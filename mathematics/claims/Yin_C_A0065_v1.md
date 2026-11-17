---
author: Yin
---

# Which translates must occur in proofs for a single color

## Statement

Fix \(k\ge1\) and the [four-line inverse pairing and coarse \(C_7\) populations](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).
There are connected, root-separated, aspherical matching realizations with those exact coarse counts, their torsion-free original cone group \(G\), and their nonzero characteristic-two zero product, having the following properties.
Both prescribed roots have coarse color zero, and colors on either side are taken from forward root paths before inverting the second factor.

Fix one side \(Y\), one forward color \(c\in\{3,5,6\}\), and any partial matching of its vertices.
For each matched pair assume a path between its endpoints has a proof of triviality in the **original** cone presentation.
Write that proof as an ordinary product of conjugates of based graph-loop words or their inverses in the free rose group.
A term has a side and a coarse deck index \(q\in C_7\) as defined below.
Let \(u\) be the number of unmatched vertices in the color.
For a side/index \((T,q)\), write \(N_{T,q}\) for the number of matched pairs whose supplied proof contains a term at that side and index.
Set \(h_3=4k\) and \(h_5=h_6=2k\).
Then
\[
                      u+2N_{T,q}\ \ge\ h_c                                \tag{1}
\]
holds separately for **all seven** indices on the opposite side and **all six nonzero** indices on side \(Y\).
It holds for every choice of the pair paths, proofs, number of terms and loop bases.
For a complete matching, color 3 would require at least \(2k\) different pairs using each of those thirteen side/index choices and at least \(26k\) relator occurrences in total.
For either other color the corresponding bounds are \(k\) and \(13k\).
Relators occurring in different proofs are counted at their occurrences; the number of different words or basepoints can be smaller.
For example, avoiding a single one of the thirteen choices leaves at least \(4k\) unmatched vertices in color 3, even if all the other choices are available without restriction.

In the same realizations \(\ker(G\to C_7)\) is perfect.
No quotient over this \(C_7\) with nontrivial solvable kernel, including an order-21 quotient, is available.
The inequalities arise from explicit finite permutation data for the two graphs.
Those permutations need not define an action of \(G\).
The existence of a complete erasure in an exceptional safeguarded four-line tuple remains open.

## Two actions with different point stabilizers

Put \(m=4k+1\), \(V=\mathbb Z/m\mathbb Z\), \(D=\{0,1,2,4\}\), and \(v=16513\).
Use the finite group
\[
 W=(V^{C_7}\oplus V^{C_7})\rtimes C_7,\qquad
 (\ell,c)(\ell',c')=(\ell+S_c\ell',c+c'),\qquad
 (S_c f)(j)=f(j-c).
\]
The two copies of \(V^{C_7}\) are indexed by the side names \(A,B\).
Let \(H_A\) be the subgroup of the first copy supported only at zero and \(H_B\) the subgroup of the second copy supported only there.
Both have order \(m\).
Give the first graph the right action on \(\Omega_A=H_A\backslash W\), and the second the right action on \(\Omega_B=H_B\backslash W\).
Use \(H_A,H_B\) as root states.
Each set has \(d=7m^{13}\) states.
At a fixed coarse color \(c\), a state on side \(Y\) specifies the values of all fourteen coordinates of \(\ell\) except the \(Y\)-coordinate at zero: precisely this value can be changed by left multiplication by \(H_Y\).

Write \(r=(0,1)\) for the rotation.
Use \(r,r^2,r^4\) on the three oriented intersection arrows of C_A0051.
On two different mixed extra–ordinary pairs use a unit point mass at slot zero of the first and second copies of \(V^{C_7}\), respectively, with inverse increments on the reverse letters.
Use the identity on all remaining pairs.
Conjugating the two point masses by rotations supplies both copies at every slot, so the letter map \(\theta:F\to W\) is onto from the free rose group \(F\).
Its projection to \(C_7\) is the original prescribed increment map.

## Exact type counts and the thirteen coordinate histograms

Take \(n\) through sufficiently large multiples of \(2dv^2\).
Start with an equal allocation of every original type among the \(d\) states on its side.
The number of vertices at each state on a side is then the even integer \(n/d\).
On side \(Y\) distinguish the states of coarse color \(c\) represented by \((\ell,c)\) where every entry in **both** functions of \(\ell\) is the same \(j\in V\).
Different \(j\)'s give different states, as thirteen coordinates are still visible.
Partition the \(m-1\) nonzero \(j\)'s into two sets \(J_1,J_2\) of cardinality \(2k\).
For each selected line \(i\in D\), change only counts of its empty-extra type on both sides.
In a distinguished state with \(j\in J_1\) add \(\mathbf1_{\{c=i+1\}}\), and in one with \(j\in J_2\) add \(\mathbf1_{\{c=i+2\}}\).
In the distinguished zero state add
\[
          7\mathbf1_{\{c=i\}}-1-2k\mathbf1_{\{c=i+1\}}-2k\mathbf1_{\{c=i+2\}} .
\]
All other entries are unchanged.
Summing the changes over states above \(c\) recovers the prescribed \(7\mathbf1_{\{c=i\}}-1\), and summing over all states preserves the original type total.
These perturbations are bounded independently of \(n\) for fixed \(k\), and all counts are positive for large \(n\).

Right multiplication by the active rotation shifts the coarse color and leaves every lamp entry fixed.
Thus every fine-state population on an intersection pair matches its prescribed opposite population exactly because the two line indices shift by the same increment.
Private pairs have identical changes on one line, and the mixed pairs touch neither a changed ordinary point nor a changed extra-bearing type.
Their right actions therefore match the uniform populations exactly, even though they add a lamp value at a color-dependent slot.
All the prescribed blocks can be matched by actual bijections.
Choose the roots in the designated zero states.
The common coarse actions factor through the regular \(C_7\) action, so coning every component leaves a surjection \(\eta:G\to C_7\).

Consider any one of the thirteen visible coordinate positions on one side and restrict the vertices to a single coarse color \(c\).
Before perturbation each possible coordinate value occurs an even number of times, as the count is a sum of the even state totals.
The nonzero value \(j\) now has odd count exactly when \(c\in D+1\) for \(j\in J_1\), or \(c\in D+2\) for \(j\in J_2\).
This calculation is valid for every visible position, because in every changed state all these coordinates equal \(j\).
At \(c=3\) all \(4k\) nonzero coordinate values are odd.
At \(c=5\) precisely the \(2k\) values in \(J_1\) are odd, and at \(c=6\) precisely those in \(J_2\) are odd.
The zero value has even count in all three colors, by the even coarse total.
This calculation uses actual prescribed vertex populations and does not identify these states with original group labels.

## Counting the relator terms of an arbitrary certificate

If a loop \(R\) is read at vertex \(z\) of side \(T\), write \(w_z\) for a forward root word to that vertex on its side.
The permutation \(\theta(w_z R w_z^{-1})\) fixes the designated root state and therefore belongs to \(H_T\).
This statement only uses readability of the loop.
Now let \(P\) be any path from \(x\) to \(y\) on side \(Y\), with both vertices in the chosen coarse color.
Suppose the rose word of \(P\) has a certificate
\[
   W(P)=\prod_i a_i R_i^{\pm1}a_i^{-1}\quad\text{in } F.
\]
In the term for the loop based at \(z_i\) on side \(T_i\), the conjugator from its based representative \(w_{z_i}R_iw_{z_i}^{-1}\) is \(w_xa_iw_{z_i}^{-1}\) after conjugating the whole certificate by \(w_x\).
Its coarse increment
\[
                        q_i=\eta(\pi(w_xa_iw_{z_i}^{-1})),\qquad \pi:F\to G ,
\]
is the stated deck index.
The conjugator's lamp part acts trivially on the abelian base of \(W\) by conjugation.
Its rotation shifts the single allowed slot to \(q_i\), so that term can change only the coordinate \((T_i,q_i)\).
This remains true with the inverse reading and for arbitrary conjugating words.

Choose any forward root words \(w_x,w_y\), with images \(\theta(w_x)=(\ell_x,c),\theta(w_y)=(\ell_y,c)\).
Since \(w_x P\) and \(w_y\) terminate at the same vertex, they give the same \(H_Y\)-coset.
Consequently \(\theta(w_xW(P)w_x^{-1})\) equals \(\theta(w_y w_x^{-1})=(\ell_y-\ell_x,0)\) up to left multiplication by \(H_Y\).
The discrepancy changes none of the thirteen visible coordinates.
If the endpoints differ at one visible position, at least one certificate term of precisely its side and index is unavoidable.

In a partial matching, pairs whose ends agree at a given position remove an even number from a single value bin.
Each other pair affects at most two odd bins, and each unmatched vertex can account for at most one.
Thus \(h_c\le u+2N_{T,q}\) for every visible position, proving (1).
Summing the number of forced terms for a complete matching over the thirteen distinct positions proves the relator-occurrence bounds.
The contributing pairs for different positions can overlap.
As the construction works for arbitrary fixed \(k\), the necessary number of terms can diverge along a diagonal sequence with \(n\) sufficiently large at each \(k\).
It gives no uniform positive fraction of all vertices on such a sequence.

## Safeguarded realizations

Take independent uniform bijections in the compatible blocks on the two sides.
Both actions are transitive permutation actions of fixed size for each fixed \(k\).
The [side-specific pattern comparison](Yin_C_A0060_v1.md#geometric-safeguards-and-the-absence-of-group-quotient-certificates) and the [bounded-perturbation estimates](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) apply here.
Indeed each stub pool has size \(N+O(1)\), \(N=n(129/v)/d\), and any positive specified turn pool differs by \(O(1)\) from the corresponding balanced-state count.
Impossible turns are still impossible.
Choose \(c_0>0\) with \(c_0\log(2d|T|/(129/v))<1\) and \(2c_0\log132<1\), and set \(L=\lfloor c_0\log n\rfloor\), where \(|T|\) is the number of signed rose letters.
The block switches and small-set expansion bounds give girth probability at least \(\exp(-o(n))\) before conditioning and diameter \(O(L)\) with probability tending to one after conditioning.
Each permitted bounded stage gains at most a factor \(d^{b+E-V'+j}\exp(o(L))\) from the states, where \(E,V',b,j\) count edges, vertices, components and prescribed initial images.
The power is bounded by the source's whole-chain count, since each signed word propagates the initial state deterministically in any permutation action.
This preserves its exclusion of the necessary bounded patterns and hence its deterministic arrangement and cone-picture arguments.
For macroscopic cuts the limiting balanced count has negative entropy exponent whenever there is no state section with the indicated cut density.
At zero loss each state has a constant marking across types and is preserved along the generating increments, and transitivity makes such an invariant cut constant everywhere.
Small-set expansion and this macroscopic cut estimate give connectedness of both sides.
Intersecting the events proves torsion-freeness, root separation, asphericity and the original nonzero zero product over \(\mathbb F_2\) with conditional probability tending to one. [Ope26f, §§3–6](../literature/pdf/Ope26f.pdf#page=7)

## Why the coarse kernel may also be perfect

Write \(N_0=\ker(F\to C_7)\), \(K=\ker(G\to C_7)\), and \(S_Y=\theta^{-1}(H_Y)\subset N_0\).
Each \(S_Y\) is normal in \(N_0\) since \(\theta(N_0)\) is the abelian base of \(W\).
Let \(s\in F\) lift \(r\in W\).
All the subgroups \(s^q S_Y s^{-q}\) for \(q=0,\ldots,6\) and \(Y=A,B\) together generate \(N_0\).
Indeed each contains \(\ker\theta\), and their images generate every coordinate in the base of \(W\).

An index-\(j>1\) subgroup of \(K\) gives a transitive coset action of \(N_0\) on \(j\) points that factors through \(K\).
Regard it as edge transports on the connected coarse rose cover with \(j\) marks over every coarse color, using a fixed tree there as in the [small-index proof](Yin_C_A0061_v1.md#vertex-markings-from-small-index-subgroups).
For each side and offset \(q\), use the transport on the cover above \(c+q\) when reading a graph letter at coarse color \(c\).
An additional compatible marking of the actual graph exists for every offset: every closed graph walk is a cone relation, and its conjugate based at the identity after lifting from any coarse color acts trivially in \(K\).

At least one of these fourteen transport tests has **no** section depending only on the fine state.
Otherwise, for each \(Y,q\), the mark chosen at \(H_Y\) over coarse color \(q\) is fixed by all of \(S_Y\), the words that fix this fine state.
Transport the marked point back to the identity fiber using the path \(s^q\) from zero to \(q\).
The group \(s^q S_Ys^{-q}\) then fixes that point of the transitive \(N_0\)-action.
It is normal in \(N_0\), so it fixes every point.
If all these tests had sections, their generated group \(N_0\) would act trivially, contradicting \(j>1\).
This uses all the offsets at the coarse cover; merely intersecting two stabilizers would not give the assertion for a nonnormal subgroup of \(K\).

We give the probability counts to specify the uniformity needed here.
For the side and offset without a section, the balanced-incidence entropy bound of [C_A0061](Yin_C_A0061_v1.md#an-entropy-inequality-independent-of-the-marking-alphabet) gives \(A-B\le -(129/20-1)d^{-1}\sum_\omega H(m_\omega)+o(1)\) for its marked-type first moment.
Here \(m_\omega\) is the marking distribution in fine state \(\omega\), \(A\) is the type-color entropy, and \(B\) is half the sum of the signed matching-end entropies with their frequencies.
Its \(o(1)\) error remains uniform for \(j\le n\) under bounded type perturbations by the total-variation entropy estimate there.
For any chosen assignment of modal marks to fine states some block fails the relevant transport because no section exists.
At least \(N/2-O(1)\) vertices must therefore be nonmodal, giving a negative gap bounded away from zero for fixed \(k\), independently of \(j\).
The type histograms and all the permutations on the coarse-cover edges cost \(\exp(O(j\log n))\) in total, including the factorial approximation error.
The fourteen choices of side and shift cost only a constant.
For some \(\kappa>0\), summing over \(2\le j\le\kappa n/\log n\) and dividing by the subexponential girth cost gives exponentially small probability for any such subgroup of \(K\).

Finally the coarse rose cover has fixed rank \(1+7(8258-1)\).
On the diameter event, lifted fundamental graph loops of length \(O(\log n)\) present \(K_{\rm ab}\) on its non-tree edges after abelianization.
Excluding an index-two subgroup gives a full-rank integral minor odd modulo two.
The absolute determinant is at most \((C\log n)^{1+7(8258-1)}\) by Hadamard's inequality.
For large \(n\) this bounds the order of any possible abelianization below the excluded index threshold, so \(K_{\rm ab}=0\). [Integral determinant argument](Yin_C_A0061_v1.md#from-bounded-length-relators-to-perfection)
The small-index estimate and the geometric events hold simultaneously with conditional probability tending to one.
Every solvable image of the perfect \(K\) is trivial, giving the claimed absence of solvable-kernel extensions.
This is a property of the actual cone group, whereas the two finite coset actions constrain certificates without requiring the full cone group to act on either state set.

## Assessment history

### Decision both-sides-and-deck-indices

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:31 |
| status | proved |
| reason | Independent review verified the displacements, the thirteen histograms and the perfection argument for the actual coarse kernel. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The partial-matching inequalities for unrestricted relator certificates and the genuine four-line realizations for each fixed k. |
| argument | [Counting terms of arbitrary certificates](#counting-the-relator-terms-of-an-arbitrary-certificate) | The two state actions, exact perturbations, path identities, safeguarded matching law and the finite-index argument. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0101_v1.md#whole-argument-finding) | Independent review of the fixed argument and its stated applicability. |

## Current assessment

[Selected decision](#decision-both-sides-and-deck-indices)
