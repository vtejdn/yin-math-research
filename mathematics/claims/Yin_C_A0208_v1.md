---
author: Yin
---

# A two-phase test for the twenty-dimensional binary constituent

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{25}\), with \(\chi(s)=1,\chi(t)=7\), and set \(N=[H,H]\).
Suppose the irreducible \(\Phi_{25}\) constituent of \(H_1(N;\mathbb F_2)\) occurs.
For any complex two-by-two matrices \(A,B,C,D\) with \(A\) invertible, the regular nullity of
\[
                   K=B+At-s(D+Ct)
\]
is at most \(2/5\).
Only this one corner is required to be invertible in the quantitative statement.
The trace is unnormalized on matrix coordinates.

Consequently, if \(H\) is torsion-free, satisfies regular group-ring scalar injectivity and admits a rank-\(3/2\) four-site input at the critical cyclic marking, then
\[
                         H_1([H,H];\mathbb F_2)=0.
\]
Indeed the [five-sheeted calculation](Yin_C_A0206_v1.md#the-two-cyclic-covers) leaves only the zero module or the single \(\Phi_{25}\) constituent after excluding \(\Phi_5\); the [four corners](Yin_C_A0201_v1.md#statement) must all be invertible at a half-dimensional kernel.
Thus the abelianization of the finite-index commutator subgroup in such an input must be finite of odd order.

## Two real signs are sufficient

Index 25 coordinates by \(\mathbb Z/25\), with \(Pe_i=e_{i+1}\).
For subsets
\[
                 I=\{3,7,14,21\},\qquad J=\{0,4,5,10\}
\]
write \(a_i=1_I(i)\), \(v_i=1_J(i)\).
For a nonzero complex parameter put
\[
      S(w)e_i=w^{a_i} e_{i+1},\qquad
      T(w)e_i=w^{-v_i} e_{i+7}.
\]
At \(w=1\) this gives the cyclic permutation representation \(s\mapsto P,\ t\mapsto P^7\).
At \(w=-1\) the assignment is also an actual representation of the marked group.
To see this, put \(q_0=0,\ q_{i+1}=q_i+a_i\bmod2\), consistently since \(|I|=4\).
Conjugating by the sign diagonal with entries \((-1)^{q_i}\) makes the first generator \(P\) and the second \(P^7\operatorname{diag}((-1)^{e_i})\), where
\[
                         e_i=q_i+q_{i+7}+v_i\bmod2 .
\]
The zero positions of \(e\) are exactly \(0,1,2,3,4,5,10\).
The respective numbers of ones in the five residue classes modulo five are \(2,4,4,4,4\).
This nonzero vector belongs to the simple twenty-dimensional component of the regular binary permutation module.
The [marked residual quotient](Yin_C_A0206_v1.md#the-marked-representation-and-the-residual-quotient) realizes the representation with this chosen sign vector.
The same projection onto the simple constituent is available if another constituent is present, since the nonzero cyclic generator projects onto each occurring constituent.

## The linear coefficient and the constant submatrix

Use a two-coordinate block per index and let \(X(w)\) be the original rectangle with the \(s\)-translation multiplied by \(S(w)\) and the \(t\)-translation by \(T(w)\) on the auxiliary coordinates.
At both real signs unitary absorption gives \(\dim_H\ker X(w)=25\delta\), where \(\delta=\dim_H\ker K\).
Multiply the two columns at position \(i\) by \(w^{v_i}\) to obtain \(Q(w)\).
In these columns the four possible exponents, in the order of terms \(1,s,t,st\), are
\[
                         v_i,\quad a_i+v_i,\quad 0,\quad a_{i+7}.
\]
Since \(I\cap J=\varnothing\) and \(I-7\subseteq I\cup J\), the result is \(Q_0+wQ_1\).
Only the eight block columns indexed by \(I\cup J\) can contribute to \(Q_1\).
Thus \(\operatorname{rk}_H Q_1\le16\).

For \(w\ne0\), multiply \(Q(w)\) on the right by the constant unit \(P^{-7}t^{-1}\), using identity matrices on the appropriate coordinates.
The result is \(X(w)T(w)^{-1}t^{-1}\).
At zero the resulting constant matrix is
\[
           K_0=A+B t^{-1}V-s C U-s D t^{-1} UV ,
\]
where \(Ue_i=e_{i+1}\) if \(i\notin I\) and zero otherwise, and \(Ve_{i+7}=e_i\) if \(i\notin J\) and zero otherwise.
Here \(U,V\) act on the auxiliary indices and commute with all group-ring coefficient matrices.
In particular \(\operatorname{rk}K_0=\operatorname{rk}Q_0\).
Delete block row and column 6.
In the following order every surviving arrow of \(U,V,UV\) points from an earlier to a later vertex:
\[
 4,5,22,15,8,23,16,9,10,24,0,1,2,3,17,18,11,19,12,20,13,21,14,7 .
\]
The check uses precisely the arrows \(i\to i+1\) for \(i\notin I\), \(i+7\to i\) for \(i\notin J\), and \(i+7\to i+1\) for \(i\notin I\cup J\), omitting arrows incident to 6 in each list.
This last list includes two-step arrows with intermediate vertex 6 when their endpoints survive.
Thus the 24-block submatrix is triangular with diagonal entries \(A\).
It is invertible over the group ring by finite triangular substitution and \(\dim_H\ker Q_0\le2\).

## The nullity comparison

Write \(E_+=\ker(Q_0+Q_1)\) and \(E_-=\ker(Q_0-Q_1)\) in affiliated modules.
The column scalings at the two signs are invertible, so each has dimension \(25\delta\).
The image of \(E_++E_-\) under \(Q_0\) lies in the image of \(Q_1\), and its intersection with \(\ker Q_0\) costs at most two dimensions in the domain.
It follows that \(\dim(E_++E_-)\le16+2\).
Also \(E_+\cap E_-\subseteq\ker Q_0\) by addition of the two defining equations.
Dimension additivity now gives \(50\delta\le16+2+2=20\).
This actual two-phase bound excludes half nullity in the twenty-dimensional branch; the case of zero binary homology remains open.

## Assessment history

### Decision two-phase-binary-test

| Field | Value |
| --- | --- |
| date | 2026-11-26T07:51 |
| status | proved |
| reason | Independent review verified the signed action, the twenty-four-block minor and the resulting strict bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-corner estimate and the complete binary homology obstruction. |
| argument | [Two real signs are sufficient](#two-real-signs-are-sufficient) | The signed quotient and the five parity counts. |
| argument | [The linear coefficient and the constant submatrix](#the-linear-coefficient-and-the-constant-submatrix) | Column exponents, multiplication order and the triangular minor. |
| argument | [The nullity comparison](#the-nullity-comparison) | Unnormalized finite-dimensional module estimate. |
| review | [Two real signs on twenty-five positions](../audits/reviews/Yin_R_A0188_v1.md#two-real-signs-on-twenty-five-positions) | Independent whole-proof finding. |

## Current assessment

[Selected decision](#decision-two-phase-binary-test)
