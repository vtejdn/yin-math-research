---
author: Yin
---

<a id="ckmyz26-u001"></a>
# CKMYZ26: the second eigenvalue moment controls the potential deficit

<a id="second-moment-criterion"></a>
## Criterion and inspected scope

The inspected edition is [arXiv:2611.12785v1](https://arxiv.org/pdf/2611.12785v1), dated 9 November 2026.
The selected reading covers Lemma 2.8, Proposition 2.12, Theorem 3.1, Remark 3.2, Theorem 3.3 and its proof, and the concluding use of Proposition 3.7 in the proof of Theorem 1.1.
For comparison with the repository arguments, it also covers the word-chain construction in Lemma 2.13, the statements and application interfaces of Theorem 3.4, Proposition 3.5 and Lemma 3.6, and the coefficient geometry, projected-column covariance estimate and triangular reduction displayed in Sections 4.1–4.4.
The comparison identifies proof mechanisms and quantifiers, with the complete auxiliary-ensemble singular-value estimates taken as source inputs.

For random \(B_n\in M_{d_n}(\mathbb C)\), the source uses
\[
 b(B_n):=\frac1{d_n}\sum_{j=1}^{d_n}|\lambda_j(B_n)|^2,\qquad
 b(B):=\int_{\mathbb C}|z|^2\,d\mu_B(z).
\]
Under convergence in probability of all tracial star moments, \(\mathbb P(\|B_n\|>R_0)\to0\) for some fixed \(R_0\), and \(\sup_n\mathbb E\|B_n\|^p<\infty\) for some \(p>2\), Theorem 3.1 equates convergence \(\mathbb E b(B_n)\to b(B)\), expected local \(L^1\) convergence of logarithmic potentials, and weak Brown-measure convergence in probability.
The quantities are eigenvalue moments.

<a id="potential-deficit"></a>
## Exact error formula

Put \(U_n(z):=d_n^{-1}\log|\det(B_n-zI)|\) and \(U(z):=\log\Delta(B-z)\).
For \(R>\max(R_0,\|B\|)\), the disk identity gives equations (3.4)–(3.5) on PDF p. 15,
\[
 \mathbb E\int_{D_R}|U_n-U|\,d^2z
 =2\mathbb E\int_{D_R}(U_n-U)_+\,d^2z
 +\frac\pi2\bigl(b(B)-\mathbb E b(B_n)+t_{n,R}\bigr).
\]
Here \(0\le t_{n,R}\le\mathbb E[\|B_n\|^2{\bf1}_{\{\|B_n\|>R\}}]\to0\), while regularization controls the positive part.
Remark 3.2 consequently gives
\[
 \limsup_n\mathbb E\int_K|U_n-U|\,d^2z
 \le\frac\pi2\bigl(b(B)-\liminf_n\mathbb E b(B_n)\bigr)
\]
for every compact \(K\).

Theorem 3.3 transfers second-moment convergence from positive imaginary Gaussian rotations to the original GUE inputs.
The proof of Theorem 1.1 invokes Theorem 3.1 at this endpoint on PDF p. 21.
The complete auxiliary estimates and the remaining support and regularity proofs were outside this reading.

<a id="repository-disk-comparison"></a>
## Comparison with the repository disk criterion

The repository's [D9 disk calculation](../../../drafts/Yin_D_F0009.md#disk-moment) concerns the general fixed-law finite-second-moment Wigner model and uses
\[
 m_{n,R}:=\int\min(|\lambda|^2,R^2)\,d\mu_{B_n}(\lambda),
 \qquad
 q_{n,R}:=\int\log^+(|\lambda|/R)\,d\mu_{B_n}(\lambda).
\]
The source's Lemma 2.8 defines
\[
 T_R(\mu_{B_n})
 :=\int_{|\lambda|>R}
 \bigl(|\lambda|^2-R^2-2R^2\log(|\lambda|/R)\bigr)\,d\mu_{B_n}(\lambda).
\]
Expanding these definitions gives the exact correspondence
\[
 b(B_n)-T_R(\mu_{B_n})=m_{n,R}+2R^2q_{n,R}.
\]
Whenever the source expectation hypotheses hold, substitution in (3.5) gives precisely the expectation of D9's finite-\(n\) identity
\[
 \int_{D_R}|U_n-U|\,d^2z
 =2\int_{D_R}(U_n-U)_+\,d^2z
   +\frac{\pi}{2}(b(B)-m_{n,R})-\pi R^2q_{n,R}.
\]
The common mechanism is the disk integral of the logarithmic kernel and positive-part control from regularization.
The source controls the ordinary second moment in expectation through its norm-tail hypotheses.
D9 uses a bounded cutoff and a pathwise control event suited to its broader model.
Its [remaining lower bound](../../../drafts/Yin_D_F0009.md#wigner-lower-bound) is still an unproved summability estimate for arbitrary Wigner polynomials.

<a id="repository-gue-comparison"></a>
## Comparison with the adopted GUE argument

The repository's completed GUE proof is [C186v1](../../../claims/Yin_C_F0186_v1.md#argument), strengthened in [C186v3](../../../claims/Yin_C_F0186_v3.md#argument) and presented in the [F0012 paper](../../../manuscripts/Yin_T_F0012/readme.md).
Both that proof and CKMYZ26 use a fixed word-chain Schur linearization, Hermitization, a polynomial least-singular-value floor and control of the number of small singular values.
The signs in the root row and column of their word-chain constructions differ by a scalar block conjugation, giving the same Schur complement and auxiliary block structure.

The repository [compresses an approximate kernel](../../../claims/Yin_C_F0186_v1.md#compression), repairs a fixed-dimensional quadratic system using a real polynomial distance inequality, lifts the repair within Hermitian inputs, and [bounds the Gaussian tube around the determinant zero set](../../../claims/Yin_C_F0186_v3.md#tube-without-floor).
These estimates act on the original GUE tuple.
Its intermediate singular-value count uses CGP22 resolvent comparison and SS15 Puiseux regularity.
The [affine concentration and moving-cutoff estimates](../../../claims/Yin_C_F0186_v3.md#summable-small-mass) produce summable marginal errors, and the [planar passage](../../../claims/Yin_C_F0186_v3.md#brown-as) gives almost-sure weak convergence under every cross-size coupling.

CKMYZ26 instead treats the fixed positive-\(y\) rotation
\[
 Z_n(iy)=\cosh(y)G_n+i\sinh(y)H_n
 \ \stackrel{\rm law}{=}\
 G'_n+\sqrt2\sinh(y)C_n.
\]
Conditioning on \(G'_n\) gives tensorized Ginibre pencils with structured means.
Sections 4.1–4.4 use irreducible coefficient geometry, nets in coefficient subspaces, the covariance of a projected independent block column, and a composition series for the general coefficient tuple.
Theorem 3.4 has the form
\[
 \mathbb P\{s_{\min}(I+\textstyle\sum_jR_j\otimes(C_j+D_j))\le t\}
 \le C\bigl(n^a t^{2/m}+e^{-cn}\bigr)
\]
for bounded means \(D_j\).
Lemma 3.6 uses Banna–Mai estimates for the small-singular-value count.
Proposition 3.7 gives convergence in the positive-\(y\) ensemble, and Theorem 3.3 transfers only its expected Brown second moment to \(y=0\), where Theorem 3.1 gives the weak convergence in probability stated in Theorem 1.1.

Thus the general disk criterion in D9 and the source criterion have the same potential-deficit identity, while the adopted complete GUE proof uses different small-value estimates and a different final convergence argument.
The Gaussian rotation transfer supplies a step specific to the source's GUE setting.
The repository comparison is ordinary source reading and mathematical inspection of the cited current arguments, with their existing review relationships retained at their responsible homes.

The [fourth-moment Wigner transfer investigation](../../../ledger/Yin_L_F0068_v1.md) retains the local convexity and integrability tests, the fixed-noise conditional application of Theorem 3.4, and the unresolved zero-noise boundary estimate.
These are repository deductions and applicability limits, rather than additional results asserted by CKMYZ26.

