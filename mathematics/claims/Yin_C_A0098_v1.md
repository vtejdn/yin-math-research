---
author: Yin
---
# A three-term progression forced by three left labels

## Statement

Let \(g_1,g_2,g_3\) be distinct elements of a torsion-free group \(G\), and let \(B\subset G\) be finite and nonempty.
If every element of \(\{g_1,g_2,g_3\}B\) has at least two representations \(g_i b\), then for some \(i\ne j\), writing \(x=g_j^{-1}g_i\), there is \(b\in B\) with
\[
                            b,\quad xb,\quad x^2 b\ \in B .
\]
The three elements are distinct.
In particular a zero product over any field with exactly these three left labels forces this progression in the exact right support.
The same implication applies to the two supports before choosing coefficients.

## Argument

Suppose that none of the three unordered pairs of labels yields such a progression in either direction.
For each pair \(i,j\), the finite translation graph on \(B\) for \(x=g_j^{-1}g_i\) consists of isolated vertices and disjoint single edges.
Indeed \(x\) has infinite order, and three consecutive vertices in an \(x\)-orbit would be a forbidden progression.
Each intersection point of \(g_iB\) and \(g_jB\) corresponds bijectively to an oriented edge \(b\mapsto xb\) in this graph, so \(|g_iB\cap g_jB|\le |B|/2\).

At each output let \(d\in\{2,3\}\) count its representations.
Summing \(d\) gives \(3|B|\), and summing \(\binom d2\) gives the sum of the three pairwise intersection sizes.
Since \(\binom d2\ge d/2\), with strict inequality for \(d=3\), both bounds on this sum force equality.
Each output therefore has precisely two representations, and all three translation graphs are perfect matchings on \(B\).

For each \(b\in B\) orient the edge \(\{i,j\}\) of the label triangle from \(i\) to \(j\) if \(g_i b=g_j b'\) for its unique neighbor \(b'=g_j^{-1}g_i b\) in the matching for this pair.
Otherwise the reverse edge is present because \(b\) belongs to a matched pair, and both directions at \(b\) would require three consecutive vertices in the same orbit.
Each label \(i\) has exactly one outgoing edge, by uniqueness of the second representation of \(g_i b\).
Consequently the orientation at \(b\) is one of the two directed cycles on three vertices.
Along a matching edge the orientation of the associated label pair reverses, so the directed cycles at the endpoints are opposite.
Both cycle types therefore occur.

Let \(B_+\) be the vertices with cycle \(1\to2\to3\to1\), and \(B_-\) the other vertices.
Each perfect matching pairs the two types bijectively, in the same direction at all vertices of \(B_+\).
Thus, setting \(t_1=g_2^{-1}g_1,\ t_2=g_3^{-1}g_2,\ t_3=g_1^{-1}g_3\), we have
\[
                            t_1 B_+=t_2 B_+=t_3 B_+=B_- .
\]
Each \(t_j^{-1}t_i\) stabilizes the finite nonempty set \(B_+\).
Its action by left translation has a finite power fixing a point, so torsion-freeness forces \(t_j^{-1}t_i=1\).
Their common value \(t\) satisfies \(t^3=t_3t_2t_1=1\), hence \(t=1\), contradicting the distinctness of the labels.
This proves the progression assertion.
In a zero product a uniquely represented output has a nonzero coefficient because both factors have exact support and the coefficients lie in a field.
This proves the application to [A0002](../tasks/Yin_T_A0002_v1.md#contract).
The argument does not exclude configurations containing the forced progression.

## Assessment history

### Decision three-label-progression

| Field | Value |
| --- | --- |
| date | 2026-11-21T04:40 |
| status | proved |
| reason | Independent review verified the intersection count, orientation constraints and use of torsion-freeness. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The support progression forced by three left labels over any field. |
| argument | [Proof](#argument) | The matching and finite-stabilizer argument, including the repeated-product hypothesis and the application to zero products. |
| review | [Whole finding](../audits/reviews/Yin_R_A0134_v1.md#whole-finding) | Complete independent proof inspection with its stated limits. |

## Current assessment

[Selected decision](#decision-three-label-progression)
