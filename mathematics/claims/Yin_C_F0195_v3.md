---
author: Yin
---

# Clipped Wigner logarithms along dimensions selected from second-moment tails

<a id="statement"></a>
## Logarithmic depth and the ordinary determinant

Consider the independent real symmetric or complex Hermitian Wigner colors of [F0013](../tasks/Yin_T_F0013_v1.md#input-model), allowing mixed colors and arbitrary couplings across dimensions.
Write \(\xi_j\) for the centered variance-one raw strict upper law of color \(j\), and assume finite second moments on the diagonal.
Fix \(\sigma\ge0\) and suppose
\[
 \sum_j\mathbb E|\xi_j|^2\big(\log(2+|\xi_j|)\big)^\sigma<\infty .
\]
For a fixed square affine pencil \(L=b+\sum_{j=1}^g A_jx_j\) of size \(m\), let \(\nu_N\) be its empirical singular-value probability measure at the normalized matrices and let \(u=\log\Delta_{\operatorname{tr}_m\otimes\tau}(L(s))>-\infty\) be its free logarithm at a standard free semicircular system.
Let \(0<\theta\le1\) be a uniform free smoothed-mass exponent for the variance-rescaled auxiliary pencils in [the comparison below](#comparison).
Such an exponent exists for every such pencil.
Put \(q=(\sigma+1)\theta/(\theta+2)\) and \(\ell_N=\log(N+2)\).

There is a deterministic increasing sequence of even dimensions on which, for each fixed \(B>0\), the clipped logarithm satisfies
\[
 \int \log\max\bigl(s,\exp(-B\ell_N^q)\bigr)\,d\nu_N(s)
       \longrightarrow u
 \quad\text{almost surely and in every finite }L^p,\ p\ge1 .
 \tag{1}
\]
The sequence may depend on the laws, the pencil and the chosen exponent, and is independent of \(B\) and of the coupling.
In particular finite second moments alone give (1) with \(q=\theta/(\theta+2)\).

If \(\sigma\ge 2/\theta\) and every raw law also satisfies the [translation condition (T)](Yin_C_F0186_v38.md#statement), then the ordinary normalized logarithm \(U_N=(mN)^{-1}\log|\det L(W^{(N)})|\) converges to \(u\) almost surely and in every finite \(L^p\) on this sequence.
The almost-sure dimension limsup on the full sequence equals \(u\).
The same limsup conclusion holds for a fixed scalar polynomial and fixed complex shift in [F0014](../tasks/Yin_T_F0014_v1.md#contract) under these assumptions on its exact linearization.
For \(\sigma=0\), (1) leaves the logarithmic contribution between its cutoff and the polynomial least-singular-value floor unresolved.

<a id="argument"></a>
## Selection from dyadic shells

For \(R_k=2^k,\ k\ge1\), define
\[
 J_k=\sum_j\left(R_k^2\Pr\{|\xi_j|>R_k\}
          +R_k^{-1}\mathbb E[|\xi_j|^3{\bf1}_{|\xi_j|\le R_k}]\right).
\]
Then \(\sum_{k\ge1}k^\sigma J_k<\infty\).
Indeed for \(x\ge2\), choose \(h=\lfloor\log_2 x\rfloor\).
The sum of the first integrand is at most \(\sum_{k\le h}k^\sigma4^k\le C_\sigma(1+h)^\sigma x^2\).
The second is at most \(x^3\sum_{k\ge h}k^\sigma 2^{-k}\le C_\sigma(1+h)^\sigma x^2\).
For \(0\le x<2\) the same bounds with weight \(C_\sigma x^2\) follow from the convergent geometric series.
Taking expectations proves summability and supplies a subsequence with \(d_k=k^{\sigma+1}J_k\to0\), since \(\sum k^{-1}\) diverges.

Along this subsequence set
\[
 w_k=\min\{\log(k+2),(d_k+k^{-1})^{-1/4}\},\qquad
 a_k=k^{-(\sigma+1)/(\theta+2)}/w_k,\qquad
 N_k=2\Big\lceil\frac{R_k^2}{2a_k^2}\Big\rceil .
\]
We have \(w_k\to\infty,\ w_k^2d_k\to0,\ R_k/\sqrt{N_k}\le a_k\), and \(\ell_{N_k}/k\to2\log2\).
Thin the sequence if necessary to make the dimensions strictly increasing.

<a id="comparison"></a>
## Rank and third moments at the same truncation scale

At \(N=N_k\) abbreviate \(a=a_k,\ R=R_k\).
Replace each strict upper entry by \(\xi_j{\bf1}_{|\xi_j|\le R}\), with its conjugate below the diagonal.
The expected normalized rank of the change is at most \(CN\sum_j\Pr\{|\xi_j|>R\}\) by the bounded rank of each physical pair.
Center each truncated law at its actual mean \(\mu_j\).
The second moment bound gives \(|\mu_j|\le R^{-1}\), so this deterministic change \(D\) has \(\|D\|_{\rm HS}^2/(mN)\le C R^{-2}\) even for complex means.
Discarding the singular directions of \(D\) above \(t\) costs normalized rank at most \(C R^{-2}t^{-2}\), and the remainder has norm at most \(t\).
The singular-value variational principle bounds the expected original count at \(t\) by the centered truncated count at \(2t\) plus the two rank costs.

Let \(v_j\) be the standard deviation of the centered truncated upper law and divide the entire centered color by \(v_j\), including the original diagonal in this division.
Eventually \(1/2\le v_j\le2\) by the second moments.
The resulting upper variance is one, its raw third absolute moment is at most \(C(1+\mathbb E[|\xi_j|^3{\bf1}_{|\xi_j|\le R}])\), and the diagonal second moments remain uniformly bounded.
The centered core is evaluated with coefficients \(v_j A_j\).
Use the [fixed-coefficient graph lift and its free kernel identity](Yin_C_F0186_v39.md#tail-subsequence) for \(v\in[1/2,2]^g\).
In this lift the random coefficients are fixed, the drift varies over a compact semialgebraic set, and every lifted free pencil has zero kernel because invertible scaling preserves the full inner rank of \(L\).
The lifted free smoothed mass at scale \(t\) is therefore at most \(Ct^\theta\) by [the uniform free estimate](Yin_C_F0195_v2.md#argument).
The graph embedding bounds the normalized core count by \(g+1\) times the normalized lifted count.

The [within-size third-moment replacement](Yin_C_F0195_v1.md#derivative-bound) is linear in the raw third absolute moments and uniform in this drift.
Using the [diagonal and Gaussian covariance comparisons](Yin_C_F0195_v1.md#covariance-interpolation) and [the uniform GOE estimate](Yin_C_F0195_v2.md#finite-count) gives
\[
 \mathbb E\nu_N([0,t])\le C\left(t^\theta+N\sum_j\Pr\{|\xi_j|>R\}
   +R^{-2}t^{-2}+N^{-1}t^{-6}
   +N^{-1/2}t^{-3}
      \left(1+\sum_j\mathbb E[|\xi_j|^3{\bf1}_{|\xi_j|\le R}]\right)\right)
 \quad(0<t\le1).
 \tag{2}
\]
The factor two in the core threshold changes only the constants, using the trivial bound for \(2t>1\).
Since \(N\asymp R^2/a^2\), the tail-rank term and the truncated third-moment term at \(t\ge a\) are together bounded by \(C a^{-2}J_k\).
Every remaining error at \(t\ge a\) decays exponentially in \(k\) up to polynomial factors because \(R=2^k\) and \(a^{-1}\le k^{(\sigma+1)/(\theta+2)}\log(k+2)\).
Consequently for some \(e_k\ge0\),
\[
 \mathbb E\nu_N([0,t])\le Ct^\theta+e_k \quad(a\le t\le1),
 \qquad k^q e_k\to0,\qquad k^q a^\theta\to0 .
 \tag{3}
\]
Indeed \(k^q a^{-2}J_k=w_k^2d_k\), while \(k^q a^\theta=w_k^{-\theta}\).

<a id="deep-clips"></a>
## From the middle count to a deep logarithmic cutoff

Set \(c_N=\exp(-B\ell_N^q)\), eventually smaller than \(a\).
For any fixed \(0<d<1\), take \(N\) large enough that \(a<d\).
The expected excess of the negative log clipped at \(c_N\) over that clipped at \(d\) is \(\int_{c_N}^d\mathbb E\nu_N([0,t])\,dt/t\).
The part below \(a\) is at most \(B\ell_N^q(Ca^\theta+e_k)=o(1)\).
The rest is at most \(Cd^\theta/\theta+e_k\log(1/a)\) by (3), and \(e_k\log(1/a)\to0\).
At fixed \(d\) the bounded continuous negative log test converges in expectation by the [weak singular law](Yin_C_F0186_v4.md#finite-variance-weak).
Sending \(d\downarrow0\) identifies the limit of the deep clipped negative-log expectations with the free negative-log integral.

The [bounded-rank row concentration](Yin_C_F0186_v4.md#row-concentration) for the original signed Hermitian dilation gives deviation probabilities at most \(2\exp(-cNx^2/(B^2\ell_N^{2q}))\) from the expectation of the clipped negative log at any \(x>0\), since the test has variation at most \(2B\ell_N^q\).
These tails are summable for fixed \(x\), and their integrals give convergence of every finite centered \(L^p\) norm to zero.
The [positive log](Yin_C_F0186_v4.md#log-statistics) converges almost surely and in every finite \(L^p\) by the fixed-law positive-tail estimates.
This proves (1) under the given coupling.

If \(q\ge1\), choose \(B\) sufficiently large in (1) that the [finite-variance least-value bound under (T)](Yin_C_F0186_v38.md#floor-statement) applies at \(c_N\) with summable failure probability.
Every sufficiently large even dimension is good by the [finite-target witness result](Yin_C_F0186_v9.md#all-even-witness).
The excess of the clipped normalized logarithm over the ordinary one lies between zero and \((\log c_N-\log s_{\min})_+\).
With the floor exponent \(\kappa>0\), the tail of this upper bound at \(x\ge0\) is at most \(CN^{5/2}\exp(-\kappa B\ell_N^q-\kappa x)\).
Increasing \(B\) makes the prefactor summable even at \(q=1\).
Borel--Cantelli and integration against \(p x^{p-1}\) remove the cutoff almost surely and in every finite \(L^p\).
Fixed-cutoff convergence through all dimensions bounds the full ordinary limsup above by \(u\), and convergence on the even subsequence gives its lower bound.
For any fixed nonconstant scalar polynomial and shift, [exact scalar linearization](../ledger/Yin_L_F0061_v2.md#linearization-transfer) multiplies the pencil and free logarithms by the same auxiliary dimension, and the [scalar free-target argument](Yin_C_F0186_v38.md#polynomial-consequences) gives finiteness also at \(z=P(0)\).
Constant polynomials have their deterministic logarithms directly.

## Current assessment
[Selected decision](#decision-dyadic-depth-reviewed)

## Assessment history

### Decision dyadic-depth-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:59 |
| status | open |
| reason | Coupling the raw truncation radius to the target count scale gives a common dyadic tail bound and a complete candidate proof of these subsequence limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Clipped and ordinary limits](#statement) | Fixed-law favorable even dimensions, the finite-second-moment depth and the logarithmic moment condition for ordinary determinants. |
| argument | [Weighted dyadic selection](#argument) | Tail probability and truncated third absolute moment at the same radius. |
| support | [Moving-variance count](#comparison) | The normalized rank and Lindeberg errors at the chosen dimensions and scales. |
| support | [Logarithmic integrals](#deep-clips) | Concentration on the original matrices, polynomial floor at the endpoint, and scalar transfer. |

### Decision dyadic-depth-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:02 |
| status | proved |
| reason | Independent whole-proof review confirmed the dyadic selection, the changing-variance comparison, the clipped limits and the ordinary determinant at the moment threshold. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Selected-dimension limits](#statement) | The clipping depth for finite second moments and for higher logarithmic weights. |
| argument | [Common dyadic selection](#argument) | Weighted convergence of the tail probability and truncated third moment. |
| support | [Intermediate singular values](#comparison) | Varying truncation with free coefficients represented by a compact drift family. |
| support | [Clipped and ordinary logarithms](#deep-clips) | All fixed depth factors, almost-sure and finite-\(L^p\) limits, and the polynomial-floor endpoint. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0201_v3.md#dyadic-depth-whole-proof) | Whole theorem, scalar normalization and the residual finite-variance gap. |
