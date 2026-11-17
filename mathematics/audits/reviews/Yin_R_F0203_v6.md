---
author: Yin
---

# Finite-variance near-kernel overlap for the quadratic pencil

<a id="finite-variance-overlap-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T12:55 an agent acting for Yin completed independent inspection of [C196v6](../../claims/Yin_C_F0196_v6.md#statement).
It took no part in developing the proof and received no exploration notes, prior v6 findings, author explanations or proof-development dialogue before forming its own findings.
The inspection identified two endpoint definitions in the minor statement.
The final version requires enough available cross columns and compares successive singular values by the strict cross-multiplied inequality, also defined when adjacent values vanish.
The reviewer checked the corrected formulation.

Truncation at \(\sqrt N\log^2(N+2)\) gives the stated polynomial failure probability at a polylogarithmic norm bound and a small enough number of marked endpoints.
The fixed-tuple rectangle tests still have exponentially small failure after conditioning on admissible marks.
The compensator nets have log size \(o(N)\); the entropy of the sparse phases is absorbed by the sufficiently small support coefficient.
The reviewer checked the \(K^{-11}\) phase bound, the \(K^{-46}\) covariance eigenvalue bound and the \(K^{26}/\sqrt N\) scaled column bound.
With at least \((2-\eta)N\) directions these powers leave the stated dictionary entropy reserve.
The fixed-width spectral windows follow from the bounded-range semicircle limit and the small mass outside that range.
The two cited Littlewood--Offord inputs were checked in their stated regimes.
The two singular frames use the same fresh columns, so their failure probabilities are added.
The column-volume normalization gives \(N^{-7r}\), and rescaling the near-full minor preserves a compact nonreal parameter region.
Transpose and adjoint uses exchange the two independent colors and apply the appropriate spectral shift.
The review did not independently re-prove the external small-ball theorems.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Original-law exclusions](../../claims/Yin_C_F0196_v6.md#statement) | Corrected gap and number of columns; fixed laws and all declared parameters. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Truncation and row tests](../../claims/Yin_C_F0196_v6.md#argument) | Finite second moments, walk count and polynomial exceptions. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Sparse phase](../../claims/Yin_C_F0196_v6.md#compensation) | Rectangle isolation and the scale of all approximations. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Finite alphabets](../../claims/Yin_C_F0196_v6.md#dictionary) | Covariance fibers, short columns, rank loss and entropy. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Initial volume](../../claims/Yin_C_F0196_v6.md#first-overlaps) | Measurable near-vector and the conditional fresh column. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Short-column estimate](../../audits/literature/KS26/Yin_U001.md#ks26-u001) | Hypotheses on the truncated second-moment mass and on the column sizes. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Inverse Littlewood--Offord](../../audits/literature/Ngu12a/Yin_U001.md#real-scalar-geometric-inverse) | A positive mass of nonzero raw differences and two real dimensions. |
| [Whole-proof finding](#finite-variance-overlap-whole-proof) | [Projected flag](../../claims/Yin_C_F0351_v2.md#discrete-overlaps) | Gram--Schmidt for both old-minor singular frames. |
