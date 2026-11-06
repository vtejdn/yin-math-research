---
author: Yin
---

# DMR08: transitivity forces an invertible matrix

<a id="dmr08-u001"></a>
## Inspected source

Use the [25-page author PDF](readme.md#author-pdf): introduction, PDF pp. 1-2, and Proposition 5.1 with its complete proof, PDF/printed p. 14.

<a id="transitive-operator-space"></a>
## Definition: transitive operator space

For finite-dimensional complex vector spaces \(X,Y\), a linear operator space \(\mathcal L\subseteq\operatorname{Hom}(X,Y)\) is **transitive** when
\[
 \mathcal Lx=Y\qquad\text{for every }0\ne x\in X.
\]

<a id="finite-dimensional-transitive-invertible"></a>
## Proposition 5.1 and inspected proof

A transitive complex linear subspace of \(M_n(\mathbb C)\) contains an invertible matrix.
Equivalently, a linear subspace consisting entirely of singular matrices is not transitive.

The proof chooses a maximal-rank element and uses invertible left/right changes to make it \(P=\operatorname{diag}(I_k,0)\).
For \(T=\begin{pmatrix}T_0&E\\F&T_1\end{pmatrix}\), maximality and the Schur complement of \(T+tP\) give
\[
 T_1=F(T_0+tI_k)^{-1}E
\]
for sufficiently large real \(t\).
Taking \(t\to\infty\) gives \(T_1=0\), so every \(T\) maps \(\ker P\) into \(\operatorname{Ran}P\), contradicting transitivity.

The complete proposition proof was read directly, including the rank factorization and limiting step.
Accept this complex finite-dimensional input at that scope.
This is ordinary source inspection, not an independent project-proof review.
The real-field adaptation and signed nonlinear determinant theorem require their own project argument; neither is claimed as a source statement.
Other results and other editions were not audited.
