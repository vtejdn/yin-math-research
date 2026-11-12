---
author: Yin
---
# Nonzero amalgamated boundary shifts and a finite polynomial kernel certificate

Date: 2026-11-12 (Asia/Hong_Kong).
This development serves [S_A0005](../strategies/Yin_S_A0005.md) and the bounded discriminator in [the seven-route assessment](../ledger/Yin_L_A0018_v1.md#amalgamated-atom-transport).
It constructs an actual indefinite two-vertex group-ring matrix with a non-bottom zero atom, uniformly invertible expected kernel and nonzero actual subordination boundary values.
It then isolates a finite polynomial kernel certificate that recovers those boundary values in the actual cyclic rational matrix ring, without requiring rationality of the full expected kernel.
The four-path example is covered by an explicit finite-tree unitary gauge and cyclic vertex blocks; it supplies no new group class.
The general certificate is conditional on displayed polynomial kernel columns and an actual expected-Gram condition, not an existence assertion for arbitrary group-ring kernels.

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
The total kernel is nonzero under (13), since the displayed nonzero \(W\) lies in it.
No hypothesis that the whole amalgam already has the Atiyah property is used.
The argument is valid for a noncentral cyclic edge as well: coefficient extraction, bimodularity and the actual cyclic-field inclusion do not require centrality.
The worked example, however, remains central and is already covered by known group results.

## Source comparison and continuation limit

The inspected local sources for reuse were [C_F0181's graded subordination proof](../claims/Yin_C_F0181_v1.md#graded-subordination-proof), [BBL21-U001](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), and the complete preceding calibration [L_A0014](../ledger/Yin_L_A0014_v1.md).
They supply the exact accepted subordination premise, kernel inclusion, trace normalization and the earlier support and expectation failures.
The finite polynomial recovery formula (12) was not located in those selected local passages; this limited comparison supports no historical priority claim.
It is the direct consequence of the source kernel inclusion and conditional-expectation bimodularity proved above.
The finite-tree gauge belongs to the already retained [tree-transport mechanism](../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators); the [source comparison in L_A0017](../ledger/Yin_L_A0017_v1.md#source-scope-correction) also records the scalar phase-gauge mechanism of BGVM20, without importing a general unitary-weighted index equality.
No new external theorem or uninspected extension of BBL21 is being used.

This pilot supplies a nonzero actual boundary shift and a sufficient route from finite polynomial kernel data to controlled vertex rational coefficients.
The remaining general problem includes finding such columns or a replacement certificate when they do not exist, and handling diffuse expected-kernel degeneration when only full support is known.
Finite polynomial columns in a kernel cannot be assumed for arbitrary nonamenable group-ring matrices; the [free-tree finite-support obstruction](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) already rules out that blanket assumption.
Even when polynomial columns exist, their expected Gram need not meet (13), and this investigation proves no general normalization restoring it.
The useful next input would therefore be a genuine finite group-ring matrix outside the finite-tree/known energy reductions, with a verified expected-Gram certificate or an alternative constrained boundary recovery mechanism.
Further positive zero-atom or opposite-base-shift examples do not address those remaining obligations.

## Assessment history

### Decision reviewed-boundary-certificate

| Field | Value |
| --- | --- |
| date | 2026-11-11T16:33 |
| status | proved |
| reason | Independent whole-candidate review supports the nonzero actual boundary model, both finite polynomial witness variants and the conditional integer-rank transfer from known vertex division closures. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete cyclic-amalgam hypotheses, actual boundary recovery, stronger expected-Gram certificate, conditional vertex-rank conclusion and explicit indefinite model. |
| argument | [Argument](#argument) | Complete formulas (1)--(15), full example, support and bounded-inverse distinctions, actual cyclic field, subgroup rank transfer and source/continuation limitations. |
| review | [Independent whole-candidate finding](../audits/reviews/Yin_R_A0020_v1.md#whole-candidate-finding) | Exact complete saved candidate and declared analytic source interfaces, with no universal witness, new group-class or Task-completion assertion. |

## Current assessment

[Selected decision](#decision-reviewed-boundary-certificate)

