---
author: Yin
---

<a id="par88-u001"></a>
# Par88-U001: Kronecker's Proof and Its Strategy Interfaces

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Source: [Par88](../../../literature/pdf/Par88.pdf), exact artifact in the registry (private lookup: `../../../literature/registry.md#par88-intake`). |
| source-locator | Scope: Theorem 3.11, printed pp. 37-38 / PDF pp. 45-46, read and visually checked independently by the coordinating agent and the star-interface source reader. |
| inspection | Coverage: **audited within this scope**, using the complete elementary reconstruction in [Miy22-U009](../Miy22/Yin_U009_v1.md#miy22-u009). |

No whole-book audit.
The star-interface source reader read Chapter 5, pp. 48-50 / PDF pp. 56-58: the transfer formula C(sI-A)^{-1}B and stable state spectrum give a systems interpretation.

Date: 2026-09-09.
Source: [Par88](../../../literature/pdf/Par88.pdf), exact artifact in the registry (private lookup: `../../../literature/registry.md#par88-intake`).
Scope: Theorem 3.11, printed pp. 37-38 / PDF pp. 45-46, read and visually checked independently by the coordinating agent and the star-interface source reader.
Coverage: **audited within this scope**, using the complete elementary reconstruction in [Miy22-U009](../Miy22/Yin_U009_v1.md#miy22-u009).
No whole-book audit.

## Proof Mechanism and Minimality

For the Hankel matrix H=(a_{m+n}), rank r makes the first r+1 columns dependent.
Thus a nonzero polynomial q satisfies the scalar recurrence q(E)a=0.
Multiplying a(z)=sum_{n>=0} a_n z^{-n-1} by q(z) removes its negative powers.
Conversely, a proper rational expression yields a recurrence and finite column span.
A minimal recurrence, or the reachable and observable shift realization in Miy22-U009, proves that rank equals the reduced denominator degree, counting pole multiplicities.
Boundedness forces the genuine poles into the open unit disk.

The source compresses two minimality steps.
An arbitrary dependence first gives degree **at most** r.
Its polynomial may also have inactive roots: a_n=2^{-n} satisfies (E-1/2)(E-2)a=0, although its Hankel operator is bounded.
Therefore the assertion that all recurrence roots must lie in the disk applies after cancellation/minimality; it is false for an arbitrary annihilator.
Miy22-U009 supplies these steps without changing the theorem.

## Additional Passages Read for Strategy

The star-interface source reader read Chapter 5, pp. 48-50 / PDF pp. 56-58: the transfer formula C(sI-A)^{-1}B and stable state spectrum give a systems interpretation.
This passage supplies no theorem upgrading a bounded output at a fixed operator tuple to a bounded whole inverse.

Chapter 6, Lemma 6.3, p. 57 / PDF p. 65, gives the Hankel intertwining relation H S=S* H, hence an invariant kernel.
Theorem 6.4 and Lemma 6.9, pp. 57-58 and 61, connect inner functions and finite codimension.
These are **selected reading**, not a full AAK or Beurling proof audit.
The column-space and invariant-kernel approaches both need an actual shift/residual operation.
Their applicability to Yin_T_F0001 is assessed in the [strategy investigation](../../../ledger/Yin_L_F0010_v1.md#kronecker-strategies).

Additional source cautions from the reader, not used as project inputs: Proposition 6.1's rank-n formulation requires minimality/no cancellation (g=1=z^2 z^{-2} has rank one); the rank-at-most-n formulation used in the approximation problem is compatible with that example.
Lemma 6.9's displayed interpolation argument needs Hermite conditions for repeated zeros, or iteration of the one-zero codimension argument.
No downstream AAK theorem is claimed audited here.

## Search and Review Boundary

The user's strategy question triggered this original-proof reading after lightweight intake.
Earlier source-access limits remain historical facts; this unit supersedes only the current statement that Partington's proof has not been inspected.
Kronecker's 1881 paper remains unreviewed.
The mathematical comparison is supported by the actual proof and the independent Miy22-U009 reconstruction, not by publisher metadata or numerical truncation.
