# Control-M LinkedIn Carousel

An 11-slide LinkedIn carousel about **Control-M orchestration** with a focus on
the **SAP integration use case** and a single-page snapshot of what else
Control-M can orchestrate. Designed in BMC's brand language (deep-navy
backgrounds, orange-yellow gradient accents, Space Grotesk + Inter).

Authored by **Arshad Parwez**.

## What's inside

| Path | Description |
| --- | --- |
| `slides.html` | Source of all 11 slides (open in any browser to preview) |
| `output/slide-01.png` ... `slide-11.png` | Individual slides at 1080x1350 (LinkedIn portrait, 2x DPR) |
| `output/control-m-linkedin-carousel.pdf` | All 11 slides as a single PDF (use this for LinkedIn document posts) |
| `render.js` | Puppeteer script that produces the PNGs |
| `render-pdf.js` | Puppeteer script that produces the PDF |
| `fix-slides.js` | Helper that re-numbers slides and stamps the byline |

## Slide outline

1. Title - "Control-M? Isn't that just a monitoring tool?"
2. Myth vs Reality - side-by-side comparison + from-the-field callout
3. What Control-M actually is - definition + stats
4. The Problem - silos, no visibility, missed SLAs, audit gaps
5. Core Capabilities Part 1 - workflow, MFT, SLA, hybrid cloud
6. Core Capabilities Part 2 - jobs-as-code, predictive analytics, self-service, audit/APIs
7. Spotlight: SAP - why SAP needs orchestration
8. Control-M for SAP - layered architecture
9. Beyond SAP - 8 integration categories on one page
10. Business Value - CFO + IT/Ops + stats
11. Closing CTA - engagement prompts + hashtags

## How to upload to LinkedIn

**Option A - PDF document post (recommended):**
Click "Add a document" on a new LinkedIn post and upload
`output/control-m-linkedin-carousel.pdf`. LinkedIn renders it as a swipeable
carousel.

**Option B - Image carousel:**
Upload `slide-01.png` through `slide-11.png` in order as multiple images.

## Regenerating the slides

```bash
cd slides
npm install puppeteer
node render.js       # produces PNGs
node render-pdf.js   # produces the PDF
```
