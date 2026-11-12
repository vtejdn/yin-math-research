---
author: Yin
---
# Polynomial kernel normalization and actual amalgamated boundary certificates

Date: 2026-11-12 (Asia/Hong_Kong).
This development serves [S_A0005](../strategies/Yin_S_A0005.md) and the bounded discriminator in [the seven-route assessment](../ledger/Yin_L_A0018_v1.md#amalgamated-atom-transport).
It constructs an actual indefinite two-vertex group-ring matrix with a non-bottom zero atom, uniformly invertible expected kernel and nonzero actual subordination boundary values.
It then isolates a finite polynomial kernel certificate that recovers those boundary values in the actual cyclic rational matrix ring, without requiring rationality of the full expected kernel.
An additional polynomial congruence now normalizes every full-support expected Gram of a displayed finite kernel witness to a uniformly positive one, using the principal ideal domain structure of the cyclic group ring.
The four-path example is covered by an explicit finite-tree unitary gauge and cyclic vertex blocks; it supplies no new group class.
The general certificate requires displayed polynomial kernel columns whose expected Gram has full support; it asserts no such witness for arbitrary group-ring kernels.

## Statement

Let \(G=G_1*_H G_2\) be an actual amalgamated product, with \(H\cong\mathbb Z\), and let \(B=\mathcal N(H)\).
Use the coefficient-extracting canonical conditional expectation \(E_H:\mathcal N(G)\to B\), extended entrywise to \(E^{(n)}\).
All analytic ranks and nullities use the unnormalized matrix trace.
For a bounded selfadjoint \(Y\), write \(p=1_{\{0\}}(Y)\) and \(\nu_n(Y)=(\operatorname{Tr}_n\otimes\tau_G)(p)\).
For selfadjoint \(Y_j\in M_n(\mathbb CG_j)\), the two vertex algebras are free over \(M_n(B)\) in the matrix amplification, by the reduced-word and entrywise argument already retained in [L_A0014](../ledger/Yin_L_A0014_v1.md#setting-and-accepted-interfaces).

The accepted [BBL21 general-base interface](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), with the kernel inclusion checked in [R_A0014](../audits/reviews/Yin_R_A0014_v1.md#nonrationality-and-boundary-values), has the following precise use.
If \(Y=Y_1+Y_2\) and \(\xi=E^{(n)}(p)\) has a bounded inverse, the actual selfadjoint subordination boundary limits \(b_j\in M_n(B)\) satisfy
\[
b_1+b_2=0,\qquad
p\le p_{\ker(Y_j-b_j)},
\qquad
\nu_n(Y_1-b_1)+\nu_n(Y_2-b_2)=n+\nu_n(Y).
\tag{1}
\]
The analytic existence and boundary-limit theorem remain accepted external inputs at their recorded scope.
In particular, a full support for \(\xi\) without a bounded inverse does not justify (1).
The formulas below determine these actual limits using (1); merely finding matrices with a compatible kernel is not being substituted for the subordination theorem.

Suppose \(W\in M_{n,k}(\mathbb CG)\), \(k\ge1\), satisfies \(YW=0\), and put \(C=E^{(n)}(WW^*)\) and \(N_j=E^{(n)}(Y_jWW^*)\).
If \(\xi\) has a bounded inverse and \(C\) has full support, then the actual boundary values satisfy \(b_j=N_jC^{-1}\in M_n(\mathbb C(H))\).
The stronger finite-witness condition \(C\ge\varepsilon I_n\), \(\varepsilon>0\), independently supplies both analytic premises.
If both torsion-free vertex groups satisfy complex Atiyah, either variant implies \(\nu_n(Y)\in\mathbb Z\), using their already known actual division closures.
More generally, full support of \(C\) alone supplies a finite matrix \(D\in M_n(\mathbb CH)\), independently invertible in the actual affiliated algebra, and \(W_0\in M_{n,k}(\mathbb CG)\) such that \(W=DW_0\) and \(E^{(n)}(W_0W_0^*)\ge\varepsilon I_n\).
The selfadjoint finite vertex matrices \(Y'_j=D^*Y_jD\) satisfy \((Y'_1+Y'_2)W_0=0\) and preserve the original nullity.
Applying the preceding certificate to this normalized sum proves \(\nu_n(Y)\in\mathbb Z\) under the same known vertex hypotheses, without separately assuming a bounded inverse of the original \(\xi\).
The normalized boundary values are actual cyclic rational matrices; no existence or boundedness of the original boundary values is inferred when the original expected kernel is degenerate.
The polynomial normalization has a specific two-variable counterexample below, and no conclusion for arbitrary edge coefficient rings is asserted.
No assertion that such polynomial kernel columns always exist is included.
The displayed indefinite four-path model has a non-bottom zero atom, boundedly invertible expected kernel, and nonzero nonscalar actual boundary values \(b_1=B_0\), \(b_2=-B_0\); its nullities are \(1,2,3\) as detailed below.

## Argument

### An indefinite four-path model

Use the central cyclic amalgam
\[
G=\langle u,a\mid[u,a]=1\rangle*_{\langle u\rangle}
  \langle u,b\mid[u,b]=1\rangle
  \cong\mathbb Z\times F(a,b).
\]
Set
\[
\lambda=\frac{\sqrt5-1}{2},\qquad
\lambda^2+\lambda=1,
\qquad
B_0=\operatorname{diag}(0,1,1,0).
\]
Define actual finite group-ring matrices
\[
Y_1=\begin{pmatrix}
-\lambda&a&0&0\\
a^{-1}&-\lambda&0&0\\
0&0&-\lambda&a\\
0&0&a^{-1}&-\lambda
\end{pmatrix},\qquad
Y_2=\begin{pmatrix}
0&0&0&0\\
0&0&b&0\\
0&b^{-1}&0&0\\
0&0&0&0
\end{pmatrix},\qquad Y=Y_1+Y_2.
\tag{2}
\]
Both summands are selfadjoint and belong to their respective vertex group rings.
The first has spectrum \(\{-1-\lambda,1-\lambda\}\), and the second has spectrum \(\{-1,0,1\}\), so each is indefinite.
Their entries are affine in the indicated group generators, with complex scalar constants.

Let
\[
d_1=1,\quad d_2=a^{-1},\quad d_3=b^{-1}a^{-1},\quad
d_4=a^{-1}b^{-1}a^{-1},\qquad U=\operatorname{diag}(d_1,d_2,d_3,d_4).
\]
For the ordinary four-vertex path adjacency matrix \(J\), direct multiplication gives
\[
Y=U(J-\lambda I_4)U^*.
\tag{3}
\]
Indeed \(d_1d_2^*=a\), \(d_2d_3^*=b\), and \(d_3d_4^*=a\).
This finite tree gauge is written explicitly and uses no Atiyah conclusion.
The characteristic polynomial of \(J\) is \(x^4-3x^2+1\), with roots \(\pm\lambda,\pm(1+\lambda)\).
Thus the spectrum of \(J-\lambda I_4\) is
\[
\{1,0,-2\lambda,-(1+2\lambda)\},
\]
and its zero eigenvalue is simple and lies strictly between negative and positive eigenvalues.
This is a non-bottom atom, not a positive zero-atom model.

Put
\[
v=(1,\lambda,-\lambda,-1)^t,
\quad c=v^*v=2(1+\lambda^2),
\quad
W=Uv=\begin{pmatrix}
1\\ \lambda a^{-1}\\-\lambda b^{-1}a^{-1}\\-a^{-1}b^{-1}a^{-1}
\end{pmatrix}.
\tag{4}
\]
Then \(YW=0\), \(W^*W=cI\), and (3) gives the exact kernel projection
\[
p=\frac1cWW^*,\qquad \nu_4(Y)=1.
\tag{5}
\]
The four words \(d_i\) are distinct reduced free-group words.
For \(i\ne j\), the nontrivial free-group word \(d_i d_j^{-1}\) does not belong to the central subgroup \(\langle u\rangle\), so conditional expectation kills every off-diagonal entry of \(p\).
Consequently
\[
\xi=E^{(4)}(p)
 =\frac1{2(1+\lambda^2)}\operatorname{diag}(1,\lambda^2,\lambda^2,1)
 \ge\frac{\lambda^2}{2(1+\lambda^2)}I_4.
\tag{6}
\]
This verifies the actual bounded-inverse hypothesis in (1) before invoking subordination.

Direct multiplication, using \(1-\lambda^2=\lambda\), gives
\[
Y_1W=B_0W,\qquad Y_2W=-B_0W.
\tag{7}
\]
Neither vector on the right is zero, so the summands do not separately annihilate the total kernel.
For the actual boundary values from (1), the kernel inclusion gives \(Y_jp=b_jp\).
Equations (5) and (7) therefore imply
\[
(b_1-B_0)p=0,\qquad (b_2+B_0)p=0.
\]
Taking conditional expectation and using its bimodularity gives
\((b_1-B_0)\xi=(b_2+B_0)\xi=0\).
The independently established inverse in (6) proves the exact actual boundary values
\[
\boxed{b_1=B_0,\qquad b_2=-B_0.}
\tag{8}
\]
The matrix \(B_0\) is nonzero and nonscalar.

The two diagonal two-square blocks of \(Y_1-B_0\) are
\[
\begin{pmatrix}-\lambda&a\\a^{-1}&-\lambda-1\end{pmatrix},\qquad
\begin{pmatrix}-\lambda-1&a\\a^{-1}&-\lambda\end{pmatrix}.
\]
Each is unitarily equivalent, using only a diagonal group unitary, to a constant two-square matrix with determinant \(\lambda(1+\lambda)-1=0\) and nonzero trace \(-1-2\lambda\).
Each therefore has analytic rank one and nullity one.
The only nonzero block of \(Y_2+B_0\) is
\(\left(\begin{smallmatrix}1&b\\b^{-1}&1\end{smallmatrix}\right)\), which is unitarily equivalent to the constant all-ones matrix and has rank one.
The remaining two zero coordinates contribute two more kernel dimensions.
Hence
\[
\nu_4(Y_1-b_1)=2,\qquad
\nu_4(Y_2-b_2)=3,\qquad
2+3=4+1.
\tag{9}
\]
The vertex nullities and the total nullity have independent finite-matrix certificates, not an application of the whole group's Atiyah theorem.

The total operator in (3) is indefinite, so it cannot be the sum of two positive operators after cancelling opposite base shifts.
In particular this is not the preceding positive three-square model with opposite base shifts added to its summands.
Nevertheless the explicit tree gauge and cyclic two-square vertex reductions fully explain this success.
The example resolves the requested nonzero-boundary pilot without providing a new analytic mechanism outside those known reductions.

### Recovery from polynomial kernel columns

There is a useful algebraic interface that does not require the entire kernel projection or its expectation to be rational.
Retain the actual cyclic amalgam setting and the bounded selfadjoint sum \(Y=Y_1+Y_2\).
Suppose a finite matrix \(W\in M_{n,k}(\mathbb CG)\), with \(k\ge1\), is explicitly given and satisfies
\[
YW=0.
\]
It need not parametrize the entire kernel, and its columns need not be analytically independent.
Set
\[
C=E^{(n)}(WW^*),\qquad N_j=E^{(n)}(Y_jWW^*).
\tag{10}
\]
Both matrices belong to \(M_n(\mathbb CH)\).
Indeed the products before expectation are finite matrices over \(\mathbb CG\), and the canonical expectation retains exactly their finitely many coefficients whose group labels lie in \(H\).
This is a finite coefficient calculation in the specified actual group; no uniform word-problem algorithm is asserted.

First assume separately that \(\xi=E^{(n)}(p)\) has a bounded inverse, so (1) applies, and that \(C\) has full support.
Because \(pW=W\), the kernel inclusion in (1) gives
\[
Y_jW=b_jW,\qquad b_j C=N_j.
\tag{11}
\]
The second equality uses bimodularity, in precisely the displayed order.
The positive full-support matrix \(C\in M_n(\mathbb CH)\) has an actual affiliated inverse in \(M_n(\mathcal U(H))\).
For \(H\cong\mathbb Z\), the [actual cyclic rational field](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) puts this inverse in \(M_n(\mathbb C(H))\).
For completeness, a zero Laurent determinant would give a nonzero rational kernel column and contradict full support, while a nonzero determinant gives the usual adjugate inverse in the actual cyclic field.
Thus
\[
\boxed{b_j=N_jC^{-1}\in M_n(\mathbb C(H)).}
\tag{12}
\]
This equality is in the actual affiliated algebra, and its left side is bounded by the accepted subordination theorem.
No boundedness of \(C^{-1}\) is required in this first variant, and no assertion about pointwise action of an unbounded inverse on all Hilbert vectors is used.
In particular, neither \(p\) nor \(\xi\) is assumed to belong to the group ring or its rational closure.

A stronger expected-Gram hypothesis supplies the missing subordination hypothesis automatically.
If the displayed polynomial columns satisfy
\[
C\ge\varepsilon I_n\qquad(\varepsilon>0),
\tag{13}
\]
then their range lies in the kernel of \(Y\), so
\[
0\le WW^*\le\|W\|^2 p.
\]
Conditional expectation preserves this order, giving
\[
\xi\ge\frac{C}{\|W\|^2}
     \ge\frac{\varepsilon}{\|W\|^2}I_n.
\tag{14}
\]
The matrix \(W\) is nonzero by (13), so the denominator is positive.
Equations (1) and (12) are therefore justified directly from the finite kernel witness and (13), without knowing the complete kernel in advance.
This condition is stronger than full support of \(C\); that distinction is essential in a diffuse base.

If instead \(W\) spans the whole kernel in the sense that the support of \(WW^*\) equals \(p\), then full support of \(\xi\) implies full support of \(C\), but still gives no bounded lower bound.
Indeed, for a kernel projection \(q\) of \(C\), faithfulness applied to \(qWW^*q\) gives \(pq=0\), hence \(q\xi q=0\).
Full support of \(\xi\) forces \(q=0\).
This observation does not remove the bounded-inverse premise for (1).
The earlier \(\mathbb Z^2\) example in [L_A0013](../ledger/Yin_L_A0013_v1.md#full-support-does-not-supply-a-bounded-inverse-even-for-a-group-ring-matrix) has the full polynomial kernel column \(W=(v,-(u-1))^t\), with \(C=\operatorname{diag}(1,|u-1|^2)\); both \(C\) and \(\xi\) have full support and neither has a bounded inverse.

The four-path example satisfies the stronger certificate with
\[
C=\operatorname{diag}(1,\lambda^2,\lambda^2,1),\qquad
N_1=B_0C,\qquad N_2=-B_0C.
\]
Formula (12) recovers (8) directly.

### Polynomial normalization over the cyclic edge

Write \(R=\mathbb C[z,z^{-1}]=\mathbb CH\) and \(K=\mathbb C(z)\), with \(z\) the actual infinite-order generator of \(H\).
For the given finite matrix \(W\), choose distinct cosets \(Hu_1,\ldots,Hu_s\) meeting its support and write
\[
W=\sum_{\alpha=1}^{s} F_\alpha u_\alpha,
\qquad F_\alpha\in M_{n,k}(R),
\qquad F=[F_1\ \cdots\ F_s]\in M_{n,ks}(R).
\tag{N1}
\]
The representatives denote actual group unitaries, acting identically on the matrix coordinates.
Coefficients are on the left; no normality or centrality of \(H\) is needed.
For distinct representatives, \(u_\alpha u_\beta^{-1}\notin H\), so bimodularity and coefficient extraction give
\[
C=E^{(n)}(WW^*)=\sum_\alpha F_\alpha F_\alpha^*=FF^*.
\tag{N2}
\]
If \(C\) has full support, its Laurent determinant is nonzero by the earlier cyclic-field argument.
Consequently \(F\) has row rank \(n\) over \(K\).

The ring \(R\) is a principal ideal domain: \(\mathbb C[z]\) is Euclidean, and localization at powers of \(z\) preserves principality by contracting an ideal and then localizing it again.
Let \(M\subset R^n\) be the submodule generated by the columns of \(F\).
It is free of rank \(n\).
For completeness, the free-submodule assertion follows by induction on the number of coordinates.
The image of the first-coordinate projection of a submodule is an ideal \((d)\).
If this ideal vanishes, use the remaining coordinates; otherwise choose a vector whose first coordinate is \(d\), subtract its appropriate multiples from every other vector, and split off its free cyclic summand.
The zero-first-coordinate submodule is handled inductively, and tensoring with \(K\) identifies the resulting number of basis vectors with the field rank.
This proves the exact finite-rank assertion needed here without assuming that \(M\) is a direct summand of \(R^n\).

Choose a basis of \(M\), and let \(D\in M_n(R)\) have those basis vectors as columns.
Expressing the columns of \(F\) in that basis, and the basis in the original generators, gives matrices
\[
F_0\in M_{n,ks}(R),\qquad S\in M_{ks,n}(R),
\qquad F=DF_0,\qquad D=FS.
\]
The columns of \(D\) are linearly independent over \(K\), so \(\det D\ne0\).
Canceling \(D\) over \(K\) yields the polynomial right inverse
\[
F_0S=I_n.
\tag{N3}
\]
The matrix \(D\) need not be unimodular over \(R\).
Its nonzero Laurent determinant nevertheless gives \(D^{-1}\in M_n(K)\) in the actual affiliated algebra, independently of all unknown group-matrix ranks.
The same actual inverse embeds in both vertex algebras and in the amalgam by the subgroup representation.

Partition \(F_0=[F_{0,1}\ \cdots\ F_{0,s}]\) into the original block sizes and put
\[
W_0=\sum_\alpha F_{0,\alpha}u_\alpha\in M_{n,k}(\mathbb CG).
\]
Then \(W=DW_0\) as a finite group-ring identity.
All entries of \(S\) are bounded cyclic group-ring operators, so (N3) implies
\[
C_0:=E^{(n)}(W_0W_0^*)=F_0F_0^*
\ge\|S\|^{-2}I_n.
\tag{N4}
\]
Indeed \(S^*F_0^*=I_n\) gives \(\|\zeta\|\le\|S\|\|F_0^*\zeta\|\) for every Hilbert vector \(\zeta\).
The norm \(\|S\|\) is positive because (N3) is an identity.
This proves a uniform lower bound and not merely full support.

Set
\[
Y'_j=D^*Y_jD\in M_n(\mathbb CG_j),\qquad
Y'=Y'_1+Y'_2=D^*YD.
\tag{N5}
\]
Each summand is bounded and selfadjoint, and
\[
Y'W_0=D^*YW=0.
\]
The bounded-witness estimate (14), now applied to \(W_0\), makes \(E^{(n)}(p_{\ker Y'})\) boundedly invertible.
The BBL21 theorem therefore applies to the actual normalized sum and supplies actual bounded selfadjoint boundary values \(b'_j\).
The preceding recovery argument gives
\[
b'_j=E^{(n)}(Y'_jW_0W_0^*)C_0^{-1}\in M_n(K).
\tag{N6}
\]
Finally, \(D\) and \(D^*\) are actual affiliated units, so
\[
\nu_n(Y')=\nu_n(Y).
\tag{N7}
\]
This is affiliated rank invariance for the two bounded matrices, not a pointwise claim that the potentially unbounded \(D^{-1}\) maps every Hilbert vector to a Hilbert vector.
Neither the full kernel projection nor its original expectation was inverted during this construction.
The original expectation need have no bounded inverse; the analytic theorem is used only after normalization in that case.

If instead \(F\) has field rank \(0<r<n\), this method supplies only a corner bound.
The classical Smith reduction gives unimodular Laurent matrices \(U,V\) with \(UFV\) rectangular diagonal, having nonzero entries \(d_1,\ldots,d_r\) and all remaining entries zero.
Take \(D=U^{-1}\operatorname{diag}(d_1,\ldots,d_r,1,\ldots,1)\), which is again an actual affiliated unit.
Writing \(J\) for the rectangular diagonal matrix with \(r\) ones and otherwise zeros gives \(F_0=D^{-1}F=JV^{-1}\), hence
\[
\operatorname{supp}(F_0F_0^*)=q:=\operatorname{diag}(I_r,0),
\qquad F_0F_0^*\ge\|V\|^{-2}q.
\tag{N9}
\]
The zero-rank case has \(F=0\) and no nonzero witness.
No invertible square cyclic factor can turn a rank-deficient expected Gram into a full-support one, because its affiliated rank is preserved.
Additional kernel columns might enlarge that support, but their existence is separate information.
Compression of the normalized matrix to \(q\) requires a new kernel calculation and trace corrections; deleting output coordinates can introduce kernels, so (N9) is not a full-size BBL21 premise or a formula for the original nullity.

### Conditional reduction to the known vertex ranks

Assume now that both torsion-free vertex groups have the known complex Atiyah property, so their actual rational closures \(D_j\subset\mathcal U(G_j)\) are division rings.
Suppose either the first variant's two separate analytic premises hold or the finite kernel witness satisfies the stronger condition (13).
Then \(\mathbb C(H)\subset D_j\) under the actual subgroup embedding, and (12) puts
\[
Y_j-b_j\in M_n(D_j).
\]
The subgroup embeddings and trace/rank preservation use the right-coset decomposition retained in [Lin93's source account](../audits/literature/Lin93/Yin_U001.md#ring-lemmas-and-the-extension-argument).
Only that subgroup interface is used here, not a finite-index hypothesis.
Equivalently, all cyclic denominators in (12) remain the same actual units in each vertex and in the amalgam.

Gaussian elimination over the already known actual division ring \(D_j\) uses only actual affiliated units and yields an analytic rank \(r_j\in\{0,\ldots,n\}\).
Therefore \(\nu_n(Y_j-b_j)=n-r_j\) is independently an integer.
The source identity (1) gives
\[
\boxed{\nu_n(Y)=n-r_1-r_2\in\mathbb Z.}
\tag{15}
\]
This is a sufficient certificate for the displayed additive matrix, not a proof that every additive matrix admits suitable polynomial kernel columns.
If only full support of \(C\) was initially known, apply this same vertex-rank argument to the normalized matrices (N5) and their actual values (N6), then use (N7).
Thus full support of the displayed polynomial witness Gram suffices for integer nullity, without a separate bounded-inverse premise on the original expected kernel.
The total kernel is nonzero under (13), since the displayed nonzero \(W\) lies in it.
No hypothesis that the whole amalgam already has the Atiyah property is used.
The argument is valid for a noncentral cyclic edge as well: coefficient extraction, bimodularity and the actual cyclic-field inclusion do not require centrality.
The worked example, however, remains central and is already covered by known group results.

### Why the same polynomial repair fails for a two-variable edge

The principal ideal domain input is a substantive restriction of the normalization.
Let \(H_2=\langle x,y\mid[x,y]=1\rangle\cong\mathbb Z^2\), let \(G_{\mathrm{ex}}=H_2\times\langle s\rangle\), and take the one-entry finite group-ring witness
\[
W=(x-1)+(y-1)s.
\tag{N8}
\]
For the coefficient expectation onto \(H_2\),
\[
C=E_{H_2}(WW^*)=|x-1|^2+|y-1|^2
\]
has full support: its torus symbol vanishes only at \((1,1)\), a Haar-null set.
Its continuous symbol approaches zero there, so it has no strictly positive lower bound.
Suppose a same-size polynomial factorization \(W=dW_0\), with nonzero \(d\in\mathbb C[x^{\pm1},y^{\pm1}]\) and finite \(W_0\in\mathbb CG_{\mathrm{ex}}\), were to give a uniformly positive expected Gram for \(W_0\).
Comparing the distinct cosets \(H_2s^j\) forces \(d\) to divide both \(x-1\) and \(y-1\) in the Laurent ring.
The element \(x-1\) is prime because its quotient ring is \(\mathbb C[y^{\pm1}]\), and it does not divide \(y-1\), as evaluation at \(x=1\) shows.
Any common divisor is therefore a unit, of the form \(c x^r y^t\), with \(c\ne0\).
The Laurent-unit description follows by adding the highest and lowest exponents in a product equal to one, first in \(x\) over the domain \(\mathbb C[y^{\pm1}]\), and then in \(y\).
Its absolute value on the torus is the constant \(|c|\), so the new expected Gram equals \(|c|^{-2}C\) and still has no positive lower bound.
This contradiction excludes precisely the same-size polynomial left factor and finite witness normalization used above.
It does not exclude stabilization, different kernel witnesses, analytic congruences or another degeneration repair, and it exhibits no forbidden Atiyah rank.
For example, taking \(Y=0\) makes (N8) a kernel witness, but the different witness \(1\) has a uniformly positive Gram; the obstruction concerns the specified witness and factorization.

## Source comparison and continuation limit

The inspected local sources for reuse were [C_F0181's graded subordination proof](../claims/Yin_C_F0181_v1.md#graded-subordination-proof), [BBL21-U001](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), and the complete preceding calibration [L_A0014](../ledger/Yin_L_A0014_v1.md).
They supply the exact accepted subordination premise, kernel inclusion, trace normalization and the earlier support and expectation failures.
The finite polynomial recovery formula (12) was not located in those selected local passages; this limited comparison supports no historical priority claim.
It is the direct consequence of the source kernel inclusion and conditional-expectation bimodularity proved above.
The finite-tree gauge belongs to the already retained [tree-transport mechanism](../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators); the [source comparison in L_A0017](../ledger/Yin_L_A0017_v1.md#source-scope-correction) also records the scalar phase-gauge mechanism of BGVM20, without importing a general unitary-weighted index equality.
The cyclic polynomial-module normalization reuses classical principal ideal domain arguments, with a direct proof of the needed submodule assertion above.
The inspected [Coh06 original](../literature/pdf/Coh06.pdf) supplies \(\mathbb C[z]\) as a principal ideal domain at Theorem 1.3.2, printed p. 74 / PDF p. 98, finite free-submodule arguments at Propositions 1.4.1 and 1.4.5, printed pp. 78--79 / PDF pp. 102--103, and Smith reduction at Theorem 1.4.7 and proof, printed pp. 80--81 / PDF pp. 104--105.
The opening of Section 1.5, printed p. 86 / PDF p. 110, identifies the Laurent localization and infinite cyclic group algebra.
Localization at powers of \(z\), the coset coefficient calculation, the positive Gram bound and the actual congruence application are given explicitly here.
These selected algebraic passages were inspected for this use; no full-book audit or uninspected extension of BBL21 is claimed.
The normalization extends the specific [cyclic degeneration repair](../ledger/Yin_L_A0014_v1.md#an-exact-affiliated-normalization-and-its-limits) to every displayed polynomial witness with full-support expected Gram over the cyclic edge.

This pilot supplies a nonzero actual boundary shift and a sufficient route from finite polynomial kernel data to controlled vertex rational coefficients.
The remaining general problem includes finding such columns or a replacement certificate when they do not exist, and handling expected kernels whose support is not certified by those finite witnesses.
Finite polynomial columns in a kernel cannot be assumed for arbitrary nonamenable group-ring matrices; the [free-tree finite-support obstruction](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) already rules out that blanket assumption.
Even when polynomial columns exist, their expected Gram need not have full support.
For a cyclic edge, the polynomial normalization now removes the separate uniform-lower-bound obstacle whenever the displayed expected Gram has full support.
It leaves the existence of polynomial kernel witnesses and their full expected support as actual assumptions; a rank-deficient expected Gram yields no full-support subordination premise by this argument.
The useful next input is therefore a genuine finite group-ring matrix outside the finite-tree/known energy reductions, with a full-support expected Gram for explicit polynomial kernel columns or a different constrained boundary recovery mechanism.
Further positive zero-atom or opposite-base-shift examples do not address those remaining obligations.

## Assessment history

### Decision reviewed-polynomial-normalization

| Field | Value |
| --- | --- |
| date | 2026-11-11T16:54 |
| status | proved |
| reason | Independent whole-artifact review supports finite polynomial normalization of every full-support cyclic expected Gram, nullity-preserving actual congruence, normalized boundary recovery and conditional integer rank, with explicit rank-deficient and two-variable limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete original and normalized certificate variants, known-vertex hypothesis, indefinite example and the exact normalization limitations. |
| argument | [Argument](#argument) | Formulas (1)--(15) and (N1)--(N9), actual coset coefficients, PID factorization, uniform Gram bound, affiliated rank invariance, vertex transfer, two-variable obstruction and source scope. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0020_v2.md#whole-artifact-finding) | Complete saved statement and proof, all examples, endpoints, source interfaces and remaining witness/full-support assumptions. |

## Current assessment

[Selected decision](#decision-reviewed-polynomial-normalization)

