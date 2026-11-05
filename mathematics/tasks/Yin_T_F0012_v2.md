---
author: Yin
---

# Almost-sure Brown measure convergence for general GUE polynomials

This is the authorized almost-sure strengthening of the [completed probability-convergence contract](Yin_T_F0012_v1.md#contract).
The original contract, completion decision and its exact v1 support remain retained at that version.

## Contract

### Question

Fix \(d\ge1\) and a scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\) in self-adjoint indeterminates, with coefficients and degree independent of \(N\).
On a common probability space, for every \(N\), let \(H_1^{(N)},\ldots,H_d^{(N)}\) be independent normalized GUE matrices with density proportional to \(\exp(-N\operatorname{Tr}(H^2)/2)\).
No independence between different matrix sizes is imposed.
Let \(s_1,\ldots,s_d\) be free centered semicircular elements of variance one in a finite von Neumann algebra with faithful normal tracial state.
Write \(A_N=P(H_1^{(N)},\ldots,H_d^{(N)})\), \(a=P(s_1,\ldots,s_d)\), and
\[
 \mu_N=\frac1N\sum_{j=1}^N\delta_{\lambda_j(A_N)},
\]
with algebraic multiplicities.

Does \(\mu_N\) converge weakly to the Brown measure \(\mu_a^{\mathrm{Br}}\) almost surely, for every fixed \(d,P\) and every coupling across sizes with the stated within-size laws?
Precisely, for each fixed \(d,P\) and such coupling, the required conclusion is an event of probability one on which
\[
 \int\varphi\,d\mu_N\longrightarrow\int\varphi\,d\mu_a^{\mathrm{Br}}
\]
for every bounded continuous real function \(\varphi\) on \(\mathbb C\).
The event may depend on \(P\); simultaneous convergence over all polynomial coefficients is not requested.

### Scope and directly related objective

The model remains unperturbed GUE and includes nonnormal polynomial evaluations.
The selected earlier [pencil estimate and probability theorem](../claims/Yin_C_F0186_v1.md#statement) are established starting inputs at their actual scope.
The associated [affine determinant theorem](../claims/Yin_C_F0186_v2.md#statement) currently gives convergence in probability, not a strengthened convergence mode.

The same human instruction separately authorizes considering almost-sure and expectation convergence of the normalized logarithmic determinants in C_F0186_v2.
Retain the exact finite versus minus-infinite limit conventions and any \(L^1\) conclusion at that Claim's appropriate version.
That auxiliary strengthening is within this research round, but does not change the Brown-measure convergence statement above.

### Completion criteria

Give a complete proof of the almost-sure Brown-measure assertion under the stated coupling quantifiers, or a rigorous counterexample to it.
A counterexample must specify fixed \(d,P\), a coupling with the prescribed within-size GUE laws, a bounded continuous test function and a positive-probability event of failure of the asserted limit.
An estimate that only gives convergence in probability, or a subsequence without the full sequence, does not complete this contract.
Completion requires review of the complete proof or counterexample against these exact hypotheses, quantifiers and convergence mode.
Assess the associated affine determinant strengthening separately at its responsible Claim home.

## Current decision
[Selected decision](#decision-almost-sure-completed)

## Lifecycle and completion

### Decision almost-sure-reopened

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:29 |
| status | active |
| authority | Yin explicitly requested reactivating F0012 to consider almost-sure convergence, and strengthening C_F0186_v2 to almost-sure and expectation convergence. |
| reason | The probability-convergence contract is completed, while the stronger full-sequence almost-sure assertion and its necessary tail/concentration interfaces require new work and review. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Almost-sure contract](#contract) | Every fixed scalar polynomial, unperturbed normalized GUE, arbitrary coupling across sizes, and weak convergence on a probability-one event. |

### Decision almost-sure-completed

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:50 |
| status | completed |
| authority | Yin explicitly reactivated F0012 for almost-sure convergence and authorized the associated affine determinant strengthening; the current contract permits completion by a reviewed proof of its full assertion. |
| reason | C_F0186_v3 proves full-sequence almost-sure weak convergence for every fixed scalar polynomial and every coupling with the prescribed within-size GUE laws. Its independent whole-chain review checks the one-event planar passage and every original strengthened quantifier. The associated affine logarithmic almost-sure and expectation assertions are also established in that Claim. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Exact almost-sure contract](#contract) | One probability-one event for every fixed polynomial and allowed cross-size coupling, with convergence against every bounded continuous real test function. |
| support | [Strengthened result](../claims/Yin_C_F0186_v3.md#statement) | The complete almost-sure scalar Brown-measure conclusion, with the affine strengthened results assessed at their own Claim home. |
| support | [Complete proof](../claims/Yin_C_F0186_v3.md#argument) | Summable affine concentration, extreme-tail controls, exact linearization, Fubini and the pathwise local L1 potential passage. |
| review | [Independent whole-proof and contract finding](../audits/reviews/Yin_R_F0190_v3.md#independent-strong-proof) | Explicitly binds this exact contract and both selected supports, with the accepted external-input and non-formal-review limits. |

## Post-completion review

The [independent post-completion full-chain inspection](../audits/reviews/Yin_R_F0190_v7.md#post-completion-full-chain) checks this exact v2 contract and the complete C_F0186_v1--v3 chain at its stated external-input boundary.
It confirms that the selected statement and proof satisfy the GUE completion criteria, including arbitrary coupling, full-sequence almost-sure convergence and one event for all bounded continuous real test functions.
