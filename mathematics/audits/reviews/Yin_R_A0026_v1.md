---
author: Yin
---
# Independent review of rational projection parity and the central-winding obstruction

Review act: 2026-11-11T17:36 UTC.
Human record author: Yin.
The reviewer was a separately assigned agent outside substantive development of this fixed candidate.
The supplied context contained exact candidate paths, review instructions and operational metadata, without development dialogue, proposing-agent mathematical summaries or previous project-review conclusions.
The complete candidates were read, their obligations enumerated and their arguments and necessary inputs checked before initial findings were formed.
No prior project-review conclusion was consulted before that point.
Afterward, the header and opening of an existing review of the separate scalar power-column input L_A0020 were visible during a declaration-format check; that review is not evidence for this finding.
The inspected object is the complete 12 November 2026 revision of [L_A0022_v1](../../ledger/Yin_L_A0022_v1.md).
This is a whole-artifact mathematical and source-interface review, not a Task-completion review or a re-audit of the scalar free-additive-atom theorem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete candidate](../../ledger/Yin_L_A0022_v1.md) | All statements, arguments, displayed formulas, actual group and matrix models, source interfaces and stated limitations in the inspected revision. |
| [Whole-artifact finding](#whole-artifact-finding) | [Projection lemma](../../ledger/Yin_L_A0022_v1.md#a-rational-projection-lemma) | Complete two-variable rational specialization and even-rank argument, including almost-everywhere boundedness and semilinear symmetry. |
| [Whole-artifact finding](#whole-artifact-finding) | [Kernel projection](../../ledger/Yin_L_A0022_v1.md#producing-the-rational-orthogonal-kernel-projection) | Rational Gram inverse, generic rank, actual orthogonal projection, inherited symmetries and integer group-kernel dimension. |
| [Whole-artifact finding](#whole-artifact-finding) | [Negative family](../../ledger/Yin_L_A0022_v1.md#why-finite-winding-and-monodromy-alone-still-fail) | Complete polar construction, trace-half monodromy family, actual ambient realization and rational-closure exclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coverage and remaining obligation](../../ledger/Yin_L_A0022_v1.md#coverage-source-scope-and-the-remaining-general-matrix-obligation) | Existing group-class coverage, norm-equation comparison, general-quotient limitation and obstruction to specializing every rational inverse. |
| [Whole-artifact finding](#whole-artifact-finding) | [Central trace input](../../ledger/Yin_L_A0019_v1.md#a-full-joint-trace-identity-not-just-a-scalar-moment-fit) | Group-ring trace identity, bounded functional-calculus extension and kernel-atom disintegration as used here. |
| [Whole-artifact finding](#whole-artifact-finding) | [Matrix trace boundary](../../ledger/Yin_L_A0019_v1.md#known-coverage-and-what-this-test-does-not-establish) | Extension with unnormalized matrix trace and absence of general fiber-rank quantization; no re-review of the scalar adjacency conclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Actual index-two input](../../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding) | Actual coset embedding, closed affiliated operations and factor-two trace normalization used by the norm comparison. |
| [Whole-artifact finding](#whole-artifact-finding) | [Norm criterion](../../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness) | Complete index-two division criterion specialized to the commutative coefficient field; no review of L_A0003's separate concrete example is asserted. |
| [Whole-artifact finding](#whole-artifact-finding) | [Known source coverage](../literature/Lin93/Yin_U001.md#routine-lemmas-and-induction) | Applicable established extension/division-closure interface only, retaining the source audit's external-foundation limits. |

## Whole-artifact finding

The complete candidate is mathematically sound at its stated scope.
Its rational-projection argument proves integer kernel dimension for every finite group-ring matrix over the stated \(G_{2,2}\), and its bounded projection family genuinely excludes the proposed inference from finite winding, analyticity and monodromy alone.
No mathematical gap requiring a change to the candidate was found.
The obligations checked were rational removability, preservation of projection rank under specialization, parity from compatible symmetries, faithful regular-trace normalization, production of the actual rational kernel projection, the complete negative-family construction and its rational-closure exclusion, and the exact known-coverage and generalization boundaries.

### Rational specialization and parity

A pole along \(w=1\) over \(\mathbb C(u)\) has a nonzero rational leading coefficient.
For all but finitely many circle values of \(u\), the corresponding one-variable specialization retains that pole.
Fubini supplies one such value for which every entry satisfies the almost-everywhere orthogonal-projection bound in \(w\).
A genuine pole violates that bound on a positive-measure arc, so no entry has a pole along this divisor.
This proves that \(P_0=P(u,1)\) exists over \(\mathbb C(u)\); it does not assume an evaluation map on every rational function.

Specialization preserves the idempotent equation.
For an idempotent over either characteristic-zero field, its trace is the integer rank, so the constant rational function \(\operatorname{Tr}P\) specializes to the same integer.
This proves rank preservation for the projection without assuming preservation of the rank of an arbitrary original matrix at \(w=1\).
The first symmetry makes \(P_0\) preserve the two eigenspaces of \(S_n\).
The second symmetry and \(D_nS_nD_n=-S_n\) identify one restricted matrix after the field automorphism \(u\mapsto-u\) with the other restriction.
A field automorphism and an invertible conjugation preserve rank, so the two ranks agree and their sum is even.
Zero and full-rank projections are included.

### Actual group model and matrix kernels

The presentation calculation is exact: with \(r=ab^{-1}\), the common-square relation gives \(ara^{-1}=r^{-1}\), while \(b=r^{-1}a\) gives the inverse presentation substitution.
The resulting semidirect-product normal form proves torsion-freeness and identifies \(\langle r,a^2\rangle\) as a free abelian subgroup of rank two and index two.
Thus the rational variables are not assigned a hidden algebraic relation.

The model \(s\mapsto S\), \(t\mapsto T(w)\) respects the involution relations and sends \(st\) to \(\operatorname{diag}(w,w^{-1})\).
The integrated half matrix trace is one on the identity, zero on nonidentity rotations, and zero on reflections.
It is therefore the canonical faithful trace on the quotient group algebra.
For the model of \(G\), odd powers in the normal forms \(r^ja^k\) give off-diagonal matrices, and even powers give \(u^k\operatorname{diag}(w^j,w^{-j})\).
Their double Haar integrals are zero unless \(j=k=0\), which verifies the exact factor \(1/2\) in formula (5).
Conjugation by \(D\) justifies using the full \(u\)-circle instead of one square-root branch.
The same equality for all powers of \(A^*A\), followed by bounded continuous functional calculus and the decreasing bounded approximants to the zero spectral projection, gives the matrix-kernel identity with the unnormalized matrix trace.
This checks the specific L19 interface directly, with no assumption of fiber integrality.

Both conjugacy identities for the group generators are correct and extend through their inverses and finite linear combinations to rectangular matrices.
Over \(F=\mathbb C(u,w)\), a rational kernel basis specializes to independent columns with the correct kernel dimension outside finitely many Laurent-polynomial zero sets.
Those sets have Haar measure zero by Fubini and one-variable root bounds.
On that generic set the involution \(\star\) becomes Hermitian adjoint, so the Gram matrix is positive definite when the kernel dimension is positive.
Its determinant is consequently a nonzero rational function, making formula (7) a legitimate rational matrix inverse.
The resulting matrix is the actual orthogonal kernel projection almost everywhere.
Its two symmetries follow from uniqueness of orthogonal projection, then hold as rational identities because equality on a full-measure torus subset forces the relevant Laurent-polynomial numerators to vanish.
The projection lemma makes its generic rank \(d\) even, and the checked trace identity gives \(\dim_G\ker A=d/2\).
The case \(d=0\) is explicitly handled without an empty Gram inverse.
All inverse operations in this argument occur first over the stated rational field.

### The negative projection family and its exact boundary

Direct evaluation gives \(qtp=-i\sin\varphi\,\xi_-\xi_+^*\).
Its polar factor has initial support \(p\) and final support \(q\), since the zeros of \(\sin\varphi\) are Haar-null.
The character automorphism satisfies \(\alpha(p)=q\), \(\alpha(t)=-t\) and hence \(\alpha(qtp)=-(qtp)^*\), proving \(\alpha(v)=-v^*\) by polar uniqueness.
The orthogonal supports give \(v^2=(v^*)^2=0\), so \(J=v+v^*\) is a selfadjoint unitary anticommuting with \(s\).
Its trace is zero, also directly visible from the displayed off-diagonal matrix.
These identities prove that every \(e_\theta\) is a projection of trace \(1/2\), with the stated character monodromy and operator-norm real analyticity in \(\theta\).
The selfadjoint operator \(1-e_\theta\) has exactly that zero-atom mass for every parameter.
The discontinuity used later concerns \(w\), not the analytic central parameter.

The actual ambient construction is legitimate: a central Borel square root of \(z\) is a bounded unitary, and dividing \(a,b\) by it produces selfadjoint involutions in \(\mathcal N(G)\).
The same bounded polar construction and central real and imaginary parts give a projection there.
Changing the square-root branch changes the signs of both involutions and of the two scalar coefficients; the character transformation changes \(J\) by the same sign, so the product expression is branch-compatible.
The L19 trace identity gives the asserted trace \(1/2\) for this actual projection.

The signs in formula (11) follow by expanding the two rank-one polar terms.
Matrices over the actual rational closure embed into matrices over \(\mathbb C(w)\).
An ambient-invertible rational matrix cannot have identically zero determinant, since that would give a generic nonzero kernel and a nonzero actual kernel projection.
The ordinary adjugate therefore supplies its rational inverse.
A rational function essentially bounded on the unit circle cannot have a genuine circle pole and extends continuously over its removable singularities.
The nonzero opposite one-sided limits of the sign function at \(w=1\) exclude such a rational entry for \(J\), and for \(e_\theta\) whenever \(\sin(\theta/2)\ne0\).
The one-variable rational Gram construction likewise makes any kernel projection of a finite rational-closure matrix with one regular-module input rational in \(w\), excluding this projection.
The exceptional central parameters where the sine coefficient vanishes are correctly omitted from that exclusion.

### Sources and remaining scope

Linnell's Theorem 1.3, printed p. 562, was visually checked in the [retained journal scan](../../literature/pdf/Lin93.pdf#page=3).
Its torsion-free, free-normal-subgroup and elementary-amenable-quotient hypotheses apply with the infinite cyclic subgroup generated by \(r\), or through the already retained class-closure account.
It is accepted as established coverage; this review does not re-audit its historical proof or the external Hughes--Lewin foundations recorded in the source unit.
That known theorem is a comparison, not a premise of the parity proof.
The L_A0003 actual embedding and complete norm criterion also apply: the coefficient field is \(\mathbb C(r,z)\), conjugation inverts \(r\) and fixes \(z\), and its invariant \(z\)-valuation turns a putative norm solution into the impossible equality \(2v_z(c)=1\).
This independently confirms the stated comparison without using the new parity conclusion as its premise.

The new calculation uses L19's trace interface but not its scalar free-additive-atom input.
It therefore does not enlarge the inspection scope of BBL21 or AER26.
For other quotients \(C_p*C_q\), the trace integral alone supplies neither a commutative rational model nor the needed divisibility of its value.
The displayed counterexample verifies that generic constancy, finite central winding and correct monodromy do not supply that divisibility.
Finally, an infinite-order group element sent to one by a character has an invertible actual affiliated difference \(g-1\), whose inverse cannot pass through a unital specialization sending that difference to zero.
This confirms why the successful specialization is restricted to the bounded projection after removability is proved.
No extension beyond the calibration group, new group-class coverage, literature-wide priority claim or A0001 completion follows from this finding.
