---
author: Yin
---

# Spectral concentration at one point for divergent cubic singular mass

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be one coordinate of a bounded normal generating tuple with actual starred conjugate variables in a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\).
Let \(N=W^*(X_j:j\ne i)\), let \(\mathcal G\subset N\) be a fixed family, and write \(K=\sigma(Z)\).
For \(b\in\mathcal G\) write \(T_b=Z-b=U_b P_b\), \(P_b=|T_b|\), and put
\[
 F(s)=\sup_{b\in\mathcal G}\tau(1_{[0,s]}(P_b)),\qquad
 h_s(v)=\frac{s^2}{v^2+s^2},\qquad a_s(v)=\frac{sv}{v^2+s^2}.
\]
Use the empty supremum zero.
The shifted polar \(U_b\) is unitary by the [singular-law theorem](Yin_C_F0229_v1.md#statement).
For \(s>0\) and \(b\in\mathcal G\) put \(H=\tau(h_s(P_b))>0\), \(V=U_b a_s(P_b)\) and \(h'=U_bh_s(P_b)U_b^*\).
Define two probabilities and a complex measure on \(K\) by their values on bounded Borel \(c\):
\[
 R(c)=H^{-1}\tau(c(Z)h_s(P_b)),\qquad
 L(c)=H^{-1}\tau(c(Z)h'),\qquad
 G(c)=H^{-1}\tau(c(Z)V).
\]
If \(\int_0^\infty F(s)^3\,ds/s^3=\infty\), there are \(s_n\downarrow0\), \(b_n\in\mathcal G\), a point \(z_0\in K\) and a complex number \(q\) such that
\[
 \tau(1_{[0,s_n]}(P_{b_n}))\ge F(s_n)/2,\qquad
 R_n\rightharpoonup\delta_{z_0},\qquad L_n\rightharpoonup\delta_{z_0},
 \qquad G_n\rightharpoonup q\delta_{z_0}.                                \tag{1}
\]
All three limits are weak against continuous functions on the fixed spectrum, and \(\sup_n|G_n|(K)<\infty\).
The corresponding trace-normalized right and left singular projections \(1_{[0,s_n]}(P_{b_n})\) and \(U_{b_n}1_{[0,s_n]}(P_{b_n})U_{b_n}^*\), used in place of the soft weights in \(R_n,L_n\), have the same two point-mass limits.
In particular their normalized spectral second moments of \(|Z-z_0|\) tend to zero.
The conclusion applies to a fixed shift whose singular law is the [critical radial power law](Yin_C_F0261_v2.md#endpoint-radial-law).
The law of the marginal \(Z\) itself remains diffuse.
The result constrains the normalized spectral states at shrinking mass, and allows concentration at one marginal point.

## Argument

### Simultaneous choice of scales

Set \(h=h_s(P_b)\), \(A=\tau(a_s(P_b))\), and write \(D_\eta(s)=\int_s^\infty H_\eta(F(t))\,dt/t^2\), where \(H_\eta(x)=\int_0^x\mu_u(|\eta|)\,du\) and \(\mu_u\) denotes decreasing spectral rearrangement in the probability trace.
For every fixed \(\eta\in L^2(M)\), the [rearrangement estimate](Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) gives
\[
                  |\langle\eta,V\rangle|,\ |\langle\eta,h\rangle|
                       \le sD_\eta(s).                                   \tag{2}
\]
Indeed both \(a_s(v)/s\) and \(h_s(v)/s\) are bounded by \(\min(1/s,1/v)\) for \(v>0\), including the second bound since \(sv\le s^2+v^2\).
Their singular-value tails at level \(y\) are at most \(F(1/y)\).
The proof of the cited estimate uses just these inequalities for the tested operator and square integrability of the fixed vector.

Take \(I_\varepsilon=\int_\varepsilon^\infty F(s)^3ds/s^3\to\infty\).
On \([\varepsilon,\infty)\) use the probability measure proportional to \(F(s)^3ds/s^3\) when \(I_\varepsilon>0\), with any ratio below defined as zero at \(F(s)=0\).
For each fixed \(\eta\), the mean of \((s^2D_\eta(s)/F(s)^2)^{3/2}\) tends to zero.
Indeed its numerator before dividing by \(I_\varepsilon\) is exactly \(\int_\varepsilon^\infty D_\eta(s)^{3/2}ds\).
If \(F=0\) on part of the interval the numerator is bounded above by that integral.
Minkowski after \(t=sy\) gives
\[
 \|s^{2/3}D_\eta(s)\|_{L^{3/2}(ds/s,\ s\ge\varepsilon)}
 \le \tfrac32
 \|s^{-1/3}H_\eta(F(s))\|_{L^{3/2}(ds/s,\ s\ge\varepsilon)}.
\]
The power \(3/2\) of the last norm is at most \(3(2I_\varepsilon/3)^{1/4}\sqrt2\,\|\eta\|_2^{3/2}\) by the [superlevel and Hardy estimate](Yin_C_F0261_v1.md#a-nonlinear-integral-estimate).
Thus the claimed mean is \(O_\eta(I_\varepsilon^{-3/4})\).

For \(J(s)=\int_1^\infty F(su)du/u^2\), one has \(A\le J(s)\) and \(H\le J(s)\).
Indeed each scalar integrand is bounded by \(\min(1,s/v)=\int_1^\infty 1_{\{v\le su\}}du/u^2\).
Minkowski gives
\[
          \|s^{-2/3}J(s)\|_{L^3(ds/s,\ s\ge\varepsilon)}
                    \le 3 I_\varepsilon^{1/3},
\]
as \(\int_1^\infty u^{2/3}du/u^2=3\).
Consequently \(J(s)/F(s)\le 6\) except on a set of probability at most \(1/8\).
Let \((\eta_j)\) be any countable collection of fixed Hilbert vectors.
For each \(n\) take \(\varepsilon\) sufficiently small that, except on a set of probability less than \(1/2\), \(s<1/n\) and \(s^2D_{\eta_j}(s)/F(s)^2<1/n\) for all \(j\le n\).
Here the numerator of the mass on \(s\ge1/n\) stays finite, and Markov's inequality applies to the finitely many preceding means.
Select \(s=s_n\) satisfying all these bounds and \(J(s)\le6F(s)\), with \(F(s)>0\).
Pass to a decreasing subsequence if needed.
Choose \(b_n\) with \(t_n=\tau(1_{[0,s_n]}(P_{b_n}))\ge F(s_n)/2\).
Since \(h_s\ge1/2\) on \([0,s]\), one has \(F/4\le H\le6F\) and \(|G|(K)\le A/H\le24\).
Equation (2) proves simultaneously
\[
             (s/H^2)\langle\eta_j,V\rangle,\quad
             (s/H^2)\langle\eta_j,h\rangle\ \longrightarrow\ 0
                            \qquad\text{for every fixed }j.               \tag{3}
\]

### Two tensor identities off the collision diagonal

Identify outer derivatives \(\delta=\delta_i\) with \(L^2(M\bar\otimes M^{\rm op})\) by \(\Phi(x\otimes y)=x\otimes y^{\rm op}\).
In this convention the derivative at \(T_b\) is \(1\), and the derivative at \(T_b^*\) is the fixed marginal unitary \(k(z,w)=(\bar z-\bar w)/(z-w)\) in the product spectral algebra of \(Z\).
The [shifted graph and resolvent calculation](Yin_C_F0229_v1.md#argument) puts \(h,V\) in the original closed derivative domain and gives
\[
       s\Phi(\bar\delta V)=h'\otimes h^{\rm op}
                                   -(V\otimes V^{\rm op})k,\qquad
       s\Phi(\bar\delta h)=-(h\otimes V^{\rm op})k
                                   - V^*\otimes h^{\rm op}.              \tag{4}
\]
For the second formula differentiate \(s^2(T_b^*T_b+s^2)^{-1}\) by the inverse product rule, using \(T_b h=sV\) and \(hT_b^*=sV^*\).
All scalar tests below come from the *same* original derivation.

Choose the countable tests in (3) to include the adjoints \(\delta^*\Phi^{-1}((c(Z)\otimes d(Z)^{\rm op})^*)\) for all pairs of monomials \(c,d\) in the spectral coordinate and its conjugate.
They exist by the [actual tensor adjoint domain](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability).
The choice of adjoints makes pairing against a derivative equal to tracing its product with \(c(Z)\otimes d(Z)^{\rm op}\).
Multiplying (4) by these fixed tests and tracing shows that the complex measures
\[
        L_n\otimes R_n-k(G_n\otimes G_n),\qquad
        k(R_n\otimes G_n)+\overline{G_n}\otimes R_n                    \tag{5}
\]
converge weakly to zero on \(K^2\).
Indeed tensor traces of separated spectral symbols factor into products of the indicated one-leg measures by cyclicity, also on the opposite leg.
At a fixed \(n\) each measure is absolutely continuous relative to the marginal trace law on its leg.
It follows by approximation by bounded simple functions that the inserted \(k\) acts as the recorded measurable product multiplier, with arbitrary diagonal value since the marginal trace law is diffuse.
The variation of (5) is uniformly bounded by the previous norm bounds, so uniform polynomial density on \(K^2\) gives weak convergence against every continuous test from (3).

Compactness and metrizability give a subsequence of \(R_n,L_n,G_n\) with weak limits \(R,L,G\) on \(K\).
Products of the separate measures converge on continuous tests by their uniform variation bounds and uniform density of finite sums of separated continuous functions.
On the open complement of the diagonal \(k\) is continuous, symmetric and of modulus one.
Testing (5) on compactly supported continuous functions there gives exact equalities of restricted measures
\[
       L\otimes R=k(G\otimes G),\qquad
       k(R\otimes G)=-\overline G\otimes R
                            \quad\text{off }z=w .                        \tag{6}
\]
No claim about convergence through the discontinuity of \(k\) on the diagonal is required.

### The common limiting point

The first right side of (6) is symmetric under exchanging the two legs.
Hence \(L\otimes R=R\otimes L\) off the diagonal, and on the diagonal these two measures agree because the exchanging map fixes every point there.
Taking their first marginal gives \(L=R=:\sigma\).
Suppose that two disjoint Borel sets \(I,J\) have positive \(\sigma\)-mass.
On \(I\times J\) the first identity and \(|k|=1\) give \(\sigma|_I\otimes\sigma|_J=|G||_I\otimes|G||_J\).
Taking marginals proves equivalence of \(\sigma\) and \(|G|\) separately on both sets.
Write \(q(z)=dG/d\sigma\) on their union.
On \(I\times J\), for \(\sigma^2\)-almost every \((z,w)\), the two equalities (6) now give
\[
           k(z,w)q(z)q(w)=1,\qquad k(z,w)q(w)=-\overline{q(z)}.
\]
Multiplication of the second equality by \(q(z)\) contradicts the first since \(|q(z)|^2\ge0\).
A probability whose support has two different points has two such disjoint neighborhoods, so \(\sigma=\delta_{z_0}\).
The second identity of (6) on \(\{z_0\}\times(K\setminus\{z_0\})\) then gives \(G|_{K\setminus\{z_0\}}=0\).
This proves (1).

Finally \(e_n=1_{[0,s_n]}(P_{b_n})\le 2h_{s_n}(P_{b_n})\).
The positive spectral measures normalized by \(\tau(e_n)=t_n\) are dominated by \((2H_n/t_n)R_n\) and \((2H_n/t_n)L_n\) on their respective legs, with \(2H_n/t_n\le24\).
They are probabilities, so concentration of the two dominating probabilities at \(z_0\) gives the same limiting point for both hard cutoffs.
Testing with the continuous function \(|z-z_0|^2\) gives the claimed second moments.
At the scalar critical radial law the singleton envelope is \(F(s)=s^{2/3}\) for \(0<s<1\), and its cubic integral diverges.
Thus any actual realization of that law must satisfy the concentration conclusion even without an assumed phase bound.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:33 |
| status | open |
| reason | Fix the joint spectral concentration requirement for divergent cubic singular mass and the two independent original derivative tests for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Divergent envelopes for fixed or varying shifts force a common spectral point in both soft and hard normalized marginal states. |
| argument | [Argument](#argument) | Simultaneous scale selection, trace formula for the positive diagonal resolvent block, off-diagonal product identities and point-mass rigidity. |
| dependency | [Singular laws and resolvent graphs](Yin_C_F0229_v1.md#argument) | Zero kernels, unitary polar decomposition, shifted starred graph and inverse differentiation in the original closed graph. |
| dependency | [Actual tensor adjoint domain](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Fixed algebraic tensors of marginal polynomials lie in the actual adjoint domain; the marginal law is diffuse and the starred symbol is the unitary off-diagonal secant phase. |
| dependency | [Hilbert-vector rearrangement](Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) | Uniform singular-value layer bound for both scaled resolvents against each fixed square-integrable vector. |
| dependency | [Truncated nonlinear estimate](Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) | The superlevel integration and Hardy bound for the same nondecreasing envelope on every truncated interval. |
| dependency | [Endpoint radial law](Yin_C_F0261_v2.md#endpoint-radial-law) | Its singular distribution, used only in the fixed-shift application. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:46 |
| status | proved |
| reason | Independent review establishes common point-mass localization along any divergent cubic envelope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Divergent envelopes for fixed or varying shifts force a common spectral point in both soft and hard normalized marginal states. |
| argument | [Argument](#argument) | Simultaneous scale selection, trace formula for the positive diagonal resolvent block, off-diagonal product identities and point-mass rigidity. |
| dependency | [Singular laws and resolvent graphs](Yin_C_F0229_v1.md#argument) | Zero kernels, unitary polar decomposition, shifted starred graph and inverse differentiation in the original closed graph. |
| dependency | [Actual tensor adjoint domain](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Fixed algebraic tensors of marginal polynomials lie in the actual adjoint domain; the marginal law is diffuse and the starred symbol is the unitary off-diagonal secant phase. |
| dependency | [Hilbert-vector rearrangement](Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) | Uniform singular-value layer bound for both scaled resolvents against each fixed square-integrable vector. |
| dependency | [Truncated nonlinear estimate](Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) | The superlevel integration and Hardy bound for the same nondecreasing envelope on every truncated interval. |
| dependency | [Endpoint radial law](Yin_C_F0261_v2.md#endpoint-radial-law) | Its singular distribution, used only in the fixed-shift application. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0278_v1.md#finding) | Scale selection, both resolvent identities, off-diagonal product measures and hard-cutoff localization. |
