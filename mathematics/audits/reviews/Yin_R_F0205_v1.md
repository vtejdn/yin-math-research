---
author: Yin
---

# Residual inverse energy and physical reservoirs: independent whole-proof review

Date of the review and final affected-interface recheck: 2026-11-11T14:35, UTC.
The human record author is Yin.
The reviewing agent was outside substantive proof development and received the fixed candidate, necessary dependencies, exact assignment and repository rules without development dialogue, a mathematical summary or an expected verdict.
The reviewer read the complete candidate and formed initial findings before inspecting its dependency arguments and source interfaces.
No earlier project R conclusion was used to determine the candidate's verdict.
Existing source-unit accounts were read as mathematical inputs with their stated acceptance limits.
The authoring agent supplied the actual domain, input-model and measurability clarifications requested during inspection; the reviewer independently reread those edits and the affected argument before recording this finding.
The reviewer did not edit the Claim or contribute a substantive proof repair.

The inspected artifact is the current [C197 statement](../../claims/Yin_C_F0197_v1.md#statement) and [complete argument](../../claims/Yin_C_F0197_v1.md#argument), including its explicit fixed centered diagonal model, nonnegative integer mode counts, positive load threshold and minor-measurability qualification.
This is a whole-proof review of that Claim, not a completion review of the broader Brown-measure Task.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [C197 statement](../../claims/Yin_C_F0197_v1.md#statement) | All hypotheses, fixed-parameter and coupling quantifiers, free inverse dichotomy, finite invertibility, residual divergence, whole-space restriction and reservoir conclusions. |
| [Whole-candidate finding](#whole-candidate-finding) | [C197 argument](../../claims/Yin_C_F0197_v1.md#argument) | Complete current proof, including both companion orientations, truncation and deletion normalization, compression estimates and measurable inverse-mode selection. |
| [Whole-candidate finding](#whole-candidate-finding) | [C186v4 statement](../../claims/Yin_C_F0186_v4.md#statement) | Only fixed self-adjoint matrix-polynomial weak spectral convergence under the exact finite-variance model and arbitrary cross-size coupling. |
| [Whole-candidate finding](#whole-candidate-finding) | [C186v4 argument](../../claims/Yin_C_F0186_v4.md#argument) | The rank-stability, bounded-entry moments, finite-variance expected weak limit and row-block concentration chain supplying that input; no new review of its remaining conclusions. |
| [Whole-candidate finding](#whole-candidate-finding) | [C196 statement](../../claims/Yin_C_F0196_v1.md#statement) | Complex fourth-moment compressible-vector exclusion on a fixed norm guard, simultaneous bounded shifts, and applicability after principal deletion and interchange of input laws. |
| [Whole-candidate finding](#whole-candidate-finding) | [C196 argument](../../claims/Yin_C_F0196_v1.md#argument) | Fourth-moment small-ball, both lawful rectangular exposures, sparse nets and compressible extension; the subsequent spread and companion-distance deductions were also read and checked. |
| [Whole-candidate finding](#whole-candidate-finding) | [Miy26 spectral interface](../literature/Miy26/Yin_U003.md#miy26-u003) | Corollary 1.2 for nonscalar rational functions of a finite free semicircular tuple, with exact affiliated and bounded inverse conventions. |
| [Whole-candidate finding](#whole-candidate-finding) | [Miy26 boundedness input](../literature/Miy26/Yin_U002.md#miy26-u002) | The retained regularization, finite residual-space, exponential-decay and bounded-operator identification argument for the L2-to-boundedness implication. |
| [Whole-candidate finding](#whole-candidate-finding) | [Miy26 external interfaces](../literature/Miy26/Yin_U004.md#miy26-u004) | The accepted free-field and canonical affiliated-operator interfaces used by the semicircular corollary, retaining original-proof inspection limits. |

<a id="whole-candidate-finding"></a>
## Outcome and mathematical evidence

The complete clarified C197 statement follows from its argument at the stated scope.
No unresolved mathematical or source-applicability gap remains in this inspected candidate.
The following checks give the decisive evidence.

### Free inverse and finite invertibility

The evaluated polynomial \(s_1s_2+2s_2s_1-z\) is nonzero for every complex \(z\), by algebraic freeness of the semicircular tuple.
The accepted free-field interface supplies an affiliated inverse, and Miy26's boundedness theorem makes any such L2 inverse bounded.
This proves the dichotomy without a Brown-support premise.
The reviewer directly checked Miyagawa, [arXiv:2603.19528v2](https://arxiv.org/pdf/2603.19528v2), Theorem 1.1 and Corollary 1.2 with its proof on PDF pp. 1--2, against U003.
The finite faithful trace and field property are essential.

Multiplication on both sides verifies the displayed companion-inverse formula in the affiliated matrix algebra.
Its upper-left corner is \((P-z)^{-1}\); finite matrix L2 norm would imply finite L2 norm of that corner, so infinite inverse energy transfers to the companion.
The trace of \(|L|^{-2}\) equals the squared L2 norm of the inverse by tracial equivalence of the left and right inverse products.

For each finite realization, the determinant polynomial has a nonzero leading coefficient and finitely many zeros.
Tonelli on bounded planar disks and a countable intersection over \(N,D\) produce a deterministic full-area \(Z_0\).
Simultaneous invertibility is asserted almost surely for each fixed \(z\in Z_0\), not on one event for every \(z\in Z_0\).
The construction depends only on the within-size laws and remains valid for any prescribed cross-size coupling.

### Fixed truncation, deletion and mode counts

The Hermitian dilation is a fixed \(6\)-by-\(6\) self-adjoint matrix pencil in the two inputs.
C186v4 applies with exactly the centered fixed diagonal and off-diagonal laws now stated in C197.
Its relevant proof uses entry truncation, rank control and summable bounded-differences tails; it needs neither independence across sizes nor an almost-sure norm bound.

The dilation's eigenvalues are the signed singular values of \(L_N(z)\).
Normalization by \(1/(2N)\), instead of its full dimension \(6N\), therefore gives precisely \(3\tau_3(f_R(|L(z)|))\).
The capped inverse-square function is continuous at zero with value \(R\), vanishes at infinity and has total variation \(2R\).
Physical deletion removes \(6|D|\) scalar coordinates of this same dilation, so principal-submatrix interlacing controls unnormalized counting functions by \(6r\).
Integration and normalization give the bound \(6rR/N\), uniformly over all admitted deletions.
There is no separate minor convergence event requiring a large union bound.

Removing at most the first nonnegative \(k_N\) inverse modes loses at most \(k_NR\) from the capped sum, and this loss divided by \(N\) tends to zero for fixed \(R\).
The countable integer truncations admit one probability-one event on which the lower limit is at least every \(3\tau_3(f_R(|L(z)|))\).
Monotone convergence then forces divergence in the spectral case.
No unbounded varying truncation is passed through the finite-size limit, and no rate is obtained.

### Both low-singular spaces and simultaneous minors

C196's fourth-moment estimate allows conjugated entries and dependence between real and imaginary parts.
Its first rectangular action supplies positive coefficient norm, and the second conditional exposure leaves independent original entries because both exposed index sets avoid the sparse support.
The mirrored Hermitian rectangle is not treated as independent, and the norm guard is not conditioned into the fresh rectangle law.
The sparse-net entropy and the count-good Bernoulli implication give the required exponential exclusion simultaneously in the bounded shift.

Rescaling a principal minor by \(\sqrt{N/n}\) preserves the fixed raw laws and gives \(n^{-1/2}\) normalization.
The product and spectral parameter scale by \(N/n\), bounded by \(2\) eventually for fixed \(r\).
The same C196 constants therefore apply with enlarged fixed guards and shift disks.
Interchanging the input colors treats the adjoint polynomial.
The polynomial number of deletion sets is absorbed by an exponential bound without independence of minor events.
Finitely many smaller dimensions can be absorbed by the constant \(C\).

The right residual equations give root norm at least \([2(1+2K)]^{-1}\) and root residual at most \((1+3K)a\).
The left equations give the swapped polynomial with parameter \(\overline z\), root norm at least \([2(1+3K)]^{-1}\) and residual at most \((1+2K)a\).
Sufficiently small common \(a\) thus forces incompressibility of each normalized root.
Normalized sparse truncation converts this into a uniform root tail bound outside every admitted support, including the zero-head case.
Every vector of either low-singular subspace satisfies its residual bound, so these are whole-subspace inequalities, valid also at zero singular values.

### Compression, loads and inverse remainder

Orthonormal bases \(X,Y\) for the two spaces give the representation \(E=XFY^*\).
Restriction bounds put both Gram matrices of \(P_TX,P_TY\) between \(c_*^2I\) and \(I\).
Polar decomposition and singular-value inequalities for invertible factors yield the lower factor \(c_*^2\) and upper factor \(1\), including rectangular \(F\) and appended zeros.
Summing squares gives the Hilbert--Schmidt estimate with squared-energy factor \(c_*^4\).

For the explicitly positive \(\epsilon\), the load identity bounds the removed set by \(2/\epsilon\).
Every retained load can only decrease under compression, and removed-coordinate loads are zero.
Division by the retained energy proves the normalized load bound.
The choice \(\epsilon=N^{-1/4}\) removes at most \(2N^{1/4}\) coordinates and is therefore allowed eventually.

Inverse singular terms have range in the right low-singular space and adjoint range in the left low-singular space, matching the compression hypotheses.
Terms corresponding to singular values larger than \(a\) have total squared norm at most \(3N/a^2\).
Subtracting this uniform \(O(N)\) contribution from residual divergence proves the low-space divergence.
Measurable spectral projections and a measurable basis choice within ties make the actual inverse remainder minor-measurable.
The deterministic inequalities for arbitrary \(E\) need no measurability; the fresh-border assertion is correctly restricted to minor-measurable selections.

## Source completeness and limits

Source identification and applicability needed by C197 are adequate.
Miy26's primary statements and corollary proof were checked directly, and U002's retained boundedness reconstruction was inspected, including the finite-dimensional decay argument and affiliated identification.
The accepted foundational free-field, bounded-intersection, homogeneous-norm and affiliated-operator interfaces retain their recorded source limits.
Their original proofs were not recursively re-audited here.
C186v4's bounded-differences and bounded-entry sources and C196's method attribution retain their existing exact source records; no theorem from that method attribution is invoked directly for the dependent product.

The norm guard remains an event restriction, without summability of its complement.
Residual divergence supplies no quantitative rate.
This finding proves no lower bound for the complete determinant-coefficient tensor, conditional small-ball estimate, averaged distance-probability floor, logarithmic convergence or broader Brown-measure conclusion.
No numerical experiment or formal verification was used as mathematical evidence.
The Claim's assessment and adoption of this finding remain the responsibility of its explicit C decision.
