---
author: Yin
---

# Attainment and upper semicontinuity of the largest fractional nullity on two marks

## Statement

For a torsion-free group \(H=\langle s,t\rangle\) on two ordered marks, suppose every nonzero scalar in \(\mathbb CH\) is injective in the regular representation.
Let \(\Delta(H;s,t)\) be the supremum of zero and of all noninteger regular nullities of
\[
                          P(t)-sQ(t),\qquad P(z)=Az+B,\quad Q(z)=Cz+D
\]
over the complex two-square coefficients, with unnormalized coordinate trace.
These fractional nullities lie in \((0,1)\) by the [four-column reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound).
Put \(t_j=s^jts^{-j}\).
Suppose the three right cosets represented by \(1,s,s^2\) of \(K_3=\langle t_0,t_1\rangle\) in \(H\) are distinct.
Then \(\Delta(H;s,t)\le2/3\), and whenever it is positive some choice of coefficients attains it.

Moreover, if two-marked torsion-free, scalar-injective groups \((H_n;s_n,t_n)\) converge to \((H;s,t)\), then
\[
                    \limsup_n\Delta(H_n;s_n,t_n)\le\Delta(H;s,t).
\]
Convergence means eventual agreement on all relations in each fixed marked word ball.
Only the limiting group is required to satisfy the coset condition.

In particular assume the four right cosets of \(K_4=\langle t_0,t_1,t_2\rangle\) represented by \(1,s,s^2,s^3\) are distinct in \(H\).
If \(H\) admits no half-nullity rectangle on the given marks, there are \(\epsilon>0\) and a finite marked radius \(R\) such that every torsion-free scalar-injective marked group agreeing with \(H\) through radius \(R\) has \(\Delta\le1/2-\epsilon\).
This applies to every residually finite \(H\) with these four cosets by the [periodic image theorem](Yin_C_A0310_v1.md#statement), and also to any such marking with an abelian quotient of order 24 by the [order-24 exclusion](Yin_C_A0303_v1.md#statement) and the [abelian quotient reduction](Yin_C_A0241_v1.md#statement).
The same assertion applies if some periodic image of \(t\) violates the conclusions of the periodic image theorem.
The nearby groups can have different finite quotients and different coset counts.

## A limiting rational plane with large intersection

When \(t=1\), the groups agreeing with that single relation are cyclic and have only integer ranks, by cyclic spectral evaluation.
Suppose \(t\ne1\), so \(t\) has infinite order.
For every noninteger input the [singular pencil reduction](Yin_C_A0184_v1.md#singular-cyclic-blocks) gives invertible \(P,Q\) over the one-variable rational field.
Its nullity is the intersection dimension of the plane spanned by the columns of the vertical stack of \(Q(t),P(t)\) with the graph of \(sI_2\).
A constant point correspondence of \(PQ^{-1}\) would give integer rank by the [two-dimensional transfer test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
For a noninteger input, the two labels cannot generate a cyclic group, so the hypothesis \(s\notin\langle t\rangle\) of that test holds also for inputs in the approaching groups.
The [window bound for a graph](Yin_C_A0183_v1.md#statement) gives \(\Delta(H;s,t)\le2/3\) at the limiting marking.

Suppose a converging sequence of such groups has rectangles of noninteger nullities \(\delta_n\) converging to \(a>0\).
The same reasoning permits a constant sequence of groups.
Balance each cyclic plane by a simultaneous invertible constant change \(T_n\oplus T_n\) of input and output using the [constant metric construction](Yin_C_A0307_v1.md#balancing-the-cyclic-plane).
This preserves its graph intersection and makes the sum of the Haar averages of the two diagonal blocks of its projection equal to \(I_2\).
The construction uses the absence of constant point correspondence in the respective input, and all \(t_n\) occurring in these inputs have infinite order.

The [compactness of degree-one plane presentations](Yin_C_A0307_v1.md#compactness-of-degree-one-plane-presentations) supplies, after taking a subsequence, a balanced rational plane \(V(z)\) of dimension two in \(\mathbb C(z)^4\).
Either it contains a nonzero constant vector or two polynomial columns of degree at most one span it.
In fact the normalized exterior coordinates give convergence of the cyclic orthogonal projections almost everywhere and in Haar \(L^2\).
If the limiting orthonormal coefficient columns become dependent over \(\mathbb C(z)\), their common primitive column has degree zero and yields that constant vector.
Let \(\kappa\) be the graph intersection dimension for this plane at \(H\).
For each power of the compression of the cyclic projection by the shift graph projection, the trace converges.
Indeed bounded Fejér approximations in \(t\) to the limit cyclic matrix have convergent marked traces by agreement on finite word relations.
The \(L^2\) convergence and uniformly bounded operator norms control the replacement errors.
Taking the decreasing infimum of these power traces gives \(\kappa\ge a\).
This comparison uses no bound on the graph intersections in \(H_n\).

## Graph limits and split limits

Suppose one coordinate projection of \(V\) has rank two over \(\mathbb C(z)\).
Then the plane is the graph of a rational matrix \(M\) over that coordinate.
Use \(r=s\) for the original input and \(r=s^{-1}\) after exchanging the coordinates, which carries the shift graph to that of \(s^{-1}I_2\).
The three-coset condition also holds in the latter orientation: the reverse subgroup is \(s^{-1}K_3s\), and membership of any power of \(s\) is preserved under this conjugation.
The graph window therefore gives \(0<\kappa\le2/3\) in either orientation, including graphs of singular transfers.

In fact a singular \(M\) cannot occur here.
For \(M=0\) the intersection is zero.
For a rational rank-one \(M\), write \(M=f g\) with \(f\) a rational column and \(g\) a rational row, and evaluate at \(t\).
Application of \(g(t)\) identifies the affiliated kernel of \(I_2-r^{-1}f(t)g(t)\) with that of the scalar \(1-g(t)r^{-1}f(t)\), with inverse on the latter kernel given by \(r^{-1}f(t)\).
Choose nonzero Laurent polynomials \(d,e\) simultaneously clearing the entries of \(g,f\) respectively.
Multiplying the scalar on the left by \(d(t)\) and on the right by \(e(t)\) gives the group-ring element
\[
                  d(t)e(t)-(d(t)g(t))r^{-1}(f(t)e(t)).
\]
The multipliers are affiliated units and scalar injectivity makes the cleared element zero or an affiliated unit.
This would give integer \(\kappa\).
For invertible \(M\) a constant vector in its graph has both components nonzero and gives a constant point correspondence, also forcing integer \(\kappa\) because \(r\notin\langle t\rangle\).

The remaining graph has two linear generating columns.
Write their input and output blocks as \(Q_*(z),P_*(z)\); the input block is rationally invertible.
Its evaluation parametrizes the graph, and \(\kappa=\dim\ker(P_*(t)-rQ_*(t))\).
If \(r=s^{-1}\), left multiplication by \(-sI_2\) puts this matrix in the original rectangle form \(Q_*(t)-sP_*(t)\).
Thus the actual marked group \(H;s,t\) attains the fractional nullity \(\kappa\ge a\).

If neither coordinate projection has full rank, each has rank one and \(V=X(z)\oplus Y(z)\) for two rational lines.
A constant line on either side forces the other to be the constant orthogonal line by balance, giving zero intersection.
Indeed its projection averages to a projection, and positivity on the orthogonal complement makes it equal to that projection almost everywhere.
This also handles any split plane with a nonzero constant vector.
Otherwise the two linear generating columns show that each line admits a nonconstant fractional linear coordinate ratio.
Indeed one can project a generating linear column nontrivially onto each line and take the ratio of its two coordinates.
Choose the same numerical coordinate basis on both sides, so that the lines are graphs of such functions \(u,v\).
The intersection is parametrized by the scalar kernel of \(u(t)-v(s^{-1}ts)\).
Clear its first denominator on the left and its second on the right.
As before \(\kappa\) is zero or one, and positivity forces equality of the two affiliated functions at the actual group elements.
Each fractional linear function is invertible as a change of variable, so these functions generate the same cyclic von Neumann algebra for the two translations.
Fourier support then gives \(\langle t\rangle=\langle s^{-1}ts\rangle\), hence \(s^{-1}ts=t^{\pm1}\).
This fixed word relation also holds in all sufficiently late \(H_n\).
They would be cyclic-by-cyclic, hence amenable, with integer regular ranks by [Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups) and scalar injectivity.
This contradicts the chosen inputs.
Thus every positive limit \(a\) under consideration is bounded above by an attained fractional nullity at \(H\).

## The supremum and the four-coset gap

A sequence of groups with positive limsup of \(\Delta\) admits a subsequence and fractional nullities converging to that limsup, by the definition of supremum.
The preceding argument gives the asserted upper semicontinuity.
On the constant sequence at \(H\), the same argument realizes \(\Delta(H;s,t)\) when it is positive.

Four distinct cosets for \(K_4\) imply the three-coset hypothesis since \(K_3\subseteq K_4\).
They also bound every fractional nullity at \(H\) by \(1/2\) by the four-position window.
If the value \(1/2\) is excluded, attainment gives \(\Delta(H;s,t)<1/2\).
Taking \(\epsilon=(1/2-\Delta(H;s,t))/2\), failure of the stated finite-radius conclusion would give groups agreeing through each successive radius with \(\Delta>1/2-\epsilon\), contradicting upper semicontinuity.

The coset condition itself need not persist in a marked neighborhood.
For example \((\mathbb Z;z^n,z)\) converges to the standard two-generator marking of \(\mathbb Z^2\), since a word with exponent sums \(a,b\) evaluates there as \(z^{na+b}\) in the approximants.
All the indicated cosets are distinct at the limit and coincide in each approximant.
More generally membership of a prescribed power of \(s\) in the subgroup generated by finitely many prescribed words is open in marked group space, since any witnessing word equality is finite.
The condition that the specified cosets be distinct is consequently closed.
The gap proof uses it only at the limiting marking.

## Assessment history

### Decision attainment-and-upper-semicontinuity

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | At a three-coset marking the largest positive fractional nullity is attained and bounds the limit superior from neighboring markings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | At a three-coset marking the largest positive fractional nullity is attained and bounds the limit superior from neighboring markings. |
| argument | [A limiting rational plane with large intersection](#a-limiting-rational-plane-with-large-intersection) | A limiting rational plane with large intersection. |
| argument | [Graph limits and split limits](#graph-limits-and-split-limits) | Graph limits and split limits. |
| argument | [The supremum and the four-coset gap](#the-supremum-and-the-four-coset-gap) | The supremum and the four-coset gap. |
| review | [Attainment and upper semicontinuity](../audits/reviews/Yin_R_A0222_v1.md#attainment-and-upper-semicontinuity) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-attainment-and-upper-semicontinuity)
