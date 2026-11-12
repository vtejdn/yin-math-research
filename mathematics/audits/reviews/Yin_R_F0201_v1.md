---
author: Yin
---

# Third-moment Wigner singular counts: independent whole-proof review

The review act was performed at 2026-11-11T13:34 UTC under human record author Yin.
The target is the 2026-11-11 candidate [C195v1](../../claims/Yin_C_F0195_v1.md#statement), with its count-candidate decision dated 2026-11-11T13:29 and complete argument at its fixed v1 path.
The reviewer was separately assigned outside the substantive development of this proof.
Only the assignment, applicable rules and startup facts, fixed candidate, and necessary fixed dependencies and source interfaces were supplied.
No proof-development dialogue, exploration notes, author explanations, or prior review conclusion about C195v1 was supplied or consulted.
The reviewer formed initial findings by reading the statement and complete proof, then checked the necessary source and dependency interfaces.
The candidate was not edited and no substantive repair was contributed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#wigner-count-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#wigner-count-whole-proof) | [C195v1 statement](../../claims/Yin_C_F0195_v1.md#statement) | All stated affine comparison, affine count, shrinking-scale and scalar-polynomial conclusions under their exact moment and independence assumptions. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C195v1 argument](../../claims/Yin_C_F0195_v1.md#argument) | The complete argument through Polynomial-squared-count, including coordinate replacement, covariance interpolation, counting and polynomial transfer. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C186v8 affine input](../../claims/Yin_C_F0186_v8.md#goe-affine-input) | Exact GOE and free normalization and the affine Schultz specialization only. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C186v8 mesoscopic count](../../claims/Yin_C_F0186_v8.md#goe-mesoscopic-count) | Matrix-valued algebraicity, exclusion of the zero pole and the power bound used in C195; no least-value or logarithmic-limit assertion. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C186v1 word-chain pencil](../../claims/Yin_C_F0186_v1.md#polynomial-application) | The explicit word-chain construction, everywhere invertible triangular auxiliary block and exact Schur complement only. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C186v8 scalar free input](../../claims/Yin_C_F0186_v8.md#goe-scalar-brown) | Nonconstancy of the squared scalar polynomial, its free atomlessness and power behavior, and finite free logarithm of the word-chain pencil only. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C186v2 algebraic interface](../../claims/Yin_C_F0186_v2.md#logarithmic-tail) | The SS15 matrix-valued algebraicity/Puiseux implication from absence of a zero atom only; the GUE comparison is not used. |
| [Whole-proof finding](#wigner-count-whole-proof) | [C186v3 bounded factorization](../../claims/Yin_C_F0186_v3.md#linearization-transfer) | Direct bounded Fuglede-Kadison block factorization and normalized determinant identity only, not the alternative probability-limit proof. |
| [Whole-proof finding](#wigner-count-whole-proof) | [Sch05 specialization](../literature/Sch05/Yin_U001.md#goe-hermitization-specialization) | Accepted Theorem 3.2, equation (3.6), with its stated auxiliary trace, variances and strictly positive imaginary parameter. |
| [Whole-proof finding](#wigner-count-whole-proof) | [FK52 bounded multiplicativity](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) | Accepted bounded product formula, including zero determinants, in the stated finite tracial algebra. |
| [Whole-proof finding](#wigner-count-whole-proof) | [MS24 determinant convention](../literature/MS24/Yin_U001.md#determinant-convention) | Ordinary logarithmic determinant and normalized amplification convention only. |

<a id="wigner-count-whole-proof"></a>
## Whole-proof finding

The complete candidate is mathematically supported at its exact stated scope.
No unresolved gap was found in the Wigner-GOE comparison, Affine-count, Shrinking-count, or Polynomial-squared-count.
The following checks supply the substantive basis for this finding.

### Replacement and covariance interpolation

The input model is the fixed-law, within-size independent Hermitian model in [F0012v3](../../tasks/Yin_T_F0012_v3.md#contract), with the candidate's additional third off-diagonal moments.
Each raw complex entry changes a Hermitian matrix by a direction of rank at most \(2p\) and norm at most \(\|B_j\||h|/\sqrt n\).
The differentiated resolvent product therefore has normalized trace bounded by the claimed \(2r!\|B_j\|^r|h|^rn^{-1-r/2}\eta^{-r-1}\).
The estimate uses the rank of that product and the Hermitian resolvent bound, without an entry truncation or norm event.

For a raw diagonal coordinate, conditioning leaves its mean zero.
The second derivative bound gives an expected \(O(n^{-2}\eta^{-3}\mathbb E\zeta_j^2)\) error; summing \(dn\) coordinates gives the required diagonal term.
Thus inserting GOE diagonals after the off-diagonal comparison uses only second moments.

For each off-diagonal pair, the linear and quadratic Taylor terms depend exactly on the mean vector and full real covariance.
Replacing the pair jointly therefore cancels those terms even when its two real components are dependent.
The third directional derivative remainder has expectation \(O(n^{-5/2}\eta^{-4})\) with the stated third-moment constant, and summing the pairs gives \(O(n^{-1/2}\eta^{-4})\).
A covariance-matched Gaussian has uniformly bounded third absolute moment because its real covariance has trace one.
Singular covariance is permitted.

The covariance contraction was expanded directly in the two directions \(X+Y\) and \(i(X-Y)\).
The coefficient of \(D_XD_Y\) vanishes because both entry laws have total variance one; the remaining coefficients are \(c_j-1\) and \(\overline c_j-1\), with the signs shown in the candidate.
Cyclicity of the full trace gives
\[
 \operatorname{Tr}(RXRXR)
 =\operatorname{Tr}_p\bigl(B_jR_{ba}B_j(R^2)_{ba}\bigr).
\]
The Hilbert-Schmidt trace inequality and Cauchy-Schwarz over pairs bound the sum by the product of the full Hilbert-Schmidt norms.
This yields \(2\|B_j\|^2\eta^{-3}\) after dividing by \(pn\); no factor of \(n\) remains in that block sum.
Gaussian integration by parts contributes the separate factor \(1/(2n)\), which includes the square of the raw-entry normalization.
Integrating in the interpolation parameter therefore gives \(O(n^{-1}\eta^{-3})\).
The argument remains valid when a covariance is singular by representing it as a linear image of standard real Gaussians.
Bounded derivatives justify the interior identity, and continuity plus its uniform bound gives the endpoint comparison.

All those estimates are uniform in the Hermitian deterministic constant \(B_0\).
The candidate restricts this uniformity to the Wigner-GOE step, as required; the subsequent free comparison has its separate fixed-pencil constant.

### Affine count and shrinking scale

The Hermitian dilation has eigenvalues \(s_k,-s_k\), with both signs counted and normalized by \(2mn\).
Consequently its resolvent satisfies the candidate's exact identity
\[
 -t\operatorname{Im}G_{H_n}(it)
 =\frac1{mn}\sum_k\frac{t^2}{s_k(L_n)^2+t^2}.
\]
The kernel is at least one half on \([0,t]\), including a zero singular value.

The Schultz specialization uses \(a_0=0\), \(a_j=B_j/\sqrt2\) and \(\lambda=itI-B_0\).
Its imaginary part is \(tI>0\), the constant is included once, and the real and free symmetrizations have variance one.
No invertibility of \(A_0\) is required by this comparison or by the counting step.

A finite ordinary free logarithm excludes a zero atom of the Hermitization law.
The accepted algebraic/Puiseux interface and the bound \(|G(it)|\le t^{-1}\) exclude all exponents below \(-1\), while the vanishing atom excludes the exponent \(-1\).
The resulting bound \(t|\operatorname{Im}G(it)|\le Ct^\beta\), for some \(0<\beta\le1\), is therefore applicable.
Multiplying both resolvent comparisons by \(t\) gives the displayed count errors \(n^{-1/2}t^{-3}\) and \(n^{-1}t^{-6}\), with the smaller powers absorbed for \(t\le1\).
The two necessary exponent conditions are \(\gamma(3+\beta)\le1/2\) and \(\gamma(6+\beta)\le1\).
The candidate's strict range \(0<\gamma<1/(6+2\beta)\) satisfies both.

### Scalar-polynomial transfer

For each word, the retained chain has the stated polynomial inverse and reproduces that word in \(-BQ^{-1}C\).
Concatenation therefore supplies the exact pencil for the arbitrary fixed polynomial, including the affine case with auxiliary size one.
No input norm bound enters this algebraic identity.

On the right-singular subspace of \(S=P(W^{(n)})-zI\) corresponding to \([0,t]\), the graph map \(x\mapsto(x,-Q^{-1}Cx)\) is injective and cannot decrease norm.
The image has the same dimension and every vector there satisfies \(\|Lv\|\le t\|v\|\).
Applying min-max to \(L^*L\) gives precisely the claimed inequality between the unnormalized counts.
After normalization the only loss is the fixed auxiliary size.
This also covers \(t=0\) and singular matrices, without estimating \(\|Q^{-1}\|\).

The highest homogeneous part of \((P-z)^*(P-z)\) is nonzero when \(P\) is nonconstant.
The scalar SS15 input and its algebraic behavior therefore give a finite free scalar logarithm.
At the bounded free tuple, the direct block factorization in C186v3 has bounded triangular factors with determinant one and the correct normalized direct-sum weight.
It supplies the finite free pencil logarithm required by the affine count, independently of any finite-dimensional least-value estimate.
Finally \(x=t^2\) converts the singular-value exponent and cutoff to \(\beta_z/2\) and \(n^{-2\gamma_z}\), as stated.

### Source acceptance and limits

The source statements of [Schultz, arXiv:math/0308192v1](https://arxiv.org/pdf/math/0308192v1), Theorem 3.2, equation (3.6), PDF p. 15, and its Gaussian normalization were checked against the retained Sch05 unit.
The exact [SS15 arXiv:1305.1920v1](https://arxiv.org/pdf/1305.1920v1) Theorem 1.1(5)(6), PDF pp. 1--2, and Corollary 1.2, PDF p. 3, were checked for matrix-valued algebraicity and the scalar atomlessness use.
Those established theorems are accepted at these matched interfaces; their complete source proofs were not independently re-audited.
Bounded determinant multiplicativity and its finite-tracial convention were reused at the exact retained FK52/MS24 scope, while the word-chain factorization and its application were checked directly.

The cited [Chatterjee arXiv:math/0508519v3](https://arxiv.org/pdf/math/0508519v3) Theorem 1.1 and Gaussian interpolation/integration-by-parts passage were checked as attribution for the replacement methods.
The candidate supplies its own matrix-coefficient argument and does not invoke that paper as a theorem already stating this result.
This review makes no novelty or whole-source-proof claim.

The conclusion is an expected shrinking count for each within-size law, so arbitrary cross-size coupling introduces no extra obligation.
It gives no least-singular-value floor, no unregularized logarithmic convergence, and no completion of the full finite-second-moment F0012 contract.
The original-law floor needed by the conditional direct-Hermitization route remains outside this finding.
No formal proof-assistant verification or numerical experiment is asserted.
