---
author: Yin
---

# Self-review of the sandwich coordinate-change proof

Date: 2026-11-22T07:14, UTC.
Human record author: Yin.

The agent that prepared the coordinate-change proof performed this whole-proof self-review on the fixed v4 text.
The development discussion, the v1 model and scalar lift, and the earlier v1 review were available in the review context.

<a id="sandwich-coordinate-change-finding"></a>
## Finding

The self-review covers the statement and complete bounded-dual argument of [C_F0012 v4](../../claims/Yin_C_F0012_v4.md#statement).
The standard-space and scalar-lift inputs agree with the same measure, tensor model and scalar normalizations in v1.
The [v1 finding](Yin_R_F0056_v1.md#main-counterexample-finding) supplies the earlier checks of those inputs, including applicability of the weighted Hilbert-transform bound.

The product rule gives the two specified defects for \(T\) and \(D_2\).
Since \(X=X^*\) and \(Xq=\Omega\), the two-sided multiplication of the rank-one operator produces \(P_\Omega\).
Conversely the vanishing of \(X([S,D_2]-q\langle q,\cdot\rangle)X\) gives vanishing on \(\operatorname{ran}X\) by injectivity and then on \(H\) by boundedness.
Both orientations of the right-multiplier correction agree with their vacuum actions and tracial pairings.
This checks all four dual commutators, with \([X,T]\) normalized in the generator-first convention.

In the free model, right creation commutes with first-factor multiplication and with left creation.
For left annihilation the exceptional grade is \(H_0\), where the commutator is the vacuum projection.
Thus the product-rule formulas apply to the actual original pair \((T,r)\).
Negating the old scalar lift changes its commutator sign and preserves commutation with \(S\).

The closed right multiplier \(Q\) acts on the last factor, and \(r\) appends \(1\in\operatorname{Dom}X^{-1}\).
More explicitly, \(Qr\) appends \(q\), with norm \(\|q\|_2\), including on the Hilbert direct sum.
This proves that the natural domain of \(QrQ\) is \(\operatorname{Dom}Q\).
Both left generators commute with the spectral projections of \(\rho(X)\) and preserve that domain.
The pairing with \(\Omega\in\operatorname{Dom}Q\) gives \(QP_\Omega Q\xi=q\langle q,\xi\rangle\).
For bounded \(f\in H_0\) supported in \((\varepsilon/2,\varepsilon]\), the value \((qf)\otimes q\) gives the claimed diverging norm ratio.
The review uses this composition for its domain computation and boundedness obstruction.

The final-two-factor map has row squared \(L^2\) norm two for the stated law.
Cauchy–Schwarz bounds it from \(K\bar\otimes K\) to \(K\), and the orthogonality of distinct output grades gives a bounded full-space \(R\).
At grade one \(T_1\) preserves the first coordinate, and on higher grades \(R\) never changes the first factor.
The only nonzero grade of \([R,l]\) is \(H_0\).
Both terms of \([R,l^*]\) vanish on grades zero and one, and the factors are disjoint from grade two onward.
Selfadjointness of \(S\) gives the stated sign in \([S,R^*-R]\).
The two half-kernels add to \(q(s)q(t)\) almost everywhere, verifying the weighted rank-one identity on the whole space.
Consequently both final duals are bounded and their operator and adjoint domains are all of \(H\).

The bounded spectral cutoffs lie in \(W^*(X)\), and \(a_\varepsilon Ya_\varepsilon=e_\varepsilon S e_\varepsilon\) converges strongly to \(S\), proving the generation claim.
The checked statement concerns the generator change, the bounded-dual construction and the direct composition's unboundedness.
The norm-separation and rational-closure conclusions are handled by the separately reviewed v1 argument.
There is no remaining gap in the v4 statement in this self-review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Sandwich coordinate-change finding](#sandwich-coordinate-change-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Sandwich coordinate-change finding](#sandwich-coordinate-change-finding) | [v4 statement](../../claims/Yin_C_F0012_v4.md#statement) | All hypotheses and conclusions of the transfer, the bounded concrete realization and the unbounded right-multiplier composition. |
| [Sandwich coordinate-change finding](#sandwich-coordinate-change-finding) | [v4 argument](../../claims/Yin_C_F0012_v4.md#argument) | Rank-one equivalence and correction, original duals, inverse-multiplier domain, unboundedness test, triangular-kernel boundedness and all grade checks, and generation by cutoffs. |
| [Sandwich coordinate-change finding](#sandwich-coordinate-change-finding) | [v1 tracial model](../../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | Same tracial Hilbert space, grade identification and first- and last-factor actions in the v4 application. |
| [Sandwich coordinate-change finding](#sandwich-coordinate-change-finding) | [v1 scalar dual](../../claims/Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction) | The bounded scalar operator for the same measure and its last-factor lift with the generator-first sign conversion. |
