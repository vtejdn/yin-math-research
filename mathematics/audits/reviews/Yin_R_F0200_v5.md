---
author: Yin
---

# Independent whole-proof review of nonsymmetric Wigner polynomial floors

<a id="finding"></a>
## Finding: the complete v5 candidate has no unresolved mathematical gap

The review act is dated 2026-11-05T11:14 UTC, with Yin as human record author.
A separately organized agent outside substantive proof development reviewed [C_F0194_v5](../../claims/Yin_C_F0194_v5.md#statement), its complete argument, its [candidate decision](../../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-candidate), and all eleven declared direct dependency interfaces.
The reviewer received fixed mathematical inputs, the review assignment, applicable rules and execution conditions, without proof-generation dialogue, exploration drafts, author explanations or prior conclusions about this proof.
No D material or previous R finding was consulted.
The statement's obligations were checked against the forward proof and the actual fixed dependency scopes.
This is an independent whole-proof mathematical review, not formal verification or a new audit of every accepted dependency's original proof.

No unresolved gap was found in the main uniform in-probability least-singular-value estimate or in the subsidiary uncovered-diagonal exclusion, hub and adjugate approximations, small-minor ratio and singular-value implications, omitted-row kernel anti-concentration, and raw and normalized second-smallest floors.
The conclusions apply to the exact fixed real finite-second-moment Wigner laws, polynomially bounded deterministic complex shifts without symmetry, and independent random shifts on their stated guards.
The review supports adoption at that scope; adoption remains the responsible Claim's decision.

### Internal-row exclusion and its deterministic consequences

The symmetric-part floor is used only for genuinely complex symmetric shifts of the same real Wigner randomness.
For internal dimension d=m-1 in [N/3,N], the bound N^(gamma+1/2)<=d^(gamma+2) holds eventually, and d^(-a_s)/sqrt(N)>=N^(-a_s-1/2).
The internal and outer union bounds can therefore be absorbed by selecting the accepted floor's probability exponent first.
No floor for a nonsymmetric B or D is inferred from this input.

The cofactor row identity is valid for arbitrary complex B by polynomial continuation, and the large uncovered diagonal supplies det(B) nonzero.
After division by this determinant, its random coefficient map is exactly U=sym(B^(-1))=B^(-T)sym(B)B^(-1).
The symmetric-part floor and ||B||<=N^K give s_min(U)>=N^(-L-2K), without an upper bound on B^(-1).
Ordinary transpose is used correctly, and transposition preserves singular values even over the complex field.

Deleting the k cover coordinates loses at most k singular directions: on ker(U_IT), extension by zero gives the claimed lower bound for U_TT.
Thus at least p-k>=p/2 directions remain when k<2r_N and r_N log(N)=o(N).
Conditioning on B and x_I leaves the coordinates x_T independent with their original real law.
The random adjugate norm is eliminated by the deterministic ratio |det(B)|>=N^(-J)||A||_F before the distance estimate is invoked.
The projected affine radius is at most N^(L+2K+1+J-H), and the fixed choice H>J+L+2K+1 makes it admissible.
The accepted distance estimate is uniform over complex affine subspaces and centers, so its conditional use is legitimate.
The norm and symmetric-part restrictions used at this step are B-measurable; the proof does not condition on the adaptive cover or a row-dependent good event.
The deterministic-cover count is exp(o(N)), preserving the exp(-cN) error.
These checks also cover arbitrarily slowly growing r_N and all m in [N/2,N].

The rank bound rank(Q_I)<=2|I| and the entrywise Frobenius estimate give the stated hub approximation.
The identities D^TQ=(sym D)A and DQD^T=(det D)sym D hold without invertibility.
Using the symmetric-part floor in the first identity proves the adjugate approximation with its displayed norm cost.
Using a rank-q approximation in the second identity gives |det D|/||A||_F<=N^(2K+L_0)e_N when q=2|I|<m.
For invertible D, ||D^(-1)||_F<=sqrt(m)/s_min(D) has the correct direction for the stated upper bound on s_min(D).
For singular D with A nonzero, the corank is exactly one and the same singular-value conclusion is immediate.
The choices of J and H after the fixed precision exponent absorb both diagonal and off-diagonal terms of e_N.
None of these consequences alone asserts an isolated smallest direction.

### Omitted-row counting and the second-smallest floor

The actual fixed counting class and profile proof of C_F0194_v1 permit any set of at least m-C_0 row constraints.
Equation (26) explicitly retains only a polynomial penalty for the omitted constraints; the later profile cancellation and subexponential exceptional-coordinate counts remain applicable.
The nonsymmetric deterministic offsets enter as centers, and deterministic diagonal conditioning is within the fixed module's scope.
The inverse theorem and rounding are applied to complex coefficients as real vectors of dimension two, with real scalar randomness.
Their structural constants are fixed before the fine exponent a.
For a vector annihilating all but the omitted row, rounding gives residual at most C m^(K+1-a) on precisely the retained rows, which fits the fixed tolerance after enlarging C_0 independently of a.
The finite candidate-existence event proves measurability and the simultaneous assertion for all kernel vectors and all omitted indices.
Using the original-size conditional law xi_N throughout comparable block sizes preserves its uniform anti-concentration constants and avoids a change of truncation law at each minor.

For B_0 consisting of the first N-1 rows, deleting coordinate i is contractive for its row distance.
The projected other rows are exactly D_i with its original-N row omitted.
Their measurable bilinear kernel vector depends only on D_i, while every coordinate of the projected exposed row is an off-diagonal variable independent of D_i.
The mirrored partners are in the deleted coordinate and do not survive in the conditioning matrix.
For a bilinear unit normal u, its Hilbert-space normal is conjugate(u), giving dist(z_i,H_i')>=|sum_j (z_i)_j u_j| with the stated orientation.
The radius N^(-a) is no larger than (N-1)^(-a).
The omitted-row concentration bound, union over N-1 retained rows and Gram-inverse identity therefore yield s_(N-1)(B_0)>=N^(-a-1/2).
Adding the last row is a positive semidefinite perturbation of B_0^*B_0, so the inequality for s_(N-1)(M) follows even though B_0 is rectangular.

The raw-entry union bound is C N^(2-2kappa), and kappa>(B+4)/2 supplies the required extra probability margin.
Conditioning on all independent cutoffs and then on diagonal values preserves the off-diagonal product law.
The entry exponent K has fixed slack for N versus N-1, and b>B+4 absorbs the row union.
Multiplying a normalized matrix by sqrt(N), applying the raw theorem to shift exponent gamma+1 and enlarging the final singular-value exponent proves the normalized version.
No least-singular-value premise enters this second-smallest argument.

### Complete assembly, uniformity and source limits

The accepted many-index input requires only its stated norm and rank guards, which are supplied by the finite-second-moment entry estimate and the reviewed raw corank tail after scaling.
The second-floor estimate applies to all actual principal minors by another enlarged polynomial failure exponent.
The isolated-minor exponents A_0 and L_iso are fixed before T_0,J,H and the final A.
The choice T_0>L_iso+L_2+2 ensures both t_1(sqrt(N)D_i)<=N^(-L_iso) and t_1(D_i)/t_2(D_i)<=N^(-L_iso) on the retained low-matching branch.
The exactly corank-one alternative is also one of the fixed isolated-minor theorem's explicit branches.
Thus this invocation does not expand the older restricted theorem to unverified minors.

The matching radius is h_N/N for normalized Wigner entries, and A>H+2K+2 enforces its exact scale condition.
The raw determinant-ratio identity has factor N because its numerator has degree N and its minor adjugate has degree N-2.
Consequently A>A_0+2K+2 supplies the raw isolated-minor ratio threshold.
The split must retain G_i in the low-matching intersection; the proof does so and never needs a small probability for the whole low-matching event.
The pointwise many-index bound averages the matching contribution, while the low-matching contribution is controlled by the isolated-minor union probability and common guard failures.
A common exceptional event can be added once to this average, up to its fixed prefactor, without a new factor N.
With r_N=floor(sqrt(N)), the accepted rate psi(r_N) is O(sqrt(log(2+N)) N^(-1/18)).
All chosen exponents are fixed after the laws,gamma,B, and every bound is uniform in the deterministic shift.
Conditioning on an independent shift within one dimension and integrating on its guard is valid without cross-size independence.

The exact direct interfaces were read in C_F0188_v2, C_F0194_v1, C_F0194_v2 and C_F0194_v3.
The fixed class, full profile count and rounding in v1, and the fixed distance, averaging, two-copy matching and norm arguments in v3 were inspected at their actual uses.
The symmetric-shift theorem and full corank-tail theorem were reused as accepted inputs at their stated scopes, without a recursive audit of their whole proof ancestry.
The Ngu12a unit and its source notes identify arXiv:1105.5733v1 Condition 1 and Theorem 1.3 on PDF pp. 2--3; those retained source facts and the local rounding interface support the real-scalar, dimension-two and uniform anti-concentration uses here.
Original literature PDFs were not reopened in this review, and the original inverse-theorem proof remains an accepted external input at its recorded inspection depth.
The MNV and bounded-product concentration source theorems likewise enter through the accepted exact v3 interfaces, without a new source-proof audit.
No unary argument from C_F0194_v4, numerical experiment, uninspected proof-assistant code, or assertion about arbitrary matrix-coefficient pencils is used.
The main error is not summable as displayed, and this review establishes neither an almost-sure full-sequence least-value floor nor any Brown-measure or broader Task completion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finding) | [Exact main and subsidiary assertions](../../claims/Yin_C_F0194_v5.md#statement) | Complete main bound, uncovered-diagonal exclusion, approximation and minor consequences, omitted-row concentration, raw and normalized second-smallest floors, all stated models, parameters and independent random-shift extensions. |
| [Whole-proof finding](#finding) | [Complete v5 argument](../../claims/Yin_C_F0194_v5.md#argument) | Entire new proof and assembly, including internal-row conditioning, cover union, deterministic identities, rectangular normals, Gram identity, probability and exponent order, raw scaling and exact limitations. |
| [Whole-proof finding](#finding) | [Exact candidate decision](../../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-candidate) | The selected candidate's complete assertion, argument and eleven declared direct dependencies at their actual displayed scopes; this review supplies evidence, not Claim adoption. |
| [Whole-proof finding](#finding) | [Symmetric-part floors](../../claims/Yin_C_F0188_v2.md#statement) | Accepted theorem only for genuinely complex symmetric shifts of real finite-second-moment Wigner matrices, with comparable dimensions, raw scaling and enlarged union-bound exponents checked. |
| [Whole-proof finding](#finding) | [Exact structured class](../../claims/Yin_C_F0194_v1.md#counting-class) | Rational progression candidates, precision and structural constants, and at least m-C_0 prescribed constraints as used for one omitted row. |
| [Whole-proof finding](#finding) | [Complete nonsymmetric-offset count](../../claims/Yin_C_F0194_v1.md#structured-vector-counting) | Omitted-row polynomial cost, full profile count, nonsymmetric centers, deterministic diagonals and uniform comparable-size truncated-law use. |
| [Whole-proof finding](#finding) | [Linear inverse and rounding interface](../../claims/Yin_C_F0194_v1.md#inverse-rounding) | Dimension-two real-scalar inverse theorem and rational rounding, with structural constants before fine precision and the new retained-row residual verified in v5. |
| [Whole-proof finding](#finding) | [Accepted linear source conventions](../literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Retained arXiv:1105.5733v1 Condition 1 and Theorem 1.3 conventions and applicability for real scalar laws and dimension-two coefficients; source notes read, original PDF and proof not newly audited. |
| [Whole-proof finding](#finding) | [Isolated-minor probability theorem](../../claims/Yin_C_F0194_v1.md#statement) | Exact raw corank-one or absolute-and-relative isolated branch, determinant-ratio threshold, polynomial shifts and union bound, used only after v5 establishes every premise. |
| [Whole-proof finding](#finding) | [Fixed linear-codimension distance](../../claims/Yin_C_F0194_v3.md#linear-codimension) | Uniform exponential estimate for independent real coordinates near complex affine subspaces of codimension at least half the ambient dimension, under B and x_I conditioning. |
| [Whole-proof finding](#finding) | [Accepted many-index averaging](../../claims/Yin_C_F0194_v3.md#spread-and-average) | Pointwise usable-index implication and averaged probabilities under the norm and rank guards, including singular corank one and no index-union loss. |
| [Whole-proof finding](#finding) | [Accepted finite-radius matching](../../claims/Yin_C_F0194_v3.md#two-copy-matching) | Exact real-law two-copy conditional estimate, nonsymmetric offsets, complex projection, normalized h/N scale and psi(r), without any typicality assumption for high matching. |
| [Whole-proof finding](#finding) | [Polynomial norm calculation](../../claims/Yin_C_F0194_v3.md#polynomial-shift-proof) | Finite-second-moment raw-entry union bound and normalized norm guard at the enlarged requested failure exponent. |
| [Whole-proof finding](#finding) | [Reviewed corank guard](../../claims/Yin_C_F0194_v2.md#decision-corank-tail-reviewed) | Accepted full corank-at-least-two tail for arbitrary complex nonsymmetric polynomial shifts, with normalized-to-raw substitution checked; no second-smallest claim imported. |
