---
author: Yin
---

# Contextual literature for the affine semicircular determinant manuscript

This assessment answers Yin's request to examine the manuscript in order and find external work that helps readers understand its direct and indirect mathematical connections, beyond indispensable proof inputs.
The original search and selected-statement reading took place on 2026-10-10 against the 33-page manuscript revision identified below.
Its 29 distinct numbered definitions, theorems, propositions, lemmas, corollaries, remarks and examples are all covered in the original inventory, together with the substantial unnumbered arguments in Sections 2, 3, 5, 6, 7 and Appendix A.
These historical numbers are not the numbering of the subsequently expanded [current manuscript](../paper/main.tex).

The original numbered statements below identify the 33-page revision inspected for this assessment.
Yin subsequently authorized integration of the entire substantive comparison map, with concise explanations and nearby remarks while preserving the paper's structure.
The current placements are recorded below.
Existing source audits retain their actual scope; contextual citations do not create new Claim decisions, automatically expand proof dependencies or establish priority.

## Current integration of the substantive comparison map

The authorized revision includes the substantive connections across the whole inventory.
Several original rows share one nearby explanation; elementary steps and searches that found no suitable additional theorem retain their existing proofs without a forced citation.
The table uses semantic TeX labels so that added remarks do not make this navigation depend on obsolete theorem numbers.
Source keys are the actual canonical keys in [references.bib](../../../../literature/references.bib).
The [current manuscript review](../paper/review.md#citation-and-mathematical-comparison-checks) owns integration verification.
The [document README](../paper/readme.md#receiving-build) owns build evidence.

| Current placement | Semantic labels or nearby passage | Integrated connection and canonical sources |
| --- | --- | --- |
| [Section 1](../paper/sections/introduction.tex) | `def:determinant-capacity` | Operator scaling, noncommutative rank and geodesic optimization: `GGOW20`, `AZGL+18`, alongside the existing `Gur04` and `MS24`. |
| [Section 2](../paper/sections/dyson.tex) | `eq:dyson-general`, `eq:imaginary-balance`, `eq:primitive`, `subsec:gap-tools` | Half-plane solution and holomorphic contraction (`HRFS07`), resolvent integration for deterministic log-determinant equivalents (`HLN07`), and strict positive-map defects (`Pop03`). The local proofs and their derivative/stability uses remain explicit. |
| [Section 3](../paper/sections/main-proof.tex) | `rem:capacity-attainment` | Distinguish attained homogeneous capacity and exact scaling (`Gur04`) from attained affine determinant trials, using the scalar semicircular example. |
| [Section 4.1](../paper/sections/imaginary-hs.tex) | `rem:positive-cone-context`, `rem:capacity-congruence` | Positive matrix equations (`HRFS07`), positive-definite geodesics (`SH15`), and common positive congruences in comparison with independent left/right scaling (`AZGL+18`). |
| [Section 4.2](../paper/sections/imaginary-hs.tex) | `rem:hs-strict-domain`, `lem:hs-coordinates`, `rem:hs-objectives` | Retain the public proposal/domain distinction (`Spe26`); identify the geometric mean (`BJL19`) and the exact zero-covariance Wigner–Yanase correction gap (`Han08`). |
| [Section 5](../paper/sections/positive-pencils.tex) | `rem:positive-sdp` | The strict-feasibility criterion is the negative-pencil specialization of the spectral-edge SDP (`Kun26`). The determinant minimum and least feasible matrix remain conclusions of the manuscript argument. |
| [Section 6.2](../paper/sections/ordered-minmax.tex) | `prop:minmax-isotropic`, `eq:minmax-isotropic-coordinate` | Retain Biane's boundary-coordinate identification (`Bia97`) and compare the full real-shift ordered expression with the branch-restricted exterior formula (`BCG25`). This also supplies the comparison for the preceding scalar and commuting cases. |
| [Section 6.3](../paper/sections/ordered-minmax.tex) | `rem:minmax-domains`, `eq:minmax-matrix-inner`, `eq:minmax-matrix-hessian`, `prop:minmax-square-completion` | Order flatness versus Hilbert–Schmidt positivity (`AEK19`); the exact positive inner equation (`Bel15`); reduced-Hessian elimination and quadratic conjugacy (`BV04`). The [Bel15 follow-up](minmax.md#bel15-integration-followup) records the source-variable substitution. |
| [Section 7.1–7.2](../paper/sections/spectral.tex) | `def:brown`, `prop:brown-atoms`, `eq:brown-regularized-minimum` | Hermitization and regularized Brown measures (`BSS18`); distinguish kernel-projection traces from masses of Brown-measure atoms (`ACSY24`). |
| [Section 7.3](../paper/sections/spectral.tex) | `ex:brown-circular-coefficients`, `prop:brown-radial-details`; following scalar R-diagonal remark | Keep the operator-valued circular example (`DG24`) and flatness comparison (`AK20`); distinguish its matrix covariance formula from the scalar R-diagonal S-transform formula (`HL00`). |
| [Section 7.4](../paper/sections/spectral.tex) | `prop:brown-stable-resolvent`, `prop:brown-contour-mass`; following variance-profile and spectral-subspace remarks | Exact diagonal-output spectral-radius reduction and the additional assumptions for support/density conclusions (`AK26`); invariant spectral subspaces and contour masses (`HS09`). The shared strict-defect mechanism is explained earlier through `Pop03`. |
| [Section 7.5–7.6](../paper/sections/spectral.tex) | `prop:brown-optimizer-density`, `rem:dyson-stability`; free-circular-addition remark and block-diagonal example | Circular-addition density formulas (`Zho26`), uniform regularized-density bounds (`BYZ24`), quantitative Dyson stability with extra hypotheses (`AEK19`), and invariant-block Brown measures (`HS09`). |

New source reading remains passage-specific.
In particular, `Bel15` is now retained and Proposition 3.1/Remark 3.2 have been checked; `AK26` has an identified canonical work and artifact; and the Brown-measure author group is `BSS18`, not the repository's different `BSS17`.
Original Lehner and Wigner–Yanase full-text inspection is still not claimed: the concrete comparisons cite the directly inspected `Kun26` and `Han08`.
Appendix A remains an explicit local proof, with its positive-cone input connected to the literature in Section 4 rather than a new comparison appendix.

## How to read the assessment

Each detailed note identifies the mathematical content, the proposed source, the exact or indirect connection, assumptions that affect the comparison, suggested placement, and actual inspection depth.
The four notes contain source titles, versions, primary URLs and checked theorem/page locators:

- [General formula, capacity, Dyson equation and main proof](core.md).
- [Hilbert--Schmidt comparison, positive pencils and Appendix A](comparison.md).
- [Ordered minimum and maximum](minmax.md).
- [Brown-measure applications](brown.md).

An exact identification of a formula or a special case has a different role from a shared proof mechanism, a useful contrasting hypothesis, or broad research context.
The table makes these roles explicit.
Existing citations are retained where they already supply the best connection.
Elementary steps do not need new references merely because they were included in the search.

<a id="complete-inventory-in-manuscript-order"></a>
## Original 29-item inventory in the 33-page revision's order

| Item | Worthwhile external connection | Proposed use and boundary | Detailed note |
| --- | --- | --- | --- |
| Definition 1.1: determinant and capacity | Gurvits; Garg--Gurvits--Oliveira--Wigderson; operator scaling and noncommutative rank | Explain the wider role of capacity. Positive capacity and exact scaling do not imply bounded invertibility of the evaluated pencil. | [Core](core.md) |
| Definition 1.2: affine pencil | Mai--Speicher's centered determinant identity and block covariance | Existing MS24 is sufficient; use the phase example to explain what extra affine data are needed. | [Core](core.md) |
| Theorem 1.3: general formula and attainment | MS24; Hachem--Loubaton--Najim's log-determinant deterministic equivalents; homogeneous scaling | Separate the exact centered recovery, a shared resolvent-integration method, and the different meanings of attained minima. HLN07 does not provide the unrestricted matrix infimum. | [Core](core.md) |
| Proposition 1.4: strict Hilbert--Schmidt formula | Speicher's public proposal; positive-matrix variational descriptions | The public proposal is already cited. Preserve its domain distinction; connect to the concrete comparison in Section 4 rather than add a general reference list. | [Comparison](comparison.md) |
| Definition 1.5: feasible matrices | Kunisky's spectral-edge semidefinite program, following Lehner | The manuscript's block constraint is precisely the zero-threshold constraint for the negative pencil. | [Comparison](comparison.md) |
| Theorem 1.6: strictly positive pencils | The same Lehner--Kunisky spectral-edge formula | Directly explains strict positivity versus strict feasibility. It does not give the determinant minimum, least feasible matrix or uniqueness. | [Comparison](comparison.md) |
| Corollary 1.7: capacity bound and absence of atoms | MS24; Arizmendi--Cebron--Speicher--Yin; free circular addition | Contrast potential lower bounds with point-spectrum/rank information and, separately, planar absolute continuity. Develop this in Section 7.2. | [Brown](brown.md) |
| Proposition 1.8: radial Brown measure | Alt--Kruger; Haagerup--Larsen | Compare matrix covariance data with the scalar R-diagonal S-transform approach. Scalar R-diagonality is not automatic from operator-valued circularity. | [Brown](brown.md) |
| Definition 2.1: matrix Cauchy transform | Helton--Rashidi Far--Speicher; Ajanki--Erdos--Kruger | Explain the distinguished half-plane solution of the Dyson equation and its stability theory. | [Core](core.md) |
| Lemma 4.1: positive-cone minimum | Helton--Rashidi Far--Speicher; Sra--Hosseini | The same positive matrix equation has a fixed-point characterization; the manuscript's geodesic proof supplies its variational characterization. | [Comparison](comparison.md) |
| Proposition 4.2: imaginary constant term | The preceding operator-valued quadratic equation | Reuse the preceding comparison; distinguish the resolvent solution from its determinant evaluation. | [Comparison](comparison.md) |
| Remark 4.3: strict domain | Public Speicher proposal; singular quadratic optimization | The existing counterexample is the useful explanation. A generalized inverse alone does not settle a nonstrict-domain extension; no extra citation is presently needed. | [Comparison](comparison.md) |
| Lemma 4.4: positive coordinates | Bhatia--Jain--Lim and the matrix geometric mean | Exact identification `c_b=b^{-1}#H_b`. It explains the square-root expression, not the entire domain bijection. | [Comparison](comparison.md) |
| Proposition 4.5: corrections comparison | Schur-complement elimination | Shared mechanism, not an externally verified theorem for this inequality. The proof should remain explicit; a general matrix reference is optional. | [Comparison](comparison.md) |
| Lemma 4.6: global comparison | Positive fixed-point equations and quadratic majorants | No close matching external theorem was verified in the bounded search. No additional standalone citation is recommended. | [Comparison](comparison.md) |
| Remark 4.7: comparison under the coordinate change | Wigner--Yanase skew information, with Hansen's directly checked definition | For eta=0 the correction gap is half the squared Hilbert--Schmidt norm of the commutator of b^(1/2) and a_0, hence a multiple of skew information. This interpretation does not extend here to arbitrary eta. | [Comparison](comparison.md) |
| Proposition 6.1: shifted scalar semicircle | Belius--Concetti--Genovese | Compare with a branch-restricted infimum on the left exterior. The manuscript's ordered formula permits every real shift. | [Min--max](minmax.md) |
| Proposition 6.2: isotropic covariance | Biane; Belius--Concetti--Genovese | Biane gives the exact boundary-coordinate and density identification. BCG25 adds a different variational formulation with broader input measures but a narrower shift/branch domain. | [Min--max](minmax.md) |
| Remark 6.3: isotropic covariance and Hilbert--Schmidt positivity | Ajanki--Erdos--Kruger | Order flatness, complete positivity and positive definiteness on Hilbert--Schmidt space are distinct. This is a useful hypothesis comparison. | [Min--max](minmax.md) |
| Theorem 6.4: matrix ordered minimum and maximum | Operator-valued Dyson/subordination theory; reduced Hessians | The source mechanisms give context. None of the checked results was identified with the full theorem, and a minimax-interchange theorem is not its justification. | [Min--max](minmax.md) |
| Remark 6.5: quadratic completion | Boyd--Vandenberghe's positive quadratic conjugacy | Exact standard construction; a citation is optional because the short calculation is already present. It neither interchanges extrema nor proves attainment. | [Min--max](minmax.md) |
| Definition 7.1: Brown measure | Mingo--Speicher; Belinschi--Sniady--Speicher | Retain the existing convention reference; use the research paper for regularization and hermitization, not a duplicate definition. | [Brown](brown.md) |
| Proposition 7.2: possible atom locations | Arizmendi--Cebron--Speicher--Yin; Haagerup--Schultz | Situate a restriction on locations relative to rank information and invariant subspaces. These sources are not identified as proofs of the full arbitrary-coefficient proposition. | [Brown](brown.md) |
| Example 7.3: circular matrix coefficients | Dykema--Griffin; Alt--Kruger | The existing cumulant characterization identifies the class, while the random-matrix literature explains why the model matters. | [Brown](brown.md) |
| Proposition 7.4: radial density and minimizers | Alt--Kruger; Haagerup--Larsen | Compare hypotheses, the data used by the formulas and the support conclusions. Scalar R-diagonal and flatness assumptions must stay visible. | [Brown](brown.md) |
| Proposition 7.5: strict spectral-radius criterion | Popescu's positive-map Stein criterion; Alt--Kruger on deformed circular elements | Explain the stability threshold. The commutative-base overlap is exact in a special class, not a theorem transfer to every coefficient map. | [Core](core.md), [Brown](brown.md) |
| Corollary 7.6: contour mass | Haagerup--Schultz; deformed variance-profile models | Interpret contour integrals as masses of spectral clusters. Under rho=0, distinguish deterministic eigenvalue counting from a general atom-quantization assertion. | [Brown](brown.md) |
| Lemma 7.7: matrix regularizer and inverse Hessian | Resolvent sensitivity and partial optimization | General mechanism only; no close external version of the exact conditional-expectation/Hessian identity was verified. | [Brown](brown.md) |
| Proposition 7.8: regularized density from optimizers | Belinschi--Sniady--Speicher; Zhong; Belinschi--Zhi Yin--Zhong | Connect the formula with hermitization and circular-addition densities. A uniform zero-regularizer estimate is an additional requirement for limiting area density. | [Brown](brown.md) |

<a id="substantial-unnumbered-content"></a>
## Original analysis of substantial unnumbered content

The complete inventory above is supplemented by the following analyses, in their manuscript positions:

- **Sections 1--3:** the centered capacity reduction and exact-scaling comparison; the integrated-resolvent log-determinant formula; hermitization; the strict positive-map inequality and Neumann series; analytic continuation and the spectral-gap test; each step from regularized coercivity to critical-point identification, de-regularization, attainment and uniqueness.
  See [core.md](core.md).
- **Section 4, equations (4.4)--(4.5):** the homogeneous capacity formula is an orbit-norm problem under a common positive congruence.
  The broader left-right scaling literature permits two factors and must not be equated with this restriction.
  The closing hermitization comparison already has adequate references.
  See [comparison.md](comparison.md).
- **Section 5:** block positivity, Fock-space completion, monotone iteration, the least feasible matrix, the determinant minimum, its derivative equation and the nonstrict boundary example are each considered.
  The minus-sign iteration has a different branch from the HRS07 plus-sign iteration.
  See [comparison.md](comparison.md).
- **Section 6:** the commuting reduction (6.5), failure of a global saddle interpretation, the centered equation (6.21), and the covariance counterexample are covered.
  No extra citation is needed for the direct-sum calculation.
  See [minmax.md](minmax.md).
- **Section 7:** the trace of a kernel projection versus the mass of an atom of the Brown measure; spectrum versus support; operator-valued cumulants; optimizer differentiation versus the linearized Dyson equation; the selfadjoint, isotropic, scalar circular, block-diagonal and deterministic examples.
  See [brown.md](brown.md).
- **Appendix A:** the inverse-order inequality, complete positivity of the inverse series, quadratic majorization, support/kernel reduction and the regularizer limit.
  These have recognizable mechanisms, but no checked generic Schur-complement result alone supplies the full argument.
  See [comparison.md](comparison.md).

<a id="connections-that-merit-editorial-priority"></a>
## Original editorial assessment

The highest priority is a precise relationship that changes the reader's understanding of a result.
Several candidates meet that criterion:

1. **Positive pencils and spectral-edge optimization.**
   Kunisky's Theorem 1.9 gives the same block matrix after changing the signs of the pencil coefficients.
   This places the strict-feasibility assertion in an established norm/spectral-edge problem and leaves the determinant assertions clearly distinguished.
2. **The coordinate change and matrix analysis.**
   Recognizing the geometric mean in Lemma 4.4 makes its explicit square root familiar.
   The eta=0 Wigner--Yanase identity in Remark 4.7 explains the correction gap as noncommutativity rather than an isolated numerical example.
3. **Ordered formulas and scalar free convolution.**
   BCG25 is a particularly useful comparison for Section 6: compare its physical branch and left-exterior domain with the manuscript's ordered extrema and full real-shift domain.
   Biane supplies the exact spectral coordinate already used in the text.
4. **Spectral-radius criteria and deformed circular models.**
   Under rho=0, diagonal constant term and diagonal-output covariance, the manuscript's positive-map test reduces to the variance-profile matrix test.
   Explain this overlap before discussing stronger support or density conclusions under the other paper's assumptions.
5. **Regularized Brown measures and the zero-regularizer limit.**
   Belinschi--Sniady--Speicher supplies the established hermitization framework.
   The free-circular-addition results of Belinschi--Zhi Yin--Zhong explain what an additional uniform density bound achieves.
   These references place Proposition 7.8 and its limits in a broader analytic program.
6. **Different notions of atoms and spectral subspaces.**
   ACSY24 is a direct reference for the distinction after (7.11).
   Haagerup--Schultz adds meaning to the contour and invariant-block calculations; neither should be cited as a general Brown-atom theorem for rank data.

For the introductory research picture, the most useful additional connections are operator scaling/noncommutative rank (GGOW20 and Allen-Zhu--Garg--Li--Oliveira--Wigderson), deterministic log-determinant equivalents (HLN07), operator-valued quadratic equations (HRS07), and positive-map stability (Popescu).
Ajanki--Erdos--Kruger adds quantitative MDE context with its stronger assumptions.
These connections should be placed where their mathematical role can be stated, rather than combined into a long list after the main theorem.

General Schur-complement, quadratic-conjugacy and minimax references have lower priority.
The manuscript already explains those elementary operations.
An additional citation is justified when it supports an interpretation that the text actually develops.

<a id="reading-depth-and-checks"></a>
## Original reading depth and checks

The original detailed notes distinguished existing audited inputs, newly inspected selected statements or proofs, and abstract-level leads.
Original Lehner and Wigner--Yanase full texts were not accessible in that pass; the particular formulas were checked through the identified primary later papers.
Haagerup--Larsen's detailed locator relied on an existing repository inspection.
At that stage the Alt--Kruger deformed-circular source still needed its artifact/version reconciled, and Belinschi's operator-valued boundary-geometry paper needed exact-statement reading.
The current integration above records the subsequent `AK26` and `Bel15` work without retrospectively expanding those original reading scopes.
The Kronecker-matrix and noncommutative-inner-rank leads remain outside the adopted theorem-level comparisons.

The original bounded independent checks of the three local identifications, including the required rho=0 correction and reviewer relationship, are retained in the [manuscript-local bounded findings](../paper/review.md#original-related-literature-bounded-review).

The public Speicher proposal remains `Spe26`; historical abbreviations in the detailed notes do not rename canonical keys.

The assessment is not an exhaustive citation-network search, and failure to verify an exact precedent is not a finding of novelty.
Its original priority discussion explains the proposed editorial roles; the later authorization covers the full substantive map, whose actual placements and source keys are recorded in the current integration section.
