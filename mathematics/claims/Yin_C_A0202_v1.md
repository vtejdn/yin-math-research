---
author: Yin
---

# Finite phase bounds for group-ring matrices supported on longer words

## Statement

Let \(G=\langle s,t\rangle\) be discrete, and fix simple two-point unitary spectra \(a\pm b,\ c\pm d\) with \(bd\ne0\).
Use the [two-generator normal form](Yin_C_A0194_v1.md#normal-form-for-a-pair-of-unitary-matrices)
\[
 S=aI+bJ_0,\quad T(z)=cI+dJ_z,\quad
 J_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 J_z=\begin{pmatrix}0&z^{-1}\\z&0\end{pmatrix}.
\]
Let \(\mathcal Z\) be the phases on the circle at which \(s\mapsto S,\ t\mapsto T(z)\) is an actual representation of \(G\).
The set is closed under inversion by coordinate exchange.
In the finite case put \(k=|\mathcal Z|>0\).
Consider any \(h\)-by-\(h\) matrix \(X=\sum_g X_g g\) over \(\mathbb CG\) and let \(\delta\) be its regular nullity using unnormalized matrix trace.
For each occupied \(g\), choose a word \(w_g\) representing it and form the Laurent matrix on \(2h\) coordinates
\[
              A(z)=\sum_g w_g(S,T(z))\otimes X_g g .
\]
Each term retains its original group translation.
The two formal inverses of the generator matrices have Laurent entries because both determinants are nonzero constants.

1. Multiply rows and columns of \(A(z)\) by integral powers of \(z\) to obtain a polynomial matrix \(Q(z)\), with column degrees bounded by \(d_j\ge0\).
   If \(Q(z_0)\) is injective at some \(z_0\in\mathbb C\), then
   \[
                   2k\delta\le\sum_{j=1}^{2h}\min(k,d_j).
   \]
   A group-ring unit as the constant matrix suffices.
   Columns of width zero cost nothing, including coordinates added as a separate identity block.
   Infinitely many allowed phases imply \(\delta=0\) under the same injectivity assumption.
2. Suppose \(Q(z)=\sum_{j=0}^{w}Q_j z^j\), \(w\ge1\), is obtained in this way and \(Q_j=JQ_{w-j}J\), where \(J\) exchanges the two auxiliary blocks.
   Suppose \(Q_0\) is invertible over \(\mathbb CG\).
   Then \(\delta\le hw/k\), and if all nonzero group-ring scalars act injectively and \(0<\delta<1\), then
   \[
                         \delta\le (hw-1)/k.
   \]
   Both ends and the reciprocity condition are checkable on the finitely many coefficients.

The width tests depend on the supplied words and gauges.
Only the evaluations at the allowed phases must represent \(G\); a favorable word choice suffices.
The [relator test](Yin_C_A0195_v1.md#statement) determines which phases are allowed for a finite presentation, independently of the chosen input matrix.
Inclusions of the marked subgroup in a larger group preserve the regular ranks by the right-coset decomposition.

## Column widths and interpolation

At every allowed \(z\), the absorbed unitary twist of \(X\) has nullity \(2\delta\).
The absorbing unitary operates separately on each group fiber and equals the identity on the identity fiber, as in the [regular trace calculation](Yin_C_A0194_v1.md#normal-form-for-a-pair-of-unitary-matrices).
The row and column monomials are invertible complex coordinate matrices at these phases and preserve this dimension.
For a given integer weight on each row, strip the least exponent from each nonzero column to use its remaining exponent range as \(d_j\).
A column that is identically zero is incompatible with the full-rank evaluation assumption.

Take any finite set of \(k\) allowed phases.
In column \(j\) use input polynomials of degree strictly less than \((k-d_j)_+\), with coefficients in \(\ell^2(G)\).
Every component of their product by \(Q(z)\) has degree less than \(k\).
Multiplication is injective on this polynomial input: in a nonzero input's expansion at \(z_0\), the first nonzero vector coefficient is sent by \(Q(z_0)\) to a nonzero vector coefficient of the product.
Evaluation of the output at the \(k\) distinct phases is still injective by the scalar Vandermonde matrix.
These operations are bounded equivariant maps between finite coordinate Hilbert modules; their image lands in the sum of the closed ranges of the \(k\) evaluations, each of dimension \(2h-2\delta\).
Thus
\[
           \sum_j(k-d_j)_+\le k(2h-2\delta).
\]
This gives the stated bound and, by arbitrarily large finite subsets, the conclusion with infinitely many phases.
This is the unequal-column-degree version of the [finite evaluation argument](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration).

## Reciprocal coefficients and the companion involution

The identity \(A(z^{-1})=J A(z)J\) holds formally on all Laurent words.
For instance, if the row weights on each exchanged pair sum to the same \(\rho\), and all column pairs have sum \(\gamma\), the gauged matrix satisfies \(Q(z^{-1})=z^{-\rho-\gamma}JQ(z)J\).
When \(Q\) is polynomial and \(\rho+\gamma=w\), this gives the stated coefficient reciprocity.
By the endpoint assumption \(Q_w=JQ_0J\) is also a group-ring unit.

Use the monic companion \(L\in M_{2hw}(\mathbb CG)\) with identity superdiagonal blocks and last row
\[
                    -Q_w^{-1}Q_0,\ldots,-Q_w^{-1}Q_{w-1}.
\]
Over the affiliated algebra its eigenspace at \(z\) identifies with \(\ker Q(z)\) via the vector \((v,zv,\ldots,z^{w-1}v)\).
Define \(W(x_0,\ldots,x_{w-1})=(Jx_{w-1},\ldots,Jx_0)\).
Conjugating \(L\) by \(W\) produces the identity subdiagonal and first row
\[
                    -Q_0^{-1}Q_1,\ldots,-Q_0^{-1}Q_w .
\]
These are exactly the blocks of \(L^{-1}\), obtained by solving the companion equations starting with the constant coefficient.
In particular \(L,L^{-1}\) belong to the matrix group ring, and reciprocity survives the ordered left normalization.

For finite \(\mathcal Z\), let \(p(x)=\prod_{z\in\mathcal Z}(x-z)\).
The distinct eigenspaces form the kernel of \(p(L)\) as an algebraic direct sum over affiliated modules, by scalar interpolation on its kernel.
Hence the image of \(p(L)\) has dimension \(2hw-2k\delta\).
This proves the first bound.
If scalar injectivity holds and \(0<\delta<1\), there is no nonzero finite-support eigenvector of \(L\) at an allowed phase.
Indeed the first block of such a vector gives a nonzero finite-support vector in \(\ker Q(z)\).
Undoing the gauge on that input and the absorption on the group fibers preserves finite support and puts it in two copies of \(\ker X\).
A nonzero component there has a nonzero group-ring coordinate and would generate an affiliated submodule of dimension one, contradicting \(\delta<1\).

No scalar polynomial then annihilates \(L\).
Otherwise the primary polynomial idempotent of an allowed eigenvalue, followed by the highest nonvanishing power of \(L-z\) on that primary summand, produces a nonzero group-ring matrix whose columns are finite-support eigenvectors.
This also uses \(\delta>0\), to guarantee a nonzero primary summand.
The image of \(p(L)\) is preserved by \(L^{\pm1}\) and by \(W\), since \(p(L^{-1})\) is a nonzero scalar times \(L^{-k}p(L)\).
Its two \(W\)-sign subspaces are the images of the group-ring matrices \((I\pm W)p(L)/2\).
Any nonzero such image has dimension at least one, using a nonzero group-ring entry.
If the total image dimension were below two, \(W\) would act as a scalar sign there.
Then \(WLW=L^{-1}\) would give \((L^2-I)p(L)=0\), the forbidden polynomial identity.
This gives the sharper bound.
The proof extends the [degree-one swap](Yin_C_A0200_v1.md#the-action-of-the-block-swap-on-the-remaining-image) to all reciprocal degrees by reversing the companion coordinates.

## A long mixed Schur family on the perfect marking

Use the [torsion-free perfect group and marking](Yin_C_A0194_v1.md#an-explicit-perfect-marking) indexed by \(n\ge0\), with the prescribed \(S=iJ_0,\ T(z)=I/2+i\sqrt3 J_z/2\).
It has \(8(n+1)\) allowed phases by the [exact count](Yin_C_A0195_v1.md#statement).
For any \(r\ge1\) take
\[
          X=G_+(st)^r+G_-(st)^{-r}+Y,\qquad
          G_+,G_-\in{\rm GL}_h(\mathbb C).
\]
The entries of \(Y\) may be arbitrary finite linear combinations of words that each contain fewer than \(r\) syllables \(t^j\), after grouping consecutive powers of the individual generators.
The integer exponents in all syllables are unrestricted.
Indeed \(T(z)^j=c_j I+d_j J_z\) for positive and negative integers \(j\), and \(S^i\) is constant, so every formal entry from \(Y\) has exponents strictly between \(-r\) and \(r\).

The two other terms have exactly the required opposite extreme blocks.
In fact
\[
 ST(z)=\tfrac{i}{2}J_0-\tfrac{\sqrt3}{2}\operatorname{diag}(z,z^{-1}),
 \qquad T(z)^{-1}S^{-1}=-\tfrac{i}{2}J_0-\tfrac{\sqrt3}{2}\operatorname{diag}(z^{-1},z).
\]
In the \(r\)-th power the coefficient at either extreme exponent comes only from taking the corresponding diagonal term \(r\) times.
Thus \(Q(z)=z^r A(z)\) is reciprocal of degree \(2r\).
Its constant and top matrices are block diagonal, with the two diagonal blocks equal, in opposite orders, to \((-\sqrt3/2)^rG_-(st)^{-r}\) and \((-\sqrt3/2)^rG_+(st)^r\).
They are group-ring units.
The unrestricted entries of \(Y\) therefore give
\[
                        \dim_G\ker X\le \frac{hr}{4(n+1)} .
\]

For an explicit two-by-two Schur scalar let \(r=2\), \(L=(st)^2+(st)^{-2}\), and take
\[
             X=\begin{pmatrix}1-t&L+u\\L+v&d_0\end{pmatrix}.
\]
Here \(u,v,d_0\) are independent group-ring sums of words with at most one \(t\)-syllable as above.
Take \(G_+=G_-=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).
The marking has \(t^3\) of infinite order, so \(1-t\) is an affiliated unit by the bilateral shift on its cyclic subgroup.
Schur elimination identifies the nullity of \(X\) with that of
\[
              d_0-(L+v)(1-t)^{-1}(L+u).
\]
Consequently for \(n=2\) its nullity is at most \(1/3\), without a scalar injectivity assumption.
The three independent perturbations may use arbitrarily many group elements and arbitrarily long powers, in the original regular representation.
The proof does not decide whether a smaller positive nullity occurs, or supply a full-rank evaluation for every possible word matrix.
