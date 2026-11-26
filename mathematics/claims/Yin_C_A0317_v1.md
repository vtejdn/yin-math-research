---
author: Yin
---

# A sixteen-point affine action excludes the binary commutator module at order twenty

## Statement

Let \(H=\langle s,t\rangle\) have an order-ten character of marked degrees \((1,2)\) and a permutation representation on \(\mathbb F_{16}\) of the form
\[
       s:\xi\longmapsto w\xi,\qquad t:\xi\longmapsto 1+w^2\xi ,
\]
where \(w\) has order five.
Assume \(t\) and \(t^2s\) have infinite order.
For \(K=B+At-s(D+Ct)\) with complex \(h\)-square corners all invertible and invertible assembly \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\), the regular nullity with unnormalized coordinate trace satisfies
\[
                               \dim_H\ker K\le 13h/80 .
\]
In particular the bound is \(13/40\) at size two.

Consequently, under the torsion-free, scalar-injective [noncyclic order-twenty half-kernel hypotheses](Yin_C_A0313_v1.md#statement), \(M=H'/H''\) has order prime to ten, and the binary coinvariants \(M_{C_2^2}\) vanish.
Writing \(W,E_1,E_2\) for the order-five and the two sign-generator actions on this finite abelian group, \(M\) is the direct sum of its three nontrivial sign components.
Each is a cyclic module over \(\mathbb Z[\zeta_5]\), with \(\zeta_5\) acting as \(W\).
A nonzero component must involve an odd prime different from five.
The argument leaves these three components open.

## A lift of the sixteen permutations

Represent the field by four-bit polynomial coordinates modulo \(X^4+X+1\), with lowest bit the constant term.
The polynomial is irreducible: it has no root in \(\mathbb F_2\) and is not divisible by \(X^2+X+1\).
Use \(w=X^3\), which has order five since \(X^{15}=1\) and \(X^3\ne1\).
The four elements of order five are conjugate by field Frobenius, so this choice covers each \(w\) in the statement.
Write \(x,y\) for the displayed permutations in the order of coordinates \(0,\ldots,15\).
For each \(z^{10}=1\) twist by the tensor product of this permutation representation and the actual character sending \(s,t\) to \(z,z^2\).
Conjugate the result by the diagonal with entries \(z^{d_i}\).
The following table gives the images, the \(d_i\), and integer lifts \(a_i,b_i\) of \(1+d_{x(i)}-d_i,\ 2+d_{y(i)}-d_i\bmod10\).

| | Values at sites zero through fifteen |
| --- | --- |
| \(x(i)\) | 0, 8, 3, 11, 6, 14, 5, 13, 12, 4, 15, 7, 10, 2, 9, 1 |
| \(y(i)\) | 1, 13, 10, 6, 4, 8, 15, 3, 11, 7, 0, 12, 14, 2, 5, 9 |
| \(d_i\) | 8, 6, 2, 1, 2, 7, 9, 3, 5, 5, 0, 3, 1, 3, 8, 7 |
| \(a_i\) | 1, 0, 0, 3, -2, 2, -1, 1, -3, -2, -2, 1, 0, 0, -2, 0 |
| \(b_i\) | 0, -1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, -1, 1, 1, 0 |

At the ten phases the edge from \(i\) to \(x(i)\) transmits by \(z^{a_i}s\) and the edge from \(i\) to \(y(i)\) transmits by \(z^{b_i}t\).
Regular absorption makes the twisted nullity \(16\dim_H\ker K\) at each of these phases.
These transports keep the original group operators in every coordinate.

## Orienting the zero-cost circuits

At each site let \(X,Y\) be the outgoing values on the \(t,s\) edges, and \(T,S\) their incoming values.
The equations \(S=BX+AT,\ Y=DX+CT\) give exactly the twisted rectangle after eliminating \(Y\).
Invertibility of the four corners and assembly implies that any two of \(X,Y,T,S\) determine the other two by constant matrices.
Consequently one may [reverse a collection of edges](Yin_C_A0226_v1.md#reversing-the-edges-of-a-minimum-circulation) that has equal numbers entering and leaving each vertex.
Each reversed edge carries the inverse group translation and negated exponent, with equivalent kernel for \(z\ne0\).

Reverse the \(s\)-edges with initial sites \(4,6,8,9,10,13,14,15\) and the \(t\)-edges with initial sites \(1,2,5,12\).
Their initial and terminal multisets agree by the two permutation rows of the table.
Every residual exponent is nonnegative and their sum is \(26\).
The zero-cost edges in their new orientation are
\[
\begin{gathered}
1\to8,\ 2\to3,\ 12\to10,\ 2\to13,\ 1\to15,\\
0\to1,\ 10\to2,\ 3\to6,\ 8\to5,\ 6\to15,\ 7\to3,\ 8\to11,\ 9\to7,\
10\to0,\ 11\to12,\ 15\to9 .
\end{gathered}
\]
Their only recurrent components are the two directed circuits
\[
             1,8,11,12,10,0,1\qquad\hbox{and}\qquad 3,6,15,9,7,3.
\]
For instance after identifying each of these two listed circuits to a point the remaining arrows form an acyclic graph: they include arrows from the first circuit to \(2,5\) and the second circuit, and from \(2\) to \(13\) and the second circuit.
All edges on the two circuits retain their original orientation.
The first reads \(s,t,t,s,t,t\) and the second reads five copies of \(t\).

Let \(L\) be the constant local solution taking the two new incoming values to the two outgoing values at each site, and \(T(z)\) the residual transport on the outgoing coordinates.
The polynomial matrix \(I-LT(z)\) at zero is invertible in affiliated matrices.
In the order of the components, substitution deals with every acyclic vertex.
On a single circuit only one input from the same component is active at each vertex, and substitution around it leaves a diagonal equation \(I-Du\) for a constant \(h\)-square matrix \(D\).
The group element \(u\) is conjugate to \((t^2s)^2\) or \(t^5\), respectively, by the indicated ordering.
It has infinite order, so \(I-Du\) is invertible in the affiliated algebra by the scalar polynomial \(\det(I-Dz)\) with constant term one evaluated at a bilateral shift.
This proves full rank at zero irrespective of the other edges between components.

Each group of \(h\) columns indexed by a residual edge has degree at most its residual exponent.
The [individual-column interpolation estimate](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) on the ten nonzero phases therefore gives
\[
                       10\cdot16\dim_H\ker K\le26h .
\]
This proves the stated quantitative assertion.

## Excluding the binary part and splitting the odd components

At a half kernel the [marked splitting](Yin_C_A0313_v2.md#splitting-with-a-prescribed-lift-of-the-first-mark) gives \(H/H''=M\rtimes Q,\ Q=C_5\times C_2^2\), with actual marks \((0,\sigma),(v,\tau)\), where \(v\) generates \(M\) as a module.
On \(B_*=M_{C_2^2}\) the order-five action satisfies \(\Phi_5(W)=0\).
If \(B_*/2B_*\ne0\), it is cyclic and nonzero over \(\mathbb F_2[z]/(\Phi_5)\), a field of order sixteen because two has order four modulo five.
Identify the class of \(v\) with one and the action of \(W\) with multiplication by \(w\).
Project the split extension onto this additive group extended by \(C_5\), killing the binary complement.
The two actual marked images act affinely by exactly \(x,y\) in the statement.
The required character exists since a character of \(Q\) has weights \(1,2\bmod10\) as in the [order-twenty marking](Yin_C_A0311_v1.md#the-noncyclic-quotient-of-order-twenty).
Also \(t\) and \(t^2s\) have nontrivial binary degrees and infinite order in \(H\).
All four corners and their assembly are invertible, so the bound \(13/40\) contradicts the half kernel.

The [odd-prime calculation on \(B_*\)](Yin_C_A0313_v3.md#statement) then implies \(B_*=0\).
On \(M/2M\) put \(I=(E_1-I_d,E_2-I_d)\) for the ideal of the acting binary group algebra, where \(I_d\) denotes the identity map.
The two generators commute and their squares vanish in characteristic two, so the cube of this ideal acts by zero.
The vanishing of \(B_*\) gives \(I(M/2M)=M/2M\), whence \(M/2M=0\).
The finite \(M\) has odd order, and five already does not divide its order.
Multiplication by four is thus invertible on \(M\).
The four mutually orthogonal idempotents \((I_d+\epsilon_1 E_1)(I_d+\epsilon_2 E_2)/4\) split \(M\) into its sign components.
The trivial summand identifies with \(B_*=0\).
On each remaining summand the image of \(v\) generates over \(\mathbb Z[W]\) since the binary action is scalar there.
The relation \(\Phi_5(W)=0\) gives the asserted cyclotomic module structure.

## Assessment history

### Decision the-sixteen-point-affine-action

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | The two original-group circuits give the bound 13h/80, eliminating the two-primary part of the metabelian commutator module. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two original-group circuits give the bound 13h/80, eliminating the two-primary part of the metabelian commutator module. |
| argument | [A lift of the sixteen permutations](#a-lift-of-the-sixteen-permutations) | A lift of the sixteen permutations. |
| argument | [Orienting the zero-cost circuits](#orienting-the-zero-cost-circuits) | Orienting the zero-cost circuits. |
| argument | [Excluding the binary part and splitting the odd components](#excluding-the-binary-part-and-splitting-the-odd-components) | Excluding the binary part and splitting the odd components. |
| review | [The sixteen-point affine action](../audits/reviews/Yin_R_A0221_v1.md#the-sixteen-point-affine-action) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-sixteen-point-affine-action)
