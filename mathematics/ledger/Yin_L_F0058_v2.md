---
author: Yin
---

# F0012: exact linear-pencil reduction and the reach of conditional Gaussianity

Date and owner: 2026-11-04T16:33 UTC, Yin.
This development synthesis answers whether [S_F0027](../strategies/Yin_S_F0027.md#route) supplies a route to general polynomials and makes the linearization interface explicit.
The main agent and two development subagents checked the algebra and applicability boundaries.
No independent review, full-class estimate or Claim assessment is asserted.

## Inputs and scope

The [first synthesis](Yin_L_F0058_v1.md) retains the conditional Gaussian subclass, the mesoscopic singular-value estimates, the sufficient logarithmic-tail bridge and the normalized Schur candidate.
This version adds the exact general reduction and refines the relation between that subclass and the general route; it does not replace or duplicate those arguments.
[Han26, Section 2.2, Lemma 2.1 and Fact 2.4](https://arxiv.org/html/2606.01664v1#S2.SS2) were checked again for the algebraic reduction.
Its Theorem 1.5 concerns Ginibre inputs, not the GUE estimate proposed below.
The [existing local inspection](../audits/literature/Han26/Yin_U001.md#linearization) supplies the same source boundary.
Nie22 is reused at the exact [statement scope already inspected](Yin_L_F0058_v1.md#source-boundary).
A bounded additional search for Kronecker/GUE pencils and small singular values supplied no theorem resolving the arbitrary-coefficient target below; this is not a nonexistence claim.

<a id="exact-linearization"></a>
## Exact reduction to a fixed-size affine pencil

Write a fixed scalar polynomial as
\(P(x)=c_0+\sum_j c_jx_j+\sum_{|w|\ge2}c_w x_{i_1}\cdots x_{i_{|w|}}\), omitting zero coefficients.
For each word of length \(k\ge2\), introduce \(k-1\) auxiliary coordinates and put
\[
 Q_w:=I_{k-1}-T_w,\qquad (T_w)_{r,r+1}:=x_{i_{r+1}}\quad(1\le r\le k-2).
\]
Thus \(Q_w^{-1}=I+T_w+\cdots+T_w^{k-2}\) in every unital algebra.
Let \(B_w\) have first entry \(c_wx_{i_1}\) and other entries zero, and let \(C_w\) have last entry \(-x_{i_k}\) and other entries zero.
Then
\[
 -B_wQ_w^{-1}C_w=c_wx_{i_1}\cdots x_{i_k}.
\]
With \(Q:=\bigoplus_w Q_w\), \(B:=(B_w)_w\), \(C:=(C_w)_w^{\mathsf T}\), and
\(a_z:=c_0-z+\sum_jc_jx_j\), form
\[
 L_P(z;x):=\begin{pmatrix}a_z&B\\C&Q\end{pmatrix}
 =A_0-zE_{11}+\sum_{j=1}^d A_jx_j.
 \tag{L}
\]
Its size \(m:=1+\sum_{|w|\ge2}(|w|-1)\) depends only on \(P\), not \(N\).
The notation \(C:=(C_w)_w^{\mathsf T}\) means stacking the column blocks, without transposing their algebra entries.
If no auxiliary coordinates are needed, use \(m=1\) and \(L_P=P-z\).

The Schur complement is exactly
\[
 a_z-BQ^{-1}C=P(x)-z.
\]
This word-chain construction is an elementary, possibly nonminimal implementation of the linearization principle; Han26 uses smaller coefficient-tensor factorizations.
For matrix input \(H^{(N)}\), (L) becomes
\[
 L_N(z):=A_0\otimes I_N+\sum_j A_j\otimes H_j^{(N)}-zE_{11}\otimes I_N.
\]
The block \(Q(H)\) is unit upper triangular.
Consequently
\[
 \det L_N(z)=\det(P(H^{(N)})-zI_N),\qquad
 (L_N(z)^{-1})_{11}=(P(H^{(N)})-zI_N)^{-1},
 \tag{D}
\]
where the inverse identity is used on the equivalent invertibility domains.
In particular \(s_{\min}(P(H)-zI)\ge s_{\min}(L_N(z))\), including the singular case.

Let \(S:=P(H)-zI\).
The exact factorization
\[
 L_N=
 \begin{pmatrix}I&BQ^{-1}\\0&I\end{pmatrix}
 \begin{pmatrix}S&0\\0&Q\end{pmatrix}
 \begin{pmatrix}I&0\\Q^{-1}C&I\end{pmatrix}
 \tag{E}
\]
also controls the whole singular-value list.
On \(\max_j\|H_j\|\le R\), all auxiliary factors and their inverses are bounded by constants depending only on \(P,R\).
The polynomial inverse of \(Q\) is essential here.
Thus for some \(c_{P,R}>0\),
\[
 c_{P,R}\min(s_{\min}(S),1)\le s_{\min}(L_N)\le s_{\min}(S).
\]
Singular values of \(L_N\) and \(\operatorname{diag}(S,Q)\) are comparable up to fixed factors by (E).
Since \(Q\) has its smallest singular value bounded below, small-singular-value counting and logarithmic tails transfer with the normalization factor \(1/m\).
This is an analytic reduction, not merely an equivalence of exact invertibility.

<a id="monic-target"></a>
## The monic GUE-pencil target sufficient for F0012

At zero input, \(L_P(z;0)=D_z:=\operatorname{diag}(c_0-z,1,\ldots,1)\).
For fixed \(z\ne c_0\), define
\[
 T_N(z):=(D_z^{-1}\otimes I_N)L_N(z)
 =I_m\otimes I_N+\sum_j R_j(z)\otimes H_j^{(N)},\qquad R_j(z):=D_z^{-1}A_j.
 \tag{M}
\]
There is no \(N\)-dependent coefficient loss.
Moreover \((T_N(z)^{-1})_{11}=(c_0-z)S^{-1}\), so
\[
 s_{\min}(S)\ge |c_0-z|\,s_{\min}(T_N(z)).
\]
The one excluded point is harmless for almost-everywhere hermitization.

A clean sufficient research target is:

For every fixed \(m,d\) and \(R_1,\ldots,R_d\in M_m(\mathbb C)\), there is a finite \(C_R>0\) such that
\[
 \mathbb P\!\left\{
 s_{\min}\!\left(I_m\otimes I_N+\sum_jR_j\otimes H_j^{(N)}\right)<N^{-C_R}
 \right\}\longrightarrow0.
 \tag{GUE-P}
\]

This is a proposed GUE counterpart of Han26 Theorem 1.5.
It is not claimed proved or necessary for F0012.
For each fixed \(z\ne c_0\), (GUE-P) applies to the fixed matrices \(R_j(z)\).
The inverse-compression estimate transfers it to \(P(H)-zI\), and the [existing mesoscopic/logarithmic bridge](Yin_L_F0058_v1.md#common-bridge) finishes the original Task.
No uniformity over all \(z\), all polynomials or growing \(m\) is required.
A suitably small subexponential floor, with exponent matched to the retained mesoscopic bound, would also suffice.

<a id="spectral-parameter"></a>
## Preserve the spectral parameter and normalization

For \(u_N(z):=N^{-1}\log|\det(P(H)-zI)|\), (D) gives
\[
 \frac1{mN}\log|\det L_N(z)|=\frac1m u_N(z).
\]
The original eigenvalue measure is therefore recovered from this pencil potential by multiplying its distributional Laplacian by \(m/(2\pi)\).
The parameter coefficient in (L) is \(E_{11}\), not \(I_m\).
Ordinary eigenvalues of \(L_N(0)\) correspond instead to \(\det(L_N(0)-zI_{mN})\), a different polynomial.
Thus an ordinary Brown-measure convergence theorem for that single matrix cannot be substituted for the required pencil-potential statement.

The monic normalization has a further deterministic correction:
\[
 \frac1{mN}\log|\det T_N(z)|
 =\frac1m\big(u_N(z)-\log|c_0-z|\big).
\]
Its missing logarithm cannot be discarded before taking the distributional Laplacian.

For singular-value analysis, hermitize (M):
\[
 \mathcal H_N(z):=
 \begin{pmatrix}0&T_N(z)\\T_N(z)^*&0\end{pmatrix}
 =
 \begin{pmatrix}0&I_m\\I_m&0\end{pmatrix}\otimes I_N+
 \sum_j\begin{pmatrix}0&R_j(z)\\R_j(z)^*&0\end{pmatrix}\otimes H_j^{(N)}.
\]
The coefficients are self-adjoint and fixed size.
This supplies a self-adjoint matrix-valued semicircular limit after replacing \(H_j\) by \(s_j\).
It handles the fixed-regularizer limit but does not by itself control the logarithmic singularity at zero.
The non-Hermitian pencil before hermitization should not itself be called a self-adjoint operator-valued semicircular variable.

<a id="covariance-boundary"></a>
## What F0027 teaches, and the exact obstruction to applying Nie directly

A GUE pencil is already jointly Gaussian, irrespective of \(m\).
Gaussianity is therefore not the missing general ingredient.
For \(T_N=I_m\otimes I_N+\sum_jR_j\otimes H_j\) and unit block vectors \(u=(u_a)\), \(v=(v_b)\), its centered complex variance is
\[
 \mathbb E|u^*(T_N-\mathbb ET_N)v|^2
 =\frac1N\sum_j\left\|\sum_{a,b}(R_j)_{ab}v_bu_a^*\right\|_{\mathrm{HS}}^2.
 \tag{C}
\]
This follows directly from the conjugated GUE covariance used in the [subclass calculation](Yin_L_F0058_v1.md#conditional-gaussian).

Define the finite-dimensional coefficient quantity
\[
 \chi_R:=\inf_{\|a\|=\|b\|=1}\sum_j|a^*R_jb|^2.
\]
If \(\chi_R>0\), sum its inequality over physical coordinate pairs in (C).
The sums of squared norms of the corresponding auxiliary vectors are both one, so (C) is at least \(\chi_R/N\).
A real projection of the complex Gaussian gives the required small-ball bound uniformly over the deterministic mean.
Since the pencil has a fixed norm quantile, Nie22 yields a polynomial floor.
For example, for fixed \(r>0\), threshold \(c_RN^{-4-2r}\) has failure probability at most \(CN^{-r}\), with the fixed \(m\)-factors absorbed into \(c_R\).

But \(\chi_R>0\) need not hold for polynomial linearizations.
For the complex linear space \(\mathcal S:=\operatorname{span}\{R_j\}\), it says exactly that \(\mathcal S b=\mathbb C^m\) for every nonzero \(b\).
Compactness gives the positive uniform constant when no pair annihilates every coefficient.
If \(\chi_R=0\), take unit \(a,b\) annihilating every \(a^*R_jb\), and orthogonal physical vectors \(\xi,\eta\) for \(N\ge2\).
Then \(u:=a\otimes\xi\), \(v:=b\otimes\eta\) make \(u^*T_Nv=0\) identically, including its mean.
Nie22's global condition then fails.
Adding the deterministic identity to the random coefficient space is not legitimate.

Even \(R_1=E_{12}\), \(R_2=E_{21}\) generate \(M_2(\mathbb C)\) while \(\chi_R=0\), witnessed by \(a=b=e_1\).
Thus irreducibility of the generated algebra is weaker than the needed one-step noise condition.
This does not imply that such pencils are singular or that (GUE-P) is false.
It identifies the limitation of the direct black-box application.

In F0027, conditioning on \(H_1\), passing to its eigenbasis and eliminating auxiliary blocks leaves the Gaussian noise map
\(\Phi_D(X):=DX+2XD\).
Its matrix-unit weights \(\lambda_i+2\lambda_j\) have a polynomial lower bound from the trace split.
This creates the effective covariance lower bound on the original matrix.
The same example in its sparse \(3\)-by-\(3\) linearization has zero bilinear directions, as recorded in [v1](Yin_L_F0058_v1.md#schur-route).

For a general polynomial, eliminating auxiliaries can leave multiple occurrences of the same unconditioned GUE input.
The effective random matrix is then a Gaussian polynomial or rational expression, not jointly Gaussian.
Consequently F0027 supplies a useful mechanism and a calibration case, but no automatic induction on polynomial degree.

<a id="revised-allocation"></a>
## General route and next discriminating question

The full-class objective should be (GUE-P), or its weaker logarithmic-tail version, under [S_F0028](../strategies/Yin_S_F0028.md#route).
Keep F0027 as a concrete supporting mechanism rather than a promise that solving increasingly complicated subclasses will exhaust F0012.
The precise next issue is whether conditioning and normalized block elimination can recover enough effective noise directions for pencils with \(\chi_R=0\).

The finite-dimensional coefficient algebra can guide a composition-series reduction, as in the algebraic part of Han26.
On irreducible factors, products of coefficients give more directions than their linear span.
Those product directions do not carry independent Gaussian coefficients in the original pencil.
Turning that algebraic propagation into a quantitative estimate on actual normalized block distances is the unproved step.
The [Schur-complement candidate](Yin_L_F0058_v1.md#schur-route) identifies the correct random normalization to retain.
A successful finite-size example must demonstrate that estimate on a genuinely degenerate coefficient space, not merely recheck the already sufficient condition \(\chi_R>0\).
