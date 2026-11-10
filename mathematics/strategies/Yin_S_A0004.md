---
author: Yin
---
# Relations-compatible analytic and algebraic ranks

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Prove that the actual affiliated rational closure of a complex group ring is a division ring, using the MSY23 equivalence with integer matrix rank. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Current priority selected by Yin; seek group-specific control of actual rational kernels, using the index-two extension probe as the preferred structured test. |

## Mechanism and obstruction

Use [MSY23, Theorem 5.25](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence): integer analytic rank for all polynomial matrices in a bounded tuple is equivalent to its actual rational closure, or equivalently its division closure, in the affiliated algebra being a division ring.
The [survey's analytic probe](../ledger/Yin_L_A0001_v1.md#relation-sensitive-analytic-probe) specifies the trace convention and the direct specialization to a tuple of regular group generators and their inverses.
This criterion already supplies the analytic-algebraic bridge; no free-field realization or algebraic freeness is required.
The remaining problem is to prove that every nonzero element of the actual rational closure is invertible, using an analytic argument that respects the group's relations.
An abstract division-ring embedding alone still does not identify this actual closure.

## Current findings

The [first mechanism tests](../ledger/Yin_L_A0002_v1.md) establish cyclic rational invertibility, mixed resolvent sums with nonzero scalar real part, and a noncommutative Klein bottle calibration.
They also exhibit a general finite-tracial obstruction to deriving rational invertibility from scalar polynomial injectivity alone.
The actual proofs, coefficient and domain limits, Ore obstruction and source qualifications remain in that fixed record.
These tests provide no new group-class coverage.

The [Ele03 matrix deduction](../claims/Yin_C_A0001_v1.md#statement), with its [independent whole-argument review](../audits/reviews/Yin_R_A0002_v1.md#whole-argument-finding), settles the proposed scalar-kernel extraction for finitely generated amenable groups and the stated scalar-denominator Schur complements.
The boundary estimate has error equal to the number of input components times the Følner boundary fraction.
If a nonzero Schur complement has a kernel, the polynomial block matrix yields a nonzero group-ring element with an analytic kernel.
This reduces that amenable case to scalar analytic injectivity; it neither derives amenability nor scalar injectivity from torsion-freeness.

## Strategic reassessment

The 10 November 2026 reassessment retains this route as the main approach and gives a structured finite-extension test priority over unrestricted depth-one experiments.
The amenable extraction and the [completed JZ19 tensor argument](../claims/Yin_C_A0002_v1.md#statement) close two specific interfaces; neither provides the missing implication from torsion-freeness to rational invertibility.
The tensor argument works for arbitrary affiliated operators, so its conclusion alone does not distinguish the group-ring setting.
For a scalar rational element \(r\), its centralizer lower bound gives
\[
\dim_{G\times G}C_{HS}(r)\geq\bigl(\dim_G\ker r\bigr)^2.
\]
This is compatible with a proper nonzero kernel unless an independent upper bound or discreteness statement is established.
The [JZ19 upper-bound mechanism](../audits/literature/JZ19/Yin_U001.md#hilbert-schmidt-mechanism) excludes eigenvalues outside the coefficient field through sofic product-group approximation and strict eigenvalue finiteness; it does not exclude zero, which already belongs to that field.
Its [strong Atiyah assembly](../audits/literature/JZ19/Yin_U001.md#base-change-proof) obtains the needed integer-rank input from the additional algebraic-coefficient Atiyah premise.
Consequently, further general cutoff or tensor refinements are support work when a specific application requires them, rather than the default candidate for the missing group-specific mechanism.

The retained [finite-tracial obstruction](../ledger/Yin_L_A0002_v1.md#why-infinite-orbits-and-scalar-injectivity-do-not-finish-the-argument) rules out an argument based only on finite trace and scalar polynomial injectivity, without refuting the canonical group-ring conjecture.
A useful continuation must exploit additional information about actual rational expressions, the group's relations or its canonical trace.
The [JZLA20 reduction](../audits/literature/JZLA20/Yin_U001.md#general-torsion-free-boundary) illustrates the distinction: the cyclic quotient of the finite source subgroup and its compatible rank extension make rational-complexity induction work.
Torsion-freeness alone does not supply that reduction, and relabeling the expression complexity does not replace it.

## Next discriminating step

Use the [index-two finite-extension probe](Yin_S_A0001.md#first-discriminating-step) as the preferred concrete test of this route, while retaining that strategy's separate finite-extension scope.
Choose an explicit torsion-free extension with \(D_{\mathbb C}(H)\) known to be the actual affiliated division ring, and screen the example against existing positive classes.
Verify the actual crossed-product embedding, its closure comparison and the complete division criterion before relying on them.
Then test whether the relation \(\alpha(b)b=h\) can be excluded for rational \(b\in D_{\mathbb C}(H)\) by an invariant, valuation or justified leading-term argument that goes beyond its exclusion for \(b\in H\).
Finding an actual rational solution is also a useful reverse test, subject to the existing nonzero-factor and finite-matrix verification obligations.
A criterion conditional on the absence of rational solutions, without any new way to constrain those solutions, does not justify expanding this branch.
Even a successful finite-extension criterion only covers its verified hypotheses; it does not propagate automatically to arbitrary torsion-free groups or arbitrary rational presentations.

Retain the earlier depth-one family as a comparison problem:
\[
r=(1-f)-(1-h)(1-g)^{-1}(1-k),
\qquad g\ne e,
\]
whose cyclic denominator is justified directly by torsion-freeness.
Return to this family when explicit relations suggest a group-ring elimination or canonical-trace argument that forces \(r=0\) or \(\ker r=0\).
The [continuation analysis](../ledger/Yin_L_A0002_v1.md#precise-continuation-point) states the corresponding block matrix and the original scalar kernel-extraction question.
The amenable scope is now covered above; the arbitrary torsion-free scope remains unresolved.
Assuming integer rank of that block matrix would be circular; generic expression induction and arbitrary finite-support kernel extraction have already failed the recorded tests.
Keep the complex-phase two-resolvent numerator as a smaller comparison example, without claiming an established open or novel status.
Any successful restricted test must subsequently be extended to arbitrary rational presentations before it can resolve the selected group's full Task.

## Decision conditions and contribution

Continue if the construction supplies an independent invertibility or kernel-vanishing argument applicable to the actual rational closure beyond an already known class, or removes a specific obstruction in the infinite-edge route.
Pause if it merely restates the known closure equivalence, assumes the desired matrix integrality, or imposes free-field realization incompatible with the group's relations.
The exact equivalence is established source input; a new mechanism proving its division-ring side and a new positive case remain unresolved.

## Source-audit findings

Yin's requested audits of Ele03, JZ19, JZLA20 and Lin93 have now read their complete selected editions.
Lin06 has the requested localization, Proposition 2.2 and Theorem 2.6 inspection, and Bar19 has the full Kielak appendix with its necessary preceding construction.
The actual source proofs, corrections, accepted foundations and unverified steps remain in their responsible units.

| Source | Consequence for this route |
| --- | --- |
| [Ele03](../audits/literature/Ele03/Yin_U001.md#boundary-proof) | Finite propagation makes the finite restriction possible; the Følner limit turns positive kernel dimension into a finite-support witness. Rational inverses need block linearization and cannot inherit finite propagation directly. |
| [JZLA20](../audits/literature/JZLA20/Yin_U001.md#general-torsion-free-boundary) | Rational tree complexity is usable only with its lower-complexity invertibility hypotheses and a suitable regular ambient comparison. Local indicability supplies the cyclic quotient of the expression's finite source subgroup; Hughes freeness identifies the actual analytic envelope. |
| [Lin93](../audits/literature/Lin93/Yin_U001.md#transfer-boundaries) | The free-tree finite-rank defect and the elementary amenable extension machinery supply the missing rank information for their stated classes, without scalar Ore localization. |
| [Lin06](../audits/literature/Lin06/Yin_U001.md#scope-for-schur-complements) and [Kielak's appendix](../audits/literature/Bar19/Yin_U001.md#affiliated-applicability-boundary) | Classical scalar fractions require the explicit Ore/domain hypotheses. For a field group algebra known to be a domain, nonamenability excludes Ore localization but does not exclude an actual rational division closure. |
| [JZ19](../audits/literature/JZ19/Yin_U001.md#affiliated-and-schur-applicability) | Coefficient change and canonical ranked envelopes transfer established matrix-rank information. The strong Atiyah deduction retains soficity and the algebraic-coefficient Atiyah premise. |

The [JZ19 cutoff tensor step](../claims/Yin_C_A0002_v1.md#statement) now has a complete domain-sensitive proof and the independent review selected there.
Its [source supplement](../audits/literature/JZ19/Yin_U001.md#lemma-910-2-completion) makes spectral distinctness explicit and replaces the unsupported cutoff-space codomain by the full Hilbert tensor product.
This resolves the selected analytic checking gap and proves the centralizer lower bound for arbitrary affiliated operators; it does not supply the separate upper bounds or integer ranks needed by the Atiyah argument.
The later coefficient-change assembly and its other external inputs are not independently re-reviewed by this local completion.
The source units also retain local statement/formula repairs without treating them as refutations of the main theorems.

Reuse the existing MSY23 and Lin00 proof inspections at their documented scopes.
Beyond the amenable test, a useful continuation must supply a replacement for the vanishing-boundary argument or the local-indicability reduction, rather than assuming the desired block-matrix integrality.
