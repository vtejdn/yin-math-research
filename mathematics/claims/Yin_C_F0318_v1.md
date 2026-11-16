---
author: Yin
---

# Directional Cauchy energy and the transverse slice of a normal coordinate

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(\mu\) be the compact spectral law of a normal coordinate with actual scalar conjugate variable \(\xi_\mu\) on its represented starred polynomial core.
Identify complex numbers with real two-dimensional column vectors, writing \(v_\mu=(\operatorname{Re}\xi_\mu,\operatorname{Im}\xi_\mu)^T\).
Let \(c^2(\mu)=\int\kappa(z,w,v)^2\,d\mu^3\), with reciprocal circumradius \(\kappa=0\) on collinear or repeated triples.
Write \(\theta(z)=\lim_{r\downarrow0}\mu(B(z,r))/(2r)\).
On the positive-density rectifiable part let \(\mathsf t(z)\) denote either choice of unit tangent vector.
Then
\[
 \int v_\mu v_\mu^T\,d\mu
     =\frac{c^2(\mu)}3 I_2+
         \frac{4\pi^2}3\int_{\theta>0}\theta(z)^2
                        \mathsf t(z)\mathsf t(z)^T\,d\mu(z).             \tag{1}
\]
The tangent sign is immaterial.
In particular, for every angle \(\phi\),
\[
          c^2(\mu)\le3\|\operatorname{Im}(e^{-i\phi}\xi_\mu)\|_2^2.     \tag{2}
\]
The constant three is sharp even for a bounded planar area density.
For a law supported on a straight line only the tangential term in (1) survives, and every zero-density part contributes zero to that term.

For an actual coordinate \(Z\) of a normal tuple with vacuum \(\xi\) and marginal law \(\mu\), let \(\delta^\#p=(\delta(p^*))^\dagger\) be the reversed derivation.
Here \(\dagger\) flips and takes adjoints on the two legs.
Write \(Y=\operatorname{Im} Z\), \(\eta=\|Y\|_2\), and \(\epsilon=\|\xi-Z\|_2\).
Then \(c^2(\mu)\le3(\eta+\epsilon)^2\).
Set \(\delta_y=(\delta-\delta^\#)/(2i)\), \(T_y=(\mathrm{id}\otimes\tau)\delta_y\), and \(\zeta_y=i(\xi-\xi^*)/2\).
The transverse component and its normalized generator satisfy
\[
 \|\zeta_y\|_2\le\eta+\epsilon,\qquad
 \|\delta_y Z\|_2^2=\eta^2+\operatorname{Re}\langle\xi-Z,iY\rangle
                         \le\eta(\eta+\epsilon).                         \tag{3}
\]

On an exchange-symmetric pair with full actual starred conjugate variables, use the matched curvature forms \(F^j(u)\), the nonnegative inner term \(H(u)\), and the difference \(D(u)\) of [the signed comparison](Yin_C_F0314_v1.md#statement).
For every one of its tests \(u=h\pm i\sqrt{1-h^2}\) on the original strict polynomial core,
\[
 \begin{split}
 F^j(u)&=4\big(\|\zeta_{jy}\|_2^2-\|T_{jy}u-u\zeta_{jy}\|_2^2\big),\\
 -D(u)&=4\sum_{j=0,1}
       \big(\|T_{jy}u-u\zeta_{jy}\|_2^2-\|\zeta_{jy}\|_2^2\big)+H(u),
 \qquad 0\le H(u)\le 6(\eta+\epsilon)^2.                               \tag{4}
 \end{split}
\]
Exchange gives common \(\eta,\epsilon\).
Thus only the two transverse slice values in (4) require control on this unitary test class once \(\eta,\epsilon\) are bounded.
The uniform lower bound for \(D(u)\) in the general normal comparison remains open.

## Argument

### Soft symmetrization in a direction

Use the [actual scalar vacuum and hard Cauchy transforms](Yin_C_F0267_v1.md#hard-cauchy-transforms-and-the-original-core).
In particular the measure is diffuse, has finite curvature \(c^2(\mu)\), and its maximal linear density belongs to \(L^2(\mu)\).
For \(\lambda=\mu\) or any Borel restriction of \(\mu\), the same finiteness conditions hold by domination.
Let \(C\lambda\) denote the real vector field given by the principal value of \(\int (z-w)|z-w|^{-2}\,d\lambda(w)\).
This is the conjugated complex Cauchy kernel, with \(v_\mu=2C\mu\).
The [exact scalar norm and graph reduction](../audits/literature/TV06/Yin_U002.md#tv06-u002) apply to each \(\lambda\).
The hard truncations converge strongly in \(L^2(\lambda)\) to \(C\lambda\).

For \(a>0\) use the bounded soft kernel \(K_a(v)=v/(|v|^2+a^2)\), with vector field \(C_a\lambda(z)=\int K_a(z-w)d\lambda(w)\).
For \(d>0\) the multiplier \(d^2/(d^2+a^2)\) equals the mass of \([0,d)\) for the probability density \(2r a^2/(r^2+a^2)^2\) on \(r>0\).
Consequently the soft field is the average against this density of the hard fields with radii \(r\), first by absolute integration at fixed \(a\).
Their Hilbert norms are bounded uniformly in \(r\) by strong convergence at zero and the pointwise kernel bound away from zero.
As \(a\downarrow0\) this probability concentrates at zero, giving \(C_a\lambda\to C\lambda\) strongly.

For a real vector \(e\) and a triple of distinct sites \(z_i\), let \(v_{ij}=z_i-z_j\), let \(L=|\det(v_{12},v_{13})|\), and let \(P_a=\prod_{i<j}(|v_{ij}|^2+a^2)\).
The sum over the three vertices has the identity
\[
 \sum_{i=1}^3 (e^T K_a(v_{ij}))(e^T K_a(v_{ik}))
   =\frac{|e|^2L^2+(a^2/2)\sum_{i<j}(e^T v_{ij})^2}{P_a},
                 \qquad \{j,k\}=\{1,2,3\}\setminus\{i\}.                \tag{5}
\]
To verify the constant term write \(A=v_{12},B=v_{13},x=e^T A,y=e^T B\).
Multiplication by \(P_a\) gives the constant term \(xy|B-A|^2+x(x-y)|B|^2+y(y-x)|A|^2=|xB-yA|^2\).
In the plane this is \(|e|^2\det(A,B)^2\), by expanding in real coordinates.
The coefficient of \(a^2\) is \(xy+x(x-y)+y(y-x)=(x^2+y^2+(x-y)^2)/2\).

Integrating the left side gives \(3\int(e^T C_a\lambda)^2d\lambda\) by permutation symmetry.
The repeated-site diagonals are null by diffuseness.
On distinct triples \(L^2/P_0=\kappa^2/4\), including the collinear case, and \(L^2/P_a\le L^2/P_0\).
It follows from strong convergence and dominated convergence in (5) that the positive matrices
\[
     \frac{2a^2}{3}\int
           \frac{\sum_{i<j} v_{ij}v_{ij}^T}{P_a}\,d\lambda^3
         \longrightarrow R(\lambda)
           =4\int (C\lambda)(C\lambda)^T d\lambda-\tfrac13 c^2(\lambda)I_2 .
                                                                          \tag{6}
\]
Convergence of matrix entries follows by polarization in two dimensions.
The scalar Cauchy norm identity of the cited source now gives
\[
               \operatorname{tr}R(\lambda)
                      =\frac{4\pi^2}3\int\theta_\lambda^2\,d\lambda .
                                                                          \tag{7}
\]

### Localizing the positive matrix to tangents

For a countable Borel partition \(E=\bigsqcup_n E_n\), positivity of the integrand in (6) gives \(R(\mu|_E)\succeq\sum_{n\le m}R(\mu|_{E_n})\) for each finite \(m\), by keeping just the triples contained in one piece.
Here positive matrices are ordered by their quadratic forms.
At \(\mu\)-almost every point of a Borel set \(F\), differentiation of its indicator against \(\mu\) gives \(\theta_{\mu|_F}=\theta_\mu\).
Consequently (7) gives equality of the trace of \(R(\mu|_E)\) with the sum of all the traces.
The positive remainder therefore vanishes in the countable limit.
Thus \(E\mapsto R(\mu|_E)\) is a finite positive matrix-valued measure of trace measure \((4\pi^2/3)\theta^2\mu\).
Its density relative to this trace measure is almost everywhere a positive matrix \(M(z)\) of trace one.
This follows by applying the Radon--Nikodym theorem to the entries and testing positivity on rational directions.

The cited rectifiability statement covers the positive-density part up to null sets by countably many Lipschitz graphs, on which the density is with respect to arclength.
For clarity, absolute continuity there also follows by covering arclength-null sets with small balls on the pieces where the finite maximal linear density is bounded.
Assign overlapping graphs disjointly to their first occurrence.
At almost every point of each assigned graph its Lipschitz parametrization by the horizontal parameter in its graph coordinates is differentiable, with nonzero tangent vector.
For any fixed angular tolerance \(\rho>0\), these points can be partitioned into countably many measurable pieces so that all chords in any one piece make angle at most \(\rho\) with one line of unit direction \(t_0\), and the tangents there also make angle at most \(\rho\) with that line.
Indeed group points by a small angular neighborhood of the derivative direction and by a common lower bound for the radius on which their differentiability error divided by the parameter increment is small.
Subdivide into parameter intervals shorter than that lower bound.
The derivative has norm at least one in graph coordinates, giving the claimed chord control by choosing the angular neighborhoods and errors sufficiently small.

If \(e_0\) is perpendicular to \(t_0\), every chord in the piece satisfies \(|e_0^T v_{ij}|^2\le\sin^2(\rho)|v_{ij}|^2\).
The same bound compares the \(e_0\)-component of (6) with its trace for any Borel restriction inside the piece.
Passing to the measure density gives \(e_0^TM(z)e_0\le\sin^2(\rho)\) there almost everywhere for its trace measure.
Use a countable sequence \(\rho\to0\).
The normals for the corresponding pieces approach the tangent-normal line at almost every point, and \(\|M(z)\|\le1\).
Thus the tangent-normal direction is in the kernel of \(M(z)\).
A positive matrix of trace one with this property equals \(\mathsf t(z)\mathsf t(z)^T\).
On the zero-density part (7) gives zero matrix measure.
Taking \(E\) to be the whole support in (6) proves (1).

Choose \(e=(-\sin\phi,\cos\phi)^T\) to obtain (2).
Equivalently rotating \(Z\) to \(e^{-i\phi}Z\) multiplies its normalized derivation by \(e^{i\phi}\) and its vacuum by \(e^{-i\phi}\), since the Hilbert inner product is linear in its second variable.
A scalar straight-line law has zero triple curvature and constant tangent line at positive-density points.
Normalized area on a disk has \(\theta=0\), positive triple curvature and an actual vacuum, as in the [disk calculation](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density).
Thus (2) is an equality there for every axis with positive right side.

### The transverse term on mixed tests

Projection of the joint vacuum onto \(W^*(Z)\) gives \(\xi_\mu\) by the marginal double-trace identity, and conditional expectation commutes with taking imaginary parts.
Hence \(\|\operatorname{Im}\xi_\mu\|_2\le\|\operatorname{Im}\xi\|_2\le\eta+\epsilon\).
This proves the stated directional curvature bound for the tuple and the bound on \(\|\zeta_y\|_2\).
The [forced phase and reversal](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) give \(\delta Z^*=k(z,w)=(\bar z-\bar w)/(z-w)\) and \(\delta^\#Z=\bar k\).
Since \(|k|=1\) almost everywhere and the vacuum tested on \(Z-Z^*\) gives \(1-\int k\,d\mu^2=\langle\xi,2iY\rangle\), one has
\[
     \|\delta_yZ\|_2^2=\tfrac12(1-\operatorname{Re}\int k\,d\mu^2)
                        =\operatorname{Re}\langle\xi,iY\rangle .
\]
Traciality gives \(\operatorname{Re}\langle Z,iY\rangle=\|Y\|_2^2\), proving (3).

For one coordinate let \(\delta_x=(\delta+\delta^\#)/2\) and put \(A_a=(\delta_a\otimes1)\delta_a-(1\otimes\delta_a)\delta_a\) for \(a=x,y\) on the original core using the actual closed tensor-leg graphs.
Expanding the two squares shows \(A_x-A_y\) equals one half the sum of the individual associators of \(\delta,\delta^\#\).
These two associators are zero on the full core by [actual coassociativity in both orientations](Yin_C_F0076_v1.md#statement).
Thus \(A_y=(A_x+A_y)/2\).
The componentwise calculation preceding (19) of the [actual mixed-energy identity](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) gives for its \(y\) component on the analytic unitaries
\[
 \|T_yu\|_2^2=2\operatorname{Re}\langle T_yu,u\zeta_y\rangle
        -\operatorname{Re}\langle(\mathrm{id}\otimes\tau\otimes\tau)A_y u,u\rangle .
\]
Here the last expression denotes the analytic evaluation of the contracted defect, which is an outer derivation before its final slice.
To see the componentwise identity directly on core \(p\), the real product rule gives
\(T_y(p^*p)=p^*T_yp+((\mathrm{id}\otimes\tau)((\delta_y p^*)\cdot p))\).
Pairing with \(\zeta_y\) and using flip reality expresses the second summand's pairing as the pairing of \(p\) with \(\Theta(\delta_y p)\zeta_y\), in real part, where \(\Theta(a\otimes b)h=a\,\tau(bh)\).
Substituting \(T_y^2p=(\mathrm{id}\otimes\tau\otimes\tau)A_yp+\Theta(\delta_yp)\zeta_y\) and \(T_y^*q=q\zeta_y-T_yq\) yields the preceding two cross terms with the additional core term \(-\operatorname{Re}\langle\zeta_y,T_y(p^*p)\rangle\).
It vanishes in the analytic-unitary limit by the norm and first-derivative product convergence to \(u^*u=1\).
The same actual graph calculation therefore applies to this one component.
Equation (20) there and the [signed curvature convention](Yin_C_F0314_v1.md#quantitative-control-of-the-full-cores) identify the real pairing for the sum of the two associators with \(F^j(u)/2\).
The equal split just proved gives \(F^j(u)/4\) for \(A_y\).
Completing the square proves the first equality in (4), using \(\|u\zeta_y\|_2=\|\zeta_y\|_2\).
Finally \(D+H=F^0+F^1\), and \(0\le H\le 2c^2(\mu)\) by the [inner-term formula](Yin_C_F0314_v1.md#adding-the-two-partial-liberations).
Equations (1) and (2) give the last estimate in (4).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:18 |
| status | open |
| reason | Fix the directional matrix energy, sharp curvature bound and transverse mixed-unitary formula for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact tangent-direction matrix term, sharp rotated scalar curvature estimate, joint generator defect, and the signed transverse identity. |
| argument | [Argument](#argument) | Positive matrix remainder, restriction additivity from the scalar trace, tangent localization and the individual real-component graph identity. |
| dependency | [Hard Cauchy field](Yin_C_F0267_v1.md#hard-cauchy-transforms-and-the-original-core) | Actual scalar vacuum equals twice the conjugated hard Cauchy limit and actual marginals have finite geometric energy. |
| dependency | [Exact scalar energy and graph reduction](../audits/literature/TV06/Yin_U002.md#tv06-u002) | Principal values, scalar squared norm coefficients, arclength density, strong hard limits and graph covering at positive density. |
| dependency | [Disk input](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Normalized planar area has an actual scalar vacuum and zero one-dimensional density. |
| dependency | [Phase and coassociativity](Yin_C_F0076_v1.md#statement) | Actual phases, reversed vacua and vanishing of both pure tensor-leg associators on the joint starred core. |
| dependency | [Mixed component energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual adjoint and mixed-iterate graph calculations before (19), analytic-unitary passage and the curvature contraction in (20). |
| dependency | [Signed difference](Yin_C_F0314_v1.md#statement) | The matched forms, scalar difference, nonnegative inner term and analytic-unitary test class. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:31 |
| status | proved |
| reason | Adopt the directional Cauchy energy, sharp curvature estimate and transverse mixed-energy identities after independent review of the geometric and operator arguments. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact tangent-direction matrix term, sharp rotated scalar curvature estimate, joint generator defect, and the signed transverse identity. |
| argument | [Argument](#argument) | Positive matrix remainder, restriction additivity from the scalar trace, tangent localization and the individual real-component graph identity. |
| dependency | [Hard Cauchy field](Yin_C_F0267_v1.md#hard-cauchy-transforms-and-the-original-core) | Actual scalar vacuum equals twice the conjugated hard Cauchy limit and actual marginals have finite geometric energy. |
| dependency | [Exact scalar energy and graph reduction](../audits/literature/TV06/Yin_U002.md#tv06-u002) | Principal values, scalar squared norm coefficients, arclength density, strong hard limits and graph covering at positive density. |
| dependency | [Disk input](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Normalized planar area has an actual scalar vacuum and zero one-dimensional density. |
| dependency | [Phase and coassociativity](Yin_C_F0076_v1.md#statement) | Actual phases, reversed vacua and vanishing of both pure tensor-leg associators on the joint starred core. |
| dependency | [Mixed component energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual adjoint and mixed-iterate graph calculations before (19), analytic-unitary passage and the curvature contraction in (20). |
| dependency | [Signed difference](Yin_C_F0314_v1.md#statement) | The matched forms, scalar difference, nonnegative inner term and analytic-unitary test class. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0327_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
