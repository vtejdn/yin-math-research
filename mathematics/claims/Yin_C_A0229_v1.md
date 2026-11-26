---
author: Yin
---

# A uniform gap below half nullity at order twenty-five when the commutator subgroup is not perfect

## Statement

Let the torsion-free group \(H=\langle s,t\rangle\) have abelianization \(C_{25}\) with marked images \(1,7\).
Set \(N=H'\), \(M=N/H''\), and \(P_*=2227495051\).
Suppose \(M\ne0\).
For all complex two-by-two corners \(A,B,C,D\) with each corner and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible, the four-site matrix \(K=B+At-s(D+Ct)\) satisfies
\[
              \dim_H\ker K\ \le\ \frac12-\frac1{50P_*}.
\]
Here the matrix trace is unnormalized and scalar group-ring injectivity is not assumed.
The numerical gap is a sufficient uniform bound.

More generally suppose \(H=\langle s,t\rangle\) is torsion-free with scalar group-ring injectivity and admits a surjection onto \(C_{25}\), with arbitrary marked images.
If rank \(3/2\) occurs for a four-site matrix with any complex two-by-two corners, then \(H_{\rm ab}=C_{25}\) and **every solvable quotient of \(H\) factors through that cyclic group**.
This excludes the half constant-column increment in the corresponding four-column pencil whenever a nonabelian solvable quotient exists.
In particular the half increment is excluded for residually solvable groups in this class.
A remaining hypothetical half witness would yield a genuine two-by-two group-ring matrix on the perfect subgroup \(N\), with a single-inverse Schur scalar of rank in \((0,1/2]\).

## Reduction to a simple character quotient

Let \(S=\operatorname{Ad}_s\) on \(M\) and \(M_j=M/\Phi_j(S)M\) for \(j=5,25\).
The [cyclic module calculation](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module) gives finiteness of \(M\), invertibility of \(S-I\), absence of five-primary torsion and \(\Phi_5(S)\Phi_{25}(S)M=0\).
These facts use just the cyclic abelianization and finite generation.
If \(M_5\ne0\), the [fifth-component bound](Yin_C_A0215_v1.md#statement) gives nullity at most \(614/1375\), below the stated cutoff.
Otherwise \(\Phi_5(S)\) is surjective, so \(M=M_{25}\).
Since this is a nonzero finite cyclic module, it has a simple quotient in some characteristic \(p\ne5\).
In this quotient \(S^{-1}\) has primitive eigenvalue \(\alpha\) of order twenty-five and the module has order \(p^{\operatorname{ord}_{25}(p)}\).
It suffices to use one simple quotient to bound the original regular nullity.

The order of \(p\bmod25\) is either its order modulo five or five times that order.
In the latter case the [five-slice theorem](Yin_C_A0216_v1.md#statement) gives nullity at most \(2/5\).
In the former case \(p^4\equiv1\bmod25\), so the possible residues are \(1,7,18,24\).
For residues \(7,18\) the simple quotient has order \(p^4\).
If \(p>18^5\), the [Euclidean character bound](Yin_C_A0218_v1.md#numerical-consequence-for-the-twenty-fifth-component) gives nullity at most \(2/5\), since \(|M_{25}|\ge p^4>18^{20}\) and \(B\) is invertible.
In the finite complementary interval the [quartic period calculation](Yin_C_A0220_v1.md#statement) gives the same bound except at \(p=7\), where the [four-prime estimate](Yin_C_A0217_v1.md#factor-coverage-and-numerical-bounds) gives \(1918/4375\).
All these upper bounds are below \(1/2-1/(50P_*)\).
The size comparison used here applies directly to the coefficient pencil and does not presuppose a half kernel.

## The two remaining residues and the uniform gap

For \(p\equiv1\bmod25\) through 100000 use the [complete split interval](Yin_C_A0219_v1.md#split-primes-and-a-strict-improvement-over-column-widths).
Above 100000, if \(p\) divides a nonzero norm of a simple cycle of the transfer graph, the [exceptional divisor calculation](Yin_C_A0227_v1.md#the-finite-endpoint-certificates) covers every such prime and every primitive marking.
The largest such prime is \(P_*\).
For \(p\equiv-1\bmod25\) through 2300650 use the [complete quadratic interval](Yin_C_A0228_v1.md#extension-of-the-quadratic-certificate), including the original interval through 100000.
Each of these finite results exhibits integer matching costs \(L,U\) for actual twists with
\[
      25p\,\dim_H\ker K\le2(U-L),\qquad 4(U-L)<25p .
\]
Integrality gives \(25p-4(U-L)\ge1\), so the gap is at least \(1/(50p)\ge1/(50P_*)\).

For each remaining split prime no nonzero cycle norm vanishes modulo \(p\).
Every remaining quadratic prime exceeds 2300625.
The [single-cycle theorem](Yin_C_A0226_v1.md#the-split-and-quadratic-nonvanishing-tests) therefore supplies in either case a line of genuine characters avoiding every nonperiodic cycle tie, for the particular primitive marking of the quotient.
Its specialization proof works for all nonzero scalar multiples on that line.
For the slight uniform improvement needed here, use the actual weighted mean in the [Fourier estimate](Yin_C_A0226_v1.md#choosing-a-multiple-on-a-fixed-line-of-functionals).
Since the zero multiplier has weight \(2/p\) and contributes zero, some nonzero multiplier has centered width sum strictly less than
\[
                         \frac{25p/4-p/16}{1-2/p}.
\]
The matching spread is at most this sum, so at size two the regular nullity is strictly less than \(99/(200(1-2/p))\).
For \(p>100000\) this is below \(499/1000\), and hence below \(1/2-1/(50P_*)\).
This exhausts every possible characteristic of a nonzero \(M\).

## Consequences for the original half increment

Under scalar group-ring injectivity, the [critical marking and corner theorem](Yin_C_A0201_v1.md#statement) normalizes a half-rank witness up to swapping or inverting labels and permuting the corners.
It supplies invertibility of all four corners.
The abelianization is exactly \(C_{25}\): it maps onto that cyclic group, and a larger finite abelianization would give a quotient of order at least fifty while an infinite finitely generated abelianization would give arbitrarily large cyclic quotients.
Both possibilities contradict the [abelian quotient exclusion](Yin_C_A0201_v1.md#consequence-for-finite-abelian-quotient-orders).
The [four-column equivalence](Yin_C_A0184_v1.md#statement) supplies invertibility of the assembled block and equates existence of a half increment with existence of a rank-\(3/2\) rectangle on the same labels.
The first part now forces \(M=0\), or equivalently \(H'=H''\).

The image of a perfect subgroup in a solvable group is both perfect and solvable, hence trivial.
Thus every solvable quotient factors through \(H/H'=C_{25}\).
Conversely, when \(M\ne0\), the finite metabelian quotient \(H/H''\) witnesses a nonabelian solvable quotient.
If \(H\) is residually solvable and \(H'\) is perfect, every element of \(H'\) vanishes in every solvable quotient, so \(H'=1\).
This would give \(H=C_{25}\), contrary to torsion-freeness.
Finally the [two-by-two Schur descent](Yin_C_A0222_v1.md#a-single-inverse-and-exact-coordinate-ranks) gives the asserted obstruction over the actual perfect commutator subgroup in the remaining case.
The implication does not exclude all such perfect subgroups.

## Assessment history

### Decision a-uniform-half-nullity-gap-and-solvable-quotients

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:09 |
| status | proved |
| reason | Independent whole-proof review verified the uniform constant, every characteristic and the consequences on the original marked subgroup. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform bound without scalar injectivity and consequences under the scalar hypothesis. |
| argument | [Reduction to a simple character quotient](#reduction-to-a-simple-character-quotient) | Finiteness, the fifth quotient, degree growth and every quartic characteristic. |
| argument | [The two remaining residues and the uniform gap](#the-two-remaining-residues-and-the-uniform-gap) | The two finite ranges, complete split divisors, the infinite ranges and the numerical gap. |
| argument | [Consequences for the original half increment](#consequences-for-the-original-half-increment) | Arbitrary critical marking and corners, perfect commutator, residual solvability and two-by-two descent. |
| review | [A uniform half-nullity gap and solvable quotients](../audits/reviews/Yin_R_A0196_v1.md#a-uniform-half-nullity-gap-and-solvable-quotients) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-a-uniform-half-nullity-gap-and-solvable-quotients)
