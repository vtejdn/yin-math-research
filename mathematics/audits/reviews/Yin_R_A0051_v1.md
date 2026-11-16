---
author: Yin
---
# Primitive four-coset factors and finite abelianization

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0020_v1.md) for Yin on 2026-11-16T15:49 UTC.
The reviewer had checked the two earlier claims used as inputs, but did not develop this derivation or receive its development discussion, author explanations, exploration notes or earlier verdicts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0020_v1.md#statement) | Gcd removal, rank preservation, scalar uniqueness, localization of both supports and finite abelianization. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0020_v1.md#argument) | Both multiplication sides, the collision graphs, the rank inequality on degree layers and the unique-product obstruction. |
| [Whole-argument finding](#whole-argument-finding) | [Product-table test](../../claims/Yin_C_A0020_v1.md#a-finite-test-on-the-product-table) | Extreme rectangles and the cardinality bound for arbitrary real table weights satisfying all collision equalities. |
| [Whole-argument finding](#whole-argument-finding) | [Four-column relation](../../claims/Yin_C_A0021_v1.md#the-four-column-relation) | The primitive Laurent generator for each four-coset window under the half-rank hypotheses. |
| [Whole-argument finding](#whole-argument-finding) | [Two-coset rank bound](../../claims/Yin_C_A0019_v1.md#consequences-for-group-ring-products) | Rank strictly above one half for a nonzero element on at most two left cosets, or on at most two right cosets after taking its adjoint. |

## Whole-argument finding

The localization and finite-abelianization assertions hold for the primitive pair defined in the statement.
Each exterior gcd acts by a nonzero Laurent multiplier on the regular copies of its infinite cyclic subgroup and is an affiliated unit.
Cancelling the two gcds from opposite ends of the zero product therefore preserves the product and both ranks.
Within the four occupied left cosets of \(b\), its primitive column generates the full Laurent kernel of \(a\).
For a nonzero multiplier \(p\), the smallest and largest exponents of each coefficient times \(p\) are the corresponding sums of exponents.
Containment inside the original coefficient support therefore forces both exponents of \(p\) to be zero.
Taking adjoints converts the primitive left coefficients of \(a\) into primitive right coefficients of \(a^*\), giving the same uniqueness for left annihilators of \(b\).

Every representation of a fixed product contributes a row to the same row component and a column to the same column component.
Restricting either factor to one component preserves every required coefficient cancellation, so scalar uniqueness forces both graphs to be connected.
A row edge gives \(x^{-1}x'=yy'^{-1}\) in the subgroup of collision differences and a column edge gives that same element or its inverse.
Paths put the rows in \(x_0D\) and the columns in \(Dy_0\).
Conversely each generator of \(D\) belongs to both difference sets by definition.
The supports of the translated factors thus each contain the identity and generate \(D\).
Translation preserves their product being zero and preserves the regular ranks, which are the same on \(D\) and on \(G\) by right coset decomposition.

For the grading inequality, write \(s_+=t^n c\) with \(c\in\mathbb C[N]\).
The map from layer \(t^jN\) to \(t^{j+n}N\) then has multiplier \(t^{-j}ct^j\) in the chosen coordinates.
Conjugation preserves the canonical trace on \(N\), so the initial projection has \(N\)-dimension \(r_N(c)=r_D(s_+)\) on every layer.
On the sum of these initial spaces over \(M\) layers, any nonzero input has a highest occupied layer whose leading output cannot cancel.
Polar decomposition equates the dimension of this restricted domain with that of its closed image.
The latter is supported in \(M+n-m\) output layers and lies in the global range subspace.
Thus the compression of the global range projection dominates the closed image projection, and its \(N\)-trace is \((M+n-m)r_D(s)\).
Dividing by \(M\) proves the maximal-degree estimate, and applying it to the opposite homomorphism gives the minimal-degree estimate.

An epimorphism from \(D\) onto \(\mathbb Z\) would take at least two values on each of the generating supports, since each contains the identity.
For the translated first support, intersecting its four right cosets with \(D\) uses right cosets of \(D\cap x_0^{-1}Hx_0\).
The second uses left cosets of \(D\cap y_0Ky_0^{-1}\).
If either cyclic intersection had degree zero, one of that factor's two extreme parts would occupy at most two cosets.
The two-coset rank bound, with an adjoint on the right-coset side, would give rank strictly above one half in conflict with the grading inequality.
For trivial intersection the same conclusion follows because two distinct points in a torsion-free group lie in one coset of an infinite cyclic subgroup.
Consequently the grading is injective on both cyclic intersections and each occupied coset supplies at most one term of maximal degree.
Only maximal-degree pairs can contribute to the maximal sum, so the corresponding nonzero factors with at most four terms each have zero product.

The reviewer checked Definition 1.1 and Theorem 1.4 on pp. 2–3 of [Nielsen and Soelberg's author manuscript](../../literature/pdf/NS24--author.pdf).
For two nonempty finite subsets of a torsion-free group whose sizes sum to less than sixteen, it yields a product with one representation.
Its hypothesis holds here because \(D\) is a subgroup of \(G\) and the sum is at most eight.
That coefficient cannot vanish over \(\mathbb C\).
The source's computer-assisted bound is accepted at the level of its theorem statement.
Excluding an epimorphism to \(\mathbb Z\) proves finite abelianization since \(D\) is finitely generated.

For a real weighting of the product table, the collision equalities imply that every representation of a product attaining the maximal sum belongs to the maximal rectangle.
Its complete coefficient sum therefore still vanishes after restricting to that rectangle.
Applying the same source theorem gives the bound sixteen for the sum of the two side cardinalities, also at the minimum by negating the weights.
This conclusion allows real weights without assuming that they extend to a homomorphism.
The remaining case is a primitive difference group with finite abelianization and product tables satisfying these bounds.
