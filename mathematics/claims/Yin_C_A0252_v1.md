---
author: Yin
---

# Full group-ring inner rank and a first-layer drop for groups with finite abelianization

## Statement

Let \(G=\langle g_1,\ldots,g_s\rangle\) have finite abelianization, with \(g_1\) of infinite order.
There exists a square matrix \(U\) of size \(s\) over \(\mathbb ZG\) with invertible complex augmentation and full inner rank over \(\mathbb CG\), whose inner rank drops to at most \(s-1\) after adjoining just the affiliated inverse of \(g_1-1\).
In particular its regular rank is at most \(s-1\).

For the torsion-free Promislow group on two standard generators, the drop is exactly from two to one, and the regular kernel dimension is exactly one.
There is also an eight-square example on that group with inner rank eight over the group ring, inner rank six after the same single cyclic denominator, and regular rank six.
This group satisfies the complex strong Atiyah conjecture.
Thus torsion-freeness and regular scalar injectivity are compatible with a full group-ring inner rank and a nontrivial, integer-dimensional kernel, even for two columns.

In the [order-24 closed-chain test](Yin_C_A0247_v1.md#statement), the actual index-four subgroup \(F\) has finite abelianization if the half-rank rectangle exists.
It therefore admits a full-inner-rank presentation matrix with a one-layer rank drop by the same construction.
Any obstruction based on the eight-square chain must use more of its four-step structure than the rank discrepancy and cyclic denominators alone.

## Relator columns and a single cyclic pivot

Map the free group on \(s\) letters onto \(G\) by the given marking.
The exponent sums of the words in its kernel form the kernel of \(\mathbb Z^s\to G_{\rm ab}\).
Indeed abelianizing the quotient adds exactly the exponent sums of the relators.
Since the quotient is finite, one can choose \(s\) actual relator words whose exponent vectors are linearly independent over \(\mathbb Q\).
This choice needs no finite presentation.

For each chosen word \(w=l_1\cdots l_n\) expand
\[
       w-1=\sum_{j=1}^n (l_j-1)l_{j+1}\cdots l_n .
\]
A positive letter \(g_i\) contributes its suffix to the coefficient of \(g_i-1\), while a negative letter contributes the negative suffix multiplied on the left by \(g_i^{-1}\).
This is the right-coefficient convention for the [presentation boundary](Yin_C_A0139_v1.md#the-presentation-boundary).
Take the resulting \(s\)-component coefficients in \(\mathbb ZG\) as one column of \(U\).
The corresponding product with the row \((g_1-1,\ldots,g_s-1)\) is zero because \(w=1\) in \(G\).
The augmentation of the column is precisely its exponent vector, so \(\varepsilon(U)\) has ordinary rank \(s\).
Any factorization of \(U\) over \(\mathbb CG\) factors its augmentation through the same number of columns; hence \(U\) has full inner rank there.

Write \(V\) for the lower \(s-1\) rows of \(U\).
The element \(g_1-1\) is injective on each regular cyclic coset by Fourier transform and is therefore an affiliated unit.
Using the row relation above gives the factorization
\[
       U=
       \begin{pmatrix}
       -(g_1-1)^{-1}(g_2-1)&\cdots&-(g_1-1)^{-1}(g_s-1)\\
       & I_{s-1} &
       \end{pmatrix} V ,
\]
where the lower block is the identity.
This proves the upper bounds and \(\dim_G\ker U\ge1\).

## The Promislow group and the index-four subgroup

Use the [Promislow presentation](Yin_C_A0118_v1.md#a-double-over-an-infinite-cyclic-subgroup) with generators \(a,b\), and take the relator words
\[
                b^{-1}a^2b a^2,\qquad a^{-1}b^2a b^2 .
\]
Their exponent vectors are \((4,0),(0,4)\).
This torsion-free group has [integer regular ranks for every finite complex group-ring matrix](Yin_C_A0013_v1.md#the-complete-task-interface-and-its-remaining-generalization-gap), hence every nonzero scalar has regular rank one.
The constructed two-square \(U\) has nonzero entries by augmentation, giving regular rank at least one; the single-pivot factorization gives the reverse inequality.
It follows that \(\ker U\) has dimension one and that one is the exact inner rank after that inverse.
The block diagonal \(U\oplus U\oplus I_4\) has invertible augmentation and regular rank six.
The two factorizations use the same inverse \((a-1)^{-1}\) and give a six-coordinate factorization there.
Regular rank rules out every shorter factorization.
The comparison concerns these numerical ranks; this block diagonal has no asserted realization as the four-step chain.

For the order-24 group set \(N=H'\).
The [finiteness of \(N/N'\)](Yin_C_A0245_v1.md#the-integral-orders-and-the-finite-commutator-abelianization) and \(F/N\simeq C_6\) imply that \(F/N'\) is finite.
Indeed \(N/N'\) is its normal subgroup of index six.
Since \(N'\subseteq F'\), its quotient \(F/F'\) is finite as well.
The finite-index subgroup \(F\) is finitely generated and contains the infinite-order \(t\).
Choose a generating list with \(t\) first to apply the construction inside the same group.

## Assessment history

### Decision full-inner-rank-in-the-presentation-example

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:32 |
| status | proved |
| reason | Independent whole-proof inspection verified the stated bounds, hypotheses and argument at the indicated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full group-ring rank, one cyclic inverse and the limits of numerical rank comparison. |
| argument | [Relator columns and a single cyclic pivot](#relator-columns-and-a-single-cyclic-pivot) | Full-rank exponent vectors, suffix expansion and the explicit factorization. |
| argument | [The Promislow group and the index-four subgroup](#the-promislow-group-and-the-index-four-subgroup) | Sharp two- and eight-coordinate examples and finite abelianization for the subgroup. |
| review | [Full inner rank in the presentation example](../audits/reviews/Yin_R_A0202_v1.md#full-inner-rank-in-the-presentation-example) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-full-inner-rank-in-the-presentation-example)
