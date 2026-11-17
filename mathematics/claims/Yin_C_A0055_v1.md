---
author: Yin
---

# A homology constraint on simultaneous copies of opposite-side loops

## Statement

Let \(A,B\) be two finite connected rooted graphs immersed in the same rose \(R\), and cone both graphs to that rose to form \(X\).
Let \(G=\pi_1(X)\), and write \(g_x,h_y\) for the forward group labels read from the respective roots.
Let \(\eta:G\to Q\) be any known group homomorphism, including the trivial one.
All homology groups in the argument have coefficients in \(\mathbb F_2\).

For any path \(P:x\to x'\) in \(A\) that reads the word of a closed path \(C\) in \(B\) based at \(y\), place an undirected edge between \(x\) and \(x'\) in an auxiliary multigraph on the vertices of \(A\).
Such a correspondence will be called a copy.
The copy gives \(g_x=g_{x'}\) in the original group, since coning \(B\) kills \(C\).
Give the auxiliary edge the vector \([C]\) in the indicated summand of
\[
    V_Q=\bigoplus_{q\in Q}H_1(B),\qquad q=\eta(g_xh_y^{-1}).
\]
Here \([C]\) is the parity vector of the actual **edges of \(B\)** traversed by \(C\).
Reversing both paths gives the same vector.
The data may include multiple witnesses between the same vertices.
One may propagate an edge to every pair obtained from its endpoints by a sequence of common signed steps in \(A\), retaining its vector.

If \(X\) is aspherical, the following assertions hold for any such family of copies and propagations.

1. Their vectors sum to zero on every cycle of the auxiliary multigraph.
   Equivalently the edge assignment is the sum of endpoint values of a \(V_Q\)-valued function on vertices.
2. Any two matchings of the same vertex set, including two perfect matchings of a color proposed for erasure over \(\mathbb F_2\), have the same total vector if both saturate exactly that set.
   The conclusion also compares different witnesses for the very same paired vertices.
3. The comparisons are finite graph calculations for the supplied paths and quotient colors when equality of the finitely many indices in \(Q\) is supplied or decidable, as for \(Q=C_7\).
   They can refute a proposed system of copied relations in an aspherical matching without solving the word problem.

The same assertions hold when an edge equality has a supplied proof by several conjugates of graph relations, using the sum of its opposite-side contributions as specified below.
For a true equality in an aspherical cone the resulting vector is independent of the proof.

The graded test can reject a system which passes the test with \(Q\) trivial, has no off-diagonal or cross-side synchronous cycle, and passes the cycle-injection tests for the two originally rooted lifts alone.
The high-girth example below has two complete pairings of its left color 3 and a torsion-free group, but its specified cone complex is not aspherical.

## From cycles in the lifted rose to vertex potentials

Let \(\widetilde R\) be the preimage of \(R\) in the universal cover of \(X\).
This is the Cayley graph with vertices \(G\) and directed edges given by right multiplication by the signed letters.
Fix the lifts \(i_A,i_B\) of the graph maps that send their respective roots to the identity.
Left multiplication indexes the other lifts of each cone.
The connecting map for the universal-cover pair sends
\[
    \bigoplus_{u\in G}\bigl(H_1(A)_u\oplus H_1(B)_u\bigr)
       \longrightarrow H_1(\widetilde R)
\]
by the edge-chain maps of those lifts.
The domain is the relative degree-two homology since the open cone cells split by copy and each cone has relative homology \(H_1\) of its base in degree two.
Asphericity gives \(H_2(\widetilde X)=0\), so this connecting map is injective. [Relative cone calculation](../ledger/Yin_L_A0052_v1.md#a-homological-rejection-test-under-the-source-safeguards)

For a copy as above, \(i_A(P)\) is a cycle chain in \(\widetilde R\) and equals the image of \([C]\) in the single \(B\)-summand indexed by \(g_xh_y^{-1}\).
Indeed the two word paths start at the same Cayley vertex after this translation and follow the same successive edges.
For a common step \(t\) at \(x,x'\), transport the witness to their neighbors using the \(A\)-path that first goes back along \(t^{-1}\), traverses \(P\), and goes forward along \(t\).
The added edges in the Cayley graph cancel since \(g_x=g_{x'}\), so the closed Cayley edge chain is unchanged.
This works through arbitrarily many steps without requiring that the additional edges be readable in \(B\).

Choose any subset of auxiliary edges having even degree at every \(A\)-vertex, retaining distinct copies of parallel edges.
The sum of their witness paths is then a cycle chain in the fixed copy of \(A\), since their vertex boundaries cancel.
Its image in \(\widetilde R\) equals the sum of their original opposite-side cycle vectors in the corresponding translated \(B\)-summands, by the preceding paragraph.
Injectivity and the fact that these are different direct summands force the sum to vanish in each \(B\)-summand.
Adding its entries over all deck indices with the same image under \(\eta\) gives exactly zero in \(V_Q\).
All these sums have finite support.

For each auxiliary component, fix a zero potential at one vertex and integrate the edge vectors along a spanning tree.
The zero sum on cycles ensures that the remaining edges also have the claimed endpoint sums.
Conversely such potentials force zero on every cycle.
Therefore summing the edge vectors over any matching counts the potentials at its saturated vertices once each.
Alternatively, the symmetric difference of two matchings on the same saturated set has everywhere even degree.
This proves the assertions and gives a test using the finite edge rows of \(B\) in the finitely many quotient positions that occur.
For a fixed collection of possible witnesses, one can check fundamental cycles of the propagated auxiliary multigraph, including a cycle made from two parallel witnesses.

## Certificates using several graph relations

More generally, suppose the word \(W\) of an \(A\)-path \(x\to x'\) is supplied with a free-group identity
\[
                       W=\prod_j u_j R_j^{\pm1}u_j^{-1},
\]
where \(R_j\) is the word of a specified based closed walk on either side.
This is ordinary evidence from the original cone presentation and implies \(g_x=g_{x'}\).
For a walk \(R_j\) on \(B\) based at \(y_j\), add its edge parity vector in the \(Q\)-summand with index
\[
                    \eta(g_x)\,\eta(\pi(u_j))\,\eta(h_{y_j})^{-1},
\]
where \(\pi\) maps the free rose group to \(G\).
Terms from \(A\) contribute zero to this opposite-side vector.
Reversing the sign of one \(R_j\) does not change its parity chain.
The formula uses only the given graph walks and the quotient images of the signed letters, since even the prefix to \(x\) or \(y_j\) is an explicit root path.

Indeed in the Cayley graph each conjugate word returns to \(g_x\).
The path for \(u_j\) and its reverse cancel in its binary edge chain, leaving only the corresponding relator in its translated lift.
Free cancellation of the product preserves the resulting chain.
In a cycle of auxiliary edges, the sum of witness paths on \(A\) is still in the fixed \(A\)-summand.
The translated \(A\)-terms of the certificates lie in other or possibly the same \(A\)-summand.
Projecting the equality supplied by the injective connecting map to the **\(B\)**-summands kills all those contributions.
Its zero sum persists after combining deck indices in \(Q\) and after common-step propagation.
Two proofs of the same endpoint equality, even along different paths in \(A\), give parallel auxiliary edges and hence the same vector.
This handles multiple relators without imposing new group relations.

## A graded obstruction invisible at the trivial quotient

Choose \(m\ge2\) and six distinct rose generators \(a,b,c,d,e,f\), with a further private generator \(r\).
Set
\[
 U=a c^{m-2}b,\qquad V=d e^{m-2}f,\qquad W=UV,\qquad W'=VU.
\]
Use additive seven-colors \(2,-1,0,1,0,-2,3\) for \(a,b,c,d,e,f,r\), respectively.
Thus \(U,V\) have colors \(1,-1\).
Make \(B\) a single oriented cycle reading \(W\), rooted at \(\beta_0\) before \(U\), with \(\beta_1\) just after \(U\).
Their colors are \(0,1\), and every interior vertex of the two arcs has color \(2\).
Give \(A\) a fresh root with one \(r\)-edge to \(x_1\).
Build a path \(x_1\to x_2\to x_3\to x_4\) reading \(W\) on each of its three successive arcs, and a separate path \(x_1\to x_4\) reading \(W'\).
Use fresh interior vertices on all four arcs.
The distinct initial and terminal letters of \(U,V\) ensure immersion at the branch vertices.
Both graphs are connected with girths \(2m\) on \(B\) and \(8m\) on \(A\).

Coning both gives the same group as coning \(B\) alone.
The sole \(B\)-cycle kills \(W\).
The cyclically conjugate \(W'\) then vanishes and the \(A\)-relation \(W^3(W')^{-1}\) is redundant.
Eliminating \(f\), which occurs once in \(W\), gives a free group and the displayed colors give a genuine homomorphism to \(C_7\).
The forward labels of all four \(x_j\) equal \(r\).
These are exactly the vertices on \(A\) of color 3.
The three \(W\)-arcs take colors from \(3+\{0,1,2\}\), attaining 3 only at their ends, and the \(W'\)-arc is based at the \(B\)-phase of color 1, which occurs only once on that cycle.
The \(A\)-root is separated from every non-root because every non-root label begins with the free private generator \(r\) followed by letters with no \(r\).
The \(B\)-root is separated because no other \(B\)-vertex has color zero.
Pairing \(x_1\) with \(x_2\) and \(x_3\) with \(x_4\) uses two \(W\)-copies.
Pairing \(x_2\) with \(x_3\) and \(x_1\) with \(x_4\) uses one \(W\)-copy and one \(W'\)-copy.
Both matchings erase color 3 by actual equalities in the original group.

The two underlying \(B\)-vectors always equal the same nonzero fundamental cycle \(z\).
Consequently both matching sums vanish at the trivial quotient.
In fact the ungraded potential test passes even after all common-step propagations of these four witnesses.
The \(W'\)-edge between \(x_1,x_4\) has no common initial step, since their respective stubs are \(\{a,d,\bar r\}\) and \(\{\bar f,\bar b\}\).
Transports of the other three edges move along corresponding positions on consecutive \(W\)-arcs.
At \(x_1\) a transport with \(x_2\) can only move forward, and at \(x_4\) a transport with \(x_3\) can only move backward.
At the intermediate vertices of each arc the two possible readings continue or retrace the same chain.
Thus the auxiliary graph consists of the four endpoint edges and paths on the three corresponding interior vertices for each internal \(W\)-position, apart from repeated identical witnesses or isolated vertices.
With all ungraded edges valued \(z\), every cycle has even length.
In \(V_{C_7}\) the first sum is twice \(z\) at index \(3\), hence zero.
The second has \(z\) at index \(3-0=3\) and \(z\) at index \(3-1=2\), hence is nonzero.
The test proves failure of asphericity for \(X\).

To check the distinction from the simpler tests, any nonempty cyclically immersed path on \(A\) follows its single core cycle, whose word contains both positive and negative letters.
On \(B\) every such word has all letters of one sign.
Thus there is no cross-side synchronous cycle.
In either side the cyclic core word has a signed marker occurring only once in one traversal, on \(A\) for example the negative \(a^{-1}\) on the \(W'\)-arc, and on \(B\) the positive \(a\).
Two walks in the same orientation with identical synchronized readings must therefore coincide at the marker, hence throughout by inverse matching.
Walks in opposite orientations cannot have the same cyclic reading, since on \(B\) the signs differ, and on \(A\) one traversal has three positive \(a\)'s and one negative \(a\), interchanged in reverse.
This rules out all off-diagonal synchronous cycles. [Synchronous pair test](Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices)

The two fixed lifts' cycle images also remain independent in the Cayley graph.
To see this, use the cone complex with just the \(B\)-cone, which has the same group and is aspherical because its rose-with-disk presentation collapses the free edge \(f\) with that disk. [Cone-to-disk model](../literature/pdf/Ope26f.pdf#page=20)
The connecting map there injects all translates of \(H_1(B)\).
The \(A\)-core chain maps to \(z\) at \(r\) and \(z\) at \(rU^{-1}\), using the three \(W\)-copies and the reversed \(W'\)-copy.
The fixed \(B\)-cycle maps to \(z\) at \(1\).
Their seven-colors \(3,2,0\) distinguish these three deck indices, proving independence for the two fixed lifts.
The obstruction for the full complex uses their other deck translates.

These two graphs do not have the prescribed source vertex types.
The test excludes any proposed surgery exhibiting mismatched vectors, whereas a single disjoint matching without additional witnesses or synchronized cycles may pass it.
General proofs of word equality need not be single copied loops, and passing the homology test does not establish asphericity or erasure in a source realization.

## Assessment history

### Decision graded-cycle-obstruction

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:24 |
| status | proved |
| reason | The review checked the direct-sum homology map, quotient indices and the distinction between torsion-freeness and asphericity. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Homology vectors of equality certificates, propagation, comparison of matchings and the test example. |
| argument | [Proof](#from-cycles-in-the-lifted-rose-to-vertex-potentials) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0091_v1.md#whole-argument-finding) | Independent review of the statement, proof and its direct inputs at the indicated scope. |

## Current assessment

[Selected decision](#decision-graded-cycle-obstruction)
