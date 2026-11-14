---
author: Yin
---

# An explicit Gaussian column density and a sharp fourth-moment obstruction

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

In the one-channel tracial Gaussian model over \(N=L^\infty(\mu)=W^*(Z)\), let \(S\) be standard semicircular, free from \(N\), let \(a(z,y)>0\) be real symmetric almost everywhere with bounded row \(L^2\) norms, and let \(T_a\) be its selfadjoint field.
Assume that \((Z,T_a)\) satisfies the [actual starred conjugate-variable condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
In the generated algebra \(M=W^*(N,S)\), write \(E=(\mathrm{id}\otimes\tau)\delta_{T_a}\) on the original represented mixed starred polynomial algebra, let \(\xi\) be the vacuum of that coordinate, and put
\[
             h(z)=\int a(z,y)^{-2}\,d\mu(y),\qquad
             d=\frac{\xi^2+h}{2\|\xi\|_2^2}.
\]
Here \(\xi=\xi^*\) as a tracial \(L^2\) element, \(h=\mathbb E_N(\xi^2)\), and \(d\) is a probability density in \(L^1(M)\).
For every original mixed polynomial \(p\),
\[
                 \|Ep\|_2^2\le 4\|\xi\|_2^2\,\tau(d p^*p).             \tag{1}
\]
Summation gives the corresponding column bound.

For the fixed [two-disk Markov pair](Yin_C_F0259_v1.md#statement), this density belongs to every \(L^s(M)\), \(1\le s<4\).
No probability density in \(L^4(M)\) satisfies the domination inequality with any finite constant, already for tests \(u(Z,Z^*)T_a v(Z,Z^*)\).
The same tests exclude every density in the \(L^1\)-closed convex hull of the probability densities in the two marginal algebras \(N\) and \(W^*(T_a)\).
On this one fixed actual pair the available exponents of integrability for a dominating probability density are exactly \(1\le s<4\).

## Argument

### Right creation and the explicit density

Put \(\beta=1/a\).
The [single-channel vacuum formula](Yin_C_F0157_v2.md#statement) gives \(\beta\in L^2(\mu^2)\), generation and the vacuum \(\xi\) represented by the pure one-edge path \(\beta\).
For \(\beta_n=\min(\beta,n)\), let \(\xi_n=T_{\beta_n}\) be the bounded real symmetric field.
Its path vector converges in \(L^2(M)\) to \(\xi\), so \(\xi\) is selfadjoint and \(\xi_n^2\to\xi^2\) in \(L^1\) by tracial Cauchy–Schwarz.
The [creation and annihilation representation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) gives \(\mathbb E_N(\xi_n^2)(z)=h_n(z)=\int\beta_n(z,y)^2\,d\mu(y)\).
Monotone convergence and continuity of conditional expectation on \(L^1\) yield \(\mathbb E_N(\xi^2)=h\) and \(\tau(h)=\|\xi\|_2^2\).

On the path space \(H_k=L^2(\mu^{k+1})\) define right creation by
\[
    (R_n F)(z_0,\ldots,z_{k+1})=
                         F(z_0,\ldots,z_k)\beta_n(z_k,z_{k+1}).
\]
These are bounded operators for fixed \(n\), mapping each degree to the next.
Right multiplication by \(\xi_n\) is \(R_n+R_n^*\), by reversing the variables and conjugating the left field formula, since \(\beta_n\) is real symmetric.
Integration of the final variable separately in each degree gives
\[
           \|R_n(p\Omega)\|_2^2=\tau(h_n p^*p)
\]
for bounded \(p\), since right action by a base function multiplies the final endpoint.
For \(m>n\), the same norm formula with \((\beta_m-\beta_n)^2\) bounds the squared difference by \(\|p\|^2\|\beta_m-\beta_n\|_2^2\).
Hence \(R_n p\) converges in Hilbert norm, and the limiting vector has norm \(\tau(hp^*p)^{1/2}\).
Moreover \(p\xi_n\to p\xi\) in Hilbert norm.
It follows that \(R_n^* p\) converges to a vector \(D(p)\) on every bounded \(p\), with
\[
              \|D(p)\|_2\le\|p\xi\|_2+\tau(hp^*p)^{1/2}.                \tag{2}
\]

For clarity, the last-edge annihilation obtained in this limit agrees with the original slice on the mixed core.
For each \(n\), \(R_n^*\) kills \(1\) and commutes with left multiplication by \(Z,Z^*\).
Its commutator \([R_n^*,L_{T_a}]\) vanishes on positive degrees and has range in \(H_0\).
Indeed left creation adds an edge at the initial endpoint, while \(R_n^*\) integrates out the final edge.
They commute on paths of positive degree by the explicit formulas.
Left annihilation and \(R_n^*\) commute on degrees at least two by integration in the two endpoint variables, and both compositions vanish at degrees zero and one.
These identities follow first on bounded product paths by Fubini and then on each degree by boundedness.
On \(H_0\), the commutator is the integral operator with kernel \(a(z,y)\beta_n(z,y)\), which converges in Hilbert–Schmidt norm to the constant-one kernel by \(0\le a\beta_n\le1\) and dominated convergence.
Extended by zero on positive degrees, the limiting commutator is \(P_\Omega\).
Taking limits on bounded vectors gives the prescribed generator commutators for \(D\) there.
The original right slice on the core has the same commutators and value at \(1\), including at \(Z^*\) by the [forced normal generators](Yin_C_F0076_v1.md#statement).
Induction on mixed words proves equality.
Since \(\|p\xi\|_2^2=\tau(\xi^2p^*p)\), squaring (2) proves (1) and positivity and trace normalization give the probability assertion.

### The two-disk pair and its cutoffs

Use the notation and construction in [the fixed Markov example](Yin_C_F0259_v1.md#argument).
Thus \(D_0,D_1\) are the disjoint unit disks centered at \(0,4\), of masses \(5/8,q=3/8\), respectively.
Write \(f=1_{D_1},\ e_r=1_{\{|z|\le r\}}\) for \(0<r<1\) and \(t_r=\tau(e_r)=(5/8)r^2\).
On the cross rectangles \(D_0\times D_1,D_1\times D_0\), \(P=a^2\) equals \(m(z)=\sqrt{|z|}/2\) at the point in \(D_0\).
It is at least one on both same-disk squares.
For \(p_r=e_r T_a f\), the mixed polynomial approximants from that example have right-slice outputs tending in \(L^2\) to \(q e_r\) and converge strongly-star to \(p_r\) on a bounded ball.
Any probability density in \(L^1(M)\) thus pairs with the limiting square, by strong convergence on its square-root vector.

Write \(B_r=p_r^*p_r\ge0\).
Its trace is \(q\int_{e_r}m\,d\mu\le(q/2)t_r\sqrt r\).
Its marginal expectations are
\[
          \mathbb E_N B_r=f\int_{e_r}m\,d\mu,\qquad
          0\le\mathbb E_{W^*(T_a)} B_r\le4\tau(B_r)1 .                \tag{3}
\]
The first identity is the zero-edge component of \(fT_a e_r T_a f\), and the second is the [conditional square calculation](Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square).
In particular every probability density in either marginal satisfies \(\tau(w B_r)\le C_1 t_r\sqrt r\) with an absolute constant.
Linearity and norm continuity against each fixed bounded \(B_r\) give the same bound on the closed convex hull stated above.
Domination there with constant independent of \(r\) would contradict \(q^2t_r\le C^2\tau(wB_r)\) as \(r\downarrow0\).

The bounded field has left creation kernel \(a(z,y)\).
Multiplication on the left by \(e_r\) and on the right of the creation operator by \(f\) restricts it to \(e_r(z)a(z,y)f(y)\), with squared row norm at most \(\int_{e_r}m\,d\mu\).
The annihilation part is the adjoint of the creation compressed in the other order, whose squared row norm is at most \(q\sqrt r/2\).
The field representation therefore gives \(\|p_r\|\le C_2 r^{1/4}\).
Consequently \(\|B_r\|_\infty\le C_2^2\sqrt r\) and \(\|B_r\|_1\le C_3r^{5/2}\).
The elementary spectral inequality \(\|B_r\|_{4/3}\le\|B_r\|_\infty^{1/4}\|B_r\|_1^{3/4}\) gives \(\|B_r/t_r\|_{4/3}\le C_4\).
Meanwhile \(\|B_r/t_r\|_1\le(q/2)\sqrt r\to0\).
For any \(w\in L^4(M)\), approximate \(w\) in \(L^4\) by bounded elements.
Tracial Hölder and the uniform \(L^{4/3}\) bound control the error, while the \(L^1\) limit controls the bounded approximant.
Thus \(\tau(wB_r)/t_r\to0\), excluding every such probability density from the domination inequality.
The probability trace also excludes every \(L^s\) density for \(s>4\).

### Integrability of the full-algebra density

In this example decompose the one-edge vector \(\beta\) into its same-disk and cross-disk parts.
The same-disk kernel is bounded by one, so its field is a bounded element.
For \(g=1_{D_0}m^{-1/2}\), the two cross-disk kernels are \(g(z)f(y)\) and \(f(z)g(y)\).
Their elements sum to \(gSf+fSg\), by the separated-kernel correspondence first with bounded truncations of \(g\) and then by \(L^2\) convergence.
Since \(m^{-1/2}=\sqrt2|z|^{-1/4}\) on the unit disk, \(g\in L^u(\mu)\) for all \(1\le u<8\).
Both cross terms therefore belong to \(L^{2s}(M)\) for every \(1\le s<4\), using the boundedness of \(f,S\).
It follows that \(\xi^2\in L^s(M)\) in this range.
Also \(h\) is bounded on \(D_1\) by \(1+\int_{D_0}m^{-1}\,d\mu<\infty\), while on \(D_0\) it is bounded by \(1+q/m\).
Integration in polar coordinates shows \(h\in L^s(\mu)\) for \(s<4\).
This proves the asserted simultaneous integrability for the explicit \(d\) and completes the exponent determination.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:38 |
| status | open |
| reason | Fix the explicit full-algebra density and the critical integrability exponent for domination on the two-disk Gaussian pair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit domination in the positive single-channel model, no mixtures of marginal densities and exact strong integrability range on the two-disk pair. |
| argument | [Argument](#argument) | Right creation and its limiting adjoint, original generator commutators, two marginal expectations, critical normalized cutoff norms and decomposition of the successful weight. |
| dependency | [Single-channel vacuum](Yin_C_F0157_v2.md#statement) | Full actual Gaussian condition, positive-amplitude generation and the pure one-edge reciprocal-amplitude vacuum. |
| dependency | [Creation and annihilation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Wick creation row norms, reversal to the right action and bounded separated fields. |
| dependency | [Normal starred values](Yin_C_F0076_v1.md#statement) | The original distinguished derivation kills both omitted normal letters. |
| dependency | [Two-disk construction](Yin_C_F0259_v1.md#argument) | Markov covariance on the two components, strong-star approximation of the singular tests and their canonical slice outputs. |
| dependency | [Semicircular marginal conditional square](Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square) | Uniform positive bound by four times the trace for the conditional expectation of the tests. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:42 |
| status | proved |
| reason | Adopt the explicit full-algebra probability density and the exact strong integrability range of all possible dominating densities on the fixed pair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit domination in the positive single-channel model, no mixtures of marginal densities and exact strong integrability range on the two-disk pair. |
| argument | [Argument](#argument) | Right creation and its limiting adjoint, original generator commutators, two marginal expectations, critical normalized cutoff norms and decomposition of the successful weight. |
| dependency | [Single-channel vacuum](Yin_C_F0157_v2.md#statement) | Full actual Gaussian condition, positive-amplitude generation and the pure one-edge reciprocal-amplitude vacuum. |
| dependency | [Creation and annihilation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Wick creation row norms, reversal to the right action and bounded separated fields. |
| dependency | [Normal starred values](Yin_C_F0076_v1.md#statement) | The original distinguished derivation kills both omitted normal letters. |
| dependency | [Two-disk construction](Yin_C_F0259_v1.md#argument) | Markov covariance on the two components, strong-star approximation of the singular tests and their canonical slice outputs. |
| dependency | [Semicircular marginal conditional square](Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square) | Uniform positive bound by four times the trace for the conditional expectation of the tests. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0272_v1.md#finding) | The right-creation realization, limiting commutator, two marginal expectations, critical fourth-moment obstruction and all subcritical exponents. |
