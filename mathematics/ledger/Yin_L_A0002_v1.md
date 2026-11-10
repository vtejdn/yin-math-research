---
author: Yin
---
# Torsion-freeness and actual rational inverses: first mechanism tests

Date: 2026-11-10.
This exploration serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through the selected [fourth route](../strategies/Yin_S_A0004.md).
The coordinating agent and three research delegates developed and locally checked the arguments for Yin.
The findings below are elementary mechanism tests, source specializations and explicit failures of proposed implications; they supply no new group-class theorem or resolution of the Task.
There is no formal independent proof audit or novelty claim.

## Exact target and foundations

Write \(B=\lambda_G(\mathbb CG)\), \(M=\mathcal N(G)\), \(U=\mathcal U(M)\), and \(R_G=\operatorname{Rat}_{U}(B)\).
All sums, products and inverses of unbounded operators below are operations in the finite affiliated \(*\)-algebra, rather than unqualified pointwise operations on operator domains.
The [retained finite-trace interface](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) identifies injectivity with affiliated invertibility by polar decomposition.
The [MSY23 Theorem 5.25 interface](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) makes the Task equivalent to division of the actual rational closure.
The present question is how torsion-freeness can force every nonzero \(r\in R_G\) to have scalar analytic rank one.

## Cyclic rational functions

Fix \(g\ne e\) in a torsion-free group.
On each right coset \(\langle g\rangle t\), the operator \(\lambda(g)\) is a bilateral shift.
Its Fourier realization is multiplication by \(z\) on the circle with Haar measure.
Every nonzero Laurent polynomial \(p(z)\) has only finitely many circle zeros, so \(p(\lambda(g))\) is injective and has an affiliated inverse.
Consequently
\[
\mathbb C(z)\longrightarrow U,\qquad
p/q\longmapsto p(\lambda(g))q(\lambda(g))^{-1}
\]
is an actual field embedding, and every nonzero element in its image is a unit of \(U\).

This image is the actual rational closure of the cyclic group algebra.
Indeed a singular matrix over this field has a nonzero field-valued kernel column, which remains nonzero in \(U\), whereas a nonsingular matrix already has its inverse over the field.
It therefore cannot acquire an additional inverse merely by passing to \(U\).

The use of torsion-freeness is precise: it supplies infinite order of \(g\).
For an element of finite order \(m>1\), the nonzero projection
\[
p_g=\frac1m\sum_{j=0}^{m-1}\lambda(g)^j
\]
instead satisfies \((1-\lambda(g))p_g=0\).
The cyclic argument needs no hypothesis about relations among several infinite-order elements.

Every finite product of nonzero cyclic rational functions is also a unit, even when its factors do not commute.
This supplies no additive closure assertion.

## Mixed resolvent sums with a scalar real part

Here is a family involving arbitrarily many noncommuting group elements for which the cyclic input does pass through addition.
Let \(g_j\ne e\), \(|z_j|=1\), \(a_j\in\mathbb R\), and
\[
c=\sum_{j=1}^{N}a_j\ne0,\qquad
T_j=(1-z_j\lambda(g_j))^{-1},\qquad
r=\sum_{j=1}^{N}a_jT_j,
\]
where \(N\) is finite.
All denominators are justified by the preceding cyclic calculation.
Put \(V_j=z_j\lambda(g_j)\).
The affiliated identities
\[
T_j^*=(1-V_j^*)^{-1}=-T_jV_j,
\qquad
T_j+T_j^*=T_j(1-V_j)=1
\]
give
\[
r+r^*=cI.
\]
Thus \(H=(r-r^*)/(2i)\) is selfadjoint affiliated and \(r=c/2+iH\).
Spectral calculus yields
\[
r^{-1}=\bigl(c/2+iH\bigr)^{-1}\in M,
\qquad
\|r^{-1}\|\le \frac{2}{|c|}.
\]
Since \(r\in R_G\) and the actual rational closure is inverse closed in \(U\), this inverse also lies in \(R_G\).

Positive real coefficients are an immediate special case, but their positivity is unnecessary when the real coefficient sum is nonzero.
No commutation, amenability, orderability or Atiyah hypothesis is used.
This is a direct Cayley-transform and spectral-calculus test, not a new assertion of group-class coverage.
It does not cover arbitrary complex coefficients or the real zero-sum case, and no general rational expression has been shown to admit this scalar-real-part form.

## The first additive scalar tests

For cyclic fractions
\[
x=p(g)q(g)^{-1},\qquad y=a(h)b(h)^{-1},
\]
with nonzero denominators, commutation within each cyclic field gives
\[
q(g)(x+y)b(h)=p(g)b(h)+q(g)a(h).
\]
The two outside multipliers are already units.
Thus this particular rational addition reduces to kernel vanishing for the displayed structured group-ring numerator.
This calculation establishes no Ore condition or common-denominator formula for arbitrary noncommutative rational expressions.

A useful direct coefficient region is also available.
Let \(A=\sum_{j=0}^{k}c_j\lambda(g_j)\), where the \(g_j\) are distinct and zero coefficients have been removed.
If
\[
|c_0|\ge\sum_{j=1}^{k}|c_j|,
\]
then \(A\) is affiliated invertible.
For strict inequality, a Neumann series gives a bounded inverse after extracting \(c_0\lambda(g_0)\).
For equality and \(k\ge1\), an equation \(A\xi=0\) with \(\xi\ne0\) would express \(\xi\) as a convex combination of vectors \(V_j\xi\) of the same norm, where
\[
p_j=|c_j|/|c_0|,\qquad
V_j=-\frac{c_j/c_0}{p_j}\lambda(g_0^{-1}g_j),
\qquad
\xi=\sum_jp_jV_j\xi.
\]
Strict convexity of Hilbert space forces every \(V_j\xi=\xi\).
This produces an eigenvector for an infinite-order regular group unitary, contradicting the cyclic Fourier calculation.
The scalar one-term case is immediate.
Finite-trace polar decomposition then supplies dense range and affiliated invertibility.

This covers all nonzero binomials, but the coefficient region does not cover every trinomial.
For example, the complex-phase resolvent test
\[
r_{g,h}=(1-g)^{-1}+i(1-h)^{-1},
\qquad
(1-g)r_{g,h}(1-h)=(1+i)-ig-h
\]
has coefficient lengths \(\sqrt2,1,1\) when \(e,g,h\) are distinct.
All three strict triangle inequalities hold.
Neither the scalar-real-part resolvent argument nor the coefficient-dominance argument settles this general test.
The bounded follow-up literature search did not settle its general complex analytic status; this is not an assertion that the test is new or open.
The inspected comparison passages were [AT18, arXiv v1, Theorems 1.4 and 1.6](https://arxiv.org/pdf/1612.00934v1), [AT21, arXiv v1, Theorems 1.1–1.2](https://arxiv.org/pdf/1905.09494v1), and [BJ24, arXiv v1, Theorem 4](https://arxiv.org/pdf/2402.08625v1).
Their algebraic zero-divisor conclusions retain finite-support, coefficient, residual-group or invertible-pairing conditions; none of these inspected passages supplies the required general complex \(\ell^2\)-kernel statement.
These are scope comparisons, not proof inputs or complete source audits.

## A noncommutative calibration

The preceding complex-phase test can be solved directly in the Klein bottle group
\[
G=\langle a,b\mid aba^{-1}=b^{-1}\rangle.
\]
This torsion-free semidirect product is an already known Atiyah group.
Put \(z=a^2\), \(w=b\).
The normal subgroup \(H=\langle z,w\rangle\cong\mathbb Z^2\) has index two, and left multiplication in the right \(\mathbb CH\)-basis \((1,a)\) is represented by
\[
a\longmapsto
\begin{pmatrix}0&z\\1&0\end{pmatrix},
\qquad
b\longmapsto
\begin{pmatrix}w&0\\0&w^{-1}\end{pmatrix}.
\]
Therefore \(s=(1+i)-ia-b\) is represented by
\[
S(z,w)=
\begin{pmatrix}1+i-w&-iz\\-i&1+i-w^{-1}\end{pmatrix},
\qquad
\det S=(1+i-w)(1+i-w^{-1})+z.
\]
The determinant is a nonzero Laurent polynomial because its \(z\)-coefficient is one.
A nonzero Laurent polynomial in two variables has Haar-null zero set on \(\mathbb T^2\): outside the finite set where all coefficients in the second variable vanish, it has finitely many zeros in that variable, so Fubini applies.
Fourier decomposition over \(H\) makes \(S\) invertible almost everywhere.
Thus \(s\), and then \((1-a)^{-1}+i(1-b)^{-1}\), are affiliated invertible.

The calibration respects a noncommutative group relation, but it uses the extra finite-index abelian structure.
It does not show how torsion-freeness alone controls the corresponding general numerator.

## Why infinite orbits and scalar injectivity do not finish the argument

In \(\mathcal N(\mathbb Z)=L^\infty(\mathbb T)\), choose an arc \(E\) of Haar measure \(1/2\) and put \(p=1_E\).
The operator is equivariant for the regular translations and has kernel dimension \(1/2\), although the group is torsion-free.
Its kernel can have infinite translation orbits without their translates being mutually orthogonal.
There is no contradiction: \(p\) is outside the actual rational closure \(\mathbb C(z)\).
A rational function vanishing on a positive-measure arc has identically zero numerator, so a nontrivial indicator cannot belong to that closure.
Any useful orbit argument must therefore use actual rationality as well as equivariance.

There is a stronger obstruction to an induction that assumes only scalar polynomial injectivity.
Reuse [MSY23 Example 5.24](../audits/literature/MSY23/Yin_U005.md#example-524-integral-rank-need-not-preserve-free-field-rank).
Let
\[
Y=(T^2,TST,TS^2T)
\]
for a free semicircular pair \(S,T\), let \(Z=(Z_1,Z_2,Z_3)\) be a free semicircular triple in another finite tracial algebra, and use the average trace on their direct sum.
Set \(X_j=Y_j\oplus Z_j\).
The retained source proves that \(Y\) is algebraically free and has integer polynomial-matrix ranks; the free triple \(Z\) also has these properties.
Consequently every nonzero scalar formal polynomial \(p(X)\) has rank one.

Nevertheless
\[
P(X)=\begin{pmatrix}X_1&X_2\\X_2&X_3\end{pmatrix}
\]
has rank \((1+2)/2=3/2\).
The first summand has rank one by the source's rational identity.
The formal polynomial matrix \(P\) is full, since evaluation at \((1,0,1)\) gives \(I_2\); free-field rank preservation gives rank two on \(Z\).
Both \(Y_1\) and \(Z_1\) are affiliated invertible, so
\[
r=X_3-X_2X_1^{-1}X_2
  =0\oplus(Z_3-Z_2Z_1^{-1}Z_2)
\]
is an element of the actual rational closure with rank \(1/2\).
The second summand has rank one by Schur elimination of the rank-two matrix \(P(Z)\).
Thus \(r\ne0\) and \(r\) is not invertible, even though all nonzero scalar polynomials in \(X\) are invertible.

This is a direct consequence of the retained source example and an ordinary checked direct-sum calculation.
It is not a canonical group representation and does not refute the Task.
It shows exactly why finite trace, algebraic freeness and scalar analytic injectivity alone cannot justify closure under rational addition.
The unresolved argument must use further structure of the group ring with its canonical trace.

## Denominator clearing and finite propagation

There is a correct conditional reduction.
Assume every nonzero element of \(B\) is affiliated invertible and \(B\) is a right Ore domain.
Its classical fraction division ring \(Q(B)\) embeds in \(U\).
Gaussian elimination over \(Q(B)\) shows that a square matrix over it which is invertible over \(U\) already has its inverse over \(Q(B)\).
Hence \(Q(B)\) is rationally closed in \(U\).
Conversely its scalar fractions lie in \(R_G\), so \(R_G=Q(B)\).

The Ore hypothesis cannot be silently supplied by torsion-freeness.
Even \(\mathbb CF_2\) is non-Ore, although its actual rational closure is a division ring; [Lin06, Proposition 2.2, arXiv v2 p.3](https://arxiv.org/pdf/math/0311071v2#page=3) gives the non-Ore obstruction for groups containing a free subgroup.
Moreover, under the domain assumption, Ore is equivalent to amenability by [Kielak's appendix to Bar19, Theorem A.1, arXiv v2 p.5](https://arxiv.org/pdf/1605.09133v2#page=5).
Thus an insistence on scalar group-ring fraction clearing excludes important nonamenable examples.

For finitely generated amenable groups, [Ele03, Theorem 1, arXiv v1 p.2](https://arxiv.org/pdf/math/0111180v1#page=2) turns a scalar group-ring \(\ell^2\)-kernel into a nonzero finitely supported kernel witness.
Together with the amenable-domain Ore result recalled in [Lin06, Theorem 2.6, p.4](https://arxiv.org/pdf/math/0311071v2#page=4), this is a known conditional bridge from the algebraic domain property.
It does not establish either assumption from torsion-freeness.

Rational inversion also loses finite propagation, already for
\[
(2-g)^{-1}=\sum_{n\ge0}2^{-n-1}g^n
\]
with \(g\) of infinite order.
Linearizing a rational equation into a polynomial system does not restore a general finite-support kernel-witness principle.
For \(F_2=\langle a,b\rangle\), the operator
\[
\partial=(a-1,\ b-1):\ell^2(F_2)^2\to\ell^2(F_2)
\]
has dense image, because its adjoint kernel consists of common invariant \(\ell^2\) vectors and is zero.
Consequently its kernel has von Neumann dimension one.
Its finitely supported kernel is zero: a finitely supported zero-boundary edge chain on the free Cayley tree vanishes by removing leaf edges.
This does not contradict integer matrix ranks; it rules out a proposed analytic-to-finite-support shortcut for arbitrary polynomial systems.

The [bounded common denominators in Lin00](../audits/literature/Lin00/Yin_U001.md#bounded-fractions-and-common-denominators) belong to \(\mathcal N(G)\), not necessarily to \(\mathbb CG\).
They therefore cannot make scalar group-ring injectivity applicable to a general rational numerator.

## Precise continuation point

The positive tests use infinite order at their denominators and a separate mechanism controlling the resulting numerator or real part.
The general step still missing is a group-sensitive exclusion of a nonzero proper kernel for a rational Schur complement.

A concrete next family is
\[
r_{f,g,h,k}
 =(1-f)-(1-h)(1-g)^{-1}(1-k),
\qquad f,g,h,k\in G,\quad g\ne e.
\]
The denominator is justified directly by torsion-freeness.
The question is whether this actual affiliated element is either zero or injective, first under explicitly specified relations among \(f,g,h,k\).
For
\[
A=\begin{pmatrix}1-f&1-h\\1-k&1-g\end{pmatrix}
\]
the established Schur identity is
\[
\operatorname{rk}(A)=1+\operatorname{rk}(r_{f,g,h,k}).
\]
Using integer rank of \(A\) to settle the question would assume the target.
Cases where commutation or an explicit change of pivot reduces the Schur complement to a scalar group-ring numerator should be identified before claiming a genuinely rational obstruction.

One possible intermediate lemma would extract, from a nonzero noninjective Schur complement, a nonzero scalar group-ring element with nontrivial \(\ell^2\)-kernel.
No such lemma has been proved here, and the direct-sum example rules out proving it using only general finite-tracial algebra.
Even that lemma would require a separate scalar analytic zero-divisor input and would not automatically handle arbitrary rational complexity.
The current continuation should test an actual relation-dependent elimination or canonical-trace argument, rather than infer division from expression complexity alone.

## Inspection and use limits

The cyclic, coefficient-dominance, resolvent, Klein bottle, projection and tree calculations above were checked directly within this exploratory discussion.
The direct-sum obstruction reuses the exact MSY23 source example and its documented free-field inputs.
The local affiliated-algebra foundation, rather than an unproved assertion about pointwise unbounded domains, supports the displayed identities.
Lin06, Ele03 and the Kielak appendix were inspected in their stated primary arXiv versions at the cited theorem passages; no complete proof audit is claimed.
The bounded support-three search supplies no exhaustive status or novelty conclusion.
No new positive group class, counterexample to the Task or complete rational-closure invertibility mechanism has been obtained.
