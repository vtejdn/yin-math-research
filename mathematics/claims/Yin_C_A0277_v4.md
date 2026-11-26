---
author: Yin
---

# A common group element is necessary for half nullity at arbitrary coefficient moduli

## Statement

Let the rows of \(H\) be \((1,1,1)\), \((1,\lambda u,\mu v)\), and \((1,\sigma w,\theta z)\) in the regular representation of a discrete group, with arbitrary nonzero complex coefficients.
Suppose \(A=\langle u,v\rangle\) and \(B=\langle w,z\rangle\) are free on their indicated pairs.
If \(A\cap B=\{1\}\), then
\[
                              \dim_G\ker H<\frac12
\]
with the unnormalized coordinate trace.
Consequently a half kernel for the [four-binomial matrix under scalar injectivity](Yin_C_A0273_v1.md#statement) requires a nonidentity element common to the two free face subgroups.
This applies after any choice of common row and also to the adjoint after normalization.

For each \(K\ge1\) there exist an integer \(R\) and \(\epsilon>0\) depending only on \(K\) with the following property.
Suppose all four moduli lie in \([1/K,K]\).
If the radius-\(R\) word balls in the two indicated free bases intersect only in the identity, then \(\dim_G\ker H\le1/2-\epsilon\).
These constants are existential; for rows close to unit moduli there is a separate [explicit radius and gap](Yin_C_A0281_v1.md#statement).

## A constant change of metric balances the first projection

Write \(W=\mathbf1^\perp\subset\mathbb C^3\), and let \(P,Q\) be the projections onto the kernels of the second and third rows on \(W\), as in the [two-row calculation](Yin_C_A0277_v1.md#the-scalar-coefficient-of-each-row-projection).
Both have unnormalized trace one and the trace of their meet is \(\delta=\dim_G\ker H\).
Any invertible constant \(T:W\to W\) preserves the dimension of the intersection while transforming the two ranges by the same map.
Use a bar for the matrix of identity Fourier coefficients.

For every constant line \(E\subset W\), the intersection of \(\operatorname{ran}P\) with \(E\otimes\ell^2(G)\) is zero.
Indeed on a spanning constant column \((c_1,c_2,c_3)\) the second row is the nonzero free-group scalar \(c_1+\lambda c_2u+\mu c_3v\), since \(1,u,v\) are distinct.
It is regularly injective by the [free-group division-ring theorem](../audits/literature/Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate) and subgroup inclusion.

Let \(\mathcal B\) consist of positive semidefinite constant matrices of trace one on \(W\).
It is a closed real three-ball, since subtracting \(I_W/2\) gives the operator-norm ball of radius \(1/2\) in the real three-dimensional space of traceless Hermitian two-squares.
For \(T\in\mathcal B\) let \(P_T\) be the orthogonal image projection of \(TP\).
It has trace one for invertible \(T\).
At a boundary point \(T=e\) of rank one, the preceding transversality to \(\ker e\) gives \(\operatorname{rk}(eP)=1\); hence the projection is the full constant \(e\).

The map \(T\mapsto\overline{P_T}\) is continuous.
Indeed for \(T_j\to T\), set \(D=TP,\ p=P_T,\ p_j=P_{T_j}\).
Since \((I-p_j)T_jP=0\), one gets \(\|(I-p_j)D\|_2\to0\) in the matrix trace norm of \(L^2\).
On the spectral projection \(d_\eta=\mathbf1_{[\eta,\infty)}(DD^*)\) this gives \(\operatorname{Tr}((I-p_j)d_\eta)\le\eta^{-1}\|(I-p_j)D\|_2^2\).
Letting \(\eta\downarrow0\), with \(d_\eta\uparrow p\), proves \(\operatorname{Tr}((I-p_j)p)\to0\).
All these image projections have the same trace, so \(p_j\to p\) in \(L^2\), giving convergence of the trace matrices.
The map from \(\mathcal B\) to itself is the identity on its boundary.
Omitting its center would give a retraction to that boundary by radial projection, contrary to the [no-retraction theorem, Hatcher, Corollary 2.15](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf).
Thus some interior, invertible \(T\) gives \(\overline{P_T}=I_W/2\).
Fix this \(T\) and let \(Q_T\) be the image projection of \(TQ\).

Since \(P_T,Q_T\) have entries in their respective subgroup von Neumann algebras, trivial intersection gives
\[
        \operatorname{Tr}(P_TQ_T)
            =\operatorname{tr}_W(\overline{P_T}\,\overline{Q_T})=1/2
\]
by the group Fourier coefficients.
The compression \(P_TQ_TP_T\) dominates their meet, giving \(\delta\le1/2\).
Equality would make that compression equal the meet by faithfulness, and therefore \(P_T\) and \(Q_T\) would commute.
For example, \(P_TQ_T(I-P_T)Q_TP_T=P_TQ_TP_T-(P_TQ_TP_T)^2\) would vanish.

## The coefficient lines after the change of metric

Use the [three-edge covering tree](Yin_C_A0277_v2.md#the-row-projection-on-the-three-regular-tree) for either free pair.
At a left vertex \(h\) store its transformed state \(f(h)\in W\).
Its original three edge values are \(l_i(f(h))\), where \(l_i:W\to\mathbb C\) is coordinate \(i\) of \(T^{-1}\).
The first row equation is automatic.
At a right vertex the three edge values, each from a different adjacent left vertex, satisfy their one linear relation with the three nonzero coefficients of the row in question.
These are exactly the equations of the transformed kernel inside \(\ell^2(J;W)\) for the relevant free group \(J\); the norm is the sum of the ordinary squared norms of the transformed states.

Denote this Hilbert kernel by \(\mathcal K\), its projection by \(D\), and evaluation of its state at \(h\) by \(E_h:\mathcal K\to W\).
Then \(E_hE_h^*=\overline D\) at every \(h\), by right translations, and the Fourier coefficient at \(h\) is \(D_h=E_hE_1^*\).
We describe these coefficients when \(\overline D\) is invertible.
Put \(a_i=l_i^*(1)\), identified with a nonzero vector of \(W\).

Cut the tree edge of color \(i\) at a chosen left vertex \(h\).
Solutions with \(l_i(f(h))=0\) are an orthogonal sum of solutions supported on the two halves.
Indeed restriction to either half still satisfies every right-vertex equation, as the only removed contribution across the cut is zero.
The orthogonal complement of this sum in \(\mathcal K\) is the line spanned by \(E_h^*a_i\), the representing vector of this boundary value; it is nonzero since \(\overline D\) is invertible.
Its state at \(h\) is \(\overline D a_i\).
For \(h\ne1\), cut the edge at \(h\) toward the identity vertex.
Evaluation at the identity vanishes on the solutions supported on the \(h\)-side, and evaluation at \(h\) vanishes on solutions supported on the other side.
Thus the image of \(D_h\) is contained in the line through \(\overline D a_{e(h)}\), where \(e(h)\) is the color of the last edge on the geodesic from \(1\) to \(h\).
The adjoint argument gives the analogous line through \(\overline D a_{s(h)}\) for \(D_h^*\), with \(s(h)\) the first geodesic color.
Consequently each nonzero such coefficient has rank one and has exactly these two lines.

Every distance-two coefficient is nonzero.
To see this, cut at the central right vertex between the two left vertices.
Its three branches have independent left states except for the boundary-value relation \(\sum_i r_i x_i=0\), with all \(r_i\ne0\).
On branch \(i\) the least squared norm of an extension with specified edge value \(x_i\) is \(c_i|x_i|^2\) with \(0<c_i<\infty\).
Indeed surjectivity of the left state evaluation follows from invertibility of \(\overline D\); it gives feasible branch data, and continuity of the evaluation and projection onto the closed affine solution set give strict positivity and attainment for value one.
Conversely all triples satisfying the displayed relation extend by joining these three branch solutions.
For the joint boundary-value operator from \(\mathcal K\) to \(\mathbb C^3\), its product with its adjoint is therefore
\[
             C^{-1}-C^{-1}r^*(rC^{-1}r^*)^{-1}r C^{-1},
             \qquad C=\operatorname{diag}(c_i),\quad r=(r_1,r_2,r_3).
\]
Indeed the least extension norm is the \(C\)-norm on \(\ker r\), and the displayed matrix is the covariance of its inclusion into the ordinary coordinate space, obtained by projecting perpendicular to \(C^{-1/2}r^*\) before multiplying on both sides by \(C^{-1/2}\).
Every off-diagonal entry is nonzero.
Such an entry is obtained by applying the two corresponding \(l_i,l_j^*\) to the coefficient between the two left states.
This proves nonvanishing for every geodesic of length two.

## The two orders of a group product

Suppose equality held in the half bound.
Write \(P'=P_T,\ Q'=Q_T\).
For an element \(a\in A\setminus\{1\}\), the Fourier coefficient of the commutator at \(a\) equals \([P'_a,\overline{Q'}]\), by the unique \(AB\) and \(BA\) factorizations there.
More generally every mixed product \(ab\) has coefficient \(P'_a Q'_b\) in \(P'Q'\); for \(Q'P'\) its coefficient is \(Q'_{b'}P'_{a'}\) if \(ab=b'a'\) and zero if there is no such expression.
These formulas follow by bounded \(L^2\) approximation in each subgroup and uniqueness of the finite product term. [Coefficient comparison](Yin_C_A0277_v2.md#alternating-products-at-the-next-syllable-length)

Commutation forces \(\overline{Q'}\) to preserve the images of all six short \(P'_a\).
These include the three distinct lines of \(a_i\), since \(\overline{P'}=I_W/2\) and every color occurs at the end of a length-two path.
The lines are distinct because \(a_i=T^{-*}(e_i-\mathbf1/3)\) and \(T\) is invertible.
A two-square matrix preserving three distinct lines is scalar.
Since \(\overline{Q'}\) has trace one, it too equals \(I_W/2\).
Thus for both projections the output and input lines of each nonzero nonidentity coefficient are the \(a_i\)-lines of its last and first colors respectively.

Choose different colors \(i,j\) with \(a_i,a_j\) nonorthogonal; three distinct lines in \(W\) cannot be pairwise orthogonal.
There are distance-two elements \(a\in A,\ b'\in B\) with these respective end colors.
The coefficient \(P'_{a^{-1}}Q'_{b'}\) is nonzero: both short coefficients are nonzero and the first color of \(a^{-1}\) is the last color of \(a\).
Commutation therefore forces a unique expression \(a^{-1}b'=b''a''\) in opposite order with both factors nonidentity and \(Q'_{b''}P'_{a''}\ne0\).
By equality of range lines in this coefficient comparison, the last color of \(b''\) equals the first color of \(a\).

Now \(ab''=b'(a'')^{-1}\).
The coefficient \(P'_a Q'_{b''}\) is nonzero because its two adjoining lines coincide by that color identity.
Its range is the line \(a_i\).
By commutation the opposite coefficient would also be nonzero, but its range is the distinct line \(a_j\) from \(b'\).
This contradiction proves strictness for all four nonzero moduli.

## Common words at bounded coefficient ratios

It suffices to work in the subgroup generated by the four labels since regular inclusion preserves matrix ranks.
If the uniform assertion failed for some \(K\), for every positive integer \(j\) one could choose a four-marked group with the two stated free pairs and trivial intersection of their radius-\(j\) balls, coefficients in the prescribed annulus, and nullity greater than \(1/2-1/j\).
Pass to a subsequence on which all coefficients converge in that annulus and on which the truth of each word relation stabilizes, by diagonal selection on the countable free group of four letters.
The relations eventually true define a normal subgroup of that free group and hence a limiting marked group.
Both pairs remain free there.
Any fixed pair of nonidentity reduced words in the two pairs eventually lies within the tested balls, so cannot represent one common element in the limit.

The regular nullity is upper semicontinuous in this passage.
Indeed choose \(C>0\) bounding \(\|H^*H\|\) uniformly by the coefficient bound, in all groups and the limit.
For each fixed positive \(m\) the regular trace of \((I-H^*H/C)^m\) converges by finite word expansion, convergence of coefficients and stabilization of the identities.
Each such trace dominates the corresponding nullity, and the limit group's traces decrease to its nullity by spectral calculus.
The limit would therefore have nullity at least \(1/2\), contradicting strictness.
This establishes the existence of the uniform radius and gap on the stated coefficient annulus.
