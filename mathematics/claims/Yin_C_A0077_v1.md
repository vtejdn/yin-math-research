---
author: Yin
---

# Two six-vertex blocks with a full crossing matching and a computable central product

## Statement

Fix \(t\ge1\) in the [thirteen-position four-line law](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers), with lamp modulus \(m=4t+1\).
For every fixed \(0<\delta<1\), a sufficiently small fixed positive logarithmic girth constant gives the following configurations with probability tending to one conditional on girth.
Two disjoint six-vertex blocks over left color \(3\) have independent internal tensors \(T_1,T_2\).
Their twelve marked vertices have one and the same original group label.
Every one of the \(6!\) matchings between the two blocks, using only cross-block pairs, has explicit central witnesses, and **each of its six pairs requires relators from all thirteen positions in any proof**.
Every one of the \(11!!\) internal or crossing perfect matchings of these twelve vertices has witnesses with the same rank-two central tensor \(T_1+T_2\).
If the whole color admits a true complete pairing, all these choices extend to the color with a common matching of the complement.
These are full crossing matchings of the designated twelve vertices, and the extension makes no existence assertion for a completely erased color.

On the same type of realization a chain of three disjoint six-vertex blocks admits two all-position bridges with the same directed change of visible coordinates and different computable central values, of ranks one and two.
All eighteen marks again have the same true label.
Every matching of the eighteen marks along the chain has the same rank-three total.
In particular different bridge values in one actual label class still do not force different matching products.
For each of the two fixed words used below at least \(\lfloor n^{1-\delta}\rfloor\) disjoint simple open lifts may be required, with the source types, protected roots, asphericity, torsion-freeness, binary zero product and perfect coarse kernel of C65.

## Making every position change with a central value

Use the word \(D\) constructed from the two one-lamp cycles \(L_A,L_B\) in [C72](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges).
From any coarse-\(3\) start it adds one in all thirteen visible coordinates, and it is trivial in the original group.
In the mixed homomorphism of [C66](Yin_C_A0066_v1.md#the-finite-tensor-calculation) based at such a start, its two first coordinates are
\[
       a_D=\sum_{q\in C_7\setminus\{0\}}[L_A]_q,\qquad
       b_D=\sum_{q\in C_7}[L_B]_q .
\]
Indeed \(D\) uses a single positive conjugate per position, with the conjugator of coarse increment \(q-3\) and a graph-loop base of coarse color zero.
Each completed move has zero coarse increment, so the next move has the same initial coarse color.
The simple one-lamp loops have nonzero binary homology.
The summands at the displayed distinct indices are independent within each side.
Although the central coordinate of \(D\) is not needed, the square of any triple \((a,b,c)\) in the mixed group is exactly \((0,0,a\otimes b)\).
Consequently the bridge \(D^2\) has central tensor
\[
                       T_D=a_D\otimes b_D\ne0 .
\]
Its state change is now \(+2\) at every position, nonzero modulo \(4t+1\).
Taking squares gives balanced explicit certificates, since the based word repeats each of its named factors twice.
The square operation takes place in the central test, while the necessity of using every slot follows from the independent state changes in the finite coset actions, also for unbalanced alternative proofs.

Choose four of the neutral independent commutators \(M_i=[s_iU_is_i^{-1},V_i]\) from C72, cyclically reduced as in the [six-vertex construction](Yin_C_A0075_v1.md#genuine-bridges-between-disjoint-six-vertex-blocks).
Their tensors at coarse color \(3\) are \(T_i=[U_i]_3\otimes[V_i]_3\).
The four first-side factors and \(a_D\) are linearly independent, as are the second-side factors and \(b_D\), by the disjoint neutral cycles and the additional nonzero summands of the lamp cycles.
Let \(E_0\) be a neutral-guard conjugate of the freely reduced word \(D^2\); let \(E_1\) be a neutral-guard conjugate of the freely reduced word \(D^2 M_4\).
Neither reduction is empty by its state change.
Reading these words from coarse \(3\) gives the central values \(T_D,T_D+T_4\) respectively, with the same \(+2\) change at every position.
The neutral guards preserve the indices in the square and commutator formulas, and each word remains null in the original group.
The second tensor has rank two by the independence just proved.

## Matching the twelve or eighteen marks

First read the simple open path
\[
                           M_1^5 E_0 M_2^5 .
\]
Number the six ends of the successive commutator copies \(x_0,\ldots,x_5\) in the first block and \(y_0,\ldots,y_5\) in the second, including the start of each block.
All twelve true group labels agree since each completed word is a relation.
The path from \(x_i\) to \(y_j\) has tensor
\[
             ((5-i)\bmod2)T_1+T_D+(j\bmod2)T_2.
\]
One may base every subpath by its prefix from the initial mark.
All complete commutator and bridge contributions are central, so the stated formula survives inversions and changes of rooted graph paths.
Every crossing changes all thirteen slots by two or minus two, independent of its choice of path or proof.
The [single-position certificate argument](Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate) forces every position in a proof for that pair.
For any matching by a bijection between the blocks, each of the two endpoint index lists contains three odd marks, and \(T_D\) occurs six times.
The total is \(T_1+T_2\).
In fact the potentials \(iT_1\) and \(5T_1+T_D+jT_2\) give every pair witness along the path by taking the difference of the endpoint potentials.
Their sum over all twelve marks proves the assertion for every perfect matching, including the \(15^2\) using only internal pairs.
The [alternating path extension](Yin_C_A0070_v1.md#extending-witnessed-matchings-on-even-blocks) gives the common complement whenever there is a full matching of the color.

For the second assertion use the path
\[
                      M_1^5 E_0 M_2^5 E_1^{-1} M_3^5 .
\]
Orient both bridges from the outer blocks toward the middle, so their lamp changes agree.
The simple path again makes all marks distinct and each completed segment is trivial in the original group.
Give each block its initial offset from the prefix path and local potential \(iT_j\) at its \(i\)-th mark.
Every marked displacement is central.
In the total of a matching each offset occurs six times and each \(T_j\) occurs three times, so the answer is \(T_1+T_2+T_3\) irrespective of the two different bridge values.
This construction displays the bridges on a chain. It does not supply an independently forced additional edge closing that chain with an inconsistent value.

Finally, both displayed words can be chosen freely reduced: choose each neutral guard off the end-letter inverse pairs of its adjacent commutator powers and of the freely reduced bridge it guards.
Their length is at most \(C R+C'\) for the logarithmic search radius \(R\) of C72, with \(C,C'\) depending only on the fixed lamp modulus.
Add these two words to its list of \(O(n^{a/4})\) open-path searches from the designated color-\(3\) state, taking \(a>0\) sufficiently small for the enlarged length coefficient.
The [fresh-turn estimate and girth-conditioning calculation](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges) give success probability at least \(300^{-(CR+C')}\) per trial within the \(O(n^{1-a/2})\) exposure budget.
The mean per word exceeds \(n^{1-\delta/2}\) for large \(n\), and the cycle-search failure \(\exp(-\Omega(n^{a/2}))\) and open-path failure probabilities absorb the conditioning cost \(\exp(O(n^{3a/8}\log n))\).
This proves the claimed number of actual configurations in the same nonregular state law.

## Assessment history

### Decision central-all-position-crossings

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:04 |
| status | proved |
| reason | Independent review verified the squared bridge tensor, all twelve-vertex matchings, the different bridge values on three blocks and exposure in the original model. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Central bridges using all thirteen positions, full crossing matchings on twelve marks and the common totals on two or three blocks. |
| argument | [Proof](#making-every-position-change-with-a-central-value) | Squaring and decorating the bridge, counts and values of the matchings, extension and probabilistic realization. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0113_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-central-all-position-crossings)
