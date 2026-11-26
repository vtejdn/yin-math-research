---
author: Yin
---

# Four columns with two occurrences of each cyclic label

## Statement

Assume \(G\) is torsion-free and every nonzero element of \(\mathbb CG\) acts injectively in the left regular representation.
Write \(U=U(G)\) for its affiliated algebra and use its regular trace with unnormalized matrix traces.
For \(s,t\in G\) consider every pencil
\[
 L=[\,C_s s-D_s\mid C_t t-D_t\,],
 \qquad C_s,D_s,C_t,D_t\in M_{\ell,2}(\mathbb C).
\]
The following are equivalent for the fixed ordered labels.

1. Some such \(L\) and constant column \(\alpha\) have \(\operatorname{rk}[L,\alpha]-\operatorname{rk}L=1/2\).
2. A four-row pencil of this form has rank \(7/2\).
3. Some matrix \(K=B+At-s(D+Ct)\) with \(A,B,C,D\in M_2(\mathbb C)\) has rank \(3/2\).

Whenever a pencil has noninteger rank, the coefficient columns from each label separately span the same four-dimensional constant space and form a basis of it.
In particular every pencil with at most three output rows has integer rank.
In condition 3, the constant matrix \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\) must be invertible and both \(Az+B\) and \(Cz+D\) must be invertible over \(\mathbb C(z)\).
If \(s\notin\langle t\rangle\), the normalized four-row pencil in the proof has rank at least three.
When \(s\in\langle t\rangle\) or \(t\in\langle s\rangle\), all ranks are integers.

Set \(M(z)=(Az+B)(Cz+D)^{-1}\) in the remaining case.
Condition 3 is excluded if \(M(z)\) leaves invariant a complex line in the constant two-dimensional space, or interchanges two distinct constant lines, with the line identities taken over \(\mathbb C(z)\).
A group homomorphism \(\langle s,t\rangle\to\mathbb Z\) vanishing at \(t\) and nonzero at \(s\) also excludes it.
These tests apply to the two-label instance of the [prescribed pencil criterion](Yin_C_A0167_v2.md#statement); they pose no integrality assumption at larger matrix sizes.

## Intersecting the two column spaces

If both labels lie in one cyclic group the result on integer ranks follows by reduction over its Laurent fraction field, including a trivial label.
For the remaining discussion neither label belongs to the cyclic subgroup of the other, and each has infinite order.
Its scalar rational function field embeds in \(U\) because every nonzero Laurent polynomial acts injectively on each copy of its bilateral shift.
Write \(E_i\) for the complex span of the four columns of \(C_i,D_i\), for \(i=s,t\), and \(W=E_s\cap E_t\).
We use right \(U\)-modules, identifying the dimension of a matrix image with its analytic rank.
Extending constant spaces to \(U\) preserves their intersections, by a constant change of basis.

Let \(F_i\) be the image of the two columns for \(i\), intersected with \(W\otimes_{\mathbb C}U\).
Ordinary linear algebra over \(\mathbb C(i)\) gives a basis matrix for \(F_i\) and a matrix of equations defining it within \(W\).
Indeed both the original columns and the projection onto constant coordinates modulo \(W\) are defined over this field, and elementary row and column operations remain invertible over \(U\).
In particular \(f_i=\dim_U F_i\le2\) is an integer.
The images of the two label blocks have integer dimensions by the same field reduction, and their intersection equals \(F_s\cap F_t\).
Dimension additivity computes the total rank by subtracting the dimension of this intersection from the sum of the two ranks.

If \(f_s=0\) the intersection vanishes.
If \(f_s=1\), write a single rational basis column \(u(s)\) for \(F_s\) and use equations with rational rows \(r(t)\) for \(F_t\).
The intersection is parametrized by the common right kernel of the scalars \(r(t)u(s)\).
Each scalar is either zero or an affiliated unit: multiplying on the left by a common Laurent denominator of the entries of \(r(t)\), and on the right by one for the entries of \(u(s)\), gives a group-ring element to which scalar injectivity applies.
The nonzero denominators are affiliated units.
Thus the intersection has dimension zero or one.
The argument with the two labels interchanged handles \(f_t\le1\).
This calculation also shows that two right lines with rational basis columns in possibly different infinite cyclic subgroups have integer intersection dimension.

It remains to have \(f_s=f_t=2\).
Both label images then lie entirely in \(W\otimes U\), since they have dimension at most two and a full submodule cut is its full support module in the affiliated algebra.
Projecting their columns modulo \(W\) yields zero, and linear independence of \(1,i\) in the group ring forces both \(C_i\) and \(D_i\) to have all columns in \(W\).
Thus \(E_s=E_t=W\), of dimension \(l\) with \(2\le l\le4\).
For \(l=2\) both label images fill it.
For \(l=3\) there is a single rational equation over \(\mathbb C(t)\) for \(F_t\).
Apply it to the two basis columns of \(F_s\); by left and right denominator clearing as above both resulting scalars are zero or units.
The resulting one-row map on two coordinates has integer rank, and the intersection has integer dimension.
This leaves only \(l=4\), in which each of the two lists of four original coefficient columns is a basis.

## The four group elements and the trace bound

Use this common four-dimensional output space and the basis from the first label to identify the pencil by a constant row change with
\[
 L_0=\begin{pmatrix}sI_2&U(t)\\I_2&V(t)\end{pmatrix},\qquad
 U(z)=Az+B,\quad V(z)=Cz+D.
\]
The basis condition on the second label is exactly the invertibility of \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\).
Elimination at the constant identity block gives \(\operatorname{rk}L_0=2+\operatorname{rk}(U(t)-sV(t))\).
Conversely this same pencil linearizes every four-site matrix in item 3, without initially requiring any rank condition on its constant coefficients.
The first label has full constant span in this constructed pencil, so a noninteger rank forces the second label to have that same full span.

Under the basis conditions the two two-column images each have dimension two.
The first image is a graph whose projection is
\[
 P=\tfrac12\begin{pmatrix}I_2&sI_2\\s^* I_2&I_2\end{pmatrix}.
\]
The projection \(Q\) onto the second image has entries in \(\mathcal N(\langle t\rangle)\) and trace two.
Since \(s\notin\langle t\rangle\), the off-diagonal terms in the matrix trace of \(PQ\) have zero regular trace by Fourier support.
Thus \(\operatorname{Tr}(PQ)=1\), where \(\operatorname{Tr}\) includes the group trace.
The meet \(P\wedge Q\) is dominated by the positive compression \(PQP\), so its trace is at most one.
Dimension additivity gives \(\operatorname{rk}L_0\ge3\).

For \(\alpha\ne0\), quotienting the output by its complex line gives a pencil \(L'\) of the same column form and \(\operatorname{rk}[L,\alpha]=1+\operatorname{rk}L'\).
If \(L\) has noninteger rank, restrict to its four-dimensional constant span.
An \(\alpha\) outside that span has increment one, and an \(\alpha\) inside gives a quotient on at most three rows there, of integer rank.
Consequently a half increment forces either \(L\) itself to have half-integer rank, or \(L\) to have integer rank and \(L'\) to have half-integer rank.
After removing extraneous output coordinates the pencil of half-integer rank is four-row and has rank \(7/2\) by the lower bound three.
Conversely for a four-row pencil of rank \(7/2\), quotienting by any nonzero constant column gives rank at least \(5/2\) and at most three; three-row integrality forces rank three.
Together with the linearization this proves all three equivalences.

## Singular cyclic blocks

If \(U(t)\) is invertible and \(V(t)\) has rank one, write \(V(t)U(t)^{-1}=w(t)v(t)\) as a column times a row over \(\mathbb C(t)\).
After multiplication by \(U(t)^{-1}\) on the right the matrix is \(I_2-s w(t)v(t)\).
Its nullity equals that of \(1-v(t)s w(t)\), by eliminating either identity pivot in the border with off-diagonal blocks \(s w(t)\) and \(v(t)\).
Common Laurent denominators on the left and right of this scalar give a group-ring element, so it has integer nullity.
Rank-zero \(V\) is immediate.
If \(V\) is invertible and \(U\) singular, first multiply on the left by \(-s^{-1}\) and interchange the roles of \(U,V\).

If both are singular, the invertibility of the four-by-four constant coefficient matrix forces each to have rank one and both coefficient rows \([A\ B]\) and \([C\ D]\) to have complex row rank two.
A two-by-two matrix pencil of generic rank one with coefficient column span of dimension two has a constant one-dimensional right kernel.
Indeed its two coefficient matrices have rank at most one; when their images are independent, nonproportional coefficient rows in rank-one factorizations would give a rank-two generic sum.
Hence \(U(z)=u(z)r\), \(V(z)=w(z)h\) with nonzero constant rows \(r,h\).
These rows are independent because the vertically stacked pencil has rank two.
A constant input basis change reduces the two image columns to \(u(t)\) and \(-s w(t)\).
Multiplying the latter on the right by the unit \(s^{-1}\) gives a column rational in \(sts^{-1}\).
The two-line calculation above gives integer rank.

## Constant lines and a character test

If both cyclic blocks are invertible, right multiplication by \(V(t)^{-1}\) reduces the rank to that of \(sI_2-M(t)\).
For a constant invariant line, constant simultaneous conjugation makes \(M\) triangular, with rational functions of \(t\) on the diagonal.
Each \(s-f(t)\) is an affiliated unit: right multiplication by the denominator gives a nonzero group-ring element by the disjoint cosets \(s\langle t\rangle\) and \(\langle t\rangle\).
Thus the triangular matrix has rank two.

For two interchanged constant lines the same conjugation gives
\[
 M(t)=\begin{pmatrix}0&f(t)\\g(t)&0\end{pmatrix}.
\]
Eliminating the first pivot \(s\) leaves \(s-g(t)s^{-1}f(t)\).
Multiplying this scalar on the left by \(s\) gives \(s^2-g(sts^{-1})f(t)\).
It has a Laurent denominator on the left from \(\langle sts^{-1}\rangle\) and one on the right from \(\langle t\rangle\); clearing them yields a group-ring element.
The scalar is zero or an affiliated unit.
Both constant-line tests use only rational identities, so clearing denominators reduces them to finitely many coefficient equations in a constant change of basis.

Finally a character to \(\mathbb Z\) killing \(t\) and nonzero at \(s\) gives rank-preserving regular twists that multiply \(s\) by infinitely many distinct phases and fix \(U(t),V(t)\).
The [finite-evaluation polynomial rank bound](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) applied to the bounded pencil \(U(t)-z sV(t)\) at zero gives full rank because \(U(t)\) is an affiliated unit.
For an unrestricted residual \(M(t)\) the graph trace bound alone still permits rank \(3/2\) for \(sI_2-M(t)\); excluding that value would advance the [original problem](../tasks/Yin_T_A0001_v1.md#contract).

## Assessment history

### Decision four-column-reduction

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:23 |
| status | proved |
| reason | The independent review verified the full argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Half increment, rank seven halves and rank three halves. |
| argument | [Intersecting the two column spaces](#intersecting-the-two-column-spaces) | Moving rational columns through a constant output intersection. |
| argument | [The four group elements and the trace bound](#the-four-group-elements-and-the-trace-bound) | The two graph planes, linearization and quotient. |
| argument | [Singular cyclic blocks](#singular-cyclic-blocks) | Both singly and doubly singular cyclic pencils. |
| argument | [Constant lines and a character test](#constant-lines-and-a-character-test) | Two constant-line cases and a character. |
| review | [Four-column reduction](../audits/reviews/Yin_R_A0179_v1.md#four-column-reduction) | Independent review of the stated result and its argument. |

## Current assessment

[Selected decision](#decision-four-column-reduction)
