---
author: Yin
---

# Yin_C_F0011: Independent Full-Chain Review of the Scaled Model

Date: 2026-09-09.
Reviewer: the coordinating agent, independent of final author the reviewing agent.
Reviewed complete artifact: [Yin_C_F0011](../../claims/Yin_C_F0011_v1.md#yin_c_f0011).
The root proposed the factoriality diagnostic during discussion; this review separately read and checked the assembled proof, including all other conclusions.


## Review relationships

| Review | Relationship |
| --- | --- |
| [Actual complete finding](#scaled-model-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Actual complete finding](#scaled-model-finding) | [C_F0011 statement](../../claims/Yin_C_F0011_v1.md#statement) | Complete scaled model: relative-commutant/factoriality calculation, center recovery and cutoff generation, fixed-matrix fiberwise affiliated invertibility, bounded contraction observation, continuous-section obstruction to every bounded inverse representation, and absence of bounded duals. No refutation of the original bounded-dual conjecture or Task completion. |
| [Actual complete finding](#scaled-model-finding) | [C_F0011 argument](../../claims/Yin_C_F0011_v1.md#1-recovering-the-center-and-the-whole-tensor-product) | Complete scaled model: relative-commutant/factoriality calculation, center recovery and cutoff generation, fixed-matrix fiberwise affiliated invertibility, bounded contraction observation, continuous-section obstruction to every bounded inverse representation, and absence of bounded duals. No refutation of the original bounded-dual conjecture or Task completion. |

<a id="scaled-model-finding"></a>
The coordinating reviewer explicitly proposed the factoriality diagnostic during the same proof discussion.
This substantive contribution/shared mathematical context makes the whole assembled finding self-reviewed; it does not remove the actual complete proof checks.
The original inspection date, computations, source limits and independent wording remain historical facts; this declaration maintenance performs no new review and does not infer a relationship from C's retired aggregate field.

## Complete-Chain Checks

1. The relative commutant is computed in the ambient tensor product before identifying N with B.
   The two fiber equations share a conull set and t is nonzero there.
   Factoriality of the unscaled semicircular algebra therefore gives scalar fibers.
   No factoriality of the scaled tuple is assumed.
2. The convex-hull minimizer is bounded and belongs to N: positive convex combinations remain between 0 and 4, a weak-* subnet stays in that order interval, and L2 pairings identify its limit with the minimizer.
   Unitary invariance now gives a bounded central element.
   The fiber trace is a conjugation-invariant L2 contraction, so that element is t².
   Bounded cutoff recovery then proves N=B.
   Full support guarantees a nonconstant center; only nonatomic measures guarantee a diffuse center.
3. Fixing each full polynomial matrix first avoids an uncountable-conull-set error.
   Scalar scaling is an automorphism preserving fullness at each positive t.
   The accepted semicircular free-field input gives injective fibers; the direct-integral kernel is zero.
   In the finite algebra the polar final support is also one, giving the required affiliated inverse.
   The hypotheses of the audited MSY23 full-matrix criterion are now all met.
4. The contraction on Ran(Q^1/2) is well-defined and bounded by S1² <= Q.
   It commutes with the commutant on that dense range, so its extension belongs to M0.
   The two adjoint factor identities hold in M0.
   Support(Q)=1 makes the cancellation in U(M0) legitimate and gives g=C*C.
   Central cancellation of t in U(B) gives the bounded constant section f=g.
   Algebraic freeness excludes its being scalar, including zero.
5. Norm-continuous sections embed isometrically because every relative neighborhood, including ones approaching zero, has positive measure.
   The scalar value condition at zero is closed under all C*-operations, and the generators satisfy it.
   The nonscalar constant g fails that condition.
   The explicit positive Neumann argument proves inverse closure at every matrix size.
   Thus f is excluded from the scalar division closure and from every polynomial bounded-inverse matrix representation, regardless of size or minimality.
6. The bounded-dual exclusion uses selfadjointness, the exact skew-adjoint/source-dual conversion, and the accepted [Dab10-U001](../literature/Dab10/Yin_U001.md#dab10-u001) factoriality theorem with two generators.
   Its n>=2 qualification is essential and satisfied.
   The nontrivial center contradicts that consequence.
   This does not assert anything about a finite-rank class for nonexistent duals.

## Dependencies, Outcome, and Limits

The semicircular Fock/free-field interfaces, finite affiliated calculus, and exact Dab10/Voi98 theorem interface are resolved at the declared source-review depths.
The proof has no dependency on Yin_C_F0001's converse, no bounded inverse inferred from fiberwise injectivity, and no division-closure claim justified by a norm limit.
Norm closure is used only for the separate containing C*-algebra.
The contraction factor and continuous-section argument were reconstructed directly.
The unscaled factoriality input does not depend on the scaled conclusion.

**Pass: Yin_C_F0011 is proved / independently reviewed.**
It refutes the stronger bounded-descent assertion under free-field embedding alone and proves that this particular scaled model has no bounded duals.
It therefore does not refute Yin_C_F0001 and does not, by itself, complete Yin_T_F0001.
The full-support atomic boundary, support-dependent affiliated products, strong cutoff limits, and universal representation quantifier were checked.
No numerical experiment, proof assistant, external human review, or literature-priority assessment was performed.
