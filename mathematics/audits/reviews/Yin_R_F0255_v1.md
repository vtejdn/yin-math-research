---
author: Yin
---

# Independent review of the column bound for graphs with slope of bounded variation

An independent agent for Yin examined the [candidate decision of 2026-11-14T11:00](../../claims/Yin_C_F0246_v1.md#decision-candidate), its entire statement and proof, and the direct inputs at the scopes below.
The reviewer took no part in developing the proof and received only the fixed target and review assignment.
The reviewer formed the finding without exploration notes, development dialogue, author explanations or prior opinions on this candidate.

## Finding

At 2026-11-14T11:03 UTC the reviewer found that the argument establishes the stated \(A(1+V)\|\xi\|_2\) bound with an absolute \(A\), the actual vacuum, both canonical domains and the generator-first commutator for the specified coordinate.
The finding supports acceptance of the entire candidate, including its simultaneous application to correlated selfadjoint tuples.

For the old real coordinate, the disjoint interval estimate bounds the cubed \(L^3\) norms of the histograms by an absolute constant times \(\|\mathbb E_{W^*(S)}\xi\|_2^2\).
Testing against continuous functions identifies any weak \(L^3\) limit with the spectral law.
The old inverse-gap energy is exactly \(\|\xi-\mathbb E_{W^*(S)}\xi\|_2^2\).
Relabelling preserves the marginal algebras, the liberation vacuum and its prescribed inner difference, while \(|h(s)-h(t)|\ge |s-t|\) controls the transformed energy.
The scalar Lipschitz-graph criterion supplies the other input for existence of the target vacuum.
Its Lipschitz-dependent singular-integral norm is used only for existence and never enters the claimed column constant.
At the real coordinate every starred generator has derivative either zero or \(1\otimes1\).
The resulting derivation and its extension killing the two free Haar factors are real, algebraic and coassociative by the product rule, with the original vacuum.
I checked Definition 4.8 and (4.11) of Theorem 4.9 on p. 26 of Mai's arXiv:1512.07593v2 against this use.
Its factor two and the factor two in the norm of the encoded column give \(c(C\delta)\le4\|\xi\|_2\).

For a vertex strictly between the arguments, \(J_b=-i|s-b|/[q(t)(h(s)-h(t))]\) in both orientations.
Averaging \(m(t)-m(v)\) over the interval gives \(-\operatorname{sign}(s-t)\int_{\min(s,t)}^{\max(s,t)} |s-b|\,dm(b)/|s-t|\) when both endpoints are continuity points of \(m\).
This recovers (5), including the reversed orientation and the second-leg reciprocal \(q(t)^{-1}\).
The omitted endpoint and jump lines have product measure zero, and \(|J_b|\le1\) independently of \(m\).

For each \(b\), the two pieces of \(\sum_j d_j^2\) use different measures.
The liberation term sums against \(d\nu_\eta\), with zero diagonal mass and \(\sum_{|s-t|\le2r_j} r_j^{-2}\le(16/3)|s-t|^{-2}\) off the diagonal.
The mass term uses the disjoint real shells and Hölder, followed by convolution with the summable weights \(2^{-2n/3}\) on \(\ell^3\).
Both estimates are uniform in \(b\) and in the length of the interval.
On each rectangle the real parts of the two Laplace exponents supply the sum of the two distances from \(b\).
Multiplying the resulting bound \(r_j/(x_{\min}+y_{\min})^2\) by the localized liberation cost gives an absolute multiple of \(d_j\) for \(0<y\le r_j\), and of \(2^{k-j}d_k\) for the larger shell \(k<j\).
For separated factors the product rule includes the term \(pG(w)\), controlled on the whole column by \(\|\sum p_k^*p_k\|^{1/2}\|G(w)\|_2\).
Uniformly bounded polynomial approximation in the liberation graph justifies this step for measurable \(w\), including the Borel shell cutoffs.
The outputs retain their first-leg projection on the right, so traciality gives Hilbert orthogonality across first shells and orientations.
Summation with \(2^{-n}\) on \(\ell^2\) and bounded convergence in the coarse inner spectral measure now bound each vertex by an absolute multiple of \(\|\xi\|_2\).

On each tested coarse vector joint Borel measurability gives a strongly measurable integral in its separable cyclic spectral subspace.
The finite signed measure \(dm\) therefore contributes at most \(V\) times the uniform vertex cost, also for atoms and singular continuous variation.
The constant symbol in the first leg paired with \(q(t)^{-1}\) costs at most \(2c(C\delta)\) since \(|q|\ge1\).
These bounds are independent of the baseline slope, the number of vertices and the number of column entries.
On the target mixed core \(I_K\bar\delta\) has the required generator values.
The bounded graph approximants for each column, with their joint norm cut off at \(1+\varepsilon\), transfer the estimate because \(|K|\le1\).
The omitted relabellings may be bounded Borel functions that are one-to-one with Borel inverse on their conull images.
Replacing \(g\) by \(-g\) preserves the constants and gives the left-slice bound by flip-adjoint and tracial involution.
The two-slice theorem applies to the weakly dense represented core and its actual canonical operator.
The bounded term in the core commutator extends across its graph closure, giving \([Y_j,-\bar E]=\delta_{ij}P_\Omega\) on the closure domain and in particular on \(M\Omega\).
Applying the distinguished result separately at each coordinate proves the simultaneous claim.
For a piecewise affine graph \(V\) is the sum of the interior jump magnitudes, giving \(V\le2|a|\) for \(g(s)=a|s|\).
The review checked the cited interfaces and used the established input theorems at those scopes, without a fresh proof audit of the external theorems.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0246_v1.md#decision-candidate) | Entire fixed candidate and its stated applications. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0246_v1.md#statement) | Actual vacuum, both oriented mixed-column bounds, domains, commutator, simultaneous changes and the stated BV examples. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0246_v1.md#argument) | Old norm and energy, secant expansion, vertex rectangles, both shell summations, signed integration, transfer and domain conclusions. |
| [Finding](#finding) | [ACSY and strong-domain conventions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual vacuum on the represented starred core and the sign and domains of the generator-first commutator. |
| [Finding](#finding) | [Marginal packing](../../claims/Yin_C_F0233_v1.md#statement) | Part 1 for disjoint interval projections and their individual centers gives uniform cubed histogram bounds. |
| [Finding](#finding) | [Inverse-gap identity and criterion](../../claims/Yin_C_F0238_v1.md#statement) | Old energy relative to the projected vacuum and existence of the target vacuum from its scalar and liberation data. |
| [Finding](#finding) | [Coarse spectral measures](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination for shell limits and integrated multipliers, and zero diagonal liberation mass. |
| [Finding](#finding) | [Invariant liberation](../../claims/Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Bounded marginal graph extension, preserved vacuum and pushforward of its joint measure. |
| [Finding](#finding) | [Scalar graph criterion](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Sufficiency of a compact real \(L^3\) probability density for a scalar actual vacuum on either graph. |
| [Finding](#finding) | [Normal derivative formulas](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, forced starred values, and real algebraic old derivation at the selfadjoint coordinate. |
| [Finding](#finding) | [Free extension](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual old vacuum on the free extension by two Haar generators with zero derivative there. |
| [Finding](#finding) | [Haar column encoding](../../claims/Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Equation (5), exact output orthogonality and at most twice the old input column norm. |
| [Finding](#finding) | [Mai's contraction theorem](../literature/Mai15/Yin_U002.md#mai15-u002) | Definition 4.8 and Theorem 4.9, inequality (4.11), in arXiv:1512.07593v2 on the enlarged real algebraic core. |
| [Finding](#finding) | [Measurable product identity](../../claims/Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Equations (2) and (3) bound the separated term with the measurable reciprocal slope on the second leg. |
| [Finding](#finding) | [Localized liberation estimate](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6) for orthogonal spectral projections with their union under the appropriate centered ball. |
| [Finding](#finding) | [Marginal liberation graph](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Bounded marginal approximation extends the product identity on each fixed projected liberation graph. |
| [Finding](#finding) | [Target mixed-core approximation](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Generator identification, zero omitted derivatives and one joint norm cutoff for finite graph-approximating columns. |
| [Finding](#finding) | [Two-slice domain theorem](../../claims/Yin_C_F0072_v1.md#statement) | Part B for the canonical closure and its actual Hilbert adjoint, using single-input bounds in both orientations. |
