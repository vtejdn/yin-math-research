---
author: Yin
---
# A torsion-free matching construction with two nonzero seven-class parity patterns

## Statement

There is a choice of the inverse pairing allowed in [Ope26f, §2.1](../literature/pdf/Ope26f.pdf#page=4) and of color-preserving matchings for which the following assertions hold.
Write \(v=16513,\ k=129,\ p=k/v\) and take \(n\) through sufficiently large multiples of \(14v^2\).
The cone group has an actual quotient \(C_7=\mathbb Z/7\).
The graphs can be chosen connected, with all the source's prescribed type totals, its root-separation and asphericity conclusions, and its two nonzero factors with zero product over \(\mathbb F_2\) in a torsion-free group.

Take roots in color zero and put \(K=\{0,1,2,4\}\subset C_7\).
In the first factor the number of vertex occurrences over \(c\) is \(n/7+3\) for \(c\in K\) and \(n/7-4\) for \(c\notin K\).
The second factor, using inverse group labels, has the reflected histogram, with \(-K\) in place of \(K\).
The counts of occurrence pairs over the identity and each nonidentity quotient product are \(n^2/7+84\) and \(n^2/7-14\), respectively.
In particular neither factor projects to zero over \(\mathbb F_2\), and their projected product is zero.

In the modified random law below, with probability tending to one after logarithmic girth conditioning, all but \(o(n)\) vertices on each side have a group label of multiplicity one.
Every quotient class then contains \(n/7-o(n)\) or more distinct surviving group labels on each side, in the sense of a lower bound along a deterministic error of size \(o(n)\).
Their count in each class has the parity given by the exact occurrence histogram and is at most its occurrence count.
After collecting both sides, the number of support pairs above each quotient product is even and, divided by \(n^2\), converges in probability to \(1/7\).
Consequently all seven classes are occupied on the actual collected supports, with odd classes \(K,-K\).
For a connected realization with these occurrence counts to retain only its four odd classes after collection would require at least \(3n/7-12\) repeated vertices on that side.
If both sides have this erasure, more than \(66\%\) of all vertex pairs must lie in group-product fibers merging different simultaneous-step components for all sufficiently large \(n\) and girth at least three.
These conclusions realize the nonzero parity patterns and distinguish them from erasure of the other classes.
With probability tending to one the actual supports in this modified law still have the [uniform positive-density product bound](Yin_C_A0050_v1.md#positive-density-for-the-actual-collected-supports) over every commutative ring with \(1\ne-1\), for all unit coefficients on those supports.

## Four lines and the exact color matchings

Choose four distinct projective lines with no three concurrent in the plane of order 128, and index them by \(i\in K\).
For example the three coordinate lines and \(X+Y+Z=0\) have this property.
There are six distinct intersection points, and each selected line has \(129-3=126\) points on no other selected line.
Thus \(v-6-4\cdot126\) ordinary points lie outside the four lines.
Take three of these exterior points as the ordinary partners of the three extras, and give each mixed inverse pair color increment zero.
Pair the remaining exterior points amongst themselves and pair the 126 private points within each selected line, also at zero increment.
Both pairings are possible by evenness.

Label each intersection point by the unordered pair of its line indices.
The following arrows give the last three inverse pairs and the increments in the indicated direction:
\[
 \{0,1\}\longrightarrow\{1,2\}\quad(+1),\qquad
 \{0,2\}\longrightarrow\{2,4\}\quad(+2),\qquad
 \{0,4\}\longrightarrow\{1,4\}\quad(+4).
\]
In each arrow the second pair is the translate of the first by its increment in \(C_7\).
Take the negative increments in the reverse directions, defining a surjection \(\eta:F\to C_7\) from the rose group.

On both sides start by dividing each full prescribed type equally among the seven colors, as in the [balanced planted model](../ledger/Yin_L_A0047_v1.md#a-different-choice-of-matchings).
Integrality follows from \(14v^2\mid n\).
For each selected line \(i\), change the color histogram of its empty-extra type, on both sides, by the vector
\[
                             f_i(c)=7\mathbf1_{\{c=i\}}-1 .
\]
All other refined counts are unchanged.
Each modified full type retains its exact uncolored count since \(\sum_c f_i(c)=0\), and every refined type remains positive for sufficiently large \(n\).
The change of the color histogram of an outgoing letter is zero on the exterior points and extras, \(f_i\) at a private point on line \(i\), and \(f_i+f_j\) at the intersection of \(i,j\).
Consequently, if \(N_{t,c}\) counts the vertices carrying \(t\) in color \(c\) on one side, then exactly
\[
                              N_{t,c}=N_{\bar t,c+\eta(t)}.             \tag{1}
\]
At an intersection arrow this uses \(f_{i+d}(c+d)=f_i(c)\) for its two summands.
It also holds on the second side, since only the empty-extra types were changed.
Independently choose uniform bijections within these matched color blocks for each side and each inverse pair.
They give actual matchings with all the source's assigned labels.
Every closed walk has total increment zero, so coning every component of both graphs leaves the surjection \(\eta\) to \(C_7\).

Put \(a=n/7\).
Summing the four changes gives the forward count \(a-4+7\mathbf1_{\{c\in K\}}\) on each side.
On connected sides with roots of color zero this is the required path-label count before inversion.
For product color \(t\), the occurrence count is
\[
  \sum_{c\in C_7}(a-4+7\mathbf1_K(c))(a-4+7\mathbf1_K(c-t))
      =7a^2-112+49|K\cap(K+t)|.
\]
The six unordered pairs listed in the three arrows show that every nonzero difference occurs exactly twice as an ordered difference of \(K\).
Thus the intersection has size four for \(t=0\) and two otherwise, giving the two claimed numbers.
Since \(a\) is even, the projected parity indicators are precisely \(\mathbf1_K\) and \(\mathbf1_{-K}\).

## Geometric safeguards under the change of counts

Let \(N=np/7\).
Each matching block has size \(N+O(1)\), with a bound independent of \(n\), since the construction changes only four type histograms by bounded integers.
Fix \(L=\lfloor c_0\log n\rfloor\), where \(c_0\log(14|T|/p)<1\) and \(2c_0\log132<1\), as in the [balanced switching argument](../ledger/Yin_L_A0047_v1.md#girth-local-expansion-and-the-cost-of-a-matching-prescription).
For a short cycle of length \(j<L\), its distinct matching prescriptions cost at most \((N-O(1)-j)^{-j}\) before conditioning.
Together with the vertex and label counts of Ope26f, Lemma 2.2, this gives \(n^{\gamma+o(1)}\) expected edges on short cycles as an upper bound, with \(\gamma=c_0\log(14|T|/p)<1\).
Indeed the denominator for \(j<L\) is at least \(N/2\) for large \(n\), giving the same geometric series as in the balanced bound.
The source switch repairs a bad edge by transposing its match with a distant nonbad edge in the same block.
For tuples with at most \(n^{\gamma'}\) bad edges, \(\gamma<\gamma'<1\), the bad-edge and distance exclusions total \(o(n)\), while every block has order \(n\) available choices.
Markov's inequality and the reverse count of at most \(\sum_{j\le n^{\gamma'}}(Cn^2)^j=\exp(o(n))\) switch sequences give girth-event probability at least \(\exp(-o(n))\).
The product distribution on tuples is uniform here because the block sizes are fixed in advance.

Under girth conditioning the switching bound for a new pair, with \(s\) feasible prescriptions already fixed, is at most
\[
                   (N-O(1)-s-O(132^{2L+2}))^{-1}
\]
whenever the denominator is positive.
All switches stay within the assigned block, and the only additional loss relative to the balanced computation is its bounded change of size.
Iterating the bound on \(E=O(L)\) distinct prescriptions gives \(N^{-E}\exp(o(L))\).
For small-set expansion take \(j\le \rho n\) with fixed \(\rho>0\) sufficiently small that \(\lceil129j/2\rceil\le N/3\).
A failure of doubling gives that many edge prescriptions in at most \(2j\) vertices.
The conditioned bound \(2/N\) for each prescription together with the set and edge counts in the [small-set proof](../ledger/Yin_L_A0047_v1.md#girth-local-expansion-and-the-cost-of-a-matching-prescription) gives at most \([C(j/n)^{62.5}]^j\) at size \(j\).
Shrinking \(\rho\) and summing yields doubling throughout this range with probability \(1-o(1)\), and the same \(O(L)\) upper bound on component diameters by disjoint growing balls.

For the bounded rooted pattern estimate of [Ope26f, Proposition 3.1](../literature/pdf/Ope26f.pdf#page=7), fix the unlabelled pattern and word labels in one multiplicity stage.
The [balanced stage calculation](../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors) first propagates colors on each component, then bounds named vertex choices from the refined counts before imposing injectivity.
In a prescribed color an unrestricted marked vertex now has \(n/7+O(1)\) choices.
For any internal turn the permitted type count differs from its balanced value by \(O(1)\); a structurally absent turn still has zero choices.
A positive balanced count is at least a fixed positive multiple of \(n\) because the alphabet and full types are fixed.
Thus the uniform bounds \(n/7\) and \(Nw(t,u)\) used there acquire at most a factor \(1+C/n\) per unprescribed vertex, where \(w\) is the source turn bound.
A prescribed root still has at most one possible image.
There are \(O(L)\) stage vertices, giving an additional factor \(\exp(O(L/n))\).
With the preceding prescription cost, the balanced factor \(7^{b_j+E_j-V_j+k_j}\) relative to the uncolored stage estimate remains bounded up to \(\exp(o(L))\).
Here \(b_j,E_j,V_j,k_j\) denote the component, edge, vertex and prescribed-root counts of [that stage](../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors), with boundedly many whole chains.
In particular one continues to use the source's uncolored word weights in the upper bound, including their reversal symmetry and squared-word estimate.
The bounded number of stages, choice of a small numerical stage bound and union bound over the subexponential number of patterns preserve the \(o(1)\) bound of Proposition 3.1, uniformly in each fixed choice of designated roots.
The deterministic planar and cone-picture arguments on the diameter event therefore give absence of reduced spherical arrangements, root separation and a contractible universal cover with probability \(1-o(1)\) under girth conditioning.
The final common-degree argument uses exactly the original outgoing types and still gives the zero product over \(\mathbb F_2\). [Ope26f, Proposition 4.5 and §§5–6](../literature/pdf/Ope26f.pdf#page=18)

## Connectedness, collection and the erasure threshold

For macroscopic disconnected pieces use a second binary color marking a putative partition with no crossing edge.
At fixed marked refined histograms the usual multinomial and matching factorial count gives expected count at most \(\exp(n(A_n-B_n)+O(\log n))\).
Here \(A_n\) sums the marked entropies of the full type-and-color classes with their actual frequency weights, and \(B_n\) is half the sum of marked entropies at signed-label-and-color classes with their actual weights.
The latter formula uses the exact matching of the two endpoint histograms for a compatible cut.
The weights differ by \(O(1/n)\) from those in the [balanced cut estimate](../ledger/Yin_L_A0047_v1.md#connectedness-and-the-other-finite-quotients).
If the macroscopic cut bound were to lose its strict entropy gap, a subsequence of feasible marked distributions with smaller-side density in \([\rho,1/2]\) would converge to a feasible balanced distribution of the same density range with exponent at least zero.
In that limit concavity gives \(B\ge(129/2)A\), so every refined type and every signed-label class would be monochromatic.
Every two line types at a fixed planted color have a common ordinary point, making the marking depend only on that color.
The matching equations and the increment \(+1\) then make it constant across all colors, contrary to the cut density.
The polynomial number of histograms and subexponential cost of girth therefore exclude macroscopic cuts with probability \(1-o(1)\) under conditioning.
Small-set expansion excludes smaller components.
Both full side graphs are consequently connected with probability tending to one.

For any specified vertex the uniform rooted estimate gives probability \(o(1)\) of a trivial group label on a path to some different vertex of its component.
This is exactly the event it has the same group label as another vertex, independently of the reference root.
Summing probabilities and applying Markov's inequality as in the [singleton calculation](Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) gives \(o(n)\) repeated vertices in probability on each side.
One may choose a deterministic \(o(n)\) upper bound holding with probability \(1-o(1)\).
Thus each class contributes at least its occurrence count minus \(o(n)\) distinct surviving labels, and their count has the parity of the occurrence count by collecting multiplicities modulo two.
Selecting one occurrence for each surviving label embeds both actual supports back into the vertex lists, omitting only repeated vertices.
The resulting pair rectangle loses \(o(n^2)\) positions in probability.
At every quotient product its count lies between the corresponding exact precollection count minus \(o(n^2)\) and that precollection count, simultaneously over the seven products.
The difference is even at every product because each individual class count has retained its parity.
These statements hold simultaneously with the connectedness and source safeguards just proved.
They realize two nonzero, opposite Fourier parity masks with all quotient classes occupied even after collection.
The [cyclic lifting test](Yin_C_A0042_v1.md#statement) therefore permits an exact characteristic-zero lift of the projected equations on these supports.

In any connected tuple with these histograms, complete erasure of the three classes outside a side's four odd colors would require every one of their \(3(n/7-4)\) occurrences to be repeated.
This is an exact necessary count, incompatible with the high-probability bound above.
If it holds on both sides, put \(r=3(n/7-4)\).
At least \(n^2-(n-r)^2\) ordered pairs have a repeated coordinate, by counting the complementary rectangle.
By the [fixed degree count](Yin_C_A0047_v1.md#the-fixed-graph-walk), fewer than \(0.009n^2\) pair vertices lie outside isolated two-vertex simultaneous components when the sides are connected and the girth is at least three.
At an isolated component with a repeated first coordinate label, replace that occurrence by another of the same group label while keeping the second vertex fixed.
The product is unchanged, and the new pair is outside the two-vertex component, since a simultaneous edge changes both vertices.
The same holds for a repeated second coordinate label.
Thus at least \(n^2[1-(1-r/n)^2-0.009]\) occurrences lie in product fibers containing more than one simultaneous component.
The limiting lower fraction \(1-16/49-0.009\) exceeds \(0.66\).
No exceptional matching with this erasure is asserted to exist.

## Product fibers and complex coefficients in the four-line law

For the [two-root bounded-pattern estimate](Yin_C_A0049_v1.md#a-bounded-pattern-with-one-prescribed-interval-on-each-side), the same block and vertex bounds above hold when the two initially specified vertices lie on different sides.
Each prescribed vertex still has at most one possible image, the two root savings are distinct, and the bounded factor \(7^{b_j+E_j-V_j+k_j}\) allows \(k_1\le2\).
The bounded-type perturbation therefore changes its stage bounds by at most \(\exp(o(L))\), just as for one root, with the same squared-word upper bound.
The deterministic two-break disk argument and averaging in [the two-root proof](Yin_C_A0049_v1.md#statement) then give \(o(n^2)\) impure occurrences in probability.
Its support-set product cardinality limit also persists, since the full uncolored type counts give the same degree count and the singleton and purity estimates control the same \(o(n^2)\) losses.

For [stability under deletions](Yin_C_A0050_v1.md#a-uniform-gap-under-deletions) use the actual refined-type frequencies and the actual block sizes divided by \(n\) in the factorial and joint-table entropy estimate.
They differ by \(O(1/n)\) from the balanced weights on a fixed index set.
If no uniform negative exponent held for small positive defect at some nonzero binary assignment, a subsequence with defect tending to zero would converge to compatible balanced marginals and joint tables at a fixed nonzero assignment with exponent at least zero.
This contradicts the balanced strict gap, since the limiting color group is still \(C_7\).
The polynomial table count and subexponential girth cost give exponential stability to the deletion of some \(\varepsilon n\) edges.
The fixed type counts also preserve the lower degrees in the [deterministic removal argument](Yin_C_A0050_v1.md#actual-product-fibers-after-edge-removal).
Together with purity, this gives a constant \(c_*>0\) independent of \(n\) such that, with probability \(1-o(1)\), \(|\operatorname{supp}(ab)|\ge c_*n^2\) for every choice of unit coefficients on the two actual collected supports and every commutative ring with \(1\ne-1\).
Thus the exact lift on the quotient coexists in this family with failure of complex or ramified modulo-four lifting on the full group products.

## Assessment history

### Decision four-line-matching

| Field | Value |
| --- | --- |
| date | 2026-11-17T08:57 |
| status | proved |
| reason | The independent review verifies the exact integral matchings, geometric and probabilistic estimates, conditional erasure bound and implications for the two product tables. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual torsion-free realizations of both odd masks, true occupancy, a necessary erasure threshold and typical coefficient obstruction. |
| argument | [Proof](#four-lines-and-the-exact-color-matchings) | Full four-line construction and proof for the modified matching law. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0082_v1.md#whole-argument-finding) | Independent inspection of the complete proof and its applications of the source. |

## Current assessment

[Selected decision](#decision-four-line-matching)
