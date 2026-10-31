---
author: Yin
---
# Independent whole review of starred derivations and the canonical full-domain equivalence

Review performed and recorded: 2026-10-14T10:31.
Human record author: Yin.
Review method: separately assigned AI mathematical review, not personal human inspection.

## Arrangement, sequence and scope

The reviewer did not develop or edit [C_F0070 v1](../../claims/Yin_C_F0070_v1.md).
Shared context included the user's two ACSY24 comparison questions and the earlier work on the distinct canonical-domain direction.
Before the fixed Claim was supplied, the coordinating author sent the continuous-partition candidate and its proposed comparison conclusion.
The reviewer checked that candidate read-only, independently expanded the sign-average estimates, and cautioned against extending agreement on the polynomial core to agreement on all M.
That was a preliminary review of a supplied argument, not contribution of a missing proof step.
It was disclosed to the proof author.
The fixed Statement, complete S1--S19 argument, added vacuum corollary and source section were then read and checked in full.
No Claim edits were made.

This review covers Parts A--C of the exact 2026-10-14 C_F0070 v1 and its stated dependencies.
The reviewer had separately completed the whole C_F0069 v1 review retained in [R_F0042](Yin_R_F0042_v1.md#conclusion); that unchanged automatic-continuity result is reused at Part A only, and its interface was checked anew.
No review of the two unresolved general questions is inferred from the present statement.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0070 statement](../../claims/Yin_C_F0070_v1.md#statement) | Exact Parts A--C: unique starred-core derivations from bare normal duals, three-way equivalence under ACSY24 and actual single-vector vacuum corollary. |
| [Conclusion](#conclusion) | [C_F0070 argument](../../claims/Yin_C_F0070_v1.md#argument) | Entire S1--S19 proof, continuous partitions and finite sign averages, coarse-kernel injectivity, graph restoration and final vacuum calculation. |
| [Conclusion](#conclusion) | [C_F0070 source relationship](../../claims/Yin_C_F0070_v1.md#source-relationship-and-limits) | Exact dependency scopes, prior mechanism attribution, actual canonical closure and unproved general-implication boundaries. |
| [Conclusion](#conclusion) | [C_F0069 statement](../../claims/Yin_C_F0069_v1.md#statement) | Part A automatic M-to-H boundedness and diffuseness applied to each diagonal generator relation; unchanged complete support reused from R_F0042. |
| [Conclusion](#conclusion) | [C_F0069 argument](../../claims/Yin_C_F0069_v1.md#argument) | Part A interface only, with bare full-domain operators, normal coordinates and no closability or adjoint premise. |
| [Conclusion](#conclusion) | [CS77-U001](../literature/CS77/Yin_U001.md#cs77-u001) | Exact bounded-map Fuglede specialization on B(M,H), including its hermitian generators and absence of a required H-to-H extension. |
| [Conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 closability of the specified canonical starred core and the actual vacuum-adjoint definition used in Parts B and C. |

## Kernel and bounded-map commutation checks

The preliminary one-coordinate statement has precisely the needed assumptions: E is bounded from the operator norm of M to H, x is normal, and the commutator relation holds on all M.
The spectral-atom contradiction uses only bounded-vector inputs and faithful trace.
The marginal diagonal is therefore null, and the phase kernel k_x is an actual L2 vector of norm one.
Under Theta its HS commutator with x has kernel `(w-z)k_x(z,w)=bar(w)-bar(z)`, which is the kernel of `[P,x*]`; thus (S2) has the correct sign.

The Jacobi computation (S3) is legitimate for maps on M because all left multiplications involved preserve M.
Normality of x removes the extra commutator term.
F is bounded M-to-H and commutes with x, so the exact CS77 specialization applies.
For clarity, on V=B(M,H) the real and imaginary commutator operators are commuting hermitian operators: their real exponential groups act by left unitary multiplication on H and inverse left unitary precomposition on M.
Both are isometries.
Proposition 1 with Q=0 gives commutation with x*.
This supplies commutation with C*(x) by uniform approximation, without asserting weak continuity of F or Hilbert-space closability of E.

The primary Cambridge CS77 PDF was reopened at Proposition 1 and its following kernel consequence, printed p.197.
Its exact bounded-map specialization in CS77-U001 was checked directly.
The source's standard hermitian/normal convention and the opening printed wording issue are already explicit in that U; the application uses the displayed commuting hermitian operators.
The source's cited foundational proof chain was not re-audited.

## Continuous partitions and the vanishing defect

A fixed planar grid supplies nonnegative smooth bumps with uniformly bounded overlap; normalizing by the square root of their squared sum on a neighborhood of the compact spectrum gives (S4).
Only finitely many bumps meeting that spectrum are needed.
Grid size is chosen proportional to epsilon, so the support diameter condition holds on the spectrum and the overlap number q is independent of epsilon.
No rectifiability or one-dimensional spectral hypothesis is hidden here.

For each sign choice, pointwise Cauchy-Schwarz with at most q active functions gives both estimates in (S5), including the factor epsilon for r_j.
Commutation of F with chi_j and the quadratic partition identity give (S6).
The constants bar(lambda_j) cancel in (S7) by complex linearity of E.
Expanding each finite Rademacher average kills exactly the off-diagonal terms; bounded left multiplication on H and the M-to-H norm of E give the two bounds C q epsilon ||a||.
In particular the estimates do not grow with the number of grid functions and do not use an H-to-H bound for E.

The second term is an actual HS operator with kernel (S9).
Cauchy-Schwarz bounds the partition factor by one.
A nonzero summand forces both spectral points into a support of diameter at most epsilon.
Therefore its squared norm is bounded by the product-measure mass of `|z-w|<=epsilon`, which tends to zero by diffuseness.
This also makes the convergence rigorous when the partitions vary with epsilon.
Equations (S6)--(S10) give F=0 on every bounded vector.
The homogeneous case uses the same bounded-map Fuglede input directly and needs no diffuseness.

## Represented derivations and uniqueness

For the supplied tuple, applying C_F0069 Part A to -D_i and X_i yields both the required norm continuity and coordinate diffuseness.
The normalization in (S11) is bounded M-to-H because multiplication of a fixed L2 vector by a is bounded by ||a||.
It annihilates Omega and has the stated positive dual-first commutator.
The diagonal starred commutator follows from the partition proof; the off-diagonal ones vanish by the homogeneous Fuglede assertion, using individual normality only.

The product rule expresses every commutator on the represented starred algebra as an HS operator restricted to M.
Density of M Omega gives uniqueness of this extension, so zero evaluated polynomials cannot introduce representation dependence.
Theta is unitary and intertwines exactly the outer bimodule actions with left/right multiplication of HS operators.
Hence (S13)--(S15) define a genuine derivation on A and identify its vacuum contraction, without a closability inference.

The uniqueness argument is valid on the full coarse Hilbert space.
The two spectral algebras acting on its separate legs carry their faithful product trace; the diagonal joint spectral projection has trace `(mu_j tensor mu_j){z=w}=0`, hence is zero as an operator.
This proves injectivity of L_j despite possible spectral multiplicity on the full H.
Differentiating the actual normal relation gives (S16) with the stated sign.
Its prescribed phase vector solves the equation, so every derivation with the unstarred generator values has those same starred values.
Agreement on all generators and adjoints gives agreement on A.
No adjoint condition is used for this uniqueness.

## Canonical-closure equivalence

Under the additional ACSY24 hypotheses, its Theorem 3.4 supplies closability of exactly E_i0 on A Omega.
The source interface in ACSY24-U001 has this scope, and does not supply full-M domains by itself.
A bare full-domain dual normalized as in (S11) has the same starred derivation by the preceding uniqueness, so its restriction agrees with the supplied canonical core.
Its M-to-H bound yields (S18) on the entire starred core.

Kaplansky density followed by uniform polynomial approximation gives uniformly norm-bounded approximants to every a Omega.
Reflexivity supplies a weakly convergent subnet of the bounded outputs.
The graph of the original canonical closure is a norm-closed linear subspace of H direct_sum H and hence weakly closed; the weak limit lies in that graph.
This proves actual original-closure membership, not existence of an unspecified extension.
Conversely graph-core approximation and boundedness of X_j and P give (S19), so the restriction of the canonical closure supplies condition 3.
Its sign reversal gives condition 2.
These implications prove exactly the three stated existential conditions.

The proof correctly identifies the supplied normalized map with the canonical core only on A.
It does not use the false inference that A is operator-norm dense in M, does not identify the two maps on every bounded vector, and does not conclude that the supplied algebraic full-domain map is Hilbert-space closable.
The comparison therefore retains its needed quantifiers.

## Single-vector adjoint corollary

The supplied D_i has dense domain M Omega, so its Hilbert adjoint is defined as an operator even if that adjoint's domain is not dense.
Membership of Omega in that domain is sufficient.
With the inner product linear in its second argument and eta_i=D_i Omega,

`<Omega,E_i(a)>=-<D_i* Omega,a>+tau(a eta_i)`.

Traciality for bounded-L2 products follows by L2 approximation of eta_i by bounded elements and gives `tau(a eta_i)=tau(eta_i a)=<eta_i*,a>`.
Thus the exact representing vector is `-D_i* Omega+eta_i*`.
The contraction identity (S15) converts this to the vacuum pairing for delta_i.
Since the generating starred core is dense in H, this is precisely the actual delta_i-adjoint condition, including the claimed vector.
No density of Dom D_i*, closedness of D_i, or closed graph theorem for the supplied map is required.

If a consumer starts with a larger-domain D_i, restriction to M Omega preserves the value of D_i* Omega whenever the latter exists.
This observation checks the restriction interface under the stronger premise M Omega subset Dom D_i intersect Dom D_i*, without adding any further operator-domain conclusion.

## Source and conclusion

C_F0069 Part A is the genuine project input; CS77-U001 is the genuine published bounded-map input; ACSY24-U001 supplies the canonical-core closure in Part B and the actual-adjoint meaning.
The phase uniqueness and graph restoration mechanisms attributed to C_F0025 and C_F0027 are reproduced with sufficient local justification.
C_F0037 supplies proof provenance, not an assumed theorem with the new bare-domain hypotheses.
The inspected evidence does not establish novelty, priority, or exhaustive literature absence.

## Conclusion

The complete C_F0070 v1 Parts A--C and their full S1--S19 argument and vacuum calculation pass this independently organized review, with no required mathematical correction.
The exact fixed claim can support proved / independently reviewed if this finding is adopted by the coordinating author.

This result removes the closability assumption from the starred-derivation construction, proves the stated equivalence under ACSY24, and gives ACSY24 under the additional single-vector adjoint premise.
It does not establish that ACSY24 alone supplies full-M canonical domains, nor that the bare normal dual premise alone supplies an L2 vacuum.
No formal verification, manuscript-layout inspection or completion of either unresolved general implication is claimed.
