---
author: Yin
---

# Gaussian transpose covariance comparison for matrix-polynomial resolvents

The main scalar GOE Brown and affine determinant conclusions are fixed in [the reviewed C_F0186_v9 theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed), with the retained proof modules and [whole-proof independent finding](../audits/reviews/Yin_R_F0190_v8.md#independent-goe-parity-proof) at their exact scopes.
This continuing Draft retains the distinct optional general-polynomial GOE--GUE covariance comparison, its complete candidate proof, exact source interface and unresolved review scope.
That comparison is not a premise of the reviewed Schultz-based GOE argument.
The arbitrary finite-variance input laws in [F0012](../tasks/Yin_T_F0012_v3.md#contract) remain outside the Gaussian comparison.
The optional comparison itself has not undergone independent mathematical review and has no adopted proved assessment.

<a id="comparison-target"></a>
## Exact comparison target

Fix a selfadjoint matrix-coefficient noncommutative polynomial \(H\) in \(d\) selfadjoint variables, of fixed auxiliary size \(m\).
Let \(X_{\mathrm O}^{(N)}\) be independent normalized GOE inputs with off-diagonal variance \(1/N\) and diagonal variance \(2/N\), and let \(X_{\mathrm U}^{(N)}\) be independent normalized GUE inputs with the standard variance-one semicircular normalization.
For \(w\in\mathbb C^+\), write \(R_X(w)=(wI-H(X))^{-1}\) and normalized trace \(\operatorname{tr}_{mN}=(mN)^{-1}\operatorname{Tr}\).
The candidate bound is
\[
 \left|\mathbb E\operatorname{tr}_{mN}R_{X_{\mathrm O}}(w)
       -\mathbb E\operatorname{tr}_{mN}R_{X_{\mathrm U}}(w)\right|
 \le\frac{C_H}{N}\bigl((\Im w)^{-2}+(\Im w)^{-3}\bigr).
 \tag{Comparison}
\]
For coefficient families bounded on a compact parameter set, the desired constant is uniform on that set.
The direct physical-index contraction, rather than a dimension-free norm bound for each individual entry derivative followed by summation, is the essential point to verify.

<a id="optional-direct-comparison"></a>
## Optional sharper comparison by transpose covariance contraction

This section supplies the complete proposed proof of (Comparison).
It is independent of the Schultz input and is not needed in the reviewed GOE argument.

Let \(O,U\) be independent normalized GOE and GUE tuples, and set \(X_t=\sqrt t\,O+\sqrt{1-t}\,U\).
For one physical matrix use the Hermitian Hilbert--Schmidt basis
\[
 D_i=E_{ii},\qquad
 S_{ij}=(E_{ij}+E_{ji})/\sqrt2,\qquad
 A_{ij}=i(E_{ij}-E_{ji})/\sqrt2,\quad i<j.
\]
The GOE covariance is \(2/N\) on the \(D_i,S_{ij}\) coordinates and zero on the \(A_{ij}\) coordinates.
The GUE covariance is \(1/N\) on all of them.
For a smooth function, Gaussian covariance interpolation therefore differentiates its expectation by
\[
 \frac1{2N}\mathbb E
 \left[\sum_i D_{D_i}^2+
       \sum_{i<j}(D_{S_{ij}}^2-D_{A_{ij}}^2)\right]f(X_t)
 =\frac1{2N}\sum_{i,j}\mathbb E D_{E_{ij}}^2 f(X_t),
 \tag{Covariance-contraction}
\]
summed also over the fixed input index.
On the right the directional derivatives mean the complex-bilinear extension of the polynomial/resolvent derivatives at a Hermitian tuple.
Indeed \(D_{S_{ij}}^2-D_{A_{ij}}^2=D_{E_{ij}}^2+D_{E_{ji}}^2\).
This is the coordinate form of the difference \(N^{-1}\delta_{ik}\delta_{jl}\).

Here is a self-contained justification of the standard Gaussian interpolation step.
Differentiate \(f(\sqrt t\,O+\sqrt{1-t}\,U)\) for \(0<t<1\), condition on the other Gaussian vector, and apply one-dimensional integration by parts \(\mathbb E[g h(g)]=\mathbb E[h'(g)]\) coordinatewise.
The two terms have coefficients \(1/2\) times their respective coordinate variances, producing their covariance difference.
The real and imaginary parts can be treated separately.
For fixed \(\Im w>0\), resolvent derivatives have polynomial Gaussian-coordinate growth, so integration by parts and differentiation under the integral are justified by Gaussian integrability.
Continuity at the endpoints follows from \(|\operatorname{tr}R|\le1/\Im w\).
A checked attribution for this known formula is Bansal--Sinha, ECCC Report 2020/127, Lemmas 2.3--2.4, PDF p. 10; no new external proof is required for this elementary calculation.

Write \(H(X)=\sum_\omega A_\omega\otimes X_\omega\), let \(R=(w-H(X_t))^{-1}\), and put \(\mathcal E_{ij}=I_m\otimes E_{ij}\).
At fixed word positions the first derivative has terms \(B\mathcal E_{ij}C\), and its second derivative has terms \(B\mathcal E_{ij}C\mathcal E_{ij}D\).
The number of terms is fixed, and products of their coefficient norms are bounded by a fixed polynomial in \(1+\max_j\|X_{t,j}\|\).
No such coefficient depends on \(i,j\).
The resolvent differentiation rule is
\[
 D^2R=R(D^2H)R+2R(DH)R(DH)R.
\]
After trace cyclicity each term in the first summand is of the form \(\operatorname{tr}_{mN}(U\mathcal E_{ij}V\mathcal E_{ij})\), with the coefficient norm product costing at most \((\Im w)^{-2}\) times that fixed polynomial.
Each term in the second summand has the same form with three resolvent factors and cost at most \((\Im w)^{-3}\).
For example
\[
 \operatorname{Tr}(R B_1\mathcal E_{ij}C_1R B_2\mathcal E_{ij}C_2R)
 =\operatorname{Tr}(C_2R^2B_1\mathcal E_{ij}C_1RB_2\mathcal E_{ij}).
\]

For arbitrary block matrices \(U,V\in M_m(M_N(\mathbb C))\), physical matrix-unit multiplication gives the exact identity
\[
 \sum_{i,j}\operatorname{tr}_{mN}
      (U\mathcal E_{ij}V\mathcal E_{ij})
 =\frac1{mN}\sum_{a,b=1}^m
       \operatorname{Tr}_N(U_{ab}V_{ba}^T).
 \tag{One-trace-contraction}
\]
It uses \(\sum_{i,j}E_{ij}ME_{ij}=M^T\).
Since \(\|V_{ba}^T\|=\|V_{ba}\|\) and each block norm is bounded by the full operator norm,
\[
 \left|\sum_{i,j}\operatorname{tr}_{mN}
      (U\mathcal E_{ij}V\mathcal E_{ij})\right|
 \le m\|U\|\,\|V\|.
\]
Thus no extra physical dimension remains after summing the derivatives.
The auxiliary factor is fixed.

Uniformly in \(N,t\), the interpolating Gaussian input has operator-norm moments of every fixed order.
For a unit complex \(v\), its real Gaussian quadratic form has variance
\[
 \operatorname{Var}(v^*X_{t,j}v)
 =(1+t|v^Tv|^2)/N\le2/N.
\]
A \(1/4\)-net of the complex unit sphere has size at most \(9^{2N}\), and its maximum absolute quadratic form controls half the Hermitian operator norm.
The scalar Gaussian tail therefore gives
\[
 \mathbb P\{\|X_{t,j}\|>2r\}
 \le2\exp(2N\log9-Nr^2/4).
\]
For a fixed sufficiently large \(r\), and then by integration for every fixed power, this proves the required uniform operator-norm moments.
Therefore (Covariance-contraction), the two resolvent powers, and (One-trace-contraction) imply
\[
 \left|\frac d{dt}\mathbb E\operatorname{tr}_{mN}(w-H(X_t))^{-1}\right|
 \le\frac{C_H}{N}
       \bigl((\Im w)^{-2}+(\Im w)^{-3}\bigr).
\]
Integrating from zero to one proves (Comparison) as a complete candidate deduction.
For a fixed-degree coefficient family bounded on a compact set, the finite word count and coefficient norm bounds are uniform, so the same constant works throughout that set.
This includes \(H=Q_z=(P-z)^*(P-z)\) with \(z\) in a fixed compact disk.
The proof supplies no finite-variance comparison for non-Gaussian Wigner inputs.

Combined with the separately accepted CGP22 GUE--free comparison, this optional bound would give the squared-singular-value estimate
\[
 \mathbb E\nu_N^{Q_z}([0,t])
 \le C\bigl(t^\beta+N^{-1}t^{-2}+N^{-2}t^{-4}\bigr),
\]
at the exact free zero-atom interface.
The more favorable shrinking exponent is not needed for the main Schultz-based GOE proof.

<a id="cgp22-actual-statement"></a>
## Actual GUE comparison and matrix amplification

The selected [CGP22 v1 original](../literature/pdf/CGP22--arxiv-v1.pdf) was read at Corollary 1.3, PDF p. 5, and its short derivation on p. 27.
The corollary takes independent normalized GUE inputs of size \(N\), a free semicircular system, a fixed deterministic auxiliary dimension \(M\), arbitrary deterministic matrices \(Y_j^M\) and their adjoints, and a fixed selfadjoint formal polynomial in these two sets of variables.
For all \(z\notin\mathbb R\) it gives
\[
 \left|\mathbb E G_{P(X^N\otimes I_M,I_N\otimes Y^M)}(z)
   -G_{P(x\otimes I_M,1\otimes Y^M)}(z)\right|
 \le L_P(\|Y^M\|)\frac{M^2}{N^2}
       \left(|\operatorname{Im}z|^{-5}+|\operatorname{Im}z|^{-2}\right).
\]
The trace is normalized by the full product dimension \(NM\).
An arbitrary fixed matrix-coefficient Hermitian polynomial is encoded by using its coefficient matrices and adjoints as deterministic variables, taking a selfadjoint formal representative, and interchanging tensor factors.
This agrees with the [exact fixed input](../claims/Yin_C_F0186_v2.md#logarithmic-tail) and supplies no GOE conclusion by itself.
The theorem's proof is an accepted external input; the selected Laplace-transform derivation of the corollary was inspected, rather than a new audit of the complete paper.
The actual 40-page v1 original is now retained at its existing logical source address.

## Actual source-inspection and continuation limits

The [CGP22 formula and source-proof inspection scope](#cgp22-actual-statement) are retained above at their exact arXiv v1 passages.
The [SS15 source unit](../audits/literature/SS15/Yin_U001.md#ss15-u001) supplies the accepted matrix-polynomial algebraicity/Puiseux and scalar atomlessness interfaces, with their distinct zero-atom and original-proof inspection boundaries.
The optional squared-singular-value consequence uses that actual atom interface and the separately accepted GUE comparison.
The underlying proofs of the accepted external comparison and algebraicity theorems have not been newly audited in full.

The standard interpolation attribution was directly checked in Nikhil Bansal and Makrand Sinha, ECCC Report 2020/127, Lemmas 2.3--2.4 on PDF p. 10, at the [primary PDF](https://eccc.weizmann.ac.il/report/2020/127/download/).
That source is used for attribution of the known Gaussian identity, while the complete derivation used here is given above.
The reviewed Schultz-based proof does not depend on that attribution source.
The [independent GOE finding](../audits/reviews/Yin_R_F0190_v8.md#independent-goe-parity-proof) covers the actual v8/v9 argument and does not review this optional general-polynomial comparison.
No non-Gaussian finite-variance comparison, novelty claim or full literature-coverage assertion follows from this candidate.
