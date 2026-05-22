// One-time fix-up: re-numbers slides 1..N consistently, fixes duplicate IDs,
// rebalances progress bars, and stamps the author byline on every slide.
const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'slides.html');
let html = fs.readFileSync(file, 'utf8');

const BYLINE = 'By Arshad Parwez';

const sectionOpenRegex = /<section class="slide" id="s\d+">/g;
const sections = [];
let m;
while ((m = sectionOpenRegex.exec(html)) !== null) {
  sections.push(m.index);
}
const total = sections.length;
console.log(`Found ${total} slides; re-stamping...`);

for (let i = total - 1; i >= 0; i--) {
  const start = sections[i];
  const end = i + 1 < total ? sections[i + 1] : html.indexOf('</body>', start);
  let block = html.slice(start, end);
  const num = i + 1;
  const numStr = String(num).padStart(2, '0');
  const totalStr = String(total).padStart(2, '0');
  const pct = Math.round((num / total) * 100);

  block = block.replace(
    /<section class="slide" id="s\d+">/,
    `<section class="slide" id="s${num}">`
  );
  block = block.replace(
    /<div class="slide-num"><span>\d+<\/span>\s*\/\s*\d+<\/div>/,
    `<div class="slide-num"><span>${numStr}</span> / ${totalStr}</div>`
  );
  block = block.replace(
    /<div class="bottom-bar">\s*<span>[^<]*<\/span>\s*<div class="progress-track"><div class="progress-fill" style="width:[^"]*"><\/div><\/div>\s*<span>[^<]*<\/span>\s*<\/div>/,
    `<div class="bottom-bar">\n    <span>${BYLINE}</span>\n    <div class="progress-track"><div class="progress-fill" style="width:${pct}%"></div></div>\n    <span>${numStr} / ${totalStr}</span>\n  </div>`
  );

  html = html.slice(0, start) + block + html.slice(end);
}

html = html.replace(
  /SWIPE\s*&rarr;\s*\d+\s*SLIDES,\s*[^<]*</,
  `SWIPE  &rarr;  ${total} SLIDES, 2 MINUTES<`
);

fs.writeFileSync(file, html);
console.log(`Done. ${total} slides re-stamped with byline "${BYLINE}".`);
