---
author: Yin
---

# Twisting the regular representation along relations

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) | Determine regular ranks of mixed complex group-ring pencils, starting with the first Schur step and its repeated-denominator extensions. |

## Route

| Field | Value |
| --- | --- |
| parent | [Relations-compatible analytic and algebraic ranks](Yin_S_A0004.md#mechanism-and-obstruction) |
| disposition | active |
| priority | Test a three-state repeated-denominator pencil whose upper and lower entries both have contributions from each vertex, so the two auxiliary corner ranks require independent verification. |

Use unitary representation families of the actual group to preserve the canonical trace throughout a deformation.
At a singular parameter of the auxiliary polynomial matrix, its coefficients may simplify enough to give a regular-rank lower bound.
The [22 November comparison with the F-series techniques](../ledger/Yin_L_A0069_v1.md#second-priority-for-an-individual-schur-complement) selected this branch to continue beyond ordinary scalar character tests and the finite-rank separator for freely placed rows.
The auxiliary matrices must satisfy every relator at infinitely many unitary phases.
An arbitrary finite-dimensional evaluation carries no lower bound of this kind.

The [first calculation](../claims/Yin_C_A0118_v1.md#statement) gives full rank for a shared denominator involving both sides of a noncentral amalgam with finite abelianization.
For the [property (T) vertex example](../claims/Yin_C_A0121_v1.md#the-finite-quotient-detecting-the-commutator) an actual commutator supplies both invertible corner maps in a finite quotient.
The tested pencils can use coefficients generating the entire double.
The [mixed relation comparison](../claims/Yin_C_A0122_v1.md#statement) shows that a conjugator interchanging tensor factors can keep infinitely many phases on a proper quotient where every two-dimensional choice of those pivots fails.
An un-conjugated commuting relation kills the required product of the two corner maps at **any** multiplicity for the specified two weights.

For multiple inverses, [the corner rank inequality](../claims/Yin_C_A0123_v1.md#statement) applies even to affiliated vertex coefficients after clearing the common denominators on the left.
When the upper entries are from vertex one, the lower border from vertex two, and the repeated diagonal and last entry are the same mixed \(p\), every chain length is settled.
To test a case where neither corner is forced triangular, keep the congruence double's \(p\), set \(s=I+3E_{21}\), \(t=I+3E_{32}\) in each vertex and use
\[
       h=s_1+s_2,\qquad b'=t_1+t_2,\qquad c'=s_1t_1+t_2s_2,
       \qquad p-c'p^{-1}h p^{-1}b'.
\]
Use its three-state polynomial border, decompose both corner matrices in the finite mod-five representation, and check their ranks with the original vertex convolution coefficients retained.
If the full corner ranks can be proved, determine which mixed words admit the same reduction.
If a polynomial calculation forces a corner kernel, record that kernel before searching for different auxiliary weights.
If both corner questions still require the original unknown vertex ranks, redirect effort to [cyclic edge supports](Yin_S_A0005.md#cyclic-edge-support-through-a-regular-group-action).
The general \(P_k\Rightarrow P_{k+1}\) test also allows an arbitrary final diagonal and unrestricted coefficients; no common deformation under those hypotheses is known here.
