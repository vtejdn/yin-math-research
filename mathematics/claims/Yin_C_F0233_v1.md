---
author: Yin
---

# Packing of singular projections with locally scalar or finite-spectrum shifts

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=X_i\) be a coordinate of a finite normal generating tuple in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace and the [actual ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Write \(B=W^*(X)\), \(N=W^*(X_j:j\ne i)\), and \(\zeta=\mathbb E_B(\delta_i^*(1\otimes1))\).
There is a positive density \(d\in L^1(B)\) with \(\tau(d)=1\) such that the following estimates hold simultaneously.
Set \(K=(1024/27)(12\|\zeta\|_2)^2\).

1. For every \(0\le a\le1\) in \(M\) with \(t=\tau(a)>0\), and every complex \(\lambda\),
   \[
       \frac{t^4}{\|(X-\lambda)a^{1/2}\|_2^2}\le K\,\tau(da).
       \tag{1}
   \]
   In particular the left sides are summable with sum at most \(K\) whenever \(\sum a\le1\), with separate centers allowed.
   For any such single test with \(\|(X-\lambda)a^{1/2}\|_2\le R\sqrt t\), one has \(t^3/R^2\le K\tau(da)\).
   Uniformly over these tests, \(t^3/R^2\to0\) as \(R\downarrow0\).
2. Let \(e_j\) be mutually orthogonal nonzero projections in \(M\), \(t_j=\tau(e_j)\), and let \(b_j\in N\) and \(r_j>0\) satisfy \(\|(X-b_j)e_j\|_2\le r_j\sqrt{t_j}\).
   This includes the [singular-projection tests](Yin_C_F0211_v1.md#statement).
   Choose any normal finite-spectrum \(c_j=\sum_l\lambda_{jl}q_{jl}\) in \(N\) with a finite projection partition \(\sum_l q_{jl}=1\).
   Put
   \[
   \begin{split}
       t_{jl}&=\tau(e_jq_{jl}),\qquad m_j=\frac{t_j^2}{\sum_l t_{jl}^2},\\
       R_j&=r_j+\frac{\|(b_j-c_j)e_j\|_2+\|[c_j,e_j]\|_2}{\sqrt{t_j}}.
   \end{split}
   \]
   Then
   \[
          \frac{t_j^3}{m_j^2 R_j^2}\le K\tau(de_j),\qquad
          \sum_j\frac{t_j^3}{m_j^2 R_j^2}\le K.                      \tag{2}
   \]
   Thus the original packing sum \(\sum_j t_j^3/r_j^2\) is bounded by \(K L^2\) on every family admitting choices with \(\sup_j m_j R_j/r_j\le L\).
   This condition includes shift tests commuting with their normal finite-spectrum shifts when the numbers of spectral values on the tested projections are uniformly bounded.
   It also applies when the shifts themselves are nonnormal if they have the stated approximations.

No property of the omitted algebra beyond the stated approximation is needed in (2).
The density is fixed by the single marginal and works also when the \(e_j\) lie outside \(N\).

## Argument

### A scalar commutator and positive weights in the ambient algebra

The [normal phase formula](Yin_C_F0076_v1.md#statement), part 1, gives a diffuse trace law for \(X\).
The distinguished derivation on polynomials in \(X,X^*\) takes values in \(L^2(B)\otimes_2 L^2(B)\) by the formula for the starred generator and the product rule.
Restriction of the vacuum identity gives the actual scalar vacuum \(\zeta\).
Denote by \(c\) the [canonical column constant](Yin_C_F0208_v1.md#statement) for this one-coordinate system.
Adjoin two free Haar unitaries as in that theorem.
The enlarged system has the same vacuum \(\zeta\) in its old coordinate and consists of three freely independent normal coordinates.
The [free normal estimate](Yin_C_F0162_v1.md#statement), part B, gives the canonical full-domain dual of that coordinate with operator-norm-to-Hilbert norm at most \(3\|\zeta\|_2\).
Thus the enlarged bounded-dual optimum is at most \(3\|\zeta\|_2\), and (2) of C_F0208 gives \(c\le12\|\zeta\|_2\).

Apply the [optimal-density commutator](Yin_C_F0211_v1.md#statement), equation (2), to the scalar algebra \(B\).
It gives \(d\) as above, with \(d^{-1}\in L^1(B)\), and an operator \(T\) on \(L^2(B)\) of norm \(c\) satisfying
\[
          [T,L_X]=|1\rangle\langle d^{-1/2}|.
\]
Fix \(a,\lambda\) as in (1), let \(w=\mathbb E_B a\), and write \(\sigma^2=\|(X-\lambda)a^{1/2}\|_2^2/t\).
The scalar weight \(0\le w\le1\) has integral \(t\), and \(t\sigma^2=\tau(w|X-\lambda|^2)\) by traciality and the expectation identity.
Diffuseness implies \(\sigma>0\).
Set \(h=w1_{[0,2\sigma]}(|X-\lambda|)\) and \(t'=\tau(h)\).
Markov's inequality against \(w\,d\tau\) gives \(t'\ge3t/4\).
Compress the commutator by \(L_{\sqrt h}\) on both sides.
In each term of the compressed commutator replace \(X\) by \(X-\lambda\) and use \(\|(X-\lambda)\sqrt h\|\le2\sigma\) and \(\|\sqrt h\|\le1\).
The norm of the compressed rank-one operator therefore gives
\[
    \sqrt{t'}\,\|\sqrt h\,d^{-1/2}\|_2\le4c\sigma,\qquad
    t'\le\|\sqrt h\,d^{-1/2}\|_2\,\|\sqrt h\,d^{1/2}\|_2 .
\]
The second inequality is Cauchy–Schwarz in the abelian algebra \(B\).
Combining the inequalities gives
\[
      (3t/4)^3\le16c^2\sigma^2\tau(dh)
              \le16c^2\sigma^2\tau(da).
\]
For the last step use \(h\le w\) and \(\tau(dw)=\tau(da)\), first with bounded truncations of \(d\), then by monotone convergence of positive functionals.
This proves (1) with the indicated \(K\).
If \(\sigma\le R\), then \(t^3\le KR^2\), since \(\tau(da)\le1\).
As \(R\) tends to zero, \(t\) therefore tends to zero uniformly.
For every \(C>0\), \(\tau(da)\le C t+\tau((d-C)_+)\), so the right side of (1) tends to zero uniformly as asserted.

### Spectral partitions of the approximating shifts

For one index omit \(j\) and apply (1) to \(a_l=e q_l e\), whose trace is \(t_l\) and whose sum is \(e\).
Set \(v_l=\|(X-\lambda_l)e q_l\|_2\).
Traciality and \(q_l^2=q_l\) give \(v_l^2=\|(X-\lambda_l)a_l^{1/2}\|_2^2\).
Ignore zero-trace terms, for which \(a_l=e q_l=0\).
Cauchy–Schwarz gives
\[
       \frac{(\sum_l t_l^2)^2}{\sum_l v_l^2}
               \le \sum_l\frac{t_l^4}{v_l^2}\le K\tau(de).
\]
The identity
\[
 (X-\lambda_l)e q_l=(X-b)e q_l+(b-c)e q_l+[c,e]q_l
\]
uses only \(cq_l=\lambda_l q_l\).
Taking norms in the finite direct sum of Hilbert spaces and using \(\sum_l\|zq_l\|_2^2=\|z\|_2^2\) gives
\[
       (\sum_l v_l^2)^{1/2}\le r\sqrt t+\|(b-c)e\|_2+\|[c,e]\|_2
                         =R\sqrt t .
\]
As \(\sum_l t_l^2=t^2/m\), the individual bound in (2) follows.
Sum it using orthogonality and the normalization of \(d\).
If \(b=c\) commutes with \(e\), then \(R=r\) and Cauchy–Schwarz gives \(m\le\#\{l:t_l>0\}\).
All finite-family estimates pass to countable families by partial sums.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:28 |
| status | open |
| reason | The marginal density applied to positive ambient weights and the resulting packing bound for finite-spectrum approximations are fixed for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous weighted scalar bounds, their uniform small-radius limit and singular-projection packing with local finite-spectrum approximations. |
| argument | [Argument](#argument) | Free enlargement supplies a scalar bounded commutator, weighted compression gives one density, and spectral partitions control the original projection tests. |
| dependency | [Normal coordinate phases](Yin_C_F0076_v1.md#statement) | Part 1, diffuseness and the marginal values of the actual starred derivation. |
| dependency | [Two-Haar column criterion](Yin_C_F0208_v1.md#statement) | The old vacuum in the free enlargement and its lower bound on enlarged bounded-dual cost in terms of the original column cost. |
| dependency | [Free normal contraction estimate](Yin_C_F0162_v1.md#statement) | Part B, (S5) and (S6) for the enlarged freely independent tuple and its old vacuum. |
| dependency | [Optimal scalar density](Yin_C_F0211_v1.md#statement) | Existence and attainment in (2), faithfulness, inverse integrability and the weighted rank-one identity on the scalar Hilbert space. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:32 |
| status | proved |
| reason | Independent review verifies the scalar density, its use for noncommuting ambient weights and the spectral partition that bounds the original packing sum. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous weighted scalar bounds, their uniform small-radius limit and singular-projection packing with local finite-spectrum approximations. |
| argument | [Argument](#argument) | Free enlargement supplies a scalar bounded commutator, weighted compression gives one density, and spectral partitions control the original projection tests. |
| dependency | [Normal coordinate phases](Yin_C_F0076_v1.md#statement) | Part 1, diffuseness and the marginal values of the actual starred derivation. |
| dependency | [Two-Haar column criterion](Yin_C_F0208_v1.md#statement) | The old vacuum in the free enlargement and its lower bound on enlarged bounded-dual cost in terms of the original column cost. |
| dependency | [Free normal contraction estimate](Yin_C_F0162_v1.md#statement) | Part B, (S5) and (S6) for the enlarged freely independent tuple and its old vacuum. |
| dependency | [Optimal scalar density](Yin_C_F0211_v1.md#statement) | Existence and attainment in (2), faithfulness, inverse integrability and the weighted rank-one identity on the scalar Hilbert space. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0242_v1.md#whole-proof-finding) | Both parts, finite and countable families, the effective number of spectral values, the commutator error and the small-radius limit. |
