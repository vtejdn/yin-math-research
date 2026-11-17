---
author: Yin
---

# Forced single-letter discrepancies at polynomially many paired labels without a common exchange

## Statement

Fix the [thirteen-position four-line type and state counts](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers) at lamp modulus \(m=4t+1,\ t\ge1\), and the six active signed letters at the intersections of the four prescribed lines.
For every \(0<\gamma<\log(123)/(\log(123)+2\log(129))\), there exist safeguarded realizations on \(n\) vertices per side and an actually matchable subset of left color \(3\) with the following properties for all sufficiently large admissible \(n\) in the sequence below.
In particular one may take \(\gamma=0.33\).

For **each** active signed letter \(a\), the set contains configurations at at least \(n^\gamma\) distinct original group labels.
The labels chosen for different \(a\)'s are disjoint.
At each such label there are two disjoint six-vertex commutator blocks \(X,Y\).
Every \(X\)-mark carries exactly the one active letter \(a\), and every \(Y\)-mark carries no active letter.
All twelve marks have the same prescribed thirteen coordinates and the same original group label.
Every crossing pair has an actual equality proof, and every such proof uses each of the thirteen side and coarse-index positions.
The two block tensors are independent and the connecting bridge has zero binary central displacement.
Every one of the \(6!\) crossing matchings of the twelve marks therefore has the same rank-two total tensor.

Choose five marks in each block at every selected label, and let \(Z\) be their union.
This set has a perfect matching by original equalities.
In **every** such matching of \(Z\), each label assigned to \(a\) has an odd number of pairs on which **exactly \(a\)** differs among the six active stubs.
For every ordered pair consisting of an \(X\)-mark and a \(Y\)-mark, even from different chosen labels or different choices of \(a\), the entire simultaneous-step component has just two vertices.
There is a common step along one specified neutral ordinary letter, whose only common continuation retraces the step.
In particular no word can exchange marks between the two blocks in both directions, even at one fixed true label with a forced one-sided \(a\)-step.

The graphs have the source's exact prescribed vertex types and coarse counts, asphericity, torsion-free original group, root separation, the nonzero binary factors of zero product, and perfect coarse \(C_7\)-kernel.
The construction uses the additional [modulus-\(m^2\) graph states](Yin_C_A0079_v1.md#equal-prescribed-fine-states-in-genuine-source-tuples), which project to the prescribed counts.
The forcings here concern matchings of the actually pairable set \(Z\).
The [private-boundary argument for every pairing of the whole color](Yin_C_A0078_v1.md#statement) uses all occurrences at a group label, including vertices outside \(Z\).
Membership of these labels in that private-boundary set and complete erasure of the color are not established.

## Prescribing the active masks and their common neutral step

In the projective plane of order \(128\), choose an ordinary–ordinary neutral letter \(\sigma\) outside every line through two of the six active points.
There are at most \(\binom62\) such lines of size 129 and only three additional ordinary partners of extras to avoid among 16513 points.
The six lines \(L_a\) through \(\sigma\) and the respective active letters \(a\) are distinct, each carrying exactly one active point.
Choose another line \(L_0\) through \(\sigma\), carrying none.
Every \(L_a\) meets \(L_0\) exactly at \(\sigma\).
Choose also two distinct lines \(L'_+,L'_-\) through \(\bar\sigma\).
At each marked vertex prescribe its ordinary line and the empty extra set.
We will use \(L_a,L_0\) for the marks, and \(L'_+,L'_-\) for their respective \(\sigma\)-neighbors.
Each of these empty-extra types has a positive linear count at every fine state for the fixed modulus by the [balanced populations with bounded changes](Yin_C_A0079_v1.md#equal-prescribed-fine-states-in-genuine-source-tuples).

Use two neutral simple cycles \(U_1,U_2\) on the left and \(V_1,V_2\) on the right, disjoint within each side and based in its zero state.
Also use the word \(D\) from the [one-lamp cycle searches](Yin_C_A0072_v1.md#a-closed-graph-loop-changing-a-single-lamp) at modulus \(m^2\).
In the notation \(R=\lceil b\log n/\log64\rceil\) for the cycle-search depth, these cycle words and \(D\) have length \(O_t(R+1)\).
From coarse color \(3\), \(D\) adds one to each visible lamp modulo \(m^2\) and is trivial in the original group.
Its squared based value in the binary mixed group is the tensor of its two first-coordinate vectors, nonzero by the [square calculation](Yin_C_A0077_v1.md#making-every-position-change-with-a-central-value).
At coarse color \(3\) these vectors depend only on the named cycles and coarse indices.

For side-by-side marks on a chosen ordinary line \(L\), use the commutator
\[
       M(i,L)=[s U_i s^{-1},\, q V_i q^{-1}]
\]
with two neutral ordinary stubs \(s,q\) on \(L\).
Take them from distinct inverse pairs, avoid \(\sigma\), and avoid the inverse pairs of the end letters of both cycles.
The words are cyclically reduced, beginning in \(s\) and ending in \(q^{-1}\), and their tensor at coarse \(3\) is \(T_i=[U_i]_3\otimes[V_i]_3\).
The two tensors are independent since the respective cycles are edge-disjoint.
A vertex between two copies of \(M(i,L)\) has incoming stub \(q\) and outgoing stub \(s\), determining precisely \(L\).
Write \(M_+=M(1,L_a)\) and \(M_-=M(2,L_0)\) for the chosen active letter \(a\).
The latter can be fixed for all six choices of \(a\).

Let \(B\) be the freely reduced form of \(D^{2m}\).
It is nonempty since it changes each lamp by \(2m\) modulo \(m^2\).
Choose a neutral \(h_+\in L_a\) and a neutral \(h_-\in L_0\) from distinct inverse pairs, each away from \(\sigma\), the relevant end stubs of the commutators and the inverse pairs of the ends of \(B\).
All these choices are possible since each line has at least 120 neutral ordinary stubs.
Put
\[
       E=h_+B h_+^{-1}h_-B h_-^{-1},\qquad
       P_a=M_+^5 E M_-^5 .
\]
This gives a freely reduced word with twelve marks at the six copy boundaries in each block.
At the last \(X\)-mark the two required stubs are the terminal incoming stub of \(M_+\) and \(h_+\), both on \(L_a\).
At the first \(Y\)-mark they are \(h_-\) and the initial stub of \(M_-\), both on \(L_0\).
These pairs are distinct, and none of the prescribed path stubs at a mark is \(\sigma\).
The extra-set and two endpoint-line conditions will be imposed when reading the path.

Both halves of \(E\) are equality words with the same central tensor because \(D^{2m}\) is \((D^2)^m\) and \(m\) is odd.
The neutral outer guards leave the first-coordinate vectors of the based \(D\)'s unchanged, so their squares have the same value also at a different initial group label over coarse \(3\).
The sum of the two central tensors is zero.
The actual state change of \(E\) is \(4m\) in all thirteen positions modulo \(m^2\), which is nonzero at the higher modulus and zero modulo \(m\).
Both commutators leave every state fixed as words.
All twelve marks on an open lift of \(P_a\) therefore have one original label and one prescribed modulus-\(m\) state.
By the [one-position test for arbitrary certificates](Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate) applied to the actual higher auxiliary states, any cross-block proof needs all thirteen coarse positions.
The internal potentials at successive marks change by \(T_1\) and \(T_2\) respectively, while \(E\) contributes zero.
Counting the three odd indices on each six-mark block gives crossing-matching total \(T_1+T_2\), as in the [central matching computation](Yin_C_A0077_v1.md#matching-the-twelve-or-eighteen-marks).

## Separating labels by a free family of connectors

Choose a neutral ordinary \(p_0\in L_0\) from a different inverse pair from \(\sigma\) and the end stub of \(M_-\).
Choose a further neutral generator \(c\) and a set \(S\) of 62 neutral inverse pairs, all from different pairs and disjoint from that of \(p_0\).
For all freely reduced words \(w\) of the same length \(l\ge1\) in \(S\), use
\[
          C_w=p_0 w c w^{-1}p_0^{-1}.
\]
On the free-subalphabet event these \(D_0=124\cdot123^{l-1}\) connectors freely generate a subgroup of the actual group.
Indeed in the free group on \(S\) and \(c\), a reduced product of the conjugates \(w c w^{-1}\) and their inverses can first combine consecutive powers with the same \(w\).
Successive remaining \(c\)-powers are separated by a nonempty freely reduced word \(w^{-1}w'\) on \(S\), so they cannot cancel.
Conjugation of the family by \(p_0\) preserves freeness.
The [restricted-word proof for the subalphabet](Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction) applies in the present fixed auxiliary states because this 64-pair ordinary alphabet has reduced row sum \(127/129<1\), the word counts are unchanged, and the side-dependent embedding bound has a bounded state factor per multiplicity stage, as in [C65](Yin_C_A0065_v1.md#safeguarded-realizations).
The capped-picture extraction is the same one as in [C59](Yin_C_A0059_v1.md#capped-pictures-with-an-outer-segment-in-the-chosen-letters).
This group event holds with conditional probability tending to one simultaneously for the finitely many possible 64-pair alphabets, which permits choosing letters after the bounded-cycle searches.

Read each of the words
\[
                         P_a\,C_w\,P_a^{-1}                              \tag{1}
\]
on a simple open path in the left graph.
The connector joins two \(Y\)-marks at the two junctions.
There the incoming/outgoing stubs are \(p_0\) and the terminal incoming stub of \(M_-\), in either order, so both marks admit exactly line \(L_0\).
The end choice of \(p_0\) ensures free reduction of (1).
The two twelve-mark configurations have respective true labels \(g,g\pi(C_w)\), since \(P_a\) is null in the cone group.
They have the same two higher states by the reverse choice of the second path and neutrality of \(C_w\).
For exposure choose the same initial finer left state of coarse color \(3\) for all words (1).

For every one of the 24 marks, in addition expose its still unused \(\sigma\)-stub to a fresh vertex.
Require the new vertex to have empty extras and line \(L'_+\) for an \(X\)-mark or \(L'_-\) for a \(Y\)-mark.
After the exposures, at \((x,y)\) for any \(X\)-mark and \(Y\)-mark the common outgoing stubs consist precisely of \(\sigma\), because the two prescribed lines meet there and both extra sets are empty.
At \((x^\sigma,y^\sigma)\) only \(\bar\sigma\) is common, since the new prescribed lines are distinct through \(\bar\sigma\).
All these neighbors are fresh and are kept distinct from all marks, also on later paths.
Thus \((x,y)\) and \((x^\sigma,y^\sigma)\) constitute the entire simultaneous-step component.
Its two vertices are different and the unique edge reverses on the only next step.
This argument works across all the different active-letter configurations because \(L_0,\sigma,L'_+,L'_-\) are shared.
Reversing the order of the two coordinates yields the same conclusion.

## Fresh vertices, conditioning and the number of different labels

Here are parameters giving polynomially many distinct labels with all restrictions on one tuple.
Take \(l=\lfloor\lambda\log n\rfloor\), where \(\lambda>0\) is fixed below, so \(D_0=n^{\lambda\log123+o(1)}\).
Fix a sufficiently small \(0<b<1/8\) for the cycle-search exponent and budget \(O(n^{1-b/2})\), starting in the unconditioned modulus-\(m^2\) law.
The [cycle estimates](Yin_C_A0072_v1.md#a-closed-graph-loop-changing-a-single-lamp) give the two neutral cycles on each side and the two one-lamp cycles except with probability \(\exp(-\Omega(n^{b/2}))\), using this budget.
All the permitted turns have positive linear pools, and each nonempty matching block has size \(np/d'+O(1)\) with \(p=129/16513,\ d'=7(m^2)^{13}\).
There are constants \(C,C'\) depending only on the fixed modulus for which each word (1) has length at most \(CR+C'+2l\).
The extra 24 exposures per trial are a fixed additional cost.

Mark every touched vertex, including failed searches.
A fresh starting vertex of the required full \(L_a\)-type in its initial state can be chosen directly.
At unmarked turns the [uniform fresh-turn probability](Yin_C_A0072_v1.md#a-closed-graph-loop-changing-a-single-lamp) is at least \(1/300\) within the budget.
To reach a specified mark require the fresh partner to belong to its specified line with empty extras.
It then carries all required path stubs and \(\sigma\).
The same condition at the terminal \(X\)-mark of (1) needs only its incoming path stub.
The balanced population for *any* specified empty-extra line on the left in a single fine state is \(n(1-3p/2)/(16513d')\), perturbed by only \(O(1)\).
Among potential partners carrying a required incoming stub on the line, its asymptotic fraction is \((1-3p/2)/129>1/300\).
The same bound holds for each prescribed line at the 24 new neighbors.
Marking \(O(n^{1-b/2})\) vertices has removed only \(o(n)\) candidates from each relevant pool.
At a mark the simple fresh path used only its incident path stubs, which are different from \(\sigma\), and previous trials have not touched this vertex.
Thus its \(\sigma\)-stub is available, and the additional exposures go to distinct fresh partners with the stated conditional lower bounds.

Divide \(\lfloor n^{1-b/2}/(CR+C'+2l+25)\rfloor\) trials as evenly as possible among the \(6D_0\) words, retaining successes only after all the extra neighbors have been found.
Inside the connector all incoming and required next stubs are distinct ordinary points, prescribing one of the 129 equally weighted lines through the incoming stub.
Away from its two marked junctions no extra-set condition is imposed.
The full-line count in each prescribed state is \(n/(16513d')+O(1)\), while the incoming-stub population is \(129n/(16513d')+O(1)\).
Hence the success probability for each such turn, including freshness, is at least \(1/(129+\varepsilon)\) for any fixed \(\varepsilon>0\) once \(n\) is large.
There are at least \(2l\) of these interior turns, with all remaining path and neighbor conditions costing no more than \(CR+C'+24\) uses of the \(1/300\) bound after enlarging \(C'\) by a fixed amount.
Thus the conditional success probability is at least \(300^{-CR-C'-24}(129+\varepsilon)^{-2l}\).
The binomial lower comparison for each word has mean at least
\[
        n^{1-b/2-Cb\log(300)/\log64-\lambda(\log123+2\log(129+\varepsilon))-o(1)} .
\]
Choose \(\varepsilon>0\) sufficiently small and then \(\lambda\) such that \(\gamma/\log123<\lambda<1/(\log123+2\log(129+\varepsilon))\).
Put \(s=1-\lambda(\log123+2\log(129+\varepsilon))>0\) and choose \(b>0\) so small that \(b/2+Cb\log(300)/\log64<s/3\) and \(3b/8<s/2\).
The mean then exceeds \(n^{s/2}\) for large \(n\).
The probability of missing a word is at most \(6D_0\exp(-\Omega(n^{s/2}))\) by a union bound over the list.
Choose the girth constant with \(c_0\log(2d'|T_{\rm src}|/p)<b/4\) and \(2c_0\log132<1\), also small enough for the geometric inputs.
The [switching estimate](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges) gives reciprocal girth probability at most \(\exp(O(n^{3b/8}\log n))\), absorbed by the preliminary and later failure bounds.
Intersect after conditioning with the free-subalphabet event, root connectedness and all the safeguarded and perfection events of the [exact original-type refinement](Yin_C_A0079_v1.md#equal-prescribed-fine-states-in-genuine-source-tuples).
This establishes simultaneous existence of the displayed paths whose distinct trials, including their neighbors, are vertex-disjoint.

For a fixed \(a\), keep one such path per \(w\).
Make an edge between the true labels of its two configurations \(g,g\pi(C_w)\).
The \(D_0\) unoriented edges are different because an unoriented edge determines its connector value up to inversion and these free generators are distinct up to inversion.
They belong to a forest, since right multiplication by the free basis \(\{\pi(C_w)\}\) gives copies of its Cayley tree on left cosets of the subgroup it generates.
Root each finite tree and assign each edge its more distant endpoint.
This selects one of its two actually witnessed configurations per path with **distinct** true labels on all \(D_0\) paths for that \(a\).
Repeat for the six active letters.
By retaining \(\lfloor D_0/6\rfloor\) labels per letter successively one can make all six lists disjoint, since fewer than \(5D_0/6+1\) previously selected labels are ever unavailable.
Since \(\lambda\log123>\gamma\), the retained count exceeds \(n^\gamma\) for sufficiently large \(n\).
No probabilistic independence of group labels of disjoint graph paths is used.

Any actual pairing of the specified \(Z\) stays within each of the chosen group labels.
There are five marks of each type there, so the number of mixed pairs is odd by reducing the five \(X\)-endpoints modulo two.
Each such pair has unequal readability only at its designated active letter.
Conversely pairing all five across gives one actual perfect matching at every label, hence on their union.
For the original even blocks of six per type, there are also perfect internal matchings with *zero* active discrepancies on the twelve marks.
These two choices of marked set distinguish defects forced by odd class sizes in a partial problem from the stronger problem concerning a complete, exactly populated color.

## Assessment history

### Decision isolated-discrepancies

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:37 |
| status | proved |
| reason | Independent review verifies the construction with exact types and its restriction to the specified subset. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Polynomially many original labels with forced discrepancies on a pairable subset and isolated two-vertex simultaneous components. |
| argument | [Proof](#prescribing-the-active-masks-and-their-common-neutral-step) | Prescribed types and states, separated original labels, exposure estimates and the parity obstruction on each designated pair. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0122_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-isolated-discrepancies)
