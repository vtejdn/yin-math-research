---
author: Yin
---
# Complementary whole review of vacuum converses and mixed duals

Review performed and recorded: 2026-10-14T11:17.
Human record author: Yin.
Method: separately organized AI mathematical review with the component contributions and review arrangement disclosed below; no personal human inspection is claimed.

## Arrangement and exact inputs

The audit_acsy_nonnormal reviewer first reread the published ACSY24 PDF, pp.34--36, and the entire existing ACSY24-U001 reconstruction and review.
It then received the proposed spectral-partition argument from the full_acsy_counterexample author, checked the working argument read-only, and subsequently read the complete fixed [C_F0071 v1](../../claims/Yin_C_F0071_v1.md) and [C_F0071 v2](../../claims/Yin_C_F0071_v2.md).
The exact accepted candidate covered below is v2, dated 2026-10-14T11:14, Parts A--E and the complete Argument including the added mixed reverse implication.

The partition lemma and real/selfadjoint application were developed by the other author; root proposed the scalar-normal, affine and mixed-reverse extensions.
The reviewer independently checked their written arguments and did not edit either fixed Claim.
After its initial checks, this reviewer proposed the unitary-forward twist.
Accordingly that component is not represented as an independent discovery or an entirely noncontributing review by this same agent.
Root separately checked the written unitary-forward construction, its bounded contraction, inverse-vacuum identity and actual adjoint conclusion, and communicated the successful independent component check.
The conclusion below uses these complementary checks: this reviewer covers the partition, real/selfadjoint, scalar, affine and mixed-reverse arguments; root supplies the separate check of the unitary-forward contribution.
Shared candidate dialogue and author explanations were available.
The arrangement is not a blind review.

Previously accepted inputs are reused at their actual scope: C_F0069 Part A and its R_F0042 review; C_F0070 Part A and R_F0043; the scalar statement of C_F0055 and R_F0037; C_F0043 Section 3 and its [original closed-curve finding](Yin_R_F0075_v1.md#scope-of-acceptance); Dab10-U002; and the MSY23 finite-cycle interface.
Their relevant statements and applications were checked.
This is not a recursive new review of their entire upstream proof chains.

## Current relationship clarification

The original dated independent/complementary wording below is preserved as the historical account.
The current C_F0071 whole finding is self-reviewed: the reviewer proposed the unitary-forward twist and shared candidate dialogue and author explanations were available; the author's complementary component check is not an isolated whole-proof review.
This is an actual mathematical contribution, not an inference merely from a supplied fixed proof.
For the separate ACSY24 source finding, the reviewer first read the existing reconstruction and review; the retained arrangement does not establish an isolated initial source-proof context, so that exact relationship is unknown.

## Review relationships

| Review | Relationship |
| --- | --- |
| [C_F0071 conclusion](#conclusion) | self-reviewed |
| [ACSY24 no-normality finding](#acsy-no-normality) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [C_F0071 conclusion](#conclusion) | [C_F0071 v2 Statement](../../claims/Yin_C_F0071_v2.md#statement) | Exact Parts A--E, actual adjoints, density, existential equivalences and unresolved general scope. |
| [C_F0071 conclusion](#conclusion) | [C_F0071 v2 Argument](../../claims/Yin_C_F0071_v2.md#argument) | Entire argument, including full mixed reverse, with complementary independent component checks disclosed above. |
| [C_F0071 conclusion](#conclusion) | [C_F0069 Part A](../../claims/Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H continuity for a bare full-domain dual with a normal diagonal coordinate. |
| [C_F0071 conclusion](#conclusion) | [C_F0070 Part A](../../claims/Yin_C_F0070_v1.md#statement) | Scalar normal starred derivation, diffuseness and exact canonical-core agreement only. |
| [C_F0071 conclusion](#conclusion) | [C_F0055 scalar input](../../claims/Yin_C_F0055_v1.md#statement) | Nonatomic scalar normal law, actual vacuum and canonical bounded-vector domains; no mixed/free-tuple conclusion is imported. |
| [C_F0071 conclusion](#conclusion) | [C_F0043 Section 3](../../claims/Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Real unitary twist, defect, energy identity, analytic-unitary approximation and canonical operator reconstruction, rechecked for the mixed adaptation. |
| [C_F0071 conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002_v1.md#dab10-u002) | Accepted selfadjoint finite-Fisher contraction and graph-domain implication; no attribution of the mixed theorem to the printed source. |
| [C_F0071 conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Actual vacuum interface and Proposition 3.5 used for scalar nonatomicity, with the source reconstruction rechecked below. |
| [ACSY24 no-normality finding](#acsy-no-normality) | [ACSY24-U001](../literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Published Section 3.2 definition, Theorem 3.4, Proposition 3.5 and the entire local regularization reconstruction; no normality or reality premise. |

## Partition and real-derivation checks

The abstract form identity makes phi norm-continuous by setting a=1 and Hermitian by conjugating and exchanging a,b.
For a selfadjoint element, a finite continuous square partition on its real spectrum can be chosen with at most two nonzero functions at every point.
The number of functions may grow; the overlap bound does not.
The pointwise estimate for every sign choice is at most sqrt(2), so the Hilbert-space sign identity yields sum ||E h_j||_2^2 <= 2 C^2 without a dimension factor.

The weighted square sums converge uniformly to a, and their squared-weight sums converge uniformly to a^2: the second error is bounded by epsilon times 2||a||+epsilon.
Pairing each h_j with itself, applying Cauchy--Schwarz to the finite sum, and then using norm continuity gives the claimed 2 sqrt(2) C L2 bound for selfadjoint a.
Hermitian phase rotation proves the same constant for arbitrary a.
No spectral projections, weak continuity of E, Hilbert-space closability or extension of the form identity to all M is assumed.

For a real derivation, the two contractions obey F(a*)=(Ea)*.
The outer Leibniz rule therefore gives exactly the symmetric-form identity; bounded partial traces and multiplication by the fixed bounded coefficients justify it even for Hilbert-valued, nonalgebraic derivative tensors.
Norm approximation extends that identity only to B=C*(A), which is sufficient.
Density of A Omega in H is explicit in v2, so the resulting functional estimate is precisely membership of 1 tensor 1 in the actual Hilbert adjoint domain.
Coassociativity is not used for this converse.

## Selfadjoint, scalar and affine applications

For a bare selfadjoint tuple, apply C_F0069 Part A separately to the diagonal relation for each -D_i and then normalize.
The fixed L2 vector D_i(1) contributes a bounded M-to-H multiplication map.
Finite product commutator expansions give finite-rank operators on the represented polynomial algebra.
If two words evaluate equally, their commutator extensions agree on the dense bounded-vector domain; injectivity of Theta makes the tensor independent of the presentation.
Thus the derivation exists before invoking the new vacuum result.
Reversal of selfadjoint words gives reality.
The identity E_i1=0 identifies E_i with its right contraction.
The result is a joint vacuum on all words, not merely separate marginal conjugate variables.

The selfadjoint reverse uses the exact accepted Dab10-U002 estimate and canonical weak-graph argument.
C_F0070 Part B is a consistent comparison interface, not an unproved assertion of a full-domain extension.

In the scalar normal case, the divided difference of a starred polynomial is bounded on a compact spectral square.
The kernel is symmetric under exchanging its two variables, without complex conjugation.
Therefore F=E and the bilinear square identity holds on C*(x).
The same partitions yield 2 sqrt(2) C on selfadjoint inputs; splitting into real and imaginary parts and using ||a||_2^2+||b||_2^2=||a+ib||_2^2 yields 4 C on all inputs.
No false reality assertion is made.
For the reverse direction, maximal Delta excludes a spectral atom by the rank-one finite-cycle test; the normal relation then forces the divided-difference derivative, since multiplication by z-w has trivial kernel for a nonatomic product law.
These facts match all hypotheses of the accepted C_F0055 scalar theorem.

For X=A S+b, the common represented star algebra is unchanged.
The inverse indices D_i^X=sum_k (A^{-1})_{ki}D_k^S and D_k^S=sum_i A_{ik}D_i^X give the required Kronecker commutators.
The same coefficient transformations apply to derivations.
Finite linear combinations preserve actual vacuum-adjoint membership.
This application genuinely includes some nonnormal tuples and makes no claim about arbitrary nonnormal tuples.

## Unitary forward and mixed reverse checks

The generator inverse identity gives the correct starred commutator -delta_ij U_j* P U_j*.
For a distinguished selfadjoint coordinate the induced derivation is real even when other coordinates are unitary, because all their derivatives and starred derivatives vanish.

For a distinguished unitary coordinate the forward right twist beta=i delta#(1 tensor U) has beta(U)=i 1 tensor U and beta(U*)=-i U* tensor 1.
It is real on the entire core.
Its contraction is i(E(aU)-aE(U)), with E(U)=1, and hence has norm at most ||E||+1.
The vacuum-transfer calculation is

    phi_beta(aU*) = i phi_delta(a) - i tau(aU*).

Thus phi_delta(a)=-i phi_beta(aU*)+tau(aU*), with the claimed norm bound.
Root independently checked this component, including the actual L2-adjoint meaning; the reviewer's earlier proposal of the twist is disclosed above.
The written proof does not invoke an uninspected full tensor-adjoint theorem from ACSY24 Lemma 3.3.

For the mixed reverse, ACSY24's derivative values on every starred generator are algebraic tensors.
Product induction supplies A tensor_alg A for all words.
In the unitary case the reverse uses the distinct left twist i I_(U tensor 1)theta.
The direct vacuum identity i(phi_theta(Ua)-tau(a)) is correct by traciality.
The general tensor-adjoint formula

    beta*(a tensor b)=a zeta b-(Ea)b-a(Fb)

follows from the vacuum pairing on a* p b*, with the order and conjugations retained.
It places algebraic tensors in the actual adjoint domain; density proves closability.
Its b=1 specialization gives E*p=p zeta-Ep.

The triple derivation defect is zero for a distinguished selfadjoint coordinate and i kappa beta for a distinguished unitary coordinate.
The two cross product terms cancel, and the generator checks are unchanged by the types of the zero-derivative coordinates.
The contracted defect formula and both lines of the displayed norm identity were checked with the declared inner product convention.
In particular the term involving i epsilon Ep is retained and bounded; it is not discarded as formally imaginary.

The analytic square-root series for a strict selfadjoint contraction converges together with its differentiated series.
All terms of the final energy identity therefore have legitimate limits.
The product derivative converges, and closability identifies the derivative of u*u=1 as zero.
This yields the stated 4||zeta||_2+2 epsilon and 5||zeta||_2+2 epsilon bounds.
For a unitary coordinate, N=-i rho(U*)E and N*p=i E*(pU) have the correct scalar conjugation and preserve the core.

Finally, bounded polynomial approximants to each element of M give weakly relatively compact outputs.
The actual closed graph is weakly closed, so this yields membership in the canonical closure, not an unspecified Banach-space extension.
The same reasoning applies to the actual adjoint.
Uniqueness of every weak cluster value gives weak convergence of the original bounded net; applying it also to X_j p_alpha passes the commutator identity to all M Omega.
The sign reversal then gives a generator-first full-domain dual.
This completes the mixed reverse without assuming mutual commutativity or freeness.

<a id="acsy-no-normality"></a>
## ACSY24 no-normality finding

The published [ACSY24 PDF](../../literature/pdf/ACSY24.pdf), pp.34--36, was text-read directly in this review.
The definition requires a weakly dense star algebra and a Hilbert tensor codomain.
Theorem 3.4 explicitly explains why the argument written originally for selfadjoint variables remains valid on a dense star algebra.
Proposition 3.5 lists arbitrary bounded generators, normalized derivations on C<X,X*> and actual vacuum adjoints.
Neither normality nor reality is imposed.

The entire ACSY24-U001 reconstruction was checked again.
Star closure supplies both original and adjoint-generator bounded HS commutators.
Graph approximation gives invariance of Dom closure(D) under every a in A; adjoint pairing with a* gives invariance of Dom D* and [D*,a]=-T_(a*)*.
Consequently the selfadjoint doubling and its bounded HS block commutator are valid for nonnormal X_j.
The resolvent signs and coefficients in the bounded regularization identity are correct.
Strong convergence of the uniformly bounded selfadjoint resolvent factors gives the asserted HS convergence by finite-rank approximation.
The final products are bounded finite rank, their trace limits are justified, and the two independent commutant vacuum tests force every finite-rank cycle to vanish.

The source's final affiliation shortcut on p.36 is not sufficient if it is read as claiming that these canonical duals belong to U(M).
Indeed a closed operator affiliated with M that annihilates Omega would annihilate the dense set M' Omega and therefore be zero, contradicting its nonzero dual commutator.
The local regularization avoids this premise.
The outcome is that Proposition 3.5 is supported at its full nonnormal scope by the audited reconstruction; no normality has been silently used to repair that abbreviated source step.
The source's original cited proof chains are not newly audited, and no all-M domain conclusion follows from this regularization.

## Conclusion

The complete C_F0071 v2 Parts A--E and their full argument pass the complementary independently organized review described above, with no required mathematical correction.
If adopted by its responsible author, this exact finding supports proved / independently reviewed for v2.
The new conclusions establish equivalence for selfadjoint tuples, all mixed selfadjoint/unitary tuples, one arbitrary normal generator, and invertible complex affine reparameterizations of selfadjoint tuples.
They do not settle either implication for arbitrary correlated normal tuples or arbitrary general tuples, and they do not identify every supplied full-domain operator with a canonical closure on all M.

The separate source finding confirms the previously audited nonnormal scope of ACSY24 Proposition 3.5 and the need to distinguish the local regularization from the printed affiliation shortcut.
Source completeness is limited to the exact accepted interfaces and bounded search records stated here; no novelty, priority, formal verification, manuscript revision or completion of the general comparison is claimed.
