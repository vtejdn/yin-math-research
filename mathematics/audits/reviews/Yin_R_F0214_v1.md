---
author: Yin
---
# Independent review of gluing dual systems across two central summands

The review act took place at 2026-11-13T13:28 UTC under Yin's authorship.
An agent outside proof development inspected the fixed [C_F0206 v1 candidate](../../claims/Yin_C_F0206_v1.md#decision-candidate) dated 2026-11-13T13:22.
The agent received the claim and the names of its required inputs, with no proof-development discussion, draft, author explanation or previous verdict on this claim.
The two declared dependencies were available with their own historical assessments.
Their use here was checked at the mathematical interfaces specified below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finding) | [C_F0206 v1 statement](../../claims/Yin_C_F0206_v1.md#statement) | Quantifiers on the derivations and the central projection, the two equivalences, separated single spectra and the circular example. |
| [Whole-proof finding](#finding) | [C_F0206 v1 argument](../../claims/Yin_C_F0206_v1.md#argument) | All four proof sections, including signs, trace normalization, domains and the represented mixed-block derivation. |
| [Whole-proof finding](#finding) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Tracial coarse tensor convention and its intertwining with composition on Hilbert--Schmidt operators. |
| [Whole-proof finding](#finding) | [C_F0074 v1 statement](../../claims/Yin_C_F0074_v1.md#statement) | One bounded nonnormal circular generator with an actual ACSY derivation and a bounded generator-first dual. |
| [Whole-proof finding](#finding) | [T_F0011 v1 definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | The full represented star domain and actual vacuum for \(\mathsf A\), and the distinct bounded-vector domains and commutator required for \(\mathsf F\) and \(\mathsf S\). |

## Graph closure and the two mixed blocks

For \(a,b,x\) in the polynomial star algebra, the middle term of \(\langle1\otimes1,\delta(a^*xb^*)\rangle\) is \(\langle a\otimes b,\delta x\rangle\) with the stipulated inner product.
The end terms test \(\delta(a^*)\) and \(\delta(b^*)\) against \(1\otimes b x^*\) and \(x^*a\otimes1\), respectively.
Their norms are bounded by \(\|b\|\|x\|_2\) and \(\|a\|\|x\|_2\).
Together with the vacuum bound on \(a^*xb^*\), these tests put a dense algebraic tensor product in the adjoint domain.
This also checks why the familiar dense-adjoint-domain argument for a free difference quotient works for these Hilbert-tensor-valued derivations without a reality condition. [Voiculescu, Section 4.1 and Corollary 4.2](../literature/Voi98/Yin_U004.md#adjoint-domains-and-closability-41-43)

For the central \(C^*\)-projection, selfadjoint norm approximation followed by compression gives the two disjoint real spectral intervals.
On their containing interval the sup norm of a divided-difference error is at most the sup norm of the derivative error, including at coincident spectral values.
The joint functional calculus for the commuting outer actions on the tensor space therefore gives graph convergence of the polynomials.
For a projection given in the closed domain, convergence of \(x_n\) in \(L^2\) and convergence of \(\delta_i x_n\) in the coarse space suffice, since the differentiated commutator involves \(x_n\) on the vacuum tensor and bounded multiplication by the fixed \(X_j\) on \(\delta_i x_n\).
The input commutators tend to zero, so closability forces their limiting derivatives to vanish.
The resulting equation uses \(K_{12}\) for the \(12\) block and \(-K_{21}\) for the \(21\) block, with positive generator-first commutator in both cases.

## Dual domains and trace weights

The rank-one map \(h\mapsto u\,\tau(vh)\) has Hilbert--Schmidt norm \(\|u\|_2\|v^*\|_2\), and polarization gives the indicated tensor isometry.
Precomposition by \(L_z\) changes \(v\) to \(vz\), and postcomposition changes \(u\) to \(zu\).
Thus the mixed tensors supply bounded operators \(H_b\to H_a\) whose generator commutators are exactly the mixed vacuum blocks \(h\mapsto t_b\tau_b(h)e_a\) when \(i=j\), and zero otherwise.
The intrinsic corner commutator follows by dividing the compressed diagonal by \(t_a>0\).
For adjoint tests in \(M_a\) both inner products are rescaled by the same constant, giving \(t_a^{-1}e_aD_i^*h\) for the adjoint of the corner restriction.
Conversely the assembled diagonal \(t_aD_i^a\) has the ambient vacuum coefficient, and the two bounded mixed blocks admit bounded adjoints on the opposite blocks.
This proves the adjoint-domain inclusion wherever \(\mathsf S\) calls for it and uses only linearity on bounded vectors in the \(\mathsf F\) construction.

## Separated spectra and the example

Positive distance between the compact spectra permits an oriented grid boundary with the stated indices, including when one spectrum surrounds a component of the other.
The resolvents belong to the generated unital \(C^*\)-algebra by inverse closedness, and their contour integrals give the central units and hence recover both generated summands.
Writing \(R_a=(z-X^a)^{-1}\), the difference of the two resolvent products in the tensor Sylvester equation is \(R_a\otimes e_b-e_a\otimes R_b\).
Its integral gives \(e_a\otimes e_b\) for either ordered pair using the contour belonging to the first index.
The bounded-operator contour formula and these index conventions agree with [Nevanlinna, Theorem 1.2, arXiv:1904.07549v1](https://arxiv.org/pdf/1904.07549#page=3).
The direct tensor calculation suffices for existence of the required mixed solution.

The coordinate map \(w\mapsto w_a\) sends represented star polynomials to represented corner star polynomials.
On a mixed component, expansion of \((uv)_ak_{ab}-k_{ab}(uv)_b\) gives the outer product rule with the two intermediate terms cancelling.
At \(X\) all four components sum to the full vacuum tensor.
For a diagonal vacuum test the product of the inherited inner-product factors is \(t_a^2\).
For a mixed test the two simple tensors moved onto the vacuum have norms \(\sqrt{t_b}\|w_a\|_{H_a}\) and \(\sqrt{t_a}\|w_b\|_{H_b}\).
Summing the four bounded functionals on the dense represented star domain gives actual vacuum-adjoint membership.

In the circular input the right-deletion combination \(E\) satisfies \([E,c]=P_\Omega\), the representing vector of the derivation vacuum is \(E^*\Omega\), and \([c,c^*]\Omega\ne0\).
The bounded dual is \(-E\).
Real scalar translation preserves all three identities and moves the spectrum by the same scalar.
The strict separation \(\lambda>2\|c\|\) and positivity of both weights yield a nonzero proper central projection while the assembled dual is bounded on the full Hilbert space.

## Finding

The whole fixed argument proves the stated two-summand implications and the separated-spectrum example at the exact three Task definitions.
The known Sylvester formula has the indicated source and sign, and the two declared mathematical inputs supply the interfaces used.
The unrestricted implication from \(\mathsf A\) to \(\mathsf F\) and estimates across infinitely many summands lie outside this finding.
