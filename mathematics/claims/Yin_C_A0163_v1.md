---
author: Yin
---

# How many sites does a polynomial kernel certificate need?

## Statement

For a discrete group \(G\), write \(H_G=\ell^2(G)\), \(U_G=L^0(\mathcal N(G))\), and \(D_G=\operatorname{Div}_{U_G}(\mathbb CG)\).
Let \(A\in M_{m,n}(\mathbb CG)\) act by left convolution and let \(S\) be a finite set containing the identity and the group elements occurring in its entries.
The sites of a column \(y\in(\mathbb CG)^n\) are the group elements where at least one coordinate of \(y\) has a nonzero coefficient.
For \(k\ge1\), let \(W_k\) be the closed span in \(H_G^n\) of all solutions of \(Ay=0\) supported on at most \(k\) sites.

1. Put \(T=S^{-1}S\) and \(B_k=T^{\lfloor k/2\rfloor}\), with \(T^0=\{1\}\).
   There is a finite matrix \(C_k\) over \(\mathbb CG\) whose columns each solve \(Ay=0\) on at most \(k\) sites of \(B_k\) and whose closed range is \(W_k\).
   Its columns can be obtained by solving ordinary finite complex linear systems.
   Consequently, the translates of all \(k\)-site solutions span \(\ker A\) after closure exactly when the one finite matrix \(C_k\) has rank \(\dim_G\ker A\).
   In that event \(p_{\ker A}\in M_n(D_G)\).
   The exponent \(\lfloor k/2\rfloor\) is sharp even for matrices with \(S=\{1,t\}\) on \(G=\langle t\rangle\cong\mathbb Z\).

2. For every \(c\ge1\) there is a torsion-free nilpotent group \(\Gamma_c=\langle a_c,b_c\rangle\) such that the propagation-one row \(A_c=(a_c-1,\ b_c-1)\) has kernel of unnormalized von Neumann dimension one.
   Its entire affiliated kernel has the one-column generator
   \[
       Y_c=\begin{pmatrix}a_c-1&b_c-1\\0&1\end{pmatrix}^{-1}
                \binom{0}{1},
   \]
   and its Hilbert kernel has orthogonal projection \(I_2-A_c^*(A_cA_c^*)^{-1}A_c\).
   If \(s_c\) is the smallest number of sites supporting a nonzero polynomial kernel column, then
   \[
                   \lfloor c/2\rfloor+1\ \le s_c\ \le 3\cdot 2^c-2 .
   \]
   For these rows \(W_k=0\) when \(k<s_c\), and \(W_k=\ker A_c\) when \(k\ge s_c\).
   The integer \(s_c\) equals the least number of distinct positive-edge tails of a simple circuit in the Cayley graph with edges oriented from \(g\) to \(a_cg,b_cg\).

3. All these marked pairs embed in one two-generated torsion-free amenable group \(G_*\).
   The same formulas, dimensions and exact thresholds \(s_c\) hold for their rows over \(G_*\).
   Thus even in a fixed group, at fixed matrix size and with only three group elements in the input and in the displayed rational realization, a uniform bound on the number of sites of a polynomial kernel column can exclude the entire kernel.
   The word lengths of \(a_c,b_c\) may grow in the fixed marking of \(G_*\).
   In the varying groups \(\Gamma_c\) they are generators.

4. Put \(B_c=A_c^*A_c\), let \(\tau_2\) be the normalized matrix trace extending the group trace, and take \(d\ge1\) with \(2d\le c\).
   In both \(\Gamma_c\) and \(G_*\), the Christoffel upper bound computed from the first \(2d\) moments is exactly
   \[
       \min_{\deg q\le d,\ q(0)=1}\tau_2\bigl(q(B_c)^*q(B_c)\bigr)
           =\frac12+\frac{1}{2(2\cdot3^d-1)}.
   \]
   At these same inputs the normalized rank lower bound from any family of polynomial kernel columns on at most \(d\) sites per column is zero.
   The rational column \(Y_c\) gives the exact lower bound \(1/2\) at every \(c\).

For [the finite-rank criterion](../tasks/Yin_T_A0003_v3.md#contract), a bounded number of sites therefore gives a finite search window for polynomial annihilators of each prescribed finite-propagation input.
The [rational-annihilator criterion](Yin_C_A0160_v1.md#statement) allows the inverses in \(Y_c\).
The example quantifies the loss incurred by replacing such rational witnesses with polynomial columns, even when each individual kernel admits a polynomial column of full rank.

<a id="argument"></a>
## Reduction to a finite ball

For a solution \(y\) with finite set of sites \(F\), join distinct \(g,h\in F\) when \(Sg\cap Sh\ne\varnothing\).
The image under \(A\) of the restriction of \(y\) to a connected component \(P\) is supported on \(SP\).
These output sets are disjoint for distinct components, so each component restriction solves \(Ay=0\).
This uses the collision graph of the [scalar lifting argument](../ledger/Yin_L_A0054_v1.md#lifting-a-small-algebraic-annihilator) with all input coordinates at a site kept together.
Each edge has \(h\in Tg\).
For \(|P|\le k\), choose a spanning tree and a midpoint vertex of a longest path in the tree.
If that path has length \(d\), each vertex has distance at most \(\lceil d/2\rceil\) from the midpoint, since a branch extending farther would give a longer path to one endpoint.
Since \(d\le k-1\), there is a site \(g_0\) with \(P\subseteq B_k g_0\).
Right multiplication by \(g_0^{-1}\) moves the solution into \(B_k\) and preserves its equation.

For each subset \(Q\subseteq B_k\) with \(|Q|\le k\), compute a complex basis for the kernel of the restriction from inputs on \(Q\) to outputs on \(SQ\).
Take all these basis vectors as columns of \(C_k\), using a zero column if all the restricted kernels vanish.
The closure of their translates equals the closed range of \(C_k\), since finitely supported inputs are dense and the columns act by bounded convolution.
The component reduction identifies this closure with \(W_k\).
As \(W_k\subseteq\ker A\), faithfulness of the trace gives equality exactly at equality of dimensions.
The [finite-column projection formula](../ledger/Yin_L_A0076_v1.md#a-finite-set-of-kernel-generators-after-hilbert-space-closure) then gives
\[
               p_{\ker A}=C_k C_k^*(A^*A+C_k C_k^*)^{-1}.
\]

For sharpness take the \(k-1\) equations \(y_{j+1}=t y_j\), \(1\le j<k\), on \(\mathbb Z\), with a zero row for \(k=1\).
The kernel consists of \((1,t,\ldots,t^{k-1})^{\mathsf T}f\), \(f\in H_{\mathbb Z}\).
Picking any nonzero coefficient of a polynomial \(f\) exhibits \(k\) consecutive sites in the union of the coordinate supports.
The vector with \(f=1\) attains \(k\) sites and its translates span the kernel.
In \(T=\{1,t,t^{-1}\}\) the least radius of a ball containing \(k\) consecutive sites is \(\lfloor k/2\rfloor\).

## Two-column kernels and the shortest polynomial flow

Consider an infinite-order \(a\) and another element \(b\) in a discrete group.
The difference \(a-1\) and its adjoint have zero Hilbert kernel, since an invariant square-summable function on an infinite \(a\)-orbit vanishes.
Thus \(a-1\) is an affiliated unit, \(A=(a-1,b-1)\) has dense range, and its kernel has dimension one.
Solving the affiliated row equation for the first coordinate gives precisely the multiples of the displayed column \(Y\) by elements of \(U_G\).
The positive scalar \(AA^*\) is injective, and the affiliated inverse in \(I_2-A^*(AA^*)^{-1}A\) gives the orthogonal kernel projection by polar decomposition.
Both formulas use group-ring entries and inverses of affiliated units.

Take the truncated free associative ring
\[
       R_c=\mathbb Z\langle x,y\rangle/(\text{words of length }c+1),
\]
and let \(J\) be its ideal of positive-degree elements.
Set \(a_c=1+x,\ b_c=1+y\), and \(\Gamma_c=\langle a_c,b_c\rangle\le1+J\).
Inverses exist by the finite geometric sum.
The inclusion \([1+J^i,1+J^j]\subseteq1+J^{i+j}\) follows by commuting the two factors modulo \(J^{i+j}\), so \(\Gamma_c\) is nilpotent of class at most \(c\).
If the first nonzero degree of \(u\in J\) is \(d\), the degree-\(d\) coefficient vector of \((1+u)^m-1\) is \(m\) times that of \(u\) for every \(m\ge1\).
Thus \(1+J\) is torsion-free.

A nonempty freely reduced word in \(a_c,b_c\) is a product of \(r\) alternating syllables with nonzero integer exponents \(e_1,\ldots,e_r\).
When \(r\le c\), consider the alternating degree-\(r\) monomial with the same sequence of letters.
In the truncated expansions of the syllables, each contributing factor supplies at most one letter to this monomial, since two consecutive letters from a single syllable would agree.
Thus each factor supplies one, and the coefficient is \(\prod_j e_j\ne0\), also for negative exponents.
In particular no nonempty freely reduced word of length at most \(c\) is trivial in \(\Gamma_c\).

For an upper bound on a relator length, in the abstract free group \(F(a,b)\) put \(w_1=b\) and \(w_{j+1}=[a,w_j]=a w_j a^{-1}w_j^{-1}\).
To see that a reduced word commuting with \(a\) is a power of \(a\), strip its leading and trailing powers of \(a\).
Any nonempty remaining word begins and ends in \(b^{\pm1}\), so conjugating \(a\) by it cannot give \(a\).
Inductively \(w_{j+1}\) is nontrivial and, having zero \(a\)-exponent sum, cannot be a power of \(a\).
Its length satisfies \(|w_{j+1}|\le2|w_j|+2\), so \(|w_{c+1}|\le3\cdot2^c-2\).
Its image belongs to \(1+J^{c+1}=\{1\}\).
The underlying undirected Cayley graph consequently has a simple circuit of length at most \(3\cdot2^c-2\), obtained from the closed reduced walk for this word.
Each simple circuit has length greater than \(c\).
The edges of this graph are distinct as unoriented edges for the two marked directions, since \(a_c,b_c\) have distinct independent degree-one coefficients and infinite order.

A polynomial column \((u,v)^{\mathsf T}\) is a finite edge chain, assigning coefficient \(u(g)\) to \(g\to a_cg\) and \(v(g)\) to \(g\to b_cg\).
Its boundary is \(A_c(u,v)^{\mathsf T}\).
The graph of nonzero edges of a nonzero chain with zero boundary has no vertex of degree one, and therefore contains a simple circuit.
All its positive-edge tails are sites of the chain, independently of the direction in which the circuit is traversed.
Conversely, assigning coefficients \(1\) or \(-1\) along an oriented traversal gives a kernel column with precisely the positive-edge tails of that circuit as its sites.
Since a site can supply at most two edges, a circuit of length \(\ell\) occupies between \(\lceil\ell/2\rceil\) and \(\ell\) sites.
This proves the formula for \(s_c\) and both bounds.

Every nontrivial finitely generated subgroup \(K\le\Gamma_c\) maps onto \(\mathbb Z\).
Indeed choose the smallest positive degree \(d\) occurring as a lowest degree in some \(g-1\), \(g\in K\setminus\{1\}\).
The degree-\(d\) component of \(g-1\) is additive under multiplication in \(K\), and some coordinate maps \(K\) onto a nonzero subgroup of \(\mathbb Z\).
Thus \(\Gamma_c\) is locally indicable.
By [Jaikin-Zapirain and López-Álvarez, Corollary 6.2](../audits/literature/JZLA20/Yin_U001.md#atiyah-proof), every nonzero scalar in \(\mathbb C\Gamma_c\) has rank one.
Every nonzero polynomial column therefore has rank one, since one of its coordinates is injective.
A circuit attaining \(s_c\) gives a column of this rank in \(\ker A_c\), and faithfulness of the trace identifies its closed range with the whole kernel.

## All thresholds in one fixed group

Left multiplication on the integral word basis of \(R_c\) embeds \(\Gamma_c\) into \(\mathrm{UT}_{2^{c+1}-1}(\mathbb Z)\), the upper unitriangular integer matrices of that size.
Order the basis by decreasing word length so the positive-degree terms lie strictly above the diagonal.
The representation is faithful because multiplication evaluated at \(1\) recovers the element.

Let \(N\) be the group of upper unitriangular matrices indexed by \(\mathbb Z\) with only finitely many nonzero off-diagonal entries, and let \(G_*=N\rtimes\mathbb Z\), with the action shifting both matrix indices by one.
Every finite subset of \(N\) lies in a finite upper unitriangular block.
Each block is torsion-free and nilpotent by the same filtration argument applied to strictly upper triangular matrices.
Hence \(N\) is torsion-free and locally nilpotent.
It is amenable as a directed union of nilpotent groups, and its extension \(G_*\) by \(\mathbb Z\) is amenable and torsion-free.
The shift conjugates \(I+E_{0,1}\) to the adjacent elementary transvections.
Together they generate \(G_*\), since \([I+E_{i,j},I+E_{j,k}]=I+E_{i,k}\) for \(i<j<k\).
Powers give all integral coefficients, and elimination of successive superdiagonals expresses every finite block as a product of these matrices.
Embed each \(\Gamma_c\) in a consecutive block of \(N\).

A chain over \(G_*\) decomposes over the disjoint right cosets \(\Gamma_c g\), each of which is preserved by both left shifts in \(A_c\).
Its restriction to each coset therefore solves the same boundary equation when the original chain does.
Right translation identifies that coset with \(\Gamma_c\), preserving the number of sites.
This proves that the smallest size of a nonzero polynomial kernel column in \(G_*\) remains \(s_c\).
The column of an attaining circuit still has an injective coordinate by applying the same coset decomposition to its convolution operator.
The formulas and full-range conclusion for \(A_c\) over \(G_*\) follow.

## Exact moment bounds on the tree balls

Write \(L_c=A_cA_c^*=4-a_c-a_c^{-1}-b_c-b_c^{-1}\).
For \(j\ge1\), cycling the factors gives \(\tau_2(B_c^j)=\tau(L_c^j)/2\).
The constant moments of both \(B_c\) and \(L_c\) equal one, so \(q(0)=1\) gives
\[
       \tau_2\bigl(q(B_c)^*q(B_c)\bigr)
          =\tfrac12+\tfrac12\Vert q(L_c)\delta_e\Vert_2^2 .
\]
For \(j\le 2d\le c\), extracting the coefficient of the identity in \(L_c^j\) gives exactly the same number in the free group on the two marked letters.
Indeed every contributing word has length at most \(j\), and the only such words representing the identity reduce freely to the empty word.
The embedding in \(G_*\) preserves all these coefficients.
It suffices to minimize the squared norm on the right for the free group.

There put \(s=a+a^{-1}+b+b^{-1}\) and \(L=4-s\).
The vector \(q(L)\delta_e\) is supported in the radius-\(d\) ball, whose cardinality is \(N_d=1+\sum_{j=1}^d4\cdot3^{j-1}=2\cdot3^d-1\).
The homomorphism sending every group element to \(1\) sends \(L\) to zero, so the sum of this vector's coefficients is \(q(0)=1\).
Cauchy–Schwarz gives squared norm at least \(1/N_d\).
For equality, let \(u_j\) be the sum in the group ring of all words of reduced length \(j\).
Counting possible cancellations in a tree gives \(u_0=1\), \(u_1=s\), \(u_2=s^2-4\), and \(u_{j+1}=s u_j-3u_{j-1}\) for \(j\ge2\).
Hence \(N_d^{-1}\sum_{j=0}^d u_j=q(L)\) for some polynomial of degree at most \(d\).
Its coefficients sum to one and its squared norm at \(\delta_e\) is \(1/N_d\).
This gives the claimed minimum.
The lower rank of zero follows from \(s_c>d\), and \(Y_c\) has rank one by its second coordinate, or equivalently by the kernel projection formula.
Appending a zero second column gives a square witness of the same rank in the formulation of the moment criterion.

## Assessment history

### Decision sparse-kernel-sites

| Field | Value |
| --- | --- |
| date | 2026-11-25T13:38 |
| status | proved |
| reason | Separating the sites into connected components localizes sparse solutions, while the nilpotent approximations and the tree moment calculation show how far polynomial witnesses can lag behind a fixed rational witness. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The sharp search radius, two-column examples in torsion-free nilpotent groups and one fixed host, and the exact Christoffel bounds. |
| argument | [Argument](#argument) | Component localization, integral word expansions, shortest flows, the common unitriangular host and radial polynomials on the tree. |
| dependency | [Collision graph](../ledger/Yin_L_A0054_v1.md#lifting-a-small-algebraic-annihilator) | The scalar component argument extended here to columns. |
| dependency | [Projection formula](../ledger/Yin_L_A0076_v1.md#a-finite-set-of-kernel-generators-after-hilbert-space-closure) | Rational recovery after finite column exhaustion. |
| dependency | [Locally indicable groups](../audits/literature/JZLA20/Yin_U001.md#jzla20-u001) | Corollary 6.2 for injectivity of the nonzero group-ring coordinate. |
| dependency | [Moment bounds](Yin_C_A0160_v1.md#statement) | Normalized upper and lower kernel estimates. |
| review | [Sparse kernel columns](../audits/reviews/Yin_R_A0173_v1.md#sparse-kernel-columns) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-sparse-kernel-sites)
