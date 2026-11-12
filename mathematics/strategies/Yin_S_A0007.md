---
author: Yin
---
# Return-word determinants and local exponent rigidity

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Seek integer atom residues from torsion-free primitive return words and their multivariate determinant series, retaining arbitrary complex coefficients. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Seek an invariant for actual infinite-dimensional coefficient rings with a proved kernel back-transfer; a faithful central-finite algebra model forces virtual abelianness and cannot extend the completed Promislow certificate to a new group class. |

## Mechanism and actual input

For a finite matrix over a group ring, use the unnormalized trace to form the exponential return series
\[
D_A(t)=\exp\left(-\sum_{j\ge1}
  (\operatorname{Tr}_n\otimes\tau_G)(A^j)\frac{t^j}{j}\right).
\]
The [torsion-free cycle calculation](../ledger/Yin_L_A0015_v1.md#torsion-free-cycle-arithmetic-and-its-obstruction) gives an Euler product over primitive closed labelled index paths.
Torsion-freeness enters at an actual step: if a repeated closed path has identity group label, its primitive root also has identity label.
Keeping the edge coefficients as independent variables retains an identity over their integer polynomial ring.

The source basis is Kontsevich's scalar product for arbitrary torsion-free groups and the Kassel--Reutenauer cyclic-series matrix construction, at the exact checked scope in L_A0015.
Their free-group algebraicity results are not asserted for general groups.
For a positive contraction obtained from \(A^*A\), the [logarithmic boundary exponent](../ledger/Yin_L_A0015_v1.md#logarithmic-slopes-and-return-amplitudes) is exactly the original unnormalized kernel dimension.

This differs from scalar rational-pivot methods, approximation by other groups and amalgamated atom transport.
Its proposed new information is the canonical word structure and its primitive-root constraint.

## Refuted shortcuts and remaining obligation

Integer Taylor coefficients do not force integer local exponents.
The [explicit probability-law test](../ledger/Yin_L_A0015_v1.md#torsion-free-cycle-arithmetic-and-its-obstruction) has a rational Cauchy transform and determinant series \(\sqrt{1-4t}\) with integer coefficients, yet atom mass one half.
Algebraicity alone also permits fractional exponents.
A finite list of return moments supplies neither a boundary limit nor its arithmetic.
The [commutation investigation](../ledger/Yin_L_A0016_v1.md#even-cyclic-root-closure-and-positive-moments-do-not-suffice) strengthens the obstruction to an actual cyclic root-closed language with nonnegative integer primitive counts and a positive aggregate spectral law having an atom of mass one half.
That language cannot be the identity language of any group; full group multiplication and unitary joint-distribution compatibility are not implied by those weaker properties.

The missing theorem must use more of the actual labelled cyclic structure than those generic properties.
It must control the relevant real boundary exponent even when continuous spectrum accumulates at the atom.
An ordinary argument-principle proof requiring a meromorphic continuation is not available in general.

The full Task allows arbitrary complex coefficients.
An integer-coefficient theorem alone is therefore insufficient.
The multivariate identity preserves coefficient dependence formally, but a valid passage to every complex specialization requires an additional argument.

## Exact commutation feedback

The [primitive correction product](../ledger/Yin_L_A0016_v1.md#primitive-returns-and-their-critical-growth) consists exactly of the new return words created by commutation.
Its nonbacktracking resummation is the exact four-dimensional determinant correction to the tree vertex-edge formula.
The actual critical cycle growth yields a positive product value and zero power exponent, while the generic fractional-law product has different critical growth.
These are relation-specific facts, not a theorem that integer cycle multiplicities force integer residues.

## Next discriminating investigation

The [positive-definite word-kernel test](../ledger/Yin_L_A0017_v1.md#positive-definite-word-kernels) makes one missing compatibility condition explicit: normalized zero-one positive-definite functions are subgroup indicators, and conjugation invariance and root closure recover torsion-free quotient data.
This rejects false group-like languages but does not by itself prove residue quantization.
The [completed central-winding calculation](../ledger/Yin_L_A0019_v1.md#a-full-joint-trace-identity-not-just-a-scalar-moment-fit) gives the actual full-word trace disintegration for \(\langle a,b\mid a^p=b^q\rangle\) and passes rigorously to atom masses by bounded spectral functions.
For the scalar weighted adjacency family, almost every cyclic free-product fiber is atomless by the strict free atom threshold, so the original torsion-free law is atomless.
The [mixed-power example](../ledger/Yin_L_A0019_v1.md#the-mixed-power-test-and-its-fractional-quotient-atoms) has fractional quotient atoms and even an entirely atomic exceptional fiber, none of which survives the Haar integral.
This rules out quotient-atom persistence or winding specialization as substitutes for the actual canonical trace.
Its [scalar conclusion is already covered by grading](../ledger/Yin_L_A0019_v1.md#known-coverage-and-what-this-test-does-not-establish); continuing the same scalar calibration would duplicate that resolved case.
The joint trace identity extends to selfadjoint matrix inputs, but the scalar free-atom threshold supplies no matrix trace quantization.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0021_v1.md#whole-artifact-finding) checks the complete normal form, joint trace, boundary passage, exceptional fibers, coefficient degeneracies and height-coverage comparison at their stated source scope.
The [non-D-finiteness and slow-tail theorems](../ledger/Yin_L_A0017_v1.md#regularity-obstructions) exclude universal differential-equation and positive-power asymptotic targets.

The [matrix winding calculation](../ledger/Yin_L_A0022_v1.md#a-rational-projection-lemma) supplies an independent parity constraint in the actual index-two \(G_{2,2}\) model.
Boundedness removes a rational kernel projection's pole at a reflection fixed divisor; specializing that projection preserves its rank, and the remaining symmetry pairs its two character-block ranks.
Its [analytic projection counterexample](../ledger/Yin_L_A0022_v1.md#why-finite-winding-and-monodromy-alone-still-fail) has finite winding, correct monodromy and constant trace one half, but its sign jump excludes actual rational finite input.
The [whole-artifact review](../audits/reviews/Yin_R_A0026_v1.md#whole-artifact-finding) confirms both calculations and the existing abelian-by-cyclic coverage.
The next calibration tests whether actual cocycle and projection identities retain enough information for divisibility beyond index two; merely specializing group relations may introduce quotient torsion and lose that information.

The [Promislow matrix test](../ledger/Yin_L_A0024_v1.md) derives all actual four-coset right-translation covariances and their three square cocycles.
After any first square-coordinate specialization to \(1\) or \(-1\), an explicit rank-two rational orthogonal projection satisfies every descended covariance and surviving cocycle.
The [independent finding](../audits/reviews/Yin_R_A0031_v1.md#whole-artifact-finding) confirms that the specializations preserve the rank of an original projection but discard a necessary rational liftability constraint.
At value \(1\), the counterprojection is the actual averaging projection of a newly created involution in the torsion quotient.
The next step must retain original liftability or a global invariant; the descended identities alone do not supply divisibility by four.

The [formal Promislow lift](../ledger/Yin_L_A0028_v1.md) retains every original square cocycle and right covariance, all finite jets, and a locally bounded analytic rank-two projection.
Its [whole-artifact review](../audits/reviews/Yin_R_A0037_v1.md#whole-artifact-finding) confirms both the explicit lift and the deformation that removes an additional left-commutation property.
The explicit square-root germ fails global rational descent, while a restricted global irreducibility argument gives divisibility by four only when the projection also commutes with the specified left generator.
That extra commutation is not forced by the full local equations.
The unresolved global test must therefore retain rational descent beyond finite jets and avoid assuming that extra commutation for arbitrary matrix kernels.
The [full global descent reduction](../ledger/Yin_L_A0028_v2.md) now identifies the actual covariance algebra and independently proves the coefficient division ring for the index-two subgroup.
It retains the exact non-involutive action and reduces the obstruction to two mixed rational norm equations; elementary valuations alone exclude both pure-coefficient cases without controlling addition in the mixed case.
All original determinant-line cocycles admit rational rank-two data, so determinant information cannot improve parity to divisibility by four.
Keeping exterior decomposability instead gives an explicit six-variable quadratic form over \(\mathbb C(U,V,T)\); its anisotropy is equivalent to the complete rational rank-divisibility problem for this actual group.
The [independent whole-input finding](../audits/reviews/Yin_R_A0037_v2.md#whole-input-finding) verifies both directions, all coefficient orders, the actual trace model and the comparison-only Albert-form attribution.
That reduction supplies no anisotropy proof itself; the independent global certificate below now supplies this missing step for the known Promislow class.

The [Albert-form identification](../ledger/Yin_L_A0028_v3.md#an-explicit-albert-form-identification) now gives the explicit biquaternion algebra \((U,d)\otimes(UV,e)\), with an invertible rational change of six coordinates.
The inspected Lewis theorem supplies the exact division/anisotropy equivalence for that algebra, without asserting an unproved isomorphism to the original crossed product.
The same [valued-extension calculation](../ledger/Yin_L_A0028_v3.md#every-henselian-valued-extension-with-quadratically-closed-residue-loses-anisotropy) constructs a nonzero isotropic vector in every henselian extension whose residue field has characteristic different from two and all nonzero elements square.
Its three exhaustive cases also show that an anisotropic henselian extension must preserve U as a unit with nonsquare residue.
The explicit completion vectors use square roots that do not lie in the original rational field, so this is an obstruction to those local certificates and not a rational solution.
The [independent whole-input finding](../audits/reviews/Yin_R_A0037_v3.md#whole-input-finding) checks the new calculations and their exact source interfaces.
CG23's directly relevant virtually abelian and Promislow presentation is retained as comparison: its Ore division algebra is introduced after invoking the established domain theorem, so that presentation does not independently exclude the mixed norm solutions here.

The [nonsquare-residue test](../ledger/Yin_L_A0028_v4.md) shows that preserving U as a unit with nonsquare residue still permits isotropy.
The injective change \(T=ZV\) followed by completion to \(\mathbb C(U,Z)((V))\) has an anisotropic even residue form but an explicitly isotropic odd residue form and an exact formal isotropic lift.
More generally, every extension containing a square root of \((1-V)(1-W)\) has the displayed isotropic vector; this rules out every henselian test with both \(v(V)>0\) and \(v(W)>0\) in residue characteristic different from two.
The square root is absent from the original rational field by its odd valuation at V = 1, and the constructed isotropic line does not descend.
The [independent whole-input finding](../audits/reviews/Yin_R_A0037_v4.md#whole-input-finding) checks the exact embedding, residue forms, recursion, generalized vector, non-descent and the inspected Kne09 Springer-criterion comparison.
Isotropy of the completion is the proved conclusion; hyperbolicity and rational isotropy are not asserted.
These completion failures remain valid and explain why the original rational field must be retained in the global argument.

The [global division certificate](../claims/Yin_C_A0013_v1.md#statement) now proves anisotropy over the original \(L=\mathbb C(U,V,T)\), resolving this calibration's mixed rational norm system completely.
Its explicit Brauer calculation separates the biquaternion class as \([D_0\otimes L]+[U,T^2-UV]\), with \(D_0\) defined over \(\mathbb C(U,V)\).
Rational valuation arguments prove that both constant extensions required by the inspected Siv10 criterion remain division; that criterion then makes the original class have index four.
The accepted Albert equivalence and complete actual-model back-transfer exclude every mixed rational solution, prove division of the actual Promislow crossed product and give integer kernel dimensions for all its finite complex rectangular matrices.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0037_v5.md#whole-artifact-finding) checks the calculation, original theorem, actual cocycles, exterior descent, all-size projections and trace normalization.
The proof does not invoke a known Promislow group-ring division or Atiyah theorem as a premise, but its group coverage is already known.
The local isotropic vectors above require larger fields and do not descend, consistently with this global anisotropy.
The [central-finite obstruction](../ledger/Yin_L_A0029_v1.md#a-faithful-central-finite-model-forces-virtual-abelianness) now shows that a faithful complex group-algebra embedding in an algebra finite over a central field forces virtual abelianness, by a dimension polynomial identity and the inspected Passman theorem.
This also excludes finite-input models containing a generating set and its inverses; allowing the dimension to depend on the input does not evade the obstruction.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0039_v1.md#whole-artifact-finding) verifies the source application, actual four-coset embedding, both closure comparisons and the precise faithful-model limitation.
The explicit test \(F_2\times P\), with P the Promislow group, retains an independently known coefficient division ring and the original cocycle, but free words exclude every finite central dimension and the formerly commutative norm formula acquires a nonzero commutator term.
Its full group is separately covered by Lin93, so this is a mechanism test rather than new Atiyah coverage.
An auxiliary finite-dimensional invariant without a faithful group-algebra embedding is not ruled out; it must be derived from the actual noncommutative action and have its own proved implication for original kernels or rational idempotents.
Siv10 has no supplied extension to arbitrary infinite-dimensional coefficient division algebras.
Continuation therefore requires either such an auxiliary back-transfer or a genuinely infinite-dimensional valuation or rank invariant, rather than another faithful central-finite realization.

Identify an explicit compatibility property of the full group identity language or joint unitary distribution that is absent from the constructed counterexample and can supply an independent boundary estimate.
Require a concrete matrix or noncentral relation family whose kernel gains a constraint beyond the existing cyclic, graded, energy and known division-coefficient tests.
Check that its proposed use does more than restate the original group-ring rank problem.
Preserve the distinction between positive aggregate moments and a positive-definite full joint distribution.
For the nonbacktracking determinant, justify continuation to the atom parameter rather than evaluating the cycle expansion beyond its convergence disk.

Use the [geometric index route](Yin_S_A0006.md) as a model for a finite signed atomic contribution while allowing the continuous correction to be transcendental.
A new recurrence, arithmetic condition or factorization earns further investment only when it excludes the retained fractional behavior and respects arbitrary complex coefficient specialization.
