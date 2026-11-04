---
author: Yin
---

# Degenerate GUE pencils: actual eliminations and the arbitrary-minor obstruction

Date and owner: 2026-11-04T17:20 UTC, Yin.
This records bounded exploration for [F0012](../tasks/Yin_T_F0012_v1.md#contract) and [S_F0028](../strategies/Yin_S_F0028.md#route).
The complete examples, failures and symmetrization mechanism below were developed and self-checked by the assigned agents.
They are not independent review evidence.
The separate general geometric result is [C_F0186](../claims/Yin_C_F0186_v1.md#statement), whose own assessment controls its use.

<a id="schur-findings"></a>
## Current finding

The normalized Schur estimate cannot be uniform over arbitrary bounded invertible minors, even when the fixed coefficient algebra is irreducible.
The four-dimensional three-cycle construction below gives a conditional distance of order an arbitrarily small parameter with high probability.
Its chosen minor does not belong to the actual monic pencil, so it does not refute F0012 or the structured-minor route.
For the actual pencil with these same coefficients, a different block elimination and conditional Gaussian estimate give a polynomial floor.
This actual model is irreducible, has \(\chi_R=0\), and admits no invertible left multiplier making every random coefficient self-adjoint.
The remaining general issue for the conditional Schur mechanism is to exploit the identity and coefficient relations retained by an actual minor instead of replacing it by an unrestricted deterministic matrix.

## A bounded-minor counterexample respecting the exposed GUE coefficients

Put \(m=4\), and use the five fixed coefficients
\[
 R_1=E_{31},\quad R_2=E_{32},\quad R_3=E_{43},\quad
 R_4=E_{14},\quad R_5=E_{24}.
 \tag{1}
\]
Decompose the auxiliary space as \(V_A\oplus V_B\oplus V_C\), with
\(V_A=\operatorname{span}(e_1,e_2)\), \(V_B=\mathbb Ce_3\), and \(V_C=\mathbb Ce_4\).
Each coefficient maps one step along \(V_A\to V_B\to V_C\to V_A\).
The directed graph of matrix units is strongly connected.
Products along directed paths therefore give every matrix unit, so the unital generated algebra is \(M_4(\mathbb C)\).
Nevertheless \(e_1^*R_je_1=0\) for every \(j\), hence \(\chi_R=0\).

Let \(n=N-1\), with \(N\ge3\), and expose one physical row and column exactly as for normalized GUE input.
Let \(g_{ji}\), \(1\le j\le5\), \(1\le i\le n\), be independent circular complex Gaussians with \(\mathbb E|g_{ji}|^2=1/N\).
Let \(h_j\) be independent real Gaussians of variance \(1/N\), independent of all \(g_{ji}\).
Define
\[
 B_i=\sum_jg_{ji}R_j,\qquad C_i=\sum_j\overline{g_{ji}}R_j,
 \qquad B=[B_1\ \cdots\ B_n],\qquad
 C=\operatorname{col}(C_1,\ldots,C_n),
 \qquad D=I_4+\sum_jh_jR_j.
 \tag{2}
\]
The notation for \(C\) means stacking the blocks without transposing their entries.
Thus \(B,C,D\) have precisely the joint exposed law of the corresponding monic GUE pencil.

Now replace the conditioned minor by the arbitrary bounded invertible matrix
\(Q_\delta=\delta I_{4n}\), with \(0<\delta\le1\).
Then \(BC=\sum_iB_iC_i\) is a sum of words of length two in the coefficients.
Every such word maps \(V_A\to V_C\), \(V_B\to V_A\), and \(V_C\to V_B\).
The images of the three domain summands are in distinct target summands, and each restriction has rank at most one.
Consequently
\[
 \operatorname{rank}(BC)\le3
 \tag{3}
\]
for every realization, including when the entries are complex.
For a unit \(x\in\ker(BC)\), the normalized Schur distance satisfies
\[
 F_\delta x=(I_4+\delta^{-2}BB^*)^{-1/2}Dx,
 \qquad
 s_{\min}(F_\delta)\le
 \frac{\delta\|D\|}{s_{\min}(B)}
 \tag{4}
\]
whenever \(B\) has full row rank.

This full-rank event is not a rare condition.
The first two rows of \(B\) occupy the auxiliary-coordinate-four columns, with coefficient rows \((g_{4i})_i\) and \((g_{5i})_i\).
Its third row occupies auxiliary-coordinate-one and auxiliary-coordinate-two columns with coefficients \((g_{1i},g_{2i})_i\), and its fourth row occupies auxiliary-coordinate-three columns with coefficients \((g_{3i})_i\).
These supports are disjoint except for the first two rows.
The elementary law of large numbers gives
\[
 BB^*\xrightarrow{\mathbb P}\operatorname{diag}(1,1,2,1),
 \qquad \|D-I_4\|\xrightarrow{\mathbb P}0.
 \tag{5}
\]
Thus, for example, \(\mathbb P\{s_{\min}(F_\delta)\le4\delta\}\to1\), uniformly over deterministic choices of \(\delta=\delta_N\in(0,1]\).
Taking \(\delta_N=e^{-N}\) defeats every proposed uniform conditional floor \(e^{-N^\kappa}\) with \(0<\kappa<1\).

The failure is an exact obstruction to an unrestricted-minor lemma, not just the unrelated triangular-matrix warning in the starting synthesis.
It keeps fixed irreducible coefficients, GUE row/column correlation, fixed-dimensional block size, bounded \(Q_\delta\), and invertibility of the minor.
It does not keep the minor's actual pencil form.
For the coefficients (1), every actual minor is
\(I_{4n}+\sum_jR_j\otimes A_j\), whose four auxiliary diagonal blocks equal \(I_n\).
Therefore \(Q_\delta\) is not an actual minor unless \(\delta=1\).
This is exactly the hypothesis that a successful revised estimate must use.

## Actual-minor coefficient frames

Suppose \(Q=I_m\otimes I_n+\sum_jR_j\otimes A_j\), with Hermitian \(A_j\) satisfying \(\max_j\|A_j\|\le M\).
For a unit vector \(v\) with \(\|Qv\|\le\varepsilon<1\), commutation of the two tensor factors gives
\[
 1-\varepsilon
 \le\left\|\sum_j(I_m\otimes A_j)(R_j\otimes I_n)v\right\|
 \le M\sqrt d\left(\sum_j\|(R_j\otimes I_n)v\|^2\right)^{1/2}.
 \tag{6}
\]
For a unit \(u\) with \(\|Q^*u\|\le\varepsilon\), the same estimate holds with \(R_j^*\) in place of \(R_j\).
In particular, exposed Gaussian row and column couplings to actual near-kernel vectors have mean-square size at least \((1-\varepsilon)^2/(NdM^2)\).
This prevents exact invisibility of a single actual pole to either side separately.
It does not yet control their joint matrix determinant or the graph normalization.
The correlation of the two couplings and simultaneous near-kernel directions remain substantive obligations.

## The actual three-cycle model has a polynomial floor

For the coefficients (1) and independent normalized GUE inputs \(H_1,\ldots,H_5\), the actual pencil is
\[
 T_N=
 \begin{pmatrix}
 I&0&0&H_4\\
 0&I&0&H_5\\
 H_1&H_2&I&0\\
 0&0&H_3&I
 \end{pmatrix}.
 \tag{7}
\]
Use the fourth auxiliary block as root, and the first three as auxiliaries.
Their minor and inverse are
\[
 Q_0=
 \begin{pmatrix}I&0&0\\0&I&0\\H_1&H_2&I\end{pmatrix},
 \qquad
 Q_0^{-1}=
 \begin{pmatrix}I&0&0\\0&I&0\\-H_1&-H_2&I\end{pmatrix}.
\]
The root Schur complement is
\[
 S_N=I+H_3(H_1H_4+H_2H_5).
 \tag{8}
\]
The elementary block factorization in [L58v2](../ledger/Yin_L_F0058_v2.md#exact-linearization) applies to this auxiliary elimination.
On \(\max_j\|H_j\|\le M\), its factors and inverses have norm bounded by a constant depending only on \(M\), so
\[
 s_{\min}(T_N)\ge c_M\min(s_{\min}(S_N),1).
 \tag{9}
\]
This is an auxiliary-coordinate elimination, distinct from the physical-row deletion in (2).

Condition now on \(H_1,H_2,H_3\).
The original Schur complement (8) is jointly Gaussian in the still independent GUE inputs \(H_4,H_5\).
For unit vectors \(u,v\in\mathbb C^N\), its centered complex variance is exactly
\[
 \mathbb E_{H_4,H_5}|u^*(S_N-I)v|^2
 =\frac1N\big(\|H_1H_3u\|^2+\|H_2H_3u\|^2\big)
 \ge \frac{s_{\min}(H_1)^2s_{\min}(H_3)^2}{N}.
 \tag{10}
\]
The formula follows from the same conjugated covariance identity as [L58v1, (G)](../ledger/Yin_L_F0058_v1.md#conditional-gaussian); the two summands have zero cross covariance by independence.

The needed lower bounds for \(H_1\) and \(H_3\) follow without a local spectral law.
For one normalized GUE matrix, write \(H=H^0+(g/N)I\), with \(g\sim N(0,1)\) independent of \(H^0\).
Conditioning on \(H^0\) and taking a union over its \(N\) eigenvalues gives
\[
 \mathbb P\{s_{\min}(H)\le\delta\}\le C N^2\delta.
 \tag{11}
\]
Fix \(b>2\) and restrict to \(s_{\min}(H_1),s_{\min}(H_3)\ge N^{-b}\).
Then (10) is at least \(N^{-4b-1}\).
A real projection of a complex Gaussian and its density bound give the global bilinear small-ball condition with threshold \(cN^{-2b-1/2}\), uniformly over the deterministic mean \(u^*v\).
On \(\max_{1\le j\le3}\|H_j\|\le M\),
\[
 \|S_N\|\le1+M^2(\|H_4\|+\|H_5\|),
\]
so its conditional norm has a fixed quantile bound depending only on \(M\).
Use [Nie22, arXiv:2111.05553v2, Theorem 1.6](https://arxiv.org/html/2111.05553v2#S1.SS2) at the statement scope retained in [L58v1](../ledger/Yin_L_F0058_v1.md#source-boundary).
For fixed \(r>0\), take its small-probability parameter equal to \(N^{-r}\).
Combining that theorem with (9)--(11) gives constants \(c_M,C_M>0\) such that, for sufficiently large \(N\),
\[
 \mathbb P\{s_{\min}(T_N)<c_MN^{-(4b+4+2r)}\}
 \le C_M N^{2-b}+C_M N^{-r}
       +\sum_{j=1}^{5}\mathbb P\{\|H_j\|>M\}.
 \tag{12}
\]
For fixed \(M>2\), the right side tends to zero by the usual normalized GUE norm bound already used in the starting analytic bridge.
For example \(b=3,r=1\) gives a constant multiple of \(N^{-18}\) as a sufficient floor, with an \(O(N^{-1})\) algebraic error plus the norm tails.
The exponent is deliberately crude.

This estimate controls all actual physical block distances in probability as well.
Indeed, for any invertible matrix \(T\), a unit vector \(x\) in one block, and any vector \(y\) in the other blocks,
\[
 \|T(E_ax+E_{-a}y)\|\ge s_{\min}(T)\sqrt{1+\|y\|^2}\ge s_{\min}(T).
\]
Taking the infimum over \(y\) shows \(s_{\min}(F_a)\ge s_{\min}(T)\).
This conclusion is an unconditional estimate for the actual ensemble.
It does not assert a uniform conditional bound after fixing an arbitrary physical minor.

The example is outside the simultaneously symmetrizable-coefficient class.
If an invertible matrix \(J\) made both \(JR_1\) and \(JR_2\) self-adjoint, then
\(JR_1=(Je_3)e_1^*\) would force \(Je_3\in\mathbb Ce_1\), while
\(JR_2=(Je_3)e_2^*\) would force \(Je_3\in\mathbb Ce_2\).
Thus \(Je_3=0\), contradicting invertibility.
In particular no invertible Hermitian symmetrizer exists.

The same calculation allows replacing the root identity in (8) by \(-zI\) for any fixed \(z\): only the deterministic mean and norm quantile change.
It therefore provides a candidate full hermitization bridge for the scalar polynomial
\(P(x_1,\ldots,x_5)=x_3x_1x_4+x_3x_2x_5\), not merely a zero-shift pencil estimate.
This polynomial has nonnormal Hermitian evaluations: take \(x_3=I\), \(x_2=0\), \(x_1=\operatorname{diag}(1,2)\), and \(x_4=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).
The resulting value is \(\begin{pmatrix}0&1\\2&0\end{pmatrix}\).
The [common analytic bridge](../ledger/Yin_L_F0058_v1.md#common-bridge) supplies the remaining source-based convergence argument at its recorded inspection scope.
The present derivation is unreviewed development; it is not a Claim assessment or a proof of the arbitrary-coefficient target.

## Consequence for the general route

The three-cycle example separates three assertions that should not be conflated.
Irreducibility alone does not give an estimate uniform over bounded arbitrary minors, as (1)--(5) show.
The actual pencil with those coefficients nevertheless has a polynomial floor, by (7)--(12).
Its successful proof changes the block elimination and preserves independent Gaussian inputs, rather than estimating a physical Schur complement uniformly in its minor.
For general coefficients, locating such an elimination or quantifying the actual-minor constraints remains open.
The frame bounds (6) are necessary usable information but do not yet settle the joint normalized determinant.

<a id="symmetrizer"></a>

## A separate exact mechanism: symmetrization and a positive trace direction

Suppose there is a fixed invertible Hermitian matrix \(J\in M_m(\mathbb C)\) such that every \(JR_j\) is Hermitian.
Suppose also that a real unit vector \(a\in\mathbb R^d\) satisfies
\[
 B:=\sum_j a_j JR_j>0.
 \tag{SP}
\]
Then \(K_N:=(J\otimes I_N)T_N\) is Hermitian.
Write the exact GUE trace decomposition
\[
 H_j=H_j^0+(g_j/N)I_N,
 \qquad g_j=\operatorname{Tr}H_j\sim N(0,1).
\]
The \(g_j\) are independent of the traceless inputs and independent across \(j\).
Decompose \(g=\xi a+g^\perp\), where \(\xi\sim N(0,1)\) is independent of \(g^\perp\) and all traceless inputs.
Conditioning on these latter variables gives
\[
 K_N=K_N^0+(\xi/N)(B\otimes I_N),
 \qquad
 (B^{-1/2}\otimes I_N)K_N(B^{-1/2}\otimes I_N)
 =S_N^0+(\xi/N)I_{mN},
\]
where \(S_N^0\) is conditionally deterministic and Hermitian.
If \(s_{\min}(T_N)<\varepsilon\), then
\[
 s_{\min}(S_N^0+(\xi/N)I_{mN})
 < \frac{\|J\|}{\lambda_{\min}(B)}\varepsilon.
\]
Each of the \(mN\) real eigenvalues of \(S_N^0\) excludes an interval for \(\xi\) of length at most \(2N\|J\|\varepsilon/\lambda_{\min}(B)\).
The standard Gaussian density is bounded by \((2\pi)^{-1/2}\), so conditioning and the union bound give
\[
 \mathbb P\{s_{\min}(T_N)<\varepsilon\}
 \le \frac{2m\|J\|}{\sqrt{2\pi}\lambda_{\min}(B)}N^2\varepsilon.
 \tag{SPB}
\]
No input norm event is needed for this estimate.

For \(m=d=2\), take \(R_1=E_{12}\), \(R_2=E_{21}\), and \(J=E_{12}+E_{21}\).
Then \(JR_1=E_{22}\), \(JR_2=E_{11}\), and \(a=(1,1)/\sqrt2\) gives \(B=I_2/\sqrt2\).
The coefficient algebra is all of \(M_2(\mathbb C)\), although the one-step covariance quantity \(\chi_R\) vanishes.
Thus (SPB) handles a genuine degenerate coefficient space by a mechanism not supplied by Nie22's global bilinear condition.

This family does not automatically propagate to the coefficients of \(P(H)-zI\) for almost every complex \(z\).
In particular, the usual Hermitization coefficients \(\begin{psmallmatrix}0&R_j\\R_j^*&0\end{psmallmatrix}\) have no positive definite real linear combination, since each such combination has spectrum symmetric about zero.
The existence of \(J\) and the definite direction (SP) must be checked at the actual pencil.
This calculation is retained as development evidence and a calibration mechanism, without a formal Claim assessment.

## Further limits of covariance-based repairs

Invertible left and right operator scaling preserves the existence of annihilating bilinear pairs, so it cannot turn \(\chi_R=0\) into the existing one-step condition.
Indeed, under \(R_j\mapsto LR_jK\), an annihilating pair \((a,b)\) becomes \((L^{-*}a,K^{-1}b)\), followed by normalization.
Passing to products of coefficient matrices creates a stronger deterministic covariance map but does not create independent noise coefficients for those products in the original pencil.
Stationary GUE input refresh preserves the desired distribution but also preserves the deficient linear noise space for a pencil, leaving a new quantitative estimate necessary.
These observations concern the inspected implementations, not impossibility of broader scaling or stochastic approaches.
