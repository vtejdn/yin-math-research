---
author: Yin
---

# The distinguished vacuum and a dimension-free slice bound for relative Gaussian models

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded normal with compact diffuse law \(\mu\), let \(N=W^*(Z)\), and take \(r\) standard free semicirculars free from \(N\) in their tracial free product.
Use the [matrix Gaussian construction](Yin_C_F0209_v1.md#statement): \(A(z,w)\) is a measurable complex \(q\times r\) matrix with \(A(w,z)=\overline{A(z,w)}\) and \(\operatorname{ess\,sup}_{w}\int\sum_l|A_{jl}(z,w)|^2d\mu(z)<\infty\) for every \(j\).
Here \(q,r\) are arbitrary positive finite integers and the bar denotes entrywise conjugation.
Let \(T_1,\ldots,T_q\) be its bounded selfadjoint pure first-chaos fields, \(M=W^*(Z,T_1,\ldots,T_q)\), and \(P\) their represented starred polynomial algebra.
Relative actuality means that an outer derivation \(D:P\to L^2(M)\otimes_2 L^2(M)\) with \(DZ=1\otimes1,\ DT_j=0\) has the actual vacuum \(\xi=D^*(1\otimes1)\).

Write \(G=(AA^*)^{1/2}\), \(G_\epsilon=(G^2+\epsilon^2 I_q)^{1/2}\), and
\[
 J=\lim_{\epsilon\downarrow0}\int
 \frac{\|P_\epsilon^{-1}Q_\epsilon-P_\epsilon Q_\epsilon^{-1}\|_{\rm HS}^2}
 {|z-v|^2}\,d\mu(z)d\mu(w)d\mu(v),\qquad
 P_\epsilon=G_\epsilon(z,w),\quad Q_\epsilon=\overline{G_\epsilon(w,v)}.
                                                                    \tag{1}
\]
The Hilbert–Schmidt norm uses the unnormalized matrix trace and the endpoint diagonal is null.
The integrals increase as \(\epsilon\) decreases.
Relative actuality is equivalent to existence of the scalar normal vacuum \(\xi_N\) of \(\mu\) and \(J<\infty\), in which case
\[
 \|\xi\|_2^2=\|\xi_N\|_2^2+J,\qquad
 \|(\mathrm{id}\otimes\tau)Dp\|_2,\ \|(\tau\otimes\mathrm{id})Dp\|_2
                   \le\sqrt{17}\,\|\xi\|_2\,\|p\|,\quad p\in P.           \tag{2}
\]
In particular the original right-slice closure and its Hilbert adjoint have domains containing \(M\Omega\) at this coordinate.
These bounds are independent of \(q,r\), the size of the fields and the rank of their covariance.
They exclude this family from witnessing unbounded [relative slice-to-vacuum ratios](Yin_C_F0305_v1.md#statement).

Equivalently, \(J<\infty\) requires and is implied by the following two conditions together: \(\ker G(z,w)\) is almost surely one fixed conjugation-invariant subspace, and the integral in (1) with \(P=G(z,w),Q=\overline{G(w,v)}\) and their inverses on its orthogonal complement is finite.
The zero subspace and the zero-dimensional complement are both allowed.
There is no requirement of an integrable inverse amplitude on the complement.
An example below has scalar \(G>0\) almost everywhere, \(J<\infty\) and \(\int G^{-2}\,d\mu^2=\infty\).

## Argument

### Adding free channels and identifying the limiting vacuum

The coordinating agent proposed regularizing the observed fields with independent noises while differentiating only at \(Z\).
Adjoin \(q\) further free standard semicirculars \(S'_j\) freely to the full original ambient algebra and use \(T_j^\epsilon=T_j+\epsilon S'_j\).
They have amplitude matrix \([A\ \epsilon I_q]\) over the same base and therefore positive reduced amplitude \(G_\epsilon\).
Their common row bounds are finite for every fixed \(\epsilon\), and \(\int\operatorname{tr}(G_\epsilon^{-2})\,d\mu^2\le q/\epsilon^2\).
Put \(M_\epsilon=W^*(Z,T_1^\epsilon,\ldots,T_q^\epsilon)\) inside this single ambient free product.

Suppose first that the original distinguished vacuum exists.
Projection to the marginal yields \(\xi_N\), since normality and diffuseness force the starred derivative of \(Z\) to be the marginal divided difference.
The [normal starred relation](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) at the one designated coordinate uses no coefficient derivatives.
Extend \(D\) from the original core freely, killing the new semicirculars.
The vacuum remains \(\xi\), since on centered reduced words involving noise every differentiated base letter leaves a centered free segment on a trace leg.
This also holds for Hilbert tensor values by approximation with bounded base tensors.
The restriction to the new generated algebra kills \(T_j^\epsilon\), and its actual vacuum is the Hilbert projection \(P_\epsilon^{\rm alg}\xi\) onto \(L^2(M_\epsilon)\).
Indeed its values on the new core are obtained using only the two \(Z\)-symbols, the new generators, and the product rule, so belong to the new coarse space.
At each new coefficient the free semicircular derivative scaled by \(\epsilon^{-1}\) supplies the actual normalized derivative by the same restriction and vacuum projection.
Thus the smoothed tuple meets the full hypotheses of the matrix Gaussian theorem, whose two-edge formula gives
\[
            \|P_\epsilon^{\rm alg}\xi\|_2^2=\|\xi_N\|_2^2+J_\epsilon,      \tag{3}
\]
where \(J_\epsilon\) is the integral in (1).
In particular these integrals are bounded.
For a fixed polynomial its input with \(T^\epsilon\) converges in operator norm to its old input.
For each \(\eta\in L^2(M)\), approximate it by a fixed original core vector, and then use the corresponding new polynomial vector as a competitor for its distance to \(L^2(M_\epsilon)\).
It follows that \(P_\epsilon^{\rm alg}\eta\to\eta\) in norm; nesting of the subspaces is unnecessary.
Applied to (3) this proves the exact norm formula whenever relative actuality holds.

Conversely suppose the scalar vacuum exists and the integrals are bounded as \(\epsilon\downarrow0\).
The full Gaussian criterion gives an actual normalized distinguished derivative and a vacuum of squared norm \(\|\xi_N\|_2^2+J_\epsilon\) at every smoothed tuple for which \(J_\epsilon<\infty\).
Along a sequence tending to zero these vectors have a weakly convergent subsequence in the common ambient Hilbert space.
For every formal starred word polynomial \(p\), its evaluations converge in operator norm, and its formal derivative tensors converge in the ambient coarse norm, using the same unit and starred marginal phase at \(Z,Z^*\), zero at the fields and norm-convergent bounded outer multipliers.
The limiting vacuum identity holds for these formal evaluations, with the weak limit projected onto \(L^2(M)\).
For any represented relation \(p(Z,T)=0\), test that identity on \(a p b\) for arbitrary starred polynomials \(a,b\).
Only the middle term \(a(D_{\rm formal}p)b\) survives in the product rule.
Its double trace is therefore zero for every \(a,b\), and density of the test tensors from the original core shows \(D_{\rm formal}p=0\) in the original coarse space.
Thus the limiting derivation descends and has its actual vacuum in \(L^2(M)\).
The preceding projection argument now applies to this vacuum itself.

### The kernels allowed by finite variation

For fixed \(z,w,v\) choose orthonormal eigenbases of \(P,Q\), with eigenvalues \(s_i,t_j\ge0\) and corresponding vectors \(u_i,v_j\).
By the [matrix norm expansion](Yin_C_F0209_v1.md#removing-the-matrix-amplitude-cutoff), the squared numerator of (1) is
\[
 \sum_{i,j}|\langle u_i,v_j\rangle|^2\,
 \frac{(s_i^2-t_j^2)^2}{(s_i^2+\epsilon^2)(t_j^2+\epsilon^2)}.
\]
This proves monotonicity and gives a limit by monotone convergence, independently of any measurable choice of bases.
Finiteness requires the eigenspaces for zero of either matrix to be orthogonal to the positive eigenspaces of the other matrix, hence \(\ker G(z,w)=\ker G(v,w)\) for almost every triple by edge reversal.
The measurable projection onto that kernel, averaged in \(z\) at fixed \(w\), is a matrix \(K(w)\) equal to the kernel projection almost everywhere on the corresponding row, by Fubini.
Edge reversal gives \(K(w)=\overline{K(z)}\) for almost every pair.
Integrating in \(z\) makes \(K(w)\) a constant real projection almost everywhere.
On its orthogonal complement all eigenvalues are positive; the expansion there converges to the displayed unsmoothed integrand, and the directions in the common kernel contribute zero.
The converse and the stated equivalence follow from the same expansion.

### A single-input bound independent of all color counts

In the full-rank case of the [Gaussian matrix construction](Yin_C_F0209_v1.md#reference-corrections-for-bounded-positive-matrices), the reference derivative at \(Z\) kills the free semicircular family and has vacuum \(\xi_N\).
It has right-slice norm at most \(3\|\xi_N\|_2\) by the [free normal estimate](Yin_C_F0162_v1.md#statement), since the scalar base and standard semicirculars are freely independent actual coordinates.
In the intrinsic square positive model the correction uses degree-one arrays with total squared coefficient norm \(B^2\le\|H\|_2^2\), where \(H\) is the two-edge component and \(\|H\|_2^2\) is the second integral of that matrix theorem.
Indeed after the two changes of dummy variables its arrays are \(P^{-1}Q-I,\ I-PQ^{-1}\) divided by the endpoint gap and modified by conjugation; the real Hilbert–Schmidt cross term is nonnegative.
The [orthogonal colored-cut estimate](Yin_C_F0209_v1.md#contractions-with-a-single-inserted-color) has constant \(2\sqrt2 B\) for the right slice, since at each suffix position the different colors have orthogonal initial subspaces.
Hence in the bounded positive matrix case the canonical right-slice norm at \(Z\) is at most \(3\|\xi_N\|_2+2\sqrt2\|H\|_2\le\sqrt{17}\|\xi_N+H\|_2\), the scalar and two-edge parts being orthogonal.
The intrinsic path isometry in that theorem preserves the target trace, Hilbert norms, represented norms and the two \(Z\)-symbols when passing to a rectangular matrix.

For clarity this exact constant survives removal of an upper amplitude cutoff.
In the reference square representation replace the positive matrix by its spectral clipping from above at integers \(L\).
After the same changes of dummy variables, each clipped correction array has pointwise squared Hilbert–Schmidt norm bounded by the squared two-edge density of the unclipped model: the positive cross term bounds either summand by the clipped sum, and (6) in the [matrix clipping proof](Yin_C_F0209_v1.md#removing-the-matrix-amplitude-cutoff) bounds that sum by the unclipped one.
The arrays converge pointwise, hence in the coefficient Hilbert norm by domination.
The corresponding reference correction maps on the reference core are linear in those arrays; the colored-cut estimate bounds the norm of each difference by \(2\sqrt2\) times the coefficient difference.
These bounded maps have normal extensions of the same norm: the finite-degree actual-adjoint argument in the cut estimate gives dense Hilbert adjoint domain, and the [normal extension argument](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) then applies.
Thus the reference maps, including the fixed scalar reference derivative, converge in operator norm as maps from the reference algebra to its trace Hilbert space to a normal map with the same bound.
Normality passes to this limit since testing against each Hilbert vector gives a norm limit of normal linear functionals.
The clipped fields are uniformly bounded and converge strongly-star to the fields of the unclipped matrix in this same representation.
Testing the limit map on any fixed unclipped target polynomial therefore gives the weak limit of the clipped reference maps on the corresponding clipped polynomials.
Those maps there agree with the clipped canonical right slices by the matrix construction, and the polynomial product rule gives convergence of those sliced tensors in trace Hilbert norm using the fixed two symbols at the base.
This identifies the limit with the canonical right slice on the unclipped core and proves the same numerical bound there.

Apply this bound at \(G_\epsilon\).
The full smoothed vacuum is needed only in its distinguished coordinate, of norm at most \(\|\xi\|_2\) by (3).
Norm convergence of the input polynomials and Hilbert convergence of their derivative tensors as \(\epsilon\downarrow0\) give the right-slice bound in (2) on the actual original core.
For the left slice take the adjoint normal base \(Z^*\), with base parameter \(\bar z\) and kernel \(A'(\bar z,\bar w)=A(z,w)\); the fields \(T_j\) stay selfadjoint.
The [flip-adjoint derivation](Yin_C_F0073_v1.md#statement) interchanges right and left slice on adjointed inputs and has vacuum \(\xi^*\) of the same norm.
Its construction uses the actual distinguished derivative alone.
Applying the right-slice bound in those coordinates gives the second inequality of (2), and the [two-slice domain theorem](Yin_C_F0072_v1.md#statement) gives both domain inclusions.

### Finite distinguished energy with infinite inverse amplitude

Use disks \(E_j\) of centers \(2^{-j}\) and radii \(2^{-j-4}\), \(j\ge1\), with uniform area of total mass \(t_j=3\cdot4^{-j}\) on disk \(j\).
This compactly supported diffuse probability has an actual scalar vacuum by the [bounded-density disk calculation](Yin_C_F0303_v1.md#a-non-gaussian-example-at-the-summability-threshold).
The distance between disks \(j\ne k\) is at least \(2^{-\min(j,k)}/3\).
Take one field and one noise, and set \(h_j=2^{-j/4}\).
On \(E_j\times E_n\) set \(A=h_j h_n\) if \(j\ne n\), with \(A=t_n\) on \(E_n^2\).
This positive symmetric bounded kernel has finite row bounds, and \(\int A^{-2}d\mu^2\ge\sum_n t_n^2/t_n^2=\infty\).

In the integral with endpoint indices \(j,k\) and middle index \(n\), equal endpoint indices give zero.
If all three indices are distinct, the amplitude ratio compares \(h_j\) and \(h_k\).
Use \(4^{\min(j,k)}\le2^{j+k}\) and \((b-b^{-1})^2\le b^2+b^{-2}\) for \(b>0\).
The total is bounded by an absolute multiple of \((\sum_j2^jt_jh_j^2)(\sum_k2^kt_k/h_k^2)<\infty\).
If exactly one endpoint equals \(n\), call the other index \(m\).
The two amplitudes are \(t_n\) and \(h_n h_m\).
For the term with ratio \(h_n h_m/t_n\), bound the inverse squared gap by \(9\cdot4^m\); its contribution is bounded by a multiple of \(\sum_n h_n^2\sum_m4^m t_m h_m^2<\infty\).
For the reverse ratio use \(9\cdot4^n\); this gives at most a multiple of \(\sum_n4^n t_n^4/h_n^2\sum_m t_m/h_m^2<\infty\).
Thus \(J<\infty\) and the distinguished coordinate obeys (2), although the inverse-amplitude condition for a vacuum at the field fails.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:17 |
| status | open |
| reason | Fix the single-coordinate Gaussian vacuum criterion, exact norm, dimension-free bound and example for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinguished actuality and two domain bounds for arbitrary finite bounded Hermitian families, fixed real nullspace, and a positive full-rank example with no integrable inverse amplitude. |
| argument | [Argument](#argument) | Independent noise smoothing, convergence of intrinsic vacuum projections, relation descent, monotone Gram ratios, quantitative reference cut bounds and cross-disk estimates. |
| dependency | [Gaussian matrix theorem](Yin_C_F0209_v1.md#argument) | Bounded field row criterion, positive matrix realization, full actuality, two-edge vacuum, colored derivative norms, intrinsic path isometry and upper clipping transfer. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Forced marginal starred derivative at a diffuse actual base. |
| dependency | [Free scalar-reference estimate](Yin_C_F0162_v1.md#statement) | Right contraction at the base with numerical constant three for every finite free normal family. |
| dependency | [Normal extension](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Same-norm normal extension of bounded core slices having dense Hilbert adjoint domain. |
| dependency | [Flip-adjoint derivative](Yin_C_F0073_v1.md#statement) | Reversing the two Hilbert legs on adjoints and equality of distinguished vacuum norms in the opposite orientation. |
| dependency | [Two-slice graph criterion](Yin_C_F0072_v1.md#statement) | Bounded original right and left contractions imply domain inclusion for the closure and the actual adjoint. |
| dependency | [Planar disk marginal](Yin_C_F0303_v1.md#a-non-gaussian-example-at-the-summability-threshold) | Bounded planar density and finite scalar geometric energy for the specified disk law. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:24 |
| status | proved |
| reason | Independent review verified the single distinguished-vacuum criterion, constant real null directions, the dimension-independent square-root-of-seventeen bound and the example without a noisy-coordinate vacuum. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinguished actuality and two domain bounds for arbitrary finite bounded Hermitian families, fixed real nullspace, and a positive full-rank example with no integrable inverse amplitude. |
| argument | [Argument](#argument) | Independent noise smoothing, convergence of intrinsic vacuum projections, relation descent, monotone Gram ratios, quantitative reference cut bounds and cross-disk estimates. |
| dependency | [Gaussian matrix theorem](Yin_C_F0209_v1.md#argument) | Bounded field row criterion, positive matrix realization, full actuality, two-edge vacuum, colored derivative norms, intrinsic path isometry and upper clipping transfer. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Forced marginal starred derivative at a diffuse actual base. |
| dependency | [Free scalar-reference estimate](Yin_C_F0162_v1.md#statement) | Right contraction at the base with numerical constant three for every finite free normal family. |
| dependency | [Normal extension](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Same-norm normal extension of bounded core slices having dense Hilbert adjoint domain. |
| dependency | [Flip-adjoint derivative](Yin_C_F0073_v1.md#statement) | Reversing the two Hilbert legs on adjoints and equality of distinguished vacuum norms in the opposite orientation. |
| dependency | [Two-slice graph criterion](Yin_C_F0072_v1.md#statement) | Bounded original right and left contractions imply domain inclusion for the closure and the actual adjoint. |
| dependency | [Planar disk marginal](Yin_C_F0303_v1.md#a-non-gaussian-example-at-the-summability-threshold) | Bounded planar density and finite scalar geometric energy for the specified disk law. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0316_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
