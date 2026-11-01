---
author: Yin
---

# Three free square-zero factors: scalar polynomial center and positive-word bounded reconstruction

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Three free square-zero matrix units: the central reduction stops

<a id="statement"></a>
<a id="three-square-zero-reconstruction-interface"></a>

Date: 2026-09-16.
Human record author: Yin.
Proof developed by a Codex research agent for [Yin_T_F0007_v1](../tasks/Yin_T_F0007_v1.md#decision-candidate-0001).
The three stated conclusions were accepted after complete independent mathematical review by another AI agent: the scalar polynomial center, the exact noncentral commutator norm, and the conditional bounded scalar reconstruction.
The positive-word support question and full three-generator permanence statement remain open.
No mathematical Role is assigned.

## 1. Scope and reused inputs

Let
\[
 (M,\tau)=*_{i=1}^3(M_2(\mathbb C),\operatorname{tr}_2),\qquad
 x_i=e_{12}^{(i)},\qquad A_3=\mathbb C\langle x_1,x_2,x_3\rangle,
 \qquad F_3=\operatorname{Div}_{L^0(M)}A_3.
\]
Each input C1+C x_i satisfies the original T_F0007 hypotheses, exactly as in the independently reviewed [C_F0112 (recorded assessment 2)](Yin_C_F0112_v1.md#decision-candidate-0002).
The question remains whether F_3 intersect M=Div_M A_3.

This three-factor test remains within the original binary [T_F0007 contract](../tasks/Yin_T_F0007_v1.md).
Group the first two factors as N_12=W*(M_2^(1),M_2^(2)) with its finitely generated coordinate algebra A_12=C<x_1,x_2>.
C_F0112 gives the required input closure equality for A_12; C1+C x_3 has the input equality in the third M2 factor.
The grouped N_12 and the third factor are free, and their coordinate algebras generate A_3.
Thus the full binary permanence assertion would apply to these two inputs and settle this exact three-factor test.

Read and reused: the [C_F0112 proof](Yin_C_F0112_v1.md), [Yin_S_F0016](../strategies/Yin_S_F0016.md), the finite-state argument in [C_F0106 Sections 5-7](Yin_C_F0106_v1.md), and the already audited adjoint-free small-power elimination of [DR97-U004, Lemma 11](../audits/literature/DR97/Yin_U004.md#dr97-u004).
The next calculations are direct finite-word comparisons and a specific change of basis in that existing state construction; no broad literature search or new external theorem is needed.
No known-result novelty claim is made.

## 2. The center of the three-generator polynomial algebra is only the scalars

The nonempty words x_(i_1)...x_(i_n) with adjacent indices different are nonzero, mutually orthogonal reduced free-product vectors on the vacuum.
Each has squared L2 norm 2^{-n}.
Thus they and 1 are linearly independent.
Every word with an adjacent repeated index is zero because x_i^2=0.
Consequently the only polynomial relations are the three square-zero relations, and these reduced words form a vector-space basis of A_3.

Let h in A_3 commute with all three x_i, and let w be any nonempty reduced word.
Choose k different from both its first and its last index; three available indices guarantee this choice.
Then x_k w is reduced.
Its coefficient in x_k h is exactly the coefficient of w in h, since prefix deletion is unique.
Its coefficient in h x_k is zero: every nonzero word in the latter ends in k, whereas x_k w ends in the last index of w, which is not k.
The equation [x_k,h]=0 therefore forces the coefficient of w to vanish.
This applies to every nonempty w, so
\[
                         Z(A_3)=\mathbb C1.       \tag{1}
\]
This coefficient proof concerns the polynomial algebra, not an asserted description of the center of an affiliated or abstract rational closure.

In particular C_F0112's pair parameter t_12=x_1x_2+x_2x_1 fails to be central after adjoining x_3:
\[
 [t_{12},x_3]=x_1x_2x_3+x_2x_1x_3
                 -x_3x_1x_2-x_3x_2x_1.
\]
The four displayed words are mutually orthogonal and each has squared L2 norm 1/8.
Therefore
\[
                    \|[t_{12},x_3]\|_2^2=\frac12.              \tag{2}
\]
The first specific failure in extending C_F0112 is thus its central localization: there is no nonconstant polynomial central parameter over which this infinite-dimensional A_3 could have the same finite-module structure.
The word count is also explicit: there are 3 times 2^{n-1} nonzero basis words of length n, instead of the two alternating words at each positive length in the pair case.
This invalidates direct reuse of C_F0112's four rational scalar coefficients.
It does not refute the bounded-intersection equality or exclude another rational representation mechanism.

The two-letter cases remain established inside M.
For N=W*(M_2^(i),M_2^(j)), every affiliated rational expression in x_i,x_j takes values in L0(N); invertibility of its intermediate operators is unchanged by the trace-preserving inclusion N subset M because their kernel projections belong to N and are unchanged in a faithful normal representation.
An affiliated element of N bounded in M belongs to N by its spectral projections.
Hence C_F0112 still reconstructs every bounded expression involving at most two of the three generators.
Any unresolved example must use all three.

## 3. A precise sufficient next interface: support in the original letters

Let H_+ be the closed L2 span of the vacuum and all reduced words in x_1,x_2,x_3.
The following conditional implication follows from the accepted finite-state mechanism:
\[
 \boxed{\quad f\in F_3\cap M,\quad f\Omega\in H_+
       \quad\Longrightarrow\quad f\in\operatorname{Div}_M A_3.\quad}
                                                               \tag{3}
\]
This is a sufficient implication only; neither automatic membership in H_+ nor its necessity for bounded scalar closure is asserted here.

Here are the exact interfaces proving (3).
Let B be the polynomial star algebra generated by the full three M2 factors.
Since A_3 subset B, f belongs to Div_(L0(M)) B intersect M.
C_F0106's finite-rank and residual construction gives a minimal representation of its full reduced-word coefficient series,
\[
 \beta_w=\lambda\mu(w)\gamma,
\]
over the centered selfadjoint Pauli bases of the factors.
Its proof supplies actual matrices mu_t with same-factor forbidden products zero, and
\[
 V=\sum_t\mu_t\otimes a_t,\qquad V^n\longrightarrow0,
 \qquad f=\lambda(I-V)^{-1}\gamma.                \tag{4}
\]
The decay is the matrix operator-norm decay proved in C_F0106 before its positive-pivot step.
No assumption about boundedness of an arbitrary original affiliated pencil is inserted.

In each factor replace the selfadjoint orthonormal basis
\[
 a_1=e_{12}+e_{21},\qquad a_2=-i e_{12}+i e_{21},
 \qquad a_3=e_{11}-e_{22}
\]
by the orthonormal basis
\[
 z_+=\sqrt2 e_{12}=(a_1+i a_2)/\sqrt2,\quad
 z_-=\sqrt2 e_{21}=(a_1-i a_2)/\sqrt2,\quad z_0=a_3.
\]
Write z_t=sum_s U_(ts)a_s for the block-diagonal unitary change of basis.
Coefficients in the new reduced-word tensor basis have the recognizable representation with transition matrices
\[
 \widetilde\mu_t=\sum_s\overline{U_{ts}}\mu_s.
\]
This follows by the tensor product change of basis at each letter of each reduced word.
It also preserves minimality because the old and new transition families linearly span each other, separately within each factor; therefore their reachable and observable spaces agree.
Same-factor zero products are preserved by these linear combinations.

The assumption f Omega in H_+ says that every coefficient containing a minus or zero letter vanishes.
For any such letter t and arbitrary words p,q, minimality gives
\[
 0=\beta_{ptq}=\lambda\widetilde\mu(p)
              \widetilde\mu_t\widetilde\mu(q)\gamma
 \quad\Longrightarrow\quad\widetilde\mu_t=0.
\]
Indeed the observable rows and reachable columns span their full finite-dimensional spaces.
This is an actual matrix identity, not cancellation only after the output vectors.

Finally the state pencil is unchanged by the unitary substitution:
\[
 \sum_t\widetilde\mu_t\otimes z_t
 =\sum_{t,s,r}\overline{U_{ts}}U_{tr}\mu_s\otimes a_r
 =\sum_s\mu_s\otimes a_s=V.
\]
All unwanted transitions have vanished, so V=sum_i tilde(mu)_(i,+) tensor sqrt(2)x_i lies in a matrix algebra over the **original** A_3.
The actual decay V^n->0 is unchanged.
DR97-U004 Lemma 11 now gives every entry of (I-V)^{-1} using finitely many bounded scalar inverses of expressions in the entries of V, without adjoining adjoints.
Combining with (4) proves (3).

## 4. Remaining support question and scope boundary

The concrete next question is whether every f in F_3 intersect M satisfies f Omega in H_+, or whether an explicit genuinely three-letter affiliated expression produces a bounded output with a nonzero coefficient containing z_- or z_0.
A positive answer would close this three-generator test through (3).
A negative answer would obstruct this support route; by itself it would not prove failure of the original scalar division-closure equality, whose elements have not been shown necessarily to lie in H_+.

The support question, affiliated invertibility of x_1+x_2+x_3, and the rational center are not settled by this argument.
The diffuse-input route still has a different first obstacle: replacing its infinite marginal alphabet by a controlled finite realization.
The three-matrix-unit calculation neither resolves nor supersedes that diffuse question.

The independently reviewed conclusions are (1), the nonzero commutator and exact norm (2), and the conditional reconstruction (3) with the displayed source interfaces.
They explain exactly why C_F0112 cannot simply be repeated and isolate one concrete additional hypothesis that would suffice.
The review does not establish automatic positive-word support, the full three-generator closure equality, or general T_F0007.
No numerical computation or proof-assistant verification is claimed.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:31 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#three-square-zero-reconstruction-interface) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: The polynomial center is scalar and the two-factor parameter is noncentral; explicit positive-word Fourier support suffices for bounded scalar reconstruction in the original three-generator algebra.
Automatic support and full permanence remain open.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:41 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#three-square-zero-reconstruction-interface) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0112_v1.md#decision-candidate-0002) | The input equalities, two-generator bounded reconstruction and reduction of this three-factor test to the original binary Task contract. |
| dependency | [Exact material](Yin_C_F0106_v1.md#decision-candidate-0002) | Full finite-factor residual representation, minimality, same-factor forbidden products, actual state-pencil decay and bounded-output realization before scalar reconstruction. |
| review | [Exact material](../audits/reviews/Yin_R_F0102_v1.md) | Complete three-part statement, stable minimal representation and original-alphabet scalar elimination, fixed dependencies and binary Task applicability; support is an explicit unproved additional premise, not a general permanence conclusion. |

Recorded mathematical summary: The polynomial center is scalar and the two-factor parameter is noncentral; explicit positive-word Fourier support suffices for bounded scalar reconstruction in the original three-generator algebra.
Automatic support and full permanence remain open.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:54 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#three-square-zero-reconstruction-interface) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0112_v1.md#decision-candidate-0002) | The input equalities, two-generator bounded reconstruction and reduction of this three-factor test to the original binary Task contract. |
| dependency | [Exact material](Yin_C_F0106_v1.md#decision-candidate-0002) | Full finite-factor residual representation, minimality, same-factor forbidden products, actual state-pencil decay and bounded-output realization before scalar reconstruction. |
| review | [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0090-applicability) | Yin_C_F0113 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: The polynomial center is scalar and the two-factor parameter is noncentral; explicit positive-word Fourier support suffices for bounded scalar reconstruction in the original three-generator algebra.
Automatic support and full permanence remain open.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-applicability

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:13 |
| status | proved |
| reason | Select the same actual applicability finding at its responsible R home, with its original date, exact per-Claim scope and known shared mathematical context, preserving statement, argument, dependencies and mathematical assessment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#three-square-zero-reconstruction-interface) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0112_v1.md#decision-candidate-0002) | The input equalities, two-generator bounded reconstruction and reduction of this three-factor test to the original binary Task contract. |
| dependency | [Exact material](Yin_C_F0106_v1.md#decision-candidate-0002) | Full finite-factor residual representation, minimality, same-factor forbidden products, actual state-pencil decay and bounded-output realization before scalar reconstruction. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0103_v1.md#c-f0090-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Complete three-part statement, stable minimal representation and original-alphabet scalar elimination, fixed dependencies and binary Task applicability; support is an explicit unproved additional premise, not a general permanence conclusion.

Review: [Exact material](../audits/reviews/Yin_R_F0102_v1.md).

Material covered by that review: [Exact material](Yin_C_F0113_v1.md).

Yin_C_F0113 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0090-applicability).

Material covered by that review: [Exact material](Yin_C_F0113_v1.md).
