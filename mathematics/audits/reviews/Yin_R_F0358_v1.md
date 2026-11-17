---
author: Yin
---

# Gaussian flag compression and the terminal singular values of a real Wigner polynomial

An agent acting for Yin performed a separate initial whole-proof review of [C351v1](../../claims/Yin_C_F0351_v1.md#statement) at 2026-11-17T06:21 UTC.
The reviewer took no part in developing this proof and received the fixed Claim and the inspection scope without proof-development dialogue, author explanations or a previous finding on C351v1.
The earlier results were checked at the interfaces identified below.

## Finding

The proof establishes almost-sure weak Brown convergence under every cross-dimensional coupling and complete convergence of the terminal integral for the stated two-color model.
The Gaussian assumption concerns the strict upper law of \(B_N\).
The regular component belongs to the strict upper law of \(A_N\), and both diagonals need only the original centering and second moments.

For \(n=N-k\) and \(a=n/N\), each old input is \(\sqrt a\) times a canonical input, so the quadratic minor is \(aP_n^{\rm can}\).
The factor \(a\) multiplying the canonical normalized logarithmic sum and the shift \(z/a\) both follow from the original \(1/N\) normalization.
The jumps of the even \(k\) have size two and eventual spacing tending to infinity, so each \(n\) has bounded multiplicity and the every-coupling trim applies along finitely many injective subsequences.
On the summable Frobenius norm guard the discarded positive logs cost \(O_R(h\log N)\).
Thus \(b_{2h}\ge b_h-o(1)\), while the fixed positive regularizer bounds \(b_{2h}\) from above with error \(2h|\log d|/N\).
The canonical regularizer changes from \(d\) to \(d/a\) with log error at most \(|\log a|\).
Taking \(d\downarrow0\) after \(N\to\infty\) proves the second trim in planar \(L^1\).
The difference of the two sums then bounds \(h\log^- t_{2h+1}/N\) in \(L^1\).

The adaptive index \(r\) depends only on the minor and the shift.
Telescoping every later adjacent ratio down from \(t_{2h+1}\) costs at most \(160h^3\log N\) before normalization.
At a strict gap the norm of the exterior power after removal of its leading rank-one term is the retained product times \(t_r/t_{r+1}\).
The complementary-minor identity applies separately to the unitary left and right singular frames against the same real orthogonal flag.
For a complex unit vector orthogonal to the previously projected Gaussian columns, the real and imaginary variances of its scalar projection sum to one.
One real Gaussian coordinate therefore gives the conditional small-ball bound for each projected distance, including when the complex frame has real directions.
The two determinant overlaps each exceed \(N^{-7r}\) outside the stated summable exception.
Their product dominates the operator-norm remainder since \(14r\le28h<40h\).
No independence between these overlaps is used, and \(r=0\) gives the uncompressed determinant directly.

For subsequent deletions the cofactor is the determinant times \(v^{\mathsf T}T^{-1}v\) in the real orthogonal basis.
Congruence of the transpose-symmetric part by \(T\) gives \(\operatorname{sym}M'-zI\), of norm at least \(|\operatorname{Im}z|\) for real \(M'\).
On the norm guard, an eigenvalue of the real or imaginary symmetric part of \(T^{-1}\) thus has modulus at least \(c_\delta N^{-10}\).
Conditioning on all other Gaussian coordinates gives \(\lambda X^2+c\), whose sublevel probability at \(N^{-32}\) is \(O_\delta(N^{-11})\).
The normalization by the Gaussian norm costs at most \(N^4\) outside \(O(N^{-3})\), so the \(N^{-36}\) floor holds at each remaining step with summable total failure over all \(k\) deletions.

The parameter exceptional sets have summable expected area away from the real axis.
For the final compression the negative part of its log determinant divided by \(N\) has a deterministic local planar square bound because the eigenvalue mass \((n-k)/N\) is at most one and the square of the negative logarithmic kernel is integrable.
The same bound and compact Brown support control the target on the exceptional sets and shrinking real strip.
This yields the lower limit for each disk on independent dimensions, where converse Borel--Cantelli gives summability of the compression deviations at their specified marginals.
The one-sided transfer then gives Brown convergence under every coupling, and the scalar terminal equivalence gives complete convergence for every real threshold \(v>0\) by taking a smaller positive rational threshold.
The unrestricted finite-variance Task, including fully atomic input pairs, remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Gaussian flag finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Gaussian flag finding](#finding) | [Claim statement](../../claims/Yin_C_F0351_v1.md#statement) | Fixed raw laws, centering and moments, Gaussian and regular-component hypotheses, Brown limit, global terminal rank and all positive thresholds. |
| [Gaussian flag finding](#finding) | [Complete proof](../../claims/Yin_C_F0351_v1.md#argument) | Independent minor, genuine principal compression, normalization, reduction to the disk lower deviations and every-coupling conclusion. |
| [Gaussian flag finding](#finding) | [Minor trims](../../claims/Yin_C_F0351_v1.md#minor-trims) | Canonical dilation, bounded multiplicities, both trimmed limits and the intermediate negative logarithm. |
| [Gaussian flag finding](#finding) | [Adaptive gap](../../claims/Yin_C_F0351_v1.md#adaptive-gap) | Gap choice, exterior remainder, complementary left and right overlaps on a common real Gaussian flag. |
| [Gaussian flag finding](#finding) | [Later hyperplanes](../../claims/Yin_C_F0351_v1.md#later-hyperplanes) | Cofactor identity, transpose-symmetric inverse norm, quadratic small-ball estimate and accumulated losses. |
| [Gaussian flag finding](#finding) | [Planar passage](../../claims/Yin_C_F0351_v1.md#planar-transfer) | Measurable finite compressions, summable bad areas, planar square bounds, strip removal and the terminal implication. |
| [Gaussian flag finding](#finding) | [Fourth-moment model](../../claims/Yin_C_F0186_v26.md#statement) | Canonical normalization, real Wigner laws and independence within each size. |
| [Gaussian flag finding](#finding) | [Concentration hypothesis](../../claims/Yin_C_F0186_v32.md#statement) | Concentration-function integral for the regular component. |
| [Gaussian flag finding](#finding) | [One-sided transfer](../../claims/Yin_C_F0186_v33.md#statement) | Mesoscopic even block, permitted atoms, original normalization and sufficient exterior disk criterion. |
| [Gaussian flag finding](#finding) | [Scalar trim and terminal equivalence](../../claims/Yin_C_F0186_v36.md#statement) | Global scalar rank under every coupling and complete convergence of the terminal negative logs. |
| [Gaussian flag finding](#finding) | [Regularized potentials](../../claims/Yin_C_F0186_v4.md#regularized-potentials) | Fixed regularizer and local uniform almost-sure convergence on each canonical subsequence. |
