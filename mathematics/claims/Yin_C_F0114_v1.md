---
author: Yin
---

# Normal dual choices differ by right affiliation and share adjoint-module existence

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Right-affiliated comparison of normal dual systems

<a id="statement"></a>

Kind: Claim/proof module.
Date: 2026-09-16.
Human record author: Yin.
Proof developed by a Codex research agent; separate review by another AI agent identified the explicit common-domain clarification in Section 4.
Consumer: [Yin_T_F0005_v1](../tasks/Yin_T_F0005_v1.md#decision-candidate-0001), Q1.
The [selected assessment](#decision-candidate-0003) records the mathematical and review assessments.
The comparison does not establish existence of a good reference dual.

<a id="normal-dual-affiliated-comparison"></a>
## 1. Inputs and the precise question

Read the current C_F0102 [small-module phase argument](Yin_C_F0102_v1.md), C_F0104 [canonical analytic-phase argument](Yin_C_F0104_v1.md), and C_F0086 [original-domain and balanced-form argument](Yin_C_F0086_v1.md).
The comparison also uses the existing C_F0036/C_F0037 normal-dual argument ([Yin_C_F0036_v1](Yin_C_F0036_v1.md#yin_c_f0036), [Yin_C_F0037_v1](Yin_C_F0037_v1.md#yin_c_f0037)) and C_F0032 projection localization, already used by C_F0086.
No new external source theorem or web acquisition is used.

Let a bounded normal tuple X generate a finite faithful tracial von Neumann algebra M, with H=L2(M), and let D_i and R_i be closable normalized duals on dense left modules E_D and E_R.
They have the same normalized generator commutators.
The first question is whether their difference really is a right-affiliated multiplier without assuming a bounded reference.
The second is whether this supplies a good reference in the first place.

The first question has a positive answer by the following proof.
The second remains unresolved for a general noncommuting analytic-arc tuple.
These are separate logical steps.

## 2. Comparison of two unbounded dual choices

Fix one coordinate.
Put F=E_D intersect E_R.
C_F0086's countable-intersection argument makes F a dense left M-module.
Its restriction theorem gives

`closure(D|F)=closure(D)` and `closure(R|F)=closure(R)`.

Thus F is an original graph core for both operators.
Define A=D-R on F.
**A difference of two closable operators is not automatically closable**, so affiliation cannot be inferred at this point by simply taking its closure.

For each v in F, both orbit maps `a -> D(av)` and `a -> R(av)` are bounded from operator norm to H, and are weakly continuous on uniformly bounded strongly convergent nets, as proved in C_F0086.
Their difference has these two orbit properties.
C_F0037 gives the same bounded starred-generator commutators for D and R, determined solely by the fixed tuple and normalized generator commutators.
Consequently A commutes with every starred polynomial.
Norm approximation extends this identity to C*(X).
A uniformly bounded strong-star Kaplansky approximation then gives, by the separate weak continuity of the two original orbits,

`A(av)=a Av` for all a in M and v in F.                         (1)

No closedness assertion about A has been used.

Choose increasing projections e_n in F with e_n tending strongly to 1, using C_F0032 and the tail-meet construction of C_F0086.
Put eta_n=Ae_n, viewed as an L2 affiliated element.
Equation (1) gives

`e_n eta_n=eta_n`, and `e_n eta_m=eta_n` for m>=n.

Thus the left support of `eta_m-eta_n=(1-e_n)eta_m` has trace at most `tau(1-e_n)`.
The sequence is Cauchy in measure, without a uniform L2 bound.
Completeness of affiliated measure topology supplies eta in L0(M), and continuity of multiplication gives

`e_n eta=eta_n=Ae_n`.                                         (2)

For a bounded q in F, C_F0032's bounded-target localization supplies left projections p_n tending strongly to 1 and projections f_n in F with

`p_n q=a_n f_n`, where a_n belongs to M.

Formula (2) holds for every projection f in F, not just the selected e_n.
Indeed, f intersect e_n tends strongly to f; (1), applied on the left to f, and measure convergence identify `(f intersect e_n)eta=A(f intersect e_n)=(f intersect e_n)Af`, so f eta=Af in measure.
Therefore

`p_n A q=A(p_n q)=a_n A f_n=a_n f_n eta=p_n q eta`.

Taking limits in measure gives Aq=q eta.
For arbitrary q in F, use left spectral cutoffs of |q*|.
They produce bounded q_k in F with q_k tending to q and `Aq_k` tending to Aq in H by (1).
Affiliated multiplication continuity gives the same equality.
We have proved

`Aq=q eta` for every q in F.                                  (3)

In particular A is a restriction of the closed right multiplication operator C=rho(eta), so it is closable.
Its full domain is a dense left M-module.
Applying C_F0086's restriction theorem once more, now to this already closed right multiplier, shows

`closure(A)=rho(eta)`.

This proves the right-affiliated comparison on a genuine common graph core, rather than treating it as a formal cancellation.
Eta is unique: (2), or density together with the module restriction argument, determines it.

## 3. Adjoint-module existence is independent of the dual choice

Suppose the reference adjoint R* contains a dense left module V_R.
No boundedness of R on H or on all M is assumed.
Since `C*=rho(eta*)` has a dense left-module domain, C_F0086's intersection argument shows that

`V=V_R intersect Dom C*`

is again a dense left module.
For p in V and q in F, equation (3) gives the legitimate Hilbert pairing

`<p,Dq>=<R*p+C*p,q>`.

Thus `V subset Dom(D|F)*`, with the displayed value for the adjoint.
Because F is a graph core for the original D,

`V subset Dom D*`, and `D*p=R*p+p eta*` on V.                 (4)

This is an inclusion and a formula on V.
It does not assert an unrestricted equality between adjoints of unbounded sums or equality of their full domains.
The proof works separately for each coordinate, as the consumer criterion permits distinct adjoint modules.

The implication is symmetric in D and R.
Therefore, among all existing closable normalized dual systems on dense left modules for this fixed normal tuple, the property that every original adjoint has a dense left test module is independent of the choice of dual system.
The existing bounded-reference C_F0036 is a special case; this comparison requires only one reference with the desired adjoint-module property.

Once such a reference exists, it is unnecessary to apply any infinite spectral-phase series to its right-affiliated difference.
This explains why the arbitrary-tensor example in C_F0102, whose dual is a bounded good reference plus right multiplication, does not obstruct the adjoint-module conclusion.
Its series pathology concerns the proposed representation-dependent construction only.
No repetition or enlargement of that counterexample is needed here.

## 4. What an intrinsic balanced correction would still have to provide

The C_F0086/C_F0102 proof needs an H-valued operator Q on a dense left module G contained in E_D, with bounded weakly continuous left orbits and

`[Q,a]=[D,a*]*`

for starred polynomials a, using the actual bounded commutator representatives.
These identities make

`b(p,q)=<p,Dq>+<Qp,q>`

balanced, after which corner densities and left-cutoff graph recovery produce original-adjoint test modules.
The gluing stage itself does not require a right spectral-multiplier series.

If a good reference R already exists, this can be realized without such a series: restrict to the common dense left module G=E_D intersect E_R intersect V_R and put Q=-R*.
The extra E_R intersection ensures that both entries of the difference pairing use the actual original R domain.
The bounded commutator adjoint identity gives the required paired commutators.
Q is closable, so its orbit properties follow as in C_F0086; the cross form is the right-affiliated difference pairing.
This is a valid intrinsic replacement **conditional on reference existence**.

Conversely, if the desired original-adjoint module V_D is already known, Q=-D* on `E_D intersect V_D` supplies exactly such a correction and the balanced form is zero.
Thus the unrestricted existence of an admissible intrinsic Q is effectively equivalent to the desired adjoint-module conclusion.
Calling Q intrinsic does not in itself solve that existence problem; a separate construction using the analytic-arc geometry is required.

The attempted normalization `D-rho(D1)` is unavailable when 1 is absent from E_D.
Dense left modules need not contain 1 or even a full-support vector: a union of nested proper left ideals `M e_n`, with e_n increasing to 1, is a simple example.
Local values De cannot automatically be subtracted as right multipliers on `M e`: right multiplication sends e to a vector with left support at most e, whereas De need not satisfy eDe=De.
Compressing to eDe removes only that corner and does not by itself construct a compatible normalized reference on the remaining corners.

Even the formal canonical polynomial vacuum map obtained from the prescribed bounded commutators has not here been shown closable or equipped with a dense left-domain realization.
Nor does subtracting an arbitrary right-affiliated eta automatically make `[D-rho(eta),rho(S_i)]` bounded or produce the smooth right module required by C_F0104.
That would require a proved regularity decomposition, beyond the comparison statement (3).

## 5. Exact stopping boundary

The established comparison is: two closable normalized dual choices differ by a unique right-affiliated multiplier on a common original graph core; existence of dense original-adjoint modules transfers from any one good reference, even an unbounded one.
This gives a precise route that entirely avoids defining the canonical phase on an arbitrary right-affiliated summand.

Still missing: a noncircular construction of at least one good reference for an arbitrary normal analytic-arc tuple from the bare existence of a closable dual on a dense left module.
The accepted C_F0086 supplies it for line/circle coordinates, and C_F0104 supplies it under its additional right-domain hypotheses.
For a single scalar normal coordinate the ambient algebra is abelian, so right smooth invariance is already left invariance and C_F0104 applies.
The unresolved case is the general noncommuting tuple without these extra interfaces.

No general Q1 counterexample or proof results from this comparison.
The scope excludes general reference existence.
The separately recorded complete proof review covers the comparison and transfer, including the explicit Section 4 common-domain clarification.
No proof-assistant verification or external human review is claimed.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:07 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-dual-affiliated-comparison) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Two closable normalized dual systems on dense left modules differ by a unique right-affiliated multiplier on their common original graph core; dense actual adjoint-module existence transfers from either system to the other.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:10 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-dual-affiliated-comparison) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0032_v1.md#decision-candidate-0002) | Projection windows and bounded-target localization in dense left modules. |
| dependency | [Exact material](Yin_C_F0037_v1.md#decision-candidate-0002) | Fixed-tuple starred-generator commutators for closable normalized normal duals. |
| dependency | [Exact material](Yin_C_F0086_v1.md#decision-candidate-0002) | Dense module intersections, original graph-core restrictions, orbit continuity and balanced-form interface. |
| review | [Exact material](../audits/reviews/Yin_R_F0101_v1.md) | Entire comparison, measure gluing, original graph cores, actual adjoint transfer and common-domain Q interface; no assertion of reference existence. |

Recorded mathematical summary: Two closable normalized dual systems on dense left modules differ by a unique right-affiliated multiplier on their common original graph core; dense actual adjoint-module existence transfers from either system to the other.

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
| argument | [Exact material](#normal-dual-affiliated-comparison) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0032_v1.md#decision-candidate-0002) | Projection windows and bounded-target localization in dense left modules. |
| dependency | [Exact material](Yin_C_F0037_v1.md#decision-candidate-0002) | Fixed-tuple starred-generator commutators for closable normalized normal duals. |
| dependency | [Exact material](Yin_C_F0086_v1.md#decision-candidate-0002) | Dense module intersections, original graph-core restrictions, orbit continuity and balanced-form interface. |
| review | [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0093-applicability) | Yin_C_F0114 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: Two closable normalized dual systems on dense left modules differ by a unique right-affiliated multiplier on their common original graph core; dense actual adjoint-module existence transfers from either system to the other.

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
| argument | [Exact material](#normal-dual-affiliated-comparison) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0032_v1.md#decision-candidate-0002) | Projection windows and bounded-target localization in dense left modules. |
| dependency | [Exact material](Yin_C_F0037_v1.md#decision-candidate-0002) | Fixed-tuple starred-generator commutators for closable normalized normal duals. |
| dependency | [Exact material](Yin_C_F0086_v1.md#decision-candidate-0002) | Dense module intersections, original graph-core restrictions, orbit continuity and balanced-form interface. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0103_v1.md#c-f0093-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Entire comparison, measure gluing, original graph cores, actual adjoint transfer and common-domain Q interface; no assertion of reference existence.

Review: [Exact material](../audits/reviews/Yin_R_F0101_v1.md).

Material covered by that review: [Exact material](Yin_C_F0114_v1.md).

Yin_C_F0114 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0093-applicability).

Material covered by that review: [Exact material](Yin_C_F0114_v1.md).
