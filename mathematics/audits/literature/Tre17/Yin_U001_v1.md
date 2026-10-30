---
author: Yin
---

# Tre17: Analytic Chebyshev Coefficients

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | The mathematical version read is [arXiv:1608.02216v1](https://arxiv.org/pdf/1608.02216), 2016-08-07, 7 pages. |
| source-locator | The inspected statements are Lemma 3.1 on p.3 and, chiefly, Lemma 5.1 on pp.4-5, including its short proof explanation and the definition of the elliptic polycylinder. |
| inspection | The exact statement and applicability are accepted as a standard approximation input. |

<a id="tre17-u001"></a>
## Tre17-U001: The Elliptic Polycylinder Estimate

Date/reviewer: 2026-09-11, the coordinating agent.
Source identity: Lloyd N. Trefethen, *Multivariate polynomial approximation in the hypercube*, Proceedings of the American Mathematical Society 145(11) (2017), 4837-4844, DOI 10.1090/proc/13623.
Formal publication metadata was verified from the [author-hosted published PDF](https://people.maths.ox.ac.uk/trefethen/hypercube_published.pdf) and [Oxford repository record](https://ora.ox.ac.uk/objects/uuid%3A2b479033-64e3-4096-89e8-6b26d038f331).
The sole bibliographic registry is [literature/readme.md](../../../literature/readme.md).

The mathematical version read is [arXiv:1608.02216v1](https://arxiv.org/pdf/1608.02216), 2016-08-07, 7 pages.
The inspected statements are Lemma 3.1 on p.3 and, chiefly, Lemma 5.1 on pp.4-5, including its short proof explanation and the definition of the elliptic polycylinder.
No complete comparison of the published text and preprint is asserted.

For a function analytic on the product of Bernstein ellipses with parameters rho_j>1, Lemma 5.1 gives its tensor Chebyshev coefficient estimate

\[
|c_{k_1,\ldots,k_s}|\le C_{\widetilde\rho}
\prod_{j=1}^s\widetilde\rho_j^{-k_j}
\qquad(1<\widetilde\rho_j<\rho_j).
\]

This spells out the source's O_epsilon convention: the constants are uniform in the multi-index, after choosing smaller ellipses.
In particular, a function holomorphic near a compact real square has a tensor polynomial expansion whose coefficients remain summable after multiplication by any fixed polynomial in the two degrees.
Affine rescaling of the real intervals causes no change to exponential summability.

The exact statement and applicability are accepted as a standard approximation input.
The source traces the contour-integral estimate to Bochner-Martin, Theorem 11, p.95; that book was not independently inspected.
The main hypercube approximation theorem, its special isotropic analyticity assumption and its Euclidean-degree conclusions are not used.
In particular the consumer invokes Lemma 5.1 directly and does not impose the stronger Assumption A of Section 4.

The [analytic-graph domain argument](../../../claims/Yin_C_F0041_v1.md) supplies the operator-specific weighted adjoint estimate.
Its elementary derivative bound for T_n on [-1,1] is checked there from T_n'=n U_{n-1} and |U_{n-1}|<=n.
It is not attributed to an uninspected theorem here.

Reuse/search record: existing Yin_C_F0040 and Yin_C_F0039 supply polynomial tensors and an unweighted projective expansion, respectively, but do not supply the weighted adjoint-domain convergence needed for an analytic change of coordinates.
Local ledger/literature searches found no such accepted approximation interface.
A primary-source search through Trefethen's author site first located the 2017 Chebyshev lecture outline and the book page, then the exact multivariate Lemma 5.1 above.
Search stopped at this sufficient statement.
No claim of full-paper audit, formal verification or novelty is made.
