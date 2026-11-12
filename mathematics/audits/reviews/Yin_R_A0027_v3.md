---
author: Yin
---
# Independent review of vertex-local rotations and expected support

Review performed at 2026-11-11T19:14 UTC for Yin.
The reviewed object is the whole fixed [L_A0023 v3](../../ledger/Yin_L_A0023_v3.md), including all nineteen displayed equations, complete kernels, simultaneous additivity, maximal expected support, the stated coupled-rotation obstruction and the exact support compression.
This review adds evidence for the new rotation argument in the existing R_A0027 family and leaves the earlier findings at their actual physical inputs.

## Review arrangement and inputs

A separately assigned reviewer outside substantive proof development read the fixed candidate and its necessary mathematical inputs directly.
No development draft, proof-generation dialogue, author explanation or substantive development summary was supplied or consulted.
The assignment supplied the exact fixed target, review scope, repository instructions and the main agent's operational metadata.
The reviewer reconstructed the candidate's arguments and reported initial findings before consulting [R_A0027 v2](Yin_R_A0027_v2.md#whole-candidate-finding).
That subsequent comparison disclosed no discrepancy at the unchanged eight-square input.

The mathematical inputs actually read were the whole [L_A0023 v2](../../ledger/Yin_L_A0023_v2.md), the free-boundary and support arguments in [L_A0023 v1](../../ledger/Yin_L_A0023_v1.md), the whole [C_A0007 v4](../../claims/Yin_C_A0007_v4.md), its [v3 boundary interface](../../claims/Yin_C_A0007_v3.md#statement), the retained [BBL21 general-base source inspection](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), and the [T_A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).
The C_A0007 result and the external analytic theorem remain accepted inputs at their recorded scopes.
This review checks their applicability to the compressed matrix; it is not a new independent audit of the whole C_A0007 proof or the source's analytic foundations.
The checking method was exact ordered matrix calculation, complete kernel equations, finite-support tree reasoning, reduced-word support and positive-operator inequalities.
No numerical evidence, generic free-variable rank assumption or formal proof verification is used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [Whole L_A0023 v3](../../ledger/Yin_L_A0023_v3.md) | Whole fixed candidate, including all constructions, complete analytic and polynomial kernels, exact dimensions, support maxima, comparison, source applicability and continuation limits. |
| [Whole-candidate finding](#whole-candidate-finding) | [Inputs and outcome](../../ledger/Yin_L_A0023_v3.md#inputs-and-outcome) | Exact free amalgam, unnormalized traces, eight-square input, nullity six, polynomial rank five, expected rank eleven and the stated compressed correction. |
| [Whole-candidate finding](#whole-candidate-finding) | [Four rotations](../../ledger/Yin_L_A0023_v3.md#the-four-rotations-and-additivity) | Equations (2)--(4), two-sided polynomial unitarity and simultaneous preservation of a selfadjoint vertex decomposition. |
| [Whole-candidate finding](#whole-candidate-finding) | [Complete kernels](../../ledger/Yin_L_A0023_v3.md#complete-kernel-and-finite-witnesses) | Equations (5)--(9), necessary and sufficient analytic parametrization, complete free polynomial module and its analytic span. |
| [Whole-candidate finding](#whole-candidate-finding) | [Exact expected support](../../ledger/Yin_L_A0023_v3.md#exact-expected-support) | Equations (10)--(12), coefficient extraction, maximal finite-witness support and the identical support of the actual expected kernel projection. |
| [Whole-candidate finding](#whole-candidate-finding) | [Terminal obstruction](../../ledger/Yin_L_A0023_v3.md#the-terminal-sum-and-difference-including-a-coupled-rotation-obstruction) | Equations (13)--(15), optional boundary rotations, arbitrary additional zero coordinates and the exact restricted vertex-unitary quantifiers. |
| [Whole-candidate finding](#whole-candidate-finding) | [Support compression](../../ledger/Yin_L_A0023_v3.md#a-single-support-compression-and-its-exact-correction) | Equations (16)--(19), independently invertible product constraints, corner rank four, corner nullity seven and the full-support finite witness. |
| [Whole-candidate finding](#whole-candidate-finding) | [Continuation boundary](../../ledger/Yin_L_A0023_v3.md#continuation-boundary) | Exact residual obstruction, absence of a general discarded-rank formula and separation from the full Task contract. |
| [Whole-candidate finding](#whole-candidate-finding) | [Eight-square input](../../ledger/Yin_L_A0023_v2.md#an-explicit-additive-eight-square-matrix) | Rechecked entries, auxiliary inverse, rank six, analytic nullity two and complete polynomial generator used by v3. |
| [Whole-candidate finding](#whole-candidate-finding) | [Free-boundary input](../../ledger/Yin_L_A0023_v1.md#an-additive-noncentral-boundary-matrix) | Actual free-group analytic rank one of the boundary row and vanishing finite polynomial kernel. |
| [Whole-candidate finding](#whole-candidate-finding) | [Normalization statement](../../claims/Yin_C_A0007_v4.md#statement) | Applicability of the accepted theorem to the eleven-coordinate additive compression and its displayed full-support witness; no fresh whole-theorem review. |
| [Whole-candidate finding](#whole-candidate-finding) | [General-base source interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) | Reused inspected version, general von Neumann base and bounded-inverse hypothesis of the analytic input reached through C_A0007 v4. |

## Whole-candidate finding

The whole fixed candidate is mathematically supported at its stated scope.
No unresolved proof gap was found.
Its calculations improve the polynomial expected-support rank of this additive realization, prove the precise residual edge relation and independently compute the compression correction.
They do not establish a new group class or complete the general torsion-free Atiyah Task.

### The fixed input and the simultaneous rotations

For the actual group \(F(z,a,b)\), the equation \(A^*f=0\) forces square-summable \(f\) to be constant on infinite \(a\)-orbits and hence zero.
Thus the row \(\partial=(A\ B)\) has rank one and analytic kernel dimension one.
For finite group-ring coefficients, its kernel equation is a finitely supported cycle on a free Cayley tree in each right coset of \(F(a,b)\).
Leaf removal gives zero polynomial kernel.
These are actual operator and finite-support facts, rather than an injectivity assumption for arbitrary torsion-free group rings.

The unit triangular block of L_A0023 v2 has the displayed finite two-sided inverse.
Its Schur congruence gives rank six and nullity two for \(K\).
Solving the rows also gives exactly the candidate's equation (5): the boundary rows force \(y_1=t_2\), the remaining equations force both multipliers to vanish, and the two product constraints give \(t_1=bf\), \(t_2=abf\).
The only additional analytic freedom is \((\eta,\theta)\in\ker\partial\).
The finite-support calculation makes the stated single column the complete polynomial kernel generator.

Multiplying each displayed \(U_i\) by its adjoint in both orders gives the identity.
The four pairs are disjoint, so their simultaneous product is a finite bounded unitary and transports the whole kernel of \(K\oplus0_4\).
It preserves rank six and raises nullity from two to six.

The four selected old coordinates have no matrix entries between them.
The only incident entries in rows \(2,7\) belong to the first vertex, and those in rows \(3,6\) belong to the second, exactly as shown in (4).
After simultaneous rotation every new nonzero entry is obtained by multiplying one of these entries on one side by an element of that same vertex ring.
No nonzero entry undergoes multiplication by factors from two different rotated pairs.
Selfadjointness is preserved by congruence, and splitting adjoint pairs together therefore gives the asserted selfadjoint vertex decomposition.

### Complete polynomial and analytic kernels

Applying \(U^*\) to the complete input kernel and four free coordinates gives every coordinate in (6)--(7), including the signs of the new boundary coordinates.
The inverse \(U\) proves necessity and sufficiency and the uniqueness of all parameters.
For polynomial vectors, the free-boundary parameters vanish by the tree calculation.
Consequently the five columns in (8) generate the complete right polynomial kernel module freely, not just a selected submodule.

Before rotation the first column has six unitary entries and the four remaining columns are distinct new constant coordinate columns.
Their inner products are therefore exactly
\[
W^*W=\operatorname{diag}(6,1,1,1,1).
\]
This equality also proves that their analytic range is closed and has dimension five.
The analytic kernel has dimension six, so the transported free-boundary component contributes precisely the missing analytic dimension.

### Maximal expected support

The distinct words \(1,a,b,ab\) occupy distinct cosets \(Hu\), and each \(g_i\) lies outside \(H\).
Coefficient expectation deletes all cross terms between these words in \(w_0w_0^*\), and deletes the off-diagonal term in each \(w_iw_i^*\).
This gives exactly (10).

The last sum in (10) spans all eight rotated coordinate directions.
Modulo that span, \(v_1,v_b,v_{ab}\) give the three independent directions \(e_0,e_4,e_1+e_5\).
All eleven directions are present and their orthogonal complement is exactly \(\mathbb C(e_1-e_5)\).
Thus (11) has the stated rank and support, with no missing additional edge direction.

Every analytic kernel vector satisfies \(x_1=x_5\), hence \(p\le q\).
The closed witness range lies in that kernel and its squared operator norm is six, giving
\[
WW^*\le6p,\qquad C\le6E_H(p)\le6q.
\]
Since \(q\) is constant and \(\operatorname{supp}C=q\), these inequalities give \(\operatorname{supp}E_H(p)=q\).
The same terminal row annihilates every polynomial witness, irrespective of its right coefficients.
Bimodularity bounds each expected Gram by the same support corner, and the displayed \(W\) attains rank eleven.
This proves both maximality claims and the disappearance of the old multiplier-coordinate annihilators.

### Terminal relation and the stated coupled families

Expanding the quadratic form of the eight-square matrix gives (14), with the ordered product constraints shown there.
The change to \(p_+,q_-\) makes \(y_1-t_2=\sqrt2q_-\).
Since \(ry\) has no \(y_1\) term, \(p_+\) couples only through the second multiplier, while the mixed boundary row remains attached to \(q_-\).
Changing only \(p_+\) leaves the existing kernel equation \(q_-=0\).

After the multiplier rotations, the old \(y_3\) row still meets the proposed \(V\)-block only in \(q_-\).
Without the optional \(y_3\) rotation its entry there is \(\sqrt2B^*\); with that rotation the first output row has entry \(B^*\).
Thus the assumption of additive output really forces \(B^*u_j\in\mathbb CG_1+\mathbb CG_2\) for every entry of \(e_{q_-}^*V\), without a possible cancellation from another entry in that row.

For \(g\in G_1\setminus H\), the group element \(b^{-1}g\) lies outside both vertices.
Different \(g\)'s give different such words, and none is supplied by \(-u\) or by \(b^{-1}h\) with \(h\in H\).
This proves both directions of (15).
The row \(e_{q_-}^*V\) therefore lies in the edge group ring.
Its product with its adjoint is one, so it remains nonzero, and it annihilates every transformed analytic kernel vector.
Bimodularity preserves this nonzero edge annihilator under expectation.
The argument permits any stated additional zero coordinates and the two optional boundary rotations.
Its symmetric version uses \(A^*\) and the untouched first-vertex row.
It does not extend the exclusion to simultaneous operations changing both available boundary rows.

### Compression, comparison and source limits

The constant projection \(q\) commutes with \(U\), since all four rotations fix the terminal coordinates.
It is therefore legitimate to compute the compressed rank before rotation.
Setting \(q_-=0\) removes the whole mixed boundary term and leaves exactly the two constraints in (16).
The displayed two-column submatrix of \(R\) has the finite inverse in (18), verified in both multiplication orders.
Hence \(R\) is onto, \(R^*\) is one-to-one and the selfadjoint matrix with off-diagonal blocks \(R,R^*\) has rank four.

Its kernel equations force both multipliers to vanish, \(t_1=by_0\) and \(p_+=\sqrt2ab y_0\), with \(y_2,y_3\) free.
There are three kernel dimensions in the seven-coordinate unrotated compression and four further free zero coordinates.
Thus the eleven-coordinate corner has nullity seven and rank four, exactly one more kernel dimension than \(\widehat K\).
Counting in that corner is essential; treating the discarded coordinate as another zero in size twelve would give a different nullity.

The original \(W\) lies in the corner and is killed by the compressed matrix.
Constant orthonormal identification of the corner with eleven coordinates transports (10)--(11) to a full-support expected Gram and preserves both finite vertex summands.
All premises of the accepted C_A0007 v4 statement are therefore met.
That theorem's rectangular normalization supplies the bounded-inverse expected-kernel hypothesis needed by the retained BBL21 general-base interface; full support alone is not silently substituted for the analytic hypothesis.

The input's free-boundary rank and the explicit unit pivots independently determine this correction.
The rotations supply no general discarded-rank formula for an unknown input.
The comparison with the word-chain failure is consequently valid, while the claimed advance remains a calibration in a free group.
The source interface reuses the recorded arXiv v2 theorem statement and applicability inspection and does not assert a new original-source audit, a new analytic theorem or historical priority.
The exact Task contract still quantifies over every torsion-free discrete group and every finite complex group-ring matrix.
Neither that coverage nor a general full-support witness construction is supplied by this candidate.
