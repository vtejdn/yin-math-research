---
author: Yin
---

# Line incidence forces failures of common active steps in a paired color

## Statement

Use the [four selected lines and their allowed inverse pairing](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).
Call the six signed ordinary letters at their intersections *active*.
The 126 other points on each selected line are its *private* letters, paired into 63 inverse pairs within that line.
Fix one of the two sides, use forward labels, and take \(c\in\{3,5,6\}\).
Two vertices differ on an active letter if exactly one carries its outgoing stub.

In the four-line law, or in the [thirteen-position law](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers) with its lamp modulus fixed, let \(L=\lfloor c_0\log n\rfloor\) for a sufficiently small fixed \(c_0>0\).
There is a constant \(\gamma>0\) for which the following holds with probability tending to one conditional on girth, simultaneously on both sides and in all three colors.
For **every** partial pairing of vertices of color \(c\) by equal labels in the original cone group, more than \(\lfloor\gamma L\rfloor\) distinct group labels have an unmatched vertex or a pair differing on an active letter.
In particular, if the color is completely paired, some single active signed letter can be read on exactly one member of a pair at more than \(\lfloor\gamma L\rfloor/6\) distinct group labels.
This applies to any choice of pairs and proofs, allowing both sides and all coarse deck indices.
The geometry, root separations, original characteristic-two zero product and, in the thirteen-position law, the perfect coarse kernel may be imposed on the same tuples.
The proof identifies a set of \(z\) such labels from the four private-edge boundaries alone.
If a proportion \(\rho\) of that set occurs in the odd boundary of all four lines, then
\[
            z\ \ge\ 3^{\lfloor\lfloor\gamma L\rfloor/2\rfloor\,2\rho/(1+\rho)} .
\]
In particular a fixed positive proportion would force a positive power of \(n\) distinct labels.

There is a deterministic alternative on any connected tuple with these coarse type counts: if a proposed true partial pairing has the indicated unmatched or differing occurrences at only \(r\) distinct group labels, its original group kills a nonempty cyclically reduced word on the private letters with at most \(\max(1,r)\) monochromatic runs around the circle, where the color of a letter here is its private line.
The word length inside each run is unrestricted.
In the [connected high-girth realization with cone group \(C_7\)](../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group), the exact same coarse types and counts permit a genuine complete pairing with just two pairs differing on active letters, all at one original label.
That realization has torsion and fails the ordinary-arrangement and root-separation safeguards.

## A finite cycle from the four private lines

Fix \(c\), and let \(i\) range over the four selected lines.
Use the labelled Cayley multigraph of the actual cone group \(G\), keeping distinct rose edges even when their group elements agree.
Push all private \(i\)-edges of the side graph in this color to the Cayley graph by the forward root labels, and reduce their counts modulo two.
Write \(E_i\) for this finite binary edge chain and \(b_i=\partial E_i\).
The edges stay in color \(c\) since they have coarse increment zero.
Each \(E_i\) is nonempty: for **each** of its 63 inverse pairs the number of edges before projection is \(np/7-1\), counted by one oriented stub, with \(p=129/16513\).
The balanced value \(np/7\) is even at the admissible sizes, and the adjustment on the unique selected line through that private point is \(-1\).
This remains true after summing the fine-state counts in the thirteen-position law. [Coarse perturbations](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) · [Fine-state sums](Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms)

For an actual label \(g\) over \(c\), let \(a_g\) be the occurrence parity and let \(e_{ij}(g)\) be the parity of its vertices carrying the active intersection of lines \(i,j\).
For each original vertex the number of its ordinary stubs on line \(i\) is either \(1\) or \(129\), since its own ordinary type is one projective line.
Counting the ends of private edges therefore yields
\[
               b_i(g)=a_g+\sum_{j\ne i} e_{ij}(g)\quad\text{in }\mathbb F_2.
\]
In particular \(\sum_i b_i(g)=0\) since the active intersections occur twice.
Loops in the labelled Cayley multigraph also count both ends, as required for this boundary formula.
Let \(Z=\{g:b_i(g)\ne0\text{ for some }i\}\).
At a label all of whose vertices are paired with agreement on every active letter, \(a_g=0\) and every \(e_{ij}(g)=0\).
Thus every element of \(Z\) contributes a distinct label of the kind required in the statement.

If the support of one \(E_i\) contains a cycle, a simple cycle there gives a nonempty cyclically reduced null word on that one private alphabet.
This includes a loop or a cycle of two distinct parallel edges: reversal of a signed letter in a Cayley walk would reverse the same edge.
Otherwise all four supports are forests.
In each color \(i\) pair the edge ends at each vertex, leaving exactly one unpaired there if the degree is odd.
The resulting nonempty paths cover the edges, have distinct endpoints and are reduced, since no trail in a forest can close.
Their endpoints are the elements with \(b_i(g)=1\), each used just once for that \(i\).
Make a finite multigraph on \(Z\) with one edge of color \(i\) for each such path.
It is nonempty, and each vertex has positive even degree because \(\sum_i b_i=0\).
It has a simple cycle, allowing a pair of parallel edges.
At any vertex, at most one incident edge of any given color occurs, so successive paths in this cycle are on different private alphabets, including at the cyclic junction.
Concatenating them gives a nonempty cyclically reduced null word with at most \(|Z|\) monochromatic runs.
This proves the deterministic alternative and identifies actual group labels at the changes of line.

## Excluding private relations with few changes of line

We prove a property of the cone group that does not presuppose a pairing.
For some fixed \(\gamma>0\), with conditional probability tending to one no nonempty cyclically reduced word on the four private alphabets with at most \(\lfloor\gamma L\rfloor\) circular runs is trivial in \(G\).
Freeness for each individual 63-pair alphabet alone would allow relations alternating between different alphabets.

First let \(k_L\ge1\) be any prescribed integer sequence with \(k_L=o(L)\).
We use the [restricted-word counting proof](Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction) and its [outer-segment argument](Yin_C_A0059_v1.md#capped-pictures-with-an-outer-segment-in-the-chosen-letters).
As the allowed language take all reduced words with at most \(k_L+1\) linear runs from the four private alphabets, including their subwords and inverse readings.
Cutting a circular word with at most \(k_L\) runs at any point puts it in this language.
Only the uniform saving for each source grid block requires a change.

In the alignment step of [Ope26f, (3.5), pp. 10–11](../literature/pdf/Ope26f.pdf#page=10), let \(d\ge1\) be the fixed bound on the integer offset count after the ordinary interval and language-interval cuts.
Take \(N=\lfloor(L/(k_L+1))^{1/(2(d+1))}\rfloor,\ R=\lfloor\sqrt N\rfloor\).
These tend to infinity.
The same simultaneous pigeonhole argument supplies \(1\le u\le N^d\), with grid scale \(s=L/(uR)\) satisfying
\[
     \frac{L}{N^{d+1/2}}\le s\le L/R,\qquad
                  \max_a\operatorname{dist}(a/s,\mathbb Z)\le R/N .
\]
In particular \(s\ge\sqrt{L(k_L+1)}\), \(s=o(L)\), \(k_L/s=o(1)\), and the relative alignment error tends to zero.
The bounded number of chain-end fragments costs \(O(s)\) per chain, the \(O(L/s)\) block-bin choices have logarithmic cost \(O((L/s)\log(s+1))=o(L)\), and each recovered partner word is specified up to \(o(s)\) letters.
The numerical grid is still determined by the unlabelled pattern.

For a full block of length \(h=s+O(1)\), every permitted private word has turn weight \(129^{1-h}\).
There are 126 initial choices after specifying the first line and at most 125 continuations at any step that stays on its line.
At a change there are at most \(3\cdot126\) choices on the other lines.
Summing over at most \(k_L\) change positions bounds the word count by
\[
   504\,125^{h-1}\sum_{r=0}^{\min(k_L,h-1)}
                       \binom{h-1}{r}(378/125)^r
                     =125^{h}\exp(o(h))
\]
as an upper bound, uniformly over the pattern, since \(k_L/h\to0\).
For example the logarithmic cost of choosing the change positions is \(O(\log h+k_L\log(eh/k_L))=o(h)\).
Thus the total turn weight is at most \(\exp(-\xi s)\) for some fixed \(\xi>0\) for all sufficiently large \(L\), by \(125<129\).
In every bin \(d_i=\lfloor-\log P(W)\rfloor\) the restricted count is at most \(\exp(d_i+1-\xi s)\).

This is the only language-specific input to the restricted stage selection of C59.
One can mark each whole outer-contact interval as a language interval regardless of the number of changes of line inside it: a full grid word there is a subword of the chosen language.
The unrestricted link components retain the original squared-weight bound, and a dominant block with a language occurrence uses the preceding restricted bin saving.
Their product of numerical stage bounds has logarithm at most \(-cH+a_0 b+o(L)\) as in C59, for a fixed \(c>0\), total inner pattern length \(H\ge L\), and \(b\) unrestricted unmatched letters.
Choose \(\varepsilon>0\) small compared with \(c/a_0\) before the fixed pattern bounds.
A bounded number of stages and \(\exp(o(L))\) pattern and bin choices give probability \(\exp(-\Omega(L))\) for a forbidden bounded system with \(b\le\varepsilon H\) under the girth-conditioned law. [Stage selection and final union bound in Ope26f, (3.12)](../literature/pdf/Ope26f.pdf#page=14)
The seven-color and side-dependent lamp states only change the embedding factor by a bounded state power per stage and \(\exp(o(L))\) under the bounded type perturbations: after specifying the initial state of each component all its compared labels determine its successive states. [C65, stage estimates](Yin_C_A0065_v1.md#safeguarded-realizations)

Fix the diameter bound \(d_0L\) holding with conditional probability tending to one and write \(\mathcal G_L\) for this event.
For a nonempty cyclically reduced null word in the language, the reduced capped picture has at least one nonempty inner graph boundary.
Treat the whole linear outer reading as the one restricted segment in C59, with zero unrestricted outer length.
All retained contacts with that segment have allowed subwords, using its closure under inverse readings.
The splitting, closing and planar extraction on \(\mathcal G_L\) give exactly a forbidden bounded system as in [C59's capped-picture proof](Yin_C_A0059_v1.md#capped-pictures-with-an-outer-segment-in-the-chosen-letters).
The constants in that extraction depend on \(\varepsilon,d_0\) and the girth scale; the outer word contributes only one segment regardless of its length or its number of runs.
It follows that for each prescribed \(k_L=o(L)\) the conditional probability of \(\mathcal G_L\) together with such a null word of at most \(k_L\) circular runs is \(\exp(-\Omega(L))\).

To obtain a fixed linear cutoff, suppose for every positive integer \(j\) that the probability of this intersection at cutoff \(\lfloor L/j\rfloor\) exceeded \(\exp(-\sqrt L)\) at arbitrarily large admissible sizes.
Select one such size for each \(j\), with its \(L_j\) strictly increasing and at least \(j^2\).
Set \(k_{L_j}=\lfloor L_j/j\rfloor\) there and \(k_L=1\) elsewhere.
This is one deterministic \(o(L)\) sequence, contradicting its exponential probability bound at these sizes.
Hence some fixed \(j\) has intersection probability at most \(\exp(-\sqrt L)\) for all sufficiently large sizes.
With \(\gamma=1/j\), the diameter event then gives the asserted absence with conditional probability tending to one.
Since it is an event about the actual group, the deterministic cycle argument applies simultaneously to all the stated colors, sides and partial pairings.
For a complete matching, assign one differing active letter to each of the resulting distinct labels and use the fact that there are six such letters.

## Branching at labels in all four private boundaries

Put \(z=|Z|\) and let \(z_4\) be the number of its labels with \(b_i(g)=1\) for all four \(i\).
On the event just proved, each monochromatic \(E_i\) is a forest and the endpoint multigraph constructed above has girth greater than \(\lfloor\gamma L\rfloor\).
Indeed any simple cycle of \(r\) edges there gives the null word with \(r\) circular runs.
The multigraph has \(z_4\) vertices of degree four and \(z-z_4\) of degree two.
Start uniformly on its directed edges, then repeatedly choose a uniform edge out of the current vertex other than the reverse of the incoming edge.
The uniform directed-edge law is stationary because a given directed edge out of a vertex \(v\) has \(\deg(v)-1\) permitted predecessors, each passing to it with probability \(1/(\deg(v)-1)\).
At each step the conditional entropy given the path so far, averaged over the walk, is therefore \(\frac{4z_4}{2z+2z_4}\log3\).
Put \(q=\lfloor\lfloor\gamma L\rfloor/2\rfloor\).
For each fixed initial edge, distinct nonbacktracking continuations of length \(q\) have distinct final vertices: a repeat within a continuation or a collision between two continuations would give a cycle of length at most \(2q\) among the continuations.
Here one may start the continuations at the head of the initial edge and forbid its reverse on the first step.
Their conditional entropy is at most \(\log z\).
The entropy chain rule yields \(\log z\ge q\,\frac{2z_4}{z+z_4}\log3\), proving the stated bound.
The four-line populations alone supply no positive lower bound on the additional proportion \(\rho=z_4/z\) in this argument.

## What the exact vertex populations permit

Group the vertices of one specified color by the subset of the six active letters they carry.
Each ordinary line had even coarse-color population \(n/(7\cdot16513)\) before the perturbation.
Exactly the four selected lines now have odd totals in this color.
They give four distinct masks, the three intersections incident to the respective selected line.
No other line contains three active points: any three edges of the complete graph on the four line indices include two sharing an index, and those two intersections already determine the selected line of that index.
Thus exactly four masks have odd cardinality.
Pair within each mask leaving one vertex at each of these four, then pair the four remaining vertices in twos.
This gives precisely two pairs with differing active masks, and every pairing needs at least two because a differing pair can correct at most two odd mask counts.
In the [exact-type example of L52](../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group) every vertex in the color has the same original label, so this pairing is genuine there.
On the safeguarded tuples the growing obstruction comes from the original-group relations needed to close the private paths.
It forces failures of common readability in any putative complete matching, including outside any fixed number of true-label classes supplied by [known crossings between independent blocks](Yin_C_A0077_v1.md#matching-the-twelve-or-eighteen-marks).
It leaves open whether such a matching forces one common word to exchange two independent blocks with both parities changed, and whether the color can be erased on an exceptional safeguarded tuple.

## Assessment history

### Decision private-line-pairing-defects

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:46 |
| status | proved |
| reason | Independent review verified the private-edge boundary identity, the variable-language exclusion, the distinct-label count and the exact-mask comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous bounds for arbitrary partial true pairings on the stated event, with a deterministic private-word alternative and a conditional branching estimate. |
| argument | [Proof](#a-finite-cycle-from-the-four-private-lines) | Line incidence, turn counts with varying run bounds, a diagonal choice of constants, and the two-defect type comparison. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0114_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-private-line-pairing-defects)
