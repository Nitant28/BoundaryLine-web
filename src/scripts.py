# -*- coding: utf-8 -*-
"""Premium animation stack: Lenis + GSAP + ScrollTrigger + SplitType."""

SCRIPT_BLOCK = r"""
(function () {
  'use strict';

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(pointer: fine)').matches;

  if (window.lucide) lucide.createIcons();

  /* ---------- Premium logo intro (fail-safe, never blank) ---------- */
  const pre = document.getElementById('preloader');
  const preBar = document.getElementById('preloader-bar');
  const logoWrap = document.getElementById('preloader-logo-wrap');
  const tag = document.getElementById('preloader-tag');
  const rule = document.getElementById('preloader-rule');
  let introStarted = false;
  let introFinished = false;
  let heroStarted = false;

  function finishIntro() {
    if (introFinished) return;
    introFinished = true;
    document.documentElement.classList.add('intro-done');
    document.documentElement.style.overflow = '';
    // Always land at the top so nothing is shifted down after refresh
    window.scrollTo(0, 0);
    if (window.__lenis) window.__lenis.scrollTo(0, { immediate: true });
    if (pre) {
      pre.classList.add('is-done');
      if (pre.parentNode) pre.remove();
    }
    if (typeof startHeroMotion === 'function') startHeroMotion();
  }

  function runIntro() {
    if (introStarted) return;
    introStarted = true;

    // Hard kill — never leave users on a black screen
    const failSafe = window.setTimeout(finishIntro, 2600);

    // If the CSS failsafe already faded the preloader (very slow network), skip the intro
    if (!pre || getComputedStyle(pre).visibility === 'hidden') {
      window.clearTimeout(failSafe);
      finishIntro();
      return;
    }

    if (!window.gsap || reduce) {
      if (!window.gsap) document.documentElement.classList.add('no-anim');
      window.clearTimeout(failSafe);
      finishIntro();
      return;
    }

    document.documentElement.style.overflow = 'hidden';

    // Keep logo visible from first paint; only refine motion
    const tl = gsap.timeline({
      defaults: { ease: 'power3.out' },
      onComplete: () => {
        window.clearTimeout(failSafe);
        finishIntro();
      },
    });

    if (preBar) tl.to(preBar, { width: '100%', duration: 1.2, ease: 'power2.inOut' }, 0);
    if (logoWrap) tl.fromTo(logoWrap, { scale: 0.96 }, { scale: 1, duration: 0.7 }, 0);
    if (rule) tl.fromTo(rule, { scaleX: 0.6, opacity: 0.5 }, { scaleX: 1, opacity: 1, duration: 0.45 }, 0.35);
    if (tag) tl.fromTo(tag, { y: 8, opacity: 0.7 }, { y: 0, opacity: 1, duration: 0.45 }, 0.4);

    tl.to(pre, { autoAlpha: 0, duration: 0.55, ease: 'power2.inOut' }, 1.55);
  }

  // Start ASAP — do NOT wait for full window.load (that caused the black blank)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runIntro, { once: true });
  } else {
    runIntro();
  }

  /* ---------- Lenis + GSAP tick ---------- */
  let lenis;
  if (!reduce && window.Lenis) {
    lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });
    document.documentElement.classList.add('lenis', 'lenis-smooth');
    window.__lenis = lenis;
    if (window.gsap && window.ScrollTrigger) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    } else {
      (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    }
  }

  /* ---------- Custom cursor ---------- */
  const dot = document.querySelector('.cursor-dot');
  const outline = document.querySelector('.cursor-outline');
  if (fine && !reduce && dot && outline && window.gsap) {
    const pos = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    const mouse = { x: pos.x, y: pos.y };
    window.addEventListener('mousemove', (e) => { mouse.x = e.clientX; mouse.y = e.clientY; });
    gsap.ticker.add(() => {
      pos.x += (mouse.x - pos.x) * 0.22;
      pos.y += (mouse.y - pos.y) * 0.22;
      gsap.set(dot, { x: mouse.x, y: mouse.y });
      gsap.set(outline, { x: pos.x, y: pos.y });
    });
    document.querySelectorAll('a,button,.hover-target,.masonry-item,.media-zoom').forEach((el) => {
      el.addEventListener('mouseenter', () => outline.classList.add('is-active'));
      el.addEventListener('mouseleave', () => outline.classList.remove('is-active'));
    });
  }

  /* ---------- Navbar ---------- */
  const navbar = document.getElementById('navbar');
  const syncNav = () => navbar?.classList.toggle('is-scrolled', (window.scrollY || lenis?.scroll || 0) > 40);
  if (lenis) lenis.on('scroll', syncNav);
  else window.addEventListener('scroll', syncNav, { passive: true });
  syncNav();

  const burger = document.getElementById('burger');
  const mobile = document.getElementById('mobile-menu');
  if (burger && mobile) {
    const toggle = () => {
      const open = mobile.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      if (lenis) open ? lenis.stop() : lenis.start();
    };
    burger.addEventListener('click', toggle);
    mobile.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => mobile.classList.contains('is-open') && toggle()));
  }

  if (!window.gsap) {
    document.documentElement.classList.add('no-anim');
    return;
  }
  gsap.registerPlugin(window.ScrollTrigger);

  /* ---------- SplitType + hero (after intro, once) ---------- */
  function startHeroMotion() {
    if (heroStarted || reduce || !window.gsap) return;
    heroStarted = true;

    if (window.SplitType) {
      document.querySelectorAll('[data-split]').forEach((el) => {
        if (el.dataset.splitDone === '1') return;
        el.dataset.splitDone = '1';
        const type = el.getAttribute('data-split') || 'chars';
        const split = new SplitType(el, { types: type, tagName: 'span' });
        const targets = type.includes('chars') ? split.chars : split.words;
        gsap.set(targets, { yPercent: 120, opacity: 0 });
        gsap.to(targets, {
          yPercent: 0, opacity: 1,
          duration: 1.05, stagger: 0.026, ease: 'power4.out', delay: 0.04,
        });
      });
    }

    const heroTl = gsap.timeline({ delay: 0.06 });
    heroTl
      .from('.hero-kicker', { y: 24, opacity: 0, duration: 0.75, ease: 'power3.out' }, 0)
      .from('.hero-sub', { y: 28, opacity: 0, duration: 0.85, ease: 'power3.out' }, 0.12)
      .from('.hero-ctas .btn', { y: 24, opacity: 0, duration: 0.7, stagger: 0.08, ease: 'power3.out' }, 0.24)
      .from('.match-chip', { y: 36, opacity: 0, duration: 0.85, ease: 'power3.out' }, 0.3)
      // Scale only — never translate Y (that left the black gap at the top on refresh)
      .fromTo('.hero-bg img',
        { scale: 1.08 },
        { scale: 1, duration: 2, ease: 'power2.out', clearProps: 'transform' },
        0
      );
  }

  // If intro already skipped / missing, start hero once
  if (!document.getElementById('preloader')) startHeroMotion();

  /* ---------- Animated icon stroke draws (scroll-in + hover replay) ---------- */
  if (!reduce) {
    document.querySelectorAll('.icon-draw').forEach((wrap) => {
      const main = [];
      const accent = [];
      wrap.querySelectorAll('path, circle, polyline, line, rect, ellipse').forEach((el) => {
        let len = 80;
        try {
          if (el.getTotalLength) len = el.getTotalLength();
        } catch (e) {}
        el.dataset.len = String(len);
        el.style.strokeDasharray = String(len);
        el.style.strokeDashoffset = String(len);
        (el.classList.contains('icon-accent') ? accent : main).push(el);
      });

      const draw = (fast) => {
        gsap.killTweensOf([...main, ...accent]);
        gsap.set([...main, ...accent], { strokeDashoffset: (i, el) => +el.dataset.len });
        const tl = gsap.timeline();
        tl.to(main, {
          strokeDashoffset: 0,
          duration: fast ? 0.55 : 1.1,
          stagger: fast ? 0.05 : 0.1,
          ease: 'power2.inOut',
        }, 0);
        if (accent.length) {
          tl.to(accent, {
            strokeDashoffset: 0,
            duration: fast ? 0.4 : 0.7,
            stagger: fast ? 0.06 : 0.12,
            ease: 'power2.out',
          }, fast ? 0.25 : 0.55);
        }
        return tl;
      };

      ScrollTrigger.create({
        trigger: wrap,
        start: 'top 90%',
        once: true,
        onEnter: () => {
          draw(false);
          gsap.fromTo(wrap, { scale: 0.85, rotate: -4 }, { scale: 1, rotate: 0, duration: 0.9, ease: 'back.out(1.6)' });
        },
      });

      // Redraw on hover of the surrounding tile / card
      const hoverHost = wrap.closest('.why-card, .icon-tile, .why-feature-icon') || wrap;
      let last = 0;
      hoverHost.addEventListener('pointerenter', () => {
        const now = Date.now();
        if (now - last < 700) return;
        last = now;
        draw(true);
      });
    });
  }
  if (!reduce) {
    document.querySelectorAll('[data-marquee]').forEach((row) => {
      const dir = row.getAttribute('data-marquee') === 'rev' ? 1 : -1;
      const dur = parseFloat(row.getAttribute('data-dur') || '45');
      const total = row.scrollWidth / 2;
      gsap.to(row, {
        x: dir * -total,
        duration: dur,
        ease: 'none',
        repeat: -1,
        modifiers: {
          x: gsap.utils.unitize((x) => {
            const v = parseFloat(x);
            return ((v % total) + total) % total * (dir < 0 ? -1 : 1) * (dir < 0 ? 1 : -1);
          }),
        },
      });
      // Simpler reliable loop:
      gsap.killTweensOf(row);
      gsap.set(row, { x: dir > 0 ? -total : 0 });
      gsap.to(row, {
        x: dir > 0 ? 0 : -total,
        duration: dur,
        ease: 'none',
        repeat: -1,
      });
    });
  }

  /* ---------- Scroll reveals ---------- */
  if (reduce) {
    document.querySelectorAll('[data-reveal]').forEach((el) => el.classList.add('is-in'));
  } else {
    gsap.utils.toArray('[data-reveal]').forEach((el) => {
      const delay = parseFloat(el.getAttribute('data-delay') || '0');
      gsap.fromTo(el,
        { opacity: 0, y: 56 },
        {
          opacity: 1, y: 0, duration: 1.15, delay, ease: 'power3.out',
          scrollTrigger: { trigger: el, start: 'top 88%', toggleActions: 'play none none none' },
        }
      );
    });

    gsap.utils.toArray('[data-stagger]').forEach((parent) => {
      const kids = parent.children;
      gsap.from(kids, {
        opacity: 0, y: 40, duration: 0.95, stagger: 0.1, ease: 'power3.out',
        scrollTrigger: { trigger: parent, start: 'top 85%' },
      });
    });
  }

  /* ---------- Counters ---------- */
  document.querySelectorAll('.counter').forEach((counter) => {
    const target = +counter.dataset.target;
    const obj = { val: 0 };
    ScrollTrigger.create({
      trigger: counter,
      start: 'top 90%',
      once: true,
      onEnter: () => {
        gsap.to(obj, {
          val: target, duration: 2, ease: 'power2.out',
          onUpdate: () => {
            const n = Math.round(obj.val);
            counter.textContent = n < target ? String(n).padStart(String(target).length, '0') : target.toLocaleString();
          },
        });
      },
    });
  });

  /* ---------- Parallax media (skip hero — Y shift caused top black gap) ---------- */
  if (!reduce) {
    gsap.utils.toArray('[data-speed]').forEach((el) => {
      if (el.closest('#hero, .hero-bg')) return;
      const speed = parseFloat(el.getAttribute('data-speed') || '0.2');
      gsap.to(el, {
        yPercent: speed * 40,
        ease: 'none',
        scrollTrigger: { trigger: el.parentElement || el, start: 'top bottom', end: 'bottom top', scrub: true },
      });
    });
  }

  /* ---------- Testimonials ---------- */
  const track = document.getElementById('tst-track');
  const dotsWrap = document.getElementById('tst-dots');
  if (track) {
    const slides = [...track.querySelectorAll('.tst-slide')];
    let index = 0;
    const per = () => (window.innerWidth >= 1100 ? 3 : window.innerWidth >= 768 ? 2 : 1);
    const max = () => Math.max(0, slides.length - per());
    function renderDots() {
      if (!dotsWrap) return;
      dotsWrap.innerHTML = '';
      for (let i = 0; i <= max(); i++) {
        const b = document.createElement('button');
        b.className = 'tst-dot' + (i === index ? ' is-active' : '');
        b.setAttribute('aria-label', 'Slide ' + (i + 1));
        b.addEventListener('click', () => { index = i; go(); });
        dotsWrap.appendChild(b);
      }
    }
    function go() {
      index = Math.max(0, Math.min(index, max()));
      gsap.to(track, { xPercent: -(100 / per()) * index, duration: 0.75, ease: 'power3.out' });
      renderDots();
    }
    document.getElementById('tst-prev')?.addEventListener('click', () => { index--; go(); });
    document.getElementById('tst-next')?.addEventListener('click', () => { index++; go(); });
    window.addEventListener('resize', go);
    go();
  }

  /* ---------- Gallery filter + lightbox ---------- */
  const chips = document.querySelectorAll('.filter-chip');
  const items = document.querySelectorAll('.gallery-item');
  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      chips.forEach((c) => c.classList.remove('is-active'));
      chip.classList.add('is-active');
      const cat = chip.dataset.filter;
      items.forEach((item) => item.classList.toggle('is-visible', cat === 'all' || item.dataset.cat === cat));
      ScrollTrigger.refresh();
    });
  });
  if (chips[0]) chips[0].click();

  const lightbox = document.getElementById('lightbox');
  const lbImg = document.getElementById('lightbox-img');
  const lbCap = document.getElementById('lightbox-cap');
  document.querySelectorAll('[data-lightbox]').forEach((el) => {
    el.addEventListener('click', () => {
      if (!lightbox || !lbImg) return;
      lbImg.src = el.getAttribute('data-lightbox');
      if (lbCap) lbCap.textContent = el.getAttribute('data-alt') || '';
      lightbox.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      lenis?.stop();
    });
  });
  function closeLb() {
    lightbox?.classList.remove('is-open');
    document.body.style.overflow = '';
    lenis?.start();
  }
  document.getElementById('lightbox-close')?.addEventListener('click', closeLb);
  lightbox?.addEventListener('click', (e) => { if (e.target === lightbox) closeLb(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeLb(); });

  /* ---------- Tabs / accordions / form ---------- */
  document.querySelectorAll('[data-tab]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.tab;
      document.querySelectorAll('[data-tab]').forEach((b) => b.classList.toggle('is-active', b === btn));
      document.querySelectorAll('.panel').forEach((p) => p.classList.toggle('is-active', p.id === id));
    });
  });
  document.querySelectorAll('.roster-toggle').forEach((btn) => {
    btn.addEventListener('click', () => {
      btn.classList.toggle('is-open');
      btn.parentElement.querySelector('.roster')?.classList.toggle('is-open');
    });
  });
  document.querySelectorAll('.news-toggle').forEach((btn) => {
    btn.addEventListener('click', () => {
      const body = btn.closest('.news-card')?.querySelector('.news-body');
      body?.classList.toggle('is-open');
      btn.textContent = body?.classList.contains('is-open') ? 'Show less' : 'Read more';
    });
  });

  const form = document.getElementById('contact-form');
  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    let ok = true;
    form.querySelectorAll('[required]').forEach((field) => {
      const err = field.parentElement.querySelector('.field-error');
      const invalid = !field.value.trim() || (field.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value));
      field.classList.toggle('is-invalid', invalid);
      err?.classList.toggle('is-visible', invalid);
      if (invalid) ok = false;
    });
    if (ok) {
      document.getElementById('form-success')?.classList.remove('hidden');
      form.reset();
    }
  });

  /* Active section nav */
  const sections = [...document.querySelectorAll('section[id]')];
  const links = document.querySelectorAll('.nav-link[href*="#"]');
  if (sections.length && links.length) {
    ScrollTrigger.create({
      start: 0, end: 'max',
      onUpdate: () => {
        const y = (lenis?.scroll || window.scrollY) + 130;
        let cur = sections[0]?.id;
        sections.forEach((s) => { if (s.offsetTop <= y) cur = s.id; });
        links.forEach((a) => {
          const href = a.getAttribute('href') || '';
          a.classList.toggle('is-active', href.endsWith('#' + cur));
        });
      },
    });
  }
})();
"""
