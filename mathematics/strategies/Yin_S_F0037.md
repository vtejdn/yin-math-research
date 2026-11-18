---
author: Yin
---

# Trace observations after omitting irregular Wigner entries

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance Brown convergence](../tasks/Yin_T_F0012_v3.md#contract) | Seek summable singular-value lower bounds with arbitrary real diagonal laws and partly continuous off-diagonal laws. |

## Route

| Field | Value |
| --- | --- |
| disposition | proposed |
| priority | Validate the punctured frame with all diagonal observations erased, then allow a small positive fraction of erased off-diagonal sites per row. |
| parent | [Ordinary cyclic shifts](Yin_S_F0035.md#route) |

## The first frame to check

The [dimension surplus after erasure](../ledger/Yin_L_F0070_v1.md#erased) permits the Gram span to lie outside the trace kernel.
At the good sites two constraints are available, proximity to the active image and proximity to the trace kernel.
Test the net on these sites with the Gram projection error included, keeping the Chernoff exceptions separate from the union over erasures.
Once the frame holds for every possible exceptional set, retain the actual marked coordinate derivatives in [Han's determinant argument](../audits/literature/Han26b/Yin_U001.md#wigner-edges).
First target all absolutely continuous upper laws in their declared coordinate spaces, with finite second moments and arbitrary diagonals.
When all raw blocks satisfy the [product-measure tube hypotheses](../claims/Yin_C_F0186_v43.md#statement), the three Wigner limits already follow by repairing the kernel.
For arbitrary fixed diagonal values, the [diagonal-preserving repair](../ledger/Yin_L_F0061_v6.md#repair) yields another test under regular upper laws.
It requires a bound on the projection onto the span of the physical components of an approximate kernel vector.
The [two-channel example](../ledger/Yin_L_F0061_v6.md#obstruction) distinguishes that projection from the mass of the vector at one site.
A second target permits a small singular component whose mass may depend on the number of colors and the cyclic coefficient size.
The [polynomial localization and pointwise-to-planar argument](../ledger/Yin_L_F0070_v1.md#localization) explains why the frame can use a polynomial norm guard and shift-dependent powers of \(N\).
A Bernoulli upper law leaves no continuous marks.
The [spectral-parameter route](Yin_S_F0036.md#route) retains that case as a primary test.
