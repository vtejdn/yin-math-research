---
author: Yin
---

# Coupling-sensitive rejection tests for Wigner determinant strategies

This bounded comparison concerns [F0012](../tasks/Yin_T_F0012_v3.md#contract), [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract).
It records strategic exploration by an assigned agent for Yin on 2026-11-05, evaluated by the responsible research agent, rather than an independent proof review.
No supported alternative mechanism emerged in the inspected scope.
The comparison supports continuing the actual nonsymmetric product-inverse shift test, without claiming that success for that pilot would settle arbitrary matrix coefficients.

## Original objective and the changed probability threshold

The [finite-variance controls](../claims/Yin_C_F0186_v4.md#remaining-defect) leave the full F0012 objective equivalent to vanishing planar logarithmic defect.
The [reviewed carrier theorem](../claims/Yin_C_F0186_v7.md#remaining-boundary) handles a genuine restricted class by combining conditional symmetric shifts, a polynomial floor and intermediate singular values.
For general linearizations, the [actual-minor obstruction](Yin_L_F0059_v1.md#schur-findings) and [continuing block question](../drafts/Yin_D_F0010.md#negative-logarithmic-gap) remain relevant.

The determinant Tasks require less than full-sequence spectral convergence.
For finite free target c, the [reviewed exact criterion](../claims/Yin_C_F0190_v1.md#statement) requires the lower-deviation probabilities to have lower limit zero at every positive tolerance.
Thus a favorable deterministic dimensional subsequence can suffice under arbitrary coupling.
This observation changes the test of a proposed probability input, but supplies no missing random-matrix estimate.

## Sharp exponential positive moments still do not suffice

The [existing moment comparison](Yin_L_F0060_v1.md#comparison) already separates positive moments from inverse moments and the direction of determinant comparison.
The coupling criterion gives a sharper elementary rejection test.
Let X_N equal c with probability one half and c-1 otherwise.
For every fixed t>0,
\[
 \frac{1}{tN}\log\mathbb E e^{tNX_N}
 =c+\frac{1}{tN}\log\frac{1+e^{-tN}}2
 \longrightarrow c.
\]
Nevertheless the probability of X_N<c-1/2 is one half at every dimension.
A single common Bernoulli variable can make X_N=c-1 at every dimension on an event of probability one half.
Its upper limit then fails to equal c on that event, although every normalized exponential positive-moment rate has the correct limit.
This is a probability counterexample to the proposed implication, not a Wigner counterexample.
In particular a constant lower good-event probability, or a Paley--Zygmund lower bound that decays with dimension, does not meet the arbitrary-coupling contract.

A substantially stronger normalized fractional-moment convergence, with a suitable upper bound and uniform integrability, could force the required lower-tail control.
No independent mechanism establishing that stronger premise was found here.
Restating it as a new target would relocate the unresolved determinant problem.
Fixed negative moments are unavailable when the finite determinant has a singular atom, as in [the retained discrete examples](Yin_L_F0061_v1.md#discrete-expectation-obstruction).
Truncation would require a new estimate at the chosen truncation scale.

## First missing bridges for smoothing and coefficient products

Full Gaussian smoothing changes the source of regularity but also changes the evaluated nonnormal matrix.
Removing it would require a justified spectral-stability statement for the original output.
The [alternating cyclic-shift comparison](Yin_L_F0061_v2.md#brown-nonimplication) prevents deducing that stability from small rank or matching star-moments alone.
A purely atomic input law and its Gaussian smoothing also do not approach each other in total variation.
No replacement argument sufficient for the unperturbed contract was obtained.

Products of coefficient matrices may span more directions than the original coefficients.
The [retained covariance comparison](Yin_L_F0059_v1.md#symmetrizer) explains why this creates no independent noise in those directions by itself.
A multistep exposure would become a different mechanism only after constructing and controlling that randomness for the original pencil.
No such construction was found.
Merely asking for a block small-value estimate would repeat the existing obligation.

## Counterexample filter and limits of the source search

The real-symmetric witness argument remains in [the continuing matrix-pencil investigation](../drafts/Yin_D_F0012.md#real-symmetric-witness-subsequence).
A [common-phase zero-diagonal extension](../drafts/Yin_D_F0018.md#a-common-phase-zero-diagonal-witness-filter) is retained as a continuing algebraic counterexample-search filter.
It supplies no quantitative determinant bound and is not used as proved support for any Task or Claim here.

The strategic agent's bounded 2026-11-05 search tested symmetric random matrices with arbitrary nonsymmetric perturbations, non-Hermitian Kronecker models, and polynomial pseudospectral stability.
The symmetric-perturbation and Han leads returned to the [existing source frontier](Yin_L_F0061_v1.md#source-frontier).
The primary [Alt--Erdos--Kruger--Nemish record, arXiv:1706.08343v3](https://arxiv.org/abs/1706.08343v3), was inspected only at its title, authors, version and abstract.
No theorem or proof from that work was adopted.
Its abstract-level spectral-exclusion scope did not provide the missing lower determinant estimate; the [existing AEK19 comparison](../audits/literature/AEK19/readme.md) separately retains the flatness boundary.
This search does not establish theorem absence, novelty or a global impossibility for these mechanisms.
No further source preparation is needed for this limited negative assessment.

## Current allocation consequence

The [current route](../strategies/Yin_S_F0032.md#route) therefore retains the original planar objective and actual-minor boundary.
The concrete next technical test is [the actual product-inverse shift](../drafts/Yin_D_F0011.md#the-actual-nonsymmetric-shift) for a nonsymmetric three-factor polynomial.
It already has the required intermediate input and isolates the missing bottom logarithmic range.
A successful estimate would still need a genuine propagation argument before replacing the general matrix-coefficient obligation.
The moment and witness comparisons above are rejection and counterexample filters, not that propagation argument.
