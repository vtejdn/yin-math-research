---
author: Yin
---

# And13: the finite-fourth-moment spectral-inclusion input

<a id="and13-u001"></a>
## Exact statement and acceptance

On 11 November 2026, the source agent directly inspected the [arXiv-v3 reprint](readme.md#arxiv-v3), Sections 1.2.1--1.2.3, Theorem 2 and Corollary 1, pp. 3--5.
These established results are accepted at statement-and-applicability depth; the original proof was not newly audited.

For each input color \(\ell\), the source takes independent upper-triangular variables \(x_\ell(i,j)\), jointly independent across colors and pairs.
Their law depends only on \(\ell\) and whether \(i=j\), with
\[
 \mathbb Ex_\ell(1,1)=\mathbb Ex_\ell(1,2)=0,
 \qquad \mathbb E|x_\ell(1,2)|^2=1,
 \qquad \mathbb E|x_\ell(1,1)|^4+\mathbb E|x_\ell(1,2)|^4<\infty.
\]
Diagonal variables are real, and the real and imaginary parts of each off-diagonal variable are independent.
The raw Hermitian matrices \(X_\ell^N\) use the first \(N\) rows and columns of these infinite arrays; the normalized inputs are \(X_\ell^N/\sqrt N\).

For any fixed selfadjoint matrix-valued noncommutative polynomial \(f\), Theorem 2 asserts, for every \(\varepsilon>0\),
\[
 \sigma\!\left(f(X^N/\sqrt N)\right)
 \subseteq \{t:\operatorname{dist}(t,\operatorname{supp}\mu_f)<\varepsilon\}
 \quad\text{eventually almost surely},
\]
where \(\mu_f\) is the law of \(f(s)\) for standard free semicircular inputs in a faithful tracial model.
Corollary 1 asserts \(\|f(X^N/\sqrt N)\|\to\|f(s)\|\) almost surely for every matrix-valued polynomial \(f\).

## Applicability boundary

Real off-diagonal laws satisfy the real/imaginary independence condition.
Finite second moments alone on the diagonal and arbitrary coupling across sizes require the separate [project adaptation in C194v30](../../../claims/Yin_C_F0194_v30.md#exterior-proof).
This source does not directly cover dependent real and imaginary parts.
The additionally inspected Theorem 4 assumptions (14)--(20), pp. 13--14, allow some dependence but impose transpose parity and vanishing cross second moments; they are not an automatic removal of that restriction.
No spectral-interior least-singular-value estimate is asserted here.
