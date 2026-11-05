---
author: Yin
---

# Complex-symmetric conditional shifts for the two-Wigner product

## Task associations

| Task | Scope |
| --- | --- |
| [Finite-variance F0012](../tasks/Yin_T_F0012_v3.md#contract) | A two-real-Wigner product pilot for the general polynomial negative-logarithm problem. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Complete and independently check the finite-variance complex-symmetric least-singular-value input before asserting an unconditional product theorem. |
| parent | [Planar defect route](Yin_S_F0032.md#route) |

## Mechanism

Condition on \(W_2\) in
\[
 W_1W_2-zI=(W_1-zW_2^{-1})W_2.
\]
For real symmetric \(W_2\), the conditional shift is complex symmetric.
A summable polynomial least-singular-value floor for this class, together with the [reviewed intermediate estimate](../claims/Yin_C_F0187_v2.md#statement), would control the bottom singular values and their negative logarithmic sum.
The [reviewed spectral and planar controls](../claims/Yin_C_F0186_v4.md#statement) supply the remaining convergence interfaces.

## Precise gap and current work

The desired shift theorem must use only a fixed centered unit-variance real off-diagonal law, allow independent diagonal laws or conditioned deterministic diagonals, and have arbitrarily high polynomial failure exponents for polynomially bounded complex symmetric shifts.
The inspected ORSV15 theorem carries \(2+\tau\) and iid diagonal assumptions; its attribution to a personal communication supplies no bare-second-moment theorem.
The [source boundary](../ledger/Yin_L_F0061_v1.md#source-frontier) distinguishes it from Nguyen's published real-symmetric-shift result.
The [fixed complex adaptation](../claims/Yin_C_F0188_v2.md#argument) includes the inverse Littlewood--Offord structure and full probability-profile count.
Its initial version had an order-dependent lower-bound gap after reservoir permutation; the revised candidate reclassifies low-product vectors after each permutation and awaits a fresh independent review.
The [two-factor deduction](../claims/Yin_C_F0186_v5.md#argument) remains a candidate conditional on that exact input.
Its argument is not yet adopted as a proved input.

## Relation to the full target

Even a complete two-factor theorem does not settle all scalar noncommutative polynomials or matrix-coefficient pencils.
The pilot is valuable because its shift exposes the real/atomic second-moment difficulty while the intermediate singular-value and planar interfaces are already available.
