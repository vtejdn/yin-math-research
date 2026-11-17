---
author: Yin
---

# A two-color Wigner determinant with purely atomic strict upper laws

An agent acting for Yin reviewed the [fixed C351v4 proof](../../claims/Yin_C_F0351_v4.md#statement) at 2026-11-17T06:45 UTC independently of its development.
The reviewer received the fixed claim and the scope of the check, with no proof-development dialogue, author explanation or previous finding on v4.
The review used the [earlier moving-shift review](Yin_R_F0358_v3.md#moving-shifts-whole-proof) and the [two-component review](Yin_R_F0358_v2.md#mixed-components-whole-proof) for inherited estimates, and checked the changed hypotheses and their applications through the planar conclusion.

<a id="fine-atomic-laws-whole-proof"></a>
## Whole-proof finding

The fixed laws and size-dependent representations in C351v4 suffice for the ordinary moving-shift determinant limit, compact summability of the marginal deviations, almost-sure weak Brown convergence under every coupling and the terminal series at the stated trim.
The dyadic example satisfies every hypothesis with two fixed purely atomic laws and arbitrary model diagonals.

At each size one may generate independent labeled entries using the two displayed mixtures and forget their labels to obtain precisely the original matrix-pair law.
Thus a probability bound on a matrix event proved this way holds for its original marginal under every coupling.
The canonical minor, the cross-block rank and norm guards, and the first \(r\) projections use the fixed full laws.
In particular \(r\) depends on the minor and the shift before the flag is sampled, and neither frame needs a bound on the concentration of the conditional component in the first \(r\) draws.

For a later column, the matching in the symmetric quadratic form depends only on the minor and past columns.
Its disjoint members have independent label-success indicators with probabilities \(p_{B,N}^2\) for edges and \(p_{B,N}\) for loops.
Their joint failure has probability at most \(\exp(-p_{B,N}^2(n-k)/4)\), and multiplication by \(k\) preserves summability by the assumed growth of \(p_{B,N}^2N/\log N\).
Substitution of the residual-label values preserves the coefficient \(2K_{ij}\) or \(K_{ii}\) of a surviving edge or loop.
If \(M_f\) is the maximum coefficient modulus, then \(M_f\ge c_\delta N^{-12}\) and \(e^{-2T_N}\le M_f e^{-T_N}\) eventually.
The degree-two sublevel bound holds also at atoms and its constants are uniform by the common first absolute moment bound.
The condition \(T_N/\log N\to\infty\) gives both the required logarithmic threshold and summability of \(kn e^{-cT_N}\).
For the remaining \(k Q_{\nu_{B,N}}(C e^{-cT_N})\) term one may replace \(c\) by \(c/2\).
Each successful step has nonzero numerator and nonzero projection, so the upper bound \(N^4\) on its squared projected length suffices for the determinant lower bound.

For the separate interior, Hall failure on a set of \(s\) left vertices requires all its edges to some \(l-s+1\) right vertices to be absent.
Reflection \(s\mapsto l-s+1\) reduces the union sum to at most twice the sum of \(\exp(2s\log l-psl/2)\) for \(s\le(l+1)/2\).
Since \(pl/\log N\to\infty\), a geometric sum bounded by \(C e^{-pl/4}\) suffices.
The labels alone determine the interior matching, so its selected entries still have independent laws \(\nu_{A,N}\) after all unmatched values are exposed.
The coefficient \(N^{-k}\) of the joint top monomial initializes the reversed quartic recursion.
Whenever all earlier draws in this reverse order have succeeded, the next leading coefficient is nonzero and determined by the past.
Dividing by it gives a monic quartic whose modulus is below \(e^{-T_N}\) only if the draw is within \(e^{-T_N/4}\) of the real part of one of its four roots.
This includes an exact zero and yields a first-failure probability at most \(4l Q_{\nu_{A,N}}(e^{-T_N/4})\).
On the complementary event, multiplication of the successful ratios gives the lower bound \(N^{-k}e^{-lT_N}\).

Consequently the undivided comparison of C351v3 has a summable probability bound uniform in the individual parameter on each compact neighborhood off the real axis.
The deterministic logarithmic costs divided by \(N\) tend to zero since \(q_n^3\log N=o(N)\) and \(kT_N=o(N)\).
For each size, Fubini excludes intermediate spectra for a deterministic full-area set of parameters.
Strict violation of the undivided comparison is open in the parameter for each sample, so Fatou retains the same bound at every prescribed nonreal point.
At a deterministic \(z_N\to z\notin\mathbb R\), both original-minor trims converge at the canonical shift \(Nz_N/n\), since \(n=N-k\) has bounded multiplicities and \(n/N\to1\).
Subtracting their normalized logs controls \(q_n\log^-t_{2q_n+1}/N\), and the regularized upper estimate closes the ordinary determinant limit.
This reasoning uses first Borel--Cantelli and the every-coupling trimmed input.
To get compact marginal summability, a divergent sum of individual near-supremal probabilities would give divergent finite blocks in nested compact sets shrinking to a single point.
Independent dimensions would then have infinitely many deviations along a convergent deterministic subsequence of shifts, contrary to the moving-shift limit and continuity of \(u\).
The resulting assertion takes the supremum of individual probabilities.

For each coupling, Fubini on countably many disks gives almost-sure potential convergence for planar almost every parameter on a single sample event.
The real axis has zero planar area, and the pathwise local square bound supplies uniform integrability on every disk.
The distributional Laplacian of the local \(L^1\) limit identifies the limiting measure, and the pathwise tightness turns this into weak convergence.
The terminal equivalence then applies at every rational positive threshold, hence by monotonicity at every positive threshold.

The unscaled dyadic law is symmetric, bounded and of positive variance, and the countable union of its grids has full mass.
Conditioning on \(j\ge J\) has probability \(1/J\).
An interval of radius \(s\) after the fixed variance rescaling meets at most \(1+C2^j s\) grid points at level \(j\), hence the conditional concentration is at most \(2^{-J}+Cs\).
With the stated \(J_N\), \(2^{-J_N}\le(N+1)^{-6}\), and \(k e^{-c\log^2(N+3)}\) is summable for every \(c>0\).
The two label-growth ratios have orders \(\log N\) and \(N/\log^3 N\), respectively.
The same hypothesis excludes finite support because every positive-mass component on at most \(b\) points has an atom of mass at least \(1/b\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Statement](../../claims/Yin_C_F0351_v4.md#statement) | Fixed original laws, dimension-dependent component hypotheses and all four probabilistic conclusions. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Argument](../../claims/Yin_C_F0351_v4.md#argument) | Whole argument beginning with the unchanged linear tests and the fresh-column quadratic estimates. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Interior](../../claims/Yin_C_F0351_v4.md#atomic-matching) | Varying-density Hall bound and stopped, nonzero-on-success quartic recursion. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Conclusions](../../claims/Yin_C_F0351_v4.md#conclusions) | Moving shifts under each coupling, compact marginal probabilities, planar convergence and terminal series. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Atomic example](../../claims/Yin_C_F0351_v4.md#dyadic-example) | Fixed normalized dyadic law, conditional concentration, scale choices and finite-support obstruction. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Model](../../claims/Yin_C_F0186_v26.md#statement) | Within-size independence, original fourth and diagonal second moments and cross-dimensional coupling. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Rank guard](../../claims/Yin_C_F0196_v4.md#statement) | Cross-block singular-value lower bound outside summable exceptions. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Exterior](../../claims/Yin_C_F0351_v2.md#argument) | Original-law minor, fresh columns, norm guards and choice of gap rank. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [First columns](../../claims/Yin_C_F0351_v2.md#discrete-overlaps) | Both original-law frame tests with summable arithmetic-exclusion failures. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Quadratic form](../../claims/Yin_C_F0351_v2.md#quadratic-matchings) | Real flag, cofactor ratio and disjoint large coefficients before the fresh labels. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Scalar product bound](../../claims/Yin_C_F0186_v31.md#product-polynomial-sublevel) | Degree-two lower-tail bound for product laws with uniformly bounded first absolute moments. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Quartic coefficients](../../claims/Yin_C_F0186_v33.md#argument) | Matching-value independence, degree and top coefficient in the physical normalization. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Exterior-to-interior comparison](../../claims/Yin_C_F0351_v2.md#interior) | Determinant assembly and Gram factor, with both component estimates supplied at their new scales. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Old minor](../../claims/Yin_C_F0351_v1.md#minor-trims) | Bounded multiplicity and two-trim control of the first retained negative logarithm. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Moving trim limits](../../claims/Yin_C_F0351_v3.md#statement) | Each trim at deterministic nonreal limits under all couplings and continuity of the free potential. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Undivided inequality](../../claims/Yin_C_F0351_v3.md#fixed-compressions) | Product factors, extension by continuity, old-minor trim transfer and normalization. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Marginal series](../../claims/Yin_C_F0351_v3.md#uniform-marginals) | Divergent convergent-shift subsequence and independent-dimension converse Borel--Cantelli. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Regularized upper bound](../../claims/Yin_C_F0186_v4.md#regularized-potentials) | Fixed-regularizer upper bound at moving shifts and subsequent removal of regularizer. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Planar controls](../../claims/Yin_C_F0186_v4.md#noncompact-planar) | Pathwise tightness and eventual locally uniform planar square-integral bound for potentials. |
| [Whole-proof finding](#fine-atomic-laws-whole-proof) | [Terminal equivalence](../../claims/Yin_C_F0186_v36.md#statement) | Every-coupling weak Brown convergence implies the terminal deviation series at the specified trim. |
