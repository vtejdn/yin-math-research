---
author: Yin
---

<a id="bbvh23-u001"></a>
# Gaussian resolvent comparison with deterministic drift

Inspected edition and pagination are described in the [source notes](readme.md).

<a id="matrix-resolvent"></a>
## The Gaussian matrix resolvent

The inspected passages are the definitions of the Gaussian and free models in (2.1) on p. 9, the centered matrix parameters on p. 10, and Theorem 2.8 spanning pp. 11–12.
For fixed Hermitian coefficients \(A_0,\ldots,A_n\), let \(X=A_0+\sum A_j g_j\) with independent standard real normal variables, and replace the \(g_j\) by a standard free semicircular family to define \(X_{\rm free}\).
At \(Z=itI,\ t>0\), the norm of the difference between the expected resolvent and the matrix-valued expectation of the free resolvent is at most
\[
 t^{-5}\left\|\sum_{j=1}^n A_j^2\right\|
 \sup_{\operatorname{Tr}|M|^2\le1}\sum_{j=1}^n |\operatorname{Tr}(A_j M)|^2 .
\]
Both factors use the centered coefficients, so the estimate is uniform in the deterministic shift \(A_0\).
The trace in the supremum is unnormalized.
Yin uses this theorem at its stated scope for the [conditional Gaussian comparison](../../../claims/Yin_C_F0195_v4.md#free-background).
The original proof in Section 5 was not independently audited.
