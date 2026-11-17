---
author: Yin
---

# A diagonal sign chain at a stable energy of a Hermitian pencil

<a id="monotone-sign-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T13:29 an independent agent acting for Yin reviewed the [fixed C356v1 proof](../../claims/Yin_C_F0356_v1.md#statement), its original-source Kronecker local law and the directly used determinant modules.
The reviewer took no part in developing it and received no prior findings, development explanations or drafts about this proof.
The whole theorem and the two stated families of examples pass within the indicated spectral stability regime.

The reviewer checked the Kronecker model and [AEKN19 Lemma B.1(i)](../literature/AEKN19/Yin_U001.md#stable-block-law) in the actual preprint at pp. 27–28.
The fixed-ray hypotheses give the required high-probability physical diagonal resolvent bounds, without a separate flatness condition.
Conditioning the sign count in its central range loses only a polynomial factor.
The resolvent transfer to the matrix independent of its first-color diagonal signs uses the inverse of \(1+R(H_*-H)\) at the wider window.
The negative-site estimate, the Gaussian integration-by-parts moment bound, and the conditional net for the next block of flips have the asserted exponents.
The latter compares \(N^{3/32}\) with \(N^{1/32}\log N\).
The min-max improvement exceeds \(2N^{-3}\) whenever an eigenvalue lies in the tested interval.
The inertia calculation includes an endpoint kernel by counting eigenvalues at most \(-1\), and only the initial guard is conditioned on in the estimate of the expected positive increment.
The final incidence count gives the advertised failure power, with sufficient slack.

The reviewer checked fullness, the use of finite-variance clipping before the translation-regular step, dyadic Borel--Cantelli and the full-size limsup under arbitrary coupling.
In the Pauli example the three specified random coefficients have full rank; its span can contain rank-one combinations.
The stability denominators on the open bulk interval are bounded away from zero.
The small tridiagonal drift retains stability, and the triangular pivot gives the stated order of multiplication in the scalar recursion and the log factor \(m\).
The finding gives a polynomial floor at the prescribed stable energy and makes no all-energies or all-dimensions almost-sure assertion.
The original proof of the external local law was not fully re-audited.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#monotone-sign-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Stable Hermitian sign model](../../claims/Yin_C_F0356_v1.md#statement) | Original independent signs, a positive definite direction and stability of the fixed energy. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Local projection bounds](../../claims/Yin_C_F0356_v1.md#argument) | The two window scales and the random sign count. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Conditional sampling](../../claims/Yin_C_F0356_v1.md#negative-sites) | Selective mass on sites still available for flips. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Spectral flow](../../claims/Yin_C_F0356_v1.md#crossings) | Min-max gain, crossing expectation and the original-law probability. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Coefficient and scalar examples](../../claims/Yin_C_F0356_v1.md#examples) | Pauli matrices, tridiagonal couplings and normalized scalar continuants. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Local law at stable parameters](../../audits/literature/AEKN19/Yin_U001.md#stable-block-law) | Ray assumptions, normalization and estimates on physical resolvent blocks. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Finite-variance clipping](../../claims/Yin_C_F0186_v40.md#band) | Log-band control without the translation hypothesis. |
| [Whole-proof finding](#monotone-sign-whole-proof) | [Finite free log](../../claims/Yin_C_F0352_v1.md#statement) | Application to a full Hermitian pencil. |
