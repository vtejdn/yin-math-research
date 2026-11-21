---
author: Yin
---
# Independent review of fixed-factor precision and support

An agent outside development reviewed the complete fixed v2 proof directly on 21 November 2026, with no inherited development discussion or prior finding on v2.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0039_v2.md#statement) | Precision cutoff, stationarity and growth, modular lifts, finite support search and conditions on the fixed integral factor. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0039_v2.md#argument) | Complete minor calculation, geometric series, connected support reduction and exact dihedral example. |
| [Whole finding](#whole-finding) | [MD26 witnesses](../literature/MD26/Yin_U001.md#md26-u001) | Proposition 7.11 and proof of Theorem C, p.30, with root protection in the fixed group. |

## Whole finding

The complete stated result is supported.
Multiplying each full-column row minor by its adjugate shows divisibility by \(p^e\) since at least one input coefficient is a unit.
The column length bound gives the strict cutoff and a rational null vector descends to a primitive integer vector by clearing denominators and dividing out the gcd.
The conclusion at \(s_{\mathbb C}-1\), monotonicity, infinite-limit case and signed-unit endpoint follow with the given quantifiers.
Right translation preserves the equation and moves a primitive connected component into the stated finite ball since distinct components have disjoint outputs.
The finite decision requires verified group equalities also on the output rows.

Multiplication by \(A\) on the left telescopes the geometric correction at each precision while preserving the nonzero residue \(c\).
MD26 arXiv v1 p.30 was checked directly for the fixed torsion-free group, \(ab=1,\ ac=0\) and protected \(c\ne0\).
The geometric existence theorem was accepted at its stated scope.
Integer convolution in the dihedral example independently gives both products \(AB=BA=3\) and the changed-coefficient zero product at reflection coefficient two.
This checks the distinction between varying the support coefficients and keeping the whole left input fixed.
The proof does not provide a sublinear support construction for the actual MD26 factors.
