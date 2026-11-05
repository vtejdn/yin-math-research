---
author: Yin
---

# Full logarithmic limits for one-real-Wigner matrix polynomials

This continuing deduction concerns the stronger full-sequence almost-sure logarithmic limit for matrix polynomials in one real Wigner input, with arbitrary fixed coefficient matrices.
The broader complex-input probability and arbitrary-coupling limsup conclusions are fixed in the [reviewed C_F0186_v11 theorem](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed), including every scalar affine tuple, the exact parity classification and one-variable matrix fibers.
The argument below retains the stronger real-input convergence mode that is not asserted by that general complex theorem.
It is a direct deduction from reviewed scalar inputs, without a separate fixed Claim or independent review of this matrix-polynomial strengthening.
The general multi-direction coefficient question in [F0013](../tasks/Yin_T_F0013_v1.md#contract) remains unresolved.

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
