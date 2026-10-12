document.querySelectorAll('[data-reveal]').forEach((el) => {
  new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      const type = el.dataset.reveal || 'fade';
      el.classList.add(`reveal-${type}`);
      observer.unobserve(el);
    }
  }).observe(el);
});