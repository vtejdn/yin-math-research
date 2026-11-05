---
author: Yin
---

# Conditional nonsymmetric carrier determinant limits in probability

<a id="scope"></a>
## Scope and unresolved input

This continuing deduction concerns the original finite-variance real Wigner subclass of F0014 and does not claim a full almost-sure Brown theorem.
It is conditional on the arbitrary nonsymmetric shift floor in [D_F0025](Yin_D_F0025.md#in-probability-floor), whose new candidate proof is not treated as adopted here.
The carrier certificate and root-factorization interfaces come from [C_F0186_v7](../claims/Yin_C_F0186_v7.md#statement), but the whole-carrier reversal-symmetry condition is removed below.
The [three-factor conditional assembly](Yin_D_F0011.md#conditional-three-factor-limsup) supplies the preceding special-case argument, with a general fixed number of certified factors replacing its three factors.
This is coordinated project development for Yin, not independent review or a proof of the floor premise.

<a id="floor-premise"></a>
## Exact conditional floor premise

Use normalized real symmetric Wigner inputs with fixed centered variance-one off-diagonal laws and independent fixed finite-second-moment diagonal laws, allowing atoms and arbitrary coupling across dimensions.
For each gamma,B>0, assume that there are A,C,N_0 such that
\[
 \sup_{\max_{ij}|F_{ij}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Floor-premise}
\]
The supremum is over deterministic complex matrices without symmetry assumptions, and constants may depend on the fixed laws, gamma and B.
For an independent random shift the estimate applies conditionally on its polynomial entry guard, whose failure probability is added.
Only convergence to zero of this bound is used, and the displayed second term is not summable.
This is the exact proposed [candidate interface](Yin_D_F0025.md#in-probability-floor), not an extension of the accepted symmetric-shift theorem by fiat.

<a id="statement"></a>
## Enlarged carrier class and conditional conclusions

Let W_1,...,W_d be independent real Wigner inputs within each dimension, in the exact fixed-law finite-second-moment model of [C_F0186_v7](../claims/Yin_C_F0186_v7.md#statement).
Use word reversal without coefficient conjugation under the [accepted convention](../claims/Yin_C_F0186_v6.md#word-reversal).
Fix rev Q=Q for a polynomial Q(x_2,...,x_d), a scalar c in C\{0}, K>=0, and
\[
 T_\nu=x_{j_\nu}+Q_\nu((x_j)_{j\ne1,j_\nu}),
 \qquad 2\le j_\nu\le d,\qquad
 \operatorname{rev}Q_\nu=Q_\nu,\qquad 1\le\nu\le K.
\]
Define
\[
 H=cT_1\cdots T_K,\qquad R=(x_1+Q)H.
 \tag{Carrier}
\]
Take H=c when K=0.
Indices may repeat and factors may share inputs and be dependent, and no reversal symmetry is assumed for H.
Under (Floor-premise), every fixed z in C satisfies
\[
 N^{-1}\log|\det(R(W)-zI)|
 \longrightarrow c_z=\log\Delta_\tau(R(s)-z)
 \quad\hbox{in probability},\qquad c_z\in\mathbb R,
 \tag{Log-probability}
\]
and its limsup equals c_z almost surely under every allowed cross-size coupling.
The conclusions include z=0 and extend to every fixed g(R)-z with g a one-variable polynomial.
The target is finite when g(t)-z is a nonzero polynomial, while an identically zero g(t)-z makes both sides -infinity identically.
No simultaneous event over an uncountable parameter family is asserted.

For every finite ordered product S=prod_(h=1)^q g_h(R_h), where each carrier may use a different relabeling of the same independent inputs, the same probability and every-coupling limsup conclusions hold at zero shift.
The factors may share variables, be dependent and fail to commute.
Its free logarithm is finite when every g_h is a nonzero polynomial.
A zero polynomial factor makes both sides -infinity identically, and the empty product has target zero.
This product assertion alone gives no conclusion for S-z at nonzero z.

<a id="argument"></a>
## Conditional proof

<a id="carrier-guard"></a>
### Certified carrier and arbitrary conditional shift

Fix B>2.
The [accepted polynomial norm guard](../claims/Yin_C_F0186_v6.md#argument) gives polynomial norm bounds for the fixed polynomials used here, with failure O(N^(-B)).
For T_nu, condition on all inputs except W_(j_nu).
The shift Q_nu is independent of that input, complex symmetric and polynomially bounded on its norm guard.
The [accepted symmetric-shift floor](../claims/Yin_C_F0188_v2.md#statement) gives an exponent b_nu with P{s_min(T_nu(W))<N^(-b_nu)}=O(N^(-B)).
A finite union and s_min(AB)>=s_min(A)s_min(B) give an event J_N and exponent b_H such that
\[
 \mathbb P(J_N^c)=O(N^{-B}),\qquad
 s_{\min}(H(W))\ge N^{-b_H},\qquad \|Q(W)\|\le N^{b_H}
 \quad\hbox{on }J_N.
\]
The fixed scalar is absorbed by increasing the exponent, and K=0 has a deterministic inverse bound.
No independence between the factors is required.

Fix z and define F_N=Q(W)-zH(W)^(-1) on J_N, and F_N=0 otherwise.
This measurable shift is independent of W_1 and has a deterministic polynomial norm bound, after increasing its exponent to absorb |z|.
It is generally nonsymmetric.
The floor premise, conditioned on this shift, gives A_z with P{s_min(W_1+F_N)<N^(-A_z)}->0.
On J_N,
\[
 P_N=R(W)-zI=(W_1+F_N)H(W).
 \tag{Factorization}
\]
Thus for some fixed a_z,
\[
 \mathbb P\{s_{\min}(P_N)<N^{-a_z}\}\longrightarrow0.
 \tag{Output-floor}
\]
This estimate is not used as a summable bound.

<a id="middle-and-free-log"></a>
### Polynomial middle range derives the finite free target

Put L=K+1 and q_N=ceil(N^(3/4)).
The [uniform complex-shift intermediate theorem](../claims/Yin_C_F0187_v2.md#statement) applies conditionally to W_1+F_N and separately to each T_nu.
Each failure probability is at most C N^2 exp(-c N^(1/4)), with no norm condition on the shift.
For increasing singular values a_r, the [accepted deterministic product inequality](../claims/Yin_C_F0186_v6.md#argument) is
\[
 a_{r_1+\cdots+r_L-(L-1)}(M_1\cdots M_L)
 \ge\prod_{\nu=1}^La_{r_\nu}(M_\nu)
\]
when the index on the left is at most N.
Distribute k+L-1 among L positive indices differing by at most one.
For k>=2L(q_N+1), each index is in the intermediate range and its predecessor is at least k/(2L).
The factorization gives constants c_0>0 and k_N=2L(q_N+1)=O(N^(3/4)) with
\[
 a_k(P_N)\ge c_0(k/N)^L,\qquad k_N\le k\le N,
 \tag{Output-middle}
\]
outside a summable exception, including J_N^c.
For K=0 use the single-factor inequality with L=1.
This finite union and product argument does not require factor independence.

First Borel--Cantelli makes (Output-middle) eventual almost surely under every allowed coupling.
The [accepted Hermitized weak law](../claims/Yin_C_F0186_v4.md#statement) applies to the original fixed polynomial R-z.
Its limiting singular law nu_z obeys
\[
 \nu_z([0,t])\le C t^{1/L}
 \quad\hbox{for all sufficiently small }t>0.
 \tag{Free-small-mass}
\]
Indeed the finite count is at most k_N+C N t^(1/L), and weak convergence at slightly larger continuity points followed by their decrease to t gives this bound.
It excludes a zero atom and gives finite negative logarithm by integrating nu_z([0,t])/t on (0,1).
The bounded free operator R(s)-z has finite positive logarithm as well.
Consequently c_z is finite before any unregularized logarithmic convergence is used.
No bounded free inverse or general free full-rank theorem is assumed.

<a id="logarithmic-passage"></a>
### Tails in probability and arbitrary-coupling limsup

On the event of (Output-floor) and (Output-middle), the bottom k_N singular values contribute at most a_z k_N log N/N=o(1) to the normalized negative logarithm.
The other values below fixed small t have total contribution at most
\[
 C t^{1/L}(1+|\log t|)+o(1).
\]
Their indices are at most C N t^(1/L), and summing -log c_0+L log(N/k) up to this bound proves the display by the elementary integral estimate for the logarithm.
The good event has probability tending to one, so these tails vanish uniformly in probability as t decreases to zero.
The [accepted positive logarithmic tails](../claims/Yin_C_F0186_v4.md#positive-tail) apply to the fixed polynomial P_N.
For fixed upper and lower cutoffs the clipped continuous logarithm converges by weak convergence.
Removing the cutoffs proves (Log-probability), without convergence of expected unregularized logarithms.

The [accepted regularized upper bound](../claims/Yin_C_F0186_v4.md#regularized-potentials) gives limsup N^(-1)log|det P_N|<=c_z almost surely under every allowed coupling.
Convergence in probability makes P{N^(-1)log|det P_N|<c_z-eta}->0 at each eta>0.
The [arbitrary-coupling marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion) gives equality of this limsup under every coupling.
Equivalently one selects a deterministic subsequence with summable lower deviations and applies first Borel--Cantelli there.
No independence across dimensions or full-sequence summability of (Output-floor) is needed.

<a id="outer-and-product"></a>
### Outer polynomial and ordered-product closures

For nonzero nonconstant g(t)-z, factor it as b prod_(j=1)^r(t-lambda_j), with b nonzero and repeated roots retained.
Finite determinant multiplicativity gives
\[
 N^{-1}\log|\det(g(R(W))-zI)|
 =\log|b|+\sum_{j=1}^{r}N^{-1}\log|\det(R(W)-\lambda_jI)|.
\]
All summands converge in probability to already finite free logarithms, and a finite union bound handles dependence.
The [accepted bounded FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) identifies the sum of targets with log Delta(g(R(s))-z).
A nonzero constant g(t)-z has deterministic logarithm log|b|, and an identically zero polynomial gives the zero matrix at every dimension and at the free limit.
Apply the universal upper bound to the fixed polynomial g(R)-z and then C_F0190_v1 to obtain its limsup conclusion.
One must use probability convergence here, rather than infer a limsup of a sum from the individual limsups.

For S=prod_h g_h(R_h), apply the probability conclusion to each factor at zero shift.
A finite union gives convergence in probability of the sum of log determinants when all targets are finite.
Finite and bounded free determinant multiplicativity identify the finite and limiting sums with the ordered products.
The universal upper bound for the fixed polynomial S and the same marginal criterion give its every-coupling limsup.
The zero-factor and empty-product cases follow directly.

<a id="examples-and-limits"></a>
## Actual enlargement and remaining boundary

Taking Q=0 and H=x_2...x_d includes every fixed ordered product x_1...x_d of distinct independent real Wigner inputs, including three or more factors, at every fixed z.
The factor indices j_nu may repeat within H, which remains independent of W_1 by the exact certificate.
This removes the precise rev H=H restriction identified in [C_F0186_v7](../claims/Yin_C_F0186_v7.md#remaining-boundary).
At zero shift the certified base carrier also has a stronger almost-sure log limit directly from the accepted factorwise floors and intermediate bounds.
The nonsummable vanishing candidate error does not prove full-sequence almost-sure fixed-parameter log convergence at general nonzero z.
No full almost-sure Brown theorem, general matrix-coefficient pencil theorem, or completion of the full F0014 contract is claimed.
The only new probabilistic premise is (Floor-premise), not an additional unproved low-matching hypothesis.
