# Affiliated Rationality Paper

Author: Yin.

## Purpose and Inputs

This is the principal paper for [Yin_T_F0001](../../../../tasks/Yin_T_F0001_v7.md#yin_t_f0001).
The entry file is [main.tex](main.tex).
It inputs the six active files in `sections/` and the local BibTeX subset `references.bib`.
Complete bibliographic data remains in the [canonical bibliography](../../../../literature/references.bib).
No figures or network inputs are required.
Current manuscript citation applications and their source-evidence links are in the project [citation map](../citation.md).
Current writing opinions are in [revisions.md](revisions.md).

## Build

Run the following sequence from this document directory with TeX Live, pdfLaTeX and BibTeX available:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Repeat pdfLaTeX when the log requests another pass to settle cross-references.
The document uses `amsart`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `mathtools`, `geometry`, `microtype`, `needspace` and `hyperref`.
The bibliography style is `amsalpha`.
Build products stay in this document directory.
The document-local ignore rule permits tracking `main.pdf`; non-PDF TeX auxiliary files are ignored by Git.

## Latest Build

The sources for the numbered closure identity in Lemma 4.7 compiled successfully on 2026-11-18 with the commands above using TeX Live 2025, pdfTeX 1.40.27 and BibTeX 0.99d.
The resulting PDF has 21 pages.
This build precedes the relocation of the liberation-gradient remark.
In the current source, Remark 4.1 immediately follows the recalled definition at the start of Section 4.
The [organization record](../organization.md) gives the current environments and proof dependencies.

The source check found 82 unique labels, no unresolved references and exactly 21 cited bibliography entries.
The final TeX and BibTeX logs contain no compilation errors, unresolved citations or references, duplicate-label warnings, missing-character diagnostics, box diagnostics or requests for another pass.
The final TeX log retains the pdfTeX font-expansion warning, "font should be expanded before its first use".
The revised source and compilation diagnostics were checked; no page rendering or visual layout inspection was performed.

See the [open manuscript problems](../review.md) and the [provenance of the mathematical results](../readme.md#mathematical-provenance).
