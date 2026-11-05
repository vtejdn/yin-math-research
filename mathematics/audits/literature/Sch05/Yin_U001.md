---
author: Yin
---

# Sch05-U001: Matrix-coefficient GOE resolvent comparison through real Ginibre variables

<a id="sch05-u001"></a>
## Exact edition and accepted inspection scope

The exact primary edition is [arXiv:math/0308192v1](../../../literature/pdf/Sch05--arxiv-v1.pdf), with [edition and publication notes](readme.md).
The selected 2026-11-05 reading covers the Gaussian ensemble definitions and symmetrization on PDF p. 2, the affine matrix-coefficient model on p. 6, the circular-system and free-resolvent definitions on p. 9, Theorem 3.2 on p. 15, and the constant-dependence observation in Remark 4.3 on p. 19.
Theorem 3.2 and the immediately preceding argument on pp. 14--15 were visually inspected, while the model and normalization were read in the actual source text.
Theorem 3.2 is accepted as an established external input at its exact fixed-coefficient statement after checking the GOE application below.
Its proof invokes Corollary 2.5 and the methods of Haagerup--Thorbjornsen Theorem 5.7; that underlying proof and all of Schultz's preceding master-equation analysis were not independently re-audited here.
The source's complete strong-convergence theorem is not needed as an additional premise of this selected input.
This is ordinary source preparation by a proof developer, not independent review of any resulting project theorem.

<a id="gaussian-and-free-normalizations"></a>
## Real Gaussian and free circular normalizations

On PDF p. 2, \(Y\in\mathrm{GRM}^{\mathbb R}(n,\sigma^2)\) means that its \(n^2\) real entries are independent \(N(0,\sigma^2)\) variables.
The source's \(X\in\mathrm{GOE}(n,\sigma^2)\) is real symmetric with independent variables \(X_{ii}/\sqrt2\) and \(X_{ij}\), \(i<j\), each having law \(N(0,\sigma^2)\).
It explicitly records
\[
 X=\frac{Y+Y^*}{\sqrt2}\in\mathrm{GOE}(n,\sigma^2).
 \tag{Real-symmetrization}
\]
With \(\sigma^2=1/n\), the off-diagonal variance is \(1/n\) and the diagonal variance is \(2/n\).
Thus this is the centered variance-one semicircular normalization needed in the selected real-Gaussian Wigner submodel.

On PDF p. 9, the source takes a circular system \(y_1,\ldots,y_r\) by requiring
\[
 x_j=\frac{y_j+y_j^*}{\sqrt2},
 \qquad x_{j+r}=\frac{y_j-y_j^*}{i\sqrt2},
 \qquad 1\le j\le r,
\]
to form a semicircular system \(x_1,\ldots,x_{2r}\).
In particular, the first \(r\) selfadjoint combinations are free variance-one semicircular elements.

<a id="matrix-affine-resolvent"></a>
## Exact operator-valued affine resolvent bound

Fix positive integers \(m,r\), matrices \(a_0,\ldots,a_r\in M_m(\mathbb C)\) with \(a_0=a_0^*\), and independent matrices \(Y_1^{(n)},\ldots,Y_r^{(n)}\) in \(\mathrm{GRM}^{\mathbb R}(n,1/n)\).
Take a circular system \(y_1,\ldots,y_r\) in a \(C^*\)-probability space \((\mathcal A,\tau)\), with the normalization just specified.
The source's Section 2 model and free comparison are
\[
 S_n=a_0\otimes I_n+
       \sum_{j=1}^r\left(a_j\otimes Y_j^{(n)}+a_j^*\otimes(Y_j^{(n)})^*\right),
\]
\[
 s=a_0\otimes1+
       \sum_{j=1}^r\left(a_j\otimes y_j+a_j^*\otimes y_j^*\right).
\]
For \(\lambda\in\mathcal O=\{\lambda\in M_m(\mathbb C):\operatorname{Im}\lambda>0\}\), define
\[
 G_n(\lambda)=\mathbb E(\operatorname{id}_m\otimes\operatorname{tr}_n)
          [(\lambda\otimes I_n-S_n)^{-1}],
 \qquad
 G(\lambda)=(\operatorname{id}_m\otimes\tau)[(\lambda\otimes1-s)^{-1}],
\]
where \(\operatorname{tr}_n=n^{-1}\operatorname{Tr}_n\).
Theorem 3.2, equation (3.6), PDF p. 15, states that a finite constant \(C_2\) satisfies
\[
 \|G_n(\lambda)-G(\lambda)\|
 \le\frac{C_2}{n}(\|\lambda\|+K)^2
       \left(\|(\operatorname{Im}\lambda)^{-1}\|^7+
             \|(\operatorname{Im}\lambda)^{-1}\|^5\right),
 \qquad K=\|a_0\|+16\sum_{j=1}^r\|a_j\|,
 \tag{Schultz-3.6}
\]
for every \(n\) and every \(\lambda\in\mathcal O\).
Remark 4.3 on PDF p. 19 states that the constants introduced through this bound can be expressed in terms of \(m\) and the coefficient norms.
The matrix coefficients may be complex, and \(a_j\) for \(j\ge1\) need not be selfadjoint.
This is an expectation estimate, not a probability statement or an almost-sure unregularized determinant theorem.
Its expectation depends only on the law within one dimension, so using it does not require independence between distinct dimensions.

<a id="goe-hermitization-specialization"></a>
## Direct specialization to the actual affine Hermitization

For fixed \(A_0(z),A_1,\ldots,A_d\in M_q(\mathbb C)\), let
\[
 L_n(z)=A_0(z)\otimes I_n+\sum_jA_j\otimes X_j^{(n)},
 \qquad
 B_0(z)=\begin{pmatrix}0&A_0(z)\\A_0(z)^*&0\end{pmatrix},
 \qquad
 B_j=\begin{pmatrix}0&A_j\\A_j^*&0\end{pmatrix}.
\]
Every \(B_j\) is selfadjoint, and the signed-singular-value Hermitization is
\[
 H_n(z)=\begin{pmatrix}0&L_n(z)\\L_n(z)^*&0\end{pmatrix}
       =B_0(z)\otimes I_n+\sum_jB_j\otimes X_j^{(n)}.
\]
Apply the exact source model with auxiliary size \(m=2q\), \(a_0=0\), \(a_j=B_j/\sqrt2\), and
\[
 \lambda_z(\eta)=i\eta I_{2q}-B_0(z),\qquad\eta>0.
\]
Then \(\operatorname{Im}\lambda_z(\eta)=\eta I_{2q}\), and (Real-symmetrization) identifies the finite resolvent with that of \(H_n(z)\).
The free circular normalization identifies the comparison with the Hermitization \(H(z)\) of the same pencil in variance-one free semicircular variables.
Taking the normalized outer matrix trace cannot increase the operator-norm error, so (Schultz-3.6) gives
\[
 \left|\mathbb E\frac1{2qn}\operatorname{Tr}(i\eta I-H_n(z))^{-1}
       -(\operatorname{tr}_{2q}\otimes\tau)(i\eta I-H(z))^{-1}\right|
 \le\frac{C_K}{n}(\eta^{-7}+\eta^{-5}),\qquad0<\eta\le1,
 \tag{GOE-Hermitization}
\]
uniformly for \(z\) in any fixed set on which \(\|B_0(z)\|\) is bounded.
This uniformity follows from the theorem's single constant for all \(\lambda\in\mathcal O\), with the random coefficients and \(a_0=0\) fixed.
Equivalently, at one fixed \(z\), one may take \(a_0=B_0(z)\) and \(\lambda=i\eta I\); these two constant placements must not be combined, which would count \(B_0(z)\) twice.

The specialization is applied to the linear Hermitization of an affine pencil.
It therefore avoids assuming a direct general-polynomial resolvent bound, or putting a rank-deficient imaginary corner parameter into a theorem requiring a strictly positive imaginary part.
The subsequent free small-mass estimate, negative logarithmic tails, Gaussian concentration and Brown-measure passage remain project arguments at their actual consuming Claim.
For example, if its free signed-singular law has no atom at zero and the accepted algebraic/Puiseux input gives mass \(O(t^\beta)\) near zero, this resolvent bound yields the mesoscopic expected count \(O(t^\beta+n^{-1}t^{-6})\).
That counting deduction does not itself provide a least-singular-value floor or complete a determinant theorem.
