---
author: Yin
---

# DHH+25-U001: Block product support, endpoint restriction and positivity boundary

## Source and inspection

[Source and edition notes](readme.md).

Source edition: 109-page arXiv:2510.10712v1, submitted 2025-10-12; inspected diagnostic copy distinct from canonical intake.

Passages: Theorems 1.25/1.27/1.28 pp. 13-15; Corollary 5.4 p. 74; Proposition 5.18/Corollary 5.19 p. 82; Proposition 6.4-Theorem 6.7 pp. 84-87.

Inspection: 2026-09-11 selected primary PDF text/HTML checked and deeper source interfaces read after an endpoint contradiction; no full source audit or separate independent review.


<a id="dhh+25-u001"></a>
## Selected source scope

The reading dates, artifact distinctions, substantive source content and actual limits below remain those of that original inspection.

## Retained selected source content

<a id="dhh+25-product-support"></a>
Date: 2026-09-11.
Reader: the spectral-extension research agent.
This supplements the existing [Miy26-U008 interface](../Miy26/Yin_U004.md#miy26-u004) and [circular product adaptation](../Miy26/Yin_U006.md#miy26-u006) for a non-circular application.
The sole bibliographic identity is [DHH+25 in references.bib](../../../literature/references.bib).

## Source and scope

The exact source is the [109-page arXiv v1 PDF](https://arxiv.org/pdf/2510.10712v1), submitted 2025-10-12.
Theorem 1.25 and formula (1.17) are on p. 13; Theorem 1.27 and formulas (1.19)-(1.21) span pp. 13-14; Theorem 1.28 is on p. 15.
Printed and PDF page numbers coincide.
These pages were read again from extracted primary-PDF text, alongside the [primary HTML](https://arxiv.org/html/2510.10712v1).
After an endpoint contradiction was found, the relevant review was deepened to Corollary 5.4 (p. 74), Proposition 5.18 and Corollary 5.19 (p. 82), and Proposition 6.4 through Theorem 6.7 (pp. 84-87), including their cited subordination input.
Block-freeness remains an accepted external theorem; the Brown-support conclusion now requires the explicitly separated repair below.

A temporary diagnostic copy was downloaded to `tmp/DHH+25-spectral-selection.pdf`: 4,644,920 bytes.
It is not a new canonical literature file, does not replace the existing intake, and does not establish identity with any separately served revision.
The initial web-tool PDF access was intermittent; the direct versioned-PDF retrieval and local extraction supplied the final exact page checks.

## Intended application and the initial source interface

Let \(k\ge2\), let \(a_1,\ldots,a_k\) be free identically distributed bounded R-diagonal elements of a finite faithful tracial von Neumann algebra, and suppose

\[
\|a_i\|_2=1,\qquad
\int_0^\infty x^{-2}\,d\mu_{|a_i|}(x)=\infty.
\tag{1}
\]

The infinite value includes a kernel and agrees with the source's convention \(\|a^{-1}\|_2=\infty\) when an \(L^2\) inverse does not exist.
For \(t>0\), put

\[
B_k(t)=\prod_{j=1}^k(1+t a_j),\qquad
S_k(r)=1+r+\cdots+r^{k-1}.
\]

Theorem 1.27, with its time parameter \(s=k t^2\) and initial unitary \(u_0=1\), states

\[
\operatorname{supp}\mu_{B_k(t)}
=\left\{z\in\mathbb C:
 |z-1|^2\le t^2 S_k(|z|^{2/k})\right\}.
\tag{2}
\]

Indeed, its removed disk has defining inequality

\[
|z|^{2/k}<\frac{s}{k\|a^{-1}\|_2^2}-1=-1,
\]

so it is empty.
Its strict support domain is described by

\[
\frac{k|z-1|^2}{S_k(|z|^{2/k})}<s.
\]

The strict-to-weak closure conversion, including \(z=0\), \(|z|=1\), and positive real boundary points, is exactly the elementary angular/radial argument already checked in Miy26-U005.
This conversion does not require Theorem 1.28's further global topology assertions.
The review below distinguishes the source's proved containment from its stronger introductory wording.
The complete derivation of (2), followed by the ordinary-spectrum equality, is now the project deduction [Yin_C_F0094 proof version 2](../../../claims/Yin_C_F0094_v1.md#yin_c_f0094-proof).

## A restriction revealed by an endpoint check

The unrestricted wording \(k\in\mathbb N\) in the displayed Theorem 1.27 cannot be applied blindly at \(k=1\).
For \(u_0=1\), a Haar-unitary step \(a=u\), and \(0<t<1\), the product is \(1+tu\).
It is normal, and its Brown support is the circle \(\{|z-1|=t\}\).
In the source's time convention \(s=t^2\), formula (1.20) gives an empty removed disk, while (1.19)-(1.21) give the disk \(\{|z-1|\le t\}\).
Thus that general source specialization is false as printed.

This does not refute (2), whose hypothesis excludes Haar steps, but it is a concrete reason to avoid importing the theorem outside a checked range.
For the application's \(k=1\) case, use the already accepted bounded R-diagonal spectral theorem directly: (1) gives zero inner radius and unit outer radius, and translation/scaling gives the disk.
No general source correction is assumed.

The origin of the restriction is visible in the second-moment calculation for the circulant initial matrix \(Z\): for \(k\ge2\), its normalized trace is zero and \(\|Z-\lambda\|_2^2=1+|\lambda|^2\); at \(k=1,u_0=1\), it is instead \(|1-\lambda|^2\).
The source's centered removed-disk expression therefore needs separate treatment there.
This diagnosis is a local applicability check, not an author-confirmed erratum or a complete repair of all \(k=1\) statements.

## A second issue: the detailed proof only supplies containment

DHH+25 Proposition 6.4(6) and Theorem 6.7 explicitly establish that the Brown measure is supported in the closure of the calculated domain.
Proposition 6.4 cites Theorem 3.6 of Bercovici--Zhong.
Although the bibliography specifies arXiv v1, that theorem numbering matches [BZ22's 2025 v2](../BZ22/Yin_U001.md#bz22-density-interface), whose conclusion is also only containment.
DHH+25 Remark 1.26 asserts density nonvanishing, but no proof of general strict positivity was found in the reviewed chain.
Merely writing a real-analytic density or excluding boundary mass does not supply the reverse support inclusion.

For this application's normal circulant initial operator, Yin_C_F0094 version 2 supplies the missing reverse inclusion by deriving a strictly positive density from the checked BZ22 formulas.
This uses only normality, positive interior subordination parameters and the nonzero R-diagonal step; its calculation is displayed in equations (13)-(15) of that proof.
Thus the present application no longer accepts unproved general support equality as an external dependency.
This is a local project repair, not an author-confirmed correction or a claim to have audited the whole source.

The separately checked block interfaces are exact: with cyclic indices, \(Z=\sum E_{j,j+1}\) and \(A=\sum a_j\otimes E_{j,j+1}\), Corollary 5.19 gives scalar-trace freeness and the step star-law for \(A\); Corollary 5.4 identifies the product Brown measure as the pushforward under \(\lambda\mapsto\lambda^k\).
In the bounded case no unbounded block domain enters these applications.
Lemma 6.6's proof computes the needed reciprocal-root identity correctly; its displayed part (2) has missing inverse/square notation, so the application uses the actual calculation \(k^{-1}\|(Z-z^{1/k})^{-1}\|_2^2=1/T_k(u_0;z)\).

## Inspection and dependency limits

The source's block-linearization, R-diagonal freeness and Brown-support containment are accepted external inputs in the range above.
The exact parameter substitutions and removed-disk disappearance have been checked.
The reverse inclusion is the explicit project calculation just linked.
Possible boundary singular mass affects the measure's decomposition, not the resulting closed support.
The \(t=0\) case is the scalar identity and is treated separately; a common complex step parameter is reduced to \(|t|\) using the rotation invariance of R-diagonal star-distributions.

This unit does not silently revise the prior circular-only audit.
Its new scope is the iid R-diagonal specialization with (1), the general \(k=1\) warning, and the support-containment/positivity distinction exposed by the deeper check.
It does not accept arbitrary initial unitaries, arbitrary time/finite-inverse cases, or every formula in the 109-page source.
No separate independent review or full source-proof verification was performed in writing this record.
