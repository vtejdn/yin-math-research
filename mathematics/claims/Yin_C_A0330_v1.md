---
author: Yin
---

# Two complementary spectral kernels over one actual scalar inverse

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity, and put \(A_0=\mathbb CH\).
Write \(P(z)=Az+B,\ Q(z)=Cz+D\) for regular complex two-square pencils with \(t\) of infinite order.
Set \(K_\nu=P(t)-\nu s Q(t)\), \(U=s^{-1}P(t)Q(t)^{-1}\), with unnormalized matrix trace.
Suppose two distinct nonzero complex values \(\lambda,\mu\) give positive noninteger nullities adding to one.
Then the two-coordinate polynomial kernels are simultaneously
\[
       \ker K_\lambda=Z e_\lambda U(H),\qquad
       \ker K_\mu=Z e_\mu U(H),\qquad
       Z=\binom{z}{1},\quad e_\lambda+e_\mu=1,\quad e_\lambda e_\mu=e_\mu e_\lambda=0 .
\]
Here \(e_\nu\) are algebraic scalar idempotents, and \(z,e_\lambda,e_\mu\) all belong to the ring obtained from the original group ring by adjoining the inverse of one explicit nonzero group-ring scalar.
For any nonzero pivot in the first column of \(K_\nu\), the image of \(e_\nu\) is the actual affiliated right kernel of that pivot's Schur complement, using the second input coordinate.
The direct sum \(K_\lambda\oplus K_\mu\) has inner rank exactly three over this one-inverse ring.

In particular if a sign character sends \(s\) to \(-1\) and fixes \(t\), any half kernel of \(K_1\) satisfies these conclusions with \(\lambda=1,\mu=-1\).
Writing \(F\) for the sign kernel and \(\alpha={\rm Ad}_{s^{-1}}\), it further forces a scalar \(V\) in the first inverse layer over \(\mathbb CF\) satisfying
\[
         V\alpha(V)=s^2,\qquad e_\pm=(1\pm V s^{-1})/2 .
\]
This \(V\) is a unit of the first layer but \(c V d\notin\mathbb CF\) for every pair of nonzero \(c,d\in\mathbb CF\).
The conditions are necessary on the original group, including at the noncyclic order-twenty marking for either choice of first mark.
They do not assert the existence of a half kernel.

## A rank-one matrix with no polynomial syzygies

Set \(t_1=sts^{-1},\ q=\det Q,\ Q_0=Q(t),\ P_0=P(t)\).
The products below are in their displayed order:
\[
 R=q(t_1)s^2(U-\lambda I)(U-\mu I)Q_0
   =(P\,{\rm adj}\,Q)(t_1)P_0
        -(\lambda+\mu)q(t_1)sP_0+\lambda\mu q(t_1)s^2Q_0 .
\]
This is a matrix over \(A_0\).
The distinct-root interpolation and the dimension hypothesis give it rank exactly one.
The two exterior factors are affiliated units.
Also the kernels of \(K_\nu\) are the two eigenspaces after the same coordinate map \(Q_0\), so they lie in \(\ker R\).
The [three-parameter budget](Yin_C_A0329_v1.md#statement) shows that no third eigenvalue can have positive dimension.

No nonzero column \(w\in A_0^2\) is killed by \(R\).
Indeed \(Q_0 w\) would lie in the direct sum of the two eigenspaces.
The group-ring column \(s^{-1}K_\lambda w=(U-\lambda I)Q_0w\) is in the \(\mu\)-space.
If nonzero it generates a module of dimension one by the scalar hypothesis, impossible in that fractional space.
If zero, the original nonzero column \(w\) is in \(\ker K_\lambda\), likewise impossible.

There is also no nonzero group-ring row \(l\) with \(lR=0\).
The nonzero group-ring row \(v=l q(t_1)s^2\) would lie in the left kernel of \((U-\lambda I)(U-\mu I)\).
The left eigenspace at \(\nu\) has the same dimension as the right one by polar decomposition of the square operator \(U-\nu I\) in finite affiliated modules.
If \(v(U-\lambda I)=0\), the row \(v\) contradicts the fractional dimension there.
Otherwise \(v(U-\lambda I)Q_0=v(s^{-1}P_0-\lambda Q_0)\) is a nonzero polynomial row in the left \(\mu\)-space multiplied on the right by the unit \(Q_0\).
That space again has dimension less than one, which is impossible.
In particular every row and column of \(R\) is nonzero.
Each individual row has rank one and the same right kernel as \(R\) by inclusion and equality of dimensions of the affiliated kernel modules.
Consequently neither entry of any row can be zero, since a zero entry would put a constant coordinate column in \(\ker R\).

## The common kernel coordinate and the inner rank

Take any row \((a,b)\) of \(R\) and let \(Z=(-a^{-1}b,1)^{\mathsf T}\).
Its image equals \(\ker R\) by solving the row equation.
Put \(L=Q_0^{-1}s^{-1}P_0\), similar to \(U\) via \(Q_0\).
The range of \(Z\) is \(\ker((L-\lambda I)(L-\mu I))\) and is \(L\)-invariant.
Its second coordinate is a free parameter, so \(LZ=Z d\) where
\[
              d=(0,1)Q_0^{-1}s^{-1}P_0 Z,\qquad (d-\lambda)(d-\mu)=0 .
\]
Define \(e_\lambda=(d-\mu)/(\lambda-\mu)\) and \(e_\mu=(d-\lambda)/(\mu-\lambda)\).
They give the stated decomposition since \(K_\nu=sQ_0(L-\nu I)\).
If a pivot is chosen in the first column, exchanging output rows if needed and eliminating that nonzero group-ring pivot over \(U(H)\) identifies the kernel of the Schur complement with the set of second coordinates of this same kernel.
That set equals \(e_\nu U(H)\).
In particular its orthogonal projection is the range projection of this idempotent.

Only \(a^{-1}\) and \(q(t)^{-1}\) occur in \(Z,d,e_\nu\).
Both belong to \(A_0[(a q(t))^{-1}]\) inside \(U(H)\) because \(q(t)(a q(t))^{-1}=a^{-1}\) and \((a q(t))^{-1}a=q(t)^{-1}\).
The product \(a q(t)\) is a nonzero group-ring scalar, being a product of affiliated units.
In this ring the column \((Z e_\lambda,Z e_\mu)^{\mathsf T}\), meaning the vertical concatenation of its two columns of length two, is killed by the block diagonal sum.
It can be taken to a coordinate column by invertible elementary operations.
First subtract \(z\) times the second coordinate within each pair from the first, leaving \((0,e_\lambda,0,e_\mu)^{\mathsf T}\).
Add its fourth coordinate to the second to get one, and use that one to clear the fourth.
The block matrix therefore factors through three columns there.
Its regular rank is three, which bounds every inner factorization from below.
For example, if both constant augmentations \(P(1)-\lambda Q(1),P(1)-\mu Q(1)\) are invertible, the original group-ring inner rank of the direct sum is four by augmentation, while in the one-inverse ring it is three.
The original inner rank is not needed for the kernel formulas.

## The scalar norm on the sign kernel

The sign twists \(U\) to \(-U\), so nullity \(1/2\) for \(K_1\) gives the same at \(-1\).
In this case the middle term of the group-ring expression for \(R\) vanishes.
All its entries lie over \(F\), as \(t,t_1,s^2\in F\).
In particular the row \(a,b\) and the column \(Z\) are defined over the first inverse layer in \(U(F)\).
More explicitly \(Z\) uses only \(a^{-1}\).
Move \(s^{-1}\) to the right in the formula for \(d\) to get \(d=V s^{-1}\), with
\[
                    V=(0,1)Q_0^{-1}\alpha(P_0 Z).
\]
Thus the ring \(\mathbb CF[(\alpha(a)q(t))^{-1}]\) already contains \(V\).
The equality \(d^2=1\) yields \(V\alpha(V)=s^2\), which gives \(V^{-1}=\alpha(V)s^{-2}\) in the first inverse layer, the ring generated by all available group-ring scalar inverses at this first step.
In particular the homogeneous rational unit \(V s^{-1}\) is an actual involution over the original sign extension.

If \(c V d_0\in\mathbb CF\) for nonzero \(c,d_0\in\mathbb CF\), multiply \(V s^{-1}-1\) on the left by \(c\) and on the right by \(\alpha^{-1}(d_0)\).
The result would be the group-ring scalar \((c V d_0)s^{-1}-c\,\alpha^{-1}(d_0)\).
Its even component is nonzero and its two terms have distinct sign degrees.
It would thus have rank one, although the exterior multipliers are units and \(V s^{-1}-1\) has rank \(1/2\).
This contradiction proves the assertion on two-sided clearing.

## Assessment history

### Decision two-original-kernels-after-one-scalar-inverse

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | Complementary spectral kernels yield exact Schur idempotents and inner rank three for the direct sum after one specified scalar inverse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complementary spectral kernels yield exact Schur idempotents and inner rank three for the direct sum after one specified scalar inverse. |
| argument | [A rank-one matrix with no polynomial syzygies](#a-rank-one-matrix-with-no-polynomial-syzygies) | A rank-one matrix with no polynomial syzygies. |
| argument | [The common kernel coordinate and the inner rank](#the-common-kernel-coordinate-and-the-inner-rank) | The common kernel coordinate and the inner rank. |
| argument | [The scalar norm on the sign kernel](#the-scalar-norm-on-the-sign-kernel) | The scalar norm on the sign kernel. |
| review | [Two original kernels after one scalar inverse](../audits/reviews/Yin_R_A0227_v1.md#two-original-kernels-after-one-scalar-inverse) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-two-original-kernels-after-one-scalar-inverse)
