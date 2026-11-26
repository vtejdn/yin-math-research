---
author: Yin
---

# Character and coefficient restrictions on the four-binomial matrix

## Statement

Let \(H=(a_{ij}g_{ij})_{1\le i,j\le3}\) have nine monomial entries over a torsion-free group \(G\), with \(a_{ij}\in\mathbb C^\times\) and \(g_{ij}\in G\).
Use the unnormalized regular matrix trace and write \(\delta=\dim_G\ker H\).
By group and scalar row and column gauges normalize the first row and column to ones.
The four remaining entries are nonzero multiples of group labels \(u,v,w,z\), in row order.
Put \(J=\langle u,v,w,z\rangle\), the [subgroup of closed support products](Yin_C_A0207_v1.md#localization-and-the-weighted-matching) in this gauge.
Elimination at the upper left subtracts exactly one from the rank, giving the [four-binomial matrix](Yin_C_A0266_v3.md#the-only-three-row-pattern-left) on the remaining two coordinates.

If the rank is noninteger, then \(0<\delta<1\) and \(J_{\rm ab}\) is finite.
For every finite abelian quotient of \(J\) of order \(N\),
\[
                         \delta\le (64/(11N))^{1/4}.
\]
In particular a half-dimensional kernel forces \(|J_{\rm ab}|\le93\).
More precisely, let \(m\) be the exponent of a given finite abelian quotient.
For every nonzero integer lift \((a,b,c,d)\) of the weights on \(u,v,w,z\) of any character of that quotient, put
\[
      d_*(a,b,c,d)=
      \max\{a,b,c,d,a+d,b+c\}-\min\{a,b,c,d,a+d,b+c\}.
\]
Then \(m\delta\le d_*(a,b,c,d)\).
All these assertions use only torsion-freeness.

Under the additional hypothesis that every nonzero group-ring scalar is regularly injective there are two further tests.

* In each of the three choices of two rows and in each of the three choices of two columns, the two fundamental closed products on that \(K_{2,3}\) support must freely generate their subgroup.
  Any spanning tree gauge for the face gives the same free-basis condition.
* There exist positive real numbers \(r_1,r_2,r_3\) such that each triple \((|a_{i1}|r_1,|a_{i2}|r_2,|a_{i3}|r_3)\) satisfies all strict triangle inequalities.
  A separate positive triple satisfies the same condition for the transpose of the modulus matrix.
  These tests may use the original coefficients before gauge normalization.

Failure of either additional condition forces the original regular rank to be an integer.

## An extreme matching of a three-square matrix

Every two-square monomial corner has integer rank one or two in a torsion-free group.
Eliminate at a monomial pivot: the scalar remainder is a difference of two monomials, zero or an affiliated unit by the bilateral shift computation for an infinite-order relative label.
If any corner has rank one, the same pivot in \(H\) leaves a two-square with one zero entry.
Its other entries are all zero or affiliated units of this same binomial form, so its rank is an integer by triangular elimination or deletion of a zero row or column.
Hence a noninteger rank forces all two-square corners to be affiliated units and the full rank to be strictly between two and three.

Give each entry of the three-square a real cost, and let the six permutation weights be the sums along the perfect matchings.
The three even weights and the three odd weights have equal sums, since each triple uses all nine entries exactly once.
If the six weights are not all equal, either the minimum or maximum occurs once, or one of these extremes occurs exactly twice with opposite parities.
Indeed if one extreme occurs twice in just one parity, the third weight of that parity must lie strictly beyond every weight of the other parity in the opposite direction, by equal sums, so the opposite extreme is unique.
If neither extreme has multiplicity at most two, both have multiplicity three and the six values have only two levels.
Equal sums would then require equal counts at the upper level in both parities, inconsistent with three occurrences.

Give a monomial at position \((i,j)\) integer cost \(k_{ij}\) by multiplying it by a formal central variable to the power \(k_{ij}\).
Use the preceding extreme, reversing all exponents if it is a maximum.
The [minimum matching potentials](Yin_C_A0219_v1.md#lower-and-upper-potentials) give row and column monomial gauges so all exponents are nonnegative and each edge of a minimizing matching has exponent zero.
At the zero endpoint, order this matched diagonal first and direct each other zero-cost position from its row to its column.
Every simple directed cycle replaces the corresponding diagonal edges to yield another minimizing permutation.
At a unique minimum the endpoint is triangular up to a simultaneous permutation, with monomial diagonal.
At a two-permutation minimum of opposite parities, the permutations differ by a transposition.
There is exactly one such directed cycle, of length two.
Thus the endpoint is block triangular with one full two-square monomial corner and one monomial scalar.
The corner is exactly a corner of the original matrix, since the zero-exponent coefficients retain their original entries.
In both cases the endpoint is injective when all two-square corners are units.
Extra endpoint entries outside the diagonal blocks do not change this conclusion.

## Integer characters and finite matching spreads

Take the costs on the normalized first row and column equal to zero and the four other costs equal to \(a,b,c,d\).
The six matching weights are precisely those in \(d_*\).
Their spread vanishes only for the zero vector: equality of \(a,b,c,d\) and \(a+d\) forces all four to vanish.
For a nonzero homomorphism \(J\to\mathbb Z\), its costs on the four generators therefore give a full-rank endpoint of the polynomial construction when the rank of \(H\) is noninteger.
At every unit-circle phase the evaluation has the original rank by the genuine character twist.
The [polynomial rank comparison](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) precludes a positive common deficit on infinitely many such phases against the full-rank endpoint.
Hence no such homomorphism exists, and finite generation gives finite abelianization.

For costs lifting a finite character, at each of the \(m\) distinct \(m\)-th roots the twist preserves the original rank.
This counts parameter values even if some characters coincide.
The [different-output-degree matching estimate](Yin_C_A0219_v1.md#interpolation-with-different-output-degrees) bounds the sum of their nullities by \(d_*\), since the block size at each of the nine sites is one.
For clarity, the multiplication map on the coefficient spaces in that estimate is injective by comparing the first nonzero coefficient of an input polynomial at the full-rank zero endpoint just constructed.
Thus this use requires neither a bounded inverse of the endpoint nor a specialization of an unbounded group-ring inverse in a quotient.
Reversing all costs preserves the spread and permutes the root parameters.
This gives the indicated individual-lift bound.

## The volume of the matching-spread ball

For a finite quotient of order \(N\) and exponent \(m\), the four normalized labels generate the quotient.
All its characters therefore give a subgroup of \((\mathbb Z/m)^4\) of order \(N\).
Its inverse image \(\Lambda\) in \(\mathbb Z^4\) has covolume \(m^4/N\).

The spread \(d_*\) is a norm, being the range of six linear forms, symmetric under negation with zero kernel.
Its closed unit ball has four-dimensional volume \(11/4\).
To see the normalization, identify \((a,b,c,d)\) with the six entries
\[
           (a+d,b,c\,;\ b+c,d,a)
\]
in two triples of equal sum, modulo adding a common constant.
This map identifies the integer lattice with the integral equal-sum lists modulo integral common constants.
Indeed for any such list \((e_0,e_1,e_2;o_0,o_1,o_2)\) add \(e_0-o_1-o_2\) to every entry, after which \(e_0=o_1+o_2\) and \(o_0=e_1+e_2\).
The four coordinates \(o_2,e_1,e_2,o_1\) recover \(a,b,c,d\).
Permuting the triples internally or exchanging them accordingly preserves the lattice and its volume.

The unique minimum is at any one of six possible coordinates outside a set of measure zero.
Take \(e_0\) minimal, subtract it, and set the resulting \(e_0=0\).
The four remaining free coordinates \(e_1,e_2,o_1,o_2\) are unimodular coordinates, by the same integral reconstruction.
They lie in \([0,1]\), with the single condition \(0\le e_1+e_2-o_1-o_2\le1\).
Replacing \(o_i\) by \(1-o_i\) shows that the sum of four coordinates in the unit four-cube must lie in \([2,3]\).
The portion of the cube with sum at least two has volume \(1/2\) by reflection; the portion with sum greater than three has volume \(1/24\) by the unit four-simplex at \((1,1,1,1)\).
This chamber has volume \(11/24\), giving the asserted total over six chambers.

If \(\lambda\) is the least nonzero spread on \(\Lambda\), the open balls of radius \(\lambda/2\) around its points are disjoint.
Volume comparison gives \(11\lambda^4/64\le m^4/N\).
Combined with \(m\delta\le\lambda\), this is the stated order estimate, including \(|J_{\rm ab}|\le\lfloor1024/11\rfloor=93\) at \(\delta=1/2\).

## The two-row and two-column subgroups

Assume regular scalar group-ring injectivity and noninteger rank.
Choose two rows and any pivot position in the first of them.
After putting this whole pivot row and column equal to ones, the other row of this face has the form \((1,\lambda s,\mu t)\) after permutation.
Subtracting the pivot leaves a row \((\lambda s-1,\mu t-1)\) in the residual two-square matrix.
Both entries are nonzero by the two-square-corner test.
The elements \(s,t\) are the two fundamental closed products of the face, and a different free basis of its graph fundamental group preserves injectivity of the label homomorphism.

Suppose the elements do not freely generate.
For distinct nonidentity labels up to inversion, the [weighted two-cycle calculation](Yin_C_A0166_v2.md#a-group-relation-gives-two-binomials-a-common-left-multiple) gives a nonzero common right multiple of the two entries by applying its left-multiple result to their adjoints and taking adjoints back.
When one label is trivial, or the two agree up to inversion, the nonzero entries commute and their product gives a common multiple.
Thus this row has a group-ring kernel column \((r,s')^{\mathsf T}\) with a nonzero coordinate.
The latter coordinate is an affiliated unit by scalar injectivity, so the column generates a right module of dimension one and fills the row kernel by faithfulness.
Applying the other row to the same column gives a group-ring scalar, either zero or an affiliated unit.
The nullity of the two-square is therefore an integer, contradicting the hypothesis.
Taking the adjoint proves the result on the other three faces.

## Strict triangles for the numerical coefficients

Choose a nonzero Hilbert-space kernel vector \(\xi=(\xi_1,\xi_2,\xi_3)\) and put \(r_j=\|\xi_j\|\).
For each row the three vectors \(a_{ij}g_{ij}\xi_j\) sum to zero, so their lengths satisfy the triangle inequalities.
If equality occurs in any of them, these vectors all lie in one complex line by equality in the Hilbert-space triangle inequality.
The same holds if any one of the three lengths is zero.
Choose a nonzero vector \(\eta\) on this line and constants \(c_j\) so that \(\xi_j=c_j(a_{ij}g_{ij})^{-1}\eta\) in that row.
In every row \(k\) the group-ring scalar \(\sum_j c_j(a_{kj}g_{kj})(a_{ij}g_{ij})^{-1}\) annihilates \(\eta\), so it is zero by scalar injectivity.
The group-ring column with entries \(c_j(a_{ij}g_{ij})^{-1}\) then lies in the kernel and has a unit coordinate, giving nullity at least one.
This contradicts \(0<\delta<1\).
Thus all \(r_j>0\) and all row triangles are strict.
The adjoint matrix has the same positive nullity by the finite trace and squareness, giving the transpose test.
For example a modulus matrix with diagonal \(2\) and all off-diagonal entries \(1\) fails already on rows, since summing the three required inequalities \(2r_i<\sum_{j\ne i}r_j\) gives a contradiction.
This excludes a fractional regular rank for every labeling at these boundary moduli.

## Assessment history

### Decision matching-spreads-and-six-free-faces

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | The matching interpolation, lattice volume and subgroup kernel tests give the stated character and coefficient restrictions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [An extreme matching of a three-square matrix](#an-extreme-matching-of-a-three-square-matrix) | Extreme parity and the two-square corner. |
| argument | [Integer characters and finite matching spreads](#integer-characters-and-finite-matching-spreads) | Actual parameter twists and integer output widths. |
| argument | [The volume of the matching-spread ball](#the-volume-of-the-matching-spread-ball) | The normalized lattice volume and the nullity bound. |
| argument | [The two-row and two-column subgroups](#the-two-row-and-two-column-subgroups) | Common right multiples and the row kernel. |
| argument | [Strict triangles for the numerical coefficients](#strict-triangles-for-the-numerical-coefficients) | Strictness under scalar group-ring injectivity. |
| review | [Matching spreads and six free faces](../audits/reviews/Yin_R_A0209_v1.md#matching-spreads-and-six-free-faces) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-matching-spreads-and-six-free-faces)
