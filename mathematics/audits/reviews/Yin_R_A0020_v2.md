---
author: Yin
---
# Independent review of cyclic polynomial normalization and actual boundary certificates

Review time: 2026-11-11T16:50.
Human record author: Yin.
The reviewer was separately assigned the fixed candidate and its exact mathematical dependencies, outside its substantive proof development.
No development draft, proof-generation conversation, proposing-agent proof summary or prior R_A0020 conclusion was supplied or consulted.
The obligations below were enumerated from the candidate statement before checking its complete argument and source interfaces.
After the initial findings, the coordinator notified the reviewer of an explicit restriction to \(0<r<n\) in the Smith corner paragraph; the saved endpoint and the separate zero-rank sentence were then inspected directly.
Only the author header and title of R_A0020_v1 were read for publication in the same review family; its verdict is neither inherited nor adopted.

## Inputs

- [C_A0007_v2 statement](../../claims/Yin_C_A0007_v2.md#statement) and [complete argument](../../claims/Yin_C_A0007_v2.md#argument), including the example, polynomial recovery, normalization, vertex reduction, two-variable obstruction and complete source/continuation limitations.
- [BBL21 general-base interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), checked against [arXiv:1903.09002v2](https://arxiv.org/html/1903.09002v2), Theorems 3.1, 3.2 and 3.5 and the stated trace convention.
- [Cyclic rational functions](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), [finite-support obstruction](../../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation), [diffuse support example](../../ledger/Yin_L_A0013_v1.md#full-support-does-not-supply-a-bounded-inverse-even-for-a-group-ring-matrix), and the complete [preceding calibration](../../ledger/Yin_L_A0014_v1.md).
- [Lin93 affiliated closure and rank conventions](../literature/Lin93/Yin_U001.md#affiliated-closure-and-rank-conventions), [subgroup interface](../literature/Lin93/Yin_U001.md#ring-lemmas-and-the-extension-argument), and [Lin06 matrix-localization interface](../literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures).
- [Coh06 original](../../literature/pdf/Coh06.pdf), Theorem 1.3.2, printed p. 74 / PDF p. 98; Propositions 1.4.1 and 1.4.5, printed pp. 78--79 / PDF pp. 102--103; Theorem 1.4.7 and its proof, printed pp. 80--81 / PDF pp. 104--105; and Section 1.5's opening, printed p. 86 / PDF p. 110.
- The applicable subordination passages in [C_F0181](../../claims/Yin_C_F0181_v1.md#graded-subordination-proof), [tree transport](../../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators), and the retained [BGVM20 source-scope comparison](../../ledger/Yin_L_A0017_v1.md#source-scope-correction).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0007_v2.md#statement) | Complete hypotheses, conclusions, actual affiliated setting and explicit limitations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0007_v2.md#argument) | Complete proof, example, source interfaces and limitation arguments under the stated accepted external foundations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Four-path model](../../claims/Yin_C_A0007_v2.md#an-indefinite-four-path-model) | Exact spectra, kernel projection, expectation, actual boundary values and three nullities. |
| [Whole-artifact finding](#whole-artifact-finding) | [Polynomial recovery](../../claims/Yin_C_A0007_v2.md#recovery-from-polynomial-kernel-columns) | Both hypotheses, multiplication order, cyclic rational inverse and whole-kernel support observation. |
| [Whole-artifact finding](#whole-artifact-finding) | [Cyclic normalization](../../claims/Yin_C_A0007_v2.md#polynomial-normalization-over-the-cyclic-edge) | Coset factorization, PID module basis, bounded right inverse, congruence, rank invariance, positive-rank corner and zero-rank endpoint. |
| [Whole-artifact finding](#whole-artifact-finding) | [Vertex ranks](../../claims/Yin_C_A0007_v2.md#conditional-reduction-to-the-known-vertex-ranks) | Actual vertex division closures, subgroup ranks and normalized integer-nullity deduction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Two-variable obstruction](../../claims/Yin_C_A0007_v2.md#why-the-same-polynomial-repair-fails-for-a-two-variable-edge) | Specified one-entry witness and same-size polynomial-factor obstruction, with its stated exclusions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Source and continuation limits](../../claims/Yin_C_A0007_v2.md#source-comparison-and-continuation-limit) | Selected-source comparison, classical algebra attribution, remaining witness/full-support assumptions and absence of a general permanence conclusion. |

## Whole-artifact finding

The complete candidate is mathematically sound at its stated scope.
The full-support polynomial-witness hypothesis suffices for the cyclic normalization and, when both vertex groups satisfy complex Atiyah, for integer nullity of the displayed additive selfadjoint matrix.
The argument neither assumes the whole amalgam's Atiyah property nor obtains a general existence theorem for polynomial kernel witnesses.
No unresolved gap was found in the local proof or its use of the inspected source interfaces.

### Obligations and accepted analytic input

The required chain is: establish the actual amalgamated probability space; verify the example; recover actual boundary values from finite columns; construct a polynomial normalization with a uniform lower bound; preserve nullity in the actual affiliated ring; reduce the normalized vertex kernels to integer ranks; and verify all stated obstructions and limitations.
For the first obligation, alternating centered vertex group-ring entries have zero coefficient expectation by reduced-word normal form.
Entrywise expansion proves the same assertion for matrix products, and bounded strong approximation extends it to the vertex von Neumann algebras.
This works without normality or centrality of the edge subgroup.

BBL21 Theorem 3.5 applies to a general von Neumann base with the trace-preserving expectation and an invertible positive expected kernel.
Its part (vii) explicitly gives the intersection of the two boundary kernels and the trace identity; the actual selfadjoint boundary limits are those constructed through Theorems 3.1--3.2.
Applying the theorem to \(M_n(\mathcal N(G))\) with normalized trace and multiplying the result by \(n\) gives exactly (1).
The theorem's analytic foundations remain accepted external inputs, rather than newly re-proved results of this review.
Full support alone is not substituted for its invertibility hypothesis.

### Example and recovery formula

The three successive products \(d_i d_{i+1}^{-1}\) are \(a,b,a\), so the displayed unitary conjugation gives the constant path matrix exactly.
Its characteristic polynomial, four shifted eigenvalues and vector \(v\) verify a simple interior zero eigenvalue and the kernel projection \(WW^*/c\).
Distinct free-group words eliminate every off-diagonal expected coefficient, giving the stated strictly positive diagonal expectation.
Multiplication by each summand gives \(Y_1W=B_0W\) and \(Y_2W=-B_0W\).
The source kernel inclusion and invertibility of the expectation therefore identify the actual limits as \(B_0,-B_0\), without inferring them merely from a compatible algebraic decomposition.
The two determinant-zero blocks of \(Y_1-B_0\) each have rank one, while \(Y_2+B_0\) has one rank-one block and two zero coordinates.
The nullities \(1,2,3\) and their trace identity follow independently.
The total operator's negative and positive spectrum verifies the stated distinction from the positive zero-atom construction.

For general displayed columns, \(pW=W\) and the source inclusion give \(Y_jW=b_jW\).
Taking expectation after right multiplication by \(W^*\) gives \(N_j=b_jC\) in that order.
Both coefficient matrices are finite Laurent matrices over the actual cyclic subgroup.
A singular Laurent determinant would produce a nonzero rational kernel column, and clearing its scalar denominators produces a nonzero bounded polynomial kernel column, contradicting full support of \(C\).
The adjugate formula then supplies the actual cyclic affiliated inverse and proves \(b_j=N_jC^{-1}\).
The inequality \(WW^*\leq\|W\|^2p\) proves the stronger finite-witness variant.
When the columns span the whole kernel, a base projection in the kernel of \(C\) is orthogonal to \(p\) by faithfulness, so full support of \(E(p)\) forces it to vanish.
The cited \(\mathbb Z^2\) column gives exactly the stated full-support matrices without a lower bound.

### Polynomial normalization and the rank-deficient endpoint

For distinct right cosets \(Hu_\alpha\), multiplying \(u_\alpha u_\beta^{-1}\) on either side by elements of \(H\) cannot put it in \(H\).
Consequently coefficient expectation gives \(C=FF^*\) even for a nonnormal subgroup.
Full support makes \(F\) have row rank \(n\) over \(\mathbb C(z)\).
The contraction/localization argument makes the Laurent ring a PID, and the supplied induction proves the required free-submodule assertion.
A basis of the generated column module yields \(F=DF_0\) and \(D=FS\); cancellation over the field gives \(F_0S=I_n\).
No direct-summand or unimodularity assumption on \(D\) is required.

Regrouping \(F_0\) in the original cosets gives a finite group-ring \(W_0\) with \(W=DW_0\).
Taking adjoints of the polynomial right inverse gives the uniform estimate \(F_0F_0^*\geq\|S\|^{-2}I_n\).
The congruence \(Y'=D^*YD\) stays bounded, selfadjoint and vertexwise polynomial, and \(Y'W_0=0\).
It therefore satisfies BBL21's hypothesis by the already checked witness inequality.
The nonzero Laurent determinant supplies an actual affiliated inverse of \(D\) in the edge, vertices and amalgam.
Affiliated rank invariance then gives (N7); the argument makes no invalid assertion about applying an unbounded inverse to every Hilbert vector.

For the saved endpoint \(0<r<n\), Smith reduction gives \(F_0=JV^{-1}\), and \(V^{-1}(V^{-1})^*\geq\|V\|^{-2}I\) gives exactly (N9), supported on \(q\).
The zero-rank case is treated separately and supplies no witness.
Invertible cyclic congruence preserves that deficient rank, so no full-size invertibility premise follows.
Compression can enlarge a kernel and requires its own dimension correction, as the candidate states.

### Vertex reduction and two-variable obstruction

The known complex Atiyah premise on each vertex supplies its actual division closure, not an abstract field embedding.
The standard rational-closure interface is also visible from the Cramer stabilization retained in Lin06: a nonzero noninvertible rational element would have affiliated rank strictly between zero and one, and stabilization would contradict integer ranks of group-ring matrices.
Gaussian elimination in the resulting actual division ring uses affiliated units, so its matrix rank is the integer pivot count.
Right-coset subgroup decomposition preserves these ranks on passing to the amalgam.
Thus (1) gives \(n-r_1-r_2\), and (N7) transfers the normalized result to \(Y\).
This uses the vertex hypothesis only at that step.

For the two-variable witness, coefficient expectation is the sum of the two squared moduli and has exactly the stated isolated torus zero.
A finite factorization \(W=dW_0\) forces coefficientwise divisibility of both \(x-1\) and \(y-1\); all other coset coefficients vanish because the Laurent ring is a domain.
Primality of \(x-1\) and its failure to divide \(y-1\) force \(d\) to be a unit.
The Laurent units have constant torus modulus, so rescaling cannot remove the missing lower bound.
This verifies precisely the specified factorization obstruction, including the harmless \(Y=0\) example and the possibility of a different witness.

### Source coverage and remaining scope

The selected Coh06 passages support the cited PID, finite-module and Smith statements and the Laurent group-algebra identification.
The source theorem is more general than the commutative specialization used here; its invocation introduces no stronger algebraic conclusion.
The proof supplies its own localization, Gram and congruence deductions.
The earlier local passages supply the stated subordination, cyclic-field and support comparisons; the polynomial recovery formula is a direct new deduction within this candidate, without a historical priority claim.
The finite-tree comparison was checked against the retained tree-transport argument, while the BGVM20 observation is reused at its retained scalar phase-gauge scope and does not import a general matrix-weighted equality.

The finite-support obstruction is substantive: the free-tree boundary operator has dense image and an analytic kernel of dimension one, but a finitely supported zero-boundary chain must vanish by leaf removal.
It can also be made into a square selfadjoint kernel obstruction by taking its adjoint times itself.
Accordingly the candidate's witness-existence and expected-full-support restrictions cannot be dropped by the present argument.
The cyclic normalization removes only the lower-bound obstacle once a full-support polynomial witness is available.
No new group class, arbitrary edge-ring normalization or full Atiyah permanence theorem is established.

This review checks the entire selected project argument and its source applicability, not the original analytic proof of BBL21, a full Coh06 book audit, a new proof of affiliated-operator foundations or an unrestricted novelty search.
The unavailable final-journal identification in the BBL21 source account remains outside its scope.
No formal verification or computational proof certificate is claimed.
