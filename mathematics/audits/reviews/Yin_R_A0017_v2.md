---
author: Yin
---
# Independent review of distinct incidence couplings and their projection geometry

Review act: 2026-11-11T13:59, in UTC, for Yin.
The exact target is the complete 2026-11-11 working revision of [C_A0004_v2](../../claims/Yin_C_A0004_v2.md#statement) and its [argument](../../claims/Yin_C_A0004_v2.md#argument), including formulas (1)--(25), all intervening assertions, the collective-holonomy subsection, the explicit inverse following (24), and the concluding source and generality limits.
This is new review evidence for the distinct-coupling variant.
The [preceding review](Yin_R_A0017_v1.md#whole-artifact-finding) retains its actual v1 target and is not relabelled as a review of v2.

## Arrangement and accepted inputs

A separately organized reviewing agent outside substantive proof development performed this whole-argument inspection.
Its initial context contained the fixed target locator, governing instructions, actual human and scope, and administrative work-start metadata.
It contained no development dialogue, development draft, mathematical development summary, author explanation or previous verdict about the target.
The reviewer enumerated the obligations from the statement and formed initial findings from the complete target before consulting the existing input-review conclusions.
During inspection it received notices identifying two additions to the target, read those additions directly and checked their affected interfaces.
It read no development draft or development-helper answers and supplied no substantive repair.

The review accepted the exact [incidence certificate](../../claims/Yin_C_A0004_v1.md#geometric-integer-certificate), [first-return convention](../../claims/Yin_C_A0004_v1.md#complete-first-return) and [finite-support obstruction](../../claims/Yin_C_A0004_v1.md#noncompact-edge-modes), with their [v1 review](Yin_R_A0017_v1.md#whole-artifact-finding), at those unchanged interfaces only.
It inspected the underlying [finite-graph formulation](../../claims/Yin_C_A0003_v1.md#finite-graph-certificate), [tree-transport proof](../../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators) and corresponding [Claim finding](Yin_R_A0007_v1.md#claim-finding).
The bounded transport argument remains valid before the torsion-free step, which is replaced by the newly checked infinite-orbit argument in the collective-holonomy extension.

The accepted [finite-trace support identities](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) were checked for their rectangular application by polar decomposition.
No integer-rank theorem for arbitrary group-ring matrices is imported.
The general source proof of these finite-von-Neumann-algebra foundations was not re-audited.

The exact [tree and square-lattice transforms](../../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms), with the applicable [independent review](Yin_R_A0016_v1.md#whole-artifact-finding), were read for the degree-four normalization, elliptic modulus convention and tree spectral interval.
The target's weighted cavity argument and complex endpoint adaptation were checked directly, rather than transferred from the isotropic or real-endpoint cases.
The accepted inputs do not form a dependency cycle through the new variant.

## Whole-artifact finding

No substantive mathematical gap was found in the complete current statement and argument under their stated hypotheses.
The grounds for that finding are the following checks of every numbered formula and the additional assertions.

### Common projection and full matrices

The two actual loop labels give an injective incidence column in both groups.
The lower kernel equation then forces the root coordinate to vanish, independently of the bounded selfadjoint base operator.
The polar isometry has initial projection equal to the identity, and rectangular support-trace equality gives the edge-kernel dimension \(2-1\).
The bounded regularized operators converge strongly to the range projection, proving (3) without a bounded inverse for the lattice Laplacian.

The imaginary-part estimate for \(z-a-L/z\), together with the estimate for its adjoint, proves invertibility throughout the upper half-plane.
Block elimination gives (5) in its displayed noncommuting order.
Strict negativity of the finite-cell Green imaginary part gives its invertibility and validates (2).
The accepted renewal convention matches the direct Schur formula, while the full-layer return operator uses a different projection and cannot be replaced by a traced version of the cell formula.

For (6), averaging the real parts of \(b_1,b_2\) gives \(x/2,y/2\), and the independent odd sine terms remove the remaining contributions.
This yields the off-diagonal edge entry \(Z/(4z)\) as well as the root-edge entries.
Schur inversion with edge block \(M/z\) gives exactly (7)--(8).
The transposes are bilinear analytic transposes, and strict negativity on the edge subspace proves \(M\) invertible; invertibility of the full matrix then gives \(h\ne0\).

Formula (9) is the pointwise orthogonal complement of the incidence column away from the zero-measure common zero.
The arcsine average of \(x/(x+y)\) and the remaining integral give \(\mathbb E[xy/(x+y)]=2-4/\pi\).
Thus (4) has the stated lattice matrix, eigenvalues \(1/\pi\) and \(1-1/\pi\), trace one and rank two.

### Lattice endpoint, spectral bands and return asymptotics

The comparison with \(-(L+2z)^{-1}\) has a numerator bounded by a constant times \(\eta L+\eta^2\) on \(z=i\eta\).
The true and comparison denominators are uniformly bounded below by a constant times \(L+\eta\).
The convolution density of \(L\) is bounded near zero, so the two error integrals have orders \(O(\eta\log(1/\eta))\) and \(O(\eta)\).
The singularity of that density away from zero does not invalidate the estimate, because the denominators there are bounded away from zero.

The exact isotropic transform uses parameter \(4+2z\), and its complementary elliptic modulus satisfies \(k'^2=z+O(z^2)\).
The principal logarithm therefore gives \(-\log(16/z)/(4\pi)\).
Along the positive imaginary axis this has imaginary constant \(+1/8\), verifying the normalization, sign and error in (10).

Symmetrizing \(X-Y\) gives the limiting integrand \((x-y)^2/(2L^2)\).
Together with \(X+(1-z)Y=(z^2-2z)q-1\) and \(\mathbb E[xy/L^2]=1/(2\pi)\), this gives every constant in (11).
The derivative limit for \(Z\) is justified by \(xy\le L^2/4\), and its value is \(3/\pi-1\).
Substitution establishes the full matrix expansion (12), including its non-scalar constant part.

The symmetric edge vector is the \(1/\pi\)-eigenvector of \(C_Z\), giving \(r^{\mathsf T}C_Z^{-1}r\to\pi/8\).
Consequently \(h=q-\pi/8+o(1)\).
Substituting in (8) then gives the root coefficient, both root-edge coefficients and both edge eigendirections in (13), with the stated signs and remainder order.
The exact trace identity gives (14), including the factor three, the real constant \(-1/6\) and the imaginary constant \(-1/12\).

The nonzero fiber branches have the stated derivatives and opposite signs away from \(x+y=0\).
The positive branch exceeds one, making its derivative in \(y\) negative.
The corner values therefore give exactly \([-4,0]\) and \([\sqrt5-1,\sqrt5+1]\).
For fixed \(y\), nonzero derivative in \(x\) gives absolutely continuous pushforward laws; positive matrix spectral measures are dominated by the trace law.
Continuity and positive-measure preimages give the whole stated support, including its endpoints.

The unique zero contact has expansion \(\lambda_-=-(\theta^2+\phi^2)/2+O((\theta^2+\phi^2)^2)\).
The uniform polar-coordinate inversion gives density \(1/(2\pi)+O(\varepsilon)\) on the negative side.
There is no positive continuous mass below \(\sqrt5-1\).
After division by three, integration yields exactly (15).
The spectral multiplier is bounded by one and tends pointwise to the kernel indicator, giving strong residue convergence.
Its norm on the active complement remains one because zero belongs to that complement's spectrum, whereas finite-cell compression converges in matrix norm.

### Weighted free-tree matrices and isolated atom

The deleted-edge operators are compressions of the positive degree-four Laplacian, so the lower spectral bound survives on each subtree.
The same upper-half-plane pencil estimate gives actual analytic cavity inverses.
Deleting an edge of each type gives the two multiplicities in (16).
Both orientations carry the analytic coefficient \(t\), so the recursion uses \(t^2\), not \(|t|^2\).
The actual operator inverses specify the physical branch and the large-parameter behavior.

Successive elimination along the unique reduced-word path gives a factor \(h_u\) for a \(u\)-edge and \(t h_v\) for a \(v\)-edge.
The coefficients at words of lengths zero, one and two then give all entries of (17), including \(-gc_1c_2/z\).
Schur inversion gives (18), with its signs determined by the root complement \(-zW\).
The strict imaginary-part argument proves the stated inverses and nonvanishing condition.

At parameter four, the accepted tree transform gives coefficient \((3/8)3^{-|h|}\).
Multiplying \(I-DL^{-1}D^*\) in the actual left-convolution convention gives the four translated terms in (19).
At the identity this yields the free matrix in (4), with eigenvalues \(1/3\) and \(2/3\).
At \(v^n\) the first diagonal coefficient is \(-3^{-n}/6\), proving infinite support.
The coefficient estimate alone is correctly not used to assert absolute summability.

The Schur inequality gives the positive radius in (20).
The explicit bounded active inverse used in the general gap argument also handles the center of this interval.
Thus the complementary resolvent extends analytically through zero, and the full residue converges in norm with error \(O(\eta)\).

Differentiating the two cavity equations gives \(h_u'=-1/5\) and \(h_v'=-2/15\).
The product \(t h_v\) has derivative \(-7/15\), and the root diagonal has derivative \(g'=-9/32\).
Substitution gives every coefficient in (21).
For the return matrix, the resulting values \(W(0)=3/4\) and \(W'(0)=-9/16\) give the root pole and constant in (22).
The derivative of \(g/W\) vanishes at zero; the derivative of \(M_F^{-1}c\) is \((0,1)^{\mathsf T}\).
These facts verify the unequal root-edge linear coefficients in (22).
The edge linear term is exactly \(-zI_2/2\).
A pole of this return function is therefore compatible with a vanishing root Green function and no root atom.

### Projection geometry and the finite probabilistic interpretation

Entrywise Parseval and \(PP^*=P\) give (23), including the order \(P(g)P(g)^*\).
Cauchy--Schwarz gives absolute convergence of each scalar matrix entry.
Removing the identity coefficient gives \(C-C^2\), and the trace inequality follows from the \(E\) real eigenvalues of \(C\).
The two explicit squared masses follow from the eigenvalues already checked.
The sum vanishes exactly when all off-cell coefficients vanish.

On the lattice, the polynomial cycle column lies in the kernel and spans its measurable one-dimensional fibers almost everywhere.
The closure-of-range argument, followed by polynomial density in the scalar input space, proves generation by its translates even though the multiplier vanishes at one point.
Different directional limits of the projection diagonal exclude a continuous representative.
Fourier transformation then excludes membership in the reduced group \(C^*\)-algebra, absolute coefficient summability and finite propagation.

On the free group, the norm-convergent geometric series for \(L^{-1}\) gives finite-propagation approximants at a geometric rate.
It does not assert that those approximants are projections.
The accepted finite-forest leaf argument excludes every nonzero finitely supported kernel vector.
The two examples therefore verify both directions of the asserted distinction between finite-support generation and projection regularity.

For the two-edge determinantal law, inclusion-exclusion gives the two singleton probabilities, the double probability and the empty probability exactly as stated.
The matrices in (4) are positive contractions, and these four probabilities are nonnegative and sum to one.
Direct calculation of the first and second moments gives mean one and variance \(\operatorname{Tr}(C-C^2)\).
This is a finite probability interpretation, without an inference of group-ring integrality from an arbitrary integer mean.

### General sufficient conditions and determinant limits

In the collective-holonomy extension, the tree equations and all loop transports remain valid for groups with torsion.
Each unit phase disappears after taking absolute values, so a joint fixed vector has constant modulus on every orbit of the subgroup generated by the actual loop labels.
If that subgroup is infinite, all its regular-action orbits are infinite, and square summability forces the vector to vanish.
Inconsistent phases cannot invalidate this sufficient implication.
The subgroup is the image of the based loop group; changing tree preserves that image at a fixed root, and changing root conjugates it.
Thus infinitude is independent of the choices.
The finitely generated infinite-group example has this full holonomy group, including when its generators have finite order.
The same support-trace subtraction gives \(E-N\), without asserting anything about finite holonomy or arbitrary matrices.

For (24), polar decomposition identifies precisely the active complement.
The displayed inverse is a bounded two-sided inverse when \(L\ge\gamma I\), with the correct noncommuting order in its lower-right entry.
The real-parameter Schur estimate gives the stated radius for \(\|A\|\le a_0\).
If there is no positive lower bound, the unit vectors \((0,Vf_n)\) have images of norm tending to zero, proving the reverse implication.
The geometric series for \(L^{-1}\) gives the recorded approximation error, with the constant-inverse case treated separately.

For (25), the lower equation gives \(x=-C_0D^*y\) by injectivity of \(D\).
Substituting into the upper equation gives exactly \((I-AC_0)D^*y=0\).
Its assumed injectivity then proves the kernel equality and the unchanged orthogonal projection.
The norm-product condition is a sufficient Neumann-series criterion; the finite coefficient-sum bound is an available upper bound and is not asserted necessary.
The real scalar perturbations \(|\epsilon|<1/2\) meet that criterion for these models.
No arbitrary edge-potential invariance is inferred.

The finite-cell determinant identities follow from the same Schur complements used for the full inverses.
Since \(\det C_F=2/9\) and \(W(0)=3/4\), the free constant is \(-1/6\).
The lattice complement \(h\) gives the stated logarithmic factor and coefficient.
Both logarithmic growth exponents are one although the local residue matrices have rank two.
These computations do not identify a finite-cell determinant with a group-operator determinant or its logarithmic derivative with the full spectral trace.

## Source applicability and limits

The reviewer directly inspected [DLMF 19.12.1 and the value following 19.12.3](https://dlmf.nist.gov/19.12).
The convergent series permits a complex complementary modulus with \(0<|k'|<1\), uses the principal logarithm, and has \(d(0)=2\log2\).
These statements supply the precise complex-endpoint input in (10); the complete source derivation was not audited.

The exact [Lyons arXiv:math/0204325v4 PDF](https://arxiv.org/pdf/math/0204325v4), dated 18 June 2003, was checked at Section 1, equation (1.1), PDF page 2, and Section 3, especially the final paragraphs on PDF page 10.
These passages give the determinantal inclusion convention and distinguish the closed star space from the closure of finite cycle spaces, with the corresponding wired and free forest projections.
Their role here is attribution and interpretation.
The finite two-edge law was checked directly, and no infinite-forest theorem or source proof is a premise of the new matrix, index or asymptotic calculations.
The complete source proof and historical priority were not investigated.

The accepted tree, lattice, incidence and finite-trace inputs are sufficient at the exact interfaces described above.
The previous reviews are reused only for those inputs, and no repeated-leaf asymptotic is transferred to v2.
No unresolved source-applicability issue was found at the stated scope.
This is mathematical agent review without numerical experiments or a proof assistant.

The result does not determine the full free-model spectral type away from the zero gap, classify finite-holonomy cases, establish universal determinant behavior or convert arbitrary group-ring matrices to incidence form.
It supplies neither a new Atiyah group class nor completion of the [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).
The target's mathematical assessment and any Task decision remain separate acts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0004_v2.md#statement) | Exact four-part statement, every hypothesis and normalization, both complete matrix models, projection geometry and all separately stated extensions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0004_v2.md#argument) | Complete current argument, formulas (1)--(25), analytic branches, matrix inverses, endpoint constants and estimates, spectral support, locality, finite probability law, general sufficient conditions, determinant calibration, accepted-input interfaces and source limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Collective holonomy](../../claims/Yin_C_A0004_v2.md#collective-holonomy-condition) | Entire added subsection: arbitrary discrete groups, phases, infinite actual holonomy subgroup, orbit proof, choice invariance, finitely generated example and finite-holonomy limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Gap and deformations](../../claims/Yin_C_A0004_v2.md#gap-and-deformation-conditions) | Both directions of (24), explicit bounded active inverse, quantitative gap and finite-propagation approximation, complete (25) and norm-product sufficient condition. |
