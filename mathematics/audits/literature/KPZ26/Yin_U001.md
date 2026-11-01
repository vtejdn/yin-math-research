---
author: Yin
---

# KPZ26-U001: Freely infinitely divisible R-diagonal homogeneous spectra

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Online 25-page arXiv:2605.25434v1 PDF, title May 26 2026 and arXiv submission May 25; HTML displays August 24, and selected results were rechecked in the exact PDF.

Passages: Definition 3.1/Theorem 3.2 p. 7; Example 3.4 pp. 8-9; Theorem 4.1 p. 9/proof pp. 12-14; Proposition 5.2/Corollary 5.3 p. 15; Lemma 2.4 p. 4.

Inspection: 2026-09-11 selected primary statements, applicability and stated proof interfaces read; no reliable full visual or whole-source proof audit; forthcoming perturbation theorem excluded.


<a id="kpz26-u001"></a>
## Selected source scope


## Retained selected source content

<a id="kpz26-selected-audit"></a>
Date: 2026-09-11.
Reader: the spectral-extension research agent.
Scope: targeted primary-source statement and applicability checks for the new spectral-extension objective.
This is not a whole-paper audit or an independent review of all original proofs.
The bibliographic identity remains in [references.bib](../../../literature/references.bib).

## Artifact and version boundary

The inspected primary source is the [25-page arXiv v1 PDF](https://arxiv.org/pdf/2605.25434v1), with printed page numbers equal to one-based PDF page numbers.
Its title page is dated **May 26, 2026**; the [arXiv record](https://arxiv.org/abs/2605.25434) records submission on **May 25, 2026**.
The source is a public preprint, not an established journal publication.
The DOI is [10.48550/arXiv.2605.25434](https://doi.org/10.48550/arXiv.2605.25434).

The experimental [v1 HTML](https://arxiv.org/html/2605.25434v1) was used to locate formulas but displays **August 24, 2026**.
The selected statements were consequently checked again in the versioned PDF.
A complete PDF/HTML comparison or explanation of that discrepancy is not claimed.
No local source PDF was retained in this intake, so a local byte count and checksum are not applicable.
Web PDF rendering was attempted but did not reliably return all requested page images; the accepted checks below use the primary PDF's extracted formulas and matching selected HTML formulas, not an asserted full visual review.

## Input map

| Input | Exact locator in the PDF | Accepted scope and inspection depth |
| --- | --- | --- |
| Freely infinitely divisible R-diagonal elements | Definition 3.1 and Theorem 3.2, p. 7 | Definition and characterization checked, including the Boolean-to-free Bercovici--Pata factor. The two short implication interfaces were read; the cited foundational classification proofs were not re-audited. |
| Homogeneous polynomial permanence | Theorem 4.1, p. 9; proof pp. 12-14 | Bounded, finite, star-free R-diagonal family; additive free infinite divisibility; scalar homogeneous polynomials of one positive degree. Statement checked and final proof mechanism read. The preceding Fock-model lemmas and the approximation theorem are retained external proof inputs, not independently verified here. |
| No square-integrable inverse at zero | Proposition 5.2, p. 15 | Statement and its short S-transform proof checked, including the kernel case. |
| Brown support equals spectrum | Corollary 5.3, p. 15 | Bounded case only. Its dependency is Proposition 5.2 and the R-diagonal annulus/spectrum input, which is already accepted at [Miy26-U008](../Miy26/Yin_U004.md#miy26-u004). |
| Circular and product examples | Example 3.4, pp. 8-9; surrounding p. 7 classification | The bounded products of circular elements are covered. Negative powers in the broader example can be unbounded and are not inserted into the bounded theorem. |

## Definition and hypothesis conversion

Work in a finite von Neumann algebra with a faithful normal tracial state.
A bounded R-diagonal element (X) is freely infinitely divisible here when, for every positive integer (n), its star-distribution is that of a sum of (n) free identically distributed R-diagonal elements.
This is **additive** free infinite divisibility, not multiplicative infinite divisibility of its modulus and not R-diagonality alone.

Theorem 3.2 identifies this condition with additive free infinite divisibility of the symmetrized modulus law.
Its other equivalent condition is

\[
\mu_{X^*X}=\mathbb B(\nu)\boxtimes\Pi_1,
\]

for a probability measure \(\nu\) on \([0,\infty)\), where \(\mathbb B\) is the Boolean-to-free Bercovici--Pata bijection and \(\Pi_1\) is the rate-one Marchenko--Pastur law.
The source explicitly gives the bounded realization correspondence for compactly supported \(\nu\).
Replacing \(\mathbb B(\nu)\) by an arbitrary positive law is not the stated characterization.
In particular, no assertion that an arbitrary product of a circular element and an independent bounded positive element is in this class is made.

A standard circular element belongs to the class: the sum of \(n\) free circular elements of variance \(1/n\) is again variance-one circular.
This is an immediate covariance/free-Gaussian specialization of the definition, consistent with Example 3.4.
Products of finitely many free circular elements give further bounded examples; Theorem 4.1 also admits free families with different laws and variances.
More generally the compactly supported parameter \(\nu\) above supplies a class of bounded laws, rather than only a family of polynomial coordinate changes of one fixed semicircular system.

## Consumed theorem and explicit spectrum specialization

Let \(X_1,\ldots,X_d\) be bounded freely infinitely divisible R-diagonal elements whose generated star-algebras are free.
They need not be identically distributed.
For \(m\ge1\), put

\[
T=P(X)=\sum_{|w|=m}\alpha_wX_w,
\qquad
R^2=\sum_{|w|=m}|\alpha_w|^2
       \prod_{j=1}^{m}\tau(X_{w_j}^*X_{w_j}).
\tag{1}
\]

Theorem 4.1 puts \(T\) in the same R-diagonal and freely infinitely divisible class.
Proposition 5.2 gives

\[
\int_0^\infty t^{-2}\,d\mu_{|T|}(t)=\infty,
\tag{2}
\]

with the extended value at zero; this allows a nontrivial kernel.
The already accepted bounded R-diagonal spectral theorem, together with (2), therefore gives

\[
\sigma_{\mathcal M}(T)
=\operatorname{supp}\mu_T
=\{z\in\mathbb C:|z|\le R\}.
\tag{3}
\]

Here \(R=\|T\|_2\).
The verification is the orthogonal holomorphic word calculation already used in [Yin_C_F0017](../../../claims/Yin_C_F0017_v1.md#yin_c_f0017): in \(\tau(X_v^*X_w)\), every nonzero cumulant block pairs one starred with one unstarred entry, and the unique nested pairing requires \(v=w\).
Allowing different variances replaces \(\sigma^{2m}\) by the product in (1); no homogeneous norm estimate or identical-distribution assumption is used for this calculation.
If \(R=0\), faithfulness makes \(T=0\), and (3) is the singleton \(\{0\}\), handled separately from non-Dirac modulus formulations.

Formula (3) is a direct specialization of checked source statements and this normalization calculation.
It is not registered as a newly proved project Claim.
It extends the homogeneous circular disk calculation in [Miy26-U005](../Miy26/Yin_U006.md#miy26-u006).
A scalar constant term translates the disk.
The usual polynomial spectral mapping theorem then gives \(\sigma(q(T))=q(\{|z|\le R\})\) for scalar one-variable polynomials \(q\); this does not turn an arbitrary mixed-degree multivariable polynomial into a homogeneous one.

## Proof interfaces and limits

The first part of the source's Theorem 4.1 proof uses the product-cumulant formula and equal block lengths.
Nonzero alternating blocks in a connected noncrossing partition force alternating adjoint signs between consecutive polynomial factors.
This R-diagonality argument uses only free R-diagonal inputs.
Its second part represents the alternating cumulants by positive moments of \(VV^*\) in a Fock model, first for symmetric compound free Poisson data and then by approximation.
Free infinite divisibility is used in that second interface; homogeneity cannot be dropped in the equal-block argument.

For Proposition 5.2, the kernel case gives (2) immediately.
Otherwise the source factors the modulus-square law as \(\eta\boxtimes\Pi_1\), with \(\eta(\{0\})=0\), and uses

\[
S_{\eta\boxtimes\Pi_1}(u)=\frac{S_\eta(u)}{1+u},\qquad u\downarrow-1.
\]

The source's Lemma 2.4, p. 4, identifies the limit of \(S_\eta(u)\) with \(\int x^{-1}\,d\eta(x)\in(0,\infty]\).
Its proof is a monotone-convergence calculation; read together with Proposition 5.2, it checks the required divergence and not merely noninvertibility in operator norm.

The source says at the start of Section 5, p. 14, that Theorem 5.1 on general additive perturbations belongs to a forthcoming revised version of another paper.
**That theorem is not an accepted dependency of the present note.**
Neither the homogeneous result above nor Proposition 5.2 requires it.

These checks do not establish Miy26's all-rational \(L^2\)-to-bounded theorem for an entire freely infinitely divisible R-diagonal tuple.
Formula (2) concerns \(T^{-1}\) at zero, not all shifted inverses or arbitrary rational expressions.
Brown-support equality alone is not a proof of pointwise failure of square-integrability for every inverse on the spectrum.
General nonhomogeneous holomorphic polynomials, mixed-star polynomials, and multivariable rational expressions remain separate targets in the research record (original material now separated into [Yin_C_F0093_v1](../../../claims/Yin_C_F0093_v1.md), [Yin_C_F0094_v1](../../../claims/Yin_C_F0094_v1.md), [Yin_L_F0023_v1](../../../ledger/Yin_L_F0023_v1.md)).

## Search and review record

The source was found on 2026-09-11 after existing Miy26, Yin_C_F0015, Yin_C_F0017, Yin_C_F0020 and Yin_C_F0021 material did not supply a broad new full-spectrum class.
Primary-source queries included `free R-diagonal spectrum polynomial creation`, `R-diagonal polynomials spectrum Haagerup`, and `free Meixner rational L2 bounded spectrum`.
The concrete new lead was homogeneous permanence for freely infinitely divisible R-diagonals.
Inspection stopped at the inputs needed for (3); a whole-paper audit would be a separate task.
A subsequent resolvent search located the Haagerup--Kemp--Speicher resolvent paper, but no new theorem from it is consumed here.
There is no novelty claim, formal verification, complete source-proof audit or independent review of this newly written unit.
