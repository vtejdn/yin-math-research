---
author: Yin
---

# Independent review of the uniform slice bound at bounded product density

## Finding

On 2026-11-16T17:21 UTC a reviewer outside proof development independently examined the [candidate decision](../../claims/Yin_C_F0316_v1.md#decision-candidate) dated 2026-11-16T17:17.
The reviewer received the fixed proof and the requested scope without development dialogue or a previous finding on this candidate.
The proof establishes (1) for all polynomial contractions at either coordinate in both orientations, under the stated full actuality hypothesis.

The measurable inverse preserves the individual marginal algebras, and the correlated Haar theorem supplies exchange, the actual product vacuum and the transfer to the core with omitted \(Y\).
In the non-Haar case the phase criterion supplies the finite \(J\) and the exact squared vacuum norm \(s^2=\|\xi_\mu\|_2^2+\|H\|_2^2J\).
The separate Haar case already has \(k\le3\).

For a Laurent polynomial \(b\), the Abel expansion of \(rw/(z-rw)\) selects strictly negative output frequencies.
The Lipschitz bound for \(b\) and \(|z-rw|\ge\sqrt r\,|z-w|\) justify passing to the limit in the difference integral.
Convergence of the Abel projections in \(L^2(m)\) implies convergence in \(L^2(\nu)\) with factor at most \(\sqrt L\).
Moving the negative projection to the positive one in the bilinear Haar pairing and testing against Laurent polynomials identifies \(H^*=P_-\rho-P_+\rho\) in \(L^2(\nu)\).
The bounded part of \(D\) then has norm at most \((L+1)/2+L\) on \(L^2(\nu)\), since multiplication by \(\rho\) into \(L^2(m)\) and restriction back to \(L^2(\nu)\) each have norm at most \(\sqrt L\).
Multiplication by \(\rho\) annihilates changes of representative on its zero set.
Centering both input and output preserves this Hilbert bound for \(R_1\).
For \(R_2\) centering the input costs at most two in supremum norm, which cancels the factor one half and gives the bound \(\|H\|_2\) into the centered output space.

Expanding the difference of the two scalar soft slices in (3) cancels their diagonal terms and leaves exactly \(O_{k_\epsilon}\).
The uniform scalar column estimate for bounded marginal inputs therefore gives \(6(2+\sqrt2)\|\xi_\mu\|_2\) for this kernel operator, including multiplication of the inputs by the measurable unimodular function \(\bar h\).
In the terminal-word formula the scalar mean \(\tau(Db)\) gives cost \(2\|H\|_2\|k_\epsilon\|_2\).
The centered-map proof applies separately to \(R_2\) since it kills constants, has centered range, and is bounded on continuous functions of \(V\) in supremum norm.
The commutative finite-family estimate and the terminal coefficient bound two give \(2\sqrt{4/\pi}\|H\|_2\|k_\epsilon\|_2\) for its contribution.
Bounded separated approximants to the fixed cutoff symbol converge in the inner spectral calculus and in kernel Hilbert norm, as required by these estimates.

For the \(R_1\) term, appending a centered noise letter and then an arbitrary terminal base letter gives the reduced-word Hilbert tensor isometry.
It yields \(\mathbb E_A((u_\alpha b_i)^*(u_{\alpha'}b_{i'}))=\delta_{\alpha\alpha'}\delta_{ii'}1\) for orthonormal families of the indicated prefixes and centered noise letters.
Thus the positive sum of squares of the bounded terminal coefficients of a column is at most its conditional expected squared modulus.
After applying \(O_{k_\epsilon}\) to these coefficients, the action on the noise leg is \(R_1\otimes I\).
The squared norm before this action is the sum over all indices of the squared norms of the \(O_{k_\epsilon}\) outputs, by orthonormality of the input noise vectors.
This proves the tensor estimate without requiring their images under \(R_1\) to be orthogonal and gives cost \(3(2+\sqrt2)(3L+1)\|\xi_\mu\|_2\).

The reference cutoff contributes at most \(36\|\xi_\mu\|_2\) on the rotated target core, including graph approximation of the phase.
Taking the strong cutoff limit on each fixed finite column is valid on the diffuse marginal coarse correspondence.
Since \(\|k_\epsilon\|_2\le\sqrt J\), division by \(s\) yields the displayed constant \(38+2\sqrt{4/\pi}+3(2+\sqrt2)(3L+1)\).
Conjugating the adjoint tuple replaces \(\rho\) by its reflection and preserves the two energy terms, and exchange gives the same estimate at the other coordinate.
The normal slice agrees with the original slice on the reparametrized core by bounded strong-star approximation of the omitted variables.
For the uniform law of a measurable set the density bound is the reciprocal of its Haar mass.
This applies (1) under the same actuality hypothesis, including for sets with a spectral hole.
The review checked the three direct results at their cited interfaces.
Uniformity as the density bound tends to infinity remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0316_v1.md#decision-candidate) | Entire fixed decision including the three declared dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0316_v1.md#statement) | Density and actuality assumptions, both coordinates and adjoint orientations, the explicit uniform constant, full polynomial unit ball and measurable-set examples. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0316_v1.md#argument) | Abel projection formula, distinct bounds for both centered terms, terminal tensor and module decomposition, cutoff removal and original-core transfer. |
| [Finding](#finding) | [Correlated Haar model](../../claims/Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Actual product vacuum, energy norm, Haar comparison, normal transfer to the reparametrized core and exchange. |
| [Finding](#finding) | [Weighted phase estimates](../../claims/Yin_C_F0265_v1.md#argument) | Centered and scalar terminal bounds, measurable-kernel passage, reference term and adjoint orientation. |
| [Finding](#finding) | [Scalar bridge](../../claims/Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Uniform column cost on bounded scalar inputs for the soft slice and its kernel formula. |
