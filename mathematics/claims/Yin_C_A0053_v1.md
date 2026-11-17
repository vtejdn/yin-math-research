---
author: Yin
---
# Polynomially many genuine paired collisions in each even color

## Statement

Use the [four-line matching law](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) or its [order-21 or order-28 refinement](../ledger/Yin_L_A0053_v1.md#exact-refinement-with-two-binary-coordinates), with both prescribed roots of color zero.
Take \(n\) through the admissible sizes of the corresponding law and take the permitted fixed girth constant \(c_0=1/1000\).
With probability tending to one under girth conditioning and the source safeguards, each of the forward colors \(3,5,6\) on **each** side contains at least \(\lfloor n^{1/5}\rfloor\) vertex-disjoint pairs of distinct vertices with equal labels in the original cone group.
On the second side inversion negates the quotient colors and preserves the equalities.
All these pairs consist of non-root vertices.
In the refined laws the same conclusion holds simultaneously in **each fine bin** over the three forward colors.
Moreover for every fixed \(0<\delta<1\), choosing a sufficiently small positive \(c_0=c_0(\delta)\) gives \(\lfloor n^{1-\delta}\rfloor\) such pairs in each bin.
No single girth constant uniform as \(\delta\downarrow0\) is asserted.

The equality in each pair comes from a word read on a simple open path on that side and on a genuine cycle of the opposite side.
The group is torsion-free, has the prescribed root separations, and the source factors are nonzero with zero product over \(\mathbb F_2\).
This supplies a growing family of actual collisions even though all but \(o(n)\) vertices on each side have multiplicity one and all seven true colors survive in typical realizations.
The counted pairs are disjoint as vertices.
Their *group labels* need not be different, and their existence does not imply erasure of the color.

## The unconditioned exposure law

Write \(v=16513,\ k=129,\ p=k/v\), let \(d=7,21,28\) be the order of the planted group, and put \(N=np/d\).
Call a signed letter usable here if it is ordinary, its inverse is ordinary, and its increment is zero in the entire planted group.
On ordinary–ordinary pairs the refined increments have zero extra coordinate in both refinements.
Of the ordinary letters three are paired with extras and six are active, so every vertex has at least \(129-9=120\) usable stubs.
Both sides have the following uniform counts in a specified planted color:

- A block for any usable signed letter has \(N+O(1)\) vertices.
- For two distinct usable signed letters the common pool has \(n/(dv)+O(1)\) vertices, because the two corresponding ordinary points determine exactly one projective line.

The errors are bounded constants from changes at four empty-extra types, in the specified fine bins on each side.
In particular the ratio of the latter count to a single-stub block size tends to \(1/129\).
Initially sample in the **unconditioned** law under consideration, in which all matching blocks are independent uniform bijections.
Revealing the partner of an unused stub in any direction chooses uniformly among the still unmatched opposite stubs of its block, conditional on the entire exposed history.
Mark all vertices ever touched by a search on its side.
Throughout a search using \(O(n^{15/16})\) exposures, each prescribed positive pool above loses at most \(O(n^{15/16})=o(n)\) touched vertices.
Hence a newly revealed partner is old with probability \(O(n^{-1/16})\), and has probability at least \(1/300\) to be fresh and to carry any specified usable next letter distinct from its incoming stub.
The constants can be taken uniform over all histories within this budget. A fresh starting vertex of a specified color and first stub can always be chosen directly.

## Finding a short closed word on one side

We first work on side \(B\) using only usable edges in color zero.
Set
\[
        R=\left\lceil\frac{\log n}{4\log64}\right\rceil,\qquad
        M=64^R,\qquad n^{1/4}\le M\le64n^{1/4}.
\]
A trial starts at a fresh vertex and attempts to grow a tree with 64 children at every internal vertex up to depth \(R\).
A hit inside the current tree supplies a simple cycle of length at most \(2R+1\): the exposed edge is new and the old edges of the tree provide the return path.
Loops and two distinct parallel edges are allowed in this unconditioned search.
All cycle words so obtained are cyclically reduced, since no inverse consecutive readings are possible along a cycle without reversing the very same edge in an immersed graph.

For each current internal vertex, use up to 100 unused usable stubs to collect its 64 fresh children.
Before an internal hit, its only already exposed stub upon first growing its children is its parent stub, if present.
Indeed any intervening edge arriving there during the same trial would already have hit the current tree, and its original discovery was at an untouched vertex.
If a tree has not found a cycle and aborts at this vertex, at least 37 of at most 100 attempts hit previously touched vertices outside the current tree.
Conditional probabilities and a union bound over the choices of 37 attempts bound this probability by \(O(n^{-37/16})\), uniformly under the exposure budget.
There are \(O(M)\) internal vertices, so the trial either finds a cycle or finishes the tree except for an abort probability \(O(Mn^{-37/16})\).
A failed trial is discarded and its touched vertices remain marked.

For a complete tree with no internal hit, the \(M\) leaves still have all their usable stubs except their respective incoming ones.
Each can supply an ordered pair \(t,s\) of available usable labels from distinct inverse pairs.
Since the alphabet is fixed, at least \(c_1 M\) leaves admit the same ordered choice, for some fixed \(c_1>0\).
Choose two disjoint sublists each of size at least \(c_2M\) for large \(n\).
From the first sublist expose \(t\)-edges.
A fresh partner carrying \(\bar s\) has conditional probability at least \(1/300\), because \(\bar t\ne\bar s\).
If an exposure hits a tree vertex, the same cycle shortcut applies.
Otherwise, except with probability \(\exp(-\Omega(M))\), at least \(c_3M\) distinct fresh partners with unused \(\bar s\)-stubs are obtained.
Indeed a sequence of trials with conditional success probabilities at least a fixed \(u>0\) dominates independent Bernoulli trials of parameter \(u\), by using a fresh uniform random number at each step.
We can count an early cycle as success for the trial and use arbitrary additional Bernoulli trials in this comparison.
The positive lower-tail estimate follows from the ordinary binomial bound.
The potential partners are distinct because the \(t\)-matching is injective, and the two label pairs used in this step are different.

Expose the \(s\)-edges from the second sublist.
Until a shortcut cycle is found, their stubs remain available and the opposite matching block still contains all the \(\bar s\)-stubs just designated.
Each such exposure hits the designated set with conditional probability at least \(c_4M/n\) because all these vertices have the same planted color and the block size is \(O(n)\).
A hit gives a two-edge connection, through a vertex outside the tree, between distinct leaves.
The tree path between those leaves closes a simple cycle of length at most \(2R+2\).
The chance of at least one hit is at least \(1-(1-c_4M/n)^{\lfloor c_2 M\rfloor}=\Omega(M^2/n)\), since \(M^2/n\to0\).
Combining the growth and connection steps, each new trial conditionally succeeds with probability \(\Omega(n^{-1/2})\).
This bound allows early successful cycles and discards the stated abort events.

Run \(\lfloor n^{11/16}\rfloor\) trials or stop on the first cycle.
Each uses \(O(M)\) edges, so the total number of touched vertices stays \(O(n^{15/16})\) as required.
The conditional lower bounds give failure probability at most \(\exp(-\Omega(n^{3/16}))\).
On success select one of the resulting simple cycle words \(W\) from the \(B\)-data alone.
Every letter is usable and \(1\le |W|\le 2R+2\).

## Reading the same word on disjoint open paths

Condition on the unconditioned \(B\)-data specifying \(W=t_1\cdots t_h\).
Independence leaves side \(A\) in its unconditioned matching law, with the same usable-stub estimates.
In a specified fine bin over color 3 choose a fresh starting vertex carrying \(t_1\), and attempt to expose a path reading \(W\).
At each step require a completely fresh endpoint, carrying \(t_{j+1}\) if another step follows.
The incoming stub is \(\bar t_j\ne t_{j+1}\) by free reduction, and at the final step only freshness is needed.
Mark the vertices of failed trials too and abort a trial at its first failure.
Under the budget bound each trial therefore succeeds with conditional probability at least \(300^{-h}\).
A successful path has distinct endpoints, is disjoint from the other successful paths and stays in its fine bin because all increments are zero.

Take \(\lfloor n^{15/16}/(2R+3)\rfloor\) trials.
The exposure budget is \(O(n^{15/16})\), and the number of starting vertices needed is \(o(n)\) in a fixed positive-density first-stub pool.
Since
\[
       300^{-h}\ge 300^{-4}n^{-\log 300/(2\log64)},\qquad
       \frac{15}{16}-\frac{\log300}{2\log64}>0.25,
\]
the binomial comparison has mean greater than \(n^{0.24}\) for all sufficiently large \(n\).
Its lower-tail bound gives at least \(\lfloor n^{1/5}\rfloor\) successful paths except with probability \(\exp(-\Omega(n^{0.24}))\).
The bound is uniform in the selected word.
The same exposure works in every fine bin over colors 3, 5 and 6. One may use a separate marginal failure estimate at each fine color and take their union.
Coning side \(B\) makes \(W=1\) in the actual group, so the two endpoints of every successful path have equal forward group labels whenever they belong to the chosen root component.
Both endpoint occurrences are distinct even if the resulting group element is shared by more vertices.

The same proof with the two sides interchanged uses the same ordinary-pair turn counts, since both sides use the same projective lines and the same four bounded line-count adjustments.
Thus an \(A\)-cycle pairs distinct occurrences in the three forward colors on \(B\).
There is no requirement that this reverse event be independent of the first one.
A finite union over both sides and the specified fine bins still has failure probability \(\exp(-\Omega(n^{3/16}))\) before conditioning.

## Conditioning and what is paired

For the chosen \(c_0\), \(\gamma=c_0\log(2d|T|/p)<0.02\) for all three laws.
The [short-cycle expectation and switching proof](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts), with its [fine block sizes](../ledger/Yin_L_A0053_v1.md#matching-safeguards-and-the-relative-mod-two-quotient), gives at most \(n^{\gamma+o(1)}\) expected bad edges before conditioning.
With probability at least \(1/2\) the tuple has at most \(n^{0.05}\) such edges.
It can then be switched to girth at least \(L=\lfloor c_0\log n\rfloor\) in at most \(n^{0.05}\) transpositions within the assigned blocks.
Reversing the switch sequences costs at most \(\sum_{j\le n^{0.05}}(Cn^2)^j\) choices, giving girth probability at least \(\exp(-O(n^{0.05}\log n))\).
Dividing the preceding unconditional failure bound by this probability still gives a bound tending to zero.
In particular on a surviving tuple the cycle found in the successful description cannot be shorter than \(L\).
The exposure searches only established events in matching space; they did not fix short word prescriptions before estimating conditional geometry.

In each of these girth-conditioned laws, connectedness, the source's root separations and cone asphericity hold simultaneously with probability \(1-o(1)\), by the [four-line safeguards](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) and their [finite refinements](../ledger/Yin_L_A0053_v1.md#a-smaller-quotient-of-odd-order-even-when-the-relative-mod-two-test-is-trivial).
Intersecting gives all the stated original-group equalities on complete root components of a torsion-free tuple, with the genuine characteristic-two zero product.
No occurrence paired here can be the chosen root since the three colors differ from zero.
There may still be unpaired singleton labels within every designated color.
Indeed [the four-line singleton estimate](Yin_C_A0051_v1.md#connectedness-collection-and-the-erasure-threshold) supplies \(n/7-o(n)\) surviving labels per coarse color in probability in the order-seven law, and the [product support bound](Yin_C_A0051_v1.md#product-fibers-and-complex-coefficients-in-the-four-line-law) still applies there.
In the order-21 law the bin with extra coordinate 1 and coarse color 3 is odd, being in \(K+1=\{1,2,3,5\}\).
The other nonzero extra coordinate also detects color 3.
The [order-21 certificate](../ledger/Yin_L_A0053_v1.md#a-smaller-quotient-of-odd-order-even-when-the-relative-mod-two-test-is-trivial) shows on these very tuples that all three even coarse colors on each side have a surviving group label, while the open paths give many disjoint pairs in every such fine bin.
Thus the found pairs cannot extend to a complete erasing pairing on the refined tuples.

## Exponents arbitrarily close to one

For fixed \(0<\delta<1\), put \(a=\delta/8,\ b=a/2,\ R=\lceil a\log n/\log64\rceil\) and \(M=64^R=\Theta(n^a)\).
Use exposure budget \(O(n^{1-b})\) per search, so the conditional probability of an old partner is \(O(n^{-b})\).
The tree abort bound in one trial is now \(O(n^{a-37b})=o(1)\), and \(M^2/n\to0\).
Consequently the per-trial cycle probability is at least \(\Omega(M^2/n)\): an early internal hit is already a successful trial; otherwise the connection estimate applies whenever the tree finishes.
In \(\lfloor n^{1-b-a}\rfloor\) trials the failure bound is \(\exp(-\Omega(n^{a-b}))\).
On the other side use \(\lfloor n^{1-b}/(2R+3)\rfloor\) open-path trials.
The binomial comparison mean is at least \(n^{1-b-2a\log300/\log64-o(1)}\), which exceeds \(n^{1-\delta/2}\) for large \(n\) with these choices.
The probability of fewer than \(\lfloor n^{1-\delta}\rfloor\) successes is then \(\exp(-\Omega(n^{1-\delta/2}))\).
Choose \(c_0>0\) with \(c_0\log(2d|T|/p)<a/4\) and \(2c_0\log132<1\).
Using \(3a/8\) in place of \(0.05\) in the girth repair gives conditioning cost at most \(\exp(O(n^{3a/8}\log n))\), which is absorbed since \(a-b=a/2\).
All fixed-parameter geometric conclusions still apply for this choice of \(c_0\).
Taking a finite union as before finishes the stronger statement without a positive lower bound on the fraction of the whole color that can be paired.

Given an actual matching tuple, a closed word on one side and simple open lifts on the other can be checked by graph traversal alone.
More generally, among vertices of a single simultaneous-step component with a fixed second coordinate, the first coordinates all have equal group labels, by cancellation of their common second factor.
Disjoint pairs extracted from such lists certify individual original-group equalities without solving a word problem.

## Assessment history

### Decision simultaneous-partial-pairings

| Field | Value |
| --- | --- |
| date | 2026-11-17T09:51 |
| status | proved |
| reason | Independent review verified the two searches, disjoint paths, original cone relations, the girth-conditioning cost and the exponent choices in all three laws. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous disjoint pairs in the original group in every designated coarse or fine bin at the stated girth scales. |
| argument | [Proof](#the-unconditioned-exposure-law) | Full proof for the four-line law and its two refinements. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0089_v1.md#whole-argument-finding) | Independent whole-proof review including both growth estimates and the surviving odd bins. |

## Current assessment

[Selected decision](#decision-simultaneous-partial-pairings)
