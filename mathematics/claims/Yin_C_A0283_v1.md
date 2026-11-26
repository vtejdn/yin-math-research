---
author: Yin
---

# Two consecutive Fourier indices exclude unipotent marks in projective degree two

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and an abelian quotient of order 24.
Suppose the complex two-by-two rectangle \(B+At-s(D+Ct)\) has regular rank \(3/2\).
Use the [normalized ordered marking](Yin_C_A0241_v1.md#statement), and let \(x,y\) be its images in a finite quotient.
Put \(y_j=x^jyx^{-j}\), \(m=|y|\) and \(\mathcal R=\langle y_2\rangle\langle y_3\rangle x^4\).

If \(m\ge3\) and \(\langle y_1\rangle\cap\langle y_0\rangle=\{1\}\), there are two consecutive residues \(i,i+1\bmod m\) such that
\[
 \bigcup_{e=i,i+1}\bigl(y_1^e\langle y_0\rangle\ \cup\
                    \langle y_1\rangle y_0^e\bigr)\subseteq\mathcal R .
\]
In particular all exponents of the other factor are allowed, including zero.

For any field \(k\), if a homomorphism \(H\to {\rm PGL}_2(k)\) has finite image and \(y\) is nonidentity unipotent, its image is cyclic.
Here projective unipotence means that after extending the field and rescaling, \(y\) is represented by a nonidentity unipotent matrix.
In particular for every prime power \(q\ge4\) the group \({\rm PSL}_2(\mathbb F_q)\) with any nonidentity unipotent second mark is excluded as an image.
This includes every \(q=3^f\) with \(f\ge2\).
The calculation below treats arbitrary finite images and imposes no restriction on the order of the first mark.

## The two complete rows and columns of finite labels

The [two-factor transfer comparison](Yin_C_A0280_v1.md#two-factors-in-the-actual-finite-regular-twist) attaches rational Fourier blocks \(E_j\), \(j\bmod m\), to the genuine regular twist by the finite image.
If \(E_a(t_1)E_b(t_0)\ne0\), then \(y_1^a y_0^b\in\mathcal R\), by unique factorization on the left.
We verify that every \(E_b\) is nonzero and two consecutive \(E_a\)'s are rational units.
Their evaluations at the actual infinite-order \(t_j=s^jts^{-j}\) preserve ranks, so each such unit can occur in either position against any block.

If \(C,D\) are both invertible, the [Taylor coefficient calculation](Yin_C_A0280_v1.md#which-finite-frequencies-must-contribute) makes all nonzero-index blocks invertible.
In particular indices 1 and 2 are distinct units.
In the same expansion the coefficient of \(z^m\) in \(E_0(z)\) is \(V(-T)^{m-1}D^{-1}\), with \(T=D^{-1}C\), \(V=A-BD^{-1}C\).
This coefficient is invertible, so \(E_0\) is nonzero.
If \(D\) is invertible and \(C\) is singular, the same proof gives units \(E_0,E_1\) and proves nonvanishing for every other block.
If \(C\) is invertible and \(D\) is singular, inversion of the parameter gives units \(E_{-1},E_0\) and nonvanishing for every block.
These cover all cases by the [denominator pencil restrictions](Yin_C_A0245_v1.md#two-fourier-blocks-of-the-rational-transfer).
The asserted consecutive rows and columns follow.

## A determinant along a full unipotent row

Enlarge the coefficient field to an algebraic closure and choose lifts \(X\in {\rm GL}_2\) of \(x\) and \(Y=I+N\) of \(y\), where \(N\ne0\) and \(N^2=0\).
Write \(Q=\langle x,y\rangle\) for the finite image and suppose it is noncyclic.
By [perfectness of the commutator](Yin_C_A0278_v1.md#statement) it is nonsolvable.
The lift \(Y\) fixes a unique projective point, the line \(\ker N=\operatorname{im}N\).
Choose a nonzero \(u\) on this line and write \(u_j=X^ju\), \(Y_j=X^jYX^{-j}\).
If \(X\) fixed the same line, \(Q\) would lie in the solvable projective upper triangular subgroup.
Consequently \(u_0,u_1\) are independent, as are \(u_{-1},u_0\).
In characteristic zero the element \(y\) would have infinite order because \(Y^j=I+jN\).
In positive characteristic \(p\) it has projective order \(p\), and its nonidentity powers have the same unique fixed line.
In particular \(\langle y_0\rangle\cap\langle y_1\rangle=\{1\}\).

First suppose \(p\ge3\).
For either of the two distinct full row indices \(e\) proved above, \(y_1^e y_0^j\in\mathcal R\) for every \(j\in\mathbb F_p\).
Thus \(Y_1^eY^j=c\,Y_2^aY_3^bX^4\) for some \(a,b\in\mathbb F_p\) and scalar \(c\), which may depend on \(e,j\).
Taking determinants gives \(c^2=(\det X)^{-4}\).
Evaluate the matrices on \(u_{-1}\) and take determinants against \(u_2\).
On the right, \(X^4u_{-1}=u_3\), \(Y_3^b u_3=u_3\), and the determinant-one matrix \(Y_2^a\) fixes \(u_2\).
It follows that the function
\[
             j\longmapsto \det(u_2,Y_1^e(I+jN)u_{-1})
\]
takes at most the two values \(\pm(\det X)^{-2}\det(u_2,u_3)\).
This affine function of \(j\) is therefore constant, since a nonconstant affine function takes \(p\ge3\) distinct values on the prime field.
Its linear coefficient is zero.
As \(Nu_{-1}\) is a nonzero multiple of \(u\), this means \(Y_1^e u\) spans the line of \(u_2\).
Applying this to both consecutive indices would make \(y_1\) fix the line of \(u\), although its unique fixed line is that of \(u_1\).
This contradiction excludes the noncyclic image in odd characteristic.

In characteristic two, \(y_0,y_1\) are involutions.
By [neighboring generation](Yin_C_A0274_v1.md#statement), their subgroup in \(Q\) is normal with cyclic quotient of order dividing four.
A group generated by two involutions has a normal cyclic subgroup generated by their product and quotient of order at most two, so it is solvable.
Its cyclic extension \(Q\) is also solvable, again contradicting the noncyclic assumption.
Finally \({\rm PSL}_2(\mathbb F_q)\) for \(q\ge4\) is noncyclic, as the upper and lower nonidentity elementary unipotent matrices already do not commute projectively.
This gives the stated family.

## Assessment history

### Decision consecutive-fourier-columns-and-unipotent-marks

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:38 |
| status | proved |
| reason | Two consecutive Fourier blocks are units, and the unipotent row calculation excludes a finite noncyclic projective image of the stated type. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The consecutive rows and columns and the projective obstruction. |
| argument | [The two complete rows and columns of finite labels](#the-two-complete-rows-and-columns-of-finite-labels) | The two consecutive rational units and all nonzero blocks. |
| argument | [A determinant along a full unipotent row](#a-determinant-along-a-full-unipotent-row) | Determinant signs, the affine row and the case of two involutions. |
| review | [Consecutive Fourier columns and unipotent marks](../audits/reviews/Yin_R_A0212_v1.md#consecutive-fourier-columns-and-unipotent-marks) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-consecutive-fourier-columns-and-unipotent-marks)
