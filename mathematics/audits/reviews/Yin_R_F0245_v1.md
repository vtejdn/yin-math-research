---
author: Yin
---

# Independent review of coordinate dual domains on closed curves and mixed arc covers

## Whole-proof finding

At 2026-11-13T17:48 UTC a separately assigned agent completed independent review of the [statement](../../claims/Yin_C_F0236_v1.md#statement) and [argument](../../claims/Yin_C_F0236_v1.md#argument) of the [17:46 candidate](../../claims/Yin_C_F0236_v1.md#decision-candidate).
The reviewer had worked on other normal-coordinate questions, including omitted shifts, and on holomorphic changes of a nonnormal circular coordinate.
The reviewer did not develop the closed-curve proof, receive its development reasoning, or consult its development draft or prior findings.
All twelve declared direct inputs were checked at their uses, together with the full-core and sign conventions.
The argument establishes the single-coordinate assertion without assumptions on the other marginal carriers and the entire comparison when all carriers admit the stated parametrizations.

### Laurent secants and the original adjoint domain

For \(n=-m<0\), multiplication of the difference for \(z^m-w^m\) by \(-z^{-m}w^{-m}\) gives exactly the negative Laurent expansion with terms \(z^{-1-a}w^{a-m}\), \(0\le a<m\).
The total absolute exponent in each term is \(m+1\), including the single term for \(m=1\).
For \(n>0\) it is \(n-1\); the zero mode contributes nothing.
The first-moment weight of the coefficients of \(J\) is therefore bounded by \(\sum_{n\ne0}|c_n|\,|n|(|n|+2)\), finite by (1).
Regularity gives the nonzero angular tangent divided by \(iz\) on the diagonal.
Distinct points have distinct images and the series is continuous on the compact two-torus, giving a positive minimum for \(|J|\) before any restriction to the actual spectrum.
The unweighted torus Wiener conclusion supplies \(K=J^{-1}\) with absolutely summable coefficients; its coefficients need no first-moment bound.
For periodic \(C^3\) parametrizations Parseval gives \(\sum |n|^6|c_n|^2<\infty\) and Cauchy–Schwarz with \(\sum_{n\ne0}|n|^{-2}<\infty\) proves (1).

The inverse to a local real projection of the parametrization gives an angle on a neighborhood of each parameter point; exponentiating removes the angle's choice of branch.
Compact injectivity lets each chart miss the complementary parameter patch.
A smooth partition extends the complex inverse to a plane rectangle without requiring a global choice of angle or a circle-valued extension there.
Uniform real \(C^1\) polynomial approximation controls differences divided by the complex chord by integrating the real derivative error along the segment in the rectangle.
The marginal law is diffuse under actual ACSY, so the diagonal presents no additional derivative condition for this approximation.
For negative powers extending the conjugate positive power avoids any zero of the extension off the carrier.
The actual coarse derivative bounds on both \(U^j\) and \(U^{-j}\) follow from the unit-circle chord bound and the supremum norm of \(K\).

Operator-norm convergence and coarse convergence of all generator approximants allow the full represented product rule at each fixed word, including words mixing different replacements.
The inner \(I_J\) commutes with the outer Leibniz actions; on the marginal tensor \(I_JK=1\), and the inverse rule gives the algebraic value \(-U^*\otimes U^*\) on \(U^*\).
An omitted replacement and its adjoint have zero derivative by omitted-polynomial approximation.
Expanding the old vacuum pairing of \(U^{-j}pU^{-k}\) with graph approximants bounds the actual elementary-tensor adjoint norm by \(\|\xi\|_2+(|j|+|k|)\|K\|_\infty\).
The adjoint of the inner multiplier at the unit tensor uses conjugated coefficients and opposite powers, with this same bound.
Its series is absolutely convergent in the graph of the old adjoint, proving the new actual vacuum on the entire new core.
This explains the different Fourier weights needed for \(J\) and \(K\).

### Mixed cores, signs and the two original canonical domains

The distinguished unitary-coordinate calculation has algebraic range on the mixed core because only \(U,U^*\) have nonzero prescribed values.
After the inner twist all other generators and their adjoints still have zero values; the computation with omitted normal generators therefore applies without supposing that the entire tuple is unitary.
The same graph construction for a distinguished arc coordinate uses its selfadjoint parameter and the established arc multiplier, with the loop coordinates treated as omitted approximable functions.
Each new parameter generates the original marginal von Neumann algebra by the two inverse functional calculi.

The bounded restrictions of the closed parameter slice and of its adjoint hold on all bounded vectors.
The bounded-ball graph extension in the arc argument applies to the mixed parameter core.
For the distinguished Laurent sums, the operator-first commutator of the inverse power follows from \([E,U^{-1}]=-U^{-1}[E,U]U^{-1}\) on bounded inputs.
Thus the kernel of the commutator for \(r(U)\) is \(J\) with the same exponents as above.
Uniform convergence of the secants gives Hilbert–Schmidt convergence of their rank-one operator representation, while norm convergence of the multipliers suffices for the bounded \(M\)-to-\(L^2\) restrictions.
The absolutely summable right multipliers in \(Q_K\) correct \(J\) to the unit tensor and preserve the zero omitted commutators.
Reversing their order, taking adjoints and conjugating coefficients gives an actual adjoint tested against every bounded vector.
Negation converts the resulting operator-first commutator to the task's generator-first convention.
These facts yield a strong original witness whenever the parameter tuple has actual ACSY.

To recover the original canonical slice at a single coordinate, the two-Haar enlargement preserves its carrier and the old vacuum, and its finite witness cost bounds the original full column cost via \(c_i\le4\beta_i\).
Repeating on the adjoint tuple uses the conjugated carrier and C_F0076's companion.
Explicitly its right slice at \(a^*\) equals the involution of the original left slice at \(a\).
The column bound implies the bounded right cut individually in either application.
Thus C_F0072 Part B has both of its required original cut bounds and yields all bounded vectors in both the domain of the original closure and that of its actual adjoint.
Merely exhibiting the corrected witness would not by itself identify these canonical domains.

For the reverse joint comparison the bare normal theorem supplies operator-norm-to-Hilbert continuity and starred commutator kernels on the represented core, without any vacuum premise.
The same plane approximants transport the commutators to \(K_i\), including vanishing at omitted coordinates.
The correction now uses \(J_i\), followed by the sign for a bare parameter witness.
C_F0071 Part D applies to a tuple whose individual coordinates are selfadjoint or unitary, including mixtures.
Together with the strong-to-bare restriction and C_F0070 Part C this closes the stated equivalence chain.
The single-coordinate conclusion requires none of these reverse comparisons for the other coordinates.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0236_v1.md#statement) | Single distinguished loop, original canonical column and both domains, all mixed loop/arc actual, bare and strong comparisons. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0236_v1.md#argument) | Both Laurent signs, projective invertibility, graph and actual adjoint, parameter domains, correction, two-Haar enlargement and mixed bare converse. |
| [Whole-proof finding](#whole-proof-finding) | [Torus Wiener lemma](../literature/Den09/Yin_U002.md#den09-u002) | Example 20 on \(\mathbb T^2\) for a zero-free absolutely convergent Fourier series. |
| [Whole-proof finding](#whole-proof-finding) | [Weighted Fourier estimate](../../claims/Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Parseval and summability for a periodic \(C^3\) parametrization. |
| [Whole-proof finding](#whole-proof-finding) | [Arc coordinates](../../claims/Yin_C_F0234_v1.md#statement) | Inverse charts, graph and adjoint approximation, omitted replacements and restoration on the arc and mixed cores. |
| [Whole-proof finding](#whole-proof-finding) | [Normal marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, diffuseness, divided difference, closability and adjoint companion. |
| [Whole-proof finding](#whole-proof-finding) | [Actual tensor adjoint](../../claims/Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Graph approximants of powers and their adjoints, weighted elementary tensor estimates and closure of the adjoint. |
| [Whole-proof finding](#whole-proof-finding) | [Unitary core bounds](../../claims/Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Unitary core Leibniz values and both actual canonical domain bounds. |
| [Whole-proof finding](#whole-proof-finding) | [Omitted normal coordinates](../../claims/Yin_C_F0158_v2.md#the-unitary-coordinate-and-its-real-twist) | Unitary calculation on a mixed core with zero values at both orientations of all omitted generators. |
| [Whole-proof finding](#whole-proof-finding) | [Projective correction](../../claims/Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Right multiplier series, Hilbert–Schmidt commutator multiplication and reversed actual adjoint. |
| [Whole-proof finding](#whole-proof-finding) | [Column criterion](../../claims/Yin_C_F0208_v1.md#statement) | Preservation on two-Haar enlargement and \(c_i(X)\le4\beta_i\) for the old generator. |
| [Whole-proof finding](#whole-proof-finding) | [Original canonical domains](../../claims/Yin_C_F0072_v1.md#statement) | Part B applied to both original bounded cuts after the adjoint-tuple step. |
| [Whole-proof finding](#whole-proof-finding) | [Bare normal commutators](../../claims/Yin_C_F0070_v1.md#statement) | Parts A and C, automatic bounded normalized maps, forced starred kernels and vacuum from the strong premise. |
| [Whole-proof finding](#whole-proof-finding) | [Mixed comparison](../../claims/Yin_C_F0071_v2.md#statement) | Part D for the selfadjoint and unitary parameter tuple, in both directions. |
| [Whole-proof finding](#whole-proof-finding) | [Task conventions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Generator-first commutator, full represented starred core and actual strong domains. |
