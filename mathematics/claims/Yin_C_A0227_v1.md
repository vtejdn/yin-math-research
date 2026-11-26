---
author: Yin
---

# Split prime factors of the nonzero circulation norms at order 25

## Statement

Use the order-25 marking \(H=\langle s,t\rangle\), \(H_{\rm ab}=C_{25}\), with marked images \(1,7\), and let \(M_{25}\) be the twenty-fifth cyclotomic quotient of the commutator abelianization.
Let \(\mathcal P\) consist of the primes \(p>100000\), \(p\equiv1\bmod25\), dividing at least one **nonzero** [simple-cycle norm](Yin_C_A0225_v1.md#the-norm-calculation-and-the-cycles-descending-modulo-five).
There are 5426 such primes, with largest member \(2227495051\).
If \(M_{25}\) has a simple quotient with characteristic in \(\mathcal P\), then the regular nullity of
\[
                            K=B+At-s(D+Ct)
\]
is strictly below \(1/2\) for all invertible complex two-by-two corners with \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible.
The trace on matrix coordinates is unnormalized.
This finite-quotient implication does not need torsion-freeness or scalar group-ring injectivity.

Consequently every split prime \(p\) outside the [previously tested interval](Yin_C_A0219_v1.md#split-primes-and-a-strict-improvement-over-column-widths) has one of two properties.
The rank estimate applies as just stated if \(p\in\mathcal P\).
For \(p\notin\mathcal P\), no simple-cycle polynomial with nonzero cyclotomic norm vanishes at any primitive twenty-fifth root in \(\mathbb F_p\), by divisibility of the norm.
This latter property concerns the cycle evaluations; the finite matching computation here covers precisely the primes in \(\mathcal P\).

## Exact prime divisors and marked characters

Among the 92032 projection classes in the [cycle computation](../computations/programs/Yin_J_A0008/verify_cycle_norms.mjs), the nonzero norms take 10234 distinct positive integer values.
Their maximum is \(5314180901\).
The same verifier with the option `--split-exceptions` lists their distinct prime divisors by trial division using a sieve through the square root of that maximum.
Each successful division removes the whole prime power, and any remaining integer greater than one is prime once the next trial prime exceeds its square root.
There are 5931 different prime divisors altogether.
Intersecting with the two conditions defining \(\mathcal P\) yields the stated 5426 primes.
In particular this enumeration imposes no independent interval cutoff on a split prime factor of a nonzero norm.

At a simple quotient of characteristic \(p\in\mathcal P\), the multiplier of \(S=\operatorname{Ad}_s\) is a primitive twenty-fifth root in \(\mathbb F_p\).
For each inverse multiplier \(r\) and each \(1\le c<p\), the [marked character construction](Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit) realizes the exponents \(w_i=[cr^i]_{\rm cen}\) at all \(p\)-th roots of unity.
Here \(0\le i<25\) and the centered representative lies between \(-(p-1)/2\) and \((p-1)/2\).
Every choice of \(c\) is allowed because the nonzero module generator and the index shift are absorbed in the additive functional.
For each \(p\) the [exceptional-prime verifier](../computations/programs/Yin_J_A0008/verify_exceptional_split.py) obtains a root of order 25 and checks that its powers with unit exponents give twenty distinct roots of this order.
Thus all 108520 marked roots are included.
All modular powers, orbit weights and matching computations at these primes use Python integers.

## The finite endpoint certificates

For each root the verifier applies the [two-end computation](../computations/programs/Yin_J_A0008/verify_matching_spread.py) to positive multipliers in increasing order until it finds a certificate.
The available row offsets in input \(i\) are \(0,1,7,8\), of costs \(0,0,w_i,w_i\).
For the minimum \(L\) and maximum \(U\) it verifies feasible integer dual prices and an actual matching attaining equality.
The counts of first successful multipliers \(c=1,2,3,4\) were respectively \(101922,6354,240,4\).
The resulting values satisfy \(4(U-L)<25p\).
For at least one endpoint it also checks every strongly connected component of the tight arrows after identifying each matched row with its input.
The components are singleton loops or two-column components in which one column uses offsets \(0,1\) and the other uses \(7,8\) to reach the same two rows.
The [endpoint argument](Yin_C_A0217_v1.md#verifying-full-rank-away-from-zero) makes the diagonal blocks invertible: singleton blocks are translated corners, and a two-column block is a translated copy of the coefficient assembly with its block columns exchanged.
An invertible endpoint gives an injective specialization at a nonzero parameter.
By regular absorption and the [two-end interpolation theorem](Yin_C_A0219_v1.md#statement),
\[
                          25p\,\dim_H\ker K\ \le\ 2(U-L)<25p/2.
\]
The computation tests the full matched graph for each marked root even if only some cycle norms vanish on that root.

## Assessment history

### Decision split-divisors-of-nonzero-cycle-norms

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:09 |
| status | proved |
| reason | Independent proof review, a second reconstruction of all norms and complete reproduction verified the exceptional split markings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All split prime divisors above one hundred thousand and the stated rank implication. |
| argument | [Exact prime divisors and marked characters](#exact-prime-divisors-and-marked-characters) | The precise exceptional set, modular arithmetic and all twenty marked roots. |
| argument | [The finite endpoint certificates](#the-finite-endpoint-certificates) | The extremal costs, full specialization and all first successful multipliers. |
| review | [Split divisors of nonzero cycle norms](../audits/reviews/Yin_R_A0196_v1.md#split-divisors-of-nonzero-cycle-norms) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-split-divisors-of-nonzero-cycle-norms)
