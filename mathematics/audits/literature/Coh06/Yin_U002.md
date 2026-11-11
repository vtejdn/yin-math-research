---
author: Yin
---
# Higman linearization by enlargement

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Coh06-U002

Source: [Coh06, Section 5.8, printed p. 311 / PDF p. 335](../../../literature/pdf/Coh06.pdf#page=335), the opening paragraphs before equation (1).
The development agent directly read this passage for Yin on 2026-11-11 and checked the displayed elementary transformations by multiplication.
The passage identifies the construction as linearization by enlargement, also called Higman's trick, and attributes it to Higman [40].
This unit verifies Cohn's passage and its elementary identity; it makes no earliest-priority claim and does not claim inspection of the 1940 paper.

### Source statement and elementary construction

Cohn considers a matrix over a free algebra \(k\langle X\rangle\) whose selected entry is \(f+ab\).
He adjoins an identity state and uses elementary row and column operations to replace the selected two-by-two corner by
\[
\begin{pmatrix}f+ab&0\\0&1\end{pmatrix}
\longrightarrow
\begin{pmatrix}f+ab&a\\0&1\end{pmatrix}
\longrightarrow
\begin{pmatrix}f&a\\-b&1\end{pmatrix}.
\]
He then repeats this construction to obtain a matrix of the form
\[
A_0+\sum_{j=1}^{s}A_jx_j,
\qquad A_j\in M_{m,n}(k),
\]
which is his definition of a linear matrix in equation (1).
This permits a constant term and does not require any coefficient matrix to be invertible.

In complete block notation, for \(P=A+BC\) over any unital ring and compatible rectangular blocks, the checked identity is
\[
\begin{pmatrix}I&-B\\0&I\end{pmatrix}
\begin{pmatrix}A&B\\-C&I\end{pmatrix}
\begin{pmatrix}I&0\\C&I\end{pmatrix}
=\operatorname{diag}(P,I).
\]
Each outer matrix has a two-sided inverse obtained by changing the sign of its off-diagonal block.
Thus the identity uses no inverse of \(A,B,C\), or \(P\).
It remains valid after any unital ring evaluation, including a quotient imposing relations among the variables.
This last applicability statement is direct evaluation of the checked identity; it imports no free-field fullness or regularity conclusion.

### Inspection and use limits

The selected source proof consists of the displayed elementary transformation and its finite iteration, both checked at the preceding scope.
The exact terminating complexity, affiliated rank shift and closed-kernel dimension comparison are consuming-argument details, not assertions attributed to this page of Cohn.
The following pages, printed pp. 312--313 / PDF pp. 336--337, were read to identify the distinction from the later monic normal-form results.
Their highest-degree arguments use the free-algebra setting; Lemmas 5.8.1--5.8.2 and Theorem 5.8.3 are not accepted here for an arbitrary relations quotient.
This is a selected elementary source inspection, not a whole-book audit, independent project review, or a review of the original weak-algorithm foundations.
