---
author: Yin
---

# Original rational derivative graphs for L2 polynomial-matrix inverses

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## L2 polynomial-matrix inverses and original finite rational derivatives

<a id="statement"></a>
<a id="l2-polynomial-pencil-original-graph"></a>

Date: 2026-09-29.
Human author: Yin.
Authoring agent: counterexample.
Permanent proof promoted after complete independent scratch review.
Exact original hypotheses are [C_F0025_v1](Yin_C_F0025_v1.md#yin_c_f0025), plus the explicitly stated full matrix inverse L2 premise.
This is a conditional sufficient criterion for bounded scalar weak forms, not an assertion that every bounded rational scalar supplies that premise.

The proof below has no mathematical dependence on scratch files.
Exact permanent review binding and Claim allocation are separate actions.

The accepted [CR94-U001 minimality interface](../audits/literature/CR94/Yin_U001.md#cr94-u001) supplies algebraic state independence; no analytic state-integrability hypothesis is imported.
The actual proof uses C_F0025 normal phases, original polynomial graph closure, bounded Neumann series, and tracial spectral dominated convergence as detailed below.
No new source theorem is imported and no complete source audit is claimed.

## 1. Statement and reused boundary

Let L belong to M_n(C<X_1,...,X_d>) and be invertible over U(M).
Assume that every entry of Y=L^(-1) lies in L2(M).
Then every entry of Y belongs to every ORIGINAL closed coarse derivation domain, and

    partial_i Y=-Y(partial_i L)Y.                              (1)

The right side is a finite algebraic tensor of L2 entries.
If u and v are scalar row and column matrices and f=uYv is bounded, every original weak commutator of f has the bounded finite-rank representative

    Theta(-uY(partial_i L)Yv).                                (2)

The pencil need not have invertible constant term, and need not itself be normal.
The argument actually permits every unstarred polynomial matrix L.

Automatic L2 inverse-state results under bounded Hilbert-space duals and bounded polynomial adjoint images do not apply under the present hypotheses.
C_F0007 starts its state extraction from already finite commutators.
This note supplies only an original-graph sufficiency bridge once inverse integrability is known.
The existence and minimal-state independence of affine representations use the accepted Yin20/CR94-U001 interfaces; their source proofs are not re-audited here.

## 2. Finite phase expressions on the polynomial core

Fix i and let k_i be the normal phase vector partial_i X_i*.
As in C_F0025, there is a unitary I_i on the coarse Hilbert space, formed from the INNER right-X_i action on the first factor and left-X_i action on the second, with

    k_i=I_i(1 tensor1).

Its joint spectral multiplier is the modulus-one scalar phase off the null diagonal.
This INNER operator commutes with all OUTER left/right M actions.
In particular, for bounded a,b,

    a k_i b=I_i(a tensor b),  ||a k_i b||2=||a||2||b||2.         (3)

The identity extends to arbitrary L2 a,b by completion.
It is an identity on the coarse Hilbert space, not a claim of an operator Schur multiplier bound.

The derivative of any mixed starred polynomial is a finite sum of tensors p tensor q and phase tensors p k_i q, with bounded polynomial coefficients.
The derivative of an unstarred polynomial has only the first kind; its adjoint polynomial has only the second kind.
Therefore each matrix entry of partial_i L* admits such a finite phase expression, and there is a finite constant C_L,i such that, for bounded matrix G,H,

    ||G(partial_i L*)H||_(matrix coarse)
        <=C_L,i ||G||_(matrix L2)||H||_(matrix L2).              (4)

This follows entrywise from (3), multiplication by the fixed bounded polynomial coefficients, and finite-dimensional Cauchy--Schwarz.
The same estimate without phases holds for partial_i L.
No norm uniform in L is used.

For each fixed polynomial q, both maps v -> v(partial_i q) and v -> (partial_i q)v are bounded from L2 to the coarse Hilbert space, by the same finite expressions.
Thus left and right polynomial multiplication preserve the original closed domain and their product rules extend to every original graph vector.
This follows directly by core graph approximation.

## 3. Bounded soft inverses in the actual graph

For t>0 put

    A_t=L*L+t I,  C_t=LL*+t I,  Y_t=A_t^(-1)L*=L*C_t^(-1).

Each inverse A_t^(-1),C_t^(-1) belongs entrywise to every original coarse graph, with its usual inverse derivative.
Indeed choose a scalar c exceeding the matrix norm of A_t and use its Neumann series in I-A_t/c, whose norm is strictly less than1.
The series converges in operator norm and in each coarse graph: termwise derivatives are bounded by a geometric series with the extra factor equal to the degree.
Its partial sums are original starred matrix polynomials.
The same argument applies to C_t.
It also gives uniformly bounded polynomial graph approximants for each fixed t.

The ordinary product rule on these approximants now gives the EXACT identity

    partial_i Y_t
      =-Y_t(partial_i L)Y_t
       +t A_t^(-1)(partial_i L*)C_t^(-1).                     (5)

For completeness, differentiating A_t^(-1)L* first gives

    -Y_t(partial_i L)Y_t
       +A_t^(-1)(partial_i L*)(I-LY_t),

and I-LY_t=t C_t^(-1).
All these objects are bounded for fixed t, so no unbounded product is involved in deriving (5).

## 4. The residual tends to zero using precisely the L2 inverse premise

Polar spectral calculus and the premise Y in matrix L2 give

    Y_t -> Y in matrix L2.

Indeed the scalar singular-value multiplier s/(s^2+t) is bounded by1/s and converges to1/s.
Define bounded matrices

    G_t=sqrt(t) A_t^(-1),  H_t=sqrt(t) C_t^(-1).

For positive singular values s,

    sqrt(t)/(s^2+t)<=1/(2s),

and the left side tends to zero for every s>0.
The L2 inverse assumption and dominated convergence therefore imply

    ||G_t||2 ->0,  ||H_t||2 ->0.                              (6)

Regularity rules out a positive-trace zero spectral projection.
The tracial singular-value distributions of |L| and |L*| agree, so the same L2 domination is valid for both matrices.

By (4), the residual in (5), equal to G_t(partial_i L*)H_t, tends to zero in matrix coarse L2.
The main term tends to -Y(partial_i L)Y, because partial_i L is a finite polynomial tensor and both Y_t factors converge in L2.
The limit is an algebraic finite sum of L2 tensors.
Original closedness proves (1).

The square-root split in (6) is essential.
Estimating t A_t^(-1) on one side and C_t^(-1) on the other would leave an uncontrolled factor.
Neither side needs an operator-norm limit or an L4 inverse assumption.

## 5. Original weak forms for bounded scalar output

Scalar matrix compression gives f=uYv in every original coarse domain, with the derivative in (2).
For each original polynomial q, the bounded graph action from Section2 gives fq in that same original domain and

    partial_i(fq)=(partial_i f)q+f partial_i q.

This step does NOT need uniformly bounded approximants uY_t v.
Those approximants need not be uniformly bounded even when f is bounded.
Instead, the fixed polynomial right-action correction is a bounded map from H into the coarse Hilbert space, as proved in Section2.

Contract the product rule by id tensor tau.
The normalized original dual closure contains this contracted graph, since its original polynomial values are exactly that contraction.
Thus, on all original polynomial tests p,q,

    beta_i^f(p,q)=<p,Theta(partial_i f)q>.

Every factor of partial_i f is L2, giving a bounded finite-rank operator.
C_F0025 normalization invariance restores the originally specified dual weak form; no new extension of that dual is chosen.

## 6. Exact remaining obligation

For a general bounded rational f, choose a minimal affine representation f=uL(X)^(-1)v.
The unresolved premise is whether ALL entries of that evaluated inverse belong to L2 under the original C_F0025 hypotheses.
Minimality provides algebraic scalar independence, but no integrability by itself.
The new kernel-affine tests do not yet apply, because these state entries depend on the coordinate being differentiated; damping them creates additional derivative terms.
Accordingly this note is a conditional rationality criterion and an explicit graph construction, not the desired automatic state theorem or a resolution of the general correlated task.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T23:55 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#l2-polynomial-pencil-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: If the complete affiliated inverse of an unstarred polynomial matrix is entrywise L2, its entries lie in every original closed coarse derivative graph with the finite-tensor inverse formula; every bounded scalar compression consequently has finite-rank original weak commutators.
Automatic inverse integrability is not asserted.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:15 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#l2-polynomial-pencil-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original canonical coarse derivations, inner normal phase and the original normalized weak-form interface. |
| review | [Original finding](../audits/reviews/Yin_R_F0078_v1.md#verdict-and-exact-hypothesis) | Unknown initial context; whole six-section inverse-L2 conditional original-graph result, without automatic inverse integrability. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:55 |
| status | proved |
| reason | Adopt the newly performed isolated whole-proof finding at its exact scope after initial independent inspection and later historical comparison. Preserve the fixed mathematics, earlier decisions and exact non-review relations; historical checking relationships remain at their actual findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#l2-polynomial-pencil-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original canonical coarse derivations, inner normal phase and the original normalized weak-form interface. |
| review | [New whole independent finding](../audits/reviews/Yin_R_F0078_v1.md#f0103-whole-independent-20261023) | Complete current fixed proof at the exact hypotheses and limits stated in the new finding; earlier unknown relationships and their historical adoption are not reclassified. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T23:58 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#l2-polynomial-pencil-original-graph) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original canonical coarse derivations, inner normal phase and the original normalized weak-form interface. |
| review | [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0103) | Whole proof: finite inner-phase estimate, actual Neumann graph approximants, exact soft matrix inverse identity, square-root residual domination under full inverse L2, fixed polynomial graph action and bounded compression weak forms. No automatic matrix-state integrability or general rationality completion. |

Recorded mathematical summary: If the complete affiliated inverse of an unstarred polynomial matrix is entrywise L2, its entries lie in every original closed coarse derivative graph with the finite-tensor inverse formula; every bounded scalar compression consequently has finite-rank original weak commutators.
Automatic inverse integrability is not asserted.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Whole proof: finite inner-phase estimate, actual Neumann graph approximants, exact soft matrix inverse identity, square-root residual domination under full inverse L2, fixed polynomial graph action and bounded compression weak forms.
No automatic matrix-state integrability or general rationality completion.

Review: [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0103).

Material covered by that review: [Exact material](Yin_C_F0061_v1.md).
