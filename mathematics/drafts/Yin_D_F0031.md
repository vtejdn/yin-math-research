---
author: Yin
---

# An alternative Fourier selection repair and a generalized cofactor interface

This ordinary proof development for the [finite-variance Brown question](../tasks/Yin_T_F0012_v3.md#contract) began on 2026-11-05.
The two-marginal finite-family count, common cutoff controls and economical initial nets now have adequate fixed proofs in [C_F0194_v10](../claims/Yin_C_F0194_v10.md#argument), using the complete [v7 profile construction](../claims/Yin_C_F0194_v7.md#generic-finite-family-count).
Their actual intermediate scope permits two different nondegenerate marginal laws and arbitrary dependence within each independently exposed unordered pair.
This draft retains the wider cofactor interface below and a distinct direct replacement of the Fourier selection use of NO15 Claim A.2.
That direct source-proof route has not received a complete source-chain audit or independent project review.

The original NO15 arXiv v4, 57-page edition, PDF pp. 7--20 was read for the inverse/counting split and Section 5 construction, and Theorem 4.1 on p. 12 was visually checked.
Appendix A, pp. 45--50, was also read for the Fourier separation interface and its actual downstream use.
This selected reading is not a complete original-proof review.

<a id="initial-families"></a>
## A generalized cofactor interface and exact unit normalization

The fixed economical-witness argument can also be used with a matrix \(A\) satisfying
\[
 \|A\|_{\mathrm F}=1,\qquad DA=AD=\lambda I,
 \tag{Adjugate-interface}
\]
where \(D\) has entries bounded by \(n^{K_0}\) and \(\lambda\) may be zero.
A nonzero normalized adjugate is an example, but is not required for the following conditional construction.
Fix \(0<\varepsilon<1\), a fixed integer \(r\), and a constant \(C_0\).
Suppose that \(|I|\ge n-2n^\varepsilon\), \(|I_0|\le r\), and integers \(0<|k|\le n^{C_0}\), \(|k_{ij}|\le n^{C_0}\) satisfy
\[
 \left\|k r_i(A)+\sum_{j\in I_0}k_{ij}r_j(A)\right\|_2\le n^{-a}
 \qquad(i\in I).
\]
Denote the displayed row combination by \(r'_i\).
Remove the at most \(r\) base indices from \(I\), and choose a column \(c\) of \(A\) with \(\|c\|_2\ge n^{-1/2}\).
Its coordinates have modulus at most one and satisfy the corresponding scalar integer relations up to \(n^{-a}\).
Round its base and exceptional coordinates on a complex grid of mesh \(n^{-a}\), and solve those integer relations exactly for the remaining coordinates.
The coordinate error is at most \(C_r n^{-a+C_0}\), so the full vector error is at most \(C_r n^{-a+C_0+1/2}\).
For sufficiently large \(n\) and \(a>C_0+2\), the rounded vector is nonzero and its normalization has distance at most \(C_r n^{-a+C_0+1}\) from \(c/\|c\|_2\).
The identity \(DA=\lambda I\) makes the latter vector a kernel vector outside one row, so the unit rounded vector has residual at most \(n^{-a+C_0+K_0+3}\) on those rows eventually.

The integer coefficients cost \(n^{O_{r,C_0}(n)}\), the exceptional-position choices cost \(\exp(O(n^\varepsilon\log n))\), and all gridded scalar values cost \(n^{O_{a,r}(n^\varepsilon+1)}\).
Thus the deterministic family has size \(n^{C_1n+o_a(n)}\), with \(C_1\) independent of \(a\).
Normalizing every nonzero member does not increase this cardinality.
This proves the precise unit-norm version without requiring that \(A\) be an adjugate.

In the complementary branch, let one modified row \(r'_i\) have norm at least \(n^{-a}\) and suppose an inverse step has supplied
\[
 \mathbb P_\eta\{|\sum_j\eta_j r'_i(j)|\le n^{-2a+C_0}\}\ge n^{-C_0}
\]
for independent copies of a fixed nondegenerate complex finite-second-moment scalar law.
Its normalized row has concentration at least \(n^{-C_0}\) at radius \(n^{-a+C_0}\), and \(AD=\lambda I\) makes it annihilate every column outside \(\{i\}\cup I_0\).
The [fixed initial-net construction](../claims/Yin_C_F0194_v7.md#generic-initial-net), including fixed-phase TV08 and replacement of used centers by unit witnesses, gives the corresponding economical family for \(D^T\).
The two-law splitting and common-cutoff adaptations are fixed in [v10](../claims/Yin_C_F0194_v10.md#argument).
Choosing the finite-family exclusion exponent first and then sufficiently large \(a\) absorbs all fixed rounding and matrix-norm losses.
This is an applicability extension of that fixed counting proof, conditional on the displayed integer relations and concentration input; it does not prove such inputs for an arbitrary \(A\).

<a id="fourier-separation-repair"></a>
## A replacement for the Fourier separation use of Claim A.2

The [explicit separation obstruction](../audits/literature/NO15/Yin_U002.md#separation-obstruction) shows that the printed positive-probability ratio statement in NO15 Claim A.2 cannot be used literally, even for every normalized symmetrized elliptic pair.
The following local replacement proves exactly the coefficient-selection property used at the double-counting stage on PDF p. 48.
It does not assert that Claim A.2's original support conclusion is true.

For a centered unit-variance \((\mu,\rho)\)-family pair, its complex covariance Gram matrix is
\[
 G=\mathbb E
  \begin{pmatrix}U\\V\end{pmatrix}
  \begin{pmatrix}\overline U&\overline V\end{pmatrix}
 =\begin{pmatrix}1&\rho(2\mu-1)\\\rho(2\mu-1)&1\end{pmatrix}.
\]
Its smallest eigenvalue is at least \(1-|\rho|>0\).
For an independent pair copy \((U',V')\), put
\(Z=(2(U-U'),2(V-V'))\).
Its covariance Gram matrix is \(8G\), so the complex linear span of its support is \(\mathbb C^2\).
Otherwise a nonzero complex linear functional would vanish almost surely and give a zero Gram eigenvalue.
Choose two linearly independent support points and sufficiently small bounded neighborhoods \(E_1,E_2\) of them.
There are constants \(p,\Delta,C>0\), depending only on the fixed pair law, such that
\[
 \mathbb P(Z\in E_j)\ge p,\qquad
 |d_1d'_2-d_2d'_1|\ge\Delta,\qquad
 |d_1|,|d_2|,|d'_1|,|d'_2|\le C
 \tag{Support-determinant}
\]
whenever \(d\in E_1,d'\in E_2\).
Individual components of these vectors are allowed to vanish.

Fix any finite set \(S\subset\mathbb C\), coefficients \(a_i',b_i'\), and define the nonnegative Fourier cost
\[
 H(z)=\sum_{s\in S}\sum_i
   \|\operatorname{Re}[(z_1a'_i+z_2b'_i)s]\|_{\mathbb R/\mathbb Z}^2.
\]
Suppose \(\mathbb EH(Z)\le M\).
For \(M>0\), each \(E_j\) contains a point whose cost is at most \(2M/p\), by Markov's inequality within that event.
For \(M=0\), almost every point has zero cost, so the same selection is possible with cost zero.
Choose such points \(d\in E_1,d'\in E_2\); they satisfy (Support-determinant).

The distance to the integer lattice obeys
\(\|x+qy\|_{\mathbb R/\mathbb Z}\le\|x\|_{\mathbb R/\mathbb Z}+|q|\|y\|_{\mathbb R/\mathbb Z}\) for every integer \(q\).
Thus for \(q=1,2,3,4\),
\[
 H(d+qd')\le2H(d)+2q^2H(d')\le68M/p.
 \tag{Fourier-cost}
\]
These bounded integer combinations need not belong to the support of \(Z\); only their deterministic Fourier costs are used after the selection step.

Set \(\eta_0=\Delta/(24C)\).
For a fixed coordinate \(j\), at most one of the four integers \(q\) can satisfy \(|d_j+qd'_j|<\eta_0\).
Indeed two such integers would give \(|d'_j|<2\eta_0\) and \(|d_j|<9\eta_0\).
Together with the other coordinate's \(C\)-bounds, these inequalities would imply
\(|d_1d'_2-d_2d'_1|<11C\eta_0<\Delta\), a contradiction.
At most two of the four rows are bad for one of the two coordinates.
Choose two different remaining integers \(q,q'\), and set \(e=d+qd'\), \(e'=d+q'd'\).
Then
\[
 \eta_0\le|e_j|,|e'_j|\le5C\quad(j=1,2),
 \qquad |e_1e'_2-e_2e'_1|
   =|q'-q|\,|d_1d'_2-d_2d'_1|\ge\Delta,
\]
and therefore
\[
 |e_1/e_2-e'_1/e'_2|\ge\Delta/(25C^2).
 \tag{Selected-separation}
\]
Both rows satisfy (Fourier-cost).
Their coefficients may depend on the actual Fourier cost, as the source's mixing coefficients may depend on the dimension and input coefficient arrays, but every bound above depends only on the fixed pair law.

In NO15 p. 48 the available expectation is \(M=16m|S|\), where \(m\ge0\) is the parameter in that Fourier estimate.
The two selected arrays \(v_i=e_1a'_i+e_2b'_i\) and \(v_{n+i}=e'_1a'_i+e'_2b'_i\) consequently satisfy
\[
 \sum_{s\in S}\sum_{i=1}^{2n}
       \|\operatorname{Re}(v_i s)\|_{\mathbb R/\mathbb Z}^2
 \le (2176/p)m|S|.
\]
This has precisely the fixed-constant form of the source's next displayed estimate.
If \(\beta>0\), \(\sum_i(|a_i|^2+|b_i|^2)=1\), and \(a'_i=\beta^{-1}a_i,b'_i=\beta^{-1}b_i\), the coefficient bound also gives
\[
 \sum_{i=1}^{2n}|v_i|^2\le100C^2\beta^{-2},
\]
which is the norm scale used on p. 50.
Thus the invalid support-ratio claim can be bypassed at this particular Fourier selection step without sacrificing nonzero mixing coefficients, determinant separation, a fixed cost constant or the required norm scale.

This local repair assumes only the displayed expectation bound at the beginning of the source's double-counting step.
It does not verify every preceding Fourier inequality or every later discretization and additive-combinatorial argument.
In particular, the full corrected geometric mixed inverse theorem and its passage to Theorem 4.1 have not been established by this local selection lemma.

<a id="remaining-inverse-boundary"></a>
## Boundary of this direct source-proof variant

The [fixed local argument](../claims/Yin_C_F0194_v10.md#argument) supplies the mixed geometric inverse, bounded integer row relations and full elliptic least-value assembly through a different Fourier route that permits zero individual mixing components.
Its [positive-covariance extension](../claims/Yin_C_F0194_v11.md#argument) checks that route under the larger pair hypothesis.
Those fixed arguments, rather than the incomplete original-source reconstruction here, supply the available least-value input.

The alternative selection lemma above bypasses the false Claim A.2 at its double-counting use, conditional on the displayed Fourier expectation bound, while retaining nonzero components and separated ratios.
It does not certify every preceding Fourier inequality or subsequent discretization and additive-combinatorial step of that source proof.
That remaining inspection belongs only to this alternative source-proof route; it is not an outstanding global inverse-theorem premise of the [adopted additive result](../claims/Yin_C_F0186_v14.md#decision-corrected-elliptic-reviewed).
The original source's retained arithmetic and separation counterexamples remain valid, and this local replacement does not assert a corrected published edition.
