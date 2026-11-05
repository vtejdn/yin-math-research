---
author: Yin
---

# Nonsymmetric carrier determinant limits in probability

<a id="scope"></a>
## Scope and review boundary

This continuing deduction concerns the original finite-variance real Wigner subclass of F0014 and does not claim a full almost-sure Brown theorem.
It uses the arbitrary nonsymmetric shift floor in [C_F0194_v5](../claims/Yin_C_F0194_v5.md#statement), adopted by its [reviewed decision](../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed) following [independent whole-proof review](../audits/reviews/Yin_R_F0200_v5.md#finding).
The ordered carrier shape and root-factorization interfaces come from [C_F0186_v7](../claims/Yin_C_F0186_v7.md#statement), but all its reversal-symmetry conditions are removed in the proposed carrier statement below.
The [three-factor conditional assembly](Yin_D_F0011.md#conditional-three-factor-limsup) supplies the preceding special-case argument, with a general fixed number of certified factors replacing its three factors.
This is coordinated project development for Yin, and the carrier extension below has not yet received its own formal independent review or adoption.

<a id="floor-premise"></a>
## Exact adopted floor input

Use normalized real symmetric Wigner inputs with fixed centered variance-one off-diagonal laws and independent fixed finite-second-moment diagonal laws, allowing atoms and arbitrary coupling across dimensions.
The adopted input asserts that for each gamma,B>0 there are A,C,N_0 such that
\[
 \sup_{\max_{ij}|F_{ij}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Floor-input}
\]
The supremum is over deterministic complex matrices without symmetry assumptions, and constants may depend on the fixed laws, gamma and B.
For an independent random shift the estimate applies conditionally on its polynomial entry guard, whose failure probability is added.
Only convergence to zero of this bound is used, and the displayed second term is not summable.
This is the exact [adopted fixed interface](../claims/Yin_C_F0194_v5.md#statement), including its [within-dimension independent-random-shift conditioning](../claims/Yin_C_F0194_v5.md#in-probability-floor).
It is not an extension of the accepted symmetric-shift theorem by fiat.

<a id="statement"></a>
## Enlarged carrier class and proposed conclusions

Let W_1,...,W_d be independent real Wigner inputs within each dimension, in the exact fixed-law finite-second-moment model of [C_F0186_v7](../claims/Yin_C_F0186_v7.md#statement).
Fix an arbitrary scalar polynomial Q(x_2,...,x_d), a scalar c in C\{0}, K>=0, and
\[
 T_\nu=x_{j_\nu}+Q_\nu((x_j)_{j\ne1,j_\nu}),
 \qquad 2\le j_\nu\le d,\qquad 1\le\nu\le K,
\]
where every \(Q_\nu\) is an arbitrary fixed scalar polynomial in exactly the allowed other variables.
Define
\[
 H=cT_1\cdots T_K,\qquad R=(x_1+Q)H.
 \tag{Carrier}
\]
Take H=c when K=0.
Indices may repeat and factors may share inputs and be dependent.
No reversal symmetry is assumed for \(Q\), any \(Q_\nu\), or \(H\).
Using (Floor-input), the deduction below gives for every fixed z in C
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

<a id="two-sided-statement"></a>
### Two-sided carriers by cyclic reduction

Let \(H_{\mathrm L},H_{\mathrm R}\) be fixed scalar polynomials in \(x_2,\ldots,x_d\), and suppose their product \(H_{\mathrm R}H_{\mathrm L}\) has exactly the certificate for \(H\) above.
Define
\[
 \widetilde R=H_{\mathrm L}(x_1+Q)H_{\mathrm R},
 \qquad R_0=(x_1+Q)H_{\mathrm R}H_{\mathrm L}.
 \tag{Two-sided}
\]
All the stated probability and every-coupling limsup conclusions hold for \(\widetilde R\), its outer polynomial images, and finite ordered products of those images at zero shift.
Their finite free targets have the same constant-zero exceptions as the preceding statement.
In particular it suffices that each \(H_{\mathrm L}\) and \(H_{\mathrm R}\) separately be a nonzero scalar times a finite ordered product of certified factors \(T_\nu\).
The combined certificate is formed by concatenating the right factors before the left factors and multiplying the two scalars.
All factors still omit \(x_1\), and repeated distinguished indices, shared variables and dependencies between the two sides are allowed.
An empty factor list on either side is permitted.
Neither side nor their product is required to be reversal symmetric.
Only the combined product's certificate is needed for this transfer.

<a id="argument"></a>
## Development argument from the adopted inputs

<a id="carrier-guard"></a>
### Conditional-shift carrier and arbitrary exposed shift

Fix B>2.
The [accepted polynomial norm guard](../claims/Yin_C_F0186_v6.md#argument) gives polynomial norm bounds for the fixed polynomials used here, with failure O(N^(-B)).
For T_nu, first choose a polynomial norm exponent for Q_nu from that guard, and condition on all inputs except W_(j_nu).
The shift Q_nu is independent of that input and satisfies a deterministic polynomial entry bound on its norm guard.
Applying (Floor-input) with that exponent gives a fixed b_nu and
\[
 \mathbb P\{s_{\min}(T_\nu(W))<N^{-b_\nu}\}
 \le C_{\nu,B}N^{-B}
       +C_\nu\sqrt{\log(2+N)}N^{-1/18}
 \longrightarrow0.
 \tag{Factor-floor-probability}
\]
The norm-guard failure is included in \(C_{\nu,B}N^{-B}\), and no symmetry of Q_nu is used.
A finite union and s_min(AB)>=s_min(A)s_min(B) give an event J_N and exponent b_H such that
\[
 \mathbb P(J_N^c)\longrightarrow0,\qquad
 s_{\min}(H(W))\ge N^{-b_H},\qquad \|Q(W)\|\le N^{b_H}
 \quad\hbox{on }J_N.
\]
The fixed scalar is absorbed by increasing the exponent, and K=0 has a deterministic inverse bound.
No independence between the factors is required.
Choose \(J_N\) as the intersection of the displayed carrier-floor and norm events, so it is measurable in \(W_2,\ldots,W_d\) only.
The parameter order is first \(B>2\), then norm exponents for the finitely many \(Q_\nu\), then their floor-input exponents \(b_\nu\), then a norm exponent for \(Q\) and \(b_H\), then a deterministic entry exponent \(\gamma\) for \(F_N\), and finally the floor-input exponent \(A_z\).
Increasing B only improves the polynomial part of the error and does not make the displayed main error summable.

Fix z and define F_N=Q(W)-zH(W)^(-1) on J_N, and F_N=0 otherwise.
This measurable shift is independent of W_1 and has a deterministic polynomial norm bound, after increasing its exponent to absorb |z|.
It is generally nonsymmetric.
The adopted floor input, conditioned on this shift, gives A_z with P{s_min(W_1+F_N)<N^(-A_z)}->0.
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
Write increasing singular values as \(a_r(M)=s_{N-r+1}(M)\).
The [accepted deterministic product inequality](../claims/Yin_C_F0186_v6.md#argument) is
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
on an event of probability tending to one.
The individual intermediate estimates have summable failures, but J_N^c need not be summable, and the factorization is only asserted on J_N.
For K=0 use the single-factor inequality with L=1.
This finite union and product argument does not require factor independence.

The [accepted Hermitized weak law](../claims/Yin_C_F0186_v4.md#statement) applies to the original fixed polynomial R-z.
Its limiting singular law nu_z obeys
\[
 \nu_z([0,t])\le C t^{1/L}
 \quad\hbox{for all sufficiently small }t>0.
 \tag{Free-small-mass}
\]
Indeed let \(F_N(t)\) be the empirical singular distribution function and \(F(t)=\nu_z([0,t])\).
At every positive continuity point \(t\) of \(F\), the accepted weak convergence gives \(F_N(t)\to F(t)\) in probability.
On the event of (Output-middle), \(F_N(t)\le k_N/N+C t^{1/L}\).
If \(F(t)>C t^{1/L}\), choose a fixed positive margin smaller than this gap.
The convergence in probability and \(k_N/N\to0\) would then make the displayed upper bound fail with probability tending to one, contradicting that its event has probability tending to one.
This proves the bound at continuity points.
For arbitrary small positive \(t\), decrease positive continuity points to \(t\) and use continuity from above of the finite measure \(\nu_z\).
The argument uses the deterministic weak limit and marginal probabilities, with no eventual almost-sure middle estimate or cross-size independence.
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

<a id="two-sided-argument"></a>
### Exact finite and free cyclic transfer

For every finite tuple, put \(U=H_{\mathrm L}(W)\) and \(V=(W_1+Q(W))H_{\mathrm R}(W)\).
Then \(UV=\widetilde R(W)\), \(VU=R_0(W)\), and the [accepted finite cyclic identity](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) gives
\[
 \det(\widetilde R(W)-zI)=\det(R_0(W)-zI)
 \qquad(z\in\mathbb C).
 \tag{Finite-cyclic}
\]
It requires no inverse of either side, including at \(z=0\).
The same accepted block-Schur argument gives
\[
 \Delta_\tau(uv-z)=\Delta_\tau(vu-z)
 \qquad(z\ne0)
 \tag{Free-cyclic}
\]
for the corresponding bounded free elements \(u,v\).
At zero, ordinary bounded FK multiplicativity supplies \(\Delta_\tau(uv)=\Delta_\tau(u)\Delta_\tau(v)=\Delta_\tau(vu)\), also when a determinant vanishes.
The preceding deduction for \(R_0\) therefore transfers its finite target, logarithmic limit in probability and almost-sure upper-limit equality to \(\widetilde R\) at every fixed \(z\).
This transfer does not claim equality of singular-value distributions or a least-singular-value floor for the two cyclic forms.
Factoring any nonconstant scalar \(g(t)-z\) over its finitely many roots, as in the preceding outer-polynomial argument, transfers the exact finite determinant and free determinant identities to \(g(\widetilde R)-z\).
Constants and the identically zero polynomial have their already stated direct meanings.
The same finite-sum argument proves the ordered-product conclusion, without asserting a nonzero-shift identity for a general ordered product.

<a id="one-occurrence-boundary"></a>
### A single distinguished occurrence is not a general sum of sandwiches

This extension covers a single factorization \(H_{\mathrm L}(x_1+Q)H_{\mathrm R}\) with the stated certificate, rather than every polynomial of degree one in \(x_1\).
For the free algebra \(\mathcal A=\mathbb C\langle x_2,\ldots,x_d\rangle\), the terms containing exactly one \(x_1\) identify uniquely with \(\mathcal A\otimes\mathcal A\) by \(a x_1 b\leftrightarrow a\otimes b\).
A single sandwich has coefficient tensor \(H_{\mathrm L}\otimes H_{\mathrm R}\) of rank at most one.
For example, with \(d\ge3\), \(x_2x_1+x_1x_3\) has tensor \(x_2\otimes1+1\otimes x_3\) of rank two, since both pairs of displayed left and right words are linearly independent.
It therefore has no such single-sandwich representation for this distinguished \(x_1\), regardless of the independent term \(Q\).
This algebraic boundary is not a determinant counterexample and does not exclude other methods or choices of distinguished input.

<a id="symmetric-special-case"></a>
### Previously accepted stronger symmetric special cases

Use the [accepted reversal convention](../claims/Yin_C_F0186_v6.md#word-reversal), which does not conjugate scalar coefficients.
If \(Q\), every \(Q_\nu\), and the whole \(H\) are reversal symmetric, the [reviewed carrier theorem](../claims/Yin_C_F0186_v7.md#statement) already proves full almost-sure fixed-parameter logarithmic limits and the stated Brown limits at its actual scope, independently of (Floor-input).
If \(Q\) and every \(Q_\nu\) are reversal symmetric but \(H\) is not, their separate accepted symmetric-shift floors still give a full almost-sure zero-shift log limit for the base carrier.
Indeed at zero its exact factorization is the finite product of \(W_1+Q(W)\) and the \(T_\nu(W)\), each with a summable polynomial floor and summable intermediate failure.
The deterministic product inequalities then give the bottom and middle negative-logarithmic bounds already proved in the accepted carrier argument, and C_F0186_v4 supplies weak convergence and positive tails.
The exact cyclic identities transfer that zero-shift log limit to the two-sided form.
These stronger special cases do not supply full almost-sure convergence for the new arbitrary-\(Q_\nu\) class, and no such strengthening is inferred from its nonsummable carrier guard.

<a id="examples-and-limits"></a>
## Actual enlargement and remaining boundary

Taking Q=0 and H=x_2...x_d includes every fixed ordered product x_1...x_d of distinct independent real Wigner inputs, including three or more factors, at every fixed z.
The factor indices j_nu may repeat within H, which remains independent of W_1 by the exact certificate.
This removes the precise rev H=H restriction identified in [C_F0186_v7](../claims/Yin_C_F0186_v7.md#remaining-boundary) and also permits arbitrary additive shifts in the carrier factors and the exposed first factor.
The adopted floor's nonsummable vanishing error does not prove full-sequence almost-sure fixed-parameter log convergence at general nonzero z.
No full almost-sure Brown theorem, general matrix-coefficient pencil theorem, or completion of the full F0014 contract is claimed.
The probabilistic floor used here is the adopted (Floor-input), with no additional unproved low-matching hypothesis; the carrier extension itself remains unreviewed proof development.
