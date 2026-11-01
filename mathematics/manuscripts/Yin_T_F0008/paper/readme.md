# A Variational Formula for Affine Semicircular Determinants

Responsible manuscript author: Yin.
The publication author is Sheng Yin, Institute for Advanced Study in Mathematics, Harbin Institute of Technology; email: sheng.yin@hit.edu.cn.
The project [citation map](../citation.md) records current external citation uses and links to their source evidence.

## Current manuscript

The current manuscript is the user-approved seven-section expansion of the paper.
Its artifact is [main.tex](main.tex), with seven section files, one comparison appendix and [references.bib](references.bib).
Its generated PDF location is `main.pdf`, alongside the source; the PDF and auxiliary products remain Git-ignored.
The source inputs are `main.tex`, `references.bib` and the eight `sections/*.tex` files.
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

<a id="receiving-build"></a>
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

The final PDF has 36 pages.
All citations and cross-references resolve; the final log has no missing-character or box warnings.
All 36 rendered pages were inspected for clipping, overlap and pagination at contact-sheet scale.
The latexmk launcher requires Perl, which was unavailable; the direct commands above completed successfully.
This receiving typesetting check creates no new mathematical proof review or Claim assessment.

## Review records

The [manuscript-local review record](review.md) owns the current expanded review: the complete integration self-review, three noncontributor agent checks, the complete definition and citation review, the bounded related-literature identification checks, the final source and output manifest, and the bounded independent findings for the related-literature comparisons.

The dated records below retain specific checks of the current manuscript and of earlier manuscript revisions.
Each identifies the manuscript state it examined, with its actual participation relationship, findings and stated limits.
They are manuscript-local exposition and citation checks, not whole-source proof audits or independent reviews of the fixed Claim arguments.
The earlier 14-, 15- and 13-page revisions are collected under [retained historical inspection scopes](#retained-historical-inspection-scopes).

## Current-revision review records

<a id="contextual-literature-integration-review"></a>
### Contextual literature integration

Implemented Yin's authorization to incorporate the entire substantive [manuscript-order comparison map](../related-literature/readme.md#current-integration-of-the-substantive-comparison-map), following the [placement choice](../conventions.md#contextual-literature-placement).
The seven-section structure, abstract and Appendix A are unchanged.
Short connections appear at the relevant definitions or proof steps; nine new remarks provide the longer comparisons nearby.
The original 29-item analysis remains bound to its earlier 33-page revision, while its new navigation uses the current semantic labels.

The additions explain operator scaling and capacity; half-plane Dyson solutions, resolvent integration and positive-map stability; positive-cone geodesics, common congruences, geometric means and the zero-covariance skew-information identity; the positive-pencil spectral-edge SDP; scalar free-convolution domains, the exact Belinschi inner equation and reduced-Hessian elimination; and the Brown-measure connections to kernel projections, scalar R-diagonality, diagonal variance profiles, invariant spectral subspaces, circular addition and Dyson stability.
Existing Biane, Mai--Speicher and Dykema--Griffin attributions remain in place.
No citation was forced into a step for which the assessment found no useful matching result.
This is a scoped citation and exposition self-review; the local identifications were also checked by noncontributor agents, as recorded in [the review record](review.md#citation-and-mathematical-comparison-checks).

<a id="direct-result-connections-review"></a>
### Direct relationships between results

At Yin's request, the coordinating writer checked the introductions, proof openings and remarks throughout the manuscript under [Make direct relationships between results explicit](../../../../framework/rules/writing.md#direct-result-connections).
Proposition 7.2 now begins by applying Theorem 1.3 to the scalar shift of the centered pencil, before using real-linearity, and identifies the positivity estimate behind ray monotonicity.
Further references clarify the capacity and radial consequences of the main theorem, the zero-imaginary-part limit, the comparison of quadratic corrections, the commuting and centered min--max specializations, the attained-minimum step in Proposition 7.5, and the use of that proposition in Corollary 7.6.
Existing explicit dependency statements were retained without duplicate explanations.
This is a scoped exposition and dependency-reference self-review, not a new independent proof audit; earlier fixed mathematical and review records retain their scope.

<a id="direct-exposition-review-2026-10-10"></a>
### Direct statements and restrained modifiers: review, 2026-10-10

At Yin's request, [State results directly and use modifiers sparingly](../../../../framework/rules/writing.md#direct-results-and-modifiers) was added to the framework's general mathematical writing rules.
The coordinating agent reread the abstract, seven sections and appendix for redundant modifiers, premature derivation terminology and placement of technical details.
The introduction now states the determinant as an infimum over positive definite matrices without "finite-dimensional", "outer variable" or "of the coefficient size".
Other revisions replace commentary about formulas with their mathematical content, remove repeated descriptions of trial domains and proof organization, and leave the Hessian calculation details in the Brown section.
Necessary hypotheses, boundary distinctions, actual nested-extremum terminology and proof steps are retained; the abstract was reviewed and retained.
This is an exposition self-review, not a new independent proof audit; earlier review records below retain their own revisions.

<a id="precise-object-review-2026-10-10"></a>
### Precise object names: manuscript review, 2026-10-10

At Yin's request, the single principle [Prefer precise object names](../../../../framework/rules/writing.md#precise-object-names) was added to the general mathematical writing rules and applied throughout the current manuscript.
The coordinating agent read all nine TeX files: the abstract and main file, all seven sections, and the comparison appendix.
This was a complete object-name and hypothesis-correspondence self-review, not a new independent proof audit.
Earlier reviews retain their actual inputs and scope.

The revisions identify coefficient matrices and their index ranges explicitly, replace informal noise/physical/energy terminology by the corresponding coefficients, matrix Cauchy transform or quadratic correction, and distinguish extrema from extremizers.
The introduction now states the imaginary constant term as T-iD and correctly says that the trial-domain bijection does not identify the full objectives pointwise.
The appendix names its ambient Hilbert space and corner algebras and identifies the support projections as those of H.
The AK20 comparison explicitly retains C>c>0 from the previously inspected flatness assumption.
No displayed formula, semantic label, bibliography entry or fixed mathematical record was changed; no new proof input was introduced.

<a id="precise-object-followup-review"></a>
### Follow-up review of precise object names, 2026-10-10

At Yin's request, the coordinating writer reread the abstract, all seven sections and Appendix A under [Prefer precise object names](../../../../framework/rules/writing.md#precise-object-names).
This follow-up corrected terminology omissions in the [earlier review](#precise-object-review-2026-10-10): the text still used "Brown atom", "Brown support", "Brown mass" and similar abbreviations without identifying their objects consistently.
The manuscript now names atoms of mu_T, supp(mu_T), the mass mu_T({z}) and the logarithmic potential.
Section 7.5 explicitly identifies beta_epsilon as the normalized Laplacian of u_epsilon, and the abstract specifies that the Hessian gives a regularized density.
The scalar semicircular example now assigns capacity to eta=id rather than to the semicircular element.

The same review replaced vague references to inner solutions, logarithmic objectives, outer minimizers and positive defects with the relevant maps, functions, variables or inequalities.
The isotropy condition is attributed to the covariance map; Section 6 distinguishes its Hilbert--Schmidt positivity explicitly.
The radial regularization paragraph now names F_epsilon and f_epsilon directly, the spectral-measure example uses the already defined q(X^{-1}(x)), and the repeated tensor-product convention was removed from Lemma 7.7 because Definition 1.2 already supplies it.
The current manuscript plan and provenance descriptions use the same object names.
Standard terms with an existing definition or source, including Brown measure, matrix Cauchy transform, capacity, hermitization and operator-valued circular element, were retained.

This is a whole-manuscript terminology and exposition self-review, with checks of the affected definitions, hypotheses and formula references.
It is not a new independent proof audit or a new whole-source citation audit.
All displayed mathematical expressions and all semantic labels are preserved; one equation's trailing punctuation changed.
Bibliographic entries and the exact citation commands, including their locators, are unchanged.
Earlier fixed research and manuscript-review records retain their original scope.

<a id="circular-example-fixed-registration"></a>
### Fixed registration and independent review of the circular example

At Yin's request, the complete argument underlying Example 7.3 and its following cumulant explanation was independently reviewed before registration as [C_F0173](../../../claims/Yin_C_F0173_v1.md#circular-example-statement).
The [reviewer-authored finding](../../../audits/reviews/Yin_R_F0130_v1.md#circular-example-independent-review) covers the full local proof, arbitrary complex and degenerate matrix coefficients, standard circular normalization, all orders of matrix-valued cumulants, rotation invariance, direct DG24/MS17 source checks, and the exact hypothesis interface to Proposition 1.8.
It found no unresolved gap or missing hypothesis.
Its scope excludes a renewed review of the Brown/spectral proof or the whole manuscript.

The mathematical body and independent finding were preserved verbatim on promotion, and the manuscript's provenance table now selects this fixed argument for the example.
This registration updates supporting records only; the TeX sources and PDF remain the revision identified by the review account.
Earlier reviews retain their own scopes and versions.

<a id="circular-example-review"></a>
### Current revision: matrix coefficients and circular elements

Implemented the [circular example choice](../conventions.md#circular-coefficient-example).
Introduction 1.4 briefly mentions matrix-coefficient linear combinations of free circular elements.
Example 7.3 in Section 7.3 now writes c_k=(s_(2k-1)+i s_(2k))/sqrt(2), the paired semicircular coefficients, their cancellation in rho, and the resulting map eta.
The following paragraph identifies the two surviving matrix-valued second cumulants, cites [DG24, Theorem 2.9 and Definition 2.10](../../../literature/pdf/DG24.pdf), and explains rotation invariance.
The transition explicitly applies the main theorem to T-z1_m for the radial potential and density formulas.
The former Proposition 7.3 is now Proposition 7.4; semantic labels resolve the changed body numbering, while Proposition 1.8 retains its number and statement.

The coordinating agent checked the coefficient calculation, circular normalization, conditional-expectation identities, rotation argument and their agreement with the [inspected DG24 definitions](../../../audits/literature/DG24/readme.md).
DG24 was registered from its public arXiv v2 and added to the manuscript bibliography; the eight existing entries were preserved.
The existing AK20 flatness comparison remains in place.
This is a scoped mathematical-exposition and citation check of the additions; the main results and existing proof bodies were not changed, and no earlier independent review is extended to the new revision.

<a id="intro-results-review"></a>
### Current revision: results in Introduction 1.3--1.4

Implemented the [introductory result organization](../conventions.md#intro-result-organization).
Proposition 1.4 states the strict Hilbert--Schmidt formula; Definition 1.5 and Theorem 1.6 give the positive-pencil trial sets and minimum in terms of J; Corollary 1.7 states the capacity bound and atomlessness; Proposition 1.8 states the radial distribution, absolute continuity and spectral disk.
Section 7.3 retains the additional radial density and regularized-minimizer formulas as Proposition 7.3.
Complete proofs remain in the body without duplicate introductory statements.
Remarks 4.3, 4.7 and 6.3 place the domain and correction comparisons beside their formulas and examples.

The coordinating agent reviewed the revised Introduction 1.3--1.4, the affected definitions, statements and proof references in Sections 4--7, and their source attribution.
The selfadjointness assumptions are confined to Introduction 1.3; the Brown corollary retains arbitrary complex coefficients, and the radial proposition retains a_0=0 and rho=0.
The positive-pencil formula uses the identity log det P(b)=J(b), with the same factor 1/m and the same feasible sets and optimizer.
Text comparison confirms that Introduction 1.1, 1.2 and 1.5 and the proof bodies in Sections 4--6 are unchanged; the radial proof changes only the reference for positive-capacity atomlessness.
The former combined capacity/atom proposition and proof were split with their local notation made explicit.
This is a scoped exposition and statement-correspondence self-review, not a new independent proof audit or whole-manuscript definition/citation review; earlier evidence remains bound to its recorded revisions.

### Current review: necessary hypotheses and special cases

Reviewed the abstract, seven sections and appendix under Yin’s then-applicable special-case writing choice.
That source-profile reference records the historical review scope; no source profile was transferred.
Removed eleven redundant scope statements in the introduction, imaginary-constant-term, ordered min--max and spectral sections, including "Singular outputs are allowed", the remaining n=0 allowance and repeated zero-capacity/noncommutation qualifications.
Retained necessary positivity and selfadjointness assumptions, extended-real conventions, proof branches for zero or singular quantities, and examples explaining limits of the conclusions.
No displayed formula, hypothesis or proof step was changed.
This is an exposition self-review, not a fresh independent proof audit; earlier reviews retain their original scope.

### Local clarification of the DG24 citation

In Section 7.3, separated the two logical uses of DG24: Theorem 2.9(b) identifies the cumulant pattern as matrix-valued R-diagonality, and Definition 2.10, together with the vanishing of higher cumulants, identifies circularity.
The subsequent rotation argument and transition to the main variational theorem remain in place.
This clarifies the already reviewed argument in C_F0173 without changing its statement, proof or fixed review.
The local wording and citation were checked against that argument; earlier records retain their original revisions.

## Retained historical inspection scopes

The following dated records retain their inspected revisions, participation relationships, actual mathematical findings and limitations.
Historical source manifests identify the original inspected artifacts; they do not certify a later edited carrier or its current contents.

<a id="historical-first-review-2026-09-12"></a>
<a id="historical-first-review-2026-09-12--yin_t_f0008-manuscript-mathematical-and-writing-self-review"></a>
### Yin_T_F0008 Manuscript: Mathematical and Writing Self-Review

Revision note, 2026-09-12: this record describes the first 14-page manuscript and retains its original coverage.
The subsequent user-approved reorganization is covered by the [15-page structure-rewrite self-review](#historical-structure-review-2026-09-12).
References below to the final manuscript concern this record's own revision.

Date and reviewer: 2026-09-12, the coordinating agent, the manuscript's writing agent.
Review status: **self-reviewed**.
Scope: the final complete manuscript, all seven sections, abstract, bibliography and nine TeX/Bib source files.
The earlier independent ledger reviews retain their own artifact and scope boundaries; they are not independent reviews of this manuscript.
The final local PDF has 14 pages.
Inspected source paths appear below.

<a id="historical-first-review-2026-09-12--authorization-scope-and-disposition"></a>
#### Authorization, Scope and Disposition

The user requested adding MS24 to the community writing references and preparing a Yin_T_F0008 progress manuscript with stronger motivation and clear explanations.
The paper presents existing Yin_C_F0119-Yin_C_F0123 arguments and the already checked signed Schur reduction.
No new theorem Role, main-theorem designation, reusable lemma extraction, research-run restart or new mathematical scope was implemented.

Disposition: no unresolved discrepancy found between the final manuscript and the registered results at their stated scopes.
Complete definition clarity and citation compliance were checked separately, as recorded below.
Broader literature attribution/priority comparison remains unperformed under the offline restriction.
No novelty claim is inferred from the local proofs.

<a id="historical-first-review-2026-09-12--mathematical-comparison"></a>
#### Mathematical Comparison

| Final manuscript | Checks and conclusion |
| --- | --- |
| Introduction and Section 2; Yin_C_F0119 | Normalized absolute finite determinant and ordinary Fuglede-Kadison determinant agree. Checked variance one, dimension doubling, bilinear covariance symmetry, negative-imaginary-part convention and weighted uniqueness. Differentiating the primitive gives the normalized Cauchy transform and its asymptotic fixes the constant. The bounded correction in the monotone formula covers both positive and zero determinant; the scalar infimum follows from the positive derivative, without being misrepresented as free matrix optimization. The full covariance blocks preserve the extra information exposed by the scalar phase example. |
| Section 3; Yin_C_F0120 | Selfadjoint noise and strictly positive D are retained. The exponential-path calculation, compact sublevel sets, unique critical point, deterministic congruence and determinant normalization reproduce the recorded proof. The zero-drift infimum uses fixed trials and allows minus infinity. Homogeneous rescaling gives exactly ordinary capacity for the stated selfadjoint coefficient representation. The finite positive trial matrix has log determinant J_D minus m. |
| Section 4; Yin_C_F0121 final formulation | All coefficients are selfadjoint and S has a strict positive gap. Checked the Schur-complement domain, square completion, strict-feasibility equivalence, increasing iteration, last-letter Fock subtree recursion and strong inverse convergence. The least-feasible-matrix comparison and operator concavity give global minimality; local strictness follows from the differentiated gap equation and finite-map contraction. The paper spells out the elementary norm estimate used there. No stability constraint is imposed on trial matrices. The strict-domain infimum is unattained. Indefinite and general zero-edge cases remain excluded. |
| Section 5; Yin_C_F0122 | Checked scalar inner maximization, boundary cases, unique outer optimizer, and the explicit failure of the raw saddle inequality. The commuting case requires no joint independence of diagonal entries. In the isotropic case, the full coefficient condition, finite atomic drift law, pole separation, monotone X-coordinate, unique resolvent boundary limit and objective value match the proof. The uniform Cauchy bound justifies the entire continuous spectral density, including exclusion of atoms/singular parts. |
| Section 6; Yin_C_F0123 | Checked the shift and resolvent signs, derivative block, differentiated Dyson equation, invertibility at fixed positive regularization, trace-positive density, and 1/pi versus 1/(2 pi) constants. Weak convergence is an accepted MS17 input, not a newly supplied proof. General Brown-support/spectrum equality and uniform boundary stability are not claimed. The selfadjoint inversion formulas and scalar elliptic examples retain their separate stronger source/argument justifications. |
| Section 7; signed Schur reduction | Multiplication of the three factors gives the displayed pencil. Trace-zero square-zero triangular increments have determinant one, and the normalized block determinant equals the regularized determinant of S. The pencil is indefinite, so the positive-pencil minimum is explicitly inapplicable. Its general variational use is a proposed continuation, not an established result. |

Normalization checks include zero noise in the imaginary-drift objective, the centered scalar value exp(-1/2) at variance one, the circular limit r=0, and exclusion of the line degeneration r=v from formulas dividing by v-r.
The manuscript does not promote these consistency checks to an independent proof.

<a id="historical-first-review-2026-09-12--whole-manuscript-definition-and-citation-coverage"></a>
#### Whole-Manuscript Definition and Citation Coverage

This check covered the final text and all displayed/informal constructions, rather than a vocabulary search or changed lines alone.
The standing von Neumann algebra background exemption was applied; it did not remove the finite/faithful/normal/tracial hypotheses.
No Yin_T_F0001-specific terminology exemption was imported.

| Coverage | Definition clarity | Source compliance and scope |
| --- | --- | --- |
| Abstract and Section 1 | The research question precedes technical notation. Centered covariance and capacity domain are explicit; affine semicircular pencil is locally defined; isotropy is stated by its exact map. The example explains why constants need more coefficient data. | MS24 Definition 1.1 and Theorem 1.2 identify the existing result. Gur04 supplies the capacity antecedent. The abstract and introduction make no general-global-optimization or priority claim. |
| Section 2.1 | Ordinary/normalized traces, matrix expectation, finite determinant, modulus, spectral log integral and zero convention are explicit. Semicircular density and adjacent-algebra freeness convention are recalled. | MS24 Definition 2.1 and Proposition 2.3; FK52 foundation; MS17 Section 1.11 and Chapter 9 (9.5), Definition 10, Theorem 11 and Proposition 13. The ordinary zero-sensitive determinant is used throughout. |
| Sections 2.2-2.3 | Analytic primitive, logarithm normalization, hermitization, resolvent solution, regulator and local coefficient functional are defined. Extra covariance maps are displayed rather than named without explanation. | The primitive and uniqueness are proved locally from the specified MS17 inputs. Hermitization cites MS24 Section 3 and MS17 Chapter 11 Section 9. The local functional is not attributed as a standard generalized capacity. |
| Section 3 | Positive trial domain, objective, critical equation and exponential paths are given. Sublevel compactness and the relevant convexity are explained. The zero-drift and positive determinant-matrix constructions are explicit. | Existing determinant multiplicativity and the paper's primitive are the actual inputs. The proof does not import an uncited global convexity theorem or claim ordinary convexity. |
| Section 4 | Residual, affine matrix inequality, Schur complement calculation, strict positivity, full Fock space, creation operators and their acting spaces, inverse expectation, iteration and Hilbert-Schmidt pairing are supplied. Complete positivity is defined and the needed norm estimate is explained. | The Fock citation was corrected during drafting to Miy22 Section 2.1, pp. 3-5, following the already accepted Miy22-U001 input also linked in the MS24 analytic dependency chain. MS24 Section 2.2 supplies the complete-positivity convention. No source proof depth was silently expanded. |
| Section 5 | Positive part, ordered extrema, raw saddle inequalities, scalar variances, isotropic covariance, drift eigenvalue law, inner optimizer and coordinate X are defined. The Poisson kernel is displayed and its inversion role explained. | Local scalar/isotropic derivations reproduce Yin_C_F0122 from the already cited Dyson inputs. No external minimax or subordination theorem, or new attribution of the semicircular convolution model, is invoked. |
| Section 6 | Potential, distributional Laplacian, complex derivative convention, Brown measure, regularized density, block derivative operator and planar area measure are specified. Spectral measures and the general operator spectrum are distinguished. Elliptic parameters and degenerate regimes are explicit. | MS17 Chapter 11 Theorem 5/Definition 6, (11.8), Section 9 (11.14)-(11.15), p. 270 normal specialization and Theorem 9 elliptic example. The semicircular linear-combination input cites Chapter 2 Section 2. These uses agree with the [selected spectral audit](../../../audits/literature/MS17/Yin_U001.md). |
| Section 7 and bibliography | Signed block pencil and its factorization are fully displayed. The remaining variational question is stated as unresolved. Bibliographic names, titles, versions and keys match the sole registry. | Determinant rules cite MS24; the bounded determinant foundation is FK52. Five sources are mathematically used. MSY23 is a style model only and was not added merely for stylistic use. |

No remaining definition/citation omission was identified within this complete inspection.
The cited source inputs retain the acceptance and upstream proof-depth boundaries in their existing audits; this is not a fresh full audit of those sources.

<a id="historical-first-review-2026-09-12--exposition-and-visual-review"></a>
#### Exposition and Visual Review

MSY23/MSY23 remains the primary style model.
The [MS24 source observations](../../../audits/literature/MS24/readme.md#presentation-observations) retain the inspected terminology and presentation.
All explanatory prose is independently written; no substantial source passage was copied.

The introduction now relates a finite normalized determinant to the geometric mean of singular values, explains why spectral shifts introduce a constant term, gives the phase obstruction, and describes the three variational mechanisms.
The proofs use short purpose statements and explanation after calculations.
Final reading clarified adjacent-algebra freeness, replaced ambiguous wording about a "positive real inverse", and described the imaginary optimizer without suggesting the real objective has an imaginary part.
All 14 final pages were visually inspected after the last wording and contents-layout changes; no clipping, overlap, missing glyph or unreadable formula was found.

<a id="historical-first-review-2026-09-12--exact-reviewed-files"></a>
#### Exact Reviewed Files

Paths below are relative to the paper directory.
The nine TeX/Bib files identify the complete inspected source set; the local PDF was visually inspected.
README or audit navigation edits are outside this source scope.

- `main.tex`
- `references.bib`
- `build/main.pdf`
- `sections/dyson.tex`
- `sections/imaginary-drift.tex`
- `sections/introduction.tex`
- `sections/minimax.tex`
- `sections/outlook.tex`
- `sections/positive-pencils.tex`
- `sections/spectral.tex`

<a id="historical-structure-review-2026-09-12"></a>
<a id="historical-structure-review-2026-09-12--yin_t_f0008-structure-rewrite-manuscript-self-review"></a>
### Yin_T_F0008 Structure Rewrite: Manuscript Self-Review

The original review and manifest below remain evidence for the structure-rewrite revision.

Date and reviewer: 2026-09-12, the coordinating agent, the manuscript's writing agent.
Review state: **self-reviewed**.
Artifact: the complete current [Yin_T_F0008 paper](readme.md), all seven sections, abstract, bibliography and nine TeX/Bib source files.
The final local output has 15 pages; its complete inspected source list appears below.

The [first-version review](#historical-first-review-2026-09-12) retains its original 14-page revision.
This record covers the later presentation; neither record is an independent review by another agent.
Earlier research reviews retain their own scopes and artifact versions, as linked in the [project provenance table](../readme.md#result-and-proof-provenance).

<a id="historical-structure-review-2026-09-12--authorization-and-changes"></a>
#### Authorization and Changes

The user approved rewriting the manuscript according to the discussed organization: Yin_C_F0121 as the first highlighted result, Yin_C_F0120 as the link to ordinary capacity, Yin_C_F0122 as the second highlight, and Yin_C_F0119/Yin_C_F0123 as the common analytic foundation and general spectral applications.
The rewrite implements that presentation without expanding Yin_C_F0119-Yin_C_F0123, assigning a theorem Role, declaring a new main theorem, or restarting the stopped autonomous research run.

The abstract and introduction now lead with the strictly positive affine minimum.
The introduction displays its precise coefficient hypotheses, finite strict-positivity criterion, determinant objective, feasible domain and unique optimizer.
It explains the order-comparison mechanism and why setting the real drift to zero cannot supply the centered specialization.
The following imaginary-drift result supplies the actual limiting connection to MS24.
Isotropic ordered minimax then explains how an imaginary trial variable can remain useful at real spectral parameters.

Section 2 retains the common selfadjoint Dyson identities and their proofs.
The former general hermitization subsection, including the full determinant proof and covariance calculation, now belongs to Section 6 with the scalar phase obstruction and spectral applications.
The positive and imaginary sections exchange places; their proofs remain complete.
Section openings, transitions, roadmap and further questions follow the same order.
Semantic result labels remain stable; the introduction adds labels for its displayed highlights.

<a id="historical-structure-review-2026-09-12--full-mathematical-presentation-check"></a>
#### Full Mathematical Presentation Check

The complete final source was read, including unchanged proof paragraphs and source-dependent examples.
The following table records the checks on this revision, using the registered result scopes and earlier research reviews as the comparison baseline.
Compilation is separate evidence and is not a proof check.

| Coverage | Verification and scope |
| --- | --- |
| Abstract and Section 1 | Each highlighted statement agrees with its body proposition. The positive result requires all coefficients to be selfadjoint and a strict positive gap; its finite criterion uses strict feasibility, whereas its attained minimum uses nonstrict feasibility. The matrix P has log determinant J, with ordinary trace and the correct dimension normalization. The imaginary objective includes the subtraction of m outside the minimum. The isotropic display retains positive variance, arbitrary selfadjoint drift and the specified order of optimization. |
| Section 2; Yin_C_F0119 common foundation | Checked the negative-imaginary-part resolvent convention, moment recursion, weighted uniqueness, bilinear trace symmetry, derivative of the logarithmic primitive and its asymptotic constant. All three variational proofs can use these selfadjoint identities without depending on the relocated hermitization argument. |
| Section 3; Yin_C_F0121 | Checked the Schur complement and convex feasible sets, Fock square completion, spectral-gap continuation, increasing inverse iteration, last-letter subtree recursion and inverse convergence. The inverse expectation is the least feasible matrix. Operator concavity gives nonnegative objective derivative along the comparison segment. The differentiated gap equation gives strict local Hessian positivity and hence uniqueness. Strict-domain approximation and nonattainment are retained. Indefinite pencils and a general zero-gap boundary are excluded. |
| Section 4; Yin_C_F0120 | Checked strict convexity along exponential paths, compact sublevel sets, unique critical equation, deterministic congruence for noncentral D, and all determinant constants. The zero-drift infimum uses fixed trials and permits minus infinity. Homogeneous rescaling gives the stated capacity quotient at the selfadjoint coefficient hypothesis. Ordinary affine convexity is explicitly not asserted. |
| Section 5; Yin_C_F0122 | Checked scalar inner maximization, outer minimizer, endpoint values and the raw-saddle counterexample. In the isotropic proof, pole separation, the increasing X-coordinate and the unique boundary limit justify the objective value; uniform Cauchy-transform bounds justify the complete continuous density. The determinant version includes the full logarithmic term with its factor one half. No general covariance or matrix minimax theorem is inferred. |
| Section 6.1-6.2; Yin_C_F0119 general formula | The phase example still distinguishes two pencils with the same original covariance and constant term. Hermitization retains dimension 2m, all covariance blocks and the unique regularized Dyson solution. Checked the normalized primitive, exponential determinant, exact bounded correction, positive derivative and zero-determinant limit. The scalar infimum follows along a prescribed solution and is not described as free matrix optimization. |
| Section 6.3-6.5; Yin_C_F0123 | Checked the shift sign, derivative block, linearized Dyson system, fixed-positive-regularizer invertibility and the positive trace formula for density, including the Laplacian constants. Brown-measure construction and weak convergence remain accepted MS17 inputs. No uniform boundary stability or general equality of Brown support and operator spectrum is asserted. The selfadjoint inversion and scalar elliptic examples retain their distinct hypotheses and cited source scopes. |
| Section 7 | The existing signed Schur factorization and normalized determinant agree. Its selfadjoint block pencil is indefinite, so the highlighted positive-pencil proposition does not apply. A variational continuation and general boundary stability remain questions. |

No unresolved internal mathematical discrepancy was identified in this final-text check.
This disposition concerns the stated scopes and this source revision.
The rewrite adds no broader literature priority assessment or new upstream source audit.

<a id="historical-structure-review-2026-09-12--definition-clarity-and-citation-compliance"></a>
#### Definition Clarity and Citation Compliance

Both checks cover the whole final text, not only changed lines.
The standing von Neumann algebra background exemption is applied with the actual finite, faithful, normal and tracial hypotheses retained.
No Yin_T_F0001-specific primary-source choice or terminology exemption is imported.

| Text | Definition clarity | Citation compliance |
| --- | --- | --- |
| Introduction and Section 2 | Affine pencil, normalized traces, finite determinant, spectral log integral, zero convention, semicircular normalization, freeness, matrix Cauchy transform and resolvent solution are specified. | MS24 Definition 1.1, Theorem 1.2, Definition 2.1 and Proposition 2.3; Gur04 antecedent; FK52 foundation; MS17 Section 1.11 and Chapter 9 inputs remain attached to the relevant uses. |
| Sections 3-4 | Residual, linear matrix inequality, Schur complement, positive gap, Fock space and creation-operator spaces, matrix iteration, complete positivity, Hilbert-Schmidt pairing, objectives and exponential paths are explicitly supplied or briefly explained. | Miy22 Section 2.1, pp. 3-5 supplies the Fock realization; MS24 Section 2.2 supplies complete positivity. The determinant rules and local primitive are the analytic inputs. No uncited general convexity theorem is imported. |
| Section 5 | Ordered extrema, positive part, saddle inequalities, isotropic covariance, eigenvalue law, auxiliary coordinate and Poisson kernel are stated explicitly. | These are local calculations from the cited Dyson inputs; no separate minimax or subordination theorem is claimed as an external input. |
| Section 6 | Hermitization, full covariance maps, regularizer, local coefficient functional, logarithmic potential, complex derivatives, distributional Laplacian, Brown measure and elliptic parameters are explicit. | The hermitization citations moved with the construction. MS17 Chapter 11 Brown-measure, regularization, normal-specialization and elliptic-example references remain in place, within the [existing selected-passage audit](../../../audits/literature/MS17/Yin_U001.md). |
| Section 7 and bibliography | The signed pencil and factorization are displayed with their matrix spaces and regularization convention. All five bibliography entries are used. | The block determinant uses the stated MS24 rules. Bibliographic keys and source versions are unchanged. MSY23 remains a style model and is not cited solely for that role. |

No definition or citation omission was identified within this inspection.
The source interfaces retain their existing audit acceptance and proof-depth boundaries.
MSY23/MSY23 remains the primary style model; the [MS24 source observations](../../../audits/literature/MS24/readme.md#presentation-observations) records the inspected source terminology; manuscript applications remain in the current conventions.
Explanatory prose was written independently, without copying community-source passages.

<a id="historical-structure-review-2026-09-12--build-reference-and-visual-evidence"></a>
#### Build, Reference and Visual Evidence

The recorded local latexmk command completed successfully with TeX Live 2025 and pdfLaTeX/BibTeX.
The final TeX log has no actual LaTeX/package warnings, unresolved references or citations, or overfull/underfull boxes.
The launcher emitted its nonfatal Windows Perl locale fallback.

All 15 final PDF pages were visually inspected after the last source edits.
The title, abstract, compact contents, highlighted determinant formula, numbered propositions, long equations, page boundaries, proof endings and bibliography are readable, with no clipping, overlap or missing glyph found.

The document/project records, manuscript index, proof-review index and MS24 application note now point to this organization and review.
No network search, download, Git commit, submission, source-priority determination or research-goal completion is part of this operation.

<a id="historical-structure-review-2026-09-12--exact-reviewed-files"></a>
#### Exact Reviewed Files

Paths are relative to the paper directory.
README and audit navigation edits do not change this complete nine-file TeX/Bib source manifest.

- `main.tex`
- `references.bib`
- `sections/introduction.tex`
- `sections/dyson.tex`
- `sections/positive-pencils.tex`
- `sections/imaginary-drift.tex`
- `sections/minimax.tex`
- `sections/spectral.tex`
- `sections/outlook.tex`
- `build/main.pdf`

<a id="historical-main-review-2026-09-13"></a>
<a id="historical-main-review-2026-09-13--yin_t_f0008-first-manuscript-around-the-general-main-theorem"></a>
### Yin_T_F0008 First Manuscript around the General Main Theorem

Date: 2026-09-13.
Reviewer: the coordinating agent, **self-review by the writing agent**.
Artifact: the seven-file TeX/Bib manifest below for [the current paper](main.tex), including all five sections, abstract and bibliography.
This review covers the actual manuscript; the earlier independent ledger reviews remain separate evidence.

<a id="historical-main-review-2026-09-13--authorization-and-proof-versions"></a>
#### Authorization and Proof Versions

The user selected Yin_C_F0126/Yin_C_F0127 as the combined main theorem, Yin_C_F0121 as secondary, the Yin_C_F0119 phase obstruction as introductory motivation for rho, and Yin_C_F0123 as an application, then authorized writing the first manuscript.
This replaces the earlier progress-paper organization.
The [project provenance table](../readme.md#result-and-proof-provenance) identifies the authoritative complete ledger proofs and their separate reviews.

No reusable lemma was extracted and no project Claim Role field or ledger proof version was changed.
The included Yin_C_F0127 argument is the direct critical-point-to-gap proof, with attainment and the unique optimizer.
Its supplementary rational L2 equivalence and divergent-regularizer consequences are omitted, as are Yin_C_F0120/Yin_C_F0122/Yin_C_F0124/Yin_C_F0125 and elliptic examples.
Thus the paper does not require Yin_C_F0095, Miy26 or Spe26.
These are explicit manuscript scope decisions, not changes to the omitted research results.

<a id="historical-main-review-2026-09-13--mathematical-findings"></a>
#### Mathematical Findings

The full argument was compared with Yin_C_F0119, Yin_C_F0126, Yin_C_F0127, the final matrix-supersolution version of Yin_C_F0121, and the included Yin_C_F0123 calculation.
No unresolved mathematical discrepancy was found at this revision.

1. **General formula:** the real Hilbert--Schmidt quadratic form controls the rho term by the eta term, leaving a strictly positive epsilon contribution.
   Compact sublevels give a minimum before any resolvent identification is used.
   Differentiation of the inner quadratic maximum gives the stated outer critical equation.
2. **Signs and value:** the polar-factor argument and strict subunital adjoint map force both block signs.
   The signed Schur inverse then gives the physical Dyson solution, fixing every critical point and hence the unique regularized minimum.
   The determinant of the block inverse and the two trace identities reproduce the primitive with the correct factor `2m`.
   Rescaling `Q = epsilon^2 R` removes the regularizer by a fixed-trial upper bound, including an infimum of minus infinity.
3. **Attainment:** the unregularized critical equation forces a unitary normalized off-diagonal block.
   The two diagonal positive-map estimates give strict stability on the full complex block space.
   The finite-dimensional analytic implicit step is justified explicitly by contraction of `G -> G - L^{-1} E(w,G)`; its derivative and adjoint symmetry identify the physical upper-half-plane branch.
   Stieltjes inversion and faithful trace then give a true spectral gap.
   Bounded inversion gives the converse and the optimizer limit.
   The real gap derivative determines every critical trial uniquely.
4. **Strict positivity:** square completion proves strict feasibility implies a positive operator gap; the gap Dyson equation proves the converse.
   Finite Fock compressions identify the monotone iteration with the inverse expectation, proving it is the least feasible matrix.
   The directional comparison and positive Hessian at that matrix give global minimality and uniqueness without claiming global ordinary convexity.
   The strict-domain infimum is correctly not attained.
   Its optimizer is `q = E(S^{-1})`, while the main optimizer is `R_* = E(S^{-2})`, related by the differentiated Dyson equation.
5. **Spectral application:** shifts preserve both noise maps.
   The main attainment assertion determines the full spectrum.
   The regularized Brown derivative equation uses the correct lower-left block and sign; the trace density is nonnegative without commuting its two inverse factors.
   The claimed limit is weak, allowing singular measures.
   Brown support is not identified with full spectrum for general nonnormal coefficients.

Boundary checks include no noise, arbitrary complex coefficients, zero capacity, singular covariance outputs, zero determinant, and a nonstrict positive boundary such as `2+s`.
None is silently excluded from the general formula.
Only the secondary theorem requires a strict positive gap.
No assertion of optimization complexity or uniform derivative stability is made.

<a id="historical-main-review-2026-09-13--whole-manuscript-definitions-and-citations"></a>
#### Whole-Manuscript Definitions and Citations

Coverage is **all five final sections, including retained passages**, under the [expanded writing rules](../../../../framework/rules/writing.md#whole-manuscript-definition-review).
This is not a diff-only review.
Mathematical clarity and citation coverage were checked separately.
The standing explicitly permitted background terms remain exempt; no new blanket exemption or Yin_T_F0001-specific source choice was inferred.

| Final section | Organization, meaning and source checks |
| --- | --- |
| Introduction | Determinant/capacity and affine pencil/coefficient maps have independent definitions. Normalized traces, the zero atom, singular outputs, arbitrary complex coefficients, and the real-linear trial calculation are explicit. Freeness and semicircular normalization cite MS17; MS24 Definitions 1.1/2.1 and Section 2.2 supply determinant/capacity/complete-positivity conventions. The phase example and centered reduction are proved in place. |
| Preliminaries | The Cauchy transform has a definition environment and the MS17 Chapter 9 (9.5) convention. Dyson input cites Chapter 9 Definition 10, Theorem 11 and Proposition 13. The physical branch, full block maps, trace pairing, regularizer and scalar gap criterion are explained before use. Hermitization cites MS24 Section 3 and MS17 Chapter 11 Section 9. Positive-map and kernel estimates are supplied explicitly. |
| Main proof | Trial objectives and auxiliary blocks remain local notation. Spaces, real versus complex linearity, adjoints, spectral radius, critical-point directions and inverse conventions are explicit. The analytic implicit step has an explicit local argument. No definition is used to assume a minimizer or a physical branch. No new specialized external mathematical input is imported. |
| Strict-positive theorem | Feasible matrices have their own definition; the Schur equivalence and convexity are proved afterward. Strict positivity, LMI, Fock space, creation-operator action, local Hessian and trace pairing are explained. The Fock realization cites Miy22 Section 2.1, pp. 3–5. Its matrix spectral-law/faithfulness interface was checked against the existing source and ledger records. |
| Spectral applications | Brown measure has a definition environment with the distributional real-Laplacian convention; existence and support are stated separately and attributed to MS17 Chapter 11 Theorem 5, Definition 6 and (11.8). Weak regularization cites Section 9 (11.14)–(11.15). The selfadjoint identification cites p. 270. Density beta avoids collision with the coefficient map rho. The final uses agree with the original trace and resolvent conventions. |

The five definition environments separate defining statements from motivation and proved properties.
Subsequent uses, first introduction, internal references and ambient spaces were checked throughout.
Generic covariance arguments are lowercase `b`; actual evaluations retain their own variables.
Finite normalized determinants use uppercase Delta, both theorem statements present the operator determinant directly, and no formula is boxed.

MSY23/MSY23 remains the primary style model and MS24 the approved community reference.
Source prose was composed independently; no substantial verbatim or near-verbatim reuse occurred.
The five bibliography entries match all citation keys.
Source inputs were checked at their stated use and locator against the local dependency/source evidence; this is not a new audit of the full textbook proofs or a historical-priority search.
No definition/citation obligation was left unresolved within the included scope.

<a id="historical-main-review-2026-09-13--build-and-visual-verification"></a>
#### Build and Visual Verification

The final MiKTeX 25.4/pdfTeX 1.40.27, BibTeX and latexmk 4.88 build succeeded with `latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error main.tex`.
The output has 13 pages.
The final TeX log has no unresolved citation/reference, missing character or layout warning.
The Windows Perl launcher emitted its nonfatal locale fallback.
MiKTeX required the approved access outside the sandbox to its existing user configuration; no package download was needed.

All 13 final pages were rendered and visually inspected for formula width, glyphs, theorem/definition layout, page transitions and bibliography.
No clipping, overlap, missing glyph or unreadable equation was found.
These mechanical checks do not establish the mathematical findings above.

<a id="historical-main-review-2026-09-13--exact-reviewed-manifest"></a>
#### Exact Reviewed Manifest

Paths are relative to the paper directory.
The bibliography was retained unchanged.
README and navigation changes are outside this complete TeX/Bib manifest.

- `main.tex`
- `references.bib`
- `sections/introduction.tex`
- `sections/dyson.tex`
- `sections/main-proof.tex`
- `sections/positive-pencils.tex`
- `sections/spectral.tex`
- `build/main.pdf`

<a id="historical-main-review-2026-09-13--ms24-notation-follow-up"></a>
#### MS24 Notation Follow-up

Date and reviewer: 2026-09-13, the coordinating agent; **self-review limited to the requested notation correction and all affected uses across the five manuscript sections**.
This addendum identifies the current source/output revision; the preceding complete proof and definition/citation review retains its historical manifest and scope.

The user requested a fresh check of MS24, a summary of its notation, correction of the convention and correction of the manuscript.
The [source note](../../../audits/literature/MS24/readme.md#notation-recheck) records the actual arXiv v1 passages and the [revised preference](../conventions.md#yin_t_f0008-covariance-argument) owns the adopted Yin_T_F0008 rule.
Directly inspected source passages include Definition 1.1/Theorem 1.2 (p. 3), the trace and dual conventions (pp. 5–7), scaling matrices (pp. 8–9), the rho/block notation (p. 12), approximate minimizers (p. 14) and positive capacity trials (p. 15).
The relevant text was checked against rendered pages 3, 7, 8, 12, 14 and 15.

The earlier rule exempting all previously named trial matrices from the lowercase-b correction was too narrow.
It is superseded.
MS24 uses b in the capacity infimum and positive trials, while c and c_delta denote other selected matrices.
Its introductory finite matrix B shows that this is a role-sensitive convention, not a universal uppercase prohibition.
Its rho and rho* are already present in Lemma 3.5(ii), so the manuscript now gives that exact citation at their introduction as well as at the block formula.

| Changed use | Current notation and affected-use check |
| --- | --- |
| Main and positive variational trials | R becomes b throughout domains, actions, statements, critical equations, substitutions and applications; the dependent families become b_*, b_epsilon, H_b, T_b and Z_b. The secondary optimizer q retains its distinct meaning. |
| Regularized trial and segments | The main proof's Q becomes c, including c_epsilon, inner-map subscripts and the rescaling c = epsilon^2 b. The positive proof's segment Q_t becomes b_t. The introductory fixed comparison B becomes c. The operator Gram matrices P,Q in the Brown calculation and the preliminary moments Q_k are distinct objects and retain their symbols. |
| Avoiding variable capture | Auxiliary map arguments are x where b is fixed. The scalar b_rho becomes gamma_rho; the first Fock congruence coefficients b_j become d_j. Neither change alters an operand or a multiplication order. |
| Covariance blocks and adjoints | The former tilde-rho is rho*, explicitly identified as the adjoint of rho. Generic block entries are b_ij, giving eta(b_22), rho(b_21), rho*(b_12), eta*(b_11) in the original block order. |
| Identities and scalar matrix determinant | Finite identities are 1_m, 1_d and 1_{2m}; identity maps in Neumann inverses are id. The user's Delta_m notation is retained, with b as its local finite-matrix argument. The unrelated Hilbert-space identity I, resolvent block script-R and right row factors R_i retain their existing meanings. |

Meaning and source checks: every affected definition and use was read in the five sections.
The real-linear solve, trace constants, determinant exponents, star order, strict/non-strict domains, optimizer identities and Brown signs remain the same.
In particular, the rescaling uses the same variable in every factor, and the relation between the main and secondary optimizers is now b_* = q^2 + q eta(b_*) q.
The new rho* definition agrees with its former explicit formula and with MS24.
The source uses a normalized linear-first pairing tr_m(x y*); Yin_T_F0008 retains its stated unnormalized conjugate-first Hilbert--Schmidt pairing and real inner product.
These conventions give the same adjoint maps, and no normalization in the objective or primitive was changed.

Verification distinguishes notation consistency from a new proof audit.
The title/entry file and bibliography are unchanged.
Source searches find no old R trial family, I_m/I_d/I_{2m}, or tilde-rho.
No Claim Role, proof version, mathematical scope or ledger statement changed.
The previous notation-coverage statement is qualified by this correction; the earlier mathematical review is not relabeled as a review of the later revised source.

The final build succeeded with 13 pages; all citations and internal references resolve, and the final TeX log has no layout or missing-character warning.
The existing nonfatal Windows Perl locale fallback remains.
All 13 updated pages were visually inspected, including the main infimum, block covariance, regularized rescaling, secondary minimum and optimizer relation.
No clipping, overlap or missing glyph was found.
Generated PDFs and renderings remain ignored in build/.

Inspected source/output paths, relative to the paper directory:

- `main.tex`
- `references.bib`
- `sections/introduction.tex`
- `sections/dyson.tex`
- `sections/main-proof.tex`
- `sections/positive-pencils.tex`
- `sections/spectral.tex`
- `build/main.pdf`
