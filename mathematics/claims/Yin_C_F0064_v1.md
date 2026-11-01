---
author: Yin
---

# Complete original bounded weak rationality under normal polynomial-core hypotheses

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Bounded affiliated rationality from the original polynomial weak forms

<a id="statement"></a>
<a id="normal-small-core-bounded-rationality"></a>

Date: 2026-09-29.
Human author: Yin.
Synthesis author: counterexample agent.
Mathematical contributions: another AI agent (liberation finite-defect derivation and tensor removal), root (intrinsic formulation and compressed state-graph mechanism), and counterexample agent (compressed state graphs and this bounded-companion synthesis).

The result resolves the bounded weak-form companion of T_F0001 at its exact starting hypotheses.
It is not a claim of literal arbitrary-fraction domain agreement for the unbounded original duals.
The separate intrinsic affiliated criterion and its comparison with the primary task have their own proof and assessment.

## 1. Exact assumptions and theorem

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace.
Set H=L2(M,tau), Omega=1, and let P_Omega be the vacuum projection.
Let X=(X_1,...,X_d) be bounded normal generators of M.
Write

    P=C<X_1,X_1*,...,X_d,X_d*>,
    A=C<X_1,...,X_d>,  F=Div_(U(M)) A.

The starred algebra P is the analytic test domain.
Generator adjoints are not adjoined to A by this notation.
All finite ranks below are ordinary complex Hilbert-space ranks; inner products are linear in the second entry.

Suppose D_i0 has domain exactly P, Omega is in its actual Hilbert-adjoint domain, and on P

    [D_i0,X_j]=delta_ij P_Omega,
    [D_i0,X_j*] has a compact bounded extension to H.

These are exactly [C_F0025_v1](Yin_C_F0025_v1.md#yin_c_f0025), with no all-M original-domain or bounded-Hilbert-space-dual assumption.
That input derives closability, P subset Dom D_i0*, the original normalized coarse derivations partial_i, maximal Delta and the embedded free field F.

For f in M define on original polynomial tests

    beta_i^f(p,q)=<D_i0* p,fq>-<f* p,D_i0 q>, p,q in P.

Then

    f belongs to F intersect M
      IFF every beta_i^f has a bounded finite-rank representative.          (T)

For rational f, the representative is uniquely

    T_i(f)=Theta(partial_i^rat f),
    Theta(g tensor h)q=g tau(hq),                            (1)

where each formal rational derivative is an algebraic finite tensor of L2 vectors.
In fact f and fq for every q in P lie in each ORIGINAL closed coarse derivative graph, with partial_i f=partial_i^rat f and the actual product rule.

## 2. Exact permanent proof inputs

Besides C_F0025 (recorded assessment 3), the two complete permanent modules used below are:

1. [C_F0063_v1: liberation and intrinsic affiliated tensors](Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion),

   The required conclusion is Section3, formula(8): for every rational affiliated u and every bounded fraction pair, s(partial_i^rat u)t is an algebraic finite L2 tensor.
   This module includes the complete actual liberation bound proof in Appendix A and the fraction-derivation and tensor-support arguments.
   The present theorem uses its bounded case only.
2. [C_F0062_v1: minimal states and original rational graphs](Yin_C_F0062_v1.md#minimal-rational-states-original-graph),

   Sections1--4 turn left and right L2 states into the actual output graph and original weak form; Section5 derives those state premises from formal L2 derivative tensors by the accepted minimal-affine representation interface.
   No full inverse L2 premise is imported.

These input locators identify the complete accepted proof versions used in this synthesis.
There is no mathematical dependence on a scratch artifact.
External representation/minimality interfaces are retained at the scopes recorded by these modules, rather than re-audited or silently strengthened here.

Existence of a full affine representation for every free-field element is the precise accepted interface of [Yin20-U001, Sections4--6](../audits/literature/Yin20/Yin_U001.md#yin20-u001), reconstructing Theorem IV.3.2 by the corrected Algorithm IV.3.4.
The finite expression recursion and explicit sum/product/inverse block identities produce a full affine pencil over the free field; applying its faithful embedding gives the corresponding affiliated inverse.
The present use retains that algebraic existence theorem, not a bounded matrix inverse conclusion.
Among the nonempty set of representation sizes choose a least one.
Separate linear independence of its left and right states is then the distinct accepted interface [CR94-U001](../audits/literature/CR94/Yin_U001.md#cr94-u001).
That latter source is not used to assert representation existence.

## 3. Bounded rational elements have finite L2 derivative tensors

For clarity, the mechanism from the first module is recorded explicitly.
Set B_i(g tensor h)=gX_i tensor h-g tensor X_i h.
The original liberation derivation delta_i=i B_i partial_i has an actual original contraction A_i whose domain and adjoint domain both contain M.
Its generator commutators are finite rank.
Therefore the exact C_F0034 fraction calculus applies on the specified left M-module M, with adjoint test module M.

The module proves that its affiliated finite-defect tensor is the derivation

    eta_i(u)=i B_i partial_i^rat u, u in F.                  (2)

This identification follows from actual common-denominator identities, addition/product/inverse rules, and the generator values.
It does not assume that the desired original normal weak commutator is already finite rank.

For bounded rational f choose the literal bounded fraction pair (1,f,f,1).
The actual liberation commutator is bounded finite rank, so

    i B_i partial_i^rat f in H tensor_alg H.

The finite-tensor removal lemma in the same module applies because every X_i-lambda is regular in U(M).
It yields

    partial_i^rat f in H tensor_alg H for every i.           (3)

This implication is purely algebraic on finite tensors.
It asserts no norm bound for B_i^(-1), no operator Schur multiplier bound, and no inverse on a completed tensor space.

## 4. Recover states and identify the original graphs

Constants, including zero, already have zero derivative and zero weak form and preserve every polynomial graph.
For a nonconstant f choose, by the existence and least-size argument in Section2, a minimal affine representation f=uL(X)^(-1)v with scalar coefficient matrices.
The faithful free-field embedding makes it a valid affiliated matrix inverse.
Minimality gives separate scalar linear independence of the left state entries g=uL^(-1) and the right entries h=L^(-1)v.

Writing L=A_0-sum_i A_i X_i, the formal derivative is

    partial_i^rat f=sum_k(g A_i)_k tensor h_k
                    =sum_j g_j tensor(A_i h)_j.

The algebraic quotient by H in one tensor leg, using (3) and state independence in the other, places g A_i and A_i h in L2 for i>=1.
The identities gL=u and Lh=v do the same for i=0.
Fullness of L makes sum_i A_i A_i* and sum_i A_i* A_i positive definite scalar matrices, so the reconstruction in the second module places every g_j and h_k in L2.
This is only the first algebraic state bootstrap; no derivative theorem is applied to unbounded state entries.

The actual graph theorem of that module now gives

    f in Dom closure(partial_i),
    closure(partial_i)f=-g(partial_i L)h=partial_i^rat f.

Its proof compresses bounded soft inverse matrices.
The two compressed residual factors tend to zero in L2 using g,h and the bounded multiplier sqrt(t)Y_t*, without assuming the complete inverse is L2 or the scalar approximants uniformly bounded.
Bounded graph actions by fixed original polynomials give fq in the same original graph and its product derivative.

Contracting by id tensor tau yields (1) on all original polynomial tests for the normalized contraction.
C_F0025's exact algebraic normalization invariance makes this the representative of the specified original beta.
Every factor is L2, so the representative is bounded and finite rank.
Density of P proves uniqueness.

## 5. The converse and the exact domain consequence

If every original beta_i^f has a bounded finite-rank representative, C_F0025 (recorded assessment 3) applies directly and gives f in F.
Combined with Sections3--4, this proves (T) and the stated original coarse graph construction.

There is also a legitimate full-domain consequence for the NORMALIZED contractions.
Put eta_i0=D_i0(Omega), E_i0(p)=D_i0(p)-p eta_i0 and E_i=closure(E_i0).
The proof supplies on P

    E_i(fq)=f E_i q+T_i(f)q.

For any q in Dom E_i, approximate q in its original graph by polynomials.
The bounded f and T_i(f), and closedness of E_i, then give

    f Dom E_i subset Dom E_i,
    [E_i,f]q=T_i(f)q on Dom E_i.                            (4)

Adjoint duality also gives f* Dom E_i* subset Dom E_i* and E_i* f*-f*E_i*=-T_i(f)* there.
These are consequences for the normalized actual closures, not for an independently selected extension.

For the unnormalized original D_i0=E_i0+right-multiplication-by-eta_i0, the theorem asserts the original weak forms via C_F0025 normalization.
No full-domain invariance of closure(D_i0) is inferred merely from beta on P: P has not been assumed an adjoint graph core, and nonuniform soft approximants do not automatically converge after that unbounded right multiplier.
Thus (4) is not silently transferred to the unnormalized D_i.

## 6. Task scope and remaining primary-domain issue

This is the complete bounded weak-form companion for arbitrary correlated normal tuples under the exact original assumptions, without geometric or free independence restrictions.
It includes the earlier special fraction classes and supplies actual normalized original graphs rather than only formal finite derivative tensors.

For genuinely unbounded u, the intrinsic liberation/deconvolution criterion has a separate precise formulation in its own module.
Whether its test functional realization fulfills the primary task's intended regular commutator convention, and agreement with literal arbitrary raw composition domains sD_i b-aD_i t, must be assessed there and in the task audit.
The bounded theorem alone is not declared completion of that primary objective.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-29T00:23 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-small-core-bounded-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: For every bounded element of an arbitrary correlated normal tuple satisfying the exact original polynomial-domain dual assumptions, membership in the unstarred affiliated division closure is equivalent to finite-rank representatives of all original polynomial weak commutators.
Original coarse graphs and normalized full-domain invariance are recovered without asserting unnormalized full-domain invariance.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:15 |
| status | proved |
| reason | Select the exact original scoped finding at its disclosed unknown initial relationship and restore the two distinct source inputs already used by this proof and review. Mathematical status, theorem, normalized graph scope and historical decisions remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-small-core-bounded-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original polynomial dual hypotheses, normalized coarse derivations, free-field embedding, weak-form normalization invariance and the reverse bounded implication. |
| dependency | [Exact material](Yin_C_F0062_v1.md#decision-candidate-0002) | Minimal left and right L2 state recovery from finite rational derivative tensors and actual original compressed output graphs; no full inverse L2 premise. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation finite-defect derivation and finite-support deconvolution, applied with the bounded fraction pair (1,f,f,1), to place formal rational derivatives in algebraic L2 tensors. |
| dependency | [Exact source input](../audits/literature/Yin20/Yin_U001.md#yin20-u001) | Previously accepted Sections 4–6 corrected affine-existence construction. |
| dependency | [Exact source input](../audits/literature/CR94/Yin_U001.md#cr94-u001) | Previously accepted distinct least-size left/right state independence, without an invertible constant coefficient. |
| review | [Original finding](../audits/reviews/Yin_R_F0078_v1.md#closed-domain-statement-and-boundary) | Unknown initial context; whole six-section bounded weak-form equivalence and normalized graph invariance, with distinct affine-existence and state-independence inputs. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:55 |
| status | proved |
| reason | Adopt the newly performed isolated whole-proof finding at its exact scope after initial independent inspection and later historical comparison. Preserve the fixed mathematics, earlier decisions and exact non-review relations; historical checking relationships remain at their actual findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-small-core-bounded-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original polynomial dual hypotheses, normalized coarse derivations, free-field embedding, weak-form normalization invariance and the reverse bounded implication. |
| dependency | [Exact material](Yin_C_F0062_v1.md#decision-candidate-0002) | Minimal left and right L2 state recovery from finite rational derivative tensors and actual original compressed output graphs; no full inverse L2 premise. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation finite-defect derivation and finite-support deconvolution, applied with the bounded fraction pair (1,f,f,1), to place formal rational derivatives in algebraic L2 tensors. |
| dependency | [Exact source input](../audits/literature/Yin20/Yin_U001.md#yin20-u001) | Previously accepted Sections 4–6 corrected affine-existence construction. |
| dependency | [Exact source input](../audits/literature/CR94/Yin_U001.md#cr94-u001) | Previously accepted distinct least-size left/right state independence, without an invertible constant coefficient. |
| review | [New whole independent finding](../audits/reviews/Yin_R_F0078_v1.md#f0106-whole-independent-20261023) | Complete current fixed proof at the exact hypotheses and limits stated in the new finding; earlier unknown relationships and their historical adoption are not reclassified. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-29T00:26 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-small-core-bounded-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original polynomial dual hypotheses, normalized coarse derivations, free-field embedding, weak-form normalization invariance and the reverse bounded implication. |
| dependency | [Exact material](Yin_C_F0062_v1.md#decision-candidate-0002) | Minimal left and right L2 state recovery from finite rational derivative tensors and actual original compressed output graphs; no full inverse L2 premise. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation finite-defect derivation and finite-support deconvolution, applied with the bounded fraction pair (1,f,f,1), to place formal rational derivatives in algebraic L2 tensors. |
| review | [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0106) | Whole six-section assembly and both actual proof interfaces: all bounded elements, both implications for specified original polynomial weak forms, zero and constants, affine existence and minimal independence, finite L2 rational tensors, minimal states, actual original coarse graphs and normalized closure/adjoint invariance. No unnormalized full-domain invariance or arbitrary raw fraction-domain equality is inferred. |

Recorded mathematical summary: For every bounded element of an arbitrary correlated normal tuple satisfying the exact original polynomial-domain dual assumptions, membership in the unstarred affiliated division closure is equivalent to finite-rank representatives of all original polynomial weak commutators.
Original coarse graphs and normalized full-domain invariance are recovered without asserting unnormalized full-domain invariance.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/Yin20/Yin_U001.md); [Exact material](../audits/literature/CR94/Yin_U001.md).

Whole six-section assembly and both actual proof interfaces: all bounded elements, both implications for specified original polynomial weak forms, zero and constants, affine existence and minimal independence, finite L2 rational tensors, minimal states, actual original coarse graphs and normalized closure/adjoint invariance.
No unnormalized full-domain invariance or arbitrary raw fraction-domain equality is inferred.

Review: [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0106).

Material covered by that review: [Exact material](../audits/literature/CR94/Yin_U001.md); [Exact material](../audits/literature/Yin20/Yin_U001.md); [Exact material](Yin_C_F0064_v1.md).
