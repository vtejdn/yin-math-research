---
author: Yin
---
# Layer peeling and finite coefficient certificates for the triple commutator

## Statement

Let \(G\) be a group, let \(D\in\mathbb C[G]\), and write
\[
 \partial_XY=[X,Y],\qquad
 H_D=[D,D^*],\qquad
 E_D=\partial_D^3(D^*)=\partial_D^2(H_D).
\]
The adjoint is the usual group-algebra adjoint.
The following tests concern the actual finite group supports and their actual product equalities.
They strengthen the [extremal-layer test in v1](Yin_C_A0095_v1.md#testing-the-extreme-layers-of-one-element).
They do not prove that every scalar triple-commutator solution in a torsion-free group is normal.
The [fixed-group domain equivalence](Yin_C_A0095_v1.md#statement) remains quantified over all finite elements.

### The next homogeneous component

Let \(\chi:\langle\operatorname{supp}D\rangle\to\mathbb R\) be a group character, and suppose \(D\) has at least three distinct homogeneous degrees.
Let \(h\) be the highest degree, \(m\) the next highest, \(l\) the lowest, and \(l_1\) the next lowest.
Write
\[
 P=D_h=cu,\qquad Q=D_l,\qquad R=D_m,\qquad T=D_{l_1},
 \qquad c\ne0,
\]
where the top layer is a single group element, and put
\[
                       a=h-m,\qquad b=l_1-l.
\]
The middle layers \(R,T\) can coincide.
If \(E_D=0\), then \(u\) commutes with \(Q,Q^*\).
After using that conclusion, the component of \(E_D\) at degree
\[
                         3h-l-\min(a,b)
\]
is respectively
\[
\begin{cases}
 \partial_P^3(T^*),& b<a,\\
 \partial_P^2([R,Q^*]),& a<b,\\
 \partial_P^2\bigl([P,T^*]+[R,Q^*]\bigr),& a=b.
\end{cases}                                                     \tag{1}
\]
Each displayed expression must vanish.
In the first case \(u\) commutes with \(T\).
In the second case \(u\) commutes with \([R,Q^*]\).
In the third case it commutes with \([P,T^*]+[R,Q^*]\).
The latter two conclusions do not in general assert that \(u\) commutes with \(R\).
All collisions between terms at the displayed degree are included in (1); group-word collisions within those expressions are retained by computing them in \(\mathbb C[G]\).

### A separated singleton top layer

Allow any number of lower layers, including just one.
Write \(D=cu+W\), where \(W\ne0\) and \(\chi(u)=h\) is strictly larger than all degrees of \(W\).
Let \(m,l\) be the highest and lowest degrees of \(W\).
If
\[
                         h-m>m-l                              \tag{2}
\]
and \(E_D=0\), then \(u\) commutes with every homogeneous part of \(W\), and hence with \(W,W^*\).
Consequently
\[
                   H_D=H_W,\qquad E_D=E_W.                    \tag{3}
\]
Thus a nonnormal solution yields a nonnormal solution after deleting its singleton highest layer.
This is the precise peeling conclusion under (2); it does not assert that \(W\) is normal.
For two layers, \(m=l\), so this includes the earlier two-layer test.

### Three layers with reciprocal extrema

Suppose instead that
\[
                  D=cu+R+du^{-1},\qquad
                  \chi(u)=h>0,\qquad \deg_\chi R=0,
                  \qquad c,d\ne0,\quad R\ne0.                 \tag{4}
\]
If \(E_D=0\), then
\[
                         H_D=H_R,\qquad E_R=0.                \tag{5}
\]
Hence a nonnormal solution yields a nonnormal solution supported on the middle layer alone.
No commutation of \(u\) with \(R\), and no comparison of \(|c|\) and \(|d|\), is assumed or concluded.

In a fixed torsion-free group, a nonnormal solution of minimal support to the criterion in v1 therefore has neither form (2) nor form (4).
The peeling proofs themselves do not require torsion-freeness.

### A finite certificate without characters

Fix distinct labels \(S=\{g_1,\ldots,g_n\}\subseteq G\).
Introduce independent commuting variables \(z_1,\ldots,z_n,w_1,\ldots,w_n\), and form
\[
 D_z=\sum_i z_i g_i,\qquad D_w^\dagger=\sum_i w_i g_i^{-1},
\]
\[
 H(z,w)=[D_z,D_w^\dagger]=\sum_h H_h(z,w)h,\qquad
 E(z,w)=\partial_{D_z}^3(D_w^\dagger)=\sum_g E_g(z,w)g.
                                                                    \tag{6}
\]
Thus \(H_h\) has bidegree \((1,1)\) and \(E_g\) has bidegree \((3,1)\), with integer coefficients.
For each nonzero coefficient polynomial \(H_h\), suppose some two indices \(r(h),s(h)\), allowing equality, satisfy
\[
 z_{r(h)}z_{s(h)}H_h
             \ \in\ \operatorname{span}_{\mathbb Q}\{E_g:g\in G\}.
                                                                    \tag{7}
\]
Then every \(D=\sum_i c_i g_i\) with all \(c_i\ne0\) and \(E_D=0\) is normal.
The hypothesis is a finite rational row-space test in the monomial basis
\[
                z_1^{\alpha_1}\cdots z_n^{\alpha_n}w_j,
                 \qquad \sum_i\alpha_i=3.
                                                                    \tag{8}
\]
It uses only the exact products occurring in (6), so it remains available when every real group character is constant on the support.
Failure of (7) is inconclusive; the test decides existence of this linear certificate, not the full coefficient problem.
Exact support is essential for dividing by the multiplier in (7).

## Unitary powers and the leading component

For any group element \(u\), conjugation \(T(X)=uXu^{-1}\) is a unitary permutation of the group basis of \(\ell^2(G)\).
For every positive integer \(k\),
\[
                    \partial_u^k(X)=(T-I)^k(X)u^k.
                                                                    \tag{9}
\]
The spectral theorem for the unitary \(T\) gives
\[
             \ker(T-I)^k=\ker(T-I).
                                                                    \tag{10}
\]
Consequently \(\partial_u^k(X)=0\) implies \([u,X]=0\), for finite group-ring \(X\) in particular.
This is a Hilbert-space statement about a unitary permutation, not a domain assumption about \(\mathbb C[G]\).

The highest possible degree in \(E_D\) is \(3h-l\).
Only the three top unstarred layers and the bottom starred layer attain it, giving
\[
                         \partial_P^3(Q^*).
                                                                    \tag{11}
\]
Equations (9)–(10) yield \([u,Q^*]=0\), and taking adjoints gives \([u,Q]=0\).

## The next degree and the gap condition

In a term of \(E_D\), replacing one unstarred top layer by the next highest layer decreases its degree by at least \(a\).
Replacing the bottom starred layer by the next lowest layer decreases the degree by at least \(b\).
There is no positive decrease smaller than \(\min(a,b)\).
At exactly that decrease there can only be one of these replacements, or the two different possibilities when \(a=b\); no two replacements can contribute at this degree.

The starred replacement gives \(\partial_P^3(T^*)\).
The unstarred replacement gives the sum of three orders,
\[
 \bigl(\partial_P^2\partial_R+
       \partial_P\partial_R\partial_P+
       \partial_R\partial_P^2\bigr)(Q^*).
\]
Since \(\partial_P(Q^*)=0\), the latter two orders vanish and the first is \(\partial_P^2([R,Q^*])\).
Adding both contributions in the equal-gap case gives (1).
Applying (9)–(10) proves its three stated consequences.

To prove the full conclusion under (2), consider each lower degree \(\alpha\in[l,m]\) that occurs in \(W\).
Any term with at least one unstarred factor from \(W\) has degree at most
\[
                            2h+m-l.
\]
But (2) gives, simultaneously for every such \(\alpha\),
\[
                 3h-\alpha\ \ge 3h-m\ >2h+m-l.
\]
Therefore the entire component at degree \(3h-\alpha\) consists only of
\[
                         \partial_P^3(D_\alpha^*).
\]
The distinct values of \(\alpha\) give distinct degrees.
This establishes all the lower-layer commutations independently, without assuming that an induction avoids later homogeneous collisions.
Taking adjoints gives commutation with the unstarred parts too.
The element \(cu\) is normal and commutes with \(W,W^*\).
Expanding the two commutators now gives (3).

The next-degree conclusion alone is weaker than this gap theorem.
For example, in the torsion-free group \(F(u,w)\times\langle v\rangle\), take
\[
 D=u+w+v,\qquad \chi(u)=3,\quad\chi(w)=2,\quad\chi(v)=0,
\]
where \(v\) is central.
The leading relation \([u,v]=0\) and the next expression
\[
                         \partial_u^2([w,v^{-1}])=0
\]
both hold, although \([u,w]\ne0\).
The full triple commutator is nonzero: the central \(v\) drops out, and the highest component for \(u+w\) is \(\partial_u^3(w^{-1})\).
Its four group words \(u^3w^{-1},u^2w^{-1}u,uw^{-1}u^2,w^{-1}u^3\) are distinct free-group normal forms, with coefficients \(1,-3,3,-1\).
This is a diagnostic of the incomplete next-degree test, not a nonnormal solution of \(E_D=0\).

## Reciprocal extrema

Under (4), the degree \(2h\) and \(-2h\) components of \(H_D\) vanish because \(u\) and \(u^{-1}\) commute.
The degree \(h\) component is
\[
 X=[cu,R^*]+[R,\bar d u]
   =[u,cR^*-\bar d R].
                                                                    \tag{12}
\]
Its degree \(-h\) component is \(X^*\), since \(H_D\) is self-adjoint.
Its degree zero component is \(H_R\), because the two individual extremal monomials are normal.
The degree \(3h\) component of \(\partial_D^2(H_D)\) is
\[
 c^2\partial_u^2(X)
       =c^2\partial_u^3(cR^*-\bar d R).
                                                                    \tag{13}
\]
Its vanishing and (9)–(10) give \(X=0\).
Thus \(H_D=H_R\) and this self-commutator has degree zero.

The degree \(2h\) component of \(\partial_D^2(H_R)\) is \(c^2\partial_u^2(H_R)\), so \(u\) commutes with \(H_R\).
Therefore \(u^{-1}\) also commutes with it.
The degree-zero component of the same expression is
\[
 \partial_R^2(H_R)
   +\partial_{cu}\partial_{du^{-1}}(H_R)
   +\partial_{du^{-1}}\partial_{cu}(H_R).
                                                                    \tag{14}
\]
The last two terms vanish.
The first is \(E_R\), proving (5).
Other homogeneous components impose further conditions on a solution, but none is discarded in deriving this necessary reduction.
If \(D\) is nonnormal, equality of the self-commutators makes \(R\) nonnormal, so deleting both extremal labels strictly decreases support.

## Constructing and using the character-free certificate

Expand the triple commutator as
\[
 E=D_z^3D_w^\dagger-3D_z^2D_w^\dagger D_z
            +3D_zD_w^\dagger D_z^2-D_w^\dagger D_z^3.
                                                                    \tag{15}
\]
For each ordered quadruple of labels, use the actual group product to place its term in the correct output row.
Combine all terms with the same commutative coefficient monomial in the basis (8), including the different orders of the three unstarred indices.
This produces the integer row vectors of the \(E_g\).
Likewise collect the two products in \(H\) to obtain every \(H_h\).
It is not sufficient to count syntactically different words: equal group elements and equal coefficient monomials must both be combined.

Membership in (7) is equivalent to a finite rational identity
\[
                z_{r(h)}z_{s(h)}H_h=\sum_g q_{hg}E_g,
                \qquad q_{hg}\in\mathbb Q.
                                                                    \tag{16}
\]
These identities can be found or rejected by exact rational Gaussian elimination.
All the equality information required to construct the rows is finite.
No algorithm for deciding arbitrary group words is assumed; those identifications must be supplied or verified for the actual group.

The variables \(w_i\) were independent while constructing these polynomial identities.
For a genuine adjoint, specialize \(z_i=c_i\) and \(w_i=\bar c_i\).
Then the right side of (16) vanishes if \(E_D=0\).
The multiplier \(c_{r(h)}c_{s(h)}\) is nonzero because every specified support coefficient is nonzero, so \(H_h(c,\bar c)=0\).
This holds for every output coefficient and proves normality.
No inference treats the actual coefficients and their conjugates as independent after specialization.

As an inexpensive separate obstruction, if one collected row \(E_g\) is a single nonzero monomial in the variables \(z,w\), then no full-support solution of \(E_D=0\) exists on that support.
Such a row cannot vanish after the same specialization.
This test and (7) are coefficient identities for one fixed support, unlike the projective component pruning and Newton boundary arguments in [C33](Yin_C_A0033_v1.md#statement).
They require no varying coefficient curve or real character.

## A finite-group diagnostic with no real characters

The tests must not eliminate genuine nonnormal solutions in groups with torsion.
Let \(G=S_3\), \(a=(12)\), \(b=(23)\), and \(D=ca+db\).
The relations \(a^2=b^2=1\) and \(aba=bab\) give
\[
 H_D=(c\bar d-d\bar c)(ab-ba),
\]
\[
 E_D=4(c^2+d^2-cd)(c\bar d-d\bar c)(ab-ba).
                                                                    \tag{17}
\]
For example, \([a,ab-ba]=2(b-aba)\) and \([b,ab-ba]=2(aba-a)\); applying the second commutator gives the factor in (17).
Taking \(c=e^{\pi i/3}\) and \(d=1\) makes the quadratic factor zero and the self-commutator nonzero.
This support therefore fails the sufficient row-space certificate (7), as it must: its nonzero \(E\)-rows span the polynomial \((z_1^2+z_2^2-z_1z_2)(z_1w_2-z_2w_1)\), whereas none of the products \(z_rz_s(z_1w_2-z_2w_1)\) is a scalar multiple of it.
The subgroup has no nonconstant real characters.
The calculation checks the scope of the character-free test; it provides no torsion-free counterexample.

## Assessment history

### Decision layer-and-coefficient-tests

| Field | Value |
| --- | --- |
| date | 2026-11-21T04:36 |
| status | proved |
| reason | The separate reviewer verified the layer calculations and the sufficient finite coefficient test, including both diagnostics. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The next degree, the two support reductions and the rational certificate on exact support. |
| argument | [Proof](#unitary-powers-and-the-leading-component) | Unitary conjugation and leading degree, with subsequent proofs of the gap, reciprocal extrema and finite test. |
| review | [Whole finding](../audits/reviews/Yin_R_A0131_v2.md#whole-finding) | Complete independent inspection at the mathematical and source scope stated in the finding. |

## Current assessment

[Selected decision](#decision-layer-and-coefficient-tests)
