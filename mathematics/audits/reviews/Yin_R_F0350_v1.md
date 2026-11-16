---
author: Yin
---

# Whole-proof review of the normal canonical-domain and fraction theorem

## Finding

On 2026-11-16T19:53 UTC an independent agent acting for Yin reviewed the fixed candidate, its entire argument and each direct input in the table below.
The reviewer took no part in developing the proof and received the fixed Claim and its specified scope without development dialogue, exploration notes or a proposed verdict.
The initial inspection used the cited mathematical arguments and the source statement of ACSY24 Proposition 3.5.
The finding supports the full statement of C_F0346 v1, including its absolute estimates, the original closed operators and both fraction criteria.
It covers the normal-tuples result and its dependencies at the points of use.
The other objectives of F0011 and a new proof audit of all the dependencies are outside this finding.

### The signed estimate

Fix the test \(u\) throughout the cell computation.
In the uncentered square inequality take \(v=k\pm N^{3/4}1_R\), with \(R\) one of \(N\) pieces of cell \(l\) of mass \(t_l/N\).
The denominator in either sign divided by \(t_lN^{1/2}\) tends to one uniformly, and the increment to \(\tau k\) has magnitude \(t_lN^{-1/4}\).
In the sign average of \(\int v(z)^2v(w)^2d\nu\), all terms with both endpoints in \(R\) vanish because \(\nu(R^2)=0\).
After averaging the pieces and dividing by \(t_lN^{1/2}\), the two one-endpoint terms give \(2\int k(z)^2 1_l(w)d\nu/t_l\), using \(\zeta=\zeta^*\) for symmetry.
This averaged normalized numerator stays bounded, justifying the uniform replacement of the denominators even for uneven spectral row masses.
The additional diagonal pairing on the left is nonnegative by the projection identity on \(R\).
These calculations give (2) for the full real coefficient space, including vectors supported across both parts of \(Q\).

Center the values of \(p\) in the probability weights \(t_i/m\).
The uncompressed \(r_l\) annihilates \(t\), as does \(b_l\) by centering.
At unequal entries the sum of the \(r_l\) products is \(2v_0-(p_i^2+v_0)-(p_j^2+v_0)\), and the \(b_l\) products add \(2p_ip_j\).
This determines the full Laplacian since each \(t_i>0\).
Compressing each vector now costs the cross-edge term (3), with each edge from \(B\) to \(Q\setminus B\) counted once.
Away from the pivot, \(p_l^2+v_0+2p_i^2\le4\operatorname{osc}_Q(p)^2\), and the pivot is multiplied by \(\nu_{ll}=0\).
Pairing the positive summands with (2), and using the nonnegative diagonal of \(F\) against \(W+L\), gives the lower bound (1) with \(8\nu(B\times Q)/m\) times the squared oscillation.
Quantization gives uniform simple approximations, and inserting the resulting bounded kernels at a fixed analytic test commutes with that limit.
Null cells contribute zero to the spectral actions.
This argument uses no lower bound on a nonzero cell mass.

For a pair \(z\in B,w\in3B\), integrating admissible centers and radii costs at most \(\pi\int_{|z-w|/4}^\infty r^{-3}dr\).
On the scalar cross term the factor \(|h_v(z)-h_v(w)|^2=|z-w|^2\kappa(z,w,v)^2\) cancels the resulting inverse squared distance.
On the other term the angular oscillation integral costs \(CT(B)\), and \(T(B)\le K\mu(3B)\) cancels the mass denominator.
This leaves the inverse-gap integral of the liberation measure, whose diagonal is null.
The complementary disks satisfy the unconditional small-local-mass estimate for the collected kernel at each disk.
For \(r\) between positive finite cutoffs, Fubini at the fixed test follows from the bounded kernel insertion on the compactly supported marginal and the differentiated power series.
The nonnegative truncated kernels increase to \(g\) after disk normalization.
Jensen's inequality and \(|z-w|\kappa\le2\) bound \(\iint|z-w|^2g^2d\mu^2\) by four times the total squared curvature.
Both generator gaps thus converge in the original coarse norm.
The relative mixed-energy identity has defect \(F_g(u)/2\) subtracted from the vacuum pairing.
Its phase graph approximations concern \(Z,Z^*\) and their scalar divided differences, and multiplication by any omitted coefficient gives the usual Leibniz terms with zero derivative of that coefficient.
Thus the identity needs no actual derivative normalized at the killed projection.
The two signs average to the initial selfadjoint contraction, giving the bound by scaling and linearity, uniformly in the spread model.

### Returning to the original tuple

For each lattice word use the circle model with its actual vacuum of norm at most \(CB_c\).
Its finitely many spectral components satisfy \(e_i\zeta e_i=0\), which supplies the partition used above.
Smooth spectral cutoffs approximate the labels in operator norm and in the derivative graph.
Filtered through the two conditional expectations, the off-label circle average of the inverse difference equals \(1/(c_i-c_j)\) and the equal-label derivative is zero.
Outer bimodularity recovers the discrete derivative on each word, and slicing followed by projection is contractive.
This bounds \(K_{\rm lat}\) without a label or word constant.
The rounding direction \(K_{\rm proj}\le C K_{\rm lat}\), followed by \(K_{\rm rel}\le2K_{\rm proj}\), carries precisely that uniform cost to all finite killed selfadjoint coefficient families.
No partition is assumed on the original tuple.

The normal commutation relation and the zero product-diagonal projection of a diffuse marginal uniquely fix the starred generator value at each coordinate.
Full ACSY supplies this diffuseness for all omitted coordinates.
Their real and imaginary parts therefore qualify as killed coefficients, including the harmless zero coefficient for one generator.
The flip-adjoint derivative on the adjoint tuple interchanges the two slices and conjugates the vacuum isometrically.
For the original right slice \(E\) the initial core adjoint is \(E^*p=p\xi-((\tau\otimes\mathrm{id})\partial(p^*))^*\).
Uniformly bounded Kaplansky approximants have bounded images under both \(E\) and its core adjoint, and weak graph closure puts each bounded vector in both actual domains.
On the core \(E(X_jp)-X_jEp=\delta_{ij}\tau(p)1\).
The bounded-vector graph limit applies also to \(X_jp\), yielding \([X_j,-\overline E]=\delta_{ij}P_\Omega\).
For a supplied strong system the normal converse constructs the starred derivative, with vacuum \(-D_i^*\Omega+(D_i\Omega)^*\).
All these claims concern the represented starred core.

### Affiliated fractions

The published Proposition 3.5 uses this same starred domain and actual vacuum condition, yielding \(\Delta(X)=d\).
Part A of C_F0068 applies to the unstarred division closure and one bounded regular fraction with a finite-rank solution.
For the canonical system put \(B_i=-D_i\), so that \([B_i,X_j]=\delta_{ij}P_\Omega\).
The graph of \(B_i|_{M\Omega}\) contains the original polynomial graph and is contained in the closed graph of \(B_i\), so the closure used in Part C is exactly \(B_i\).
For every legal \(Q\) its natural domain contains \(M\Omega\).
The adjoint test on bounded vectors \(b^*B_i^*s^*\eta-t^*B_i^*a^*\eta\) extends agreement with a bounded representative to that entire domain.
Conversely finite rank on the natural domain implies finite rank on the bounded vectors, where Part C applies.
For each \(u\), existence of one common fraction for all \(i\) is equivalent to the test at every bounded fraction.
The coordinate ranks are independent of \(Q\), and the boundary solution at fixed \(Q\) is \(-\overline{sD_i b-aD_i t}\).
For a supplied generator-first system the bounded-vector discrepancy is \((sb-at)xD_i^{\rm supplied}\Omega=0\).
The dense common restriction and closability of the two fraction operators identify their bounded finite-rank closures whenever either has finite rank on its natural domain.
No equality of their two natural domains is needed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0346_v1.md#decision-candidate) | Complete candidate and its fixed list of direct inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0346_v1.md#statement) | Original normal tuple, quantitative estimates, domains, two fraction quantifiers and supplied systems. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0346_v1.md#argument) | Full proof from the cell bound to the unstarred division closure. |
| [Finding](#finding) | [Actual vacuum](../../claims/Yin_C_F0238_v1.md#statement) | The commutator at the distinguished coordinate yields a symmetric liberation measure with zero diagonal and the inverse-gap budget. |
| [Finding](#finding) | [Projection square](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | The lower bound vanishes on every zero-cost cell and measurable subcell, for each analytic test. |
| [Finding](#finding) | [Spectral row](../../claims/Yin_C_F0335_v1.md#statement) | The finite-cell row form used here follows from the direct relative spike calculation. |
| [Finding](#finding) | [Uncentered square](../../claims/Yin_C_F0331_v1.md#the-uncentered-square) | The trace term and two-sided spectral numerator have the required normalization for each real marginal spike. |
| [Finding](#finding) | [Disk representation](../../claims/Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Similarity of the overlap integral and the angular identity represent the squared curvature with a positive absolute normalization. |
| [Finding](#finding) | [Scalar curvature](../../claims/Yin_C_F0255_v1.md#statement) | Projection to the diffuse scalar marginal controls its integrated squared curvature. |
| [Finding](#finding) | [Complementary disks](../../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) | The unconditional estimate bounds the integral of the absolute signed collected disk costs on every truncated bad region. |
| [Finding](#finding) | [Matched energy](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap-weighted convergence in both orientations, the sign of the curvature term and use of the relative phase graphs. |
| [Finding](#finding) | [Lattice equivalence](../../claims/Yin_C_F0339_v1.md#statement) | Rounding transfers a uniform lattice cost to the original trace-half projection supremum. |
| [Finding](#finding) | [Circle spread](../../claims/Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | The actual vacuum budget and zero equal-label blocks permit the finite partition estimate. |
| [Finding](#finding) | [Conditional recovery](../../claims/Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Norm and graph approximation of old words and exact conditional means of the inverse gap. |
| [Finding](#finding) | [Projection coefficient theorem](../../claims/Yin_C_F0308_v1.md#statement) | The comparison with all finite selfadjoint coefficient families loses an absolute factor at most two. |
| [Finding](#finding) | [Forced adjoint values](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Full ACSY forces diffuse marginals and fixes both distinguished and omitted starred derivative values. |
| [Finding](#finding) | [Adjoint tuple](../../claims/Yin_C_F0073_v1.md#statement) | Flip-star preserves the vacuum norm and turns the opposite slice into a right slice on the same represented core. |
| [Finding](#finding) | [Two-slice domains](../../claims/Yin_C_F0072_v1.md#statement) | Core adjoint formula and weak graph closedness for the canonical closure and its Hilbert adjoint. |
| [Finding](#finding) | [Generator commutators](../../claims/Yin_C_F0078_v2.md#the-original-canonical-operators) | Bounded approximation extends the original commutators to every bounded vector with the asserted sign. |
| [Finding](#finding) | [Normal converse](../../claims/Yin_C_F0070_v2.md#actual-vacuum-under-the-additional-single-vector-adjoint-condition) | The strong adjoint domain includes the trace vector needed in the exact starred-core converse. |
| [Finding](#finding) | [ACSY24 Proposition 3.5](../literature/ACSY24/Yin_U001.md#acsy24-u001) | The inspected source proposition applies to the entire starred core and gives maximal Delta. |
| [Finding](#finding) | [Maximal-Delta boundary equation](../../claims/Yin_C_F0068_v1.md#statement) | Part A uses one legal fraction and arbitrary bounded finite-rank certificates in the right-multiplication convention. |
| [Finding](#finding) | [Specified realization](../../claims/Yin_C_F0068_v1.md#dual-specializations) | Part C on the original closure, all legal fractions or one common fraction, boundary sign and intrinsic coordinate ranks. |
| [Finding](#finding) | [Canonical compatibility](../../claims/Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) | Cancellation on bounded vectors and equal finite-rank closures for supplied strong systems on their actual individual domains. |
