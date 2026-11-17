---
author: Yin
---

# EYY12: counting and confinement for Wigner matrices

<a id="eyy12-u001"></a>
## Hypotheses and estimates

In the [final arXiv version](readme.md#arxiv-v7), pp. 4–5, equations (2.1)–(2.4), \(H=(h_{ij})\) is Hermitian or real symmetric, with independent centered upper-triangular entries, including the diagonal.
The variance matrix \(B=(\sigma_{ij}^2)\), where \(\sigma_{ij}^2=\mathbb E|h_{ij}|^2\), is column-stochastic and satisfies \(\max_{ij}\sigma_{ij}^2\le C_0/N\).
Its eigenvalue \(1\) is simple and its remaining spectrum lies in \([-1+\delta_-,1-\delta_+]\), with fixed \(\delta_\pm>0\).
The uniform tail condition (2.17), p. 7, is \(\mathbb P(|h_{ij}|>t\sigma_{ij})\le \vartheta^{-1}\exp(-t^\vartheta)\) for some fixed \(\vartheta>0\), every \(t\ge1\), and every index and size.

<a id="semicircle-counting-and-locations"></a>
For the eigenvalues \(\lambda_1\le\cdots\le\lambda_N\), the normalized counting function is \(F_N(E)=N^{-1}\#\{j:\lambda_j\le E\}\).
Write \(F_{\rm sc}\) for the distribution function of the [standard semicircle law](../NS06/Yin_U002.md#semicircular) on \([-2,2]\), and let \(\gamma_j\in[-2,2]\) be its \(j/N\) quantile, with \(\gamma_N=2\); see (1.3), p. 3, (2.14), p. 6, and (2.23)–(2.24), p. 8.
Theorem 2.1(iii), p. 7, (2.22), and Theorem 2.2, p. 8, (2.25)–(2.26), give the following simultaneous bounds:

\[
\begin{split}
\|H\|&\le 2+N^{-2/3}(\log N)^{9L},\\
|\lambda_j-\gamma_j|&\le N^{-2/3}\min(j,N-j+1)^{-1/3}(\log N)^L \quad(1\le j\le N),\\
\sup_{|E|\le5}|F_N(E)-F_{\rm sc}(E)|&\le N^{-1}(\log N)^L .
\end{split}
\]

For sufficiently large \(N\) and \(A_0\log\log N\le L\le\log(10N)/(10\log\log N)\), the exceptional probability is at most \(3C\exp[-c(\log N)^{\phi L}]\) by a union bound, with \(A_0>1\), \(C,c>0\), and \(0<\phi<1\) depending only on \(\vartheta,\delta_\pm,C_0\).

## Bounded real Wigner entries

Suppose that every real upper-triangular variable \(\sqrt N h_{ij}\), including those on the diagonal, has variance one and absolute value at most a common fixed \(K\).
Together with centering and independence this gives \(B=\mathbf1\mathbf1^{\mathsf T}/N\), whose only nonzero eigenvalue is \(1\); (2.17) holds by taking \(\vartheta\) small enough that \(\vartheta^{-1}\exp(-K^\vartheta)\ge1\).
This covers Rademacher entries and any fixed bounded truncation whose laws have been centered and rescaled to variance one, provided the rescaling is defined and the upper-triangular independence is preserved.
The constants may depend on the truncation level.
At \(L=A_0\log\log N\) the factor \((\log N)^L\) is \(N^{o(1)}\), and the exceptional probabilities decay faster than every power of \(N^{-1}\).
The first Borel–Cantelli lemma thus gives all three bounds eventually almost surely for any coupling across sizes, for each fixed choice of the standardized laws.

The cited parts of both theorems and their hypotheses were checked directly and are accepted as external inputs at statement and applicability depth.
The original proofs were not independently audited; these estimates concern eigenvalues of the Hermitian input and by themselves give no lower bound on singular values of a polynomial of several matrices.
