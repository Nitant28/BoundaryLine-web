# -*- coding: utf-8 -*-
"""
Boundaryline site builder.

Usage:
  python build.py

Output:
  site/   static HTML + assets
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "site"

sys.path.insert(0, str(SRC))

import components as c  # noqa: E402

OUT.mkdir(exist_ok=True)


def wrap(title, active, *sections):
    return (
        c.head(title, active)
        + c.nav(active)
        + '<main id="main">'
        + "".join(sections)
        + "</main>"
        + c.footer()
        + c.lightbox_and_wa()
        + c.page_end()
    )


PAGES = {
    "index.html": wrap(
        "BOUNDARYLINE | Cross Every Boundary",
        "home",
        c.hero(),
        c.why(),
        c.vision(),
        c.mission(),
        c.stats(),
        c.about_movement(),
        c.gallery_home(),
        c.testimonials(),
        c.team(),
        c.news_teaser(),
    ),
    "about.html": wrap(
        "About | BOUNDARYLINE",
        "about",
        c.page_hero_inner("ABOUT", "ABOUT", "Building the operating system for grassroots cricket."),
        c.about_page_body(),
    ),
    "gallery.html": wrap(
        "Gallery | BOUNDARYLINE",
        "gallery",
        c.page_hero_inner("01", "GALLERY", "Moments from grounds, academies, and match days."),
        c.gallery_body(),
    ),
    "news.html": wrap(
        "News | BOUNDARYLINE",
        "news",
        c.page_hero_inner("02", "NEWS", "Updates from the Boundaryline ecosystem."),
        c.news_body(),
    ),
    "contact.html": wrap(
        "Contact | BOUNDARYLINE",
        "contact",
        c.page_hero_inner("03", "CONTACT", "Fixtures, partnerships, media. Drop us a line."),
        c.contact_body(),
    ),
}


def build():
    for name, html in PAGES.items():
        path = OUT / name
        path.write_text(html, encoding="utf-8")
        print(f"  wrote {path.relative_to(ROOT)} ({len(html):,} bytes)")
    print(f"\nDone. Serve with:\n  python -m http.server 8080 --directory site")


if __name__ == "__main__":
    print("Building Boundaryline...\n")
    build()
