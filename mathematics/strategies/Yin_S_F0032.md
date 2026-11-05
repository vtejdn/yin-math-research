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
| priority | The reviewed preliminary controls are complete; focus on the negative logarithmic defect, with a two-factor real-Wigner pilot to test a summable small-value method. |

## Mechanism and accepted controls

The [reviewed finite-variance theorem](../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed) proves selfadjoint and Hermitized almost-sure weak limits, positive logarithmic tails, regularized potential convergence and planar tightness without higher moments or norm bounds.
Its [exact defect equivalence](../claims/Yin_C_F0186_v4.md#remaining-defect) reduces the remaining general Task to vanishing planar mass of the regularization defect.
This isolates a necessary and sufficient missing assertion rather than asserting a new full theorem.
The exact cyclic subclass \(g(AC^*C)\), \(A=A^*\), is already covered by that reviewed result.

The [reviewed intermediate bound](../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) gives \(s_{N-j}(W+F)\ge c j/N\) for \(j\ge N^{3/4}\), uniformly for independent complex shifts, outside summable failures.
The scalar conditional-shift pilot is developed in the child route.
For a general matrix-valued linearization, block-row correlations and coefficient-space degeneracy still need their own estimates; the scalar-shift result does not automatically tensorize.

## Relationship to the Gaussian routes

The completed [Gaussian strong route](Yin_S_F0031.md#route) retains its original scope and completion.
Its Gaussian algebraic-tube probability does not apply to atomic product measures, and the all-affine-fixed-shift extension fails for real symmetric inputs, as shown in [the retained obstructions](../ledger/Yin_L_F0061_v1.md#atomic-tube-obstruction).
The earlier [Schur route](Yin_S_F0028.md#route) and [actual-minor obstruction](../ledger/Yin_L_F0059_v1.md#schur-findings) remain relevant methodological evidence.
Irreducibility with \(\chi_R=0\) cannot justify a conditional estimate uniform over arbitrary invertible minors; any new argument must keep the actual pencil identities.

## Next discriminating work and limits

First test whether the complex-symmetric conditional shift in a two-real-Wigner product admits a polynomial floor with summable failure under only second moments and arbitrary independent diagonal laws.
If it does, combine the floor with the reviewed intermediate estimate and logarithmic-potential controls at the exact coupling quantifiers.
Then identify which part of that proof survives a fixed auxiliary block size and degenerate coefficient covariance.
The [source frontier and counterexamples](../ledger/Yin_L_F0061_v1.md) prevent using higher-moment theorems or expectation-log assertions outside their hypotheses.
No counterexample to the exact general Task has been established.
