---
author: Yin
---

# Singular-value products after a rank-\(k\) perturbation and a paired block addition

<a id="statement"></a>
## Projection estimate and paired block estimate

For a complex matrix \(Z\) write \(p_j(Z)=\prod_{i=1}^j s_i(Z)\), with singular values in decreasing order, \(p_0(Z)=1\), and missing singular values set equal to zero.
For a matrix \(U\) with \(k\) columns put \(\operatorname{vol}_k(U)=\det(U^*U)^{1/2}\).
Take \(c_k=2^{3k}\binom{2k}{k}\).

Let \(T,R:\mathbb C^d\to\mathbb C^h\) with \(1\le k\le\min(d,h)\) and \(\operatorname{rank}R\le k\).
Choose any singular vector decomposition of \(T\) and let \(P\) project off the first \(k\) left singular vectors in that decomposition.
Then
\[
 p_k(PR)\le c_k p_k(T-R).
 \tag{1}
\]
The estimate is uniform in the dimensions and in the choice of singular vectors at ties.

For a square \(M\) of size \(n\), consider a simultaneous row and column addition
\[
 B=\begin{pmatrix} M&U\\ V^*&D\end{pmatrix},
 \qquad U,V\in\mathbb C^{n\times k},\quad D\in\mathbb C^{k\times k}.
\]
For \(0\le r\le n-2k\), fix a singular vector decomposition of \(M\).
Let \(Q_L\) remove its first \(r+k\) left singular vectors and \(Q_R\) remove its first \(r\) right singular vectors.
Then
\[
 p_{r+2k}(B)\ \ge\ c_k^{-1}p_r(M)
               \operatorname{vol}_k(Q_LU)\operatorname{vol}_k(Q_RV).
 \tag{2}
\]
The same fixed singular vector decomposition is used on the two sides, even at repeated singular values.
There is no restriction on \(D\) or on dependence between the two borders.

<a id="argument"></a>
## A coefficient of the compressed volume polynomial

Set \(E=T-R\).
If \(p_k(PR)=0\), (1) follows immediately.
If \(p_k(T)=0\), the chosen first \(k\) left singular vectors contain \(\operatorname{ran}T\), so \(PR=-PE\) and contractivity on exterior powers gives (1).
Assume henceforth \(p_k(PR)p_k(T)>0\), which entails \(\operatorname{rank}R=k\).

Let \(F\) be a frame of \(k\) orthonormal top right singular vectors of \(T\) paired with the chosen left singular vectors, and let \(G\) be an orthonormal frame of \(\operatorname{ran}R^*\).
Write \(\mathcal V=\operatorname{span}(F,G)\), of dimension \(d_0\le 2k\), and \(\mathcal H=\operatorname{ran}(TF)\oplus\operatorname{ran}(PR)\), of dimension \(2k\).
The two summands are orthogonal.
Both \(TF\) and \(RG\) have columns in \(\mathcal H\).
In orthonormal bases of \(\mathcal V,\mathcal H\) let \(C\) and \(D_0\) denote \(T\) and \(E\) restricted to \(\mathcal V\) and orthogonally projected onto \(\mathcal H\).
In particular \(\operatorname{rank}(C-D_0)\le k\).
Use \(F,G\) also for the coordinates of the frames in \(\mathcal V\).

The square matrix \(B_0=[CF,(C-D_0)G]\) satisfies
\[
 |\det B_0|=p_k(T)p_k(PR).
 \tag{3}
\]
Indeed the volume of the first \(k\) columns is \(p_k(T)\), and the projections of the last \(k\) columns orthogonal to the first \(k\) are the columns of \(PRG\).
Their volume is \(p_k(PR)\) because \(R=RGG^*\).
Thus \(S=CC^*+D_0D_0^*\) is positive definite, since the columns of \([C,D_0]\) span all columns of \(B_0\).
Put \(X=S^{-1/2}C\), \(Y=S^{-1/2}D_0\).
Then \(XX^*+YY^*=I_{2k}\) and the operator \([X,Y]\) has norm one.
The factorization
\[
 S^{-1/2}B_0=[X,Y]\begin{pmatrix}F&G\\0&-G\end{pmatrix}
\]
gives \(\|S^{-1/2}B_0\|\le2\), by the triangle inequality applied to the diagonal and off-diagonal block maps in the last factor.
Consequently \(|\det B_0|\le 2^{2k}\det(S)^{1/2}\).

On the space \(\ker (X-Y)^*\) of dimension at least \(k\), one has \(X^*v=Y^*v\) and \(\langle XX^*v,v\rangle=\|v\|^2/2\).
By the min-max principle the decreasing eigenvalues of \(XX^*\) obey \(\lambda_k\ge1/2\ge\lambda_{k+1}\) and all belong to \([0,1]\).
Using \(YY^*=I_{2k}-XX^*\), the coefficient of \(t^k\) in
\[
 \det(tXX^*+YY^*)=\prod_{i=1}^{2k}(t\lambda_i+1-\lambda_i)
\]
is at least \(2^{-2k}\).
Indeed the term choosing \(t\lambda_i\) from the first \(k\) factors and \(1-\lambda_i\) from the others has at least that value, and all other contributions are nonnegative.

Multiplication by \(\det S\) gives the corresponding coefficient of \(\det(tCC^*+D_0D_0^*)\).
Cauchy--Binet applied to \([\sqrt t\,C,D_0]\) for \(t\ge0\) expresses that coefficient as the sum of \(|\det[C_I,(D_0)_J]|^2\) over \(k\)-column subsets \(I,J\) of the two matrices.
Each such determinant is at most \(p_k(T)p_k(E)\) in modulus: the combined volume is at most the product of the two column volumes, which are bounded by the respective exterior operator norms under restriction and projection.
Counting the terms gives
\[
 2^{-2k}\det S\le \binom{d_0}{k}^{2}p_k(T)^2p_k(E)^2 .
\]
Combining this bound with (3) and cancelling \(p_k(T)>0\) proves (1).

<a id="block-application"></a>
## Applying the projection estimate to a paired addition

If \(p_r(M)=0\), (2) follows from nonnegativity.
Use the chosen singular vector bases to write \(M=\operatorname{diag}(H,T)\) with the leading \(r\) singular values in \(H\), and write the two transformed border columns as \(U=(U_1^{\mathsf T},U_2^{\mathsf T})^{\mathsf T}\) and \(V=(V_1^{\mathsf T},V_2^{\mathsf T})^{\mathsf T}\).
The convention for \(r=0\) omits \(H\) and its correction.
Put \(A=D-V_1^*H^{-1}U_1\), and first assume \(A\) invertible.

As in the [block compression](../drafts/Yin_D_F0009.md#auxiliary-block-interface), compress \(\bigwedge^{r+2k}B\) to the coordinate exterior bases containing the \(r\) head coordinates, any \(k\) tail coordinates and all \(k\) added coordinates.
Two Schur eliminations show that the entry indexed by two tail subsets \(I,J\) equals
\[
 \det H\,\det A\,
 \det\bigl((T-U_2A^{-1}V_2^*)_{I,J}\bigr).
\]
Thus \(p_{r+2k}(B)\ge p_r(M)|\det A|\,p_k(T-R_0)\) for \(R_0=U_2A^{-1}V_2^*\).
Apply (1) to \(T,R_0\), with \(P\) removing the top \(k\) left singular vectors of this tail in the chosen decomposition.
On the one-dimensional space \(\bigwedge^k\mathbb C^k\), the middle exterior map of \(PU_2A^{-1}V_2^*\) is multiplication by \(\det A^{-1}\).
It follows that \(|\det A|p_k(PR_0)=\operatorname{vol}_k(PU_2)\operatorname{vol}_k(V_2)\), including the case where a column volume vanishes.
The two volumes are exactly those in (2).
For singular \(A\), replace \(D\) by \(D+\epsilon I_k\) along a sequence of positive \(\epsilon\downarrow0\) for which \(A+\epsilon I_k\) is invertible.
The right side of (2) is unchanged, and singular values on the left are continuous.

## Scope for Wigner polynomial determinants

The [paired scalar inequality](../ledger/Yin_L_F0067_v2.md#paired-border-growth) supplies the sharper scalar constant \(2\).
The [earlier comparison with Luo, Han and Zhang](../drafts/Yin_D_F0009.md#auxiliary-block-interface) identifies their Schatten-norm estimate and the separate singular-product question.
This argument resolves that deterministic question at every fixed auxiliary size.
For use in [F0012](../tasks/Yin_T_F0012_v3.md#contract), iteration still requires lower probability estimates for the two projected border volumes under the actual shared Wigner entries and quantitative control of the last few directions where \(r>n-2k\).
A linearization may have coefficient ranges forcing a projected volume to vanish, in which case (2) gives only the nonnegative lower bound zero.
The existing [planar defect criterion](Yin_C_F0186_v27.md#statement) states the summability needed for the full-sequence Brown conclusion in the real fourth-moment model.

## Assessment history

### Decision paired-volumes-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T04:54 |
| status | proved |
| reason | Independent review verified the exterior-volume comparison and the paired block estimate in the stated dimensions, including ties and singular blocks. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Projection and paired block estimates](#statement) | Both deterministic inequalities, with the stated constant, singular-vector choices and dimension restrictions. |
| argument | [Projection proof](#argument) | Compressed mixed volume and the central determinant coefficient. |
| support | [Block deduction](#block-application) | Exterior compression, both Schur eliminations and the limiting argument at a singular block. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0356_v1.md#finding) | Both deterministic inequalities at their precise scope. |

## Current assessment

[Selected decision](#decision-paired-volumes-reviewed)
