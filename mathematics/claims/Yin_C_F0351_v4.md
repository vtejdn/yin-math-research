---
author: Yin
---

# Summable Wigner determinant deviations for fixed laws with fine atomic components

<a id="statement"></a>
## Original-law conclusions

Let \(P_N=A_NB_N+2B_NA_N\) and \(P=s_1s_2+2s_2s_1\) in the real [finite fourth off-diagonal and finite second diagonal moment model](Yin_C_F0186_v26.md#statement).
Both raw strict upper laws \(\sigma_A,\sigma_B\) are fixed, centered and of variance one.
At each size \(N\), suppose that these same two laws admit decompositions
\[
 \sigma_i=p_{i,N}\nu_{i,N}+(1-p_{i,N})\eta_{i,N},\qquad 0<p_{i,N}\le1,\quad i=A,B,
\]
where the component laws \(\nu_{i,N}\) have uniformly bounded first absolute moments.
The labels used to sample these mixtures are independent across entries at that size.
They provide a representation of the prescribed fixed marginals, and impose no condition across dimensions.
Put \(k=2\lfloor\log^3(N+3)/2\rfloor\).
Assume
\[
 \frac{p_{A,N} k}{\log N}\to\infty,\qquad
 \frac{p_{B,N}^2 N}{\log N}\to\infty .
\]
Suppose there is a deterministic \(T_N\) with \(T_N/\log N\to\infty\), \(kT_N=o(N)\), such that for every constant \(c>0\) and each \(i\),
\[
 \sum_{N\ {\rm large}} k Q_{\nu_{i,N}}\big(e^{-c T_N}\big)<\infty ,
 \qquad Q_\nu(t)=\sup_{x\in\mathbb R}\nu([x-t,x+t]).
 \tag{Fine}
\]
The two colors may be interchanged because interchanging them transposes \(P_N\), preserving determinants and shifted singular values.

For every allowed coupling the eigenvalue laws of \(P_N\) converge weakly almost surely to the Brown measure of \(P\).
With \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\), the [terminal probability series](Yin_C_F0186_v36.md#statement) is finite for every integer disk and every positive threshold.
For every deterministic \(z_N\to z\notin\mathbb R\), the untrimmed normalized log determinants converge almost surely to \(u(z)=\tau\log|P-z|\).
On every compact \(K\subset\mathbb C\setminus\mathbb R\) and for each \(\varepsilon>0\) the stronger marginal series is finite:
\[
 \sum_N\sup_{w\in K}\Pr\!\left\{\left|N^{-1}\log|\det(P_N-wI)|-u(w)\right|>\varepsilon\right\}<\infty .
\]
Both fixed laws may be purely atomic.

<a id="argument"></a>
## Compression estimates under size-dependent decompositions of the same law

Use the [two-color compression](Yin_C_F0351_v2.md#argument) at this \(k\).
All input spectral estimates, the [original cross-block rank guard](Yin_C_F0196_v4.md#statement), the two trims of the uncompressed minor and the [first \(r\) projection tests](Yin_C_F0351_v2.md#discrete-overlaps) depend only on the original fixed laws.
In particular the summable \(O(q_n n^{-5/4})\) failure of those linear tests uses the concentration of the full entry law through its real-scalar inverse theorem and the near-mode arithmetic exclusion.
The hypothetical components enter only the later single-column quadratic tests and the separate matched interior.

For each later column the [symmetric quadratic form](Yin_C_F0351_v2.md#quadratic-matchings) has a matching with at least \((n-k)/4\) disjoint edges or loops of coefficient modulus at least \(c_\delta N^{-12}\) on the norm guard and on a compact parameter region \(|\operatorname{Im}z|\ge\delta>0\).
Conditional on the past this matching is fixed before sampling the labels of the fresh column.
The chance that none of these edges retains both endpoints is at most \(\exp(-c p_{B,N}^2(n-k))\), including loops, whose success probability is at least \(p_{B,N}^2\).
The union over \(k\) columns is summable.
After revealing residuals, at least one quadratic coefficient in the remaining entries retains this lower bound.
The [degree-two product sublevel estimate](Yin_C_F0186_v31.md#product-polynomial-sublevel) is uniform here: its one-dimensional interval bound uses the first absolute moment only for the outer tail, and its fixed-degree induction uses only the degree and this common moment bound besides the displayed concentration function.
It applies also to atomic laws.
At threshold \(e^{-2T_N}\), divide by the maximal coefficient, which is at least \(c_\delta N^{-12}\).
The failure at each step is bounded by \(C Q_{\nu_{B,N}}(C e^{-cT_N})+Cn e^{-cT_N}\) in addition to the label and norm exceptions.
The condition (Fine) absorbs constant factors in the interval radius by decreasing \(c\).
The resulting union over \(k\) columns is summable.
On successful columns the determinant ratios are nonzero and the logarithmic cost, including normalization of the columns, is \(O(kT_N+k\log N)\).

<a id="atomic-matching"></a>
## Interior matching without atomlessness

Split the \(k\) interior sites into two fixed sides of size \(l=k/2\).
A perfect matching of regular labels may be selected using the labels alone.
For independent Bernoulli edges of parameter \(p=p_{A,N}\), Hall's obstruction and a union bound give failure probability at most
\[
 \sum_{s=1}^{l}\binom ls\binom l{s-1}(1-p)^{s(l-s+1)} .
\]
The terms are symmetric under \(s\leftrightarrow l-s+1\).
For \(s\le(l+1)/2\) each is at most \(\exp(2s\log l-psl/2)\).
Since \(p l/\log N\to\infty\), this sum is \(O(e^{-p l/4})\) and hence summable.

After revealing every unmatched entry, use the [interior determinant and top matched coefficient](Yin_C_F0186_v33.md#argument).
At an admissible parameter the top successive coefficient is the deterministic nonzero \(N^{-k}\).
Expose the \(l\) matched entries in reverse order of coefficient extraction.
If the already computed leading coefficient is nonzero, the next polynomial divided by it is monic of degree four.
Conditional on previous successful draws, the probability that its modulus is below \(e^{-T_N}\) is at most \(4Q_{\nu_{A,N}}(e^{-T_N/4})\), by covering the real line near the four complex roots.
Count an exact zero as failure and stop the reverse exposure at its first failure.
This conditional procedure never divides by zero, including for a discrete component.
A union bound gives summable failure by (Fine), and the initial coefficient and successful ratios cost at most \(k\log N+lT_N\) in the logarithm.

<a id="conclusions"></a>
## Passing to the original model

On a fixed compact set off the real axis, the estimates just proved give the [undivided product inequality](Yin_C_F0351_v3.md#fixed-compressions) with parameter-uniform summable exceptional probabilities and errors \(O((q_n^3\log N+kT_N+k\log N)/N)=o(1)\).
All other factors and normalizations are the ones in the [original matrix comparison](Yin_C_F0351_v2.md#interior).
The initial proof of the inequality uses parameters outside the finite spectra of the intermediate compressions for each sample.
Fubini and the continuity argument for the undivided inequality extend the same probability bound to each deterministic nonreal parameter.
Under the independent coupling, the [moving-shift trimmed limits](Yin_C_F0351_v3.md#statement) apply to the old minor after the original \(n/N\) rescaling, and Borel--Cantelli gives the corresponding untrimmed limit.
The same proof works under any coupling because those input bounds are marginal and summable.
The compact uniform marginal assertion follows from the [compactness and independence argument](Yin_C_F0351_v3.md#uniform-marginals).
For the Brown conclusion, for fixed \(z\notin\mathbb R\) use the pointwise assertion and Fubini over the plane.
The [pathwise local planar square bound](Yin_C_F0186_v4.md#noncompact-planar) upgrades convergence at almost every parameter on one sample event to local \(L^1\) convergence of potentials there.
Their distributional Laplacians converge, and tightness gives weak convergence of the eigenvalue probabilities.
The [terminal equivalence](Yin_C_F0186_v36.md#statement) now gives the deviation series at the original marginals.

<a id="dyadic-example"></a>
## A pair of fixed purely atomic laws

Choose an integer \(j\ge1\) with probability \(1/(j(j+1))\).
Given \(j\), sample uniformly from the \(2^j\) midpoints of the equal subintervals of \([-1,1]\), and divide by the standard deviation of the unconditional sample.
This defines a fixed bounded symmetric variance-one law with countable support in the measure-theoretic sense.
Every individual grid value is an atom, and the closed support also contains the accumulation points.
Use this law for each strict upper input, independently within the prescribed Wigner model, and for instance take both diagonals zero.
At dimension \(N\), call levels \(j\ge J_N=\lceil6\log_2(N+1)\rceil\) regular.
Their mass is \(1/J_N\) by telescoping.
Their mixture has bounded first moment, and a uniform grid interval count gives \(Q_{\nu_N}(s)\le C(s+2^{-J_N})\) after the fixed rescaling.
Taking \(T_N=\log^2(N+3)\) verifies (Fine), \(kT_N=o(N)\) and both matching assumptions.
This proves the terminal series for two fixed purely atomic laws, also with arbitrary centered second-moment diagonals.

For strict upper laws with fixed positive regular components of logarithmic decay exponent greater than one, [C351v2](Yin_C_F0351_v2.md#statement) gives the corresponding fixed-component conclusion.
For a finite-support law with at most \(b\) atoms, every component of positive mass has a maximal atom of mass at least \(1/b\).
Such a law cannot satisfy (Fine), even when its mixture representation is allowed to depend on \(N\).

## Current assessment
[Selected decision](#decision-fine-atoms-reviewed)

## Assessment history

### Decision fine-atoms-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:42 |
| status | open |
| reason | The component analysis extends the conditional probability estimates to atomic measures at the required shrinking scale and supplies an explicit fixed example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Model and assertions](#statement) | Terminal summability, Brown convergence and ordinary logarithms for the specified fixed laws. |
| argument | [Compression proof](#argument) | The original-law linear tests, scaled quadratic small balls and monic ratios. |

### Decision fine-atoms-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:48 |
| status | proved |
| reason | Independent review verified the size-dependent decomposition of the fixed laws, the reverse exposure with atomic draws, terminal summability and the explicit dyadic example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed laws and conclusions](#statement) | Full Brown convergence, summable terminal losses and fixed nonreal shift convergence under the fine-component conditions. |
| argument | [Original cross block](#argument) | Original-law overlaps, disjoint quadratic coefficients and summable label and sublevel exceptions. |
| support | [Matched interior](#atomic-matching) | Hall matching and reverse monic exposure with exact zeros counted as failures. |
| support | [Planar and pointwise limits](#conclusions) | Every coupling, fixed moving parameters, uniform single-parameter marginal probabilities and the planar criterion. |
| support | [Purely atomic example](#dyadic-example) | Two countably supported fixed bounded input laws and the finite-support boundary. |
| dependency | [First column estimates](Yin_C_F0351_v2.md#discrete-overlaps) | Original distribution at each dimension. |
| dependency | [Fixed parameter comparison](Yin_C_F0351_v3.md#fixed-compressions) | Undivided continuous product inequality and the ordinary logarithm. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v4.md#fine-atomic-laws-whole-proof) | Entire statement at its fixed-law scope. |
