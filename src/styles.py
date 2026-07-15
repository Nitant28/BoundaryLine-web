# -*- coding: utf-8 -*-

TAILWIND_CONFIG = """
tailwind.config = {
  theme: {
    extend: {
      colors: {
        black: '#0B0B0B',
        white: '#ffffff',
        'pitch-gray': '#3A3A3A',
        chalk: '#F4F4F2',
        'line-gray': '#D9D9D6',
        willow: '#C9A227',
      },
      fontFamily: {
        display: ['Oswald', 'sans-serif'],
        sans: ['DM Sans', 'sans-serif'],
        mono: ['Space Mono', 'monospace'],
      },
      maxWidth: { site: '1400px' },
      spacing: {
        'section': 'clamp(80px, 12vw, 140px)',
        'gutter': 'clamp(20px, 4vw, 48px)',
      },
      letterSpacing: {
        tighter: '-0.02em',
        widest: '0.22em',
      }
    }
  }
}
"""

STYLE_BLOCK = """
:root{
  --black:#0B0B0B;
  --chalk:#F4F4F2;
  --line:rgba(217,217,214,.14);
  --ink:rgba(11,11,11,.12);
  --ease:cubic-bezier(0.16,1,0.3,1);
  --gutter:clamp(20px,4vw,48px);
  --site:1400px;
}
*{ box-sizing:border-box; }
html{ scroll-behavior:auto; }
html.lenis,html.lenis body{ height:auto; }
.lenis.lenis-smooth{ scroll-behavior:auto!important; }
body{
  background:var(--black); color:#fff; overflow-x:hidden;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility;
  cursor:none;
}
@media (max-width:1023px),(pointer:coarse){ body{ cursor:auto; } .cursor-dot,.cursor-outline{ display:none!important; } }

.site-wrap{ width:100%; max-width:var(--site); margin-inline:auto; padding-inline:var(--gutter); }
.section-pad{ padding-block:clamp(72px,11vw,132px); }

/* Cursor */
.cursor-dot,.cursor-outline{ position:fixed; top:0; left:0; transform:translate(-50%,-50%); border-radius:50%; z-index:9999; pointer-events:none; mix-blend-mode:difference; }
.cursor-dot{ width:6px; height:6px; background:#fff; }
.cursor-outline{ width:38px; height:38px; border:1px solid rgba(255,255,255,.55); transition:width .3s var(--ease),height .3s var(--ease),background .3s; }
.cursor-outline.is-active{ width:70px; height:70px; background:rgba(255,255,255,.1); }

.h-display{ font-family:'Oswald',sans-serif; text-transform:uppercase; line-height:.88; letter-spacing:-0.025em; font-weight:600; }
.t-mono{ font-family:'Space Mono',monospace; text-transform:uppercase; letter-spacing:.18em; }
.sec-label{ font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.22em; text-transform:uppercase; color:#8a8a8a; }

a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{ outline:2px solid #fff; outline-offset:3px; }
.bg-chalk a:focus-visible,.bg-white a:focus-visible,.bg-chalk button:focus-visible,.bg-white button:focus-visible{ outline-color:#0B0B0B; }
.skip-link{ position:absolute; left:-9999px; top:0; background:#fff; color:#0B0B0B; padding:12px 20px; z-index:100; font-family:'Space Mono',monospace; font-size:12px; letter-spacing:.1em; text-transform:uppercase; }
.skip-link:focus{ left:12px; top:12px; }

.img-mono{ filter:grayscale(100%) contrast(1.12) brightness(.9); }
.img-cover{ width:100%; height:100%; object-fit:cover; display:block; }
.media-zoom{ overflow:hidden; }
.media-zoom img{ transition:transform 1.1s var(--ease), filter .6s ease; }
.group:hover .media-zoom img,.media-zoom:hover img{ transform:scale(1.06); }

.hairline{ border-color:var(--line)!important; }
.hairline-ink{ border-color:var(--ink)!important; }

::-webkit-scrollbar{ width:5px; }
::-webkit-scrollbar-track{ background:#0B0B0B; }
::-webkit-scrollbar-thumb{ background:#3A3A3A; }

/* Nav — exact mockup: logo left, links center, CTA right */
#navbar{
  position:fixed; inset:0 0 auto 0; z-index:50; height:78px;
  display:grid; grid-template-columns:1fr auto 1fr; align-items:center;
  padding-inline:var(--gutter);
  transition:background .4s ease, backdrop-filter .4s ease, border-color .4s ease, height .35s ease;
  border-bottom:1px solid transparent;
}
#navbar.is-scrolled{ height:64px; background:rgba(11,11,11,.82); backdrop-filter:blur(18px); border-color:rgba(217,217,214,.1); }
.nav-brand{ justify-self:start; }
.nav-links{ justify-self:center; display:none; gap:28px; align-items:center; }
.nav-actions{ justify-self:end; display:flex; align-items:center; gap:12px; }
@media (min-width:1100px){ .nav-links{ display:flex; } }
.nav-link{ position:relative; padding-bottom:3px; font-size:11px; letter-spacing:.2em; color:rgba(255,255,255,.72); }
.nav-link:hover,.nav-link.is-active{ color:#fff; }
.nav-link::after{ content:''; position:absolute; left:0; bottom:0; width:0; height:1px; background:#fff; transition:width .35s var(--ease); }
.nav-link:hover::after,.nav-link.is-active::after{ width:100%; }

.mobile-menu{ position:fixed; inset:0; background:#0B0B0B; z-index:40; transform:translateY(-105%); transition:transform .6s var(--ease); display:flex; flex-direction:column; padding:100px var(--gutter) 40px; }
.mobile-menu.is-open{ transform:translateY(0); }
.mobile-menu a{ font-family:'Oswald',sans-serif; text-transform:uppercase; font-size:clamp(2.2rem,8vw,3.4rem); letter-spacing:-0.02em; line-height:1.15; }
.hamburger{ width:26px; height:14px; position:relative; }
.hamburger span{ position:absolute; left:0; width:100%; height:1.5px; background:#fff; transition:transform .3s,opacity .3s,top .3s; }
.hamburger span:nth-child(1){ top:0; } .hamburger span:nth-child(2){ top:6px; } .hamburger span:nth-child(3){ top:12px; }
.hamburger.is-open span:nth-child(1){ top:6px; transform:rotate(45deg); }
.hamburger.is-open span:nth-child(2){ opacity:0; }
.hamburger.is-open span:nth-child(3){ top:6px; transform:rotate(-135deg); }

/* Hero — full-bleed cinematic */
.hero{
  position:relative; min-height:100svh; width:100%;
  display:flex; flex-direction:column; justify-content:flex-end;
  overflow:hidden;
}
.hero-bg{ position:absolute; inset:0; z-index:0; }
.hero-bg img{ width:100%; height:115%; object-fit:cover; object-position:center 30%; will-change:transform; }
.hero-marquee-layer{ position:absolute; inset:0; z-index:1; opacity:.28; pointer-events:none; display:flex; flex-direction:column; justify-content:center; gap:12px; transform:rotate(-1.5deg) scale(1.12); }
.marquee-track{ overflow:hidden; width:100%; }
.marquee-row{ display:flex; width:max-content; gap:12px; will-change:transform; }
.marquee-row img{ height:clamp(140px,18vw,220px); width:auto; object-fit:cover; flex-shrink:0; }
.hero-shade{
  position:absolute; inset:0; z-index:2;
  background:
    linear-gradient(180deg, rgba(11,11,11,.45) 0%, rgba(11,11,11,.25) 35%, rgba(11,11,11,.85) 78%, #0B0B0B 100%),
    radial-gradient(ellipse at 50% 40%, transparent 0%, rgba(0,0,0,.55) 100%);
}
.hero-content{ position:relative; z-index:5; width:100%; padding-bottom:clamp(72px,10vw,120px); padding-top:120px; }
.hero-grid{
  display:grid; gap:32px; align-items:end;
  grid-template-columns:1fr;
}
@media (min-width:900px){
  .hero-grid{ grid-template-columns:1.4fr .75fr; gap:40px; }
}
.hero-title{ font-size:clamp(4.2rem,14vw,11.5rem); line-height:.78; }
.hero-kicker{ font-size:11px; letter-spacing:.28em; color:rgba(255,255,255,.55); margin-bottom:18px; }
.hero-sub{ font-size:clamp(12px,1.1vw,15px); color:rgba(255,255,255,.7); letter-spacing:.04em; max-width:34ch; line-height:1.55; margin-top:18px; }
.hero-ctas{ display:flex; flex-wrap:wrap; gap:12px; margin-top:28px; }
.match-chip{
  backdrop-filter:blur(14px); background:rgba(11,11,11,.55);
  border:1px solid rgba(255,255,255,.14); padding:18px 20px;
}

/* Buttons */
.btn{ display:inline-flex; align-items:center; gap:10px; font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.18em; text-transform:uppercase; padding:14px 26px; transition:background .3s,color .3s,border-color .3s,transform .35s var(--ease); }
.btn-primary{ background:#fff; color:#0B0B0B; }
.btn-primary:hover{ background:#D9D9D6; }
.btn-ghost{ border:1px solid rgba(255,255,255,.4); color:#fff; }
.btn-ghost:hover{ border-color:#fff; background:rgba(255,255,255,.05); }
.btn-ink{ border:1px solid rgba(11,11,11,.3); color:#0B0B0B; }
.btn-ink:hover{ border-color:#0B0B0B; }

/* Grid sections matching mockup */
.why-grid{
  display:grid; gap:48px;
  grid-template-columns:1fr;
}
@media (min-width:960px){
  .why-grid{ grid-template-columns:minmax(240px,.9fr) 1.4fr; gap:64px; align-items:start; }
}
.why-features{
  display:grid; gap:36px 40px;
  grid-template-columns:1fr;
}
@media (min-width:640px){ .why-features{ grid-template-columns:1fr 1fr; } }

.vision-grid{
  display:grid; gap:40px; align-items:center;
  grid-template-columns:1fr;
}
@media (min-width:960px){
  .vision-grid{ grid-template-columns:.7fr 1.1fr .95fr; gap:48px; }
}

.mission-grid{
  display:grid; gap:40px;
  grid-template-columns:1fr;
  border-top:1px solid var(--ink); padding-top:48px;
}
@media (min-width:800px){
  .mission-grid{ grid-template-columns:repeat(3,1fr); gap:0; }
  .mission-grid > * + *{ border-left:1px solid var(--ink); padding-left:40px; }
  .mission-grid > *:not(:last-child){ padding-right:40px; }
}

.stats-grid{
  display:grid; gap:28px 20px;
  grid-template-columns:repeat(2,1fr);
}
@media (min-width:700px){ .stats-grid{ grid-template-columns:repeat(3,1fr); } }
@media (min-width:1100px){ .stats-grid{ grid-template-columns:repeat(6,1fr); } }
.stat-num{ font-family:'Oswald',sans-serif; font-size:clamp(2.2rem,4.5vw,3.6rem); letter-spacing:-0.02em; line-height:1; }

.gallery-mosaic{
  display:grid; gap:12px;
  grid-template-columns:repeat(2,1fr);
  grid-auto-rows:minmax(160px,auto);
}
@media (min-width:800px){
  .gallery-mosaic{
    grid-template-columns:repeat(4,1fr);
    grid-template-rows:repeat(2,minmax(260px,1fr));
  }
  .gallery-mosaic .g-lg{ grid-column:span 2; grid-row:span 2; }
  .gallery-mosaic .g-wide{ grid-column:span 2; }
}

.team-grid{
  display:grid; gap:12px;
  grid-template-columns:repeat(2,1fr);
}
@media (min-width:700px){ .team-grid{ grid-template-columns:repeat(3,1fr); } }
@media (min-width:1100px){ .team-grid{ grid-template-columns:repeat(5,1fr); } }

.about-grid{
  display:grid; gap:40px; align-items:center;
  grid-template-columns:1fr;
}
@media (min-width:900px){ .about-grid{ grid-template-columns:1fr 1.15fr; gap:56px; } }

/* Split text chars for GSAP */
.split-line{ overflow:hidden; display:block; }
.split-word,.split-char{ display:inline-block; will-change:transform,opacity; }

/* GSAP initial states */
[data-reveal]{ opacity:0; transform:translateY(48px); }
[data-reveal].is-in{ opacity:1; transform:none; }

.grass-edge{
  height:22px; width:100%;
  background:linear-gradient(180deg,transparent,rgba(0,0,0,.4));
  mask-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 18' preserveAspectRatio='none'%3E%3Cpath fill='white' d='M0 18 L3 6 L6 16 L10 2 L14 14 L18 4 L22 15 L26 1 L30 13 L34 5 L38 17 L42 3 L46 12 L50 0 L54 14 L58 6 L62 16 L66 2 L70 13 L74 7 L78 17 L82 4 L86 12 L90 1 L94 15 L98 5 L102 14 L106 3 L110 11 L114 6 L118 16 L120 18 Z'/%3E%3C/svg%3E");
  -webkit-mask-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 18' preserveAspectRatio='none'%3E%3Cpath fill='white' d='M0 18 L3 6 L6 16 L10 2 L14 14 L18 4 L22 15 L26 1 L30 13 L34 5 L38 17 L42 3 L46 12 L50 0 L54 14 L58 6 L62 16 L66 2 L70 13 L74 7 L78 17 L82 4 L86 12 L90 1 L94 15 L98 5 L102 14 L106 3 L110 11 L114 6 L118 16 L120 18 Z'/%3E%3C/svg%3E");
  mask-size:100% 100%; -webkit-mask-size:100% 100%;
}

.status-dot{ width:7px; height:7px; border-radius:999px; background:#C9A227; box-shadow:0 0 0 3px rgba(201,162,39,.25); animation:pulse-dot 1.8s ease infinite; }
@keyframes pulse-dot{ 0%,100%{ box-shadow:0 0 0 3px rgba(201,162,39,.25);} 50%{ box-shadow:0 0 0 6px rgba(201,162,39,.08);} }

.tst-track{ display:flex; }
.tst-slide{ flex:0 0 100%; padding:0 8px; }
@media (min-width:768px){ .tst-slide{ flex:0 0 50%; } }
@media (min-width:1100px){ .tst-slide{ flex:0 0 33.333%; } }
.tst-dot{ width:8px; height:8px; border-radius:999px; background:rgba(255,255,255,.25); border:0; padding:0; transition:width .3s,background .3s; }
.tst-dot.is-active{ background:#fff; width:22px; border-radius:4px; }

.masonry{ column-count:1; column-gap:12px; }
@media (min-width:640px){ .masonry{ column-count:2; } }
@media (min-width:1024px){ .masonry{ column-count:3; } }
.masonry-item{ break-inside:avoid; margin-bottom:12px; overflow:hidden; cursor:pointer; }
.gallery-item{ display:none; } .gallery-item.is-visible{ display:block; }
.filter-chip{ border:1px solid rgba(255,255,255,.25); padding:8px 16px; font-family:'Space Mono',monospace; font-size:10px; letter-spacing:.18em; text-transform:uppercase; transition:background .25s,color .25s; }
.filter-chip.is-active{ background:#fff; color:#0B0B0B; }

.lightbox{ position:fixed; inset:0; background:rgba(10,10,10,.96); z-index:200; display:none; align-items:center; justify-content:center; flex-direction:column; }
.lightbox.is-open{ display:flex; }
.lightbox img{ max-width:88vw; max-height:76vh; object-fit:contain; }

.tab-btn{ position:relative; padding-bottom:10px; color:#8a8a8a; font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.18em; text-transform:uppercase; }
.tab-btn.is-active{ color:#fff; }
.tab-btn::after{ content:''; position:absolute; left:0; bottom:0; height:2px; width:0; background:#fff; transition:width .3s; }
.tab-btn.is-active::after{ width:100%; }
.panel{ display:none; } .panel.is-active{ display:block; }

.roster{ max-height:0; overflow:hidden; transition:max-height .5s var(--ease); }
.roster.is-open{ max-height:320px; }
.roster-toggle svg{ transition:transform .35s; }
.roster-toggle.is-open svg{ transform:rotate(45deg); }
.news-body{ max-height:0; overflow:hidden; transition:max-height .55s var(--ease); }
.news-body.is-open{ max-height:420px; }

.field-input{ background:transparent; border:1px solid rgba(255,255,255,.22); color:#fff; width:100%; padding:14px 16px; font-size:14px; transition:border-color .25s; }
.field-input:focus{ border-color:#fff; outline:none; }
.field-input::placeholder{ color:#6b6b6b; }
.field-label{ font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:#8a8a8a; display:block; margin-bottom:8px; }
.field-error{ display:none; color:#e5b8b8; font-family:'Space Mono',monospace; font-size:11px; margin-top:6px; }
.field-error.is-visible{ display:block; }
.field-input.is-invalid{ border-color:#c97878; }

.wa-float{ position:fixed; right:20px; bottom:20px; z-index:80; width:52px; height:52px; border-radius:999px; background:#fff; color:#0B0B0B; display:flex; align-items:center; justify-content:center; box-shadow:0 8px 28px rgba(0,0,0,.45); transition:transform .35s var(--ease); }
.wa-float:hover{ transform:scale(1.08); }
.wa-tip{ position:fixed; right:82px; bottom:34px; z-index:80; background:#fff; color:#0B0B0B; font-family:'Space Mono',monospace; font-size:11px; letter-spacing:.05em; padding:8px 12px; opacity:0; transform:translateX(6px); transition:opacity .3s,transform .3s; pointer-events:none; white-space:nowrap; }
.wa-float:hover ~ .wa-tip{ opacity:1; transform:translateX(0); }

.page-hero{ padding-top:160px; padding-bottom:64px; }
.preloader{ position:fixed; inset:0; z-index:10000; background:#0B0B0B; display:flex; align-items:center; justify-content:center; }
.preloader-brand{ font-family:'Oswald',sans-serif; font-size:clamp(2rem,6vw,3.5rem); letter-spacing:-0.02em; overflow:hidden; }
.preloader-bar{ position:absolute; bottom:0; left:0; height:2px; width:0; background:#fff; }

@media (prefers-reduced-motion:reduce){
  *{ animation:none!important; transition:none!important; }
  [data-reveal]{ opacity:1; transform:none; }
  body{ cursor:auto; }
}
"""
