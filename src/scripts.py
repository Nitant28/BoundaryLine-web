# -*- coding: utf-8 -*-
"""Premium animation stack: Lenis + GSAP + ScrollTrigger + SplitType."""

SCRIPT_BLOCK = r"""
(function () {
  'use strict';

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(pointer: fine)').matches;

  if (window.lucide) lucide.createIcons();

  /* ---------- Preloader ---------- */
  const pre = document.getElementById('preloader');
  const preBar = document.getElementById('preloader-bar');
  function killPre() {
    if (!pre || !window.gsap) {
      pre?.remove();
      return;
    }
    const tl = gsap.timeline({ onComplete: () => pre.remove() });
    tl.to(preBar, { width: '100%', duration: 0.85, ease: 'power3.inOut' }, 0)
      .to('.preloader-brand', { y: -40, opacity: 0, duration: 0.45, ease: 'power3.in' }, 0.55)
      .to(pre, { yPercent: -100, duration: 0.7, ease: 'power4.inOut' }, 0.7);
  }
  if (document.readyState === 'complete') setTimeout(killPre, 200);
  else window.addEventListener('load', () => setTimeout(killPre, 180));

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

  if (!window.gsap) return;
  gsap.registerPlugin(window.ScrollTrigger);

  /* ---------- SplitType hero title ---------- */
  if (window.SplitType && !reduce) {
    document.querySelectorAll('[data-split]').forEach((el) => {
      const type = el.getAttribute('data-split') || 'chars';
      const split = new SplitType(el, { types: type, tagName: 'span' });
      const targets = type.includes('chars') ? split.chars : split.words;
      gsap.set(targets, { yPercent: 120, opacity: 0 });
      gsap.to(targets, {
        yPercent: 0, opacity: 1,
        duration: 1.1, stagger: 0.028, ease: 'power4.out', delay: 1.05,
      });
    });
  }

  /* ---------- Hero intro ---------- */
  if (!reduce) {
    const heroTl = gsap.timeline({ delay: 0.95 });
    heroTl
      .from('.hero-kicker', { y: 24, opacity: 0, duration: 0.8, ease: 'power3.out' }, 0)
      .from('.hero-sub', { y: 28, opacity: 0, duration: 0.9, ease: 'power3.out' }, 0.15)
      .from('.hero-ctas .btn', { y: 24, opacity: 0, duration: 0.75, stagger: 0.08, ease: 'power3.out' }, 0.28)
      .from('.match-chip', { y: 40, opacity: 0, duration: 0.9, ease: 'power3.out' }, 0.35)
      .from('.hero-bg img', { scale: 1.12, duration: 2.2, ease: 'power2.out' }, 0);

    /* Hero parallax */
    gsap.to('.hero-bg img', {
      yPercent: 18, ease: 'none',
      scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true },
    });
  }

  /* ---------- Infinite marquees via GSAP ---------- */
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

  /* ---------- Parallax media ---------- */
  if (!reduce) {
    gsap.utils.toArray('[data-speed]').forEach((el) => {
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
