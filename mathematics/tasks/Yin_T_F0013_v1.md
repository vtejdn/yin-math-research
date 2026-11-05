---
author: Yin
---

# Dimension-limsup determinants of matrix-valued affine Wigner pencils

## Contract

### Input model

Fix \(d\ge1\).
For each \(j\), the off-diagonal law \(\xi_j\) is a fixed complex law with \(\mathbb E\xi_j=0\) and \(\mathbb E|\xi_j|^2=1\); the diagonal law \(\zeta_j\) is fixed, real, centered and has finite second moment.
For every \(N\), the upper off-diagonal entries of \(W_j^{(N)}\) are independent copies of \(\xi_j/\sqrt N\), its diagonal entries are independent copies of \(\zeta_j/\sqrt N\), and the lower entries are conjugates of the upper ones.
All these families and the \(d\) matrices are independent within each size.
All sizes live on one probability space with arbitrary cross-size coupling.
Real and atomic laws are allowed, and the real and imaginary components of an entry need not be independent.
The entry laws do not vary with \(N\), and no moment above two or density is imposed.
Let \(s_1,\ldots,s_d\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal tracial state \(\tau\).

### Main question

Fix \(m\ge1\) and arbitrary \(A_0,A_1,\ldots,A_d\in M_m(\mathbb C)\), independently of \(N\), and put
\[
 L_N=A_0\otimes I_N+\sum_jA_j\otimes W_j^{(N)},\qquad
 L=A_0\otimes1+\sum_jA_j\otimes s_j,\qquad
 \tau_m=\operatorname{tr}_m\otimes\tau.
\]
Does
\[
 \limsup_{N\to\infty}\frac1{mN}\log|\det L_N|
 =\log\Delta_{\tau_m}(L)
 \quad\text{almost surely}
 \tag{Matrix-limsup}
\]
hold for every fixed model, coefficient tuple and allowed coupling?
Equivalently, is \(\limsup_N|\det L_N|^{1/(mN)}=\Delta_{\tau_m}(L)\) almost surely?
The event may depend on the fixed tuple, laws and coupling; a common event for all uncountably many tuples is not required.
Use the ordinary FK determinant including zero mass, with \(\log0=-\infty\) and \(\exp(-\infty)=0\).
The coefficients need not be selfadjoint, and the constant matrix may be singular or zero.
Both matrix size \(m\) and the coefficient tuple are fixed as \(N\) grows.

### Scope and completion criteria

Resolve (Matrix-limsup) by a complete proof or a rigorous counterexample under these exact hypotheses and obtain applicable review of that resolution.
A counterexample must specify fixed coefficients and entry laws, an allowed coupling and a positive-probability failure of the displayed equality.
The already available upper bound \(\limsup\le\log\Delta(L)\) alone is not completion.
A GUE-only, scalar-coefficient, monic-only or nondegenerate-covariance result is partial progress for this full affine contract.
The [zero-limit and upper-semicontinuity discussion](../ledger/Yin_L_F0061_v2.md#upper-limit) separates the automatic direction from the unresolved equality.
The [GUE theorem](../claims/Yin_C_F0186_v3.md#statement) and [finite-variance controls](../claims/Yin_C_F0186_v4.md#statement) remain available at their exact existing scopes.
The [real symmetric conditional-shift theorem](../claims/Yin_C_F0188_v2.md#statement) is not a theorem for arbitrary auxiliary matrix coefficients.

Full-sequence fixed-parameter convergence and expectation convergence of unregularized logarithms are not required for completion.
They may be studied as strengthenings only with explicit admissible hypotheses: the [parity and atomic examples](../ledger/Yin_L_F0061_v1.md#real-affine-obstruction) prevent asserting them uniformly in this model.
This Task concerns determinant approximation, separately from the [F0012 full-sequence Brown-measure contract](Yin_T_F0012_v3.md#contract).
The [exact linearization transfer](../ledger/Yin_L_F0061_v2.md#linearization-transfer) explains its sufficient relationship to the [separate scalar determinant question](Yin_T_F0014_v1.md#contract).

For a finite free logarithm, the [reviewed marginal criterion](../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed) shows that the lower bound under every allowed coupling is equivalent to a vanishing lower limit of each fixed lower-deviation probability.
It is enough to approach the target in probability along a suitable deterministic dimensional subsequence.
This exact reduction supplies no such estimate for the general coefficient tuple; the original equality remains unresolved.

The [reviewed GOE affine theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) establishes the upper-limit equality for every fixed coefficient tuple in the exact real Gaussian submodel, including singular constant matrices.
It proves the full logarithmic limit along all even dimensions and classifies full-sequence convergence at a finite target by existence of one odd-dimensional real-symmetric invertible witness.
Arbitrary fixed-law finite-variance entries remain outside that Gaussian result.

The [reviewed complex affine and matrix-fiber theorem](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed) resolves this contract for every scalar coefficient tuple, that is, for all m=1, under the full stated complex finite-variance model.
It also resolves every fixed matrix polynomial in one Hermitian input and the specified real-linear-combination reductions, including arbitrary singular constant matrices.
The finite-target logarithms converge in probability along all even dimensions, with the theorem's exact pure-imaginary zero-diagonal obstruction to a full-sequence probability limit.
Several unrelated matrix coefficient directions remain outside that result, so the original arbitrary-m contract stays active.

The [reviewed positive-frame block theorem](../claims/Yin_C_F0187_v3.md#decision-block-intermediate-reviewed) proves a summable intermediate singular-value bound for fixed matrix coefficients satisfying its additional condition \(\chi_A>0\), with arbitrary constant coefficient \(A_0\).
It also derives a finite free logarithm and controls the intermediate negative-logarithmic range, while leaving the bottom contribution unresolved.
Its actual projected-block and elimination examples show why neither free invertibility nor the ordinary polynomial linearization supplies that frame condition in general.

## Public literature boundary

The [2026-11-05 primary-source comparison](../ledger/Yin_L_F0062_v1.md#wigner-status) found no theorem or counterexample covering this exact contract and identified explicit related conjectures still discussed in 2026.
It does not certify that this precise finite-variance, fixed-parameter, arbitrary-coupling limsup formulation has already been explicitly named as a public open problem.
The distinction between public source status and the repository's internal results is preserved there.
The contract and selected lifecycle decision are unchanged by this literature assessment.

## Current decision

[Selected decision](#decision-separated-determinant-objective)

## Lifecycle and completion

### Decision separated-determinant-objective

| Field | Value |
| --- | --- |
| date | 2026-11-05T03:58 |
| status | active |
| authority | Yin requested separate Tasks for matrix-valued linear-polynomial and scalar-valued polynomial determinants, following the discussion of dimension limsup. |
| reason | The matrix coefficient problem has an independently identifiable analytic obstruction and supplies the scalar determinant problem through exact linearization; the original Brown-measure objective remains separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Matrix-pencil determinant question](#contract) | Ordinary normalized determinant limsup equality for arbitrary fixed affine coefficients under fixed-law finite-variance Wigner inputs and arbitrary cross-size couplings. |
