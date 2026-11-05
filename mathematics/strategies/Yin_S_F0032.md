---
author: Yin
---

# Finite-variance spectral controls and the planar logarithmic defect

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance F0012](../tasks/Yin_T_F0012_v3.md#contract) | Almost-sure weak Brown-measure convergence for every fixed scalar polynomial of independent fixed-law finite-variance Wigner matrices, under arbitrary cross-size couplings. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Extend the scalar estimates to actual matrix-coefficient blocks and purely imaginary inverse shifts, while seeking full-sequence logarithmic or planar controls beyond determinant limits in probability. |

## Mechanism and accepted controls

The [reviewed finite-variance theorem](../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed) proves selfadjoint and Hermitized almost-sure weak limits, positive logarithmic tails, regularized potential convergence and planar tightness without higher moments or norm bounds.
Its [exact defect equivalence](../claims/Yin_C_F0186_v4.md#remaining-defect) reduces the remaining general Task to vanishing planar mass of the regularization defect.
This isolates a necessary and sufficient missing assertion rather than asserting a new full theorem.
The exact cyclic subclass \(g(AC^*C)\), \(A=A^*\), is already covered by that reviewed result.

The [reviewed intermediate bound](../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) gives \(s_{N-j}(W+F)\ge c j/N\) for \(j\ge N^{3/4}\), uniformly for independent complex shifts, outside summable failures.
The [completed scalar conditional-shift route](Yin_S_F0033.md#route) now proves the [displayed nonnormal polynomial classes](../claims/Yin_C_F0186_v6.md#statement), including affine two-factor products and polynomial symmetric conditional shifts.
For a general matrix-valued linearization, block-row correlations and coefficient-space degeneracy still need their own estimates; the scalar-shift result does not automatically tensorize.

The [reviewed finite-product extension](../claims/Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed) now treats every displayed reversal-symmetric carrier with conditional-shift factor certificates, its arbitrary outer polynomials at each fixed parameter, and zero-shift ordered products.
The [continuing nonsymmetric test](../drafts/Yin_D_F0011.md) now concerns stronger almost-sure controls for the actual inverse shift of a three-factor product.
The nonsymmetric probability floor below does not by itself give the summability or planar control needed there.
The [reviewed cofactor mechanism](../claims/Yin_C_F0194_v1.md#decision-isolated-minor-reviewed) excludes its exact isolated-minor bottom event with arbitrary polynomially bounded nonsymmetric offsets.
The [reviewed corank-tail theorem](../claims/Yin_C_F0194_v2.md#decision-corank-tail-reviewed) now excludes full corank at least two with any prescribed polynomial failure rate, including the original three-factor product at each fixed nonzero parameter.
That rank result alone left corank-one, well-conditioned and clustered-minor bottom branches, subsequently treated in probability by the floor theorem below.
The [reviewed many-index theorem](../claims/Yin_C_F0194_v3.md#decision-many-index-reviewed) supplies a new probability reduction for those branches using independent rectangular blocks, coarse right-vector spread and finite-radius quadratic matching.
Its [exact polynomial-shift inequality](../claims/Yin_C_F0194_v3.md#polynomial-shift-consequence) retains a mean low-matching probability; the subsequent floor proof controls its tiny-ratio intersection instead of requiring that whole mean to vanish.
The [reviewed unary refinement](../claims/Yin_C_F0194_v4.md#decision-unary-reviewed) additionally controls many effective diagonal or linear terms, while retaining the joint tiny-ratio, low-matching and low-unary-count event.
Its two-point-law cancellation and conditional Rademacher obstruction are explicit.
The [method comparison and counterexamples](../ledger/Yin_L_F0066_v1.md) explain why neither a deterministic symmetric-part floor nor generic finite-to-one Riccati inversion can replace that random input.
The [reviewed nonsymmetric-shift floor](../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed) now gives a polynomial least-singular-value floor in probability for one real Wigner matrix plus an arbitrary independent polynomially bounded complex shift.
Its arbitrary-power second-smallest floor, internal-row cofactor estimate and isolated-minor assembly control the previously uncovered low-matching intersection.
The remaining main error is not summable, so this result supplies no full-sequence almost-sure Brown conclusion.
The [reviewed phase-line theorem](../claims/Yin_C_F0194_v6.md#decision-phase-line-floor-reviewed) now supplies the corresponding probability floor for \(\xi=c\eta\), \(|c|=1\), \(\operatorname{Re}c\ne0\), with a complete weighted-graph and finite-phase counting argument.
Its every-phase auxiliary second-value estimate leaves the pure-imaginary odd-size obstruction intact.
The [reviewed complex-law package](../claims/Yin_C_F0194_v7.md#decision-complex-floor-reviewed) now provides the generic complex orientation-envelope argument and the non-line least-value floor.
It also proves the exact symmetric-quantile guarded pure-imaginary floor and the arbitrary-power even-dimensional floor for zero-diagonal skew inputs and skew shifts.
No arbitrary pure-imaginary shift is claimed to satisfy that guard.
The [reviewed random-diagonal theorem](../claims/Yin_C_F0194_v8.md#decision-random-diagonal-reviewed) now supplies an exponential guard-failure bound uniformly over arbitrary independent complex shifts when the real diagonal law is nonconstant and has finite second moment.
It therefore supplies the all-dimension probability floor for that remaining input class, while a centered zero diagonal still needs a separate structural argument.
The [retained complex orientation and compression examples](../ledger/Yin_L_F0066_v2.md) explain why the stated gauge and quantile hypotheses cannot be dropped.

## Relationship to the Gaussian routes

The completed [Gaussian strong route](Yin_S_F0031.md#route) retains its original scope and completion.
Its Gaussian algebraic-tube probability does not apply to atomic product measures, and the all-affine-fixed-shift extension fails for real symmetric inputs, as shown in [the retained obstructions](../ledger/Yin_L_F0061_v1.md#atomic-tube-obstruction).
The earlier [Schur route](Yin_S_F0028.md#route) and [actual-minor obstruction](../ledger/Yin_L_F0059_v1.md#schur-findings) remain relevant methodological evidence.
Irreducibility with \(\chi_R=0\) cannot justify a conditional estimate uniform over arbitrary invertible minors; any new argument must keep the actual pencil identities.

## Related determinant Tasks

[Matrix-pencil F0013](../tasks/Yin_T_F0013_v1.md#contract) and [scalar-polynomial F0014](../tasks/Yin_T_F0014_v1.md#contract) have separate dimension-limsup determinant completion criteria.
Their [linearization and logical boundaries](../ledger/Yin_L_F0061_v2.md) permit independent progress tracking while this route retains the full F0012 planar-defect objective.
Completion of either determinant Task does not by itself complete this route or F0012.
Their [exact marginal criteria](../claims/Yin_C_F0190_v1.md#statement) permit a favorable deterministic subsequence for the upper-limit problem, while the present route still owes the full-sequence planar assertion.

## Next discriminating work and limits

Identify which part of the accepted scalar inverse-concentration argument survives a fixed auxiliary block size and degenerate coefficient covariance.
The [continuing block-pencil investigation](../drafts/Yin_D_F0010.md#negative-logarithmic-gap) retains the precise warning that a polynomial floor plus qualitative weak convergence is insufficient.
The [reviewed positive-frame block estimate](../claims/Yin_C_F0187_v3.md#decision-block-intermediate-reviewed) now handles correlated physical blocks and gives summable intermediate bounds at its explicit additional coefficient hypothesis.
Its free CDF and finite logarithm do not control the bottom singular values, and the fixed [projection and elimination examples](../claims/Yin_C_F0187_v3.md#actual-projected-block-failure) exclude importing that hypothesis into a general linearization.
The next discriminating estimate must control the intermediate and bottom logarithmic ranges for actual minors, or directly establish the planar defect bound.
The [source frontier and counterexamples](../ledger/Yin_L_F0061_v1.md) prevent using higher-moment theorems or expectation-log assertions outside their hypotheses.
No counterexample to the exact general Task has been established.
The [bounded alternative-mechanism comparison](../ledger/Yin_L_F0063_v1.md) found no supported replacement in its inspected scope.
It records why sharp positive exponential moments, smoothing without spectral stability, and coefficient products without new independent noise do not close the current gap.
The [fixed internal-row and probability-floor argument](../claims/Yin_C_F0194_v5.md#in-probability-floor) has complete independent review and an adopted assessment.
The [reviewed nonsymmetric-carrier assembly](../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) now proves logarithmic convergence in probability and arbitrary-coupling upper-limit equality for its real-input class, including the original three-factor test at every fixed parameter.
The [reviewed complex affine and carrier assembly](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed) now resolves every scalar affine coefficient tuple and every one-Hermitian-variable matrix polynomial under the original complex laws.
Its carrier class allows arbitrary complex backgrounds and eligible exposed inputs, with exact probability, parity and arbitrary-coupling upper-limit conclusions.
The [independent-real-component reduction](../drafts/Yin_D_F0028.md) retains an alternative floor argument under its additional latent-noise hypothesis; the broader eligible-carrier conclusion is fixed in the reviewed assembly.
The [pure-imaginary investigation](../drafts/Yin_D_F0029.md) retains the stronger even-dimensional almost-sure scalar result and tests the remaining polynomial inverse-shift hypotheses without asserting a false all-size floor.
The [one-real-Wigner matrix-polynomial deduction](../drafts/Yin_D_F0012.md#one-real-wigner-matrix-pencil) retains a stronger full-sequence almost-sure logarithmic conclusion than the general complex matrix-fiber theorem.
The [continuing three-factor investigation](../drafts/Yin_D_F0011.md) retains the separate [fresh-border cofactor method](../drafts/Yin_D_F0011.md#fresh-two-border-rewrite), its uniform polynomial-pencil bulk estimate and the remaining relative-normalization gaps for stronger estimates.
The [reviewed complete GOE theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) closes the real-Gaussian Brown submodel and proves arbitrary-coefficient affine upper limits, all-even logarithmic limits and the exact odd-witness classification.
Its quantitative comparison uses the actual Schultz affine Hermitization source, while the [optional direct GOE--GUE comparison](../drafts/Yin_D_F0024.md#optional-direct-comparison) remains a separate continuing proof variant.
The general fixed-law finite-variance contract still requires full-sequence bottom-logarithm or planar-defect control, with purely imaginary inverse shifts and general matrix-coefficient blocks retaining separate unresolved interfaces.
The [exact truncation and scalar-smoothing comparison](../ledger/Yin_L_F0065_v1.md) specifies safe eventual input equality, sharp finite-variance cutoff thresholds, and why harmless scalar spectral smoothing does not bound the singular regularization defect.
