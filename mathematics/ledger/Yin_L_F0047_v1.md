---
author: Yin
---
# ACSY24 and full-domain duals: exact reductions, positive cases and remaining gaps

Date: 2026-10-14.
Human author Yin.
The normal_domain and bare_dual agents carried out separate bounded explorations; root checked the displayed norm-equivalence and sandwich contradiction, organized this fixed comparison, and retains the original source-search limits.
The new accepted Claim assessments and independent reviews belong to their linked C/R materials.
This synthesis is self-checked and is not an independent mathematical review.

The explicit human request had three parts: retain the arbitrary-tuple relative CS05 theorem, test ACSY24 against the actual canonical full-M closure domain for correlated normal tuples, and test the converse from bare linear full-M duals.
This account retains useful exploratory reductions and failed tests.
It does not reopen a completed Task or claim resolution of either general implication.

## Fixed complete results and their roles

The requested complete arbitrary-tuple relative-Delta theorem has no adequate project-proof home identified in the retained public materials.
The [CS05 source unit](../audits/literature/CS05/Yin_U001.md#cs05-u001) retains the relative cycle definition, the transpose/adjoint correction and the bounded-dual source mechanism at its stated scope.
That source account does not supply the complete requested project extension; this missing-input limitation is retained separately from the normal-domain deductions below.
[CS05-U001](../audits/literature/CS05/Yin_U001.md#cs05-u001) owns the bounded literature comparison.

[Automatic norm continuity and scalar converse, C_F0069](../claims/Yin_C_F0069_v1.md) retains the new deductions from this investigation: every bare full-domain normal dual is automatically bounded M -> H; one selfadjoint generator with a bare full-domain dual satisfies the actual ACSY24 vacuum-adjoint condition.
The second conclusion also holds for each selfadjoint marginal, not jointly.
The complete proofs are in C_F0069, not in this synthesis.
[Lau88-U001](../audits/literature/Lau88/Yin_U001.md#lau88-u001) owns the external automatic-continuity input and its inspection boundary.

## General normal canonical-domain question

Question: under ACSY24 Proposition 3.5 for a normal generating tuple, must the actual closure of E_i0=(id tensor tau) partial_i on the starred polynomial core contain all M Omega?
The arbitrary correlated-normal implication remains unresolved in this bounded investigation.

### Exact operator and equivalent remaining estimate

Let `(M,tau)` be finite tracial, let the bounded normal tuple `X` generate M, and put `H=L2(M,tau)`, `Omega=1`, and `P=C<X,X*>`.
Assume actual densely defined outer-bimodule derivations

`partial_i:P -> H tensor_2 H`,
`partial_i X_j=delta_ij (1 tensor 1)`,
`1 tensor 1 in Dom(partial_i*)`.

Write `xi_i=partial_i*(1 tensor 1)`, `E_i0=(id tensor tau)partial_i`, and `E_i=closure(E_i0)`.
These are the original polynomial operators and their actual Hilbert closures.
The source supplies closability and polynomial adjoint domains; see [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md).
A different full-domain extension would not answer the question.

For each fixed i the desired conclusion is equivalent to

`there exists C_i<infinity such that ||E_i0 p||2 <= C_i ||p|| for every p in P`.  (N1)

Here is the complete equivalence, reusing the graph mechanism of [C_F0027, Section 5](../claims/Yin_C_F0027_v1.md).
If `M Omega subset Dom E_i`, the map `a -> E_i(a Omega)` from the Banach space M to H has closed graph: operator-norm convergence implies L2 convergence, and E_i is closed.
The closed graph theorem gives (N1).
Conversely, Kaplansky density, followed by norm approximation inside `C*(X)`, gives for every a in M a bounded net `p_alpha in P` with `p_alpha Omega -> a Omega` in H and uniformly bounded operator norms.
Under (N1), `E_i0 p_alpha` has a weakly convergent subnet in H.
The graph of the closed linear operator E_i is a norm-closed linear subspace of `H direct_sum H`, hence weakly closed.
Its weak limit contains `(a Omega,eta)`, proving `a Omega in Dom E_i`.
This proves membership in the original graph and uses no unidentified maximal extension.
In this finitely generated setting sequences could also be obtained by bounded L2 approximation, but the net proof avoids an unnecessary separability premise.

Only the first bound is needed for the user's closure-domain question.
A bound for `E_i0*` is additionally needed to obtain all-M adjoint domains by the same method; it must not be silently included in or inferred from (N1).

### Already established positive scopes

1. [C_F0055](../claims/Yin_C_F0055_v1.md#statement) proves the scalar normal-coordinate estimate with constant `(5+2 sqrt(27)) ||xi||2`, and both actual domains.
   Combined with [C_F0045](../claims/Yin_C_F0045_v1.md#statement), this answers the question affirmatively for arbitrary freely independent normal coordinates.
   The older unresolved marginal-bound sentence in C_F0045 is superseded by the later scalar result; it is not a current gap.
2. [C_F0043, Section 3](../claims/Yin_C_F0043_v1.md) proves the needed estimate for arbitrary correlated unitary tuples, and its subsequent sections handle univalent analytic closed-curve coordinates.
   [C_F0060](../claims/Yin_C_F0060_v1.md) handles the stated univalent analytic arc hypotheses.
   These are geometric assumptions and do not cover arbitrary compact planar spectra.
3. The unitary calculation is coordinatewise: if just the selected coordinate `X_i` is unitary, its derivation vanishes on every other generator and adjoint, including normal coordinates with unrestricted spectra.
   The product-rule and coassociativity-defect calculation in C_F0043 Section 3 therefore still applies to this i on the entire mixed starred core.
   All tensors produced by this particular derivation are algebraic polynomial tensors.
   Thus (N1) holds for a unitary coordinate even if other normal coordinates are unrestricted.
   This is an immediate reuse of that proof, not a new general-tuple theorem or a freeness claim.

### Two mechanisms tested in this continuation

**Scalar positive-weight symmetrization.**
The scalar proof in C_F0055 bounds Cauchy transforms after replacing a scalar probability measure mu by `(1+f/2)mu`, for real `||f||infinity<=1`; its three-variable curvature kernel is nonnegative.
For a general mixed polynomial p, `p(X)` does not belong to the abelian algebra `W*(X_i)`.
Replacing mu_i by a scalar weight from that algebra can test only the marginal conditional expectation of p and cannot represent `E_i0 p`.
Applying the argument separately to marginal functions therefore gives no estimate on all mixed words.
A noncommutative positive-weight version would have to retain the full joint vacuum xi_i and prove its own positivity identity.
[C_F0057](../claims/Yin_C_F0057_v1.md) excludes the simpler proposed lower bound depending only on the marginal curvature/law: its correlated Haar family has unbounded negative mixed-defect values while all marginals remain fixed.
Those examples have bounded duals and satisfy the domain conclusion; they are failures of a proposed estimate, not counterexamples to the user's implication.

**Singular sandwich transport.**
The maximal-Delta example `(h,hSh)` in [C_F0068, Section 4](../claims/Yin_C_F0068_v1.md#sharpness-proof), with h uniform on `(0,1)` and S semicircular free from h, excludes even a bare full-M dual.
It might appear to give a normal-tuple counterexample here.
It does not: it fails the ACSY24 vacuum premise.
This failure can be checked directly, without importing the desired general-normal conclusion.
Suppose a derivation partial_Y on the represented starred core had `partial_Y h=0`, `partial_Y Y=1 tensor 1`, and actual vacuum xi.
For a real polynomial c(h),

`partial_Y(c(h) Y c(h))=c(h) tensor c(h)`,
`tau(c(h))^2 = <xi,c(h) Y c(h)>`,
`|tau(c(h))|^2 <= ||xi||2 ||c(h) h||^2 ||S||2`.  (N2)

For each fixed epsilon>0, polynomial approximation to the continuous function `c_epsilon(t)=1/(t+epsilon)` on `[0,1]` permits passing to (N2).
Since `||c_epsilon(h)h||<=1`, its right side is at most `||xi||2 ||S||2`, whereas `tau(c_epsilon(h))=log((1+epsilon)/epsilon)` diverges.
Thus there is no such actual vacuum.
This eliminates the uniform-h sandwich as a counterexample before any domain theorem is invoked.
The test does not rule out every singular correlated transport; a viable example would have to satisfy the joint L2 vacuum conditions and simultaneously violate (N1).

### Precisely retained obstruction and search scope

[C_F0056, Section 6](../claims/Yin_C_F0056_v1.md) has already proved ordinary coassociativity in the original iterated Hilbert domains.
With `partial_i^dagger(p)=(partial_i(p*))^dagger` and `F_i0=(id tensor tau)partial_i^dagger`, the genuine adjoint identities are

`E_i0* p=p xi_i-F_i0 p`,
`F_i0* p=p xi_i*-E_i0 p`.

Coassociativity controls `E_i E_i0 p` and `F_i F_i0 p`; the norm calculation requires mixed terms such as `E_i F_i0 p`.
On a noncommutative mixed core, one may not replace F by `J E J` as in the scalar calculation.
A mixed-domain/positivity estimate incorporating the joint vacuum remains the exact missing step of this route.
Neither [C_F0106](../claims/Yin_C_F0106_v1.md)'s bounded-rational graph invariance nor the weak form of rationality supplies a uniform bound over the full operator-norm unit ball of P.

The bounded external search on 2026-10-14 used the expressions `normal dual system conjugate free probability bounded`, `non-self-adjoint conjugate variables bounded derivation`, `Dabrowski normal operators difference quotients`, `generalized difference quotient conjugate bounded`, and `coassociativity conjugate variables estimate`, after the local Claims above and ACSY24/Dab10 source interfaces were checked.
It surfaced the familiar selfadjoint q-Gaussian dual-system literature and unrelated results, but no primary-source statement with the exact arbitrary correlated normal-domain conclusion was verified.
Those search hits are leads, not accepted theorem inputs.
No global literature-absence or novelty assertion is made.
The general implication and a genuine counterexample are both still unresolved in this bounded exploration; (N1), the coordinatewise positive reuse, and the explicit failure of the sandwich test identify the continuation target.

## Bare full-domain dual question

### Exact implication and known reductions

Let X=(X_1,...,X_d) be a bounded normal generating tuple in a finite tracial von Neumann algebra M, H=L2(M), and P the vacuum projection.
The premise being tested is the existence of complex-linear maps D_i:M Omega -> H satisfying [X_j,D_i]=delta_ij P on all M Omega.
No continuity, closability, adjoint condition, or normalization is included.
The proposed conclusion is existence of derivations partial_i on A=C<X,X*> with values in H tensor H, partial_i X_j=delta_ij (Omega tensor Omega), and Omega tensor Omega in the actual Hilbert-space domain of partial_i*.
This is an existential assertion about X.
A badly behaved choice of D for an X that already has good derivations would not refute it.

[C_F0024, Section 3](../claims/Yin_C_F0024_v1.md) and [C_F0030, Section 3](../claims/Yin_C_F0030_v1.md) prove Delta(X)=d from this premise alone, by clearing finite-rank ranges into M before composing with D.
This supplies unstarred algebraic freeness.
It does not establish the actual vacuum-adjoint estimate on A.
[C_F0068, Part B](../claims/Yin_C_F0068_v1.md) proves that maximal Delta alone does not even imply the premise; its sandwich example cannot be used as a counterexample to the present implication.

With the additional assumptions that each D_i is closable and Omega belongs to Dom D_i*, the implication is already covered by [C_F0038](../claims/Yin_C_F0038_v1.md) and [C_F0025](../claims/Yin_C_F0025_v1.md).
Indeed, normality supplies the Hilbert--Schmidt starred-generator commutators.
Normalize with the sign required by the present generator-first convention:

\[
 E_i(a\Omega)=-D_i(a\Omega)+aD_i\Omega,
 \qquad E_i\Omega=0,\qquad [E_i,X_j]=\delta_{ij}P.
\]

On A, define partial_i a=Theta^{-1}([E_i,a]), where Theta identifies the coarse tensor product with Hilbert--Schmidt operators and Theta(Omega tensor Omega)=P.
Leibniz's identity gives a well-defined derivation, including the actual starred relations of A.
Its vacuum functional satisfies

\[
 \langle\Omega\otimes\Omega,\partial_i a\rangle
 =\langle\Omega,E_i(a\Omega)\rangle
 =\left\langle-D_i^*\Omega+(D_i\Omega)^*,a\Omega\right\rangle.
\]

Thus its actual adjoint vacuum exists, with the displayed L2 vector.
The bare premise is not yet known to supply the Hilbert-space closability and actual vacuum-adjoint assumptions used by this particular argument.
The automatic operator-norm continuity now proved in C_F0069 is a distinct conclusion.
[C_F0045](../claims/Yin_C_F0045_v1.md) gives an L1 vacuum density for closable full-domain selfadjoint duals and explicitly stops short of an L2 density or vacuum-adjoint membership.

### Source check of the unbounded-dual equivalence

The abstract of Shlyakhtenko's *Remarks on free entropy dimension* can suggest that closability alone suffices.
Theorem 1(b), p. 3 of [arXiv math/0504062v1](https://arxiv.org/pdf/math/0504062), explicitly includes Y Omega=0 and Omega in Dom Y*.
The exact source interface is already retained in [Shl06-U001](../audits/literature/Shl06/Yin_U001.md#shl06-u001).
It therefore does not eliminate the missing vacuum condition.
Corollary 1 in that arXiv edition uses anti-symmetric operators, which again supply an adjoint-domain condition; the retained Abel preprint numbers that corollary 2.
These are coverage boundaries, not nonimplication results.

### Ongoing routes and failure conditions

One-variable candidates use X as multiplication by the coordinate for a diffuse compactly supported probability measure mu.
On polynomials the normalized dual is forced to be

\[
 E_0p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\mu(w).
\]

A measure with no L2 conjugate variable is not by itself a counterexample: one must construct an all-L-infinity input dual satisfying the equation.
Likewise, formal extension by a vector-space basis does not preserve the required C[z]-module commutator equation, and an algebraic extension into measurable functions does not ensure L2-valued outputs.
These are the decisive obligations for this route.

A second possible route is automatic continuity for algebraic intertwiners.
A bounded search found Sinclair's [*Automatic Continuity of Linear Operators*, Chapter 2](https://www.cambridge.org/core/books/abs/automatic-continuity-of-linear-operators/intertwining-operators/065AF1210581543AA9FC8A9CBA86F3A3), whose publisher summary distinguishes critical eigenvalues and divisible algebraic spectral subspaces.
Only that summary was inspected.
It concerns homogeneous equations ST=RS; the present rank-one inhomogeneous commutator is not covered by an inspected theorem.
That summary alone was not used to deduce automatic continuity.
The subsequent exact Lau88 application resolved the operator-norm continuity question; its complete proof is in C_F0069, linked below.


## Consequences of the new fixed deductions

The Laursen triangular-intertwiner argument in C_F0069 removes arbitrary operator-norm discontinuity as a possible obstruction for a normal coordinate with a dual defined on every bounded vector.
The result applies to the supplied dual itself.
Thus a future counterexample to the bare converse cannot be justified merely by choosing a pathological discontinuous map on M.

It remains incorrect to identify this M-to-H norm continuity with boundedness on H, Hilbert-space closability, or a vacuum adjoint.
The Fourier-average proof in C_F0069 obtains the latter in the one-selfadjoint-generator case by the explicit inequality
\[
 |(\tau\otimes\tau)(\partial p)|\le
      2\|E:\mathcal M\to H\|\,\|p\|_2,\qquad p\in\mathbb C[x].
\]
Its antisymmetric scalar kernel is the additional reason that case is now positive.
Simply applying the marginal proof to every coordinate does not give the joint vacuum estimates on mixed words.

The earlier scalar counterexample search must therefore exclude a single selfadjoint generator: that case is now affirmatively resolved by the linked result.
No corresponding scalar nonselfadjoint normal converse or general joint converse was proved during this round.

## Continuation targets

For ACSY24 implying the actual canonical full-M domain, the remaining exact target is (N1) for arbitrary mixed starred polynomials.
A useful route must control the mixed E_i F_i terms with the full joint vacuum; marginal-only curvature bounds and the already excluded sandwich example do not suffice.

For the bare full-domain hypothesis implying ACSY24, start from the now-established M-to-H continuity and verify what additional starred-generator commutator or spectral-localization conclusions follow without Hilbert-space closability.
Then seek the joint bound
\[
 |(\tau\otimes\tau)(\partial_i p)|\le C_i\|p\|_2
 \quad(p\in\mathbb C\langle X,X^*\rangle),
\]
with a well-defined derivation on that represented starred core.
The existing C_F0038 proof must not be imported wholesale where it uses weak continuity obtained from closability.

These are unresolved mathematical targets, not refuted statements.
No primary source with either exact arbitrary-correlated-normal implication was verified in the bounded searches recorded above.
This does not assert that the wider literature lacks such a theorem.
