---
author: Yin
---
# Exact products in the Gardam group and unique products in its word balls

## Whole finding

At 2026-11-21T06:19 UTC an agent outside the development of [C105 v2](../../claims/Yin_C_A0105_v2.md#statement) independently reviewed its four assertions and complete [argument](../../claims/Yin_C_A0105_v2.md#argument) for Yin.
The review used the fixed proof, programs and source passages, together with the [prior review of v1](Yin_R_A0142_v1.md#whole-finding) for the coefficient exclusion that v2 invokes.
The reviewer received the scope of the bounded calculation and the author's reported completion counts, without the proof-development discussion.
The exact product computation and both exhaustions below establish the asserted bounds for every pair of nonempty subsets of the stated balls.

### Presentation and word equality

Following the arrows from the upper vertex on [Gardam's slide 12](../../literature/pdf/Gar21c.pdf#page=12) gives \(acb,add,afg,bbf,cef,cdg,eeg\).
The review checked both relators of the two-generator presentation against the slide and [Mian–Siddique, p. 2](../../literature/pdf/MS26b--arxiv-v1.pdf#page=2).
Solving for \(c,f,g,d,e\) successively gives \(a^{-1}b^{-1},b^{-2},b^2a^{-1},ba^2b^{-2},bab^2\).
The remaining boundary words become \(R_1\) and \(bR_2b^{-1}\) after free cancellation.
Thus substitution gives one homomorphism, and \(a,b\) in the triangle group satisfy both defining relators for the inverse homomorphism.
The five displayed generator identities verify the composites on all generators.

An independent construction from the 21 oriented cyclic triples gave the same 98 distinct left-hand sides and replacements as the retained verifier.
For each ordered \(x\ne y\) there was exactly one pair \(xuz,yvz\) with common last letter.
Its equality \(xu=yv\) gives the length-preserving rule \(x^{-1}y=uv^{-1}\).
This rule removes one negative-before-positive inversion, and the other rules shorten the word, proving termination.
For each of the \(14^3\) three-letter strings the reviewer followed **all** reductions to irreducibles.
There were 560 strings admitting two initial positions, 1,624 admitting one and 560 admitting none, and each string had exactly one irreducible descendant.
Equal positions give the same replacement and disjoint positions commute even when a replacement deletes letters.
These exhaust all local ambiguities, so the induction on length and inversion count in C105 applies to arbitrary words.
The rule equalities contain inverse cancellation and every defining triangle, and each is valid in the triangle group.
Consequently equality of the normal forms is equivalent to equality in the two-generator group.

### Balls and product fibers

The reviewer enumerated freely reduced words in \(a,b,a^{-1},b^{-1}\) by length and applied rightmost reduction.
For each radius from zero through eight the resulting set of normal forms agreed with the entire breadth-first ball produced by J_A0005.
The respective sizes were \(1,5,17,53,161,467,1311,3637,9929\).
In each of the five tested rectangles the reviewer checked every product by comparing rightmost reduction of the concatenated normal forms with the verifier's leftmost reduction of the original words.
Each product table covered the ball of the summed radii, with 26,845 distinct products for radius nine and 9,929 for radius eight.

Both appendix lists agreed in their printed order with [Mian–Siddique, p. 10](../../literature/pdf/MS26b--arxiv-v1.pdf#page=10).
Partitioning their 896 cells by rightmost normal form gave the same sets of cells as all 336 classes of J_A0004.
The least fiber size was two.
Thus the new partition on every subrectangle is the restriction of the partition used in v1.
R_A0142 v1 covers the enumeration of the three permitted support choices and the three coefficient contradictions over every field.
The reviewer checked this interface and reran J_A0004 with assertions enabled.
In each surviving restriction the three two-cell equations cancel two terms of a three-cell equation, forcing the product of two nonzero coefficients to vanish, including in characteristic two.

### Exhaustion of rectangles

For fixed maximal indices \(h,k\), a rectangle with no uniquely represented product must extend the cell \((h,k)\).
Each selected cell needs a second cell of the same fiber whose endpoints are both selected.
In J_A0005 the compatibility masks remove only labels with a singleton against a required label, and a forced partner is the last possible choice for a required cell.
Branching on all available partners covers every completion of that cell, including those that use multiple partners.
Every successor adds a label and the two required masks determine the remaining problem for fixed \(h,k\), which justifies memoization within those bounds.
A state with all required cells partnered supplies a genuine witness.

The reviewer also implemented a second search directly on the independently calculated tables, using the published endpoint order.
For each \(h\) and cell \(t\) in rows up to \(h\), let \(m_h(t)\) be the least column of another cell of its fiber in those rows, or \(+\infty\) if there is none.
The two least columns in each fiber suffice to compute \(m_h\), since two distinct cells of a product fiber always have different columns by right cancellation.
In columns up to \(k\) a required cell with \(m_h(t)>k\) cannot have a partner.
For a required cell still lacking a selected partner, the second search tried each partner in the prefix for which all newly required cross cells passed this test.
The original required cell supplies a partner for the newly added cell itself.
Each recursive call added its endpoints to the selected lists.
The search kept no cache and added one partner per step, allowing the same state to be reached by several paths.
Its small positive and negative controls agreed with literal subset enumeration for 104 rectangles in cyclic groups of orders two through seven.

| Radii | Pairs of maxima searched | Recursive calls in the second search |
| --- | ---: | ---: |
| \((1,8)\) | 3,073 | 16,661 |
| \((2,7)\) | 10,011 | 99,011 |
| \((3,6)\) | 17,662 | 645,062 |
| \((4,4)\) | 6,894 | 166,433 |
| \((4,5)\) | 23,709 | 4,487,161 |

All five searches exhausted their branches.
The reviewer also ran the retained J_A0005 verifier with assertions enabled and reproduced each published seed and state count, including 2,785,704 states for \((4,5)\).
Inversion reverses the two supports and bijects their product fibers, and inclusion of balls preserves an exclusion for their subsets.
After exchanging the radii if necessary, one of the four tested pairs of sum nine dominates each positive \(r,s\) with \(r+s\le9\).
For radius zero one support is a singleton and cancellation gives uniqueness directly.
The coefficient at a uniquely represented product is a single nonzero product in the field.
The result applies to these bounded supports and separately to the exact appendix rectangle through the v1 coefficient argument.
The behavior of arbitrary supports and the torsion-freeness of the presented group lie outside this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0105_v2.md#statement) | All four assertions for the given presentation, fields and support ranges. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0105_v2.md#argument) | Both presentation maps, termination and confluence, exact tables, the full subset exhaustion and the two field conclusions. |
| [Whole finding](#whole-finding) | [Presentation](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation) | The seven oriented source triangles, the two defining relators and the substitutions in both directions. |
| [Whole finding](#whole-finding) | [Exact balls and appendix partition](../../claims/Yin_C_A0105_v2.md#exact-balls-and-the-appendix-partition) | Word-metric balls and the exact multiplication table on the 60 ordered source words. |
| [Whole finding](#whole-finding) | [Bounded exhaustion](../../claims/Yin_C_A0105_v2.md#exhausting-the-bounded-rectangles) | Soundness of every restriction, forced step, branch, stopping criterion and memoized state. |
| [Whole finding](#whole-finding) | [Computation description](../../computations/programs/Yin_J_A0005/readme.md) | Reproduction scope and the five radius pairs. |
| [Whole finding](#whole-finding) | [Exact word and ball verifier](../../computations/programs/Yin_J_A0005/verify.py) | Every rewriting rule, critical overlap, ball, product table, partner search and exclusion in the default range. |
| [Whole finding](#whole-finding) | [Appendix computation](../../computations/programs/Yin_J_A0004/verify.py) | The supplied word lists, partition, support choices and coefficient certificates as used by v2. |
| [Whole finding](#whole-finding) | [Earlier statement](../../claims/Yin_C_A0105_v1.md#statement) | The unchanged all-fields coefficient exclusion adopted on the appendix supports. |
| [Whole finding](#whole-finding) | [Earlier argument](../../claims/Yin_C_A0105_v1.md#argument) | Applicability of the three-rectangle argument to the identical partition and fields. |
| [Whole finding](#whole-finding) | [Earlier review](Yin_R_A0142_v1.md#whole-finding) | Existing independent review of the unchanged v1 support enumeration and coefficient contradictions. |
