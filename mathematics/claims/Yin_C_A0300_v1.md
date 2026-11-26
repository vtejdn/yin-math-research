---
author: Yin
---

# Distinct double poles are impossible at the order-twenty-four half kernel

## Statement

Under the [order-24 half-rank hypotheses](Yin_C_A0290_v1.md#statement), every unit-circle zero of each of the two determinants \(\det(Az+B)\) and \(\det(Cz+D)\) is simple.
Each determinant has at least one such zero.
In particular an entire multiplicity pattern is excluded for the original regular transfer, even when the numerator and denominator double zeros are distinct.

Indeed [the two-factor pole bound](Yin_C_A0290_v1.md#statement) makes any boundary double zero require one in each determinant, and [the common-root argument](Yin_C_A0294_v1.md#statement) excludes coinciding roots.
In the remaining double case the [two-sided diagonal form](Yin_C_A0292_v1.md#the-two-rational-forms) gives, in a constant basis,
\[
    M(z)=D(z)E D(z),\qquad
    D(z)={\rm diag}(1,u(z)),\qquad u(z)=\frac{z-\beta}{z-\alpha},
    \qquad E=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
with distinct unit scalars \(\alpha,\beta\), \(ad\ne0\), and \(\det E\ne0\).
We prove that this form contradicts the [fourth-power identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) in \(U(H)\).
Existence of a unit-circle zero on each side is the [six-evaluation obstruction](Yin_C_A0244_v1.md#statement).

## Scalar equations from two off-diagonal entries

Both \(b,c\) are nonzero, since otherwise the transfer has a constant invariant line, excluded by the [four-column reduction](Yin_C_A0184_v1.md#statement).
Set \(x=s^{-1},\ u=u(t),\ q=bc/(ad),\ k=(1-q)^{-2}\).
Thus \(q\ne0,1\).
Conjugating \(xM(t)\) by \(D(t)\) gives \({\rm diag}(x,u x u)E\).
A further constant diagonal conjugation whose first to second entry ratio is \(a/b\) yields
\[
       T=\begin{pmatrix}X&X\\qY&Y\end{pmatrix},\qquad
       X=ax,\quad Y=d u x u,\quad T^4=I.
\]
All \(X,Y\) are affiliated units.
Set \(Z=X+Y\).
This too is a unit.
In fact \((t-\alpha)Z(t-\alpha)\) is the group-ring scalar
\[
                  a(t-\alpha)x(t-\alpha)+d(t-\beta)x(t-\beta).
\]
Its four possible labels \(t^i x t^j\), \(0\le i,j\le1\), are distinct by the [trivial intersection of neighboring cyclic groups](Yin_C_A0290_v1.md#applying-the-four-step-identity), after moving \(x\) to the right.
If the scalar vanished the coefficients would give \(a+d=0\) and \(a\alpha+d\beta=0\), impossible.
Scalar injectivity in the finite affiliated algebra makes this nonzero scalar a unit, and the two end factors already are units.

Use \(T^2=T^{-2}\) and
\[
      T^{-1}=(1-q)^{-1}
        \begin{pmatrix}X^{-1}&-Y^{-1}\\-qX^{-1}&Y^{-1}\end{pmatrix}.
\]
Right multiplication of the upper-right and lower-left entry identities by \(Y\) and \(X\), respectively, gives
\[
             XZY=YZX=-k(X^{-1}+Y^{-1}).
\]
Since \(X^{-1}+Y^{-1}=Y^{-1}ZX^{-1}\), the second equality gives \(Y^2ZX^2=-kZ\).
The top-left entry of the same matrix identity gives
\[
 \begin{aligned}
 (1-q)X^2+qXZ
     &= k\big((1-q)X^{-2}+q(X^{-1}+Y^{-1})X^{-1}\big)\\
     &= k(1-q)X^{-2}-qYZ .
 \end{aligned}
\]
Consequently
\[
          q Z^2=(1-q)P,\qquad P=kX^{-2}-X^2 .
\]
In particular \(Z\) commutes with \(P\), and so does \(Y=Z-X\).

## The commutant of a two-term Laurent polynomial

Let \(w=s^2\), and define
\[
   K=\{h\in H:\ h s^n h^{-1}=s^{\varepsilon n}
                         \text{ for some }n>0,\ \varepsilon\in\{1,-1\}\}.
\]
Common multiples show that \(K\) is a subgroup, with the unique sign defining a homomorphism, since \(s\) has infinite order.
For any \(P_0=A_0 w+B_0 w^{-1}\) with two nonzero scalar coefficients, every affiliated scalar commuting with \(P_0\) is affiliated over \(K\).
If \(K\) has no elements of negative sign, every such scalar commutes with \(w\).

First let \(V\) be a bounded commuting scalar, regarded as a vector of \(L^2(\mathcal N(H))\).
Left and right multiplication by \(w\) are commuting unitaries \(L_w,R_w\).
The commutation equation factors as
\[
       (L_w-R_w)(A_0 I-B_0 L_w^{-1}R_w^{-1})V=0 .
\]
The two factors are commuting normal operators in the same abelian von Neumann algebra.
The kernel of their product is the sum of the two kernels by their joint spectral projections.
In the first kernel Fourier coefficients are constant along orbits of \(h\mapsto w h w^{-1}\), so nonzero coefficients are supported on finite orbits, in the positive part of \(K\).
The second kernel is zero unless \(|A_0|=|B_0|\).
When equality holds, coefficients have constant moduli along orbits of \(h\mapsto w h w\); a finite orbit there gives \(h w^j h^{-1}=w^{-j}\) for some \(j>0\).
Thus the bounded commuting scalar has Fourier support in \(K\) and belongs to \(\mathcal N(K)\) by the subgroup expectation.
Without any negative elements the second kernel is zero, so \(V\) commutes with \(w\).

For an affiliated scalar \(V\) commuting with \(P_0\), its graph projection \(e\) has affiliated range \(\{(b,Vb): b\in U(H)\}\).
This module is invariant under the bounded normal matrix \(N={\rm diag}(P_0,P_0)\), equivalently \((I-e)Ne=0\).
In a finite tracial algebra this implies \(eN=Ne\): writing \(N\) in two-by-two blocks relative to \(e\), the trace of the first diagonal block of \(NN^*-N^*N\) is \(\|eN(I-e)\|_2^2\), hence zero.
All bounded entries of \(e\) therefore commute with \(P_0\).
Since \(e_{11}=(I+V^*V)^{-1}\) and \(e_{21}=V e_{11}\), the bounded result gives \(V=e_{21}e_{11}^{-1}\in U(K)\).
In the absence of a negative element its two graph entries actually commute with \(w\), giving the second assertion also for \(V\).

## The two-factor support forces the sign to be positive

The polynomial \(P=k a^{-2}s^2-a^2s^{-2}\) has the preceding two-term form, so \(Y\in U(K)\).
As \(s\in K\), we obtain
\[
                 u(t)u(t_{-1})=d^{-1}Yx^{-1}\in U(K),
                        \qquad t_{-1}=s^{-1}ts .
\]
This product already belongs to the affiliated algebra of \(F=\langle t,t_{-1}\rangle\).
The intersection of the two affiliated subgroup algebras inside \(U(H)\) is \(U(K\cap F)\): each bounded graph entry lies in both subgroup von Neumann algebras, so has Fourier support in their intersection, and the graph formula recovers the scalar.
In particular the product is a unit there, since it has zero kernel and dense range in the regular representation.
The [two-factor subgroup theorem](Yin_C_A0272_v1.md#statement) now gives \(F\subseteq K\).
Its cyclic subgroups are infinite and disjoint, and both scalar rational factors \(u(z)\) satisfy the required nonrotation condition since their unique pole \(\alpha\ne0\) cannot be fixed by any nontrivial rotation.
This application uses the trivial right translation in that theorem.

Thus \(K\) contains both generators \(s,t\), and so \(K=H\).
Its sign homomorphism is positive on \(s\); it is positive also on \(t\), since \(t\) has even degree in \(H_{\rm ab}=C_{24}\).
There are no negative elements.
In particular the commutant result applied to \(Y\) now gives \([Y,s^2]=0\), so \(X^2=a^2s^{-2}\) commutes with \(Y,Z\).

## A positive scalar would be a nontrivial group translation

Cancelling the unit \(Z\) on the right in \(Y^2ZX^2=-kZ\) gives \(Y^2=-kX^{-2}\).
Substitution into \(qZ^2=(1-q)P\) then gives
\[
                    XY+YX=P/q .
\]
For \(B_1=XY=ad(xu)^2\) one has \(B_1(YX)=XY^2X=-kI\).
Thus
\[
                       B_1-k B_1^{-1}=P/q .
\]
In particular \(x u\) commutes with \(P\), being a square root of \(B_1/(ad)\).
The same commutant result shows that \(x u\) commutes with \(s^2\).
So does \(u\) itself, and solving its fractional linear expression for \(t\) shows \([t,s^2]=0\) (the scalar \(u-I=(\alpha-\beta)(t-\alpha)^{-1}\) is an affiliated unit).
Therefore \(s^2\) is central in \(H\).

On the Fourier circle \(\overline{u(z)}=(\alpha/\beta)u(z)\), whence \(u^*=(\alpha/\beta)u\).
Since \(x^*=s=s^2x\), centrality yields
\[
                 Y^*=(\overline d/d)(\alpha/\beta)^2 s^2Y .
\]
But \(Y^2=-k a^{-2}s^2\).
The positive affiliated scalar \(Y^*Y\) would therefore equal a nonzero scalar multiple of \(s^4\).
The latter has the full circle of its scalar radius as spectrum in the regular representation, since \(s^4\) has infinite order.
This is impossible for a positive operator and excludes the distinct double roots.

## Assessment history

### Decision distinct-boundary-double-poles

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:54 |
| status | proved |
| reason | Both coincident and distinct double poles are excluded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both coincident and distinct double poles are excluded. |
| argument | [Scalar equations from two off-diagonal entries](#scalar-equations-from-two-off-diagonal-entries) | Scalar equations from two off-diagonal entries. |
| argument | [The commutant of a two-term Laurent polynomial](#the-commutant-of-a-two-term-laurent-polynomial) | The commutant of a two-term Laurent polynomial. |
| argument | [The two-factor support forces the sign to be positive](#the-two-factor-support-forces-the-sign-to-be-positive) | The two-factor support forces the sign to be positive. |
| argument | [A positive scalar would be a nontrivial group translation](#a-positive-scalar-would-be-a-nontrivial-group-translation) | A positive scalar would be a nontrivial group translation. |
| review | [Distinct boundary double poles](../audits/reviews/Yin_R_A0216_v1.md#distinct-boundary-double-poles) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-distinct-boundary-double-poles)
