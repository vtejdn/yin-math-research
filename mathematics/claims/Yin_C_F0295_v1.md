---
author: Yin
---

# Localization of a deficient normal slice to orthogonal projections near two spectral points

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let a finite tuple of bounded normal generators satisfy the [actual starred conjugate-variable hypothesis](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix a coordinate \(Z\), either orientation (write \(Z^*\) in place of \(Z\) for the other), the corresponding derivation \(\delta\), and \(E=(\mathrm{id}\otimes\tau)\delta\) on the represented polynomial core \(P\).
Write \(T_r\) for its normal cutoff with inner multiplier \(m_r(z,w)=|z-w|^2/(|z-w|^2+r^2)\).
Fix any positive sequence \(r_j\to0\).

If \(E\) is unbounded on the operator-norm unit ball of \(P\), there are two possibly equal points of the marginal spectrum with the following property.
In the spectral projection of any neighborhood of their union there are mutually orthogonal projections \(p_n\), each in both oriented forward and adjoint domains and having convergent cutoff values in both orientations.
Their supports may be taken in disjoint marginal annuli shrinking to the union, in the sense \(p_n\le 1_{U_n\setminus U_{n+1}}(Z)\) for nested neighborhoods shrinking to the union.
For **every** infinite \(J\subseteq\mathbb N\), the projection \(p_J=\sum_{n\in J}p_n\) satisfies
\[
 p_J\notin\operatorname{Dom}\bar E,\qquad
 \sup_j\|T_{r_j}p_J\|_2=\infty .
\]
Thus on one atomic abelian subalgebra of an arbitrarily small marginal corner the restriction of the forward graph to its subsum projections contains exactly the finite subsums (the subalgebra can use \(\sum p_n\) as its unit).
Conversely the existence of such a family excludes a finite single-input bound.
This criterion leaves open whether any actual normal tuple has a deficient orientation.

## Argument

### Localization before taking graph limits

Let \(C=\mathrm{id}\otimes\tau\), \(\gamma=I_{z-w}\delta\), and \(B=\|C\gamma\|_{\infty\to2}<\infty\) by the [liberation bound](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm).
Uniformly in \(r\), the two errors
\[
 T_r(Zx)-ZT_rx,\qquad T_r(xZ)-(T_rx)Z
\]
have norm at most \(L\|x\|\), where \(L=1+3B\).
For the first error the product rule gives the trace slice of \(I_{m_r}(1\otimes1)\cdot x\), of norm at most \(\|x\|\) by coarse Hilbert contraction.
The second error is \(xT_rZ-C I_{m_r}\gamma(x)\) by traciality in the second leg and the product rule.
Here \(\|T_rZ\|_2\le1\), and \(1-m_r\) is a probability mixture of products of marginal unitary characters by the [Gaussian representation and separated multiplier estimate](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm).
That estimate bounds the slice of \(I_{1-m_r}\gamma\) by \(2B\).
The bounds on \(P\) extend to \(M\) by bounded strong-star approximation, normality of \(T_r\), and weak lower semicontinuity.

For \(e=1_{\{|Z-\lambda|<s\}},\,f=1_{\{|Z-\lambda|<2s\}}\), if \(x=x(1-f)\) then \(\|(T_rx)e\|_2\le L\|x\|/s\).
Indeed take \(x_k=x(1-f)(Z-\lambda)^{-k}\) with the inverse restricted to \(1-f\).
Apply the right error bound to \(x_k(Z-\lambda)=x_{k-1}\) successively and multiply on the right by \(e\).
The \(k\)-th error is bounded by \(L\|x\|(2s)^{-k}s^{k-1}\), and the remainder after \(k\) steps by \(\|T_r\|_{\infty\to2}2^{-k}\|x\|\), which tends to zero for each fixed \(r\).
The left error bound gives \(\|eT_rx\|_2\le L\|x\|/s\) for \(x=(1-f)x\) by the same iteration on the left.
These estimates concern physical supports of inputs and outputs of the normal maps.

The cutoff norms are unbounded along the prescribed sequence by [core convergence](Yin_C_F0282_v1.md#statement).
There is a pair \((\lambda,\mu)\) such that the norms of \(x\mapsto 1_V(Z)T_{r_j}(x)1_W(Z)\) are unbounded for every open rectangle \(V\times W\) about this pair.
Otherwise finitely many bounded rectangles cover the compact spectral product.
Partition the spectrum into finitely many Borel cells according to membership in all their left and right sides.
Each nonempty pair of cells lies inside a bounded rectangle, so summing the finitely many block bounds bounds all the cutoff norms.
Take balls of radius \(s\) around the two points and let \(F\) be the spectral projection of the union of their doubled balls.
Writing \(x=FxF+(1-F)x+Fx(1-F)\), the two off-support estimates show that already on the unit ball of \(FMF\) the cutoff norms are unbounded.
This holds with arbitrarily small \(s\).

### Recovering large actual graph values in punctured neighborhoods

Fix any open neighborhood \(U\) of the two points in the plane.
Consider the class of core expressions enlarged by adjoining smooth compactly supported functions of the two real components of \(Z\).
Every fixed expression has uniformly operator-bounded polynomial approximants converging in operator norm with convergence of both coarse derivatives in Hilbert norm, and with those derivatives bounded in the opposite spatial tensor algebra of [the mixed spectral cut calculation](Yin_C_F0285_v1.md#slices-of-resolvents-of-a-mixed-polynomial).
Indeed, on a box containing the spectrum, a smooth function can be approximated in \(C^1\) by real-variable polynomials (periodize a smooth extension, approximate by finite Fourier sums and then Taylor polynomials of the exponentials).
The normal marginal derivative is its divided difference, bounded by the Lipschitz constant, also in the conjugate orientation.
Products pass by the Leibniz rule and operator-norm convergence of each factor.
Write \(E\) also for its closed value on these expressions.
Allow smooth characters on the spectrum using a cutoff equal to one there.

On contractions \(y\) in this class supported on both sides in a compact subset of \(U\setminus\{\lambda,\mu\}\), the values \(\|Ey\|_2\) are unbounded.
Suppose instead that they are at most \(K\).
For a marginal character \(v\), the expression \(yv\) has the same support constraint, so the separated multiplier identity
\[
 C I_{v^*\otimes v}\delta(y)=E(yv)v^*-yE(v)v^*
\]
bounds its norm by \(K+b\), where \(b\) bounds the scalar marginal slice on contractions by the [scalar column estimate](Yin_C_F0267_v1.md#statement).
Integration against the Gaussian probability gives \(\|T_ry\|_2\le2K+b\) for every \(r\).
The identity is valid on this class by the graph approximation above.
Take the union of two small doubled balls with closure in \(U\), and its projection \(F\) as above.
Each contraction in \(FMF\) is a bounded strong-star limit of such punctured expressions with norms at most one: approximate the contraction by polynomial contractions by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) and norm rescaling, and multiply on both sides by smooth cutoffs supported in \(U\) away from the two points, tending to one on the doubled balls except at those points.
The points have zero spectral projection by [marginal diffuseness](Yin_C_F0076_v1.md#statement).
Normality of each \(T_r\) would give the same uniform bound throughout \(FMF\), a contradiction.

Real and imaginary parts therefore give selfadjoint contractions \(h\) of the same kind with arbitrarily large \(\|Eh\|_2\).
For almost every \(0<t<1\), both \(1_{(t,\infty)}(h)\) and \(1_{(t,\infty)}(-h)\) have both oriented cutoff limits and the four graph inclusions, as in the [mixed spectral cut theorem](Yin_C_F0285_v1.md#statement).
To use that argument on \(h\), the approximants just constructed give both bounded spatial derivatives of \(h\), and polynomial functions of \(h\) lie in both closed coarse graphs by the norm and derivative product limits.
The same Neumann approximation for the resolvent therefore gives its derivative as the bounded derivative of \(h\) multiplied by the two outer resolvents.
The cited sliced resolvent bound and integrable mass criterion apply unchanged to the scalar law of \(h\); almost every threshold satisfies the criterion and has zero atomic mass.
The strong input and graph limits for the adjoint formula also hold on these approximants.
All these upper projections retain the punctured support of \(h\).
If their forward norms were bounded by a common \(D\) over all such \(h\) and all good thresholds, the spectral layer representation of \(h\), paired against \(E^*v\) for \(v\in\operatorname{Dom}E^*\), would give \(|\langle v,Eh\rangle|\le2D\|v\|_2\).
Density would bound \(\|Eh\|_2\).
This proves availability of punctured projections with arbitrarily large actual forward norms and convergent cutoffs.

### A single sequence for all infinite subsums

Choose successively a good projection \(p_n\) in the current punctured neighborhood, so large in forward norm that one can take a unit \(v_n\in\operatorname{Dom}E^*\) with
\[
 |\langle v_n,\bar E p_n\rangle|> 3n+3+\sum_{k<n}\big(\|\bar E p_k\|_2+\sup_j\|T_{r_j}p_k\|_2\big).
\]
All previous suprema are finite by convergence.
Choose \(j_n>j_{n-1}\) such that \(|\langle v_n,(T_{r_{j_n}}-\bar E)p_n\rangle|<1\).
Shrink the next neighborhood to miss the compact support used for \(p_n\) and to have radius tending to zero around the pair.
Make it small enough that both normal functionals \(x\mapsto\langle E^*v_n,x\rangle\) and \(x\mapsto\langle v_n,T_{r_{j_n}}x\rangle\) have absolute value at most one on contractions of its corner.
This is possible since the neighborhood projections decrease to zero by diffuseness: for a normal functional with tracial \(L^1\) density, first truncate that density in \(L^1\) and use the corner trace for its bounded part.
This use of a density is the [finite tracial predual identification](../audits/literature/AP18/Yin_U003.md#l1-predual-interface).
The same choice controls every later tail since neighborhoods are nested.

For an infinite \(J\), take \(n\in J\).
Terms preceding \(p_n\) in each of the two scalar pairings cost at most the displayed sum, and the tail is a projection in the smaller corner.
Hence \(|\langle E^*v_n,p_J\rangle|>n\) and \(|\langle v_n,T_{r_{j_n}}p_J\rangle|>n\).
The first inequality is impossible for infinitely many unit tests if \(p_J\in\operatorname{Dom}\bar E\); the second gives cutoff divergence.
Finite sums retain their graph and convergence properties by linearity.
Applying this argument at each orientation where the bound fails, and using the [two-orientation criterion](Yin_C_F0075_v1.md#statement), gives a necessary obstruction for failure of the original strong condition.
The converse uses the same criterion if any such family is exhibited on an actual tuple.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:03 |
| status | open |
| reason | Fix localization and the subsum obstruction for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Localization and simultaneous subsum divergence for any deficient actual slice. |
| argument | [Argument](#argument) | Uniform multiplication errors, punctured smooth tests, graph limits and orthogonal subsums. |
| dependency | [Liberation and Gaussian multipliers](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Bounded liberation slice and Gaussian separated multipliers. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#statement) | Fixed-radius normality and core convergence along any prescribed sequence. |
| dependency | [Mixed spectral cuts](Yin_C_F0285_v1.md#statement) | Sliced resolvent estimate, good thresholds, four graph domains and norm limits. |
| dependency | [Marginal vacuum and diffuseness](Yin_C_F0076_v1.md#statement) | Diffuse marginal and its two represented divided differences. |
| dependency | [Scalar estimate](Yin_C_F0267_v1.md#statement) | Bounded scalar marginal slice. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation. |
| dependency | [Tracial predual](../audits/literature/AP18/Yin_U003.md#ap18-u003) | Normal functionals have integrable densities. |
| dependency | [Normal domain comparison](Yin_C_F0075_v1.md#statement) | Relation to the original strong condition. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:10 |
| status | proved |
| reason | Independent review verified the two multiplication errors, localization in punctured corners and simultaneous divergence and domain omission for every infinite subsum. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Localization and simultaneous subsum divergence for any deficient actual slice. |
| argument | [Argument](#argument) | Uniform multiplication errors, punctured smooth tests, graph limits and orthogonal subsums. |
| dependency | [Liberation and Gaussian multipliers](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Bounded liberation slice and Gaussian separated multipliers. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#statement) | Fixed-radius normality and core convergence along any prescribed sequence. |
| dependency | [Mixed spectral cuts](Yin_C_F0285_v1.md#statement) | Sliced resolvent estimate, good thresholds, four graph domains and norm limits. |
| dependency | [Marginal vacuum and diffuseness](Yin_C_F0076_v1.md#statement) | Diffuse marginal and its two represented divided differences. |
| dependency | [Scalar estimate](Yin_C_F0267_v1.md#statement) | Bounded scalar marginal slice. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation. |
| dependency | [Tracial predual](../audits/literature/AP18/Yin_U003.md#ap18-u003) | Normal functionals have integrable densities. |
| dependency | [Normal domain comparison](Yin_C_F0075_v1.md#statement) | Relation to the original strong condition. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0301_v1.md#finding) | Complete fixed candidate and its declared dependency interfaces. |
