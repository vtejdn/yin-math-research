---
author: Yin
---

# Normalized Schur-complement anti-concentration for GUE linearizations

## Task associations

| Task | Scope |
| --- | --- |
| [F0012 contract](../tasks/Yin_T_F0012_v1.md#contract) | The full fixed-degree scalar-polynomial class through a least-singular-value estimate for its GUE linearizations. |

## Route

| Field | Value |
| --- | --- |
| disposition | superseded |
| priority | Its general monic-pencil deliverable is achieved by successor S_F0030 using finite-dimensional geometric repair; the universal conditional Schur estimate remains unproved. |

## Precise target and mechanism

The [exact word-chain reduction](../ledger/Yin_L_F0058_v2.md#exact-linearization) transfers every fixed scalar polynomial to a fixed-size matrix-valued linear pencil.
A sufficient general target is: for every fixed \(m,d,R_1,\ldots,R_d\), some \(C_R>0\) satisfies
\[
 \mathbb P\{s_{\min}(I_m\otimes I_N+\sum_jR_j\otimes H_j^{(N)})<N^{-C_R}\}\longrightarrow0.
\]
The [monic normalization and inverse compression](../ledger/Yin_L_F0058_v2.md#monic-target) show that this would resolve F0012 with the existing logarithmic bridge.
This sufficient target is now proved in [C_F0186](../claims/Yin_C_F0186_v1.md#statement) by a different mechanism.
The weaker subexponential floor below remains a sufficient target for the conditional Schur approach.
Keep the [corner spectral parameter and determinant normalization](../ledger/Yin_L_F0058_v2.md#spectral-parameter); ordinary eigenvalue convergence of the linearization matrix is a different assertion.

Use a fixed-size linearization of \(P(H)-zI\) for almost every fixed \(z\).
Delete a physical row and column together, so the remaining minor is independent of the exposed GUE variables.
For \(T_N=\begin{pmatrix}D&B\\C&Q\end{pmatrix}\), control
\[
 F:=(I+BQ^{-1}Q^{-*}B^*)^{-1/2}(D-BQ^{-1}C).
\]
This is the normalized block-distance matrix.
Its normalization and inverse-minor dependence are essential.

A sufficient first target is a subexponential lower-tail estimate for these distances strong enough to control all block rows, including exceptional minor events.
The [block inverse calculation](../ledger/Yin_L_F0058_v1.md#schur-route) converts such a bound to the [common sufficient floor](../ledger/Yin_L_F0058_v1.md#common-bridge):
\(\mathbb P\{s_{\min}(P(H)-zI)^2<e^{-N^{\kappa_z}}\}\to0\), with \(0<\kappa_z<\alpha_z\gamma_z\).
A polynomial floor would be stronger than needed.

## Inputs and obstruction

The Han26 polynomial linearization remains algebraically usable, but its independent exposed-column proof does not transfer to GUE.
The Schur numerator is a fixed-size quadratic Gaussian polynomial conditional on the minor.
A determinant small-ball estimate alone does not control the normalized matrix.
Irreducibility of coefficient matrices also does not imply Nie22's global bilinear condition.
Both failures have [explicit tests](../ledger/Yin_L_F0058_v1.md#schur-route).
The [finite-dimensional covariance criterion](../ledger/Yin_L_F0058_v2.md#covariance-boundary) isolates the easy case \(\chi_R>0\) and proves why the direct Nie application fails when \(\chi_R=0\).

## Disposition and retained obligations

The irreducible \(\chi_R=0\) investigation gives an actual three-cycle pencil with a conditional polynomial floor, but refutes the proposed estimate uniform over unrestricted bounded invertible minors.
The complete [calculations and failure scope](../ledger/Yin_L_F0059_v1.md#schur-findings) distinguish that failure from the still possible actual-minor Schur mechanism.
The investigation led to [S_F0030](Yin_S_F0030.md#route), which proves the general target without a covariance assumption.
The exact [F0012 completion](../tasks/Yin_T_F0012_v1.md#decision-full-polynomial-proof) removes the need to close the universal conditional Schur estimate for this Task.
That stronger methodological question remains unproved and is not certified by the geometric argument.

## Evidence

[Source boundaries](../ledger/Yin_L_F0058_v1.md#source-boundary) and [normalized Schur mechanism](../ledger/Yin_L_F0058_v1.md#schur-route).
