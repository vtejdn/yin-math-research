---
author: Yin
---
# Integer-rank approximation with control near zero

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Transfer integer kernel dimensions along specified marked-group approximations, separating existing convergence theorems from genuinely missing inputs. |

## Route

| Field | Value |
| --- | --- |
| disposition | proposed |
| priority | Conditional; choose an actual target family before investing in a new spectral estimate. |

## Mechanism and known inputs

For a marked-group approximation \(G_i\to G\), transport one finite word matrix with fixed complex coefficients to matrices \(A_i\).
If the \(G_i\) are torsion-free Atiyah groups and their kernel dimensions converge, integrality passes to \(G\).
The [survey's approximation probe](../ledger/Yin_L_A0001_v1.md#approximation-probe) records this finite-lattice argument, a sufficient small-spectrum estimate and the two main failure modes.

Reuse JZ19 when the approximating groups are sofic, and JZLA20 when the target is virtually locally indicable.
In the former setting, the main remaining question may be the existence of suitable integer-rank approximants rather than analytic convergence.
The sofic \(\overline{\mathbb Q}\)-to-\(\mathbb C\) coefficient upgrade is already known.
The [completed JZ19 tensor step](../claims/Yin_C_A0002_v1.md#statement) supplies its centralizer lower bound, not integer-rank approximants or the algebraic-coefficient Atiyah premise.
Accordingly the [current strategy reassessment](Yin_S_A0004.md#strategic-reassessment) retains this route's conditional priority and places construction of the required approximants before additional general spectral estimates.

## First discriminating step

Choose a specific torsion-free target family and establish that the proposed marked approximants exist.
Identify exactly which existing rank theorem applies.
If none does, test a determinant, spectral-profile or other estimate that uniformly prevents positive spectral mass from accumulating at zero.
Require each approximation to preserve integer rank, or prove the additional divisibility needed to recover integers from a finer denominator lattice.

## Decision conditions and contribution

Continue only with an explicit family and an input whose verification would extend the available theorem.
Finite quotients with growing denominators, or weak spectral convergence alone, do not close the route.
A successful result covers the demonstrated approximation class; a universal proof still requires showing that arbitrary torsion-free groups admit the needed models.
