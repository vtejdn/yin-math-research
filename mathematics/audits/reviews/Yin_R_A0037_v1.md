---
author: Yin
---
# Independent review of the formal Promislow projection lift

Review act: 2026-11-11T18:18.
The human record author is Yin.
This is a separately organized, independent mathematical review of the whole fixed [L_A0028_v1](../../ledger/Yin_L_A0028_v1.md), as read in the worktree on the stated date.
The reviewer did not participate in its substantive development and received no proof-development dialogue, mathematical summary, author explanation or previous review conclusion about this candidate.
The fixed candidate and the exact prerequisite materials identified below were read directly.
No development draft or other review of this candidate was consulted.
The findings were formed by reconstructing the arguments and multiplying the displayed sparse matrices, with direct inspection of the necessary primary-source passages.
No proof-assistant verification is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0028_v1](../../ledger/Yin_L_A0028_v1.md) | The whole formal and analytic construction, all displayed identities (1)--(19), finite-jet and nonrationality conclusions, restricted rational theorem, deformation, and stated unresolved scope. |
| [Whole-artifact finding](#whole-artifact-finding) | [Actual four-coset matrices](../../ledger/Yin_L_A0024_v1.md#the-actual-left-matrices-and-right-semilinear-symmetries) | The left matrices, coefficient involution, right semilinear matrices, composition order, covariance and square translations used by L_A0028. |
| [Whole-artifact finding](#whole-artifact-finding) | [Specialized projection](../../ledger/Yin_L_A0024_v1.md#a-rank-two-counterexample-to-the-surviving-symmetry-inference) | The exact initial projection E_y, its rank, star and descended covariance, as inputs to L_A0028. |
| [Whole-artifact finding](#whole-artifact-finding) | [Actual finite-index model](../../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model) | The actual four-coset representation and factor-four trace identity relevant to distinguishing the formal lift from an original group kernel projection; no review of unrelated L_A0010 arguments. |
| [Whole-artifact finding](#whole-artifact-finding) | [Rational Gram projection](../../ledger/Yin_L_A0022_v1.md#producing-the-rational-orthogonal-kernel-projection) | The rational kernel-projection construction and its direct three-variable use in the prerequisite model; no review of unrelated L_A0022 arguments. |

## Formal coefficient ring and projection

The substitution defining star sends \(t\) to \(-t/(1+t)\), has t-adic order one and is its own inverse.
Together with inversion of x and z and conjugation of constants, it defines precisely the extension of the original scalar involution to R.
The two automorphisms in (2) preserve R and its t-adic filtration, commute with each other and with star, and restrict to the stated original automorphisms on F.
The Laurent-expansion map from F into K((t)) is injective.
This is an algebraic embedding of coefficient fields; it is not an embedding of this formal completion into the original affiliated algebra.

The square-root recursion uses the invertible coefficient 2 at every degree and gives one root s with constant term one.
Applying star or either automorphism and comparing constant terms proves all three identities in (4), without selecting a rational square root.
With \(c:=x^{-1}z\), the nonzero entries of \(D^{-1}B\) are exactly \(s,cs,s^{-1},c^{-1}s^{-1}\) in the positions displayed in (7).
The two resulting two-dimensional blocks square to the identity and have trace zero.
The diagonal entries of D agree on each B-connected pair, so B commutes with D.
Consequently the star calculation in (8) is valid in its actual noncommutative order.

The four columns in (9) are eigenvectors with the indicated signs.
After grouping the coordinates into the two B-invariant pairs, each pair of columns has determinant a unit multiple of 2s or 2cs.
They therefore give a basis over R, proving freeness of both summands and rank two over K((t)).
Reduction at t = 0 gives exactly the E_y of the fixed prerequisite, not merely an isomorphic projection.

## Original symmetries and the actual model

The source [Gardam, arXiv:2102.11818v4, Section 3.1, pp. 4--5](../../literature/pdf/Gar21--arxiv-v4.pdf#page=4) was inspected directly.
Its normal subgroup, quotient, action and cocycle agree with the fixed basis (1,a,b,ab).
In particular, the source establishes that \(\langle a^2,b^2,(ab)^2\rangle\) is free abelian of rank three, with quotient \(C_2^2\), and gives the conjugation actions used in L_A0024.
The torsion-free assertion and its amalgam argument were also inspected there; the characteristic-two unit construction elsewhere in the source is not used.

Converting the source's left-coefficient normal forms to the right-coefficient basis gives the displayed A, B, C_a and C_b.
For example, the source commutator identity yields \(ba=ab\,xy^{-1}z^{-1}\), and the corresponding right-multiplication column is the fourth-row coefficient of \(C_a\).
The formulas retain all three independent translation variables.
Direct sparse multiplication checks \(B^2=\operatorname{diag}(y,y^{-1},y,y^{-1})\), the two generator square identities, and the original left/right commutation identities.
For the composition convention used in the candidate, \(C_{ab}:=C_b\sigma_b(C_a)\) has nonzero entries \(z,x^{-1}z,x^{-1},1\) in positions \((1,4),(2,3),(3,2),(4,1)\), respectively.
Applying sigma_ab and multiplying gives z times the identity, confirming the composition order and the third square relation.

C_a interchanges the two coordinate pairs, while C_b preserves each pair.
The transformations of s therefore give both equations (11) entry by entry.
The matrices satisfying a fixed covariance equation are closed under sums, products and inversion of invertible members.
This proves (12), and the two generator equations imply their group-word and inverse consequences.
The right matrices and automorphisms themselves are unchanged, so the original group and cocycle identities remain valid after passage to R.
No extra scalar, commuting or weakened right action was substituted.

The finite-index model is the actual unitary change of coordinates from four copies of the regular N-module to the regular P-module.
For a group element, the sum of the four diagonal coefficient traces is four when the element is the identity and zero otherwise.
Normality then gives the factor-four trace identity for the represented von Neumann algebra and its kernel projections.
The rational Gram formula in L_A0022 applies with three independent variables: a nonzero minor has a measure-zero torus zero set, and the generic Gram matrix is positive definite.
Thus an actual rational kernel projection of field rank d has original group dimension d/4.
The candidate never applies this group trace conclusion to its formal or merely local analytic projection.
In particular, its ordinary matrix trace two is not evidence for an original group projection of trace one half.

## Analytic realization and finite jets

The coefficient ratios give convergence of both square-root series for |t| < 1.
For \(|w|<\delta<\log2\), the estimate \(|\exp(\pm w)-1|<1\) puts y and its inverse in that disk.
The chosen branch \(s(\exp(w))=\exp(w/2)\) is consistent with the formal root and with inversion and conjugation on this domain.
The displayed entries are holomorphic for nonzero x and z and y in the stated neighborhood.
On its torus part, B and D are unitary, their quotient is a unitary involution, and the resulting matrix is an ordinary orthogonal projection.
The entry bound and the stated analytic interpretation of star follow.

The t-adic ideals are preserved by every operation used, so the exact equations descend to each R_N.
The basis determinant remains a unit after reduction, proving free image and kernel rather than merely a formal trace assertion over a ring with nilpotents.
These reductions are compatible and come from the single analytic projection.

For the degree-one representatives, direct multiplication gives \((H^{[1]})^2=(1-t^2/4)I\) and projection defect \(-t^2I/16\).
Each two-dimensional block of the representative projection has determinant \(t^2/16\), giving total determinant \(t^4/256\) as asserted in (14).
The ordinary representative consequently has generic rank four, while its quotient-class image over R_1 is free of rank two.
These claims concern different rings and are consistent.
For arbitrary N, analytic Taylor remainders and the displayed monomials of modulus one on the x,z torus give the uniform error and operator-norm estimate stated in the candidate.
Neither exact projection nor exact contractivity of an ordinary polynomial representative is needed or implied.

The finite-order limitation is correctly quantified as solvability of the specified equations and local-bound requirements.
A compatible solution at every order rules out a contradiction based only on failure of such solvability.
It does not rule out degree bounds, global rationality conditions, or another additional necessary condition.

## Nonrationality and the restricted global theorem

The valuation at y = 0 of a rational square in K(y) is even, whereas y has valuation one.
The entry s/2 therefore excludes rationality of the explicit lift.
Injectivity of Laurent expansion also excludes a rational matrix with exactly this full expansion.
One circuit about zero changes both s and its inverse by a sign and hence sends the projection to its distinct complement.
This monodromy belongs to the constructed germ and supplies no universal statement about other germs with the same constant term.

For (16), y and its inverse are distinct elements of F, so commutation with B_n forces preservation of the two eigenspaces of B_n squared.
The irreducible polynomial \(X^2-y\) makes the first space a vector space over \(F(\sqrt y)\), with the square root acting as \(B_n\).
The image of an idempotent commuting with this action has even F-dimension.
The semilinear bijection C_a,n sigma_a exchanges the two coordinate spaces and, by covariance, their image spaces; therefore their F-dimensions are equal.
The total rank is a multiple of four for every positive n.
For n = 1, an idempotent of rank zero or four is zero or the identity.
A rational idempotent regular at y = 1 cannot specialize to E_y because its constant integer trace would have to specialize from zero or four to two.
This proof uses exactly the extra B-commutation stated in (16), with no star or second-covariance premise hidden in the argument.

## The deformation and its consequence

Since Q-I lies in tM_4(R), both T and T star lie there, and K_0 is t-adically topologically nilpotent and skew-adjoint.
The exponential and its inverse are well defined, inherit both covariance equations coefficientwise, and satisfy U_0 star = U_0 inverse.
Conjugation therefore preserves the exact projection, star, covariance and rank properties, with the same constant term.
The convergent matrix exponential gives the claimed local analytic realization and is unitary on the torus.

Expanding \(Q^\star=Q^{-1}=I-tJ+O(t^2)\) gives \(K_1=JA+A^{-1}J\), exactly as stated.
Using \(E_y=(I+B_0)/2\) and \(B_0^2=I\) reduces the first commutator coefficient to \(K_1-B_0K_1B_0\).
Its \((1,2)\) entry is \((x-1)-(1-x)z^{-1}=(x-1)(1+z^{-1})\), which is nonzero in K.
This confirms (19) without any generic numerical specialization.
Thus the local equations and the initial projection do not imply the added B-commutation.
The candidate correctly makes no rationality assertion for this deformation.

## External coverage and remaining scope

The primary [Linnell journal scan, Theorems 1.3 and 1.5, printed pp. 562--564](../../literature/pdf/Lin93.pdf#page=3), was inspected directly for its exact hypotheses, coefficient field, affiliated ambient algebra and division conclusion.
The source's elementary-amenable and class-C hypotheses apply to the torsion-free virtually abelian group here.
The relevant theorem statement and applicability are accepted as established external background; its proof and external foundations were not re-audited in this review.
The retained [source unit](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) identifies that separate proof-inspection scope.
This supports the candidate's statement that known division coverage is available, while leaving its actual crossed-product identification outside the elementary formal-lifting proof.
The candidate neither silently invokes that coverage to prove its own restricted theorem nor claims to have completed the unrestricted rational descent argument.

## Whole-artifact finding

No mathematical gap was found in the fixed candidate at its stated scope.
The whole argument supports an exact rank-two formal and locally analytic lift, every compatible finite jet with the stated local bounds, nonrationality and complementary monodromy of this explicit lift, the rational rank-divisibility theorem with additional B-commutation, and the demonstration that the extra commutation is not forced by the local data.
The conclusion remains a failure of the specified formal and finite-jet repair mechanism, together with a restricted global theorem.
It is not a proof excluding every other rational lift, a general rank-divisibility theorem for original group-ring matrices, or a completion review of T_A0001.
The prerequisite checks above cover only their exact used interfaces and do not extend this finding to the unrelated arguments in L_A0010, L_A0022 or L_A0024.
