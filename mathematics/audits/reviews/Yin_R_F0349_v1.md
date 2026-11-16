---
author: Yin
---

# Independent review of the lattice curvature graph certificates

## Finding

On 2026-11-16T19:45 UTC a reviewer outside development of this proof independently checked the candidate dated 2026-11-16T19:43, including the entire statement, argument and four declared dependency targets.
The reviewer received the fixed candidate and its scope without development dialogue or an earlier finding on it.
The exact diagonal completion, both sufficient certificates and the resulting bounds on the full polynomial unit ball follow under the finite-label model assumptions. [Candidate](../../claims/Yin_C_F0345_v1.md#decision-candidate)

The actual vectors at pivot \(\ell\) have \(\|w_\ell\|=1\) and \(Y_{\ell\ell}=w_\ell\) by vanishing of the inserted diagonal and diagonal vacuum.
For distinct nonpivot indices the polarized energy gives a normalized two-vector term \(s_{\ell i}+s_{\ell j}-s_{ij}\).
The two cross terms with \(w_\ell\) cancel its first two summands, and using \(V_{\ell\ell}=0\) gives \(1-s_{\ell i}\) directly on an edge meeting the pivot.
Since \(f_{ii}=0\), this proves the stated positive Gram correction of \(X\) and its lower diagonal bound.
Expanding its diagonal gives \(t_\ell d_{\ell i}=\|V_{\ell i}\|^2-2t_i f_{\ell i}\).
The paired norm identity and symmetry of \(f,\nu\) then give \(2\nu_{i\ell}\) upon adding the reverse edge.

Testing positivity against a real positive semidefinite matrix at each pivot gives the upper bound on minus the sum of the trace pairings with \(X\).
On one edge use the larger of the two normalized diagonal coefficients times \(2\nu_{i\ell}\).
The subtracted excess times the other directed correction is bounded above by the coefficient difference times \(t_i t_\ell\max(t_i,t_\ell)\), because each \(d_{\ell i}\ge-t_i^2\).
The pivot diagonal contributes zero for every pivot size.
The inverse-gap term is in the budget, and each annulus of radius \(2^jh\) contributes at most \(2^{1-j}M_i/h\) to the scalar inverse-square sum.
Using \(t_i/h\le M_i\) gives the required scalar correction.
For the two-label comparison each separate normalized row constraint has diagonals \(1,5\), up to order, and off-diagonal entry 2, hence determinant 1.
Both nonpivot squared norms would have to be at least 4 by pairing with their pivot unit vectors.
The directed identity instead requires \(\theta_{12}+\theta_{21}=4\), less than the necessary 6.
This verifies the strict comparison of the algebraic row constraints at the stated abstract-data scope.

For the Cauchy identity a translation and complex dilation put the first two sites at 0 and 1.
Substitution gives \(4(\operatorname{Im}c_\ell)^2/(|c_\ell|^2|1-c_\ell|^2)\) on each side with the same inverse-square scaling.
The repeated indices missing from the curvature sum contribute \(2(t_i+t_j)|k_{ij}|^2\) to the off-diagonal of \(K+R\).
The real Gram rows defining \(R\) are positive and their nonpivot diagonal is exactly \(t_\ell|k_{\ell i}|^2\).
The weighted graph square shows that each \(L(a)\) is positive and kills \(t\).
The row sums against \(t\) are \(H_i\) and \(3H_i\) for the two Cauchy Gram matrices, giving the factor \(1+9=10\) on the diagonal completion.
Assigning each edge of \(L(b)\) to its smaller-mass endpoint bounds the unique nonpivot entry there by \(4t_\ell/|c_i-c_\ell|^2\), with no accumulation at fixed ordered pair.
Under (2) the sum of the positive pivot matrices therefore equals \(\Lambda-K\) with the required diagonal bounds.
As \(F_K=t^{\mathsf T}Kt-\operatorname{tr}(KX)\) and \(X_{ii}=t_i^2\), inequality (5) gives the stated lower bound with its indicated sign.
A universal constant in (2) would give the unrestricted normal converse through the lattice equivalence.

For a subset \(S\), the weighted row products have off-diagonal sum \(-\lambda_S\) and each row kills \(t\).
These two facts determine the full graph matrix because all masses are positive.
At a nonpivot in \(S\) the diagonal of an individual summand is \(t_\ell\lambda_S/t(S)\), so the sum obeys the first quantitative bound in (3).
For a signed remainder \(w=e+b\), the two-entry matrix has nonnegative diagonal, determinant zero and off-diagonal \(-w\).
The smaller-mass assignment bounds its nonpivot diagonal by \(2(2+C_2)t_\ell/|c_i-c_\ell|^2\).
Its quadratic form on \(t\) is \(2t_it_j(|w|-w)\) per edge, bounded in sum by the same annular estimate.
This accounts for the change of diagonal and proves the lower bound with linear dependence on \(1+C_1+C_2\).
The two-component energy, Hilbert triangle inequality and passage from both analytic unitary signs to arbitrary polynomials give the claimed square-root dependence for the original slices.
Conjugating the label positions preserves curvature, the budget, and all certificate constants.
A collinear set has \(g=0\), and on a circle of radius \(R_0\) the single full subset of weight \(R_0^{-2}\) has error \(-(t_i+t_j)/R_0^2\).
The diameter bound \(2R_0\) gives both constants at most 4, including the two-label case, and a single label has zero derivative.
The existence of a uniform certificate for all configurations remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0345_v1.md#decision-candidate) | Fixed candidate with both criteria and its specified original model. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0345_v1.md#statement) | Exact matrix identity, positive decompositions, implications, uniform bounds and geometric examples. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0345_v1.md#argument) | Every pivot calculation, coupled constraint, matrix completion, edge assignment, subset certificate and slice estimate. |
| [Finding](#finding) | [Lattice Gram theorem](../../claims/Yin_C_F0342_v1.md#statement) | Unnormalized pairings, budget, lattice realization and equivalence of the uniform lower bound to the normal converse. |
| [Finding](#finding) | [Polarized energy](../../claims/Yin_C_F0342_v1.md#polarizing-the-rank-one-energy) | Directed norm sum, triple mixed Gram entry, pivot support and real pairings used in the positive matrices. |
| [Finding](#finding) | [Full core estimate](../../claims/Yin_C_F0342_v1.md#the-cauchy-gram-identity) | Transfer of the signed lower bound through analytic tests to the full polynomial ball and the reflected label orientation. |
| [Finding](#finding) | [Spectral row inequalities](../../claims/Yin_C_F0335_v1.md#statement) | Normalized row inequality on label-constant functions used in the two-label comparison of abstract constraints. |
