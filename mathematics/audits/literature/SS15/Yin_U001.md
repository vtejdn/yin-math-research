---
author: Yin
---

# SS15-U001: Haar and semicircular matrix-polynomial algebraicity, Puiseux expansions and atom boundaries

<a id="ss15-u001"></a>
## Edition and accepted inputs

The selected edition is the retained [SS15--arxiv-v1.pdf](../../../literature/pdf/SS15--arxiv-v1.pdf), with its [visible date labels and edition limits](readme.md).
The reading covers Theorem 1.1 on PDF pp. 1--2, Corollary 1.2 and the Haar-algebraicity attribution on p. 3, the analytic/Puiseux and logarithmic explanations on p. 4, and Definition 5.3 on p. 18.
Theorem 1.1(5)--(7) on p. 2 was visually inspected as well as read in the source text.
Theorem 1.1(5)(6) is accepted as an established external input for fixed selfadjoint matrix polynomials in either a free semicircular family or a free Haar-unitary family, including adjoints.
Part (7) is accepted at its punctured positive logarithmic-integrability statement, and Corollary 1.2 at its scalar semicircular nonconstant-polynomial statement.
Their proofs and external dependencies were not independently re-audited in full here.
The source says the Haar case of part (5) is contained in the proof of its reference [15], Theorem 3.6, while Section 5 adapts that mechanism to semicircular variables.
This is the source's attribution, not a separately performed inspection of reference [15].
This preparation develops applications and supplies no independent-review status for a project theorem.

<a id="matrix-algebraicity-and-puiseux"></a>
## Matrix-polynomial setting and analytic interface

Let \(X_1,\ldots,X_n\) be either freely independent semicircular elements or freely independent Haar unitaries in a faithful tracial \(C^*\)-probability space \((\mathcal A,\tau)\).
Let \(H=[p_{ab}(X_1,\ldots,X_n)]\in M_\ell(\mathcal A)\) be selfadjoint, with fixed noncommutative polynomial entries in the variables and their adjoints.
Let \(\mu_H\) be its probability spectral measure for \(\operatorname{tr}_\ell\otimes\tau\).
Definition 5.3 fixes
\[
 G_H(z)=\int_{\mathbb R}\frac{d\mu_H(t)}{z-t},
 \qquad \operatorname{Im}z>0.
 \tag{SS-Cauchy}
\]
Theorem 1.1(5) says its formal Laurent expansion at infinity is algebraic, equivalently satisfying a nonzero polynomial equation in the spectral variable and the transform.
Part (6) supplies a finite exceptional set \(A\subset\mathbb R\), analytic continuation through the remaining intervals, and convergent local Puiseux expansions at each \(a\in A\).
With a downward vertical slit from each exceptional point and a sufficiently small strip about the real axis, the branch agreeing with \(G_H\) above the real axis is meromorphic in a finite root coordinate at each \(a\).
Precisely, there are an integer \(q>0\) and a local radius such that \((z-a)^qG_H(z)\) has a convergent power series in the branch \((z-a)^{1/q}\) cut along \(a-i[0,\infty)\).
Thus the expansion has finitely many negative powers and rational exponents with a fixed finite denominator.
Away from \(A\), the measure is either zero or has a real-analytic density on each component interval.
With (SS-Cauchy), Stieltjes inversion gives density \(-\pi^{-1}\operatorname{Im}G_H(x+i0)\).
The unscaled \(\operatorname{Im}(g)\) density phrase printed in Theorem 1.1(6) is not used literally; its sign and factor are read consistently with Definition 5.3.
The algebraic and Puiseux conclusions are independent of that typographical normalization.

<a id="atoms-and-logarithms"></a>
## Atomlessness and punctured logarithms

For non-atomic freely independent normal inputs, Theorem 1.1(2) only forces each atom of an \(\ell\)-by-\(\ell\) matrix-polynomial distribution to have mass in \(\ell^{-1}\mathbb Z\).
It does not assert matrix-polynomial atomlessness.
A constant diagonal summand may retain an atom even when another summand is a nonconstant polynomial in a semicircle or a Haar unitary.
Corollary 1.2 concerns a nonconstant scalar selfadjoint polynomial in freely independent semicircular variables and concludes that its limiting law is non-atomic.
It does not exclude the zero atom of an arbitrary matrix polynomial.
A finite ordinary logarithmic determinant of a square operator \(L\) excludes its zero singular-value atom and hence the zero atom of its Hermitization.
Once that atom is excluded, the positive-power bound for \(\eta|\operatorname{Im}G_H(i\eta)|\) follows by the [existing matrix-valued Puiseux argument](../../../claims/Yin_C_F0186_v2.md#logarithmic-tail).
That deduction applies unchanged to the Haar alternative actually included in Theorem 1.1.

If \(\mu_H\) is supported in \([0,\infty)\), Theorem 1.1(7) states
\[
 \lim_{\varepsilon\downarrow0}\int_{\varepsilon}^{1}\log t\,d\mu_H(t)>-\infty.
 \tag{SS-punctured-log}
\]
This punctured statement omits a possible atom at zero.
It does not alone prove a positive ordinary Fuglede--Kadison determinant until that atom is separately excluded.
