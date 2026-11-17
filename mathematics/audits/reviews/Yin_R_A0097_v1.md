---
author: Yin
---

# Growing subgroup-index bounds, integral perfection and an alternating-group image

A separate reviewing agent inspected fixed C_A0061_v1 for Yin on 2026-11-17T02:43 UTC.
The reviewer developed earlier fixed-target and planted finite-color estimates and their bounded-perturbation applications, but did not develop C_A0061 or receive its development discussions, author explanations or prior verdicts.
Here the growing marking alphabets, the subgroup-cover argument, integral perfection, and the application to actual vertex labels were all checked independently.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0061_v1.md#statement) | Growing finite-index threshold for possibly nonnormal subgroups, perfect kernel, factorization to solvable groups and simultaneous six-color survival. |
| [Whole-argument finding](#whole-argument-finding) | [Alphabet-independent entropy](../../claims/Yin_C_A0061_v1.md#an-entropy-inequality-independent-of-the-marking-alphabet) | Ordinary projective incidence, small and large coordinate estimates, numerical constant and independence of the mark count. |
| [Whole-argument finding](#whole-argument-finding) | [Small-index subgroups](../../claims/Yin_C_A0061_v1.md#vertex-markings-from-small-index-subgroups) | Transitive coset action, no global section, graph markings, modal lower bound, uniform error sizes and union bound up to \(\kappa n/\log n\). |
| [Whole-argument finding](#whole-argument-finding) | [Perfection](../../claims/Yin_C_A0061_v1.md#from-bounded-length-relators-to-perfection) | Correct subgroup presentation in the planted rose cover, relation lengths, integer minor, comparison with the subgroup-index threshold, and solvable images. |
| [Whole-argument finding](#whole-argument-finding) | [Alternating-group refinement](../../claims/Yin_C_A0061_v1.md#a-refinement-that-distinguishes-all-six-colors-using-a-perfect-kernel) | Noncommuting increments, exact block shifts, original group quotient, rooted factor counts, topology and perfection of the coarse kernel. |
| [Whole-argument finding](#whole-argument-finding) | [Incidence input](../../claims/Yin_C_A0040_v1.md#the-probability-of-a-cut) | Equally frequent ordinary lines and the exact projective plane incidence identity. |
| [Whole-argument finding](#whole-argument-finding) | [Finite group model](../../claims/Yin_C_A0044_v1.md#matching-within-the-prescribed-color-classes) | Independent matching blocks with the regular right action of the fixed planted group. |
| [Whole-argument finding](#whole-argument-finding) | [Diameter and patterns](../../claims/Yin_C_A0044_v1.md#girth-conditioning-and-bounded-patterns) | Girth-conditioning cost, small-set expansion, diameter, and fixed finite state factors in the bounded-pattern proof. |
| [Whole-argument finding](#whole-argument-finding) | [Perturbation input](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Uniformly bounded deviations from balanced positive type and turn counts, with the required exact matching symmetries. |

## Whole-argument finding

For the balanced distributions subtracting the mean in the incidence identity kills the constant projection.
The normalized variance of the point-conditioned coordinate is \(q/k^2\) times the line-conditioned variance, which is at most \(m_i(1-m_i)\).
For \(m_i\le p^2\), \(u_{ti}\le m_i/p\) gives \(\log(1/u_{ti})\ge\tfrac12\log(1/m_i)\) wherever the summand is positive.
For the remaining coordinates, the lower bound on \(\mathbb E[u_{ti}(1-u_{ti})]\) and monotonicity of the displayed integral give a coefficient at least \(0.102249487\ldots>1/10\) on \(m_i\log(1/m_i)\).
This argument is coordinatewise and loses no factor depending on the number of symbols.
Bounded perturbations change the conditional mixtures of the *same* type distributions by \(O(1/n)\) in total variation.
The coupling entropy inequality thus costs at most \(O((\log n)/n)\) per entropy in the normalized estimate for \(m\le n\), with finitely many types, labels and planted colors.

An index-\(m\) subgroup of \(H\) has a transitive coset action whether or not the subgroup is normal.
Lifting that action to the fundamental group of the planted rose cover gives edge permutations with inverse readings, for example after setting tree-edge permutations to the identity.
A section fixed around every cover loop would supply a fixed point of the transitive action for \(m>1\).
Nevertheless each closed walk of the first matching graph lifts to a loop whose permutation is the identity, since its based conjugate is a cone relation already trivial in \(H\).
Path transport therefore gives a compatible marking on this side, also when it is disconnected.

For fixed compatible histograms the named-destination matching count and type multinomials give exponent \(n(A-B)\) with factorial error \(O(m\log(n+1))\).
Each signed endpoint entropy is counted with a half because matching transports the two distributions by a bijection.
Over the ordinary points the coefficient in \(B\) is at least \(129/20\) times the average overall entropy, whereas the upper bound for \(A\) uses coefficient one.
A modal mark at each planted color cannot be a section.
Every pair in a block witnessing its violation has a nonmodal endpoint, and each vertex can occur at most twice among endpoints of that single block.
This yields at least \(np/(2d)-O(1)\) nonmodal vertices and, after accounting for actual color weights, the claimed uniform entropy gap.
The \(O(m\log n)\) logarithmic cost includes all histograms and the possible edge permutations on the fixed planted cover.
A sufficiently small fixed \(\kappa\) absorbs this cost for all \(m\le\kappa n/\log n\), simultaneously in the conditional bound after division by the \(\exp(-o(n))\) girth-event probability.
Any nontrivial image of \(H\) in a target no larger than that threshold would itself give a forbidden subgroup index by taking the kernel.

For integral perfection, the planted rose cover has constant cycle rank \(r=1+d(8258-1)\).
The fundamental loops of breadth-first trees in the matching components have length at most \(2D\log n+1\) on the diameter event.
All their lifts, one at each planted color, provide exactly the abelianized relations for \(H\): different free-group conjugations amount to changing the cover base vertex and conjugating inside the cover.
Removing tree coordinates gives vectors in \(\mathbb Z^r\) whose \(\ell^1\)-norm is at most that loop length.
Absence of an index-two subgroup forces their span modulo two to have rank \(r\), so there is an integer \(r\)-row minor of odd nonzero determinant.
Hadamard bounds its absolute value by \((C\log n)^r\).
This bounds the finite order of \(H_{\mathrm{ab}}\) from above, since the full relation lattice contains the one generated by these rows.
Any nontrivial such abelian group would have a prime-order quotient with index below \(\kappa n/\log n\) for all sufficiently large \(n\).
The contradiction proves perfection with probability tending to one, using the diameter event in addition to the exponential index estimate.
Its implication for maps to arbitrary solvable groups needs no finiteness restriction because every subgroup of a solvable group is solvable.

The three stated 3-cycles generate \(A_5\) successively by transitivity and the size of the stabilizer of the new point.
The intersection arrows generate the \(C_7\) coordinate, and the three mixed inverse pairs generate the separate \(A_5\) coordinate.
The modified empty-extra types meet none of the mixed pairs, so the noncommuting right shifts there match initially uniform populations exactly.
At the ordinary intersection arrows the changes translate with the line indices.
The fine counts sum to the desired coarse histogram and preserve the original type totals.
The untouched fine baseline \(n/420\) is even, and the two modified nonidentity sheets have the respective additional forward masks \(D+1,D+2\).
In particular the two fine counts at color 3 are \(n/420+1\), with identity count \(n/420-6\).
Inversion on the second list just permutes the corresponding labels and sheets.
Each odd fine count forces an actual surviving original group label, since all repetitions of that group element contribute in the same fine bin.
The bounded changes preserve the positive turn estimates, geometric safeguards, and connectedness in the stipulated fixed finite planting law.
The perfect \(H\) lies in the commutator subgroup of the coarse kernel \(K\), whose commutator subgroup also maps onto the perfect quotient \(A_5\).
Hence \(K\) is perfect, all over-\(C_7\) solvable-kernel quotients are trivial over the base, and the simultaneous odd bins remain detectable in the stipulated nonsolvable quotient.
The complete fixed result is supported at its stated probability, group and label scopes.
