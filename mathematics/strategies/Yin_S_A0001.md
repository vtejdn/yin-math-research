---
author: Yin
---
# Finite extensions through analytic crossed products

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Transfer the complex-coefficient conjecture from a normal finite-index subgroup to its torsion-free overgroup under explicit sufficient hypotheses. |

## Route

| Field | Value |
| --- | --- |
| disposition | proposed |
| priority | Preferred concrete companion to route four; test the index-two rational obstruction after checking actual realization and existing coverage. |

## Mechanism and missing bridge

Assume \(H\triangleleft G\), \(G/H\) finite, \(G\) torsion-free and the conjecture known for \(H\).
Set \(D=D_{\mathbb C}(H)\subseteq\mathcal U(H)\).
The intended bridge is to identify the induced crossed product \(D*(G/H)\) with the relevant analytic closure and establish its division property.
The [survey's finite-extension probe](../ledger/Yin_L_A0001_v1.md#finite-extension-probe) records the exact conditional setup and a self-checked index-two obstruction.
The known transfer theorem with finite-classifying-space, cohomological-completeness and torsion-free-quotient assumptions is the comparison benchmark, as recorded in the [permanence discussion](../ledger/Yin_L_A0001_v1.md#coefficients-and-permanence).
The [route-four reassessment](Yin_S_A0004.md#strategic-reassessment) selects this probe because its explicit extension relations may constrain rational elements, whereas the completed general finite-tracial lemmas supply no such constraint.
This is cross-route reuse of the same finite-extension mechanism, not a claim that the general torsion-free problem has reduced to index two.

## First discriminating step

For an explicit torsion-free index-two extension, verify the crossed-product embedding and the complete factorization criterion.
Check the analytic closure comparison as well; the retained factorization identity alone is not yet a proved complete division criterion.
Then test whether the equation \(\alpha(b)b=h\), with \(b\in D\), can have a rational solution even though it has no solution in \(H\).
Begin with a controlled class of rational expressions and identify an invariant that distinguishes group-level torsion from rational factorization.
Screen the chosen group against existing positive classes before claiming new coverage.
If the first investigation only restates the absence of rational norm solutions as a conditional criterion, retain that formulation but defer broader investment until a way to constrain rational \(b\) is available.

## Decision conditions and contribution

Continue if the probe produces a division criterion under weaker hypotheses than known transfer theorems, or an explicit rational obstruction in the actual analytic closure.
A verified obstruction would require extraction and review of a finite group-ring matrix before supporting a counterexample.
Pause the current formulation if it only assumes division of the crossed product without a testable way to prove or disprove it.
A positive finite-extension result would enlarge known cases; it would not show that every torsion-free group arises from such a subgroup.
