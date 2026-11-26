---
author: Yin
---

# The marked metabelian quotients left by the order-twenty-four constraints

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular group-ring scalar injectivity and an abelian quotient of order 24.
Suppose a complex two-by-two four-site rectangle \(B_0+A_0t-s(D_0+C_0t)\) has regular rank \(3/2\).
Use the [normalized ordered marking](Yin_C_A0241_v1.md#statement) with \(s,t\) of degrees \(3,4\) in \(H_{\rm ab}=C_{24}\).
Then \(M=H'/H''\) is cyclic and the marked group \(H/H''\) occurs in the following list of twenty finite candidates.

Take one entry in each column independently.
A pair \((m,u)\) denotes the additive cyclic group of order \(m\) with the action \(x\mapsto ux\), and \(0\) denotes the trivial module.

| First factor \(A\) | Second factor \(B\) |
| --- | --- |
| \(0,\ (3,-1),\ (9,2),\ (9,5)\) | \(0,\ (5,2),\ (5,-2),\ (13,5),\ (13,-5)\) |

With \(M=A\oplus B\), let \(\gamma\) generate the cyclic complement of order 24 acting by the displayed multipliers.
Put \(v=1\) in each nonzero coordinate and use the ordered generators
\[
                     s=\gamma^3,\qquad t=v\gamma^4 .
\]
These twenty groups are pairwise nonisomorphic with the specified ordered marking.
The list is a necessary condition for the original rank hypothesis.
In particular \(|M|\in\{1,3,5,9,13,15,39,45,117\}\).

Write \(a=|A|,\ b=|B|\), using size one for a trivial factor.
For every positive integer \(k\) the following tests are exact in each displayed finite group:
\[
 \begin{aligned}
 s t^k s^{-1}=t^k      &\quad\Longleftrightarrow\quad a\mid k\ \text{and}\ b\mid k,\\
 s t^k s^{-1}=t^{-k}   &\quad\Longleftrightarrow\quad 3\mid k\ \text{and}\ b\mid k .
 \end{aligned}
\]
A nontrivial neighboring cyclic intersection in \(H\) gives one of these necessary divisibilities with its actual conjugation sign, by the [common power in the original group](Yin_C_A0240_v1.md#the-common-rational-matrix-on-neighboring-cyclic-groups).

## Separating the two residual factors

Write \(S=\operatorname{Ad}_{ts^{-1}}\) on \(M\), and \(M_r=M/\Phi_r(S)M\).
The [cyclic complement calculation](Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group) splits \(H/H''=M\rtimes\langle\overline{ts^{-1}}\rangle\) with \(S^{24}=1\) and \(S-I\) invertible.
The [two-sided transfer bound](Yin_C_A0253_v1.md#statement) gives finite odd order and \(M_3=M_{12}=M_{24}=0\), and the [eighth quotient](Yin_C_A0241_v1.md#statement) also vanishes.
Each corresponding cyclotomic endomorphism is therefore invertible.
Removing these factors and \(X-1\) from \(X^{24}-1\) gives \(f(S)h(S)=0\), where \(f=X^3+1=(X+1)\Phi_6\) and \(h=X^2+1\).
The identity
\[
                 (X+1)f+\big(1-X(X+1)\big)h=2
\]
on this group of odd order splits \(M=A\oplus B\) with \(A=\ker f(S)\) and \(B=\ker h(S)\).
Indeed its two terms divided by two decompose every vector into these kernels and their intersection is zero.
The same identity makes \(h(S)\) invertible on \(A\) and \(f(S)\) invertible on \(B\), so \(B\simeq M_4\) and \(M_2,M_6\) are the corresponding quotients of \(A\).

On \(A\) one has \(1-S^3=2\), and on \(B\) one has \((1-S^3)(1-S)=2\).
Thus \(1-S^3\) is invertible on all of \(M\).
Conjugating the original complement by a translation \(c\) adds \((1-S^3)c\) to its generator's third power.
Choose \(c\) so that the new generator \(\gamma\) satisfies \(s=\gamma^3\), and write \(t=v\gamma^4\).
The vector \(v\) generates \(M\) over \(\mathbb Z[S]\), since in the quotient by its module span the two marks still generate and both lie in the cyclic complement.
In particular \(A,B\) are cyclic modules with projected generators \(v_A,v_B\).

The orders of \(M_2,M_6\) both divide three by the [second quotient bound](Yin_C_A0249_v1.md#statement) and [odd sixth quotient bound](Yin_C_A0253_v1.md#the-four-quadratic-factors-in-characteristic-five).
The subgroup \((S+1)A\) is a quotient of \(A/\Phi_6(S)A\), and its index in \(A\) is \(|M_2|\).
Hence \(|A|\mid9\).
If \(|A|=3\), then \(S^3=-1\) forces \(S=-1\).
If \(A\) were elementary abelian of order nine, \((S+1)^3=0\) would give \((S+1)^2=0\) in dimension two.
This makes \(\Phi_6(S)=(S+1)^2=0\) in characteristic three and would give \(|M_6|=9\).
On cyclic \(A\) of order nine, the roots of \(u^3=-1\) are \(2,5,8\bmod9\).
The last gives \(|M_2|=9\), leaving \(2,5\).

The [Gaussian quotient bound](Yin_C_A0249_v1.md#two-torsion-coordinates-over-the-gaussian-integers) gives \(B\simeq\mathbb Z[i]/I\) of order \(1,5,9\) or 13, with \(S=i\).
At the two primes 5 and 13 the roots of \(X^2+1\) are \(\pm2\) and \(\pm5\), respectively.
At order nine the ideal is \((3)\), since every Gaussian integer of norm nine is associated to three, so the module here would be \(\mathbb F_9\).

## The degree-four fibers of the middle intersection

Project onto \(B\rtimes C_{24}\) in this last case.
Identify \(v_B\) with \(1\in\mathbb F_9\) and write \(i\) for the image of \(S\).
On this module \(\gamma^4\) centralizes the translations, so the adjacent conjugates \(t_j=s^jts^{-j}=i^{3j}\gamma^4\) commute.
For each integer \(k\) the translation coordinates of the elements of degree \(4k\bmod24\) in \(\langle t_0,t_1\rangle\) form the set \(k+\mathbb F_3(i^3-1)\).
Indeed products with exponent sum \(k\) give this affine line, and changing the sum by six leaves it unchanged in characteristic three.
Conjugation by \(s^2\) acts by \(i^6=-1\), so the corresponding line for \(\langle t_2,t_3\rangle\) is \(-k+\mathbb F_3(i^3-1)\).
For \(k=1\) the two lines are disjoint because \(2\notin\mathbb F_3(i^3-1)\).
The [middle intersection theorem](Yin_C_A0240_v1.md#statement) supplies an element in both original adjacent-pair groups of degree \(4\bmod24\), which would project to both lines.
This excludes \(B=\mathbb F_9\).

The remaining factors have relatively prime orders and are cyclic as additive groups, so their sum is cyclic.
On each nonzero factor \(S\) acts by a scalar and the projected module generator \(v\) is an additive generator.
Rescaling independently realizes the displayed marking.
For each of the twenty pairs the commutator \(sts^{-1}t^{-1}=(S^3-1)v\) generates the whole additive group, since \(S^3-1\) is invertible.
The two marks generate the quotient \(C_{24}\) and hence their full semidirect product, whose derived subgroup is \(M\).
Any ordered marked isomorphism preserves conjugation by \(ts^{-1}=v\gamma\) on \(M\).
The orders distinguish the nine choices of the underlying pair of additive groups, and different scalar actions on a cyclic primary factor cannot be conjugate.
This gives the asserted marked count.

## Testing the sign of a common power

Set \(w_k=(1+S^4+\cdots+S^{4(k-1)})v\).
In translation and degree coordinates \(t^k=(w_k,4k)\), \(st^ks^{-1}=(S^3 w_k,4k)\) and \(t^{-k}=(-S^{-4k}w_k,-4k)\).
On \(B\) one has \(S^4=1\) and both \(1\pm S^3\) are invertible since their product is \(1-S^6=2\).
The translation comparison for either sign on this factor is therefore equivalent to \(b\mid k\).

On \(A\) the positive comparison requires \(2w_{k,A}=0\), or \(w_{k,A}=0\).
If \(|A|=3\), then \(S^4=1\) and this holds exactly for \(3\mid k\).
If \(|A|=9\), then \(S^4=-S\) is \(4\) or \(7\bmod9\).
These units have cube one and \(1+S^4+S^8=3\bmod9\).
The sum for \(w_{k,A}\) has value \(k\bmod3\); when \(3\mid k\), grouping consecutive triples gives value \(k\bmod9\).
The positive comparison thus requires and suffices that \(a\mid k\), also for the trivial \(A\).
For a negative comparison the degrees agree exactly when \(3\mid k\).
In that case \(S^{4k}=1\) on \(A\), so \(S^3=-1\) gives the negative translation equality there automatically.
Combining the two factors proves both tests.

## Assessment history

### Decision the-twenty-marked-metabelian-candidates

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:10 |
| status | proved |
| reason | Whole-proof inspection confirmed the integral splitting, exclusion of the noncyclic factor, twenty marked possibilities and exact finite power tests. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The cyclic module, normalized ordered marking and both signed common-power tests. |
| argument | [Separating the two residual factors](#separating-the-two-residual-factors) | The integral factor splitting and cyclic action possibilities. |
| argument | [The degree-four fibers of the middle intersection](#the-degree-four-fibers-of-the-middle-intersection) | Exclusion of the nine-element Gaussian component and distinction of ordered markings. |
| argument | [Testing the sign of a common power](#testing-the-sign-of-a-common-power) | Exact comparisons in each finite group and their scope in the original group. |
| review | [The twenty marked metabelian candidates](../audits/reviews/Yin_R_A0205_v1.md#the-twenty-marked-metabelian-candidates) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-twenty-marked-metabelian-candidates)
