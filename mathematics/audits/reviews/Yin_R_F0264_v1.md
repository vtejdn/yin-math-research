---
author: Yin
---

# Independent review of the maximal-density criterion for a normal vacuum

I reviewed the complete [candidate fixed at 2026-11-14T11:56](../../claims/Yin_C_F0255_v1.md#decision-candidate) for Yin.
I had previously used the scalar soft-energy, column and optimal-density results in work on changes of coordinates.
I took no part in developing the present maximal-density criterion or its proof.
I first saw its four-grid compression argument in the fixed candidate.
Before reaching this finding I used the candidate and its mathematical inputs, without consulting its development dialogue, drafts, author explanations or previous review conclusions.

## Whole-proof finding

At 2026-11-14T11:59 UTC I found that the proof establishes the scalar equivalence with absolute norm comparison, both original scalar bounded-vector domains, and the stated three-condition characterization on the mixed starred core.

An actual scalar starred derivation at \(Z\) is a one-coordinate instance of the normal phase theorem.
It forces diffuseness and its values on both generators agree with the divided difference.
The Leibniz rule gives the same conclusion on every represented starred polynomial.
The bound \(c\le12\|\xi_\mu\|_2\) is the one-coordinate bound in the proof of C_F0233, obtained there from the freely enlarged scalar estimate.
It concerns the finite column constant required in C_F0211, so that theorem supplies a single density \(d\) of mass one with integrable reciprocal, and an attained bounded implementer of norm \(c\).

In the compression by the multiplication projection \(P_Q\), \(Z-\lambda\) commutes with \(P_Q\) and has norm at most \(\ell/\sqrt2\) on its range.
The compressed commutator is the difference of two operators of norm at most \(c\ell/\sqrt2\), and equals the rank-one operator with vectors \(1_Q\) and \(1_Q d^{-1/2}\).
This yields \(\mu(Q)\langle d^{-1}\rangle_Q^{1/2}\le\sqrt2 c\ell\).
Jensen gives \(\langle d^{-1}\rangle_Q\ge\langle\sqrt d\rangle_Q^{-2}\), in the direction needed to dominate the density ratio by the average of \(\sqrt d\).
The uncompressed rank-one norm is \(\|d^{-1/2}\|_2\ge1\), by Cauchy–Schwarz with \(\sqrt d\) and \(\int d\,d\mu=1\).
Taking a support point as center gives \(\|d^{-1/2}\|_2\le2cD\), covering all radii greater than \(D\).

With \(L=16D\), the dyadic scales \(L2^{-j}\), \(j\ge0\), contain a unique member in \([8r,16r)\) for each \(0<r\le D\).
In each axis the two endpoint lattices differ by \(L/3\), whose residue is either one third or two thirds of a lattice spacing at every selected scale.
An interval of length \(2r\le\ell_j/4\) therefore misses the boundary of at least one grid completely, even for closed balls and masses on square edges.
The independent choices in the two axes give four square filtrations, each nested across scales since its translation is fixed.
A positive ball about a support point is contained in a positive-mass square that also contains the point.
For a filtration the maximal averages through depth \(n\) satisfy the displayed weak estimate by disjoint first-crossing squares, including their possibly countably many squares at the starting scale.
Layer-cake integration yields the strong bound \(2\|\sqrt d\|_2=2\), first at finite depth where the maximum of the finitely many conditional expectations is square-integrable, then in the limit.
Squaring the maximum over four filtrations costs at most the sum of the four squared maximal functions.
For example \(\int(M_1\mu)^2\,d\mu\le(4+8192)c^2\) follows, including the large radii.

For the curvature term, the limit of the positive soft energy away from collisions is half the squared Menger curvature.
Fatou and the soft triple-integral bound \(3\|\xi_\mu\|_2^2\) give precisely the coefficient six stated in the candidate.
Conversely any atom gives infinite maximal density at a point of positive measure.
For a diffuse law the double difference defines a represented coarse-valued outer derivation on the dense starred marginal polynomials and satisfies \(\delta Z=1\otimes1\).
Its pairing with \(1\otimes1\) equals the scalar integral of the original right slice \(E_0p\).
Thus \(E_0^*1\) supplied by part A of C_F0053 is also the actual vacuum adjoint of that derivation.
The bound there is \(2\sqrt{K_0G(\mu)}\) for its norm, and both bounded-vector inclusions are for the closure and actual adjoint of the original polynomial slice.
I checked the Tolsa–Verdera input at its recorded interface in C_F0053, namely the truncated Cauchy estimate for positive measures with both finite energy terms.

For the forward joint implication C_F0238 supplies all three required coordinate conditions except the reformulation of the scalar vacuum, which the preceding scalar equivalence provides.
For the reverse implication finiteness of each \(G(\mu_i)\) gives both diffuseness and its actual scalar vacuum.
The represented liberation derivation and its actual vacuum are required separately at each \(i\).
Its inverse-gap integral has precisely the off-diagonal left-right spectral measure used in C_F0238.
The latter theorem supplies the mixed-core actual derivation and the orthogonal squared norm \(\|\xi_{\mu_i}\|_2^2+I_i\).
The comparison constants for \(G+I_i\) can therefore be taken as \(\min(1,a)\) and \(\max(1,A)\) from the scalar comparison.
The bounded-vector domain conclusion of this candidate concerns the scalar slice.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Fixed candidate](../../claims/Yin_C_F0255_v1.md#decision-candidate) | Scalar geometric equivalence, norm comparison, both scalar domains and the mixed recovery statement fixed on November 14. |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0255_v1.md#statement) | Compact planar probabilities with or without atoms, absolute constants, original scalar domains and all coordinates of finite correlated normal tuples. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0255_v1.md#argument) | Optimal-density compression, Jensen, four translated grids and maximal estimate, curvature and scalar-domain converse, joint orthogonal decomposition. |
| [Whole-proof finding](#whole-proof-finding) | [Normal marginal formulas](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, actual scalar diffuseness and starred marginal difference quotient on the represented algebra. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar column bound](../../claims/Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) | The one-coordinate finite-column constant is at most twelve times the actual scalar vacuum norm. |
| [Whole-proof finding](#whole-proof-finding) | [Optimal commutator](../../claims/Yin_C_F0211_v1.md#statement) | The attained rank-one commutator for the same finite column constant, its normalized faithful density and integrable reciprocal. |
| [Whole-proof finding](#whole-proof-finding) | [Vacuum-to-curvature estimate](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Fatou applied to the positive soft energy bounds curvature with constant six. |
| [Whole-proof finding](#whole-proof-finding) | [Geometric scalar theorem](../../claims/Yin_C_F0053_v1.md#maximal-density-cauchy-core-transfer) | Part A, finite geometric energy gives the actual scalar vacuum, quantitative bound and the two original bounded-vector domains. |
| [Whole-proof finding](#whole-proof-finding) | [Joint recovery](../../claims/Yin_C_F0238_v1.md#statement) | Both directions on the original mixed starred algebra and equation (1) for the actual joint vacuum norm. |
| [Whole-proof finding](#whole-proof-finding) | [Truncated Cauchy estimate](../literature/TV06/Yin_U001.md#tv06-u001) | The accepted Theorem 2 bound used inside the converse of C_F0053, at statement and hypothesis scope. |
