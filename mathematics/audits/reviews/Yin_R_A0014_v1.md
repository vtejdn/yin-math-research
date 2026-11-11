---
author: Yin
---
# Independent whole-artifact review of the first amalgamated-atom tests

Review act: 2026-11-11T08:44 (UTC).
Human record author: Yin.
The reviewed artifact is the complete 2026-11-11 revision of [L_A0014 v1](../../ledger/Yin_L_A0014_v1.md), with its displayed formulas (1)--(14), arguments and stated limits.
This is a mathematical proof inspection of that fixed exploration artifact, not a Task-completion review.

## Arrangement and inputs

A separately organized reviewing agent performed this initial whole-artifact inspection outside substantive proof development.
The assignment supplied the fixed artifact, necessary dependency locations, the review scope and authorization facts.
No proof-generation dialogue, exploration notes, author explanations or prior findings about this artifact were supplied or consulted.
The reviewer read the proof itself and its directly necessary interfaces, independently reconstructed the calculations, and formed the finding below without reading L_A0013 or the development chats.
Incidental references in the source unit to earlier reviews were not used as evidence for this finding.

The selected mathematical inputs are:

- [L_A0014 v1](../../ledger/Yin_L_A0014_v1.md), in its entirety.
- [C_F0181 v1, square support cuts](../../claims/Yin_C_F0181_v1.md#trace-conventions-and-square-support-cuts), only for the algebraic projection identities; their general-base use was checked directly.
- [BBL21 U001, general-base interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), at its recorded accepted-external-input scope.
  The reviewer also checked the statement of Theorem 3.5, especially part (vii), in the [matching arXiv v2 primary text](https://arxiv.org/html/1903.09002v2), dated 15 May 2020.

Standard finite von Neumann algebra, polar-decomposition, conditional-expectation and affiliated-operator foundations are accepted.
The analytic foundations of BBL21 subordination were not re-audited.
The inspection checks source identification and applicability for the inputs actually used here; it does not identify the final journal edition or assert source completeness for the surrounding research program.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete fixed artifact](../../ledger/Yin_L_A0014_v1.md) | Entire statement and argument, formulas (1)--(14), exact normalizations, all examples and the limits of the proposed next investigation. |
| [Whole-artifact finding](#whole-artifact-finding) | [Setting and accepted interfaces](../../ledger/Yin_L_A0014_v1.md#setting-and-accepted-interfaces) | Group realization, amalgamated and matrix-amplified freeness, faithful expectation and the general-base support identity. |
| [Whole-artifact finding](#whole-artifact-finding) | [Support-cut examples](../../ledger/Yin_L_A0014_v1.md#both-support-cuts-can-be-ineffective) | Both explicit kernel projections, full support without a bounded inverse, affiliated normalization and the different behavior of the affine realization. |
| [Whole-artifact finding](#whole-artifact-finding) | [Additive model](../../ledger/Yin_L_A0014_v1.md#an-additive-two-vertex-model-with-an-invertible-expected-kernel) | Positive decomposition, exact kernel and nullities, conditional-expectation integrals and the uniform lower bound. |
| [Whole-artifact finding](#whole-artifact-finding) | [Nonrationality](../../ledger/Yin_L_A0014_v1.md#the-expected-kernel-leaves-the-cyclic-rational-field) | Laurent-polynomial identity, rational-square obstruction and the precise coefficient-field conclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Boundary values](../../ledger/Yin_L_A0014_v1.md#the-actual-subordination-boundary-values-are-nevertheless-zero) | Theorem 3.5 kernel intersection and trace applicability, positivity argument, bimodularity and vanishing of both actual boundary values. |
| [Whole-artifact finding](#whole-artifact-finding) | [Support-cut input](../../claims/Yin_C_F0181_v1.md#trace-conventions-and-square-support-cuts) | Only the projection and square-nullity identities reused by this artifact; no review of the full C argument is claimed. |
| [Whole-artifact finding](#whole-artifact-finding) | [BBL21 source interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) | General-base theorem hypotheses and the exact source clauses used here, with accepted analytic foundations. |

## Whole-artifact finding

No mathematical gap was found in the complete fixed artifact at its stated scope.
The displayed examples and deductions establish the claimed calibrations without using an Atiyah conclusion for the amalgamated group.
The decisive checks follow.

### Setting, order and support cuts

The group presentation identifies the central copy of the infinite cyclic group and leaves the free group on the two remaining generators.
Alternating centered words from the two vertex algebras have nontrivial reduced free-group parts, so their expectation onto the cyclic base vanishes.
The same assertion for matrices follows entrywise by expanding products of centered matrices.
Thus the later summands are free over the full matrix base, with the trace-preserving expectation used in BBL21.
This reasoning needs no claim from L_A0013.

For any faithful conditional expectation, the support of the expected kernel contains the actual kernel projection.
The proof is the vanishing of the positive compression by the complementary base support and faithfulness.
Decomposing the domain into that support and its orthogonal complement then gives formula (1).
This argument supplies no bounded inverse on a diffuse support, in agreement with the artifact's restriction on the imported C interface.

For (2)--(4), direct multiplication gives both Gram operators as \(1+h\).
The projection formulas are obtained as \(I-r^*(rr^*)^{-1}r\) and \(I-c(c^*c)^{-1}c^*\), respectively.
Their off-diagonal entries have the stated adjoint order; centrality of \(s\) and \(h\) justifies the displayed common denominators.
The off-diagonal expectations vanish, and the diagonal traces sum to one.
The zero set of \(u-1\) has Haar measure zero, while every sufficiently small neighborhood of that point has positive measure.
Consequently both expected kernels have full support and lack a bounded inverse.
The two successive support cuts are identities, and selfadjoint doubling preserves this failure in its two diagonal kernel blocks.

The diagonal multiplier in (5) uses the actual inverse of \(u-1\) in the affiliated algebra, with products understood as affiliated closures.
Its two-sided multiplication cancels the central factors in the stated order and gives the displayed bounded matrix.
On almost every cyclic fiber the diagonal multiplier is an invertible ordinary scalar matrix, so the analytic kernel dimension is preserved in this example.
The normalized row and column each have Gram operator \(2\), giving both expected kernels exactly \(I_2/2\).
The argument establishes no bounded similarity.

For (6), the first block equation forces the last coordinate of a kernel vector to vanish, leaving the kernel of the row \(r\); the adjoint calculation leaves the kernel of \(c^*\).
The first support is \(q=\operatorname{diag}(I_2,0)\).
The range of \(Pq\) is exactly the third coordinate because \(r\) is surjective, so its adjoint kernel is exactly the first two coordinates.
The second cut is therefore the same \(q\), and the final matrix is zero.
The successive unnormalized nullities are \(1,2,3\), giving two corrections of one.
This confirms the distinction between the mixed polynomial matrix and its affine realization.

### Additive model and conditional expectation

Expanding \(V^*V\) gives precisely the two positive matrices in (7), each in its indicated vertex algebra.
The central real element \(t\) commutes with the first free Haar unitary, so \(f\) is normal and the expansion of \(f^*f\) has the stated Laurent-polynomial coefficients.
Solving the two row equations gives exactly the column \(w\), including the order \(b^*f\) in its third entry.
Every kernel vector has this form with its first coordinate as parameter.
The identity \(w^*w=1+2f^*f\) proves that \(wk^{1/2}\) is an isometry onto that kernel and that its unnormalized nullity is one.
Each individual row has a bounded right inverse, giving the two individual nullities of two.

The expectation of the kernel projection was checked entry by entry.
A term from the first vertex followed by the second free Haar unitary has zero expectation.
Conjugation by the second unitary preserves the central expectation of a first-vertex term.
The remaining entries reduce to Haar integration in the first unitary with real parameter \(t\).
Writing \(A:=3+2t^2\), one has \(A-4|t|=1+2(|t|-1)^2>0\), so the denominator is uniformly positive and the circle integral is valid for every \(t\in[-2,2]\).
It yields the displayed \(\alpha\), while \(\alpha+2\beta=1\) and the first cosine moment give the displayed \(m\).
At \(t=0\), the integral gives \(k=1/3\) and \(m=0\), resolving the apparent quotient singularity in (10).

The operator bound \(k\ge 1/19\) follows from \(\|f\|\le3\).
Applying it to the two-component column and then taking expectation gives the first inequality in (11).
The comparison matrix is positive, has determinant one, and has trace at most six, hence its smaller eigenvalue is at least \(1/6\).
The third entry satisfies \(\beta\ge(t^2+1)/19\).
These estimates prove the stated uniform bound \(\xi\ge I_3/114\), including all parameter endpoints, without any spectral-gap premise for \(H\).

### Nonrationality and boundary values

Substitution of \(t=u+u^{-1}\) gives exactly the Laurent polynomial and \(Q\) in (13).
Almost-everywhere rational equality on the circle implies the corresponding rational-function identity, since a nonzero rational function cannot vanish at infinitely many distinct regular points.
If \(Q\) were a rational square, cancellation of numerator and denominator would make it a polynomial square.
With positive choice of leading coefficient \(2\), the coefficients of degrees seven through four force the candidate square root to be \(2u^4+3u^2+4\).
Its constant coefficient gives the contradiction \(16\ne4\).
Thus the first diagonal entry, and hence the entire expected-kernel matrix, does not belong to the stated cyclic rational field.
This argument concerns the full expectation, not its support or every possible larger coefficient algebra.

The source check confirms that BBL21 Theorem 3.5 applies to a general von Neumann base and explicitly includes the kernel-intersection identity in part (vii).
Here the ambient faithful normal tracial state is the normalized matrix trace tensored with the group trace, the summands are bounded selfadjoint operators free over the matrix base, and (12) supplies the required bounded inverse of the expected kernel.
Positivity implies that each summand annihilates the kernel of their sum.
The source's kernel inclusion then implies \(b_jp=0\), and bimodularity gives \(b_j\xi=0\).
The proved inverse of \(\xi\) forces each actual boundary value to vanish.
Multiplication of the source's normalized trace identity by three yields exactly \(2+2=3+1\).
The same reasoning validates the stated positive-zero-atom limitation and the observation about opposite base shifts.

### Scope and remaining limits

The artifact establishes failure of the specified support-only repair on its mixed polynomial matrix and nonrationality of the full expected kernel in its additive two-vertex model.
Its explicit normalization and affine support calculation correctly prevent either observation from being promoted to an impossibility theorem for atom transfer.
The positive model supplies no nonzero or uncontrolled subordination boundary coefficient.
The proposed indefinite or non-bottom-atom test is a next research target, not an established construction.

All calculations concern the stated central cyclic amalgam.
This review establishes no noncentral cyclic-edge theorem, universal normalization or support-repair theorem, new Atiyah group class, or completion of the governing Task.
It is an ordinary mathematical review with the accepted foundations stated above, not formal verification.
