---
author: Yin
---

# Common-phase zero-diagonal witnesses for affine Wigner pencils

This continuing candidate concerns the algebraic counterexample boundary of [F0013](../tasks/Yin_T_F0013_v1.md#contract).
The evaluated strategic comparison and its useful failed implications are fixed in [L_F0063](../ledger/Yin_L_F0063_v1.md).
The responsible route continues its actual-minor and nonsymmetric-shift work; the candidate below supplies neither a logarithmic approximation nor adopted proved support.
Its distinct content is the common-phase zero-diagonal extension, reusing the real-symmetric witness argument at its existing home.

## A common-phase zero-diagonal witness filter

The real-symmetric witness argument is fixed in the [reviewed all-large-even construction](../claims/Yin_C_F0186_v9.md#all-even-witness) and is reused here.
Here is a limited extension to a different input support.
Fix a common phase \(\theta\in\mathbb R\) for every input variable, and suppose \(\Delta(L(s))>0\).
There is a positive integer \(q\) such that the affine determinant is a nonzero polynomial on the real-symmetric tuple space of dimension \(q\), by that existing argument.
Write this polynomial as \(f(R_1,\ldots,R_d)\).
The substitution \(R\mapsto-R\) is an invertible real-linear substitution, so \(f(R)f(-R)\) is also a nonzero polynomial.
Choose a real-symmetric tuple \(R\) at which both factors are nonzero.

Set
\[
 K_\theta=\begin{pmatrix}0&e^{i\theta}\\ e^{-i\theta}&0\end{pmatrix},
 \qquad X_j=K_\theta\otimes R_j.
\]
The matrices \(X_j\) are Hermitian and have zero diagonals.
Every upper off-diagonal entry lies in the real line \(e^{i\theta}\mathbb R\): entries inside the two diagonal blocks vanish, and entries in the upper off-diagonal block are \(e^{i\theta}\) times real numbers.
One fixed physical unitary diagonalizes \(K_\theta\) to \(\operatorname{diag}(1,-1)\), simultaneously for every \(j\).
It therefore transforms \(L(X)\) to \(L(R)\oplus L(-R)\), which is invertible.
Block-diagonal repetition supplies such witnesses in every positive multiple of \(2q\).

Consequently, the affine determinant is not identically zero on these common-phase zero-diagonal support spaces along that dimensional subsequence.
For zero-diagonal Wigner inputs whose off-diagonal phase-line scalar variables are independent and non-atomic, a nonzero polynomial has zero probability of vanishing, by induction over its real coordinates.
The normalization by \(N^{-1/2}\) is an invertible coordinate scaling and does not change polynomial nonidentity.
This rules out an identically-singular obstruction on every divisible dimension for that restricted law class.

This extension does not provide a quantitative lower determinant bound, a summability estimate, or a nonnormal spectral limit.
It does not apply to a finite atomic support merely because the polynomial is nonzero on its real linear span.
The same physical diagonalization also requires a common phase; different phases for different inputs are not covered by the construction.
Arbitrary diagonal laws have not been reduced to the displayed zero-diagonal support, and no such reduction is asserted.
Thus a counterexample based only on a persistent transpose parity identity should first be tested against this dimensional gate; finite-support identities and quantitative near-singularity remain possible questions.

## Continuation boundary

The displayed candidate still needs fixed mathematical organization and suitable review before use as established support.
The real-symmetric input witness is supplied by that exact fixed construction, while the common-phase extension here retains its own unresolved review and adoption scope.
Arbitrary diagonal laws, different coordinate phases and quantitative determinant bounds remain outside the present argument.
