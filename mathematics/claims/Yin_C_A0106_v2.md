---
author: Yin
---
# Girth and index-six subgroups for the seven collinear triples

## Statement

Let \(\Gamma\) be the Gardam group with the two-generator and seven-triangle presentations identified in [C105v2](Yin_C_A0105_v2.md#identifying-the-seven-triangle-presentation).
Use the seven distinct positive generators \(a,b,c,d,e,f,g\).
The exceptional triples of the [outermost-coefficient criterion](Yin_C_A0106_v1.md#statement) are
\[
 \begin{array}{c|ccccccc}
 y&a&b&c&d&e&f&g\\ \hline
 P_y&bdg&bcf&afg&acd&ceg&abe&def .
 \end{array}                                                   \tag{1}
\]
A string in this display denotes a set, with the written order used when defining its two ratio generators.

Fix \(P=\{x,y,z\}\) from (1).
Define a simple bipartite graph \(\mathcal G_P\) with two copies of \(\Gamma\), called left and right.
For each \(v\in\Gamma\) and \(p\in P\), join the left vertex \(v\) to the right vertex \(pv\), marking that edge by \(p\).
Let
\[
                         H_P=\langle x^{-1}y,x^{-1}z\rangle.
                                                               \tag{2}
\]
The [finite verifier J_A0006](../computations/programs/Yin_J_A0006/readme.md) establishes the following facts, with the proof interfaces given below.

1. Each of the seven graphs \(\mathcal G_P\) has girth exactly \(24\).

2. If \(B\subset\Gamma\) is finite and nonempty and \(PB\) has no uniquely represented product, then
   \[
                               |B|\ge126.                    \tag{3}
   \]
   If, in addition, some product has three representations in \(P\times B\), then
   \[
                               |B|\ge189.                    \tag{4}
   \]
   There is no radius restriction on \(B\).
   These bounds also apply to the right support of a zero product over any field whose left support is exactly \(P\).

3. All seven ratio subgroups satisfy
   \[
                 [\Gamma:H_P]=6,\qquad
                 (H_P)_{\rm ab}\cong C_4\oplus C_{28}.         \tag{5}
   \]
   In particular every additive homomorphism \(H_P\to\mathbb R\) is zero.
   Every multiplicative complex character has image of exponent dividing \(28\), and there are exactly \(112\) such characters.
   A finite abelianization supplies no continuous height on these subgroups.

Combining (3) with v1 and the infinite-order ratio argument below gives an arbitrary-radius corollary:
for **every field** \(k\), every nonzero \(\alpha\in k[\{a,b,c,d,e,f,g\}]\), and every nonzero finite \(\beta\in k[\Gamma]\) with
\[
                         |\operatorname{supp}\beta|\le125,
\]
one has \(\alpha\beta\ne0\).
The two-label case uses the building realization specified below.
The exact girth, index and abelianization calculations use only the presentations and the proved word problem.

No zero product or non-unique-product rectangle attaining (3) or (4) is constructed.
The assertions do not prove finite-support regularity for the exceptional triples with unrestricted right-support size.

<a id="argument"></a>

## The finite girth certificate

The normal form of C105v2 supplies exact equality in \(\Gamma\).
A graph step from side \(0\) to side \(1\) prepends the positive color \(p\); a step in the opposite direction prepends \(p^{-1}\).
This convention matches left multiplication in the definition of \(\mathcal G_P\).
All three neighbors of each vertex are distinct, since \(a,\ldots,g\) represent distinct group elements.

At the left identity vertex the verifier enumerates every nonbacktracking colored path of length at most \(11\).
Nonbacktracking means that two successive colors differ.
Every new endpoint, including its side, is distinct from all earlier endpoints.
At depth \(j\), for \(1\le j\le11\), there are exactly \(3\cdot2^{j-1}\) endpoints.
Thus the checked rooted tree has
\[
                         1+3(2^{11}-1)=6142
\]
vertices.

Right multiplication by an element of \(\Gamma\), simultaneously on both sides, is a color-preserving graph automorphism.
It is transitive on left vertices.
If a cycle of length at most \(22\) existed, translate one of its left vertices to the identity.
The two halves of the cycle would give distinct nonbacktracking paths of length at most \(11\) to the same endpoint, contradicting the certificate.
The graph is bipartite, so this proves girth at least \(24\).

For the upper bound the following pairs of color paths have the same endpoint.
Each path starts at the left identity and has length \(12\).

| Triple | First path | Second path |
| --- | --- | --- |
| \(bdg\) | dbdbdbdgbgbg | bgdgdgdgdbgb |
| \(bcf\) | cbcbcbcfbfbf | bfcfcfcfcbfb |
| \(afg\) | fafafafgagag | agfgfgfgfaga |
| \(acd\) | cacacacdadad | adcdcdcdcada |
| \(ceg\) | ecececegcgcg | cgegegegecgc |
| \(abe\) | babababeaeae | aebebebebaea |
| \(def\) | edededefdfdf | dfefefefedfd |

The verifier follows the first path and then the reverse of the second.
It checks closure at the identity, cyclic nonbacktracking, and distinctness of all \(24\) vertices before the final return.
These are genuine simple \(24\)-cycles in the actual group graph.
The finite search that originally found them is not needed to reproduce the certificate.

## The support bound from two rooted trees

Suppose \(PB\) has no uniquely represented product.
Take the finite incidence subgraph with left vertices \(B\), right vertices \(PB\), and all its product edges.
Every left degree is exactly \(3\).
Every right degree is \(2\) or \(3\): absence of unique products gives the lower bound, and at most one preimage occurs for each of the three labels \(p\).
This is a simple subgraph of \(\mathcal G_P\), so it has no cycle shorter than \(24\).

Choose an edge with left endpoint \(v\) and right endpoint \(w\).
Grow a nonbacktracking tree of depth \(11\) from each endpoint, forbidding the chosen edge as the first step.
All vertices in these two trees are distinct.
A repetition within one tree would produce a cycle of length at most \(22\).
An intersection between the two trees, using the original edge, would produce a cycle of length at most \(11+11+1=23\).
Both contradict the girth bound.

The left-rooted tree contains at least
\[
                  1+2+4+8+16+32=63
\]
left vertices, at depths \(0,2,\ldots,10\).
The right-rooted tree contains at least the same \(63\) left vertices, at depths \(1,3,\ldots,11\).
At each subsequent left vertex there are two forward choices, and at each right vertex at least one.
Thus \(|B|\ge126\).

If \(w\) is a right vertex of degree \(3\), its tree has two first choices instead of one.
Its left-vertex count is then at least \(126\), while the left-rooted tree still has at least \(63\).
Choosing an incident edge proves \(|B|\ge189\).
This proves (3)–(4) by a finite graph argument and not by a probabilistic estimate.

For a zero product with all three left coefficients nonzero, each actual product fiber receives a sum of nonzero terms.
A singleton cannot sum to zero over any field.
Its incidence graph therefore satisfies the same degree conditions.
If all fibers have size two, \(3|B|\) is even, so \(|B|\) is even.
In particular an odd-sized right support for such a zero product would require a triple fiber and would satisfy (4).

## A short exact certificate for the index

For \(P=(x,y,z)\), write
\[
                       t=x^{-1}y,\qquad u=x^{-1}z.
\]
Uppercase \(T,U\) denote their inverses.
The native input in J_A0006 consists, for each \(P\), of a six-state table for right multiplication by \(a,b\), six representative words \(r_0,\ldots,r_5\), and twelve short words in \(t,u,T,U\).

First, the two table columns are permutations.
Both defining relators of \(\Gamma\) fix every state.
Thus the table is a genuine action of the presented group on six points.
The words \(t,u\), converted to \(a,b,A,B\) by C105v2's explicit substitutions, fix state zero.
The representatives send state zero to all six different states.
Consequently \(H_P\) is contained in the stabilizer of zero and
\[
                            [\Gamma:H_P]\ge6.                \tag{6}
\]

For each table transition \(i\xrightarrow{q}j\), where \(q=a\) or \(b\), the retained word \(h_{i,q}(t,u)\) is checked by exact normal form to satisfy
\[
                       r_i q r_j^{-1}=h_{i,q}(t,u).
                                                               \tag{7}
\]
Thus the union of the six right cosets \(H_P r_i\) is closed under right multiplication by \(a,b\).
It is also closed under their inverses: reverse (7) to obtain
\(r_jq^{-1}=h_{i,q}^{-1}r_i\), and use that each table column is a permutation.
The union contains the identity and hence all of \(\Gamma\).
Therefore \([\Gamma:H_P]\le6\).
Together with (6) this proves the exact index and identifies the table as the actual Schreier coset graph.

Only twelve normal-form identities are needed per triple.
The proof uses neither a bare coset-enumerator success message nor a finite permutation image as an upper bound on subgroup index.
The exploratory coset enumeration and the search for the words in (7) are replaced by these explicit retained certificates.

There are also short relations illustrating why the ratios cannot simply be treated as free generators:
\[
 \begin{array}{c|l}
 bdg,\ bcf,\ afg,\ def & ututUttUUTUTTuuT\\
 acd,\ ceg,\ abe & uututtUUtUTUTuTT .
 \end{array}                                                  \tag{8}
\]
For each indicated triple the word is freely reduced, has length \(16\), and its image in \(\Gamma\) has empty normal form.
The verifier checks these facts and the zero exponent sums in \(t,u\).
Balanced relations such as (8) alone would not prove existence of a character.
The full abelianization computation below gives the opposite conclusion.

## Integral abelianization of the ratio subgroups

Use the six-sheeted cover of the standard two-generator presentation complex determined by the verified coset action.
Its fundamental group at state zero is exactly \(H_P\), by the preceding index certificate.
No asphericity of this complex is needed to compute its first homology.

The Schreier graph has six vertices and twelve oriented positive edges: one \(a\)-edge and one \(b\)-edge at each vertex.
The verifier chooses a spanning tree with five edges.
The remaining seven edges are an integral basis for the graph's cycle group after collapsing the tree.
For every state, trace each of the two defining relator loops, recording \(+1\) or \(-1\) according to the orientation of each traversal.
Projection to the seven non-tree edges gives an integer matrix with twelve rows and seven columns.
These are exactly the cellular boundaries of all twelve lifted two-cells.
Consequently
\[
             (H_P)_{\rm ab}
               \cong \mathbb Z^7/
                    \langle\text{rows of this matrix}\rangle.
                                                               \tag{9}
\]

For every triple the integer Smith diagonal is
\[
                            1,1,1,1,1,4,28.                  \tag{10}
\]
J_A0006 generates each matrix directly from the table and the original relators, then performs integer Euclidean row and column operations.
Each operation is a swap, sign change, or addition of an integer multiple of another row or column.
It therefore preserves the lattice quotient up to isomorphism.
The code checks the final off-diagonal zeros and divisibility of successive positive entries.
The Euclidean loop terminates because a nonzero remainder reduces the pivot's absolute value; if the pivot fails to divide a remaining entry, adding that entry's row produces such a remainder.
This proves (5), including the torsion exponents, rather than just full rational rank or a modular rank test.

A homomorphism from \(C_4\oplus C_{28}\) to the additive torsion-free group \(\mathbb R\) is zero.
Its complex multiplicative characters are the independent choices of a fourth and a twenty-eighth root of unity.
This gives the character assertions in the statement.
In particular \(H_P\) is not a nontrivial free group and is not locally indicable.
No conclusion about the abelianization of every finite-index subgroup of \(H_P\) is inferred from (10) alone.

## Combining the exceptional and nonexceptional supports

For a support of at least four positive generators, or a three-element support not in (1), v1 proves a uniquely represented product with every nonempty finite right support.
The scalar coefficient statement there works over every field.

A one-label element is a nonzero scalar times a group element and is invertible.
For two distinct positive labels \(p,q\), it remains to know that \(p^{-1}q\) has infinite order.
Here one can use the triangle-building realization recalled in [L67](../ledger/Yin_L_A0067_v1.md#the-group-and-the-biradial-convention), with its precise CM94 source scope.
The group acts freely on vertices of the complete CAT(0) triangle building.
Each positive generator changes vertex type by one modulo three, so \(p^{-1}q\) preserves type.
A finite-order building isometry fixes a point: take the circumcenter of a finite orbit.
It then preserves the unique smallest simplex whose relative interior contains that point.
A type-preserving isometry fixes every vertex of this simplex, whose vertex types are distinct.
The free vertex action makes the isometry the identity.
Since \(p,q\) are distinct by the exact normal form, \(p^{-1}q\ne1\), and it must have infinite order.

Now a two-label coefficient factors as
\[
        c_p p+c_q q=c_p p(1+\lambda p^{-1}q),
             \qquad \lambda=c_q/c_p\ne0.
\]
Left multiplication by the nonzero Laurent polynomial \(1+\lambda t\), with \(t=p^{-1}q\) of infinite order, is injective on \(k[\Gamma]\).
Indeed decompose a finite input into right cosets \(\langle t\rangle v\).
Each component is a Laurent polynomial module over the domain \(k[t^{\pm1}]\), and different components remain separate.
This proves the two-label case.
The same conclusion could instead use the torsion-free assertion for this group on [Gardam's slide 12](../literature/pdf/Gar21c.pdf#page=12); the argument above states the needed geometric implication explicitly.

The only remaining left supports are the seven triples (1).
For them (3) excludes every right support of size at most \(125\).
This proves the corollary without a restriction on the right word radius.
The building input is used only for the two-label step, not in the girth or subgroup calculations.

## What the finite-index reduction does and does not give

After multiplying the left factor by \(x^{-1}\), a coefficient supported on \(P=(x,y,z)\) becomes
\[
                             c_x+c_y t+c_z u\in k[H_P].
\]
Left multiplication by this element preserves each right coset \(H_P v\).
Thus a finite annihilator in \(k[\Gamma]\) decomposes into independently annihilated components on at most six such cosets.
A nonzero component gives an annihilator inside \(k[H_P]\) after right translation.
This reduction retains the unrestricted right-support problem; it does not place \(H_P\) in a class with a known domain theorem.

The finite character group in (5) also does not force arbitrary coefficient phases to be characters of \(H_P\).
Partial cancellation equations on a finite support need not impose every relation of the whole subgroup.

There is a further source-dependent limitation on a proposed faithful linear representation.
Gardam's slide 12 states that \(\Gamma\) is not linear over \(\mathbb C\).
If a finite-index subgroup \(H_P\) had a faithful finite-dimensional complex representation, inducing it to \(\Gamma\) would produce a faithful representation of dimension six times as large.
An element moving the base coset is detected by the coset permutation; an element fixing that coset lies in \(H_P\) and is detected on its corresponding block.
Thus that stated source property excludes the proposed linear route for \(H_P\) as well.
This paragraph uses the source's nonlinearity assertion; it is not a conclusion of the finite tables.

The present computation resolves the girth, subgroup index and subgroup abelianization questions.
It supplies necessary support bounds for the exceptional three-label coefficients and an arbitrary-radius exclusion up to right-support size \(125\).
It leaves the larger exceptional right supports, and the general complex zero-divisor problem, open.

## Assessment history

### Decision collinear-triples

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:42 |
| status | proved |
| reason | Independent recomputation of the graph endpoints, Schreier data and integral minors verifies the finite certificates and their support consequences. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact girth, subgroup index and abelianization for all seven triples, and all-fields support bounds at arbitrary radius. |
| argument | [Proof](#argument) | The rooted paths, semiregular tree count, subgroup and integral homology certificates, and reduction of the other left supports. |
| review | [Whole finding](../audits/reviews/Yin_R_A0143_v2.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Outermost coefficients](Yin_C_A0106_v1.md#decision-outer-layer) | Arbitrary finite right supports for the positive left supports covered by the terminal criterion. |
| dependency | [Exact word problem](Yin_C_A0105_v2.md#decision-exact-balls) | Presentation and normal form for the girth and subgroup certificates. |

## Current assessment

[Selected decision](#decision-collinear-triples)
