---
author: Yin
---

# Independent review of conditional Haar addition and rank-one Schur limits

<a id="independent-conditional-schur-proof"></a>
## Finding: the restricted statement and complete argument are supported

Review act: 2026-11-05T08:16, human record author Yin.
A separately organized AI reviewer outside substantive proof development checked the fixed [C_F0193_v1 statement](../../claims/Yin_C_F0193_v1.md#statement) and [entire argument](../../claims/Yin_C_F0193_v1.md#argument), including the conditional theorem, original affine application, amplitude interval, matrix example and direct scalar corollary.
The supplied review context contained the exact target, assignment, human authority, applicable rules and operational limits.
No exploration drafts, proof-generation dialogue, author explanations, development summaries or prior conclusions about C_F0193 were supplied or consulted before the initial findings.
The reviewer read the fixed proof and its necessary dependencies directly and reported initial findings before proposing any repair.
No substantive repair was proposed or contributed.
No earlier review of C_F0193 was consulted or relied upon.

No remaining mathematical gap was found in the exact restricted assertions.
The proof establishes full ordinary normalized logarithmic limits almost surely under every allowed cross-dimensional coupling, and hence the stated upper-limit and independent-dimension consequences.
The strict-bulk affine and scalar classes have positive finite ordinary FK determinant and no bounded free inverse.
The restrictions remain essential to the proved scope: this finding does not settle the unrestricted [F0015 contract](../../tasks/Yin_T_F0015_v1.md#contract) and supplies no Task-completion conclusion.

## Conditional theorem and source interfaces

The checked mathematical edition of HZ25 is the retained arXiv:2210.11147v4, as identified in [the source edition note](../literature/HZ25/readme.md).
I read the original pp. 8--12 and 14--19, including the model and symmetrized singular-law identification, Propositions 2.1--2.2, Theorem 2.3, Definitions 2.6--2.7, Theorems 2.8 and 3.2, and Lemmas 4.3--4.4.
The critical formulas on pp. 9, 12, 15, 18 and 19 were also visually inspected.
The [existing source unit](../literature/HZ25/Yin_U001.md#hz25-u001) correctly separates these accepted inputs from the local conditional and integration deductions.

The source hermitization uses dimension 2N and normalized trace 1/(2N), with positive singular empirical measures normalized by 1/N.
Its convention G(z)=integral (z-x)^{-1} dnu(x) gives -Im G(i eta) equal to the average of eta/(s_j squared plus eta squared).
Thus the sign and the factor 1/2 in the regularized logarithm agree with the candidate's defect identity.
The source model with Sigma=I is a full physical U(N) perturbation after singular-value decomposition of an arbitrary additive matrix; no auxiliary block Haar matrix is substituted.
The source's Section 2.3 also identifies the free symmetrized singular law with the stated convolution, including for a positive deformation d free from the Haar unitary.

Regular bulk at zero supplies finite strictly positive imaginary subordination values.
Their continuous extensions on i[0,1], the reciprocal-Cauchy-transform identity and compactness give a denominator bounded away from zero.
For every sequence of uniformly supported positive laws converging weakly to mu, moment convergence realizes the hypotheses of Proposition 2.2 in one commutative tracial algebra.
The contradiction argument consequently gives an actual fixed Levy neighborhood, without any unasserted rate of convergence.
The proof correctly uses omega_1 plus omega_2 in the denominator; I confirmed the repeated-index misprint in the original Lemma 4.3 display on p. 18.

Theorem 2.8 has a fixed neighborhood hypothesis and its sufficiently large dimension depends on the listed limiting measures, interval, spectral scale and norm bound.
The candidate's deterministic sequence completion by quantile approximations permits each admissible finite deformation as an input to that uniform statement.
The at-least-three-point symmetrization hypothesis is present in the conditional theorem.
The singleton interval I={0} is legitimate here; the source itself makes that application in the proof of Theorem 4.1 on p. 16.
The stochastic-domination exponents can be fixed before the O(log N) grid union, whose resulting failure probabilities are summable.

Conditioning only on the background at the current dimension preserves its conditional Haar law.
The deterministic uniform bound gives P(E_N intersect B_N) at most N^{-D} by conditional expectation.
First Borel--Cantelli applies to these joint events and the assumed eventual guard, without summability of P(E_N complement) or cross-dimensional independence.
Conditioning on the entire sequence is neither assumed nor used.
At fixed positive eta, Proposition 2.2 and this same summable bound give the required Cauchy-transform convergence.
Compact eventual support and uniqueness of the symmetric Stieltjes transform identify all weak subsequential limits, with a countable intersection sufficient for the asserted almost-sure conclusion.

The dyadic estimate integrates to a constant times delta plus O(N^{-1+epsilon} log N); the factor-two spectral bound also covers the final partial interval.
Theorem 3.2 and the three ranges in the original proof of Lemma 4.4 give the tiny-integral estimate uniformly over every additive deterministic deformation.
Sigma=I discharges its inverse hypothesis even when D_N is singular.
The large fixed L makes Markov's bound at N^{-1} summable.
The same least-value tail, with threshold tending to zero at fixed N, gives almost-sure finite invertibility.
The exact spectral differentiation identity and the limiting free resolvent bound then justify the final removal of the logarithmic regularizer, including finiteness of the limiting logarithmic integral.
No in-probability eigenvalue theorem is used as a replacement for these steps.

## Affine Schur reduction and auxiliary conclusions

I checked the fixed-coefficient strong Haar input and the bounded-inverse argument retained at [L_F0062_v1](../../ledger/Yin_L_F0062_v1.md#haar-pencils).
I also read the published CM14 Theorem 1.5 and Corollary 2.3 at printed pp. 150 and 154 through [the primary source](https://smf.emath.fr/download/pdf/44403), identified in [its source note](../literature/CM14/readme.md).
Those statements require independence of the Haar inputs within each dimension and impose no independence between different dimensions.
Matrix coefficients are explicit in Corollary 2.3.
Uniform polynomial approximation of inverse positive moduli therefore transfers the two bounded free inverse assumptions to eventual finite inverses and strong rational convergence.
It supplies deterministic eventual norm bounds and singular-law convergence for D_N=C_N^{-1}.
Setting D_N to zero when either required finite inverse is unavailable defines a background-measurable statistic and changes no eventual conclusion.
The fresh Haar variable is independent of this entire within-dimension statistic.

The finite identity is det L_N=det B_N det C_N det(D_N+V_N), with each small factor of dimension N.
On the free side the rectangular block elimination has the same sign and order: YX=vc, unitary conjugation replaces vc by cv, and 1+cv=c(d+v).
The normalized traces give m log Delta(L)=m log Delta(B)+log Delta(c)+log Delta(d+v), so division by mN on the finite side matches every free term.
All multipliers in the elimination are bounded unipotents.
The [FK52 unit](../literature/FK52/Yin_U001.md#fk52-u001) supplies ordinary bounded multiplicativity, including zero values.
The [Luc22 unit](../literature/Luc22/Yin_U001.md#luc22-u001) supplies Theorem 14.18 only for the identity-diagonal triangular factors, where dense range, injectivity and agreement with the ordinary determinant are automatic.
I checked the original Luc22 Theorem 14.18 on p. 24 for those precise hypotheses and its sum-trace normalization.
The free Haar-generated algebra can be realized as the free-group von Neumann algebra, so these factors lie in the group-module setting of that source; trace-faithful free Haar models give the same determinant values.

The two strict moments place zero in HZ25's regular bulk with no exceptional atom, since d is boundedly invertible.
A point-mass modulus law cannot satisfy both strict inequalities.
The strong rational convergence jointly with the fresh Haar variable identifies the actual possibly nonnormal d+v singular law with the convolution law obtained independently by the conditional theorem.
The logarithmic integrals therefore agree.
Positive regular-bulk density at zero excludes a bounded inverse and the resolvent bound gives a finite logarithmic integral.
The rectangular inverse identity transfers noninvertibility from d+v to L, while bounded determinant multiplicativity transfers determinant positivity.

The [coefficient-position symmetry](../../claims/Yin_C_F0192_v1.md#coefficient-gauge) was checked at its stated interface.
Its dimensionwise Haar change of variables preserves the finite laws, both coupling regimes and the free target.
It supplies no Schur inverse or bulk hypothesis, and the candidate explicitly requires those checks after a permutation.

For c_t=t c_0, the moments are |t| squared times norm(c_0)_2 squared and |t|^{-2} times norm(c_0^{-1})_2 squared.
The exact two strict inequalities therefore give the displayed amplitude annulus.
Trace invariance expresses the inverse moment through |c_0|^{-2}, and strict Cauchy--Schwarz makes the annulus nonempty exactly under the stated nonconstant-modulus condition.

In the displayed 2-by-2 example I recomputed B^{-1}, c and d.
The circle lower bounds give both required bounded inverses.
Expanding (1+u/10)/(1+u/2) gives constant Fourier coefficient 1 and squared nonconstant coefficient sum (4/25)/(1-1/4)=16/75.
For its reciprocal the corresponding sum is (4/25)/(1-1/100)=16/99.
The listed invariant lines have no common member.
Each rank-one matrix has nonzero trace, so a simultaneous single-entry similarity would put both entries on the diagonal and force commutation, contradicted by their direct products.
The claimed exclusion from the previously stated two-position, single-entry sparse and simultaneous triangular classes is therefore correct at its explicit direct-coverage scope.

## Direct scalar corollary

The strict squared triangle inequalities force all three coefficients to be nonzero.
The bounded deformation (a_0+a_1U_N)/a_2 has the required almost-sure singular-law limit under every coupling, and its fresh perturbation remains full Haar conditionally.
Its limiting modulus law is nonconstant and has no zero atom.
The circle moment calculations give norm(d)_2 squared=(x_0+x_1)/x_2 and inverse second moment x_2/|x_0-x_1| when x_0 differs from x_1.
When x_0=x_1, the inverse second moment is infinite because of the inverse-square singularity at the unique circle root; this is a measurable inverse moment and does not assert bounded invertibility.
The two strict bulk inequalities are consequently equivalent to the three stated strict squared triangle inequalities, including the equal-modulus case.
Scaling by a_2 adds exactly log|a_2| to both logarithmic targets.
The resulting full limit, finite positive determinant and absence of a bounded free inverse follow at the asserted strict scope.
No equality or outside-region conclusion is supplied.

## Verification limits

This is an independent mathematical review of the project's complete restricted argument and the applicability interfaces actually used.
The original proofs behind HZ25's cited continuity and local-law inputs and Rudelson--Vershynin estimate were accepted at their checked external statements, not independently re-audited.
CM14's strong-convergence proof, FK52's original analytic proof and Luc22's cited foundational book proofs were not recursively re-audited.
The retained source-unit boundaries remain in force.
No formal verification, general coefficient theorem, boundary bulk theorem, uniform event over all coefficient tuples or priority finding is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [C193 exact statement](../../claims/Yin_C_F0193_v1.md#statement) | Entire conditional theorem, rank-one affine theorem, arbitrary-coupling quantifiers, ordinary normalizations, positive-FK/unbounded-inverse conclusions, amplitude interval, exact matrix example and scalar strict-triangle corollary. |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [C193 complete argument](../../claims/Yin_C_F0193_v1.md#argument) | Entire guarded conditional local-law and logarithmic-integral argument, finite/free Schur reduction, rational strong-convergence guards, free-target identification, amplitude/example calculations and scalar proof. |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [HZ25 exact source unit](../literature/HZ25/Yin_U001.md#hz25-u001) | Only the inspected v4 model/normalization and free singular-law identification, Definitions 2.6--2.7, Propositions 2.1--2.2, Theorems 2.3, 2.8, 3.2 and Lemma 4.4 interfaces used by C193; primary applicability and the local displayed-index issue were checked, without a recursive audit of cited source proofs. |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [L62 Haar background input](../../ledger/Yin_L_F0062_v1.md#haar-pencils) | Only fixed-coefficient almost-sure strong Haar convergence under the original coupling quantifier and its bounded-inverse polynomial approximation consequences for B_N, C_N and the required rational singular laws. |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [FK52 exact source unit](../literature/FK52/Yin_U001.md#fk52-u001) | Only accepted ordinary bounded multiplicativity in finite tracial algebras, including zero values, applied to bounded Schur and rectangular factors; no new audit of the original classical proof. |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [Luc22 exact source unit](../literature/Luc22/Yin_U001.md#luc22-u001) | Only Theorem 14.18 for bounded unipotent factors with identity diagonal maps, their dense-range/injectivity hypotheses, ordinary-determinant agreement and sum-trace normalization. |
| [Independent conditional and Schur review](#independent-conditional-schur-proof) | [C192 coefficient gauge](../../claims/Yin_C_F0192_v1.md#coefficient-gauge) | Only the proved dimensionwise Haar coefficient-position symmetry and preservation of both coupling regimes and the free determinant, with all new Schur and strict-bulk assumptions checked separately. |
