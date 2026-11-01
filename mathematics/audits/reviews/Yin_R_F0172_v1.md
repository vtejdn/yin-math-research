---
author: Yin
---
# Independent review of the arcsine ordinary-dual obstruction and liberation finite-rank test

Date and human record author: 2026-10-18T11:46, Yin.
The reviewer was separately assigned after C_F0163 v1 was fixed and did not write or modify that Claim.
The review was not blind: the shared root conversation included the proposed counterexample and its informal consequences.
The reviewer read the complete fixed Claim, C_F0080 v1 and its R_F0053 review, then independently checked the power-commutator identity, actual domains, vacuum pairing, rank calculation and division-closure argument.
R_F0053 was consulted as prior review of the direct dependency, not as an earlier review of C_F0163.
This is a whole-proof mathematical review of C_F0163 v1 at its decision-initial, not a manuscript review or completion review of the wider conjugate-variable comparison Task.

## Current relationship clarification

The recorded shared root context included the proposed counterexample and its informal mathematical consequences before this fixed Claim was reviewed.
This is known substantive development context for the ordinary-dual obstruction and liberation finite-rank comparison, so the single whole-proof finding has a self relationship under the current context rule.
Its direct dependency C_F0080 and the earlier R_F0053 finding remain at their actual recorded scopes; their prior independent wording does not supply isolated coverage for this deduction.
The original dated independent wording and complete mathematical finding remain historical, and no new review or reviewer-supplied repair is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [C_F0163 v1 initial decision](../../claims/Yin_C_F0163_v1.md#decision-initial) | Exact reviewed initial candidate, its complete selected statement and argument, and its sole declared project dependency. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0163 v1 Statement](../../claims/Yin_C_F0163_v1.md#statement) | Normal nonatomic arcsine generator, normalized liberation dual, absence of every ordinary dual with the stated common domains, universal rank bound and nonrational projection. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0163 v1 Argument](../../claims/Yin_C_F0163_v1.md#argument) | All four proof sections, including the polynomial-core strengthening, domains, signs, fraction quantifiers and equality of division closure with C(X). |
| [Whole-proof finding](#whole-proof-finding) | [C_F0080 v1 Statement](../../claims/Yin_C_F0080_v1.md#statement) | The unchanged multiplication model, normal nonatomic generation, regular scalar shifts and the bounded normalized liberation dual. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0080 v1 Argument](../../claims/Yin_C_F0080_v1.md#argument) | Only the operator construction, monomial arcsine moments, their convolution and L2 convergence used by C_F0163; the alternative Chebyshev proof is not needed here. |
| [Whole-proof finding](#whole-proof-finding) | [C_F0080 accepted decision](../../claims/Yin_C_F0080_v1.md#decision-accepted-counterexample) | The existing acceptance and recorded review scope of the direct project input. |

## Whole-proof finding

The complete statement and argument are mathematically valid, with no unresolved dependency or proof gap.
They support adoption of C_F0163 v1 as proved and independently reviewed; the Claim decision owns adoption.

The dependency has exactly the same probability measure, multiplication representation, vacuum and commutator convention as the new Claim.
The coordinate function generates L-infinity(mu), and nonatomicity makes every scalar shift and its adjoint injective, hence the shift has dense range.
The operator P_Omega is bounded and selfadjoint on H.
The explicitly stated one-variable normalization L=P_Omega is satisfied; no vacuum-annihilating alternative normalization is imported.
The binomial moment series gives the convolution equal to one, and dominated convergence gives norm_2(X^(2n+1) Omega) tending to zero.
These input facts were inspected directly as well as compared with their prior review.

For the ordinary-dual contradiction, M Omega is invariant under multiplication by X and contains every X^k Omega.
Thus each application of [X,D]=P_Omega in the telescoping identity acts on a vector in Dom D.
The leftmost multiplication powers are bounded operators, so D Omega need not lie in an invariant domain of D.
No unasserted composition involving D twice occurs.
Expanding X^k D-D X^k cancels successive terms with the positive sign prescribed by [X,D]=P_Omega.
For odd k the vacuum pairing is the sum of products of even moments and is exactly one.

With the inner product linear in the second entry, selfadjointness of X gives
\[
 \langle\Omega,X^kD\Omega\rangle
 =\langle X^k\Omega,D\Omega\rangle,
 \qquad
 \langle\Omega,DX^k\Omega\rangle
 =\langle D^*\Omega,X^k\Omega\rangle.
\]
The first identity requires only D Omega in H; the second uses exactly Omega in Dom D* and X^k Omega in Dom D.
Cauchy--Schwarz yields the stated vanishing upper bound and contradicts the constant one.
The proof therefore excludes every D in the stated class, and in fact proves the claimed polynomial-core strengthening.
It does not infer nonexistence merely from failure of one canonical operator.

For every fraction pair, all coefficients and P_Omega are bounded on H, so the natural domain of both products is all H.
Since P_Omega xi=Omega times <Omega,xi>, the displayed range is contained in the span of s Omega and a Omega, of dimension at most two.
The operator is bounded and equals its Hilbert-space closure.
The calculation is independent of u and of the fraction identities, so it covers every u and every fraction pair, including zero coefficients and coinciding range vectors.

A nonzero polynomial has only finitely many zeros, all mu-null.
It is therefore regular in L0(M), and its reciprocal defines the asserted embedded rational-function field.
Every nonzero element of that field has its inverse in the same field, so it is division closed.
Conversely division closure must contain inverses of every nonzero polynomial, which proves the equality with C(X) in both directions.
The projection 1_(0,1)(X) has trace one half by symmetry and has neither value zero nor value one as an element of M.
The elementary field identity e(e-1)=0 therefore excludes it from C(X).
The unit-denominator pair (1,p,p,1) is admissible and gives [P_Omega,p]; the universal range argument also covers every other pair for p.
This proves failure of the proposed finite-rank characterization even with the universal fraction quantifier.

## Dependencies and limits

The only project mathematical dependency is the inspected scope of C_F0080 v1.
No ordinary-dual-to-conjugate-variable theorem, maximal-Delta theorem, manuscript theorem, numerical calculation or formal verification is used.
The other steps are elementary adjoint identities, finite-rank range bounds and rational-function field algebra, reproduced in the Claim and checked above.
No outstanding source-completeness obligation was identified for this local deduction; historical priority and a literature-wide novelty search were not undertaken.
The example does not contradict a rationality theorem requiring an ordinary dual, since its ordinary-dual hypothesis fails.
It does not refute the stronger condition of membership in a finite-rank commutator image, and it does not decide conjugate-variable versus ordinary-dual existence for general normal or nonnormal tuples.
