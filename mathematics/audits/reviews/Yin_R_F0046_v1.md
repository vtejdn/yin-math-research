---
author: Yin
---
# Independent review of adjoint tuples, right duals and reversal symmetry

Review performed and recorded: 2026-10-14T14:08.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and inspected scope

The reviewer did not develop or edit [C_F0073 v1](../../claims/Yin_C_F0073_v1.md).
The coordinating agent assigned its complete fixed-material review after the argument was prepared by another agent.
Shared context included the general comparison question, the earlier normal-tuple and two-contraction results, and the author's statement of the intended checks.
The reviewer read the complete fixed candidate, reconstructed its conjugation and graph arguments, and checked the reduced-word reversal before forming this conclusion.
The candidate disclosed a preliminary root check; its correctness was not taken as evidence for the present verdict.

The inspected artifact is the complete C_F0073 v1 Statement, Argument and scope discussion, prepared at 2026-10-14T13:55 and read in the working tree on the review date.
All Parts A-C and the free-normal application are covered.
The exact C_F0069 and C_F0070 interfaces were checked; the entire C_F0072 proof was read and its quantitative, actual-adjoint and graph outputs verified for the present invocation.
The AP18 tracial-conjugation source note and the Voi98 free-product source unit are used at their already inspected scopes.
No new primary-source reading or full re-audit of their original predecessor proofs is claimed.

This review does not use the normal/singular decomposition under development elsewhere.
It does not turn conditional symmetry results into a conclusion for arbitrary correlated normal tuples.

## Current relationship clarification

The original dated independent wording remains historical.
The record identifies a fixed candidate, necessary earlier normal/two-contraction results and the intended review checks, which are legitimate inputs.
It does not establish whether the shared comparison context was limited to these fixed inputs or also carried substantive development about this adjoint/reversal proof.
The current whole-finding relationship is therefore unknown rather than guessed self from dependency reuse or the checklist.
No reviewer repair is recorded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0073 statement](../../claims/Yin_C_F0073_v1.md#statement) | All Parts A-C: actual-vacuum adjoint stability, exact three-way reduction under F(X), normalization and canonical domains, reversal-symmetry estimate and free-normal application. |
| [Conclusion](#conclusion) | [C_F0073 argument](../../claims/Yin_C_F0073_v1.md#argument) | Complete Sections 1-5, including every J sign, starred uniqueness, graph passage, right-action normalization and construction of the von Neumann antiautomorphism. |
| [Conclusion](#conclusion) | [C_F0069 Part A](../../claims/Yin_C_F0069_v1.md#statement) | Automatic norm-to-L2 boundedness of supplied full-domain normal duals, applied to X and X* and to the sign-converted J-conjugate system. |
| [Conclusion](#conclusion) | [C_F0070 Part A](../../claims/Yin_C_F0070_v1.md#statement) | Unique starred Hilbert-valued derivations and their normalized right contractions; diffuseness and uniqueness apply equally to X*. |
| [Conclusion](#conclusion) | [C_F0072](../../claims/Yin_C_F0072_v1.md#statement) | Both operator-norm-to-L2 contraction bounds give an actual vacuum of norm at most 2(C_E+C_F), the actual core adjoint and both canonical full domains. |
| [Conclusion](#conclusion) | [Voi98-U005](../literature/Voi98/Yin_U005_v1.md#voi98-u005) | Accepted/reconstructed pointed free-product Hilbert model and end actions in Sections 5.5-5.8 only; no use of the source's invalid literal compression formula. |
| [Conclusion](#conclusion) | [C_F0045 Section 3](../../claims/Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Existing realization of the whole reduced-word polynomial core; no marginal bound, freeness lifting estimate or later theorem conclusion imported. |
| [Conclusion](#conclusion) | [AP18 conjugation interface](../literature/AP18/Yin_U002_v2.md#tomita-foundational-reference) | Existing tracial J construction and its source boundary; both left/right conjugation formulas verified directly in the present review. |

## Actual vacua and the conjugation conventions

On bounded vectors J lambda(a) J=rho(a*) and J rho(a) J=lambda(a*); both sides are bounded, so these identities hold on H.
J is conjugate linear.
The tensor dagger is also conjugate linear and reverses the outer actions.
Consequently delta#(a)=(delta(a*)) dagger is complex linear, satisfies the outer Leibniz rule, and is involutive.
Its value on Y_j* is the prescribed delta_ij 1 tensor 1 when delta has that value on Y_j.

With the inner product linear in its second variable, the actual vacuum identity is

(tau tensor tau)delta(a)=tau(xi* a).

Conjugating after replacing a by a* gives tau(a xi)=tau(xi a), which is represented by xi*.
This is a bounded functional for the L2 norm on the entire same starred core, so it proves an actual adjoint-domain statement, not just a formal moment identity.
Applying the involution twice proves A(Y) if and only if A(Y*) without normality.

The contraction identities E#=J L J and L#=J E J follow on elementary tensors and extend through the bounded Hilbert slice maps.
No interchange of the ordinary flip with dagger, or of J with a complex-linear reversal, occurs.

## The exact adjoint-tuple reduction

Under F(X), the automatic bounds and unique starred derivations of C_F0069/C_F0070 apply to the exact normal generating tuple.
The same is true for X* whenever F(X*) is assumed.
The derivation delta_i# is already defined on the whole starred algebra and is normalized on X_j*.
Uniqueness for X* therefore identifies it with the derivation obtained from its supplied full-domain dual.
In particular its right contraction J L_i J is bounded.
This proves the left-contraction bound with no adjoint-domain assumption on the supplied duals.

Conversely, bounded E_i and L_i imply that both contractions of delta_i# are bounded.
The hypotheses of C_F0072 are exact: the same weakly dense unital star algebra, the outer derivation into the coarse Hilbert space, and the two norm bounds.
C_F0072 supplies a closable core right contraction with its canonical closure N_i containing all M Omega, and with the actual adjoint also containing all M Omega.

On the core, the Leibniz rule gives [N_i,X_j*]=delta_ij P.
If v belongs to Dom N_i, a sequence in the core converges to v in its graph norm.
Multiplying the sequence by X_j* preserves the core, and its N_i-images converge by the bounded commutator identity.
Closedness therefore proves invariance of the entire closure domain and the same identity there.
Thus -N_i restricted to M Omega has [X_j*,-N_i]=delta_ij P.
This is precisely F(X*), with the correct sign.

Applying C_F0072 separately to delta_i gives A(X) and both canonical domains for X.
The other application gives the corresponding assertions for X*.
Neither application identifies an arbitrary supplied full-domain map with a canonical closure on all M.

The constant in Part C is also correct.
With both contraction constants equal to C_i, C_F0072 gives 2(C_i+C_i)=4C_i, without assuming a real derivation or improving the non-Hermitian estimate.

## Right-action maps and normalization

A system [R_i,rho(X_j)]=delta_ij P transforms under J into

[JR_iJ,lambda(X_j*)]=delta_ij P.

Therefore D_i'=-JR_iJ has the generator-first relation for X*, and the inverse transformation is R_i=-JD_i'J.
M Omega is invariant under J, and double conjugation of a complex-linear map is complex linear.
These assertions do not require the maps to be continuous before C_F0069 is applied.

For G_i=JR_iJ, subtracting a G_i1 makes the normalized map G_i0.
It is bounded M-to-H by the normal-dual input and agrees on the starred core with the right contraction of delta_i#, namely J L_i J.
Directly,

J G_i0 J(a)=R_i(a)-R_i(1)a.

Thus the normalization is on the stated side, its value at 1 vanishes, and its restriction to the core is L_i.
The correction a -> R_i(1)a commutes with all right multipliers.
Both the dual identity and the boundedness claimed for R_i0 are consequently justified.

Direct conjugation of E_i instead gives a right-action relation for X_j*, not for X_j.
Equation (14) accurately records this limitation; the proof does not use a single J-conjugation to assume adjoint stability.

## The prescribed reversal symmetry

For a trace-preserving complex-linear star antiautomorphism sigma, V(a Omega)=sigma(a) Omega is an isometry because

tau(sigma(a)* sigma(a))=tau(sigma(aa*))=tau(a*a).

Surjectivity gives a complex-linear unitary on H fixing Omega.
Its restriction to M is operator-norm isometric.
On bounded vectors V lambda(a) V inverse=rho(sigma(a)), hence everywhere by boundedness.
The maps R_i=V E_i V inverse are defined on all M Omega because sigma maps M onto M.
They have the exact right-action relation, vanish at Omega, and retain the M-to-H norm C_i.
The preceding normalization result identifies their core values with L_i.
This proves the asserted estimate and the canonical consequences.

No invariance of each X_j under an unspecified involution is assumed: sigma(X_j)=X_j is an explicit hypothesis here.

## Free normal coordinates and extension to the von Neumann algebra

For freely independent normal coordinates, each B_j=W*(X_j) is abelian.
Freeness identifies the tracial Hilbert space with the pointed free-product tensor model, by sending centered reduced tensors to their products.
The existing source and full-core interfaces support exactly this identification.

Reversing the tensor order is complex linear and isometric on every summand; the reversed indices still form a reduced word.
The resulting V is a unitary involution fixing the vacuum.
On bounded centered reduced tensors, left multiplication by a in B_j creates a new first factor when the first index differs from j; reversal turns this into the corresponding right creation.
When the first index equals j, decompose a eta_1 into its scalar and centered parts.
The scalar contraction and remaining centered term reverse to the analogous right-end terms.
Abelianness of B_j gives a eta_1=eta_1 a at that end.
The vacuum case agrees as well.
This verifies V lambda(a) V=rho(a) for every a in B_j.

Conjugation by V is normal on B(H), so generation gives

V lambda(M) V=W*(rho(B_1),...,rho(B_d))=rho(M).

Right multiplication is a faithful normal star anti-representation.
Its inverse on rho(M), composed with conjugation by V, defines a surjective complex-linear star antiautomorphism sigma of M.
This construction proves the extension to all M; it is not merely an algebraic reversal on words.
It fixes every B_j, hence every X_j.
The vacuum coefficient verifies trace preservation.
All hypotheses of the preceding symmetry argument are supplied.

The argument requires no unspecified reversal of nonabelian internal factors and does not assume that arbitrary free normal laws possess full-domain duals.
The application retains F(X) as a hypothesis.

## Conclusion

The exact statement and complete argument of C_F0073 v1 pass this independently organized review with no required mathematical correction.
This supports proved / independently reviewed for that fixed claim if adopted by its responsible decision.

The supported advance is the exact equivalence, under F(X) and normality, between bounded left contractions, existence of the stated right-action systems, and F(X*).
Actual vacua are separately invariant under adjoint tuples for arbitrary bounded generating tuples.
A trace-preserving complex-linear reversal fixing the generators supplies the missing conditions, including for free normal coordinates satisfying F(X).

The review does not prove F(X) implies F(X*) for an arbitrary correlated normal tuple and does not infer that implication from A(X) if and only if A(X*).
Accepted source interfaces retain their recorded edition, passage and original-proof limitations.
No external priority claim, numerical verification, formal proof, manuscript review or Task-completion finding is made.
