---
author: Yin
---

# Two rank-two commutator witnesses and a rational matrix on a cyclic subgroup

## Statement

Let \(G\) be torsion-free and assume that every nonzero scalar of \(\mathbb CG\) is injective in the regular representation.
Let \(s,t\ne 1\) be distinct up to inverse, let \(R_g\) be right multiplication by \(g\) on \(H=\ell^2(G)\), and suppose \(T_s,T_t\) are bounded operators of complex rank two.
Write \(F=[R_s,T_s]+[R_t,T_t]\).
Suppose \(F\) has ordinary complex rank one.
Use the [two endpoint lists](Yin_C_A0166_v2.md#endpoint-dimensions-and-a-cyclic-chain) of minimal decompositions of the witnesses.
Regard the second list as right translates after taking adjoints, which replaces its labels by \(s^{-1},t^{-1}\).

At least one list has endpoint span \(X\) of dimension at most four.
On **each** such list, writing \(s,t\) for its oriented labels, the following are necessary.

1. Both starting two-planes \(E,J\) and their translated two-planes split the same four-space:
   \[
                      X=E\oplus Es=J\oplus Jt.
   \]
2. There are two-by-two complex polynomial matrices \(C(Z),D(Z)\) of degree at most one such that both determinants are nonzero polynomials.
   The four columns obtained by stacking the constant and linear coefficients of \([C,D]\) form a basis of \(\mathbb C^4\).
   Writing \(M(Z)=C(Z)^{-1}D(Z)\), a row \(y=(y_1,y_2)\) with complex-linearly independent entries in \(H\) satisfies
   \[
                     y\bigl(tI_2-M(s)\bigr)=0 .
   \]
   There are no nonzero constant columns \(c,d\in\mathbb C^2\) with \(M(Z)c=d f(Z)\) for a scalar rational function \(f\).
3. Suppose \(K=\langle s,t\rangle\) has a circle-valued character trivial on \(s\) whose value on \(t\) has finite order \(n\).
   Every vector in this \(X\), viewed as an affiliated scalar, has regular rank at most \(2/n\).
   An infinite-order value on \(t\) excludes \(F\) of rank one.
   The roles of the two labels can be exchanged.
   In particular, an order \(n\ge5\) at an isolated label excludes a rank-one boundary for which both tensor factors have regular rank \(1/2\).
   By the [prescribed-list construction](Yin_C_A0167_v2.md#a-pencil-for-the-particular-schur-scalar) this excludes half-rank Schur scalars realized with at most two occurrences of either label and no other nonidentity labels, under that character hypothesis.

If either witness has rank at most one, the [one-edge and two-label exclusions](Yin_C_A0166_v2.md#statement) apply instead.
The conditions here concern the two-by-two transfer matrix over the **actual** cyclic fraction field inside the affiliated algebra.
They leave open possible solutions with no constant direction correspondence and no excluding character.

## Excluding a chain on either tight list

The [ordinary rank inequality](Yin_C_A0166_v2.md#endpoint-dimensions-and-a-cyclic-chain) gives \(\operatorname{rank}_{\mathbb C} F\ge \dim X_1+\dim X_2-8\) for the first and second endpoint spans.
If both dimensions were at least five the boundary would have rank at least two.
Fix any list with \(\dim X\le4\).
Its two-dimensional starting spaces \(E,J\) arise from the two translated rank-two witnesses, so \(X=E+Es+J+Jt\).
The cyclic subgroup case cannot give rank one by the cited exclusion, so we may take \(t\notin\langle s\rangle\) and \(s\notin\langle t\rangle\).

If \(\dim(E+Es)<4\), the [cyclic chain lemma](Yin_C_A0166_v2.md#endpoint-dimensions-and-a-cyclic-chain) makes \(E+Es=L=v\operatorname{span}_{\mathbb C}(1,s,s^2)\).
This space has codimension at most one in \(X\).
Both \(J\cap L\) and \(\{w\in J:wt\in L\}\) have dimension at least one.
If a nonzero \(w\) belongs to both, write \(w=vp(s)\) and \(wt=vq(s)\).
The scalar \(p(s)t-q(s)\) is nonzero by disjoint coset supports, whereas its product with \(v\) on the left is zero.
This contradicts scalar injectivity, since nonzero group-ring scalars are invertible in the finite affiliated algebra \(U=\mathcal U(G)\).
The two subspaces are therefore complementary lines in \(J\).
Every vector in the first is in \(v\mathbb CG\); each vector in the second lies there too, by right translation of its endpoint by \(t^{-1}\).
Consequently \(X\subset v\mathbb CG\), excluding rank one by the [group-ring lift of a tensor leg](Yin_C_A0166_v2.md#shared-endpoints-and-lifting-a-leg-into-the-group-ring).
Interchanging the labels also rules out \(\dim(J+Jt)<4\).
This proves the simultaneous direct sums.

## The rational transfer matrix

Choose a basis row \(x\) of \(E\) and a basis row \(y\) of \(J\).
In the basis \((x,xs)\) of \(X\), write
\[
             y=x C(s),\qquad yt=x D(s).
\]
Here \(C,D\) have degree at most one in the indicated scalar variable and the coefficient columns of \([C,D]\) give the stated constant change of basis.
The inclusion \(\mathbb C(Z)\to\mathcal U(\langle s\rangle)\) at \(Z=s\) is faithful since \(s\) has infinite order.

If \(\det C(Z)\) vanishes identically, every matrix in the linear span of its two coefficient matrices has rank at most one.
Such a nonzero pencil has a common image line or a common kernel line.
Indeed two rank-one matrices with independent image and independent row directions have a sum of rank two.
The common kernel alternative would give a nonzero constant column killed by both coefficient matrices, contradicting independence of the stacked coefficient columns of \(C\).
In the common image alternative there is a nonzero constant \(c\) such that \(J\subset(xc)\operatorname{span}(1,s)\).
Then \(X=J+Jt\subset(xc)\mathbb CG\), again impossible by the group-ring lift.
If \(\det D(Z)=0\) the identical argument applied to \(Jt\) gives \(X=Jt+J\subset(xc)\mathbb CG\), this time using \(t^{-1}\).
Thus \(C,D\) are both invertible over the cyclic fraction field.
Substitution gives the claimed left kernel row \(y\).

If \(M(Z)c=d f(Z)\) for nonzero constant columns \(c,d\), then \(f\ne0\) and \(w=yc,\ v=yd\) obey \(wt=v f(s)\).
When \(c,d\) are dependent, the resulting scalar \(t-\lambda f(s)\), for some \(\lambda\ne0\), annihilates \(w\) on the right.
Write \(f=N/D_0\) with nonzero scalar polynomials.
Multiplying that scalar on the left by \(D_0(s)\) gives the nonzero group-ring element \(D_0(s)t-\lambda N(s)\), by the same disjoint coset supports.
Both it and \(D_0(s)\) are affiliated units, a contradiction.
For independent \(c,d\), the space \(X\) is spanned by \(v,w,vt,wt\).
Since \(w=v f(s)t^{-1}\), all four belong to \((vD_0(s)^{-1})\mathbb CG\), as witnessed by the coefficients \(D_0(s),N(s)t^{-1},D_0(s)t,N(s)\), respectively.
The same lift now gives the contradiction even when the common left factor is unbounded.

## Several equal eigenmodule dimensions

The left kernel of the two-by-two matrix \(tI_2-M(s)\) has trace dimension \(h\), using the unnormalized coordinate trace.
In a finite tracial algebra this equals its right kernel dimension.
Right multiplication as a matrix by \(t^{-1}I_2\) converts it to \(I_2-M(s)t^{-1}\) with the same left kernel.
Under the character twists on \(K\), \(M(s)\) stays fixed while \(t\) is multiplied by all powers of the character value on \(t\).
These twists extend to affiliated matrices by spectral calculus and preserve the normalized group trace.
Subgroup inclusion preserves matrix ranks by the coset embedding, so the same \(h\) can be computed in \(\mathcal U(K)\).
Thus the left eigenmodules of \(M(s)t^{-1}\) at each of the distinct character phases have dimension \(h\).
Any finite selection of them forms a direct sum by interpolation in the right-acting operator, hence their dimensions sum to at most two.
This proves \(h\le2/n\), and yields \(h=0\) in the infinite case.

Writing \(P\) for the left kernel projection over \(G\), one has \(y=yP\).
Any vector of \(X\) is \(y d_0+yt d_1=y(d_0+M(s)d_1)\) for constant columns \(d_0,d_1\).
Its regular rank is at most \(\operatorname{rk}_G y\le\operatorname{rk}_G P=h\).
Left kernel dimension zero would force the nonzero row \(y\) to vanish.
The first tensor factor of a rank-one boundary belongs to the first endpoint span, and the adjoint of its second factor belongs to the right-translated second endpoint span.
Hence a bound below \(1/2\) on either tight side excludes a boundary with both factors of rank \(1/2\).
The prescribed-list construction uses such factors for a half-rank Schur scalar and bounds the ordinary witness ranks by the label multiplicities.
