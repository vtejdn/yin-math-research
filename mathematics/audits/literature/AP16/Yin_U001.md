---
author: Yin
---

# AP16-U001: Normal phase and universal operator Schur multipliers

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | English arXiv:1611.01593v1, 2016-11-05, 97 pages; online-only at the original reading. |
| source-locator | Introduction pp. 3-4, Section 3.1 and Theorems 3.3.2-3.3.3, pp. 53-54. |
| inspection | 2026-09-29 definitions and exact statements checked; Theorem 3.3.3 proof mechanism inspected, original Schur foundations accepted. |

<a id="ap16-u001"></a>
## Selected input and original reading

The original reading dates, exact source version, inspection depth and limitations remain those recorded below.
The source-proof inspection is limited to the reading described below.

## Retained selected source content

Date: 2026-09-29.
Reader: counterexample agent.
Purpose: distinguish the normal phase's coarse L2 unitarity from a possible operator-norm lifting in T_F0001.

Artifact inspected online: Aleksandrov--Peller, *Operator Lipschitz functions*, English arXiv:1611.01593v1 (2016-11-05), 97 pages, <https://arxiv.org/pdf/1611.01593v1>.
The PDF title, both authors, version margin, and source table of contents were inspected.
No local PDF was obtained; failed acquisition is distinct from the mathematical inspection.

| Passage | Inspection | Use and limit |
| --- | --- | --- |
| Introduction, printed/PDF pp.3--4; Section3.1 | Definitions checked | Operator Lipschitz and commutator Lipschitz estimates are different for normal spectra. |
| Theorem3.3.2, printed/PDF p.53 | Exact statement checked and accepted as an established external theorem | A continuous function on a closed planar set is commutator Lipschitz exactly when its off-diagonal divided difference, with the prescribed zero diagonal, is a universal Schur multiplier. No complete proof audit is claimed. |
| Theorem3.3.3, printed/PDF p.53, proof continuing p.54 | Statement and proof mechanism inspected | Commutator Lipschitz continuity forces complex differentiability relative to the set at nonisolated points. The proof uses finite divided-difference restrictions and the triangular-sign Schur obstruction. Prior Schur multiplier foundations are accepted, not re-audited. |

For a closed disk, f(z)=conjugate(z) fails complex differentiability at every interior point.
Thus its off-diagonal divided difference

    k(z,w)=(conjugate(z)-conjugate(w))/(z-w)

is not a universal operator Schur multiplier.
In contrast |k|=1 off the diagonal, so it is a unitary multiplier of the coarse Hilbert tensor space for a diffuse scalar spectral measure.
This is the precise limit on an unrestricted operator-norm lifting shortcut.
It is not a counterexample to the actual-vacuum rationality criterion.

<a id="local-disk-law-comparison"></a>
The distinction can be seen within the current theorem's positive examples.
For normalized area measure mu on the unit disk,

    sup_z integral |z-w|^(-1) dmu(w) <= 4,

and the symmetric bound also holds: translate the disk into the radius-two disk and integrate r^(-1) against planar area.
Weighted Cauchy--Schwarz gives the elementary Schur estimate directly: if both absolute kernel row and column integrals are at most 4, its L2 integral operator C has norm at most 4.
Furthermore ||C1||_infinity<=4.
Hence E p=p C1-Cp extends to a bounded L2 operator of norm at most 8, with [E,z]=P and the required Hilbert--Schmidt starred commutator.
The normalized dual and its actual vacuum therefore exist for this very disk law.
C_F0055 covers free copies as well.
Failure of universal operator Schur multiplication is compatible with a valid full rationality criterion for these tuples.

The Schur estimate in the preceding paragraph is reconstructed here from Cauchy--Schwarz, not imported as another unaudited source theorem.
No whole AP16 article audit, historical novelty assertion, or correlated counterexample is claimed.
