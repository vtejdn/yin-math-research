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

Run the following sequence from this document directory with pdfLaTeX and BibTeX available:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

With MiKTeX, pass `--disable-installer` to each pdfLaTeX invocation.
Repeat pdfLaTeX when the log requests another pass to settle cross-references.
The document uses `amsart`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `mathtools`, `geometry`, `microtype`, `needspace` and `hyperref`.
The bibliography style is `amsalpha`.
Build products stay in this document directory.
The document-local ignore rule permits tracking `main.pdf`; non-PDF TeX auxiliary files are ignored by Git.

## Latest Build

The sources with Proposition 4.2 and Lemma 4.9 preceding the proof of Theorem 1.7 compiled successfully on 2026-11-18 using MiKTeX 25.4, pdfTeX 1.40.27 and BibTeX 0.99d.
The build ran in the directory containing `main.tex` with the commands above and one extra pdfLaTeX pass to settle cross-references.
The resulting PDF has 21 pages.
The [organization record](../organization.md) gives the current environments and proof dependencies.

The source check found 82 unique labels and the build resolved all cross-references and 21 bibliography entries.
The final TeX and BibTeX logs contain no compilation errors, unresolved citations or references, duplicate-label warnings, missing-character diagnostics, box diagnostics or requests for another pass.
The final TeX log retains the pdfTeX font-expansion warning, "font should be expanded before its first use".
The check covered the revised source, references and compilation diagnostics.

See the [open manuscript problems](../review.md) and the [provenance of the mathematical results](../readme.md#mathematical-provenance).
