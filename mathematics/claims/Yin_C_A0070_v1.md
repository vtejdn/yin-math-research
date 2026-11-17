---
author: Yin
---

# Alternative matchings forced by repeated commutator paths

## Statement

Consider the [four-line model with fourteen prescribed colors](Yin_C_A0054_v1.md#a-planted-binary-coordinate-which-does-not-certify-any-of-the-six-colors).
Fix \(0<\delta<1\) and an odd integer \(m\ge3\).
There are a sufficiently small fixed logarithmic girth constant and a fixed \(\gamma>0\) for which the following holds with probability tending to one conditional on girth.
Write \(k=\lfloor n^\gamma\rfloor\) and let \(h\) be the largest odd integer at most \(n^{1-\delta}\).
In **each** of the two fine bins over forward left color \(3\) there is a set of \(2mkh\) vertices with at least
\[
                           ((2m-1)!!)^{kh}                             \tag{1}
\]
distinct perfect matchings by witnessed original-group equalities.
The witnesses can use both translated relator families.
Each of these matchings has the same nonzero central signature of tensor rank \(k\) in the [mixed two-group test](Yin_C_A0066_v1.md#the-finite-tensor-calculation).
The ordinary first homology of every displayed displacement vanishes even at the unrestricted deck indices.
These assertions hold together with connectedness, asphericity, torsion-freeness, root separation, the original binary zero product and absence of an order-21 quotient over the specified character.
One may simultaneously require the kernel of the planted map onto \(C_{14}\) to be perfect and every map to a finite group of order at most \(\kappa n/\log n\) to factor through that planting, for a fixed \(\kappa>0\).
The two bins concerned have even sizes.
Every quotient over the coarse \(C_7\) with solvable kernel also factors through this \(C_{14}\), since it sends the perfect planted kernel into that solvable kernel.
Thus the covers of bounded order just specified and all such solvable refinements have only even bins above color \(3\).

On **any** tuple possessing the paths below, if the whole coarse color admits a complete matching by genuine original-group equalities, each matching in (1) extends to one of the whole color with an identical choice of partners on the complement of the displayed set.
This conclusion can be obtained from a supplied full matching by splicing paths, even when it pairs displayed vertices to outside partners.
If all the supplied edges already have central elementary-abelian signatures given by a common displacement homomorphism, every full alternative produced by this splicing has the same total as the original.
Thus even exponentially many forced alternatives can carry exactly the same nonzero information on their common marked subset.
The existence of these partial matchings is unconditional on full erasure, and typical tuples in this law actually have surviving original labels. [C54, fine counts and singleton estimate](Yin_C_A0054_v1.md#a-planted-binary-coordinate-which-does-not-certify-any-of-the-six-colors)

## Extending witnessed matchings on even blocks

Take disjoint blocks of \(2m\) vertices, all equal in original group label within each block, allowing different blocks to have the same label.
Suppose the successive edges of a path through the marked vertices \(x_0,\ldots,x_{2m-1}\) of one block certify these equalities with the same central element \(T\) of order dividing two, in additive notation.
Then every two marked vertices have a subpath certificate with value \((j-i)T\) for \(x_i,x_j\).
For any matching inside this block the total equals \((m\bmod 2)T\), since the sum of endpoint indices modulo two counts the \(m\) odd indices once.
There are \((2m-1)!!\) distinct matchings of a labeled block by recursively choosing a partner for the first remaining vertex.
Distinct choices on disjoint blocks give distinct matchings on their union \(Z\).
More generally any signed differences of vertex potentials with values in an elementary abelian group have fixed matching total on that vertex list.

Let \(M\) now be any given full true matching and \(P_0\) one fixed internal matching of \(Z\).
In the multigraph formed by their edges, every vertex of \(Z\) has degree two and every vertex of the complement has degree one.
The path components pair all complement vertices, and the remaining components are cycles entirely in \(Z\), including doubled edges.
Use each path as an explicit proof for its two outside endpoints, reversing the constituent equality certificates when necessary.
Every true internal choice \(P\) therefore extends with this same complement matching.
When the given signatures of \(M,P_0,P\) arise from the same homomorphism and are central of exponent two, their sums on cycles vanish by telescoping the displacements.
Thus the complement path signatures have total \(T(M)+T(P_0)\).
If \(T(P)=T(P_0)\), the total of the full extension equals \(T(M)\).
When using the mixed tensor with balanced free-word witnesses, one can rebase all constituent expressions to the chosen root words by the fixed-root graph loops, which are killed in the displacement homomorphism. [C66, certificate and root-path conventions](Yin_C_A0066_v1.md#the-finite-tensor-calculation)
The formula for the total uses the displacement homomorphism, even if a freely written concatenation also contains an unbalanced fixed-root term.
If the initial matching is known only as a list of true equalities, the extensions still exist but the formula assigns no explicit central values to its unknown witnesses.

## Repeated paths with independent mixed signatures in the even bins

Put \(s=2m-1\), \(a=\delta/(64s)\), \(b=a/2\), \(\gamma=a/4\) and \(R=\lceil a\log n/\log 64\rceil\).
Before girth conditioning, perform the [neutral cycle searches on both sides](Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple) at fine color \((0,0)\).
Each search uses \(O(n^{1-b})\) exposures and, except with probability \(\exp(-\Omega(n^{a-b}))\), supplies \(k\) vertex-disjoint simple cycles of length at most \(2R+2\).
Only their diagonal pairs are needed here.
Let \(U_i,V_i\) be their respective words and choose a neutral usable spacer \(t_i\) outside the inverse pairs of the first and last letters of both words.
The commutator \(W_i=[t_iU_it_i^{-1},V_i]\) is cyclically reduced.
Indeed its first letter is \(t_i\) and its last letter is the inverse of the first letter of \(V_i\), in addition to the [four internal splice checks](Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple).
Thus \(W_i^s\) is freely reduced, uses only neutral letters and has length at most \(s(8R+12)\).

In either left fine bin above \(3\), conditional on these searches, the necessary matching blocks are fresh.
Divide \(\lfloor n^{1-b}/(s(8R+12)+1)\rfloor\) trials as evenly as possible among the \(k\) prescribed words \(W_i^s\).
As in the [bounded-exposure proof](Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths), mark all visited vertices including failures, start on a fresh vertex carrying the first stub and demand a fresh eligible endpoint at each step.
The budget is \(O(n^{1-b})\) and each usable turn originally has linearly many realizations in the bin, so each trial conditionally succeeds with probability at least \(300^{-s(8R+12)}\).
For each word its binomial lower comparison therefore has expectation at least
\[
 n^{\,1-b-a/4-8sa\log(300)/\log(64)-o(1)} > n^{\,1-\delta/2}
\]
for large \(n\), since \(b+a/4=3a/4\) and \(8\log(300)/(64\log(64))<0.18\).
The binomial lower tail and a union bound over both bins and \(k\) words give at least \(h\) successful paths per word except with probability \(2k\exp(-\Omega(n^{1-\delta/2}))\).
Successes within a bin have disjoint vertex sets.
The [fourteen-color girth bound](Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple) with its constant reduced to satisfy \(c_0\log(28|T_{\rm src}|/p_{\rm src})<a/4\) and \(2c_0\log132<1\) costs at most \(\exp(O(n^{3a/8}\log n))\) in either failure probability.
Since \(a-b=a/2\), the conclusion survives conditioning.
All geometric and quotient safeguards follow on intersecting the probability-\(1-o(1)\) events of C54 and [the bounded-perturbation theorem for the planted \(C_{14}\)](Yin_C_A0061_v1.md#statement).
Every finite map of order at most its stated bound then factors through this planting, whose two fine bins are even over left \(3\).

Mark the \(s+1=2m\) points at the ends of successive copies of \(W_i\) on each of \(h\) successful simple paths per index.
Every marked vertex on a path has its original starting label since both loop words are cone relations.
Each copy is a commutator in the actual relation group and thus has zero first-homology class.
The successive mixed tensors equal \(T_i=[U_i]_3\otimes[V_i]_3\), since all starting coarse indices are \(3\), spacers are neutral and the selected cycles are based in fine color \((0,0)\).
Rebasing from their cycle base vertices uses the corresponding root paths. [C66, actual indices of both families](Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple)
One may use the common initial root path followed by prefixes for every marked vertex of that path, so all subpath witnesses are products of conjugates of the balanced commutators.
Since \(m,h\) are odd, the total on \(Z\) is \(\sum_{i=1}^k T_i\) for every choice in (1).
The \(U_i\) classes are independent by edge-disjointness, as are the \(V_i\) classes, so this sum has rank \(k\).
Each nontrivial rank-one scalar test of a tensor still has a definite value on this fixed sum.
Alternative readings assembled along the same chains and the original pairing cannot create a conflicting product.
An argument excluding full erasure must impose additional relations on the possible certificates, or detect a surviving label by another method.

## Assessment history

### Decision alternative-matchings-on-repeated-paths

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:33 |
| status | proved |
| reason | Independent review verified the extensions on an arbitrary complement, the number of distinct marked matchings, their common tensor and the quotient scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The even bins in the prescribed law, the common mixed tensor and the conditional extension of all internal choices. |
| argument | [Proof](#extending-witnessed-matchings-on-even-blocks) | Alternating path splicing, simultaneous long reads and exact scopes of the existence and consistency statements. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0106_v1.md#whole-argument-finding) | Independent review of the matching arguments, probability estimates and the solvable-kernel corollary. |

## Current assessment

[Selected decision](#decision-alternative-matchings-on-repeated-paths)
