---
author: Yin
---

# Wigner product determinants at the positivity threshold for bounded and atomic inputs

<a id="statement"></a>
## Ordinary determinants at nonreal shifts

Use the [fixed-law finite-variance Wigner model](../tasks/Yin_T_F0014_v1.md#contract), allowing arbitrary coupling across dimensions.
Let \(A_N=2I+X_N\), \(P_N=A_NB_N\), \(p=(2+s_x)B(s)\), and \(u(z)=\tau\log|p-z|\).
All colors other than \(X\) may have arbitrary admissible real or complex laws with just their second moments, including atomic laws.
The following results concern two choices of the first color.

1. Suppose the real raw off-diagonal and diagonal laws of \(X\) are bounded and take \(B=XY+YX+ZYZ\).
   This includes symmetric signs off the diagonal with either signs or zeros on the diagonal.
   The ordinary logarithms \(N^{-1}\log|\det(P_N-zI)|\) converge to \(u(z)\) locally uniformly on \(\mathbb C\setminus\mathbb R\) in probability through all dimensions and almost surely along all dyadic dimensions.
2. There is a fixed symmetric purely atomic law for the diagonal and strict upper entries of the first raw color, with variance one and infinite \(2+\epsilon\) moment for every \(\epsilon>0\), and a deterministic increasing sequence of dyadic dimensions \(N_j\) for which \(A_{N_j}>0\) eventually almost surely.
   For every fixed selfadjoint polynomial \(B\), even one using \(X\), the same locally uniform almost-sure logarithmic convergence holds along \(N_j\).

In either case, for each allowed coupling and fixed polynomial there is one event of probability one on which
\[
       \limsup_{N\to\infty}N^{-1}\log|\det(P_N-zI)|=u(z)
       \quad\text{for every }z\notin\mathbb R .
\]
The [finite and free word-chain identities](../ledger/Yin_L_F0061_v2.md#linearization-transfer) give the same limsup for the associated fixed affine pencil at each such \(z\), with logarithms divided by its auxiliary size.

<a id="rates"></a>
## The size and probability of the nonreal logarithmic loss

Use \(S=|A_N|^{1/2}\), \(Q=\mathbf1_{(-\infty,0)}(A_N)\), \(C=SB_NS\) and the compression \(D_N(z)=I_Q+2zQ(C-zI)^{-1}Q\) on the range of \(Q\).
Let \(L_N(z)=N^{-1}\sum_{\operatorname{Im}\lambda\ne0}\log^-|\lambda-z|\) sum over the nonreal eigenvalues of \(P_N\) with algebraic multiplicity.
For each compact \(K\subset\mathbb C\setminus\mathbb R\) in case 1, outside an event of probability at most \(C_KN^{-1/16}\),
\[
      \sup_{z\in K}\|D_N(z)+I_Q\|\le C_K N^{-1/16},
      \qquad
      \sup_{z\in K}L_N(z)\le C_K N^{-3/4}.
      \tag{1}
\]
If the diagonal raw law is the same as the off-diagonal law, the exponent \(1/16\) in the probability and compression estimates may be replaced by any fixed \(0<a<1/6\), and \(N^{-3/4}\) by \(N^{-1+\eta}\) for any fixed \(\eta>0\), with constants depending also on \(a,\eta\).
For instance \(a=1/8,\eta=1/16\) apply when all upper entries including the diagonal are independent symmetric signs.

<a id="argument"></a>
## Counting nonpositive eigenvalues of the first factor

First give every independent upper entry of a real matrix \(\widehat X\), including its diagonal, the bounded centered raw off-diagonal law of \(X\), normalized by \(\sqrt N\).
The [rigidity theorem of Erdős, Yau and Yin](../audits/literature/EYY12/Yin_U001.md#eyy12-u001), arXiv v7, Theorem 2.2, (2.25), applies: the variance matrix has all entries \(1/N\), and this fixed bounded law has the required uniform subexponential tail.
If \(\gamma_i\) is the \(i/N\) quantile of the variance-one semicircle law, then for every fixed \(\epsilon,M>0\), except with probability \(O_{\epsilon,M}(N^{-M})\),
\[
        \max_{1\le i\le N}|\lambda_i(\widehat X)-\gamma_i|
           \le N^{-2/3+\epsilon}.
        \tag{2}
\]
Indeed the theorem's extra factor is \(N^{o(1)}\min(i,N-i+1)^{-1/3}\), and its error probability is smaller than every fixed power.
If the diagonal has a different bounded law, use the same strict upper entries for the two matrices and take independent diagonal copies for \(\widehat X\).
The diagonal replacement has operator norm at most \(C/\sqrt N\), so the ordered eigenvalues differ by at most that amount.
This is a comparison of one-size marginal probabilities and imposes no cross-size coupling condition.

Write \(r_N=\#\{\lambda_i(X_N)\le-2\}\) and \(T_N=\operatorname{Tr}(2I+X_N)_-\), using the unnormalized trace.
If the maximum classical-location error is at most \(d\), every eigenvalue counted by \(r_N\) has depth at most \(d\) below \(-2\) and classical location at most \(-2+d\).
The semicircle density at \(-2+t\) is at most \(C\sqrt t\), hence \(r_N\le CNd^{3/2}\) and \(T_N\le CNd^{5/2}\).
Thus on an event depending only on \(X_N\), with complement of probability \(O_M(N^{-M})\), one has \(\|X_N\|\le3\) and the following bounds.
For an arbitrary bounded diagonal take \(d=C N^{-1/2}\) by (2) with \(\epsilon<1/6\), obtaining \(r_N\le C N^{1/4}\) and \(T_N\le C N^{-1/4}\).
For the same law on and off the diagonal, take \(d=N^{-2/3+\epsilon}\), giving \(r_N\le C N^{3\epsilon/2}\) and \(T_N\le C N^{-2/3+5\epsilon/2}\).

<a id="covariance"></a>
## Covariance, compression and the dyadic limit

Suppose on the preceding event that \(T_N\le C N^{-4a}\) and \(\|X_N\|\le3\).
Put \(H=SQ\), so \(\|H\|_{\rm HS}^2=T_N\), and \(F_Z=\operatorname{Tr}(Z^2)/N\).
The [covariance inequalities](Yin_C_F0360_v1.md#negative-trace) give \(\mathbb E(F_Z)\le C\) and, conditional on \(X_N\),
\[
     \mathbb E\big[\|XYH\|_{\rm HS}^2+\|YXH\|_{\rm HS}^2
                           +\|ZH\|_{\rm HS}^2\mid X_N\big]\le C T_N.
\]
Conditional on \(X_N,Z_N\), they give \(\mathbb E_Y\|ZYZH\|_{\rm HS}^2\le C F_Z\|ZH\|_{\rm HS}^2\).
Discard \(F_Z>N^a\) at probability cost \(O(N^{-a})\).
On its complement, conditional Markov at threshold \(N^{-a}\) for the Hilbert--Schmidt norm, followed by integration over \(Z_N\), bounds the probability of a large cubic term on the good \(X_N\) event by \(C N^{2a+a-4a}=C N^{-a}\).
This truncation does not assume that \(F_Z\) and \(ZH\) are independent or that \(Z\) has a fourth moment.
Each of the two quadratic terms exceeds the same threshold with probability at most \(C N^{-2a}\) on the good event.
Since \(\|S\|\le\sqrt5\) there, this proves \(\|CQ\|\le C N^{-a}\) outside an event of probability \(O(N^{-a})\).
Use \(a=1/16\) for bounded diagonals; in the identical-law case choose \(\epsilon>0\) small enough that \(2/3-5\epsilon/2\ge4a\) and \(3\epsilon/2\le\eta\).

For \(h=\operatorname{dist}(K,\mathbb R)>0\), the [resolvent compression bound](Yin_C_F0358_v3.md#sufficient) gives \(\|D_N(z)+I_Q\|\le 4\|CQ\|/h\) throughout \(|\operatorname{Im}z|\ge h/2\).
For large \(N\) on the same event this is less than one, so \(D_N(z)\) is invertible throughout that region.
The [exact determinant factorization](Yin_C_F0358_v3.md#argument) then puts all nonreal eigenvalues in \(|\operatorname{Im}\lambda|<h/2\).
Their number is at most \(2r_N\) by the [finite count](Yin_C_F0358_v2.md#argument), including a possible kernel of \(A_N\).
Their distance to \(K\) is at least \(h/2\); hence \(L_N(z)\le (2r_N/N)\log^-(h/2)\) there, proving (1).
The bounds imply \(\sup_K L_N\to0\) in probability and almost surely along \(N=2^j\) by the first Borel--Cantelli lemma.
The [ordinary potential decomposition](Yin_C_F0358_v2.md#loss) gives the logarithmic limits and the whole-sequence upper bound on \(K\), since \(2+s_x\) is positive and injective by the semicircle law.
A countable compact exhaustion gives one event throughout \(\mathbb C\setminus\mathbb R\).

<a id="atomic"></a>
## A fixed atomic law with no moment above two

Prescribe variance masses \(v_j=2^{-j}\) for \(j\ge1\).
For increasing \(t_j\ge2^{j^2}\), give each of \(t_j,-t_j\) probability \(v_j/(2t_j^2)\) and give the remaining mass to zero.
There is positive mass at zero, the mean vanishes by symmetry, and the variance is \(\sum_jv_j=1\).
For every \(\epsilon>0\) the \(2+\epsilon\) moment equals \(\sum_j v_jt_j^\epsilon=\infty\).

The sequence of magnitudes and favorable dimensions can be chosen recursively.
Start with \(t_1=2\).
After \(t_1,\ldots,t_j\) have been chosen, put mass from all omitted magnitudes at zero and form \(X_N^{[j]}\) with this bounded law for every raw upper entry including the diagonal.
Its raw variance is \(\sigma_j^2=\sum_{k\le j}v_k=1-2^{-j}\).
For this fixed \(j\), apply (2) to \(X_N^{[j]}/\sigma_j\); the law-dependent constants may depend on \(j\).
As \(2\sigma_j<1+\sigma_j<2\), there exists a dyadic \(N_j>N_{j-1}\) (start with \(N_0=1\)) such that \(\Pr(\|X_{N_j}^{[j]}\|>1+\sigma_j)\le2^{-j}\).
For definiteness take the smallest such dyadic and choose \(t_{j+1}=\max(2t_j,2N_j,2^{(j+1)^2})\).
This determines one fixed law, independently of future matrix samples, \(B\) and the coupling.

At size \(N_j\), realize the bounded matrix by replacing every raw entry of the full model of magnitude greater than \(t_j\) by zero.
The probability that any replacement occurs is at most
\[
      N_j^2\sum_{k>j}v_k/t_k^2
      \le N_j^2\,2^{-j}/t_{j+1}^2\le 2^{-j}.
\]
Thus except with probability at most \(2^{1-j}\), \(2I+X_{N_j}\ge(1-\sigma_j)I>0\).
Summability proves eventual strict positivity under every coupling without requiring a positive lower bound uniform in \(j\).
At these sizes \(Q=0\), so the [Hermitian comparison determinant](Yin_C_F0358_v3.md#comparison) is exactly the ordinary product determinant in absolute value for every nonreal shift, whatever the shared selfadjoint polynomial \(B\).
Its known locally uniform almost-sure limit and the [full-sequence upper bound](Yin_C_F0358_v2.md#loss) prove case 2.
This construction chooses the atomic law together with its favorable dimensions and gives no such positivity conclusion for an arbitrary prescribed unbounded atomic law.

## Current assessment
[Selected decision](#decision-atomic-edge-reviewed)

## Assessment history

### Decision atomic-edge-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:07 |
| status | open |
| reason | A rigidity estimate controls the negative trace for bounded first-color laws; a separate fixed atomic law has positive first factors on selected dimensions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two ordinary determinant conclusions](#statement) | Critical first factor, arbitrary other finite-variance laws, arbitrary cross-size coupling and the associated affine pencil. |
| argument | [Counting at the lower spectral edge](#argument) | The classical-location error, bounded diagonal comparison, nonpositive count and unnormalized negative trace. |
| support | [Quantitative conclusion](#rates) | Compression, loss and probability exponents, including the independent sign ensemble. |
| support | [Covariance and determinant comparison](#covariance) | Heavy-tailed remaining colors, strip exclusion and almost-sure dyadic convergence. |
| support | [Atomic construction](#atomic) | Variance one without higher moments, deterministic favorable sizes and every fixed selfadjoint second factor. |

### Decision atomic-edge-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:13 |
| status | proved |
| reason | Edge rigidity for the bounded first law gives polynomial small-compression failure and dyadic limits, while truncation at lacunary atomic magnitudes gives favorable dimensions without any higher moment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed assertions](#statement) | Edge rigidity for the bounded first law gives polynomial small-compression failure and dyadic limits, while truncation at lacunary atomic magnitudes gives favorable dimensions without any higher moment. |
| argument | [Complete proof](#argument) | Original input restrictions, exact parameter and coupling requirements. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0369_v1.md#atomic-edge-whole-proof) | Assessment of the complete fixed proof. |
