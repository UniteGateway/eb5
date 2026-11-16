# GoEB5 — goeb5.in

EB-5 US investor-visa website for GoEB5, powered by Unite Group, Inc. Static HTML/CSS/JS — no framework or server needed.

## Pages (18)

Home · About Unite Group · Why USA · EB-5 Program · Texas Solar Project · Investments · Gallery · Process · Partners & Advisors · FAQ & Resources · Contact / Apply · Investor Portal · News & Insights · Social & Connect · Privacy Policy · Terms of Use · Investment Disclaimer · Sitemap

## Structure

```
*.html          built pages (upload these with assets/ and img/)
assets/site.css shared styles
assets/site.js  shared features: projects, country flags, calculator,
                eligibility check, booking slots, forms, gallery, social links
img/            logo and photos (Unsplash License)
src/home-v2.html approved home-page content the build preserves
build.py        generates every page from shared header/footer
```

## Editing

1. Change page content in `build.py` (or shared styles/scripts in `assets/`).
2. Run `python3 build.py` to regenerate the `.html` files.
3. Commit the changes.

`build.py` also writes `spa/index.html`, a single-file preview used inside Claude (ignored by git).

## Before going live

- **Forms** validate in the browser but do not send data. Connect them to an email service or CRM.
- **Social profiles:** paste profile URLs into `window.SOCIAL` in `assets/site.js`; icons then open those pages.
- **Investor portal** is a placeholder until a backend (auth, database, document room) is built.
- **Legal pages** are drafts for review by counsel.
- **Texas project:** EB-5 eligibility, TEA status and regional-center sponsorship are still under evaluation; keep the disclaimers until verified.

## Deploy

Upload all `.html` files plus the `assets/` and `img/` folders to the web root for goeb5.in (any static host: cPanel, Netlify, Vercel, GitHub Pages).
