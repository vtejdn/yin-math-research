---
author: Yin
---

# Normal liberation equivalence and nonnormal obstruction: whole-proof self-review

Date: 2026-10-28T11:11.
Human record author: Yin.
This is a whole-proof authoring-agent self-review of [C_F0083 v2](../../claims/Yin_C_F0083_v2.md).
The reviewer developed the argument and had the preceding mathematical discussion, source-interface summaries and earlier conclusions in context.
It is not an independent review.
During the authoring check, the reviewer identified the need to replace the common algebra in the open v1 candidate by the individual cores \(\mathcal P_i=\operatorname{Alg}(A_i,B_i)\).
The corrected v2 statement and complete argument were then reread and checked, with the normal extension, actual adjoint test, sign conversion and counterexample checked at that full-core scope.
The old v1 candidate remains open and is not an accepted proof input.

The directly consulted source units are those in the bindings below.
Their statements and application hypotheses are accepted at their own retained inspection depths.
The current C_F0082 statement and selected decision supply the unchanged forward implication; its energy proof and earlier reviews are not reclassified as a review of this new converse.
The C_F0074 circular model was consulted as construction provenance.
No source-proof audit or formal verification beyond the retained interfaces is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole comparison](#whole-comparison) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole comparison](#whole-comparison) | [Statement](../../claims/Yin_C_F0083_v2.md#statement) | Every normal-equivalence condition, arbitrary ambient algebra, actual conjugate-vector and gradient formulas, information bound, and bounded nonnormal counterexample. |
| [Whole comparison](#whole-comparison) | [Argument](../../claims/Yin_C_F0083_v2.md#argument) | Full normal algebra-level extension, individual-core relation descent, actual Hilbert adjoint, accepted forward implication, explicit Fock operators and incompatible gradient moments. |
| [Whole comparison](#whole-comparison) | [Conventions](../../claims/Yin_C_F0083_v2.md#definitions-and-conventions) | L1 versus L2 gradients, actual adjoint definition of the local liberation-conjugate terminology, signs, realification and the distinct bounded-vector dual-system definition. |
| [Whole comparison](#whole-comparison) | [Forward implication](../../claims/Yin_C_F0082_v1.md#decision-self-reviewed) | Accepted finite-information construction of closed normalized duals with both bounded-vector domains, including the ambient extension, at its unchanged self-reviewed scope. |
| [Whole comparison](#whole-comparison) | [Bounded-map Fuglede input](../literature/CS77/Yin_U001_v1.md#cs77-u001) | Proposition 1's checked specialization on B(M-infinity,H), with normality and isometric unitary multiplication; no H-bounded extension is assumed. |
| [Whole comparison](#whole-comparison) | [Kaplansky density](../literature/AP18/Yin_U001_v1.md#ap18-u001) | Uniformly bounded strong approximation within each generated algebra, accepted at statement-and-applicability depth. |
| [Whole comparison](#whole-comparison) | [Gradient interface](../literature/Voi99/Yin_U003_v1.md#voi99-u003) | Actual represented liberation derivation, consistent word moments, anti-reality, skewadjointness and the minus sign in Proposition 6.1. |
| [Whole comparison](#whole-comparison) | [Information convention](../literature/Voi99/Yin_U004_v1.md#voi99-u004) | Definition 9.1 for a finite coordinate family; the semicolon convention and infinite value for absent or non-L2 gradients. |
| [Whole comparison](#whole-comparison) | [Tensor realization](../literature/Voi98/Yin_U005_v1.md#voi98-u005) | Only the tracial rank-one/Hilbert-Schmidt identification supplying injectivity for the evaluated algebraic tensors. |
| [Whole comparison](#whole-comparison) | [Fock input](../literature/Miy22/Yin_U001_v1.md#miy22-u001) | Full Fock creation and annihilation, the faithful tracial L2 representation and variance-one free semicircular normalization; earlier textbook-proof limits remain. |
| [Whole comparison](#whole-comparison) | [Bounded source comparison](../literature/Voi99/Yin_U001_v1.md#voi99-u001) | Definition 13.1 and Proposition 13.3 at their bounded selfadjoint algebra-level scope, without claiming a converse bounded implementation theorem. |
| [Whole comparison](#whole-comparison) | [Ordinary conjugate-variable comparison](../../claims/Yin_C_F0080_v1.md#decision-accepted-counterexample) | The existing accepted arcsine example is used only to distinguish ordinary conjugate variables; the one-coordinate liberation gradient is checked directly as zero. |

## Domain and proof checks

The statement uses \(L^2\) liberation gradients and actual vacuum-adjoint vectors, rather than merely \(L^1\) gradients.
The explicit terminology \(\xi_i=\gamma_i^*(1\otimes1)\) is a local convention and is not attributed to Voi99 as a universal naming choice.
The anti-real signs give \(\xi_i=-j_i\), while the scalar adjoint rule for \(\delta_i=\mathrm i\gamma_i\) gives \(\eta_i=-\mathrm i\xi_i=\mathrm i j_i\).
These conversions preserve existence and squared norms.

Restriction of \(L_i\) to \(M\Omega\) is closable because the original adjoint contains the dense subspace \(M\Omega\).
The same holds after subtracting \(P_\Omega\).
A convergent sequence in the graph of the map \(M_\infty\to H\) lies in the actual Hilbert closure, and its limit input already lies in \(M\Omega\).
This proves the Banach closed graph assertion used to apply the bounded-map Fuglede input.
No operator-norm-to-L2 bound is silently treated as a Hilbert-space bound.

For each \(i\), Fuglede is applied to \(L_i-P_\Omega\) at \(X_i\), and to \(L_i\) at all other normal coordinates.
The resulting star-algebra commutation extends to the full \(A_i\) and \(B_i\) through bounded strong approximants and the Hilbert closed graph.
For a fixed bounded vector, both sides of each intertwining identity converge strongly.
This supplies the full relations before any liberation derivation is invoked.

The correction from v1 is necessary for the recorded proof scope.
The von Neumann algebra \(B_i\) need not be contained in the common algebra generated algebraically by the \(A_j\).
Version v2 instead defines the \(i\)-th formal derivation on \(A_i*_{\mathbb C}B_i\).
The commutator identity is tested on every formal element there and descends by injectivity of the finite-rank tensor representation.
Its actual domain is all of \(\mathcal P_i\Omega\), dense in \(H_N\).
Consequently the adjoint pairing tests every vector required by the \(A_i:B_i\) definition.

For \(h_i=L_i\Omega\) and \(k_i=L_i^*\Omega\), the first-variable-linear pairing was checked explicitly:
\[
 \langle[p,L_i]\Omega,\Omega\rangle
 =\tau(ph_i)-\langle p\Omega,k_i\rangle
 =\langle p\Omega,Jh_i-k_i\rangle.
\]
Projection to \(H_N\) leaves this equality unchanged for \(p\in\mathcal P_i\).
The final vector bounds the functional in the L2 norm of \(p\), establishing membership in the actual adjoint domain.
The argument uses the original \(L_i^*\Omega\), not a formal adjoint or an unspecified extension.
Anti-reality then makes the obtained vector skewadjoint and identifies its negative with the source gradient.
The projection and triangle inequalities give the stated information bound.
As a sign check, when \(M=N\) and \(L_i\) is bounded selfadjoint, the formula reduces to \((L_i-JL_iJ)\Omega\), as in Voi99 Proposition 13.3.

The unchanged C_F0082 implication gives closed normalized choices from finite coordinate information.
All its local hypotheses are matched; neither generation of \(M\) nor regularity of shifts is inserted into the converse.
The implication cycle contains no dependency on the new claim through its forward input.

## Counterexample and comparison checks

On the full Fock word basis, \([r_k^*,S_j]=\delta_{kj}P_\Omega\).
The two complex combinations in the proof give all four identities \([X_j,D_i]=\delta_{ij}P_\Omega\), with positive generator-first sign.
The vacuum computation of \(c^*c-cc^*\) proves nonnormality.
The right multipliers are bounded and commute with the left action; traciality gives the sign \([\rho(x),P_\Omega]=[x,P_\Omega]\).
Jacobi therefore gives the required liberation commutators for \(K_i=[\rho(X_i),D_i]\).
Their residual sum \(R=K_1+K_2-P_\Omega\) commutes with both generators, so subtracting \(R/2\) preserves the relations and gives sum normalization.
Every operator and adjoint has domain all of \(H\), since each constructed operator is bounded.

Both individual generated von Neumann algebras equal \(M\).
For the centered variance-one \(a=S_1\), the two formal descriptions of \(a^2\) force the same gradient pairing to be both zero and minus one.
This contradicts even an L1 gradient and does not presume that an inconsistent formal derivation already exists on the represented algebra.
It proves precisely the claimed failure of the nonnormal converse.

The source's bounded selfadjoint category retains its full algebra commutation requirements.
The counterexample meets the generator-domain definition and does not supply such an algebra-level system.
The fixed ordinary-conjugate-variable example is a comparison, and does not refute the normal equivalence for liberation gradients.
The scalar-relative one-coordinate gradient is zero for every marginal law by its trace formula.

## Whole comparison

The complete v2 statement, definitions, proof and comparison are supported at the accepted input scopes, with no remaining mathematical gap identified in this self-review.
This supports a proved assessment with the explicitly self-reviewed relationship.
It supplies no independent review of the generalized equivalence or counterexample, no formal verification and no theorem producing bounded selfadjoint implementations from finite information.
The earlier open candidate and all previous input reviews retain their exact versions and scopes.
