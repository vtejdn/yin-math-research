---
author: Yin
---

# Conditional product densities and the concentration of highly correlated spectral tests

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \((Z,Y)\) be a bounded normal generating pair with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\).
Write \(B=W^*(Z)\), \(N=W^*(Y)\), and let \(\mu,\eta\) be the respective marginal laws.
Let \(\gamma(dy,dz)=\eta(dy)\nu_y(dz)=\mu(dz)\sigma_z(dy)\) be the spectral coupling determined by \(\tau(1_S(Y)1_F(Z))\).
Set \(\lambda=\eta\otimes\mu\), \(r=d\lambda/d\gamma\), \(K=\overline{\operatorname{span}NB}^{\,2}\), and \(\kappa=\xi_Z^*Z-Z\xi_Z^*\) for the actual distinguished vacuum \(\xi_Z\).
For probabilities \(\alpha,\beta\) put \(\chi^2(\alpha\mid\beta)=\int (d\alpha/d\beta-1)^2d\beta\) when \(\alpha\ll\beta\), and set it equal to infinity otherwise.

1. The row divergences \(g(y)=\chi^2(\mu\mid\nu_y)\) and column divergences \(h(z)=\chi^2(\eta\mid\sigma_z)\) are integrable, with
   \[
      \int_S g\,d\eta=\|P_K(1_S(Y)\kappa)\|_2^2,\qquad
      \int_F h\,d\mu=\|P_K(\kappa 1_F(Z))\|_2^2.                         \tag{1}
   \]
   In particular \(g\le\mathbb E_N(\kappa\kappa^*)\) and \(h\le\mathbb E_B(\kappa^*\kappa)\) almost everywhere.
   For almost every \(y\), \(g(y)\) is the least number \(G\) such that every bounded Borel scalar \(a\) satisfies
   \[
       |\mu(a)-\nu_y(a)|^2\le G\,\mathrm{Var}_{\nu_y}(a),
       \qquad \mathrm{Var}_{\nu}(a)=\nu(|a-\nu(a)|^2).                   \tag{2}
   \]
   The column statement holds with \(h\) and the two variables interchanged.
   If \(\gamma=f\lambda+\gamma_{\rm s}\) is its Lebesgue decomposition, the singular part has mass at most \(\chi^2(\lambda\mid\gamma)/(1+\chi^2(\lambda\mid\gamma))\).
   All assertions about the density permit a nonzero singular part.

2. For measurable spectral sets \(S,F\) write \(\alpha=\eta(S)\), \(\beta=\mu(F)\), \(t=\gamma(S\times F)\).
   If \(\alpha>0\), \(0<\beta<1\), one has \(0<t<\alpha\) and
   \[
             \frac{\alpha(t-\alpha\beta)^2}{t(\alpha-t)}
                     \le \int_S g\,d\eta .                                \tag{3}
   \]
   The corresponding column bound exchanges \(\alpha,\beta\) and uses \(\int_F h\,d\mu\) when \(\beta>0,\ 0<\alpha<1\).
   Thus the left sides of (3) sum to at most \(\chi^2(\lambda\mid\gamma)\) on disjoint \(S\)'s, for any choices of the \(F\)'s.
   If \(\alpha_n>0,\ \alpha_n\to0,\ \beta_n\to0,\ t_n/\alpha_n\to1\), then
   \[
                           \frac{\alpha_n-t_n}{\alpha_n^2}\to\infty.     \tag{4}
   \]

3. Suppose a sequence of centered selfadjoint unit vectors \(a_n\in L^2(B)\), \(b_n\in L^2(N)\) has \(\tau(a_n b_n)\to1\).
   For every \(L>0\), the variances of the spectral clips \(\mathrm{clip}_L(a_n)\), \(\mathrm{clip}_L(b_n)\) onto \([-L,L]\) tend to zero.
   Both sequences converge to zero in trace measure.
   In particular, for each fixed \(L>0\),
   \[
         \tau(|a_n|^2 1_{\{|a_n|>L\}})\to1,\qquad
         \tau(|b_n|^2 1_{\{|b_n|>L\}})\to1.                              \tag{5}
   \]
   This constrains every sequence approaching equality in the centered correlation bound, including in a pair whose maximal centered correlation equals one.

4. At the level of ordered probability data there are symmetric couplings of the diffuse uniform probability on \([0,1]\) with itself for which both row and column divergences are integrable and maximal centered correlation equals one.
   They can have either zero singular mass or positive diagonal mass.
   The construction tests exactly the simultaneous product-density estimates; the existence of a joint starred vacuum for a prescribed coupling involves further mixed-word conditions.

## Argument

### The exact row and column norms

The [product-density identity](Yin_C_F0279_v1.md#the-product-law-in-the-ordered-representation) identifies \(r-1\in L^2(\gamma)\) with \(P_K\kappa\in K\) under the isometry sending \(n(y)a(z)\) to \(n(Y)a(Z)\).
Disintegration of \(r\gamma=\lambda\) identifies \(r(y,\cdot)\) with \(d\mu/d\nu_y\) and \(r(\cdot,z)\) with \(d\eta/d\sigma_z\), simultaneously outside null sets in the respective marginals.
Indeed a countable uniformly dense set of continuous tests, including the constant, identifies each finite conditional measure.
The projection onto \(K\) commutes with left \(N\) and right \(B\), since the spanning subspace is invariant under those multipliers and their adjoints.
Multiplying \(r-1\) by the row or column indicator in the isometry and taking its squared norm gives (1).
Dropping the projection gives the upper bounds by conditional expectation.
Both integrals on the full spaces equal \(\chi^2(\lambda\mid\gamma)\).

On a fiber of finite divergence the difference of means of \(a\) equals \(\nu_y((r(y,\cdot)-1)(a-\nu_y(a)))\).
Cauchy–Schwarz gives (2), and centered bounded truncations of the real vector \(r(y,\cdot)-1\) converge to it in \(L^2(\nu_y)\).
Testing those truncations proves optimality, including the zero case.
The column proof uses the other disintegration.
In the Lebesgue decomposition, \(\lambda\ll\gamma\) gives \(f>0\) almost everywhere for \(\lambda\).
The density \(r\) vanishes on the singular part and equals \(1/f\) on the absolutely continuous part.
Hence \(1+\chi^2(\lambda\mid\gamma)=\int f^{-1}d\lambda\), while \(\int f\,d\lambda=1-\gamma_{\rm s}(\mathrm{whole})\).
Cauchy–Schwarz on \(\lambda\) gives the singular-mass bound.

### Leakage from a nearly saturated rectangle

Apply (2) to the indicator of \(F\), writing \(m(y)=\nu_y(F)\).
Since \(0<\beta<1\) and \(\mu\ll\nu_y\), \(0<m(y)<1\) almost everywhere.
Then
\[
       g(y)\ge\frac{(m(y)-\beta)^2}{m(y)(1-m(y))}
             =\frac{\beta^2}{m(y)}+\frac{(1-\beta)^2}{1-m(y)}-1 .
\]
The right side is convex in \(m(y)\).
Average with the normalized restriction of \(\eta\) to \(S\), under which \(m\) has mean \(t/\alpha\).
Jensen's inequality gives (3).
Summing over disjoint rows uses the nonnegativity of \(g\).
In the regime of (4), \(t_n/\alpha_n\to1\) and \((t_n-\alpha_n\beta_n)/\alpha_n\to1\).
Consequently the left side of (3) is asymptotic to \(\alpha_n^2/(\alpha_n-t_n)\).
The right side tends to zero by absolute continuity of the integral of \(g\).
Here \(\beta_n>0\) eventually because \(t_n>0\) and \(t_n\le\beta_n\).

### Centered tests at an angle tending to zero

The [actual normal liberation calculation](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) supplies the represented partial liberation derivation acting by \(a\otimes1-1\otimes a\) on the distinguished marginal and zero on the omitted one.
Its vacuum adjoint is \(Z^*\xi_Z-\xi_Z Z^*\), so the trace-pairing liberation gradient \(j\) is in \(L^2(M)\).
The [liberation moment identity and its extension to von Neumann closures](../audits/literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient) give, for bounded selfadjoint \(a\in B,\ b\in N\),
\[
          2|\tau(ab)-\tau(a)\tau(b)|=|\tau(j[a,b])|
                         \le\|j\|_2\|[a,b]\|_2.                         \tag{6}
\]
Indeed the two trace pairings on \(ab\) and \(ba\) are opposite, by the indicated product rule.
Bounded strong-star approximation in the two marginal algebras passes these trace pairings to arbitrary bounded marginal tests.

Since \(\|a_n-b_n\|_2^2=2-2\tau(a_n b_n)\), this difference tends to zero.
For \(A_n=\mathrm{clip}_L(a_n)\), \(D_n=\mathrm{clip}_L(b_n)\), one has \(\|A_n-D_n\|_2\le\|a_n-b_n\|_2\).
Indeed the scalar clips are 1-Lipschitz, and the squared norms are the integrals of squared differences against the ordered trace coupling of the two spectral variables, which also applies to \(L^2\) variables by truncation.
Therefore \(\|[A_n,D_n]\|_2=\|[A_n,D_n-A_n]\|_2\le2L\|D_n-A_n\|_2\to0\).
Equation (6) makes the covariance of the two clips tend to zero.
Subtracting that covariance from the variance of \(A_n\) amounts to pairing the centered \(A_n\) with the centered \(A_n-D_n\), of norm tending to zero.
The centered clips have uniformly bounded \(L^2\) norms; the same argument for \(D_n\) proves variance convergence for both.

Centering of the original variables gives \(|\tau(A_n)|\le\tau(|a_n|1_{\{|a_n|>L\}})\le1/L\), and likewise for \(D_n\).
For any \(\epsilon>0\) choose \(L>\max(\epsilon,2/\epsilon)\).
Then \(\{|a_n|>\epsilon\}=\{|A_n|>\epsilon\}\) and Chebyshev's inequality with \(|\tau(A_n)|<\epsilon/2\) gives trace tending to zero.
This proves convergence in measure for both variables.
For each fixed \(L\), the positive elements \(|a_n|^2 1_{\{|a_n|\le L\}}\) and \(|b_n|^2 1_{\{|b_n|\le L\}}\) are bounded and converge to zero in measure, hence also in \(L^1\).
Subtracting their traces from one gives (5).

### A symmetric coupling with maximal centered correlation one

Let \(m\) be Lebesgue probability on \([0,1]\) and partition this interval up to endpoints into \(I_n\), \(n\ge1\), of masses \(p_n=2^{-n}\).
Take \(e(x)=e_n=1/(n+1)\) on \(I_n\) and \(c=\int e\,dm>0\).
Let \(dm^2=dm(y)dm(z)\) and let \(\Delta_*m\) denote the diagonal probability measure.
For any \(0\le s\le1\) use the symmetric measure
\[
     d\gamma_s=
       \left[\frac{e(y)e(z)}c+(1-s)\sum_{n\ge1}
              \frac{1-e_n}{p_n}1_{I_n}(y)1_{I_n}(z)\right]dm^2
              +s\,\Delta_*\big((1-e)m\big).
\]
The first term from \(e(y)e(z)/c\) has row marginal \(e\,dm\); the two within-cell terms supply the remaining \((1-e)\,dm\).
Symmetry gives the other marginal.
Its absolutely continuous density \(f_s\ge e(y)e(z)/c>0\) satisfies
\[
       \int f_s^{-1}dm^2\le c\left(\sum_{n\ge1}p_n/e_n\right)^2<\infty .
\]
Thus \(dm^2/d\gamma_s\) is square integrable for either ordering, and the singular mass is \(s(1-c)\).
For \(t_n=\gamma_s(I_n\times I_n)\) one has exactly
\[
            t_n=p_n(1-e_n)+e_n^2 p_n^2/c .
\]
The covariance of the same cell indicator in the two coordinates, divided by its variance, is \((t_n-p_n^2)/(p_n(1-p_n))\to1\).
Cauchy–Schwarz bounds centered correlation by one, so the supremum equals one for each \(s\).
In particular these laws exhibit integrable reverse product densities without a strict angle between the two centered coordinate spaces.
The example concerns ordered marginals and their coupling.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:41 |
| status | open |
| reason | Fix the conditional norms, leakage bounds, concentration of nearly perfectly correlated tests and the gapless ordered-data construction for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact local product-density norms, spectral rectangle leakage, loss of bounded-amplitude energy at limiting correlation one, and an abstract symmetric probability example. |
| argument | [Argument](#argument) | Ordered projection and disintegration, Jensen's inequality, the clipped liberation pairing and all marginals and near-maximal tests of the explicit coupling. |
| dependency | [Product-density identity](Yin_C_F0279_v1.md#statement) | The product law has an \(L^2\) density represented by the projected vacuum commutator. |
| dependency | [Partial liberation from a normal vacuum](Yin_C_F0238_v1.md#statement) | Existence on the joint represented core and the Hilbert adjoint vacuum \(Z^*\xi_Z-\xi_Z Z^*\). |
| dependency | [Liberation gradient and angle identity](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | The liberation-derivation sign convention and the centered commutator identity on bounded marginal tests. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:52 |
| status | proved |
| reason | The independent review verifies the conditional divergences, leakage inequality, mass escape and ordered probability example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact local product-density norms, spectral rectangle leakage, loss of bounded-amplitude energy at limiting correlation one, and an abstract symmetric probability example. |
| argument | [Argument](#argument) | Ordered projection and disintegration, Jensen's inequality, the clipped liberation pairing and all marginals and near-maximal tests of the explicit coupling. |
| dependency | [Product-density identity](Yin_C_F0279_v1.md#statement) | The product law has an \(L^2\) density represented by the projected vacuum commutator. |
| dependency | [Partial liberation from a normal vacuum](Yin_C_F0238_v1.md#statement) | Existence on the joint represented core and the Hilbert adjoint vacuum \(Z^*\xi_Z-\xi_Z Z^*\). |
| dependency | [Liberation gradient and angle identity](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | The liberation-derivation sign convention and the centered commutator identity on bounded marginal tests. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0290_v1.md#finding) | Exact fiber norms, optimal variance constants, vanishing-mass limits, clipped liberation pairing and distinction between the measure model and full actuality. |
