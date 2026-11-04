---
author: Yin
---

# Conditional Gaussian anti-concentration after diagonalizing one GUE input

## Task associations

| Task | Scope |
| --- | --- |
| [F0012 contract](../tasks/Yin_T_F0012_v1.md#contract) | A concrete nonnormal subclass of the unperturbed GUE problem; success is partial progress, not completion of the all-polynomial contract. |

## Route

| Field | Value |
| --- | --- |
| disposition | superseded |
| priority | The subclass convergence deliverable is absorbed by the completed general route S_F0030; the direct conditional mechanism remains retained as development evidence. |

## Precise target and mechanism

First assemble and check Brown-measure convergence for \(P(x,y):=xy+2yx\).
Then extend to \(P(x,y):=q(x)+\sum_r f_r(x)y g_r(x)\) when the highest homogeneous part \(K_m\) of \(K(u,v):=\sum_r f_r(u)g_r(v)\) satisfies \(K_m(1,1)\ne0\).
A nonzero constant \(K\) is also included.
Condition on \(H_1\) and pass to its eigenbasis; the conjugated polynomial matrix remains jointly Gaussian in \(H_2\).
Apply Nie22 to that matrix, not to a generally degenerate sparse linearization.

The [conditional calculation](../ledger/Yin_L_F0058_v1.md#conditional-gaussian) gives the exact covariance, the trace split and the candidate polynomial least-singular-value estimate.
For degree \(m\ge1\), the scalar trace shift bounds the minimum coefficient with failure probability \(O(N^{3-B/m})\) for \(B>3m\).
The [common analytic bridge](../ledger/Yin_L_F0058_v1.md#common-bridge) explains why that estimate suffices.

## Inputs and remaining obligations

The [general linearization analysis](../ledger/Yin_L_F0058_v2.md#covariance-boundary) explains the route's contribution to F0012.
Success would validate a conditioning-and-elimination mechanism that creates a nondegenerate effective Gaussian noise map.
It would not supply induction on polynomial degree: general elimination produces repeated occurrences of the remaining random input and loses joint Gaussianity.
The full-class target is the [monic GUE-pencil estimate](../ledger/Yin_L_F0058_v2.md#monic-target), originally pursued by [S_F0028](Yin_S_F0028.md#route) and now established through [S_F0030](Yin_S_F0030.md#route).

Nie22 Theorem 1.6 and the CGP22/SS15 statements were inspected at their recorded editions; their proofs are external inputs.
The local calculation has been self-checked, but the assembled subclass result has not received a formal assessment or independent review.
No novelty is asserted.

The kernel hypothesis is only sufficient.
For \(K=u-v\), diagonal weights vanish and this particular global small-ball argument fails.
Conditioning does not leave a Gaussian matrix when the remaining input appears nonlinearly, so the route does not cover general F0012.

## Disposition and retained obligations

The completed [S_F0030](Yin_S_F0030.md#route) covers this subclass through the reviewed [general result](../claims/Yin_C_F0186_v1.md#statement).
The direct conditional calculation has not thereby acquired an independent review, and its particular quantitative exponents are not adopted as part of that result.
No further subclass proof is required for F0012.
Revisit this mechanism only for a separately justified quantitative or structural target.

## Evidence

[Search, calculations and remaining boundaries](../ledger/Yin_L_F0058_v1.md#source-boundary).
