---
author: Yin
---
# Every subrectangle of the Mian–Siddique witness excludes zero products

## Statement

Let \(\Gamma=\langle a,b\mid aba^2b^{-1}a^2b^{-2},\,ab^3ab^4a^{-1}b\rangle\).
Take \(A,B\) to be the two lists of sizes 32 and 28 in [Mian and Siddique, arXiv v1, Appendix A, p. 10](../literature/pdf/MS26b--arxiv-v1.pdf#page=10).
For **every field** \(k\) and nonzero \(u\in k[A],v\in k[B]\), one has \(uv\ne0\) in \(k[\Gamma]\).
This includes arbitrary nonempty subsets on either side.

Mian and Siddique prove that \(AB\) has no uniquely represented product; their theorem checks a partner for every one of the 896 products.
Their Sections 1 and 7 distinguish the formal non-unique-product result from the torsion-free lattice description attributed to Gardam.
The coefficient exclusion below needs only the given presentation, so it does not require a separate proof of that description.
It applies to this support rectangle; [A0002](../tasks/Yin_T_A0002_v1.md#contract) also includes all other finite supports on this and other torsion-free groups.

## Argument

### Necessary coefficient equations from a finite quotient

Use the joint image \(Q\) of the two homomorphisms in Sections 2.2 and 3.2 of the paper.
The cyclic coordinate in \(\mathbb Z/42\) sends \(a\) to \(-8\) and \(b\) to \(1\).
In the permutation coordinate on \(\{0,1,2,3\}\) use \(a=(0\,1\,2)\) and \(b=(1\,3\,2)\), composing permutations as functions.
The [finite verifier](../computations/programs/Yin_J_A0004/readme.md) enumerates 168 states by right multiplication in the joint image and checks both relators at every state.
In this directed Cayley graph let \(C\) be the \(\mathbb F_2\)-space with a basis consisting of the outgoing \(a\)-edge and \(b\)-edge at each vertex.
For a word starting at the identity, record its endpoint in \(Q\) and the vector in \(C\) giving the parities of its edge traversals, identifying traversal of an edge backwards with traversal of the same edge.
Quotient \(C\) by the span of the chains of both relators starting at all vertices.
Inserting or removing a free cancellation preserves the chain.
Inserting a relator loop or its reverse at any place changes it by a vector in this span and preserves the remainder of the path.
These changes generate equality in the presented group, including insertion of a conjugate relator followed by free reduction.
Thus equal group elements have the same endpoint and quotient chain.
No converse to this implication is needed.
The use of \(\mathbb F_2\) to label paths puts no restriction on the coefficient field \(k\).

Partition the cells \((i,j)\) by the signatures of their product words, numbering rows and columns from zero in appendix order.
The rank of the relator chains in the 336-dimensional edge space is 161.
The number of buckets of each size is

| Size | 2 | 3 | 4 | 5 | 6 | 7 | 10 | 11 | 12 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Buckets | 230 | 53 | 26 | 10 | 8 | 6 | 1 | 1 | 1 |

The individual row signatures are distinct, as are the individual column signatures.
In particular the lists define genuine sets of the stated sizes in \(\Gamma\).
Write \(x_i,y_j\) for their coefficients.
If the group-ring product is zero, summing its coefficient equations over the group elements in each bucket gives
\[
                              \sum_{(i,j)\in T}x_i y_j=0
                              \quad\text{for every bucket }T.
\]
A bucket can be a union of actual fibers; these equations are necessary even when that union is strict.

### Exhaustion of support choices

For the nonzero row and column coefficients let \(I,J\) be their index sets.
No bucket can meet \(I\times J\) in exactly one cell.
Exhaustion gives exactly three rectangles satisfying this condition with both sides nonempty.
Each contains all 28 columns.
The three row sets are respectively all rows and
\[
\begin{split}
 I_1&=\{0,1,2,3,4,5,6,7,9,10,11,12,17,18,26,27,31\},\\
 I_2&=\{4,8,9,13,14,15,16,19,20,21,22,23,24,25,28,29,30\}.
\end{split}
\]

The calculation in J_A0004 starts with none of the 60 labels decided, keeping separate disjoint sets of required and forbidden labels.
A cell is possible if both endpoints avoid the forbidden set and is required if both endpoints are required.
If only one cell remains possible in a bucket, it cannot be required; if it has just one undecided endpoint that endpoint is forbidden.
If exactly two cells remain possible and one is required, both endpoints of the other are required.
Every application of these implications preserves all completions satisfying the necessary condition.
Conflicting assignments and an empty allowed side have no such completion.
When propagation stops, branch on one undecided label, requiring it in one branch and forbidding it in the other.
The two branches exhaust the completions without overlap, and at a terminal assignment the same tests detect exactly a singleton bucket.
Thus the printed three rectangles are obtained without assuming any lower bound on support size, any group-word decision procedure, or any restriction on coefficient phases.

### Three short contradictions

Put \(R_{ik}=x_i/x_k\), \(C_{lj}=y_l/y_j\) on each surviving rectangle.
A bucket reduced to the two cells \((i,j),(k,l)\) gives \(R_{ik}=-C_{lj}\).
In each line below all three adjacent relations in the path are of this form, allowing the equality to be read in either direction.
The listed triple is an entire bucket after restriction to the indicated rectangle.

| Row set | Three-pair path, with a minus sign at each step | Triple |
| --- | --- | --- |
| All | \(R_{0,3},\ C_{20,13},\ R_{23,19},\ C_{1,6}\) | \((0,6),(3,1),(7,8)\) |
| \(I_1\) | \(R_{0,3},\ C_{20,13},\ R_{26,31},\ C_{1,6}\) | \((0,6),(3,1),(7,8)\) |
| \(I_2\) | \(R_{4,9},\ C_{17,16},\ R_{23,19},\ C_{0,2}\) | \((4,2),(9,0),(16,3)\) |

The verifier checks every required pair and triple against the signature buckets after restriction, including the order of the two ratios at each step.
The three signs give \(R_{ik}=-C_{lj}\) for the first two cells of the triple, so those two contributions cancel.
The remaining cell has two nonzero coefficients and cannot vanish in any field.
This also holds in characteristic two, where two equal contributions add to zero.
It excludes all three choices and proves the statement.

The inspected source is the 10-page [arXiv v1](https://arxiv.org/abs/2609.22380v1), with the presentation and finite images on pp. 2–4, the formalization limits on p. 7 and the word lists on p. 10.
The paper contains no separate table of contents.
The finite computation here does not audit the authors' Lean development or identify every equality between products in the infinite group.

## Assessment history

### Decision appendix-supports

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:15 |
| status | proved |
| reason | Independent source transcription, a separate exhaustion of all support choices and the three coefficient contradictions cover the exact assertion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nonempty pair of sub-supports in the specified 32-by-28 rectangle over any field. |
| argument | [Proof](#argument) | Finite quotient equations, exhaustive support propagation and signed ratios. |
| review | [Whole finding](../audits/reviews/Yin_R_A0142_v1.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |

## Current assessment

[Selected decision](#decision-appendix-supports)
