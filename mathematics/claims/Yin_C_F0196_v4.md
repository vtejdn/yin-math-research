---
author: Yin
---

# The observation map on exterior near-kernels and a planar determinant bound

<a id="statement"></a>
## Original-law statement

Let \(A,B\) be the independent real symmetric Wigner inputs with fixed [fourth off-diagonal and second diagonal moments](Yin_C_F0198_v1.md#statement).
Write \(M=AB+2BA,\ D(z)=M-zI_N\).
For a deterministic coordinate set \(I\) of size \(k\) let \(J=I^c\), let \(Xh=(h_I,(Bh)_I)\), let \(H=\ker X\), and let \(\Pi\) be the complex orthogonal projection onto \(H\).
Define \(L(z)=\Pi D(z)\) and \(E_t(z)=\operatorname{ran}\mathbf1_{[0,t]}(|L(z)|)\), \(t>0\), using \(|L|=(L^*L)^{1/2}\).
The count of singular values of \(X|_{E_t}\) includes the kernel on its domain, so there are exactly \(\dim E_t\) values.
These maps and counts depend only on \(B\) and the entries of \(A\) outside \(I\times I\).
They describe the [conditional subspace at the original residual](../drafts/Yin_D_F0042.md#conditional-subspace).

There is \(\delta>0\) depending only on the laws such that the following holds for \(1\le k\le\delta N\), including varying deterministic \(k,I\).
Fix \(R>0\).
Outside an original-law event of probability at most \(C_R N^{-3}+C_R e^{-c_R N^{1/8}}\), all of the following estimates hold on the disk \(K_R=\{|z|\le R\}\).
Constants are uniform in \(k,I\) and in the positive scales \(t,u\).
The theorem holds for each prescribed \(I\), without a simultaneous assertion over all such coordinate sets.

1. \(B_{JI}\) has all its \(k\) singular values bounded below by a fixed constant.
   The full subspace count and the restricted singular values \(s_j=s_j(X|_{E_t(z)})\) satisfy
   \[
    \int_{K_R}(\dim E_t(z)-2k)_+\,dA(z)
       \le \frac{C_R N}{\log(1/t)}\quad(0<t<1),
    \qquad
    \int_{K_R}\sum_{j=1}^{\dim E_t(z)}
      \log^-\!\sqrt{t^2+s_j^2}\,dA(z)\le C_R N .
    \tag{Planar-observation}
   \]
   Here \(\log^-x=\max(0,-\log x)\), and eigenvalue parameters of a fixed finite matrix may be dropped in disk integrals.
   In particular, for \(r=\sqrt{t^2+u^2}<1\),
   \[
    \int_{K_R}\#\{j:s_j\le u\}\,dA(z)
       \le \frac{C_R N}{\log(1/r)} .
    \tag{Position-count}
   \]

2. Choose deterministic \(t_N,u_N>0\) with \(r_N=\sqrt{t_N^2+u_N^2}<1\) and \(k\log(1/r_N)/N\to\infty\).
   For the exterior-measurable set
   \[
   G_N=\{z\in K_R:\ (\dim E_{t_N}(z)-2k)_+
                      +\#\{j:s_j(X|_{E_{t_N}(z)})\le u_N\}
                          > k b_N\},\qquad
   b_N=\sqrt{\frac{N}{k\log(1/r_N)}},
   \]
   one has \(|G_N|\le C_R b_N\) on the indicated good event.
   At each remaining parameter at most \(k b_N=o(k)\) directions in \(E_{t_N}\) have observation singular value at most \(u_N\), and on their orthogonal complement the inverse onto its image has norm at most \(1/u_N\).
   The corresponding contribution to the [original extreme logarithmic loss](Yin_C_F0186_v27.md#clipping-definition) satisfies
   \[
       \sum_N \mathbb P\left\{\int_{G_N}D_N(z)\,dA(z)>v\right\}<\infty
       \qquad (v>0).
       \tag{Discarded-position-loss}
   \]
   In particular this holds with the additional indicator of \(F_N(z)^c\) from [C186v29](Yin_C_F0186_v29.md#statement).
   For macroscopic \(k\), any two fixed inverse polynomial scales satisfy the hypothesis.
   For arbitrary \(k\) it also permits \(t_N,u_N\) of size \(\exp(-H_N)\) when \(H_N\gg N/k\).
   If \(\log(1/r_N)\gg N\), the parameter set on which even a single restricted singular value is at most \(u_N\) has area \(O_R(N/\log(1/r_N))=o(1)\) and the same summable loss estimate.

These statements allow arbitrary cross-size couplings.
They estimate the cost of exceptional parameter positions and the conditioning of the surviving observation directions.
The small-ball probability of the remaining inside equations with their actual reconstructed targets is a further input to the full planar conclusion.

## Current assessment
[Selected decision](#decision-position-planar-reviewed)

## Assessment history

### Decision position-planar-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T03:03 |
| status | open |
| reason | The exact square determinant, unconditional cross-block lower bound and planar restricted-observation estimates are submitted for independent checking. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-law result](#statement) | Disk-integrated logarithmic restricted singular count, small-area position loss and the inverse on the surviving exterior subspace. |
| argument | [Complete argument](#argument) | Exterior square map, triangular determinant, sparse-tail cross-block control and a common logarithmic budget. |
| dependency | [Truncation](Yin_C_F0198_v1.md#sparse-truncation) | Uniform bounded truncated norms and sparse marked coordinates, with summable exceptions. |
| dependency | [Rectangular estimate](Yin_C_F0196_v1.md#affine-small-ball) | Independent affine sums with centered unit variance and bounded fourth moment. |
| dependency | [Planar envelope](Yin_C_F0186_v29.md#argument) | Quantitative upper envelope for the original loss on an arbitrary small-area set, including matrix-dependent sets. |

### Decision position-planar-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T03:11 |
| status | proved |
| reason | The independent review verifies the determinant identity and both integrated singular estimates, including the original-law summable loss on exceptional parameter positions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-law result](#statement) | Disk-integrated logarithmic restricted singular count, small-area position loss and the inverse on the surviving exterior subspace. |
| argument | [Complete argument](#argument) | Exterior square map, triangular determinant, sparse-tail cross-block control and a common logarithmic budget. |
| dependency | [Truncation](Yin_C_F0198_v1.md#sparse-truncation) | Uniform bounded truncated norms and sparse marked coordinates, with summable exceptions. |
| dependency | [Rectangular estimate](Yin_C_F0196_v1.md#affine-small-ball) | Independent affine sums with centered unit variance and bounded fourth moment. |
| dependency | [Planar envelope](Yin_C_F0186_v29.md#argument) | Quantitative upper envelope for the original loss on an arbitrary small-area set, including matrix-dependent sets. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0203_v4.md#position-planar-whole-proof) | The entire fixed statement, its proof and the directly inspected dependency interfaces. |

<a id="argument"></a>
## An exterior square matrix

For \(h\) supported on \(J\), the condition \((Bh)_I=0\) is \(B_{IJ}h_J=0\).
Since \(B\) is real symmetric, \(H\) therefore consists exactly of the vectors supported on \(J\) and orthogonal to \(\operatorname{ran}B_{JI}\) there.
Changes of \(A_{II}\) contribute to \(ABh\) only on \(I\) and to \((BAh)_J\) only in \(\operatorname{ran}B_{JI}\).
Consequently \(L\) is exterior-measurable.
Finite spectral calculus gives the same measurability for \(E_t\) and the restricted singular counts, also jointly in \(z\).
For example the measured restricted Gram operator is the compression of \(X^*X\) to the range of the measured spectral projector.

Suppose \(B_{JI}\) has full column rank.
Then \(X\) is onto \(\mathbb C^{2k}\), \(\dim H=N-2k\), and
\[
 T(z)h=(L(z)h,Xh)\ \in H\oplus\mathbb C^{2k}
\]
has equal source and target dimensions.
In the orthogonal domain splitting \(H\oplus H^\perp\), its lower-left block is zero and its diagonal blocks are \(C_H-zI_H,\ X|_{H^\perp}\), where \(C_H=\Pi M|_H\).
In particular \(C_H\) and the whole square map are exterior-measurable before exposing \(A_{II}\).
In orthonormal bases one has
\[
  |\det T(z)|=|\det(C_H-zI_H)|\prod_{j=1}^k s_j(B_{JI}).
  \tag{Exterior-square-determinant}
\]
Indeed the absolute determinant of \(X|_{H^\perp}\) is \((\det XX^*)^{1/2}\).
With the two outputs in the stated order,
\[
 XX^*=\begin{pmatrix}I_k&B_{II}\\ B_{II}&B_{II}^2+B_{IJ}B_{JI}\end{pmatrix}.
\]
Taking the Schur complement of \(I_k\) proves the formula.
This computation accounts for the possibly large \(B_{II}\) without assuming that all the nonzero singular values of \(X\) are bounded below.

## Original-law estimates for the coefficients

Use [C198v1](Yin_C_F0198_v1.md#sparse-truncation) with truncation exponent \(1/16\) and counting slack \(1/8\).
It sets to zero each raw coordinate exceeding \(N^{7/16}\) in absolute value, giving truncated \(A_0,B_0\) and \(M_0=A_0B_0+2B_0A_0\).
With probability at least \(1-Ce^{-cN^{1/8}}\), both truncated input norms are at most a fixed \(K\), the aggregate number of marked coordinates is at most \(N^{3/8}\), \(\operatorname{rank}(B-B_0)\le2N^{3/8}\), and \(\operatorname{rank}(M-M_0)\le4N^{3/8}\).
In addition \(\|A\|,\|B\|\le N^2\) except with probability \(O(N^{-3})\), by the expected squared Hilbert--Schmidt norm \(O(N)\) of each input.

We check the original cross block directly.
Condition on all the mark indicators of \(B\).
For mark count at most \(N^{3/8}\), remove from \(J\) every endpoint of any marked entry of \(B\), leaving \(J'\) with at least \(N-k-2N^{3/8}\) coordinates.
Conditional on these indicators, \(B_{J'I}=(B_0)_{J'I}\) has independent raw strict off-diagonal entries of the common law conditional on \(|\xi|\le N^{7/16}\).
The means can be absorbed into deterministic centers for each fixed test direction.
The centered variances tend to one and the standardized fourth moments are uniformly bounded.
For any fixed real unit \(v\in\mathbb R^k\), the [rectangular affine bound](Yin_C_F0196_v1.md#affine-small-ball) thus gives \(\|B_{J'I}v\|\ge c_0\) except with conditional probability \(e^{-c_1N}\), uniformly in the permitted indicators.
Take a real unit sphere net of mesh \(c_0/(2(K+1))\) with at most \((1+4(K+1)/c_0)^k\) points.
Choosing \(\delta>0\) sufficiently small gives \(|J'|\ge N/5\) as required by the bound and leaves an exponentially small union exception.
On \(\|B_0\|\le K\), the net extends to \(s_{\min}(B_{J'I})\ge c_0/2\).
This also holds for complex inputs by real symmetry of its Gram matrix.
Adding the other rows can only increase the least singular value.
Integrate over the indicators and add the original truncation and norm exceptions.
No fresh-entry law was conditioned on an upper or lower matrix norm.

## Planar logarithmic singular budgets

On this common good event, replace \(T(z)\) for comparison by
\[
 T_0(z)h=(\Pi(M_0-zI_N)h,\ h_I,\ (B_0h)_I)
\]
with the original projection and codomain.
The norm of this map is bounded by a constant \(C_{R,K}\) uniformly for \(z\in K_R\).
The difference \(T-T_0\) has rank at most \(6N^{3/8}\).
The crude original norm bound gives \(\|T(z)\|\le C_R(1+N^4)\) throughout the disk.
By min-max on the kernel of the difference, all but at most \(6N^{3/8}\) singular values of \(T(z)\) are at most \(C_{R,K}\).
Therefore \(\sum_j\log^+s_j(T(z))\le C_R N+O_R(N^{3/8}\log N)\le C'_R N\).
The same argument, comparing \(D(z)\) directly with \(M_0-zI_N\), gives this uniform bound for \(D(z)\) as well.

Put \(p=\dim H\), with eigenvalues \(\lambda_1,\ldots,\lambda_p\) of \(C_H\) counted algebraically.
Away from these finitely many eigenvalue parameters, the determinant identity gives
\[
 \sum_j\log^-s_j(T(z))
 \le C_R N+k\log^-(c_0/2)+\sum_{j=1}^p\log^-|z-\lambda_j|.
\]
This uses the identity \(\sum_j\log^- s_j=\sum_j\log^+s_j-\log|\det T|\).
For any complex \(\lambda\), the integral of \(\log^-|z-\lambda|\) over the whole plane is \(\pi/2\), by radial integration in the unit disk centered at \(\lambda\).
Consequently
\[
 \int_{K_R}\sum_j\log^-s_j(T(z))\,dA(z)\le C_R N .
 \tag{Square-log-budget}
\]
Identically, \(\det D(z)=\prod_{j=1}^N(\lambda_j(M)-z)\) implies the same planar logarithmic budget for \(D(z)\), by its positive-log bound.

For each \(j\le\dim E_t\), take the span of the first \(j\) ascending right singular directions of \(X|_{E_t}\), including its zero modes.
For \(h\) in that span, \(\|T(z)h\|^2=\|L(z)h\|^2+\|Xh\|^2\le(t^2+s_j^2)\|h\|^2\).
Thus the \(j\)-th ascending singular value of \(T(z)\) is at most \(\sqrt{t^2+s_j^2}\), by min-max.
The monotonicity of \(\log^-\) proves the second part of (Planar-observation); restricting the sum to \(s_j\le u\) proves (Position-count).
Also \(\operatorname{rank}(D-L)\le2k\).
Intersecting \(E_t\) with \(\ker(D-L)\) shows \((\dim E_t-2k)_+\le\#\{j:s_j(D)\le t\}\).
Apply the planar logarithmic budget for \(D\) to this count for the first inequality in (Planar-observation).
The same good event gave both budgets, so all positive scales in their stated ranges are allowed.

## Loss on the removed parameters

By (Planar-observation) and (Position-count), the area of \(G_N\) is at most \(C_R N/[k b_N\log(1/r_N)]=C_R b_N\).
The [small-area envelope on an arbitrary measurable set](Yin_C_F0186_v29.md#argument) bounds the integral of \(D_N\) on any subset of this disk of area \(m\le\pi\) by
\[
 C_Rm+\tfrac m2(1+\log(\pi/m))
\]
except with probability \(O_R(N^{-3})\), with limiting value zero for \(m=0\).
It applies to \(G_N\) despite its dependence on the outside entries, and the bound tends to zero there as \(b_N\to0\).
For each fixed threshold the exceptional probability is summable, proving (Discarded-position-loss), including its version restricted to \(F_N^c\) by positivity.
The one-singular-value assertion follows from Markov's inequality for planar area and (Position-count) at count one, followed by the same envelope.
The original-law exceptional event here is charged once for this planar comparison and is never imposed on the still-unexposed entries for an interior small-ball calculation.
The set \(G_N\) itself, the singular subspaces for its definition and the observation map are measurable before exposing those entries.
