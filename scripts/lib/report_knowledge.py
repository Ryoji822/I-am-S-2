"""Persistent report sections, independent of daily news and forecast scoring."""

import copy
import json
import posixpath
import re
from zoneinfo import ZoneInfo

from .forecast_contract import instant, require

SUBJECTS = ('openai', 'anthropic', 'google', 'xai', 'bytedance', 'market-overview', 'scenario-tracker')


def load_dossiers(root, now):
    day = instant(now).astimezone(ZoneInfo('Asia/Tokyo')).date().isoformat()
    dossiers = {subject: json.loads((root / 'config/dossiers' / f'{subject}.json').read_text())
                for subject in SUBJECTS}
    require(all(d['available_on'] <= day for d in dossiers.values()), 'dossier baseline is from the future')
    validate_dossiers(dossiers)
    return dossiers


def validate_dossiers(dossiers):
    require(set(dossiers) == set(SUBJECTS), 'all five companies and two cross-company reports required')
    for subject, dossier in dossiers.items():
        require(dossier['subject'] == subject and bool(dossier['title']), 'invalid dossier identity')
        sections = dossier['sections']
        ids = [section['id'] for section in sections]
        require(len(ids) == len(set(ids)), 'duplicate dossier section')
        require(set(ids) == set(dossier['required_sections']), 'dossier coverage was removed')
        require(bool(sections), 'empty dossier')
        for section in sections:
            require(all(isinstance(section[key], str) and section[key].strip()
                        for key in ['id', 'title', 'body']), 'empty report section')
        require(any('https://' in section['body'] for section in sections), 'dossier needs sources')


def collection_index(dossiers):
    """Give the collector navigation, while analysis and rendering retain full text."""
    return {subject: {'title': dossier['title'], 'available_on': dossier['available_on'],
                     'overview': dossier['sections'][0]['body'].split('\n\n')[0],
                     'scope': '収集用索引。分析・反証・出力には別途全文を渡す。',
                     'sections': [{'id': section['id'], 'title': section['title'],
                                   'record_id': section.get('record_id'),
                                   'reviewed_at': section.get('reviewed_at'),
                                   'source_urls': sorted(set(re.findall(r'https://[^\s)]+', section['body'])))}
                                  for section in dossier['sections']]}
            for subject, dossier in dossiers.items()}


def merge_dossiers(baseline, state, now):
    dossiers = copy.deepcopy(baseline)
    updates = sorted(state['records']['dossier_section'].values(), key=lambda row: (instant(row['reviewed_at']), row['id']))
    for update in updates:
        if instant(update['reviewed_at']) > instant(now):
            continue
        dossier = dossiers[update['subject']]
        require(update['section'] in dossier['required_sections'], 'unknown dossier section')
        dossier['sections'] = [updated_section(section, update, state) if section['id'] == update['section'] else section
                               for section in dossier['sections']]
    validate_dossiers(dossiers)
    return dossiers


def citation_urls(text):
    return set(re.findall(r'https://[^\s)]+', text or ''))


def citations_are_reviewed(section, update, records):
    """Exact URL match. Another section's citations do not review this one."""
    sources = [records['evidence'][identifier] for identifier in update['evidence_ids']]
    allowed = citation_urls(section['body']) | {source['url'] for source in sources}
    return citation_urls(update['body']) <= allowed


def updated_section(section, update, state):
    require(citations_are_reviewed(section, update, state['records']), 'unreviewed dossier citation')
    sources = [state['records']['evidence'][identifier] for identifier in update['evidence_ids']]
    return {**section, 'body': update['body'], 'analysis': update['analysis'],
            'uncertainty': update['uncertainty'], 'record_id': update['id'],
            'reviewed_at': update['reviewed_at'], 'sources': sources}


def partition_dossier_updates(baseline, state, updates, now):
    """Split section updates into publishable and withheld.

    Withheld updates are not applied. A later update that supersedes one of them
    is withheld too, so an unreviewed revision cannot parent a published one.
    """
    dropped = []
    remaining = list(updates)
    while remaining:
        dossiers = merge_dossiers(baseline, state, now)
        kept, failed = [], []
        blocked = {record['id'] for record in dropped}
        for update in sorted(remaining, key=lambda row: (instant(row['reviewed_at']), row['id'])):
            blocked.update(record['id'] for record in failed)
            if update.get('supersedes') in blocked:
                failed.append(update)
                continue
            dossier = dossiers[update['subject']]
            require(update['section'] in dossier['required_sections'], 'unknown dossier section')
            section = next(item for item in dossier['sections'] if item['id'] == update['section'])
            if not citations_are_reviewed(section, update, state['records']):
                failed.append(update)
                continue
            kept.append(update)
            dossier['sections'] = [updated_section(item, update, state) if item['id'] == update['section'] else item
                                   for item in dossier['sections']]
        if not failed:
            return kept, dropped
        dropped.extend(failed)
        remaining = kept
    return [], dropped


def dossier_text(dossier, heading=1):
    lines = ['#' * heading + ' ' + dossier['title'], '', dossier['introduction'], '']
    for section in dossier['sections']:
        lines += ['#' * (heading + 1) + ' ' + section['title'], '', section['body'], '']
        if section.get('record_id'):
            lines += [section['analysis'], '', '残る限界：' + section['uncertainty'], '',
                      f"確認更新：{section['reviewed_at']}（{section['record_id']}）。", '']
    return '\n'.join(lines)


def relocate_links(text, target_directory):
    """Dossier bodies use links relative to static_intelligence, including in shadow."""
    def replacement(match):
        label, url = match.groups()
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', url) or url.startswith(('#', '/')):
            return match.group(0)
        path = posixpath.normpath(posixpath.join('static_intelligence', url))
        if target_directory.startswith('state/shadow/') and path.startswith('static_intelligence/'):
            path = posixpath.join('state/shadow', path)
        return f'[{label}]({posixpath.relpath(path, target_directory)})'
    return re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', replacement, text)
