---
author: Yin
---

# Required translates in both graph presentations of a color pairing

At 2026-11-17T03:21 UTC a separate agent reviewed the fixed [C65](../../claims/Yin_C_A0065_v1.md) for Sheng Yin.
The reviewer developed C51 and C61, independent inputs on the four-line counts and the regular-state entropy argument, and previously reviewed the side-specific action estimates in C60.
The reviewer did not develop C65, receive its proof-development dialogue or see an earlier verdict on it.
The nonregular stabilizer argument and its extension from the regular-state input were checked directly in C65.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [C65 statement](../../claims/Yin_C_A0065_v1.md#statement) | All thirteen choices separately on either forward side, partial and complete pairing counts, perfect actual coarse kernel, and remaining erasure question. |
| [Whole-argument finding](#whole-argument-finding) | [Two actions](../../claims/Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers) | Right multiplication on \(H_Y\backslash W\), single hidden lamp per side, order, increments and surjectivity from the rose. |
| [Whole-argument finding](#whole-argument-finding) | [Thirteen histograms](../../claims/Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms) | Integrality, signed line changes, compatibility in each block and the coordinatewise odd populations. |
| [Whole-argument finding](#whole-argument-finding) | [Arbitrary certificates](../../claims/Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate) | Signed displacements, based-loop conversion, conjugation slot, odd-bin accounting and multiplicities of terms. |
| [Whole-argument finding](#whole-argument-finding) | [Safeguards](../../claims/Yin_C_A0065_v1.md#safeguarded-realizations) | Within-block switching, bounded patterns for distinct transitive actions, connectedness and true cone-group conclusions. |
| [Whole-argument finding](#whole-argument-finding) | [Perfection argument](../../claims/Yin_C_A0065_v1.md#why-the-coarse-kernel-may-also-be-perfect) | Offset tests, normal stabilizers, generation, all transitive small-index actions, uniform entropy and integral determinant. |
| [Whole-argument finding](#whole-argument-finding) | [Exact coarse counts](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Where the changed lines meet the inverse pairs. |
| [Whole-argument finding](#whole-argument-finding) | [Side-specific safeguard input](../../claims/Yin_C_A0060_v1.md#geometric-safeguards-and-the-absence-of-group-quotient-certificates) | Why deterministic propagation in two fine actions suffices for the geometric inputs. |
| [Whole-argument finding](#whole-argument-finding) | [Alphabet-uniform entropy](../../claims/Yin_C_A0061_v1.md#an-entropy-inequality-independent-of-the-marking-alphabet) | The regular-state estimate and its nonregular interface. |
| [Whole-argument finding](#whole-argument-finding) | [Permutation count](../../claims/Yin_C_A0061_v1.md#vertex-markings-from-small-index-subgroups) | The small-index estimate after checking the nonregular interface. |
| [Whole-argument finding](#whole-argument-finding) | [Determinant](../../claims/Yin_C_A0061_v1.md#from-bounded-length-relators-to-perfection) | The integral determinant argument in the seven-state cover. |

## Whole-argument finding

Writing \(e_{T,j}\) for the unit vector at side \(T\) and slot \(j\), the semidirect law gives
\[
      (\ell,c)(e_{T,0},0)(\ell,c)^{-1}=(e_{T,c},0).
\]
The oriented intersection steps separately generate the rotation, and translating the two mixed steps generates all fourteen cyclic coordinates, including for composite \(m=4k+1\).
Left multiplication by \(H_Y\) changes exactly the \(Y\)-lamp at slot zero, regardless of coarse color.
Hence \(H_Y\backslash W\) has \(7m^{13}\) states and admits the required right action, with all other positions visible.
The coarse quotient alone follows directly from all graph loops having zero rotation.

For any selected type \(i\), summing the \(2k\) changes at \(i+1\) and \(2k\) changes at \(i+2\) with the change at the zero lamp restores \(7\mathbf1_{\{c=i\}}-1\).
Its sum over \(c\) is zero, and the prescribed divisibility gives integer, eventually positive populations on every originally occurring type.
The modified states move by right rotation to the states with identical lamps and shifted coarse color.
Each intersection arrow shifts both line indices by exactly that amount.
The private inverses lie on the same line, and neither the ordinary outside partners nor the extra stubs in the two mixed pairs occur among changed types.
Thus every matching equality survives at the fine-state level on each side.
The even baseline gives odd nonzero visible values precisely in \(J_1\) for \(D+1=\{1,2,3,5\}\) and in \(J_2\) for \(D+2=\{2,3,4,6\}\).
The three outside coarse colors have even total, so the remaining zero bin is even in each.
This proves the \(4k,2k,2k\) odd-bin counts at every visible position on each forward side.

For a loop at \(z\), the rooted loop \(w_z R w_z^{-1}\) fixes \(H_T\) under right multiplication, so its image is in \(H_T\).
Conjugating it by \(w_x a_i w_z^{-1}\) moves its permitted lamp from \(0\) to \(q_i\) with the positive shift displayed above.
Inverting the loop negates its value at that same slot.
For \(x,y\) of color \(c\),
\(\theta(w_y w_x^{-1})=(\ell_y-\ell_x,0)\).
Since \(w_xP\) and \(w_y\) end at the same graph state, the based path displacement differs from this value by a vector in \(H_Y\).
All thirteen visible positions therefore measure actual changes which a supplied free-word certificate can produce only by using the corresponding terms.
This argument permits arbitrary conjugators, arbitrary bases and both kinds of graph loop.
The inverse convention for the second group-ring factor only reflects the forward color and preserves the paired equalities.

At each position, a pair with equal values exhausts two vertices from one bin, and at most two initially odd bins can be accounted for by a pair with unequal values.
An unmatched vertex accounts for at most one.
This gives \(h_c\le u+2N_{T,q}\) separately, even when some counted terms evaluate trivially.
On a complete matching the lower bounds sum because every term occurrence has only one side and one slot.
They give \(26k\) occurrences for color 3 and \(13k\) in either other color, while a single pair may be counted at multiple slots.

For fixed \(k\) the two finite state sets have fixed equal size.
Every positive letter or turn pool changes by a bounded amount in each state, and every absent turn remains absent.
Words determine later states from an initial state on either side independent of the size of its stabilizer.
These facts verify the hypotheses of the within-block switching, small-set doubling and side-specific bounded-pattern comparisons.
Their girth probability cost is subexponential with the two stated bounds on \(c_0\), and the state factors in the bounded-chain comparison are constant at fixed \(k\).
The only invariant cuts constant on fine states are trivial by transitivity, giving the missing macroscopic connectedness estimate on each side.
The source implications then apply to the actual two rooted graphs in the same tuple.

For the perfection assertion, consider any transitive action of \(N_0\) of degree \(j>1\) descending to \(K\).
Every graph loop transported over any coarse offset acts trivially because all its root-based conjugates are defining relations in \(G\).
Consequently a vertex marking of each graph exists for every offset by transporting an initial mark along graph paths.
A section on the *fine states* would force every free word in \(S_Y=\theta^{-1}(H_Y)\) to fix the mark at the root state over that offset, since such a word fixes the fine root state.
All its successive transitions are among permissible complete fine-state transitions, irrespective of whether a particular vertex reads that whole word.
Transport along \(s^q\) from coarse zero to \(q\) gives the subgroup \(s^q S_Ys^{-q}\) fixing a point back at zero, with this order of conjugation for the right action.
The subgroup is normal in \(N_0\) since its image under \(\theta\) is one lamp coordinate subgroup inside the abelian base and it contains \(\ker\theta\).
On a transitive action a normal subgroup fixing one point fixes them all.
As \(Y,q\) vary, these fourteen coordinate subgroups generate the whole base and their preimages generate \(N_0\).
Thus the existence of a section at every side and shift would force the whole action trivial.
The argument allows nonnormal index-\(j\) subgroups of \(K\).

For the failing test, a modal assignment of marks to fine states violates a directed block relation, and each of its \(N+O(1)\) edges has at least one nonmodal endpoint.
Even if both endpoints lie in the same state, at least \(N/2-O(1)\) different vertices are nonmodal since a vertex occurs at most twice in that block.
The ordinary incidence bound within each state and the permutation-preserved end entropies give the C61 coefficient \(129/20-1>0\).
As \(N/n=(129/v)/d\), the resulting gap is positive at fixed \(k\), independently of \(j\le n\).
Bounded perturbations of type weights cost \(O((\log n)/n)\) per normalized entropy at these alphabet sizes.
The numbers of histograms, coarse-edge permutations, side/offset choices and factorial approximation errors have total logarithmic cost \(O(j\log n)\) for fixed \(k\).
Each candidate action that factors through \(K\) must realize the compatible marking on at least one side and offset without a section, so the stated union bound applies even when the failing choice depends on the proposed action.
The gap absorbs all \(j\le\kappa n/\log n\) at sufficiently small fixed \(\kappa\), including the subexponential conditioning cost.

The determinant bound uses the actual coarse cover with rank \(1+7(8258-1)\), independent of the two nonregular state sets.
Every graph fundamental relator lifts above every coarse color, and these lifts present the coarse kernel after abelianization.
The diameter bound supplies rows of norm \(O(\log n)\), and exclusion of index two supplies a full-rank odd minor.
Hadamard's bound on that minor gives \((C\log n)^{1+7(8258-1)}\) as an upper bound on the order of the finite abelianization.
For sufficiently large \(n\) at fixed \(k\), any prime quotient of a nontrivial such group would violate the small-index bound.
Thus \(K\) is perfect and cannot map onto a nontrivial solvable kernel, including in an infinite solvable extension over the coarse quotient.
The complete C65 statement follows at its fixed-\(k\) existence scope.
Its finite histograms constrain proofs of equalities and do not decide whether a whole outside color can erase in an exceptional source realization.
