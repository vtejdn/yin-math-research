---
author: Yin
---

# Adjacent generators from the fold of the middle subgroup double

## Statement

Let \(x,y\) be infinite-order elements of a discrete group with \(\langle x\rangle\cap\langle y\rangle=\{1\}\), and put \(A=\langle x,y\rangle\).
Let \(L(z),R(z)\in{\rm GL}_n(\mathbb C(z))\).
Assume for each nontrivial root of unity \(\eta\) that \(L(\eta z)\ne L(z)D\) for every constant complex matrix \(D\), and that \(R(\eta z)\ne cR(z)\) for every constant scalar \(c\).
If \(J\le A,\ a\in A\) and
\[
                     L(x)R(y)a^{-1}\in{\rm GL}_n(U(J)),
\]
then \(J=A\).
Here \(U(J)\) denotes the affiliated algebra for the canonical group trace.
The hypotheses allow poles on the Fourier circle of either cyclic group.

In particular let \(H=\langle s,t\rangle\) satisfy the torsion-free, scalar-injective [order-24 half-rank hypotheses](Yin_C_A0240_v1.md#statement) with marks \(3,4\).
Write \(F=\ker(\chi\bmod4)\), \(t_i=s^its^{-i}\), and \(A_i=\langle t_i,t_{i+1}\rangle\).
Then \(A_i=F\) for every integer \(i\), including the case of disjoint neighboring cyclic groups and finite adjacent abelianization.
Thus each of \(s^4,t_{i-1},t_{i+2}\) must be an actual word in \(t_i,t_{i+1}\).
A proper adjacent subgroup rules out the half rank.

## The fold supplies a character on the auxiliary subgroup

Write \(P=A_2*_J A_1\) for the double with copies indexed by \(1,2\); denote the two copies of \(x,y,a\) by \(x_i,y_i,a_i\).
Subgroup inclusions preserve affiliated rational expressions by regular trace preservation, and the two images of the given matrix agree since it belongs to \(U(J)\).
Rearranging
\(L(x_1)R(y_1)a_1^{-1}=L(x_2)R(y_2)a_2^{-1}\) gives
\[
 T=L(x_2)^{-1}L(x_1)=R(y_2)dR(y_1)^{-1},\qquad d=a_2^{-1}a_1.
\]
Put \(E=\langle x_2,x_1\rangle\) and \(B=\langle y_2,d y_1d^{-1}\rangle\).
Then \(T\in{\rm GL}_n(U(E))\) and \(T=Vd\) with \(V\in{\rm GL}_n(U(B))\).

There is an element \(e\in E\cap Bd\) for which \(Te^{-1}\) belongs to \({\rm GL}_n(U(E\cap B))\).
Indeed the nonzero bounded transform of \(T\) has entries supported on \(E\), and equals the bounded transform of \(V\) times \(d\), so some coefficient lies in \(E\cap Bd\).
For any such \(e\), both \(Te^{-1}\) and its inverse are affiliated over \(E\) and over \(B\).
The intersection of these algebras is the affiliated algebra of the subgroup intersection, by entrywise bounded transforms and the Fourier support characterization. [Subgroup cut with a right translation](Yin_C_A0188_v1.md#regular-fourier-support-of-the-cut)

Let \(\pi:P\to A\) be the fold, equal to the identity on the underlying \(A\) in both copies.
Then \(\pi(E)=\langle x\rangle\), \(\pi(B)=\langle y\rangle\), and \(\pi(d)=1\).
The assumed disjointness gives \(\pi(E\cap B)=\{1\}\) and \(\pi(e)=1\).
Identify \(\langle x\rangle\) with \(\mathbb Z\) by \(x\mapsto1\).
The restriction of \(\pi\) to \(E\) thereby gives an integer character that vanishes on \(E\cap B\) and on \(e\), while taking both \(x_1,x_2\) to one.
The fold is used only on group elements to define this character.
The resulting unitary twists of the regular representation of \(E\) fix \(Te^{-1}\) and \(e\).
For every \(|\lambda|=1\) this proves
\[
    L(\lambda x_2)^{-1}L(\lambda x_1)=L(x_2)^{-1}L(x_1).
\]
On rearranging, \(H_\lambda(x_1)=H_\lambda(x_2)\), where \(H_\lambda(z)=L(\lambda z)L(z)^{-1}\).
In particular the common value is affiliated over \(\langle x_1\rangle\cap\langle x_2\rangle\).

## Recovering both original generators

The group intersection \(A_1\cap A_2=J\) follows from amalgam normal form.
Consequently \(\langle x_1\rangle\cap\langle x_2\rangle\) corresponds in either copy to \(\langle x\rangle\cap J\).
If \(x\notin J\), this is a proper subgroup of an infinite cyclic group.
There is a nontrivial finite root of unity \(\eta\) whose phase twist fixes its affiliated algebra: for an index \(l>1\) use a primitive \(l\)-th root, and for the trivial subgroup take \(-1\).
The same \(\eta\) works for every \(\lambda\).
Cyclic Fourier evaluation and rationality then give
\[
                L(\lambda\eta z)L(\eta z)^{-1}
                         =L(\lambda z)L(z)^{-1}
                         \qquad(|\lambda|=1)
\]
as identities over \(\mathbb C(z)\).
Thus \(L(z)^{-1}L(\eta z)\) is invariant under every unit rotation of \(z\).
Each entry is a constant rational function, contrary to the hypothesis on \(L\).
It follows that \(x\in J\).

The given product now gives \(R(y)a^{-1}\in{\rm GL}_n(U(J))\).
Taking the bounded transform as before gives some \(y^h\in Ja\).
Then \(R(y)y^{-h}\) belongs to \(U(J\cap\langle y\rangle)\).
If the latter cyclic subgroup is proper, its Fourier rotation by some nontrivial finite root \(\eta\) would give \(R(\eta z)=\eta^hR(z)\).
The hypothesis on \(R\) excludes this, so \(y\in J\) as well.

## The order-24 application

Put \(A=A_0=\langle t_0,t_1\rangle,\ B=A_2,\ J=A\cap B,\ g=s^4\).
For the rational matrix \(M(z)\) of the rectangle the [middle product](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) satisfies \(M(t_1)M(t_0)a^{-1}\in{\rm GL}_2(U(J))\), with \(g=ba,\ b\in B,\ a\in A\), and \(F=\langle A,B\rangle\).
The [rotational exclusion for the two-dimensional transfer](Yin_C_A0256_v1.md#two-factors-in-a-single-subgroup-coset) verifies both hypotheses on the matrix functions with \(L=R=M\).
When \(\langle t_0\rangle\cap\langle t_1\rangle=\{1\}\), the result above gives \(J=A\).
Thus \(A\subseteq B\) and \(g\in B\); conjugation by \(s^2\) gives \(B\subseteq gAg^{-1}\subseteq B\), hence \(A=B=F\).
When the cyclic intersection is nontrivial this is the [common-power result](Yin_C_A0258_v1.md#statement).
Conjugation by each \(s^i\), which normalizes \(F\), proves the assertion at every adjacent pair.

## Assessment history

### Decision recovering-the-subgroup-from-two-rational-factors

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | The folded double recovers both adjacent generators even for disjoint cyclic subgroups with finite adjacent abelianization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [The fold supplies a character on the auxiliary subgroup](#the-fold-supplies-a-character-on-the-auxiliary-subgroup) | Cyclic intersections and right cosets of affiliated subgroups. |
| argument | [Recovering both original generators](#recovering-both-original-generators) | The two distinct rotation conditions on the rational functions. |
| argument | [The order-24 application](#the-order-24-application) | Generation of the actual index-four subgroup. |
| review | [Recovering the subgroup from two rational factors](../audits/reviews/Yin_R_A0208_v1.md#recovering-the-subgroup-from-two-rational-factors) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-recovering-the-subgroup-from-two-rational-factors)
