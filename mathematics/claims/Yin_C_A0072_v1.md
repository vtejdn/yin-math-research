---
author: Yin
---

# Equal-label paths crossing thirteen prescribed relator positions

## Statement

Fix \(t\ge1\), set \(m=4t+1\), and use the [two coset actions and four-line populations](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers) with cyclic lamp group \(\mathbb Z/m\).
The left state at coarse color \(3\) records thirteen lamps, one at each \((A,q)\) for \(q\ne0\) and each \((B,q)\) for \(q\in C_7\).
Each based conjugate in an original-presentation certificate changes at most the lamp of its specified side and coarse deck index. [Certificate convention](Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate)
For every fixed \(0<\delta<1\) one can choose a fixed positive logarithmic girth constant and \(\gamma>0\) such that the following properties hold together with probability tending to one conditional on girth.

1. There are at least \(\lfloor n^{1-\delta}\rfloor\) vertex-disjoint simple paths on the left, each with designated vertices of the **same original group label** in all \(m^{13}\) fine states over coarse color \(3\).
   There is also a word \(D\) connecting a state to the state obtained by adding one to every visible lamp, along actual equalities.
   Its first segment is a closed walk on the right graph read as an open path on the left and changes the \((B,3)\) lamp.
   Every proof for the endpoints of a \(D\)-path uses all thirteen positions, even allowing unrestricted conjugates of both sides' relators.
2. On disjoint simple paths one can read two parallel copies of this same bridge \(D\), starting from the two endpoints of a nonzero central commutator witness.
   Their initial right-loop segments give two directly synchronized crossings of fine states, and the entire bridges change all thirteen lamps.
   On the far side one can read a second commutator with an independent tensor at **both** transported endpoints.
   The first tensor is preserved by the common word \(D\), so two parallel copies of any word cannot join the endpoints of one such central pair to those of a pair with a different central tensor.
3. There is a set of \(2K\) actual left color-3 vertices with a witnessed perfect matching, where \(K\asymp n^\gamma\).
   Every pair of this displayed matching changes all thirteen lamps.
   In **any** perfect matching of these same vertices by original equalities, and for **any** supplied graph paths and free-word proofs, at least \(2t\) different pairs use each of the thirteen positions.
   At \((A,3)\) and \((B,3)\) together the proofs use at least \(K\) independent first-homology directions, in the sum of the two dimensions defined below.
   Thus they use at least \(K+22t\) relator occurrences in total.
   These assertions allow the named loops and conjugators to be chosen after the tuple and the matching.

The realizations have aspherical cone, torsion-free original group, the prescribed separated roots and the two nonzero binary factors of zero product.
The coarse \(C_7\)-kernel can be perfect on these same tuples, excluding every nontrivial solvable-kernel refinement. [Perfect coarse kernel](Yin_C_A0065_v1.md#why-the-coarse-kernel-may-also-be-perfect)
Fine states constrain proofs and can distinguish occurrences of the very same original label.
Different disjoint paths can repeat the same group label.
The actual perfect matching above covers a subset of one color.

## A closed graph loop changing a single lamp

Use the notation \(W=(V^{C_7}\oplus V^{C_7})\rtimes C_7\), \(V=\mathbb Z/m\), \(\theta:F\twoheadrightarrow W\) and \(\Omega_T=H_T\backslash W\) from [C65](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers).
Put \(d=|\Omega_T|=7m^{13}\), \(v=16513\), and \(p=129/v\).
For each side \(T=A,B\) let the oriented mixed letter \(\lambda_T\) satisfy \(\theta(\lambda_T)=e_{T,0}\), the unit lamp at slot zero of that side.
Right multiplication by \(\lambda_T\) fixes the state \(H_T\).
Call an ordinary letter neutral here if its inverse is ordinary and its image in \(W\) is the identity.
Every vertex has at least 120 such stubs by the four-line inverse pairing.

Every prescribed signed-letter pool in a specified state has size \(np/d+O(1)\).
At either side any two distinct required stubs have positive joint population in each state.
Two distinct ordinary points determine one line, an ordinary point and an extra have joint fraction \(p^2\) in the balanced law, and two distinct extras have joint fraction \(p/2\) on \(A\) and \(p\) on \(B\).
Thus, conditional on carrying the incoming stub, a distinct required outgoing stub has limiting fraction at least \(\min(1/129,p,1/2)>1/300\).
The bounded changes at the fixed \(d\) states preserve this strict inequality with room for \(o(n)\) used vertices. [Original types, §2.1](../literature/pdf/Ope26f.pdf#page=4) [Exact state counts](Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms)
In the unconditioned sampling, after any revealed history touching \(O(n^{1-b})\) vertices for fixed \(b>0\), a fresh partner with any required permissible next stub has conditional probability at least \(1/300\) for large \(n\).
This uses the unused part of its particular bijection and holds even when that matching block has been sampled previously.

Fix \(0<a<1/8\), put \(b=a/2,\ R=\lceil a\log n/\log64\rceil\) and \(M=64^R\).
In state \(H_T\) seek a simple cycle using exactly one mixed letter \(\lambda_T\) and otherwise neutral edges.
Grow a 64-ary neutral tree to depth \(R\) from a fresh vertex, marking all touched vertices, including unsuccessful trials.
Use the [tree exposure with up to 100 attempts per internal vertex](Yin_C_A0053_v1.md#finding-a-short-closed-word-on-one-side).
Here an edge returning to the current tree aborts the trial.
There are \(O(M)\) attempts and \(O(M)\) current vertices, so this costs probability \(O(M^2/n)=o(1)\) conditional on the earlier trials.
Failure at a vertex without a current-tree hit requires at least 37 old destinations in its attempts, each with conditional probability \(O(n^{-b})\).
Over the tree this costs \(O(n^{a-37b})=o(1)\).
Thus with conditional probability \(1-o(1)\) the whole fresh tree is available.

Divide the leaves into two halves.
From each leaf in the first half reveal one unused neutral edge, seeking a fresh endpoint carrying \(\lambda_T\).
Do the same in the second half seeking \(\bar\lambda_T\).
An accidental arrival in the tree can be discarded by aborting, at cost \(O(M^2/n)\).
Until such an abort the conditional turn bound and binomial domination give at least \(cM\) fresh endpoints of the required kind in each half except for probability \(\exp(-\Omega(M))\), for some \(c>0\).
This bound may be applied with fictitious additional Bernoulli trials after an abort, subtracting its probability.
Retain only endpoints first discovered by their designated edges, so all retained endpoints are distinct.
Their mixed stubs are unused since all these exposures used neutral letters.
The two lists lie in the one compatible mixed block because \(H_T\lambda_T=H_T\).
Expose the \(\lambda_T\)-edges from the first list.
Until the first hit each draw has probability at least \(c'M/n\) of ending in the second list, whose \(\bar\lambda_T\)-stubs all remain available.
A hit closes a simple cycle through the two new leaves and their tree path, of length at most \(2R+3\).
It traverses exactly one mixed edge and can be oriented to have \(\theta\)-value \(e_{T,0}\).
The conditional success probability per trial is \(\Omega(M^2/n)\).
In \(\lfloor n^{1-b-a}\rfloor\) trials per side the total number of touched vertices is \(O(n^{1-b})\), and failure to find a cycle is at most \(\exp(-\Omega(n^{a-b}))\).
Write \(L_T\) for one such oriented cycle word, based at one of its vertices in state \(H_T\).

On both sides find also \(\lfloor n^{a/4}\rfloor\) vertex-disjoint simple neutral cycles in state \(H_T\), marking all previous vertices throughout the searches.
The [disjoint neutral-cycle proof](Yin_C_A0054_v1.md#many-opposite-cycles-and-simultaneous-open-lifts) works here with the same fixed positive turn fractions, linear block sizes and total \(O(n^{1-b})\) budget.
In particular it gives lengths at most \(2R+2\) and failure probability \(\exp(-\Omega(n^{a-b}))\).
One may prevent reuse of earlier successful vertices by treating earlier touched vertices as old at the start of each new trial.
The cycle classes on each side are independent, also modulo the class of \(L_T\), since their supports are edge-disjoint and the latter contains a mixed edge.
Call their words \(U_i\) on \(A\) and \(V_i\) on \(B\).

## Reading prescribed state changes and parallel bridges

All cycles just found are relations in the original cone group.
Their basepoints need only lie in the root component, as holds on the connectedness event.
An oriented one-slot move from a color-3 state is realized by the word \(h L_T^{\pm1}h^{-1}\), with \(h\) a rose word of pure rotation \(q-3\).
Indeed right multiplication from coarse color \(3\) shifts the lamp by \(S_3S_{q-3}e_{T,0}=e_{T,q}\) with the chosen sign.
This works at every starting state and every visible position.
The word \(h\) can be made of at most six copies of the active rotation letter with increment \(1\), with neutral guard letters at either end.
The guards can be chosen to avoid inverse cancellations next to the rotation, the based cycle, and the preceding or following conjugated word.
For rotation zero one neutral guard alone suffices.
At a designated \((B,3)\) move one can use \(h=1\), reading \(L_B\) itself as a genuine synchronous path based at the chosen \(B\)-cycle vertex.
The guards at its neighbors can avoid its first and last letters.
All these choices preserve the \(W\)-image of the intended move since the guards are neutral, and preserve triviality in \(G\) by conjugation.

Choose \(D\) as a product of the thirteen positive one-slot moves, beginning with the unguarded \(L_B\) at \((B,3)\).
Its endpoints in a left lift differ by one at every visible position and have the same original label.
The [single-slot necessity for arbitrary certificates](Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate) now requires all thirteen positions in **each** proof of such an equality.
Only its initial segment is required to be directly readable as a \(B\)-cycle.
The complete bridge can use both sides' defining relations.

A fixed finite list of signed one-slot moves can likewise be realized by a concatenation of guarded words.
In particular the graph of the \(m^{13}\) visible states at color \(3\) with unit coordinate steps is connected.
A traversal of a spanning tree visits them all using at most \(2(m^{13}-1)\) moves.
A simple open lift of its word has a vertex of the same original group label at each successive move boundary, hence in every one of the states.
The graph path stays simple even when its fine-state itinerary revisits a state.

For two independent tensor directions take neutral commutator words
\[
       M_i=[s_i U_i s_i^{-1},V_i],\qquad
       T_i=[U_i]_3\otimes[V_i]_3 .
\]
Choose \(s_i\) neutral outside the inverse pairs of the first and last letters of the two cycles, so \(M_i\) is freely reduced.
It is an original equality word at any left occurrence and its [mixed central tensor](Yin_C_A0066_v1.md#the-finite-tensor-calculation) at coarse color \(3\) is \(T_i\).
Conjugation by a neutral guard preserves this tensor by the formula for a commutator and the unchanged two coarse indices.
After choosing the guards and retaining \(M_i\) for the guarded word, the freely reduced path word is
\[
                  M_2^{-1}\ D^{-1}\ M_1\ D\ M_2 .                     \tag{1}
\]
In traversal order label the six boundaries \(z_0,y_0,x_0,x_1,y_1,z_1\).
Then \(x_i\to y_i\) for \(i=0,1\) read the identical forward \(D\), including the same initial right-side loop.
The two fine states at \(x_0,x_1\) agree, as do those at \(y_0,y_1,z_0,z_1\), and their difference across a bridge is the all-ones vector.
The source pair \(x_0,x_1\) has value \(T_1\), which is retained between \(y_0,y_1\) under common right transport by \(D\).
Both \(y_i\to z_i\) have value \(T_2\).
All six true labels agree, and \(T_1,T_2\) are independent, since the neutral cycles in either graph have independent classes.
The two transported pairs \(y_0,y_1\) and \(z_0,z_1\) necessarily have the same value \(T_1\).
In general common readable right steps preserve the displacement in the homomorphism killing the fixed \(A\)-copy, as is seen by canceling the common suffix in the two endpoint root words.
Consequently it is impossible to have parallel copies of the same bridge with the two original and transported pair tensors prescribed to be distinct.
This applies regardless of how the bridge's own equality is proved and does not assign it a central value.

Here are the simultaneous open-path estimates, also for the family of words used below.
The list consists of one fixed spanning-tree tour, (1), and at most \(\lfloor n^{a/4}\rfloor\) words \(D M_i\).
There are constants \(C,C'\) depending on \(t\) such that every length is at most \(CR+C'\), since each named cycle is no longer than \(2R+3\) and all fixed moves use bounded guards.
These constants can be chosen before choosing \(a\).
For (1) choose any color-3 start, for the tour take a chosen first state, and for \(D M_i\) use the particular initial states specified below.
The two neutral exterior segments in (1) keep the state fixed, so a chosen start at \(z_0\) determines the state at \(x_0\) by the inverse \(D\) move.
Using \(O(n^{1-b})\) further exposures, split \(\lfloor n^{1-b}/(CR+C'+1)\rfloor\) trials as evenly as possible among these words.
Start each at a fresh vertex of its positive first-stub pool and expose each edge to a fresh endpoint bearing the next required stub, keeping the marks from all trials and both kinds of cycle searches.
Conditional on those histories the unused parts of all fixed matchings remain uniform.
Every prescribed reduced turn, including those incident to mixed or rotation stubs, has the \(1/300\) lower bound above in the required state.
This argument does not condition on all matching blocks of any side or state.
Each word's success count dominates a binomial with mean at least
\[
        n^{1-b-a/4-Ca\log(300)/\log64-o(1)} .
\]
Choose \(a>0\) sufficiently small that this exceeds \(n^{1-\delta/2}\) for large \(n\).
Except with probability \(\exp(-\Omega(n^{1-\delta/2}))\) times the number of words, every word has at least \(\lfloor n^{1-\delta}\rfloor\) successful simple lifts, disjoint as vertices also across words.
The cycle search failures above are bounded by \(\exp(-\Omega(n^{a/2}))\).
Choose \(c_0>0\) with \(c_0\log(2d|T_{\rm src}|/p)<a/4\) and \(2c_0\log132<1\), with \(|T_{\rm src}|\) the number of signed letters.
The [short-cycle switch count](Yin_C_A0053_v1.md#exponents-arbitrarily-close-to-one) uses only the fixed block sizes \(np/d+O(1)\) and permits the [nonregular states](Yin_C_A0065_v1.md#safeguarded-realizations).
Switching at most \(n^{3a/8}\) bad edges costs at most \(\exp(O(n^{3a/8}\log n))\) on division by the girth probability.
This is absorbed by both unconditional estimates.
Intersect with C65's geometric and perfect-kernel events after conditioning, which hold with probability \(1-o(1)\) for this sufficiently small fixed \(c_0\).
All occurrences and group equalities above are now in the actual rooted source graphs.

## A tensor bound on unrestricted certificates

For any aspherical double cone and given finite quotient \(Q\), use the notation \(N=\ker(F\to G)\) and the binary spaces \(U,V'\) of the [mixed tensor construction](Yin_C_A0066_v1.md#the-finite-tensor-calculation), omitting the identity \(A\)-summand for left pairings.
The prime distinguishes \(V'\) from the lamp group.
Take any linear quotients \(\bar U,\bar V\) of these spaces and form \(P=\bar U\times\bar V\times(\bar U\otimes\bar V)\) with multiplication as in C66.
Choose a representative root path from the identity to each *actual* deck vertex of the lifted rose, using the empty path at the identity.
On every based translated graph group prescribe its natural homology map to its side's quotient axis in \(P\), with central coordinate zero.
All these prescriptions extend simultaneously to \(\rho:N\to P\).
Indeed the direct-sum homology isomorphism for the universal-cover pair gives the first two coordinates of such a map, and freeness of the lifted rose group gives an arbitrary lift to \(P\).
On each translated graph its discrepancy with the prescribed axis map is a homomorphism to the central elementary abelian subgroup because both maps agree modulo that subgroup.
The same direct-sum isomorphism, before merging any deck indices, extends all discrepancies to one central correction on \(N\).
This proves the assertion even for infinitely many translates and gives trivial image to the fixed \(A\)-loop group.

In particular the image is the identity for **every** conjugated root relator whose named homology vector is zero in its quotient axis.
Its arbitrary conjugator differs from the chosen section at that deck vertex by an element of \(N\), and conjugating the identity cannot alter it.
Further quotient maps on \(\bar U,\bar V\) induce a homomorphism on \(P\) by the associated tensor projection on its central coordinate.
If these quotients kill the classes of all terms in some supplied collection of arbitrary certificates, every corresponding endpoint displacement becomes the identity.
For another matching on the same vertices whose displacements are known central tensors, their total must become zero after this quotient.
Indeed root paths may differ by fixed \(A\)-loops with trivial image, and the displacement products telescope along the alternating cycles of the two matchings.
This gives a rank bound independent of any balance assumption on the competing certificates.
If the original known total is \(T\in\bar U\otimes\bar V\) and the named competing first-layer spans are \(E\subset\bar U,\ J\subset\bar V\), then
\[
                 T\in E\otimes\bar V+\bar U\otimes J,\qquad
                 \operatorname{rank}T\le\dim E+\dim J .               \tag{2}
\]
The first assertion is the kernel of the tensor projection to \((\bar U/E)\otimes(\bar V/J)\), by choosing complements.
The two summands in such a decomposition have ranks at most \(\dim E,\dim J\), respectively.
The two dimensions enter through their sum because an unrestricted commutator certificate can use only conjugates of a loop from one side.

## One actual matching with both lower bounds

Take \(K\) to be \(2t\) times the largest odd integer at most \(\lfloor n^{a/4}\rfloor/(2t)\) for sufficiently large \(n\), so \(\gamma=a/4\) works.
For \(1\le i\le K\) use one of the disjoint successful paths \(D M_i\).
Choose its initial visible vector to have all thirteen entries \(j\), with \(j=1,3,\ldots,4t-1\) used equally often.
The final visible vector then has all entries \(j+1\), and its true group label is the initial one.
Guards on \(M_i\) can be chosen to avoid cancellation after \(D\).
In each visible position the \(4t\) values \(1,\ldots,4t\) occur an odd number of times on this endpoint set, and zero does not occur.
A pair staying within one value removes even multiplicity in that bin.
Hence in any perfect matching of this set at least \(2t\) pairs have endpoints differing at the position, forcing a certificate term there for each such pair.

For the central test keep only the two homology summands at coarse deck index \(3\), further quotienting each by the class of \(L_T\) on that side.
Under the simultaneous axis prescription just proved, all conjugated lamp-loop terms in \(D\) are killed.
The stored based displacement of \(D M_i\) therefore has exactly the central tensor \(T_i\) in these quotients.
The start of \(M_i\) still has coarse color \(3\), and its two graph cycle bases have color zero.
The neutral cycle classes stay independent modulo the lamp cycles on both sides by the disjoint source edges.
Thus the stored sum over the \(K\) pairs has rank \(K\).
For any alternate matching with arbitrary original-presentation certificates, let \(E,J\) be the spans of the homology vectors of its terms at \((A,3),(B,3)\) respectively, reduced modulo the two indicated lamp-cycle classes.
All other positions have already been dropped.
Applying (2) gives \(\dim E+\dim J\ge K\), so at least \(K\) term occurrences are needed in those two positions combined.
The other eleven positions each require at least \(2t\) further term occurrences by the odd-bin argument.
This proves the claimed \(K+22t\) bound for the actually saturated subset.
The words \(D\) and \(D M_i\) have identical actions on the fine states and give different displacements in the displayed central quotient, so a crossing's lamp increment alone does not determine its central value.

## Assessment history

### Decision thirteen-position-bridges

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:03 |
| status | proved |
| reason | Independent review verified the correct deck indices for the lamp changes, the common bridges and the lower bounds for unrestricted certificates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | True equal-label bridges across all visible coordinates, and simultaneous position and rank bounds on the designated marked set. |
| argument | [Proof](#a-closed-graph-loop-changing-a-single-lamp) | One-lamp cycles, simultaneous reads, central correction on full deck summands and the combined bounds under the stated law. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0108_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-thirteen-position-bridges)
