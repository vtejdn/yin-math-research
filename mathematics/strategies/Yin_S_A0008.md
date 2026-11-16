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
| priority | Seek a verified sparse projection of the collected supports of an exceptional matching, using the mod-eight criterion on a cyclic quotient of order seven. |

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

## Which cyclic quotients of the matching construction remain

The [finite-target entropy calculation](../claims/Yin_C_A0041_v1.md#statement) shows that the original random matching law admits a nontrivial map to any fixed finite target with exponentially small probability.
Both sides are [typically connected and almost all their vertex labels are distinct](../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots).
Alternatively, [independently matching seven equal color classes](../ledger/Yin_L_A0047_v1.md) gives genuine torsion-free realizations with a cyclic quotient of order seven.
Every quotient class then has exactly \(n/7\) vertex occurrences per side and an even positive number of collected group labels.
The projected equations lift by integer signs.
The [finite-target version](../claims/Yin_C_A0044_v1.md#statement) can arrange this compatibility simultaneously for every target in a preassigned finite list.

For any connected realization, the two collected supports have even cardinality.
The [cyclic lifting classification](../claims/Yin_C_A0042_v1.md#statement) proves that mod four always lifts here and that mod eight detects every obstruction to an exact lift at the marked point, even after allowing arbitrary finite ramification.
Only the two opposite four-class odd masks, each without any other occupied class, can fail.
Their [seven complete quotient fibers](../ledger/Yin_L_A0046_v1.md#complete-fibers-with-arbitrary-positive-odd-multiplicities) provide a direct certificate.
The [neighbor and integer-height tests](../claims/Yin_C_A0043_v1.md#neighbor-constraints) exclude these masks before collecting the connected vertex lists and constrain how they could arise after collection.

For this quotient, pursue only an exceptional matching with a verified nonzero character and sufficient group-label collision data to distinguish missing classes from occupied classes of even count.
In particular, in a nearly injectively labelled connected realization the remaining obstruction requires just one nonzero pair of letter increments and full occurrence coverage on at least one side.
Without a candidate meeting these conditions, use complete original fibers or investigate a different quotient.
