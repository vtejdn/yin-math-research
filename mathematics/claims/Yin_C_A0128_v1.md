---
author: Yin
---

# Algebraic rank strata and positive kernel gaps at fixed group support

## Statement

Let \(N\) be a finite von Neumann algebra with faithful normal tracial state and use the unnormalized matrix extension of the trace.
Let \(T(z)\) be a rectangular matrix polynomial in \(s\) **commuting complex parameters** with bounded matrix coefficients over \(N\).
For every real \(r\) the set
\[
                 \{z\in\mathbb C^s:\operatorname{rk}_N T(z)\le r\}
\]
is Zariski closed over \(\mathbb C\).
The same holds relative to a complex affine algebraic variety.
On an irreducible variety \(V\) the maximal rank is attained outside a countable union of proper closed subvarieties.
For the full parameter space there is also a degree bound for one nonzero polynomial vanishing on a sublevel strictly below an observed rank, given below.

Fix a discrete group \(G\), a group-ring matrix \(A=\left(\begin{smallmatrix}a&b_0\\c&d\end{smallmatrix}\right)\) with \(a\) an affiliated unit, its Schur complement \(S=d-ca^{-1}b_0\), and its kernel projection \(P\) of trace \(1/2\).
Fix a finite support set \(F\subset G\), put \(h(z)=\sum_{g\in F}z_g g\), and let
\[
  d_F(z)=\dim_G\{\xi\in P\ell^2(G):(1-P)h(z)\xi=0\}.
\]
For \(\eta>0\) each \(X_\eta=\{d_F\ge\eta\}\) is a complex algebraic cone.
The minimum of \(d_F\) is attained.
If every \(h\) supported in \(F\) has positive defect, that minimum is strictly positive.

Allowing some zero defects, the stronger assertion that all **strictly positive** \(d_F(z)\) have a common positive lower bound is equivalent to constructibility of \(\{d_F>0\}\).
In this case the positive-defect locus is closed.
A sufficient condition is a uniform degree bound on equations cutting out all the sets \(X_{1/n}\) for this same \(F\).
The defect is also the true nullity of the [fixed-size group-ring matrix](Yin_C_A0125_v2.md#group-ring-witnesses-and-the-exact-projection) \(K_{h(z)}^*K_{h(z)}\).
These assertions require no balance of the center-valued trace.

## Interpolation on the coordinate ring

The [one-parameter finite-evaluation proof](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) compares the dimension of a polynomial input space with ranks at its evaluation points.
For a general irreducible complex affine variety \(V\subset\mathbb C^s\), let \(E_n\) be the restrictions to \(V\) of scalar polynomials of total degree at most \(n\), and write \(H_n=\dim_{\mathbb C} E_n\).
If the total degree of \(T\) is at most \(l\), multiplication by \(T\) raises this filtration by at most \(l\).
For fixed \(l\) one has \(H_{n+l}/H_n\to1\).
Indeed \(H_n\) is the Hilbert function of degree \(n\) of the projective closure, using homogenization with the affine-chart variable.
Its eventual Hilbert polynomial has positive leading coefficient, including the constant case for a point.

Suppose \(Y\) is Zariski dense in \(V\) and \(\operatorname{rk}_N T(y)\le r\) throughout \(Y\).
Choose \(H_{n+l}\) points from \(Y\) whose evaluations on \(E_{n+l}\) give an injective scalar linear map.
This is possible because the evaluation functionals from \(Y\) span the whole dual of \(E_{n+l}\).
In any scalar basis of \(E_{n+l}\), the resulting square evaluation matrix is invertible.
It therefore also detects polynomial vectors with Hilbert-space coefficients.

If some point of \(V\) has rank greater than \(r\), choose such a point \(z_0\) in the smooth locus.
This choice uses lower semicontinuity of image rank for norm convergence and Euclidean density of the smooth locus in a complex reduced irreducible variety.
For the semicontinuity, truncate the initial space at a positive singular-value threshold, on which every sufficiently small norm perturbation is bounded below, and let the threshold tend to zero.
Let \(L\) be the initial projection space of \(T(z_0)\) in the appropriate finite sum of \(L^2(N)\).
It has dimension \(\operatorname{rk}_N T(z_0)\) and \(T(z_0)\) is injective on \(L\).

Multiplication by \(T(z)\) on \(L\)-valued sections from \(E_n\otimes_{\mathbb C}L\) is injective as a map of polynomial sections on \(V\).
To see this, expand a nonzero section in local holomorphic coordinates around \(z_0\).
A suitable continuous complex linear functional on the finite span of its coefficient vectors yields a nonzero scalar section, which has a nonzero Taylor coefficient because a nonzero regular function on \(V\) cannot vanish on a smooth neighborhood.
Every Taylor coefficient lies in \(L\).
In the lowest nonzero homogeneous term, the coefficient of any selected nonzero monomial is sent to its image under \(T(z_0)\), since terms of positive order from \(T\) contribute nothing at this degree.
The resulting polynomial vector is therefore nonzero.
This also covers a zero-dimensional \(V\), with the constant coefficient as the only term.

After evaluation at the selected points the product is still injective and lands in the direct sum of their closed image spaces.
This is a bounded right \(N\)-linear map on \(H_n\) copies of \(L\).
Taking finite Hilbert-module dimensions gives
\[
 H_n\,\operatorname{rk}_N T(z_0)
       \ \le\ \sum_{i=1}^{H_{n+l}}\operatorname{rk}_N T(y_i)
       \ \le\ H_{n+l}r.
\]
Letting \(n\) tend to infinity contradicts the choice of \(z_0\).
Thus any rank bound on a Zariski-dense subset holds on the entire irreducible variety.

Apply this assertion to each irreducible component of the Zariski closure of the claimed sublevel.
The sublevel is dense in each component after removing the other components, so it contains each whole component.
This proves closedness.
For \(R=\sup_{z\in V}\operatorname{rk}_N T(z)\), the countably many sublevels at \(R-1/n\) are proper.
On a smooth coordinate ball the proper algebraic subsets are closed and nowhere dense, so Baire's theorem ensures their union cannot cover \(V\).
The complementary points have rank \(R\), which proves attainment.

If \(V=\mathbb C^s\) and \(T(z_0)\) has rank \(R_0>r\), take \(n\) such that
\[
   R_0\binom{n+s}{s}>r\binom{n+l+s}{s}.
\]
If the sublevel were a uniqueness set for degree at most \(n+l\), the same evaluation inequality would fail at these finite dimensions.
Hence a nonzero polynomial of degree at most \(n+l\) vanishes on the whole sublevel.
This bound provides one containing hypersurface, with no uniform bound claimed as \(r\uparrow R_0\).

## Exact and positive defects on a fixed support

Apply the polynomial statement to \(T(z)=(1-P)h(z)P\), since \(d_F(z)=1/2-\operatorname{rk}_G T(z)\).
Alternatively \(K_{h(z)}\) has polynomial dependence on \(z\) and rank \(3-d_F(z)\), by elimination of two copies of \(a\).
Its adjoint contains conjugated parameters, but its positive Gram matrix has the same kernel.
The homogeneity of the compressed map gives the cone property, and attainment of the maximal rank gives the attained minimum defect.

Write \(C_n=X_{1/n}\) for \(n\ge1\), allowing \(C_n\) to be empty.
The sets increase and \(\{d_F>0\}=\bigcup_n C_n\).
A positive lower bound on all positive defects is equivalent to stabilization of this chain, which makes its union closed and hence constructible.
Conversely, if the union is constructible, it contains a nonempty relatively open subset of each irreducible component of its closure, after exclusion of the other components.
Such an open subset cannot be covered by countably many proper closed subsets of that component, by the same coordinate-ball Baire argument.
Thus each component lies entirely inside some \(C_n\).
There are only finitely many components, so a single \(C_n\) contains the closure and the chain stabilizes.
The empty union satisfies the same assertion.
If each \(C_n\) is cut out set-theoretically by equations of degrees at most a fixed \(D\), the spaces of degree-at-most-\(D\) polynomials vanishing on \(C_n\) form a decreasing chain in a fixed finite-dimensional vector space.
They stabilize and determine the corresponding zero sets, proving the stated sufficient condition.

## A two-direction spectral test

Suppose the compressed coefficient space has dimension two and contains \(T_0=(1-P)h_0P\) of rank \(1/2\).
It has full initial support \(P\) and full final support \(1-P\), so polar decomposition gives an affiliated inverse between those corners.
Select an independent compression \(T_1=(1-P)h_1P\) and put \(D=T_0^{-1}T_1\in P\mathcal U(G)P\).
Up to nonzero scaling, every nonzero compression is \(T_0\) or \(T_1-zT_0\).
In the latter case its defect is the trace of the eigenmodule \(\ker(D-zP)\) inside \(P\).
The zero compression has defect \(1/2\).
Eigenmodules at finitely many distinct points are in algebraic direct sum in \(P\mathcal U(G)\), by the scalar interpolation polynomials in \(D\).
Their dimensions therefore sum to at most \(1/2\).
Hence the positive-defect gap holds exactly when \(D\) has only finitely many eigenvalues of positive kernel trace.
If no exact direction exists, the previously proved minimum is already positive.

For a comparison, take the finite algebra \(M_2(\ell^\infty(\mathbb N))\) with the average matrix trace and atom weights \(2^{-n}\) for \(n\ge1\).
Set \(P=e_{11}\) and take \(D_0(n)=1/n\) as a bounded diagonal scalar function.
The two directions \(e_{21}\) and \(e_{21}D_0\) have compressions from \(P\) into \(1-P\).
The first is exact, while the pencil \(e_{21}(D_0-z)\) has defect \(2^{-n-1}\) at \(z=1/n\) and zero at all other \(z\).
Each positive-threshold set in this affine line is finite, but their increasing union is infinite and proper.
Here \(P\) can be realized as the kernel of the Schur scalar \(1-P\) with top-left pivot \(1\) and zero off-diagonal entries.
This model uses the displayed tracial coefficient algebra, not a canonical torsion-free regular group ring.
It tests the failure of a uniform positive gap to follow simply from closedness of all threshold strata.

For [A0001](../tasks/Yin_T_A0001_v1.md#contract), the minimum and constructibility test in this result are taken separately for each fixed \(F\).
Allowing supports to escape every fixed finite set requires further control even if every individual support has a positive lower bound.

## Assessment history

### Decision rank-strata-at-fixed-support

| Field | Value |
| --- | --- |
| date | 2026-11-23T07:16 |
| status | proved |
| reason | Independent inspection verified the complete statement, its arguments and the stated limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rank sublevels, fixed supports and the positive-gap criterion. |
| argument | [Interpolation](#interpolation-on-the-coordinate-ring) | Hilbert growth, optimal interpolation and injective multiplication of sections. |
| argument | [Positive defects](#exact-and-positive-defects-on-a-fixed-support) | Constructibility equivalence and degree condition for one support. |
| argument | [Spectral test](#a-two-direction-spectral-test) | Corner eigenmodules and infinitely many positive weights in the comparison. |
| review | [Independent finding](../audits/reviews/Yin_R_A0164_v1.md#rank-strata-at-fixed-support) | Whole argument at the stated scope. |

## Current assessment

[Selected decision](#decision-rank-strata-at-fixed-support)
