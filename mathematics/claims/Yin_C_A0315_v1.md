---
author: Yin
---

# Perfect two-generator groups with arbitrarily long transfer windows

## Statement

For each \(n\ge7\) congruent to one modulo six there is a residually finite torsion-free perfect marked group \(H_n=\langle s,t\rangle\) with integral regular ranks for all complex group-ring matrices.
It has \(n-2\) distinct right cosets represented by \(1,s,\ldots,s^{n-3}\) of the subgroup
\[
                    \langle s^jts^{-j}:0\le j\le n-4\rangle .
\]
In particular no nontrivial scalar character exists on these markings.
For every \(\epsilon>0\), at each fixed \(H_n\) there is a finite marked word neighborhood in which every two-generator torsion-free scalar-injective group has every noninteger regular nullity of a complex two-square four-site matrix at most \(\epsilon\).
The neighborhood allows groups with other permutation images.

There is also a quantitative test for groups that do have the displayed permutation image below.
Suppose a two-marked group \(G\) maps to the permutations
\[
                    x=(0\ 1\ \cdots\ n-1),\qquad y=(0\ 2\ 1)
\]
on the marks \(s,t\) respectively, and \(t\) has infinite order in \(G\).
For all complex square pencils \(P,Q\) of size \(h\) with \(Q\) invertible over \(\mathbb C(z)\), the original regular nullity satisfies
\[
                        \dim_G\ker(P(t)-sQ(t))\le h/(n-2).
\]
This estimate uses unnormalized matrix trace.

## A perfect subgroup of the triangle lift

Write \(q=n-2\) and take the full lift \(\Gamma(n,3,q)\) of the orientation-preserving hyperbolic triangle group \(\Sigma(n,3,q)\).
Indeed \(1/n+1/3+1/q<1\).
Use the [lifted triangle presentation](../audits/literature/Mil75/Yin_U001.md#lifted-triangle-presentation), in which \(X^n=Y^3=Z^q=XYZ=c\) and \(c\) generates the infinite cyclic central covering kernel.
This group acts faithfully by increasing lifts of boundary-circle transformations on the real line, so it is torsion-free. [Lifted circle action](Yin_C_A0194_v1.md#an-explicit-perfect-marking)

Set
\[
 d=2nq-3n-3q,\qquad l=(5n+1)/6,\qquad m=(7n-13)/6,\qquad
 a=(ld-1)/n,\qquad b=(d-1)/3 .
\]
Here \(d>0\), \(d\equiv6\bmod n\), and \(d\equiv1\bmod3\), so these are integers.
Put \(s=Xc^a,\ t=Yc^b,\ u=c^d\) and define \(H_n\) to be their two-generator subgroup \(\langle s,t\rangle\).
It projects onto \(\Sigma(n,3,q)\), since the first two vertex rotations generate that triangle group.
One has
\[
                 s^n=u^l,\qquad t^3=u,\qquad (st)^q=u^m .
\]
The last equality follows from \(XY=cZ^{-1}\) and \(q(1+a+b)-1=dm\) on substituting \(q=n-2\).
Writing \(S,T\) for the classes of \(s,t\) in the abelianization gives \(nS-3lT=0\) and \(qS+(q-3m)T=0\).
Their determinant \(n(q-3m)+3lq=-1\) forces both generators to vanish.
For the first member \(n=7\), these are \(s=Xc^{29},\ t=Yc^{11}\), with \(u=c^{34}\).
The relations read \(7S=18T,\ 5S=13T\).

## The finite permutation test

The product \(xy\), applying \(y\) first, fixes 1 and 2 and cycles \(0,3,4,\ldots,n-1\) in that order.
The three orders of \(x,y,(xy)^{-1}\) are \(n,3,q\), respectively.
Their product is the identity, so they define a representation of \(\Sigma(n,3,q)\), giving the specified marks on \(H_n\).
They generate \(A_n\).
Indeed the conjugates of \(y\) give the inverses of all the consecutive three-cycles.
If \(d_i=(i\ i+1)\), the latter cycles are \(d_i d_{i+1}\).
Their subgroup contains every \(d_i d_j\), by multiplying the consecutive pairs or taking inverses.
Pairs of adjacent transpositions generate the even permutations in this sense, and both \(x\) and \(y\) are even.

Every \(x^j yx^{-j}\) with \(0\le j\le n-4\) moves only \(j,j+1,j+2\).
The subgroup they generate fixes \(n-1\), while every \(x^k,\ 1\le k\le n-3\), moves it.
Thus none of the powers \(s^k,\ 1\le k\le n-3\), belongs to the displayed subgroup of conjugates in any marked group mapping to \(x,y\).
This gives the \(n-2\) distinct right cosets.
For \(G\) as in the statement, \(Q(t)\) is an affiliated unit by Haar spectral evaluation at the infinite-order translation.
Right multiplication by its inverse reduces the rectangle to its graph comparison.
Applying the [transfer window](Yin_C_A0183_v1.md#statement) with \(n-2\) positions gives the asserted bound.

## Residual finiteness, integrality and neighboring markings

Let \(\pi:H_n\to\Sigma(n,3,q)\) be the projection.
Its kernel is an infinite cyclic central group, since it is a subgroup of the covering kernel containing \(u=t^3\ne1\).
Take the inverse image \(H_0\) of a torsion-free normal finite-index surface subgroup of \(\Sigma(n,3,q)\).
Such a subgroup exists by Selberg's lemma applied to the characteristic-zero linear triangle group, taking the normal core; its free cocompact action on the hyperbolic plane gives a closed orientable surface of genus at least two. [Hyperbolic surface subgroup argument](../ledger/Yin_L_A0082_v1.md#the-surface-subgroup-and-its-central-extension)

For residual finiteness, elements with nonidentity image under \(\pi\) are detected by a finite image of the finitely generated linear triangle group.
Indeed take the matrix entries of generators and their inverses in a faithful linear representation, invert one nonzero entry of the desired matrix minus the identity and reduce at a maximal ideal of this finitely generated ring.
The residue field is finite. [Finite-field specialization](Yin_C_A0284_v1.md#preserving-a-noncommuting-pair-on-specialization)
To separate elements of the central kernel, fix its generator \(z\).
Choose lifts \(a_i,b_i\) of the standard surface generators.
The group \(H_0\) has a presentation with \(z\) central and single further relation \(\prod_i[a_i,b_i]=z^e\) for some integer \(e\).
Indeed the surface relator lifts to a power of \(z\), and quotienting the resulting presented group by \(z\) gives the surface presentation.
Its resulting surjection onto \(H_0\) can have kernel only in the subgroup generated by \(z\), on which it is injective since this element has infinite order.
For any nonzero \(j\) take an integer \(N>|j|\), \(N\ge2\).
In the finite group of upper unitriangular three-square matrices over \(\mathbb Z/N\), send \(z\) to \(I+E_{13}\), the first two generators \(a_1,b_1\) to \(I+eE_{12},I+E_{23}\), and the remaining generators to \(I\).
The commutator of the first pair is \(I+eE_{13}\), the required \(e\)-th power.
This separates \(z^j\).
The kernel of that finite map of \(H_0\) has finite index also in \(H_n\); its normal core in \(H_n\) still excludes \(z^j\).
This proves residual finiteness.

For integrality use the [surface-kernel argument](../ledger/Yin_L_A0082_v1.md#the-surface-subgroup-and-its-central-extension) with the central cyclic kernel computed above.
The kernel of a surjection from the surface group to \(\mathbb Z\) is free, since it is the group of the noncompact infinite cyclic covering surface.
Its inverse image in \(H_0\) is the direct product of this free group and the central cyclic kernel, by lifting a free basis.
To recover \(H_0\) and then \(H_n\), the further quotients are infinite cyclic and finite.
These extensions place \(H_n\) in Linnell's class \(\mathcal C\), so torsion-freeness gives all-matrix integrality over \(\mathbb C H_n\). [Linnell's theorem](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems)
In particular nonzero group-ring scalars are regularly injective and the supremum of fractional four-site nullities, with zero included, equals zero.
The proved windows contain the three positions required for [upper semicontinuity](Yin_C_A0307_v2.md#statement).
At each \(H_n\), failure of the claimed \(\epsilon\)-neighborhood would give a sequence of torsion-free scalar-injective groups agreeing on larger and larger word balls with fractional nullities exceeding \(\epsilon\), contrary to that theorem.

## Assessment history

### Decision perfect-markings-with-long-windows

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | The marked triangle lifts are perfect and residually finite, with the stated long windows and small fractional nullities on neighboring markings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The marked triangle lifts are perfect and residually finite, with the stated long windows and small fractional nullities on neighboring markings. |
| argument | [A perfect subgroup of the triangle lift](#a-perfect-subgroup-of-the-triangle-lift) | A perfect subgroup of the triangle lift. |
| argument | [The finite permutation test](#the-finite-permutation-test) | The finite permutation test. |
| argument | [Residual finiteness, integrality and neighboring markings](#residual-finiteness-integrality-and-neighboring-markings) | Residual finiteness, integrality and neighboring markings. |
| review | [Perfect markings with long windows](../audits/reviews/Yin_R_A0222_v1.md#perfect-markings-with-long-windows) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-perfect-markings-with-long-windows)
