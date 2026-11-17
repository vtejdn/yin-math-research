---
author: Yin
---

# Distinguishing the three even colors of the four-line construction in a finite quotient

Keep the inverse pairing, letter increments to \(C_7\), and the exact integer histograms of every type in the [four-line construction](../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).
Write \(D=\{0,1,2,4\}\) in forward coordinates on both sides.
The three other colors \(3,5,6\) have even counts, and the inverse-label second factor has the reflected colors.
There are legitimate torsion-free realizations with these precise coarse data in which a finite quotient certifies a surviving group label in **each** of the three even colors on both sides.
Over the coarse quotient the finer quotient has kernel \(C_2^2\).
A single additional \(C_2\) can certify color 3 on the first side, but cannot certify all three first-side colors by odd refined counts.
The latter limitation holds for every connected matching with the specified parity patterns.
Allowing a kernel of odd order gives an example of order \(21\), the least possible order of any finite quotient over \(C_7\) that certifies all three first-side even colors by odd refined counts.

## Exact refinement with two binary coordinates

Let \(V_0=\{0,e_1,e_2,e_1+e_2\}\) be a two-dimensional binary vector space and \(P=C_7\times V_0\).
Take \(n\) through sufficiently large multiples of \(56v^2\), with \(v=16513\).
Split each full type uniformly into the 28 classes before the following bounded integral changes.
This is possible since all source counts are integral at \(n=2v^2\), and \(n/28\) is even.
Use the four selected lines indexed by \(i\in D\) in C_A0051, and write \(f_i(c)=7\mathbf 1_{\{c=i\}}-1\).
On the empty-extra type of line \(i\), on each side, add the counts in this table at fine color \((c,s)\).

| Binary coordinate \(s\) | Change at \((c,s)\) |
| --- | --- |
| \(0\) | \(f_i(c)-\mathbf 1_{\{c=i+1\}}-\mathbf 1_{\{c=i+2\}}\) |
| \(e_1\) | \(\mathbf 1_{\{c=i+1\}}\) |
| \(e_2\) | \(\mathbf 1_{\{c=i+2\}}\) |
| \(e_1+e_2\) | \(0\) |

All other counts are unchanged.
The sum over \(s\) of these four changes is exactly \(f_i(c)\), recovering the prescribed counts of every coarse type and the same \(n\), and their sum over \(c,s\) is zero.
Every fine type still has positive count for large \(n\).
The change in each fixed binary coordinate is a function of \(c-i\).
Give each of the three special intersection arrows its original increment in the first coordinate and zero in the second.
At every other ordinary–ordinary pair give zero increment in both coordinates.
Private pairs on one selected line have identical changes, and at an intersection arrow the two new line indices are the two old ones translated by its increment.
Thus the stub histograms in each binary coordinate match exactly across these arrows.
On two of the three mixed extra–ordinary pairs assign increments \((0,e_1)\) and \((0,e_2)\) in one orientation, with their negatives in reverse.
The last mixed pair has zero increment.
The ordinary partners of the extras are exterior to all four selected lines, and no changed type carries any extra.
Both ends of a mixed pair consequently have the original uniform fine stub counts, even when its increment changes the binary coordinate.
These increments generate \(P\).
Choosing independent bijections in the resulting equally sized fine blocks gives actual source matchings.
Right translation of the fine color follows the label increments, so coning all components leaves a surjection \(G_n\to P\) inducing the original coarse character.

Choose both roots at \((0,0)\).
For connected sides all vertices are occurrences.
In the \(e_1\) coordinate the parity indicator in forward colors is \(D+1=\{1,2,3,5\}\), and in the \(e_2\) coordinate it is \(D+2=\{2,3,4,6\}\).
Indeed the uniform part contributes \(n/28\) at every fine class and the four indicated point increments add their respective translated indicators.
Thus \(3,5\) have an odd refined count at \(e_1\), and \(3,6\) at \(e_2\).
The same holds on the second side with the first coordinates negated when reading its inverse labels.
A group label and all its repetitions have the same image in \(P\), so parity is unchanged by collection in each fine class.
This proves survival in all six specified coarse classes from the finite quotient alone, including on any exceptional matching in this connected fine-colored family.

If \(\mathcal K=\ker(G_n\to C_7)\), the quotient map takes \(\mathcal K\) onto \(V_0\).
It kills \([\mathcal K,\mathcal K]\mathcal K^2\), so the canonical relative mod-two quotient of [C_A0047](../claims/Yin_C_A0047_v1.md#a-finite-test-for-complete-erasure-of-a-color) distinguishes at least the fine classes used here.
Projecting \(V_0\) further onto the coefficient of \(e_1\) gives a \(C_{14}\) quotient already certifying the two first-side colors \(3,5\): the binary-one class is the union of the \(e_1\) and \(e_1+e_2\) classes, and the latter contributes an even count everywhere.

## Matching safeguards and the relative mod-two quotient

The fine ensemble is a bounded perturbation of the [balanced \(P\)-matching model](../claims/Yin_C_A0044_v1.md#matching-within-the-prescribed-color-classes).
In this application the number of classes is \(28\), the marginal letter frequency is \(\rho=129/v\), and each matching block has size \(N+O(1)\), where \(N=n\rho/28\).
For completeness, choose the fixed logarithmic girth constant small enough that \(c_0\log(56|T|/\rho)<1\) and \(2c_0\log132<1\).
The short-cycle and switching arguments use only these block sizes, the degree bound, and reversibility of a switch within one block.
They give girth-event probability at least \(\exp(-o(n))\) and conditional cost \(N^{-E}\exp(o(L))\) for \(E=O(L)\) prescriptions, with \(L=\lfloor c_0\log n\rfloor\).
The same bounds for \(O(k)\) prescriptions at \(k\le\varepsilon n\), with \(k\) small enough relative to \(N\), give small-set expansion and diameter \(O(L)\) as in [C_A0051's switch and expansion calculation](../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts).

For a prescribed occurrence of a turn, its count within a fine color differs by \(O(1)\) from the balanced count.
Existing positive type frequencies bound every positive turn count below by a constant times \(n\), while impossible turns remain impossible because no new type is introduced.
Thus vertex assignments in a bounded stage differ in their upper bound by a factor \((1+O(1/n))^{O(L)}\) from the balanced calculation.
Choosing one fine color per connected stage component and propagating it along the assigned words gives the factor \(28^{b_j+E_j-V_j+k_j}\), bounded independently of \(n\) by the same whole-chain count as in [C_A0044](../claims/Yin_C_A0044_v1.md#girth-conditioning-and-bounded-patterns).
This preserves the bounded-pattern estimate, including with either prescribed root.
The diameter event and the source's deterministic arrangement and cone-picture reductions give asphericity, torsion-freeness, root separation and the nonzero characteristic-two zero product with probability tending to one after girth conditioning.
For macroscopic cuts the type and block proportions tend to their balanced positive values.
Any loss of the strict entropy gap on cuts of density bounded away from zero and one would give a limiting balanced zero-loss marking constant at every fine color.
Compatibility and generation of \(P\) force the same mark across all colors, a contradiction.
Together with small-set expansion this proves connectedness with probability tending to one.
Intersecting these events furnishes the asserted torsion-free realizations. [Ope26f, Proposition 4.5 and §§5–6](../literature/pdf/Ope26f.pdf#page=18)

The same compactness argument applies to the [finite-target test](../claims/Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient).
For any fixed finite \(Q\) and fixed assignment \(\theta:F\to Q\) not factoring through the chosen map to \(P\), a limiting balanced zero-loss marking would give \(g(z+\eta(t))=g(z)\theta(t)\) for every fine \(P\)-color \(z\) and signed letter \(t\).
Here \(\eta:F\to P\) denotes the fine increment map.
Propagation in the right regular action gives the prohibited factorization.
The polynomial histogram count and subexponential girth cost therefore exclude all such maps with exponentially high conditional probability, for any preassigned finite list of targets.

Indeed, typically \(\mathcal K/([\mathcal K,\mathcal K]\mathcal K^2)\) has **exactly** dimension two and trivial \(C_7\) action in this fine law.
It is finite-dimensional since \(\mathcal K\) is an index-seven subgroup of a finitely generated group.
It surjects equivariantly onto the two-dimensional trivial module \(V_0\).
If its dimension is larger, semisimplicity in characteristic two for \(C_7\) gives either a three-dimensional trivial quotient or a nontrivial irreducible cubic quotient with additive group \(\mathbb F_8\).
The irreducibles come from the linear and the two cubic factors of \(X^7-1\) over \(\mathbb F_2\).
Quotienting the relative extension by the kernel of the corresponding module map gives an extension of \(C_7\) by this elementary abelian group.
It splits because the eighth power of any lift of a generator is a lift of the same generator of order seven.
Thus \(G_n\) would surject onto either \(C_7\times C_2^3\) or \(\operatorname{AGL}(1,8)\), both of order \(56\).
Apply the finite-target test to these two fixed groups: a surjection onto either cannot factor through \(P\) of order \(28\).
This proves the typical dimension assertion.
In the original C_A0051 law, the limiting balanced group for the same finite-target test is \(C_7\).
Even a nonfactoring map to \(C_{14}\) has exponentially small conditional probability there.
The refined law selects legitimate but exceptional tuples from the space admitting the original four-line blocks.

## Why one additional binary bit cannot certify all three first-side colors

Consider any connected source matching with the four-line coarse parity masks and any further quotient over \(C_7\) with kernel of order two.
This extension is \(C_{14}\): its kernel has trivial automorphism group, and the eighth power of a generator lift supplies a splitting.
Identify it with \(C_7\times C_2\), keeping the prescribed orientation of \(C_7\).
On side \(A\), the number of vertices with binary coordinate one is even.
To see this, for every signed letter count its stubs at vertices on that sheet.
For the two letters of an inverse pair the counts are either equal or complementary in the total \(n\rho\) under the bijection, according as the binary increment is zero or one.
The total \(n\rho\) is even at source-admissible sizes, so the two stub counts always have equal parity.
Summing over all inverse pairs gives an even number, whereas summing at the binary-one vertices counts their degrees \(129\) or \(131\), both odd.
This argument uses the first side's prescribed types and does not assume a random matching.

Write \(R=\mathbb F_2[C_7]\), use \(D,D^*\) also for the indicator sums of \(D,-D\), and let \(\varepsilon=s-1\) for the order-two generator.
The refined group algebra is \(R[\varepsilon]/(\varepsilon^2)\).
The two projected factors are \(D+\varepsilon a\), \(D^*+\varepsilon b\), where \(a,b\in R\) are the binary-one sheet indicators after collecting modulo two.
The source zero product in the refined group algebra gives \(aD^*+Db=0\).
The elements \(D,D^*\) are the two different cubic idempotents in \(R=\mathbb F_2\times\mathbb F_8\times\mathbb F_8\), as also seen by evaluating \(1+X+X^2+X^4\) on the two cubic orbits and at one. [C_A0042, cubic factors](../claims/Yin_C_A0042_v1.md#separating-the-cubic-factors)
The two summands lie in disjoint cubic ideals, so \(aD^*=0\).
The sheet-count argument gives \(a(1)=0\) too.
Hence \(a\in RD\).
This ideal has eight elements, and its seven nonzero elements are exactly the seven translates of \(D\): they are distinct since translation by a generator cannot stabilize a set of four elements in \(C_7\).
At any coarse color outside \(D\) the two binary sheets have identical parities, both equal to the value of \(a\) there.
Every nonidentity translate of \(D\) contains exactly two points outside \(D\), since its intersection with \(D\) has size two.
It follows that a single binary refinement certifies either zero or two of the three first-side even colors by odd subcounts, never all three.
The explicit \(C_{14}\) quotient above attains two, and the \(C_2^2\) kernel attains three.
This minimality concerns certification by odd bins on side \(A\).
Failure of that certificate does not imply erasure of any original group label.

## A smaller quotient of odd order, even when the relative mod-two test is trivial

Use \(P'=C_7\times C_3\cong C_{21}\) and take \(n\) through sufficiently large multiples of \(42v^2\).
In the table use just the first three rows, with binary coordinates \(0,e_1,e_2\) replaced by \(0,1,2\in C_3\).
The deleted fourth row had identically zero change.
The new uniform base is integral and each fine class originally has \(n/21\) vertices on a side, an even number.
One mixed inverse pair with increment \((0,1)\) suffices to generate the new kernel, and the other two can have zero increment.
No changed type touches these mixed pairs.
All ordinary–ordinary increments still have zero second coordinate, so their stub equalities hold in each of the three coordinates just as before.
The changes sum to the exact prescribed \(f_i\).
The two nonidentity coordinates have the same odd masks \(D+1,D+2\), so the quotient again certifies all three even colors on both connected sides, with the inverse convention on the second factor.
All fine growth and matching estimates previously used apply with 21 in place of 28, taking \(N=n\rho/21\) and \(c_0\log(42|T|/\rho)<1\).
Thus actual torsion-free examples with root separation and the characteristic-two zero product exist here too.

Every finite group surjecting onto \(C_7\) has order a multiple of seven.
A quotient of order seven gives only the original coarse counts.
A group of order fourteen surjecting onto \(C_7\) has normal subgroup of order two, so the preceding single-bit bound applies.
Therefore no smaller finite group over \(C_7\) can provide odd refined counts in all three first-side even classes simultaneously.

In this odd-order planted ensemble the canonical relative mod-two quotient typically gives **no** refinement over \(C_7\).
If \(\mathcal K/([\mathcal K,\mathcal K]\mathcal K^2)\) were nonzero, a simple \(C_7\)-module quotient would give a surjection onto \(C_{14}\) or \(\operatorname{AGL}(1,8)\) by the split-extension argument above.
Neither of these even-order groups is a quotient of \(P'\).
Applying the perturbed finite-target entropy estimate to those two targets therefore excludes the event with exponentially high probability under girth conditioning.
A nontrivial finite \(2\)-group quotient of \(\mathcal K\) would have a further quotient of order two, so it is excluded on the same event.
The \(C_{21}\) odd-bin certificates and this failure of every relative \(2\)-group refinement thus hold together on torsion-free realizations of the same coarse data.
