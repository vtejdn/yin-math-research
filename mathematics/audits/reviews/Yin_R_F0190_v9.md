---
author: Yin
---

# Independent review of nonsymmetric finite-variance Wigner carriers

Review act: 2026-11-05T11:45.
The human record author is Yin.
This is a first whole-proof independent review of [C_F0186_v10](../../claims/Yin_C_F0186_v10.md#statement), including its model, complete argument, subsidiary assertions and [candidate decision](../../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-candidate).
The reviewer was outside substantive development of this proof and received the fixed Claim, exact dependency locators, assignment and applicable rules.
No exploration draft, development dialogue, author mathematical summary or earlier finding about this proof was supplied or consulted.
Obligations were enumerated from the statement before checking the forward argument and its direct inputs.
Earlier accepted project theorems and the retained FK source theorem are reused at their actual interfaces; this review does not claim a new whole-proof audit of those inputs or their original sources.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Exact statement](../../claims/Yin_C_F0186_v10.md#statement) | Entire carrier theorem and its two-sided, outer-polynomial and zero-shift ordered-product extensions, including finite-target, zero-polynomial and empty-product branches. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Exact model](../../claims/Yin_C_F0186_v10.md#model) | Fixed real centered finite-second-moment laws, normalization, within-dimension independence, arbitrary cross-size coupling and ordinary determinant conventions. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Complete argument](../../claims/Yin_C_F0186_v10.md#argument) | Entire proof, including guards, conditional floors, middle singular values, finite free logarithms, tail removal, arbitrary-coupling limsup, cyclic and polynomial transfers, algebraic boundary and symmetric-case comparison. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Candidate decision](../../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-candidate) | Exact statement, argument and all six declared dependency interfaces; the open candidate decision itself makes no unsupported acceptance or Task-completion claim. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Nonsymmetric floor decision](../../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed) | Accepted normalized real Wigner floor, uniformly for arbitrary polynomially bounded complex shifts and independent random shifts on guards; only a vanishing probability bound is used. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Nonsymmetric floor statement](../../claims/Yin_C_F0194_v5.md#statement) | Exact laws, N^(-A) threshold, polynomial entry bound, C_B N^(-B)+C sqrt(log(2+N)) N^(-1/18) error and absence of shift symmetry. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Random-shift floor interface](../../claims/Yin_C_F0194_v5.md#in-probability-floor) | Within-dimension conditioning, uniform constants and addition of a background-measurable guard failure; no conditioning on a whole cross-size sequence. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Intermediate theorem decision](../../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Real-input specialization, arbitrary independent complex shifts without norm restrictions, and the exact intermediate range and stretched-exponential error. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Intermediate theorem statement](../../claims/Yin_C_F0187_v2.md#statement) | Translation of s_(N-j) at j from ceil(N^(3/4)) through N-1 into a_r at r=j+1, including the largest singular value. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Finite-variance controls decision](../../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Accepted fixed-polynomial Hermitized weak convergence, positive logarithmic tails, fixed-regularizer limits and cyclic identities on the exact centered real submodel. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Positive logarithmic tails](../../claims/Yin_C_F0186_v4.md#positive-tail) | Expected uniform integrability of the positive logarithm, applied to each original fixed polynomial and converted to probability tail control. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Regularized potentials](../../claims/Yin_C_F0186_v4.md#regularized-potentials) | The universal almost-sure upper bound obtained from fixed positive regularizers and their countable decrease to zero. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Finite and free cyclic identities](../../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) | Exact finite determinant identity for all z and bounded-free block-Schur identity for nonzero z, with normalized block trace. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Norm guards and product inequality](../../claims/Yin_C_F0186_v6.md#argument) | Only the polynomial norm-event calculation and deterministic increasing-singular-value product inequality; no nonsymmetric use of its symmetric-shift theorem. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Marginal criterion decision](../../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed) | Accepted finite-target arbitrary-coupling limsup criterion on complete within-dimension input laws. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Marginal criterion argument](../../claims/Yin_C_F0190_v1.md#coupling-criterion) | Probability convergence supplies lower-deviation probabilities tending to zero, and a deterministic summable subsequence supplies the almost-sure lower limsup bound. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [FK source scope](../literature/FK52/Yin_U001.md#fk52-u001) | Retained accepted ordinary bounded multiplicativity in finite tracial algebras, including zero determinants and its disclosed source-proof limits. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [FK multiplicativity](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) | Applicability to bounded free root factors, arbitrary dependent ordered products and the cyclic identity at zero; no affiliated inverse is used. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Word reversal](../../claims/Yin_C_F0186_v6.md#word-reversal) | Comparison-only convention reversing words without conjugating scalar coefficients. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Symmetric carrier theorem](../../claims/Yin_C_F0186_v7.md#statement) | Comparison-only accepted stronger theorem when Q, every Q_nu and the combined H are reversal symmetric. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Symmetric ordered-product theorem](../../claims/Yin_C_F0186_v7.md#outer-polynomial-statement) | Comparison-only almost-sure zero-shift conclusion obtained from relabeled empty-carrier factors; it is not an input to the new nonsymmetric proof. |
| [Nonsymmetric carrier finding](#nonsymmetric-carrier-finding) | [Earlier carrier boundary](../../claims/Yin_C_F0186_v7.md#remaining-boundary) | Exact removal of the old whole-carrier reversal restriction and accurate distinction between zero and nonzero shifts. |

<a id="nonsymmetric-carrier-finding"></a>
## Whole-proof finding

No unresolved mathematical gap or source-applicability gap was found in the exact C_F0186_v10 statement and complete argument under its accepted inputs.
The proof establishes logarithmic convergence in probability to a finite free logarithm for every fixed certified carrier and parameter, and almost-sure equality of the dimension limsup under every prescribed cross-size coupling.
Its stated outer-polynomial, zero-shift ordered-product and two-sided extensions, together with their degenerate branches and algebraic scope boundary, are also supported.
This finding supplies independent review evidence at this fixed version; it does not itself select a Claim assessment or complete a Task.

### Obligations and conditional estimates

The statement requires a floor for each conditional factor, a background-measurable invertible-carrier event, control of all but o(N/log N) output singular values, a finite deterministic free target, removal of both logarithmic tails, and preservation of the arbitrary-coupling quantifier through every closure.
The subsidiary obligations include z=0, K=0, repeated distinguished indices, dependent factors, nonzero constants, identically zero outer polynomials, empty ordered products, cyclic transfer without inverses, and the distinction from general sums of sandwiches.
These obligations were checked against the full argument rather than only the principal displayed limit.

For each T_nu, the polynomial Q_nu omits its distinguished input and x_1.
Conditioning on the other inputs therefore leaves the exposed real Wigner law unchanged, and its norm event supplies the deterministic entry bound required by C_F0194_v5.
The floor input is already normalized by sqrt(N), so no raw-matrix rescaling is missing here.
Its broader diagonal allowance includes the centered diagonals of C10, and its complex nonsymmetric shift allowance includes all displayed Q_nu.
The arbitrary-power norm failures follow from C_F0186_v6 by choosing the norm exponent after B; the main floor error remains nonsummable.

The finite union of factor events and the deterministic least-value product inequality give the claimed carrier inverse bound without independence among the T_nu.
The scalar c is nonzero and is absorbed into a fixed exponent for sufficiently large N.
The chosen J_N uses only W_2,...,W_d, so defining F_N=Q-zH^(-1) there and zero elsewhere gives a measurable shift independent of W_1 with a deterministic polynomial norm bound.
The inverse is used only on the invertible event, and the factorization is used only on that event.
The final conditional floor and a union with J_N^c therefore prove Output-floor with probability tending to one, including at z=0 and with deterministic H=c when K=0.
The stated parameter order has no circular dependence.

### Middle values and the finite free target

The real-input case of C_F0187_v2 gives a_r(M)>=c(r-1)/N for q_N+1<=r<=N, uniformly over each conditional shift.
For L factors the iterated deterministic inequality has left index sum(r_nu)-(L-1), exactly as used in C10.
Distributing k+L-1 among L nearly equal positive indices gives r_nu-1>=k/(2L) and r_nu>=q_N+1 when k>=2L(q_N+1).
Their upper endpoints remain at most N.
For fixed L this range is nonempty for all sufficiently large N, and the nonzero scalar c is absorbed into c_0.
Thus Output-middle follows from the conditional intermediate events and J_N, without treating the latter as eventually almost sure.
The case L=1 uses the same valid range with harmless slack.

The weak law is applied to the original fixed polynomial R-z, not to the truncated rational shift F_N.
At each continuity point of the deterministic limiting singular distribution, weak convergence yields convergence of the empirical count in probability.
Output-middle bounds that count by k_N/N+C t^(1/L) on events with probability tending to one.
A positive deterministic excess of the limiting count over C t^(1/L) would contradict these two probability statements.
Decreasing continuity points to an arbitrary t preserves the bound by continuity from above.
Its limit as t decreases to zero excludes a zero atom, and integration of the count divided by t gives a finite negative logarithm.
Boundedness of R(s)-z gives the finite positive part.
The argument therefore establishes the finite target before using unregularized logarithmic convergence, with no free inverse or hidden full-rank theorem.

### Logarithmic passage and coupling

On the joint floor and middle event, the first k_N singular values contribute at most a_z k_N log(N)/N, which tends to zero because k_N=O(N^(3/4)).
For subsequent values below t, Output-middle confines their indices to at most C N t^(1/L), and summing log(N/k) gives the stated C t^(1/L)(1+abs(log t))+o(1) bound.
These estimates give precisely uniform vanishing of the negative tail in probability.
The accepted positive-tail expectation bound gives positive-tail control in probability by Markov's inequality.
Weak convergence of the clipped continuous logarithm then yields the finite logarithmic probability limit, even though singular finite matrices can occur on the vanishing exceptional events.
No convergence of the expected unregularized logarithm is needed or established.

For each fixed polynomial and parameter, the unregularized logarithm is bounded above by every positive regularization.
The accepted regularized almost-sure limits, intersected over a countable sequence of regularizers decreasing to zero, give the upper bound by the ordinary FK logarithm under every allowed coupling.
The proved probability convergence gives a deterministic subsequence with summable lower deviations from the finite target.
First Borel--Cantelli on that subsequence proves the reverse limsup inequality without cross-size independence.
The complete input spaces are finite-dimensional real entry spaces with their prescribed product laws, so they satisfy the marginal criterion's standard Borel setting.

### Closures, cyclic transfer and boundaries

For a nonconstant nonzero g(t)-z, scalar root factorization supplies finitely many carrier differences with finite targets.
Finite determinant multiplicativity and a finite union of probability deviations justify convergence of their sum even when the factors are dependent or some finite matrices are singular.
Bounded FK multiplicativity identifies the free target with that same finite sum.
The universal upper bound is then applied to the resulting fixed polynomial itself before invoking the marginal criterion.
This correctly avoids inferring a limsup of a sum from the individual limsups.
The same reasoning covers finite ordered products at zero, including shared inputs and noncommuting factors.
Nonzero constants, an identically zero polynomial factor and the empty product have the stated direct values.

For the two-sided carrier, U=H_L and V=(x_1+Q)H_R give exactly UV and VU in the claimed order.
The finite Schur identity applies for nonzero z and extends polynomially to zero.
The accepted bounded-free block identity has the correct normalized trace and gives equal determinants off zero; bounded multiplicativity gives equality at zero without division by a possibly zero determinant.
Root factorization transfers these exact identities to the outer polynomials, and the probability-sum argument handles their ordered products.
No equality of singular laws or least-value floors for the two cyclic forms is inferred.
Concatenating the right certificate before the left preserves omission of x_1, the permitted distinguished inputs and the nonzero scalar, including either empty list.

The one-occurrence words split uniquely into a word before x_1 and a word after it, giving the stated algebraic tensor description.
For d>=3, x_2 and 1 are linearly independent on the left, and 1 and x_3 are linearly independent on the right, so x_2 tensor 1+1 tensor x_3 has rank two.
An independent term H_L Q H_R contains no x_1 and cannot change that coefficient tensor.
Thus the example excludes precisely the asserted single-sandwich representation, without becoming a determinant counterexample.

The symmetric comparison uses v7 at its actual stronger scope.
When only Q and the Q_nu are reversal symmetric, each individual factor is a relabeled empty-carrier case, and its accepted zero-shift ordered-product conclusion permits the dependent product with the scalar absorbed into an outer polynomial.
The exact cyclic identity transfers that zero-shift conclusion to the two-sided form.
For Q=0 and H=x_2...x_d, each carrier factor has zero additive shift and the certificate is valid, even when the whole product is not reversal symmetric.
The comparison and this example accurately identify the enlargement without claiming full almost-sure convergence for the arbitrary-shift class.

### Source and review limits

All six declared logical dependency interfaces were read and matched to their uses, including the normalized floor, the intermediate index convention, the centered finite-variance weak controls, the two restricted v6 calculations, the finite-target marginal criterion and bounded FK multiplicativity.
The v7 assertions were inspected only as accepted comparison inputs, and the original scalar Task model was checked for the stated real centered submodel.
These accepted inputs are not recursively re-proved by this review.
The FK unit retains the original finite-factor source passages and its finite-tracial adaptation, including the zero-determinant extension; the present check concerns applicability of that retained bounded theorem and does not claim fresh primary-source inspection.
No unresolved citation or source-scope mismatch was identified in the argument reviewed here.

The finding does not assert a full-sequence almost-sure logarithmic limit for general nonsymmetric carriers, a full almost-sure Brown theorem, a theorem for general matrix-coefficient pencils, or completion of the unrestricted scalar-polynomial Task.
It asserts no common event over uncountably many parameters and no nonzero-shift conclusion for a general ordered product solely from the zero-shift closure.
No proof modification was made during this independent review.
