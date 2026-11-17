---
author: Yin
---

# Integral constraints on exchanges and an erased color without an exchange

## Statement

In the two-graph aspherical cone setting of the [common-word test](Yin_C_A0075_v1.md#statement), commutators of actual relation words have oriented mixed tensors over \(\mathbb Z\).
If two internal paths have words in the commutator subgroup of the full relation group, start in the same quotient color, and can both be replaced by the same readable word at their respective endpoints, their integral tensors agree.
For \(k\ge2\) six-vertex blocks in the same coarse color with independent integral types, as in the [repeated commutator construction](Yin_C_A0070_v1.md#repeated-paths-with-independent-mixed-signatures-in-the-even-bins), the \(6^k\) marked tuples belong to **\(6^k\) different** simultaneous-step components.
This allows intermediate paths through unmarked vertices.

Suppose one word cyclically carries a mark from each of \(\ell\ge2\) blocks to a mark of the next, with the internal changes witnessed by paths in the commutator subgroup of the relation group and the original cone group torsion-free.
All the blocks must then have the same true label, and the sum of their **oriented** internal changes must be divisible by \(\ell\) in the integral tensor lattice.
For distinct edge-disjoint diagonal types this forces the change of mark number in every participating block to be divisible by \(\ell\).
In particular even a *single* odd mark change is impossible in a two-block exchange.
This exclusion can be tested in a finite unitriangular group over \(\mathbb Z/\ell^2\mathbb Z\).
For \(\ell=2\) a single offending coordinate is detected in a group of order 64.
The integral assertion uses commutators and their powers, including all the indicated six-vertex blocks.
On the two actual blocks of the [thirteen-position full crossing matching](Yin_C_A0077_v1.md#matching-the-twelve-or-eighteen-marks), even a swap with no internal mark change is impossible.
Their fine states alone rule it out despite the \(6!\) genuine crossing matchings on the twelve marks.
There are also genuine thirteen-position source tuples in which these two independent blocks have the **same prescribed fine state** and their bridge has zero binary central tensor.
All \(6!\) crossing matchings again exist, and the finer auxiliary action forces all thirteen relator positions in every proof of any crossing even though the prescribed coordinates agree.
The same finer action forbids any word exchanging marks in both directions.

The following comparison tuples are obtained from genuine four-line tuples on \(n\) vertices per side.

1. The two enlarged immersed graphs are connected, have logarithmic girth lower bound and diameter \(O(\log n)\), have their designated roots separated, and have an aspherical cone complex with torsion-free fundamental group.
   Their two actual vertex factors are the original two nonzero elements of zero product over \(\mathbb F_2\), under the inclusion of the old group.
2. For some fixed \(\gamma\in(0,1)\), only \(O(n^\gamma\log n)=o(n)\) vertices on either enlarged side have added or different types.
   On restricting to the old letters every old vertex has exactly its prescribed original type, and every one of the \(n^2\) old cross-side intersections of outgoing labels retains its odd cardinality on the enlarged alphabet.
   Only two new rose generators are required.
3. For an actual new character onto \(C_7\), the **entire** forward left color \(3\) can be perfectly paired by equal original-group labels.
   A displayed full pairing has a nonzero binary central total of rank \(K\asymp n^\gamma\) in a projected mixed tensor space.
   Every perfect matching of this color by original equalities uses at least \(K\) independent translated first-homology directions in the sum of the dimensions from the two sides, even for unrestricted relator certificates.
4. There are \(K/2\) disjoint pairs of independent six-vertex blocks in the erased color.
   For each such pair all twelve marks have one common true label, every one of the \(6!\) full crossing matchings extends to a matching of the entire color, and **no** word carries a mark of the first block to any mark of the second while also carrying a mark of the second to any mark of the first.
   This last conclusion includes swaps with zero mark changes.

The added paths have low-degree vertices and the new character is trivial on the old group.
The erased color has \(O(n^\gamma\log n)=o(n)\) vertices, compared with the prescribed \(n/7-4\) vertices in the four-line law.
Its projected binary factors both vanish, while the nonzero factors in the original group algebra are preserved.
The comparison therefore leaves open the [prescribed four-line color counts and exact vertex types](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).

## Oriented central displacements

Let \(F\) be the free rose group, \(G\) the cone group, \(N=\ker(F\to G)\), and \(\eta:G\to Q\) a finite quotient.
The universal-cover relative sequence from the [graph cone calculation](Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials) also holds with integer coefficients.
Contractibility makes its connecting map an isomorphism
\[
     \bigoplus_{g\in G}\bigl(H_1(A;\mathbb Z)_g\oplus H_1(B;\mathbb Z)_g\bigr)
                    \longrightarrow H_1(N;\mathbb Z).
\]
The groups on the left are free abelian, and conjugation by an element of \(F\) translates the deck indices by its image in \(G\).
This follows by translating the lifted graph and changing the basing path, which induces only inner conjugation in \(N\).
Combine the deck indices by \(\eta\), discard the identity summand of \(A\), and denote the resulting two finite-rank free abelian groups by \(U,V\).
Use the group
\[
 P_{\mathbb Z}=U\times V\times(U\otimes_{\mathbb Z}V),\qquad
 (a,b,c)(a',b',c')=(a+a',b+b',c+c'+a\otimes b').
\]
The tensor coordinate subgroup is central.
The two-coordinate map on \(N\) lifts to \(\rho:N\to P_{\mathbb Z}\) because \(N\) is the fundamental group of the lifted rose, a graph.
Its restriction to the rooted copy of \(A\) is central and factors through this copy's integral \(H_1\).
Negate that restriction on its actual deck summand, extend by zero on the other summands, and multiply by this central correction.
We may therefore take \(\rho\) trivial on all fixed-root \(A\)-loops.
For an oriented internal \(A\)-path from \(x\) to \(y\) with word \(p\in[N,N]\), its based tensor is the last coordinate of \(\rho(f_x p f_x^{-1})\), where \(f_x\) is a left root path.
This matches the displacement \(\rho(f_y f_x^{-1})\) since the two words differ by a fixed-root \(A\)-loop.
Changing either endpoint root path multiplies it on the left by a fixed-root graph loop and does not alter the value.
Reversing the path negates it.
For a commutator of a translated \(A\)-loop with class \(u\) and a translated \(B\)-loop with class \(v\), in that order and with convention \([x,y]=xyx^{-1}y^{-1}\), the answer is \(u\otimes v\) by the multiplication law, independent of the two central coordinates of the factors.

Suppose \(p_x,p_y\in[N,N]\) are the two given paths at starts \(x,y\), and a common word \(w\) has the same respective endpoints.
It has trivial image in \(G\) since each given internal path does.
The two homomorphisms \(n\mapsto\rho(f_x n f_x^{-1})\) and \(n\mapsto\rho(f_y n f_y^{-1})\) agree in their first two coordinates if the starts have the same \(Q\)-color.
Their pointwise discrepancy is consequently a homomorphism to the central tensor subgroup and vanishes on \([N,N]\).
If \(x,y\) have the same actual label, the maps differ by an inner conjugation in \(P_{\mathbb Z}\), which preserves their central values for \(w\) since its images equal those of the given paths.
If their labels differ, the rooted-loop comparisons place \([w]\) in the full integral \(A\)-summand at \(g_x^{-1}\) and also in the distinct one at \(g_y^{-1}\), using \([p_x]=[p_y]=0\).
Disjointness of summands forces \([w]=0\), so \(w\in[N,N]\) and the two maps again agree there.
Thus every synchronized path between two marked pairs has equal oriented internal tensors.
In six-vertex blocks of independent types \(T_i,T_j\) this gives \((h'-h)T_i=(l'-l)T_j\), forcing both differences zero.
Projecting any simultaneous path to pairs of coordinates proves the full \(6^k\) component count.

## Divisibility for a cyclic exchange

Number the blocks cyclically, with \(x_i,y_i\) in block \(i\), and let the same \(w\) be readable from \(x_i\) to \(y_{i+1}\).
Write \(g_i\) for block \(i\)'s true label.
The equations \(g_i\pi(w)=g_{i+1}\) imply \(\pi(w)^\ell=1\), hence \(\pi(w)=1\) by torsion-freeness.
Thus the \(g_i\)'s all coincide.
Use the root words \(f\) as above and let
\[
 n_i=\rho(f_{x_i}f_{x_0}^{-1}),\qquad
 v_0=\rho(f_{x_0}w f_{x_0}^{-1}),\qquad
 c_i=\rho(f_{y_i}f_{x_i}^{-1}).
\]
As fixed-root \(A\)-loops are killed, \(c_{i+1}n_{i+1}=n_i v_0\).
The \(c_i\) are central internal changes, so \(v_0^\ell=\prod_i c_i\).
If \(v_0=(a,b,c)\), its first coordinates in this power are \(\ell a,\ell b\).
Both must vanish, forcing \(a=b=0\) in the free abelian axes.
The last coordinate is then \(\ell c\).
For distinct diagonal types from edge-disjoint simple cycles, evaluating on one oriented edge of the first cycle and one of the second gives an integral tensor coordinate functional which is one on the selected type (after choosing signs) and zero on the others.
Thus \(\ell\) divides every individual oriented mark change in those blocks.
For \(\ell>5\) every such change in a six-vertex block must be zero.

For a finite test reduce the three coordinates modulo \(\ell^2\), and, for the scalar coordinate test, apply integral linear forms to the two axes and their product to the central coordinate.
In this finite group \(v_0^\ell\) has first coordinates \(\ell a,\ell b\) and last coordinate \(\ell c+\binom{\ell}{2}a\otimes b\).
Vanishing first coordinates now give \(a,b\) divisible by \(\ell\), so the quadratic term vanishes modulo \(\ell^2\).
The resulting scalar central value must be divisible by \(\ell\) modulo \(\ell^2\).
For a swap this uses unitriangular three-by-three matrices over \(\mathbb Z/4\mathbb Z\), whose three free entries give 64 elements.
This excludes an odd change even if every other block change is even, beyond the exponent-two rank bound of the [binary cyclic test](Yin_C_A0075_v1.md#a-common-word-cycling-among-blocks).

For blocks in the [thirteen-position state law](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers), there is a second necessary condition when every mark in block \(i\) has the same visible state \(\lambda_i\) in a fixed coarse color \(c\).
A common word connecting these blocks has zero rotation because its initial and terminal coarse colors agree.
Its image in the finite auxiliary group is therefore a lamp vector \(b\) with no rotation.
From any state at \(c\), right multiplication by this word adds the same visible vector \(v=\operatorname{proj}_{\rm vis}(S_cb)\).
Consequently a cyclic exchange requires \(\lambda_{i+1}=\lambda_i+v\) and \(\ell v=0\) in \((\mathbb Z/m\mathbb Z)^{13}\), with \(m=4t+1\).
When \(\gcd(\ell,m)=1\), every block in the cycle must have the same fine state.
For the actual [two blocks linked by a squared bridge](Yin_C_A0077_v1.md#making-every-position-change-with-a-central-value), the difference is \(2\) in every visible slot, hence is nonzero modulo \(m\).
Since \(m\) is odd, no common word can exchange any marks between these blocks in both directions, even with unconstrained proof words and zero internal changes.
This uses only a necessary condition for readability in the actual graphs, so the auxiliary permutations need no action on the original group.

## Equal prescribed fine states in genuine source tuples

Fix the original thirteen-lamp modulus \(m=4t+1\) and the two sets \(J_1,J_2\) of its nonzero entries in the [C65 fine counts](Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms).
Use the two C65 actions with modulus \(m'=m^2\), each of size \(d'=7(m')^{13}\).
Reduction of lamps modulo \(m\) induces equivariant projections of the auxiliary groups and the two coset state sets, since the subgroup hidden at the root maps onto the corresponding old hidden subgroup.
Each side has \(m^{13}\) fine lifts of each prescribed modulus-\(m\) state.
Take \(n\) a sufficiently large multiple of \(2d'v^2\), where \(v=16513\).
Allocate each full type uniformly to all \(d'\) states first.
For each nonzero \(j\in\mathbb Z/m\mathbb Z\) take its representative \(1\le j\le m-1\) in \(\mathbb Z/m'\mathbb Z\).
Apply the exact integer changes of C65 on the distinguished constant-lamp states with these representatives and on the zero-lamp states, using the original \(t,J_1,J_2\).
Do not modify the other states.
Projection gives exactly the modulus-\(m\) count of **each full type at each prescribed state**, by equal fiber size before the changes and the single chosen lift of each nonzero distinguished state.
At the finer level the rotation preserves all lamp entries and the changes depend on the line and coarse color through their difference.
The private pairs and mixed pairs therefore still match exactly by the same per-line and unchanged-pool arguments as in C65.
This gives valid original matched tuples with additional auxiliary information.
The law sampled with the extra information need not be uniform on the projected matchings.

For each fixed \(m'\) these are bounded perturbations of its two balanced transitive actions.
The [geometric comparison](Yin_C_A0065_v1.md#safeguarded-realizations) uses long matching pools of size \(np/d'+O(1)\), positive prescribed turns, bounded whole-chain state factors and transitivity, all valid here.
The [coarse perfection proof](Yin_C_A0065_v1.md#why-the-coarse-kernel-may-also-be-perfect) also applies: the conjugates over all seven offsets of the two hidden coordinate subgroups still generate the full lamp base, and its entropy and bounded-diameter estimates require only a fixed number of states and bounded perturbations.
Thus there are actual connected, root-separated, aspherical source tuples with the original torsion-free group and nonzero binary zero product, and with perfect \(C_7\)-kernel.
The finer coset data are graph states, including in this perfect-kernel family.

Use the [one-lamp cycles and the word \(D\)](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges) at modulus \(m'\).
Their search uses only the fixed-size action, neutral trees in the root state, linear turn pools, and the fact that the appropriate mixed letter fixes its own root state.
As before \(D\) is trivial in the actual group, adding one to every visible slot of a left color-3 state.
Take two neutral independent commutators \(M_1,M_2\) from the same search.
Let \(E\) be a neutral-guard conjugate of the freely reduced form of \(D^{4m}\).
It is nonempty by its change \(4m\ne0\bmod m^2\), and in the binary mixed group its based value is the identity since the fourth power of every element there is one.
Choose the guard to avoid cancellations and read \(M_1^5 E M_2^5\) on a simple open left path starting at coarse color \(3\).
For any fixed \(0<\delta<1\), this fixed number of repetitions per word increases only the constant in the \(CR+C'\) length bound in [the fresh-path and conditioning estimate](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges).
Taking the cycle-search exponent and the fixed positive girth constant sufficiently small gives at least \(\lfloor n^{1-\delta}\rfloor\) disjoint such paths with conditional probability tending to one, simultaneously with the stated safeguards.
All twelve marks on each path have one true label, the two blocks' tensors \(T_1,T_2\) are independent, and each of the \(6!\) crossing matchings has total \(T_1+T_2\) by the [endpoint-potential computation](Yin_C_A0077_v1.md#matching-the-twelve-or-eighteen-marks).
The two states agree modulo \(m\), and the end of the first block and the start of the second agree in the binary central test.
In the modulus-\(m'\) auxiliary action the two block states differ by \(4m\) in every visible slot.
Consequently every proof of each crossing requires terms at all thirteen side and coarse-index positions by the [one-slot certificate calculation](Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate), even though none of the modulus-\(m\) slots distinguishes the endpoints.
A bidirectional exchange would require \(8m=0\bmod m^2\), impossible since \(m\ge5\) is odd.
This excludes a common exchange even when compared marks have equal original labels, equal prescribed modulus-\(m\) states and zero internal changes.
It does not presume or produce full-color erasure at the prescribed source counts.

## Keeping the old factors while adjoining trees

Choose an admissible sequence of [C65 realizations](Yin_C_A0065_v1.md#safeguarded-realizations) on \(n\) vertices per side with [C72's disjoint neutral cycles](Yin_C_A0072_v1.md#a-closed-graph-loop-changing-a-single-lamp).
For some fixed \(\gamma>0\) these supply at least \(\lfloor n^\gamma\rfloor\) simple mutually vertex-disjoint cycles on each side, all of length \(O(\log n)\).
We take \(\gamma<1\).
These original groups \(G_0\) have a perfect kernel over the given \(C_7\), hence \(G_0\) has no quotient \(C_2\).
There is an old graph loop of odd rose-word length.
Indeed sending every old rose generator to the nonzero element of \(C_2\) would kill both graph loop groups if all fundamental graph loops had even length.
Use breadth-first trees in the two graphs to choose a fundamental loop of odd length \(O(\log n)\), since both original diameters are \(O(\log n)\).
Freely and cyclically reducing gives a nonempty cyclically reduced loop word \(L\) at an old vertex of its graph, still of odd length.
The ordinary free-rose abelianization \([L]_F\) is nonzero because its coefficients sum to one modulo two.

In binary first homology project out the line generated by the class of \(L\) on its side.
The simple disjoint cycle classes of that side lose at most one dimension, so one can retain \(K\asymp n^\gamma\) independent cycle classes on each side modulo this line, with \(K\) even.
Write \(U_i,V_i\) for the chosen old oriented cycle words, \(1\le i\le K\), and let
\[
                         M_i=[s_i U_i s_i^{-1},V_i].
\]
Choose the old letter \(s_i\) outside the inverse pairs of the end letters of both cycle words, so \(M_i\) is cyclically reduced.
It is null in \(G_0\), and has zero exponent sum in every rose generator.
The independent integral diagonal types from these old cycles are primitive in the full integral tensor lattice by the edge evaluations above.

Extend the rose by just two generator pairs \(r_A,r_B\).
Give all old letters color zero and \(r_A,r_B\) color \(3\) in a new \(C_7\).
For every consecutive pair of indices \(i=2j-1,\ i+1=2j\), put
\[
         W_j=M_i^5\,h_j L^2h_j^{-1}\,M_{i+1}^5\,h'_j L(h'_j)^{-1}.
\]
Each of the old guard letters \(h_j,h'_j\) can avoid the inverse pairs of the end letters of \(L\) and of its neighboring commutator words, including across the cyclic boundary.
There are only finitely many forbidden letters at a given junction and the old alphabet suffices.
Thus \(W_j\) is cyclically reduced, null in \(G_0\), and of odd length \(d_j=O(\log n)\), since the commutators have even lengths.

On each side \(T=A,B\) select \(K/2\) different old vertices \(z_{T,j}\).
At vertex \(z_{T,j}\) attach an outward stem \(r_T\) followed by the first \(2d_j-1\) letters of \(W_j W_j\) on a line of fresh vertices.
Different trees use disjoint new vertices.
The resulting maps remain immersions because no old vertex had its private stem and no tree word has an inverse splice.
The new vertices on this tree are indexed by prefixes of \(W_j W_j\) of lengths \(0,\ldots,2d_j-1\) after the stem, so the two graphs have the same enlarged number of vertices.
Their old-to-old cross-side intersections of signed stubs are unchanged because the two extra stem labels are distinct and absent on the other side's old vertices.
Only \(K/2\) old vertices on each side acquire an additional stub.
The new vertices and altered old vertices together number \(O(K\log n)\) per side.
Girth is unchanged because every new edge belongs to a tree, and the diameter increases by at most twice the longest added path.

Each enlarged graph retracts onto its old graph by contracting the trees.
The maps to the rose are homotopic relative to the old graph to the old graph map composed with that retraction, by contracting the parametrized tree paths toward their attachment points.
Homotopy invariance of attaching the cones therefore identifies the enlarged cone complex up to homotopy with the old one wedged with the two extra circles.
Its fundamental group is \(G_0*F(r_A,r_B)\), which is torsion-free by free-product normal form.
Its universal cover is homotopy equivalent to a tree of contractible copies of the old universal cover joined at points, hence it is aspherical.
The new character is a surjection, and the old group embeds with its original root labels.
A new label on side \(T\) is \(g_{z_{T,j}}r_T p\) for some old prefix word \(p\), with \(g_{z_{T,j}},p\) evaluated in \(G_0\).
Free-product normal form makes it nonidentity, preserving both designated root separations.

On each appended path the prefixes of lengths \(a,d_j+a\), \(0\le a<d_j\), give the same original-group label, because \(W_j=1\) there.
Every new vertex has new color \(3\), and every old vertex new color zero.
These disjoint pairs exhaust the entire color \(3\) on each forward side.
They also cancel from the two group-ring factors over \(\mathbb F_2\), including after inverting the right-side vertex list.
The enlarged factors are therefore exactly the old nonzero factors in the embedded \(\mathbb F_2 G_0\), with their zero product preserved.
In the new cyclic quotient each factor has zero image since all its surviving labels have color zero and the old list has even cardinality.
The old four-line character can separately be extended across the two free letters, but its even outside bins are a different erasure question.

## A full matching of large rank with no swap

Use the [simultaneous axis prescriptions](Yin_C_A0072_v1.md#a-tensor-bound-on-unrestricted-certificates) over \(\mathbb F_2\) for the enlarged aspherical cone and its new character.
Keep only the coarse index \(3\) on each side and quotient also by \([L]\) on its side there.
All named commutator factors are based at old vertices of color zero and are read from prefixes of color \(3\).
Tree attachments leave both graph homology groups unchanged.
In the retained axes \(M_i\) therefore has central value \(T_i=[U_i]\otimes[V_i]\), while every conjugate of \(L\) is killed.
These values persist under the guard conjugations at the given coarse indices.
For a prefix \(p\) of the first traversal in a graft, a root word \(f\) to its old attachment vertex gives paired endpoint words \(f r_A p,\ f r_A W_j p\).
Their based displacement is exactly \(f r_A W_j r_A^{-1} f^{-1}\).
Thus every one of its \(d_j\) pairs has value \(T_{2j-1}+T_{2j}\).
Oddness of \(d_j\) makes the binary sum over the entire erased color \(\sum_{i=1}^K T_i\), of rank \(K\) by the independent choices on both sides.
For an arbitrary alternative matching by original equalities the [quotient bound (2)](Yin_C_A0072_v1.md#a-tensor-bound-on-unrestricted-certificates) forces the sum of dimensions of the spans of its named translated homology vectors in the two retained axes to be at least \(K\).
The comparison applies to arbitrary conjugators and arbitrary graph-loop words, including certificates with no explicitly balanced decomposition.

In the first traversal of \(W_j\) mark the six boundaries of the five copies of \(M_{2j-1}\) and the six boundaries of the five copies of \(M_{2j}\).
These blocks have no shared vertex, because their separating path \(h_j L^2h_j^{-1}\) has positive length.
Every completed segment is trivial in the original group, so all twelve labels equal \(g_{z_{A,j}}r_A\).
Any prescribed perfect matching of the twelve, including any crossing bijection, can be completed on the whole color.
Indeed every true-label class there has even size, and removing the twelve marks subtracts twelve from just one class.
The complement can be fixed once for all the choices.

Assume the same word is readable from a mark in the first interval to a mark in the second and from a mark in the second to a mark in the first.
Reduce the common word, since adjacent inverse letters retrace the same edge in an immersed graph and their deletion preserves both endpoints.
If both paths stay in this tree, a reduced path there is the unique connecting path.
In the forward direction its rose abelianization is \(2[L]_F\), as the remaining pieces are whole copies of commutators.
In the reverse direction it is \(-2[L]_F\), different in the free abelian rose lattice.
If one path reaches the old graph, it must cross the private stem inversely and the path before that first crossing is the unique backward tree segment from its initial mark.
A path remaining in the tree interval uses no stem letter.
If both paths reach the old graph, their first private letter occurs at different positions, since every first-interval mark is strictly closer along the tree to the stem than every second-interval mark.
Neither case can give identical reduced words.
This proves the complete absence of common-word exchanges in these actually erased blocks.
The exceptional low-degree vertices and choice of quotient are essential limits of what this example tests about the original four-line model.

## Assessment history

### Decision oriented-exchange-and-refined-states

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:46 |
| status | proved |
| reason | Independent review verified the integral action and divisibility tests, the precise fine-state law, and preservation of the old factors in the grafted comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Restrictions on genuine exchanges and the separate scope of complete erasure under the new character in enlarged graphs. |
| argument | [Proof](#oriented-central-displacements) | Oriented lifts, finite reduction, projections of the finer state tables, and geometry and labels after the tree attachments. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0115_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-oriented-exchange-and-refined-states)
