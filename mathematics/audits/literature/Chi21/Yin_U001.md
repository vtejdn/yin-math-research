---
author: Yin
---

# Chi21: Lindeberg arrays and individual Gaussian swapping

<a id="chi21-u001"></a>
## Source and accepted scope

The inspected edition is [arXiv:2106.00871v1](readme.md#arxiv-v1), Section 3, Theorem 3 and its displayed proof on printed pages 4--6.
The centered scalar triangular-array statement is accepted with the hypotheses below.
The statement and the replacement argument were read directly in that edition; this is not an independent project-proof review or a whole-source audit.

<a id="lindeberg-array"></a>
## Exact scalar input

For each \(n\), let \(X_{n,1},\ldots,X_{n,k_n}\) be independent real random variables with mean zero and finite variance.
Assume
\[
 \sum_{i=1}^{k_n}\mathbb E X_{n,i}^2=1,
 \qquad
 \sum_{i=1}^{k_n}\mathbb E\!\left[X_{n,i}^2
             \mathbf1_{\{|X_{n,i}|>\delta\}}\right]\longrightarrow0
 \quad\text{for every fixed }\delta>0.
\]
Then \(\sum_iX_{n,i}\) converges in distribution to a standard real Gaussian.
No identical-distribution assumption within a row or independence between different rows is required.
The result supplies qualitative convergence, without a convergence rate.

<a id="swapping-mechanism"></a>
## Inspected replacement mechanism and project boundary

Replace one summand at a time by an independent centered Gaussian with the same variance.
For a smooth test function, independence and matching first two moments cancel the first two Taylor terms in the difference of expectations.
Small increments are controlled by continuity of the second derivative, and large increments by the stated second-moment tails.
The Lindeberg condition also implies that the largest summand variance tends to zero.
The Gaussian fourth-moment identity then controls the sum of Gaussian tail remainders, completing the telescoping comparison.

The [project vector adaptation](../../../claims/Yin_C_F0194_v23.md#gaussian-smoothing) separately proves the finite-dimensional covariance and uniformity statements needed for its conditional application.
This source alone does not provide that vector adaptation, uniform quadratic anti-concentration, a polynomial window estimate, or the actual random-minor diffusion premise.
