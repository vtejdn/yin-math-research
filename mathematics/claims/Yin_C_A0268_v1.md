---
author: Yin
---

# Two spectral atoms or small positive polynomial nullities inside the original group

## Statement

Let \(G\) be discrete, \(U=\mathcal U(G)\), \(N=\mathcal N(G)\), and \(D=\bigcup_j D_j(G)\) the actual scalar division closure of \(\mathbb CG\) in \(U\).
A unit below has an inverse in \(U\); for elements of \(D\) this is equivalent to invertibility in \(D\).
Use the regular trace and unnormalized matrix dimensions.
The following are equivalent in this fixed group.

1. \(D\) is a local ring.
2. Every bounded positive contraction in \(D\) has at most one of zero and one as spectral atoms.
3. Every Hermitian group-ring pencil \(B-\lambda E_{11}\) with affiliated-unit complementary principal block is singular at at most one real parameter.

Suppose \(a\in D_j(G)\) is nonzero and singular and its center-valued initial rank \(c\) satisfies \(kc\ge1\) for some positive integer \(k\).
Fix a polynomial Schur presentation of \(a\) with square affiliated-unit pivot of size \(s\).
Then at least one of the following occurs in the original group.

* There is a positive contraction in \(D_{j+1}(G)\) with atoms at zero and one of the same strictly positive mass.
* One family of positive \((ks+1)\)-square group-ring matrices has strictly positive nullities with infimum zero.
  Only a column of \(k\) group-ring polynomials varies, with all terms of the original presentation fixed.

The first outcome holds whenever finitely many right multiples \(ag\) with \(g\in G\) have zero joint kernel, since \(\ker(ag)=g^{-1}\ker a\).
In the other case all trials in the second family have positive nullity.
In a factor take \(k=\lceil1/\operatorname{rk} a\rceil\), and the same choice works whenever \(c\) is scalar.
For a two-by-two first Schur scalar one can take \(s=1\).

In particular, for each individual torsion-free group in which every nonzero member of \(D\) has center-valued rank bounded below by a positive scalar, strong Atiyah is equivalent to locality of \(D\) together with a positive gap above zero in the nullities of positive group-ring matrices at each fixed size.
The gap may depend on the size, and the group need not be enlarged.
This applies to the factor and [scalar center-valued rank cases](Yin_C_A0260_v1.md#statement).

## Locality and the two atoms

The ring \(D\) is star-closed by taking adjoints in its finite inverse expressions, and is directly finite since \(U\) is directly finite.
If \(D\) is not local it has distinct maximal right ideals.
Their sum contains \(1\), so \(x+y=1\) with both \(x,y\in D\) nonunits.
Conversely in a directly finite local ring the nonunits are exactly the unique maximal right ideal, so no such pair exists.
Indeed a nonunit generates a proper right ideal by direct finiteness.
Every affiliated nonunit in this finite tracial setting has strictly positive nullity.

More generally take any \(x,y\in D_j\) with nonzero kernels meeting trivially.
Then the column \(J=(x,y)^{\mathsf t}\) is injective over \(U\) and \(J^*J\) is an affiliated unit.
The orthogonal projection \(R=J(J^*J)^{-1}J^*\) is bounded with entries in \(D_{j+1}\), and the positive contraction \(b=R_{11}\) has exact atom masses
\[
                 \tau(1_{\{0\}}(b))=\nu(x),\qquad
                 \tau(1_{\{1\}}(b))=\nu(y).
\]
Projection of the affiliated image of \(J\) on its first coordinate has rank \(\operatorname{rk}x\), also the rank of the Gram compression \(b\).
The points \((u,0)\) in this image are precisely the images of \(\ker y\) under the injective \(J\), and identify with \(\ker(1-b)\). [Endpoint compression](Yin_C_A0246_v1.md#constructing-two-endpoint-atoms-in-one-inverse-layer)
In particular \(x+y=1\) supplies disjoint kernels and produces both atoms.
If \(b,1-b\) have atoms at zero they are nonunits summing to the identity, which proves the first equivalence.

A Hermitian pencil with affiliated-unit complementary block has an affiliated selfadjoint scalar Schur complement \(T-\lambda\) with \(T\in D\).
Indeed the inverse of its complementary block belongs to a matrix ring over a finite inverse layer by [positive Gram inversion](Yin_C_A0239_v1.md#inner-rank-and-the-unit-class), using the Gram matrix for an arbitrary invertible block.
Two distinct real singular parameters give two nonunits \(T-\lambda,T-\mu\) whose suitable scalar multiples sum to \(1\).
Conversely the [fixed Hermitian polynomial realization](Yin_C_A0246_v1.md#linearization-with-one-varying-diagonal-entry) of \(b-\lambda\) gives both singular parameters whenever \(b,1-b\) are nonunits.
This proves the pencil characterization of locality.

## Finite intersections of translated kernels

Write \(p=p_{\ker a}\), and for \(g\in G\) put \(p_g=g^{-1}pg\).
Suppose some finite family has zero intersection and choose such a family minimal by inclusion.
It has at least two elements, and by a common conjugation it may be arranged to contain the identity.
Remove one element \(u\) other than the identity.
The remaining intersection \(p'\) is nonzero, lies below \(p\), and satisfies \(p'\wedge p_u=0\).
Thus \(p'\wedge u^{-1}p'u=0\).
The positive element \(x=\sum_{g\ \mathrm{remaining}} g^{-1}a^*ag\) belongs to \(D_j\) and has kernel projection \(p'\).
Apply the previous construction to \(x,u^{-1}xu\) to obtain both atoms of mass \(\tau(p')\).
This finite intersection argument uses no lower bound on \(c\).

Otherwise every finite intersection is nonzero.
For arbitrary group-ring entries \(v_1,\ldots,v_k\) the column \(V=(av_1,\ldots,av_k)^{\mathsf t}\) has positive nullity: the intersection of \(p_g\) over the union of their finite supports lies in its kernel.
For the empty union the whole domain is in the kernel.
Nevertheless the supremum of its rank over these columns is one.
Indeed the diagonal projection with \(k\) copies of \(1-p\) has center-valued dimension \(kc\ge1\).
Projection comparison in the matrix amplification supplies an isometric column from one full coordinate into this diagonal projection.
Approximate its entries in \(L^2\) by group-ring elements and compress to that projection.
The dimension lost to the kernel of each trial is at most its squared \(L^2\) error from the isometry.
Multiplying the entries by \(a\) then preserves the rank of the compressed column, since \(a\) has initial support \(1-p\). [Original-group comparison and approximation](Yin_C_A0239_v1.md#the-exact-original-infimum)

If \(a=d_0-CA^{-1}B_0\) is the fixed polynomial presentation, write \(D_k(T)=I_k\otimes T\) just in the next display for a block diagonal of \(k\) copies and put \(v=(v_1,\ldots,v_k)^{\mathsf t}\).
The group-ring matrix
\[
     Z(v)=\begin{pmatrix}
       D_k(A)&D_k(B_0)v\\ D_k(C)&D_k(d_0)v
     \end{pmatrix}
\]
has \(ks+1\) columns and Schur remainder \(V\).
Thus \(\nu(Z(v)^*Z(v))=\nu(V)>0\), with infimum zero over these same fixed-size tests.
For a group-ring scalar itself a presentation with \(s=0\) just gives its column of polynomial products.

If locality and all the indicated gaps hold, neither outcome is available for a nonzero singular scalar satisfying the lower bound on its center-valued rank.
When the bound holds for each nonzero scalar the division closure is therefore a skew field, giving strong Atiyah for a torsion-free group by the [division closure criterion](../tasks/Yin_T_A0001_v1.md#starting-references).
Conversely strong Atiyah makes the division closure a skew field and all positive polynomial nullities positive integers.

## Assessment history

### Decision locality-and-fixed-size-positive-nullities

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Independent review verified locality, the original-group construction, the fixed test size and both directions of the gap criterion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The three local-ring conditions, equal-atom alternative and fixed-group gap criterion. |
| argument | [Locality and the two atoms](#locality-and-the-two-atoms) | Distinct maximal right ideals, exact Gram endpoint masses and Hermitian linearization. |
| argument | [Finite intersections of translated kernels](#finite-intersections-of-translated-kernels) | Minimal support family, positive trial kernels and approximation with fixed pivot size. |
| review | [Locality and fixed-size positive nullities](../audits/reviews/Yin_R_A0206_v1.md#locality-and-fixed-size-positive-nullities) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-locality-and-fixed-size-positive-nullities)
