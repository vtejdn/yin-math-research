---
author: Yin
---

# Coupled order-25 character orbits at four residual primes

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{25}\) with marked images \(1,7\).
Put \(N=[H,H]\), \(M=N_{\rm ab}\), and \(M_{25}=M/\Phi_{25}(S)M\), where \(S\) acts by conjugation by \(s\).
Suppose \(M_{25}\) has a simple module quotient of characteristic \(p\in\{7,43,101,149\}\).
For each rectangle \(K=B+At-s(D+Ct)\) with all four complex two-by-two corners and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible, the regular nullity with unnormalized matrix trace satisfies
\[
                           \dim_H\ker K\le 236/505 < 1/2 .
\]
The bound applies to every possible irreducible marked factor at these primes, without torsion-freeness or scalar injectivity in this quantitative assertion.
Consequently, for a torsion-free group with regular scalar injectivity, a rectangle of rank \(3/2\) requires \(\gcd(|M|,7\cdot43\cdot101\cdot149)=1\).
This removes one prime from each of the four [residue classes left by the independent-slice test](Yin_C_A0216_v1.md#the-remaining-prime-divisors).

## Characters from a single coupled orbit

Use the [cyclic module construction](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module): \(M\rtimes C_{25}\) is an actual quotient with lift \(s\) of order 25, and \(u=ts^{-7}\) generates \(M\) over \(\mathbb Z[S]\).
On a simple quotient at characteristic \(p\), the dual orbit lists can be written \(e_i=\lambda(\alpha^i)\) for any \(\mathbb F_p\)-linear functional on \(\mathbb F_p(\alpha)\), where \(\alpha\) is the inverse of the multiplier of \(S\).
Indeed the nonzero factor from \(u\) and the index shift are absorbed into the functional in the [marked orbit formula](Yin_C_A0216_v1.md#orbit-coordinates-on-the-five-slices).
Writing \(P e_i^{\rm std}=e_{i+1}^{\rm std}\) modulo 25, each list gives the representations \(s\mapsto P,\ t\mapsto P^7\operatorname{diag}(w^{e_i})\) for all \(w^p=1\).

Let \(F(X)=\sum_{j=0}^{d}F_j X^j\) be the monic minimal polynomial of \(\alpha\), a factor of \(\Phi_{25}\bmod p\).
For any initial vector of length \(d\) prescribe the values of \(\lambda\) on the basis \(1,\alpha,\ldots,\alpha^{d-1}\).
The entire length-25 list is then determined by
\[
                    e_{i+d}=-\sum_{j<d}F_j e_{i+j}\quad\bmod p .
\]
Thus the exponents used below belong to a single marked orbit; the five slices need not be independently specifiable.

For each factor the [integer verifier](../computations/programs/Yin_J_A0008/verify_coupled.py) gives an initial vector and an integer \(a\in\{0,1\}\).
Take \(z^{25p}=1\), \(w=z^{25}\), and multiply the preceding representation by the cyclic character with values \(z^{ap},z^{7ap}\).
This gives
\[
               s\longmapsto z^{ap}P,\qquad
               t\longmapsto P^7\operatorname{diag}(z^{b_i}),
\]
where \(b_i\) is the centered integer representative of \(7ap+25e_i\bmod25p\).
All \(25p\) different parameter values are legitimate even when \(a=0\) and some representations repeat.
In each two-column input block \(i\) the offsets \(0,1,7,8\) have coefficients \(B,-sD,At,-sCt\), respectively, and exponents \(0,ap,b_i,ap+b_i\).
Stripping the minimum in each column gives total column degree at most \(2W\), where \(W=25|a|p+\sum_i|b_i|\).

## Verifying full rank away from zero

For each certificate write \(w_{ji}\) for the exponent of an allowed arrow from input \(i\) to row \(j\).
The verifier produces an input \(i(j)\) matched to every row and integer prices \(u_i,v_j\).
It checks directly that the matching is bijective, \(u_i+v_j\le w_{ji}\) for every allowed arrow, and equality holds on every matched arrow.
No correctness assumption on the algorithm for finding those integers is needed.
Multiplication by the row powers \(z^{-v_j}\) and column powers \(z^{-u_i}\) therefore gives a polynomial matrix whose value at zero has precisely the equality arrows.

Identify each row with its matched input and partition this directed graph by mutual reachability.
The verifier checks that all components are singletons or pairs.
For pairs it checks that all four arrows survive: the offsets from one input are \(0,1\), and those from the other are \(7,8\), with the same pair of adjacent output rows.
Ordering the components gives a block triangular matrix.
Its diagonal blocks are individual invertible corners times group translations and, after a block permutation, copies of
\[
 \begin{pmatrix}At&B\\-sCt&-sD\end{pmatrix}
  =\operatorname{diag}(I_2,-sI_2)
    \begin{pmatrix}A&B\\ C&D\end{pmatrix}
    \operatorname{diag}(tI_2,I_2).
\]
The constant value in this choice of row and column powers is consequently boundedly invertible.
By norm continuity it stays invertible at some nonzero complex parameter.
There the earlier column-degree normalization, which determines \(W\), has the same full rank.
These two normalizations have different purposes and can use different powers.

## Factor coverage and numerical bounds

| \(p\) | Degree of each factor | Number of factors | Maximum \(W\) |
| --- | --- | --- | --- |
| 7 | 4 | 5 | 959 |
| 43 | 4 | 5 | 5925 |
| 101 | 1 | 20 | 14750 |
| 149 | 2 | 10 | 21100 |

The verifier checks that the listed monic polynomials have product \(\Phi_{25}=1+X^5+X^{10}+X^{15}+X^{20}\) in \(\mathbb F_p[X]\) and that the degrees in the table equal \(\operatorname{ord}_{25}(p)\).
Since \(X^{25}-1\) is separable at these primes, all primitive roots have Frobenius orbit of precisely that degree.
Thus every listed polynomial is irreducible and every possible factor is included, including inverses of generator roots.
At \(p=101\) the initial value one and \(a=0\) work for all twenty primitive roots; distinct roots can give different equality graphs.
For example, the factor \(X^4+4X^3+3X^2+4X+1\) at \(p=7\) uses \((0,0,4,1)\) and \(a=1\).
The remaining exact inputs and the checks on widths and blocks are recorded in [J_A0008](../computations/programs/Yin_J_A0008/readme.md#coupled-orbits-at-four-primes).

At each of the \(25p\) roots the absorbed representation has nullity \(25\dim_H\ker K\).
The [column-degree bound](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) now gives \(\dim_H\ker K\le2W/(625p)\).
The four respective bounds are \(1918/4375,\ 11850/26875,\ 236/505,\ 42200/93125\), all at most \(236/505\).

For a rank-\(3/2\) rectangle under torsion-freeness and scalar injectivity, the [corner](Yin_C_A0201_v1.md#statement) and [constant matrix](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) hypotheses follow.
The [preceding exclusions](Yin_C_A0216_v1.md#the-remaining-prime-divisors) give finite \(M=M_{25}\).
If its order were divisible by one of the four primes, \(M/pM\) would supply a simple quotient just tested.
This proves the stated restriction while leaving the other primes in those residue classes open.

## Assessment history

### Decision coupled-character-orbits-at-four-primes

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:36 |
| status | proved |
| reason | Independent proof review and finite reproduction established the stated uniform bound for every marked factor. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All four residual primes and the half-rank consequence. |
| argument | [Characters from a single coupled orbit](#characters-from-a-single-coupled-orbit) | The marked quotient, orbit recurrence, genuine twists and column widths. |
| argument | [Verifying full rank away from zero](#verifying-full-rank-away-from-zero) | Integer prices, tight components and the order of the group factors. |
| argument | [Factor coverage and numerical bounds](#factor-coverage-and-numerical-bounds) | All forty factors and the common upper bound. |
| review | [Coupled character orbits at four primes](../audits/reviews/Yin_R_A0193_v1.md#coupled-character-orbits-at-four-primes) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-coupled-character-orbits-at-four-primes)
