---
author: Yin
---
# Matrix covariance criterion for several normal Gaussian coordinates over an abelian base

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded normal with diffuse compact spectral law \(\mu\), \(N=W^*(Z)\), and let \(S_1,\ldots,S_r\) be a finite standard free semicircular family free from \(N\) in its generated finite algebra \(M\) with faithful normal probability trace.
Let \(A(z,w)\) be a measurable \(q\times r\) complex matrix, \(q,r\ge1\), with \(A(w,z)=\overline{A(z,w)}\) almost everywhere.
A bar means entrywise conjugation, superscript \(t\) means transpose and superscript \(*\) means conjugate transpose.
Write \(T_j\) for the selfadjoint pure first-chaos field with noise coefficients \(A_{jl}\), so that a separated kernel \(f(z)g(w)\) in noise \(l\) represents \(f(Z)S_l g(Z)\).
The field is bounded in \(M\) exactly when
\[
  \rho_j^2=\mathop{\rm ess\,sup}_w\int\sum_{l=1}^r |A_{jl}(z,w)|^2\,d\mu(z)<\infty,
  \qquad \rho_j\le\|T_j\|\le 2\rho_j .
\]

Assume these row bounds and put \(X=(Z,T_1,\ldots,T_q)\), \(M_A=W^*(X)\), \(G=(AA^*)^{1/2}\).
With the intrinsic trace, Hilbert space and [original starred ACSY and strong dual conditions](../tasks/Yin_T_F0011_v1.md#contract), the following are equivalent.

1. \(X\) satisfies \(\mathsf A\) on its represented star-polynomial core, with actual vacuum adjoints.
2. \(X\) satisfies \(\mathsf S\) on \(L^2(M_A)\), with both dual and actual adjoint domains containing \(M_A\Omega\).
3. The scalar divided difference on \(\mathbb C[Z,Z^*]\) has an actual vacuum \(\xi_N\) in \(L^2(N)\), \(A\) has full row rank almost everywhere, and the following two integrals are finite.
   \[
   \int {\rm tr}(G(z,w)^{-2})\,d\mu^2,\qquad
   \int \frac{\|P^{-1}Q-PQ^{-1}\|_{\rm HS}^2}{|z-v|^2}\,d\mu^3,
   \quad P=G(z,w),\quad Q=\overline{G(w,v)} .
   \tag{1}
   \]
   Here \({\rm tr}\) is the unnormalized finite matrix trace and the endpoint diagonal is null.

Under these conditions the closures of the original canonical contractions and their actual adjoints contain all bounded vectors, and \(\mathsf F\) follows.
In a reduced \(q\)-color representation the \(T_j\) vacuum has one-edge coefficient \(\overline{G^{-1}e_j}\), and the \(Z\) vacuum equals \(\xi_N+H\), with two-edge coefficient
\[
 H(z,w,v)=\frac{\overline{P^{-1}Q-PQ^{-1}}}{\bar z-\bar v}.
 \tag{2}
\]
The edge isometry below gives these intrinsic vectors in the original representation.
For \(q=1\) with a single noise this recovers the criterion of [C_F0157 v2](Yin_C_F0157_v2.md#statement).
No common diagonalizing basis for the edge matrices is assumed.
The unrestricted comparison for arbitrary correlated normal tuples remains open.

## Argument

### Colored paths and the rank obstruction

The [semicircular mixed-moment formula](../audits/literature/NS06/Yin_U004.md#ns06-u004) pairs only matching colors.
Consequently the relative Wick Hilbert space in degree \(n\) is \(L^2(\mu^{n+1};(\mathbb C^r)^{\otimes n})\).
Indeed the Wick recurrence of [C_F0153](Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) creates the specified leading color and annihilates the leading edge only when its color matches, integrating the first base coefficient against \(\mu\).
After subtracting internal contractions the scalar product of two paths is the product of the base scalar products times the Kronecker deltas for their successive colors.
Base coefficients act on the endpoints, giving orthogonal path spaces whose polynomial span is dense.

Creation by row \(j\) multiplies by its coefficient vector at the new leading edge.
Its squared norm on \(f\) integrates \(|f|^2\) against the row integral at the first old endpoint, hence the operator norm is \(\rho_j\), already on degree zero.
Hermitian edge reversal gives the field as creation plus its adjoint.
Truncating the entries in modulus gives bounded fields in \(M\) by the separated-kernel construction on each noise of [C_F0157 v2](Yin_C_F0157_v2.md#argument).
With finite row bound these fields are uniformly bounded and their vacuum vectors converge in \(L^2\), hence they converge strongly on the dense bounded right multiples of the vacuum and then on all vectors.
Conversely the action of a pure first-chaos field on \(f\in N\) has coefficient vector \(A_{j\bullet}(z,w)^t f(w)\).
Testing indicators of row level sets proves necessity of the row bound.

Suppose first that \(\mathsf A\) holds in the possibly smaller \(M_A\).
The diffuse normal relation forces \(\partial_i Z^*=0\) for a field coordinate \(i\), as in the [one-field target moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests).
Embed its vacuum \(\psi_i\) into the ambient Wick space and let \(h_i(z,w)\in\mathbb C^r\) be its first-chaos projection.
The pairing with \(f(Z)T_j g(Z)\) for marginal polynomials \(f,g\) is \(\delta_{ij}\tau(f)\tau(g)\).
The products of the first-chaos coefficients with \(h_i\) are integrable by Cauchy--Schwarz, and polynomial rectangles determine finite measures on the compact base.
Thus
\[
           A(z,w)\overline{h_i(z,w)}=e_i \quad\text{almost everywhere for all }i.
 \tag{3}
\]
This forces full row rank and \(q\le r\).
The least squared norm of a solution of \(Au=e_i\) is \((G^{-2})_{ii}\), by the full-row-rank right inverse \(A^*G^{-2}\).
Integrating and summing proves the first integral in (1).

### The intrinsic noise space

Whenever the rank is full, write \(A=GV\) with \(V=G^{-1}A\) and \(VV^*=I_q\).
Both \(G\) and \(V\) obey entrywise conjugation on reversal of the base edge.
The complex-linear map \(J(z,w)=V(z,w)^t:\mathbb C^q\to\mathbb C^r\) is an isometry because \(\bar V V^t=I_q\).
It takes \(G_{j\bullet}^t\) to \(A_{j\bullet}^t\).
Tensor these maps along each successive edge, leaving degree zero fixed.
This path isometry intertwines the reduced row creations with the original ones.
It also intertwines their annihilations since each original row vector is in the range of the corresponding edge isometry and inner products with it are preserved.
It fixes the vacuum and the base multiplication action, and the reversal symmetry respects the tracial involution.

In the \(q\)-color model, the span of the vectors \(f(Z)T_jg(Z)\Omega\), \(f,g\in N\), is dense in the first chaos.
A vector \(h\) in its orthogonal complement gives \(G\bar h=0\) by the same integrable rectangle tests, hence vanishes.
The bounded reference semicirculars therefore belong to the reduced target algebra, since their vectors belong to its \(L^2\) space and conditional expectation fixes them.
Thus the reduced pair of base and fields generates the entire \(q\)-noise reference algebra.
The range of the path isometry is exactly the closure of the original target polynomial vectors, by intertwining and the cyclicity just proved.
It identifies the two intrinsic tracial representations, including their full domains and actual adjoints.
For rectangular \(A\) this argument requires generation only of the intrinsic algebra.
We henceforth use the square positive coefficient matrix \(G\), which also satisfies the original row bounds because \(G^2=AA^*\).

### Actual quadratic tests and the order of the matrices

For \(\mathsf A\), the \(Z\) derivative on the base is the scalar divided difference by the normal relation, and compression of its vacuum gives the actual scalar \(\xi_N\).
Let \(h(z,w,v)\) be the two-edge coefficient matrix of its vacuum, with rows indexing the first noise and columns the second.
For smooth \(f_0,f_2\) with positively separated supports and marginal polynomial \(f_1\), test it on \(f_0T_j f_1 T_k f_2\).
The [smooth endpoint graph argument](Yin_C_F0156_v1.md#actual-target-moment-tests) applies since all the fields are bounded, their \(Z\) derivatives vanish, and the endpoint multipliers are uniformly approximable together with their first divided differences.
The scalar contraction is zero because the endpoints have disjoint support.
The degree-two vector has entries \(f_0(z)G_{js}(z,w)f_1(w)G_{kt}(w,v)f_2(v)\).
These are in \(L^2(\mu^3)\) since the two squared row integrals at \(w\) are bounded, using the reversal symmetry for the second row.
The identities extend from bounded entry truncations by tracial \(L^2\) convergence of uniformly bounded fields and dominated convergence of the Wick coefficients.

The conditional two-field contraction on an edge \((u,w)\) uses \(\sum_l G_{jl}(u,w)G_{kl}(w,u)=(G(u,w)^2)_{jk}\).
The middle Leibniz term pairs two centered one-field factors and vanishes.
In the left endpoint derivative the surviving base contraction is at \((v,w)\), while the right endpoint derivative subtracts the contraction at \((z,w)\).
Thus the integral pairing against \(f_0(z)f_1(w)f_2(v)\) has density \((Q^2-P^2)_{jk}/(z-v)\), since \(G(v,w)=\overline{G(w,v)}=Q\).
The two-edge vector pairing has density \((P\bar h Q)_{jk}\), since \(G(w,v)^t=Q\).
Both densities are integrable on separated endpoint sets by the row bounds and Cauchy--Schwarz.
Localization of the smooth endpoint tests and density of the middle polynomials give the equality almost everywhere off the null endpoint diagonal.
Therefore \(P\bar h Q=(Q^2-P^2)/(z-v)\) and \(h=H\) as in (2).
This establishes necessity of the second integral with its specified matrix order.

### Contractions with a single inserted color

On the reference star-polynomial core write \(\partial_l S_t=\delta_{lt}1\otimes1\) for the free derivation that kills the base.
On a Wick word its Leibniz expansion cuts exactly the edges of color \(l\) and leaves the two remaining subpaths on the two tensor legs.
One sees this by differentiating the colored recurrence above, where terms removing an internal matching pair cancel.
For a Hilbert tensor \(\beta_l\) let \(I_{\beta_l}\partial_l\) insert \(\beta_l\) into those cuts by the outer bimodule actions.
The following estimate applies to \(\delta_\beta=\sum_l I_{\beta_l}\partial_l\) when all tensors have total relative degree exactly \(n=0\) or \(1\).
Put \(B^2=\sum_l\|\beta_l\|_2^2\).

For a fixed suffix degree \(k\), let \(C_{l,k}\) delete the unique edge leaving \(k\) edges on the right if its color is \(l\), and give zero otherwise.
These partial isometries have orthogonal initial subspaces as \(l\) varies, by the Wick isometry and the unique position of the deleted edge.
In particular \(\sum_l\|C_{l,k}p\|_2^2\le\|p\|_2^2\).
Expand the right leg of \(\beta_l\) in a reversed bounded Wick basis of degree \(k\) and \(C_{l,k}p\) in that basis before reversal.
The traced cut is the sum of products of the two left coefficients, by the orthonormal trace pairing, exactly as in the [suffix cut identity](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate).
Hölder in tracial \(L^2\), Cauchy--Schwarz over the colors and basis vectors, and then over \(0\le k\le n\) give
\[
 \|(\mathrm{id}\otimes\tau)\delta_\beta p\|_1
       \le\sqrt{n+1}\,B\|p\|_2 .
\]
Writing \(\beta_l^\star\) for the componentwise adjoint of both legs, the actual vacuum is \(\sum_l\partial_l^*(\beta_l^\star)\).
Indeed for a fixed split each adjoint reinserts its specified color isometrically, with mutually orthogonal ranges, and the sum over \(n+1\) splits has norm at most \(\sqrt{n+1}B\).
Testing polynomial vectors gives the actual adjoint pairing and passage from finite Wick tensors follows by Hilbert approximation, since each reference polynomial has finitely many cuts.
The same \(L^2\)-to-\(L^1\) estimate holds after the flip and adjoint of both legs.
By the [actual adjoint and reverse bound argument](Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound), the canonical contraction and its actual adjoint have full bounded-vector domains and restrictions of norms at most \(2\sqrt{n+1}B\) and \(\sqrt{n+1}B\), respectively.
In detail the \(L^1\) estimate puts bounded inputs in the adjoint domain by Riesz duality, and the Leibniz adjoint identity subtracts the reversed contraction from the input times the vacuum.
Applying that identity to the reversed derivative bounds the original contraction on its core.
Uniformly bounded strong polynomial approximation and weak closedness of its graph give the full original closure.
These arguments apply to the finite sum over colors with the norm \(B\).

### Reference corrections for bounded positive matrices

Assume item 3 and first assume that \(G\) is essentially bounded in matrix norm.
Let \(\delta_N\) be the reference derivation agreeing with the scalar divided difference and killing all \(S_l\).
It has actual vacuum \(\xi_N\) and bounded canonical and adjoint restrictions to the reference algebra, from the [scalar estimate](Yin_C_F0055_v1.md#statement) and the [normalized free lift](Yin_C_F0045_v1.md#statement) for the free family \(Z,S_1,\ldots,S_q\).
The bounds of this fixed reference derivation are independent of \(G\).

For a reference \(Z\) derivation correcting \(\delta_N\), take \(\delta_\beta S_l=\beta_l\) of total relative degree one.
Before the componentwise adjoint define its two arrays by
\[
 \begin{split}
 B_0(z,w,v)&=\frac{G(z,v)^{-1}G(w,v)-I}{z-w},
       && (B_0)_{lt}\ \text{on } N\otimes (N S_t N),\\
 B_1(z,w,v)&=\left(\frac{I-G(z,v)^{-1}G(z,w)}{w-v}\right)^t,
       && (B_1)_{tl}\ \text{on } (N S_t N)\otimes N .
 \end{split}                                                     \tag{4}
\]
The base variables index the first endpoint, middle endpoint and last endpoint of the two-leg path in the order displayed.
Applying the componentwise adjoint in \(B_0\) reverses the last two base variables and conjugates the entry.
The adjoint reinserts color \(l\) first, so the resulting two-edge matrix is \(\overline{P^{-1}Q-I}/(\bar z-\bar v)\).
In \(B_1\) the componentwise adjoint reverses the first two variables, conjugates the entry and reinserts \(l\) last.
Using \(G(w,z)^*=G(w,z)\) and edge reversal, the resulting matrix is \(\overline{I-PQ^{-1}}/(\bar z-\bar v)\).
Their sum is \(H\).

At each path the Hilbert--Schmidt cross term is nonnegative, since
\[
 {\rm Re\,tr}\big[(P^{-1}Q-I)^*(I-PQ^{-1})\big]
     ={\rm tr}(P^{-1}Q+PQ^{-1}-2I)\ge0.
\]
Indeed \(P^{-1}Q\) is similar to a positive matrix and the other trace is the trace of its inverse.
The two arrays in (4) lie in orthogonal coefficient degree spaces before insertion.
Their squared norms sum to at most \(\|H\|_2^2\) after integrating the pointwise inequality and reversing the dummy base variables.
In particular (4) defines actual Hilbert tensors even without essential boundedness of \(G^{-1}\).
The preceding cut lemma supplies both bounded-vector domain estimates for their correction, controlled by \(\|H\|_2\).
The reference sum \(\delta'=\delta_N+\delta_\beta\) has actual vacuum \(\xi_N+H\).
Its canonical contraction and adjoint are bounded on the reference algebra with bounds depending only on the fixed scalar estimate and \(\|H\|_2\).
For the sum this follows first on the core by addition for both the contraction and its reverse, then on all bounded vectors by the same bounded-core weak graph argument.

We verify its commutator with each actual \(T_j\).
On a separated polynomial approximation of \(G_{jt}\), the two arrays of the free reference derivative \(\delta_NT_j\), with remaining color \(t\), are the divided differences
\[
 \frac{G_{jt}(z,v)-G_{jt}(w,v)}{z-w},\qquad
 \frac{G_{jt}(z,w)-G_{jt}(z,v)}{w-v}.
 \tag{5}
\]
Insertion of (4) multiplies the noise index by \(G(z,v)\) at the two external endpoints.
Thus the corrections to the arrays (5) are the \(jt\) entries of \(G(z,v)B_0\) and \(G(z,v)B_1^t\), which are precisely the negatives of (5).
In particular (5) consists of \(L^2\) tensors since \(G\) is bounded and (4) is in \(L^2\).

For a measurable bounded \(G\) choose bounded separated polynomial entry approximants \(G^{(k)}_{jt}\) converging almost everywhere with a common supremum bound and preserving reversal by symmetrization.
Such approximants follow by bounded continuous approximation in measure on the compact base square, uniform polynomial approximation there, and subsequence selection.
On reference-core tensors, [the weak integration-by-parts identity (M6)](Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) identifies the limit of the \(\delta_N T^{(k)}_j\) pairings with (5).
Its parameterized scalar statement applies separately to each entry and each of the two legs, with the other base variable fixed in the tensor test.
The finite reference polynomials have bounded base polynomial factors in each Wick degree, and other color and degree components are orthogonal.
The correction arrays with \(G^{(k)}(z,v)\) converge strongly in \(L^2\) against (4) by dominated convergence.
The reference tensor commutator identity for the canonical contraction \(E'\) gives
\(\langle u,[E',T_j^{(k)}]v\rangle=\langle u\otimes v^*,\delta'T_j^{(k)}\rangle\)
on reference-core \(u,v\).
Here the full-domain restriction coincides with the core contraction on its domain.
The fields \(T_j^{(k)}\) converge strongly together with their adjoints, by their uniform operator bound and tracial \(L^2\) convergence.
In the matrix element of the commutator one may move \(E'\) to its actual adjoint on \(u\), showing \([E',T_j]=0\) on reference-core matrix elements.
The extension to every bounded \(v\) uses a uniformly bounded strong-star approximating net \(v_d\) in the reference core.
The values \(E'v_d\) and \(E'T_jv_d\) converge weakly to \(E'v\) and \(E'T_jv\), since they are bounded and their weak cluster points lie in the closed graph.
Similarly the reference commutator with \(Z\) is \(P_\Omega\) on all bounded vectors, by the reference generator rule and this approximation.
This proves the \(Z\)-coordinate commutators at the full required domain.

For the target coordinate \(j\), take degree-zero insertions with \(\delta_j S_l=(G^{-1})_{lj}\) and zero base derivative.
Their total squared norm is \(\int(G^{-2})_{jj}\).
On \(T_k^{(d)}\) they give \((G^{(d)}G^{-1})_{kj}\to\delta_{kj}\) in the coarse Hilbert space, by uniform boundedness of the approximants and square integrability of the column.
The same full-adjoint matrix element passage gives the commutators \(\delta_{kj}P_\Omega\) with all \(T_k\), and the base commutator vanishes.
Negating these contractions and the one for \(Z\) gives the generator-first strong system.
Each original contraction annihilates the vacuum.
The [normal strong-to-ACSY implication](Yin_C_F0070_v1.md#statement) ensures the actual target derivations exist and are unique.
The reference contraction agrees on target words with the canonical contraction by its commutators with \(Z,Z^*,T_k\), including the fixed marginal commutator with \(Z^*\).
Taking the inner product against the vacuum on this dense target core identifies the target vacua with the reference adjoint values at the unit, namely \(\overline{G^{-1}e_j}\) for channel \(j\) and \(\xi_N+H\) for \(Z\).
Their normalized contractions have the [full canonical domains](Yin_C_F0075_v1.md#statement).

### Removing the matrix amplitude cutoff

For general full-rank \(G\) satisfying item 3, truncate its eigenvalues from above at integers \(m\ge1\) by positive matrix functional calculus, obtaining \(G_m\).
Its edge reversal is preserved, and \((G_m^2)_{jj}\le(G^2)_{jj}\) keeps the same operator cutoff for every field.
The kernel rows converge in \(L^2\) by domination of \({\rm tr}(G^2)\), so the fields converge in moments by bounded strong convergence.
Furthermore \({\rm tr}(G_m^{-2})\le{\rm tr}(G^{-2})+q\).

Take orthonormal eigenbases \(u_s,v_t\) for \(P,Q\) with eigenvalues \(\lambda_s,\gamma_t>0\).
Then
\[
 \|P^{-1}Q-PQ^{-1}\|_{\rm HS}^2
 =\sum_{s,t}|\langle u_s,v_t\rangle|^2
          (\gamma_t/\lambda_s-\lambda_s/\gamma_t)^2 .
 \tag{6}
\]
The same bases apply after truncation.
Truncation from above contracts the distance between the logarithms of any two eigenvalues, and \(|r-r^{-1}|=2\sinh|\log r|\).
Each squared scalar factor in (6) therefore decreases under the cutoff, proving \(\|H_m(z,w,v)\|_{\rm HS}\le\|H(z,w,v)\|_{\rm HS}\).
The clipped \(H_m\) and columns \(\overline{G_m^{-1}e_j}\) converge strongly in their respective Hilbert spaces by dominated convergence.

The bounded-matrix proof now gives uniform bounds on each clipped canonical contraction and adjoint, since the scalar reference term is fixed and their corrections have uniformly bounded coefficient norms by (1), (4) and (6).
Consequently the original and adjoint tuples each have bounded full-domain dual norms with uniform caps, using \(-E'^*\) for the adjoint-tuple operator-first commutators.
The [closed norm sublevels and two-sided normal criterion](Yin_C_F0201_v2.md#statement) give \(\mathsf S(X)\) on the limiting intrinsic algebra.
The same normal strong-to-ACSY and canonical-domain theorems apply, completing the equivalence.
For any fixed target star polynomial the actual derivatives on the clipped kernels converge in the coarse Hilbert norm to those on \(G\), by the word rule, since all unstarred generator derivative values and the diffuse marginal starred values are fixed, and uniformly bounded word multipliers converge strongly with their adjoints.
Passing the clipped vacuum identities to the limit on this dense target core yields precisely (2) and the stated one-edge vacua.
The rectangular isometry then transports these formulas and all domain assertions to \(M_A\).

### Noncommuting covariances in two channels

Take normalized area measure on the unit disk and \(Z(z)=z\).
The scalar vacuum exists by absolute integration of \(|z-v|^{-1}\), as in the [disk example](Yin_C_F0157_v2.md#infinite-spectral-blocks-with-no-convergence-in-operator-norm).
For \(q=r=2\), use the real positive matrix \(A=G\) defined by
\[
 D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 K=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 G(z,w)=I+\tfrac1{16}\big[D\,{\rm Re}(z+w)+K\,{\rm Im}(z+w)\big].
\]
Its spectrum is in \([3/4,5/4]\).
The matrices \(G(z,w),G(w,v)\) have a nonzero commutator whenever the coefficient vectors of \(D,K\) are linearly independent, which holds on an open set of positive \(\mu^3\) measure.
Here \(Q=G(w,v)\), and \(\|Q-P\|\le (2/16)|z-v|\).
The identity \(P^{-1}Q-PQ^{-1}=P^{-1}(Q-P)+(Q-P)Q^{-1}\) bounds the quotient in (1) uniformly, so the tuple has both strong domains.
On the other hand (3) excludes every positive-measure failure of full row rank, including \(q>r\), from both \(\mathsf A\) and \(\mathsf S\).

## Assessment history

### Decision matrix-gaussian-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:40 |
| status | open |
| reason | The candidate argument gives a color-resolved intrinsic criterion including rank obstruction, noncommuting matrix ratios, measurable kernels and full canonical domains. Independent proof review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Row criterion, intrinsic ACSY and strong equivalence, rank and two integrals, full canonical domains, explicit vacuum vectors and noncommuting example. |
| argument | [Argument](#argument) | Colored paths, rectangular isometry, quadratic testing, both coefficient arrays and their actual adjoints, reference commutators, eigenvalue clipping and domain transfer. |
| dependency | [Matching-color Wick rule](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Mixed moments for the free semicircular family with abelian base insertions and only equal-color pairings. |
| dependency | [Relative Wick recurrence](Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) | Relative Hilbert path construction and the cut and insertion method, with the matching-color recurrence proved here. |
| dependency | [Suffix cut](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) | Orthogonal right-coefficient expansion and the noncommutative product estimate, applied with the indicated colored cuts. |
| dependency | [Adjoint duality](Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound) | Actual vacuum, flip identity and Riesz domain and reverse estimates after verifying the colored Hilbert bounds. |
| dependency | [Scalar estimate](Yin_C_F0055_v1.md#statement) | Actual scalar vacuum gives bounds on both marginal contraction directions. |
| dependency | [Free lift](Yin_C_F0045_v1.md#statement) | Normalized base contraction on the free family of the base and the standard reference semicirculars. |
| dependency | [Target moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests) | Normal marginal phase and original smooth endpoint graph tests with bounded fields; the matrix contractions are computed here. |
| dependency | [Weak integration by parts](Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) | Scalar parameterized (M6) on algebraic tests with bounded entries and square-integrable leg quotients, justified by (4). |
| dependency | [Single-coordinate bounded fields](Yin_C_F0157_v2.md#argument) | Bounded-kernel field construction and the scalar area-disk vacuum, also used in the explicit two-channel example. |
| dependency | [Law-space limit](Yin_C_F0201_v2.md#statement) | Closed global dual norm caps at a fixed operator cutoff, and normal characterization using both signs. |
| dependency | [Normal strong-to-ACSY implication](Yin_C_F0070_v1.md#statement) | Actual full-core derivations and forced marginal values for the normal strong tuple. |
| dependency | [Normal canonical comparison](Yin_C_F0075_v1.md#statement) | Both original canonical domains for each coordinate in the intrinsic algebra under the normal strong condition. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:48 |
| status | proved |
| reason | Adopt the intrinsic multichannel Gaussian equivalence and matrix vacuum formulas, including measurable kernels and rank obstruction, after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Row criterion, intrinsic ACSY and strong equivalence, rank and two integrals, full canonical domains, explicit vacuum vectors and noncommuting example. |
| argument | [Argument](#argument) | Colored paths, rectangular isometry, quadratic testing, both coefficient arrays and their actual adjoints, reference commutators, eigenvalue clipping and domain transfer. |
| dependency | [Matching-color Wick rule](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Mixed moments for the free semicircular family with abelian base insertions and only equal-color pairings. |
| dependency | [Relative Wick recurrence](Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) | Relative Hilbert path construction and the cut and insertion method, with the matching-color recurrence proved here. |
| dependency | [Suffix cut](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) | Orthogonal right-coefficient expansion and the noncommutative product estimate, applied with the indicated colored cuts. |
| dependency | [Adjoint duality](Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound) | Actual vacuum, flip identity and Riesz domain and reverse estimates after verifying the colored Hilbert bounds. |
| dependency | [Scalar estimate](Yin_C_F0055_v1.md#statement) | Actual scalar vacuum gives bounds on both marginal contraction directions. |
| dependency | [Free lift](Yin_C_F0045_v1.md#statement) | Normalized base contraction on the free family of the base and the standard reference semicirculars. |
| dependency | [Target moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests) | Normal marginal phase and original smooth endpoint graph tests with bounded fields; the matrix contractions are computed here. |
| dependency | [Weak integration by parts](Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) | Scalar parameterized (M6) on algebraic tests with bounded entries and square-integrable leg quotients, justified by (4). |
| dependency | [Single-coordinate bounded fields](Yin_C_F0157_v2.md#argument) | Bounded-kernel field construction and the scalar area-disk vacuum, also used in the explicit two-channel example. |
| dependency | [Law-space limit](Yin_C_F0201_v2.md#statement) | Closed global dual norm caps at a fixed operator cutoff, and normal characterization using both signs. |
| dependency | [Normal strong-to-ACSY implication](Yin_C_F0070_v1.md#statement) | Actual full-core derivations and forced marginal values for the normal strong tuple. |
| dependency | [Normal canonical comparison](Yin_C_F0075_v1.md#statement) | Both original canonical domains for each coordinate in the intrinsic algebra under the normal strong condition. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0217_v1.md#conclusion) | Whole proof and twelve direct inputs, including noncommuting edge matrices, actual correction operators, spectral clipping and both domains. |
