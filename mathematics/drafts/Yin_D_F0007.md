---
author: Yin
---
# Free-Haar quadratic-adjoint benchmarks and a spectral-graph normalization limit

## Question and development scope

This draft develops auxiliary left a*a and right aa* estimates for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The calculations were developed for Yin by the quadratic_haar_graph subagent under the root agent's assignment.
They are mathematical development and self-checking, not independent review.
The general correlated normal case remains unresolved.

Let (M,tau) be finite tracial with faithful normal probability trace, let H=L2(M,tau), and let P be a represented weakly dense unital star algebra.
Inner products are linear in the second variable, and the tensor actions are outer.
Let delta:P -> H tensor_2 H be a derivation with actual vacuum xi=delta*(1 tensor 1) in H.
Define the actual one-sided adjoint maps
\[
 T_\ell(a)=\delta^*(a\otimes1),\qquad T_r(a)=\delta^*(1\otimes a).
\]
The general tensor-adjoint domain formula guarantees their existence on P.
The needed inequalities are
\[
 \|T_\ell(a)\|_2^2\le C_\ell\|T_\ell(a^*a)\|_2,
 \qquad
 \|T_r(a)\|_2^2\le C_r\|T_r(aa^*)\|_2.
 \tag{Q1}
\]

The elementary bounded-H sufficient condition, including the positive-input adjoint pairing and the stronger centered-coordinate constant, is retained in [D_F0006](Yin_D_F0006.md#the-maps-are-actual-slice-adjoints).
It uses boundedness on H, which is stronger than the operator-norm-to-H conclusion of S.
It cannot be applied to arbitrary S witnesses without that additional hypothesis.

## Full mixed-word formulas for free Haar unitaries

Let U_1,...,U_d be freely independent Haar unitaries and fix i.
On the evaluated Laurent core, delta(U_j)=delta_ij 1 tensor 1 and delta(U_j*)=-delta_ij U_j* tensor U_j*.
The group-word orthonormal basis gives the actual vacuum xi=U_i.
The tensor-adjoint formula, evaluated on every reduced word w, gives
\[
 T_\ell(w)=
 \begin{cases}0,&w\text{ ends in }U_i^{-1},\\wU_i,&\text{otherwise},\end{cases}
 \qquad
 T_r(w)=
 \begin{cases}0,&w\text{ begins in }U_i^{-1},\\U_iw,&\text{otherwise}.\end{cases}
 \tag{Q4}
\]
The empty word falls in the second case.
For example, in the left formula the contraction of delta(w*)* can survive only at the first letter of w*, which is U_i precisely when w ends in U_i inverse.
Its surviving value is wU_i and cancels the a xi term.
All other word cuts have a nonidentity reduced first leg and hence zero trace.
The corresponding final-letter argument gives the right formula.
The surviving output words are pairwise distinct, so both maps extend to partial isometries on H with norm one.
Since ||U_i||2=1, the [bounded-H sufficient condition](Yin_D_F0006.md#the-maps-are-actual-slice-adjoints) proves both (Q1) with C_ell=C_r=1 on the entire mixed Laurent core.

## Adopted coordinate-local result

The initial selfadjoint/unitary coordinate proof, including the exact real-twist defect identity, actual adjoint transport, L2 error absorption and opposite-algebra right estimate, remains fixed in [C_F0158 v1](../claims/Yin_C_F0158_v1.md#statement).
The stronger [v2 result](../claims/Yin_C_F0158_v2.md#statement) incorporates root's completion of the square, the smaller constant ||2xi-U||2 and fixed-vector finite-family domination.
Its [selected decision](../claims/Yin_C_F0158_v2.md#decision-reviewed-quadratic) adopts the full statement and argument as proved after [independent review](../audits/reviews/Yin_R_F0167_v1.md#conclusion).
It applies to any distinguished selfadjoint or unitary coordinate of an arbitrary normal tuple satisfying A.
The other normal coordinates need not be selfadjoint or unitary, since [C_F0076 Part 1](../claims/Yin_C_F0076_v1.md#statement) makes their starred derivatives zero.
The fixed Claim owns that full argument; the auxiliary benchmarks above are not its proof dependencies.

## Continuing scope

For C3 spectral graphs of a free standard semicircular family, [C_F0137's projective K correction](../claims/Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) is H-bounded because the reference right annihilation is H-bounded.
However, subtracting its vacuum normalization introduces right multiplication by a vector eta, and H-boundedness of that multiplication requires eta in M rather than merely H.
The current calculation does not establish that additional point, so this bounded-H route remains incomplete.
The later [C_F0162 scalar-normal and freely independent result](../claims/Yin_C_F0162_v1.md#statement), using [C_F0160's fixed-vector lift](../claims/Yin_C_F0160_v1.md#statement), already proves both quadratic estimates for this free graph class without resolving the stronger H-bounded normalization point.
This class therefore supplies no remaining counterexample candidate to (Q1).
The unresolved search still includes correlated nonlinear graphs and other normal tuples for which bounded-H duals are unavailable and the unitary first-order defect calculation does not apply.
