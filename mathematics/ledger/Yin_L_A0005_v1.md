---
author: Yin
---
# Independent rank constraints for bordered rational pencils: mechanisms and obstructions

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route four](../strategies/Yin_S_A0004.md).
The question is whether torsion-freeness and the regular representation supply an independent reason excluding the forbidden bordered rank interval in the [established criterion](../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria).
The main agent and two development helpers investigated the positive energy mechanism, complementary-block reduction, operator domains, weighted-tree obstruction and finite-section tests for Yin.
These findings identify exact interfaces and failures of proposed intermediate steps, without claiming a new positive group class or resolving the Task.
The complete investigation has an [independent whole-argument review](../audits/reviews/Yin_R_A0007_v1.md#exploration-finding), including its final positive-realization restriction and precise source and domain limits.

## Setting and the remaining rank interval

Let \(G\) be a finitely generated torsion-free group, \(H=\ell^2(G)\), \(B=\lambda(\mathbb CG)\), \(M=\mathcal N(G)\), and \(U=\mathcal U(M)\).
Use the faithful canonical trace on \(M\) and the unnormalized trace on its matrix amplifications.
Let \(L\in M_N(B)\) be affine linear in fixed regular generators and their inverses, and suppose \(L\) is invertible in \(M_N(U)\).
For a constant scalar row \(u\in M_{1,N}(\mathbb C)\) and column \(v\in M_{N,1}(\mathbb C)\), set
\[
Q=\begin{pmatrix}0&u\\v&L\end{pmatrix},
\qquad r=uL^{-1}v\in U.
\]
The established affiliated rank identity is
\[
\operatorname{rk}_G Q=N+\operatorname{rk}_G r,
\qquad
\dim_G\ker Q=\dim_G\ker r.
\]
The problem is to exclude \(0<\dim_G\ker Q<1\), equivalently \(N<\operatorname{rk}_G Q<N+1\), without assuming an Atiyah integer-rank conclusion.
No bounded inverse of \(L\) is assumed in the general setting.

## An independent positive rank certificate

The [energy and regular-transport theorem](../claims/Yin_C_A0003_v1.md#statement) supplies a sufficient condition that does not use Atiyah integrality.
For a positive definite constant matrix \(W\), a nonzero constant column \(v\), and \(u=\gamma v^*W\) with \(\gamma\ne0\), set \(H=\operatorname{Re}(WL)\).
If \(H\ge0\) and \(\ker H\cap\ker u=0\), its bounded energy argument gives \(\ker Q=0\), hence \(\operatorname{rk}_G Q=N+1\).
The proof and every hypothesis are retained in that fixed Claim, including the separate admissibility condition on \(L\) when \(H\) has a kernel.

Two regular-representation certificates make the needed kernel condition explicit.
For \(H=\sum_j C_j^*C_j(2-\zeta_jg_j-\overline{\zeta_j}g_j^{-1})\) with \(g_j\ne e\) and \(|\zeta_j|=1\), its kernel is exactly \((\bigcap_j\ker C_j)\otimes\ell^2(G)\).
For a finite graph incidence matrix whose edge rows are \(w_i-\zeta_e g_e w_j\), the kernel of \(D^*D\) has dimension equal to the number of connected components with identity transport around every closed walk.
An actual nonidentity loop transport kills a component's kernel by the absence of eigenvectors for infinite-order regular group unitaries.
These are independent integer-rank constraints for the stated structured operators over every torsion-free group.
If the positive real part is injective, denominator admissibility follows independently too, even without a spectral gap.
The construction does not convert an arbitrary linear realization into this structured form.

## Complementary-block reduction and the scalar obstruction

Assume \(u\ne0\) and \(v\ne0\); otherwise \(r=0\) already gives the allowed endpoint.
Choose constant \(S,T\in GL_N(\mathbb C)\) such that \(Sv=e_1\) and \(uT=e_1^*\), and put
\[
L'=SLT=\begin{pmatrix}a&b\\c&A\end{pmatrix}.
\]
Here \(A\) is the complementary \((N-1)\)-by-\((N-1)\) affine pencil, with the empty matrix understood when \(N=1\).
Multiplication of \(Q\) by the corresponding block-diagonal constant matrices gives
\[
Q'=\begin{pmatrix}0&1&0\\1&a&b\\0&c&A\end{pmatrix}.
\]
The upper-left two-by-two block
\[
J=\begin{pmatrix}0&1\\1&a\end{pmatrix},\qquad
J^{-1}=\begin{pmatrix}-a&1\\1&0\end{pmatrix}
\]
is invertible already over the group ring.
Its Schur correction vanishes, since
\[
\begin{pmatrix}0&c\end{pmatrix}
J^{-1}\begin{pmatrix}0\\b\end{pmatrix}=0.
\]
Consequently bounded group-ring block elimination gives
\[
\operatorname{rk}_G Q=2+\operatorname{rk}_G A,
\qquad
\operatorname{rk}_G r=\operatorname{rk}_G A-(N-2),
\qquad
\dim_G\ker Q=\dim_G\ker A.
\]
No integrality premise is used, but the constraint has merely moved to the complementary pencil.
For \(N=1\) the nonzero border is always full rank; for \(N=2\) the outstanding rank test is already a scalar group-ring injectivity problem.
For \(N\ge2\), admissibility of \(L\) forces \(N-2\le\operatorname{rk}_G A\le N-1\), without excluding the interior.

This is the elementary complementary-nullity mechanism.
The finite-dimensional field version was checked in [Bri13, arXiv v2, Proposition 2, p. 2](../literature/pdf/Bri13--arxiv-v2.pdf#page=2).
That source is attribution and comparison, not a premise asserting the result over affiliated rings; the displayed noncommutative block elimination proves the needed rank version directly.
Only the introduction, conventions and cited proposition were used, with no whole-paper or historical-priority claim.

### Uniformly controlled denominators still contain every scalar test

Let \(a\in\mathbb CG\) be any scalar element and choose \(\varepsilon>0\) with \(\varepsilon\|a\|\le1\).
For instance the sum of absolute values of its coefficients gives an explicit bound for choosing \(\varepsilon\).
After including its finite support in the group tuple, \(a\) is affine linear in that tuple.
Set
\[
L_a=\begin{pmatrix}1&\varepsilon a\\0&1\end{pmatrix},
\qquad u=e_1^*,\qquad v=e_2.
\]
Then
\[
L_a^{-1}=\begin{pmatrix}1&-\varepsilon a\\0&1\end{pmatrix},
\quad
\|L_a\|,\|L_a^{-1}\|\le2,
\quad
\operatorname{Re}L_a\ge\tfrac12 I_2,
\quad
uL_a^{-1}v=-\varepsilon a.
\]
The real-part bound follows because the off-diagonal selfadjoint perturbation has norm \(\varepsilon\|a\|/2\).
Thus even a uniformly accretive denominator with a polynomial bounded inverse retains the entire scalar analytic zero-divisor question when the border is unmatched.
This is an exact reduction of difficulty, not an example of a fractional rank over a torsion-free group.
In this example \(uv=0\), so no positive definite \(W\) and nonzero scalar \(\gamma\) can satisfy \(u=\gamma v^*W\), because that would give \(uv=\gamma v^*Wv\ne0\).

A second completion is
\[
\widetilde L_a=\begin{pmatrix}0&1\\1&\varepsilon a\end{pmatrix},
\qquad
\widetilde L_a^{-1}=\begin{pmatrix}-\varepsilon a&1\\1&0\end{pmatrix}.
\]
It has the same norm bounds, and \(e_1^*\widetilde L_a^{-1}e_1=-\varepsilon a\).
When \(a=a^*\), it is a selfadjoint denominator with a bounded inverse and a matched border, but its real part is indefinite.
Passing from any scalar \(b\) to \(a=b^*b\) preserves its kernel and makes this a test of the full scalar injectivity problem after enlarging the finite generating tuple.
Thus matching the border alone, even with selfadjointness and bounded invertibility, is insufficient to simplify that problem; the positive energy hypothesis supplies the additional information in the Claim.

### A positive realization restricts the scalar value

There is also an obstruction to an exact-value-preserving universal conversion into the positive energy class.
Suppose \(L\) is affiliated-invertible, \(u=\gamma v^*W\), and \(H=\operatorname{Re}(WL)\ge0\), with the notation of the Claim.
The affiliated algebra identity gives
\[
\operatorname{Re}(\gamma^{-1}r)
=v^*L^{-*}HL^{-1}v
=\bigl(H^{1/2}L^{-1}v\bigr)^*
  \bigl(H^{1/2}L^{-1}v\bigr)\ge0.
\]
All products here are closed affiliated products, and the last expression is positive as the square of a closed affiliated column.
The first equality follows by expanding \(H=(WL+L^*W)/2\) and cancelling the neighboring inverses in their displayed order.
Thus every scalar value represented by this energy class lies, after a scalar rotation and positive rescaling, in a closed accretive half-plane.
For a nonidentity element \(g\) of a torsion-free group, the regular unitary \(\lambda(g)\) has Haar spectral distribution on the circle by its bilateral-shift decomposition.
For every nonzero \(\gamma\), the real part of \(\gamma^{-1}\lambda(g)\) has a nonzero negative spectral subspace, so it is not positive.
Therefore even this already invertible rational element has no exact representation in the stated positive energy class, regardless of the state dimension.
This rules out a universal exact-value-preserving conversion, without ruling out more general transformations that preserve the relevant kernel or use additional independently known invertible factors.

## The domain-safe graph and its bounded cutoffs

The relevant affiliated-product and polar-decomposition foundations are the [retained MSY23 interfaces](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
They are accepted at that scope; the general construction of the affiliated algebra is not reproved here.

As a bounded operator on \(H^N\), \(L\) is injective with dense range.
Its affiliated inverse is the closed operator with domain \(\operatorname{Ran}L\).
Define the closed rectangular operator
\[
T=L^{-1}v,
\qquad
\operatorname{Dom}T=\{x\in H:vx\in\operatorname{Ran}L\}.
\]
This composition is closed: if \(x_j\to x\) and \(Tx_j\to y\), boundedness of \(v\) and closedness of \(L^{-1}\) give \(vx\in\operatorname{Dom}L^{-1}\) and \(Tx=y\).
It is densely defined by the affiliated-product calculus.
For a direct density check when \(v\ne0\), write \(v=\|v\|w\), where \(w:H\to H^N\) is a constant isometry, and choose spectral cutoffs \(f_j\uparrow I_N\) for \(|L^{-1}|\).
The projection onto \(wH\cap f_jH^N\) has unnormalized trace at least \(1-\operatorname{Tr}_N\otimes\tau(I_N-f_j)\).
Pulling these subspaces back by \(w\) gives subspaces of \(\operatorname{Dom}T\) whose projections increase to \(I_H\).
The case \(v=0\) has \(T=0\) on all of \(H\).

The affiliated scalar \(r\) is the closure of \(uT\), and put \(p=P_{\ker r}\in M\).
The bounded matrix \(Q\) has the exact graph kernel
\[
\ker Q
=\{(x,-Tx):x\in\operatorname{Dom}T\cap pH\}.
\]
Indeed, \(Q(x,y)=0\) means \(uy=0\) and \(vx+Ly=0\).
The second equation gives \(vx\in\operatorname{Ran}L\) and \(y=-Tx\), while the first becomes \(uTx=0\).
On \(\operatorname{Dom}T\), the closed operator \(r\) agrees with \(uT\), proving both inclusions.
This does not assert that every vector of \(\ker r\) belongs to \(\operatorname{Dom}T\).

For \(m>0\), let
\[
e_m=1_{[0,m]}(|T|)\in M.
\]
These scalar spectral projections increase strongly to \(1\), and their ranges lie in \(\operatorname{Dom}T\).
The finite projection-dimension inequality gives
\[
\tau(p\wedge e_m)\ge\tau(p)-\tau(1-e_m).
\]
Since \((p\wedge e_m)H\subseteq pH\cap\operatorname{Dom}T\), faithfulness of the trace shows that the latter domain is dense in \(pH\).
First-coordinate projection therefore defines a bounded injective equivariant map from the closed space \(\ker Q\) into \(pH\), with dense range.
Its polar decomposition identifies the corresponding dimension projections and yields
\[
\dim_G\ker Q=\tau(p).
\]
Thus the graph calculation recovers the bordered rank identity without an unjustified identification of unbounded domains.

There is also a quantitative bounded-cutoff statement.
For every \(\varepsilon>0\), choose \(m\) with \(\tau(1-e_m)<\varepsilon\).
On the closed submodule \((p\wedge e_m)H\), the operator \(T\) is bounded by \(m\), and its graph in \(\ker Q\) has dimension at least \(\tau(p)-\varepsilon\).
This preserves all but an arbitrarily small amount of the kernel dimension in a bounded graph.
The cutoffs \(e_m\) need not have finite propagation or group-ring entries, so this statement supplies neither an improved finite-boundary estimate nor quantization of \(\tau(p)\).

## An admissible bounded denominator with no finite-support kernel vector

The [earlier free-tree example](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) rules out finite-support extraction for arbitrary polynomial systems.
The following direct adaptation places that obstruction inside the exact constant-border family, with both borders nonzero and the denominator boundedly invertible.

Take \(G=F(g,h)\) and put
\[
a=2-g,\qquad b=2-h.
\]
Choose
\[
L=
\begin{pmatrix}
1&0&0\\
0&b&a\\
0&0&1
\end{pmatrix},
\qquad
u=(1,0,0),
\qquad
v=(0,0,1)^{\mathsf T}.
\]
The norm-convergent geometric series
\[
b^{-1}=\sum_{n\ge0}2^{-n-1}h^n
\]
belongs to \(\mathcal N(G)\) and satisfies \(\|b^{-1}\|\le1\).
Consequently
\[
L^{-1}=
\begin{pmatrix}
1&0&0\\
0&b^{-1}&-b^{-1}a\\
0&0&1
\end{pmatrix}
\]
is bounded, and \(r=uL^{-1}v=0\).
The actual bordered matrix is
\[
Q=
\begin{pmatrix}
0&1&0&0\\
0&1&0&0\\
0&0&b&a\\
1&0&0&1
\end{pmatrix}.
\]
It is affine linear and has both scalar borders nonzero.
Directly solving its rows gives
\[
\ker Q
=\left\{
\begin{pmatrix}x\\0\\b^{-1}ax\\-x\end{pmatrix}
:x\in H
\right\}.
\]
This bounded equivariant graph is isomorphic to \(H\), so
\[
\dim_G\ker Q=1,
\qquad
\operatorname{rk}_G Q=3.
\]
This calculation uses no Atiyah theorem for free groups.

### Weighted-tree proof of the absence of finite-support vectors

A finite-support vector in \(\ker Q\) would give \(x,y\in\mathbb CG\) satisfying
\[
(2-h)y=(2-g)x.
\]
The left Cayley graph of \(F(g,h)\), with edges \(s\longleftrightarrow gs\) and \(s\longleftrightarrow hs\), is a tree.
Regard the finite supports of \(x\) and \(y\) as a finite collection of oriented \(g\)- and \(h\)-edges.
In \((2-h)y-(2-g)x\), a \(g\)-edge with coefficient \(x_s\) contributes \(-2x_s\) at \(s\) and \(x_s\) at \(gs\), while an \(h\)-edge with coefficient \(y_s\) contributes \(2y_s\) at \(s\) and \(-y_s\) at \(hs\).
Distinct positive-generator edges give distinct undirected edges of this tree.
If the finite supporting forest is nonempty, it has a leaf incident to exactly one supported edge.
The equation at that leaf forces that edge coefficient to vanish, since every endpoint weight is nonzero.
Removing that edge and repeating proves \(x=y=0\).
Therefore
\[
\ker Q\cap(\mathbb CG)^4=\{0\}.
\]
The proof is the explicit weighted leaf-removal argument, rather than an application of a general denominator-clearing assertion.

### Exponentially accurate finite-support approximate vectors

For every integer \(m\ge0\), set
\[
z_m=\sum_{n=0}^{m}2^{-n-1}h^n a\delta_e,
\qquad
\xi_m=(\delta_e,0,z_m,-\delta_e)^{\mathsf T}.
\]
The finite geometric-series identity gives
\[
bz_m=(1-2^{-m-1}h^{m+1})a\delta_e,
\]
and hence
\[
Q\xi_m=
\begin{pmatrix}
0\\0\\-2^{-m-1}h^{m+1}a\delta_e\\0
\end{pmatrix}.
\]
Since \(a\delta_e=2\delta_e-\delta_g\),
\[
\|Q\xi_m\|=\sqrt5\,2^{-m-1},
\qquad
\|\xi_m\|\ge\sqrt2.
\]
Thus the exact-family example admits exponentially accurate finite-support approximate kernel vectors while having no nonzero exact finite-support kernel vector.
Bounded invertibility, exponential inverse decay and finite propagation therefore do not by themselves justify exact extraction.

### Exact scope of this obstruction

This example has \(N=3\), \(r=0\), and \(\operatorname{rk}_GQ=N\), so it lies at an allowed endpoint.
It is not a counterexample to the forbidden-interval assertion or to the Atiyah conjecture.
In particular, it does not refute a hypothetical extraction theorem restricted to \(0<\dim_G\ker Q<1\).
It does refute unrestricted extraction for the precise bordered family, even with the additional bounded-denominator hypotheses above.
Any use of a fractional-kernel restriction would require a separate argument; it cannot be obtained by applying the failed unrestricted principle.

## Cyclic translates and finite compressions can retain fractional density

The [earlier arc projection](../ledger/Yin_L_A0002_v1.md#why-infinite-orbits-and-scalar-injectivity-do-not-finish-the-argument) shows that translation equivariance alone does not quantize dimension.
Its finite compressions also show why linear independence of translates and accurate spectral cutoffs do not repair that argument.

Let \(G=\mathbb Z\), identify \(\mathcal N(G)=L^\infty(\mathbb T)\), and let \(p=1_E\) for an arc \(E\) with normalized Haar measure \(\alpha\in(0,1)\).
For \(n\ge1\), let \(F_n=\{0,\ldots,n-1\}\), let \(P_{F_n}\) be its coordinate projection, and write
\[
C_n=P_{F_n}pP_{F_n}\big|_{\mathbb C[F_n]}.
\]
With \(c_k=\widehat{1_E}(k)\), the matrix entries are \((C_n)_{ij}=c_{i-j}\), for \(0\le i,j<n\), after fixing the usual Fourier convention.
Every nonzero finite trigonometric polynomial has only finitely many circle zeros.
Thus its squared modulus has strictly positive integral on both \(E\) and its complement, and
\[
0<C_n<I_n.
\]
In particular every \(C_n\) has ordinary algebraic rank \(n\).
The same argument for any finite set of exponents shows that every finite family of translates of \(p\delta_e\) is linearly independent.

### Exact Fourier trace defect

The diagonal and Parseval identities give
\[
\operatorname{tr}C_n=\alpha n,
\qquad
\sum_{k\in\mathbb Z}|c_k|^2=\alpha.
\]
Counting pairs with difference \(k\) gives
\[
\operatorname{tr}C_n^2
=\sum_{|k|<n}(n-|k|)|c_k|^2.
\]
Therefore the exact nonnegative trace defect is
\[
d_n:=\operatorname{tr}(C_n-C_n^2)
=n\sum_{|k|\ge n}|c_k|^2
 +\sum_{|k|<n}|k|\,|c_k|^2.
\]
For an arc, \(c_0=\alpha\) and \(|c_k|\le1/(\pi|k|)\) whenever \(k\ne0\).
Consequently, for \(n\ge2\),
\[
0\le d_n
\le\frac{2}{\pi^2}
\left(\frac{n}{n-1}+\sum_{k=1}^{n-1}\frac1k\right)
=O(\log n).
\]
This estimate follows directly from \(\sum_{k=n}^\infty k^{-2}\le(n-1)^{-1}\); no asymptotic Toeplitz theorem is used in its proof.

### Spectral counting and its failure to quantize dimension

Let \(\lambda_1,\ldots,\lambda_n\in(0,1)\) be the eigenvalues of \(C_n\), and fix \(\varepsilon\in(0,1)\).
For \(\lambda\ge\varepsilon\), one has \(1-\lambda\le\lambda(1-\lambda)/\varepsilon\), while for \(\lambda<\varepsilon\), one has \(\lambda\le\lambda(1-\lambda)/(1-\varepsilon)\).
Summing these two estimates yields
\[
\left|\#\{j:\lambda_j\ge\varepsilon\}-\operatorname{tr}C_n\right|
\le
\max\{\varepsilon^{-1},(1-\varepsilon)^{-1}\}\,d_n.
\]
Hence
\[
\#\{j:\lambda_j\ge\varepsilon\}
=\alpha n+O_\varepsilon(\log n).
\]
Thus full ordinary rank of all finite Gram matrices, linear independence of all finite translates, a logarithmic projection defect and accurate spectral-cutoff counts coexist with an arbitrary fractional limiting density \(\alpha\).
The finite counting functions are integer valued, but division by \(n\) does not make their limit an integer.
The smallest eigenvalues also cannot have a positive uniform lower bound, since a positive proportion of the eigenvalues approach the zero end in the stated counting sense.

### Source identification and group-rational boundary

After rotating the arc to be centered, \(C_n\) is unitarily equivalent to the classical prolate matrix with bandwidth \(W=\alpha/2\).
The primary [KRD20 arXiv v2](../literature/pdf/KRD20--arxiv-v2.pdf), Section 2.1, equation (1), printed pp. 3--4, identifies that finite matrix and its time- and band-limiting interpretation.
Section 3.1, printed pp. 5--6, records its strict spectral bounds, trace, and known clustering behavior.
These passages were read online in the primary 29-page arXiv version revised on 28 September 2020 to verify the attribution and conventions.
The local Fourier trace-defect and counting derivation above is self-contained.
The source's stronger eigenvalue estimates, their full proofs and its historical references were not audited or used as proof inputs here.
No novelty claim is made for this classical finite-section phenomenon.

This projection is not in the actual rational closure of \(\mathbb C\mathbb Z\).
That closure is \(\mathbb C(z)\) in the affiliated multiplication algebra, by the same nonzero-polynomial null-zero-set argument used in the [abelian comparison](../ledger/Yin_L_A0004_v1.md#actual-rank-and-the-complete-atiyah-premise).
A rational function equal to \(1_E\) would vanish on a positive-measure complement, forcing its numerator to be identically zero, contrary to \(\alpha>0\).
The projection also has infinite propagation.
It therefore supplies a boundary for orbit and compression arguments, not an admissible rational Schur complement or a counterexample to the Task.

## Consequence for the independent-constraint search

The positive energy theorem and its cyclic and finite-graph realizations exclude the forbidden interval for their exact stated matrix families without a general Atiyah input.
Their use of torsion-freeness is explicit: it removes fixed vectors of the actual nontrivial loop transports and cyclic differences.
The complementary-block and uniformly controlled denominator reductions show that denominator regularity and border size do not independently remove the scalar analytic zero-divisor obstruction.
The graph description gives an exact domain interface and bounded submodules of arbitrarily close kernel dimension, but no independent discreteness statement.
The free-group example prevents the bordered structure, bounded denominator or inverse decay from being used as an unrestricted finite-support extraction principle.
The cyclic finite-section example prevents independence and spectral counting alone from being used to turn normalized local dimensions into integers.
The unresolved step must exploit additional actual group-rational structure, a special algebraic form of the pencil, or another independent constraint that excludes a proper nonzero scalar rational kernel.
None of these obstructions rules out such an additional mechanism.
The next useful positive test is a positive-energy certificate for a concrete nontrivial realization, or a justified transformation preserving its kernel while using only independently known invertible factors.
An exact-value-preserving universal conversion to the matched positive class is ruled out by the cyclic unitary example above.
Replacing \(L\) by \(L^*L\) does not provide that conversion: \(L^{-1}=(L^*L)^{-1}L^*\) changes the right border to \(L^*v\), which is generally a group-ring column rather than the required matching constant column.
Likewise, positive regularization alone supplies no kernel-dimension continuity at the zero-regularization endpoint.
