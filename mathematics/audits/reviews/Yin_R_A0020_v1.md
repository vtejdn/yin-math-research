---
author: Yin
---
# Independent review of the nonzero boundary model and polynomial kernel certificate

Date: 2026-11-11T16:29.
Human record author: Yin.
The review covers the complete fixed [C_A0007 v1](../../claims/Yin_C_A0007_v1.md), including its statement, argument, worked model, source comparison and continuation limits.
It does not assess completion of the broader Atiyah Task.

## Arrangement and inputs

This is an initial independent whole-argument inspection by an agent outside the substantive development of the candidate.
The supplied mathematical input was the saved candidate and its necessary fixed dependencies; no development draft, proof-generation dialogue, proposing-agent explanation or previous review of this candidate was supplied or consulted.
The reviewer first enumerated the obligations from the saved statement and checked its construction, then followed its source and dependency links.
The prior [R_A0014 finding](Yin_R_A0014_v1.md#nonrationality-and-boundary-values) was consulted only as the cited review of the earlier calibration and analytic interface, after the initial candidate inspection.
It was not treated as a review of C_A0007.

The directly inspected mathematical inputs were the complete [preceding calibration](../../ledger/Yin_L_A0014_v1.md), the cited [cyclic-field argument](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) and [finite-support obstruction](../../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation), the [support-degeneration example](../../ledger/Yin_L_A0013_v1.md#full-support-does-not-supply-a-bounded-inverse-even-for-a-group-ring-matrix), [C_F0181's graded proof](../../claims/Yin_C_F0181_v1.md#graded-subordination-proof), [tree transport](../../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators), and the [scoped BGVM20 comparison](../../ledger/Yin_L_A0017_v1.md#source-scope-correction).
The source interfaces were [BBL21 U001](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) and [Lin93's subgroup and rank account](../literature/Lin93/Yin_U001.md#ring-lemmas-and-the-extension-argument), with its preceding rank conventions.
The reviewer directly checked BBL21 arXiv v2, Theorem 3.5(vii), the boundary-limit construction in Theorem 3.2 and its general-base hypotheses in the [matching primary HTML](https://arxiv.org/html/1903.09002v2).
The already adopted equivalence between complex Atiyah and the actual division-closure assertion was also checked at [Lück--Linnell, arXiv v3, Theorem 2.3(3)](https://arxiv.org/html/1602.06906v3), with coefficients \(F=\mathbb C\).

Standard finite von Neumann algebra, conditional-expectation, polar-decomposition and affiliated-rank foundations are accepted.
The BBL21 analytic existence and boundary theorem are accepted at their verified stated scope; their underlying analytic proof was not fully re-audited.
The Lück--Linnell equivalence was checked at statement and applicability depth, not re-proved.
The Lin93 source account was reused, and the subgroup/rank application was checked directly; this review adds no audit of Lin93's full proof or its external foundations.
The final BBL21 journal edition was not inspected.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [Statement](../../claims/Yin_C_A0007_v1.md#statement) | Complete hypotheses and conclusions, including both certificate variants, actual boundary values and conditional integer nullity. |
| [Whole-candidate finding](#whole-candidate-finding) | [Argument](../../claims/Yin_C_A0007_v1.md#argument) | Complete proof, formulas (1)--(15), analytic/rational interfaces and all asserted limits. |
| [Whole-candidate finding](#whole-candidate-finding) | [Four-path model](../../claims/Yin_C_A0007_v1.md#an-indefinite-four-path-model) | Actual group-ring realization, gauge, spectrum, kernel projection, uniform expected-kernel bound, boundary identification and all three nullities. |
| [Whole-candidate finding](#whole-candidate-finding) | [Polynomial recovery](../../claims/Yin_C_A0007_v1.md#recovery-from-polynomial-kernel-columns) | Finite coefficient extraction, support and bounded-inverse distinction, affiliated cancellation, full-kernel support observation and calibration. |
| [Whole-candidate finding](#whole-candidate-finding) | [Vertex-rank reduction](../../claims/Yin_C_A0007_v1.md#conditional-reduction-to-the-known-vertex-ranks) | Actual cyclic embeddings, known vertex division closures, unnormalized analytic rank and the conditional integer conclusion, including noncentral edges. |
| [Whole-candidate finding](#whole-candidate-finding) | [Source and continuation limits](../../claims/Yin_C_A0007_v1.md#source-comparison-and-continuation-limit) | The selected local comparison, known tree mechanism, lack of a general polynomial-witness theorem and absence of a new group-class or Task-completion claim. |
| [Whole-candidate finding](#whole-candidate-finding) | [BBL21 interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) | Exact general-base theorem hypotheses and boundary/kernel/trace application, retaining accepted analytic foundations. |
| [Whole-candidate finding](#whole-candidate-finding) | [Cyclic field](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | The actual Laurent rational field and its use for a full-support matrix inverse. |
| [Whole-candidate finding](#whole-candidate-finding) | [Subgroup interface](../literature/Lin93/Yin_U001.md#ring-lemmas-and-the-extension-argument) | Actual affiliated subgroup embeddings and compatible trace/rank, without a finite-index assumption or a whole-source proof audit. |

## Whole-candidate finding

No mathematical gap was found in the complete fixed candidate at its stated scope.
The explicit model and the conditional finite polynomial certificate are justified without assuming the Atiyah property of the whole amalgam.
The checks below discharge the obligations enumerated from the statement; they do not assert universal existence of the certificate.

### Analytic input and normalization

Reduced alternating words from the two vertex group rings, centered over \(\mathbb CH\), have zero coefficient expectation onto \(H\).
The normal conditional expectation and the usual bounded approximation extend this to the vertex von Neumann algebras.
Expanding an alternating product of centered matrices entrywise gives the corresponding freeness over \(M_n(\mathcal N(H))\).
This argument works for an actual noncentral amalgam as well as for the central example.

Apply BBL21 with ambient tracial state \((\operatorname{Tr}_n\otimes\tau_G)/n\), base \(M_n(\mathcal N(H))\), and atom \(0\).
The source requires the expected kernel to have a bounded inverse and supplies actual selfadjoint subordination limits, their sum, and the kernel-intersection and trace identities.
Multiplying its trace identity by \(n\) gives exactly formula (1); kernel intersection gives the inclusion used by the candidate.
The source construction identifies these elements as limits of the actual subordination functions.
Full support alone does not meet its inverse hypothesis.
These are verified statement and applicability checks, with the source analytic theorem accepted rather than fully re-proved.

### The explicit model

The given presentation is the central cyclic product with the free group on \(a,b\), so all four diagonal entries of \(U\) are actual group unitaries.
The three ordered products \(d_1d_2^*,d_2d_3^*,d_3d_4^*\) are respectively \(a,b,a\), proving the exact gauge identity.
The characteristic polynomial factors as \((x^2-\lambda^2)(x^2-(1+\lambda)^2)\).
After subtraction of \(\lambda\), its four distinct eigenvalues are the stated \(1,0,-2\lambda,-(1+2\lambda)\); the zero atom is simple and is not bottom spectrum.
The two summands also each have positive and negative spectrum by their displayed two-coordinate blocks.

The relation \(\lambda^2+\lambda=1\) gives \(Jv=\lambda v\), and \(W^*W=cI\).
The gauge and the simple eigenvalue therefore show that \(WW^*/c\) is the whole kernel projection, not merely a subprojection.
Its unnormalized trace is one.
Distinct reduced words \(d_i\) have \(d_id_j^{-1}\notin H\) for \(i\ne j\), so expectation removes exactly the off-diagonal entries and yields formula (6).
Its smallest eigenvalue is the strictly positive stated constant.

Direct multiplication gives \(Y_1W=(0,\lambda a^{-1},-\lambda b^{-1}a^{-1},0)^t=B_0W\) and \(Y_2W=-B_0W\).
The two nonzero middle coordinates ensure that the summands do not separately annihilate this kernel.
The source inclusion gives \(Y_jp=b_jp\), and bimodularity followed by multiplication by the already proved bounded inverse of \(\xi\) identifies the actual \(b_j\) with \(B_0,-B_0\).
No uniqueness assertion for arbitrarily chosen compatible shifts replaces that step.

Each two-coordinate block of \(Y_1-B_0\) is diagonally unitarily equivalent to its constant block, whose determinant vanishes and whose trace is nonzero.
It has rank one, so the two blocks give nullity two.
The middle block of \(Y_2+B_0\) likewise has rank one, while the two outside coordinates are zero, giving nullity three.
The normalization check is consequently \(2+3=4+1\).
Because \(Y\) itself has negative spectrum, it cannot be a sum of positive operators obtained by cancelling opposite base shifts.
The calculation is nevertheless fully explained by the explicit tree gauge and the stated vertex blocks.

### Polynomial recovery and the two inverse hypotheses

The products \(WW^*\) and \(Y_jWW^*\) have finite group-ring support, so coefficient extraction gives precisely matrices over \(\mathbb CH\), even when \(H\) is noncentral.
The proof asserts no algorithm for deciding group-word membership uniformly.
From \(YW=0\), the range of \(W\) is contained in the kernel and hence \(pW=W\).
The source inclusion then yields \(Y_jW=b_jW\), and expectation gives \(N_j=b_jC\) in this order.

Since \(H\cong\mathbb Z\), its group algebra is the Laurent polynomial ring acting by multiplication on the circle.
If \(\det C=0\) as a Laurent polynomial, a nonzero rational kernel column can be multiplied by a common Laurent denominator to give a nonzero Laurent kernel column.
That bounded column has a nonzero range projection in the kernel of \(C\), contradicting full support.
Thus the determinant is nonzero, and the adjugate formula gives \(C^{-1}\) in the actual matrix rational field.
Nonzero Laurent denominators vanish only on a Haar-null set, so these inverses agree with the affiliated inverses under the actual cyclic embedding.
Right multiplication of \(N_j=b_jC\) by this affiliated inverse is legitimate ring cancellation and proves formula (12).
It does not apply an unbounded inverse to every Hilbert-space vector, and it does not require \(C^{-1}\) to be bounded.
The boundedness and selfadjointness of the resulting \(b_j\) are supplied by the analytic theorem, whose separate \(\xi\)-inverse hypothesis remains in force.

For the stronger certificate, \(pW=W\) gives \(0\le WW^*\le\|W\|^2p\).
Positivity of the conditional expectation gives formula (14), and \(C\ge\varepsilon I\) ensures \(W\ne0\) and a positive denominator.
This proves the analytic inverse hypothesis before using the source theorem and also ensures full support of \(C\).
Neither rationality of \(p\) nor rationality of \(\xi\) enters the argument.

For the supplementary full-kernel observation, a base projection \(q\) with \(Cq=0\) satisfies \(E(qWW^*q)=0\).
Faithfulness gives \(qW=0\), and the assumption that the support of \(WW^*\) is \(p\) then gives \(pq=qp=0\).
Consequently \(q\xi q=0\), and full support of the positive \(\xi\) forces \(q=0\).
This proves support, not a quantitative lower bound.
The cited commuting example has \(E(WW^*)=\operatorname{diag}(1,|u-1|^2)\); its kernel expectation and this Gram matrix both approach zero near \(u=1\) while remaining supported everywhere in the measure-theoretic sense.
It confirms the stated distinction.
For the four-path model, the diagonal Gram and the two products \(N_j=\pm B_0C\) agree with the earlier boundary calculation.

### Actual vertex ranks and source limits

The vertex hypothesis supplies division rings in the actual affiliated algebras, not arbitrary abstract skew fields.
The equivalence and equality with rational closure used here are exactly the torsion-free, \(F=\mathbb C\) specialization of Lück--Linnell Theorem 2.3(3).
Every nonzero cyclic Laurent denominator has its actual affiliated inverse already in each vertex division closure; subgroup inclusion keeps that same inverse in the amalgam.
No centrality or finite-index hypothesis is needed.

Gaussian elimination over \(D_j\) produces invertible matrices over \(D_j\) reducing \(Y_j-b_j\) to \(\operatorname{diag}(I_{r_j},0)\).
These are also invertible matrices over the actual affiliated algebra, where left and right multiplication preserve analytic rank.
The right-coset realization of subgroup operators preserves kernel projections and their identity-coordinate traces, so the vertex nullities used in the ambient source identity are exactly \(n-r_j\).
Substitution gives \(\nu_n(Y)=n-r_1-r_2\), with the correct unnormalized convention and no use of the total group's Atiyah property.
Nonnegativity follows from its established equality with an actual nullity.

The selected C_F0181, BBL21-U001 and L_A0014 passages do not state the displayed finite polynomial recovery formula.
This confirms the candidate's limited local comparison only, with no historical-priority conclusion.
The explicit gauge agrees with the retained tree-transport mechanism, and the BGVM20 comparison is confined to the stated scalar phase gauge rather than a general matrix-weighted equality.
The free-tree boundary operator in L_A0002 has nonzero analytic kernel but no finite-support kernel by the leaf-edge argument; thus the existence of polynomial kernel columns cannot be assumed for arbitrary group-ring systems.
Taking its positive square also preserves this obstruction for a selfadjoint matrix, if that narrower comparison is wanted.

The candidate establishes a sufficient certificate and a fully verified pilot example.
It does not establish availability of the certificate for all additive matrices, a general repair of diffuse support degeneration, a new Atiyah group class, or completion of the governing Task.
This is a mathematical proof review with the accepted-source boundaries above, not proof-assistant verification or a full re-audit of the cited external theories.
