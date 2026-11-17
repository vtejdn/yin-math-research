---
author: Yin
---

# Endpoint estimates for a nonclosed row with no gapped representative of its kernel

## Statement

Let \(H\) be any finitely generated group, possibly a fixed four-line group from [C51](Yin_C_A0051_v1.md#statement).
On the single group \(G=H\times\mathbb Z^d\), \(d=3,4\), use the generating sets of the two factors together.
There are rational group-ring matrices \(A,A_0\) of the same size \(N\)-by-\(dN\) and nonclosed range with exactly the same row Gram matrix.
All their unnormalized column-Gram trace moments, including all squared time increments of the heat polynomials, therefore agree.
Their nullities are both \((d-1)N\).
The kernel projection of \(A_0\) is constant.
The actual kernel projection \(p\) of \(A\) lies outside \(M_{dN}(C_r^*(G))\).
In particular no finite group-ring matrix, or even matrix over \(C_r^*(G)\), of closed range has this kernel.
The entries of \(A\) require the whole group as support, as do those of \(p\), also after independent group translations of all rows and columns.

Let \(B=A^*A/M\) with \(M>4d\), \(Q_k=(I-B)^k\), and use the endpoint sum of [C62](Yin_C_A0062_v1.md#statement),
\[
 D_k(R^{-1})=\sum_{g\in G}(1-e^{-|g|/R})^4\|\widehat Q_k(g)\|_{\rm HS}^2.
\]
For \(d=4\) the original powers satisfy, uniformly in \(k\ge1,\ R\ge2\),
\[
 D_k(R^{-1})\le C R^{-4}(1+\log R),\qquad
 \|Q_{2k}-Q_k\|_2^2\asymp k^{-2}.
\]
The projection satisfies, for every \(0\le\beta<4\),
\[
 \sum_{|g|>R}(1+|g|)^\beta\|\widehat p(g)\|_{\rm HS}^2
 \le C_\beta R^{\beta-4}.
\]
Its fourth weighted square moment diverges.
For \(3<\beta<4\) and \(k_j=\lceil2^{\kappa j}\rceil\), \(\kappa>0\), the C62 series converges exactly for \(\kappa>\beta/2\), omitting any initial repeated times.
At \(d=3\), the spatial moment of \(p\) is infinite for **every** \(\beta>3\), while the constant projection has zero exterior tail with identical scalar return and increment data.
All differential estimates below apply to the finite polynomials of the original input and their true endpoint coefficients.
For a four-line \(H\) this construction uses extra commuting directions in \(G\).
It gives a comparison for the individual-group question without asserting the existence of those directions in \(H\).

## Matrices with identical row products

Write \(z_j\) for the \(j\)-th standard generator of \(\mathbb Z^d\), \(a_j=1-z_j\), and \(\ell=\sum_{j=1}^d a_j^*a_j\).
Choose \(N\) a power of two divisible by \(2^d\) and large enough to list the identity and a finite generating set of \(H\) as \(h_1,\ldots,h_N\), using identity entries as padding.
Let \(S\) be the normalized real Walsh matrix of order \(N\) with a constant first column.
Its orthogonality follows from binary character orthogonality, and all its entries are \(\pm1/\sqrt N\).
Put \(U=S^*\operatorname{diag}(h_1,\ldots,h_N)S\), a group-ring unitary with rational coefficients and \(U_{11}=N^{-1}\sum_i h_i\).
Use the row of square blocks
\[
 A=(a_1 U,\ a_2 I,\ldots,a_d I).
\]
The centrality of the lattice coordinates gives \(AA^*=\ell I_N\).
For the comparison matrix take exterior multiplication \(e_j\) by the \(j\)-th basis vector on the exterior algebra of \(d\) coordinates, with its standard orthonormal basis.
This is the lattice exterior-difference construction of the Hodge–Dirac operator. [Miranda and Parra, arXiv v1, equation (20)](../literature/pdf/MP23--arxiv-v1.pdf#page=11)
The operators \(e_j,e_j^*\) satisfy \(e_i e_j+e_j e_i=0\) and \(e_i e_j^*+e_j^* e_i=\delta_{ij}I\) by insertion and removal of a basis element.
Consequently the selfadjoint matrix \(L=\sum_j(a_j e_j+a_j^*e_j^*)\) satisfies \(L^2=\ell I_{2^d}\).
The arXiv version of MP23 defines its scalar difference Laplacian by neighbors minus twice the central value in each direction on p. 11, while Lemma 3.1 on p. 12 identifies the square with that Laplacian and the proof uses the positive Dirichlet form.
The direct factorization here fixes the positive sign through \(\ell=\sum_j a_j^*a_j\). [MP23, Lemma 3.1 and equation (23)](../literature/pdf/MP23--arxiv-v1.pdf#page=12)
Take a direct sum \(L_N\) of \(N/2^d\) copies and set \(A_0=(L_N,0,\ldots,0)\) with \(d\) block columns.
This gives \(A_0A_0^*=AA^*\) in the group ring, hence equality in every row-product fiber at every power.
The positive column-Gram spectral measures agree by rectangular polar decomposition, including multiplicity, and equal column counts then give equal trace mass at zero.

On the lattice torus write \(z_j=e^{i\xi_j}\), \(-\pi\le\xi_j\le\pi\).
The scalar \(\ell(\xi)=\sum_j(2-2\cos\xi_j)\) vanishes only at zero and is comparable to \(|\xi|^2\) there.
The row products are injective with spectrum accumulating at zero.
Both matrices have dense nonclosed range, and their nullities follow from the trace of their final support \(I_N\).
In particular \(L_N\) is injective, so the comparison projection on its last \(d-1\) blocks is constant.

## Grouped endpoints and adjacent times

Write \(U_1=U,\ U_i=I_N\) for \(i>1\) and \(q=1-\ell/M\).
For \(k\ge1\), finite multiplication of \(A^*A\) gives the following exact group-ring identity in its \(i,j\) block:
\[
 (Q_k)_{ij}=\delta_{ij}I_N
     - U_i^*U_j\, a_i^*a_j\,M^{-1}\sum_{v=0}^{k-1}q^v .                 \tag{1}
\]
Indeed \((A^*A)^r=A^*(AA^*)^{r-1}A\) for \(r\ge1\).
Each coefficient of \(q^v\) is the total amplitude of all lattice walks with that endpoint, including the holding term.
Formula (1) takes the signed second difference at the common endpoint and multiplies by the finite \(H\)-coefficient of \(U_i^*U_j\).
It thus computes the column product fibers before squaring.
On the torus its nonconstant multiplier is
\[
 m_{ij,k}(\xi)=\frac{\overline a_i a_j}{\ell}(1-q^k).
\]
The projection uses \(m_{ij,\infty}=\overline a_i a_j/\ell\) almost everywhere by bounded spectral convergence.

We verify the uniform Fourier bound
\[
 |\widehat m_{ij,k}(x)|\le C(1+|x|)^{-d},\qquad 1\le k\le\infty .       \tag{2}
\]
On each annulus \(|\xi|\asymp t\le t_0\), derivatives of order \(s\) of \(\overline a_i a_j/\ell\) are \(O_s(t^{-s})\) by the quotient rule and the quadratic lower bound for \(\ell\).
The positive function \(v=-\log q\) is comparable to \(t^2\) there and has derivatives of positive order \(s\) bounded by \(C_s t^{2-s}\).
Every derivative of order \(s>0\) of \(q^k=e^{-kv}\) is bounded there by a sum of \(C_s t^{-s}(kt^2)^b e^{-c kt^2}\) with \(1\le b\le s\).
These terms are uniform in \(k\), and the undifferentiated multiplier is bounded.
Derivatives on the smooth periodic region away from zero are uniformly bounded as \(q\) stays below one there and \(q>0\).
Resolve a neighborhood of the origin by smooth cutoff differences on dyadic annuli \(t=2^{-j}t_0\), whose order-\(s\) derivatives are \(O_s(t^{-s})\).
An annular integral is bounded in modulus by \(C_L t^d(1+t|x|)^{-L}\) by \(L\) integrations by parts in a coordinate with largest \(|x_i|\), together with the volume bound.
For \(L>d\), summing separately over \(t|x|\le1\) and \(t|x|>1\) gives (2), including the smooth exterior by periodic integration by parts.
The same estimates apply with \(1-q^k\) replaced by one.

All nonconstant coefficients in the \(H\) coordinate are confined to the same finite set for all \(k\).
The number of lattice points in each unit \(\ell^1\) shell of radius \(r\ge1\) is \(O((1+r)^{d-1})\), by counting nonnegative integer compositions and signs.
By (2) the squared shell mass is \(O((1+r)^{-d-1})\) for both \(Q_k\) and \(p\), with a changed constant for the bounded shifts of length in \(H\).
For \(d=4\), summing with \(\min(1,(r/R)^4)\) gives \(O(R^{-4}(1+\log R))\), and summing over \(r>R\) with weight \((1+r)^\beta\) gives \(O_\beta(R^{\beta-4})\).

With normalized torus volume, the exact squared increment at times \(k<l\) is
\[
 \|Q_k-Q_l\|_2^2=N\int_{\mathbb T^d}q^{2k}(1-q^{l-k})^2\,d\xi .
\]
Only the positive column spectrum contributes, and it has the same measure as the scalar row Gram repeated \(N\) times.
If \(l/k\) stays in a compact subinterval of \((1,\infty)\), the integral is \(O(k^{-d/2})\) by Gaussian integration near zero and exponential decrease elsewhere.
On a fixed annulus \(c/\sqrt k\le|\xi|\le2c/\sqrt k\) both factors have positive constant lower bounds, giving the reverse estimate for large \(k\).
For \(d=4\) the endpoint terms at \(R=2^j\) are summable after weighting by \(2^{\beta j}\) for \(\beta<4\).
The increment terms on the stated geometric schedule are comparable to \(2^{(\beta-2\kappa)j}\) for large \(j\), proving the threshold even at equality.

## The discontinuity, the critical exponent and support

The scalar diagonal block \(p_{ii}=I_N(1-|a_i|^2/\ell)\) has incompatible directional limits along the \(i\)-axis and any different axis at zero, as in the earlier [two-dimensional gradient example](Yin_C_A0056_v1.md#the-exponent-for-positive-matrices-and-the-spatial-condition).
It is smooth off zero, so it has no almost-everywhere equal continuous version.
Finite group polynomials on \(H\times\mathbb Z^d\) become continuous \(C_r^*(H)\)-valued functions of \(\xi\); their regular operator norm is the supremum norm by the lattice Fourier transform.
The same continuity holds for their norm limits.
Thus \(p\) lies outside the reduced matrix algebra, whereas the kernel projection of a closed-range matrix there belongs to it by continuous functional calculus above the spectral gap.
For \(d=3\), if the weighted moment with \(\beta>3\) were finite, Cauchy–Schwarz and \(\sum_x(1+|x|)^{-\beta}<\infty\) would make the Fourier series of the scalar diagonal absolutely summable, contradicting its discontinuity.
For \(d=4\), the second derivative in \(\xi_i\) of \(1-|a_i|^2/\ell\) has magnitude at least \(c|\xi|^{-2}\) on a cone about any different axis near zero.
Indeed after radial rescaling by \(r\), the diagonal multiplier at \(r\omega\) tends in \(C^2\) on a fixed annulus to \(1-\omega_i^2/|\omega|^2\) by the cosine expansion, and its indicated second derivative is nonzero at that other unit axis.
Square integration on this cone diverges like \(\int_0^\epsilon r^{-1}\,dr\).
If the fourth spatial moment were finite, Parseval for distributional derivatives would give a square-integrable second derivative, contrary to this bound already off the origin.

For the subgroup support test, the \(11\) entry of \(a_1 U\) has in its support every listed \(h\) at lattice coordinate zero as well as their translates by \(z_1\).
When an entry is translated on the left and right into a subgroup, the differences of its support elements belong to a conjugate of that subgroup.
Here they give all of \(H\) up to inner conjugation, and the central \(z_1\); the other scalar blocks give the remaining \(z_i\).
For \(p\), some lattice Fourier coefficient of \(\overline a_2a_1/\ell\) is nonzero, so a single off-diagonal entry of the block \(p_{21}\) contains all listed \(h\) at the same lattice coordinate.
Each \(p_{ii}\) has positive identity coefficient and positive Fourier coefficient at \(z_i\).
For the latter, condition on the other torus coordinates, writing \(s=\sum_{j\ne i}|a_j|^2>0\) almost surely.
The diagonal symbol \(s/(s+2-2\cos\xi_i)\) is strictly increasing in \(\cos\xi_i\), so its covariance with this nonconstant mean-zero random variable is positive, as is seen by taking half the expected product of differences of two independent copies.
The sine part integrates to zero.
Thus the diagonal entries recover every central \(z_i\) even under independent translations, and the off-diagonal entry recovers the normal factor \(H\), as asserted.

## Assessment history

### Decision endpoint-tails-without-gapped-representative

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:31 |
| status | proved |
| reason | Independent review verified the identical row products, signed endpoint estimates, sharp time and spatial thresholds and discontinuity. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rational matrices on the product with a lattice, different spatial behavior at identical scalar moments, and failure of a closed-range representative. |
| argument | [The matrices and their products](#matrices-with-identical-row-products) | Gram factorization, Fourier estimates, trace increments, sharpness and recovery of full support. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0104_v1.md#whole-argument-finding) | Independent review of the fixed argument and its stated applicability. |

## Current assessment

[Selected decision](#decision-endpoint-tails-without-gapped-representative)
