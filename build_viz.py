"""viz_data.json + 템플릿 → visualization.html (자체 포함, KO/EN 토글)."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, 'viz_data.json')
EDA_PATH = os.path.join(BASE, 'eda_data.json')
OUT_PATH = os.path.join(BASE, 'visualization.html')

REPO = 'https://github.com/gisbi-kim/roboticists-oral-history'

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>Roboticists Oral History — Career Timeline</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
:root {
  --bg: #fafafa;
  --fg: #222;
  --muted: #777;
  --border: #e5e5e5;
  --row-h: 14px;
  --col-w: 7px;
  --name-w: 280px;
  --year-h: 28px;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: -apple-system, "Helvetica Neue", "Apple SD Gothic Neo", sans-serif;
       background: var(--bg); color: var(--fg); font-size: 13px; }
header { padding: 12px 18px; border-bottom: 1px solid var(--border); background: #fff;
         display: flex; justify-content: space-between; align-items: flex-start; }
.title h1 { margin: 0 0 4px; font-size: 16px; }
.sub { color: var(--muted); font-size: 12px; }
.lang-toggle { display: flex; gap: 0; border: 1px solid var(--border); border-radius: 4px;
               overflow: hidden; }
.lang-toggle button { border: 0; background: #fff; padding: 6px 14px; font-size: 12px;
                     cursor: pointer; font-weight: 500; color: var(--muted); }
.lang-toggle button.active { background: #222; color: #fff; }
.lang-toggle button:not(.active):hover { background: #f0f0f0; }

/* 탭 */
.tabs { display: flex; gap: 0; border-bottom: 1px solid var(--border); background: #fff;
        padding: 0 18px; }
.tab-btn { border: 0; background: transparent; padding: 10px 16px; font-size: 13px;
           cursor: pointer; color: var(--muted); border-bottom: 2px solid transparent;
           font-weight: 500; }
.tab-btn.active { color: var(--fg); border-bottom-color: #222; }
.tab-btn:hover:not(.active) { color: var(--fg); }
.tab-pane { display: none; }
.tab-pane.active { display: block; }

/* EDA */
.eda { padding: 20px 24px; max-width: 1500px; margin: 0 auto; }
.eda h2 { font-size: 15px; margin: 24px 0 8px; padding-bottom: 4px;
          border-bottom: 1px solid var(--border); }
.eda h2:first-child { margin-top: 0; }
.eda h2 .en { color: var(--muted); font-weight: normal; font-size: 13px; margin-left: 6px; }
.eda-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 16px; margin-bottom: 8px; }
.eda-card { background: #fff; border: 1px solid var(--border); border-radius: 6px;
            padding: 12px 14px; }
.eda-card.wide { grid-column: 1 / -1; }
.eda-card h3 { margin: 0 0 8px; font-size: 13px; color: var(--fg); }
.eda-card .chart-wrap { position: relative; height: 240px; }
.eda-card .chart-wrap.tall { height: 380px; }
.eda-card.wide .chart-wrap { height: 320px; }
.eda-card ul { padding-left: 18px; margin: 0; font-size: 12px; line-height: 1.7; }
.eda-card table { width: 100%; font-size: 12px; border-collapse: collapse; }
.eda-card th, .eda-card td { padding: 4px 6px; border-bottom: 1px solid #f0f0f0;
                              text-align: left; }
.eda-card th { background: #f8f8f8; font-weight: 600; }
.matrix { font-size: 11px; }
.matrix td { text-align: center; padding: 4px; border: 1px solid #eee;
             font-variant-numeric: tabular-nums; }
.matrix th { background: #fafafa; padding: 4px; }
.muted-note { color: var(--muted); font-size: 11px; padding: 4px 0; }

.controls { padding: 10px 18px; border-bottom: 1px solid var(--border); background: #fff;
            display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
.controls label { font-size: 12px; }
.controls input[type=text] { padding: 4px 8px; border: 1px solid var(--border); border-radius: 4px;
                             font-size: 12px; width: 180px; }
.controls select { padding: 4px 6px; border: 1px solid var(--border); border-radius: 4px;
                   font-size: 12px; background: #fff; }
.controls input[type=range] { width: 90px; vertical-align: middle; }
.controls .yr_label { display: inline-block; min-width: 86px; text-align: center; font-variant-numeric: tabular-nums; }
.controls button { padding: 4px 10px; border: 1px solid var(--border); border-radius: 4px;
                   font-size: 12px; background: #fff; cursor: pointer; }
.controls button:hover { background: #f0f0f0; }
.legend { display: flex; gap: 8px; flex-wrap: wrap; padding: 6px 18px;
          border-bottom: 1px solid var(--border); background: #fff; }
.legend .item { display: flex; align-items: center; gap: 4px; cursor: pointer; user-select: none;
                font-size: 11px; padding: 2px 6px; border-radius: 3px; }
.legend .item.off { opacity: 0.3; }
.legend .swatch { width: 10px; height: 10px; border-radius: 2px; }

.viz { position: relative; }
.year-header { position: sticky; top: 0; z-index: 5; background: #fff;
               border-bottom: 1px solid var(--border); height: var(--year-h);
               margin-left: var(--name-w); }
.year-header .tick { position: absolute; top: 8px; font-size: 10px; color: var(--muted);
                     transform: translateX(-50%); }
.year-header .tick.major { font-weight: 600; color: var(--fg); }

.rows { position: relative; background-repeat: repeat; }
.row { position: relative; height: var(--row-h); border-bottom: 1px solid rgba(0,0,0,0.03);
       transition: background 0.08s; }
.row:nth-child(even) { background: rgba(0,0,0,0.015); }
.row.hl, .row.hl:nth-child(even) { background: #fff4c2; }
.row.hl .name { background: #fff4c2; font-weight: 600; }
.name { position: absolute; left: 0; top: 0; width: var(--name-w); padding: 0 8px;
        line-height: var(--row-h); font-size: 11px; color: var(--fg);
        white-space: nowrap; overflow: hidden;
        border-right: 1px solid var(--border); background: #fff;
        display: flex; align-items: center; gap: 4px; }
.name .pname { flex: 1; overflow: hidden; text-overflow: ellipsis; cursor: pointer; }
.name .pname:hover { color: #06c; text-decoration: underline; }
.name .lnk { color: #888; font-size: 10px; padding: 0 3px; border-radius: 2px;
             text-decoration: none; flex-shrink: 0; }
.name .lnk:hover { background: #eef; color: #06c; }
.event { position: absolute; height: calc(var(--row-h) - 2px); top: 1px;
         width: var(--col-w); border-radius: 1px; cursor: pointer;
         transition: transform 0.05s; }
.event:hover { transform: scaleY(1.4); z-index: 4; }
.event.inferred { opacity: 0.45; }
.event.inferred:hover { opacity: 0.85; }
.event.selected { outline: 2px solid #111; outline-offset: 1px; z-index: 6; }
.event.selected.inferred { opacity: 1; }

.tooltip { position: fixed; background: #222; color: #fff; padding: 8px 10px;
           border-radius: 6px; font-size: 12px; max-width: 360px; line-height: 1.5;
           pointer-events: none; opacity: 0; transition: opacity 0.1s; z-index: 100;
           box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
.tooltip.show { opacity: 1; pointer-events: auto; }
.tooltip .person { font-weight: 600; margin-bottom: 4px; }
.tooltip .year { color: #aaa; font-size: 11px; font-weight: normal; }
.tooltip .ev { margin: 4px 0; }
.tooltip .meta { color: #aaa; font-size: 11px; }
.tooltip a { color: #6cf; text-decoration: none; display: block; margin-top: 6px;
             font-size: 11px; }
.tooltip a:hover { text-decoration: underline; }

footer { padding: 8px 18px; color: var(--muted); font-size: 11px;
         border-top: 1px solid var(--border); background: #fff; }
footer a { color: var(--muted); }
</style>
</head>
<body>
<header>
  <div class="title">
    <h1 id="page_title"></h1>
    <div class="sub" id="page_sub"></div>
  </div>
  <div class="lang-toggle">
    <button id="btn_ko" class="active">한국어</button>
    <button id="btn_en">English</button>
  </div>
</header>

<nav class="tabs">
  <button class="tab-btn active" id="tab_btn_timeline" data-tab="timeline"></button>
  <button class="tab-btn" id="tab_btn_eda" data-tab="eda"></button>
</nav>

<div class="tab-pane active" id="tab_timeline">

<div class="controls">
  <label><span id="lbl_sort"></span>
    <select id="sort">
      <option value="birth"></option>
      <option value="alpha"></option>
      <option value="count"></option>
    </select>
  </label>
  <label><span id="lbl_search"></span>
    <input type="text" id="search">
  </label>
  <label><span id="lbl_phase"></span>
    <select id="phase">
      <option value=""></option>
      <option value="k12"></option>
      <option value="undergrad"></option>
      <option value="grad"></option>
      <option value="early_career"></option>
      <option value="mid_career"></option>
      <option value="senior"></option>
    </select>
  </label>
  <label><span id="lbl_year"></span>
    <input type="range" id="ymin">
    <span class="yr_label" id="yr_label"></span>
    <input type="range" id="ymax">
  </label>
  <button id="btn_reset"></button>
  <span class="sub" id="visible_count"></span>
</div>

<div class="legend" id="legend"></div>

<div class="viz">
  <div class="year-header" id="year_header"></div>
  <div class="rows" id="rows" style="margin-left: var(--name-w);"></div>
</div>

<div class="tooltip" id="tooltip"></div>

</div><!-- /tab_timeline -->

<div class="tab-pane" id="tab_eda">
  <div class="eda" id="eda_container"></div>
</div>

<footer>
  <span id="footer_text"></span>
</footer>

<script>
const VIZ_DATA = __DATA__;
const EDA_DATA = __EDA__;
const REPO = "__REPO__";

// 네트워크: 인디고로 재배치 (회색=개인사, 빨강=실패와 모두 시각적으로 멀게).
// 의미와 색상 매핑:
//   라이트 그레이=중립(개인사), 딥 블루=학습(교육), 포레스트 그린=안정(직업),
//   오렌지=활동(연구), 보라=비즈니스(창업), 청록(teal)=커뮤니티,
//   노랑=명예, 인디고=네트워크, 딥 레드=실패, 짙은 갈색=외부 영향
const TYPE_COLOR = {
  '개인사':       '#BDC3C7',
  '교육':         '#2980B9',
  '직업 이력':    '#229954',
  '연구·프로젝트': '#E67E22',
  '창업·산업':    '#8E44AD',
  '학회·커뮤니티': '#16A085',
  '수상·명예':    '#F1C40F',
  '네트워크':     '#5C6BC0',
  '실패·전환':    '#C0392B',
  '외부 영향':    '#5D4037',
};

const TYPE_EN = {
  '개인사':       'Personal',
  '교육':         'Education',
  '직업 이력':    'Career',
  '연구·프로젝트': 'Research / Projects',
  '창업·산업':    'Industry / Founding',
  '학회·커뮤니티': 'Community',
  '수상·명예':    'Honors',
  '네트워크':     'Network',
  '실패·전환':    'Setback / Pivot',
  '외부 영향':    'External Events',
};

const PHASE_LABELS = {
  ko: { '': '전체', k12: 'K-12 (학창)', undergrad: '학부생',
        grad: '대학원생', early_career: '박사후·신임',
        mid_career: '중견', senior: '시니어/원로' },
  en: { '': 'All', k12: 'K-12', undergrad: 'Undergrad',
        grad: 'Grad student', early_career: 'Early career',
        mid_career: 'Mid career', senior: 'Senior' },
};

const I18N = {
  ko: {
    title: 'Roboticists Oral History — 커리어 시각화',
    sub: '110명의 거장 / 2778개 이벤트 (반투명 셀 = 원문에 연도 미상, 앞뒤 컨텍스트로 추론)',
    sort: '정렬:',
    sort_birth: '출생/최초연도순',
    sort_alpha: '이름순 (가나다)',
    sort_count: '이벤트 수 (많은 순)',
    search: '검색:',
    search_ph: '이름 (영문)',
    phase: '페이즈:',
    year_range: '연도:',
    reset: '필터 초기화',
    visible: (n) => `표시 중: ${n}명`,
    tip_year_inferred: (raw, y) => `(원문: "${raw}" · 추론 ${y}년)`,
    footer: `데이터: <a href="${REPO}" target="_blank">${REPO}</a>`,
    link_timeline: '[타임라인]',
    link_interview: '[인터뷰전문]',
    tab_timeline: '커리어 시각화',
    tab_eda: 'EDA',
  },
  en: {
    title: 'Roboticists Oral History — Career Timeline',
    sub: '110 pioneers / 2778 events (translucent cell = year unknown in source, inferred from context)',
    sort: 'Sort:',
    sort_birth: 'By birth / earliest year',
    sort_alpha: 'Alphabetical',
    sort_count: 'Event count (most first)',
    search: 'Search:',
    search_ph: 'name',
    phase: 'Phase:',
    year_range: 'Years:',
    reset: 'Reset filters',
    visible: (n) => `Showing: ${n} people`,
    tip_year_inferred: (raw, y) => `(source: "${raw}" · inferred ${y})`,
    footer: `Data: <a href="${REPO}" target="_blank">${REPO}</a>`,
    link_timeline: '[Timeline]',
    link_interview: '[Interview]',
    tab_timeline: 'Career Timeline',
    tab_eda: 'EDA',
  },
};

const ROW_H = 14;
const NAME_W = 280;
const MIN_COL_W = 7;
let COL_W = MIN_COL_W;  // 윈도우 너비에 맞춰 동적 계산
const Y_MIN = VIZ_DATA.year_min;
const Y_MAX = VIZ_DATA.year_max;
const YEAR_SPAN = Y_MAX - Y_MIN + 1;

function computeColW() {
  // 사용 가능한 가로 너비를 연 수로 나눠서 cell 너비 결정
  const avail = window.innerWidth - NAME_W - 24;  // 24px 우측 여유
  const w = Math.max(MIN_COL_W, Math.floor(avail / YEAR_SPAN));
  COL_W = w;
}

let lang = 'ko';
let activeTypes = new Set(Object.keys(TYPE_COLOR));
let currentSort = 'birth';
let currentSearch = '';
let currentPhase = '';
let yearMin = Y_MIN;
let yearMax = Y_MAX;
let selectedDiv = null;
let selectedEvent = null;
let urlUpdatePending = false;

function applyLang() {
  const t = I18N[lang];
  document.title = t.title;
  document.getElementById('page_title').textContent = t.title;
  document.getElementById('page_sub').textContent = t.sub;
  document.getElementById('lbl_sort').textContent = t.sort;
  document.getElementById('lbl_search').textContent = t.search;
  document.getElementById('lbl_phase').textContent = t.phase;
  document.getElementById('lbl_year').textContent = t.year_range;
  document.getElementById('btn_reset').textContent = t.reset;
  document.getElementById('search').placeholder = t.search_ph;
  document.getElementById('footer_text').innerHTML = t.footer;
  document.getElementById('tab_btn_timeline').textContent = t.tab_timeline;
  document.getElementById('tab_btn_eda').textContent = t.tab_eda;

  const sortSel = document.getElementById('sort');
  sortSel.options[0].textContent = t.sort_birth;
  sortSel.options[1].textContent = t.sort_alpha;
  sortSel.options[2].textContent = t.sort_count;

  const phaseSel = document.getElementById('phase');
  const ph = PHASE_LABELS[lang];
  for (const o of phaseSel.options) o.textContent = ph[o.value];

  buildLegend();
  render();
  if (edaBuilt) {
    Object.keys(chartInstances).forEach(k => destroyChart(k));
    edaBuilt = false;
    if (document.getElementById('tab_eda').classList.contains('active')) {
      buildEDA();
      edaBuilt = true;
    }
  }
}

function buildLegend() {
  const el = document.getElementById('legend');
  el.innerHTML = '';
  for (const [t, c] of Object.entries(TYPE_COLOR)) {
    const it = document.createElement('div');
    it.className = 'item' + (activeTypes.has(t) ? '' : ' off');
    const label = lang === 'en' ? TYPE_EN[t] : t;
    it.innerHTML = `<span class="swatch" style="background:${c}"></span><span>${label}</span>`;
    it.onclick = () => {
      if (activeTypes.has(t)) activeTypes.delete(t);
      else activeTypes.add(t);
      it.classList.toggle('off');
      render();
      updateUrl();
    };
    el.appendChild(it);
  }
}

function buildYearHeader() {
  const hdr = document.getElementById('year_header');
  hdr.innerHTML = '';
  const span = Y_MAX - Y_MIN + 1;
  hdr.style.width = (span * COL_W) + 'px';
  for (let y = Y_MIN; y <= Y_MAX; y++) {
    const x = (y - Y_MIN) * COL_W + COL_W / 2;
    if (y % 5 === 0) {
      const t = document.createElement('div');
      t.className = 'tick' + (y % 10 === 0 ? ' major' : '');
      t.style.left = x + 'px';
      t.textContent = y;
      hdr.appendChild(t);
    }
  }
  // 십년 단위 세로 그리드 (.rows 배경)
  const rows = document.getElementById('rows');
  const decadeStart = Math.ceil(Y_MIN / 10) * 10;
  const offsetX = (decadeStart - Y_MIN) * COL_W + COL_W / 2;
  rows.style.backgroundImage =
    'linear-gradient(to right, rgba(0,0,0,0.08) 1px, transparent 1px)';
  rows.style.backgroundSize = (10 * COL_W) + 'px 100%';
  rows.style.backgroundPosition = offsetX + 'px 0';
}

function getPersonOrder() {
  const ps = Object.keys(VIZ_DATA.persons);
  if (currentSort === 'alpha') {
    return ps.sort((a, b) =>
      (VIZ_DATA.persons[a].full_name || a).localeCompare(VIZ_DATA.persons[b].full_name || b));
  } else if (currentSort === 'birth') {
    const earliest = {};
    for (const e of VIZ_DATA.events) {
      if (e.year != null) {
        if (!(e.person in earliest) || e.year < earliest[e.person])
          earliest[e.person] = e.year;
      }
    }
    return ps.sort((a, b) => {
      const ma = VIZ_DATA.persons[a], mb = VIZ_DATA.persons[b];
      const ay = (ma.birth_year != null) ? ma.birth_year :
                 (earliest[a] != null) ? earliest[a] : 9999;
      const by = (mb.birth_year != null) ? mb.birth_year :
                 (earliest[b] != null) ? earliest[b] : 9999;
      return ay - by;
    });
  } else {
    return ps.sort((a, b) => VIZ_DATA.persons[b].event_count - VIZ_DATA.persons[a].event_count);
  }
}

function render() {
  const order = getPersonOrder();
  const rows = document.getElementById('rows');
  rows.innerHTML = '';
  const span = Y_MAX - Y_MIN + 1;
  const width = span * COL_W;

  // 화살표 네비 위해 인물별 이벤트를 연도순 정렬
  const byPerson = {};
  for (const p of order) byPerson[p] = [];
  for (const e of VIZ_DATA.events) {
    if (e.year == null) continue;
    if (e.year < yearMin || e.year > yearMax) continue;
    if (!activeTypes.has(e.type)) continue;
    if (currentPhase && e.phase !== currentPhase) continue;
    if (byPerson[e.person]) byPerson[e.person].push(e);
  }
  for (const p of order) byPerson[p].sort((a, b) => a.year - b.year);

  let visible = 0;
  const searchLower = currentSearch.toLowerCase();
  for (const p of order) {
    const meta = VIZ_DATA.persons[p];
    const fullName = meta.full_name || p;
    if (searchLower && !fullName.toLowerCase().includes(searchLower)
                    && !p.toLowerCase().includes(searchLower)) continue;
    visible++;

    const evs = byPerson[p];
    const row = document.createElement('div');
    row.className = 'row';
    row.style.width = (width + NAME_W) + 'px';
    row.style.marginLeft = (-NAME_W) + 'px';
    row.addEventListener('mouseenter', () => row.classList.add('hl'));
    row.addEventListener('mouseleave', () => row.classList.remove('hl'));

    const name = document.createElement('div');
    name.className = 'name';
    const intvTgt = lang === 'en' ? 'ethw_source_eng' : 'translated_kor';
    const tlTgt = lang === 'en' ? 'timelines_eng' : 'timelines_kor';
    const i18 = I18N[lang];
    name.innerHTML = `
      <span class="pname" title="${escapeHtml(fullName)} · ${meta.event_count} events">${escapeHtml(fullName)}</span>
      <a class="lnk" href="${REPO}/blob/main/${tlTgt}/${p}.md" target="_blank">${i18.link_timeline}</a>
      <a class="lnk" href="${REPO}/blob/main/${intvTgt}/${p}.md" target="_blank">${i18.link_interview}</a>
    `;
    name.querySelector('.pname').onclick = () => {
      window.open(`${REPO}/blob/main/${intvTgt}/${p}.md`, '_blank');
    };
    row.appendChild(name);

    for (const e of evs) {
      const div = document.createElement('div');
      div.className = 'event' + (e.year_inferred ? ' inferred' : '');
      div.style.left = (NAME_W + (e.year - Y_MIN) * COL_W) + 'px';
      div.style.background = TYPE_COLOR[e.type] || '#666';
      div._eventData = e;
      div.addEventListener('mouseenter', (ev) => showTip(ev, e));
      div.addEventListener('mousemove', positionTip);
      div.addEventListener('mouseleave', hideTip);
      div.addEventListener('click', (ev) => { ev.stopPropagation(); clickEvent(e, div); });
      // 선택 상태가 유지되도록 재렌더 후에도 같은 셀 다시 표시
      if (selectedEvent && e === selectedEvent) {
        div.classList.add('selected');
        selectedDiv = div;
      }
      row.appendChild(div);
    }
    rows.appendChild(row);
  }
  document.getElementById('visible_count').textContent = I18N[lang].visible(visible);
}

let tipTimeout;
function showTip(ev, e) {
  clearTimeout(tipTimeout);
  const t = document.getElementById('tooltip');
  const i = I18N[lang];
  const _pm = VIZ_DATA.persons[e.person];
  const fullName = (_pm && _pm.full_name) || e.person;
  // 언어에 따라 이벤트 텍스트와 year_raw 스왑
  const eventText = (lang === 'en' && e.event_en) ? e.event_en : e.event;
  const yearRaw = (lang === 'en' && e.year_raw_en) ? e.year_raw_en : e.year_raw;
  const yearLabel = e.year_inferred
    ? i.tip_year_inferred(escapeHtml(yearRaw), e.year)
    : `(${escapeHtml(yearRaw)})`;
  const typeLabel = lang === 'en' ? (TYPE_EN[e.type] || e.type) : e.type;
  const phaseLabel = PHASE_LABELS[lang][e.phase] || e.phase;
  t.innerHTML = `
    <div class="person">${escapeHtml(fullName)} <span class="year">${yearLabel}</span></div>
    <div class="ev">${escapeHtml(eventText)}</div>
    <div class="meta">${typeLabel} / ${e.subtype} / ${phaseLabel}</div>
  `;
  t.classList.add('show');
  positionTip(ev);
}
function positionTip(ev) {
  const t = document.getElementById('tooltip');
  const tw = t.offsetWidth || 320;
  const th = t.offsetHeight || 100;
  // 기본: 커서 우하단 12px. 화면 밖이면 좌/상으로 뒤집기.
  let x = ev.clientX + 12;
  let y = ev.clientY + 12;
  if (x + tw > window.innerWidth - 8) x = ev.clientX - tw - 12;
  if (y + th > window.innerHeight - 8) y = ev.clientY - th - 12;
  if (x < 8) x = 8;
  if (y < 8) y = 8;
  t.style.left = x + 'px';
  t.style.top = y + 'px';
}
function hideTip() {
  tipTimeout = setTimeout(() => {
    if (selectedDiv && selectedEvent) {
      // 선택된 셀이 있으면 그 정보로 복원
      showTipAtCell(selectedDiv, selectedEvent);
    } else {
      document.getElementById('tooltip').classList.remove('show');
    }
  }, 250);
}
function clickEvent(e, div) {
  // 같은 셀 다시 클릭 → 해제 (토글)
  if (selectedDiv === div) {
    clearSelection();
    return;
  }
  selectEvent(div, e);
}

function selectEvent(div, e) {
  if (selectedDiv && selectedDiv !== div) selectedDiv.classList.remove('selected');
  selectedDiv = div;
  selectedEvent = e;
  div.classList.add('selected');
  showTipAtCell(div, e);
  updateUrl();
}

function clearSelection() {
  if (selectedDiv) selectedDiv.classList.remove('selected');
  selectedDiv = null;
  selectedEvent = null;
  document.getElementById('tooltip').classList.remove('show');
  updateUrl();
}

function showTipAtCell(div, e) {
  // 호버 툴팁과 동일 콘텐츠를 셀 옆에 고정
  clearTimeout(tipTimeout);
  const t = document.getElementById('tooltip');
  const i = I18N[lang];
  const _pm = VIZ_DATA.persons[e.person];
  const fullName = (_pm && _pm.full_name) || e.person;
  const eventText = (lang === 'en' && e.event_en) ? e.event_en : e.event;
  const yearRaw = (lang === 'en' && e.year_raw_en) ? e.year_raw_en : e.year_raw;
  const yearLabel = e.year_inferred
    ? i.tip_year_inferred(escapeHtml(yearRaw), e.year)
    : `(${escapeHtml(yearRaw)})`;
  const typeLabel = lang === 'en' ? (TYPE_EN[e.type] || e.type) : e.type;
  const phaseLabel = PHASE_LABELS[lang][e.phase] || e.phase;
  const hint = lang === 'en'
    ? '<div class="meta" style="margin-top:6px;color:#7af">← →: navigate · Esc: deselect</div>'
    : '<div class="meta" style="margin-top:6px;color:#7af">← →: 좌/우 셀 이동 · Esc: 해제</div>';
  t.innerHTML = `
    <div class="person">${escapeHtml(fullName)} <span class="year">${yearLabel}</span></div>
    <div class="ev">${escapeHtml(eventText)}</div>
    <div class="meta">${typeLabel} / ${e.subtype} / ${phaseLabel}</div>
    ${hint}
  `;
  t.classList.add('show');
  // 셀 옆에 위치 (오른쪽이 화면 밖이면 왼쪽으로)
  const rect = div.getBoundingClientRect();
  const tw = t.offsetWidth || 320;
  const th = t.offsetHeight || 120;
  let x = rect.right + 8;
  let y = rect.top - 4;
  if (x + tw > window.innerWidth - 8) x = rect.left - tw - 8;
  if (x < 8) x = 8;
  if (y + th > window.innerHeight - 8) y = window.innerHeight - th - 8;
  if (y < 8) y = 8;
  t.style.left = x + 'px';
  t.style.top = y + 'px';
}
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

document.getElementById('tooltip').addEventListener('mouseenter', () => clearTimeout(tipTimeout));
document.getElementById('tooltip').addEventListener('mouseleave', hideTip);
document.getElementById('sort').addEventListener('change', (e) => { currentSort = e.target.value; render(); });
document.getElementById('search').addEventListener('input', (e) => { currentSearch = e.target.value; render(); });
document.getElementById('phase').addEventListener('change', (e) => { currentPhase = e.target.value; render(); });
document.getElementById('btn_ko').addEventListener('click', () => {
  lang = 'ko';
  document.getElementById('btn_ko').classList.add('active');
  document.getElementById('btn_en').classList.remove('active');
  applyLang();
  updateUrl();
});
document.getElementById('btn_en').addEventListener('click', () => {
  lang = 'en';
  document.getElementById('btn_en').classList.add('active');
  document.getElementById('btn_ko').classList.remove('active');
  applyLang();
  updateUrl();
});

// 연도 범위 슬라이더 초기화
const ymin = document.getElementById('ymin');
const ymax = document.getElementById('ymax');
ymin.min = Y_MIN; ymin.max = Y_MAX; ymin.value = yearMin;
ymax.min = Y_MIN; ymax.max = Y_MAX; ymax.value = yearMax;
function updateYearRangeUI() {
  document.getElementById('yr_label').textContent = `${yearMin} – ${yearMax}`;
}
function onRangeChange() {
  let lo = parseInt(ymin.value, 10);
  let hi = parseInt(ymax.value, 10);
  if (lo > hi) { const tmp = lo; lo = hi; hi = tmp; }
  yearMin = lo; yearMax = hi;
  ymin.value = lo; ymax.value = hi;
  updateYearRangeUI();
  render();
  updateUrl();
}
ymin.addEventListener('input', onRangeChange);
ymax.addEventListener('input', onRangeChange);

document.getElementById('btn_reset').addEventListener('click', () => {
  activeTypes = new Set(Object.keys(TYPE_COLOR));
  currentSort = 'birth';
  currentSearch = '';
  currentPhase = '';
  yearMin = Y_MIN; yearMax = Y_MAX;
  ymin.value = Y_MIN; ymax.value = Y_MAX;
  document.getElementById('search').value = '';
  document.getElementById('phase').value = '';
  document.getElementById('sort').value = 'birth';
  clearSelection();
  updateYearRangeUI();
  buildLegend();
  render();
  updateUrl();
});

// 모든 상태 변경 시 URL 갱신 훅
const _origSort = document.getElementById('sort').onchange;
document.getElementById('sort').addEventListener('change', updateUrl);
document.getElementById('search').addEventListener('input', updateUrl);
document.getElementById('phase').addEventListener('change', updateUrl);

// ---- 퍼말링크: URL ↔ state ----
function updateUrl() {
  if (urlUpdatePending) return;
  urlUpdatePending = true;
  requestAnimationFrame(() => {
    urlUpdatePending = false;
    const p = new URLSearchParams();
    if (lang !== 'ko') p.set('lang', lang);
    if (currentSort !== 'birth') p.set('sort', currentSort);
    if (currentSearch) p.set('q', currentSearch);
    if (currentPhase) p.set('phase', currentPhase);
    if (yearMin !== Y_MIN) p.set('y1', yearMin);
    if (yearMax !== Y_MAX) p.set('y2', yearMax);
    const allTypes = Object.keys(TYPE_COLOR);
    if (activeTypes.size !== allTypes.length) {
      // 짧게: 비활성만 기록 (보통 더 적음)
      const off = allTypes.filter(t => !activeTypes.has(t));
      p.set('off', off.join(','));
    }
    if (selectedEvent) {
      const key = `${selectedEvent.person}|${selectedEvent.year}|${selectedEvent.event.slice(0, 50)}`;
      p.set('sel', key);
    }
    const qs = p.toString();
    const url = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
    history.replaceState(null, '', url);
  });
}

function applyUrlState() {
  const p = new URLSearchParams(window.location.search);
  if (p.get('lang') === 'en') lang = 'en';
  if (p.get('sort')) currentSort = p.get('sort');
  if (p.get('q')) currentSearch = p.get('q');
  if (p.get('phase')) currentPhase = p.get('phase');
  if (p.get('y1')) yearMin = parseInt(p.get('y1'), 10) || Y_MIN;
  if (p.get('y2')) yearMax = parseInt(p.get('y2'), 10) || Y_MAX;
  if (p.get('off')) {
    const offSet = new Set(p.get('off').split(','));
    activeTypes = new Set(Object.keys(TYPE_COLOR).filter(t => !offSet.has(t)));
  }
  // UI 동기화
  document.getElementById('sort').value = currentSort;
  document.getElementById('search').value = currentSearch;
  document.getElementById('phase').value = currentPhase;
  ymin.value = yearMin; ymax.value = yearMax;
  if (lang === 'en') {
    document.getElementById('btn_en').classList.add('active');
    document.getElementById('btn_ko').classList.remove('active');
  }
}

function applySelectionFromUrl() {
  const p = new URLSearchParams(window.location.search);
  const sel = p.get('sel');
  if (!sel) return;
  const parts = sel.split('|');
  if (parts.length < 3) return;
  const [person, yearStr, prefix] = parts;
  const year = parseInt(yearStr, 10);
  // DOM에서 매칭 셀 찾기
  const allDivs = document.querySelectorAll('.event');
  for (const d of allDivs) {
    const e = d._eventData;
    if (e && e.person === person && e.year === year &&
        e.event.slice(0, 50) === prefix) {
      selectEvent(d, e);
      d.scrollIntoView({ block: 'center', inline: 'center' });
      return;
    }
  }
}

// ---- 탭 전환 ----
let edaBuilt = false;
function switchTab(name) {
  document.querySelectorAll('.tab-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.tab === name);
  });
  document.querySelectorAll('.tab-pane').forEach(p => {
    p.classList.toggle('active', p.id === 'tab_' + name);
  });
  if (name === 'eda' && !edaBuilt) {
    buildEDA();
    edaBuilt = true;
  }
}
document.getElementById('tab_btn_timeline').addEventListener('click',
  () => switchTab('timeline'));
document.getElementById('tab_btn_eda').addEventListener('click',
  () => switchTab('eda'));

// ---- EDA 라벨 i18n ----
const EDA_LABELS = {
  ko: {
    A: 'A. 인구학', A_birth: '출생 연도 (10년 단위)',
    A_country: '출생 국가 Top 25', A_gender: '성별', A_iv: '인터뷰 연도',
    B: 'B. 학력',
    B_bs_field: '학사 전공 분포', B_phd_field: '박사 전공 분포',
    B_bs_school: '학사 출신 대학 Top 20', B_phd_school: '박사 출신 대학 Top 20',
    B_same: '학사·박사 동일 대학', B_bs_phd_yrs: '학사→박사 소요 연수',
    B_edu_country: '교육받은 국가', B_advisor: '박사 지도교수 (다중 등장)',
    C: 'C. 커리어',
    C_per_type: '타입별 이벤트 수', C_per_phase: '페이즈별 이벤트 수',
    C_matrix: '타입 × 페이즈 매트릭스',
    C_by_year: '연도별 전체 이벤트', C_by_year_type: '연도별 타입 추이',
    D: 'D. 직업 이력',
    D_first: '박사 후 첫 직장 유형', D_orgs: '소속 기관 Top 25',
    D_moves: '이직 횟수 분포', D_intl: '박사 국가 ≠ 첫 직장 국가',
    E: 'E. 연구·주제',
    E_topics: '연구 주제 Top 30', E_topics_per: '인물당 주제 수',
    E_breakthrough: '돌파 시점 (박사 후 N년)',
    F: 'F. 학회·커뮤니티',
    F_admin: '보직 누적 Top 20', F_confs: '학회·저널 창설',
    G: 'G. 수상·명예',
    G_types: '상 종류 Top', G_count: '인물별 수상 수 Top',
    G_fellow: 'IEEE Fellow 추대 시점 (박사 후 N년)',
    H: 'H. 창업·산업',
    H_pct: '창업 경험 비율', H_serial: '시리얼 창업가',
    I: 'I. 실패·전환',
    I_subtypes: '실패·전환 세부 유형', I_with: '한 번 이상 실패·전환 경험',
    I_pivot: '분야 전환(pivot) Top',
    J: 'J. 외부 영향',
    J_events: '인생 영향 외부 사건',
    L: 'L. 한국·아시아 서브셋',
    L_korean: '한국 출신', L_asia: '아시아 국가 인물 수',
    M: 'M. 스토리 발굴',
    M_tenure: '한 곳 20년 이상 재직 Top', M_diverse: '커리어 다양성 Top',
    M_late: '늦게 박사 받은 Top', M_young: '어린 나이에 박사 받은 Top',
    M_doc: '인터뷰 이벤트 풍부도 Top',
    persons: '인물 수', events: '이벤트 수', count: '수', years: '년',
  },
  en: {
    A: 'A. Demographics', A_birth: 'Birth year (decades)',
    A_country: 'Birth country Top 25', A_gender: 'Gender', A_iv: 'Interview year',
    B: 'B. Education',
    B_bs_field: 'Bachelor field', B_phd_field: 'PhD field',
    B_bs_school: 'Bachelor school Top 20', B_phd_school: 'PhD school Top 20',
    B_same: 'Same school BS = PhD', B_bs_phd_yrs: 'Years from BS to PhD',
    B_edu_country: 'Country of education', B_advisor: 'PhD advisors (top mentions)',
    C: 'C. Career',
    C_per_type: 'Events per type', C_per_phase: 'Events per phase',
    C_matrix: 'Type × Phase matrix',
    C_by_year: 'All events by year', C_by_year_type: 'Type trend over time',
    D: 'D. Career history',
    D_first: 'First job after PhD', D_orgs: 'Top organizations',
    D_moves: 'Number of moves per person', D_intl: 'PhD country ≠ first-job country',
    E: 'E. Research / Topics',
    E_topics: 'Topics Top 30', E_topics_per: 'Topics per person',
    E_breakthrough: 'Breakthrough timing (years post-PhD)',
    F: 'F. Community',
    F_admin: 'Admin role count Top 20', F_confs: 'Conferences / journals founded',
    G: 'G. Honors',
    G_types: 'Award types', G_count: 'Awards per person Top',
    G_fellow: 'Years from PhD to IEEE Fellow',
    H: 'H. Industry / Founding',
    H_pct: '% who founded a company', H_serial: 'Serial founders',
    I: 'I. Setback / Pivot',
    I_subtypes: 'Setback subtypes', I_with: 'Has at least one setback',
    I_pivot: 'Field pivots Top',
    J: 'J. External Events',
    J_events: 'External events affecting careers',
    L: 'L. Korea / Asia subset',
    L_korean: 'From South Korea', L_asia: 'People by Asian country',
    M: 'M. Stories',
    M_tenure: 'Tenure ≥ 20 years at one org Top', M_diverse: 'Most diverse careers Top',
    M_late: 'Latest PhD age Top', M_young: 'Youngest PhD age Top',
    M_doc: 'Most documented lives Top',
    persons: 'People', events: 'Events', count: 'Count', years: 'Years',
  },
};

// ---- Chart.js 헬퍼 ----
const chartInstances = {};
function destroyChart(id) {
  if (chartInstances[id]) { chartInstances[id].destroy(); delete chartInstances[id]; }
}
function chartBar(id, labels, values, label, opts) {
  destroyChart(id);
  const ctx = document.getElementById(id);
  if (!ctx) return;
  chartInstances[id] = new Chart(ctx, {
    type: 'bar',
    data: { labels, datasets: [{ label, data: values, backgroundColor: '#3498DB' }] },
    options: Object.assign({
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: { y: { beginAtZero: true } }
    }, opts || {})
  });
}
function chartHBar(id, labels, values, label) {
  destroyChart(id);
  const ctx = document.getElementById(id);
  if (!ctx) return;
  chartInstances[id] = new Chart(ctx, {
    type: 'bar',
    data: { labels, datasets: [{ label, data: values, backgroundColor: '#16A085' }] },
    options: {
      indexAxis: 'y', responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: { x: { beginAtZero: true }, y: { ticks: { font: { size: 10 } } } }
    }
  });
}
function chartPie(id, labels, values, colors) {
  destroyChart(id);
  const ctx = document.getElementById(id);
  if (!ctx) return;
  chartInstances[id] = new Chart(ctx, {
    type: 'doughnut',
    data: { labels, datasets: [{ data: values, backgroundColor: colors ||
      ['#3498DB', '#E67E22', '#2ECC71', '#9B59B6', '#F1C40F', '#E74C3C', '#16A085',
       '#5C6BC0', '#95A5A6', '#5D4037'] }] },
    options: { responsive: true, maintainAspectRatio: false,
               plugins: { legend: { position: 'right', labels: { font: { size: 10 } } } } }
  });
}
function chartLine(id, labels, datasets) {
  destroyChart(id);
  const ctx = document.getElementById(id);
  if (!ctx) return;
  chartInstances[id] = new Chart(ctx, {
    type: 'line',
    data: { labels, datasets },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: datasets.length > 1, position: 'right', labels: { font: { size: 10 } } } },
      elements: { point: { radius: 0 }, line: { tension: 0.2 } },
      scales: { y: { beginAtZero: true, stacked: false } }
    }
  });
}

function histBins(values, binSize) {
  if (!values.length) return { labels: [], counts: [] };
  const lo = Math.floor(Math.min(...values) / binSize) * binSize;
  const hi = Math.ceil(Math.max(...values) / binSize) * binSize;
  const bins = {};
  for (let b = lo; b <= hi; b += binSize) bins[b] = 0;
  for (const v of values) {
    const b = Math.floor(v / binSize) * binSize;
    bins[b] = (bins[b] || 0) + 1;
  }
  const keys = Object.keys(bins).map(Number).sort((a, b) => a - b);
  return { labels: keys.map(k => `${k}–${k + binSize - 1}`), counts: keys.map(k => bins[k]) };
}

// ---- EDA 빌드 ----
function buildEDA() {
  const L = EDA_LABELS[lang];
  const D = EDA_DATA;
  const c = document.getElementById('eda_container');
  c.innerHTML = '';

  const T = (ko, en) => lang === 'ko' ? ko : en;

  function section(id, title) {
    const s = document.createElement('section');
    s.className = 'eda-cat';
    s.innerHTML = `<h2>${title}</h2><div class="eda-grid" id="grid_${id}"></div>`;
    c.appendChild(s);
    return s.querySelector('.eda-grid');
  }
  function card(grid, title, body, wide, tall) {
    const d = document.createElement('div');
    d.className = 'eda-card' + (wide ? ' wide' : '');
    d.innerHTML = `<h3>${title}</h3>${body}`;
    grid.appendChild(d);
    return d;
  }
  function chartCard(grid, title, canvasId, wide, tall) {
    return card(grid,
      title,
      `<div class="chart-wrap${tall ? ' tall' : ''}"><canvas id="${canvasId}"></canvas></div>`,
      wide, tall);
  }
  function listCard(grid, title, items) {
    const lis = items.map(s => `<li>${s}</li>`).join('');
    return card(grid, title, `<ul>${lis}</ul>`);
  }
  function tableCard(grid, title, headers, rows, wide) {
    const head = headers.map(h => `<th>${h}</th>`).join('');
    const body = rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
    return card(grid, title, `<table><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>`, wide);
  }

  // --- A. 인구학 ---
  let g = section('A', L.A);
  chartCard(g, L.A_birth, 'ch_A_birth');
  chartCard(g, L.A_gender, 'ch_A_gender');
  chartCard(g, L.A_country, 'ch_A_country', false, true);
  chartCard(g, L.A_iv, 'ch_A_iv');

  // --- B. 학력 ---
  g = section('B', L.B);
  chartCard(g, L.B_bs_field, 'ch_B_bs_field', false, true);
  chartCard(g, L.B_phd_field, 'ch_B_phd_field', false, true);
  chartCard(g, L.B_bs_school, 'ch_B_bs_school', false, true);
  chartCard(g, L.B_phd_school, 'ch_B_phd_school', false, true);
  chartCard(g, L.B_same, 'ch_B_same');
  chartCard(g, L.B_bs_phd_yrs, 'ch_B_bs_phd_yrs');
  chartCard(g, L.B_edu_country, 'ch_B_edu_country', false, true);
  chartCard(g, L.B_advisor, 'ch_B_advisor', false, true);

  // --- C. 커리어 ---
  g = section('C', L.C);
  chartCard(g, L.C_per_type, 'ch_C_type');
  chartCard(g, L.C_per_phase, 'ch_C_phase');
  // Type × Phase matrix (rendered as HTML table)
  const m = D.C_type_phase_matrix;
  if (m && m.rows) {
    const head = '<th></th>' + m.phases.map(p => `<th>${p}</th>`).join('');
    const body = m.rows.map(r => {
      const max = Math.max(...m.phases.map(p => r[p]));
      return `<tr><td style="text-align:left">${r.type}</td>` +
        m.phases.map(p => {
          const v = r[p];
          const a = max ? Math.min(0.95, v / max * 0.85 + 0.05) : 0;
          return `<td style="background:rgba(52,152,219,${a})">${v || ''}</td>`;
        }).join('') + '</tr>';
    }).join('');
    card(g, L.C_matrix, `<table class="matrix"><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>`, true);
  }
  chartCard(g, L.C_by_year, 'ch_C_year', true, false);
  chartCard(g, L.C_by_year_type, 'ch_C_year_type', true, true);

  // --- D. 직업 이력 ---
  g = section('D', L.D);
  chartCard(g, L.D_first, 'ch_D_first');
  chartCard(g, L.D_intl, 'ch_D_intl');
  chartCard(g, L.D_orgs, 'ch_D_orgs', false, true);
  chartCard(g, L.D_moves, 'ch_D_moves');

  // --- E. 연구 ---
  g = section('E', L.E);
  chartCard(g, L.E_topics, 'ch_E_topics', true, true);
  chartCard(g, L.E_topics_per, 'ch_E_per');
  chartCard(g, L.E_breakthrough, 'ch_E_bk');

  // --- F. 학회 ---
  g = section('F', L.F);
  chartCard(g, L.F_admin, 'ch_F_admin', false, true);
  const confs = (D.F_conferences_created || [])
    .slice(0, 30)
    .map(c => `${c.year_raw || '—'}: <b>${escapeHtml(c.person)}</b> · ${escapeHtml(c.event)}`);
  if (confs.length) listCard(g, L.F_confs, confs);

  // --- G. 수상 ---
  g = section('G', L.G);
  chartCard(g, L.G_types, 'ch_G_types', false, true);
  chartCard(g, L.G_count, 'ch_G_count', false, true);
  chartCard(g, L.G_fellow, 'ch_G_fellow');

  // --- H. 창업 ---
  g = section('H', L.H);
  chartCard(g, L.H_pct, 'ch_H_pct');
  const sf = (D.H_serial_founders || [])
    .map(s => `<b>${escapeHtml(s.full_name || s.person)}</b> (${s.count}): ${(s.companies || []).map(escapeHtml).join(', ')}`);
  if (sf.length) listCard(g, L.H_serial, sf);

  // --- I. 실패 ---
  g = section('I', L.I);
  chartCard(g, L.I_subtypes, 'ch_I_sub');
  chartCard(g, L.I_with, 'ch_I_with');
  const piv = (D.I_pivot_top || []).map(x => `<b>${escapeHtml(x.person)}</b>: ${x.count}`);
  if (piv.length) listCard(g, L.I_pivot, piv);

  // --- J. 외부 ---
  g = section('J', L.J);
  chartCard(g, L.J_events, 'ch_J', true, true);

  // --- L. 한국/아시아 ---
  g = section('L', L.L);
  const kor = (D.L_korean_pioneers || []).map(p =>
    `<b>${escapeHtml(p.full_name || p.person)}</b>` +
    (p.birth_year ? ` (${p.birth_year})` : '') +
    (p.phd ? ` — PhD: ${escapeHtml(p.phd)}` : '') +
    ` · ${(p.topics || []).map(escapeHtml).join(', ')}`);
  if (kor.length) listCard(g, L.L_korean, kor);
  chartCard(g, L.L_asia, 'ch_L_asia');

  // --- M. 스토리 ---
  g = section('M', L.M);
  const tenure = (D.M_longest_tenure_top || []).slice(0, 15).map(x =>
    `<b>${escapeHtml(x.full_name || x.person)}</b> @ ${escapeHtml(x.org)} — ${x.years}${L.years} (${x.period})`);
  if (tenure.length) listCard(g, L.M_tenure, tenure);

  const div = (D.M_most_diverse_career_top || []).map(x =>
    `<b>${escapeHtml(x.full_name || x.person)}</b> · entropy=${x.entropy} · ${x.type_count} types · ${x.total_events} events`);
  if (div.length) listCard(g, L.M_diverse, div);

  const late = (D.M_latest_phd_age_top || []).map(x =>
    `<b>${escapeHtml(x.full_name || x.person)}</b>: ${x.age}세 (born ${x.birth_year}, PhD ${x.phd_year})`);
  if (late.length) listCard(g, L.M_late, late);

  const young = (D.M_youngest_phd_age_top || []).map(x =>
    `<b>${escapeHtml(x.full_name || x.person)}</b>: ${x.age}세 (born ${x.birth_year}, PhD ${x.phd_year})`);
  if (young.length) listCard(g, L.M_young, young);

  const docTop = (D.M_most_documented_lives || []).map(x =>
    `<b>${escapeHtml(x.full_name || x.person)}</b>: ${x.count}`);
  if (docTop.length) listCard(g, L.M_doc, docTop);

  // ----- 차트 채우기 -----
  // A
  chartBar('ch_A_birth',
    D.A_birth_year_decades.map(d => d.decade + 's'),
    D.A_birth_year_decades.map(d => d.count), L.persons);
  chartPie('ch_A_gender',
    D.A_gender.map(d => d.gender),
    D.A_gender.map(d => d.count));
  chartHBar('ch_A_country',
    D.A_birth_country_top.map(d => d.country),
    D.A_birth_country_top.map(d => d.count), L.persons);
  chartBar('ch_A_iv',
    D.A_interview_year.map(d => d.year),
    D.A_interview_year.map(d => d.count), L.persons);

  // B
  chartHBar('ch_B_bs_field',
    D.B_bs_field.map(d => d.field), D.B_bs_field.map(d => d.count), L.persons);
  chartHBar('ch_B_phd_field',
    D.B_phd_field.map(d => d.field), D.B_phd_field.map(d => d.count), L.persons);
  chartHBar('ch_B_bs_school',
    D.B_bs_school_top20.map(d => d.school), D.B_bs_school_top20.map(d => d.count), L.persons);
  chartHBar('ch_B_phd_school',
    D.B_phd_school_top20.map(d => d.school), D.B_phd_school_top20.map(d => d.count), L.persons);
  chartPie('ch_B_same',
    [T('동일', 'Same'), T('다름', 'Different'), T('미상', 'Unknown')],
    [D.B_same_school_bs_phd.same, D.B_same_school_bs_phd.different, D.B_same_school_bs_phd.unknown]);
  const bs2phd = histBins(D.B_bs_to_phd_years, 2);
  chartBar('ch_B_bs_phd_yrs', bs2phd.labels, bs2phd.counts, L.persons);
  chartHBar('ch_B_edu_country',
    D.B_education_countries.map(d => d.country),
    D.B_education_countries.map(d => d.count), L.persons);
  chartHBar('ch_B_advisor',
    D.B_phd_advisors_top.map(d => d.advisor),
    D.B_phd_advisors_top.map(d => d.count), L.persons);

  // C
  chartBar('ch_C_type',
    D.C_events_per_type.map(d => d.type), D.C_events_per_type.map(d => d.count), L.events);
  chartBar('ch_C_phase',
    D.C_events_per_phase.map(d => d.phase), D.C_events_per_phase.map(d => d.count), L.events);
  chartLine('ch_C_year',
    D.C_events_by_year.map(d => d.year),
    [{ label: L.events, data: D.C_events_by_year.map(d => d.count),
       borderColor: '#3498DB', backgroundColor: 'rgba(52,152,219,0.1)', fill: true }]);
  const yt = D.C_events_by_year_type;
  if (yt) {
    const COL = {'개인사':'#95A5A6','교육':'#3498DB','직업 이력':'#229954','연구·프로젝트':'#E67E22','창업·산업':'#8E44AD','학회·커뮤니티':'#16A085','수상·명예':'#F1C40F','네트워크':'#5C6BC0','실패·전환':'#C0392B','외부 영향':'#5D4037'};
    chartLine('ch_C_year_type', yt.years,
      yt.types.map(t => ({ label: t, data: yt.series[t], borderColor: COL[t] || '#666', backgroundColor: 'transparent', borderWidth: 1.5 })));
  }

  // D
  chartPie('ch_D_first',
    D.D_first_job_type.map(d => d.type),
    D.D_first_job_type.map(d => d.count));
  chartPie('ch_D_intl',
    [T('같음', 'Same'), T('다름', 'Different'), T('미상', 'Unknown')],
    [D.D_intl_migration_phd_to_first_job.same,
     D.D_intl_migration_phd_to_first_job.different,
     D.D_intl_migration_phd_to_first_job.unknown]);
  chartHBar('ch_D_orgs',
    D.D_top_orgs.map(d => d.org), D.D_top_orgs.map(d => d.count), L.persons);
  const moves = histBins(D.D_moves_per_person, 1);
  chartBar('ch_D_moves', moves.labels, moves.counts, L.persons);

  // E
  chartHBar('ch_E_topics',
    D.E_topics_top30.map(d => d.topic), D.E_topics_top30.map(d => d.count), L.persons);
  const tpp = histBins(D.E_topics_per_person, 1);
  chartBar('ch_E_per', tpp.labels, tpp.counts, L.persons);
  const bk = histBins(D.E_breakthrough_years_post_phd, 5);
  chartBar('ch_E_bk', bk.labels, bk.counts, L.events);

  // F
  chartHBar('ch_F_admin',
    D.F_admin_role_count_top.map(d => d.person),
    D.F_admin_role_count_top.map(d => d.count), L.events);

  // G
  chartHBar('ch_G_types',
    D.G_award_types_top.map(d => d.name), D.G_award_types_top.map(d => d.count), L.events);
  chartHBar('ch_G_count',
    D.G_award_count_top.map(d => d.person), D.G_award_count_top.map(d => d.count), L.events);
  const fellow = histBins(D.G_ieee_fellow_years_post_phd, 5);
  chartBar('ch_G_fellow', fellow.labels, fellow.counts, L.persons);

  // H
  chartPie('ch_H_pct',
    [T('창업 경험 있음', 'Founded'), T('없음', 'Did not')],
    [D.H_founded_pct.founded, D.H_founded_pct.not]);

  // I
  chartBar('ch_I_sub',
    D.I_setback_subtypes.map(d => d.subtype),
    D.I_setback_subtypes.map(d => d.count), L.events);
  chartPie('ch_I_with',
    [T('경험 있음', 'With'), T('없음', 'Without')],
    [D.I_persons_with_setback['with'], D.I_persons_with_setback['without']]);

  // J
  chartHBar('ch_J',
    D.J_external_events.map(d => d.event),
    D.J_external_events.map(d => d.count), L.events);

  // L
  chartBar('ch_L_asia',
    Object.keys(D.L_country_subset_counts),
    Object.values(D.L_country_subset_counts), L.persons);
}

// 키보드: ←/→ 같은 인물의 이전/다음 셀, Esc 해제
document.addEventListener('keydown', (ev) => {
  if (!selectedDiv) return;
  if (ev.key === 'Escape') { ev.preventDefault(); clearSelection(); return; }
  if (ev.key !== 'ArrowLeft' && ev.key !== 'ArrowRight') return;
  // 입력 필드에선 무시
  const tag = (ev.target && ev.target.tagName) || '';
  if (tag === 'INPUT' || tag === 'SELECT' || tag === 'TEXTAREA') return;
  ev.preventDefault();
  const dir = ev.key === 'ArrowLeft' ? -1 : 1;
  const row = selectedDiv.parentElement;
  if (!row) return;
  const cells = Array.from(row.querySelectorAll('.event'));
  const idx = cells.indexOf(selectedDiv);
  const newDiv = cells[idx + dir];
  if (newDiv && newDiv._eventData) {
    selectEvent(newDiv, newDiv._eventData);
    newDiv.scrollIntoView({ block: 'nearest', inline: 'nearest' });
  }
});

// 윈도우 리사이즈 → cell 폭 재계산 + 재렌더 (디바운스)
let resizeTimer;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    computeColW();
    buildYearHeader();
    render();
  }, 100);
});

computeColW();
buildYearHeader();
applyUrlState();
updateYearRangeUI();
applyLang();
applySelectionFromUrl();
</script>
</body>
</html>
"""


def main():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data_str = f.read()
    eda_str = '{}'
    if os.path.exists(EDA_PATH):
        with open(EDA_PATH, 'r', encoding='utf-8') as f:
            eda_str = f.read()
    html = (HTML_TEMPLATE
            .replace('__DATA__', data_str)
            .replace('__EDA__', eda_str)
            .replace('__REPO__', REPO))
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'출력: {OUT_PATH} ({os.path.getsize(OUT_PATH)/1024:.1f} KB)')


if __name__ == '__main__':
    main()
