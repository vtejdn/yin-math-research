---
author: Yin
---
# Three-term progressions in a right support with three left labels

At 2026-11-21T04:39 UTC a separate reviewer for Yin inspected the entire statement and argument of C_A0098_v1 and its application to the [A0002 contract](../../tasks/Yin_T_A0002_v1.md#contract).
The reviewer took no part in developing this proof and received no development dialogue, exploration notes, author explanation or prior verdict about it.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0098_v1.md#statement) | Three distinct left labels, finite nonempty right support, repeated representations in a torsion-free group, and the consequence for a zero product over a field. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0098_v1.md#argument) | The intersection count, equality in both bounds, the orientations and bijections between cycle types, the finite stabilizer, and the coefficient argument. |

## Whole finding

For a pair \(i\ne j\), put \(x=g_j^{-1}g_i\).
Since \(x\) has infinite order, left multiplication by \(x\) partitions \(G\) into doubly infinite paths.
If \(B\) contains no three consecutive vertices on these paths, the edges \(b\mapsto xb\) with both ends in \(B\) are pairwise disjoint.
Each such edge gives a different output \(g_i b=g_j(xb)\), and every point of \(g_iB\cap g_jB\) determines its edge uniquely.
Writing \(d(y)\) for the number of translates containing \(y\), the repeated-representation assumption gives \(d(y)=2\) or \(3\) at every output.
Consequently
\[
  \frac{3|B|}{2}
   =\frac12\sum_y d(y)
   \leq\sum_y\binom{d(y)}2
   =\sum_{i<j}|g_iB\cap g_jB|
   \leq\frac{3|B|}{2}.
\]
Equality on the left excludes every triple representation.
Equality on the right forces every pair to attain \(|B|/2\) disjoint edges, which cover \(B\).

At each \(b\) each pair matching gives exactly one of \(g_j^{-1}g_i b\in B\) and \(g_i^{-1}g_j b\in B\).
The second representation of \(g_i b\) gives the unique outgoing edge from label \(i\), so the three arrows form a directed cycle.
If \(b'=g_j^{-1}g_i b\) is its partner for this pair, the reverse translation takes \(b'\) back to \(b\).
The pair arrow therefore reverses, and the direction of a single arrow distinguishes the two possible cycles.
In particular both types occur since \(B\) is nonempty.
For the cyclically ordered pairs \(12,23,31\), the respective translations carry \(B_+\) onto \(B_-\) because each matching covers both types.

Hence \(s=t_j^{-1}t_i\) permutes \(B_+\).
For any \(b\in B_+\) its orbit is finite, so \(s^m b=b\) for some \(m>0\).
Cancellation gives \(s^m=1\), and torsion-freeness gives \(s=1\).
The three translations thus have a common value \(t\), and the order of multiplication is
\[
 t^3=(g_1^{-1}g_3)(g_3^{-1}g_2)(g_2^{-1}g_1)=1.
\]
It follows that \(t=1\), contradicting \(g_1\ne g_2\).
The resulting progression has three distinct terms because its step has infinite order.

For exact supports \(\{g_1,g_2,g_3\}\) and \(B\ne\varnothing\), a uniquely represented output has one nonzero product as its coefficient over any field.
A zero product therefore satisfies the combinatorial hypothesis in every characteristic.
The proof establishes a necessary condition on the supports and leaves open whether configurations containing such a progression admit a zero product.
