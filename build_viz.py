"""viz_data.json + 템플릿 → visualization.html (자체 포함 단일 파일)."""
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
<title>Roboticists Oral History — 행적 시각화</title>
<style>
:root {
  --bg: #fafafa;
  --fg: #222;
  --muted: #777;
  --border: #e5e5e5;
  --row-h: 14px;
  --col-w: 7px;
  --name-w: 140px;
  --year-h: 28px;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: -apple-system, "Helvetica Neue", "Apple SD Gothic Neo", sans-serif;
       background: var(--bg); color: var(--fg); font-size: 13px; }
header { padding: 12px 18px; border-bottom: 1px solid var(--border); background: #fff; }
h1 { margin: 0 0 4px; font-size: 16px; }
.sub { color: var(--muted); font-size: 12px; }
.controls { padding: 10px 18px; border-bottom: 1px solid var(--border); background: #fff;
            display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
.controls label { font-size: 12px; }
.controls input[type=text] { padding: 4px 8px; border: 1px solid var(--border); border-radius: 4px;
                             font-size: 12px; width: 160px; }
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
.year-header .gridline { position: absolute; top: var(--year-h); width: 1px;
                         background: rgba(0,0,0,0.04); }

.rows { position: relative; }
.row { position: relative; height: var(--row-h); border-bottom: 1px solid rgba(0,0,0,0.03); }
.row:nth-child(even) { background: rgba(0,0,0,0.015); }
.name { position: absolute; left: 0; top: 0; width: var(--name-w); padding: 0 8px;
        line-height: var(--row-h); font-size: 11px; color: var(--fg);
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        border-right: 1px solid var(--border); background: #fff;
        cursor: pointer; }
.name:hover { background: #eef; }
.event { position: absolute; height: calc(var(--row-h) - 2px); top: 1px;
         width: var(--col-w); border-radius: 1px; cursor: pointer;
         transition: transform 0.05s; }
.event:hover { transform: scaleY(1.4); z-index: 4; }
.event.dim { opacity: 0.12; }
.event.inferred { opacity: 0.45; }
.event.inferred:hover { opacity: 0.85; }

.tooltip { position: fixed; background: #222; color: #fff; padding: 8px 10px;
           border-radius: 6px; font-size: 12px; max-width: 360px; line-height: 1.5;
           pointer-events: none; opacity: 0; transition: opacity 0.1s; z-index: 100;
           box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
.tooltip.show { opacity: 1; pointer-events: auto; }
.tooltip .person { font-weight: 600; margin-bottom: 4px; }
.tooltip .year { color: #aaa; font-size: 11px; }
.tooltip .ev { margin: 4px 0; }
.tooltip .meta { color: #aaa; font-size: 11px; }
.tooltip a { color: #6cf; text-decoration: none; display: block; margin-top: 6px;
             font-size: 11px; }
.tooltip a:hover { text-decoration: underline; }

footer { padding: 8px 18px; color: var(--muted); font-size: 11px;
         border-top: 1px solid var(--border); background: #fff; }
</style>
</head>
<body>
<header>
  <h1>Roboticists Oral History — 행적 시각화</h1>
  <div class="sub">110명의 거장 / 2778개 이벤트 (반투명 셀 = 원문에 연도 미상, 앞뒤 컨텍스트로 추론)</div>
</header>

<div class="controls">
  <label>정렬:
    <select id="sort">
      <option value="alpha">이름순 (가나다)</option>
      <option value="birth">출생/최초연도순 (오래된 순)</option>
      <option value="count">이벤트 수 (많은 순)</option>
    </select>
  </label>
  <label>검색:
    <input type="text" id="search" placeholder="인물명 (영문)">
  </label>
  <label>페이즈:
    <select id="phase">
      <option value="">전체</option>
      <option value="k12">k12</option>
      <option value="undergrad">undergrad</option>
      <option value="grad">grad</option>
      <option value="early_career">early_career</option>
      <option value="mid_career">mid_career</option>
      <option value="senior">senior</option>
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
  데이터 출처: <a href="__REPO__" target="_blank">__REPO__</a> ·
  클릭 시 GitHub의 한국어 인터뷰로 이동
</footer>

<script>
const VIZ_DATA = __DATA__;
const REPO = "__REPO__";

const TYPE_COLOR = {
  '개인사':       '#999999',
  '교육':         '#4A90E2',
  '직업 이력':    '#50C878',
  '연구·프로젝트': '#F39C12',
  '창업·산업':    '#9B59B6',
  '학회·커뮤니티': '#1ABC9C',
  '수상·명예':    '#F1C40F',
  '네트워크':     '#E91E63',
  '실패·전환':    '#E74C3C',
  '외부 영향':    '#5D4037',
};

const COL_W = 7, ROW_H = 14;
const Y_MIN = VIZ_DATA.year_min;
const Y_MAX = VIZ_DATA.year_max;

let activeTypes = new Set(Object.keys(TYPE_COLOR));
let currentSort = 'alpha';
let currentSearch = '';
let currentPhase = '';

function buildLegend() {
  const el = document.getElementById('legend');
  el.innerHTML = '';
  for (const [t, c] of Object.entries(TYPE_COLOR)) {
    const it = document.createElement('div');
    it.className = 'item';
    it.dataset.type = t;
    it.innerHTML = `<span class="swatch" style="background:${c}"></span><span>${t}</span>`;
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
    return ps.sort();
  } else if (currentSort === 'birth') {
    // birth_year 없으면 그 인물의 최초 이벤트 연도로 fallback
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

  // 인물별 이벤트 모으기
  const byPerson = {};
  for (const p of order) byPerson[p] = [];
  for (const e of VIZ_DATA.events) {
    if (e.year == null) continue;
    if (!activeTypes.has(e.type)) continue;
    if (currentPhase && e.phase !== currentPhase) continue;
    if (currentSearch && !e.person.includes(currentSearch.toLowerCase())) continue;
    if (byPerson[e.person]) byPerson[e.person].push(e);
  }

  let visible = 0;
  for (const p of order) {
    const evs = byPerson[p];
    if (currentSearch && !p.includes(currentSearch.toLowerCase())) continue;
    visible++;
    const row = document.createElement('div');
    row.className = 'row';
    row.style.width = (width + 140) + 'px';
    row.style.marginLeft = '-140px';

    const name = document.createElement('div');
    name.className = 'name';
    name.textContent = p;
    name.title = `${p} (이벤트 ${VIZ_DATA.persons[p].event_count}개)`;
    name.onclick = () => window.open(`${REPO}/blob/main/translated_kor/${p}.md`, '_blank');
    row.appendChild(name);

    for (const e of evs) {
      const div = document.createElement('div');
      div.className = 'event' + (e.year_inferred ? ' inferred' : '');
      div.style.left = (140 + (e.year - Y_MIN) * COL_W) + 'px';
      div.style.background = TYPE_COLOR[e.type] || '#666';
      div.addEventListener('mouseenter', (ev) => showTip(ev, e));
      div.addEventListener('mouseleave', hideTip);
      div.addEventListener('click', () => clickEvent(e));
      row.appendChild(div);
    }

    rows.appendChild(row);
  }
  document.getElementById('visible_count').textContent =
    `표시 중: ${visible}명`;
}

let tipTimeout;
function showTip(ev, e) {
  clearTimeout(tipTimeout);
  const t = document.getElementById('tooltip');
  const tlUrl = e.line_no
    ? `${REPO}/blob/main/timelines_kor/${e.person}.md#L${e.line_no}`
    : `${REPO}/blob/main/timelines_kor/${e.person}.md`;
  const intUrl = `${REPO}/blob/main/translated_kor/${e.person}.md`;
  const yearLabel = e.year_inferred
    ? `(원문: "${escapeHtml(e.year_raw)}" · 추론 ${e.year}년)`
    : `(${escapeHtml(e.year_raw)})`;
  t.innerHTML = `
    <div class="person">${e.person} <span class="year">${yearLabel}</span></div>
    <div class="ev">${escapeHtml(e.event)}</div>
    <div class="meta">${e.type} / ${e.subtype} / ${e.phase}</div>
    <a href="${tlUrl}" target="_blank">→ 타임라인의 해당 라인 열기</a>
    <a href="${intUrl}" target="_blank">→ 한국어 인터뷰 전문 열기</a>
  `;
  t.classList.add('show');
  positionTip(ev);
}
function positionTip(ev) {
  const t = document.getElementById('tooltip');
  const x = ev.clientX + 12;
  const y = ev.clientY + 12;
  t.style.left = Math.min(x, window.innerWidth - 380) + 'px';
  t.style.top = Math.min(y, window.innerHeight - 160) + 'px';
}
function hideTip() {
  // 200ms 지연: 사용자가 툴팁의 링크로 이동할 시간
  tipTimeout = setTimeout(() => {
    document.getElementById('tooltip').classList.remove('show');
  }, 250);
}
function clickEvent(e) {
  const url = e.line_no
    ? `${REPO}/blob/main/timelines_kor/${e.person}.md#L${e.line_no}`
    : `${REPO}/blob/main/timelines_kor/${e.person}.md`;
  window.open(url, '_blank');
}
function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

document.getElementById('tooltip').addEventListener('mouseenter', () => clearTimeout(tipTimeout));
document.getElementById('tooltip').addEventListener('mouseleave', hideTip);
document.getElementById('sort').addEventListener('change', (e) => { currentSort = e.target.value; render(); });
document.getElementById('search').addEventListener('input', (e) => { currentSearch = e.target.value.toLowerCase(); render(); });
document.getElementById('phase').addEventListener('change', (e) => { currentPhase = e.target.value; render(); });

buildLegend();
buildYearHeader();
render();
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
