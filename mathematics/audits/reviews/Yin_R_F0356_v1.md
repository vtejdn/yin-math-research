---
author: Yin
---

# Review of the projected singular product and paired block inequality

An agent for Yin independently checked both inequalities of [Yin_C_F0347_v1](../../claims/Yin_C_F0347_v1.md#statement) at 2026-11-17T04:53 UTC.
The reviewer did not participate in the proof development and received no development discussion, author explanation or prior verdict.
The initial derivation used the fixed Claim alone.
The reviewer then compared the cited draft reduction, the scalar bound and the stated scope of the Wigner application.

## Finding

Both inequalities hold with \(c_k=2^{3k}\binom{2k}{k}\) for the indicated dimensions and every permitted choice of singular vectors at ties.

For (1), the nonzero-volume case forces both \(TF\) and \(PRG\) to have rank \(k\).
Projecting \(RG\) orthogonally to \(TF\) gives \(PRG\), whose \(k\)-volume equals \(p_k(PR)\) because \(G\) spans the initial space of \(R\); this verifies the determinant in (3) and the invertibility of the normalizer \(S\).
The right factor in the normalized determinant map is the sum of a block diagonal contraction and an off-diagonal contraction, so its norm is at most \(2\), including when the two domain frames overlap.
For \(K=\ker(X-Y)^*\), the rank restriction gives \(\dim K\ge k\) and \(2\|X^*v\|^2=\|v\|^2\) on \(K\).
The two Rayleigh-quotient characterizations, each applied on a \(k\)-dimensional subspace of \(K\) in dimension \(2k\), place \(1/2\) between the \(k\)-th and \((k+1)\)-st eigenvalues of \(XX^*\).
Choosing the \(k\) largest eigenvalues of \(XX^*\) and the complementary factors from \(I-XX^*\) therefore contributes at least \(2^{-2k}\) to the central coefficient, with no cancellation.
Cauchy--Binet bounds the unnormalized coefficient by \(\binom{d_0}{k}^2p_k(T)^2p_k(T-R)^2\), because the volume of each column group is bounded by its global exterior norm under orthogonal compression.
Taking square roots and using \(d_0\le2k\) gives the claimed constant after cancellation of \(p_k(T)>0\).
If \(p_k(T)=0\), the removed left subspace contains the range of \(T\); if \(p_k(PR)=0\), the estimate is immediate.

For (2), keeping the head, \(k\) tail indices and all new indices on each side gives the matrix of the compressed exterior map.
Eliminating the diagonal head and then the auxiliary Schur block in every such minor leaves the same multiplier \(\det H\det A\) times the corresponding minor of \(T-U_2A^{-1}V_2^*\); this also works with the empty head.
The norm of this compression is \(p_r(M)|\det A|p_k(T-U_2A^{-1}V_2^*)\).
The exterior map of the projected perturbation factors through the one-dimensional \(\bigwedge^k\mathbb C^k\), so its norm is exactly the product of the two column volumes divided by \(|\det A|\), even if a border is rank deficient.
The left tail projection removes the next \(k\) vectors in the chosen singular basis, whereas the right tail retains every direction after the original \(r\); this recovers the two different projections stated in (2).
When the head product vanishes the lower bound is zero, and when \(A\) is singular a sequence avoiding the finitely many roots of \(\det(A+\epsilon I)\) preserves both projected volumes and gives the claimed limit.

The [draft's multiplicative target](../../drafts/Yin_D_F0009.md#auxiliary-block-interface) is exactly the interface this argument supplies, and the [scalar calculation](../../ledger/Yin_L_F0067_v2.md#paired-border-growth) gives coefficient \(1/2\) in the scalar paired inequality.
Neither prior argument is needed for the proof of (1) or (2); no priority or optimality conclusion was examined.
The estimates are deterministic, can have a zero right side and do not address the terminal range \(r>n-2k\).
They supply neither a probability bound for projected borders nor summability in the [planar defect criterion](../../claims/Yin_C_F0186_v27.md#statement), and hence no completion of the [Wigner Task](../../tasks/Yin_T_F0012_v3.md#contract).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0347_v1.md#statement) | Both deterministic inequalities, exact constant, ranks, dimensions, ties and endpoints. |
| [Finding](#finding) | [Compressed volume polynomial](../../claims/Yin_C_F0347_v1.md#argument) | Whole proof of (1), including the degenerate cases and coefficient bounds. |
| [Finding](#finding) | [Paired block application](../../claims/Yin_C_F0347_v1.md#block-application) | Whole proof of (2), including different left and right projections and singular Schur blocks. |
