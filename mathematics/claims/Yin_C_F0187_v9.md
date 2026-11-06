---
author: Yin
---

# Intermediate singular values for a bounded two-channel pencil with zero one-step frame

This version develops the intermediate singular-value obligation in the bounded two-channel branch of [F0013](../tasks/Yin_T_F0013_v1.md#contract).
It preserves the different positive-frame theorem at C187v3 and uses an actual-kernel balance estimate for the present zero-frame coefficients.
The argument makes no novelty claim and has [independent whole-proof coverage](../audits/reviews/Yin_R_F0191_v9.md#balanced-middle-and-conditional-log) selected below.


<a id="statement"></a>
## Exact model and conclusions

For \(j=1,2\), let \(W_j^{(N)}\) be independent real symmetric Wigner matrices with independent upper off-diagonal entries distributed as \(\xi_j/\sqrt N\).
Each fixed real law satisfies \(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and \(|\xi_j|\le L\).
The diagonal entries of input \(j\) are independent copies of \(\zeta_j/\sqrt N\), with \(\zeta_j\) fixed, real, centered and bounded by \(L\).
All upper-triangular coordinates and the two inputs are independent within each size, while cross-size coupling is arbitrary.
Zero diagonal laws are allowed.
Put \(\alpha:=\sqrt2\), \(X:=W_1^{(N)}+W_2^{(N)}\), \(Y:=W_1^{(N)}+\alpha W_2^{(N)}\), and
\[
 L_N:=\begin{pmatrix}X&I_N\\I_N&Y\end{pmatrix}.
\]
The first off-diagonal law need not be Rademacher in this section.
There are constants \(c>0\) and, for each fixed \(D>0\), constants \(A_D,C_D>0\) such that eventually
\[
 \mathbb P\left\{\exists\,4\lceil A_D\log N\rceil\le j\le2N-1:
 s_{2N-j}(L_N)<c\,j/N\right\}\le C_DN^{-D}.
 \tag{Balanced-middle}
\]
Singular values are listed in decreasing order.
The accepted inputs are the bounded norm event in [C187v4](Yin_C_F0187_v4.md#spectral-residual-spread), the bounded-product convex concentration inequality (9) in [C187v2](Yin_C_F0187_v2.md#argument), and the exact projected-row and block Gram identities in [C187v3](Yin_C_F0187_v3.md#physical-block-distance).
The proof of the external bounded-product inequality retains its recorded source-inspection boundary.
The positive-frame hypothesis of C187v3 is not invoked.


Let \(s_1,s_2\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal tracial state \(\tau\), and define
\[
 \ell:=\begin{pmatrix}s_1+s_2&1\\1&s_1+\sqrt2s_2\end{pmatrix},
 \qquad \tau_2:=\operatorname{tr}_2\otimes\tau.
\]
The limiting singular law satisfies \(\nu_{|\ell|}([0,t])\le Ct\) for sufficiently small \(t>0\), and \(\log\Delta_{\tau_2}(\ell)\) is finite.
With \(D>1\), the intermediate negative-logarithmic bound (Balanced-middle-log) below holds almost surely under every allowed coupling.
If, in addition, there are fixed \(c_*,A>0\) such that
\[
 \mathbb P\{s_{\min}(L_N)<c_*N^{-A}\}\longrightarrow0,
 \tag{Additional-polynomial-floor}
\]
then \((2N)^{-1}\log|\det L_N|\to\log\Delta_{\tau_2}(\ell)\) in probability.
Under that additional hypothesis its limsup equals the same free logarithm almost surely for every coupling.
The exact finite/free determinant identities give the corresponding conclusions for \(Q_N:=(W_1+\sqrt2W_2)(W_1+W_2)-I_N\), with normalized logarithm \(N^{-1}\log|\det Q_N|\) and target \(\log\Delta_\tau((s_1+\sqrt2s_2)(s_1+s_2)-1)=2\log\Delta_{\tau_2}(\ell)\).
No polynomial floor is proved in this version.
The one-step coefficient frame is zero; the theorem derives its estimate from the actual retained kernel geometry, not from a positive-frame assumption.

<a id="argument"></a>
## Complete proof and conditional logarithmic deduction

<a id="strong-tall-two-channel-rectangles"></a>
### Constant lower bounds for sufficiently thin cross rectangles

Choose a fixed \(\Lambda\ge1\) for which
\[
 \mathbb P\{\max(\|X\|,\|Y\|)>\Lambda\}\le Ce^{-cN}.
 \tag{Balanced-norm}
\]
Such a choice follows from the fixed bounded-input norm proof in C187v4.
For \(1\le k\le\delta N\), put \(T_k:=\{N-k+1,\ldots,N\}\), and, for \(i\notin T_k\), put \(V_i:=[N]\setminus\{i\}\) and \(U_{i,k}:=V_i\setminus T_k\).
The fixed \(\delta\in(0,1/4)\) will be sufficiently small.
Each of \(X[U_{i,k},T_k]\) and \(Y[U_{i,k},T_k]\) has independent centered entries with the original \(N^{-1/2}\) normalization.
The unscaled entry variances are respectively \(2\) and \(3\), and their fourth moments have a common finite bound depending only on the fixed bounded laws.

Here is an elementary lower-tail and net proof with the required constants.
For either rectangle \(B\), a fixed real unit vector \(z\in\mathbb R^k\), and a row \(R_\ell:=(Bz)_\ell\), write \(v\in\{2,3\}\) for its unscaled entry variance.
Here \(\eta\) denotes an unscaled entry, with law \(\xi_1+\xi_2\) for \(X\) and \(\xi_1+\alpha\xi_2\) for \(Y\).
Independence and centering give
\[
 \mathbb E R_\ell^2=v/N,\qquad
 \mathbb E R_\ell^4
 =N^{-2}\left(\mathbb E\eta^4\sum_jz_j^4+
                  6v^2\sum_{j<r}z_j^2z_r^2\right)
 \le C_4N^{-2}.
\]
Splitting the second moment at \(v/(2N)\) and using Cauchy--Schwarz yields
\[
 \mathbb P\{R_\ell^2\ge v/(2N)\}\ge p_0:=v^2/(4C_4)>0.
\]
The indicators of these row events are independent.
For their sum \(S\), with \(m:=|U_{i,k}|\ge N/2\) eventually, exponential Markov at parameter \(1\) gives
\[
 \mathbb P\{S\le p_0m/2\}
 \le \exp\{-p_0(1-e^{-1}-1/2)m\}.
\]
Consequently \(\|Bz\|\ge a_0:=(p_0v/8)^{1/2}\) outside \(e^{-c_1m}\), for fixed constants that can be chosen commonly for the two laws.

Take a deterministic \(\theta\)-net of the real unit sphere, with \(\theta:=\min(1/2,a_0/(2\Lambda))\), of size at most \((3/\theta)^k\).
On the norm event (Balanced-norm), \(\|B\|\le\Lambda\), so lower bounds \(a_0\) at its net points imply \(s_{\min}(B)\ge a_0/2\).
Choose \(\delta\) so that \(\delta\log(3/\theta)<c_1/4\).
The union bound over the net, both rectangles, and all at most \(N^2\) pairs \((i,k)\), then gives
\[
 s_{\min}(X[U_{i,k},T_k])\ge a,\qquad
 s_{\min}(Y[U_{i,k},T_k])\ge a
 \tag{Balanced-rectangles}
\]
simultaneously for a fixed \(a>0\), outside \(Ce^{-cN}\).
No row distribution was conditioned on the full-matrix norm event in this calculation.
When exposing a fresh row below, use the minor-measurable version of these norm and rectangle conditions; the full norm event only bounds the probability of their failure.

<a id="actual-kernel-channel-balance"></a>
### Both channels carry a fixed fraction of every projected kernel vector

Fix \(i,k\) as above.
In the \(2(N-1)\) coordinates of \(V_i\), let \(H_i\) be the span of the rows of
\[
 M_i:=\begin{pmatrix}X[V_i,V_i]&I_{N-1}\\I_{N-1}&Y[V_i,V_i]\end{pmatrix}
\]
with physical indices in \(U_{i,k}\), and let \(P\) be the orthogonal projection onto \(H_i^\perp\).
Then \(\operatorname{rank}P\ge2k\).
Every \(z=(u,v)\in H_i^\perp\) obeys
\[
 u_U+Y[U,V]v=0,\qquad v_U+X[U,V]u=0,
\]
where \(U:=U_{i,k}\) and \(V:=V_i\).
On the minor norm and rectangle conditions,
\[
 \|u_U\|\le\Lambda\|v\|,\qquad
 a\|u_{T_k}\|
 \le\|v_U\|+\|X[U,U]u_U\|
 \le(1+\Lambda^2)\|v\|.
\]
Hence \(\|u\|\le B_0\|v\|\), where \(B_0:=\Lambda+(1+\Lambda^2)/a\).
Interchanging the two equations and using the \(Y\) rectangle also gives \(\|v\|\le B_0\|u\|\).
With \(b:=(1+B_0^2)^{-1}\), each channel therefore has at least fraction \(b\) of the squared norm of every vector in \(H_i^\perp\).
For the two channel projections \(\Pi_1,\Pi_2\), this says
\[
 P\Pi_\ell P\ge bP,\qquad
 \operatorname{Tr}(P\Pi_\ell)\ge b\,\operatorname{rank}P
 \quad(\ell=1,2).
 \tag{Kernel-channel-balance}
\]
No invertibility or row-rank assertion about \(M_i\) was assumed.

<a id="balanced-fresh-row-distance"></a>
### Conditional fresh-row concentration with a degenerate one-step frame

Keep the first \(N-k\) physical row blocks of \(\sqrt N L_N\), and call the resulting matrix \(\mathsf B\).
For its retained physical index \(i\), delete the two columns of index \(i\) from the current block and all the other row blocks.
The projected other-row space is exactly \(H_i\) above.
Condition on both input principal minors on \(V_i\); this fixes \(H_i\), \(P\), and the minor norm and rectangle conditions while leaving the \(2(N-1)\) original off-diagonal row entries independent.
The projected raw current block \(F_i\) has, at physical index \(\ell\in V_i\), the diagonal auxiliary block
\[
 \operatorname{diag}(\xi_{1,\ell}+\xi_{2,\ell},
                     \xi_{1,\ell}+\alpha\xi_{2,\ell}).
\]
The constant off-diagonal auxiliary identity and the current diagonal variables vanish upon deletion of the physical column.

For a real unit auxiliary vector \(a=(a_1,a_2)\), put \(Y_a:=\|PF_i^{\mathsf T}a\|\).
The common covariance block of \(F_i^{\mathsf T}a\) is
\[
 T_a:=
 \begin{pmatrix}
 2a_1^2&(1+\alpha)a_1a_2\\
 (1+\alpha)a_1a_2&3a_2^2
 \end{pmatrix}
 =\operatorname{diag}(a_1,a_2)
 \begin{pmatrix}2&1+\alpha\\1+\alpha&3\end{pmatrix}
 \operatorname{diag}(a_1,a_2).
\]
The middle matrix is positive definite, with determinant \((\alpha-1)^2\).
If \(\kappa>0\) denotes its least eigenvalue, then \(T_a\ge\kappa\operatorname{diag}(a_1^2,a_2^2)\), including when one component of \(a\) is zero.
By (Kernel-channel-balance),
\[
 \mathbb E[Y_a^2\mid M_i]
 =\operatorname{Tr}\!\left(P(T_a\otimes I_{N-1})\right)
 \ge\kappa b\,\operatorname{rank}P\ge2\kappa bk.
 \tag{Balanced-covariance}
\]
Here tensor order is auxiliary first, and the conditional law also includes the separate two input minors determining \(M_i\).

As a function of the original independent real row coordinates, \(Y_a\) is convex and \(\sqrt3\)-Lipschitz.
Each coordinate has support diameter at most \(2L\).
The accepted bounded-product inequality yields
\[
 \mathbb P\{|Y_a-\operatorname{med}Y_a|>t\mid\text{two minors}\}
 \le Ce^{-ct^2}.
\]
Its integrated \(L^2\) error from the median is bounded by a fixed constant.
The \(L^2\) triangle inequality and (Balanced-covariance) imply, for \(k\) above a fixed constant,
\[
 \operatorname{med}Y_a\ge c_0\sqrt k,\qquad
 \mathbb P\{Y_a<c_0\sqrt k/2\mid\text{two minors}\}\le Ce^{-ck}.
\]
The constants are uniform over auxiliary directions and over every minor satisfying the indicated conditions.

Take a deterministic \(N^{-1}\)-net of the real unit circle with at most \((3N)^2\) points.
The bounded fresh coordinates give \(\|F_i\|\le C_L\sqrt N\), so its net error is at most \(C_LN^{-1/2}\).
It follows that \(\inf_{\|a\|=1}\|PF_i^{\mathsf T}a\|\ge c_2\sqrt k\) outside conditional probability \(CN^2e^{-ck}\).
Coordinate contraction from the full row space to the deleted-column space, exactly as in C187v3, implies that the actual full row-distance Gram \(G_i\) satisfies \(G_i\ge c_2^2kI_2\).
Union over all \(i,k\), use (Balanced-rectangles), and put \(k_{\min}:=\lceil A_D\log N\rceil\).
For sufficiently large \(A_D\), all these Gram bounds hold simultaneously for \(k_{\min}\le k\le\lfloor\delta N\rfloor\), outside
\[
 CN^4e^{-ck_{\min}}+Ce^{-cN}\le C_DN^{-D}.
 \tag{Balanced-Grams}
\]

<a id="balanced-middle-index-count"></a>
### Exact block identity and the logarithmic range

The Gram bounds imply full row rank of each \(\mathsf B\): a nonzero row relation would give a nonzero combination from one physical row block in the span of the others.
The block Schur formula therefore gives
\[
 \sum_{r=1}^{2(N-k)}s_r(\mathsf B)^{-2}
 =\sum_{i=1}^{N-k}\operatorname{Tr}G_i^{-1}
 \le CN/k.
\]
For \(j\ge4k_{\min}\), choose \(k:=\min(\lfloor j/4\rfloor,\lfloor\delta N\rfloor)\).
Eventually \(k\ge k_{\min}\), \(k\le j/4\), and \(k\ge\delta j/4\) for \(j\le2N-1\).
At least \(j-2k+1\ge j/2\) singular values in this row-deleted list are no larger than \(s_{2N-j}(\mathsf B)\).
Thus
\[
 (j-2k+1)s_{2N-j}(\mathsf B)^{-2}\le CN/k.
\]
Row-deletion interlacing and the raw normalization give
\[
 s_{2N-j}(L_N)\ge N^{-1/2}s_{2N-j}(\mathsf B)
 \ge c\sqrt{jk}/N\ge c'j/N,
\]
proving (Balanced-middle).

With \(D>1\), this estimate is eventually almost sure under every cross-size coupling by summability.
Writing the singular values in increasing order as \(a_1\le\cdots\le a_{2N}\) and \(r_N:=4\lceil A_D\log N\rceil+2\), the same elementary integral comparison as in [C187v3](Yin_C_F0187_v3.md#block-mesoscopic-log) gives
\[
 \limsup_N\frac1{2N}
 \sum_{\substack{r\ge r_N\\a_r<t}}(-\log a_r)
 \le Ct(1+|\log t|)
 \quad\text{almost surely},\qquad 0<t<1.
 \tag{Balanced-middle-log}
\]
The accepted Hermitized weak law in [C186v4](Yin_C_F0186_v4.md#row-concentration) then gives \(\nu_{|\ell|}([0,t])\le Ct\), hence a finite free logarithm.
The fixed norm event controls positive logarithms in this bounded model.
For completeness, weak convergence at continuity points, together with the count bound \(r_N/(2N)+Ct\), gives the limiting mass bound first at those points and then everywhere by decreasing continuity points.
Its integral against \(dt/t\) near zero is finite.
For each fixed truncation parameter \(t>0\), the function \(x\mapsto\log\max(x,t)\) is continuous on the eventual common compact singular-value interval.
Weak convergence thus gives convergence of these truncated logarithms.
Since the original logarithm is no larger, sending \(t\downarrow0\) gives the almost-sure upper bound by the finite free logarithm under every coupling.

If one additionally proves \(\mathbb P\{s_{\min}(L_N)<cN^{-A}\}\to0\) for fixed \(c,A>0\), the omitted bottom contribution is at most
\[
 \frac{r_N}{2N}(A\log N+|\log c|)
 =O((\log N)^2/N)
\]
on that event's complement.
Weak convergence, (Balanced-middle-log), and this estimate then give
\[
 \frac1{2N}\log|\det L_N|
 \longrightarrow\log\Delta_{\tau_2}(\ell)
 \quad\text{in probability}.
 \tag{Balanced-log-conditional}
\]
The required polynomial floor is separate; the displayed logarithmic limit has precisely the additional hypothesis (Additional-polynomial-floor).
The marginal coupling criterion in [C190v1](Yin_C_F0190_v1.md#coupling-criterion), together with the accepted upper bound, would give the F0013 limsup equality for this fixed bounded two-channel submodel.
The finite and free identities in [L66v5](../ledger/Yin_L_F0066_v5.md#model-and-determinants) transfer the corresponding statement to \(Q_N:=(W_1+\alpha W_2)(W_1+W_2)-I_N\), with the factor \(2\) in logarithmic normalization.
This conditional bounded-model conclusion leaves arbitrary coefficient tuples, original finite-second-moment laws and the F0012 full-sequence planar contract unresolved.

## Current assessment
[Selected decision](#decision-balanced-middle-reviewed)

## Assessment history

### Decision balanced-middle-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:57 |
| status | open |
| reason | Complete candidate bounded-law intermediate estimate down to a logarithmic number of bottom singular values, actual two-channel kernel balance, free logarithmic integrability and the conditional deduction from an additional polynomial floor. Applicable proof review remains pending; no least-value floor or original general Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Bounded two-channel middle and conditional log theorem](#statement) | Fixed real bounded centered laws, variance-one off-diagonals, original normalization, arbitrary cross-size coupling; summable middle bound, finite free target and logarithmic convergence conditional on an additional polynomial floor. |
| argument | [Complete balance and concentration proof](#argument) | Thin rectangle estimate, actual kernel balance, independent fresh-row covariance and concentration, block Gram identity, index count and logarithmic consequences. |
| dependency | [Fixed bounded norm event](Yin_C_F0187_v4.md#spectral-residual-spread) | Exponentially small exception for a fixed operator-norm bound, with the exact bounded centered input model. |
| dependency | [Bounded-product convex concentration](Yin_C_F0187_v2.md#argument) | Inequality (9) for independent bounded real coordinate blocks; accepted external input with its recorded source and proof-inspection boundary. |
| dependency | [Projected physical block geometry](Yin_C_F0187_v3.md#physical-block-distance) | Exact deletion restoring fresh-row independence and coordinate contraction, without invoking the positive-frame covariance bound. |
| dependency | [Block Gram and index identities](Yin_C_F0187_v3.md#block-negative-second-moment) | Exact negative-second-moment identity and row-deletion interlacing, restated at auxiliary size two and the new deletion range. |
| dependency | [Hermitized almost-sure weak convergence](Yin_C_F0186_v4.md#row-concentration) | Almost-sure singular-law convergence for this fixed matrix polynomial under arbitrary cross-size coupling. |
| dependency | [Arbitrary-coupling marginal criterion](Yin_C_F0190_v1.md#coupling-criterion) | In-probability convergence to a finite target and the existing almost-sure upper bound imply the limsup conclusion under every coupling. |
| dependency | [Exact finite and free determinant identities](../ledger/Yin_L_F0066_v5.md#model-and-determinants) | Direct bounded block factorization and accepted FK multiplicativity transfer the conditional logarithmic conclusions to the specified quadratic polynomial. |

### Decision operator-gap-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T21:00 |
| status | proved |
| reason | Adopt the exact C187v7 statement and argument after independent whole-proof review of its mixed fourth-layer calculation, operator-gap energy, fixed-effective-rank loads and three-branch matrix reduction. This decision concerns that earlier fixed statement; the separate intermediate-value candidate in the present version retains its own pending review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact operator-gap conclusions and three-branch consequence](Yin_C_F0187_v7.md#statement) | Bounded real two-channel model, all full or single-deletion minors and closest-mode choices; formal sign energy, load with a fixed effective-rank bound, and the Rademacher first-input matrix reduction with explicit remaining minor average. |
| argument | [Complete candidate proof](Yin_C_F0187_v7.md#argument) | Mixed coefficient inner-product bound, full-layer cancellation estimate, load interface, graph scale and measurable union of all three coefficient branches. |
| dependency | [Actual closest-mode cross-energy](Yin_C_F0187_v5.md#actual-cross-energy-statement) | Uniform cross fourth-layer squared coefficient norm at least c times residual squared Frobenius norm divided by N^4 on invertible bounded real minors. |
| dependency | [Residual physical row spread and norm/size controls](Yin_C_F0187_v4.md#spectral-residual-spread) | Uniform residual physical row energy, residual divergence and fixed norm event in the original-coordinate bounded real model. |
| dependency | [Closest-mode leverage and spectral mass](Yin_C_F0187_v4.md#fresh-row-projector) | Weighted minor mass and physical projector estimates give a closest eigenvalue tending to zero and vanishing leverage uniformly over all stated minors and mode choices. |
| dependency | [Fixed high-effective-rank whole-layer theorem](Yin_C_F0187_v6.md#statement) | The unchanged high-rank threshold and complete fourth-layer energy/load conclusion, used in the combined matrix consequence; its fresh-row identification also fixes the actual sign-border interpretation. |
| dependency | [Pole coefficient bounds and retained dominant threshold](Yin_C_F0194_v13.md#dominant-coefficients) | The pre-dominance residual row-load estimate and the existing dominant coefficient branch at its unchanged K_* threshold. |
| dependency | [General conditional matrix bridge](Yin_C_F0194_v13.md#statement) | Conditional graph-energy hypotheses and norm-guarded matrix reduction with matching error tending to zero. |
| dependency | [Largest-mode graph area](Yin_C_F0194_v13.md#pole-area) | Uniform graph area at most C times (1+abs(q))(1+residual operator norm), with no pole-dominance premise. |
| dependency | [Existing two-branch probability assembly](Yin_C_F0194_v13.md#combined-probability-assembly) | Minor-measurable high-rank and dominant good events, matched graph scales and uniform regularity exceptions, with their original thresholds retained in the new union. |
| dependency | [Original-input quadratic conversion](Yin_C_F0194_v13.md#dominant-probability-assembly) | The exact auxiliary-column swap and inverse-block identity give simultaneous singularity and s_min(Q_N) at least s_min(L_N). |
| review | [Independent operator-gap finding](../audits/reviews/Yin_R_F0191_v7.md#operator-gap-and-three-branch-reduction) | Complete exact C187v7 statement, new argument and direct fixed-input interfaces, including original branch thresholds and the remaining exceptional-minor average. |


### Decision comparable-modes-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T21:02 |
| status | proved |
| reason | Adopt the exact C187v8 deterministic comparable-mode separation, all-invertible complete fourth-layer energy/load theorem and singular-minor-only matrix reduction after independent whole-proof review. The exact operator-gap premise was separately reviewed and adopted without changing its mathematics. No singular-minor probability or unconditional logarithmic conclusion is asserted by this decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All-invertible energy and exact matrix consequence](Yin_C_F0187_v8.md#statement) | Bounded real actual two-channel minors, original normalization, deterministic raw comparable-mode separation, all-invertible formal-sign energy/load, actual single-deletion Rademacher border, and matrix reduction retaining the singular-minor average. |
| argument | [Complete candidate argument](Yin_C_F0187_v8.md#argument) | Actual inverse identities, three-operator Gram construction, finite quadratic-product algebra and Hilbert-space transfer, collision/load bounds, exhaustive coefficient regimes and measurable graph normalization. |
| dependency | [Joint approximate-mode gap](Yin_C_F0187_v5.md#statement) | Uniform no-common-approximate-mode bound for the two bounded real inputs, transferred explicitly to X and Y at a fixed center range. |
| dependency | [Full-inverse physical controls](Yin_C_F0187_v6.md#whole-layer-physical-transfer) | Uniform invertible-branch divergence, physical diagonal negligibility and vanishing normalized maximum physical row energy before imposing a rank branch. |
| dependency | [Exact fourth coefficient loads](Yin_C_F0187_v6.md#rank-refined-four-cycle-error) | The direct complete-layer coordinate load upper bound, with original N normalization, used independently of the high-rank lower bound. |
| dependency | [High-effective-rank energy and loads](Yin_C_F0187_v6.md#statement) | Unchanged fixed high-rank threshold and whole-layer energy/load theorem; its fixed fresh-row identification also fixes the actual sign-border scope. |
| dependency | [Operator-gap energy and loads](Yin_C_F0187_v7.md#statement) | Accepted exact operator-gap input, adopted by decision-operator-gap-reviewed in this material, with unchanged gap constant, complete-layer energy and fixed-rank load decay. |
| dependency | [General conditional graph bridge](Yin_C_F0194_v13.md#statement) | Real fair-sign fourth-energy/load conditions, graph area normalization and many-index norm-guarded matrix probability reduction. |
| dependency | [Largest-mode graph area](Yin_C_F0194_v13.md#pole-area) | Uniform area bound at scale Q times residual Frobenius norm for the separated branch, without Frobenius dominance. |
| dependency | [Norm event and quadratic conversion](Yin_C_F0194_v13.md#dominant-probability-assembly) | Fixed bounded-model full norm exception, actual fresh-row support bound, and exact inverse-block comparison s_min(Q_N) at least s_min(L_N). |
| review | [Independent comparable-mode finding](../audits/reviews/Yin_R_F0191_v8.md#comparable-modes-and-invertible-assembly) | Exact C187v8 statement, complete new argument and all declared dependency interfaces, including the separately adopted operator-gap input and the graph-normalized matrix reduction. |


### Decision balanced-middle-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T21:08 |
| status | proved |
| reason | Independent whole-proof review verified the exact bounded-law intermediate singular-value theorem, actual kernel balance, summable probability estimate, finite free logarithm and logarithmic consequences under the separate polynomial-floor hypothesis. This decision accepts precisely those conclusions and does not assert the additional floor. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Bounded two-channel middle and conditional log theorem](#statement) | Fixed real bounded centered laws, variance-one off-diagonals, original normalization, arbitrary cross-size coupling; summable middle bound, finite free target and logarithmic convergence conditional on an additional polynomial floor. |
| argument | [Complete balance and concentration proof](#argument) | Thin rectangle estimate, actual kernel balance, independent fresh-row covariance and concentration, block Gram identity, index count and logarithmic consequences. |
| dependency | [Fixed bounded norm event](Yin_C_F0187_v4.md#spectral-residual-spread) | Exponentially small exception for a fixed operator-norm bound, with the exact bounded centered input model. |
| dependency | [Bounded-product convex concentration](Yin_C_F0187_v2.md#argument) | Inequality (9) for independent bounded real coordinate blocks; accepted external input with its recorded source and proof-inspection boundary. |
| dependency | [Projected physical block geometry](Yin_C_F0187_v3.md#physical-block-distance) | Exact deletion restoring fresh-row independence and coordinate contraction, without invoking the positive-frame covariance bound. |
| dependency | [Block Gram and index identities](Yin_C_F0187_v3.md#block-negative-second-moment) | Exact negative-second-moment identity and row-deletion interlacing, restated at auxiliary size two and the new deletion range. |
| dependency | [Hermitized almost-sure weak convergence](Yin_C_F0186_v4.md#row-concentration) | Almost-sure singular-law convergence for this fixed matrix polynomial under arbitrary cross-size coupling. |
| dependency | [Arbitrary-coupling marginal criterion](Yin_C_F0190_v1.md#coupling-criterion) | In-probability convergence to a finite target and the existing almost-sure upper bound imply the limsup conclusion under every coupling. |
| dependency | [Exact finite and free determinant identities](../ledger/Yin_L_F0066_v5.md#model-and-determinants) | Direct bounded block factorization and accepted FK multiplicativity transfer the conditional logarithmic conclusions to the specified quadratic polynomial. |
| review | [Independent balanced-middle finding](../audits/reviews/Yin_R_F0191_v9.md#balanced-middle-and-conditional-log) | Exact statement and complete proof, all direct input interfaces, index and conditioning scope, weak-law upgrade, logarithmic limits and finite/free normalization. |

