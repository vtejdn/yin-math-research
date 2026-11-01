---
author: Yin
---
# Independent complete review of the measurable Hermitian Gaussian criterion

Review performed and recorded: 2026-10-14T21:19.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and inspected scope

The complete fixed [C_F0157 v1](../../claims/Yin_C_F0157_v1.md), initial decision dated 2026-10-14T21:15, was read together with its three exact direct inputs: the full C_F0156 argument, the C_F0153 statement and applicable relative-degree proof, and the C_F0070 statement including Part C and its actual vacuum calculation.
The separate complete [R_F0164](Yin_R_F0164_v1.md#conclusion) for C_F0156 was read at its arrangement, bindings and conclusion; C_F0156 had been selected as proved and independently reviewed before this review was fixed.

Root and the normal branch developed C_F0157 and its measurable phase/criterion proof.
This reviewer did not contribute to that proof, to C_F0156's M1--M8 construction, or to the measurable Gaussian phase argument, and did not read D_F0002.
The assignments disclosed the intended criterion and the points needing scrutiny.
The reviewer previously contributed the Wick-word contraction formula and cut/application checks during C_F0145's development, and developed separate nonnormal examples and finite-relation results.
That earlier relative-degree work is an accepted ancestor of C_F0153, not an independently re-reviewed result here.
The present independent classification covers the new fixed C_F0157 argument and the exact applicability of its accepted direct interfaces; it does not reclassify the reviewer's earlier development.

No author modification or mathematical repair was requested during this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0157 statement](../../claims/Yin_C_F0157_v1.md#statement) | Exact equivalence of intrinsic actual A, strong S, and the scalar actual vacuum plus inverse-square and positive-modulus chi integrability for bounded measurable Hermitian kernels, including zeros, target generation, original canonical domains and phase-correct vacua. |
| [Conclusion](#conclusion) | [C_F0157 argument](../../claims/Yin_C_F0157_v1.md#argument) | All four sections: actual phase automorphism, intrinsic moment necessity and zero-set exclusion, premise-independent sufficiency, strong-to-vacuum implication and original canonical identification. |
| [Conclusion](#conclusion) | [C_F0156 argument](../../claims/Yin_C_F0156_v1.md#argument) | Bounded Gaussian construction and generation, actual target moment extraction, M4--M8 algebraic-tensor integration by parts, full-adjoint matrix-element transfer and original closure restoration. The hypotheses used in the sufficient construction are checked without importing its supplied-target-A premise. |
| [Conclusion](#conclusion) | [C_F0153 statement](../../claims/Yin_C_F0153_v1.md#statement) | Arbitrary abelian-base relative Wick model, actual coefficient adjoints and degree-zero/one contraction/domain estimates. The finite separated-block application is not treated as a measurable-kernel theorem. |
| [Conclusion](#conclusion) | [C_F0070 statement](../../claims/Yin_C_F0070_v1.md#statement) | Normal-tuple Part C: actual vacuum from full bounded-vector duals with the vacuum in each actual adjoint domain, and the normal starred-core uniqueness used to identify canonical restrictions. No general bare-F converse is imported. |

## 1. The measurable phase is an actual automorphism

The Hermitian condition on a makes b=|a| symmetric.
Its zero set may be chosen symmetric up to a null set.
Defining theta=a/b off that set and theta=1 on it gives a unimodular measurable kernel with theta(v,z)=conjugate(theta(z,v)).
Null-set choices do not affect the operators on the product-measure relative Wick spaces.

Each U_n is multiplication by a product of unimodular edge factors, so it is unitary.
U_0 fixes every vector in L2(N), in particular Omega.
The left N action is multiplication at the first endpoint and commutes with these scalar factors.

In U S U*, creation adds the leading factor theta(z_0,z_1), while annihilation integrates the removed first variable with coefficient conjugate(theta(z_0,z_1))=theta(z_1,z_0).
These are exactly the creation and adjoint-annihilation actions of T_theta.
This verifies USU*=T_theta as a bounded-operator identity, not just an equality of vacuum vectors.

The generation argument is also valid for this phase.
Finite separated marginal kernels can approximate conjugate(theta) almost everywhere with a common supremum bound; they may be chosen Hermitian by symmetrization.
Multiplying them pointwise by theta gives uniformly bounded Hermitian kernels tending to 1.
Their Gaussian operators are finite outer N combinations of T_theta, and the bounded creation/annihilation model gives strong convergence to S.
Hence W*(N,T_theta)=M.
Conjugation by U therefore maps M onto M, fixes N pointwise and preserves the trace because U Omega=Omega.

For finite separated b_l, the outer N coefficients commute with conjugation by U, so U T_(b_l) U*=T_(theta b_l).
Uniformly bounded Hermitian approximants to b and the same strong-limit argument establish UT_bU*=T_a.
Consequently the two intrinsic target algebras and their original star polynomial cores correspond exactly.

The tensor-square unitary respects the coefficient bimodule actions.
Unitary conjugation therefore transports derivations and their actual adjoints, the specified canonical restrictions and their closures, as well as the dual operators and their actual adjoint domains.
The trace automorphism is isometric in operator norm, so all the imported norm estimates retain their constants.
No derivative of the measurable phase, and no extension of a supplied target derivation to S, is involved.

## 2. Necessity is intrinsic before generation and excludes zeros

For the normal coordinate Z, the outer spectral difference has zero kernel on the coarse Hilbert space because its joint scalar measures are absolutely continuous with respect to mu squared and the diagonal is null.
Thus a T-coordinate derivation killing Z also kills Z*.
This argument works in the intrinsic target coefficient module before equality with M is known.

Testing the actual T vacuum against f(Z)T_b g(Z) gives equation (6).
These test vectors lie in reference relative degree one.
After the isometric inclusion L2(M_b) into the reference space, the equation tests b times the conjugate of the H1 projection against every polynomial tensor f tensor g.
This product is L2 because b is bounded.
Density forces it to equal 1 almost everywhere.
Therefore a positive-measure zero set is impossible, and the projection is precisely 1/b in L2.
Neither inverse membership nor target generation was assumed to obtain this conclusion.

Once b is nonzero almost everywhere, the bounded Gaussian generation proof applies.
Its truncations b min(n,1/b) are uniformly bounded by one and tend to one; the intermediate finite-kernel approximants are bounded for each fixed n.
The two successive strong-limit steps place S in W*(N,T_b), proving M_b=M.

The Z-coordinate marginal restriction and vacuum compression then give the actual scalar xi_N.
C_F0156's separated-endpoint quadratic tests apply under exactly the established hypotheses: bounded positive b almost everywhere, an actual original target vacuum, and the normal marginal graph approximation.
Their first and last derivative contributions identify the H2 projection with chi_b.
Dividing by the adjacent nonzero factors is legitimate on a full-measure set.
The endpoint diagonal is null.
Thus the second integral is finite because this is an existing Hilbert projection, rather than a formally assigned function whose domain was assumed.

This proves item 1 implies item 3, including the zero-kernel case.
It does not require equality M_a=M before the first moment argument.

## 3. Sufficiency does not use supplied target A

This is the most important premise check.
Start only with the three conditions in item 3.
The actual scalar xi_N gives the free-reference derivation delta_N on C<Z,Z*,S>, zero on S, with its actual vacuum and the scalar/free contraction bounds retained in C_F0156.
Generation follows from b nonzero almost everywhere independently of any target derivation.

For r=b(z,w)/b(w,v)>0, the real numerators r inverse minus one and one minus r have the same sign.
Their squared magnitudes therefore sum to at most the squared magnitude of r inverse minus r.
The two coefficient components in (8) are orthogonal before insertion, while their actual partial_S adjoints concatenate to the same degree-two path and add.
Thus ||beta||2<=||chi_b||2 and partial_S*(beta*)=chi_b are actual Hilbert statements.
C_F0153's arbitrary-base degree-one result applies to these coefficients; no finite spectral partition or bounded inverse of b is being imported.

The reference sum delta_N+I_beta partial_S has actual vacuum xi_N+chi_b.
The forward and reversed contraction bounds and the original-graph mechanism give the closure E'_Z and its actual adjoint on all bounded vectors.
This construction uses only the supplied scalar vacuum and the explicit Hilbert beta.
It does not use the existence of a Z-coordinate target derivation.

The commutator at T_b requires an additional passage, and it is present.
Reversing the componentwise adjoint in (8) gives the two ratios in C_F0153 (G5).
Multiplication by the bounded outer endpoint value b makes their negatives the formal first- and second-leg divided differences of b.
Consequently G_b is L2.
The soft-Cauchy argument M4--M6 in C_F0156 uses only xi_N and actual algebraic tensor adjoints.
It does not assert maximal/minimal graph equality or a core for the entire adjoint.

For bounded smooth polynomial kernels b_n tending almost everywhere to b, M7 pairs the reference derivative against fixed original polynomial tensors, moves the derivative onto their actual adjoints, and identifies the limit by the parameterized soft identity.
M8 gives strong coarse convergence of the inserted correction to -G_b by dominated convergence in the explicit degree-one coefficient spaces.
Thus the weak commutator limit is zero on the reference core.
The actual full adjoint domain and bounded strong convergence of T_(b_n) pass this identity to T_b on every bounded vector.
The same reference-core argument gives the required Z and Z* commutators.
This portion of C_F0156 is premise-independent once xi_N and beta have been constructed, as C_F0157 explicitly checks.

For the T coordinate, 1/b belongs to relative coefficient degree zero by assumption.
The actual adjoint insertion theorem gives its vacuum Psi(1/b), both full domains and commutation with Z,Z*.
The quotient b_n/b tends to one strongly in L2, dominated by a constant multiple of b inverse squared in the squared norm.
Its Hilbert--Schmidt commutator limit is therefore P.
The same actual-adjoint matrix-element passage gives the all-bounded-vector T commutator.

Negating these normalized operators produces the generator-first strong duals.
No supplied target A or unknown target-to-reference extension has been used in this construction.
This establishes item 3 implies item 2 directly.

## 4. Strong duals, original closures and complex vacuum formulas

The target pair is normal and generates its intrinsic algebra.
Strong S puts Omega in the actual adjoint domain of each dual.
C_F0070 Part C therefore supplies the represented starred derivations and actual vacua.
Its assumptions match precisely; the inference is not from bare F alone.
This proves item 2 implies item 1.

For the constructed operators, the value at 1 is zero.
On the original target core their generator and starred-generator commutators agree with the unique normal derivations, so induction on words identifies their restrictions with the canonical contractions.
The established core bounds, actual target adjoint pairings and bounded original-core graph approximation give the original target closures on all M.
No equality of maximal and minimal divided-difference domains, or closure of a formal sum, is substituted for this step.

On the positive side the complete vacua are xi_N+chi_b and Psi(1/b).
Their actual values are determined on the dense target core.
Under the phase unitary U, the first-chaos vector 1/b becomes theta/b=a/(b^2)=1/conjugate(a), while the degree-two component becomes theta(z,w)theta(w,v)chi_b.
The degree-zero vector xi_N is unchanged.
These orders and conjugates agree with the direct linear moment equation a conjugate(psi_H1)=1.
Substituting a directly into the positive ratio expression would generally be wrong; the fixed statement correctly uses phase transport instead.

The quantitative bounds survive because the automorphism preserves the operator norm and U preserves every Hilbert norm.
Zero sets have already been excluded wherever these formulas use inverse coefficients.

## Source and verification limits

The full C_F0156 fixed proof was read to distinguish its initial actual-vacuum moment extraction from its later constructive and weak-domain arguments.
Its separate R_F0164 supplies the independent complete review of that theorem and seven inputs.
The present review does not re-audit all external sources behind those accepted interfaces.
C_F0153 is consumed only at its explicitly proved arbitrary-abelian-base finite-relative-degree scope; its separate finite separated-block application is not extended by assertion.
C_F0070 is consumed at Part C and the normal uniqueness interface.

The reviewer's earlier C_F0145 contribution remains development provenance, and no independent status for it is inferred from this record.
There was no consultation of D_F0002, numerical experiment, new source theorem, formal proof, or author correction used to close a gap.

## Conclusion

**Pass: complete fixed C_F0157 v1 independently reviewed.**
The full statement, all four proof sections and the three exact direct inputs are covered, including the actual measurable phase automorphism, intrinsic zero-set exclusion, both directions of the integrability criterion, sufficiency without supplied target A, actual original canonical domains and phase-correct complex vacua.
No mathematical correction was found.

The accepted scope is A iff S iff the stated three analytic conditions in the bounded measurable Hermitian Gaussian class.
These conditions imply F.
A converse from bare F, an unrestricted correlated-normal theorem and the general A-to-F implication remain outside the result.
This is not a Task completion review.
