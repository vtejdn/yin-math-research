---
author: Yin
---

# Independent review of collinear and strip slice bounds

## Finding

On 2026-11-16T19:26 UTC a reviewer outside proof development independently checked the [candidate decision](../../claims/Yin_C_F0340_v1.md#decision-candidate) dated 2026-11-16T19:23, including its full statement, argument and six declared direct dependency targets.
The reviewer received the fixed claim and scope without development dialogue or a prior finding on this candidate.
The absolute collinear bound and the \(C m^3\) strip bound follow for the stated operator-norm-to-\(L^2\) slice on the full represented word algebra.
Here an unrestricted projection in the two-label conclusion is still subject to the common model assumptions, including the actual partial liberation vacuum; neither commutation with the slots nor finite-dimensionality is required.

Rigid motions and common dilation preserve the normalized cost because \(|H_i|\), \(M_i\), the square root of the inverse-gap sum and the slice norm scale in the asserted way.
After reducing to the real line, separation by \(h\) suffices for the free-corner interval construction: the old slot cuts are spectral projections of the new selfadjoint \(X\), the old algebra embeds with its trace, and the off-slot pair distances after spreading are at least \(3|x_i-x_j|/4\).
The same-slot liberation mass vanishes.
Within a slot the weighted scalar vacuum costs \(O(t_i/h)\le O(M_i)\) in conditional Hilbert norm, and on the annulus \(|x_i-x_j|\asymp 2^\ell h\) the reciprocal-kernel error after averaging costs \(O(2^{-\ell}M_i)\).
This gives the actual distinguished vacuum with \(\|\xi_X\|_2\le C B_x\) even when the real centers are not regularly spaced.

The real slice estimate is used through its proof at terminal weight one.
The represented derivative on \(X,P\) is real, takes algebraic tensor values and is coassociative by its generator values and the product rule.
Its one actual vacuum is selfadjoint by reality and traciality and gives the core adjoint formula for this slice.
Consequently the cited coassociative energy identity and the differentiated unitary series apply, giving \(4\|\xi_X\|_2\|p\|\) without requiring a conjugate variable for \(P\).
For a smooth slot indicator, uniform \(C^1\) polynomial approximation on a containing real interval controls its divided differences uniformly off the diagonal, and hence in the diffuse coarse Hilbert space.
The Leibniz rule extends simultaneous operator-norm input convergence and graph-value convergence to each fixed word with \(P\).
The expectation of a corner function is its normalized conditional mean times its slot, so projecting the two tensor legs averages the reciprocal against the product of the two interval probabilities.
The projected slice is the old expectation of the continuous slice, a contraction, and the projected word derivative is an outer derivation by bimodularity.
It has zero inner diagonal on every word because the corresponding insertion vanishes on each generator and commutes with the outer actions.

For \(T=X'-Y'\) of the unit-scale intervals, symmetry gives \(dA_1(d)=\mathbb E[1/(1-T^2/d^2)]\) for \(|d|\ge1/2\).
Since \(|T|\le1/4\), this quantity is at least one with error \(O(|d|^{-2})\) and derivative \(O(|d|^{-3})\) at infinity.
After the smooth cutoff, its reciprocal minus one is in \(H^1(\mathbb R)\), whose Fourier transform is integrable by weighted Cauchy–Schwarz.
Rescaling its Fourier measure and adding the mass at frequency zero realizes \(1/(dA_h(d))\) on \(|d|\ge h\) with universal variation.
For a separated unitary insertion the traced product rule yields \(E'(pw)v-pE'(w)v\), bounded by twice the one-input slice cost on the unit ball.
The Fourier integral therefore recovers the exact discrete derivative on every word with an absolute slice bound, without assuming a column estimate.

For the strip encoding, with \(b=n_i-n_j\) and \(k=y_i-y_j\), the real gap is \(b+k/(2m)\).
For \(b=0\) on distinct slots the planar gap is exactly \(2m\) times the real gap; for \(b\ne0\) the real gap has modulus at least \(|b|/2\) and the planar gap at most \(m|b|\).
The resulting inequality \(|c_i-c_j|\le 2m|x_i-x_j|\) controls the mixed budget and, by inclusion of balls of radii \(s,2ms\) above the respective lower cutoffs, the maximal densities.
For \(|b|\le2m\) the center mass is at most \(3m M_i(c)\) and the difference of reciprocal gaps on distinct slots has modulus at most \(2m+1\).
For \(|b|>2m\), its modulus is \(O(m/|b|^2)\); a horizontal shell of scale \(R\ge 2m\) is contained in a planar ball of radius \(O(R)\), so the shell errors sum to \(O(M_i(c))\).
This gives \(B_x\le C m^2 B_c\), retaining cancellation in \(H_i(c)\).

The ratio of the real to the complex gap is one plus \((1/(2m)-i)k/(b+ik)\).
For either sign of \(k\ne0\), the last fraction is \(-i\) times the Fourier transform provided by density \(|k|e^{-|k|t}\) on \(t>0\) with character \(e^{i\operatorname{sgn}(k)bt}\); its measure has variation one.
Normalized circle characters isolate each integer row difference with the same variation bound.
Together they give separated old marginal unitaries, and the number of nonzero row differences is at most \(2(m-1)\).
This proves the additional \(O(m)\) cost, also covering one row when the correction is empty, and a rotation gives the column case.
There is no estimate here independent of the strip width on unrestricted planar lattices.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0340_v1.md#decision-candidate) | Fixed candidate and selected support. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0340_v1.md#statement) | All real-separated configurations up to rigid motion and all consecutive horizontal or vertical strips of the asserted width. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0340_v1.md#argument) | Entire interval construction, exact recovery, two Fourier estimates and strip comparison. |
| [Finding](#finding) | [Finite-label data](../../claims/Yin_C_F0339_v1.md#statement) | Actual model, word algebra, trace, killed projection, discrete derivative and precise budget. |
| [Finding](#finding) | [Free corner noises](../../claims/Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Interval laws, expectations, extension of liberation, and inverse-gap estimates. |
| [Finding](#finding) | [Spread scalar vacuum](../../claims/Yin_C_F0339_v1.md#the-scalar-vacuum-of-the-spread-measure) | Quantitative recovery of an actual distinguished derivative from an arbitrarily separated real spread. |
| [Finding](#finding) | [Projection approximation](../../claims/Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Graph and norm approximation, projected product means and their use with interval averaging. |
| [Finding](#finding) | [Real slice bound](../../claims/Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) | Unweighted coassociative calculation requiring only the actual distinguished derivative. |
| [Finding](#finding) | [Separated insertion](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | One-input traced product rule and integration of separated unitary insertions against a finite measure. |
