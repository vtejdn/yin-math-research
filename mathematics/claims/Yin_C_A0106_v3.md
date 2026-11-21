---
author: Yin
---
# Endpoint capacities for the seven collinear triples

## Statement

Use the Gardam group, positive generators and seven exceptional triples of [C106v2](Yin_C_A0106_v2.md#statement):
\[
               P\in\{bdg,bcf,afg,acd,ceg,abe,def\}.
\]
The graph has left vertices \(v\in\Gamma\), right vertices \(w\in\Gamma\), and a color-\(p\) edge from \(v\) to \(pv\), for \(p\in P\).
Its girth is \(24\), as proved in v2.
The index-six subgroup and abelianization conclusions of v2 are unchanged.

Let \(B\subset\Gamma\) be finite and nonempty.
If \(PB\) has no uniquely represented product, the fixed-depth endpoint capacities below imply
\[
                              |B|\ge361.                     \tag{1}
\]
If there is also a product with three representations, they imply
\[
                              |B|\ge655.                     \tag{2}
\]
Under the same absence of uniquely represented products, if \(361\le |B|\le654\), every fiber must have size two, forcing \(|B|\) to be even.
Thus size \(361\) is excluded as well, and the unconditional necessary bound is
\[
                              |B|\ge362.                     \tag{3}
\]
No restriction is imposed on the word lengths of elements of \(B\).

Consequently, for every field \(k\), every nonzero
\(\alpha\in k[\{a,b,c,d,e,f,g\}]\), and every nonzero finite \(\beta\in k[\Gamma]\) with
\[
                         |\operatorname{supp}\beta|\le361,
                                                               \tag{4}
\]
one has \(\alpha\beta\ne0\).
In particular this includes the size-at-most-\(360\) range directly given by (1); the extra value follows from parity.
The nonexceptional and two-label steps are reused from v2, including its explicitly stated geometric input for infinite order of two-label ratios.
The new endpoint calculation itself uses only the exact group word problem.

The [retained J_A0007 verifier](../computations/programs/Yin_J_A0007/readme.md) computes precisely the following two finite path families, for each of the seven triples.
There is no extrapolation to greater depths.

<a id="argument"></a>

## The exact ambient endpoint histograms

A path is nonbacktracking if consecutive edge colors differ.
Endpoints are actual group elements identified by the complete normal form of C105v2.
Multiplicities count different paths, including paths of different allowed lengths.

At a left root, let \(m_L(v)\) count all nonbacktracking paths ending at the left vertex \(v\), with even length in \(\{0,2,\ldots,16\}\).
The length-zero path is included.
At a right root, let \(m_R(v)\) count all nonbacktracking paths ending at the left vertex \(v\), with odd length in \(\{1,3,\ldots,17\}\).
In both cases a root may be moved to the identity on its side by right multiplication in \(\Gamma\), preserving colors and paths.

For all seven triples the complete histograms are identical:

| Root and allowed lengths | Endpoints of multiplicity 1 | Of multiplicity 2 | Of multiplicity 3 | Total distinct endpoints | Total paths |
| --- | ---: | ---: | ---: | ---: | ---: |
| Left, even lengths at most 16 | 126,397 | 2,238 | 66 | 128,701 | 131,071 |
| Right, odd lengths at most 17 | 250,257 | 5,577 | 244 | 256,078 | 262,143 |

No endpoint has multiplicity greater than three in these families.
Vertices outside the displayed endpoint sets have multiplicity zero.
The weighted sums agree with the independent path counts
\[
 \begin{split}
 131071
    &=1+\sum_{j=1}^{8}3\cdot2^{2j-1}=2\cdot4^8-1,\\
 262143
    &=\sum_{j=0}^{8}3\cdot2^{2j}=4^9-1.
 \end{split}                                                   \tag{5}
\]
The program checks the path count at every intermediate pair of steps as well as these final totals.

The computation aggregates paths by their exact endpoint and final color.
From a left endpoint \(v\), two consecutive colors \(i,k\) produce
\[
                v\longmapsto p_i v
                   \longmapsto p_k^{-1}p_i v.
\]
The restrictions \(i\ne\) the preceding color and \(k\ne i\) are exactly the nonbacktracking conditions.
Each state retains its path count, so aggregation loses no multiplicity.
Left-root enumeration starts with the empty path.
Right-root enumeration starts with the three one-edge paths to \(p^{-1}\), after which the same two-step rule applies.
There are exactly eight pair steps in either calculation.

This gives a finite deterministic construction of both histograms.
The normal-form cache is capped at 50,000 entries and cleared between root cases.
The maximum depths are fixed in the program.
The calculation does not enumerate possible right supports \(B\) or assume that they lie in a word ball.

## Paths forced inside a finite rectangle

Assume \(PB\) has no unique product.
Its finite incidence subgraph has left vertex set \(B\), right vertex set \(PB\), left degrees exactly three and right degrees two or three.
Paths entirely inside this subgraph are among the ambient paths with the same root and have their left endpoints in \(B\).

Choose a left root in \(B\).
There are at least three nonbacktracking paths of length two.
After each subsequent pair of steps there are at least two continuations: a reached left vertex has two choices after excluding the incoming edge, and a reached right vertex has at least one.
Therefore the number of selected even paths of length at most sixteen, including the empty path, is at least
\[
                    M_L=1+3\sum_{j=0}^{7}2^j=766.             \tag{6}
\]
This counts paths, so it remains valid when their endpoints coincide.

If a right vertex has degree three in the finite subgraph, choose it as root.
There are three first steps.
The same branching count shows that the number of selected odd paths of length at most seventeen is at least
\[
                    M_R=3\sum_{j=0}^{8}2^j=1533.              \tag{7}
\]
The degree-three assumption here is exactly the triple-fiber hypothesis in (2).

For a general endpoint multiset, one can upper-bound the paths supported on \(k\) vertices by summing its \(k\) largest multiplicities.
The present bounds also account for low-multiplicity vertices that \(B\) must contain.
This extra restriction is essential to the stated values \(361\) and \(655\).

## Why the short endpoints have multiplicity one

We use a simple consequence of girth, with path cancellation made explicit.
In a graph of girth at least \(24\), a nonbacktracking path of length less than \(24\) cannot repeat a vertex: a shortest repeated-vertex segment would give a shorter simple cycle.
If two distinct such paths have the same initial and terminal vertices, remove their common initial segment and their common terminal segment where applicable.
Their remaining union contains a cycle of length at most the sum of the two original lengths.
Equivalently, free cancellation in one path followed by the reverse of the other cannot remove the entire closed walk unless the two reduced edge paths were identical.
This argument allows arbitrary shared prefixes and suffixes; it does not require the paths to be internally disjoint beforehand.

For the left-root family, every selected even path of length at most six has a distinct endpoint.
There are at least
\[
                          q_L=1+3+6+12=22                   \tag{8}
\]
such endpoints in \(B\).
An additional ambient path of allowed even length at most sixteen to one of these endpoints would give a cycle of length at most \(6+16=22\), impossible.
Thus all these endpoints have \(m_L=1\).

For the degree-three right-root family, the selected odd paths of length at most five give at least
\[
                          q_R=3+6+12=21                     \tag{9}
\]
distinct endpoints in \(B\).
An additional ambient odd path of length at most seventeen to one of them would give a cycle of length at most \(5+17=22\).
Thus all have \(m_R=1\).

The verifier also checks these multiplicity-one assertions directly for the larger ambient short endpoint sets.
There are 127 ambient endpoints of even paths of length at most six from a left root, and 63 ambient endpoints of odd paths of length at most five from a right root.
Every one retains multiplicity one in its respective final depth-sixteen or depth-seventeen family.
These ambient counts are distinct from the lower bounds 22 and 21 forced inside the finite rectangle.

## Capacity inequalities and parity

For either ambient multiplicity function \(m\), all values are \(0,1,2,3\).
If there are at most \(N_3\) ambient endpoints of multiplicity three and \(B\) contains at least \(q\) endpoints of multiplicity one, then
\[
 \begin{split}
 \sum_{v\in B}m(v)
   &=2|B|+|\{v\in B:m(v)=3\}|-|\{v\in B:m(v)=1\}|\\
   &\hspace{18mm}-2|\{v\in B:m(v)=0\}|\\
   &\le2|B|+N_3-q.                                          \tag{10}
 \end{split}
\]
The zero-multiplicity term explicitly permits elements of \(B\) outside the computed endpoint set.
This is why (10) is an arbitrary-radius bound.

The paths counted in (6) all occur in the ambient left-root family.
Its histogram has \(N_3=66\), and (8) gives \(q=22\).
Hence
\[
                    766\le2|B|+66-22=2|B|+44,
\]
which proves \(|B|\ge361\).
Under the triple-fiber hypothesis, (7), (9) and the right-root histogram give
\[
                   1533\le2|B|+244-21=2|B|+223,
\]
which proves \(|B|\ge655\).

If \(361\le|B|\le654\), the latter inequality forbids every triple fiber.
Since singleton fibers were already excluded, all fibers then have size two.
Counting the edges of the incidence graph gives
\[
                              3|B|=2|PB|.
\]
Therefore \(|B|\) is even, excluding \(361\) and proving (3).
This parity step is independent of the coefficient characteristic.

For a group-ring zero product with left support exactly one of the exceptional triples, nonzero coefficients prohibit singleton fibers over any field.
Thus all these necessary support bounds apply.
For left support of at least four positive labels or a nonexceptional triple, v1 already excludes every finite annihilator.
One- and two-label supports are handled in [v2's combination argument](Yin_C_A0106_v2.md#combining-the-exceptional-and-nonexceptional-supports).
These unchanged inputs and (3) prove the full positive-generator corollary (4).

The finite histograms establish the stated numerical exclusions.
They do not imply that a limit of these capacities diverges, that a greater depth always improves the bound, or that arbitrary-size right annihilators are excluded.
No support attaining either bound is supplied.

## Assessment history

### Decision walk-multiplicities

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:55 |
| status | proved |
| reason | A fresh independent enumeration and complete proof review verify both rooted path counts, the forced endpoints and the parity and coefficient conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | For each exceptional triple, absence of unique products requires at least 362 right labels and at least 655 when there is a triple fiber, yielding all-fields nonvanishing up to 361 for every positive left support. |
| argument | [Proof](#argument) | Exact ambient endpoint distributions, minimum branching in a finite rectangle, the girth estimate for short endpoints and pair-fiber parity. |
| review | [Whole finding](../audits/reviews/Yin_R_A0143_v3.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Triple graphs and other supports](Yin_C_A0106_v2.md#decision-collinear-triples) | Girth 24 and the one- and two-generator finite-support input. |
| dependency | [Outer-layer criterion](Yin_C_A0106_v1.md#decision-outer-layer) | The larger and nonexceptional positive supports against arbitrary finite inputs. |
| dependency | [Group normal forms](Yin_C_A0105_v2.md#decision-exact-balls) | Faithful word equality and the triangle presentation for the endpoint enumeration. |

## Current assessment

[Selected decision](#decision-walk-multiplicities)
