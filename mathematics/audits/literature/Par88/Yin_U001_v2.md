---
author: Yin
---

<a id="par88-u001"></a>
# Par88-U001: Kronecker's Proof and Its Strategy Interfaces

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Partington, *An Introduction to Hankel Operators* (Cambridge University Press, first published 1988; 2007 digitally printed reissue). The proof reading recorded the source/account locator `../../../literature/registry.md#par88-intake`; the [later definition recheck](#definition-recheck) describes a supplied 111-page scan of that reissue at the same locator. The presently available PDF matches the edition, page count and theorem/page locator, but its exact identity with the file read on 2026-09-09 is unverified. |
| source-locator | Scope: Theorem 3.11, printed pp. 37-38 / PDF pp. 45-46, read and visually checked independently by the coordinating agent and the star-interface source reader. |
| inspection | Coverage: **audited within this scope**, using the complete elementary reconstruction in [Miy22-U009](../Miy22/Yin_U009_v1.md#miy22-u009). |

No whole-book audit.
The star-interface source reader read Chapter 5, pp. 48-50 / PDF pp. 56-58: the transfer formula C(sI-A)^{-1}B and stable state spectrum give a systems interpretation.

Date: 2026-09-09.
Source: [Par88](../../../literature/pdf/Par88.pdf), with the edition and historical-file identity limit stated in the source-version field above.
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

## Additional retained definition source recheck

<a id="definition-recheck"></a>

Its exact definitions, source version and locators, actual visual pages and unreviewed-proof limits are preserved.
Already sufficient definitions and theorem arguments remain at their linked U homes.
The original sidecar and unchanged-file language records that earlier checkpoint; this retention neither opens the source again nor performs a new proof or independent review.

Date: 2026-09-10.
Reviewer: the unbounded-operator agent, selected primary-source reading and self-review.
This sidecar supplements the definitions behind [Par88-U001](Yin_U001_v1.md#par88-u001), without creating another source unit or changing its proof assessment.

Source: [Par88](../../../literature/pdf/Par88.pdf), the supplied 111-page scan of the 2007 digital reissue of the 1988 book, as identified in the registry (private lookup: `../../../literature/registry.md#par88-intake`).
Printed page = PDF page − 8.

## Actual inspection and existing homes

Text and full rendered pages were inspected at printed p. 15 / PDF p. 23, pp. 30–31 / PDF pp. 38–39, pp. 37–38 / PDF pp. 45–46, and p. 57 / PDF p. 65.
The Chapter 3 introductory matrix on printed p. 29 / PDF p. 37 was read in extracted text.
The scan's Fourier exponents, projection ranges and absence of coefficient conjugation in its reversion map were checked visually.

The prior exact Kronecker statement and adopted rank/pole convention remain in [Miy22-U009, Exact Statement and Conventions](../Miy22/Yin_U009_v1.md#exact-statement-and-conventions).
The review of Partington's original proof remains [Par88-U001, Proof Mechanism and Minimality](Yin_U001_v1.md#proof-mechanism-and-minimality).
The following precise source definitions were not written out fully in that short unit and are supplied here for definition navigation.

<a id="hardy-spaces"></a>
## Hardy spaces and the shift

**Source Definition 2.2, printed p. 15 / PDF p. 23.**
For \(1\le p<\infty\), \(H^p\) is the space of analytic functions on the open unit disk with

\[
\|f\|_{H^p}=
\sup_{0\le r<1}
\left(\frac1{2\pi}\int_0^{2\pi}|f(re^{\mathrm i\theta})|^p\,d\theta\right)^{1/p}
<\infty .
\]

\(H^\infty\) consists of bounded analytic functions on the disk, with the supremum norm.
The source writes \(H_p\); the superscript convention here is a notation change.
Lemma 2.3 on the same page identifies \(H^2\) with coefficient \(\ell^2(\mathbb N_0)\) and the closed nonnegative-Fourier subspace of \(L^2(\mathbb T,d\theta/(2\pi))\).
Its orthonormal basis is \(1,z,z^2,\ldots\).
The source inner product is first-linear.

**Source convention, Lemma 6.3, printed p. 57 / PDF p. 65.**
The shift is \(S:H^2\to H^2,\ (Sf)(z)=zf(z)\).
Its adjoint deletes the first coefficient, \(S^*(\sum_{n\ge0}a_nz^n)=\sum_{n\ge0}a_{n+1}z^n\).
The Hankel intertwining relation there is \(\Gamma S=S^*\Gamma\).
The relation is an established result, not an extra definition of an arbitrary dual derivative; the strategy use does not identify multiplication by a normal generator with this shift.

<a id="hankel-symbol-conventions"></a>
## Hankel matrices, operators and three symbol conventions

**Source setup, Chapter 3, printed pp. 29–31 / PDF pp. 37–39.**
The Hankel matrix has entries \(H_{m,n}=a_{m+n}\), \(m,n\ge0\).
It gives a bounded Hankel operator on \(H^2\) only when the column prescription extends boundedly.
In that case

\[
\Gamma z^m=\sum_{n\ge0}a_{m+n}z^n.
\]

Let \(P_+\) project \(L^2(\mathbb T)\) onto \(H^2\), let \(P_-=I-P_+\), and let \(M_g\) be multiplication by \(g\in L^\infty(\mathbb T)\).
For Fourier coefficients \(g_k\), the source's three conventions are:

| Source convention | Bounded map on \(H^2\) | Matrix coefficients |
| --- | --- | --- |
| Approach A; Theorem 3.1, pp. 30–31 | \(P_+M_gR\), with \(R(z^m)=z^{-m}\) | \(a_n=g_n\) for \(n\ge0\) |
| Approach B, p. 30 | \(P_+RM_g\) | \(a_n=g_{-n}\) for \(n\ge0\) |
| Approach C, pp. 30–31 | \(UP_-M_g\), with \(U(z^{-n-1})=z^n\) | \(a_n=g_{-n-1}\) for \(n\ge0\) |

The maps \(R\) and \(U\) are complex-linear coefficient reversals on the stated Fourier spaces.
They are not complex conjugation of coefficients.
In Approach C one may equivalently keep \(P_-M_g:H^2\to(H^2)^\perp\), with its range basis \(z^{-1},z^{-2},\ldots\), instead of identifying that range with \(H^2\).

Only the designated Fourier half and, depending on the approach, its constant term are seen by the operator.
Therefore the phrase “rational symbol” requires this convention or a normalization of the unused coefficients.
Finite rank of one Hankel block does not assert rationality of the entire arbitrary \(L^2\) symbol.
The project's two-block Haar comparison already makes that distinction in [Miy22-U009](../Miy22/Yin_U009_v1.md).

## Laurent and rank conventions

Theorem 3.11, printed pp. 37–38 / PDF pp. 45–46, associates the coefficient power series \(f(z)=\sum_{n\ge0}a_nz^n\) with

\[
(Uf)(z)=z^{-1}f(z^{-1})=\sum_{n\ge0}a_nz^{-n-1}.
\]

This is the Laurent convention adopted in Miy22.
When rational, this Laurent function is strictly proper at infinity.
Rank is ordinary complex rank, and the pole count uses the reduced rational function with multiplicities, including a possible pole at zero.
The existing [minimality qualification](Yin_U001_v1.md#proof-mechanism-and-minimality) and [Miy22-U009 normalization](../Miy22/Yin_U009_v1.md#exact-statement-and-conventions) remain the authoritative theorem interpretation; this check does not reopen their proofs.

The algebraic Hankel matrix of a multiletter formal series is a related definition with a different index set and no automatic boundedness premise; see [BR10, Chapter 2 Section 1, printed pp.30–31 / PDF pp.42–43](../../../literature/pdf/BR10.pdf#page=42).
Grouping them under Hankel terminology is navigation, not a claim that all their analytic realizations are interchangeable.

## Actual consumers, citation purpose and limits

[The Kronecker strategy investigation](../../../ledger/Yin_L_F0010_v1.md#what-the-classical-proof-contributes) cites Par88-U001 for its column-space/shift mechanisms and explicitly tests limits of normal-generator transfer.
This is discussion/strategy use.
[Yin_C_F0004's exact rank comparison](../../../claims/Yin_C_F0004_v1.md#exact-rank-refinement-and-the-kronecker-comparison) refers forward to Miy22-U009 rather than importing Partington's proof as a dependency.
[The Yin_C_F0015 Hardy applications discussion](../../../ledger/Yin_L_F0007_v1.md#classical-hardy-functions) also cites Miy22-U009 for the Fourier-half issue; the general Yin_C_F0015 proof does not assume a Hardy symbol.

Citation purposes: standard or exposition for Hardy/Hankel definitions, notation for the Fourier indexing.
No historical origin claim is made.
This is not a proof audit of Hardy boundary theory, Nehari, Beurling, AAK, the cited original Kronecker paper or the rest of the monograph.
Original audit and source PDF were preserved.
