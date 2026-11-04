---
author: Yin
---

# Planar logarithmic defects through structured GUE smoothing

## Task associations

| Task | Scope |
| --- | --- |
| [F0012 contract](../tasks/Yin_T_F0012_v1.md#contract) | An alternative full-class sufficient condition based on planar logarithmic tails rather than a pointwise minimum singular value. |

## Route

| Field | Value |
| --- | --- |
| disposition | superseded |
| priority | The F0012 convergence obligation is absorbed by completed route S_F0030; structured-refresh overlap estimates remain unproved and are no longer required for this Task. |

## Precise target and mechanism

For ordinary singular values, set
\[
 F_N^z(t):=N^{-1}\#\{j:s_j(P(H)-zI)<t\},\qquad
 D_N(K,\varepsilon):=\int_K\int_0^\varepsilon F_N^z(t)\frac{dt}{t}\,d^2z.
\]
For every compact \(K\) and \(\delta>0\), seek
\[
 \lim_{\varepsilon\downarrow0}\limsup_N
 \mathbb P\{D_N(K,\varepsilon)>\delta\}=0.
\]
The [conditional bridge](../ledger/Yin_L_F0058_v1.md#averaged-route) explains how this yields the exact Task conclusion.

One stronger sufficient target is high-probability diagonalizability with eigenvector condition number at most \(N^{C_P}\).
It bounds the extreme-small-singular-value defect by the area of small disks around eigenvalues.
The retained three-scale argument combines this with pointwise mesoscopic estimates; no uniform-in-\(z\) source estimate is assumed.

## Inputs and obstruction

BKMS21 controls overlaps under independent additive Ginibre noise; this is a method model, not an applicable theorem for \(P(H)\).
Try the distribution-preserving input refresh
\(H_j(t):=e^{-t/2}H_j+\sqrt{1-e^{-t}}H'_j\).
The output noise is structured and nonlinear.
A quantitative nondegeneracy estimate for its overlaps or pseudospectral area is missing.

Planar averaging alone does not remove the logarithmic defect.
Nor can external output noise be removed using only its vanishing norm.
The [nilpotent-shift tests](../ledger/Yin_L_F0058_v1.md#failed-shortcuts) exclude both shortcuts.

## Disposition and retained obligations

The completed [S_F0030](Yin_S_F0030.md#route) establishes the exact Task by the pointwise singular-value route and a complete logarithmic-potential argument.
Its [reviewed conclusion](../claims/Yin_C_F0186_v1.md#statement) does not assert polynomial eigenvector conditioning or establish the proposed structured-refresh overlap mechanism.
Those auxiliary questions remain unproved; no further work on them is required for F0012.
A future investigation should identify a separate quantitative target before reactivating this route.

## Evidence

[Source inspection limits and search](../ledger/Yin_L_F0058_v1.md#source-boundary), [parameter order and localization argument](../ledger/Yin_L_F0058_v1.md#averaged-route).
