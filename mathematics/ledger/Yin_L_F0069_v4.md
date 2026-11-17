---
author: Yin
---

# A deterministic obstruction to the quartic companion's right border estimate

<a id="scope"></a>
## The proposed extension and its exact limitation

The finding of 2026-11-18 concerns the extension of the [cubic directional estimate](../claims/Yin_C_F0362_v1.md#direction) to \(P_3=1+x^3y+yx\) under the [finite-variance Task](../tasks/Yin_T_F0012_v3.md#contract).
The [partial exterior and commuting-residue calculation](Yin_L_F0069_v3.md#partial) remain available at every fixed degree.
The obstruction here concerns an additional deterministic assertion that would have supplied the right directional estimate for a five-channel affine companion.
Real symmetric inputs and a nonreal eigenvalue do not by themselves exclude failure of that estimate, even for bounded matrices whose relevant vector occupies arbitrarily many spectral values of \(X\).
These deterministic examples are not independent Wigner inputs and are not counterexamples to Brown convergence.

<a id="direction"></a>
## The right directional test

Use the affine companion
\[
 L(w)=\begin{pmatrix}
 1-w&X&0&0&Y\\
 0&-I&X&0&0\\
 0&0&-I&X&0\\
 Y&0&0&-I&0\\
 X&0&0&0&-I
 \end{pmatrix}.
\]
Its scalar Schur complement is \(P_3(X,Y)-wI\).
At an exact scalar null vector \(v\), its right null vector is
\[
 r=(v,X^2Yv,XYv,Yv,Xv).
\]
For an auxiliary direction \(a=(a_0,a_1,a_2,a_3,a_4)\), the two color coefficients obtained by applying this direction to the companion's coefficient matrices and this graph are
\[
 a_0X^2Yv+a_1XYv+a_2Yv+a_4v,
 \qquad a_0Xv+a_3v.
 \tag{1}
\]
Conjugating every component of \(a\) does not change the existence of a unit direction where both vanish.
When \(a_0=a_3=0\), this asks whether a relation
\[
 (a_1X+a_2I)Yv+a_4v=0
 \tag{2}
\]
can coexist with a nonreal eigenvalue of \(X^3Y+YX\).
The constructions below answer yes and rule out deducing localization in finitely many thin \(X\)-spectral windows from these two equations alone.

<a id="counterexample"></a>
## Bounded examples with arbitrarily many spectral values

Let \(A\) be a positive diagonal \(m\)-by-\(m\) matrix and let \(u\) be a real unit vector such that \(u,Au\) are linearly independent.
Fix a nonzero real \(c\), put
\[
 d=c(u^{\mathsf T}A^2u-1),\qquad
 V=[u,Au],\qquad
 W=[cA^{-1}u,cA^2u-du],\qquad G=V^{\mathsf T}V.
\]
The two off-diagonal entries of \(V^{\mathsf T}W\) both equal \(c\):
\[
 u^{\mathsf T}(cA^2u-du)=c,
 \qquad (Au)^{\mathsf T}(cA^{-1}u)=c.
\]
Thus \(V^{\mathsf T}W\) is symmetric, and the real symmetric matrix
\[
 B=WG^{-1}V^{\mathsf T}+VG^{-1}W^{\mathsf T}
       -VG^{-1}(V^{\mathsf T}W)G^{-1}V^{\mathsf T}
 \tag{3}
\]
satisfies \(BV=W\).
Indeed the last two terms in \(BV\) cancel because \(W^{\mathsf T}V=V^{\mathsf T}W\).
Consequently
\[
 Bu=cA^{-1}u,\qquad BAu=cA^2u-du.
\]
Set
\[
 X=\begin{pmatrix}A&0\\0&-A\end{pmatrix},\qquad
 Y=\begin{pmatrix}0&B\\B&0\end{pmatrix},\qquad
 v=\binom{u}{iu}.
\]
Direct multiplication gives
\[
 XYv=icv,
 \qquad
 (X^3Y+YX)v
 =\binom{i(cA^2u-BAu)}{-cA^2u+BAu}
 =idv.
 \tag{4}
\]
When \(d\ne0\), \(w=1+id\) is nonreal.
The nonzero direction \(a=(0,1,0,0,-ic)\), normalized to unit length, makes both expressions in (1) vanish exactly.
The graph \(r\) can likewise be normalized without changing this vanishing.

If the spectrum of \(A\) lies in a fixed interval \([a_-,a_+]\subset(0,\infty)\) and
\[
 u^{\mathsf T}A^2u-(u^{\mathsf T}Au)^2\ge\sigma^2>0,
\]
then \(G^{-1},V,W\), and therefore \(B,X,Y\), have norms bounded by constants depending only on \(a_-,a_+,\sigma,|c|\).
This follows from \(\det G\ge\sigma^2\), the uniform bound on \(\operatorname{tr}G\), and (3).
One may also add any real symmetric matrix \(C\) with \(CV=0\) to \(B\), preserving (4).
Thus the construction is not restricted to a low-rank \(B\).

To keep the same nonreal shift while spreading the vector, choose
\(0<r_0<r_1<\min(\mu,1-\mu)\) with \(0<\mu<1\).
For \(m=2k\), choose distinct equally spaced \(r_j\) in \([r_0,r_1]\) and take the diagonal entries of \(A\) in pairs
\[
 \sqrt{\mu+r_j},\quad\sqrt{\mu-r_j},
 \qquad 1\le j\le k,
\]
with \(u=m^{-1/2}(1,\ldots,1)^{\mathsf T}\).
Then \(u^{\mathsf T}A^2u=\mu\), so \(d=c(\mu-1)\ne0\) is fixed.
The two intervals of diagonal values are separated, each carries half the squared mass of \(u\), and their endpoints stay in a fixed compact subset of \((0,1)\).
Their separation gives a uniform positive lower bound for the variance in the preceding display, so the norm bound is uniform in \(k\).
Each of the four corresponding intervals in the spectral measure of \(X\) at \(v/\sqrt2\) is an image of an equally spaced grid under a map with derivative bounded above and away from zero.
An interval of radius \(\delta\) therefore captures at most \(C\delta+C/m\) of that spectral measure.
Any fixed number of windows with radii tending to zero captures mass tending to zero, although (1) vanishes exactly at the same fixed nonreal shift.

<a id="odd-change"></a>
## What the odd power changes, and what it does not

For \(Z=X^3+X\) and \(H=X^3-X\), the exact identity
\[
 X^3Y+YX=\tfrac12(ZY+YZ+[H,Y])
\]
separates an anticommutator from a commutator.
The scalar function \(x\mapsto z=x^3+x\) is strictly increasing, and \(H=g(Z)\) under functional calculus with
\[
 g'(z)=\frac{3x^2-1}{3x^2+1},\qquad |g'(z)|\le1.
\]
This gives scalar Lipschitz information but supplies no positive symmetrizer or real-spectrum conclusion; (4) is already an obstruction to such an inference.

A diagonal symmetrizer depending only on \(X\) also fails in general.
At \(X=\operatorname{diag}(1,2,3)\), an invertible diagonal \(D=\operatorname{diag}(h_1,h_2,h_3)\) satisfying
\(D(X^3Y+YX)=(X^3Y+YX)^{\mathsf T}D\) for every real symmetric \(Y\) would require
\[
 h_i(x_i^3+x_j)=h_j(x_j^3+x_i).
\]
Multiplying around the three indices would give
\[
 (1^3+2)(2^3+3)(3^3+1)
 =(2^3+1)(3^3+2)(1^3+3).
\]
The two sides equal \(924\) and \(1044\), respectively.
This excludes that universal invertible diagonal metric, including an indefinite one, but says nothing about metrics depending on \(Y\) or a larger auxiliary representation.

<a id="next-test"></a>
## A different test for the next representation

The example defeats the deterministic right directional floor for this companion and the proposed finite-window deduction.
It does not exclude a probability estimate using the actual independent Wigner laws, a bound that discards a controlled bad subspace, or a different companion.
The [fixed-dimensional restoration theorem](../claims/Yin_C_F0363_v3.md#statement) still requires its initial comparison and actual projected-kernel hypotheses.

An exploratory alternative is to expose both colors on two selected physical sites before taking a directional rank estimate.
The proposed change is to retain mixed terms in the two-site Schur determinant that the one-site linear directional test discards.
A first discriminating investigation is an exact expansion on the family (3)--(4): after eliminating the unchanged companion blocks, test whether a mixed coefficient involving fresh \(X\) and fresh \(Y\) coordinates survives in the direction annihilated by (1).
If every relevant mixed coefficient still vanishes, this particular grouping adds no information against the obstruction and should not be pursued on the strength of the same directional argument.
If a coefficient survives, its physical coefficient span and conditional covariance must next be tested on actual independent panels before invoking any restoration estimate.
No such two-site coefficient or probability estimate is established here.
