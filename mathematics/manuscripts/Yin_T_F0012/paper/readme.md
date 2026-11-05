# Paper Source and Build

The [paper](main.tex) proves almost-sure Brown-measure convergence for polynomials in independent GUE matrices and almost-sure and mean convergence for affine determinants.
The entry point is `main.tex`, which reads the five files in `sections/`, the [bibliography subset](references.bib) and the [bibliography style](yin-amsalpha.bst).
The bibliography style reuses the repository's adapted AMS style for alphabetic labels, author initials and alphabetical sorting.
The [project record](../readme.md) identifies the underlying arguments, and the [manuscript review](review.md) and [citation map](../citation.md) record the checks on this exposition.

## Local build

Run from this `paper/` directory with pdfLaTeX and BibTeX.
The tested MiKTeX commands use installed packages and keep output alongside `main.tex`.

```powershell
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error main.tex
pdflatex --disable-installer -interaction=nonstopmode -halt-on-error main.tex
```

The document uses AMS-LaTeX, Latin Modern, mathtools, geometry, microtype and hyperref.
The [main PDF](main.pdf) is eligible for Git tracking under the author's policy.
Auxiliary outputs are ignored.

## Latest build

On 2026-11-05, the commands above built the Task v2 revision of `main.tex`, all five included sections and the local bibliography inputs using MiKTeX 25.4, pdfTeX 1.40.27 and BibTeX 0.99d.
The output has twelve pages.
The final logs report no unresolved citations or cross-references, missing characters or box diagnostics.
The generated bibliography contains the eleven cited works with alphabetic author–year labels, initialed given names, full family names and alphabetical author order.
Page rendering and visual inspection were outside the build check under [Yin's compilation policy](../../../../profiles/Yin/writing/readme.md#compilation-and-layout-checks).
