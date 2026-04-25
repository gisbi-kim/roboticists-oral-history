"""events_tagged.csv + timelines_kor/*.md → viz_data.json

각 이벤트에 다음을 부착:
- year (정수, 추출 가능한 경우만)
- line_no (timeline_kor 파일 내 라인 번호)
- 인물별 birth_year (정렬용)
"""
import csv
import json
import os
import re
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, 'events_tagged.csv')
TIMELINES_DIR = os.path.join(BASE, 'timelines_kor')
OUT_PATH = os.path.join(BASE, 'viz_data.json')

YEAR_RE = re.compile(r'\b(18\d{2}|19\d{2}|20\d{2})\b')
SEP_RE = re.compile(r'^\s*(.+?)\s+—\s+(.+?)\s*$')


def extract_year(year_raw: str):
    m = YEAR_RE.search(year_raw)
    if not m:
        return None
    y = int(m.group(1))
    # "1990년대 후반"·"late 1990s" → +7
    # "1990년대 중반" → +5
    # "1990년대 초반" → +2
    if '후반' in year_raw or 'late' in year_raw.lower():
        y += 7
    elif '중반' in year_raw or 'mid' in year_raw.lower():
        y += 5
    elif '초반' in year_raw or 'early' in year_raw.lower():
        y += 2
    return y


def normalize(s: str) -> str:
    """매칭용 정규화: 공백/대시/구두점 정리."""
    s = s.replace('–', '-').replace('—', '-')
    s = re.sub(r'\s+', '', s)
    return s


def build_line_map(person):
    """timelines_kor/{person}.md를 읽어 정규화한 (year_raw, event) → line_no 매핑."""
    path = os.path.join(TIMELINES_DIR, f'{person}.md')
    mapping = {}
    in_code = False
    with open(path, 'r', encoding='utf-8') as f:
        for ln, raw in enumerate(f, 1):
            line = raw.strip()
            if line.startswith('```'):
                in_code = not in_code
                continue
            if not in_code or not line:
                continue
            m = SEP_RE.match(line)
            if not m:
                continue
            year_raw = m.group(1).strip()
            event = m.group(2).strip()
            mapping[(normalize(year_raw), normalize(event))] = ln
            # event 단독 매칭(연도 표기 차이 흡수)
            mapping.setdefault(('', normalize(event)), ln)
    return mapping


def parse_timeline_order(person):
    """timelines_kor/{person}.md를 읽어 라인 순서대로 (line_no, year_raw, event, year)
    리스트 반환. timeline 파일이 chronological order의 진실 소스."""
    path = os.path.join(TIMELINES_DIR, f'{person}.md')
    out = []
    in_code = False
    with open(path, 'r', encoding='utf-8') as f:
        for ln, raw in enumerate(f, 1):
            line = raw.strip()
            if line.startswith('```'):
                in_code = not in_code
                continue
            if not in_code or not line:
                continue
            m = SEP_RE.match(line)
            if not m:
                continue
            year_raw = m.group(1).strip()
            event = m.group(2).strip()
            year = extract_year(year_raw)
            out.append({'line_no': ln, 'year_raw': year_raw,
                        'event': event, 'year': year})
    return out


FULL_NAME_RE = re.compile(r'^#\s*(.+?)\s*[—–-]\s*행적')


def get_full_name(person):
    path = os.path.join(TIMELINES_DIR, f'{person}.md')
    with open(path, 'r', encoding='utf-8') as f:
        first = f.readline().strip()
    m = FULL_NAME_RE.match(first)
    return m.group(1).strip() if m else person


def main():
    # 인물별 line map + 풀네임
    line_maps = {}
    full_names = {}
    for fn in os.listdir(TIMELINES_DIR):
        if fn.endswith('.md'):
            person = fn[:-3]
            line_maps[person] = build_line_map(person)
            full_names[person] = get_full_name(person)

    # CSV 로드 + 부착
    events = []
    person_birth = {}
    person_events = defaultdict(int)
    miss_line = 0
    miss_year = 0
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for csv_idx, row in enumerate(reader):
            person = row['person']
            year_raw = row['year_raw']
            event = row['event']
            year = extract_year(year_raw)
            lm = line_maps.get(person, {})
            key = (normalize(year_raw), normalize(event))
            line_no = lm.get(key) or lm.get(('', normalize(event)))
            if year is None:
                miss_year += 1
            if line_no is None:
                miss_line += 1
            # birth year 추출
            if row['subtype'] == 'birth' and year is not None:
                if person not in person_birth or year < person_birth[person]:
                    person_birth[person] = year
            person_events[person] += 1
            events.append({
                'person': person,
                'year_raw': year_raw,
                'year': year,
                'year_inferred': False,
                'event': event,
                'type': row['type'],
                'subtype': row['subtype'],
                'phase': row['phase'],
                'line_no': line_no,
                '_csv_idx': csv_idx,
            })

    # 연도 추론: timeline 파일의 라인 순서가 진실. 인물별 [min~max known] 안에서만.
    # 1) 인물별 timeline-order 리스트로 보간 결과 산출
    # 2) tagged event를 (year_raw_norm, event_norm)로 매칭해서 추론된 year 부착
    inferred_by_key = {}  # (person, year_raw_norm, event_norm) → year
    for person in line_maps.keys():
        order = parse_timeline_order(person)
        if not order:
            continue
        years = [r['year'] for r in order]
        known = [y for y in years if y is not None]
        if not known:
            continue  # 추론 불가
        y_min, y_max = min(known), max(known)
        n = len(order)
        for i in range(n):
            if years[i] is not None:
                continue
            # 앞뒤 known 찾기
            p_idx, p_y = None, None
            for j in range(i - 1, -1, -1):
                if years[j] is not None:
                    p_idx, p_y = j, years[j]
                    break
            s_idx, s_y = None, None
            for j in range(i + 1, n):
                if years[j] is not None:
                    s_idx, s_y = j, years[j]
                    break
            if p_y is not None and s_y is not None:
                ratio = (i - p_idx) / (s_idx - p_idx)
                inferred_year = round(p_y + (s_y - p_y) * ratio)
            elif p_y is not None:
                # 외삽 금지: 마지막 known에 그대로 붙임
                inferred_year = p_y
            elif s_y is not None:
                inferred_year = s_y
            else:
                continue
            # 인물 범위 안으로 클램프
            inferred_year = max(y_min, min(y_max, inferred_year))
            order[i]['year'] = inferred_year
            key = (person, normalize(order[i]['year_raw']),
                   normalize(order[i]['event']))
            inferred_by_key[key] = inferred_year

    # tagged event에 추론 결과 부착
    inferred = 0
    for e in events:
        if e['year'] is not None:
            continue
        key = (e['person'], normalize(e['year_raw']), normalize(e['event']))
        if key in inferred_by_key:
            e['year'] = inferred_by_key[key]
            e['year_inferred'] = True
            inferred += 1

    # _csv_idx 제거
    for e in events:
        e.pop('_csv_idx', None)

    # 인물 메타데이터
    persons = sorted(set(e['person'] for e in events))
    person_meta = {
        p: {
            'full_name': full_names.get(p, p),
            'birth_year': person_birth.get(p),
            'event_count': person_events[p],
        }
        for p in persons
    }

    # 통계 (보간 결과 포함)
    years_all = [e['year'] for e in events if e['year'] is not None]

    out = {
        'persons': person_meta,
        'events': events,
        'year_min': min(years_all) if years_all else None,
        'year_max': max(years_all) if years_all else None,
    }
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=None, separators=(',', ':'))

    print(f'총 이벤트: {len(events)}')
    print(f'인물 수: {len(persons)}')
    print(f'birth_year 추출됨: {len(person_birth)} / {len(persons)}')
    print(f'year 직접 추출: {len(events) - miss_year}')
    print(f'year 보간 추론: {inferred}')
    print(f'year 결국 미상: {miss_year - inferred}')
    print(f'line_no 매핑 실패: {miss_line}')
    print(f'연도 범위: {out["year_min"]} ~ {out["year_max"]}')
    print(f'출력: {OUT_PATH} ({os.path.getsize(OUT_PATH)/1024:.1f} KB)')


if __name__ == '__main__':
    main()
