---
author: Yin
---
# Cauchy residues through geometric index formulas

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Seek a relation-compatible geometric index formula for spectral residues of finite complex group-ring matrices. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Test a genuinely noncentral kernel representation that escapes the proved central-fiber gap obstruction, or supply independent trace arithmetic for an already gapped actual projection; finite central constructions preserving the singular fiber cannot create the required gap. |

## Mechanism

The [Cauchy synthesis](../ledger/Yin_L_A0015_v1.md#boundary-residues-and-reciprocal-slopes) identifies integer unnormalized kernel dimension with integer total boundary residue.
Its [Schur-energy formula](../ledger/Yin_L_A0015_v1.md#schur-complements-and-boundary-energy) separates a real balance equation from the square-integrability that produces an atom.
A generic resolvent equation does not supply the required arithmetic.

The [geometric source model](../ledger/Yin_L_A0015_v1.md#a-geometric-index-mechanism-beyond-algebraicity) supplies additional information.
For the universal-cover Jacobi operator of a finite graph with nonzero complex Hermitian scalar edge weights and real potentials, the Aomoto index theorem identifies the sum of vertex residues with the number of components of the atom-support forest minus its external boundary size.
The [source-scope clarification](../ledger/Yin_L_A0017_v1.md#source-scope-correction) distinguishes this BGVM20 index theorem from the positive-weight BBGSS23 product interface.
The related finite vertex-edge product for the logarithmic potential exhibits a mechanism for signed local orders.
The full embedded-atom theorem uses the accepted BGVM20 interface; the BBGSS23 product proof sketch is not a replacement for it.

This differs from [S_A0005](Yin_S_A0005.md): the intended arithmetic comes from a geometric index and cancellation of local resolvent factors, rather than atom transfer between two amalgamated vertex algebras.
It also differs from [S_A0003](Yin_S_A0003.md), since no approximation by integer-rank groups is assumed.
The present tree model has a free deck group and supplies no new Atiyah class.

## Missing bridge

The [completed commutation pilot](../ledger/Yin_L_A0016_v1.md) gives the exact correction through a four-dimensional nonbacktracking operator determinant and its logarithmic derivative.
Its root-deletion calculation identifies the off-diagonal cavity transport lost by the tree model.
The actual lattice resolvent is elliptic, and a logarithmic spectral-edge singularity [excludes every finite fixed-power product of algebraic factors](../ledger/Yin_L_A0016_v1.md#boundary-residues-and-failure-of-an-algebraic-cavity-repair) as the full correction.
The stronger finite algebraic-factor target is therefore unavailable even in this elementary commutation case.

The same pilot proves zero atom residues directly, despite logarithmic divergences and a zero reciprocal boundary value with infinite slope.
It separates transcendental continuous corrections from atomic corrections, without producing a new Atiyah group class.

For general matrix pencils, the missing input is a relation-compatible estimate or index formula for the atomic part of the correction.
A trace of an arbitrary projection, or an assumed integer nullity of the correction operator, does not supply that input.
The four-dimensional correction still has entries in the actual group algebra; its finite size does not remove the rank problem.
BGVM20 already permits complex Hermitian scalar weights and gives a finite-graph multiplicity lower bound for unitary twists.
An exact formula for general complex matrix pencils remains a separate extension.

## Selected literature mechanisms

The [first-return operator identities](../ledger/Yin_L_A0017_v1.md#first-return-functions) preserve matrix amplitudes and split across an actual overlap with no direct exterior coupling.
The [mass-transport formula](../ledger/Yin_L_A0017_v1.md#mass-transport-atoms) is an atom-only index on trees; extending it requires both a cycle correction and arithmetic beyond expected counts.
The [finite-support free-resolution formula](../ledger/Yin_L_A0017_v1.md#finite-support-euler) is an independent integer Euler certificate when its growth and module hypotheses hold.
Its amenable kernel-localization component reuses C_A0001 rather than establishing new coverage.

The [decoration benchmark](../ledger/Yin_L_A0017_v1.md#decoration-and-invisible-modes) has a nonzero matrix atom that the attachment-root Green function misses.
Matching-measure formulas on cyclic graphs concern a different law, and [general positive-power spectral-tail control is false even for torsion-free groups](../ledger/Yin_L_A0017_v1.md#regularity-obstructions).

## Embedded-atom calculation and geometric certificate

The [variable-coupling model](../claims/Yin_C_A0004_v1.md#statement) computes the complete one-cell Green matrix and first-return matrix for two couplings \(1-u\) over \(\mathbb Z^2\), with base \(v+v^{-1}\).
Its normalized zero atom is \(1/3\), carried by the antisymmetric leaf channel.
The complementary continuous density diverges as \(|x|^{-1/2}\), while the symmetric Green function diverges as \(\eta^{-1/2}\) with zero atom residue.
The [complete matrix boundary calculation](../claims/Yin_C_A0004_v1.md#boundary-asymptotics) retains a nonzero off-diagonal return term and distinguishes strong operator residue convergence from operator-norm convergence.

The [geometric extension](../claims/Yin_C_A0004_v1.md#geometric-integer-certificate) reuses the actual regular-transport theorem of C_A0003.
If every component of a finite labelled graph has a nonidentity closed-walk transport, its incidence operator \(D\) is injective, and \(\begin{pmatrix}A&D^*\\D&0\end{pmatrix}\) has unnormalized zero atom \(E-N\) for every selfadjoint base \(A\).
This gives an independently checkable sufficient condition with no spectral gap, amenability or commutation hypothesis.
The [free-group example](../claims/Yin_C_A0004_v1.md#noncompact-edge-modes) also shows that the atom need not be generated by finitely supported modes.
These are structured operator families, not a new Atiyah group class.

## Next discriminating investigation

The [distinct-coupling comparison](../claims/Yin_C_A0004_v2.md#statement) now supplies both complete cell return matrices and the two actual nonlocal zero projections.
Their cell residues have rank two and trace one, with eigenvalues \(1/\pi,1-1/\pi\) on the lattice and \(1/3,2/3\) on the free group.
The [coefficient sum rule](../claims/Yin_C_A0004_v2.md#projection-locality-and-index) identifies the failure of local idempotence with the full off-cell squared coefficient mass.
The lattice has one-sided continuous accumulation and logarithmic Green corrections, while the free atom has a gap and an analytic complement.
Finite-support generation and regularity of the orthogonal projection are distinct: the lattice has compact generating cycles but no continuous projection symbol, while the free tree has no compact kernel vectors but does have norm-convergent finite-propagation projection approximations.

The [collective-holonomy condition](../claims/Yin_C_A0004_v2.md#collective-holonomy-condition) replaces individual infinite-order transports by an infinite subgroup generated by all loop labels.
The [factored edge-block condition](../claims/Yin_C_A0004_v2.md#gap-and-deformation-conditions) preserves the same projection for interactions \(DC_0D^*\) when \(I-AC_0\) is independently injective, for example under \(\|A\|\|C_0\|<1\).
These conditions do not reduce arbitrary group-ring kernels to the certified form.

The [signed-edge calculation](../claims/Yin_C_A0004_v3.md#statement) now reduces that perturbation to the exact scalar Schur operator \([u+u^{-1}+(\varepsilon-1)(v+v^{-1})]/\varepsilon\).
For every nonzero \(\varepsilon\), both comparison models lose the entire zero atom, and zero remains in continuous spectrum.
The lattice has a logarithmic density singularity at \(\varepsilon=2\); the free model has a finite positive zero density for every fixed nonzero parameter.
The [complete boundary formulas](../claims/Yin_C_A0004_v3.md#lattice-critical-boundary) and [free-tree formulas](../claims/Yin_C_A0004_v3.md#free-density-and-residues) separate fixed-parameter atom exclusion from the singular concentration as \(\varepsilon\to0\).

The [finite-layer recurrence certificate](../claims/Yin_C_A0004_v3.md#height-layer-certificate) proves injectivity from boundedly invertible outer coefficients, with no amenability assumption.
The [primary-checked Lin92 criterion](../claims/Yin_C_A0004_v3.md#ordered-quotient-source) extends the scalar mechanism to an injective least coefficient over a right-orderable quotient.
In particular, the displayed scalar family has zero kernel whenever its torsion-free two-generator subgroup admits a nonzero map to \(\mathbb Z\).
The [torsion obstruction](../claims/Yin_C_A0004_v3.md#holonomy-obstruction) shows that infinite collective holonomy alone cannot retain the earlier integer index after signed edge potentials.

The [rank-one height model](../claims/Yin_C_A0005_v1.md#statement) now specifies both extremes as \(\operatorname{diag}(1,0)\) and the full middle block as \(\left(\begin{smallmatrix}a&b\\b^*&c\end{smallmatrix}\right)\).
Its [finite-section formula](../claims/Yin_C_A0005_v1.md#finite-section-formula) has exact normalized-kernel limit with error at most \(2/m\), but retains von Neumann dimensions over the coefficient group.
The [singular-middle reduction](../claims/Yin_C_A0005_v1.md#singular-middle-reduction) separates the common kernel of \(b,c\) from an actual compressed height operator.
The [transport condition](../claims/Yin_C_A0005_v1.md#compressed-transport-certificate) bounds that remaining nullity by the overlap defect \(p\wedge\sigma^{-1}(1-p)\), and gives the exact common-kernel dimension when this defect vanishes.
The bounded finite-layer proof and the affiliated extension have separate domain hypotheses.

The [finite-orbit formula](../claims/Yin_C_A0005_v1.md#projection-middle-and-finite-orbits) computes the remaining term through finite Dirichlet paths, with odd paths contributing at zero potential.
The [same-rank comparison](../claims/Yin_C_A0005_v1.md#same-ranks-different-transport) has kernel dimensions \(1/2\) and \(3/4\) solely from changing the transport action; both groups have torsion.
The [coupled residual family](../claims/Yin_C_A0005_v1.md#coupled-residual-and-energy) still contains any selfadjoint scalar coefficient-group kernel, while positive transport energy supplies a separately certified geometric subclass.
These results reuse the matrix-valued graded criterion in L_A0007 and the singular-coefficient rank bound in L_A0008; they do not import a matrix version of Lin92 or establish a new Atiyah group class.

The [infinite commuting-orbit formula](../claims/Yin_C_A0005_v2.md#statement) now identifies the residual nullity exactly as the sum of traces of odd finite-path start projections.
The [complete component decomposition](../claims/Yin_C_A0005_v2.md#finite-starts-and-the-missing-infinite-components) eliminates half-infinite starts by finite invariant trace and retains an injective all-open component.
The [actual kernel and residual law](../claims/Yin_C_A0005_v2.md#actual-projections-and-boundary-residues) include the global graph Gram inverse, the arcsine remainder, path eigenvalue accumulation and exact zero residues.
The atom truncation error is bounded by the finite-path mass divided by \(L+1\).
The [LNW08 comparison](../claims/Yin_C_A0005_v2.md#source-comparison-and-continuation-boundary) attributes the arbitrary-parameter lamplighter construction at its inspected source scope.

The [torsion-free von Neumann realization](../claims/Yin_C_A0005_v2.md#torsion-free-realization-in-the-von-neumann-algebra) has arbitrary Bernoulli weights and nullity \(2\theta/(1+\theta)\), but its nontrivial scalar projection is not a group-ring element.
The [group-ring comparison](../claims/Yin_C_A0005_v2.md#exact-group-ring-admissibility-and-its-limitations) gives genuine finite-lamp fractional models with torsion and isolates the conditional scalar-projection premise for general torsion-free coefficient groups.
The [Boolean trace criterion](../claims/Yin_C_A0005_v2.md#a-trace-lower-bound-forces-a-finite-boolean-orbit) shows that a uniform positive lower bound for every nonzero finite Boolean intersection forces a finite orbit; integer individual ranks alone do not suffice.
For torsion-free abelian coefficient groups, actual group-ring matrix projections satisfy that lower bound.
The stronger [augmentation rigidity](../claims/Yin_C_A0005_v2.md#augmentation-rigidity-for-abelian-group-ring-matrix-projections) makes an entrywise group-automorphism orbit stationary already from adjacent commutation.
Its enlarged zero-potential block model has exact kernel projection \(\operatorname{diag}(0,P)\) and dimension \(\operatorname{rank}\varepsilon(P)\).

The [finite abelian coefficient theorem](../claims/Yin_C_A0005_v3.md#statement) now starts with an arbitrary finite matrix \(A\) over a torsion-free abelian coefficient group, derives its actual rational kernel projection, and treats the middle block \(A^*A\).
If all transported projections commute, every nonzero finite Boolean intersection has positive integer unnormalized trace, the transport orbit has period at most \(2^d\), and the complete path formula has integer nullity between zero and \(d\).
This uses generic Laurent-field rank and actual affiliated congruence, not augmentation of the spectral projection.
The [explicit two-cycle](../claims/Yin_C_A0005_v3.md#actual-spectral-projection-and-its-two-cycle) has \(\sigma(p)=I_2-p\), trace one, and no Laurent-polynomial representative; its genuine four-square group-ring matrix has nullity two.
Thus rational spectral projections derived from finite coefficients can have nonstationary commuting transport, even though the earlier group-ring projections are rigid.
The selected [independent review](../audits/reviews/Yin_R_A0018_v3.md#finding-rational-kernel-transport) covers the whole theorem, actual inverses, matrix-path amplification, explicit full kernel projection and known-coverage boundary.
All groups in that theorem are already covered torsion-free abelian-by-cyclic groups.

The [noncommuting rank-two theorem](../claims/Yin_C_A0005_v4.md#statement) now treats rational kernel projections of trace two with rank-one forward hopping over the same independently embedded abelian coefficient field.
Its complete residual kernel is exactly \(\ker(ptp|_p)\cap\ker(pt^{-1}p|_p)\), so its nullity is zero or one even though each individual defect has trace one.
The [rational frame dichotomy](../claims/Yin_C_A0005_v4.md#rational-frame-proof-and-independently-admissible-pivots) reduces every such case either to an invertible saddle with a certified field-unit off-diagonal or to a zero channel and an independently invertible graded scalar channel.
The [finite eight-coordinate example](../claims/Yin_C_A0005_v4.md#a-finite-group-ring-witness-with-genuinely-noncommuting-transport) has genuinely noncommuting transport, positive individual defects and a nonzero compressed residual, but that residual is boundedly invertible by an explicit cyclic saddle.
Its complete kernel projection is \(\operatorname{diag}(0,p)\) with nullity two, and its group is virtually abelian.
The selected [independent whole-artifact review](../audits/reviews/Yin_R_A0018_v4.md#finding-rank-two-noncommuting-transport) covers the actual frame/domain reasoning, exact projection equality and complete example.
This exhausts the rank-two zero-potential alternatives at the stated rational-field interface; another example within that interface would not supply a new mechanism.

Next, require an explicitly changed interface before further example construction: a nonzero compressed potential, higher kernel rank with additional geometric structure, or actual coefficient projections whose arithmetic is certified without assuming the entire coefficient closure is a division ring.
Specify the finite input, residual equations and overlap corrections and screen the old saddle, graded and coefficient-division reductions before investing in a new index.
For commuting transport over a different coefficient group, identify an independent arithmetic constraint on the actual intersections; assuming its whole rational closure is a division ring merely imports the coefficient Atiyah premise.
Separate spectral projections outside the group ring from actual group-ring projections, and preserve the entrywise-action hypothesis of the augmentation certificate.
The actual overlap defect and its remaining equations must be retained; an unexplained scalar kernel trace or an assumed integer weight cannot close the argument.
For the two-generator scalar family, a group with finite abelianization is a separate unresolved calibration direction; first choose a concrete torsion-free relation system and compare known Atiyah coverage before investing in its spectrum.
For flat components, preserve the [explicit positive-potential cases](../claims/Yin_C_A0004_v1.md#geometric-integer-certificate) and the [unrestricted obstruction](../claims/Yin_C_A0004_v1.md#scope-and-obstruction), rather than replacing their remaining group-ring kernel question by a formal inverse.
Retain the actual trace corrections and matrix size when passing to an affine realization.

For a subsequent noncentral cyclic-amalgam or other relation family, first specify the operator and verify the condition in its canonical law.
Any claim of new coverage must first be compared with existing Atiyah theorems.
The [nonbacktracking continuation domain](../ledger/Yin_L_A0016_v1.md#a-finite-nonbacktracking-determinant-correction) is part of the obligation: the zero-atom parameter can lie outside the cycle-series convergence disk.
An identity that only re-expresses the unknown kernel trace is not a reduction.

## Normal hopping without a coefficient division assumption

The [normal compressed-hopping theorem](../claims/Yin_C_A0008_v1.md#statement) proves that \(K+K^*+\varepsilon p\) has no kernel for every nonzero real \(\varepsilon\), while its zero-potential kernel is exactly \(\ker K\).
The actual height action rotates the normal spectral measure; it supplies an atom-location constraint without imposing integer trace on the remaining zero atom.
Its [finite nine-vertex star](../claims/Yin_C_A0008_v1.md#specified-group-and-finite-regular-transport-input) works over an arbitrary torsion-free coefficient group, with finite group-ring Gram inverses and a noncommuting infinite projection orbit.
The complete eighteen-square matrices have kernel projection \(\operatorname{diag}(0,p)\) and nullity one at every nonzero potential.
At zero potential they retain exactly \(1+\dim_H\ker(1+u+v)\); no limiting argument removes that unknown term.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0023_v1.md#whole-artifact-finding) covers the entire construction and the singular inverse limit.
The coefficient-potential problem retains the compression on the common hopping kernel, every Schur correction and the actual affiliated domains.

## Noncommuting potentials and the exact defect pivot

The [coefficient-potential theorem](../claims/Yin_C_A0010_v2.md#statement) needs equality of the two hopping kernels, a weaker premise than normality.
For their common projection \(\delta\), it proves
\(\tau(\delta\wedge\ker V)\le\dim\ker(K+K^*+V)\le\tau(\ker(\delta V\delta))\).
For a semidefinite coefficient potential the complete kernel projection is exactly \(\delta\wedge\ker V\).
The [actual cyclic-energy potential](../claims/Yin_C_A0010_v2.md#an-actual-noncommuting-finite-star-potential) certifies \(\delta V\delta\) independently and resolves a finite genuinely noncommuting family, even though its residual is indefinite and fails the direct cyclic and coefficient-dominance tests.
The proof uses the already established graded and singular-coefficient rank mechanisms after the defect split; it does not create a new whole-group Atiyah theorem.
The [independent review](../audits/reviews/Yin_R_A0030_v1.md#whole-artifact-finding) covers the complete affiliated-domain chain and bounded projection formulas.
At zero potential the coefficient kernel is still present; the [cyclic inertia application](../claims/Yin_C_A0009_v2.md#consequences-for-the-retained-schur-problems) bounds its scalar trinomial trace by \(1/3\) but does not make it zero.
Further perturbations are useful only if they constrain that unchanged zero-potential defect or yield a genuinely kernel-preserving comparison.

## The full coefficient kernel inside normal transport

The [normal zero-potential encoding](../claims/Yin_C_A0011_v1.md#statement) now retains every rectangular coefficient-matrix kernel in an explicit finite group-ring family, with nullity \(m+\dim_H\ker A\).
All nonzero scalar potentials have the complete known kernel \(\operatorname{diag}(0,p)\), while the zero-potential arithmetic is equivalent to the entire A0001 contract.
The equivalence persists with nonzero normal hopping and noncommuting projection translates of exact period two.
Its [independent whole-artifact finding](../audits/reviews/Yin_R_A0035_v1.md#whole-artifact-finding) verifies the actual finite origin and the affiliated saddle calculation when the Gram inverse is unbounded.
Normality, finite orbit, bounded rational origin and known integer trace of the initial projection therefore leave the full unknown coefficient kernel intact in this family.
A positive criterion must impose an independently checkable condition that fails for this encoding; merely adding a nonzero potential cannot constrain the unchanged zero-potential limit.

## Compatible central-variable specialization

The [compatible specialization certificate](../claims/Yin_C_A0012_v1.md#statement) supplies that separating condition for \(N=H\times\mathbb Z^d\), with the action fixing \(H\) and acting on the central variables.
An independently invertible specialized row Gram at the auxiliary identity makes the actual rational overlap an affiliated unit; the specialization inverse itself may be unbounded.
The parameter proof uses countable affiliated eigenvalues, Fubini and explicit polynomial Schur realizations, with no evaluation of the canonical trace at one point.
Both hopping defects vanish, and the existing graded residual then gives the full finite kernel \(\operatorname{diag}(0,p)\) of integer trace \(n-r\) for every finite selfadjoint coefficient potential.
The [independent whole-proof finding](../audits/reviews/Yin_R_A0038_v1.md#whole-argument-finding) covers all actual inverse domains and the nonnormal, noncommuting period-three example with unbounded Gram and overlap inverses.
C_A0011 fails the specialization because its Fourier denominator vanishes there, and C_A0008's twisted free generators lack the required compatible central specialization.
No kernel-preserving reduction of arbitrary finite inputs to this certified subclass has been established.

The [generic-rank extension](../claims/Yin_C_A0012_v2.md#statement) proves that the actual integrated rank of every bounded-coefficient rectangular Laurent matrix equals the supremum of its torus-fiber ranks, attained almost everywhere.
In one variable the exceptional set is countable and its total rank-loss mass is at most the Laurent degree width times the generic rank.
The rational extension uses only the specified syntax's actual defined inverse gates.
The [independent whole-proof finding](../audits/reviews/Yin_R_A0038_v2.md#whole-proof-finding) checks the corner, companion, rational-domain and finite-kernel interfaces.
These analytic constraints do not supply arithmetic for the loss at one exceptional fiber.
For arbitrary \(A\), the finite compatible family \(M(x)=(A^*A+(1+x)I\ \ 0)\) has certified generic support and gives an integer-nullity matrix, while its action-compatible specialization \(x=-1\) adds exactly \(\dim\ker A\) to that nullity.
The specialized inverse gate fails precisely when that kernel is nonzero, even though the generic projection has a constant rational representative.
Any attempted transfer back from a certified generic family must therefore control the original fiber's rank loss, not evaluate that simplified representative as though it remained the specialized kernel projection.

The [symmetric singular-fiber construction](../claims/Yin_C_A0012_v3.md#statement) strengthens this obstruction with a degree-minimal pencil having invertible outer coefficients, prescribed regular endpoint values and one transitive exceptional orbit.
Its generic rank, every local contour count and the bounded-unit homotopy on every nonsingular loop are independent of the arbitrary input matrix A, while each exceptional defect is \(r+\dim\ker A\).
The exact discrepancy between the global contour count and the total geometric loss is \(q\operatorname{rk}(A)\).
Even the scalar examples A = 0 and A = 1 have the same stated data and different geometric defects, refuting contour-count equality and forced saturation.
Positive selfadjoint finite inputs and the actual compatible transport realization retain these defects; a genuine inversion action also preserves the entire singular orbit through an explicit two-coordinate representation.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0038_v3.md#whole-artifact-finding) verifies all finite kernels, contour calculations, group relations and trace normalizations.
Thus an additional exact geometric formula must control the explicit correction independently; if it supplies only an integer total over an orbit, divisibility by the orbit size is a further obligation.
Further repetitions of that orbit or nonsingular-loop invariants alone do not advance the original arbitrary-matrix problem.
The next candidate must specify an original-input property that excludes this encoding for a proved reason, or preserve the original kernel through the singular comparison.

The [bounded transverse theorem](../claims/Yin_C_A0012_v4.md#statement) now supplies an exact contour idempotent under a bounded semisimple split and invertible compressed derivative.
Its range is the geometric kernel and its finite trace is exactly the kernel dimension, with no integer-valued conclusion supplied by analyticity.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0038_v4.md#whole-artifact-finding) checks the nonorthogonal corners, actual residue, countertests, finite transport, C*-membership and original Kato interface.
For \(F_A(z)=A^*A+(1-z)I\), the first missing premise is a genuine complementary spectral gap; even the finite input \(A=\operatorname{diag}(0,1-u)\) over an infinite cyclic group fails it.
Under that gap the contour is the original kernel projection in the reduced group C*-algebra, so integer trace of this actual projection is the next independent obligation.
Polynomial functional calculus vanishing at zero and identity stabilization followed by bounded invertible multipliers cannot repair a nongapped input while preserving its kernel in the stated classes.
The theorem therefore removes the contour-versus-geometric correction on a precise subclass and rules out several proposed gap repairs, while leaving both general-input coverage and projection arithmetic unresolved.

The [quantitative central-gap obstruction](../claims/Yin_C_A0012_v5.md#statement) now excludes every finite central Laurent construction with a positive excess of specialized nullity over generic nullity.
For excess delta at a fiber and angular Lipschitz bound L, the integrated positive singular-value mass below epsilon is at least \(\delta\min(\pi,\epsilon/L)/\pi\).
Thus it has no complementary spectral gap, independently of the number of auxiliary blocks or their noncommutative coefficient group.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0038_v5.md#whole-artifact-finding) verifies the strict perturbation estimate, exact rectangular trace, generic-rank premise and Haar integration.
The explicit free-group boundary augmentation preserves the original kernel dimension but has a gap exactly when the input already has one.
Consequently nonamenability of the auxiliary group alone cannot regularize this construction.
Further work on a gap-producing transformation must exhibit its actual kernel relation and explain which central specialization hypothesis fails; repeating a compatible finite block construction is excluded by this theorem.
The separate problem of integer trace for a genuinely obtained projection remains open even after that analytic obstacle is bypassed.

## Relation to the return-word route

The [return-word arithmetic route](Yin_S_A0007.md) keeps the whole primitive-cycle series and seeks local-exponent rigidity from its labelled structure.
This route seeks a finite geometric index formula.
The completed pilot changes the target to an index for the atomic part, without requiring a finite algebraic formula for the whole transform.
They can exchange exact correction identities, but neither is a premise for the other.
