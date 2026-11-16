---
author: Yin
---
# Lifting a characteristic-two zero product at a fixed residue point

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) | Seek a scalar counterexample over the complex numbers by lifting a fixed finite zero product in an actual torsion-free group. |

## Route

| Field | Value |
| --- | --- |
| parent | [Relations-compatible analytic and algebraic ranks](Yin_S_A0004.md#current-structural-investigation) |
| disposition | active |
| priority | Test exact unions of product fibers for a first lifting obstruction, then test whether the same residue point lies in the closure of characteristic-zero solutions. |

## Input and distinction from rank sampling

The [Ope26f construction](../ledger/Yin_L_A0034_v1.md#scope-for-the-group-ring-product) supplies a scalar zero product in characteristic two in a torsion-free group, at the scope of the authors' theorem.
An exact lift over a number field would already give a scalar kernel of trace strictly between zero and one.
No hypothesis on the value \(1/2\), on amenability, or on the number of occupied cyclic cosets is needed for this implication.
The [local lifting equations](../claims/Yin_C_A0038_v1.md#the-incidence-matrix-and-lifting) test successive powers of the same prime.
The [local saturation test](../claims/Yin_C_A0039_v1.md#horizontal-specialization) allows arbitrary ramification and tests the specified residue point.

## Which equations can discriminate

First distinguish a necessary coarse equation from a sufficient refinement.
Under a verified group homomorphism every fiber for the images of the group products is a union of actual fibers.
Thus a contradiction among these coarse equations obstructs the corresponding lift in the original group.
For the first mod-four test one can work with repeated occurrences before collecting equal source labels.
An odd multiplicity can be assigned the desired lifted coefficient and cancelling pairs of \(1,-1\); for even multiplicity use only such pairs.
This shows why an inconsistency after quotienting and allowing all occurrence coefficients would also give an obstruction on the actual odd-multiplicity supports.
By contrast, different components of the simultaneous-step graph can map to the same actual group element, so failure after imposing one equation per component alone has no such implication.
Satisfaction of all the refined equations with the distinguished root coefficients nonzero can yield a zero product; check the two actual collected factors and the coefficient field at every application.

Seek a union of entire actual or quotient fibers with even incidence at every vertex and cell count \(2\bmod4\).
Such a union excludes every unramified lift of the marked point at the first step.
The [finite quotient test](../ledger/Yin_L_A0045_v1.md) rules out using any quotient of order at most four to detect this obstruction.
It also rules out detecting a mod-four obstruction after projection to an odd-order quotient when the input vertices of each side occupy every projected label.
For a verified sparse quotient, retain all occupied images and their occurrence counts.
In \(C_7\) three complete fibers already obstruct every characteristic-zero solution for the indicated sparse supports, while additional occupied labels can enlarge those same fibers.
The [ramified example](../claims/Yin_C_A0039_v1.md#a-group-table-that-requires-ramification-at-the-marked-point) shows why this would still leave the characteristic-zero question open.
For the next decision seek an identity \(2^j f\in I\) with \(f\) nonzero at the marked point, or exhibit a component in characteristic zero specializing to it.
Either certificate requires verified group-product equations at the scope used.
The published type counts and the [type-level calculation](../claims/Yin_C_A0038_v1.md#statement) do not determine the complete table of a particular choice of matchings.
The rank sampling and moment tests in the parent route remain available for questions about the ranks of an actual complex solution.
