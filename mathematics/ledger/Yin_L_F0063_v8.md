---
author: Yin
---

<a id="polynomial-spread-is-not-diffuse-mass"></a>
# Polynomial coordinate spread does not supply fixed-scale Gaussian smoothing

This ordinary exploration for Yin on 6 November 2026 tests the proposed qualitative smoothing step in the free-gap single-pole branch of [F13](../tasks/Yin_T_F0013_v1.md#contract).
The [actual rectangle consequence](Yin_L_F0063_v4.md#actual-minor-spread) guarantees linearly many physical blocks above a polynomial threshold, but their guaranteed total squared mass may tend to zero.
The distinction matters when the residual Schur error has only an unspecified rate tending to zero.
The following exact original-row calculation rejects an inference from that coordinate-count conclusion alone.
It asserts no actual-minor realization or rectangle good event and is not a Task counterexample.

Take the six real symmetric size-three coefficients
\[
 A_1=E_{11},\quad A_2=E_{22},\quad A_3=E_{33},\quad
 A_4=(E_{12}+E_{21})/\sqrt2,\quad
 A_5=(E_{13}+E_{31})/\sqrt2,\quad
 A_6=(E_{23}+E_{32})/\sqrt2.
\]
They form a basis of the symmetric matrices and have a positive complex-direction frame by the [existing basis argument](Yin_L_F0063_v3.md#positive-frame-physical-boundary).
Let \(n=N-1\), \(b_N=N^{-3/2}\), and
\[
 a_N=\sqrt{1-(n-1)b_N^2},\qquad
 e_1=a_N(1,0,0)^T,\quad
 e_k=b_N(1,0,0)^T\quad(2\le k\le n).
\]
Then \(\sum_k\|e_k\|^2=1\), every block is at least \(N^{-3/2}\), and the mass outside the first block is \(O(N^{-2})\).
Use independent original Rademacher coordinates \(\xi_{j,k}\) and set
\[
 z_N=\sum_{k=1}^n\sum_{j=1}^6\xi_{j,k}A_je_k
     =a_N X_1+b_N\sum_{k=2}^n X_k,
 \qquad
 X_k=(\xi_{1,k},\xi_{4,k}/\sqrt2,\xi_{5,k}/\sqrt2)^T.
\]
Each \(X_k\) has mean zero and deterministic squared norm two.
The remainder \(h_N=b_N\sum_{k=2}^nX_k\) has
\[
 \mathbb E\|h_N\|^2=2(n-1)b_N^2=O(N^{-2}).
\]
Consequently
\[
 \big|\|z_N\|^2-2\big|
 \le 2|a_N^2-1|+2a_N\|X_1\|\|h_N\|+\|h_N\|^2
       =O_{\mathbb P}(N^{-1}).
\]
For every positive sequence \(t_N\to0\) with \(Nt_N\to\infty\), it follows that
\[
 \mathbb P\{|\|z_N\|^2-2|\le t_N\}\longrightarrow1.
\]
In particular, for the definite frozen background \(B=I_3\) and pole \(\lambda=N/2\), the normalized proxy
\[
 (N/\lambda)\det B-z_N^T\operatorname{adj}(B)z_N
       =2-\|z_N\|^2
\]
does not have vanishing small-ball probability at all shrinking windows.
This does not contradict the much finer polynomial-window estimate in L63v4.
It shows why a residual comparison error merely tending to zero cannot be absorbed using the coordinate-count statement alone.

The sufficient additional condition tested in the [conditional smoothing candidate](../claims/Yin_C_F0194_v23.md#diffuse-single-pole-statement) is a minor-measurable set of blocks carrying a fixed positive squared mass while its largest block tends to zero.
The present vectors fail that condition: any set with maximum block tending to zero excludes the first block and has vanishing total mass.
The conditional theorem and its actual-model coverage are separate questions; this calculation has no independent proof review or Claim adoption.
