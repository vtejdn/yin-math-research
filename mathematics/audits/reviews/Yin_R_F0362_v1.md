---
author: Yin
---

# Support witnesses on the symmetric sign cube

<a id="sign-support-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T12:59 an independent agent acting for Yin inspected the [fixed C354v1 theorem](../../claims/Yin_C_F0354_v1.md#statement) and its necessary fixed inputs.
The reviewer had no development role and received no development discussion, earlier findings, drafts or author explanations before the inspection.
For any fixed eligible even block count \(r\), the proof gives a symmetric sign-support witness in every dimension \(rp\) for all sufficiently large odd primes \(p\).

The reviewer recomputed the Fourier decomposition, the zero and nonzero diagonal variances \((2p-1)/(rp)\) and \((p-1)/(rp)\), and the real and imaginary off-diagonal variances.
At each prime all nonzero frequencies have identical marginal laws.
The centered triangular arrays give the stated GOE and GUE fiber limits at fixed \(r\), and the determinant zero sets are closed null sets under both limits by the initial unrestricted real symmetric witness, even for complex coefficients.
Over the coefficient field \(K\), of finite degree \(d\) over its chosen purely transcendental subfield, adjoining \(\sqrt p\) leaves at least \((p-1)/(2d)\) automorphisms acting on the cyclotomic generator.
All coefficients and the normalization are fixed, and the inverse powers in the transposed blocks transform to the correct other-frequency lower entries.
There are at most \(2d\) nonzero orbits, so the union bound uses no independence between fibers and requires no quantitative central limit rate.
The word-chain pivot gives the same support statement at every prescribed scalar shift.
The original iid sign ensemble receives only a positive probability of invertibility from this construction; the probability tending to one belongs to the auxiliary circulant ensemble.
The finding gives no least-value floor under the original law.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#sign-support-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#sign-support-whole-proof) | [Support and model](../../claims/Yin_C_F0354_v1.md#statement) | Arbitrary full affine pencils, fixed coefficients, even block count, and scalar specialization. |
| [Whole-proof finding](#sign-support-whole-proof) | [Block-circulant construction](../../claims/Yin_C_F0354_v1.md#argument) | Sign symmetry, physical normalization and a nonzero starting polynomial. |
| [Whole-proof finding](#sign-support-whole-proof) | [Gaussian fiber limits](../../claims/Yin_C_F0354_v1.md#fiber-limits) | Correct covariance and probability of singularity in each marginal. |
| [Whole-proof finding](#sign-support-whole-proof) | [Bounded orbit count](../../claims/Yin_C_F0354_v1.md#galois-orbits) | Arbitrary complex coefficients and union over the correlated frequencies. |
| [Whole-proof finding](#sign-support-whole-proof) | [Free logarithm](../../claims/Yin_C_F0352_v1.md#statement) | The finite free logarithm of a full pencil. |
| [Whole-proof finding](#sign-support-whole-proof) | [Unrestricted symmetric witnesses](../../claims/Yin_C_F0186_v9.md#all-even-witness) | Eventual even sizes under realification with unchanged complex coefficients. |
| [Whole-proof finding](#sign-support-whole-proof) | [Word-chain pivot](../../ledger/Yin_L_F0061_v2.md#linearization-transfer) | Invertibility at exactly the same scalar evaluations. |
