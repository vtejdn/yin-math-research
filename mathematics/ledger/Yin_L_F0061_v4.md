---
author: Yin
---

# Direct Hermitization for fourth-moment Wigner inputs: surviving steps and remaining estimates

This comparison answers Yin's question of 11 November 2026 about extending the repository's GUE proof while bypassing the second eigenvalue moment criterion in [D9](../drafts/Yin_D_F0009.md).
It reuses the exact failures and realification in [v1](Yin_L_F0061_v1.md), the determinant reductions in [v2](Yin_L_F0061_v2.md), and the fourth-moment spectral-gap and norm conclusions in [v3](Yin_L_F0061_v3.md), without replacing their scopes.
The main authoring agent and two parallel read-only agents checked the proof interfaces and the conditional assembly below.
These are ordinary development checks, not an independent project review or an adopted proof of the general Wigner theorem.
The [Gaussian rotation investigation](Yin_L_F0068_v1.md) concerns a separate noise-removal route.

<a id="direct-route"></a>
## What bypassing the disk statistic means

For a fixed scalar polynomial \(P\), write \(A_n=P(W^{(n)})\), \(a=P(s)\), and
\[
 u_n(z)=\frac1n\log|\det(A_n-zI)|,
 \qquad u(z)=\tau\log|a-z|.
\]
The direct route proves convergence of these potentials by controlling singular-value logarithms, then obtains weak Brown-measure convergence from the distributional Laplacian.
It need not use D9's truncated radial-moment lower bound as an input.
On the existing control event, [D9](../drafts/Yin_D_F0009.md#disk-moment) and the [planar logarithmic defect](../claims/Yin_C_F0186_v4.md#remaining-defect) are equivalent tests for the desired convergence.
A successful direct proof consequently implies the D9 lower bound as an output; changing the intermediate statistic does not eliminate the underlying logarithmic defect.

<a id="surviving-steps"></a>
## Exact scope of the transferable steps

| GUE proof component | Wigner status at the present interface |
| --- | --- |
| Word-chain linearization and determinant identity | Algebraic and unchanged for arbitrary input tuples. |
| Hermitized weak limits, fixed regularization and positive logarithmic tails | Already proved for fixed laws with finite second moments in [C186v4](../claims/Yin_C_F0186_v4.md#statement). |
| Compression, quadratic error bound and lifting a near kernel | Deterministic for Hermitian inputs; the [realification in v1](Yin_L_F0061_v1.md#real-gaussian-monic-route) preserves real-symmetric sampling spaces. |
| Gaussian measure of a tube around singular inputs | Requires a new original-law probability estimate; fourth moments do not supply a Gaussian tube bound. |
| Expected singular-value count at a shrinking scale | Now supplied by [C195v1](../claims/Yin_C_F0195_v1.md#decision-count-reviewed) for fixed pencils with finite free logarithm and scalar polynomials under third off-diagonal and second diagonal moments. |
| Concentration of counts and moving clipped logarithms | The [row-block bound in C186v4](../claims/Yin_C_F0186_v4.md#row-concentration) replaces Gaussian concentration, as detailed below. |
| Planar passage and tightness | The [local planar bounds in C186v4](../claims/Yin_C_F0186_v4.md#noncompact-planar) work already under finite second moments, without an eventual operator-norm bound. |

Fourth moments permit the norm approximation and the free spectral-gap case proved in [v3](Yin_L_F0061_v3.md#gap).
They do not control the contribution of a few exponentially small singular values when the free operator has no gap.
The [scalar-shift intermediate-value theorem](../claims/Yin_C_F0187_v1.md#statement) does not cover general matrix-coefficient pencils and does not give a least-value estimate.

<a id="probability-boundary"></a>
## Why the Gaussian probability theorem cannot be copied unchanged

The [GUE tube step](../claims/Yin_C_F0186_v1.md#tubes) combines a deterministic distance-to-singularity implication with a Gaussian mixture of uniform ball measures.
Its geometric source, [Lotz, Theorem 1.1](https://arxiv.org/pdf/1210.3742v4#page=1), controls the probability for a point sampled uniformly from a ball.
The retained [Rademacher polynomial test](Yin_L_F0061_v1.md#atomic-tube-obstruction) has a degree-four polynomial \(q_n\) with \(q_n(0)=1\), yet the product input lies in its zero set surely.
Thus neither a fourth moment nor even bounded entries permits a generic degree-only replacement of the Gaussian tube estimate.
This test does not assert that \(q_n\) is a pencil determinant.

There is also an obstruction for actual monic pencils to a bound that tends to zero with the radius at each fixed matrix size and has no additive error.
For \(n=2^k\), the [symmetric Hadamard realization](Yin_L_F0061_v1.md#discrete-expectation-obstruction) makes \(I-W_n\) singular with positive probability for a Rademacher Wigner law.
Consequently a bound of the form \(\mathbb P\{s_{\min}(I-W_n)\le t\}\le Cn^A t^b\) cannot hold for all sufficiently small \(t>0\).
A Wigner substitute may allow an exceptional probability \(p_n\), for example
\[
 \mathbb P\{s_{\min}(L_n)\le t\}\le Cn^A t^b+p_n,
\]
with \(p_n\to0\) for a probability conclusion or a summable \(p_n\) for the almost-sure assembly below.
This displayed form is a possible sufficient target, not an established estimate or a necessary form.

The full affine fixed-parameter GUE theorem is also too strong a transfer target: the [odd-dimensional real commutator](Yin_L_F0061_v1.md#real-affine-obstruction) is identically singular although its free determinant is positive.
For the Brown-measure application one instead needs the scalar polynomial linearizations for Lebesgue-almost every \(z\).
At \(z\ne P(0)\) their constant coefficient is invertible, so their determinant is nonzero at zero input even on the real-symmetric sampling space.
The commutator example does not refute this narrower route or the Brown convergence conjecture.
The [monic GOE observation](Yin_L_F0061_v1.md#real-gaussian-monic-route) retains the earlier real Gaussian tube adaptation and its then-open count interface.
The [complete reviewed GOE theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) subsequently closed that Gaussian interface, and C195 now transfers its affine count to the stated Wigner laws.

<a id="conditional-small-values"></a>
## A sufficient pair of original-law estimates

Use the fixed-law finite-second-moment Wigner model and its already established controls in C186v4; finite fourth moments are a subclass.
For a fixed nonconstant \(P\) and Lebesgue-almost every fixed \(z\), let
\[
 \nu_{n,z}=\frac1n\sum_{i=1}^n\delta_{s_i(A_n-zI)^2}
\]
be the squared-singular-value law.
Suppose there are constants \(B,\gamma,\beta,\kappa,C>0\), allowed to depend on \(P,z\), such that
\[
 \mathbb P\{s_{\min}(A_n-zI)<n^{-B}\}\longrightarrow0,
 \tag{Floor}
\]
and
\[
 \mathbb E\nu_{n,z}([0,t])\le Ct^\beta+Cn^{-\kappa}
 \qquad(n^{-\gamma}\le t\le1).
 \tag{Count}
\]
Decrease \(\gamma\) if necessary so that \(\gamma<2B\).
No uniform constants in \(z\) are required for the following pointwise argument and Fubini passage.

On the floor event, the negative logarithmic contribution below \(n^{-\gamma}\) is at most
\[
 2B(\log n)\nu_{n,z}([0,n^{-\gamma}]).
\]
Its expectation bound from (Count), without restricting the count to the event, tends to zero.
Layer integration from \(n^{-\gamma}\) to \(\varepsilon\) bounds the remaining expected contribution by
\[
 C\varepsilon^\beta(1+|\log\varepsilon|)
 +C(\log n)(n^{-\gamma\beta}+n^{-\kappa}).
\]
Together with (Floor) this proves negative-log uniform integrability in probability.
The weak Hermitized limit and positive logarithmic tails already in C186v4 therefore give \(u_n(z)\to u(z)\) in probability for almost every \(z\).
In particular (Count) forces a power bound at zero for the free singular law, so its negative logarithm is integrable at these parameters.

For a compact planar disk \(K\), put \(E_{n,\delta}=\{(\omega,z):z\in K,\ |u_n(z)-u(z)|>\delta\}\).
Dominated convergence in \(z\) gives \((\mathbb P\otimes dA)(E_{n,\delta})\to0\).
The uniform expected local \(L^2\) bound in [C186v4](../claims/Yin_C_F0186_v4.md#noncompact-planar) and Cauchy--Schwarz give
\[
 \mathbb E\int_K|u_n-u|\,dA
 \le\delta|K|+C_K(\mathbb P\otimes dA)(E_{n,\delta})^{1/2}.
\]
First sending \(n\) to infinity and then \(\delta\) to zero yields expected local \(L^1\) convergence and weak Brown convergence in probability.
This assembly never integrates the unregularized logarithm on a singular exceptional event at a fixed \(z\).

<a id="non-gaussian-concentration"></a>
## Almost-sure assembly using row blocks instead of Gaussian concentration

Strengthen (Floor) to
\[
 \sum_n\mathbb P\{s_{\min}(A_n-zI)<n^{-B}\}<\infty
 \tag{Summable-floor}
\]
for Lebesgue-almost every fixed \(z\), and keep (Count) unchanged.
The [bounded-variation row-block inequality](../claims/Yin_C_F0186_v4.md#row-concentration), applied to the indicator at \(t_n=n^{-\gamma}\), gives
\[
 \mathbb P\{\nu_{n,z}([0,t_n])-\mathbb E\nu_{n,z}([0,t_n])>n^{-\delta}\}
 \le2\exp(-c n^{1-2\delta})
\]
for any \(0<\delta<\min(\gamma\beta,\kappa,1/2)\).
The bound is summable, so \(\nu_{n,z}([0,t_n])=O(n^{-\delta})\) eventually almost surely.

For any fixed \(K_0>0\), consider
\[
 h_n(x)=\frac12\log\bigl(\max(n^{-\gamma},\min(x,n^{K_0}))\bigr).
\]
Its total variation is \((\gamma+K_0)\log n/2\), so the same inequality gives summable fixed-deviation errors of order \(\exp[-c n a^2/\log^2 n]\).
Apply Borel--Cantelli for \(a=1/k\), \(k\ge1\), to obtain almost-sure convergence of the centered doubly clipped statistics.
The [positive logarithmic tail controls](../claims/Yin_C_F0186_v4.md#positive-tail) and their [almost-sure version](../claims/Yin_C_F0186_v4.md#log-statistics) remove the upper clipping in expectation and almost surely.
Indeed, the removed contribution is at most \(\frac12\int_{x>n^{K_0}}\log x\,d\nu_{n,z}(x)\).
Consequently, for
\[
 V_n(t)=\frac12\int\log\max(x,t)\,d\nu_{n,z}(x),
\]
one has \(V_n(t_n)-\mathbb E V_n(t_n)\to0\) almost surely.
For fixed \(0<\varepsilon<1\), the existing weak limits and positive-tail control give \(\mathbb E V_n(\varepsilon)\to\frac12\int\log\max(x,\varepsilon)\,d\nu_z(x)\).
Also, layer integration and (Count) give
\[
 0\le\mathbb E V_n(\varepsilon)-\mathbb E V_n(t_n)
 \le C\varepsilon^\beta+Cn^{-\kappa}\log n.
\]
Thus \(\mathbb E V_n(t_n)\to u(z)\).
On the eventual floor,
\[
 0\le V_n(t_n)-u_n(z)
 \le B(\log n)\nu_{n,z}([0,t_n])\longrightarrow0.
\]
This proves pointwise almost-sure potential convergence for almost every fixed \(z\).
Fubini, the existing pathwise local planar \(L^2\) bounds, and tightness then give weak Brown convergence almost surely for every allowed cross-size coupling.
No independence between sizes, Gaussian concentration, eventual operator-norm bound, or D9 lower-bound input is used in this conditional assembly.

<a id="remaining-work"></a>
## Exact remaining work

The direct route has a complete conditional continuation once (Floor) and (Count), or (Summable-floor) and (Count), hold for the original-law general polynomial evaluations.
The [reviewed C195 count](../claims/Yin_C_F0195_v1.md#polynomial-transfer) now supplies (Count) for the third-moment subclass, which includes the fourth-moment focus.
Obtaining the original-law least-value floor at the required probability or summability scope remains the unresolved random-matrix problem.
For the two-sided quadratic test, [C196](../claims/Yin_C_F0196_v1.md#decision-incompressibility-reviewed) supplies norm-guarded physical incompressibility and distance averaging, while its actual averaged distance probabilities remain uncontrolled.
An additive singularity error is compatible with this route, while reproducing the GUE unregularized expectation theorem at every fixed shift is unnecessary and can be false for discrete laws.
The spectral-gap case from v3 and the realification from v1 remain useful established partial interfaces, with their original checking limits.
No general finite-fourth-moment least-value floor or completed Wigner Brown theorem is asserted here.
