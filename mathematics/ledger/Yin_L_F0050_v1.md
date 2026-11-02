---
author: Yin
---
# ACSY24 Proposition 3.5 and full-domain duals: equivalence classes and remaining questions

Date: 2026-10-14T11:18.
Human author Yin.
Root's comparison under the user's explicit continuation request.
The new arguments are retained in [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement); the counterexample tests are retained in [L_F0049](Yin_L_F0049_v1.md).
This advances the comparison in [L_F0048](Yin_L_F0048_v1.md) without rewriting earlier fixed findings.

## Exact hypotheses being compared

The complete new fixed proof has been adopted as [proved](../claims/Yin_C_F0071_v2.md#decision-reviewed), with the C_F0071 conclusion in R_F0044 declared self-reviewed.
[R_F0044](../audits/reviews/Yin_R_F0044_v1.md#conclusion) records the complementary review arrangement; its separate [source finding](../audits/reviews/Yin_R_F0044_v1.md#acsy-no-normality) and [failed-test finding](../audits/reviews/Yin_R_F0134_v1.md#failed-test-conclusion) cover those respective inputs.
The comparison below remains a root synthesis, not a claim that the general implications have been resolved.

Let M=W*(X_1,...,X_d) be finite tracial with faithful normal tracial state, H=L2(M), Omega=1, P=P_Omega, and A=C<X,X*>.

- F(X): there exist complex-linear maps D_i:M Omega -> H satisfying [X_j,D_i]=delta_ij P on all M Omega.
  No continuity, closability or adjoint-domain premise is included.
  The maximal-Delta implication at this scope is proved by the [argument in C_F0024 Section 3](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors).
- A(X): there exist outer-bimodule derivations partial_i:A -> H tensor_2 H satisfying partial_i X_j=delta_ij 1 tensor 1 and 1 tensor 1 in Dom partial_i*.
  This is the complete premise of ACSY24 Proposition 3.5.

Both conditions imply Delta(X)=d.
Comparing their hypotheses requires deciding F(X) implies A(X) and A(X) implies F(X) separately.
An unresolved implication is not a proved nonimplication.

## The source has been audited without normality

[ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), especially Sections 3 and 6, already contains a separately checked reconstruction of the source's abbreviated final step.
During this continuation the published 73-page artifact, pp.34--36, and the full reconstruction were rechecked.
The proof does not assume normality or reality.

The starred core supplies both [E_0,a] and [E_0,a*] as Hilbert-Schmidt operators and the actual core adjoint.
Graph approximation and adjoint pairing establish domain invariance for the closure E and E*.
The selfadjoint block S=[[0,E*],[E,0]] therefore has a bounded Hilbert-Schmidt commutator with diag(X_j,X_j), even if X_j is nonnormal.
Resolvent regularization gives bounded E_t=E(1+tE*E)^-1 with [E_t,X_j] tending to delta_ij P in Hilbert-Schmidt norm.
The finite-rank cycle trace calculation then proves maximal Delta.

The original phrase about affiliated operators on p.36 is not used to infer affiliation with M or an all-M domain.
In particular a normalized canonical E with E Omega=0 cannot be affiliated with M and still satisfy its nonzero dual commutator: affiliation would make it commute on its domain with M', killing the dense subspace M' Omega.
The repository reconstruction supplies the needed justification without that inference.
The audit covers the local proof and its accepted foundations; it is not formal verification or an external human review.

## New equivalence results

The current selected assessment and complete proof are owned by [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement).
They give:

| Class of generating tuple | F(X) implies A(X) | A(X) implies F(X) |
| --- | --- | --- |
| Any finite selfadjoint tuple, without freeness | Yes | Yes |
| Any finite tuple with each coordinate selfadjoint or unitary, without freeness | Yes | Yes |
| A single arbitrary normal generator | Yes | Yes |
| Invertible complex affine changes X=B S+b of selfadjoint generating tuples S | Yes | Yes |
| Arbitrary correlated normal tuples | Not resolved generally | Not resolved generally |
| Arbitrary bounded generating tuples | Not resolved generally | Not resolved generally |

The new real-derivation input is stronger than the former scalar argument.
If delta is real on a dense starred core and E=(id tensor tau)delta is bounded from the operator norm into H, then the actual vacuum exists and its norm is at most 2 sqrt2 ||E||.
Neither coassociativity nor closability is a premise of this converse.
Its complete spectral-partition proof belongs to C_F0071, not this comparison.

For selfadjoint tuples, C_F0069 supplies automatic boundedness of normalized full-domain duals and the induced derivations are real.
The converse just described therefore gives joint conjugates, not merely marginal conjugates.
Dab10 supplies the opposite implication.

For scalar normal generators, symmetry of the scalar divided-difference kernel makes its two contractions equal; the same partition argument gives the vacuum with sufficient bound 4||E||.
C_F0055 supplies the reverse after the exact diffuse divided-difference identification.

For a unitary coordinate, a one-tensor twist makes the derivation real, with a contraction explicitly expressed through the already bounded E.
An exact Leibniz vacuum identity untwists it.
The mixed reverse is proved coordinatewise in C_F0071 using a real derivation whose coassociativity defect is zero for a selfadjoint coordinate and i kappa delta for a unitary coordinate, followed by the C_F0043 norm calculation and original-closure graph argument.
This does not claim that Dab10's printed theorem already states the mixed result.

These findings supersede the earlier statement that only the single-selfadjoint or marginal converse had been proved.
They do not supersede the remaining arbitrary correlated-normal questions.

## Counterexample tests and the common conclusion

[L_F0049](Yin_L_F0049_v1.md) excludes two concrete nonnormal candidates:

1. X=(h,hS), with h positive regular and h^-1 not in L2.
   The actual starred relation Yh=hY* forces partial_Y(Y*)=h^-1 tensor h, violating the Hilbert-valued derivation premise.
   The full-domain commutator also forces h^-1 in L2.
2. x=s I+e12 in M2(L-infinity(0,1)).
   The starred relations force a non-square-integrable divided-difference tensor.
   Independently, the full-domain commutator would produce a bounded G:L-infinity -> L2 with [[G,s],s]=P0/2; spectral pinching contradicts this.
   The automatic boundedness and exact pinching proof are retained in the linked record.

Neither is a separating counterexample: both A(X) and F(X) fail.

The Jordan example does have Delta(x)=1.
For every complex lambda the fiber x(s)-lambda is invertible for almost every s, so left multiplication by x on H has no eigenvectors.
If a nonzero finite-rank T commuted with x, its finite-dimensional nonzero range would be x-invariant and have an eigenvector, a contradiction.
The [MSY23 finite-cycle characterization](../audits/literature/MSY23/Yin_U002.md#msy23-u002) therefore gives maximal Delta.
Thus the common conclusion alone implies neither hypothesis, even for one nonnormal generator.
This last observation is a direct specialization of the checked characterization and was separately checked by the audit agent.

## Exact remaining normal questions

[C_F0070](../claims/Yin_C_F0070_v1.md#statement) continues to give the sharp interfaces outside the positive classes.

Starting from F(X) for a normal tuple, unique starred derivations delta_i and bounded canonical contractions on the core already exist.
The remaining target is the joint estimate
\[
 |(\tau\otimes\tau)(\delta_i p)|\le C_i\|p\|_2
 \qquad(p\in A).
\]
The new real-derivation lemma cannot simply be applied because delta_i is not generally real.

Starting from A(X) for a normal tuple, put E_i0=(id tensor tau)partial_i on A Omega.
C_F0070 proves
\[
 F(X)\quad\Longleftrightarrow\quad
 M\Omega\subseteq\operatorname{Dom}\overline{E_{i,0}}\quad\text{for every }i.
\]
The latter is equivalent to a uniform operator-norm-to-H bound on each canonical core contraction, by closed graph in one direction and Kaplansky plus weak closed graph in the other.
Seeking another full-domain algebraic dual does not evade this obligation.

The unitary proof suggests realifying a general normal derivation by a marginal spectral phase.
A merely bounded measurable tensor twist does not yet give either a uniform contraction bound or an inverse-twist actual adjoint-domain statement.
ACSY24's algebraic-tensor adjoint interface cannot be silently extended to all bounded measurable coefficients.
This is a possible next route with two explicit analytic gaps, not a further proved implication.

## Source search and retained scope

The bounded reuse search checked C_F0045, C_F0069, C_F0070, C_F0043, C_F0055, ACSY24-U001, Dab10-U002 and Shl06-U001, then primary-source searches concerning bounded contractions, dual systems and conjugate-variable converses.
The selected source statement of Mai's [Regularity of distributions of Wigner integrals, Theorem 4.9](https://arxiv.org/pdf/1512.07593#page=26) was read again: it assumes reality, algebraic coassociativity and the actual vacuum, and yields contraction bounds.
It does not state the new reverse implication.
Shl06 and the inspected MS23 dual-system definitions retain an explicit vacuum-adjoint premise.
No exact published statement of the new converse was verified in this bounded search; no novelty or exhaustive absence claim follows.

The principal unfinished question remains whether A(X) and F(X) agree for arbitrary correlated normal tuples or arbitrary bounded tuples.
No separating example or general resolution is claimed.
