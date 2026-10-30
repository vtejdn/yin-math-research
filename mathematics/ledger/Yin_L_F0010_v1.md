---
author: Yin
---

<a id="kronecker-strategies"></a>
# Kronecker Mechanisms for Yin_T_F0001

Subsequent outcome, 2026-09-09: [Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012) completes the sandwich test with actual bounded duals and excludes every bounded scalar expression.
It refutes the universal bounded-state/descent upgrade, including the two-state test.
The derivations, proposed bridges and then-unresolved descriptions below are preserved as exploration history; current dispositions are in the [strategy index](../strategies/readme.md).

Date: 2026-09-09.
User-authorized investigation for [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), preserving [Yin_C_F0001](../claims/Yin_C_F0001_v1.md#yin_c_f0001).
This is a strategy assessment; proposed analytic bridges below are not proved claims.
Current priorities remain in the [route index](../strategies/readme.md).

## What the Classical Proof Contributes

[Par88-U001](../audits/literature/Par88/Yin_U001_v1.md#par88-u001) audits the actual Theorem 3.11 proof.
Together with [Miy22-U009](../audits/literature/Miy22/Yin_U009_v1.md#miy22-u009), it separates three mechanisms:

1. A finite-dimensional space of Hankel columns is invariant under the backward shift.
   Finite rank alone is insufficient; the Hankel intertwining relation supplies the invariance.
2. The induced finite-dimensional state operator gives a rational realization.
   Reachability and observability remove unused states and canceled poles.
3. Square summability excludes unstable states.
   This controls the entire minimal resolvent and is the analytic step to study for bounded descent.

For several letters, stable residual spaces and recognizable series already provide an algebraic analogue, audited in [BR10-U001](../audits/literature/BR10/Yin_U001_v1.md#br10-u001).
[Miy22-U003-U005](../audits/literature/Miy22/Yin_U003_v1.md#miy22-u003) realize both the residual and analytic steps in semicircular coordinates.
Repeating only formal rationality does not fill the present gap: [Yin_C_F0005](../claims/Yin_C_F0005_v1.md#yin_c_f0005) already gives S_D subset F_X intersect M.

## A Concrete State-Space Advance

[Yin_C_F0007](../claims/Yin_C_F0007_v1.md#yin_c_f0007) makes the finite derivative data algebraically canonical: its tensors agree with free-field rational derivatives, and their factors can be chosen in F_X intersect L2(M).
In the additional case of a minimal scalar realization regular at zero,

\[
f=uA(X)^{-1}v,\qquad A=I-\sum_i B_iX_i,
\]

the actual left and right states g=uA(X)^{-1} and h=A(X)^{-1}v belong to L2(M) entrywise.
Minimality and tensor slices, rather than an assumed orthogonal word basis, give this conclusion.
The same independent state families yield rank[D_i,f]=rank_C(B_i), and reachability gives n<=1+sum_i rank[D_i,f].
This is an actual finite-state dimension bound in the stated chart.
The authoritative statement, argument and review are in Yin_C_F0007.

This removes the need to guess rational factors in the initial finite-tensor decomposition.
It does **not** prove that all entries of A(X)^{-1} lie in L2 or M, or that the finite state spaces carry a Hilbert-space shift with the required stability.
General free-field elements need not have a scalar point of regularity; the monic-zero realization assertion has its stated restricted scope.

## The Most Useful New Literature Mechanism

[JMS21-U001](../audits/literature/JMS21/Yin_U001_v1.md#jms21-u001) provides the closest analytic template: for a minimal rational Fock-space series, square summability passes from the scalar coefficients to all state-entry series; a positive finite-dimensional Gramian then gives strict stability.
This is a noncommutative counterpart of excluding classical poles on the boundary.

For Yin_T_F0001 the discriminating next question is whether the bounded duals and the finite-rank hypothesis control **all necessary state observations** in the actual tracial Hilbert space.
In a chosen minimal realization, finite-dimensional observability gives finitely many words w such that the rows u B_w span all rows.
Therefore boundedness of each row u B_w A(X)^{-1} would give boundedness of the entire inverse.
Yin_C_F0007 supplies the initial L2 states, not these bounded observations.
One must construct residual operations that produce these rows with estimates, or a direct estimate

\[
\|\xi\|_{H^n}\leq C\|A(X)\xi\|_{H^n}
\quad(\xi\in H^n).
\]

Because A(X) is already invertible in affiliated operators, this estimate would make its inverse bounded.
This is a proposed sufficient target, not an estimate established by minimality or finite rank.

Even after obtaining that inverse, bounded scalar elimination remains necessary.
[PV23-U001](../audits/literature/PV23/Yin_U001_v1.md#pv23-u001) confirms that scalar and matrix rational domains are separately defined in the general realization literature.
For a contraction obtained in an admissible rational coordinate chart, Miy22's small-norm scalar-pivot argument is a concrete sufficient mechanism; arbitrary polar factorization or matrix inversion is not a substitute.

## Tests That Rule Out Naive Transfers

- General L2(M) membership does not give square-summable formal Taylor coefficients.
  A decisive example is Haar U and f=(1-2U)^{-1}.
  The denominator is a bounded unit, so f is in the original division closure; its minimal one-state monic realization has coefficient A_1=2 and g=h=f in M.
  Nevertheless its Taylor coefficients at zero are 2^n, not square summable.
  Its valid bounded expansion is instead f=-sum_{n>=1}2^{-n}U^{-n}.
  Thus even bounded minimal states and scalar-zero regularity do not yield stability at that fixed chart.
  This example, proposed by another AI agent and directly checked by the coordinating agent, refutes the fixed-chart coefficient inference while supporting the need for rational/Laurent coordinates.
  The weighted-disk example in Yin_C_F0007 separately refutes a universal rational-L2-to-boundedness shortcut, not Yin_C_F0001's bounded-f conclusion.
- A norm-convergent Neumann-series realization with polynomial matrix entries produces entries in the norm closure of C<X>.
  It cannot represent every desired element: Haar U^{-1} is already in the original division closure but outside that closure (indeed outside the L2 closure of C[U]).
  A global strategy must allow bounded rational coordinate changes or separate Laurent sectors.
  Scalar rescaling alone does not supply the missing convergence.
- For T_i=[D_i,f], Jacobi gives

  \[
  [T_i,X_j]=\delta_{ij}[P,f]+[D_i,[f,X_j]].
  \]

  The second term prevents the general commutator tuple from satisfying the one-variable divided-difference relation.
  Also, Par88's finite-codimension kernel argument cannot simply use multiplication by X_j as its shift.
  Each X_j has atomless spectral measure by compression of its dual relation; a proper closed finite-codimensional X_j-invariant subspace would give an eigenvector for X_j* in its finite-dimensional orthogonal complement.
  Thus the intended residual operation must differ from original normal multiplication.
  These are direct obstruction checks, not goal counterexamples.

## Decision and Search Evidence

Continue Yin_S_F0002 with **minimal rational states and quantitative observability** as the next bounded-realization test.
Following the user's request to record the new strategy, this mechanism is registered as [Yin_S_F0005](../strategies/Yin_S_F0005.md#s_f0005), with an initial two-state test and explicit coordinate/scalar-descent obligations.
Yin_C_F0007 also strengthens the input to Yin_S_F0001.
Retain Yin_S_F0004 as a model-specific route: its residual operation and norm estimates still need construction.
The general conjecture is open.

The 2026-09-09 search addressed finite-rank noncommutative Hankel operators, rational series, minimal realization, Fock Hardy stability, and matrix-centre domains.
Primary sources inspected were the local Par88 proof, existing BR10/Miy22 audits, JMS21 Lemma 3.4 and Theorem 3.5, and PV23 Section 4.3.
Searches also located Volcic's matrix-coefficient Hankel-module theory and scalar-domain corrections; they were not promoted to additional theorem inputs.
The search stopped after identifying a specific stability mechanism and its exact applicability gaps.
No exhaustive absence, novelty or priority conclusion is made; no private manuscript text was searched or uploaded.

The actual [Kronecker strategy and Haar review findings](../audits/reviews/Yin_R_F0055_v4.md#retained-kronecker-and-mechanism-clarification-reviews) retain their original 2026-09-09 evidence, repair and checking relationships.
