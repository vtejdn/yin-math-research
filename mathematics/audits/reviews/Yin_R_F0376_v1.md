---
author: Yin
---

# Ordinary Wigner log determinants under inverse logarithmic concentration

<a id="log-concentration-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-18T11:35 an agent acting for Yin completed an independent review of C368v1 and the complete quantile-grid argument in L61v5.
The reviewer received the fixed mathematical inputs and requested scope and had no role in developing either argument.
The reviewer formed the findings below from the statements, proofs and identified source before consulting the earlier independent findings on the reused pencil and planar estimates.
The proof establishes the matrix and scalar determinant assertions and the almost-sure Brown limit for the declared independent-coordinate models, including the dimension-zero example.

### The quantile grid and the affine slices

For each atomless marginal the continuous distribution function sends its left quantile at rank \(v\in(0,1)\) to \(v\).
The quantiles at distinct ranks are distinct, and the pushforward of Lebesgue measure by the quantile is the marginal law.
Thus all open marginal cells, including the two tails, have mass at most \(1/K\).
The expected number of threshold points between two fixed endpoints is \(K\) times the marginal mass between them, even in the presence of gaps in the support.
Endpoint hits have probability zero.
Fix each point of the closed tube and a nearest zero.
A union bound gives probability at least \(1-Kkq(r)\) of keeping both in one open box.
The intersection event is measurable jointly in the grid and point because a fixed countable dense subset of the zero set detects every open box that meets it.

A zero and a positive value occur in each box meeting the nonempty zero set.
A line segment in that box therefore meets every sufficiently small positive level.
There are only finitely many boxes and coordinate slices, so one such level \(\delta\) works in all boxes and avoids the critical values on every positive-dimensional slice and all vertex values. [Sard's scalar regular-value theorem](../literature/Sar42/Yin_U001.md#scalar-regular-values)
On an affine slice \(S\), regularity on \(S\cap H\) makes the differential of \(F\) nonzero on its tangent directions wherever \(F=\delta\).
Consequently the further coordinate hyperplane \(H\) cuts the level in \(S\) transversely there.
Constant restrictions yield empty levels.

For a closed transverse cut of a connected smooth manifold by a single coordinate, the two adjacent complementary regions are locally constant along each component of the cut, labeled by the sign of the coordinate difference.
The graph of regions is connected because a path between any two regions can be made transverse relative to its endpoints and then crosses only finitely many times by compactness of its parameter interval.
Thus deleting the cut adds at most its number of components.
Closedness here is relative to the open manifold after preceding hyperplanes have been deleted, so the same argument bounds the additional regions there.
Iteration on the last plane counts each subset of compatible coordinate planes exactly once.
Every component of the level off the planes lies in one open box.

Milnor's Theorem 2 uses ordinary Čech cohomology over a field and applies to real affine varieties in \(\mathbb R^l\).
I checked the printed statement and its proof through the passage to the entire affine variety on pp. 275–278.
In the compact smooth hypersurface estimate, a generic height is Morse and the transverse polar equations bound its number of critical points by the product of their degrees.
For the affine theorem the regular compact neighborhoods defined by the squared equations and a small radial quadratic term have boundary degree at most \(2D\).
Alexander duality halves the boundary Betti sum, nested neighborhoods give the bound on each closed ball, and compact subpolyhedra detect the homology of the full variety. [Milnor, *On the Betti numbers of real varieties*](https://www.math.uchicago.edu/~shmuel/QuantCourse%20/Milnor%2C%20betti%20numbers%20of%20real%20varieties.pdf)
Applied to the one equation on \(S\), its zeroth Betti number bounds the number of components by \(D(2D-1)^{l-1}\), including unbounded components.
Since vertices miss the level, summation over codimensions gives at most \(\sum_{j<k}\binom kj K^j(2D)^{k-j}=(K+2D)^k-K^k\) occupied boxes.
Each box has probability at most \(K^{-k}\) by coordinate independence.
For \(8Dk^2q(r)\le1\) the specified choice of \(K\) gives \(Kkq(r)\le1/2\) and \(2Dk/K\le8Dk^2q(r)\).
Averaging and using \(e^t-1\le2t\) for \(0\le t\le1\) yields \(32Dk^2q(r)\).
The trivial probability bound covers the remaining range, and an empty zero set gives zero.

### From the tube to the three limits

Finite free logarithm gives the two-moment singular-count estimate on the polynomial window for each fixed matrix coefficient tuple.
Changing one of the \(O(N)\) independent upper-row groups changes the singular count by \(O_m(1/N)\), by Hermitian dilation and the rank inequality.
Because \(s<\gamma\beta\) and \(2s<1\), deviations above \(N^{-s}\) have the stated summable tail.
The polynomially clipped logarithm tends to the free value with only the two-moment hypotheses. [Earlier finite-variance proof review](Yin_R_F0190_v39.md#final-affine-whole-proof)

On a good dimension the raw coordinates parametrize the prescribed real symmetric and Hermitian spaces surjectively, including after orthogonal changes in each planar upper entry.
The squared determinant is therefore a nonzero real polynomial of degree at most \(2mN\).
The deterministic repair compresses the real and imaginary parts of the approximate kernel and the outgoing columns into dimension bounded in terms of the fixed pencil.
Its block correction preserves all input symmetries, and an empty compressed zero set excludes that type on the guard for small \(\varepsilon\).
Its Hilbert--Schmidt bound converts to the raw coordinate bound \(C\sqrt N\,\varepsilon^\kappa\), including the fixed rotations.
Only the deterministic part of the earlier repair is needed here. [Earlier review of the deterministic repair](Yin_R_F0190_v37.md#translation-smoothing-whole-proof)

All raw coordinate laws are atomless by (1), and finitely many fixed coordinate types allow a common \(C_A\).
The expected squared Frobenius norms total \(O(N)\).
At \(\varepsilon=e^{-N^\eta}\) the guard thus costs \(O(Ne^{-2\theta N^\eta})\), and the tube costs \(O_A(N^{5-A\eta})\), since \(Dk^2=O(N^5)\).
The latter is summable precisely in the stated sufficient range \(A\eta>6\) for this estimate.
With \(0<\eta<s\), the excess per singular value below the polynomial cutoff is at most \(N^\eta\) off the least-value exception, and at most an \(N^{-s}\) fraction contributes.
First Borel–Cantelli proves almost-sure convergence through all good sizes for each allowed coupling.

A finite target supplies witnesses in every sufficiently large even dimension by simultaneous realification of \(H\) and \(\overline H\) with both pencil evaluations invertible.
The unitary in this realification acts on the physical factor, so arbitrary fixed complex coefficients, including the constant, are retained.
A bad size has identically zero determinant.
Conversely any witness rules out factorization through fewer than \(m\) columns, and the free full-pencil power estimate at zero background gives a finite free logarithm.
At a target of \(-\infty\), monotone fixed lower clips give the requisite upper bound on the full sequence.

The unit triangular word-chain pivot yields equality of the unnormalized finite determinants and a factor \(m\) in both normalized log identities.
The nonconstant scalar target is finite at every prescribed \(z\), including \(P(0)\), by the scalar atomlessness and logarithmic integrability input.
For \(z\ne P(0)\), the zero tuple witnesses every dimension.
Joint measurability of the finite potentials allows Fubini on each disk, giving one probability-one event of area-almost-everywhere convergence for each fixed polynomial and coupling.
The pathwise local square bound gives uniform integrability on every disk and hence local \(L^1\) convergence.
The distributional Laplacian and tightness give weak convergence against all bounded continuous tests on that event. [Earlier review of the planar bounds](Yin_R_F0190_v4.md#finite-variance-controls)

For the example, the minimum gap between level-\(j\) intervals is at least \(\ell_j\).
At \(\ell_{j+1}<r\le\ell_j\), the product \(Q(r)(1+\log(1/r))^A\) is bounded by \(2^{1-j}(1+(j+1)^2\log 3)^A\), uniformly in \(j\) for every fixed \(A\).
At \(r=\ell_j\), the lower bound \(2^{-j}\) excludes every positive power of \(r\), while the level covers give zero Hausdorff dimension.
Centering and variance normalization rescale distances by a nonzero constant and preserve these properties.
Constant polynomials satisfy both scalar conclusions directly.
The general Task contracts also admit atoms and dependent planar coordinates, which are outside the present proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole proof](#log-concentration-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole proof](#log-concentration-whole-proof) | [Matrix and scalar limits](../../claims/Yin_C_F0368_v1.md#statement) | Exact coordinate laws, fixed coefficients and shifts, dimension limsup and pathwise weak limit. |
| [Whole proof](#log-concentration-whole-proof) | [Complete argument](../../claims/Yin_C_F0368_v1.md#argument) | Count, floor, loss on good sizes, scalar and planar conclusions. |
| [Whole proof](#log-concentration-whole-proof) | [Dimension-zero law](../../claims/Yin_C_F0368_v1.md#example) | Upper bounds at every inverse logarithmic power and failure of every positive power law. |
| [Whole proof](#log-concentration-whole-proof) | [Quantile-grid tube](../../ledger/Yin_L_F0061_v5.md#tube) | General independent atomless marginals, boundary, measurability and probability estimate. |
| [Whole proof](#log-concentration-whole-proof) | [Grid box count](../../ledger/Yin_L_F0061_v5.md#box-count) | Regularization, transverse cuts, Milnor bound and dimension dependence. |
| [Whole proof](#log-concentration-whole-proof) | [Finite-variance count](../../claims/Yin_C_F0186_v40.md#statement) | Fixed affine coefficients, positive polynomial window and second moments. |
| [Whole proof](#log-concentration-whole-proof) | [Clipped determinant](../../claims/Yin_C_F0186_v40.md#determinant) | Almost-sure convergence with the polynomial cutoff under second moments. |
| [Whole proof](#log-concentration-whole-proof) | [Structured repair](../../claims/Yin_C_F0186_v38.md#argument) | Guarded deterministic distance, empty types and mixed symmetries. |
| [Whole proof](#log-concentration-whole-proof) | [Witness dimensions](../../claims/Yin_C_F0186_v38.md#log-assembly) | Finite-target even witnesses and full-sequence upper bound at a negative infinite target. |
| [Whole proof](#log-concentration-whole-proof) | [Realification](../../claims/Yin_C_F0186_v9.md#all-even-witness) | The physical change of basis preserves the coefficient matrices. |
| [Whole proof](#log-concentration-whole-proof) | [Free full-pencil estimate](../../claims/Yin_C_F0352_v1.md#statement) | At zero background, a full fixed pencil has finite free logarithm. |
| [Whole proof](#log-concentration-whole-proof) | [Scalar transfer](../../claims/Yin_C_F0186_v40.md#scalar) | Identical finite and free normalization factors and witnesses away from \(P(0)\). |
| [Whole proof](#log-concentration-whole-proof) | [Scalar integrability](../../claims/Yin_C_F0186_v38.md#polynomial-consequences) | Nonconstant polynomials and all fixed shifts. |
| [Whole proof](#log-concentration-whole-proof) | [Word-chain identity](../../ledger/Yin_L_F0061_v2.md#linearization-transfer) | Unit pivot and equality of the two witness sets. |
| [Whole proof](#log-concentration-whole-proof) | [Row concentration](../../claims/Yin_C_F0186_v4.md#row-concentration) | Summable upper-count deviations without cross-size independence. |
| [Whole proof](#log-concentration-whole-proof) | [Planar control](../../claims/Yin_C_F0186_v4.md#noncompact-planar) | Local square bounds and tightness under the finite-variance model. |
