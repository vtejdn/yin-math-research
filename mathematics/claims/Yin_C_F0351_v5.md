---
author: Yin
---

# Almost-sure Brown convergence and summable terminal deviations for two Rademacher inputs

<a id="statement"></a>
## The sign model

Let \(A_N,B_N\) be independent real symmetric matrices whose independent upper triangular entries, including diagonals, are uniform on \(\{-N^{-1/2},N^{-1/2}\}\).
Different dimensions may be coupled arbitrarily.
Put \(P_N=A_NB_N+2B_NA_N\) and \(p=ab+2ba\) for free standard semicircular \(a,b\).
Write \(s_1\ge\cdots\ge s_N\), \(\log^-x=\max(0,-\log x)\), and \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
For every \(0<R<\infty\) and every \(\epsilon>0\),
\[
 \sum_{N:\,q_N<N}\Pr\left\{
 \frac1N\int_{|z|<R}\sum_{j>N-q_N}\log^-s_j(P_N-zI)\,dA(z)>\epsilon
 \right\}<\infty .
\]
Values at the finitely many eigenvalues do not affect the integral.
Almost surely under each allowed coupling, \(N^{-1}\log|\det(P_N-\cdot I)|\) converges in local planar \(L^1\) to \(\tau\log|p-\cdot|\), and the empirical eigenvalue probability converges weakly to the Brown measure of \(p\).

<a id="argument"></a>

<a id="sign-flag-area"></a>
## Summable planar deviations for all later sign hyperplanes

Take two independent real symmetric Wigner matrices with raw Rademacher entries, including their independent diagonals, in the physical normalization of [the flag construction](../claims/Yin_C_F0351_v1.md#later-hyperplanes).
Let \(n=N-k\), where \(k=O(\log^3 N)\), and let \(M=A_{JJ}B_{JJ}+2B_{JJ}A_{JJ}\) on the \(n\) old sites.
The independent raw columns \(g_1,\ldots,g_k\) of the other block of \(B\) have iid sign coordinates.
Write \(H_l=\operatorname{span}(g_1,\ldots,g_l)^\perp\), \(T_l(z)=P_{H_l}(M-zI)|_{H_l}\), and let \(R_l(z)\) be its inverse extended by zero on \(H_l^\perp\).
At the finite spectra of these compressions ignore the ratio, as all statements below concern area.
Outside column dependence, its value on adding the next normal is
\[
 d_l(z)=\det T_{l+1}(z)/\det T_l(z)
       =g_{l+1}^{\mathsf T}R_l(z)g_{l+1}/\|P_{H_l}g_{l+1}\|^2.
\]
For every bounded disk \(K\) and every \(v>0\) one has
\[
 \sum_N\Pr\{|\{z\in K:\min_{0\le l<k}|d_l(z)|<N^{-2}\}|>v\}<\infty . \tag{1}
\]
Column dependence has summable probability by the [physical cross-block estimate](../claims/Yin_C_F0196_v4.md#statement).
The bound allows the first deletion used in a determinant comparison to depend on the shift and the old minor.

**Physical blocks at several shifts.**
Fix \(D\), a compact upper-half-plane set and a positive minimum spacing for \(D\) shifts in it.
Let \(e,f\) project onto two distinct classes of a deterministic partition into a fixed number of classes of equal limiting density.
Two halves suffice for (1).
For real \(t\in S^{D-1}\), put \(C_j=e\operatorname{Re}\operatorname{sym}R_l(z_j)f\), where symmetrization uses transpose and the real part is taken entrywise.
There exist \(s,\gamma>0\) such that \(\sum_jt_j C_j\) has at least \(\gamma n\) singular values above \(s\) simultaneously for all these choices and all \(l\), outside a summable event of the original old pair.
The \(C_j\) admit bounded approximants \(G_j\) with total rank error less than \(\gamma n/10\).
The same approximants work for all \(l\).
The bounds depend on the compact set, spacing and \(D\).

To verify this, use the free semicircular pair \(a,b\), \(m=ab+2ba\), jointly free from the finite-dimensional algebra of the coordinate projections with their limiting traces.
Define \(K(z)=((m-z)^{-1}+(m^*-z)^{-1})/2\) in the affiliated algebra.
The counterpart of the real symmetric matrix before the coordinate restrictions is \((K(z)+K(\bar z))/2\).
The embedded [semicircular free field used in C11](../claims/Yin_C_F0011_v1.md#yin_c_f0011) detects rational identities, so a scalar identity for a nonzero real combination would specialize at \(b=1,a=x\) to the same scalar identity of rational functions of \(x\).
The distinct simple poles at \(z_j/3,\bar z_j/3\) force every coefficient to vanish.
All the resolvents here exist as affiliated elements by the same free-field embedding.

For any such nonscalar affiliated element \(X\) in the first free factor, \(eXf\ne0\).
Use the equal-trace colors of the coordinate partition.
Permutation of the colors extends to a trace-preserving automorphism fixing the first free factor, so vanishing of one distinct-color corner would force all of them to vanish.
Then \(X\) commutes with \(e\), as do its bounded transform \(Y=X(1+X^*X)^{-1/2}\) and its adjoint.
Every bounded first-factor element \(Y\) commuting with the nontrivial free projection is scalar.
After subtracting its trace the two centered reduced words in the commutator with \(e-\tau(e)\) are orthogonal and each has squared norm \(\|Y-\tau(Y)\|_2^2\|e-\tau(e)\|_2^2\).
The injective bounded transform then makes \(X\) scalar.

Here are details of uniform finite-matrix transfer.
To see continuity of the affiliated resolvents in measure as \(z\) varies, approximate each inverse by \(F_\eta(T)=h_\eta(T^*T)T^*\), \(h_\eta(x)=1/\max(x,\eta^2)\).
The approximation agrees with the inverse except on a subspace of trace at most \(\tau(1_{[0,\eta)}(|T|))\), and depends continuously in operator norm on \(T\) in bounded sets.
The small-singular-value fractions tend to zero uniformly on the compact shifts by the singular-value shift inequality, finite covering and absence of a zero atom at every shift.
Finite sums, corners and multiplication by bounded coefficients preserve this continuity in measure.
Nonvanishing of every directional free corner and compactness of the shifts and the unit sphere therefore give fixed \(s,\gamma>0\) and at least \(4\gamma\) of the free trace above \(4s\), uniformly.
Indeed a strict singular-value lower count persists in a neighborhood under an operator-norm perturbation plus a perturbation supported on a projection of sufficiently small trace.
Choose \(\eta>0\) so small that the total trace loss from replacing every inverse in these formulas by \(F_{2\eta}\), including conjugate and transposed terms, is below \(\gamma/100\).
The finite model can then use the upper count at \(2\eta\) when approximating by \(F_\eta\).

The normalized mixed traces of the bounded Wigner pair and the fixed coordinate colors converge in expectation to the stated free moments.
For a monomial with \(h\) Wigner factors, expand its trace as closed walks with site-color restrictions from the diagonal projections.
Surviving leading index patterns have \(1+h/2\) vertices and a tree of \(h/2\) edges, each traversed twice with the same Wigner color.
All other nonzero patterns lose a power of \(n^{1/2}\) or more.
Counting the permitted labels of the vertices gives the product of their allowed color densities, exactly the free Wick recursion that pairs the return traversal of each tree edge and takes the trace of its enclosed word.
The scaling multiplier \((n/N)^{h/2}\) tends to one.
The two input norms are bounded by a fixed constant outside probability \(Ce^{-cn}\).
Each fixed real unit-vector quadratic form is a sign sum with sum of squared coefficients \(O(1/n)\), so a fixed-radius net of the sphere works with a sufficiently large constant bound.
On this event approximate \(F_\eta\) uniformly by a fixed matrix polynomial in \(T,T^*\) using scalar polynomial approximation to \(h_\eta\).
For fixed polynomial matrices, normalized singular-value counts at continuity points have exponentially small fixed deviations from their limiting counts.
Indeed the mixed moments give convergence of the expected singular measures by the norm guard and moment bounds (on its complement the norms have deterministic polynomial bounds), and changing one independent upper-row group changes a fixed polynomial matrix by bounded rank, by telescoping each word.
The bounded differences inequality applied to the spectral counting function gives the exponential bound.
Using upper and lower counts at interior continuity points supplies the strict inequalities with slack above, both for the approximants and the small-singular-value counts of \(M-z\).
Finite nets suffice for the bounded approximants, which have a common norm-continuity modulus on the norm guard, and for the small-singular counts by the shift inequality.
This proves the simultaneous finite count and rank-error bounds for \(l=0\).
For \(l>0\), \(P_{H_l}(I-(M-z)R_l)=0\), so \(R_l-R_0\) has rank at most \(l\) whenever both inverses exist.
Transpose symmetrization and entrywise real part cost at most \(4l\), and \(Dk=o(n)\).
The bounded approximants to the original physical block thus give the assertions for every flag, even though the later subspaces need not be independent of its compressed resolvents.

**Several quadratic tests on the same sign column.**
Condition on the old pair and all earlier columns.
Suppose \(r\le D\) selected shifts are tested at this step.
If all their ratios have magnitude below \(N^{-2}\), the real raw quadratic forms have magnitudes below \(nN^{-2}\), since \(\|g\|^2=n\).
Write the independent halves of \(g\) as \(u,v\).
Two Cauchy--Schwarz applications give that the fourth power of the probability of the simultaneous tests is at most the probability that the tests hold at all four corners \((u,v),(u',v),(u,v'),(u',v')\), with independent copies.
Subtracting opposite corners converts this into the upper bound \(\Pr\{|(u-u')^\mathsf TC_j(v-v')|\le 2nN^{-2},\ 1\le j\le r\}\).

The independent coordinates of \(x=u-u'\) have variance two and support in \([-2,2]\).
For every set \(S\) of at most \(\alpha n\) output coordinates let \(Q_S\) be orthogonal projection off those coordinates and the ranges of all \((C_j-G_j)^\mathsf T\).
Every real unit combination \(Q_S\sum t_jG_j^\mathsf T\) still has a fixed positive fraction of singular values above a fixed constant, by the preceding rank estimates and small \(\alpha\).
Consequently the squared mean norm in the sense \(\mathbb E\|Q_S\sum t_jG_j^\mathsf T x\|^2\) is at least \(cn\).
The norm is a convex function of \(x\) with bounded Lipschitz constant, so the [bounded-product convex concentration inequality](../claims/Yin_C_F0187_v2.md#argument) gives an exponential lower-tail bound below \(c'\sqrt n\).
Indeed integration of its two-sided median deviation bounds gives a bounded second centered moment about the median and hence the same order lower bound on the median.
Choose \(\alpha>0\) small enough for the entropy of all \(S\) to be less than the exponential rate, then take a sufficiently fine fixed net for \(t\), using \(\|x\|\le2\sqrt n\) and the bounded \(G_j\).
Except with \(Ce^{-c'n}\), after every such coordinate deletion the remaining row vectors \(w_i=((C_j^\mathsf T x)_i)_{j=1}^r\) form a matrix with least singular value at least \(c''\sqrt n\).
The discarded error ranges contribute nothing after applying \(Q_S\).
This argument also permits projecting off any additional, conditionally fixed output subspace of bounded dimension independent of \(x\).

Choose a maximum absolute determinant basis among the remaining rows.
Every other row has coefficients bounded by one in this basis, by the replacement determinant formula.
The matrix of these coefficients has operator norm at most \(\sqrt{nr}\), so the basis matrix has least singular value bounded below by a constant.
Remove that basis and repeat to obtain \(L\ge c_r n\) disjoint such bases.
For independent signs or differences of independent signs \(y_i\), these bases imply
\[
 \sup_a\Pr\{\|\textstyle\sum_i y_i w_i-a\|\le1\}\le C_r L^{-r/2}. \tag{2}
\]
Indeed majorize the unit-ball indicator by \(e^{1/2}\exp(-\|\cdot\|^2/2)\), use its standard Gaussian Fourier representation, discard the phase and unused factors, and apply Hölder with exponent \(L\) to the bases.
The characteristic-function modulus for a single coordinate is \(|\cos t|\) or \(\cos^2 t\), respectively.
For a basis matrix \(U\) and a standard Gaussian \(G\), the covariance of \(UG\) dominates \(c^2 I_r\).
It therefore has the distribution of \(cG'\) plus an independent Gaussian shift.
The wrapped one-dimensional normal density on a period of \(|\cos|\) is uniformly bounded under translation.
Its integral against \(|\cos|^L\) is at most \(C_c/\sqrt L\), by the quadratic falloff at a maximum.
Condition on the shift and multiply over the independent coordinates of \(G'\).
Hölder now gives (2), with no upper bound required on the basis norms.
Apply (2) to \(y=v-v'\), since for large \(N\) the box of widths \(2nN^{-2}\) is inside the unit ball.
The original conditional probability is at most \(C_D n^{-r/8}\).

**From simultaneous shifts to area.**
Take \(D=16\).
Assign each of the \(D\) separated shifts a step at which it has a bad ratio.
At a step with \(r\) assigned shifts use the conditional bound just proved and iterate over the independent next columns in chronological order.
Since the exponents add, the probability for all shifts to be bad is at most \(C_D k^D n^{-D/8}\) plus the summable old-pair and rank exceptions.
For almost every tuple none of the finitely many possible sign realizations in that dimension has a pole at its coordinates.
For a disk and prescribed area \(v\), remove a thin real strip of area less than \(v/2\) and reflect the lower half to the upper half, using conjugation symmetry of the real flag and a larger bounding disk if necessary.
If the original exceptional area exceeds \(v\), its upper image has area at least \(v/4\).
Choosing a fixed spacing small enough, sequential removal of at most \(D-1\) disks of that spacing leaves at least \(v/8\) of choices at every stage.
Thus the product area of separated bad tuples is at least \((v/8)^D\).
Fubini and the uniform probability bound prove (1), since \(k^{16}n^{-2}\) is summable.
Combining (1) with the [first singular-subspace deletions](../claims/Yin_C_F0351_v2.md#discrete-overlaps) gives the later-hyperplane part of the exterior determinant comparison for two sign inputs.
The estimate concerns the planar exceptional set jointly over shifts.
A single fixed shift uses only the smaller one-direction exponent.

<a id="paired-sign-restoration"></a>
## Restoring the physical site and its observed image with one fresh sign row

Consider \(M=AB+2BA\) with both independent real Wigner inputs having normalized Rademacher upper entries, and take \(I=\{i_1,\ldots,i_k\}\), \(J=I^c\), \(k=o(N)\).
Reveal \(B,A_{JJ},A_{II}\) first.
For each \(i\in I\) write \(x_i\) for the vector supported on \(J\) with entries \(A_{ji}\) there.
The vectors \(\sqrt N\,x_i|_J\) are independent sign vectors under this conditioning.
Reveal them in the order \(i_1,\ldots,i_k\).
Let \(H_t\) be the real orthogonal complement of \(\{e_{i_j},Be_{i_j}:j>t\}\), with its usual complexification for determinants.
Initially \(H_0\) is the exterior space in the [repeated-interior identity](../drafts/Yin_D_F0042.md#repeated-interior), and \(H_k\) is the entire space.
For each advance \(t=1,\ldots,k\) put \(i=i_t\), \(F=[e_i,Be_i]\), \(G=[x_i,Bx_i]\) and \(D=\bigl(\begin{smallmatrix}0&1\\2&0\end{smallmatrix}\bigr)\).
The contribution from this row of \(A\) to \(M\) is exactly \(FDG^{\mathsf T}+GDF^{\mathsf T}\).
Both terms from any later row vanish after compression on both sides to \(H_t\).
Both terms from the current row vanish after compression on both sides to \(H_{t-1}\).
These cancellations also make the old compressed matrix measurable before the current row is drawn.

Put \(P_t\) for the projection onto \(H_t\).
On the [cross-block floor](../claims/Yin_C_F0196_v4.md#argument) the two columns of \(P_tF\) are independent.
In fact the full column map of the pairs on \(I\) takes \((g,h)\) to the vector with coordinates \((g+B_{II}h,B_{JI}h)\) on \(I,J\).
Its least singular value is bounded below in terms of \(s_{\min}(B_{JI})\) and \(\|B_{II}\|\).
Taking the distance to the span of the later pairs preserves this lower bound for the two current projected columns.
In the sign model \(\|B_{II}\|\le k/\sqrt N\), which tends to zero at \(k\asymp\log^3 N\).
Choose a real orthonormal frame \(L\) for \(H_t\ominus H_{t-1}\) and set \(F_L=L^{\mathsf T}F\).
For every \(z\) off the old compressed spectrum, let \(R\) equal the old compressed inverse of \(M-z\), extended by zero outside \(H_{t-1}\).
The determinant ratio from \(H_{t-1}\) to \(H_t\) equals the determinant of a two-by-two Schur complement.
Its highest possible homogeneous term in \(x_i\) is
\[
 4\det(F_L^{\mathsf T}F_L)
 \det\!\begin{pmatrix}
 x_i^{\mathsf T}Rx_i & x_i^{\mathsf T}RBx_i\\
 x_i^{\mathsf T}BRx_i & x_i^{\mathsf T}BRBx_i
 \end{pmatrix}.
\]
Indeed the upper-right and lower-left old-to-new blocks have linear parts \(P_{t-1}GDF_L^{\mathsf T}\) and \(F_LDG^{\mathsf T}P_{t-1}\), respectively.
The new diagonal block is affine, and the quadratic part of its Schur complement is \(-F_LD(G^{\mathsf T}RG)DF_L^{\mathsf T}\).
Taking its determinant gives the formula, with an additional factor \(N^{-2}\) when the quartic is written in raw signs.
Interior entries of \(A_{II}\) have already been fixed and affect only lower degrees.
The geometric factor is common to all shifts at a given step and has a fixed positive lower bound on the indicated mesoscopic guard.

The four symmetric matrices of quadratic coefficients are
\[
 K_{ab}(z)=\operatorname{sym}(B^a R B^b),\qquad a,b\in\{0,1\},
 \quad\operatorname{sym}(T)=(T+T^{\mathsf T})/2 .
\]
For the rank comparison on \(J\) one may use the corresponding original minor matrices \(K^0_{ab}\) built from \(B_{JJ}\) and \(R_0=(A_{JJ}B_{JJ}+2B_{JJ}A_{JJ}-z)^{-1}\).
Indeed replacing \(M\) by its zero-padded original minor and \(B\) by its zero-padded \(JJ\) block costs \(O(k)\) rank.
Compressing to \(H_{t-1}\) and adjoining an identity on its complement also costs \(O(k)\) rank.
More precisely compare \(P_{t-1}(M-z)P_{t-1}+1-P_{t-1}\) with the direct sum of \(M_J-z\) and the identity on \(I\).
Their difference has rank \(O(k)\), their inverses have the same rank discrepancy when defined, and deleting the complementary identity changes the inverse by another \(O(k)\) rank.
The resulting difference of each \(K_{ab}\) and its zero-padded minor version has rank \(O(k)\), irrespective of inverse norms and revealed row values.

For a tuple of distinct shifts in the open upper half-plane the four minor coefficient functions at each shift, together with those at their conjugates, are complex-linearly independent modulo scalars as free rational functions.
To check this, specialize the two self-adjoint indeterminates to real scalars \(A=x,B=b\) with \(b\ne0\).
At each pole in the rational variable \(3bx\), vanishing of the residue for all \(b\) forces the coefficients of \(K_{00},K_{11}\) to vanish and those of \(K_{01},K_{10}\) to be opposites.
The remaining difference is \([R_0-R_0^{\mathsf T},B]/2\).
Take \(B=\operatorname{diag}(b_1,b_2)\) with distinct nonzero entries and \(A=\operatorname{diag}(x_1,x_2)+u(E_{12}+E_{21})\).
At \(u=0\), the derivative of its \(12\) entry is
\[
 \frac{(b_1-b_2)^2}{2(3b_1x_1-z)(3b_2x_2-z)} .
\]
Taking residues in \(3b_1x_1\) at each distinct shift thus kills all the remaining coefficients.
The scalar and two-dimensional specializations both have nonsingular denominators around the evaluation points used for the real identities.
The [free-field identification](../audits/literature/MSY23/Yin_U004.md#msy23-u004) applies to the free semicircular pair, so these tests also exclude a scalar relation in its affiliated algebra.

**A joint area estimate for these restored determinants.**
Fix \(D\) and a compact set of \(D\)-tuples in the open upper half-plane with a fixed positive separation between any two shifts.
Divide \(J\) into four disjoint deterministic classes of asymptotic density \(1/4\), discarding or fixing up to three excess coordinates.
Use both real and imaginary parts of every \(K_{ab}\) at the chosen shifts as real symmetric matrices.
Every real unit linear combination of this family is nonscalar in the affiliated free limit, by the just-proved independence at the shifts and their conjugates.
Its limiting corner between any two different classes is nonzero.
Indeed permutation of the four equal free color projections fixes the two semicircular variables, so vanishing of one such corner gives vanishing of every ordered off-diagonal corner.
The affiliated element would commute with a nontrivial free color projection, forcing its bounded transform, and then the element itself, to be scalar as in the [sign-flag argument](#sign-flag-area).

Apply the bounded approximation and rank proof of that argument to this finite family.
The added left and right factors of \(B_{JJ}\) are bounded on its norm guard and preserve the rank bound for the difference of the true and regularized inverses.
Thus on a single original-minor event with complement \(Ce^{-cn}\), \(n=|J|\), every real unit combination has a positive fraction of singular values bounded below in each cross corner, uniformly on the indicated tuples.
Its bounded approximant can be taken linear in the combination, with the sum of the error ranks for the family smaller than a prescribed fraction of \(n\).
For this last assertion first obtain the positive fraction for the true free combinations, then choose the regularization and polynomial approximations as in the sign-flag argument.
The \(O(k)\) additional ranks from the restoration comparison above preserve these properties for every regular old compression.
The constants may depend on \(D\), the compact domain and its spacing.
For planar integration one may discard the poles for each fixed dimension and all its finitely many sign samples and restoration steps.

Consider a single restoration step and \(r\le D\) assigned shifts.
Condition on the information available before drawing the row, including the original-minor and cross-block guards.
Four Cartesian Cauchy--Schwarz inequalities bound the sixteenth power of the probability that all \(r\) determinant ratios have modulus at most \(N^{-3}\) by the probability that the same inequalities hold at all sixteen resamplings of the four blocks.
Taking the alternating sum of those values keeps only the four-distinct-block part of the quartic and increases the bound by at most a factor of sixteen.
Write \(u_p\), \(1\le p\le4\), for the independent differences of raw sign vectors in the four classes.
For each shift \(z_j\) set \(w_{pq,j}=(u_p^{\mathsf T} K_{ab}^{pq}(z_j)u_q)_{ab}\), where the superscripts denote the physical corner.
For vectors indexed by \(00,01,10,11\) put
\[
 h(v,w)=v_{00}w_{11}+v_{11}w_{00}-v_{01}w_{10}-v_{10}w_{01}.
\]
Expansion of the two quadratic products in the determinant shows that their fourth mixed difference in raw coordinates is four times
\[
 X_j=h(w_{12,j},w_{34,j})+h(w_{13,j},w_{24,j})+h(w_{14,j},w_{23,j}).
\]
The factor four comes from the two orders of each pair in each symmetric quadratic form.
The common geometric factor and the normalization \(N^{-2}\) in the Schur ratio show that all the resampling inequalities imply \(|X_j|\le C/N\) for every \(j\).

Call a shift bad at the first pair if \(|w_{12,j,00}|\le1\).
For any prescribed subset of \(s\) shifts, the probability that they are all bad at this pair is at most \(C_D n^{-s/2}\).
Use the real parts of the \(00\) kernels at those shifts, condition on \(u_1\), and apply the [disjoint-basis estimate (2)](#sign-flag-area) to \(u_2\), with the exponentially small exceptional \(u_1\) there.
The estimate for a fixed-radius box follows by covering it with a bounded number of unit balls.

Now fix \(u_1,u_2\) and the exact set of bad first-pair shifts, with \(r-s\) shifts remaining.
The terms other than \(h(w_{12,j},w_{34,j})\), viewed as linear functions of \(u_4\), have coefficient vectors in a fixed real subspace \(E\) of dimension at most \(16D\).
It is spanned by the real and imaginary parts of the fourth-class vectors \((K_{ab}^{p4}(z_j))^{\mathsf T}u_p\) for \(p=1,2\).
This subspace is fixed before drawing \(u_3\), even though the multipliers of its vectors can depend on \(u_3\).
For any real unit combination \(t\) over the remaining shifts, the main term \(\sum_jt_j\operatorname{Re}h(w_{12,j},w_{34,j})\) has coefficient vector at \(u_4\) equal to a real linear combination of the \(34\) kernels transposed and applied to \(u_3\).
The norm of its array of real coefficients on the full real and imaginary kernel family is at least one, since the coefficient of \(w_{34,j,11}\) is \(t_j w_{12,j,00}\) and the shifts used here satisfy \(|w_{12,j,00}|>1\).
Apply the output-spread proof of (2) on the unit sphere of the *whole* real kernel family with input \(u_3\), projecting off \(E\), the deleted output coordinates and the bounded-approximation error ranges.
Homogeneity then gives its simultaneous lower bound \(c\sqrt n\) for every such coefficient array, allowing unbounded norms for the individual \(w_{12,j}\).
Consequently the complete real coefficient vectors of \((\operatorname{Re}X_j)_j\) at \(u_4\) have least singular value at least \(c\sqrt n\) after each sufficiently small fixed-fraction deletion of output coordinates, outside conditional probability \(Ce^{-cn}\) over \(u_3\).
Indeed the nuisance terms vanish under the extra projection onto \(E^\perp\), and applying this projection simultaneously with the coordinate deletions and the rank-error projections only decreases the norm.
The maximum-volume basis extraction and (2) now bound the joint small-ball probability at \(u_4\) by \(C_D n^{-(r-s)/2}\).
For \(s=r\) this last probability is bounded by one.
Multiply by the upper bound for the prescribed \(s\) first-pair failures, sum over their finitely many possible subsets, and take the sixteenth root.
The conditional probability of the original simultaneous determinant-ratio tests at this step is at most \(C_D n^{-r/32}\).

Assign \(D=64\) separated bad parameters to restoration steps, allowing repeated steps.
For each assignment the chronological conditional estimates multiply to \(C_D n^{-2}\), and there are at most \(k^D\) assignments.
The original-minor and cross-block exceptional probabilities are paid once.
The [separated-tuple area argument](#sign-flag-area) therefore gives a summable probability that on a fixed disk a set of area greater than any prescribed \(v>0\) has some restoration ratio of modulus below \(N^{-3}\), at \(k\asymp\log^3N\).
Outside this bad set the restored log determinant exceeds its starting compression log determinant minus \(3k\log N\).
The normalized negative part of any realized characteristic log has uniformly bounded disk \(L^2\) norm, since it is bounded by the sum of translated \(\log^-(|z|)\) kernels divided by \(N\).
The positive part on a fixed disk is bounded by a constant on the sign-input norm guard.
Thus the loss on a set of area \(v\) is \(O_R(\sqrt v)\) in the normalized disk comparison.
This planar argument does not supply summable deviations at one prescribed nonreal shift.

<a id="trim-assembly"></a>
## Starting from the trimmed principal minor

Fix \(k=2\lfloor\log^3(N+3)/2\rfloor,\ n=N-k,\ h=q_n\).
At the beginning of the reverse restorations the space is embedded in the \(J\) coordinates and is orthogonal there to the columns of \(B_{JI}\).
The extra terms \(A_{JI}B_{IJ}+2B_{JI}A_{IJ}\) in the full \(JJ\) block vanish after compression on both sides.
Hence the starting determinant for the restorations agrees with the outcome of the \(k\) old-minor flag deletions.
The two probability bounds may expose the inputs in different orders because the final exceptional sets are combined by a union bound.

Write \(t_1(z)\le\cdots\le t_n(z)\) for the singular values of \(M-zI\) on the old sites and \(b_j=N^{-1}\sum_{i>j}\log t_i\).
By the [two-trim result for this original principal minor](Yin_C_F0351_v1.md#minor-trims), on each disk \(b_{2h}\to u=\tau\log|p-\cdot|\) in \(L^1\) and \(\int (h/N)\log^-t_{2h+1}\to0\) almost surely under every coupling.
Use the [original-law arithmetic overlap estimate](Yin_C_F0351_v2.md#discrete-overlaps) for the sign columns.
At each shift separated from the real axis choose the largest \(1\le r\le2h\) with \(t_r/t_{r+1}<N^{-40h}\), taking zero if there is none.
The overlap estimate and the [compound-minor comparison](Yin_C_F0351_v1.md#adaptive-gap) give log determinant at least \(Nb_r-O(h\log N)\) after the first \(r\) deletions.
The failure probability is at most \(O(hn^{-5/4}+(1+k)N^{-3})+Ce^{-cn^{1/8}}\) uniformly on bounded regions separated from the axis, and at \(r=0\) the initial log is exact.
Fubini, Markov and Borel--Cantelli give vanishing exceptional area almost surely on each such region.
The remaining adjacent ratios through \(2h\) give
\[
 b_r\ge b_{2h}-(2h/N)\log^-t_{2h+1}-160h^3\log N/N .
\]
Multiply the subsequent deletion and restoration ratios on the complement of the exceptional sets.
At most \(k\) of each are used, giving total normalized log cost at most \(5k\log N/N\).
The two exceptional areas tend to zero almost surely by their summable fixed-area deviations.
Consequently \(U_N(z)=N^{-1}\log|\det(P_N-zI)|\ge b_{2h}(z)-(2h/N)\log^-t_{2h+1}(z)-o(1)\) on the remaining region with deterministic vanishing error.
On each disk \(U_N^-\) has a deterministic bounded \(L^2\) norm by Jensen applied to the \(N\) translated negative logarithmic kernels.
The free potential has bounded local \(L^2\) norm by the same argument for the compactly supported Brown measure.
Cauchy--Schwarz handles the exceptional sets and a strip of vanishing width about the real axis, by first using the countable regions \(|\operatorname{Im}z|\ge1/j\).
Thus \(\int (u-U_N)_+\to0\) almost surely on every disk.
For the opposite bound the [trimmed full-matrix potential](Yin_C_F0186_v36.md#statement) converges to \(u\) in local \(L^1\), and the omitted positive logarithms divided by \(N\) are \(o(1)\) uniformly on the disk since the input norms are eventually bounded almost surely.
This proves local \(L^1\) convergence.
Taking distributional Laplacians and using tightness gives the weak Brown limit.
The [terminal equivalence](Yin_C_F0186_v36.md#statement) gives the asserted marginal series by applying the result to independent dimensions and the converse Borel--Cantelli lemma.
Arbitrary radii and thresholds follow from integer disks and smaller positive rational thresholds.

## Current assessment
[Selected decision](#decision-sign-terminal-reviewed)

## Assessment history

### Decision sign-terminal-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:53 |
| status | open |
| reason | The Wigner minor comparison, multishift estimates and paired restorations give a complete candidate for the sign model. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two Rademacher inputs](#statement) | Summable planar terminal deviations, local potentials and the weak Brown limit. |
| argument | [Actual sign flags](#argument) | The physical minor and the simultaneous quadratic tests. |
| support | [Restoring fresh borders](#paired-sign-restoration) | The rank-two extension and its fourth mixed difference. |
| support | [Assembling the trim](#trim-assembly) | Initial arithmetic overlap and full-chain integral estimate. |

### Decision sign-terminal-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:58 |
| status | proved |
| reason | Independent whole-proof review confirmed the planar terminal series and the Brown limit for the two sign matrices, with separate independent inspection of the physical-corner and multishift estimates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sign model and limits](#statement) | Both sign inputs, any cross-size coupling, local logarithmic potentials and summable integrated deviations. |
| argument | [Complete proof](#argument) | Physical corners, sign flags, paired restorations and the final comparison. |
| support | [Quadratic ratios](#sign-flag-area) | Simultaneous tests on a genuine sign column of the old-minor flag. |
| support | [Quartic ratios](#paired-sign-restoration) | Multishift lower bounds for the Schur determinant of each restored pair. |
| support | [Terminal series](#trim-assembly) | Initial overlap, two trims and the every-coupling passage. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v5.md#sign-whole-proof) | All conclusions for the stated sign law. |
| review | [Independent physical-corner review](../audits/reviews/Yin_R_F0358_v5.md#sign-corner-review) | Free and finite corners, conditional concentration and integration over separated parameters. |
