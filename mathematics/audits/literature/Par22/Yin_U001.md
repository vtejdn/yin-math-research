---
author: Yin
---

# Par22-U001: Matrix-coefficient Haar resolvent comparison and conditional concentration

<a id="par22-u001"></a>
## Exact source and accepted scope

The inspected edition is [arXiv:2005.13834v2](../../../literature/pdf/Par22--arxiv-v2.pdf), with [edition notes](readme.md).
The reading covers Theorem 1.1 and its amplification remarks on PDF p. 3, Corollary 1.1 on pp. 4--5, the free-product and trace conventions in Section 2.4 on p. 11, Theorem 4.1 on pp. 24--25, its constant-dependence paragraph on p. 25, the resolvent proof in Section 5.1 on pp. 34--35, and Proposition 5.1 with its proof on pp. 36--37.
The displays on pp. 5, 25 and 35 were visually inspected in addition to text reading.
Corollary 1.1 and Proposition 5.1 are accepted as established external inputs at the precise statements below after checking the fixed-matrix Hermitization application and the distinction between their centers.
The Fourier calculation producing the resolvent powers was checked directly.
The proof of Theorem 4.1 through free unitary Brownian motion, covariance estimates and Lemma 4.4 was not re-audited in full.
Proposition 5.1 invokes special-unitary concentration in Anderson--Guionnet--Zeitouni, Corollary 4.4.28; that foundational proof was not independently re-audited here.
This preparation is proof development, not independent review of a resulting project theorem.

<a id="matrix-polynomial-resolvent"></a>
## Exact tensor-amplified resolvent interface

Let \(U^{(N)}=(U_1^{(N)},\ldots,U_p^{(N)})\) be independent Haar \(U(N)\) matrices, let \(u=(u_1,\ldots,u_p)\) be free Haar unitaries in a tracial \(C^*\)-probability space \((\mathcal A,\tau)\), and include their adjoints in polynomial evaluation.
Let \(Y=(Y_1,\ldots,Y_q)\subset M_M(\mathbb C)\) be arbitrary deterministic matrices, including adjoints, and let \(P\) be a fixed selfadjoint noncommutative polynomial.
Set
\[
 P_N=P(U^{(N)}\otimes I_M,I_N\otimes Y),
 \qquad P_\infty=P(u\otimes I_M,1\otimes Y).
\]
The free tensor model uses \(\mathcal A\otimes M_M(\mathbb C)\) with normalized trace \(\tau\otimes\operatorname{tr}_M\).
The deterministic matrices commute with the Haar variables through the tensor factors but need not commute with one another.
Define
\[
 G_N(z)=\frac1{NM}\operatorname{Tr}_{NM}(zI-P_N)^{-1},
 \qquad G_\infty(z)=(\tau\otimes\operatorname{tr}_M)(zI-P_\infty)^{-1},
 \qquad \|Y\|=\max_j\|Y_j\|.
\]
Corollary 1.1 gives a polynomial \(L_P\), depending only on \(P\), such that for \(N\ge2\), every \(M,Y\), and \(z\notin\mathbb R\),
\[
 |\mathbb EG_N(z)-G_\infty(z)|
 \le L_P(\|Y\|)\frac{M^2\log^2N}{N^2}
       \left(|\operatorname{Im}z|^{-5}+|\operatorname{Im}z|^{-2}\right).
 \tag{Par-resolvent}
\]
The source display is written for all natural dimensions; only \(N\ge2\) is used here, and its \(\log^2N\) expression is not used at \(N=1\).
No deterministic empirical-law convergence rate, regular-bulk hypothesis, invertibility assumption, or commutation hypothesis on the members of \(Y\) is required.
The \(M^2\) factor is retained for noncommuting matrix coefficients.

<a id="fourier-proof-passage"></a>
## Critical Fourier passage

In this tensor setting Theorem 4.1 bounds the expected normalized-trace difference for
\[
 f(x)=\int_{\mathbb R}e^{ixy}\,d\nu(y),
 \qquad \int_{\mathbb R}(1+y^4)\,d|\nu|(y)<\infty,
\]
by
\[
 \frac{M^2\log^2N}{N^2}L_P(\|Y\|)
   \int_{\mathbb R}(|y|+y^4)\,d|\nu|(y).
 \tag{Par-Fourier}
\]
Section 5.1 takes \(f_z(x)=(z-x)^{-1}\).
For \(\operatorname{Im}z<0\), it uses \(d\nu_z(y)=i e^{-iyz}\mathbf1_{y\ge0}\,dy\), giving exactly
\[
 \int_0^\infty(y+y^4)e^{-|\operatorname{Im}z|y}\,dy
 =|\operatorname{Im}z|^{-2}+24|\operatorname{Im}z|^{-5}.
\]
Conjugation gives the other half-plane, and 24 is absorbed into \(L_P\).
An intermediate line on p. 35 prints \(1+y^4\), whereas its preceding exact integral, Theorem 4.1, and final resolvent bound use the needed \(y+y^4\) weight.
The stated resolvent powers follow from the latter exact weight without relying on that inconsistent intermediate typography.

<a id="haar-hermitization-match"></a>
## Fixed matrix coefficients and Hermitization

For \(L_N=A_0\otimes I_N+\sum_jA_j\otimes U_j^{(N)}\), take \(M=2m\) and
\[
 B_0=\begin{pmatrix}0&A_0\\A_0^*&0\end{pmatrix},
 \qquad B_j=\begin{pmatrix}0&A_j\\0&0\end{pmatrix}.
\]
Its Hermitization is
\[
 \mathcal H_N=B_0\otimes I_N+
       \sum_j\bigl(B_j\otimes U_j^{(N)}+B_j^*\otimes(U_j^{(N)})^*\bigr).
\]
After flipping tensor factors, use the selfadjoint polynomial
\[
 P(x,y)=\tfrac12(y_0+y_0^*)+\sum_j(y_jx_j+x_j^*y_j^*)
\]
at \(x_j=U_j^{(N)}\otimes I_M\), \(y_j=I_N\otimes B_j\).
The same flip identifies the free target with the Hermitization of \(A_0\otimes1+\sum_jA_j\otimes u_j\), preserving normalized trace.
Thus (Par-resolvent) gives \(CN^{-2}\log^2N(\eta^{-5}+\eta^{-2})\) at \(z=i\eta\), with \(C\) depending only on the fixed tuple.
Bounded deterministic parameter dependence gives uniform constants on compact parameter sets through \(L_P(\|Y\|)\).
No conclusion controlling the smallest singular value follows from this comparison alone.

<a id="conditional-special-unitary-concentration"></a>
## Exact concentration statement and its center

Proposition 5.1 assumes a continuous \(f:U(N)^p\to\mathbb C\) with
\[
 |f(X)-f(Y)|\le L
   \left(\sum_{j=1}^p\operatorname{Tr}_N((X_j-Y_j)(X_j-Y_j)^*)\right)^{1/2}.
\]
Here \(\operatorname{Tr}_N\) is unnormalized, so the metric is product chordal Hilbert--Schmidt distance.
Let \(U_j\) be independent Haar \(U(N)\) matrices and independently let \(W_j\) be independent Haar \(SU(N)\) matrices.
Then
\[
 \mathbb P\bigl\{|f(U)-\mathbb E_Wf(W_1U_1,\ldots,W_pU_p)|\ge\delta\bigr\}
 \le4p\exp\left(-\frac{N\delta^2}{4p^2L^2}\right).
 \tag{Par-SU-concentration}
\]
The center is a conditional special-unitary average, not \(\mathbb Ef(U)\).
The central-phase correction and spectral-statistic application are developed separately in [C_F0192_v2](../../../claims/Yin_C_F0192_v2.md#haar-concentration).
The source uses independence within each dimension; summable dimensionwise bounds need no independence between dimensions.
