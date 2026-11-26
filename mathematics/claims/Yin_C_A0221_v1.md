---
author: Yin
---

# Quadratic order-25 characters through one hundred thousand

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{25}\) with marked images \(1,7\); put \(N=[H,H]\), \(M=N_{\rm ab}\), and \(M_{25}=M/\Phi_{25}(S)M\) for \(S=\operatorname{Ad}_s\).
Suppose \(M_{25}\) has a simple module quotient of characteristic \(p\equiv24\bmod25\) with \(p\le100000\).
Then any four-site matrix \(K=B+At-s(D+Ct)\) with invertible complex two-by-two corners and invertible assembled block \(\left(\begin{smallmatrix}B&A\\ D&C\end{smallmatrix}\right)\) has regular nullity strictly below \(1/2\), with unnormalized matrix trace.
The bound covers all ten marked irreducible quadratics at each of the 463 such primes; it does not assume torsion-freeness or scalar injectivity.

Consequently, if \(H\) is torsion-free with regular scalar group-ring injectivity and \(K\) has rank \(3/2\), then every prime divisor \(p\) of the finite commutator abelianization \(M\) satisfies one of
\[
 \begin{array}{ll}
 p\equiv1\bmod25, & 100000<p<18^{20},\\
 p\equiv24\bmod25, & 100000<p<18^{10}.
 \end{array}
\]
In particular the lower cutoff concerns every prime divisor, including those in the split class; it does not assert the existence of any prime divisor.

## Enumerating the marked quadratic traces

For \(p\equiv-1\bmod25\), each primitive twenty-fifth root \(\alpha\) lies in \(\mathbb F_{p^2}\) with \(\alpha^p=\alpha^{-1}\), and its minimal polynomial is \(X^2-vX+1\) with \(v=\alpha+\alpha^{-1}\in\mathbb F_p\).
There are ten distinct traces for the twenty primitive roots, since the trace determines the unordered pair of roots of this quadratic.
Define \(T_0(y)=2,\ T_1(y)=y,\ T_{k+2}(y)=yT_{k+1}(y)-T_k(y)\).
For any nonzero \(\xi\), \(T_k(\xi+\xi^{-1})=\xi^k+\xi^{-k}\).
The [integer verifier](../computations/programs/Yin_J_A0008/verify_quadratic_spread.py) searches residues \(y\bmod p\) for \(v=T_{(p+1)/25}(y)\) satisfying \(T_{25}(v)=2,\ T_5(v)\ne2\).
The test certifies that a root of \(X^2-vX+1\) has order exactly 25, because \(x+x^{-1}=2\) is equivalent to \(x=1\) in a field.
For existence one may take \(y=\xi+\xi^{-1}\) for a generator of the norm-one subgroup of \(\mathbb F_{p^2}^\times\), which has order \(p+1\).
The values \(T_k(v)\) for \(1\le k\le12\), \(5\nmid k\), give every such quadratic trace since these \(k\) exhaust units modulo 25 up to sign.
The program verifies distinctness and both order tests on all ten outputs.

For the given simple quotient use the [marked orbit construction](Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit).
An \(\mathbb F_p\)-linear functional on the quadratic field can take any specified initial values \((e_0,e_1)\) on the basis \((1,\alpha)\).
Its values \(e_i\) on successive powers of \(\alpha\) satisfy \(e_{i+2}=v e_{i+1}-e_i\bmod p\).
The inverse generator and the scalar from \(ts^{-7}\) are accounted for in the orbit formula; inversion also preserves each quadratic trace.
For any \(p\)-th root of unity \(z\) the assignment \(s\mapsto P,\ t\mapsto P^7\operatorname{diag}(z^{w_i})\) is therefore an actual representation on 25 coordinates, where \(P\) is the cyclic forward shift and \(w_i\) is the centered integer representative of \(e_i\).
There is no additional scalar character twist.

## Both matching costs for the ten traces

The exponents of the four block entries from input \(i\) at row offsets \(0,1,7,8\) are \(0,0,w_i,w_i\), respectively.
The corresponding group-weighted corners are \(B,-sD,At,-sCt\).
Let \(L\) and \(U\) be the minimum and maximum matching costs on these 25 rows and columns.
As in the [two-end matching theorem](Yin_C_A0219_v1.md#statement), the verifier checks exact integer dual prices and a tight perfect matching separately for the original and negated costs.
At least one extremum must give an invertible specialization.
For this test it identifies matched rows with their inputs and checks the mutually reachable components of the tight graph.
A singleton gives an invertible corner times a group translation.
For each pair it checks both possible offsets from each column: these are \(0,1\) from one and \(7,8\) from the other, to the same pair of adjacent output rows.
After permutation the block is \(\operatorname{diag}(I,-sI)\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\operatorname{diag}(tI,I)\).
Thus a tight graph consisting only of these components gives a block triangular invertible evaluation at zero after the appropriate row and column gauges, reversing the parameter first in the maximum-cost case.
Invertibility persists near zero, giving the needed nonzero parameter for the original pencil.

The program tries \((1,1),(2,1),(3,1),(2,3)\) as initial values in that order.
For each success the matching spread obeys \(4(U-L)<25p\).
Absorption multiplies the original nullity \(\delta\) by 25 at each of the \(p\) true phases, so [interpolation with separate output degrees](Yin_C_A0219_v1.md#interpolation-with-different-output-degrees) gives \(25p\delta\le2(U-L)\), proving strict exclusion.
In the [executed check](../computations/programs/Yin_J_A0008/readme.md#quadratic-matching-spread-through-one-hundred-thousand) there were 463 primes and 4630 marked traces.
The counts for the first successful initial pair were respectively 2267, 2283, 78 and 2.
The result is restricted to the indicated finite interval.

## Bounds on remaining primes

In the torsion-free scalar-injective half-rank setting, the [four-corner test](Yin_C_A0201_v1.md#statement) and [assembled block test](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) apply.
The [subgroup and size reductions](Yin_C_A0218_v1.md#numerical-consequence-for-the-twenty-fifth-component) give \(M=M_{25}\) with \(|M|<18^{20}\), and the [quartic exclusion](Yin_C_A0220_v1.md#statement) leaves only \(p\equiv1,24\bmod25\).
For each prime divisor \(p\), \(M/pM\) has a simple quotient whose order is \(p^{\operatorname{ord}_{25}(p)}\), because \(\Phi_{25}(S)\) annihilates \(M\) and \(p\ne5\).
For the split class the [split-prime scan](Yin_C_A0219_v1.md#split-primes-and-a-strict-improvement-over-column-widths) excludes all \(p\le100000\) and the upper bound follows from \(p\le |M|\).
For the nonsplit quadratic class the present scan excludes all \(p\le100000\) and \(p^2\le |M|\) gives the smaller upper bound.

## Assessment history

### Decision all-quadratic-traces-through-one-hundred-thousand

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:36 |
| status | proved |
| reason | Independent proof review and a separate trace and matching enumeration established the strict bound at all quadratic markings in the interval. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Quadratic exclusion in the finite interval and both remaining prime ranges. |
| argument | [Enumerating the marked quadratic traces](#enumerating-the-marked-quadratic-traces) | All ten traces, their orders, recurrence and absorbed representations. |
| argument | [Both matching costs for the ten traces](#both-matching-costs-for-the-ten-traces) | The endpoint certificate, extremal costs and the four initial pairs. |
| argument | [Bounds on remaining primes](#bounds-on-remaining-primes) | Split and quadratic size constraints and the trivial commutator abelianization. |
| review | [All quadratic traces through one hundred thousand](../audits/reviews/Yin_R_A0193_v1.md#all-quadratic-traces-through-one-hundred-thousand) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-all-quadratic-traces-through-one-hundred-thousand)
