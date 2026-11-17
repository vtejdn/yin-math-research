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
The [common-subsequence theorem](../claims/Yin_C_F0358_v4.md#statement) gives summable marginal small-determinant probabilities for both symmetrizer classes outside one deterministic polar set, on one subsequence extracted from any starting dimensions.
The set may contain the specified point \(i\).
For the shared-input cubic second factor above, the [Gaussian radius and negative-trace tests](../claims/Yin_C_F0360_v1.md#statement) do give the prescribed-shift equality, including \(i\), under their respective hypotheses.
The [bounded real first input estimate](../claims/Yin_C_F0361_v1.md#rates) allows arbitrary two-moment laws for the other colors and makes the compression close to minus identity with polynomially small failure probability.
The [purely atomic construction](../claims/Yin_C_F0361_v1.md#atomic) allows the first law itself to lack every moment above two on its selected dimensions.
When the first raw diagonal is a nondegenerate Gaussian and the second color is GUE or has the specified full complex translation modulus, the [conditional smoothing theorem](../claims/Yin_C_F0360_v2.md#statement) gives full-sequence almost-sure ordinary convergence at every prescribed nonreal parameter.
It permits arbitrary two-moment first upper entries and arbitrary two-moment third color.
For this degree-four product, the [summable strip-count theorem](../claims/Yin_C_F0365_v2.md#statement) permits arbitrary finite-variance laws of all three colors, including fully atomic inputs.
It yields the ordinary logarithm on all dyadic dimensions at each nonreal point outside a deterministic polar set.
At the prescribed \(i\), the [dilation estimate](../claims/Yin_C_F0365_v1.md#dilation) proves the limsup under the same unrestricted first and third laws whenever both raw laws of \(Y\) have the stated Hölder total-variation modulus under dilation.
For an arbitrary atomic middle law, on the specified favorable dimensions the [remaining loss](../claims/Yin_C_F0365_v2.md#fixed) involves only roots closer to \(i\) than \(N^{-b}\), for any fixed \(b>0\).
An exact root counts with infinite loss.
Thus a sufficient next estimate is a vanishing probability of any root in one such disk on a further subsequence; an estimate on the normalized sum of the log distances would suffice even when the disk is occasionally occupied.
With the test point kept at \(i\) and the first factor changed to \(c+X\), the [coefficient half-plane argument](../claims/Yin_C_F0358_v5.md#statement) gives summable deviations on all dyadic sizes for every real \(c>2\) outside a deterministic polar set, for every fixed selfadjoint second polynomial and arbitrary two-moment input laws.
Its clipped reference has a strictly positive first factor, and its estimates on compact subsets of the coefficient half-plane do not reach the endpoint \(c=2\).
This route requires a positive free symmetrizer or factor, while the [ordinary row-restoration route](Yin_S_F0032.md#current-allocation-and-discriminating-tests) also covers free limits with two-dimensional Brown support.
