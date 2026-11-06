---
author: Yin
---

# Independent whole-proof review of the approximately rank-two symmetric-shift floor

- Review act: 2026-11-05T15:11 UTC; human record author: Yin.
- Arrangement: an independently assigned agent outside substantive development of this proof inspected its fixed statement and entire argument.
  The review context contained the assignment, current framework rules and operational metadata, with no inherited proof-development discussion, author explanation or mathematical summary.
  No working draft, including D27, or earlier R finding was consulted.
- Inputs and sequence: the reviewer read [C_F0194_v9](../../claims/Yin_C_F0194_v9.md#statement), its complete argument and selected open decision, then checked the three direct dependency interfaces specified below.
  The accepted decisions of the two dependency Claims establish the adopted input scopes; their earlier independent review conclusions are not represented as a fresh recursive audit here.
- Source verification: Youla's retained 1961 publication, printed p. 694 / PDF p. 1, introduction equation (1), was read directly in extracted text and on the rendered page.
  The complete original source proof was not audited.
- Artifact and scope: the current C_F0194_v9 mathematical text selected by [decision-rank-two-candidate](../../claims/Yin_C_F0194_v9.md#decision-rank-two-candidate), dated 2026-11-05T14:59, including its model, every subsidiary deterministic assertion, probability and approximation arguments, random-shift form, and rank-three and parity boundaries.
  The Claim remains responsible for any later adoption of this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Exact statement](../../claims/Yin_C_F0194_v9.md#statement) | Complete model, uniform exact and approximate rank-two floor, L=a+1, independent random shifts, all included algebraic assertions, rank-three example, parity and general-shift limits. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Complete argument](../../claims/Yin_C_F0194_v9.md#argument) | Entire proof, including factorization, finite-rank identities, two-skew-update determinant and singular-value comparisons, parameter order, probability estimates, truncation, conditioning and the explicit rank-three construction. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Candidate decision](../../claims/Yin_C_F0194_v9.md#decision-rank-two-candidate) | Exact open candidate and its three declared dependencies; this review makes no C assessment decision. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Rank-three boundary](../../claims/Yin_C_F0194_v9.md#rank-three-boundary) | Verified deterministic counterexample to the finite coordinate-pair-update implication, its uniform even-dimensional extension and the stated limits of that negative result. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Accepted skew-floor decision](../../claims/Yin_C_F0194_v7.md#decision-complex-floor-reviewed) | Reuse only of its accepted even-skew floor for the same fixed real amplitude law, zero diagonal, even dimension and deterministic complex skew shifts. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Even-skew floor](../../claims/Yin_C_F0194_v7.md#even-floor) | Exact normalization, uniform shift-entry exponent and arbitrary fixed inverse-power failure exponent, applied three times; the accepted proof is not recursively re-audited. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Accepted second-moment decision](../../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Only the one-input second-moment estimate at positive-tail, specialized to identically zero diagonal. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Positive-tail input](../../claims/Yin_C_F0186_v4.md#positive-tail) | E tr_N(W_N^2)<=1 and its conversion to a polynomial operator-norm exceptional probability; no polynomial-tail, Brown-measure or other conclusion of that Claim is imported. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [You61 source unit](../literature/You61/Yin_U001.md#you61-u001) | The symmetric unitary-congruence statement of equation (1), its source identity and inspection limit; no dependence on this U's consumer link or any claimed project conclusion. |
| [Rank-two whole-proof finding](#rank-two-whole-proof) | [Symmetric congruence](../literature/You61/Yin_U001.md#symmetric-congruence) | Direct primary-source statement check at printed p. 694 / PDF p. 1, and the conversion from Q^T S Q to S=V diag(s_j(S)) V^T; the full source proof remains outside this review. |

<a id="rank-two-whole-proof"></a>
## Finding: the complete stated result is supported

No unresolved mathematical gap was found in the complete C_F0194_v9 statement and argument under the exact accepted inputs above.
The finding includes the positive exact and approximate rank-two floor, the subsidiary deterministic identities and rank-one specialization, and the negative deterministic rank-three boundary.
It supports acceptance at precisely that scope, without itself selecting a new Claim decision.

### Source factorization and deterministic algebra

The original You61 equation (1) applies to every square complex transpose-symmetric matrix and identifies the diagonal entries as the nonnegative square roots of the eigenvalues of S^*S.
It imposes no reality, Hermitian, positivity or nonsingularity assumption on S.
Thus the source supplies exactly the accepted statement needed here.
For V:=conjugate(Q), both V and V^T are unitary, and multiplication of Q^T S Q by their appropriate inverses gives the displayed factorization.
Taking the first two scaled columns, including zero columns when required, gives ||U||^2=||S_2||<=||S|| and ||S-S_2||=s_3(S).
The assertions include the zero and rank-one cases without an invertibility assumption on S or U.
The entry bound on F gives the same entry bound on each of sym F and skew F, hence their operator norms are at most N^(gamma+1).

For invertible A with A^T=-A, its inverse is transpose-skew, so K:=U^T A^(-1)U is transpose-skew for every number of columns of U.
The block determinant computation proves det(I+XY)=det(I+YX), which gives the stated small determinant identity.
Multiplication of the proposed inverse by A+UU^T leaves the coefficient I-(I+K)(I+K)^(-1)=0, proving the inverse identity at exactly its asserted invertibility hypothesis.
The bounds use ||U^T||=||U||, valid for the Euclidean operator norm also over complex matrices.
For one column K=0 and ||UU^T||=||U||^2, giving the stated unchanged determinant and rank-one inverse bound.
Combining this bound with the accepted skew floor and a fixed polynomial bound on ||S|| proves the claimed rank-one specialization.

For two columns K=kJ, J^2=-I_2 and ||J||=1.
The two perturbations A_+ and A_- remain complex transpose-skew, and the rectangular determinant calculation gives (1-ik)^2 and (1+ik)^2 with the stated signs.
The identity det(I_2+K)=1+k^2 and its displayed inverse formula follow by multiplication.
There is no use of conjugate transpose in these algebraic expressions.

The singular-value comparison is valid for nonnormal matrices.
For rank R<=2, ker R has dimension at least N-2 and I+R is the identity on that subspace.
The singular-value min-max formula therefore gives s_j(I+R)>=1 for j<=N-2; multiplying the singular values gives |det(I+R)|>=s_min(I+R)^2.
Moreover s_min(A^(-1)A_+/-)>=s_min(A_+/-)/||A||.
Taking square roots of the two determinant moduli proves both scalar-factor lower bounds and then the product lower bound for |1+k^2|.
This controls a determinant of a matrix differing from the identity by rank at most two, and does not estimate a ratio of two unrelated full determinants.

### Uniform probability, approximation and random shifts

Each of A, A_+ and A_- is W_N plus a deterministic complex transpose-skew shift when F is fixed.
Its shift entries are bounded by N^gamma+N^(gamma+1)<=N^(gamma+3) for all sufficiently large N, uniformly in the admissible F and the chosen factorization.
The exact C_F0194_v7 interface allows these non-Hermitian shifts for the same fixed centered variance-one real amplitude law and identically zero diagonal.
Its constants are uniform over this class, so three applications with failure exponent B+1 and one union bound supply the common least-value event without any independence among the three matrices.

In this model the direct calculation gives E||W_N||_F^2=N-1<=N, agreeing with the selected C_F0186_v4 input.
Consequently the norm exceptional probability is at most 4N^(1-2D), which is bounded by a constant times N^(-B) for the stated choice 2D>B+2.
The condition D>gamma+3 also makes ||skew F||<=N^D/2 eventually and ||U||^2<=N^D.
Only second moments of the original entries are used.

The choices are ordered without circularity: b is fixed from the skew-floor interface at gamma+3 and B+1, then D, h:=5b+4D, a:=h+3 and L:=h+4 are fixed.
On the common good event, ||K||<=N^(b+D), |1+k^2|>=N^(-2b-2D) and ||(I_2+K)^(-1)||<=2N^(3b+3D).
The correction term in the finite-rank inverse formula is at most 2N^(2b+D+3b+3D), yielding ||(W_N+F)^(-1)||<=3N^h.
All exceptional probabilities and dimension thresholds are uniform in F.

For general admissible F, the truncated shift F_2:=skew F+S_2 need not retain F's original entry exponent, but the proof does not require that assertion.
Its skew part is unchanged and its factor satisfies the same norm bound, so the three actual skew shifts still obey the already selected exponent gamma+3.
Thus the same b,D,h apply to F_2 without reselecting parameters.
The least-singular-value perturbation inequality gives s_min(W_N+F)>=N^(-h)/3-N^(-h-4)>N^(-h-3) for every sufficiently large N on the good event.
This verifies the strict inequality needed to exclude the stated event with threshold <=N^(-a), and gives exactly L=a+1.

The deterministic estimate is uniform over every fixed F in the displayed class, so integrating it over an independent random F_N restricted to Gamma_N proves the guarded random-shift form.
The entry and singular-value conditions defining Gamma_N are measurable, as is the least-value event.
No measurable choice of the auxiliary factorization is required because only the established deterministic probability bound is integrated.
Neither a spectral good event nor the shift guard is used to change the conditional law of W_N.
The proof is within each dimension and requires no independence across dimensions.

### Verified negative boundary and limits

For the displayed three-by-three K, direct determinant expansion gives det(I_3+K)=1+x^2+y^2+z^2.
At x=y=z=i/sqrt(3) this vanishes.
The displayed six-by-six block matrices multiply to the identity, and A^T=-A; hence A is invertible while A+UU^T is singular.
For each coordinate pair p<q, restriction to its two columns reduces the perturbation determinant to (1-ik)^2 or (1+ik)^2 with k=K_pq=i/sqrt(3).
All six factors are the nonzero real numbers (1+1/sqrt(3))^2 or (1-1/sqrt(3))^2.
The finite collection of invertible six-by-six matrices has finite norms and a positive minimum least singular value.
Direct sum with copies of J preserves such bounds uniformly for every larger even dimension, while preserving singularity of the symmetric update.
This is a valid counterexample to the asserted deterministic implication from those finitely many pairwise skew updates.
It supplies no counterexample with the required random Wigner law and an independent shift.

The odd-dimensional obstruction follows from det A=det(-A)=(-1)^N det A for every complex transpose-skew A, with F=0 already admissible.
Failure of the earlier symmetric-quantile guard does not imply the new small-third-singular-value guard: a symmetric shift diag(1,1,1,0,...,0) has s_3=1, while every principal symmetric minor has rank at most three, so its k_N-th singular value is zero once k_N>3.
The new proof therefore does not exhaust the complementary regime of that guard.
For a general symmetric rank r perturbation, the inverse formula still requires control of I_r+U^T A^(-1)U, and the verified rank-three example prevents deriving it from the listed coordinate-pair updates alone.

The accepted even-skew theorem is reused at its exact interface; its underlying earlier argument and adopted source proofs were not recursively re-audited.
The You61 proof beyond the inspected statement was not reviewed, and no formal verification is claimed.
No arbitrary complex-shift theorem, odd-dimensional floor, carrier determinant transfer or original Task completion follows from this review.
