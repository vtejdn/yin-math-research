---
author: Yin
---
# Independent review of the spectral-chain tensor argument

Review time: 2026-11-10T15:24 (UTC).
Human record author: Yin.

The reviewer independently inspected the complete [statement](../../claims/Yin_C_A0002_v1.md#statement), [argument](../../claims/Yin_C_A0002_v1.md#argument), and [source corrections and scope](../../claims/Yin_C_A0002_v1.md#source-corrections-and-scope) of Yin_C_A0002_v1 in its 10 November 2026 working revision.
The review covers the chain-cutoff construction, bounded injectivity on completed Hilbert tensor products, the dimension limit, the denominator-cleared centralizer inclusion, and matrix amplification.
The reviewed mathematical sections were held unchanged during this inspection.

## Arrangement and inputs

The reviewer did not participate in substantive development of the proof and received the fixed Claim, requested review scope, repository instructions, and operational metadata directly.
No proof-generation dialogue, development summary, author explanation, or previous review conclusion was supplied or consulted before the initial findings.
The Claim's own derivation-context paragraph was visible as part of the direct review input; no underlying conversation or helper report was supplied.
The reviewer formed the initial findings from the Claim and the original mathematical source, without relying on the existing source unit's assessments or any other project review.
The later reading of the journal-edition entrance was limited to identifying the retained edition and its page correspondence.
No substantive repair to the Claim was contributed by this reviewer.

The inspected primary source is the [retained JZ19 journal edition](../literature/JZ19/readme.md#journal-edition).
The reviewer read printed pp. 476–477 for Section 3.2, pp. 521–523 for the finite-module and Hilbert–Schmidt conventions, pp. 525–527 for the target statement and printed proof, and the opening of p. 528 for the stated consequence.
The six specified pages 521–523 and 525–527 were also inspected as rendered page images to verify the displayed formulas, indices, conjugates, and literal hypotheses.
Printed page numbers equal the PDF page numbers plus 463.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0002_v1.md#statement) | Entire statement, including arbitrary admissible cutoff choices, the finite-family limit, centralizer consequence, and unnormalized matrix amplification. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0002_v1.md#argument) | Complete argument and every domain, closure, tensor-completion, dimension, and source-use interface. |
| [Whole-argument finding](#whole-argument-finding) | [Source corrections and scope](../../claims/Yin_C_A0002_v1.md#source-corrections-and-scope) | Distinctness correction, repeated-parameter counterexample, corrected codomain, and the stated limits of the result. |

## Domain and closure checks

The affiliated powers are consistently interpreted as closed products in the finite affiliated algebra.
The argument does not infer ordinary iterated domain membership merely from membership in the kernel of such a power.
The spectral projection used in the cutoff construction has range in the domain of the closed operator, and the bounded map with coordinates given by the successive powers of the truncated operator has exactly the finite target dimension used in the loss estimate.
Its kernel therefore has the asserted dimension and puts every required intermediate vector inside the same spectral cutoff.
The displayed induction proves actual successive applications through order $j+1$, with a uniform bound on each relevant image.
The ordinary iterates agree with the affiliated powers because each ordinary product is contained in the corresponding closed affiliated product.
After the highest required shifted iterate vanishes, the finite chain span is invariant and lies in the operator domain, which justifies arbitrary later polynomial applications on those individual vectors.
The same construction applies to the adjoint.

Polar decomposition applies to each closed affiliated power in the same finite algebra.
Its initial and final support projections have equal trace, so the kernel dimensions for the power and its adjoint agree.
The adjoint of the affiliated power is the corresponding closed adjoint power, and subtraction of successive kernel dimensions gives exactly the required adjoint-layer equality.
The nested-kernel assertion follows from the affiliated algebra identity with the kernel projection; it introduces no assumption about ordinary powers outside the constructed cutoffs.

The left bounded denominator of an affiliated polynomial is injective, and the numerator is bounded by the stated polar-decomposition functional calculus.
The numerator agrees with the denominator followed by the polynomial only on the polynomial's domain, which is precisely how the proof uses it.
No unbounded operator is applied to an arbitrary vector in a completed tensor product.

## Injectivity and dimension checks

Each chain term is a tensor product of bounded maps on the declared closed cutoff spaces, so it extends to the Hilbert completion.
For a single spectral parameter, projection of the second factor onto the highest layer kills every lower-level contribution and every shifted second factor at that highest level.
The sole remaining map is the tensor product of the highest adjoint iterate and the inclusion of the highest cutoff space.
The adjoint iterate has zero kernel on that layer, even if its range is not closed.
The dense ranges of the two adjoints prove injectivity of their completed tensor product without a lower norm bound.
Finite descending induction then eliminates all levels.

For distinct spectral parameters, the Chinese-remainder congruences hold to the maximal level needed for each primary chain.
Their polynomial action on every elementary second factor is justified by the preceding actual-domain argument.
Multiplying by the bounded left denominator turns that action into an identity between bounded maps on the full completed source.
Continuity extends the identity from elementary tensors, and injectivity of the denominator tensor identity isolates each spectral parameter.
The single-parameter argument then proves the asserted injectivity.
No closed direct-sum decomposition of generalized eigenspaces is assumed.

The codomain is the full Hilbert tensor product, and the closed image is used only after the bounded map has been defined and shown injective.
Finite-module dimension additivity and the tensor product trace give the exact dimension formula.
For any choices satisfying the stated bounds, each cutoff dimension lies between $\max(0,d_{\lambda,j}-\varepsilon)$ and $d_{\lambda,j}$.
The finite squeeze therefore proves the claimed limit without nesting or continuity of the cutoff choices.
Taking the supremum over finite spectral families and finite levels gives every finite subsum in the final nonnegative series; no countability or enumeration assumption on the point spectrum is needed for that passage.

## Centralizer and matrix checks

For an elementary chain pair, the finite-rank operator has range in the domain of $A$, while all vectors defining its coefficient functionals lie in the domain of $A^*$.
Thus the two compositions used in the telescoping identity have bounded extensions on precisely the domains asserted in the Claim.
The conjugate scalar in the adjoint chain is consistent with the inner product being linear in its first variable.
The telescoping boundary terms vanish by the actual terminal chain identities.

The chosen right denominator has range in the domain of $A$, and the left denominator gives the stated bounded numerator on that domain.
This proves the denominator-cleared equality for each elementary finite-rank image.
Left and right multiplication by bounded operators are bounded on Hilbert–Schmidt space, so their difference has a closed kernel containing the full closed tensor image.
This agrees with the source's centralizer definition on pp. 522–523 and avoids an unjustified closure argument for the raw unbounded commutator.

Replacing $X$ by its product with a finite $n$-point set preserves freeness and finite orbit count and identifies the affiliated matrix algebra with the corresponding amplified operator algebra.
The Hilbert–Schmidt space is the matrix space over the original Hilbert–Schmidt space.
The $H$-module dimension is $n|H\backslash X|$, and the ambient $H\times H$-module dimension is its square.
Consequently the layer dimensions and the centralizer lower bound have the unnormalized matrix convention used in Proposition 9.9.
No factor of $n$ or $n^2$ is lost.

## Source match and accepted foundations

The printed Lemma 9.10(2) on p. 527 lists spectral parameters without an explicit distinctness condition.
The Claim's scalar zero-operator example satisfies the printed hypotheses and gives left side $1$ and right side $2$ when a parameter is repeated.
It is therefore a valid counterexample to the literal unrestricted formula.
Restricting to distinct parameters is sufficient for Proposition 9.9, whose series is over different elements of the point spectrum.
Allowing nonnegative maximal levels in the Claim adds the valid level-zero case.

The source only requires boundedness along the cutoff chains on p. 526; those conditions do not require the chain images to remain in the selected cutoff subspaces.
The proposed cutoff-space tensor codomain on p. 527 therefore needs justification not supplied by those hypotheses.
The Claim's full-space codomain and bounded-map argument establish the required dimension result without that assertion.
The source's later statement that Proposition 9.9 follows from the lemma is matched by the separately checked centralizer inclusion and finite-subsum passage.
Neither Lemma 9.10(2) nor Proposition 9.9 is used as a premise of the local proof.

The review accepts the standard closed affiliated-operator algebra, spectral calculus, polar decomposition, and finite Hilbert-module dimension as foundational inputs at the scope explicitly declared in the Claim.
Section 3.2 supplies the affiliated-algebra setting, and Section 9.1 supplies the group-module trace, Hilbert–Schmidt identification, and denominator-cleared centralizer definition.
Proposition 9.1 supplies the weak-exact dimension additivity used for bounded equivariant maps.
The product-dimension formula is also directly consistent with the product of the two projection traces under that identification.
The applications of these inputs, including finite trace, equivariance, closed kernels, and closed image targets, were checked individually.
The underlying proofs of spectral theory, the affiliated-algebra construction, and the cited Lück dimension theorem were not recursively re-audited.
JZ19's Corollary 9.4 and its unbounded tensor embedding calculation are not necessary inputs to this local argument.

## Whole-argument finding

The complete reviewed argument establishes the exact corrected statement of Yin_C_A0002_v1 under its declared standard foundations.
No unresolved mathematical gap was found in the cutoff construction, tensor injectivity, dimension limit, centralizer consequence, or matrix amplification.
This independently reviewed finding supports acceptance of the Claim's full stated result and its reconstruction of the distinct-parameter form of JZ19 Lemma 9.10(2).

The review does not establish the literal repeated-parameter source formula, which is false as explained above.
It does not review the remaining proof of JZ19, its coefficient-change theorems, or the complex Atiyah conjecture for arbitrary torsion-free groups.
It is a mathematical proof review, not formal verification or a computational certificate.
Later substantive changes to the reviewed statement, argument, or source-use interfaces require review at their actual changed scope.
