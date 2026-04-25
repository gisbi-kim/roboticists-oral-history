"""viz_data.json + 템플릿 → visualization.html (자체 포함, KO/EN 토글)."""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, 'viz_data.json')
OUT_PATH = os.path.join(BASE, 'visualization.html')

REPO = 'https://github.com/gisbi-kim/roboticists-oral-history'

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>Roboticists Oral History — Career Timeline</title>
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

.controls { padding: 10px 18px; border-bottom: 1px solid var(--border); background: #fff;
            display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
.controls label { font-size: 12px; }
.controls input[type=text] { padding: 4px 8px; border: 1px solid var(--border); border-radius: 4px;
                             font-size: 12px; width: 180px; }
.controls select { padding: 4px 6px; border: 1px solid var(--border); border-radius: 4px;
                   font-size: 12px; background: #fff; }
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

.rows { position: relative; }
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
  <span class="sub" id="visible_count"></span>
</div>

<div class="legend" id="legend"></div>

<div class="viz">
  <div class="year-header" id="year_header"></div>
  <div class="rows" id="rows" style="margin-left: var(--name-w);"></div>
</div>

<div class="tooltip" id="tooltip"></div>

<footer>
  <span id="footer_text"></span>
</footer>

<script>
const VIZ_DATA = __DATA__;
const REPO = "__REPO__";

// 네트워크(slate)와 실패·전환(red)이 색공간에서 멀어지도록 재선정.
// 의미와 색상 매핑:
//   회색=중립(개인사), 파랑=학습(교육), 녹=안정(직업), 주황=활동(연구),
//   보라=비즈니스(창업), 청록=커뮤니티, 노랑=명예, 짙은 슬레이트=네트워크,
//   빨강=경고/실패, 짙은 갈색=외부 영향
const TYPE_COLOR = {
  '개인사':       '#95A5A6',
  '교육':         '#3498DB',
  '직업 이력':    '#2ECC71',
  '연구·프로젝트': '#E67E22',
  '창업·산업':    '#9B59B6',
  '학회·커뮤니티': '#1ABC9C',
  '수상·명예':    '#F1C40F',
  '네트워크':     '#34495E',
  '실패·전환':    '#C0392B',
  '외부 영향':    '#6E2C00',
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
    title: 'Roboticists Oral History — 행적 시각화',
    sub: '110명의 거장 / 2778개 이벤트 (반투명 셀 = 원문에 연도 미상, 앞뒤 컨텍스트로 추론)',
    sort: '정렬:',
    sort_birth: '출생/최초연도순',
    sort_alpha: '이름순 (가나다)',
    sort_count: '이벤트 수 (많은 순)',
    search: '검색:',
    search_ph: '이름 (영문)',
    phase: '페이즈:',
    visible: (n) => `표시 중: ${n}명`,
    tip_year_inferred: (raw, y) => `(원문: "${raw}" · 추론 ${y}년)`,
    footer: `데이터: <a href="${REPO}" target="_blank">${REPO}</a>`,
    link_timeline: '[타임라인]',
    link_interview: '[인터뷰전문]',
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
    visible: (n) => `Showing: ${n} people`,
    tip_year_inferred: (raw, y) => `(source: "${raw}" · inferred ${y})`,
    footer: `Data: <a href="${REPO}" target="_blank">${REPO}</a>`,
    link_timeline: '[Timeline]',
    link_interview: '[Interview]',
  },
};

const COL_W = 7, ROW_H = 14;
const Y_MIN = VIZ_DATA.year_min;
const Y_MAX = VIZ_DATA.year_max;

let lang = 'ko';
let activeTypes = new Set(Object.keys(TYPE_COLOR));
let currentSort = 'birth';
let currentSearch = '';
let currentPhase = '';

function applyLang() {
  const t = I18N[lang];
  document.title = t.title;
  document.getElementById('page_title').textContent = t.title;
  document.getElementById('page_sub').textContent = t.sub;
  document.getElementById('lbl_sort').textContent = t.sort;
  document.getElementById('lbl_search').textContent = t.search;
  document.getElementById('lbl_phase').textContent = t.phase;
  document.getElementById('search').placeholder = t.search_ph;
  document.getElementById('footer_text').innerHTML = t.footer;

  const sortSel = document.getElementById('sort');
  sortSel.options[0].textContent = t.sort_birth;
  sortSel.options[1].textContent = t.sort_alpha;
  sortSel.options[2].textContent = t.sort_count;

  const phaseSel = document.getElementById('phase');
  const ph = PHASE_LABELS[lang];
  for (const o of phaseSel.options) o.textContent = ph[o.value];

  buildLegend();
  render();
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
      const ay = VIZ_DATA.persons[a].birth_year ?? earliest[a] ?? 9999;
      const by = VIZ_DATA.persons[b].birth_year ?? earliest[b] ?? 9999;
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

  const byPerson = {};
  for (const p of order) byPerson[p] = [];
  for (const e of VIZ_DATA.events) {
    if (e.year == null) continue;
    if (!activeTypes.has(e.type)) continue;
    if (currentPhase && e.phase !== currentPhase) continue;
    if (byPerson[e.person]) byPerson[e.person].push(e);
  }

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
    row.style.width = (width + 280) + 'px';
    row.style.marginLeft = '-280px';
    row.addEventListener('mouseenter', () => row.classList.add('hl'));
    row.addEventListener('mouseleave', () => row.classList.remove('hl'));

    const name = document.createElement('div');
    name.className = 'name';
    const yrTag = meta.birth_year ? ` (${meta.birth_year}-)` : '';
    const intvTgt = lang === 'en' ? 'ethw_source_eng' : 'translated_kor';
    const i18 = I18N[lang];
    name.innerHTML = `
      <span class="pname" title="${escapeHtml(fullName)}${yrTag} · ${meta.event_count} events">${escapeHtml(fullName)}${yrTag}</span>
      <a class="lnk" href="${REPO}/blob/main/timelines_kor/${p}.md" target="_blank">${i18.link_timeline}</a>
      <a class="lnk" href="${REPO}/blob/main/${intvTgt}/${p}.md" target="_blank">${i18.link_interview}</a>
    `;
    name.querySelector('.pname').onclick = () => {
      window.open(`${REPO}/blob/main/${intvTgt}/${p}.md`, '_blank');
    };
    row.appendChild(name);

    for (const e of evs) {
      const div = document.createElement('div');
      div.className = 'event' + (e.year_inferred ? ' inferred' : '');
      div.style.left = (280 + (e.year - Y_MIN) * COL_W) + 'px';
      div.style.background = TYPE_COLOR[e.type] || '#666';
      div.addEventListener('mouseenter', (ev) => showTip(ev, e));
      div.addEventListener('mousemove', positionTip);
      div.addEventListener('mouseleave', hideTip);
      div.addEventListener('click', () => clickEvent(e));
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
  const fullName = (VIZ_DATA.persons[e.person]?.full_name) || e.person;
  const yearLabel = e.year_inferred
    ? i.tip_year_inferred(escapeHtml(e.year_raw), e.year)
    : `(${escapeHtml(e.year_raw)})`;
  const typeLabel = lang === 'en' ? (TYPE_EN[e.type] || e.type) : e.type;
  const phaseLabel = PHASE_LABELS[lang][e.phase] || e.phase;
  t.innerHTML = `
    <div class="person">${escapeHtml(fullName)} <span class="year">${yearLabel}</span></div>
    <div class="ev">${escapeHtml(e.event)}</div>
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
    document.getElementById('tooltip').classList.remove('show');
  }, 250);
}
function clickEvent(e) {
  const tgt = lang === 'en' ? 'ethw_source_eng' : 'translated_kor';
  window.open(`${REPO}/blob/main/${tgt}/${e.person}.md`, '_blank');
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
});
document.getElementById('btn_en').addEventListener('click', () => {
  lang = 'en';
  document.getElementById('btn_en').classList.add('active');
  document.getElementById('btn_ko').classList.remove('active');
  applyLang();
});

buildYearHeader();
applyLang();
</script>
</body>
</html>
"""


def main():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data_str = f.read()
    html = HTML_TEMPLATE.replace('__DATA__', data_str).replace('__REPO__', REPO)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'출력: {OUT_PATH} ({os.path.getsize(OUT_PATH)/1024:.1f} KB)')


if __name__ == '__main__':
    main()
