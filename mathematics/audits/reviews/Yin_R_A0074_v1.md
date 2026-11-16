---
author: Yin
---

# Deterministic restrictions on the seven color classes

A separate reviewing agent inspected the fixed C_A0043_v1 for Yin on 2026-11-16T18:19 UTC.
The same reviewer independently checked the added fourth item and its unwrapping argument on 2026-11-16T18:21 UTC.
The reviewer did not develop this Claim or receive its development discussion, author explanations or any earlier verdict before checking it.
The reviewer previously developed the two different random matching results C_A0041 and L_A0047 cited for comparison and independently checked the arithmetic classification C_A0042.
The deterministic proof under review uses the fixed vertex-type proportions and C_A0042.
The two random-model theorems supply no step in its argument.
On 2026-11-16T18:24 UTC the reviewer separately inspected L_A0046's direct seven-fiber calculation for Yin, having taken no part in that derivation and received no prior development discussion or verdict about it.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |
| [Seven quotient fibers](#seven-quotient-fibers) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0043_v1.md#statement) | Conditional occurrence, collected-support and repeated-vertex assertions for a given quotient and connected sides. |
| [Whole-argument finding](#whole-argument-finding) | [Neighbor constraints](../../claims/Yin_C_A0043_v1.md#neighbor-constraints) | Pair frequencies, three-term progressions, six two-element translates and connectedness with a single opposite pair. |
| [Whole-argument finding](#whole-argument-finding) | [Passing to supports](../../claims/Yin_C_A0043_v1.md#passing-from-vertices-to-the-two-actual-supports) | Parity and occupancy after collection, exact use of the \(C_7\) classification, and the \(n/(3v)\) threshold. |
| [Whole-argument finding](#whole-argument-finding) | [Unwrapping the occurrence sets](../../claims/Yin_C_A0043_v1.md#unwrapping-when-both-occurrence-sets-omit-a-color) | Independently chosen cuts, common signed integer changes, cancellation in the Laurent polynomial domain, and the integer-sign lift on a true support. |
| [Whole-argument finding](#whole-argument-finding) | [Matching-instance calculation](../../claims/Yin_C_A0043_v1.md#what-a-supplied-matching-instance-would-determine) | Forest test, conditional histograms and coarse-product cardinalities. |
| [Whole-argument finding](#whole-argument-finding) | [Cyclic classification](../../claims/Yin_C_A0042_v1.md#statement) | Zero-indicator and two-quadruple rows, algebraic lifts, and obstruction over all finite ramified or unramified extensions at precision eight. |
| [Seven quotient fibers](#seven-quotient-fibers) | [Complete quotient fibers](../../ledger/Yin_L_A0046_v1.md#complete-fibers-with-arbitrary-positive-odd-multiplicities) | Normalization by translations and a common dilation, the seven complete rectangle unions and arbitrary odd class counts. |
| [Seven quotient fibers](#seven-quotient-fibers) | [Direct unit calculation](../../ledger/Yin_L_A0046_v1.md#why-four-appears-in-the-identity-coefficient) | Cancellation at unit aggregates, the single remaining coefficient, ramified precision and the integral sign witness modulo four. |
| [Seven quotient fibers](#seven-quotient-fibers) | [Matching-instance qualifications](../../ledger/Yin_L_A0046_v1.md#which-counts-come-from-the-paper) | Conditional inputs, occurrence counts versus true support counts, and use of the comparative balanced example. |

## Whole-argument finding

The reviewer checked the exact line and extra proportions, matching bijections and even total size in [Ope26f, §2.1, p. 4](../../literature/pdf/Ope26f.pdf#page=4).
The root-component occurrence sums, cancellation mechanism and unspecified choice of matching were checked in [Ope26f, §6, p. 24](../../literature/pdf/Ope26f.pdf#page=24).

In the actual source each ordinary line occurs with fraction \(1/v\).
Two distinct ordinary letters determine exactly one line.
An individual extra occurs within every line class with fraction \(p\) on either side, since on the first side precisely two of the extra pairs contain it and each has fraction \(p/2\).
Thus a mixed pair has fraction \(p^2\), and a pair of extras has fraction \(p/2\) or \(p\) on the two sides respectively.
With \(p=129/16513\) and \(129^2>16513\), each distinct-letter pair occurs at least \(n/v\) times.

Signed inverse edges have opposite increments, also after reversing all increments for inverse group labels on the second side.
Surjectivity on the cone group makes at least one letter increment nonzero.
The two inverse letters occur at a common vertex, so its color and the two neighboring colors form a nonconstant progression.
The six directed differences of \(0,1,3\) are the six distinct nonzero residues, excluding that triple and its affine images.
For its four-point complement \(K\), inclusion-exclusion gives exactly two representations of each nonzero directional difference.
If \(I_d(K)=I_e(K)=\{x,y\}\) with \(d\ne e\), the three ordered translates of \((x,y)\) have distinct first coordinates and repeat the same difference three times.
Hence the six sets \(I_d(K)\) are precisely the six two-element subsets of \(K\).
The reviewer also enumerated all fourteen affine images of the complement and verified this property directly.

Every pair of distinct realized nonzero increments must give intersecting neighbor sets if all vertices have colors in \(K\).
Taking at most one set from each of the three complementary pairs allows at most three increments, and closure under negation then leaves only one nonzero opposite pair.
The induced undirected step graph on \(K\) then has only two edges.
Zero-step edges and multiple graph edges cannot connect its four colors.
Connectedness of the graph side excludes this remaining case.

Collection within a fixed group label removes an even number of vertices in characteristic two.
Consequently the colorwise parity masks agree before and after collection, even when an occupied class disappears entirely.
Connectedness ensures that each occurrence factor uses the entire even-sized side.
The cyclic classification then leaves only a zero parity factor or two complementary-to-line quadruple masks with opposite cubic orbits.
In the latter case both occurrence sides have at least one additional occupied class by the neighbor proof.
The exact-lift row therefore applies before collection.
After collection the only obstruction to an exact marked lift is the pair of tight quadruples, with both sides losing all occurrences in at least one outside class.
That pair still lifts modulo four and fails modulo eight, including over finite ramified extensions when precision is measured in powers of two.

With four or more realized nonzero increments, some two of their \(I_d(K)\) are disjoint.
Choose two corresponding distinct signed letters.
Each of their at least \(n/v\) common vertices is either outside \(K\) or has a specified neighbor outside \(K\).
For a fixed outside vertex there is at most one preimage along each of the two signed steps by bijectivity of the corresponding matching.
Including the possibility of charging the vertex to itself costs at most three charges.
A tight collected mask thus requires at least \(n/(3v)\) outside occurrences, all of which are repeated vertices.
The strict inequality on just one side suffices to eliminate a tightly occupied pair.

For item 4 the forward letter colors on both sides have the same signed step after scaling by \(d^{-1}\), including on the side whose factor ultimately takes inverses.
After deleting one omitted color the induced nearest-neighbor graph on the other six residues is a path.
Its consecutive integer representatives realize every directed step \(0,+1,-1\) with the corresponding integer difference, since the two end residues of this path are not neighbors in the seven-cycle.
Separate cuts and subtraction of the two root values therefore preserve the common signed change along each simultaneous step.
The difference of integer heights is constant on each such component, and the component has even size by the source's degree sum.
This proves exact zero of the product of the two height polynomials over \(\mathbb F_2[T,T^{-1}]\).
Its domain property forces an individual factor to vanish, which reduces to zero also after reducing exponents modulo seven, restoring the scaling and the second factor's sign.
The same side has only even counts on its true projected support and admits a lift by opposite integer signs.
Thus a tightly occupied one-step obstruction requires at least one full occurrence set before collection.

For fixed matching data, the signed letter counts of fundamental forest loops span the cycle relations after mapping to the abelian target.
Their nullspace over \(\mathbb F_7\) therefore finds exactly the characters, and a nonzero one is onto.
Forest path sums give the occurrence counts, whereas a count of surviving labels requires additional information about odd group-label equivalence classes within each color.
A complete partition by label equality is sufficient; identifying individual equivalence pairs is unnecessary if the odd-class counts are already determined.
The seven-rectangle convolution formula is exact for either specified pair of histograms.
The published existence proof supplies neither a distinguished matching nor those numerical true-support counts.
The review supports the four stated deterministic results and does not infer a quotient or a lift of the original group equations from them.

## Seven quotient fibers

For two tight quadruples of opposite orientation, their missing triples are independent translates of opposite Fano lines, by the reviewed classification C_A0042.
The identity \(\{3,5,6\}=6-\{0,1,3\}\) gives \(D=\{0,1,2,4\}\) and \(-D\) as compatible representatives, allowing an inversion common to both sides if needed.
Listing the sixteen values \(i-j\) for \(i,j\in D\) gives the four diagonal pairs above zero and exactly the six printed pairs of two rectangles above nonzero colors.
With repeated images in a quotient each such rectangle contributes the product of its aggregate coefficients, irrespective of further separation of those cells in the original group.

For opposite colors \(1,6\), multiplication of the two binomial equalities gives \(p_1(p_0-p_2)=0\).
The analogous products for \(2,5\) and \(3,4\) give \(p_2(p_0-p_4)=0\) and \(p_4(p_1-p_0)=0\), respectively.
After inverting the aggregates all four \(p_i\) coincide.
This localization matters for an unrestricted polynomial quotient with several occurrences per class; a sum of individual invertible variables can otherwise vanish.
At the marked point odd cardinality gives residue one for each aggregate.
They are therefore invertible for every lift being tested, also in \(\mathcal O_L/2^n\mathcal O_L\).
The remaining coefficient is \(4p_0\), nonzero in characteristic zero and of valuation exactly \(2v_L(2)\), strictly below \(v_L(8)\).
In the other direction, the signs \(+1\) at index zero and \(-1\) elsewhere on both sides solve all six off-zero equations integrally and give four at zero.
Each sign can be realized on any positive odd number of occurrences by assigning that sign once and then opposite pairs.

The argument thus proves the precise obstruction without a Fourier determinant for any actual occurrence data with the specified tight odd masks.
The reference to the source's unspecified matchings and the comparison with the balanced construction preserve their separate scopes.
In the latter calculation the exact occurrence counts \(n/7\) give \(n^2/7\) cells per coarse product, while seven products of even true counts \(n/7-o(n)\) give a multiple of four of size \(n^2/7-o(n^2)\).
This arithmetic uses the previously developed balanced histogram result at its stated scope and does not constitute another independent review of that construction.
