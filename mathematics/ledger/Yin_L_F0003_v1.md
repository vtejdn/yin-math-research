---
author: Yin
---

# Boundedness after the Affiliated Main Theorem

<a id="boundedness-model-synthesis"></a>
Date: 2026-09-09.
**Historical checkpoint:** this note preserves the assessment and exploratory plan at that date, not a current execution queue.
The [current Task family record](../tasks/Yin_T_F0001_v7.md#current-decision) owns the later contract, selected lifecycle and separate pending completion-chain inspection.
Author: the coordinating agent.
Scope: synthesis and route selection for the user's [expanded Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#expanded-affiliated-and-boundedness-contract), using the exact new claims at their [Claim index](../claims/index.md).
This note assigns no additional universal conjecture and makes no novelty claim.

## The Main Theorem and the Two Analytic Questions

[Yin_C_F0013](../claims/Yin_C_F0013_v1.md#yin_c_f0013) is the desired affiliated main theorem.
With \(F_X=\operatorname{Div}_{U(M)}\mathbb C\langle X\rangle\), this theorem identifies finite bounded defects with membership in \(F_X\), and bounded finite commutators with \(F_X\cap M\).
The bounded-intersection assertion is refuted by [Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012).

Subsequent update, 2026-09-09: [Yin_C_F0022](../claims/Yin_C_F0022_v1.md#yin_c_f0022) extends the affiliated criterion to selfadjoint tuples with L2 conjugates, using canonical closed duals and defects on all bounded vectors.
[Yin_C_F0023](../claims/Yin_C_F0023_v1.md#yin_c_f0023) additionally constructs bounded normalized duals for all q in (-1,1), so Yin_C_F0013 itself applies throughout the canonical q-Gaussian family.
Both deductions have complete independent reviews; they do not establish either analytic property below.

Update, 2026-09-10: [Yin_C_F0024](../claims/Yin_C_F0024_v1.md#yin_c_f0024), at its claim-registry assessment, unifies the normal/bounded-dual and selfadjoint/finite-Fisher interfaces through dual and adjoint domains containing all bounded vectors.
Maximal Delta and the required continuity estimates follow from those hypotheses.
This broadens the main criterion without changing either analytic boundedness question or the existing model results.

The active analytic questions are distinct:

\[
\text{(L)}\quad F_X\cap L^2(M)\subseteq M,
\qquad
\text{(B)}\quad F_X\cap M=\operatorname{Div}_M\mathbb C\langle X\rangle.
\]

An affiliated free-field realization, a bounded dual system, and a homogeneous norm inequality serve different purposes.
None substitutes for the other two or proves (L)/(B) without the missing argument.

## Current Model Map

| Model and exact coordinates | Main-theorem applicability | Boundedness progress | Unresolved interface |
| --- | --- | --- | --- |
| Canonical d-dimensional q-Gaussian tuple | [Yin_C_F0023](../claims/Yin_C_F0023_v1.md#yin_c_f0023) constructs bounded normalized duals for every finite d and every -1<q<1; Yin_C_F0013 applies throughout. Yin_C_F0022 also applies through finite Fisher information | [Yin_C_F0020 B](../claims/Yin_C_F0020_v1.md#yin_c_f0020) proves both (L) and (B) for every nonzero real linear marginal, for all \(-1<q<1\) | The full multivariable rational coefficient geometry and scalar reconstruction. Bounded-dual existence is now settled in this model; neither (L) nor (B) follows merely from it |
| Free identically distributed bounded R-diagonal variables, positive-word holomorphic expansion | [Yin_C_F0017](../claims/Yin_C_F0017_v1.md#yin_c_f0017) needs neither normality nor duals. Yin_C_F0013 applies only after a separate valid normal-coordinate verification | Recognizable, weighted-L2 holomorphic coefficients give an actual bounded geometric matrix inverse and a value in scalar division closure | Whether a specified affiliated rational evaluation has this positive-word expansion. Regularity at zero alone does not establish that identification |
| R-diagonal \(a=uh\), with beta(4,4) modulus h free from Haar u | [Yin_C_F0019](../claims/Yin_C_F0019_v1.md#yin_c_f0019) explicitly constructs bounded duals for the normal generating pair (u,h) | \(a^{-1}\in F_{(u,h)}\cap L^2(M)\setminus M\), with squared L2 norm 7. Thus unrestricted (L) fails, even in a model to which Yin_C_F0013 applies | This does not refute the positive-word theorem or establish failure of (B) for this pair |
| One nonzero bounded R-diagonal a, with the intrinsic subspace \(H_{\mathrm{hol}}=\overline{\mathbb C[a]}^{L^2}\) | [Yin_C_F0021](../claims/Yin_C_F0021_v1.md#yin_c_f0021) needs neither normality nor duals, and even allows a kernel of a | Every \(f\in\operatorname{Div}_{U(M)}\mathbb C[a]\cap H_{\mathrm{hol}}\) lies in bounded scalar division closure. Its coefficient recurrence is derived from its rational equation | The analogous intrinsic implication for several noncommuting R-diagonal variables is not established |
| Sufficiently small selfadjoint analytic free transports of a semicircular tuple | [Yin_C_F0018](../claims/Yin_C_F0018_v1.md#yin_c_f0018) transfers bounded duals through a projectively invertible evaluated free Jacobian; the source's analytic inverse supplies generation | Scalar bi-Lipschitz transports satisfy both properties; rationally compatible multivariable changes inherit known results; a fixed pencil with a spectral margin remains bounded under quantified perturbation | General analytic transport need not preserve the rational fields or finite rank. The multivariable assertions remain unresolved |

## What the Models Suggest in Common

The positive proofs combine two concrete structures.

First, finite-dimensional coefficient dynamics converts actual L2 summability into decay.
In Yin_C_F0015 this is finite Hankel rank, equivalently a finite linear realization; its observable residual system has a Stein energy identity.
In Yin_C_F0017 multiplicative holomorphic words make that structure directly usable, and minimality propagates scalar summability to every matrix entry.
This is a link to finite linear systems and observability, rather than an unexplained assumption on a list of coefficients.

Second, homogeneous operator-norm estimates turn that decay into operator-norm convergence.
Yin_C_F0017 uses the square-root-degree strong Haagerup estimate.
The q model has a polynomial-degree Haagerup estimate in the actual q inner product, but orthonormalizing each degree separately does not preserve finite-dimensional word dynamics.
Its scalar q-Hermite recurrence is degree dependent and approaches a constant recurrence exponentially.
A controlled perturbation of finite-dimensional recurrence is therefore a meaningful candidate replacement for literal finite residual rank; it has not yet been proved to control general multivariable rational elements.

For (B), a third step remains essential: produce a bounded rational realization and perform valid scalar inverse elimination.
A norm limit of polynomials alone belongs to a norm-closed algebra and need not belong to division closure.
Yin_C_F0017 supplies this third step explicitly; Yin_C_F0015 alone does not.

## A Spectral Test for Proposed Differential Conditions

Before pursuing a condition involving conjugate variables, a Jacobian, or free difference quotients, test its behavior at scalar rational poles.
Property (L) necessarily implies the following elementary obstruction test: whenever a polynomial \(p(X)\) is regular but its affiliated inverse is unbounded, that inverse cannot be in L2.

Indeed let \(\mu_{|p|}\) be the spectral distribution of \(|p(X)|\).
Standard spectral calculus gives
\[
\|p(X)^{-1}\|_2^2=\int_{(0,\infty)}t^{-2}\,d\mu_{|p|}(t).
\]
For example a lower bound \(\mu_{|p|}((0,t])\ge c t^2\) for all sufficiently small t forces divergence of this integral, by the layer-cake formula \(2\int_0^\infty t^{-3}\mu_{|p|}((0,t])\,dt\).
This is a useful sufficient test for excluding that particular L2 inverse.
It is not asserted to imply (L) or (B) for all rational expressions.

The beta modulus in Yin_C_F0019 has spectral mass comparable to \(t^4\) at zero, allowing its inverse to be L2.
By contrast, a q-Hermite endpoint has mass comparable to \(t^{3/2}\), and an interior point has mass comparable to t.
The direct pole proof in Yin_C_F0020 therefore excludes every scalar rational pole.
Smoothness or boundedness of a conjugate variable alone does not express this spectral distinction: Yin_C_F0016 already supplies bounded Lipschitz conjugates together with an L2 pole.

This suggests searching for estimates that jointly control spectral mass near zeros and rational derivative states.
It does not justify announcing a new free-probability regularity criterion before its quantifiers and implications are proved.

## Next Discriminating Steps

1. **q-Gaussian:** derive a degree-dependent transfer equation for rational q-Wick coefficients with quantitative q-Gram control.
   Use the already computed cubic correction and the scalar resolvent recurrence as consistency tests.
   Prove a decay theorem for that equation before invoking the Haagerup estimate.
2. **Holomorphic R-diagonal:** Yin_C_F0021 now solves the intrinsic positive-subspace implication for one variable by identifying multiplication with a unilateral shift and deriving a finite recurrence.
   Investigate the corresponding several-variable implication, where a single scalar polynomial denominator is unavailable in general.
   The inverse obstruction and the bounded Haar resolvent outside the subspace are mandatory boundary tests.
3. **Analytic transport:** exploit structure of the actual transport Jacobian beyond projective summability.
   A projectively small invertible tensor can already send the vacuum projection to infinite rank, so finite-rank preservation requires a further invariant finite-dimensional space or a different rational reconstruction argument.
4. **Common analytic conditions:** compare quantitative inverse-state estimates, observability/coercivity and spectral lower-tail conditions.
   Bare finite Fisher information is already excluded.
   A stronger proposed differential condition must survive the beta and sandwich tests and yield an actual implication toward (L) or (B).

The model statements and their proof reviews record the mathematical progress at this checkpoint.
These next steps were exploratory obligations under the then-active Task.
