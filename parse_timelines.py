"""timelines_kor/*.md → events.jsonl

각 행적 연보 파일에서 `[시기] — [사건]` 라인을 추출해
{person, year_raw, event} JSONL로 변환.
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
TIMELINES_DIR = os.path.join(BASE, 'timelines_kor')
OUT_PATH = os.path.join(BASE, 'events.jsonl')

# 라인 패턴: 시기 ` — ` 사건  (em-dash, 양쪽 공백 필수)
# 연도 범위 1978–1980 (en-dash) 같은 경우와 충돌하지 않도록 em-dash 만 허용
SEP_RE = re.compile(r'^\s*(.+?)\s+—\s+(.+?)\s*$')


def parse_file(path):
    person = os.path.basename(path)[:-3]
    events = []
    in_code = False
    with open(path, 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.rstrip('\n')
            stripped = line.strip()
            if stripped.startswith('```'):
                in_code = not in_code
                continue
            if not in_code:
                continue
            if not stripped:
                continue
            m = SEP_RE.match(stripped)
            if not m:
                continue
            year_raw = m.group(1).strip()
            event = m.group(2).strip()
            # 너무 짧은 잡음 제거
            if len(event) < 2 or len(year_raw) < 1:
                continue
            events.append({
                'person': person,
                'year_raw': year_raw,
                'event': event,
            })
    return events


def main():
    files = sorted(f for f in os.listdir(TIMELINES_DIR) if f.endswith('.md'))
    all_events = []
    per_person = {}
    for fn in files:
        path = os.path.join(TIMELINES_DIR, fn)
        evs = parse_file(path)
        per_person[fn[:-3]] = len(evs)
        all_events.extend(evs)

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        for e in all_events:
            f.write(json.dumps(e, ensure_ascii=False) + '\n')

    print(f'Total events: {len(all_events)}')
    print(f'Files: {len(files)}')
    print(f'Avg events/person: {len(all_events) / len(files):.1f}')
    print('\n5 fewest events:')
    for k, v in sorted(per_person.items(), key=lambda x: x[1])[:5]:
        print(f'  {k}: {v}')
    print('\n5 most events:')
    for k, v in sorted(per_person.items(), key=lambda x: -x[1])[:5]:
        print(f'  {k}: {v}')


if __name__ == '__main__':
    main()
