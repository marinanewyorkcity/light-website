# marinanewyorkcity.com

The official website of Marina Kapler, creator behind [@marina.newyorkcity](https://www.instagram.com/marina.newyorkcity/).

A fast, hand-coded static site (no builders, no trackers) hosted free on GitHub Pages and served at https://marinanewyorkcity.com.

## Updating

- **Text and layout:** edit `index.html` and `styles.css` directly. Every push to `main` redeploys the site automatically within a minute or two.
- **News & events and the trip planner:** edit `events.json`. Each entry is `{ "title", "start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "text", "location" }`. The News section shows the next 3 upcoming events; the trip planner matches events against the visitor's dates.

## Images

All images live in the repo root next to `index.html`:
- `hero.jpg`, `logo.png`, `about-marina.jpg`, `empire.jpg`
- `logo-01.png` through `logo-24.png` (client/partner logos, shown in the scrolling marquee)
- Gallery: `gallery-01.jpg` through `gallery-08.jpg` — drop files with these names into the repo root and they appear in the gallery automatically (with lightbox, no code changes needed)
