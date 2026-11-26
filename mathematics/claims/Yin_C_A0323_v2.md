---
author: Yin
---

# Scalar and matrix kernel projections without a closed-range assumption

## Statement

Let \(K=[L,R]\) be a bounded two-square matrix over \(A=C_r^*(H)\), written in an orthonormal basis of its two input coordinates, and assume that the column \(L\) is bounded below.
Put \(a=L^*L,\ X=a^{-1}L^*R\) and
\[
             D=R^*R-(L^*R)^*a^{-1}(L^*R),\qquad
             p=\mathbf1_{\{0\}}(D),\qquad P=\mathbf1_{\{0\}}(K^*K).
\]
The projections at zero initially belong to the group von Neumann algebra and its two-square matrix algebra, respectively.
Then
\[
                        p\in A\quad\Longleftrightarrow\quad P\in M_2(A).
\]
Whenever this holds, \(0\oplus p\) and \(P\) are Murray-von Neumann equivalent in \(M_2(A)\).
In particular every tracial state \(\phi\) on \(A\) has \(\phi(p)=({\rm Tr}_2\otimes\phi)(P)\), with unnormalized coordinate trace.

For the regular trace \(\tau\), put \(\delta=\tau(p)=({\rm Tr}_2\otimes\tau)(P)\) and \(\eta=(1+\|X\|^2)^{-1}\).
If \(\delta\) is absent from the set of regular traces of scalar projections in \(A\), then the operator-norm distances satisfy
\[
                   {\rm dist}(p,A)=1/2,\qquad
                   {\rm dist}(P,M_2(A))\ge\eta/2.
\]
These distances are also the infima of distances to scalar and matrix group-ring elements since the latter are norm dense.
For a noninteger two-label four-site nullity, the [bounded column theorem](Yin_C_A0323_v1.md#statement) supplies such an input basis.
All these tests apply when \(K\) has nonclosed range.

Suppose additionally \(H\) is finitely generated, with word length \(|g|\), and satisfies the rapid decay inequality \(\|f\|_{\rm op}\le C\|f\|_{2,r}\) on its complex group ring for some \(r\ge0\), where
\[
                  \|f\|_{2,u}^2=\sum_{g\in H}(1+|g|)^{2u}|f_g|^2.
\]
Use the sum of entrywise squares for matrices.
If \(K\) is a group-ring matrix, then for each fixed \(u>r\) one has
\[
                         \|p\|_{2,u}<\infty
                           \quad\Longleftrightarrow\quad
                         \|P\|_{2,u}<\infty .
\]
In this assertion the norms use the Fourier coefficients of the von Neumann algebra projections.
It follows in particular that finiteness at every nonnegative exponent is equivalent on the two sides.
Under the scalar trace obstruction above, both weighted square sums diverge already at exponent \(r\).

## Recovering the two projections

The Gram matrix of \(K\) has first diagonal entry \(a\ge cI\) for some \(c>0\).
The bounded [Gram elimination](Yin_C_A0323_v1.md#reduction-to-one-scalar-in-the-reduced-group-algebra) identifies the kernel of \(K\) with the range of the column \(Jp\), where \(J=(-X,I)^{\mathsf T}\).
Indeed the first Gram equation gives the first coordinate \(-Xv\) and the second then gives \(Dv=0\).
This column has closed range since its last coordinate is the identity on \(p\ell^2(H)\), irrespective of the range of \(K\).

Put \(B_0=I+pX^*Xp\).
It commutes with \(p\) and satisfies \(I\le B_0\le\eta^{-1}I\).
The bounded partial isometry \(V=JpB_0^{-1/2}\) and the last diagonal block \(P_{22}\) satisfy
\[
             V^*V=p,\qquad VV^*=P,\qquad
             P_{22}=pB_0^{-1}p,\qquad
             {\rm spec}(P_{22})\subseteq\{0\}\cup[\eta,1].
\]
In fact the first equality follows from \(pJ^*Jp=pB_0p\), and the range of \(V\) is exactly the graph range just identified.
Thus
\[
                         p=\mathbf1_{[\eta,1]}(P_{22}).
\]
If \(p\in A\), the formula for \(V\) belongs to the corresponding column over \(A\) by functional calculus, proving both \(P\in M_2(A)\) and equivalence there.
If \(P\in M_2(A)\), its last block belongs to \(A\), and the spectral gap for that block recovers \(p\in A\) by continuous functional calculus.
Constant input basis changes preserve the matrix algebra, its tracial values and its operator-norm distance.

## Distance from the scalar projection traces

For a bounded selfadjoint \(B\) with spectrum in \(\{0\}\cup[\eta,1]\) and any selfadjoint \(B'\) with \(\|B'-B\|<\eta/2\), the straight segment between them has spectrum uniformly separated from \(\eta/2\).
This follows from the distance bound on the spectrum of a selfadjoint perturbation.
The spectral projections above that threshold vary norm continuously along the segment.
Their trace in the finite von Neumann algebra is consequently constant, since two projections within norm less than one are equivalent and finitely many such comparisons cover the segment.
If \(B'\in A\) its endpoint spectral projection lies in \(A\).

Apply this observation first to \(B=p\) with gap one and then to \(B=P_{22}\) with gap \(\eta\).
For any approximating element one may take its selfadjoint part without increasing the error.
A matrix approximation to \(P\) has last block approximating \(P_{22}\) at least as well.
An error strictly below either asserted threshold would thus give a scalar projection in \(A\) with regular trace \(\delta\).
Finally \(\|p-I/2\|=1/2\), proving the exact scalar distance.

## A fixed rapid decay exponent on both sides

For clarity, inverse closure at the single exponent \(u>r\) follows directly from the stated rapid decay inequality.
Let \(\mathcal H^u\) denote the Hilbert completion of the group ring for \(\|\cdot\|_{2,u}\).
It embeds in \(A\) by rapid decay, with the same Fourier coefficients, and is closed under adjoints.
For finitely supported \(f,g\) the word-length triangle inequality and
\((1+|xy|)^u\le 2^u((1+|x|)^u+(1+|y|)^u)\) give
\[
 \|fg\|_{2,u}\le C_u\big(\|f\|_{2,u}\|g\|_{2,r}
                          +\|f\|_{2,r}\|g\|_{2,u}\big).
\]
Indeed one bounds the weighted convolution by the sum of two convolutions of absolute coefficients, placing the weight on one factor at a time.
The other factor acts boundedly by left or right convolution by rapid decay, using inversion for the right action.
Density extends the product bound and a constant rescaling of the norm gives a Banach algebra.

For \(\theta=r/u<1\), weighted Hilbert-space interpolation gives
\(\|f\|_{2,r}\le\|f\|_{2,0}^{1-\theta}\|f\|_{2,u}^{\theta}\), while \(\|f\|_{2,0}\le\|f\|_{\rm op}\) by applying the convolution to the identity vector.
For a constant \(C'_u\ge1\) it follows that
\[
       \|f^2\|_{2,u}\le C'_u\|f\|_{2,u}^{1+\theta}
                                   \|f\|_{\rm op}^{1-\theta}.
\]
Normalize first to \(\|f\|_{\rm op}=1\).
All the dyadic powers still have operator norm at most one, so the positive part of the logarithm of their weighted norms grows at most as
\((1+\theta)^j\log^+\|f\|_{2,u}+\log C'_u\sum_{k=0}^{j-1}(1+\theta)^k\) for the power \(2^j\).
If a power vanishes its spectral radius is already zero.
Dividing the bound by \(2^j\) gives limit zero, also when \(\theta=0\).
The spectral radius formula and scaling therefore bound the spectral radius in \(\mathcal H^u\) by \(\|f\|_{\rm op}\).

If \(x\in\mathcal H^u\) is invertible in \(A\), take \(c>\|x\|_{\rm op}^2\).
The element \(I-x^*x/c\) has operator norm strictly below one and hence spectral radius below one in \(\mathcal H^u\).
Its geometric series converges there, proving \(x^{-1}=(x^*x)^{-1}x^*\in\mathcal H^u\).
Consequently holomorphic functional calculus of a single element stays in this algebra, by the resolvent contour formula in the complete norm.
This includes the positive inverse square root and the separated spectral projection used above.

For a group-ring input, \(a,L^*R\in\mathcal H^u\) and inverse closure gives \(X\in\mathcal H^u\).
If \(p\in\mathcal H^u\), all entries in \(V\) and \(P=VV^*\) belong to that algebra.
If all entries of \(P\) belong to it, the separated spectral projection of \(P_{22}\) belongs to it and equals \(p\).
A group von Neumann algebra element with finite \(\|\cdot\|_{2,u}\) agrees with its group-ring truncation limit in this space by rapid decay and Fourier uniqueness.
This proves the equivalence at each fixed exponent.
At \(r\) itself, finite weighted norm still gives operator-norm convergence of truncations by the defining inequality, scalar or entrywise.
Therefore the positive distance bounds under the trace obstruction force divergence on both sides at \(r\).

## Assessment history

### Decision the-two-kernel-projections-at-nonclosed-range

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:51 |
| status | proved |
| reason | The graph formulas recover both kernel projections, transfer their trace obstruction and preserve each stated Fourier weight above the rapid decay exponent. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The equivalence of membership, distances, and fixed weighted Hilbert norms. |
| argument | [Recovering the two projections](#recovering-the-two-projections) | The bounded graph and the isolated positive spectrum of the bottom coordinate. |
| argument | [Distance from the scalar projection traces](#distance-from-the-scalar-projection-traces) | The two distance bounds for a trace omitted by the scalar projections. |
| argument | [A fixed rapid decay exponent on both sides](#a-fixed-rapid-decay-exponent-on-both-sides) | The two-sided algebra estimate and finite Fourier moments at the threshold. |
| dependency | [A bounded positive scalar denominator](Yin_C_A0323_v1.md#statement) | The gapped scalar Gram entry. |
| review | [A bounded scalar pivot in the regular representation](../audits/reviews/Yin_R_A0225_v1.md#a-bounded-scalar-pivot-in-the-regular-representation) | Independent review of the pivot and scalar Schur complement. |
| review | [The two kernel projections at nonclosed range](../audits/reviews/Yin_R_A0225_v1.md#the-two-kernel-projections-at-nonclosed-range) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-two-kernel-projections-at-nonclosed-range)
