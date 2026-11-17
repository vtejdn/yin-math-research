---
author: Yin
---

# Terminal logarithmic losses for two Wigner laws with regular components

An agent representing Yin performed a separate initial whole-proof review of the [two-component Claim](../../claims/Yin_C_F0351_v2.md#statement) at 2026-11-17T06:28 UTC.
The reviewer received the fixed Claim, dependency locators and requested scope, and took no part in the development of its argument.
The review used the Gaussian predecessor and its existing finding for the inherited interfaces.
No proof-development dialogue, author explanations or earlier finding on the two-component Claim entered the review.

<a id="mixed-components-whole-proof"></a>
## Whole-proof finding

The argument proves almost-sure weak Brown convergence for each coupling of the dimensions and summability of the terminal integral exceedance probabilities for every positive threshold under the stated raw-law assumptions.
A component can have singular continuous law satisfying the displayed concentration bound.
Any positive absolutely continuous part also suffices, since its density restricted to a positive-mass level set with a finite upper bound gives, after normalization, a component with \(Q(a)=O(a)\).

For the old minor, \(M=(n/N)P_n^{\rm can}\), so the canonical parameter is \(Nz/n\) and both the trim and the regularized upper estimate use the original denominator \(N\).
The bounded multiplicities in \(n=N-k\) preserve every-coupling local \(L^1\) convergence of the first trim.
The second trim and the integral of \(h\log^-t_{2h+1}/N\) then follow with the original second-moment norm guard as in C351v1.
The largest eligible gap is selected before drawing the raw columns.
On the gap event its bottom modes have residual bounded by \((N^5+R)N^{-40h}\), which after the change of normalization is eventually less than the fixed residual threshold divided by \(\sqrt n\).
Transposition exchanges the two independent colors, and conjugation exchanges the upper and lower half-plane shifts.
The compact-parameter partial-alphabet exclusion therefore applies to every unit vector in both bottom singular subspaces, including the adaptively selected vectors.

For a fresh real iid column the normalized complex coefficients are deterministic given the past.
Nondegeneracy gives a positive-probability annulus for the difference of two independent raw entries, as required by Nguyen's geometric inverse theorem.
With \(n'=\lfloor n/2\rfloor\) and concentration at least \(n^{-5/4}\), the theorem gives \(O(n^{3/4})\) progression values approximating at least \(n/2\) coefficients.
The Euclidean error on those coordinates is at most \(\sqrt n\,N^{-5}\), and the cardinality is eventually below \(\lfloor n^{9/10}\rfloor\).
This contradicts the exclusion for either frame.
In Gram--Schmidt each scalar projection lower bounds the distance from the current projected column to the span of the preceding ones.
The projected volume floor \(N^{-5r}\) and the ambient column volume upper bound \(N^{2r}\) give the \(N^{-7r}\) overlap for each frame with a joint summable exception \(O(h n^{-5/4}+kN^{-3}+e^{-c n^{1/8}})\).
Their product dominates the exterior-power remainder because \(14r\le28h<40h\).
For \(r=0\) the initial determinant is the full determinant of the minor.

At a later deletion, compressing by a real isometry preserves all \(d'\) singular values of the middle \(d'\)-dimensional congruence in \(K\) when it is embedded back into the coordinate space.
The shifted real symmetric factor has least singular value at least \(\delta\), and the two inverse factors have least singular value \(1/\|T\|\).
A maximal disjoint matching of entries above the chosen threshold has \(l\) edges, with loops allowed.
Removing entries incident to its at most \(2l\) endpoints incurs rank at most \(4l\), and the remaining norm is below the \(d'\)-th singular value.
Thus \(4l\ge d'\).
Fresh independent labels put the regular law on both endpoints of some matched edge except with exponentially small probability, also when \(p_B=1\).
Conditioning on all residual-label values does not change the selected quadratic monomial's leading coefficient.
The coefficient modulus is at least \(c_\delta N^{-12}\), so the degree-two product sublevel bound at logarithmic scale \(T_N\) controls the event that the unnormalized numerator falls below \(e^{-2T_N}\).
It uses only the component's first absolute moment and its specified concentration tail.
The denominator is at most \(N^4\) on the column guard.
Zero projections are included among the failed tests.

In the interior, exposing the labels before selecting the perfect matching retains independent regular entries there.
The Gram factor is controlled at the original cross-block normalization.
The repeated interior has leading coefficient \(N^{-k}\) in the joint monomial of fourth powers.
Atomlessness permits the reverse conditioning on successive leading coefficients, and a monic quartic at a fresh real draw has lower log tail at height \(T_N\) bounded by \(4Q_{\nu_A}(e^{-T_N/4})\).
This is the pointwise ratio estimate in C186v33, which does not require the stronger concentration integral used by its subsequent disk martingale.
The costs \(O(kT_N+k\log N+h^3\log N)\) are \(o(N)\).
The polynomial exceptions from the two label arguments have summable total bound \(O(kN^{-d\theta})\), where \(1/d<\theta<1\).

Fixed-size characteristic polynomials have finite zero sets, so removing singular intermediate denominators costs zero planar area almost surely.
Fubini gives summable expected exceptional areas on each disk outside each fixed real strip, and these areas tend to zero almost surely under arbitrary cross-size coupling.
The original and compressed normalized negative logarithms have a uniform deterministic local square-integral bound by translation of the negative logarithmic kernel and Jensen's inequality.
This controls discarded areas and the real strips as their width tends to zero, while the two-trim inequality controls the integrated lower deficit on the good sets.
Taking the regularizer down to zero after the local uniform limit controls the integrated upper overshoot.
Local \(L^1\) convergence thus gives convergence against smooth compactly supported tests by the distributional Laplacian, and the Brown limit has total mass one.
C186v36 then yields complete convergence for the original marginal laws at positive rational thresholds and hence at any real threshold \(v>0\) by using a smaller positive rational.
The geometric inverse theorem is used at its recorded statement and applicability depth.
The proof does not establish these conclusions for arbitrary pairs of fully atomic strict upper laws.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Two-component finding](#mixed-components-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Two-component finding](#mixed-components-whole-proof) | [Statement](../../claims/Yin_C_F0351_v2.md#statement) | Concentration hypothesis for each positive component, raw and diagonal moments, almost-sure every-coupling weak limit and global terminal series for every positive threshold. |
| [Two-component finding](#mixed-components-whole-proof) | [Argument](../../claims/Yin_C_F0351_v2.md#argument) | Complete chain from the independent minor to the every-coupling local potential limit and the original marginal series. |
| [Two-component finding](#mixed-components-whole-proof) | [First columns](../../claims/Yin_C_F0351_v2.md#discrete-overlaps) | Quantitative exclusion for both frames, inverse theorem and complementary volumes of the common real flag. |
| [Two-component finding](#mixed-components-whole-proof) | [Later columns](../../claims/Yin_C_F0351_v2.md#quadratic-matchings) | Full-rank symmetric congruence, large disjoint coordinate matching, label conditioning and normalized small-ball estimate. |
| [Two-component finding](#mixed-components-whole-proof) | [Interior and planar passage](../../claims/Yin_C_F0351_v2.md#interior) | Label-matched quartic ratios, determinant transfer, summable exceptions, disk integrals, weak limit and terminal conclusion. |
| [Two-component finding](#mixed-components-whole-proof) | [Original model](../../claims/Yin_C_F0186_v26.md#statement) | Within-size independence, raw scaling, fixed laws and moments of both colors. |
| [Two-component finding](#mixed-components-whole-proof) | [Two minor trims](../../claims/Yin_C_F0351_v1.md#minor-trims) | Dilation, repeated minor dimensions, comparison of trims and integrable intermediate logarithm. |
| [Two-component finding](#mixed-components-whole-proof) | [Adaptive exterior power](../../claims/Yin_C_F0351_v1.md#adaptive-gap) | Adjacent ratios, unitary complementary minors and second singular value of the exterior power. |
| [Two-component finding](#mixed-components-whole-proof) | [Cofactor identity](../../claims/Yin_C_F0351_v1.md#later-hyperplanes) | Real hyperplane compression determinant and transpose-symmetric inverse congruence. |
| [Two-component finding](#mixed-components-whole-proof) | [Planar transfer](../../claims/Yin_C_F0351_v1.md#planar-transfer) | Uniform negative logarithmic square bound and shrinking-strip argument. |
| [Two-component finding](#mixed-components-whole-proof) | [Partial-alphabet exclusion](../../claims/Yin_C_F0196_v3.md#statement) | Positive fraction of coordinates and fixed approximation/residual scales for old right and transposed left modes. |
| [Two-component finding](#mixed-components-whole-proof) | [Compact off-axis estimates](../../claims/Yin_C_F0186_v29.md#argument) | Uniform parameters after minor dilation and complex conjugation. |
| [Two-component finding](#mixed-components-whole-proof) | [Nguyen's geometric inverse theorem](../literature/Ngu12a/Yin_U001.md#real-scalar-geometric-inverse) | Independent copies of a nondegenerate real multiplier, two-dimensional unit coefficient array, cardinality and approximation scale. |
| [Two-component finding](#mixed-components-whole-proof) | [Cross-block floor](../../claims/Yin_C_F0196_v4.md#statement) | Full column rank and fixed lower singular-value bound on a prescribed mesoscopic block. |
| [Two-component finding](#mixed-components-whole-proof) | [Degree-two product sublevels](../../claims/Yin_C_F0186_v31.md#product-polynomial-sublevel) | Tail in terms of maximum monomial coefficient, first absolute moment and concentration at an exponential scale. |
| [Two-component finding](#mixed-components-whole-proof) | [Monic interior ratios](../../claims/Yin_C_F0186_v33.md#argument) | Fixed exterior, matching law, exact factorization, Gram factor and conditional tail of each individual monic ratio. |
| [Two-component finding](#mixed-components-whole-proof) | [Factorization](../../claims/Yin_C_F0194_v36.md#fixed-interior-factorization) | Exterior-measurable Schur factor, both Jacobians and size of the matched coefficient. |
| [Two-component finding](#mixed-components-whole-proof) | [Regularized potentials](../../claims/Yin_C_F0186_v4.md#regularized-potentials) | Fixed positive regularizer and local uniform almost-sure upper approximation. |
| [Two-component finding](#mixed-components-whole-proof) | [Scalar trim and terminal equivalence](../../claims/Yin_C_F0186_v36.md#statement) | Canonical trim, every-coupling Brown convergence and complete convergence for each integer disk and positive rational threshold. |
