---
author: Yin
---

# Finite-variance block pencils, intermediate singular values and the remaining bottom logarithm

This continuing investigation concerns the general fixed-matrix-coefficient [F0013 contract](../tasks/Yin_T_F0013_v1.md#contract) and its distinct relationship to the nonselfadjoint [F0012 contract](../tasks/Yin_T_F0012_v3.md#contract).
The fixed [spectral and planar controls](../claims/Yin_C_F0186_v4.md#statement), [Hermitian intermediate bound](../claims/Yin_C_F0187_v2.md#statement), [complex symmetric shift argument](../claims/Yin_C_F0188_v2.md#argument) and [conditional-shift polynomial deduction](../claims/Yin_C_F0186_v6.md#argument) retain their own exact assessments and review boundaries.
The general matrix-coefficient pencil problem is not discharged by those scalar conditional shifts.
The [fixed frontier](../ledger/Yin_L_F0061_v1.md) owns the finite-variance moment counterexamples, atomic and real-affine obstructions, and inspected source scope.

<a id="negative-logarithmic-gap"></a>
## A floor and qualitative weak convergence do not suffice

Put \(r_n=1/\sqrt{\log n}\), for sufficiently large \(n\), and consider the deterministic probability measures
\[
 \nu_n=(1-r_n)\delta_1+r_n\delta_{n^{-A}},\qquad A>0.
\]
Then \(\nu_n\Rightarrow\delta_1\), and every support point is at least \(n^{-A}\), but
\[
 \int_{(0,1)}|\log t|\,d\nu_n(t)=A\sqrt{\log n}\longrightarrow\infty.
\]
This disproves the inference from a polynomial floor and qualitative weak singular convergence to negative logarithmic uniform integrability.
It is not a Wigner counterexample.
The distinction explains why the intermediate estimate is a necessary separate input to the presently closed scalar-shift mechanisms.

## Actual block inputs and remaining questions

For the exact corner-parameter linearization of \(P(W)-z\), retain the fixed auxiliary dimension and the actual coefficient and minor relations in
\[
 L_N(z)=A_0(z)\otimes I_N+\sum_j A_j\otimes W_j^{(N)}.
\]
The scalar shift theorem exposes an independent row with independent scalar coordinates and a quadratic cofactor expression.
A physical block row of this pencil has correlations imposed by the matrices \(A_j\), and its block determinant can have a higher fixed degree in the exposed variables.
The scalar inverse Littlewood--Offord argument and the scalar distance-to-subspace variance cannot be applied without proving the corresponding block statements.

Irreducibility of the coefficient algebra does not give the missing one-step covariance bound when \(\chi_R=0\), as the [existing exact covariance criterion](../ledger/Yin_L_F0058_v2.md#covariance-boundary) shows.
A Schur argument must also retain the structure of an actual minor, because the [arbitrary-minor conditional estimate is false](../ledger/Yin_L_F0059_v1.md#schur-findings).
The [reviewed positive-frame block theorem](../claims/Yin_C_F0187_v3.md#decision-block-intermediate-reviewed) now controls the intermediate range under its explicit additional coefficient-frame hypothesis and derives a finite free logarithm.
Its [actual projection and elimination boundaries](../claims/Yin_C_F0187_v3.md#actual-projected-block-failure) show why that hypothesis does not follow from a finite free target, irreducibility, constant auxiliary basis changes or the usual word-chain linearization.
The remaining questions are a quantitative actual-minor mechanism for degenerate coefficient families and the [bottom logarithmic contribution](../claims/Yin_C_F0187_v3.md#block-mesoscopic-log), which is still uncontrolled even by the positive-frame intermediate result.
For F0012, success must imply the [exact defect condition](../claims/Yin_C_F0186_v4.md#remaining-defect).
For F0013, a suitable dimensional subsequence with negligible bottom logarithm in probability may suffice under the [coupling criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion); a new polynomial floor alone is insufficient by the example above.

<a id="constant-row-deflation"></a>
## Exact removal of deterministic auxiliary rows and columns

The following elementary reduction retains the constant coefficient rather than deleting its physical columns.
It is ordinary exploratory proof development for Yin on 2026-11-05, not an independent review or a new adopted Claim.
It uses fixed linear algebra and the accepted [bounded unitriangular FK identity](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction), and makes no assumption that \(A_0\) is invertible.

Let
\[
 K_{\mathrm L}:=\bigcap_{j=1}^d\ker A_j^*,\qquad q:=\dim K_{\mathrm L}>0,
\]
and choose an \(m\)-by-\(q\) matrix \(U\) whose orthonormal columns span \(K_{\mathrm L}\).
If \(\operatorname{rank}(U^*A_0)<q\), a nonzero linear combination of these rows annihilates every coefficient including \(A_0\).
Every finite evaluation then has a fixed left nullspace, and the free evaluation has a nonzero kernel projection for its adjoint.
Finite-trace polar decomposition gives the same kernel trace for the operator and its adjoint, so both determinant logarithms are identically \(-\infty\).
This branch resolves the equality for that coefficient tuple without a small-value estimate.

If \(\operatorname{rank}(U^*A_0)=q\), put \(r:=m-q\).
Choose a fixed invertible column change \(T\) satisfying \(U^*A_0T=(0\ I_q)\), and complete \(U^*\) to the bottom \(q\) rows of a fixed invertible row change \(S\).
Then, for every input tuple in any unital algebra,
\[
 S L(x)T
 =\begin{pmatrix}B(x)&C(x)\\0&I_q\end{pmatrix},
 \qquad
 B(x):=B_0+\sum_jB_jx_j,
 \tag{Deterministic-strip}
\]
where \(B\) has size \(r\) and both displayed nonconstant blocks remain affine in the original inputs.
The lower block identity follows directly from \(U^*A_j=0\) for \(j\ge1\) and the chosen column change.
No actual random minor is inverted and no products of random inputs are generated.

Let \(\kappa:=m^{-1}\log|\det S\det T|\).
For \(r>0\), the exact finite and free identities are
\[
 \frac1{mN}\log|\det L_N|
 =\frac rm\,\frac1{rN}\log|\det B_N|-\kappa,
 \qquad
 \log\Delta_{\tau_m}(L)
 =\frac rm\log\Delta_{\tau_r}(B)-\kappa.
 \tag{Deflated-log}
\]
The first follows from the ordinary triangular determinant.
For the second, factor the displayed block matrix as an upper unitriangular matrix times \(\operatorname{diag}(B,I_q)\), and use bounded multiplicativity and the normalized block trace.
Both identities include zero determinants.
When \(r=0\), the reduced block is empty and its displayed logarithmic contribution is zero.
Thus the original determinant-limsup question is exactly equivalent to the smaller affine question, with unchanged entry laws and cross-size coupling, unless it was already resolved by the nullspace branch.
The corresponding column reduction applies to \(K_{\mathrm R}:=\bigcap_{j=1}^d\ker A_j\), with fixed row and column changes in the opposite order.

For reference, when \(r>0\) the same factorization gives
\[
 s_{\min}(L_N)
 \ge c_{S,T}\,
 \frac{\min\{s_{\min}(B_N),1\}}{1+\|C_N\|}.
\]
The finite-second-moment Frobenius bound supplies polynomial norm guards for the affine block \(C_N\).
Consequently a polynomial floor for the smaller pencil transfers, but the exact determinant identity is preferable here because it does not lose a factor at every controlled singular index.

Repeated left or right reductions strictly decrease the auxiliary size.
They terminate at a constant block, a fixed nullspace, or a smaller pencil with both common noise kernels zero.
This is a finite preprocessing reduction, not a claim that the final pencil has positive frame.
For instance,
\[
 \begin{pmatrix}W_1&I&W_2\\I&0&0\\0&0&W_3\end{pmatrix}
\]
has a singular constant coefficient and determinant \((-1)^N\det W_3\); the deterministic second auxiliary row is removed by the reduction, after which a deterministic column leaves only \(W_3\).
The two other input directions do not enter its determinant.

<a id="mixed-factor-coding-obstruction"></a>
## A two-dimensional residual pencil and loss of all conditional noise

The deterministic-strip reduction cannot address every remaining coefficient degeneracy.
Set \(\alpha:=\sqrt2\), take \(K>0\), and consider
\[
 A_1:=I_2,\qquad A_2:=\operatorname{diag}(1,\alpha),\qquad
 A_0:=K\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
\[
 L_N=
 \begin{pmatrix}X_N&KI_N\\KI_N&Y_N\end{pmatrix},
 \qquad X_N:=W_1+W_2,\qquad Y_N:=W_1+\alpha W_2.
 \tag{Mixed-factor-pencil}
\]
Both noise coefficients are invertible, so both common noise kernels vanish and remain zero under fixed invertible left and right coefficient changes.
In particular no such change can create a completely deterministic row or column to start the preceding reduction.
The coefficient algebra including \(A_0\) is the full matrix algebra: the distinct diagonal entries of \(A_2\) give the two diagonal matrix units, and multiplication by \(A_0/K\) gives the off-diagonal ones.
Nevertheless \(e_1^*A_je_2=0\) for both noise coefficients, so \(\chi_A=0\).

Swapping the two auxiliary columns gives a constant invertible diagonal pivot \(KI_N\), and hence
\[
 \det L_N=\det(Y_NX_N-K^2I_N).
 \tag{Mixed-product}
\]
The same bounded block factorization gives
\[
 \log\Delta_{\tau_2}(L)
 =\tfrac12\log\Delta_\tau(yx-K^2),
 \qquad x:=s_1+s_2,\quad y:=s_1+\alpha s_2.
\]
Neither identity requires invertibility of \(X_N\), \(Y_N\), \(x\) or \(y\).
At \(K=6\), the free pencil is boundedly invertible, since the noise block has norm at most \(2(1+\sqrt2)<6\), while the constant swap has least singular value six.
Thus this example has a finite free logarithm without any further free regularity theorem.

Now let both input laws be independent symmetric signs and let both diagonals be zero.
For each strict upper coordinate, \(\sqrt N(Y_N)_{ab}\) takes the four distinct values
\[
 1+\alpha,\quad1-\alpha,\quad-1+\alpha,\quad-1-\alpha.
\]
Each value uniquely identifies both original signs.
Consequently \(\sigma(Y_N)=\sigma(W_1,W_2)\), and the conditional law of \(X_N\) given \(Y_N\) is a point mass.
There is no residual independent Wigner noise available after that conditioning.
In contrast, the unconditional covariance matrix of one raw real pair \((X,Y)\) is
\[
 \begin{pmatrix}2&1+\alpha\\1+\alpha&1+\alpha^2\end{pmatrix},
 \qquad \det=(\alpha-1)^2>0.
\]
Thus even a nonsingular covariance matrix of the mixed entries, invertible individual noise coefficients, full coefficient algebra and a finite free target do not justify the proposed conditional-noise step.
This is a failure of conditioning on a mixed factor, not a counterexample to the determinant question or to conditioning on an original independent input.
It is distinct from the earlier observation that coefficient products alone do not manufacture independent noise: here an exact scalar-product reduction exists, but the natural conditioning destroys all of the randomness one hoped to expose.

<a id="original-input-quadratic-test"></a>
## The next discriminating test keeps the original independent input

For the residual pencil above, condition on the original \(B_N:=W_2\), leaving \(W_1\) independent.
The exact scalar problem is then
\[
 Q_N:=(W_1+\alpha B_N)(W_1+B_N)-K^2I_N
 =W_1^2+W_1B_N+\alpha B_NW_1+\alpha B_N^2-K^2I_N.
 \tag{Original-input-quadratic}
\]
This is a quadratic expression in the exposed Wigner matrix, and its two mixed terms have unequal coefficients.
The displayed factorization does not satisfy the existing carrier certificate: the right factor still contains the very input being exposed in the left factor, so the independent-background requirement fails.
The [latent additive-component argument](Yin_D_F0028.md#latent-floor-proof) does not repair the coding obstruction, because it requires a genuinely independent residual component rather than one recovered from the conditioned factor.

A useful first test is to determine whether the accepted scalar internal-row/cofactor mechanism extends to this fixed quadratic expression while retaining the actual conditioned \(B_N\) and both occurrences of each exposed variable.
One may start with real inputs and fixed nonzero \(K\), seeking a polynomial least-value floor in probability uniformly on polynomial norm guards for the actual independent \(B_N\), or identify a concrete obstruction to that uniformity.
This is an unresolved estimate, not supplied by the determinant identity or by the invertibility of \(A_1\).
It should be tested on parameters without a deterministic free spectral gap; \(K=6\) above only certifies that the conditional-coding obstruction persists even at a finite free target.
Even success on a polynomial floor must be accompanied by a middle-range or direct bottom-log bound before the general F0013 lower limit follows.

The allocation recommendation is therefore to use deterministic-strip removal as finite preprocessing and test the quadratic original-input problem on the smallest residual pencil.
A flag algorithm restricted to fixed basis changes and deterministic full-row or full-column pivots is already unable to start on this example.
This recommendation does not exclude a more elaborate decomposition or a multistep random exposure.
The new material supplies exact reductions and a conditioning obstruction; it supplies no new general least-value floor, positive-frame bottom-log estimate or completion of F0013.

## The fixed conditional obstruction

The [complete actual-minor counterexample](../ledger/Yin_L_F0066_v5.md#actual-minor-singular-atom) has conditional singularity probability one half despite bounded actual minors and inverses.
Its [free-target certificate](../ledger/Yin_L_F0066_v5.md#identity-direction-free-density) gives a finite logarithm at the same fixed coefficients and laws.
The [rare-event boundary](../ledger/Yin_L_F0066_v5.md#actual-minor-allocation-boundary) redirects the continuing question to typical minors or to retaining more independent border coordinates, without refuting an unconditional Task.

<a id="typical-minor-energy-matching"></a>
## A conditional energy-to-matching test for typical minors

A complementary strategic calculation isolates a sufficient condition that avoids a new comparison theorem for low-influence polynomials.
A bounded strategic source comparison on 2026-11-05 inspected [Mossel--O'Donnell--Oleszkiewicz, arXiv v2, Theorems 2.1--2.2](https://arxiv.org/html/math/0503503v2#S2.SS1) as a Gaussian-comparison lead.
That comparison did not establish the actual conditional coefficient-energy or load hypotheses needed here, so no result from that source is invoked in the following deduction.
The retained test instead uses the already accepted fixed-degree matching estimate below; it remains a proposed typical-minor mechanism.
Its sole probabilistic input is the accepted [MNV16 Theorem 1.6 interface](../audits/literature/MNV16/Yin_U001.md#matching-rank), for real multilinear polynomials in independent fair signs at any fixed degree, with arbitrary constant and lower-degree terms.
The source's original proof remains accepted at the inspection scope retained in that U; this argument adds only the following coefficient-energy and greedy-selection calculation.

Let
\[
 p(\varepsilon)=\sum_{S\subseteq[n],\ |S|\le D}c_S\varepsilon_S,
 \qquad \varepsilon_S:=\prod_{i\in S}\varepsilon_i,
\]
be the exact multilinear representation on the sign cube, with \(D\ge1\) its highest nonzero degree and \(c_S\in\mathbb C\).
Put
\[
 \sigma_D^2:=\sum_{|S|=D}|c_S|^2>0,\qquad
 \tau_D:=\frac{\max_i\sum_{\substack{|S|=D\\i\in S}}|c_S|^2}
                      {\sigma_D^2}.
 \tag{Top-layer-energy-load}
\]
For real coefficients, discard the degree-\(D\) coefficients of modulus less than
\(\lambda=\sigma_D/(\sqrt2\,n^{D/2})\).
There are at most \(n^D\) such monomials, so the discarded squared energy is at most \(\sigma_D^2/2\).
Choose one retained \(D\)-set and delete all retained sets meeting it, continuing greedily until none remain.
Each choice deletes at most
\(D\tau_D\sigma_D^2\)
of the original squared energy, because the sum of the coordinate loads over the chosen set bounds that deleted energy.
The chosen disjoint sets consequently number at least \(1/(2D\tau_D)\), with integer rounding downward allowed in a lower bound.
Their coefficients all have modulus at least \(\lambda\).

For complex coefficients, choose the real or imaginary projection whose degree-\(D\) squared energy is at least \(\sigma_D^2/2\).
In that projection, discarding coefficients smaller than
\[
 \lambda:=\frac{\sigma_D}{2n^{D/2}}
\]
loses at most \(\sigma_D^2/4\), leaving at least that much energy.
Its individual coordinate loads are at most the original \(\tau_D\sigma_D^2\).
The same argument yields at least
\[
 r:=\left\lfloor\frac1{4D\tau_D}\right\rfloor
 \tag{Energy-matching-rank}
\]
disjoint degree-\(D\) coefficients of projected modulus at least \(\lambda\).
Whenever \(r\ge2\) and \(2\rho<\lambda\), the disk event \(|p-z|\le\rho\) is contained in an interval of length less than \(\lambda\) for this real projection.
Scaling it by \(\lambda\) and using the first MNV16 bound gives, uniformly over its center \(z\in\mathbb C\),
\[
 \mathbb P\{|p-z|\le\rho\}
 \le C_D\sqrt{\log r}\,r^{-1/(4D+1)}.
 \tag{Energy-matching-small-ball}
\]
No coefficient bound is imposed on lower-degree terms, and no union over possible monomial matchings is taken.

For a conditional row calculation, let \(a_N>0\) be a scale measurable in the conditioned variables, let \(n\le cN\), and let the actual degree satisfy \(1\le D\le D_0\) for a fixed \(D_0\).
If, on a good conditioning set,
\[
 \sigma_D\ge N^{-A}a_N,\qquad \tau_D\le t_N\longrightarrow0,
 \tag{Typical-top-layer-obligation}
\]
then choosing \(B>A+D_0/2+1\) makes \(\rho=N^{-B}a_N\) meet the interval requirement for all sufficiently large \(N\).
The conditional small-ball probability in (Energy-matching-small-ball) tends to zero uniformly on that good set.
If the complement's probability also tends to zero, integration supplies an unconditional \(o(1)\) estimate for this polynomial small-ball event.
An upper bound on the bad-set probability, the displayed energy and load hypotheses, and conversion of the matrix event to that polynomial event are new obligations, not consequences of MNV16.
Its first displayed rate need not be summable, even for a matching of order \(N\), and it cannot be multiplied by \(N\) in a naive union over physical rows.
Thus this criterion is initially suited to a probability estimate and the F0013/F0014 subsequence route; F0012 still needs its stronger full-sequence conclusion.

For the real two-channel pencil with an invertible physical minor, entries of its \(2\)-by-\(2\) Schur complement have degree at most two in the exposed original row, so its determinant has degree at most four before restriction to atomic support.
Repeated powers must first be reduced using the exact support or an actually justified conditional fair-sign representation; formal polynomial degree or nonzero coefficients before that reduction do not give (Top-layer-energy-load).
After two-copy conditioning for more general real or complex entry laws, any needed spread in the newly random coefficient array must also be proved; the exact quadratic precedent is [C_F0194_v3](../claims/Yin_C_F0194_v3.md#two-copy-matching), not a blanket higher-degree extension.
The true highest nonzero layer may have degree one, two or three, and degree zero needs a separate deterministic-distance test.
Moreover, the normalization \(a_N\) must be related to the actual matrix small-distance event, including Schur denominators, graph normalization and the other singular factors; an unnormalized determinant coefficient alone supplies no floor.

In the [fixed bad atom](../ledger/Yin_L_F0066_v5.md#actual-minor-singular-atom), with alpha and t specified there, restriction to the sign cube gives exactly
\[
 \det L_N=(-1)^N\frac{2(1+\alpha)^2t^2}{N^2}(1-\varepsilon_1).
\]
All formal quartic and quadratic layers have disappeared, the highest layer has degree one and \(\tau_1=1\), and its conditional singular atom is consistent with the failure of (Typical-top-layer-obligation).
The resulting allocation is therefore to test top-layer energy and coordinate-load spread on typical actual minors, accounting for bad-minor probability and all degree fallbacks, rather than to seek a conditional floor uniform over every actual minor.
This is a concrete sufficient mechanism and a matching obstruction, not a proof that the required typical-minor hypotheses hold for the original pencil.

The [single-input coefficient calculation](Yin_D_F0033.md#all-sign-layers) now supplies every exact sign layer for this actual two-channel Schur determinant.
Its [row-load estimate and off-diagonal Gram test](Yin_D_F0033.md#offdiagonal-gram-test) reduce the bounded-inverse fourth-layer branch to a concrete noncancellation condition, while [distinct inverse modes](Yin_D_F0033.md#distinct-inverse-modes) explain why the square of one dominant inverse pole is not the correct general normalization.
The [single-pole residual criterion](Yin_D_F0033.md#single-pole-residual-test) supplies an explicit energy and load alternative for an unbounded dominant mode, with auxiliary direction, cross-energy and matrix-distance obligations retained.
The [reviewed bounded two-channel theorem](../claims/Yin_C_F0187_v4.md#decision-bounded-two-channel-reviewed) supplies its physical-leverage and residual row-spread inputs for the stated real bounded K=1 model, uniformly over single physical deletions and removed modes on the invertible branch.
The cross fourth-layer energy is now supplied by the fixed theorem below, while pole dominance, singular minors and the bottom logarithm remain separate obligations.
The [two-original-row test](Yin_D_F0032.md#general-minor-bridge) keeps both inputs random and controls the formerly obstructing cancelling minor, with a [finite-variance probability floor](Yin_D_F0032.md#finite-variance-two-row-floor) and a [bounded-law neighbourhood](Yin_D_F0032.md#near-cancelling-minors).
Its [coefficient resonance](Yin_D_F0032.md#two-row-critical-boundary) retains a nonsummable conditional singular atom at another fixed coupling, so neither the extra row nor the coefficient formulas alone supply the required general typical-minor estimate.
The [reviewed two-original-sign-row theorem](../claims/Yin_C_F0194_v12.md#decision-two-original-row-reviewed) now covers every actual bounded-inverse minor with its small real exposed-diagonal guard through exhaustive constant, quadratic and quartic alternatives.
It retains the fixed inverse bound and nonsummable failure rate; the probability of that guard and the original logarithmic conclusions are not supplied by this conditional result.
The [explicit inverse-growth calculation](Yin_D_F0032.md#polynomial-minor-inverse-guard) extends the developing conditional argument to inverse bounds N^kappa with kappa<1/4 and retains the resulting normalization loss.
The [fixed-scale spectral-mass deduction](Yin_D_F0032.md#fixed-guard-at-zero-bulk) shows that every fixed inverse guard is atypical at the actual bounded K=1 bulk point, preventing direct unconditional use of that guarded theorem.
The graph normalization and complete assembly below address this obstruction without such a fixed inverse guard.
The [reviewed auxiliary Gram and cross-energy theorem](../claims/Yin_C_F0187_v5.md#decision-auxiliary-cross-energy-reviewed) now derives the all-mode Gram gap and uses the actual inverse identities to prove closest-mode cross-layer noncollapse in the bounded real model.
Its [generic residual kernel](../claims/Yin_C_F0187_v5.md#generic-kernel-statement) still excludes deriving this conclusion from the abstract spread properties alone.
The fixed results below now cover all inverse-mode regimes, match the coefficient scale to matrix distance and complete the logarithmic assembly for bounded real off-diagonal laws and finite-second-moment real diagonals.
The [continuing zero classification and actual-pencil sign example](Yin_D_F0033.md#homogeneous-inverse-zero-locus) distinguish raw polynomial vanishing from collapse after restriction to atomic support, retaining the exact typicality conditions that the example violates.

<a id="two-channel-block-averaging"></a>
## Fixed physical averaging and graph normalization

The complete physical-block argument is retained in [C194v13](../claims/Yin_C_F0194_v13.md#block-averaging), using the fixed shifted-rectangle input C194v3.
Its averaging step applies to every fixed centered variance-one real first off-diagonal law of finite second moment and an arbitrary independent real symmetric second input, on the stated full-matrix norm guard.
It covers every full corank and does not require invertibility of a retained principal minor.
The separate fourth-layer small-ball bridge in that Claim requires an actual Rademacher first row and its explicit coefficient/graph conditions.

The [reviewed general reduction](../claims/Yin_C_F0194_v13.md#decision-graph-energy-reviewed) gives matrix scale \(c b_N^{-2}N^{-5}\) when those conditions hold on the norm guard \(\|L_N\|\le b_N\).
Its [combined bounded-model consequence](../claims/Yin_C_F0194_v13.md#combined-branch-statement) uses the [reviewed whole-layer high-rank theorem](../claims/Yin_C_F0187_v6.md#statement) together with the dominant-mode cross-energy argument.
That v13 consequence retains an average of singular physical minors and invertible minors having both bounded effective inverse rank and insufficient single-mode dominance.
It does not estimate that average within v13; the subsequent mode estimates and whole-parent shift below complete the bounded-model argument.

The [reviewed operator-gap theorem](../claims/Yin_C_F0187_v9.md#decision-operator-gap-reviewed) weakens Frobenius dominance to separation in inverse operator norm at bounded effective rank.
The [reviewed comparable-mode theorem](../claims/Yin_C_F0187_v9.md#decision-comparable-modes-reviewed) completes the remaining invertible regimes, leaving the singular-minor average in its matrix consequence.
The balanced-kernel intermediate theorem below supplies the negative-logarithmic range that a polynomial floor alone would not control.
The coefficient directions \(A_1=I_2,A_2=\operatorname{diag}(1,\sqrt2)\) have \(\chi_A=0\), since \(u=e_1,v=e_2\) annihilate both matrix coefficients in the [fixed frame definition](../claims/Yin_C_F0187_v3.md#statement).
Thus the positive-frame theorem does not supply that input; the separate balanced-kernel argument below is required.
General coefficient tuples, the original finite-second-moment laws and the full-sequence planar conclusion retain their separate obligations.

<a id="balanced-two-channel-middle"></a>
## Fixed balanced-kernel intermediate theorem

The complete bounded real two-channel theorem is retained in [C187v9](../claims/Yin_C_F0187_v9.md#statement), with [independent adoption](../claims/Yin_C_F0187_v9.md#decision-balanced-middle-reviewed).
For every fixed \(D>0\), it gives \(s_{2N-j}(L_N)\ge cj/N\) simultaneously for \(j\ge4\lceil A_D\log N\rceil\), outside probability \(C_DN^{-D}\).
It requires no Rademacher law and derives channel balance from the actual retained kernel despite the zero one-step coefficient frame.

<a id="strong-tall-two-channel-rectangles"></a>
### Thin physical rectangles

The [fixed thin-rectangle proof](../claims/Yin_C_F0187_v9.md#strong-tall-two-channel-rectangles) uses bounded fourth moments, independent row indicators and a small-aspect sphere net.
It gives a constant least singular value uniformly over the required rectangles outside exponentially small failure.
The norm event is used only to extend the net, not to condition the fresh distribution.

<a id="actual-kernel-channel-balance"></a>
### Actual kernel balance

The [fixed kernel argument](../claims/Yin_C_F0187_v9.md#actual-kernel-channel-balance) uses both identity-coupled block equations and the two cross rectangles.
Each channel carries a fixed fraction of every projected kernel vector's squared norm, with no invertibility or row-rank assumption.

<a id="balanced-fresh-row-distance"></a>
### Fresh-row covariance and concentration

The [fixed conditional argument](../claims/Yin_C_F0187_v9.md#balanced-fresh-row-distance) conditions only on the two input minors and their measurable good conditions.
Kernel balance supplies a trace covariance lower bound even for an auxiliary direction with one zero coordinate.
Bounded-product concentration and a real two-dimensional net give the full physical row-distance Gram bound.

<a id="balanced-middle-index-count"></a>
### The logarithmic range and remaining bottom condition

The [fixed block identity and index count](../claims/Yin_C_F0187_v9.md#balanced-middle-index-count) leave only \(O(\log N)\) bottom singular values and give summable intermediate negative-logarithmic control.
Together with the accepted almost-sure weak law, this also proves a finite free logarithm.
An additional polynomial least-value floor in probability then makes the normalized bottom contribution \(O((\log N)^2/N)\), giving a logarithmic probability limit and the arbitrary-coupling limsup.
The exact finite/free determinant transfer to the shifted quadratic product and its factor two are included in that fixed theorem.
The next row-distribution calculation and the whole-parent scalar-shift construction address the additional floor; the original finite-second-moment and general coefficient contracts remain broader.

<a id="bounded-pair-weighted-fourth-layer"></a>
## Bounded two-copy fourth energy and the unconditional assembly

The complete weighted fourth-energy argument is fixed in [C186v17](../claims/Yin_C_F0186_v17.md#bounded-two-copy-fourth-layer), with its [independent whole-chain review](../audits/reviews/Yin_R_F0190_v16.md#bounded-two-channel-whole-chain) and [proved adoption](../claims/Yin_C_F0186_v17.md#decision-bounded-two-channel-reviewed).
The exact two-copy representation preserves the original bounded row law, retains a fixed fraction of the formal fourth energy with failure controlled by its maximum coordinate load, and gives a vanishing actual conditional load.
Its [enlarged-conditioning graph assembly](../claims/Yin_C_F0186_v17.md#shifted-parent-graph-bridge) integrates each row representation separately and uses physical averaging without an index union loss.
The [deterministic whole-parent translation](../claims/Yin_C_F0186_v17.md#deterministic-atom-avoiding-shift) removes singular retained minors, and the fixed proof checks all translated spectral and coefficient interfaces before transferring the floor back.
Together with the balanced middle estimate, this proves an unconditional exponent-five floor, full-sequence logarithmic convergence in probability and arbitrary-coupling almost-sure limsup equality in the exact bounded two-channel model.
The reviewed diagonal extension is recorded below; unbounded off-diagonal work continues separately.

<a id="finite-variance-diagonal-transfer"></a>
## Reviewed finite-second-moment diagonal extension

The complete extension is fixed and adopted in [C186v18](../claims/Yin_C_F0186_v18.md#decision-finite-diagonal-two-channel-reviewed), with [independent whole-chain coverage](../audits/reviews/Yin_R_F0190_v17.md#finite-diagonal-two-channel-whole-chain).
It retains bounded real off-diagonal laws and allows fixed centered real diagonal laws with only finite second moment.
Its [noncommuting perturbation argument](../claims/Yin_C_F0186_v18.md#diagonal-mass-projector-transfer) transfers weighted mass and physical resolvents, and its [actual Gram proof](../claims/Yin_C_F0186_v18.md#perturbed-joint-gap-and-gram) rederives the eigenvector bound from the perturbed equations.
The fixed proof then establishes the exponent-five floor and probability logarithmic limit, with a separate scalar regularized-potential upper bound giving the arbitrary-coupling limsup.
The [summability boundary](../claims/Yin_C_F0186_v18.md#finite-diagonal-summability-boundary) retains the diagonal heavy-tail example and the reason an eventual fixed norm bound cannot be substituted into this argument.

<a id="real-parameter-two-channel-extension"></a>
## Reviewed coefficient and real-parameter extension

The explicit interval, signed free channel mass and complete parameter conversion are fixed and adopted in [C186v19](../claims/Yin_C_F0186_v19.md#decision-real-parameter-two-channel-reviewed).
Its [independent whole-chain review](../audits/reviews/Yin_R_F0190_v18.md#real-parameter-two-channel-whole-chain) includes the separate deterministic-interface inspection.
This extends the coefficient \(\alpha\) and real quadratic parameter while retaining bounded real off-diagonal laws and finite-second-moment diagonals.
The exact [parameter boundaries](../claims/Yin_C_F0186_v19.md#parameter-boundaries) concern the linear channel-mass mechanism and do not refute determinant approximation at excluded parameters.

<a id="finite-variance-selective-sign-row"></a>
## Reviewed finite-variance row conversion

The complete result is fixed and adopted in [C194v14](../claims/Yin_C_F0194_v14.md#decision-finite-variance-graph-reviewed), with [independent whole-proof coverage](../audits/reviews/Yin_R_F0200_v14.md#finite-variance-graph-bridge).
Its [formal matching and two-copy survival](../claims/Yin_C_F0194_v14.md#finite-variance-two-copy-thinning) convert the actual finite-second-moment row without an upper amplitude cutoff.
Its [pair support guard](../claims/Yin_C_F0194_v14.md#pair-row-support-guard) uses only a weak law for squared coordinates and supports a graph-area bound uniformly over the remaining signs.
The separate [selected-sign energy/load lemma](../claims/Yin_C_F0194_v14.md#selective-sign-energy-load) preserves those two quantities by revealing large-amplitude signs; it is not needed for the shorter matching proof.

<a id="finite-variance-physical-controls"></a>
## Reviewed physical controls for the original finite-variance laws

The complete original-law extension is fixed and adopted in [C187v10](../claims/Yin_C_F0187_v10.md#decision-finite-variance-physical-reviewed), with [independent whole-proof coverage](../audits/reviews/Yin_R_F0191_v10.md#finite-variance-physical-regularity).
It proves almost-sure uniform weighted weak convergence through two physical deletions and fixed-window physical resolvent and projector bounds through one deletion, for any deterministic vanishing scalar shift.
It also gives closest-mode physical leverage tending to zero and uniform full-residual energy divergence, row spread and physical diagonal negligibility after removing any eigenmode.
The [weighted original-row cutoff and summable nets](../claims/Yin_C_F0187_v10.md#finite-variance-projected-row) require no fixed matrix-norm guard.
The [exact remaining scope](../claims/Yin_C_F0187_v10.md#remaining-scope) separates those full-matrix controls from a visible-residual comparison, auxiliary Gram separation and complete fourth-layer coercivity.
In particular, full physical row spread alone is not yet a normalized coefficient-load bound relative to an established fourth-layer energy.

<a id="finite-variance-joint-gap-controls"></a>
## Reviewed fixed-center joint residual gap

The [original-law joint gap](../claims/Yin_C_F0187_v12.md#decision-finite-variance-joint-gap-reviewed), with [independent whole-proof review](../audits/reviews/Yin_R_F0191_v12.md#finite-variance-joint-gap-reviewed), excludes a common approximate eigenvector at fixed bounded scalar centers through every single deletion.
Its bounded transfer uses a tail-adapted projection, with the full Frobenius and first-input count exceptions paid once.
The later low-energy Gram result below requires its own compressed joint gap and component estimates.

<a id="finite-variance-middle-controls"></a>
## Reviewed finite-variance intermediate logarithmic control

The [middle theorem C187v11](../claims/Yin_C_F0187_v11.md#decision-finite-variance-middle-reviewed), with its [complete independent review](../audits/reviews/Yin_R_F0191_v11.md#finite-variance-middle-reviewed), now supplies the original-law intermediate input.
Its [actual kernel graph trace](../claims/Yin_C_F0187_v11.md#kernel-graph-trace) needs only a common Frobenius bound and replaces the earlier fixed operator-norm and thin-rectangle premises.
It gives \(s_{2N-j}(L_N)\ge c(j/N)^{3/2}\) from \(j\) of order \(\sqrt{N\log N}\), outside one common \(o(1)\) exception plus an arbitrary inverse power.
The [logarithmic deduction](../claims/Yin_C_F0187_v11.md#finite-variance-middle-log) proves full-sequence logarithmic convergence in probability if a separate polynomial least-value floor is supplied.
No such floor, summable common exception or full-sequence almost-sure logarithmic conclusion is proved by that theorem.

<a id="finite-variance-formal-graph-interface"></a>
### The actual-minor interface and its fixed-model resolution

The [fixed conditional matrix theorem](../claims/Yin_C_F0194_v14.md#statement) retains an arbitrary independent real symmetric second input and arbitrary independent first diagonals.
Its graph supremum concerns a radius-two first-row ball with the actual conditioned second border fixed, and its error retains the average failure of the formal energy, load and graph hypotheses.
The [normalized second-input and parent-norm corollaries](../claims/Yin_C_F0194_v14.md#finite-variance-second-input-corollary) provide concrete finite-second-moment row guards and a polynomial parent norm guard, without proving that minor average vanishes.
The complete reviewed assembly below establishes those actual-minor hypotheses with vanishing averaged failure for the fixed real two-channel model, using one atom-avoiding whole-parent shift.
The reviewed middle theorem above now supplies the separate intermediate logarithmic control for this exact finite-variance pencil.
The two failures below explain why simpler truncation or deletion transfers do not supply this input.

<a id="finite-variance-single-shift-assembly"></a>
### A single shift and the reviewed finite-variance theorem

The complete assembly is fixed in [C186v20](../claims/Yin_C_F0186_v20.md#argument), whose [proved decision](../claims/Yin_C_F0186_v20.md#decision-finite-variance-two-channel-reviewed) selects the independent whole-chain review.
Its proof uses one deterministic atom-avoiding \(0<\theta_N<N^{-10}\) to assemble a \(cN^{-6}\) least-value floor without a residual bad-minor term, the all-dimension logarithmic probability limit, and the every-coupling almost-sure limsup for the original real finite-variance two-channel pencil.
The fixed proof now owns every necessary algebraic, probability and logarithmic interface; this Draft is development provenance, not a logical dependency.

A sufficient interface for alternative proofs can be stated more weakly than the three separate inverse-mode energy bounds.
For the actual shifted single-deletion inverse \(Z_i\), let \(Q_i=\|Z_i\|\), \(m_i=s_2^\downarrow(Z_i)\), and let \(\sigma_{4,i},\tau_{4,i}\) denote its formal fourth coefficient size and normalized load.
For some fixed \(c>0\), it is enough that for every fixed \(\varepsilon>0\),
\[
 \frac1N\sum_i\mathbb P\{\sigma_{4,i}<cQ_im_i/N^2
                              \ \text{or}\ \tau_{4,i}>\varepsilon\}\to0.
\]
The exact [two-mode graph area](../claims/Yin_C_F0186_v20.md#actual-second-border-and-conditioning) is at most a fixed multiple of \(Q_im_i\) once \(Q_i,m_i\ge1\); their uniform divergence follows from the accepted shifted residual theorem.
This is a sufficient inverse-only target, not a necessary lower bound for the smaller actual-border family.
The fixed proof obtains the stronger uniform estimate from the accepted high-rank input and the [reviewed shifted low-rank theorem](../claims/Yin_C_F0187_v15.md#statement).
Its graph step only needs the displayed average, so a uniform-minor conclusion is unnecessary for a future alternative proof.

<a id="finite-variance-shifted-high-rank-interface"></a>
#### The shifted high-rank interface

The [fixed shifted calculation](../claims/Yin_C_F0186_v20.md#shifted-high-rank-coefficients) applies the accepted approximate-mode event with \(\lambda=-\theta_N\) to the whole low subspace of each actual shifted minor.
It then applies the deterministic six-Gram and rank-sensitive coefficient arguments to those shifted blocks, using C187v10's explicit shifted physical limits.
It never compares two real inverses or treats an unshifted theorem statement as a theorem for varying diagonal laws.

<a id="finite-variance-actual-border-assembly"></a>
#### Actual second borders and measurable conditioning

The [fixed conditioning argument](../claims/Yin_C_F0186_v20.md#actual-second-border-and-conditioning) defines each good event by minor-measurable numerical coefficient bounds and the actual second border.
Only the average second-row norm failure is used; neither a simultaneous row guard nor independence of a second border from its own minor is assumed.
The global events proving those numerical bounds and the parent norm event are not inserted into the fresh-row conditioning.

<a id="finite-variance-conditional-floor-log"></a>
#### The polynomial scale and its logarithmic use

The accepted Frobenius event gives \(\|L_N+\theta_NI\|\le B\sqrt N\) with probability tending to one, so [the fixed graph assembly](../claims/Yin_C_F0186_v20.md#finite-variance-matrix-floor) has scale \(cN^{-6}\).
The original single shift is smaller than that scale and returns the floor to the original matrix; no singular-minor remainder or shifted-logarithm comparison remains.
The [fixed logarithmic deduction](../claims/Yin_C_F0186_v20.md#finite-variance-logarithmic-conclusions) uses the accepted original-model middle theorem, then a separate regularized upper bound and a marginal subsequence for the almost-sure limsup.
The [low-rank adoption](../claims/Yin_C_F0187_v15.md#decision-shifted-finite-variance-low-rank-reviewed) and [whole-chain finding](../audits/reviews/Yin_R_F0190_v19.md#finite-variance-two-channel-whole-chain) now supply their respective evidence.
Neither full-sequence almost-sure logarithmic convergence nor the unrestricted determinant or Brown-measure Tasks follow from these statements.

<a id="finite-variance-minor-guard-boundary"></a>
### Two precise limits of a direct truncation or deletion transfer

The [fixed atomic cutoff calculation](../ledger/Yin_L_F0065_v1.md#atomic-cutoff-obstruction) already separates exact-input matching from a vanishing rank fraction, and its [sharp threshold statement](../ledger/Yin_L_F0065_v1.md#sharp-exact-truncation) gives the actual finite-variance matching thresholds.
Those statements do not make a fixed operator-norm guard typical.
For an explicit admissible real input, choose \(p\in(2,4)\), let \(Y\) be symmetric with \(\mathbb P\{|Y|>t\}=t^{-p}\) for \(t\ge1\), and put
\[
 s:=\sqrt{p/(p-2)},\qquad \xi:=Y/s.
\]
Then \(\mathbb E\xi=0\), \(\mathbb E\xi^2=1\), and for every fixed \(A>0\), eventually
\[
 \begin{split}
 \mathbb P\{\|W_1^{(N)}\|\le A\}
 &\le\mathbb P\{\max_{i<j}|\xi_{ij}|\le A\sqrt N\}\\
 &=(1-s^{-p}A^{-p}N^{-p/2})^{N(N-1)/2}
 \le\exp(-c_A N^{2-p/2})\longrightarrow0.
 \end{split}
\]
In the actual two-channel model with \(\alpha=\sqrt2\), the deterministic identity
\[
 W_1=(\alpha X-Y)/(\alpha-1),\qquad
 \|W_1\|\le\frac{\alpha+1}{\alpha-1}\|L_N\|
\]
uses only that \(X,Y\) are principal diagonal blocks of \(L_N\).
Thus \(\mathbb P\{\|L_N\|\le A\}\to0\) for every fixed \(A\), regardless of the independent second input.
The same estimate holds for each fixed physical deletion, since its off-diagonal coordinate count is still comparable to \(N^2\) with the original normalization.
Consequently the fixed-norm premises of the bounded-minor coefficient arguments cannot simply be declared typical under finite variance.
This is an obstruction to that premise, not to the determinant contract.

A different quantitative issue concerns deleting a vanishing coordinate fraction and transferring an unregularized logarithm by rank alone.
Fix \(A>0\), put \(k_N:=\lfloor N/\log N\rfloor\), and define the positive diagonal matrix
\[
 D_N:=\operatorname{diag}(\underbrace{N^{-A},\ldots,N^{-A}}_{k_N},1,\ldots,1).
\]
Both \(D_N\) and \(I_N\) have operator norm at most one and least singular value at least \(N^{-A}\), while
\[
 \operatorname{rank}(D_N-I_N)=k_N=o(N),\qquad
 \frac1N\log\det D_N
 =-A\frac{k_N\log N}{N}\longrightarrow-A.
\]
Thus even a common polynomial floor does not make a bare rank-\(o(N)\) comparison sufficient for logarithmic transfer.
The corresponding truncation-height estimate requires a quantity of order \((k_N/N)\log N\) to vanish, or a more informative bound on the affected singular values.
This deterministic diagonal example is distinct from the [nonnormal perturbation examples](../ledger/Yin_L_F0058_v1.md#failed-shortcuts) and is not asserted to occur as an actual Wigner-pencil minor.


The [favorable-subsequence tail calculation](Yin_D_F0033.md#favorable-subsequence-tail-rank) supplies a deterministic dimensional subsequence along which the rank-times-log input perturbation vanishes almost surely.
It leaves polynomial floors for both outputs and the varying truncated-law interface unresolved.
The [high-amplitude path](Yin_D_F0033.md#high-amplitude-path-resonance) and [flat auxiliary-slope test](Yin_D_F0033.md#flat-two-mode-slope-test) isolate different ways the fourth coefficient norm can become small relative to the ball graph area.
The latter already has flat physical modes and vanishing relative fourth load, but neither construction supplies the weighted Wigner bulk and simultaneous-deletion information needed for a counterexample to all the reviewed physical controls.

<a id="vanishing-entry-truncation-norm-obstruction"></a>
## A finite-variance truncation with vanishing entries and divergent operator norm

The following ordinary development supplies a different obstruction from the preceding untruncated Pareto maximum-entry example.
Here every retained normalized entry tends uniformly to zero, and the rank-times-log truncation error tends to zero in probability, but the truncated operator norm diverges.
The obstruction comes from many retained large coordinates in a rare row, rather than from one retained entry of unbounded size.

### One fixed centered variance-one law

Put \(t_0:=e^e\) and \(\kappa:=e t_0^2\).
Let \(V\ge0\) have survival function
\[
 \mathbb P\{V>t\}:=
 \begin{cases}
 1,&0\le t<t_0,\\
 \displaystyle\frac{\kappa}{t^2\log t\,(\log\log t)^2},&t\ge t_0.
 \end{cases}
\]
This is a continuous decreasing survival function, equal to one at \(t_0\) and tending to zero at infinity.
The tail integral gives
\[
 \mathbb EV^2
 =t_0^2+2\kappa\int_{t_0}^{\infty}
             \frac{dt}{t\log t\,(\log\log t)^2}
 =t_0^2+2\kappa<\infty.
\]
Let \(\eta\) be an independent fair sign and define
\[
 s:=\sqrt{t_0^2+2\kappa},\qquad
 \xi:=\eta V/s,\qquad c_0:=\kappa/s^2.
\]
Then \(\xi\) is a fixed real symmetric centered law with variance one.
Its survival function satisfies
\[
 \overline F(t):=\mathbb P\{|\xi|>t\}
 =\frac{\kappa}{s^2t^2\log(st)\,(\log\log(st))^2}
 \sim\frac{c_0}{t^2\log t\,(\log\log t)^2}
 \quad(t\to\infty).
 \tag{Vanishing-entry-fixed-tail}
\]

Let \(W_N\) be real symmetric with independent upper off-diagonal entries \(\xi_{ij}/\sqrt N\), distributed according to this law, and zero diagonal.
Cross-size coupling is arbitrary throughout.
For sufficiently large \(N\), set
\[
 \ell_N:=\log N,\qquad \lambda_N:=\log\log N,\qquad
 \varepsilon_N:=\lambda_N^{-1/2},\qquad
 T_N:=\varepsilon_N\sqrt N,
\]
and define the coordinatewise raw truncation
\[
 (\widetilde W_N)_{ij}:=
 \frac{\xi_{ij}}{\sqrt N}\mathbf 1_{\{|\xi_{ij}|\le T_N\}}
 \quad(i<j),
\]
with symmetric lower entries and zero diagonal.
Every entry satisfies \(|(\widetilde W_N)_{ij}|\le\varepsilon_N\to0\).
Symmetry preserves centering exactly, and the truncated raw variance tends to one by integrability of \(\xi^2\).
Thus rescaling that variance back to one would multiply the matrix by a deterministic factor tending to one and would not change the norm conclusion below.

### Independent bipartite row counts

Since \(\log T_N\sim\ell_N/2\) and \(\log\log T_N\sim\lambda_N\),
\[
 \overline F(T_N)\sim\frac{2c_0}{N\ell_N\lambda_N},\qquad
 p_N:=\mathbb P\{T_N/2<|\xi|\le T_N\}
 \sim\frac{6c_0}{N\ell_N\lambda_N}.
 \tag{Vanishing-entry-band-probability}
\]
The second relation uses \(\overline F(T_N/2)/\overline F(T_N)\to4\).
Partition the physical coordinates into sets \(I_N,J_N\) of sizes \(\lfloor N/2\rfloor\) and \(\lceil N/2\rceil\).
For each \(i\in I_N\), let \(D_i\) count the edges to \(J_N\) whose raw absolute value lies in \((T_N/2,T_N]\).
These counts are mutually independent, because the corresponding unordered upper-triangular coordinates are disjoint even when two edges have a common endpoint in \(J_N\).
Each count is binomial with parameters \(m_N:=|J_N|\) and \(p_N\), and mean
\[
 \mu_N:=m_Np_N\sim\frac{3c_0}{\ell_N\lambda_N}.
\]
Put \(k_N:=\lfloor\ell_N/(4\lambda_N)\rfloor\).
For sufficiently large \(N\), one has \(1\le k_N\le m_N\) and \(p_N\le1/2\), so
\[
 \begin{split}
 \mathbb P\{D_i\ge k_N\}
 &\ge\binom{m_N}{k_N}p_N^{k_N}(1-p_N)^{m_N-k_N}\\
 &\ge\left(\frac{\mu_N}{k_N}\right)^{k_N}e^{-2\mu_N}.
 \end{split}
\]
Here \(\binom m k\ge(m/k)^k\), obtained by comparing the factors \((m-j)/(k-j)\) with \(m/k\), and \(\log(1-p)\ge-2p\) for \(p\le1/2\).
Moreover,
\[
 \log(k_N/\mu_N)=2\lambda_N+O(1),\qquad
 k_N\log(k_N/\mu_N)=(1/2+o(1))\ell_N.
\]
Consequently \(\mathbb P\{D_i\ge k_N\}\ge N^{-2/3}\) eventually.
Independence across \(I_N\) now gives
\[
 \mathbb P\{\max_{i\in I_N}D_i<k_N\}
 \le\exp(-N^{1/3}/3).
 \tag{Vanishing-entry-degree-exception}
\]

If \(D_i\ge k_N\), the retained row has at least \(k_N\) entries of absolute value greater than \(\varepsilon_N/2\).
The operator norm is at least the Euclidean norm of that row, hence for a fixed \(c>0\), eventually
\[
 \|\widetilde W_N\|
 \ge\frac{\varepsilon_N\sqrt{k_N}}2
 \ge c\frac{\sqrt{\log N}}{\log\log N}
 \longrightarrow\infty
\]
outside the exception in (Vanishing-entry-degree-exception).
That exception is summable in \(N\).
First Borel--Cantelli proves this eventual norm lower bound almost surely under every cross-size coupling.
The same counting argument applies after any one prescribed physical deletion, with the original \(\sqrt N\) normalization.

### Rank-times-log compatibility and its exact limit

Let \(R_N:=\operatorname{rank}(W_N-\widetilde W_N)\).
Changing one upper off-diagonal entry and its symmetric partner has rank at most two, so
\[
 \mathbb E\left[\frac{R_N\log N}{N}\right]
 \le N\log N\,\overline F(T_N)
 \sim\frac{2c_0}{\log\log N}\longrightarrow0.
 \tag{Vanishing-entry-rank-log}
\]
Thus the rank-times-log error vanishes in probability along the full sequence.
Choosing a deterministic subsequence with \(\log\log N_k\ge2^{3k}\) makes these first moments \(O(2^{-3k})\).
The already retained [Markov and first-Borel--Cantelli subsequence argument](Yin_D_F0033.md#favorable-subsequence-tail-rank), at thresholds \(2^{-k}\), gives almost-sure vanishing of this error along \(N_k\) under every cross-size coupling.
The norm still diverges along that same subsequence, since its preceding almost-sure lower bound holds along all dimensions.

More generally the same fixed law permits \(\varepsilon_N:=(\log\log N)^{-a}\) for every fixed \(0<a<1\).
The band mean is then of order \((\log\log N)^{2a-2}/\log N\), while
\[
 \log(k_N/\mu_N)
 =2\log\log N+(1-2a)\log\log\log N+O(1).
\]
The preceding binomial estimate therefore still has exponent \(-(1/2+o(1))\log N\).
It yields a summable-exception norm lower bound of order
\[
 \frac{\sqrt{\log N}}{(\log\log N)^{a+1/2}}\longrightarrow\infty,
\]
while the first moment of the rank-times-log error is \(O((\log\log N)^{2a-2})\to0\).

This construction rules out deducing a typical fixed operator-norm core from a vanishing entry cap together with a negligible rank-times-log truncation error.
It does not rule out more informative truncation, deletion or preconditioning mechanisms with additional proved inputs.
In particular, it proves no failure of a polynomial least-value floor, the logarithmic determinant contract, or the reviewed original-law intermediate singular-value profile.
The truncated laws still vary with \(N\), and applying the fixed bounded-law theorem to them would require a separate uniform theorem.


<a id="finite-variance-low-mode-gram-candidate"></a>
## Reviewed finite-variance low-energy auxiliary Gram separation

The complete [fixed statement](../claims/Yin_C_F0187_v13.md#statement) and [argument](../claims/Yin_C_F0187_v13.md#argument) retain the low-energy auxiliary Gram conclusion and its necessary compressed joint gap.
The [large tail spectral threshold](../claims/Yin_C_F0187_v13.md#bounded-compression) is chosen after the cutoff-dependent sphere-net budget, avoiding an unsupported rate comparison for a finite-variance tail.
The [proved assessment](../claims/Yin_C_F0187_v13.md#decision-finite-variance-low-mode-gram-reviewed) selects the [independent whole-proof finding](../audits/reviews/Yin_R_F0191_v13.md#finite-variance-low-mode-gram-reviewed).
The remaining fourth-layer coercivity and actual graph-area comparison are not supplied by this result, so it does not establish a finite-variance least-value floor.


<a id="approximate-mode-gram-continuation"></a>
## Reviewed approximate-mode and low-subspace geometry

The complete argument developed at this address is fixed in [C187v14](../claims/Yin_C_F0187_v14.md#approximate-mode-stability), with its [proved adoption](../claims/Yin_C_F0187_v14.md#decision-finite-variance-high-rank-reviewed) and [independent whole-proof finding](../audits/reviews/Yin_R_F0191_v14.md#finite-variance-high-rank-reviewed).
It preserves the original C187v13 good event and center box, controls the explicit approximate-mode errors, and gives a fixed Gram lower bound for every vector in a sufficiently small whole spectral subspace, including combinations of distinct eigenmodes.
Its [signed low-subspace comparison](../claims/Yin_C_F0187_v14.md#low-subspace-six-gram) retains the coordinate-map injectivity, compression with signed weights and exact input-action identities needed by the coefficient argument.
This Draft address records the development provenance; the complete fixed proof owns the mathematical reasoning.
C187v14 additionally proves its stated unshifted raw six-Gram and high-effective-rank fourth-layer conclusions, but supplies no all-regime least-value floor by itself.
The [reviewed shifted low-rank theorem](../claims/Yin_C_F0187_v15.md#decision-shifted-finite-variance-low-rank-reviewed) and [reviewed single-shift assembly](../claims/Yin_C_F0186_v20.md#decision-finite-variance-two-channel-reviewed) supply the subsequent branches and fixed-model determinant conclusion.

<a id="three-channel-propagation-probe"></a>
## Ordinary exploration: a three-channel propagation probe, not an adopted theorem

This is ordinary strategic and algebraic exploration for Yin on 2026-11-06, with a direct authoring self-check rather than an independent review.
It tests propagation within the existing [actual-minor strategy](../strategies/Yin_S_F0032.md), while retaining the full arbitrary-coefficient [F0013 contract](../tasks/Yin_T_F0013_v1.md#contract) and arbitrary-polynomial and fixed-parameter [F0014 contract](../tasks/Yin_T_F0014_v1.md#contract).
The [proved two-channel result](../claims/Yin_C_F0186_v20.md#statement) concerns its fixed real coefficient tuple; it supplies no three-channel theorem.
Start the proposed test with two independent real Wigner inputs \(C_N,D_N\) under the original centered, variance-one off-diagonal and centered finite-second-moment diagonal laws, with the original \(N^{-1/2}\) normalization and arbitrary coupling across dimensions.
Put
\[
 A=C_N,\qquad B=C_N+D_N,\qquad E=C_N+\sqrt2D_N,
 \qquad
 \mathcal L_N=
 \begin{pmatrix}A&I&0\\I&B&I\\0&I&E\end{pmatrix}.
 \tag{Three-channel-model}
\]
The proposed extension would add one auxiliary-size-three coefficient tuple to F0013 and, by the exact identity below, the repeated-variable cubic
\[
 P(x,y)=(x+\sqrt2y)(x+y)x-2x-\sqrt2y
 \tag{Three-channel-polynomial}
\]
at the exceptional parameter \(z=P(0,0)=0\) to F0014.
Neither conclusion is asserted here, and success on this real model would not resolve arbitrary complex laws, all matrix coefficients, all scalar parameters or the full-sequence Brown-measure problem.

### Two constant pivots give the finite and free determinant identities

For arbitrary \(A,B,E\) in a unital algebra, swap the first two block columns and subtract \(B\) times the first block row from the second and the first block row from the third.
Then swap the last two block columns and subtract \(E\) times the second block row from the third.
The resulting exact sequence is
\[
 \begin{pmatrix}A&I&0\\I&B&I\\0&I&E\end{pmatrix}
 \longmapsto
 \begin{pmatrix}I&A&0\\B&I&I\\I&0&E\end{pmatrix}
 \longmapsto
 \begin{pmatrix}I&A&0\\0&I-BA&I\\0&-A&E\end{pmatrix}
 \longmapsto
 \begin{pmatrix}I&0&A\\0&I&I-BA\\0&E&-A\end{pmatrix}
 \longmapsto
 \begin{pmatrix}I&0&A\\0&I&I-BA\\0&0&EBA-E-A\end{pmatrix}.
 \tag{Three-channel-pivots}
\]
No input block or final polynomial is inverted.
For \(N\)-by-\(N\) blocks, each column transposition has determinant sign \((-1)^{N^2}=(-1)^N\), so the two signs cancel.
The block-row operations have determinant one, proving
\[
 \det\mathcal L_N=\det(EBA-E-A)=\det P(C_N,D_N).
 \tag{Three-channel-finite-determinant}
\]

For the free version take \(A=c\), \(B=c+d\), \(E=c+\sqrt2d\), where \(c,d\) are the bounded freely independent semicircular limits, and use the normalized auxiliary trace \(\tau_3=\operatorname{tr}_3\otimes\tau\).
Reuse only the [bounded FK multiplicativity and unitriangular determinant-one argument](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) already accepted there, with its [fixed finite-tracial source input](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
Every row factor in (Three-channel-pivots) is a bounded invertible unitriangular element, and the column swaps are unitaries, all of FK determinant one.
The final matrix equals
\[
 \operatorname{diag}(I,I,P(c,d))
 \begin{pmatrix}I&0&c\\0&I&I-(c+d)c\\0&0&I\end{pmatrix}.
\]
Its second factor is again bounded unitriangular, so block trace normalization gives
\[
 \Delta_{\tau_3}(\mathcal L)^3=\Delta_\tau(P(c,d)),
 \qquad
 \log\Delta_{\tau_3}(\mathcal L)
 =\frac13\log\Delta_\tau(P(c,d)).
 \tag{Three-channel-free-determinant}
\]
These identities include zero determinants and logarithm \(-\infty\), without an inverse or logarithmic integrability assumption on \(P(c,d)\).
Thus the determinant-limsup conclusions for this pencil and this cubic at zero are exactly equivalent after the factor three; this is an algebraic reduction, not a proof of either conclusion.

### The coefficient degeneracy survives deterministic stripping

Write
\[
 T=\operatorname{diag}(0,1,\sqrt2),\qquad
 K=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},
 \qquad
 \mathcal L_N=I_3\otimes C_N+T\otimes D_N+K\otimes I_N.
\]
The common left and right noise kernels vanish because the first noise coefficient is \(I_3\), so the [deterministic-strip reduction](#constant-row-deflation) cannot start.
On the other hand, the noise-frame quantity
\[
 \chi=\inf_{\|p\|=\|q\|=1}
       \bigl(|p^*q|^2+|p^*Tq|^2\bigr)
\]
is zero: choose \(p=e_1,q=e_2\).
The constant coefficient \(K\) is singular, with kernel containing \((1,0,-1)^T\).
The unital algebra generated by \(T,K\) is nevertheless all of \(M_3(\mathbb C)\): polynomials in the three-distinct-eigenvalue matrix \(T\) give the diagonal matrix units, and multiplication by \(K\) and along its two-edge path gives the remaining units.
Consequently this test is neither a positive-frame case nor a new application of constant-row removal or coefficient irreducibility alone.

### A scalar joint gap does not imply a three-component Gram gap

Consider the deterministic two-dimensional real symmetric matrices
\[
 C_0=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
 D_0=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For every real unit vector \(u=(u_1,u_2)^T\) and every real pair \(a,b\), minimization over the two centers gives
\[
 \begin{split}
 \|(C_0-aI)u\|^2+\|(D_0-bI)u\|^2
 &\ge \operatorname{Var}_u(C_0)+\operatorname{Var}_u(D_0)\\
 &=u_1^2u_2^2+1-4u_1^2u_2^2\\
 &=1-3u_1^2u_2^2\ge\frac14.
 \end{split}
 \tag{Three-channel-scalar-gap}
\]
Here \(\operatorname{Var}_u(H)=\|Hu\|^2-\langle u,Hu\rangle^2\).
Form the real symmetric six-dimensional matrix \(\mathcal L_0=I_3\otimes C_0+T\otimes D_0+K\otimes I_2\), choose any eigenvalue \(\lambda\), and put \(C_1=C_0-\lambda I_2\).
Then \(I_3\otimes C_1+T\otimes D_0+K\otimes I_2=\mathcal L_0-\lambda I_6\) has a nonzero real zero mode \(v=(u_1,u_2,u_3)\), with each \(u_j\in\mathbb R^2\).
The scalar joint-gap lower bound (Three-channel-scalar-gap) remains unchanged after shifting \(C_0\), because its center \(a\) is arbitrary.
All matrix norms are bounded by absolute constants, since \(|\lambda|\le1+2\sqrt2\).
Nevertheless the three-component Gram matrix \((\langle u_a,u_b\rangle)_{a,b=1}^3\) has rank at most two and is singular.
This refutes the deterministic inference from bounded input norms and a positive scalar joint gap to a positive three-component Gram for every low mode.
It does not assert a typical-minor obstruction, the physical spread hypotheses of the Wigner model, failure of sixth-layer energy, or a counterexample to either Task.

### A varying auxiliary kernel can annihilate a three-by-three quadratic determinant

The following additional algebraic probe was supplied in the same coordinated exploration and checked directly here, without an independent-review claim.
In this paragraph alone take \(\mathcal E=\mathcal H=\mathbb R^3\), \(\mathsf A=I_{\mathcal H}\), and maps \(U_i:\mathcal H\to\mathcal E\) given by
\[
 U_i h=\frac{e_i\times h}{\sqrt2},\qquad i=1,2,3.
\]
The cross-product identity gives
\[
 \sum_{i=1}^3\|U_i h\|^2=\|h\|^2,
 \qquad
 \|\mathsf A\|=1,\quad\|\mathsf A\|_F^2=3,\quad s_3(\mathsf A)=1.
\]
Since \(U_i^*x=(x\times e_i)/\sqrt2\), the quadratic matrix is
\[
 B(x):=\bigl[\langle U_i^*x,\mathsf A U_j^*x\rangle\bigr]_{i,j=1}^3
 =\frac{\|x\|^2I_3-xx^T}{2}.
\]
For \(x\ne0\), its eigenvalues are \(\|x\|^2/2,\|x\|^2/2,0\), and its kernel is \(\mathbb R x\).
Consequently
\[
 \det B(x)\equiv0,\qquad
 \operatorname{adj}B(x)=\frac{\|x\|^2xx^T}{4},\qquad
 \bigcap_{x\ne0}\ker B(x)=\{0\}.
\]
The adjugate identity also holds at zero, where both sides vanish.
Thus a zero quadratic-matrix determinant need not have a fixed nonzero auxiliary kernel, even with an isometric stacked map and three nonzero singular values of \(\mathsf A\).
This example does not satisfy a strict whole-subspace Gram lower bound: for every unit \(h\),
\[
 \bigl[\langle U_i h,U_j h\rangle\bigr]_{i,j=1}^3
 =\frac{I_3-hh^T}{2}
\]
is singular.
It therefore excludes only an unconditional extension of a two-component zero classification or of an isometry-only energy argument.
The later [finite-channel theorem](../claims/Yin_C_F0187_v16.md#statement) resolves raw noncancellation under its strict whole-subspace Gram and spectral hypotheses; this example supplies no actual inverse, Wigner minor or Task counterexample.

### Actual low-rank realizations and the first unsupported bridge

For an actual \(n\)-dimensional physical minor, keep its input matrices \(C,D\), the fixed \(T,K\) above and a block vector \(v=(u_1,u_2,u_3)\).
With \(V=[u_1\ u_2\ u_3]\in M_{n,3}(\mathbb R)\), the exact mode equation is
\[
 \mathcal L v=\lambda v
 \quad\Longleftrightarrow\quad
 CV+DVT+VK=\lambda V.
 \tag{Three-channel-realization}
\]
For an approximate mode the right side is \(\lambda V+R\), with \(\|R\|_F=\|(\mathcal L-\lambda I)v\|\).
The auxiliary Gram is \(V^TV\), so its degeneracy means that this actual equation has a nonzero realization with column rank at most two.
The two-dimensional example shows why the accepted scalar joint-gap argument alone cannot exclude such realizations.
It does not show that excluding common two-dimensional invariant subspaces is sufficient: the displayed equation is the constraint to analyze, and separate invariance under \(C,D\) has not been deduced from it.

There is a further exact rank-two constraint, suggested and checked within this same coordinated exploration.
If \(\operatorname{rank}V=2\), \(Va=0\) and \(a\ne0\), multiplying (Three-channel-realization) by \(a\) gives
\[
 DVT a+VK a=0,\qquad
 (I-P_V)DVT a=0,
 \tag{Three-channel-kernel-constraint}
\]
where \(P_V\) is the orthogonal projection onto \(\operatorname{ran}V\).
The one-dimensional space \(\ker V\) cannot be a coordinate axis.
Indeed \(u_1=0\) forces \(u_2=0\) by the first mode equation, \(u_3=0\) forces \(u_2=0\) by the third, and \(u_2=0\) forces \(u_1+u_3=0\) by the second; each case has rank at most one.
Since the eigenvalues of \(T\) are distinct, \(\ker V\) therefore cannot be a \(T\)-invariant line.

For a deterministic \(V\) and independent centered fresh vectors \(\xi,\eta\in\mathbb R^n\), each with independent variance-one coordinates, the row
\[
 r=N^{-1/2}(\xi^TV+\eta^TVT)
\]
has covariance
\[
 \operatorname{Cov}(r^T)
 =N^{-1}(V^TV+TV^TVT),\qquad
 \ker\operatorname{Cov}(r^T)
 =\{a:Va=0,\ VTa=0\}.
 \tag{Three-channel-fresh-row-covariance}
\]
For the exact rank-two realizations above this kernel is zero, since a nonzero vector in it would span a \(T\)-invariant \(\ker V\).
This is a deterministic full-rank covariance observation, with no dimension-uniform lower bound claimed.
An actual mode \(V\) depends on the input matrices, so using this fresh-row calculation requires a justified exposure that makes the relevant \(V\) independent of the retained row variables.
Quantitative covariance separation, nearly rank-two realizations, the net budget and finite-variance tails all remain to be controlled.

The first proposed investigation is to determine which nearly rank-deficient realizations can occur on typical original-law minors, using their actual independent inputs and physical controls, and which would actually obstruct the complete sixth-degree coefficient layer.
For an invertible actual minor with inverse \(Z=(Z_{ab})_{a,b=1}^3\), exposing the original first-input row \(x\) gives the highest homogeneous Schur term, up to sign,
\[
 h_Z(x)=\det\bigl[(x^TZ_{ab}x)_{a,b=1}^3\bigr].
\]
Nonvanishing of this raw degree-six polynomial would still not supply energy after repeated physical indices are removed, vanishing coordinate loads, the actual border graph normalization or the middle singular-value estimate.
These steps must retain the original conditioning and normalization; they cannot use a bound uniform over arbitrary invertible minors or replace mixed factors by independent noise.
The [existing typical-minor energy test](#typical-minor-energy-matching), [mixed-factor coding obstruction](#mixed-factor-coding-obstruction) and [actual-minor allocation boundary](../ledger/Yin_L_F0066_v5.md#actual-minor-allocation-boundary) retain those limitations.
A successful short test would identify a new probabilistic constraint on the actual realizations or a sufficient coefficient mechanism surviving their rank deficiency; merely postulating a sixth-layer lower bound would relocate the missing estimate.
This section therefore supports a bounded propagation investigation within S32, without a new strategic adoption, Claim or unrestricted determinant conclusion.

<a id="three-channel-covariance-bound"></a>
## Ordinary derivation: a quantitative three-channel covariance bound

This continues the preceding probe for Yin on 2026-11-06 as ordinary proof development with an authoring self-check, not an independent review or adopted theorem.
All spaces and matrices below are finite-dimensional and real, and \(C,D\in M_n(\mathbb R)\) are symmetric.
Retain \(T=\operatorname{diag}(0,1,\sqrt2)\), the three-vertex path matrix \(K\), and a real parameter \(\lambda\).
For \(V\in M_{n,3}(\mathbb R)\), order singular values as \(s_1(V)\ge s_2(V)\ge s_3(V)\ge0\), padding with zeros when necessary, and put
\[
 \mathcal F_\lambda(V):=CV+DVT+VK-\lambda V,\qquad
 G(V):=V^TV+TV^TVT,\qquad
 L:=\|C\|+\sqrt2\|D\|+|\lambda|.
\]
The conclusions are deterministic; in particular the original finite-variance model is not assumed to have bounded operator norms.

### A lower bound assuming only a second singular value

Suppose
\[
 \|V\|_F\le1,\qquad s_2(V)\ge d>0,\qquad
 \varepsilon:=\|\mathcal F_\lambda(V)\|_F\le d/2.
\]
Then
\[
 \lambda_{\min}G(V)\ge
 \frac{d^4}{676(1+L)^2}.
 \tag{Three-channel-covariance-lower}
\]
No hypothesis that \(s_3(V)\) is small is needed.

Write \(V=[u_1\ u_2\ u_3]\).
The first and third approximate-mode equations give
\[
 \|u_2\|\le L\|u_1\|+\varepsilon,\qquad
 \|u_2\|\le L\|u_3\|+\varepsilon,
\]
and the second gives \(\|u_1+u_3\|\le L\|u_2\|+\varepsilon\).
Approximate \(V\), respectively, by the rank-one matrices \([0\ 0\ u_3]\), \([u_1\ 0\ 0]\) and \([u_1\ 0\ {-u_1}]\).
The second singular value is at most the Frobenius error of each such approximation, so
\[
 d\le(1+L)\|u_j\|+\varepsilon,\qquad
 \|u_j\|\ge\kappa:=\frac{d}{2(1+L)}
 \quad(j=1,2,3).
 \tag{Three-channel-column-lower}
\]

Let \(q=\sqrt{\lambda_{\min}G(V)}\).
If \(q\ge d/2\), (Three-channel-covariance-lower) follows immediately because \(d\le1\).
Otherwise choose a unit minimizing vector \(a\in\mathbb R^3\) and a unit smallest right singular vector \(b\) of \(V\).
Then
\[
 \|Va\|^2+\|VTa\|^2=q^2,\qquad s_3(V)\le q,
\]
and the lower singular bound on \(b^\perp\) implies
\[
 \|P_{b^\perp}a\|\le q/d,\qquad
 \|P_{b^\perp}Ta\|\le q/d,\qquad
 |\langle a,b\rangle|\ge\sqrt3/2.
\]
Decomposing \(a=\langle a,b\rangle b+P_{b^\perp}a\) therefore gives
\[
 \|P_{b^\perp}Tb\|
 \le\frac{2(1+\sqrt2)q}{\sqrt3\,d}.
\]
Put \(\delta:=\sqrt2-1\), and choose \(k\) with \(b_k^2=\max_jb_j^2\ge1/3\).
Writing \(t_1=0,t_2=1,t_3=\sqrt2\), the diagonal variance identity gives
\[
 \|P_{b^\perp}Tb\|^2
 =\sum_{i<j}(t_i-t_j)^2b_i^2b_j^2
 \ge\frac{\delta^2}{3}(1-b_k^2).
\]
Since \(\|V\|\le1\), it follows that
\[
 \|u_k\|
 \le s_3(V)+\sqrt{1-b_k^2}
 \le\left(1+\frac{2(1+\sqrt2)}{d\delta}\right)q
 \le\frac{13q}{d}.
\]
The last inequality uses \(d\le1\) and \(1+2(1+\sqrt2)/\delta=7+4\sqrt2<13\).
Combining with (Three-channel-column-lower) yields \(q\ge d^2/[26(1+L)]\), proving the stated bound.

### A scalar joint gap also excludes approximate rank one

For the next conclusion, drop the a priori second-singular-value assumption and suppose that \(g>0\) satisfies
\[
 \|(C-aI)u\|^2+\|(D-bI)u\|^2\ge g^2
 \tag{Three-channel-scalar-gap-input}
\]
for every real unit \(u\) and every real \(a,b\).
It suffices to assume this for \(|a|\le\|C\|\), \(|b|\le\|D\|\), since these boxes contain the minimizing Rayleigh quotients.
Define
\[
 \beta:=\left(1+\frac{\sqrt3\|D\|}{g}
                  +\frac{18}{g\delta}\right)^{-1}.
\]
For every pair of real unit vectors \(u\in\mathbb R^n\), \(a\in\mathbb R^3\), one has
\[
 \|\mathcal F_\lambda(ua^T)\|_F\ge\beta.
 \tag{Three-channel-rank-one-residual}
\]

To prove this, set \(c_u=\langle u,Cu\rangle\), \(d_u=\langle u,Du\rangle\), \(r_C=(C-c_uI)u\), \(r_D=(D-d_uI)u\), and \(r=\|\mathcal F_\lambda(ua^T)\|_F\).
Projection onto \(u^\perp\) gives \(r_Ca^T+r_D(Ta)^T\), while projection onto \(\mathbb Ru\) gives the row vector
\[
 ((c_u-\lambda)a+d_uTa+Ka)^T.
\]
The \(2\)-by-\(2\) Gram matrix of \(a,Ta\) has trace at most three and determinant
\[
 \sigma^2:=\|P_{a^\perp}Ta\|^2.
\]
Its smaller eigenvalue is therefore at least \(\sigma^2/3\).
Using (Three-channel-scalar-gap-input) for \(r_C,r_D\), the first projection yields
\[
 r^2\ge\frac{\sigma^2}{3}
             (\|r_C\|^2+\|r_D\|^2)
 \ge\frac{\sigma^2g^2}{3}.
\]
Choose \(k\) with \(a_k^2\ge1/3\) and put \(\rho=\sqrt{1-a_k^2}\).
The same diagonal variance identity used above gives
\[
 \rho\le\frac{\sqrt3\,\sigma}{\delta}
       \le\frac{3r}{g\delta}.
\]
For \(b=\operatorname{sgn}(a_k)e_k\), one has \(\|a-b\|\le\sqrt2\rho\).
Since \(b^TKb=0\), \(\|K\|=\sqrt2\) and \(\|Kb\|\ge1\),
\[
 \|P_{a^\perp}Ka-Kb\|
 \le3\|K\|\|a-b\|\le6\rho,\qquad
 \|P_{a^\perp}Ka\|\ge1-6\rho.
\]
Projecting the second residual row onto \(a^\perp\) also gives
\[
 \|P_{a^\perp}Ka\|\le r+\|D\|\sigma.
\]
Together these inequalities imply
\[
 1\le r\left(1+\frac{\sqrt3\|D\|}{g}
                   +\frac{18}{g\delta}\right),
\]
which proves (Three-channel-rank-one-residual).

Now let \(\|V\|_F=1\), write its leading singular decomposition as \(V=sua^T+E\), and put \(J=L+\sqrt2\), \(\varepsilon=\|\mathcal F_\lambda(V)\|_F\).
Then \(s=s_1(V)\ge1/\sqrt3\), \(\|E\|_F\le\sqrt2s_2(V)\) and \(\|\mathcal F_\lambda(E)\|_F\le J\|E\|_F\).
Consequently
\[
 \frac{\beta}{\sqrt3}
 \le s\beta
 \le\varepsilon+\sqrt2J\,s_2(V).
\]
If \(\varepsilon\le\beta/(2\sqrt3)\), this yields
\[
 s_2(V)\ge d_*:=\frac{\beta}{2\sqrt6(L+\sqrt2)}.
 \tag{Three-channel-second-mode-lower}
\]
In particular \(\varepsilon\le d_*/2\) suffices for both this conclusion and (Three-channel-covariance-lower) with \(d=d_*\).
Thus bounded input norms and a positive scalar joint gap give a uniform combined covariance lower bound for all normalized sufficiently accurate modes in a fixed bounded energy range.
This concerns \(G(V)\), not the single-input Gram \(V^TV\), and does not contradict the preceding two-dimensional example.

### A conditional tail-projection transfer

Let \(Q\) be an orthogonal projection with
\[
 \|QC\|\le B_C,\qquad \|QD\|\le B_D,
\]
and put \(W=QV\), \(e=\|(I-Q)V\|_F\).
On \(\operatorname{ran}Q\), use \(C_Q=QCQ\), \(D_Q=QDQ\).
The exact compressed equation is
\[
 C_QW+D_QWT+WK-\lambda W=R_Q,
 \qquad
 R_Q=QR-QC(I-Q)V-QD(I-Q)VT,
\]
where \(R=\mathcal F_\lambda(V)\).
Hence
\[
 s_2(W)\ge d-e,\qquad
 \|R_Q\|_F\le\varepsilon+(B_C+\sqrt2B_D)e.
\]
If \(s_2(V)\ge d\), \(\|V\|_F\le1\) and
\[
 e\le d/2,\qquad
 \varepsilon+(B_C+\sqrt2B_D)e\le d/4,
 \tag{Three-channel-projection-premises}
\]
then (Three-channel-covariance-lower), with lower singular bound \(d/2\), applies to \(W\).
Orthogonality gives \(G(V)=G(QV)+G((I-Q)V)\), so
\[
 G(V)\succeq G(W)\succeq
 \frac{d^4}{10816(1+B_C+\sqrt2B_D+|\lambda|)^2}I_3.
 \tag{Three-channel-projected-covariance}
\]
The accepted [bounded-compression construction](../claims/Yin_C_F0187_v13.md#bounded-compression) supplies bounded \(QC,QD\) after the permitted conditioning on the first input and the second-input tail.
Its small discarded dimension alone does not bound \(e\) for the new three-channel modes.
No original-law probability estimate for (Three-channel-projection-premises), nor an applicable projected joint-gap input that automatically replaces it, has been proved here.
The second singular bound obtained above also uses full bounded norms and the stated uncompressed joint gap; it cannot be transferred to finite variance by silently replacing those norms with compressed norms.

### Exposing both original rows gives the combined Gram

Let \(U:\mathcal H\to\mathbb R^{3n}\) be an isometric embedding of a real spectral subspace of the actual minor, with component maps \(U_i:\mathcal H\to\mathbb R^n\).
For \(h\in\mathcal H\), put \(V_h=[U_1h\ U_2h\ U_3h]\) and define
\[
 \widetilde U_i h=(U_ih,t_iU_ih)\in\mathbb R^n\oplus\mathbb R^n.
\]
Then the three-component Gram of \((\widetilde U_i h)_i\) is exactly \(G(V_h)\).
Under the bounded-norm and scalar joint-gap assumptions above, fix a center \(\lambda_0\) and evaluate \(L,d_*\) at \(\lambda=\lambda_0\).
If the spectral subspace lies in \([\lambda_0-\rho,\lambda_0+\rho]\) with \(\rho\le d_*/2\), then every unit \(h\) gives \(\|V_h\|_F=1\) and \(\|\mathcal F_{\lambda_0}(V_h)\|_F\le\rho\).
The two deterministic bounds therefore give a strict whole-subspace combined Gram bound with
\[
 g_3=\frac{d_*^4}{676(1+L)^2}.
\]
In particular, at \(\lambda_0=0\) this holds on the whole range of \(\mathbf1_{[-\rho,\rho]}(\mathcal L)\), where \(\mathcal L=I_3\otimes C+T\otimes D+K\otimes I_n\), including arbitrary combinations of its low eigenmodes.
It does not give the single-input three-component Gram excluded by the earlier example.

After conditioning on the two retained input minors and the removed diagonal entries, keep both original normalized border vectors \(x,y\) fresh.
Their coordinates come from the two original independent laws.
For a spectral inverse contribution \(Z=U\mathsf A U^*\), with a real selfadjoint operator \(\mathsf A\) on \(\mathcal H\), its quadratic Schur matrix is
\[
 \left[
 \left\langle U_i^*x+t_iU_i^*y,\,
       \mathsf A(U_j^*x+t_jU_j^*y)\right\rangle
 \right]_{i,j=1}^3
 =
 \left[
 \left\langle\widetilde U_i^*(x,y),\,
       \mathsf A\widetilde U_j^*(x,y)\right\rangle
 \right]_{i,j=1}^3.
 \tag{Three-channel-two-input-layer}
\]
For the full inverse its determinant, up to sign, is the degree-six homogeneous layer of the actual Schur determinant.
Keeping only a low spectral contribution gives its corresponding degree-six polynomial, not an identity discarding the other inverse modes.
This exposure retains the second original border rather than conditioning it away, and so makes the combined Gram relevant to the actual two-input polynomial.

The stacked maps \(\widetilde U_i\) need not be isometric, but
\[
 I_{\mathcal H}\preceq
 S:=\sum_i\widetilde U_i^*\widetilde U_i
   =\sum_i(1+t_i^2)U_i^*U_i
 \preceq3I_{\mathcal H}.
\]
The maps \(\widehat U_i=\widetilde U_iS^{-1/2}\) therefore have an isometric stack.
If the combined Gram lower bound is \(g_3\|h\|^2I_3\), their whole-subspace Gram lower bound is at least \((g_3/3)\|h\|^2I_3\).
The quadratic matrix in (Three-channel-two-input-layer) is preserved by replacing \(\mathsf A\) with \(S^{1/2}\mathsf A S^{1/2}\) at the same time.
This normalization does not prove a determinant-energy bound.
Uniform control on the relevant original-law low spectral subspaces, the finite-second-moment projection interface, quantitative sixth-degree energy after physical-index collisions, coefficient loads and a compatible actual graph-distance bridge all remain necessary unresolved steps.

<a id="finite-channel-noncancellation-continuation"></a>
## Finite-channel noncancellation and a quaternionic test

The continuing signed-weight question led to the [reviewed finite-channel theorem](../claims/Yin_C_F0187_v16.md#decision-finite-channel-reviewed), whose fixed proof owns the general exact nonvanishing and quantitative compactness arguments.
Its [independent whole-proof finding](../audits/reviews/Yin_R_F0191_v16.md#finite-channel-signed-determinant-reviewed) covers those exact conditional assertions.
The theorem covers every fixed real channel number under its injectivity or strict whole-subspace Gram hypotheses, including arbitrary signs and rank above three.
It concerns the raw polynomial and leaves the actual-model and distinct-coordinate interfaces above unchanged.
For the preceding combined maps, suppose additionally that the unnormalized spectral weight satisfies \(\|\mathsf A\|_F^2\le K\|\mathsf A\|^2\) and \(s_3(\mathsf A)\ge d\|\mathsf A\|>0\).
Writing \(\widehat{\mathsf A}=S^{1/2}\mathsf A S^{1/2}\), the bounds \(I\preceq S\preceq3I\) give
\[
 \|\mathsf A\|\le\|\widehat{\mathsf A}\|\le3\|\mathsf A\|,
 \qquad \|\widehat{\mathsf A}\|_F^2\le9K\|\widehat{\mathsf A}\|^2,
 \qquad s_3(\widehat{\mathsf A})\ge(d/3)\|\widehat{\mathsf A}\|.
\]
The last inequality follows by applying the singular-value product bound to \(\mathsf A=S^{-1/2}\widehat{\mathsf A}S^{-1/2}\).
Thus the theorem applies with parameters \((p,g,K,d)=(3,g_3/3,9K,d/3)\) and supplies a raw degree-six lower bound at scale \(\|\mathsf A\|^3\) in this comparable-mode branch.
It supplies no such uniform scale when the third singular value is allowed to vanish relative to the first.
The maximum-rank method uses the inspected transitive-space input DMR08; a bounded search on 2026-11-06 for transitive singular matrix spaces and locally linearly dependent operators located its [precise source inspection](../audits/literature/DMR08/Yin_U001.md#finite-dimensional-transitive-invertible).
The search stopped once that input supplied the needed real finite-dimensional step, whose adaptation is explicit in the fixed proof.
No novelty or exhaustive-literature claim is made.

The following ordinary calculation was another test of possible signed cancellation during this exploration.
It is retained to distinguish the failed counterexample candidate from the earlier cross-product example that violates strict Gram separation.
On \(\mathbb R^4\), define
\[
 J(a,b,c,d)=(-b,a,-d,c),\qquad
 K(a,b,c,d)=(-c,d,a,-b),\qquad L=JK,
\]
\[
 (U_1,U_2,U_3)=\frac1{\sqrt3}(I,J,K).
\]
The matrices \(J,K,L\) are skew orthogonal, \(J^2=K^2=-I\), and \(JK=-KJ\).
Direct inner products give
\[
 \sum_i\|U_i h\|^2=\|h\|^2,\qquad
 [\langle U_i h,U_jh\rangle]_{i,j=1}^3
 =\frac{\|h\|^2}{3}I_3.
\]
For every real symmetric \(A\in M_4(\mathbb R)\), put
\[
 B_A(x)=[\langle U_i^*x,A U_j^*x\rangle]_{i,j=1}^3.
\]
For \(x\ne0\), the first three columns of the orthogonal matrix
\[
 O_x=\frac1{\|x\|}[x\ {-Jx}\ {-Kx}\ Lx]
\]
span \((Lx)^\perp\).
The top-left principal cofactor of order three in \(O_x^T A O_x\) is its fourth diagonal adjugate entry.
For invertible \(A\), use \(\operatorname{adj}(O_x^TAO_x)=O_x^T\operatorname{adj}(A)O_x\); the identity for singular \(A\) follows by polynomial continuity.
Keeping the three normalization factors gives
\[
 \det B_A(x)
 =\frac{\|x\|^4}{27}(Lx)^T\operatorname{adj}(A)(Lx).
 \tag{Quaternionic-sixth-layer}
\]
Both sides are zero at \(x=0\), so the formula holds there as well.
Since \(L\) is orthogonal and \(\operatorname{adj}(A)\) is symmetric,
\[
 \sup_{\|x\|=1}|\det B_A(x)|
 =\frac{\|\operatorname{adj}(A)\|}{27}
 =\frac{s_1(A)s_2(A)s_3(A)}{27}.
\]
In particular \(\|A\|=1\) and \(s_3(A)\ge d\) imply the lower bound \(d^2/27\), including rank-four indefinite weights.
This rules out the four-dimensional quaternionic candidate as a counterexample to strict-Gram raw separation.
It does not bound a six-distinct-coordinate sign layer; in four physical coordinates such a layer is empty.

For completeness, take two identical quaternionic blocks on \(\mathbb R^8\) and a block-diagonal symmetric weight \(A=\operatorname{diag}(A_1,A_2)\).
If either block has rank at least three, vectors supported in that block give a nonzero determinant by the preceding identity.
If the total rank is at least three and neither block has rank three, one block has rank two and the other is nonzero; relabel them in that order.
Choose \(x_1\ne0\) with \(Lx_1\in\ker A_1\).
The corresponding compression \(B_1(x_1)\) has rank two, because its three-dimensional compression space contains \(\operatorname{ran}A_1\).
Let \(c\ne0\) span its kernel, so \(\operatorname{adj}B_1=\kappa cc^T\) for a nonzero scalar \(\kappa\).
The matrix \(U(c)=(c_1I+c_2J+c_3K)/\sqrt3\) is invertible, since \(U(c)^TU(c)=\|c\|^2I/3\).
Thus some \(y\) satisfies
\[
 c^TB_2(y)c=\langle U(c)^*y,A_2U(c)^*y\rangle\ne0.
\]
Both \(B_1\) and \(B_2\) have zero determinant, and
\[
 \det(B_1+tB_2)
 =t\,\operatorname{tr}(\operatorname{adj}B_1 B_2)
   +t^2\operatorname{tr}(\operatorname{adj}B_2 B_1)
\]
has a nonzero linear coefficient.
For some \(t>0\), the vector \((x_1,\sqrt t\,y)\) therefore gives a nonzero determinant.
This further direct test covers only block-diagonal weights; the fixed finite-channel theorem supplies the separate general argument.

<a id="three-channel-distinct-layer-transfer"></a>
## Comparable-mode use of the fixed physical collision and load estimates

The complete fixed-degree collision, coefficient-normalization and load arguments are now retained in [C187v18](../claims/Yin_C_F0187_v18.md#physical-high-rank-transfer), with its [adopted independent review](../claims/Yin_C_F0187_v18.md#decision-high-rank-tensor-reviewed).
Those local estimates do not require a high effective rank; that hypothesis is used there to supply one particular raw tensor lower bound.
The following comparable-mode application instead uses a separate raw lower bound, potentially supplied by [C187v16](../claims/Yin_C_F0187_v16.md#statement) after its actual geometric and spectral hypotheses are established.
This remains a conditional application, not an unconditional random-matrix conclusion.

For fixed channel number \(p\) and fixed real slopes \(t_1,\ldots,t_p\), use the exact local objects of C187v18:
\[
 Z=Z^T\ne0\in M_{pn}(\mathbb R),\quad
 F=\|Z\|_F,\quad Q=\|Z\|,\quad
 P_i=I_p\otimes e_ie_i^T,
\]
\[
 d_i=\|P_iZ\|_F^2,\quad d_*=\max_i d_i,\quad
 \mathcal D=\sum_i\|P_iZP_i\|_F^2,
 \qquad R(x,y)e_a=e_a\otimes(x+t_a y).
\]
Let \(h_Z(x,y)=\det(R(x,y)^TZR(x,y))\), and let \(\mathscr T\) be its arithmetic-average symmetric tensor of order \(2p\).
Assume fixed \(b>0,K\ge1\) satisfy
\[
 \sup_{\|z\|=1}|h_Z(z)|\ge bQ^p,
 \qquad F^2\le KQ^2.
\]
Cauchy--Schwarz gives \(\|\mathscr T\|_F\ge bQ^p\).
The fixed collision estimate and its exact coefficient normalization then give
\[
 \|\mathscr T_{\rm dist}\|_F^2
 \ge b^2Q^{2p}-C_{p,t}F^{2p-2}(\mathcal D+d_*),
 \qquad
 \sigma_{2p,\rm phys}^2
 =\frac{(2p)!}{N^{2p}}\|\mathscr T_{\rm dist}\|_F^2.
\]
Here distinct means all physical positions differ, and the sign substitution retains the original parent scale \(N^{-1/2}\), even for a smaller minor.
The two input coordinates at a physical position remain separate independent variables.
If \((\mathcal D+d_*)/F^2\to0\), the relative collision error is at most
\(C_{p,t}K^p(\mathcal D+d_*)/F^2\to0\).
Consequently, eventually
\[
 \sigma_{2p,\rm phys}^2
 \ge \frac{(2p)!b^2Q^{2p}}{2N^{2p}}.
\]
For \(p=3\) this is the bound \(360b^2Q^6/N^6\).
The fixed complete-layer load estimate is
\[
 L_i^{(2p)}\le C_{p,t}F^{2p-2}d_i/N^{2p}.
\]
The complete layer includes coefficients using both input coordinates at one physical position and has energy at least \(\sigma_{2p,\rm phys}^2\).
Thus its maximum normalized group load is at most
\(C_{p,t,b}K^p d_*/F^2\to0\).
Physical diagonal spread and physical row spread remain separate inputs; the second is not being used to infer the first.
No channel number or slope bound grows with dimension.
The third-mode comparability used to obtain the three-channel raw input is not needed again in this transfer.
Actual-model spread, raw noncancellation outside the comparable-mode and adopted high-rank ranges, and a compatible conditional graph-distance conversion remain separate obligations.

<a id="three-channel-two-column-exclusion"></a>
## Original-law combined-Gram continuation and its application boundary

The complete original finite-second-moment three-channel argument is fixed in [C187v19](../claims/Yin_C_F0187_v19.md#statement), whose responsible decision determines its current assessment.
Its [three column estimates and whole-subspace assembly](../claims/Yin_C_F0187_v19.md#argument) use the adopted C187v17 second-singular-value input and retain all full and single-deletion minors, bounded energy ranges, approximate modes and whole low spectral subspaces.
The two opposite conditioning constructions are established as separate original-law events before their unconditional intersection.
No whole-subspace Gram conclusion is inferred merely from checking one eigenbasis.
The complete proofs are retained there rather than duplicated in this continuing application draft.

<a id="three-channel-quadratic-endpoint"></a>
### Why the projected linear endpoint argument alone was insufficient

The [fixed quadratic endpoint proof](../claims/Yin_C_F0187_v19.md#quadratic-endpoint-reduction) uses a full-vector approximation followed by two rectangular copy differences.
The following failed linear shortcut remains useful when testing propagation to another coefficient tuple.
Under the conditioning on the complete first input and the second-input tail, write \(D=\Theta+W\), let \(Q\) be the conditioned bounded compression, and put \(V_0=\ker Q\).
Suppose the three residuals of the path pencil have norms at most \(\varepsilon\), the compressed channel norms are at most \(B\), and \(\|u_1\|\le b_1\).
The first equation gives \(\|Qu_2\|\le Bb_1+\varepsilon\).
Let \(z_2\) be the projection of \(u_2\) onto \(V_0\), and let \(P_0\) project onto
\(\operatorname{Ran}Q\cap(V_0+CV_0+\Theta V_0)^\perp\).
The second equation then gives only
\[
 \|P_0u_3+P_0Wz_2\|
 \le\varepsilon+b_1+B(Bb_1+\varepsilon).
\]
The image \(P_0WV_0\) depends on the unexposed coordinates, so a noise bound for a subspace fixed before exposure cannot be invoked on that image.
This projected relation alone does not place the full \(u_3\) near a fixed small subspace.
Multiplying the small error in \(u_2\) by an uncompressed input would require an unavailable operator-norm bound.
Likewise, selfadjoint pairing cancels the common \(C-\lambda I\) terms but yields only
\[
 (\alpha-1)\langle u_3,Du_2\rangle
 =\|u_3\|^2-\|u_2\|^2+\langle u_1,u_3\rangle
   -\langle u_3,r_2\rangle+\langle u_2,r_3\rangle.
\]
The compressed bounds do not control this uncompressed mixed inner product.
These observations delimit the linear shortcut; they do not contradict the fixed quadratic argument or the original Tasks.

For the determinant application, [C187v20](../claims/Yin_C_F0187_v20.md#inverse-and-truncation) now supplies the complete-inverse cutoff comparison and physical diagonal and maximum row-energy spread for this original three-channel model, uniformly over every fixed deletion count on the actual invertible branches.
The inverse energy and cutoff comparisons are almost sure, while the physical spread ratios are asserted in probability.
The [conditional low-rank theorem C187v21](../claims/Yin_C_F0187_v21.md#statement) supplies raw quadratic and quartic bounds under its first- and second-pole gaps and small-corner conditions, and a product-scale raw sixth bound under its third-to-fourth pole gap.
The [mixed head-residual theorem C187v22](../claims/Yin_C_F0187_v22.md#statement) additionally treats the specified separated one- or two-mode heads when the residual has bounded effective rank on its own scale, without requiring a gap after the third pole.
Its whole-support Gram requirement is available only on the permitted low spectral subspace in the original model, so the [product-scale tail comparison](../claims/Yin_C_F0187_v22.md#three-channel-use-and-limits) must still be checked in an application.
The later [mixed high-residual theorem](../claims/Yin_C_F0187_v23.md#statement) and [all-scale physical assembly](../claims/Yin_C_F0187_v24.md#statement) supply the remaining spectral branches and compatible complete sixth-layer energy and loads for the actual original-model inverse.
The [adopted original-row bridge and floor](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed) supply the separate graph-normalized probability argument, common-shift treatment of singular minors and unshifted least-value floor.
The complete lower Walsh-layer cancellation warning remains valid, while this assembly uses the highest sixth layer.
The separate [adopted middle theorem](../claims/Yin_C_F0187_v25.md#decision-three-channel-middle-reviewed) and [complete assembly](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed) now supply the fixed-model determinant conclusion.
This completed three-channel test resolves its fixed real coefficient tuple and repeated-variable cubic at zero; arbitrary coefficients and polynomials in F13 and F14 retain their original obligations.

<a id="three-channel-physical-spread"></a>
## Three-channel physical spread and the complete-inverse interface

The original real finite-second-moment three-channel path model now has the [fixed complete-inverse theorem C187v20](../claims/Yin_C_F0187_v20.md#statement), under its [proved decision](../claims/Yin_C_F0187_v20.md#decision-three-channel-physical-reviewed).
Its [complete argument](../claims/Yin_C_F0187_v20.md#argument) owns the fixed-deletion Gram extension, free zero-mass calculation, weighted weak limits, conditional fresh-row covariance, physical Schur estimate and separate row and diagonal energy bounds.
Those proofs are retained there rather than duplicated in this application draft.

For every fixed number of physical deletions and deterministic parent shift \(\theta_N\to0\), its conclusions are uniform on the actual invertible branches, without conditioning by the probability of invertibility or imposing a bounded original-input norm.
The [weighted weak limits](../claims/Yin_C_F0187_v20.md#weighted-weak-limits), divergence \(\|Z\|_F^2/n\to\infty\), and [complete-inverse cutoff comparison](../claims/Yin_C_F0187_v20.md#inverse-and-truncation) are almost sure.
The physical diagonal and maximum row-energy ratios tend to zero in probability, as do the corresponding ratios for the low-cutoff inverse and fixed-mode residuals.
The combined-Gram event's common \(o(1)\) error is not upgraded to a summable bound.

The [actual high-effective-rank application](../claims/Yin_C_F0187_v20.md#actual-high-rank-coefficients) supplies C187v18's complete-inverse quadratic separation, distinct-physical sixth-layer energy and complete grouped loads with the original \(N^{-1/2}\) border normalization.
The two input coordinates at a physical position remain separate variables.
Its sign substitution is a formal coefficient calculation; conversion under the original finite-variance row law and graph normalization remains a separate application.

For the full spectral range, the [low-rank application entrance](Yin_D_F0033.md#three-channel-low-rank-probe) now links the adopted C187v24 assembly; the stronger coarse product-scale condition of the earlier C187v21 remains a conditional interface rather than an assumption of that assembly.
The [atom-avoiding shift](../claims/Yin_C_F0187_v20.md#atom-avoidance-and-scope) provides literal shifted inverses, not an unshifted floor.
Neither fixed-deletion physical spread nor this high-rank coefficient interface proves the middle logarithmic estimate, a determinant limit, arbitrary coefficient propagation or either original Task.

<a id="three-channel-sixth-row-bridge"></a>
## Two-original-row sixth-degree bridge and the reviewed fixed-model floor

The later [adopted all-scale coefficient theorem C187v24](../claims/Yin_C_F0187_v24.md#statement) supplies complete sixth energy, vanishing physical-group load and bounded-boundary graph area for every required fixed-deletion actual inverse.
The complete original-row conversion and floor argument is fixed in [C194v16](../claims/Yin_C_F0194_v16.md#statement), under its [proved assessment](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed).
Its [two-law copy construction](../claims/Yin_C_F0194_v16.md#two-law-copy-thinning) keeps both original independent finite-second-moment borders and pays the entire paired-support failures only through physical averaging.
The [three-column graph and averaging argument](../claims/Yin_C_F0194_v16.md#three-column-graph) yields a conditional threshold \(cb_N^{-3}N^{-7}\), with arbitrary independent exposed diagonals and no inverse-norm assumption.
For the original fixed real laws, the [reviewed application](../claims/Yin_C_F0194_v16.md#original-model-floor) uses \(b_N=B\sqrt N\) and one atom-avoiding shift below \(N^{-10}\) to obtain an unshifted \(aN^{-17/2}\) probability floor.
The same floor passes to the ordered cubic \((C+\sqrt2D)(C+D)C-2C-\sqrt2D\) through the exact [upper-right inverse block identity](../claims/Yin_C_F0194_v16.md#cubic-inverse-block).
The complete proof resides in the fixed C, with [independent whole-proof review](../audits/reviews/Yin_R_F0200_v16.md#sixth-original-row-whole-proof) covering the conditional bridge, original-model application and every direct interface.
The probability floor is not a summable almost-sure statement and alone supplies no middle negative-logarithmic estimate or determinant limit.
The separate middle and determinant conclusions are supplied by the reviewed assembly below; both general Task contracts remain unresolved.

<a id="three-channel-conditional-log-assembly"></a>
## Reviewed logarithmic assembly for the three-channel model

The complete assembly developed here is fixed in [C186v21](../claims/Yin_C_F0186_v21.md#statement), with its [full argument](../claims/Yin_C_F0186_v21.md#argument) and [proved assessment](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed).
The exact [adopted C187v25 middle theorem](../claims/Yin_C_F0187_v25.md#statement) supplies the original unshifted profile beyond \(6m_N=O(N^{5/6}(\log N)^{1/6})\), with exponent \(7/2\), one common vanishing exception and arbitrary inverse-power remainder.
Together with the [adopted C194v16 floor](../claims/Yin_C_F0194_v16.md#original-model-floor), this yields negative-logarithmic control and the fixed assembly's finite free targets, all-dimension logarithmic probability limits and every-coupling almost-sure limsup.
The [finite/free determinant step](../claims/Yin_C_F0186_v21.md#finite-and-free-determinants) retains the exact ordered cubic at zero and the normalization factor three, while the [coupling step](../claims/Yin_C_F0186_v21.md#every-coupling-limsup) uses the accepted fixed-regularizer upper bound and marginal criterion.
The complete proof no longer depends on this rolling Draft.
The [independent whole-proof finding](../audits/reviews/Yin_R_F0190_v20.md#finite-variance-three-channel-whole-proof) covers the complete assembly and every direct interface, including the separately reviewed and adopted middle input.
The theorem does not assert full-sequence almost-sure logarithmic convergence, a general coefficient or complex-input extension, Brown convergence or completion of either general Task.

<a id="positive-frame-energy-partition"></a>
## Positive-frame rectangles and the actual inverse-energy partition

The [adopted rectangle result](../claims/Yin_C_F0194_v18.md#decision-positive-frame-rectangles-reviewed) has its complete statement and proof in [C194v17](../claims/Yin_C_F0194_v17.md#statement).
It supplies an exponential all-small-physical-support bound and exact distance averaging under a positive complex coefficient frame, for every fixed auxiliary dimension and the original complex finite-second-moment laws.
The [adopted low inverse-energy result](../claims/Yin_C_F0194_v18.md#decision-low-inverse-energy-reviewed) separately gives direct complete-Schur and graph-distance control for arbitrary fixed real symmetric coefficients on invertible actual minors with normalized inverse energy at most a slowly growing K_N.
The probability errors vanish marginally and after averaging; no union over all minors is asserted.
The [adopted spectral-point geometry](../claims/Yin_C_F0187_v26.md#decision-positive-frame-spectral-spread-reviewed) now supplies residual energy and separate physical spread after each fixed number of head removals when zero belongs to the free spectrum.
The distinct free-gap branch with actual inverse energy above the slow threshold remains unresolved; weak convergence alone cannot exclude its isolated small finite-dimensional eigenvalues.
These exact interfaces preserve their separate coefficient and input-law scopes and do not yet supply the general positive-frame bottom floor or either determinant Task.

<a id="fixed-input-count-sixth-probability-bridge"></a>
## A fixed number of original input laws in the sixth-degree probability bridge

The complete conditional probability argument is fixed in [C194v19](../claims/Yin_C_F0194_v19.md#statement), with its current assessment at that material's exact selected decision.
It converts complete sixth coefficients and physical-group loads for any fixed number of original real laws into a norm-guarded positive-frame least-value bound at scale \(b_N^{-3}N^{-7}\), for sufficiently large N.
Its proof retains the original two-copy representation, the entire sign-support graph-area guard and the unconditional average of minor exceptions.
The [adopted fixed-d physical coefficient theorem](../claims/Yin_C_F0187_v27.md#decision-positive-frame-complete-sixth-reviewed) supplies those hypotheses on invertible spectral-point minors, and the [adopted C186v22 assembly](../claims/Yin_C_F0186_v22.md#decision-positive-frame-spectral-point-assembly-reviewed) supplies the common atom-avoiding shift and quantitative return to the unshifted parent at its exact spectral-point scope.
Actual high inverse energy in the free-gap branch is not covered by the adopted [spectral-point geometry](../claims/Yin_C_F0187_v26.md#decision-positive-frame-spectral-spread-reviewed).

<a id="positive-frame-spectral-point-log-assembly"></a>
## Original positive-frame spectral-point floors and logarithmic assembly

The complete original-model statement and assembly are fixed in [C186v22](../claims/Yin_C_F0186_v22.md#statement), with its [proved decision](../claims/Yin_C_F0186_v22.md#decision-positive-frame-spectral-point-assembly-reviewed) and [independent whole-proof review](../audits/reviews/Yin_R_F0190_v21.md#positive-frame-spectral-point-assembly-whole-proof).
The exact scope is real symmetric \(m=3\) coefficients with \(\chi_A>0\), zero in the free spectral support, fixed original real finite-second-moment laws, and arbitrary cross-size coupling.
The [common actual-minor shift](../claims/Yin_C_F0186_v22.md#common-atom-avoiding-shift), [measurable good events](../claims/Yin_C_F0186_v22.md#minor-good-events), and [Frobenius guard](../claims/Yin_C_F0186_v22.md#frobenius-norm-guard) match the adopted C187v27 and C194v19 interfaces without changing the original fresh-row law.
The [quantitative unshifted return](../claims/Yin_C_F0186_v22.md#unshifted-floor) gives the adopted \(aN^{-17/2}\) floor for the original pencil before any logarithm is taken.
The [middle and free-target step](../claims/Yin_C_F0186_v22.md#middle-and-free-target) and [complete logarithmic-tail assembly](../claims/Yin_C_F0186_v22.md#logarithmic-probability-limit) give finite free log and all-dimension probability logdet convergence.
The [coupling step](../claims/Yin_C_F0186_v22.md#every-coupling-limsup) separately combines the almost-sure regularized upper bound with the marginal favorable-subsequence criterion.
The [remaining scope](../claims/Yin_C_F0186_v22.md#scope-and-provenance) retains the free-gap high-energy branch and general F13/F14 coefficient and polynomial obligations.
The complete proof no longer depends on this rolling Draft; its adopted scope does not include the complementary free-gap branch or the general Task contracts.

<a id="free-gap-finite-pole-resonance"></a>
## Continuing free-gap research: actual inverse tails and strong resonance

The complete fixed-\(K\), real size-three inverse-approximation statement and proof are fixed in [C194v20](../claims/Yin_C_F0194_v20.md#statement), with its [proved decision](../claims/Yin_C_F0194_v20.md#decision-inverse-trace-norm-approximation-reviewed) and [independent whole-proof review](../audits/reviews/Yin_R_F0200_v22.md#inverse-trace-norm-approximation-whole-proof).
The current continuing questions are the actual free-gap inverse-tail probability input and the strong-resonance branch.
Keep the original fixed real finite-second-moment Wigner model, real symmetric \(A_0,\ldots,A_d\in M_3(\mathbb R)\), and the positive complex-direction frame \(\chi_A>0\).
Write \(L_N=A_0\otimes I_N+\sum_jA_j\otimes W_j^{(N)}\) and \(L=A_0\otimes1+\sum_jA_j\otimes s_j\), and assume zero lies in a free spectral gap.

### The total-loss target remains sufficient without a pointwise floor

Fix \(0<g<\operatorname{dist}(0,\sigma(L))\), put \(v=\log\Delta_{\operatorname{tr}_3\otimes\tau}(L)\in\mathbb R\), and define
\[
 D_N(g)=\frac1{3N}\sum_{|\lambda_a(L_N)|<g}
                 \log\frac g{|\lambda_a(L_N)|}.
\]
An exact zero eigenvalue contributes \(+\infty\), rather than being removed from the sum.
The [fixed target comparison](../claims/Yin_C_F0194_v20.md#model) gives \(X_N=Y_N(g)-D_N(g)\), with \(Y_N(g)\to v\) almost surely under every coupling by C186v4.
Thus \(D_{N_\ell}(g)\to0\) in probability along deterministic dimensions remains a sufficient direction for the original determinant limsup contract.
Neither the free gap nor the fixed conditional theorem supplies this total-loss estimate.

<a id="inverse-trace-norm-approximation"></a>
<a id="inverse-trace-norm-stability"></a>
<a id="inverse-trace-norm-schur-graph"></a>
<a id="inverse-trace-norm-parent-interface"></a>
### Fixed conditional interface

[C194v20](../claims/Yin_C_F0194_v20.md#statement) uses an actual invertible minor \(M\) and a minor-measurable selfadjoint approximation \(E\) with \(\|E\|_F^2/N\le K\) for fixed \(K\), and \(\|M^{-1}-E\|_1/N\le\delta_N\to0\).
Its complete [noncommuting comparison](../claims/Yin_C_F0194_v20.md#inverse-trace-norm-stability) and [original-row Schur/graph estimates](../claims/Yin_C_F0194_v20.md#inverse-trace-norm-schur-graph) are fixed there and require neither a rank bound nor physical spread.
The [parent interface](../claims/Yin_C_F0194_v20.md#inverse-trace-norm-parent-interface) explicitly assumes vanishing mean approximation failure and gives a conditional \(cN^{-2}\) floor.
The common atom-avoiding shift must be the same shift at which that probability premise holds, and it is returned to zero before logarithms.
The [logarithmic assembly](../claims/Yin_C_F0194_v20.md#conditional-logarithmic-assembly) yields probability convergence on the dimensions satisfying the extra premise and an every-coupling limsup.
These conditional implications are adopted; the actual probability premise is not established or derived from the free gap.

<a id="finite-poles-and-trace-tail-boundary"></a>
### The missing actual inverse-tail probability

The [fixed finite-pole comparison](../claims/Yin_C_F0194_v20.md#finite-poles-and-trace-tail-boundary) allows fixed or growing pole counts when their total inverse nuclear error is \(o(N)\).
It also retains the distinction that \(k_N=o(N)\) alone controls the background resolvent comparison, but does not control the full head correction by that argument.
For the canonical gap truncation
\[
 E=M^{-1}\mathbf1_{\{|M|\ge g\}},\qquad
 \frac{\|E\|_F^2}{N}\le3/g^2,
\]
the new actual-model probability input would control
\[
 \frac1N\sum_{|\lambda_a(M)|<g}|\lambda_a(M)|^{-1}
\]
by a deterministic \(\delta_N\to0\), with averaged failure tending to zero along favorable deterministic dimensions.
Exact zeros count as infinite error unless the same deterministic common shift has already removed them.
The free gap gives a vanishing normalized count of gap modes, not this inverse-first-moment tail.
For the original parent, the corresponding inverse-tail condition would imply \(D_N(g)\to0\) directly by the [fixed total-loss bound](../claims/Yin_C_F0194_v20.md#finite-poles-and-trace-tail-boundary).
It is only sufficient and is not proposed as necessary for the original determinant contract.
Proving either actual inverse-tail condition remains a new probability problem, rather than an automatic consequence of restating the conditional interface.

### The unresolved strong-resonance test

Use the actual minor and border notation of [C194v20](../claims/Yin_C_F0194_v20.md#statement), and split spectrally
\[
 Z=M^{-1}=E+\sum_{\ell=1}^{k}\lambda_\ell e_\ell e_\ell^T,
 \qquad Ee_\ell=0,\qquad \|E\|_F^2/N\le K
\]
with orthonormal inverse eigenmodes and fixed \(K\).
Define
\[
 S_E=A_N+D_i-R^TER,\quad
 Y=(R^Te_1,\ldots,R^Te_k),\quad
 \Lambda_{\rm h}=\operatorname{diag}(\lambda_1,\ldots,\lambda_k).
\]
The exact algebra is
\[
 S=S_E-Y\Lambda_{\rm h}Y^T,\qquad
 \det S=\det S_E\det(I_k-\Lambda_{\rm h}Y^TS_E^{-1}Y)
\]
whenever \(S_E\) is invertible.
The fixed rank-background comparison and residual-row concentration explain the stability of \(S_E\), while the complete Schur proof absorbs the second term only through its small normalized nuclear error.
For \(k=1\) and \(|\lambda|\gtrsim N\), the unhandled factor remains
\[
 1-\lambda\,y^TS_E^{-1}y.
\]
The objects \(y\) and \(S_E\) use the same original fresh rows; covariance positivity does not make them independent or exclude atomic resonance.
A negative-logarithmic-loss estimate for this factor under the actual original law along favorable deterministic dimensions would be a different new probability input.
No such estimate is proved here, and an unrelated prescribed-minor example would not settle it.

The [actual gapped example in L63v3](../ledger/Yin_L_F0063_v3.md#positive-frame-physical-boundary) rules out imposing vanishing physical diagonal energy on the whole inverse, but does not rule out the pole/background distinction.
The [favorable-subsequence rank-times-log estimate](Yin_D_F0033.md#favorable-subsequence-tail-rank) controls clipped logarithms only.
The [vanishing-entry truncation obstruction](#vanishing-entry-truncation-norm-obstruction) shows that the truncated norm can still diverge along that same subsequence.
Neither fact supplies the missing lower clipping or a bounded operator-norm core.
The inspected [BC17 boundary in L61v1](../ledger/Yin_L_F0061_v1.md#source-frontier) retains its carried third- and fourth-moment hypotheses; no new external bare-second-moment result has been inspected or adopted here.

<a id="strong-single-pole-rectangle-test"></a>
## Continuing after the fixed strong-single-pole test

The complete bounded mechanism test is fixed in [L63v4](../ledger/Yin_L_F0063_v4.md#strong-single-pole-rectangle-test), as ordinary exploration without an independent review or a new Claim assessment.
Its [exact real model](../ledger/Yin_L_F0063_v4.md#model) retains a real unit eigenvector of the actual minor and its signed real inverse eigenvalue.
The [actual-minor rectangle calculation](../ledger/Yin_L_F0063_v4.md#actual-minor-spread) gives \(cN^{-3/2}\) physical block lower bounds, and the [frozen proxy calculation](../ledger/Yin_L_F0063_v4.md#frozen-proxy) gives linear matching at scale \(cN^{-3}\) and its original-law degree-two small-ball estimate.
The [same-row comparison](../ledger/Yin_L_F0063_v4.md#same-row-gap) only gives \(o_{\mathbb P}(1)\) error for the normalized complete Schur polynomial, which does not transfer that polynomial-window estimate.
The [exact graph interface](../ledger/Yin_L_F0063_v4.md#graph-interface) retains and cancels the large-pole scale without resolving the complete-polynomial probability input.

The remaining ordinary question is direct control of the full polynomial \(P_N=(N/\lambda)\det S\), or of its complete coefficients after conditional original-law pairing, under these actual-minor hypotheses.
The [fixed outcome](../ledger/Yin_L_F0063_v4.md#conclusion) does not infer survival of the proxy matching when the residual-dependent terms use those same fresh variables.
No estimate for this next step, actual-law resonance counterexample, or completed determinant branch has been obtained.

<a id="strong-pole-complete-polynomial-test"></a>
## Complete strong-pole test and the remaining coefficient problem

The complete bounded investigation is fixed in [L63v5](../ledger/Yin_L_F0063_v5.md#strong-pole-complete-polynomial-test), as ordinary exploration and authoring self-checking rather than an independent review or Claim assessment.
Its [opposite-sign definite branch](../ledger/Yin_L_F0063_v5.md#opposite-sign-complete-schur) controls the complete original-row polynomial and its exact graph normalization, with fresh-row good events handled only by intersection and probability errors.
Its [actual finite-variance example](../ledger/Yin_L_F0063_v5.md#paired-coefficient-l2-obstruction) shows that an untruncated squared average of complete paired quadratic coefficients may diverge, including on a positive-probability actual strong-pole event.
The example does not refute a direct original-law small-ball estimate, and the controlled sign branch has no established probability coverage.

<a id="complete-pole-next-interface"></a>
### Continuing complete-coefficient question

The [remaining interface](../ledger/Yin_L_F0063_v5.md#complete-pole-next-interface) concerns same-sign definite resonance, indefinite backgrounds, and their actual-model probabilities.
A bounded or weighted pairing argument must control the full coefficients with repeated-variable collisions and its exact original-law probability cost, rather than only the frozen quadratic proxy.
Keep that coefficient or polynomial estimate aligned with the exact graph scale; no general free-gap determinant conclusion follows from the completed test.

<a id="extreme-pole-definite-background-test"></a>
## Extreme single poles and the remaining resonance band

The complete bounded test is fixed in [L63v6](../ledger/Yin_L_F0063_v6.md#extreme-pole-definite-background-test), as ordinary exploration and authoring self-checking without independent review or Claim adoption.
For the same actual real size-three single-pole model, a definite stable residual background and \(|\lambda|\ge\Lambda_0N^4\) permit an original-law complete Schur estimate for either pole sign.
The exact graph normalization gives an \(N^{-3}\) determinant threshold and, on the parent norm intersection, an \(N^{-4}\) distance threshold, with failure tending to zero uniformly over that actual measurable branch.
This uses the original linear small-ball estimate and fixed-tolerance definiteness of the complete residual Schur block, without a shrinking-window proxy transfer or an upper bound on the pole magnitude.
Its [actual averaged intersection](../ledger/Yin_L_F0063_v6.md#actual-average-and-remaining-probability) incurs no factor \(N\), but does not estimate branch coverage.
Together with the opposite-sign test, the same-sign definite single-pole resonance remains only in \(c_0N\le|\lambda|<\Lambda_0N^4\); indefinite backgrounds and multiple strong poles remain unresolved.
The existing favorable-subsequence truncation estimate still controls clipped logarithms only, so no actual inverse-tail or total-negative-log-loss probability for the full free-gap model is asserted.

<a id="residual-matrix-quadratic-noise-test"></a>
## Residual matrix noise in the same-sign single-pole band

This ordinary development for Yin, dated 2026-11-06T10:24 UTC, tests the remaining same-sign range \(c_0N\le|\lambda|<\Lambda_0N^4\) in [L63v6](../ledger/Yin_L_F0063_v6.md#actual-average-and-remaining-probability).
It retains the original size-three real positive-frame model, actual single-pole decomposition \(M^{-1}=E+\lambda ee^T\), fixed normalized residual energy and the good minor-and-diagonal conditioning of [L63v5](../ledger/Yin_L_F0063_v5.md#strong-pole-complete-polynomial-test).
The calculation obtains a polynomial-scale original-law small-ball estimate for a measurably selected entry of the complete residual Schur matrix \(S_E\).
It does not obtain a determinant small-ball estimate, an estimate for the full pole-updated matrix \(S\), or the missing actual branch probabilities.
The finite-dimensional obstruction below explains why the entry estimate cannot simply be contracted with the relevant scalar cofactor.
This is ordinary authoring and self-checking, not independent review or Claim adoption.

<a id="cross-input-matrix-coercivity"></a>
### The complex-direction frame detects every symmetric matrix through cross-input terms

For the fixed real symmetric matrices \(A_1,\ldots,A_d\in M_3(\mathbb R)\), assume the existing complex-direction frame condition
\[
 \chi_A:=\inf_{\substack{u,v\in\mathbb C^3\\\|u\|=\|v\|=1}}
                  \sum_j|v^*A_ju|^2>0.
\]
For real symmetric \(H\), define
\[
 C_{jl}(H):=A_jHA_l+A_lHA_j,\qquad 1\le j<l\le d.
 \tag{Residual-cross-input-map}
\]
Then there is a fixed \(\gamma_A>0\) such that
\[
 \sum_{j<l}\|C_{jl}(H)\|_F^2\ge\gamma_A\|H\|_F^2
 \quad\text{for every }H\in M_3(\mathbb R)_{\rm sa}.
 \tag{Residual-cross-input-coercivity}
\]
Here the subscript denotes real symmetric matrices.

To prove injectivity, suppose all the cross terms vanish and let \(r=\operatorname{rank}H>0\).
For every nonzero complex \(u\), the matrix
\[
 V(u):=(A_1u,\ldots,A_du)\in M_{3,d}(\mathbb C)
\]
has full row rank by \(\chi_A>0\).
Thus \(V(u)\) is surjective and \(V(u)^T\) is injective, and
\[
 \operatorname{rank}\bigl(V(u)^THV(u)\bigr)=r.
 \tag{Residual-cross-input-rank}
\]
This statement uses the algebraic transpose, not the adjoint.
The off-diagonal entry with indices \(j,l\) is
\(u^TA_jHA_lu=\tfrac12u^TC_{jl}(H)u=0\).
Hence this rank-\(r\) matrix is diagonal with entries
\[
 q_j(u):=u^TA_jHA_ju.
\]
Let \(J\) consist of the indices for which the quadratic polynomial \(q_j\) is not identically zero.
The product of these finitely many nonzero polynomials is nonzero, so at a suitable nonzero complex \(u\) all of them are simultaneously nonzero.
The rank identity then gives \(|J|=r\).
At every other nonzero complex \(u\), the same rank identity forces all the \(r\) polynomials indexed by \(J\) to remain nonzero.
This is impossible for a nonzero homogeneous quadratic polynomial in three complex variables.
Indeed its real symmetric coefficient matrix may be orthogonally diagonalized; a form of rank at most one has a nontrivial kernel, and with two nonzero eigenvalues \(\alpha,\beta\), the vector with two coordinates \(1,t\), where \(t^2=-\alpha/\beta\), is a nonzero complex zero.
The contradiction proves injectivity.
Compactness of the real symmetric Frobenius unit sphere yields (Residual-cross-input-coercivity).

<a id="actual-residual-diagonal-blocks"></a>
### The actual minor equation supplies linearly many usable diagonal blocks

Write the physical diagonal blocks of the actual residual \(E\) as \(E_{kk}\), and retain
\[
 g_E=N^{-1}\sum_{k=1}^{n}E_{kk},\qquad
 B_E=A_0+\theta_NI_3-\sum_jA_jg_EA_j,
 \qquad
 \|B_Eg_E-I_3\|\le\tfrac12.
 \tag{Residual-actual-background-equation}
\]
These are the actual measurable objects and good event used in the preceding fixed single-pole tests.
The residual energy gives
\[
 \sum_k\|E_{kk}\|_F^2\le KN,\qquad
 \|g_E\|_F\le\sqrt{K n/N}\le\sqrt K.
\]
For all sufficiently large \(N\), the fixed coefficients and \(\theta_N\to0\) therefore give a fixed \(C_E\ge1\) such that \(\|B_E\|\le C_E\).
The background equation implies \(\|g_E\|_F\ge\|g_E\|\ge(2C_E)^{-1}=:a_0\), and consequently
\[
 \sum_k\|E_{kk}\|_F\ge Na_0.
 \tag{Residual-diagonal-first-moment}
\]
Set \(h_-=a_0/4\) and \(h_+=4K/a_0\).
Blocks of norm less than \(h_-\) contribute at most \(Na_0/4\) to this last sum.
Blocks of norm greater than \(h_+\) contribute at most
\(h_+^{-1}\sum_k\|E_{kk}\|_F^2\le Na_0/4\).
It follows that at least \(\rho N\) physical indices, for fixed \(\rho=a_0/(2h_+)>0\), satisfy
\[
 h_-\le\|E_{kk}\|_F\le h_+.
 \tag{Residual-many-diagonal-blocks}
\]
This is an actual deterministic consequence on the good conditioning, not an additional delocalization or rate assumption.

<a id="complete-residual-entry-small-ball"></a>
### An original-law entry estimate for the complete residual Schur matrix

For the original raw border coordinates \(\xi_{j,k}\), the physical block of \(R\) at \(k\) is
\(N^{-1/2}\sum_jA_j\xi_{j,k}\).
Thus the coefficient of \(\xi_{j,k}\xi_{l,k}\), with \(j<l\), in the complete matrix
\[
 S_E=A_0+\theta_NI_3+D_i-R^TER
\]
is exactly \(-N^{-1}C_{jl}(E_{kk})\).
No off-diagonal physical block \(E_{kh}\), \(h\ne k\), contributes to this same pair of original variables.
The matrix coercivity and (Residual-many-diagonal-blocks) show that, at each of those indices, some input pair \(j<l\) and some matrix entry \((a,b)\) have coefficient magnitude at least \(c_A/N\), for a fixed \(c_A>0\).
A pigeonhole choice among the nine entries gives one \(\mathcal F\)-measurable pair \((a,b)\) and at least \(\rho N/9\) disjoint physical groups with such a pair of original variables.
All selections occur before the fresh border is sampled.

Use the exact original-law two-copy representation
\[
 \xi_{j,k}=\frac{\xi'_{j,k}+\xi''_{j,k}}2+
             \varepsilon_{j,k}\frac{\xi'_{j,k}-\xi''_{j,k}}2.
\]
Fixed nonzero variances and finitely many input laws give fixed \(b_0,p_0>0\) such that each selected copy difference has modulus at least \(b_0\) with probability at least \(p_0\).
The disjoint selected pairs survive independently with probability at least \(p_0^2\); a fixed positive fraction survive outside an error \(Ce^{-cN}\).
After conditioning on all copies, the coefficient of each corresponding quadratic sign monomial in \((S_E)_{ab}\) has modulus at least \(c_Ab_0^2/(4N)\).
The original polynomial has degree at most two, so squares produce only constant or linear sign terms, and no higher-degree collision changes these quadratic coefficients.
The full real sign polynomial, with its unrestricted center and all other coefficients retained, therefore has matching rank at least a fixed multiple of \(N\) on that copy event.
The accepted [MNV16 degree-two theorem and interval normalization](../audits/literature/MNV16/Yin_U001.md#quadratic-specialization) give fixed \(c_1,c,C>0\) such that
\[
 \sup_{t\in\mathbb R}
 \mathbb P\left\{|(S_E)_{ab}-t|\le c_1N^{-1}
                   \,\middle|\,\mathcal F\right\}
 \le Ce^{-cN}+C\sqrt{\log N}\,N^{-1/9}.
 \tag{Residual-complete-entry-small-ball}
\]
Choose \(c_1\) small enough that the closed interval has length strictly less than the guaranteed coefficient scale after normalization.
The center may be \(\mathcal F\)-measurable, but is not allowed to depend on the fresh \(z\) or \(S_E\).
The source statement and its recorded source-proof inspection limit are reused at exactly that real degree-two scope.
No squared average of complete degree-six coefficients is taken, so the finite-variance integrability obstruction in L63v5 is not bypassed or contradicted.
The estimate is uniform over the actual good conditionings, and can be integrated or averaged over their original-model intersections without a factor \(N\).
It requires neither a rate for \(q_N(K)\) nor an additional moment of an original coordinate.

<a id="scalar-projection-obstruction"></a>
### Why the remaining scalar resonance does not follow from this estimate

Matrix coercivity does not imply coercivity after a prescribed scalar contraction, even with a positive frame and a positive contraction.
For an exact finite-dimensional example, take the six real Frobenius-orthonormal symmetric matrix units
\[
 E_{11},E_{22},E_{33},
 \quad (E_{12}+E_{21})/\sqrt2,\quad
 (E_{13}+E_{31})/\sqrt2,\quad
 (E_{23}+E_{32})/\sqrt2
\]
as \(A_1,\ldots,A_6\), and take \(H=I_3\).
As in the [positive-frame calculation of L63v5](../ledger/Yin_L_F0063_v5.md#paired-coefficient-l2-obstruction), this family satisfies
\[
 \sum_j|v^*A_ju|^2=\tfrac12(1+|u^Tv|^2)\ge\tfrac12
\]
for complex unit \(u,v\).
Nevertheless \(\operatorname{Tr}C_{jl}(I_3)=2\operatorname{Tr}(A_jA_l)=0\) for all \(j<l\).
With independent fair signs and \(U=\sum_jA_j\varepsilon_j\), it follows that \(\operatorname{Tr}(U^2)=6\) deterministically.
There is also a rank-one positive contraction with the same obstruction: for \(u=e_1\), the nonzero vectors among \(A_ju\) are \(e_1,e_2/\sqrt2,e_3/\sqrt2\), which are pairwise orthogonal.
Hence \(u^TC_{jl}(I_3)u=0\) for every \(j<l\), and \(u^TU^2u=2\) deterministically.
These facts concern the finite-dimensional coefficient map, not a claimed actual-minor event or a counterexample to the original Wigner determinant task.
They show why neither positive definiteness nor the matrix entry estimate alone supplies the scalar contraction needed at a determinant resonance.

For the remaining same-sign band, the actual complete polynomial is still
\[
 \frac N\lambda\det S
   =\frac N\lambda\det S_E-z^T\operatorname{adj}(S_E)z,
\]
and \(z\) uses the same original row as \(S_E\).
The polynomial has degree up to six; its cofactor contraction is row-dependent, and the complete paired coefficients can receive the repeated-variable contributions retained in L63v5.
Consequently (Residual-complete-entry-small-ball) cannot be substituted for a small-ball estimate of this polynomial or for an original-parent floor.
The new actual-minor information is the rate for a complete residual entry and the cross-input matrix mechanism that supplies it.
The next discriminating question is whether several such matrix directions force a surviving complete determinant layer with the required original-law probability and graph normalization, or whether the actual minor equation excludes the scalar degeneracies on enough of the resonant branch.
No favorable dimensional subsequence for the missing total negative-logarithmic loss, and no general free-gap completion, has been proved by this calculation.

<a id="vector-visibility-and-sixth-cancellation"></a>
## Vector visibility and the complete sixth-degree cancellation test

The complete bounded test is fixed in [L63v7](../ledger/Yin_L_F0063_v7.md#vector-visibility-and-sixth-cancellation), as ordinary development and authoring self-checking without independent review or Claim adoption.
It strengthens the residual matrix direction argument and then tests the actual cancellation between the two terms of the full single-pole polynomial.

<a id="cross-input-vector-visibility"></a>
The [vector-visibility proof](../ledger/Yin_L_F0063_v7.md#cross-input-vector-visibility) gives a uniform bound for \(\sum_{j<l}\|(A_jHA_l+A_lHA_j)u\|^2\) in every real vector direction, using the complex-direction frame at its essential rank-three step.
Its exact local determinant curvature consequence is not a discrete coefficient or original-law small-ball estimate.

<a id="three-group-exact-coefficients"></a>
<a id="same-sign-pole-full-matching-cancellation"></a>
The [three-group calculation](../ledger/Yin_L_F0063_v7.md#three-group-exact-coefficients) gives coefficients \(-8\) and \(2\), producing [exact cancellation](../ledger/Yin_L_F0063_v7.md#same-sign-pole-full-matching-cancellation) of a linear matching extracted from the residual determinant when \(E=c(I-ee^T)\) and \(\lambda=c(1+4n)\).
The entire sixth layer is not claimed to vanish.

<a id="fixed-law-realization-and-rectangle-boundary"></a>
The [same fixed-law realization](../ledger/Yin_L_F0063_v7.md#fixed-law-realization-and-rectangle-boundary) preserves fixed positive-frame coefficients, the free gap, original normalization and finite-second-moment independent coordinates, with positive probability for each specified finite minor.
Those minors satisfy the spectral decomposition and background equation and have a flat chosen eigenvector, but their off-support rectangles have rank at most one.
They therefore lie outside the required good-minor event and supply no counterexample to the target probability theorem.

<a id="complete-matching-next-interface"></a>
The [remaining inference](../ledger/Yin_L_F0063_v7.md#complete-matching-next-interface) is a complete pole-updated Schur estimate that uses the actual simultaneous minor geometry to retain an adequate layer or otherwise control the full value and graph denominator.
Residual entry anti-concentration, vector visibility, local curvature and preservation of a selected residual matching do not by themselves close that step.
Actual branch probabilities or a direct total negative-logarithmic-loss estimate remain unresolved.

<a id="actual-inverse-rectangles-and-directional-schur"></a>
## Actual inverse rectangles and a complete directional Schur estimate

The complete argument is fixed in [L63v10](../ledger/Yin_L_F0063_v10.md#actual-inverse-rectangles-and-directional-schur) as ordinary development and authoring self-checking, without independent review or Claim adoption.
It uses the actual good-minor rectangles and a minor norm guard to control every auxiliary direction selected before the fresh border is sampled.

<a id="inverse-cut-transmission"></a>
The [commutator transmission](../ledger/Yin_L_F0063_v10.md#inverse-cut-transmission) gives \(s_{3\lfloor\delta n\rfloor}(M^{-1}[J,I])\ge cN^{-3/2}\) on each actual small-support cut and loses only one singular direction after removing a single pole.
It needs neither a bound on that pole nor a residual inverse-energy bound.

<a id="inverse-cut-original-quadratic-matching"></a>
The [frame and matching argument](../ledger/Yin_L_F0063_v10.md#inverse-cut-original-quadratic-matching) retains linearly many disjoint original quadratic coefficients of size \(cN^{-7/2}\) in the complete \(u^TSu\).
This includes the full pole contribution, with no residual proxy error.

<a id="inverse-cut-original-directional-small-ball"></a>
The [original-law bound](../ledger/Yin_L_F0063_v10.md#inverse-cut-original-directional-small-ball) gives conditional small-ball probability at most \(Ce^{-cN}+C\sqrt{\log N}\,N^{-1/9}\) at that scale, uniformly over preselected minor-measurable real unit directions and centers.
Its original-model physical average has no factor \(N\).
The unresolved step is making the approximate kernel direction independent of an unused fresh subblock while retaining adequate rank, or obtaining a surviving matching for the complete determinant from several cuts jointly.
The fixed-direction estimate alone does not control the full determinant, the graph-normalized distance or the total negative-logarithmic loss.

<a id="regularized-core-original-diffuse-mass"></a>
## Original-model diffusion and the remaining pole coverage

The complete original-model diffusion deduction is fixed in [C194v24](../claims/Yin_C_F0194_v24.md#statement), with its actual assessment at that responsible material.
It preserves the common principal core, different diagonal laws, all fixed deletions and shifts, and the intrinsic minor-measurable event needed for the [single-pole theorem C194v23](../claims/Yin_C_F0194_v23.md#diffuse-single-pole-statement).
The exact [JSS20 input](../audits/literature/JSS20/Yin_U001.md#jss20-u001) retains the inspected edition and source-proof limits.
The [subsequent low-rank residual theorem](../claims/Yin_C_F0194_v25.md#statement) supplies the stable background on a bounded-energy residual branch; the remaining original free-gap question is actual residual-energy coverage or a complete treatment of the other pole configurations or total negative-logarithmic loss.
The diffusion deduction supplies no such coverage probability and no completion of the general F13 contract.

<a id="low-rank-residual-stable-background"></a>
## Stable residuals and the remaining inverse-mode coverage

The complete statements and arguments are fixed in [C194v25](../claims/Yin_C_F0194_v25.md#statement), with their actual status at its [current assessment](../claims/Yin_C_F0194_v25.md#current-assessment).
Its [stable-background statement](../claims/Yin_C_F0194_v25.md#stable-background-statement) retains the original-law, marginal fixed-deletion and noncommuting rank-o(N) approximation scope.
Its [free-gap clipping](../claims/Yin_C_F0194_v25.md#free-gap-clipping) supplies a bounded residual and a rank-o(N) removed head, without bounding that head's magnitude or complete Schur contribution.

<a id="single-exceptional-mode-all-scales"></a>
The [all-scale one-mode argument](../claims/Yin_C_F0194_v25.md#single-exceptional-mode-all-scales) retains the complete original-row expression and graph denominator, with its positive-frame, auxiliary-dimension-three and bounded-residual hypotheses.
The [natural-scale physical spread](../claims/Yin_C_F0194_v25.md#natural-scale-spread) and [conditional parent deduction](../claims/Yin_C_F0194_v25.md#single-mode-average-tightness-parent) contain the strengthened distance average and its exact shift and logarithmic interfaces.

<a id="single-mode-average-tightness-parent"></a>
The actual unresolved probability input is the displayed physical-index average tightness of the normalized inverse energy after removing one largest inverse eigenmode, with singular minors counted as failures.
That tightness has not been supplied by the original free-gap model; rank o(N) of the clipped head does not imply it.
The next research step is to establish that average tightness along suitable deterministic dimensions, or to obtain complete multiple-pole or total negative-logarithmic-loss control that bypasses it.
No unconditional free-gap determinant theorem or general F13/F14 completion is inferred from the fixed conditional theorem.

<a id="low-mode-flat-reservoir-probe"></a>
## A common flat reservoir for an entire exceptional spectral space

This deduction was developed for Yin on 2026-11-06T13:11 through ordinary research and authoring self-checks, without independent review or Claim adoption.
The [adopted natural-scale spread](../claims/Yin_C_F0194_v25.md#natural-scale-spread) is strong enough to retain a common reservoir for every vector in a small near-kernel subspace.
The proof uses that accepted result and the [intrinsic minor event](../claims/Yin_C_F0194_v24.md#argument), rather than applying a new source theorem to an adaptively compressed matrix.
The complete inverse coefficient and original-law probability deductions remain separate from the geometric result below.

### Original model and simultaneous reservoir statement

Use independent original real finite-second-moment Wigner inputs, fixed real symmetric coefficients \(A_0,\ldots,A_d\in M_m(\mathbb R)\), and the positive complex-direction frame \(\chi_A>0\).
The off-diagonal laws are fixed, centered, real and variance one; the diagonal laws are fixed, centered and real with finite second moment.
Upper-triangular coordinates and input colors are independent within each size, while coupling across sizes is arbitrary.
The auxiliary dimension \(m\) and input count \(d\) are fixed, and all entries retain the original \(N^{-1/2}\) normalization.
Fix a physical deletion bound \(r\) and a deterministic sequence of nonnegative integers \(\ell_N=o(N)\).
Write
\[
 L_N=A_0\otimes I_N+\sum_j A_j\otimes W_j^{(N)},\qquad
 M_{\mathcal D,\theta}=(L_N+\theta I)[\mathcal D^c,\mathcal D^c],
 \qquad |\mathcal D|\le r.
\]
Let \(a_0,p,c_-,c_+>0\) be the constants in C194v25's natural-scale spread statement at this deletion bound.
Put
\[
 \nu_N=\sqrt{\frac{\max\{1,\ell_N\}}N},\qquad
 \kappa=\frac{p c_-^2}{2}>0.
 \tag{Reservoir-parameters}
\]
There is an original-model event with probability tending to one on which the following assertions hold simultaneously for every displayed deletion, every real \(|\theta|\le1\), and every real linear subspace \(V\) of the retained space satisfying
\[
 q:=\dim V\le\ell_N,\qquad
 \|M_{\mathcal D,\theta}w\|\le a_0\|w\|
       \quad(w\in V).
 \tag{Reservoir-subspace-hypotheses}
\]
Let \(P=P_V\) be its orthogonal projection, and let \(\Pi_k\) be the rank-\(m\) physical coordinate projection at retained index \(k\).
Define the physical leverage and the one common retained set by
\[
 \ell_k(P)=\operatorname{Tr}(\Pi_kP\Pi_k)
           =\|\Pi_kP\|_F^2,\qquad
 T=T(V):=\{k\in\mathcal D^c:\ell_k(P)\le\nu_N\},\qquad
 Q_T=\sum_{k\in T}\Pi_k.
 \tag{Reservoir-selection}
\]
Then
\[
 |\mathcal D^c\setminus T|\le\frac{\ell_N}{\nu_N}=o(N),\qquad
 \kappa\|w\|^2\le\|Q_Tw\|^2\le\|w\|^2\quad(w\in V),
 \tag{Reservoir-common-mass}
\]
and
\[
 \|\Pi_kw\|^2\le\nu_N\|w\|^2
       \quad(k\in T,\ w\in V).
 \tag{Reservoir-original-leverage}
\]
Thus the same physical set retains a fixed mass for every vector in the entire subspace, while its largest retained block leverage tends to zero.
The inequalities also hold for the complexification of the real subspace, by their real positive-semidefinite Gram formulation below.
For \(V=\{0\}\), take \(T=\mathcal D^c\); all the assertions are vacuous or immediate.

To prove the assertion, trace additivity gives \(\sum_{k\in\mathcal D^c}\ell_k(P)=q\).
Hence the number of excluded positions is at most \(q/\nu_N\le\ell_N/\nu_N\), which is at most \(pN/2\) for all sufficiently large \(N\).
Every real unit \(w\in V\) is an admissible near-kernel vector for C194v25, so at least \(pN\) positions have \(\|w_k\|\ge c_-/\sqrt N\).
At least \(pN/2\) of those positions remain in \(T\), giving
\[
 \|Q_Tw\|^2\ge\frac{pN}{2}\frac{c_-^2}{N}=\kappa.
\]
The set \(T\) was selected from \(P_V\), independently of the particular vector \(w\); the accepted spread event already holds for all these vectors.
Finally \(\|\Pi_kP\|^2\le\|\Pi_kP\|_F^2\le\nu_N\) on \(T\), which proves the leverage bound.
This argument removes only the high-leverage positions; it does not need to choose a new cut separately for each vector.

### Intrinsic minor measurability and a whole free-gap spectral space

For each retained minor, use the intrinsic event from C194v24 that its own original constant cuts hold and that its unshifted pencil has the required regularized principal core.
The proof of C194v25's natural-scale spread applies pointwise on that intrinsic event, with the same constants and original normalization, for all \(|\theta|\le1\).
The common original parent event implies all these intrinsic events, so their simultaneous failure still has probability tending to zero.
For a minor-measurable subspace \(V\), its projection, leverages, and set \(T\) are minor-measurable.
No common parent good event is inserted into the fresh-border conditioning.

In particular, suppose that zero lies outside the spectrum of the free selfadjoint pencil \(L\).
Choose a fixed \(0<\delta\le\min\{a_0,1\}\) with \([-3\delta,3\delta]\) disjoint from that spectrum.
For every \(|\theta|\le\delta\), take the entire spectral space
\[
 V_{\mathcal D,\theta}
 =\operatorname{ran}\mathbf1_{[-\delta,\delta]}(M_{\mathcal D,\theta}).
 \tag{Reservoir-entire-gap-space}
\]
It satisfies the near-kernel norm bound whether or not the minor is invertible.
Interlacing at the two interval endpoints and the scalar shift give
\[
 \dim V_{\mathcal D,\theta}
 \le\#\{\text{eigenvalues of }L_N\text{ in }[-2\delta,2\delta]\}+2mr
 \tag{Reservoir-uniform-gap-rank}
\]
simultaneously for all the displayed deletions and shifts.
The [accepted weak spectral law](../claims/Yin_C_F0186_v4.md#statement) makes the right side divided by \(N\) tend to zero in probability, because the fixed closed interval has no limiting mass.
Consequently one can choose a deterministic \(\ell_N=o(N)\) so that the probability that the right side exceeds \(\ell_N\) tends to zero.
For an explicit choice, select increasing \(N_j\) for which the normalized parent count exceeds \(1/(2j)\) with probability at most \(1/j\) for every \(N\ge N_j\), require \(N_j\ge4mrj\), and put \(\ell_N=\lceil N/j\rceil\) for \(N_j\le N<N_{j+1}\).
This deterministic choice depends on the marginal laws and fixed coefficients, not on the coupling across dimensions or on a realized border.
Intersect its rank event with the original core/cut event to obtain all the reservoir conclusions simultaneously for the entire low spectral space, every fixed deletion, and every \(|\theta|\le\delta\).
In a fresh-border application the actual intrinsic rank and core/cut events are used; the parent event is only evidence for their probability bounds.
The probability error is not asserted summable, and no finite-matrix spectral exclusion or inverse-energy bound follows from this construction.

### The compressed subspace and signed head retain their size

Take an orthonormal basis matrix \(U\) for \(V\), so \(P=UU^T\), and put
\[
 G=U^TQ_TU,\qquad \kappa I_q\preceq G\preceq I_q,\qquad
 \widetilde U=Q_TUG^{-1/2}.
\]
The matrix \(\widetilde U\) is an isometry onto \(W=Q_TV\), and \(\dim W=q\).
The orthogonal projection onto this compressed subspace is
\[
 P_W=Q_TUG^{-1}U^TQ_T.
 \tag{Reservoir-compressed-projection}
\]
For every retained physical position \(k\in T\), its diagonal block obeys the positive-semidefinite bound
\[
 \Pi_kP_W\Pi_k\preceq\kappa^{-1}\Pi_kP\Pi_k,
 \qquad
 \operatorname{Tr}(\Pi_kP_W\Pi_k)\le\nu_N/\kappa.
 \tag{Reservoir-compressed-leverage}
\]
The blocks outside \(T\) are zero.
The formula and bounds do not depend on the choice of orthonormal basis for \(V\), so their content is minor-measurable even when that basis is not specified.

Let \(H=H^T\) be any real symmetric matrix supported on \(V\), meaning \(H=PHP\), with arbitrary eigenvalue signs and magnitudes.
Write \(H=UCU^T\), where \(C=C^T\), and let \(H_T=Q_THQ_T\).
The exact isometric representation is
\[
 H_T=\widetilde U\,(G^{1/2}CG^{1/2})\,\widetilde U^T.
\]
The singular-value product inequalities therefore give, with zeros padded if necessary,
\[
 \kappa s_j(H)\le s_j(H_T)\le s_j(H)
       \quad(1\le j\le q).
 \tag{Reservoir-head-singular-comparison}
\]
For completeness, the upper bound follows by applying \(s_j(ABC)\le\|A\|\|C\|s_j(B)\) to the two factors \(G^{1/2}\).
The lower bound follows by expressing \(C=G^{-1/2}(G^{1/2}CG^{1/2})G^{-1/2}\) and using \(\|G^{-1/2}\|^2\le\kappa^{-1}\).
These inequalities follow directly from the singular-value minimax characterization and use no positivity of \(C\).
In particular rank is preserved and
\[
 \kappa^2\sum_{j>k}s_j(H)^2
 \le\sum_{j>k}s_j(H_T)^2
 \le\sum_{j>k}s_j(H)^2
       \quad(0\le k\le q).
 \tag{Reservoir-head-tail-comparison}
\]
The case \(k=0\) compares the full squared Frobenius norms; every other case compares the residual energy after removing the largest \(k\) singular modes at its own scale.
This preserves any separately established energy divergence, but establishes no such divergence by itself.

### Uniform row and physical diagonal loads on every compressed residual

Put \(\omega_N=\nu_N/\kappa\).
For every real symmetric \(D=P_WDP_W\), including \(H_T\) and each of its spectral residuals, one has
\[
 \max_k\|\Pi_kD\|_F^2\le\omega_N\|D\|_F^2,\qquad
 \sum_k\|\Pi_kD\Pi_k\|_F^2\le\omega_N\|D\|_F^2.
 \tag{Reservoir-compressed-row-diagonal-spread}
\]
Indeed, \(D=P_WD\) gives
\(\|\Pi_kD\|_F\le\|\Pi_kP_W\|\|D\|_F\le\sqrt{\omega_N}\|D\|_F\).
Also \(D=DP_W\) gives
\[
 \|\Pi_kD\Pi_k\|_F^2
 =\|\Pi_kDP_W\Pi_k\|_F^2
 \le\omega_N\|\Pi_kD\|_F^2.
\]
Summing and using \(\sum_k\|\Pi_kD\|_F^2=\|D\|_F^2\) proves the diagonal estimate.
Every unit vector in \(W\), and hence every normalized head or residual eigenvector of \(H_T\), has maximum physical block squared norm at most \(\omega_N\).
Thus the row, physical diagonal, and individual-head bounds hold simultaneously for all spectral residuals, including repeated eigenspaces and all sign patterns.
Normalized ratios are asserted only when the relevant Frobenius norm is nonzero; the unnormalized inequalities also include the zero matrix.

For the uncompressed head itself, the corresponding restricted statements are
\[
 \max_{k\in T}\|\Pi_kH\|_F^2\le\nu_N\|H\|_F^2,\qquad
 \sum_{k\in T}\|\Pi_kH\Pi_k\|_F^2\le\nu_N\|H\|_F^2.
\]
The compressed bounds are stronger for the intended use because their denominator is the actual compressed or residual energy, rather than the original full-head energy.

### Exact coefficient interface and the first additional step

For auxiliary dimension three, the [whole-space maps and local factor bounds of C187v27](../claims/Yin_C_F0187_v27.md#whole-space-local-maps) can be formed on the retained physical set \(T\), with the same fixed auxiliary coefficients and the original scaling by \(N\).
The positive-frame bound holds on every physical subspace because \(Q_T\) removes whole physical blocks and commutes with the auxiliary coefficient maps.
The row and diagonal quantities in (Reservoir-compressed-row-diagonal-spread) are exactly the geometric quantities in its [mixed physical collision estimates](../claims/Yin_C_F0187_v27.md#mixed-physical-collisions), now verified for the signed compressed head and all its own residuals.
They are not yet assertions about the spectral residuals of the complete compressed inverse \(Q_TZQ_T\).

Conditional on the original minor, the set \(T\) is fixed and the original border coordinates at positions in \(T\) remain independent with their original laws, also after exposing all border coordinates outside \(T\).
Writing the complete Schur determinant as a polynomial in these remaining variables, its homogeneous degree-six part depends on \(Q_TZQ_T\), rather than on \(H_T\) alone.
The bounded clipped residual, cross terms with the exposed complement, and the full graph denominator must therefore remain in a subsequent calculation.
The [C194v19 probability interface](../claims/Yin_C_F0194_v19.md#statement) still requires complete sixth-degree energy and small physical-group loads at a scale dominating the full graph area on the entire two-copy sign support.
The present reservoir alone supplies none of those complete inverse or graph-area conclusions.

The [adopted C194v26 argument](../claims/Yin_C_F0194_v26.md#argument) now supplies that transfer to the complete compression in the size-three high-residual branch, compares its retained-variable coefficient scale with the full uncompressed graph denominator, and performs the original-law matching conversion and physical-index average.
The present section retains the broader fixed-auxiliary-dimension reservoir and uniform-shift geometry, whose scope is not replaced by that size-three statement.
Small residual-energy cases require a different argument: a head of rank at most two already has \(\det(R_T^TH_TR_T)=0\), irrespective of its Frobenius norm or flatness, so a sixth-layer theorem cannot follow from large full-head energy alone.
The adopted two-mode argument below supplies the separate estimate for that remaining size-three branch.
Neither the reservoir alone nor C194v26 implies full-head energy divergence or a general Task completion.

<a id="bounded-two-mode-schur-probe"></a>
## Bounded two-mode theorem and the free-gap assembly

The complete argument is now fixed in [C194v27](../claims/Yin_C_F0194_v27.md#statement) and [adopted](../claims/Yin_C_F0194_v27.md#decision-two-mode-free-gap-reviewed) after [independent whole-proof review](../audits/reviews/Yin_R_F0200_v30.md#two-mode-free-gap-whole-proof).
Its [bounded-two-mode theorem](../claims/Yin_C_F0194_v27.md#bounded-two-mode-statement) gives a joint marginal graph-determinant bound at N^(-6) for every fixed residual-energy cutoff after two inverse modes, without a spectral-position assumption.
The proof retains the original diagonal and border conditioning, a common rank-two reservoir, the exact [adopted signed nonvanishing interface](../claims/Yin_C_F0194_v27.md#two-mode-signed-nonvanishing), singular-covariance Gaussian smoothing and all pole scales with the complete graph denominator.
Its [free-gap assembly](../claims/Yin_C_F0194_v27.md#free-gap-assembly) combines this bound with adopted C194v26 to obtain the N^(-15/2) unshifted probability floor and the probability logarithmic and every-coupling limsup conclusions.
The [two-position union](../claims/Yin_C_F0194_v27.md#spectral-position-union) joins the adopted spectral-point branch at the common weaker exponent 17/2 for the real symmetric size-three positive-frame class.
No additional original-model residual-tightness premise remains in this adopted assembly.
General complex coefficients, arbitrary auxiliary dimension, the unrestricted scalar-polynomial task, full-sequence almost-sure logarithms and Brown-measure conclusions remain outside this result.
