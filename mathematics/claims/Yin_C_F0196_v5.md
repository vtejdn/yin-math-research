---
author: Yin
---

# Independent borders of the exterior compression and the restricted singular maps

<a id="statement"></a>
## Conditional compression, border moments and planar singular bounds

Use the fixed original real Wigner model in [C196v4](Yin_C_F0196_v4.md#statement), with finite fourth moments off the diagonal and finite second moments on the diagonal.
Fix \(R,d>0\), a sufficiently small fixed \(\lambda>0\) permitted by its cross-block estimate, and a deterministic ordered set \(I\) of size \(k=\lfloor\lambda N\rfloor\).
Write \(J=I^c,\ m=N-k,\ V=B_{JI}\), \(K=\ker V^T\) in \(\mathbb C^m\), and denote the orthogonal projection onto \(K\) by \(P_K\).
Set
\[
 D(z)=A_{JJ}B_{JJ}+2B_{JJ}A_{JJ}-zI_m .
\]
Then \(V\) has iid entries of law \(\xi/\sqrt N\), where \(\xi\) has the raw off-diagonal law of \(B\), and \(V\) is independent of the two square \(J\) blocks.
Identifying \(H=\ker(h\mapsto(h_I,(Bh)_I))\) with \(K\), the exterior operator \(C_H-zI_H\) in [D42](../drafts/Yin_D_F0042.md#repeated-interior) equals \(P_K D(z)|_K\).

Let \(v_1,\ldots,v_k\) be the columns of \(V\), \(V_l=[v_1,\ldots,v_l]\), \(K_l=\ker V_l^T\), and
\[
 Q_l(z)=(-1)^l\det
 \begin{pmatrix}D(z)&V_l\\V_l^T&0\end{pmatrix},\qquad
 Q_0(z)=\det D(z).
\]
Conditional on the square blocks and the first \(l-1\) border columns, write \(P\) for projection onto \(K_{l-1}\), \(D_{l-1}=P D(z)|_{K_{l-1}}\), and \(G_{l-1}=\det(V_{l-1}^TV_{l-1})\), with \(G_0=1\).
Use real orthonormal bases of these conjugation-invariant spaces when transposing.
Define the symmetric complex matrix
\[
 S_{l-1}=\tfrac12(T_{l-1}+T_{l-1}^T),\qquad
 T_{l-1}=G_{l-1}P\,\operatorname{adj}(D_{l-1})P ,
\]
where the middle operator is extended by zero on \(K_{l-1}^\perp\).
If \(V_{l-1}\) has deficient column rank, take both matrices zero.
Writing \(\mathbb E_{l-1}\) for this conditional expectation, one has the exact first and centered second moments
\[
 \begin{split}
 \mathbb E_{l-1} Q_l(z)&=-N^{-1} Q_{l-1}'(z),\\
 \mathbb E_{l-1}|Q_l-\mathbb E_{l-1}Q_l|^2
 &=N^{-2}\left(2\sum_{i\ne j}|(S_{l-1})_{ij}|^2+
       (\mathbb E\xi^4-1)\sum_i|(S_{l-1})_{ii}|^2\right).
 \end{split}
 \tag{Conditional-border-moments}
\]
In particular \(\mathbb E_V Q_k(z)=(-1/N)^k Q_0^{(k)}(z)\) for every deterministic square-block realization.
If additionally the law of \(\xi\) is symmetric, the unweighted conditional average also satisfies
\[
 \mathbb E_V[\det(P_KD(z)|_K)\mid \operatorname{rank}V=k]
     =\frac{(-1)^k}{m(m-1)\cdots(m-k+1)}Q_0^{(k)}(z)
 \tag{Symmetric-border-mean}
\]
whenever the conditioning event has positive probability, with the square blocks fixed throughout.

Put \(t=N^{-d}\).
There is a random Borel set \(\mathcal Z_N\subset\{|z|\le R\}\) determined by the two square blocks and \(V\).
Outside an event of probability at most \(C_R N^{-3}+C_R e^{-c_R N^{1/8}}\), it satisfies \(|\mathcal Z_N|\le C_{R,d,\lambda}/\log N\).
For every \(z\) outside this set in the disk let \(E_{\rm r}\) and \(E_{\rm l}\) be the right and left singular subspaces of \(D(z)\) for values at most \(t\).
There is a fixed \(\sigma>0\) such that, in both spaces \(E\),
\[
 \|V^T e\|\ge \sigma\|e\|\quad(e\in E),
 \qquad
 \inf_{\substack{h\in K\\ \|h\|=1}}\operatorname{dist}(h,E)
 \ \ge\ \frac{\sigma}{\sqrt{\sigma^2+\|V\|^2}} .
 \tag{Two-sided-angles}
\]
When \(E=0\), the first inequality is vacuous and the distance is one.
Consequently for every unit \(h\in K\),
\[
 \|D(z)h\|,\ \|D(z)^*h\|
 \ \ge\ t\frac{\sigma}{\sqrt{\sigma^2+\|V\|^2}}
 \ \ge\ c_{d,\lambda}N^{-d-2}.
 \tag{Preprojection-floors}
\]
In particular any unit \(h\in K\) with \(\|P_KD(z)h\|\le u\) has
\(\operatorname{dist}(D(z)h/\|D(z)h\|,\operatorname{ran}V)\le C N^{d+2}u\), and the adjoint assertion holds as well.
The contribution of the removed parameters to the original \(N\)-dimensional [loss \(D_N\)](Yin_C_F0186_v27.md#clipping-definition) has
\[
 \sum_N\Pr\!\left\{\int_{\mathcal Z_N}D_N(z)\,dA(z)>b\right\}<\infty
 \qquad(b>0).
\]
The same conclusions allow any coupling across sizes and the additional [restriction to \(F_N(z)^c\)](Yin_C_F0186_v29.md#statement).
The distance of \(D(z)h/\|D(z)h\|\) from \(\operatorname{ran}V\) for an adaptively chosen \(h\in K\) remains uncontrolled from below.

## Current assessment

[Selected decision](#decision-independent-border-reviewed)

## Assessment history

### Decision independent-border-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T03:50 |
| status | open |
| reason | The new independent-border representation, conditional moments and simultaneous preprojection floors are submitted for whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-law statement](#statement) | Independent bordering of the exterior compression, conditional polynomial moments and two-sided exclusion of the principal-block small singular directions outside a small planar set. |
| argument | [Complete candidate](#argument) | Compression identity, repeated border expansion, sign symmetries, restricted rectangular small ball and uniform integrated logarithmic budget. |
| dependency | [Rectangular small-ball theorem](../audits/literature/KM15/Yin_U001.md#km15-u001) | Uniform lower singular value for a tall matrix of iid isotropic real rows with uniform linear-form L2/L1 bound. |
| dependency | [Sparse truncation](Yin_C_F0198_v1.md#sparse-truncation) | Bounded truncated input norms and few altered entries with summable original-law exceptions. |
| dependency | [Arbitrary-set loss envelope](Yin_C_F0186_v29.md#argument) | Original logarithmic loss on matrix-dependent planar sets of vanishing area. |

### Decision independent-border-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T03:57 |
| status | proved |
| reason | Independent review confirms the original-law border moments, normalization and simultaneous preprojection singular bounds outside a disk set of summably negligible loss. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All polynomial identities, singular and distance estimates, exceptional probabilities, and the summable loss claim. |
| argument | [Complete proof](#argument) | Compression and successive determinant expansions, conditional averaging, restricted tests, planar deletion and the original loss. |
| dependency | [Wigner model and observation map](Yin_C_F0196_v4.md#statement) | Fixed entry laws, deterministic cut, and kernel of the observation map. |
| dependency | [Exterior compression](Yin_C_F0194_v36.md#fixed-interior-factorization) | Definition of the operator on the observation kernel. |
| dependency | [KM15 source unit](../audits/literature/KM15/Yin_U001.md#km15-u001) | Theorem 1.4 on isotropic iid real rows, its normalization, aspect ratio and conditional application. |
| dependency | [Sparse truncation](Yin_C_F0198_v1.md#sparse-truncation) | Finite-moment model, uniform truncated norms, marked-coordinate count and rank comparison. |
| dependency | [Loss definition](Yin_C_F0186_v27.md#clipping-definition) | Normalized nonnegative original-matrix excess with the finite-eigenvalue convention. |
| dependency | [Arbitrary-set envelope](Yin_C_F0186_v29.md#argument) | Uniform original-law upper event, translated logarithms and measurable-set bound. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0203_v5.md#independent-border-whole-proof) | Independent verification of the statement, the full argument and the scope of the inputs used. |

<a id="argument"></a>
## Compression and successive border columns

Block multiplication gives
\[
 (AB+2BA-zI)_{JJ}
  =D(z)+A_{JI}V^T+2V A_{IJ}.
\]
The final term is killed by projection onto \(K\) on the left, while the middle term vanishes on \(K\) on the right.
All other coordinates of \(H\) vanish on \(I\).
The strict off-diagonal entries of \(B\) crossing from \(I\) to \(J\) belong to distinct independent upper pairs, disjoint from both square blocks.
This proves the claimed identification and independence.

With real orthonormal frames adapted to \(K_l\oplus\operatorname{ran}V_l\), a determinant expansion in the \(l\) border rows and columns gives
\[
 Q_l=\det(V_l^T V_l)\det(P_{K_l}D(z)|_{K_l})
\]
on full column rank.
Indeed the border coordinates in the second subspace give a square determinant with absolute value \(\det(V_l^T V_l)^{1/2}\), and pairing the row and column expansions contributes the sign \((-1)^l\).
The determinant defining \(Q_l\) vanishes at every rank-deficient \(V_l\).
If \(V_{l-1}\) has full column rank, set \(y=Pv_l\).
When \(y\ne0\), the new Gram determinant is \(G_{l-1}\|y\|^2\) by an orthogonal basis change of the border span or the Gram Schur complement.
The determinant compressed further onto \(K_{l-1}\cap y^\perp\) equals \(y^T\operatorname{adj}(D_{l-1})y/\|y\|^2\), by choosing the final basis vector \(y/\|y\|\) and expanding its diagonal cofactor.
Thus \(Q_l=v_l^T T_{l-1} v_l=v_l^T S_{l-1} v_l\).
For \(y=0\) the same identity follows since both sides vanish, and it also holds by definition after an earlier rank failure.
In particular no invertibility or condition-number hypotheses on \(D(z)\) are necessary.

Because \(v_l\) has centered independent entries of variance \(1/N\), its conditional quadratic form has mean \(N^{-1}\operatorname{Tr}T_{l-1}\).
On full rank, \(Q_{l-1}=G_{l-1}\det D_{l-1}\) and \(D_{l-1}'=-1\) on its domain.
The determinant derivative is minus its adjugate trace, yielding the first conditional formula, including the identically zero rank-deficient case.
The centered raw quadratic form is a sum of diagonal terms \(S_{ii}(\xi_i^2-1)\) and off-diagonal terms \(2S_{ij}\xi_i\xi_j\) for \(i<j\).
All distinct terms are pairwise orthogonal in complex \(L^2\) by centering and independence, even with a nonzero third moment.
This yields the stated second formula after dividing by \(N^2\).
Each coefficient of \(Q_l\) has degree at most two in each independent column separately and has finite second moment by the fourth moment assumption.
Iterating expectations in the polynomial identity, coefficient by coefficient, proves the derivative mean.

For the extra symmetric-law assertion choose an orthonormal frame \(Y\) of \(K\) on full rank and put \(r=m-k\).
The determinant \(\det(Y^TDY)\) equals \(\operatorname{Tr}((\bigwedge^r D)(\bigwedge^r P_K))\), by expanding the top exterior power of the compression.
The law of \(K\) conditional on full rank is invariant under all diagonal coordinate sign changes and all coordinate permutations.
The average of \(\bigwedge^r P_K\) is diagonal in the coordinate \(r\)-subset basis because distinct subsets have distinct sign characters.
It is a scalar matrix by the permutations, and trace one gives the scalar \(1/\binom mr\).
Hence the conditional mean is the sum of size-\(r\) principal minors of \(D\) divided by \(\binom mr\).
The coefficient of \(w^k\) in \(\det(D(z)+wI_m)=Q_0(z-w)\) computes this sum and gives the stated normalization.

<a id="restricted-small-ball"></a>
## Independent testing of both principal-block near-kernels

Condition on the two square blocks.
For a specified complex \(r\)-dimensional subspace \(E\subset\mathbb C^m\) measurable in that data, let \(E_\mathbb R\subset\mathbb R^m\) be the span of the real and imaginary parts of a complex basis.
It has dimension \(\widetilde r\le2r\) and contains both parts of each vector in \(E\).
Take an orthonormal basis of \(E_\mathbb R\) and project each raw border column \(\sqrt N v_l\) onto these coordinates.
The resulting \(k\) real rows are iid and isotropic in dimension \(\widetilde r\).
For a real unit vector \(u\) in this space, the corresponding real linear form \(X\) has \(\mathbb E X^2=1\) and \(\mathbb E X^4=3+(\mathbb E\xi^4-3)\sum_j a_j^4\le \max(3,\mathbb E\xi^4)\) in its orthonormal coefficient vector \(a\).
Hölder's inequality gives \(\mathbb E X^2\le(\mathbb E|X|)^{2/3}(\mathbb E X^4)^{1/3}\).
This verifies the dimension-uniform \(L^2/L^1\) hypothesis of [KM15, arXiv v1, Theorem 1.4](../audits/literature/KM15/Yin_U001.md#isotropic-row-lower-bound).
For some law-dependent \(\kappa,c_1,c_2>0\), whenever \(r\le\kappa k\), that theorem in its \(k^{-1/2}\) row normalization gives simultaneously on \(E_\mathbb R\)
\[
 \|V^T x\|\ge c_1\sqrt{k/N}\|x\|
\]
except with conditional probability at most \(2e^{-c_2 k}\).
The same bound holds for every \(x\in E\) by summing its squared real and imaginary components.
For \(E=0\) it holds without an exception.
For large \(N\) set \(\sigma=c_1\sqrt{\lambda/2}\).
The argument treats subspaces at fixed \(z\) from either \(D^*D\) or \(DD^*\), using only the two square blocks, with a union bound for the two tests.

To estimate the area on which \(r>\kappa k\), take the truncation with exponents \(1/16,1/8\) from [C198v1](Yin_C_F0198_v1.md#sparse-truncation).
Except with probability \(Ce^{-cN^{1/8}}\), the full truncated input norms are bounded by a fixed constant and the number of marked coordinates is at most \(N^{3/8}\).
The same upper norm bounds and mark count hold on the \(J\) principal blocks.
The difference between the original and truncated square-block polynomials has rank at most \(4N^{3/8}\) by the two product differences applied to the principal blocks.
Also \(\|A\|,\|B\|\le N^2\) except with probability \(O(N^{-3})\) by the expected squared Hilbert--Schmidt norm of each input.
Thus uniformly on the disk all but \(4N^{3/8}\) singular values of \(D(z)\) are bounded above by a fixed constant, and every singular value is at most \(3N^4+R\).
It follows that \(\sum\log^+s_i(D(z))\le C_R N\).
Writing \(\alpha_j\) for the eigenvalues of the square-block polynomial, its negative-logarithm sum is at most \(C_RN+\sum_j\log^-|z-\alpha_j|\) off the finite eigenvalue set.
Each last term integrates over the whole plane to \(\pi/2\), as follows by integration in polar coordinates.
The integrated negative-logarithm sum is therefore at most \(C'_R N\).
For \(r(z)=\#\{s_i(D(z))\le t\}\) this gives
\[
 \big|\{z:|z|\le R,\ r(z)>\kappa k\}\big|
 \le \frac{C_R N}{\kappa k\log(1/t)}
 \le \frac{C_{R,d,\lambda}}{\log N}.
\]

Include this last set in \(\mathcal Z_N\), together with parameters \(r(z)\le\kappa k\) where either restricted \(V^T\) test falls below \(\sigma\).
The sets are Borel because spectral projections for intervals of Hermitian matrices are Borel and restricted singular bounds can be tested by positivity of their compressed Hermitian forms.
Without conditioning on any truncation or upper-norm event, Fubini and the conditional KM15 bound give expected area of this latter failure set at most \(4\pi R^2 e^{-c_2k}\).
Its area exceeds \(N^{-1}\) with probability at most \(4\pi R^2 N e^{-c_2 k}\).
Together with the original good events, this proves the stated area bound and ensures \(\|V\|\le N^2\).

For \(h\) of unit norm in \(K\), put \(\beta=\|(1-P_E)h\|\).
Then \(\sigma\sqrt{1-\beta^2}\le\|V^T P_E h\|=\|V^T(1-P_E)h\|\le\|V\|\beta\).
Solving this inequality gives the claimed angular separation.
The orthogonal complement of \(E_{\rm r}\) is supported on singular values greater than \(t\) for the right action, giving \(\|D h\|\ge t\beta\).
The left action follows by the same calculation for \(D^*\).
Projecting the unit image \(D h/\|D h\|\) onto \(K\) proves the distance assertion, with its adjoint analogue.

The [arbitrary-set logarithmic envelope](Yin_C_F0186_v29.md#argument) gives a bound of the form \(C_R a+\frac a2(1+\log(\pi/a))\) for the original disk loss on every measurable subset of area \(a\le\pi\), with a simultaneous original-law exception of order \(N^{-3}\).
It applies directly to the random \(\mathcal Z_N\), whose good-event area tends to zero, even though the loss uses all original matrix entries.
For each fixed positive threshold the remaining marginal failure probabilities are summable, so first Borel--Cantelli applies under any coupling across sizes.
This proves the asserted removed-set conclusions.
Controlling the further projection of the tested image onto \(K\), or giving a negative logarithmic tail for a complex random variable from its first two border moments, requires additional input.
