---
author: Yin
---
# The first radius sum and an inclusion-minimal pair of supports

## Whole finding

At 2026-11-21T06:51 UTC an agent outside the development of [C105 v3](../../claims/Yin_C_A0105_v3.md#statement) independently reviewed its full [argument](../../claims/Yin_C_A0105_v3.md#argument) for Yin.
The reviewer received the fixed claim and its scope, including the final minimality clause, and consulted the prior findings on the two fixed dependencies.
The claimed minimum is ten, and the specified pair realizes it with every proper nonempty subrectangle admitting a uniquely represented product.

The generating set and word balls agree with those of [C105 v2](../../claims/Yin_C_A0105_v2.md#statement).
Its third assertion covers arbitrary nonempty subsets with radius sum at most nine, so every pair in the optimization problem satisfies the required lower bound if it has no uniquely represented product.
For the ball exhaustions and the correctness of the group normal form the reviewer used the [existing independent finding](Yin_R_A0142_v2.md#whole-finding).

The reviewer compared the two word lists with [Appendix A, p. 10](../../literature/pdf/MS26b--arxiv-v1.pdf#page=10).
Prepending \(a\) to each of the seventeen selected rows and cancelling its initial inverse where present gives the displayed list in v3, with maximum word length four.
The maximum printed column length is six.
Using the exact normal form of J_A0005 on the translated lists gave 17 distinct row elements and 28 distinct column elements.
Grouping all 476 cells by the normal form of their product gave 188 products.
For multiplicities \(2,3,4,5,6,7,10\) the counts were respectively \(136,28,13,4,4,2,1\).
Thus the exhibited pair attains the lower bound.

The exhaustive list in [C105 v1](../../claims/Yin_C_A0105_v1.md#exhaustion-of-support-choices) contains exactly three nonempty rectangles with no singleton class.
All require all 28 columns, and the two other row sets contain row 8, which is absent from \(I_1\).
The exact partition in v2 identifies these classes with group fibers, and left multiplication by \(a\) induces a bijection on fibers even after restricting either support.

The reviewer also checked minimality directly on the translated table.
For a fixed nonempty row set \(I\), start with the allowed columns and delete a column \(j\) whenever some cell \((i,j)\), \(i\in I\), has no other cell of the same product among the remaining columns and rows in \(I\).
Any subset of the remaining columns that contains \(j\) would retain that singleton, so every deletion preserves all solutions with row set \(I\).
Starting with all columns, only the full row set retained any columns after these deletions among the \(2^{17}-1\) row sets checked.
With all rows fixed, starting with any one of the 28 columns omitted led to deletion of all remaining columns.
Every proper column subset omits at least one of those columns, which completes the second check.

For every field, left multiplication of the first factor by \(a^{-1}\) preserves nonvanishing and carries its support into the original seventeen rows.
Associativity gives \((a^{-1}\alpha)\beta=a^{-1}(\alpha\beta)\), so the [coefficient theorem of v1](../../claims/Yin_C_A0105_v1.md#statement) applies also when either factor uses only part of its allowed support.
The reviewer checked its scope against the [v1 finding](Yin_R_A0142_v1.md#whole-finding) and verified the three two-cell fibers and the three-cell fiber for \(I_1\) directly in the translated table.
If both supports are full and \(\alpha\beta=0\), the pair equations give \(x_0/x_3=-y_{20}/y_{13}=x_{26}/x_{31}=-y_1/y_6\), so the first two terms of the triple at \((0,6),(3,1),(7,8)\) cancel and force \(x_7y_8=0\).
This contradicts full support in every characteristic.
For proper supports the uniquely represented product already has a nonzero coefficient.
The existence of complex zero divisors on unrestricted supports remains outside this conclusion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0105_v3.md#statement) | Sharp radius sum, the specified sizes and radii, all proper nonempty subrectangles and all nonzero factors over each field. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0105_v3.md#argument) | Lower bound, restriction of exact fibers, both uses of translation, radius bounds and the coefficient conclusion. |
| [Whole finding](#whole-finding) | [Bounded unique products](../../claims/Yin_C_A0105_v2.md#statement) | All nonempty subsets with radius sum at most nine in the same word metric. |
| [Whole finding](#whole-finding) | [Exact appendix partition](../../claims/Yin_C_A0105_v2.md#exact-balls-and-the-appendix-partition) | Applicability of the normal form and equality of the product fibers and signature classes on each restriction. |
| [Whole finding](#whole-finding) | [Support enumeration](../../claims/Yin_C_A0105_v1.md#exhaustion-of-support-choices) | The three nonempty rectangles with no singleton class and their containment relations. |
| [Whole finding](#whole-finding) | [Coefficient exclusion](../../claims/Yin_C_A0105_v1.md#statement) | All coefficient fields and all nonempty sub-supports of the original lists. |
| [Whole finding](#whole-finding) | [Appendix transcription](../../computations/programs/Yin_J_A0004/verify.py) | The 32 rows, 28 columns and their exact printed order. |
| [Whole finding](#whole-finding) | [Exact normal form](../../computations/programs/Yin_J_A0005/verify.py) | Normal-form routine used in the direct translated-table computation. |
| [Whole finding](#whole-finding) | [Review of v1](Yin_R_A0142_v1.md#whole-finding) | Earlier independent coverage of the support enumeration and all-fields exclusion used in v3. |
| [Whole finding](#whole-finding) | [Review of v2](Yin_R_A0142_v2.md#whole-finding) | Earlier independent coverage of exact equality, the appendix partition and the bounded ball exhaustions. |
