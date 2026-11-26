---
author: Yin
---

# Peripheral fillings exclude the marked half-kernel without residual finiteness of the label group

## Statement

In the [order-24 half-kernel problem](Yin_C_A0288_v1.md#statement), suppose there is a homomorphism from the label group \(H\) to a group \(G\) such that the image \(u\) of the normalized second mark \(t\) has infinite order.
If \(u\) lies in a residually finite hyperbolically embedded subgroup \(P\) of \(G\), the four-site matrix cannot have nullity \(1/2\) under the stated torsion-free and scalar-injectivity hypotheses on \(H\).
The same exclusion holds when \(u\) acts loxodromically and satisfies weak proper discontinuity for some isometric action of \(G\) on a hyperbolic space.

In particular, this rules out such a half-kernel whenever \(H\) is word-hyperbolic or hyperbolic relative to residually finite peripheral groups.
The ambient group in the first assertion and the relatively hyperbolic label group in the final assertion need not be residually finite.
Only this marked rectangle and its stated nullity are at issue.

## Making the sixth power survive in a periodic image

If the half-kernel exists, the [periodic-image theorem](Yin_C_A0288_v1.md#normal-closures-and-finite-index-subgroups) says that in every homomorphic image in which \(t\) has finite order, its order divides six.
Indeed the map there factors through \(C_{24}\), in which the normalized \(t\) has degree four and order six.
It suffices to find an image of \(G\) in which \(u\) has finite order and \(u^6\ne1\).

For a hyperbolically embedded \(P\), the group-theoretic filling theorem provides a finite set \(\mathcal F\subset P\setminus\{1\}\) such that for every normal subgroup \(N\) of \(P\) avoiding \(\mathcal F\), the map \(P/N\to G/\langle\!\langle N\rangle\!\rangle_G\) is injective. [Dahmani, Guirardel and Osin, Theorem 2.27(a)](https://arxiv.org/abs/1111.7048)
Residual finiteness of \(P\) provides a finite-index normal subgroup missing every element of \(\mathcal F\cup\{u^6\}\), by intersecting the kernels of finitely many finite representations.
In this filling the image of \(u\) lies in the finite group \(P/N\) and its sixth power survives by the injection.
Composing \(H\to G\) with this filling contradicts the periodic-image theorem.
Conjugating \(u\) into \(P\) also suffices because both assertions about its order are conjugacy invariant.

For a loxodromic element satisfying weak proper discontinuity, its maximal virtually cyclic subgroup \(E_G(u)\) is hyperbolically embedded. [Dahmani, Guirardel and Osin, Theorem 6.8](https://arxiv.org/abs/1111.7048)
This subgroup is residually finite.
Indeed an infinite virtually cyclic group has a normal infinite cyclic subgroup of finite index, by taking the core of an infinite cyclic subgroup of finite index.
The subgroups of positive multiples of that normal cyclic group are characteristic in it, normal and of finite index in the full group, and intersect trivially.
The preceding construction therefore applies to \(E_G(u)\), also when the ambient \(G\) has torsion.

## Relatively hyperbolic label groups

Take \(G=H\).
The normalized \(t\) has infinite order by its nonzero degree and torsion-freeness.
In a word-hyperbolic group every infinite-order element is loxodromic with weak proper discontinuity on its Cayley graph for a finite generating set. [Dahmani, Guirardel and Osin, section 6](https://arxiv.org/abs/1111.7048)
This gives the word-hyperbolic assertion.

Now suppose \(H\) is hyperbolic relative to a family \(\{P_\lambda\}\) of residually finite subgroups.
If \(t\) is conjugate into \(P_\lambda\), use the peripheral filling theorem on this subgroup and take the trivial filling kernels in all other subgroups. [Osin, Theorem 1.1](https://arxiv.org/abs/math/0510195)
As above a finite-index normal subgroup of \(P_\lambda\) avoids both the forbidden elements and the conjugate of \(t^6\).
If \(t\) is not parabolic, its maximal virtually cyclic subgroup can be added to the peripheral family while preserving relative hyperbolicity. [Osin, elementary subgroups and bounded generation](https://arxiv.org/abs/math/0404118)
Apply the same filling theorem to that additional residually finite subgroup.
Both cases produce the requisite image with finite-order second mark whose sixth power is nontrivial.

## Assessment history

### Decision peripheral-fillings-and-survival-of-a-sixth-power

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:38 |
| status | proved |
| reason | The specified fillings make the second mark periodic and keep its sixth power nontrivial, contradicting the original-group theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The general ambient-image condition and the relatively hyperbolic families. |
| argument | [Making the sixth power survive in a periodic image](#making-the-sixth-power-survive-in-a-periodic-image) | The peripheral quotient, the sixth power and the virtually cyclic subgroup. |
| argument | [Relatively hyperbolic label groups](#relatively-hyperbolic-label-groups) | Both parabolic and nonparabolic placements of the infinite-order mark. |
| review | [Peripheral fillings and survival of a sixth power](../audits/reviews/Yin_R_A0212_v1.md#peripheral-fillings-and-survival-of-a-sixth-power) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-peripheral-fillings-and-survival-of-a-sixth-power)
