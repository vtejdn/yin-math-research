---
author: Yin
---

# A bound on the full metabelian quotient at a half-rank rectangle

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free, assume scalar injectivity over \(\mathbb CH\), and suppose \(H_{\rm ab}=C_{26}\).
Write \(N=[H,H]\), \(B=N_{\rm ab}\).
If a four-site two-by-two matrix on the two labels has regular rank \(3/2\), then \(B\) is a finite group of odd order, its order is prime to 13, and
\[
                                 |B|\le 75^{24}.
\]
In the normalized marking with degrees \(1,10\) write \(S=\operatorname{Ad}_s\) on \(B\) and \(B_r=B/\Phi_r(S)B\) for \(r=13,26\).
Here \(\Phi_r\) is the cyclotomic polynomial.
More precisely \(S-1\) and \(S+1\) are automorphisms of \(B\), and \(|B_r|\le75^{12}\) for each \(r\).
The numerical bounds are sufficient and no optimality is claimed.
They concern the entire finite metabelian quotient \(H/[N,N]\), which has order \(26|B|\).
Via the [four-column pencil equivalence](Yin_C_A0184_v1.md#statement) the same restrictions apply to a half-dimensional constant-column increment.

## The cyclic coefficient module

Assume the proposed half rank, orient and order the labels as in the [order-26 homology test](Yin_C_A0203_v1.md#the-two-pairs-of-extreme-coefficients), and write the rectangle as
\[
                K=B_0+A t-s(D+C t).
\]
All four constant corners are invertible by that test.
The [modulo-thirteen obstruction](Yin_C_A0203_v1.md#statement) gives \(B/13B=0\); finite generation makes \(B\) finite of order prime to thirteen.
One has \(S^{26}=1\), \(S-1\) is an automorphism and \(H/[N,N]=B\rtimes\langle s\bmod [N,N]\rangle\), with cyclic factor of order 26.
The element \(u=t s^{-10}\bmod[N,N]\) generates \(B\) as a \(\mathbb Z[S]\)-module, since the conjugates of \(u\) and \(s\) generate the whole split group.

A nonzero quotient of \(B/(S+1)B\) of odd prime order \(p\) gives a marked dihedral quotient of \(H\) with rotations of order \(p\): \(s\) acts by inversion and \(t=u s^{10}\) generates the rotations.
This is excluded by the [odd-order rotation test](Yin_C_A0204_v1.md#the-reflection-and-rotation).
Nor can this cokernel have a quotient of order two, since \(S+1=S-1\) modulo two.
Thus \(S+1\) is an automorphism.
Factor \(X^{26}-1=(X-1)(X+1)\Phi_{13}(X)\Phi_{26}(X)\).
It follows that \(\Phi_{13}(S)\Phi_{26}(S)B=0\).
Multiplication by \(\Phi_{13}(S)\) therefore maps \(B_{26}\) onto \(\Phi_{13}(S)B\), giving \(|B|\le |B_{13}||B_{26}|\).
This uses no decomposition at primes dividing the order of the cyclic action.

## A representation test for a single finite character

For \(r=13,26\), let \(\eta:B_r\to\mathbb R/\mathbb Z\) be a character of order \(k>1\), and choose integers \(q_i\) modulo \(k\) by
\[
            q_i/k=\eta(S^{-i-10}u)\pmod{1},\qquad 0\le i<r .
\]
Use the image of \(u\) in \(B_r\).
One has \(S^r=1\) on this quotient; when \(r=26\) one also has \(S^{13}=-1\).
For every \(z^k=1\) there is an actual unitary representation
\[
             s\longmapsto P,\qquad
             t\longmapsto P^{10}\operatorname{diag}(z^{q_i}),
             \qquad Pe_i=e_{i+1}\quad(i\bmod r).
\]
Indeed \(b\in B_r\) acts diagonally by the phases of the corresponding multiple of \(\eta(S^{-i}b)\), equivariantly for conjugation by \(P\), and \(t=u s^{10}\).
The construction takes place in a quotient of the actual split metabelian group.
Regular absorption gives nullity \(r\delta\) at each such parameter, where \(\delta=\dim_H\ker K\).

For \(r=13\) suppose representatives can be chosen with \(0<q_i<k\) for every \(i\).
For \(r=26\) suppose \(q_{i+13}=-q_i\), all \(0<|q_i|<k\), and their signs alternate with the parity of \(i\).
In either case set \(j=\sum_{i<r}|q_i|/(k r/13)\), and assume \(j\le3\).
Then
\[
                                   \delta\le 2j/13 .
\]
To see this, twist the rectangle by the displayed matrices and keep the same formulas for arbitrary complex \(z\ne0\).
In block column \(i\) its powers are \(0,q_i\).
Shifting its two columns by \(z^{-\min(0,q_i)}\) gives two degree bounds \(|q_i|\).
Write \(E=B_0-(sP)D\) and \(F=A-(sP)C\) on the auxiliary copies, with constant two-by-two matrices repeated along the diagonal.
For positive weights the constant columns come from \(E\); for negative weights they come from \(F P^{10}(tI)\).
The matrix \(E\) is invertible over the cyclic rational field of \(s\), since the formal specialization \(s=0\) gives the invertible corner \(B_0\) on every channel.
The infinite order of \(s\) makes this rational calculation valid in the regular representation.
If all weights are positive this proves full rank of the constant matrix.
In the alternating case the set \(I\) of negative positions is preserved by addition of ten.
Multiply on the left by \(E^{-1}\) and eliminate the identity columns at the other positions.
The remaining square block is the \(I,I\) principal submatrix of \(E^{-1}F\), times the restricted permutation and \(tI\) on the right.
That principal submatrix is invertible over the same cyclic field: at \(s=0\) it is a sum of diagonal copies of \(B_0^{-1}A\).
The constant matrix thus has full regular rank.
The [individual column degree inequality](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) at the \(k\) phases gives \(kr\delta\le2\sum_i|q_i|\), proving the test.

## Finding the sign pattern in a large finite module

A character on \(B_r\) is determined by its first twelve coordinates above.
Indeed \(\Phi_r\) is monic of degree twelve with unit constant term, and the first twelve consecutive translates of \(S^{-10}u\) by \(S^{-1}\) generate the cyclic module over \(\mathbb Z\).
There are \(|B_r|\) such character points in the twelve-dimensional torus.
Suppose \(|B_r|>75^{12}\).
Divide each coordinate interval \([0,1)\) into 75 equal half-open intervals.
Two character points occupy the same box.
The difference gives a nonzero rational lift \(x_0,\ldots,x_{11}\) with \(|x_i|<1/75\).
For \(r=13\), complete it by \(\sum_{i=0}^{12}x_i=0\) and extend periodically.
For \(r=26\), complete it by \(\sum_{i=0}^{12}(-1)^i x_i=0\) and extend by \(x_{i+13}=-x_i\).
These completions agree modulo one with the actual character difference by its cyclotomic relation, and \(|x_{12}|<12/75\).

Let \(V\) be the corresponding real space of dimension twelve satisfying the stated cyclic or antiperiodic relations.
Its shift has annihilating polynomial \(\Phi_r\), which is irreducible over \(\mathbb Q\).
The first twelve shifts of the nonzero rational vector \(x\) therefore form a rational basis of the rational vectors in \(V\), and so a real basis of \(V\).
Their reductions modulo one are all characters of \(B_r\).
In the first case take the target \(y_i=2/13\) at each index; subtract 2 at coordinate zero to obtain a vector of \(V\).
In the second take \(y_i=(-1)^i 2/13\), subtract 2 at zero and adjust coordinate 13 by the opposite amount to obtain a vector of \(V\).
These adjustments preserve the target phases modulo one.

Express this adjusted vector in the shift basis and round all twelve coefficients to nearest integers.
For any one output coordinate the twelve shifts use twelve distinct positions modulo 13, and hence at most one entry can have absolute value as large as \(12/75\).
The coordinate error is strictly less than \((11+12)/(2\cdot75)<2/13\).
The rounded vector gives an actual character; its coordinates can therefore be represented modulo one within that error of the unadjusted \(y_i\).
For \(r=13\) the fractions \(q_i/k\) then lie in \((0,4/13)\).
Their sum is an integer by the cyclotomic relation, hence is 1, 2 or 3.
For \(r=26\) the first thirteen fractions have alternating signs and absolute values in \((0,4/13)\); choose the next thirteen to be their exact negatives.
The sum of the first thirteen absolute values is the alternating sum and is again an integer in \((0,4)\).
In both cases the character is nontrivial, has some order \(k>1\), and meets the preceding test with \(j\le3\).
This contradicts half nullity and proves the bounds on \(|B_r|\) and \(|B|\).

## The binary primary part

If \(B/2B\ne0\), then \(S^{26}-1=(S-1)^2\Phi_{13}(S)^2=0\) in characteristic two.
Since \(S-1\) is invertible, the nonzero module has a nonzero quotient by \(\Phi_{13}(S)\).
The polynomial \(\Phi_{13}\) is irreducible over \(\mathbb F_2\) since 2 has multiplicative order twelve modulo 13, as \(2^6=-1\) and \(2^4\ne1\bmod13\).
By cyclic generation this quotient is the full twelve-dimensional simple module.
It can be identified with the binary vectors of length thirteen of even coordinate sum under cyclic shift: this shift on the even subspace is annihilated by \(\Phi_{13}\), and the subspace has dimension twelve.
Equivalently its character vectors on the thirteen consecutive translates of the cyclic generator are precisely the even vectors, since they satisfy the sum relation and there are \(2^{12}\) of them.
Use the one with a zero only at index zero, in the coordinate convention of the representation test.

At every \(z^{26}=1\), the parity sign represented by \(z^{13}\) raised to this vector combines with the marked cyclic character to give actual unitary matrices
\[
              s\longmapsto zP,\qquad
              t\longmapsto P^{10}\operatorname{diag}(z^{10},z^{-3},\ldots,z^{-3})
\]
on thirteen coordinates.
Delete the two input columns at index zero, shift each remaining column by \(z^3\), and delete the two output rows at index ten.
The remaining square matrix has 24 columns of degree at most four: the original exponents in each retained column are \(0,1,-3,-2\).
Its constant term is the permutation from the remaining indices to their translates by ten with invertible two-coordinate entries \(At\).
Deleting two input coordinates lowers the kernel dimension by at most two and deleting the output coordinates cannot lower it.
The column inequality now yields \(26(13\delta-2)\le24\cdot4\), or \(\delta\le74/169\).
This contradicts half nullity and proves \(B/2B=0\).
For finite \(B\) this excludes its entire 2-primary part.

## Computing the modules from relators

For a presentation in the normalized labels, track the prefix height \(h\bmod26\) of each word, starting at zero.
In a relator, \(s^{\pm1}\) only changes the height; \(t\) contributes \(X^h\) and then increases the height by ten; \(t^{-1}\) first decreases it by ten and contributes minus the new \(X^h\).
The resulting polynomial \(f_w\) describes the relator as an additive translation in the split metabelian group on one cyclic module generator.
In the actual metabelian quotient \(s^{26}=1\), so it can be added when computing that quotient.
After imposing it and commuting all conjugates of \(t s^{-10}\), the group before the remaining relators is \((\mathbb Z[X]/(X^{26}-1))\rtimes C_{26}\).
Every defining relator now has height zero.
Its normal closure in this split group imposes the ideal generated by all its shifts, hence
\[
 B_r \cong \mathbb Z[X]/\bigl(\Phi_r(X),\, f_w(X)\text{ for the defining relators }w\bigr).
\]
For a finite presentation integral matrices of height twelve give these quotient sizes by Smith reduction.
The particular finite-character sign tests can be run directly even when a quotient size is below the uniform bound.
The argument does not decide whether the remaining bounded metabelian quotients can occur together with fractional rank.

## Assessment history

### Decision the-finite-metabelian-quotient-at-order-26

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:12 |
| status | proved |
| reason | Independent inspection verified the cyclotomic bounds, binary case and quotient calculation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The bounds on both cyclotomic quotients and their product. |
| argument | [The cyclic coefficient module](#the-cyclic-coefficient-module) | The split marking and invertibility of the sum and difference with the identity. |
| argument | [A representation test for a single finite character](#a-representation-test-for-a-single-finite-character) | Faithful evaluation of each finite character. |
| argument | [Finding the sign pattern in a large finite module](#finding-the-sign-pattern-in-a-large-finite-module) | The count of boxes, rational independence and approximation error. |
| argument | [The binary primary part](#the-binary-primary-part) | The binary sign bound and oddness at half rank. |
| argument | [Computing the modules from relators](#computing-the-modules-from-relators) | Recovering the two quotients from a finite presentation. |
| review | [The finite metabelian quotient at order 26](../audits/reviews/Yin_R_A0189_v1.md#the-finite-metabelian-quotient-at-order-26) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-finite-metabelian-quotient-at-order-26)
