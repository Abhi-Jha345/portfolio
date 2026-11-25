(() => {
  const doc = document.documentElement;
  doc.classList.add('js');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // language
  const setLang = (lang) => {
    document.querySelectorAll('[data-en]').forEach((el) => {
      const v = el.getAttribute('data-' + lang);
      if (v !== null) el.textContent = v;
    });
    doc.lang = lang;
    document.querySelectorAll('.lang button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.lang === lang)));
    try { localStorage.setItem('lang', lang); } catch (e) { /* storage unavailable */ }
  };
  let saved = null;
  try { saved = localStorage.getItem('lang'); } catch (e) { /* storage unavailable */ }
  if (saved === 'de') setLang('de');
  document.querySelectorAll('.lang button').forEach((b) => b.addEventListener('click', () => setLang(b.dataset.lang)));

  // top bar becomes solid after the hero
  const bar = document.querySelector('.bar');
  const onScroll = () => bar.classList.toggle('is-solid', window.scrollY > window.innerHeight * 0.6);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // hero video: no autoplay for reduced motion
  const hero = document.querySelector('.hero__video');
  if (hero && reduce) { hero.removeAttribute('autoplay'); hero.pause(); }

  // project videos: play in view, toggle button
  const setState = (btn, playing) => {
    btn.dataset.state = playing ? 'playing' : 'paused';
    btn.setAttribute('aria-label', playing ? 'Pause video' : 'Play video');
  };
  document.querySelectorAll('.media video').forEach((v) => {
    const btn = v.parentElement.querySelector('.vtoggle');
    v.dataset.user = '';
    btn.addEventListener('click', () => {
      if (v.paused) { v.play().catch(() => {}); v.dataset.user = 'play'; } else { v.pause(); v.dataset.user = 'pause'; }
    });
    v.addEventListener('play', () => setState(btn, true));
    v.addEventListener('pause', () => setState(btn, false));
  });

  if ('IntersectionObserver' in window) {
    const vio = new IntersectionObserver((entries) => {
      entries.forEach(({ target: v, isIntersecting }) => {
        if (isIntersecting && !reduce && v.dataset.user !== 'pause') v.play().catch(() => {});
        if (!isIntersecting && !v.paused) v.pause();
      });
    }, { threshold: 0.45 });
    document.querySelectorAll('.media video').forEach((v) => vio.observe(v));

    if (!reduce) {
      const rows = document.querySelectorAll('.work');
      const rio = new IntersectionObserver((entries) => {
        entries.forEach(({ target, isIntersecting }) => {
          if (isIntersecting) { target.classList.remove('is-pending'); rio.unobserve(target); }
        });
      }, { threshold: 0.2 });
      rows.forEach((r) => {
        const top = r.getBoundingClientRect().top;
        if (top > window.innerHeight) { r.classList.add('is-pending'); rio.observe(r); }
      });
    }
  }
})();
