---
author: Yin
---

# Kernel projections and the unrestricted finite-rank equation

## Task associations

| Task | Scope |
| --- | --- |
| [A0003](../tasks/Yin_T_A0003_v3.md#contract) | Decide how far the local commutation condition can be removed for finitely generated torsion-free groups. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Determine when the zero-kernel spectral projection of a bordered group-algebra pencil has its last diagonal coefficient in the division closure. |

## Mechanism and current evidence

The unrestricted equation detects rationality exactly for groups whose division closure contains its scalar kernel projections. [Unrestricted criterion](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected)
It suffices to work with a bounded affine pencil with injective leading block and constant border and to recover one diagonal coefficient of its kernel projection.
The coefficient and the kernel projection of the original scalar rational element determine one another by explicit rational operations. [Corner reduction](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil)
Complete deletion passes in both directions across a finite-index inclusion, which supplies a positive answer for virtually locally indicable groups. [Finite-index transfer](../ledger/Yin_L_A0073_v1.md#ascent-and-descent-of-kernel-projections)

The sharpened finite-rank criterion constructs its test matrix from the fraction and the solution tuple. [Prescribed witness space](../claims/Yin_C_A0131_v4.md#statement)
On the original freely chosen subspace, any sublinear cutoff on the ranks of test operators can be satisfied by adjoining translates along one infinite cyclic subgroup.
An arbitrary tuple can fail the full local condition even for a rational element of the two-torus. [Rank cutoffs and the torus example](../ledger/Yin_L_A0074_v1.md#restricting-the-rank-of-local-test-operators)

## Next investigation

For a bordered pencil \(B\) with last coordinate inclusion \(J\), consider \(J^*\varepsilon(B^*B+\varepsilon I)^{-1}J\) for \(\varepsilon>0\).
Each such compression is rational by scalar Gram elimination and spectral calculus gives strong convergence to the desired coefficient as \(\varepsilon\) decreases to zero.
The unresolved step is an algebraic formula for this particular limit using inverses of affiliated units.
If a nonzero scalar polynomial \(q\) satisfies \(q(B^*B)J=0\), the spectral measure on the range of \(J\) is supported on the finite set of nonnegative roots of \(q\).
Polynomial interpolation gives a scalar polynomial equal to one at zero and zero at every positive root, so applying it to \(B^*B\) and compressing by \(J\) gives the required kernel coefficient in the group algebra.
For infinite spectral support, test whether a recurrence with group-algebra coefficients on the columns \((B^*B)^jJ\) still isolates the zero projection by scalar rational operations.
A negative resolution requires proving nonmembership of the actual coefficient for a specified torsion-free group.
The finite-index result excludes proposed counterexamples commensurable with groups already known to admit complete deletion.
