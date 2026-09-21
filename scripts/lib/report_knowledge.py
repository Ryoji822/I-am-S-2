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


def updated_section(section, update, state):
    sources = [state['records']['evidence'][identifier] for identifier in update['evidence_ids']]
    prior_urls = set(re.findall(r'https://[^\s)]+', section['body']))
    allowed = prior_urls | {source['url'] for source in sources}
    require(set(re.findall(r'https://[^\s)]+', update['body'])) <= allowed, 'unreviewed dossier citation')
    return {**section, 'body': update['body'], 'analysis': update['analysis'],
            'uncertainty': update['uncertainty'], 'record_id': update['id'],
            'reviewed_at': update['reviewed_at'], 'sources': sources}


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
