---
author: Yin
---

# The remaining marked abelianizations for a half-dimensional four-site kernel

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity.
If some complex two-square rectangle \(B+At-s(D+Ct)\) has regular nullity \(1/2\), its marked abelianization belongs to the following list of 35 classes.
We identify pairs up to an isomorphism of the abelian group, interchange of the two marks, and independent inversion of either mark.

* The trivial abelianization contributes one class.
* For a nontrivial cyclic abelianization use additive coordinates \((1,k)\) in \(C_n\).
  The last column of the table below lists the 30 remaining pairs.
* For a noncyclic abelianization the group is \(C_m\times C_2\) and the marks are \((1,0),(k,1)\).
  The four remaining pairs \((m,k)\) are \((2,0),(4,1),(6,1),(10,2)\).

This is the exact list passing the order, individual mark index and short-character comparisons used below.
Realization of any of the surviving markings requires a further argument.
For the noncyclic group of order twenty the [solvable-image exclusion](Yin_C_A0321_v1.md#statement) further requires \(H'\) perfect.
The cyclic markings of orders 25 and 26 have the same perfectness restriction. [Order 25](Yin_C_A0229_v1.md#consequences-for-the-original-half-increment) [Order 26](Yin_C_A0237_v1.md#statement)

## Index and character conditions

Let \(Q=H_{\rm ab}\), write \(\bar s,\bar t\) for its marks, and take the trace unnormalized on matrix coordinates.
The [abelian order bound](Yin_C_A0201_v1.md#consequence-for-finite-abelian-quotient-orders) gives \(|Q|\le26\) and excludes order 23, since an infinite finitely generated abelian group has arbitrarily large cyclic quotients.
The [normal closure index bound](Yin_C_A0327_v1.md#actual-phases-and-the-normal-closure-of-a-mark) gives
\[
                       [Q:\langle\bar s\rangle]\le2,\qquad
                       [Q:\langle\bar t\rangle]\le2.
\]
In fact the quotient of \(H\) by the normal closure of either mark is already cyclic, and therefore agrees with the corresponding abelian quotient.

For any character of the marks with integer lifts \(a,b\) at parameter order \(e\ge2\), put
\[
                  c(a,b)=2(|a|+|b|)-\mathbf 1_{\{ab\ne0\}} .
\]
The [four-site character bound](Yin_C_A0311_v1.md#character-costs-for-a-two-square-rectangle) requires \(2c(a,b)\ge e\) whenever \((a,b)\ne(0,0)\).
It suffices to use divisors of the exponent of \(Q\) because the parameter lifts at the order of the cyclic character image can be reduced by the common divisor of both weights and the parameter order, with at least as strong an inequality.
A nonzero lift of the trivial character has \(c(a,b)\ge2e\) and never excludes a half kernel.

## Cyclic coordinates and all divisor costs

For \(Q=C_n\), at least one of the two generating residues is a unit.
Indeed their gcds with \(n\) are at most two by the index bound, and two nonunits would both be even for even \(n\), precluding generation.
Put the unit first and rescale it to one.
Thus \(\gcd(n,k)\le2\).
Independent inversions identify \(k\) and \(-k\).
If \(k\) is a unit, interchange further identifies \(k\) with \(k^{-1}\) and its negative modulo \(n\).
If it is a nonunit, there is only one unit mark, so no additional identification occurs.
We take the smallest nonnegative representative of the resulting set.
These transformations preserve rectangle nullity through the [marking symmetries](Yin_C_A0196_v1.md#all-surjections-onto-the-quotient).

For \(e\mid n,\ e\ge2\), and integer \(j\), put \(\|j\|_e=\min_{h\in\mathbb Z}|j-eh|\).
The following integer is \(n\) times the smallest nontrivial character cost divided by its chosen parameter order:
\[
             D_n(k)=\min_{\substack{e\mid n,\ e\ge2\\1\le a\le\lfloor e/2\rfloor}}
                      \frac{n}{e}\left(2(a+\|ka\|_e)
                                      -\mathbf 1_{\{\|ka\|_e\ne0\}}\right).
\]
Indeed \(b\equiv ka\bmod e\), so \(a=0\bmod e\) gives only the trivial character.
Otherwise symmetry and taking centered representatives give the stated range.
The cyclic criterion is \(2D_n(k)\ge n\).
The middle column gives the costs in the order of the candidate \(k\)'s before this last comparison.

| \(n\) | Canonical \(k\) with index at most two | \(D_n(k)\) in order | Remaining \(k\) |
| ---: | --- | --- | --- |
| 2 | 0, 1 | 2, 3 | 0, 1 |
| 3 | 1 | 3 | 1 |
| 4 | 1, 2 | 3, 4 | 1, 2 |
| 5 | 1, 2 | 3, 5 | 1, 2 |
| 6 | 1, 2 | 3, 5 | 1, 2 |
| 7 | 1, 2 | 3, 5 | 2 |
| 8 | 1, 2, 3 | 3, 5, 6 | 2, 3 |
| 9 | 1, 2 | 3, 5 | 2 |
| 10 | 1, 2, 3, 4 | 3, 5, 7, 6 | 2, 3, 4 |
| 11 | 1, 2, 3 | 3, 5, 7 | 3 |
| 12 | 1, 2, 5 | 3, 5, 6 | 5 |
| 13 | 1, 2, 3, 5 | 3, 5, 7, 9 | 3, 5 |
| 14 | 1, 2, 3, 4, 6 | 3, 5, 7, 9, 6 | 3, 4 |
| 15 | 1, 2, 4 | 3, 5, 9 | 4 |
| 16 | 1, 2, 3, 6, 7 | 3, 5, 7, 9, 6 | 6 |
| 17 | 1, 2, 3, 4, 5 | 3, 5, 7, 9, 9 | 4, 5 |
| 18 | 1, 2, 4, 5, 8 | 3, 5, 9, 9, 6 | 4, 5 |
| 19 | 1, 2, 3, 4, 7 | 3, 5, 7, 9, 9 | none |
| 20 | 1, 2, 3, 6, 9 | 3, 5, 7, 9, 6 | none |
| 21 | 1, 2, 4, 8 | 3, 5, 9, 9 | none |
| 22 | 1, 2, 3, 4, 5, 6, 8, 10 | 3, 5, 7, 9, 10, 10, 9, 6 | none |
| 23 | 1, 2, 3, 4, 5, 7 | 3, 5, 7, 9, 11, 9 | none |
| 24 | 1, 2, 5, 7, 10, 11 | 3, 5, 11, 9, 10, 6 | none |
| 25 | 1, 2, 3, 4, 7, 9 | 3, 5, 7, 9, 13, 9 | 7 |
| 26 | 1, 2, 3, 4, 5, 6, 7, 8, 10, 12 | 3, 5, 7, 9, 11, 10, 10, 9, 13, 6 | 10 |

For example, at \(n=16,k=7\) the order-eight lift \((1,-1)\) gives cost \(6\) after scaling by \(16/8\).
At \(k=6\), the divisor orders \(2,4,8,16\) give scaled minimum costs \(16,16,10,9\), respectively.
The rows of orders 20 and 24 are also excluded by the direct [cyclic order-twenty](Yin_C_A0314_v1.md#statement) and [order-twenty-four](Yin_C_A0303_v1.md#statement) theorems.

## Noncyclic coordinates

For noncyclic \(Q\) both mark indices are exactly two, so each mark has order \(m=|Q|/2\).
Since they generate \(Q\), its exponent is \(m\).
The finite abelian invariant factors therefore give \(Q=C_m\times C_2\) with \(2\mid m\) and \(2\le m\le12\).
Choose coordinates with \(\bar s=(1,0)\).
To see directly that this is possible, take any element \(v\) outside \(\langle\bar s\rangle\), with \(2v=h\bar s\).
If \(h\) were odd, the order of \(2v\) would have the same two-primary part as \(m\), impossible since the order of \(v\) divides \(m\).
Then \(v-(h/2)\bar s\) is an involution outside \(\langle\bar s\rangle\), giving the complementary \(C_2\).

Now \(\bar t=(k,1)\) has order \(m\), so \({\rm lcm}(m/\gcd(m,k),2)=m\).
Changing the complementary involution adds \(m/2\) to \(k\), and inversion permits a sign change.
For the six possible \(m\)'s, these operations alone reduce to the rows below.
The two candidates at \(m=10\) before the character test are inequivalent because modulo five interchange only inverts a nonzero slope and the orbits of 1 and 2 under sign and inversion are disjoint.

At each \(e\mid m,\ e\ge2\), the exponent of the second mark is \(ka\) plus the exponent of the chosen complementary involution.
Thus \(b\equiv ka\bmod e\) if \(e\) is odd, and \(b\equiv ka\bmod(e/2)\) if \(e\) is even.
This time \(a=0,\ b\ne0\bmod e\) is allowed.
Minimizing \(m c(a,b)/e\) over these character residues, with a centered representative in each coordinate, gives the table.
One may take \(0\le a\le\lfloor e/2\rfloor\) and test the one or two possible centered second residues, discarding the trivial pair.
The required threshold is \(m/2\).

| \(m\) | Candidate \(k\) | Minimum scaled cost | Result |
| ---: | ---: | ---: | --- |
| 2 | 0 | 2 | retained |
| 4 | 1 | 3 | retained |
| 6 | 1 | 3 | retained |
| 8 | 1 | 3 | excluded |
| 10 | 1 | 3 | excluded |
| 10 | 2 | 5 | retained |
| 12 | 1 | 3 | excluded |

This also accounts for the noncyclic order-twenty class in the [order-twenty classification](Yin_C_A0311_v1.md#the-noncyclic-quotient-of-order-twenty).
The normal closure condition excludes \(C_3^2\) and \(C_6\times C_3\) before these final character comparisons, since those groups have no cyclic subgroup of index at most two.

## Assessment history

### Decision the-remaining-marked-abelianizations

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | The normal closure index, short-character inequalities and separate order exclusions give exactly the listed thirty-five necessary markings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The normal closure index, short-character inequalities and separate order exclusions give exactly the listed thirty-five necessary markings. |
| argument | [Index and character conditions](#index-and-character-conditions) | Index and character conditions. |
| argument | [Cyclic coordinates and all divisor costs](#cyclic-coordinates-and-all-divisor-costs) | Cyclic coordinates and all divisor costs. |
| argument | [Noncyclic coordinates](#noncyclic-coordinates) | Noncyclic coordinates. |
| review | [The remaining marked abelianizations](../audits/reviews/Yin_R_A0228_v1.md#the-remaining-marked-abelianizations) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-remaining-marked-abelianizations)
