---
author: Yin
---

# Descent of half-dimensional Schur kernels and the role of the regular trace

## Initial mixing bound

At 2026-11-23T06:17 UTC a reviewer outside proof development examined the whole first version of [C0125](../../claims/Yin_C_A0125_v1.md#statement) without author explanations or a prior finding on that version.
The review verified the defect recurrence by center-valued polar comparison, conjugacy averaging and norm lower semicontinuity at a triangular limit.
It checked the Baire argument, the kernel identification by the two pivot rows, the exact second-layer projection formula, and the third-layer algebraic matrix units of that version.
The stronger depth bound below uses a different rectangular inverse.

## Original-group test and depth two

At 2026-11-23T06:24 UTC the same independent reviewer checked the entire fixed [second version](../../claims/Yin_C_A0125_v2.md#statement) and compared both proofs.
The positive estimate requires center-valued half trace.
The left and right defects then have equal center-valued traces, and the convex hull of group conjugates of the right defect contains its center-valued trace.
This bounds the supremum of the available rank gains below by the square of the scalar defect.
The rescaled perturbation converges to a triangular matrix with the two indicated diagonal ranks.
Lower semicontinuity and approximation of the extrema give the recurrence without attainment assumptions.
The linear pencil rank estimate yields density at each tolerance and the Baire category theorem applies in the complete space of absolutely summable coefficients.

The reviewer checked the kernel of \(K_b\) by solving its first and third rows in the affiliated algebra.
The Gram matrix has the same kernel dimension.
For an exact finite sum the column \(V\) has full initial support, and its final support is dominated by \(\operatorname{diag}(Q,Q)\) with the same unnormalized faithful trace.
Thus \(VL=\operatorname{diag}(Q,Q)\), using only the scalar half trace at this step.
The first diagonal block gives \(Q\), and the second column gives \(xF=0\) and \(xbF=Q\).
Together with \(LV=1\) these identities prove both corner inverse equations.
All expressions use just the one new scalar inverse in the second layer, proving the algebraic matrix-unit, parity and odd-dimensional representation assertions.
In the free cyclic extension, the kernel of \(QtP\) within \(P\) is the intersection of two free half-trace projections and hence zero.
These checks do not impose a center condition on the original group for that extension, and they leave finite support in the original group and the proposed general exclusion open.

## Nonregular free group representation

At 2026-11-23T06:18 UTC the reviewer independently checked the complete fixed [C0126](../../claims/Yin_C_A0126_v1.md#statement) without participating in its development or consulting an earlier verdict.
The reviewer checked the external semicircular example and free-field rank interface against MSY23, published pp. 30-31, 42-43 and 46, accepting its realization results as inputs.
The longest syllable pattern in a nonzero group-ring sum isolates a nonzero tensor of one-variable coefficient lists.
The prefix code and scaling of the free field preserve the first nonzero homogeneous term at the specialized triple, even though that triple satisfies a rational relation.
This proves scalar injectivity at both summands.
The nonzero imaginary trace on the first generator distinguishes the trace from the regular one.

The Cayley factors clear both row and column denominators in the group-ring matrix and give the stated two block evaluations of its Schur complement.
For every rational expression defined on both blocks, the recursive polynomial pivot preserves both domains.
The rank of its border at the specialized triple is at most the free polynomial inner rank, which is attained at the free triple.
Consequently projection to the free triple embeds the inverse closure into a skew field and excludes the proposed nonzero kernel projection from every original layer.
After adjoining a free Haar unitary the half-trace support formula does produce that projection at depth two.
The representation establishes a limitation on arguments that omit the regular trace.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Initial mixing bound](#initial-mixing-bound) | independently reviewed |
| [Original-group test and depth two](#original-group-test-and-depth-two) | independently reviewed |
| [Nonregular free group representation](#nonregular-free-group-representation) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Initial mixing bound](#initial-mixing-bound) | [First statement](../../claims/Yin_C_A0125_v1.md#statement) | Whole first version including its original third-layer bound. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Statement](../../claims/Yin_C_A0125_v2.md#statement) | Both original-group alternatives, depths and the free extension. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Defect recurrence](../../claims/Yin_C_A0125_v2.md#reduction-of-the-defect-with-one-more-group-element) | Center-valued averaging, triangular perturbation and quantitative bound. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Banach algebra](../../claims/Yin_C_A0125_v2.md#exact-mixing-with-absolutely-summable-coefficients) | Density, category and the infinite-support scope. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Polynomial witnesses](../../claims/Yin_C_A0125_v2.md#group-ring-witnesses-and-the-exact-projection) | The two pivot equations and the positive matrix of size three. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Single Gram inverse](../../claims/Yin_C_A0125_v2.md#algebraic-matrix-units-from-a-single-inverse) | Exact corner inverses, parity and depth. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Free extension](../../claims/Yin_C_A0125_v2.md#free-cyclic-extension-at-depth-two) | Free conjugate and trace threshold. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Polynomial pencil rank](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | The countability result for bounded linear pencils. |
| [Original-group test and depth two](#original-group-test-and-depth-two) | [Free supports](../../claims/Yin_C_A0124_v1.md#free-conjugates-and-sums-of-positive-operators) | Trace-preserving inclusion and the meet of two free projections. |
| [Nonregular free group representation](#nonregular-free-group-representation) | [Statement](../../claims/Yin_C_A0126_v1.md#statement) | Faithful unitary representation, scalar injectivity, original and extended layers. |
| [Nonregular free group representation](#nonregular-free-group-representation) | [Cayley generators](../../claims/Yin_C_A0126_v1.md#cayley-generators-and-scalar-injectivity) | Formal series and both free-field specializations. |
| [Nonregular free group representation](#nonregular-free-group-representation) | [Group-ring matrix](../../claims/Yin_C_A0126_v1.md#a-matrix-over-the-group-ring-and-its-half-kernel) | Clearing denominators and the two Schur ranks. |
| [Nonregular free group representation](#nonregular-free-group-representation) | [Failure of descent](../../claims/Yin_C_A0126_v1.md#why-the-kernel-projection-fails-to-descend) | Common polynomial representation, rank comparison, projection after free extension. |
| [Nonregular free group representation](#nonregular-free-group-representation) | [Semicircular source example](../literature/MSY23/Yin_U005.md#example-524-integral-rank-need-not-preserve-free-field-rank) | The rational identity and the algebraically free specialized triple. |
| [Nonregular free group representation](#nonregular-free-group-representation) | [Free-field criterion](../literature/MSY23/Yin_U004.md#theorem-56-exact-equivalences) | Actual polynomial matrix rank for a free-field realization. |
