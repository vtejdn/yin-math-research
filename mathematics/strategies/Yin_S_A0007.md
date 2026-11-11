---
author: Yin
---
# Return-word determinants and local exponent rigidity

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Seek integer atom residues from torsion-free primitive return words and their multivariate determinant series, retaining arbitrary complex coefficients. |

## Route

| Field | Value |
| --- | --- |
| disposition | proposed |
| priority | Exploratory arithmetic candidate: identify information in the labelled multivariate Euler product that can rule out fractional boundary exponents beyond one-variable integrality. |

## Mechanism and actual input

For a finite matrix over a group ring, use the unnormalized trace to form the exponential return series
\[
D_A(t)=\exp\left(-\sum_{j\ge1}
  (\operatorname{Tr}_n\otimes\tau_G)(A^j)\frac{t^j}{j}\right).
\]
The [torsion-free cycle calculation](../ledger/Yin_L_A0015_v1.md#torsion-free-cycle-arithmetic-and-its-obstruction) gives an Euler product over primitive closed labelled index paths.
Torsion-freeness enters at an actual step: if a repeated closed path has identity group label, its primitive root also has identity label.
Keeping the edge coefficients as independent variables retains an identity over their integer polynomial ring.

The source basis is Kontsevich's scalar product for arbitrary torsion-free groups and the Kassel--Reutenauer cyclic-series matrix construction, at the exact checked scope in L_A0015.
Their free-group algebraicity results are not asserted for general groups.
For a positive contraction obtained from \(A^*A\), the [logarithmic boundary exponent](../ledger/Yin_L_A0015_v1.md#logarithmic-slopes-and-return-amplitudes) is exactly the original unnormalized kernel dimension.

This differs from scalar rational-pivot methods, approximation by other groups and amalgamated atom transport.
Its proposed new information is the canonical word structure and its primitive-root constraint.

## Refuted shortcuts and remaining obligation

Integer Taylor coefficients do not force integer local exponents.
The [explicit probability-law test](../ledger/Yin_L_A0015_v1.md#torsion-free-cycle-arithmetic-and-its-obstruction) has a rational Cauchy transform and determinant series \(\sqrt{1-4t}\) with integer coefficients, yet atom mass one half.
Algebraicity alone also permits fractional exponents.
A finite list of return moments supplies neither a boundary limit nor its arithmetic.

The missing theorem must use more of the actual labelled cyclic structure than those generic properties.
It must control the relevant real boundary exponent even when continuous spectrum accumulates at the atom.
An ordinary argument-principle proof requiring a meromorphic continuation is not available in general.

The full Task allows arbitrary complex coefficients.
An integer-coefficient theorem alone is therefore insufficient.
The multivariate identity preserves coefficient dependence formally, but a valid passage to every complex specialization requires an additional argument.

## First discriminating investigation

Work with the multivariate primitive-return series for a small presentation with one relation.
Compare its structural identities with those of the fractional law above before investing in a general local-exponent assertion.
Determine whether positivity plus the full compatible return language imposes a restriction not shared by a generic integral algebraic series.
A finite recurrence or finite factorization is useful only when derived from the actual relations and when its contribution to the boundary residue is justified.

The [geometric index route](Yin_S_A0006.md) supplies a known model of the stronger structure that would be needed: a finite signed count for a residue.
Use its factorization as a calibration, without assuming that every primitive-cycle product admits that finite collapse.
Retain a negative result if a proposed arithmetic property is still compatible with fractional boundary exponents.
