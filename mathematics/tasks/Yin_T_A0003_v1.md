---
author: Yin
---

# Kernel projections in the division closure of a torsion-free group algebra

## Contract

Let \(G\) range over finitely generated torsion-free discrete groups.
Use the regular representation, its group von Neumann algebra \(\mathcal N(G)\), and the division closure \(D_G\) of \(\mathbb CG\) in \(L^0(\mathcal N(G))\).
Determine whether the orthogonal projection \(p_x\) onto \(\ker x\) belongs to \(D_G\) for every \(G\) and every \(x\in D_G\).
Rational elements here can have arbitrary finite inverse depth and can be unbounded.

The [group-algebra finite-rank criterion](../claims/Yin_C_A0131_v1.md#statement) identifies this question with \(D_G=R_G\), where \(R_G\) is the algebraic \(*\)-regular closure of \(\mathbb CG\) in the same affiliated ring.
Equivalently, the question is whether existence of a fraction pair and finite-rank solution in that criterion characterizes membership in \(D_G\) for every such group.

A positive resolution requires a proof for every specified \(G,x\).
A negative resolution requires a finitely generated torsion-free group in its regular representation and an \(x\in D_G\) with a proof that \(p_x\notin D_G\), or equivalently an element of \(R_G\setminus D_G\).
In the latter formulation a witness already has a finite-rank certificate by the cited criterion.
Any completion review must cover the group, representation, both closure memberships at issue and the exact universal proof or counterexample.

## Starting evidence

For a group satisfying the complex strong Atiyah conjecture, \(D_G\) is a division ring and \(p_x=0\) for every nonzero \(x\in D_G\).
The [integer-dimension question](Yin_T_A0001_v1.md#contract) would thus give one sufficient answer.
The present question also permits \(p_x\ne0\) provided it lies in \(D_G\).
The [equivalence with closure under relative inverses](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected) reduces the unrestricted step to membership of these kernel projections.
The vanishing of a homogeneous cycle in a free group, or failure of uniqueness for a group with relators, does not decide that membership.

## Current decision

[Proposed research](#decision-proposed)

## Lifecycle and completion

### Decision proposed

| Field | Value |
| --- | --- |
| date | 2026-11-25T06:21 |
| status | proposed |
| authority | Yin's inquiry about extending F0001 to finitely generated groups, particularly torsion-free groups, permits registering the unresolved uniform question for a separate research decision. |
| reason | The finite-rank equation detects the regular closure for every marked group. Equality with the division closure under torsion-freeness alone remains to be established or refuted. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Kernel projections](#contract) | Membership of every scalar rational kernel projection for every finitely generated torsion-free group in its regular representation. |
| support | [Finite-rank characterization](../claims/Yin_C_A0131_v1.md#decision-group-algebra-criterion) | Reduction to equality of the division and regular closures, including the known strong Atiyah case. |
