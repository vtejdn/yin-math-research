---
author: Yin
---
# Girth, subgroup index and support bounds for the seven Gardam triples

## Whole finding

At 2026-11-21T06:40 UTC an agent outside proof development independently reviewed the [statement](../../claims/Yin_C_A0106_v2.md#statement), [complete argument](../../claims/Yin_C_A0106_v2.md#argument) and [J_A0006 verifier](../../computations/programs/Yin_J_A0006/verify.py) for Yin.
The reviewer received the claim, its dependencies and the requested scope without the proof-development discussion.
The earlier [review of v1](Yin_R_A0143_v1.md#whole-finding) was consulted for the outermost-coefficient input before the new computations.
For each of \(bdg,bcf,afg,acd,ceg,abe,def\), the exact girth is \(24\), the ratio subgroup has index six and its abelianization is \(C_4\oplus C_{28}\).
Absence of uniquely represented products requires at least \(126\) right factors, increasing to \(189\) when there is also a triple fiber.
The corollary for every field and every nonzero left coefficient supported on the seven positive generators holds for every nonzero right coefficient of support size at most \(125\), without a restriction on its radius.

**Words and girth.**
The oriented faces on [Gardam's Warwick slides, 25 November 2021, slide 12 of 13](../../literature/pdf/Gar21c.pdf#page=12) give the seven triangle words used in C_A0105_v2.
The same slide displays the two defining relators, which also appear in [Mian–Siddique, arXiv v1, p. 2, (1)](../../literature/pdf/MS26b--arxiv-v1.pdf#page=2).
Eliminating the five additional letters fixes \(a,b\) and, by free reduction, sends the seven triangle words to five empty words, \(R_1\) and \(bR_2b^{-1}\).
Hence the two presentation maps are inverse.
I regenerated all 98 rewriting rules from the oriented triangles and joined all 560 overlapping reductions by taking the rightmost reducible pair at every step.
Every rule is an equality in the triangle group, the rules include inverse cancellation and imply all the triangular relators, and the ordered pair of word length and negative-before-positive inversions decreases at every step.
Termination and the overlap checks therefore make irreducible words exact group-element identifiers.

The ordinary run of J_A0006 with assertions enabled completed for all seven triples.
For a separate count I stored the inverse of the group element at a vertex and updated it by appending \(p^{-1}\) on a forward step and \(p\) on a return step, normalizing by rightmost reduction.
For each triple the counts \(3\cdot2^{j-1}\) for \(1\le j\le11\) gave 6,142 distinct vertices together with the root, keeping the two sides separate.
At depth 12 there were 6,120 endpoints reached once and 12 reached twice, accounting for all 6,144 paths and giving the first collisions.
Right translation sends a left vertex of any shorter cycle to the root, where its two half-paths would already collide by depth 11.
I also checked that each specified 24-step circuit returns to the root and has 24 distinct vertices before its final step.

**Right-support bounds.**
When every fiber has at least two elements, the incidence graph on \(B\sqcup PB\) has left degree three and right degrees two or three.
From each endpoint of a chosen edge consider the nonbacktracking paths of length at most 11 that avoid that edge on their first step.
A path with a repeated vertex contains a cycle, and two distinct simple paths from the same root to the same vertex give a cycle of length at most 22.
If the opposite families meet, truncation at a first intersection and the original edge give a cycle of length at most 23.
The left vertices counted by the two families are consequently all distinct.
The left-rooted family contains at least \(1+2+4+8+16+32=63\) left vertices, and the right-rooted family contains at least \((\deg w-1)63\) for right root \(w\).
This gives 126 in general and 189 upon choosing a right root of degree three.
A zero product over a field has no singleton fiber because its contribution would be a single nonzero coefficient product.
When all fibers have degree two, \(3|B|=2|PB|\) makes \(|B|\) even.
Neither lower bound asserts attainability.

**Index and abelianization.**
I checked the seven six-state permutation tables against both presentation relators at every state.
The two ratios fix the base state, and the six given representatives reach distinct states, giving the lower index bound.
I independently evaluated each of the \(7\cdot12\) Schreier identities by concatenating its two sides with the second inverted and taking its rightmost normal form.
Each comparison reduced to the empty word, as did the balanced freely reduced length-sixteen relation in each pair of ratios.
The Schreier identities close the union of the six represented right cosets under both positive generators and, by inverse transitions, under their inverses.
The union contains the identity, so it is the whole group and the six-point action is the required coset action.

For a separate integral calculation I traced the two relators from each of the six states and retained all 12 oriented positive edges.
This gives the cellular boundary \(\partial_2\) in the uncontracted cover.
Using integer row operations on the twelve boundary rows gave seven independent rows spanning the same lattice.
The positive greatest common divisors of their \(k\)-rowed minors for \(k=1,\ldots,7\), computed using fraction-free determinants, were
\[
                    1,\quad1,\quad1,\quad1,\quad1,\quad4,\quad112
\]
in all seven cases.
Successive ratios give invariant factors \(1,1,1,1,1,4,28\).
The connected six-vertex graph has \(\operatorname{im}\partial_1\cong\mathbb Z^5\), as one also sees by taking the differences of the six vertices along a spanning tree.
The exact sequence \(0\to H_1\to C_1/\operatorname{im}\partial_2\to\operatorname{im}\partial_1\to0\) splits over that free group.
The middle term has rank \(12-7=5\), hence \(H_1\) equals its torsion subgroup \(C_4\oplus C_{28}\).
The computed \(H_1\) is the abelianization of \(H_P\) because the cover of the presentation complex of \(\Gamma\) has fundamental group \(H_P\) at the base vertex.
This confirms the contracted \(12\)-by-\(7\) calculation without using the verifier's tree or its Smith reduction.
It gives 112 complex characters of exponent dividing 28 and excludes a nonzero additive real character.
The subgroup is nontrivial and finitely generated, so it also fails local indicability.

**Source use and the seven-generator corollary.**
The cyclically read triangle words give seven distinct three-point lines.
Each pair of distinct points occurs in exactly one line, and the 21 ordered incident pairs each determine one completing letter, which verifies the projective-plane and cyclic-triple hypotheses.
The [published article of Cartwright and Młotkowski, §1(b), pp. 348–349, PDF pp. 4–5](../../literature/pdf/CM94.pdf#page=4) recalls the building construction from its reference [2], Theorem 3.4.
Page 349 identifies the vertices with group elements, assigns type \(+1\) to each positive generator, and states simple transitivity on vertices.
In the complete CAT(0) Euclidean building the circumcenter of a finite orbit is fixed, and type preservation then fixes each vertex of the simplex containing that center in its relative interior.
Simple transitivity and the distinct one-letter normal forms imply that \(p^{-1}q\) has infinite order for \(p\ne q\).
The right cosets of \(\langle p^{-1}q\rangle\) give Laurent polynomial modules, on each of which \(1+\lambda p^{-1}q\) acts injectively for \(\lambda\ne0\).
A single label is a unit up to its nonzero coefficient.
For three labels outside the list, or four to seven labels, the scalar boundary argument in C_A0106_v1 gives a uniquely represented product by choosing a maximal-length right word and an eligible left letter.
At a positive initial symbol only the listed predecessor triple is forbidden, at an inverse symbol only its corresponding positive letter is forbidden, and the empty word admits all labels.
The remaining cases are exactly the seven triples covered by the lower bound 126.

Normalizing a triple-supported coefficient by \(x^{-1}\) preserves the annihilator equation and gives an element of the subgroup algebra.
Right translation of any nonzero annihilated coset component then gives a nonzero annihilator in that algebra.
Gardam's slide 12 also states nonlinearity over \(\mathbb C\).
The claimed inheritance by the subgroup follows because a faithful representation of a finite-index subgroup induces a faithful representation of the full group, as detected by the base coset and its block.
The source inspection verifies that premise as an assertion of the slide and accepts the cited triangle-building theorem at its stated hypotheses.
The general nonlinearity theorem and the original construction of Euclidean buildings were outside this proof inspection.
Finite-support regularity for larger exceptional supports and the general zero-divisor question remain open here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0106_v2.md#statement) | All seven triples, both conditional support bounds, subgroup conclusions, all fields and unrestricted right radius up to 125 right support elements. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0106_v2.md#argument) | Entire proof from the finite girth certificate through the last section, including the tree count, index, integral abelianization, two-label argument, coset reduction and source-dependent nonlinearity implication. |
| [Whole finding](#whole-finding) | [J_A0006 scope](../../computations/programs/Yin_J_A0006/readme.md) | Full seven-triple run, reproduction inputs and mathematical interpretation of the reported outcomes. |
| [Whole finding](#whole-finding) | [J_A0006 verifier](../../computations/programs/Yin_J_A0006/verify.py) | Exact tables, words, paths, transitions, boundary matrices and Smith calculations for every case, with an independent recomputation. |
| [Whole finding](#whole-finding) | [J_A0005 word operations](../../computations/programs/Yin_J_A0005/verify.py) | Presentation words, generator substitutions and the finite normal-form operations used by J_A0006. |
| [Whole finding](#whole-finding) | [Presentation identification](../../claims/Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation) | Seven triangular relators, five eliminations and inverse presentation maps. |
| [Whole finding](#whole-finding) | [Word problem](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) | Validity, termination and confluence of the exact equality test and its metric consequence. |
| [Whole finding](#whole-finding) | [Outermost coefficients](../../claims/Yin_C_A0106_v1.md#argument) | Scalar one-letter terminal criterion for nonexceptional positive supports and arbitrary nonempty finite right supports. |
| [Whole finding](#whole-finding) | [Building input](../../ledger/Yin_L_A0067_v1.md#the-group-and-the-biradial-convention) | Projective-plane and triangle-presentation data, the vertex action and the type map used for two distinct labels. |
