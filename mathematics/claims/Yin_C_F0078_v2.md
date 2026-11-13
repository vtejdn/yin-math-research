---
author: Yin
---
# Curvature row bounds and canonical domains for correlated normal tuples

Version 2 of C_F0078 extends the marginal upper-growth theorem by estimating the coordinate gap along every finite kernel composition.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a bounded normal generating tuple in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, and write \(H=L^2(M,\tau)\) and \(\Omega=1\).
Assume the full ACSY condition \(\mathsf A\) on the represented star algebra \(\mathcal A=\mathbb C\langle X,X^*\rangle\), with outer coordinate derivations \(\delta_i\), \(\delta_i X_j=\delta_{ij}1\otimes1\), and actual adjoint vacua \(\xi_i=\delta_i^*(1\otimes1)\in H\).
For each marginal write \(K=\sigma(X_i)\), let \(\mu\) denote its diffuse spectral probability, and put
\[
 g(z,v)=\int \mathfrak c(z,w,v)^2\,d\mu(w)\qquad(z\ne v).
\]
Here \(\mathfrak c\) is the reciprocal circumradius of a noncollinear triple and zero for collinear or repeated points.
In row integrals set \(g(z,z)=0\).
Suppose that each marginal satisfies both bounds
\[
 A=\sup_{z\in K}\int g(z,v)\,d\mu(v)<\infty,\qquad
 B=\sup_{z\ne v\in K}|z-v|g(z,v)<\infty.                     \tag{1}
\]
Then for each \(i\) the canonical operator \(D_i=-\overline{(\mathrm{id}\otimes\tau)\delta_i}\) satisfies
\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
 \qquad [X_j,D_i]|_{M\Omega}=\delta_{ij}P_\Omega|_{M\Omega}.
\]
Thus on the indicated marginal class \(\mathsf A\) is equivalent to the ordinary dual-system condition \(\mathsf S\), which requires both domains on all bounded vectors.
The joint law may be correlated.

A sufficient marginal condition for (1), writing \(D=\mathrm{diam}(K)>0\), \(t_j=2^{-j}D\) and \(\theta_j=\sup_{z\in K}\mu(\overline B(z,t_j))/t_j\), is
\[
                         \sum_{j\ge0}\theta_j^2<\infty.          \tag{2}
\]
In particular every bound \(\mu(\overline B(z,t))\le C t/(1+\log(D/t))^\beta\) for \(0<t\le D\) with \(\beta>1/2\) suffices.
All upper power growth bounds with exponent greater than one imply (2).

## Argument

### Propagation of the coordinate gap

Fix a coordinate, put \(R=1+A\), \(B'=B+D\), and let \(q_j\) be the finite real symmetric nonnegative polynomial kernels in [version 1, equation (12)](Yin_C_F0078_v1.md#argument).
Their construction uses only diffuseness and off-diagonal continuity of \(g\).
The latter follows by dominated convergence from \(\mathfrak c(z,w,v)\le2/|z-v|\) and continuity away from repeated points.
They satisfy \(q_j\le g+1\) off the diagonal and converge pointwise there to \(g\).
Fix such a \(q\) and put \(b_k=q^{\circ k}\) for successive kernel composition against \(\mu\).
These kernels are finite real symmetric polynomial tensors.
Their row masses are bounded by \(R^k\) by repeated integration.
For all distinct \(z,v\) one has
\[
                    |z-v| b_k(z,v)\le k B'R^{k-1}.             \tag{3}
\]
Indeed the endpoint distance is at most the sum of the \(k\) edge lengths.
For each summand bound its length times its kernel by \(B'\).
The two remaining path segments integrate separately, one from \(z\) and one from \(v\), with bounds \(R^{l-1}\) and \(R^{k-l}\) for edge \(l\), using symmetry at the right endpoint.
For \(k=1\) the assertion is the original gap bound for \(q\).
Each finite kernel times its own gap also vanishes at equality of its two arguments.

### Uniform energy on analytic-core unitaries

Write \(\gamma\) for the partial liberation derivation at the distinguished marginal, with value \(n\otimes1-1\otimes n\) there and zero at the other starred generators.
For a finite real symmetric polynomial kernel \(b\), put \(E_b=(\mathrm{id}\otimes\tau)\mathrm i I_b\gamma\), with \(I_b\) the inner insertion, and \(\eta_b=(\mathrm i I_b\gamma)^*(1\otimes1)\).
Use the finite-kernel identities (13) and (15) in [version 1](Yin_C_F0078_v1.md#argument), which hold before the growth estimates.
In the joint spectral calculus of left and right multiplication by \(X_i\) on \(H\), \(\eta_b=-\mathrm i S_{(\bar z-\bar v)b}\xi_i\).
Thus \(\|\eta_{b_k}\|_2\le kB'R^{k-1}\|\xi_i\|_2\), also for a vacuum spectral measure charging the diagonal.
For \(u=a+\mathrm i\sqrt{1-a^2}\) with \(a=a^*\in\mathcal A\), \(\|a\|<1\), write \(v_k=\|E_{b_k}u\|_2\).
The finite energy inequality gives
\[
 v_k^2\le 2\big(kB'R^{k-1}\|\xi_i\|_2+R^k\big)v_k+v_{2k}.
\]
Set \(s=2R\), \(w_n=v_{2^n}/s^{2^n}\), and \(c=2(1+B'\|\xi_i\|_2/R)\).
Division by \(s^{2k}\), using \(k/2^k\le1\), gives \(w_n^2\le c w_n+w_{n+1}\).
For this fixed \(q,u\) the sequence is bounded.
Indeed \(b_k\le\|q\|_\infty R^{k-1}\) by bounding the last edge, and the finite Leibniz expansion at \(a\) and differentiated binomial series at \(u\) give \(\|E_bu\|_2\le c_u\|b\|_{L^2(\mu^2)}\), as in [C_F0077 following (B7)](Yin_C_F0077_v1.md#argument).
If \(w_n>c+1\) at any index, each succeeding value grows by at least the fixed factor \(w_n-c>1\), contradicting boundedness.
Consequently
\[
                      \|E_{q_j}u\|_2\le s(c+1)                 \tag{4}
\]
uniformly in the approximant and the analytic-core unitary.

### The original canonical operators

We specify why the limit and normal mixed energy in [version 1, sections 5 and 6](Yin_C_F0078_v1.md#argument) apply with (4).
At the distinguished generator and its adjoint the derivative values are \(\mathrm i(z-v)q_j\) and \(\mathrm i(\bar z-\bar v)q_j\).
They are bounded by \(B'\) and converge in the coarse space by dominated convergence.
This gives convergence on every original core word by Leibniz, and convergence at every fixed \(u\) above by the differentiated binomial series.
The joint spectral multipliers defining the vacua likewise converge on \(\xi_i\) by dominated convergence, using zero diagonal values.
Denote the limiting partial trace by \(E_g\).
The actual phase graphs and the normal mixed energy calculation (19)--(20) of version 1 now give
\[
 V(u)^2\le2\|\xi_i\|_2 V(u)+s(c+1)/2,
\]
where \(V(u)^2\) is the sum of the squared norms of the partial traces for the two real parts of \(\delta_i\).
This step uses the finite bound (4) and the generator identity for the mixed defect, whose identification on the actual graphs in version 1 precedes its energy estimate.
Averaging \(u,u^*\), rescaling and splitting real and imaginary parts bounds both real partial traces from the core operator norm into \(H\).
Their complex combinations bound the canonical contraction \(E_0\) and the opposite contraction \(F_0\), and \(E_0^*p=p\xi_i-F_0p\) on the core.
Bounded Kaplansky approximation and the weak closedness of the two actual graphs give both asserted canonical domains.
The core commutators pass to bounded vectors by the bounded approximation and weak graph argument of version 1.
The reverse implication uses [C_F0070 Part C](Yin_C_F0070_v1.md#statement).

### Dyadic marginal test

For fixed \(z\), partition the pair integral of \(\mathfrak c(z,w,v)^2\) by \(t_{j+1}<\max(|z-w|,|z-v|)\le t_j\).
The integrand is at most \(4/t_{j+1}^2\) and the shell has mass at most \(\mu(\overline B(z,t_j))^2\).
Diffuseness makes the omitted pair null, so \(A\le16\sum_j\theta_j^2\).
Put \(L=\sup_j\theta_j\).
Dyadic comparison gives \(\mu(\overline B(z,t))\le2Lt\) for every \(t>0\), also for \(t>D\) since \(LD\ge1\).
For \(r=|z-v|>0\), integrate first over \(|z-w|\le r\) and then over \(2^m r<|z-w|\le2^{m+1}r\), \(m\ge0\).
Using \(\mathfrak c\le2/\max(r,|z-w|)\) gives \(g(z,v)\le(8+16\sum_{m\ge0}2^{-m})L/r=40L/r\).
This proves (1).
For the logarithmic growth bound (2) follows from \(\theta_j\le C(1+j\log2)^{-\beta}\).
For the power bound \(\theta_j\) decreases at least geometrically in the upper estimate.

Condition (1) is additional to \(\mathsf A\).
For example the scalar law in [C_F0143](Yin_C_F0143_v1.md#statement) has an unbounded curvature row and an actual conjugate variable.
The unrestricted correlated-normal implication and the arbitrary-tuple bare-domain implication in F0011 remain open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T08:49 |
| status | open |
| reason | The path estimate closes the finite energy recurrence under (1) and yields the dyadic test. Independent review of this extension is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Marginal curvature bounds and dyadic criterion for the full canonical domains and the normal equivalence. |
| argument | [Argument](#argument) | Uniform finite-power gap estimate, dyadic energy recurrence, actual canonical graphs and dyadic geometry. |
| dependency | [Normal growth theorem, version 1](Yin_C_F0078_v1.md#argument) | Finite polynomial approximants, actual vacuum and finite energy identities, normal mixed energy, graph and commutator passage. |
| dependency | [Weighted partial liberation](Yin_C_F0077_v1.md#argument) | Finite Leibniz and analytic-core continuity for a fixed unitary, uniformly over Hilbert kernels. |
| dependency | [Normal strong dual to ACSY](Yin_C_F0070_v1.md#statement) | Part C for the reverse implication. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T08:58 |
| status | proved |
| reason | Adopt the path estimate, canonical domain theorem and dyadic criterion after an independent review of their full proof and the required operator-domain transfers. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Marginal curvature bounds and dyadic criterion for the full canonical domains and the normal equivalence. |
| argument | [Argument](#argument) | Uniform finite-power gap estimate, dyadic energy recurrence, actual canonical graphs and dyadic geometry. |
| dependency | [Normal growth theorem, version 1](Yin_C_F0078_v1.md#argument) | Finite polynomial approximants, actual vacuum and finite energy identities, normal mixed energy, graph and commutator passage. |
| dependency | [Weighted partial liberation](Yin_C_F0077_v1.md#argument) | Finite Leibniz and analytic-core continuity for a fixed unitary, uniformly over Hilbert kernels. |
| dependency | [Normal strong dual to ACSY](Yin_C_F0070_v1.md#statement) | Part C for the reverse implication. |
| review | [Independent review](../audits/reviews/Yin_R_F0207_v1.md#curvature-row-criterion) | Complete marginal row and gap theorem, finite-kernel energy recurrence, actual canonical domains, normal reverse implication and dyadic consequences. |
