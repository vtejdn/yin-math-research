---
author: Yin
---

# Higher-degree polynomial witnesses for the anticommutator pair

Task: [T_F0003](../tasks/Yin_T_F0003_v2.md#contract).
Let h have law 4t^3 dt on (0,1), let b be a standard semicircular element free from h, and set Y=hb+bh.
Use the standard graded tracial model and the bounded operator K_Y fixed in [C_F0369](../claims/Yin_C_F0369_v1.md#argument).
That Claim contains the complete anticommutator bounded-dual construction, C*-recovery, affiliated nonmembership of b, exact b-degree-one divisibility test, commutator-pair obstruction and quadratic small-vector obstruction.
Its [selected assessment](../claims/Yin_C_F0369_v1.md#decision-quadratic-tests) relies on the [developer self-review](../audits/reviews/Yin_R_F0378_v1.md#quadratic-finding), not an independent inspection.
Those results do not settle the unrestricted closure equality for (h,Y).
Only the following continuing higher-degree candidate remains in this draft.

## Higher-degree polynomial extension: candidate, not adopted

A plausible strengthening for the anticommutator pair is
\[
 \{f\in\mathbb C\langle h,b\rangle:
          \operatorname{rank}[K_Y,f]<\infty\}
 =\mathbb C\langle h,Y\rangle.
\]
The proposed induction uses the highest b-degree N coefficient polynomial Q(t_0,...,t_N).
For each j, the block from H_(N-j) to H_(j-1) should isolate the j-th commutator insertion and give a kernel Q/(t_(j-1)+t_j), with the right tensor variables reversed.
Finite rank should force divisibility by that adjacent sum, and imposing this for every j should make their product divide Q and permit subtraction of a polynomial in h,Y.
Before adopting this statement, explicitly verify the boundary-layer formula, the finite-rank compression isolating every nonzero polynomial remainder, coprimality of the adjacent linear factors, and the exact highest-layer subtraction and induction.
The completed [b-degree-one argument in C_F0369](../claims/Yin_C_F0369_v1.md#an-exact-obstruction-for-witnesses-of-b-degree-at-most-one) does not supply those missing written checks automatically.
