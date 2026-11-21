---
author: Yin
---
# The first radius sum admitting non-unique products in Gardam's group

## Statement

In Gardam's two-generator presentation let \(B_r\) be the radius-\(r\) ball for \(a,b,a^{-1},b^{-1}\).
The least \(r+s\) for which two nonempty finite sets \(P\subseteq B_r,\ Q\subseteq B_s\) have no uniquely represented product is exactly \(10\).
It is attained with \(r=4,\ s=6,\ |P|=17,\ |Q|=28\).
For this choice every proper nonempty subrectangle has a uniquely represented product.
For these particular sets every field \(k\) and all nonzero \(\alpha\in k[P],\ \beta\in k[Q]\) satisfy \(\alpha\beta\ne0\).

## Argument

The [bounded unique-product theorem](Yin_C_A0105_v2.md#statement) gives the lower bound \(r+s\ge10\).
Write \(u_i\) for row \(i\) and \(Q\) for the full column list of [Mian–Siddique, Appendix A](../literature/pdf/MS26b--arxiv-v1.pdf#page=10), with the zero-based numbering in [the fixed transcription](../computations/programs/Yin_J_A0004/verify.py).
Use the seventeen indices
\[
 I_1=(0,1,2,3,4,5,6,7,9,10,11,12,17,18,26,27,31).
\]
The [support enumeration](Yin_C_A0105_v1.md#exhaustion-of-support-choices) gives at least two cells per occupied bucket for this row set and all 28 columns.
The [exact group partition](Yin_C_A0105_v2.md#exact-balls-and-the-appendix-partition) identifies every bucket with one actual product fiber.
Restricting equal partitions to \(I_1\) preserves equality of their fibers, so every product in this subrectangle has at least two representations in the group.
The only other nonempty singleton-free rectangles in the full enumeration have either all 32 rows or the distinct seventeen-row set \(I_2\), and both have all columns.
Consequently none is a proper subrectangle of \(I_1\times Q\).

Put \(P=\{a u_i:i\in I_1\}\).
Left translation carries each product \(u_i v\) to \(a(u_i v)\) and bijects the associated representations.
The same bijection applies to each restricted rectangle, proving the claimed minimality.
Writing \(A=a^{-1}, B=b^{-1}\) in words, free reduction of \(a u_i\) in the order above gives
\[
 a,\ aa,\ 1,\ ab,\ aab,\ aaB,\ b,\ abb,\ aabb,\ aaBB,\
 bA,\ bb,\ bAb,\ bbb,\ bAA,\ bAbb,\ bAAb .
\]
All have length at most four, and every word in \(Q\) in the appendix has length at most six.
The distinct row and column counts follow from the exact partition calculation's check on the two word lists and injectivity of left translation.
This proves the upper bound at \((4,6)\).

Finally \(a^{-1}\alpha\) is nonzero and supported on the seventeen original rows, while \(\beta\) is supported on the original columns.
The [all-fields coefficient exclusion](Yin_C_A0105_v1.md#statement) gives \((a^{-1}\alpha)\beta\ne0\).
Multiplication by \(a\) gives the asserted nonzero product.
Whether this group admits any pair of nonzero complex group-algebra elements with zero product remains open here.

## Assessment history

### Decision first-radius-sum

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:52 |
| status | proved |
| reason | The independent reviewer checks the matching lower bound, the appendix words and translated fibers, the support minimality and the all-fields implication. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The exact first radius sum for a pair with no uniquely represented product, an inclusion-minimal 17-by-28 example and coefficient exclusion over every field. |
| argument | [Proof](#argument) | The small-radius theorem and a single left translation of seventeen rows in the exact appendix table. |
| review | [Whole finding](../audits/reviews/Yin_R_A0142_v3.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Support choices and coefficients](Yin_C_A0105_v1.md#decision-appendix-supports) | The exhaustive list of singleton-free rectangles and coefficient exclusion on the original appendix table. |
| dependency | [Exact products and bounded balls](Yin_C_A0105_v2.md#decision-exact-balls) | Equality of the actual appendix fibers and nonexistence of such pairs at radius sum at most nine. |

## Current assessment

[Selected decision](#decision-first-radius-sum)
