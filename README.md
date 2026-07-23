# Raunak Singh — Portfolio

A static, single-page professional portfolio (finance & business analytics), built as plain HTML/CSS/JS — no build step, no framework.

## View it locally

Just open `index.html` in a browser, or serve it so relative links behave normally:

```
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploy it for free (pick one)

- **GitHub Pages**: push this folder to a GitHub repo, then enable Pages on the `main` branch (root). Your CV can link to `https://<username>.github.io/<repo>`.
- **Vercel**: `vercel` (or drag-and-drop the folder into vercel.com) — no config needed, it's static.
- **Netlify**: drag-and-drop the folder into app.netlify.com/drop.

## Structure

- `index.html` — the one-page portfolio (About, Experience, Case Studies grid, Skills, Achievements, Education, Contact)
- `case-studies/*.html` — one full detail page per case study (methodology, assumptions, key findings with charts, key takeaways, downloads), linked from each card on `index.html`
- `assets/css/style.css` — design system (light corporate/consulting theme) shared by the home page and every detail page
- `assets/js/main.js` — nav behavior and scroll-reveal, shared by the home page and every detail page
- `assets/js/case-charts.js` — Chart.js configs for the detail pages, one init function per case study, all using numbers sourced from the underlying report
- `assets/docs/` — downloadable CV and case-study source reports
- `assets/img/favicon.svg` — monogram favicon
- `legacy_streamlit_app/` — the previous Streamlit version, kept for reference, no longer live

## Adding a real headshot

The hero section currently shows an "RS" monogram avatar instead of a photo (no standalone headshot image file existed in the project). To use a real photo:

1. Drop a square photo into `assets/img/`, e.g. `assets/img/headshot.jpg`.
2. In `index.html`, replace:
   ```html
   <div class="avatar-monogram">RS</div>
   ```
   with:
   ```html
   <img src="assets/img/headshot.jpg" alt="Raunak Singh" class="avatar-monogram" style="object-fit:cover;">
   ```

## Updating content

All content is real, sourced from `Raunak Singh_CV.pdf` and the case-study reports in `assets/docs/`. To edit a case study, open its file directly in `case-studies/` — each page is self-contained (Objective, Methodology, Assumptions, Key Findings, Key Takeaways, Tools, Downloads). The summary card on `index.html` (inside `#caseGrid`) is a separate, shorter blurb that links to the detail page — update both if a case study's framing changes. There's no CMS or data file layer; everything is plain HTML.
