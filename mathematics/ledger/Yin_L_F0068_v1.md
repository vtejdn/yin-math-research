---
author: Yin
---

# Gaussian rotation and the fourth-moment Wigner disk lower bound

On 11 November 2026, an authoring agent for Yin examined the user-directed question whether the Gaussian rotation and convexity argument of CKMYZ26 supplies the lower bound in [D9](../drafts/Yin_D_F0009.md#wigner-lower-bound) when the fixed Wigner off-diagonal laws have finite fourth absolute moments.
The diagonal laws may still have finite second moments, as in the [earlier fourth-moment investigation](Yin_L_F0061_v3.md).
The calculations and conditional deductions below were checked during authoring, without an independent proof review or a completed Claim assessment.
The general lower bound remains unresolved.

<a id="source-transfer"></a>
## The exact source mechanism

The source is [arXiv:2611.12785v1](https://arxiv.org/pdf/2611.12785v1), Proposition 2.12, Theorem 3.3 and its proof, Theorem 3.4 and the following conditioning remark, and Proposition 3.5 with Lemma 3.6.
The [source-reading unit](../audits/literature/CKMYZ26/Yin_U001.md#repository-gue-comparison) owns the proof comparison and its inspection limits.
Write \(b(A)=n^{-1}\sum_{j=1}^n|\lambda_j(A)|^2\).
For independent GUE tuples \(G,H\), set
\[
 g_n(w)=\mathbb E b\bigl(P(\cos(w)G+\sin(w)H)\bigr),
 \qquad f_n(y)=g_n(iy).
\]
Analyticity gives subharmonicity of \(g_n\), while the real rotation
\[
 (G,H)\longmapsto(\cos(x)G+\sin(x)H,-\sin(x)G+\cos(x)H)
\]
preserves their joint law and hence gives \(g_n(x+iy)=f_n(y)\).
The distributional inequality \(\Delta g_n\ge0\) therefore becomes \(f_n''\ge0\).
Evenness and a uniform bound for \(f_n(1)\) then give
\[
 0\le f_n(y)-f_n(0)\le C_P|y|\qquad(|y|\le1).
 \tag{Gaussian-boundary}
\]
This dimension-uniform boundary estimate transfers the fixed-positive-noise conclusion to the original GUE input.
Subharmonicity alone does not eliminate the horizontal second derivative and does not imply this convexity.

<a id="non-gaussian-convexity"></a>
## Exact convexity fails even for bounded laws

For independent centered real variables \(\xi,\eta\) of variance one and fourth moment \(\mu_4\), direct expansion gives
\[
 \mathbb E\left(\frac{\xi+\eta}{\sqrt2}\right)^4
 =\frac{\mu_4+3}{2}.
\]
In particular, Rademacher laws are not preserved by the real rotation used above.
There is also a direct failure of the proposed convexity, rather than only a missing invariance argument.
Let \(\epsilon,\delta\) be independent Rademacher variables and put
\[
 Z(y)=\cosh(y)\epsilon+i\sinh(y)\delta,
 \qquad P(z)=(z^2-1)^2+1.
\]
Since \(Z(y)^2=1+i\sinh(2y)\epsilon\delta\), one has
\[
 P(Z(y))=1-\sinh^2(2y),\qquad
 \mathbb E|P(Z(y))|^2=(1-\sinh^2(2y))^2
 =1-8y^2+O(y^4).
\]
Thus \(f''(0)=-16\).
This is an exact size-one test with all entry moments finite, so an all-size version of the source convexity theorem for arbitrary Wigner laws is false.
For every \(R>1\), the same local calculation applies to the cutoff \(\min(|P(Z(y))|^2,R^2)\) near zero.
This test does not refute an asymptotic convexity or boundary estimate for large Wigner matrices, and it is not a counterexample to the Wigner Brown-measure conjecture.

<a id="integrability-cutoff"></a>
## Fourth moments do not justify the untruncated expectation

Choose a centered symmetric variance-one law with \(\mathbb P(|\xi|>t)\asymp t^{-5}\), and take real Wigner matrices with zero diagonal and off-diagonal entries \(\xi_{ij}/\sqrt n\).
Then \(\mathbb E|\xi|^4<\infty\) and \(\mathbb E|\xi|^6=\infty\).
For \(P(x)=x^3\) and every \(n\ge2\), selfadjointness gives
\[
 b(P(W_n))=\frac1n\operatorname{Tr}W_n^6
 \ge\frac1n\|W_n\|^6
 \ge n^{-4}|\xi_{12}|^6.
\]
Consequently \(\mathbb E b(P(W_n))=\infty\) at every such size.
Finite fourth moments therefore do not even make the source's untruncated expectation usable for arbitrary-degree polynomials.

D9 instead uses the bounded statistic
\[
 m_{n,R}(A)=\frac1n\sum_{j=1}^n\min(|\lambda_j(A)|^2,R^2).
\]
The scalar function \(z\mapsto\min(|z|^2,R^2)\) is not subharmonic: at a point with \(|z|=R\), its average on every sufficiently small centered circle is strictly smaller than its value \(R^2\).
Thus Proposition 2.12 cannot simply be applied after this cutoff.
Truncating the input law instead resolves finite-size integrability, but it neither restores rotation invariance nor proves stability of this eigenvalue statistic under the truncation error.

<a id="fixed-noise"></a>
## What can be transferred at fixed Gaussian noise

Let \(W_n=(W_{1,n},\ldots,W_{k,n})\) be a tuple independent of normalized complex Ginibre matrices \(C_n=(C_{1,n},\ldots,C_{k,n})\), and suppose \(M_n=\max_j\|W_{j,n}\|\) is tight in probability.
Finite fourth off-diagonal moments and finite second diagonal moments give this norm tightness by the estimates in [L61v3](Yin_L_F0061_v3.md).
Fix \(\sigma>0\), a nonconstant scalar polynomial \(P\), and \(z\notin E_P\), where
\[
 E_P=\{z\in\mathbb C:P(c)=z\text{ for every }c\in\mathbb C^k\}.
\]
Choose \(c_0\) with \(P(c_0)\ne z\) and use the word-chain pencil \(L_z\) and invertible scalar basepoint matrix \(K_{z,c_0}=L_z(c_0)\) from the source.
Writing \(B_j\) for its variable coefficients gives
\[
 (K_{z,c_0}^{-1}\otimes I_n)L_z(W_n+\sigma C_n)
 =I+\sum_jR_j\otimes(C_{j,n}+D_{j,n}),
 \quad R_j=\sigma K_{z,c_0}^{-1}B_j,
 \quad D_{j,n}=(W_{j,n}-c_{0,j}I_n)/\sigma.
\]
Conditionally on \(W_n\), these are exactly the structured means allowed by Theorem 3.4.
On \(\{M_n\le K\}\) their norms are at most \(\max_j(K+|c_{0,j}|)/\sigma\).
The same Schur-complement comparison as in source Proposition 3.5 therefore yields
\[
 \mathbb P\{s_{\min}(P(W_n+\sigma C_n)-zI_n)<t\}
 \le\mathbb P\{M_n>K\}
   +C_{K,\sigma,z,P}\bigl(n^{a(m)}t^{2/m}+e^{-c_{K,\sigma,z,P}n}\bigr),
 \tag{Conditional-floor}
\]
for all sufficiently large \(n\), with \(m\) the fixed pencil size and \(a(m)\) as in the source.
The exponent \(a(m)\) is independent of the mean bound \(K\).
For any \(q>0\), choose \(M>m(a(m)+q)/2\), then send \(n\) to infinity at fixed \(K\), followed by \(K\) to infinity.
This proves
\[
 \mathbb P\{s_{\min}(P(W_n+\sigma C_n)-zI_n)<n^{-M}\}\longrightarrow0.
\]
Only the conditional error inside the norm guard has the stated polynomial rate; norm tightness alone supplies neither a summable unconditional error nor uniform constants as \(\sigma\downarrow0\).
This is a conditional application of the source theorem, whose full proof is an external input rather than an independently re-audited result here.

A least-value floor still needs quantitative control of the number of small singular values to yield convergence of logarithmic potentials.
Source Lemma 3.6 uses a GUE selfadjoint-polynomial count estimate; it does not automatically cover an arbitrary Wigner background conditioned as above.
The repository's [intermediate-value theorem](../claims/Yin_C_F0187_v1.md#statement) concerns \(W_n+F_n\) with scalar coefficients and an independent shift, and explicitly does not cover general matrix-coefficient pencils.
Thus the displayed floor by itself is not a proof of Brown convergence even at fixed \(\sigma\).

<a id="zero-noise-target"></a>
## The precise boundary estimate that would close the expectation gap

Put
\[
 A_{n,\sigma}=P(W_n+\sigma C_n),\qquad
 a_\sigma=P(s+\sigma c),\qquad
 m(\sigma)=\int|w|^2\,d\mu_{a_\sigma}(w),
\]
where \(c\) is a free standard circular tuple independent of the standard semicircular tuple \(s\).
Choose the D9 radius \(R>\|P(s)\|\).
For all sufficiently small \(\sigma\), norm continuity ensures \(R>\|a_\sigma\|\).
The free tuple \(s+\sigma c\) has the same joint star law as \(\cosh(y)s'+i\sinh(y)t'\), where \(s',t'\) are free standard semicircular tuples and \(\sinh(y)=\sigma/\sqrt2\).
The free part of Theorem 3.3 consequently gives \(m(\sigma)\to m(0)\), in fact with an \(O(\sigma)\) error.
The free endpoint continuity is therefore available.

Suppose separately that the fixed-positive-noise ensemble has Brown convergence in probability, so boundedness gives
\[
 \mathbb E m_{n,R}(A_{n,\sigma})\longrightarrow m(\sigma)
 \qquad(\sigma>0\text{ fixed and sufficiently small}).
\]
The remaining sufficient one-sided estimate is
\[
 \boxed{\displaystyle
 \lim_{\sigma\downarrow0}\limsup_{n\to\infty}
 \bigl(\mathbb E m_{n,R}(A_{n,\sigma})
       -\mathbb E m_{n,R}(A_{n,0})\bigr)_+=0.}
 \tag{Wigner-boundary-target}
\]
Indeed, subtract this excess from the fixed-noise expectation and then let \(\sigma\) decrease to zero to obtain
\(\liminf_n\mathbb E m_{n,R}(A_{n,0})\ge m(0)\).
Together with D9's upper control and boundedness of the statistic, this implies convergence of its mean and convergence in probability to \(m(0)\), hence Brown convergence in probability through the disk criterion.
It does not establish D9's almost-sure conclusion under every cross-size coupling, for which the [summable marginal lower deviations](../drafts/Yin_D_F0009.md#wigner-lower-bound) remain necessary.

Norm bounds and analytic subharmonicity cannot supply this dimension-uniform boundary continuity on their own.
For the nilpotent upper shift \(J_n\), put \(B_n(w)=J_n+wE_{n1}\).
This is an entire matrix family with \(\|B_n(w)\|\le1+|w|\), and its eigenvalues are the \(n\)-th roots of \(w\), so
\[
 b(B_n(w))=|w|^{2/n},\qquad b(B_n(0))=0.
\]
For every fixed \(w\ne0\), the first quantity tends to one.
This example concerns general analytic matrix families, not Wigner inputs, and shows exactly why off-boundary convergence and a common norm bound do not suffice for the proposed transfer.
Likewise, replacement estimates proved only at fixed singular regularization do not justify removing that regularization uniformly in \(n\); that passage must control the logarithmic defect rather than assume its disappearance.

The usable outcome is a conditional fixed-noise singular-value estimate and a precise new Wigner boundary target, with exact failures of two direct extensions.
No lower-bound proof or change of the accepted F0012 status is claimed.
