---
author: Yin
---

# Independent review of unary oscillation and low-matching cofactor refinement

<a id="finding"></a>
## Whole-proof finding

Review performed at 2026-11-05T10:56.
The human record author is Yin.
A separately assigned reviewing agent, outside substantive development of this proof, inspected the fixed [C_F0194_v4 statement](../../claims/Yin_C_F0194_v4.md#statement), [complete argument](../../claims/Yin_C_F0194_v4.md#argument), and [candidate decision](../../claims/Yin_C_F0194_v4.md#decision-unary-candidate), including all three declared direct dependency interfaces.
No exploration draft, proof-generation dialogue, author explanation or previous review finding was supplied or consulted.
The fixed proof and its accepted-input declarations were direct review inputs.
This is a fresh independent review of the complete v4 argument, not an inherited conclusion from reviews of earlier versions.

The mathematical verdict is positive for every assertion as stated, including the auxiliary unary estimate, conditional low-matching estimate, refined average, polynomial-shift consequence and explicit conditional counterexample.
No mathematical gap or unresolved source applicability was found within this scope.
The candidate's open status and the decision whether to adopt this finding remain responsibilities of C_F0194_v4.

### Obligations and decisive checks

For the support-sensitive oscillation step, the two rows formed from three distinct support points have nonzero determinant
\[
 (t_1-t_0)(t_2-t_0)(t_1-t_2).
\]
Their least singular value controls complex as well as real coefficient pairs.
Uniform continuity on the compact coefficient set \(\max(|q|,|l|)=1\) allows fixed positive-probability neighborhoods, so the lower probability and oscillation scale are independent of the particular coefficients.
For a law supported on two points, direct substitution gives \(\xi^2=(u+v)\xi-uv\).
Thus the effective coefficient is exactly \(l+(u+v)q\), including its possible vanishing.
The two cases exhaust a variance-one real law.
Neither argument uses moments of the unary variables.

The independent two-copy representation preserves the full joint law of the unary family.
On any selected set of at least s sufficiently weighted indices, the independent copy differences exceed a fixed multiple of the weight with a uniform positive probability.
The exponential indicator estimate therefore supplies a fixed multiple of s surviving sign coefficients, except with probability exponentially small in s.
At least half of those coefficients have a common real or imaginary projection of the required size.
After conditioning the copies, this projection remains a real linear polynomial of independent fair signs, even though the projection was selected from those copies.
Its threshold rank is at least a fixed multiple of s after scaling.
Choosing \(c_0\) sufficiently small makes the projected closed disk fit strictly inside a length-one interval.
The accepted degree-one source estimate yields \(Cs^{-1/2}\); enlarging C covers bounded s for which the guaranteed rank can be below the source threshold two.
Extra summands, arbitrary centers and complex coefficients introduce no missing condition.

The bordered determinant identity was checked with ordinary transpose and distinct shifts f and g.
Its quadratic, linear and constant coefficients give exactly the displayed q, l, b and R.
A maximal matching has fewer than r edges on the specified branch, and its endpoint set covers every threshold edge.
The fixed finite greedy choice is measurable in the minor alone.
For each possible selected set, conditioning on its exposed coordinates leaves the remaining raw row coordinates independent with their original law.
In particular, the proof does not select a cover from the unexposed row.

For the remainder, distinct unordered products \(x_jx_k\) are orthogonal in complex \(L^2\).
A shared-index cross term uses only \(\mathbb E\xi^2\) and \(\mathbb E\xi\); disjoint pairs have zero expectation by centering.
Each squared product has expectation one.
There are fewer than \(n^2/2\) retained pairs, and every retained coefficient has modulus below \(h\|A\|_F\).
Consequently
\[
 \mathbb E(|R|^2\mid D,a,y)
 =\frac4{n^2}\sum_{j<k,\ j,k\in T}|Q_{jk}|^2
 \le 2h^2\|A\|_F^2.
\]
There is no fourth-moment requirement or lost dimension factor.
Chebyshev at radius \((c_0\lambda/2)\|A\|_F\), followed by the unary bound at scale \(\lambda\|A\|_F\), gives the claimed \(C\chi(s)+C(h/\lambda)^2\) estimate.
The event inclusion uses no independence between the unary sum and its remainder.
The large-diagonal sufficient condition is valid precisely in the at-least-three-support-points case; the two-point effective slope is retained without discarding cancellations.

The [v3 statement](../../claims/Yin_C_F0194_v3.md#statement) and [v3 argument](../../claims/Yin_C_F0194_v3.md#argument) were read at the declared interfaces.
Their model, constants, nonzero-adjugate ratio, rank-at-least-\(n-1\) guard, pointwise averaging, normalized matching radius and independent-shift scope agree with v4.
Splitting each \(G_i\) into the matching branch, the low-matching large-count branch and the remaining low-count branch yields the refined average directly.
Both bounded branches are integrated with factor \(1/n\), rather than summed without that factor.
The last branch retains its actual \(G_i\) intersection.
This step uses no independence among principal minors and gives no meaning to N on a zero-adjugate branch.

For the polynomial consequence, the v3 finite-second-moment norm estimate and raw-normalized corank substitution apply with exactly the additional diagonal-law assumption stated in v4.
The exceptional probabilities remain \(C_Bn^{-B}\) on \(\Gamma_n\).
The inequality \(A>H+2K+2\) gives
\[
 C_1n^{2K+1-A}=o(n^{-H-1}),
\]
which satisfies the matching radius and, since \(H>L\), the unary radius for all sufficiently large n.
The new remainder error is \(n^{-2(H-L)}\).
The argument works for every allowed deterministic sequence \(r_n,s_n\); growth is needed only for the stated vanishing-error consequence.
Uniformity in deterministic shifts allows conditioning first on an independent random shift in the dimension and then integrating, including the guard \(\Gamma_n\).
It does not assert a conditional formula with that random shift left unconditioned, or require independence across dimensions.

For the Rademacher obstruction, direct multiplication gives \(B^TB=\left(\begin{smallmatrix}5&4\\4&5\end{smallmatrix}\right)\), so the singular values are 3 and 1.
The inverse is \(B^{-1}=\frac13\left(\begin{smallmatrix}-1&-2\\2&1\end{smallmatrix}\right)\).
These formulas verify the claimed adjugate, diagonal symmetric adjugate, full rank, absent off-diagonal edges and Frobenius ratio \(1/\sqrt5\).
The normalized border contributes norm \(\sqrt{(n-1)/n}\), and the Schur complement is identically zero because every Rademacher square is one.
Thus the full matrix has norm below four and exactly corank one.
All effective unary slopes vanish.
This verifies the stated conditional obstruction, without supplying an occurrence probability for an actual Wigner minor or a claim about other omitted indices.

### Source applicability and limits

The [MNV16 source unit](../literature/MNV16/Yin_U001.md#mnv16-u001), its edition note and the [primary 2016 journal PDF](https://theoryofcomputing.org/articles/v012a011/v012a011.pdf) were inspected.
The primary PDF text on pages 2 and 3 confirms equation (1.1), Definition 1.5 and Theorem 1.6, including real multilinear coefficients, independent fair signs, threshold rank at least two and arbitrary-center intervals of length one.
For degree one, the logarithmic degree factors in the second numerator vanish, giving the required inverse square root of rank.
The complex projection, arbitrary-law representation and conditional decomposition are project deductions checked above, not claims attributed to that theorem.
The original source proof and its external dependencies are accepted without a new full audit.
The already accepted v3 results are reused at their declared fixed scopes; this review does not recursively re-audit their accepted external source proofs.
No unresolved attribution or applicability issue was found for the substantive inputs used by v4.

The terminal mean of the tiny-ratio, low-matching, low-unary-count events is not estimated by this proof.
When \(r_n,s_n\) tend to infinity and that mean and the shift-guard failure vanish, the conclusion stated here is convergence of the displayed marginal probability, with no automatic summability.
The conditional counterexample does not refute an unconditional least-singular-value statement.
This finding does not establish completion of the general Brown-measure, matrix-determinant or scalar-determinant contracts and supplies no extension to genuinely complex off-diagonal laws or general matrix-coefficient pencils.
No formal verification or new numerical evidence is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finding) | [Exact v4 statement](../../claims/Yin_C_F0194_v4.md#statement) | Every asserted unary, conditional, averaged and polynomial-shift bound, support-sensitive weights, quantifiers, model, counterexample and stated limitation. |
| [Whole-proof finding](#finding) | [Complete v4 argument](../../claims/Yin_C_F0194_v4.md#argument) | Entire proof from three-point or two-point oscillation through the sign representation, normalized border decomposition, second-moment remainder, conditioning, refined average, polynomial scales and explicit Rademacher construction. |
| [Whole-proof finding](#finding) | [Candidate decision](../../claims/Yin_C_F0194_v4.md#decision-unary-candidate) | Exact declared statement, argument and all three dependency scopes; the finding leaves adoption and canonical assessment to C. |
| [Whole-proof finding](#finding) | [Accepted v3 statement](../../claims/Yin_C_F0194_v3.md#statement) | Exact normalized real model, constants, nonzero-adjugate many-index average, matching radius, rank guard and uniform independent-shift scope used by v4. |
| [Whole-proof finding](#finding) | [Accepted v3 argument](../../claims/Yin_C_F0194_v3.md#argument) | Applicability of pointwise averaging, normalized degree-two matching estimate and finite-second-moment norm/corank exceptions; accepted source proofs are not recursively re-audited. |
| [Whole-proof finding](#finding) | [Exact MNV16 input](../literature/MNV16/Yin_U001.md#mnv16-u001) | Primary 2016 journal equation (1.1), Definition 1.5 and Theorem 1.6 at degree one; real fair-sign polynomial, rank and interval hypotheses checked, original source proof accepted externally. |
