---
author: Yin
---

# An index-two character, analytic rank and the second Schur coefficient

A separate reviewing agent inspected the fixed C_A0037_v1 for Yin on 2026-11-16T17:54 UTC.
The reviewer did not participate in the development of this Claim and received or consulted no C_A0037 proof-development dialogue, author explanation or previous verdict.
The reviewer previously helped develop the fixed coefficient chart in C_A0035 and the cyclic-coset result used by the older four-point bound.
Those earlier results are inputs at their established scopes.
This review independently checks their use in C_A0037 and its new symbolic example calculation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0037_v1.md#statement) | Index-two anti-invariant height, the strict and tied width cases, rank bounds, exact half-rank criterion and finite algebraic locus. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0037_v1.md#argument) | Restriction trace, circle-generic rank, row and column exponents, ordered Schur series, disk argument and finite truncation. |
| [Whole-argument finding](#whole-argument-finding) | [Tied leading face](../../claims/Yin_C_A0037_v1.md#what-a-tied-leading-face-detects) | Group and scalar endpoint identities, binomial injectivity, and use of the strict four-point rank gap. |
| [Whole-argument finding](#whole-argument-finding) | [Second coefficient](../../claims/Yin_C_A0037_v1.md#the-second-coefficient-on-the-actual-twelve-row-support) | Both supports' endpoint tests and the complete degree-two rank certificate for the row support. |
| [Whole-argument finding](#whole-argument-finding) | [Vandermonde estimate](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Countable exceptional set for unnormalized rank of a one-parameter finite matrix polynomial with bounded operator coefficients. |
| [Whole-argument finding](#whole-argument-finding) | [Four-point rank](../../claims/Yin_C_A0027_v1.md#four-point-rank) | Strict gap above \(1/2\) for nonzero sums on at most four points in a torsion-free group. |
| [Whole-argument finding](#whole-argument-finding) | [Binary coefficient chart](../../claims/Yin_C_A0035_v1.md#the-true-fibers-and-all-binary-solutions) | Original-first indexing, parameter coordinates and both coefficient vectors in formula (4). |
| [Whole-argument finding](#whole-argument-finding) | [Heisenberg sign representation](../../ledger/Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation) | Faithfulness, group generators and the central coordinate of \((XY)^2\). |

## Whole-argument finding

Since conjugation by \(t^2\) is inner on \(H\), every character of \(H\) is invariant under the square of \(\sigma\).
The symmetrized character therefore extends rationally as stated, proving the anti-invariance assertion when \(K_{\rm ab}\) is finite.
The sign rule forces zero degree for \(t^2\).
Multiplying the two right-module basis vectors by \(u+tv\) gives the two printed columns, with \(t^2\sigma(v)\) in the upper-right position.
The restriction doubles the trace on the range projection since the two scalar diagonal coefficients at the coset representatives agree by right translation.

The twist and scalar row and column rescalings preserve rank on the entire unit circle.
The cited Vandermonde argument applies to the rescaled polynomial matrices and all subsequent polynomial evaluations with bounded group-ring coefficients.
Its estimate for finite subsets bounds the sum of the drops from supremum, so even an uncountable subset of the circle or an open disk contains a point of maximum rank.
In the strict first-width case the two off-diagonal minimal exponents after doubling are \(2\alpha+k-2\beta\) and \(2\delta-k-2\gamma\).
The chosen integer makes both positive and both diagonal minimal exponents zero.
The two diagonal values give the claimed bound by trace-preserving conjugation.
After switching columns the same reasoning covers the other width.

In the tied case the pivot's constant term is invertible in the group ring, where the recurrence computes the *right* quotient coefficient in \(EA=C\) with the stated order.
After eliminating through degree \(j\), dividing the new lower row by \(s^j\) yields a polynomial matrix whose lower-left entry vanishes at zero and whose lower-right entry there is \(S_j\).
At zero an invertible column operation kills the upper-right entry, giving rank \(1+r_H(S_j)\).
All row operations preserve the circle ranks because \(s\ne0\) on the circle.
Conversely, vanishing of all coefficients forces the Schur complement to vanish in a disk by convergence of the inverse around the bounded invertible pivot.
On this disk the pre-elimination polynomial matrix has rank one, so its maximum rank is one, using the countable-exception argument on that matrix itself.
No evaluation of the formal inverse on the circle is required.

Every Laurent coordinate of each \(S_j\) is computed from finitely many group products and an inverse monomial at the fixed pivot.
Noetherianity bounds the needed prefix because the whole ideal is generated by a finite subset of those coordinates.
This justifies the semidecision of emptiness with the stipulated effective group arithmetic and coefficient-family data.
It gives no computable stopping rule merely from consecutive equal truncation ideals.
For monomial endpoints, conjugation of the two group labels in \(S_0\) gives exactly the displayed ordered four-element identity, and the scalar equality balances the products of endpoint coefficients.
Distinct labels give an injective binomial when \(H\) is torsion-free by restriction to the infinite cyclic subgroup generated by the relative group element.
The two strictly winning small faces invoke the four-point estimate under its torsion-free hypothesis.

For the example the reviewer used the [original group words and exact multiplication law](../../computations/programs/Yin_J_A0003/verify.py), appended the four exterior translates on each side in the C_A0035 order and formed the four matrix blocks separately.
The sign \(i\) multiplies under the group law, the coordinate \(p\) is additive on \(i=1\), and conjugation by \(Y\) negates it there.
The four maximum heights in the row matrix, in block order \(A,B,C,D\), are \(1,1,2,2\), with indices \(2,5,11,10\).
For the column matrix they are \(0,3,0,3\), with indices \(1,11,5,10\).
Direct multiplication of the constant Schur terms gives zero on both sides after substitution from formula (4).

The reviewer independently multiplied group-ring elements with symbolic Laurent coefficients, collecting at each five-coordinate integer group label.
Computing the ordered series through degree two directly from the original four blocks, before the suggested column simplification, gives \(E_0=bL\) and the terms \(aJ\) and \(-abxz/y^2\) of \(E_1\).
The row residuals at orders zero and one vanish.
At order two the coefficients at \(h^{-1},1,h\), respectively, are
\[
 -ax/y-y^4/(x^2z^2),\quad
 1+abz/y+ay^3/(xz^2)+b^2y^4/(x^2z^2),\quad
 -b^2-aby^3/(x^2z).
\]
There are no other group labels at that order.
The infinite order of \(h\) makes every nonzero such Laurent polynomial injective by Fourier transform on its cyclic subgroup and restriction to cosets.
The value at all parameters one, the positivity exclusion and the vanishing at the stated point with \(a=-1\) follow from these coefficients.
The faithful finite-sign extension of the integer Heisenberg group also confirms that the particular torsion-free example is already in an elementary amenable class covered by the known complex Atiyah theorem.

The proof supports the stated rank bounds, equivalence, finite-locus result and actual computation at their specified hypotheses.
No new whole-proof review of the earlier coefficient chart, the general finite-support rank gap, or the universal Atiyah conjecture is implied.
