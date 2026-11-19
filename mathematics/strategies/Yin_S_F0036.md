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
| priority | Carry the finite-matrix residue detector through the actual cross-color Schur observation, and test its extension beyond commuting polynomial specializations. |
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

The 19 November 2026 [discrete tests](../ledger/Yin_L_F0070_v3.md#density-obstructions) rule out replacing density slicing by coefficient irreducibility or large Boolean relative gradients alone.
The [finite matrix residue detector](../ledger/Yin_L_F0070_v3.md#physical-detector) provides a different source of algebraic information, including an antisymmetric physical cross-color test that recovers all three auxiliary directions.
The [commutator-cubic extension](../ledger/Yin_L_F0070_v4.md#schur) supplies the analogous full four-channel detector for \([x,y]x\).
Prioritize its actual independent-panel and selected-volume interface; the earlier commutator companion has a thin-support Brown problem and served only as the first test of this mechanism.
The correlated-product disk pairing and the quartic principal trims above remain unresolved, without a claim that this new detector supplies either estimate.

For a purely atomic upper law \(\mu\) and an absolutely continuous replacement \(\nu\), consider the mixture \((1-\theta_N)\mu+\theta_N\nu\) on its \(M=N(N-1)/2\) independent upper entries.
The original product is supported on the \(M\)-fold power of a countable set, to which the mixture product assigns exactly \((1-\theta_N)^M\).
Conditioning on no replacements recovers the original product, so the total variation distance is exactly \(1-(1-\theta_N)^M\).
A direct comparison with vanishing total variation requires \(N^2\theta_N\to0\), in which case the chance of even one marked edge tends to zero.
The [positive-component proof](../claims/Yin_C_F0186_v45.md#marks) uses a fixed positive frequency of marked edges, so the unperturbed sign experiment still needs its own determinant estimate.
