---
author: Yin
---
# Independent review of the Promislow projection-specialization obstruction

Review act: 2026-11-11T17:55Z.
The responsible human record author is Yin.
This is an initial independent whole-artifact mathematical review of [L_A0024, physical v1](../../ledger/Yin_L_A0024_v1.md), in its working-tree revision read on 2026-11-11 UTC.
The reviewer was outside substantive proof development and received the fixed candidate, necessary fixed source locators, requested scope and operational rules.
No development draft, proof-generation dialogue, proposing-agent mathematical summary or earlier project-review conclusion was supplied or consulted.
The reviewer enumerated the obligations from the candidate's precise conclusion, inspected the candidate and necessary fixed dependencies, and derived the findings below without relying on earlier R findings.
This review does not assess completion of T_A0001.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete candidate](../../ledger/Yin_L_A0024_v1.md) | All mathematical assertions and all displayed equations, including the bounded conclusion and explicit nonconclusions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Setting and proposed test](../../ledger/Yin_L_A0024_v1.md#fixed-setting-and-proposed-test) | Actual group, coset convention, rational projection construction, rank and trace interface. |
| [Whole-artifact finding](#whole-artifact-finding) | [Left and right matrices](../../ledger/Yin_L_A0024_v1.md#the-actual-left-matrices-and-right-semilinear-symmetries) | Equations (1)--(9), conjugation actions, order of right composition, square cocycles and projection covariance. |
| [Whole-artifact finding](#whole-artifact-finding) | [Specialization preservation](../../ledger/Yin_L_A0024_v1.md#what-coordinate-specialization-really-preserves) | Removability, rank, selfadjointness, boundedness and covariance under successive coordinate specializations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Rank-two counterexamples](../../ledger/Yin_L_A0024_v1.md#a-rank-two-counterexample-to-the-surviving-symmetry-inference) | Equations (11)--(13), the torsion quotient interpretation, all three initial coordinates, both fixed signs and subsequent specializations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact remaining constraint](../../ledger/Yin_L_A0024_v1.md#exact-remaining-constraint-and-conclusion) | Equation (14), the precise failed inference, comparison with index-two parity, square-root extensions and unresolved original liftability. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0010 group source interface](../../ledger/Yin_L_A0010_v1.md#group-and-selected-pencil) | Only the presentation and Gar21-derived torsion-free, normal-subgroup, index, action and cocycle facts used here; not its scalar-pencil investigation. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0010 actual representation](../../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model) | Actual regular four-coset representation, unnormalized matrix trace and factor one quarter. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0022 rational lemma](../../ledger/Yin_L_A0022_v1.md#a-rational-projection-lemma) | Removable-pole and rank-preservation arguments, and the exact two-symmetry mechanism used for comparison. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0022 Gram construction](../../ledger/Yin_L_A0022_v1.md#producing-the-rational-orthogonal-kernel-projection) | Rational orthogonal kernel projection construction and its extension from two independent torus variables to three. |

## Obligations and checked interfaces

The conclusion to be checked is a failure of a specific proposed inference after specialization.
It requires a legitimate specialization of every original rational orthogonal projection under consideration, and an explicit specialized projection satisfying every retained condition while having rank two.
It does not require an original group-ring matrix with a fractional kernel dimension.
The following checks cover both sides of that distinction.

### Source facts and actual trace

I directly inspected [Gar21, arXiv v4, Section 3.1, pp. 4--5](../../literature/pdf/Gar21--arxiv-v4.pdf#page=4).
The source uses right conjugation and the section with image \(1,a,b,ab\).
Its amalgam of Klein bottle groups identifies the normal \(\mathbb Z^2\) subgroup and the infinite-dihedral quotient, then identifies the kernel of the quotient onto \(C_2^2\) as the free abelian group on \(a^2,b^2,(ab)^2\).
I checked the displayed action on these three generators and the passage deriving the cocycle.
The source's torsion-freeness argument uses the standard fact that finite-order elements in an amalgam are conjugate into a factor; that foundational theorem was accepted at its stated application, rather than re-proved in this review.
No unit-conjecture construction or division conclusion in Gar21 is used.

The right-coefficient basis means that left multiplication has entry \(r^{-1}gs\) when \(gs\in rN\).
This reconstructs the candidate's matrices \(A\) and \(B\) from the source action and cocycle and matches L_A0010.
The unitary identification of \(\ell^2(P)\) with four copies of \(\ell^2(N)\) is an actual regular-representation identification.
For a group element, the sum of the four coefficient-of-identity diagonal traces is four at the identity and zero otherwise.
Normality extends this identity to the group von Neumann algebra and its matrix kernel projections.
Consequently, for domain size \(n\), the group dimension is one quarter of the integrated ordinary \(4n\)-dimensional matrix trace, with no extra division by \(n\).

The extension of the Gram construction from L_A0022 to \(\mathbb C(x,y,z)\) is valid.
A nonzero Laurent polynomial has a torus zero set of Haar measure zero by induction and Fubini.
A rational field basis of the kernel therefore evaluates to an independent basis of the actual kernel on a common full-measure set.
Its Hermitian Gram matrix is positive definite there, so its determinant is a nonzero rational function.
The resulting rational projection has generic rank \(d\), and its integrated trace is \(d\).
This proves the stated original-group trace \(d/4\) without an Atiyah or division premise.

### Left matrices, semilinear order and cocycles

Direct multiplication verifies \(A^2\), \(B^2\), \(AB\) and \((AB)^2\) as displayed.
Each matrix is monomial with torus-modulus-one entries, so its stated unitarity holds.
For right multiplication, \(rna=(ra)(a^{-1}na)\) supplies \(\sigma_a\), and the analogous identity supplies \(\sigma_b\).
The source cocycle, converted from left coefficients to right coefficients using its action, gives both \(ba=ab\,xy^{-1}z^{-1}\) and \(aba=b\,y^{-1}z^{-1}\).
These give the stated \(C_a\); the columns of \(C_b\) follow from right multiplication by \(b\).

The order for the right action by \(ab\) is first right multiplication by \(a\), then by \(b\).
Thus the linear coefficient of the composite is
\[
 C_{ab}=C_b\sigma_b(C_a)
 =
 \begin{pmatrix}
 0&0&0&z\\
 0&0&x^{-1}z&0\\
 0&x^{-1}&0&0\\
 1&0&0&0
 \end{pmatrix},
 \qquad
 \sigma_{ab}(x,y,z)=(x^{-1},y^{-1},z).
\]
Multiplication verifies the three scalar squares \(xI\), \(yI\), \(zI\).
The covariance identities are identities of maps with the correct input and output dimensions.
They hold for the left generators, hence their inverses, products and finite linear combinations, and therefore for every group-ring matrix.

On a common generic torus set, these semilinear maps identify the kernel at the transformed parameter with the kernel at the original parameter through a unitary matrix.
Uniqueness of the orthogonal projection gives (9).
The exceptional sets remain null under the parameter automorphisms, so equality almost everywhere is sufficient to give the rational identities.
No fiberwise arbitrary change of representation is being substituted for actual right translation.

### Removability and successive rank preservation

For an entry with a putative pole along \(y=1\), write it over \(\mathbb C(x,z)\) as \((y-1)^{-k}h\), where \(k>0\), \(h\) is regular at one and \(h(x,1,z)\ne0\).
Outside a measure-zero parameter set in \((x,z)\), that leading coefficient is finite and nonzero and the residual denominator remains nonzero near \(y=1\).
Fubini supplies such a pair for which the original bound also holds for almost every \(y\).
The pole would violate the bound on a positive-measure circle arc.
This proves regularity over the parameter field, with no need to claim joint continuity at every point of the full divisor.

Specialization preserves the idempotent identity and the integer trace.
An idempotent over any of these characteristic-zero fields has rank equal to its trace, so the rank remains exactly \(d\).
The torus involution preserves the specialization divisor and descends to the remaining variables, which preserves selfadjointness.
Thus the specialized rational idempotent again gives orthogonal projections almost everywhere and has the same entry bounds.
Both parameter automorphisms preserve \(y=1\), and their monomial coefficients remain invertible, so both complete covariance identities descend.

This argument applies again to each remaining variable.
It also applies to a first coordinate equal to \(-1\), since inversion fixes both signs and the same pole argument works at either point.
It covers rank zero and full rank without a separate generic-invertibility assumption.
It preserves the rank of the already constructed projection; it does not identify that projection with the kernel projection of a specialized original matrix.

### Counterexamples, all coordinates and all signs

At \(y=1\), \(B_y\) is a unitary involution with trace zero.
Hence \(E_y=(I+B_y)/2\) is selfadjoint, idempotent and rank two over \(\mathbb C(x,z)\).
Its entries are Laurent polynomials, so there are no poles at any further torus specialization.
Covariance follows by applying the already checked left/right commutation identities to \(B\), then specializing and taking the indicated affine combination.
The identity matrix has the same covariance, and the parameter automorphisms fix the scalar coefficients.
Consequently the example satisfies both generator covariances and all their word and inverse consequences, with the actual specialized cocycle still present.

The subgroup \(\langle y\rangle\) is normal, since conjugation by the generators preserves it.
It is a direct summand of \(N\), so the quotient has \(N/\langle y\rangle\cong\mathbb Z^2\) of index four.
The image of \(b\) is outside that subgroup and has square one, hence is a nonidentity involution.
The specialized matrices are the actual four-coset matrices for this quotient.
Its averaging projection is the kernel projection of \(1-b\), and its trace is \(2/4=1/2\).
This is a statement about the torsion quotient, with no original-group kernel projection constructed.

The same checks apply to \(A\) at \(x=1\) and \(AB\) at \(z=1\).
For either sign \(\varepsilon\), the corresponding specialized matrix \(G\) satisfies \(G^2=\varepsilon I\) and \(G^*=G^{-1}\).
For a constant \(\mu\) with \(\mu^2=\varepsilon\) and \(|\mu|=1\), the matrix \(\mu^{-1}G\) is a selfadjoint involution with trace zero.
Therefore \((I+\mu^{-1}G)/2\) again has rank two and every descended covariance.
This covers both choices of square root as well as all three coordinate choices.
For \(\varepsilon=-1\), this is a matrix specialization argument; it is not being interpreted as the ordinary quotient obtained by killing a translation.

The polynomial identities persist under every later allowed coordinate substitution and the trace stays two.
The final matrix (13) is obtained directly from \(B_y\), and its commutation with both surviving permutation matrices is correct.

### Lost information and comparison

Equation (14) is the exact idempotency defect of the displayed unspecialized expression.
It identifies a concrete square-translation condition that vanished, without proving that every possible lift fails.
The existence of the specialized example alone cannot show that it is the specialization of an original equivariant rational projection.
The candidate consistently keeps that question separate.

The comparison with L_A0022 is valid at the stated scope.
There the useful specialization leaves a free parameter and a second automorphism exchanges the two constant eigenspaces, forcing equal ranks.
Here the common fixed set of the two original parameter actions consists of the eight sign triples.
Already one coordinate specialization admits the displayed rank-two projection despite the other two free parameters and the full surviving covariance.
Extending the coefficient field by square roots cannot eliminate an explicit projection over the original smaller field merely by extending those same equations.
Every compatible lifted parameter automorphism acts on its original-field entries as before, and deck automorphisms fix them.
Additional restrictions involving the original unspecialized family would be new input, rather than consequences of the descended equations alone.

For the contextual statement of already known group-class coverage, I checked the exact hypotheses retained in [Lin93's group-class and theorem account](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems).
The checked group source supplies torsion-freeness, and being abelian-by-finite makes the Promislow group elementary amenable.
Thus the existing coverage statement is applicable.
The proof of Linnell's theorem is not re-audited or used as a premise for the obstruction established here.

## Verification facts and limits

The review consists of the direct mathematical checks above and inspection of the stated fixed source interfaces.
An auxiliary one-time Laurent-polynomial diagnostic also verified the original left and right unitaries, all three scalar square identities, covariance of \(A,B,AB\) with all three right operators, all six signed first-coordinate projection families, and their 24 further signed endpoint specializations.
Its coefficients were integral or dyadic Gaussian values, so these checks involved exact arithmetic on the displayed finite expressions rather than approximate torus sampling.
The diagnostic corroborates those algebraic calculations and does not prove the measure, trace, source-applicability or lifting assertions.
The decisive identities and arguments are retained in the fixed candidate and this review; no continuing computation depends on a temporary program.
No proof-assistant verification was performed.

## Whole-artifact finding

No mathematical gap was found in the inspected fixed candidate.
Its complete bounded conclusion is supported: rationality, projection bounds, all descended right-translation covariances and their surviving cocycle identities do not force rank divisible by four after any of the specified initial coordinate specializations.
The explicit rank-two families establish this failure already after the first specialization.

The original faithful trace factor and rank preservation of an actual original projection remain valid.
This finding does not assert that the counterexample lifts to an original rational equivariant projection, does not construct a fractional original-group kernel dimension, and does not refute the Atiyah conclusion.
It does not establish a new group-class theorem, discharge the remaining noncommutative specialization problem, or complete T_A0001.
