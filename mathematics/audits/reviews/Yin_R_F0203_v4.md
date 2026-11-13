---
author: Yin
---

# Exterior observation on near-kernels of the two-sided Wigner product

<a id="position-planar-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-13T03:08 an agent acting for Yin independently checked the [C196v4 candidate](../../claims/Yin_C_F0196_v4.md#decision-position-planar-candidate), including its entire statement and proof.
The reviewer received the fixed artifact and review scope, took no part in the derivation, and inspected the proof and its mathematical inputs before consulting any earlier review findings.
The assignment supplied no development dialogue, author explanation or earlier verdict on this proof.

The argument proves both planar bounds, the inverse estimate on the surviving directions and summability of the extreme logarithmic loss on the discarded parameters.
The exceptional probability applies to each prescribed deterministic coordinate set and permits all the stated scales and arbitrary coupling across dimensions.
The inside equations on surviving parameters still require a small-ball estimate for their actual targets.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Exterior observation](#position-planar-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Exterior observation](#position-planar-whole-proof) | [Candidate decision](../../claims/Yin_C_F0196_v4.md#decision-position-planar-candidate) | Original-law candidate with its declared support and limitations. |
| [Exterior observation](#position-planar-whole-proof) | [Exact statement](../../claims/Yin_C_F0196_v4.md#statement) | Both integrated estimates, the threshold count, the area and inverse conclusions, and the complete-convergence statements. |
| [Exterior observation](#position-planar-whole-proof) | [Complete proof](../../claims/Yin_C_F0196_v4.md#argument) | Exterior measurability, determinant, conditional rectangular estimate, positive and negative logarithmic budgets, and loss on the removed sets. |
| [Exterior observation](#position-planar-whole-proof) | [Sparse truncation](../../claims/Yin_C_F0198_v1.md#sparse-truncation) | Model, raw threshold, marked-coordinate count, truncated norm and perturbation ranks. |
| [Exterior observation](#position-planar-whole-proof) | [Affine row bound](../../claims/Yin_C_F0196_v1.md#affine-small-ball) | Fixed-vector tensorization and its uniform application after standardizing the unmarked off-diagonal law. |
| [Exterior observation](#position-planar-whole-proof) | [Planar envelope](../../claims/Yin_C_F0186_v29.md#argument) | Uniform upper tail and arbitrary-set layer integral needed for small-area loss. |
| [Exterior observation](#position-planar-whole-proof) | [Clipping definition](../../claims/Yin_C_F0186_v27.md#clipping-definition) | Original-matrix normalized nonnegative excess, with the finite-eigenvalue convention. |

## Conditional subspaces and the square determinant

Writing \(h=(h_I,h_J)\) gives \(Xh=(h_I,B_{II}h_I+B_{IJ}h_J)\).
Thus \(\ker X\) has the asserted description and \(\operatorname{rank}X=k+\operatorname{rank}B_{JI}\).
For every perturbation supported on \(A_{II}\), the two changes in \(Mh\) sum to a vector in the coordinate space on \(I\) plus \(\operatorname{ran}B_{JI}\) on \(J\).
Projection annihilates that vector even for \(h\) outside \(H\).
The spectral projector is a joint Borel function of the exterior entries and \(z\).
The compressed Gram matrix on the full space has the desired spectrum together with exactly \(N-\dim E_t\) extra zeros, which gives measurable restricted counts.

On full column rank, \(T\) is square in the indicated orthogonal decompositions and the lower-left block vanishes.
The upper-left block is \(C_H-zI_H\) because \(\Pi|_H=I_H\).
The lower-right block \(Y=X|_{H^\perp}\) satisfies \(YY^*=XX^*\), whose Schur complement is \(B_{IJ}B_{JI}\).
This proves the absolute determinant formula with exactly \(k\) cross-block singular factors.

## Original-law probability and uniformity

The truncation exponents give \(4/16+1/8=3/8\), \(2/16=1/8\) and raw cutoff \(N^{7/16}\).
Deletion of at most two \(J\)-endpoints per marked coordinate leaves at least \(N-k-2N^{3/8}\) rows.
After fixing the mark indicators, the retained rectangle consists of independent strict off-diagonal coordinates with the same conditional unmarked law, since \(I\) and the surviving rows are disjoint and no reflected pair is repeated.
Truncated conditional first and second moments converge to their original values, and centering and standardizing preserve a bounded fourth moment.
The affine bound absorbs the new mean row by row, and the standard deviation is uniformly bounded away from zero for large \(N\).
For at least \(N/5\) rows it therefore gives a fixed lower threshold and failure \(e^{-cN}\) for every real net point.
The exponential net cardinality in \(k\) leaves an exponentially small failure for sufficiently small law-dependent \(\delta\).
The extension uses the unconditional event \(\|B_0\|\le K\) only after bounding this conditional net failure.
The real Gram matrix has the same minimum Rayleigh quotient over real and complex unit vectors, and restoring rows increases it.
Finally the expected squared Hilbert--Schmidt bound \(O(N)\) at squared threshold \(N^4\) gives the stipulated \(O(N^{-3})\) exception.

## Planar estimates and loss

Using the same projection and codomain for \(T_0\) ensures that \(\operatorname{rank}(T-T_0)\le\operatorname{rank}(M-M_0)+\operatorname{rank}(B-B_0)\le6N^{3/8}\).
The bounded-norm comparison and the original polynomial norm bound yield a total positive singular logarithm \(O_R(N+N^{3/8}\log N)\) for \(T\) and \(D\).
For \(T\), the determinant contributes at most \(k\log^-(c_0/2)\) plus one translated negative logarithm for each eigenvalue of \(C_H\), counted algebraically.
For \(D\) there is one such term per eigenvalue of \(M\).
Each logarithm has full-plane integral \(\pi/2\), including when its center lies in the disk, and the finite singular parameter sets have zero area.

On the first \(j\) ascending restricted right singular directions one has \(\|Lh\|\le t\|h\|\) and \(\|Xh\|\le s_j\|h\|\).
The variational upper bound for the \(j\)-th ascending singular value of \(T\) thus includes all kernel multiplicities, and decreasing \(\log^-\) gives the asserted integrated sum.
Each thresholded term with \(s_j\le u\) contributes at least \(\log(1/r)\) when \(r<1\).
Intersecting \(E_t\) with the kernel of \(D-L\) costs at most \(2k\) dimensions and bounds the remaining dimension by the number of singular values of \(D\) at most \(t\).
The planar budget for \(D\) gives the claimed denominator \(\log(1/t)\).

Since \(t_N\le r_N\), the integral of the sum of the two counts defining \(G_N\) is at most \(C_R N/\log(1/r_N)\).
Dividing by \(k b_N\) gives \(C_R b_N\), and the largest inverse norm on the orthogonal complement inside \(E_t\) is at most \(1/u_N\), with the zero-dimensional case vacuous.
The accepted arbitrary-set envelope holds simultaneously for the resulting matrix-dependent sets on its event and tends to zero as their area vanishes.
The union of its \(O_R(N^{-3})\) exception and the two summable original-law tails proves the deviation series for every threshold.
Positivity permits the additional indicator, and the count integral bounds the area of even one bad direction when \(\log(1/r_N)\gg N\).
For \(k\) proportional to \(N\), two fixed inverse polynomial scales give \(\log(1/r_N)\) of order \(\log N\).

The non-elementary truncation and planar-envelope inputs were used at their established scopes after checking the local derivations and their hypotheses at these interfaces.
The cited affine fourth-moment estimate has its complete symmetrization and row-count argument in C196v1.
The review found no additional external theorem needed for the deductions in C196v4 and did not re-audit the underlying published norm or concentration theorems.
