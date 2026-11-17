---
author: Yin
---

# Erasure forces positive complex rank for short sparse relations

## Statement

Fix either side and a forward color \(c\in\{3,5,6\}\) of a connected four-line tuple with the [original coarse types and populations](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).
Suppose the whole color disappears after collecting equal labels modulo two in its actual cone group \(G\).
Choose \(s=62\) of the \(8252\) neutral ordinary inverse pairs uniformly without replacement.
Retain their formal marking, even if some of their values in \(G\) coincide, and let \(K\le G\) be the subgroup that they generate.
Use one positive orientation for each inverse pair in the marked Cayley multigraph of \(K\).
Put
\[
                     H=2\left\lceil\frac{\log n}{\log(65/64)}\right\rceil+4 .
\]
Let \(P_H\) project onto the closed span in \(\ell^2(K)^s\) of all translates of the complex oriented cycle chains of cyclically reduced null words of length at most \(H\).
Let \(P_\infty\) project onto the closure of all finitely supported complex cycle chains.
On the same alphabet with probability greater than \(1/4000\), both
\[
          \operatorname{Tr}_{K}(P_H)\ge\tfrac1{128},
            \qquad \operatorname{Tr}_{K}(P_\infty)\ge\tfrac1{64}       \tag{1}
\]
hold, with the unnormalized trace over the \(s\) edge coordinates.
The first quantity is the regular rank of a finite matrix of integer group-ring coefficients formed from all those short relations.
If \(K\) is infinite, the second bound implies \(\beta_1^{(2)}(K)\le 61-1/64\).
The bounds are conditional on the given tuple, and the only probability is the draw of the alphabet.
They require neither asphericity nor freeness of a subalphabet nor integrality of an unknown trace.

In particular a color cannot erase if the proportion of alphabets meeting the first bound in (1) is at most \(1/4000\).
The same exclusion follows from such an upper bound on the proportion meeting the second, or on the proportion meeting both.
These are criteria on the actual relation spaces; the existence of a short relator alone gives no such numerical estimate on the proportion.

## Argument

Let \(v>0\) be the number of true labels with nonempty odd ordinary-stub set in the specified color.
Use [C88's finite-alphabet surplus estimate](Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets) on the fixed erased color.
With probability greater than \(1/4000\), the retained odd-edge subgraph \(B\) in the marked Cayley graph of \(G\) has \(e\) edges and \(v_0\le v\) nonisolated vertices with
\[
                             2e-2v_0\ge v/32 .                        \tag{2}
\]
Fix this alphabet for the rest of the proof.
All edges of \(B\) run along the marked generators of \(K\), with possibly several components in distinct left cosets of \(K\).
Left translation back to \(K\) preserves the marked edge coordinates on each coset separately.

Throughout a deletion procedure count only the nonisolated vertices of the remaining graph.
As long as its surplus is at least \(v/64\), its average degree is at least \(2+1/64\).
It has a simple cycle of length at most \(H\).
Indeed loops and parallel edges immediately give lengths one and two.
In the simple case prune leaves to obtain a nonempty core of at least the same average degree and minimum degree two.
For a uniform directed initial edge, continue by uniform nonbacktracking steps.
Uniform directed-edge measure is stationary, and the mean conditional entropy of one step is at least \(\log(\bar d-1)\) by convexity of \(d\log(d-1)\) on \([2,\infty)\), where \(\bar d\) is the core's average degree.
If the girth is greater than \(2j+2\), the continuations of length \(j\) from a fixed initial edge have distinct endpoints, giving conditional entropy at most \(\log n\).
Taking \(j=\lceil\log n/\log(65/64)\rceil+1\) contradicts that bound. [Nonbacktracking count](Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets)

Record the cycle and delete just one of its edges from the graph before pruning, choosing that edge as its pivot.
Any isolated vertices may now be omitted.
The surplus decreases by at most two per deletion.
Starting from (2), at least \(\lceil v/128\rceil\) such steps are available before the surplus can be less than \(v/64\).
Orient each recorded cycle and give each traversed edge coefficient \(+1\) or \(-1\) according to its chosen positive orientation.
The resulting chains are independent over \(\mathbb C\): in any nonzero linear combination, the pivot of its earliest cycle has a nonzero coefficient, since later cycles avoid that edge.
Each cycle reads a nonempty cyclically reduced null word in \(G\) and in \(K\), by closure and the uniqueness of the outgoing edge of each signed marked type.
The procedure allows different cycles to share other edges and allows their unbased words to agree.

## Compression to the finite edge set

For either projection \(P\), extend its regular representation to \(G\) by using the corresponding copy of \(P\) on every left coset of \(K\).
The method of compressing an equivariant projection to a finite Cayley edge set and the identification of reduced first homology with square-summable cycles modulo the closed finite-cycle space are classical. [Lyons–Pichot–Vassout, proof of Theorem 2.2, pp. 600–601](../literature/pdf/LPV08.pdf#page=6)
Because the cycle space is invariant under left translation in \(K\), the diagonal entry at any edge of type \(t\) in any coset is the same number \(p_t\in[0,1]\).
Their sum over the \(s\) positive types is \(\operatorname{Tr}_K(P)\).
Compress this operator to the finite complex edge space of \(B\), and let \(e_t\) be the number of its positively oriented edges of type \(t\).
Then its ordinary trace is \(\sum_t e_t p_t\).
There is at most one outgoing positive edge of any specified type from each vertex, and a loop likewise uses just one positive coordinate.
Thus \(e_t\le v_0\) and the compression trace is at most \(v_0\operatorname{Tr}_K(P)\).
For any \(b\) independent cycles supported in \(B\) which the extended \(P\) fixes, the compression acts as the identity on their \(b\)-dimensional span.
It is a positive contraction, so its trace is at least \(b\).
This comparison takes place before identifying the different cosets with one another; the translated cycles need not remain linearly independent inside a single copy of \(\ell^2(K)^s\).

For \(P=P_H\), take the short pivot cycles and use \(v_0\le v\) to obtain the first bound of (1).
For \(P=P_\infty\), the entire cycle space of \(B\) has dimension \(e-v_0+\#\pi_0(B)\) with isolated vertices omitted.
This is at least \(v/64\) by (2), giving the second bound.
Both use the same alphabet and the same original edge set.

For the finite matrix interpretation, enumerate all signed cyclically reduced words of length at most \(H\) which close at the identity in the marked group.
For each, take the oriented chain of its path from the identity.
It is a column of \(s\) finite integer coefficient arrays on \(K\).
The operator sending a finitely supported function in that input coordinate to the corresponding sum of left translates of the chain is a finite right-convolution matrix.
Its closed range over all columns is exactly the range of \(P_H\).
Inverting group indices converts the same matrix convention to ordinary left convolution and preserves the unnormalized trace.
The cutoff is finite, even if the word problem or the regular rank is not supplied algorithmically.

For infinite \(K\), the edge boundary has dense range in \(\ell^2(K)\), because its adjoint kills precisely the constant functions on the connected Cayley graph.
Hence its Hilbert kernel has \(K\)-dimension \(s-1=61\).
The closed finite-cycle space is the closure of the cellular two-boundaries in the Cayley complex obtained by attaching all finite relators: every such boundary is a finite cycle, and every finite cycle is a linear combination of closed paths.
Equivalently one takes the closed span of the boundary images from finite lists of relators.
Adding higher cells to make the universal cover contractible does not change this first homology.
The reduced first \(\ell^2\)-Betti number of the group is consequently \(61-\operatorname{Tr}_K(P_\infty)\), using the preceding Cayley-cycle identification for finitely generated groups and the cellular dimension convention. [Lück, finite-type cellular definitions](../literature/pdf/Luc02--book-manuscript.pdf#page=46)
This gives the stated deficiency without assuming that \(K\) is finitely presented.

## What the independent cycles force in cone fillings

There is a separate binary count for any chosen fillings of \(b\) independent sparse cycle chains.
Use the finitely many translated cone copies that occur in the chosen fillings, and write \(\Gamma_C\) for the source graph of copy \(C\).
The fillings express the cycles as sums of pushed-forward graph cycles, by summing their lifted graph-loop boundaries modulo two.
The resulting preimages in \(\bigoplus_C Z_1(\Gamma_C;\mathbb F_2)\) are independent because their images are.
Restrict their span to source edges outside the sparse alphabet, and let \(m_e\) count the distinct such source edges mapping to each off-alphabet Cayley edge \(e\), counting source copies separately.
The kernel of restriction lies in the sum of the cycle spaces of the sparse-alphabet subgraphs \((\Gamma_C)_S\).
At edge \(e\) the restricted coefficients must sum to zero, a space of dimension \((m_e-1)_+\).
Therefore
\[
                 b\le \sum_C \beta_1((\Gamma_C)_S;\mathbb F_2)
                              +\sum_{e\text{ outside }S}(m_e-1)_+ .
\]
The excess over an edge includes both distinct edges of one source copy and contacts between different copies.
For example, take two polygon relators equating a letter \(c\) to \(a_1\cdots a_m\) and to \(b_1\cdots b_m\), with \(m\ge2\) and all the displayed letters distinct, and add a free generator \(d\).
Eliminating \(c,b_m\) gives a free group.
The path on the \(a_i\) followed by the reverse path on the \(b_i\) is a simple sparse cycle when only \(c\) is omitted, since the nonempty proper prefixes are all distinct in the resulting free basis.
Its translates along \(d^j\) give arbitrarily many disjoint cycles.
Each fills with two polygons meeting in one \(c\)-edge, while each polygon is embedded and uses each of its unoriented labels at most once, so distinct translates of the same polygon share no edge.
This example concerns the inference from the cycle count alone.
The four-line type restrictions impose additional folds but the inequalities above do not put a same-copy fold in any prescribed filling, or force a common word for two pairs.

## Assessment history

### Decision short-relation-rank

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:42 |
| status | proved |
| reason | Independent review verifies the two subgroup trace bounds, the finite word cutoff and the limits on what a cone filling must do. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Regular rank forced by erasure in a positive fraction of short-relation alphabets, and the corresponding first Betti deficiency for an infinite subgroup. |
| argument | [Proof](#argument) | Independent oriented cycles at finite length, finite compression, the boundary matrix and the off-alphabet contact estimate. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0127_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-short-relation-rank)
