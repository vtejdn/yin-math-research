---
author: Yin
---
# Independent review of principal-annihilator certificates and finite-stage trace obstructions

## Review arrangement and fixed scope

The review act was completed at 2026-11-12T12:29 UTC, with Yin as the human record author.
A separately assigned agent outside the substantive development of the inspected proof performed this initial independent review.
The reviewer received the fixed mathematical text, necessary input locators, the review scope and applicable repository rules, without proof-development discussion, a mathematical summary of that development, author explanations or prior review findings.
No existing R material was read or used.
The inspection covers the complete three-subsection argument in the selected section of the 2026-11-12 working revision of L_A0030_v1 and its stated kernel-density, projective-trace and Hilbert-completion interfaces.
It does not review the other arguments in that ledger or certify completion of the Task.

Throughout the finding, \(G\) is torsion-free amenable, \(B=\mathbb CG\), \(0\ne a\in B\), and \(K_a=\operatorname{ann}_B(a)\), as in the surrounding ledger context.
The extra finite-cohomological-dimension and finiteness assumptions remain confined to the paragraphs that state them.
In particular, the statements about principal annihilators concern annihilators of nonzero elements.

## Inputs

[Inspected argument](../../ledger/Yin_L_A0030_v1.md#smaller-algebraic-certificates-and-their-exact-missing-hypotheses) supplies all three conditional certificates and their limitations.
The surrounding setup and projective-trace discussion were read to determine the nonzero-element premise and the intended interface.

[Complete kernel density](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization) supplies equation (3), used here only for bounded matrices over the group ring.
[Passage beyond finite generation](../../claims/Yin_C_A0001_v2.md#passage-beyond-finite-generation) supplies the extension of this input to arbitrary amenable groups.
The current argument and the exact use of that extension were inspected.
The underlying earlier finite-propagation estimate and the rational-realization theory are accepted at their stated scope rather than independently re-audited here.

[Finite projective resolution interface](../../claims/Yin_C_A0001_v2.md#the-finite-projective-resolution-interface) states the finite Euler-trace formula.
[Its Hilbert-completion proof](../../claims/Yin_C_A0001_v2.md#proof-of-the-homological-interface) was rechecked at the idempotent, restricted-kernel, image-closure and dimension-additivity interfaces used by all three subsections.

[BCM04 projective trace](../literature/BCM04/Yin_U001.md#amenable-projective-trace) supplies the established integer trace for every finitely generated projective right \(\mathbb CG\)-module under the exact torsion-free amenable hypotheses.
Its stated applicability was inspected.
The assembly theorem and original source proof were not independently audited.
The JZL25 attribution is not an additional proof input: the coefficient-specific diagonal-tensor argument is given and checked directly in the inspected ledger.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-section finding](#whole-section-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-section finding](#whole-section-finding) | [Complete selected section](../../ledger/Yin_L_A0030_v1.md#smaller-algebraic-certificates-and-their-exact-missing-hypotheses) | All three subsections, every displayed formula, added hypotheses, endpoint cases, finiteness conditions and stated limits in the 2026-11-12 revision. |
| [Whole-section finding](#whole-section-finding) | [Projective submodule certificate](../../ledger/Yin_L_A0030_v1.md#a-nonzero-projective-part-would-already-suffice) | Algebraic injection, completed injection, positive integer trace contradiction, universal-extraction equivalence and nonessentiality calculation for nonzero a. |
| [Whole-section finding](#whole-section-finding) | [Finite cohomological dimension](../../ledger/Yin_L_A0030_v1.md#finite-cohomological-dimension-does-not-supply-finite-generation) | Right-module diagonal tensor, global dimension, Ext shifting, d at most one, FP_t truncation including t zero, and exact coherence limitations. |
| [Whole-section finding](#whole-section-finding) | [Infinite-resolution tail](../../ledger/Yin_L_A0030_v1.md#an-infinite-coherent-resolution-can-preserve-the-fractional-tail) | Specified syzygy embeddings, weak exactness, both recurrence formulas, parity lower bounds and conditional vanishing or termination criterion. |
| [Whole-section finding](#whole-section-finding) | [Kernel-density input](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization) | Applicability of equation (3) to the bounded stacked group-ring matrices used in the selected ledger; not an independent review of the full rational-localization theorem. |
| [Whole-section finding](#whole-section-finding) | [Arbitrary amenable groups](../../claims/Yin_C_A0001_v2.md#passage-beyond-finite-generation) | Finite-matrix restriction and right-coset extension needed to use kernel density without a finite-generation hypothesis on G. |
| [Whole-section finding](#whole-section-finding) | [Finite-resolution statement](../../claims/Yin_C_A0001_v2.md#the-finite-projective-resolution-interface) | Equation (10) and its exact finite-resolution hypotheses as invoked by the ledger. |
| [Whole-section finding](#whole-section-finding) | [Homological proof interface](../../claims/Yin_C_A0001_v2.md#proof-of-the-homological-interface) | Trace of a bounded nonselfadjoint idempotent, stacked restricted kernels, weak exactness and Euler dimension formula; kernel density remains a declared input. |
| [Whole-section finding](#whole-section-finding) | [BCM04 trace input](../literature/BCM04/Yin_U001.md#amenable-projective-trace) | Exact hypotheses, unnormalized trace and right-projective applicability; the original assembly-theoretic proof is accepted externally. |

## Checked obligations

### Projective submodules and nonessentiality

For a right-module injection \(D:EB^r\to K_a\), extending by \(E\) gives a genuine finite group-ring matrix with \(D=DE\) and \(aD=0\).
The algebraic kernel of the stacked matrix \(\binom{D}{I-E}\) is zero precisely because an element in it lies in \(EB^r\) and is killed by the given injection.
Complete kernel density therefore gives a zero Hilbert kernel and makes the restricted map on the closed range \(H_E\) injective.
The nonselfadjoint nature of \(E\) causes no problem: the range-projection calculation in the cited homological proof identifies its trace with \(\dim_G H_E\).
A nonzero algebraic projective module has a nonzero Hilbert range, so faithfulness makes this dimension strictly positive.
Polar decomposition identifies it with the dimension of the image closure, which is contained in \(\ker a\).
The upper bound \(\nu(a)<1\) uses \(a\ne0\) and faithfulness of the regular representation.
The positive integer trace contradiction is consequently valid.

The universal extraction property is stated only as an equivalent unresolved condition: the proved obstruction makes it imply the domain conclusion, and the domain conclusion makes the quantified nonzero annihilators absent.
The identity \(K_a\cap a^*B=0\) follows from the displayed positive Hilbert norm calculation.
Since \(a^*\) itself is nonzero, \(a^*B\) is a nonzero right ideal witnessing failure of essentiality.
This proves the stated obstruction to an essential-ideal argument without deciding a Goldie hypothesis.

### Cohomological dimension and finite truncation

The diagonal action is a right action.
For \(g,h\in G\), the untwisting map sends \(gh\otimes mh\) to \(gh\otimes mg^{-1}\), exactly the result of applying \(h\) to the first factor after untwisting \(g\otimes m\).
Thus the displayed order of \(g^{-1}\) is correct.
The untwisted module is a direct sum of copies of the regular right module, indexed by a complex basis of \(M\).
Tensoring preserves exactness over \(\mathbb C\), and preserves the relevant split summands with their diagonal actions.
It therefore produces a projective resolution of \(M\) of length at most \(d\).
The basis may be infinite, so this argument supplies no finite-generation conclusion for the resulting terms.

The two short exact sequences give the stated double dimension shift for every \(i\ge1\).
When \(d\le1\), vanishing of \(\operatorname{Ext}^1_B(J_a,M)\) for all \(M\) makes \(J_a\) projective.
The resulting splitting makes \(K_a\) a finitely generated projective direct summand of \(B\), so the trace argument applies.

For \(d\ge2\), the bound \(\operatorname{pd}_B K_a\le d-2\) follows from the same shift.
Writing \(t=d-2\), the distinction between \(FP_0\) and projectivity is essential and is correctly retained.
At \(t=0\), the independent projective-dimension bound supplies projectivity, while \(FP_0\) supplies finite generation.
At \(t\ge1\), \(Z_t\) is the \(t\)-th syzygy and is finitely generated as the image of the finitely generated term \(P_t\).
The displayed \(\operatorname{Ext}^1_B(Z_t,M)\cong\operatorname{Ext}^{t+1}_B(K_a,M)\) has the correct shift.
Its vanishing makes \(Z_t\) projective and validates the finite truncation using \(P_0,\ldots,P_{t-1}\).
Every term of that truncation is finitely generated, so the cited finite Euler-trace formula has exactly its required hypotheses.

Right coherence would make the kernel of the finite free map defining \(K_a\) finitely generated and permit successive finite free presentations.
This supplies the indicated \(FP_t\) conditions, but neither coherence nor those conditions are inferred from amenability or torsion-freeness.
The text correctly separates the classical tensor construction from the additional finiteness input.

### Infinite weakly exact resolutions

At each stage, the inclusion of \(Z_j\) into its prescribed ambient finite projective module, using \(B\) at the initial stage, represents the composite differential by a finite group-ring matrix.
The cited stacked-kernel argument identifies its Hilbert kernel with the closure of the algebraic next syzygy.
Density of the algebraic projective module in its Hilbert range identifies the outgoing image closure with the closure used to define \(z_j\).
Consequently dimension additivity gives \(z_{j+1}=p_j-z_j\), without requiring closed algebraic images or a new tensor-exactness hypothesis.
At the initial stage complete kernel density gives \(z_0=\nu(a)\).
Repeated substitution yields the displayed finite alternating-sum identity with sign \((-1)^N\) on the tail.

Since every \(p_j\) is an integer, even-indexed dimensions differ from \(\alpha\) by integers, while odd-indexed dimensions differ from \(-\alpha\) by integers.
Their nonnegativity and \(0<\alpha<1\) give exactly the stated lower bounds.
They therefore prevent any subsequence of syzygy dimensions from tending to zero under a hypothetical fractional initial dimension.
Termination also forces that initial dimension to be integral.
The equations alone allow a persistent fractional tail, so an infinite finitely generated projective resolution does not supply the missing finite Euler characteristic.
This is the precise limitation claimed, without an assertion that an actual counterexample or such a fractional resolution exists.

## Whole-section finding

No mathematical gap was found in the complete selected section under its explicit hypotheses and the declared kernel-density and established projective-trace inputs.
The projective-submodule certificate, the finite-cohomological-dimension certificate with its stated low-dimensional cases and \(FP_{d-2}\) assumption when \(d\ge2\), and the infinite-resolution tail calculation are valid at their stated scopes.
The nonzero-element premise, the cases \(d\le1\) and \(t=0\), arbitrary amenable groups, and the distinction between finite generation and finite projective dimension were all included in the inspection.

This finding supplies independent review of these conditional arguments and their direct interfaces.
It does not establish the missing extraction property, finite-generation conditions, coherence, a vanishing tail, a new class of groups satisfying the Atiyah conclusion, or the full Task.
It also does not replace the original source-proof audit limits of the accepted BCM04 input or supply independent coverage of the rest of C_A0001_v2.
