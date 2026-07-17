# -*- coding: utf-8 -*-
"""HTML components — Boundaryline premium."""

from data import (
    uns, STAFF, TESTIMONIALS, TEAMS,
    FIXTURES_UPCOMING, FIXTURES_RESULTS, NEWS, PHOTO_GALLERY,
    HERO_SUB, VISION, VISION_EXTRA, MISSION, MISSION_POINTS, WHY_POINTS,
    PROBLEM, SOLUTION, WHAT_WE_DO, WHY_NOW, PROGRESS, PROGRESS_NOTE,
    PHILOSOPHY, LONG_TERM, FUTURE,
)
from assets_map import LOCAL, DL, HERO_LOCAL


def logo_img(variant="light", cls="", alt="Boundaryline", el_id=""):
    src = LOCAL["logo_dark"] if variant == "dark" else LOCAL["logo"]
    id_attr = f' id="{el_id}"' if el_id else ""
    eager = ' fetchpriority="high"' if el_id == "preloader-logo-img" else ""
    return f'<img src="{src}" alt="{alt}" class="brand-logo {cls}"{id_attr}{eager} decoding="async">'


def icon_svg(name):
    icons = {
        "trophy": """<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M10.5 5.5h11v6.5a5.5 5.5 0 0 1-11 0V5.5z"/><path d="M10.5 7.5H6.8a.8.8 0 0 0-.8.8c0 2.6 1.9 4.7 4.5 5"/><path d="M21.5 7.5h3.7a.8.8 0 0 1 .8.8c0 2.6-1.9 4.7-4.5 5"/><path d="M16 17.5v3.5"/><path d="M12.5 25.5h7"/><path d="M13.5 21h5l1 4.5h-7l1-4.5z"/><path class="icon-accent" d="M14 9l1.4 1.4L18 7.8"/></svg>""",
        "calendar": """<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="5" y="7.5" width="22" height="19" rx="1.5"/><path d="M5 13h22"/><path d="M11 4.5v5"/><path d="M21 4.5v5"/><path class="icon-accent" d="M9.5 17.5h3"/><path class="icon-accent" d="M14.5 17.5h3"/><path class="icon-accent" d="M19.5 17.5h3"/><path class="icon-accent" d="M9.5 22h3"/><path d="M14.5 22h3"/><path class="ic-flip" d="M22 26.5l5-5"/></svg>""",
        "network": """<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="6.5" r="3"/><circle cx="6.5" cy="24" r="3"/><circle cx="25.5" cy="24" r="3"/><path d="M16 9.5v5.5"/><path d="M16 15l-7.8 6.5"/><path d="M16 15l7.8 6.5"/><circle class="icon-accent" cx="16" cy="15" r="1.2"/></svg>""",
        "globe": """<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="10.5"/><path d="M5.5 16h21"/><g class="ic-spin"><ellipse cx="16" cy="16" rx="4.8" ry="10.5"/></g><path class="icon-accent" d="M7.5 10.5c2.4 1.4 5.3 2.2 8.5 2.2s6.1-.8 8.5-2.2"/><path class="icon-accent" d="M7.5 21.5c2.4-1.4 5.3-2.2 8.5-2.2s6.1.8 8.5 2.2"/></svg>""",
        "sun": """<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="5.2"/><path d="M16 4.5v3.2"/><path d="M16 24.3v3.2"/><path d="M4.5 16h3.2"/><path d="M24.3 16h3.2"/><path class="icon-accent" d="M7.9 7.9l2.2 2.2"/><path class="icon-accent" d="M21.9 21.9l2.2 2.2"/><path class="icon-accent" d="M24.1 7.9l-2.2 2.2"/><path class="icon-accent" d="M10.1 21.9l-2.2 2.2"/></svg>""",
        "users": """<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="12" cy="10.5" r="3.8"/><path d="M4.5 25c1.4-4.4 4.1-6.7 7.5-6.7s6.1 2.3 7.5 6.7"/><circle class="icon-accent" cx="21.5" cy="11.5" r="3"/><path class="icon-accent" d="M21 18.5c3 0 5.4 2 6.5 5.8"/></svg>""",
        "zap": """<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M18 3.5L7.5 18.5H15l-1.5 10L24 13.5h-7.5l1.5-10z"/><path class="icon-accent" d="M23 5.5l3-1.5"/><path class="icon-accent" d="M25 9.5l2.5.5"/></svg>""",
        "eye": """<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M3 16s5-8.5 13-8.5S29 16 29 16s-5 8.5-13 8.5S3 16 3 16z"/><circle cx="16" cy="16" r="4"/><circle class="icon-accent" cx="17.4" cy="14.6" r="1"/></svg>""",
    }
    return f'<span class="icon-draw" data-icon="{name}">{icons.get(name, icons["globe"])}</span>'


def head(title, active="home"):
    from styles import TAILWIND_CONFIG, STYLE_BLOCK
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Boundaryline. Building the operating system for grassroots cricket.">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=Oswald:wght@500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="assets/logo.png" fetchpriority="high">
<style>{STYLE_BLOCK}</style>
</head>
<body class="font-sans antialiased text-white selection:bg-white selection:text-black bg-black" data-page="{active}">
<a class="skip-link" href="#main">Skip to content</a>
<div id="preloader" class="preloader" aria-hidden="true">
  <div class="preloader-grain" aria-hidden="true"></div>
  <div class="preloader-inner">
    <div class="preloader-logo-wrap" id="preloader-logo-wrap">
      {logo_img("light", "preloader-logo-img", "Boundaryline", "preloader-logo-img")}
    </div>
    <span class="preloader-rule" id="preloader-rule" aria-hidden="true"></span>
    <p class="preloader-tag" id="preloader-tag">cross every boundary</p>
  </div>
  <div id="preloader-bar" class="preloader-bar"></div>
</div>
<div class="cursor-dot hidden lg:block" aria-hidden="true"></div>
<div class="cursor-outline hidden lg:block" aria-hidden="true"></div>
"""


def nav(active="home"):
    links = [
        ("index.html", "HOME", "home"),
        ("about.html", "ABOUT", "about"),
        ("gallery.html", "GALLERY", "gallery"),
        ("news.html", "NEWS", "news"),
        ("index.html#testimonials", "STORIES", "stories"),
        ("contact.html", "CONTACT", "contact"),
    ]
    desktop = "".join(
        f'<a href="{h}" class="nav-link hover-target {"is-active" if k==active else ""}">{lab}</a>'
        for h, lab, k in links
    )
    mobile = "".join(f'<a href="{h}" class="mobile-menu-link hover-target">{lab}</a>' for h, lab, k in links)
    return f"""
<nav id="navbar">
  <a href="index.html" class="nav-brand hover-target inline-flex items-center" aria-label="Boundaryline home">
    {logo_img("light", "nav-logo")}
  </a>
  <div class="nav-links t-mono">{desktop}</div>
  <div class="nav-actions">
    <a href="contact.html" class="hidden sm:inline-flex btn btn-ghost !py-2.5 !px-5 hover-target">CONTACT US</a>
    <button id="burger" class="hamburger hover-target" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</nav>
<div id="mobile-menu" class="mobile-menu" aria-hidden="true">
  <div class="mobile-menu-inner">
    <nav class="mobile-menu-nav" aria-label="Primary">
      {mobile}
    </nav>
    <div class="mobile-menu-cta">
      <a href="contact.html" class="btn btn-ghost mobile-menu-btn hover-target">CONTACT US</a>
    </div>
  </div>
</div>
"""


def _marquee_row(paths, direction="fwd", dur="48"):
    imgs = "".join(
        f'<img src="{p}" alt="" class="img-mono" loading="eager" decoding="async">'
        for p in paths
    )
    attr = "rev" if direction == "rev" else "fwd"
    return f'<div class="marquee-track"><div class="marquee-row" data-marquee="{attr}" data-dur="{dur}">{imgs}{imgs}</div></div>'


def hero():
    paths = HERO_LOCAL
    n = len(paths)
    r1, r2, r3 = paths[: n // 3], paths[n // 3 : 2 * n // 3], paths[2 * n // 3 :]
    hero_img = LOCAL["hero_player"]
    return f"""
<section id="hero" class="hero">
  <div class="hero-bg">
    <img src="{hero_img}" alt="Boundaryline cricket" class="img-mono">
  </div>
  <div class="hero-marquee-layer" aria-hidden="true">
    {_marquee_row(r1, "fwd", "52")}
    {_marquee_row(r2, "rev", "44")}
    {_marquee_row(r3, "fwd", "58")}
  </div>
  <div class="hero-shade"></div>

  <div class="hero-content">
    <div class="site-wrap">
      <div class="hero-grid">
        <div>
          <p class="hero-kicker t-mono">CROSS EVERY BOUNDARY.</p>
          <h1 class="h-display hero-title">
            <span class="hero-word" data-split="chars">BOUNDARY</span>
            <span class="hero-word" data-split="chars">LINE</span>
          </h1>
          <p class="hero-sub">{HERO_SUB.upper()}</p>
          <div class="hero-ctas">
            <a href="contact.html" class="btn btn-primary hover-target group">GET STARTED <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
            <a href="about.html" class="btn btn-ghost hover-target">WHY BOUNDARYLINE</a>
          </div>
        </div>
        <div class="match-chip">
          <div class="flex items-center gap-2 mb-2">
            <span class="status-dot"></span>
            <span class="t-mono text-[10px] text-willow" style="letter-spacing:.2em">TALK TO US</span>
          </div>
          <p class="h-display text-2xl md:text-[1.75rem] mb-1 leading-none">BOOK A FIXTURE</p>
          <p class="t-mono text-[10px] text-white/45 mt-2" style="letter-spacing:.14em">7506849705 · 8424028435</p>
          <a href="contact.html" class="t-mono text-[10px] mt-4 inline-flex items-center gap-2 text-white/70 hover:text-white hover-target" style="letter-spacing:.16em">CONTACT <i data-lucide="arrow-right" class="w-3 h-3"></i></a>
        </div>
      </div>
    </div>
  </div>
  <div class="absolute bottom-0 left-0 w-full grass-edge z-20 opacity-80"></div>
</section>
"""


def why():
    cards = "".join(f"""
      <div class="border-t border-black/10 pt-5 why-card">
        <div class="why-feature-icon">{icon_svg(icon)}</div>
        <div class="flex items-center gap-3 mb-3 text-pitch-gray">
          <span class="t-mono text-[10px] why-num" style="letter-spacing:.18em">{num}</span>
        </div>
        <h3 class="t-mono text-xs font-bold mb-3 why-title" style="letter-spacing:.16em">{title}</h3>
        <p class="text-sm text-pitch-gray leading-relaxed">{copy}</p>
      </div>""" for icon, num, title, copy in WHY_POINTS)
    return f"""
<section id="why" class="bg-chalk text-black section-pad">
  <div class="site-wrap why-grid">
    <div data-reveal>
      <p class="sec-label mb-5">01</p>
      <h2 class="h-display text-5xl md:text-7xl mb-8">WHY<br>BOUNDARYLINE?</h2>
      <p class="text-pitch-gray leading-relaxed max-w-sm text-[15px] mb-8">
        Most organizers run tournaments. We build ecosystems: the full journey, not isolated events.
      </p>
      <a href="about.html" class="btn btn-ink hover-target">READ THE FULL STORY</a>
    </div>
    <div class="why-features" data-stagger>{cards}</div>
  </div>
</section>
"""


def vision():
    return f"""
<section class="bg-black text-white section-pad overflow-hidden">
  <div class="site-wrap vision-grid">
    <div data-reveal>
      <p class="sec-label mb-4">02</p>
      <h2 class="h-display text-5xl md:text-7xl">OUR<br>VISION</h2>
    </div>
    <div data-reveal data-delay="0.1">
      <p class="text-xl md:text-[1.65rem] font-light leading-[1.5] text-white/70">{VISION}</p>
    </div>
    <div class="vision-frame media-zoom" data-reveal data-delay="0.15">
      <img src="{LOCAL['vision_match']}" alt="Grassroots cricket match in play" class="img-mono" data-speed="0.1" loading="lazy">
    </div>
  </div>
</section>
"""


def mission():
    cols = "".join(f"""
      <div>
        <div class="mb-6 icon-tile">{icon_svg(icon)}</div>
        <h3 class="t-mono text-xs font-bold mb-4" style="letter-spacing:.16em">{title}</h3>
        <p class="text-sm text-pitch-gray leading-relaxed">{copy}</p>
      </div>""" for icon, title, copy in MISSION_POINTS[:3])
    return f"""
<section class="bg-white text-black section-pad">
  <div class="site-wrap">
    <div class="mb-12" data-reveal>
      <p class="sec-label mb-4">03</p>
      <h2 class="h-display text-5xl md:text-7xl mb-6">OUR MISSION</h2>
      <p class="text-pitch-gray max-w-2xl text-[15px] leading-relaxed">{MISSION}</p>
    </div>
    <div class="mission-grid" data-stagger>{cols}</div>
  </div>
</section>
"""


def stats():
    cells = ""
    for target, suffix, label in PROGRESS:
        cells += f"""
        <div class="border-t border-white/15 pt-7">
          <p class="stat-num mb-2"><span class="counter" data-target="{target}">{"0"*len(str(target))}</span>{suffix}</p>
          <p class="t-mono text-[10px] text-white/45" style="letter-spacing:.18em">{label}</p>
        </div>"""
    return f"""
<section id="stats" class="bg-black text-white section-pad relative border-y border-white/10">
  <div class="absolute top-0 left-0 w-full grass-edge opacity-40 rotate-180"></div>
  <div class="site-wrap relative z-10">
    <div class="flex justify-between items-end mb-10" data-reveal>
      <p class="sec-label">04 / PROGRESS SO FAR</p>
      <p class="sec-label hidden md:block">UNDER 8 MONTHS</p>
    </div>
    <div class="stats-grid" style="grid-template-columns:repeat(2,1fr)" data-stagger>{cells}</div>
    <style>@media(min-width:900px){{ .stats-grid{{ grid-template-columns:repeat(4,1fr)!important; }} }}</style>
  </div>
  <div class="absolute bottom-0 left-0 w-full grass-edge opacity-40"></div>
</section>
"""


def about_movement():
    return f"""
<section class="bg-chalk text-black section-pad">
  <div class="site-wrap about-grid">
    <div data-reveal>
      <p class="sec-label mb-5">ABOUT US</p>
      <h2 class="h-display text-4xl md:text-6xl mb-6 leading-[0.92]">MORE THAN A<br>TOURNAMENT<br>COMPANY.</h2>
      <p class="text-pitch-gray leading-relaxed max-w-md text-[15px] mb-8">
        {WHAT_WE_DO}
      </p>
      <a href="about.html" class="btn btn-ink hover-target">EXPLORE ABOUT</a>
    </div>
    <div class="media-zoom aspect-[4/3] md:aspect-[5/4]" data-reveal data-delay="0.12">
      <img src="assets/gallery-01.jpg" alt="Boundaryline community" class="img-cover img-mono" loading="lazy">
    </div>
  </div>
  <div class="site-wrap mt-14" data-reveal>
    <blockquote class="bg-black text-white px-8 py-10 md:px-14 md:py-12 text-center">
      <p class="text-lg md:text-2xl font-light leading-relaxed text-white/85 italic max-w-3xl mx-auto">
        "{PHILOSOPHY}"
      </p>
    </blockquote>
  </div>
</section>
"""


def gallery_home():
    show = PHOTO_GALLERY[:7]
    sizes = ["g-lg", "", "", "g-wide", "", "", ""]
    tiles = "".join(f"""
      <div class="relative overflow-hidden media-zoom hover-target {cls}" data-lightbox="{item['src']}" data-alt="{item['alt']}">
        <img src="{item['src']}" alt="{item['alt']}" class="img-cover img-mono min-h-[180px]" loading="lazy">
      </div>""" for item, cls in zip(show, sizes))
    return f"""
<section id="gallery" class="bg-black text-white section-pad">
  <div class="site-wrap">
    <div class="flex justify-between items-end mb-12" data-reveal>
      <div>
        <p class="sec-label mb-4">05</p>
        <h2 class="h-display text-5xl md:text-7xl">GALLERY</h2>
      </div>
      <a href="gallery.html" class="t-mono text-[11px] hover-target inline-flex items-center gap-2" style="letter-spacing:.16em">
        EXPLORE MOMENTS <i data-lucide="arrow-right" class="w-4 h-4"></i>
      </a>
    </div>
    <div class="gallery-mosaic" data-stagger>{tiles}</div>
    <div class="mt-8 flex justify-end" data-reveal>
      <a href="gallery.html" class="btn btn-ghost hover-target">VIEW ALL <i data-lucide="plus" class="w-4 h-4"></i></a>
    </div>
  </div>
</section>
"""


def testimonials():
    slides = "".join(f"""
      <div class="tst-slide">
        <div class="h-full bg-black border border-white/10 p-7 md:p-8 flex flex-col justify-between hover:border-white/30 transition-colors">
          <div class="mb-8 relative">
            <span class="h-display text-6xl text-white/10 absolute -top-5 -left-1 leading-none">"</span>
            <p class="text-sm text-white/70 leading-relaxed relative z-10 italic">{t['quote']}</p>
          </div>
          <div class="flex items-center gap-4">
            <div class="w-11 h-11 rounded-full overflow-hidden bg-pitch-gray shrink-0">
              <img src="{uns(t['id'], 200)}" class="img-cover img-mono" alt="{t['name']}" loading="lazy">
            </div>
            <div>
              <p class="t-mono text-xs font-bold" style="letter-spacing:.12em">{t['name'].upper()}</p>
              <p class="text-[10px] text-white/40 uppercase tracking-wider mt-0.5">{t['role']}</p>
            </div>
          </div>
        </div>
      </div>""" for t in TESTIMONIALS)
    return f"""
<section id="testimonials" class="bg-[#111] text-white section-pad border-t border-white/10">
  <div class="site-wrap grid grid-cols-1 lg:grid-cols-12 gap-12">
    <div class="lg:col-span-3" data-reveal>
      <p class="sec-label mb-4">06</p>
      <h2 class="h-display text-5xl md:text-6xl mb-4">WHAT PEOPLE<br>SAY ABOUT US</h2>
      <p class="text-sm text-white/50 leading-relaxed mb-8 max-w-xs">Real feedback from captains, parents, coaches, and players across Mumbai.</p>
      <div class="flex gap-3">
        <button id="tst-prev" class="w-12 h-12 border border-white/20 flex items-center justify-center hover:bg-white hover:text-black transition-colors hover-target" aria-label="Previous"><i data-lucide="arrow-left" class="w-5 h-5"></i></button>
        <button id="tst-next" class="w-12 h-12 border border-white/20 flex items-center justify-center hover:bg-white hover:text-black transition-colors hover-target" aria-label="Next"><i data-lucide="arrow-right" class="w-5 h-5"></i></button>
      </div>
      <div id="tst-dots" class="flex gap-2 mt-6"></div>
    </div>
    <div class="lg:col-span-9 overflow-hidden" data-reveal data-delay="0.1">
      <div id="tst-track" class="tst-track">{slides}</div>
    </div>
  </div>
</section>
"""


def team():
    cards = "".join(f"""
      <div class="border border-black/10 pt-5 pb-4 hover-target">
        <p class="h-display text-2xl md:text-3xl mb-2 leading-tight">{m['name'].upper()}</p>
        <p class="t-mono text-[10px] text-pitch-gray" style="letter-spacing:.14em">{m['role'].upper()}</p>
      </div>""" for m in STAFF)
    return f"""
<section class="bg-chalk text-black section-pad">
  <div class="site-wrap">
    <div class="flex flex-col lg:flex-row gap-12 lg:gap-16 mb-4">
      <div class="lg:w-[28%] shrink-0" data-reveal>
        <p class="sec-label mb-4">07</p>
        <h2 class="h-display text-5xl md:text-7xl mb-6">THE TEAM</h2>
        <p class="t-mono text-[11px] text-pitch-gray" style="letter-spacing:.16em">THE PEOPLE<br>BEHIND BOUNDARYLINE</p>
      </div>
      <div class="lg:w-[72%] grid grid-cols-2 md:grid-cols-3 gap-3 md:gap-4" data-stagger>{cards}</div>
    </div>
  </div>
</section>
"""


def news_teaser():
    imgs = [PHOTO_GALLERY[0]["src"], PHOTO_GALLERY[1]["src"], PHOTO_GALLERY[3]["src"]]
    cards = ""
    for i, n in enumerate(NEWS[:3]):
        src = imgs[i % len(imgs)]
        cards += f"""
        <article class="border border-white/10 hover:border-white/25 transition-colors overflow-hidden group">
          <div class="aspect-[16/10] media-zoom">
            <img src="{src}" alt="" class="img-cover img-mono" loading="lazy">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-3 mb-3">
              <span class="t-mono text-[10px] text-white/45" style="letter-spacing:.16em">{n['tag']}</span>
              <span class="text-white/20">·</span>
              <span class="t-mono text-[10px] text-white/45" style="letter-spacing:.16em">{n['date']}</span>
            </div>
            <h3 class="h-display text-2xl mb-3 leading-tight">{n['title'].upper()}</h3>
            <p class="text-sm text-white/50 leading-relaxed mb-5 line-clamp-2">{n['excerpt']}</p>
            <a href="news.html" class="t-mono text-[10px] hover-target inline-flex items-center gap-2" style="letter-spacing:.16em">READ MORE <i data-lucide="arrow-right" class="w-3 h-3"></i></a>
          </div>
        </article>"""
    return f"""
<section class="bg-black text-white section-pad border-t border-white/10">
  <div class="site-wrap">
    <div class="flex justify-between items-end mb-12" data-reveal>
      <div>
        <p class="sec-label mb-4">08</p>
        <h2 class="h-display text-5xl md:text-7xl">LATEST NEWS</h2>
      </div>
      <a href="news.html" class="t-mono text-[11px] hover-target hidden sm:inline-flex items-center gap-2" style="letter-spacing:.16em">ALL STORIES <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5" data-stagger>{cards}</div>
  </div>
</section>
"""


def footer():
    return f"""
<footer class="bg-black text-white pt-24 pb-10 relative overflow-hidden border-t border-white/10">
  <div class="absolute inset-0 opacity-[0.22] pointer-events-none">
    <img src="{DL['lights']}" alt="" class="img-cover img-mono" loading="lazy" data-speed="0.08">
    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/85 to-black/50"></div>
  </div>
  <div class="site-wrap relative z-10">
    <div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-20" data-reveal>
      <div class="md:col-span-6">
        <div class="mb-6" data-reveal>{logo_img("light", "footer-logo")}</div>
        <p class="sec-label mb-4">09</p>
        <h2 class="h-display text-5xl md:text-7xl leading-[0.85]">CROSS EVERY<br>BOUNDARY.</h2>
        <p class="t-mono text-[10px] text-white/40 mt-6" style="letter-spacing:.16em">BOUNDARYLINE © 2026. ALL RIGHTS RESERVED.</p>
      </div>
      <div class="md:col-span-2">
        <h4 class="t-mono text-[10px] text-white/40 mb-5" style="letter-spacing:.18em">QUICK LINKS</h4>
        <ul class="space-y-3 text-sm">
          <li><a href="index.html" class="hover:text-white/50 transition-colors hover-target">Home</a></li>
          <li><a href="about.html" class="hover:text-white/50 transition-colors hover-target">About</a></li>
          <li><a href="gallery.html" class="hover:text-white/50 transition-colors hover-target">Gallery</a></li>
          <li><a href="index.html#testimonials" class="hover:text-white/50 transition-colors hover-target">Stories</a></li>
          <li><a href="news.html" class="hover:text-white/50 transition-colors hover-target">News</a></li>
          <li><a href="contact.html" class="hover:text-white/50 transition-colors hover-target">Contact</a></li>
        </ul>
      </div>
      <div class="md:col-span-4">
        <h4 class="t-mono text-[10px] text-white/40 mb-5" style="letter-spacing:.18em">GET IN TOUCH</h4>
        <ul class="space-y-3 text-sm text-white/70">
          <li><a href="mailto:info.boundaryline@gmail.com" class="hover:text-white hover-target">info.boundaryline@gmail.com</a></li>
          <li><a href="tel:+917506849705" class="hover:text-white hover-target">7506849705</a></li>
          <li><a href="tel:+918424028435" class="hover:text-white hover-target">8424028435</a></li>
          <li>Nandanvan Complex, Brahmand Thane W 400607</li>
        </ul>
        <div class="flex gap-5 mt-8">
          <a href="#" class="hover-target" aria-label="Instagram"><i data-lucide="instagram" class="w-5 h-5"></i></a>
          <a href="#" class="hover-target" aria-label="Facebook"><i data-lucide="facebook" class="w-5 h-5"></i></a>
          <a href="#" class="hover-target" aria-label="X"><i data-lucide="twitter" class="w-5 h-5"></i></a>
          <a href="#" class="hover-target" aria-label="YouTube"><i data-lucide="youtube" class="w-5 h-5"></i></a>
        </div>
      </div>
    </div>
    <div class="flex flex-col sm:flex-row justify-between gap-4 border-t border-white/10 pt-8 text-[10px] t-mono text-white/35" style="letter-spacing:.16em">
      <p>DESIGNED FOR PERFORMANCE</p>
      <div class="flex gap-8">
        <a href="#" class="hover:text-white/60">PRIVACY POLICY</a>
        <a href="#" class="hover:text-white/60">TERMS &amp; CONDITIONS</a>
      </div>
    </div>
  </div>
</footer>
"""


def lightbox_and_wa():
    return """
<div id="lightbox" class="lightbox" role="dialog" aria-modal="true">
  <button id="lightbox-close" class="absolute top-6 right-6 btn btn-ghost !py-2 hover-target">CLOSE</button>
  <img id="lightbox-img" src="" alt="">
  <p id="lightbox-cap" class="t-mono text-[10px] text-white/45 mt-4" style="letter-spacing:.16em"></p>
</div>
<a href="https://wa.me/917506849705" class="wa-float hover-target" target="_blank" rel="noopener" aria-label="WhatsApp"><i data-lucide="message-circle" class="w-6 h-6"></i></a>
<span class="wa-tip">CHAT WITH US</span>
"""


def page_end():
    from scripts import SCRIPT_BLOCK
    from styles import TAILWIND_CONFIG
    # All heavy JS loads at the end of <body> so the preloader (styled by the
    # inline <style> in <head>) paints instantly — nothing blocks first paint.
    return f"""<script src="https://cdn.tailwindcss.com"></script>
<script>{TAILWIND_CONFIG}</script>
<script src="https://unpkg.com/lucide@latest"></script>
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/split-type@0.3.4/umd/index.min.js"></script>
<script>{SCRIPT_BLOCK}</script>
</body>
</html>
"""


def page_hero_inner(num, title, subtitle=""):
    sub = f'<p class="t-mono text-[11px] text-white/45 mt-4 max-w-xl" style="letter-spacing:.14em">{subtitle}</p>' if subtitle else ""
    return f"""
<section class="page-hero bg-black text-white border-b border-white/10">
  <div class="site-wrap" data-reveal>
    <p class="sec-label mb-4">{num}</p>
    <h1 class="h-display text-5xl md:text-8xl leading-[0.88]" data-split="chars">{title}</h1>
    {sub}
  </div>
</section>
"""


def schedule_body():
    upcoming = ""
    for f in FIXTURES_UPCOMING:
        live = f["status"] == "LIVE SOON"
        status = f"""<span class="inline-flex items-center gap-2 t-mono text-[10px] {'text-willow' if live else 'text-white/45'}" style="letter-spacing:.16em">{'<span class="status-dot"></span>' if live else ''}{f['status']}</span>"""
        upcoming += f"""
        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 md:gap-6 items-center border-t border-white/10 py-6 px-1 hover:bg-white/[0.02] transition-colors" data-reveal>
          <div class="md:col-span-2 flex md:block gap-3 items-baseline">
            <span class="h-display text-3xl md:text-4xl">{f['day']}</span>
            <span class="t-mono text-[10px] text-white/45" style="letter-spacing:.14em">{f['mon']} · {f['time']}</span>
          </div>
          <div class="md:col-span-2">{status}<p class="t-mono text-[10px] text-white/40 mt-2" style="letter-spacing:.14em">{f['stage']}</p></div>
          <div class="md:col-span-5">
            <p class="h-display text-2xl md:text-3xl">{f['home']} <span class="text-white/30 text-lg">vs</span> {f['away']}</p>
            <p class="text-xs text-white/40 mt-2">{f['venue']}</p>
          </div>
          <div class="md:col-span-3 md:text-right">
            <a href="contact.html" class="btn btn-ghost !py-3 hover-target">BOOK NOW</a>
          </div>
        </div>"""
    results = "".join(f"""
      <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center border-t border-white/10 py-6 px-1" data-reveal>
        <div class="md:col-span-2"><span class="h-display text-3xl">{f['day']}</span> <span class="t-mono text-[10px] text-white/45">{f['mon']}</span></div>
        <div class="md:col-span-6">
          <p class="h-display text-xl md:text-2xl">{f['home']} <span class="text-white/40 text-sm">{f['hs']}</span> <span class="text-white/30 mx-1">vs</span> {f['away']} <span class="text-white/40 text-sm">{f['as_']}</span></p>
          <p class="text-xs text-white/40 mt-2">{f['venue']}</p>
        </div>
        <div class="md:col-span-4 md:text-right"><p class="t-mono text-[11px] text-white/70" style="letter-spacing:.1em">{f['note']}</p></div>
      </div>""" for f in FIXTURES_RESULTS)
    return f"""
<section class="bg-black text-white section-pad">
  <div class="site-wrap">
    <div class="flex gap-8 mb-8 border-b border-white/10">
      <button data-tab="panel-upcoming" class="tab-btn is-active hover-target">UPCOMING</button>
      <button data-tab="panel-results" class="tab-btn hover-target">RESULTS</button>
    </div>
    <div id="panel-upcoming" class="panel is-active">{upcoming}</div>
    <div id="panel-results" class="panel">{results}</div>
  </div>
</section>
"""


def teams_body():
    cards = ""
    for t in TEAMS:
        squad = "".join(f'<li class="t-mono text-[11px] text-white/45 py-1.5 border-b border-white/5" style="letter-spacing:.1em">{p}</li>' for p in t["squad"])
        cards += f"""
        <div class="border border-white/12 p-6 hover:border-white/30 transition-colors" data-reveal>
          <div class="flex items-start justify-between mb-6">
            <div>
              <p class="t-mono text-[10px] text-white/45 mb-2" style="letter-spacing:.18em">{t['code']}</p>
              <h3 class="h-display text-3xl">{t['name'].upper()}</h3>
            </div>
            <div class="w-14 h-14 border border-white/20 flex items-center justify-center"><span class="h-display text-xl">{t['code'][:2]}</span></div>
          </div>
          <p class="t-mono text-[10px] text-white/45 mb-1" style="letter-spacing:.14em">{t['tag']}</p>
          <p class="text-sm text-white/40 mb-4">{t['record']} · Est. {t['founded']} · {t['home']}</p>
          <button class="roster-toggle t-mono text-[10px] inline-flex items-center gap-2 hover-target border border-white/20 px-3 py-2" style="letter-spacing:.14em">SQUAD <i data-lucide="plus" class="w-3.5 h-3.5"></i></button>
          <ul class="roster mt-4">{squad}</ul>
        </div>"""
    return f'<section class="bg-black text-white section-pad"><div class="site-wrap grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4" data-stagger>{cards}</div></section>'


def gallery_body():
    chips = "".join(
        f'<button class="filter-chip hover-target {"is-active" if c=="all" else ""}" data-filter="{c}">{l}</button>'
        for c, l in [("all", "ALL"), ("action", "ACTION"), ("community", "COMMUNITY"), ("awards", "AWARDS")]
    )
    items = ""
    for i, g in enumerate(PHOTO_GALLERY):
        h = 260 + (i % 4) * 36
        items += f"""
        <div class="masonry-item gallery-item is-visible hover-target media-zoom" data-cat="{g['cat']}" data-lightbox="{g['src']}" data-alt="{g['alt']}">
          <img src="{g['src']}" alt="{g['alt']}" class="img-mono" style="width:100%;height:{h}px;object-fit:cover" loading="lazy">
        </div>"""
    return f"""
<section class="bg-black text-white section-pad">
  <div class="site-wrap">
    <div class="flex flex-wrap gap-2 mb-10" data-reveal>{chips}</div>
    <div class="masonry">{items}</div>
  </div>
</section>
"""


def about_page_body():
    problem_lis = "".join(f'<li class="border-t border-white/10 py-4 text-sm text-white/65 leading-relaxed">{p}</li>' for p in PROBLEM["points"])
    solution_cards = "".join(f"""
      <div class="border border-white/12 p-6 md:p-8">
        <p class="t-mono text-[10px] text-white/40 mb-3" style="letter-spacing:.16em">{title.upper()}</p>
        <p class="text-sm text-white/70 leading-relaxed">{copy}</p>
      </div>""" for title, copy in SOLUTION["points"])
    why_now = "".join(f'<li class="border-t border-black/10 py-4 text-sm text-pitch-gray leading-relaxed">{p}</li>' for p in WHY_NOW)
    why_cards = "".join(f"""
      <div class="border-t border-black/10 pt-5 why-card">
        <div class="why-feature-icon">{icon_svg(icon)}</div>
        <div class="flex items-center gap-3 mb-3 text-pitch-gray">
          <span class="t-mono text-[10px] why-num" style="letter-spacing:.18em">{num}</span>
        </div>
        <h3 class="t-mono text-xs font-bold mb-3 why-title" style="letter-spacing:.16em">{title}</h3>
        <p class="text-sm text-pitch-gray leading-relaxed">{copy}</p>
      </div>""" for icon, num, title, copy in WHY_POINTS)

    return f"""
<section class="bg-chalk text-black section-pad">
  <div class="site-wrap why-grid">
    <div data-reveal>
      <p class="sec-label mb-5">01</p>
      <h2 class="h-display text-5xl md:text-7xl mb-8">WHY<br>BOUNDARYLINE?</h2>
      <p class="text-pitch-gray leading-relaxed max-w-sm text-[15px]">{WHAT_WE_DO}</p>
    </div>
    <div class="why-features" data-stagger>{why_cards}</div>
  </div>
</section>

<section class="bg-black text-white section-pad">
  <div class="site-wrap grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
    <div class="lg:col-span-5" data-reveal>
      <p class="sec-label mb-5">02</p>
      <h2 class="h-display text-5xl md:text-6xl mb-6">THE PROBLEM</h2>
      <p class="text-white/65 leading-relaxed text-[15px] mb-6">{PROBLEM['lead']}</p>
      <p class="text-white/80 leading-relaxed text-[15px]">{PROBLEM['close']}</p>
    </div>
    <div class="lg:col-span-7" data-reveal data-delay="0.08">
      <ul>{problem_lis}</ul>
    </div>
  </div>
</section>

<section class="bg-[#111] text-white section-pad border-y border-white/10">
  <div class="site-wrap">
    <div class="mb-12 max-w-3xl" data-reveal>
      <p class="sec-label mb-5">03</p>
      <h2 class="h-display text-5xl md:text-6xl mb-6">OUR SOLUTION</h2>
      <p class="text-white/65 text-[15px] leading-relaxed mb-4">{SOLUTION['lead']}</p>
      <p class="text-white/65 text-[15px] leading-relaxed">{SOLUTION['close']}</p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-stagger>{solution_cards}</div>
  </div>
</section>

<section class="bg-white text-black section-pad">
  <div class="site-wrap grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
    <div class="lg:col-span-5" data-reveal>
      <p class="sec-label mb-5">04</p>
      <h2 class="h-display text-5xl md:text-6xl mb-6">WHY NOW</h2>
      <p class="text-pitch-gray text-[15px] leading-relaxed">The market is ready. Participation is rising, and families want real match experience, not only nets.</p>
    </div>
    <div class="lg:col-span-7" data-reveal data-delay="0.08">
      <ul>{why_now}</ul>
    </div>
  </div>
</section>

<section class="bg-black text-white section-pad">
  <div class="site-wrap">
    <div class="mb-12" data-reveal>
      <p class="sec-label mb-5">05</p>
      <h2 class="h-display text-5xl md:text-6xl mb-6">PROGRESS SO FAR</h2>
      <p class="text-white/65 text-[15px] leading-relaxed max-w-3xl">{PROGRESS_NOTE}</p>
    </div>
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-6" data-stagger>
      {"".join(f'''
      <div class="border-t border-white/15 pt-7">
        <p class="stat-num mb-2"><span class="counter" data-target="{t}">{"0"*len(str(t))}</span>{s}</p>
        <p class="t-mono text-[10px] text-white/45" style="letter-spacing:.18em">{lab}</p>
      </div>''' for t,s,lab in PROGRESS)}
    </div>
  </div>
</section>

<section class="bg-chalk text-black section-pad">
  <div class="site-wrap about-grid">
    <div data-reveal>
      <p class="sec-label mb-5">06</p>
      <h2 class="h-display text-4xl md:text-6xl mb-6 leading-[0.92]">LONG-TERM<br>VISION</h2>
      <p class="text-pitch-gray leading-relaxed text-[15px] mb-8">{LONG_TERM}</p>
      <p class="t-mono text-[11px] text-pitch-gray" style="letter-spacing:.14em">{PHILOSOPHY}</p>
    </div>
    <div data-reveal data-delay="0.1">
      <p class="sec-label mb-5">07</p>
      <h2 class="h-display text-4xl md:text-5xl mb-6">THE FUTURE<br>WE ARE BUILDING</h2>
      <p class="text-pitch-gray leading-relaxed text-[15px]">{FUTURE}</p>
    </div>
  </div>
</section>

<section class="bg-black text-white section-pad">
  <div class="site-wrap">
    <div class="mb-12" data-reveal>
      <p class="sec-label mb-5">08</p>
      <h2 class="h-display text-5xl md:text-6xl mb-4">OUR TEAM</h2>
      <p class="text-white/55 text-sm max-w-xl">Co-founders lead strategy and operations. Match management keeps fixtures running on the ground.</p>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-4" data-stagger>
      {"".join(f'''
      <div class="border border-white/12 p-5 md:p-6">
        <p class="h-display text-2xl md:text-3xl mb-2">{m["name"].upper()}</p>
        <p class="t-mono text-[10px] text-white/45" style="letter-spacing:.14em">{m["role"].upper()}</p>
      </div>''' for m in STAFF)}
    </div>
  </div>
</section>
"""


def news_body():
    cards = ""
    for i, n in enumerate(NEWS):
        src = PHOTO_GALLERY[i % len(PHOTO_GALLERY)]["src"]
        cards += f"""
        <article class="news-card border border-white/10 overflow-hidden hover:border-white/25 transition-colors" data-reveal>
          <div class="grid grid-cols-1 md:grid-cols-12">
            <div class="md:col-span-4 aspect-[16/10] md:aspect-auto media-zoom min-h-[180px]">
              <img src="{src}" alt="" class="img-cover img-mono" loading="lazy">
            </div>
            <div class="md:col-span-8 p-6 md:p-8 flex flex-col justify-center">
              <div class="flex gap-3 mb-3">
                <span class="t-mono text-[10px] text-white/45" style="letter-spacing:.16em">{n['tag']}</span>
                <span class="t-mono text-[10px] text-white/35" style="letter-spacing:.16em">{n['date']}</span>
              </div>
              <h3 class="h-display text-2xl md:text-3xl mb-3">{n['title'].upper()}</h3>
              <p class="text-sm text-white/50 leading-relaxed">{n['excerpt']}</p>
              <div class="news-body"><p class="text-sm text-white/50 leading-relaxed pt-3 border-t border-white/10 mt-3">{n['body']}</p></div>
              <button class="news-toggle t-mono text-[10px] mt-4 self-start hover-target" style="letter-spacing:.16em">Read more</button>
            </div>
          </div>
        </article>"""
    return f'<section class="bg-black text-white section-pad"><div class="site-wrap space-y-5">{cards}</div></section>'


def contact_body():
    return """
<section class="bg-black text-white section-pad">
  <div class="site-wrap grid grid-cols-1 lg:grid-cols-12 gap-14">
    <div class="lg:col-span-5" data-reveal>
      <h2 class="h-display text-4xl md:text-5xl mb-8">LET'S TALK</h2>
      <p class="text-white/55 text-sm leading-relaxed mb-10 max-w-sm">
        Fixtures, partnerships, academy enquiries, or media. Reach the Boundaryline team directly.
      </p>
      <ul class="space-y-5 text-white/70 text-sm mb-10">
        <li class="flex gap-4"><i data-lucide="mail" class="w-5 h-5 text-white/40 shrink-0"></i><a href="mailto:info.boundaryline@gmail.com" class="hover-target hover:text-white">info.boundaryline@gmail.com</a></li>
        <li class="flex gap-4"><i data-lucide="phone" class="w-5 h-5 text-white/40 shrink-0"></i>
          <span>
            <a href="tel:+917506849705" class="hover-target hover:text-white block">7506849705</a>
            <a href="tel:+918424028435" class="hover-target hover:text-white block mt-1">8424028435</a>
          </span>
        </li>
        <li class="flex gap-4"><i data-lucide="map-pin" class="w-5 h-5 text-white/40 shrink-0"></i>Nandanvan Complex, Brahmand Thane W 400607</li>
      </ul>
      <div class="flex gap-5">
        <a href="#" class="hover-target" aria-label="Instagram"><i data-lucide="instagram" class="w-5 h-5"></i></a>
        <a href="#" class="hover-target" aria-label="Facebook"><i data-lucide="facebook" class="w-5 h-5"></i></a>
        <a href="#" class="hover-target" aria-label="YouTube"><i data-lucide="youtube" class="w-5 h-5"></i></a>
      </div>
    </div>
    <div class="lg:col-span-7" data-reveal data-delay="0.1">
      <form id="contact-form" class="space-y-5" novalidate>
        <div>
          <label class="field-label" for="name">Name</label>
          <input id="name" name="name" required class="field-input" placeholder="Your name">
          <p class="field-error">Please enter your name.</p>
        </div>
        <div>
          <label class="field-label" for="email">Email</label>
          <input id="email" name="email" type="email" required class="field-input" placeholder="you@email.com">
          <p class="field-error">Enter a valid email.</p>
        </div>
        <div>
          <label class="field-label" for="message">Message</label>
          <textarea id="message" name="message" required rows="5" class="field-input resize-none" placeholder="How can we help?"></textarea>
          <p class="field-error">Please add a message.</p>
        </div>
        <button type="submit" class="btn btn-primary hover-target">SEND MESSAGE</button>
        <p id="form-success" class="hidden t-mono text-[11px] text-willow mt-4" style="letter-spacing:.16em">MESSAGE SENT. WE'LL BE IN TOUCH.</p>
      </form>
    </div>
  </div>
</section>
"""
