---
author: Yin
---

# Negative inertia and the remaining determinant at a nonreal shift

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance Brown convergence](../tasks/Yin_T_F0012_v3.md#contract) | Count exactly real eigenvalues of a polynomial with a free positive symmetrizer. |
| [Matrix pencil determinants](../tasks/Yin_T_F0013_v1.md#contract) | Transfer the ordinary scalar logarithm to the associated affine pencil at the same prescribed shift. |
| [Scalar polynomial determinants](../tasks/Yin_T_F0014_v1.md#contract) | Determine the logarithmic contribution of the exceptional nonreal roots. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | At a prescribed nonreal shift, test the compression to the negative subspace of a finite factor whose positive free limit has spectrum reaching zero. |

## Real roots of an indefinite finite model

For \(PG=GP^*\) with \(G=G^*\), the negative index of \((P_N-t)G_N\) can increase across a real interval only by the number of real roots there counted with algebraic multiplicity.
The [inertia argument](../claims/Yin_C_F0358_v1.md#argument) treats finite singular metrics by compression to their ranges.
The [two endpoint inertias](../claims/Yin_C_F0358_v2.md#argument) bound the total nonreal count by \(2n_-(G_N)+\dim\ker G_N\).
For the stated positive free metrics this count is \(o(N)\) almost surely, also for Hermitian Wigner matrices with complex entries and factors sharing arbitrary inputs.
The [previous thin-support theorem](../claims/Yin_C_F0186_v25.md#statement) already gives weak convergence for the free-semidefinite products.
The exact count identifies which finite roots can still affect a prescribed nonreal logarithm.
Nakatsukasa and Noferini discuss finite-dimensional indefinite Hermitian eigenvalue counts in [NN19](https://doi.org/10.1016/j.laa.2019.05.010).
The argument used here is proved in the linked claims.

## The remaining probability question

Take \(A_N=2I+X_N\), \(B_N=X_NY_N+Y_NX_N+Z_NY_NZ_N\) and \(P_N=A_NB_N\).
The free factor \(2+s_x\) is positive and its spectrum reaches zero.
The finite factors share \(X_N\); conditioning on the negative eigenspace of \(A_N\) also conditions on part of \(B_N\).
At \(z=i\) the [loss criterion](../claims/Yin_C_F0358_v2.md#loss) asks whether the exceptional nonreal roots can approach \(i\) closely enough for a fixed positive normalized logarithmic loss along the favorable dimensions.
Set \(Q_N=1_{(-\infty,0)}(A_N)\) and \(C_N=|A_N|^{1/2}B_N|A_N|^{1/2}\).
The [exact determinant identity](../claims/Yin_C_F0358_v3.md#argument) leaves the compression of the unitary \((C_N+iI)(C_N-iI)^{-1}\) to \(\operatorname{ran}Q_N\), of dimension \(o(N)\) almost surely.
The [Hermitian comparison potential](../claims/Yin_C_F0358_v3.md#comparison) already has its ordinary limit.
At each fixed \(\epsilon>0\), bound the probability that the absolute determinant of this compression is below \(e^{-\epsilon N}\) on favorable dimensions.
The [negative-part bound](../claims/Yin_C_F0358_v3.md#sufficient) settles this test when \(\|B_N\|\sqrt{\|A_N\|\,\|(A_N)_-\|}\to0\) almost surely, even if \(A_N\) is indefinite infinitely often.
The two-moment input contract alone supplies no such norm bound.
A rank-only lower bound already fails for a bounded deterministic model.
On two sites take \(A=\operatorname{diag}(1,-1)\), \(B=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), and extend each by the identity.
Then \(n_-(A)=1\) while \(AB\) has the eigenvalues \(i,-i\) in every dimension.
To realize the displayed polynomial, take \(X=A-2I,\ Z=0\), set \(Y_{12}=Y_{21}=-1/4\) on the two sites and set \(Y=-I/2\) on their complement, with all other entries zero.
The matrices in this example are deterministic, so controlling the original Wigner law remains a separate probability question.
This route requires a positive free symmetrizer or factor, while the [ordinary row-restoration route](Yin_S_F0032.md#current-allocation-and-discriminating-tests) also covers free limits with two-dimensional Brown support.
