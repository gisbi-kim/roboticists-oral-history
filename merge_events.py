"""events_tagged/batch_*.jsonl → events_tagged.jsonl + events_tagged.csv

11개 배치 결과를 병합·검증·CSV 변환.
"""
import csv
import glob
import json
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
TAGGED_DIR = os.path.join(BASE, 'events_tagged')
OUT_JSONL = os.path.join(BASE, 'events_tagged.jsonl')
OUT_CSV = os.path.join(BASE, 'events_tagged.csv')

VALID_PHASES = {'k12', 'undergrad', 'grad', 'early_career', 'mid_career', 'senior'}
VALID_TYPES = {'개인사', '교육', '직업 이력', '연구·프로젝트', '창업·산업',
               '학회·커뮤니티', '수상·명예', '네트워크', '실패·전환', '외부 영향'}


def main():
    rows = []
    invalid = []
    for path in sorted(glob.glob(os.path.join(TAGGED_DIR, 'batch_*.jsonl'))):
        with open(path, 'r', encoding='utf-8') as f:
            for ln, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    invalid.append((path, ln, f'JSON: {e}'))
                    continue
                # 검증
                missing = [k for k in ('person', 'year_raw', 'event', 'type', 'subtype', 'phase')
                           if k not in obj]
                if missing:
                    invalid.append((path, ln, f'missing: {missing}'))
                    continue
                if obj['phase'] not in VALID_PHASES:
                    invalid.append((path, ln, f'phase invalid: {obj["phase"]}'))
                if obj['type'] not in VALID_TYPES:
                    invalid.append((path, ln, f'type invalid: {obj["type"]}'))
                rows.append(obj)

    # JSONL 병합
    with open(OUT_JSONL, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

    # CSV
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['person', 'year_raw', 'event',
                                          'type', 'subtype', 'phase'])
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # 통계
    print(f'총 이벤트: {len(rows)}')
    print(f'인물 수: {len(set(r["person"] for r in rows))}')
    print(f'유효성 오류: {len(invalid)}')
    if invalid:
        for v in invalid[:10]:
            print(f'  {v}')

    print('\n=== 타입 분포 ===')
    for k, v in Counter(r['type'] for r in rows).most_common():
        print(f'  {k:20s} {v:5d} ({v/len(rows)*100:5.1f}%)')

    print('\n=== 페이즈 분포 ===')
    for k, v in Counter(r['phase'] for r in rows).most_common():
        print(f'  {k:15s} {v:5d} ({v/len(rows)*100:5.1f}%)')

    print('\n=== 상위 서브타입 (15개) ===')
    for k, v in Counter(r['subtype'] for r in rows).most_common(15):
        print(f'  {k:25s} {v:5d}')


if __name__ == '__main__':
    main()
