---
author: Yin
---

# Ordinary determinants of a shared-input Wigner product at a prescribed nonreal shift

<a id="statement"></a>
## Two hypotheses on the input laws

Use the [fixed-law Hermitian Wigner model](../tasks/Yin_T_F0014_v1.md#contract) with three independent colors in each size and arbitrary coupling across sizes.
All unspecified raw laws may be complex or real, atomic, and have only finite second moments as in that contract.
For \(c\ge2\) write
\[
 A=cI+X,\qquad B=XY+YX+ZYZ,\qquad P=AB.
\]
Let \(u_c(z)=\tau\log|(c+s_x)(s_xs_y+s_ys_x+s_zs_ys_z)-z|\).
For each prescribed \(z\notin\mathbb R\) the almost-sure equality
\[
 \limsup_N N^{-1}\log|\det(P_N-zI)|=u_c(z)                         \tag{1}
\]
holds under either of the following hypotheses.

1. \(c>2\), \(X\) is real symmetric with any admissible two-moment laws, and \(Y\) is a normalized GOE or GUE.
   There is no further restriction on \(Z\).
   There is a deterministic subsequence of dyadic sizes, depending only on \(X,c\), along which convergence holds almost surely for each prescribed \(z\).
2. \(c\ge2\), \(\|X_N\|\) is bounded in probability, and the **unnormalized** trace \(T_N=\operatorname{Tr}(cI+X_N)_-\) converges to zero in probability.
   There is no further restriction on \(Y,Z\).
   These assumptions hold in particular for \(c=2\) and \(X\) normalized GUE.
   The logarithms converge locally uniformly off the real axis in probability, and along a deterministic subsequence this convergence is almost sure on all compact subsets there.

Here \(H_-=\max(-H,0)\).
The [finite and free word-chain identities](../ledger/Yin_L_F0061_v2.md#linearization-transfer) give (1) for the associated fixed affine pencil with the logarithms divided by the auxiliary size.

<a id="argument"></a>
## A summable count beyond a fixed gap

In case 1 let \(b_N=N^{-1}\#\{\lambda(X_N)\le-c\}\), counting multiplicities.
We prove \(\sum_{j\ge1}\mathbb E b_{2^j}<\infty\).
Choose \(2<a<c\) and a smooth nonincreasing \(f\) equal to one on \((-\infty,-c]\) and zero on \([-a,\infty)\).
Then \(b_N\le\operatorname{tr}_N f(X_N)\), with \(\operatorname{tr}_N=\operatorname{Tr}/N\).

Truncate the raw real strict-upper entries \(\xi\) at \(|\xi|\le\sqrt N\).
Each altered pair costs rank at most two, so the expected change of the normalized trace test is at most \(N\Pr(|\xi|>\sqrt N)\) by rank interlacing and the unit variation of \(f\).
Centering the truncated entries subtracts \(\mu_N({\bf 1}{\bf 1}^t-I)/\sqrt N\), where \(\mu_N=\mathbb E[\xi{\bf1}_{|\xi|\le\sqrt N}]\) and \({\bf 1}\) is the all-ones column.
The rank-one part and scalar shift cost at most \(1/N+\|f'\|_\infty|\mu_N|/\sqrt N\).
Set \(\sigma_N^2=\operatorname{Var}(\xi{\bf1}_{|\xi|\le\sqrt N})\le1\).

Replace the centered truncated pairs by Gaussian ones of the same variance and the diagonals by centered Gaussian diagonals of raw variance \(2\sigma_N^2\).
For a rank-\(r\) Hermitian direction \(H\), the \(k\)-th derivative of \(\operatorname{tr}_N f(M+tH)\) is at most \(C_f(r/N)\|H\|^k\) in absolute value for \(1\le k\le3\), uniformly in \(M,t\).
Indeed its first derivative is \(\operatorname{tr}_N(H f'(M+tH))\).
Fourier inversion of the smooth compactly supported \(f'\) and Duhamel's formula bound the next derivatives by the trace norm of \(H\), the remaining operator norms, and finite Fourier moments of \(f'\).
Taylor replacement through order two for the pairs and order one for the diagonals therefore changes the expected test by at most
\[
 C_f\left[N^{-1/2}\left(1+\mathbb E|\xi|^3{\bf1}_{|\xi|\le\sqrt N}\right)
                      +N^{-1}(1+\mathbb E|\zeta|^2)\right],
\]
where \(\zeta\) is the original raw diagonal.
This step uses the independence of each replacement coordinate from the matrix with that coordinate removed.

The comparison matrix has law \(\sigma_N G_N\) for normalized GOE \(G_N\).
For either standard GOE or GUE one has \(\mathbb E\lambda_{\max}(\pm G_N)\le2\).
Indeed compare \(v^*G_Nv\) on the unit sphere with \(2\operatorname{Re}(g^*v)/\sqrt N\) for a standard real or circular complex Gaussian vector \(g\) with \(\mathbb E\|g\|^2=N\).
For GOE the respective variances of increments at \(v,w\) are \(4(1-(v^tw)^2)/N\) and \(4\|v-w\|^2/N\).
For GUE they are \(2(1-|v^*w|^2)/N\) and \(2\|v-w\|^2/N\).
The first is at most the second in either case.
The Gaussian comparison of expected maxima follows on finite nets by interpolating the expected function \(\beta^{-1}\log\sum_i e^{\beta x_i}\) between independent Gaussian vectors: its derivative toward the larger increments is \(\beta/4\) times the expectation of their variance differences averaged with the products of the two softmax weights.
Letting \(\beta\to\infty\) and taking dense nets proves the bound \(2\mathbb E\|g\|/\sqrt N\le2\).
The extreme eigenvalues are \(\sqrt{2/N}\)-Lipschitz in independent standard real Gaussian coordinates by the Hilbert--Schmidt inequality.
Thus [Gaussian concentration](Yin_C_F0186_v8.md#goe-concentration) bounds \(\Pr\{\lambda_{\min}(\sigma_N G_N)<-a\}\) by \(e^{-c_aN}\), with the same estimate for the expected normalized trace test.

Along \(N=2^j\), both \(\sum_j N\Pr(|\xi|>\sqrt N)\) and \(\sum_j N^{-1/2}\mathbb E[|\xi|^3{\bf1}_{|\xi|\le\sqrt N}]\) are finite.
For each raw magnitude \(t\), summing the corresponding geometric series gives at most \(C t^2\) in each case, and Tonelli's theorem applies.
This proves the claimed summability of \(\mathbb E b_{2^j}\).
Since \(\sum_j j^{-1}=\infty\), there are increasing \(j_l\) with \(\sum_l j_l\mathbb E b_{2^{j_l}}<\infty\).

<a id="radius"></a>
## Gaussian dilation of the independent color

In standard real Gaussian coordinates for \(Y_N\), write \(Y_N=R_NY_N^\circ\) with \(R_N=\chi_D/\sqrt D\) independent of \(Y_N^\circ,X_N,Z_N\).
Here \(D=N(N+1)/2\) for GOE and \(D=N^2\) for GUE.
By homogeneity the eigenvalues of \(P_N\) equal \(R_N\lambda\), with \(\lambda\) ranging over the eigenvalues formed using \(Y_N^\circ\).
The number of these nonreal eigenvalues is at most \(2Nb_N\) by the [finite count for a product](Yin_C_F0358_v2.md#argument).
The density of \(\log R_N\) is bounded by \(C\sqrt D\le CN\), since the density is proportional to \(e^{Dt-D e^{2t}/2}\), has its maximum at zero, and its normalizing constant is given by the chi density and Stirling's bounds.
For \(0<r<\min(1,|z|/2)\), the event \(|R_N\lambda-z|<r\) requires \(R_N|\lambda|\in(|z|-r,|z|+r)\).
Its probability is at most \(\min(1,C_z Nr)\), uniformly in \(\lambda\), including the empty event for \(\lambda=0\).
Integrating this estimate gives \(\mathbb E_{R_N}\log^-|R_N\lambda-z|\le C_z+\log N\).
Consequently the expected normalized sum of negative logarithmic distances from \(z\) to the nonreal roots is at most \(2(C_z+\log N)\mathbb E b_N\).
It tends to zero almost surely along \(N=2^{j_l}\) for the random sum itself, by summability of these expectations.
The [ordinary root-potential identity](Yin_C_F0358_v2.md#loss) now gives convergence on that subsequence and the upper bound on the whole sequence, proving (1).

<a id="negative-trace"></a>
## The trace of the negative part at the edge

In case 2 put \(S=|A|^{1/2},\ Q={\bf1}_{(-\infty,0)}(A),\ H=SQ,\ C=SBS\).
Then \(\|H\|_{\rm HS}^2=T_N\).
For any independent Hermitian Wigner color \(W\) in this model and deterministic \(D\ge0\),
\[
             \mathbb E[W D W]\ \le\ K_W(\operatorname{Tr}D/N)I.
\]
Indeed expanding \(v^*Ww\) in the independent centered upper entries and diagonals gives \(\mathbb E|v^*Ww|^2\le K_W\|v\|^2\|w\|^2/N\), by bounding the squared sum of the two coefficients of each conjugate pair by twice their squared moduli.
Diagonalize \(D\) and sum this bound.
In particular \(\mathbb E[W^2]\le K_W I\).

Conditional on \(X\), the squared Hilbert--Schmidt norms of \(YH,ZH,YXH\) have expectations at most \(K_Y T_N,K_ZT_N,K_Y\|X\|^2T_N\), respectively.
Each tends to zero in probability by conditional Markov on the event where the corresponding upper bound is small.
It follows also that \(\|XYH\|_{\rm HS}\to0\) in probability by tightness of \(\|X\|\).
Conditional on \(X,Z\) the covariance estimate gives
\[
       \mathbb E_Y\|ZYZH\|_{\rm HS}^2
            \le K_Y(\operatorname{Tr}Z^2/N)\|ZH\|_{\rm HS}^2.
\]
The trace factor is bounded in probability by its bounded expectation, so the right side tends to zero in probability.
A further conditional Markov bound proves \(\|BH\|_{\rm HS}\to0\) in probability.
As \(\|S\|\) is bounded in probability, \(\|CQ\|\le\|S\|\|BH\|_{\rm HS}\to0\) in probability.
The [exact negative-subspace comparison](Yin_C_F0358_v3.md#sufficient) bounds the distance of its determinant factor from minus the identity in operator norm by \(2\|CQ\|/|\operatorname{Im}z|\).
Thus the factor's normalized log determinant tends to zero uniformly in probability on each compact set away from the real axis, since every singular value lies between \(1-\epsilon\) and \(1+\epsilon\) when that distance is at most \(\epsilon<1\).
The Hermitian comparison logarithm already has its locally uniform almost-sure limit.
A deterministic subsequence along which \(\|CQ\|\to0\) almost surely gives locally uniform almost-sure convergence there.
The [whole-sequence upper bound](Yin_C_F0358_v2.md#loss) then yields (1) for each prescribed \(z\).

<a id="gue-edge"></a>
## A trace estimate for the normalized GUE

Take \(c=2\) and \(X_N\) to be normalized GUE.
The preceding Gaussian maximum and concentration estimates show that \(\|X_N\|\) is tight and \(\|(2I+X_N)_-\|=O_{\mathbb P}(N^{-1/2})\).
For \(w=-2+i\eta\), \(0<\eta\le1\), let \(R=(X_N-wI)^{-1}\) and \(m=\operatorname{tr}_N R\).
Normalized GUE can be written \(N^{-1/2}\sum_\alpha g_\alpha H_\alpha\) in a real Hilbert--Schmidt orthonormal basis of the Hermitian matrices, with independent standard real Gaussians \(g_\alpha\).
The identity \(\sum_\alpha H_\alpha M H_\alpha=(\operatorname{Tr}M)I\) follows using the diagonal units and the real and imaginary Hermitian off-diagonal basis elements.
Gaussian integration by parts in \(\operatorname{tr}_N X_NR=1+wm\), with \(\partial_\alpha R=-N^{-1/2}RH_\alpha R\), gives \(\mathbb E m^2+w\mathbb E m+1=0\).
The Gaussian Poincaré inequality gives \(\mathbb E|m-\mathbb E m|^2\le 1/(N^2\eta^4)\), since the squared gradient is \(N^{-3}\|R^2\|_{\rm HS}^2\le N^{-2}\eta^{-4}\) by Parseval in the complexification of the basis.
Completing the square in the quadratic for \(\mathbb E m\) gives
\[
     |\mathbb E m+w/2|\le C\bigl(\sqrt\eta+N^{-1}\eta^{-2}\bigr).
\]
Each eigenvalue in \([-2-\eta,-2+\eta]\) contributes at least \(1/(2N\eta)\) to \(\operatorname{Im}m\).
For \(\eta=N^{-2/5}\) the expected count there is at most \(C N^{2/5}\).
With probability tending to one all eigenvalues below \(-2\) lie in this window by the extreme-eigenvalue bound.
Multiplying their \(O_{\mathbb P}(N^{2/5})\) count by their \(O_{\mathbb P}(N^{-1/2})\) maximal depth proves \(T_N=O_{\mathbb P}(N^{-1/10})\).

## Current assessment
[Selected decision](#decision-shared-product-reviewed)

## Assessment history

### Decision shared-product-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:54 |
| status | open |
| reason | A summable fixed-gap count and Gaussian dilation control the nonreal roots, while covariance bounds give a separate negative-trace criterion at the edge. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two fixed-shift conclusions](#statement) | Original Wigner laws, arbitrary coupling and the exact affine transfer. |
| argument | [Fixed-gap count](#argument) | Smooth comparison along dyadic dimensions under only second moments on the real first color. |
| support | [Gaussian dilation](#radius) | Small distances to each prescribed nonreal shift. |
| support | [Negative trace](#negative-trace) | Arbitrary original second and third colors including heavy tails. |
| support | [GUE edge](#gue-edge) | A concrete free-edge first color with vanishing unnormalized negative trace. |

### Decision shared-product-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:03 |
| status | proved |
| reason | A gap and radial estimate or an unnormalized negative-trace bound establish the prescribed nonreal determinant limsup in the two stated models. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed theorem](#statement) | A gap and radial estimate or an unnormalized negative-trace bound establish the prescribed nonreal determinant limsup in the two stated models. |
| argument | [Complete argument](#argument) | The stated input laws, parameter sets and coupling requirements. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0368_v1.md#shared-product-whole-proof) | Full scope of this version. |
