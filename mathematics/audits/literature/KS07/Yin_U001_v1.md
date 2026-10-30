---
author: Yin
---

# KS07: Selected Holomorphic Word Inputs

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected artifact: online [arXiv:math/0512481v2](https://arxiv.org/pdf/math/0512481), revised 2005-12-28, 27 PDF pages. |
| source-locator | Definition 1.2 and Theorem 1.3, printed pp. 2-3, concern a free identically distributed family of bounded R-diagonal elements $a_i$ in a tracial C*-probability setting. |
| inspection | Its original complete proof is not independently audited here. |

For the finite subfamily used in the project and a homogeneous holomorphic polynomial $p$ of positive degree $m$, Section 4.1, printed p. 17, equations (4.1)-(4.3), computes for degree $m$ The R-diagonal cumulant definition was also read in Section 2, printed pp. 7-8.

## KS07-U001

Date and reviewer: 2026-09-09, the L2-Kronecker scope agent.
Source identity: Todd Kemp and Roland Speicher, *Strong Haagerup inequalities for free R-diagonal elements*, Journal of Functional Analysis 251(1) (2007), 141-173, DOI [10.1016/j.jfa.2007.03.011](https://doi.org/10.1016/j.jfa.2007.03.011).
Inspected artifact: online [arXiv:math/0512481v2](https://arxiv.org/pdf/math/0512481), revised 2005-12-28, 27 PDF pages.
The registry owns its bibliographic and acquisition fields; no local PDF was retained here.

### Statement and hypotheses

Definition 1.2 and Theorem 1.3, printed pp. 2-3, concern a free identically distributed family of bounded R-diagonal elements $a_i$ in a tracial C*-probability setting.
For the finite subfamily used in the project and a homogeneous holomorphic polynomial $p$ of positive degree $m$,
\[
\|p\|\le C_a\sqrt m\,\|p\|_2,
\]
where $C_a<\infty$ depends on the common distribution.
Use nonzero $a_i$ when normalizing their L2 norms.
The degree-zero bound is handled separately by scalar norm equality.
A faithful finite von Neumann trace meets the source assumptions.

The theorem is accepted as an established external input at statement and applicability level.
Its original complete proof is not independently audited here.
The exact optimal constant is unnecessary for the application and is not transcribed from the parsed formula.

### Monomial L2 interface

Section 4.1, printed p. 17, equations (4.1)-(4.3), computes for degree $m$
\[
\left\|\sum_{|w|=m}c_w a_w\right\|_2^2
=\sum_{|w|=m}|c_w|^2\|a_1\|_2^{2m}.
\]
The local proof reconstruction is in [Yin_C_F0017, Section 2](../../../claims/Yin_C_F0017_v1.md#yin_c_f0017): in $\tau(a_v^*a_w)$, the noncrossing-cumulant expansion has all adjoints before all nonadjoints.
Alternation forces two-element blocks, and the only possible noncrossing pairing is the nested one.
Freeness forces matching word labels.
Unequal lengths have zero moment by the same pairing requirement.
Thus normalized monomials form an orthonormal basis of the closed holomorphic subspace, not generally of the whole L2 space.

The R-diagonal cumulant definition was also read in Section 2, printed pp. 7-8.
The elementary word-norm argument was independently reconstructed; this does not constitute a review of the full strong Haagerup inequality.

### Scope and access limitations

The estimate covers words without adjoints.
It does not imply a bound for arbitrary mixed-star polynomials or affiliated rational expressions.
Yin_C_F0017 supplies a separate minimal-realization and matrix-entry argument when actual coefficient summability is present.

Reading used online parsed PDF formulas.
Requests for source page screenshots failed, and retrieval of the author-hosted journal PDF timed out.
No visual or journal/preprint version comparison is claimed.
The source's Brown-measure paragraph was not used: the exact Brown-support/spectrum distinction remains governed by the independently identified HL00 interface.
This unit makes no source-wide accuracy assessment.
