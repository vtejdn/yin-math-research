---
author: Yin
---

# Projected column pairs for the unequal-length cubic

The [first physical compression](Yin_L_F0069_v1.md#one-site) for \(P=I+X^2Y+YX\) produces the two columns \(v,Xv\) on one side and \(v,Yv\) on the other, with the same real random vector \(v\).
Here \(X,Y\) denote the real symmetric old blocks, and the scalar shift in \((X+\zeta I)v\) does not change the projected area with \(v\).
We examine the determinant on a remaining two-plane at an even gap.

<a id="energy"></a>
## Coefficient energy on a near-null plane

Let \(Q=\operatorname{span}_{\mathbb C}\{u,t\}\) with \(u,t\) orthonormal, and let \(A=X\) or \(A=Y\).
In this frame the projected determinant is
\[
 q_A(v)=(u^*v)(t^*Av)-(t^*v)(u^*Av)=v^{\mathsf T}M_Av .
\]
Take \(M_A\) transpose-symmetric, so it has rank at most four.
In a real orthonormal eigenbasis of \(A\) with eigenvalues \(a_i\),
\[
 (M_A)_{ij}=\tfrac12(a_j-a_i)\overline{(u_it_j-t_iu_j)} .
\]
In particular its trace vanishes in every real orthonormal frame.
Write \(\mu_h=h^*Ah\) and \(\operatorname{Var}_h(A)=\|(A-\mu_h I)h\|^2\) for a unit vector \(h\).
Expanding the squared minors gives the frame-independent identity
\[
 \begin{aligned}
 2\|M_A\|_{\rm HS}^2
 &=\sum_{i<j}(a_i-a_j)^2|u_it_j-t_iu_j|^2\\
 &=u^*A^2u+t^*A^2t-2(\mu_u\mu_t-|u^*At|^2)\\
 &=\operatorname{Var}_u(A)+\operatorname{Var}_t(A)
   +(\mu_u-\mu_t)^2+2|u^*At|^2 .
 \end{aligned}
\]
Indeed, \(\sum_j|u_it_j-t_iu_j|^2=|u_i|^2+|t_i|^2\), and the term with weights \(a_i a_j\) is the determinant of the compression of \(A\) to \(Q\).

Suppose \(\|X\|,\|Y\|\le K\), \(K>0\), and put \(T=P-wI\) with \(w\notin\mathbb R\).
If a unit \(h\) satisfies \(\|Th\|\le\delta\) or \(\|T^*h\|\le\delta\), then \(|\operatorname{Im}(h^*Ph)|\ge|\operatorname{Im}w|-\delta\).
For \(a=h^*Xh\), replacing \(X^2h,Xh\) by \(a^2h,ah\) in \(\langle X^2h,Yh\rangle+\langle Yh,Xh\rangle\) leaves a real number and changes the sum by at most \(K(2K+1)\|(X-aI)h\|\).
Here \(\|(X^2-a^2I)h\|\le2K\|(X-aI)h\|\).
Alternatively, replacing \(Yh\) by \((h^*Yh)h\) makes the same sum real and changes it by at most \((K^2+K)\sqrt{\operatorname{Var}_h(Y)}\).
Thus if \(Q\) lies in a left or right singular subspace at scale \(\delta<|\operatorname{Im}w|\), the identity gives
\[
 \|M_X\|_{\rm HS}\ge
 \frac{|\operatorname{Im}w|-\delta}{K(2K+1)},\qquad
 \|M_Y\|_{\rm HS}\ge
 \frac{|\operatorname{Im}w|-\delta}{K^2+K}.
\]
These bounds apply to any two-plane remaining inside that subspace after previous columns have been projected out.
They do not distinguish diagonal from off-diagonal coefficients in the coordinates of the independent entries.

<a id="sign-obstruction"></a>
## Sign cancellation on both exact null planes

Fix \(0<r<1\) and any nonreal \(w\).
Start with the two-dimensional real symmetric blocks
\[
 X_1=\begin{pmatrix}r&0\\0&-r\end{pmatrix},\qquad
 Y_1=\begin{pmatrix}
 (\operatorname{Re}w-1)/(r^2+r)&b\\ b&(\operatorname{Re}w-1)/(r^2-r)
 \end{pmatrix},\qquad
 b=\frac{|\operatorname{Im}w|}{r\sqrt{1-r^2}} .
\]
For \(P_1=I+X_1^2Y_1+Y_1X_1\), both diagonal entries equal \(\operatorname{Re}w\); the off-diagonal entries \((r^2-r)b,(r^2+r)b\) have product \(-(\operatorname{Im}w)^2\).
Its two distinct eigenvalues are \(w,\bar w\).
Put two identical copies of the pair on the diagonal, optionally adjoining zero \(X,Y\) blocks on which \(P=I\).
The left and right null planes of \(T\) each have an orthonormal basis \((h,0),(0,h)\) in the two copies, taking the appropriate unit left or right mode \(h\) of \(P_1-wI\) and zero entries in the filler.
For \(A=A_1\oplus A_1\) on the two copies, the linear forms \(h^*,h^*A_1\) on each copy are the same.
Consequently the corresponding \(q_A(v)\) is a constant times \(v_1v_4-v_2v_3\), by multiplicativity of the two-by-two determinant.
The constant is nonzero for \(A=X,Y\) on either plane by the energy bound at \(\delta=0\).

Now make the same real orthogonal change of physical coordinates for both old matrices, so the old vector coordinates in terms of the independent input coordinates \(s\) are
\[
 v_1=(s_1+s_4)/\sqrt2,\quad v_4=(s_1-s_4)/\sqrt2,\qquad
 v_2=(s_2+s_3)/\sqrt2,\quad v_3=(s_2-s_3)/\sqrt2 .
\]
Each projected determinant is now a constant times \((s_1^2-s_4^2-s_2^2+s_3^2)/2\).
It vanishes for every sign vector with coordinates of the same modulus, including every realization of an independent normalized Rademacher column.
The old blocks are bounded independently of the filler dimension, the null spaces are those of the actual cubic on these blocks, and the gap above the two zero singular values is positive for fixed \(w,r\).
This excludes a deterministic inference from total coefficient energy to a sign small-ball bound.
These deliberately chosen old blocks do not supply an event of appreciable probability for independent Wigner minors; the direct projected-volume estimate on typical old inputs remains open here.
The [one-direction exterior compression](../claims/Yin_C_F0362_v2.md#exterior) and its [fresh \(X\)-row restoration](../claims/Yin_C_F0362_v2.md#restoration) bypass this projected pair.
