---
author: Yin
---

# Metric entropy of concentrated feasible Wigner graph images

The [conditional exterior probability and partial-alphabet bound](../claims/Yin_C_F0194_v33.md#statement) provide a threshold for the size of an admissible root dictionary.
An inverse theorem turns that exclusion into simultaneous concentration bounds for macroscopic row reservoirs, and a bounded-law example limits what a converse can yield at the same covering scale.
The [independent review of the three profile and lattice sections](../audits/reviews/Yin_R_F0200_v37.md#macroscopic-profiles-and-lattice) covers the guarded statements at their fixed fresh-row scope.
The [unguarded partial-alphabet theorem](../claims/Yin_C_F0196_v3.md#decision-tail-compensation-reviewed) supplies the same deterministic no-alphabet condition for all actual near-modes at the fixed nonreal shift outside an original-law event of probability at most \(Ce^{-cN^{1/8}}\).
Substitution into the Fourier proof below gives the same fresh-row exponents at that unconditional rate, since its other inputs are unit norm and the two fixed entry laws.
The [exterior subspace calculation](#conditional-subspace) and the [conditional determinant with a repeated interior block](#repeated-interior) have been checked in development.

<a id="macroscopic-row-profiles"></a>
## Concentration on every macroscopic reservoir

Use the finite-fourth-moment real Wigner hypotheses, fixed \(K\) and fixed \(z\notin\mathbb R\) of the [partial-alphabet estimate](../claims/Yin_C_F0194_v33.md#partial-alphabet).
Fix \(a,b>0\), \(0<\theta\le1\) and \(0<\eta<1\).
For \(\xi\) either original raw strict upper law, and fixed coefficients \(h\) and \(S\subset[N]\), define
\[
 \rho_\xi(h_S,t)=
 \sup_{w\in\mathbb C}\mathbb P_{\mathrm{fresh}}
       \left\{\left|\sum_{j\in S}h_j\xi_j-w\right|\le t\right\},
\]
where the test variables are independent copies of \(\xi\).
Except on an event of probability \(Ce^{-cN}+N^{-cN}\), on \(\max(\|A\|,\|B\|)\le K\), every unit \(h\) with \(\|(AB+2BA-zI)h\|\le b/\sqrt N\) satisfies
\[
 \rho_\xi(h_S,a/N)<N^{-3/2+\eta}
 \qquad \text{for both original colors and every } |S|\ge\theta N .
 \tag{Scalar-reservoir}
\]
The coefficients and the reservoir may be selected from the original matrices because the displayed quantity is a deterministic function of those selected coefficients and the test law.

To prove the implication, suppose a fixed coefficient array on \(S\), with \(n=|S|\ge\theta N\), has concentration at least \(N^{-3/2+\eta}\).
If \(\|h_S\|=0\), all \(n\) coordinates already have the single value zero.
Otherwise identify \(\mathbb C\) with \(\mathbb R^2\), divide its coefficient array by \(t_S=\|h_S\|\), and set the normalized ball radius to \(2a/(Nt_S)\).
The factor two also makes the implication valid for the source's open-ball convention.
This array has squared norm sum one and its concentration is at least \(N^{-3/2+\eta}\ge n^{-2}\) for sufficiently large \(N\) at fixed \(\theta\).
Each fixed variance-one law satisfies Condition 1 of Hoi H. Nguyen, *A continuous variant of the inverse Littlewood–Offord problem for quadratic forms*, arXiv:1105.5733v1, printed/PDF page 2.
Indeed \(\mathbb P\{|\xi-\xi'|>0\}>0\) for independent copies, and some bounded interval bounded away from zero captures a fixed positive amount of this mass.
Apply [Theorem 1.3, printed/PDF pages 2–3](../audits/literature/Ngu12a/Yin_U001.md#real-scalar-geometric-inverse) with dimension two, source parameters \(B=2,\epsilon=1/2\), and \(n'=\lfloor n/2\rfloor\).
For the earlier Nguyen–Vu corollary underlying this theorem, the authors identify a gap in its original deduction and repair its proof while retaining the small-cardinality statement in their [erratum, Corollary 1.2 and §2](https://people.math.osu.edu/nguyen.1261/cikk/ILO-erratum.pdf).
The allowed range \(n^\epsilon\le n'\le n\) holds eventually.
After multiplying its proper symmetric progression by \(t_S\), at least \(n-n'\) of the original coordinates are within \(2a/N\) of a set of cardinality at most
\[
 \max(1,C N^{3/2-\eta}/\sqrt{n'})\le C_\theta N^{1-\eta}.
\]
For large \(N\) this is at most \(\lfloor N^{1-\eta/2}\rfloor\).
Consequently at least \(\theta N/2\) coordinates admit an alphabet of that size with Euclidean error at most \(2a/\sqrt N\).
The single simultaneous partial-alphabet exclusion with \(\gamma=\theta/2,\alpha=1-\eta/2\) therefore proves (Scalar-reservoir), covering every eligible \(S\) and both laws at once.

For \(q=Ah,\ g=Bh\), consider the [three-complex-coordinate row profile](../claims/Yin_C_F0194_v31.md#original-root-triad) on the same reservoir,
\[
 \sum_{j\in S}\bigl(h_j\xi_{A,j},\ h_j\xi_{B,j},\
                         g_j\xi_{A,j}+2q_j\xi_{B,j}\bigr).
\]
In the virtual test with these fixed coefficients, the first two complex components are independent because they use separate fresh color samples.
Any event that the full vector lies in a prescribed Euclidean ball of radius \(a/N\) forces both components into the respective coordinate balls of the same radius.
Its concentration is thus bounded above by \(\rho_{\xi_A}(h_S,a/N)\rho_{\xi_B}(h_S,a/N)\).
By using (Scalar-reservoir) with \(\eta/2\), the six-real-dimensional concentration is less than \(N^{-3+\eta}\) for every such \(S\) on the same kind of summably guarded event.
Applying C194v31's row product to a prescribed triple uses the original row exposure under its hypotheses.
The estimate here permits an adaptive coefficient array only as an input to an independent virtual concentration function.
It does not justify conditioning the original matrices on their own near-mode or multiplying these bounds for rows of that adaptive triple.

<a id="fourier-profile"></a>
## A Fourier estimate using the full partial-alphabet exclusion

At the same fixed \(a,b,\theta,K,z\), any fixed \(0<\eta<1\) admits the stronger bounds
\[
 \rho_\xi(h_S,a/N)<N^{-2+\eta},\qquad
 \rho_{\rm triad}(h,g,q;S,a/N)<N^{-4+\eta}.
 \tag{Planar-profile}
\]
These hold for both original scalar laws, all \(|S|\ge\theta N\) and every actual guarded unit near-mode of residual at most \(b/\sqrt N\), outside one event of probability \(Ce^{-cN}+N^{-cN}\).
The joint quantity uses independent fresh colors as above.
The proof below uses only the partial-alphabet exclusion and elementary Fourier inversion.

Choose \(0<\epsilon<\min(1/4,\eta/16)\), write \(\Delta=N^{-\epsilon}\), and identify complex coefficients with planar points.
Use the partial-alphabet bound with \(\gamma=\theta/4,\alpha=1-\epsilon/2\) and squared-sum approximation norm \(2/\sqrt N\).
On its guarded good event, no collection of \(\gamma N\) coordinates of an actual near-mode can be covered by at most \(N^\alpha\) fixed-mesh squares of side \(1/N\).
Indeed the centers of the squares would give an alphabet with total Euclidean error at most \(1/\sqrt N\).
Fix any \(S\) of size at least \(\theta N\) and let \(S_0=\{j\in S:\ |h_j|\le L/\sqrt N\}\), choosing \(L\) so large that \(|S_0|\ge3\theta N/4\) by unit norm.
Dropping the other independent coordinates can only increase the concentration, by conditioning on the omitted summands.

Let \(\xi'\) be an independent copy of \(\xi\).
There are fixed \(0<l<H<\infty\) with \(\mathbb P\{l\le|\xi-\xi'|\le H\}=p>0\).
For the two laws these constants can be chosen separately, then take a common smaller cutoff \(c_0>0\) with \(c_0 H L<1/4\).
With Fourier convention \(e^{2\pi i t\cdot x}\), write \(\phi(t)=\mathbb E\exp(2\pi i t\cdot\sum_{j\in S_0}h_j\xi_j)\).
The identities \(1-|\mathbb E e^{2\pi i s\xi}|^2=\mathbb E[1-\cos(2\pi s(\xi-\xi'))]\) and \(1-\cos(2\pi u)\ge c\,\operatorname{dist}(u,\mathbb Z)^2\) imply
\[
 |\phi(t)|\le\exp\!\left\{-c\,\mathbb E_v
       \sum_{j\in S_0}\operatorname{dist}(v\, t\cdot h_j,\mathbb Z)^2\right\},
 \qquad v=|\xi-\xi'|.
\]
This uses independence across \(j\) for the product of scalar characteristic functions and linearity of expectation to use a common symmetrizing variable \(v\).

For every planar unit direction \(e\), the strip \(|e\cdot x|\le N^{-1/2}\Delta\) intersected with \(|x|\le L/\sqrt N\) meets \(O_L((1+\sqrt N)(1+\sqrt N\Delta))=O_L(N^{1-\epsilon})\) squares of the fixed mesh.
For instance, enlarge the two side lengths of an enclosing rotated rectangle by \(2\sqrt2/N\) and divide the enlarged area by \(N^{-2}\).
Thus fewer than \(\theta N/4\) coordinates of \(S_0\) lie in that strip, uniformly in \(e\).
It follows that \(\sum_{j\in S_0}(e\cdot h_j)^2\ge(\theta/2)\Delta^2\).
For \(|t|\le c_0\sqrt N,\ v\in[l,H]\), the distances in the Fourier bound equal \(|v\,t\cdot h_j|\), since \(v|t||h_j|<1/4\).
Integration over such \(v\) yields \(|\phi(t)|\le\exp(-c\Delta^2|t|^2)\).

Now assume \(c_0\sqrt N\le T=|t|\le N^{1-\epsilon}\) and fix \(l\le v\le H\).
Inside \(|x|\le L/\sqrt N\), the resonant set \(\operatorname{dist}(v\,t\cdot x,\mathbb Z)\le\Delta\) is covered by \(O_{H,L}(1+T/\sqrt N)\) strips, each with length at most \(2L/\sqrt N\) and width \(2\Delta/(vT)\).
The same enlarged-rectangle count bounds the total number of fixed mesh squares by
\[
 C(1+T/\sqrt N)(1+\sqrt N)(1+N\Delta/T)
 \ \le\ C' N^{1-\epsilon},
\]
where \(T\ge c_0\sqrt N,\ T\le N^{1-\epsilon}\) and \(\epsilon<1/2\).
For large \(N\) this is below \(N^{1-\epsilon/2}\), uniformly in angle, \(T\), and \(v\in[l,H]\).
The no-alphabet event therefore places at least \(\theta N/2\) elements of \(S_0\) outside that resonant set.
The characteristic-function inequality integrated over \(v\in[l,H]\) gives \(|\phi(t)|\le\exp(-cN\Delta^2)\) over the whole intermediate range.

For completeness let \(k(u)=(\sin(\pi u)/(\pi u))^2\), with \(k(0)=1\), and \(K_2(x)=k(x_1)k(x_2)\).
The inverse transform of the triangular function \((1-|t|)_+\) is \(k\), by direct integration.
Thus \(K_2(x)=\int_{[-1,1]^2} e^{2\pi i t\cdot x}\prod_{i=1}^2(1-|t_i|)\,dt\), and \(K_2\) is nonnegative and bounded below by an absolute positive constant on \(|x|\le1/4\).
Take \(T_0=N^{1-\epsilon}/2\), so that the square of frequency support \([-T_0,T_0]^2\) lies in \(\{|t|\le N^{1-\epsilon}\}\).
Since \(T_0 a/N\le1/4\) eventually, for every center \(w\) the preceding majorant and its Fourier integral give
\[
 \mathbb P\left\{\left|\sum_{j\in S_0}h_j\xi_j-w\right|\le a/N\right\}
   \le C T_0^{-2}\int_{[-T_0,T_0]^2}|\phi(t)|\,dt
   \le C N^{-2+4\epsilon}+C e^{-cN^{1-2\epsilon}} .
\]
Here the low-frequency Gaussian integral is \(O(\Delta^{-2})\), while the area of the intermediate frequency domain is \(O(T_0^2)\).
The fixed constants are absorbed into \(N^{-2+\eta/2}\) for all large \(N\).
Applying this to both original raw laws and using the independent first two virtual components gives (Planar-profile) with the stated joint exponent.

The scalar exponent two is the natural upper limit, up to subpowers, for a uniform nonvacuous estimate at this radius.
For any fixed unit \(h\), any \(S\), and any fixed centered variance-one raw law, the fresh sum has second absolute moment at most one.
A fixed planar box carries at least half its mass and can be covered by \(O_a(N^2)\) Euclidean balls of radius \(a/N\), so its concentration is always at least \(c_a N^{-2}\).
The estimate leaves the residual coordinate of the six-real-dimensional row available for a further gain, conditional on its first two images.

<a id="family-and-boundary"></a>
## A dense set of concentrated original-entry profiles

There is a metric-entropy limitation to using high concentration itself to obtain the necessary saving below unit entropy coefficient.
Let \(A,B\) be independent real symmetric Wigner matrices with Rademacher raw strict upper and diagonal laws and entry normalization \(N^{-1/2}\), and fix the guard \(\max(\|A\|,\|B\|)\le K\).
Round the real and imaginary coordinates of any unit \(h_*\) to \(N^{-1}\mathbb Z\), and divide the resulting \(u\) by \(d=\|u\|=1+O(N^{-1/2})\).
The unit vectors \(h=u/d\) so obtained are \(C/\sqrt N\)-dense in the complex sphere.
For every realization on the norm guard, their actual images \(g=Bh,q=Ah\) have real and imaginary coordinates in \((d N^{3/2})^{-1}\mathbb Z\), while those of \(h\) are in \((dN)^{-1}\mathbb Z\).
For each of the original [three-complex-coordinate row sums](../claims/Yin_C_F0194_v31.md#original-root-triad) with these fixed coefficients, real and imaginary parts in the first two coordinates have lattice spacing \((dN)^{-1}\) and those in the last have spacing \((dN^{3/2})^{-1}\).
The centered row sum using fresh independent raw signs has second absolute moment at most \(2\|h\|^2+\|g\|^2+4\|q\|^2\le2+5K^2\), uniformly for every suffix or coordinate subset.
A fixed six-dimensional box therefore has at least half the probability and contains \(O_K(N^7)\) attainable lattice points.
Each coefficient profile has a joint atom at least \(c_K N^{-7}\), including when the original inputs yielding the coefficients were already realized.
This is solely a statement about the concentration function of a prescribed profile tested against fresh row signs.
It supplies no lower bound for the probability of a specified residual target for the input realization that selected \(q,g\).
At radius \(a_0/\sqrt N\) with \(a_0\) fixed, any cover of these roots induces a \((C+a_0)/\sqrt N\) cover of the unit complex sphere.
Normalized spherical-cap volume in real dimension \(2N\) bounds its cardinality below by \((c\sqrt N)^{2N-1}=N^{(1-o(1))N}\).
Consequently the image equations and the condition that every joint row concentration is at least \(N^{-C_1}\), with \(C_1>7\), alone give no fixed saving in this coarse entropy coefficient even for bounded Wigner entries.
The complement residual equations constrain the actual target, and a proof using these additional correlations, or a count reaching a finer scale, remains open.
Neither a summable estimate for the unrestricted planar integral of \(D_N\) nor almost-sure Brown convergence for arbitrary cross-size coupling follows from this example or the conditional exterior bound.

<a id="conditional-subspace"></a>
## The subspace determined by the exterior equations

Use the real fourth-moment model above and fix \(z\ne0\).
Write \(D=AB+2BA-zI_N\).
For a fixed \(k\)-element coordinate set \(I\) put \(J=I^c\).
Let \(\Pi\) be the [exterior projection](../claims/Yin_C_F0194_v33.md#statement) onto the vectors supported on \(J\) and orthogonal to the range of \(B_{JI}\) there.
The entire map \(L=\Pi D\) is measurable given \(B\) and \(A\) outside \(I\times I\).
Indeed the part of \(ABh\) using \(A_{II}\) is supported on \(I\), and the \(J\)-component of the corresponding part of \(BAh\) lies in \(\operatorname{ran}B_{JI}\), for every \(h\).
Define the complex subspace \(E_t=\operatorname{ran}\mathbf1_{[0,t]}(|L|)\), \(t>0\), and write \(n_t(D)\) for the number of singular values of \(D\) in \([0,t]\), with multiplicities.
Then
\[
 \dim_{\mathbb C} E_t\le k+\operatorname{rank} B_{JI}+n_t(D)\le 2k+n_t(D).
 \tag{Exterior-subspace-dimension}
\]
The rank of \(D-L\) is at most \(\operatorname{codim}\operatorname{ran}\Pi=k+\operatorname{rank}B_{JI}\).
Intersect \(E_t\) with \(\ker(D-L)\).
On this intersection \(\|Dh\|=\|Lh\|\le t\|h\|\), so its dimension is at most \(n_t(D)\) by min-max.
The same argument with two maps in either order bounds the difference of their singular counts by the rank of their difference.

The [polynomial count](../claims/Yin_C_F0195_v1.md#polynomial-transfer), applied at the squared threshold \(t^2\), yields \(\mathbb E n_t(D)\le C_z N t^{\beta_z}\) for \(N^{-\gamma_z}\le t\le1\), with \(\beta_z,\gamma_z>0\).
Partition the independent coordinates of each color into \(N\) blocks by their upper-triangular row index.
An alteration of one block changes that input by rank at most two and \(D\) by rank at most four.
The singular-count difference is therefore at most four.
The [bounded-differences argument](../claims/Yin_C_F0186_v4.md#row-concentration) for these \(2N\) independent blocks gives
\[
 \Pr\{n_t(D)>\mathbb E n_t(D)+s\}\le \exp[-s^2/(16N)].
\]
Fix \(0<d<\gamma_z\) with \(d\beta_z<1/2\), put \(t_N=N^{-d}\), and take \(s=N^{1-d\beta_z}\).
Outside a single event of probability at most \(\exp[-N^{1-2d\beta_z}/16]\), (Exterior-subspace-dimension) bounds \(\dim_{\mathbb C}E_{t_N}\) by \(2k+(1+C_z)N^{1-d\beta_z}\) simultaneously for every \(I\).
For fixed \(\eta>0\) one can instead choose a sufficiently small constant \(t>0\) to obtain \(\dim_{\mathbb C}E_t\le2k+\eta N\) except with probability at most \(\exp[-c_\eta N]\).
For any prescribed \(I\), its subspace-dimension event itself is exterior-measurable.
Its exceptional probability can thus be charged once, before testing \(A_{II}\), without conditioning the interior entries on \(n_t(D)\).

If \(\|Dh\|\le\varepsilon\) for a unit \(h\), then \(\operatorname{dist}(h,E_t)\le\varepsilon/t\) by the singular decomposition of \(L\).
For \(\varepsilon<t/2\), normalizing its projection on \(E_t\) increases this distance bound by at most a factor two.
The unit sphere in \(E_t\) has an exterior-measurable \(r\)-net with at most \((1+2/r)^{2\dim_{\mathbb C}E_t}\) elements for \(0<r<1\).
One may choose a measurable orthonormal basis by applying Gram-Schmidt in coordinate order to the projected standard basis and transferring a fixed Euclidean net in that dimension.
On a fixed norm guard, the residual at a chosen net point is at most \(\varepsilon+(3K^2+|z|)(2\varepsilon/t+r)\).
The ratio \(\varepsilon/t\) is required when the spectral cutoff decreases with \(N\).

For full-column-rank \(B_{JI}\), the codomain of \(L\) has complex dimension \(N-2k\), so \(\dim_{\mathbb C}\ker L\ge2k\).
Consequently a direct Euclidean cover of the compatible kernel sphere has real-dimensional leading power at least \(4k-1\) in \(1/r\), by spherical-cap volume.
When \(k\) is proportional to \(N\), a homogeneous four-real-dimensional small-ball factor of order \(r^4\) on each of \(k\) ideal interior tests would balance this leading entropy.
This compares exponents only.
The actual [one-color interior equations](../claims/Yin_C_F0194_v31.md#one-color-root-reconstruction) test the two complex coefficients \((h_j,(Bh)_j)\) with the same fresh real \(A\) entry.
The independent-color product in (Planar-profile) does not estimate this one-color pair.
For an interior reconstructed-error vector of norm at most \(C\varepsilon\), scaling its coordinates by \(\sqrt N\) gives squared errors with sum at most \(C^2N\varepsilon^2\).
Thus all but a fixed fraction of \(k\) tested rows have raw error \(O(\sqrt{N/k}\,\varepsilon)\).
For a macroscopic \(k\), a root approximation at \(N^{-1/2}\) only supplies this typical raw scale \(O(N^{-1/2})\), while (Planar-profile) uses the finer radius \(a/N\).

One possible further reduction uses the exterior-measurable map \(Xh=(h_I,(Bh)_I)\) into \(\mathbb C^{2k}\).
To parametrize the remaining roots by those very coefficients at precision \(r\), one needs an estimate on the small singular subspace of \(X|_{E_t}\), including the scale of the inverse on its orthogonal complement and the covering cost in the discarded directions.
The rank bound above only gives the dimension of \(E_t\).
The [integrated position estimate](../claims/Yin_C_F0196_v4.md#statement) controls the small singular directions of \(X|_{E_t}\) outside an exceptional parameter set of summably negligible loss.
The [two-target estimate](../claims/Yin_C_F0194_v34.md#statement) controls actual row hits for eligible exterior-measurable candidates.
The unrestricted low-product planar loss still requires control of interior-dependent roots.

<a id="repeated-interior"></a>
## The conditional interior determinant in the two observation coordinates

Use the [square exterior map](../claims/Yin_C_F0196_v4.md#argument) for a prescribed \(I\) of size \(k\), and let \(P:\mathbb C^N\to\mathbb C^k\) be coordinate restriction.
Assume \(V=B_{JI}\) has full column rank and \(z\notin\sigma(C_H)\), where \(H=\ker X\), \(\Pi=\Pi_H\), \(C_H=\Pi(AB+2BA)|_H\), and \(Xh=(Ph,PBh)\).
Write \(D^e=A^eB+2BA^e-zI\), where the \(I\times I\) entries of \(A^e\) vanish and all other entries agree with \(A\).
For the actual real symmetric interior \(U=A_{II}\), put \(\mathcal U=\operatorname{diag}(U,U)\) and \(Z=(2BP^*,P^*)\).
Then \(D=M-zI=D^e+Z\mathcal U X\).
The map \(Z\) has image \(H^\perp\), since the two column spaces are the two rows of \(X\) under adjoint and the first has simply been scaled by two.
It is an isomorphism from \(\mathbb C^{2k}\) to \(H^\perp\).
All the following targets are determined before sampling the interior.
Define
\[
 T h=(\Pi D h,Xh),\qquad
 W(z)=-Z^{-1}(1-\Pi)D^e T^{-1}(0,\,\cdot\,).
\]
The inverse \(Z^{-1}\) here acts only on \(H^\perp\).
In orthonormal bases adapted to \(H\oplus H^\perp\), \(D T^{-1}\) has first output component equal to its first input component and lower-right block \(Z(\mathcal U-W(z))\).
Consequently
\[
 |\det D(z)|
 =2^k\,\det(V^*V)\,|\det(C_H-zI_H)|\,
       |\det(\mathcal U-W(z))|.
 \tag{Repeated-interior-determinant}
\]
Indeed the [exterior determinant identity](../claims/Yin_C_F0196_v4.md#argument) gives \(|\det T|=|\det(C_H-zI_H)|\det(V^*V)^{1/2}\).
The Gram matrix \(Z^*Z\) has blocks \(4P B^2P^*,2B_{II},2B_{II},I_k\).
Its Schur complement over \(I_k\) is \(4V^*V\).
Multiplying the two absolute Jacobians and the lower-right determinant proves the formula.
The stated identity applies off the finite pole set.

One arithmetic constraint on an exact interior target follows directly.
If \(a=Xh=(y,w)\) and \(W(z)a=(t_1,t_2)\), the exact equation \(\mathcal U a=W(z)a\) requires both \(Uy=t_1\) and \(Uw=t_2\).
Writing \(C\) for the real \(k\)-by-4 matrix of real and imaginary input columns and \(Y\) for the corresponding real target columns, symmetry forces \(C^TY=Y^TC\).
If \(\|\mathcal U a-W(z)a\|\le \varepsilon\), the Frobenius norm of the skew part \(C^TY-Y^TC\) is at most \(2\|C\|\,\varepsilon\), by inserting \(UC\) and using \(\|Y-UC\|_{\rm HS}\le\varepsilon\).
These compatibility relations are polynomial conditions on the exterior target.
Using the determinant identity to control the remaining low-concentration profiles would require bounds on the negative logarithm of \(\det(\mathcal U-W(z))\) at the actual meromorphic \(W(z)\), or small-ball estimates on its dependent candidate directions.
The two copies of \(U\) have identical entries in every realization.
