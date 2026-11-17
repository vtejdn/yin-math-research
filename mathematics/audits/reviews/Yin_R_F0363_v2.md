---
author: Yin
---

# Null-line reduction for real binary quadratic polynomials

<a id="binary-null-lines-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T13:41 an independent agent acting for Yin reviewed the [fixed C355v2 result](../../claims/Yin_C_F0355_v2.md#statement), including the arguments for nonzero affine coefficients.
The reviewer had no development role and consulted no drafting conversation, exploration notes or earlier v2 findings.
The result is supported for the original model with both the upper and the diagonal input laws fixed as in F0012.

In the two null directions the off-diagonal entries of the transformed quadratic tensor are nonzero and have nonzero sum, giving \(\lambda\ne0,-1\).
The diagonal shifts absorb the two linear coefficients and leave all cross blocks, selected site masks and physical pair spans unchanged.
The row update uses the \(V'x\) term for the shifted second form.
At \(n/N=a\) the congruence of the canonical three-channel companion requires precisely \(d_U/\sqrt a,d_V/\sqrt a,(z-c')/a\).
The reviewer checked the resulting fixed-clip comparisons, the uniform free log bound on the compact full family and the small moving drifts needed at the near-full minor.
Both centered conditional row variances and the affine spectral-window inequalities survive the shifts.
A real or complex sparse-vector test still sees the original top quadratic via its second rectangular difference.
Each nonzero variable combination in the three-dimensional pencil retains rank two and using the constant gives an invertible bottom block.

If either conditional variance vanishes almost surely then the transformed raw law lies on a measurable planar-null graph.
Any positive absolutely continuous component rules this out.
For signs the differences of the four words give exactly the required null-line direction test.
A single direction suffices for the finite-variance planar and prescribed nonreal claims; the stated two-direction test gives the additional real-axis sign assertion.
The ordinary limsup uses the clipped upper bound and dyadic almost-sure convergence at each prescribed parameter.
The reviewer used existing inputs at the inspected interfaces without re-proving all their external foundations.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#binary-null-lines-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Binary coefficient and law hypotheses](../../claims/Yin_C_F0355_v2.md#statement) | Nondegenerate indefinite symmetric part, full tensor and the additional conditional-variance requirements. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Affine null-line reduction](../../claims/Yin_C_F0355_v2.md#argument) | Both mixed powers and the actual moving drifts under physical normalization. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Input-law tests](../../claims/Yin_C_F0355_v2.md#laws) | A positive absolutely continuous component and the exact sign-word directions. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Conditional physical row](../../claims/Yin_C_F0355_v1.md#argument) | Joint original law and the row-by-row exposures. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Conditional restoration](../../claims/Yin_C_F0355_v1.md#conditional-tests) | Clipping, Fourier tests and the two-dimensional update. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Real sign targets](../../claims/Yin_C_F0355_v1.md#real-signs) | Bidirectional conditional variation and selected physical subspaces. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [General affine-quadratic trims](../../claims/Yin_C_F0186_v42.md#statement) | Physical normalization and nonreal parameter comparisons. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Full compact companions](../../claims/Yin_C_F0352_v1.md#statement) | Uniform logarithmic integrability for the moving free matrices. |
| [Whole-proof finding](#binary-null-lines-whole-proof) | [Real-axis initialization](../../claims/Yin_C_F0351_v7.md#trim) | Two-sided spectral gaps, fixed-fraction scaling and borderline small terms. |
