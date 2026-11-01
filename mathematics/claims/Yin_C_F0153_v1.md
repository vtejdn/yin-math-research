---
author: Yin
---
# Full canonical domains for finite Gaussian block changes of a normal coordinate

Human author: Yin.
The normal-branch agent developed the relative-degree-one correction, its positivity estimate, the arbitrary-abelian-base cut argument and the actual separated-block application.
Root proposed the Gaussian block diagnostic and requested the all-degree check.
These are development contributions, not independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let Z be bounded normal, N=W*(Z), with diffuse compact spectral law mu and faithful normal probability trace.
Assume that its scalar represented starred divided-difference derivation

\[
 \partial_Z f(z,v)=\frac{f(z)-f(v)}{z-v},
 \qquad f\in\mathbb C[Z,Z^*],
\]

has actual vacuum xi_N in L2(N).
Let S be standard semicircular free from N, and put M=W*(N,S).
Suppose sigma(Z) is the disjoint union of finitely many nonempty compact sets K_i with positive pairwise distances.
Write p_i=1_(K_i)(Z), choose strictly positive real numbers a_ij=a_ji, and set

\[
 T=\sum_{i,j}a_{ij}p_iSp_j,\qquad
 R=\sum_{i,j}a_{ij}^{-1}p_iSp_j,\qquad
 \mathcal A=\mathbb C\langle Z,Z^*,T\rangle.
\]

Then W*(Z,T)=M.
The normal pair (Z,T) has represented Hilbert-tensor derivations delta_Z,delta_T on A with prescribed coordinate values, both actual vacuum adjoints, and both original canonical full bounded-vector domains:

\[
 M\Omega\subseteq\operatorname{Dom}\overline{E_j}
                 \cap\operatorname{Dom}E_j^*,
 \quad E_j=(\mathrm{id}\otimes\tau)\delta_j,
 \quad\operatorname{Dom}E_j=\mathcal A\Omega,
 \quad j=Z,T.
\]

Here delta_Z Z=1 tensor 1, delta_Z T=0, delta_T Z=delta_T Z*=0 and delta_T T=1 tensor 1.
The normal starred value of delta_Z is its usual phase.
Negating the canonical closures gives generator-first duals on all M Omega.
In particular the pair satisfies A and S, and hence bare F.
These assertions concern the original target core and actual adjoints, not separately selected extensions.

The Z vacuum decomposes orthogonally as xi=xi_N+v_beta, with v_beta in relative S degree two.
Put

\[
 K_0=\sqrt{4/\pi}(5+2\sqrt{27}),\qquad K=\sqrt{K_0^2+8}.
\]

If F_Z=(id tensor tau)delta_Z# denotes the adjoint-reversed contraction, then

\[
 \|E_Zp\|_2,\|F_Zp\|_2\le K\|\xi\|_2\|p\|,
 \qquad \|E_Z^*p\|_2\le(1+K)\|\xi\|_2\|p\|.
\]

The T vacuum is R, and its contraction and adjoint bounds are respectively 2||R||2 and ||R||2.
The constants for Z do not depend on the number or masses of the blocks, their separation, or the values and inverses of a_ij; the hypotheses ensure that the displayed actual vacuum is finite.

Let g(z,v)=integral c(z,w,v)^2 dmu(w), where c is Menger curvature.
Define C_g on the target core as the actual contraction of the normal mixed defect, equivalently the partial liberation weighted by g at its generator values.
This definition does not require g itself to be a coarse Hilbert tensor.
For every analytic-core unitary u=b+i sqrt(1-b^2), with b=b* in A and ||b||<1,

\[
 \operatorname{Re}\langle u,C_gu\rangle
 \ge-(4K+2K^2)\|\xi\|_2^2.
\]

The proof includes a reusable relative-degree statement: if N is any abelian finite tracial algebra and S is free standard semicircular, the weighted reference derivative I_beta partial_S obeys (G3) for every beta with total relative S degree at most n.
Its proof explicitly constructs the relative Wick cut for that base; it does not apply the two-semicircular statement of C_F0145 outside its hypotheses without an argument.

A finite atomic version of the correction estimate is also proved below, with diagonal-zero divided differences.
Its vector xi_formal is not an ACSY conjugate variable for atomic Z.
Neither arbitrary measurable inverse coefficients nor countably many spectral blocks are included.
The result resolves the all-unitary estimate for this finite Gaussian construction; it does not prove A implies S for arbitrary correlated normal tuples.

## Reuse and source scope

The exact inputs are the finite block model of C_F0149, the relative-degree proof of C_F0145, the NS06 free Wick interface, the scalar actual-vacuum estimate and smooth approximation of C_F0055, the normalized free lift of C_F0045, the original-graph restoration of C_F0072, and only the exact mixed-energy identity from C_F0078 Section 6.
The comparison with C_F0141 is stated at the end.
No new external theorem, numerical scan or novelty assertion is used.
All new relative-base and target-core adaptations are proved here.

## Argument


The proof controls the complete canonical contraction, rather than only its degree-preserving part.
The coefficient positivity prevents cancellation between the two relative-degree-one components of the actual reference adjoint.
All generator cores and graph passages are specified below.

### Relative degree with an arbitrary abelian base

Let N be an abelian finite tracial algebra and let S be a standard semicircular free from N.
Its relative S-degree spaces satisfy
\[
 H_n\simeq L^2(N)^{\otimes_2(n+1)}\quad(n\ge0),
 \qquad H=\bigoplus_{n\ge0}H_n.
 \tag{G1}
\]
The map sends a_0 tensor ... tensor a_n to the relative Wick polynomial W(a_0,...,a_n), with highest term a_0 S a_1 ... S a_n.
The free semicircular pairing formula in [NS06-U003](../audits/literature/NS06/Yin_U004.md#ns06-u004) proves the inner product as the product of the n+1 marginal inner products, after subtracting all internal contractions; distinct degrees are orthogonal.
Equivalently the recurrence is given by left multiplication in N at a_0, left S creation W(1,a_0,...,a_n), and annihilation tau(a_0)W(a_1,...,a_n) for n>=1.
At n=0 only creation occurs.
This gives the same complete relative Wick construction used for projection paths in C_F0149.
Choosing a bounded orthonormal basis of L2(N), including 1, makes all finite basis Wick vectors bounded and gives their dense polynomial span.

The reference derivative partial_S kills N.
Differentiating that recurrence proves
\[
 \partial_SW(a_0,\ldots,a_n)
 =\sum_{j=1}^n W(a_0,\ldots,a_{j-1})
                    \otimes W(a_j,\ldots,a_n).
 \tag{G2}
\]
Thus cutting at the S with exactly k remaining S letters is an isometry from the sum of degrees at least k+1 onto H tensor_2 H_k.
On each degree this is simply reassociation of the tensor factors in (G1).
No scalar-semicircular hypothesis on N is needed for that cut.

The proof of [C_F0145 Sections 2--3](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) now applies with this exact cut.
For beta in the sum of H_j tensor H_k with j+k<=n, coefficient expansion in the reversed bounded Wick basis gives E_beta p=sum_v x_v a_v.
L2 Holder and Cauchy--Schwarz give ||E_beta p||1<=sqrt(n+1)||beta||2||p||2.
The inserted-letter adjoint is the sum of n+1 isometric concatenations, so beta* is in the actual partial_S adjoint domain and ||v_beta||2<=sqrt(n+1)||beta||2.
Riesz duality, the actual core adjoint identity and its flip-star version then give exactly
\[
 \|E_\beta p\|_2\le2\sqrt{n+1}\|\beta\|_2\|p\|,
 \quad
 \|E_\beta^*p\|_2\le\sqrt{n+1}\|\beta\|_2\|p\|,
 \quad v_\beta=\partial_S^*(\beta^*).
 \tag{G3}
\]
These are the same algebraic identities and limits as in C_F0145; (G1)--(G2) verify the only change of reference.
Approximate a general beta within its finite-degree Hilbert subspace by finite Wick tensors.
At each fixed core polynomial the finite partial_S expansion passes the values in H, and the adjoint isometry bound passes the vacuum.
The estimates therefore hold for all such beta.
Bounded-core weak graph limits restore both original domains as in [C_F0072 Section 4](Yin_C_F0072_v1.md#4-restoration-of-both-full-domains).
For the uses below, n is only 0 or 1.
This is a finite-relative-degree estimate, not boundedness for every Hilbert coefficient.

### Exact coefficients and absence of cancellation

First take the finite N and positive symmetric a of [C_F0149 v2](Yin_C_F0149_v2.md#statement), with projection masses m_i and a standard free semicircular S.
Let Z=sum z_i p_i with distinct z_i.
On N define the divided difference with diagonal zero, denoted delta_N, and extend it to alg(N,S) by delta_N S=0.
This atomic derivative has delta_N Z=1 tensor 1 minus sum_i p_i tensor p_i; it is not an ACSY witness for atomic Z.
The following correction identity is nonetheless an exact represented-core calculation.

Let T=sum a_ij p_i S p_j, and define the desired derivation delta on alg(N,T) to agree with delta_N on N and kill T.
Since the substitution is invertible at finite N, it extends to alg(N,S).
Put beta=delta S.
The difference from the free reference is
\[
 \delta=\delta_N+I_\beta\partial_S.
 \tag{G4}
\]
The multiplier occurring when differentiating T with respect to S is the OUTER map sum a_ij p_i beta p_j.
It is not inner insertion by a.
Its inverse divides a coarse term with external endpoints z,v by a(z,v).

Before componentwise adjoint, the two degree-one coefficient functions of beta are
\[
 \frac{a(w,v)/a(z,v)-1}{z-w}\quad
      \hbox{at }p_z\otimes p_w S p_v,
 \qquad
 \frac{1-a(z,w)/a(z,v)}{w-v}\quad
      \hbox{at }p_z S p_w\otimes p_v.
 \tag{G5}
\]
Repeated divided-difference nodes have value zero in this atomic calculation.
Componentwise adjoint reverses the S-containing leg; with
\[
 r(z,w,v)=a(z,w)/a(w,v)>0,
\]
the two coefficient functions of beta* become
\[
 b_0(z,w,v)=\frac{r^{-1}-1}{\bar z-\bar v},
 \qquad
 b_1(z,w,v)=\frac{1-r}{\bar z-\bar v}.
 \tag{G6}
\]
They are zero at z=v, where symmetry makes r=1.
The two beta* components belong respectively to H_0 tensor H_1 and H_1 tensor H_0, hence are orthogonal.
Their actual partial_S adjoints both land in H_2, with common Wick path (z,w,v), and add.
Thus
\[
 \|\beta\|_2^2=\int(|b_0|^2+|b_1|^2)\,d\mu^3,
 \qquad
 \|v_\beta\|_2^2=\int|b_0+b_1|^2\,d\mu^3.
 \tag{G7}
\]
The vector v_beta is exactly xi_formal from C_F0149: its coefficient is (r^-1-r)/(bar z-bar v).
The marginal vacuum of delta_N is a separate H_0 vector and is not included in xi_formal.

Since r is positive, r^-1-1 and 1-r have the same sign.
Therefore
\[
 |r^{-1}-1|^2+|1-r|^2\le|r^{-1}-r|^2,
 \qquad \|\beta\|_2\le\|v_\beta\|_2.
 \tag{G8}
\]
Combining (G3) at n=1 with (G8) controls the correction on ALL bounded vectors by 2 sqrt(2)||xi_formal||2, independently of the number and masses of blocks and the size or inverse of a.
This removes the all-degree tail-mass obstacle for the corrected normalized derivative in this exact model.
It is not yet a statement identifying the atomic curvature form with the diffuse normal energy: the atomic divided difference has a nonzero diagonal defect.

### Diffuse normal coordinates with finitely many separated spectral blocks

Now let Z be any bounded diffuse normal scalar variable whose marginal divided-difference derivation has an actual L2 vacuum xi_N.
Let S be a free standard semicircular.
Assume the spectrum K of Z is the disjoint union of finitely many compact sets K_i with positive pairwise distance.
Put p_i=1_(K_i)(Z), choose strictly positive real symmetric numbers a_ij, and set T=sum a_ij p_i S p_j.
Write M=W*(Z,S)=W*(Z,T); the equality follows from S=sum a_ij^-1 p_i T p_j and p_i in W*(Z).

The projections p_i belong to the ORIGINAL closed scalar derivation domain, with bounded divided differences.
Choose a smooth function equal to 1 near K_i and 0 near the other pieces.
The C1 polynomial approximation on a surrounding rectangle checked in [C_F0055 Section 3](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) converges uniformly together with first derivatives, hence in the marginal derivative graph.
The quotient is zero within a piece and is bounded across distinct pieces by the inverse spectral separation.
Uniform boundedness of the approximants passes their products with S and each other through the outer Hilbert bimodule actions.
The free reference derivation delta_N therefore extends to alg(C[Z,Z*,p_1,...,p_n],S) by its actual graph and finite Leibniz expansions, still with actual vacuum xi_N.
Its contraction and flipped contraction have the [normalized free-product bounds of C_F0045](Yin_C_F0045_v1.md#statement), using the [scalar actual-vacuum bound of C_F0055](Yin_C_F0055_v1.md#statement).
The normalization is zero at 1; no extra right-multiplier term is added.

Set a(z,v)=a_ij for z in K_i and v in K_j.
Form beta from (G5), now with actual scalar divided differences.
On a strip where z and v belong to the same piece, the numerator in (G6) vanishes, since a is symmetric.
On different pieces the denominator stays uniformly away from zero.
Thus both beta* coefficients are actual bounded measurable functions on K^3, and beta lies in relative S degree one.
Equations (G4)--(G8) hold as actual Hilbert identities; (G4) defines a represented derivation on the enlarged reference core and kills T by direct outer-multiplier substitution.
Restrict it to the target star core C<Z,Z*,T>.
Its actual vacuum is
\[
 \xi=\xi_N+v_\beta,
 \qquad \|\xi\|_2^2=\|\xi_N\|_2^2+\|v_\beta\|_2^2,
 \tag{G9}
\]
because H_0 and H_2 are orthogonal.
Its Z and Z* values are exactly the normal divided difference and its phase, and its T value is zero.

For clarity, the same estimate controls the adjoint-reversed derivation: it is delta_N# plus I_(beta#)partial_S, and ||beta#||2=||beta||2.
Therefore both target contractions E and F have the core bound
\[
 \|Ep\|_2,\|Fp\|_2
 \le\{K_0\|\xi_N\|_2+2\sqrt2\|v_\beta\|_2\}\|p\|
 \le K\|\xi\|_2\|p\|,
 \tag{G10}
\]
where K_0=sqrt(4/pi)(5+2 sqrt(27)) is the C_F0055 scalar constant followed by C_F0045's normalized free lift, and K=sqrt(K_0 squared+8).
The actual core adjoint E*p=p xi-Fp supplies its bound as well.
The bounded-core weak graph mechanism therefore puts all M in the original target contraction closure and actual adjoint; a closure of a sum of unbounded operators is not being assumed.

The T-coordinate derivative is I_(1/a)partial_S, with its coefficient in H_0 tensor H_0.
Its value at T is 1 tensor 1 by the outer action, and it kills Z,Z*.
Equation (G3) at n=0 gives both target canonical domains, and its actual vacuum is R=sum a_ij^-1 p_i S p_j.
Thus the normal pair (Z,T) satisfies both A and S, with a coordinate estimate controlled by its actual vacuum.
The input was only the scalar actual vacuum and the finite separated-block Gaussian construction, not a general correlated-normal theorem.

Finally this does give the formerly missing FULL analytic-unitary lower bound in the diffuse realization of this Gaussian model.
The exact actual normal energy in [C_F0078 Section 6](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains), before the growth estimate is inserted, gives
\[
 \|Eu\|_2^2+\|Fu\|_2^2
 =2\operatorname{Re}\langle Eu,u\xi^*\rangle
  +2\operatorname{Re}\langle Fu,u\xi\rangle-Q_g(u).
\]
Its mixed defect is an actual Hilbert derivation on the core and on the first-derivative analytic limits.
The formula uses the normal phase graph input already present in that section, not the separate growth hypothesis of C_F0078's theorem.
Equations (G9)--(G10) give
\[
 Q_g(u)\ge-(4K+2K^2)\|\xi\|_2^2
 \tag{G11}
\]
for every analytic-core unitary.
No independent absolute bound for C_g or weighted square-root vacuum is used.
This estimates all Wick degrees jointly, through the normalized derivative correction.
It does not improve the sharper first-Wick constant in C_F0149 or turn its atomic xi_formal into an actual conjugate variable.

The countably partitioned or arbitrary measurable Schur-transform limit remains outside this argument.
Finite actual domains for the spectral projections, an inverse multiplier on a new reference core, and convergence of the resulting vacua cannot be inferred from pointwise inversion alone.
In particular the positive-ratio estimate (G8) does not by itself prove that an unknown target derivative extends to S through an unbounded measurable inverse.
The related [C_F0141](Yin_C_F0141_v1.md#statement) uses polynomial coefficients in a selfadjoint base and proves its own target-to-reference mechanism.
It was checked for reuse and is a comparison, not a premise or an extension theorem for this planar normal base.


## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:47 |
| status | open |
| reason | Complete arbitrary-abelian-base relative-degree proof and positive Gaussian correction estimate yield both original canonical domains and the full analytic-unitary lower form for finitely many separated diffuse spectral blocks. Independent review pending; the unrestricted normal implication remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual A and both canonical full domains for the finite separated-block normal Gaussian pair, coefficient-independent vacuum bounds, full analytic-unitary lower form and exact finite-relative-degree lemma. |
| argument | [Argument](#argument) | Relative Wick cut for arbitrary abelian base, actual adjoints, outer-versus-inner inverse, positive-ratio no-cancellation estimate, actual projection graphs, target-core restoration and exact mixed-energy bound. |
| dependency | [Finite block model](Yin_C_F0149_v2.md#argument) | Finite positive Gaussian setup and its actual commutator vacuum; atomic xi_formal scope only. All new correction estimates are proved here. |
| dependency | [Relative-degree proof](Yin_C_F0145_v1.md#argument) | Suffix-cut L1, actual adjoint and reverse-bound mechanism; the changed abelian-base Wick structure is established in G1--G2. |
| dependency | [Free Wick moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Exact free semicircular pairings and relative Wick recurrence, at the unit's stated source scope. |
| dependency | [Scalar actual-vacuum bound](Yin_C_F0055_v1.md#statement) | Scalar constant, actual scalar conjugate interface, and its checked C1 approximation used for separated spectral projections. |
| dependency | [Normalized free lift](Yin_C_F0045_v1.md#statement) | Whole original free-product core and normalized infinity-to-2 bound with squared Grothendieck constant 4/pi; no arbitrary correlated lift. |
| dependency | [Original canonical graphs](Yin_C_F0072_v1.md#statement) | Actual core adjoint and bounded-core weak graph restoration; the necessary two contractions are established here. |
| dependency | [Exact normal energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual mixed normal energy before inserting a growth bound, including phase tensor-leg domains and analytic first-derivative limits. The growth theorem is not a premise. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:04 |
| status | proved |
| reason | Adopt the complete finite separated-block Gaussian theorem after R_F0161 independently checked the whole statement, all three proof sections and seven direct interfaces. The two G5 display corrections preserve mathematical meaning. No arbitrary measurable or unrestricted normal implication is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual A and both canonical full domains for the finite separated-block normal Gaussian pair, coefficient-independent vacuum bounds, full analytic-unitary lower form and exact finite-relative-degree lemma. |
| argument | [Argument](#argument) | Relative Wick cut for arbitrary abelian base, actual adjoints, outer-versus-inner inverse, positive-ratio no-cancellation estimate, actual projection graphs, target-core restoration and exact mixed-energy bound. |
| dependency | [Finite block model](Yin_C_F0149_v2.md#argument) | Finite positive Gaussian setup and its actual commutator vacuum; atomic xi_formal scope only. All new correction estimates are proved here. |
| dependency | [Relative-degree proof](Yin_C_F0145_v1.md#argument) | Suffix-cut L1, actual adjoint and reverse-bound mechanism; the changed abelian-base Wick structure is established in G1--G2. |
| dependency | [Free Wick moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Exact free semicircular pairings and relative Wick recurrence, at the unit's stated source scope. |
| dependency | [Scalar actual-vacuum bound](Yin_C_F0055_v1.md#statement) | Scalar constant, actual scalar conjugate interface, and its checked C1 approximation used for separated spectral projections. |
| dependency | [Normalized free lift](Yin_C_F0045_v1.md#statement) | Whole original free-product core and normalized infinity-to-2 bound with squared Grothendieck constant 4/pi; no arbitrary correlated lift. |
| dependency | [Original canonical graphs](Yin_C_F0072_v1.md#statement) | Actual core adjoint and bounded-core weak graph restoration; the necessary two contractions are established here. |
| dependency | [Exact normal energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual mixed normal energy before inserting a growth bound, including phase tensor-leg domains and analytic first-derivative limits. The growth theorem is not a premise. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0161_v1.md#conclusion) | Whole statement and argument, arbitrary-base finite-degree lemma, positive correction, actual graphs, full analytic-unitary bound and all seven direct interfaces. |

