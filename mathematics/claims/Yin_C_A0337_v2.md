---
author: Yin
---

# A sharp norm for nonunitary exceptional pencils and a finite return

## Statement

Use a normalized [exceptional prototype and its trace parameter](Yin_C_A0337_v1.md#statement), with \(d={\rm Tr}(M(0)M(\infty))\) and \(q(z)=z^2-s_0z+2,\ s_0=\pm\sqrt5\).
For every real \(1/2<d<2\), the optimal constant similarity norm is attained and equals
\[
       \min_{S\in {\rm GL}_2(\mathbb C)}\ \max_{|z|=1}\|S M(z)S^{-1}\|
                   =\sqrt{5-2d}+\sqrt{4-2d}.
\]
Thus, for \(55/32\le d<2\), a half-dimensional kernel forces a positive-word return even though these pencils have no constant invariant Hermitian form.
The same return holds for \(d>5/2\) satisfying
\[
                     512(d-1/2)(d-5/2)\le 27(4+2d).
\]
For example it holds for \(5/2<d\le27/10\).
In all these cases the [annular moment theorem](Yin_C_A0338_v1.md#statement) supplies an identity
\[
          g^{-1}h^{i_1}\cdots g^{-1}h^{i_{2j}}=1,\qquad
               1\le j\le5,\quad i_1,\ldots,i_{2j}\ge0,
\]
where the indices admit a common finite cutoff computable from the coefficients.
More quantitatively, absence of all returns with these numbers of factors implies regular nullity strictly below \(49/100\).
The estimate for \(d>5/2\) is a sufficient norm bound.

## The optimal similarity below two

Write \(N=qM=N_0+zN_1+z^2N_2\), \(X=N_0+N_2,\ Y=i(N_0-N_2),\ Z=N_1\) as in the [Gram calculation](Yin_C_A0337_v1.md#from-the-boundary-equation-to-three-traceless-matrices).
For \(1/2<d<2\) the \(X,Z\) block of the trace form is positive definite and \(Y\) is orthogonal to it of square \(2d-4<0\).
Make a real orthonormal basis of \({\rm span}_{\mathbb R}(X,Z)\).
The two resulting traceless matrices are anticommuting involutions.
A constant similarity makes them the Hermitian Pauli matrices \(T_3={\rm diag}(1,-1)\) and \(T_1=e_{12}+e_{21}\): first diagonalize the first involution and then normalize the off-diagonal entries of the second.
A traceless matrix anticommuting with both is a multiple of the remaining Hermitian Pauli matrix \(T_2=-i e_{12}+i e_{21}\).
Thus \(X,Z\) are Hermitian and \(Y=\pm i\sqrt{4-2d}\,T_2\) is skew-Hermitian in this same basis.

For \(z=e^{i\theta}\), multiply \(M(z)\) by the unimodular scalar \(q(z)/(z|q(z)|)\), giving the involution
\[
               V(\theta)=\frac{X\cos\theta+Z-Y\sin\theta}{|q(z)|}.
\]
Its square is \(I\) since \(N(z)^2=p(z)q(z)I\) and \(p(z)=z^2\overline{q(z)}\).
One has \(V(-\theta)=V(\theta)^*\) in this basis.
If the numerator of \(V\) is written as the sum of its Hermitian part \(H\) and skew-Hermitian part \(J\), then \(HJ=-JH\) and \(J^2=-b^2 I\) with \(b=\sqrt{4-2d}\,|\sin\theta|\).
Therefore \(H^2=(|q(z)|^2+b^2)I\).
After diagonalizing \(H\) unitarily its eigenvalues are opposite, and \(J\) is skew off-diagonal of off-diagonal modulus \(b\).
The two singular values of \(H+J\) are \(\sqrt{|q(z)|^2+b^2}\pm b\), by the two diagonal entries and the modulus of the off-diagonal entry of \((H+J)^*(H+J)\).
This includes \(b=0\).

In particular \(\|V(\theta)\|=\sqrt{1+c^2}+c\), where \(c=b/|q(z)|\).
Since
\[
                |q(e^{i\theta})|^2=(3\cos\theta-s_0)^2+\sin^2\theta ,
\]
the maximum of \(|\sin\theta|/|q(z)|\) equals one, attained at \(\cos\theta=s_0/3\).
This gives the stated norm in our basis.
For every other similarity, submultiplicativity and the spectral radius of the product at \(\theta,-\theta\) bound the squared supremum norm below by
\[
               r\big(V(\theta)V(-\theta)\big)
                           =r\big(V(\theta)V(\theta)^*\big)=\|V(\theta)\|^2 .
\]
The product spectral radius is similarity invariant, so the bound is optimal.
The maximum is at most two precisely when \(\sqrt{4-2d}\le3/4\), equivalently \(d\ge55/32\).

## An upper bound above five halves

For \(d>5/2\), the orthogonal matrices \(X,Y\) have positive squares, so put their normalized versions in two Hermitian Pauli directions by the same involution argument.
The component of \(Z\) along \(X\) is a real multiple of \(X\), and its component along \(Y\) vanishes.
Its orthogonal remainder is a purely imaginary multiple of the third Hermitian Pauli matrix, of squared modulus
\[
              b^2=\frac{4(d-1/2)(d-5/2)}{4+2d}
\]
by the determinant of the \(X,Z\) block and the square of \(X\).
Thus the numerator of \(V(\theta)\) again has anticommuting Hermitian and skew-Hermitian parts, now with the same \(b\) for every angle.
The singular value calculation gives an upper bound \(\sqrt{1+c^2}+c\) with \(c=b/\min_{|z|=1}|q(z)|\).
The displayed formula for the denominator, as a quadratic in \(\cos\theta\), has its minimum square \(3/8\) at \(3s_0/8\).
Hence \(c\le3/4\) is exactly the stated sufficient inequality.
It holds up to \(27/10\) on this side, since the ratio \((d-1/2)(d-5/2)/(4+2d)\) increases there.

For both parameter ranges the constructed constant similarity commutes with each group translation.
The norm of the resulting \(U=g^{-1}M(h)\) is at most two.
The same is true of its inverse, since each two-square boundary value has determinant of modulus one and hence equally large norms for itself and its inverse.
Their squared spectral radii are at most four.
The hypotheses and conclusions of the annular return theorem, including its [finite exponent cutoff](Yin_C_A0338_v1.md#a-finite-search-in-the-original-word-ball), therefore apply.

## Assessment history

### Decision optimal-norm-below-two-and-bounded-positive-returns

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:25 |
| status | proved |
| reason | The paired boundary values give the exact optimal norm below two and a sufficient bound above five halves. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The paired boundary values give the exact optimal norm below two and a sufficient bound above five halves. |
| argument | [The optimal similarity below two](#the-optimal-similarity-below-two) | The optimal similarity below two. |
| argument | [An upper bound above five halves](#an-upper-bound-above-five-halves) | An upper bound above five halves. |
| dependency | [Earlier result, version 1](Yin_C_A0337_v1.md#statement) | The real Gram signatures distinguish positive, indefinite, and absent invariant Hermitian forms and all admissible parameters have regular realizations. |
| review | [Constant forms for the prototype](../audits/reviews/Yin_R_A0233_v1.md#constant-forms-for-the-prototype) | Independent inspection of the preceding version. |
| review | [Optimal norm below two and bounded positive returns](../audits/reviews/Yin_R_A0233_v1.md#optimal-norm-below-two-and-bounded-positive-returns) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-optimal-norm-below-two-and-bounded-positive-returns)
