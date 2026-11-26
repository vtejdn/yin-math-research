---
author: Yin
---

# The six scalar evaluations exclude a circle-bounded transfer at cyclic order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular group-ring scalar injectivity, and suppose \(\chi:H\twoheadrightarrow C_{24}\) has marks \(\chi(s)=3,\chi(t)=4\).
Suppose the regular rank of \(K=B+At-s(D+Ct)\) is \(3/2\), with complex two-by-two coefficients and unnormalized matrix trace.
The transfer \(M(z)=(Az+B)(Cz+D)^{-1}\) and its inverse must each have an actual pole on the unit circle.
Consequently the two polynomials \(u(z)=\det(Az+B)\) and \(v(z)=\det(Cz+D)\) each have a unit-circle zero.
If the reduced scalar determinant \(u/v\) has neither zeros nor poles on that circle, the two polynomials must share their unit-circle zeros with matching multiplicities and the reduced rational function has degree at most one.
In particular a finite Blaschke product of degree two for \(\det M\) excludes the proposed half kernel.

If \(\langle t\rangle\cap\langle sts^{-1}\rangle=\langle t^k\rangle\ne\{1\}\), each of \(u,v\) must have a zero whose order divides \(\operatorname{lcm}(6,k)\).
These are necessary conditions for the singular transfer; they leave open the general case with poles.

## An obstruction for six numerical matrices

Write \(\mu_n\) for the group of complex \(n\)-th roots of unity.
There is no two-by-two matrix of the form \(M(z)=(Az+B)(Cz+D)^{-1}\), with \(Cz+D\) invertible over \(\mathbb C(z)\), such that \(M\) is regular at each \(\zeta\in\mu_6\) and
\[
                          M(\zeta)^4=\zeta^3 I_2\qquad(\zeta\in\mu_6).
\]
This numerical assertion permits poles elsewhere and imposes no group assumption.

To prove it, define
\[
    D_*(w)=\det\big(B+w^4 A-w^3 D-w^7 C\big),\qquad
    E=\{0,3,4,6,7,8,10,11,14\}.
\]
The polynomial has degree at most fourteen with all exponents in \(E\), by the two-by-two determinant formula.
It is nonzero: choose a nonzero \(z\) with \(Cz+D\) invertible, and let \(w\) run over the four fourth roots of \(z\).
If \(D_*\) vanished identically, all four distinct values \(w^3\) would be eigenvalues of the fixed two-by-two matrix \(M(z)\).

For each \(\zeta\in\mu_6\), map the four elements \(w\in\mu_{24}\) with \(w^4=\zeta\) to the four distinct roots \(w^3\) of \(Y^4=\zeta^3\).
The assumed matrix identity selects an unordered pair of these eigenvalues counting multiplicities, out of ten options.
For each selected \(w\), the matrix in \(D_*(w)\) equals \((M(\zeta)-w^3 I)(C\zeta+D)\), by the rational identity and regularity at \(\zeta\).
It is singular, even if \(C\zeta+D\) is singular.
If an eigenvalue occurs twice, \(M(\zeta)=w^3 I\) since the polynomial \(Y^4-\zeta^3\) is separable.
Then every entry of the matrix in \(D_*(w)\) vanishes at that \(w\), so \(D_*\) has a root of multiplicity at least two there.
Thus the corresponding degree-twelve monic product \(L(w)\) of the selected roots' linear factors must divide \(D_*(w)\).

Write \(L=\sum_{j=0}^{12}L_j w^j\); its constant coefficient is a unit in \(\mathbb Z[\zeta_{24}]\), since it is a product of roots of unity.
If the quotient \(D_*/L=a+bw+cw^2\) has \(a=0\), the missing coefficients at one and two successively force \(b=c=0\), contradicting nonvanishing.
Normalize \(a=1\) by scaling \(D_*\).
The same missing coefficients force
\[
                b=-L_1/L_0,\qquad c=-(L_2+bL_1)/L_0.
\]
The normalized quotient now belongs to \(\mathbb Z[\zeta_{24}][w]\), irrespective of the original complex matrix coefficients.
At \(j=5,9,12,13\) one requires \(L_j+bL_{j-1}+cL_{j-2}=0\), setting \(L_{13}=0\).

The [exact six-fiber computation](../computations/programs/Yin_J_A0010/verify_six_fibers.mjs) reduces these necessary equalities through the homomorphism \(\mathbb Z[\zeta_{24}]\to\mathbb F_{97}\) sending \(\zeta_{24}\) to the primitive root \(4\).
For fiber \(i=0,\ldots,5\) it chooses two elements of \(\{4^{i+6j}:0\le j<4\}\) with repetition, multiplies their six monic quadratic factors, and computes the uniquely forced \(b,c\).
None of the \(10^6\) choices passes the four remaining coefficient tests.
This reduction uses only the roots and the forced algebraic coefficients of the normalized factorization.
An independent test in the same [reproducible program](../computations/programs/Yin_J_A0010/readme.md#six-fibers-of-the-rectangular-determinant) uses the nine coefficients indexed by \(E\) directly.
It checks that the value rows at the chosen roots, using a derivative row as the second constraint at each double selection, have rank nine in all million cases over \(\mathbb F_{97}\).
As a comparison, both algorithms leave 24 modular choices at the primitive root 7 modulo 193.
Only the zero count modulo 97 is needed for the obstruction over \(\mathbb C\).

## Evaluation of the group identity

Put \(t_i=s^its^{-i}\), \(g=s^4\) and \(F=\ker(\chi\bmod4)\).
The [four-step calculation](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) gives rational invertibility of \(M\), the identity \(M(t_3)M(t_2)M(t_1)M(t_0)=gI\), and a character \(\psi=\chi/4:F\to C_6\) with \(\psi(t_i)=1,\ \psi(g)=3\).
If \(M\) has no poles on the circle, each entry is rational and holomorphic on an annulus about it, hence has absolutely summable Laurent coefficients.
All four matrices are then in \(M_2(\ell^1(F))\), a convolution algebra faithfully represented on \(\ell^2(F)\), since convolution with the identity vector recovers the coefficients.
Consequently the identity holds in this algebra and each character \(h\mapsto\zeta^{\psi(h)}\) may be applied for \(\zeta\in\mu_6\).
The result is \(M(\zeta)^4=\zeta^3I\), which the numerical obstruction forbids.
If \(M^{-1}\) has no poles on the circle, apply the same argument to the reversed product of the four inverse matrices.
The right side evaluates to \(\zeta^{-3}I=\zeta^3I\), and \(M^{-1}(z)=(Cz+D)(Az+B)^{-1}\) is again of the required form.

In particular the denominator determinant \(v\) has a circle zero and applying the inverse assertion gives one for \(u\).
If \(u/v\) after cancellation is finite and nonzero on the circle, the boundary zeros cancel with full multiplicity; since \(u,v\) have degree at most two and a common root, the reduced degree is at most one.
A rational inner function has unimodular boundary values except at removable singularities, and its reduced form has neither boundary zeros nor boundary poles.

## Central denominators for neighboring cyclic groups with nontrivial intersection

By the [normal power calculation](Yin_C_A0240_v1.md#the-common-rational-matrix-on-neighboring-cyclic-groups), \(h=t^k\) is central in \(F\) and \(t_i^k=h^{\pm1}\).
For a nonzero scalar polynomial \(v(z)\), put
\[
                 V(z^k)=\prod_{\eta^k=1}v(\eta z).
\]
The product is invariant under rotation by \(\mu_k\), giving a nonzero polynomial \(V\).
It writes \(v(t_i)^{-1}\) as a group-ring numerator divided by the central element \(V(h)\) or \(V(h^{-1})\).
These denominators are affiliated units, because \(h\) has infinite order and their Laurent polynomials are nonzero.
The four-step identity can therefore be cleared into a genuine group-ring identity using a common product of central denominators.

Suppose \(v\) has no zero in \(\mu_{\operatorname{lcm}(6,k)}\).
At every character \(t_i\mapsto\zeta,\ \zeta\in\mu_6\), both \(V(\zeta^k)\) and \(V(\zeta^{-k})\) are nonzero, since all factors are values at \(\eta\zeta^{\pm1}\), \(\eta\in\mu_k\).
Thus the characters extend to these central fractions and again give the impossible six matrix identities.
The same argument for the reversed inverse product applies to \(u\) as the denominator determinant.
This proves the stated root-of-unity restriction even when the original circle functions have other poles.

## Assessment history

### Decision six-singular-fibers-and-the-two-transfer-poles

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:32 |
| status | proved |
| reason | Independent whole-proof inspection verified the stated bounds, hypotheses and argument at the indicated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Circle poles, the determinant bound and the common-power consequence. |
| argument | [An obstruction for six numerical matrices](#an-obstruction-for-six-numerical-matrices) | The sparse determinant, root multiplicities and legitimate cyclotomic reduction. |
| argument | [Evaluation of the group identity](#evaluation-of-the-group-identity) | Absolute Fourier summability of a pole-free transfer and character evaluation. |
| argument | [Central denominators for neighboring cyclic groups with nontrivial intersection](#central-denominators-for-neighboring-cyclic-groups-with-nontrivial-intersection) | The common central denominator and the orders of the required zeros. |
| review | [Six singular fibers and the two transfer poles](../audits/reviews/Yin_R_A0202_v1.md#six-singular-fibers-and-the-two-transfer-poles) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-six-singular-fibers-and-the-two-transfer-poles)
