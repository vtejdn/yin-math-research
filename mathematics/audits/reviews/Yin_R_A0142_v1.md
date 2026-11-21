---
author: Yin
---
# Zero products on the Mian–Siddique witness

## Whole finding

At 2026-11-21T05:49 UTC an agent outside the development of C105 v1 independently reviewed its [statement](../../claims/Yin_C_A0105_v1.md#statement), [argument](../../claims/Yin_C_A0105_v1.md#argument) and [verifier](../../computations/programs/Yin_J_A0004/verify.py) for Yin.
The reviewer received the fixed inputs and the questions to check, without the proof-development discussion or an earlier verdict on this claim.
The proof excludes zero products over every field for every pair of nonempty supports contained in the indicated 32 rows and 28 columns.

The reviewer checked the presentation on p. 2, the cyclic generator images on p. 3, the two permutation cycles on p. 4 and all 60 words in their printed order on p. 10 of the [retained arXiv v1](../../literature/pdf/MS26b--arxiv-v1.pdf).
The abelianized relators have exponent vectors \((5,-2)\) and \((1,8)\), hence vanish under \((a,b)\mapsto(-8,1)\) modulo 42.
In the right Cayley graph a free cancellation traverses the same edge twice, and an inserted conjugate \(w r^{\pm1}w^{-1}\) traverses its stem twice and a relator loop at the endpoint of \(w\).
The stem cancels in the parity chain, and the remaining summand vanishes modulo the span of the translated relator chains.
Both changes preserve the endpoint, so each group-product fiber is contained in a single signature class.
Summing the zero coefficient at each group element within that class gives the required class equation in \(k\), regardless of its characteristic.

An independent implementation extracted the word lists from the PDF text layer, represented each permutation by its inverse, and numbered vertices in lexicographic order.
Symmetric differences of edge sets and elimination on the least edge in each nonzero relator chain gave 168 vertices, 336 directed generator edges and relator rank 161.
Both relators closed at every vertex.
There were 32 distinct row signatures and 28 distinct column signatures.
The independent partition agreed with the program on the membership of every cell of every class, including all 230 classes of size two and 53 classes of size three.

For an independent exhaustion, the reviewer used Boolean variables \(r_i,c_j\) for the support labels and \(e_{ij}\) for the 896 cells.
Three clauses for each cell enforce \(e_{ij}\leftrightarrow(r_i\land c_j)\).
For every class \(T\) and each cell \(t\in T\), the clause \(\neg e_t\lor\bigvee_{s\in T\setminus\{t\}}e_s\) requires a second selected cell whenever \(t\) is selected.
Requiring at least one row and one column gave 3,586 clauses on 956 variables.
Partitioning by the least selected row and column gave 896 disjoint initial cases.
Unit propagation followed by branching on both values of an undecided support label exhausted them in 2,082 search nodes, counting the initial cases.
There were precisely three models, with row sets equal to all rows, \(I_1\), and \(I_2\) as printed in C105, and all 28 columns in each.
The original verifier also passed with assertions enabled and checked the exact row and column masks.

For a pair \(((i,j),(k,l))\) in one of the two-cell restrictions set \(D=(x_i y_j)/(x_k y_l)\).
All factors are nonzero on the support, and the pair equation gives \(D=-1\).
For each of the three rows of the certificate table, the reviewer checked equality of each indicated pair and triple with its entire restricted class.
Taking the first pair ratio times the inverse second ratio times the third ratio cancels the intermediate variables.
The result is \((x_0y_6)/(x_3y_1)\) for all rows and for \(I_1\), and \((x_4y_2)/(x_9y_0)\) for \(I_2\).
In every case its value is \((-1)(-1)^{-1}(-1)=-1\), so the triple equation forces \(x_7y_8=0\) in the first two cases and \(x_{16}y_3=0\) in the third.
Each is impossible on the given support, also in characteristic two.
The exclusion uses only the presentation and the printed witness.
The paper's Lean development and Gardam's torsion-freeness assertion lie outside this review, as do supports beyond this rectangle.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0105_v1.md#statement) | All nonzero elements over any field with supports in the respective Appendix A lists. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0105_v1.md#argument) | The necessary equations, all allowed support rectangles and all three coefficient contradictions. |
| [Whole finding](#whole-finding) | [Computation description](../../computations/programs/Yin_J_A0004/readme.md) | Source transcription, invocation and scope of the finite calculation. |
| [Whole finding](#whole-finding) | [Verifier](../../computations/programs/Yin_J_A0004/verify.py) | Exact source words, group images, relator chains, all 896 cell memberships, support enumeration and ratio checks. |
| [Whole finding](#whole-finding) | [Source presentation and finite images](../../claims/Yin_C_A0105_v1.md#necessary-coefficient-equations-from-a-finite-quotient) | The presentation, generator images, witness order and formalization scope on pp. 2–4, 7 and 10 of Mian–Siddique v1. |
