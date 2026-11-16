---
author: Yin
---

# Review of the finite-label lattice criterion for the normal converse

## Finding

Review time (UTC) 2026-11-16T19:18.
A reviewer outside the development of C_F0339 inspected its entire candidate dated 2026-11-16T19:16 and the eleven direct dependency interfaces listed below.
No development dialogue, author explanation, exploration notes or earlier finding on this candidate was supplied or consulted.
The two universal constants in (2), the circle recovery on the original graph and the segment approximation all hold at the stated scope.

For a finite marginal partition, inner multiplication by \(k_{ij}\) takes the liberation derivative of \(U\) to the off-diagonal indicator and that of \(U^*\) to the off-diagonal discrete chord phase.
When rounding an actual coordinate, bounded strong-star marginal approximants to the cells have convergent liberation derivatives because liberation is the inner difference on that marginal.
The word product rule lets one project its vacuum to \(L^2(N)\), and the projection contracts each \(e_i,e_j\) block by bimodularity.
Every old pair in distinct cells has distance at most \((1+\sqrt2)|c_i-c_j|\), so the inverse squared gap for the old liberation vector bounds the weighted off-diagonal sum with the claimed slack.
The maximal density controls balls of centers since an old point in cell \(i\) is within \(4s\) of every old point whose center is within \(s\ge h\).
The near part of the difference between \(H_i\) and the soft Cauchy transform at parameter \(h^2\) is bounded by \(C M_1\mu(x)\).
On a distant shell of scale \(2^kh\), the change of kernel costs \(Ch/(2^kh)^2\), and the shell mass is at most \(C2^kh M_1\mu(x)\).
The summable factor \(2^{-k}\), the \(L^2\) maximal density bound and the uniform soft Cauchy bound therefore give \(B_c\le C\|\xi\|_2\) independently of the labels and mesh.
For \(\mu^2\)-almost every pair of points the rounded symbols converge to the unrounded generator symbols with bound one, including convergence of the off-diagonal indicator to the unit.
Finite word expansions now converge in the common coarse Hilbert norm and in operator norm on inputs.
The right trace is contractive, so \(K_{\rm proj}\le C K_{\rm lat}\) follows on each original contraction, rescaling the approximating words by their norms if necessary.

I checked the free semicircular mixed-moment formula (14.5) and free compression Theorem 14.10 in the retained publisher-layout edition of Nica and Speicher, printed pp. 228 and 230.
These accepted inputs give variance \(t_i\) before the \(t_i^{-1/2}\) normalization.
Testing a polynomial in the compressed variable against an old coefficient, the Wick contractions of the intermediate \(e_i\)'s leave only a scalar multiple of \(e_i\) in the old algebra.
Thus conditional expectation of a bounded spectral function is its normalized component mean times \(e_i\), also for noncommutative \(N\).
The construction can prescribe either uniform component law by measurable functional calculus.
The extended complementary derivation kills the old projections and the new noises.
Its centered free extension preserves the old vacuum \(-\eta\); tensor adjunction on algebraic simple tensors gives closability.
Bounded strong-star approximation of the compressed noise functions by killed polynomials converges in its graph, and on finite mixed words the remaining bounded outer multipliers converge strongly on their coarse inputs.
Subtracting from \(\operatorname{ad}\) gives the required liberation with vacuum \(+\eta\) in \(M'\), since the disjoint components of \(V\) recover \(D\) and \(N\subset M'\).

Inner restriction by \(e_i\otimes e_i\) kills each original liberation generator and hence every such word.
The endpoint terms in the double trace at \(e_i p e_i\) cancel, proving \(e_i\eta e_i=0\).
For \(i\ne j\) the different noise labels force the trace of the two conditionally centered component functions separated by \(N\) coefficients to vanish.
Indeed a function centered over \(N\) in \(N*W^*(S_i)\) lies in the closed span of reduced words containing an \(i\)-noise letter and having no other noise label.
An intervening old factor may cancel without canceling distinct noise letters \(i,j\).
Together with the conditional means this gives the product marginal distribution of the \(i,j\) block of the vector, first for bounded \(e_iNe_j\) coefficients and then by \(L^2\) approximation for \(e_i\eta e_j\).
The resulting density relative to \(\mu'^2\) on that product is \(\|e_i\eta e_j\|_2^2/(t_it_j)\).
The separation \(3|c_i-c_j|/4\) gives the constant \(16/9\) in the inverse-gap budget.
The finite density bound with zero same-label blocks also permits the finite-valued feature criterion after reconstruction; the feature constant may depend on the finite data.

The squared norm of each component vacuum is \(O(h^{-2})\) by the scalar geometric criterion, using linear density for both laws, zero curvature for a segment and constant reciprocal radius for a circle.
In the marginal vacuum pairing the same-component contribution has weight \(t_i^2\); the opposite order on distinct components gives the factor two in (3).
The cross-component Cauchy error sums to \(CM_i\) by the same shell calculation, this time using the center-ball masses at scales at least \(h\).
Since \(t_i/h\le M_i\), this bounds the full scalar squared norm by \(C\sum_i t_i(|H_i|^2+M_i^2)\).
The coarse inner gap is injective for the diffuse spread law.
The adjoint reconstruction converges in norm on the liberation term off the diagonal and weakly on the scalar row-minus-column term, which is enough for the pairing on each original word.
The two limiting vectors are orthogonal.
Together these facts give the actual normalized derivative at \(V\) with \(\|\xi'\|_2\le C B_c\), keeping \(P\) killed.

For exact recovery on circles the spectral label indicators extend as smooth functions constant on neighborhoods of each component.
Polynomial approximation on a box in the \(C^1\) norm gives convergence both in input operator norm and uniformly in the off-diagonal divided differences.
These approximants place the labels and their words with \(P\) in the original graph; this argument uses the component gaps.
For distinct components write \(z-w=(c_i-c_j)+b\), with \(|b|\le h/4\le|c_i-c_j|/4\).
In the product circle measures all positive moments of \(b\) vanish, so the absolutely convergent geometric series for the reciprocal averages to \(1/(c_i-c_j)\).
The same-component label difference is zero.
Consequently the product of conditional expectations recovers precisely \(d_c\) on each label, and its \(N\)-bimodularity recovers the full derivative on words with \(P\).
Tracing the second leg commutes with projecting the first leg to \(N\).
Applying the original projection estimate to polynomial approximants and passing to these norm limits gives \(K_{\rm lat}\le C K_{\rm proj}\).

In the segment construction both phases can be compared to the common block phase even if \(Z,V\) do not commute with each other inside a block.
The respective far-label phase errors are at most \(Ch/s\), and the squared Hilbert mass of the remaining pairs before or after spreading is controlled by the common center-pair mass in (the \(s+2h\) neighborhood of) the old diagonal.
Taking \(h\downarrow0\) before \(s\downarrow0\) removes it by diffuseness.
The mesh-dependent ambient couplings suffice for fixed test words because the values of \(V\) converge in distance to the embedded \(Z\) in operator norm and all generator derivative errors in coarse norm tend to zero.
This gives the normalized segment witness comparison independently of any exact segment averaging identity.
The two extended-real bounds imply equivalence of finiteness with the original normal problem, and dilation by \(1/h\) multiplies both the discrete slice and its budget by \(h\).
The argument establishes the reduction and individual domains on the spread models; finiteness of a uniform constant over all finite lattices remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0339_v1.md#decision-candidate) | Complete candidate dated 2026-11-16T19:16 and its eleven direct interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0339_v1.md#statement) | Two universal comparison inequalities, scaling, exact circle recovery, segment witnesses and individual original domains. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0339_v1.md#argument) | Rounding budget and phase, corner noise and vacuum, scalar reconstruction, label projection in the original graph and the segment approximation. |
| [Finding](#finding) | [Projection reduction](../../claims/Yin_C_F0308_v1.md#statement) | Relative models with one killed trace-half projection, and equivalence of their universal bound to the normal converse. |
| [Finding](#finding) | [Liberation commutator](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Actual vacuum commutator and inverse-gap control at the original distinguished coordinate. |
| [Finding](#finding) | [Borel graph extension](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Spectral projections in the liberation graph and bounded strong-star approximation of products. |
| [Finding](#finding) | [Scalar geometric estimate](../../claims/Yin_C_F0255_v1.md#statement) | Maximal linear density budget in rounding and component scalar vacua after spreading. |
| [Finding](#finding) | [Soft Cauchy bound](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform marginal \(L^2\) estimate at regularization parameter \(h^2\). |
| [Finding](#finding) | [Free semicircular compression](../literature/NS06/Yin_U004.md#ns06-u004) | Variance under normalized compression, old-algebra conditional moments and the use of separate free noise labels. |
| [Finding](#finding) | [Centered free extension](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Zero derivative on the new free factors and preservation of the old adjoint vacuum. |
| [Finding](#finding) | [Finite-label domains](../../claims/Yin_C_F0337_v1.md#statement) | Finite-valued feature domination and finite secant energy on a separated finite-component law, giving both original domains. |
| [Finding](#finding) | [Actual adjoint reconstruction](../../claims/Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Weak scalar correction and norm-convergent off-diagonal correction on the represented core. |
| [Finding](#finding) | [Relative projection](../../claims/Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Relative reconstruction with a killed atomic selfadjoint coefficient and diffuse distinguished law. |
| [Finding](#finding) | [Scalar approximation](../../claims/Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | \(C^1\) approximation by starred polynomials on the whole box, controlling derivatives of the separated label indicators. |
