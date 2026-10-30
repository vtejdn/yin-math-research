---
author: Yin
---
# Independent review of the two-contraction vacuum and canonical-domain criterion

Review performed and recorded: 2026-10-14T13:24.
Human record author: Yin.
The root agent independently checked the complete fixed [C_F0072 v1](../../claims/Yin_C_F0072_v1.md), authored by the acsy_rationality_check agent.
This is an AI mathematical review, not personal human inspection or formal verification.

## Arrangement and inputs

The author supplied the developing argument in the shared comparison discussion.
Root checked its bilinear and adjoint formulas before registration and then read the entire fixed statement and proof after registration.
Thus this is a separately performed mathematical check with author explanations available, not a blind review.
Root did not develop the two-contraction partition proof.
The current review covers the entire fixed candidate dated 2026-10-14T13:21, its constants, both actual operator domains, and the two declared dependency interfaces.

The reviewed inputs C_F0071 v2 and C_F0070 v1 supply already accepted continuous-partition and canonical-graph mechanisms.
Their present uses were checked directly; the new argument is written in full.
Standard Hilbert-space weak compactness, actual adjoints, continuous functional calculus, tracial Cauchy-Schwarz and Kaplansky density are used at their ordinary scope.
No new external source, unverified source identification, or claim of mathematical priority is introduced.
No other result or broader implication is reviewed here.

## Current relationship clarification

The original dated independent wording remains the historical description.
The arrangement explicitly says the developing argument was supplied through shared comparison discussion and author explanations were available; root also checked developing bilinear and adjoint formulas before the fixed candidate.
This is known additional substantive proof-development context, so the current whole finding is self-reviewed even though root did not originate the two-contraction partition proof.
It is not a classification inferred merely from reading the fixed statement, proof or dependencies.
No independent-gap repair chain is recorded for this target.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0072 statement](../../claims/Yin_C_F0072_v1.md#statement) | Both parts under weak star-algebra density and the two finite norm bounds, without reality, coassociativity or closability assumptions. |
| [Conclusion](#conclusion) | [C_F0072 argument](../../claims/Yin_C_F0072_v1.md#argument) | Complete four-step proof, the actual adjoint formula, constants and both canonical graph-domain assertions. |
| [Conclusion](#conclusion) | [C_F0071 symmetric-form mechanism](../../claims/Yin_C_F0071_v2.md#symmetric-form-lemma) | Continuous square partitions with overlap two and the finite independent-sign Hilbert estimate; both contractions are checked separately here. |
| [Conclusion](#conclusion) | [C_F0070 canonical graph mechanism](../../claims/Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky approximation and weakly closed graph argument only; the present bounds and actual adjoint are proved before using that mechanism. |

## Bilinear identity and norm extensions

For an outer derivation, applying tau tensor tau to delta(ab) gives exactly

    phi(ab) = tau(F(a)b) + tau(a E(b)).

The order of the two contractions is correct.
Each product pairs a bounded element with an L2 vector, so traciality and Cauchy-Schwarz make it continuous in the operator norms of a,b under the stated hypotheses.
E,F and phi therefore extend uniquely to B, the norm closure of A, and the bilinear identity extends to B.
This does not assume any extension of delta to B and does not require phi to be Hermitian.

## The spectral-partition estimate

For a selfadjoint a in B the compact real spectrum admits a finite continuous square partition with supports of diameter at most epsilon and overlap at most two.
Functional calculus puts its functions in B, where the preceding norm extensions are available.
The selected support values lambda_j yield uniform approximation both of t by sum lambda_j h_j(t)^2 and of t squared by sum lambda_j squared h_j(t)^2.
Taking the trace gives the exact second limit in (6), including spectra with atoms or disconnected supports.

For every choice of signs the squared pointwise sum is at most twice sum h_j squared, hence at most two.
The finite sign average of the squared Hilbert norm is the sum of the squared output norms; cross terms cancel.
This proves both estimates in (7) with no factor depending on the number of partition functions.
The two estimates are independent and use no reality relation.

Applying the bilinear identity to h_j squared and two Cauchy-Schwarz inequalities gives sqrt(2)(C_E+C_F) times the weighted square norm.
The operator-norm limit is legal because phi is norm continuous.
For general p=a+i b, the trace of the commutator in p* p vanishes, so the sum of the L2 squares of a,b is the L2 square of p.
This proves the stated constant 2(C_E+C_F).
No Hermitian phase-rotation argument is silently used.

Weak density makes A Omega dense in H.
Thus the bound is precisely the Hilbert adjoint criterion at 1 tensor 1 for delta with domain A Omega, and its representing vector is unique.
The proof establishes an actual vector, not only a bounded functional in the operator norm.

## Actual adjoint and both canonical domains

With inner product linear in the second variable, the checked identity is

    <a, E_0 b> = phi(a* b) - tau(F(a*) b)
                 = <a xi - (F(a*))* , b>.

Multiplication a xi is legitimate in L2.
The tracial involution on F(a*) gives the displayed conjugation, so no adjoint-order or sign change is needed.
This identifies E_0* on the dense core A Omega, proves closability of E_0, and yields its adjoint norm bound with the constant ||xi||_2+C_F.
The proof does not assume that the left contraction is an adjoint or identify it with E using reality.

Kaplansky density for B, followed by norm approximation in A, supplies a net converging in L2 to any a in M with uniform norm at most ||a||+epsilon.
The two output nets are bounded by the two distinct estimates.
Their product is weakly relatively compact, so taking a common subnet is legitimate.
Each corresponding graph pair lies in one of two norm-closed linear graphs, both weakly closed.
Their limits therefore give membership in the specified closure and its actual adjoint.
Weak lower semicontinuity gives the two norm estimates, and the arbitrary epsilon can be removed.
Nothing asserts that the supplied maps have norm-continuous extensions to M before this graph step.

## Conclusion

The complete fixed statement and argument of C_F0072 v1 pass this independently performed review without a mathematical correction.
The review supports proved / independently reviewed for that exact version if selected by its responsible decision.

The result is sufficient for the actual vacuum and both canonical full domains under the TWO contraction bounds.
It does not prove that either bound follows from the other, does not establish those bounds from an arbitrary ACSY hypothesis, and does not settle the unrestricted comparison for correlated normal tuples.
In particular the bounded coarse-tensor spectral phase supplies no missing M-to-L2 norm estimate in this proof.
