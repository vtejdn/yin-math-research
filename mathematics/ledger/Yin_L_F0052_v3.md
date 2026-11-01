---
author: Yin
---
# A bounded module counterexample with a single uniformly distributed selfadjoint generator

Record kind: research operation.
Date and owner: 2026-10-16T02:59, Yin; construction and complete local hypothesis check by the authoring AI agent.
The user asked whether the diffuse counterexample can use one selfadjoint generator and whether absolute continuity of its law restores the proposed conclusion.
This version answers both questions with x(t)=t in L-infinity([0,1],dt), whose law is exactly Lebesgue probability measure.
The [preceding version](Yin_L_F0052_v2.md) retains the one-normal-generator and two-selfadjoint-coordinate constructions, while [v1](Yin_L_F0052_v1.md) retains the original atomic example and the general boundedness and normal-part boundaries.
Those fixed arguments are not rewritten.
The construction below is self-reviewed; no independent review, fixed Claim assessment change or manuscript edit is claimed.

## Current proof home

The complete original argument and its original dates, local-check statements and earlier review descriptions remain below.

## Exact strengthened question and inputs

Let (M,tau) be finite tracial with faithful normal probability trace, H=L2(M,tau), and Omega=1.
The proposed replacement assumes only that E:M to H is bounded, while A in B(H) preserves M Omega, [A,x]=0, B in B(H), and
\[
 [[E,x],A]=[B,x]
\]
on M Omega.
It would conclude that T=[E,A]-B|_{M Omega} is a left W*(x)-module map.
Here x is additionally required to be selfadjoint with nonatomic, or even Lebesgue-absolutely-continuous, spectral distribution.

The construction below has
\[
 M=W^*(x)=L^\infty([0,1],dt),\qquad x(t)=t,\qquad B=0,
\]
and A is left multiplication by a projection.
The map E even preserves M Omega and is bounded from M to M, but T is not a left M-module map.

The preceding weak-star limit construction supplies the mechanism to reuse.
Searches of F-line Claims, drafts and ledger records for nowhere-dense sets, dense open sets and local averaging found no existing construction resolving this stronger question.
Replacing disjoint spectral components by local averages over a dense open complement avoids the need for disjoint translates of a positive-measure set.
The argument uses only the displayed integral estimates, L1--L-infinity duality and a fixed nonprincipal ultrafilter.
No novelty claim is made.

The [CS89 source unit](../audits/literature/CS89/Yin_U001.md#cs89-u001) records the normal-part and ultraweak-closure interface from Section 2, Lemmas 2.2--2.3.
Its scope remains a selected reading, not a full-paper audit.
The [normal-part construction](../claims/Yin_C_F0132_v1.md#1-the-normal-part-and-source-interface) is used only in the explanatory normal-part calculation below; the counterexample itself is independent of that calculation.

## A positive-measure closed set with dense open complement

Let m denote Lebesgue measure on [0,1].
Enumerate the rationals in (0,1) as r_1,r_2,..., and put
\[
 O=\bigcup_{j\ge1}\left((r_j-2^{-j-2},r_j+2^{-j-2})\cap[0,1]\right),
 \qquad K=[0,1]\setminus O.
\]
The set O is relatively open and dense, and
\[
 0<m(O)\le\sum_{j\ge1}2^{-j-1}=\frac12.
\]
Consequently K is closed with empty interior and 1/2 <= m(K) < 1.
Put p=1_K and take
\[
 M=L^\infty([0,1],m),\qquad
 \tau(a)=\int_0^1a(t)\,dt,\qquad
 H=L^2([0,1],m),\qquad \Omega=1,\qquad x(t)=t.
\]
Then x=x*, W*(x)=M, and the spectral law of x is Lebesgue probability measure on [0,1].
In particular the law is absolutely continuous with bounded density, it has no atoms, and x-lambda is regular for every complex lambda.
The projection p=1_K(x) belongs to W*(x) and has nonzero trace, but is not a point spectral projection.

## Local averages and their weak-star limit

For n>=1 and t in [0,1], set
\[
 I_n(t)=(t-1/n,t+1/n)\cap[0,1],
 \qquad d_n(t)=m(O\cap I_n(t)).
\]
Because O is open and dense, d_n(t)>0 for every t.
For a in M define
\[
 F_n(a)(t)
 =p(t)\frac{\displaystyle\int_{O\cap I_n(t)}a(s)\,ds}{d_n(t)}.       \tag{1}
\]
The integrals depend only on the L-infinity class of a.
Their numerator and denominator are measurable functions of t; indeed both are continuous before multiplication by p, by the moving-interval estimate.
Thus (1) defines an element of M without choosing any simultaneous pointwise representatives.

Each F_n is positive and complex-linear, and
\[
 \|F_n(a)\|_\infty\le\|a\|_\infty,\qquad
 F_n(1)=p,\qquad F_n(pa)=0,\qquad pF_n(a)=F_n(a).                  \tag{2}
\]
The localization in (1) also gives
\[
 \|F_n(xa)-xF_n(a)\|_\infty
 \le\frac1n\|a\|_\infty.                                      \tag{3}
\]
More generally, for f in C([0,1]),
\[
 \|F_n(fa)-fF_n(a)\|_\infty
 \le\omega_f(1/n)\|a\|_\infty,                                \tag{4}
\]
where omega_f(epsilon)=sup{|f(s)-f(t)|: |s-t|<=epsilon} tends to zero with epsilon.

Fix a nonprincipal ultrafilter U on the positive integers.
For every a in M define F(a) in M by
\[
 \int_0^1g(t)F(a)(t)\,dt
 =\lim_{n\to U}\int_0^1g(t)F_n(a)(t)\,dt
 \qquad(g\in L^1([0,1])).                                       \tag{5}
\]
The right side is a bounded linear functional on L1 with norm at most ||a||_infinity, so L1--L-infinity duality gives a unique F(a).
The same fixed ultrafilter is used for all a and g.
It follows that F is positive, complex-linear and contractive from M to M.
Multiplication by a fixed bounded function is weak-star continuous, so (2)--(4) yield
\[
 F(1)=p,\qquad F(pa)=0,\qquad pF(a)=F(a),\qquad
 F(xa)=xF(a),\qquad F(fa)=fF(a)\quad(f\in C([0,1])).             \tag{6}
\]
In particular F(f)=pf for every continuous f, even though F(p)=0.

## All hypotheses and the failed module identity

Define
\[
 E(a\Omega)=F(a)\Omega,\qquad A=L_p,\qquad B=0.                  \tag{7}
\]
By the support and contraction properties in (6),
\[
 \|E(a\Omega)\|_2\le m(K)^{1/2}\|a\|_\infty.
\]
Equality holds for a=1, so E:M to H has norm m(K)^{1/2}.
It also preserves M Omega.
The operator A is an orthogonal projection in B(H), preserves M Omega and commutes with x.

Equation (6) gives [E,x]=0.
The required matching identity consequently holds on all M Omega:
\[
 [[E,x],A]=0=[B,x].
\]
All compositions are defined there because A and x preserve M Omega.

However, (6) also gives
\[
 EA=0,\qquad AE=E,\qquad T=[E,A]-B=-E.
\]
Taking a=p in W*(x) and xi=Omega gives
\[
 T(p\Omega)=0,\qquad pT(\Omega)=-p\Omega\ne0.                  \tag{8}
\]
This disproves the module conclusion for one selfadjoint generator with uniform spectral law.

The extra normalization E(Omega)=0 would not repair the implication.
Indeed, replacing E by E-L_p|_{M Omega} preserves boundedness, commutation with x and the commutator with A, while making its value at Omega zero.

## Missing continuity and the singular remainder

For k>=1 put
\[
 f_k(t)=\max\{1-k\operatorname{dist}(t,K),0\}.
\]
Then f_k belongs to C([0,1]), f_k=1 on K, and f_k decreases pointwise to p.
In particular f_k-p tends to zero in L2 and f_k tends ultraweakly to p.
But (6) gives
\[
 E(f_k\Omega)=p\Omega,\qquad E(p\Omega)=0,\qquad
 E((f_k-p)\Omega)=p\Omega\ne0.                                 \tag{9}
\]
Thus E is not ultraweak-to-weak continuous and is not closable on M Omega as an operator in H.
Its boundedness from M to H does not supply boundedness on H.

For the normal-part explanation, put R=N(E), using the normal-part map from C_F0132.
Compatibility with bounded postcomposition and precomposition by left multiplication gives
\[
 [R,x]=0,\qquad AR=R,\qquad RA=0.
\]
Since R is ultraweak-to-weak continuous and x=x*, commutation first holds for polynomials in x and then extends to W*(x)=M by ultraweak continuity.
Therefore R(aOmega)=aR(Omega) for every a in M.
It follows that
\[
 R(\Omega)=pR(\Omega)=R(p\Omega)=0,
\]
hence R=0.
All of E and T=-E is singular in this normal-part decomposition.

Absolute continuity of the law of x controls its scalar spectral measure.
It does not impose ultraweak continuity on arbitrary bounded maps from M to H.
Here local averaging is normalized only by the measure of the dense open complement in each small interval, which may be much smaller than the whole interval.
The explicit sequence (9) exhibits the resulting failure of L2 continuity and of the required Borel-functional-calculus passage.

## Outcome and checking scope

The boundedness substitution fails with a single selfadjoint generator whose law is exactly Lebesgue probability measure on [0,1].
This simultaneously resolves the single-selfadjoint nonatomic question and its absolute-continuity strengthening.
The failure occurs already in a diffuse abelian algebra with A a left multiplier and E preserving M Omega.
The current ultraweak-to-weak hypothesis cannot be replaced solely by boundedness plus either of these spectral conditions.

The construction of K, positivity of all denominators, measurable well-definedness, the bounds and ultrafilter limit, exact commutation, all domain assumptions, the failed module equality and the normal-part calculation were checked locally.
The source scope used above remains the recorded selected CS89 reading and the existing C_F0132 interface.
No independent mathematical review or Claim adoption occurred.
The manuscript was not modified.
