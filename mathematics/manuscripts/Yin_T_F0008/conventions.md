# Affine-Capacity Manuscript Conventions

### Yin_T_F0008: Covariance Argument

Scope: the Yin_T_F0008 manuscript.
The [source notation check](../../audits/literature/MS24/readme.md#notation-recheck) records the exact passages and distinguishes observed source practice from its local application.

Use lowercase \(b\) both for the generic covariance argument and for the positive matrix variable throughout the capacity and affine variational formulas:
\[
 \eta(b)=\sum_j a_jba_j^*,\qquad
 \rho(b)=\sum_j a_jba_j.
\]
Apply the choice to the complete variable family and every dependent argument and subscript: \(b>0\), \(b_*\), \(b_\varepsilon\), \(b_t\), \(H_b\), \(\mathcal T_b\), \(Z_b\), \(\mathcal V(b)\), \(F(b)\), \(L(b)\), \(P(b)\) and \(J(b)\).
Do not retain the former positive trial \(R\) under a claim that it is merely an actual evaluation.

Use other lowercase names for distinct trial/scaling matrices, as MS24 uses \(c,c_1,c_2,c_\delta\).
In the present Yin_T_F0008 proof the regularized trial is \(c\), with \(c=\varepsilon^2b\) and corresponding \(c_\varepsilon\).
Once a trial \(b\) is fixed, use \(x\) for a separate dummy argument of an auxiliary map when necessary to avoid shadowing.
Actual evaluations such as \(\eta(c)\), \(\eta^*(P)\), \(\rho(Z_b^*)\) and \(\Theta(G)\) retain their mathematical operands; the source does not make every operand the same variable.

Follow MS24 in writing the covariance adjoints \(\eta^*,\rho^*\), the block arguments \(b_{ij}\), identity matrices \(1_m,1_{2m}\), and the trace distinction \(\operatorname{tr}_m=\operatorname{Tr}_m/m\).
Keep the user's existing \(\Delta_m\) convention for the normalized finite determinant.
Coefficients \(a_j\), semicircular variables \(s_j\), and pencils/operators \(S,T\) already follow the source.
Uppercase auxiliary matrix or transform names remain permitted where explicitly defined; MS24 itself uses a finite matrix \(B\) in its introduction.
Its source-specific \(S^h,\eta^h\) do not require replacing Yin_T_F0008's general selfadjoint-pencil notation \(\mathscr H,\Theta\).

Check the entire affected formulas and proofs, not just the defining lines: domains, optimizers, substitutions, adjoints, block identities, references and multiplication order must remain consistent.
Historical research and audit artifacts retain their inspected notation and actual checked scope.

<a id="yin_t_f0008-real-linear-invertibility"></a>
### Yin_T_F0008: Real-Linear Invertibility

Scope: the Yin_T_F0008 manuscript.
Write that `T_b is invertible as a real-linear map on M_m(C)`.
Use the same explicit wording for the regularized inner map `L_{epsilon,c}`.
This specifies both the linearity and the underlying space.
It does not restrict the matrices to real entries or change the mathematical assertion.

### Yin_T_F0008: Present the Determinant Directly

For the presentation of Yin_C_F0126, State the principal determinant formula with \(\Delta(S)\) on the left, in line with the MS24 determinant formulation.
Retain the equivalent logarithmic action in the proof as needed.
Apply this preference to current Yin_T_F0008 theorem summaries and subsequent manuscript presentation; it does not change the formula, trace normalization, extremum domain or Claim Role.

<a id="yin_t_f0008-first-manuscript-selection"></a>
## Main Manuscript Results

Combine Yin_C_F0126 and the attainment/unique-optimizer assertions of Yin_C_F0127 as the main theorem, present Yin_C_F0121 as the secondary theorem, put the Yin_C_F0119 eta-only counterexample in the introduction to motivate rho, and present Yin_C_F0123 as an application.
The section plan below includes the selected further results.
The [manuscript scope and provenance](readme.md#documents-and-scope) records their actual use.
This selection does not itself extract reusable project lemmas or change Claim Role fields.

<a id="expanded-manuscript-selection"></a>
## Manuscript Section Plan

Keep Yin_C_F0126/Yin_C_F0127 as the central theorem and Yin_C_F0121 as the secondary positive-pencil result.
Organize the expanded paper as follows:

1. Introduction.
2. Preliminaries and the Dyson equation.
3. The general variational formula and attainment.
4. Positive imaginary drift and the Hilbert--Schmidt formula: Yin_C_F0120, followed by the strict-domain Speicher-type formula and the direct comparison of variational objectives.
5. Strictly positive affine pencils: Yin_C_F0121.
6. Ordered min--max principles: the scalar, commuting and isotropic cases of Yin_C_F0122, and the separately scoped strict-Hilbert--Schmidt-positive matrix formula Yin_C_F0125.
7. Spectral applications: the existing Yin_C_F0123 interfaces, the full-spectrum attainment criterion, the isotropic density, and the direct Brown applications selected below.

Use Appendix A for the long global/quadratic-form comparison.
Keep the reduced-Hessian and matrix-regularizer/inverse-Hessian arguments in the body.
Keep the directions of the comparison inequalities, the proof dependency chain, the extremum order and the short scope counterexamples in the main text.
Isotropic covariance in dimension greater than one is not a special case of strict Hilbert--Schmidt-positive covariance.

Use the existing lowercase b family for the general positive trial, with a separately defined lowercase c for the strict-domain variable in the comparison section.
The [fixed quadratic energy-order bridge](../../claims/Yin_C_F0182_v1.md#quadratic-energy-order) retains its actual author self-check scope.
The parameterization now has its complete [C_F0164 proof home](../../claims/Yin_C_F0164_v1.md#argument) and actual [internal self-review](../../audits/reviews/Yin_R_F0175_v1.md#positive-cone-finding); no isolated independent review is asserted.
The general determinant proof remains independent of the subsequent Speicher comparison.
Preserve the distinction between the public proposal Spe26 and the private manuscript Spe26b in attribution.
This selection changes no fixed mathematical Claim, review, Role or completed Task disposition.

<a id="brown-application-plan"></a>
### Brown Application Selection and Placement

The following writing choices retain the exact source scopes and do not themselves establish independent review.
Actual manuscript inspections and builds belong in the [manuscript record](paper/review.md#expanded-review).

| Planned subsection | Content and exposition | Responsible material and exact scope |
| --- | --- | --- |
| 7.1. Shifted potentials and spectral interpretation | Recall the normalized logarithmic potential of the Brown measure, the main variational formula for spectral shifts, and attainment as the full-spectrum criterion. Establish the interface used by all subsequent applications. | [C_F0123](../../claims/Yin_C_F0123_v1.md), [C_F0126](../../claims/Yin_C_F0126_v1.md), [C_F0127](../../claims/Yin_C_F0127_v1.md). Retain the distinction between operator spectrum and support of the Brown measure. |
| 7.2. Determinant lower bounds and atoms of the Brown measure | State short corollaries giving the uniform capacity lower bound, absence of atoms of the Brown measure at positive capacity for arbitrary constant term, and possible atom locations among the eigenvalues of the constant term without a capacity assumption. | [C_F0172, Sections 1--2](../../claims/Yin_C_F0172_v1.md) and [C_F0171, Section 6](../../claims/Yin_C_F0171_v1.md). Arbitrary complex coefficients; neither commutation nor rho=0 is assumed. Atomlessness alone does not imply planar absolute continuity. |
| 7.3. Centered pencils with vanishing rho | Present one substantial proposition: the concave squared-radius envelope, radial cumulative mass from regularized minimizers, absolute continuity away from zero, the density bound, and the exact operator spectral disk. Add the positive-capacity corollary giving absolute continuity of the entire Brown measure. | [C_F0170, Sections 1--4](../../claims/Yin_C_F0170_v1.md), using [C_F0172](../../claims/Yin_C_F0172_v1.md) to exclude the remaining origin atom. Require zero constant term and rho=0; no flatness or irreducibility assumption. The proof does not identify the support of the Brown measure with the whole spectral disk. |
| 7.4. An invertibility criterion and enclosed mass | Derive the finite algebraic equation plus strict CP spectral-radius condition. Under rho=0, specialize to the explicit affine spectral test and exterior determinant, then deduce the mass assigned by the Brown measure to the region enclosed by a resolvent contour from the deterministic eigenvalue count. | [C_F0171, Sections 1--3](../../claims/Yin_C_F0171_v1.md). The general invertibility criterion permits arbitrary rho. The eigenvalue-count formula requires rho=0 and an actual contour in the resolvent set; it is not an unconditional atom-weight formula. |
| 7.5. Density from the variational optimizer | Give the arbitrary positive matrix regularizer as a short lemma, prove the positive optimizer Hessian and its inverse formula, and state formulas for the derivative and Laplacian of the regularized logarithmic potential. Compare with the existing Dyson derivative system without duplicating both full calculations. | [C_F0169, Sections 1--4](../../claims/Yin_C_F0169_v1.md), with [C_F0123](../../claims/Yin_C_F0123_v1.md) supplying the Brown-measure normalization and weak regularization limit. Positivity is at the optimizer; no global convexity, uniform zero-regularizer stability or pointwise density limit is asserted. |
| 7.6. Recoveries and examples | Retain selfadjoint spectral-measure recovery and the isotropic density from the ordered min--max section. Use the scalar circular law and translated deterministic point mass as short normalization checks for the new formulas. | [C_F0122](../../claims/Yin_C_F0122_v1.md), [C_F0123](../../claims/Yin_C_F0123_v1.md), [C_F0170, Section 6](../../claims/Yin_C_F0170_v1.md), [C_F0169, Section 4](../../claims/Yin_C_F0169_v1.md). Keep each example's hypotheses explicit. |

Keep the short matrix-regularization and inverse-Hessian proof in the body.
Appendix A may hold the long Hilbert--Schmidt/global quadratic-form comparison; No second appendix is selected.
The optional residual/Dyson alternative in C_F0169 need not be repeated.
Omit the optional circle-mean disk/atom recovery in C_F0171 and logarithmic disk-mass bound in C_F0172.
Preserve the distinction between the trace of the kernel projection and the mass of an atom of the Brown measure next to any discussion of diverging regularized minimizers.

Use the established lowercase b notation, synchronized provenance and citations.
Mathematical, definition/citation and build reviews cover the actual manuscript revision at their recorded scopes.
The earlier main-theorem proof stays logically independent of these applications and of the Speicher comparison.
Selection for writing does not settle literature priority; the limited related-literature inspection in C_F0170 remains limited.
No new Claim decision, project Role or Task completion decision is implied by this plan.


<a id="intro-result-organization"></a>
## Results in the Introduction

In Subsection 1.3, state the strict Hilbert--Schmidt formula as a proposition and the strictly positive-pencil formula as the secondary theorem, including their actual trial domains and formulas.
Introduce the positive-pencil functional J directly; leave its matrix-exponential representation P and the relation between the two minimizers in Section 5.
Keep the imaginary-constant-term formula in Section 4 and summarize the ordered min--max results with a short forward reference.

In Subsection 1.4, state the uniform capacity bound and absence of atoms of the Brown measure as a corollary, and the radial distribution of the Brown measure, absolute continuity and spectral disk as a proposition.
Leave atom locations, the minimizer representation of radial mass, density bounds and the general Hessian formula in Section 7.
Distinguish the introductory radial statement from the additional density and minimizer formulas in the body.

Keep the complete proofs in their respective body sections and refer to the introductory statements rather than repeating them.
Explain the difference between the two quadratic corrections and the distinction between isotropic and strictly Hilbert--Schmidt-positive covariance in remarks beside the relevant formulas and examples.

## Circular Coefficient Example

In Section 7.3, exhibit linear combinations of free standard circular elements with complex matrix coefficients.
Write the paired semicircular coefficients explicitly and compute rho=0 and eta.
Explain their relation to matrix-valued circular elements using [DG24, Theorem 2.9 and Definition 2.10](../../literature/pdf/DG24.pdf), with the two surviving second cumulants identified.
Briefly mention this class in Introduction 1.4.
Distinguish rotation invariance from the cumulant structure from the variational potential and spectral conclusions obtained by applying the main theorem to T-z1_m.

## Contextual Literature Placement

Incorporate all substantive connections identified by the [manuscript-order literature assessment](related-literature/readme.md), including existing citations whose mathematical role needs explanation.
Preserve the manuscript's section structure and flow.
State a short connection beside the relevant definition, result or proof step; use a nearby remark when an explicit comparison requires more space.
Do not move these explanations to a new appendix.

Identify the actual relationship: a special case, a common equation, a shared proof step, a different hypothesis or a related application.
Give the parameters and necessary assumptions when identifying formulas.
Keep a contextual comparison distinct from a source used to prove the manuscript's result.
Entries for which the assessment found no useful additional citation do not require a forced reference.
For this manuscript, order exposition by the reader's mathematical question and by the role of each result.
Place common identities before the proofs that use them, defer general technical constructions until a result first needs them, and state exact parameters when explaining a specialization or limiting relation.

<a id="opening-motivation"></a>
## Opening Motivation

After the disclosure and before the mathematical background, identify the question in Roland Speicher's public blog post [Spe26](https://rolandspeicher.com/2026/09/09/a-story-of-the-determinant-of-operator-valued-semicircular-elements/) as the motivation: extending the determinant formula for centered operator-valued semicircular elements to arbitrary mean.
Cite the post and describe this work as an experiment in doing mathematics with AI.
Keep this as one short paragraph.

## Hexagon Submission Choices

| Submission item | Author's choice |
| --- | --- |
| Primary subject | `math.OA` |
| Cross-list subject | `math.PR` (Probability; the platform's valid code for the requested `math.P`) |
| MSC2020 classifications | `46L54`, `15A15` |
| Text origin | Entirely generated using OpenAI Astra, as declared by Yin; use the platform's "Primarily AI-generated text" option and state the exact model and extent in the provenance explanation. |
| Human checking and understanding | `none`: no part of the work has been checked and understood by a human, as declared by Yin. |
| Public license | CC0 1.0 Universal. |

The text-origin field does not designate an AI system as a contributor.
The human contributor remains Sheng Yin.
The platform's current category and declaration values are documented in its [official submission schema](https://hexagonmath.org/api/v1/openapi.json).

The abstract states: "The text of this manuscript was generated entirely by OpenAI's large language model Astra."
Begin the introduction with a separate paragraph headed "Disclosure of AI assistance." in bold.
State that the mathematical content and text were generated entirely by an autonomous exploration system using this model under human guidance, followed by the declaration that no part has been checked and understood by the author.
Present the manuscript as a record of the exploration and its findings, shared in its current form to invite feedback and collaboration from interested readers.
These are manuscript-specific disclosures.
Existing agent reviews retain their actual checking relationships and do not establish human verification.

For the disclosure paragraph's format and concise factual style, follow the bold run-in headings on page 2 of Wang and Yin, [Powers of generalized gamma convolutions, arXiv:2609.26558v1](https://arxiv.org/pdf/2609.26558v1).
This is a scoped presentation reference: the model attribution, extent of generation, human-review status and opening placement follow this manuscript's own declarations.
The reference paper's substantive-assistance description, repository statement and Apache license do not apply here.

CC0 1.0 Universal is the selected public license.
The final rights confirmation has not been made.
These choices record submission preparation, not an upload or publication.

## Formula Emphasis

Keep the introductory determinant minimum prominent and explained, without a box.

## Citation Applications

The [citation map](citation.md) records actual external citation uses and links to source evidence.
This file remains the home for manuscript-specific notation, terminology and exposition choices.
