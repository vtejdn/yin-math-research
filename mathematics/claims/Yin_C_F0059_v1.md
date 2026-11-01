---
author: Yin
---

# Original L2 states for bounded affine outputs over a coordinate kernel

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Bounded affine outputs over a coordinate kernel have actual L2 states

<a id="kernel-affine-original-l2-states"></a>

Date: 2026-09-29.
Human author: Yin.
Authoring agent: counterexample.
Permanent proof promoted from independently reviewed arguments.
Original hypotheses and canonical derivations are exactly [C_F0025_v1](Yin_C_F0025_v1.md#yin_c_f0025).
No general all-M domain or bounded Hilbert-space dual is assumed.

The full original graph-module argument and affine-state proof are included here.
Historical scratch review inputs were the kernel-denominator proof and amended affine proof.

Reuse: C_F0025 supplies the actual phase/coarse derivation and normalized weak form.
The graph projection, row/column damping, finite Gram probes and trace limits are proved below.
No external source theorem is newly imported.

## Statement

Under C_F0025, fix i and put B=W*(X_j:j!=i).
Let

    f=sum_(l=1)^m r_l X_i s_l+b0 in M,

where r_l,s_l,b0 belong to U(B).
Assume the two finite families (r_l) and (s_l) are separately complex-linearly independent; a finite tensor expression can always be reduced to this form by scalar row/column operations.
Then every r_l and s_l belongs to L2(B), f belongs to the ORIGINAL closed coarse domain of partial_i, and

    partial_i f=sum_l r_l tensor s_l.                           (1)

The original coordinate-i weak commutator consequently has the bounded finite-rank representative Theta(sum r_l tensor s_l).
No assertion about the other coordinate weak forms is made.
For m=0, bounded f=b0 belongs to B and the conclusion is derivative zero.

The original graph's B-bimodule property is proved in full below: the closed graph reduces the paired left/right B actions.
Thus every bounded B coefficient has derivative zero and may be multiplied with actual graph vectors.
No global M-domain assumption is used.

## Original coarse graph module property

Fix i, write d=partial_i for the original canonical coarse derivation, xi=d*(1 tensor1), and B=W*(X_j:j!=i).
Since d vanishes on every starred generator of B, its closed graph is invariant under the paired bounded representations

    lambda(b) on H,  lambda(b) tensor I on H tensor H,

and similarly under right multiplication on H and on the second coarse factor.
Invariance holds first for each generator and its adjoint, by the original product rule and graph approximation.
The orthogonal projection onto the closed graph therefore commutes with the generated diagonal von Neumann representations.
Thus every bounded b in B preserves the original closed domain and

    d(bp)=b dp,  d(pb)=(dp)b.

Taking p=1 shows that B itself lies in that original domain with derivative zero.
This is a strong graph-representation argument; no assertion that arbitrary M lies in the domain has been introduced.

## Left states

Choose the positive regular contraction

    sigma0=(1+sum_l s_l* s_l)^(-1/2) in B.

Each s_l sigma0 is bounded and their independence is preserved, because sigma0 is a unit in U(B).
Hence bounded probes c_j in B can be chosen so that

    tau(s_l sigma0 c_j)=delta_lj.

Indeed use finite linear combinations of (s_l sigma0)* and their positive definite L2 Gram matrix.
Define the positive affiliated operator

    R=sum_l r_l r_l*+(b0 sigma0)(b0 sigma0)*,
    rho_n=(1+R/n)^(-1/2).

These are bounded regular contractions in B, increasing strongly to1.
Every rho_n r_l and rho_n b0 sigma0 is bounded by the usual row damping inequality, with bound sqrt(n) sufficient.
Consequently

    q_n=rho_n f sigma0
       =sum_l (rho_n r_l) X_i (s_l sigma0)+rho_n b0 sigma0

belongs to the original closed coarse domain, and its derivative is the displayed finite tensor of those bounded coefficients.
For any bounded a in B, the ACTUAL vacuum identity on a q_n c_j gives

    tau(a rho_n r_j)=<xi_i,a rho_n f sigma0 c_j>.

The right side is bounded in absolute value by

    ||xi_i||2 ||f|| ||sigma0 c_j|| ||a rho_n||2.

Set a=(rho_n r_j)*.
Its left pairing is ||rho_n r_j||2 squared and ||a rho_n||2<=||a||2.
Thus ||rho_n r_j||2 is uniformly bounded in n.
Monotone convergence of rho_n squared in the extended trace pairing tau(r_j* rho_n squared r_j) proves r_j in L2.
This uses no prior L1 trace of the untruncated affiliated states.

## Right states

Choose instead a fixed positive regular left damping

    rho0=(1+sum_l r_l r_l*)^(-1/2),

so the bounded family rho0 r_l remains independent.
Pick bounded a_j in B with tau(a_j rho0 r_l)=delta_jl.
Let

    S=sum_l s_l* s_l+(rho0 b0)*(rho0 b0),
    sigma_n=(1+S/n)^(-1/2).

The vector rho0 f sigma_n has bounded B coefficients and actual derivative sum_l rho0 r_l tensor s_l sigma_n.
Testing it with a_j on the left and an arbitrary bounded c in B on the right yields

    tau(s_j sigma_n c)=<xi_i,a_j rho0 f sigma_n c>.

Take c=(s_j sigma_n)* and use ||sigma_n c||2<=||c||2.
The same estimate and monotone convergence give s_j in L2.
The symmetric argument is essential: no L2 bound for products of two previously obtained states is substituted for this separate step.

## Actual graph limit and weak form

For a simultaneous final approximation choose regular contraction sequences rho_n,sigma_n increasing strongly to1 with rho_n r_l, rho_n b0, and s_l sigma_n all bounded; the same row/column damping formulas provide them.
Then

    q_n=rho_n f sigma_n

has norm at most ||f||, converges in L2 to f, and belongs to the original closed coarse domain.
Its derivatives converge in coarse L2 to (1), because left/right multiplication of the now-L2 states by the uniformly bounded strongly convergent damping operators converges in L2.
Original closedness proves (1).

For any original polynomial q, the same B-module formulas and the ordinary core product rule give

    partial_i(q_n q)=(partial_i q_n)q+q_n partial_i q.

One can verify this directly from q_n's bounded-coefficient affine expression: first (s_l sigma_n)q belongs to the original graph by its B-module property.
Left multiplication by X_i preserves that graph, because the polynomial rule partial_i(X_i v)=1 tensor v+X_i partial_i v extends by closedness from the core to every original graph vector v.
Apply it to v=(s_l sigma_n)q and then multiply on the left by rho_n r_l in B.
The constant term is handled by the same B-module property.
The first terms converge by (1); the second converge because q_n are uniformly bounded and converge strongly as left multipliers.
Thus fq belongs to the original coarse graph and satisfies its product rule.
Contracting produces the actual normalized original weak commutator Theta(partial_i f) on all polynomial tests.
C_F0025's normalization invariance restores the specified original D_i0 weak form without a new domain assumption.

## Scope

This proof detects all minimal affine states over the von Neumann algebra annihilated by a coordinate derivation.
It does not assert that a general free rational function has such a single-coordinate affine expression, nor that its coefficients' other derivatives have finite rank.
The full general correlated criterion remains open.
The result is a direct rational-state mechanism and a rigorous exclusion of singular single-occurrence sandwich counterexamples under the actual vacuum assumption.


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
| argument | [Exact material](#kernel-affine-original-l2-states) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Under the exact normal polynomial-core vacuum assumptions, a bounded affine expression with minimal affiliated coefficients in the other-coordinate algebra has L2 left and right states, an actual original coarse derivative, and a finite-rank weak commutator for the distinguished coordinate.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:10 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#kernel-affine-original-l2-states) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core derivations, actual vacuum, inner phase and normalized original weak-form interface. |
| review | [Original finding](../audits/reviews/Yin_R_F0078_v1.md#verdict-and-exact-scope) | Actual complete original affine-state finding, with unknown initial context and unchanged distinguished-coordinate scope; the graph-action clarification is not reclassified as a substantive repair. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:55 |
| status | proved |
| reason | Adopt the newly performed isolated whole-proof finding at its exact scope after initial independent inspection and later historical comparison. Preserve the fixed mathematics, earlier decisions and exact non-review relations; historical checking relationships remain at their actual findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#kernel-affine-original-l2-states) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core derivations, actual vacuum, inner phase and normalized original weak-form interface. |
| review | [New whole independent finding](../audits/reviews/Yin_R_F0078_v1.md#f0101-whole-independent-20261023) | Complete current fixed proof at the exact hypotheses and limits stated in the new finding; earlier unknown relationships and their historical adoption are not reclassified. |

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
| argument | [Exact material](#kernel-affine-original-l2-states) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core derivations, actual vacuum, inner phase and normalized original weak-form interface. |
| review | [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0101) | Whole permanent proof: reducing original graph module, separate row and column damping, actual vacuum probes, extended trace limits, original product graph and distinguished-coordinate weak form. Other-coordinate weak forms are not claimed. |

Recorded mathematical summary: Under the exact normal polynomial-core vacuum assumptions, a bounded affine expression with minimal affiliated coefficients in the other-coordinate algebra has L2 left and right states, an actual original coarse derivative, and a finite-rank weak commutator for the distinguished coordinate.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Whole permanent proof: reducing original graph module, separate row and column damping, actual vacuum probes, extended trace limits, original product graph and distinguished-coordinate weak form.
Other-coordinate weak forms are not claimed.

Review: [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0101).

Material covered by that review: [Exact material](Yin_C_F0059_v1.md).
