---
author: Yin
---

# Dimension upper limits of determinants and the separation from Brown convergence

This formulation retains the determinant discussion underlying [matrix-pencil F0013](../tasks/Yin_T_F0013_v1.md#contract) and [scalar-polynomial F0014](../tasks/Yin_T_F0014_v1.md#contract).
The [earlier finite-variance frontier](Yin_L_F0061_v1.md) retains its complete source comparisons, moment and parity examples, and actual proof references.
The arguments here explain the target and its limits; they are not Task-completion or independent-review evidence.

<a id="upper-limit"></a>
## Upper semicontinuity and the actual equality target

For matrices \(A_N\) of size \(n_N\), write
\[
 \ell_N=n_N^{-1}\log|\det A_N|,\qquad
 \ell_{N,\delta}=(2n_N)^{-1}\log\det(A_N^*A_N+\delta^2I).
\]
Use ordinary determinants, \(\log0=-\infty\), and normalized traces.
Suppose the fixed-regularizer limits hold almost surely, \(\ell_{N,\delta}\to\ell_\delta\), and \(\ell_\delta\downarrow\ell\) as \(\delta\downarrow0\).
The [finite-variance spectral and logarithmic controls](../claims/Yin_C_F0186_v4.md#argument) provide this regularized interface for the polynomial models at issue.
Intersecting the events for a countable decreasing regularizer sequence, the inequality \(\ell_N\le\ell_{N,\delta}\) gives
\[
 \limsup_N\ell_N\le\ell.
\]
This is the upper-semicontinuity direction, also discussed at the [retained MS24 convention](../audits/literature/MS24/Yin_U001.md#determinant-convention).
The new equality question is whether \(\limsup_N\ell_N=\ell\), not merely whether that automatic upper bound holds.
If \(\ell=-\infty\), the upper bound already gives \(\ell_N\to-\infty\) and determinant roots tending to zero.
For finite \(\ell\), equality requires infinitely many dimensions above \(\ell-\eta\) for every \(\eta>0\); it does not require all sufficiently large dimensions to be above it.

Set \(d_{N,\delta}=\ell_{N,\delta}-\ell_N\ge0\), allowing infinity.
For finite \(\ell\), fixed-regularizer convergence gives
\[
 \liminf_N d_{N,\delta}=\ell_\delta-\limsup_N\ell_N.
\]
Hence the upper-limit equality is equivalent to
\[
 \lim_{\delta\downarrow0}\liminf_N d_{N,\delta}=0.
\]
Full-sequence convergence instead requires the corresponding condition with \(\limsup_N d_{N,\delta}\).
The difference in quantifiers is substantive.
The [real commutator parity obstruction](Yin_L_F0061_v1.md#real-affine-obstruction) invalidates a general full-sequence fixed-parameter assertion, while leaving the upper-limit question open; existence of a good subsequence must still be proved.

<a id="linearization-transfer"></a>
## Exact transfer from a matrix pencil to a scalar polynomial

For each fixed scalar polynomial \(P\) and fixed \(z\), the [word-chain construction](Yin_L_F0058_v2.md#exact-linearization) gives a fixed auxiliary dimension \(m\) and
\[
 L_P(z;x)=A_0-zE_{11}+\sum_j A_jx_j
 =\begin{pmatrix}a_z&B\\C&Q\end{pmatrix},\qquad
 a_z-BQ^{-1}C=P(x)-z,
\]
where \(Q\) is unit upper triangular with a polynomial inverse.
At finite size, its Schur determinant identity gives \(\det L_P(z;W)=\det(P(W)-zI)\).
The [bounded FK multiplicativity interface](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation), applied to the same unit-triangular factors, gives
\[
 \log\Delta_\tau(P(s)-z)
 =m\log\Delta_{\operatorname{tr}_m\otimes\tau}(L_P(z;s)).
\]
Consequently the finite logarithms differ by exactly the same factor \(m\), and taking a dimension limsup preserves that equality.
The matrix-pencil upper-limit theorem is therefore sufficient for the scalar-polynomial upper-limit theorem at each fixed parameter.
No uniformity over all coefficient tuples or all parameters on a single event is required for this implication.
The parameter enters the corner \(E_{11}\), not the full auxiliary identity.
A monic-only theorem covers \(z\ne P(0)\) after deterministic normalization, but does not by itself settle the scalar Task's exceptional fixed parameter.

<a id="brown-nonimplication"></a>
## Pointwise upper limits do not establish a full spectral limit

Let \(J_N\) be the nilpotent shift with ones on the first superdiagonal, and put \(C_N=J_N+E_{N1}\).
Take \(A_N=C_N\) for even \(N\) and \(A_N=J_N\) for odd \(N\).
Both norms are at most one, and their difference has rank one.
For every fixed word in a matrix and its adjoint, telescoping gives a normalized trace difference of order \(1/N\).
The cyclic matrices have the Haar-unitary star-moment limit, so the whole alternating sequence has that same star-moment limit.
Nevertheless,
\[
 N^{-1}\log|\det(A_N-zI)|=
 \begin{cases}
 N^{-1}\log|z^N-1|,&N\text{ even},\\
 \log|z|,&N\text{ odd}.
 \end{cases}
\]
Its limsup is \(\log^+|z|\) for every \(z\), with value zero also at \(z=0\); on the unit circle the odd dimensions give zero and the even values are bounded above by \((\log2)/N\).
This is the logarithmic potential of the uniform unit-circle measure.
The even spectral measures converge to that measure, while the odd spectral measures equal \(\delta_0\).
Thus they do not converge along the full sequence, despite the correct pointwise upper limit everywhere.
This is a counterexample to a general implication, not a Wigner-polynomial counterexample.
The original [F0012 contract](../tasks/Yin_T_F0012_v3.md#contract) still requires full-sequence almost-sure weak convergence, with its [planar defect criterion](../claims/Yin_C_F0186_v4.md#remaining-defect).
