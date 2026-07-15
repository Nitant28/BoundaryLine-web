# Boundaryline website

Professional static site for Boundaryline.

## Structure

```
clientweb1/
├── build.py          # site generator
├── src/              # Python source
│   ├── data.py       # all content + copy
│   ├── assets_map.py # image path map
│   ├── components.py # HTML sections
│   ├── styles.py     # CSS + Tailwind config
│   └── scripts.py    # client JS (GSAP / Lenis)
├── media/            # source photography
├── docs/             # specs + design references
│   ├── Boundaryline-Website-Spec.pdf
│   └── references/
└── site/             # generated output (serve this)
    ├── *.html
    └── assets/
```

## Build

```bash
python build.py
```

## Run locally

```bash
python -m http.server 8080 --directory site
```

Open http://127.0.0.1:8080/
