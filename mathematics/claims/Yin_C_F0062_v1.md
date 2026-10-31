---
author: Yin
---

# Original rational graphs from only minimal left and right L2 states

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Original rational output graphs from left and right L2 states

<a id="statement"></a>
<a id="minimal-rational-states-original-graph"></a>

Date: 2026-09-29.
Human author: Yin.
Mathematical contributors: root and counterexample agent, who proposed the same compressed residual identity in near-concurrent messages.
Complete proof promoted after independent review by another AI agent, separate from both contributors.

The mathematical body below is unchanged.
Permanent review binding and Claim allocation are separate administrative actions.

Exact inputs: [C_F0025_v1 original normal core](Yin_C_F0025_v1.md#yin_c_f0025), [C_F0061_v1 bounded Neumann and finite-phase graph constructions](Yin_C_F0061_v1.md#l2-polynomial-pencil-original-graph), and the [CR94-U001 minimal-state interface](../audits/literature/CR94/Yin_U001.md#cr94-u001).
Section 5 proves the algebraic first bootstrap without additional analytic assumptions or a full-inverse bootstrap.

The conclusion concerns the original normalized coarse/contraction graphs and the original specified weak forms via C_F0025 normalization invariance.
It does not infer full-domain invariance of the unnormalized original D_i from weak forms on the polynomial tests.
No mathematical input resides only in scratch files, and no new external source is introduced.

## 1. Conditional original-graph statement

Assume exactly C_F0025 (recorded assessment 3).
Let L be a square unstarred polynomial matrix, invertible over U(M), write Y=L^(-1), and let u,v be scalar row and column.
Suppose the two state families

    g=uY,  h=Yv

are entrywise L2, and the scalar output f=uYv is bounded.
Then f belongs to EVERY original closed coarse derivative domain, with

    partial_i f=-g(partial_i L)h.                            (1)

Every original weak form of f is represented by the corresponding bounded finite-rank operator Theta(partial_i f).
There is no assertion that Y itself is entrywise L2 or that the states g,h lie in these derivative domains.

## 2. Actual soft inverses and state convergence

Put A_t=L*L+t I, C_t=LL*+t I, and

    Y_t=A_t^(-1)L*=L*C_t^(-1).

For each fixed t these are bounded original-graph elements by the Neumann series construction in accepted C_F0061 (recorded assessment 2).
In particular the exact identity

    partial_i Y_t
       =-Y_t(partial_i L)Y_t
          +t A_t^(-1)(partial_i L*)C_t^(-1)                 (2)

holds on those actual closures.
Its derivation uses only bounded polynomial graph approximants; it requires no L2 inverse hypothesis.

Polar spectral calculus for the affiliated Y gives

    F_t=(I+t YY*)^(-1),  E_t=(I+t Y*Y)^(-1),
    Y_t=F_t Y=Y E_t.

Both F_t,E_t are contractions converging strongly to I.
Consequently

    g_t=uY_t=g E_t ->g in L2,
    h_t=Y_t v=F_t h ->h in L2,
    f_t=uY_t v ->f in L2.                                   (3)

The multiplication statements are valid for matrix L2 rows and columns by bounded approximation and the normal left/right representations.
The operator norms of f_t are NOT asserted uniformly bounded; a separately reviewed admissible minimal-pencil example shows that assertion can fail.

## 3. The compressed residual uses only these two state families

Define S_t=sqrt(t)Y_t*.
Polar functional calculus gives

    ||S_t||<=1/2,  S_t ->0 and S_t* ->0 strongly.             (4)

Indeed the singular-value multiplier is sqrt(t)s/(1+t s^2), bounded by1/2 and converging pointwise to zero on the spectral measure of |Y|.
The respective polar actions yield strong convergence for the operator and its adjoint.
No integrability of Y is needed for (4).

The EXACT identities needed for the compressed residual are

    sqrt(t)u A_t^(-1)=g S_t,
    sqrt(t)C_t^(-1)v=S_t h.                                 (5)

For example Y Y_t*=A_t^(-1) and Y_t* Y=C_t^(-1), by polar calculus or the bounded resolvent identities.
Equations (4) and the L2 state premises imply

    g S_t ->0 in L2,  S_t h ->0 in L2.                       (6)

The derivative partial_i L* is a finite sum of polynomial tensors acted on by the inner normal-phase unitary of the generator X_i.
This is the finite-phase estimate from C_F0061 (recorded assessment 2), which commutes with all outer actions.
Thus the compression of the residual in (2) is

    (g S_t)(partial_i L*)(S_t h) ->0 in coarse L2.            (7)

In particular this is not a bound on the full uncompressed residual and does not imply full inverse L2 integrability.

The compressed main term converges by (3): partial_i L is a finite ordinary polynomial tensor, so

    -g_t(partial_i L)h_t ->-g(partial_i L)h.

Every limiting tensor factor is L2.
Combining this with f_t ->f in L2 and actual closedness proves (1).

## 4. Exact original weak-form compatibility

For every fixed original starred polynomial q, the correction map z -> z(partial_i q) is bounded H -> coarse H: each term is an ordinary finite tensor or an inner-phase image of one, with bounded polynomial coefficients.
Therefore right multiplication by q is a bounded map of the original derivative graph, with its original product rule.
This is precisely the polynomial graph-action argument in C_F0061 (recorded assessment 2).

It follows that fq is in the original graph and

    partial_i(fq)=(partial_i f)q+f partial_i q.

No uniformly bounded f_t approximation is needed for this passage.
Contract by id tensor tau; the original normalized dual closure contains the contracted graph.
Its actual adjoint pairing with all original polynomial tests gives

    beta_i^f(p,q)=<p,Theta(partial_i f)q>.

Since f is bounded, all the terms of the original weak form are defined.
The tensor in (1) has finite L2 factors, so its representative is bounded finite rank.
C_F0025 normalization invariance restores the exact specified original duals without assuming any enlarged original domain.

## 5. Minimal affine states from L2 rational derivative tensors

The following algebraic argument uses only the stated rational derivative tensors and state independence.
Assume f has a minimal affine representation

    L=A_0-sum_(i=1)^d A_i X_i,  f=uYv,

and suppose the FORMAL rational derivative tensors of f belong to H tensor_C H.
Minimality gives separate complex-linear independence of the left state entries g_j and the right state entries h_k, by the accepted CR94-U001 interface.
The formal inverse rule gives

    partial_i^rat f=sum_k(g A_i)_k tensor h_k
                    =sum_j g_j tensor(A_i h)_j.              (8)

Quotient the first algebraic tensor factor by H.
Independence of the h_k implies g A_i in H for i>=1.
Quotient the second factor instead and use the independence of g_j to obtain A_i h in H.
No operator domain is used here.

The affiliated identities gL=u and Lh=v yield

    g A_0=u+sum_i(g A_i)X_i in H,
    A_0 h=v+sum_i X_i(A_i h) in H.

The constant matrices Q_R=sum_(i=0)^d A_i A_i* and Q_L=sum_(i=0)^d A_i* A_i are positive definite: otherwise the full matrix L would have a nonzero scalar left or right kernel.
Hence

    g=[sum_i(g A_i)A_i*]Q_R^(-1) in H,
    h=Q_L^(-1)sum_i A_i*(A_i h) in H.                         (9)

This obtains EXACTLY the two state premises needed in Sections1--4.
It requires neither bounded Hilbert-space duals nor a second bootstrap for every entry of the inverse.
There is no need to apply any derivative theorem to the unbounded state entries.

Consequently, for bounded rational f, any independently justified procedure which places all its formal rational derivative tensors in algebraic H tensor H now suffices for the actual original weak-form conclusion.
Identification of a liberation finite-defect tensor with its formal rational derivative is a separate premise under investigation, not proved by this graph-compatibility note.
In particular no already bounded original weak commutator was assumed to derive (8)--(9).

## Reuse and exact scope

The original Neumann and finite-phase estimates are accepted C_F0061 (recorded assessment 2); the normalization is C_F0025 (recorded assessment 3).
Minimal affine existence and state independence are the recorded Yin20/CR94-U001 interfaces.
The new analytic step is compressed residual control (5)--(7), which removes the full inverse L2 premise.
It is joint mathematical work of root and counterexample agent, so either author is unsuitable as the sole independent reviewer of this step.
No new external source or acquisition is introduced.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-29T00:16 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#minimal-rational-states-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: For a bounded rational matrix compression, L2 left and right states alone restore every original coarse derivative graph and original weak commutator.
Minimal affine state independence extracts those two L2 families from finite L2 formal derivative tensors; the full inverse need not be L2.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:15 |
| status | proved |
| reason | Select the exact original scoped finding at its disclosed unknown initial relationship and restore the explicitly used minimal-state source input. Preserve all mathematics and historical inputs; the earlier reviewer concern does not establish reviewer authorship of the authors’ repair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#minimal-rational-states-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core coarse derivations, inner phase and exact original weak-form normalization invariance. |
| dependency | [Exact material](Yin_C_F0061_v1.md#decision-candidate-0002) | Bounded Neumann graph approximation, exact soft inverse derivative, finite-phase estimate and fixed-polynomial graph action; its full inverse L2 premise is not imported. |
| dependency | [Exact source input](../audits/literature/CR94/Yin_U001.md#cr94-u001) | Previously accepted minimal-state separate linear independence of the left/right families, not affine existence. |
| review | [Original finding](../audits/reviews/Yin_R_F0078_v1.md#independent-review-left-and-right-states-recover-the-original-output-graph) | Unknown initial context; whole five-section two-state compressed residual and independent-family extraction. The authors supplied the graph-recovery proof; reviewer did not supply its repair. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:55 |
| status | proved |
| reason | Adopt the newly performed isolated whole-proof finding at its exact scope after initial independent inspection and later historical comparison. Preserve the fixed mathematics, earlier decisions and exact non-review relations; historical checking relationships remain at their actual findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#minimal-rational-states-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core coarse derivations, inner phase and exact original weak-form normalization invariance. |
| dependency | [Exact material](Yin_C_F0061_v1.md#decision-candidate-0002) | Bounded Neumann graph approximation, exact soft inverse derivative, finite-phase estimate and fixed-polynomial graph action; its full inverse L2 premise is not imported. |
| dependency | [Exact source input](../audits/literature/CR94/Yin_U001.md#cr94-u001) | Previously accepted minimal-state separate linear independence of the left/right families, not affine existence. |
| review | [New whole independent finding](../audits/reviews/Yin_R_F0078_v1.md#f0104-whole-independent-20261023) | Complete current fixed proof at the exact hypotheses and limits stated in the new finding; earlier unknown relationships and their historical adoption are not reclassified. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-29T00:20 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#minimal-rational-states-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core coarse derivations, inner phase and exact original weak-form normalization invariance. |
| dependency | [Exact material](Yin_C_F0061_v1.md#decision-candidate-0002) | Bounded Neumann graph approximation, exact soft inverse derivative, finite-phase estimate and fixed-polynomial graph action; its full inverse L2 premise is not imported. |
| review | [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0104) | Whole permanent proof: left/right state convergence, compressed square-root residual, original fixed-polynomial graph action, specified weak forms through normalization invariance, and finite-tensor minimal-state extraction. No full inverse L2 or unnormalized original full-domain invariance is asserted. |

Recorded mathematical summary: For a bounded rational matrix compression, L2 left and right states alone restore every original coarse derivative graph and original weak commutator.
Minimal affine state independence extracts those two L2 families from finite L2 formal derivative tensors; the full inverse need not be L2.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/CR94/Yin_U001.md).

Whole permanent proof: left/right state convergence, compressed square-root residual, original fixed-polynomial graph action, specified weak forms through normalization invariance, and finite-tensor minimal-state extraction.
No full inverse L2 or unnormalized original full-domain invariance is asserted.

Review: [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0104).

Material covered by that review: [Exact material](../audits/literature/CR94/Yin_U001.md); [Exact material](Yin_C_F0062_v1.md).
