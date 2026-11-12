---
author: Yin
---
# Independent review of arbitrary coefficient kernels in an inverse-difference array

Review date: 2026-11-11T16:29 (UTC).
Human record author: Yin.
This is an initial independent inspection of the complete fixed [C_A0006 statement](../../claims/Yin_C_A0006_v1.md#statement), [argument](../../claims/Yin_C_A0006_v1.md#argument), and [source-scope discussion](../../claims/Yin_C_A0006_v1.md#source-scope-and-remaining-question), in the revision dated 2026-11-12 (Asia/Hong_Kong).
The reviewing agent was outside substantive proof development and received the fixed candidate, its exact assignment, applicable rules and necessary dependencies without inherited proof-development discussion, development drafts, mathematical summaries or prior conclusions about this candidate.
Obligations were determined from the statement before following the proof and its dependencies.
No prior review of this candidate was consulted.
Earlier review prose in the retained foundational source unit was encountered while reading its actual proofs; it was not used as a substitute for checking the invoked derivations.
The final source paragraph identifying Feld18 and its local logical PDF link was reread after its locator maintenance.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-claim finding](#whole-claim-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-claim finding](#whole-claim-finding) | [Statement](../../claims/Yin_C_A0006_v1.md#statement) | Complete hypotheses and assertions: initial inverse certificates, individual Haar laws, exact rank and nullity, finite group-ring realization, scalar and all-size scopes, partial block rank, grading and joint-word limitations. |
| [Whole-claim finding](#whole-claim-finding) | [Argument](../../claims/Yin_C_A0006_v1.md#argument) | Entire argument, equations (1)--(20), directly invoked local proofs, actual affiliated-domain and trace interfaces, and the final source-scope discussion, within the foundational limits stated below. |

## Whole-claim finding

The statement is supported by the complete argument under its exact hypotheses.
No mathematical gap, circular invertibility premise or source-applicability gap was found in the inspected scope.
The conclusion is an exact obstruction to the proposed rational-unitary extension of the inverse-difference induction, not a solution or counterexample to the [all-size Task](../../tasks/Yin_T_A0001_v1.md#contract).

### Actual objects and original inverse certificates

The pair-coordinate proof in [L_A0011's Klein bottle calculation](../../ledger/Yin_L_A0011_v1.md#an-actual-torsion-free-collision-after-one-step) verifies torsion-freeness and the infinite orders of the required elements.
The relation makes \(z=t^2\) central and gives \((tg^j)^2=z\).
Passing to the direct product with arbitrary torsion-free \(H\) preserves torsion-freeness.
The regular-representation tensor identification and its identity vector give the product canonical trace; they do not require any Atiyah premise for \(H\).

Since \(a\) is a bounded selfadjoint matrix, the lower bounds for both \(B^*B\) and \(BB^*\), and likewise for \(C\), give bounded inverses regardless of \(\ker a\).
Commutation of functions of \(a\) then verifies unitarity of \(q=CB^{-1}\) and both identities (3), including the minus sign in \(I_m-q^2=-4i\varepsilon aB^{-2}\).
No inverse of \(a\) is introduced.
Each cross difference has a norm-convergent inverse because its unitary row parameter has norm one and its column scalar is larger than one.

The ordered factors in (6) are correct.
For \(qg^r\), commutation of the product-group factors and the matrix-normalized product trace give every nonzero integral moment in (7), including negative powers.
The [relative-unitary averaging proof](../../ledger/Yin_L_A0011_v1.md#a-relative-path-certificate-and-its-missing-premise) applies with the sign changed to test \(1-qg^r\): the squared absolute value of the averaging operator has trace \(1/N\), forcing the eigenprojection at one to vanish.
Finite-trace polar decomposition then supplies the actual affiliated inverse.
The [cyclic proof](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) gives the same conclusion for \(1-g\).
These certificates precede all uses of the row-difference inverses and are independent of the unknown coefficient rank.
The identical tensor calculation proves (8), since \(tg^2\) has infinite order.
Thus the claimed individual Haar laws hold for the actual normalized trace, rather than an independently chosen auxiliary trace.

### The two exact rank calculations

The [inverse-difference factorization and central-column shape calculation](../../ledger/Yin_L_A0011_v1.md#one-inverse-difference-schur-step) were checked directly in their displayed order, including the [three-square conclusion](../../ledger/Yin_L_A0011_v1.md#a-shape-invariant-with-central-column-parameters).
They use ring identities and already justified units, so their use in the matrix-amplified affiliated algebra is legitimate.
The transformed cross differences are similar to the original ones; no new row-separation inverse is assumed.

In (10), the middle products cancel as \(x_ic_i+c_ix_1=x_1^2-x_i^2\).
Combining the squares (9) with (3) therefore gives exactly (11), with positive coefficient \(4i\varepsilon\) and ordered factors \(c_3^{-1}z\,aB^{-2}\).
Every factor surrounding \(a\) is an independently known unit.
The two block pivots contribute \(m\) each under the unnormalized matrix trace.
The kernel projection of \(a\) in the product representation is its projection over \(H\) tensored with the identity on the Klein bottle factor, so its trace is unchanged.
This proves both equalities in (12).

The second argument was also checked without relying on the first rank conclusion.
The three denominator-clearing polynomials have exactly the coefficient columns displayed in \(F\), and direct expansion gives \(\det F=-2\).
They commute with the respective row parameter and are bounded units.
Multiplying the last block row by \(B^2\) produces \(BC\,tg^2\) and \(C^2z\), so every entry of (14) is a finite group-ring matrix entry.
The row operations in (15) are ordered correctly.
After the identity pivot, the independently certified pivot \(t(g-1)I_m\) has zero last block to its right; eliminating below it leaves precisely \((C^2-B^2)z=4i\varepsilon az\).
Thus the second calculation gives the same rank and nullity without assuming integer rank for rational matrices.
The only potentially unbounded inverse in this second elimination is the cyclic second pivot.

For these uses, the [actual Schur identity](../../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) and the [closure-aware rank-invariance proof](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) were inspected directly.
The latter obtains product-rank inequalities from closure-of-range inclusion and kernel inclusion, then applies the inverse to obtain equality.
Consequently the equalities concern closed-kernel dimensions in the affiliated algebra; no pointwise action of an unbounded inverse on every Hilbert-space kernel vector is asserted.

### Quantifiers, boundary cases and limitations

For scalar nonzero \(a\), (11) is nonzero because multiplication by units is injective algebraically.
A universal zero-or-unit assertion for that separation would therefore force scalar injectivity.
The replacement \(a=b^*b\) preserves the kernel of any scalar group-ring input \(b\).
This yields the claimed scalar scope without asserting an all-matrix equivalence from scalar injectivity alone.

For arbitrary rectangular \(A\), the bounded Gram identity \(\ker(A^*A)=\ker A\) verifies (17).
Its dimensions use the original number of input columns, not a normalized block trace.
Thus integer rank for the entire constructed block class implies the full Task over every torsion-free coefficient group.
Conversely, the Task applies to the explicitly finite group-ring matrix \(\mathcal P_a\) over torsion-free \(H\times\Gamma\), and the bounded equivalences transfer its integer rank to \(\mathcal K_a\).
This is a global equivalence with the all-size Task, not a claim that an arbitrary fixed coefficient group already satisfies that Task.

The zero input gives rank \(2m\) and nullity \(m\) consistently with both calculations.
For the stated two-square diagonal example, the Cayley value is exactly \(\operatorname{diag}(1,(3+4i)/5)\), and (18) gives ranks five and one with nullity one as claimed.
The example is an allowed integer defect; it neither exhibits a fractional defect nor makes every nonzero block invertible.

The character sending \(t\) to degree one respects the Klein bottle relation.
The factors in (11) have degrees \(-1,2,0,0\), respectively, so their product has degree one while its zero kernel still contains the arbitrary coefficient problem.
This agrees with the exact direct-product coefficient example in [L_A0008](../../ledger/Yin_L_A0008_v1.md#degree-one-still-contains-fractional-coefficient-defects), whose argument and stated exclusions were inspected.
The claim does not apply the nonzero-spectral-parameter character criterion at zero or assume an independently established coefficient division ring.
It correctly leaves the original four-group-element family unclassified: the third row parameter here is generally a rational unitary rather than a regular group element.

Finally, direct multiplication gives \(x_3x_2^{-1}=qg^{-1}\) and \(x_1x_2^{-1}=g\), proving (19).
For nonzero \(a\), the identity \(q-I_m=2i\varepsilon aB^{-1}\) makes this word nonidentity.
Under the explicitly optional restriction \(\varepsilon\|a\|<1\), the continuous functional-calculus expression for \(\operatorname{Re}q\) has the strictly positive lower bound in (20).
Faithfulness of the normalized actual trace then gives a nonzero mixed-word trace.
This disproves the inference from the individual Haar moments to a regular-group joint-word trace law without changing any earlier rank formula.

### Sources and foundational boundary

The retained [MSY23 finite-affiliated foundations](../literature/MSY23/Yin_U004.md#ambient-algebra-domains-and-foundational-inputs) supply closed affiliated operations, matrix amplification and polar decomposition.
Their specific [finite-trace invertibility consequences](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and local rank proof were reread and checked for the present matrix and domain conventions.
The general existence and associativity theory for affiliated closures, and the general polar-decomposition theorem, are retained foundational inputs rather than newly audited source proofs.
No free-field realization theorem, maximal-Delta premise or projection-comparison theorem is used in this claim.

The [GGRW05 arXiv v4](https://arxiv.org/pdf/math/0208146v4), Example 1.2.3(a), Definition 1.2.5 and Proposition 1.2.6, printed/PDF pp. 9--10, was inspected directly.
These passages support the recorded Schur-expression attribution and actual-ring inverse premise.
They do not supply the candidate's inverse-difference injectivity or its particular rank reduction, which are proved by the inspected local calculations.
No generic or formal free-field evaluation is imported from that source.

The [UBC original of Feld18](https://www.math.ubc.ca/~feldman/m511/cayley.pdf), dated November 27, 2018, was inspected directly at Theorem 1(c), printed/PDF p. 1, and its proof on p. 2.
Its convention satisfies \(q=-C_+(\varepsilon a)\), since \(\varepsilon a-iI_m=-iC\) and \(\varepsilon a+iI_m=iB\).
The bounded selfadjoint input satisfies the theorem's hypotheses, and the candidate also establishes its required inverse and adjoint identities directly.
The citation is attribution for that conversion; no selfadjoint-extension theorem or additional unbounded Cayley-domain assertion is needed.

The review covers the complete candidate and its directly invoked project-proof interfaces, with the source scope just specified.
It does not claim a full audit of either cited external work, historical priority, numerical evidence, formal verification or Task completion.
The remaining coefficient-kernel difficulty is retained exactly; the review supplies no evidence that a forbidden fractional kernel actually exists.
