---
author: Yin
---

# Complex Wigner floors from an independent real additive component

<a id="scope"></a>
## Scope and exact inputs

This is ordinary proof development for the finite-variance determinant Tasks, not independent review or an adopted complex-input theorem.
The [reviewed C_F0186_v10 carrier theorem](../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) remains fixed and real-input only.
The new point is a direct distributional reduction to the [accepted real nonsymmetric-shift floor](../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed), followed by an explicit check of its carrier-proof interfaces.
The other inputs are the [complex Hermitian intermediate theorem](../claims/Yin_C_F0187_v2.md#statement), [finite-variance complex-input weak and logarithmic controls](../claims/Yin_C_F0186_v4.md#statement), [deterministic singular-product inequality](../claims/Yin_C_F0186_v6.md#argument), [arbitrary-coupling marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion), and [ordinary bounded FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
Only these retained exact inputs and elementary conditioning, variance, norm and singular-product calculations are used.
No new external theorem or source-proof inspection is asserted.

<a id="complex-floor-statement"></a>
## A real additive component suffices for the complex floor

Fix a centered complex law \(\xi\) with \(\mathbb E|\xi|^2=1\).
Assume a distributional decomposition
\[
 \xi\ \stackrel{\mathrm d}=a\eta+\theta,
 \qquad a>0,\qquad
 \eta\in\mathbb R,\quad
 \mathbb E\eta=0,\quad\mathbb E\eta^2=1,
 \qquad
 \mathbb E\theta=0,\quad\mathbb E|\theta|^2<\infty,
 \qquad \eta\perp\theta,
 \tag{Real-component}
\]
with fixed laws and fixed real \(a\), independently of dimension.
Here \(\eta\perp\theta\) means statistical independence.
The real and imaginary parts of \(\theta\) need not be independent.
Independence and centering give \(a^2+\mathbb E|\theta|^2=1\), in particular \(a\le1\).
Let \(W_N\) be Hermitian with independent strict upper entries of law \(\xi/\sqrt N\), their conjugates below, and independent real diagonal entries of a fixed centered finite-second-moment law \(\zeta/\sqrt N\).
For every \(\gamma,b>0\), there exist fixed \(A,C_b,C,N_0\), depending on the chosen decomposition, \(\zeta,\gamma,b\), such that
\[
 \sup_{\max_{ij}|F_{ij}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_bN^{-b}
       +C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Complex-floor}
\]
The supremum is over deterministic complex matrices, with no symmetry requirement.
The same estimate holds for a shift \(F_N\) independent of \(W_N\) on its polynomial entry guard, with that guard's complementary probability added.
No density, higher moment or summability of the displayed main error is asserted.
The conclusion is a marginal estimate and makes no assumption about cross-size coupling.

<a id="latent-floor-proof"></a>
## Distributional realization and proof of the floor

Fix one dimension and draw independent copies of the pair \((\eta,\theta)\) for every strict upper coordinate, together with the independent diagonal variables.
Let \(V_N\) be the normalized real symmetric Wigner matrix with upper law \(\eta\) and diagonal law \(\zeta/a\).
Let \(B_N\) be Hermitian with zero diagonal and strict upper law \(\theta/\sqrt N\).
All these choices can be made with \(V_N\) independent of \(B_N\).
The Hermitian matrix
\[
 W_N'=aV_N+B_N
 \tag{Latent-realization}
\]
has exactly the prescribed complete within-dimension law of \(W_N\), including its independent coordinates, diagonal and lower conjugations.
The condition that \(a\) be real is used in both the lower-entry identity and the real diagonal of \(V_N\).

For an arbitrary requested polynomial failure exponent \(b>0\), choose \(K>(b+3)/2\).
The Frobenius calculation and Markov inequality give
\[
 \mathbb E\|B_N\|_F^2
  =(N-1)\mathbb E|\theta|^2\le N,
 \qquad
 \mathbb P\{\|B_N\|>N^K\}
 \le N^{1-2K}\le N^{-b-2}
 \tag{Noise-guard}
\]
for all sufficiently large \(N\).
If \(\theta=0\), the noise guard is deterministic.
On this guard and \(\max|F_{ij}|\le N^\gamma\), choose a fixed
\[
 \Gamma>\max\{\gamma,K\}+1
\]
so that every entry of \((F+B_N)/a\) is at most \(N^\Gamma\) for large \(N\).
Conditional on \(B_N\), the matrix \(V_N\) is still a real Wigner input with its fixed real law and fixed finite-second-moment diagonal law.
Apply C_F0194_v5 with exponent \(\Gamma\) and failure exponent \(b+2\) to
\[
 W_N'+F=a\left(V_N+(F+B_N)/a\right).
\]
It yields a fixed exponent \(A_0\) and the required floor bound at threshold \(aN^{-A_0}\).
Choose \(A>A_0+1\), so \(N^{-A}/a\le N^{-A_0}\) for all sufficiently large \(N\).
Adding (Noise-guard) and absorbing its polynomial term proves (Complex-floor).
This argument keeps the constants uniform over all deterministic shifts in their prescribed guard.

For an independent random \(F_N\), the original joint law of \((W_N,F_N)\) is its product law.
It therefore has the same distribution as \((aV_N+B_N,F_N')\), where \(F_N'\) has the prescribed shift law and is drawn independently of the entire latent pair.
Conditioning on \(B_N,F_N'\) and integrating the uniform real estimate on both guards proves the random-shift assertion.
The event and statistic depend only on \((W_N,F_N)\), so this distributional realization proves the claimed bound for the original pair.
It does not assume that \(F_N\) is independent of latent variables on an already specified realization.
Nor does it require the original coupling across dimensions to carry any latent coordinates.
Only the complete marginal input law at each dimension is used.

<a id="examples-and-phase-boundary"></a>
## Included laws and a phase-line exclusion

If \(\xi=R+iI\) has independent real and imaginary parts and \(\operatorname{Var}R>0\), take
\[
 a=\sqrt{\operatorname{Var}R},
 \qquad \eta=R/a,\qquad\theta=iI.
\]
Centering of \(\xi\) centers both real variables, and this is exactly (Real-component).
Thus the direct floor includes all such fixed finite-variance laws, as well as the real-law case \(a=1,\theta=0\).
It also permits arbitrary dependence between the real and imaginary parts of the residual noise \(\theta\).

A nonreal phase-line law \(\xi=c\eta_0\), where \(\eta_0\) is a nondegenerate real variable and \(\operatorname{Im}c\ne0\), does not satisfy (Real-component).
Indeed define the real linear functional \(L(w)=\operatorname{Im}(\overline c\,w)\).
For the phase-line law \(L(\xi)=0\) almost surely.
An independent decomposition would instead give
\[
 \operatorname{Var}L(a\eta+\theta)
 =a^2(\operatorname{Im}c)^2+\operatorname{Var}L(\theta)>0,
\]
a contradiction.
In particular merely assuming \(\operatorname{Re}c\ne0\) does not give the additive decomposition.
This is a failure of the proposed reduction for such laws, not a counterexample to the floor for every excluded law.
Replacing \(a\) by a general complex scalar would also lose the real symmetric latent matrix identity and is not part of this argument.

<a id="mixed-carrier-statement"></a>
## Carrier transfer with unrestricted complex Hermitian backgrounds

Use the fixed-law complex Hermitian model of the scalar determinant Task, with centered normalized off-diagonal laws of variance \(\mathbb E|\xi_j|^2=1\), independent real centered finite-second-moment diagonal laws, independence within each size, and arbitrary cross-size coupling.
Let \(\mathcal I\) be the set of indices whose off-diagonal laws have a fixed decomposition (Real-component), possibly with different \(a_j,\eta_j,\theta_j\).
Choose a distinguished index in \(\mathcal I\), relabeled as \(1\).
Let \(Q\) be an arbitrary scalar polynomial in the other inputs, and let
\[
 H=cT_1\cdots T_K,\qquad
 T_\nu=x_{j_\nu}+Q_\nu((x_j)_{j\ne1,j_\nu}),
 \qquad j_\nu\in\mathcal I\setminus\{1\},\qquad c\ne0,
 \qquad R=(x_1+Q)H,
 \tag{Mixed-carrier}
\]
with fixed \(K\ge0\) and empty product \(H=c\).
All \(Q_\nu\) are arbitrary fixed scalar polynomials in the displayed allowed variables.
Their nonexposed input indices may have arbitrary complex Hermitian Wigner laws in the Task model and need not lie in \(\mathcal I\).
Repeated distinguished indices, shared variables and dependencies among carrier factors are allowed.
No reversal symmetry is imposed.

The proposed direct transfer gives, for every fixed \(z\in\mathbb C\),
\[
 N^{-1}\log|\det(R(W)-zI)|
 \longrightarrow \log\Delta_\tau(R(s)-z)\in\mathbb R
 \quad\hbox{in probability},
 \tag{Mixed-log-probability}
\]
and equality of its almost-sure limsup with that finite target under every allowed coupling.
The same conclusions hold for each fixed \(g(R)-z\), with finite target if \(g(t)-z\) is a nonzero polynomial and identically \(-\infty\) when \(g(t)-z\equiv0\).
They also hold at zero shift for every finite ordered product of such outer-polynomial outputs, allowing different eligible distinguished indices and shared inputs.
Each nonzero polynomial factor has a finite target; a zero polynomial factor makes the product identically zero, and the empty product has logarithm zero.
No nonzero-shift conclusion for a general ordered product follows just from this product statement.
Two-sided carriers \(H_{\mathrm L}(x_1+Q)H_{\mathrm R}\) have the same conclusions whenever \(H_{\mathrm R}H_{\mathrm L}\) has the displayed mixed certificate.
None of these probability estimates is promoted to a full-sequence almost-sure logarithmic limit or a full Brown theorem.

<a id="transfer-argument"></a>
## Complete interface check for the mixed transfer

The C_F0186_v10 conclusion itself is real-input only, so it is not invoked as a complex-input theorem.
We transfer its [fixed proof](../claims/Yin_C_F0186_v10.md#argument) by the following explicit input substitutions and retain the entire probability-level assembly.

For every fixed polynomial \(A\) of degree \(D\ge1\), the accepted complex-input power-tail estimate in C_F0186_v4 gives
\[
 \mathbb P\{\|A(W)\|>t\}
 \le N\,\mathbb E\mu_{|A(W)|}((t,\infty))
 \le C_A N t^{-2/D}.
\]
Thus every polynomial shift has a fixed polynomial norm guard with any requested polynomial failure exponent, exactly as required in the carrier proof.
Expose each \(W_{j_\nu}\) only after fixing all other input matrices.
Its shift \(Q_\nu(W)\) is independent of that input, and (Complex-floor) applies on this norm guard because \(j_\nu\in\mathcal I\).
The finite union and product lower bound give a fixed \(b_H\) and an event \(J_N\), measurable in the inputs other than \(W_1\), with
\[
 \mathbb P(J_N^c)\to0,\qquad
 s_{\min}(H(W))\ge N^{-b_H},\qquad
 \|Q(W)\|\le N^{b_H}\quad\hbox{on }J_N.
\]
Define \(F_N=Q(W)-zH(W)^{-1}\) there and zero elsewhere.
It is independent of \(W_1\) and has a deterministic polynomial norm bound.
Applying (Complex-floor) to this exposed input gives a fixed \(b_z\) with
\[
 \mathbb P\{s_{\min}(R(W)-zI)<N^{-b_z}\}\to0,
 \qquad
 R(W)-zI=(W_1+F_N)H(W)\quad\hbox{on }J_N.
\]
This uses only distributional floor bounds for the original exposed inputs.
If a latent construction is desired for a conditional application, all other input matrices can be included in the background independent of the latent pair for the currently exposed index, preserving the complete within-size input law.

C_F0187_v2 applies directly to each full complex Hermitian \(W_{j_\nu}\) and to \(W_1\), with their original variance-one laws and arbitrary independent shifts.
It is not applied to the residual noise \(B_j\) as though that noise had variance one.
Writing \(L=K+1\) and increasing singular values as \(a_k\), the same deterministic product inequality yields constants \(c_0,C>0\) and \(k_N\le C N^{3/4}\) such that
\[
 a_k(R(W)-zI)\ge c_0(k/N)^L,\qquad k_N\le k\le N,
\]
on an event of probability tending to one.
The individual intermediate failures are summable, but the output event includes \(J_N\), whose complement need not be summable.

C_F0186_v4 gives the deterministic weak limiting singular law \(\nu_z\) for the original fixed complex-input polynomial \(R-z\).
At every positive continuity point \(t\), its empirical distribution function converges to \(\nu_z([0,t])\) in probability.
The last middle estimate bounds that empirical count by \(k_N/N+C t^{1/L}\) with probability tending to one.
A strict violation \(\nu_z([0,t])>C t^{1/L}\) would contradict these two probability limits.
Decreasing continuity points to arbitrary small \(t>0\) therefore gives \(\nu_z([0,t])\le C t^{1/L}\), excluding a zero atom and proving finite negative free logarithm.
The bounded free operator controls its positive logarithm, so the target is finite without a bounded free inverse assumption.

On the joint floor and middle event, the bottom \(k_N\) normalized negative logarithms contribute at most \(b_z k_N\log N/N=o(1)\).
The other values below \(t\) contribute at most \(C t^{1/L}(1+|\log t|)+o(1)\), by summing the middle bound.
Their common good event has probability tending to one.
Together with C_F0186_v4 weak convergence and positive logarithmic tails, clipping at fixed upper and lower cutoffs and then removing the cutoffs proves (Mixed-log-probability).
Its accepted fixed-regularizer upper bound gives the universal almost-sure limsup upper inequality.
C_F0190_v1 then converts the marginal probability convergence to every-coupling almost-sure upper-limit equality.

For \(g(t)-z=b\prod_\ell(t-\lambda_\ell)\), finite determinant multiplicativity gives the finite sum of base log determinants, and bounded FK multiplicativity identifies its limiting free sum.
All base targets are finite, so a finite union proves probability convergence even with shared inputs.
The universal upper bound and the same marginal criterion give the outer-polynomial limsup assertion.
Constants, repeated roots and the identically zero polynomial are covered directly.
Finite sums and the same two multiplicativities give the ordered-product statement at zero, without commutation or independence between factors.
For the two-sided form, the accepted finite and bounded-free cyclic identities in C_F0186_v4 identify it with \((x_1+Q)H_{\mathrm R}H_{\mathrm L}\) at each nonzero parameter; at zero use ordinary FK multiplicativity.
The finite cyclic identity also holds at zero without inversion.
Root factorization and the same finite-sum argument transfer all the stated outer and product conclusions.
The argument depends on original within-dimension laws and marginal estimates only, so an arbitrary original cross-size coupling need not realize any simultaneous latent decomposition.
