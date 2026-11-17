---
author: Yin
---

# Real shifts of products of two correlated Wigner forms

<a id="statement"></a>
## Sign differences and fixed real shifts

Let \(A_N,B_N\) be independent symmetric Wigner matrices with independent fair signs on and above their diagonals, divided by \(\sqrt N\).
Fix linearly independent real coefficient vectors \(\alpha,\beta\in\mathbb R^2\) and set \(U=\alpha_1 A_N+\alpha_2 B_N,\ V=\beta_1 A_N+\beta_2 B_N,\ P_N=UV\).
Write \(u,v\) for the same two forms in a free standard semicircular pair and \(\nu=\|\alpha\|_2\|\beta\|_2\).
Fix a real \(z\ne0\), put \(\epsilon=\operatorname{sgn}z,\ k=\epsilon\langle\alpha,\beta\rangle,\ t=\sqrt{|z|}\), and assume
\[
 \epsilon(\alpha\cdot d)(\beta\cdot d)>0\quad\text{for some }d\in\{-1,0,1\}^2,
 \qquad t\ne(\nu+k)/\sqrt{\nu}.
 \tag{1}
\]
Then \(\Pr\{s_{\min}(P_N-zI)\le tN^{-3}\}\le C_zN^{-1/4}\) for all sufficiently large \(N\).
The ordinary normalized log determinant \(N^{-1}\log|\det(P_N-zI)|\) converges to \(\tau\log|uv-z|\) in probability.
For every coupling across sizes it converges almost surely to this value along \(N=2^j\), and its full-sequence almost-sure limsup equals the same value.
At \(z=0\) the same log limits hold with value \(\log\nu-1\) for the original [real finite-variance Wigner laws](../tasks/Yin_T_F0013_v1.md#input-model), including arbitrary admissible diagonal laws.

<a id="argument"></a>
## The symmetric pencil

Set \(r=\sqrt{\|\beta\|_2/\|\alpha\|_2}\), so \(r\alpha,\epsilon\beta/r\) have the same squared length \(\nu\) and inner product \(k\), with \(|k|<\nu\).
The Hermitian two-channel matrix
\[
 H=\begin{pmatrix}rU&tI\\tI&\epsilon V/r\end{pmatrix}
\]
has drift \(tX\), where \(X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), and random coefficients \(D_j=\operatorname{diag}(r\alpha_j,\epsilon\beta_j/r)\).
By (1), after changing the sign of \(d\) if needed, \(\sum_jd_jD_j\) is positive definite.
Swapping the block columns gives top-left pivot \(tI\) and Schur complement \(-(\epsilon/t)(VU-zI)\).
Thus \(|\det H|=|\det(P_N-zI)|\), since \(VU-zI=(P_N-zI)^*\).
When invertible, the inverse Schur complement has norm \(t\|(P_N-zI)^{-1}\|\), bounded by \(\|H^{-1}\|\) as a corner of the inverse after the swap.
The same factorization over the free algebra has unit triangular factors and a unitary column swap.
Multiplicativity of the Fuglede--Kadison determinant and its invariance under adjoints therefore give \(2\log\Delta_{\operatorname{tr}_2\otimes\tau}H(s)=\tau\log|uv-z|\).

<a id="stability"></a>
## Stability at zero energy

Write \(\mathcal S(T)=\sum_jD_jTD_j\).
It multiplies the diagonal entries by \(\nu\) and the off-diagonal entries by \(k\).
For \(\eta>0\) the unique \(R>\nu\) satisfying
\[
 1=\frac{R\eta^2}{(R-\nu)^2}+\frac{Rt^2}{(R+k)^2}
\]
exists because the right side decreases strictly from infinity to zero on this interval.
Put \(h=\eta/(R-\nu)>0,\ n=t/(R+k)\).
Then \(h^2+n^2=1/R\), and \(M=ihI+nX\) has positive imaginary part.
Direct substitution gives \(-M^{-1}=i\eta I-tX+\mathcal S(M)\), identifying the positive-imaginary-part Dyson solution.
In particular \(\|M\|=1/\sqrt R\le1/\sqrt\nu\).

On \(\operatorname{diag}(1,-1)\) and \(\left(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right)\), which both anticommute with \(X\), the operator \(T\mapsto T-M\mathcal S(T)M\) acts by \(1+\nu/R\) and \(1+k/R\), respectively.
On the ordered basis \(I,X\) its matrix is
\[
 \begin{pmatrix}
 1-\nu(n^2-h^2)&-2ikhn\\
 -2i\nu hn&1-k(n^2-h^2)
 \end{pmatrix}.
\]
Its determinant is
\[
 (1-\nu/R)(1-k/R)+2(\nu+k)h^2>0 .
\]
As \(\eta\downarrow0\), \(R\) decreases to a finite limit \(R_0\ge\nu\), by monotonicity of the defining equation in \(R\) and \(\eta\).
For \(t<(\nu+k)/\sqrt\nu\), a limit \(R_0>\nu\) would require \(R_0t^2/(R_0+k)^2=1\), whereas this term is already less than one at \(\nu\) and decreases thereafter.
Hence \(R_0=\nu\) and \(h^2\to1/\nu-t^2/(\nu+k)^2>0\).
For \(t>(\nu+k)/\sqrt\nu\), the second term alone exceeds one at \(\nu\), so \(R_0>\nu\) and \(h\to0\).
In either case the displayed determinant stays positive at the limit.
As \(\eta\to\infty\), \(R\to\infty\), \(M\to0\), and the stability operator tends to the identity.
Continuity and the displayed bounds give a uniform inverse on the entire ray.
At equality in (1)'s excluded scale, \(R_0=\nu,\ h\to0\) and this stability determinant vanishes.

The [sign-chord spectral flow theorem](Yin_C_F0356_v2.md#statement) at \(E=0\) now gives the stated floor via the inverse corner bound, and the stated logarithmic limits via the finite and free determinant identities.
At \(z=0\), each nonzero factor divided by its coefficient norm is a Wigner matrix with the prescribed scalar hypotheses.
Apply the [scalar case of the affine determinant theorem](Yin_C_F0353_v2.md#statement) to each factor.
Their fixed-clip upper bounds give the joint full-size upper bound, and both logs converge jointly in probability and on the same dyadic sequence by a union bound.
Finite and free multiplicativity add the two normalized logarithms.
Integrating \(\log|x|\) against the standard semicircle gives \(-1/2\), hence the sum in the limit is \(\log\nu-1\).

<a id="example"></a>
## Two injective sign forms

For \(\alpha=(1,2),\ \beta=(3,1)\), each raw form distinguishes the four sign words, so each is determined by the other.
Both original random coefficients of the symmetric companion have rank two.
The chords \(d=(1,0)\) for positive shifts and \(d=(1,-1)\) for negative shifts satisfy (1)'s strict sign condition.
With \(\nu=5\sqrt2\), the only real shifts omitted by these conclusions are \((\nu+5)^2/\nu\) and \(-(\nu-5)^2/\nu\).

<a id="nonreal"></a>
## Constant changes of basis at a nonreal shift

For complex \(w\ne0\) choose \(a^2=w\) and consider the two-channel complex symmetric pencil with diagonal forms \(U,V\) and off-diagonal entries \(aI\).
If invertible complex channel matrices \(L,K\) made \(L(\cdot)K\) Hermitian for all real scalar input values, a congruence by \(L^{-1}\) would make \((\cdot)D\) Hermitian for \(D=K(L^*)^{-1}\).
The independence of the two coefficient vectors implies that \(E_{11}D\) and \(E_{22}D\) are Hermitian individually, so \(D\) is real diagonal with nonzero entries \(d_1,d_2\).
The constant part then requires \(ad_2=\bar a d_1\), giving \(a/\bar a=\pm1\) and \(w\in\mathbb R\).
Thus a nonreal shift precludes a Hermitian two-sided equivalence of this particular companion.

## Current assessment
[Selected decision](#decision-correlated-product-reviewed)

## Assessment history

### Decision correlated-product-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:29 |
| status | open |
| reason | The symmetric pencil and its explicit stability operator give a candidate fixed-real-shift result for correlated product factors. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Ordinary determinant of the product](#statement) | Sign inputs at the stated nonzero real shifts and finite-variance inputs at zero. |
| argument | [Hermitian product linearization](#argument) | Matrix and free normalizations and the inverse corner. |
| support | [Dyson stability](#stability) | Lower and upper regimes, the failed stability at the critical scale, and the log limits. |
| support | [Sign example](#example) | Both conditional laws are deterministic even though both chord signs occur. |
| support | [Nonreal obstruction](#nonreal) | Two-sided equivalence by invertible constant channel matrices. |
| dependency | [Sign-chord floor and log limits](Yin_C_F0356_v2.md#statement) | Positive definite sign difference for the companion at a stable energy. |
| dependency | [Scalar affine log limits](Yin_C_F0353_v2.md#statement) | Each physical factor at zero, without requiring independence between the factors. |

### Decision correlated-product-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:33 |
| status | proved |
| reason | The Hermitian block realization and explicit stable Dyson solution let positive diagonal sign differences control the ordinary determinant of correlated products at the stated real shifts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Precise result](#statement) | The original sign law at the specified nonzero shifts and fixed real finite-variance inputs at zero. |
| argument | [Complete proof](#argument) | The Hermitian block realization and explicit stable Dyson solution let positive diagonal sign differences control the ordinary determinant of correlated products at the stated real shifts. |
| review | [Whole-proof assessment](../audits/reviews/Yin_R_F0364_v3.md#correlated-product-whole-proof) | The original sign law at the specified nonzero shifts and fixed real finite-variance inputs at zero. |
