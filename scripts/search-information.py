#!/usr/bin/env python3
"""Search old Information records without rewriting their format or originals."""
import argparse
import json
from pathlib import Path
from lib.legacy_information import SUBJECT_TERMS, search_information

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--company', choices=SUBJECT_TERMS)
    parser.add_argument('--before', help='Inclusive collection date, YYYY-MM-DD')
    parser.add_argument('--after', help='Inclusive collection date, YYYY-MM-DD')
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    result = search_information(Path(__file__).resolve().parents[1], args.query, args.company,
                                args.before, args.after, args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2))
