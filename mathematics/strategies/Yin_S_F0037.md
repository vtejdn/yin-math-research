---
author: Yin
---

# Trace observations after omitting irregular Wigner entries

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance Brown convergence](../tasks/Yin_T_F0012_v3.md#contract) | Full-sequence weak limits when each strict upper law has a positive absolutely continuous part and diagonals have finite variance. |
| [Matrix pencils](../tasks/Yin_T_F0013_v1.md#contract) | Ordinary affine determinant limsups, including singular drift, along multiples of an invertible witness size. |
| [Scalar polynomial determinants](../tasks/Yin_T_F0014_v1.md#contract) | Prescribed-shift limsups, including the value of the polynomial at zero. |

## Route

| Field | Value |
| --- | --- |
| disposition | completed |
| priority | Completed for each fixed positive absolutely continuous mass in every strict upper law, with arbitrary diagonal laws in the contract. |
| parent | [Ordinary cyclic shifts](Yin_S_F0035.md#route) |

## Positive continuous components and arbitrary diagonals

The initial [dimension surplus after erasure](../ledger/Yin_L_F0070_v1.md#erased) led to separate Gram operators on observed and erased sites.
The [grouped witness](../claims/Yin_C_F0186_v44.md#witness) permits a singular original drift, and the [observed-gradient estimate](../claims/Yin_C_F0186_v44.md#floor) uses only derivatives on the retained upper edges.
For arbitrary positive component masses the [disjoint sets of anchors](../claims/Yin_C_F0186_v45.md#robust) provide enough independent compactly supported observations at almost all outputs.
The [rank descent](../claims/Yin_C_F0186_v45.md#peel) removes the exceptional sites whenever sufficiently many disjoint bases cannot be extracted.
When all raw blocks satisfy the [product-measure tube hypotheses](../claims/Yin_C_F0186_v43.md#statement), the three Wigner limits already follow by repairing the kernel.
For arbitrary fixed diagonal values, the [diagonal-preserving repair](../ledger/Yin_L_F0061_v6.md#repair) yields another test under regular upper laws.
It requires a bound on the projection onto the span of the physical components of an approximate kernel vector.
The [two-channel example](../ledger/Yin_L_F0061_v6.md#obstruction) distinguishes that projection from the mass of the vector at one site.
The [polynomial localization and pointwise-to-planar argument](../ledger/Yin_L_F0070_v1.md#localization) explains why the frame can use a polynomial norm guard and shift-dependent powers of \(N\).
A Bernoulli upper law leaves no continuous marks.
The [spectral-parameter route](Yin_S_F0036.md#route) retains that case as a primary test.
