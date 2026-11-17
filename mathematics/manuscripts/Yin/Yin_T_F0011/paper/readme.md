# Paper Source and Build

The [manuscript](main.pdf) compares actual conjugate variables and full-domain dual systems, proves the normal equivalence and its affiliated rationality application, and gives both nonnormal separations.
The entry point is [main.tex](main.tex), which reads the six section files in `sections/` and the eleven-work [bibliography subset](references.bib).
The local `yin-amsalpha.bst` is reused from the F0012 manuscript and gives author–year alphabetic labels, initialed given names, full family names and alphabetical author order.
The [project record](../readme.md) identifies the responsible mathematical arguments and the [citation map](../citation.md) identifies the external interfaces used here.

## Local build

Run in this `paper/` directory with installed pdfLaTeX and BibTeX.

```powershell
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error main.tex
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error main.tex
```

The document uses AMS-LaTeX, Latin Modern, mathtools, geometry, microtype and hyperref.
The document-local ignore exceptions keep `main.pdf` and the reused bibliography style eligible for Git tracking; ordinary build byproducts remain ignored.
Yin's manuscript policy calls for source, reference and compilation-diagnostic checks, without page rendering unless explicitly requested.

## Build record

On 2026-11-17, MiKTeX 25.4 with pdfTeX 1.40.27 and BibTeX 0.99d compiled the initial manuscript into a 22-page PDF with automatic package installation disabled.
The final source checks found 52 unique labels, no unresolved source references, 26 citation uses and exactly eleven cited bibliography entries.
The supporting Markdown links and their local targets were checked.
The final TeX and BibTeX diagnostics contain no unresolved references or citations, missing-character reports or box diagnostics.
Text extraction confirmed an empty PDF author field and readable text without replacement characters.
No pages were rendered or visually inspected, in accordance with the writer's policy.
These are source and build checks by the writing agent, not an independent mathematical review of the manuscript.
