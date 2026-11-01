---
author: Yin
---

# Bounded canonical duals from a bounded derivative contraction: whole-candidate review

Review act: 2026-11-01T07:04 UTC.
Human record author: Yin.
The reviewed artifact is the 2026-11-01 working-copy candidate [Yin_C_F0092_v1](../../claims/Yin_C_F0092_v1.md), with candidate decision dated 2026-11-01T06:57.
The mathematical review covers the complete Statement and Argument, including the optional second-conjugate comparison.
It is neither maintenance acceptance nor manuscript review.

## Arrangement and inputs

A separately assigned agent performed this review without contributing to development of the fixed candidate.
No proof-development dialogue, author mathematical summary or prior verdict was supplied in the assignment.
The reviewer first read the fixed candidate and then its directly linked mathematical inputs.
Reading [Dab10-U002](../literature/Dab10/Yin_U002.md#1-conventions-and-the-exact-source-interfaces) exposed the duplicate local deduction in Section 4 and the older review conclusion in Section 5 before the reviewer completed and recorded its initial findings.
Consequently this finding is classified as `self-reviewed`; no independent relationship is claimed, and no proof-development role is invented for the reviewer.
The subsequent inspection rechecked the actual domain limits, adjoint identities and bounded-extension steps rather than relying on the earlier verdict.
A later bounded search of project review references identified existing responsible evidence; its earlier conclusions supply no new independent finding.

The accepted foundational inputs are the conjugate-variable selfadjointness, algebraic-freeness, polynomial-adjoint and closability interfaces in [Voi98-U002](../literature/Voi98/Yin_U002.md#conjugate-variables), [Voi98-U004](../literature/Voi98/Yin_U004.md#adjoint-domains-and-closability-41-43), and the relevant [C_F0022 interface](../../claims/Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input).
Voi98-U002 records Definition 3.1, Lemma 3.3 and the first-order algebraic-freeness interface at printed pp. 192-194.
Voi98-U004 records Propositions 4.1-4.3 at printed pp. 203-204, including the full two-leg adjoint formula.
Their hypotheses match the candidate's bounded selfadjoint generating tuple, faithful finite trace and existing conjugate system.
The inner-product convention is converted to linearity in the second variable; the adjoint operators and tensor-leg positions remain unchanged.
These established interfaces are accepted at the retained source-inspection depths; their original primary proofs were not freshly audited here.
Dab10-U002 supplies attribution for the related adjoint/coassociativity mechanism, not an external assertion of the exact new theorem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [Exact statement](../../claims/Yin_C_F0092_v1.md#statement) | Complete hypotheses and conclusions for every finite d>=1, the single-coordinate bounded contraction, positivity, exact right-multiplier and norm identities, simultaneous duals and bounded-spatial-derivative specialization. |
| [Whole-candidate finding](#whole-candidate-finding) | [Exact argument](../../claims/Yin_C_F0092_v1.md#argument) | Entire polynomial-adjoint, graph-product, coassociativity, positivity and bounded-extension proof, together with the optional bounded second-conjugate comparison. |

## Obligations and decisive checks

### Domains and polynomial adjoints

The generating selfadjoint tuple makes A dense in H.
Conjugate-variable selfadjointness and the polynomial adjoint formula give \(E_0p=\partial^*(p\otimes1)=p\xi-D_0p\) with exactly the candidate's contraction \((\mathrm{id}\otimes\tau)\partial p\).
The polynomial pairing gives \(E_0\subseteq D_0^*\) and also \(D_0\subseteq E_0^*\), so both densely defined operators are closable.
In particular \(E_0\subseteq D^*\) for \(D=\overline{D_0}\); the quadratic-form identity uses this actual closed-operator adjoint relation.

For polynomial graph approximants \(\xi_n\), left multiplication by p is bounded on H and by \(p\otimes1\) on \(H\otimes_2H\).
If \(\partial p=\sum_k a_k\otimes b_k\), the map \(\eta\mapsto\sum_k a_k\otimes b_k\eta\) is bounded from H to \(H\otimes_2H\), with norm at most \(\sum_k\|a_k\|_2\|b_k\|\).
Both terms in the polynomial Leibniz identity therefore converge, so derivative closedness proves the stated domain and product identity for \(p\xi\).
Applying the bounded Hilbert partial trace to the same polynomial graph pairs proves \(p\xi\in\operatorname{Dom}D\) and identifies its D-image.
This needs neither boundedness of \(\xi\) nor an unsupported equality between a closure of a composition and a composition of closures.

### Tensor legs, coassociativity and positivity

For every polynomial word, both \((\mathrm{id}\otimes\partial)\partial\) and \((\partial\otimes\mathrm{id})\partial\) sum once over each pair of increasing cut positions in the same coordinate.
Thus the algebraic coassociativity identity is valid, including in dimension one.
Conjugacy and traciality give \(\tau(b_k\xi)=(\tau\otimes\tau)\partial b_k\).
Contraction by \(\mathrm{id}\otimes\tau\otimes\tau\) identifies the remaining term with \(D_0^2p\), without exchanging the partial traces.
Because \(D_0p\) is polynomial, this proves \(E_0p\in\operatorname{Dom}D\) and \(DE_0p=pB\).

The adjoint relation gives \(\|E_0p\|_2^2=\langle p,DE_0p\rangle=\tau(p^*pB)\).
Before positivity of B is known, the upper bound follows from \(|\tau(p^*pB)|\leq\|B\|\|p\|_2^2\) and the nonnegative equality already obtained.
Right multiplication \(\rho(B)\) is bounded, so its quadratic form is nonnegative on all H by density of A.
Hence \(\rho(B)\) is positive, and the faithful right representation of the opposite algebra reflects positivity, giving \(B\geq0\).
No positivity or boundedness of the full derivative tensor is assumed here.

### Bounded closure, exact norm and dual identities

The estimate gives the unique bounded extension \(E^{\mathrm b}\) of \(E_0\).
The polynomial adjoint identity puts \(D_0\) inside \((E^{\mathrm b})^*\), and \(D_0\) equals the restriction of this bounded operator to the dense domain A.
Its graph closure is therefore \((E^{\mathrm b})^*\) on all H, so \(D^*=E^{\mathrm b}\).
Both sides of \(DE_0p=pB\) now extend as bounded operators, giving \(DD^*=\rho(B)\).
The faithful right representation is isometric, so \(\|D\|^2=\|DD^*\|=\|\rho(B)\|=\|B\|\).

The polynomial identity \(D_0(X_jp)-X_jD_0p=\delta_{ij}\tau(p)\Omega\) has the claimed rank-one projection and sign.
Since the generators and D are bounded, it extends from A to H, and \(D\Omega=0\) is preserved.
The construction applies coordinate by coordinate under the stated hypotheses, so the simultaneous conclusion needs no cross-coordinate derivative bounds.
Under the bounded spatial-tensor hypothesis the Hilbert partial trace agrees with the normal bounded partial trace, whose contractivity gives the square-root bound.
There is no hidden dimension restriction or smallness assumption.

### Optional second conjugate comparison

The polynomial adjoint formula in the other tensor leg is \(\partial^*(1\otimes\xi_n)=\xi\xi_n-(\tau\otimes\mathrm{id})\partial\xi_n\).
Under the comparison's additional assumption \(\xi\in M\), left multiplication by \(\xi\) is continuous on H, while the partial trace is continuous on the derivative graph limits.
Closedness of \(\partial^*\) proves \(1\otimes\xi\in\operatorname{Dom}\partial^*\) and the stated formula.
Both \(\xi^2\) and the bounded spatial partial trace belong to M, giving boundedness of this second conjugate variable.
Its identification with the second conjugate moment functional follows by pairing against \(\partial p\), applying conjugacy on the second factor and the same coassociativity contraction.
This comparison uses \(\tau\otimes\mathrm{id}\), whereas the bounded-dual proof uses \(\mathrm{id}\otimes\tau\); the comparison is not a premise of that proof.

## Source and scope limits

The [MS23-U005 main-theorem passage](../literature/MS23/Yin_U005.md#theorem-11-and-the-complete-internal-chain) was checked as a contextual application interface: it records bounded conjugates with closed bounded derivatives for every finite \(d\geq1\) and \(-1<q<1\).
No q-Gaussian construction or MS23 original proof is re-audited here, and no vacuum-functional estimate substitutes for the bounded-derivative hypothesis.
The degree-weighted C_F0023 argument is comparison-only and is not used as a premise.
The candidate correctly retains the exact theorem as an additional project deduction rather than attributing it verbatim to Dab10.
No new primary-source inspection or novelty/priority search was performed.
The cited foundational source interfaces suffice for this local theorem at the retained inspection depths stated above.
No rational-L2 boundedness conclusion, scalar bounded-division-closure equality, Task completion or manuscript-wide conclusion is covered.

## Whole-candidate finding

No mathematical gap was found in the complete Statement or Argument of the specified C_F0092_v1 candidate.
The proof supports boundedness of the actual Hilbert-space closure, \(B_i\geq0\), \(D_iD_i^*=\rho(B_i)\), the exact norm identity and the stated simultaneous and Lipschitz specializations under exactly its hypotheses.
The optional second-conjugate comparison is valid under its additional boundedness assumptions.
This is an actual whole-candidate `self-reviewed` finding with the context exposure disclosed above.
It supplies evidence for an explicit Claim decision if selected; it makes no Claim assessment or maintenance acceptance decision itself.
