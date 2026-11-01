---
author: Yin
---

<a id="vv16-u001"></a>
# VV16: First Derivatives of Tensor Bernstein Approximants

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | The [institutional repository](https://eprints.whiterose.ac.uk/id/eprint/106084/) identifies the [author PDF](https://eprints.whiterose.ac.uk/id/eprint/106084/1/tr182a2-copy-for-UoL.pdf) as its accepted version. |
| source-locator | Directly inspected: equation (5), printed p.4; Theorem 3, printed p.6; Theorem 4 and its notation, printed p.7. |
| inspection | Accepted on 2026-09-11 by the coordinating agent at exact-statement and applicability inspection depth; the original proof is not independently audited. |

Date/reviewer: 2026-09-11, the group-theoretic research agent.
This is a bounded source audit for Q3.

## Original source and inspection

A. Yu. Veretennikov and E. V. Veretennikova, *On partial derivatives of multivariate Bernstein polynomials*, Siberian Advances in Mathematics 26(4) (2016), 294–305, DOI [10.3103/S1055134416040039](https://doi.org/10.3103/S1055134416040039).
The Russian original appeared in Matematicheskie Trudy 18(2) (2015), 22–38.

The [institutional repository](https://eprints.whiterose.ac.uk/id/eprint/106084/) identifies the [author PDF](https://eprints.whiterose.ac.uk/id/eprint/106084/1/tr182a2-copy-for-UoL.pdf) as its accepted version.
The PDF has 20 physical pages, including one repository cover page; the manuscript is dated 2016-10-16 and has 19 numbered pages.

Directly inspected: equation (5), printed p.4; Theorem 3, printed p.6; Theorem 4 and its notation, printed p.7.
These are physical PDF pages 5, 7 and 8.
Formula (5) is the tensor polynomial on the cube, distinct from the simplex construction (4).
Theorem 3 gives uniform function convergence.
Theorem 4(1), with m=1 and d=2, gives uniform convergence of both first partial derivatives for a function in C^1(R^2).
No mixed second derivative is required.
Later proof-page retrievals timed out, so this record accepts the exact source statement and checks its application; it does not claim a full proof or full article audit.

## Rectangle interface checked here

Let R=[a,b]×[c,d], with a<b and c<d, and let f be complex-valued and C^1 on an open neighborhood U of R.
There exist polynomials P_n in the two real coordinates, with complex coefficients, such that

\[
\|P_n-f\|_{C(R)}+\|\partial_xP_n-\partial_xf\|_{C(R)}
+\|\partial_yP_n-\partial_yf\|_{C(R)}\longrightarrow0.
\]

To match the source's global domain exactly, choose a slightly larger rectangle contained in U and a smooth product cutoff which equals one near R and whose support is contained in that larger rectangle.
Extend the product of f and this cutoff by zero.
This gives a C^1 function on R^2 with the same values and first derivatives near R.
The cutoff is a product of ordinary one-variable smooth plateau functions, so no boundary extension theorem is needed.

Pull back by Phi(s,t)=(a+(b-a)s,c+(d-c)t).
Apply formula (5) to the real and imaginary parts of f composed with Phi.
For g on [0,1]^2 the resulting polynomial is

\[
\widetilde B_ng(s,t)=\sum_{i,j=0}^n g(i/n,j/n)
\binom ni s^i(1-s)^{n-i}\binom nj t^j(1-t)^{n-j}.
\]

Then set P_n=\widetilde B_ng composed with Phi^{-1}.
The derivative errors acquire the fixed factors (b-a)^{-1} and (d-c)^{-1}; both still tend uniformly to zero.
Complex linearity gives the stated complex-valued conclusion.
The approximation uses polynomials in x and y, not holomorphic polynomials in x+i y.

## Reuse and boundary

Local searches in audits, literature and ledger found no previously accepted approximation result with this C^1 conclusion.
[Tre17](../Tre17/Yin_U001.md) concerns analytic functions and weighted Chebyshev coefficient decay; it is stronger in smoothness and does not replace the present C^1 source statement.
Existing Runge records concern holomorphic approximation.
The present source supplies only convergence of functions and first partial derivatives.
It supplies no prescribed convergence rate, weighted coefficient summability or operator graph-norm estimate.
Those remain the consumer's separate obligations.
