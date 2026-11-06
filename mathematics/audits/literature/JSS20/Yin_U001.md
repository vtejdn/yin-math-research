---
author: Yin
---

# JSS20: norm regularization of a real symmetric matrix

<a id="jss20-u001"></a>
## Exact source and acceptance boundary

The input is Theorem 1.3 on printed page 2 of [arXiv:2012.00175v1](readme.md#arxiv-v1).
The title, author list, edition stamp, theorem, following diagonal remark and proof organization on printed pages 1--3 were read directly.
The theorem is accepted at statement and applicability depth; its complete proof in Section 5 and its cited inequalities have not been independently audited here.
The algorithmic Theorem 1.4 is not needed for the existence statement below and is not adopted as a project input.

<a id="symmetric-norm-regularization"></a>
## Theorem 1.3 and the unmodified principal block

Let \(A\) be a real symmetric \(n\)-by-\(n\) random matrix whose entries on and above the diagonal are independent copies of one centered variance-one real law.
For each \(0<\varepsilon\le1/2\), there are absolute constants \(c,C>0\) such that, with probability at least \(1-2e^{-c\varepsilon n}\), one can choose row and column sets, each of size at most \(\lceil\varepsilon n\rceil\), for which setting that rectangular submatrix to zero produces \(\widetilde A\) with
\[
 \|\widetilde A\|\le C\sqrt{n/\varepsilon}.
\]
The ceiling formulation harmlessly enlarges the permitted integer sets.
The chosen row and column sets need not coincide, and the modified matrix need not be symmetric.
No symmetry of the entry distribution, fourth moment, density or bounded support is assumed.

If the selected row and column sets are \(I,J\), then on \(K=[n]\setminus(I\cup J)\) the original principal block is unchanged and
\[
 |K^c|\le2\lceil\varepsilon n\rceil,
 \qquad
 \|A[K,K]\|=\|\widetilde A[K,K]\|
       \le C\sqrt{n/\varepsilon}.
\]
This last assertion is the direct compression consequence of the source theorem; it does not claim independence after selecting \(K\).

The following source remark permits independent diagonal variables of mean zero and variance one, but leaves its proof modification to the reader.
The current project application can instead use the stated iid theorem and a separate explicit comparison with the original diagonal law.
Neither the remark nor this unit supplies that comparison for arbitrary finite diagonal variance.
A measurable choice among finitely many admissible index sets is an additional elementary project step, and no efficient selection algorithm is asserted here.
