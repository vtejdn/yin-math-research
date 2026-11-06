---
author: Yin
---

<a id="vector-visibility-and-sixth-cancellation"></a>
# Vector visibility and exact cancellation of a residual sixth-degree matching

This ordinary development for Yin, dated 2026-11-06T11:04 UTC, tests the complete single-pole polynomial for [F13](../tasks/Yin_T_F0013_v1.md#contract) after the [residual-matrix calculation](../drafts/Yin_D_F0010.md#residual-matrix-quadratic-noise-test).
It strengthens the finite-dimensional matrix input, but also gives an exact cancellation of linearly many selected residual determinant coefficients by the pole term at a same-sign pole of order \(N\).
The example retains the true spectral relation \(Ee=0\), the residual energy, the good background equation, fixed positive-frame coefficients and realizability of each finite minor under one fixed collection of original laws.
Its off-support rectangles fail, so it is not a counterexample on the good-minor event needed by the actual probability argument.
Only the displayed matching is canceled; no assertion is made that the entire sixth layer vanishes.
This is ordinary development and authoring self-checking, without independent review or Claim adoption.
The [D10 test](../drafts/Yin_D_F0010.md#vector-visibility-and-sixth-cancellation) is development provenance; the complete calculation is fixed here.

<a id="cross-input-vector-visibility"></a>
## The same cross-input map is visible in every vector direction

Let \(A_1,\ldots,A_d\) be fixed real symmetric size-three coefficients with
\[
 \chi_A=\inf_{\substack{u,v\in\mathbb C^3\\\|u\|=\|v\|=1}}
                \sum_j|v^*A_ju|^2>0,
\]
and put
\[
 C_{jl}(H)=A_jHA_l+A_lHA_j.
\]
There is a fixed \(\gamma_A'>0\) such that
\[
 \sum_{j<l}\|C_{jl}(H)u\|^2
       \ge\gamma_A'\|H\|_F^2\|u\|^2
 \tag{Residual-vector-visibility}
\]
for every real symmetric \(H\) and real vector \(u\).
This is stronger than the earlier residual matrix-norm estimate, but is not a lower bound for \(|u^TC_{jl}(H)u|\).

Suppose, to the contrary, that \(H\ne0\), \(u\ne0\), and all \(C_{jl}(H)u\) vanish.
Let \(v_j=A_ju\), \(V=(v_1,\ldots,v_d)\), and \(r=\operatorname{rank}H\).
The frame implies that \(V\) has full row rank three.
The real symmetric matrix \(V^THV\) is diagonal, since its off-diagonal scalar is \(\tfrac12u^TC_{jl}(H)u\), and its rank is exactly \(r\) because \(V\) is surjective and \(V^T\) injective.
Let \(J\) be its \(r\) nonzero diagonal positions.
For \(j\notin J\), the entire column \(V^THv_j\) vanishes, so injectivity of \(V^T\) gives \(Hv_j=0\).
The \(r\) vectors \(Hv_l\), \(l\in J\), are linearly independent by their nonzero diagonal images under \(V^T\); hence they span \(\operatorname{range}H\).
For \(j\notin J\) and \(l\in J\), the original vector equation now reads
\[
 0=C_{jl}(H)u=A_jHv_l+A_lHv_j=A_jHv_l.
\]
Thus every inactive \(A_j\), \(j\notin J\), annihilates \(\operatorname{range}H\).
If \(r<3\), choose a nonzero real vector \(x\) in this range.
Then at most \(r\) of the vectors \(A_jx\) are nonzero, contradicting the frame's requirement that they span three dimensions.
If \(r=3\), every inactive \(A_j\) is zero, so only three coefficient matrices remain.
For complex \(w\), their three columns \(A_jw\) have a determinant that is a homogeneous polynomial of degree three in three variables.
It is either identically zero or has a nonzero complex zero, as follows by restricting to a two-dimensional complex plane and applying the fundamental theorem of algebra to the resulting homogeneous binary polynomial.
Both possibilities contradict full row rank for every nonzero complex \(w\).
This last step is where the complex-direction frame, rather than only a real-direction frame, is essential.
Compactness over real symmetric \(\|H\|_F=1\) and real \(\|u\|=1\) proves the uniform constant.

There is a genuine local determinant consequence, but it does not yet concern discrete coefficient preservation.
For a real unit vector \(u\), use an orthonormal basis with first vector \(u\) and write a positive semidefinite corank-one matrix and a symmetric perturbation as
\[
 S_0=\begin{pmatrix}0&0\\0&Q\end{pmatrix},
 \qquad H_0=\begin{pmatrix}a&b^T\\b&D\end{pmatrix},
 \qquad Q>0.
\]
The exact determinant is
\[
 \det(S_0+tH_0)
 =ta\det(Q+tD)-t^2b^T\operatorname{adj}(Q+tD)b.
 \tag{Residual-local-curvature}
\]
If \(H_0u\ne0\), either the linear coefficient is nonzero, or \(a=0,b\ne0\) and the quadratic coefficient is strictly negative.
This detects a matrix direction beyond the vanishing rank-one scalar projection, but it says nothing by itself about the complete original-law sign polynomial, where both \(S_E\) and \(z\) vary.

<a id="three-group-exact-coefficients"></a>
## Three physical groups with a nonzero residual coefficient and opposite pole coefficient

Write \(S_{ab}=E_{ab}+E_{ba}\), and use the following fixed real symmetric coefficient basis:
\[
 \begin{aligned}
 A_1&=E_{11}+E_{22},&
 A_2&=E_{22}+S_{12},&
 A_3&=-E_{22}+E_{33},\\
 A_4&=-E_{22}+E_{33}+S_{12}-S_{23},&
 A_5&=S_{13},&
 A_6&=S_{23}.
 \end{aligned}
 \tag{Sixth-cancellation-coefficients}
\]
These matrices span all real symmetric \(3\)-by-\(3\) matrices: in particular \(E_{22}=A_2+A_3-A_4-A_6\), and the other five standard directions then follow immediately.
The [symmetric-basis argument](Yin_L_F0063_v3.md#positive-frame-physical-boundary) therefore gives \(\chi_A>0\) with the required complex-direction convention.

For three physical positions, expose the six distinct raw variables through
\[
 U_1=x_1A_1+y_1A_2,\qquad
 U_2=x_2A_4+y_2A_5,\qquad
 U_3=x_3A_4+y_3A_6.
\]
Let \([m]\) denote the coefficient of
\(m=x_1y_1x_2y_2x_3y_3\), and set
\[
 Q=U_1^2+U_2^2+U_3^2,\qquad
 v=U_1e_1+U_2e_1+U_3e_1.
\]
The exact two coefficients are
\[
 [m]\det Q=-8,\qquad
 [m]\bigl(v^T\operatorname{adj}(Q)v\bigr)=2.
 \tag{Sixth-cancellation-two-coefficients}
\]
Here is a direct verification, retaining every term relevant to this monomial.
The cross coefficients in the three \(U_k^2\) are
\[
 C_1=\begin{pmatrix}0&2&0\\2&2&0\\0&0&0\end{pmatrix},
 \quad C_2=\begin{pmatrix}0&-1&1\\-1&0&1\\1&1&0\end{pmatrix},
 \quad C_3=\begin{pmatrix}0&0&1\\0&-2&0\\1&0&-2\end{pmatrix}.
\]
The corresponding cross coefficients in \(U_ke_1e_1^TU_k\) are
\[
 D_1=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},
 \quad D_2=\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix},
 \quad D_3=0.
\]
Extracting the coefficient of \(str\) in
\(\det(s(C_1+\delta D_1)+t(C_2+\delta D_2)+rC_3)\)
gives
\[
 -8+2\delta+2\delta^2.
 \tag{Sixth-cancellation-mixed-determinant}
\]
For example the matrix has entries \(M_{11}=0\), \(M_{12}=(2+\delta)s-t\), \(M_{13}=t+r\), \(M_{22}=2s-2r\), \(M_{23}=(1+\delta)t\), \(M_{33}=-2r\), so the coefficient follows directly from its three-by-three determinant.
At \(\delta=0\) this proves the first coefficient.
For the second, terms \((U_ke_1)^T\operatorname{adj}(Q)(U_le_1)\) with \(k\ne l\) have odd total degree in physical groups \(k,l\), whereas \(m\) has degree two in each group.
They therefore do not contribute.
The remaining terms are exactly the derivative at zero of
\(\det(Q+\delta\sum_kU_ke_1e_1^TU_k)\), whose coefficient is the derivative of (Sixth-cancellation-mixed-determinant), namely \(2\).
Finally the exact rank-one determinant identity gives
\[
 [m]\det(Q+\delta vv^T)=-8+2\delta
 \tag{Sixth-cancellation-rank-one}
\]
for every \(\delta\); the quadratic term in the auxiliary mixed calculation is not retained in this rank-one update.

<a id="same-sign-pole-full-matching-cancellation"></a>
## An exact spectral decomposition cancels a linear matching

Let \(n=N-1\), let \(w=n^{-1/2}(1,\ldots,1)^T\), and set
\[
 e=w\otimes e_1,\qquad
 E=c(I_{3n}-ee^T),\qquad
 \lambda=c(1+4n),\qquad
 Z=E+\lambda ee^T=cI_{3n}+(\lambda-c)ee^T.
 \tag{Sixth-cancellation-spectral-data}
\]
Here \(c>0\) is fixed and sufficiently small, as specified below.
These are real symmetric spectral data with \(Ee=0\), \(\|e\|=1\), positive pole of order \(N\), and
\(\|E\|_F^2/N=c^2(3n-1)/N\le3c^2\).
The corresponding actual candidate minor is
\[
 M=Z^{-1}=c^{-1}I_{3n}
              +(\lambda^{-1}-c^{-1})ee^T.
 \tag{Sixth-cancellation-minor}
\]
It is positive definite and has norm \(c^{-1}\).

Partition any \(3\lfloor n/3\rfloor\) physical positions into disjoint triples and choose the input pairs \((1,2),(4,5),(4,6)\) in each triple.
For its six selected variables, the top degree-six coefficient of the full Schur determinant depends only on those variables, so all other raw border variables may be set to zero for this extraction.
Using the original normalization, one obtains
\[
 R^TZR=\frac cN\bigl(Q+\delta vv^T\bigr),
 \qquad
 \delta=\frac{\lambda-c}{cn}=4.
\]
The top degree-six part of \(\det(A_0+D_i-R^TZR)\) is \(-\det(R^TZR)\).
Consequently its selected coefficient is
\[
 -\frac{c^3}{N^3}(-8+2\delta)=0.
 \tag{Sixth-cancellation-full-selected-zero}
\]
For the residual matrix \(E=c(I-ee^T)\), the identical calculation instead has \(\delta_E=-1/n\), giving the nonzero coefficient
\[
 [m]\det S_E=\frac{c^3}{N^3}(8+2/n).
 \tag{Sixth-cancellation-residual-selected-nonzero}
\]
Thus \(\det S_E\) has linearly many disjoint selected raw sixth-degree monomials at a polynomial scale, but every one of this matching disappears in the complete determinant.
Equivalently the two terms in
\[
 \frac N\lambda\det S
   =\frac N\lambda\det S_E-z^T\operatorname{adj}(S_E)z,
 \qquad z=\sqrt N\,R^Te,
\]
have exactly equal selected coefficients and cancel.
This uses the true \(E,e,\lambda\) decomposition, including the off-diagonal physical blocks of \(E\).
Because the full polynomial has degree at most six, no lower-degree term or other repeated-variable monomial can contribute to a sign monomial using all six of these distinct variables after two-copy pairing.
The same selected sixth-degree matching is therefore absent after that pairing.
Other sixth-degree monomials, other matchings and lower complete layers have not been evaluated or shown to vanish.

<a id="fixed-law-realization-and-rectangle-boundary"></a>
## One fixed original law realizes the minors, while the required rectangles exclude them

Choose \(c\) so small that \(3c^2\le1\) and
\(c^{-1}>2\sum_j\|A_j\|+2\), and fix
\[
 A_0=c^{-1}I_3+c\sum_jA_j^2,\qquad \theta_N=0.
 \tag{Sixth-cancellation-affine-term}
\]
Since \(A_0\succeq c^{-1}I_3\) and the free noise has norm at most \(2\sum_j\|A_j\|\), the corresponding free pencil is strictly positive with a gap at zero.
For the displayed minor,
\[
 g_E=\frac{cn}{N}I_3-\frac cN E_{11},\qquad
 B_E=A_0-\sum_jA_jg_EA_j
     =c^{-1}I_3+\sum_jA_j(cI_3-g_E)A_j.
\]
Here \(cI_3-g_E=(c/N)(I_3+E_{11})\succeq0\), so \(B_E\) is positive definite.
Moreover
\[
 \|B_Eg_E-I_3\|
 \le\frac{2+2c^2\sum_j\|A_j\|^2}{N}
 <\tfrac12
\]
eventually.
Taking the exposed diagonal coordinates equal to zero gives \(D_i=0\) and a positive definite \(B=B_E\) with the same sign as \(\lambda\).
The residual energy, polynomial norm guard, actual eigenvector relation and good background equation of the single-pole setup are satisfied.
The physical blocks of \(e\) all have norm \(n^{-1/2}\), so the individual eigenvector is also flat.

The coefficient basis permits an exact original-model realization for every sufficiently large \(N\), using laws fixed once for the entire sequence.
Each off-diagonal physical block of \(M\) is the symmetric matrix
\((\lambda^{-1}-c^{-1})E_{11}/n\).
Express it uniquely in the basis \(A_1,\ldots,A_6\), and multiply those scalar coordinates by \(\sqrt N\) to obtain the required raw off-diagonal values.
Likewise express \(M_{kk}-A_0\) in that basis and multiply by \(\sqrt N\) to obtain the raw diagonal values.
All these requirements over the countable set of dimensions form countable sets of real numbers.
For the off-diagonal law, assign positive symmetric atom masses to zero and to every required value and its negative, small enough that their total mass and total second moment are both less than one half.
Complete the remaining mass with a symmetric pair \(\pm b\), choosing \(b\) to make the total variance exactly one.
This produces one fixed centered variance-one law containing every required off-diagonal coordinate.
For the diagonal law, assign positive symmetric masses to zero and every required diagonal value and its negative, choosing their total mass less than one and their total second moment finite, and put the remaining mass at zero.
The resulting fixed diagonal law is centered and has finite second moment.
Use independent copies for every upper-triangular coordinate and input, and mirror the lower entries as prescribed.
Each finite collection specifying the minor and \(D_i=0\) then has strictly positive probability.
The probabilities may be extremely small and are not claimed to be bounded below as \(N\) grows; there is no changing-law or dependent-coordinate substitution.

The construction nevertheless fails an explicit hypothesis of the intended good-minor argument.
For every pair of disjoint physical sets \(I,J\), its cross block \(M[I,J]\) has rank at most one.
For the nonempty supports of the [positive-frame rectangle theorem](../claims/Yin_C_F0194_v17.md#statement), it has \(3|J|>1\) columns, so its least singular value is zero.
Thus these actually realizable minors lie in the rectangle exception, even though their chosen eigenvector is flat and their background equation is good.
They do not refute a statement restricted to that good rectangle event or a high-probability original-model estimate.

<a id="complete-matching-next-interface"></a>
## The remaining inference for F13

The example rules out preserving an arbitrarily chosen residual determinant matching solely from positive frame, vector visibility, a fixed residual energy bound, the exact spectral decomposition and the good background equation.
Actual realizability alone does not repair that inference: the construction is realizable, but its full random-geometric restrictions are missing.
Conversely the failed rectangle hypothesis is not a proof that rectangles suffice to preserve another complete matching.
The first unsupported step in the current determinant route remains a complete original-law estimate for the pole-updated Schur polynomial on the actual good-minor event, using enough of its simultaneous geometry to control the cancellation just exhibited.
It must either retain a sufficient full layer or otherwise control the complete value and its graph denominator; the ordinary residual entry estimate and the local curvature calculation do not supply it.
The actual probabilities of the remaining same-sign, indefinite and multiple-pole branches, or a direct total negative-logarithmic-loss estimate along favorable dimensions, remain unresolved.
No new original-parent floor, favorable dimensional subsequence or F13 completion is asserted.
