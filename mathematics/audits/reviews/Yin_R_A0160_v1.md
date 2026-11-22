---
author: Yin
---

# Regular rank for a sum of two vertex matrices and its triangular chains

## Whole finding

At 2026-11-22T04:52 UTC a separately assigned agent outside proof development reviewed the whole fixed statement and both proof sections of Yin_C_A0123_v1.
The reviewer worked from the Claim and its indicated mathematical inputs, without proof-development dialogue, author explanations or earlier findings on this Claim.
The rectangular rank inequality, the affiliated invertibility assertions and the finite inverse-layer bound follow under the stated hypotheses.

For each admissible phase, conjugation of the amplification by the fiber unitary gives a normal embedding into the matrix group von Neumann algebra and fixes the identity fiber pointwise.
The same conjugation carries the polar decomposition of a closed affiliated matrix to the twisted polar decomposition, so its range projection has trace \(2d\) times its original trace.
The embeddings on each vertex agree first on group elements, then on the von Neumann algebra by normality and on affiliated elements by spectral truncation.
This argument uses each extending unitary representation separately and requires infinitely many distinct admissible phases.

The \(21\) and \(12\) right corners acquire factors \(t^{-1}\) and \(t\) respectively.
The row scaling and exchange therefore give the displayed affine polynomial with diagonal \(R_{21},L_{12}\) and upper-right block zero at the origin.
For its finite row \(X\) of scalar coefficient entries the bounded regularizer \(s=(1+XX^*)^{-1/2}\) is an affiliated unit, and \(sX(sX)^*=XX^*(1+XX^*)^{-1}\le1\).
Applying \(s\) on every output coordinate preserves all ranks by affiliated invertibility.
For the resulting bounded matrix at zero let \(Y\) be its closed range.
The projection of \(Y\) to the first output block has range closure of dimension \(\operatorname{rk}_G R_{21}\), while its kernel on \(Y\) contains the closed image of the second input block of dimension \(\operatorname{rk}_G L_{12}\).
Rank-nullity for this restricted bounded projection gives the claimed lower bound even for rectangular blocks.
The finite-evaluation inequality for degree one gives \((k-1)\operatorname{rk}_G F(0)\le k(2d)\operatorname{rk}_G A\) for every \(k>1\), which yields (1) in the limit.
In the square case two full corners force full rank, hence an affiliated inverse.

For the border in the Claim, the first-vertex \(12\) corner is upper triangular because \(N\) is strictly upper triangular and \(b\) occupies the last column.
The second-vertex \(21\) corner is lower triangular because \(c\) occupies the last row.
Each has \(q+1\) invertible diagonal blocks, so both corners and then the border are affiliated units.
Writing \(P=pI_q\), the ordered expression \(\sum_{j=0}^{q-1}(P^{-1}N)^jP^{-1}\) inverts \(P-N\) since \(P^{-1}N\) is nilpotent.
Elimination with that pivot gives the unit \(p-c(P-N)^{-1}b\), and \(q=0\) uses the scalar two-corner test directly.
The natural subgroup embedding preserves affiliated inverses, so induction from the group ring sends each vertex layer \(D_k(V_i)\) into \(D_k(G)\).
The expression uses only ring operations on these inputs and \(p^{-1}\in D_{k+1}(G)\), regardless of the length of the chain.

For the congruence double, the paired eigenspaces give invertible off-diagonal blocks for \(a\), and the common edge action preserves the two weights at all phases.
For the conjugated commutation relation, the bent \(a_2\) and the image of \(k^{-1}a_1k\) act on different tensor factors and the two corners of the mixed denominator are regular translations tensored with identities.
These checks verify exactly the two example specializations cited in the statement.
The general chain test with arbitrary final diagonal and unrestricted border entries remains outside this result.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0123_v1.md#statement) | Rectangular inequality, square full-corner criterion, finite chains, layer bound and examples. |
| [Whole finding](#whole-finding) | [Affiliated coefficient polynomial](../../claims/Yin_C_A0123_v1.md#a-polynomial-with-affiliated-coefficients) | Normal twisting, triangular specialization, common bounded regularizer and finite-evaluation limit. |
| [Whole finding](#whole-finding) | [Finite inverse layer](../../claims/Yin_C_A0123_v1.md#the-finite-inverse-layer) | Border corners, ordered pivot inverse, scalar Schur complement and layer restriction. |
| [Whole finding](#whole-finding) | [Regular-trace identity](../../claims/Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization) | Fiber intertwiner and trace normalization. |
| [Whole finding](#whole-finding) | [Common denominators](../../claims/Yin_C_F0068_v1.md#argument) | Bounded left multiplication on a finite affiliated row in Section 2. |
| [Whole finding](#whole-finding) | [Finite-evaluation inequality](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Degree-one rectangular polynomial and arbitrarily many distinct evaluations. |
| [Whole finding](#whole-finding) | [Chain realization](../../claims/Yin_C_A0117_v1.md#chain-realization-and-rank) | Ordered finite expansion and affiliated elimination. |
| [Whole finding](#whole-finding) | [Congruence double](../../claims/Yin_C_A0121_v1.md#statement) | Application to the specified mixed denominator. |
| [Whole finding](#whole-finding) | [Finite quotient representation](../../claims/Yin_C_A0121_v1.md#the-finite-quotient-detecting-the-commutator) | Equal edge eigenvalues, distinct eigenvalues for the nonedge letter and full corners. |
| [Whole finding](#whole-finding) | [Double deformation](../../claims/Yin_C_A0121_v1.md#the-regular-rank-computation) | Two-weight extensions and both denominator corners. |
| [Whole finding](#whole-finding) | [Conjugated commutation quotient](../../claims/Yin_C_A0122_v1.md#statement) | Application to the specified mixed denominator. |
| [Whole finding](#whole-finding) | [Quotient deformation](../../claims/Yin_C_A0122_v1.md#a-bend-on-the-quotient) | Descent for every phase and both denominator corners. |
