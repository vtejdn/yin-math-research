---
author: Yin
---

# Lat05: a fourth-moment bound for the expected matrix norm

<a id="lat05-u001"></a>
## Theorem 2 and its exact applicability

Use [the published original](readme.md), Theorem 2 on printed p. 1274, PDF p. 2.
The statement concerns any finite real matrix \(X=(X_{ij})\) of independent centered entries.
Its Euclidean operator norm satisfies
\[
 \mathbb E\|X\|
 \le C\left[
    \max_i\Bigl(\sum_j\mathbb E X_{ij}^2\Bigr)^{1/2}
   +\max_j\Bigl(\sum_i\mathbb E X_{ij}^2\Bigr)^{1/2}
   +\Bigl(\sum_{ij}\mathbb E X_{ij}^4\Bigr)^{1/4}
       \right],
\]
with a universal constant.
The dimensions may be rectangular and the individual entry distributions need not be identical.
Deterministic zero entries are allowed.
The statement and its conditions have been directly checked in the original and are accepted at this scope.

The adjacent proof on printed pp. 1274--1275 was read for its reduction from Theorem 1: symmetrization, a comparison with Gaussian signs, and row/column square-sum bounds.
Theorem 1's later Gaussian norm proof was not audited.
This is source inspection during development, not independent review of a project theorem or a complete source-proof audit.

For a real symmetric Wigner matrix, the theorem cannot be applied directly to the full reflected array as if all its entries were independent.
It can be applied to its centered strict upper triangular part \(U\), with zeros elsewhere, and then \(\|U+U^T\|\le2\|U\|\).
For normalized centered truncations of a fixed off-diagonal law with finite fourth moment, row and column variance sums and the sum of all fourth moments are bounded uniformly in the dimension.
This gives a dimension-independent expected norm bound for that centered off-diagonal part.
A separate diagonal estimate and a bound for the truncated mean are still required when the diagonal law has only a second moment or the truncation is uncentered.
