---
author: Yin
---
# Independent review of four-point phase loss for omitted shifts

## Whole-proof finding

At 2026-11-13T16:59 UTC the reviewer independently checked the full [statement](../../claims/Yin_C_F0230_v1.md#statement) and [argument](../../claims/Yin_C_F0230_v1.md#argument) fixed in the [candidate decision](../../claims/Yin_C_F0230_v1.md#decision-candidate) at 2026-11-13T16:57.
The reviewer had used the fixed shifted singular-law result in a separate investigation of scalar radial functionals and had worked on rigidity under two-sided unitary changes of a normal coordinate.
The reviewer had no part in the development of this candidate and received no development discussion or earlier finding for its four-point, carrier, compression, or bounded-shift argument.
All three conclusions hold with the stated constants, weight hypotheses and shift ranges.

**Weighted four-point bound.**
The omitted shift can be nonnormal because the two kernel conclusions of C_F0229 give a unitary polar factor in that case as well.
The spectral weight \(e=g(P)\) and its polar conjugate are bounded, have the same strictly positive trace \(t\), and define laws dominated by \((\|e\|/t)\mu_X\).
The latter is diffuse by C_F0076, so the normalizations, distinctness of the four samples and all uses of the phase off its exceptional set follow.
With \(C_e=e^{1/2}\otimes(e^{1/2})^{\rm op}\), trace preservation of the conditional expectation gives \(\operatorname{Re}\langle C_e,LC_e\rangle=t^2(1-d(e))\).
Removing \(1\otimes U^{\rm op}\) by its adjoint puts \(e^{1/2}U^*\) on the output test of the second leg, while \(Ue^{1/2}\) occurs on the first input.
The weighted input tensor sees precisely \(\nu_f\otimes\nu_e\).
The two normalized output tests induce Riesz vectors of norms at most one.
On a rectangle product multiplier their normalized pairing is the scalar kernel pairing with the conjugate of the second Riesz vector as operator input.
Density in this product \(L^2\) space gives the inequality \(1-d(e)\le\|K\|\) with no positivity assumption on that pairing.

The ratio of the determinant terms is \(\bar Q/Q\), so their squared difference is \(4\sin^2(\arg Q)\).
After averaging, independence of the two first-leg samples gives the squared modulus of the kernel of \(K^*K\) and integration in the second-leg samples gives its squared Hilbert–Schmidt norm.
As \(\|K\|_{\mathrm{HS}}=1\), its largest singular value \(s\le1\) yields \(\Delta(e)\le(1-s^4)/2\le2(1-s)\le2d(e)\).
Total variation continuity of each heat-weighted law in \(s\) gives measurable angular loss.
Integration of the nonnegative defect with the heat weights gives \(I_b\) by Tonelli, and the spectral square \([0,r]^2\) gives \(t^2d(e)\le2rI_b\).
These two steps give respectively the constants \(2\) and \(4\) in the integrated and cutoff conclusions.
The heat and cutoff profiles are used as weights in product trace integrals and require only bounded spectral calculus.

**Carriers and uniformity.**
The Möbius image criterion includes the collinear case, and through any three distinct finite points there is a unique generalized circle.
For almost every triple with two \(\nu_f\) samples and one \(\nu_e\) sample, vanishing angular loss forces the resulting circle to have full \(\nu_e\)-measure.
Two distinct generalized circles intersect in at most two points, so diffuseness fixes the same circle for almost all triples and hence for both laws.
The converse follows from the same cross-ratio criterion.
Faithfulness converts \(\tau(e1_{C^c}(X))=0\) into \(1_{C^c}(X)e^{1/2}=0\), giving the stated support inclusion also for weights which are not projections.
The computation applies to \(f\) as well.
For positive contractions of trace at least \(\eta\), both laws remain in the compact weak class dominated by \(\mu_X/\eta\).
Their fourfold product varies weakly, and the bounded angular integrand is continuous outside coincidences, a null set also for each limiting product.
Consequently any sequence with vanishing angular loss forces a common limiting carrier of \(\mu_X\)-mass at least \(\eta\).

For the stronger phase assertion consider a bounded sequence of shifts and a vanishing sequence of losses.
The previous compactness conclusion applies.
On a limiting circle of radius \(\rho>0\), writing \(W(z)=(z-c)/|z-c|\), the symbol \(k(z,w)\) equals \(-\overline{W(z)W(w)}\) at distinct circle points.
The center slices and the diagonal have zero limiting product mass, justifying convergence in the varying input measures of the squared symbol error.
The normalized weighted traces of the two legs for the separable symbol are each \(h_n=\tau(e_nW^*U_n)/t_n\) by tracial cyclicity.
This gives \(d(e_n)=1+\operatorname{Re}h_n^2+o(1)\), with the square and its sign as displayed.
Since \(|h_n|\le1\), the absolute value of its imaginary part tends to one.
Choosing a fixed sign on a subsequence gives \(U_n\simeq\sigma iW\) in the right \(e_n^{1/2}\)-weighted Hilbert norm and, by multiplication on the left by \(U_n^*\), \(U_n^*W\simeq-\sigma i1\).
The other needed relation \(|X-c|\simeq\rho1\) follows directly by weak convergence against the continuous squared radius error.

Bounded left multipliers preserve these weighted approximations.
Every right multiplier used in composing them is a uniformly bounded function of \(P_n\), hence commutes with \(e_n\).
Thus \(A_n=b_n-c\simeq W(\rho-\sigma iP_n)\) and \(A_n^*W\simeq\rho+\sigma iP_n\) imply \(A_n^*A_n\simeq\rho^2+P_n^2\) in the asserted order.
For powers, each telescoping term has the difference in the middle, a bounded power of \(A_n^*A_n\) on the left, and a commuting power of \(\rho^2+P_n^2\) on the right.
Both spectra have a common compact upper bound, and \(s\mapsto(\rho-\sigma i\sqrt{(s-\rho^2)_+})^{-1}\) is continuous and bounded there since \(\rho>0\).
Polynomial approximation therefore gives \(C_n=A_n h(A_n^*A_n)\in N\) with \(C_n\simeq W\).
The resulting \(D_n=X-(c+\rho C_n)\) tends to zero in the weighted norm.
Even when \(e_n\) does not commute with \(|D_n|\), tracial positivity gives
\[
 \tau(e_n)\le \tau(1_{[0,r]}(|D_n|))+r^{-2}\|D_ne_n^{1/2}\|_2^2 .
\]
Indeed the low-spectral contribution uses \(e_n\le1\), and the high-spectral contribution uses \(r^2 1_{(r,\infty)}(|D_n|)\le D_n^*D_n\).
The reconstructed shift belongs to \(N\) and can use the uniform C_F0229 estimate with the original vacuum.
Taking the limit at each fixed \(r>0\) and then \(r\downarrow0\) contradicts the positive trace bound.
This excludes the circular carrier and establishes the stronger gap assuming that all lines have mass below \(\eta\).

**Global equality and bounds.**
The integrated nonnegative defect vanishes exactly when \(d(1)=0\), since the singular law has zero mass at the origin.
The exact squared Hilbert norm of \(L-1\) is \(2d(1)\), so equality forces the tensor identity \(k=U^*\otimes(U^*)^{\rm op}\).
The macroscopic phase bound with \(\eta=1\) and \(B=\|b\|\) excludes equality if there is no carrying line, including when a circle carries the law.
On a line of unit direction \(d\) the phase is \(\bar d^2\).
Slicing the tensor identity on the second leg with a normal functional taking a nonzero value on \((U^*)^{\rm op}\) forces \(U\) to be scalar, and the scalar equation gives exactly \(U=\pm d1\).
Each sign gives equality for a shift with the indicated polar factor, and a scalar shift strictly below the spectrum in the line direction gives the positive sign.
For bounded shifts, \(v+w\le2(\|X\|+B)\) on the full spectral square, giving the claimed \(\Delta(1)/(4(\|X\|+B))\) and the qualitative positive lower bound in the no-line case.
Finally a real scalar shift \(s>\|X\|\) gives \(P\ge s-\|X\|\) and \(I_{s1}\le1/(s-\|X\|)\), which proves the unrestricted scalar infimum.
The uniform claims concern weights with a fixed positive lower trace.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0230_v1.md#statement) | All three parts, constants and quantitative lower bounds, measurable weights and exact global equality conditions. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0230_v1.md#argument) | Opposite-leg compression, Hilbert–Schmidt determinant, circle localization, weighted reconstruction, singular mass contradiction and scalar shifts. |
| [Whole-proof finding](#whole-proof-finding) | [Shifted singular-law theorem](../../claims/Yin_C_F0229_v1.md#statement) | Equations (1) and (2), including the two zero kernels, polar phase convention, integrated defect bound and uniform mass control on the reconstructed shift in \(N\). |
| [Whole-proof finding](#whole-proof-finding) | [Normal marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 gives diffuse spectral measure and the off-diagonal unimodular symbol of the actual starred derivative. |
