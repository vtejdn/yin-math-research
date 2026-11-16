---
author: Yin
---
# A complex rank obstruction for the prescribed common-label degrees

OpenAI's September 23, 2026 preprint Ope26f describes two rooted graphs and a product of finite sums in \(\mathbb F_2[G]\).
The [author's preprint](../literature/pdf/Ope26f.pdf#page=1) gives the coefficient field on page 1, the simultaneous-step argument on page 2 and the prescribed vertex types on pages 3–4.
A simultaneous step with outgoing label \(t\) preserves the product \(g_xh_y^{-1}\), since \((g_xt)(h_yt)^{-1}=g_xh_y^{-1}\).
Every pair of vertices in the selected root components has odd common-label degree.
The degree sum on each finite component of the simultaneous-step graph then makes its number of vertices even, which cancels its contribution in characteristic two.
These are the cancellation statements in the [introduction and theorem of Ope26f](https://github.com/openai/math/blob/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex).

For the [complex-coefficient Task](../tasks/Yin_T_A0001_v1.md#contract), consider weights \(c_t\in\mathbb C\) depending only on the outgoing label.
The coefficient contributed by a pair of vertices to a product of two scalar sums with vertex coefficients \(a_x,b_y\) is \(a_xb_y\).
Consequently any attempt to realize these pair coefficients as common-label weighted degrees on the full type family must satisfy
\[
 W_{xy}:=\sum_{t\in S_x\cap S_y}c_t=a_x b_y .
\]
Here \(S_x\) is the prescribed set of outgoing labels at \(x\).
The test allows arbitrary zero weights and arbitrary zero vertex coefficients.
An inverse-symmetric choice \(c_t=c_{\bar t}\) assigns the same weight to the two readings of an undirected edge.
Over \(\mathbb C\), cancellation of the resulting sums on individual product fibers would be a further condition.

## Rank on all prescribed types

The [finite-geometry and matching prescriptions of Ope26f](https://github.com/openai/math/blob/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/sections/types.tex) use the projective plane of order \(q=128\).
Its \(v=q^2+q+1\) points are the ordinary labels.
On either side the ordinary part of a vertex type is a line.
For each line on side \(A\), the extra set \(I\) is empty or one of the three pairs from \(\{1,2,3\}\).
On side \(B\), the extra set \(J\) is empty or all three extras.
Every indicated type occurs with positive multiplicity before choosing root components.
Each extra is inverse to a distinct ordinary label, and the remaining ordinary labels are paired among themselves.

Let \(N\) be the square line-by-point incidence matrix.
Since a line has \(q+1\) points and distinct lines meet once, \(NN^{\mathsf T}=qI_v+\mathbf1\mathbf1^{\mathsf T}\).
Its eigenvalues are \(q\) and \(q+v\), so \(N\) is invertible over \(\mathbb C\).
Write \(D=\operatorname{diag}(c_t:t\text{ ordinary})\), \(e_i=c_i\) for the extra weights, and \(s=\#\{t:t\text{ ordinary},\ c_t\ne0\}\).
With a single representative for each type the entries of \(W\) are
\[
 W_{(L,I),(M,J)}
 =(NDN^{\mathsf T})_{LM}
   +\left(\sum_{i\in I}e_i\right)\mathbf1_{\{J=\{1,2,3\}\}} .
\]
Repeating the rows and columns for actual vertices preserves rank because every representative occurs.

Subtract row \((L,\varnothing)\) from each nonempty-extra row of the same line and subtract column \((M,\varnothing)\) from the full-extra column of each line.
The empty-extra rows and columns carry the block \(NDN^{\mathsf T}\), of rank \(s\).
The two off-diagonal blocks vanish.
The remaining block has identical columns, formed by repeating the three pair sums \(e_1+e_2,e_1+e_3,e_2+e_3\) at each line.
The matrix of these three linear forms has determinant \(-2\), so the remaining block has rank one precisely when \(e\ne0\).
Thus
\[
                 \operatorname{rank}_{\mathbb C}W=s+\mathbf1_{\{e\ne0\}} .
\]
Without a reversal condition the nonzero rank-one choices are exactly a single nonzero ordinary weight with all extras zero, or a nonzero vector of extra weights with all ordinary weights zero.

Suppose the support of \(c\) is closed under the inverse pairing.
If \(r\) ordinary-ordinary pairs and \(m\) mixed pairs have nonzero weights, the exact rank is
\[
                  2r+m+\mathbf1_{\{m>0\}} .
\]
The minimum among nonzero choices is two, attained by activating either kind of single inverse pair.
This rules out the scalar factorization on the full prescribed family for every nonzero inverse-symmetric choice, and also for weights with \(c_{\bar t}=-c_t\).
For antisymmetric weights, summing \(W_{xy}\) on a simultaneous-step component does cancel over \(\mathbb C\): the two orientations of each edge contribute opposite weights.
The rank bound identifies the obstruction to writing these particular canceling coefficients as a single scalar product.
Multiplication by nonvanishing separate row and column signs preserves this obstruction.

## Scope for the group-ring product

The rank calculation uses the complete array of types and is independent of the choice of matchings.
Restricting to a pair of root components can remove rows or columns needed by the calculation.
Moreover, distinct simultaneous-step components can have the same group product, so a choice of scalar vertex coefficients could cancel after summing over the group-product fibers without being given by common-label weights.
The complex lift tested here is excluded at the level of the full type array.
Whether other coefficients or a different cancellation mechanism give a complex zero divisor remains open in this comparison.
The geometric safeguards and the proof of the preprint's group theorem were outside this source inspection.
