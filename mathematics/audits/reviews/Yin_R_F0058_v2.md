---
author: Yin
---

# Self-review of the liberation-dual rationality criterion

Human record author: Yin.
Inspection: 2026-10-18T05:33.
Method and relationship: Codex authoring-agent self-review within the same proof-development session.
The reviewer had C_F0079 v1 and v2, the earlier self-review, C_F0068 Part A, C_F0063 Appendix A and the cited source-interface records.
This revision checks the definition without a vacuum condition, the complete criterion under that definition, and the normalization calculation in the fixed Claim.
This was not an independently arranged review and does not review the whole T_F0001 Task.

## Finding

The exact statement and complete argument of [C_F0079 v2](../../claims/Yin_C_F0079_v2.md#statement) were checked at the definition, proposition, tensor-recovery, assembled rationality and normalization scopes.
No unresolved gap was found in those scopes.
The result supports a proved, self-reviewed assessment for that Claim.

The new definition retains both bounded-vector domains and the liberation generator commutators, while dropping the value of L_i Omega.
The coordinate-separation proof and its closability argument were reread under precisely those hypotheses.
Neither proof evaluates L_i at the vacuum or uses a normalized representative.
The every-fraction rationality implication and fixed-pair uniqueness therefore remain direct consequences of the proposition and tensor recovery.

The normalization equivalence was checked separately.
For eta_i=L_i Omega in H, the correction a Omega maps to a eta_i is defined on M Omega and commutes with every left multiplier there.
Traciality and the linear-in-the-second-variable inner product give its adjoint value b eta_i* at b Omega.
Thus the difference operator has M Omega in its adjoint domain and kills Omega while preserving all generator commutators.
This argument uses no boundedness of eta_i and no unsupported equality of the original full operator domains.
It requires no nonatomicity.
The example L=P_Omega for one normal generator confirms that the value zero is a normalization, not an automatic property of an individual system.


For the proposition, the check reconstructed the finite-rank-cycle criterion, denominator clearing in both opposite tensor factors, the identity Phi_i(Psi_j(z))=delta_ij Theta(Psi_i(z)), and injectivity of each individual Psi_i under regularity of every scalar shift.
The latter was checked by a minimal tensor decomposition and the absence of finite-dimensional invariant subspaces, without using maximal Delta or the rationality theorem.
This excludes a dependency cycle between the proposition and the criterion.
The concrete two-point example correctly shows why the existence of liberation duals alone does not imply maximal Delta or uniqueness.

For tensor recovery, the adjoint formula is legitimate because every c_r* eta remains in M Omega, which is in Dom L_i*.
Thus the finite sum S_i is closable on M Omega.
Injectivity of s bounds the dimension of the image of S_i restricted to t M Omega; it is not used as a bounded-inverse assertion.
Density follows from the dense range of t.
The finite-rank closure has all H as its domain and is contained in the closure of S_i, forcing equality as operators.
The Theta outer actions and affiliated-tensor cancellation then identify the coordinate tensor, and the two quotient-space arguments recover both L2 factors.
The finite-rank closure input was also checked directly through the finite-dimensional range and the dense adjoint domain.

For the assembled criterion, C_F0068 Part A supplies the affiliated tensor identity for rational elements and the converse for a certificate for some fraction pair.
Its printed certificate sign is converted by negating its witnesses.
For a prescribed pair, ell_i=(s tensor t^op)k_i has total image a tensor t^op-s tensor b^op; the new recovery argument makes T_i=-Theta(ell_i) bounded finite-rank.
The finite-rank commutator identity consequently has the required sign sP_Omega b-aP_Omega t.
Existence for every pair implies existence for some pair by fraction existence, and uniqueness follows from vanishing finite-rank cycles.
No ordinary dual-system existence, fraction-rank invariance, or closure agreement for arbitrary ordinary duals is added to this Claim.

Established source theorems are accepted at the cited statement and applicability scopes; this inspection did not re-audit their complete original proofs.
The previous independent reviews of C_F0063 and C_F0068 are not relabelled as an independent review of the new generalized Claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0079_v2.md#statement) | Exact domain definition without a vacuum condition, nonatomic normality, maximal Delta, tensor recovery, rationality, uniqueness and normalization equivalence. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0079_v2.md#argument) | Complete proposition, tensor-recovery, rationality and common-domain normalization arguments, their source interfaces, signs and nonatomicity boundary. |
