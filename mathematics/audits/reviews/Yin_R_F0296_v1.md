---
author: Yin
---

# Review of the cubic criterion for polar factors of omitted shifts

## Finding

At 2026-11-14T15:32 UTC an agent outside proof development independently checked the [candidate of 2026-11-14T15:27](../../claims/Yin_C_F0287_v1.md#decision-candidate), its whole argument and all nine declared dependencies at their points of use.
The reviewer received the fixed proof and the review scope without development dialogue, exploration notes, author explanations or prior findings on this candidate.
The argument proves the four domain inclusions, the two adjoint formulas and both uniform forward cutoff limits for the stated families, including the mixed-polynomial and scalar assertions.
The dependency checks use the selected proved inputs at their stated interfaces.

In the opposite tensor representation the product rule for \(T(T^*T+s^2)^{-1}\) gives the coefficient \(1-TR_sT^*=s^2L_s\) before \(DT\), and the coefficient \(-W_s\otimes W_s^{\rm op}\) before \(DT^*\).
The kernel theorem supplies unitary polar factors for coordinate shifts.
For mixed shifts the cubic hypothesis excludes a mass at zero and equality of the two support traces gives the same unitary conclusion.
The derivative symbols of a fixed mixed \(p,p^*\) are bounded in both orientations by \(B_p\), because differentiating a word gives only bounded outer factors times bounded generator symbols.
Multiplication on the right by \(g_r\) needs no commutation with these symbols.
The omitted multipliers have bounded strong-star polynomial approximations of zero derivative.
For each individual shift the inverse series converges in both graphs with a common geometric bound for its fixed approximants, so this approximation imposes no bound on the norms of other shifts.
Applying the polynomial adjoint identity in both orientations identifies the vacua as \(\xi,\xi^*\) and the corrections as the opposite forward slices.
Bounded strong convergence of the inputs gives convergence of their left products with each vacuum in \(L^2\).

For an output band \(d\le v<2d\), the left spectral projection gives a factor \(\sqrt{p_d}/(d^2+s^2)\) in the first term and \(2d\sqrt{p_d}/(d^2+s^2)\) in the second.
The remaining trace functional on the second leg costs at most \(\|B c\|_1\le\|B\|_1\), even when the omitted contraction \(c\) fails to commute with the residual.
The positive kernel in (3) factors into two Cauchy kernels divided by \(d+w\), so its \(s\)-integral is \(\pi/(d+w)\), including at \(d=w\).
Orthogonality is used before applying the common left contraction \(a\).
For three independent samples the inverse square of their maximum has mean \(2I(F_\mu)\), which gives the lower bound \(I(F_\mu)/2\) in (4).
For the upper bound one writes \(1/\max(v,w)=\int_{\max(v,w)}^\infty t^{-2}\,dt\).
After squaring and integrating, the smaller of the two radii supplies a second factor of \(F_\mu(t)\).
Writing the larger radius as \(te^y\) leaves the weight \(2e^{-y/3}\), whose integral is six, and Hölder in \(dt/t\) supplies \(I(F_\mu)\).
This proof by nonnegative integrals allows atoms at positive radii and either infinite side of (4).

Restricting the output to \(v<\eta\) replaces the extra factor \(F_\mu(t)\) by at most \(\min(F(t),F(\eta))\).
The ordered double integral with the unrestricted product \(F(t)^2 F(u)\) is finite by the same Hölder bound, and \(F(\eta)\to0\).
Dominated convergence thus controls all the small bands using the single upper envelope, including when the shifts realizing its supremum vary with the radius.
On the bands \(d\ge\eta\), splitting the lower-end arctangent integral at \(w=\sqrt{\epsilon}\) bounds the projected tail by \(\sqrt{p_d}\) times a quantity tending to zero at fixed \(\eta\).
At the upper endpoint \((\arctan(d/A)+\arctan(w/A))/(d+w)\le 1/A\) for every \(d,w>0\).
Squaring and summing uses only \(\sum_d p_d=1\).
These estimates apply in both orientations to all omitted contractions and all radii.
On a compact \(s\)-interval the remaining error is bounded by an integrable multiple of \(\|g_r-1\|_2\), with the multiplier \(B_p\) for mixed inputs.
The diffuse coordinate law removes the diagonal in this last limit.
For fixed \(r\), normality supplies the weak limit of the bounded inputs' images, which agrees with the strong limit given by the estimates.
Closedness passes both forward and adjoint identities to the limit separately for each input.

The narrow-cone and normal-residual estimates give the common integral over the asserted families, and finite columns give it over all omitted shifts.
For a selfadjoint polynomial the missing atom identifies the open lower spectral cut with half the difference of the unit and the polar sign.
For a symmetric scalar real coordinate, \(\tau(W_s)=0\) and the positive slice integrates to \(K(|Z|)\), using \(\int_0^\infty s^2/((v^2+s^2)(w^2+s^2))\,ds=\pi/(2(v+w))\), also at \(v=w>0\).
The scalar weighted estimate supplies finite columns by summing the squared bounds, so the cubic integral for the zero shift is finite.
For the example the \(L^3\) density condition and the cubic integral require \(3\alpha>1\), whereas the lower bound for the integral of the sliced norms diverges for \(3\alpha/2\le1\).
This includes the logarithmic endpoint \(\alpha=2/3\) and yields the claimed example of a threshold outside the absolute integral criterion.
The uniform estimates concern the specified polar factors, their omitted multiples and the stated spectral cuts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0287_v1.md#decision-candidate) | Complete candidate dated 2026-11-14T15:27 and all nine declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0287_v1.md#statement) | Both signs and omitted multipliers, four domains, two uniform cutoff limits, mixed shifts, thresholds and the symmetric scalar example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0287_v1.md#argument) | Closed resolvent graphs and adjoints, dyadic projection estimates, cubic energy comparison, both uniform endpoints, cutoff removal and the logarithmic example. |
| [Finding](#finding) | [Actual starred hypothesis](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred derivations, vacuum pairings and the distinction from full bounded-vector hypotheses. |
| [Finding](#finding) | [Shifted resolvents](../../claims/Yin_C_F0229_v1.md#argument) | Trivial kernels of coordinate shifts, unitary marginal phase, opposite-tensor product rule and bounded graph approximation for each shift. |
| [Finding](#finding) | [Normal cutoffs](../../claims/Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normal bounded right slices for any individual positive radius on the original algebra and its adjoint-tuple realization. |
| [Finding](#finding) | [Polynomial adjoints](../../claims/Yin_C_F0271_v1.md#exact-energy-and-affine-line-rigidity) | Vacuum formula for the core adjoint in each orientation and identification of the flipped opposite slice. |
| [Finding](#finding) | [Mixed polynomial symbols](../../claims/Yin_C_F0285_v1.md#slices-of-resolvents-of-a-mixed-polynomial) | Norm bounds for original mixed-word derivatives in the opposite tensor algebra and right multiplication by the cutoff before slicing. |
| [Finding](#finding) | [Absolute threshold integral](../../claims/Yin_C_F0285_v1.md#statement) | The norm-product resolvent criterion at a selfadjoint threshold is comparable to its mass integral of exponent \(3/2\). |
| [Finding](#finding) | [Narrow cone](../../claims/Yin_C_F0272_v1.md#statement) | Finite cubic integral of the common envelope over all omitted shifts under the stated marginal phase bound. |
| [Finding](#finding) | [Normal residuals](../../claims/Yin_C_F0270_v1.md#statement) | Cubic integral over the complete family of exactly normal shifted residuals, with shifts allowed to vary with scale. |
| [Finding](#finding) | [Necessary cubic estimate](../../claims/Yin_C_F0258_v1.md#statement) | Finite columns bound the cubic integral for the full shift envelope and hence its zero-shift specialization. |
| [Finding](#finding) | [Scalar columns](../../claims/Yin_C_F0267_v1.md#statement) | Finite column bound from the common integrable weight of the scalar original right slice. |
| [Finding](#finding) | [Actual real coordinate](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | The identity graph over the compact real \(L^3\) probability density has an actual vacuum. |
