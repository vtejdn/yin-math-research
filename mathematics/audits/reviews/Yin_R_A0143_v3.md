---
author: Yin
---
# Fixed-depth endpoint counts for the seven Gardam triples

## Whole finding

At 2026-11-21T06:53 UTC an agent outside proof development independently reviewed the [statement](../../claims/Yin_C_A0106_v3.md#statement), [complete argument](../../claims/Yin_C_A0106_v3.md#argument) and [retained computation](../../computations/programs/Yin_J_A0007/readme.md) for Yin.
The reviewer received the fixed materials and scope without the proof-development discussion.
The [v1 finding](Yin_R_A0143_v1.md#whole-finding) and [v2 finding](Yin_R_A0143_v2.md#whole-finding) were consulted for the inherited inputs.
All seven triples give the asserted endpoint counts.
For any nonempty finite \(B\subset\Gamma\) with no singleton fiber in \(P\times B\to PB\), one has \(|B|\ge362\), and a triple fiber requires \(|B|\ge655\).
The resulting nonvanishing assertion holds over every field for every nonzero left coefficient supported on the seven positive generators and every nonzero right coefficient of support size at most \(361\).

**Independent enumeration.**
I regenerated the 98 two-letter rules from the seven triangle relators in C_A0105_v2 and joined all 560 overlapping reductions by always reducing the rightmost available pair.
Length decreases under every shortening rule, and the remaining negative-positive interchange decreases the number of negative-before-positive pairs.
Together with inverse cancellation and the equivalence of the triangle and two-generator presentations, these checks justify using irreducible words for elements of \(\Gamma\).
The sets of possible positive predecessors in the cyclic triangles give exactly \(bdg,bcf,afg,acd,ceg,abe,def\).

I enumerated color sequences separately from the maintained program, traversing a single edge at each recursion and keeping the inverse \(u^{-1}\) of the current group vertex \(u\).
A left-to-right step of color \(p\) appends \(p^{-1}\) to this inverse word, and a right-to-left step appends \(p\).
I excluded the preceding color, reduced the resulting word by rightmost reductions and counted every visit to the left side up to the specified depth.
Inversion is a bijection on endpoints, so these visit counts give the original multiplicities.
This computation started at the identity on the chosen side and imported no code from J_A0005, J_A0006 or J_A0007.

| Root and last depth | Multiplicity 1 | Multiplicity 2 | Multiplicity 3 | Distinct endpoints | Paths | Short endpoints remaining single |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Left, 16 | 126397 | 2238 | 66 | 128701 | 131071 | 127 through length 6 |
| Right, 17 | 250257 | 5577 | 244 | 256078 | 262143 | 63 through length 5 |

Each row is the full positive-multiplicity distribution for each of the seven triples.
Independently of that traversal, I ran J_A0007 with assertions enabled on all seven triples.
Its two-step transition multiplies on the left by \(p_k^{-1}p_i\), excludes immediate reversal at either step and adds the full incoming count to the new state.
The left-root initial state is the empty path, and the three right-root initial states on the left have words \(p^{-1}\) and incoming color \(p\).
The stored final color determines the permitted next step even when distinct paths have reached the same state.
Eight iterations therefore cover precisely the required lengths in both cases.
The intermediate path totals, final histograms and short-endpoint assertions all passed.

**Bounds on the finite subgraph.**
Right translation of the whole rectangle moves either chosen root to its side's identity, preserves all colors and preserves \(|B|\).
In the count below \(B\) denotes this translated support.
The graph induced by the rectangle has three choices at each left vertex and at least two at each right vertex.
From a left root, length two has at least three paths, and every subsequent pair of steps admits at least two continuations per path.
A degree-three right root supplies three paths of length one with the same continuation bound.
Thus the even family contains at least \(1+3(2^8-1)=766\) paths and the odd family at least \(3(2^9-1)=1533\).
At least \(1+3+6+12=22\) and \(3+6+12=21\) of the respective paths have lengths at most six and five.
Each is the only ambient path in its family to its endpoint.
Indeed, the short path and a different path to the same endpoint would together have length at most \(22\).
Their union would then be a tree by girth \(24\), and two given vertices of a tree admit just one nonbacktracking path.
This also covers the empty short path.

For \(i=0,1,2,3\), let \(b_i\) count vertices of \(B\) having ambient multiplicity \(i\) relative to the translated root.
The exact ambient path mass on \(B\) equals \(2|B|+b_3-b_1-2b_0\) and dominates the internal paths.
The two rows therefore give \(766\le2|B|+66-22\) and \(1533\le2|B|+244-21\) under their respective root hypotheses.
These yield \(361\) and \(655\) with arbitrary word lengths in \(B\).
Below \(655\), absence of singleton fibers forces degree two at every right vertex, whence \(3|B|=2|PB|\).
This excludes \(361\) and, more generally, every odd size below \(655\).

**Inherited inputs and scope.**
The v2 result on girth applies to exactly these graphs.
The index-six and \(C_4\oplus C_{28}\) abelianization assertions have the same subgroups as in v2.
I reran the full J_A0006 certificate for all seven triples and used the existing independent v2 review for the subgroup proof and integral computation.
Neither subgroup invariant enters the capacity inequalities.

A singleton product contributes a single nonzero scalar term over every field.
For three nonexceptional or at least four positive labels, the v1 criterion supplies such a product by choosing a maximal-length right normal word and a positive label whose join with it stays irreducible.
A competing pair would have to attain that same maximal concatenation length and hence give the same normal word, whose first letter determines the pair.
A single positive label is invertible up to its scalar.
For two distinct labels \(p,q\), v2 uses the infinite order of \(p^{-1}q\).
I checked the seven incidence lines from the triangles, their pair intersections, the unique completing letter on every incident pair and the hypotheses of the triangle-building construction recalled in [Cartwright and Młotkowski, §1(b), pp. 348–349](../../literature/pdf/CM94.pdf#page=4).
The resulting simply transitive vertex action has type increment one for every positive letter.
A finite-order type-preserving isometry fixes the circumcenter of a finite orbit in the complete CAT(0) building and then fixes the vertices of the simplex containing that center in its relative interior.
The vertex action is free, and the distinct one-letter normal forms show \(p^{-1}q\ne1\), so the ratio has infinite order.
On each right coset of its cyclic subgroup the normalized two-label factor acts by a nonzero Laurent polynomial, which is injective.
This review accepts the cited building construction at those hypotheses without re-proving the construction.
The bounds give necessary sizes and leave existence at or beyond them open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0106_v3.md#statement) | All seven triples, arbitrary finite nonempty right supports, both root hypotheses, parity and the all-field corollary through size 361. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0106_v3.md#argument) | Entire proof, including histograms at the two fixed depths, forced short endpoints, bounds on internal paths, capacities, parity and cases for the left support. |
| [Whole finding](#whole-finding) | [J_A0007 reproduction scope](../../computations/programs/Yin_J_A0007/readme.md) | Required inputs, asserted path families and limits of the seven-triple run. |
| [Whole finding](#whole-finding) | [J_A0007 verifier](../../computations/programs/Yin_J_A0007/verify.py) | Transitions, initial states, accumulation, normal-form implementation, final and intermediate checks and numerical bounds, with full independent enumeration of the final histograms. |
| [Whole finding](#whole-finding) | [J_A0006 input](../../computations/programs/Yin_J_A0006/verify.py) | The seven keys used by J_A0007 and the rerun of the existing girth and subgroup certificate. |
| [Whole finding](#whole-finding) | [J_A0005 input](../../computations/programs/Yin_J_A0005/verify.py) | Triangle rules, presentation checks and joins used in the J_A0007 run. |
| [Whole finding](#whole-finding) | [Presentation](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation) | Identification of the group used for path endpoints. |
| [Whole finding](#whole-finding) | [Word problem](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) | Validity, termination and confluence of the two-letter rules. |
| [Whole finding](#whole-finding) | [Previous statement](../../claims/Yin_C_A0106_v2.md#statement) | The same seven incidence graphs, girth and unchanged subgroup assertions. |
| [Whole finding](#whole-finding) | [Previous argument](../../claims/Yin_C_A0106_v2.md#argument) | Existing girth and subgroup proof with the precise applicability and review depth stated above. |
| [Whole finding](#whole-finding) | [Nonexceptional supports](../../claims/Yin_C_A0106_v1.md#argument) | Scalar outermost coefficient criterion for a maximal-length right input word. |
| [Whole finding](#whole-finding) | [One- and two-label cases](../../claims/Yin_C_A0106_v2.md#combining-the-exceptional-and-nonexceptional-supports) | Group-element units and injectivity of a Laurent binomial on each right coset. |
| [Whole finding](#whole-finding) | [Building input](../../ledger/Yin_L_A0067_v1.md#the-group-and-the-biradial-convention) | Triangle presentation, simply transitive vertex action and type increment for the two-label case. |
