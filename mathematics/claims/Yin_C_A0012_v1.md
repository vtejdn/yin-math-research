---
author: Yin
---
# A specialization certificate for finite compressed transport

Date: 2026-11-12 (Asia/Hong_Kong).
This argument serves [A0001](../tasks/Yin_T_A0001_v1.md#contract) and the finite-transport investigation in [S_A0006](../strategies/Yin_S_A0006.md).
It asks whether a full-row certificate at an actual central-variable specialization supplies information about the overlap defect that mere rational origin did not supply in C_A0011.

Its new interface is a specialization theorem for finite operator-coefficient Laurent matrices and rational expressions whose selected inverse gates are defined at the specialization.
The subsequent graded residual and bounded finite-matrix kernel calculation reuse existing mechanisms.
Neither a coefficient division algebra nor an integer-rank assertion for arbitrary matrices over the coefficient group is assumed.

## Statement

Let \(H\) be any torsion-free group, let \(d\ge1\), and put
\[
N=H\times\mathbb Z^d.
\]
Write \(x_1,\ldots,x_d\) for the central auxiliary generators.
Let \(\sigma\) fix \(H\) pointwise and act on these generators through an element of \(GL_d(\mathbb Z)\).
Put \(G=N\rtimes_\sigma\langle t\rangle\), with \(tnt^{-1}=\sigma(n)\) and infinite cyclic height quotient.
All traces are canonical group traces with unnormalized matrix trace, written \(\tau_k=\operatorname{Tr}_k\otimes\tau\) for the relevant group trace \(\tau\).

For \(1\le r\le n\), let
\[
M\in M_{r,n}(\mathbb CN),
\qquad
M_0:=M(1,\ldots,1)\in M_{r,n}(\mathbb CH).
\]
Assume that the row Gram matrix
\[
L_0=M_0M_0^*
\tag{1}
\]
has an independently established bounded inverse in \(M_r(\mathcal N(H))\).
Then \(M\) has full actual row rank \(r\), and its complete kernel projection is the bounded rational matrix
\[
p=I_n-M^*(MM^*)^{-1}M,
\qquad
\tau_n(p)=n-r.
\tag{2}
\]
The inverse in (2) is an actual affiliated inverse and need not be bounded.

The overlap matrix
\[
W=p\sigma(p)p+(I_n-p)
\tag{3}
\]
is an actual affiliated unit in \(M_n(\mathcal U(N))\).
Consequently the compressed hopping \(K=ptp|_p\) and its adjoint have zero kernel on the \(p\)-corner.
Normality of \(K\) is unnecessary.

For every selfadjoint finite coefficient potential \(V\in M_n(\mathbb CN)\), the residual
\[
R_V=p\bigl((t+t^{-1})I_n+V\bigr)p\big|_p
=K+K^*+pVp
\tag{4}
\]
is injective and has an actual affiliated corner inverse.
For \(B=M^*M\), the complete bounded-matrix conclusion is
\[
\mathcal H_V=
\begin{pmatrix}
(t+t^{-1})I_n+V&B\\
B&0
\end{pmatrix}\in M_{2n}(\mathbb CG),
\]
\[
\boxed{
P_{\ker\mathcal H_V}=\operatorname{diag}(0,p),
\qquad
\dim_G\ker\mathcal H_V=n-r.
}
\tag{5}
\]
No bounded inverse of \(B\) on its support is required.

In fact the argument needs only an independently established affiliated inverse for \(L_0\), rather than a bounded inverse.
The bounded condition in (1) is a convenient stronger premise.
This distinction is essential in the specialization proof: successive generic slices can be injective without having bounded inverses.

<a id="argument"></a>
## The finite-trace eigenvalue input

Let \((\mathcal A,\tau)\) be a finite von Neumann algebra with faithful normal finite trace.
Write \(\mathcal U(\mathcal A)\) for its closed affiliated algebra and \(\tau_k=\operatorname{Tr}_k\otimes\tau\).
All sums, products and inverses of affiliated operators below mean their closed affiliated-algebra operations.

For \(T\in M_k(\mathcal U(\mathcal A))\) and distinct complex numbers \(\lambda_1,\ldots,\lambda_s\), let \(e_j=P_{\ker(T-\lambda_j)}\).
The [domain-correct MSY23 Lemma 5.19 interface](../audits/literature/MSY23/Yin_U006.md#lemma-519-domain-repair) gives
\[
\sum_{j=1}^s\tau_k(e_j)
=\tau_k\left(\bigvee_{j=1}^s e_j\right)
\le k\tau(1).
\tag{6}
\]
Its bounded-row proof applies to actual affiliated \(T\).
Finite sums of genuine eigenvectors are treated by a scalar Vandermonde matrix, and rectangular polar decomposition supplies the trace equality.
There is no passage of an unbounded operator through an arbitrary norm limit and no orthogonality assumption on the eigenspaces.

It follows that \(T\) has at most countably many complex eigenvalues.
Indeed, for every positive integer \(a\), there are only finitely many \(\lambda\) with
\(\tau_k(P_{\ker(T-\lambda)})\ge1/a\).
Every nonzero eigenprojection has positive trace by faithfulness, so the union of these finite sets exhausts the eigenvalues.
By the finite-trace inverse criterion, every other \(T-\lambda\) is an actual affiliated unit.
No positive lower bound for the traces of nonzero projections is used.

## One-variable specialization with an affiliated constant inverse

Let
\[
P(z)=\sum_{j=0}^{\ell}A_jz^j
\in M_k(\mathcal A[z])
\]
have bounded coefficients, and suppose \(P(1)\) has an actual affiliated inverse.
Set
\[
\widehat P(y)=P(1+y)=A'_0+\cdots+A'_\ell y^\ell,
\qquad
A'_0=P(1).
\]
The inverse of \(A'_0\) may be unbounded.
For \(\ell=0\), every value is the same affiliated unit.
For \(\ell\ge1\), put \(C_j=(A'_0)^{-1}A'_j\) and form the actual affiliated matrix
\[
T=
\begin{pmatrix}
-C_1&-C_2&\cdots&-C_\ell\\
I_k&0&\cdots&0\\
0&I_k&\ddots&\vdots\\
\vdots&\ddots&\ddots&0
\end{pmatrix}.
\tag{7}
\]
There is no inverse of any coefficient \(A'_j\), \(j>0\), in this construction.

The lower-right \((\ell-1)k\)-square block of \(I_{\ell k}-yT\) is lower bidiagonal with identity diagonal and subdiagonal \(-yI_k\).
It has a finite triangular inverse for every scalar \(y\).
Its Schur complement is
\[
I_k+C_1y+\cdots+C_\ell y^\ell=(A'_0)^{-1}\widehat P(y).
\]
Consequently the [affiliated rank invariance](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) gives
\[
\operatorname{rk}(I_{\ell k}-yT)
=(\ell-1)k\tau(1)+\operatorname{rk}(\widehat P(y)).
\tag{8}
\]
For \(\ell=1\), this is the direct identity without a lower block.
For \(y\ne0\), the left side fails to be full precisely when \(y^{-1}\) is an eigenvalue of \(T\).
At \(y=0\), the value \(\widehat P(0)=P(1)\) is already a unit.
By (6), only countably many \(y\), hence only countably many \(z\), can be bad.

Thus
\[
P(1)\in GL_k(\mathcal U(\mathcal A))
\quad\Longrightarrow\quad
P(z)\in GL_k(\mathcal U(\mathcal A))
\text{ for all but countably many }z\in\mathbb C.
\tag{9}
\]
All inverses and equivalences in this proof are affiliated matrix identities.
No companion eigenvector is constructed by repeatedly applying an uncontrolled unbounded coefficient to a Hilbert-space vector.

For a Laurent polynomial, multiply by a sufficiently large scalar power of \(z\) before applying this argument.
At \(z=1\) that multiplication changes nothing, and on \(\mathbb T\) its scalar factor is a unit.
Therefore (9), restricted to \(\mathbb T\), also holds for finite Laurent matrices.
The same proof works at any prescribed nonzero scalar base point by translation after clearing negative powers.
The boundedness of the original polynomial coefficients does not make the inverse of its constant value bounded, and the proof has not assumed otherwise.

## Several central variables and the actual trace

Let
\[
P(z_1,\ldots,z_d)\in
M_k(\mathcal A[z_1^{\pm1},\ldots,z_d^{\pm1}])
\]
have finitely many bounded coefficients and suppose \(P(1,\ldots,1)\) is an affiliated unit.
Then
\[
P(z)\in GL_k(\mathcal U(\mathcal A))
\quad\text{for Haar-almost every }z\in\mathbb T^d.
\tag{10}
\]

The proof is induction on \(d\).
For \(d=1\), use (9).
For the inductive step, first apply the claim to \(P(z_1,\ldots,z_{d-1},1)\).
For almost every \(z'=(z_1,\ldots,z_{d-1})\), this value is an affiliated unit.
For each such \(z'\), the one-variable polynomial \(z_d\mapsto P(z',z_d)\) has that actual unit as its value at \(1\), so its bad \(z_d\)-set is countable.
This is where a theorem requiring a bounded inverse at every slice would be insufficient.

The bad set is measurable.
For each positive integer \(a\), the function
\[
z\longmapsto
\tau_k\!\left((I_k+aP(z)^*P(z))^{-1}\right)
\]
is continuous, because \(P(z)\) is norm-continuous and the positive inverse has a uniform lower bound before inversion.
Its decreasing pointwise limit is
\[
\kappa(z)=\tau_k(P_{\ker P(z)}).
\tag{11}
\]
The set \(\{\kappa>0\}\) is therefore Borel.
Fubini now proves (10), without a countability assumption on the set of good slices.

Under the actual tensor product
\[
\mathcal B=\mathcal A\,\overline\otimes\,L^\infty(\mathbb T^d),
\qquad
\tau_{\mathcal B}=\tau\otimes\mu,
\]
the Laurent matrix \(P\) is a bounded operator.
Bounded functional calculus and the normal tensor-product trace give
\[
\tau_{\mathcal B,k}(P_{\ker P})
=\lim_{a\to\infty}
\int_{\mathbb T^d}
\tau_k\!\left((I_k+aP(z)^*P(z))^{-1}\right)\,d\mu(z)
=\int_{\mathbb T^d}\kappa(z)\,d\mu(z)=0.
\tag{12}
\]
The integrands are bounded by \(k\tau(1)\), so dominated convergence is applicable.
Faithfulness proves injectivity of the actual bounded operator \(P\), and finite-trace polar decomposition gives its actual affiliated inverse.

This is the required integrated specialization theorem.
It does not replace the torus integral by evaluation at \(1\).
For instance \(\tau_{\mathbb Z}(x)=0\), whereas the specialization of \(x\) at \(1\) is \(1\).
Evaluation at one point is neither the canonical group trace nor a normal evaluation on \(L^\infty(\mathbb T^d)\).
Only the finite Laurent expressions and the explicitly certified rational expressions below are evaluated there.

For the group application, \(\mathcal A=\mathcal N(H)\), and the Fourier identification of the central direct factor is the actual group von Neumann tensor product.
If a separable Hilbert-space realization is wanted for direct-integral language, all finitely many coefficients under consideration lie in \(\mathbb CH_0\) for a finitely generated subgroup \(H_0\le H\).
Because \(\sigma\) fixes \(H\), the subgroup \(H_0\times\mathbb Z^d\rtimes\langle t\rangle\) is preserved.
Subgroup right-coset decomposition then transports the conclusions to \(H\) and \(G\), with the same canonical traces.

## Rational expressions and explicit polynomial Schur realizations

A rational expression in this section is a finite syntax built from bounded coefficient Laurent matrices by compatible sums, products, adjoints and inverses of square subexpressions.
Assume every inverse gate in that chosen syntax has an independently defined affiliated value at \(z=1\).
This is a condition on the supplied expression and its actual inverses.
There is no assumed homomorphism from the whole affiliated algebra to its specialization.

Every such expression \(E\), including a rectangular one, has a realization
\[
E=D-CL^{-1}B,
\tag{13}
\]
where \(D,C,L,B\) are finite Laurent matrices over the original bounded coefficient algebra and \(L(1)\) is an affiliated unit.
The following recursion proves this assertion and fixes all multiplication orders.

For a polynomial \(E\), take \(D=E\) and an empty \(L\)-block.
For a sum \(E_1+E_2\), use
\[
D=D_1+D_2,\quad
C=(C_1\ C_2),\quad
B=\binom{B_1}{B_2},\quad
L=\operatorname{diag}(L_1,L_2).
\tag{14}
\]
For a product \(E_1E_2\), use
\[
D=D_1D_2,\qquad
L=
\begin{pmatrix}
L_1&B_1C_2\\
0&L_2
\end{pmatrix},
\]
\[
C=(C_1\ \ D_1C_2),
\qquad
B=\binom{B_1D_2}{B_2}.
\tag{15}
\]
The inverse of this upper triangular \(L\) has upper-right block
\(-L_1^{-1}B_1C_2L_2^{-1}\).
Substituting it into (13) gives exactly
\((D_1-C_1L_1^{-1}B_1)(D_2-C_2L_2^{-1}B_2)\).
Its value \(L(1)\) is a unit because the diagonal values are units.
For the adjoint use
\[
D'=D^*,\quad C'=B^*,\quad L'=L^*,\quad B'=C^*.
\tag{16}
\]
Here the Laurent involution sends \(z_j\) to \(z_j^{-1}\), matching the torus adjoint.

Finally suppose a square \(E\) is inverted in the supplied syntax.
Form the polynomial block
\[
J=
\begin{pmatrix}
D&C\\
B&L
\end{pmatrix}.
\tag{17}
\]
At \(z=1\), the existing unit \(L(1)\) has Schur complement \(E(1)\), which is a unit by this inverse gate's premise.
The explicit block elimination
\[
\begin{pmatrix}I&-CL^{-1}\\0&I\end{pmatrix}
J
\begin{pmatrix}I&0\\-L^{-1}B&I\end{pmatrix}
=
\operatorname{diag}(E,L)
\tag{18}
\]
therefore proves \(J(1)\) is an affiliated unit without presupposing any generic inverse.
If \(E\) is \(k\)-square and \(U=\binom{I_k}{0}\), its inverse has the realization
\[
E^{-1}=U^*J^{-1}U
=0-(-U^*)J^{-1}U.
\tag{19}
\]
Thus the new denominator is the finite polynomial matrix \(J\), again with an independently certified affiliated value at \(1\).
The recursion uses no formal free-field rank factorization.

Apply (10)--(12) to each of the finitely many polynomial denominator blocks produced by this recursion.
Each is a unit for almost every fiber and a unit in the actual integrated affiliated algebra.
The identities (13)--(19), first in that algebra and also on the common conull set of good fibers, show that the selected rational expression is actually defined.
If the final square expression \(E(1)\) is also a unit, apply the final construction (17)--(19) even when the original syntax did not already invert it.
This proves
\[
\boxed{
\text{Every inverse gate is defined at }1,\quad
E(1)\in GL_k(\mathcal U(\mathcal A))
\ \Longrightarrow\
E\in GL_k(\mathcal U(\mathcal B)).
}
\tag{20}
\]

The domain statement here is substantive.
For a bounded polynomial denominator \(L\) with zero kernel, its affiliated inverse is the closed inverse on the dense range of \(L\).
In a Fourier direct-integral realization it is the maximal inverse field:
\[
\operatorname{Dom}(L^{-1})
=
\left\{\eta:
\begin{array}{l}
\eta(z)\in\operatorname{ran}L(z)\text{ for almost every }z,\\
z\mapsto L(z)^{-1}\eta(z)\text{ is measurable and square-integrable}
\end{array}
\right\}.
\tag{21}
\]
Every fiber inverse exists on its actual dense range outside the null exceptional set.
The bounded regularizations
\[
(L^*L+a^{-1}I)^{-1}L^*
\]
and their fiber versions identify the inverse on that range; their convergence there follows from the spectral theorem for \(L^*L\).
If the field on the right of (21) is square-integrable, bounded decomposability of \(L\) shows \(L(L(z)^{-1}\eta(z))=\eta\), proving the reverse domain inclusion.
Closed sums and products in (13)--(19) then have their actual affiliated meaning.
No assertion is made that an inverse acts on every Hilbert-space vector, and almost-everywhere invertibility supplies no uniform bounded inverse.

The source relationship is the same actual-domain Schur mechanism used in [L_A0006](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) and the [MSY23 polynomial-block supplement](../audits/literature/MSY23/Yin_U004.md#supplement-for-the-arbitrary-domain-aside-on-p-36).
The recursion above is supplied explicitly so that no undefined new denominator from an abstract rational identity is evaluated.
The underlying rank and eigenspace inputs are established source mechanisms; no historical novelty is claimed for rational linearization or the companion construction.

## Full row rank, the complete projection and compatible specialization

Return to the finite input \(M\).
The finite Laurent matrix \(L=MM^*\) has the unit value \(L_0\) at \(1\).
By (12), \(L\) is an actual affiliated unit in \(M_r(\mathcal U(N))\).
In particular \(\ker M^*=\ker(MM^*)=0\), so the closure of the range of \(M\) is all \(r\) row coordinates.
Rectangular polar decomposition gives
\[
\operatorname{rk}_N M=r,
\qquad
\dim_N\ker M=n-r.
\tag{22}
\]

The affiliated identity
\[
q=M^*(MM^*)^{-1}M
\]
is the initial support projection of \(M\).
For example, writing \(M=u|M|\) in rectangular polar decomposition, the full row support is \(uu^*=I_r\), and the displayed expression equals \(u^*u\).
Thus it is bounded, selfadjoint and idempotent.
Its complement \(p\) is exactly \(P_{\ker M}\), not merely a projection onto a selected subkernel.
All its entries belong to the actual rational closure of \(\mathbb CN\), because the single displayed matrix inverse has just been independently established.
Also \(\tau_n(q)=r\), giving (2).
No arithmetic assertion about any other coefficient matrix enters this computation.

At the specialization,
\[
p_0=I_n-M_0^*(M_0M_0^*)^{-1}M_0
\tag{23}
\]
is likewise the actual kernel projection of \(M_0\).
This holds even under the weaker affiliated-unit premise for \(L_0\).

The specialization
\[
\epsilon:\mathbb C[H\times\mathbb Z^d]\longrightarrow\mathbb CH,
\qquad
\epsilon(x_j)=1,\quad \epsilon(h)=h,
\]
commutes with \(\sigma\), because \(\sigma\) fixes every \(h\) and sends each auxiliary generator to a Laurent monomial.
Accordingly the chosen rational formula for \(\sigma(p)\) has a defined value at \(1\), and that value is \(p_0\).
Its inverse gates are those of \(\sigma(MM^*)\), whose value is exactly \(L_0\).
Therefore the rational expression \(W\) in (3) has all inverse gates defined at \(1\), and
\[
W(1)=p_0^3+(I_n-p_0)=I_n.
\tag{24}
\]
Apply (20) to obtain its actual affiliated inverse.

Since \(W\) is block diagonal for \(p\oplus(I_n-p)\), its \(p\)-block \(p\sigma(p)p\) is an affiliated corner unit.
Equivalently
\[
p\wedge(I_n-\sigma(p))=0.
\tag{25}
\]
The same specialization argument with \(\sigma^{-1}\) gives
\(p\sigma^{-1}(p)p+(I_n-p)\) as an affiliated unit.
One can instead infer the other kernel from finite-trace equality of the initial and final support of \(K\).
Both approaches are independent of a normality premise.

## The graded residual and complete finite kernel

The actual group \(G\) is torsion-free.
Indeed \(N\) is torsion-free, and a finite-order element of \(G\) has zero image in the infinite cyclic quotient and hence lies in \(N\).
The canonical subgroup trace extends the coefficient trace without changing the kernels or affiliated inverse certificates already obtained.
The height character supplies trace-preserving automorphisms \(\alpha_\theta\) fixing all coefficient matrices and sending \(t\) to \(e^{i\theta}t\).

On \(p\ell^2(G)^n\),
\[
KK^*=p\sigma(p)p,\qquad
K^*K=p\sigma^{-1}(p)p.
\tag{26}
\]
The units just proved therefore give \(\ker K=\ker K^*=\{0\}\).
If \(p=0\), the residual has an empty corner and the subsequent kernel calculation is immediate.
Otherwise \(pM_n(\mathcal N(G))p\), with its restricted finite faithful trace, is a legitimate finite corner.
Finite polar decomposition gives actual affiliated inverses of both \(K\) and \(K^*\).

Put \(C=pVp|_p\).
The ordered factorization is
\[
(K^*)^{-1}R_V
=p+(K^*)^{-1}C+(K^*)^{-1}K.
\tag{27}
\]
The three terms have heights \(0,1,2\), respectively, and the constant term is the corner identity \(p\).
The [one-sided graded companion theorem](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials), applied in this finite corner, makes (27) an affiliated unit.
Its proof permits the unbounded coefficients caused by \((K^*)^{-1}\).
Multiplication by the previously certified unit \(K^*\) proves that \(R_V\) is an affiliated unit.
Thus the residual is injective.

This residual implication is also the zero-defect case of the existing [coefficient-potential theorem](../claims/Yin_C_A0010_v2.md#statement).
It is not a new normal-hopping or potential principle.
The new information here is the central specialization certificate that makes the defect zero before either theorem is used.
The argument even permits a bounded coefficient \(V\) without selfadjointness, although the statement keeps \(V=V^*\) so that the final finite matrix is selfadjoint.

The complete kernel of the finite matrix in (5) follows from bounded equations alone.
If \(\mathcal H_V(\xi,\eta)=0\), the lower equation gives \(M^*M\xi=0\), hence \(\xi=p\xi\).
Applying \(p\) to the upper equation gives \(R_V\xi=0\), so \(\xi=0\).
The remaining upper equation is \(M^*M\eta=0\), hence \(\eta=p\eta\).
Conversely every \((0,p\eta)\) is in the kernel.
This proves the projection and dimension in (5), without applying a Gram support inverse to any vector.
The probability-normalized zero atom is \((n-r)/(2n)\).

## A nonnormal moving example with two unbounded inverse interfaces

Take \(d=3\), with central generators \(x_0,x_1,x_2\), and let \(\sigma\) cycle them in that order while fixing arbitrary \(H\).
Set \(r=1,n=2\) and
\[
M=(1+x_0)(-x_0\ \ 1)
=(-x_0-x_0^2\ \ 1+x_0).
\tag{28}
\]
At auxiliary identity,
\[
M_0=(-2\ \ 2),\qquad M_0M_0^*=8.
\]
The theorem applies independently of every matrix-kernel question over \(H\).
The scalar \(1+x_0\) is injective by its cyclic Fourier multiplier, so the complete kernel is the graph \((\xi,x_0\xi)\).
Its finite isometric frame and projection are
\[
F=\frac1{\sqrt2}\binom{1}{x_0},
\qquad
p=FF^*=\frac12
\begin{pmatrix}
1&x_0^{-1}\\
x_0&1
\end{pmatrix}.
\tag{29}
\]
This \(p\) has orbit exactly three.

The row Gram matrix is
\[
MM^*=2|1+x_0|^2.
\tag{30}
\]
It has no bounded inverse, since its continuous Fourier multiplier vanishes at \(x_0=-1\) and is arbitrarily small on sets of positive measure.
The supported part of \(M^*M\) has the same failure by rectangular polar decomposition.

The compressed forward coefficient is
\[
C=F^*\sigma(F)=\frac{1+x_0^{-1}x_1}{2},
\qquad F^*KF=Ct.
\]
Thus
\[
F^*KK^*F=h,\qquad
F^*K^*KF=\sigma^{-1}(h),
\]
\[
h=CC^*=\frac{2+x_0^{-1}x_1+x_1^{-1}x_0}{4},
\qquad
\sigma^{-1}(h)=
\frac{2+x_2^{-1}x_0+x_0^{-1}x_2}{4}.
\tag{31}
\]
The two Laurent polynomials are different, so \(K\) is not normal.
The function \(h\) is neither zero nor a projection.
Since \(F^*\sigma(p)F=h\), commutation of \(p,\sigma(p)\) would make \(h\) a projection, which is impossible.
Hence the orbit is genuinely noncommuting.

The multiplier \(C\) vanishes only when \(x_0^{-1}x_1=-1\), a Haar-null subtorus.
It is injective but has no bounded inverse.
Thus \(h\), and the \(p\)-block of \(W\), also have no bounded inverse.
Both the Gram and overlap inverses in this example are genuinely affiliated rather than bounded.
Nevertheless, for every selfadjoint finite \(V\in M_2(\mathbb C[H\times\mathbb Z^3])\), the four-square matrix \(\mathcal H_V\) has complete kernel \(\operatorname{diag}(0,p)\) and dimension one.
The example therefore verifies that the criterion is not restricted to normal hopping, stationary projections or globally bounded Gram inverses.

The auxiliary group \(\mathbb Z^3\rtimes_\sigma\mathbb Z\) is virtually abelian, with the index-three subgroup \(\mathbb Z^3\times3\mathbb Z\).
For arbitrary \(H\), its product with \(H\) is not thereby placed into a newly proved Atiyah class.
Only the displayed finite family is certified.

## Exact boundary relative to the retained obstruction

The construction in [C_A0011](../claims/Yin_C_A0011_v1.md#finite-group-ring-origin-of-the-complete-projection) fails the present specialization premise.
Its Fourier polynomial \(f=x_0-ix_1-x_2+ix_3\) satisfies \(f(1)=0\).
At auxiliary identity, all of the first \(m\) rows of its matrix \(M\) vanish.
The remaining \(r\) rows have the independently invertible block \(I_r+AA^*\), so the specialized row rank is \(r\), strictly less than the total \(m+r\).
Thus \(M_0M_0^*\) has a nonzero kernel, and its inverse gate cannot be evaluated at this specialization.
The rational unitary \(f(f^*)^{-1}\) likewise has no defined value there.
The new criterion does not turn that all-matrix obstruction into a positive theorem.

The finite star in [C_A0008](../claims/Yin_C_A0008_v1.md#specified-group-and-finite-regular-transport-input) uses \(N=H*F(z_1,\ldots,z_6)\), not a central direct product.
Its automorphism sends \(z_j\) to \(z_jw_j\).
Although the homomorphism sending \(z_j\) to \(1\) and fixing \(H\) exists on that free product, it does not commute with \(\sigma\) when some \(w_j\ne1\).
Indeed the two values on \(z_j\) would be \(w_j\) and \(1\).
Therefore its evaluated projection and the evaluation of its translate need not agree, and (24) is unavailable.
Its bounded Gram inverse alone never supplied that missing compatibility.
When all the twists are trivial, this particular obstruction disappears and the earlier star already has zero coefficient defect.

Central variables and compatible specialization do real work.
A single full-row evaluation is not asserted to control a free-variable family, a noncentral crossed-product parameter, or a projection whose translate has a different specialized value.
Likewise, no evaluation of an arbitrary measurable projection at one torus point is available.
The rational syntax and its independently defined inverse gates are part of the certificate.

The criterion says nothing about inputs whose specialized row Gram is singular, and it does not claim that every finite matrix can be moved into this class without changing its kernel.
A denominator that is generically invertible may still be undefined at \(1\), as C_A0011 demonstrates.
The certificate proves no uniform bounds for the inverses, no continuity of kernel projections at singular parameter values, and no equality between a point evaluation and the canonical trace.
The arithmetic in (5) comes from the actual full row support and the independently removed hopping defect.

## Source and verification scope

The finite-eigenprojection estimate is the existing [MSY23 Lemma 5.19 interface with its domain repair](../audits/literature/MSY23/Yin_U006.md#lemma-519-domain-repair).
The affine shift, companion Schur identity, countability of the exceptional sets on slices and Fubini step above are direct deductions at that interface.
The affiliated inverse and rank facts are the existing [MSY23 finite-trace foundations](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and [domain-aware rank lemma](../audits/literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof), used through the exact L_A0006 argument.
The rational recursion is an explicit actual-domain block realization, with the local MSY23 supplement cited at its stated scope.
No free-field embedding, maximal-\(\Delta\) hypothesis, inner-rank equality or coefficient division property is imported from that source.

The residual conclusion is the retained L_A0007 graded-companion certificate, alternatively the zero-defect case of C_A0010 v2.
L_A0007 already records its comparison with the established cyclic-extension rank mechanism.
The complete bounded-matrix kernel proof is the same direct residual-injectivity argument used in C_A0008 and C_A0011.
These source and mechanism attributions distinguish the new specialization application from known analytic foundations and older sufficient tests.
No external literature-wide novelty search, priority assertion, numerical proof or new whole-group Atiyah theorem is claimed.

## Assessment history

### Decision reviewed-compatible-specialization

| Field | Value |
| --- | --- |
| date | 2026-11-11T18:39 |
| status | proved |
| reason | Independent whole-proof review supports central-variable specialization with actual affiliated inverse gates, zero overlap defects, the graded residual and complete finite kernel, including the weaker affiliated-unit specialization premise. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Compatible central-variable specialization, full row rank, bounded rational projection, zero hopping defects and complete finite-matrix kernel for every stated coefficient potential. |
| argument | [Argument](#argument) | Companion and rational Schur constructions, measurable fibers and integrated domains, exact trace, nonnormal example, source uses and excluded encodings. |
| review | [Independent whole-argument finding](../audits/reviews/Yin_R_A0038_v1.md#whole-argument-finding) | Entire fixed statement and argument, exact inverse and source interfaces, all parameter and comparison cases. |

## Current assessment

[Selected decision](#decision-reviewed-compatible-specialization)

