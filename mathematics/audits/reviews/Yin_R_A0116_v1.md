---
author: Yin
---

# Review of conjugation estimates and finite row fits for kernel dimension

At 2026-11-17T04:35 UTC an agent outside the development of Yin_C_A0080_v1 independently checked the fixed statement and all five proof sections for Sheng Yin.
The reviewer had previously reviewed the rational-inverse decay input C58 and the signed shell estimate C76, including the distinction between a time horizon and a computational complexity bound.
No C80 development account, author explanation, draft proof or prior finding was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0080_v1.md#statement) | Single-group hypotheses, off-identity conjugation contraction, weighted widened shells, excess dimension, finite fits and the scalar annihilator threshold. |
| [Whole-argument finding](#whole-argument-finding) | [Conjugation on the orbits](../../claims/Yin_C_A0080_v1.md#conjugation-on-the-nonidentity-coefficients) | Amenable stabilizers, the comparison of the quasi-regular norm with the tree norm, and bounded word-length displacement. |
| [Whole-argument finding](#whole-argument-finding) | [Signed shell bounds](../../claims/Yin_C_A0080_v1.md#signed-estimates-on-widened-shells) | Restricted telescoping, averaging of noncommuting product differences, phase polarization, two finite truncations and strict error exponents. |
| [Whole-argument finding](#whole-argument-finding) | [Finite row fits](../../claims/Yin_C_A0080_v1.md#a-finite-upper-bound-from-row-fits) | Quadratic trace inequality, reconstruction in the zero-excess case, fit infimum, finite-support obstruction and adjoint criterion. |
| [Whole-argument finding](#whole-argument-finding) | [Operator-norm obstruction](../../claims/Yin_C_A0080_v1.md#why-operator-norm-fits-fail-at-nonclosed-range) | Large finite \(n\) from the rapid-decay ball estimate, approximate null vectors and loss of uniform boundedness of fitting multipliers with trace-\(L^2\) errors tending to zero. |
| [Whole-argument finding](#whole-argument-finding) | [Concrete nonclosed row](../../claims/Yin_C_A0080_v1.md#finite-fits-for-a-full-group-input-of-nonclosed-range) | Input support under translations, explicit fit errors, infinite kernel-projection support, and positive spectral exponent. |
| [Whole-argument finding](#whole-argument-finding) | [Tree estimate and example](../../claims/Yin_C_A0064_v1.md#the-row-map-and-its-kernel) | Absolute adjacency form bound on the four-regular tree and the example with no finite null vector. |
| [Whole-argument finding](#whole-argument-finding) | [C76, signed return truncation](../../claims/Yin_C_A0076_v1.md#the-joint-square-bound-across-time-and-endpoints) | Finite time tail of the cumulative signed differences. |
| [Whole-argument finding](#whole-argument-finding) | [Shell estimate](../../claims/Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell) | Weighted error to the signed limit under the dyadic trace hypothesis. |
| [Whole-argument finding](#whole-argument-finding) | [Spatial criterion and ball estimate](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Additional rapid-decay and trace inputs on the four-line group. |
| [Whole-argument finding](#whole-argument-finding) | [Finite inverse approximation](../../claims/Yin_C_A0058_v1.md#bounded-rational-inverses-have-exponential-tails) | Exponential localization of the reconstructed projection. |
| [Whole-argument finding](#whole-argument-finding) | [Cyclic spectral comparison](../../claims/Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group) | Traced positive sublevels of the infinite shift under positive operator inequalities. |

## Whole-argument finding

The source comparison covers hyperbolic boundary-pair stabilizers and virtual cyclicity. [Boutonnet–Carderi, Lemma 2.2(i) and proof](../../literature/pdf/BC15--arxiv-v2.pdf#page=6)

Conjugation identifies the free-pair orbit of \(g\ne e\) with the left coset space of its stabilizer in \(F\).
For the hyperbolic group this stabilizer lies in the stabilizer of the two boundary fixed points of \(g\).
The cited primary lemma identifies the latter group with an infinite maximal amenable subgroup containing \(g\), and its proof gives virtual cyclicity.
For an arbitrary group in the extension only amenability of the stabilizers is used.
A finitely supported vector on the cosets, lifted to normalized indicators of a common Følner set at its chosen representatives, has the same norm.
The finitely many transitions by the four letters involve left translates within the stabilizer, so their matrix coefficients converge to the desired coset coefficients.
The regular tree form bound controls the absolute real quadratic form, implying the norm bound \(2\sqrt3/4\) on every orbit, including finite or trivial stabilizers.
An infinite-index restriction is unnecessary, and the fixed identity orbit is discarded before applying the contraction.

For \(l<k_j\), a term of \(\mathsf P^l\) observed on \(S_j\) uses only the enlarged \(S_j^+\) in the source.
The contraction \(\rho^l\) applies to each such restricted input and the remaining unrestricted term costs \(\rho^{k_j}\sqrt m\).
The insertion identity for \(Q^l-Q_h^l\) keeps its factors ordered and vanishes for \(l=0\).
Real Abel polarization and the two stationary probe denominators give a norm cost at most four.
Truncation of the ordinary normalized powers costs \(\sqrt m\,z_j^{N_j+1}\); truncation of the signed return prefixes additionally costs a factor \((1-z_j^2)^{-1/2}\) with the C76 constant.
After multiplication by the square-root shell weight the orbital error has exponent \(a\log_2(1/\rho)-\beta/2>0\), and the C76 time and Abel errors admit exponent \((\kappa\alpha-\beta)/2>0\).
These are norm bounds with the unnormalized matrix trace, with no shell-size multiplier.
Finiteness of the measured sum is still an input for obtaining the projection estimate, and the trace-integrality corollary uses the stronger four-line geometry when \(\beta>3\).

The identity coefficient of \(T\) is the sum of the Gram matrices of the coefficients of \(C_0\); it has exactly the indicated constant kernel.
Since \(S\) is invertible its restriction identifies the two original Hilbert-module kernels up to dimension.
Consequently \(q-e_W\) is a projection of trace \(z^2\), and the trace-pairing error with \(D_n-T_0\) is at most \(\delta_n z\).
Every fitted residual restricted to \(q\) equals \(C_0 hq\).
The \(e_W\) part vanishes for every \(h\), and the remaining average squared trace-\(L^2\) norm is exactly \(\tau_m((q-e_W)D_n)\).
This gives \(\lambda z^2\le E^2+\delta_n z\) with the stated positive root and no injectivity or closed-range assumption on \(C_0\).
For a scalar finite-support \(b\), \(\|b\|_2^2\le\|b\|^2\dim\overline{\operatorname{ran}b}\) and \(\|b\|\le\sqrt{s}\|b\|_2\) for at most \(s\) terms.
This verifies the strict \(s^{-1/2}\) comparison.

For fixed \(h\), regularizing \(T\) on its positive part gives the claimed optimal residual in trace \(L^2\); the ambient reduced group algebra supplies finite operator-norm approximants at each fixed positive regularization.
Finite-support least-squares problems need only the ordinary finite Gram data of actual products.
If a sequence of fits gives vanishing error then \(q=e_W\), and conversely this equality permits arbitrarily accurate fits for every finite family of averaging words.
The range of \(SV\) in this case is the full kernel of \(A\), and \(V^*S^*SV\) has a positive lower bound on its domain.
The Neumann approximation therefore gives exponential decay of the reconstructed projection, with the zero constant subspace handled separately.
At nonzero excess the same range is only a subspace of the kernel with complementary trace \(z^2\).
A single fit bounds the unweighted exterior by that error plus the tail of the known subprojection, without supplying a summable spatial weight by itself.
For the adjoint the polar dimension identity gives the stated recovery of the trace on verification of a vanishing excess; it supplies no such spatial reconstruction for the original matrix.

On the rapid-decay group \(\mathsf P^n T-T_0\) still has propagation \(O(n)\), so the ball estimate converts the trace contraction into operator norm tending to zero.
Once the result is below \(\lambda/2\), \(D_n\) dominates \((\lambda/2)(I-e_W)\) because both operators annihilate \(e_W\).
At a fixed such \(n\), vectors approaching the nullspace spectrally on its orthogonal complement give the claimed lower bound for the averaged squared operator-norm residual of every bounded family.
If trace-\(L^2\) residuals vanished for uniformly bounded fitting families, a simultaneous weak cluster point for the finitely many words would solve the equations exactly, contradicting that lower bound.
The operator-norm obstruction is compatible with arbitrarily accurate fits in trace \(L^2\).

In the example, a left and right translate of \(a\) supported in a subgroup can be normalized using its identity coefficient, obtaining the conjugate of \(a\) in that subgroup.
Its \(u\)-coefficient then puts the conjugate of \(u\) in the subgroup, and cancellation of the injective cyclic difference in the affiliated algebra recovers the conjugate of \(8I+P\).
Thus the input requires the whole group under the permitted shifts.
The finite triangular change gives \(C_0=(a,0)\).
The defect of \(L_N(1-u)\) has trace-\(L^2\) norm \(N^{-1/2}\) by orthogonality of the \(N\) distinct group elements, and the other defect is bounded by \(2N8^{-k}\) without commuting \(P\) and \(u\).
This yields the displayed vanishing fits uniformly in \(h\), the recovered column \((-V,I)^t\), and the positive coefficients of \((3-v-v^{-1})^{-1}\) on every \(v^j\).
The comparison with the cyclic shift gives positive spectral exponent \(1/2\), sufficient for the C76 dyadic assumption.
The example verifies the criteria for its explicit matrix; the general inequalities do not give small fits or summable signed insertions for every nonclosed-range input.
The whole fixed claim passes at the stated scopes.
