---
author: Yin
---
# Independent review of complete amenable kernel localization and scalar descent

## Review arrangement and exact inputs

The review act is dated 2026-11-12T12:17 UTC, with Yin as the human record author.
A separately assigned reviewing agent examined the 2026-11-12 working revision of [Yin_C_A0001_v2](../../claims/Yin_C_A0001_v2.md), including its complete Statement, Argument, and Scope and remaining obstruction.
The reviewer did not participate in developing this proof and received no proof-development dialogue, author explanation, mathematical development summary, or earlier project-review verdict.
The assignment supplied the fixed proof object, the requested whole-proof scope, the necessary source locations, and the requirement to distinguish these conditional results from the unresolved general problem.
The reviewer formed the mathematical findings from the target and its necessary inputs without consulting the earlier R_A0002_v1 review.
This is an independent whole-argument inspection of this Claim, not a Task-completion audit.

The direct inputs were the [matrix boundary estimate in C_A0001_v1](../../claims/Yin_C_A0001_v1.md#matrix-boundary-estimate), the [Ele03 propagation and boundary unit](../literature/Ele03/Yin_U001.md#folner-and-propagation), [MSY23 U003's actual rational-closure definitions](../literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra), and [MSY23 U004's finite-trace affiliated interfaces](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and [domain-aware rank calculus](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof).
Those source units include their own earlier source-inspection facts; they were consulted as necessary mathematical inputs, not as prior verdicts on C_A0001_v2.
The reviewer reconstructed the reused finite-set estimate and the specific affiliated interfaces used below.
General existence and associativity of the affiliated algebra, spectral calculus, polar decomposition, and faithful finite-trace theory remain accepted foundational inputs at the scope stated in U004.

For the homological conclusion, the reviewer read the text layer of the [BCM04 author-hosted edition](../literature/BCM04/readme.md#author-edition), one-based PDF pp. 1–6 and 19, and then checked the prepared [projective-trace source unit](../literature/BCM04/Yin_U001.md#amenable-projective-trace).
The source's assembly theorems and Theorem 1.4 are accepted established inputs after their statements and applicability were checked; their original proofs were not re-audited.
The [earlier amenable comparison](../../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) was consulted only for the already-known status of the amenable domain/Atiyah equivalence.
Its Ore route and its exploratory examples are not premises of this review's verification of the submitted proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |
| [Whole-reassessment finding](#whole-reassessment-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Exact statement](../../claims/Yin_C_A0001_v2.md#statement) | All stated hypotheses and conclusions: actual rational realization, quantitative localization and complete density, finite scalar descent, conditional complete Hilbert-kernel witness, arbitrary amenable group extension, and finite-projective-resolution formula and conditional equivalence. |
| [Whole-argument finding](#whole-argument-finding) | [Complete argument](../../claims/Yin_C_A0001_v2.md#argument) | Every derivation and its direct interfaces, including unbounded affiliated domains, all dimension comparisons, deletion termination, weak exactness, and the precise accepted BCM04 projective-trace input. |
| [Whole-argument finding](#whole-argument-finding) | [Scope and remaining obstruction](../../claims/Yin_C_A0001_v2.md#scope-and-remaining-obstruction) | Conditional scope, absence of an unconditional scalar-domain conclusion, and the distinction between Hilbert closure and algebraic finite generation or projectivity. |
| [Whole-argument finding](#whole-argument-finding) | [Reused finite-set estimate](../../claims/Yin_C_A0001_v1.md#matrix-boundary-estimate) | Direct reconstruction of the rectangular finite-propagation estimate used by the new argument, with unnormalized matrix trace and the stated inner-boundary convention. |
| [Whole-reassessment finding](#whole-reassessment-finding) | [Originally submitted reassessment](../../ledger/Yin_L_A0030_v1.md) | All sections of the 2026-11-12 text inspected at 12:22 UTC, before addition of the section headed Smaller algebraic certificates and their exact missing hypotheses; that entire new section and its three subsections are excluded. The inspected remaining sections are unchanged and include the retained-result interfaces, two-term index cancellation, support-preserving number-field specialization, restriction of scalars, and limited continuation conclusions. |
| [Whole-reassessment finding](#whole-reassessment-finding) | [Two-term complex calculation](../../ledger/Yin_L_A0030_v1.md#why-the-existing-finite-free-complex-has-no-usable-index) | Reduced Hilbert homology, equality of kernel and cokernel dimensions, and the cancellation that prevents an arithmetic conclusion about the individual kernel. |
| [Whole-reassessment finding](#whole-reassessment-finding) | [Coefficient specialization](../../ledger/Yin_L_A0030_v1.md#the-remaining-coefficient-field-is-not-the-main-analytic-difficulty) | Nonzero finite-type coefficient algebra, number-field residue, and preservation of every coefficient and both exact supports. |
| [Whole-reassessment finding](#whole-reassessment-finding) | [Restriction of scalars](../../ledger/Yin_L_A0030_v1.md#the-precise-limit-of-restriction-of-scalars) | Constant complex similarity, embedding-invariant finite-window ranks, the unnormalized identity \(\nu_G(\rho(a'))=d\delta\), and its precise limitation. |

## Whole-argument finding

The complete statement and argument pass this independent inspection under their explicitly stated hypotheses and accepted foundational and external inputs.
No unresolved mathematical gap was found in the claimed extensions.
The decisive checks follow; the established amenable domain/Atiyah equivalence was not substituted for any step of the submitted proof.

### Actual rational realizations and operator domains

The rational closure is taken in the actual algebra \(U(\mathcal N(G))\), and the inverse-entry definition in MSY23 applies to this inclusion without free-field injectivity or maximal-rank assumptions.
For each entry, its chosen denominator is already a unit in the actual ambient matrix algebra.
The finite block diagonal sum and the coordinate input/output maps give the stated rectangular realization, with the minus sign absorbed into the output map.
Polynomial entries and the optional dummy identity denominator introduce no missing invertibility premise.

For a closed affiliated \(T\), spectral calculus and polar decomposition provide \(T^\dagger T=1-p_T\).
If a bounded group-ring column \(x\) satisfies \(Tx=0\) as an affiliated identity, multiplication by \(T^\dagger\) gives the bounded identity \((1-p_T)x=0\).
Its application to \(\delta_e\) places \(x\delta_e\) in the actual closed Hilbert kernel, which is contained in the operator domain.
Conversely, right invariance puts every translate of \(x\delta_e\) in that kernel; boundedness of \(x\) and closedness of the kernel then put its entire range there.
The natural product \(Tx\) is consequently zero on every input vector, so its affiliated closure is zero.
This establishes both directions needed in the proof without applying an unbounded rational expression term by term to a finite-support vector.

### Quantitative localization and complete density

Both triangular factors in equation (11) have actual affiliated inverses, and their dimensions and factor order are correct.
Rank invariance and direct-sum additivity give \(\operatorname{rk}_G L=k+\operatorname{rk}_G P\) and hence \(\nu(L)=\nu(P)\), including rectangular \(P\).
The rectangular rank inequalities are the same kernel and closed-range inequalities as in U004, or follow by adding zero blocks; they assume no integer-valued rank.

The finite-propagation input was rechecked directly.
The restriction from \(\mathbb C[F^{-w}]^{n+k}\) into \(\mathbb C[F]^{m+k}\) has kernel and image locally dominated by the corresponding invariant kernel and closed range of \(L\).
Their two nonnegative dimension deficits sum to \((n+k)|\partial_wF|/|F|\), which gives precisely the lower bound (12).
For \((x,y)\in W_F\), affiliated elimination gives \(Px=0\), and \(x=0\) forces \(y=0\) because \(Q\) is a unit.
The already-checked domain argument makes this an injective map into the genuine finite-support Hilbert kernel of \(P\).
The upper bound in (2) follows from projection order and the constant diagonal of its invariant kernel projection.

The closure \(K_0\) of all these finite-support kernel vectors is right invariant and contained in \(\ker P\).
Every local finite-dimensional subspace is dominated by its projection, so its normalized dimension is at most \(\dim_GK_0\).
The Følner limit of (2) forces \(\dim_GK_0=\nu(P)\), and faithfulness applied to the difference of the two nested projections gives equality of the subspaces.
This verifies complete density, not merely existence of a nonzero vector.
The eigenkernel observation is valid for square \(P\), the setting in which \(P-\lambda I\) is defined.

### Finite descent and the complete conditional kernel witness

For a nonzero scalar in \(B\), the finite-set estimate identifies analytic noninjectivity with existence of a nonzero algebraic right annihilator.
Thus the domain hypothesis certifies the actual affiliated inverses used as scalar pivots.
In a column relation, multiplying \(D_jv_j=-\sum_{i\ne j}D_iv_i\) on the right by \(v_j^{-1}\) gives equation (13) with the correct noncommutative order.
The factorizations \(D=D'H\) and \(D'=DJ\) imply equal analytic rank in both directions.
Only the literal group-ring submatrix \(D'\), never the affiliated coefficient matrix \(H\), is used for the next finite-propagation extraction.

A matrix of noninteger rank can never become injective while keeping that rank, and cannot reach zero columns.
Each successful pivot deletion lowers the number of columns, so finitely many such steps must expose a nonzero noninjective scalar coordinate.
Scalar extraction then supplies the claimed pair of actual nonzero group-ring zero divisors.
This argument is a finite existence descent and makes no algorithmic injectivity-decision claim.

Under the domain assumption every nonzero pivot is available, so deletion stops at an injective matrix with an integer number \(k\) of columns.
Embedding the successive relations with zeros in all earlier deleted positions gives \(d=n-k\) columns over \(B\).
On the deleted rows their matrix is triangular with affiliated units on the diagonal, hence invertible over \(U\).
This proves injectivity of \(V\); it is stronger than merely selecting linearly independent finite-support vectors over \(\mathbb C\).
Its closed range is an invariant subspace of \(\ker A_0\) of the same dimension \(d\), proving (7) by faithfulness.
Polar decomposition gives (8), with \(V^*V\) invertible in the affiliated algebra and the closed total product equal to the bounded range projection.
The argument correctly permits an unbounded inverse and a nonclosed image before closure.
The case \(d=0\) gives the zero projection and requires no inverse of a nonempty Gram matrix.

For nonzero \(a,b\in B\) with \(ab=0\), the nonzero kernel and the nonzero range support of \(a\) give \(0<\nu(a)<1\).
This proves the converse integer-dimension implication directly.
It supplies no proof that torsion-freeness alone rules out such a pair.

### Complementary scalar kernel mass and group scope

A nonzero nonunit scalar \(r\in\mathcal R\) has \(0<\alpha=\nu(r)<1\) by finite-trace injectivity/invertibility and faithfulness.
Condition (5) makes the integer dimension of \(W_F\) strictly positive, and coordinate injectivity supplies \(x\ne0\).
The identity \(p_rx=x\) places the entire closed range of \(x\) inside \(\ker r\), giving \(\operatorname{rk}_Gx\le\alpha\) and \(\nu(x)\ge1-\alpha\).
Condition (6) therefore makes the finite-support kernel of \(x\) strictly positive and gives \(z\ne0\) with \(xz=0\).
The first estimate uses only the propagation of \(L\), and the second only that of \(x\); no inverse is assigned finite propagation.

For a non-finitely-generated amenable group, all entries of a selected group-ring matrix or finite realization belong to one finitely generated amenable subgroup \(H\).
The right-coset decomposition \(G=\coprod Ht\) supplies copies of the left regular \(H\)-representation, so kernels, canonical traces, and injectivity of \(Q\) agree at the required interface.
Its affiliated inverse agrees by spectral calculus.
Finite-support approximation on finitely many cosets then gives the same complete kernel-density and conditional witness conclusions over \(G\), including when \(G\) is uncountable.
The proof does not presume that exactness of a resolution over \(\mathbb CG\) descends to \(\mathbb CH\).
For a finite group, choosing \(F=G\) uses the stated empty-complement convention and causes no boundary exception.

### The finite projective resolution and source interface

For an idempotent \(E\), its bounded range is closed, and its orthogonal range projection \(q_E\) satisfies \(q_EE=E\) and \(Eq_E=q_E\).
The off-diagonal term in \(E=q_E+q_EE(1-q_E)\) has trace zero by traciality, verifying equation (14) without requiring that \(E\) be selfadjoint.
Each right-module map between the displayed finite projectives extends to a matrix over \(B\) with the stated source and target compressions.
Stacking \(D_i\) with \(1-E_i\) identifies its kernel on \(H_i\) with the kernel of the actual group-ring matrix (15).
Complete density makes this the closure of its algebraic kernel, and algebraic exactness identifies that kernel with the preceding image.
Boundedness of the differential and density of \(E_{i+1}B^{r_{i+1}}\) give precisely the Hilbert image closure needed for weak exactness.
At the left endpoint algebraic injectivity and density give Hilbert injectivity; at the augmentation endpoint density identifies \(\overline{K_a}\) with \(\ker a\).
Kernel/closed-range dimension additivity therefore telescopes with the signs in (10).
No tensor-product exactness, closed-range hypothesis, or algebraic projectivity of \(K_a\) is silently inserted.

BCM04 Theorems 1.3 and 1.4 and Lemma 1.5 give the complex Bass statement for amenable groups without a remaining countability restriction.
Section 2 and the first paragraph of the proof of Proposition 6.1 identify the Kaplansky and augmentation traces on all of the relevant \(K_0\) for torsion-free groups.
In particular their conclusion applies to matrix idempotents, not merely the scalar idempotents treated at the end of Proposition 6.1.
For \(E_i\in M_{r_i}(B)\), the resulting trace is \(\operatorname{Tr}_{\mathbb C}(\varepsilon(E_i))=\operatorname{rank}_{\mathbb C}(\varepsilon(E_i))\), an integer with the required unnormalized convention.
The coefficient trace identity is independent of whether the represented projective module is written on the left or on the right.
This checks the exact external input used by the submitted formula.

Thus a finite resolution for a fixed nonzero \(a\) makes \(\nu(a)\) an integer in \([0,1)\), forcing it to vanish.
The assertion for every nonzero \(a\) follows only under the universally quantified finite-resolution premise.
Conversely, in a domain every \(K_a\) is zero and has a trivial finite projective resolution.
This verifies the stated equivalence while leaving the essential existence of these resolutions unresolved.

## Scope and limits of the finding

The review covers the submitted complete proof and its source interfaces, with the general operator-algebra foundations and BCM04 assembly results accepted at the depths stated above.
It is not formal verification and does not claim a fresh proof audit of every source theorem.
No claim of new group-class coverage or novelty of the amenable domain/Atiyah equivalence is supported or needed.
The finite-propagation proof supplies no finite projective resolution of a nonzero principal annihilator, and the affiliated projection formula supplies no idempotent matrix over \(B\) representing that kernel.
The full torsion-free amenable domain problem and any broader Task remain unresolved by this Claim.
The conditional results and their finite witnesses are the exact mathematical scope that passes review.

## Whole-reassessment finding

This additional review act is dated 2026-11-12T12:22 UTC.
The same reviewer independently inspected the complete [L_A0030_v1 reassessment](../../ledger/Yin_L_A0030_v1.md) as fixed at that time, after completing the preceding Claim inspection.
This was the 2026-11-12 text before addition of [Smaller algebraic certificates and their exact missing hypotheses](../../ledger/Yin_L_A0030_v1.md#smaller-algebraic-certificates-and-their-exact-missing-hypotheses).
That later section and all three of its subsections are excluded from this finding; the previously inspected sections remain unchanged.
The follow-up supplied only that fixed mathematical artifact, its exact review scope, and necessary dependency locations.
Before forming this finding, the reviewer received no development discussion or proposed repair and contributed no mathematical correction to the artifact.
The previously inspected C_A0001_v2 argument is reused here at its verified scope.
For the retained comparisons, the reviewer read the exact statement of [C_A0011_v1](../../claims/Yin_C_A0011_v1.md#statement), the stated central Laurent obstruction and specialization hypotheses of [C_A0012_v5](../../claims/Yin_C_A0012_v5.md#statement), and the faithful central-finite obstruction in [L_A0029_v1](../../ledger/Yin_L_A0029_v1.md#a-faithful-central-finite-model-forces-virtual-abelianness).
This checks their use in the reassessment, without claiming a fresh whole-proof audit of those three prior artifacts.
The [JL21](../literature/JL21/Yin_U001.md#amenable-rank-comparison), [Bac26](../literature/Bac26/Yin_U001.md#domain-hypothesis), and [JZ19 source unit's Rowen–Saltman passage](../literature/JZ19/Yin_U001.md#external-foundations) were checked at their recorded source-statement and applicability depths.
Their unrelated theorems, external proofs, and earlier project-review conclusions were not used to infer the new finding.

The originally submitted reassessment passes at the scope just specified.
The following checks establish its substantive calculations and the limits of its inferences.

### The two-term index and the existing structural comparisons

For the two-term scalar complex, the displayed quotient is reduced Hilbert homology: the image is explicitly closed before taking the cokernel.
Orthogonal complementation identifies that quotient with \(\ker a^*\).
Polar decomposition equates the traces of the initial and final support projections of \(a\), so both homology dimensions are \(1-\operatorname{rk}_G a\).
The signs in \(1-1=\dim_GH_0-\dim_GH_1\) are therefore correct.
The index equation imposes no independent arithmetic condition on the two equal masses, and the complex itself is not the finite projective resolution of \(K_a\) required by the preceding Claim.
Together with the checked BCM04 interface, this verifies both the conditional resolution argument and the precise failure of the naive two-term substitution.

The normal-hopping comparison correctly retains the arbitrary input matrix in the output nullity, so it does not simplify the full quantifiers.
The gap obstruction is used for the actual finite central-parameter construction with its compatible special-fiber nullity relation; it is not generalized to all conceivable noncentral constructions.
The central-finite comparison requires a faithful embedding of the entire coefficient group algebra into an algebra finite over a central field.
Under precisely that premise its virtual-abelianness conclusion applies, while a finite-dimensional invariant without such an embedding is not excluded.
These uses match the inspected prior statements.

JL21 supplies a normalized rank limit or infimum and identification with the canonical trace rank, without a discreteness conclusion.
Its group-ring application does not require the absent domain property, and the reassessment does not incorrectly impose one.
Bac26's actual conjugacy and associated rank-comparison setting does require the stated absence of zero divisors and maximal separation for its linear sofic representations.
The reassessment correctly rejects using those conclusions to prove that same missing hypothesis.
These are checks of the cited mechanisms, not claims that the literature contains no other applicable method.

### Support-preserving number-field specialization

The original nonzero coefficients define a unital map from the displayed algebra \(D\) to \(\mathbb C\), including the assignment \(Z=P(\alpha,\beta)^{-1}\).
Consequently \(D\) is nonzero.
For any maximal ideal, its residue is a field finitely generated as a \(\mathbb Q\)-algebra, so Zariski's lemma, equivalently the stated weak Nullstellensatz, makes it a finite extension \(K/\mathbb Q\).
Because the product \(P\) is a unit in \(D\), every individual coordinate \(X_s,Y_t\) has nonzero residue.
The specialized factors therefore retain exactly the nonempty supports \(S,T\), and the finitely many equations \(f_h=0\) give their zero product coefficient by coefficient.
Any embedding of the resulting number field into \(\mathbb C\) realizes the pair as complex group-ring elements.
All group elements used lie in the finitely generated subgroup generated by \(S\cup T\), and no amenability premise enters this specialization.
This is a direct verification of the finite-equation application of the established specialization mechanism, not a reliance on the stronger Atiyah coefficient-change theorem elsewhere in JZ19.

### The exact restriction-of-scalars factor

The regular representation of \(K\) on its \(d\)-dimensional rational vector space is an injective algebra map, and extending it coefficientwise gives the displayed injective map into \(M_d(\mathbb QG)\).
Separability gives one constant invertible complex matrix simultaneously diagonalizing this coefficient representation into its \(d\) field embeddings.
Tensoring that change of basis with the identity on \(\ell^2(G)\) is a bounded invertible equivariant change of coordinates, so it preserves analytic rank and nullity.
Thus the nullity of the rational matrix equals the sum of the nullities of the \(d\) embedded scalar factors, with no normalization by \(d\).

For a fixed finite window \(F\), the scalar equations have input support \(F\) and output support inside the finite set \(SF\).
Their matrix entries lie in \(K\), and a field embedding preserves exactly which minors vanish.
The finite-dimensional kernel dimensions are therefore identical for every embedding and every such window.
For amenable \(G\), the already-checked finite-set kernel approximation transfers this equality to analytic nullities; passage through the finitely generated support subgroup covers a group not assumed finitely generated.
Writing the common value as \(\delta\) gives exactly \(\nu_G(\rho(a'))=d\delta\).
The nonzero factors and their nonzero zero-product witnesses give \(0<\delta<1\).
These inequalities alone do not prohibit \(d\delta\) from being an integer, so restriction of scalars does not preserve the particular fractional-nullity obstruction and does not produce a rational scalar zero divisor.
This limitation does not assert the existence of a torsion-free amenable counterexample or rule out an additional coefficient-descent theorem.

### Continuation boundary

A singleton collision fiber would contribute one nonzero coefficient product to \(a'b'\), so every fiber of a zero-product witness must contain at least two pairs.
A unique-product property or a genuinely separating leading-term rule would exclude the witness, but neither property is deduced from torsion-freeness here.
For a homomorphism to an ordered additive group, the top-height product is the product of the top-height components, so the stated leading-term reduction is legitimate.
It terminates in a contradiction only if the required separating heights or structure are independently supplied, which remains an explicit missing premise.
The reassessment therefore retains valid calculations and useful limits while proving no new group class, unconditional scalar injectivity, or completion of the broader Task.
No unresolved logical gap was found in the inspected reassessment sections.
