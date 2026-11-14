---
author: Yin
---

# Marginal curvature defects and two-block output estimates for a correlated normal coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a bounded normal generating tuple with actual starred coordinate derivations in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, with \(1\otimes1\in\operatorname{Dom}\delta_j^*\) for every coordinate \(j\).
Fix a distinguished coordinate \(Z=X_i\), let \(B=W^*(Z)=L^\infty(\mu)\), and put \(N=W^*(X_j:j\ne i)\).
Write \(P=\mathbb C\langle X,X^*\rangle\), \(P_B=\mathbb C[Z,Z^*]\), \(E=(\mathrm{id}\otimes\tau)\delta_i\) on \(P\), \(T=E^*|_P\), \(\xi=\delta_i^*(1\otimes1)\), \(\xi_B=\mathbb E_B\xi\), and \(\eta=\xi-\xi_B\).
Inner products are linear in the second variable.
Let \(E_B,T_B\) denote the scalar right slice and its core adjoint for the law of \(Z\), distinct from the conditional expectation \(\mathbb E_B\).
Use the [scalar weight and curvature kernel](Yin_C_F0267_v1.md#statement)
\[
 W=\tfrac14|\xi_B|^2+\pi^2\theta^2+\tfrac12\int g(\cdot,w)\,d\mu(w),
 \qquad g(z,w)=\int\kappa(z,w,s)^2\,d\mu(s),
\]
where \(\theta\) is the ordinary linear density and \(\kappa\) is the reciprocal circumradius, zero on repeated or collinear triples.
Put \(v=\mathbb E_B(\eta\eta^*)\).

For each real \(f\in P_B\),
\[
 \operatorname{Re}\langle\xi,Tf\rangle=\int f(W+v)\,d\mu,\qquad
 \|Tf\|_2^2=\int f^2(W+v)\,d\mu-
       \tfrac14\iint g(z,w)(f(z)-f(w))^2\,d\mu(z)d\mu(w).              \tag{1}
\]
For the two tests \(f=\operatorname{Re} Z,\operatorname{Im} Z\), let \(D\) be the sum of their defects \(\operatorname{Re}\langle\xi,T(f^2)\rangle-\|Tf\|_2^2\).
With \(d=\operatorname{diam}(\operatorname{supp}\mu)>0\) and \(k(z,w)=(\bar z-\bar w)/(z-w)\) off the null diagonal,
\[
 D=\iiint \sin^2\angle(z-s,w-s)\,d\mu^3
 \ \ge\ \tfrac14\left(1-\left|\iint k\,d\mu^2\right|^2\right)
 \ \ge\ d^{-2}\inf_{\ell}\int\operatorname{dist}(z,\ell)^2\,d\mu(z),   \tag{2}
\]
where \(\ell\) ranges over affine lines.
The full-core equality \(\|Tp\|_2^2=\tau(hp^*p)\) for all \(p\in P\) with a single \(h\in L^1(M)_+\) holds exactly when the distinguished spectrum lies on an affine line, equivalently when \(D=0\).

For all \(p\in P\) the projected output satisfies
\[
         \mathbb E_B(Ep)=\overline E_B(\mathbb E_Bp)+\mathbb E_B(p\eta^*).
                                                                         \tag{3}
\]
Here the bar denotes the actual Hilbert-space closure of the scalar slice.
Consequently \(2((2+\sqrt 2)^2 W+\eta^*\eta)\) dominates this projected slice on every original column, in the sense that the squared norm for each input \(p\) is at most \(\tau(2((2+\sqrt 2)^2W+\eta^*\eta)p^*p)\).

Consider also \(K=\overline{\operatorname{span} NB}^{\,2}\subseteq L^2(M)\) with Hilbert projection \(P_K\).
Suppose for constants \(0<m\le1\le M_0<\infty\) the two-block coupling obeys
\[
       m\tau(n)1\le\mathbb E_B n\le M_0\tau(n)1
               \qquad(n\in N_+).                                         \tag{4}
\]
Then, for every \(p\in P\),
\[
 \|P_K Ep\|_2\le\|p\xi^*\|_2+
                       \sqrt{2M_0/m}\,\|p\sqrt W\|_2 .                  \tag{5}
\]
In particular \(2\xi^*\xi+4(M_0/m)W\) dominates these outputs on any finite column.
The same estimate holds for the entire right slice on the span of \(n a n'\) with \(n,n'\in N,\ a\in P_B\), using the closed derivation on these inputs.
No commutativity assumption is required on \(N\).

## Argument

### Exact energy and affine-line rigidity

The [forced starred symbols](Yin_C_F0076_v1.md#statement) identify the marginal law as diffuse and the derivative on \(P_B\) as the scalar divided difference, including on the adjoint symbol.
Pairing the joint vacuum against marginal tests gives the scalar vacuum \(\xi_B\).
For \(y,p\in P\) apply the vacuum identity to \(y^*p\).
With \(F=(\tau\otimes\mathrm{id})\delta_i\), the product rule gives \(\langle y,Ep\rangle=\langle y\xi-(F(y^*))^*,p\rangle\) and hence \(Ty=y\xi-(F(y^*))^*\).
On \(P_B\) the two scalar slices agree by symmetry of the divided difference.
Writing \(Jb=\bar b\) there, we have
\[
                 Ta=T_Ba+a\eta,\qquad T_Ba=a\xi_B-JE_BJa .
\]
The two summands are orthogonal because \(\mathbb E_B(a\eta)=0\).
For real \(f\in P_B\), traciality gives \(\|f\eta\|_2^2=\int f^2 v\,d\mu\) and \(\langle\eta,f\eta\rangle=\int f v\,d\mu\).
The scalar identities from the [planar energy formula](Yin_C_F0267_v1.md#statement) yield (1) on substitution.

Adding the two defects from (1) gives \(\tfrac14\iiint\kappa(z,w,s)^2|z-w|^2\,d\mu^3\).
The circumradius formula gives its angular expression in (2); the three independent points are distinct almost surely.
Draw \(s,z,w\) independently from \(\mu\) and let \(a(s)=\int k(z,s)\,d\mu(z)\), \(c=\int a\,d\mu\).
The squared distance between the two phase factors \(k(z,s)\) and \(k(w,s)\) is four times that squared sine.
Consequently \(2D=1-\int|a(s)|^2d\mu(s)\).
In \(L^2(\mu^2)\) the two functions \(a(z)-c,a(s)-c\) are orthogonal and are the two one-variable centered projections of \(k-c\), by symmetry.
Thus \(2\int|a-c|^2\,d\mu\le1-|c|^2\), giving \(1-|c|^2\le4D\), in particular the first inequality in (2).

Choose an angle \(\phi\) such that \(e^{-2i\phi}=c/|c|\) if \(c\ne0\), and any angle if \(c=0\).
Then \(\mathbb E\sin^2(\arg(z-w)-\phi)=(1-|c|)/2\).
The line with angle \(\phi\) through the mean of \(\mu\) has mean squared transverse distance equal to the variance of \(\operatorname{Im}(e^{-i\phi}z)\).
By independent differences this variance is at most \(d^2(1-|c|)/4\).
Since \(1-|c|\le1-|c|^2\), minimizing over lines proves the second inequality in (2).

If \(\|Tp\|^2=\tau(hp^*p)\) on \(P\), polarization with \(p=1\) gives \(\langle\xi,Tq\rangle=\tau(hq)\) for all \(q\in P\).
Both defects in (2) vanish.
The infimum over lines through the mean is attained by compactness of the direction circle, so the support lies on a line.
Faithfulness of the trace identifies the support with the spectrum.
Conversely in that case write \(Z=z_0+e^{i\phi}x\) with \(x=x^*\).
The represented core is unchanged by this affine replacement, the scaled derivative \(e^{i\phi}\delta_i\) takes \(x\) to \(1\otimes1\), and all other coordinate derivations kill both \(Z,Z^*\).
Thus the relabelled tuple still has actual starred derivations.
The [real-coordinate adjoint isometry](Yin_C_F0266_v1.md#statement) gives a density for the relabelled core, and the unimodular scaling preserves the squared norms of its adjoint outputs.
A line also gives \(D=0\) directly by the angular formula.

### The projected right slice for arbitrary correlations

For \(a\in P_B\) and \(p\in P\) the orthogonal decomposition above implies
\[
 \langle a,Ep\rangle=\langle T_Ba,\mathbb E_Bp\rangle+
                              \langle a,\mathbb E_B(p\eta^*)\rangle .
\]
The scalar slice on the core is bounded on \(L^2(W\mu)\) with norm at most \(2+\sqrt2\).
Every bounded Borel \(b\in B\) admits a polynomial sequence converging to \(b\) in \(L^2((1+W)\mu)\), by density of continuous functions for a finite Borel measure and Stone–Weierstrass.
Taking its graph limit puts \(b\) in \(\operatorname{Dom}\overline E_B\), gives precisely this weighted extension there, and identifies its pairing with \(T_Ba\).
Density in \(L^2(B)\) proves (3).
Conditional Schwarz gives \(\|(\mathbb E_Bp)\sqrt W\|_2^2\le\tau(W p^*p)\) by first truncating \(W\).
Also \(\|\mathbb E_B(p\eta^*)\|_2\le\|p\eta^*\|_2\).
These two bounds and the square triangle inequality give the asserted weight.

### The finite column on ordered two-block outputs

On the Hilbert product \(H_0=L^2(N)\otimes L^2(B)\) define \(U(n\otimes a)=na\) first on the algebraic tensor of bounded vectors.
For \(u=\sum_j n_j\otimes a_j\),
\[
    \|Uu\|_2^2=\int\sum_{j,l}\bar a_j(z)a_l(z)
                    \mathbb E_B(n_j^*n_l)(z)\,d\mu(z).
\]
For the finite list \(n_j\), (4) on positive squares of their rational linear combinations, on a common full-measure set, gives the two Gram matrix inequalities
\(m[\tau(n_j^*n_l)]\le[\mathbb E_B(n_j^*n_l)(z)]\le M_0[\tau(n_j^*n_l)]\).
Density of rational complex coefficient vectors proves them for all complex vectors, allowing \(a_j(z)\) as coefficients.
It follows that \(G=U^*U\) satisfies \(mI\le G\le M_0I\) and \(U:H_0\to K\) is an isomorphism.
The map \(U\) intertwines right multiplication by \(B\); its adjoint does as well.
Hence \(G\) commutes with bounded scalar spectral multipliers on the last factor, and \(P_K\) commutes with right \(B\).

For \(n\in N,\ a\in P_B\), the [omitted-algebra graph property](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) and bounded strong-star approximation of \(n\) by omitted polynomials permit testing the derivative of \(a^*n^*p\) in the vacuum identity.
The terms at \(a^*\) trace to \(\langle nJE_BJa,p\rangle\), by the product rule and symmetry of the scalar divided difference.
Thus, for every finite \(u=\sum_j n_j\otimes a_j\) with these factors, on putting \(L=JE_BJ\) we have
\[
       \langle Uu,Ep\rangle=\langle Uu,p\xi^*\rangle
                           -\langle U(I\otimes L)u,p\rangle .              \tag{6}
\]
This holds also for bounded inputs \(p\) admitting bounded strong-star and graph approximation, since all pairings in (6) then pass to the limit.
The indicated approximation exists for \(p\) in the span of \(n a n'\) by the omitted-algebra graph property and the product rule.

For scalar bounded inputs the map \(JT_BJ\) extends to \(L^2(W\mu)\to L^2(B)\) of norm at most \(\sqrt2\) by the [complex scalar adjoint bound](Yin_C_F0267_v1.md#statement).
On each scalar original core element \(a\) one has \(\langle La,b\rangle=\langle a,JT_BJ b\rangle\) first for scalar polynomials \(b\) by adjoint pairing and scalar conjugation.
It also holds for \(b\in L^2((1+W)\mu)\) by weighted polynomial approximation.
Tensor with \(I_{L^2(N)}\) to obtain the same estimate and duality between finite tensor tests \(u\) and every vector in \(L^2(N)\otimes L^2((1+W)\mu)\), by density of finite tensors there.

Set \(h=U^{-1}P_Kp\).
Since \(P_K\) and \(U\) intertwine bounded marginal multipliers, truncating \(\sqrt W\) gives
\[
     \|(I\otimes M_{\sqrt W})G h\|_2^2
         \le M_0\|P_K p\sqrt W\|_2^2
         \le M_0\|p\sqrt W\|_2^2.
\]
Indeed for \(s=\min(\sqrt W,t)\) one has \(\|Gs h\|^2\le M_0\langle s h,Gs h\rangle=M_0\|P_K(p s)\|^2\) before taking limits.
The right side is finite for bounded \(p\).
By (6) the pairing of \(P_K(p\xi^*-Ep)\) with \(Uu\) now equals \(\langle u,(I\otimes JT_BJ)Gh\rangle\).
Since \(\|u\|\le m^{-1/2}\|Uu\|\), duality on the dense tests proves the error bound in (5).
Its squared version gives the stated column weight by summation.
Finally \(E(n a n')=n(\mathrm{id}\otimes\tau)((\delta_i a)n')\) belongs to \(K\), since in the scalar tensor \(L^2(B)\otimes L^2(B)\) the right trace here contracts against a fixed bounded vector.
The estimates therefore apply to the full output on the stated span.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:38 |
| status | open |
| reason | Fix the joint marginal defect and rigidity, the marginal projection, and the two-block column theorem for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact marginal energy, quantitative rigidity and the affine-line criterion on the full core, universal marginal projection and the conditional two-block bound. |
| argument | [Argument](#argument) | Orthogonal vacuum splitting, two independent directions, graph pairings, conditional Gram estimate, and weighted Hilbert-product duality. |
| dependency | [Forced normal symbols](Yin_C_F0076_v1.md#statement) | Diffuse spectral law, marginal divided difference and vanishing on both omitted symbols. |
| dependency | [Scalar curvature identity and weight](Yin_C_F0267_v1.md#statement) | Polarized exact scalar energy and both homogeneous weighted scalar bounds. |
| dependency | [Selfadjoint distinguished coordinate](Yin_C_F0266_v1.md#statement) | Existence of one exact full-core density when an affine replacement puts the coordinate on the real line. |
| dependency | [Omitted algebra in the closed graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded omitted coefficients and their adjoints can be inserted with zero derivative and bounded approximation. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:47 |
| status | proved |
| reason | Independent review verifies the two-test characterization, the marginal projection and the conditional two-block bound on the stated actual tuple. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact marginal energy, quantitative rigidity and the affine-line criterion on the full core, universal marginal projection and the conditional two-block bound. |
| argument | [Argument](#argument) | Orthogonal vacuum splitting, two independent directions, graph pairings, conditional Gram estimate, and weighted Hilbert-product duality. |
| dependency | [Forced normal symbols](Yin_C_F0076_v1.md#statement) | Diffuse spectral law, marginal divided difference and vanishing on both omitted symbols. |
| dependency | [Scalar curvature identity and weight](Yin_C_F0267_v1.md#statement) | Polarized exact scalar energy and both homogeneous weighted scalar bounds. |
| dependency | [Selfadjoint distinguished coordinate](Yin_C_F0266_v1.md#statement) | Existence of one exact full-core density when an affine replacement puts the coordinate on the real line. |
| dependency | [Omitted algebra in the closed graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded omitted coefficients and their adjoints can be inserted with zero derivative and bounded approximation. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0280_v1.md#finding) | All four direct interfaces, both defect inequalities, the exact isometry criterion and the weighted two-block estimates. |
