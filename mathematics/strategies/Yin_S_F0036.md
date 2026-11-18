---
author: Yin
---

# Spectral-parameter variations for Wigner determinant lower bounds

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance Brown convergence](../tasks/Yin_T_F0012_v3.md#contract) | Seek a full-sequence lower bound on a spectral disk under the original entry laws. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Test a bottom left-right pairing for a correlated sign product and a surviving mixed sign difference for the quartic before extending to general pencils. |
| parent | [Ordinary cyclic shifts](Yin_S_F0035.md#route) |

## Determinant growth in a fixed disk

The [disk criterion](../claims/Yin_C_F0359_v3.md#statement) permits the favorable spectral point to depend on all the input entries.
Use the entire vector of characteristic coefficients at the disk center to seek the missing lower bound.
The [singular-space calculation](../claims/Yin_C_F0359_v3.md#minors) explains how even one exceptionally small singular value can be bypassed with a polynomial lower bound on its left-right overlap.
Several bad singular values require a joint minor or other control of cancellation among complementary products.

For \(P=(A+2B)(3A+B)\) near \(i\), first estimate the bilinear overlap with \(3A+B\) for the actual nearly singular vector on the original sign ensemble.
Use an independently exposed block to address the dependence of this vector on the tested entries.
The [elliptic companion](../ledger/Yin_L_F0070_v2.md#elliptic) gives the exact potential at \(i\), where the test point lies strictly inside the free spectrum.
The [uniform exterior floor](../ledger/Yin_L_F0070_v2.md#exterior) covers every compact set outside the explicit ellipse for the sign matrices.
The [bounded symmetric Jordan example](../ledger/Yin_L_F0070_v1.md#spatial) eliminates an argument from factor symmetry and a second-value floor alone.
The [two-moment quadratic trims](../claims/Yin_C_F0186_v42.md#statement) provide the scalar bulk comparison at nonreal centers. [Descent from the top trimmed product](../ledger/Yin_L_F0070_v1.md#spatial)
For \(1+x^2y^2+yx\), the [mixed same-edge sign difference](../ledger/Yin_L_F0070_v1.md#sign) identifies a legal discrete observation at the polynomial level.
Proceed to joint volume estimates only if the coefficient survives conditioning at the terminal singular subspace and is large relative to the retained singular product.
Neither a first characteristic coefficient at infinity nor pointwise convergence in probability supplies the disk probability series.
