---
author: Yin
---

# Independent review of many-index cofactors and finite-radius matching

The review act was completed at 2026-11-05T10:28 UTC for the registered human Yin.
The fixed object is the complete [C_F0194_v3 statement](../../claims/Yin_C_F0194_v3.md#statement) and [argument](../../claims/Yin_C_F0194_v3.md#argument), under its [many-index candidate decision](../../claims/Yin_C_F0194_v3.md#decision-many-index-candidate).
This was a separately arranged initial independent whole-argument inspection.
The reviewer was outside substantive proof development and received the fixed inputs, necessary dependency locators, actual human requirements, operational facts and applicable rules.
No development draft, proof-generation dialogue, author explanation or mathematical development summary was supplied or consulted.
The reviewer formed initial findings from the entire v3 statement and proof before consulting the earlier R_F0200 family.
No substantive repair was supplied.

All three declared direct dependencies were read in their actual mathematical and adoption scope.
The concentration input and Gram identity in [C_F0187_v2](../../claims/Yin_C_F0187_v2.md#argument) were checked against its accepted decision, the applicable [independent finding](Yin_R_F0191_v2.md#complex-intermediate-bound-reviewed) and [GNT14 edition notes](../literature/GNT14/readme.md).
The exact real-coefficient fair-sign theorem, matching-rank definition and interval scaling were read in [MNV16-U001](../literature/MNV16/Yin_U001.md#mnv16-u001) with its [2016 journal-edition notes](../literature/MNV16/readme.md).
Those established concentration and anticoncentration inputs are accepted at their recorded source-statement scope; neither original source proof was newly audited.
The complete [C_F0194_v2 argument](../../claims/Yin_C_F0194_v2.md#argument), its actual accepted decision and [R_F0200_v2 finding](Yin_R_F0200_v2.md#finding) were read.
Only its accepted raw real-Wigner corank-tail theorem is reused, without recursively re-auditing its earlier counting module or inverse-theorem proof.
R_F0200_v1 and v2 were read before choosing this next version of the same cofactor-review family.
Neither earlier finding supplies inspection of the new v3 deduction.
The applicable erratum and maintenance files were read and were empty.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete many-index and matching finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete many-index and matching finding](#finding) | [Exact statement](../../claims/Yin_C_F0194_v3.md#statement) | Entire normalized real-input theorem: arbitrary independent diagonal laws in the norm-guarded core, arbitrary deterministic complex shifts, uniform constants, coarse spread, principal cofactors, both averaging assertions and independent random shifts. |
| [Complete many-index and matching finding](#finding) | [Polynomial-shift assertion](../../claims/Yin_C_F0194_v3.md#polynomial-shift-consequence) | Fixed finite-second-moment diagonal law, every positive entry-bound and failure exponent, the stated order of fixed exponents, every allowed deterministic matching-size sequence, retained low-matching mean and marginal convergence consequence. |
| [Complete many-index and matching finding](#finding) | [Complete argument](../../claims/Yin_C_F0194_v3.md#argument) | All new deterministic and probability steps, including singular cases, fixed-cutoff distance concentration, all-support rectangular union, right-vector spread, cofactor average, exact two-copy conditioning, complex projection, coefficient normalization and polynomial norm/corank exceptions. |
| [Complete many-index and matching finding](#finding) | [Selected candidate](../../claims/Yin_C_F0194_v3.md#decision-many-index-candidate) | Exact statement, argument and three declared dependency selections inspected; this review does not select a new Claim assessment. |
| [Complete many-index and matching finding](#finding) | [Declared concentration dependency](../../claims/Yin_C_F0187_v2.md#argument) | Only accepted bounded-product convex concentration for independent bounded real coordinates and the elementary complex Gram-inverse negative-second-moment identity; the earlier moving-cutoff distance rate is not imported. |
| [Complete many-index and matching finding](#finding) | [Accepted concentration assessment](../../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Checked actual adoption and applicable R_F0191_v2 scope for the reused external concentration input; no new least-singular-value conclusion is inferred. |
| [Complete many-index and matching finding](#finding) | [Declared MNV16 dependency](../literature/MNV16/Yin_U001.md#mnv16-u001) | Definition 1.5 and Theorem 1.6 in the selected 2016 Theory of Computing edition, PDF pp. 2--3: real multilinear fair-sign polynomial, degree-two matching rank, arbitrary lower terms and interval center; original proof accepted externally. |
| [Complete many-index and matching finding](#finding) | [MNV16 scaling interface](../literature/MNV16/Yin_U001.md#quadratic-specialization) | Degree-two exponent 1/9, strict length-one interval containment, factor two for distinct quadratic coordinates and factor 1/n for normalized Wigner entries. |
| [Complete many-index and matching finding](#finding) | [Declared corank dependency](../../claims/Yin_C_F0194_v2.md#decision-corank-tail-reviewed) | Accepted raw real finite-second-moment polynomial-shift corank-at-least-two tail, used only for the normalized polynomial-shift consequence after scaling by sqrt(n). |
| [Complete many-index and matching finding](#finding) | [Raw corank statement](../../claims/Yin_C_F0194_v2.md#statement) | Exact finite-second-moment laws, arbitrary nonsymmetric complex shifts, polynomial entry guard, every positive probability exponent and uniform constants, checked at the consuming substitution. |
| [Complete many-index and matching finding](#finding) | [Random-shift corank interface](../../claims/Yin_C_F0194_v2.md#random-shift-statement) | Within-dimension independent random shift and guarded integration; no cross-dimensional conditioning or stronger nonsingularity assertion is used. |

<a id="finding"></a>
## Outcome

No unresolved mathematical gap was found in the entire exact C_F0194_v3 statement or its new argument under the accepted inputs and source-proof limits above.
The argument supports the many-index cofactor average, the finite-radius matching reduction and its finite-second-moment polynomial-shift consequence with the low-matching term retained.
It does not show that large matchings are typical in the actual minors.

### Deterministic algebra and exactly singular matrices

The top block row of the adjugate is \([\det D_i,-b\operatorname{adj}D_i]\), including singular blocks by polynomial continuation.
The identity \(D_i\operatorname{adj}D_i=(\det D_i)I\) gives
\[
 \sqrt{n-1}\,|\det D_i|
 \le \|D_i\|\,\|\operatorname{adj}D_i\|_F.
\]
Combining it with the bounds on the off-diagonal row and principal compression yields the stated \(\sqrt2\|M\|\|A_i\|_F\) upper bound on the full adjugate row.

For invertible M, a right least-singular vector v is an eigenvector of \(M^{-1}(M^{-1})^*=(M^*M)^{-1}\) with eigenvalue \(\sigma^{-2}\).
The i-th diagonal entry of this positive matrix therefore gives the row lower bound \(|v_i|/\sigma\), even with a multiple least singular value.
It follows that \(A_i\ne0\) and the stated ratio inequality hold whenever \(v_i\ne0\).
There is no assumption about left/right coordinate overlap or a singular-value gap.

At exact corank one the nonzero adjugate has the form \(\eta vu^*\) for right and adjoint-left unit kernel vectors.
Every nonzero \(v_i\) again gives a nonzero full adjugate row and hence \(A_i\ne0\), while the determinant ratio is zero.
Full corank at least two is excluded from the averaging event and is removed only in the separate polynomial-shift consequence.
A zero \(A_i\) is never divided by or assigned a matching graph.

### Fixed cutoff, complex subspaces and all rectangles

Finite second moment gives a fixed cutoff R for which the discarded probability is at most \(1/64\) and the retained conditional variance is at least \(1/2\).
The bad-coordinate estimate has a genuinely negative exponent because
\[
 -1/8+\log(1+(e-1)/64)<0.
\]
Conditional on the specified good set, the retained coordinates remain independent.
Coordinate projection loses at most the number of deleted coordinates in complex codimension, and adding the single mean-plus-shift vector loses at most one further dimension.
Thus the good-set complement projection has complex rank at least \(p/4\) for large p.

For real centered coordinates y and a complex orthogonal projection P, the identity \(\mathbb E\overline y_jy_k=v_R\delta_{jk}\) gives \(\mathbb E\|Py\|^2=v_R\operatorname{Tr}P\ge p/8\).
No circular complex law or nonsingular real two-dimensional covariance is required.
The projection norm, restricted to real coordinate variables, is convex and 1-Lipschitz.
Accepted bounded-product concentration applies with fixed support diameter \(2R\).
Its integrated squared deviation from a median is \(O(R^2)\), so the L2 triangle inequality forces that median to be at least \(\sqrt{p/8}-O(R)\).
The resulting lower-tail bound is exponential in p, uniformly in the complex subspace, arbitrary shift and specified good set.
This is a new fixed-cutoff deduction, rather than an unsupported strengthening of C_F0187_v2's moving-cutoff estimate.

For a disjoint cut I,J, each entry of the raw rectangle comes from a distinct strict-upper Wigner variable.
Its columns are independent and have independent coordinates; mirrored partners do not occur inside that rectangle.
Conditioning on the other columns leaves codimension at least \(n-2k+1\ge(n-k)/2\), so the distance estimate applies uniformly in every deterministic shift.
Positive column distances give full column rank.
The inverse Gram diagonal identity and trace yield
\[
 s_{\min}(B)^{-2}\le \sum_j s_j(B)^{-2}\le Ck/n.
\]
Dividing B by \(\sqrt n\) gives a lower bound \(c/\sqrt k\ge c/\sqrt n\).
The constants can be fixed uniformly for all cut proportions at most \(1/4\), before selecting delta.
The support entropy is at most \(2\delta n\log(e/\delta)\); the stated small fixed delta leaves exponential decay after the support union.
The resulting event is measurable jointly in the Wigner entries and shift because it is a finite intersection of singular-value conditions.
It uses no diagonal law.

### Spread and the exact average

On the norm guard, the rectangular floor implies that a unit vector with residual at most \(a/(4\sqrt n)\) cannot have complementary norm at most \((a/8)n^{-K-1/2}\).
Indeed the lower bound on the residual in the proof is \(3a/(8\sqrt n)\), which is strictly larger.
If at most k coordinates exceed \((a/8)n^{-K-1}\), a support containing them has complementary norm at most that forbidden threshold.
This proves the coarse spread with constants independent of K; only the sufficiently large dimension may depend on K.

For the right least-singular vector, the deterministic ratio bound at each such coordinate is at most
\[
 \frac{8\sqrt2}{a}\,n^{2K+1}\sigma.
\]
The same count applies to a right kernel vector at corank one.
More than \(\lfloor\delta n\rfloor\) usable coordinates in particular gives the claimed \(\delta n/2\) count.
The pointwise indicator inequality therefore has factor \(2/(\delta n)\), and expectation gives the stated average without any independence among principal minors or a union over omitted indices.

### Exact conditioning and the MNV16 interface

Conditional on \(D_i\) and the exposed diagonal, the remaining raw row coordinates have their original independent law.
The bordered determinant formula has quadratic part \(-x^TQ_ix/n\); different complex row and column shifts change only lower-degree terms.
The lexicographic matching and real-or-imaginary projection can be chosen measurably from the minor.
At least half the selected edges have one common projected entry of \(Q_i\) with modulus at least \(h\|A_i\|_F/\sqrt2\).

The two-copy construction selects one of two iid copies in each coordinate and therefore preserves the exact original product law.
Nondegeneracy gives fixed \(b_0,p_0>0\).
Disjointness of the matching makes endpoint survival independent between edges, with probability at least \(p_0^2\), so a survival count below a fixed positive multiple of r has exponentially small probability.
For sufficiently large r the surviving count is at least a fixed positive multiple of r and at least two.
The finitely many remaining r are covered by enlarging the final constant.

After conditioning on the copies, the fair signs remain independent and every squared-coordinate contribution is affine.
For a surviving edge the projected multilinear quadratic coefficient has modulus at least
\[
 \frac{2b_0^2}{n}\,\frac{h\|A_i\|_F}{\sqrt2}
 =\frac{\sqrt2\,b_0^2h\|A_i\|_F}{n}.
\]
Choosing \(c_*\) sufficiently small makes the projected disk event, after division by this scale, lie inside an interval of length strictly less than one.
The precise degree-two real fair-sign MNV16 theorem applies with unrestricted lower-degree coefficients and interval center.
Its coefficient matching rank is at least a fixed multiple of r.
The bound \(\sqrt{\log(2+r)}r^{-1/9}\) follows from the source bound at that rank, using eventual monotonicity and absorbing bounded ranks into the constant.
Integrating the copies recovers the original row law, with no density, symmetry of xi or higher moment assumption.

On the scale-match inequality, this controls \(\mathbb P(G_i\cap H_i)\) by \(C\psi(r)\).
Splitting off \(H_i^c\) in the exact average gives precisely the retained mean low-matching probability.
On the alternative many-matching guard, at most \(\delta n/4\) indices fail H_i, leaving at least \(\delta n/4\) simultaneous usable indices and the claimed guarded estimate.
The argument uses no independence between these events.

### Polynomial shifts and the full probability statement

The finite second moments of both fixed laws give a full raw-entry cutoff failure at most \(Cn^{2-2\kappa}\).
Taking \(\kappa>(B+2)/2\) makes this at most \(C_Bn^{-B}\).
On its complement the normalized Wigner norm is at most \(n^{\kappa+1/2}\); on Gamma_n the shift norm is at most \(n^{\gamma+1}\).
A fixed K strictly larger than both exponents absorbs their sum for all sufficiently large n.

The raw matrix \(\sqrt n M_n\) has the exact laws of the accepted C_F0194_v2 corank theorem.
On Gamma_n its shifted entries are at most \(n^{\gamma+1/2}\le n^{\gamma+1}\).
Its rank is unchanged.
The accepted theorem at entry exponent \(\gamma+1\) and failure exponent B therefore removes corank at least two with cost \(C_Bn^{-B}\).
This is the only step here that uses C_F0194_v2.

With \(h=n^{-H}\) and \(\varepsilon=n^{-A}\), the scale-match condition follows for every fixed \(A>H+2K+2\), including its constants, and the residual-radius condition holds eventually as well.
Conditioning on the independent shift in this dimension and integrating only over Gamma_n gives the low-matching terms with the exact intersection \(H_i^c\cap\Gamma_n\).
The exponential rectangle failure is absorbed into \(C_Bn^{-B}\), while Gamma_n's complement is added once.
This proves the entire displayed polynomial-shift bound for every allowed deterministic sequence r_n.

All dimensionwise constants are uniform over the shift realization and distribution.
No cross-dimensional independence or conditioning on a whole shift sequence is used.
If r_n tends to infinity, both terms in psi tend to zero, so the stated additional vanishing assumptions imply convergence of the least-singular-value probability to zero.
Those assumptions alone imply no summability.

### Limits

This finding is a mathematical proof and dependency-interface review of the complete fixed v3 candidate, without formal verification.
The accepted GNT14 concentration and MNV16 anticoncentration proofs were not newly audited, and the accepted corank theorem is reused at its exact raw-law scope.
No typicality estimate for actual-minor matchings, positive polynomial least-singular-value floor, genuinely complex off-diagonal extension or general matrix-coefficient-pencil theorem is established.
The finding does not complete F0012, F0013 or F0014, or change any Claim, Task or execution decision.
