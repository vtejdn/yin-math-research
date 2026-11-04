---
author: Yin
---

# Finite witness compression and real algebraic Gaussian tubes

## Task associations

| Task | Scope |
| --- | --- |
| [F0012 contract](../tasks/Yin_T_F0012_v1.md#contract) | All fixed scalar polynomials in independent normalized GUE matrices, including nonnormal evaluations. |

## Route

| Field | Value |
| --- | --- |
| disposition | completed |
| priority | The general monic-pencil estimate and exact F0012 application are proved and adopted with independent whole-chain review. |

## Mechanism and exact target

For a fixed-size monic pencil \(T_N=I_m\otimes I_N+\sum_jR_j\otimes H_j\), a near-kernel vector has at most \(m\) physical components.
Their span and its images under the \(d\) Hermitian inputs have dimension bounded in terms of \(m,d\), independently of \(N\).
Repair the compressed real polynomial equations, including normalization of the kernel vector, by a real algebraic distance inequality.
Lift the repair through Hermitian block perturbations whose Hilbert--Schmidt size is \(O(\varepsilon^\alpha)\), with \(\alpha>0\) independent of \(N\).

The singular-input set is defined in \(dN^2\) real Gaussian coordinates by a nonzero polynomial of degree at most \(2mN\).
A degree-controlled tube bound, extended by regular levels and converted using an exact Gaussian mixture of uniform balls, gives a bound of order
\(N^{5/2}\varepsilon^\alpha\exp(CN^{5/2}\varepsilon^\alpha)+e^{-cN^2}\)
on a fixed input-norm event.
This supplies the polynomial singular-value floor without irreducibility or \(\chi_R>0\).
The [complete argument](../claims/Yin_C_F0186_v1.md#argument) includes the exact linearization and logarithmic-tail application to F0012.

## Relationship to the earlier routes

This route emerged while examining the failure of unrestricted-minor estimates in [S_F0028](Yin_S_F0028.md#route).
It changes the decisive estimate from conditional Schur anti-concentration to distance from the actual Hermitian singular-input set.
The [degenerate examples and minor obstruction](../ledger/Yin_L_F0059_v1.md#schur-findings) remain useful tests.
The parallel [determinant comparison](../ledger/Yin_L_F0060_v1.md#comparison) identifies why free variational formulas alone do not supply a finite-GUE lower bound.
This general route also absorbs the convergence obligations of [S_F0027](Yin_S_F0027.md#route) and [S_F0029](Yin_S_F0029.md#route).
Their particular conditional exponents and structured-refresh overlap estimates are not asserted by this proof.

## Evidence and completion

The responsible mathematical assessment is [C_F0186](../claims/Yin_C_F0186_v1.md#current-assessment).
The [independent whole-chain finding](../audits/reviews/Yin_R_F0190_v1.md#whole-chain-finding) supports the adopted proof and the exact [F0012 completion](../tasks/Yin_T_F0012_v1.md#decision-full-polynomial-proof).
The separate [geometry review](../audits/reviews/Yin_R_F0188_v1.md#geometry-finding) checks the central deterministic and Gaussian estimates.
No further proof obligation remains for this route's stated deliverable under its accepted external inputs.
The exponent can be extremely small; no optimal rate, uniformity over growing coefficient dimension, or non-Gaussian extension is claimed.
