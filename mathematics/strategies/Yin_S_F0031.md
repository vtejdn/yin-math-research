---
author: Yin
---

# Summable Gaussian concentration and integrable logarithmic tails

## Task associations

| Task | Scope |
| --- | --- |
| [F0012 almost-sure contract](../tasks/Yin_T_F0012_v2.md#contract) | Full-sequence almost-sure Brown-measure convergence for every fixed scalar GUE polynomial, with arbitrary coupling across sizes. |

## Route

| Field | Value |
| --- | --- |
| disposition | completed |
| priority | The affine almost-sure and mean limits, global integrable small-singular-value tail and exact almost-sure Brown-measure contract are established with independent review. |

## Mechanism and discriminating estimates

The [existing affine proof](../claims/Yin_C_F0186_v2.md#argument) gives a polynomial singular-value floor in probability and a mesoscopic expected counting bound.
Choosing the floor exponent large makes its norm-restricted failure probability summable, provided the GUE norm exception is also summable.
Apply Gaussian concentration to clipped logarithmic singular-value averages and smooth small-value counts at a slowly shrinking polynomial cutoff.
Their Lipschitz constants are of order \(1/(N r_N)\), where \(r_N\) is the singular-value cutoff, enabling summable deviations while the mesoscopic expected mass still tends to zero.

For expectation convergence, the additive Gaussian-radius error in the current tube bound cannot be integrated down to zero.
Integrate the exact polynomial uniform-ball estimate against the full chi-radius distribution, and control the growth of the deterministic repair constant outside a fixed norm event.
The target is a global power bound for extremely small singular values with no error independent of the singular-value threshold.
Use it to remove the negative logarithmic tail in expectation; treat a minus-infinite free logarithm separately by regularized upper bounds.

An almost-sure affine determinant theorem can feed the exact word-chain linearization of a scalar polynomial.
Check both finite and free determinant identities, then use Fubini to pass from a probability-one event for each fixed planar parameter to almost-everywhere parameter convergence on one event.
The final local logarithmic-potential and weak-measure passage must hold on that event for every bounded continuous test function.

## Relationship and completion scope

This strengthens the completed geometric route [S_F0030](Yin_S_F0030.md#route) without reopening its original probability-convergence deliverable.
The broader almost-sure target is the reopened Task version, while the associated affine expectation assertion belongs to an appropriate new version of C_F0186.
Do not infer expectation convergence from probability convergence or almost-sure convergence alone.
Do not assume cross-size independence in a Borel--Cantelli argument.
The strengthened claims and exact Task conclusion have complete derivations and applicable independent review.

## Current proof artifact

The accepted result is [C_F0186_v3](../claims/Yin_C_F0186_v3.md#statement), with the global integrable tail, mean convergence, summable concentration and the full Brown-measure passage.
The [whole-proof review](../audits/reviews/Yin_R_F0190_v3.md#independent-strong-proof) supports the exact [F0012 completion](../tasks/Yin_T_F0012_v2.md#decision-almost-sure-completed).
The [independent extreme-tail review](../audits/reviews/Yin_R_F0188_v2.md#integrable-tail-and-mean) separately checks the global estimate and expectation branch.
No proof obligation remains for this route's stated deliverable under its accepted external inputs.
