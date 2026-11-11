---
author: Yin
---
# Cauchy residues through geometric index formulas

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Seek a relation-compatible geometric index formula for spectral residues of finite complex group-ring matrices. |

## Route

| Field | Value |
| --- | --- |
| disposition | proposed |
| priority | First new probability candidate: determine the correction to a vertex-edge resolvent identity caused by one explicit group relation before claiming broader coverage. |

## Mechanism

The [Cauchy synthesis](../ledger/Yin_L_A0015_v1.md#boundary-residues-and-reciprocal-slopes) identifies integer unnormalized kernel dimension with integer total boundary residue.
Its [Schur-energy formula](../ledger/Yin_L_A0015_v1.md#schur-complements-and-boundary-energy) separates a real balance equation from the square-integrability that produces an atom.
A generic resolvent equation does not supply the required arithmetic.

The [geometric source model](../ledger/Yin_L_A0015_v1.md#a-geometric-index-mechanism-beyond-algebraicity) supplies additional information.
For a positive-weight periodic Jacobi operator on the universal cover of a finite graph, the Aomoto index theorem identifies the sum of vertex residues with the number of components of the atom-support forest minus its external boundary size.
The related finite vertex-edge product for the logarithmic potential exhibits a mechanism for signed local orders.
The full embedded-atom theorem uses the accepted BGVM20 interface; the BBGSS23 product proof sketch is not a replacement for it.

This differs from [S_A0005](Yin_S_A0005.md): the intended arithmetic comes from a geometric index and cancellation of local resolvent factors, rather than atom transfer between two amalgamated vertex algebras.
It also differs from [S_A0003](Yin_S_A0003.md), since no approximation by integer-rank groups is assumed.
The present tree model has a free deck group and supplies no new Atiyah class.

## Missing bridge

For a group with relations, lifting its labelled graph to the universal tree changes the canonical joint law.
The [fourth-moment calculation](../ledger/Yin_L_A0015_v1.md#a-geometric-index-mechanism-beyond-algebraicity) gives 28 for the free two-generator adjacency operator and 36 after imposing commutation.
The corresponding logarithmic determinant correction begins with minus twice the fourth power of the expansion parameter.
Ignoring this correction would prove a statement about a different operator.

The missing input is a relation-compatible replacement or correction for the finite vertex-edge identity whose boundary contribution is independently controlled by an integer index.
A trace of an arbitrary projection, or an assumed integer nullity of the correction operator, does not supply that input.
The positive real edge hypotheses of the inspected source also leave a separate extension to general complex matrix pencils.

## First discriminating investigation

Begin with the explicit commutation relation and the fixed adjacency model in L_A0015.
Derive its relation correction beyond a finite moment truncation, preserving the actual canonical trace and distinguishing ordinary analytic continuation from boundary limits.
Test whether a finite geometric identity survives or whether the correction necessarily contains additional global spectral information.
Use the known free and abelian cases as calibration, not as new coverage.

If a controlled identity survives, test a noncentral cyclic-amalgam model or another explicitly specified relation family.
Any claim of new coverage must first be compared with existing Atiyah theorems.
If the correction only re-expresses the unknown kernel trace, retain that obstruction and stop treating the identity as a reduction.

## Relation to the return-word route

The [return-word arithmetic route](Yin_S_A0007.md) keeps the whole primitive-cycle series and seeks local-exponent rigidity from its labelled structure.
This route seeks a finite geometric index formula.
They can exchange exact correction identities, but neither is a premise for the other.
