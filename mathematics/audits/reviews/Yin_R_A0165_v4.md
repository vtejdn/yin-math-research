---
author: Yin
---

# Independent completion review of the finite-rank criterion for a group algebra

## Completion of A0003

An independent reviewer checked the [A0003 contract](../../tasks/Yin_T_A0003_v2.md#contract) and the [finite-rank characterization](../../claims/Yin_C_A0131_v3.md#statement) at commit 5d82d034ed3de9be771fe6842638b1dde80ba4fd and issued this finding at 2026-11-25T07:42 UTC.
The reviewer worked in a separate context with no role in developing the proof and received only the fixed input locations, the required scope and the repository instructions.
The reviewer formed the finding before consulting the selected Claim assessments or the earlier self-reviews, then compared those findings with the independently obtained conclusion.

For necessity, the reviewer reconstructed the affine blocks for constants, generators, addition, multiplication and inversion.
In the inversion block the scalar Schur complement equals the element being inverted, so each inverse is taken on its actual affiliated domain at every finite expression depth. [Affine realizations](../../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
For the finite row \(r\) of entries to clear on the left and the finite column \(c\) to clear on the right, \((1+rr^*)^{-1/2}\) and \((1+c^*c)^{-1/2}\) give bounded regular denominators on the required sides. [Simultaneous denominators](../../claims/Yin_C_F0068_v1.md#argument)
The trace identity gives the sign of the commutator in (1), the constant coefficients of the pencil cancel, and the resulting witnesses use the same fraction pair. [Construction of the witnesses](../../claims/Yin_C_A0131_v2.md#constructing-the-finite-rank-operators)
For \(V\) spanned by \(s\delta_e\) and the entries of the row \(\eta\), applying a test operator \(B\) entrywise to \(\eta L=s\alpha\) gives \(B(\eta)L=0\).
Right multiplication in the affiliated matrix algebra then gives \(B|_V=0\), including when \(L^{-1}\) is unbounded.

For sufficiency, the relation matrix \(K\) incorporates all complex dependencies among the basis vectors and their first translates, including the identity translate.
Its first column fixes the coordinate of \(s\delta_e\).
If \(zK=0\) for an \(L^2\)-row, the assignments \(v_iX_j\mapsto z_iX_j\) respect all those relations, and extension by zero from their finite-dimensional span produces a bounded finite-rank test operator.
The local commutation condition forces \(z=0\).
Taking adjoints gives \(\ker K^*=0\), so \(KK^*\) and each leading principal compression are positive and injective.
The finite trace gives affiliated inverses at every matrix size.
Successive scalar Schur complements therefore put all entries of \((KK^*)^{-1}\) in \(D_G\), and multiplication in the order \(K^*(KK^*)^{-1}\) gives \(s^{-1}V\subseteq D_G\).
This reasoning allows zero divisors in \(D_G\). [Sufficiency argument](../../claims/Yin_C_A0131_v3.md#recovering-the-vectors-in-the-subspace)

Finally, the range of the commutator sum lies in \(E=V+\sum_j VX_j\).
Evaluating (1) at \(t^*\delta_e\) gives the coefficient \(-\tau(tt^*)\ne0\) on \(a\).
Since \(s\delta_e\in V\), it follows that \(a\in E\) and \(u=s^{-1}a\in D_G\).

The reviewer checked the source interfaces for affine realizations and finite-trace affiliated inversion against Mai, Speicher and Yin, Definition 4.2, Theorem 4.3 and Lemma 5.2, including the matrix amplification discussion on pp. 28–29 of the published version. [Affine realizations](../literature/MSY23/Yin_U003.md#msy23-u003) and [affiliated matrices](../literature/MSY23/Yin_U004.md#msy23-u004)
The two implications characterize every affiliated element for every finitely generated discrete group.
The local condition quantifies over finite-rank test operators and uses only the regular representation.
This establishes the revised objective with no division-ring or strong Atiyah hypothesis.
The separate assertion concerning (1) with unrestricted witnesses falls outside the reviewed completion claim.
At 2026-11-25T07:46 UTC the same reviewer rechecked both implications against the [completed Task decision](../../tasks/Yin_T_A0003_v2.md#decision-finite-rank-characterization) and confirmed that the selected contract, theorem and supporting arguments match the independently inspected inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Completion of A0003](#completion-of-a0003) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Completion of A0003](#completion-of-a0003) | [Task contract](../../tasks/Yin_T_A0003_v2.md#contract) | All group and element quantifiers, the finite-rank witness requirement, and both implications for unbounded affiliated elements. |
| [Completion of A0003](#completion-of-a0003) | [Criterion](../../claims/Yin_C_A0131_v3.md#statement) | The existential fraction pair, finite-rank witnesses and subspace, followed by the local test over all finite-rank operators. |
| [Completion of A0003](#completion-of-a0003) | [Proof](../../claims/Yin_C_A0131_v3.md#argument) | Necessity from the affine row and sufficiency from the finite translation relations, scalar pivots and the numerator identity. |
| [Completion of A0003](#completion-of-a0003) | [Affine realizations and scalar pivots](../../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Realization at all finite inverse depths and inversion of positive injective Gram blocks by scalar division closure. |
| [Completion of A0003](#completion-of-a0003) | [Construction of the witnesses](../../claims/Yin_C_A0131_v2.md#constructing-the-finite-rank-operators) | The common denominators, the affine row, range control and the signed commutator sum. |
