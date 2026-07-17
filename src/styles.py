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
.nav-brand{ justify-self:start; display:inline-flex; align-items:center; }
.brand-logo{ display:block; height:auto; width:auto; max-width:100%; }
.nav-logo{ height:36px; width:auto; max-width:160px; object-fit:contain; }
@media (min-width:768px){ .nav-logo{ height:42px; max-width:190px; } }
.footer-logo{ height:56px; width:auto; max-width:220px; object-fit:contain; opacity:.95; }
.preloader-logo-img, #preloader-logo-wrap .brand-logo{
  width:min(220px,62vw); height:auto; max-height:220px; object-fit:contain;
  filter:drop-shadow(0 0 36px rgba(255,255,255,.1));
}
.nav-links{ justify-self:center; display:none; gap:28px; align-items:center; }
.nav-actions{ justify-self:end; display:flex; align-items:center; gap:12px; }
@media (min-width:1100px){ .nav-links{ display:flex; } }
.nav-link{ position:relative; padding-bottom:3px; font-size:11px; letter-spacing:.2em; color:rgba(255,255,255,.72); }
.nav-link:hover,.nav-link.is-active{ color:#fff; }
.nav-link::after{ content:''; position:absolute; left:0; bottom:0; width:0; height:1px; background:#fff; transition:width .35s var(--ease); }
.nav-link:hover::after,.nav-link.is-active::after{ width:100%; }

.mobile-menu{
  position:fixed; inset:0; background:#0B0B0B; z-index:40;
  transform:translateY(-105%); transition:transform .6s var(--ease);
  display:flex; flex-direction:column; align-items:stretch;
  padding:0; overflow-y:auto;
}
.mobile-menu.is-open{ transform:translateY(0); }
.mobile-menu-inner{
  width:100%; max-width:var(--site); margin:0 auto;
  padding:clamp(96px,18vw,120px) clamp(24px,5vw,48px) clamp(40px,8vw,64px);
  display:flex; flex-direction:column; justify-content:center;
  flex:1; min-height:100%; gap:clamp(36px,6vw,56px);
  box-sizing:border-box;
}
.mobile-menu-nav{
  display:flex; flex-direction:column;
  gap:clamp(6px,1.2vw,12px);
  align-items:flex-start;
}
.mobile-menu-link{
  font-family:'Oswald',sans-serif; text-transform:uppercase;
  font-size:clamp(2rem,7.5vw,3.2rem); font-weight:600;
  letter-spacing:0.02em; line-height:1.2;
  color:rgba(255,255,255,.92);
  padding:clamp(6px,1vw,10px) 0;
  display:inline-block;
  transition:color .3s var(--ease), letter-spacing .35s var(--ease), opacity .3s;
  position:relative;
}
.mobile-menu-link:hover,
.mobile-menu-link:focus-visible{
  color:#fff; letter-spacing:0.06em; outline:none;
}
.mobile-menu-cta{
  padding-top:clamp(8px,2vw,16px);
  border-top:1px solid rgba(255,255,255,.1);
  display:flex; align-items:center;
}
.mobile-menu-btn{
  margin-top:clamp(20px,4vw,28px);
  padding:14px 28px;
  letter-spacing:.2em;
}
.hamburger{
  width:26px; height:14px; position:relative; flex-shrink:0;
  display:block; background:transparent; border:0; padding:0; cursor:pointer;
  z-index:60;
}
.hamburger span{ position:absolute; left:0; width:100%; height:1.5px; background:#fff; transition:transform .3s,opacity .3s,top .3s; }
.hamburger span:nth-child(1){ top:0; } .hamburger span:nth-child(2){ top:6px; } .hamburger span:nth-child(3){ top:12px; }
.hamburger.is-open span:nth-child(1){ top:6px; transform:rotate(45deg); }
.hamburger.is-open span:nth-child(2){ opacity:0; }
.hamburger.is-open span:nth-child(3){ top:6px; transform:rotate(-135deg); }

/* Hero — full-bleed cinematic */
.hero{
  position:relative; min-height:100svh; min-height:100dvh; width:100%;
  display:flex; flex-direction:column; justify-content:flex-end;
  overflow:hidden;
}
.hero-bg{ position:absolute; inset:0; z-index:0; overflow:hidden; }
.hero-bg img{
  position:absolute; inset:0; width:100%; height:100%;
  object-fit:cover; object-position:center 30%;
  transform-origin:center center; will-change:transform;
}
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
.hero-content{
  position:relative; z-index:5; width:100%;
  padding-bottom:clamp(48px,8vw,120px); padding-top:clamp(96px,18vw,120px);
}
.hero-grid{
  display:grid; gap:24px; align-items:end;
  grid-template-columns:1fr;
}
@media (min-width:900px){
  .hero-grid{ grid-template-columns:1.4fr .75fr; gap:40px; }
}
/* Always stack: BOUNDARY on top, LINE below — never wraps mid-word */
.hero-title{
  display:flex; flex-direction:column; align-items:flex-start;
  margin:0; max-width:100%;
  font-size:clamp(3.25rem,18vw,11.5rem);
  line-height:.78;
}
.hero-word{
  display:block; white-space:nowrap; max-width:100%;
}
.hero-title .char, .hero-title .split-char{
  display:inline-block;
}
.hero-kicker{ font-size:clamp(9px,2.5vw,11px); letter-spacing:.28em; color:rgba(255,255,255,.55); margin-bottom:clamp(12px,2vw,18px); }
.hero-sub{
  font-size:clamp(11px,2.8vw,15px); color:rgba(255,255,255,.7);
  letter-spacing:.04em; max-width:34ch; line-height:1.55;
  margin-top:clamp(14px,2.5vw,18px);
}
.hero-ctas{
  display:flex; flex-wrap:wrap; gap:10px; margin-top:clamp(20px,4vw,28px);
}
@media (max-width:639px){
  .hero-ctas .btn{ flex:1 1 auto; justify-content:center; min-height:48px; padding:12px 16px; font-size:10px; letter-spacing:.14em; }
  .match-chip{ width:100%; padding:16px 18px; }
  .hero-title{ font-size:clamp(3.1rem,19.5vw,5.5rem); }
}
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

/* ---------- Intro / preloader ---------- */
.preloader{
  position:fixed; inset:0; z-index:10000; background:#050505;
  display:flex; align-items:center; justify-content:center;
  overflow:hidden;
}
.preloader::before{
  content:''; position:absolute; inset:0;
  background:
    radial-gradient(ellipse at 50% 40%, rgba(255,255,255,.06) 0%, transparent 55%),
    linear-gradient(180deg, #0a0a0a 0%, #050505 100%);
  pointer-events:none;
}
.preloader-inner{
  position:relative; z-index:2; text-align:center;
  display:flex; flex-direction:column; align-items:center; gap:0;
  padding:24px;
}
.preloader-mark{
  width:clamp(72px,16vw,110px); height:clamp(72px,16vw,110px);
  margin-bottom:0; opacity:0; position:absolute; inset:0; margin:auto;
  display:none;
}
.preloader-logo-wrap{
  position:relative; width:auto; height:auto;
  display:flex; align-items:center; justify-content:center; margin-bottom:8px;
  opacity:1; transform:scale(1);
}
.preloader-logo-img{
  width:min(200px,58vw); height:auto; max-height:200px; object-fit:contain;
  filter:drop-shadow(0 0 40px rgba(255,255,255,.08));
}
.preloader-tag{
  font-family:'Space Mono',monospace; font-size:clamp(10px,1.6vw,12px);
  letter-spacing:.32em; text-transform:uppercase; color:rgba(255,255,255,.55);
  margin:0; opacity:1;
}
.preloader-rule{
  width:72px; height:1px; background:rgba(255,255,255,.35);
  margin:14px auto 16px; display:block;
}
.preloader.is-leaving{ pointer-events:none; }
.preloader.is-done{ display:none!important; visibility:hidden; }
/* CSS-only failsafe: even if every script fails, the intro clears itself */
.preloader{ animation:preloader-failsafe .7s ease 4s forwards; }
@keyframes preloader-failsafe{ to{ opacity:0; visibility:hidden; } }
/* If GSAP never loads, reveal-hidden content must still be visible */
.no-anim [data-reveal]{ opacity:1!important; transform:none!important; }
.no-anim [data-stagger] > *{ opacity:1!important; transform:none!important; }
.preloader-bar{
  position:absolute; bottom:0; left:0; height:1.5px; width:0;
  background:linear-gradient(90deg, transparent, #fff 20%, #fff 80%, transparent);
}
.preloader-grain{
  position:absolute; inset:0; opacity:.04; pointer-events:none; z-index:1;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* Nav logo mark */
.nav-logo-wrap{ display:inline-flex; align-items:center; }

/* Animated feature icons — stroke-drawn, monochrome, premium */
.icon-draw{
  width:30px; height:30px; display:inline-flex; align-items:center; justify-content:center;
  color:#2c2c2c; position:relative; z-index:1;
}
.icon-draw svg{ width:100%; height:100%; overflow:visible; }
.icon-draw path, .icon-draw circle, .icon-draw polyline, .icon-draw line, .icon-draw rect, .icon-draw ellipse{
  fill:none; stroke:currentColor; stroke-width:1.4; stroke-linecap:round; stroke-linejoin:round;
  transition:stroke .45s var(--ease);
}
.icon-draw .icon-accent{ stroke-width:1.1; opacity:.55; }
.why-feature-icon{
  width:52px; height:52px; border:1px solid rgba(10,10,10,.14);
  display:flex; align-items:center; justify-content:center; margin-bottom:16px;
  position:relative; overflow:hidden; cursor:default;
  transition:border-color .5s var(--ease), transform .5s var(--ease);
}
.why-feature-icon::before{
  content:''; position:absolute; inset:0; background:#0B0B0B;
  transform:translateY(101%); transition:transform .5s var(--ease); z-index:0;
}
.why-card:hover .why-feature-icon{ border-color:#0B0B0B; transform:translateY(-3px); }
.why-card:hover .why-feature-icon::before{ transform:translateY(0); }
.why-card:hover .why-feature-icon .icon-draw{ color:#fff; }
.icon-tile{
  width:52px; height:52px; border:1px solid rgba(10,10,10,.14);
  display:flex; align-items:center; justify-content:center;
  position:relative; overflow:hidden;
  transition:border-color .5s var(--ease), transform .5s var(--ease);
}
.icon-tile::before{
  content:''; position:absolute; inset:0; background:#0B0B0B;
  transform:translateY(101%); transition:transform .5s var(--ease); z-index:0;
}
.icon-tile:hover{ border-color:#0B0B0B; transform:translateY(-3px); }
.icon-tile:hover::before{ transform:translateY(0); }
.icon-tile:hover .icon-draw{ color:#fff; }
.mission .icon-draw, .bg-white .icon-draw{ color:#2c2c2c; }
.mission .why-card:hover .icon-draw, .bg-white .icon-tile:hover .icon-draw{ color:#fff; }

/* ---------- Why section — premium micro-interactions (hover/scroll only) ---------- */
.why-feature-icon .icon-draw path,
.why-feature-icon .icon-draw circle,
.why-feature-icon .icon-draw polyline,
.why-feature-icon .icon-draw line,
.why-feature-icon .icon-draw rect,
.why-feature-icon .icon-draw ellipse{ stroke-width:2; }
.why-feature-icon .icon-draw .icon-accent{ stroke-width:1.6; }

.why-card{
  transition:transform .4s cubic-bezier(.2,.8,.2,1), box-shadow .4s cubic-bezier(.2,.8,.2,1);
}
.why-card:hover{
  transform:translateY(-6px);
  box-shadow:0 22px 36px -22px rgba(11,11,11,.22);
}
.why-num{ transition:opacity .4s cubic-bezier(.2,.8,.2,1); }
.why-card:hover .why-num{ opacity:.7; }
.why-title{ transition:transform .4s cubic-bezier(.2,.8,.2,1); }
.why-card:hover .why-title{ transform:translateY(-2px); }

.why-feature-icon .icon-draw{
  transition:transform .4s cubic-bezier(.2,.8,.2,1), filter .4s ease, color .5s var(--ease);
  will-change:transform;
}
.why-card:hover .why-feature-icon .icon-draw{ transform:scale(1.06); }

/* 01 Trophy — spring tilt + faint golden glow + sparkle */
.why-card:hover .icon-draw[data-icon="trophy"]{
  transform:rotate(7deg) scale(1.08);
  transition:transform .4s cubic-bezier(.34,1.56,.64,1), filter .4s ease, color .5s var(--ease);
  filter:
    drop-shadow(0 0 3px rgba(201,162,39,.75))
    drop-shadow(0 0 9px rgba(201,162,39,.5))
    drop-shadow(0 0 16px rgba(201,162,39,.22));
}
.why-card:hover .why-feature-icon:has(.icon-draw[data-icon="trophy"]){
  box-shadow:
    0 0 0 1px rgba(201,162,39,.18),
    0 0 18px rgba(201,162,39,.16);
}
.icon-draw[data-icon="trophy"]::before,
.icon-draw[data-icon="trophy"]::after{
  content:''; position:absolute; width:4px; height:4px; border-radius:50%;
  background:#C9A227;
  box-shadow:0 0 7px rgba(201,162,39,.9);
  opacity:0; pointer-events:none;
}
.icon-draw[data-icon="trophy"]::before{ top:-2px; left:2px; }
.icon-draw[data-icon="trophy"]::after{ top:1px; right:-2px; }
.why-card:hover .icon-draw[data-icon="trophy"]::before{ animation:sparkle .5s ease-out forwards; }
.why-card:hover .icon-draw[data-icon="trophy"]::after{ animation:sparkle .5s ease-out .12s forwards; }
@keyframes sparkle{
  0%{ opacity:0; transform:scale(.2); }
  40%{ opacity:1; transform:scale(1); }
  100%{ opacity:0; transform:scale(1.5) translateY(-3px); }
}

/* 02 Calendar — slight tilt, corner flip, soft shadow */
.why-card:hover .icon-draw[data-icon="calendar"]{
  transform:rotate(-3deg) scale(1.05);
  filter:drop-shadow(0 3px 4px rgba(0,0,0,.3));
}
.icon-draw[data-icon="calendar"] .ic-flip{
  transform-box:fill-box; transform-origin:left bottom;
  transition:transform .4s ease-out;
}
.why-card:hover .icon-draw[data-icon="calendar"] .ic-flip{ transform:rotate(-14deg); }

/* 03 Network — independent node pulses, 2px lift */
.why-card:hover .icon-draw[data-icon="network"]{ transform:translateY(-2px) scale(1.04); }
.icon-draw[data-icon="network"] circle{ transform-box:fill-box; transform-origin:center; }
.why-card:hover .icon-draw[data-icon="network"] circle:nth-of-type(1){ animation:node-pulse 1.5s ease-in-out infinite; }
.why-card:hover .icon-draw[data-icon="network"] circle:nth-of-type(2){ animation:node-pulse 1.5s ease-in-out .2s infinite; }
.why-card:hover .icon-draw[data-icon="network"] circle:nth-of-type(3){ animation:node-pulse 1.5s ease-in-out .4s infinite; }
@keyframes node-pulse{ 0%,100%{ transform:scale(1); } 50%{ transform:scale(1.14); } }

/* 04 Globe — meridians spin while hovered, subtle glow */
.why-card:hover .icon-draw[data-icon="globe"]{
  transform:scale(1.05);
  filter:drop-shadow(0 0 5px rgba(255,255,255,.22));
}
.icon-draw[data-icon="globe"] .ic-spin{ transform-box:view-box; transform-origin:50% 50%; }
.why-card:hover .icon-draw[data-icon="globe"] .ic-spin{ animation:globe-spin 2s linear infinite; }
@keyframes globe-spin{ to{ transform:rotate(360deg); } }

/* Button — border draws in, arrow slides (same button, same colors) */
.btn{ position:relative; }
.btn svg{ transition:transform .35s var(--ease); }
.btn:hover svg{ transform:translateX(6px); }
.btn-ink::before, .btn-ink::after{
  content:''; position:absolute; left:0; width:100%; height:1px; background:#0B0B0B;
  transform:scaleX(0); transition:transform .45s cubic-bezier(.2,.8,.2,1); pointer-events:none;
}
.btn-ink::before{ top:-1px; transform-origin:left center; }
.btn-ink::after{ bottom:-1px; transform-origin:right center; }
.btn-ink:hover::before, .btn-ink:hover::after{ transform:scaleX(1); }

.vision-frame{
  position:relative; overflow:hidden;
  height:clamp(240px,32vw,360px);
}
.vision-frame img{ width:100%; height:110%; object-fit:cover; object-position:center 35%; }
.vision-frame::after{
  content:''; position:absolute; inset:0;
  background:linear-gradient(180deg, transparent 50%, rgba(11,11,11,.45) 100%);
  pointer-events:none;
}

@media (prefers-reduced-motion:reduce){
  *{ animation:none!important; transition:none!important; }
  [data-reveal]{ opacity:1; transform:none; }
  body{ cursor:auto; }
  .preloader{ display:none!important; }
  /* Fade-only: no rotations, scaling, or lifts */
  .why-card:hover,
  .why-card:hover .why-title,
  .why-card:hover .icon-draw,
  .why-card:hover .icon-draw *,
  .btn:hover svg{ transform:none!important; filter:none!important; }
}
"""
