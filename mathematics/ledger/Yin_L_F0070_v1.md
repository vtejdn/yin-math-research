---
author: Yin
---

# What survives of Han's trace observations for atomic Wigner inputs

The 18 November 2026 strategy exploration for [F0012](../tasks/Yin_T_F0012_v3.md#contract) compares Han's [two-moment tensor-pencil argument](../audits/literature/Han26b/Yin_U001.md#han26b-u001) with the [complete convergence of cyclic clipped potentials](../claims/Yin_C_F0359_v2.md#clip).
Yin's main research agent and three strategy delegates examined spectral-parameter variation, deletion of unreliable trace observations and physical borders for repeated variables.
The recorded tests concern the original fixed-law model and specify the additional hypotheses at each partial step.

<a id="spatial"></a>
## Spectral variation for a correlated sign product

The [disk criterion and Taylor-minor test](../claims/Yin_C_F0359_v3.md#statement) move the determinant evaluation within a small fixed disk.
For the first Taylor coefficient the new information is the pairing of a bottom right singular vector with a bottom left singular vector.
A lower bound on the second-smallest value alone gives no such pairing.
For the pilot take \(U=A+2B,\ V=3A+B\) with \(A,B\) independent real sign Wigner matrices, and put \(L=UV-zI\) at a fixed nonreal \(z\).
The [fixed-real-shift result](../claims/Yin_C_F0356_v3.md#statement) does not provide the desired disk test near \(i\).
For this real quadratic, the [reviewed two-moment trims](../claims/Yin_C_F0186_v42.md#statement) already control the scalar product at each fixed nonreal center.
With \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\) and \(q=2h_N\), its top \(N-q\) log product divided by \(N\) tends to the free potential, and \((q/N)\log^-s_{N-q}\to0\), almost surely under each coupling.
Thus this pilot does not require a polynomial floor for \(s_{N-q}\).
In the [first-gap argument](../claims/Yin_C_F0359_v3.md#minors), descend from \(s_{N-q}\), using relative threshold \(b=N^{-Cq}/(4Nq)\).
Each additional value included before the gap is at least \(s_{N-q}b^q\).
Relative to the top \(N-q\) product the logarithmic loss is at most \(q\log^-s_{N-q}+q^2|\log b|=o(N)\).
At the first gap of order \(k\), a terminal overlap minor of size at least \(N^{-Cq}\) then supplies the required disk maximum by (2) of that argument.
If all ratios exceed or equal \(b\), the center already suffices.
Only a bound at the selected gap is needed.
The scalar upper estimate on compact subdisks follows by the cyclic clipped bound and the chart identity.
Consequently the remaining test for this quadratic is a summable failure probability for the overlap at that gap on a dense countable set of nonreal centers.
Disks with such centers also cover the real line.

For a unit bottom right singular vector \(x\) with singular value \(s_N\), the identity \(L^*\overline{Vx}=\overline{V Lx}\) follows from real symmetry.
Also \(\|U\|\|Vx\|\ge |z|-s_N\).
When the second-smallest value is \(\sigma>0\), the distance of \(\overline{Vx}/\|Vx\|\) to the bottom left line is at most \(\|V\|s_N/(\sigma\|Vx\|)\), provided the bottom direction is simple and \(Vx\ne0\).
This follows by expansion in the left singular basis for \(L\).
The scalar to estimate when this error is small is \(|x^T Vx|/\|Vx\|\).
The transpose is essential even though \(x\) is complex.
The favorable event would be a polynomial overlap when \(s_N\) is exceptionally small, with a summable probability of failure and adequate control of the other directions.
A projection estimate for a predetermined vector does not apply to this \(x\) selected by both matrices.

There is an explicit deterministic obstruction even within this product structure.
Let \(S\) be the upper nilpotent shift of size \(\ell\), \(K\) the coordinate reversal, \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) and \(Q=\operatorname{diag}(1,-1)\).
Set \(M=I_\ell\otimes J+S\otimes I_2,\ V=K\otimes Q,\ U=MV\).
Since \(VMV=M^T\) and \(V\) is a symmetric orthogonal involution, \(U\) is real symmetric.
The bounded real symmetric colors \(A=(2V-U)/5,\ B=(3U-V)/5\) give \(UV=M\).
In a unitary basis for \(J\), \(M-iI\) is the direct sum of \(S\) and \(S-2iI\).
The first has one zero and all remaining singular values equal to one, and the second has least singular value at least one.
Yet the characteristic polynomial \((t-i)^\ell(t+i)^\ell\) has zero coefficients in all orders below \(\ell\) at \(i\).
This rules out a deterministic inference from the second-value floor, boundedness and factor symmetry to low-order spectral visibility.
The colors are prescribed matrices and supply no counterexample to the Wigner assertion.

<a id="localization"></a>
## Polynomial localization and almost every parameter

For fixed colors with finite second moments, \(\mathbb E\sum_\ell\|H_\ell\|_{\rm HS}^2=O(N)\).
The event \(\max_\ell\|H_\ell\|_{\rm HS}\le N^2\) fails with probability \(O(N^{-3})\).
In Han's proof this replacement for the cutoff in (1.5) changes the scale choices, so substituting the new error into the printed theorem would skip an argument.
The punctured operator and the vectors producing its inactive singular directions now have bounds \(C N^2\) on this event, by (6.1)–(6.3) and Cauchy–Schwarz.
Choose a Grassmannian mesh \(c\delta N^{-2}\), a coordinate mesh \(c\delta N^{-5/2}\) and a gap with \(C N^2\eta\le\delta\).
The new costs are \(N^{O_p(N)}\), and the exponent of \(\delta\) in the surplus count is retained.
In Lemma 3.8 one can enlarge the constant multiplying \(\log N\) in the logarithm of the inverse scale and choose the next inactive scale \(N^{-4}\delta\).
For the projected Gram truncation use \(D_{d+1}\ge2e(D_d)+8\), so the image error \(C N^2 N^{-D_{d+1}/2}\) is negligible.
The inverse frame and triangular reconstruction consequently require different fixed powers of \(N\).

A summable polynomial floor for almost every fixed chart parameter suffices together with C359v2.
The floor exponent may depend on that parameter.
For each coupling the measurable event that some integer exponent works eventually has probability one at almost every parameter, hence holds for almost every parameter on almost every sample by Fubini.
Intersecting the probability-one clipped limits for integer exponents gives \(U_N\to u\) at those parameters.
The positive part is bounded locally by the uniform upper bound from clipping at \(N^{-1}\).
For the negative part, Jensen and the root representation bound its squared spatial integral by \(\int_{|t|<1}(\log|t|)^2dA\), uniformly over all root configurations.
This yields local \(L^1\) convergence under each coupling without a parameter-uniform floor.
This reasoning does not turn a failure probability of order \(o(1)\) into a summable one.

<a id="erased"></a>
## Removing observations on diagonals and irregular edges

Han's Wigner frame observes both copies of every off-diagonal edge and the diagonal variables in (6.9)–(6.14).
To allow arbitrary diagonals, including zero, omit the diagonal observation from every inverse row.
More generally retain off-diagonal edges only where every participating color comes from a bounded compact density component.
A law on the real line must be real throughout for the real-coordinate model.
A planar color needs a genuine two-dimensional component.
Use independent mixture indicators with these conditional component laws.
The following argument suggests a first extension when these components have sufficiently high mass, including the case of absolutely continuous off-diagonals with unbounded densities, which admit bounded compact restrictions of mass arbitrarily close to one.

Write \(V\) for Han's real space of adjoint blocks, \(p=\dim_{\mathbb R}V\), \(H_j\) for its coefficient multipliers and \(\mathcal D\) for the trace kernel.
On a nonzero irreducible factor the coefficient ranges span each of the two coordinate representations by irreducibility.
The adjoint generators \(H_j\) therefore have trivial common kernel.
There is also no nonzero subspace of \(\mathcal D\) invariant under all \(H_j\). [Doubled-algebra argument](../audits/literature/Han26b/Yin_U001.md#doubled-algebra)

The Gram span \(E\) of a row profile can now be any nonzero subspace of \(V\).
For \(Y=Y_\sigma(E)\), take the right singular space of \(v\mapsto(P_{Y^\perp}v,P_{\mathcal D^\perp}v)\) on \(E\) at singular values at most \(\tau\), of dimension \(c\).
There are uniform small \(\tau,\sigma_0>0\) with \(c<\dim Y\) for \(0<\sigma\le\sigma_0\).
Indeed, a failing sequence with cutoffs tending to zero has subsequences with all dimensions fixed and the subspaces converging.
Triviality of the common kernel forces the limiting \(Y_0\) to be nonzero.
In the limit \(H_j E_0\subset Y_0\) by the inactive singular cutoff.
The limiting right singular space lies in \(Y_0\cap E_0\cap\mathcal D\).
Failure of the strict inequality therefore implies \(Y_0\subset E_0\cap\mathcal D\), making \(Y_0\) invariant, a contradiction.

For a test of the resulting frame, allow unrestricted coordinates on at most \(\eta_0 N+1\) sites per inverse row, including the diagonal, and impose the trace kernel on the others.
If the fixed-profile anchor argument misses at most \(\kappa N\) other outputs, the remaining exponent of the net radius is at least \([1-p(\eta_0+\kappa)]N-O_p(1)\).
Here a good coordinate close to \(Y\) and \(\mathcal D\) costs at most \(c\) free dimensions, by the right singular cutoff above.
At an erased site even the cost \(p\) is affordable.
Deterministic union over the erased sets costs at most \(2^N\).
For \(g\) colors and coefficient size \(m\), one can test \(\eta_0=\kappa=1/(16p_*)\) with \(p_*=4m^2\ge p\).
If the missed component mass in each off-diagonal color is less than \(1/(256gp_*^2)\), a specified set of at most \(p_*\) anchors misses all-good status at a given outside output with probability at most \(1/(256p_*)\).
Chernoff and a polynomial union over anchors, and separately over inverse rows, give exponentially small exceptions.
These global exceptions must be paid once outside the net union.
The remaining small-ball estimate conditions only on the relevant whole-atom membership pattern and independent exterior, as in Han's Lemma 6.1.

A proof of the masked frame must carry the approximate trace condition after projecting profiles onto a Gram eigenspace and rounding to a Grassmannian center.
For a good site the new distance to \(\mathcal D\) is bounded by the profile projection error plus the subspace mesh, so the Gram thresholds must be chosen before the tube covering at the retained rank.
With a frame uniform over erased sets, select the actual sets indicated by the marks.
Then freeze the marks and the bad atoms for relative anti-concentration using derivatives in the good off-diagonal coordinates only.
Use the unconditional good-coordinate bound at this stage and add the probability of the frame exception.
Conditioning on the frame itself would destroy independence.
Although a conditional polynomial might be identically zero at a prescribed shift, monicity in the cyclic spectral parameter implies by Fubini that for almost every fixed shift the determinant is nonzero almost surely for all sizes.
For such a shift the same property holds conditionally for almost all frozen data and for each triangular factor.
The constant drift is invertible off the finite spectrum of the deterministic coefficient matrix.
This gives a concrete path to a finite-variance, arbitrary-diagonal, high continuous-mass result.
A proof with all mask-dependent frame constants and its triangular application checked together has not been adopted.
A purely atomic law has no such good component.

<a id="sign"></a>
## What a sign flip detects

For one real sign edge \(b=\pm1\) and two sites with zero diagonal, a permissible scalar pencil has determinant \(F(t,b)=t^2-b^2/N\).
The derivative in the ambient real edge coordinate is \(-2b/N\).
Both sign samples give the same determinant for every \(t\), even when the determinant is nonzero.
A resampling operator on signs sees the polynomial only modulo \(b^2-1\).
Any replacement for Han's derivative step must exhibit a nonconstant coefficient after that reduction in the actual remaining independent variables.
The example also explains why a deterministic lower bound on a Euclidean coefficient Gram cannot by itself establish the required resampling estimate.
It tests a conditional proof mechanism at two sites and does not contradict a large-dimensional probability limit.

For the zero-diagonal two-sign Wigner pilot \(P_*=1+X^2Y^2+YX\), let \(F_N(w)=\det(wI-P_*)\) and let \(x_e,y_e\in\{-1,1\}\) be the two unscaled signs on a physical edge \(e\).
Simultaneous diagonal sign conjugation of the two matrices leaves the entire characteristic polynomial invariant.
Thus a Walsh coefficient can be nonzero only if its colored edge set has even total degree at every physical vertex.
The shortest mixed cycle uses the two colors on the same edge.
For every \(N\ge2\) its coefficient satisfies
\[
 [w^{N-1}]\,\mathbb E\bigl[F_N(w)x_ey_e\bigr]=-2/N .
\]
Indeed the characteristic coefficient is minus the trace, \(\operatorname{Tr}(YX)=2\sum_f x_fy_f/N\), and changing the sign of all \(X\)'s makes the \(X^2Y^2\) trace contribution to this expectation vanish.
The sum of squared coefficients across these \(\binom N2\) edges at this order is \(2(1-1/N)\).
This detects an unnormalized signal without controlling its relative strength in any fixed spectral disk.
Freeze the other variables and test the mixed four-point difference on each of several vertex-disjoint edges against the exterior singular product.
The open step is a joint conditional lower bound on the terminal event, where contributions of other characteristic coefficients can cancel.

<a id="quartic"></a>
## A border for a word with both colors repeated

For the real two-color pilot \(P=1+x^2y^2+yx\) use the two-channel matrix with rows \(((1-z)I+YX,X)\) and \((XY^2,-I)\).
Its Schur complement is \(P(X,Y)-zI\).
For a prescribed set \(I\) of deleted sites, use a subscript \(0\) for the complementary principal blocks, and set \(V=Y_{I^c I},\ D=Y_{II},\ W=(Y^2)_{I^c I}=Y_0V+VD\).
In the exterior, restrict the first left channel to \(V^\perp\) and the first right channel to \(W^\perp\) in the retained sites, using orthonormal column frames \(Q_L,Q_R\) for these complements of column ranges.
Indeed each occurrence of a fresh \(X\) edge has left directions \((Yv,0),(v,0),(0,v)\) and right directions \((v,0),(0,v),(Y^2v,0)\) at its endpoints.
Compressing away the deleted sites and their images removes terms with \(X_{I I^c}\) or \(X_{I^c I}\).
Eliminating the surviving \(-I\) channel leaves
\[
 Q_L^T (M+BVV^T)Q_R,\qquad M=P(X_0,Y_0)-zI,\quad B=X_0^2 .
\]
The correction is present because \((Y^2)_{I^c I^c}=Y_0^2+VV^T\).
If both cross blocks have full column rank, the determinant of
\[
 \begin{pmatrix}M&BV&V\\-V^T&I&0\\V^TY_0&D&0\end{pmatrix}
\]
has absolute value \(\det(V^TV)^{1/2}\det(W^TW)^{1/2}|\det Q_L^T(M+BVV^T)Q_R|\).
Elimination of the identity produces the border with off-diagonal blocks \(V,W^T\), and orthonormal bases adapted to their ranges give the two volume factors.
Conditioning on \(X_0,Y_0,D\) makes this augmented matrix affine in the independent cross columns of \(V\).

For \(k=|I|=O(\log N\log\log N)\), the [rectangular bound](../claims/Yin_C_F0351_v8.md#cross-block) controls \(s_{\min}(V)\).
To test \(W\), condition instead on \(V\), let \(Q\) project off its range, and note \(QW=QY_0V\).
For each fixed real unit vector \(u\) in that range, the unscaled off-diagonal coefficient vectors of \(QY_0u\) have Gram \(Q(I+uu^T-2\operatorname{diag}(u_i^2))Q\).
The diagonal correction is positive before subtraction with trace at most two, so at least \(N-2k-4\) directions retain eigenvalue at least \(1/2\).
The independent-entry projection bound used in the [real linear test](../claims/Yin_C_F0367_v1.md#linear-test) supplies a fixed norm floor outside exponential probability, conditionally on \(V\) and the diagonal.
Extending over the \(N^{-3}\) mesh in the \(k\)-dimensional sphere costs \(\exp(O(k\log N))\) on the \(N^2\) norm guard.
This controls the two volume normalizations, with summable exceptions.
It leaves the determinant of the compressed old block to compare to its trimmed singular products.

On the commuting curve \(xy=t,\ t^2+t+1-z=0\), the left and right observations of a simple scalar pole have coordinates \((y,1,x)\) and \((1,xy^2,y^2)\).
When \(t\ne0\), evaluating at three distinct positive \(x\)'s gives two invertible Vandermonde-type matrices, with exponents \(-1,0,1\) and \(0,-1,-2\).
This verifies a formal coefficient-span test away from \(z=1,3/4\).
It supplies neither a lower bound for dependent physical observations nor the initial two principal trims.
The missing estimate is joint control of the bottom singular vectors against the physical column pairs \((v,Y_0v)\) and \((v,X_0^2v)\).
This is the next experiment on the pilot.
For a commutative specialization that collapses the polynomial, symmetric matrix substitutions are also available as tests of rational identities.
For instance, a diagonal \(x=\operatorname{diag}(a,b)\) and \(y=\left(\begin{smallmatrix}0&c\\c&0\end{smallmatrix}\right)\) give \(\det([x,y]x-zI)=z^2+ab(a-b)^2c^2\), although the scalar commuting substitution gives zero for the polynomial.
Passing from matrix-valued residues to the required physical corner bound remains open.
