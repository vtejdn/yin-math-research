---
author: Yin
---

# One positive denominator in the finite-rank criterion and the obstruction to prescribing it

## Statement

Let \(G=\langle g_1,\ldots,g_d\rangle\) be a finitely generated discrete group, \(H=\ell^2(G)\), \(M=\mathcal N(G)\), \(U=L^0(M)\), and \(D_G=\operatorname{Div}_U(\mathbb CG)\).
Write \(X_j=\lambda(g_j)\), \(\rho_j\xi=\xi X_j\), and \(P_e\) for the projection onto \(\mathbb C\delta_e\).
An element \(u\in U\) belongs to \(D_G\) if and only if there exist a positive contraction \(c\in M\) with zero kernel and bounded operators \(T_1,\ldots,T_d\) of finite complex rank such that \(cu,uc\in M\),
\[
          \sum_j[\rho_j,T_j]=cP_e(uc)-(cu)P_e c,                         \tag{1}
\]
and the following matrix has zero Hilbert kernel.
Put \(V=\mathbb C c\delta_e+\sum_j\operatorname{Ran}T_j\), choose a basis \(v_1=c\delta_e,v_2,\ldots,v_n\), and set \(X_0=1\).
Let \(K\) have first column \(e_1\) and one column \((\sum_{j=0}^d a_{ij}X_j)_{i=1}^n\) for each member of a complex basis of the relations \(\sum_{ij} a_{ij}v_iX_j=0\).
The matrix tested is \(KK^*\) on \(H^n\).
Every tuple for the [two-denominator equation](Yin_C_A0131_v4.md#statement) converts to a tuple for (1) with the same individual ranks and the same test matrix in corresponding bases.

Already for \(G=\mathbb Z^2\) there is a unitary \(u\in D_G\) for which the two-denominator equation has no solution with its two denominators in the von Neumann algebra \(W^*(u)\), even allowing distinct choices and arbitrary finite-rank operators.
Furthermore, for every countable family of prescribed pairs of bounded affiliated units on \(\mathbb T^2\), there is one rational unitary for which none of these pairs solves the two-denominator equation.

## Argument

### Transport of the finite-rank witnesses

Start with bounded \(s,a,b,t\), with \(s,t\) affiliated units and \(u=s^{-1}a=bt^{-1}\), and write \(S_j\) for a finite-rank solution with these fractions.
In the affiliated ring put
\[
 c=\big(1+s^{-1}(s^{-1})^*+(t^{-1})^*t^{-1}\big)^{-1},
 \qquad l=c s^{-1},\qquad r=t^{-1}c .
\]
The inverse of this positive operator bounded below by \(1\) is a positive contraction with zero kernel.
Conjugating each of the summand inequalities by \(c\) yields \(ll^*,r^*r\le c\), so \(l,r\in M\).
Both are affiliated units and have dense range on \(H\).
The products \(cu=la\) and \(uc=br\) are bounded.
Since left multipliers commute with the right translations, \(T_j=lS_jr\) satisfy (1), by multiplying the original equation on its outer sides by \(l,r\).

The finite-dimensional space \(\operatorname{Ran}S_j\) equals \(S_j(rH)\) by density.
Hence \(\operatorname{Ran}T_j=l\operatorname{Ran}S_j\) and injectivity of \(l\) preserves each rank.
The new space \(V\) is \(l\) times the old space, because \(ls=c\).
Transporting the old basis by \(l\) preserves all relations with the first translates, since \(l\) is injective and commutes with the right translations.
The same basis of relations therefore gives precisely the same \(K\).
This proves necessity by the [prescribed-space criterion](Yin_C_A0131_v4.md#statement).
For sufficiency take \(s=t=c\), \(a=cu\), \(b=uc\) in that criterion.

### A necessary condition at a torus point

In Fourier coordinates let \(A=\mathbb C[z_1^{\pm1},z_2^{\pm1}]\) act on \(H=L^2(\mathbb T^2)\) by multiplication.
For bounded \(u\), any solution with denominators \(s,t\) gives
\[
              s\otimes_A ut=su\otimes_A t\qquad\text{in }H\otimes_A H.
\]
Indeed, the algebraic tensor \(v\otimes w\) corresponds to the finite-rank operator \(\xi\mapsto v\int w\xi\), and a commutator with \(\rho_j\) corresponds to \(vz_j\otimes w-v\otimes z_jw\). [Finite-rank tensor identification](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
Fix \(\omega=(\omega_1,\omega_2)\in\mathbb T^2\), put \(\mathfrak m_\omega=(z_1-\omega_1,z_2-\omega_2)\), \(q_\omega=\sum_j|z_j-\omega_j|^2\) and \(V_\omega=H/\mathfrak m_\omega H\) as an algebraic vector space.
Then
\[
        \mathfrak m_\omega H=\left\{h\in H:\int |h|^2/q_\omega<\infty\right\}.
\]
One inclusion follows by pointwise Cauchy–Schwarz, and the converse follows by taking coefficients \(\overline{(z_j-\omega_j)}h/q_\omega\).
The tensor equality maps to \([s]\otimes[ut]=[su]\otimes[t]\) in \(V_\omega\otimes_{\mathbb C}V_\omega\), since the action of \(A\) on \(V_\omega\) is scalar evaluation at \(\omega\).
Whenever \([s]\ne0\) and \([t]\ne0\), there is a \(\lambda\in\mathbb C\) such that
\[
               [su]=\lambda[s],\qquad [ut]=\lambda[t].                 \tag{2}
\]
Indeed apply a linear functional sending \([t]\) to one on the second factor and then use \([s]\ne0\).

### A rational unitary with no denominators in its spectral algebra

Write \(a=\operatorname{Im}(\overline{\omega_1}z_1)\), \(b=\operatorname{Im}(\overline{\omega_2}z_2)\).
These real functions belong to \(A\), and
\[
                       u_\omega=(a+ib)/(a-ib)
\]
is a rational unitary since \(a=b=0\) on a finite set.
Near \(\omega\), \((a,b)\) are smooth real coordinates with Haar measure comparable to planar Lebesgue measure, and \(q_\omega\) is comparable to \(a^2+b^2\).
In the polar coordinates \(a=r\cos\theta,\ b=r\sin\theta\) the unitary is exactly \(e^{2i\theta}\) for \(r>0\).
For denominators \(s,t\in W^*(u_\omega)\) there are bounded measurable functions \(f,g\) with \(s=f(u_\omega)\), \(t=g(u_\omega)\).
If \(s,t\) are affiliated units, then \(f(e^{2i\theta})\) and \(g(e^{2i\theta})\) are nonzero for almost every \(\theta\), by applying the coordinate formula on a punctured disk.
For every \(\lambda\in\mathbb C\), the angular integral of \(|f(e^{2i\theta})(e^{2i\theta}-\lambda)|^2\) is strictly positive.
The radial integral of \(dr/r\) diverges, so \([s(u_\omega-\lambda)]\ne0\) for every \(\lambda\) in \(V_\omega\).
The same reasoning without the factor \(u_\omega-\lambda\) gives \([s]\ne0\) and \([t]\ne0\).
This contradicts (2).
As an explicit denominator for the equation alone, \(c=(a^2+b^2)/2\) is a positive contraction with zero kernel and \(cu_\omega=u_\omega c=(a+ib)^2/2\) belongs to \(A\).
Both factors on each side of the tensor equation then lie in \(A\), where their products agree.
Telescoping the Laurent monomials expresses their difference through the two balancing relations, producing finite-rank witnesses. [Balancing by generators](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)

### Countably many prescribed pairs

Given countably many pairs \((s_i,t_i)\) of bounded affiliated units, choose \(\omega\) in the conull set of simultaneous Lebesgue points where all the \(s_i,t_i\) have nonzero values.
This application of the Lebesgue differentiation theorem uses bounded functions in a coordinate chart, which can be cut off on a larger compact neighborhood. [Tao, Theorem 1.6.19](../literature/pdf/Tao11--author-preliminary.pdf#page=162)
Use the same rational unitary \(u_\omega\) for every pair.
For any \(h\) among the given denominators there exists \(\epsilon_h>0\) such that the set \(\{|h|\ge\epsilon_h\}\) has density one at \(\omega\).
This remains true in the smooth local coordinates \((a,b)\), since these and their inverse have bounded derivatives near \(\omega\).
For each \(\lambda\in\mathbb C\), choose an angular interval on which \(|e^{2i\theta}-\lambda|\) is bounded below by a positive constant.
Inside each sufficiently small dyadic annulus \(2^{-k-1}<r<2^{-k}\), its sector intersects \(\{|h|\ge\epsilon_h\}\) in area bounded below by a positive constant times \(2^{-2k}\), by density one in the enclosing disk.
Each such intersection contributes a uniform positive lower bound to \(\int |h(u_\omega-\lambda)|^2/q_\omega\), and summation gives divergence.
The same annuli give \(\int |h|^2/q_\omega=\infty\).
Thus each prescribed pair violates (2).
This obstruction concerns the choice of denominators and holds in a group where the unrestricted equation already characterizes the division closure.

## Assessment history

### Decision common-positive-denominator

| Field | Value |
| --- | --- |
| date | 2026-11-25T09:38 |
| status | proved |
| reason | Each solution transports to a common positive denominator without changing its relations, and the torus examples prove the spectral and countable-menu obstructions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A common positive denominator and all quantified obstructions on the two-torus. |
| argument | [Argument](#argument) | Transport of both fractions, ranges and relation matrix, and the two residual tensor obstructions. |
| dependency | [Prescribed witness criterion](Yin_C_A0131_v4.md#statement) | The original quantified test and the matrix recovered from the witness ranges. |
| review | [Independent proof review](../audits/reviews/Yin_R_A0167_v1.md#positive-denominators) | Transport of both fractions, ranges and relation matrix, and the two residual tensor obstructions. |

## Current assessment

[Selected decision](#decision-common-positive-denominator)
