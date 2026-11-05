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
| priority | Preliminary controls and the scalar conditional-shift pilot are reviewed and proved; focus on actual-minor block estimates for general matrix-coefficient linearizations. |

## Mechanism and accepted controls

The [reviewed finite-variance theorem](../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed) proves selfadjoint and Hermitized almost-sure weak limits, positive logarithmic tails, regularized potential convergence and planar tightness without higher moments or norm bounds.
Its [exact defect equivalence](../claims/Yin_C_F0186_v4.md#remaining-defect) reduces the remaining general Task to vanishing planar mass of the regularization defect.
This isolates a necessary and sufficient missing assertion rather than asserting a new full theorem.
The exact cyclic subclass \(g(AC^*C)\), \(A=A^*\), is already covered by that reviewed result.

The [reviewed intermediate bound](../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) gives \(s_{N-j}(W+F)\ge c j/N\) for \(j\ge N^{3/4}\), uniformly for independent complex shifts, outside summable failures.
The [completed scalar conditional-shift route](Yin_S_F0033.md#route) now proves the [displayed nonnormal polynomial classes](../claims/Yin_C_F0186_v6.md#statement), including affine two-factor products and polynomial symmetric conditional shifts.
For a general matrix-valued linearization, block-row correlations and coefficient-space degeneracy still need their own estimates; the scalar-shift result does not automatically tensorize.

## Relationship to the Gaussian routes

The completed [Gaussian strong route](Yin_S_F0031.md#route) retains its original scope and completion.
Its Gaussian algebraic-tube probability does not apply to atomic product measures, and the all-affine-fixed-shift extension fails for real symmetric inputs, as shown in [the retained obstructions](../ledger/Yin_L_F0061_v1.md#atomic-tube-obstruction).
The earlier [Schur route](Yin_S_F0028.md#route) and [actual-minor obstruction](../ledger/Yin_L_F0059_v1.md#schur-findings) remain relevant methodological evidence.
Irreducibility with \(\chi_R=0\) cannot justify a conditional estimate uniform over arbitrary invertible minors; any new argument must keep the actual pencil identities.

## Related determinant Tasks

[Matrix-pencil F0013](../tasks/Yin_T_F0013_v1.md#contract) and [scalar-polynomial F0014](../tasks/Yin_T_F0014_v1.md#contract) have separate dimension-limsup determinant completion criteria.
Their [linearization and logical boundaries](../ledger/Yin_L_F0061_v2.md) permit independent progress tracking while this route retains the full F0012 planar-defect objective.
Completion of either determinant Task does not by itself complete this route or F0012.

## Next discriminating work and limits

Identify which part of the accepted scalar inverse-concentration argument survives a fixed auxiliary block size and degenerate coefficient covariance.
The [continuing block-pencil investigation](../drafts/Yin_D_F0010.md#negative-logarithmic-gap) retains the precise warning that a polynomial floor plus qualitative weak convergence is insufficient.
The next discriminating estimate must control the intermediate and bottom logarithmic ranges for actual minors, or directly establish the planar defect bound.
The [source frontier and counterexamples](../ledger/Yin_L_F0061_v1.md) prevent using higher-moment theorems or expectation-log assertions outside their hypotheses.
No counterexample to the exact general Task has been established.
