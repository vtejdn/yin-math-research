---
author: Yin
---

# Torsion-free matching presentations with a prescribed quotient of order seven

## A different choice of matchings

The [original matching law](../claims/Yin_C_A0041_v1.md#statement) typically gives no nontrivial map to \(C_7\).
The deterministic voltage cover can create order-seven torsion.
Here the two graphs are instead sampled by independently matching each signed-label pair within seven prescribed blocks.
This gives exceptional choices in the original space of matching tuples and keeps the geometric inputs for the characteristic-two zero product.
It also determines the projected supports closely enough to decide the lifting test on this quotient.

Use the same rose, inverse-paired alphabet \(T\), vertex types, roots, and marginal label frequency \(\rho=129/16513\) as [Ope26f, §§1–2](../literature/pdf/Ope26f.pdf#page=2).
Fix any surjection \(\eta:F\to C_7\) from the free group of the rose.
Take \(n\) through multiples of \(7\cdot2(16513)^2\), so on each side each prescribed type splits equally into seven classes with colors \(c\in C_7\).
Make this split before any matching is chosen.
For each side, one \(t\) per inverse pair, and each \(c\), choose independently a uniform bijection from its vertices of color \(c\) carrying \(t\) to its vertices of color \(c+\eta(t)\) carrying \(\bar t\).
Every block has size \(N=n\rho/7\).
Use the inverse bijection for the reverse reading.
This defines a legitimate bijection for every source inverse pair and leaves all source types and turn frequencies unchanged.
Since every closed graph walk has zero total color increment, coning the components to the same rose gives a group \(G_n\) with an actual surjection \(\bar\eta:G_n\to C_7\).
The seven matching bijections are independent even when they project to the same pair of signed letters.

For all sufficiently large admissible \(n\) one can choose tuples in this law with \(G_n\) torsion-free, with both graphs connected, and with the source's two nonzero zero divisors over \(\mathbb F_2\).
Both vertex-occurrence vectors project to exactly \(n/7\) occurrences in every class of \(C_7\).
On the actual collected supports, every class is occupied, its cardinality is even, and its cardinality is \(n/7-o(n)\) along a sequence of such choices.
Moreover, for every preassigned finite list of finite target groups, the tuples may be chosen so that every homomorphism to any listed target factors through \(\bar\eta\).

## Girth, local expansion and the cost of a matching prescription

Write \(d_*=132\) and \(L=\lfloor c_0\log n\rfloor\), with \(c_0>0\) chosen so that \(c_0\log(14|T|/\rho)<1\) and \(2c_0\log d_*<1\).
The source allows sufficiently small \(c_0\), and its subsequent deterministic constants can be taken for this fixed choice.
In the independent colored law, each feasible prescription of \(k<L\) distinct matching pairs has probability at most \((N-k)^{-k}\).
Counting simple cycles by vertex and letter descriptions as in [Ope26f, Lemma 2.2](../literature/pdf/Ope26f.pdf#page=5) bounds the expected number of edges on short cycles by \(2\sum_{k<L} k(14|T|/\rho)^k=n^{\gamma+o(1)}\) or less, where \(\gamma=c_0\log(14|T|/\rho)<1\).
The bound includes loops and parallel pairs.
In the source's repair of a bad edge, require the other edge to be in the **same color block** and side.
Out of \(N\) choices, \(o(n)\) bad edges and \(O(d_*^{2L+2})=o(n)\) nearby edges are excluded.
The switch then preserves both colors and all types.
The source's two cases for a possible new short cycle use only distance and the nonbad second edge, so this switch reduces the number of bad edges.
As in the [reverse switching count](../claims/Yin_C_A0041_v1.md#girth-conditioning-and-the-torsion-free-realizations), at least half the colored tuples are within \(n^{\gamma'}\) transpositions of a high-girth tuple for \(\gamma<\gamma'<1\), and each such neighborhood has size \(\exp(o(n))\).
Hence the girth event has probability at least \(\exp(-o(n))\) in this law.

Now condition on that event and on \(s\) feasible matching prescriptions.
From any tuple containing one additional prescribed pair \(xy\), transposing its edge with a distant, unprescribed edge in the same block gives at least \(N-s-O(d_*^{2L+2})\) choices.
The output and \(xy\) identify uniquely the reverse transposition.
Thus the conditional probability of this pair is bounded by the reciprocal of that quantity whenever it is positive.
Iterating shows that any feasible \(E=O(L)\) distinct matching prescriptions cost at most
\[
                   (7/(n\rho))^E\exp(o(L)).                             \tag{1}
\]

The small-set expansion proof also survives in the girth-conditioned law.
If a \(k\)-set fails to double on adjoining its neighbors, some \(2k\)-set contains at least \(r=\lceil129k/2\rceil\) distinct edges.
Choose \(k\le\varepsilon n\) with \(\varepsilon\) so small that \(r\le N/3\).
There are at most \((C n/k)^{2k}\) such sets and at most \((Ck)^r\) choices of \(r\) prescriptions inside each, since the alphabet is fixed.
Use the preceding single-prescription bound successively to bound their probability by \((2/N)^r\).
Thus the failure probability at size \(k\) is at most \([C'(k/n)^{62.5}]^k\).
Taking \(\varepsilon\) smaller if necessary and summing separately below and above \(\sqrt n\) shows it tends to zero for the union over these sizes, on both sides.
Every ball now grows to more than \(\varepsilon n\) vertices in \(O(\log n)\) steps.
Along a geodesic, disjoint balls of that size are bounded in number, giving diameter \(O(L)\) for every component, as in [Ope26f, Lemma 2.3](../literature/pdf/Ope26f.pdf#page=6).

## The bounded-pattern estimate with the seven colors

The factor \(7^E\) in (1) cannot simply be absorbed in the error when \(E\) is proportional to \(L\).
It is canceled by the actual color constraints on vertex images.
Consider a fixed permitted word labeling of the stage \(\Delta_j\) in the proof of [Ope26f, Proposition 3.1, pp. 7–14](../literature/pdf/Ope26f.pdf#page=7).
Use its notation \(V_j,E_j,k_j\) for the vertex, edge, and prescribed-root counts, and \(Q_j\) for the number of active marked chains.
Its unlabelled-pattern analysis uses only the length, path count, girth and pairing restrictions.
In particular \(\Delta_j\) consists of a bounded number of whole chains with disjoint degree-two interiors, uniformly for each fixed choice of the pattern bounds \(K,C,I\).
Both the component count \(b_j\) and \(E_j-V_j\) are bounded in absolute value, since replacing each chain by one edge changes edge and vertex counts by the same number.

Choose an initial color on each component in at most \(7^{b_j}\) ways.
The fixed signed edge labels propagate all other colors by \(\eta\); an inconsistency gives no realization.
A prescribed initial vertex still has just one allowed image, if its color matches.
For each other vertex the earlier count of allowed images can be divided by seven, before imposing injectivity.
Indeed each type is exactly balanced across colors, so the count for a fixed internal turn is at most \((n\rho/7)w(t,u)\), and an unrestricted marked vertex has \(n/7\) choices at its required color.
Here \(w(t,u)\) is the same turn bound from the source because the mixture of types within each color is unchanged.
Relative to its uncolored bound, the vertex-image count therefore incurs a factor at most \(7^{b_j-(V_j-k_j)}\).
For feasible injective choices, different edge prescriptions are still distinct by immersion.
Applying (1), the net additional factor over the expression in source (3.10) is at most
\[
                              7^{b_j+E_j-V_j+k_j}=\exp(O_{K,C,I}(1)).
\]
It is absorbed in \(\exp(o(L))\) in that estimate.
Erasing the color constraints still gives an upper bound on the permitted word strings (3.11).
The reversed-word symmetry, squared-word estimate, link and bin counts, and the multiplicity inequality (3.4) concern the same type data, labels, and unlabelled paths.
They entail the same uniform \(o(L)\) error and exponential saving in the product of the numerical stage bounds.
The source's selection of one small stage bound and sum over \(\exp(o(L))\) enlarged patterns therefore still prove Proposition 3.1 for this law and each fixed \(K,C,I\).
The argument allows either fixed choice of rooted interval and is uniform in which actual root vertices were prescribed: the upper bound for a prescribed image was one and all combinatorial constants are independent of their names and colors.

On the diameter event, the source's deterministic arrangement reduction makes just one fixed choice of \(K,C,I\) after the geometric constants have been chosen.
Neither planar separation nor the closing, cutting or marking arguments use matching independence.
Thus [Proposition 4.5](../literature/pdf/Ope26f.pdf#page=18) still excludes reduced spherical arrangements with probability \(1-o(1)\) under girth conditioning.
The cone-picture argument, Proposition 5.1, Corollary 5.3, and the simultaneous-step degree sum in §6 are deterministic statements about these immersed rooted graphs.
They give the same asphericity, torsion-freeness, unique root contribution in each factor and zero product in characteristic two. [Ope26f, §§5–6, pp. 20–24](../literature/pdf/Ope26f.pdf#page=20)

## Connectedness and the other finite quotients

Here is the entropy estimate also needed for large disconnected pieces.
For the planted law refine each original type to \((\tau,c)\) with frequency \(\lambda_\tau/7\).
For an additional vertex marking by symbols in a fixed finite set, let \(v_{\tau,c}\) be its distribution in that refined type and \(v_{t,c}\) its distribution at outgoing label \(t\) with planted color \(c\).
For cut indicators require the additional symbol to be equal at the two ends of every edge.
For an additional homomorphism \(\theta:F\to Q\) require the new symbol at the other end to equal \(R_{\theta(t)}\) of the first symbol.
In either case the matching blocks are precisely paired color-label classes of frequency \(\rho/7\), and the distributions at their two ends must correspond by that permutation.
The same multinomial argument as in the [finite-target entropy estimate](../claims/Yin_C_A0041_v1.md#strict-entropy-loss) bounds the logarithm of the first moment for one family of refined histograms by
\[
 n(F_0-F_1)+O(\log n),\qquad
 F_0=\sum_{\tau,c}\frac{\lambda_\tau}{7}H(v_{\tau,c}),\qquad
 F_1=\frac12\sum_{t,c}\frac{\rho}{7}H(v_{t,c}).
\]
There are only polynomially many histograms, and \(F_1\ge(129/2)F_0\) by entropy concavity on each planted color.
Equality of the exponent with zero forces every refined type and label class to be monochromatic in the additional symbol.
Any two types at a fixed planted color share an ordinary letter.
Thus the additional symbol equals a single value \(f(c)\) at that planted color across all types.

For a cut indicator the matching equations give \(f(c+\eta(t))=f(c)\) for every \(t,c\).
Surjectivity of \(\eta\) makes the cut constant on the whole side.
On the compact set of compatible histograms with cut density in \([\varepsilon,1/2]\), the exponent therefore has strictly negative maximum, if the set is nonempty.
This excludes all such cuts with exponentially high probability even after the subexponential cost of girth conditioning.
The small-set expansion estimate excludes components of size at most \(\varepsilon n\) with probability \(1-o(1)\).
A disconnected side would have a component of size at most \(n/2\), giving connectedness of both sides with probability \(1-o(1)\).
Every type used in the argument is present with positive frequency on its own side, and the estimates apply on either side separately.

For a \(Q\)-coloring on the first side, equality forces \(f(c+\eta(t))=f(c)\theta(t)\).
Iterating along a word \(W\) gives \(f(c+\eta(W))=f(c)\theta(W)\).
Hence \(\ker\eta\subseteq\ker\theta\), so \(\theta\) factors through \(\eta\).
For every nonfactoring \(\theta\) compactness again gives strict loss.
Only finitely many \(\theta\) and finite target groups are involved for any fixed order bound.
Thus, with exponentially high probability under girth conditioning, all maps of \(G_n\) to these targets factor through \(\bar\eta\).
Maps factoring through \(\bar\eta\) always exist with their prescribed values.

## Occurrence counts and the actual characteristic-two supports

On the connectedness event the complete roots' occurrence factors use every vertex on each side.
The images of the path labels relative to the roots are the planted colors shifted by the respective root color, with an additional sign for the inverse labels on the second side.
The occurrence histograms in \(C_7\) therefore have exactly \(n/7\) entries in each class on each side.
Each quotient product has exactly \(7(n/7)^2=n^2/7\) vertex-pair occurrences, by summing over its seven possible first colors.

For a connected side and a fixed reference root, two vertices have the same group label precisely when a path between them has trivial label, a condition independent of the reference root.
The probability of failure of the rooted separation conclusion at an arbitrary prescribed vertex is \(o(1)\), uniformly by the bounded-pattern estimate and its deterministic application above.
Changing roots affects the event used to prove separation, but leaves the graph law and the cone group unchanged.
Summing failure probabilities shows that the expected number of vertices on either side from which a trivial-label path reaches a different vertex is \(o(n)\), under the girth condition.
Markov's inequality therefore makes their number \(o(n)\) in probability, and one can choose a deterministic error bound \(o(n)\) holding with probability tending to one.
All other vertices supply singleton labels in their components.
After restricting to the connectedness event and collecting labels over \(\mathbb F_2\), each quotient class contains at least \(n/7-o(n)\) and at most \(n/7\) distinct surviving group labels.
The count in each class has exactly the same parity as the number of original occurrences there, since replacing \(m\) occurrences by \(m\bmod 2\) deletes an even number.
Here \(n/7\) is even, so every class is occupied with an even count for sufficiently large selected \(n\).
For the true support rectangle the number of cells above each quotient product is consequently \(n^2/7-o(n^2)\) and divisible by four.

Opposite integer signs can consequently be assigned in pairs within each quotient class of the true support on either side.
They sum to zero class by class, giving an integral lift of the **projected** equations with every original variable odd.
This works for every smaller quotient factoring through the planted quotient, too.
The group-ring equations on the original supports are finer and these assignments need not solve them.
The construction thus realizes the specified quotient in a torsion-free source-type group and controls its actual histogram, while leaving the complex lifting problem on the original product fibers open.
