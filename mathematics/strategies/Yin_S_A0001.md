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
| disposition | active |
| priority | Structural companion to route four: seek an independent projective-generation constraint for an actual finite crossed product beyond known coverage, retaining the distinction between Artinianness and division. |

## Mechanism and missing bridge

Assume \(H\triangleleft G\), \(G/H\) finite, \(G\) torsion-free and the conjecture known for \(H\).
Set \(D=D_{\mathbb C}(H)\subseteq\mathcal U(H)\).
The [completed index-two investigation](../ledger/Yin_L_A0003_v1.md#division-and-rational-closure-comparison) proves the actual crossed-product embedding and its equality with both division and rational closures, by specializing Lin93's Artinian finite-extension argument.
Its [complete criterion](../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness) identifies division precisely with absence of a solution to \(\alpha(b)b=h\) in \(D\), and gives a finite group-ring matrix with kernel dimension \(1/2\) from any actual solution.
The [earlier survey probe](../ledger/Yin_L_A0001_v1.md#finite-extension-probe) retains the initial conditional formulation; its embedding and complete-criterion obligations are now resolved at the new fixed home.
The known transfer theorem with finite-classifying-space, cohomological-completeness and torsion-free-quotient assumptions is the comparison benchmark, as recorded in the [permanence discussion](../ledger/Yin_L_A0001_v1.md#coefficients-and-permanence).
The [route-four reassessment](Yin_S_A0004.md#strategic-reassessment) selects this probe because its explicit extension relations may constrain rational elements, whereas the completed general finite-tracial lemmas supply no such constraint.
This is cross-route reuse of the same finite-extension mechanism, not a claim that the general torsion-free problem has reduced to index two.

The [KLS17 projective criterion](../audits/literature/KLS17/Yin_U001.md#the-projective-formulation-with-its-full-hypothesis) supplies a precise alternative interface: for an actual semisimple Artinian closure, finite-subgroup K_0 generation controls the sizes and number of its simple blocks.
In a torsion-free group the required source is only K_0 of the coefficient field, so the missing surjectivity forces the crossed product to have a single division block.
The criterion does not require its coefficient skew field to be finite-dimensional over its center, but it does require independent generation in the actual crossed product.
Projectives associated with a finite quotient are not automatically induced from finite subgroups of the torsion-free overgroup; their relation to the actual action and cocycle must be proved.
KLS17 Proposition 4.3 does not establish arbitrary finite-extension permanence: its hypothesis for the whole finite quotient already assumes the conclusion for G.
The [audit's unresolved G-theory interface](../audits/literature/KLS17/Yin_U001.md#why-condition-3-has-not-been-cleared) is not used to remove these obligations.

In the index-two case the actual closure \(A=D\oplus Dt\) has right dimension two over the known subgroup division ring \(D\), with basis \(1,t\).
Restriction of scalars is exact and every finitely generated right \(A\)-module has finite right \(D\)-dimension.
Consequently \(\chi_H([M])=\dim_D M\) defines a homomorphism \(G_0(A)\to\mathbb Z\) with \(\chi_H([A])=2\).
For a finite group-ring matrix \(T\), its restricted matrix over \(D\) represents its action on the free right \(D\)-coordinates of the same domain and target.
Gaussian elimination over \(D\) preserves that matrix rank in \(\mathcal U(H)\), and the [two-coset trace comparison](../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding) therefore gives \(\chi_H([\operatorname{coker}T_A])=2\dim_G\operatorname{coker} T_{\mathcal U(G)}\).
Hence for \(C=\operatorname{coker}T_A\), a single equality \([C]=k[A]\) proves \(\dim_{\mathcal U(G)}(C\otimes_A\mathcal U(G))=k\) by right exactness, without preserving an arbitrary injection under coefficient extension.
For a [solution of the rational norm equation](../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness), the restricted matrix of \(t+b\) has \(D\)-rank one.
The class of \(A/(t+b)A\) therefore maps to \(1\) under the induced homomorphism \(G_0(A)/\mathbb Z[A]\to\mathbb Z/2\).
Such a solution would violate condition (3) itself, and the restriction calculation leaves the existence of a solution open.
Thus, under the stated subgroup hypothesis, (3), division of the actual crossed product and the absence of a rational norm solution are equivalent.
The forward direction uses the restriction character, and division gives the converse since a division ring has \(G_0\) freely generated by its regular module.

## Current test and coverage boundary

The [selected extension](../ledger/Yin_L_A0003_v1.md#concrete-group-and-existing-coverage) is \(G=\langle x,y,z\mid x^2y^2z^2=1\rangle\), with \(H\) the kernel sending each generator to \(1\in C_2\).
Its orientation character cannot lift to \(\mathbb Z\), excluding the simple invariant odd-valuation obstruction.
The [leading-coefficient calculation](../ledger/Yin_L_A0003_v1.md#a-leading-coefficient-constraint-on-every-rational-solution) uses a different cyclic quotient and forces any rational norm solution to give a solution in a free subgroup's actual division ring, where it is impossible.
This treats every rational element, but both \(G\) and \(H\) already belong to Linnell's class \(\mathcal C\).
Because that class is closed under elementary amenable quotients, every torsion-free finite extension of an \(H\in\mathcal C\) is already covered.
The 11 November 2026 investigation therefore completes this calibration without establishing a new permanence theorem.
The [independent whole-argument review](../audits/reviews/Yin_R_A0005_v1.md#whole-argument-finding) found no remaining mathematical or source-applicability gap in the stated scope.

## First discriminating step

For a new-coverage attempt, first identify a concrete \(H\) and extension not already covered by applicable finite-extension theorems; the bounded screening has not yet established such a pair.
For a distinct mechanism test, the retained [Promislow pair](../ledger/Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test) has no nonzero ambient homomorphism to \(\mathbb Z\), so the successful cyclic reduction cannot be repeated directly.
Its torsion-free virtually abelian status is already known; investigating its rational norm equation would test an additional invariant, not new group coverage.
Do not repeat the completed crossed-product comparison or expand more cyclic examples unless a concrete new use requires them.

## Decision conditions and contribution

Continue if the probe produces a division criterion under weaker hypotheses than known transfer theorems, or an explicit rational obstruction in the actual analytic closure.
A verified obstruction would require extraction and review of a finite group-ring matrix before supporting a counterexample.
Pause the current formulation if it only assumes division of the crossed product without a testable way to prove or disprove it.
A positive finite-extension result would enlarge known cases; it would not show that every torsion-free group arises from such a subgroup.
