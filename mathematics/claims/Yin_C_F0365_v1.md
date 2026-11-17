---
author: Yin
---

# Nonreal roots away from the real axis at the Wigner positivity threshold

<a id="statement"></a>
## A fixed-strip count and the determinant at a prescribed nonreal point

Use independent colors within each size under the [fixed complex Wigner laws with finite second moments](../tasks/Yin_T_F0013_v1.md#input-model), allowing any coupling across sizes.
Set \(A=2I+X,\ B=XY+YX+ZYZ,\ P=AB\).
For every fixed \(h>0\), count with algebraic multiplicity
\[
 k_N(h)=\#\{\lambda\in\operatorname{spec}(P_N):|\operatorname{Im}\lambda|\ge h\}.
\]
There exists a deterministic sequence of dyadic sizes \(N_l\to\infty\) for which
\[
                   (\log N_l) k_{N_l}(h)/N_l\longrightarrow0
                   \quad\text{in probability}.                          \tag{1}
\]
This holds also when every color is purely atomic.

For the determinant assertion suppose that the two raw laws \(\mu\) of \(Y\) satisfy, for some \(\alpha,C>0\) and \(0\le t\le1\),
\[
       \|(\mathrm e^t\cdot)_*\mu-\mu\|_{\rm TV}\le C t^\alpha .        \tag{2}
\]
Both laws of \(X,Z\) remain arbitrary.
For each fixed nonreal \(z\), along a deterministic subsequence of dyadic sizes the ordinary logarithms converge almost surely to
\[
       u(z)=\tau\log|(2+s_x)(s_xs_y+s_ys_x+s_zs_ys_z)-z|.
\]
In particular their full-sequence almost-sure upper limit equals \(u(z)\) under every allowed coupling.
Here the ordinary logarithm means \(N^{-1}\log|\det(P_N-zI)|\), with value \(-\infty\) at a zero.
The [exact word-chain pencil](../ledger/Yin_L_F0061_v2.md#linearization-transfer) has the corresponding upper limit divided by its fixed auxiliary dimension.
At \(z=i\), the normalized logarithm of the [negative-subspace determinant](Yin_C_F0358_v3.md#statement) tends to zero on the indicated subsequence.
For general atomic \(Y\), (1) still leaves the distances of the counted roots to \(z\) undetermined.

<a id="tails"></a>
## Summable spectral weight outside a fixed enlargement of the semicircle

For any single input \(W\), fixed \(b>2\), and \(1\le p<2\), we prove
\[
   \sum_{j\ge1}\mathbb E\,\operatorname{tr}_{2^j}
        (|W|^p\mathbf1_{\{|W|>b\}})<\infty,                         \tag{3}
\]
where \(\operatorname{tr}_N=\operatorname{Tr}/N\).
Truncate the raw off-diagonal \(\xi\) at \(\sqrt N\), center it, and let \(U\) use these entries and a zero diagonal.
In the difference \(W-U=D+E\), put the deterministic strict-upper centering mean and its conjugate lower entries in \(D\).
Then \(\|D\|\le\sqrt N|\mathbb E[\xi\mathbf1_{|\xi|>\sqrt N}]|\le\mathbb E[|\xi|^2\mathbf1_{|\xi|>\sqrt N}]=o(1)\), even for complex centering.
The remaining matrix \(E\) contains the original diagonal and large off-diagonal entries.
For any matrix \(V\), concavity of \(s^{p/2}\) first on the spectral measure of \(VV^*\) at each coordinate and then subadditivity of that power give \(\operatorname{Tr}|V|^p\le\sum_{a,b}|V_{ab}|^p\).
Consequently
\[
 \mathbb E\operatorname{tr}_N|E|^p\le
    N^{-p/2}\mathbb E|\zeta|^p+
    N^{1-p/2}\mathbb E[|\xi|^p\mathbf1_{|\xi|>\sqrt N}].
\]
The dyadic sum is finite, since for each raw magnitude \(v\) the sum of \(N^{1-p/2}\) over dyadic \(N<v^2\) is at most \(C_pv^{2-p}\).

Choose constants \(0<\theta,\eta,\beta<1\) with \(\beta\theta b>2\) and \(\theta+\eta<1\).
For \(t\ge b\) and all large \(N\), the singular-value counting inequality for sums bounds the number of singular values of \(W\) above \(t\) by those of \(U\) above \(\theta t\) plus those of \(E\) above \(\eta t\), since \(\|D\|\le (1-\theta-\eta)b\).
We bound the truncated count using an even smooth \(0\le f\le1\) that vanishes on \([-\beta,\beta]\) and equals one for \(|x|\ge1\).
Write \(a=\theta t\).
Replace each independent truncated centered complex pair in \(U\) by a centered Gaussian pair with the same real two-dimensional covariance, allowing degeneracy.
Also replace each zero diagonal by an independent real Gaussian of variance \(\sigma_N^2/N\), where \(\sigma_N^2\le1\) is the raw variance of the centered truncated off-diagonal.
Denote the resulting matrix by \(G_N\).
The [trace derivative argument by Fourier inversion and Duhamel's formula](Yin_C_F0360_v1.md#argument) applied to \(f(\cdot/a)\) and a rank-at-most-two Hermitian direction \(H\) gives a uniform bound \(C_k N^{-1}a^{-k}\|H\|^k\) on derivatives of orders \(1,2,3\).
Indeed \(f'\) is smooth of compact support, and rescaling its Fourier integral supplies each factor \(a^{-1}\).
At the zeroed pair, the first two Taylor terms depend linearly and quadratically on its real and imaginary coordinates, so the full covariance matching cancels them even when those coordinates are dependent.
For the diagonal the first-order term cancels.
Summing the remainders yields
\[
 \mathbb E\operatorname{tr}_N f(U/a)\le
 \mathbb E\operatorname{tr}_N f(G_N/a)+C(a^{-3}d_N+a^{-2}/N),
 \quad
 d_N=N^{-1/2}\big(1+\mathbb E[|\xi|^3\mathbf1_{|\xi|\le\sqrt N}]\big).
\]
Here Gaussian raw third moments are uniformly bounded and centering changes the truncated absolute third moment by at most a constant multiple.
For fixed \(v>0\), summing \(v^3N^{-1/2}\) over dyadic \(N\ge v^2\) gives at most \(C v^2\).
Thus \(\sum_j d_{2^j}<\infty\).

For all sufficiently large \(N\), \(\sigma_N>0\) since \(\sigma_N\to1\).
The reference \(G_N/\sigma_N\) has variance matrix with every entry \(1/N\).
Each standardized entry is a real or two-dimensional centered Gaussian with the sum of coordinate variances one, so the subexponential bound is uniform even for singular covariance.
The [Hermitian confinement theorem](../audits/literature/EYY12/Yin_U001.md#semicircle-counting-and-locations), Theorem 2.1(iii), applies to these independent upper entries without a requirement of independence within a complex entry.
It gives \(\Pr(\|G_N\|>\beta\theta b)=O_M(N^{-M})\) for every \(M>0\).
For the integral over unbounded \(t\), the same bound suffices by Cauchy--Schwarz and \(\mathbb E\|G_N\|^{2p}\le C(1+N^2)\).
The latter follows from \(\|G_N\|\le\|G_N\|_{\rm HS}\), the Gaussian fourth moments and \(2p<4\).
Indeed the integral of \(p t^{p-1}\mathbf1_{\|G_N\|>\beta\theta t}\) over \(t\ge b\) is bounded by \((\beta\theta)^{-p}\|G_N\|^p\mathbf1_{\|G_N\|>\beta\theta b}\).
The \(a^{-3}\) and \(a^{-2}\) terms are integrable against \(pt^{p-1}\) there.
Using the count at \(b\) and integrating the counts above \(b\) now gives (3), including the contribution from \(E\) by its Schatten bound.

<a id="compression"></a>
## Removing the large spectral modes in trace norm

Put \(S=|A|^{1/2}\), \(Q=\mathbf1_{A<0}\), \(J=I-2Q\) and \(C=SBS\).
The [finite cycling identity](Yin_C_F0358_v3.md#argument) gives the eigenvalues of \(P\) as those of \(JC\), with multiplicity.
For fixed \(0<\delta<1\), retain \(X\)-modes with \(|x|\le2+\delta\), writing \(S_0=S\mathbf1_{|X|\le2+\delta}\), \(K=XS\), \(K_0=X S_0\).
Let \(Z_0=Z\mathbf1_{|Z|\le3},\ Y_0=Y\mathbf1_{|Y|\le3},\ M=ZS,\ M_0=Z_0 S_0\).
Define the Hermitian matrix
\[
       C_0=K_0^*Y_0 S_0+S_0Y_0K_0+M_0^*Y_0M_0 .
\]
All factors here have uniformly bounded norm.
The negative \(A\)-modes in \(S_0\) have depth at most \(\delta\), so \(\|S_0Q\|\le\sqrt\delta\), \(\|K_0 Q\|\le3\sqrt\delta\), and \(\|M_0Q\|\le3\sqrt\delta\).
It follows that \(\|\operatorname{Im}(JC_0)\|=\|QC_0(I-Q)\|\le C_*\sqrt\delta\), where \(C_*\) is absolute.

Use \(\|\cdot\|_1\) for the unnormalized trace norm.
Let \(H_X,H_Y,H_Z\) be the sums of \(|w|^{3/2}\) over the discarded eigenvalues of the respective matrices.
We have
\[
 \|K-K_0\|_1+\|S-S_0\|_1\le C H_X,\qquad
 \|M-M_0\|_1\le C(H_X+H_Z).                                       \tag{4}
\]
For the second estimate expand \(M-M_0=Z_0(S-S_0)+(Z-Z_0)S_0+(Z-Z_0)(S-S_0)\).
The first two terms use the bounded factor.
For the last, Schatten Hölder with exponents \(3/2,3\) bounds the trace norm by \(H_Z^{2/3}(C H_X)^{1/3}\).
Young's inequality gives (4).

Conditionally on \(X,Z\), any matrices \(F,G\) fixed by that conditioning satisfy
\[
       \mathbb E_Y\|F^*YG\|_1\le C\|F\|_1
                (\operatorname{tr}_N G^*G)^{1/2}.                    \tag{5}
\]
Indeed for deterministic unit \(v,w\), upper-entry independence, centering and the two moments give \(\mathbb E_Y|v^*Yw|^2\le C/N\) by squaring each independent raw-pair contribution, bounding the squared sum of its two coefficients by twice the sum of their squares, and summing.
Apply this inequality to the rows in singular-vector coordinates of \(F,G\).
The trace norm of \(F^*YG\) is bounded by the sum of the Euclidean lengths of its rows in left singular-vector coordinates, giving (5) by Cauchy--Schwarz.

Set \(g=1+\operatorname{tr}_N(S^2+M^*M)\).
The family \(g\) is bounded in probability, since \(\mathbb E\operatorname{tr}_N S^2\le 2+(\mathbb E\operatorname{tr}_N X^2)^{1/2}=O(1)\) and \(\mathbb E Z^2=((N-1+\mathbb E\zeta_Z^2)/N)I\) independently of \(X\).
Replace \(K^*YS\) by \(K_0^*YS_0\) using the terms \((K-K_0)^*YS\) and \(K_0^*Y(S-S_0)\).
Apply (5) to the adjoint of the second term and use (4).
Apply the same argument to \(M^*YM-M_0^*YM_0\), using \((M-M_0)^*YM+M_0^*Y(M-M_0)\).
Consequently the conditional expected trace norm of the sum of all these errors, including the adjoint in the quadratic part, is bounded by \(C(H_X+H_Z)\sqrt g\).
Replacing \(Y\) by \(Y_0\) in the remaining bounded factors costs at most \(C H_Y\) in trace norm deterministically.
No conditional expectation given \(Y_0\) is used.

Choose \(\delta\) so small that \(C_*\sqrt\delta<h/2\).
By (3), \(a_j=\mathbb E(H_X+H_Y+H_Z)/2^j\) is summable.
Since the harmonic series diverges, there are increasing \(j_l\) with \(j_l a_{j_l}\to0\).
On \(\{g\le L\}\), which depends only on \(X,Z\), conditional Markov applied to the errors before the \(Y\)-cutoff and ordinary Markov for \(H_Y\) give \(j_l\|C-C_0\|_1/N_l\to0\) in probability there.
The complement has probability at most \(C/L\), so sending \(L\) to infinity gives unconditional convergence in probability.

Choose a unitary Schur basis for \(JC\), in which the diagonal entries are its eigenvalues.
For each counted root the absolute imaginary diagonal entry is at least \(h\), while that of \(JC_0\) has absolute value at most \(h/2\).
In any orthonormal basis the sum of absolute diagonal entries of a matrix is bounded by its trace norm, by trace duality against a diagonal matrix of unit phases.
Thus \(hk_N(h)/2\le\|J(C-C_0)\|_1=\|C-C_0\|_1\), proving (1).

<a id="dilation"></a>
## Global dilation of the second color

Fix \(z\notin\mathbb R\) and \(h=|\operatorname{Im}z|/4\).
Independently of the matrices take \(t\) uniform on \([0,N^{-J_0}]\), where \(J_0>2/\alpha\) is fixed.
Under \(Y\mapsto\mathrm e^tY\) the roots of \(P\) become exactly \(\mathrm e^t\lambda\).
For deterministic \(t\) the product-law total variation distance for the upper entries, including diagonals, is bounded by \(CN^2t^\alpha\) using (2).
The unconditional joint law after the dilation therefore differs by \(o(1)\) in total variation from the original joint law of the three colors.

Uniformly in each complex \(\lambda\), for \(0<r<\min(1,|z|/2)\) the event \(|\mathrm e^t\lambda-z|<r\) has probability at most \(\min(1,C_z N^{J_0}r)\).
For \(\lambda\ne0\) the corresponding interval for \(t+\log|\lambda|\) has length \(\log((|z|+r)/(|z|-r))\le C_zr\), and for \(\lambda=0\) the event is empty.
Integration over \(r=\mathrm e^{-s}\) gives \(\mathbb E_t\log^-|\mathrm e^t\lambda-z|\le C_z+J_0\log N\).
For the \(k_N(h)\) far roots before dilation this bounds the conditional expected sum divided by \(N\) by \((C_z+J_0\log N) k_N(h)/N\), which tends to zero in probability along (1).
Conditional Markov, first on the event where this bound is at most any fixed small \(\epsilon\), gives convergence in probability of that part of the loss.
The other nonreal roots after dilation satisfy \(|\operatorname{Im}(\mathrm e^t\lambda)|\le2h\) for large \(N\).
Their loss per root is bounded by \(\log^-(|\operatorname{Im}z|/2)\), and the [vanishing normalized number of nonreal roots](Yin_C_F0358_v2.md#argument) applies before dilation, which preserves whether a root is real.
Thus the normalized loss from all nonreal roots tends to zero in probability under the dilated law and, by total variation, under the original law.
Choose a further deterministic subsequence on which its exceedance probabilities at thresholds \(1/l\) are summable.
The first Borel--Cantelli lemma applies to every coupling.
The [real-root potential decomposition and full-sequence upper bound](Yin_C_F0358_v2.md#loss) and the [Hermitian comparison](Yin_C_F0358_v3.md#comparison) give the asserted limits.

<a id="example"></a>
## A second color with an atom and no moments above two

With probability \(1/2\) set the real raw entry to zero.
Otherwise choose an independent symmetric sign and magnitude \(\exp V\), where \(V\ge1\) has density proportional to \(\exp(-2v)v^{-2}\).
Rescale by a fixed positive constant to give variance one and take this law on and off the diagonal of \(Y\).
The second moment is finite by integrability of \(v^{-2}\), and each \(2+\epsilon\) moment diverges.
On the nonzero component, dilation translates \(V\) by \(t\), and its density extended by zero has bounded variation, since it is decreasing on \([1,\infty)\) with finite value at one.
Its \(L^1\) translation difference is at most \(t\) times its total variation, as follows by integrating the variation measure over intervals of length \(t\).
The atom at zero is fixed, giving (2) with \(\alpha=1\).
Both other colors may for example have fixed purely atomic upper and diagonal laws with [no moments above two](Yin_C_F0361_v1.md#atomic).

## Current assessment
[Selected decision](#decision-strip-dilation-reviewed)

## Assessment history

### Decision strip-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18T01:28 |
| status | open |
| reason | Dyadic summability of large-mode trace norms and a Schur-basis count give the strip estimate, and dilation controls the remaining ordinary logarithm under (2). |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strip count and ordinary logarithms](#statement) | Three fixed finite-second-moment laws, prescribed nonreal shifts and arbitrary cross-size coupling. |
| argument | [Summable spectral weight](#tails) | Fixed complex raw pairs, including singular covariance. |
| support | [Trace-norm comparison and root count](#compression) | Shallow negative modes and large modes of all three colors. |
| support | [Dilation and logarithmic convergence](#dilation) | A modulus for dilation of the two raw laws of the second color. |
| support | [Exactly two moments](#example) | A dilation-regular raw law with an atom at zero. |

### Decision strip-dilation-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-18T01:41 |
| status | proved |
| reason | Dyadic tails beyond the semicircle edge and a conditional trace-norm comparison control the nonreal root count, and a second-color dilation test supplies the fixed-shift determinant in its stated class. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-variance inputs and prescribed shifts](#statement) | Strip count without a regularity restriction; ordinary logarithms under the stated second-color dilation condition. |
| argument | [Complete proof from the dyadic tail estimate](#tails) | Complex and real laws with finite variance. |
| support | [Conditional scalar dilation](#dilation) | The indicated pointwise and coupling conclusions. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0372_v1.md#strip-dilation-whole-proof) | Full fixed statement and the stated limits for arbitrary atomic laws. |
