---
author: Yin
---

# Yin_T_F0008: Affine Capacity and Spectral Potentials

Primary goal: [Yin_T_F0008](../../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Current manuscript: **A variational formula for affine semicircular determinants**, [TeX entry](paper/main.tex), [build and writing record](paper/readme.md).
Generated PDF output belongs at `paper/main.pdf`; tracking follows the receiving repository’s applicable writing choices.
The source PDF was not transferred; the [build record](paper/readme.md#receiving-build) states the receiving build status.
Actual external citation uses and their source-evidence links are recorded in [citation.md](citation.md).

The [Hexagon submission choices](conventions.md#hexagon-submission-choices) record the selected classifications, CC0 1.0 Universal license, and Yin's declarations about generation using OpenAI Astra and human checking and understanding.
The disclosure in the abstract and at the beginning of the introduction identifies the model; the introduction states the author's own checking status and invites feedback and collaboration.

The [contextual literature assessment](related-literature/readme.md) examines the manuscript in order for external mathematical connections beyond the indispensable proof inputs.
Its original inventory covers the 29 numbered statements of the earlier 33-page revision and its substantial unnumbered arguments in manuscript order.
Yin authorized incorporating all substantive connections from that assessment.
The current manuscript develops them at the corresponding definitions, proofs and nearby remarks; its bibliography uses the canonical source entries.
The [integration review](paper/review.md#citation-and-mathematical-comparison-checks) records the actual citation and comparison checks.
Contextual comparisons retain their stated hypothesis and reading boundaries.

## Documents and Scope

On 2026-09-13 the user selected Yin_C_F0126 and Yin_C_F0127 as the combined main theorem, Yin_C_F0121 as the secondary theorem, the Yin_C_F0119 scalar phase obstruction as introductory motivation for rho, and Yin_C_F0123 as a spectral application, then authorized the manuscript around that selection.
The 2026-10-10 rewrite implements the expanded seven-section selection below with complete proofs.
The necessary Yin_C_F0119 Dyson identities and Yin_C_F0123 spectral-gap interface appear in the preliminaries.
The main formula directly recovers the full centered MS24 identity, including singular outputs and zero capacity.

Yin_C_F0120, Yin_C_F0122, Yin_C_F0124 and Yin_C_F0125 are included in the current expanded manuscript.
The scalar elliptic examples and the additional rational L2 and divergence consequences of Yin_C_F0127 are omitted.
The included Yin_C_F0127 assertions are attainment, critical points, bounded invertibility, unique optimizer and the resulting full-spectrum criterion.
The proof therefore does not import Yin_C_F0095 or Miy26.
The [comparison record](../../ledger/Yin_L_F0033_v1.md) retains the broader research picture and original alternatives.

The selection is a manuscript organization authorized by the user.
No reusable lemmas have been extracted, and the project Claim Role fields and original proof versions have not changed.
Manuscript work does not reopen the completed research goal.
The publication byline and contact details in the TeX were explicitly requested by Yin.
No literature-priority determination is claimed.

## Manuscript Section Plan

The [manuscript section plan](conventions.md#expanded-manuscript-selection) has seven sections: Yin_C_F0120 introduces the strict Hilbert--Schmidt comparison, Yin_C_F0122/Yin_C_F0125 supply ordered min--max formulas, and the spectral applications follow.
Yin_C_F0126/Yin_C_F0127 remain central, with Yin_C_F0121 the secondary positive-pencil result.

The [selected Brown subsections and appendix placement](conventions.md#brown-application-plan) give the writing order, hypotheses and proof sources.
Actual implementation and checks are recorded in the [manuscript review](paper/review.md#expanded-review).

| Fixed argument | Implemented use |
| --- | --- |
| [C_F0169](../../claims/Yin_C_F0169_v1.md) | Matrix regularization, the positive optimizer Hessian and the variational formula for the Laplacian of the regularized logarithmic potential; Section 7.5; the calculation remains in the body. |
| [C_F0170](../../claims/Yin_C_F0170_v1.md) | Centered rho=0 radial distribution, absolute continuity away from zero, positive-capacity absolute continuity and the exact spectral disk; Section 7.3. |
| [C_F0171](../../claims/Yin_C_F0171_v1.md) | The invertibility criterion, contour mass and restriction of atoms of the Brown measure to eigenvalues of the constant term; Sections 7.2 and 7.4. |
| [C_F0172](../../claims/Yin_C_F0172_v1.md) | Uniform capacity lower bound and absence of atoms of the Brown measure at positive capacity; Section 7.2; the optional disk-mass bound is not included. |

The responsible C arguments now select the [complete project self-review](../../audits/reviews/Yin_R_F0177_v1.md) at its actual four separate scopes.
The retained C/L/R accounts preserve the original author and limited collaborator checks, their actual scope and the mathematical inputs used by the existing manuscript review.
No independent whole-project proof review is inferred from these self-reviewed findings.
The manuscript incorporates these arguments; its separately recorded noncontributor checks cover the actual TeX and do not expand the fixed accounts' review scopes.
The completed Task and existing Claim decisions remain authoritative.

## Result and Proof Provenance

Repository IDs are confined to these records and source comments; reader-facing text uses semantic labels and ordinary theorem numbering.

| Manuscript label or passage | Authoritative statement and proof | Research review |
| --- | --- | --- |
| Introduction: `eq:phase-obstruction`; preliminaries: `eq:dyson-general`, `eq:primitive`, `eq:regularized-primitive` | [Yin_C_F0119](../../claims/Yin_C_F0119_v1.md#yin_c_f0119) | [Main contributor review](../../audits/reviews/Yin_R_F0127_v1.md#scope-of-the-passed-review), [determinant notation check](../../audits/reviews/Yin_R_F0127_v1.md#review-of-the-determinant-notation-addendum) and [monotonicity author check](../../audits/reviews/Yin_R_F0173_v1.md#monotonicity-self-review), each self-reviewed at its actual scope. |
| Main theorem: `thm:main`, `eq:main-determinant`; Section 3.1–3.3 | [Yin_C_F0126 general formula](../../claims/Yin_C_F0126_v1.md#yin_c_f0126), its regularized global minimum and rescaling proof | General signed-formula review (original material now separated into [Yin_R_F0128_v1 — R review](../../audits/reviews/Yin_R_F0128_v1.md), [R_F0174 determinant-presentation self-review](../../audits/reviews/Yin_R_F0174_v1.md#determinant-presentation-finding)) |
| Main theorem: attainment equivalences, `eq:main-optimizer`; Section 3.4–3.5; `eq:full-spectrum` | [Yin_C_F0127 attainment](../../claims/Yin_C_F0127_v1.md#yin_c_f0127), using its direct critical-point-to-gap argument | [Isolated attainment review, 2026-10-22](../../audits/reviews/Yin_R_F0180_v1.md#current-affine-attainment) |
| Secondary theorem: `thm:positive`, `eq:positive-minimum`, `eq:optimizer-relation` | [Yin_C_F0121 final matrix-supersolution minimum](../../claims/Yin_C_F0121_v1.md#minimum-over-all-matrix-supersolutions), its Fock iteration and strictness proof | [Selfadjoint review and extension](../../audits/reviews/Yin_R_F0181_v1.md#original-f0072-account) |
| Preliminaries: `eq:stieltjes-interval`, `eq:stieltjes-atom`; applications: `eq:linearized-dyson`, `eq:potential-derivatives` | [Yin_C_F0123](../../claims/Yin_C_F0123_v1.md#yin_c_f0123); Brown construction and weak convergence imported from MS17 | [Spectral review](../../audits/reviews/Yin_R_F0181_v1.md#new-calculations-checked) |
| Introduction: `prop:hs-formula`; Section 4: its proof, `prop:imaginary-drift`, `prop:hs-comparison`; Appendix A | [C_F0120](../../claims/Yin_C_F0120_v1.md), [C_F0124](../../claims/Yin_C_F0124_v1.md), the fixed [quadratic energy-order comparison](../../ledger/Yin_L_F0054_v1.md#quadratic-energy-order) and the parameterization in [C_F0164](../../claims/Yin_C_F0164_v1.md#argument) | Current manuscript comparison review below; source attribution is to public Spe26, not private Spe26b. |
| Section 6: `prop:minmax-scalar`, `prop:minmax-isotropic`, `prop:minmax-matrix`, `eq:minmax-hs-square-completion` | [C_F0122](../../claims/Yin_C_F0122_v1.md), [C_F0125](../../claims/Yin_C_F0125_v1.md), [C_F0164](../../claims/Yin_C_F0164_v1.md#argument) | [R_F0181, retained scalar/isotropic account](../../audits/reviews/Yin_R_F0181_v1.md#original-f0071-account), [R_F0125](../../audits/reviews/Yin_R_F0125_v1.md), and current manuscript review. Bia97 is credited for the classical spectral coordinate and density. |
| Introduction: `cor:brown-capacity`, `prop:brown-radial`; Section 7: their proofs, `prop:brown-atoms`, `prop:brown-radial-details`, `prop:brown-stable-resolvent`, `prop:brown-contour-mass`, `lem:brown-matrix-regularizer`, `prop:brown-optimizer-density` | [C_F0169](../../claims/Yin_C_F0169_v1.md), [C_F0170](../../claims/Yin_C_F0170_v1.md), [C_F0171](../../claims/Yin_C_F0171_v1.md), [C_F0172](../../claims/Yin_C_F0172_v1.md) | Current noncontributor manuscript Brown review, separately scoped from the retained L author/collaborator accounts and the [current complete project self-review](../../audits/reviews/Yin_R_F0177_v1.md). AK20 supplies a related-work comparison under stronger flatness hypotheses. |
| Section 7.3: `ex:brown-circular-coefficients` and the following cumulant explanation; brief mention in Introduction 1.4 | [C_F0173: complete coefficient and cumulant argument](../../claims/Yin_C_F0173_v1.md#circular-example-statement); [DG24, Theorem 2.9 and Definition 2.10](../../audits/literature/DG24/Yin_U001.md#dg24-u001) supplies the operator-valued circular terminology. | [Original independent coefficient/cumulant finding](../../audits/reviews/Yin_R_F0130_v1.md#circular-example-independent-review) covers the example, complete local cumulant proof, source use and hypothesis interface. The [current manuscript-local check](paper/review.md#circular-coefficients-and-radial-application) records the scoped coefficient and citation correspondence. The Brown and spectral proofs retain their existing local inputs. |

The [current manuscript review](paper/review.md#expanded-review) records the complete integration self-review and three noncontributor agent checks of the actual TeX, along with definition and citation coverage.
No ledger review is repurposed as a review of the current manuscript.

## Manuscript Review Entries

The [manuscript review record](paper/review.md) owns current manuscript scrutiny.
Its [object and hypothesis account](paper/review.md#object-and-hypothesis-correspondence) reconciles terminology checks and their correction in one current entry.
The [result-connection account](paper/review.md#result-connections-and-introduction) covers the introductory statements and their body references, and the [circular-example account](paper/review.md#circular-coefficients-and-radial-application) distinguishes the local exposition check from the fixed independent finding.
Each account retains its actual participation relationship, findings and limits.
The [document README](paper/readme.md) owns source/output instructions and build evidence.

The current [introduction organization](conventions.md#intro-result-organization) presents the Hilbert--Schmidt formula, positive-pencil theorem, capacity corollary and proposition on the radial Brown measure as explicit results in Subsections 1.3--1.4.
Their proofs remain in Sections 4, 5 and 7.

## Writing References and Earlier Versions

Primary style model: [MSY23/MSY23](../../audits/literature/MSY23/readme.md#presentation-observations), following the standing user designation.
[MS24](../../audits/literature/MS24/readme.md#presentation-observations) supplies determinant/capacity terminology and motivating exposition.
MS17 supplies operator-valued and Brown-measure conventions; Miy22 supplies the Fock-space realization.
The earlier mathematical inputs remain locally available.
During the rewrite, public AK20 and Bia97 were acquired and statement-checked for precise related-work attribution; see their [AK20](../../audits/literature/AK20/readme.md) and [Bia97](../../audits/literature/Bia97/readme.md) reading records.
No substantial source prose was reused.

The current source tree contains seven included sections and one comparison appendix; its generated output location is `paper/main.pdf`.
Useful [earlier build evidence](paper/readme.md#earlier-build-evidence) retains its historical source manifests, commands and actual results; it does not certify the current source contents.
