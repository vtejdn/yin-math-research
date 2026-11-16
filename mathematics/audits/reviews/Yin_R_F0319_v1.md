---
author: Yin
---

# Review of singular atoms after compression by a killed projection

## Whole-proof finding

At 2026-11-16T16:45 UTC a separately assigned agent for Yin independently reviewed the complete C_F0310 v1 candidate fixed at 16:41 UTC.
The reviewer worked from the fixed candidate and its mathematical inputs and received no development dialogue, author explanation, exploration notes or prior findings on this candidate.
The meet identities, the sharp total atomic mass bound and the trace-half diffuseness conclusion hold under the stated relative hypotheses.

The ambient graph construction gives the same phase at \(Z^*\) when \(p\) is obtained by bounded strong-star approximation from killed coefficients.
For a bounded selfadjoint word \(x\), uniform approximation of \(h_n'\) followed by integration approximates \(h_n\) and its divided difference, including the diagonal derivative.
Here \(\|h_n\|_\infty\le 1/(2\sqrt n)\), and the divided differences are bounded by one and converge pointwise to the singleton pair indicator.
Closedness therefore forces the outer compression of \(\delta x\) at that pair to vanish.

At the positive eigenvalue \(a^2\) of \(B^*B\), the terms of this compressed product rule, after dividing by \(a\), are \((e\otimes w^{\rm op})k\) and \(w^*\otimes e^{\rm op}\).
Multiplication on the left by \(e\otimes(w^*)^{\rm op}\) produces \(q=ww^*\) in the first term's opposite leg.
Multiplication on the right by the marginal difference uses (3) with \(k\) on the required side.
The subsequent right cut kills precisely the terms containing \(e(1-p)\) or \(w^*(1-p)\).
If \(w^*\) were proportional to \(q\), its initial and final supports would agree, and \(pZp\) would have an eigenvalue on the nonzero subprojection \(e=q\).
The small-radius estimate from C_F0309 excludes the kernel at this shifted scalar for every complex shift.
The remaining simple tensors in (5) consequently have independent second legs.
The resulting first-leg equations put both \((Z-\lambda)e=aw\) and \((Z-\lambda)^*w=ae\) in the ambient algebra.
Hence \(e\le r_a\) and \(w=ue\).
Conversely any vector in the stated meet belongs to the corner and its image under \(Z-\lambda\) stays there, so applying the compressed adjoint gives \(a^2\) times that vector.
Conjugating by \(u\) also gives the left formula because \(u\) commutes with \(r_a\).
The trace comparison follows from \(e\le r_a\).

For \(X=(1-p)Zp\), the inverse rule at fixed \(s>0\) gives \(sL_s\cdot\delta X\cdot R_s-V_s\cdot\delta X^*\cdot V_s\) for the derivative of \(V_s\).
The geometric approximants converge in graph norm even with these general derivative values since the differentiated powers have a summable bound proportional to \(nq^{n-1}\), \(q<1\).
After multiplying by \(s\), the input converges to zero and the second differentiated term converges to zero by the bounded strong-star convergence of \(\sqrt{s}V_s\) and its adjoint.
The first term converges to the compression of \(\delta X\) by the ambient left and right kernels.
Inserting \(\Phi\delta X=(1-p)\otimes p^{\rm op}\) leaves exactly \(f'_0\otimes(e'_0)^{\rm op}=0\).
Thus one rectangular kernel vanishes, while the polar partial isometry equates \(t-\tau(e'_0)\) and \(1-t-\tau(f'_0)\).
This gives \(\tau(e'_0)=(2t-1)_+\).
All positive atom projections lie in \(e'_0\), and the zero atom vanishes in the corner by C_F0309.
Their orthogonal sum gives (2) after division by \(t\), which is strictly less than one for every proper compression and vanishes for \(t\le 1/2\).

For a single supporting circle the one possible positive atom coincides with the whole rectangular right kernel.
The Haar Laurent vacuum is the generator itself, and the double trace of each differentiated mixed centered reduced word vanishes in the free product with the two-point projection algebra of weights \(t,1-t\).
This verifies that the equality examples meet the exact derivative and vacuum assumptions at every stated trace.
The dependency check covered their specific interfaces below.
The general mixed slice norm remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Candidate](../../claims/Yin_C_F0310_v1.md#decision-candidate) | Exact fixed 16:41 UTC decision and selected mathematical scope. |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0310_v1.md#statement) | Individual right and left singular atom projections for each scalar shift, total mass bound, trace-half diffuseness and sharpness. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0310_v1.md#argument) | Complete proof from the atom derivative and spatial tensor equations to the rectangular rank and equality examples. |
| [Whole-proof finding](#whole-proof-finding) | [Ambient graph and phase](../../claims/Yin_C_F0309_v1.md#derivation-and-vacuum-on-the-compressed-generated-algebra) | Closability and starred marginal phase on words also containing a projection of the killed von Neumann algebra. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar shifts](../../claims/Yin_C_F0309_v1.md#statement) | Trivial kernel for each scalar shift, used for the independence of the second tensor legs and for the zero singular mass. |
| [Whole-proof finding](#whole-proof-finding) | [Resolvent differentiation](../../claims/Yin_C_F0229_v1.md#argument) | Geometric inverse approximation and opposite-algebra product rule with both derivative values retained for the rectangular operator. |
| [Whole-proof finding](#whole-proof-finding) | [Free-product vacuum](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Laurent vacuum and its preservation upon extending by zero on a freely adjoined projection factor. |
