---
author: Yin
---
# ACSY24 Proposition 3.5 and full-domain duals: equivalence classes and remaining questions

Date: 2026-10-14T12:14.
Human author Yin.
This revision incorporates the pulled fixed equivalence results, the new atomic counterexamples [C_F0128 v2](../claims/Yin_C_F0128_v2.md#statement), and the bounded-division-closure reverse candidate [C_F0129 v1](../claims/Yin_C_F0129_v1.md#statement), under the user's explicit instruction to fix the mathematical materials.
The earlier comparison [v1](Yin_L_F0050_v1.md), positive results [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement), and failed tests [L_F0049](Yin_L_F0049_v1.md) retain their separate scope and assessments.

## Exact hypotheses being compared

The complete new fixed proof has been adopted as [proved and independently reviewed](../claims/Yin_C_F0071_v2.md#decision-reviewed).
[R_F0134](../audits/reviews/Yin_R_F0044_v1.md#conclusion) records the complementary review arrangement; its separate [source finding](../audits/reviews/Yin_R_F0044_v1.md#acsy-no-normality) and [failed-test finding](../audits/reviews/Yin_R_F0134_v1.md#failed-test-conclusion) cover those respective inputs.
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

## Four small-domain hypotheses

Write the source hypothesis as \(\mathsf A(X)\), to distinguish it from the represented algebra \(\mathcal A=\mathbb C\langle X,X^*\rangle\).
Throughout this comparison \(M=W^*(X)\), so \(\mathcal A\Omega\) is dense in \(H\).
Every condition below requires complex-linear operators, \(D_i\Omega=0\), and \([X_j,D_i]=\delta_{ij}P\) on the stated common domain.

| Condition | Common domain | Additional requirement for every i |
| --- | --- | --- |
| \(Q_{13}\) | \(\mathcal A\Omega\) | \(\Omega\in\operatorname{Dom}D_i^*\) |
| \(Q_{14}\) | \(\mathcal A\Omega\) | \(D_i\) is closable |
| \(Q_{23}\) | Some dense \(X_j\)-invariant linear subspace \(E\subseteq H\) containing \(\Omega\) | \(\Omega\in\operatorname{Dom}D_i^*\) |
| \(Q_{24}\) | Such a common subspace \(E\) | \(D_i\) is closable |

The domain in the last two rows is not assumed invariant under \(X_j^*\), nor assumed to contain \(\mathcal A\Omega\).
Invariance under each \(X_j\) is the condition making the stated commutator meaningful on all of \(E\).
The four assertions are existential: changing the operators is allowed.

The exact [ACSY24 Theorem 3.4 construction and actual adjoint formula](../audits/literature/ACSY24/Yin_U001.md#2-theorem-34-construction-and-adjoint) give
\[
 \mathsf A(X)\ \Longrightarrow\ Q_{13}\land Q_{14}.
\]
Indeed, for the source derivations take \(E_{i,0}=(\mathrm{id}\otimes\tau)\partial_i\) and \(D_{i,0}=-E_{i,0}\) on \(\mathcal A\Omega\).
The source proves normalization, the generator relation, and \(\mathcal A\Omega\subseteq\operatorname{Dom}E_{i,0}^*\); hence both vacuum membership and closability hold for this actual core operator.
In addition \(Q_{13}\Rightarrow Q_{23}\) and \(Q_{14}\Rightarrow Q_{24}\), by taking \(E=\mathcal A\Omega\).
Thus each proved positive equivalence class in the preceding table supplies all four combinations from \(F(X)\), after choosing the canonical core operators.
This does not assert Hilbert-space closability of arbitrary supplied full-domain maps.

### The strong counterexample and its precise direction

[C_F0128 v2](../claims/Yin_C_F0128_v2.md#statement) fixes a single normal generator on the disk with an atom, a dense star-polynomial domain, and one normalized dual satisfying both vacuum-adjoint membership and closability.
Nevertheless a nonzero rank-one atomic projection commutes with the generator, so \(\Delta(X)<1\).
A direct atomic-coordinate contradiction excludes every full-\(M\Omega\) dual, including any different choice of operator.
The closed extension still excludes the bounded atomic vector \(e\Omega\).

Consequently, for every \((a,b)\in\{1,2\}\times\{3,4\}\),
\[
 Q_{ab}\not\Rightarrow F(X),\qquad
 Q_{ab}\not\Rightarrow\Delta(X)=d,
 \qquad Q_{ab}\not\Rightarrow\mathsf A(X).
\]
All three failures occur even for a single normal generator; the last follows because the source hypothesis implies maximal Delta.
The proof and its selected assessment belong to C_F0128, rather than this synthesis.
This witness establishes the small-domain-to-full-domain failures.
It does not refute any implication starting from \(F(X)\).
Since both extra conditions hold together in the witness, it also does not separate vacuum-adjoint membership from closability.

The companion selfadjoint atom-plus-interval example in [C_F0128 Section 3](../claims/Yin_C_F0128_v2.md#3-selfadjoint-boundary-a-dense-algebraic-dual-need-not-be-closable) shows why a purely algebraic dense-domain hypothesis is insufficient.
An explicit sequence proves that its operator is not closable and its vacuum is outside the adjoint domain; it is not a counterexample to any of the four strengthened combinations for selfadjoint tuples.

For selfadjoint generating tuples, \(X_j\)-invariance of \(E\) implies \(\mathcal A\Omega\subseteq E\); restricting a closable operator preserves closability.
The bounded starred-commutator regularization retained in [ACSY24-U001 Section 3](../audits/literature/ACSY24/Yin_U001.md#3-reconstructing-the-unbounded-step-in-proposition-35) therefore gives
\[
 Q_{24}\Longrightarrow Q_{14}\Longrightarrow\Delta(X)=d.
\]
Here the starred commutators coincide with the given generator commutators.
The generation hypothesis supplies density of the restricted polynomial core.
This conclusion does not assert \(Q_{14}\Rightarrow F(X)\) or a finite-Fisher-information conclusion.

### Reverse candidate under bounded division closure

The complete new candidate is retained in [C_F0129 v1](../claims/Yin_C_F0129_v1.md#statement), with selected status [proof draft](../claims/Yin_C_F0129_v1.md#decision-initial).
Put
\[
 \mathcal R_X=\operatorname{Div}_M\mathbb C\langle X\rangle,
 \qquad X_j^*\in\mathcal R_X\quad(1\le j\le d).
\]
All inverses in this closure are bounded inverses in \(M\).
Under this additional hypothesis, the candidate proves from \(F(X)\) the existence of new normalized closed \(\widehat D_i\) with
\[
 M\Omega\subseteq\operatorname{Dom}\widehat D_i
                 \cap\operatorname{Dom}\widehat D_i^*,\qquad
 [X_j,\widehat D_i]=\delta_{ij}P.
\]
Its intended consequence is all four \(Q_{ab}\).
The construction also yields the actual vacuum vectors for starred derivations, hence the source hypothesis \(\mathsf A(X)\), within the same candidate argument.
No converse from \(\mathsf A(X)\) for this whole bounded-division class has been established here.

The candidate combines the retained symmetric-form estimate with new general-Hilbert--Schmidt automatic continuity, a full-domain implementation of the conjugate derivation, and two actual graph restorations.
The required complete fixed-version review of these combined interfaces remains outstanding.
Its dependencies and review obligations are listed in C_F0129, not silently supplied by reviews of the earlier component Claims.
The new operators are closures of normalized star-core restrictions; the original maps need not have been shown closable or equal to them on all bounded vectors.

Normality alone does not imply this bounded-division condition, as already fixed in [C_F0008 Section 4](../claims/Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target).
The candidate therefore does not settle arbitrary correlated normal or arbitrary nonnormal tuples.

### Current implication map

| Question | Retained conclusion |
| --- | --- |
| \(\mathsf A(X)\Rightarrow\) all four \(Q_{ab}\) | Proved by the exact ACSY24 canonical operator and core-adjoint construction. |
| \(F(X)\Rightarrow\) all four \(Q_{ab}\) in the four positive classes above | Proved, via C_F0071 and that source construction. |
| Any one \(Q_{ab}\Rightarrow F(X)\), \(\mathsf A(X)\), or maximal Delta in general | Refuted by the single normal atomic example. |
| Selfadjoint generating tuples: closable dense invariant duals imply maximal Delta | Proved by restriction to the dense polynomial core and bounded starred-commutator regularization. |
| \(F(X)\) plus adjoints in the bounded division closure implies all four \(Q_{ab}\) | Complete proof draft; not yet adopted as proved. |
| Arbitrary bounded tuples: \(F(X)\Rightarrow Q_{13},Q_{14},Q_{23},Q_{24}\) | Unresolved outside the retained positive results and candidate's extra hypothesis. |
| General equivalence of vacuum-adjoint and closability conditions | Not established; the present strong example does not separate them. |

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

The principal unfinished questions remain whether A(X) and F(X) agree for arbitrary correlated normal tuples or arbitrary bounded tuples, and which normalized dense-domain systems can always be selected from a bare F(X) system in those general classes.
C_F0128 separates each small-domain condition from both full hypotheses, but is not an F-versus-A separating example.
C_F0129 is an additional-premise proof draft, not a general resolution.
