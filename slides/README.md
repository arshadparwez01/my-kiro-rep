# Control-M LinkedIn Carousel

A 9-slide LinkedIn carousel about **Control-M orchestration** with a focus on
the **SAP integration use case**. Designed in BMC's brand language
(deep-navy backgrounds, orange-yellow gradient accents, Space Grotesk + Inter).

## What's inside

| Path | Description |
| --- | --- |
| `slides.html` | Source of all 9 slides (open in any browser to preview) |
| `output/slide-01.png` ... `slide-09.png` | Individual slides at 1080x1350 (LinkedIn portrait, 2x DPR) |
| `output/control-m-linkedin-carousel.pdf` | All 9 slides as a single PDF (use this for LinkedIn document posts) |
| `render.js` | Puppeteer script that produces the PNGs |
| `render-pdf.js` | Puppeteer script that produces the PDF |

## Slide outline

1. Title - "The engine behind every mission-critical workflow"
2. What is Control-M? (with stats)
3. The problem: silos, no visibility, missed SLAs, audit gaps
4. Core capabilities part 1: workflow, MFT, SLAs, hybrid/multi-cloud
5. Core capabilities part 2: jobs-as-code, predictive analytics, self-service, audit/APIs
6. Spotlight: why SAP needs orchestration (S/4HANA, BW, ECC, etc.)
7. Architecture: Control-M -> SAP module -> SAP workloads + non-SAP stack
8. Business value (CFO + IT/Ops + stats)
9. Closing CTA with hashtags

## How to upload to LinkedIn

**Option A - PDF document post (recommended):**
Click "Add a document" on a new LinkedIn post and upload
`output/control-m-linkedin-carousel.pdf`. LinkedIn will render it as a
swipeable carousel automatically.

**Option B - Image carousel:**
Upload `slide-01.png` through `slide-09.png` in order as multiple images on
a single post.

## Regenerating the slides

```bash
cd slides
npm install puppeteer
node render.js       # produces PNGs
node render-pdf.js   # produces the PDF
```
