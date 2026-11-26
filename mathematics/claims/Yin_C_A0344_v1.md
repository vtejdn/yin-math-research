---
author: Yin
---

# A Schur pivot alternative on the index-four subgroup with cyclic abelianization of order five

## Statement

Suppose a half-nullity rectangle satisfies the [torsion-free scalar-injective noncyclic order-twenty hypotheses](Yin_C_A0333_v1.md#statement).
Let \(N\) be the common sign kernel and \(R\in M_4(\mathbb CN)\) the signed commutator of regular rank two.
Then \(N_{\rm ab}\cong C_5\) and its commutator subgroup is perfect.
There is a three-square submatrix \(B\) of \(R\) and an actual character \(\psi\) of \(N\) such that three nested pivot minors, of sizes one, two and three, are numerically invertible.
In particular \(B\) has group-ring inner rank three.
The original eight-label support of \(R\) suffices for every entry of \(B\).
Elimination of its first two pivots gives one of the following certificates in the subgroup itself.

* A two-square submatrix has group-ring inner rank two and regular rank one, and its inner rank becomes one upon adjoining a single actual group-ring scalar inverse. The corresponding formally inverted scalar has nonzero character value.
* A two-square submatrix is numerically invertible at \(\psi\) and has strictly fractional nullity. Its Schur complement is a fractional-rank scalar over one actual group-ring inverse in \(U(N)\).
* The three-square matrix \(B\) has regular rank two. Its inner rank becomes exactly two after adjoining one actual scalar inverse at each of two successive layers. There is an explicit rational expression which vanishes there and has a nonzero formal value at \(\psi\), with both pivot values nonzero throughout the numerical calculation.

These are outcomes of a single pivot procedure. They need not be mutually exclusive for different choices of minors.
Every pivot and its actual inverse belongs to the affiliated algebra of the subgroup \(N\).

## The subgroup and a full numerical minor

Under the half hypothesis the [abelianization identification](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case) gives \(H_{\rm ab}=C_5\times C_2^2\), and the [solvable-image exclusion](Yin_C_A0321_v1.md#statement) gives \(H'=H''\).
The subgroup \(N\) is the preimage of \(C_5\).
Since \(H'\le N\) is perfect, \(H'\le N'\); since \(N/H'\cong C_5\) is abelian, \(N'\le H'\).
This proves \(N'=H'\) and the asserted abelianization.

By the [five-character detection theorem](Yin_C_A0343_v1.md#statement) some \(\psi\) gives \(\psi(R)\) rank at least three.
Choose a three-square nonsingular numerical minor, then a nonsingular two-square minor inside it and a nonzero entry of the latter.
Permutations put these in the leading positions of \(B\).
A factorization of \(B\) over \(\mathbb CN\) through fewer than three coordinates would contradict the numerical rank after applying \(\psi\).
Taking submatrices can only lower the regular rank, so \(B\) has regular rank at most two.
The regular representation on \(N\) has the scalar injectivity assumption by the coset decomposition.

## Two scalar pivot decisions

Put \(A=\mathbb CN\) and use the actual unital subalgebras of \(U(N)\).
The first pivot \(a=B_{11}\) has nonzero \(\psi(a)\), hence is an affiliated unit.
Eliminate it to get a two-square Schur remainder \(S\) over \(A[a^{-1}]\); the triangular row and column operations show that \({\rm rk}\,S\le1\).
Write \(b=S_{11}\).
The numerical values of the same formal expressions are defined at \(\psi\), and both the value of \(b\) and the determinant of the numerical \(S\) are nonzero, by the nested pivot minors.
This numerical substitution refers to the words used in the elimination.

If \(b=0\) in \(U(N)\), the selected two-square submatrix has regular rank exactly one by eliminating \(a\) and factors through one coordinate in \(A[a^{-1}]\).
Its ordinary evaluation is invertible, so it originally has inner rank two and the formal expression for \(b\) maps to zero only in the actual localization.
If \(0<{\rm rk}\,b<1\), that same two-square submatrix has regular rank \(1+{\rm rk}\,b\) and hence nullity \(1-{\rm rk}\,b\).
All original entries have the stated support.
Finally, if \({\rm rk}\,b=1\), the scalar \(b\) is invertible in the affiliated algebra.
Eliminating it in \(S\) gives a last scalar \(s=S_{22}-S_{21} b^{-1} S_{12}\) of regular rank zero.
Therefore \(s=0\).
The two invertible pivots make the rank of \(B\) exactly two and exhibit a two-column factorization over \(A[a^{-1}][b^{-1}]\).
The regular rank is a lower bound for inner rank in that subalgebra.
Universally adjoin an inverse for \(a\) first, use the displayed first Schur word for \(b\), then universally adjoin its inverse.
The character extends through both universal steps because the numerical pivot values are nonzero.
There the displayed expression for \(s\) has value \(\det\psi(B)/(\psi(a)b(\psi))\ne0\).
Its image in the actual two-layer subalgebra is zero.

## Assessment history

### Decision two-actual-pivots-over-the-index-four-subgroup

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:25 |
| status | proved |
| reason | A visible three-square minor gives an actual two-pivot test and the subgroup has cyclic abelianization of order five. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A visible three-square minor gives an actual two-pivot test and the subgroup has cyclic abelianization of order five. |
| argument | [The subgroup and a full numerical minor](#the-subgroup-and-a-full-numerical-minor) | The subgroup and a full numerical minor. |
| argument | [Two scalar pivot decisions](#two-scalar-pivot-decisions) | Two scalar pivot decisions. |
| review | [Two actual pivots over the index-four subgroup](../audits/reviews/Yin_R_A0236_v1.md#two-actual-pivots-over-the-index-four-subgroup) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-two-actual-pivots-over-the-index-four-subgroup)
