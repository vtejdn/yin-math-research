---
author: Yin
---
# Boundary supports of coefficient components and Newton polygon tests for half rank

## Statement

Let \(A,B\) be fixed finite nonempty subsets of a torsion-free discrete group \(G\).
Use complex coefficients, left convolution and the canonical regular rank \(r\).
Let \(Z\) be the variety of zero products with these exact supports, modulo separate scalar rescaling of the two factors, equivalently with one chosen coefficient on each side fixed to one as in [C_A0030](Yin_C_A0030_v1.md#statement).
Write \(n=|A|+|B|\).
Every irreducible component of \(Z\) has dimension at most \(n-16\).
In particular for \(n=16\) there are only finitely many normalized solutions and all their coefficients are algebraic numbers.
This conclusion requires no rank hypothesis.
The subtable recursion below can lower the dimension bound using the actual coefficient collisions.

There is a stronger test for a coefficient family given by monomials in two parameters.
Write \(z=(z_1,z_2)\in(\mathbb C^\times)^2\) and take
\[
 a(z)=\sum_{x\in A}\alpha_x z^{m_x}x,\qquad
 b(z)=\sum_{y\in B}\beta_y z^{n_y}y,
 \qquad m_x,n_y\in\mathbb Z^2,\quad \alpha_x\beta_y\ne0 .
\]
Suppose a nonunit irreducible Laurent polynomial \(H\) divides **every** coefficient polynomial of \(a(z)b(z)\).
Let \(P\) be its Newton polygon, the convex hull of the exponents with nonzero coefficients.
If \(P\) is two-dimensional, test the primitive inward normal \(w\) of each edge.
If \(P\) is a segment, test both primitive normals perpendicular to it.
For each such \(w\) retain precisely the labels in
\[
 A_w=\{x:w\cdot m_x=\min_{x'}w\cdot m_{x'}\},\qquad
 B_w=\{y:w\cdot n_y=\min_{y'}w\cdot n_{y'}\}.
\]

1. For every nonzero root of the corresponding edge polynomial, specified below, there is a limiting zero product on exactly \(A_w,B_w\) with explicitly determined coefficients.
   Hence \(|A_w|+|B_w|\ge16\).
2. The rank of either limiting factor plus the rank of the opposite factor at **any** point of \(H=0\) is at most one.
   In particular a component containing a pair of half ranks cannot contain this cancelling curve if \(|A_w|\le4\) or \(|B_w|\le4\) for some tested \(w\).
   For instance \(|A_w|\le4\) bounds the rank of the column factor on the curve by \(1/2-2^{-69}\).
   One may also exclude a half pair using a boundary factor supported on at most two cyclic cosets of either orientation or with a finite moment rank lower bound strictly above one half.
3. Suppose the row exponents are pairwise distinct and span the plane affinely.
   If the curve contains a half pair and \(P\) has area and \(q\) edges, then \(|A|\ge4q\ge12\).
   If \(P\) is a segment, \(|A|\ge10\).
   The corresponding bounds hold independently for the columns.
   If **both** exponent lists are pairwise distinct on their respective sides and span the plane affinely, even existence of this cancelling curve requires \(n\ge14q\) in the polygon case and \(n\ge32\) in the segment case.

## Cutting a component by product coordinates

Take the projective closure \(X\) of an irreducible component in \(\mathbb P(\mathbb C^A)\times\mathbb P(\mathbb C^B)\).
Every point still gives a zero product since the equations are bihomogeneous, and neither projective factor can be the zero vector.
Suppose \(X\) has dimension \(d>0\).
Choose a row and a column coefficient both nonzero at the same point of \(X\).
Their product is a linear coordinate in the Segre embedding, so its vanishing cuts by a projective hyperplane that does not contain \(X\).
The projective dimension theorem used in the [projection dimension test](../ledger/Yin_L_A0040_v1.md) gives an irreducible component of this section of dimension \(d-1\).
On that component at least one of the two chosen coefficients vanishes identically by irreducibility.
Both were nonzero somewhere before the cut, so at least one additional label has disappeared.
Iterate within the selected component, each time choosing a nonzero product coordinate.
The final point gives a zero product with combined support size at most \(n-d\).
Its two supports have no uniquely represented product, since the coefficient of such a product would be nonzero.
The [Nielsen–Soelberg size theorem](../audits/literature/NS24/readme.md#author-manuscript) gives \(n-d\ge16\).
If \(n=16\), there are finitely many components and each is a point.
The [density of algebraic solutions](Yin_C_A0030_v1.md#components-and-exact-support) in this finite normalized set makes every point algebraic.

There is also a finite bound using the individual products in the table.
For nonempty \(I\subseteq A,\ J\subseteq B\), discard \((I,J)\) if any element of \(IJ\) has a unique representation in \(I\times J\) or if \(|I|+|J|<16\).
For a component containing a half pair, also discard the pair if either side has at most four points or lies on at most two cosets of one infinite cyclic subgroup.
Indeed the [projective closure bound](../ledger/Yin_L_A0040_v1.md) gives ranks at most one half separately throughout the closure, and the four-point and two-coset results exclude those supports.
One may use any verified two-coset covers in this discard rule without having to decide subgroup membership in an arbitrary presented group.

Set \(D(I,J)=-1\) for discarded pairs.
Evaluate the following recursion on the other pairs in order of increasing combined size, taking the maximum of an empty collection to be \(-1\):
\[
 D(I,J)=1+\min_{(x,y)\in I\times J}
       \max_{\substack{\emptyset\ne I'\subseteq I,\ \emptyset\ne J'\subseteq J\\
                       x\notin I'\ {\rm or}\ y\notin J'}}
         D(I',J').
\]
Then \(\dim X\le D(A,B)\), with the additional discard rule available only under the half-pair hypothesis.
To see this, apply induction by combined size to any irreducible projective subvariety of \(X\) whose generic supports are \(I,J\).
The generic supports occur together on a nonempty open subset, so this pair cannot have been discarded.
Dimension zero satisfies the recursion automatically.
In positive dimension, **every** selected Segre coordinate \(a_xb_y\) cuts by one dimension, leaving an irreducible subvariety whose generic supports \(I',J'\) omit \(x\) or \(y\).
The induction bound on that subvariety gives the maximum above for the chosen cell and allows the minimum over cells.
For example, if all surviving proper subtables retain a particular row and a particular column, their common cell forces dimension zero even when \(n>16\).

## Each edge root gives an actual limiting pair

Complete \(w\) to a unimodular pair of integer covectors \(w,\ell\).
Use torus parameters \(u,v\) in which \(z^m=u^{w\cdot m}v^{\ell\cdot m}\).
In these coordinates divide \(H\) by its lowest power of \(u\), calling the result \(K(u,v)\in\mathbb C[u,v^{\pm1}]\).
The edge polynomial \(K(0,v)\) is nonzero with at least two distinct exponents, since the selected face has positive length and \(\ell\) separates its exponents.
After shifting the lowest \(v\)-power away it has a nonzero constant and positive degree, and therefore has a nonzero root.
The directions here use the ordinary minimum convention for a trivially valued Laurent polynomial, as in [Maclagan, Definitions 1.3 and 2.2](https://arxiv.org/pdf/1207.1925v1#page=4).

Every \((0,\lambda)\) with \(K(0,\lambda)=0,\ \lambda\ne0\), lies in the usual complex closure of the torus curve.
Indeed \(K\) is irreducible in \(\mathbb C[u,v^{\pm1}]\), since it is irreducible after inverting \(u\) and has no factor \(u\).
Its zero set in \(\mathbb C\times\mathbb C^\times\) is therefore irreducible, and its nonempty open part \(u\ne0\) is dense also in the usual topology by the [complex-variety density fact](Yin_C_A0030_v1.md#components-and-exact-support).
Nonemptiness of that open part also follows because \(H\) is a nonunit in the Laurent ring over \(\mathbb C\).
This works for multiple edge roots without asserting a single-valued branch over the \(u\)-plane.

Approach \((0,\lambda)\) on this curve and divide each factor by its own minimum \(u\)-power.
The two limits are the nonzero elements
\[
       a_{w,\lambda}=\sum_{x\in A_w}\alpha_x\lambda^{\ell\cdot m_x}x,
       \qquad b_{w,\lambda}=\sum_{y\in B_w}\beta_y\lambda^{\ell\cdot n_y}y .
\]
Coincident exponents on one side do not cancel distinct group labels.
All group coefficients of the product vanished along the curve by the divisibility hypothesis, so they vanish at the limit as well.

The two ranks attain their suprema simultaneously on the smooth locus of the irreducible curve by the [holomorphic evaluation argument](Yin_C_A0030_v1.md#rank-from-random-evaluations-on-a-connected-parameter-space).
They sum to at most one at such a point, because the range of \(b\) lies in the kernel of \(a\).
Lower semicontinuity and density of smooth points bound the ranks at singular points by those same suprema.
Rescaling on the punctured chart preserves ranks, and convergence of the finitely many coefficients is operator-norm convergence.
Thus the rank of each limiting factor is also at most its corresponding supremum, which proves the asserted mixed-point bound.
If the entire curve lies in a component containing a half pair, each supremum is at most one half by the component theorem, even when the chosen pair itself is elsewhere on the component.
The quantitative exclusion uses the [four-point bound](Yin_C_A0027_v1.md#four-point-rank), the [two-coset bound](Yin_C_A0019_v1.md#consequences-for-group-ring-products), or [finite moments of a normalized factor](Yin_C_A0030_v1.md#finite-moments-using-the-original-product-equations), at the stated scope of each.

## Counting boundary labels around the polygon

Let \(Q_A=\operatorname{conv}\{m_x:x\in A\}\) have dimension two, with all \(m_x\) distinct.
For any tested normal, a vertex exposed in \(Q_A\) would leave a monomial in the boundary row factor.
That unit cannot annihilate the nonzero boundary column factor.
Thus each tested normal must also expose an edge of \(Q_A\), irrespective of ranks.
For a polygon \(P\) with \(q\) edges, these give \(q\) distinct edges of \(Q_A\).
Among the labels on the selected edges, only a shared endpoint of two selected edges is counted twice.
There are at most \(q\) such vertices, since the selected edges form a subgraph of the polygon cycle.
Consequently \(\sum_w|A_w|\le |A|+q\).
If the curve contains a half pair then each summand is at least five, proving \(|A|\ge4q\).
For a segment \(P\), the two opposite normals select disjoint faces of the planar \(Q_A\), giving \(|A|\ge10\).
Interchanging \(A,B\) proves the column assertions.
If both exponent lists satisfy the hypotheses, summing \(|A_w|+|B_w|\ge16\) gives \(16q\le n+2q\) in the polygon case and \(32\le n\) in the segment case.

## Testing a branch with two residual parameters

Normalize one coefficient on each side to one.
In the free character lattice on the remaining labels, a two-term fiber prescribes the value \(-1\) on its exponent difference.
The [saturation calculation](Yin_C_A0026_v1.md#coefficient-table-and-statement) gives finitely many branches on the saturated sublattice spanned by these differences.
If its quotient after normalization has rank two, choose a complementary basis.
On a fixed consistent branch the normalized row and column coefficients now have precisely the two-parameter monomial form above.
Compute the actual fiber polynomials \(F_g=\sum_{xy=g}\alpha_x\beta_y z^{m_x+n_y}\), combining like exponents.
If some \(F_g\ne0\), every irreducible curve component of their common torus zeros is defined by an irreducible factor of their Laurent gcd, and each such factor gives a cancelling curve.
Indeed the ideal of an irreducible curve in the two-dimensional Laurent polynomial ring has height one and is principal by unique factorization.
After the common curve factors are accounted for, all components outside their union are isolated points and hence finite in number.
If all \(F_g\) vanish identically, one can take a torus path with a generic exponent direction exposing a vertex of \(Q_A\).
When that vertex carries just one row label, the limiting row is a monomial and the limiting column is nonzero, contradicting the identically vanishing product.
In particular, if one side has at most nine labels with pairwise distinct exponents whose affine span is the plane, the component of any half pair on such a branch must be an isolated point.
This test does not require a grading making every actual fiber homogeneous.

For a concrete calculation of a multiple edge root, take \(C_4=\langle g:g^4=1\rangle\),
\[
       a(s,t)=1+2tg+t^2g^2+sg^3,\qquad b=1+g+g^2+g^3 .
\]
Then \(a(s,t)b=((1+t)^2+s)b\), so \(H=(1+t)^2+s\) divides every actual fiber polynomial.
The edge at \(s=0\) has the double root \(t=-1\).
Along \(s=-(1+t)^2\) the boundary row is \((1-g)^2\) and still kills \(b\).
This example verifies the boundary specialization on an actual group table in the presence of torsion.
The support-size and four-point rank exclusions above require torsion-freeness.
For the [A0001 problem](../tasks/Yin_T_A0001_v1.md#contract), isolated coefficient solutions and branches with repeated labels at exposed exponents still require further rank information.

## Assessment history

### Decision component-boundaries

| Field | Value |
| --- | --- |
| date | 2026-11-17T01:29 |
| status | proved |
| reason | The independent review covers the full statement and argument at their stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Dimension, support recursion, Newton edge boundaries and the stated planar counting restrictions. |
| argument | [Proof](#cutting-a-component-by-product-coordinates) | The complete argument and its conditions of applicability. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0064_v1.md#whole-argument-finding) | Independent review of the exact statement and proof. |

## Current assessment

[Selected decision](#decision-component-boundaries)
