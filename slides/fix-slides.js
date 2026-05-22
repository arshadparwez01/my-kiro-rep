// One-time fix-up: re-numbers slides 1..N consistently, fixes duplicate IDs,
// rebalances progress bars, and replaces every bottom-bar section label with
// the author byline.
const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'slides.html');
let html = fs.readFileSync(file, 'utf8');

const BYLINE = 'By Arshad Parwez   &middot;   LinkedIn';

// Walk every <section class="slide" id="..."> in document order, re-stamping
// the id, the top-bar slide-num, the bottom-bar slide-num, the progress
// width and the bottom-bar label.
const sectionOpenRegex = /<section class="slide" id="s\d+">/g;
const sections = [];
let m;
while ((m = sectionOpenRegex.exec(html)) !== null) {
  sections.push(m.index);
}
const total = sections.length;
console.log(`Found ${total} slides; re-stamping...`);

// Build slice ranges (start..nextStart) so we can rewrite each slide block independently.
for (let i = total - 1; i >= 0; i--) {
  const start = sections[i];
  const end = i + 1 < total ? sections[i + 1] : html.indexOf('</body>', start);
  let block = html.slice(start, end);
  const num = i + 1;
  const numStr = String(num).padStart(2, '0');
  const totalStr = String(total).padStart(2, '0');
  const pct = Math.round((num / total) * 100);

  // 1. Section opening tag id
  block = block.replace(
    /<section class="slide" id="s\d+">/,
    `<section class="slide" id="s${num}">`
  );

  // 2. Top-bar slide indicator: <div class="slide-num"><span>NN</span> / TT</div>
  block = block.replace(
    /<div class="slide-num"><span>\d+<\/span>\s*\/\s*\d+<\/div>/,
    `<div class="slide-num"><span>${numStr}</span> / ${totalStr}</div>`
  );

  // 3. Bottom-bar: replace label, progress width, and slide-num
  block = block.replace(
    /<div class="bottom-bar">\s*<span>[^<]*<\/span>\s*<div class="progress-track"><div class="progress-fill" style="width:[^"]*"><\/div><\/div>\s*<span>\d+<\/span>\s*<\/div>/,
    `<div class="bottom-bar">\n    <span>${BYLINE}</span>\n    <div class="progress-track"><div class="progress-fill" style="width:${pct}%"></div></div>\n    <span>${numStr} / ${totalStr}</span>\n  </div>`
  );

  html = html.slice(0, start) + block + html.slice(end);
}

// Also bump the title hint that says "10 SLIDES, 2 MINUTES" to match actual count
html = html.replace(
  /SWIPE\s*&rarr;\s*\d+\s*SLIDES,\s*[^<]*</,
  `SWIPE  &rarr;  ${total} SLIDES, 2 MINUTES<`
);

fs.writeFileSync(file, html);
console.log(`Done. ${total} slides re-stamped with byline "${BYLINE}".`);
