---
author: Yin
---

# The determinant on the negative spectral subspace of a Hermitian product factor

<a id="statement"></a>
## A compression for the ordinary logarithm off the real axis

Let \(A,B\) be selfadjoint scalar polynomials in the complex Hermitian fixed-law finite-second-moment Wigner inputs of the [product symmetrizer theorem](Yin_C_F0358_v1.md#statement).
The factors may share inputs, and the coupling across dimensions is arbitrary.
Assume \(a=A(s)\ge0\) is injective for the free standard semicircular tuple \(s\).
Write \(b=B(s),\ p=ab,\ h=a^{1/2}ba^{1/2}\) and \(u(z)=\tau\log|p-z|\).
For each finite evaluation set
\[
 S_N=|A_N|^{1/2},\qquad C_N=S_NB_NS_N,\qquad
 Q_N=\mathbf1_{(-\infty,0)}(A_N),\qquad J_N=I-2Q_N .
\]
For \(z\notin\mathbb R\), put \(R_N(z)=(C_N-zI)^{-1}\) and \(D_N(z)=I_{Q_N}+2zQ_NR_N(z)Q_N\) on \(\operatorname{ran}Q_N\), where \(I_{Q_N}\) denotes its identity.
Then at every realization
\[
    |\det(A_NB_N-zI)|=|\det(C_N-zI)|\,|\det_{\operatorname{ran}Q_N}D_N(z)|.
    \tag{1}
\]
The determinant on the zero-dimensional space is one.
At \(z=i\), \(D_N(i)\) is exactly the compression of the unitary \((C_N+iI)(C_N-iI)^{-1}\) to \(\operatorname{ran}Q_N\).

Almost surely, \(\operatorname{rank}Q_N/N\to0\), the empirical spectral law of \(C_N\) tends weakly to the spectral law of \(h\), and
\[
   N^{-1}\log|\det(C_N-zI)|\longrightarrow u(z)
\]
locally uniformly on \(\mathbb C\setminus\mathbb R\).
Thus (1) isolates the entire residual ordinary logarithm in a determinant of dimension \(o(N)\), including the value \(-\infty\) at a zero.
If in addition
\[
 \|B_N\|\sqrt{\|A_N\|\,\|(A_N)_-\|}\longrightarrow0\quad\text{almost surely},
 \qquad (A_N)_-=\max(-A_N,0),
 \tag{2}
\]
then \(N^{-1}\log|\det(A_NB_N-zI)|\to u(z)\) almost surely in all dimensions, locally uniformly off the real axis.
This condition permits singular or indefinite finite \(A_N\).

<a id="argument"></a>
## Exact factorization

Suppress \(N\) in the finite matrices.
Since \(JS=SJ\) and \(A=JS^2\), cycling the square factors \(S,JSB\) gives \(\det(AB-zI)=\det(JC-zI)\), also when \(S\) has kernel.
Now \(JC-zI=J(C-zI+2zQ)\) and \(|\det J|=1\).
The determinant lemma with the isometric inclusion of \(\operatorname{ran}Q\) gives (1), since \(C-zI\) is invertible.
The identity \(I+2i(C-iI)^{-1}=(C+iI)(C-iI)^{-1}\) proves the assertion at \(i\), and the spectral theorem gives unitarity.

<a id="comparison"></a>
## The Hermitian spectral law and its logarithmic potential

Write \(k=\dim\ker A,\ d=\operatorname{rank}Q\), and let \(n_-\) count strictly negative eigenvalues.
The identity
\[
          ABA-tA=(JS)(C-tJ)(JS)
\]
holds for each real \(t\).
The summands \(\operatorname{ran}A\) and \(\ker A\) reduce \(C,J,S\), and \(JS\) is invertible on the first summand.
Congruence there gives \(n_-(ABA-tA)=n_-((C-tJ)|_{\operatorname{ran}A})\).
Changing \(C-tJ\) to \(C-tI\) on this range costs at most \(d\) in negative inertia by rank interlacing, and including the kernel costs at most \(k\).
Consequently
\[
 \left|\#\{\lambda(C)<t\}-n_-(ABA-tA)\right|\le d+k.
\]
The [finite-variance polynomial weak law](Yin_C_F0186_v4.md#finite-variance-weak) for \(A_N\), together with positivity and injectivity of \(a\), gives \((d+k)/N\to0\) almost surely.
On a common event the [inertia limit](Yin_C_F0358_v1.md#free-inertia) gives \(N^{-1}n_-(A_NB_NA_N-tA_N)\to\mu_h((-\infty,t))\) at a countable dense set of continuity points.
The distribution functions of the Hermitian \(C_N\) therefore converge weakly to \(\mu_h\).

For decreasing singular values the product inequality \(s_{j+l-1}(XY)\le s_j(X)s_l(Y)\) applied twice gives
\[
                  s_{3j-2}(C_N)\le s_j(S_N)^2 s_j(B_N)
                      =s_j(A_N)s_j(B_N),\qquad 3j-2\le N .
\]
Grouping at most three consecutive singular values from each \(3j-2\) and using \((\log^+(xy))^2\le2(\log^+x)^2+2(\log^+y)^2\) bounds the normalized squared positive-log sum for \(C_N\) by six times the sum of the two normalized bounds for \(A_N,B_N\).
These are almost surely eventually bounded by the [pathwise polynomial singular-value estimates](Yin_C_F0186_v4.md#log-statistics).
Thus the positive tails of the spectral log kernel are uniformly integrable on each bounded parameter set.
For a compact \(K\subset\mathbb C\setminus\mathbb R\) the negative part of \(\log|t-z|\), \(t\in\mathbb R\), is uniformly bounded and this function is Lipschitz in \(z\in K\) with constant at most \(\operatorname{dist}(K,\mathbb R)^{-1}\) by the reverse triangle inequality for the two distances.
Weak convergence, truncation and a finite net now give uniform convergence to \(\int\log|t-z|\,d\mu_h(t)=u(z)\), the last equality by [free cyclicity](Yin_C_F0358_v1.md#free-inertia).

<a id="sufficient"></a>
## A sufficient bound on the negative part

We have \(\|C_NQ_N\|\le\|S_N\|\|B_N\|\|S_NQ_N\|=\|B_N\|\sqrt{\|A_N\|\|(A_N)_-\|}\).
Since \(I+zR_N(z)=R_N(z)C_N\), the compression satisfies
\[
     \|D_N(z)+I_{Q_N}\|
       \le 2\|R_N(z)\|\|C_N Q_N\|
       \le 2\|C_NQ_N\|/|\operatorname{Im}z|.
\]
Under (2) this upper bound tends uniformly to zero on each compact set off the real axis.
Every singular value of the compressed factor then lies between \(1-\epsilon_N\) and \(1+\epsilon_N\) for some \(\epsilon_N\to0\) uniformly on that compact set.
Hence \(N^{-1}\log|\det_{\operatorname{ran}Q_N}D_N|\to0\) uniformly there, and (1) gives the assertion.

## Current assessment
[Selected decision](#decision-negative-compression-reviewed)

## Assessment history

### Decision negative-compression-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18T00:35 |
| status | open |
| reason | Cyclicity gives an exact determinant on the negative spectral subspace, and inertia identifies the Hermitian comparison potential. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Product class and ordinary limits](#statement) | Complex finite-variance Wigner inputs with positive injective free first factor. |
| argument | [Finite factorization](#argument) | Singular and indefinite finite first factor and the unitary compression at \(i\). |
| support | [Hermitian comparison](#comparison) | Inertia counts, singular-value tails and the locally uniform limit. |
| support | [Sufficient condition](#sufficient) | Full-sequence ordinary log convergence under (2). |

### Decision negative-compression-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-18T00:38 |
| status | proved |
| reason | The finite sign factorization and range inertia identify a convergent Hermitian determinant and leave precisely a determinant on the negative subspace of the first factor. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact determinant on the negative subspace](#statement) | The two finite factors and free positivity assumptions. |
| argument | [Complete proof](#argument) | Finite factorization and the unitary compression at i. |
| support | [Convergent Hermitian determinant](#comparison) | Weak spectral law, positive logarithmic tails and locally uniform potentials. |
| support | [Sufficient estimate](#sufficient) | The norm of the negative part and ordinary nonreal logarithms. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0366_v3.md#negative-compression-whole-proof) | All fixed claims and their scope for exact linearization. |
