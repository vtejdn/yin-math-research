---
author: Yin
---

<a id="sar42-u001"></a>
# Sar42-U001: regular values for real polynomial maps

## Source statement and inspected edition

Use the [1942 journal edition](readme.md#journal-edition).
Section 1, printed p. 883 / PDF p. 1, gives the map, differentiability hypotheses and critical-value convention.
Theorem 4.1, printed p. 885 / PDF p. 3, treats a map from an open region of \(\mathbb R^m\) into \(\mathbb R^\ell\) when \(m\le\ell\), with components of class \(C^r\), \(r\ge1\): its critical values form an \(m\)-dimensional null set.
Theorem 7.2, printed p. 889 / PDF p. 7, treats \(m>\ell\): the critical values form an \(\ell\)-dimensional null set provided \(r\ge m-\ell+1\).
The source uses \(n\) for the target dimension and \(q\) for differentiability order; \(\ell\) and \(r\) here avoid conflict with a polynomial called \(q\).
Section 2, printed p. 884 / PDF p. 2, identifies its \(\ell\)-dimensional measure on \(\mathbb R^\ell\) with outer Lebesgue measure.

<a id="scalar-regular-values"></a>
## Scalar critical and regular values

For a \(C^1\) map \(f:\mathbb R^k\to\mathbb R\), \(k\ge1\), a critical point is a point \(x\) with \(df_x=0\), and a critical value is the image of a critical point, as in Section 1 of the source.
A regular value is a number \(\delta\) for which \(df_x\ne0\) at every \(x\in f^{-1}(\delta)\), equivalently a number outside the set of critical values.
This complementary terminology includes the case of an empty preimage and is used here only for real-valued maps.

In particular, if \(f:\mathbb R^k\to\mathbb R\) is of class \(C^k\), then
\[
 f\bigl(\{x\in\mathbb R^k:df_x=0\}\bigr)
\]
has one-dimensional Lebesgue measure zero.
For \(k=1\) this is Theorem 4.1, and for \(k>1\) it is Theorem 7.2 with \(\ell=1\) and \(r=k\).
Thus every interval \((0,b)\), \(b>0\), contains a value \(\delta\) for which \(df_x\ne0\) at every point of \(f^{-1}(\delta)\).
This is the positive regular-value consequence used here; existence of a preimage is a separate condition.

## Polynomial specialization and source role

A real polynomial \(q:\mathbb R^k\to\mathbb R\) is \(C^\infty\), so the differentiability hypothesis holds in every positive integer dimension.
For any finite nonempty collection of pairs \((y_j,p_j)\) with \(q(y_j)=0<q(p_j)\), take \(b:=\min_j q(p_j)>0\).
The regular-value consequence supplies \(0<\delta<b\), and continuity along each segment from \(y_j\) to \(p_j\) ensures that \(q^{-1}(\delta)\) is nonempty and meets each such segment.
Sard's theorem supplies the choice avoiding critical values; the segment argument supplies nonemptiness and the local geometric approximation.
No compactness, properness, degree bound or positivity assumption is required by the external critical-value theorem itself.
This statement is accepted as an established external proof input for the regular-value choice, with only the direct specialization above checked here.

## Inspection limits

On 2026-11-05, an agent representing Yin directly read the stated passages and checked the scalar specialization and polynomial differentiability hypotheses.
The title page and printed pp. 885 and 889 were also rendered and checked visually, resolving the scanned inequality signs and theorem locators.
The proofs of Theorems 4.1 and 7.2 and their subsidiary inputs were not audited, and no independent project-proof review or formal verification is asserted.
This source input alone does not prove a polynomial tube bound or its Gaussian averaging extension.
