---
author: Yin
---
# An actual vacuum for a semicircular product with a singular positive factor

Human author: Yin.
Root supplied the one-coordinate candidate, the Moore--Penrose coefficient choice and its inverse-trace integrability route.
The general ACSY-to-full-domain branch established the separated-leg actual-adjoint restriction, checked the whole-core vacuum and intrinsic target compression, and fixed this proof.
Both are developers, not independent reviewers.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let s_0,S be freely independent standard variance-one semicircular elements in a finite tracial von Neumann algebra with faithful normal probability trace.
Set tilde M=W*(s_0,S), H=L2(tilde M), h=2+s_0, X=hS and N=W*(X), with the restricted trace.
Then the intrinsic target condition A(N;X) holds: there is a complex-linear represented derivation

\[
 \delta_N:\mathbb C\langle X,X^*\rangle
       \longrightarrow L^2(N)\otimes_2 L^2(N),
 \qquad \delta_NX=1\otimes1,\qquad
 1\otimes1\in\operatorname{Dom}\delta_N^*.
\]

Its actual vacuum can be chosen with norm at most sqrt(2).
The starred generator value is an actual Hilbert tensor.
Inner products are linear in their second variable and the coefficient actions are outer.
No reality condition or larger target derivation domain is imposed.

More precisely, in the closed oriented tensor subspace K_01=L2(W*(h)) tensor_2 L2(W*(S)), let

\[
 \alpha(u,v)=\frac{v}{u^2+v^2},\qquad
 \beta(u,v)=\frac{u}{u^2+v^2},
\]

where u and v denote the first h variable and second S variable.
Then ||alpha||_2^2+||beta||_2^2<=1 and both coefficients belong to the actual domains of both reference adjoints partial_h* and partial_S*.
The reference derivation delta=I_alpha partial_h+I_beta partial_S on C<h,S> has actual vacuum

\[
 v_0=\partial_h^*\alpha+\partial_S^*\beta,\qquad
 \|v_0\|_2\le\sqrt2.
\]

With Q_N the trace-preserving conditional-expectation projection onto L2(N), the target derivation is (Q_N tensor Q_N)delta restricted to its target star core, with actual vacuum Q_N v_0.

Here h is regular and h^-1 is not in L2, while tau(h^-1)=1.
The result does not assert either existence or nonexistence of a bare full-N dual, or full bounded-vector domains of the specified canonical contraction or its adjoint.
In particular this is not an A-to-F separation theorem.

## Argument

The reused input is the standard Fock model and word-cut formula from [Miy22-U001](../audits/literature/Miy22/Yin_U001.md#miy22-u001) and [C_F0144's word-cut argument](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint).
A local search by separated legs, two-block adjoints and earlier kernel constructions found no existing result at this oriented two-factor scope.
C_F0139 treats coefficients in the derivative's kernel algebra, while C_F0145's general relative-degree summability is stronger than what is verified below.
The bounded adjoint restriction here follows directly from the same exact word-cut formula, with no external approximation theorem.

### 1. An isometric restriction of both actual reference adjoints

The reference derivatives are normalized by partial_h h=1 tensor 1, partial_h S=0, partial_S h=0 and partial_S S=1 tensor 1 on C<h,S>.
Put H_0=L2(W*(h)), H_1=L2(W*(S)), and let K_01=H_0 tensor_2 H_1, viewed as a closed subspace of the ambient coarse Hilbert space.
With U_m the monic semicircular Chebyshev polynomials, its orthonormal tensor basis is U_m(s_0) tensor U_n(S), m,n>=0.
Inserting one letter in the word-cut adjoint gives

\[
 \partial_h^*(U_m(s_0)\otimes U_n(S))
       =U_{m+1}(s_0)U_n(S),\qquad
 \partial_S^*(U_m(s_0)\otimes U_n(S))
       =U_m(s_0)U_{n+1}(S).
 \tag{1}
\]

For either map, the resulting words are distinct as (m,n) varies, so each map extends to an isometry from K_01 into the ambient H.
Testing the word-cut formula against every reference Wick polynomial proves the actual adjoint pairing with this bounded output.
Thus all of K_01 belongs to BOTH actual adjoint domains, and

\[
 \|\partial_h^*\eta\|_2=\|\eta\|_2,
 \qquad \|\partial_S^*\eta\|_2=\|\eta\|_2,
 \qquad \eta\in K_{01}.
 \tag{2}
\]

This is a statement on the full mixed polynomial core, not merely on scalar marginal test functions.
It allows arbitrarily many letters in each of the two pure blocks.
It does not assert a bounded adjoint on the entire coarse space.

### 2. Hilbert coefficients for the normalized product derivative

In the commuting tensor variables u=h in the first leg and v=S in the second, define

\[
 \alpha(u,v)=\frac{v}{u^2+v^2},\qquad
 \beta(u,v)=\frac{u}{u^2+v^2}.
 \tag{3}
\]

The product-null point u=v=0 is irrelevant.
Both coefficients are real and hence fixed by componentwise adjoint.
The semicircular density of v is at most 1/pi, so for u>0

\[
 \int\frac{d\mu_S(v)}{u^2+v^2}
   \le\frac1\pi\int_{\mathbb R}\frac{dv}{u^2+v^2}
   =\frac1u.
\]

The shifted semicircular law has density sqrt(u(4-u))/(2 pi) on (0,4), so tau(h^-1)=1 by the substitution u=4 sin^2 theta.
Its mass at zero is zero, proving regularity; the inverse-square integral diverges because its integrand has order u^(-3/2) near zero.
Consequently

\[
 I:=\|\alpha\|_2^2+\|\beta\|_2^2
   =\iint\frac{d\mu_h(u)d\mu_S(v)}{u^2+v^2}
   \le1.
 \tag{4}
\]

These are actual coarse Hilbert coefficients even though h^-1 is not a Hilbert vector.
For a bounded elementary tensor a tensor b define I_eta(a tensor b)=a dot eta dot b, extending by linearity on algebraic tensors.
Define on the represented full reference star algebra A_0=C<h,S>

\[
 \delta p=I_\alpha\partial_h p+I_\beta\partial_S p.
 \tag{5}
\]

For each p the reference derivatives are finite tensors with bounded polynomial legs, so the two outer insertions in (5) are genuine Hilbert tensors.
Insertion commutes with the outer bimodule action, hence this is a represented complex-linear derivation.
Its generator values are delta h=alpha and delta S=beta.
The commuting-variable identity v alpha+u beta=1 gives

\[
 \delta X=\alpha\mathbin{\cdot}S+h\mathbin{\cdot}\beta
          =1\otimes1,\qquad
 \delta X^*=\beta\mathbin{\cdot}h+S\mathbin{\cdot}\alpha
          \in H\otimes_2H.
 \tag{6}
\]

No reality assumption is being made.
The second formula is part of the full reference derivation and is not an arbitrarily assigned formal starred value.

### 3. The actual vacuum on the entire reference core

For every p in A_0 the finite-coefficient vacuum pairing gives

\[
 \langle1,\delta p\rangle
   =\langle\alpha,\partial_h p\rangle
       +\langle\beta,\partial_S p\rangle
   =\langle v_0,p\rangle,\qquad
 v_0=\partial_h^*\alpha+\partial_S^*\beta,
 \quad \|v_0\|_2\le\sqrt{2I}\le\sqrt2.
 \tag{7}
\]

The first equality follows from traciality on elementary tensors and Hilbert continuity; alpha*=alpha and beta*=beta are used.
Equations (1)--(2) establish the actual adjoint membership on the entire reference core, so (7) proves 1 tensor 1 in Dom delta*, not a distributional identity.

### 4. Intrinsic target coefficients and actual adjoint

Finally let Q_N be trace-preserving conditional expectation on L2 and restrict p to C<X,X*>.
The map

\[
 \delta_Np=(Q_N\otimes Q_N)\delta p
 \tag{8}
\]

is an outer derivation into L2(N) tensor_2 L2(N), by N-bimodularity of conditional expectation.
It satisfies delta_NX=1 tensor 1, has an actual Hilbert starred value by (6), and has actual vacuum Q_N v_0 by (7).
This proves A(N;X) with the correct intrinsic target coefficient module, without asserting that N is the reference algebra.

## Scope of the construction

The ordinary one-sided coefficient h^-1 tensor 1 would fail to be a coarse Hilbert vector.
The two coefficients used here instead satisfy the exact equation alpha dot S+h dot beta=1 tensor 1 and both actual adjoint tests.
This uses the hidden reference factor without imposing any target domain containing h or S.
The target restriction keeps the intrinsic smaller coefficient module and projects the vacuum; equality N=tilde M is not assumed.

The compression convention is compatible with the exact restriction boundary recorded in [CN21-U001](../audits/literature/CN21/Yin_U001.md#cn21-u001).
Its correction is not an unproved premise here: bimodularity and the actual pairings are checked directly in Section 4.
No external transfer of full-domain duals, dimension inequality or uniform Jacobian inverse is used.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:14 |
| status | open |
| reason | Complete separated-leg actual-adjoint construction gives an intrinsic whole-star-core ACSY witness for hS although h inverse is not L2; no full-domain dual conclusion is claimed. Independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Concrete one-coordinate intrinsic actual-vacuum derivation, coefficient integrability, both actual reference adjoints, norm bound and explicit full-domain limitation. |
| argument | [Argument](#argument) | All four sections: oriented tensor adjoints, integrable coefficients, actual reference vacuum and target conditional-expectation compression. |
| dependency | [Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Standard normalization, faithful trace, Wick word orthonormality and reversal. |
| dependency | [Exact reference word cuts](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) | The polynomial word-cut identity for each free semicircular derivative, proved there from the recurrence. No finite-degree bound or nonlinear target theorem is transferred. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:19 |
| status | proved |
| reason | Adopt the intrinsic actual-vacuum construction after R_F0156 independently checked the entire four-section proof, both direct dependencies and the named source-comparison boundary. Existence or nonexistence of a full-domain dual remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Concrete one-coordinate intrinsic actual-vacuum derivation, coefficient integrability, both actual reference adjoints, norm bound and explicit full-domain limitation. |
| argument | [Argument](#argument) | All four sections: oriented tensor adjoints, integrable coefficients, actual reference vacuum and target conditional-expectation compression. |
| dependency | [Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Standard normalization, faithful trace, Wick word orthonormality and reversal. |
| dependency | [Exact reference word cuts](Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) | The polynomial word-cut identity for each free semicircular derivative, proved there from the recurrence. No finite-degree bound or nonlinear target theorem is transferred. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0156_v1.md#conclusion) | Entire statement and proof, actual separated-leg adjoints, coefficient integrability, whole-core vacuum, intrinsic target compression and all exact source interfaces. |

