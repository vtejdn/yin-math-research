---
author: Yin
---
# Labelled progression counts, expansion, and kernel dimension

At 2026-11-21T04:57 UTC a separate agent for Yin checked the statement and all proof sections of C_A0098_v2 against the three-label specialization of the [A0002 contract](../../tasks/Yin_T_A0002_v1.md#contract).
The reviewer took no part in developing either proof and received no exploration notes, proof-generation dialogue, author explanation or prior verdict on the v2 estimates.
The reviewer read the [earlier qualitative finding](Yin_R_A0134_v1.md#whole-finding) before forming the present findings and compared its [fixed statement and proof](../../claims/Yin_C_A0098_v1.md#argument) with the repeated argument.
The earlier independent finding supplies the exclusion of zero progressions and its exact-support consequence.
The present inspection checks the applicability of that input and independently checks the quantitative conclusions introduced in v2.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement and counts](../../claims/Yin_C_A0098_v2.md#statement-and-counts) | The hypotheses and all identities and inequalities (1)–(9), with the separate full-support condition for the kernel bound. |
| [Whole finding](#whole-finding) | [Local degree identity](../../claims/Yin_C_A0098_v2.md#the-local-degree-identity) | Local degrees, triple incidences and graph counts, retaining label multiplicity. |
| [Whole finding](#whole-finding) | [Cycles and boundary](../../claims/Yin_C_A0098_v2.md#good-cycles-and-the-exact-boundary) | Orientations at good vertices, direction of each translation, and the subtraction of internal edges of the exceptional set. |
| [Whole finding](#whole-finding) | [Exclusion of zero or one progression](../../claims/Yin_C_A0098_v2.md#excluding-zero-or-one-labelled-progression) | Applicability of the previously reviewed exclusion of zero and the new parity obstruction for one. |
| [Whole finding](#whole-finding) | [Both signs and cosets](../../claims/Yin_C_A0098_v2.md#both-signs-cosets-and-the-følner-estimate) | Normalization of the two-generator ratio, both signs, conjugation, orbit restriction and the endpoint cases. |
| [Whole finding](#whole-finding) | [Coefficient kernel](../../claims/Yin_C_A0098_v2.md#coefficient-kernel-deficiency) | Connected components, the support of each contracted equation, rank, rounding and the case of two progressions. |
| [Whole finding](#whole-finding) | [Quantitative scope](../../claims/Yin_C_A0098_v2.md#scope-of-the-quantitative-conclusion) | The fixed-ratio amenability implication, the path-length count and the application to exact supports. |

## Whole finding

For a fixed colour, the translation has infinite order and restricts on the finite set to a union of paths, with isolated vertices allowed.
A degree-two vertex is the middle of exactly one oriented three-term progression.
Each edge is distinguished by its label pair and its initial vertex, which together specify the output.
At a column \(x\), a double output involving \(x\) contributes one to the sum of its three colour degrees, and a triple output contributes two.
Counting once for each of the three left labels therefore gives \(3+r_x=3+p_x-i_x\).
This proves the local identity and puts every column of a triple fiber in \(K\).
Summation over columns gives \(P-I=3Q\), while summation within one colour gives \(2E_i=N+P_i-I_i\).
The union bound \(s\le P\) and \(I\ge0\) give the remaining inequalities in (2).

At a good column the three outgoing incidences orient three distinct pairs, with one outgoing arrow per label.
Thus the possible orientations are the two directed cycles.
For the ordered pairs \(12,23,31\), a positive endpoint uses \(t_i\) and a negative endpoint uses \(t_i^{-1}\).
At a good neighbour the shared pair reverses and determines the opposite orientation.
Translation is injective, so each edge from \(K\) to a good vertex accounts for exactly one element of the corresponding symmetric difference, whether the good endpoint is positive or negative.
The degree sum on \(K\) is \(3s+3Q\).
Each internal double fiber contributes one edge and each triple fiber contributes its three pair edges.
Removing twice the \(J+3Q\) internal edges yields \(3s-3Q-2J\), as in (4).
Coincidence of two translation steps leaves their label pairs distinct in both counts.

The qualitative input applies with the same hypotheses because a progression for an inverse step becomes one for the chosen step by reversing its order.
In the case \(P=0\), (4) also gives the bijections \(t_i B_+=B_-\) used in the earlier proof.
Both sets are nonempty since their union is \(B\) and these bijections give equal cardinalities.
The finite stabilizer argument then applies with \(t_3t_2t_1=1\) in precisely that order.
For \(P=1\), the local identity and \(P-I=3Q\) force the sole degree-two and isolated occurrences onto the same column in different colours.
The three differences \(P_i-I_i\) would be \(1,-1,0\) in some order, whereas all are congruent to \(N\) modulo two.
This verifies the strengthening to \(P\ge2\).

Write \(\tau_i=t_i^\varepsilon\) for the choice of the larger class \(U\).
In either sign \(\lvert\tau_i U\triangle V\rvert=d_i\), since left translation preserves symmetric-difference size.
The triangle inequality bounds the sum of the two generator boundaries by \(\sum_i d_i+d_b\le(4/3)\sum_i d_i\).
Dividing by \(\lvert U\rvert\ge(N-s)/2\) gives exactly (5), and (6) follows when \(P<N\).
For any two bases \(a,b\), the identity \(t_b^{-1}t_i=(t_a^{-1}t_b)^{-1}(t_a^{-1}t_i)\) gives one subgroup inclusion, and exchanging \(a,b\) gives the reverse inclusion.
For the negative sign, conjugating \(q_i=t_bt_i^{-1}\) by \(t_b^{-1}\) gives the inverse of \(t_b^{-1}t_i\), whose symmetric-difference size on each finite set equals that of the positive generator.
Thus each sign has the same two-term expansion infimum \(h_b\) after identifying its subgroup with \(H\).
The right cosets of the acting subgroup are invariant under its left translations and partition \(U\) into intersections with those cosets.
For a right coset with representative \(g\), right multiplication by \(g^{-1}\) transports the intersection into the subgroup and commutes with the left translations.
The ratio on \(U\) is a size-weighted average of the piece ratios, so some piece has at most the bound (5), and each has ratio at least \(h_b\).
Using \(h_*\le h_b\) and rearranging gives (8).
If \(s=N\), (4) makes the right side of the first inequality in (8) zero, giving the same conclusion without division by \(N-s\).
For fixed steps, a sequence with \(P/N\to0\) has a subsequence with fixed base and yields finite subsets of \(H\) with vanishing relative boundary on each of its two generators.
The triangle inequality extends this to each fixed word and hence to finite collections of words, as required by the Følner criterion.

Restricting to a full collision component preserves all representations of each output there.
Every progression belongs to one component because both of its consecutive pairs are collision edges.
Consequently \(P\ge2c\), and adding each triple to the graph of double fibers merges at most three components, giving \(c_2-c\le2Q\).
For the rank estimate, division by the given nonvanishing witness makes the double-fiber equations equalities on their endpoints.
The remaining variables are indexed by the \(c_2\) components.
If a triple meets two such components, its singleton weight is nonzero and its combined pair weight is the negative of that weight in every characteristic.
If it meets three components, all three coefficients remain nonzero.
Thus precisely the triples that join components yield nonzero equations, and their supports connect the variables into \(c\) components.
In one such component on \(m\) variables, each equation reaching a new variable from the reached set adds at most two variables.
Choose a new variable at every step.
In the square minor on these equations and variables in selection order, all entries above the diagonal are zero and the diagonal entries are nonzero.
The rank on this component is therefore at least \(\lceil(m-1)/2\rceil\), also valid for an isolated variable.
Summing component nullities gives the first bound of (9).
The inequalities \(c_2-c\le2Q,\ 2c\le P,\ 3Q\le P\) give the rest.
If \(P=2\), there is one full component and \(Q=0\), so all coordinates after division by the witness are equal and the kernel has dimension exactly one.

An oriented path on \(\ell\) vertices admits \(\max(\ell-r+1,0)\) starting points for a run of \(r\) vertices.
The three-term estimates alone therefore provide no specified longer run.
In the complex group algebra, as over any field, a singleton output of two exact supports has a nonzero coefficient.
This places a prospective three-label zero product within the hypotheses and supplies the required full-support vector for its own coefficient map.
All estimates hold at this scope.
Existence of a zero product and the general A0002 conjecture remain open here.
