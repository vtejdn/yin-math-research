---
author: Yin
---

# Tol17: A selected global Cauchy-curvature interface

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [arXiv:1408.6979v2](https://arxiv.org/abs/1408.6979v2), revised 2015-01-31, 112 PDF pages; no canonical local PDF or checksum retained. |
| source-locator | Proposition 17.1 and equation (17.5) are on printed p. 94 / PDF page 94; Theorem 17.2 is on printed p. 95 / PDF page 95. |
| inspection | This unit records an established theorem interface; it is not a full monograph or original-proof audit. |

<a id="tol17-u001"></a>
## Tol17-U001: The truncated curvature identity

Date/actor: 2026-09-11, the dual-domain research agent.
Source type: research monograph; publication state: published; access: public preprint.
Consumer: [the normal Cauchy-core continuation](../../../claims/Yin_C_F0044_v1.md), Sections 3-5.
Source key and unit allocated by the coordinating agent.
This unit records an established theorem interface; it is not a full monograph or original-proof audit.

### Source identity and inspected version

Xavier Tolsa, *Rectifiable measures, square functions involving densities, and the Cauchy transform*, Memoirs of the American Mathematical Society **245** (2017), no. **1158**, [DOI 10.1090/memo/1158](https://doi.org/10.1090/memo/1158).
The [author's publication list](https://mat.uab.cat/~xtolsa/xtolsarecentpapers.html) confirms this journal year.
The coordinating agent also checked the institutional metadata and the AMS catalog's 2016 copyright/catalog label; the project key follows the author's 2017 volume citation, without treating that label as a different mathematical version.

The inspected artifact is [arXiv:1408.6979v2](https://arxiv.org/abs/1408.6979v2), revised 2015-01-31, 112 PDF pages.
The [unversioned primary PDF endpoint](https://arxiv.org/pdf/1408.6979) delivered that version.
Proposition 17.1 and equation (17.5) are on printed p. 94 / PDF page 94; Theorem 17.2 is on printed p. 95 / PDF page 95.
The author and independent proof reviewer the polynomial-core research agent checked the version and selected passages separately.
No canonical local PDF or checksum is retained.
Published pagination and theorem numbering have not been independently compared.

### Exact imported statement and definitions

Let nu be a finite positive Radon measure on C with

\[
 \nu(B(z,r))\le Lr\qquad(z\in\mathbb C,\ r>0).
\]

Set

\[
 C_\epsilon\nu(z)=\int_{|z-w|>\epsilon}\frac{d\nu(w)}{z-w},
 \quad
 c_\epsilon^2(\nu)=
 \iiint_{\min(|z-w|,|w-v|,|v-z|)>\epsilon}
 c(z,w,v)^2\,d\nu(z)d\nu(w)d\nu(v),
\]

where c is the reciprocal circumradius, zero for collinear triples.
Proposition 17.1 gives an absolute constant a such that

\[
 \left|\|C_\epsilon\nu\|_{L^2(\nu)}^2
        -\tfrac16 c_\epsilon^2(\nu)\right|
 \le aL^2\nu(\mathbb C)\qquad(\epsilon>0).
\]

The source attributes this established identity to Melnikov-Verdera, IMRN (1995), 325-331.
Its original proof is not re-audited here.

### Applicability and limits

The consumer checks positivity, finiteness and linear growth for both mu and the auxiliary measure (1+f/2)mu.
The weighted comparison and actual dual-domain deductions are project proofs requiring their own review.
Linear growth is essential to the imported statement and is not obtained from the vacuum-adjoint condition.

Theorem 17.2 was inspected only to locate the stronger, every-square truncated testing condition for L2 operator boundedness.
It is not used in the consumer's global infinity-to-2 argument.
This unit imports no principal-value convergence from an L2 distributional density, no arbitrary-growth identity, and no extension to noncommutative mixed polynomials.
