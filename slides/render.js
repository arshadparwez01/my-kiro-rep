// Renders each .slide section in slides.html as a 1080x1350 PNG
// suitable for a LinkedIn portrait carousel.
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.join(__dirname, 'output');
const HTML_PATH = 'file://' + path.join(__dirname, 'slides.html');

(async () => {
  if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=medium'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });
  await page.goto(HTML_PATH, { waitUntil: 'networkidle0' });

  // Wait an extra tick for fonts
  await page.evaluateHandle('document.fonts.ready');

  const ids = await page.$$eval('.slide', els => els.map(e => e.id));
  console.log(`Found ${ids.length} slides:`, ids);

  for (let i = 0; i < ids.length; i++) {
    const id = ids[i];
    const handle = await page.$('#' + id);
    const fileName = `slide-${String(i + 1).padStart(2, '0')}.png`;
    const outPath = path.join(OUT_DIR, fileName);
    await handle.screenshot({ path: outPath, omitBackground: false });
    console.log(`✓ ${fileName}`);
  }

  await browser.close();
  console.log('\nDone. Output in:', OUT_DIR);
})().catch(err => {
  console.error(err);
  process.exit(1);
});
