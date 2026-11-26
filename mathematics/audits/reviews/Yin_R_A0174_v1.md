---
author: Yin
---

# Finite-rank witnesses, their column pencils and mixed cycles

## Two-sided cycles

At 2026-11-26T03:29 UTC a reviewer outside proof development reviewed C0165 v1 from the fixed text and its cited inputs.
The graph weight spaces give the asserted weighted permutations and common edge representation at every unit phase.
The ordered closing factor is \(T_nT_1\cdots T_{n-1}\).
Restriction of a nonidentity closing word to its infinite cyclic subgroup reduces the loss to the polynomial \(\det(I-zK_j)\), whose constant coefficient is one.
At the identity word the finite nullity is exact for that corner and the combined inequality gives the stated upper bound for the original operator.
The mixed scalar pivot and the original cycle elimination use only legal affiliated inverses.
The reviewer checked the two residues modulo nine and the four arrows outside the abelian subgroup modulo five.
This establishes regular full rank for the specified matrices.

## Small commutator witnesses

A separate reviewer outside proof development inspected C0166 v1 at 2026-11-26T03:29 UTC and the complete v2 at 03:31 UTC.
The review verified the rank inequality on the two legs, inverse orientation, cyclic restriction and induction giving a single chain at minimal dimension increase.
For two labels of ranks \(r,1\), both legs gain the extra required dimension unless the subgroup is cyclic, which is handled by the cyclic case.
The three active labels give distinct planes on a three-dimensional side, with the asserted alternatives for their intersections.
A shared endpoint lets the group-ring lift preserve the nonzero elementary tensor and contradict vanishing of its product.
In v2 a relation gives a simple cycle, a disjoint translated cycle and a shortest connecting path.
The resulting edge space exceeds the vertex space by one dimension.
The weighted kernel and scalar injectivity yield a nonzero common left multiple that clears the two denominators on the correct side.
This proves the pairwise freedom requirement even with an affiliated, possibly unbounded, common left factor.
The reviewer verified the sum and product orders in the two projective configurations, the four distinct group coefficients in the scalar test, and the circle character argument on the subgroup of the active labels.
The result allows a relation involving all three labels.

## Prescribed-list rank increments

The reviewer of the small witnesses also independently reviewed C0167 v1 at 2026-11-26T03:30 UTC and all of v2 at 03:32 UTC without participating in the development of either version.
Coefficient comparison in the first-leg basis gives \(wK=0\) and \(Kv=-\alpha\eta\).
The complementary image projection gives the upper and lower bounds on the fractional increment.
For the converse the relative inverse gives \(Kz=\alpha p\), and one common right regularizer gives the nonzero bounded tensor with the stated sign and at most one elementary input at each position.
The constant quotient and the first fractional row increment prove the two remaining implications and the row restriction.
Twisting on the generated subgroup and applying the polynomial rank theorem in both directions proves the infinite character deletion.
The four-term identity, equality of the ordinary ranks of each two-by-two coefficient matrix and its rearrangement, and rank invariance under the two outside multipliers identify the original Schur rank as the increment.
For a finite character the original and constant-quotient ranks each have a downward deviation of at most \(1/n\) from an integer.
Taking their difference retains that same bound.
No infinite-order character or change of group is inferred from a finite one.

## Additional check of the original pencil proof

At 2026-11-26T03:29 UTC the mixed-cycle reviewer checked C0167 v1 in full.
This reviewer had suggested looking at the relations on a first tensor leg and its one-step right translates in the preceding strategy discussion.
The finding is retained as an additional mathematical check with that prior connection.
The reviewer verified the two constructions, matrix rank conversions, row bound and infinite character deletion.
The independently assigned finding above supports adoption of v2.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Two-sided cycles](#two-sided-cycles) | independently reviewed |
| [Small commutator witnesses](#small-commutator-witnesses) | independently reviewed |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Two-sided cycles](#two-sided-cycles) | [Statement](../../claims/Yin_C_A0165_v1.md#statement) | Regular rank, cycle-word hypothesis and the two explicit examples. |
| [Two-sided cycles](#two-sided-cycles) | [Finite representation](../../claims/Yin_C_A0165_v1.md#both-cycles-in-the-finite-representation) | Graph weight spaces and simultaneous nonzero corners. |
| [Two-sided cycles](#two-sided-cycles) | [Cycle elimination](../../claims/Yin_C_A0165_v1.md#eliminating-each-vertex-cycle) | Product order, torus rank, deficient corners and the regular trace bound. |
| [Two-sided cycles](#two-sided-cycles) | [Applications](../../claims/Yin_C_A0165_v1.md#two-and-three-states-with-two-vertex-contributions-on-every-arrow) | Both mixed cyclic inputs and their residues. |
| [Small commutator witnesses](#small-commutator-witnesses) | [Statement](../../claims/Yin_C_A0166_v2.md#statement) | Small total ranks, the two-label mixed-multiplicity case and the remaining three-label conditions. |
| [Small commutator witnesses](#small-commutator-witnesses) | [Endpoint dimensions](../../claims/Yin_C_A0166_v2.md#endpoint-dimensions-and-a-cyclic-chain) | Two spans, extremal chain and rank inequality. |
| [Small commutator witnesses](#small-commutator-witnesses) | [Lifting endpoints](../../claims/Yin_C_A0166_v2.md#shared-endpoints-and-lifting-a-leg-into-the-group-ring) | Pulling a leg into the group ring and preserving its tensor rank. |
| [Small commutator witnesses](#small-commutator-witnesses) | [Common left multiple](../../claims/Yin_C_A0166_v2.md#a-group-relation-gives-two-binomials-a-common-left-multiple) | Weighted edges and two disjoint cycles. |
| [Small commutator witnesses](#small-commutator-witnesses) | [Three configurations and characters](../../claims/Yin_C_A0166_v2.md#the-three-planes-and-a-character-test) | Projective incidence, fractional linear functions and the phase test. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Statement](../../claims/Yin_C_A0167_v2.md#statement) | The label-by-label equivalence, actual Schur rank and tests by characters. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Forward direction](../../claims/Yin_C_A0167_v2.md#passing-from-a-commutator-sum-to-a-fractional-column-increment) | First-factor basis, ranks of both output factors and the new column. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Reverse direction](../../claims/Yin_C_A0167_v2.md#constructing-the-rank-one-sum-from-the-pencil) | The relative inverse, bounded right multiplier, row prefixes and row bound. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Schur scalar](../../claims/Yin_C_A0167_v2.md#a-pencil-for-the-particular-schur-scalar) | Tensor identity, two-by-two coefficient budgets and the exact increment. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Infinite character](../../claims/Yin_C_A0167_v2.md#deleting-a-label-separated-by-a-character) | Generic ranks of the projected column and its reversed pencil. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Finite character](../../claims/Yin_C_A0167_v2.md#an-isolated-label-of-finite-character-order) | The finite phase inequality and the distance from integral rank. |
| [Two-sided cycles](#two-sided-cycles) | [Congruence double](../../claims/Yin_C_A0121_v1.md#statement) | Torsion, the original mixed pivot and the mod-five representation. |
| [Two-sided cycles](#two-sided-cycles) | [Two corner ranks](../../claims/Yin_C_A0123_v1.md#a-polynomial-with-affiliated-coefficients) | Trace-normalized rank estimate for the sum of the vertex matrices. |
| [Small commutator witnesses](#small-commutator-witnesses) | [First version](../../claims/Yin_C_A0166_v1.md#statement) | Initial endpoint geometry, cyclic proof and infinite character test. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [First pencil version](../../claims/Yin_C_A0167_v1.md#statement) | Original equivalence and deletion argument. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Finite-rank tensor identity](../../claims/Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) | Commutation, balancing and bounded coefficients. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Finite phase bound](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Degree-one rectangular pencil at finitely many and at infinitely many phases. |
| [Prescribed-list rank increments](#prescribed-list-rank-increments) | [Schur balance](../../ledger/Yin_L_A0081_v1.md#the-four-terms-before-word-expansion) | Four terms at the particular group-ring input. |
