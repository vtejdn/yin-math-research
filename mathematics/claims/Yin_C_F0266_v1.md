---
author: Yin
---

# Adjoint isometry at a real coordinate and the exact scalar class of column weights

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a bounded normal generating tuple with actual starred conjugate variables in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Suppose the distinguished coordinate \(x=X_i\) is selfadjoint.
Put \(P=\mathbb C\langle X,X^*\rangle\), \(N=W^*(X_j:j\ne i)\), \(B=W^*(x)\), \(\Omega=1\) and \(H=L^2(M,\tau)\), with the inner product linear in the second variable.
On \(P\) put \(E=(\mathrm{id}\otimes\tau)\delta_i\), \(\xi=\delta_i^*(1\otimes1)\) and \(T=E^*|_P\).
There is a unique \(w\in L^1(M)_+\) such that for every \(p\in P\)
\[
                \|Tp\|_2^2=\tau(wp^*p).
\]
It has full support, \(\tau(w)=\|\xi\|_2^2\) and \(\tau(w^{-1})\le4\inf_{\lambda\in\mathbb R}\|x-\lambda1\|^2\).
There is a unique isometry \(V:H\to H\) with \(V(p\sqrt w)=Tp\).
It satisfies \(V\sqrt w=\xi\), \(V^*L^2(N)=0\), \(V^*L_{X_j}V=L_{X_j}\) and
\[
       [V,L_{X_j}]=-\delta_{ij}|\Omega\rangle\langle w^{-1/2}|.
                                                               \tag{1}
\]
Here \(L_y\) is left multiplication.
In particular \(2(w+\xi^2)\) is an unnormalized simultaneous weight for every finite column of \(E\).

The law of \(x\) has a compactly supported density \(\rho\in L^3(\mathbb R,dt)\).
Write \(a=\pi H_{\mathbb R}\rho\), where \(H_{\mathbb R}\) is the Hilbert transform with multiplier \(-i\,\operatorname{sgn}\), and identify \(\rho,a\) with functions of \(x\).
For trace-preserving conditional expectations, the two marginal densities are
\[
 \mathbb E_Nw=\mathbb E_N\xi^2,\qquad
 \mathbb E_Bw=\mathbb E_B\big((\xi-2a)^2\big)+a^2+\pi^2\rho^2.
                                                               \tag{2}
\]
When \(M=B\), let \(w_0=a^2+\pi^2\rho^2=w\).
For any positive integrable \(d\), let \(C(d)\) be the least constant in \(\|Ep\|_2\le C(d)\|p\sqrt d\|_2\) for scalar polynomials.
Then, with \(+\infty\) allowed and the ratio infinite on \(\{d=0,w_0>0\}\),
\[
        \operatorname*{ess\,sup}_{\mu}\frac{w_0}{d}
          \ \le\ C(d)^2\ \le\
               9\operatorname*{ess\,sup}_{\mu}\frac{w_0}{d},
               \qquad d\mu=\rho\,dt .                         \tag{3}
\]
The same constant works term by term on finite columns.
For a correlated tuple the lower bound still applies to the marginal tests with \(\mathbb E_B d\) in place of \(d\).

## Argument

### A normal density for the polarized energy

The [normal-coordinate formula](Yin_C_F0076_v1.md#statement) gives derivative zero on both symbols of every omitted generator.
At \(x=x^*\) it gives \(1\otimes1\).
Consequently the derivative is real, has algebraic tensor values and is coassociative on \(P\).
Indeed reality holds on the generators and propagates by the outer product rule.
The two algebraic triple derivatives agree on the generators, and the cross terms in the difference of their product rules cancel.
The [real coassociative identity and estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) now give \(\xi=\xi^*\), \(Tp=p\xi-Ep\),
\[
              \|Tp\|^2=\langle\xi,T(p^*p)\rangle,\qquad
              \|Tp\|_2\le\|\xi\|_2\|p\|.
\]
The core adjoint formula here also follows by pairing the derivative of \(p^*q\) with \(1\otimes1\) and using reality.
For \(q\in P\), \(\langle q,Tp\rangle=\langle Eq,p\rangle\) is the restriction of a normal functional on \(M\).
Choose \(q_n\in P\) tending to \(\xi\) in \(H\).
The resulting normal functionals are Cauchy on \(M\) in predual norm, since their differences on the unit ball of \(P\) are bounded by \(\|\xi\|_2\|q_n-q_m\|_2\), and that ball is strongly dense in the unit ball of \(M\) by Kaplansky density and norm approximation.
Their limit \(\ell\) agrees on \(P\) with \(p\mapsto\langle\xi,Tp\rangle\).
It is positive by the square identity, approximating square roots strongly-star by uniformly bounded polynomials.
The tracial predual identifies it with a unique \(w\in L^1(M)_+\).
Evaluation at \(1\) gives its mass.
Polarizing the square identity also proves uniqueness among densities representing the squared norms.

The commutator identity \(T(xp)-xTp=-\tau(p)\Omega\) implies
\[
 |\tau(p)|\le 2\|x-\lambda1\|\,\|p\sqrt w\|_2
\]
for real \(\lambda\), by the square identity for \((x-\lambda)p\) and for \(p\).
Strong-star bounded approximation gives this inequality for \(p\in M\).
Test with \((w+\varepsilon1)^{-1}\) and use \(\tau(w(w+\varepsilon1)^{-2})\le\tau((w+\varepsilon1)^{-1})\).
Monotone convergence gives the inverse bound and full support.
As in the [weighted commutator argument](Yin_C_F0211_v1.md#faithfulness-inverse-integrability-and-the-bounded-implementer), truncation on \(1_{[1/m,m]}(w)\) and strong density give density of \(P\sqrt w\) in \(H\) and \(\langle w^{-1/2},p\sqrt w\rangle=\tau(p)\).
Hence the core isometry has the unique asserted extension, and its generator commutators give (1).
For omitted polynomials \(q\), \(Eq=0\) implies \(\langle q,Tp\rangle=0\) for every \(p\).
Thus \(V^*L^2(N)=0\), in particular \(V^*\Omega=0\); multiplying (1) by \(V^*\) on the left gives the compressions.
For \(p\in P\), \(Ep=p\xi-V(p\sqrt w)\) proves \(\|Ep\|_2^2\le2\tau((\xi^2+w)p^*p)\).
For omitted polynomials \(q\), \(Tq=q\xi\).
The two normal functionals defined by \(w,\xi^2\) therefore agree on all \(q^*q\), and their restrictions to \(N\) coincide.

### Resolvents and the conditional variance

The projection \(\xi_B=\mathbb E_B\xi\) is the actual scalar vacuum by testing scalar polynomials.
The [geometric scalar criterion](Yin_C_F0255_v1.md#statement) gives \(\int(M_1\mu)^2\,d\mu<\infty\), where \(M_1\mu(t)=\sup_{r>0}\mu((t-r,t+r))/r\) on the real line.
This implies absolute continuity directly.
On \(\{M_1\mu\le k\}\), each interval of length \(s\) meeting this set has restricted mass at most \(2ks\), by centering a ball of radius \(2s\) at a point in the set.
Covering Lebesgue null sets by intervals and letting \(k\) increase gives \(\mu=\rho\,dt\).
Lebesgue differentiation gives \(2\rho\le M_1\mu\) almost everywhere for \(\mu\), so \(\rho\in L^3(dt)\).
The [scalar Hilbert transform realization](../audits/literature/Voi98/Yin_U002.md#proposition-35-scalar-hilbert-transform-realization) gives \(\xi_B=2a\) and \(F(t+i\varepsilon)\to a-i\pi\rho\) in \(L^3(dt)\) for the Stieltjes transform \(F(z)=\int(z-u)^{-1}\,d\mu(u)\).
The imaginary part uses the Poisson approximate identity with mass \(\pi\).

For \(p_z=(z-x)^{-1}\), \(z\notin\mathbb R\), its scalar divided difference is \(p_z\otimes p_z\).
The formulas on \(P\) transfer by uniformly approximating the derivative on the real spectral interval by polynomials, integrating with the correct constant and using uniform divided-difference convergence.
Consequently \(E p_z=F(z)p_z\), \(\tau(p_z\xi)=F(z)^2\) by the vacuum identity, and
\[
                  \tau(wp_z)=\tau(\xi^2p_z)-F(z)^3 .
\]
For the last equality use \(\ell(p_z)=\langle\xi,p_z\xi-F(z)p_z\rangle\).
The negative imaginary part divided by \(\pi\) of each measure transform converges weakly to that measure.
The cubes converge in \(L^1(dt)\) by the stated \(L^3\) convergence, and \(-\pi^{-1}\operatorname{Im}(a-i\pi\rho)^3=3a^2\rho-\pi^2\rho^3\).
It follows that \(\mathbb E_Bw=\mathbb E_B\xi^2-3a^2+\pi^2\rho^2\) for \(\mu\)-almost every real point.
Since \(\xi_B=2a\), the \(L^1\) bimodule identity for the conditional second moment gives (2), with unbounded factors justified by \(L^2\) truncation.

### All scalar dominating densities

In the scalar algebra (2) gives \(w=w_0\) and \(\xi^2\le4w_0\).
The triangle inequality for \(Ep=p\xi-Tp\) proves the upper bound in (3).
For a compactly supported smooth function \(\phi\) on the real line, use \(f_k(t)=e^{ikt}\phi(t)\).
Approximation in \(C^1\) on the spectral interval again transfers polynomial domination to each \(f_k\).
For every smooth \(f\) there the divided-difference formula gives
\[
             Ef=fa-\pi H_{\mathbb R}(f\rho)
                       \qquad\text{in }L^2(\mu).
\]
Indeed, regularize the kernel \(1/(t-u)\) by \((t-u)/((t-u)^2+\varepsilon^2)\).
Its integral against \(f(t)-f(u)\) converges to the divided-difference integral by dominated convergence and the Lipschitz bound.
The two regularized Hilbert transforms converge in \(L^3(dt)\), hence in \(L^2(\mu)\) by Hölder.
For every \(g\in L^3(dt)\), \(e^{-ikt}H_{\mathbb R}(e^{ikt}g)\to-ig\) in \(L^3(dt)\) as \(k\to+\infty\).
First take a Schwartz function with compact Fourier support, on which the multiplier is eventually constant after the shift.
Such functions are dense by smoothing and frequency truncation, and modulation preserves the norm while the Hilbert transform is bounded on \(L^3\).
Apply this limit to \(g=\phi\rho\).
It gives \(e^{-ikt}Ef_k\to\phi(a+i\pi\rho)\) in \(L^2(\mu)\).
On the input side \(|f_k|=|\phi|\), so domination implies \(\int|\phi|^2w_0\,d\mu\le C(d)^2\int|\phi|^2d\,d\mu\).
Uniform approximation of square roots of positive continuous tests on the compact support gives \(w_0\le C(d)^2d\) almost everywhere, proving the lower bound.
For a mixed tuple the same tests are in the scalar core after approximation, \(E\) has precisely the same scalar divided-difference values there and the input sees \(\mathbb E_Bd\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:07 |
| status | open |
| reason | Fix the adjoint isometry, the two marginal formulas and the scalar domination criterion for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Real distinguished coordinate, rank-one commutators, conditional densities and all scalar domination weights. |
| argument | [Argument](#argument) | Normality of the energy, weighted isometry, scalar Stieltjes identity and high-frequency localization. |
| dependency | [Normal starred symbols](Yin_C_F0076_v1.md#statement) | Both omitted starred symbols vanish and the distinguished real symbol has derivative \(1\otimes1\). |
| dependency | [Real coassociative energy](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Core adjoint formula, exact square identity and operator-norm-to-Hilbert bound. |
| dependency | [Weighted commutator argument](Yin_C_F0211_v1.md#faithfulness-inverse-integrability-and-the-bounded-implementer) | Density of weighted core vectors and the pairing with the inverse square root after the inverse estimate. |
| dependency | [Geometric scalar criterion](Yin_C_F0255_v1.md#statement) | Finite integrated maximal linear density under the actual scalar vacuum hypothesis. |
| dependency | [Scalar Hilbert transform realization](../audits/literature/Voi98/Yin_U002.md#voi98-u002) | Hilbert multiplier, \(L^3\) boundedness, actual scalar vacuum and regularized boundary limits. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:12 |
| status | proved |
| reason | The independent review establishes the isometric representation, the two exact conditional densities and the scalar weight criterion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Real distinguished coordinate, rank-one commutators, conditional densities and all scalar domination weights. |
| argument | [Argument](#argument) | Normality of the energy, weighted isometry, scalar Stieltjes identity and high-frequency localization. |
| dependency | [Normal starred symbols](Yin_C_F0076_v1.md#statement) | Both omitted starred symbols vanish and the distinguished real symbol has derivative \(1\otimes1\). |
| dependency | [Real coassociative energy](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Core adjoint formula, exact square identity and operator-norm-to-Hilbert bound. |
| dependency | [Weighted commutator argument](Yin_C_F0211_v1.md#faithfulness-inverse-integrability-and-the-bounded-implementer) | Density of weighted core vectors and the pairing with the inverse square root after the inverse estimate. |
| dependency | [Geometric scalar criterion](Yin_C_F0255_v1.md#statement) | Finite integrated maximal linear density under the actual scalar vacuum hypothesis. |
| dependency | [Scalar Hilbert transform realization](../audits/literature/Voi98/Yin_U002.md#voi98-u002) | Hilbert multiplier, \(L^3\) boundedness, actual scalar vacuum and regularized boundary limits. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0275_v1.md#finding) | Whole fixed proof, including normality, the inverse bound, Stieltjes signs, high-frequency limit and infinite ratios. |
