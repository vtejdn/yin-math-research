---
author: Yin
---

# Erd49: finite-variance complete convergence of independent averages

<a id="erd49-u001"></a>
## Inspected sufficiency theorem and attribution

Use the [1949 paper in the Rényi archive bundle](readme.md#renyi-bundle), printed p. 286 for the statement and pp. 286--288 for the sufficiency proof.
The paper explicitly attributes centered finite-variance sufficiency to Hsu and Robbins, whose original bibliographic identity is HR47 in the shared bibliography.
That original paper's proof was not inspected.
The stated sufficiency and its applicability are accepted here after direct inspection of the primary Erdős passage.
The necessity proof and the appended later remark are outside this inspection.
This is source preparation and development, not an independent project-proof review.

In standard normalized notation, let \(Z_1,Z_2,\ldots\) be independent copies of a real law with
\[
 \mathbb EZ_1=0,\qquad \mathbb EZ_1^2<\infty.
\]
Then, for every \(\varepsilon>0\),
\[
 \sum_{N=1}^{\infty}
 \mathbb P\left\{\left|\frac1N\sum_{i=1}^NZ_i\right|>\varepsilon\right\}<\infty.
 \tag{Hsu-Robbins-sufficiency}
\]
The source states summability of probabilities for sums at a linear threshold and notes the rescaling to any fixed positive threshold.
Its sufficiency proof separates large terms, bounds the event of two moderately large terms using independence, and applies a fourth-moment bound to centered truncated sums.
No finite fourth moment of \(Z_1\) is required.
The conclusion is a statement about the marginal law at each size, so it also applies when each size has a fresh row of independent copies with arbitrary dependence between sizes.

<a id="complete-convergence-definition"></a>
## Definition: complete convergence

A sequence of real random variables \(X_N\) converges completely to a real number \(a\) if
\[
 \sum_N\mathbb P\{|X_N-a|>\varepsilon\}<\infty
 \qquad\hbox{for every }\varepsilon>0.
\]
No independence of the sequence \(X_N\) is part of this definition.
It implies almost-sure convergence by first Borel--Cantelli, and depends only on the one-size marginal laws.
The displayed terminology is the conventional formulation of the source's summability conclusion, with the normalization of (Hsu-Robbins-sufficiency).

<a id="paired-row-application"></a>
## Exact squared-entry specialization

For a real centered variance-one law \(\xi\) with finite fourth moment and independent copies \(\xi',\xi''\), put
\[
 Y=(\xi')^2+(\xi'')^2,\qquad Z=Y-2.
\]
Then \(\mathbb EZ=0\) and \(\mathbb EZ^2<\infty\), so (Hsu-Robbins-sufficiency) gives
\[
 \sum_N\mathbb P\left\{N^{-1}\sum_{i=1}^N
       [(\xi_i')^2+(\xi_i'')^2]>4\right\}<\infty.
\]
This is exactly one input law's paired-row norm error in C194v30.
The two laws are summed separately.
The conclusion uses fourth moments of the original entries because their squares must have finite variance; it does not follow here from second moments of \(\xi\) alone.
