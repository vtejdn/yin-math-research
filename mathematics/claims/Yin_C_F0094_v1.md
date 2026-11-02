---
author: Yin
---

# Product spectrum for R-diagonal steps without an L2 inverse

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0094: Full Spectrum of Products with R-Diagonal Steps

<a id="yin_c_f0094"></a>

Provenance: project deduction, 2026-09-11.
Initial assessment: proof draft, awaiting separate review.
No novelty claim is made.
This combines Yin_C_F0093, [DHH+25's block and support-containment interfaces](../audits/literature/DHH+25/Yin_U001.md#dhh+25-product-support), the [BZ22 density interface](../audits/literature/BZ22/Yin_U001.md#bz22-density-interface), and the circular product formula in Miy26-U006.
It is a mixed-degree extension of Miy26 Example 4.5.
Proof version 2 supplies a normal-source positivity argument because DHH+25's checked detailed proof established only support containment.

### Statement

Let \(a_1,\ldots,a_k\), \(1\le k<\infty\), be free identically distributed bounded R-diagonal elements in a finite faithful tracial von Neumann algebra \((\mathcal M,\tau)\), such that

\[
\|a_i\|_2=1,
\qquad
\int_0^\infty x^{-2}\,d\mu_{|a_i|}(x)=\infty.
\tag{10}
\]

For every \(t\in\mathbb C\), set \(B=\prod_{i=1}^k(1+t a_i)\), with the factors in the displayed order.
Then

\[
\boxed{\quad
\sigma_{\mathcal M}(B)=\operatorname{supp}\mu_B
=\left\{z\in\mathbb C:
 |z-1|^2\le |t|^2\sum_{j=0}^{k-1}|z|^{2j/k}\right\}.
\quad}
\tag{11}
\]

The sum has value \(1\) at \(z=0\).
In particular every normalized bounded free iid freely infinitely divisible R-diagonal family satisfies (10), by the checked KPZ26 Proposition 5.2.
Infinite divisibility is a sufficient condition for this application, while (10) is the actual inverse-integrability hypothesis.

<a id="yin_c_f0094-proof"></a>
### Current proof: version 2

If \(t=0\), then \(B=1\), and (11) is the singleton \(\{1\}\).
Rotation invariance of each R-diagonal star-distribution, together with freeness, reduces the other cases to \(t>0\).
For \(k=1\), the bounded R-diagonal spectral theorem and (10) give \(\sigma(a_1)=\operatorname{supp}\mu_{a_1}=\{|z|\le1\}\); scalar translation/scaling proves (11).
This separate argument avoids the general \(k=1\) overstatement detected in the DHH+25 interface.

For \(k\ge2\), let \(Z=\sum_j E_{j,j+1}\), \(A_0=\sum_j a_j\otimes E_{j,j+1}\), with indices modulo \(k\), and use the normalized matrix trace.
DHH+25 Corollaries 5.4 and 5.19 identify \(Z\) and \(A_0\) as free, \(A_0\) as R-diagonal with the step distribution, and \(\mu_B\) as the pushforward of \(\mu_{Z+tA_0}\) by \(\lambda\mapsto\lambda^k\).
The normal operator \(Z\) has the uniform distribution on the \(k\)-th roots of unity.
With source time \(kt^2\), its removed domain is empty by (10).
BZ22 gives support containment in the closure of the strict subordination domain, and the following argument supplies the reverse containment.

<a id="yin_c_f0094-density-repair"></a>
**Strict density on the normal-source interior.**
At any point in the open subordination domain outside its finite exceptional set, apply (B1) of the BZ22 audit to \(X_1=Z\), \(X_2=tA_0\).
Retain its notation \(r,s,A,C,D,h,q\), in particular \(r,s>0\), \(1-hq>0\).
Also put

\[
E=\tau((|X_2|^2+s^2)^{-1}),\qquad
F=\tau((|X_2|^2+s^2)^{-2}).
\]

The equality \(H_2(is)=ir\) gives \(r=1/(sE)-s\).
Differentiating in \(s\), with the law of \(X_2\) fixed, yields

\[
h=\frac{2F}{E^2}-\frac1{s^2E}-1
<\frac1{s^2E}-1=\frac rs.
\tag{13}
\]

Here \(F<E/s^2\), since their positive difference is \(s^{-2}\tau(|X_2|^2(|X_2|^2+s^2)^{-2})>0\); the step is nonzero.
Normality and Cauchy--Schwarz give

\[
|D|^2\le C\,\tau(d(d+r^2)^{-2})
=C(A-r^2C),\qquad d=|\lambda-Z|^2.
\tag{14}
\]

If \(h\le0\), (B1) immediately gives \(\rho>0\).
If \(h>0\), multiply (B1) by its positive denominator and use (14):

\[
\begin{aligned}
\pi\rho\,A^2(1-hq)
&=r^2CA^2(1-hq)-2h|D|^2\\
&\ge r^2CA^2(1-hq)-2hC(A-r^2C)\\
&=CA\bigl[r^2A(1+h)-h\bigr]\\
&=CA\,\frac{r-hs}{r+s}>0.
\end{aligned}
\tag{15}
\]

The penultimate simplification uses the exact derivative \(q\) in (B1), and the last uses \(r^2A=r/(r+s)\) and (13).
Thus the Brown density is strictly positive throughout that open domain.
Removing a finite set does not alter its closure.
Support containment and this positivity therefore give equality of the Brown support with the closure of the strict domain.
DHH+25 Lemma 6.6's reciprocal-root calculation and the already audited strict-to-weak boundary conversion send this closure under \(\lambda\mapsto\lambda^k\) to the set \(K\) on the right of (11).
Properness of this polynomial map, or compactness of the support here, justifies taking the image of the closure.
Hence \(\operatorname{supp}\mu_B=K\).

Let \(c_1,\ldots,c_k\) be standard free circular elements and put \(B_c=\prod_i(1+t c_i)\).
Miy26-U006 gives \(\sigma(B_c)=K\), including the closure boundary.
Since \(B\) is a holomorphic polynomial in the \(a_i\), Yin_C_F0093 and the standard bounded Brown-support inclusion give

\[
K=\operatorname{supp}\mu_B
\subseteq\sigma_{\mathcal M}(B)
\subseteq\sigma(B_c)=K.
\]

Both inclusions are therefore equalities.
QED.

<a id="yin_c_f0094-proof-v1-history"></a>
### Preserved initial proof and reason for replacement

Version 1 used the same \(t=0\), phase reduction and \(k=1\) arguments, then used DHH+25 Theorem 1.27 directly to assert \(\operatorname{supp}\mu_B=K\) at time \(kt^2\).
With \(\sigma(B_c)=K\) from Miy26-U006 and Yin_C_F0093, the entire remaining argument was \(K=\operatorname{supp}\mu_B\subseteq\sigma(B)\subseteq\sigma(B_c)=K\).
This was a complete proof conditional on that source equality.
Its subsequent relevant-source review found that DHH+25's detailed Theorem 6.7 and the cited BZ22 Theorem 3.6 prove only support containment; general density nonvanishing was not established in the passages checked.
Version 2 preserves those external containment inputs and replaces this dependency with the explicit normal-source argument (13)-(15).
The two arguments retain their distinct review assessments.

<a id="yin_c_f0094-review"></a>
### Review and exact remaining scope

The author's self-check verified the common complex phase, \(k=1\), \(t=0\), the normalization of DHH+25 time, the absence of its removed disk under (10), and the direction of both spectrum inclusions.
It also checked \(0\in\sigma(B)\iff |t|\ge1\): each factor then has a spectral zero, and in a finite von Neumann algebra an invertible product of bounded factors would force all factors invertible.
Version 2 additionally checks the sign of the density correction, the strictly positive denominator, the derivative bound (13), and every expansion in (15).
These are checks of the candidate proof, not a separate independent review.
Yin_C_F0093's review remains a dependency obligation at this initial checkpoint.

This establishes a specific full-spectrum formula for a genuinely mixed-degree multivariable polynomial.
It proves neither pointwise \(L^2\)-inverse divergence for \(z\in K\), nor the arbitrary-polynomial reverse inclusion, nor the all-rational \(L^2\)-boundedness theorem.
A subsequent scalar polynomial \(q(B)\) has spectrum \(q(K)\) by spectral mapping, without an assertion about its Brown measure.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:54 |
| status | proved |
| reason | Adopt the exact actual original finding at its complete reviewed scope while preserving the mathematical assessment, fixed argument, dependencies and historical decisions. The original initial context-isolation fact remains unknown; no new or redated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0094) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0105_v1.md#positivity-repair) | Actual original complete C_F0094 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0094) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0105_v1.md#fresh-c43-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0094) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0105_v1.md#positivity-repair) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0105_v1.md#positivity-repair).

Material covered by that review: [Exact material](Yin_C_F0093_v1.md), [Exact material](Yin_C_F0094_v1.md), [Exact material](../ledger/Yin_L_F0023_v1.md) (together retain the original whole-source scope).
