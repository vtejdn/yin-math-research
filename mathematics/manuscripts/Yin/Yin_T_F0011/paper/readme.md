# Paper Source and Build

The [manuscript](main.pdf), titled *On conjugate variables and dual systems*, compares actual conjugate variables and full-domain dual systems, proves the normal equivalence and the maximal-Delta consequence, and gives both nonnormal separations.
The entry point is [main.tex](main.tex), which reads four main sections, two appendices and the ten-work [bibliography subset](references.bib).
The [first appendix](sections/analytic-details.tex) contains the mixed-energy graph argument and the proof of the density-square estimate; the [second](sections/reductions.tex) contains the spectral and coefficient transfers.
The local `yin-amsalpha.bst` is reused from the F0012 manuscript and gives author–year alphabetic labels, initialed given names, full family names and alphabetical author order.
The [project record](../readme.md) identifies the responsible mathematical arguments and the [citation map](../citation.md) identifies the external interfaces used here.

## Local build

Run in this `paper/` directory with installed pdfLaTeX and BibTeX.

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The document uses AMS-LaTeX, Latin Modern, mathtools, geometry, microtype and hyperref.
The document-local ignore exceptions keep `main.pdf` and the reused bibliography style eligible for Git tracking; ordinary build byproducts remain ignored.
Yin's manuscript policy calls for source, reference and compilation-diagnostic checks, without page rendering unless explicitly requested.

## Build record

On 2026-11-17, the commands above compiled the current sources into an 18-page PDF using TeX Live 2025, pdfTeX 1.40.27 and BibTeX 0.99d.
The source checks found 45 unique labels, no unresolved source references and exactly ten cited bibliography entries.
The supporting Markdown links and their local targets were checked.
The final TeX and BibTeX diagnostics contain no unresolved references or citations, missing-character reports or box diagnostics.
pdfTeX reports one font-expansion warning, "font should be expanded before its first use".
Text extraction confirmed both appendices and found no replacement characters.
No pages were rendered or visually inspected, in accordance with the writer's policy.
These are source and build checks by the writing agent, not an independent mathematical review of the manuscript.
