---
author: Yin
---

# Independent review of sum normalization and the full fraction-commutator criterion

Review act: 2026-11-01T06:27 UTC minute.
Human record author: Yin.
The reviewing agent was separately assigned after the fixed candidate was written, had no role in its substantive development, and received no proof-development conversation, mathematical summary, author explanation or previous project-review conclusion.
The initial findings were formed from the fixed statement, proof and necessary mathematical dependencies.
No earlier project R finding was consulted or adopted.

The object is the complete [v5 Statement](../../claims/Yin_C_F0079_v5.md#statement) and [v5 Argument](../../claims/Yin_C_F0079_v5.md#argument), read in the local working tree on the review date.
The selected candidate decision is [sum-normalization-candidate](../../claims/Yin_C_F0079_v5.md#decision-sum-normalization-candidate).
The necessary fixed inputs are the [v4 domain definition and three-condition statement](../../claims/Yin_C_F0079_v4.md#statement), its [algebraic, coordinate-separation, maximal-Delta, tensor-recovery and rationality arguments](../../claims/Yin_C_F0079_v4.md#argument), and [C_F0068 Part A](../../claims/Yin_C_F0068_v1.md#statement) at its stated arbitrary-bounded-tuple scope.
The [sum-normalization definition](../../claims/Yin_C_F0082_v1.md#sum-normalized-liberation-dual-system) was checked only as a definition; the finite-information theorem there is not an input to v5.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole v5 finding](#whole-v5-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole v5 finding](#whole-v5-finding) | [v5 Statement](../../claims/Yin_C_F0079_v5.md#statement) | Complete general replacement lemma, four conditions for every affiliated u and every sum-normalized system, full natural domains and fixed-pair uniqueness. |
| [Whole v5 finding](#whole-v5-finding) | [v5 Argument](../../claims/Yin_C_F0079_v5.md#argument) | Complete added proof, including common-domain correction, adjoint inclusions, full-domain closure, tensor signs, the implication cycle and normalization distinction. |
| [Whole v5 finding](#whole-v5-finding) | [v4 Statement](../../claims/Yin_C_F0079_v4.md#statement) | Necessary domain, regular-shift, maximal-Delta, tensor-recovery, three-condition and uniqueness interfaces; not a new review of every other v4 assertion. |
| [Whole v5 finding](#whole-v5-finding) | [v4 Argument](../../claims/Yin_C_F0079_v4.md#argument) | Necessary algebraic injectivity and recovery, coordinate separation, maximal-Delta proof, tensor-recovery proof and rationality argument; remaining examples and vacuum-normalization proof are outside this binding. |
| [Whole v5 finding](#whole-v5-finding) | [C_F0068 Part A](../../claims/Yin_C_F0068_v1.md#statement) | Accepted fixed maximal-Delta rationality interface without normality or ambient generation, including the printed certificate sign and its conversion; no renewed review of the complete source chain or Parts B and C. |
| [Whole v5 finding](#whole-v5-finding) | [Sum-normalization definition](../../claims/Yin_C_F0082_v1.md#sum-normalized-liberation-dual-system) | Only the definition equating the sum with P_Omega on M Omega, distinct from individual zero-vacuum conditions. |

## Whole v5 finding

No mathematical gap was found in the exact v5 statement and complete added argument, with the fixed retained inputs used at the scopes just stated.
The review checked the hypotheses and all quantified choices backward from the conclusion, then checked the construction and implication chain forward.
The decisive checks follow.

### General replacement and adjoint domains

The finite sum C is defined on M Omega, which every bounded left multiplier preserves.
Summing the generator commutators gives [X_j,C]=0 there, so subtracting C/d from every coordinate preserves every required generator relation and makes the sum P_Omega.
The displayed adjoint vector
\[
 L_i^*\eta-d^{-1}\sum_kL_k^*\eta+d^{-1}P_\Omega\eta
\]
exists in H for every bounded vector eta.
With the stated second-slot-linear inner product it represents the functional of the corrected operator on its entire domain M Omega, so that domain is contained in the adjoint domain.
Density therefore gives closability.
Each closure has exactly the same values on M Omega and the same adjoint there, so the asserted local relations and normalization survive.
This argument uses neither scalar-shift regularity nor an extension to the commutant, adjoint-generator identities, boundedness or equality of the original full domains.
The case d=1 is included.

### Full natural-domain closability

For every legal Q, bounded b and t send M Omega into M Omega, so the declared natural domain of Gamma contains this dense subspace.
For every eta in M Omega, both s*eta and a*eta are again bounded vectors in Dom L_i*.
The vector
\[
 b^*L_i^*(s^*\eta)-t^*L_i^*(a^*\eta)
\]
therefore represents the functional against Gamma on its full natural domain, not just on M Omega.
This proves dense adjoint domain and closability before rationality is assumed.
No assertion that M Omega is an original graph core is needed here.

### Necessary fixed tensor-recovery interface

The regularity of every X_i-lambda rules out nonzero finite-dimensional invariant subspaces for the relevant left and right multiplication maps on U.
The minimal finite tensor decomposition argument supplies the individual injectivity used in v4.
Because bounded multiplication preserves H, the two quotient-factor arguments also apply to its recovery from H-valued tensors.
The liberation relations used by the coordinate maps require only the stated generator commutators on M Omega.

In the v4 tensor-recovery proof, after finite denominator clearing, injectivity of the left clearing denominator makes Phi_i(h) finite rank on t M Omega.
That subspace is dense because t has dense range.
The restriction is closable, and a closable finite-rank operator has a bounded finite-rank closure on all H.
The closure of Phi_i(h) extends this everywhere-defined operator and hence equals it.
The bounded tensor action identities and cancellation of the regular denominators then give exactly
\[
 \overline{\Phi_i(h)}=\Theta(\Psi_i(\ell_i)),
 \qquad \ell_i\in H\otimes_{\mathbb C}H,
\]
for the particular tensors used in v5.
Thus v5 uses a conclusion actually proved by the retained argument, rather than merely the membership assertion in the v4 tensor-recovery statement.

### Rationality, signs and the full-domain conclusion

The v4 maximal-Delta conclusion applies to every chosen sum-normalized system because it requires only the original domain and generator conditions and scalar-shift regularity.
C_F0068 Part A supplies the rational tensors for A_X without adjoining generator adjoints and without assuming normality or M=W*(X).
Clearing them by any prescribed fraction Q gives
\[
 h=a\otimes t^{\mathrm{op}}-s\otimes b^{\mathrm{op}}
   =\sum_i\Psi_i(\ell_i).
\]
Opposite-factor multiplication gives the second factor X_i e in Psi_i(c tensor e^op).
Consequently
\[
 \Theta\Psi_i(k)=[\rho(X_i),\Theta(k)],
 \qquad
 \Phi_i(h)=aL_it-sL_ib=-\Gamma[Q,L_i]
 \quad\hbox{on }M\Omega.
\]
These identities fix both required minus signs.
Taking T_i=-Theta(ell_i) gives bounded finite-rank witnesses.

The full natural-domain Gamma is closable by the preceding separate check.
Its graph closure contains the graph of minus the bounded closure of Phi_i(h), which is already defined on all H.
An operator extending an everywhere-defined operator has no additional graph values, so the two closures are equal.
This justifies the full natural-domain assertion for the actual L_i, including systems with larger original domains.
The choice of Q and the choice of sum-normalized system were arbitrary.

### Reverse implication, quantifiers and uniqueness

Under condition 4, each bounded commutator restricts to Gamma on M Omega.
For xi there, both b xi and t xi are in M Omega, exactly where sum normalization is available.
Summing therefore yields sP_Omega b-aP_Omega t on that dense domain.
The finite sum of commutators and the certificate right-hand side are bounded, so the equality extends to all H without interchanging sums of unbounded closures.
Thus 4 implies 3.
Every affiliated u admits a legal bounded left and right fraction, so 3 implies 2.
The accepted v4 criterion supplies 2 implies 1 and the remaining equivalence of 1, 2 and 3.
Its sign conversion from C_F0068 Part A is the same simultaneous negation of witnesses checked above.
For fixed Q, every condition-4 tuple satisfies the certificate equation, and the v4 finite-rank-cycle uniqueness identifies it with the unique certificate tuple.
The argument includes zero, scalar and one-coordinate cases and introduces no extra nondegeneracy assumption.

The final distinction from zero-vacuum normalization is correct: evaluating sum normalization at Omega gives sum_i L_i Omega=Omega, so all coordinates cannot annihilate Omega.

## Inspection limits

The necessary v4 argument sections were read directly and their interfaces checked as above.
C_F0068 Part A and its already retained algebraic/free-field inputs were used at their fixed accepted scope.
The exact printed Part A statement and the rational-tensor and rank-one interfaces were inspected; this review does not repeat the complete free-field, tensor-equalizer or original external-source proof audits.
The relevant retained MSY23 finite-rank-cycle and CS05 rank-one action statements were read as mathematical interfaces; their source-inspection accounts were not adopted as a new project R verdict.
No original external document was newly inspected.
The definition from C_F0082 supplies no finite-information premise or proof step.

This finding is a mathematical proof review, not independent acceptance of local material maintenance, manuscript review, Task completion or a Claim assessment selection.
The candidate's open decision remains unchanged by this review.
