const themeToggles = document.querySelectorAll('[data-theme-toggle], #theme-toggle');
const updateThemeToggles = () => {
  const isDark = document.documentElement.classList.contains('dark');
  themeToggles.forEach((toggle) => {
    toggle.setAttribute('aria-pressed', String(isDark));
    toggle.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
  });
};

updateThemeToggles();
themeToggles.forEach((toggle) => {
  toggle.addEventListener('animationend', (event) => {
    if (event.animationName === 'bulb-pendulum-sway' && event.target.matches('.bulb-hanging')) {
      toggle.classList.remove('is-switching');
    }
  });
  toggle.addEventListener('click', () => {
    const root = document.documentElement;
    root.classList.toggle('dark');
    localStorage.theme = root.classList.contains('dark') ? 'dark' : 'light';
    updateThemeToggles();

    toggle.classList.remove('is-switching');
    void toggle.offsetWidth;
    toggle.classList.add('is-switching');
  });
});
