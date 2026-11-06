---
author: Yin
---

# KM15: constant lower singular values from linear-form small balls

<a id="km15-u001"></a>
## Source and accepted scope

The inspected edition is [arXiv:1312.3580v1](readme.md#arxiv-v1).
The reusable input is Theorem 1.4 on printed page 5, with the matrix normalization and iid-row convention from printed pages 1--2.
Its statement, hypotheses and the application interface below are accepted; the original proof has not received an independent project audit.
Theorem 2.1 and its clipping, symmetrization and contraction argument on printed pages 7--8 were also read to identify the small-ball mechanism, without a separate audit of its cited probability inequalities.

<a id="isotropic-row-lower-bound"></a>
## Theorem 1.4 in row-count notation

Let \(X\) be a real random vector in \(\mathbb R^p\) with
\[
 \mathbb E\langle X,t\rangle^2=\|t\|_2^2
 \quad(t\in\mathbb R^p).
\]
This is the second-moment isotropy convention; centering is not an additional requirement of the displayed theorem.
Suppose a fixed \(L\) satisfies
\[
 \|\langle X,t\rangle\|_{L^2}
       \le L\|\langle X,t\rangle\|_{L^1}
 \quad(t\in\mathbb R^p).
\]
Let \(X_1,\ldots,X_l\) be independent copies of \(X\), and form \(\Gamma\) with rows \(X_i^T/\sqrt l\).
There are positive constants \(c_1,c_2,c_3\), depending only on \(L\), such that
\[
 l\ge c_1p
 \quad\Longrightarrow\quad
 \mathbb P\{s_{\min}(\Gamma)<c_3\}\le2e^{-c_2l}.
\]
The source writes \(\lambda_{\min}(\Gamma)\) for this smallest singular value.
No higher moment, bounded support, density or row-norm concentration premise occurs in this statement.
If the distribution or dimension changes, its constants remain applicable when the same linear-form bound \(L\) and isotropy hold.
This is an iid-row assertion; arbitrary dependent or nonidentically distributed rows are not silently included.

<a id="pencil-cut-interface"></a>
## Original-pencil application boundary

The [project deduction](../../../claims/Yin_C_F0194_v23.md#constant-cut-argument) projects independent physical output blocks onto one fixed real auxiliary direction, computes their covariance, whitens the resulting iid rows, and proves a dimension-uniform linear-form L1 bound from the original finite collection of entry laws.
It separately checks the aspect ratio, conversion from \(\sqrt l\) to the original \(\sqrt N\) normalization, and union over supports and fixed deletions.
Those are project proof obligations, not conclusions supplied by the source citation.
An arbitrary deterministic off-cut shift, conditioning on the whole parent norm, or treating correlated rows as independent would require an additional argument outside this source use.
