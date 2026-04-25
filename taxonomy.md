# 행적(Event) 분류 체계 (Taxonomy)

110명의 행적 연보(`timelines_kor/`)에서 추출한 모든 사건을 두 축으로 태깅한다.

- **타입** (대분류 + 소분류) — 사건의 *성격*
- **페이즈** (커리어 단계) — 사건이 일어난 *시점*

두 축은 직교한다. 예: "ICRA 베스트페이퍼 후보" = `수상·명예 / 학회상` × `신임 교수`

---

## 1. 타입 (Type)

### 1.1 개인사 (Personal)
- `birth` — 출생
- `marriage` — 결혼
- `family` — 가족 사건 (출산, 사별 등)
- `relocation` — 이주 (가족 단위, 어린 시절)
- `death` — 사망
- `personal_other` — 기타 사적 사건

### 1.2 교육 (Education)
- `k12_enroll` — 초중등 입학·재학
- `k12_graduate` — 초중등 졸업
- `bs_enroll` — 학사 입학
- `bs_major` — 학부 전공·세부전공 선택
- `bs_graduate` — 학사 졸업
- `ms_enroll` — 석사 입학
- `ms_graduate` — 석사 졸업
- `phd_enroll` — 박사 입학
- `phd_advisor` — 박사 지도교수 결정
- `phd_thesis` — 박사 학위논문 주제·돌파
- `phd_graduate` — 박사 학위 취득
- `postdoc` — 박사후 시작·종료
- `sabbatical_visit` — 안식년·방문학자

### 1.3 직업 이력 (Career)
- `hire` — 입사·임용 (조교수, 연구원 등 첫 임명)
- `promotion` — 승진 (부교수, 정교수 등)
- `admin_role` — 보직 (학과장, 디렉터, 학장)
- `move` — 이직·기관 이동
- `retire` — 은퇴
- `emeritus` — 명예교수·명예직 추대

### 1.4 연구·프로젝트 (Research)
- `proj_start` — 프로젝트 시작
- `breakthrough` — 기술 돌파·발견·핵심 아이디어
- `demo` — 시연·데모
- `paper` — 주요 논문 발표·출판
- `proj_complete` — 프로젝트 완료
- `next_gen` — 후속 버전·세대 (예: Robonaut R1 → R2)

### 1.5 창업·산업 (Industry)
- `company_found` — 회사 설립
- `industry_collab` — 산업 협업·컨설팅
- `commercialize` — 상품화·판매
- `exit` — 회사 매각·IPO
- `company_close` — 회사 종료

### 1.6 학회·커뮤니티 (Community)
- `conf_create` — 학회·컨퍼런스 창설
- `editorship` — 학회/저널 의장·편집장
- `committee` — 위원회·이사회 활동
- `conf_attend` — 주요 컨퍼런스 참가·발표 (특별히 언급된 경우)
- `standards` — 표준화 활동

### 1.7 수상·명예 (Honors)
- `paper_award` — 학회상 (Best Paper, Test of Time 등)
- `lifetime_award` — 평생공로상 (Pioneer Award, Engelberger 등)
- `fellow` — 펠로우 추대 (IEEE Fellow, ASME Fellow 등)
- `gov_honor` — 정부 훈장·표창
- `honorary_degree` — 명예 학위·명예 교수직

### 1.8 네트워크 (Network)
- `mentor_meet` — 멘토·지도교수와의 만남
- `collab_start` — 협업 시작
- `influence` — 영향받은 인물·문헌
- `student_notable` — 특별히 언급된 학생 배출

### 1.9 실패·전환 (Setback / Pivot)
- `proj_fail` — 프로젝트 무산·실패
- `rejected` — 논문/제안 거절
- `forced_move` — 외부 요인에 의한 부서·기관 이동
- `pivot` — 분야 전환
- `funding_crisis` — 재정·예산 위기

### 1.10 외부 영향 (External)
- `war` — 전쟁
- `policy` — 정부 정책 변화
- `social_movement` — 사회 운동 (예: 학생 운동)
- `field_crisis` — 분야 위기 (AI winter 등)
- `disaster` — 자연재해

---

## 2. 페이즈 (Career Phase)

인물·분야 막론하고 6단계로 고정.

| 페이즈 | 코드 | 정의 |
|---|---|---|
| 학창 시절 | `k12` | 출생부터 고등학교 졸업까지 |
| 학부생 시절 | `undergrad` | 학사 과정 재학 중 |
| 대학원생 시절 | `grad` | 석사·박사 과정 재학 중 |
| 박사후·신임 | `early_career` | 박사 학위 취득 후 ~ 정교수 승진 전 (postdoc, assistant prof, junior researcher) |
| 중견 | `mid_career` | 정교수·시니어 연구원 ~ 분야 리더 인정받기 전 |
| 시니어/원로 | `senior` | 분야 리더, 학회 회장, 평생공로상 수상 이후, 은퇴·명예직 포함 |

> 페이즈 판단 기준은 인터뷰 시점이 아니라 **사건 발생 시점의 본인 신분**.
> 예: 1991년 박사 취득 직후 NASA 입사 → `early_career`. 1999년 프로젝트 리더로 승진 → `mid_career`.

---

## 3. 출력 스키마

```jsonl
{"person": "ambrose", "year_raw": "1991", "event": "박사 학위 취득", "type": "교육", "subtype": "phd_graduate", "phase": "grad"}
{"person": "ambrose", "year_raw": "1991", "event": "NASA 존슨 우주 센터 입사 (계약직)", "type": "직업 이력", "subtype": "hire", "phase": "early_career"}
{"person": "ambrose", "year_raw": "1996", "event": "로보노트 프로젝트 시작", "type": "연구·프로젝트", "subtype": "proj_start", "phase": "early_career"}
```

CSV 출력은 동일 컬럼 (`person, year_raw, event, type, subtype, phase`).

---

## 4. 분류 가이드 (모호한 케이스)

- **여러 타입에 걸치는 경우**: 가장 두드러진 한 가지로 분류. 필요 시 보조 메모.
- **연도 미상**: `year_raw`는 원문 표현 그대로 (`"학부 시절"`, `"1990년대 후반"`).
- **인터뷰 시점 사건**: 대개 `senior` 페이즈. 단, 인터뷰 당시가 신임교수면 그에 맞춰.
- **수상 vs 명예직**: IEEE Fellow는 `fellow`, 명예교수는 `emeritus` 또는 `honorary_degree`로 구분.
- **창업 vs 협업**: 본인이 설립한 회사는 `company_found`, 자문/협업은 `industry_collab`.
