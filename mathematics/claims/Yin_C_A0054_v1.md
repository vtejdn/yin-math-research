---
author: Yin
---
# Simultaneous loop witnesses and finite quotients over the even colors

## Statement

Use the full [four-line type and color counts](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings), with roots in color zero.
Write \(v=16513,\ k=129,\ p=k/v,\ D=\{0,1,2,4\}\) and use forward colors on both graphs before inverting the second factor.

1. In **every** connected such tuple of girth at least three, choose any set of at most 49 vertices on the second graph.
   Even using every closed walk based at the chosen vertices, and composing any individually readable synchronized paths they supply on the first graph, one cannot pair the entire first-side color \(3\) by this procedure.
   A positive fraction of that color has no first step in the resulting equivalence relation to any different vertex.
   This holds without a randomness or injectivity assumption.
2. Fix \(0<\delta<1\) and any finite list \(\mathcal S\) of finite simple groups containing \(C_2\).
   There are genuine torsion-free four-line realizations with an additional prescribed \(P=C_7\times C_2\) quotient, in which **all six** even coarse colors have even counts in all \(P\)-bins.
   On these tuples every finite quotient over the given \(C_7\) whose kernel has all its composition factors in \(\mathcal S\) factors through \(P\), regardless of its order.
   None of these quotients can certify an odd bin in the designated colors, including left color 3.
   In particular \(\mathcal S\) may include \(C_3\) and every prime cyclic group in any fixed finite list.
3. In the same realizations there are at least \(\lfloor n^{\delta/32}\rfloor\) mutually vertex-disjoint simple cycles on the opposite side.
   **Each** of their words yields at least \(\lfloor n^{1-\delta}\rfloor\) vertex-disjoint pairs in each fine bin over first-side colors \(3,5,6\), by reading actual open paths there.
   The open paths may be chosen vertex-disjoint across the different words as well.
   The closed cycles have independent classes in the homology of their graph and their cyclic words do not have conjugate nonzero powers in the free rose group.
   The analogous statements hold after interchanging the sides.
   The paired occurrences have equal group labels in the original cone group.

The probabilistic existence in items 2–3 uses a sufficiently small positive fixed girth constant depending on \(\delta\).
These properties hold with probability tending to one within the modified matching law below.
They select exceptional tuples from the space of the original four-line law, for which a nonfactoring map to \(C_{14}\) is exponentially unlikely by [the finite-target comparison](../ledger/Yin_L_A0053_v1.md#matching-safeguards-and-the-relative-mod-two-quotient).
In the modified law a proportion tending to one of the vertices are still singletons in their original group labels.
The failure of the indicated finite-quotient certificates and the many explicit loop witnesses therefore coexist with actual survival of the color.
Complete erasure in an exceptional legitimate realization remains unresolved.

## How many opposite-side base vertices are necessary?

On a fixed connected tuple let \(B_0\) be a set of \(s\) vertices on the second side.
Join \(x,x'\) on the first side when \((x,y)\) and \((x',y)\) lie in the same simultaneous-step component for some \(y\in B_0\).
This is precisely reachability by a synchronously readable second-side walk returning to its specified starting vertex \(y\).
Such a walk certifies \(g_x=g_{x'}\) in the original group.
Connected components of the resulting graph give the equalities obtained by using several such walks consecutively.
This definition requires the individual segments to be readable on both graphs.
Arbitrary consequences of the whole normal closure need not appear by these moves.

From the \(n/7-4\) left vertices of color 3, first set aside all with extras or with a line containing any of the three ordinary letters paired to extras.
The former number is \((3p/2)n/7\), since no type with extras was changed.
Each of the three ordinary letters occurs at \(pn/7\) left vertices of color 3 since it lies outside the four selected lines.
Thus at least \((1-9p/2)n/7-4\) vertices remain.
For any remaining \(x\) and \(y\in B_0\) with different lines, the two vertices have a unique common label \(t\), the ordinary point of intersection.
The inverse \(\bar t\) is ordinary.
Their simultaneous \(t\)-edge is a complete two-vertex component unless, at its other end \(x^t,y^t\), the lines agree or \(x^t\) has extras.
The latter exclusion is conservative since an extra intersection also requires extras on \(y^t\).

For each fixed \(y\), at most \(n/(7v)+6\) vertices were missed by requiring different initial lines.
For a fixed one of the at most \(k\) letters \(t\) in the line of \(y\), all potential \(x^t\) are in one coarse color carrying \(\bar t\).
At most \(n/(7v)+6\) of them have the line of \(y^t\), by the four-line counts.
The number carrying \(\bar t\) and any extras is \((3p^2/2)n/7\), because the extra-type counts on every line and at every color remain unchanged.
The map \(x\mapsto x^t\) is injective on its domain.
Putting \(u=(k+1)/v+3kp^2/2\), at least
\[
             (1-9p/2-su)\,\frac n7 -4-6s(k+1)                         \tag{1}
\]
of the left color-3 vertices therefore lie on an isolated simultaneous edge when paired with **each** \(y\in B_0\).
An isolated edge changes both coordinates, so for each starting \(y\in B_0\) the component of \((x,y)\) has no other pair with second coordinate \(y\).
It stays a singleton even after taking the transitive closure of all these moves.
For \(s=49\) the coefficient \(1-9p/2-49u\) exceeds \(0.00045\).
(1) is positive for the large admissible sizes under consideration.
The set \(B_0\) may be chosen after observing the entire matching tuple.
Unwitnessed pairs at these base vertices could still be equal by other group relations.

## A planted binary coordinate which does not certify any of the six colors

Take \(n\) through multiples of \(28v^2\), plant \(P=C_7\times C_2\), and start from uniform allocations of every full type to the fourteen fine colors.
The old source totals are integral already at \(2v^2\), so all these counts are integers and \(n/14\) is even.
For each of the four selected empty-extra line types \(i\in D\) add, on both sides, the following signed changes to the two fine counts over \(c\in C_7\):
\[
       \Delta_i(c,1)=\mathbf1_{\{c=i\}},\qquad
       \Delta_i(c,0)=f_i(c)-\mathbf1_{\{c=i\}},\qquad
       f_i(c)=7\mathbf1_{\{c=i\}}-1 .
\]
The sum restores exactly the four-line coarse type counts, and the total over all fine colors of each full type is unchanged.
All fine counts remain positive for sufficiently large \(n\).
Keep the four-line increments in the coarse coordinate.
Assign fine bit one in both orientations on one mixed extra–ordinary inverse pair and zero on all other pairs.
Each intersection arrow of the four lines pairs two translates of a two-element set and both fine-coordinate changes depend only on \(c-i\).
Its two matching-block populations are therefore equal.
Private ordinary points are paired on their own line, and the special ordinary partners of all extras lie outside every changed line.
Both ends of the fine-bit-one pair have uniform counts because no changed type carries an extra.
Thus all required block equalities hold over the integers and the increments generate \(P\).
Independent uniform bijections in the matched blocks give a surjection \(\pi:G\to P\) on the cone group, with the original coarse character \(\eta\).

Let \(u_0=n/14\).
The fine-bit-one histogram is \(u_0+\mathbf1_D\) and the fine-bit-zero histogram is \(u_0-4+6\mathbf1_D\), before inversion on side \(B\).
Thus the bit-zero sheet has even counts everywhere and the bit-one sheet has even counts outside \(D\).
For all six even factor colors, parity is zero in both fine bins, including after collection of actual labels.
The order-21 law of [the odd-bin construction](../ledger/Yin_L_A0053_v1.md#a-smaller-quotient-of-odd-order-even-when-the-relative-mod-two-test-is-trivial) has different refined counts.

This law is a bounded perturbation of the [balanced finite-target model](Yin_C_A0044_v1.md#matching-within-the-prescribed-color-classes).
The [geometric transfer for the four-line law](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) and its [bounded finite refinements](../ledger/Yin_L_A0053_v1.md#matching-safeguards-and-the-relative-mod-two-quotient) apply with 14 colors.
In detail, each nonempty matching pool is \(np/14+O(1)\), each prescribed positive turn-and-color count differs from its balanced value by \(O(1)\), and forbidden turns remain absent.
Switching stays within its block, the per-stage vertex count changes by at most \((1+O(1/n))^{O(L)}\) at logarithmic girth \(L\), and the number 14 is fixed in the bounded whole-chain color factor.
The small-set estimate and the limiting cut entropy give connectedness because in the limiting balanced distribution an invariant zero-loss cut is constant in each fine color, then constant on all of \(P\) because the increments generate \(P\).
The diameter and bounded-pattern estimates with fixed prescribed roots give the same deterministic arrangement exclusion, asphericity, torsion-freeness, root separation and genuine zero product over \(\mathbb F_2\) with probability \(1-o(1)\) under girth conditioning.
Uniformity in the prescribed roots also gives \(o(n)\) repeated vertices in probability, exactly as in [the singleton estimate](Yin_C_A0051_v1.md#connectedness-collection-and-the-erasure-threshold).
Thus in a typical connected tuple all fine bins actually contain \(u_0-o(n)\) or more distinct surviving labels, including every even fine bin in left color 3.

## Excluding all orders with prescribed simple composition factors

The same bounded perturbation preserves the finite-target estimate for each fixed target \(Q\).
For clarity, in the multinomial first moment the frequencies of fine types and fine label pools approach the positive balanced frequencies, and the normalized entropy exponent is continuous on the compact type-distribution space.
Any failure of the uniform negative exponent for a nonfactoring letter assignment would give in the balanced limit a marking depending only on the fine color and obeying \(f(z+\pi(t))=f(z)\theta(t)\) for every signed letter \(t\).
Propagation under right multiplication in \(Q\) would force \(\theta\) to factor, a contradiction. [Balanced finite-target argument](Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient)
The finite number of assignments, polynomial number of histograms and subexponential cost of girth then show that all maps from \(G\) to any preassigned finite list of finite groups factor through \(P\), with exponentially high conditional probability.

Put \(H=\ker\pi\).
If \(H\) surjects onto a fixed finite simple group \(S\), the kernel \(U\) of that surjection is normal in \(H\).
It has at most \(|P|\) conjugates under \(G\), and their intersection \(U_0\) is normal in \(G\).
The diagonal coset map embeds \(H/U_0\) into a product of at most \(|P|\) copies of \(S\).
Thus \(G/U_0\) is a quotient of order at most \(|P|\,|S|^{|P|}\) on which \(H\) acts nontrivially.
By applying the preceding finite-target estimate to all groups up to the largest of these finitely many order bounds, we exclude a surjection \(H\to S\) simultaneously for all \(S\in\mathcal S\).

For a finite quotient \(G\to E\) over \(C_7\), the image of \(H\) is normal in \(E\) and lies in \(\ker(E\to C_7)\).
If that kernel has its composition factors in \(\mathcal S\), so does the image of \(H\), by taking composition series through this normal subgroup.
A nontrivial finite image has a nontrivial finite simple quotient, which would contradict the preceding exclusion.
It follows that \(G\to E\) factors through \(P\), and hence its fine bins over a given coarse color are unions of bins in \(P\).
This proves the asserted invisibility of odd counts in all six even colors for the entire class of targets, with no upper bound on \(|E|\).
In particular it excludes a quotient of order 21 over the chosen \(C_7\) when \(C_3\in\mathcal S\), since such a quotient cannot factor through \(C_{14}\).
The same argument for any finite quotient of \(\ker\eta\) with these composition factors shows it factors through \((\ker\eta)/H=C_2\), without requiring that it extend to a quotient of \(G\).
The argument requires \(\mathcal S\) fixed before \(n\) grows.

## Many opposite cycles and simultaneous open lifts

Use the [fresh-stub construction](Yin_C_A0053_v1.md#finding-a-short-closed-word-on-one-side) with \(a=\delta/8,\ b=a/2,\ R=\lceil a\log n/\log64\rceil\).
In this fourteen-color law at least 120 ordinary stubs with ordinary inverse and zero increment in both coordinates occur at every vertex.
A usable-stub pool has size \(np/14+O(1)\), and a turn with two distinct usable stubs in its prescribed color has \(n/(14v)+O(1)\) candidates.
Within an \(O(n^{1-b})\) exposure budget the old-vertex probability is \(O(n^{-b})\), and the fresh probability for any required next turn is at least \(1/300\) for large \(n\).

Run all \(\lfloor n^{1-b-a}\rfloor\) cycle trials on side \(B\) at fine color zero under the unconditioned law.
Continue after successes, marking every touched vertex and beginning the next tree at an untouched one.
Each trial uses \(O(n^a)\) edge exposures, and its new 64-ary tree has \(\Theta(n^a)\) leaves if it finishes.
The conditional probability of a successful simple cycle of length at most \(2R+2\) is at least \(c n^{2a-1}\), uniformly in the preceding trials.
Indeed the internal abort bound is \(O(n^{a-37b})=o(1)\).
An internal tree hit already gives a cycle.
For a finished tree, the two-stub connector through a fresh middle vertex has probability \(\Omega(n^{2a-1})\), under this same budget, by the [leaf argument](Yin_C_A0053_v1.md#finding-a-short-closed-word-on-one-side).
Every counted cycle uses only current tree vertices and possibly its fresh connector.
Therefore different trials' selected cycles are vertex-disjoint.
Conditional binomial domination gives mean lower bound \(\Omega(n^{a-b})\), so, except with probability \(\exp(-\Omega(n^{a-b}))\), one may keep the first \(\lfloor n^{a/4}\rfloor\) cycles and their words.
They are simple and edge-disjoint, hence their classes in the integral first homology of this side graph are independent.
For safeguarded tuples even conjugate nonzero powers of their free words are impossible, since repeating the two cycles and adjusting their orientations and cyclic starting positions would give identical cyclically reduced words on disjoint underlying edges.
Pairing corresponding occurrences as opposite boundaries of an annulus gives the forbidden ordinary two-disk arrangement of [Ope26f, Definition 4.1 and Proposition 4.5](../literature/pdf/Ope26f.pdf#page=14).

Condition on the \(B\)-data before applying any girth conditioning.
On the independent \(A\) side choose any one fine bin above the three desired coarse colors.
Use a total of \(\lfloor n^{1-b}/(2R+3)\rfloor\) open-path trials in this bin and divide them as evenly as possible among the selected words.
Mark vertices globally across these trials, even across changes of word.
Since all the words use only neutral usable letters, each trial starts in an available first-stub pool in the specified bin, and a fresh realization of all its remaining turns has conditional probability at least \(300^{-(2R+2)}\).
This includes a fresh final vertex. [Disjoint open-path exposure](Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths)
For every one word its comparison binomial mean is at least
\[
             n^{\,1-b-a/4-2a\log(300)/\log(64)-o(1)}
                 > n^{\,1-\delta/2}
\]
for sufficiently large \(n\).
Thus fewer than \(\lfloor n^{1-\delta}\rfloor\) successes for any word have total conditional probability at most \(n^{a/4}\exp(-\Omega(n^{1-\delta/2}))\).
A finite union over the fine bins suffices, since paths in different bins necessarily use disjoint vertices.
Within each bin the markings ensure that no two successful paths use the same vertex.
Reversing sides gives the same probability bounds and joint conclusions by a union bound, without claiming independence of the two searches.

Take \(c_0>0\) so small that \(c_0\log(28|T|/p)<a/4\) and \(2c_0\log132<1\), with \(L=\lfloor c_0\log n\rfloor\).
As in the [conditioning step](Yin_C_A0053_v1.md#exponents-arbitrarily-close-to-one), the short-cycle expectation and switching count cost at most \(\exp(O(n^{3a/8}\log n))\) on conditioning on girth.
This is absorbed by the unconditioned cycle-search failure bound since \(a-b=a/2\), and by the open-path bound.
Intersect with the geometric, connectedness, singleton and finite-target events, all of conditional probability \(1-o(1)\).
Each selected word is a relation of the actual cone group by its opposite-side cycle.
Its simple open lifts have distinct endpoints with equal group labels, for both the forward and the inverse-factor convention.
This establishes true simultaneous original-group pairings on many independent cycle words, while a full pairing of even one whole color would require evidence beyond these paths.

## Assessment history

### Decision filtered-multiloop-pairings

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:24 |
| status | proved |
| reason | The review checked exact class counts, the arbitrary-order kernel argument and the disjoint-path probability estimates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous independent loops and the limits of finite quotient and fixed-basepoint certificates. |
| argument | [Proof](#how-many-opposite-side-base-vertices-are-necessary) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0090_v1.md#whole-argument-finding) | Independent review of the statement, proof and its direct inputs at the indicated scope. |

## Current assessment

[Selected decision](#decision-filtered-multiloop-pairings)
