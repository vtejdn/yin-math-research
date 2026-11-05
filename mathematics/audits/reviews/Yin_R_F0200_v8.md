---
author: Yin
---

# Independent whole-proof review of random diagonal quantiles and the purely imaginary floor

Review act: 2026-11-05T13:55.
Human record author: Yin.
This is an initial independent whole-proof inspection of [C_F0194_v8](../../claims/Yin_C_F0194_v8.md#statement), including every assertion, auxiliary comparison, probability calculation, application and boundary in its [complete argument](../../claims/Yin_C_F0194_v8.md#argument).
The reviewing agent was outside substantive development of this proof and received its fixed paths, assigned scope and execution constraints without inherited mathematical development context.
No working Draft, proof-generation dialogue, author explanation or prior review conclusion about C_F0194_v8 was supplied or consulted.
The statement and proof were read directly, and their obligations were checked before forming this finding.
The sole adopted dependency was inspected at its actual consuming interface, as described below; its unchanged accepted proof was reused without a recursive proof audit.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#random-diagonal-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#random-diagonal-whole-proof) | [Exact eighth-version statement](../../claims/Yin_C_F0194_v8.md#statement) | Entire exponential quantile assertion, simultaneous principal compressions, elementary auxiliary assertions, arbitrary independent random shifts, all-dimension purely imaginary floor, noncentered and constant-law boundaries, and stated limitations. |
| [Whole-proof finding](#random-diagonal-whole-proof) | [Exact eighth-version argument](../../claims/Yin_C_F0194_v8.md#argument) | Complete new proof, including all singular-subspace comparisons, bounded-variable calculation, bounded conditional-law reduction, singular split, Frobenius count, guard application and boundary arguments. |
| [Whole-proof finding](#random-diagonal-whole-proof) | [Sole accepted dependency](../../claims/Yin_C_F0194_v7.md#decision-complex-floor-reviewed) | Only the accepted purely imaginary symmetric-quantile guarded floor at L0=1 and its independent-random-shift form, with the exact law, entry, dimension, quantile-index and probability interfaces checked; the unchanged accepted proof and its original source-inspection limits are reused. |

<a id="random-diagonal-whole-proof"></a>
## Whole-proof finding

The complete eighth-version argument supports all of its displayed assertions under their exact stated hypotheses.
No mathematical gap was identified.
The new diagonal estimate is uniform over arbitrary complex centers, and its use of the accepted seventh-version theorem yields the asserted all-dimension purely imaginary floor.
This conclusion concerns this Claim and its sole direct dependency interface, not completion of an original determinant or Brown-measure Task.

### Singular-subspace comparisons

The stated max-min description follows from the singular-vector decomposition and the dimension inequality for intersecting subspaces.
Its perturbation consequence uses the same good input subspace and loses at most the perturbation operator norm.
For the low-rank consequence, intersection with the perturbation kernel loses at most its rank, while leaving the original action unchanged.
These arguments apply to arbitrary complex matrices, without a symmetry assumption.

A good subspace for a principal compression embeds by zero extension, and the full output norm is at least its retained-coordinate norm.
Conversely, imposing both the input-coordinate and output-coordinate equations on a k-dimensional good subspace loses at most two complex dimensions.
After deletion, both input and output norms are preserved on this intersection.
Thus the stated bound at index k-2 holds for every deleted coordinate on the same full-matrix event, including coordinates outside the subsequently retained truncation set.
No union bound over deletions is needed.

### Exponential bound and truncation

For a bounded nonnegative variable, the chord inequality for the convex exponential has the direction used in the proof.
Multiplication of the independent exponential moments and Markov's inequality give the exponent with \(a_0:=1-e^{-1}-1/2>0\).
Both applications satisfy the boundedness and expectation hypotheses: the membership indicators have bound one and mean q, while the later squared diagonal terms have bound \(9M^2\) and expectation at least v.

Nonconstancy of a real law supplies two positively separated bounded intervals of positive probability.
A sufficiently large symmetric cutoff therefore has \(q>0\) and conditional variance \(0<v\le M^2\), even when the original law has no global moments.
Conditioning on a membership set of positive probability preserves independence of its retained coordinates and gives the common bounded conditional law.
For deterministic G, this also fixes its compression and singular split before the retained coordinate values are sampled.
The membership failure is exponentially small, including the case q=1, where the actual failure probability is zero.

### Singular split and counting

If the retained deterministic compression has at least \(k_N\) singular values strictly above \(2M/\sqrt N\), the bounded diagonal perturbation leaves its kth singular value strictly above \(M/\sqrt N\).
If it has fewer, the complementary deterministic part has operator norm at most \(2M/\sqrt N\), and the perturbed remainder B has operator norm at most \(3M/\sqrt N\).
The split is determined by a spectral projection, so repeated singular values introduce no measurable-choice problem.

For each retained diagonal entry, its complex deterministic center does not affect the lower bound v on the expected squared magnitude.
The diagonal squares are conditionally independent, and their sum gives a lower bound for the full Frobenius norm.
Consequently, outside the stated conditional exponential failure, \(\|B\|_F^2\ge vm/(2N)\).
Counting singular values at least \(c_0/\sqrt N\), with \(c_0:=\sqrt v/2\), against the operator-norm bound yields
\[
 t\ge \frac{vm}{36M^2}.
\]
This counts all singular directions of B and does not assume independent singular values.

Since \(m\ge qN/2\), the resulting linear lower bound eventually exceeds \(2k_N\), whereas \(k_N=4\lfloor\sqrt N\rfloor+3\) grows only as \(\sqrt N\).
The deterministic part removed in the small-rank branch has rank strictly below \(k_N\), so adding it back still leaves at least \(k_N\) good directions.
In the large-rank branch, \(c_0\le M/2\) gives the same final threshold.
All required size inequalities can therefore be imposed by one law-dependent dimension threshold.

The conditional failure bound is uniform in both the membership set and the deterministic matrix.
Averaging it, adding the membership failure, and then using the compression comparisons proves the entire event in Diagonal-quantile with constants depending only on the fixed diagonal law.
Conditioning on an independent random G preserves these constants; no size restriction on G or independence across dimensions enters this argument.

### Exact seventh-version interface and application

The dependency's accepted decision explicitly includes its [purely imaginary guarded theorem](../../claims/Yin_C_F0194_v7.md#quantile-guard-floor).
That theorem allows a centered variance-one real eta, an independent fixed real finite-second-moment diagonal law without a centering assumption, arbitrary deterministic complex polynomially bounded shifts, and every sufficiently large dimension.
These are exactly the hypotheses imposed in the eighth-version least-value application.

For upper entries \(i\eta_{jk}/\sqrt N\) and conjugate lower entries, transpose symmetrization cancels every off-diagonal noise entry.
Thus the symmetric part is precisely the real random diagonal plus \(\operatorname{sym}F\), and symmetrization commutes with the principal deletion used by the old guard.
The old guard index \(4\lfloor\sqrt N\rfloor+1\) equals the new \(\ell_N=k_N-2\).
For large N, \(c_0/\sqrt N\ge N^{-1}\), so the new simultaneous compression event implies the exact old guard with L0=1.

The least-value event is contained in its intersection with that guard together with the guard's complement.
The accepted theorem bounds the first event, and the new exponential estimate bounds the second without conditioning on the guard.
The latter error is absorbed into any fixed polynomial error after changing its constant and dimension threshold.
This preserves the asserted uniformity over polynomially bounded complex shifts and imposes no parity restriction.

For a shift independent of the whole Wigner matrix, conditioning on that shift is valid for both estimates.
Integrating the deterministic bound only over its polynomial entry guard gives the claimed bound for the least-value event intersected with Gamma_N.
Adding the complement probability gives the unguarded form.
The symmetric-quantile guard itself may depend on the noise diagonal throughout.

### Boundary and source limits

A nonzero diagonal mean is absorbed into the deterministic center of each squared diagonal term and causes no missing centering hypothesis.
For a constant diagonal law, the specified scalar shift makes the random-diagonal matrix identically zero.
In the Wigner application it leaves a transpose-skew matrix, whose odd-dimensional determinant vanishes by the stated transpose and sign identities.
That shift obeys every fixed positive polynomial entry bound eventually.
This verifies the necessity of excluding constant laws for the asserted uniform all-dimension conclusion and the identification of the centered constant case with the zero law.

The new quantile proof consists of the displayed finite-dimensional subspace and bounded-variable calculations; it uses no additional unresolved external probability theorem.
The old guarded theorem remains an accepted mathematical input at the exact scope inspected here.
Its proof, earlier review and external-source proofs were not independently re-audited in this review, and their existing inspection limits remain unchanged.
No novelty or priority conclusion is supplied.
The matching error remains nonsummable at the displayed rate, and neither a matrix-coefficient determinant theorem nor a full-sequence Brown-measure conclusion follows from this review.
