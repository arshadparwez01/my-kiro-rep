// Renders slides.html into a single multi-page PDF for LinkedIn document posts.
// One page per .slide section, sized 1080x1350 px.
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const OUT_PDF = path.join(__dirname, 'output', 'control-m-linkedin-carousel.pdf');
const HTML_PATH = 'file://' + path.join(__dirname, 'slides-pdf.html');

(async () => {
  // Build a print-friendly version: each slide on its own page, no extra gaps.
  const src = fs.readFileSync(path.join(__dirname, 'slides.html'), 'utf8');
  const printified = src.replace(
    '</style>',
    `
    @page { size: 1080px 1350px; margin: 0; }
    body { gap: 0 !important; padding: 0 !important; background: #050810 !important; }
    .slide { page-break-after: always; break-after: page; margin: 0 !important; }
    .slide:last-of-type { page-break-after: auto; break-after: auto; }
    </style>`
  );
  fs.writeFileSync(path.join(__dirname, 'slides-pdf.html'), printified);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });
  await page.goto(HTML_PATH, { waitUntil: 'networkidle0' });
  await page.evaluateHandle('document.fonts.ready');

  await page.pdf({
    path: OUT_PDF,
    width: '1080px',
    height: '1350px',
    printBackground: true,
    preferCSSPageSize: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });

  await browser.close();
  console.log('PDF written to', OUT_PDF);
})().catch(err => { console.error(err); process.exit(1); });
