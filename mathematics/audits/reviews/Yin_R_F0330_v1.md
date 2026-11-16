---
author: Yin
---

# Review of a single deficient pair with independent marginal traces near free semicirculars

## Finding

At 2026-11-16T17:37 UTC a separately assigned agent for Yin independently reviewed the complete C_F0322 v1 candidate fixed at 17:36 UTC.
The reviewer took no part in developing this candidate and received the fixed mathematical inputs without development dialogue, author explanations, exploration notes or prior findings on it.
The qualitative equivalence and the simultaneous realization of (1) and (2) hold.

The grading fixes each tag and acts trivially on the first diagonal corner \(e_1M_8(R')e_1\), while reversing \(s_*\).
The conditional mean of \(s\) is \(b s_*\), with \(b>0\) from the strict trace inequality for the gapped noise.
In the four-step path expand each \(s\) into this mean and its centered remainder over \(B_*\).
One remainder gives zero after taking the base expectation.
With several remainders, if each intervening base run is centered over \(B_*\), their alternating product has zero base expectation by the reduced-word calculation, including arbitrary outer base factors.
Replacing any run between two remainders by its mean removes at least one of the distinct tags and merges the neighboring noise factors.
Repeating leaves only an ordered subsequence of at most two tags, separated by elements of \(\operatorname{span}\{1,s_*\}\).
With two retained tags, orthogonality forces all three separating factors, including those adjacent to the end cuts, to supply \(s_*\).
Their odd word projects to zero in the \(e_1\)-corner by the grading.
Each remaining one-tag contraction has scalar first-slot mean \(1/8\), using \(U\) across halves and \(\mathbb E_A(De_2D)=1/4\) within the upper half.
Zero tags also have scalar compression in expectation.
The uncontracted four entries multiply to \(J/64\).
Consequently (3) has coefficient exactly \(b^4\) on \(J\), and taking the real part leaves a real scalar remainder.

Entrywise expectation onto \(M_4(B)\) sends \(I_4p\) to \(t1\).
Every centered reduced word containing \(D\) is orthogonal to \(A\), so enlarging \(M_4(B)\) to \(C_1\) preserves this conditional expectation.
The amplification gives the same equality for \(P\) over \(C_2\).
For a general \(C\subset\mathcal R\), the leading \(L^2(C)\)-factor projection in the free-product decomposition still satisfies \(QPQ=tQ\).
A centered word from \(C\vee V\) sends the orthogonal complement into its range because \(C\) preserves \(L^2(\mathcal R)\ominus L^2(C)\) under multiplication.
Hence the two-term compression bound applies at both stages.
At the first stage \(\|H-\mathbb E_{C_2}H\|\le128\), and at the second the corresponding centered entry also has norm at most 128.
The two compressions cost at most \(256\sqrt t\) each and the tower of expectations leaves exactly (3).
For \(p=1_n\) this starts with trace \(t_n\) in the primary base, while the final first-slot projection has trace \(u_n=t_n/8\).

The direct-product diagonal derivatives are summable on the generators and have the indicated trace-weighted vacua.
Each normalized matrix lift multiplies the vacuum entry by its trace weight, and the intervening extension across \(D\) preserves it.
The total bad diagonal squared norm is \(\sum_n4^{-n}/L^2\).
The kernels between distinct good slots cost at most \(1/\delta\) in coarse norm.
For a bad block \(n\), the gap to the good spectrum and to later bad blocks is at least a constant times \(d2^{-n}\).
Summing the product weights therefore gives the stated \(d^{-2}\sum_n4^nt_n\) bound for the remaining squared kernel norm.
The mixed inner derivation completes the unit and marginal phase values and gives \(\|Ls_*\|_2\le2\|K\|_2\).
The free tensor insertion at \(v\) cancels the derivative of \(v+\lambda s_*\) and adds at most \(2\lambda\|g_v\|_2\|K\|_2\) to the vacuum norm.
The gap then allows adjoining the sign to the wordwise graph.
The restricted values are intrinsic and the projected vacuum is actual.

On the full good spectral square, the sum of the diagonal derivative and the good-to-good kernel gives the divided difference of every scalar polynomial.
Its vacuum vector is a marginal function supported on the good pieces by the explicit two contractions of the inner kernel.
In particular uniqueness follows by polynomial density on the good marginal alone, without differentiating the good support projection.
The vector equals \(c\xi_\nu\), because the restricted double trace has factor \(c^2\) whereas its single-leg Hilbert pairing has factor \(c\).
Since \(\nu\) has density \(w_g/c\), the square of its contribution to the unnormalized Hilbert norm is \((4\pi^2/3)\int w_g^3\).
Its cross term with the coordinate is \(-2c^2\), because the normalized vacuum pairing at the real generator equals one.
This proves (5).
Translation preserves the disjoint cubic contributions and the factor \(1-t\) on the top octile tends to one.
The second moment converges to one as \(\delta,t\to0\), and the reference cubic is normalized by the standard semicircular vacuum.
The remaining diagonal and kernel contributions in (6) can therefore be made small in the common trace Hilbert norm.

The individual bad pieces and the four tag projections used by \(H\) are isolated in real part.
Smooth cuts give norm and graph approximations, and their derivatives vanish after restricting both inner legs to \(E_n\).
The trace of that corner, after normalization, restricts correctly to \(R_n\), and the scaled generator sends \(Z_n\) to the unit tensor and \(Z_n^*\) to its unchanged phase.
The coefficient \(b^{-4}E_n(H-ae_1)E_n\) is intrinsic and within the chosen witness tolerance of \(J_n\) by (4).
The traced product rule costs \(u_n^{3/2}\) in the global norm, so a finite original cost would bound \(2^{n-1}/L\) by \(4a_0\) for every \(n\).
The even-algebra transfer gives the two actual vacua \(\xi,s\xi s\) and two infinite costs in the pair's own algebra.
A bare system would force finite original cost there.

For distinct halves the padding variable in the lower half is free from the upper entry and the \(J\)-coefficient in the corresponding entry of \(2U\).
Within a half the centered free symmetry, or its conjugate by \(U\), separates the two functions.
The resulting unsmoothed factorization applies to all bounded Borel functions and gives \(\mathbb E_{B_*} f(W)=\tau(f(W))1\).
The regression formula for \(s f(W)s\) then preserves exactly the same two-marginal product law.
The reference quantile variable is uniform on the entire conditional top interval in probability when the good mass \(1-t\) and the bad mass \(t\) are recombined.
The other seven slots have the original conditional semicircular variables after subtracting their translations.
Taking the supremum of the blockwise errors gives \(7\delta+d+\omega(t)\) in operator norm.
The centered sign of the free noise conjugates \(T_0\) to a free copy, and conjugation by the nearby sign \(s\) gives the claimed operator and vacuum estimates at the second coordinate as well.
Finally the preliminary mass upper bound controls \(\|K\|_2\) before \(\lambda\) is selected.
Once \(b>0\) is fixed, every finite witness restriction requires only an upper bound on its positive mass, so all can be imposed while \(\sum_n4^nt_n\) is made arbitrarily small.
This verifies the quantifiers with a single pair for each prescribed \(\varepsilon\).

The review checked all fifteen declared dependency interfaces at their uses.
The existence of a deficient normal pair remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0322_v1.md#decision-candidate) | Fixed 17:36 UTC decision with both simultaneous conditions and qualitative equivalence. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0322_v1.md#statement) | Exact product traces, model-dependent test, one hypothetical pair with two infinite costs and free reference coupling in both norms. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0322_v1.md#argument) | Full regression, nested compressions, countable construction, vacuum cancellation, trace law, coupling and parameter order. |
| [Finding](#finding) | [Matrix symmetry](../../claims/Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces) | Eight entries, grading, four-step coefficient and rectangular trace factorization for arbitrary free padding laws. |
| [Finding](#finding) | [Matrix lifts](../../claims/Yin_C_F0321_v1.md#making-the-sign-a-relative-coefficient) | Two trace-scaled matrix lifts and centered-word extension through the independent symmetry. |
| [Finding](#finding) | [Gapped sign](../../claims/Yin_C_F0317_v1.md#a-freely-perturbed-projection-close-in-norm-to-a-free-symmetry) | Positive scalar coefficient for each sufficiently small coupling and norm proximity to the independent sign. |
| [Finding](#finding) | [Norm compression](../../claims/Yin_C_F0313_v1.md#compression-of-a-free-perturbation) | Reduced-word projection proof under a general base subalgebra and the \(2\sqrt t\) factor. |
| [Finding](#finding) | [Projection witnesses](../../claims/Yin_C_F0308_v1.md#statement) | Unbounded normalized finite witnesses from failure of the universal implication using one trace-half projection. |
| [Finding](#finding) | [Continuity of witnesses](../../claims/Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Stability of the fixed contraction and its marked formal slice under a close replacement coefficient. |
| [Finding](#finding) | [Scalar actual vacua](../../claims/Yin_C_F0255_v1.md#statement) | Finite geometric energy for translated conditional semicircular densities on real intervals. |
| [Finding](#finding) | [Diagonal and mixed derivatives](../../claims/Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Countable diagonal summation, trace powers and mixed inner kernel correction. |
| [Finding](#finding) | [Free-noise correction](../../claims/Yin_C_F0317_v1.md#a-semicircular-main-summand-and-summable-distinguished-vacua) | Free extension, base tensor at the gapped noise, graph closure of the sign and vacuum projection. |
| [Finding](#finding) | [Directional Cauchy law](../../claims/Yin_C_F0318_v1.md#statement) | The scalar line vacuum norm with cubic-density coefficient \(4\pi^2/3\). |
| [Finding](#finding) | [Semicircular moments](../literature/NS06/Yin_U004.md#ns06-u004) | Variance one and identification of the coordinate with the scalar vacuum by the pairing recursion. |
| [Finding](#finding) | [Corner comparison](../../claims/Yin_C_F0313_v1.md#detecting-the-bad-polynomials-after-taking-the-sign) | Both inner-leg cuts in the normalized bad slot, graph approximation and twice the finite global cost. |
| [Finding](#finding) | [Even algebra](../../claims/Yin_C_F0311_v1.md#statement) | Actual exchanged coordinates, both actual vacua and transfer of infinite original costs. |
| [Finding](#finding) | [Bare-dual obstruction](../../claims/Yin_C_F0070_v1.md#statement) | Finite original cost from a bare normal full-domain dual system. |
| [Finding](#finding) | [Coupling and regression](../../claims/Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Quadratic conditional expectation for the smoothed sign, exact reference quantile and free conjugate semicircular pair. |
