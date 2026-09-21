"""Read-only lookup over legacy evidence. Never upgrades old claims to new facts."""

import json
from datetime import date, datetime
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

SUBJECT_TERMS = {'openai': ('openai', 'chatgpt', 'codex'),
                 'anthropic': ('anthropic', 'claude'), 'google': ('google', 'gemini', 'deepmind'),
                 'xai': ('x.ai', 'xai', 'grok', 'spacex'),
                 'bytedance': ('bytedance', 'doubao', 'seedance', 'seed2', 'coze', '字節', '豆包')}


def adapted(row, path, line):
    url = row.get('source_url', '')
    parsed = urlparse(url)
    if parsed.scheme not in {'http', 'https'} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('unusable source URL')
    return {'id': row['evidence_id'], 'legacy_info_id': row.get('legacy_info_id'),
            'source_url': url, 'source_title': row.get('source_title', ''),
            'summary': row.get('summary_for_indexing', row.get('quotable_excerpt', ''))[:800],
            'run_date': row['run_date'], 'retrieved_at': row.get('retrieved_at'),
            'published_at': None, 'trust': 'legacy_unverified',
            'legacy_source_type': row.get('source_type'), 'degraded': row.get('degraded', False),
            'content_hash': row.get('content_hash'), 'raw_path': row.get('raw_path'),
            'record_path': path, 'line': line}


def selected(row, query, subject, before, after):
    run_date = date.fromisoformat(row['run_date']).isoformat()
    retrieved = datetime.fromisoformat(row['retrieved_at'].replace('Z', '+00:00')) if row.get('retrieved_at') else None
    retrieved_day = retrieved.astimezone(ZoneInfo('Asia/Tokyo')).date().isoformat() if retrieved and retrieved.tzinfo else run_date
    if before and (run_date > before or retrieved_day > before):
        return False
    if after and run_date < after:
        return False
    text = ' '.join(str(row.get(key, '')) for key in ['evidence_id', 'legacy_info_id', 'source_url',
                                                      'source_title', 'summary_for_indexing']).lower()
    return query.lower() in text and (not subject or any(term in text for term in SUBJECT_TERMS[subject]))


def search_information(root, query='', subject=None, before=None, after=None, limit=20):
    if subject is not None and subject not in SUBJECT_TERMS:
        raise ValueError('unknown company')
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError('limit must be between 1 and 100')
    for value in [before, after]:
        if value:
            date.fromisoformat(value)
    items, errors, matches = [], [], 0
    for path in sorted((root / 'Information/processed').glob('*.jsonl'), reverse=True):
        relative = path.relative_to(root).as_posix()
        for line, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not raw.strip():
                continue
            try:
                row = json.loads(raw)
                if selected(row, query, subject, before, after):
                    item = adapted(row, relative, line)
                    matches += 1
                    if len(items) < limit:
                        items.append(item)
            except (KeyError, TypeError, ValueError, AttributeError):
                errors.append({'record_path': relative, 'line': line, 'error': 'invalid legacy record'})
    return {'items': items, 'matches': matches, 'truncated': matches > limit, 'errors': errors,
            'note': '原本は変更していません。公開日時・主張・ソース分類は再確認が必要です。検索ヒット数は独立した事象数ではありません。'}


def historical_context(root, now):
    day = datetime.fromisoformat(now.replace('Z', '+00:00')).astimezone(ZoneInfo('Asia/Tokyo')).date().isoformat()
    results = {subject: search_information(root, subject=subject, before=day, limit=3)
               for subject in SUBJECT_TERMS}
    return {'companies': results, 'scope': '会社ごと直近3件。旧情報は探索の入口。新規証拠には原資料の再検証が必要。'}
