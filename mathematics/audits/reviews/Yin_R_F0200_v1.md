---
author: Yin
---

# Independent review of the symmetrized-adjugate and isolated-minor assertions

The review act was completed at 2026-11-05T08:18 UTC for the registered human Yin.
This was a separately arranged initial independent whole-argument inspection of [C_F0194_v1](../../claims/Yin_C_F0194_v1.md#statement).
The reviewer was outside substantive development and received only the fixed statement and argument, necessary dependency locators, operational facts, applicable rules and assigned scope.
No development draft, proof-generation dialogue, author explanation, mathematical development summary or previous review conclusion was supplied or consulted.
Initial findings were formed before this record, and no substantive repair was supplied.

The reviewer read the complete fixed C_F0194_v1 argument and checked all its deterministic consequences and restricted probability assertions.
The exact linear source theorem was read directly in [arXiv:1105.5733v1, PDF pp. 2--3](https://arxiv.org/pdf/1105.5733v1), together with the progression and linear-concentration definitions on PDF pp. 1--3.
Its original proof is accepted externally and was not re-audited.
The repaired counting mechanism and deterministic-diagonal interface in C_F0188_v2 were inspected directly.
Its selected symmetric-shift theorem was reused only for the optional symmetric-part consequence.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole restricted argument](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole restricted argument](#finding) | [Exact assertions](../../claims/Yin_C_F0194_v1.md#statement) | Complete deterministic identity and inequality, exact isolated-principal-minor probability theorem, independent random-shift extension and summable arbitrary-coupling consequence. |
| [Whole restricted argument](#finding) | [Complete argument](../../claims/Yin_C_F0194_v1.md#argument) | Entire fixed argument, including the failed-inference example, optional symmetric-part consequence, truncation, rank-one reduction, full profile count, linear rounding and final assembly. |
| [Whole restricted argument](#finding) | [Declared linear-source input](../literature/Ngu12a/Yin_U001.md#ngu12a-u001) | The unit's selected arXiv v1 edition and progression and concentration conventions; the consuming linear input was checked directly against Condition 1 and Theorem 1.3 on PDF pp. 2--3, with the original source proof accepted externally. |
| [Whole restricted argument](#finding) | [Progression conventions](../literature/Ngu12a/Yin_U001.md#progression-conventions) | Complete definitions of size, properness, symmetry, displayed integer box and Euclidean closeness, including the source/local nonproper-box distinction. |
| [Whole restricted argument](#finding) | [Concentration conventions](../literature/Ngu12a/Yin_U001.md#concentration-conventions) | Linear concentration for real iid scalar variables and dimension-two coefficients; the quadratic convention was read but is not an input to the isolated-minor proof. |
| [Whole restricted argument](#finding) | [Repaired mechanism](../../claims/Yin_C_F0188_v2.md#argument) | Rational-grid formulation, complete repaired profile count and deterministic-diagonal adjustment at their reuse in C_F0194_v1; no general nonsymmetric-shift theorem is inferred. |
| [Whole restricted argument](#finding) | [Symmetric-shift theorem](../../claims/Yin_C_F0188_v2.md#statement) | Exact finite-second-moment, diagonal, normalized and independent symmetric-shift scope used only for the optional symmetric-part cofactor consequence. |
| [Whole restricted argument](#finding) | [Selected symmetric-shift assessment](../../claims/Yin_C_F0188_v2.md#decision-complex-shift-reviewed) | Reuse of the accepted theorem for W plus sym F; no new review of the original quadratic inverse theorem is claimed. |

<a id="finding"></a>
## Outcome

No unresolved mathematical gap was found in the exact C_F0194_v1 assertions or their complete restricted supporting argument, under the explicitly accepted linear inverse theorem and the accepted symmetric-shift input for the optional consequence.
The conclusion is the displayed isolated-minor determinant bound and its stated extensions.
It supplies no arbitrary-nonsymmetric-shift least-singular-value estimate, missing-minor reduction or completion of F0012.

### Deterministic assertions and the failed inference

Expanding the two sides of \(D^TQ=SA\) uses \(D^TA^T=(AD)^T=(\det D)I\) and \(DA=(\det D)I\), so the identity includes singular \(D\).
The Frobenius bound uses \(s_{\min}(S)\) and \(\|D^T\|=\|D\|\), also for complex matrices.
The undivided inequality covers \(D=0\), while division is restricted to \(D\ne0\).
The displayed two-by-two matrices have the claimed adjugate and symmetric part, and both coordinate rows of \(Q\) have residual norm \(\sqrt2\) under each of \(D\) and \(D^T\).
The example therefore disproves the stated row-to-kernel inference, while leaving the broader random-matrix target untouched.

For \(D=W+F\), the identity \(\operatorname{sym}D=W+\operatorname{sym}F\) gives the genuinely symmetric shift required by C_F0188_v2 after conditioning on independent \(F\).
Symmetrization preserves the entry bound, second moments give the polynomial norm event for \(D\), and the accepted theorem supplies the least-singular-value floor for \(\operatorname{sym}D\).
A union over principal minors only changes the selected polynomial failure exponent.
For a random shift this consequence retains the polynomial-bound event and its complement as in the statement.
It does not convert a row of the symmetrized adjugate into an adjugate row.

### Isolated-minor algebra and exponents

The block determinant identity remains valid for distinct deterministic shifts \(f,g\) and singular \(D\).
A rank-one term \(\alpha uv^T\) gives exactly the product of the two displayed bilinear linear forms.
The two remainder terms cost at most \(n^K|\det D|/\|A\|_F\) and \(n^{2K}\|E\|\).
The stated product-union inclusion follows with its constants and radius and requires no independence between the two forms.

For an invertible complex \(D\), the leading singular term of its adjugate uses a right singular vector \(u\) and the conjugate of a left singular vector as \(v\).
Thus \(\|Du\|=\|D^Tv\|=t_1\), as required for the two counting branches.
The determinant-to-adjugate ratio is at most \(t_1\), and the discarded normalized adjugate has Frobenius norm at most \(\sqrt n\,t_1/t_2\).
For a minor of dimension \(n-1\), the statement's rank \(n-2\) branch is precisely corank one and has exact rank-one adjugate with zero residuals.
The local rank descriptions in the algebraic discussion are read relative to the dimension of \(D\).

There is harmless reuse of the letter \(L\) between the auxiliary isolated-input display and the final event.
Literally the final ratio hypothesis gives adjugate error at most \(n^{1/2-L}\), rather than \(n^{-L}\) with that same letter.
The final choice \(L\ge2a_0+2K+3\) nevertheless gives the determinant remainder bound
\[
 n^{K-L}+n^{2K+1/2-L}\le2n^{-2a_0-5/2},
\]
which is strictly sufficient for the product-union step.
This is exponent bookkeeping, not an unproved estimate or a substantive repair.
The additional relative-gap observation follows directly from \(t_2\le n^K\) at its stated bounded-norm scope.

### Linear source and rational candidates

The inspected source theorem allows every positive radius, unit total coefficient norm in \(\mathbb R^d\), polynomially large concentration and an exception count between the prescribed power of the coefficient count and that count.
It supplies a proper symmetric progression of bounded rank, size at most \(\max\{C\rho^{-1}/\sqrt{n'},1\}\), and generators \(\beta p_{ij}/p\) with the stated polynomial integer controls.
Constants depend on the fixed exponents, dimension and anti-concentration constants.
Dimension two gives exactly complex coefficients with real scalar randomness.
Neither centering of a truncated law nor independent coefficient components is required.

These hypotheses match the unit singular vectors, normalized degenerate subsets and normalized profile tails.
For tail norm \(\sigma\), using radius \(t/\sigma\) and rescaling back cancels \(\sigma\) from the displayed generator step.
The bound \(\sigma\le2\) controls the remaining integer numerators polynomially even when \(\sigma\) is small.
The existential fine precision \(a_0\) may be chosen integral, so the radii and generators have the asserted rational heights.
Properness supplies polynomially bounded displayed boxes; exceptional-coordinate rounding and enlargement of the structural constant give the exact deterministic candidate class.
Its leading \(n\log n\) entropy coefficient is independent of \(a_0\).

### Complete profile count and nonsymmetric offsets

Conditioning on the bulk-complement entries and diagonal, then exposing increasing bulk rows, leaves independent strictly upper random entries in the current row.
Every other matrix contribution is a center in a complex linear concentration event.
This uses symmetry of the random family and no equality between the two deterministic off-diagonal shifts.
Omitting the bounded exceptional rows and the first tail factor costs only the polynomial factor in (26).
The tail lower bounds follow from bounded support, and the large last coordinate with anti-concentration gives the uniform direct exponential bound.
The identical reasoning applies to the transpose.

In the degenerate case, normalizing each \(q\)-subset preserves approximation radius \(t_*\) after rescaling back.
The progression-size bound is eventually one, so the proper symmetric progression is \(\{0\}\).
The claimed sparsity follows, and rounding gives only \(\exp(o(n))\) vectors with preserved large coordinate and the asserted enlarged row tolerance.
Their union retains the direct exponential estimate.

For the nondegenerate case, the reservoir costs \(\exp(o(n))\) choices and supplies (27) for every retained tail.
The proof correctly performs a fresh low-product classification after its permutation; no earlier product lower bound is transferred through that permutation.
The coarse entropy with (26) handles the new low-product class, and the remaining class gives the actual lower bound needed for the multiscale pigeonhole step.
Fine precision is chosen after structural and coarse-entropy constants to keep all relevant scales below \(t_*\).

At each profile block, \(n'\) lies in the source theorem's permitted range for the entire tail.
The reservoir upper bound makes the maximum with one harmless in the progression-size estimate.
Generators, boxes, exceptional positions and values contribute only polynomial factors, fixed constants to the power \(n\), and \(\exp(o(n))\), with no extra leading \(n\log n\) cost.
Selecting one original profile witness for each rounded vector is legitimate because it occurs in the deterministic candidate set before any row event.
Bounded raw entries control every rounded tail's comparison to that witness at the next scale.
Multiplying (30) and (31) cancels the concentration products, and \(\varepsilon=1/100\) leaves strictly more slack than the asserted \(n^{-n/3}\) bound.
The complete count is uniform in every allowed deterministic nonsymmetric shift and deterministic diagonal.

### Truncation, conditioning and assembly

Finite second moments give a raw cutoff with the required union-bound error for both entry families.
Conditioning on coordinatewise cutoffs preserves the iid strict upper family, its independence from the diagonals, and uniform anti-concentration for large \(n\).
Conditioning on actual diagonal values is legitimate because the count is uniform within their entry cutoff.
For a fixed principal minor, the remaining row coordinates are still independent of that minor with exactly the truncated law.
The bounded exposed diagonal enters only the determinant remainder.

The low-linear-concentration branch costs at most \(2n^{-b}\), while either high-concentration branch gives a structured candidate for \(D\) or \(D^T\).
Their existence probabilities were bounded without conditioning on a randomly selected kernel vector.
The union over at most \(n\) minors and restoration of the cutoff error prove the exact arbitrary polynomial failure bound with \(b>B+3\).
Conditioning on an independent random shift and integrating retains uniformity on its polynomial-bound event and adds its complement.
First Borel--Cantelli gives finite occurrence for \(B>1\) and summable extra failures under arbitrary cross-size coupling, without cross-size independence.

### Limits

This is a mathematical review of the complete fixed restricted argument, not formal verification or a re-audit of the original inverse-theorem proof.
The symmetric-shift theorem remains an accepted input at its exact selected scope.
The restricted event retains both its nonzero-adjugate condition and explicit isolated-minor alternatives.
Well-conditioned minors, clustered bottom singular values, higher-corank minors with zero adjugate, and the reduction from a general small full-matrix singular value to this restricted event remain outside the theorem and positive finding.
