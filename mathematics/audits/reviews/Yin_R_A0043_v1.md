---
author: Yin
---
# Independent whole-content review of the analytic and graph obstructions

This review was performed at 2026-11-12T13:14 UTC for Yin.
The reviewed artifact is the complete 2026-11-12 text of [L31](../../ledger/Yin_L_A0031_v1.md), including equations (1)–(12), the unnumbered graph and randomization arguments, and the final interface with C14.
The reviewer was outside substantive development and received only the fixed artifact, necessary fixed dependencies, the review assignment and applicable rules.
No development discussion, author explanation, previous R finding or other agent's mathematical conclusion was supplied or read before the initial findings; no prior review was subsequently relied on.
This is an initial whole-content mathematical inspection of L31, not a completion audit of the amenable Atiyah problem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-content finding](#whole-content-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-content finding](#whole-content-finding) | [Regularization](../../ledger/Yin_L_A0031_v1.md#cauchy-regularization-and-the-wrong-topologies) | Equations (1) and (2), their hypotheses, uniform finite-window proof and limit interpretation. |
| [Whole-content finding](#whole-content-finding) | [Norm barrier](../../ledger/Yin_L_A0031_v1.md#a-precise-norm-barrier) | The scalar projection input, connected spectrum and equations (3) and (4). |
| [Whole-content finding](#whole-content-finding) | [Inverse gates](../../ledger/Yin_L_A0031_v1.md#bounded-rational-output-versus-bounded-inverse-gates) | Equations (5)–(7), algebraic-annihilator applicability, affiliated products and both gap cases. |
| [Whole-content finding](#whole-content-finding) | [Support graph](../../ledger/Yin_L_A0031_v1.md#what-the-support-graph-already-knows) | Full matching, equation (8) and the complete-kernel-density invocation. |
| [Whole-content finding](#whole-content-finding) | [Uniquely restricted matching](../../ledger/Yin_L_A0031_v1.md#definition-uniquely-restricted-matching) | Uniform rank certificate, packing and cancellation proof of (9), unique-product equivalence and coefficient restriction. |
| [Whole-content finding](#whole-content-finding) | [Randomization](../../ledger/Yin_L_A0031_v1.md#randomization-retains-or-changes-the-decisive-correlations) | Generic shared coefficients, equations (10)–(12), converse finite-graph gauge construction and stated limits. |
| [Whole-content finding](#whole-content-finding) | [Surviving analytic target](../../ledger/Yin_L_A0031_v1.md#the-analytic-target-that-survives-these-obstructions) | C14 interface, remaining tail-estimate obligation and exclusion of universal or novelty conclusions. |
| [Whole-content finding](#whole-content-finding) | [Complete kernel localization](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization) | Exact kernel-density and rational-realization statements used in L31 at their stated hypotheses. |
| [Whole-content finding](#whole-content-finding) | [Affiliated domains](../../claims/Yin_C_A0001_v2.md#actual-realizations-and-affiliated-domains) | Invoked actual-rational and affiliated-domain conventions; no new audit of the external realization theorem. |
| [Whole-content finding](#whole-content-finding) | [Kernel-localization argument](../../claims/Yin_C_A0001_v2.md#proof-of-complete-rational-kernel-localization) | Applicability of the finite-support closure conclusion, with the earlier finite-propagation estimate accepted as input. |
| [Whole-content finding](#whole-content-finding) | [Beyond finite generation](../../claims/Yin_C_A0001_v2.md#passage-beyond-finite-generation) | Subgroup and coset transfer for the countable amenable generic-coefficient assertion. |
| [Whole-content finding](#whole-content-finding) | [C14 statement](../../claims/Yin_C_A0014_v1.md#statement) | Accuracy of L31's summary of the increment criterion, finite-moment dependence and conditional spectral exclusion; no separate whole-proof acceptance of C14. |
| [Whole-content finding](#whole-content-finding) | [HK97 assembly interface](../literature/HK97/Yin_U001.md#amenable-assembly) | Countable amenable assembly-surjectivity statement and its use in L31. |
| [Whole-content finding](#whole-content-finding) | [BCM04 trace interface](../literature/BCM04/Yin_U001.md#assembly-trace) | Torsion-free specialization of the assembly trace range and scalar projection consequence. |

## Whole-content finding

No mathematical gap requiring correction was found in the reviewed L31 argument.
Its conclusions are supported at their explicitly conditional and obstructive scopes.
None of these arguments proves injectivity for every nonzero element of a torsion-free amenable group ring.

### Regularization and finite windows

The scalar functions in (1) have exactly the stated support projections.
For distinct positive \(s,t\), their difference is \((t-s)x/((x+t)(x+s))\), which vanishes exactly at zero on the spectrum.
Thus rank distance remains \(1-\alpha>0\), although dominated spectral convergence gives strong and tracial \(L^2\) convergence and a vanishing tracial idempotency defect.

For (2), \(H+t\ge tI\) makes the complementary block invertible, and the compressed inverse equals the inverse Schur complement.
Its bound by \(t^{-1}I\) gives \(S\ge tI\).
The difference \(tS^{-1}-tK^{-1}\) is positive, bounded by \(I\), and has rank at most \(\operatorname{rank}C_F\), so its trace is bounded by that rank uniformly in \(t\).
Self-adjoint finite propagation places every nonzero row of \(C_F\) at the stated inner boundary.
The constant diagonal of \(q_t\) supplies the full trace.

Taking \(t\downarrow0\) is valid in the finite matrix and by normality of the canonical trace.
The kernel of \(H_F\) consists precisely of the vectors supported in \(F\) annihilated by \(a\), since its quadratic form is \(\|a\xi\|^2\).
The resulting normalized kernel estimate therefore has the intended meaning, but limits of normalized integers supply no integrality conclusion.

### Norm and inverse gates

HK97 gives assembly surjectivity for the required countable amenable group, and BCM04 puts the trace of its image in \(\Lambda_G=\mathbb Z\) under torsion-freeness.
Faithfulness excludes scalar projections of intermediate trace in \(C_r^*(G)\).
This uses the reduced \(C^*\)-algebra interface, without an inverse-closedness assertion for \(\ell^1(G)\).

A spectral disconnection of a self-adjoint element would produce a nontrivial continuous-functional-calculus projection.
Thus \(0\in\sigma(H)\) and \(M>0\) give \(\sigma(H)=[0,M]\).
The defect function attains \(1/4\) at \(x=t\), and positive spectral values approach zero, proving both equalities in (3), even when the zero atom vanishes.
For (4), a self-adjoint approximation at distance below \(1/2\) gives a spectral cut in \(C_r^*(G)\) at distance strictly below one from the nontrivial projection \(p\).
Neither scalar projection has that distance, while \(I/2\) supplies the matching upper bound.

In (5), the support of \(c=VV^*\) is exactly \(p\).
The operators \(H\) and \(c\) have orthogonal complementary supports, so \(H+c\) is injective and has an affiliated inverse.
The closed affiliated products in (6) are the stated bounded support projections.
A bounded inverse would belong to \(C_r^*(G)\), contradicting (4) for \(0<\alpha<1\).
These projection obstructions retain the torsion-free amenable hypotheses of the norm section.

When the entries of \(V\) generate the algebraic annihilator as a right module, complete kernel density supplies the Hilbert range closure.
For a single relation the residual kernel is \(\ker a\cap\ker b^*\).
If \(H+bb^*\) were invertible, the support of \(bb^*\) would be a nontrivial scalar \(C^*\)-projection; if zero were isolated in its spectrum, its nonzero proper kernel projection would instead contradict projectionlessness.
The assumptions \(a\ne0\) and \(b\ne0\) exclude the scalar endpoints.
Orthogonality of the two positive summands also proves (7).

### Support and tied coefficients

One fixed \(s_0\) gives a full column matching, so no Hall deficit remains.
Rank-nullity gives (8), and complete kernel localization supplies its normalized Følner limit.

A uniquely restricted matching gives a minor with one nonzero determinant term for every nonzero edge weighting.
For (9), the conflict set for translates is \((ST)^{-1}(ST)\), giving the stated greedy-packing lower bound.
Each row of \(STg\) has at least two distinct neighbors in \(Tg\).
The assigned weights make the sum over those columns zero, and rows outside \(STg\) have no neighbor in that column set.
Disjoint row and column sets make the assignments compatible and the kernel vectors independent.
The uniform rank certificate then gives (9) after the left Følner limit.

The same construction proves the converse in the asserted unique-product equivalence for arbitrary nonzero position-dependent weights.
In the forward direction, a uniquely represented product gives a nonzero output coordinate for every nonzero finite-support vector.
These graph statements do not preserve the tied coefficients required of a group-ring operator.

### Generic coefficients, gauges and perturbations

The minor on \(s_0T\) specializes to a permutation matrix, so its determinant polynomial is nonzero.
Its zero set has Lebesgue measure zero, and the union over the countably many finite supports still has measure zero.
Amenable finite-support kernel density then gives analytic injectivity.
The subgroup and coset passage in C1 supplies that implication for a countable ambient group even when it is not finitely generated.
This proves an almost-sure assertion without controlling any fixed exceptional coefficient tuple.

Block multiplication verifies (10).
Diagonal unitary conjugation preserves coordinate spectral measures and diagonal kernel weights, and multiplies each minor by a common nonzero row-and-column phase.
Row cancellation and column telescoping give (11).
The spanning-tree argument proves the converse for nonzero complex multipliers on a finite connected graph.
It supplies neither unitary multipliers without additional modulus conditions nor bounded multipliers on an infinite graph, as the text correctly states.

If the first inequality of (12) failed, the projection-intersection dimension bound would produce a nonzero vector in \(\ker H_0\) and the spectral subspace of \(H_\varepsilon\) outside the closed \(\varepsilon\)-window.
Its norm growth would be strictly greater than \(\varepsilon\), contradicting the perturbation bound.
For the second inequality, the corresponding intersection gives simultaneously \(\|H_0\xi\|>2\varepsilon\|\xi\|\) and \(\|H_0\xi\|\le2\varepsilon\|\xi\|\).
The intersection formula is used with a normalized trace; any finite trace may first be normalized without changing either inequality.
Normal continuity from above gives the asserted squeeze limit.
Nonatomicity at every positive noise therefore supplies no loss of mass in a window at the noise scale.

### Final interface and inspection limits

The C14 statement tests summability of spatially weighted increments of optimal polynomial approximants using finite moments and ball volumes.
L31 correctly retains the additional tail-estimate obligation and the stronger spectral-exclusion conclusion of the stated power-rate conditions.
No argument in L31 supplies that estimate.
The final limitations concerning continuous spectrum, tied coefficients, group-class coverage and historical novelty are justified.

The original HK97 and BCM04 assembly proofs were accepted at the statement-and-applicability depth recorded by the cited source units; their foundational arguments and original-source acquisition were not re-audited.
The C1 interfaces retain their existing finite-propagation and realization inputs.
C14 was checked as a linked conditional statement rather than registered here as a separately reviewed whole proof.
No numerical probing, experimental evidence, formal verification, novelty survey or Task-completion verdict is part of this finding.
