---
author: Yin
---

# BCG25: A Scalar Exterior Variational Formula

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Exact artifact: arXiv:2506.19064v1, 25 pages; title-page and arXiv author-order discrepancy recorded in the sole bibliographic.

Passages: Inspected locators: Theorem 1.1 and equations (1.12)-(1.15), printed/PDF pp.2-3; equation (1.6), p.1; Section 1.8.1, p.6; Lemmas 4.1-4.2 and the surrounding discussion, pp.17-18.

Inspection: Coverage state: Read, with the selected derivative computation checked.


<a id="bcg25-u001"></a>
## BCG25-U001: Semicircle Specialization and Branch Restriction

Recorded 2026-09-13 after primary-source access on 2026-09-12.
Reader: research agent the affine-source reader.
Exact artifact: arXiv:2506.19064v1, 25 pages; title-page and arXiv author-order discrepancy recorded in the sole bibliographic.
Coverage state: Read, with the selected derivative computation checked.
The following exterior theorem is accepted as a source comparison; its original full proof was not audited.
It is not a proof premise of Yin_C_F0119-Yin_C_F0123 or the new [general matrix argument](../../../claims/Yin_C_F0124_v1.md).

### Checked Statement and Conventions

The [primary PDF](https://arxiv.org/pdf/2506.19064) identifies v1 in its margin.
Inspected locators: Theorem 1.1 and equations (1.12)-(1.15), printed/PDF pp.2-3; equation (1.6), p.1; Section 1.8.1, p.6; Lemmas 4.1-4.2 and the surrounding discussion, pp.17-18.
Page numbering agrees with the PDF sequence.

Let \(\nu\) be a compactly supported probability measure on \(\mathbb R\), let \(\beta>0\), and let \(\rho=\mu_{\mathrm{sc},\beta}\boxplus\nu\), where the semicircle has variance \(\beta^2\).
Define
\[
 U_\rho(z)=\int\log|z-\lambda|\,d\rho(\lambda),\quad
 G_\rho(z)=\int(\lambda-z)^{-1}\,d\rho(\lambda),\quad
 z_*=\inf\operatorname{supp}\rho,\quad
 g_*=\lim_{z\uparrow z_*}G_\rho(z).
\]
For real \(z<z_*\), equation (1.6) gives
\[
 U_\rho(z)=
 \inf_{\substack{0<g<g_*\\\beta^2g<\inf\operatorname{supp}\nu-z}}
 \left\{\frac{\beta^2g^2}{2}
       +\int\log(\lambda-z-\beta^2g)\,d\nu(\lambda)\right\},
                                                               \tag{B1}
\]
with unique minimizer \(G_\rho(z)\).
Theorem 1.3 characterizes the edge data.

### Checked Mechanism and Limitations

Differentiation of the displayed objective yields
\[
 \beta^2\left(g-\int
       \frac{d\nu(\lambda)}{\lambda-z-\beta^2g}\right).
\]
The denominator is strictly positive throughout the feasible set, so differentiation under the compactly supported integral is locally justified.
Lemma 4.2 identifies the sign relative to the physical transform on the specified interval.
The source expressly explains on p.17 that the physical local minimum need not be a global minimum on the unrestricted domain.
Its general proof and the edge characterization were not fully re-audited.

For isotropic matrix covariance, the spectral law is a scalar free convolution with the empirical eigenvalue law of the drift.
Thus (B1) is an applicable exterior comparison for [Yin_C_F0122](../../../claims/Yin_C_F0122_v1.md).
It does not provide that record's full real-axis ordered minimax.
The scalar order and scalar \(R\)-transform used here also do not establish a variational principle for an arbitrary matrix covariance.
No matrix extension, bulk theorem, whole-paper audit or novelty claim is inferred.
