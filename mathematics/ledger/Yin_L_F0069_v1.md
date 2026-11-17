---
author: Yin
---

# The first physical compression for the unequal-length cubic word test

<a id="compression"></a>
## Deleting physical sites before restoring the fresh color

Use the [unequal-length cyclic test](../claims/Yin_C_F0359_v1.md#example) with two real symmetric matrices \(X,Y\) and
\(P=I+X^2Y+YX\).
Take \(k\) sites \(I\), their \(n\)-site complement \(J\), \(X_0=X_{JJ}\), \(Y_0=Y_{JJ}\), \(Z=X_{II}\), \(V=X_{JI}\), and \(U=Y_{JI}\).
Write \(T=I+X_0^2Y_0+Y_0X_0-wI\) and \(W=X_0V+VZ\).
Direct block multiplication gives
\[
 (P-wI)_{JJ}=T+VV^{\mathsf T}Y_0+WU^{\mathsf T}+UV^{\mathsf T}.
\]
Thus compression to \(W^\perp\) on the left and \(V^\perp\) on the right removes the two contributions of the fresh \(Y\)-columns.
It retains \(VV^{\mathsf T}Y_0\), which need not be positive or symmetric.

Consider the square bordered matrix
\[
 \mathcal B(V)=
 \begin{pmatrix}
     T&X_0 V& V\\
     V^{\mathsf T}&0&0\\
     V^{\mathsf T}Y_0& Z&-I_k
 \end{pmatrix}.
\]
Eliminating the lower identity pivot gives the remaining blocks \(T+VV^{\mathsf T}Y_0,W,V^{\mathsf T},0\).
When \(V,W\) have full column rank, the absolute determinant of \(\mathcal B(V)\), divided by
\(\det(V^{\mathsf T}V)^{1/2}\det(W^{\mathsf T}W)^{1/2}\), is exactly that of the exterior compression in orthonormal frames.
Indeed complete the two orthonormalized column spaces by their orthogonal complements and expand the bordered determinant on its last \(k\) rows and columns.
The displayed matrix and its Schur elimination are defined even without the rank assumption.
For original independent Wigner inputs, condition on \(X_0,Y_0,Z\).
The columns of \(V\) are then independent, without rotating them to diagonalize \(Z\).

<a id="one-site"></a>
## A site pair and its four rational kernels

For one deleted site, write \(v=V,\ \zeta=Z\), and assume \(T\) invertible with \(R=T^{-1}\).
The bordered determinant divided by \(\det T\), up to an overall sign, is
\[
 (1+v^{\mathsf T}Y_0Rv)\,v^{\mathsf T}R(X_0+\zeta I)v
  -(v^{\mathsf T}Rv)\,v^{\mathsf T}Y_0R(X_0+\zeta I)v .
\]
This follows from the two-by-two Schur complement, or from the adjugate formula for the single rank update.
Its homogeneous quartic term uses the kernels \(R,RX_0,Y_0R,Y_0RX_0\) through their transpose-symmetric parts; the two quartic terms involving \(\zeta\) cancel.
At commuting scalars \(X_0=x,Y_0=y\) these specialize to \(1,x,y,xy\) divided by \(1+(x^2+x)y-w\).
For distinct spectral nodes, clearing all denominators and reducing at one node excludes every nontrivial relation modulo scalars: the other factors become nonzero constants, and a numerator of total degree at most two cannot be a nonzero multiple of the cubic denominator.
The test verifies the scalar specialization needed for a four-panel argument; it does not furnish a lower bound on the first bordered determinant.

The difficulty at an adaptive gap of rank \(r\) is that a whole site brings the *same* random vector twice on each side, as \((X_0v,v)\) and \((v,Y_0v)\).
The existing scalar-column overlap estimates do not give the determinant of the two newly projected columns at a step.
An odd gap also leaves one unmatched channel in a sequence of whole-site additions.
A first quantitative test is the two-column projected volume at an even gap for these actual old matrices.
This precedes the comparison of the full scalar determinant with its retained principal-minor product.

<a id="covariance"></a>
## Why a deterministic covariance argument for the cubic is insufficient

The corner pencil with rows \((1-w,X,0,Y),(0,-1,X,0),(Y,0,-1,0),(X,0,0,-1)\) has scalar Schur complement \(P-w\).
A left null vector has auxiliary components \(Xu,X^2u,Yu\) at physical component \(u\).
The two raw border combinations, with channel scalars written after conjugation, are \(a_1u+a_2Xu+a_0Yu\) and \(a_3u+a_0X^2u\).
They can vanish identically for bounded Hermitian inputs at any prescribed nonreal \(w\).
Take \(0<r<1\), \(X=\operatorname{diag}(r,-r)\), and a real unit \(u\) whose squared coordinates are \((1+r)/2,(1-r)/2\).
Then \(u^*Xu=r^2\) and \(q=(X-r^2I)u\) is orthogonal to \(u\).
Set \(\beta=(\bar w-1)/(r^2(1-r^2))\) and \(Y=\beta q u^*+\bar\beta u q^*\).
This Hermitian matrix satisfies \(Yu=\beta q\) and
\[
    (I+YX^2+XY)u=(1+\beta r^2(1-r^2))u=\bar w u.
\]
The direction \((1,\beta r^2,-\beta,-r^2)\) annihilates both raw combinations.
Real symmetric witnesses follow by the usual realification of the matrices: the embedding \(v\mapsto(v,-iv)\) intertwines each complex matrix with its realification acting on the complexification of twice the physical dimension.
This verifies a failure of a deterministic border bound; the original independent input law imposes additional restrictions on the small spectral subspaces of \(X\) and their images under \(Y\).
