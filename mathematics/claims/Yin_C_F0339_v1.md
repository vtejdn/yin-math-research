---
author: Yin
---

# An equivalent lattice inequality for the normal converse

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

In a finite von Neumann algebra with faithful normal probability trace take a projection \(P\) of trace \(1/2\) and a finite partition of unity by nonzero orthogonal projections \(e_i\) with \(t_i=\tau(e_i)\).
Use the algebra \(N=W^*(P,(e_i)_i)\), the finite-dimensional abelian subalgebra \(D=\operatorname{span}\{e_i\}\), and the represented starred word algebra \(\mathcal N=\operatorname{alg}^*(D,P)\).
Assume its partial liberation derivation \(\gamma\), given by \(\gamma e_i=e_i\otimes1-1\otimes e_i,\ \gamma P=0\), descends and has actual vacuum \(\eta=\gamma^*(1\otimes1)\).
Label the projections by distinct points \(c_i\) of a translated square lattice of mesh \(h>0\) in the complex plane.
Put
\[
 \begin{gathered}
 U=\sum_i c_i e_i,\quad k_{ij}=\begin{cases}1/(c_i-c_j)&i\ne j,\\0&i=j,\end{cases}
 \quad d_c=I_{\sum k_{ij}e_i\otimes e_j}\gamma,\qquad E_c=(\mathrm{id}\otimes\tau)d_c,\\
 H_i=\sum_{j\ne i}t_j/(c_i-c_j),\qquad
 M_i=\sup_{s\ge h}\frac{\sum_{|c_i-c_j|\le s} t_j}{s},\\
 B_c^2=\sum_i t_i(M_i^2+|H_i|^2)
       +\sum_{i\ne j}\frac{\|e_i\eta e_j\|_2^2}{|c_i-c_j|^2}.                  \tag{1}
 \end{gathered}
\]
Here \(I\) inserts the finite marginal tensor between the two outer factors.
The derivative of \(U\) is the off-diagonal tensor \(1\otimes1-\sum_i e_i\otimes e_i\).
The finite set of marginal labels puts no finite-dimensional assumption on \(N\).

Let \(K_{\mathrm{lat}}\) be the supremum of \(\|E_c p\|_2/B_c\) on all such data and all \(p\in\mathcal N\) of operator norm at most one.
Let \(K_{\mathrm{proj}}\) be the [original relative projection-coefficient constant](Yin_C_F0308_v1.md#statement).
There is an absolute \(C\) such that, in the extended nonnegative reals,
\[
     K_{\mathrm{proj}}\le C K_{\mathrm{lat}},\qquad
     K_{\mathrm{lat}}\le C K_{\mathrm{proj}}.                                 \tag{2}
\]
Consequently \(\mathsf A\Rightarrow\mathsf S\) on arbitrary correlated normal tuples holds exactly when the single lattice inequality \(\|E_c p\|_2\le K B_c\|p\|\) has an absolute finite constant.
Scaling allows one to fix \(h=1\) in the lattice problem.

In the direction from a discrete witness to an actual relative coordinate, each \(c_i\) can be replaced by a circle of the same radius \(h/8\), with uniform conditional probability.
Conditional expectation recovers the exact discrete derivative on the whole finite-label word algebra from limits of the original polynomial derivatives.
In the converse direction every finite test from the original relative problem can also be approximated, up to an absolute factor in its normalized cost, with marginal supports a finite union of parallel horizontal segments of length \(h/4\) centered at lattice points.
Each of the circle and segment models individually has both canonical bounded-vector domains.
The existence of a uniform constant as the number of labels increases remains open.

## Argument

### Rounding an actual coordinate

Start with an actual relative \(Z,P\) in the projection problem, in the algebra they generate.
Write \(\mu\) for the diffuse law of \(Z\), \(\xi\) for the distinguished vacuum, and \(\xi_\mu\) for its marginal projection.
With the [relative commutator calculation](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core), partial liberation has vacuum \(\eta_0=[Z^*,\xi]\) and inverse-gap norm integral at most \(\|\xi\|_2^2\).
The proof uses only the distinguished derivative; the projection is a killed coefficient throughout.
Take a half-open grid of mesh \(h\), omit null cells, and let \(e_i\) be their spectral projections and \(c_i\) their centers.
Bounded support gives finitely many labels and \(\|Z-U\|\le h\).
The [Borel extension of the marginal liberation graph](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) takes each \(e_i\) to its inner difference.
Indeed uniformly bounded strong-star polynomial approximants have that explicit convergent derivative, and the outer product rule passes to finite words.
The restricted vacuum on \(N\) is \(\eta=\mathbb E_N\eta_0\).
Conditional expectation is \(D\)-bimodular, so each \(\|e_i\eta e_j\|_2\le\|e_i\eta_0 e_j\|_2\).
For \(i\ne j\), the old distances on the two cells are at most \(3|c_i-c_j|\).
This bounds the last sum in (1) by \(9\|\xi\|_2^2\).

For \(x\) in cell \(i\), mass in a center ball of radius \(s\ge h\) comes from the old ball at \(x\) of radius at most \(4s\), so \(M_i\le4M_1\mu(x)\) with an immaterial enlargement for ball boundaries.
To estimate \(H_i\), compare it at \(x\) with the soft Cauchy integral
\[
       C_h\mu(x)=\int\frac{\overline{x-y}}{|x-y|^2+h^2}\,d\mu(y).
\]
For \(|c_i-c_j|\le 6h\) both kernels have absolute value at most \(1/h\), with the discrete value zero in the same cell; the mass is at most \(C h M_1\mu(x)\).
On the other cells, for \(y\) in cell \(j\), replacing \(x-y\) by \(c_i-c_j\) and removing the regularization costs at most \(Ch/|x-y|^2\).
Annuli of radii \(2^k h\) around \(x\) contribute at most \(C2^{-k}M_1\mu(x)\) each.
Thus \(|H_i-C_h\mu(x)|\le C M_1\mu(x)\).
The [maximal density criterion](Yin_C_F0255_v1.md#statement) and the [scalar soft Cauchy estimate](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) bound the full discrete budget by \(B_c\le C\|\xi\|_2\), uniformly in the mesh.

On \(U,U^*,P\) the discretized derivative has values \(1-\sum e_i\otimes e_i\), \(\sum_{i\ne j}(\bar c_i-\bar c_j)(c_i-c_j)^{-1}e_i\otimes e_j\), and zero.
At \(\mu^2\)-almost every pair of original spectral points these marginal kernels converge as \(h\downarrow0\) to the unit and the normal phase, by diffuseness.
They are bounded by one.
Dominated convergence in the original coarse norm, norm convergence of the operators, and the finite Leibniz rule imply that \(d_c p(U,P)\to\delta p(Z,P)\) in the common coarse space for each fixed starred polynomial.
The input norms converge and the right slices converge in \(L^2\).
The lattice estimate implies the first inequality of (2).

### Free noise in each spectral corner

Conversely take the finite data of (1) and freely adjoin finitely many independent standard semicirculars \(S_i\) to \(N\) in a tracial free product.
In \(e_i\) the variable \(t_i^{-1/2}e_i S_i e_i\) is standard semicircular for the normalized corner trace.
Every bounded Borel function of it, taken in that corner, has conditional expectation onto \(N\) equal to its normalized trace times \(e_i\).
For polynomials this follows by the [free semicircular mixed-moment and compression formulas](../audits/literature/NS06/Yin_U004.md#ns06-u004), since intermediate coefficients in the conditional Wick calculation are scalar multiples of \(e_i\) or \(1\); bounded spectral approximation gives the Borel assertion.
Use a Borel function of this diffuse scalar to obtain a corner normal \(V_i\) with normalized uniform law on the circle of radius \(h/8\) about \(c_i\).
Alternatively take uniform arclength on the horizontal segment with center \(c_i\) and half-length \(h/8\).
Put \(V=\sum_i V_i\).
Its disjoint marginal components recover all \(e_i\) by spectral calculus, so \(N\subset M'=W^*(V,P)\).
Write \(\mu_i'\) for these conditional probabilities and \(\mu'=\sum_i t_i\mu_i'\).

On \(\mathcal N\), set \(\Lambda=\operatorname{ad}-\gamma\) with \(\operatorname{ad}(b)=b\otimes1-1\otimes b\).
It kills \(D\), takes \(P\) to its inner difference, and has vacuum \(-\eta\).
The [centered free extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) by zero on the new noise preserves this adjoint identity: a reduced word containing a centered new letter has a centered new letter on a surviving prefix or suffix of every cut, so its double trace is zero.
Only covariance under the involution up to the scalar \(i\) is needed for closability; \(i\Lambda\) is real and its polynomial tensors belong to the adjoint domain by the tensor adjoint formula.
Bounded functions of the compressed noises used in \(V\) can be approximated boundedly and strong-star by polynomials in the corresponding \(e_i,S_i\), all killed by this extension.
Their words with \(\mathcal N\) satisfy the same adjoint and product formulas by graph convergence.
Subtracting the extension from \(\operatorname{ad}\) therefore gives an actual partial liberation on the represented \(V,P\) core, with intrinsic vacuum \(\eta\in L^2(N)\subset L^2(M')\).
Its values on \(V,V^*,P\) are their marginal inner differences and zero at \(P\), so its core values are intrinsic.

For each \(i\), insertion of \(e_i\otimes e_i\) into \(\gamma\) gives zero on all old generators and words.
The two end corrections in the double trace of \(\gamma(e_i p e_i)\) cancel, leaving the inserted double trace at \(p\).
Consequently \(e_i\eta e_i=0\).
The mass of the new liberation spectral measure on the product of components \(i,j\) is exactly \(\|e_i\eta e_j\|_2^2\).
Distinct components have separation at least \(3|c_i-c_j|/4\), hence its full inverse-gap integral is bounded by the last sum in (1) times \(16/9\).

More precisely on distinct components this measure is \(\|e_i\eta e_j\|_2^2\,\mu_i'\otimes\mu_j'\).
For bounded \(v\in e_iNe_j\) compute \(\tau(v^*f(V_i)v g(V_j))\).
Center the two marginal functions over \(N\) using the conditional means computed above.
Their centered parts are limits of sums of free reduced words containing their respective distinct noise labels and otherwise \(N\)-letters.
The term with both centered parts has trace zero, since those distinct labels cannot cancel across the joining \(N\)-factors; one centered part has zero contribution as well.
Approximation of \(e_i\eta e_j\) in Hilbert norm by such bounded \(v\)'s proves the product formula.
In particular the new spectral density is bounded and constant on each off-diagonal product of labels and vanishes on all diagonal products.
With finitely many separated components its density is dominated by squared differences of a finite-valued label map of finite divided-difference energy, by spacing the finitely many distinct scalar map values sufficiently far apart.
The [feature estimate](Yin_C_F0337_v1.md#statement) therefore gives both original bounded-vector domains once the actual vacuum is constructed.
This qualitative use allows its bound to depend on the finite data.

### The scalar vacuum of the spread measure

Each conditional scalar law has vacuum of norm at most \(C/h\).
For the circle this follows from the [scalar geometric criterion](Yin_C_F0255_v1.md#statement) using the linear arclength growth and its constant curvature; for the segment use its linear growth and zero curvature.
With the inner product linear in the second variable the conjugate of the scalar vacuum on component \(i\) is
\[
  t_i\overline{\xi_{\mu_i'}(z)}
            +2\sum_{j\ne i}t_j\int\frac{1}{z-w}\,d\mu_j'(w).             \tag{3}
\]
Indeed the within-component divided-difference test uses weight \(t_i^2\), and interchanging the two endpoints on distinct components gives the factor two in its vacuum pairing.
These identities on the actual scalar polynomial core prove (3).
For \(z,w\) on components \(i,j\) the difference between \(1/(z-w)\) and \(1/(c_i-c_j)\) has magnitude at most \(C h/|c_i-c_j|^2\).
Decomposing the other centers by dyadic distance bounds the summed error by \(C M_i\).
Since \(t_i/h\le M_i\), (3) has squared norm at most \(C\sum_i t_i(|H_i|^2+M_i^2)\).
The [reconstruction from the actual partial liberation and the scalar vacuum](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) now gives an actual relative distinguished derivative \(\delta'\) at \(V\) with \(\|\xi'\|_2\le C B_c\).
Here one uses injectivity of the inner gap for the diffuse marginal, the marginal adjoint identity, and the zero prescribed derivative on the selfadjoint coefficient \(P\), exactly as in the [relative projection construction](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries).
It requires no derivative taking \(P\) to \(1\otimes1\).

### Recovering the discrete derivative on circles

For each \(e_i\) take a smooth function on a box containing the spectrum, identically one near its component and identically zero near all others.
The [first-derivative polynomial approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) gives uniform convergence of the functions and first derivatives by real-coordinate polynomials in \(V,V^*\).
Their divided differences converge uniformly off the diagonal on the spectral square by the real mean-value bound on the box.
Thus in the graph of \(\delta'\) the tensor of \(e_i\) has symbol
\[
                \frac{1_i(z)-1_i(w)}{z-w}.
\]
On an equal-component square it vanishes.
The same graph approximation in any fixed word in the \(e_i,P\) converges in operator norm on inputs and in coarse norm on derivatives.

For circle components the conditional mean of \(1/(z-w)\) on distinct components equals \(1/(c_i-c_j)\).
Indeed the uniformly convergent geometric expansion in the two centered displacements has constant term \(1/(c_i-c_j)\); all its higher terms average to zero by the circle moments and independence of the two integrations.
Projection by \(\mathbb E_N\otimes\mathbb E_N\) on the marginal product tensor takes precisely these product means on each pair of labels.
This follows on separated factors by the conditional expectation formula in each corner, and on the stated bounded kernel by Hilbert approximation.
Consequently it sends \(\delta'e_i\) to \(d_c e_i\), and it sends the zero derivative of \(P\) to zero.
By \(N\)-bimodularity for the outer actions it gives \(d_c p\) on every old word.
The projected right slice has norm at most that of the continuous right slice.
Applying \(K_{\mathrm{proj}}\) to the original approximating polynomials and passing to their graph limits proves \(\|E_c p\|_2\le C K_{\mathrm{proj}} B_c\|p\|\), the second inequality of (2).

### Parallel segments and the original witnesses

For an actual initial \(Z,P\), perform the same segment construction at every mesh in a scalar free extension of its original ambient algebra.
Use the previously rounded \(N=W^*(D,P)\) as the old algebra to which the construction applies.
Then \(Z,V\) each commute with the same \(e_i\), are within \(h\) and \(h/8\) of \(U\) respectively, and have the same coefficient \(P\).
Thus any fixed polynomial values converge in norm in their mesh-dependent couplings.
The normal phases at \(Z\) and \(V\) approach one another in the common coarse norm.
To see this, compare both with the blockwise discrete phase at \(U\), set to zero on equal labels.
For pairs of centers farther than a fixed \(s>0\), the difference of either phase from its discrete value is at most \(C h/s\) when \(h<s/4\).
The total product mass of the remaining label pairs equals \(\sum_{|c_i-c_j|\le s}t_it_j\) under either marginal, bounded by \(\mu^2\{|z-w|\le s+2h\}\).
First let \(h\) decrease and then \(s\) decrease, using diffuseness.
The unit tensors at the unstarred generators already agree.
The finite Leibniz expansion and the contraction of the right trace compare every fixed slice with its original value to error tending to zero, whereas \(\|\xi'\|_2\le C B_c\le C'\|\xi\|_2\).
This proves the segment assertion even though segments do not have the circle mean-value identity.
Finally the [uniform projection theorem](Yin_C_F0308_v1.md#statement) identifies finiteness of \(K_{\mathrm{proj}}\) with the full original normal implication, including its counterexample assembly if the constant is infinite.
Replacing \(c_i,h\) by \(c_i/h,1\) scales \(E_c\) and \(B_c\) by the same factor \(h\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:16 |
| status | open |
| reason | Fix the two directions of the lattice reduction, the exact circle averaging on finite words and the parallel-segment approximation to original tests. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalent discrete inequality with absolute comparison, same-mesh circular recovery and horizontal segment witnesses. |
| argument | [Argument](#argument) | Rounding, scalar Cauchy and inverse-gap budgets, corner noise extension, actual vacua, conditional recovery and norm transfer. |
| dependency | [Projection reduction](Yin_C_F0308_v1.md#statement) | Equivalence of the uniform relative estimate to the original normal implication. |
| dependency | [Liberation from the derivative](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Distinguished commutator, gap tensors and inverse-gap bound, with only a killed coefficient. |
| dependency | [Borel graph extension](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Extension of marginal liberation on spectral projections, exact differentiated products and traces. |
| dependency | [Scalar geometric estimate](Yin_C_F0255_v1.md#statement) | Maximal density bound from the old vacuum and scalar existence for the two spread laws. |
| dependency | [Soft Cauchy bound](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform scalar estimate at the rounding mesh. |
| dependency | [Free semicircular compression](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Normalized corner law, scalar free mixed moments and conditional expectation onto the old algebra. |
| dependency | [Centered free extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Preservation of the vacuum after adjoining freely independent killed noise. |
| dependency | [Finite-label domains](Yin_C_F0337_v1.md#statement) | Qualitative strong domains under domination by a finite-valued scalar map of finite secant energy. |
| dependency | [Actual reconstruction](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Sufficiency of scalar and inverse-gap conditions for the distinguished vacuum. |
| dependency | [Relative projection](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Application to a killed atomic coefficient without a second actual derivative. |
| dependency | [Scalar approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | First-derivative polynomial approximation on a box and hence divided-difference convergence of the smooth label functions. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:20 |
| status | proved |
| reason | R_F0344 checked both absolute estimates, the exact conditional projection on circles, parallel segment approximation, actual relative vacua and all eleven direct interfaces of the full lattice equivalence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalent discrete inequality with absolute comparison, same-mesh circular recovery and horizontal segment witnesses. |
| argument | [Argument](#argument) | Rounding, scalar Cauchy and inverse-gap budgets, corner noise extension, actual vacua, conditional recovery and norm transfer. |
| dependency | [Projection reduction](Yin_C_F0308_v1.md#statement) | Equivalence of the uniform relative estimate to the original normal implication. |
| dependency | [Liberation from the derivative](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Distinguished commutator, gap tensors and inverse-gap bound, with only a killed coefficient. |
| dependency | [Borel graph extension](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Extension of marginal liberation on spectral projections, exact differentiated products and traces. |
| dependency | [Scalar geometric estimate](Yin_C_F0255_v1.md#statement) | Maximal density bound from the old vacuum and scalar existence for the two spread laws. |
| dependency | [Soft Cauchy bound](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform scalar estimate at the rounding mesh. |
| dependency | [Free semicircular compression](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Normalized corner law, scalar free mixed moments and conditional expectation onto the old algebra. |
| dependency | [Centered free extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Preservation of the vacuum after adjoining freely independent killed noise. |
| dependency | [Finite-label domains](Yin_C_F0337_v1.md#statement) | Qualitative strong domains under domination by a finite-valued scalar map of finite secant energy. |
| dependency | [Actual reconstruction](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Sufficiency of scalar and inverse-gap conditions for the distinguished vacuum. |
| dependency | [Relative projection](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Application to a killed atomic coefficient without a second actual derivative. |
| dependency | [Scalar approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | First-derivative polynomial approximation on a box and hence divided-difference convergence of the smooth label functions. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0344_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
