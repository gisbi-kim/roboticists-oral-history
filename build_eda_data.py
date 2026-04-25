"""profiles/*.json + events_tagged.csv → eda_data.json

EDA 탭 렌더링용 집계 데이터 한 번에 산출.
카테고리: A 인구학 / B 학력 / C 커리어 / D 직업 / E 연구 / F 학회 / G 수상 / H 창업 / I 실패 / L 한국 / M 스토리
"""
import csv
import json
import os
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
PROFILES_DIR = os.path.join(BASE, 'profiles')
EVENTS_CSV = os.path.join(BASE, 'events_tagged.csv')
OUT_PATH = os.path.join(BASE, 'eda_data.json')


SCHOOL_ALIASES = {
    'mit': 'MIT',
    'massachusetts institute of technology': 'MIT',
    'cmu': 'CMU',
    'carnegie mellon university': 'CMU',
    'carnegie mellon': 'CMU',
    'stanford': 'Stanford University',
    'stanford university': 'Stanford University',
    'berkeley': 'UC Berkeley',
    'uc berkeley': 'UC Berkeley',
    'university of california, berkeley': 'UC Berkeley',
    'university of california berkeley': 'UC Berkeley',
    'tokyo tech': 'Tokyo Institute of Technology',
    'tokyo institute of technology': 'Tokyo Institute of Technology',
    'university of tokyo': 'University of Tokyo',
    'u tokyo': 'University of Tokyo',
    'osaka university': 'Osaka University',
    'osaka u': 'Osaka University',
    'eth zurich': 'ETH Zurich',
    'eth zürich': 'ETH Zurich',
    'epfl': 'EPFL',
    'kaist': 'KAIST',
    'caltech': 'Caltech',
    'california institute of technology': 'Caltech',
    'university of pennsylvania': 'University of Pennsylvania',
    'upenn': 'University of Pennsylvania',
    'penn': 'University of Pennsylvania',
    'university of southern california': 'USC',
    'usc': 'USC',
    'georgia tech': 'Georgia Institute of Technology',
    'georgia institute of technology': 'Georgia Institute of Technology',
    'university of michigan': 'University of Michigan',
    'u michigan': 'University of Michigan',
    'university of texas at austin': 'UT Austin',
    'ut austin': 'UT Austin',
    'university of maryland': 'University of Maryland',
    'umass amherst': 'University of Massachusetts Amherst',
    'university of massachusetts amherst': 'University of Massachusetts Amherst',
    'umass': 'University of Massachusetts Amherst',
    'jpl': 'NASA JPL',
    'nasa jpl': 'NASA JPL',
    'nasa jet propulsion laboratory': 'NASA JPL',
    'jet propulsion laboratory': 'NASA JPL',
    'nasa ames': 'NASA Ames',
    'nasa ames research center': 'NASA Ames',
    'nasa johnson space center': 'NASA JSC',
    'nasa jsc': 'NASA JSC',
}


def norm_school(s):
    if not s:
        return s
    key = s.strip().lower()
    return SCHOOL_ALIASES.get(key, s.strip())


def load_profiles():
    profiles = []
    for fn in sorted(os.listdir(PROFILES_DIR)):
        if fn.endswith('.json'):
            with open(os.path.join(PROFILES_DIR, fn), 'r', encoding='utf-8') as f:
                profiles.append(json.load(f))
    return profiles


def load_events():
    rows = []
    with open(EVENTS_CSV, 'r', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def decade(y):
    if y is None:
        return None
    return (y // 10) * 10


def hist_counter(values, label='value'):
    """Counter를 [{label, count}] 리스트로."""
    c = Counter(values)
    return [{label: k, 'count': v} for k, v in sorted(c.items(),
            key=lambda x: (-x[1], str(x[0])))]


def hist_decades(values, lo=None, hi=None):
    """연도 리스트 → [{decade, count}] (None 제외, 정렬됨)."""
    decs = [decade(v) for v in values if v is not None]
    if not decs:
        return []
    c = Counter(decs)
    if lo is None: lo = min(c.keys())
    if hi is None: hi = max(c.keys())
    return [{'decade': d, 'count': c.get(d, 0)} for d in range(lo, hi + 10, 10)]


def main():
    profiles = load_profiles()
    events = load_events()
    n_people = len(profiles)
    out = {'meta': {'n_people': n_people, 'n_events': len(events)}}

    # ---------- A. 인구학 ----------
    out['A_birth_year_decades'] = hist_decades(
        [p.get('birth_year') for p in profiles])
    out['A_interview_year'] = hist_counter(
        [p.get('interview_year') for p in profiles if p.get('interview_year')],
        'year')
    out['A_gender'] = hist_counter(
        [p.get('gender') or 'unknown' for p in profiles], 'gender')
    out['A_birth_country_top'] = hist_counter(
        [p.get('birth_country') for p in profiles if p.get('birth_country')],
        'country')[:25]

    # ---------- B. 학력 ----------
    bs_fields = []
    bs_schools = []
    phd_fields = []
    phd_schools = []
    phd_advisors = []
    same_school_count = 0
    bs_phd_known = 0
    bs_to_phd_yrs = []
    edu_countries = Counter()
    for p in profiles:
        edu = p.get('education', {}) or {}
        bs = edu.get('bs') or {}
        ms = edu.get('ms') or {}
        phd = edu.get('phd') or {}
        if bs.get('field'): bs_fields.append(bs['field'])
        if bs.get('school'): bs_schools.append(norm_school(bs['school']))
        if bs.get('country'): edu_countries[bs['country']] += 1
        if ms.get('country'): edu_countries[ms['country']] += 1
        if phd.get('country'): edu_countries[phd['country']] += 1
        if phd.get('field'): phd_fields.append(phd['field'])
        if phd.get('school'): phd_schools.append(norm_school(phd['school']))
        if phd.get('advisor'): phd_advisors.append(phd['advisor'])
        if bs.get('school') and phd.get('school'):
            bs_phd_known += 1
            if norm_school(bs['school']) == norm_school(phd['school']):
                same_school_count += 1
        if bs.get('year') and phd.get('year'):
            bs_to_phd_yrs.append(phd['year'] - bs['year'])

    out['B_bs_field'] = hist_counter(bs_fields, 'field')
    out['B_phd_field'] = hist_counter(phd_fields, 'field')
    out['B_bs_school_top20'] = hist_counter(bs_schools, 'school')[:20]
    out['B_phd_school_top20'] = hist_counter(phd_schools, 'school')[:20]
    out['B_same_school_bs_phd'] = {
        'same': same_school_count,
        'different': bs_phd_known - same_school_count,
        'unknown': n_people - bs_phd_known,
    }
    out['B_bs_to_phd_years'] = sorted(bs_to_phd_yrs)
    out['B_education_countries'] = [{'country': k, 'count': v}
        for k, v in sorted(edu_countries.items(), key=lambda x: -x[1])][:25]
    out['B_phd_advisors_top'] = hist_counter(phd_advisors, 'advisor')[:20]

    # ---------- C. 커리어 ----------
    type_count = Counter(e['type'] for e in events)
    phase_count = Counter(e['phase'] for e in events)
    type_phase = Counter((e['type'], e['phase']) for e in events)
    out['C_events_per_phase'] = [{'phase': k, 'count': v}
        for k, v in phase_count.most_common()]
    out['C_events_per_type'] = [{'type': k, 'count': v}
        for k, v in type_count.most_common()]
    # 타입 × 페이즈 매트릭스
    types_order = [t for t, _ in type_count.most_common()]
    phases_order = ['k12', 'undergrad', 'grad', 'early_career', 'mid_career', 'senior']
    matrix = []
    for t in types_order:
        row = {'type': t}
        for ph in phases_order:
            row[ph] = type_phase.get((t, ph), 0)
        matrix.append(row)
    out['C_type_phase_matrix'] = {'phases': phases_order, 'rows': matrix}

    # 연도별 활동 (year_inferred 포함)
    by_year_type = defaultdict(Counter)
    by_year_total = Counter()
    for e in events:
        # year_raw에서 첫 4자리 연도 뽑기
        import re
        m = re.search(r'(18\d{2}|19\d{2}|20\d{2})', e.get('year_raw', ''))
        if not m: continue
        y = int(m.group(1))
        by_year_total[y] += 1
        by_year_type[y][e['type']] += 1
    years = sorted(by_year_total.keys())
    out['C_events_by_year'] = [{'year': y, 'count': by_year_total[y]} for y in years]
    out['C_events_by_year_type'] = {
        'years': years,
        'types': types_order,
        'series': {t: [by_year_type[y].get(t, 0) for y in years] for t in types_order}
    }

    # ---------- D. 직업 이력 ----------
    first_job_types = []
    org_counts = Counter()
    moves_per_person = []
    intl = {'same': 0, 'different': 0, 'unknown': 0}
    for p in profiles:
        fj = p.get('first_job_after_phd') or {}
        if fj.get('type'): first_job_types.append(fj['type'])
        cps = p.get('career_path') or []
        for cp in cps:
            if cp.get('org'): org_counts[norm_school(cp['org'])] += 1
        moves_per_person.append(max(0, len(cps) - 1))
        # 박사 국가 vs 첫 직장 국가
        phd_country = ((p.get('education') or {}).get('phd') or {}).get('country')
        fj_country = fj.get('country')
        if phd_country and fj_country:
            if phd_country == fj_country: intl['same'] += 1
            else: intl['different'] += 1
        else:
            intl['unknown'] += 1
    out['D_first_job_type'] = hist_counter(first_job_types, 'type')
    out['D_top_orgs'] = [{'org': k, 'count': v}
        for k, v in org_counts.most_common(25)]
    out['D_moves_per_person'] = sorted(moves_per_person)
    out['D_intl_migration_phd_to_first_job'] = intl

    # ---------- E. 연구 ----------
    topic_counts = Counter()
    topics_per_person = []
    for p in profiles:
        ts = p.get('topics') or []
        topics_per_person.append(len(ts))
        for t in ts:
            topic_counts[t.strip().lower()] += 1
    out['E_topics_top30'] = [{'topic': k, 'count': v}
        for k, v in topic_counts.most_common(30)]
    out['E_topics_per_person'] = sorted(topics_per_person)

    # 돌파(breakthrough) 시기: events_tagged에서 subtype=breakthrough
    bk_years_post_phd = []
    phd_year_by_person = {}
    for p in profiles:
        py = ((p.get('education') or {}).get('phd') or {}).get('year')
        if py: phd_year_by_person[p['person']] = py
    import re
    for e in events:
        if e.get('subtype') != 'breakthrough':
            continue
        m = re.search(r'(18\d{2}|19\d{2}|20\d{2})', e.get('year_raw', ''))
        if not m: continue
        py = phd_year_by_person.get(e['person'])
        if py is None: continue
        bk_years_post_phd.append(int(m.group(1)) - py)
    out['E_breakthrough_years_post_phd'] = sorted(bk_years_post_phd)

    # ---------- F. 학회·커뮤니티 ----------
    admin_count = Counter()
    confs_created = []
    for e in events:
        if e['subtype'] == 'admin_role':
            admin_count[e['person']] += 1
        if e['subtype'] == 'conf_create':
            confs_created.append({'person': e['person'],
                                  'event': e['event'],
                                  'year_raw': e['year_raw']})
    out['F_admin_role_count_top'] = [{'person': k, 'count': v}
        for k, v in admin_count.most_common(20)]
    out['F_conferences_created'] = confs_created[:50]

    # ---------- G. 수상·명예 ----------
    award_counts = Counter()
    award_types = Counter()
    fellow_years_post_phd = []
    for p in profiles:
        awards = p.get('awards') or []
        award_counts[p['person']] = len(awards)
        for a in awards:
            name = (a.get('name') or '').strip()
            # 표준화: "IEEE Fellow", "ASME Fellow" 등 묶기
            if 'fellow' in name.lower():
                # 첫 단어 + Fellow
                if 'ieee' in name.lower(): award_types['IEEE Fellow'] += 1
                elif 'asme' in name.lower(): award_types['ASME Fellow'] += 1
                elif 'aaai' in name.lower(): award_types['AAAI Fellow'] += 1
                elif 'aaas' in name.lower(): award_types['AAAS Fellow'] += 1
                elif 'acm' in name.lower(): award_types['ACM Fellow'] += 1
                else: award_types[name] += 1
            elif 'pioneer' in name.lower():
                award_types['IEEE Pioneer Award'] += 1
            elif 'engelberger' in name.lower():
                award_types['Engelberger Robotics Award'] += 1
            elif 'turing' in name.lower():
                award_types['Turing Award'] += 1
            else:
                award_types[name] += 1
            # IEEE Fellow 경우, year - phd_year
            if 'ieee fellow' in name.lower() and a.get('year'):
                py = ((p.get('education') or {}).get('phd') or {}).get('year')
                if py: fellow_years_post_phd.append(a['year'] - py)
    # Top awarded persons
    out['G_award_count_top'] = [{'person': k, 'count': v}
        for k, v in award_counts.most_common(25) if v > 0]
    out['G_award_types_top'] = [{'name': k, 'count': v}
        for k, v in award_types.most_common(25)]
    out['G_ieee_fellow_years_post_phd'] = sorted(fellow_years_post_phd)

    # ---------- H. 창업·산업 ----------
    founded_count = 0
    companies_all = []
    serial_founders = []
    for p in profiles:
        cf = p.get('companies_founded') or []
        if cf:
            founded_count += 1
            for c in cf:
                companies_all.append({'person': p['person'],
                                       'name': c.get('name'),
                                       'year': c.get('year')})
        if len(cf) >= 2:
            serial_founders.append({'person': p['person'],
                                    'full_name': p.get('full_name'),
                                    'count': len(cf),
                                    'companies': [c.get('name') for c in cf]})
    out['H_founded_pct'] = {'founded': founded_count, 'not': n_people - founded_count}
    out['H_companies_all'] = companies_all
    out['H_serial_founders'] = sorted(serial_founders, key=lambda x: -x['count'])

    # ---------- I. 실패·전환 ----------
    setback_subtypes = Counter()
    pivot_persons = Counter()
    for e in events:
        if e['type'] == '실패·전환':
            setback_subtypes[e['subtype']] += 1
            if e['subtype'] == 'pivot':
                pivot_persons[e['person']] += 1
    out['I_setback_subtypes'] = [{'subtype': k, 'count': v}
        for k, v in setback_subtypes.most_common()]
    persons_with_setback = len(set(e['person'] for e in events
                                   if e['type'] == '실패·전환'))
    out['I_persons_with_setback'] = {
        'with': persons_with_setback,
        'without': n_people - persons_with_setback,
    }
    out['I_pivot_top'] = [{'person': k, 'count': v}
        for k, v in pivot_persons.most_common(15)]

    # ---------- J. 외부 영향 ----------
    ext_mentions = Counter()
    for p in profiles:
        for ex in (p.get('external_events_mentioned') or []):
            ext_mentions[ex] += 1
    out['J_external_events'] = [{'event': k, 'count': v}
        for k, v in ext_mentions.most_common(20)]

    # ---------- L. 한국 / 아시아 ----------
    korean = [p for p in profiles if p.get('birth_country') == 'South Korea']
    japanese = [p for p in profiles if p.get('birth_country') == 'Japan']
    chinese = [p for p in profiles if p.get('birth_country') == 'China']
    out['L_korean_pioneers'] = [{
        'person': p['person'], 'full_name': p.get('full_name'),
        'birth_year': p.get('birth_year'),
        'phd': ((p.get('education') or {}).get('phd') or {}).get('school'),
        'topics': p.get('topics', []),
    } for p in korean]
    out['L_country_subset_counts'] = {
        'South Korea': len(korean),
        'Japan': len(japanese),
        'China': len(chinese),
    }

    # ---------- M. 스토리 ----------
    # 최장 한 직장
    longest_tenure = []
    for p in profiles:
        for cp in (p.get('career_path') or []):
            ys, ye = cp.get('year_start'), cp.get('year_end')
            if ys and ye and (ye - ys) >= 20:
                longest_tenure.append({
                    'person': p['person'],
                    'full_name': p.get('full_name'),
                    'org': cp.get('org'),
                    'years': ye - ys,
                    'period': f"{ys}-{ye}",
                })
            elif ys and ye is None:
                # 인터뷰 시점까지 진행 중. interview_year로 cap
                iy = p.get('interview_year') or 2015
                if iy - ys >= 20:
                    longest_tenure.append({
                        'person': p['person'],
                        'full_name': p.get('full_name'),
                        'org': cp.get('org'),
                        'years': iy - ys,
                        'period': f"{ys}-",
                    })
    out['M_longest_tenure_top'] = sorted(longest_tenure, key=lambda x: -x['years'])[:20]

    # 가장 다양한 커리어 (이벤트 타입 엔트로피)
    import math
    person_type_dist = defaultdict(Counter)
    for e in events:
        person_type_dist[e['person']][e['type']] += 1
    diversity = []
    for person, c in person_type_dist.items():
        total = sum(c.values())
        if total < 5: continue
        H = -sum((v/total) * math.log2(v/total) for v in c.values() if v > 0)
        # full name lookup
        fn = next((p.get('full_name') for p in profiles if p['person'] == person), person)
        diversity.append({'person': person, 'full_name': fn,
                         'entropy': round(H, 3),
                         'type_count': len(c),
                         'total_events': total})
    out['M_most_diverse_career_top'] = sorted(diversity,
        key=lambda x: -x['entropy'])[:15]

    # 가장 늦게 박사
    latest_phd = []
    for p in profiles:
        phd = (p.get('education') or {}).get('phd') or {}
        if phd.get('year') and p.get('birth_year'):
            age = phd['year'] - p['birth_year']
            latest_phd.append({
                'person': p['person'], 'full_name': p.get('full_name'),
                'phd_year': phd['year'], 'birth_year': p['birth_year'],
                'age': age,
            })
    out['M_latest_phd_age_top'] = sorted(latest_phd, key=lambda x: -x['age'])[:10]
    out['M_youngest_phd_age_top'] = sorted(latest_phd, key=lambda x: x['age'])[:10]

    # 시리얼 창업가는 H 섹션에 이미 있음

    # 최다 이벤트 인물
    person_event_count = Counter(e['person'] for e in events)
    out['M_most_documented_lives'] = [{
        'person': k,
        'full_name': next((p.get('full_name') for p in profiles if p['person'] == k), k),
        'count': v
    } for k, v in person_event_count.most_common(15)]

    # ---------- 저장 ----------
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=None, separators=(',', ':'))

    print(f'eda_data.json: {os.path.getsize(OUT_PATH)/1024:.1f} KB')
    print(f'  meta: {out["meta"]}')
    print(f'  birth decades: {out["A_birth_year_decades"]}')
    print(f'  bs_field top 5: {out["B_bs_field"][:5]}')
    print(f'  phd_field top 5: {out["B_phd_field"][:5]}')
    print(f'  phd_school top 5: {out["B_phd_school_top20"][:5]}')
    print(f'  topics top 10: {out["E_topics_top30"][:10]}')
    print(f'  founded company: {out["H_founded_pct"]}')
    print(f'  korean: {out["L_country_subset_counts"]}')


if __name__ == '__main__':
    main()
