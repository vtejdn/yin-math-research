---
author: Yin
---

# A normal alternating subgroup on six letters at noncyclic order twenty

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free, have regular scalar group-ring injectivity, and admit the quotient \(C_5\times C_2^2\) with marks \((1,e_1),(2,e_2)\) for a binary basis.
Suppose a quotient \(J\) of \(H\) has a normal subgroup isomorphic to \(A_6\).
Every complex two-square rectangle \(B+At-s(D+Ct)\) of noninteger regular rank then has unnormalized regular nullity \(\delta\le7/15\).
This includes infinite \(J\) and all outer actions on the normal subgroup.
In particular, at a half kernel no quotient of \(H\) has a normal subgroup isomorphic to \(A_6\) or \(A_6^3\).
A finite quotient then cannot have a chief factor isomorphic to \(A_6\), or have exactly one \(A_6\) composition factor.

## Every marked action on the ten Sylow subgroups

Write \(T=A_6\).
Its Sylow three-subgroups correspond to the ten unordered partitions of six letters into two triples, by independently cycling the two triples.
The conjugation action \(T_{10}\) on them is faithful.
Its normalizer \(N\) in \(S_{10}\) has order 1440, and \(N/T_{10}\cong C_2^2\).
These group computations and a construction by transporting the two generators of \(T_{10}\) are given in the [ten-point normalizer proof](Yin_C_A0341_v3.md#all-three-outer-actions-of-cyclic-order-two).

Since the normal copy of \(T\) in \(J\) has this intrinsic family of ten subgroups, conjugation gives a genuine image \(T_{10}\le K\le N\) of \(H\).
For \(K=T_{10}\), use its faithful six-letter realization and the [six-site estimate](Yin_C_A0346_v1.md#statement).
The other possibilities are the three inverse images of the order-two subgroups of \(N/T_{10}\) and \(N\) itself.
Both marks can have arbitrary outer classes.

The [integer verifier](../computations/programs/Yin_J_A0011/verify_alternating_normalizer_twenty.mjs) chooses the first mark \(x\) in each \(N\)-conjugacy class and tests every \(y\in N\) as second mark.
It forms the actual generated subgroup and checks membership of all 360 elements of \(T_{10}\).
Every such retained pair is transitive.
To remove duplicates, traverse the two colored outgoing arrows from each possible root and take the least resulting labeled graph code.
Two transitive pairs have equal codes exactly when a bijection simultaneously intertwines their marks.
The outer cosets are numbered in the order of their construction in the cited verifier.

| Outer image | Marked classes | Ten sites | Unordered pairs | Exterior square |
| --- | ---: | ---: | ---: | ---: |
| First order-two subgroup | 159 | 103 | 43 | 13 |
| Second order-two subgroup | 234 | 156 | 50 | 28 |
| Third order-two subgroup | 234 | 140 | 65 | 29 |
| Full four-group | 468 | 300 | 129 | 39 |

## The original regular rank and consequences for finite quotients

For \(\delta>2/5\) all four corners and the assembly are invertible by the [order-twenty corner reduction](Yin_C_A0346_v1.md#two-independently-signed-phases-on-the-same-network).
Use the ten sites or their 45 unordered pairs.
For the exterior test use the ordinary pair representation at \(z^5=1\) and the genuine exterior-square representation at \(z^5=-1\).
At each \(z^{10}=1\), tensor the full representation with the marked character whose exponents \(a,b\) satisfy \(b\equiv2a\bmod5\).
The two independent binary coordinates permit the chosen parities.
Site-diagonal conjugation gives integer lifts on both kinds of edges by the [signed-pair construction](Yin_C_A0346_v2.md#a-genuine-exterior-square-representation-at-selected-phases).
The original group translations accompany these representation matrices, so every evaluated kernel has dimension \(d\delta\), where the degree \(d\) stays fixed across the ten phases.

For every one of the 1095 marked classes the verifier checks a feasible binary circulation and integer potentials with nonnegative reduced costs on every residual edge.
A residual cycle of cost zero lies in a recurrent component of the zero reduced-cost graph.
Forward and backward reachability from any of its sites determine the whole component by intersection.
The verifier requires each recurrent component to be a single directed cycle and detects the underlying group word by its marked abelian degree or its nonidentity permutation.
The [original-group endpoint estimate](Yin_C_A0346_v2.md#checking-optimality-and-the-recurrent-group-words) then gives \(10d\delta\le2D\), where \(D\) is the difference of the maximal and minimal circulation costs.
The largest \(D/d\) in the table is \(105/45=7/3\), giving \(7/15\).
This also bounds the initial range \(\delta\le2/5\).

At a half kernel every permutation representation on three points factors through \(C_5\times C_2^2\) by the [small-index theorem](Yin_C_A0346_v2.md#statement).
If \(A_6^3\) is normal in \(J\), conjugation permutes its three simple direct factors: these are its minimal nontrivial normal subgroups, since commutators with an individual factor detect each nontrivial projection to that factor.
The action on three factors has orbits of size one or two and therefore fixes a factor.
This gives a normal copy of \(A_6\) in \(J\), already excluded.
For a chief factor \(P/L\cong A_6\) of a finite quotient \(J\), apply the same exclusion to \(J/L\).
If \(A_6\) occurs exactly once among the composition factors, it occurs in a chief factor that is a direct power of a nonabelian simple group.
Indeed, a finite chief factor is characteristically simple.
The automorphic images of a minimal nontrivial normal subgroup of the factor generate it.
Whenever such an image lies outside the product of the previously chosen images, it intersects that product trivially by minimality and commutes with it by normality.
Continuing gives a direct product, and each direct factor is simple since its own normal subgroups are normal in the product.
All are isomorphic, so multiplicity one makes the chief factor itself \(A_6\).

## Assessment history

### Decision an-arbitrary-quotient-with-a-normal-alternating-group-on-six-letters

| Field | Value |
| --- | --- |
| date | 2026-11-26T19:16 |
| status | proved |
| reason | All three outer involutions and the full outer action satisfy the strict nonsolvable-image bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All three outer involutions and the full outer action satisfy the strict nonsolvable-image bound. |
| argument | [Every marked action on the ten Sylow subgroups](#every-marked-action-on-the-ten-sylow-subgroups) | Every marked action on the ten Sylow subgroups. |
| argument | [The original regular rank and consequences for finite quotients](#the-original-regular-rank-and-consequences-for-finite-quotients) | The original regular rank and consequences for finite quotients. |
| dependency | [Seven-point certificates](Yin_C_A0346_v2.md#statement) | The preceding normal-image bounds. |
| review | [Exterior-square certificates on seven points](../audits/reviews/Yin_R_A0238_v1.md#exterior-square-certificates-on-seven-points) | Independent review of the preceding certificates. |
| review | [An arbitrary quotient with a normal alternating group on six letters](../audits/reviews/Yin_R_A0240_v1.md#an-arbitrary-quotient-with-a-normal-alternating-group-on-six-letters) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-an-arbitrary-quotient-with-a-normal-alternating-group-on-six-letters)
