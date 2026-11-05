---
author: Yin
---

<a id="mnv16-u001"></a>
# Multilinear matching rank and finite-interval anticoncentration

The selected edition is the [2016 journal publication](readme.md), with the actual inspection and unreviewed-proof limits stated there.
The statement below is accepted as an established external input at its precise real-coefficient Rademacher scope.
Acceptance does not establish a project small-singular-value theorem or an independent review of the source proof.

<a id="matching-rank"></a>
## Source definition and exact theorem

Equation (1.1) on PDF p. 2 considers the real multilinear polynomial
\[
 F(x_1,\ldots,x_n)=\sum_{S\subseteq[n],\ |S|\le d}a_S\prod_{j\in S}x_j,
 \qquad a_S\in\mathbb R.
\]
Multilinear means that each individual variable has degree at most one.
For degree d, Definition 1.5 on PDF p. 3 defines rank(F) as the largest integer r for which there are pairwise disjoint d-element sets S_1,...,S_r with |a_{S_j}|>=1.
This is a coefficient-threshold matching quantity, not the spectral rank of a quadratic coefficient matrix.
All constant and lower-degree coefficients are unrestricted.

Theorem 1.6 on the same page states that an absolute constant B satisfies the following for all d,n.
If r=rank(F)>=2, epsilon_1,...,epsilon_n are independent fair signs, and I is any interval of length one, then
\[
 \mathbb P\{F(\varepsilon)\in I\}
 \le\min\left\{
 \frac{Bd^{4/3}\sqrt{\log r}}{r^{1/(4d+1)}},
 \frac{\exp(Bd\log d\log\log r+Bd^2\log d)}{\sqrt r}
 \right\}.
 \tag{MNV}
\]
The interval can have any center, which permits arbitrary constant and linear terms in an application.
The source statement is for a real polynomial and real interval; it is not directly a complex disk estimate.
The original proof and external dependencies are accepted without a new full-proof audit.

<a id="quadratic-specialization"></a>
## Direct degree-two and scale conversion

For d=2 the first denominator in (MNV) is r^(1/9).
Absorbing the fixed factors of two into constants gives
\[
 \mathbb P\{F(\varepsilon)\in I\}
 \le C\sqrt{\log r}\,r^{-1/9}.
\]
The second source bound is C(log r)^C/sqrt(r) for fixed degree two, with an absolute but unspecified exponent C.
Both tend to zero, but neither permits multiplying the bound by n when r is at most proportional to n and then claiming decay.

For a scale lambda>0, if r disjoint quadratic monomial coefficients have modulus at least lambda, apply (MNV) to F/lambda and an interval of length lambda.
A closed event |F-z|<=rho is covered by such an interval when 2rho<lambda, avoiding any endpoint convention.
There is no factor of the number of variables in this scaling.
For a symmetric matrix Q, the coefficient of x_i x_j in x^TQx is 2Q_ij when i and j differ; a double-sum convention must retain that factor.
If those coordinates are normalized as xi_i/sqrt(n), the quadratic coefficient is instead 2Q_ij/n, and the interval scale must also be divided by n.
After conditioning an exact two-copy sign representation of real variables, x_i^2 is affine in the sign, so the source's multilinearity condition applies to the resulting degree-two sign polynomial.
That conditioning and any complex real-or-imaginary projection are separate project arguments in [the fixed matching argument](../../../claims/Yin_C_F0194_v3.md#two-copy-matching), rather than additional conclusions of the source.
