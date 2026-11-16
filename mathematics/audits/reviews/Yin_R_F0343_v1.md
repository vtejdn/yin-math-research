---
author: Yin
---

# Independent review of positive endpoint costs in a normal Gaussian pair

## Finding

On 2026-11-16T19:14 UTC a reviewer outside this candidate's proof development independently checked the [candidate decision](../../claims/Yin_C_F0338_v1.md#decision-candidate) dated 2026-11-16T19:10, the whole statement and argument, and all eight declared dependency targets.
The reviewer received the fixed candidate without its development discussion or a prior finding on it.
The proof establishes the stated example, including the actual spectral measure in the generated algebra, the cost estimates for all countable partitions, and the failure of both proposed domination hypotheses.

At scale \(4^{-n}\), one Cantor cylinder gives the lower bound and a bounded number suffice for the upper bound on the vertical ball mass, with each cylinder of mass \(2^{-n}\).
The product with the horizontal interval has ball mass comparable to \(r^{3/2}\) on \(K_0\), also at boundary points; the upper bound at arbitrary centers follows by doubling the radius at an intersection point.
The dyadic contribution to squared density is \(O(r)\), and for fixed first vertex the curvature on a triple of diameter comparable to \(r\) costs at most \(O(r^{-2})\) times two ball masses, again \(O(r)\).
The separated segment law has finite scalar energy by the cited construction; on mixed triples the squared curvature is bounded by \(4/\operatorname{dist}(K_0,\operatorname{supp}\sigma')^2\), and the other component also adds only a bounded maximal linear density on either support.
Thus the mixed probability is diffuse and compact with an actual scalar vacuum, while its line-segment interiors of positive mass force divergence of the tail of \(W\).
The negative segment-pair Rayleigh quotients are multiplied by \(1/4\) for their original third vertices after normalization in the mixed probability.
The other third vertices add a uniformly bounded kernel on the pair, hence a uniformly bounded error on Hilbert unit vectors.
For every sufficiently small disk meeting \(K_0\), its triple enlargement contains a ball centered there of radius \(r\), while the near-component annuli in \(T(B)\) sum to \(O(r^{3/2}\sum_{j\ge0}2^{-j/2})\) and the separated component contributes \(O(r^2)\).
The disk reduction permits increasing its absolute threshold, which places these disks on the asserted side.

The symmetric positive amplitude and its reciprocal are bounded, so the one-color Gaussian field has a finite row bound, full rank and finite inverse-amplitude integral.
On \(K_0^2\), only the half of the middle-variable law on \(K_0\) contributes: the squared difference of the two ratios is \(4\sinh^2\) of the difference of translates of \(g\).
The horizontal marginal there is uniform.
Orthogonality gives the stated sum of squared sines for the squared translation distance, with coefficient \(2\); choosing \(2^nd\in[1/4,1/2]\) gives the lower power \(d^{3/4}\), and splitting the two geometric tails gives the matching upper bound.
Since circular horizontal distance is at most planar distance, the divided square on \(K_0^2\) is bounded by \(C|z-v|^{-5/4}\), of cost \(O(r^{1/4})\) per small annulus.
Across the fixed gap this ratio is bounded, and with both endpoints in the segment component its numerator vanishes for every middle variable.
The Gaussian theorem therefore gives actual starred conjugate variables, finite original slice costs and both bounded-vector domains at both coordinates with the intrinsic trace.
In the commutator the scalar part of the \(Z\)-vacuum cancels, and \(-i(\bar z-\bar v)\) on the second chaos cancels the denominator of its path coefficient.
The phase has modulus one, left and right projections select the two endpoints, and their diagonal has zero product mass by diffuseness.
Integration of the squared remaining numerator in the middle variable gives exactly \(\nu=H\mu^2\), including the mixed rectangles.

For any cell of mass \(s>0\) in \(K_0\), the circular horizontal arc of radius \(s/4\) at any one point has \(\mu_0\)-mass \(s/2\).
It follows that at least \(s^2/2\) of the cell square has distance at least \(s/4\), giving a normalized square mass at least \(cs^{3/4}\).
Product absolute continuity permits partitions modulo \(\mu\), and summing the cell bounds gives both \(ct^{3/4}\) and \(ct/(\sup_i t_i)^{1/4}\).
Summing the optimal lower bounds for \(n\) disjoint strips of equal mixed mass \(1/(2n)\) grows at least as \(n^{1/4}\); a single finite control measure cannot dominate this sum on \(K_0\).
The subdivision consequence of ball domination requires only its density hypothesis, so this rules it out even without testing mixed curvature integrability.
A countable small-squared-diameter cover of a conull feature image, assigned by first preimages on any positive-mass subset, would make its infimal partition cost zero, contradicting the lower bound independently of secant energy.
These obstructions concern the separate endpoint estimate and do not imply failure of signed slice bounds or of the strong domain condition.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0338_v1.md#decision-candidate) | Fixed candidate and all directly selected mathematical inputs at the reviewed revision. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0338_v1.md#statement) | Both actual systems, quantitative partition obstruction, both domination exclusions, disk and marginal conclusions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0338_v1.md#argument) | Whole proof, including the model, exact spectral density, weighted component and all partition quantifiers. |
| [Finding](#finding) | [Gaussian theorem](../../claims/Yin_C_F0209_v1.md#statement) | One positive scalar amplitude, row and inverse tests, intrinsic two-edge coefficient, actual slices and domains at both coordinates. |
| [Finding](#finding) | [Liberation commutator](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Real normalization and endpoint action on the scalar and second-chaos vacuum components. |
| [Finding](#finding) | [Scalar vacuum criterion](../../claims/Yin_C_F0255_v1.md#statement) | Maximal density and total squared curvature of the diffuse compact mixed law. |
| [Finding](#finding) | [Segment pair construction](../../claims/Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions) | Separated probability, scalar energy, positive arclength densities and negative divergent signed tests. |
| [Finding](#finding) | [Endpoint subdivision](../../claims/Yin_C_F0332_v1.md#subdivision-by-cubes) | Ball-mass hypothesis implies the partition upper bound on each Borel set. |
| [Finding](#finding) | [Feature covers](../../claims/Yin_C_F0337_v1.md#the-remaining-disks-under-feature-domination) | Squared-diameter covers force zero infimal endpoint cost on any conull restriction. |
| [Finding](#finding) | [Disk reduction](../../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) | Threshold definition and permissible enlargement of its absolute constant. |
| [Finding](#finding) | [Averaged squared density](../../claims/Yin_C_F0297_v1.md#statement) | Exact dyadic functional for the normalized product law and for the entire probability. |
| [Finding](#finding) | [F0011 contract](../../tasks/Yin_T_F0011_v1.md#contract) | Scope of represented starred conjugacy and the full bounded-vector and adjoint conditions. |
