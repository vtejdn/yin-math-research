---
author: Yin
---
# Rational projection specialization for the Promislow four-coset model

This investigation serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route seven](../strategies/Yin_S_A0007.md).
The fixed starting inputs are the [index-two rational-projection parity mechanism](../ledger/Yin_L_A0022_v1.md#a-rational-projection-lemma) and the [actual Promislow four-coset representation](../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model).
The current question is whether bounded rational specialization and actual compatible symmetries independently force divisibility by four of the generic rank of every group-ring matrix kernel projection in this representation.
The Promislow group is already covered by established virtually abelian results; the present task tests a mechanism and assumes no Atiyah or division conclusion for that group.

## Fixed setting and proposed test

Let
\[
P=\langle a,b\mid b^{-1}a^2b=a^{-2},\ a^{-1}b^2a=b^{-2}\rangle,
\quad x=a^2,\quad y=b^2,\quad z=(ab)^2.
\]
The verified source facts retained in L_A0010 give a torsion-free group and a normal subgroup \(N=\langle x,y,z\rangle\cong\mathbb Z^3\) of index four.
Use the actual coset basis \((1,a,b,ab)\), the coefficient field \(F=\mathbb C(x,y,z)\), and its torus involution.
For a finite group-ring matrix, its actual rational orthogonal kernel projection is obtained by the rational Gram construction as in L_A0022.
Its generic field rank \(d\) gives actual group kernel dimension \(d/4\), through L_A0010's faithful trace identity.
The obligation being tested is \(4\mid d\).
Specializing a projection may preserve \(d\) after removability has been proved; specializing the original matrix need not preserve its kernel dimension.

The test is to derive the actual semilinear commutant symmetries, then retain their cocycle information through successive torus coordinate specializations.
Any lost constraint or counterexample must be stated for the explicit proposed inference rather than for the original Atiyah question.

## The actual left matrices and right semilinear symmetries

Separate the two generators in L_A0010's matrix for \(1+a+b\):
\[
A=\rho(a)=
\begin{pmatrix}
0&x&0&0\\
1&0&0&0\\
0&0&0&x^{-1}\\
0&0&1&0
\end{pmatrix},
\qquad
B=\rho(b)=
\begin{pmatrix}
0&0&y&0\\
0&0&0&x^{-1}z\\
1&0&0&0\\
0&xy^{-1}z^{-1}&0&0
\end{pmatrix}.
\tag{1}
\]
Direct multiplication gives
\[
A^2=\operatorname{diag}(x,x,x^{-1},x^{-1}),
\quad
B^2=\operatorname{diag}(y,y^{-1},y,y^{-1}),
\tag{2}
\]
and
\[
AB=
\begin{pmatrix}
0&0&0&z\\
0&0&y&0\\
0&y^{-1}z^{-1}&0&0\\
1&0&0&0
\end{pmatrix},
\quad
(AB)^2=\operatorname{diag}(z,z^{-1},z^{-1},z).
\tag{3}
\]
The involution on \(F\) conjugates complex constants and inverts all three variables.
The matrices \(A,B\) are unitary for this involution, as is also immediate from their monomial entries on the torus.

Right multiplication by a group element commutes with the left group action but is semilinear in this right-coefficient coset convention.
Put
\[
\sigma_a(x,y,z)=(x,y^{-1},z^{-1}),
\qquad
\sigma_b(x,y,z)=(x^{-1},y,z^{-1}).
\tag{4}
\]
These are the actual conjugation actions \(n\mapsto a^{-1}na\) and \(n\mapsto b^{-1}nb\) on \(N\), equivalently the diagonal formulas (2)--(3).
In coordinates, right multiplication by \(a\) and \(b\) is respectively \(C_a\sigma_a\) and \(C_b\sigma_b\), where
\[
C_a=
\begin{pmatrix}
0&x&0&0\\
1&0&0&0\\
0&0&0&y^{-1}z^{-1}\\
0&0&xy^{-1}z^{-1}&0
\end{pmatrix},
\qquad
C_b=
\begin{pmatrix}
0&0&y&0\\
0&0&0&y\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}.
\tag{5}
\]
For example, \(ba=ab\,xy^{-1}z^{-1}\) and \(aba=b\,y^{-1}z^{-1}\) give the last two columns of \(C_a\).
For a coset representative \(r\), the identity \(rna=(ra)(a^{-1}na)\) explains the automorphism as well as the monomial coefficient.
The same calculation gives \(C_b\).
All these matrices are unitary almost everywhere on the torus, and the automorphisms preserve Haar measure.

The square identities are
\[
C_a\sigma_a(C_a)=xI_4,
\qquad C_b\sigma_b(C_b)=yI_4.
\tag{6}
\]
For right multiplication by \(ab\), the order of composition is \(C_b\sigma_b(C_a)\sigma_b\sigma_a\).
Writing \(C_{ab}=C_b\sigma_b(C_a)\) and \(\sigma_{ab}=\sigma_b\sigma_a\), direct multiplication gives
\[
C_{ab}\sigma_{ab}(C_{ab})=zI_4.
\tag{7}
\]
Thus the actual cocycle contains three independent square translations before specialization.

For an \(m\)-by-\(n\) group-ring matrix with image \(M\), write \(C_{a,n}=I_n\otimes C_a\), and similarly for the other sizes and generator.
Commutation of left and right multiplication gives
\[
M C_{a,n}=C_{a,m}\sigma_a(M),
\qquad
M C_{b,n}=C_{b,m}\sigma_b(M).
\tag{8}
\]
The actual rational orthogonal kernel projection \(P_M\) therefore satisfies
\[
P_M C_{a,n}=C_{a,n}\sigma_a(P_M),
\qquad
P_M C_{b,n}=C_{b,n}\sigma_b(P_M).
\tag{9}
\]
Indeed, on the generic torus set the monomial matrices give unitary correspondences of the kernel fibers; uniqueness of orthogonal projection proves (9) there and hence as rational identities.
The generator identities imply covariance for every right group translation, including all their products and inverses.

## What coordinate specialization really preserves

Let \(\Pi\in M_{4n}(F)\) be any rational orthogonal projection almost everywhere on the torus, satisfying (9).
Every entry is bounded by one there.
The L_A0022 pole argument applies with the other two variables as parameters: a nonzero leading coefficient of a pole along \(y=1\) stays nonzero for almost every parameter pair, while Fubini supplies a pair on which the projection bound holds for almost every \(y\).
The resulting one-variable pole would violate that bound on a positive-measure arc.
Thus every entry is regular along \(y=1\) over \(\mathbb C(x,z)\), and
\[
\Pi_y=\Pi(x,1,z)\in M_{4n}(\mathbb C(x,z))
\tag{10}
\]
is defined.
It remains idempotent, and its field rank remains \(d\) because the trace of an idempotent is its rank and the constant integer trace specializes unchanged.
The involution commutes with this specialization, so \(\Pi_y^\star=\Pi_y\); consequently its generic torus evaluations remain orthogonal projections and bounded.
Both automorphisms preserve the divisor \(y=1\), and the monomial matrices have no pole there, so the full identities (9) descend.
The same statements hold for \(x=1\) or \(z=1\), and iteratively for any sequence of coordinate specializations.
This proves all claimed preservation facts for \(\Pi\) itself and makes no rank assertion for a specialized \(M\).

## A rank-two counterexample to the surviving-symmetry inference

Specialize first at \(y=1\), leaving \(x,z\) algebraically independent.
Let
\[
B_y=
\begin{pmatrix}
0&0&1&0\\
0&0&0&x^{-1}z\\
1&0&0&0\\
0&xz^{-1}&0&0
\end{pmatrix},
\qquad
E_y=\frac{I_4+B_y}{2}.
\tag{11}
\]
Equation (2) gives \(B_y^2=I_4\), and unitarity gives \(B_y^\star=B_y\).
Therefore \(E_y\) is a rational orthogonal projection on every torus point, with no exceptional singularities.
Since \(\operatorname{Tr}B_y=0\),
\[
\operatorname{rank}_{\mathbb C(x,z)}E_y
=\operatorname{Tr}E_y=2.
\tag{12}
\]
In particular its rank is not divisible by four.

Every specialized identity (9) holds for \(E_y\).
To see this without selecting only a subset of the symmetries, first apply (8) to the original left multiplication matrix \(B\).
Specialization gives
\[
B_y C_{a,y}=C_{a,y}\sigma_{a,y}(B_y),
\qquad
B_y C_{b,y}=C_{b,y}\sigma_{b,y}(B_y),
\]
where
\[
\sigma_{a,y}(x,z)=(x,z^{-1}),
\qquad \sigma_{b,y}(x,z)=(x^{-1},z^{-1}).
\]
Adding the identity and dividing by two gives the same equations for \(E_y\), and therefore all their group-word consequences.
The remaining square and cocycle identities (6)--(7) still hold after substitution.
Thus neither omitted right-translation symmetry nor omission of a surviving cocycle equation explains the counterexample.
It also has full rationality, boundedness, selfadjointness and constant rank, rather than merely measurable fibers.

Further specialization at \(x=1\) and then \(z=1\), in either order, keeps this explicit projection and its rank two.
At the final point,
\[
E_{111}=\frac12
\begin{pmatrix}
1&0&1&0\\
0&1&0&1\\
1&0&1&0\\
0&1&0&1
\end{pmatrix}.
\tag{13}
\]
It commutes with both surviving regular permutation matrices of \(C_2^2\), and all ranks and symmetry relations are still valid.

The loss occurs at the first specialization, not only at the final common fixed point.
Originally \(b^2=y\) is a nontrivial translation relation; after \(y=1\), it becomes an involution relation.
In fact, \(\langle y\rangle\) is normal in the original group, and the quotient \(P/\langle y\rangle\) still has the free abelian subgroup \(N/\langle y\rangle\cong\mathbb Z^2\) of index four.
The coset of \(b\) is a nonidentity involution because it was outside \(N\).
Formula (11) is its ordinary averaging projection in the actual four-coset model of that torsion quotient.
It is also the exact kernel projection of the finite quotient group-ring element \(1-b\).
It has quotient von Neumann trace \(\frac14\operatorname{Tr}E_y=1/2\), exactly as an order-two averaging projection should.
This fractional trace belongs to that quotient, not to a constructed group-ring kernel projection for the original torsion-free group.

No choice of first coordinate equal to one avoids the same problem.
For \(x=1\), the projection \((I_4+A|_{x=1})/2\) has rank two and all specialized covariances.
For \(z=1\), use \((I_4+(AB)|_{z=1})/2\); formula (3) supplies its involution, trace-zero and unitarity properties.
Both are Laurent-polynomial projections and remain rank two under every later coordinate specialization.
More generally, at a symmetry-preserving fixed coordinate value \(t=\varepsilon\in\{1,-1\}\), the corresponding generator matrix \(G_t\) has square \(\varepsilon I_4\).
Choose a constant \(\mu\) with \(\mu^2=\varepsilon\) and \(|\mu|=1\).
Then \((I_4+\mu^{-1}G_t)/2\) is again a rank-two orthogonal projection satisfying every descended covariance.
Thus replacing a coordinate value one by minus one does not repair this inference.

## Exact remaining constraint and conclusion

The counterexample refutes the following proposed implication: a rational bounded projection satisfying all right-translation symmetries and cocycle identities surviving one or more such coordinate specializations must have rank divisible by four.
Already (11) violates it before the other variables have been specialized.
It does not refute divisibility for a projection before specialization or for a specialized projection together with a sufficiently strong separately proved lifting condition.

The direct pre-specialization expression \((I_4+B)/2\) is not an idempotent:
\[
\left(\frac{I_4+B}{2}\right)^2-\frac{I_4+B}{2}
=\frac{B^2-I_4}{4}
=\frac14\operatorname{diag}(y-1,y^{-1}-1,y-1,y^{-1}-1).
\tag{14}
\]
The vanished square-translation relation is therefore an explicit part of its failed lift.
No conclusion about the existence of a different rational lift of (11) is asserted here.
Ruling out a rank-two lift satisfying the original three-variable identities would require additional information retained from the unspecialized family; the descended equations and projection bounds cannot do it.

The comparison with L_A0022 is precise.
There the useful fixed locus leaves the square parameter free, and its square-root automorphism exchanges two constant-eigenspace summands, forcing equal ranks.
Here the common fixed locus of both actions (4) on the translation torus is finite, with every coordinate equal to \(1\) or \(-1\).
Killing any one of the three square translations already creates the rank-two averaging projection above, and the remaining semilinear symmetries preserve it.
Adjoining square roots of the remaining variables cannot remove this counterexample, because its displayed entries already lie in the smaller rational field and all covariance equations continue to hold under compatible extensions of the existing automorphisms.
The additional deck automorphisms fix those original-field entries.

The actual trace factor for an original group-ring matrix remains \(1/4\), and rank preservation of its projection under an allowed specialization remains valid.
What fails is the proposed divisibility argument after discarding the original liftability constraint.
The bounded investigation therefore yields a complete obstruction to that specific sequential-specialization route, not a new Atiyah theorem or counterexample.
All new calculations use the fixed L_A0010 group/model facts and L_A0022 rational linear algebra; no unverified external theorem, known division conclusion for \(P\), or new historical-priority claim is used.
