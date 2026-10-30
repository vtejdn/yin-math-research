# Affiliated Rationality Paper

Author: Yin.

## Purpose and Inputs

This is the principal paper for [Yin_T_F0001](../../../tasks/Yin_T_F0001_v7.md#yin_t_f0001).
The entry file is [main.tex](main.tex).
It inputs the seven active files in `sections/` and the local BibTeX subset `references.bib`.
Complete bibliographic data remains in the [canonical bibliography](../../../literature/references.bib).
No figures or network inputs are required.
Current manuscript citation applications and their source-evidence links are in the project [citation map](../citation.md).

## Build

Run from this document directory with TeX Live, pdfLaTeX and BibTeX available:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The document uses `amsart`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `mathtools`, `geometry`, `microtype`, `needspace` and `hyperref`.
The bibliography style is `amsalpha`.
Build products stay in this document directory.
The document-local ignore rule permits tracking `main.pdf`; non-PDF TeX auxiliary files are ignored by Git.

## Latest Build

The in-directory build succeeded on 2026-10-30 with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
It used TeX Live 2025, pdfLaTeX 1.40.27 and latexmk 4.86a, producing a 23-page PDF of 478987 bytes.

Definition 1.3 now defines Psi_x for every x in L0(M), with Psi_i denoting Psi_(X_i).
Lemma 4.3 uses this definition and explicitly gives both factor right multiplication maps and their induced maps on the vector-space quotients.
Its injectivity conclusion now follows from maximal Delta for the one-element tuple and Lemma 3.2; the quotient-space proof of the L2 assertion is retained.
The manuscript conventions and organization are synchronized, and the scoped reviews record the [right multiplication maps](../review.md#psi-generalization-20261029) and the [revised injectivity argument](../review.md#scalar-injectivity-via-lemma32-20261029).

Section 6 is titled Applications to liberation gradients and conjugate variables.
Definition 6.1 and Lemma 6.2 establish the full-domain gradient-to-dual construction, followed by the criterion in Proposition 6.3.
Definition 6.4, Lemmas 6.5-6.6 and Corollary 6.7 give the ordinary conjugate-variable case; Remark 6.8 retains the arcsine example.
All pre-existing semantic labels are retained, including `prop:normal-conjugates` for the authorized change to a corollary.
The introduction, [citation map](../citation.md), [organization record](../organization.md), conventions and current review boundary use these locations and numbering.

Source checks found no duplicate labels, unresolved references or missing citation keys.
The final log contains no compilation errors, undefined citations or references, duplicate-label warnings, or overfull or underfull boxes.
The build command reported the locale fallback, and the final log retains a font-expansion warning.
All 23 pages were rendered with Poppler and visually inspected.
No clipped text, overlapping content or page-layout defect was found.

Manuscript review evidence and its limits are recorded in the project [review.md](../review.md).
