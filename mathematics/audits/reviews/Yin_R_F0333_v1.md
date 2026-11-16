---
author: Yin
---

# Independent review of Hilbert-kernel estimates under spectral domination

## Finding

On 2026-11-16T17:57 UTC a reviewer outside proof development checked the [candidate decision](../../claims/Yin_C_F0326_v1.md#decision-candidate) dated 2026-11-16T17:54.
The reviewer received the fixed material and scope without development dialogue or earlier findings on this candidate.
The proof establishes (2), (3), the curvature criterion (4) and its obstruction in the [standing finite tracial setting](../../tasks/Yin_T_F0011_v1.md#original-question-and-mathematical-setting).
The reviewed statement explicitly assumes a faithful normal probability trace, as required in the marginal adjoint input and in the passage from bounded strong convergence to convergence in trace Hilbert norm.

For real symmetric \(q\), the two correction terms in the marginal adjoint formula agree, hence \(\|\eta_q\|_2=\|q\|_{L^2(\nu_\zeta)}\le m\|q\|_2\).
The entire Hilbert kernel is a permitted insertion on a core word, since the word expansion has a finite number of bounded outer multipliers.
For fixed strict selfadjoint \(h\), the norm-convergent differentiated power series bounds both analytic signs by \(C_h\|q\|_2\).
This bound is uniform in the kernel with the test fixed.

For a nonzero finite bounded symmetric tensor, its integral operator is selfadjoint and the composition powers remain finite bounded symmetric tensors.
The Hilbert–Schmidt ideal inequality gives \(\|q^{\circ k}\|_2\le\|q\|_2^k\).
Dividing (B6) at \(k=2^j\) by \(\|q\|_2^{2k}\) therefore gives \(w_j^2\le2(m+1)w_j+w_{j+1}\) for the indicated normalized slice norms.
Their supremum \(W_*\) is finite by the fixed-test bound.
Taking suprema yields \(W_*^2\le(2m+3)W_*\), including \(W_*=0\), proving the first constant starting at \(j=0\).
Symmetric finite partition approximants converge also in the vacuum-weighted norm under (1), and the analytic test values converge by the same fixed-test estimate.
Averaging both signs recovers a selfadjoint contraction after dilation, and splitting a general element into real and imaginary parts gives \(2(2m+3)\).
The actual core adjoint formula gives the further constant \(5m+6\).
Bounded core approximation, weak compactness of the outputs and weak closedness of the two graphs give both domains on \(M\Omega\) for the weighted right slice \(E_q\).
Real Hilbert duality on symmetric kernels gives its real symmetric signed density for \(F_q(u)\), with the negative part bounded in the same Hilbert norm.

For centered real \(k\), the row of \(a=k\otimes k\) vanishes identically and \(a\circ a=\|k\|_2^2a\).
With the second argument of the inner product linear, (B0c) contributes \(+\|k\|_2^2 F_a(u)\) to \(\operatorname{Re}\langle u,C_a u\rangle\).
Equation (B0e) subtracts that quantity, giving \(\|k\|_2^2F_a(u)=\|k\zeta k\|_2^2-\|E_au-u k\zeta k\|_2^2\).
This is the upper bound needed when subtracting the centered square.
The projection-square formula, with the opposite placement of the square, supplies \(F_{e\otimes e}\ge-\|e\zeta e\|_2^2/t\).
In the polarization at \(k=e/t-f/s\), disjointness gives \(\|k\|_2^2=1/t+1/s\).
The two diagonal coefficients \(ts/t^2,ts/s^2\) give precisely the two cubic trace denominators after extracting \(ts\) in (3).
All these kernels are bounded finite tensors, so the block estimate requires no spectral domination and allows arbitrary positive \(t,s\) with \(e\perp f\).

For (4), the finite positive block sums \(q_N\) have lower bound \(-L\) on both analytic signs, including for overlapping blocks.
The real symmetric remainder has lower bound \(-(2m+3)\|b\|_2\).
The inequality \(|z-v|\kappa\le2\) and Jensen give \(\||z-v|g\|_2^2\le4\iiint\kappa^2\,d\mu^3\), and compact support gives square integrability of the gap times \(b\).
The nonnegative partial sums are bounded by \(g+|b|\).
Consequently multiplication by the gap or its conjugate gives convergence of the two generator tensors in the coarse Hilbert norm, even if \(g\) is outside \(L^2(\mu^2)\).
Finite outer Leibniz expansions and the analytic series then identify their limit with the matched curvature form on each permitted unitary.
The signed mixed-energy inequality uses \(-F_g/2\), so this lower bound controls the two real component slices and hence both oriented original coordinate slices on polynomial contractions.
The exchange identity gives the same bounded negative difference when both matched forms are controlled, because its remaining nonnegative term is at most \(4\|\xi\|_2^2\).
Taking an empty block sum yields the \(g\in L^2(\mu^2)\) consequence.
The review checked the five declared dependency interfaces and the spectral-domination hypothesis of the restricted exchange construction.
A universal finite-cost conclusion for that class remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0326_v1.md#decision-candidate) | Complete candidate in the standing faithful normal probability trace setting and its five declared dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0326_v1.md#statement) | Hilbert-kernel and density bounds, weighted-slice domains, unequal-trace block estimate, curvature criterion and deficiency obstruction. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0326_v1.md#argument) | Bounded composition recurrence, centered square sign, domain passage, positive block sum and convergence of both gap tensors. |
| [Finding](#finding) | [Marginal adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Weighted Hilbert graph, symmetric vacuum and actual weighted-slice adjoint on the original core. |
| [Finding](#finding) | [Finite-kernel energy](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | (B6) at every normalized composition power, (B0c) and (B0e) on both analytic signs, and the fixed-test bound. |
| [Finding](#finding) | [Projection square](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower bound with the individual trace on each measurable positive diagonal block. |
| [Finding](#finding) | [Signed curvature](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Coarse gap limit and mixed-energy inequality with defect \(-F_g/2\) controlling both coordinate orientations. |
| [Finding](#finding) | [Exchange energy](../../claims/Yin_C_F0314_v1.md#statement) | Matched-sum identity and the bound on its remaining positive inner term. |
