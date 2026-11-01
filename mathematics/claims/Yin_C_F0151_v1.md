---
author: Yin
---
# Automatic continuity of bare duals for a bounded selfadjoint factorization

Human author: Yin.
Root developed the explicit smooth triangular calculus and the projective functional criterion after the single hidden-factor ACSY construction.
These are development contributions, not independent review.

## Current assessment
[Selected decision](#decision-initial)

## Statement

Let N be a finite tracial von Neumann subalgebra of an ambient finite tracial algebra M, with compatible faithful normal probability traces.
Put H_N=L2(N), identify N with N Omega, and let X be in N.
Assume X=AB for bounded A,B in M, B acts injectively on L2(M), and Y=BA is selfadjoint with diffuse spectral law.

Every complex-linear map E:N->H_N satisfying [E,X]=P_Omega on all bounded vectors is bounded from the operator norm to H_N.
No continuity, closability, adjoint domain, equality N=M or bounded inverse of A or B is assumed.

This applies to X=hS in N=W*(hS), where h=2+s_0 and s_0,S are freely independent standard semicirculars.
Any bare generator-first dual D has E=-D and is norm bounded.
Its existence is equivalent to bounded well-definedness of the functional (AC5)-(AC6) in the Banach projective tensor norm.
The general bounded-dual criterion holds for arbitrary bounded tuples at its stated bounded-witness scope; its application to bare witnesses uses the factorization hypothesis.

No bare dual is constructed or excluded for hS, and no canonical adjoint/full-domain conclusion is inferred.
The accepted actual A witness for this tuple remains separate.

## Reuse and source scope

The exact [Lau88-U001](../audits/literature/Lau88/Yin_U001.md#lau88-u001) published interfaces, Proposition 3.7 and Theorem 4.1, are reused at their inspected scope.
[C_F0069](Yin_C_F0069_v1.md#argument) supplies the triangular-intertwiner method and elementary no-divisible-subspace lemma for normal operators.
A local search of those records and the continuing test found no already fixed nonnormal factorization statement.
The extra smooth calculus is constructed explicitly.
The concrete product's injectivity input is C_F0147's accepted full-polynomial reference interface, with exact restriction explained below.
Hahn--Banach and Hilbert Riesz representation are used in their usual Banach/Hilbert settings.

## Argument

Here are the complete additional calculus details.
On a compact real interval containing 0 and sigma(Y), put

\[
 \Phi_f=f(0)1+A f^{[1]}(Y,0)B.
 \tag{AC1}
\]

Divided differences at repeated nodes use derivatives.
For polynomials, Phi_f=f(X), because A Y^k B=X^{k+1}.
Approximation of f and f' by polynomials shows Phi_f belongs to N for every smooth f, with norm bounded by |f(0)|+||A||||B||||f'|| infinity.
The polynomial identity extends by this approximation to Phi_(fg)=Phi_f Phi_g.
The map is unital, sends the coordinate function to X, and depends only on f near K={0} union sigma(Y).

On ambient H=L2(M), define the finite-rank/Hilbert--Schmidt expression

\[
\begin{split}
 \Gamma_f={}&f'(0)P
  +A f^{[2]}(Y,0,0)BP
  +PA f^{[2]}(0,0,Y)B\\
 &+A\left(\iint f^{[3]}(s,0,0,t)\,dE_Y(s)(BPA)dE_Y(t)\right)B.
 \tag{AC2}
\end{split}
\]

The double integral is in the Hilbert--Schmidt spectral calculus, where its norm is at most ||f'''|| infinity times ||BPA||HS/6.
The two second divided differences have bounds ||f''|| infinity/2.
Thus (AC2) is continuous for the C3 norm, without an operator-Lipschitz or arbitrary bounded-operator Schur multiplier premise.

For f(z)=z^n, (AC2) equals sum_(k=0)^(n-1) X^k P X^(n-1-k).
One direct verification expands (z-X)^-1=z^-1 I+z^-1 A(z-Y)^-1B and its product on the two sides of P: the coefficients of z^-n-1 give the four terms of (AC2).
Consequently Gamma_X=P and

\[
 \Gamma_{fg}=\Phi_f\Gamma_g+\Gamma_f\Phi_g.
 \tag{AC3}
\]

Polynomial C3 approximation (approximate the third derivative uniformly and integrate three times) extends this identity to all smooth f,g on the interval.
Each approximating polynomial Gamma preserves H_N=L2(N), so Gamma_f does too.
Its restriction H_N->H_N and then N->H_N is bounded.
If f vanishes near K, all divided differences in (AC1)-(AC2) vanish, including repeated-node derivatives, so the whole calculus vanishes.

On the Banach space H_N direct-sum N set

\[
 \mathcal T=\begin{pmatrix}L_X&P|_N\\0&L_X\end{pmatrix},
 \qquad
 \mathcal F_f=\begin{pmatrix}L_{\Phi_f}&\Gamma_f|_N\\0&L_{\Phi_f}\end{pmatrix}.
 \tag{AC4}
\]

This is a continuous multiplicative smooth calculus, unital near K, sending the coordinate to mathcal T.
The identity (z-X)^-1 above shows sigma(X) is contained in K; the same holds for the triangular operator.
Smooth partitions chi_0+chi_1=1 near K, subordinate to any two-set cover, yield closed invariant spaces closure Ran(mathcal F_chi_j) and commuting cutoffs.
A smooth function equal to (x-lambda)^-1 on a neighborhood of the support of chi_j supplies an inverse on that closed range, by multiplicativity.
Hence mathcal T is super-decomposable.
The diagonal calculus proves decomposability of L_X on N by the same argument.
No spectral projection of the nonnormal X is assumed.

For completeness, the no-divisible-subspace step is preserved under this factorization.
The bounded injective map v->Bv sends an X-divisible subspace of H_N to a Y-divisible subspace of ambient H, because BX=YB.
A selfadjoint operator has no nonzero algebraically divisible subspace, as proved by the spectral-measure argument in C_F0069.
The same applies to a divisible subspace of N by first embedding N in H_N.
Thus neither diagonal X module has a nonzero divisible subspace.
Projecting a mathcal T-divisible subspace to the second coordinate, then to the first, proves that mathcal T also has none.
Injectivity of B and diffuseness of Y imply X has no eigenvectors on H_N, so the triangular operator has none either.

Lau88 Proposition 3.7 therefore makes all algebraic spectral subspaces of mathcal T closed.
Theorem 4.1 applies to the algebraic intertwiner J(a)=(E(a),a), since mathcal T J=J L_X is exactly [E,X]=P.
It follows that J, and hence E, is bounded.
This finishes the conditional automatic-continuity argument; it does not construct E or put its adjoint on any bounded vector.

For the hidden-factor model h=2+s_0, S=s_1 free standard semicircular and X=hS, choose A=sqrt(h), B=sqrt(h)S.
Then BA=sqrt(h)S sqrt(h) is selfadjoint, B is injective, and its diffuse law follows from regularity of every X-lambda: each hS-lambda is a nonzero full scalar polynomial in the finite-Fisher semicircular reference tuple, by [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004).
If (Y-lambda)v=0 with lambda nonzero then v=sqrt(h)w with w=lambda^-1 S sqrt(h)v, and (X-lambda)w=0; hence v=0.
At zero, injectivity of both sqrt(h) and S gives ker(Y)=0 directly.
Use the exact three-variable reference of [C_F0147, Section 3](Yin_C_F0147_v1.md#3-polynomial-retraction-proves-maximal-delta): hS-lambda is a nonzero full scalar polynomial there, so its injectivity restricts to the invariant two-variable Hilbert subspace.
The target and reference algebras need not agree.

Thus a hypothetical bare full-domain dual for hS must obey an operator-norm-to-L2 bound, even though hS is nonnormal and the factorization has no bounded inverse.
The actual intrinsic ACSY construction is independently accepted in [C_F0150](Yin_C_F0150_v1.md#statement); it is not a proof premise here.
To exclude F it would still be necessary to contradict this bound on exact target elements; failure of one canonical extension is insufficient.
No such contradiction is established here.
This consequence constrains all bare witnesses but supplies no existence or nonexistence conclusion.


### A precise bounded-dual functional test

The automatic-continuity result makes an exact Banach-space criterion relevant to the same nonnormal candidate.
This criterion alone uses no ACSY hypothesis.
Write bar(H_N) for the conjugate complex Hilbert space, and let P=N tensor_pi bar(H_N), the Banach projective tensor product.
On the linear span V of

\[
 q(a,\eta)=Xa\otimes\bar\eta-a\otimes\overline{X^*\eta},
 \qquad a\in N,\quad\eta\in H_N,
 \tag{AC5}
\]

prescribe the functional

\[
 L\bigl(q(a,\eta)\bigr)=\tau(a)\langle\eta,1\rangle.
 \tag{AC6}
\]

There is a bounded E:N->H_N satisfying [E,X]=P_Omega if and only if this prescription is well-defined and bounded for the norm inherited from P.
The conjugate Hilbert factor is essential for complex linearity under the convention that the inner product is linear in its second variable.

Indeed a bounded E induces the functional F_E(a tensor bar(eta))=<eta,Ea>, of norm ||E||, and the commutator says exactly F_E restricted to V equals L.
Conversely Hahn--Banach extends a bounded L to P with unchanged norm.
For every a, its value on a tensor bar(eta) is a bounded conjugate-linear functional of eta, so Riesz representation produces the unique vector Ea.
Linearity and the projective estimate give a bounded linear map with norm at most ||L||, and testing (AC5) yields the required commutator.
This proves both directions, including all algebraic relations among the generators of V.

For several coordinates, use their corresponding spans and prescriptions separately for each desired dual, with q_j(a,eta)=X_j a tensor bar(eta)-a tensor overline(X_j*eta) and right side delta_ij tau(a)<eta,1>.
An algebraic bare dual need not define a bounded functional without an applicable automatic-continuity theorem.
For X=hS, the preceding factorization argument supplies that implication, so (AC5)-(AC6) is an exact criterion for bare F at this test.
Failure of boundedness would exclude every bare witness; an estimate on a single canonical derivative is not a substitute.

The separate [actual ACSY graph criterion](../drafts/Yin_D_F0005.md#an-exact-target-only-functional-reduction) controls a different Hilbert graph functional on target polynomials.
No estimate transferring that control to the projective norm on all bounded a has been proved.
This is a concrete remaining comparison, not an assertion that Hahn--Banach by itself constructs the desired dual.


## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:21 |
| status | open |
| reason | Complete factorization continuity proof and exact bounded-dual functional criterion; independent review pending. Neither F nor its failure is claimed for the A-positive product. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Automatic norm continuity of every bare dual under the bounded selfadjoint factorization, hS application and exact projective functional criterion. |
| argument | [Argument](#argument) | Explicit C1 and C3 calculi, Hilbert-Schmidt divided differences, spectral and divisible-subspace checks, Lau88 application, concrete injectivity and both functional-criterion directions. |
| dependency | [Published continuity interfaces](../audits/literature/Lau88/Yin_U001.md#lau88-u001) | Proposition 3.7 and Theorem 4.1 with their exact operator and critical-eigenvalue hypotheses. |
| dependency | [Normal triangular method](Yin_C_F0069_v1.md#argument) | Triangular-intertwiner mechanism and absence of nonzero normal divisible subspaces; all extra nonnormal hypotheses are proved here. |
| dependency | [Full-polynomial reference input](Yin_C_F0147_v1.md#3-polynomial-retraction-proves-maximal-delta) | Reference three-semicircular full-polynomial injectivity, restricted to hS-lambda and its two-variable Hilbert subspace; no target-A or all-bare-F conclusion imported. |
