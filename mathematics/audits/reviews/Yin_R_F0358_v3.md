---
author: Yin
---

# Moving nonreal shifts for the trimmed and ordinary Wigner product determinants

An agent representing Yin inspected the [fixed statement and proof](../../claims/Yin_C_F0351_v3.md#statement) at 2026-11-17T06:38 UTC.
The reviewer received the fixed Claim and the requested scope, worked outside its development, and used the [earlier component-law finding](Yin_R_F0358_v2.md#mixed-components-whole-proof) for the inherited arithmetic and compression estimates.
The initial review had no development dialogue, exploration notes or earlier reviewer conclusions about v3.

<a id="moving-shifts-whole-proof"></a>
## Whole-proof finding

The proof gives convergence at every prescribed deterministic \(z_N\to z\notin\mathbb R\), almost surely for each allowed coupling, with either stated trim under the fourth off-diagonal and second diagonal moments.
Ordinary determinants have the same conclusion when each strict upper law has the specified positive-mass component.
The compact marginal summability and the continuity of \(u\) off the real axis also follow.

Fix \(9/10<a<1\) and use the physical normalization \(N^{-1/2}\) throughout the borders.
At the initial size \(n=\lfloor aN\rfloor\), multiplication by the diagonal scaling on both sides lowers the retained log product by at most \(r_0|\log(n/N)|\).
The free singular measure at \(z/a\) has finite log integral \(u(z/a)/3\), so its mass at zero is zero.
The limiting discarded fraction is \((1-a)/a\), which permits a fixed continuity cutoff with strictly smaller mass.
At the moving canonical shift, weak convergence gives the retained values above this cutoff, and pathwise positive-log control gives convergence of the full clipped log.
Every omitted positive log is bounded by the log of an upper bound on a median because fewer than half the values are omitted.
An upper bound larger than the supremum of the free companion norms over these \(a\) works eventually for each fixed \(a\).
The full clipped sum contributes \(a\,u(z/a)\) to the lower bound at normalization \(1/N\), and the discarded terms cost at most \(3C(1-a)\) in the limit.
The multiplicity of \(\lfloor aN\rfloor\) is at most two, so the fixed-dimension laws apply under each original coupling after splitting the sequence.

The \(j\)-th border adds six to the retained index and three to the ambient dimension.
The old deficit is \(3(m-j)+s_N\) and the final one is \(s_N\).
The conditional estimate in C186v36 uses only the old-minor guards before the failure probabilities are summed over the chain.
Its compact-parameter constants and \(s_N/\log N\to\infty\) give eventual success at the prescribed moving shift.
The normalized sum of the costs is at most \((m/N)(|\log c|+3+3\log(N/m))\), tending to zero as the fixed fraction \(a\) increases to one after the size limit.

For the radial segment of length \(\epsilon|z|\), the average of \(\log^-|tz-w|\) near \(w=z\) is bounded by integrating the disk-intersection fraction \(\min(1,2b/(\epsilon|z|))\) over \(b=e^{-v}\), \(v\ge0\).
Together with the far-region triangle inequality this gives a majorant \(C+\log^-|z-w|\), integrable by finiteness of the compactly supported Brown potential at \(z\).
The averaged potential therefore tends to \(u(z)\).
Upper semicontinuity and the average give deterministic \(a\uparrow1\) with \(u(z/a)\to u(z)\), so only countably many initialization events are needed.
For the upper bound a fixed clip costs at most \(s_N|\log b|/N\) and is Lipschitz in the moving shift.
Sending \(b\) to zero after the size limit gives the same value \(u(z)\).

For each triangular Schur factor, unimodularity gives \(\|\bigwedge^{3N-s_N}F\|=p_{s_N}(F^{-1})\).
This estimate and its inverse bound both directions even when the middle matrix is singular.
On the eventual polynomial norm guard the log cost is \(O(s_N\log N)\).
Appending the unit singular values can replace only positive omitted logarithms of the scalar matrix, with the same cost.
The lower bound rules out more than \(s_N\) zero singular values eventually at the chosen shifts.

For the untrimmed assertion the old minor determines the gap rank before the fresh columns are drawn.
The two frame tests use a union bound on the same flag.
At the later deletions the large coefficient matching is measurable in the minor and previous columns, so its success test can reveal fresh labels and condition on residual values while retaining the required independent regular entries.
The interior perfect matching uses labels of separate entries, and its values remain independent with the component law after the other entries are fixed.
The reverse conditioning in the monic quartic ratios gives total failure \(O(kN^{-d\theta})\) in this last comparison.
Combining the compression inequality before integration with these interior ratios gives the stated product factor \(\min(1,t_{2h+1})^{2h}\), a deterministic \(o(N)\) log cost and a summable error uniform in the individual shift on each enlarged compact neighborhood.
This uses only the fixed-parameter ratios from C186v33.

For fixed \(N\), Fubini removes the intermediate zero denominators on a deterministic full-area parameter set.
For every realization, strict violation of the final product bound is open in the parameter, including at any exact eigenvalue of the full matrix.
Approaching a prescribed point through that full-area set and taking expectations of the lower limit of the violation indicators preserves the marginal bound there.
At \(w=z_N\), the two canonical trims of the old minor have bounded dimension multiplicities, the scale \(n/N\) tends to one, and their normalized logarithms both tend to \(u(z)\).
Their difference bounds \(h\log^-t_{2h+1}/N\) up to \(O(h\log N/N)\).
First Borel--Cantelli gives the determinant lower limit and the locally uniform fixed-regularizer upper estimate gives the upper limit.

Constant-shift convergence in probability lets one choose \(N_j\) so that \(Y_{N_j}(w_j)\) approaches the deterministic \(u(w_j)\) in probability for any \(w_j\to w\).
Moving-shift convergence along the same indices gives \(u(w_j)\to u(w)\).
If the sum of the supremal marginal probabilities diverged, nested finite compact covers and disjoint finite blocks of mass at least one would give a convergent deterministic subsequence of shifts with divergent probability sum.
Independent dimensions preserve those marginals and force infinitely many deviations there, contradicting moving-shift convergence and the continuity just derived.
The probability-one assertions concern prescribed shifts and couplings.
The ordinary determinant conclusion addresses the stated subclass of F0014.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#moving-shifts-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Statement](../../claims/Yin_C_F0351_v3.md#statement) | Both trims, both matrix sizes, ordinary component-law determinants, arbitrary couplings, prescribed shifts, continuity and compact marginal summability. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Argument](../../claims/Yin_C_F0351_v3.md#argument) | Complete proof starting with the fixed-fraction old minor and its canonical scaling and fixed cutoff. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Border sum and radial limit](../../claims/Yin_C_F0351_v3.md#border-cost) | Factorial sum, good radial sequence, upper bound and singular Schur transfer. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Removing the trim](../../claims/Yin_C_F0351_v3.md#fixed-compressions) | Pointwise product bound, extension to prescribed shifts, the two minor trims and the full determinant. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Continuity and summability](../../claims/Yin_C_F0351_v3.md#uniform-marginals) | Sequential continuity and divergent compact subsequence under independent dimensions. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Model and free logarithm](../../claims/Yin_C_F0186_v26.md#statement) | Real laws, moments, independence, normalized free potential and its finiteness at nonzero parameters. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Finite-variance convergence](../../claims/Yin_C_F0186_v4.md#finite-variance-weak) | Fixed-parameter weak semicircular limit for the companion dilation. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Logarithmic statistics](../../claims/Yin_C_F0186_v4.md#log-statistics) | Almost-sure convergence of fixed clips and positive-log tail control. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Regularized potentials](../../claims/Yin_C_F0186_v4.md#regularized-potentials) | Locally uniform fixed regularization for the scalar upper bound. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [One-step estimate](../../claims/Yin_C_F0186_v36.md#one-step) | Three-channel companion, gain of six indices and conditional paired estimate at a prescribed old minor. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Rank guards](../../claims/Yin_C_F0186_v36.md#rank-loss) | Uniform constants on compact sets away from the real axis and summable guarded failure along physical chains. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Canonical scaling](../../claims/Yin_C_F0186_v36.md#initial-product) | Two-sided scaling of the old companion, ordinal singular bounds, determinant and free trace normalization. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Terminal Schur factors](../../claims/Yin_C_F0186_v36.md#final-product) | Unimodular triangular factors, appended unit singular values and norm guards. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Original component conditions](../../claims/Yin_C_F0351_v2.md#statement) | Fixed positive masses and \(Q_{\nu_i}(e^{-t})=O(t^{-d})\) with \(d>1\). |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Exterior minor](../../claims/Yin_C_F0351_v2.md#argument) | Prescribed polylogarithmic exterior size, independent old minor, rank guard and deterministic full-area admissible sections. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Linear overlaps](../../claims/Yin_C_F0351_v2.md#discrete-overlaps) | Adaptive gap and shared-column projected volume estimates. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Later quadratic compressions](../../claims/Yin_C_F0351_v2.md#quadratic-matchings) | Fresh labels, surviving quadratic coefficient and jointly summable fixed-parameter failures. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Interior](../../claims/Yin_C_F0351_v2.md#interior) | Before-integration exterior estimate and quartic ratio transfer for each admissible fixed parameter. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Minor trims](../../claims/Yin_C_F0351_v1.md#minor-trims) | Canonical rescaling, dimension repetitions and control of the intermediate negative logarithm. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Gap estimate](../../claims/Yin_C_F0351_v1.md#adaptive-gap) | Adjacent-ratio loss and the determinant comparison after the first deletions. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Monic ratios](../../claims/Yin_C_F0186_v33.md#argument) | Conditioning on unmatched entries and reverse exposure of the independent matched variables. |
| [Whole-proof finding](#moving-shifts-whole-proof) | [Scalar determinant objective](../../tasks/Yin_T_F0014_v1.md#contract) | Application to the two-color polynomial, component laws and fixed nonreal shifts only. |
