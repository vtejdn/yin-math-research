---
author: Yin
---

# The finite quadratic interval through 2300650 at the critical order-25 marking

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{25}\) marked by \(1,7\).
Write \(N=[H,H]\), \(M=N_{\rm ab}\), and \(S=\operatorname{Ad}_s\) on \(M\).
Suppose \(M/\Phi_{25}(S)M\) has a simple quotient of characteristic \(p\equiv-1\bmod25\) with \(p\le2300650\).
For two-by-two complex matrices \(A,B,C,D\) with each corner and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible, the regular nullity of \(K=B+At-s(D+Ct)\) is strictly less than \(1/2\) in the unnormalized matrix trace.
This conclusion uses no scalar injectivity or torsion assumption.
It covers all ten irreducible quadratic factors at each of 8441 primes, including the [previous finite interval](Yin_C_A0221_v1.md#statement).

## Extension of the quadratic certificate

It suffices to treat \(100000<p\le2300650\).
The [quadratic trace enumeration](Yin_C_A0221_v1.md#enumerating-the-marked-quadratic-traces) produces the ten distinct values \(v=\alpha+\alpha^{-1}\) for primitive twenty-fifth roots and checks their exact orders.
For a chosen initial pair \((e_0,e_1)\), the recurrence \(e_{i+2}=v e_{i+1}-e_i\) modulo \(p\) computes an actual additive character on the powers of \(\alpha\).
The period check and the two matching costs use the same integer routines as in the [earlier quadratic scan](Yin_C_A0221_v1.md#both-matching-costs-for-the-ten-traces).
At each marking the [finite interval verifier](../computations/programs/Yin_J_A0008/verify_quadratic_remainder.py) tests the initial pairs in the order recorded in the [computation](../computations/programs/Yin_J_A0008/readme.md#quadratic-markings-through-2300650).
A success certifies a lower matching cost \(L\), an upper matching cost \(U\), the two dual feasibility inequalities with matched equalities, and an invertible lower or upper endpoint by the strongly connected component test.
It verifies \(4(U-L)<25p\) at that same marking and for the same initial pair.
The [two-end interpolation theorem](Yin_C_A0219_v1.md#statement) then gives \(25p\dim_H\ker K\le2(U-L)\).
Since both costs are integers, this also gives \(\dim_H\ker K\le1/2-1/(50p)\).

Direct trial division checks every residue \(24\bmod25\) in the new interval.
There are 7978 primes, from 100049 to 2300399, and 79780 marked quadratics.
For the five initial pairs \((1,1),(2,1),(3,1),(2,3),(3,4)\), the respective first-success counts are \(39228,39193,1304,54,1\).
The verifier prints the unique prime and trace requiring the fifth pair and checks that all ten traces at every prime have a successful certificate.
Together with the earlier 463 primes and 4630 marked traces this proves the statement.

## Assessment history

### Decision the-full-exceptional-quadratic-interval

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:09 |
| status | proved |
| reason | Independent review and full reproduction verified the finite range and the regular-rank inference at every marked trace. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every quadratic characteristic through the cutoff and the coefficient hypotheses. |
| argument | [Extension of the quadratic certificate](#extension-of-the-quadratic-certificate) | Initial values, both assignment certificates, the exceptional fifth pair and the integral gap. |
| review | [The full exceptional quadratic interval](../audits/reviews/Yin_R_A0196_v1.md#the-full-exceptional-quadratic-interval) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-full-exceptional-quadratic-interval)
