---
author: Yin
---

# Common readable words preserve the central parity of independent six-vertex blocks

## Statement

Let \(X\) be an aspherical cone complex of the two connected immersed graphs \(A,B\) in a rose, \(F\) its rose group, \(G=\pi_1X\), \(N=\ker(F\to G)\), and \(\eta:G\to Q\) a finite quotient.
Use the [mixed central group and its homomorphism \(\rho:N\to P\)](Yin_C_A0066_v1.md#the-finite-tensor-calculation), with the rooted copy of \(A\) killed.
Write \(\Phi=[N,N]N^2\) for the kernel of the map to \(H_1(N;\mathbb F_2)\).

On the left graph fix two paths joining \(x\) to \(x'\) and \(y\) to \(y'\), respectively, with words \(p_x,p_y\) in \(\Phi\).
Let \(T_x,T_y\) be their central mixed values after basing them by left root paths to \(x,y\).
Assume the two starts have the same \(Q\)-color.
If **one and the same word** is also readable from \(x\) to \(x'\) and from \(y\) to \(y'\), then \(T_x=T_y\).
This holds even when the original group labels of \(x\) and \(y\) are different, and allows the alternative common reading to use arbitrary loops on the left graph.
No bound on the proof lengths, the number of right bases or the available side and translation indices is required.

In particular choose two [six-vertex commutator blocks](Yin_C_A0070_v1.md#repeated-paths-with-independent-mixed-signatures-in-the-even-bins) of different independent tensor types \(T_1,T_2\) in left color \(3\), with vertices numbered \(0,\dots,5\) in each.
In the graph of simultaneous readable steps on ordered pairs, the \(36\) marked pairs are split into four parity classes of nine.
No connected component meets two different classes.
Consequently a proposed cross-block equality propagated by any common word back into these two blocks can only connect another pair of the **same two parities**.
Even an arbitrary path through unmarked vertices between the two marked pairs obeys this constraint.
For \(k\ge2\) blocks of independent types, their \(6^k\) marked tuples lie in at least \(2^k\) different components of the simultaneous-step graph on \(k\) coordinates.
These assertions apply to the four-line law of C70 and individually to any safeguarded tuple with the specified paths.
There are also configurations of **three disjoint six-vertex blocks in the thirteen-position law itself** in which the two ends of the middle block are connected to the outer blocks by two paths reading the same word.
Each bridge changes every one of the thirteen coordinates and proves an actual original-group equality.
The two outer blocks have a common tensor type independent of the middle type.
All eighteen marks have the same original label; in this example the remote ends of the bridges belong to two different outer blocks.

There is also a way for common readings alone to force an inter-block equality.
Suppose that, on a torsion-free tuple, one word carries a mark of each block in a cyclic list of length \(l\) to a mark of the next, allowing a change of mark within each block before reading the word again.
Then all these blocks have the same original label.
If \(4\mid l\), the sum of the internal central changes must be zero, and if \(l\equiv2\bmod4\) the sum must have tensor rank at most one.
In particular a common word cannot exchange two blocks with both mark parities changed when the sum of the two block tensors has rank two.

## Two start labels in a common coarse color

The abelianization of \(P\) used here is its pair of first coordinates \(U\oplus V\), with the central subgroup \(U\otimes V\) of exponent two as kernel of that coordinate map.
Only the coordinate map and its central kernel are needed.
The composition of \(\rho\) with the coordinate map factors through
\[
 H_1(N;\mathbb F_2)=
 \bigoplus_{g\in G}(H_1(A;\mathbb F_2)_g\oplus H_1(B;\mathbb F_2)_g).
\]
The equality is the lifted-cone isomorphism using asphericity.
Conjugation by \(f\in F\) acts on this homology by translating the deck vertex by the image of \(f\) in \(G\).
Indeed the connecting map of the relative cone sequence is deck-equivariant, and changing base paths only gives inner conjugation in \(N\). [Translated cycle classes](Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials)
The first-coordinate map sums over each coarse index and drops the \(A\)-coordinate at the identity of \(Q\).
It follows that for \(f,h\in F\) of the same coarse color the two homomorphisms
\[
 n\longmapsto\rho(fnf^{-1}),\qquad n\longmapsto\rho(hnh^{-1})
\]
have identical first coordinates on all \(n\in N\).
Their pointwise quotient lies in the central elementary abelian subgroup and is a homomorphism because this quotient is central.
Therefore they agree on \(\Phi\), even for distinct actual deck vertices.
The image under either map of an element of \(\Phi\) is central, since the first-coordinate group has exponent two and is abelian.

Take left root words \(f,h\) to \(x,y\), with images \(g_x,g_y\) in \(G\).
Let \(w\) be the alternative common word in the statement.
It is in \(N\), because \(w\) and \(p_x\) join the same two vertices and the full graph is coned.
The element \(f w p_x^{-1} f^{-1}\) is a rooted \(A\)-loop and the same is true of \(h w p_y^{-1} h^{-1}\).
Their images under \(\rho\) are trivial.
In particular \(\rho(fwf^{-1})=T_x\) and \(\rho(hwh^{-1})=T_y\).
If \(g_x=g_y\), then \(fh^{-1}\in N\), so these last two values are conjugate by \(\rho(fh^{-1})\).
They are central and hence equal.

If \(g_x\ne g_y\), the condition \(p_x\in\Phi\) and the rooted-loop observation give \([w]\in H_1(A;\mathbb F_2)_{g_x^{-1}}\) in the **full** deck direct sum.
The other path likewise puts \([w]\) in \(H_1(A;\mathbb F_2)_{g_y^{-1}}\).
These are distinct summands, so \([w]=0\) and \(w\in\Phi\).
The same-coarse-color comparison of the two homomorphisms now gives \(T_x=T_y\).
Using the full deck indices at this step is essential because the prescribed starts have the same coarse index.

## What a cross-block bridge and its transports can decide

For two marks \(i,i'\) in a block of type \(T_1\), the intervening subpath reads a power of a commutator of elements of \(N\), so lies in \(\Phi\), including for a reverse subpath.
Its based tensor is \(((i-i')\bmod2)T_1\).
The analogous value for marks \(j,j'\) in the other block is \(((j-j')\bmod2)T_2\).
A simultaneous path between the ordered pairs \((i,j)\) and \((i',j')\) supplies a word \(w\) as in the statement.
Independence forces both parities of the changes to be zero.
Projection from a \(k\)-coordinate simultaneous path to any two coordinates proves the multi-block assertion.

More generally form a graph whose nodes are blocks and in each node include all the subpath witnesses between its marks with potentials \(iT\).
Propose one cross identification on each of a forest of block pairs, and allow its transports by common words with endpoints back in the **same respective blocks**.
For independent incident types, the parity result puts every such transported edge at the same pair of parity values as its initial edge.
There is no central inconsistency forced by these data, even if an arbitrary central value of exponent two is assigned to each original cross edge.
In fact the potentials \(b+iT\), with \(b\) one offset per block, realize every assignment by choosing one root offset in each tree and solving the offset difference equation successively along its edges.
Every allowed transport has the same value as its original edge under those potentials, as required by common-step invariance.
The sum of the edge values of every saturation of a fixed set of marks is then the sum of its vertex potentials.
This is a consistency statement for the indicated central data; a potential assignment by itself supplies no original-group equality.
A conflicting cycle would require an additional constraint, for instance a separately forced bridge closing a cycle of block offsets or information about the values of bridges that leave the indicated blocks.

## A common word cycling among blocks

Write \(x_i,y_i\) for marks in block \(i\), \(0\le i<l\), and assume that there is a readable path with the same word \(w\) from \(x_i\) to \(y_{i+1}\) for each \(i\) cyclically.
Let \(g_i\) be the original label of both marks in block \(i\).
Then \(g_i\pi(w)=g_{i+1}\), hence \(\pi(w)^l=1\).
Torsion-freeness implies \(w\in N\) and \(g_i=g_0\) for all \(i\).
Thus these are genuine cross-block equalities even without a proposed full matching.

For each marked vertex let \(f_x\) be a chosen left root word, and put \(n_i=\rho(f_{x_i}f_{x_0}^{-1})\), \(v=\rho(f_{x_0}w f_{x_0}^{-1})\).
Let \(c_i=\rho(f_{y_i}f_{x_i}^{-1})\) be the known internal change, central of exponent two.
Because the rooted \(A\)-loop comparing \(f_{x_i}w\) with \(f_{y_{i+1}}\) is killed, one has
\[
                     c_{i+1}n_{i+1}=n_i v .
\]
Going around the list, centrality and \(n_0=1\) give \(v^l=\prod_i c_i\).
No centrality of the single cross-block value \(v\) was assumed.
In the group \(P\) a triple \((a,b,c)\) has square \((0,0,a\otimes b)\) and fourth power one by the multiplication law.
This proves the rank tests, including for a reversal of two blocks.
For example, with the independent diagonal tensors of C70 an odd change in each of two exchanged blocks would give a sum of rank two.
The test requires actual common readings at all the indicated marks, or an argument that the hypothesized erasure forces such readings.
It gives no necessity that an arbitrary complete pairing create that cycle.

## Genuine bridges between disjoint six-vertex blocks

Use the [one-lamp cycles, neutral cycles and thirteen-position bridge](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges) in the law of [C65](Yin_C_A0065_v1.md#statement).
Take two of the neutral commutator words \(M_i=[s_iU_i s_i^{-1},V_i]\) with their independent rank-one tensors \(T_i\), for \(i=1,2\).
Take the unguarded commutator forms in this formula; choosing \(s_i\) off the inverse pairs of the end letters of \(U_i,V_i\) ensures cyclic reduction also between successive copies.
Let \(D\) be the word adding one to every visible lamp at coarse color \(3\).
Choose one neutral guard letter \(v\) off the inverse pairs of the first and last letters of \(M_1,M_2,D\), and put \(D'=vDv^{-1}\).
Its lamp change is the same as that of \(D\), and it is a product of conjugates of cone relations.
The following is a reduced word:
\[
                  M_2^{-5}(D')^{-1} M_1^5 D' M_2^5 .
\]
The two marked intervals of type \(T_2\) are traversed in opposite senses, which does not change a central value of exponent two.
On a simple open lift, the three commutator-power intervals have six different marked vertices apiece, with no shared marks between intervals.
The spaces traversed by \((D')^{-1}\) and \(D'\) give disjoint paths from the first and last marks of the middle block to a mark on each outer block, both read as \(D'\) in that direction.
The starts have the same fine state, and at the two destinations each of its thirteen coordinates has been increased by one.
Since every named word is trivial in \(G\), the three blocks and both bridges have the claimed actual equalities at their marked ends.
Every proof for either bridge has to use the thirteen positions, by the single-slot bound in C65.
One can use any prescribed internal matchings in these blocks as part of the conditional extension argument in [C70](Yin_C_A0070_v1.md#extending-witnessed-matchings-on-even-blocks).

For completeness, for any fixed \(0<\delta<1\) in this law add this single word to the open-path list of C72 before sampling.
Its length is at most \(CR+C'\), where \(R=\lceil a\log n/\log64\rceil\) is the cycle-search radius and the constants depend on the fixed lamp modulus.
There are still \(O(n^{a/4})\) words, the used-vertex budget is \(O(n^{1-a/2})\), and every specified reduced turn, including through the guards, has fresh-partner probability at least \(1/300\).
Choose \(a>0\) small enough for the increased \(C\), so the binomial lower comparison still has mean \(n^{1-a/2-a/4-Ca\log(300)/\log64-o(1)}>n^{1-\delta/2}\) per word.
The same girth-conditioning cost \(\exp(O(n^{3a/8}\log n))\) is absorbed by the initial cycle-search and later path estimates.
This gives at least \(\lfloor n^{1-\delta}\rfloor\) disjoint simple open lifts of the displayed word with probability tending to one conditional on girth, together with the C65 safeguards.
This construction starts in the thirteen-coordinate law throughout.
The three-block crossing is obtained on a subset of the color without assuming that the entire color erases.

## Assessment history

### Decision common-word-block-parities

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:03 |
| status | proved |
| reason | Independent review checked the two deck cases, the synchronized parity and rank bounds, and the actual three-block paths. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Constraints on common readings, cyclic exchanges, forest identifications and actual cross-block equalities in the thirteen-position law. |
| argument | [Proof](#two-start-labels-in-a-common-coarse-color) | Full deck homology, central comparisons, block offsets, cyclic powers and the simultaneous-path construction. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0111_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-common-word-block-parities)
