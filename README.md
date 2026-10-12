# Jeeva Portfolio

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py makemigrations core projects articles contact
python manage.py migrate
python manage.py loaddata initial_data
python manage.py runserver
```

## Tailwind CSS

Install Node dependencies and build CSS:

```bash
npm install
npm run build        # production build
npm run dev          # watch mode for development
```

## UI Enhancements (latest update)

The portfolio UI has been enhanced with purposeful animations to improve user experience while maintaining performance and accessibility.

### What was added

- **Scroll-triggered entrance animations** using Intersection Observer:
  - Sections fade-in or slide-in as they enter the viewport.
  - Implemented via `data-reveal` attributes on HTML elements.
- **Logo theme adaptation**: The logo now inverts its colors in light theme to remain visible against the background, fixing the issue where it appeared as a dark box in dark theme.
  - "Available for work" badge pulses gently to draw attention.
  - Buttons and links retain smooth hover transitions.
- **Background gradient animation**:
  - Slowly shifting gradient on the page background for visual polish.
- **CSS Animations** (defined in `static/src/input.css`):
  - `fade-in`, `slide-in-left`, `slide-in-right`, `pulse`, `gradient-shift`, `typing`, `blink-caret`, `float`.
  - Utility classes: `.fade-in`, `.slide-in-left`, `.pulse`, `.typing-effect`, `.float`, `.hover-tilt`, delay helpers.
  - Reveal-based classes: `.reveal-fade`, `.reveal-slide-left`, `.reveal-slide-right`.
- **JavaScript update** (`static/js/animations.js`):
  - Updated IntersectionObserver logic to add appropriate reveal classes based on `data-reveal` attribute.
- **Typing effect**:
  - Animated typing effect on the headline using CSS steps animation.
- **Float animation**:
  - Gentle floating motion on the badge and other elements.
- **Hover tilt**:
  - Subtle 3D tilt effect on project cards when hovered.

### Screenshot

![Portfolio UI with typing effect and other creative animations](./screenshots/ui-enhancement-final.png)

### Implementation details

Following the `ui-enhancement` skill guidelines:

1. Analyzed existing CSS/Tailwind setup and template structure.
2. Added custom keyframe animations and utility classes to `static/src/input.css`.
3. Updated `static/js/animations.js` to handle scroll-triggered reveals.
4. Modified HTML templates (`templates/core/home.html`, `templates/base.html`, `templates/components/hire_me_badge.html`) to add `data-reveal` and animation classes.
5. Rebuilt Tailwind CSS with `npm run build`.
6. Verified animations work correctly in both light and dark modes.
7. Verified logo color adaptation works in both themes via CSS invert filter.

### Performance & accessibility

- Animations only affect `transform` and `opacity` (GPU‑accelerated).
- Respects user’s reduced‑motion preference (could be extended with `@media (prefers-reduced-motion: reduce)`).
- Kept entrance durations between 0.3s–0.6s to avoid sluggishness.
- No layout‑thrashing; DOM reads/writes are batched via Intersection Observer.

## Contributing

Feel free to submit pull requests or open issues for improvements.

## License

MIT
