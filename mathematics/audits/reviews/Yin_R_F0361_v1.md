---
author: Yin
---

# Discrete determinant floors after eliminating rank-one colors

<a id="two-direction-elimination-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T12:57 an agent acting for Yin independently inspected the [fixed v2 statement](../../claims/Yin_C_F0353_v2.md#statement) and all its substantive argument sections.
The reviewer had no role in proof development and received no exploration dialogue, drafts, earlier findings or author explanations before the inspection.
The result holds under the stated real finite-variance input model.

The reviewer reconstructed the two-sided triangularization for a two-dimensional coefficient space, treating a singular spanning matrix by a kernel vector and an invertible one by an eigenvector of the matrix ratio.
Successive left and right restrictions give the scalar diagonals, which are all nonzero affine polynomials by fullness.
For each scalar random diagonal, exposing the other colors produces an independent possibly nonsymmetric complex shift under the polynomial norm guard.
The finite number of diagonal tests use only a union bound.
Deleting or restricting a rank-one variable preserves the remaining coefficient bounds and their span.
In the nonfull complement case the inverse corner vanishes over the free field.
At finite dimensions the polynomial factorization of the complement and injectivity on its kernel force surjectivity onto the full physical block, so the entire inverse corner vanishes there as well.
No rational expression is evaluated across a singular denominator.
The inverse update then has square-zero correction and a polynomial bound.

The established scalar shift floor and the finite-variance clipping estimates give all-size convergence in probability, convergence almost surely along \(2^j\), and the all-size upper limit under any coupling.
The reviewer checked both scalar realizations, including the graph edge counts, constant term and the same factor in finite and free log determinants.
The earlier v1 elimination derivations were rechecked where used.
The external results and the upstream shift floor were inspected at the applicable statements without re-proving their full original proofs.
The inspected result assumes the stated coefficient class and real inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Coefficient class and outcomes](../../claims/Yin_C_F0353_v2.md#statement) | Rank-one colors and a residual coefficient span of dimension at most two including the drift. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Whole proof](../../claims/Yin_C_F0353_v2.md#argument) | Reduction to scalar shifts and elimination in the larger pencil. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Rank-one elimination](../../claims/Yin_C_F0353_v2.md#rank-one-step) | Full and nonfull complementary blocks and finite-dimensional rank transfer. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Logarithmic convergence](../../claims/Yin_C_F0353_v2.md#logs) | Polynomial floor, all-size probability, dyadic pathwise limits and limsup. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Scalar classes](../../claims/Yin_C_F0353_v2.md#scalar) | Bipartite quadratics and formulas with at most one repeated variable. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Independent scalar shift](../../claims/Yin_C_F0194_v5.md#statement) | Uniform polynomial floor for real symmetric Wigner noise with a general complex shift. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Nonfull complement](../../claims/Yin_C_F0353_v1.md#singular-complement) | Polynomial rank factorization and the vanishing inverse corner. |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Finite-variance logarithmic band](../../claims/Yin_C_F0186_v40.md#band) | Cutoff control before any use of (T). |
| [Whole-proof finding](#two-direction-elimination-whole-proof) | [Schur normalization](../../ledger/Yin_L_F0061_v2.md#linearization-transfer) | The finite and free multiplier in the word-chain construction. |
