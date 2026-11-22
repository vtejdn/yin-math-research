---
author: Yin
---

# Counterexamples with bounded dual systems

This alternative proof treats the bounded-dual part of the [selfadjoint example in v1](Yin_C_F0012_v1.md#statement).
It derives the change of generators from the duals for the original free pair and uses the same bounded last-two-factor operator as v1.
The norm-separation argument remains in [v1, Section 6](Yin_C_F0012_v1.md#6-exclusion-from-the-norm-closed-and-scalar-division-algebras).

## Current assessment
[Selected decision](Yin_C_F0012_v3.md#decision-quadratic-independently-reviewed)

## Statement

Let \((M,\tau)\) be a finite tracial von Neumann algebra with faithful trace, let \(H=L^2(M,\tau)\), and let \(P_\Omega\) be the projection onto the vacuum line.
Let \(X,S\in M\) be selfadjoint, with \(X\geq 0\) injective and \(q:=X^{-1}\Omega\in H\).
Write \(Y=XSX\), and suppose \(T\) is bounded with \([X,T]=P_\Omega\) and \([S,T]=0\).
With \(\rho(a)\) denoting right multiplication by \(a\), a bounded operator \(D_2\) commuting with \(X\) satisfies \([Y,D_2]=P_\Omega\) exactly when
\[
 [S,D_2]\xi=q\langle q,\xi\rangle\quad(\xi\in H).
\]
In that case the bounded operator
\[
 D_1=T-\rho(XS)D_2-D_2\rho(SX)
\]
makes \((D_1,D_2)\) a generator-first dual system for \((X,Y)\).

In the selfadjoint sandwich example, \(X\) has law \(d\mu(t)=4t^3\,dt\) on \((0,1)\), \(S\) is a standard semicircular element free from \(X\), and \(M=W^*(X,S)\).
For this pair \(W^*(X,Y)=M\), and there are bounded \(T,D_2\) satisfying the stated hypotheses.
In the tensor model below, \(r\) is the creation operator appending the unit vector \(1\) at the right end.
The direct composition \(\rho(X)^{-1}r\rho(X)^{-1}\) is unbounded on its natural domain.

## Argument

### The rank-one commutator after the change of generators

The product rule gives
\[
 [Y,T]=XSP_\Omega+P_\Omega SX,
 \qquad
 [Y,D_2]=X[S,D_2]X
\]
whenever \([X,D_2]=0\).
Since \(X=X^*\) and \(Xq=\Omega\), multiplying \(q\langle q,\cdot\rangle\) on both sides by \(X\) gives \(P_\Omega\).
If \(X[S,D_2]X=P_\Omega\), the bounded operator \([S,D_2]-q\langle q,\cdot\rangle\) therefore vanishes on \(\operatorname{ran}X\) by injectivity of \(X\).
The range is dense because \(X\) is selfadjoint and injective, proving the reverse implication.

Right multiplications commute with all left multipliers, so the two correction terms in \(D_1\) commute with \(X\), and \([X,D_1]=P_\Omega\).
Their commutators with \(Y\) are \(\rho(XS)P_\Omega\) and \(P_\Omega\rho(SX)\).
The first equals \(XSP_\Omega\) because \(\rho(XS)\Omega=XS\Omega\).
The second equals \(P_\Omega SX\) by traciality.
This proves \([Y,D_1]=0\), and the other two dual equations are those of \(D_2\).

### Original free pair and the inverse weights

In the example, the [standard tracial tensor model of v1](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) identifies \(H\) with \(\bigoplus_{n\geq0} H_n\), where \(H_n=K^{\bar\otimes(n+1)}\) and \(K=L^2((0,1),\mu)\).
The vacuum is \(1\) in \(H_0\), \(X\) multiplies the first factor by the coordinate, and \(\rho(X)\) does so on the last factor.
Left semicircular multiplication is \(S=l+l^*\), where \(l\) prepends \(1\).
The bounded scalar dual and its last-factor lift in [v1, Section 3](Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction) apply with this measure and model.
Taking \(T=-\widehat D_h\) converts its commutator \([\widehat D_h,h]=P_\Omega\) to \([X,T]=P_\Omega\) and preserves \([S,T]=0\).

Right creation \(r\) commutes with \(X\) and \(l\) because it appends a factor.
On positive degrees it also commutes with \(l^*\), which contracts the first factor.
On \(H_0\), \(l^*r\xi=\langle1,\xi\rangle1\) and \(rl^*\xi=0\), so \([S,r]=P_\Omega\).
Thus \((T,r)\) is a bounded dual system for \((X,S)\), and \([Y,r]=XP_\Omega X\).
The other commutator \([Y,T]\) acts on \(\Omega\) as \(XS\Omega\) because \(\tau(SX)=0\).
This vector is nonzero by injectivity of \(X\) and \(\|S\Omega\|_2=1\).

Here \(q(t)=1/t\) in \(K\), and \(\|q\|_2^2=4\int_0^1t\,dt=2\).
Define \(Q=\rho(X)^{-1}\) by spectral calculus.
It is selfadjoint with \(Q\Omega=q\).
The natural domain of \(QrQ\) is \(\operatorname{Dom}Q\), since \(r\) appends \(1\) and applying \(Q\) to that last factor appends \(q\in K\).
The domain is preserved by left multiplication by \(X\) and \(S\) because these commute with the spectral projections of \(\rho(X)\).
On this domain the commutator with \(X\) vanishes, and
\[
 [S,QrQ]\xi=Q[S,r]Q\,\xi=QP_\Omega Q\,\xi=q\langle q,\xi\rangle.
\]
Here \(Q\) commutes with left \(S\) on its domain, and \(Q\Omega=q\) gives the last equality by selfadjointness of \(Q\).
This gives the weight required in the first part of the proof.
The direct composition with \(r\) satisfies \(QrQf=(qf)\otimes q\) for bounded \(f\in H_0=K\).
Both inverse multiplications are defined there because \(qf,q\in K\).
For unit \(f\) supported in \((\varepsilon/2,\varepsilon]\), this vector has norm at least \(\|q\|_2/\varepsilon\).
Thus the composition is unbounded.

### The bounded second dual

For almost every \((s,t)\), decompose \(q(s)q(t)=k(s,t)+k(t,s)\), where
\[
 k(s,t)=\frac{1_{\{t\leq s\}}}{st},\qquad
 (T_1\zeta)(s)=\int_0^1 k(s,t)\zeta(s,t)\,d\mu(t).
\]
The diagonal has zero product measure.
The bound \(\int_0^1 |k(s,t)|^2\,d\mu(t)=4s^{-2}\int_0^s t\,dt=2\) and Cauchy–Schwarz give \(\|T_1\|\leq\sqrt2\) from \(K\bar\otimes K\) to \(K\).
Let \(R\) act by this map on the final two factors of every \(H_n\) with \(n\geq 1\), and let \(R=0\) on \(H_0\).
Its output grades are orthogonal, so \(\|R\|\leq\sqrt2\).
It commutes with \(X\), including on \(H_1\) because \(T_1\) preserves multiplication in \(s\).

The commutator \([R,l]\) vanishes on positive grades, where its two actions occur at opposite ends.
On \(H_0\) it maps \(\xi\) to \(T_1(1\otimes\xi)\), the integral operator with kernel \(k\).
The two maps in \([R,l^*]\) vanish on \(H_0\) and \(H_1\), and commute on higher grades because their affected factors are disjoint.
Consequently \([R,S]\) has kernel \(k\) on \(H_0\) and vanishes on the higher grades.
With \(D_2=R^*-R\), selfadjointness of \(S\) gives
\[
 [S,D_2]=[R,S]^*+[R,S]=q\langle q,\cdot\rangle .
\]
The adjoint \(R^*\) commutes with selfadjoint \(X\) as well, so this \(D_2\) satisfies the two required equations.
The first part gives the bounded \(D_1\) and verifies its two equations.

Finally, \(e_\varepsilon=1_{[\varepsilon,1]}(X)\) converges strongly to \(1\) as \(\varepsilon\rightarrow0\) because the law of \(X\) has no atom at zero.
The bounded element \(a_\varepsilon=X^{-1}e_\varepsilon\) belongs to \(W^*(X)\).
Since \(a_\varepsilon Ya_\varepsilon=e_\varepsilon S e_\varepsilon\rightarrow S\) strongly, \(W^*(X,Y)=W^*(X,S)\).

## Assessment history

### Decision sandwich-coordinate-change

| Field | Value |
| --- | --- |
| date | 2026-11-22T07:14 |
| status | proved |
| reason | The completed self-review verifies the rank-one equivalence, the actual inverse-weight calculation, the bounded half-kernel, the correction of the first dual and the generation argument. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact transfer for \(Y=XSX\), bounded duals for the specified free pair after the change of generators, and failure of boundedness for direct right-multiplier composition. |
| argument | [Argument](#argument) | All coordinate commutators and domain calculations, bounded last-two-factor construction and strong generation. |
| support | [v1 tracial model](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | Identical free model, measure and standard-space identification with left and right multiplication. |
| support | [v1 scalar dual](Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction) | Boundedness and commutation of the scalar dual and its last-factor lift, with the sign converted in v4. |
| review | [Whole-proof self-review](../audits/reviews/Yin_R_F0056_v4.md#sandwich-coordinate-change-finding) | Complete v4 statement, argument and fixed input interfaces. |
