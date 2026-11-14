---
author: Yin
---

# Independent review of square-Dini invariance of actual conjugate variables

For Yin I reviewed the complete [candidate dated 2026-11-14T11:57](../../claims/Yin_C_F0254_v1.md#decision-candidate), its direct mathematical dependencies and its published comparison.
I took no part in developing this proof and received no development dialogue, author explanations, exploration notes or prior review conclusions about the candidate.

## Finding

At 2026-11-14T11:58 UTC I found that square-Dini \(C^1\) bi-Lipschitz changes preserve the actual starred ACSY condition in both directions on the specified correlated normal tuples.
The stated scalar squared-norm bound \(4B_h\|\zeta\|_2^2\) and the mixed squared-norm estimate (2) hold with the displayed constants.

The source-vacuum estimate applies to the actual scalar polynomial pairing for the kernel with parameter \(t\) in the denominator.
The symmetrization identity \(\int S_t\,d\mu^3=3\|C_t\mu\|_2^2\) separately applies to every diffuse compact image law, before any target vacuum has been constructed.
On a shell \(r/2<R\le r\), the soft numerator at \(t=r^2\) is at least \(r^4/4\) and its denominator is at most \(16r^6\).
The original vacuum bound gives shell mass at most \(192r^2\|\zeta\|_2^2\) and summing the squared dyadic radii gives the ball bound with coefficient \(256\).
All collision diagonals are null by diffuseness, including after applying an injective map.
Disjoint grid squares of side \(r\) have total cubed mass bounded by the ball estimate at radius \(\sqrt2r\), since each triple in one square obeys that diameter bound.

For a shortest and a longest incident side of lengths \(\ell,R\), Taylor's integral formula along the two segments in the compact convex hull gives errors of size at most \(\ell\omega(R),R\omega(R)\).
The determinant error can use the full image of the longest side in its first error term, which has length at most \(LR\).
Since \(\sqrt H=2|\det(u,v)|\), the total error in the area bound is at most \(4L\ell R\omega(R)\), in addition to the linear part \(L^2\sqrt H\).
This estimate includes collinear triples and orientation-reversing derivatives.
Squaring yields (5), and the image soft denominator is at least \(\lambda^3\) times the source soft denominator at the same \(t\).
Dividing the new \(32L^2\ell^2R^2\omega(R)^2\) term by \(2\ell^2m^2R^2\) costs at most \(64L^2\omega(R)^2/R^2\), using \(m\ge R/2\).
The remaining numerator is bounded using \(\max(2L^4,L^2)\).

On the \(j\)-th shell \(\omega(R)^2/R^2\) is at most \(4\omega(r_j)^2/r_j^2\).
Multiplication by the shell mass and summation give the coefficient \(768\) in (7).
The square-Dini integral bounds the dyadic sum apart from its first term, because on \([r_j,r_{j-1}]\) monotonicity gives an integral at least \(\omega(r_j)^2\log 2\).
The contribution from scales above one is finite by compactness even when the starting diameter exceeds one.
Integrating (6) and dividing by the factor three from symmetrization gives \(64\cdot768/3=16384\) in \(B_h\), uniformly for every \(t>0\).

On a target polynomial \(p(z,\bar z)\), antisymmetry pairs the two terms in its difference into \(2\int p C_t\sigma\,d\sigma\).
The compact image hull bounds the Lipschitz constant of each fixed \(p\), so dominated convergence recovers the full unregularized difference functional.
Weak compactness of the bounded sequence \(2\overline{C_{1/n}\sigma}\) gives a vector representing that functional with the second-variable-linear inner product.
The tensor vacuum therefore belongs to the actual scalar derivative's Hilbert adjoint domain and satisfies \(\delta_{\sigma}^*(1\otimes1)=\zeta'\).
Indeed the scalar difference quotient obeys the outer product rule, descends under equality almost everywhere, and is defined on the dense represented starred polynomials.
The squared norm of the representing vector is at most \(4B_h\|\zeta\|_2^2\).

For an actual source tuple, restriction and projection of its vacuum give the scalar premise on each diffuse marginal.
The coordinate maps and inverses restrict to bounded Borel bijections on the relevant compact supports and preserve the individual marginal algebras.
Item 1 of the mixed relabelling criterion then transports the same partial liberation vacuum and its joint measure, including when other coordinates are changed at the same time.
The lower Lipschitz bound ensures that the new inverse-gap energy is at most \(a^{-2}\) times the old one.
The original squared gap contribution is \(\|\xi_i\|_2^2-\|\zeta\|_2^2\) by orthogonality, and the target reconstruction adds its gap contribution to the new scalar squared norm.
This gives (2) for the derivation on the entire represented target starred algebra without any factor depending on correlations or on the number of other coordinates.

The derivative lower bound follows by taking difference quotients in every real direction.
The inverse function theorem and global bijectivity give a \(C^1\) inverse with derivative \(Dh(h^{-1}y)^{-1}\).
The matrix inverse difference identity gives the modulus bound \(a^{-2}\omega_{h^{-1}(K')}(s/a)\) for every compact \(K'\).
Changing the integration variable to \(s/a\) preserves the square-Dini condition near zero, with any remaining bounded range handled by compactness.
The inverse map therefore satisfies the entire forward hypothesis with lower and upper Lipschitz constants \(L^{-1}\) and \(a^{-1}\).
Starting with actual ACSY for \(Y\) applies the proved direction to \(h^{-1}\), obtaining actual ACSY for \(X\) without assuming a source vacuum in advance.
For the locally \(C^{1,\alpha}\) specialization the small-scale integral is bounded by a constant times \(\int_0^1 s^{2\alpha-1}\,ds\) on each compact set.

I checked the comparison with Tolsa at the level of the published theorem statements.
Theorem 1.3 controls the image curvature for compactly supported measures of finite curvature satisfying the normalized linear growth bound, and Theorem 1.4 transfers the full \(L^2\) Cauchy operator bound for nonatomic measures. [Tolsa, Theorems 1.3 and 1.4, pp. 1246–1247](https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n3-p03.pdf)

The candidate obtains its soft row estimate from the original scalar vacuum and the diameter-shell calculation.
The conclusion and this finding concern actual ACSY, with the mixed-column question for the strong condition left open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0254_v1.md#decision-candidate) | Both directions of the fixed candidate and all quantitative vacuum estimates. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0254_v1.md#statement) | Planar square-Dini changes, correlated normal tuples, locally Hölder derivatives and one-coordinate estimates. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0254_v1.md#argument) | Fixed-scale mass bounds, determinant error, integrated soft energy, actual scalar and mixed adjoints and inverse-map argument. |
| [Finding](#finding) | [ACSY and strong conditions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | The actual vacuum on the represented starred algebra and the separate full-domain hypothesis. |
| [Finding](#finding) | [Soft three-point formula](../../claims/Yin_C_F0055_v1.md#4-soft-kernels-and-exact-positive-three-point-formulas) | Formula (9) for any distinct triple, including collinear triples, with the area normalization used in the distortion estimate. |
| [Finding](#finding) | [Soft vacuum control](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Formula (12) for source and target and (14) for the actual source vacuum alone. |
| [Finding](#finding) | [Borel relabelling](../../claims/Yin_C_F0244_v1.md#statement) | Item 1 for actual mixed-core reconstruction, invariant liberation, the squared-norm split and simultaneous changes of other coordinates. |
| [Finding](#finding) | [Published comparison](../../claims/Yin_C_F0254_v1.md#relation-to-bilipschitz-invariance-of-the-cauchy-integral) | Verified statements of Tolsa's two comparison theorems and their hypotheses. |
