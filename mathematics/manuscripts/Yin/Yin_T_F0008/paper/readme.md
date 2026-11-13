# A Variational Formula for Affine Semicircular Determinants

Responsible manuscript author: Yin.
Omit the manuscript byline and author contact details.
The project [citation map](../citation.md) records current external citation uses and links to their source evidence.

## Current manuscript

The current manuscript is the user-approved seven-section expansion of the paper.
Its artifact is [main.tex](main.tex), with seven section files, one comparison appendix and [references.bib](references.bib).
Its generated PDF location is `main.pdf`, alongside the source; Git tracks this PDF, as permitted by the document `.gitignore`, while auxiliary products remain ignored.
The source inputs are `main.tex`, `references.bib`, [yin-amsalpha.bst](yin-amsalpha.bst) and the eight `sections/*.tex` files.
The [project record](../readme.md) owns selection and mathematical provenance, and the [conventions](../conventions.md#expanded-manuscript-selection) state the current writing choices.

| Section | Function and scope |
| --- | --- |
| 1. Introduction | Define the affine determinant problem and both coefficient maps; state the general formula and attainment theorem; recover ordinary capacity at zero mean; state the strict Hilbert--Schmidt formula, positive-pencil theorem, capacity corollary and radial Brown proposition. |
| 2. Preliminaries and the Dyson equation | Establish the matrix Cauchy transform, uniqueness, logarithmic primitive, full block covariance, regularization and strict spectral-gap interface. |
| 3. Proof of the general formula and attainment | Prove the regularized global minimum, the required signs, value identification, removal of regularization, critical-point/invertibility equivalence and unique optimizer. |
| 4. Imaginary constant terms and the strict Hilbert--Schmidt formula | Prove the formula for T-iD and the capacity limit; parameterize the strict domain; compare the two quadratic corrections and establish both directions of the determinant identity. |
| 5. Strictly positive affine pencils | Prove strict-feasibility equivalence, the minimum over matrix supersolutions and its unique least optimizer, and relate it to the general formula. |
| 6. Ordered min--max principles | Treat scalar, commuting and isotropic coefficients, then separately strict HS-positive covariance; prove the reduced Hessian and limiting argument; state the negative-HS counterexample and inverse-free square completion. |
| 7. Spectral applications | Give shifted potentials, capacity bounds and atoms, centered rho=0 radial distributions, an invertibility criterion and contour mass, optimizer-Hessian density, and normalization examples. |
| Appendix A | Prove the global HS comparison, including the support/kernel corner decomposition and uniform regularization estimate. |

The main result remains C_F0126/C_F0127 and the secondary positive-pencil theorem remains C_F0121.
The comparison and applications do not enter the proof of the main theorem.
The optional disk-mass/circle-mean remarks and the extra rational L2/divergence consequences remain outside this manuscript.
No Task is reopened and no Claim Role or fixed mathematical version is changed.

Public attribution is limited to Spe26, Bia97 and AK20; the private Spe26b and Kar26 are not quoted or reproduced in the reader-facing paper.
Source identity, source-statement inspection, local proof checking and literature priority remain separate.

## Build convention

The local bibliography style is a renamed derivative of the standard AMS `amsalpha` style, with its copyright and LPPL notice retained.
It generates alphabetic author–year labels, displays given-name initials and complete family names in every entry, sorts by author family-name list and then year, and supports article identifiers in the `eid` field.
The typesetting subset uses journal abbreviations verified against the [Mathematical Reviews serials list](https://mathscinet.ams.org/msnhtml/serials.pdf); the [canonical bibliography](../../../../literature/references.bib) retains full publication metadata.

Run from this `paper/` directory:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The generated output location is `paper/main.pdf`; do not use an output-directory option or maintain a second current PDF in `build/`.
Editor builds should use the same directory.
Page-inspection PNGs may use an ignored `build/` subdirectory.
The last recorded source-repository build used TeX Live 2026, pdfTeX 1.40.29, BibTeX and latexmk 4.88; all packages are standard and no external figures or network inputs are needed for compilation.
In that source build, the documented command produced a 36-page `main.pdf`, and the final TeX and BibTeX logs have no unresolved references or citations, missing characters or box warnings.
The launcher reports a nonfatal Windows Perl locale fallback.
That source build record covers compilation, references and logs; it is not a new mathematical review, and the page-by-page visual inspections recorded below apply to their stated earlier revisions.

## Receiving build

Receiving build completed at 2026-11-01T15:24 UTC with MiKTeX 25.4, pdfTeX 1.40.27 and BibTeX.
Run from this paper directory:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

That build produced 36 pages.
All citations and cross-references resolved; its final log had no missing-character or box warnings.
All 36 rendered pages of that revision were inspected for clipping, overlap and pagination at contact-sheet scale.
The latexmk launcher requires Perl, which was unavailable; the direct commands above completed successfully.
This receiving typesetting check creates no new mathematical proof review or Claim assessment.

A subsequent bibliography rebuild on 2026-11-01 used pdflatex and BibTeX and produced a 36-page `main.pdf`.
Its final TeX and BibTeX logs had no unresolved references or citations, missing characters or box warnings.
The bibliography on pages 35--36 was rendered and visually inspected; this narrower check does not repeat the earlier inspection of all 36 pages.

The formatting build completed at 2026-11-02T04:48 UTC with TeX Live 2025, pdfTeX 1.40.27 and BibTeX 0.99d, using the five direct commands above.
The revised source includes right-hand equation numbers, untitled definition environments and defining equalities written with `:=`.
The build produced 36 pages, and its final TeX and BibTeX logs had no warnings, unresolved references or citations, missing characters or box diagnostics.
The generated bibliography was inspected for all 29 cited entries, including labels, author initials and family names, alphabetical author ordering, chronological ordering for the same author list, journal abbreviations and the DG24 article identifier.
All build inputs remained unchanged during compilation.
No pages were rendered or visually inspected for this revision, following the author's compilation policy.
This formatting and build check supplies no new mathematical or citation-applicability review.

## Latest build

On 2026-11-10 the in-directory `latexmk` command above compiled the current source after removal of the byline and author contact details.
TeX Live 2026 with pdfTeX 1.40.29, BibTeX 0.99e and latexmk 4.88 produced a 36-page `main.pdf`.
The final logs show resolved citations and cross-references and report no missing characters or box diagnostics.
Checks of the extracted PDF text and metadata confirmed that the byline, running author name and contact details are absent and the PDF author field is empty.

## Manuscript review

The [manuscript-local review record](review.md) owns the current expanded review, definition and citation coverage, object and hypothesis correspondence, result connections, circular example checks and bounded related-literature findings.
The [project record](../readme.md#result-and-proof-provenance) selects the fixed mathematical evidence and records its actual review relationships.

## Earlier build evidence

These facts concern the identified earlier source revisions and their historical `build/main.pdf` output.
They do not change the current output convention or certify the current source contents.
All source manifests below are relative to this paper directory; the former section names identify historical inputs.

The expanded-manuscript layout checks also recorded verification of the corrected introductory description on PDF p.4 and the corrected spacing after the radial density bound on PDF p.25, equation (7.14).
These physical locations identify that inspected revision.

| Recorded revision | Build and visual evidence |
| --- | --- |
| 2026-09-12, first 14-page progress manuscript | The final local PDF had 14 pages. All 14 were visually inspected after the last wording and contents-layout changes; no clipping, overlap, missing glyph or unreadable formula was found. This dated entry did not state a build command or engine version. |
| 2026-09-12, 15-page structure rewrite | The recorded local latexmk invocation succeeded with TeX Live 2025 and pdfLaTeX/BibTeX. The retained dated entry did not state its complete command line. The final TeX log had no actual LaTeX/package warnings, unresolved references or citations, or box warnings. The launcher reported a nonfatal Windows Perl locale fallback. All 15 final pages were visually inspected after the last edits, including the contents, long equations, page boundaries and bibliography; no clipping, overlap or missing glyph was found. |
| 2026-09-13, 13-page general-main-theorem manuscript | MiKTeX 25.4, pdfTeX 1.40.27, BibTeX and latexmk 4.88 completed the historical command below. The final TeX log had no unresolved citations/references, missing characters or layout warnings. The Windows Perl locale fallback was nonfatal. The build used approved access to existing MiKTeX user configuration and required no package download. All 13 pages were rendered and visually inspected, including formulas, theorem/definition layout, page transitions and bibliography; no clipping, overlap, missing glyph or unreadable equation was found. |
| 2026-09-13, notation-corrected 13-page revision | The subsequent build succeeded with 13 pages, resolved citations/references and no layout or missing-character warnings; the same nonfatal Perl locale fallback remained. All 13 updated pages were visually inspected, including the main infimum, block covariance, rescaling, secondary minimum and optimizer relation; no clipping, overlap or missing glyph was found. |

The 14- and 15-page revisions used `main.tex`, `references.bib` and the seven historical section files `dyson.tex`, `imaginary-drift.tex`, `introduction.tex`, `minimax.tex`, `outlook.tex`, `positive-pencils.tex` and `spectral.tex` under `sections/`.
The two 13-page revisions used `main.tex`, `references.bib` and the five historical section files `introduction.tex`, `dyson.tex`, `main-proof.tex`, `positive-pencils.tex` and `spectral.tex`.
The successful command recorded for the first 13-page build was run from the paper directory:

```powershell
latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error main.tex
```

This is a historical command, not the current build instruction.
The MS24 notation source finding remains at its [responsible source note](../../../../audits/literature/MS24/readme.md#notation-recheck), and the adopted notation choice remains in the [manuscript conventions](../conventions.md#yin_t_f0008-covariance-argument).
