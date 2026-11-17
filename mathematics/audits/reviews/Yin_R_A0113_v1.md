---
author: Yin
---

# Central values of all-position bridges and the matchings they witness

At 2026-11-17T04:03 UTC an agent outside the development of Yin_C_A0077_v1 independently reviewed its fixed statement and both proof sections for Sheng Yin.
The reviewer had previously checked the C66 group law and the C72 and C75 path constructions.
The reviewer examined the square of the bridge, the new matching invariants and the simultaneous sampling argument without receiving development dialogue, author explanations or previous findings on C77.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0077_v1.md#statement) | Two disjoint blocks, all-crossing and arbitrary perfect matchings of twelve marks, the eighteen-mark chain, tensor ranks and simultaneous realizations. |
| [Whole-argument finding](#whole-argument-finding) | [Square of the bridge](../../claims/Yin_C_A0077_v1.md#making-every-position-change-with-a-central-value) | All thirteen coarse deck indices, first-coordinate independence, central square of a noncentral element, balanced witnesses and two bridges of distinct rank with the same lamp change. |
| [Whole-argument finding](#whole-argument-finding) | [Matchings and actual lifts](../../claims/Yin_C_A0077_v1.md#matching-the-twelve-or-eighteen-marks) | Endpoint tensors for individual witnesses, counts and total tensors, orientations, guards, conditional common complement, trial bounds and girth conditioning. |
| [Whole-argument finding](#whole-argument-finding) | [Mixed group](../../claims/Yin_C_A0066_v1.md#the-finite-tensor-calculation) | First-layer convention for conjugated roots, omitted \(A\) identity summand and the central elementary abelian group law. |
| [Whole-argument finding](#whole-argument-finding) | [Original bridge and matching law](../../claims/Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges) | One positive conjugate at each visible side/index pair, actual mixed and neutral cycles, and uniform fresh-turn sampling after their exposure. |
| [Whole-argument finding](#whole-argument-finding) | [Proof positions](../../claims/Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate) | Necessity of a relator occurrence of the specified side and index for each nonzero visible change, with arbitrary conjugators. |
| [Whole-argument finding](#whole-argument-finding) | [Full-color extension](../../claims/Yin_C_A0070_v1.md#extending-witnessed-matchings-on-even-blocks) | Common complement when a full true matching of the color exists. |

## Whole-argument finding

Every one-slot term of \(D\) starts at coarse color three, adds conjugator rotation \(q-3\), and bases its graph loop at coarse color zero.
Thus its first-layer index is exactly \(q\), once for each of the six nonzero \(A\) indices and all seven \(B\) indices.
The two sums \(a_D,b_D\) are nonzero in the respective direct sums because the lamp cycles are simple.
The group law gives \((a,b,c)^2=(0,0,a\otimes b)\), so the central coordinate of the unsquared bridge cancels and the square has the nonzero rank-one tensor \(T_D\).
The based square repeats exactly the same conjugated relators, making a balanced certificate even if their original free-word expression tightens.
The state increment is twice the all-ones vector, nonzero at every visible slot for \(m=4t+1\ge5\).
These slot changes apply to arbitrary alternative certificates for the same endpoints.

The neutral-cycle factors in \(T_1,\ldots,T_4\) are independent in each of the two index-three summands.
Each of \(a_D,b_D\) has a nonzero component outside the corresponding index-three summand.
Thus adding \(T_4\) to \(T_D\) has rank two.
Conjugation by neutral guards leaves all coarse first-coordinate indices in the square and commutator calculations unchanged and acts trivially on the lamp coordinates.
This verifies the central bridge values for \(E_0,E_1\) without requiring a central value for \(D\).

In \(M_1^5 E_0 M_2^5\), each of the twelve marks has the same original label since the completed words are cone relations.
The two fine states differ by two at every visible position.
The subgroup displacement along the path from \(x_i\) to \(y_j\) is central with value \((5-i)T_1+T_D+jT_2\) over \(\mathbb F_2\).
Every bijection between the two six-element blocks therefore supplies a full crossing matching by explicit witnesses, and every single crossing requires all thirteen slots.
For any of the \(11!!\) matchings, each endpoint potential occurs exactly once.
The constant bridge offset occurs six times and every block has three odd indices, yielding \(T_1+T_2\), of rank two.
If a full matching of the color is supplied, the alternating-path construction leaves one common complementary matching for every internal choice on these twelve marks.

In \(M_1^5 E_0 M_2^5 E_1^{-1} M_3^5\) both bridges read with the positive lamp change when oriented from an outer block toward the middle.
Their central values, of ranks one and two, are unchanged by inverse reading.
Every marked pair has a central witness along the chain, and each initial block offset occurs six times in the sum over any matching.
The total is \(T_1+T_2+T_3\), of rank three by independence in both axes.
The two remote endpoints belong to distinct outer blocks.

After reduction the bridges are still nonempty by their lamp change, and the neutral guards can avoid the adjacent end-letter inverse pairs in both full words.
The resulting freely reduced words have length \(CR+C'\) or less with constants fixed by the lamp modulus.
Including these two templates in the trial list and choosing \(a\) after \(C\) preserves the lower mean \(n^{1-\delta/2}\) for fresh simple lifts.
The cycle-search failure exponent \(n^{a/2}\) and the open-lift failure exponent dominate the logarithm \(O(n^{3a/8}\log n)\) of the girth-conditioning cost.
The required copies consequently occur on one tuple with the C65 safeguards.
The complete matchings established here cover the twelve or eighteen marked vertices, and full erasure of their color retains its separate existence condition.
