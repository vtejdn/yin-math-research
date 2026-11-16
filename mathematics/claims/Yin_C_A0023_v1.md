---
author: Yin
---
# A rank bound for four cyclic cosets with a common pairwise intersection

## Statement

Let \(G\) be a torsion-free discrete group and \(H=\langle h\rangle\) an infinite cyclic subgroup.
Suppose
\[
 a=\sum_{i=1}^{4} f_i(h)x_i\in\mathbb C G
\]
has four distinct occupied right cosets \(Hx_i\), with all \(f_i\in\mathbb C[z,z^{-1}]\) nonzero.
Assume that the twelve double cosets \(Hx_ix_j^{-1}H\) for ordered pairs \(i\ne j\) are pairwise distinct.
Put \(H_i=x_i^{-1}Hx_i\), and assume that there is a subgroup \(J\) such that \(H_i\cap H_j=J\) for all \(i\ne j\).
Then the regular rank of \(a\), the canonical trace of its range projection, satisfies
\[
                                r(a)\ \ge\ \frac47 .
\]
The bound allows \(J=\{e\}\) and infinite cyclic \(J\) of different indices in the four cyclic groups.
It excludes this factor arrangement in a complementary half-rank zero product as considered in the [Atiyah investigation](../ledger/Yin_L_A0038_v1.md#normalization).

## Double-coset orthogonality

Work in the finite group von Neumann algebra \(\mathcal N(G)\) with trace \(\tau\) and use its affiliated algebra for invertible multipliers.
For a subgroup \(J\), denote the trace-preserving conditional expectation onto \(\mathcal N(J)\) by \(E_J\).
Take a bounded operator \(A=\sum_i g_i(h)x_i\) obtained from \(a\) by invertible left and right affiliated multipliers and satisfying \(\sum_i|g_i(z)|^2=1\) almost everywhere on the circle with probability Haar measure.
Put \(u_i=|g_i|^2\), \(T_i=x_i^{-1}u_i(h)x_i\) and \(C=\sum_i E_JT_i\).
The rank equals that of \(a\), since the two operators have isomorphic images on the regular affiliated module, whose dimension equals the trace of the Hilbert range projection.

In \(AA^*\) the diagonal sum is \(1\).
Each off-diagonal term \(g_i(h)x_ix_j^{-1}g_j(h)^*\) is supported in the corresponding double coset in \(L^2(G)\).
For bounded circle coefficients this follows by approximating them in \(L^2\) by uniformly bounded Fejér sums, as in the [double-coset moment calculation](../ledger/Yin_L_A0038_v1.md#exact-correction-for-repeated-double-cosets-and-nontrivial-intersections).
These twelve cosets are distinct and none is \(H\).
Thus \(\tau(AA^*)=1\), and tracial cyclicity gives the squared \(L^2\)-norm of the \(ij\)-term as \(\tau(T_i T_j)\).
For \(i\ne j\), the Fourier coefficients of \(T_i,T_j\) are supported respectively on \(H_i,H_j\), so their inner product is the inner product of the two restrictions to \(J\).
It follows that
\[
 \begin{aligned}
 \tau((AA^*)^2)
   &=1+\sum_{i\ne j}\tau((E_JT_i)(E_JT_j))\\
   &=1+\|C\|_2^2-\sum_i\|E_JT_i\|_2^2
     \ \le\ 1+\tfrac34\|C\|_2^2 .
 \end{aligned} \tag{1}
\]
The inequality uses \(\|\sum_i v_i\|_2^2\le4\sum_i\|v_i\|_2^2\).
Trace Cauchy–Schwarz against the range projection gives \(1\le r(a)\tau((AA^*)^2)\).

For the initial operator, multiply on the left by the inverse of \((\sum_i|f_i(h)|^2)^{1/2}\), which is an affiliated unit by the almost everywhere nonvanishing of each \(f_i\).
Its normalized coefficient intensities \(u_i\) are positive almost everywhere, sum to one, and satisfy \(\log u_i\in L^1\): \(-\log u_i\) is bounded above by \(\log\|\sum_j|f_j|^2\|_\infty-2\log|f_i|\), and a Laurent polynomial has only integrable logarithmic singularities on the circle.
If \(J\) is trivial, \(C=\sum_i\tau(T_i)1=1\) immediately, and (1) gives the result.

## Alternating normalization on the two circles

For infinite \(J=\langle k\rangle\), write \(x_i k x_i^{-1}=h^{m_i}\) with \(m_i\ne0\), and put \(\pi_i(z)=z^{m_i}\).
The left circle has coordinate \(z\) for the character of \(h\), and the right circle has coordinate \(\omega\) for the character of \(k\).
Both carry probability Haar measure.
For an intensity \(u_i\), the function for \(E_JT_i\) on the right circle is
\[
      (P_i u_i)(\omega)=\frac{1}{|m_i|}\sum_{z^{m_i}=\omega}u_i(z).
\]
Indeed \(x_i k x_i^{-1}=h^{m_i}\) identifies multiplication by a right-circle test function with its pullback by \(\pi_i\), and integration over fibers gives the conditional expectation.
Each power map sends Haar measure to Haar measure.

At a stage with \(\sum_i u_i=1\), set \(c=\sum_i P_i u_i\), the function for \(C\) in (1).
Define successively
\[
 v_i(z)=\frac{u_i(z)}{c(\pi_i(z))},\qquad
 b(z)=\sum_i v_i(z),\qquad
 u'_i(z)=\frac{v_i(z)}{b(z)} .
\]
The first update is right multiplication by \(c(k)^{-1/2}\), since \(x_i c(k)^{-1/2}x_i^{-1}=c(h^{m_i})^{-1/2}\).
The second is left multiplication by \(b(h)^{-1/2}\).
We have \(0<c\le4\) almost everywhere and \(\int c=1\).
Also \(c(\pi_i(z))\ge u_i(z)/|m_i|\) for almost every \(z\), so \(0<v_i\le |m_i|\) and \(1/4\le b\le\sum_i|m_i|\) almost everywhere.
The identity \(\sum_iP_i v_i=1\) gives \(\int b=1\), and \(\sum_i u'_i=1\).
The multipliers are well-defined affiliated units and the updated coefficients are bounded at each step.
In particular every row-normalized stage is an operator of the kind used in (1), with the same regular rank.

For positive edge densities \(d_1,\ldots,d_4\) of total mass \(\int\sum_i d_i=1\), use
\[
                 \mathcal E(d)=\sum_{i=1}^4\frac14
                         \int\log\frac{1/4}{d_i(z)}\,dz .
\]
This relative entropy is nonnegative by Jensen's inequality, and it is finite initially.
If \(\log u_i\in L^1\) at a row-normalized stage, the bounds \(c(\pi_i(z))\ge u_i(z)/|m_i|\) and \(c\le4\), together with Haar preservation, give \(\log c\in L^1\).
The bounds on \(b\) then give integrable logarithms for \(v_i,u'_i\).
Thus all the following integrals are finite at every stage.
The uniform reference densities \(1/4\) sum to one on both circles.
Consequently the two entropy decreases are exactly
\[
 \mathcal E(u)-\mathcal E(v)=-\int\log c(\omega)\,d\omega,\qquad
 \mathcal E(v)-\mathcal E(u')=-\int\log b(z)\,dz .
\]
Both are nonnegative since \(c,b\) integrate to one.
For the sequence \(c_n\) at successive row-normalized stages this proves \(\sum_n-\int\log c_n\le\mathcal E(u^{(0)})\).
On \(0<x\le4\) one has \(x-1-\log x\ge (x-1)^2/32\) by the lower bound \(1/16\) on the second derivative.
Because \(\int c_n=1\), this yields \(\|c_n-1\|_2\to0\), hence \(\|C_n\|_2^2\to1\).

Applying (1) at each of these stages and taking a limit on its numerical upper bound gives \(1\le(7/4)r(a)\).
The argument uses only the common subgroup and its four power maps and requires no character on \(G\).
For other four-coset configurations the off-diagonal terms may overlap, or different pairs may contribute through different intersection subgroups.

## Assessment history

### Decision balanced-fourth-moment

| Field | Value |
| --- | --- |
| date | 2026-11-17T00:05 |
| status | proved |
| reason | The independent review verified the argument under its stated hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The four-sevenths rank bound under the distinct double-coset and common-intersection hypotheses. |
| argument | [Proof](#double-coset-orthogonality) | Complete proof and the stated limitations for A0001. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0054_v1.md#whole-argument-finding) | Independent mathematical review of this fixed result. |

## Current assessment

[Selected decision](#decision-balanced-fourth-moment)
