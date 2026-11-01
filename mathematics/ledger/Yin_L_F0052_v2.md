---
author: Yin
---
# Diffuse counterexamples to the bounded von Neumann module conclusion

Record kind: research operation.
Date and owner: 2026-10-16T02:45, Yin; construction and complete local hypothesis check by the authoring AI agent.
The user asked whether nonatomic spectral distributions remove the obstruction in [the preceding version](Yin_L_F0052_v1.md).
This version answers that strengthened question with a diffuse counterexample and a variant with two selfadjoint coordinates whose individual distributions are absolutely continuous.
The preceding atomic construction, general boundedness consequences and precomposition caveat remain at their original fixed locator.
The arguments below are self-reviewed; no independent review, fixed Claim assessment change or manuscript edit is claimed.

## Current proof home

The complete original argument and its original dates, local-check statements and earlier review descriptions remain below.

## Question and reused inputs

Let (M,tau) be finite tracial with faithful normal probability trace, let H=L2(M,tau), and identify M with M Omega.
Suppose x_1,...,x_m are normal with nonatomic spectral distributions, E_i:M to H are bounded linear maps, and A_i in B(H) preserve M Omega and commute with every x_j.
Assume that B in B(H) satisfies
\[
 \sum_i [[E_i,x_j],A_i]=[B,x_j]\qquad(1\le j\le m)
\]
on M Omega.
The proposed conclusion is that
\[
 T:=\sum_i[E_i,A_i]-B|_{M\Omega}
\]
is a left W*(x_1,...,x_m)-module map.
This conclusion is false even for one normal generator of a diffuse abelian M, with one E and A equal to left multiplication by a projection.
The second construction also shows failure when every coordinate is selfadjoint and has an absolutely continuous spectral distribution.

The atomic construction in the preceding version supplies the mechanism: transfer bounded data from infinitely many small trace components to a fixed component, without ultraweak continuity.
Local F-line searches for diffuse module obstructions and weak-star ultrafilter limits found no existing diffuse construction covering this question.
The [normal-part construction](../claims/Yin_C_F0132_v1.md#1-the-normal-part-and-source-interface) is used only to identify the surviving singular part; the counterexample itself does not depend on that construction.
The [CS89 normal-part and balancing interface](../audits/literature/CS89/Yin_U001.md#cs89-u001), particularly the source's Lemmas 2.2--2.3 on pp.57--58, was rechecked against the publisher PDF.
It passes balancing to the normal part and its ultraweak closure, without asserting that the original bounded map equals its normal part.
No literature novelty claim or new external theorem is adopted.

## A bounded weak-star limit map

Let N=L-infinity([0,1],dt), write u(t)=t, and set
\[
 M:=\ell^\infty(\mathbb N_0;N),\qquad
 \tau(a):=\sum_{n=0}^{\infty}2^{-n-1}\int_0^1 a_n(t)\,dt,
 \qquad H:=L^2(M,\tau),\quad\Omega:=1.
\]
The algebra M is diffuse and abelian, and tau is a faithful normal probability trace.
Put
\[
 \delta_0=0,\qquad \delta_n=1/n\quad(n\ge1),\qquad
 p=(1,0,0,\ldots).
\]
Fix a nonprincipal ultrafilter U on the positive integers.
For a=(a_n) in M, define Q(a) in N by
\[
 \int_0^1g(t)Q(a)(t)\,dt
 :=\lim_{n\to U}\int_0^1g(t)a_n(t)\,dt
 \qquad(g\in L^1([0,1])).                         \tag{1}
\]
The right side is a bounded linear functional of g with norm at most sup_n ||a_n||_infinity, so the duality (L1)*=L-infinity gives a unique Q(a).
Using the same ultrafilter for every a and g makes Q complex-linear.
It is positive and contractive, Q(1)=1, and Q(pa)=0 for every a.
For f in N, multiplication of the test function g by f gives
\[
 Q((f a_n)_n)=fQ(a).
\]
Since delta_n tends to zero, the same definition and the estimate
\[
 \left|\int_0^1g\,\delta_na_n\,dt\right|
 \le\delta_n\|g\|_1\|a\|
\]
give Q((delta_n a_n)_n)=0.
The construction uses equivalence classes in L-infinity through the L1 pairing, so it requires no simultaneous choice of pointwise representatives.

Define
\[
 E(a\Omega):=(Q(a),0,0,\ldots)\Omega,\qquad
 A:=L_p\in B(H),\qquad B:=0.                     \tag{2}
\]
Then
\[
 \|E(a\Omega)\|_2
 =2^{-1/2}\|Q(a)\|_{L^2([0,1])}
 \le2^{-1/2}\|a\|.
\]
Equality holds for a=1, so E:M to H has norm 2^{-1/2}.
It even maps M Omega into M Omega and is contractive as a map from M to M.
The operator A is an orthogonal projection on H, preserves M Omega and commutes with every left multiplier from M.

## One normal generator with nonatomic distribution

Let
\[
 x_n(t):=t+\mathrm i\delta_n\qquad(n\ge0).
\]
This defines a bounded normal x in M.
Its spectral distribution is
\[
 \mu_x=\sum_{n=0}^{\infty}2^{-n-1}
       (t\mapsto t+\mathrm i\delta_n)_*(dt).
\]
Each summand has no point masses, so mu_x is nonatomic.
In particular x-lambda is regular for every complex lambda: its kernel projection is 1_{\{lambda\}}(x)=0, and normality gives dense range.
The supports [0,1]+i delta_n are pairwise disjoint, and
\[
 p=1_{[0,1]}(x)\in W^*(x).                       \tag{3}
\]
In fact W*(x)=M.
Indeed, each component projection is the spectral projection of x onto its horizontal segment, and the real coordinate t generates the L-infinity algebra on each component.
Taking bounded strong limits of finite component sums gives every element of M.

For a in M, formula (1) gives
\[
 Q(xa)=uQ(a),\qquad
 E(xa\Omega)=(uQ(a),0,\ldots)\Omega=xE(a\Omega).
\]
Thus [E,x]=0, and the matching identity is satisfied:
\[
 [[E,x],A]=0=[B,x].                               \tag{4}
\]
All remaining operator-domain assumptions hold by (2).
However,
\[
 EA=0,\qquad AE=E,\qquad T=[E,A]-B=-E,
\]
and therefore
\[
 T(p\Omega)=0,\qquad pT(\Omega)=-p\Omega\ne0.      \tag{5}
\]
Equations (3)--(5) disprove the proposed conclusion with m=r=1.
The projection p has trace 1/2 but is not a minimal projection, and it is not a point spectral projection of x.
Its entire corner pM is diffuse.

If normalization E(Omega)=0 is additionally requested, replace E by E-L_p|_{M Omega}.
The replacement is still bounded from M to H and commutes with x, while its commutator with A is unchanged.
Thus that normalization would not remove this example.

## Two selfadjoint coordinates with absolutely continuous distributions

Keep M, Q, E, A and B from (1)--(2), and define
\[
 (x_1)_n(t)=t,\qquad (x_2)_n(t)=t+\delta_n.
\]
Both coordinates are bounded and selfadjoint.
The law of x_1 is uniform on [0,1], and the law of x_2 has Lebesgue density
\[
 \rho(s)=\sum_{n=0}^{\infty}2^{-n-1}
                    1_{[\delta_n,1+\delta_n]}(s).
\]
Thus both individual spectral distributions are absolutely continuous and in particular nonatomic.
The properties of Q give [E,x_1]=[E,x_2]=0, so both matching identities hold with r=1 and B=0.
Moreover,
\[
 p=1_{\{0\}}(x_2-x_1)\in W^*(x_1,x_2)=M.
\]
The same calculation (5) disproves the module conclusion.
The difference x_2-x_1 has atomic distribution, but neither assumed coordinate does.
The first construction already supplies a single normal generator whose own distribution is nonatomic; the second isolates the additional selfadjoint-coordinate restriction.

## Why the normal-part reduction does not remove the obstruction

Let q_N be the sum of the component projections indexed by 0,...,N.
Then q_N increases strongly and ultraweakly to 1, but
\[
 E(q_Na\Omega)=0\quad(a\in M),\qquad E(\Omega)=p\Omega.
\]
In particular E is not ultraweak-to-weak continuous.
Also ||(1-q_N)Omega||_2 tends to zero while E((1-q_N)Omega)=pOmega, so E is not closable as an operator on M Omega in H.
Boundedness from M to H therefore must not be confused with boundedness on H.

Write E_n for its normal part.
The normal-part construction commutes with precomposition by left multiplication, so E_n(q_NaOmega)=0 for every N and a.
Ultraweak-to-weak continuity of E_n and q_Na tending ultraweakly to a yield E_n=0.
Consequently T_n=0 and all of T=-E is the singular remainder.
This remainder commutes with x and x* in the one-generator construction but does not commute with p in W*(x).

The precise failure of the functional-calculus limit is also explicit.
On the spectrum of the one-generator x, let
\[
 f_k(z):=\max\{1-k|\operatorname{Im}z|,0\}.
\]
The continuous functions f_k have values in [0,1], and f_k(x) tends strongly to p.
For each fixed k, the values f_k(t+i/n) tend uniformly in t to 1 as n tends to infinity.
Hence
\[
 E(f_k(x)\Omega)=p\Omega\quad\text{for every }k,
 \qquad E(p\Omega)=0.
\]
Thus commutation with continuous functional calculus does not extend to this Borel spectral projection despite the absence of point masses.

The bounded-map Fuglede implication only transfers commutation with x to commutation with x*.
The singular remainder here already has both commutations, so that implication has no further cancellation to supply.
Nonatomicity does not bridge the missing ultraweak continuity.

## Consequence and review scope

The proposed boundedness substitution fails under the additional requirement that every normal coordinate have nonatomic spectral distribution.
It fails even in a diffuse abelian algebra generated by the displayed coordinates, with A a left multiplier and E preserving M Omega.
The second example strengthens the coordinate condition to selfadjointness and absolute continuity of every individual law.
These examples address the stated commutator-module hypothesis, without imposing additional free-difference-quotient, conjugate-variable or derivation assumptions.
They do not claim a counterexample with such additional structure.

The construction of Q, all boundedness and domain conditions, the spectral distributions, generation, matching identities, explicit failed module equality and normal-part calculation were checked locally in full.
No independent mathematical review or Claim adoption occurred.
The current manuscript was not modified.
