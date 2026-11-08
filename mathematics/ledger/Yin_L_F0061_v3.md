---
author: Yin
---

# Fourth moments as a first case for Wigner determinants and Brown measures

This comparison was prepared for Yin's question of 2026-11-08 about the order in which to study [F0012](../tasks/Yin_T_F0012_v3.md#contract), [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract).
Keep the fixed laws, within-size independence and arbitrary cross-size coupling of those contracts.
Assume in this discussion that the off-diagonal laws have finite fourth absolute moments; the diagonal laws still need only finite second moments.
This is a comparison of two published estimates with the existing Task reductions, checked in the course of this discussion without independent project review.

<a id="gap"></a>
## What a fourth moment buys when the free pencil is invertible

Write \(L_N=A_0\otimes I_N+\sum_{j=1}^d A_j\otimes W_j^{(N)}\) and \(L=A_0\otimes1+\sum_{j=1}^d A_j\otimes s_j\) for the fixed \(m\)-dimensional coefficients of F0013.
If \(L\) has a bounded inverse, set \(\gamma=\|L^{-1}\|^{-1}>0\).
The following application gives \((mN)^{-1}\log|\det L_N|\to\log\Delta(L)\) in probability and hence the requested almost-sure limsup under every coupling.
There is no selfadjointness or positive-frame assumption on the coefficients, and the real and imaginary parts of an entry may be dependent.

For each off-diagonal law, truncate \(\xi\) to \(\xi{\bf1}_{|\xi|\le K}\), subtract its mean and divide by its standard deviation to obtain \(u_K\).
For sufficiently large fixed \(K\) the denominator is positive and tends to one as \(K\to\infty\), so \(\|\xi-u_K\|_4\to0\).
Let \(H_{j,K}^{(N)}\) use these same transformed entries with zero diagonal and the original normalization.
For each fixed \(K\), these bounded Wigner inputs meet the hypotheses of Brailovskaya and van Handel, [author manuscript, §2.1.4 and §9.4.1, Theorem 9.17 and Lemma 9.19](https://web.math.princeton.edu/~rvan/tuniv240625.pdf#page=78).
Indeed \(\mathbb E H=0\), \(\mathbb E H^2=(1-1/N)I\), and the independent summands indexed by unordered pairs have norm \(O_K(N^{-1/2})\).
The entry covariance is block diagonal on unordered pairs; each positive two-coordinate block has trace \(2/N\), so \(v(H)^2=\|\mathrm{Cov}(H)\|\le2/N\).
These estimates meet both logarithmic size conditions of Theorem 9.17.
Lemma 9.19 and the concluding spectral inclusion in the proof of Theorem 9.17 (manuscript pp. 79–80) give confinement for each fixed selfadjoint matrix pencil to any neighborhood of its free spectrum.
Apply this to the Hermitian dilation with coefficients \(\left(\begin{smallmatrix}0&A_j\\A_j^*&0\end{smallmatrix}\right)\), including the constant coefficient.
The eigenvalues of the dilation are the signed singular values, so at fixed \(K\) the singular values of the truncated pencil lie in \([3\gamma/4,\|L\|+1]\) with probability tending to one.

The passage back to the original inputs is where the fourth moment enters.
Write \(r_K=\xi-u_K\), and let \(U\) be the strictly upper triangular matrix with independent copies of \(r_K/\sqrt N\) above the diagonal.
Apply [Latała, author manuscript, Theorem 2, p. 2](https://www.mimuw.edu.pl/~rlatala/papers/randmatrPAMS05.pdf#page=2) separately to the real and imaginary parts of \(U\).
For each part, the largest row and column sums of variances are at most \(\|r_K\|_2^2\), and the sum of fourth moments is at most \(\|r_K\|_4^4\).
Consequently \(\sup_N\mathbb E\|U+U^*\|\le C(\|r_K\|_2+\|r_K\|_4)\to0\).
Independence between the two parts is unnecessary for the triangle inequality.
For the diagonal, \(\mathbb P(\max_{i\le N}|\zeta_i|>\epsilon\sqrt N)\le N\mathbb P(|\zeta|>\epsilon\sqrt N)\to0\), since \(t^2\mathbb P(|\zeta|>t)\to0\).
Thus for every fixed \(\epsilon>0\) the probability that the two pencils differ in norm by more than \(\epsilon\) tends to zero in the order \(\lim_{K\to\infty}\limsup_{N\to\infty}\), by the triangle inequality with the fixed weights \(\|A_j\|\).
The external estimates are used at these identified statements and their displayed interfaces; their proofs were not independently audited here.

Take \(\epsilon=\min(\gamma/4,1)\) in the comparison.
Singular-value perturbation then places all original singular values in \([\gamma/2,\|L\|+2]\) with probability tending to one.
Choose a bounded continuous test on \([0,\infty)\) that equals \(\log t\) on this interval.
The established [Hermitized weak limit and upper bound](Yin_L_F0061_v2.md#upper-limit) imply convergence in probability of the unregularized logarithm to its finite free target, and the [marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion) gives the arbitrary-coupling limsup.
For F0014 apply the same argument to the [exact Schur linearization](Yin_L_F0061_v2.md#linearization-transfer): its lower block has a polynomial inverse, so the free pencil is invertible precisely when \(P(s)-z\) is invertible.
The normalization factor is the same on the finite and free sides.

<a id="no-gap"></a>
## Where the moment assumption stops helping

A zero free determinant is already handled by the [finite-variance upper bound](Yin_L_F0061_v2.md#upper-limit).
The remaining determinant question has \(\Delta(L)>0\) but \(0\in\sigma(|L|)\).
Norm approximation does not bound the contribution of a few singular values near zero to the normalized logarithm: even one value \(e^{-N}\) contributes \(-1\) at size \(N\).
The [odd-dimensional commutator](Yin_L_F0061_v1.md#real-affine-obstruction) is exactly singular for every real symmetric input despite a positive free determinant; bounded sign laws have the same obstruction.
This rules out replacing the limsup by a full logarithmic limit at every fixed parameter under a fourth-moment hypothesis.

For the repeated-variable test \(P(x,y)=xy+2yx\), the [one-row reduction](Yin_L_F0066_v19.md#two-sided-quartic-first-obligation) still needs a probability estimate for deficient background rank and for the complete conditional numerator relative to its same-row denominator.
In the [high-corank background example](Yin_L_F0066_v19.md#two-sided-gap-with-singular-column-branch), the masses \(384\,2^{-r}/r\) at absolute value \(\sqrt r\) already give finite moments of every order.
These backgrounds are summably rare; they invalidate that uniform conditional estimate, not the determinant or Brown conjecture.
Testing the negative logarithmic tail with bounded sign inputs would therefore distinguish a structural obstruction from a truncation issue.
More explicitly, choose a fixed \(z\) with finite free logarithm and no gap, write \(\nu_{N,z}\) for the singular-value measure of \(P(W^{(N)})-zI\), and seek a deterministic subsequence \(N_k\) on which, for every \(\eta>0\),
\[
 \lim_{\epsilon\downarrow0}\limsup_{k\to\infty}
 \mathbb P\!\left\{\int_{[0,\epsilon)}|\log t|\,d\nu_{N_k,z}(t)>\eta\right\}=0 .
\]
An exact zero gives infinite tail mass in this formula; otherwise it counts both the size and the number of small singular values.
Together with the existing Hermitized and positive-log controls, this would suffice for the F0014 limsup at that parameter.

For F0012, the [full-sequence planar logarithmic defect](../claims/Yin_C_F0186_v4.md#remaining-defect) remains to be controlled even if every fixed-parameter limsup is known.
Nor can fourth moments alone give an eventual norm bound under every coupling: for a centered symmetric variance-one law with \(\mathbb P(|\xi|>t)\asymp t^{-5}\), the fourth moment is finite, but among \(N(N-1)/2\) entries the probability of exceeding \(M\sqrt N\) is of order \(N^{-1/2}\) for each fixed \(M>0\).
With independent sizes these events recur almost surely by Borel–Cantelli.
That example concerns norm control and does not refute weak convergence of empirical eigenvalue measures.
The proposed fourth-moment stage leaves the three original finite-variance questions and their completion criteria unchanged.
