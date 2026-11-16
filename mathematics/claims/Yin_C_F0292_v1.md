---
author: Yin
---

# Canonical domains after subtracting circular components of the curvature kernel

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a finite bounded normal generating tuple \(X\) with actual starred conjugate variables in a finite tracial von Neumann algebra \((M,\tau)\).
Write \(\mu\) for its spectral law, \(\delta=\delta_i\) for its coordinate derivation on \(P=\mathbb C\langle X,X^*\rangle\), \(\xi=\delta^*(1\otimes1)\), and \(\zeta=-i[Z^*,\xi]\) for the vacuum of \(i\gamma\), where partial liberation satisfies \(\gamma(f)=f\otimes1-1\otimes f\) at the distinguished marginal and vanishes at the omitted coordinates.
Let \(\nu_\zeta,\nu_\xi\) be the joint spectral measures of these vectors for left and right multiplication by \(Z\).
Set \(g(z,v)=\int\kappa(z,w,v)^2\,d\mu(w)\), where \(\kappa\) is the reciprocal circumradius with zero value on collinear or repeated triples.

Suppose that \(\mu^2\)-almost everywhere
\[
 g(z,v)=\sum_{n\ge1}\lambda_n1_{B_n}(z)1_{B_n}(v)+b(z,v),\qquad
 L=\sum_n\frac{\lambda_n}{t_n}\|e_n\zeta e_n\|_2^2<\infty ,
 \tag{1}
\]
where \(\lambda_n\ge0\), \(B_n\) are measurable with \(t_n=\mu(B_n)>0\) and \(e_n=1_{B_n}(Z)\).
Assume the real symmetric remainder \(b\) has uniformly square-integrable rows with respect to \(\mu\) and belongs to \(L^2(\nu_\zeta)\).
Then the original canonical operator \(D_i=-\overline{(\mathrm{id}\otimes\tau)\delta_i}\) and its Hilbert adjoint both have domains containing \(M\Omega\) and \([X_j,D_i]=\delta_{ij}P_\Omega\) on \(M\Omega\).

In particular the conclusion holds if pairwise disjoint circles \(K_n\) of radii \(r_n>0\) carry the full marginal mass, with \(t_n=\mu(K_n)>0\) and
\[
          \sup_n\sum_{m\ne n}\frac{t_m}{\operatorname{dist}(K_n,K_m)^2}<\infty .
          \tag{2}
\]
This permits arbitrary correlations and arbitrary spectra at the other coordinates.
If every coordinate satisfies (1), the tuple admits the strong dual system of the [normal comparison problem](../tasks/Yin_T_F0011_v1.md#contract).
There is a scalar law with actual vacuum satisfying (2) whose curvature operator is unbounded on \(L^2(\mu)\) and whose fourth kernel composition is infinite on a rectangle of positive product measure.

## Argument

### The signed estimate on analytic unitaries

Let \(u=a\pm i\sqrt{1-a^2}\) for a strict selfadjoint polynomial contraction \(a\) and define \(Q_q(u)=\operatorname{Re}\langle u,(\mathrm{id}\otimes\tau)I_q\gamma(u)\rangle\), initially for finite bounded marginal tensors \(q\).
Here \(I_{s\otimes t}(v\otimes w)=vs\otimes tw\) denotes inner insertion.
For \(e=1_B(Z)\), \(t=\tau(e)>0\), the [projection energy identity, equation (4)](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) gives
\[
 t Q_{e\otimes e}(u)
   =\|i(\mathrm{id}\otimes\tau)I_{e\otimes e}\gamma(u)-u e\zeta e\|_2^2
       -\|e\zeta e\|_2^2 .
\]
Consequently \(Q_{q_N}(u)\ge-L\) at every partial sum \(q_N=\sum_{n\le N}\lambda_n e_n\otimes e_n\).
The [weighted liberation theorem](Yin_C_F0077_v1.md#statement) bounds \(|Q_b(u)|\le K_b\) independently of \(u\), since \(b\) is symmetric with the stated row and vacuum bounds.
Its core norm estimate applies to this analytic evaluation by the binomial series, which converges both in operator norm and after differentiation at \(\|a\|<1\).

To identify the limit, the [scalar geometric criterion](Yin_C_F0255_v1.md#statement) gives finite total squared curvature and diffuseness.
Conditional Jensen and \(|z-v|\kappa(z,w,v)\le2\) give
\[
 \iint |z-v|^2g(z,v)^2\,d\mu(z)d\mu(v)\le4\iiint\kappa^2\,d\mu^3.
\]
The gap times \(b\) belongs to \(L^2(\mu^2)\) by compactness and its row bound.
From \(0\le q_N\le g+|b|\) we get \((z-v)(q_N+b)\to(z-v)g\) in \(L^2(\mu^2)\), and the same with conjugate gap.
The weighted liberation takes these gap tensors as its generator values on \(Z,Z^*\), and zero on every omitted letter.
Thus its values on each fixed polynomial converge by the finite outer Leibniz expansions.
The analytic evaluation at \(u\) also converges, since the bound on the derivative of \(a^j\) is \(j\|a\|^{j-1}\) times the derivative norm at \(a\).
In particular \(Q_g(u)\ge-L-K_b\), where the subscript \(g\) denotes evaluation through the gap tensors.
These convergences require no \(L^2(\mu^2)\) assumption on \(g\).

For the two real components of the coordinate derivation let \(V(u)^2\) be the sum of their squared right-slice norms.
Equations (19) and (20) of the [mixed-energy calculation](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) give
\[
                    V(u)^2\le2\|\xi\|_2 V(u)+(L+K_b)/2 .
\]
Indeed, the signed defect in (19) is \(-Q_g(u)/2\) by its gap tensors at \(Z,Z^*\) and its zero values on the omitted letters.
Averaging the two signs bounds the slices of the real components on strict selfadjoint contractions.
Scaling and splitting general core elements into real and imaginary parts gives the two oriented slice bounds on \(P\).
The [two-slice theorem](Yin_C_F0072_v1.md#statement) and the [original-domain commutator passage](Yin_C_F0078_v2.md#the-original-canonical-operators) give both domain inclusions and the generator commutators.

### Countably many circles

In (1) put \(B_n=K_n\) and \(\lambda_n=t_n/r_n^2\).
Three distinct points on \(K_n\) have curvature \(1/r_n\).
Every other triangle has curvature at most two divided by its diameter.
For endpoints in the same \(K_n\), summing the squared curvature over third points on other circles costs at most four times the supremum in (2).
For endpoints in \(K_n,K_l\) with \(n\ne l\), all third points outside \(K_n\) obey the same integral bound.
Those inside \(K_n\) cost at most \(4t_n/\operatorname{dist}(K_l,K_n)^2\), controlled by the sum for \(l\).
Thus the remainder \(b\) is bounded.
The [liberation vacuum identity](Yin_C_F0238_v1.md#statement) gives \(d\nu_\zeta=|z-v|^2d\nu_\xi\).
On \(K_n^2\) the gap is at most \(2r_n\), hence disjointness gives \(L\le4\sum_n\nu_\xi(K_n^2)\le4\|\xi\|_2^2\).

### A law with divergent curvature compositions

Take circles centered at \(2^{-n}\) of radii \(r_n=2^{-4n-4}\), with weights \(t_n=7\,2^{-3n}\) times normalized arclength, \(n\ge1\).
Here \(d_{nm}=\operatorname{dist}(K_n,K_m)\ge2^{-\min(n,m)}/4\), giving (2) since \(\sum_m4^m t_m<\infty\).
The scalar law has finite total curvature by the bounded remainder and \(\sum_n t_n^3/r_n^2<\infty\).
For \(z\in K_n\), its own circle contributes at most \(C t_n/r_n\) to the maximal linear density, by the arclength estimate for a disk on a circle.
The other circles contribute at most \(\sum_{m\ne n}t_m/d_{nm}\), bounded by Cauchy--Schwarz and (2).
Squaring and integrating gives finite geometric energy, hence an actual scalar vacuum by the [marginal criterion](Yin_C_F0255_v1.md#statement).
Testing \(t_n^{-1/2}1_{K_n}\) gives a curvature quadratic form at least \(t_n^2/r_n^2\to\infty\).
The curvature operator is therefore unbounded and cannot obey the weighted Schur hypothesis of the [curvature row criterion](Yin_C_F0291_v1.md#statement).

Choose compact arcs \(U,V\) of positive arclength on the first circle such that every triangle with vertices in \(U,V,\{0\}\) has curvature bounded below by a positive constant.
Such arcs exist by continuity at two points of the first circle that are noncollinear with zero.
For \(z\in U\) and \(v\in K_n\) with \(n\) sufficiently large, integration over \(V\) then gives \(g(z,v)\ge c>0\).
For both endpoints in \(U\), restricting the three intermediate vertices of \(g^{\circ4}\) to the same \(K_n\) gives the lower bound \(c^2\sum_{n\text{ large}}t_n^5/r_n^4=\infty\).
The signed estimate still applies at this marginal in every actual normal tuple containing it.
A bound for arbitrary planar marginals remains open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:00 |
| status | open |
| reason | Fix the signed curvature estimate, countable circle criterion and divergent-composition example for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The original domains under (1), its application (2) and the actual divergent-composition marginal. |
| argument | [Argument](#argument) | Projection blocks, signed remainder, two oriented slices, circle geometry and exact summability ranges in the example. |
| dependency | [Projection energy identity](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (4) for arbitrary measurable marginal projections and both analytic-unitary signs. |
| dependency | [Weighted liberation theorem](Yin_C_F0077_v1.md#statement) | The operator-norm-to-Hilbert bound for a real symmetric remainder satisfying its row and vacuum bounds. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Actual marginals have finite curvature and the example has an actual vacuum at finite geometric energy. |
| dependency | [Original mixed-energy identity](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Equations (19) and (20), including the signed defect and its gap tensors. |
| dependency | [Two-slice theorem](Yin_C_F0072_v1.md#statement) | Original operator and adjoint domains from the two oriented bounds. |
| dependency | [Original commutators](Yin_C_F0078_v2.md#the-original-canonical-operators) | Rank-one commutators on the entire algebra-generated GNS subspace. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#statement) | Commutator formula for the liberation vacuum and its squared-gap spectral measure. |
| dependency | [Weighted curvature criterion](Yin_C_F0291_v1.md#statement) | Its weighted integral inequality forces a bounded curvature operator on the marginal Hilbert space. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:10 |
| status | proved |
| reason | Independent review verified the signed block bound, the two domains, the circle separation condition and the divergent fourth composition. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The original domains under (1), its application (2) and the actual divergent-composition marginal. |
| argument | [Argument](#argument) | Projection blocks, signed remainder, two oriented slices, circle geometry and exact summability ranges in the example. |
| dependency | [Projection energy identity](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (4) for arbitrary measurable marginal projections and both analytic-unitary signs. |
| dependency | [Weighted liberation theorem](Yin_C_F0077_v1.md#statement) | The operator-norm-to-Hilbert bound for a real symmetric remainder satisfying its row and vacuum bounds. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Actual marginals have finite curvature and the example has an actual vacuum at finite geometric energy. |
| dependency | [Original mixed-energy identity](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Equations (19) and (20), including the signed defect and its gap tensors. |
| dependency | [Two-slice theorem](Yin_C_F0072_v1.md#statement) | Original operator and adjoint domains from the two oriented bounds. |
| dependency | [Original commutators](Yin_C_F0078_v2.md#the-original-canonical-operators) | Rank-one commutators on the entire algebra-generated GNS subspace. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#statement) | Commutator formula for the liberation vacuum and its squared-gap spectral measure. |
| dependency | [Weighted curvature criterion](Yin_C_F0291_v1.md#statement) | Its weighted integral inequality forces a bounded curvature operator on the marginal Hilbert space. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0302_v1.md#finding) | Complete fixed candidate and its declared dependency interfaces. |
