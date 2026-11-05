---
author: Yin
---

# Coupling criteria and finite-variance Wigner determinant upper limits

This continuing investigation concerns [matrix-pencil F0013](../tasks/Yin_T_F0013_v1.md#contract) and [scalar-polynomial F0014](../tasks/Yin_T_F0014_v1.md#contract).
The exact contracts retain fixed finite-variance Wigner laws, arbitrary fixed coefficients and arbitrary dependence between dimensions.
The [regularized upper-bound and linearization discussion](../ledger/Yin_L_F0061_v2.md) and [bounded source comparison](../ledger/Yin_L_F0062_v1.md#wigner-status) are starting inputs, rather than a completed solution.
The present material is proof development and has no independent-review status.

## Starting question and discriminating target

The existing almost-sure upper bound reduces the finite-target case to a lower recurrence assertion for the normalized ordinary logarithmic determinant.
The first question is exactly how weak a marginal probabilistic lower estimate suffices under every cross-dimensional coupling, and what failure of that estimate would permit an adversarial coupling to do.
The real commutator parity obstruction prevents demanding convergence in probability along all dimensions in complete generality.
A deterministic subsequence with a lower probability limit may still suffice.

## Current unresolved mathematical scope

No general lower recurrence estimate or counterexample for the full affine Wigner contract is asserted here.
Any proposed block or scalar subclass must retain its actual matrix coefficients and fixed parameter, including singular constant coefficients.
A polynomial least-singular-value floor alone remains insufficient by the [retained negative-logarithmic gap](Yin_D_F0010.md#negative-logarithmic-gap).

## Fixed criteria and polynomial closure

The complete marginal coupling criteria and their proofs are now fixed in [the reviewed C_F0190_v1 theorem](../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed), with its exact application limits there.
No new probability estimate for the full Wigner contract follows merely from that reduction.
The outer-polynomial and zero-shift ordered-product determinant deductions are fixed in [C_F0186_v7](../claims/Yin_C_F0186_v7.md#outer-polynomial-statement), with their complete root-factorization argument at [the fixed proof](../claims/Yin_C_F0186_v7.md#outer-polynomial-argument).
Both fixed materials remain at their actual recorded mathematical assessment and review scope.
The unique one-real-Wigner matrix-coefficient specialization below remains continuing work in this Draft.
The real-symmetric witness construction is fixed in the [reviewed all-large-even result](../claims/Yin_C_F0186_v9.md#all-even-witness).

<a id="one-real-wigner-matrix-pencil"></a>
## Arbitrary matrix coefficients in one real Wigner variable

For one real Wigner input and arbitrary fixed \(A_0,A_1\in M_m(\mathbb C)\), the full logarithmic determinant limit in F0013 follows from the accepted scalar theorem, even when \(A_0\) and \(A_1\) are singular and do not commute.
More generally, let \(H(t)\in M_m(\mathbb C[t])\) be any fixed matrix polynomial and write \(q(t)=\det H(t)\in\mathbb C[t]\).
For each real symmetric \(W_N\), unitary diagonalization of \(W_N\) gives
\[
 \det H(W_N)=\prod_{j=1}^N q(\lambda_j(W_N))
 =\det q(W_N).
\]
Here \(H(W_N)\) acts on \(\mathbb C^m\otimes\mathbb C^N\), and \(q(W_N)\) acts on \(\mathbb C^N\).
On the free side, the spectral theorem for the selfadjoint semicircular element gives
\[
 \log\Delta_{\operatorname{tr}_m\otimes\tau}(H(s))
 =\frac1m\int_{-2}^2\log|q(t)|\,d\mu_{\mathrm{sc}}(t).
\]
Indeed, for every spectral value \(t\), the sum of the \(m\) logarithmic singular values of \(H(t)\) is \(\log|\det H(t)|\), including the value \(-\infty\) at singular fibers.
The positive part is bounded on the compact interval, so the equality of the integrals is justified using a decreasing lower truncation or negative-part monotone convergence.
If \(q\equiv0\), every finite pencil is singular and the free logarithm is \(-\infty\), yielding the required identity immediately.
Otherwise factor \(q\) and apply the reviewed [scalar fixed-shift theorem](../claims/Yin_C_F0186_v6.md#statement) with base \(R(x)=x\) at its finitely many roots, as in [the fixed factorization argument](../claims/Yin_C_F0186_v7.md#outer-polynomial-argument), to obtain
\[
 \frac1{mN}\log|\det H(W_N)|
 =\frac1m\frac1N\log|\det q(W_N)|
 \longrightarrow\log\Delta(H(s))
 \quad\text{almost surely}.
\]
A nonzero \(q\) has finite free logarithm, since it has finitely many roots and the semicircle density is bounded.
The input laws may have arbitrary finite-variance real diagonals and no higher moments or density; the event applies under every cross-size coupling.
Taking \(H(t)=A_0+A_1t\) settles the complete matrix-coefficient question for this one-real-Wigner submodel.
For several real Wigner inputs, the same argument applies to \(A_0+B\sum_jr_jW_j\) with fixed real \(r_j\), because their nonzero normalized linear combination is again a real fixed-law finite-variance Wigner matrix, and the matching free linear combination is semicircular with the same variance.
This is a direct application of the already reviewed scalar input rather than a new matrix-coefficient small-value estimate.
General matrix coefficients in several variables, and complex-Hermitian input laws outside the accepted real-input small-value theorem, remain unresolved by this deduction.
This continuing matrix-coefficient deduction has not been selected as a fixed Claim or independently reviewed here.
