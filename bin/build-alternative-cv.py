#!/usr/bin/env python3
"""Refresh the standalone CV alternative from the site's existing JSON resume.

Run from any directory: python3 bin/build-alternative-cv.py
Only alternative/cv/index.html is written. No third-party packages are required.
"""

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
resume = json.loads((ROOT / "assets/json/resume.json").read_text())
socials = (ROOT / "_data/socials.yml").read_text().splitlines()
pdf = next(line.split(":", 1)[1].split("#", 1)[0].strip() for line in socials if line.startswith("cv_pdf:"))


def safe(value):
    return escape(str(value), quote=True)


def dates(entry):
    start = entry["startDate"].replace("-", ".")
    end = entry.get("endDate", "present").replace("-", ".")
    return f"{safe(start)} – {safe(end)}"


def experience(entries, kind):
    output = []
    for entry in sorted(entries, key=lambda e: e["startDate"], reverse=True):
        institution = entry["institution"] if kind == "education" else entry["name"]
        role = f'{entry["studyType"]} in {entry["area"]}' if kind == "education" else entry["position"]
        location = f'<span class="cv-location">{safe(entry["location"])}</span>' if entry.get("location") else ""
        output.append(f'''<article class="cv-entry">
          <div class="cv-date">{dates(entry)}{location}</div>
          <div><h3>{safe(institution)}</h3><p class="cv-role">{safe(role)}</p><p class="cv-description">{safe(entry.get("summary", ""))}</p></div>
        </article>''')
    return "\n        ".join(output)


publications = []
for paper in sorted(resume["publications"], key=lambda p: p["releaseDate"], reverse=True):
    publications.append(f'''<article class="cv-entry cv-publication">
          <div class="cv-date">{safe(paper["releaseDate"].replace("-", "."))}</div>
          <div><h3><a href="{safe(paper["url"])}">{safe(paper["name"])}</a></h3><p class="cv-role">{safe(paper["publisher"])}</p></div>
        </article>''')
interests = "\n            ".join(
    f'<p><strong>{safe(item["name"])}</strong><br><span>{safe(" · ".join(item.get("keywords", [])))}</span></p>'
    for item in resume["interests"]
)

page = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex, nofollow">
    <meta name="description" content="Curriculum vitae of Yuan Pu. Education, research experience, and selected publications.">
    <title>CV | Yuan Pu · alternative</title>
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🧬%3C/text%3E%3C/svg%3E">
    <link rel="preload" href="../fonts/roboto-latin.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="../styles.css">
    <script src="../theme.js"></script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header">
      <nav class="shell nav-inner" aria-label="Main navigation">
        <a class="brand" href="../index.html"><strong>Yuan</strong> Pu</a>
        <div class="nav-links">
          <a href="../index.html">about</a>
          <a href="https://yuan-pu.github.io/publications/">publications</a>
          <a href="index.html" aria-current="page">cv</a>
          <button class="theme-toggle" type="button" aria-label="Change color theme">
            <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M20.7 14A8.7 8.7 0 0 1 10 3.3 9 9 0 1 0 20.7 14Z"/></svg>
            <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg>
          </button>
        </div>
      </nav>
    </header>
    <main class="shell" id="main">
      <div class="preview-note"><span>Alternative · cv</span><a href="https://yuan-pu.github.io/cv/">View current CV ↗</a></div>
      <header class="cv-heading">
        <div><h1>curriculum vitae</h1><p class="subtitle">{safe(resume["basics"]["name"])} · Computer Science, Duke University</p></div>
        <a class="download-link" href="../../{safe(pdf.lstrip('/'))}" download>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 3v12m-5-5 5 5 5-5M5 16v5h14v-5"/></svg>
          Download PDF
        </a>
      </header>
      <div class="cv-contact"><a href="mailto:{safe(resume["basics"]["email"])}">{safe(resume["basics"]["email"])}</a><a href="https://scholar.google.com/citations?user=MIBf-swAAAAJ&amp;hl=en">Google Scholar ↗</a></div>
      <nav class="cv-nav" aria-label="CV sections"><a href="#education">Education</a><a href="#experience">Research experience</a><a href="#publications">Selected publications</a></nav>
      <div class="cv-interests"><p>Research interests</p><div>
            {interests}
      </div></div>

      <section class="cv-section" id="education" aria-labelledby="education-heading">
        <h2 id="education-heading">education</h2>
        {experience(resume["education"], "education")}
      </section>
      <section class="cv-section" id="experience" aria-labelledby="experience-heading">
        <h2 id="experience-heading">research experience</h2>
        {experience(resume["work"], "work")}
      </section>
      <section class="cv-section" id="publications" aria-labelledby="publications-heading">
        <h2 id="publications-heading">selected publications</h2>
        {chr(10).join(publications)}
        <a class="cv-publications-link" href="https://yuan-pu.github.io/publications/">Full publication list &amp; authors →</a>
      </section>
    </main>
    <footer class="site-footer"><div class="shell footer-inner"><span>Yuan Pu · <a href="../index.html">Back to about</a></span><a href="https://yuan-pu.github.io/cv/">Current CV ↗</a></div></footer>
  </body>
</html>
'''
destination = ROOT / "alternative/cv/index.html"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(page)
print(f"Generated {destination.relative_to(ROOT)} from assets/json/resume.json")
