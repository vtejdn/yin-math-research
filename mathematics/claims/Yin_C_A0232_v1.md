---
author: Yin
---

# Positive two-by-two Gram compressions of the order-25 remainder

## Statement

Let \(R\in M_{14}(\mathbb CN)\) be the rank-\(3/2\) companion remainder over the original commutator subgroup \(N\) in the [order-25 reduction](Yin_C_A0222_v1.md#the-companion-over-the-actual-commutator-subgroup).
Write \(\mathcal M=\mathcal N(N)\), \(Z\) for its normalized center-valued trace, \(\tau\) for the group trace, and \(\operatorname{Tr}_m\) for the unnormalized matrix extension of \(\tau\).
Choose any column \(c\) of \(R\) and put the \(m=13\) other columns into \(F\).
Define
\[
 a=c^*c,\quad P=ca^{-1}c^*,\quad B=(I-P)F,\quad
 e=p_{(\ker B)^\perp},\quad d=\sum_{i=1}^m Z(e_{ii}),\quad
 \eta=\tau(\min(d,1)).
\]
For \(v\in(\mathbb CN)^m\) form the positive two-by-two polynomial Gram matrix \(J(v)\) of \(c,Fv\).
Its Schur complement \(\sigma(v)\) about \(a\) is bounded and positive and satisfies
\[
       \sup_{v\in(\mathbb CN)^m}\operatorname{rk}\sigma(v)=\eta,\qquad
                          1/26\le\eta\le1/2.
\]
The supremum equals \(1/2\) precisely when \(d\le1\).
If \(N\) has infinite conjugacy classes outside the identity, the supremum over columns using at most \(k\) monomials in total is at least \(\tfrac12(1-(25/26)^k)\).
In that case an original positive two-by-two polynomial Gram matrix has rank \(3/2\), or infinitely many distinct ranks of such matrices approach \(3/2\) strictly from below.
In particular, containment of all original two-by-two ranks in \(q^{-1}\mathbb Z\) for one odd \(q\) excludes this companion under the conjugacy hypothesis.

For any center there is a positive two-by-two polynomial Gram matrix of rank exactly \(3/2\), with the same pivot \(a\), over \(N*\mathbb Z\).
If \(J_0\le N\) contains the group supports of \(R\) and freely generates a subgroup \(J_0*\langle w\rangle\) with some infinite-order \(w\in N\), the exact construction is available already in \(N\).
In these two cases the projections onto the image closure and kernel of \(R\) belong to the fourteen-by-fourteen matrices over the second scalar inverse layer of the respective group.
The proof also gives a sufficient inverse condition in \(N\) without a free direction.

## The bounded Schur complement

The column \(c\) has a nonzero group-ring coordinate and hence rank one by [two-sided nonvanishing and scalar injectivity](Yin_C_A0222_v1.md#polynomial-rows-and-columns-at-rank-below-two).
In the affiliated algebra \(a\) is a unit and polar decomposition identifies \(P\) as the orthogonal projection onto the closure of the image of \(c\).
Thus \(\operatorname{Tr}_m(e)=\operatorname{rk} B=3/2-1=1/2\).
Even for unbounded \(a^{-1}\), the matrix \(B=(I-P)F\) is bounded, and affiliated elimination gives
\[
 J(v)=\begin{pmatrix}a&c^*Fv\\v^*F^*c&v^*F^*Fv\end{pmatrix},\quad
 \sigma(v)=v^*B^*Bv,\quad
 \operatorname{rk}J(v)=1+\operatorname{rk}\sigma(v)
                       =1+\operatorname{rk}(ev).
\]
The last equality uses that \(B\) is injective on its initial support.

## Adding one monomial in the original group

For \(T=ev\), denote the center-valued dimension of its image by \(r\), its kernel projection in the scalar domain by \(p\), and \(e-p_{\operatorname{im}T}\) by \(f\), using image closures for projections.
Their center-valued dimensions are \(1-r,d-r\), respectively, and \(r\le\min(1,d)\).
Write \(I_j\) for the \(j\)-th coordinate inclusion.
The \(L^2\)-closed convex hull of the \(gpg^*\), \(g\in N\), contains \(Z(p)\): its unique minimum-norm point is fixed by every conjugation and pairing with central elements identifies it with \(Z(p)\). [Central averaging](Yin_C_A0125_v2.md#reduction-of-the-defect-with-one-more-group-element)
The contraction \(f I_j g p\) has squared \(L^2\) norm \(\tau(f_{jj}gpg^*)\), at most its image rank.
Averaging over coordinates and using the convex hull therefore gives
\[
 \sup_{j,g}\operatorname{rk}(fI_jgp)\ \ge\
 \frac1m\sum_j \tau(f_{jj}Z(p))
 =\frac1m\tau\big((d-r)(1-r)\big).
\]

For fixed \(j,g\) compare \(T+zeI_jg\) on the domain decomposition \(1-p,p\) and the target decomposition \(e-f,f\).
Scale the second target summand by \(1/z\) for \(z\ne0\).
At zero the resulting matrices converge in norm to a lower triangular matrix with diagonal blocks \(T|_{1-p}\) and \(fI_jgp\).
The first has an affiliated inverse between its support modules, so the limit rank is \(\operatorname{rk}T+\operatorname{rk}(fI_jgp)\).
Lower semicontinuity of rank for norm convergence, by spectral truncation away from zero, shows that the supremum after adding one monomial is at least this sum.

Let \(D_k\) be \(\eta\) minus the rank supremum for columns using at most \(k\) monomials.
For \(b=\min(d,1)-r\) one has \((d-r)(1-r)\ge b^2\) pointwise and \(\tau(b^2)\ge \tau(b)^2\).
Applying the preceding bound to columns approaching the \(k\)-monomial supremum gives
\[
        D_0=\eta,\qquad D_{k+1}\le D_k-D_k^2/m,\qquad
        D_k\le m/(k+m/\eta).
\]
The last step follows by reciprocation when the defects are positive, and a zero defect persists.
This proves the supremum formula.
Since \(0\le d\le m\) and \(\tau(d)=1/2\), one has \(1/(2m)\le\eta\le1/2\), with equality on the right exactly when \(d\le1\).
In a factor \(d=1/2\) and \((d-r)(1-r)\ge(1/2-r)/2\), giving \(D_{k+1}\le(1-1/(2m))D_k\).
If \(1/2\) is absent, a supremum of \(1/2\) requires a strictly increasing sequence of attained ranks approaching it.

## A finite column attaining the rank

Work in \(J_0*\langle w\rangle\) where \(J_0\) contains the group supports of \(R\).
Regular subgroup inclusion and spectral calculus put \(e\) over \(\mathcal N(J_0)\).
There is an infinite-order \(g\in J_0\), since the groups are torsion-free and a constant scalar matrix cannot have rank \(3/2\).
The \(u_i=w^i g w^{-i}\), \(1\le i\le m\), are free Haar group unitaries freely independent of \(\mathcal N(J_0)\), by free product normal form.
Choose a complex unitary \(V\) for which the diagonal entries of \(e'=V^*eV\) all have trace \(\alpha=\operatorname{Tr}_m(e)/m=1/(2m)\).
Indeed diagonalize the Hermitian matrix \((\tau(e_{ij}))\) and conjugate by a Fourier matrix to distribute the mean of its eigenvalues to every diagonal position.
Set \(v_0=(u_1,\ldots,u_m)^{\mathsf t}/\sqrt m\), \(p_0=v_0v_0^*\) and \(v=Vv_0\).

The projections \(e'\) and \(p_0\) are free for the normalized scalar matrix trace.
It suffices to check cyclic alternating products of \(e'-\alpha I\) and \(p_0-I/m\), since each projection generates a two-dimensional algebra and odd alternating words reduce by cycling the two end factors together and decomposing their product into scalar and centered parts.
The second centered projection has zero diagonal and off-diagonal entries \(u_i u_j^{-1}/m\) with \(i\ne j\).
In the expanded trace of an alternating product split each entry of \(e'-\alpha I\) into its scalar trace and its centered part.
A nonzero scalar part can only occur off the diagonal.
Consequently cancellation of successive inverse free letters is forbidden both within a projection entry and across any intervening nonzero scalar part.
If some centered entries from \(\mathcal N(J_0)\) occur, every intervening block of free letters is a nonempty reduced word, and freeness gives trace zero.
With no centered entries the resulting whole free word is nonempty and reduced, giving the same conclusion.

For free projections of normalized traces \(\alpha,\beta\) the normalized rank of their product is \(\min(\alpha,\beta)\), by the zero mass of the compressed product law. [Collins and Kemp, equation (1.6), p. 3](../literature/pdf/CK14--arxiv-v3.pdf#page=3) and [the retained free-projection formula](../audits/literature/CK14/Yin_U001.md#ck14-u001).
Since \(v_0\) is an isometry onto \(p_0\) and \(\operatorname{Tr}_m(p_0)/m=1/m\), the unnormalized rank of \(ev\) is \(m\min(1/(2m),1/m)=1/2\).
The column \(v\) uses only \(m\) distinct group elements and the Schur complement still uses the single inverse of \(a\).
Take \(J_0=N\) for the extension, or use the specified free cyclic direction inside \(N\).

## Recovering the original image and kernel projections

Suppose a polynomial \(v\) in the group under consideration already attains \(1/2\).
Then \(W=Bv\) has the same affiliated image as \(B\), by inclusion and equality of trace dimensions.
It follows that \(p_{\operatorname{im}R}=P+p_{\operatorname{im}W}\).
Both \(W=(I-ca^{-1}c^*)Fv\) and \(\sigma=W^*W\) have entries in the first [scalar inverse layer](Yin_C_A0124_v1.md#statement).

Suppose this layer contains another positive scalar \(b\) of rank \(1/2\) with \(\sigma+b\) an affiliated unit.
Write \(h=(\sigma+b)^{-1}\).
The affiliated images of \(\sigma\) and \(b\) sum to the full scalar module, since their sum contains the range of \(\sigma+b\).
Their dimensions add to one, so the images have zero intersection.
Splitting \(\sigma=(\sigma+b)h\sigma\) along this direct sum gives \(\sigma h\sigma=\sigma\).
The equality \(\ker W=\ker\sigma\) now gives \(Wh\sigma=W\).
Thus \(WhW^*\) is selfadjoint with image contained in \(\operatorname{im}W\) and acts as the identity there.
The projection \(P+WhW^*\) onto the original image is therefore in \(M_{14}(D_2)\).
Applying the criterion to \(R^*\) recovers \(p_{\ker R}=I-p_{\operatorname{im}R^*}\).

A single freely joined generator \(w\) suffices for both steps.
Put \(w_0=wgw^{-1}\) and \(w_1=w^2gw^{-2}\); then \(J_0,\langle w_0\rangle,\langle w_1\rangle\) generate their free product.
Use \(w_0\) in the column construction and set \(b=w_1\sigma w_1^{-1}\).
The two rank-half kernel projections are free and have zero intersection by the [free projection intersection formula](../audits/literature/CK14/Yin_U001.md#ck14-u001).
Positivity gives injectivity of \(\sigma+b\), hence its affiliated invertibility.
The same two freely joined generators work for \(R^*\), whose corresponding column pivots are injective by the polynomial row assertion for \(R\).
This proves the two second-layer claims.

## Assessment history

### Decision positive-gram-compressions-and-the-center

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:44 |
| status | proved |
| reason | Independent review verified the center-valued supremum, monomial increments, free projection computation and the inverse-layer bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The supremum, factor estimate, free extension and projection criteria. |
| argument | [The bounded Schur complement](#the-bounded-schur-complement) | The bounded realization of the positive single-inverse remainder. |
| argument | [Adding one monomial in the original group](#adding-one-monomial-in-the-original-group) | Lower triangular comparison, center-valued averaging and the rank estimates. |
| argument | [A finite column attaining the rank](#a-finite-column-attaining-the-rank) | Trace balancing and exact compression by a finite column in the free product. |
| argument | [Recovering the original image and kernel projections](#recovering-the-original-image-and-kernel-projections) | Second-layer formulas for the image and kernel in the indicated groups. |
| review | [Positive Gram compressions and the center](../audits/reviews/Yin_R_A0199_v1.md#positive-gram-compressions-and-the-center) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-positive-gram-compressions-and-the-center)
