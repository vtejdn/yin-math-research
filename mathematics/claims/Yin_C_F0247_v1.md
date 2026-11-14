---
author: Yin
---

# Column bounds for Lipschitz graphs with slope of bounded variation on each dyadic shell

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let a finite tuple \(X\) of bounded normal generators of a finite von Neumann algebra with faithful normal probability trace satisfy the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix a selfadjoint coordinate \(S=X_i\) with actual vacuum \(\xi\), a point \(a\in\mathbb R\), and \(R>0\) such that \(\sigma(S)\subseteq[a-R,a+R]\).
Let \(g\) be real and \(L\)-Lipschitz on this interval.
Write \(r_j=2^{-j}R\) and let \(\mathcal I_j^\pm\) be the two open intervals \(r_{j+1}<\pm(s-a)<r_j\), for \(j\ge0\).
Suppose the distributional derivative of \(g'\) on each such interval is a finite measure and
\[
                 V=\sup_{j,\pm}|Dg'|(\mathcal I_j^\pm)<\infty .
\]
The jumps at the shell boundaries may have arbitrary size consistent with \(L\).
The total variation of the slope on the whole parameter interval may be infinite.

Replace \(S\) by \(Y_i=h(S)\), \(h(s)=s+i g(s)\), and allow bounded Borel relabellings of the other coordinates that are injective with Borel inverse on conull Borel sets.
The distinguished coordinate has an actual vacuum on the represented starred polynomial core \(P_Y\), and its original right slice \(E_{Y,i}=(\mathrm{id}\otimes\tau)\delta_{Y,i}\) satisfies
\[
 \left(\sum_m\|E_{Y,i}p_m\|_2^2\right)^{1/2}
 \le C(L)(1+V)\|\xi\|_2\left\|\sum_m p_m^*p_m\right\|^{1/2}
 \qquad (p_m\in P_Y,\ \text{finite columns}).
 \tag{1}
\]
The same bound holds in the adjoint orientation.
The closure of \(E_{Y,i}\) and its Hilbert adjoint both have domains containing \(M\Omega\), and the negative closure satisfies the generator-first commutator at \(i\).
The estimate holds at every choice of \(a\) satisfying the geometric hypothesis, including points in the spectrum.
Applying it at every coordinate of a correlated selfadjoint tuple with conjugate variables gives both actual ACSY and the strong domain condition for the resulting tuple.
An explicit polygon below has infinitely many slope jumps, infinite total variation of the slope, and an inverse secant that fails the measurable Schur test for every marginal whose support contains \((a,a+\varepsilon)\) for some \(\varepsilon>0\).

## Argument

### The old core and localized energy

Write \(x=s-a,\ y=t-a,\ N=W^*(S)\), let \(\mu\) be the law of \(S\), and set \(C=\mathrm{id}\otimes\tau\).
Use the old real-coordinate derivation \(\delta\), the partial liberation \(\gamma=I_{s-t}\delta\), its vacuum \(\eta\), and the joint left-right spectral measure \(\nu\) of \(\eta\).
The symbol \(I\) acts on the inner tensor legs, so \(I_{v\otimes w}(b\otimes d)=bv\otimes wd\).
For a sliced map \(F\) on the old starred core, write \(c(F)\) for its optimal finite-column bound.
The [real-coordinate estimate and scalar packing](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) give
\[
 c(C\delta)\le4\|\xi\|_2,\qquad
 \mu=\rho\,ds,\qquad \int\rho^3\,ds\le C_0\|\mathbb E_N\xi\|_2^2.
\]
The [inverse-gap identity](Yin_C_F0238_v1.md#statement) gives \(\nu\{s=t\}=0\) and \(\int |s-t|^{-2}\,d\nu=\|\xi-\mathbb E_N\xi\|_2^2\), integrating off the diagonal.
For an interval \(J\) put
\[
 U(J)^2=\int_{J^2,\ s\ne t}\frac{d\nu(s,t)}{|s-t|^2}
                    +\int_J\rho^3\,ds.
\]
For \(b\in J\), any \(D\ge\sup_{s\in J}|s-b|>0\), \(d_n=2^{-n}D\), and \(Q_n=1_{J\cap\{|s-b|\le d_n\}}(S)\), one has
\[
 \sum_{n\ge0}\frac{(\|Q_n\eta Q_n\|_2+\tau(Q_n)^{3/2})^2}{d_n^2}
 \le C_1 U(J)^2 .                                                     \tag{2}
\]
Indeed the compression term follows by summing \(d_n^{-2}\) where \(0<|s-t|\le2d_n\) inside \(J^2\).
For the mass term put \(w_k=\mu(J\cap\{d_{k+1}<|s-b|\le d_k\})\).
The shells have length at most \(2d_k\), so Hölder gives \(\sum_k w_k^3/d_k^2\le4\int_J\rho^3\).
Now \(\tau(Q_n)/d_n^{2/3}=\sum_{k\ge n}2^{-2(k-n)/3}w_k/d_k^{2/3}\), and the triangle inequality for translates in \(\ell^3\) proves (2).
In particular \(U([a-R,a+R])\le C_2\|\xi\|_2\).

We will use the [liberation block estimate](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) for two orthogonal marginal projections \(e,f\).
Writing \(G=C I_{e\otimes f}\gamma\) and \(q=e+f\), it gives \(c(G)\le C_3(\|q\eta q\|_2+\tau(q)^{3/2})\).
An additional symbol represented on the rectangle as a sum or integral of separated measurable factors \(v(s)w(t)\), with integral or sum of supremum-norm products at most \(B\), costs at most \(2Bc(G)\).
This follows from \((G(pw)-pG(w))v\), with bounded marginal polynomial approximants to \(w\) in the liberation graph as in the [vertex estimate](Yin_C_F0246_v1.md#a-uniform-estimate-at-one-vertex).
These outputs have right support in \(e\).
For an additional Schur symbol acting on \(\delta\) itself we use the [old-core bound](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) \(c(CI_K\delta)\le2\|K\|_{\rm Schur}c(C\delta)\).

### A localized estimate for a rectangle on one side of the vertex

Let \(E,F\subset J\) be Borel subsets of one interval \(J\) on which the slope has bounded variation \(v_J=|Dg'|(\operatorname{int}J)\).
Write
\[
 K(s,t)=\frac{s-t}{h(s)-h(t)},\qquad u_0(t)=(1+i g'(t))^{-1}.
\]
Use a Borel slope representative with \(|g'|\le L\), chosen right-continuously on open intervals of bounded variation.
The diffuse marginals allow arbitrary values at individual endpoints.
We claim that
\[
 c\big(C I_{1_E(s)1_F(t)(K(s,t)-u_0(t))}\delta\big)
       \le C_4 v_J U(J).                                                \tag{3}
\]
Use the [slope-variation identity](Yin_C_F0246_v1.md#decomposition-by-the-variation-of-the-slope) on \(J\).
It writes \(K-u_0(t)=\int J_b(s,t)\,d(Dg')(b)\), with \(|J_b|\le1\), supported on pairs across \(b\).
For such pairs put \(z=|s-b|\), \(w=|t-b|\), \(\sigma=\operatorname{sign}(s-t)\).
The kernel acting on \(\gamma\) for this integrand is
\[
 \frac{J_b(s,t)}{s-t}=
 \frac{-i z}{(1+i g'(t))\,\sigma(h(s)-h(t))(z+w)} .
\]
In either orientation restrict the first variable to \(E\) and \(d_{n+1}<z\le d_n\).
First take all second variables in \(F\) on the opposite side with \(w\le d_n\), then each shell \(d_{k+1}<w\le d_k,\ k<n\) in \(F\).
The selected projections are orthogonal and their union lies in the \(Q_n\) or \(Q_k\) of (2).
The two Laplace integrals for \((\sigma(h(s)-h(t)))^{-1}\) and \((z+w)^{-1}\) give separated norm-product bounds \(4/d_n\) and \(4d_n/d_k^2\) on the respective rectangles.
Indeed the product of the two factor norms at parameters \(\lambda,\alpha\ge0\) is at most \(d_n e^{-(\lambda+\alpha)(z_{\min}+w_{\min})}\), with \(z_{\min}=d_n/2\) and \(w_{\min}=0\) or \(d_k/2\).
Set \(A_n=(\|Q_n\eta Q_n\|_2+\tau(Q_n)^{3/2})/d_n\).
The block bound and the right-support orthogonality across first shells bound the whole column by the \(\ell^2\) norm of \(C(A_n+\sum_{k<n}2^{k-n}A_k)\).
Equation (2) bounds this by \(C U(J)\) uniformly in \(b\).
Shell truncations of the bounded \(J_b\) converge strongly on every coarse input by domination of its inner spectral measure by \(\mu^2\).
The bounded jointly measurable symbols may be integrated against the finite slope variation on \(J\), by scalar Fubini on the separable cyclic spectral spaces of the column inputs.
The column triangle inequality gives (3).

### Summation over the shells at the accumulation point

Put \(Q(x)=(h(a+x)-h(a))/x\) for \(x\ne0\) and \(u(t)=1/Q(y)\).
We have \(1\le |Q|\le B=\sqrt{1+L^2}\).
Use \(u(t)\) on the whole square as one separated symbol acting on \(\delta\).
The remaining symbol \(K-u(t)\), when acting on \(\delta\) off the diagonal, is equivalent to the following symbol acting on \(\gamma\):
\[
 H(x,y)=\frac{x(Q(y)-Q(x))}{Q(y)(x-y)(xQ(x)-yQ(y))}.                 \tag{4}
\]
Choose an integer \(N\ge2\) so large that \(2^{1-N}B\le1/2\), and denote the projection of \(\{r_{j+1}<|x|\le r_j\}\) by \(e_j\).
Discarding its endpoints and the apex affects neither marginal nor coarse inputs.
Each shell has two one-sided pieces.
Write \(A_j\) for the quantity in (2) at \(b=a,\ D=R,\ J=[a-R,a+R]\) before its square and sum.

For first shell \(j\), collect **all** second shells \(k\ge j+N\) in one block.
Here the ratios \(|y/x|\) and \(|yQ(y)/(xQ(x))|\) are at most \(1/2\).
Expand both reciprocal factors in (4) by geometric series about \(x\) and \(xQ(x)\).
The product of the separated supremum bounds for either ratio is at most \(1/2\) even though the variables range independently.
The remaining factors \(x/[x^2 Q(x)]\) and \((Q(y)-Q(x))/Q(y)\) have total separated cost at most \(C(B)/r_j\).
The union of the two projections lies in \(\{|s-a|\le r_j\}\), hence the cost of the entire block is at most \(C(B)A_j\).
For each larger second shell \(k\le j-N\), expand instead about \(y\) and \(yQ(y)\).
Both reversed ratios again have separated bounds at most \(1/2\), and the remaining factor \(x/y^2\) gives total cost at most \(C(B)r_j/r_k^2\).
The union of the projections lies in the larger ball of radius \(r_k\), yielding column cost \(C(B)2^{k-j}A_k\).
Outputs for different first shells are right-supported on the orthogonal \(e_j\).
Consequently (2) and geometric \(\ell^2\) convolution give a total far-block bound \(C(B)\|\xi\|_2\).
The geometric series are used on individual rectangles separated from the diagonal.
Truncating first shells and passing to the limit acts on \(\delta\) by bounded restrictions of \(K-u(t)\), which converge strongly by the coarse measure-class property.

For the remaining offsets \(|j-k|<N\), first restrict to opposite signs of \(x,y\).
Here \(|x-y|=|x|+|y|\), and \(\sigma=\operatorname{sign}(x-y)\) has fixed sign.
Laplace representations for \(1/(\sigma(x-y))\) and \(1/(\sigma(xQ(x)-yQ(y)))\) separate the variables.
The real parts of their exponents give decay \(e^{-(\lambda+\alpha)(|x|+|y|)}\).
Together with \(x(Q(y)-Q(x))/Q(y)\) in (4) this bounds the separated cost by \(C(B)r_j/(r_j+r_k)^2\).
Writing \(m=\min(j,k)\), the block and support estimates give column cost \(C(B)A_m\).
For each fixed offset and orientation the first supports are disjoint, so (2) bounds their sum in the column norm by \(C(B)\|\xi\|_2\).
There are finitely many such offsets and orientations depending only on \(L\).

For a fixed remaining offset and one fixed common sign let \(E,F\) be the two one-sided shell pieces, and let \(J\) be their closed interval hull.
This interval spans at most \(N\) adjacent one-sided shells, so \(v_J\le N V+2NL\), including jumps at intervening boundaries.
For this family the \(J\)'s have overlap at most \(N+1\) almost everywhere, both for Lebesgue measure and in the first variable of \(\nu\), whose marginals are absolutely continuous with respect to \(\mu\).
Thus \(\sum_J U(J)^2\le (N+1) U([a-R,a+R])^2\).
On each rectangle use \(K-u_0(t)\) first.
The first supports are disjoint, and (3) gives for their sum the bound \(C(L)(1+V)\|\xi\|_2\).
The remaining symbol \(1_E(s)1_F(t)(u_0(t)-u(t))\) sums over these pairs to a Schur multiplier of norm at most two.
Indeed the matrix mask with rectangles \(E\times F\) is contractive on operator kernels because both lists of projections are disjoint: the sum maps each orthogonal input block \(L^2(F)\) into the corresponding orthogonal output block \(L^2(E)\).
Multiplying on the second variable costs \(\|u_0-u\|_\infty\le2\).
The old-core Schur estimate finishes these offsets.
Once more the sums of the restricted \(K-u_0\) and the masks converge on each coarse input by bounded pointwise convergence on the disjoint rectangles.
Adding the initial \(u(t)\) and the finitely many estimates gives (1) for \(C I_K\delta\) on the old core.

### Target core, adjoint orientation and an infinite polygon

The graph has a scalar vacuum because \(\rho\in L^3\), and its inverse-gap energy for \(\eta\) is bounded by the original one because \(|h(s)-h(t)|\ge |s-t|\).
The [liberation and scalar graph criteria](Yin_C_F0244_v1.md#argument) therefore give the distinguished target vacuum, also with the stated omitted Borel changes.
The [graph approximation of target columns](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) identifies \(\delta_{Y,i}=I_K\bar\delta\) on \(P_Y\) and supplies convergent old-core graph approximants with limit superior of input column norm at most \(1+\varepsilon\) for a target column of norm at most one.
Only boundedness of \(K\), which here has norm at most one in \(L^\infty\), is required to pass the already proved old-core estimate to this limit.
Letting \(\varepsilon\) decrease to zero proves (1).
On the adjoint tuple the starting distinguished derivation is the same real derivation, since all omitted starred letters are killed.
Changing \(g\) to \(-g\) preserves \(L,V\).
The tracial flip-adjoint converts the resulting right one-input estimate into a left one-input estimate for the original derivation.
The [two-slice theorem](Yin_C_F0072_v1.md#statement), part B, gives the asserted bounded-vector domains.
The generator commutator on the core extends by graph approximation since both left multiplication and the vacuum projection are bounded, giving the stated sign for the negative closure.

For an example take \(a=0,\ R=1\).
Let \(f\) be the tent on \([1/2,1]\), piecewise linear through \((1/2,0),(3/4,1/8),(1,0)\).
For \(2^{-j-1}\le x\le 2^{-j}\), set \(g(x)=2^{-j}f(2^j x)\), put \(g(0)=0\), and extend oddly to negative \(x\).
Each shell has slopes \(1/2,-1/2\) in its interior and has slope variation one, while infinitely many shells give infinite total variation.
For \(s_j=2^{-j}\) and \(t_k=(3/4)2^{-k}\), one has \(Q(s_j)=1\) and \(Q(t_k)=1+i/6\).
The matrix \(K(s_j,t_k)\) differs from the two-constant triangular matrix with value \(1\) for \(j<k\) and \((1+i/6)^{-1}\) for \(j>k\) by a uniformly Schur-bounded error (assign any fixed bounded value on the diagonal).
Indeed when \(|j-k|\ge3\), division by the dominant coordinate in the secant gives error at most \(C2^{-|j-k|}\).
A matrix supported on one diagonal has Schur norm at most its entry supremum, by the orthogonal input and output blocks, so summing over diagonals proves the assertion.
Triangular truncation on \(n\times n\) matrices has unbounded operator Schur norms as \(n\) grows. [Discrete Hilbert-transform test](Yin_C_F0241_v1.md#a-logarithmic-lower-bound-for-the-inverse-divided-difference)
The unequal constants therefore force unbounded Schur norms for these sampled matrices.
If the support contains \((0,\varepsilon)\), begin at any sufficiently late scale; all the sample points are then support points.
For each finite test, compress an integral operator between normalized indicators of small positive-measure neighborhoods of the \(t_k\) and \(s_j\).
The compressed multiplied entries are the test entries times the averages of \(K\) over the rectangles.
Continuity off the diagonal gives the sampled values in the shrinking-neighborhood limit, so the integral-kernel norm bound would imply the excluded uniform matrix bound.
Translation and simultaneous dilation give the same example at any chosen vertex and scale.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:05 |
| status | open |
| reason | The every-vertex mixed-core estimate for uniformly bounded shellwise slope variation and its non-Schur polygon are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every vertex, shellwise variation, both original domains, and the infinite polygon. |
| argument | [Argument](#argument) | Localization of the variation estimate, asymmetric far shells, opposite signs, and the triangular obstruction. |
| dependency | [Real-coordinate estimates](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Original column and \(L^3\) marginal packing. |
| dependency | [Inverse-gap identity](Yin_C_F0238_v1.md#statement) | Joint liberation energy and coarse product-measure domination. |
| dependency | [Liberation blocks](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Orthogonal-projection column estimate and first-leg right support. |
| dependency | [One-vertex estimate](Yin_C_F0246_v1.md#a-uniform-estimate-at-one-vertex) | Separated measurable multipliers for a liberation block. |
| dependency | [Variation kernel identity](Yin_C_F0246_v1.md#decomposition-by-the-variation-of-the-slope) | Stieltjes decomposition on each interval with bounded slope variation. |
| dependency | [Schur slicing](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Old-core finite-column estimate for measurable Schur symbols. |
| dependency | [Graph vacuum](Yin_C_F0244_v1.md#argument) | Scalar Lipschitz graph vacuum and invariance of liberation under Borel changes. |
| dependency | [Graph-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Strong graph transfer with controlled input column norm. |
| dependency | [Two-slice domains](Yin_C_F0072_v1.md#statement) | Original closure and Hilbert adjoint on bounded vectors. |
| dependency | [Triangular matrix test](Yin_C_F0241_v1.md#a-logarithmic-lower-bound-for-the-inverse-divided-difference) | Unbounded triangular Schur norms and compression to sampled rectangles. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:10 |
| status | proved |
| reason | Adopt the localized shellwise slope-variation theorem and the infinite polygon with an unbounded inverse-secant Schur multiplier after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every vertex, shellwise variation, both original domains, and the infinite polygon. |
| argument | [Argument](#argument) | Localization of the variation estimate, asymmetric far shells, opposite signs, and the triangular obstruction. |
| dependency | [Real-coordinate estimates](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Original column and \(L^3\) marginal packing. |
| dependency | [Inverse-gap identity](Yin_C_F0238_v1.md#statement) | Joint liberation energy and coarse product-measure domination. |
| dependency | [Liberation blocks](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Orthogonal-projection column estimate and first-leg right support. |
| dependency | [One-vertex estimate](Yin_C_F0246_v1.md#a-uniform-estimate-at-one-vertex) | Separated measurable multipliers for a liberation block. |
| dependency | [Variation kernel identity](Yin_C_F0246_v1.md#decomposition-by-the-variation-of-the-slope) | Stieltjes decomposition on each interval with bounded slope variation. |
| dependency | [Schur slicing](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Old-core finite-column estimate for measurable Schur symbols. |
| dependency | [Graph vacuum](Yin_C_F0244_v1.md#argument) | Scalar Lipschitz graph vacuum and invariance of liberation under Borel changes. |
| dependency | [Graph-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Strong graph transfer with controlled input column norm. |
| dependency | [Two-slice domains](Yin_C_F0072_v1.md#statement) | Original closure and Hilbert adjoint on bounded vectors. |
| dependency | [Triangular matrix test](Yin_C_F0241_v1.md#a-logarithmic-lower-bound-for-the-inverse-divided-difference) | Unbounded triangular Schur norms and compression to sampled rectangles. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0256_v1.md#finding) | Every permitted apex, both domains and the strong commutator, variation at each scale, the uniform original mixed-core column cost and the explicit sampled operator-norm obstruction. |
