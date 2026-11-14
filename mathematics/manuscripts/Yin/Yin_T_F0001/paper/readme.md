# Affiliated Rationality Paper

Author: Yin.

## Purpose and Inputs

This is the principal paper for [Yin_T_F0001](../../../../tasks/Yin_T_F0001_v7.md#yin_t_f0001).
The entry file is [main.tex](main.tex).
It inputs the seven active files in `sections/` and the local BibTeX subset `references.bib`.
Complete bibliographic data remains in the [canonical bibliography](../../../../literature/references.bib).
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

The in-directory build succeeded on 2026-11-14 with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
It used TeX Live 2026, pdfLaTeX 1.40.29, BibTeX 0.99e and latexmk 4.88, producing a 24-page PDF of 483005 bytes.

Definition 1.3 now defines Psi_x for every x in L0(M), with Psi_i denoting Psi_(X_i).
Lemma 4.3 states injectivity and the compact preimage equality $\Psi_x^{-1}(H\otimes_{\mathbb C}H)=H\otimes_{\mathbb C}H$.
Its proof explicitly records preservation of the algebraic L2 tensor product, introduces k for the reverse inclusion and gives both factor right multiplication maps and their induced maps on the vector-space quotients.
Its injectivity conclusion now follows from maximal Delta for the one-element tuple and Lemma 3.2; the quotient-space proof of the L2 assertion is retained.
The manuscript conventions and organization are synchronized, and the scoped reviews record the [right multiplication maps](../review.md#psi-generalization-20261029), the [revised injectivity argument](../review.md#scalar-injectivity-via-lemma32-20261029) and the [compact formulation and range obstruction](../review.md#tensor-recovery-range).

Section 5 is titled Applications to liberation gradients and conjugate variables.
Definition 5.1 and Lemma 5.2 establish the full-domain gradient-to-dual construction, followed by the criterion in Proposition 5.3.
Definition 5.4, Lemmas 5.5-5.6 and Corollary 5.7 give the ordinary conjugate-variable case; Remark 5.8 retains the arcsine example.
All pre-existing semantic labels are retained, including `prop:normal-conjugates` for the authorized change to a corollary.
The introduction, [citation map](../citation.md), [organization record](../organization.md), conventions and current review boundary use these locations and numbering.

Section 6 is titled Dual system criterion.
Lemma 6.6 proves that normal generators admitting a dual system admit conjugate variables, with the actual adjoint vector $\xi_i=-D_i^*\Omega+(D_i\Omega)^*$.
The proof of Theorem 1.9 now uses the certificate criterion in Corollary 5.7, Lemma 6.3 to identify the finite-rank coordinates and the retained summed identity of Lemma 6.7 for the converse.
All existing mathematical environments and semantic labels remain present.
The [current dual-system proof check](../review.md#analytic-proof-via-liberation-20261018) records the adapted spectral-pinching argument, domain and sign checks, and the dependencies after exchanging Sections 5 and 6.

The final log contains no compilation errors, undefined citations or references, duplicate-label warnings, or overfull or underfull boxes.
The build command reported the locale fallback, and the final log retains a font-expansion warning.
The revised source and compilation diagnostics were checked; no page rendering or visual layout inspection was performed for this build.

Manuscript review evidence and its limits are recorded in the project [review.md](../review.md).
