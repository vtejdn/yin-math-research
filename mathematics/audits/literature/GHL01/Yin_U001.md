---
author: Yin
---

# GHL01: the definition of uniquely restricted matching

<a id="ghl01-u001"></a>
## Source and inspection scope

The inspected source is the [first paragraph of the institutional abstract](readme.md#institutional-abstract) for Golumbic, Hirst and Lewenstein's *Uniquely restricted matchings*.
This is a direct check of the paper's reproduced abstract, not a full-text reading or proof review.

<a id="uniquely-restricted-matching"></a>
## Complete definition and application boundary

Let \(\Gamma\) be a finite graph and let \(M\) be a matching, meaning a set of edges with pairwise disjoint endpoints.
Let \(V(M)\) be the vertices incident to edges of \(M\).
Then \(M\) is uniquely restricted if the induced graph \(\Gamma[V(M)]\) has exactly one perfect matching, and that matching is \(M\).
A perfect matching covers every vertex of the induced graph exactly once.
This is the abstract's full defining condition; the local application restricts it to bipartite graphs.

The [definition and determinant argument in L_A0031](../../../ledger/Yin_L_A0031_v1.md#definition-uniquely-restricted-matching) use this terminology and directly prove the rank lower bound needed there.
No algorithmic or complexity assertion from the paper, and no uninspected full-paper rank theorem, is adopted by this source unit.
