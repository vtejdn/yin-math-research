---
author: Yin
---
# The subgroup of a complementary kernel projection

A separate reviewing agent inspected the complete [fixed Claim](../../claims/Yin_C_A0024_v1.md) for Yin on 2026-11-16T16:05 UTC.
The reviewer had checked the two-coset bound, the extreme-degree rank estimate, the primitive-pair uniqueness result, and the size theorem used for finite subsets.
The reviewer did not develop the present proof or receive its development discussion, author explanations, exploration notes or earlier verdicts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0024_v1.md#statement) | Subgroup minimality, generation, finite recovery, arbitrary cover orientations and the special primitive case. |
| [Whole-argument finding](#whole-argument-finding) | [Projection localization](../../claims/Yin_C_A0024_v1.md#localization-of-the-support-projections) | Both directions of the slice criterion, joins of projections, and the two finite generating sets. |
| [Whole-argument finding](#whole-argument-finding) | [Coefficient subsums](../../claims/Yin_C_A0024_v1.md#recovery-from-vanishing-coefficient-subsums) | Attainment of the least partition subgroup and the indecomposable fiber case. |
| [Whole-argument finding](#whole-argument-finding) | [Characters and orientations](../../claims/Yin_C_A0024_v1.md#characters-and-the-two-orientations-of-cyclic-cosets) | Independent choice of the two covers, exclusion of a character on \(D\), and vanishing of sums on character layers in \(J\). |
| [Whole-argument finding](#whole-argument-finding) | [Primitive case](../../claims/Yin_C_A0024_v1.md#primitive-pairs-and-scope-for-a0001) | Application of annihilator uniqueness to recover equality of the two subgroups. |

## Whole-argument finding

Since \(f(b)\le1-i(a)\) and their traces agree, the two projections are equal.
Both complementary projections have positive trace and determine the same subgroup by their nonidentity Fourier coefficients.
For each subgroup \(L\), Fourier restriction shows that \(p\in\mathcal N(L)\) exactly when \(D\subseteq L\).
When this holds, applying \(a(1-p)=0\) to \(\delta_e\) separates the \(x_i a_i(1-p)\) on disjoint left cosets.
Faithfulness forces each operator to vanish, and \(pb=0\) gives the other side by the disjoint right cosets.
Conversely the pairwise zero products force the join of the initial slice projections to be orthogonal to the join of the final slice projections.
They dominate \(i(a)\) and \(f(b)\), respectively, by the defining support identities.
Those latter projections sum to one, so the joins equal them.
This puts \(p\) in \(\mathcal N(L)\) as required.

Any two pairs in the same coefficient fiber have \(x^{-1}x'=yy'^{-1}\).
They therefore occupy a single pair of left and right \(J\)-cosets, and the slice criterion gives \(D\le J\).
For the \(D\)-slices the support projection of \(\sum_i a_i^*a_i\) is their initial join \(p\).
The internal row differences generate a subgroup of \(D\), and spectral calculus places \(p\) in that subgroup's von Neumann algebra.
Minimality then gives equality with \(D\).
Using \(\sum_j b_jb_j^*\) gives the column-difference equality.
The finite supports make both generating sets finite.

In every zero-sum partition, a block fixes a left coset for its rows and a right coset for its columns relative to its difference subgroup.
For each product, the coefficient from a fixed pair of those cosets is therefore a sum of whole zero blocks.
The slice criterion puts \(D\) in that difference subgroup for every partition.
Conversely partitioning by the pairs of \(D\)-cosets gives zero blocks because each \(D\)-slice product vanishes, and all resulting differences belong to \(D\).
This particular partition attains the least subgroup.
The full fibers yield the whole of \(J\), since every common difference represents an actual collision.
In a fiber of size two or three a proper nonempty zero subsum would force at least one nonzero entry to vanish, as the complementary subsum must vanish as well.

If \(D\) has an epimorphism to \(\mathbb Z\), each of the two finite generating sets supplies a slice of varying degrees.
These choices can be made independently because every pair of slices has zero product.
Their ranks in \(D\) are bounded by the original half ranks by projection domination and trace-preserving inclusion.
For each slice, translating a cover conjugates its subgroup if necessary but preserves the orientation of its cosets.
A translated coset meeting \(D\) at \(d\) intersects \(D\) in \(d(H\cap D)\) for a left coset of \(H\), or \((H\cap D)d\) for a right coset.
Thus one common cyclic or trivial subgroup provides at most five cosets for that slice.

When the character kills that subgroup, the two nonempty degree extremes occupy disjoint coset collections and one of them uses at most two cosets.
Its rank is strictly above one half by the two-coset theorem, using adjoints in the right orientation, or by direct Laurent injectivity for a binomial when the intersection is trivial.
This contradicts the extreme-degree rank bound.
The character must therefore be injective on the covering cyclic subgroup for each of the two slices.
Each maximal-degree support then has at most five terms in either orientation.
Their homogeneous product vanishes, contradicting Nielsen and Soelberg's unique-product bound for these two nonempty subsets of the torsion-free subgroup \(D\), of combined size at most ten.
Finite generation now converts absence of a nonzero integral character to finite abelianization.

Every integral character of \(J\) consequently vanishes on \(D\).
Rows in the same zero block differ by right multiplication by an element of \(D\), so they have equal degrees after translation into \(J\) by the chosen left coset representative.
Each degree sum consists of whole zero blocks, with a change of representative only shifting all degrees by a constant.
This reasoning applies without normality of \(D\) in \(J\).
In the primitive four-coset case each original slice annihilates the entire opposite factor, by the supporting projections.
The earlier scalar-uniqueness result thus forces a single occupied \(D\)-coset on each side, making both difference sets subsets of \(D\) and proving \(J=D\).
