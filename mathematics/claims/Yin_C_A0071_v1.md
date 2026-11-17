---
author: Yin
---

# Separating original labels of six-vertex blocks with identical pairing data

## Statement

Fix \(k\ge1\) and \(0<\delta<1\), and use the [four-line matching law with thirteen visible coordinates](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers).
There are constants \(c_0,\beta>0\), fixed as \(n\) tends to infinity through the admissible sizes, for which the following holds with probability tending to one conditional on girth at least \(L=\lfloor c_0\log n\rfloor\).
In each left fine state of coarse color \(3\) there are \(D=n^{\beta+o(1)}\) different neutral words \(u\) and \(h=\lfloor n^{1-\delta}\rfloor\) simple paths for each \(u\).
All \(hD\) paths in the state are vertex-disjoint.
Each path contains two disjoint blocks of six marked vertices.
The original group labels within the first block all equal some \(g\), and within the second they all equal \(g\pi(u)\), where \(\pi\) is the map from the free rose group to the cone group.
These two labels are different on **every** path, although their thirteen visible state coordinates agree.
Every one of the fifteen internal perfect matchings of **every** block has the same nonzero mixed tensor of rank one, independent of the word, the path, the fine state and the choice of matching.
Its constituent path displacements have zero ordinary first homology in the full relation subgroup.

For a fixed such state one can choose one of the two blocks on **each** of its \(hD\) paths so that the conditional probability of equal original labels for two independent uniform draws with replacement from these chosen blocks is at most
\[
                  \frac{\lceil h\sqrt{D/2}\rceil}{hD}.
\]
The sampling here is on a fixed realized tuple after choosing the blocks.
Even before choosing one endpoint per path, independent uniform draws from all \(2hD\) blocks have coincidence probability at most \(1/4+O(D^{-1/3})\).
All these assertions coexist with the [thirteen necessary relator-index bounds and the perfect coarse kernel](Yin_C_A0065_v1.md#statement).
If the whole color paired by actual equalities, no pair in such a matching could join the two blocks of any one displayed path, and the internal alternatives on all displayed blocks could be extended using a common complement matching.
There is no full erasure assumption in the construction of the paths.
It provides separation on the specified collection without requiring any general separation between disjoint paths.

## Short words separating original labels

Write \(d=7(4k+1)^{13}\) for the number of states per side and \(p=129/16513\) for the frequency of an ordinary letter.
In the chosen law, small-set expansion gives a fixed diameter bound \(d_0 L\), and the stage comparison gives the bounded-pattern exclusion for \(\varepsilon>0\) chosen before the fixed bounds on path count, total length multiple and interval count. [C65, geometric estimates](Yin_C_A0065_v1.md#safeguarded-realizations) · [Comparison for the two side actions](Yin_C_A0060_v1.md#geometric-safeguards-and-the-absence-of-group-quotient-certificates)
Degree at least 129, girth at least \(L\), and \(\log_2(2n)\le(1+2/(c_0\log2))L\) for large \(n\) supply the other conditions of Mghirbi and Douglas's Definition 3.3.
Apply the bounded-pattern estimate at the fixed triple of their definition for these constants.
Consequently, with conditional probability tending to one, a nonempty cyclically reduced trivial rose word has length at least \(c_* L\), where \(c_*=13\varepsilon/16>0\).
Indeed a reduced filling has at least one nonempty immersed graph boundary, of length at least \(L\), and its total inner length is at most the outer length divided by \(c_*\). [Mghirbi–Douglas, Proposition 4.4 and proof of Theorem B](https://arxiv.org/html/2611.04599v1#S4.SS4) · [Marked systole calculation](../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws)
In particular the free group maps injectively on its ball of radius strictly less than \(c_*L/2\).

Use \(a=\delta/2048,\ b=a/2,\ R=\lceil a\log n/\log64\rceil\).
Choose \(c_0>0\) sufficiently small for C65 and for \(c_0\log(2d|T|/p)<a/4,\ 2c_0\log132<1\), where \(T\) denotes the signed alphabet.
After fixing the resulting geometric constants choose \(\lambda>0\) so that
\[
            \lambda<c_*c_0/3,\qquad \lambda(\log2+\log300)<\delta/8 .
\]
Set \(\ell=\lfloor\lambda\log n\rfloor,\ D=2^\ell,\ \beta=\lambda\log2\).
Given two distinct ordinary generators with identity increments in the full state action, take all length-\(\ell\) positive words on these two chosen orientations.
On the marked systole event their group elements are nonidentity, mutually distinct and different from all their inverses, for every such alphabet choice and large \(n\).
This follows by injectivity on the ball containing the words, the identity and the inverse words.
Positivity in the two chosen generators gives the required free-group distinctions.

## Constructing both blocks in one matching law

Use ordinary letters with ordinary inverses and identity state increment.
Every vertex carries at least 120 of these letters.
In any fixed state the pool for one such letter has size \(np/d+O(1)\), and the simultaneous pool for any two distinct ones has \(n/(16513d)+O(1)\) vertices, since two projective points determine one line.
The bounded changes are those of C65.
Thus a fresh partner in a prescribed usable turn has conditional probability at least \(1/300\) as long as \(O(n^{1-b})\) vertices have been touched.
Reveals in one state for these letters use only matching blocks internal to that state.

On each side at its designated zero state use the [neutral simple-cycle search](Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts) with \(R,a,b\) above.
Its tree growth and connector use exactly the preceding per-vertex and per-turn bounds, giving a simple cycle word of length at most \(2R+2\) except with probability \(\exp(-\Omega(n^{a-b}))\) per side before girth conditioning.
Call the two words \(U,V\) in side order.
Choose a neutral usable signed letter \(s\) outside the inverse pairs of the first and last letters of \(U,V\).
Then \(W=[sUs^{-1},V]\) is cyclically reduced with \(|W|\le8R+12\), as in the [repeated commutator construction](Yin_C_A0070_v1.md#repeated-paths-with-independent-mixed-signatures-in-the-even-bins).
The word \(W\) is trivial in the original group because the graphs are coned.
Choose the two generators of the short positive words from different usable inverse pairs, both avoiding the end-letter pairs of \(W\).
Each of the following \(D\) words is freely reduced, has length at most \(H=80R+120+\ell\), and preserves the entire fine state at each step:
\[
                              W^5\,u\,W^5 .
\]

Conditional on the two unconditioned cycle searches, the matching blocks within each left fine state of coarse color 3 retain their original independent uniform laws.
Distribute \(\lfloor n^{1-b}/(H+1)\rfloor\) trials in a state as evenly as possible among the \(D\) words, and mark all visited vertices including failed trials.
A fresh first-stub vertex can be chosen at each trial since every fixed first-stub pool has linear size.
At each next edge demand a fresh partner carrying the prescribed next letter, or just a fresh partner at the end.
The [fresh-path comparison](Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths) gives conditional success probability at least \(300^{-H}\) and vertex-disjoint successful paths.
For each word its binomial lower comparison has expectation at least
\[
 n^{\,1-b-\lambda\log2-(80a/\log64+\lambda)\log300-o(1)}
                         > n^{1-\delta/2}
\]
for large \(n\).
Thus one can keep exactly \(h\) successful paths per word except with probability \(D\exp(-\Omega(n^{1-\delta/2}))\) in this state.
There are only \(d/7\) states to check.
The within-block switches for C65 bound the reciprocal girth probability by \(\exp(O(n^{3a/8}\log n))\): the short-cycle bad-edge expectation is at most \(n^{a/4+o(1)}\), and at most \(n^{3a/8}\) switches suffice on a set of measure at least \(1/2\). [Switching and its inverse count](Yin_C_A0053_v1.md#conditioning-and-what-is-paired)
Since \(a-b=a/2>3a/8\), both the cycle and open-path failure probabilities still tend to zero after conditioning.
We may intersect with the pattern-free, connected, root-separated and perfect-kernel events within this **same** state law.

Mark the start and the five successive ends of the copies of \(W\) in each half of a successful path.
All six labels agree in each block because \(W=1\), and the bridge multiplies their common label on the right by \(\pi(u)\).
All twelve vertices are distinct since the path is simple and \(\ell>0\).
For the mixed homomorphism on based displacements, each consecutive \(W\) contributes
\[
                     T_0=[U]_3\otimes[V]_3 .
\]
The two cycle bases have coarse color zero, the starts have coarse color 3 and the conjugating spacer is neutral.
Both cycle classes are nonzero because the cycles are simple, and the left summand at coarse index 3 survives the deletion of index zero. [C66, mixed displacement and deck indices](Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple)
Conjugates of \(W\) are commutators in the relation subgroup, so all their first-homology classes there vanish, including before any deck-index projection.
Number the six marks in a block from 0 to 5.
The path from mark \(i\) to mark \(j\) has mixed value \((j-i)T_0\), and every internal matching has total \(3T_0=T_0\), since three indices are odd.
If a full matching exists, take any matching internal to each displayed even block and splice it with the full matching along alternating paths on their union to obtain a matching on the complement. [C70, common complement](Yin_C_A0070_v1.md#extending-witnessed-matchings-on-even-blocks)
Every choice of the internal matchings extends with that complement.

## Choosing blocks with small coincidence probability

For one fine state, form an undirected multigraph on the true group labels of the displayed blocks, making each path an edge between its two labels.
There are \(hD\) edges and no loops.
A fixed unordered pair of labels \(\{g,g'\}\) determines the two possible connector values \(g^{-1}g'\) and its inverse.
At most one word \(u\) has either value, and there are only \(h\) rows for that word, so every pair has multiplicity at most \(h\).
Consequently the edges with both ends inside any set of \(s\ge1\) labels number at most
\[
                 h\min(D,\tbinom s2)\le h s\sqrt{D/2}.
\]
Give each label \(B=\lceil h\sqrt{D/2}\rceil\) available slots and match rows to slots of either of their endpoints.
For any subset of rows having \(s\) distinct endpoints, all its rows are among the internal edges just bounded and its neighboring labels have \(sB\) slots.
Hall's theorem therefore assigns every row a slot.
Keep the block of its assigned endpoint.
Each label now receives mass at most \(B/(hD)\) for a uniform draw, hence the sum of the squared label masses is at most the same bound.
The assignment uses actual group labels.
For a supplied pattern-free tuple with certified comparison constants it can be found by the [individual tuple algorithm](Yin_C_A0052_v1.md#statement) followed by finite bipartite matching.

For a uniform draw from all the blocks before assignment, each atom has mass at most \(1/2\) since every row has different endpoints.
A set \(S\) of at most \(s\) labels contains both ends of at most \(h\binom s2\) rows, so its mass is at most \(1/2+\binom s2/(2D)\).
Take \(S\) to consist of the \(s=\lfloor D^{1/3}\rfloor\) heaviest atoms, or all atoms if fewer occur.
Each remaining atom has mass at most \(1/(s+1)\).
The sum of squared masses on \(S\) is at most half its mass, and the sum outside is at most \(1/(s+1)\), giving the claimed raw bound.
These two sampling bounds concern the constructed blocks on each realized graph.
They require no independence of their group labels under the matching law.

## Assessment history

### Decision separating-six-vertex-blocks

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:03 |
| status | proved |
| reason | Independent review checked the marked systole, turn and exposure estimates, label separation and conditional sampling bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Pairs of true blocks with identical state and internal tensor, and sampling bounds on each realized thirteen-position tuple. |
| argument | [Proof](#short-words-separating-original-labels) | Short word separation, simultaneous open paths and allocation of blocks by Hall's theorem. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0107_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-separating-six-vertex-blocks)
