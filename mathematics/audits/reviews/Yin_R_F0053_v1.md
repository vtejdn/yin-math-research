---
author: Yin
---
# Review of the arcsine liberation-dual counterexample

Date and human record author: 2026-10-18T11:11, Yin.
The mathematical inspection was performed by a separately assigned agent who did not author either retained proof.
The review was not blind: its context included the original Chebyshev discussion and the information that another checking agent had contributed the shorter monomial proof.
The reviewer read the newly fixed C_F0080 v1, independently recomputed both arguments, and checked the linked definition interfaces; no prior acceptance review was relied on.
This is an initial complete-proof review of the counterexample, not a review of a larger rationality theorem or the original source proofs.

## Current relationship clarification

The recorded initial context included the original Chebyshev mathematical discussion for this same counterexample.
That is substantive proof-development context beyond the fixed Claim and its definition inputs, so the single whole-proof finding has a self relationship under the current context rule.
The shorter monomial proof was contributed by another checking agent; that contribution is separately disclosed as development, and no new independent coverage is inferred from recomputing it within the same whole-proof finding.
The original dated independent wording, mathematical calculations and exact bindings remain historical and unchanged.
No reviewer-supplied repair or new mathematical inspection is asserted here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [C_F0080 v1 Statement](../../claims/Yin_C_F0080_v1.md#statement) | Tracial multiplication model, generation, nonatomic normal law, regular scalar shifts, normalized liberation dual, and absence of a conjugate variable. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0080 v1 Argument](../../claims/Yin_C_F0080_v1.md#argument) | Complete operator construction, monomial obstruction and original Chebyshev argument, including all moment and convergence steps. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0080 v1 Definitions and provenance](../../claims/Yin_C_F0080_v1.md#definitions-and-provenance) | Compared common-domain, commutator, local sum normalization and actual vacuum-adjoint conditions. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0079 v4 definition](../../claims/Yin_C_F0079_v4.md#liberation-dual-system) | Generator-first commutators and common domains only; no theorem or normalization construction is invoked. |
| [Whole-proof finding](#whole-proof-finding) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Definition interface only: starred polynomial derivations, outer bimodule structure and actual vacuum-adjoint domain. |

## Whole-proof finding

The statement and both complete arguments are mathematically valid.

The substitution x=cos(theta) proves that mu is a probability measure and gives the stated moments.
Integration on L-infinity(mu) is a faithful normal tracial state.
The coordinate function is bounded and selfadjoint, its Borel functional calculus generates M, and its law is nonatomic.
Multiplication by x-lambda and its adjoint have zero kernels for every complex lambda, including the endpoint shifts.
The range is dense because its orthogonal complement is the adjoint kernel.
Thus all scalar shifts are regular.

The bounded selfadjoint operator P_Omega has full operator and adjoint domains.
For d=1 the commutator and sum-to-P_Omega normalization are immediate.
C_F0079 v4 supplies only the cited commutator/domain definition; its separate vacuum-annihilating normalization is not the local normalization of C_F0080.
The latter explicitly defines normalization by sum_i L_i=P_Omega, so no requirement L Omega=0 is imported.

Since X is selfadjoint, the starred polynomial algebra is C[X], dense in H.
Polynomial evaluation is injective because a nonzero polynomial has only finitely many real zeros and mu has no atoms.
The product rule with partial X=1 tensor 1 uniquely gives the stated power formula.
The proof therefore excludes every derivation allowed by the condition, not merely a chosen realization.
Membership of the vacuum tensor in the adjoint domain would make its pairing with partial bounded in the H norm, exactly the continuity contradicted below.

For the monomial argument, the even moments are 4^(-r) binom(2r,r), and the odd moments vanish.
Squaring their binomial series gives sum_(r=0)^n m_(2r)m_(2(n-r))=1.
Exactly the even-indexed terms of the product-rule sum for X^(2n+1) survive under the product trace.
Its vacuum pairing therefore equals one for every n.
Dominated convergence gives norm_2(X^(2n+1))->0 because |x|<1 almost everywhere and |x|^(4n+2)<=1.
The adjoint identity and Cauchy-Schwarz now contradict that constant pairing.
No closability or auxiliary comparison theorem is assumed.

For the Chebyshev argument, direct algebra verifies the generating function and its divided difference.
The geometric Fourier expansion gives the stated integral of the reciprocal denominator for |z|<1.
Multiplying the two scalar integrals yields ell(G_z)=z/(1-z^2).
The divided difference of T_n is bounded by sup|T_n'|<=n^2, including on the diagonal by continuation.
The series of divided differences consequently converges uniformly and absolutely in both real variables on every compact subdisk in z.
This justifies termwise integration and coefficient comparison.
Fourier orthogonality gives pairwise orthogonality and squared norms 1/2 for the nonconstant polynomials.
Both ell(p_N)=N and norm_2(p_N)=sqrt(N/2), and the resulting second adjoint-domain contradiction, are correct.

## Dependencies and limits

Only elementary multiplication-operator spectral facts, polynomial density, binomial and geometric series, Fourier orthogonality, dominated convergence and the Hilbert-space adjoint criterion are used.
The mutable exploration draft is provenance rather than logical support, and there is no circular reliance on a conjugate-variable existence theorem.
The definition interfaces were checked from the fixed local records.
Original ACSY24 or Voiculescu proofs, historical priority and literature-wide attribution were not re-audited.
The conversational comparison with liberation gradients is not a premise and is not certified by this finding.
No numerical computation or formal verification is relied on.
The example disproves the general converse with one selfadjoint generator and makes no extra assertion for each prescribed tuple length greater than one.
The finding supports adoption of C_F0080 v1 as proved and independently reviewed within this scope; the Claim decision owns that adoption.
