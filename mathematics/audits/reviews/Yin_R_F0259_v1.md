---
author: Yin
---

# Independent review of the canonical column estimate at a power-order tangency

For Yin, I reviewed the complete [candidate dated 2026-11-14T11:28](../../claims/Yin_C_F0250_v1.md#decision-candidate) and its direct mathematical inputs.
I took no part in developing this proof and received the fixed target without development dialogue, author explanations, exploration notes or previous findings about the candidate.

## Finding

At 2026-11-14T11:29 UTC I found that the proof establishes the finite original right-column estimate at the distinguished coordinate, the adjoint orientation, both canonical bounded-vector domains and the generator-first commutator under the stated hypotheses.
It covers arbitrary closed spectral subsets of the arcs, including a branch of zero spectral mass, and arbitrary correlations with the other normal generators.
The exponent and constants in the separation hypothesis are fixed for the carrier, and the column constant may depend on the geometry and the law.

For \(p=1/(\kappa-1)\), the mean value estimate for \(\ell_n\) lies between \(pR(n+1)^{-p-1}\) and \(pRn^{-p-1}\).
Together with \(p\kappa=p+1\) and \(n+1\le2n\) this gives uniform comparison with \(x^\kappa\) on the entire closed tile.
The two real assigned intervals have disjoint interiors, and the coding error in (3) is bounded by a fixed multiple of \(\ell_n\) on each.
The gap inside a tile has length \(2\ell_n\), and the gap across the next lower tile has length \(\ell_n+5\ell_{n+1}\).
The two respective pairs of decoded endpoints are separated by \(O(\ell_n)\), including the pair at the same \(x_{n+1}\) where the gap in the plane is \(2d(x_{n+1})\).
The uniform piecewise Lipschitz estimate extends to the whole hull by finite subdivision away from zero and continuity at zero.
The inverse encoding only uses the open assigned intervals with their countable endpoint images and the apex discarded by diffuseness.
Thus the decoding on the support is a conull Borel inverse even if a connecting line segment crosses an arc inside an unoccupied real gap.

On a mesh of width \(t\), the images of the occupied parts of distinct cells are disjoint, and each image lies in a disk of radius \(\operatorname{Lip}(h)t\).
The positive-weight packing inequality with individual centers therefore bounds the cubed \(L^3\) norms of the histograms.
Weak compactness and convergence against continuous functions give an \(L^3\) density of the real law and hence its scalar vacuum.
Both marginal spectral legs of the liberation vector ignore the discarded sets by normality.
Conull injectivity and the forward Lipschitz bound give \(|s-t|^{-2}\le\operatorname{Lip}(h)^2|h(s)-h(t)|^{-2}\) off the diagonal of this measure.
The omitted coordinates retain their marginal laws and liberation vacua since the distinguished marginal algebra is unchanged.
The inverse-gap criterion and the old real-coordinate estimate consequently apply to the whole represented parameter tuple.

On the cross rectangle \(x\in(r_j/2,r_j]\), \(y\le r_j/8\), the separated exponential factors for \(1/D\) have supremum product at most \(e^{-3\lambda r_j/8}\).
The error numerator in (4) has separated cost \(O(r_j^2+r_j^\kappa)\), since the midline has a horizontal tangent and bounded curvature and the height and coding errors are \(O(x^\kappa)\) or \(O(y^\kappa)\).
The reverse rectangles use \(-D\) and have the same estimate.
These two families partition the offsets of magnitude at least three, and summability of \(r_j+r_j^{\kappa-1}\) bounds the distant part of \(K-10\).
The single constant on the entire cross rectangle recovers the baseline without summing a triangular family of unit costs.

For \(|j-k|\le2\) both branch heights lie between \(c(v/8)^\kappa\) and \(Cv^\kappa\).
Direct integration gives \(-i\int_0^\infty e^{-\lambda(d_x+d_y)+i\lambda(x-y)}\,d\lambda=1/D_0\).
After multiplication by the two square roots of the heights, the two \(L^2(d\lambda)\) factors each have norm \(1/\sqrt2\).
Expansion in a real orthonormal basis and the measurable Schur factorization give the asserted \(1/2\) bound for the weighted kernel with any two restricted marginal measures.
The ratios of the height square roots have bounded separated cost on the rectangle, and so do the factors \(\epsilon_\pm(x)/\sqrt{d_xd_y}\) or \(\epsilon_\pm(y)/\sqrt{d_xd_y}\) by the coding-error bound and height comparison.
This controls both \((x-y)/D_0=1-i(d_x+d_y)/D_0\) and the normalized coding error.

The cutoff of \(g'(vt)\) in the proof has periodic \(H^1\) norm \(O(v\|g''\|_\infty)\) by the chain rule and \(g'(0)=0\).
Since the interpolation argument \((\theta x+(1-\theta)y)/v\) stays in \([1/8,1]\), the absolutely summable Fourier expansion equals \(g'\) there after rescaling.
The separated characters and integration in \(\theta\) hence bound \(g^{[1]}\) in Schur norm by \(O(v)\).
For small \(v\), the product of this symbol and \((x-y)/D_0\) has norm less than \(1/2\), so the reciprocal of \(D/D_0\) belongs to the multiplier algebra with norm at most two.
For the finitely many remaining rectangles the two closed branch pieces are compact and disjoint, since coincidence of two decoded points would require \(x=y>0\) and \(2d(x)=0\).
Smooth separated-support cutoffs of the planar reciprocal give the required bounded Fourier expansion there.
At a fixed one of the five near offsets both the row and the column projections are disjoint.
The operator norm of the direct sum of the multiplied blocks is bounded by their uniform multiplier norm times the input norm, also for infinitely many blocks.
This proves the cross bound and, by transposing the kernel and exchanging the two measured spaces, the reverse cross bound.

The passage to the original mixed core uses a Lipschitz forward decoder on the whole real hull.
The joint smooth cutoff of the squared column modulus gives approximating real-core columns with convergent coarse derivatives and limit superior of their norms at most \(1+\varepsilon\) for a unit original column.
The bounded rectangle kernel then passes through this approximation.
Multiplication by the inverse secant turns the forward differences of \(Z\) and \(Z^*\) respectively into the rectangle projection and its product with the forced original phase.
The product rule and the zero values on omitted starred letters identify the localized derivation on every represented word.
Translations cancel and a rotation of the decoded coordinates contributes precisely the inverse unit factor to the inverse secant.

For each same-branch rectangle, using one ordinary interval per branch at a positive real distance produces a different Lipschitz forward decoder.
Its conull injectivity, scalar packing and inverse-gap transfer hold as above.
The slope \(g'\pm d'\) has bounded variation on the selected closed interval by the \(C^2\) hypothesis.
The old-core graph bound followed by the equal-projection restriction and localized graph transfer of the single-piece argument gives the estimate on that branch.
Those steps use only the selected graph, so there is no outgoing-angle condition at the common endpoint and no inverse Lipschitz requirement on the other branch.
The four rectangles exhaust the coarse square since its spectral measure class is dominated by the product law.
Reflection interchanges the branches and negates \(g\), preserving their height comparison.
The actual flip-adjoint right bound gives the left single-input bound required by the two-slice theorem for the original canonical \(E\).
The identity \(E(X_jp)-X_jE(p)=\delta_{ij}\tau(p)\Omega\) persists under graph convergence since left multiplication and the vacuum projection are bounded.
It gives \([X_j,-\bar E]=\delta_{ij}P_\Omega\) on the closure domain, hence on all bounded vectors.
Applying this result coordinate by coordinate proves the stated implication for tuples.
The example \(g=0,\ d(x)=x^2\) satisfies every geometric assumption with \(\kappa=2\).
The proof allows a curved \(C^2\) midline with the prescribed tangent and leaves contacts flatter than every power open.
The established inputs were checked at their listed interfaces without a new proof audit of external multiplier or singular-integral theorems.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0250_v1.md#decision-candidate) | Complete candidate for a power-order two-branch contact. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0250_v1.md#statement) | All geometric, measure and tuple quantifiers, the column and adjoint estimates, canonical domains, commutator, and examples. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0250_v1.md#argument) | Interleaved coding, real ACSY transfer, distant and comparable cross multipliers, same-branch restriction and recovery of original columns. |
| [Finding](#finding) | [ACSY and strong condition](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred core, two bounded-vector domains and the generator-first convention. |
| [Finding](#finding) | [Normal generator formulas](../../claims/Yin_C_F0076_v1.md#statement) | Diffuse marginal, forced adjoint-letter phase and actual flip-adjoint companion. |
| [Finding](#finding) | [Scalar packing](../../claims/Yin_C_F0233_v1.md#statement) | Part 1 with one center per disjoint occupied parameter cell. |
| [Finding](#finding) | [Real chart construction](../../claims/Yin_C_F0248_v1.md#a-real-parameter-for-a-selected-chart) | Histogram density and real inverse-gap energy adapted to a countable encoding with a globally Lipschitz decoder. |
| [Finding](#finding) | [Real scalar vacuum](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Compactly supported \(L^3\) parameter density on the real identity graph. |
| [Finding](#finding) | [Borel liberation](../../claims/Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Invariance on marginal algebras and pushforward of the liberation measure at the changed and omitted coordinates. |
| [Finding](#finding) | [Inverse-gap criterion](../../claims/Yin_C_F0238_v1.md#statement) | Finite old energy and reconstruction of actual vacua on the parameter tuple. |
| [Finding](#finding) | [Coarse measure class](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination for null endpoints, uniform truncations and the four-rectangle partition. |
| [Finding](#finding) | [Old real column](../../claims/Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Finite column cost of the distinguished real derivative on the mixed parameter core. |
| [Finding](#finding) | [Measurable Schur factorization](../literature/AP25/Yin_U001.md#ap25-u001) | Hilbert-valued separated factors in (5) for arbitrary two branch measures with the operator-norm test. |
| [Finding](#finding) | [Positive distance and localized transfer](../../claims/Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Planar Fourier expansion on disjoint compacts and equality on the localized original generators. |
| [Finding](#finding) | [Old-core Schur insertion](../../claims/Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Cross multiplier on the two measured subsets of the encoded selfadjoint marginal. |
| [Finding](#finding) | [Joint column graph approximation](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Lipschitz forward map, norm cutoff and passage through the bounded localized multiplier. |
| [Finding](#finding) | [Single-piece restriction](../../claims/Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) | Bounded-variation graph on the selected branch with identical first- and second-leg projections. |
| [Finding](#finding) | [Two-slice domain theorem](../../claims/Yin_C_F0072_v1.md#statement) | Part B with both single-input slice bounds for the actual original derivation. |
