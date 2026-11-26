---
author: Yin
---

# A pole-rank bound at a four-position transfer endpoint in arbitrary size

## Statement

Let \(G\) be a discrete group, \(s,t\in G\), \(t_j=s^jts^{-j}\), and suppose \(t\) has infinite order, \(\langle t_0\rangle\cap\langle t_1\rangle=1\) and \(\langle t_1,t_2\rangle\) is nonamenable.
Let \(M(z)=P(z)Q(z)^{-1}\) with \(P(z)=Az+B,\ Q(z)=Cz+D\) regular square complex pencils of size \(h\), and assume \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\) is invertible.
Suppose \((s^{-1}M(t))^4=I_h\).
Let \(d>0\) be the largest circle pole order of either \(M\) or its inverse.
For each side \(L=M,M^{-1}\) attaining \(d\), denote the nonzero leading Laurent coefficients at its order-\(d\) circle poles by \(S_\alpha\).
Then
\[
           S_\alpha S_\beta=0\quad\text{for all such }\alpha,\beta,
             \qquad 2\sum_\alpha\operatorname{rank}_{\mathbb C} S_\alpha\le h .
\]
If either side has only simple boundary poles and at least one such pole, both sides have that property.
In this case on each side the sum of the nullities of its denominator pencil at all unit-circle roots is at most \(\lfloor h/2\rfloor\).

For the four-position [regular transfer window](Yin_C_A0183_v1.md#statement), assume the group and pencil hypotheses above and impose the fourth-power identity only at equality in the window bound.
If the four right cosets of \(\langle t_0,t_1,t_2\rangle\) represented by \(1,s,s^2,s^3\) are distinct, then \(\dim_G\ker(sI_h-M(t))\le h/4\).
A violation of the pole-rank condition above makes this inequality strict.
For example at size three, two distinct simple circle poles on a side with no higher circle poles exclude nullity \(3/4\).
The window and pole test allow labels in any discrete group satisfying the given conditions and use no scalar group-ring injectivity premise.

## A bounded left inverse for the two outer polynomial pencils

Write the inverse of the assembled matrix as \(\left(\begin{smallmatrix}E&F\\J&K\end{smallmatrix}\right)\).
Since it sends \((P,Q)^{\mathsf T}\) to \((zI,I)^{\mathsf T}\), one has
\[
             (E-zJ)M(z)=zK-F .
\]
The block row \((E-zJ,F-zK)\) has full row rank at every \(z\), being \((I,-zI)\) times an invertible matrix.
Over \(\mathbb C(z)\) both its components factor on the left through \(E-zJ\), which is therefore a regular pencil.
Exchanging the original two block rows supplies a regular linear left denominator of \(M^{-1}\) as well.
This construction includes pencils with two singular coefficient corners.

For a regular pencil \(A_0+zA_1\) and a group translation \(x\), a sequence of unit vectors with \((A_0+xA_1)\xi_n\to0\) satisfies \((xI-K_0)\xi_n\to0\) for some fixed numerical matrix \(K_0\).
Choose \(z_0\) with \(D_0=A_0+z_0 A_1\) invertible and set \(T=D_0^{-1}A_1\).
After constant left multiplication the defect is \((I+(x-z_0)T)\xi_n\).
On the generalized zero space of \(T\) this polynomial in \(x\) has a bounded polynomial inverse by nilpotence.
The component of \(\xi_n\) there tends to zero.
On the invariant complementary subspace \(T\) is invertible, and multiplication by \(T^{-1}\) gives the claim with \(K_0=z_0 I-T^{-1}\).
The two constant projections for this direct sum commute with \(x\), so orthogonality of the splitting is unnecessary.

Consequently the two regular left denominators at \(t_1,t_2\), stacked as a column, are bounded below.
Otherwise the same sequence would satisfy the two approximate constant-matrix covariance equations just obtained, contrary to the [nonamenable two-generator argument](Yin_C_A0302_v1.md#a-lower-bound-for-two-linear-left-denominators), applied with inverse generators if necessary.
For \(W=M(t_1)M(t_0)\) and \(g=s^4\), the fourth-power equality gives
\[
 W=M(t_2)^{-1}M(t_3)^{-1}g,\qquad W^{-1}=s^{-2}Ws^{-2}.
\]
Multiplying by the two left denominators and using their bounded joint left inverse expresses \(W\) as a sum of two bounded left multiples of \(M(t_0)\) and \(M(t_3)^{-1}g\).
Each has singular-value distribution \(O(v^{-1/d})\) as \(v\to\infty\) by cyclic spectral calculus.
Truncating the two terms at norm \(v\) and bounding the rank of the discarded parts proves the same tail for \(W\), and then for its unitarily translated inverse.

## Residue interactions and the independent subspaces

Choose a side \(L\) attaining \(d\) and put \(p_*=1/d\).
Its two-factor product is \(W\) or \(W^{-1}\), with the order of the two neighboring variables reversed for the inverse.
For \(0<p<p_*\) the [bounded truncation and trace inequality](Yin_C_A0302_v1.md#a-fractional-moment-lower-bound-detects-interacting-residues) give a lower bound for its absolute \(p\)-moment by
\[
               \operatorname{tr}_h\!\left(\int |L|^p\ \int |L^*|^p\right),
\]
using probability Haar integrals in the two factors.
By the upper tail the moment is \(O((1-dp)^{-1})\) as \(p\uparrow p_*\).
After multiplication by \(1-dp\), the first integral tends to \(\pi^{-1}\sum |S_\alpha|^{p_*}\), and the second has the adjoint limit.
Indeed on a local angle coordinate \(b\) at each pole the matrix \(b^d L\) extends continuously, with leading value a unit scalar times \(S_\alpha\).
The normalized measures \((1-dp)|b|^{-dp}\,db/(2\pi)\) concentrate at zero with mass \(1/\pi\).
Lower-order poles contribute bounded integrals near \(p_*\).
Multiplying the moment bound by \((1-dp)^2\) now gives \(S_\alpha S_\beta=0\) term by term as in the simple-pole proof.

Take \(L=M\), writing the inverse case with the two original pencils exchanged.
At each selected pole let \(B_\alpha\) be the leading singular coefficient of \(Q(z)^{-1}\).
Its image lies in \(\ker Q(\alpha)\), and \(B_\alpha Q(\alpha)=0\) by the inverse identity on the other side.
The assembly makes \(P(\alpha)\) injective on \(\ker Q(\alpha)\), by applying it to \((\alpha v,v)\).
There is no loss of pole order in multiplying on the left by \(P\).
Thus \(S_\alpha=P(\alpha)B_\alpha\), with the same rank and the same row space as \(B_\alpha\).

For distinct finite roots \(\alpha\) of a regular pencil the right nullspaces are independent, and so are the left nullspaces.
Indeed normalization at \(z_0\) identifies the right nullspaces with eigenspaces of \(T\) at the distinct eigenvalues \(-1/(\alpha-z_0)\).
The same calculation for the transpose gives the assertion for rows.
It follows that the row spaces of the selected residues are independent.
Their images are also independent: a relation \(\sum P(\alpha)v_\alpha=0\), with \(v_\alpha\in\operatorname{im}B_\alpha\), makes the assembled matrix kill \(\sum(\alpha v_\alpha,v_\alpha)\).
Hence \(\sum v_\alpha=0\) and all \(v_\alpha=0\).
The mutually annihilating residues have the sum of their ranges in the common kernel.
The dimension of this sum and the codimension of that common kernel both equal the stated sum of ranks.
This proves the factor two.

Finally, if one side has only simple circle poles, the [two-factor cutoff bound](Yin_C_A0290_v1.md#singular-value-bounds-for-two-cyclic-factors) gives \(O(v^{-2/3})\) for its product, in every matrix size.
A pole of order at least two on the opposite side would give a lower bound \(cv^{-1/2}\) or larger for the same singular-value distribution.
A bounded opposite side would instead contradict the lower bound for the given simple pole.
Thus all poles on both sides are simple.
At a simple pole of the reciprocal pencil, the normalized \(T\) has no nontrivial Jordan block at the corresponding eigenvalue and the reciprocal residue has rank equal to the nullity there by its spectral idempotent.
This gives the stated simple-pole form and the window application.
