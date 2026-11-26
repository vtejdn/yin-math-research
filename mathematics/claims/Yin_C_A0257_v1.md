---
author: Yin
---

# Measuring a Schur kernel by column shears in its original group

## Statement

Let \(A=\left(\begin{smallmatrix}a&b_0\\c&d_0\end{smallmatrix}\right)\) be over \(\mathbb CG\), with \(a\) an affiliated unit.
Write \(z=a^{-1}b_0\), \(S=d_0-cz\), \(p=p_{\ker S}\), \(q=1-p\), \(\delta=\tau(p)\) and \(c_0=Z(p)\), where \(Z\) is the normalized center-valued trace.
For \(v\in\mathbb CG\) shear the second column by adding the first column multiplied on the right by \(v\), giving \(A_v\).
Its Schur scalar is still \(S\).
For the two input coordinates of \(L=A_v\) in the [coordinate comparison](Yin_C_A0255_v1.md#statement), the joint rank increment is \(h=\delta\) and the sum increment is
\[
                b=\delta+r(v),\qquad r(v)=\operatorname{rk}_G(q(z+v)p).
\]
For each \(r(v)>0\), the original scalar star-regular closure contains two-square algebraic matrix units on a projection of trace exactly \(2r(v)\).
The same quantity is determined by an ordinary positive three-square group-ring matrix of nullity \(\delta-r(v)\).

The largest attainable increments satisfy
\[
 \sup_{v\in\mathbb CG}r(v)=\tau(\min(c_0,1-c_0)),\qquad
 \sup_{g\in G,\,\lambda\in\mathbb C} r(\lambda g)\ge\tau(c_0(1-c_0)).
\]
For any fixed list of \(m\ge2\) distinct integer values of \(\lambda\), the latter lower bound multiplied by \(1-1/m\) still holds.
In particular, the kernel projection \(p\) is central precisely when no shear by \(v=0\) or by a single group element \(v=g\) gives a strict two-coordinate inequality \(b>h\).
These statements apply to a nonclosed image of \(a\) or \(S\).
In a factor the first supremum is \(\min(\delta,1-\delta)\); attaining it is a separate condition.
For \(\delta=1/2\), any original shear attaining \(r(v)=1/2\) already yields a unital \(M_2(\mathbb C)\) in \(D_2(G)\).

## Kernel images and the positive polynomial test

The sheared columns are \((a,c)^{\mathsf t},(b_0+av,d_0+cv)^{\mathsf t}\), so the two terms \(cv\) cancel in the Schur complement.
Over the right affiliated module its kernel consists of the pairs \((-(z+v)\xi,\xi)\) for \(\xi\in pU\).
The joint coordinate map thus has rank \(\delta\); the sum of the separate coordinate images is \(pU+(z+v)pU\).
Projection to \(qU\) identifies its quotient by \(pU\) with \(q(z+v)pU\), giving \(b=\delta+r(v)\).
Let \(x=q(z+v)p\).
Its nonzero initial and final projections lie respectively below \(p,q\), are algebraically equivalent by \(x,x^\dagger\), and together with these two elements give the asserted matrix units on their sum of trace \(2r(v)\).

For a bounded polynomial realization take the four-by-three matrix
\[
        H_v=\begin{pmatrix}
        b_0+av&0&-a\\ d_0+cv&0&-c\\
        0&a&b_0\\0&c&d_0
        \end{pmatrix}.
\]
The top pair imposes \(A_v(-\eta,\xi)^{\mathsf t}=0\) and the bottom pair imposes \(A(\zeta,\eta)^{\mathsf t}=0\) on the three input coordinates \((\xi,\zeta,\eta)\).
The equations choose \(\eta=(z+v)\xi,\ \zeta=-z\eta\) and require \(\xi,\eta\in pU\).
This identifies \(\ker H_v\) with the kernel of \(x\) on \(pU\), of dimension \(\delta-r(v)\).
Taking \(H_v^*H_v\) preserves that kernel.

If \(\delta=r(v)=1/2\), let \(y=S^*S\), \(t=z+v\), and \(V=(y,yt)^{\mathsf t}\).
Its kernel is zero by the preceding restricted-kernel calculation, so \(u=V^*V\) is an affiliated unit in the first layer.
The rectangular inverse \(Y=u^{-1}V^*\) belongs to the second layer and \(YV=1\).
The projection \(VY\) is dominated by \(qI_2\) and has the same unnormalized trace one, so \(VY=qI_2\).
Its diagonal entries put \(q,p\) in \(D_2(G)\).
The elements \(Y(qE_{ij})V\), where \(E_{ij}\) are the scalar two-square matrix units, give unital matrix units by these two identities.
This uses the [single Gram inverse](Yin_C_A0125_v2.md#algebraic-matrix-units-from-a-single-inverse) with the affiliated first-layer multiplier \(t\); no boundedness of \(z\) is required.

## Polynomial multipliers and a finite list of coefficients

The center-valued image rank of \(q(z+v)p\) is bounded by \(\min(c_0,1-c_0)\) by comparison of its initial and final supports.
For any fixed bounded \(V\in\mathcal N(G)\), consider the pencil \(qzp+\lambda qVp\).
Right multiplication by the affiliated unit \((1+(qzp)^*(qzp))^{-1/2}\) makes both coefficients bounded and preserves every rank.
The [one-variable rank inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives a common generic maximal rank \(R\) and, on any \(m\) distinct complex parameters, a sum of ranks at least \((m-1)R\).
Also \(R\ge\operatorname{rk}(qVp)\), either by applying the same generic bound to the reversed pencil at zero, or by lower semicontinuity as the parameter tends to infinity after scalar rescaling.
In particular for each polynomial \(V\) one can absorb both the fixed \(z\) and one scalar multiple of \(V\) without losing the latter rank at a generic parameter.

By comparison in the finite von Neumann algebra one can take a partial isometry from a subprojection of \(p\) into \(q\) with center-valued rank exactly \(\min(c_0,1-c_0)\), using the two central regions on either side of \(c_0=1/2\).
Approximate this partial isometry by group-ring elements in \(L^2\) and compress by \(q,p\).
The ranks approach its rank from below in the supremum: restricting to its initial projection, the dimension of the new kernel there is at most the squared \(L^2\) error, since the limit is isometric on that projection. [Projection comparison and approximation](Yin_C_A0239_v1.md#the-exact-original-infimum)
Applying the pencil estimate to each polynomial approximant proves the first supremum.

For \(V=g\), the contraction \(qgp\) has rank at least its squared \(L^2\)-norm \(\tau(qgpg^*)\).
The closed \(L^2\)-convex hull of the conjugates of \(p\) contains \(c_0\) by [central conjugation averaging](Yin_C_A0125_v2.md#reduction-of-the-defect-with-one-more-group-element).
Hence \(\sup_g\operatorname{rk}(qgp)\ge\tau(qc_0)=\tau(c_0(1-c_0))\).
The generic and finite-list estimates above prove the two single-element bounds.
If \(p\) is noncentral, \(c_0\) is not a projection: otherwise \(\|p-c_0\|_2^2=\tau(c_0-c_0^2)=0\).
Thus the bound for \(\lambda\in\{0,1\}\) is strictly positive.
Conversely central \(p\) commutes with every affiliated coefficient, giving \(r(v)=0\) identically.

## Assessment history

### Decision shearing-an-actual-schur-input

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:07 |
| status | proved |
| reason | Whole-proof review verified the actual polynomial matrix, original corner, rank bounds and inverse depth. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact ranks, polynomial and monomial suprema, the finite coefficient list and the depth-two conclusion. |
| argument | [Kernel images and the positive polynomial test](#kernel-images-and-the-positive-polynomial-test) | The graph of the original kernel, signs in the three-coordinate test and the single extra inverse. |
| argument | [Polynomial multipliers and a finite list of coefficients](#polynomial-multipliers-and-a-finite-list-of-coefficients) | Right regularization, generic rank, polynomial approximation and central averaging. |
| review | [Shearing an actual Schur input](../audits/reviews/Yin_R_A0203_v1.md#shearing-an-actual-schur-input) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-shearing-an-actual-schur-input)
