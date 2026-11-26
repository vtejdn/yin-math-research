---
author: Yin
---

# The four corners and additional nullities at cyclic orders 25 and 26

## Statement

Let the torsion-free group \(H=\langle s,t\rangle\) have scalar group-ring injectivity and a marked surjection to \(C_m\), where \(m=25\) or \(26\).
Suppose \(K=B+At-s(D+Ct)\), with complex two-by-two coefficients, has regular rank \(3/2\).
Up to the label normalizations below, the only possible markings are \((1,7)\) for \(m=25\) and \((1,10)\) for \(m=26\).
All four constant matrices \(A,B,C,D\) must be invertible.

For either weight pair in the corresponding row of the table, define \(K(z)=B+z^bAt-z^a s(D+z^bCt)\) and \(\nu(z)=\dim_H\ker K(z)\) for \(z\ne0\).

| \(m\) | Two lifts \((a,b)\) |
| --- | --- |
| 25 | \((3,-4),(4,3)\) |
| 26 | \((3,4),(5,-2)\) |

Every \(m\)-th root of unity has nullity \(1/2\).
At \(m=26\), every other nonzero complex parameter has nullity zero.
At \(m=25\), for every finite set of additional nonzero parameters the sum of their nullities is at most \(1/2\).
In particular each such parameter has nullity at most \(1/50\).
These are necessary conditions on the unresolved cyclic markings.

## Short directions in the two marked quotients

The [finite-phase bound](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter) requires \(m/2\le2(|a|+|b|)\) for every nonzero integer lift of a multiple of the marked pair when the rectangle has rank \(3/2\).
Thus any lift of width at most six is excluded.
At order 25, surjectivity gives a unit residue among the two labels.
At order 26, if neither residue is a unit, one is 13 and the other is even and nonzero modulo 13.
Some even multiplier then gives residues \((0,2)\) up to interchange, which is excluded.

Use the label normalizations from the [rectangular phase test](Yin_C_A0196_v1.md#all-surjections-onto-the-quotient): multiplying the marks by a unit changes the generator of the quotient; adjoint and inversion interchange or change the sign of labels while preserving rank and permuting the four coefficient matrices up to signs and adjoints.
Normalize the marks to \((1,k)\) with \(0\le k\le\lfloor m/2\rfloor\).
The lifts \((1,k)\) suffice when \(0\le k\le5\).
For \(m=25\) the values \(k=6,8,9,10,11,12\) admit respectively
\[
 (4,-1),(3,-1),(3,2),(5,0),(2,-3),(2,-1).
\]
For \(m=26\) the values \(k=6,7,8,9,11,12,13\) admit respectively
\[
 (4,-2),(4,2),(3,-2),(3,1),(2,-4),(2,-2),(2,0).
\]
This leaves precisely the two markings in the statement as candidates.
Both lifts for each candidate are congruent to the indicated first coordinate times the marked pair, and both have width seven.
One lift has opposite signs and one has equal signs, so their two pairs of extreme coefficients cover all four corners.

## Counting zero and additional parameters

For one listed lift set \(Q(z)=z^{-\min(0,a,b,a+b)}K(z)\), of prescribed width seven.
For \(z\ne0\) its nullity equals \(\nu(z)\).
Its maximal rank is two, and its rank at every \(m\)-th root is \(3/2\), by [the central lift and character twists](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter).
The projective-line evaluation bound counts zero and infinity together with these roots, as in the [order-26 endpoint argument](Yin_C_A0199_v1.md#the-two-extreme-coefficients-at-order-26).
Indeed a linear fractional change of variables in the homogenized polynomial takes all the selected points into a finite chart without changing the degree bound, ranks or maximal rank.
The total deficit is at most fourteen.
The specified roots contribute \(m/2>12\), so the two extreme coefficients cannot both have rank at most one.
Each is a single translation times a constant matrix, and a full endpoint is a unit over the group ring.
Use the reversed polynomial if necessary to put a full endpoint in leading position.

For this orientation let \(T\) be the monic companion in fourteen coordinates.
For every finite set \(E\) of distinct complex parameters containing the \(m\)-th roots let \(p(X)=\prod_{\lambda\in E}(X-\lambda)\).
Interpolation decomposes \(\ker p(T)\) into the eigenspaces at those parameters.
The [finite-support kernel-column argument](Yin_C_A0197_v1.md#the-companion-and-a-column-over-the-original-group-ring) applies to this square-free polynomial: if \(p(T)=0\), a complex interpolation polynomial in \(T\) projects onto the nonzero eigenspace at one.
A nonzero column gives a nonzero group-ring vector in the kernel of \(Q(1)\) via the companion shift equations.
Scalar injectivity makes the affiliated dimension of its generated column module one, contradicting nullity \(1/2\).
Thus \(p(T)\ne0\) has a nonzero group-ring entry, hence rank at least one.
Consequently the sum of the nullities at all selected parameters is at most thirteen.

Select zero as one additional parameter.
Its nullity is at most \(13-m/2<1\); since the constant coefficient has integer rank, it is also a unit over the group ring.
This works for the original or reversed orientation and both listed lifts, proving invertibility of all four corners.
For any finite set of nonzero additional parameters the same argument in the original orientation now bounds their total nullity by \(13-m/2\).
This is zero at order 26 and \(1/2\) at order 25.
In the latter case every nonzero parameter outside the prescribed roots has an orbit of 25 distinct additional parameters of equal rank under multiplication by the 25th roots, by the same character twists.
The individual bound follows.

## Consequence for finite abelian quotient orders

More generally any finite abelian quotient of order \(N\ge27\) or \(N=23\) excludes a half-dimensional increment by the [four-column equivalence](Yin_C_A0184_v1.md#statement).
For \(N>32\) and \(29\le N\le31\) use the [order bound](Yin_C_A0198_v1.md#statement); prime order 23 is [the cyclic case](Yin_C_A0197_v1.md#statement).
At \(N=28,32\) the [boundary lattice result](Yin_C_A0198_v1.md#the-two-boundary-orders) supplies either a strict short-lift bound or a lift with two nonzero weights and \(4d=m'\), where \(m'\) is the exponent of the quotient.
The [one-unit deficit improvement](Yin_C_A0197_v1.md#a-common-deficit-at-the-roots-of-unity) applies to that latter rectangle polynomial since its outer term is a single translation and all \(m'\)-th roots have nullity \(1/2\).
At order 27 the cyclic case is already covered.
A noncyclic two-generated abelian quotient of order 27 has exponent nine, and its [full character lattice](Yin_C_A0198_v1.md#the-lattice-of-all-finite-characters) has index \(9^2/27=3\).
Its shortest positive width is at most \(\lfloor\sqrt6\rfloor=2\), which gives \(4d<9\).
Thus a finite abelianization of a residual marked group must have order at most 26, with order 23 excluded.

## Assessment history

### Decision additional-nullities-at-orders-25-and-26

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Markings, all four corners and the parameter bounds. |
| argument | [Short directions in the two marked quotients](#short-directions-in-the-two-marked-quotients) | The two normalized lists of weights. |
| argument | [Counting zero and additional parameters](#counting-zero-and-additional-parameters) | Projective evaluations, spectral columns and the remaining deficit. |
| argument | [Consequence for finite abelian quotient orders](#consequence-for-finite-abelian-quotient-orders) | All finite abelian quotients of order 23 or at least 27. |
| review | [Additional nullities at orders 25 and 26](../audits/reviews/Yin_R_A0185_v1.md#additional-nullities-at-orders-25-and-26) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-additional-nullities-at-orders-25-and-26)
