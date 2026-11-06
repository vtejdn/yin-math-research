---
author: Yin
---

<a id="three-channel-middle-frobenius-obstruction"></a>
# A deterministic obstruction to the three-channel middle trace route

This is ordinary exploration for Yin, retained on 2026-11-06T04:29 UTC after direct authoring checks and a collaborating agent's algebra check, not an independent proof review or an adopted Claim.
It concerns the actual retained-row kernel in the [three-channel path model](../drafts/Yin_D_F0010.md#three-channel-propagation-probe).
The [two-channel kernel-graph proof](../claims/Yin_C_F0187_v11.md#kernel-graph-trace) gives its fresh-row covariance bound using a positive definite two-channel slope covariance.
For the present three-channel model, that substitution is unavailable because the covariance below has rank at most two.
The construction here disproves the proposed deterministic replacement under a common Frobenius upper bound, even under a fixed operator-norm bound.
It is not a counterexample to the original independent Wigner laws, either Task, or a probabilistic middle singular-value theorem.

## The exact trace target

Let \(C,D\) be real symmetric \(n\)-by-\(n\) matrices, and put
\[
 T:=\operatorname{diag}(0,1,\sqrt2),\qquad
 K:=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},\qquad
 M:=I_3\otimes C+T\otimes D+K\otimes I_n.
\]
Let \(J\subset[n]\) have size \(m\), put \(U:=[n]\setminus J\), and let \(R_U\) restrict all three channels to physical positions in \(U\).
Define the actual retained-row kernel and its real orthogonal projection by
\[
 \mathcal K:=\ker(R_UM),\qquad P:=P_{\mathcal K}.
\]
There are \(3(n-m)\) retained rows, so \(\dim\mathcal K\ge3m\).
For a real unit auxiliary vector \(a\), the conditional projected energy of the two original fresh rows is
\[
 H_a:=\operatorname{Tr}P\bigl[(aa^T+(Ta)(Ta)^T)\otimes I_n\bigr].
\]
The tested deterministic assertion would bound this below by \(c n(m/n)^s\), uniformly over unit \(a\), from \(\|C\|_F^2+\|D\|_F^2\le C_0n\), with fixed \(c>0\) and finite \(s\).
Replacing \(n\) by the original parent size \(N=n+1\) changes no conclusion below.

## Three nearby scalar null directions

Write
\[
 M(c,d):=\operatorname{diag}(c,c+d,c+\sqrt2d)+K,
 \qquad
 p(c,d):=\det M(c,d)=c(c+d)(c+\sqrt2d)-2c-\sqrt2d.
\]
For all sufficiently small real \(c\), the following explicit odd function solves \(p(c,d(c))=0\):
\[
 d(c):=
 \frac{2c(c^2-2)}{
 \sqrt2-(1+\sqrt2)c^2+
 \sqrt{2+(6\sqrt2-4)c^2+(3-2\sqrt2)c^4}}.
\]
The denominator is positive near zero, and direct expansion gives \(d(c)=-\sqrt2c+O(c^3)\).
The formula follows from the quadratic equation
\[
 \sqrt2c\,d^2+\bigl((1+\sqrt2)c^2-\sqrt2\bigr)d+c^3-2c=0
\]
by rationalizing the root that tends to zero.
Define
\[
 b(c):=\bigl(1,-c,c(c+d(c))-1\bigr)^T.
\]
The first two coordinates of \(M(c,d(c))b(c)\) vanish identically, and the third is \(p(c,d(c))\), so \(b(c)\) is a nonzero nullvector.
The minor in rows \(1,2\) and columns \(2,3\) of \(M(c,d)\) has determinant one, so each matrix on this zero branch has rank exactly two.

Fix a sufficiently small \(\varepsilon>0\), and put \(h:=\varepsilon(\varepsilon+d(\varepsilon))\).
Oddness of \(d\) gives
\[
 b(0)=(1,0,-1)^T,\qquad
 b(\varepsilon)=(1,-\varepsilon,h-1)^T,\qquad
 b(-\varepsilon)=(1,\varepsilon,h-1)^T.
\]
Their column determinant is
\[
 \det[b(0),b(\varepsilon),b(-\varepsilon)]
 =-2\varepsilon h
 =-2\varepsilon^2(\varepsilon+d(\varepsilon))\ne0.
\]
Indeed \(\varepsilon+d(\varepsilon)=(1-\sqrt2)\varepsilon+O(\varepsilon^3)\).
Thus these three null directions are linearly independent, although all converge to the line through \((1,0,-1)^T\).

## Physical mixing and the actual retained kernel

First take \(n=3m\), and split the physical space into \(m\) mutually orthogonal triples.
On each triple use the real orthogonal matrix
\[
 Q:=\begin{pmatrix}
 1/\sqrt3&1/\sqrt3&1/\sqrt3\\
 1/\sqrt2&-1/\sqrt2&0\\
 1/\sqrt6&1/\sqrt6&-2/\sqrt6
 \end{pmatrix},
\]
and define the corresponding blocks of the two inputs by
\[
 C_\varepsilon:=Q\operatorname{diag}(0,\varepsilon,-\varepsilon)Q^T,
 \qquad
 D_\varepsilon:=Q\operatorname{diag}(0,d(\varepsilon),-d(\varepsilon))Q^T.
\]
Let \(C,D\) be the direct sums of these blocks, and let \(J\) contain the first physical coordinate in each triple.
A simultaneous physical permutation can make \(J\) a terminal set if that row-deletion convention is desired.

Conjugation by the physical matrix \(Q\) makes the restriction of \(M\) to each triple the direct sum of \(M(0,0)\), \(M(\varepsilon,d(\varepsilon))\), and \(M(-\varepsilon,-d(\varepsilon))\).
Consequently \(\operatorname{rank}M=6m\) and \(\dim\ker M=3m\).
If \(q_0,q_+,q_-\) are the three columns of \(Q\), an orthonormal nullbasis on one physical triple is
\[
 \frac{b(0)}{\|b(0)\|}\otimes q_0,\qquad
 \frac{b(\varepsilon)}{\|b(\varepsilon)\|}\otimes q_+,\qquad
 \frac{b(-\varepsilon)}{\|b(-\varepsilon)\|}\otimes q_-.
\]
Restriction of these vectors to the deleted physical coordinate has matrix
\[
 \frac1{\sqrt3}
 \left[\frac{b(0)}{\|b(0)\|},
       \frac{b(\varepsilon)}{\|b(\varepsilon)\|},
       \frac{b(-\varepsilon)}{\|b(-\varepsilon)\|}\right],
\]
which is invertible by the preceding determinant calculation.
Thus restriction \(\ker M\to\mathbb R^3\otimes\mathbb R^J\) is an isomorphism, and no nonzero vector in \(\ker M\) is supported on \(U\).

For a vector \(y\) indexed by the retained rows, symmetry of \(M\) gives
\[
 (R_UM)^Ty=MR_U^Ty.
\]
If this vanishes, \(R_U^Ty\) is a full nullvector supported on \(U\), hence is zero.
Therefore \(R_UM\) has full row rank \(6m\), and its kernel has dimension \(9m-6m=3m\).
Since \(\ker M\subseteq\ker(R_UM)\), equality of dimensions proves the exact identity
\[
 \mathcal K=\ker(R_UM)=\ker M.
\]
The projection in the trace target is therefore the projection onto the explicitly constructed full nullspace, not a replacement spectral or artificial kernel projection.

## Vanishing observed trace and the precise failure

Take \(a=e_2\), for which \(Ta=e_2\) and \(aa^T+(Ta)(Ta)^T=2e_2e_2^T\).
The nullbasis above gives exactly
\[
 H_{e_2}
 =2m\left(0+\frac{\varepsilon^2}{\|b(\varepsilon)\|^2}
              +\frac{\varepsilon^2}{\|b(-\varepsilon)\|^2}\right)
 =\frac{4m\varepsilon^2}{\|b(\varepsilon)\|^2}
 \sim2m\varepsilon^2.
\]
At the same time,
\[
 \|C\|_F^2+\|D\|_F^2
 =2m\bigl(\varepsilon^2+d(\varepsilon)^2\bigr)
 \sim6m\varepsilon^2,
 \qquad
 \|C\|+\|D\|=O(\varepsilon).
\]
For \(m/n=1/3\), the proposed lower bound \(cn(m/n)^s\) is a fixed positive multiple of \(m\), while the displayed trace divided by \(m\) tends to zero.
Hence no positive bound of that form, with any fixed exponent, follows uniformly from the Frobenius upper guard or from adding a fixed operator-norm upper guard.

For any \(n>3m\), one may append \(n-3m\) undeleted one-dimensional physical blocks with \(C=1,D=0\).
Their auxiliary matrix is \(I_3+K\), whose eigenvalues \(1,1+\sqrt2,1-\sqrt2\) are nonzero.
They add no retained kernel, preserve \(\dim\mathcal K=3m\) and the same trace formula, and add exactly \(n-3m\) to the squared input Frobenius sum.
Thus the construction also allows smaller deletion proportions, including \(m/n\to0\), by choosing \(\varepsilon\) small enough for each pair \((n,m)\).
Taking \(n=4m\) also makes the Frobenius sum comparable to \(n\), so a matching Frobenius lower guard would not repair the failure.

## What the random geometric inputs do and do not supply

The constructed inputs commute, are highly dependent, and are not samples from the original independent Wigner model with the fixed variance-one entry laws.
Every \(b(0)\otimes q_0\) is an exact zero mode with zero middle channel, so the construction violates the [fixed-deletion approximate-mode and combined-Gram input in C187v20](../claims/Yin_C_F0187_v20.md#fixed-deletion-gram-extension), inherited from [C187v19](../claims/Yin_C_F0187_v19.md#statement).
Those random inputs therefore exclude this particular obstruction on their good events.
This distinction prevents turning the deterministic failure into a claim that the desired random middle estimate is false.

Their proved deletion range is bounded independently of \(N\), and their whole-subspace Gram conclusion applies to bounded-energy spectral windows of the relevant full principal minor.
An arbitrary vector of \(\ker(R_UM)\) only satisfies \(Mz\in\mathbb R^3\otimes\mathbb R^J\); its full residual norm need not be small.
The actual retained-row kernel is neither the low spectral space of \(M\) nor the kernel of the principal minor \(M[U,U]\).
Thus one cannot apply the C187v19/C187v20 mode statement directly to every vector of this kernel, or obtain an assertion for \(m\to\infty\) principal deletions by substituting \(m\) for their fixed deletion bound.
The existing result on the undeleted or singly deleted full minor remains available at its exact scope, but a further argument is needed to transfer it to the retained-kernel trace uniformly in \(a\).

If such a trace bound \(H_a\ge cn(m/n)^s\) is established using additional random geometry, the [weighted truncation and auxiliary-net mechanism](../claims/Yin_C_F0187_v11.md#finite-variance-kernel-row) can be adapted at that actual energy, followed by the [block negative-second-moment interface](../claims/Yin_C_F0187_v11.md#finite-variance-middle-indices).
The present exploration supplies no such transfer, uniform probability estimate, three-channel middle profile or logarithmic conclusion.
It locates the failed premise precisely: Frobenius control and the deterministic path equations alone cannot provide the required all-direction retained-kernel covariance bound.
