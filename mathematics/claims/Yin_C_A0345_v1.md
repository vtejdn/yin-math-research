---
author: Yin
---

# A uniform gap for assemblies close to a unitary at any independent pair of signs

## Statement

Let a torsion-free group \(H=\langle g,h\rangle\) have regular scalar group-ring injectivity and admit both independent sign changes of its two marked generators.
For a complex two-square rectangle \(B+Ah-g(D+Ch)\) of noninteger regular nullity \(\delta\), write \(T=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\).
The matrix trace is unnormalized in \(\delta\).
There are absolute positive constants \(\gamma,\epsilon\) such that
\[
              \|T\|\,\|T^{-1}\|\le1+\gamma
                    \quad\Longrightarrow\quad\delta\le\tfrac12-\epsilon .
\]
The same conclusion holds when the condition number bound is achieved after left and right multiplication of the rectangle by invertible constant two-square matrices, acting on all four coefficients.
In particular this excludes the full unitary assembly family, including the index-four characters of numerical rank at least three at noncyclic order twenty.
It does not require a fifth-root character.
A finite procedure with real polynomial equations and inequalities can produce a positive rational pair \(\gamma,\epsilon\).
No numerical value for the pair is asserted here.

## Four-step words and the commutator kernel

The [two-square reduction](Yin_C_A0184_v1.md#statement) makes the assembly invertible and the two cyclic pencils regular for noninteger nullity.
A nonzero homomorphism to \(\mathbb Z\) would imply integer nullity by the [indicable-pair theorem](Yin_C_A0179_v1.md#statement).
As \(H\) is finitely generated, its abelianization is therefore finite.
A nontrivial intersection of \(\langle h\rangle\) and \(g\langle h\rangle g^{-1}\) would give a cyclic subgroup \(\langle h^m\rangle\), \(m>0\), normalized by \(g\).
Indeed commensuration gives a homomorphism to \(\mathbb Q^\times\) with finite image by abelianization, so conjugation preserves the cyclic power up to inversion.
An identity \(g^{-1}h^i g^{-1}h^j=1\) also normalizes a nonzero power: \((g^{-1}h^i)^2=h^{i-j}\) is central, and \(i=j\) would make the group cyclic.
The [cyclic denominator proof](Yin_C_A0343_v1.md#which-group-words-can-contribute-to-the-trace) then gives integral nullity by taking a nonzero off-diagonal cyclic entry as pivot.
If both off-diagonal entries vanish the two scalar diagonals give the same conclusion by clearing their cyclic denominators separately.
Thus neither kind of relation occurs.
In particular no word \(g^{i_1}h^{j_1}g^{i_2}h^{j_2}\), with all four exponents in \(\{1,-1\}\), is the identity.
The opposite \(g\)-sign case uses the trivial intersection and the equal-sign case uses the two-step assertion and inversion.

Use the two involutions
\[
     J_g=\begin{pmatrix}0&gI_2\\g^{-1}I_2&0\end{pmatrix},
     \qquad L_T=TJ_hT^{-1},\qquad A_T=J_gL_T ,
\]
where \(J_h\) has the same form as \(J_g\).
The four [signed graph intersections](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator) are the four joint eigenspaces of \(J_g,L_T\) on the commutator kernel.
That kernel is \(\ker(A_T^2-I)\), since the commutator is \(A_T-A_T^{-1}\).
The dimension of each joint eigenspace is \(\delta\) by the two genuine signs.
Let \(p\) be the orthogonal kernel projection and let \(t\) be the regular matrix trace divided by four.
Then \(t(p)=\delta\).
For every numerical unitary \(V\in U(4)\), the operator \(A_V=J_g VJ_hV^*\) is unitary and \(t(A_V^2)=0\): its words are among the length-four words just excluded.

## A positive lower bound from finitely many equality patterns

For a fixed group with the stated signs, word inequalities and scalar injectivity it is impossible that \(A_V^4=I\) for any numerical unitary \(V\).
Otherwise \(E=(I+A_V^2)/2\) is a group-ring projection of unnormalized trace two, using \(t(A_V^2)=0\).
Its range is the commutator kernel, where the two selfadjoint involutions commute.
They both preserve the range and therefore commute with \(E\).
The four joint projections \((I+\xi J_g)(I+\eta L_V)E/4\), \(\xi,\eta=\pm1\), are group-ring matrices.
Independent sign twists permute them transitively and preserve trace, forcing each to have unnormalized trace \(1/2\).
Each nonzero group-ring matrix has regular rank at least one because it has a nonzero scalar entry.
This is a contradiction.

Expand \(A_V^4-I\) before identifying any group words.
It is a sum on the identity and at most \(4^4\) alternating words with eight letters, with numerical matrix coefficients polynomial in the real and imaginary parts of \(V\).
All possible groups induce only finitely many partitions of this finite list by equality of words.
For a partition \(\pi\) put
\[
    f_\pi(V)=\frac14\sum_{C\in\pi}
              \left\|\sum_{w\in C}D_w(V)\right\|_{\mathrm{HS}}^2 ,
\]
where \(D_w\) are the coefficients, including the negative identity term.
For an actual partition this is \(\|A_V^4-I\|_{2,t}^2\).
Whenever the group has the conditions established above, \(f_\pi\) has no zero on \(U(4)\) by the projection argument.
It then has a strictly positive minimum by compactness.
Take \(c>0\), at most one, below all positive minima for partitions with no zero.
This is a finite choice independent of the marks, group and coefficients.
One can enumerate all partitions, decide by real quantifier elimination which admit a zero on the unitary equations, and on the others test successively smaller positive dyadic lower bounds for the polynomial on this compact set.
Partitions discarded at a zero cannot come from a group in this argument.
This procedure requires no test for realization of a formal word partition.

## Comparing the actual kernel with the unitary product

Rescale \(T\) so its smallest singular value is one and write its polar decomposition \(T=V P\); set \(\kappa=\|T\|\|T^{-1}\|\).
Subtracting the midpoint of \([1,\kappa]\) in the commutator with \(J_h\) gives \(\|[P,J_h]\|\le\kappa-1\).
As \(\|P^{-1}\|=1\) this yields
\[
      \|A_T-A_V\|\le\kappa-1,\qquad
      \|A_T^2-A_V^2\|\le \kappa^2-1=:a.
\]
Put \(S=A_V^2\), so \(S\) is unitary, \(t(S)=0\), and \(\|(S-I)p\|\le a\).
Writing the normalized \(L^2\) norm as \(\|\cdot\|_2\), one has
\[
 \begin{split}
   \|S^2-I\|_2^2
      &\le4\|(S-I)p\|_2^2+4\|(S+I)(I-p)\|_2^2\\
      &=8-16\delta+8\|(S-I)p\|_2^2
       \le8-16\delta+8a^2\delta .
 \end{split}
\]
Indeed the two factorizations of \(S^2-I\) bound the two complementary input summands separately.
The equality uses \(\|S+I\|_2^2=2\) and \(\|(S+I)p\|_2^2+\|(S-I)p\|_2^2=4t(p)\).
On the other hand \(\|S^2-I\|_2^2\ge c\) by the partition bound.
The [three-parameter budget](Yin_C_A0329_v1.md#statement) and the single sign negating \(g\) give \(2\delta\le1\), since the two eigenspaces of \(g^{-1}(Ah+B)(Ch+D)^{-1}\) at \(1,-1\) have equal dimension \(\delta\).
Choose \(\gamma>0\) small enough that \(((1+\gamma)^2-1)^2\le c/8\).
The inequalities then give \(\delta\le1/2-c/32\), proving the claim.
Constant row and column changes on the two-square rectangle multiply its assembly by the corresponding repeated diagonal factors and preserve kernel dimension.
