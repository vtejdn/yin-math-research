---
author: Yin
---

# Minimal Rational States and Quantitative Observability

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0001_v1](../tasks/Yin_T_F0001_v1.md#yin_t_f0001) | The two-state test produced Yin_C_F0012: actual minimal monic states and the entire inverse can be L2 and unbounded, with finite-rank commutators and no alternative bounded scalar expression. The universal bounded-state upgrade is false. |

## Route

| Field | Value |
| --- | --- |
| disposition | refuted |
| priority | Historical goal outcome |

## Feedback and lineage

| Relation | Source | Scope |
| --- | --- | --- |
| predecessor | [Yin_S_F0002](Yin_S_F0002.md#s_f0002) | Former concrete bounded-state subroute; its universal bounded upgrade was refuted, while the original hypotheses and failures remain historical. |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0005"></a>
Current outcome, 2026-09-09: **refuted**.
The two-state test produced Yin_C_F0012: actual minimal monic states and the entire inverse can be L2 and unbounded, with finite-rank commutators and no alternative bounded scalar expression.
The universal bounded-state upgrade is false.
See [Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012) and the [goal completion audit](../audits/reviews/Yin_R_F0054_v1.md).
Earlier targets and tests below are retained as the route's research history.

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), preserving [Yin_C_F0001](../claims/Yin_C_F0001_v1.md#yin_c_f0001).
Registered: 2026-09-09, following the user's request to record the Kronecker-inspired strategy.
Priority and disposition: [route selection](#route), refuted universal bounded-state upgrade, formerly the active concrete subroute of Yin_S_F0002.
The original analytic targets below are retained as history.

## Exact Target and Logical Role

For a bounded f with all dual commutators of finite rank, construct a rational representation whose entire inverse is bounded, using the finite rational state data from Yin_C_F0007.
Then establish admissible scalar elimination, obtaining f in Div_M C<X>.
This is a **proposed sufficient mechanism** for Yin_C_F0001, not a proved equivalence or a claim about every minimal representation.

Yin_S_F0002 owns the general affiliated-to-bounded descent problem.
Yin_S_F0005 specifies a state-estimate approach to its remaining analytic step.
Yin_S_F0004 instead seeks a new model with a total word expansion and residual operations.
This route starts from actual evaluated rational states without assuming such an expansion.

## Verified Inputs

- [Yin_C_F0005](../claims/Yin_C_F0005_v1.md#yin_c_f0005) already puts f in the affiliated free field.
- [Yin_C_F0007](../claims/Yin_C_F0007_v1.md#yin_c_f0007) identifies the finite derivatives with rational tensors having factors in F_X intersect L2(M).
  For an explicitly reachable and observable monic realization

  \[
  f=uL(X)^{-1}v,\qquad L(X)=I_n-\sum_iA_iX_i,
  \]

  its left and right states are L2, rank[D_i,f]=rank_C(A_i), and n<=1+sum_i rank[D_i,f].
  These representation statements require scalar-origin regularity.
- [The reviewed Kronecker investigation](../ledger/Yin_L_F0010_v1.md#kronecker-strategies) proves the finite-observation reduction: choose words W so that the rows uA_w span C^{1 x n}.
  Boundedness of all rows uA_w L(X)^{-1}, w in W, makes the entire inverse bounded by an invertible scalar change of row basis.
- [JMS21-U001](../audits/literature/JMS21/Yin_U001_v1.md#jms21-u001) supplies a Gramian mechanism in coefficient space.
  It is a template, not an estimate already valid in L2(M).

## Original First Discriminating Test

Start with the **two-state monic minimal subclass with at least two nonzero coefficient matrices A_i**, retaining all original normality and bounded-dual hypotheses.
Here n=2 is the state dimension, not the number of generators.
One state is already elementary: minimality makes the scalars u,v nonzero, and L(X)^{-1}=(uv)^{-1}f is bounded; its scalar polynomial inverse is admissible.
Two states give the first nontrivial matrix-inverse test.
If only one A_i is active, Yin_C_F0004 already settles the scalar rationality conclusion.
In particular, a total commutator-rank budget of one reduces to that known case.

At registration, the first unexecuted test was whether the finite commutators control enough observable rows to prove

\[
\|\xi\|_{H\oplus H}\le C\|L(X)\xi\|_{H\oplus H}
\qquad(\xi\in H\oplus H),\quad H=L^2(M,\tau).
\]

Affiliated invertibility already gives dense range; this lower bound would give a bounded inverse.
In two states, observability supplies an index i such that u and uA_i are linearly independent: otherwise the line Cu would remain invariant under multiplication by every A_i, contradicting observability.
Thus the alternative is to bound exactly the rows uL(X)^{-1} and uA_iL(X)^{-1}.
Even the first is only known to be L2 from Yin_C_F0007; boundedness of their scalar compression f does not bound this row.
Their boundedness and the displayed estimate are targets, not proved consequences.
Test the given representation first; failure there redirects toward an admissible alternative representation and is not a counterexample to Yin_C_F0001.

## Coordinate and Scalar-Descent Obligations

The fixed-origin coefficient strategy is refuted by the checked Haar example f=(1-2U)^{-1}: its one-state realization has bounded states but coefficients 2^n.
Use estimates relative to the actual tuple, or a justified rational/Laurent coordinate chart.
When transferring Yin_C_F0007 to new generators, verify the transformed normality, dual relations, finite-rank class and scalar closure; [Yin_C_F0006](../claims/Yin_C_F0006_v1.md#yin_c_f0006) supplies specified admissible changes.
Recompute the minimal state dimension and rank bound after a change of chart; general admissible changes need not preserve either.
Existence of a suitable scalar chart for every free-field element remains unproved.

After a bounded inverse is obtained, prove scalar elimination separately.
A justified small-norm realization permits the [Miy22-U005](../audits/literature/Miy22/Yin_U005_v1.md#miy22-u005) pivot argument.
Otherwise find bounded scalar pivots or another applicable descent theorem.
[PV23-U001](../audits/literature/PV23/Yin_U001_v1.md#pv23-u001) explains why matrix inversion alone does not discharge this obligation.

## Continuation and Redirection

Continue if an estimate follows from the actual dual/finite-rank hypotheses, with the scalar chart and every inverse domain checked.
A proved two-state case is a restricted result; extension to arbitrary state size and elements without a scalar point of regularity remains necessary.
Record extra model assumptions as restrictions.
Stop an attempted fixed-chart coefficient argument when it assumes an implication contradicted by the Haar test.
A failure of boundedness for one chosen pencil refutes only that auxiliary assertion.

Evidence is owned by the linked ledger and source audits.
Scope review, 2026-09-09, another AI agent: independently checked the one-state reduction, two observable rows in dimension two, single-coordinate rank-budget case, the separate scalar-pivot obligation and the need to recompute state dimension after coordinate changes.
These checks delimit the strategy; they do not prove its proposed bounded-observation estimates.
No new search, numerical experiment, theorem promotion or Yin_T_F0001 completion is part of this strategy registration.

## Resolution Decision

2026-09-09, the coordinating agent: changed disposition from `active` to `refuted` after independent review of Yin_C_F0012.
The two-state test produced Yin_C_F0012: actual minimal monic states and the entire inverse can be L2 and unbounded, with finite-rank commutators and no alternative bounded scalar expression.
The universal bounded-state upgrade is false.
Yin_S_F0006 emerged from Yin_S_F0005; Yin_S_F0002's coordinating bounded-descent target includes that failed universal upgrade.
No old ID or argument was deleted, and no replacement goal was created.
