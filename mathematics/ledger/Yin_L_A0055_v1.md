---
author: Yin
---

# Spatial decay of a kernel projection would give integrality on the four-line groups

Take a torsion-free word-hyperbolic realization \(G\) of the four-line law as established by the [pattern-free criterion and its application](Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws).
Every projection over \(C_r^*(G)\), including matrix projections with the unnormalized matrix trace, has integral trace by the [assembly argument](Yin_L_A0054_v1.md#from-hyperbolicity-to-integral-traces).
There is an approach to the remaining, potentially nonclosed-range operators which uses the Fourier coefficients of the actual nullspace projection.

For a finite matrix \(A\) over \(\mathbb CG\) with \(m\) columns put \(p=1_{\{0\}}(A^*A)\) in \(M_m(\mathcal N(G))\).
Let \(p(g)\) be the \(m\)-by-\(m\) matrix of its group Fourier coefficients and let \(|g|\) be word length for the rose marking.
For \(j\ge0\) put \(b_j^2=\sum_{2^j\le |g|<2^{j+1}}\|p(g)\|_{\rm HS}^2\).
Either of the following bounds suffices for integrality of \((\operatorname{Tr}_m\otimes\tau)p\):
\[
   \sum_{j\ge0}2^{3j/2}b_j<\infty,\qquad\text{or}\qquad
   \sum_g(1+|g|)^{3+\delta}\|p(g)\|_{\rm HS}^2<\infty
                   \quad\text{for some }\delta>0 .
\]
The constants in the group norm estimates below need only hold on the single realized group under consideration.

## Proof and the obstruction at a fractional trace

The ball form of the Haagerup inequality on a non-elementary hyperbolic group bounds the norm of a group polynomial supported in a radius-\(r\) ball by \(C_G(1+r)^{3/2}\) times its coefficient \(\ell^2\)-norm. [Nica, introduction, inequality for balls](../literature/pdf/Nic17--arxiv.pdf#page=1)
A torsion-free elementary hyperbolic group is trivial or infinite cyclic, so the binary zero divisors in this construction ensure that \(G\) is non-elementary.
Applying the inequality entry by entry bounds the operator norm of the \(j\)-th matrix shell by \(C_{G,m}2^{3j/2}b_j\).
The first displayed assumption makes the Fourier partial sums norm Cauchy in \(M_m(C_r^*(G))\).
Their limit equals \(p\) since they also converge to \(p\) in trace \(L^2\), where operator-norm convergence implies convergence in \(L^2\).
The trace integrality follows.
The second assumption implies the first by Cauchy–Schwarz with \(\sum_j2^{-j\delta}<\infty\).

Conversely if \(p\) had fractional trace, its norm distance to \(M_m(C_r^*(G))\) would be **exactly \(1/2\)**.
Indeed if \(\|p-a\|<1/2\), replacing \(a\) by its selfadjoint part preserves this strict bound.
The selfadjoint segment between \(p\) and that part has a common spectral gap about \(1/2\), by the norm bound from the spectrum of the projection \(p\).
Functional calculus along the segment gives a norm-continuous path of projections in the matrix von Neumann algebra from \(p\) to a matrix projection over the reduced group algebra.
Projections at sufficiently close parameter values are unitarily equivalent, hence the trace stays constant along the segment of spectral projections.
The end trace is an integer, a contradiction.
The upper bound is attained by \(\tfrac12 I_m\).
In particular any fractional trace would force divergence of *every* weighted moment in the display, even though \(\sum_g\|p(g)\|_{\rm HS}^2\) is finite.

These are spatial estimates for the projection, so they do not require a spectral gap for \(A^*A\).
For example take the row \((1-g,0)\) with \(g\) of infinite order.
The cyclic shift has no invariant vector in the regular representation and has approximate invariant unit vectors on longer intervals in \(\langle g\rangle\), so the row has nonclosed range.
Its kernel projection \(\operatorname{diag}(0,1)\) satisfies both tail conditions.
For a nonzero scalar satisfying either condition the integral kernel trace must be zero.
The present product-fiber and finite-support estimates do not control the shell sums of \(p\) for an arbitrary matrix.
Proving the bounds for the relevant projections, or otherwise producing a reduced-algebra projection of the same trace, remains the analytic step.

The binary zero product rules out virtual compact specialness for these torsion-free groups, since the group algebra of every torsion-free virtually compact special group over \(\mathbb F_2\) embeds in a division ring. [Fisher and Sánchez-Peralta, Theorem 1.3(1)](../literature/pdf/FSP26.pdf#page=3)
This obstruction applies to that geometric route and leaves the complex-coefficient projection question open.
