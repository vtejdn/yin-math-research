# Paper Source and Build

The [paper](main.tex) proves almost-sure Brown-measure convergence for polynomials in independent GUE matrices and convergence results for normalized determinants and logarithmic determinants of affine pencils.
The entry point is `main.tex`, which reads the five files in `sections/`, the [bibliography subset](references.bib) and the [bibliography style](yin-amsalpha.bst).
The bibliography style reuses the repository's adapted AMS style for alphabetic labels, author initials and alphabetical sorting.
The [project record](../readme.md) identifies the underlying arguments, and the [manuscript review](review.md) and [citation map](../citation.md) record the checks on this exposition.

## Local build

Run from this `paper/` directory with pdfLaTeX and BibTeX.
Use this command with TeX Live and latexmk.

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The tested MiKTeX commands use installed packages, disable automatic package installation and keep output alongside `main.tex`.

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

On 2026-11-10 the TeX Live command above compiled the current Task v2 source after removal of the byline and author contact details.
TeX Live 2026 with pdfTeX 1.40.29, BibTeX 0.99e and latexmk 4.88 produced a twelve-page `main.pdf`.
The final logs report no unresolved citations or cross-references, missing characters or box diagnostics.
The generated bibliography contains the twelve cited works with alphabetic author–year labels, initialed given names, full family names and alphabetical author order.
Both occurrences of `Hermitian` in the BSS18 title retain their capitalization in the generated bibliography.
Checks of the extracted PDF text and metadata confirmed that the byline, running author name and contact details are absent and the PDF author field is empty.
