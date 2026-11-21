---
author: Yin
---
# Normality from a triple commutator in a torsion-free group algebra

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0002](../tasks/Yin_T_A0002_v1.md#contract) | Test the fixed-group domain assertion by the equivalent normality condition on a single finite group-ring element. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Determine when finite group support forces normality from the vanishing triple commutator, starting with a support admitting an extremal layer and retaining candidates with trivial real character space. |

For the usual adjoint and \(\partial_D X=[D,X]\), [C_A0095](../claims/Yin_C_A0095_v1.md#statement) proves that the fixed torsion-free group ring is a domain exactly when every \(D\) with \(\partial_D^3(D^*)=0\) is normal.
The factorial commutator estimate becomes exact nilpotence after restriction of scalars and passage to an integral matrix group ring.
Conversely a square-zero element automatically satisfies the cubic relation and violates normality.
The known prime-ring criterion keeps this reduction in the same group.

The power three is consequential.
If \(H=[D,D^*]\) and \([D,H]=0\), then traciality gives \(\tau(H^2)=\tau(D^*(HD-DH))=0\).
Since \(H=H^*\), faithfulness gives normality for every bounded operator in a finite tracial von Neumann algebra under this shorter relation.
The triple relation permits nonnormal square-zero operators in a matrix algebra, so a proof for scalar torsion-free group rings must use their additional structure.

One can compute both group-ring expressions for a specified actual support using its products and inverse labels.
The [extreme-layer argument](../claims/Yin_C_A0095_v1.md#testing-the-extreme-layers-of-one-element) excludes a minimal nonnormal witness on two character layers when the highest layer consists of one element.
For additional layers test whether successive extremal coefficients force commutation or produce a strictly smaller nonnormal witness.
A character defined on the subgroup of the support suffices.
The case where there is no nonconstant real grading on the support needs a separate mechanism.

The [single-prime route](Yin_S_A0009.md) supplies a second source of candidate pairs \(D,F\) via the integral defects of a modular one-sided inverse.
A noncommuting finite-dimensional adjoint orbit in the actual group algebra already implies a nonzero nilpotent.
For groups on which a finite complex nilpotent has yet to be found, neither the source equations modulo \(p\) nor formal word collisions establish that orbit condition.
