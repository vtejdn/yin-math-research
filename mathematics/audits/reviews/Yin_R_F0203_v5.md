---
author: Yin
---

# Conditional moments of the exterior determinant and its singular directions

<a id="independent-border-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-13T03:54 UTC a separately assigned agent acting for Yin reviewed the fixed [C196v5 candidate](../../claims/Yin_C_F0196_v5.md#decision-independent-border-candidate).
The reviewer took no part in its development and received the artifact and review scope without development dialogue or proposer explanations.
The reviewer read the earlier R203v4 finding about the different exterior map in C196v4 and checked the present argument directly.
The complete candidate proves the conditional moments, the additional unweighted symmetric-law identity, and the simultaneous left and right preprojection estimates with the stated exceptional area and loss.
The proof leaves the final projection of an adaptively chosen image uncontrolled and supplies no negative-logarithm estimate for the compressed determinant.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Border and singular subspaces](#independent-border-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Border and singular subspaces](#independent-border-whole-proof) | [Candidate decision](../../claims/Yin_C_F0196_v5.md#decision-independent-border-candidate) | Original-law candidate with the additional symmetry condition for the unweighted mean. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Statement](../../claims/Yin_C_F0196_v5.md#statement) | All polynomial identities, singular and distance estimates, exceptional probabilities, and the summable loss claim. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Complete proof](../../claims/Yin_C_F0196_v5.md#argument) | Compression and successive determinant expansions, conditional averaging, restricted tests, planar deletion and the original loss. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Wigner model and observation map](../../claims/Yin_C_F0196_v4.md#statement) | Fixed entry laws, deterministic cut, and kernel of the observation map. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Exterior compression](../../drafts/Yin_D_F0042.md#repeated-interior) | Definition of the operator on the observation kernel. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Fixed exterior factorization](../../claims/Yin_C_F0194_v36.md#fixed-interior-factorization) | The identical algebraic derivation originally inspected in D42, reproduced at its fixed Claim location. |
| [Border and singular subspaces](#independent-border-whole-proof) | [KM15 source unit](../literature/KM15/Yin_U001.md#km15-u001) | Theorem 1.4 on isotropic iid real rows, its normalization, aspect ratio and conditional application. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Sparse truncation](../../claims/Yin_C_F0198_v1.md#sparse-truncation) | Finite-moment model, uniform truncated norms, marked-coordinate count and rank comparison. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Loss definition](../../claims/Yin_C_F0186_v27.md#clipping-definition) | Normalized nonnegative original-matrix excess with the finite-eigenvalue convention. |
| [Border and singular subspaces](#independent-border-whole-proof) | [Arbitrary-set envelope](../../claims/Yin_C_F0186_v29.md#argument) | Uniform original-law upper event, translated logarithms and measurable-set bound. |

## Border algebra and both averages

For \(h_I=0\) the second observation is \(V^Th_J\).
In the \(JJ\) block the two cross terms are \(A_{JI}V^T\) and \(2V A_{IJ}\), killed respectively on the input and output sides of the compression.
All crossing coordinates belong to distinct off-diagonal independent pairs and are independent of both square blocks.
In a real frame for the span of the first \(l\) border columns and its complement, expansion along the border gives the square of the border volume, the complementary principal minor, and the sign \((-1)^l\).
A column dependence annihilates the bordered determinant for every \(z\), including all subsequent borders.
On preceding full rank the new perpendicular component \(y\) multiplies the Gram determinant by \(\|y\|^2\), while the complementary cofactor is \(y^T\operatorname{adj}(D_{l-1})y/\|y\|^2\) for \(y\ne0\).
This proves the quadratic form identity with the ordinary transpose for complex \(D\), including singular \(D\) and, by direct substitution, \(y=0\).

The derivative of the preceding determinant gives \(-\operatorname{Tr}T_{l-1}\) because the Gram factor is independent of \(z\) and the derivative of the compressed matrix is minus its identity.
In the centered quadratic form the terms with two distinct indices enter as \(2S_{ij}\xi_i\xi_j\) for \(i<j\).
Two different pairs leave a singleton of mean zero in their product, as does the product of a pair with a centered diagonal term, even if they share an index.
Different diagonal terms are orthogonal by independence, and each diagonal term contributes \(|S_{ii}|^2(\mathbb E\xi^4-1)\).
After conjugation in the second factor this gives \(4\sum_{i<j}|S_{ij}|^2=2\sum_{i\ne j}|S_{ij}|^2\) for the raw off-diagonal contribution.
All coefficient integrability needed for iterating the derivative is over the border columns with the square blocks fixed.
Each column occurs with degree at most two, so the finite fourth moment suffices even for conditional second moments.

Under the additional symmetry, row signs and permutations preserve both the border law and the full-rank event.
The top exterior projection of the kernel has rank one.
For two distinct coordinate \((m-k)\)-subsets a sign change in their symmetric difference negates the corresponding off-diagonal matrix entry of its expectation.
Permutations equate every diagonal entry, so the expected projection is the identity divided by \(\binom{m}{k}\).
Tracing its product with \(\bigwedge^{m-k}D\) yields the normalized sum of complementary principal minors.
The sum of the minors before normalization is \([w^k]Q_0(z-w)=(-1)^kQ_0^{(k)}(z)/k!\).
This checks the falling-factorial denominator \(k!\binom{m}{k}\) for the unweighted full-rank mean, separately from the \(N^{-k}\) factor in the unconditional Gram-weighted border mean.

## Rectangular tests, area and loss

For fixed square blocks and parameter, project the independent raw border vectors onto a real orthonormal frame for the span of real and imaginary parts of the specified singular subspace.
The resulting rows are independent copies with second moment matrix \(I_p\), where \(p\le2r\).
Every unit real linear form has second moment one and fourth moment at most \(M_4=\max(3,\mathbb E\xi^4)\), hence first absolute moment at least \(M_4^{-1/2}\) by Hölder.
I checked the row normalization on printed page 1 and Theorem 1.4 on printed page 5 of the [arXiv v1 original](https://arxiv.org/pdf/1312.3580v1).
With \(\kappa\) small enough, \(r\le\kappa k\) ensures the required \(k\ge c_1p\).
The source divides each row by \(\sqrt k\), giving the factor \(\sqrt{k/N}\) for the actual border.
The bounds for the real and imaginary parts add in squared norm for each complex vector since \(V\) is real.
The left and right tests share the border, and the two-test failure bound uses only a union bound.
The source theorem is used as an accepted result at this interface.

The truncation exponents give \(4\delta+\eta=3/8\) and \(2\delta=1/8\).
Each altered coordinate pair contributes at most two to its principal-block perturbation rank, and each input occurs twice in the product difference.
Together with the truncated norm bound this leaves at most \(4N^{3/8}\) singular values above a constant on the disk.
The squared Hilbert--Schmidt expectation \(O(N)\) gives the original norm cap \(N^2\) with \(O(N^{-3})\) failure, so the exceptional singular values cost \(O_R(N^{3/8}\log N)\) in the positive-log sum.
The determinant identity bounds the negative-log sum by the positive-log sum plus one translated negative logarithm for each eigenvalue counted algebraically away from the finite eigenvalue set.
The full-plane integral of each translated term is \(\pi/2\).
Each of more than \(\kappa k\) small singular values costs at least \(d\log N\), yielding the claimed area bound.
The restricted tests and dimension conditions are jointly Borel by the spectral projections and the positive semidefinite matrix test on their ranges.
Fubini on the original law followed by Markov at area \(N^{-1}\) costs \(4\pi R^2N e^{-c k}\) for the remaining failure set.
The norm and truncation events enter only after the fixed-parameter conditional estimates.

For a unit \(h\in K\), cancellation of the two projected parts under \(V^T\) gives \(\sigma\|P_Eh\|\le\|V\|\|(1-P_E)h\|\).
The orthogonal singular decomposition yields each preprojection floor, and \(\operatorname{dist}(Dh/\|Dh\|,\operatorname{ran}V)=\|P_KDh\|/\|Dh\|\) yields the stated consequence, likewise for \(D^*\).
The arbitrary-set loss envelope applies simultaneously to the random deletion because it bounds every measurable subset on one original-matrix event.
For area \(a=O(1/\log N)\) its \(O_R(a)+a\log(\pi/a)/2\) bound tends to zero, and the union of exceptional marginal probabilities is summable.
Positivity permits restriction to the structured-event complement, and first Borel--Cantelli permits arbitrary dependence across sizes.
I used the adopted truncation and loss-envelope estimates at the stated interfaces without independently auditing their underlying published concentration results.
