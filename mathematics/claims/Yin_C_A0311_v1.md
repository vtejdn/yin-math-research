---
author: Yin
---

# Short characters at abelian quotient orders nineteen through twenty-two

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and suppose every nonzero element of \(\mathbb CH\) is regularly injective.
For a complex two-by-two four-site matrix \(K=B+At-s(D+Ct)\) of noninteger regular rank put \(\delta=\dim_H\ker K\), using the unnormalized coordinate trace.
For any abelian quotient \(Q\) of the indicated order one has
\[
\begin{array}{c|c}
 |Q|&\text{upper bound for }\delta\\ \hline
19&9/19\\
21&3/7\\
22&5/11 .
\end{array}
\]
Thus all three orders exclude regular rank \(3/2\).

At order 20 every marking gives \(\delta\le1/2\).
Only the following markings meet the half bound in the short-character inequalities, up to changing the quotient coordinates, inverting either generator and interchanging the generators.

* For \(Q=C_{20}\), the degrees are \((1,8)\), equivalently \((3,4)\) after multiplying the quotient coordinates by three.
  Every other marking gives \(\delta\le9/20\).
* For \(Q=C_5\times C_2^2\), the images are \((1,e_1),(2,e_2)\) for a basis \(e_1,e_2\) of \(C_2^2\).
  Every other marking gives \(\delta\le3/10\).

At a half kernel with either indicated quotient of order 20, \(H_{\rm ab}=Q\).
For the cyclic marking in coordinates \((1,8)\) the coefficient corners \(A,D\) are invertible and the deformation with weights \((1,-2)\) has zero nullity at every nonzero parameter outside \(\mu_{10}\).
For the noncyclic marking all four corners are invertible and the same zero-nullity assertion holds for both lifts \((1,2),(2,-1)\).
The short-character comparisons themselves give necessary conditions on these two residual markings.

## Character costs for a two-square rectangle

Write \(\mu_e\) for the \(e\)-th roots of unity.
Suppose a character of the quotient has marked weights \(a,b\bmod e\), meaning that its two values are \(\exp(2\pi i a/e),\exp(2\pi i b/e)\), and choose integers \(a,b\) not both zero.
Define
\[
              w=|a|+|b|,\qquad c(a,b)=2w-\mathbf1_{\{ab\ne0\}} .
\]
Then \(e\delta\le c(a,b)\).
Indeed the matrix of noninteger rank has a nonzero scalar entry, hence rank strictly between one and two by scalar injectivity.
The [integer-rank lift](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter) makes the generic rank of the deformation with phases \(z^a,z^b\) an integer at least this rank, so it is two.
At every \(e\)-th root the character twist preserves the rank.
The ordinary degree budget gives \(e\delta\le2w\).
For \(ab\ne0\) either extreme coefficient is a single group translation times a constant corner, including a possible zero corner.
If singular it consumes at least one unit of the budget at its own endpoint.
If invertible it has an inverse over the group ring and the [finite-support companion bound](Yin_C_A0197_v1.md#a-common-deficit-at-the-roots-of-unity) gives the same improvement.
The companion proof applies since \(0<\delta<1\).

In particular one may use a cyclic divisor \(e\) of a cyclic quotient order \(N\) before applying the one-unit improvement.
For example the lift \((3,-3)\) modulo 21 becomes \((1,-1)\) at the seven allowed phases; this gives \(7\delta\le3\).
When estimating \(c/e\), parameterizing the same seven phases with a triple power and counting 21 distinct parameters can lose part of this improvement.

## All cyclic markings

Suppose one marked residue in \(C_N\) is a unit.
Use it as the first generator after interchange, change the quotient generator to make its coordinate one, and invert the second label if necessary to obtain \((1,k)\) with \(0\le k\le\lfloor N/2\rfloor\).
These rectangle symmetries, including interchange by taking the adjoint and inverting the resulting labels, preserve the rank and permute the corners up to signs and adjoints. [Marking symmetries](Yin_C_A0196_v1.md#all-surjections-onto-the-quotient)

For \(0\le k\le4\) use \(e=N,(a,b)=(1,k)\), giving \(e\delta\le9\) in all cases.
The following table gives all remaining witnesses, listed in increasing order of \(k\).
Each entry is \((e;a,b)\) and satisfies \(e\mid N,\ b\equiv ka\bmod e\), so the root twists are genuine.
Thus the table can be checked by substituting in \(c(a,b)\).

| \(N\) | \(k\) | Witnesses in order |
| --- | --- | --- |
| 19 | \(5,\ldots,9\) | \((19;4,1),(19;3,-1),(19;3,2),(19;2,-3),(19;2,-1)\) |
| 20 | \(5,\ldots,10\) | \((5;1,0),(20;3,-2),(20;3,1),(10;1,-2),(10;1,-1),(10;1,0)\) |
| 21 | \(5,\ldots,10\) | \((21;4,-1),(7;1,-1),(7;1,0),(7;1,1),(21;2,-3),(21;2,-1)\) |
| 22 | \(5,\ldots,11\) | \((11;2,-1),(11;2,1),(22;3,-1),(22;3,2),(11;1,-2),(11;1,-1),(11;1,0)\) |

If neither residue is a unit, \(N\) cannot be prime.
For \(N=20,21,22\) respectively take \(p=5,7,11\).
Since \(N\) has just two distinct prime divisors, a generating pair of nonunits must have one member divisible by \(p\) and the other prime to \(p\).
Reducing modulo \(p\) and rescaling the remaining nonzero residue gives an axial lift of width one, hence \(\delta\le2/p\).
These comparisons give the cyclic bounds and the single residual normalization stated above.

## The noncyclic quotient of order twenty

Orders 19, 21 and 22 are square-free, hence every abelian group of each such order is cyclic.
At order 20 the other possible type is \(Q=C_5\times C_2^2\).
The binary parts of the two marks form a basis.
Write their order-five coordinates as \(a_0,b_0\), which are not both zero.
After interchange and rescaling take \(a_0=1\); one may invert the second generator independently without changing its binary part.
Thus \(b_0=r\) with \(r=0,1\) or 2 in \(\mathbb F_5\).
The full lattice of lifts at exponent ten is
\[
                        \{(a,b)\in\mathbb Z^2:\ b\equiv ra\bmod5\}.
\]
Indeed all characters in the order-five coordinate give exactly this slope modulo five; identifying \(\mu_5\) inside \(\mu_{10}\) multiplies both exponents by two, a unit modulo five.
The two binary signs give unrestricted residues modulo two, independently of those modulo five.
For \(r=0,1\) the lifts \((1,0),(1,1)\) give the two upper bounds \(2/10,3/10\).
For \(r=2\) both \((1,2)\) and \((2,-1)\) give \(c=5\).

For completeness, in the two remaining markings the minimum costs among all nonzero lifts, before division by \(e\), are
\[
\begin{array}{c|c|c}
 \text{marking}&e&\min c\\ \hline
 C_{20},(1,8)&2,4,5,10,20&2,2,5,5,10\\
 C_5\times C_2^2,\ r=2&2,5,10&2,5,5 .
\end{array}
\]
For the first row minimize \(2(|a|+|b|)-\mathbf1_{\{ab\ne0\}}\) subject to \(b\equiv8a\bmod e\).
For the second row the congruence for \(5\mid e\) is \(b\equiv2a\bmod5\), and at \(e=2\) there is no constraint.
For an elementary check one may run \(0\le a\le\lfloor e/2\rfloor\), take \(b\) of least absolute value permitted, and also check the pure axes.
At \(e=20\), for instance, \(|a|=1,2,3,4\) requires \(|b|=8,4,4,8\) respectively, whereas \((5,0)\) realizes cost ten.
A nonzero lift of the trivial character outside the centered box has width at least \(e\) and cannot lower these minima.
More generally if some weights describe the same character family at a larger parameter order, divide by the common divisor of that order and both weights.
The two costs then scale linearly except for the single unit subtracted at a mixed endpoint, which gives an at least as strong bound after division.
Thus the indicated boundaries really do survive the short-character inequalities.

## The two ends in the equality case

In each surviving mixed lift at exponent ten the degree after shifting is three, with both extreme sites single corners.
At a half kernel the ten twists use five units of the degree budget of six.
Both endpoints cannot be singular: applying the rank budget on the projective line at the ten roots, zero and infinity would use at least seven units. [Simultaneous endpoint count](Yin_C_A0201_v1.md#counting-zero-and-additional-parameters)
An invertible endpoint supplies a monic degree-three companion, reversing the parameter if required.
For any finite set of distinct parameter values containing the ten roots, its square-free annihilating polynomial on the companion cannot be zero: the interpolation projection for any of these roots would have a nonzero group-ring column in a half-dimensional eigenspace.
Therefore the complement of the sum of the corresponding eigenspace dimensions has dimension at least one, by scalar injectivity on a nonzero group-ring entry.
The combined eigenspaces have dimension at most five, already exhausted by the ten roots.
In particular zero gives no kernel at the opposite endpoint, and every nonzero parameter outside those roots has zero nullity, as in the [companion argument](Yin_C_A0201_v1.md#counting-zero-and-additional-parameters).
For \((1,-2)\) the extreme corners are \(A,D\).
For \((1,2)\) they are \(B,C\), and for \((2,-1)\) they are \(A,D\).
This gives exactly the asserted invertibilities.

Finally, an abelianization properly covering an order-20 quotient either has finite order at least 40 or is infinite and finitely generated, hence has arbitrarily large cyclic quotients.
Both possibilities violate the [upper order bound](Yin_C_A0201_v1.md#consequence-for-finite-abelian-quotient-orders) at a half kernel.
Thus each remaining order-20 quotient map is the abelianization followed by an isomorphism.

## Assessment history

### Decision short-characters-at-orders-nineteen-through-twenty-two

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:55 |
| status | proved |
| reason | The character costs give the three strict bounds, the two remaining order-20 markings and the restrictions at both ends of the extremal deformations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The three strict bounds and the necessary conditions at order twenty. |
| argument | [Character costs for a two-square rectangle](#character-costs-for-a-two-square-rectangle) | Rank loss per character, including common divisors. |
| argument | [All cyclic markings](#all-cyclic-markings) | All cyclic marked pairs and their cost witnesses. |
| argument | [The noncyclic quotient of order twenty](#the-noncyclic-quotient-of-order-twenty) | The five-primary slope, the two independent signs, and minimum costs. |
| argument | [The two ends in the equality case](#the-two-ends-in-the-equality-case) | The six-coordinate companion and the original corner ranks. |
| review | [Short characters at orders nineteen through twenty-two](../audits/reviews/Yin_R_A0218_v1.md#short-characters-at-orders-nineteen-through-twenty-two) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-short-characters-at-orders-nineteen-through-twenty-two)
