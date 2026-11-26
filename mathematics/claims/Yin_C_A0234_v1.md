---
author: Yin
---

# Matching bounds for the large split norm factors at cyclic order twenty-six

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{26}\) marked by \(1,10\), and put \(M=H'/H''\), \(S=\operatorname{Ad}_s\).
Suppose \(M/\Phi_{26}(S)M\) has a simple quotient of characteristic \(p>725546\), with \(p\equiv1\bmod26\), dividing some nonzero primitive cycle norm in the [twenty-six-channel cycle computation](../computations/programs/Yin_J_A0009/verify_phi26_cycles.mjs).
Suppose \(A,B,C,D\) are invertible complex two-by-two matrices and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) is invertible.
Then, with the unnormalized matrix trace,
\[
       \dim_H\ker\bigl(B+At-s(D+Ct)\bigr)
             \ \le\ \frac{4304409}{9573187}<\frac9{20}<\frac12 .
\]
This finite implication requires neither torsion-freeness nor scalar group-ring injectivity.

## All twelve marked roots at each norm divisor

The [exceptional-prime verifier](../computations/programs/Yin_J_A0009/verify_phi26_exceptional_split.py) consumes the sorted prime list produced by the cycle computation's split-exception option.
That computation factors the 1957 distinct nonzero primitive norms and selects their prime divisors above 725546 congruent to one modulo thirteen.
At odd primes this congruence is equivalent to \(p\equiv1\bmod26\).
There are twenty such primes, from 736399 to 1799617.
The verifier checks primality and distinctness, and its search in \(\mathbb F_p^\times\) checks that a starting root has thirteenth power \(-1\) and square different from one.
Its powers at the twelve units modulo 26 exhaust the primitive roots, which the program verifies individually.

Since \(H'\) has finite index, \(M\) is finitely generated abelian.
The map \(S-I\) is surjective on \(M\), since killing \([H,H']\) makes the group central-by-cyclic and hence abelian.
Consequently \(S-I\) is invertible on \(M\), so the \(S\)-fixed class of \(s^{26}\) is zero.
The metabelian quotient splits as \(M\rtimes C_{26}\) and \(ts^{-10}\) generates \(M\) as a cyclic module. [Split marking argument](Yin_C_A0230_v1.md#simple-quotients-and-their-marked-characters)
A simple module at one of these primes is \(\mathbb F_p\) with inverse multiplier \(r\) equal to one of the twelve roots.
For any nonzero \(c\bmod p\), the exponents \(cr^i\) are realized by the additive character of this field with an appropriate nonzero scalar absorbing the image of \(ts^{-10}\) and the index shift by ten.
With \(P\) the cyclic forward shift, at every \(z^p=1\) there is therefore an actual representation
\[
                     s\longmapsto P,\qquad
                     t\longmapsto P^{10}\operatorname{diag}(z^{w_i}),
                     \qquad w_i\equiv cr^i\bmod p .
\]
This is the [marked representation formula](Yin_C_A0210_v1.md#a-representation-test-for-a-single-finite-character) with orbit length 26.

## A change at one coordinate and both matching costs

For each root the verifier tries \(1\le c\le12\) in order.
It takes the centered representatives of \(cr^i\) for \(0\le i<26\) and changes only \(w_0\), first adding \(p\) and then, in a separate trial, subtracting \(p\).
This preserves the representations at all \(p\) phases even though the integral exponents can lose antipodal symmetry.
At input \(i\) the offsets \(0,1,10,11\) have costs \(0,0,w_i,w_i\), respectively.
For the two extreme costs \(L,U\) the verifier checks actual permutations and integer dual prices satisfying every edge inequality, with equality on the matched edges.
After identifying the matched rows with their inputs, it computes the mutually reachable components of the tight graph.
At least one extremum must have only singletons and two-column components in which both inputs reach the same two rows, with offsets \(0,1\) from one and \(10,11\) from the other.
The associated endpoint is block triangular with translated invertible corners on its singleton blocks.
After permutation each two-column diagonal block is \(\operatorname{diag}(I,-sI)\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\operatorname{diag}(tI,I)\), hence invertible.
The gauges for that endpoint give an injective specialization at a nonzero parameter by norm continuity. [Endpoint argument](Yin_C_A0217_v1.md#verifying-full-rank-away-from-zero)

For the very same \(c,w_0\), the verifier requires \(40(U-L)\le9\cdot26p\).
If \(\delta\) is the original nullity, regular absorption gives \(26\delta\) at each of the \(p\) phases and the [two-end matching bound](Yin_C_A0219_v1.md#statement) gives \(26p\delta\le2(U-L)\).
The [complete computation](../computations/programs/Yin_J_A0009/readme.md#large-split-norm-divisors-on-twenty-six-channels) covers 240 markings.
The counts of the first successful \(c\) for \(c=1,\ldots,12\) are \(84,38,54,18,22,8,10,2,0,2,0,2\).
The largest value of \(2(U-L)/(26p)\) over the first certificates is \(4304409/9573187\), attained at \(p=736399\) and \(r=375441\).

## Assessment history

### Decision the-twenty-exceptional-split-primes

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:44 |
| status | proved |
| reason | Independent review and complete recomputation verified every marked root, the changed lifts and both endpoint certificates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The precise prime set and quantitative rank bound. |
| argument | [All twelve marked roots at each norm divisor](#all-twelve-marked-roots-at-each-norm-divisor) | All primitive roots at all twenty exceptional primes. |
| argument | [A change at one coordinate and both matching costs](#a-change-at-one-coordinate-and-both-matching-costs) | Phase preservation and extremal matching costs for the same tested lift. |
| review | [The twenty exceptional split primes](../audits/reviews/Yin_R_A0198_v1.md#the-twenty-exceptional-split-primes) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-twenty-exceptional-split-primes)
