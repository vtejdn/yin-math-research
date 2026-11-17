---
author: Yin
---

# Conditioned covariance masks and scalar word-chain determinants

<a id="conditioned-core-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T12:21 an agent acting for Yin confirmed its independent whole-proof inspection of [C195v4](../../claims/Yin_C_F0195_v4.md#statement), including the precise primary-source locators.
The reviewer took no part in development and received no development discussion, exploratory notes, explanations by the developers or earlier v4 findings before the initial examination.
The reviewer accepted the conditional comparison, scalar polynomial count, good-dimension logarithms and Brown conclusion, using the source theorems at their checked statements.

A separate inspection of the downstream affine argument identified a missing \(1/N\) in the unscaled Hermitian basis identity that the initial review had missed.
After the author corrected it, the original independent reviewer checked the basis directly and re-examined the whole affected chain at 2026-11-17T12:23.
For the Hermitian Hilbert--Schmidt basis \(U_l^0\), the unscaled sum is \(\sum U_l^0 X U_l^0=\operatorname{Tr}(X)I\); with the GUE factors \(N^{-1/2}\) it is \(\operatorname{tr}_N(X)I\).
The matrix variance of the normalized coefficients is \(\|\sum c_j^2 B_j^2\|\) and their vectorized covariance has norm at most \(N^{-1}\sum c_j^2\|B_j\|_{\rm HS}^2\).
The Gaussian comparison error is \(O(N^{-1}t^{-5})\) with arbitrary frozen drift.
The corrected formula and all downstream conclusions passed the recheck.

Conditioning on the inactivity masks, complementary values and diagonals leaves independent centered bounded coefficients.
The reviewer recalculated the real-covariance Hessian, its two mixed traces and both same-direction terms.
The deterministic mask norm bound permits arbitrary dependence between the mask and the resolvent.
The normalized GUE covariance gives the scalar-free Wick recursion after conditioning on the background matrix algebra.
The reviewer inspected the BBvH23 author edition, pp. 9–12, and the BM20 v3 Theorem 1.1(i) and formulas (3.10), (3.12).
The projected \(s_j/c_j\) give conjugate variables of uniformly bounded \(L^2\) norm, and the scalar Hölder constant has at most polynomial growth in the fixed background bound.
The auxiliary Schur factors transfer the scalar count to the pencil, with the degree-one case requiring no auxiliary block.
The floor acts on the original mixed evaluation spaces and good dimensions.
The review checked the almost-sure and all finite \(L^r\) conclusions, the fixed exceptional shift and the Fubini and local uniform-integrability step for the Brown limit.
The source theorems' original proofs were not re-audited.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#conditioned-core-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Scalar theorem](../../claims/Yin_C_F0195_v4.md#statement) | Finite-variance count and all the conditional determinant and Brown conclusions. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Complete argument](../../claims/Yin_C_F0195_v4.md#argument) | Conditional comparison followed by scalar free regularity and cutoff removal. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Random covariance mask](../../claims/Yin_C_F0195_v4.md#covariance-mask) | The Hessian, pseudocovariance and two-trace terms on the actual masks. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Gaussian comparison](../../claims/Yin_C_F0195_v4.md#free-background) | Corrected physical Hilbert--Schmidt basis, variance, GUE and scalar free equivalent. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Scalar power](../../claims/Yin_C_F0195_v4.md#scalar-fisher) | Free Fisher bound and growth of the Hölder constant. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Ordinary logarithms](../../claims/Yin_C_F0195_v4.md#determinant) | Good sizes, coupling requirements and weak Brown limit. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [BBvH23 Theorem 2.8](../../audits/literature/BBvH23/Yin_U001.md#matrix-resolvent) | The operator-valued resolvent estimate and its drift-independent parameters. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [BM20 Theorem 1.1(i)](../../audits/literature/BM20/Yin_U001.md#finite-fisher-constant) | Free polynomial Hölder estimate with its quantitative constant. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Pair derivatives](../../claims/Yin_C_F0195_v1.md#derivative-bound) | Bounded third raw moments after freezing the tails. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Gaussian interpolation](../../claims/Yin_C_F0195_v1.md#covariance-interpolation) | Raw real Hessian directions and zero-diagonal terms. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Original-law floor](../../claims/Yin_C_F0186_v38.md#floor-statement) | Power probability bound on good sizes under (T). |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Good even dimensions](../../claims/Yin_C_F0186_v9.md#all-even-witness) | The realification and generic-witness inputs. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Exact Schur linearization](../../ledger/Yin_L_F0061_v2.md#linearization-transfer) | The same auxiliary normalization of the ordinary and free determinants. |
| [Whole-proof finding](#conditioned-core-whole-proof) | [Planar control](../../claims/Yin_C_F0186_v4.md#noncompact-planar) | Local square bounds and tightness under arbitrary coupling. |
