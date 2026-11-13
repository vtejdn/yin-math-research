---
author: Yin
---
# Independent review of the matrix covariance criterion

## Scope

At 2026-11-13T13:46 UTC, a reviewer outside proof development inspected the statement and whole argument of [C_F0209 v1](../../claims/Yin_C_F0209_v1.md#argument) in the fixed working revision whose candidate decision is dated 2026-11-13T13:40.
The initial review used the claim, the Task's definitions and the mathematical inputs bound below.
The reviewer received no exploration notes, proof-development dialogue, author explanations or prior review conclusions about this claim.
The existing input theorems were checked at the invoked interfaces, including the scope of the recorded semicircular moment formula.

## Conclusion

The proof establishes the row bound and the equivalence of the intrinsic starred ACSY condition, the strong full-domain dual condition and item 3 for the stated finite matrix of kernels.
The vacuum formulas, both original canonical domains and the noncommuting example follow at that scope.
The proof also gives the stated rank obstruction when the intrinsic generated algebra is smaller than the ambient algebra.

**Wick paths and the intrinsic space.**
Equal-color noncrossing pairings yield the orthogonal Wick paths, with one independent marginal \(L^2(\mu)\) factor per vertex.
The row creation norm on degree zero is the essential supremum of the fiber norm, and exactly the same fiber norm controls creation on every degree.
Edge reversal supplies selfadjointness, so entry truncation has a uniform field bound and converges strongly from tracial \(L^2\) convergence.
The one-field rectangle tests give \(A\bar h_i=e_i\) inside the ambient first chaos even for an intrinsic vacuum.
Summing the pointwise minimal squared solution norms gives \({\rm tr}(G^{-2})\).
For full row rank \(V^t\) is an isometry on each edge and intertwines both leading-edge operations on its range.
In the reduced model first-chaos density places each bounded reference semicircular in the generated algebra by conditional expectation.
This makes the isometry onto the original target cyclic space, so its induced unitary carries polynomial cores, closures and actual adjoints between the two intrinsic representations.

**Quadratic tests and order of factors.**
The normal relation determines the scalar divided difference of the base coordinate and forces the field-coordinate derivatives of \(Z^*\) to vanish.
The scalar compression therefore gives an actual marginal vacuum.
Smooth separated endpoint tests are valid on the original graph, since their uniform approximants control both the multipliers and their divided differences.
The squared norm of the two-edge polynomial path is integrable by the two row bounds at the common middle vertex.
The left endpoint derivative samples the covariance \(G(v,w)^2\), and the right endpoint derivative subtracts \(G(z,w)^2\).
Pairing the two-edge path against the vacuum puts \(G(w,v)^t=Q\) on the right of \(\bar h\).
The localized rectangle identity therefore gives \(P\bar hQ=(Q^2-P^2)/(z-v)\), including the order of both products in (2).

**Insertions and the full reference domains.**
With a fixed suffix length, the deleted color specifies orthogonal initial spaces, so summing the squared cut norms over colors costs at most \(\|p\|_2^2\).
Insertion at this split concatenates the two vertex tensors and places each inserted color in an orthogonal space.
Summing over splits costs only \(\sqrt{n+1}\), by Cauchy--Schwarz, for both the vacuum estimate and the traced-cut \(L^1\) estimate.
The latter puts bounded vectors in the actual Hilbert adjoint domain.
Applying the core Leibniz adjoint identity to the flip-star derivative gives the operator-norm-to-\(L^2\) bound for the original contraction, which passes to its closure on bounded vectors by bounded polynomial approximation and weak graph closure.
In the free lift only a terminal base letter contributes to the contraction of a reduced word, so the adjoint at the unit is the same marginal vacuum.

**Bounded matrices and measurable kernels.**
Applying the componentwise adjoint to (4) reverses the two vertices of the occupied leg.
For the second array its transpose changes the reversed product into \(PQ^{-1}\) inside the conjugation.
Writing \(U=P^{-1}Q\) gives \(PQ^{-1}=(U^*)^{-1}\), so the real cross term is \({\rm tr}(U)+{\rm tr}(U^{-1})-2q\).
The eigenvalues of \(U\) are positive by similarity to \(P^{-1/2}QP^{-1/2}\), proving the required bound on both separate coefficient norms.
Multiplication on the left by \(G(z,v)\) cancels the two differentiated kernel arrays entry by entry before taking the commutator.
For a bounded measurable entry the formal divided differences lie in \(L^2\) by these same products.
The parameterized identity (M6) evaluates the derivative of bounded polynomial approximants against each fixed algebraic test by moving the derivative to its adjoint there.
The correction tensors converge strongly by domination.
Consequently passage to the commutator requires only convergence of these fixed matrix elements, even if the approximating derivative norms grow.
The actual adjoint on each bounded test vector and the weakly closed graph on uniformly bounded approximants extend the commutators to the whole bounded domain.
For field coordinate \(j\), the degree-zero column \(G^{-1}e_j\) gives commutator \(P_\Omega\) in that channel and zero in the others, with the stated componentwise-conjugated vacuum.
Negation gives the Task's generator-first sign, and uniqueness of the starred derivation identifies the canonical contraction on target words and its vacuum by density.

**Clipping and the example.**
In the two separate spectral bases the matrix element of \(P^{-1}Q-PQ^{-1}\) has scalar factor \(\gamma_t/\lambda_s-\lambda_s/\gamma_t\), which proves (6) without simultaneous diagonalization.
Upper clipping contracts log distances, hence dominates the Hilbert--Schmidt norm of the clipped quotient by the original norm.
The inverse columns are likewise dominated in squared norm by \({\rm tr}(G^{-2})+q\).
The row bounds give a single operator cutoff and strong-star convergence of the fields in the fixed reduced model.
The uniform bounds for the contraction and its actual adjoint give bounded duals for both laws, the adjoint tuple using the operator-first witness \(-E'^*\).
The two closed norm sublevels then give strong duals at the limiting law, and the normal comparison theorems give the original canonical domains there.
On each target word the derivative terms multiply the same coarse vectors by strongly-star convergent bounded multipliers, so the limiting pairings identify the entire vacua.
On the unit disk, the absolute Cauchy integral is uniformly finite and the real-pencil example has eigenvalues \(1\pm|z+w|/16\).
Its endpoint difference is bounded by a constant times \(|z-v|\).
The commutator of its two covariances is nonzero when the two real coefficient vectors are independent, which occurs on a nonempty open set.
For a single noise and channel, the edge isometry multiplies by the phase of the kernel and gives the scalar vacuum formulas.
The unrestricted comparison for other correlated normal tuples remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [Matrix statement](../../claims/Yin_C_F0209_v1.md#statement) | Row bound, all three equivalent conditions, canonical domains and exact vacua in the stated class. |
| [Conclusion](#conclusion) | [Matrix argument](../../claims/Yin_C_F0209_v1.md#argument) | Whole argument from colored paths to the clipped limit and the two-channel example. |
| [Conclusion](#conclusion) | [Task contract](../../tasks/Yin_T_F0011_v1.md#contract) | Definitions, intrinsic coarse space, represented core, actual domains and generator-first signs only. |
| [Conclusion](#conclusion) | [Matching-color Wick rule](../literature/NS06/Yin_U004.md#ns06-u004) | Established mixed-moment formula with free base insertions and equal-color noncrossing pairs, at its recorded statement and applicability depth. |
| [Conclusion](#conclusion) | [Relative Wick recurrence](../../claims/Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) | Vertex Hilbert factors, creation, annihilation and the cut formula with the checked color restriction. |
| [Conclusion](#conclusion) | [Suffix cuts](../../claims/Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) | Right Wick coefficient expansion and the tracial product estimate summed over the actual color cuts. |
| [Conclusion](#conclusion) | [Actual adjoints](../../claims/Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound) | Vacuum test, actual Hilbert adjoint inclusion, flip-star Leibniz identity and original bounded-vector closure. |
| [Conclusion](#conclusion) | [Scalar estimate](../../claims/Yin_C_F0055_v1.md#statement) | Compact diffuse scalar marginal with actual vacuum gives the base contraction and adjoint bounds. |
| [Conclusion](#conclusion) | [Free lift](../../claims/Yin_C_F0045_v1.md#statement) | Free product of the base and reference semicircular coordinates lifts the normalized scalar bounds and vacuum. |
| [Conclusion](#conclusion) | [Original moment tests](../../claims/Yin_C_F0156_v1.md#actual-target-moment-tests) | Normal phase and separated smooth endpoint graph tests on bounded fields, with new mixed-color covariances checked here. |
| [Conclusion](#conclusion) | [Weak integration by parts](../../claims/Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) | Formula (M6) against polynomial tensor tests with one spectator variable and square-integrable formal leg derivative. |
| [Conclusion](#conclusion) | [One-field construction](../../claims/Yin_C_F0157_v2.md#argument) | Bounded separated-kernel field construction under reversal and the disk's scalar marginal vacuum. |
| [Conclusion](#conclusion) | [Scalar specialization](../../claims/Yin_C_F0157_v2.md#statement) | Positive-kernel quotient and phase transport agree for one channel and one noise. |
| [Conclusion](#conclusion) | [Closed law sublevels](../../claims/Yin_C_F0201_v2.md#statement) | Common operator cutoff, two bounded global dual norms and the normal two-sided test on the limit. |
| [Conclusion](#conclusion) | [Strong-to-ACSY implication](../../claims/Yin_C_F0070_v1.md#statement) | Normal strong duals supply the unique starred derivations on the target core and their actual vacua. |
| [Conclusion](#conclusion) | [Canonical comparison](../../claims/Yin_C_F0075_v1.md#statement) | Original normalized canonical closures and actual adjoints under the intrinsic normal strong hypothesis. |
