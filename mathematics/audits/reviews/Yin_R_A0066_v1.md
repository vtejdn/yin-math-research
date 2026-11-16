---
author: Yin
---
# Coupled fibers in exterior thickenings of the Nielsen–Soelberg table

A separate reviewing agent inspected the final fixed Claim, including the eight deletion witnesses, and its two related ledger calculations for Yin on 2026-11-16T17:29 UTC.
The reviewer had checked the original sets and cyclic cosets in [the earlier review](Yin_R_A0062_v1.md#whole-argument-finding).
The scope and hypotheses of that source input were reused here.
The reviewer did not develop the three derivations or consult their development discussions, exploration notes, author explanations or prior verdicts before forming the findings.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |
| [Thickened tables and endpoint multiplicity](#thickened-tables-and-endpoint-multiplicity) | independently reviewed |
| [Six compatible triples](#six-compatible-triples) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0035_v1.md#statement) | Actual repeated fibers, entire normalized binary solution set, variable ratios, coupled exclusion and pairwise compatibility. |
| [Whole-argument finding](#whole-argument-finding) | [Five-double identity](../../claims/Yin_C_A0035_v1.md#an-identity-using-five-double-fibers) | Exact identity and applicability over commutative domains with larger tables allowed at the given full-fiber scope. |
| [Whole-argument finding](#whole-argument-finding) | [Actual table and chart](../../claims/Yin_C_A0035_v1.md#the-true-fibers-and-all-binary-solutions) | Original-first labeling, every binary arrow and necessity and sufficiency of the six free coordinates. |
| [Whole-argument finding](#whole-argument-finding) | [Variable ratios and proper subsystems](../../claims/Yin_C_A0035_v1.md#nonconstant-ratios-and-proper-subsystems) | Fifteen fibers, the three named equations, all eight rational deletion witnesses and inclusion-minimality over \(\mathbb Q\) and \(\mathbb C\). |
| [Whole-argument finding](#whole-argument-finding) | [Faithful model](../../ledger/Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation) | Exact integer group model for equality of the original and thickened support products. |
| [Thickened tables and endpoint multiplicity](#thickened-tables-and-endpoint-multiplicity) | [Table construction](../../ledger/Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation) | Exterior translates, faithfulness and the eight-by-twelve table. |
| [Thickened tables and endpoint multiplicity](#thickened-tables-and-endpoint-multiplicity) | [Determinantal tests](../../ledger/Yin_L_A0043_v1.md#a-determinant-using-only-multiterm-equations) | Both table sizes, exact minors, Zariski-open exclusion and the exceptional rational point. |
| [Thickened tables and endpoint multiplicity](#thickened-tables-and-endpoint-multiplicity) | [Endpoint multiplicity](../../ledger/Yin_L_A0043_v1.md#why-some-double-fibers-persist) | The \(2k-1\) cell threshold and its consequence for arbitrary thickening lengths. |
| [Six compatible triples](#six-compatible-triples) | [Family](../../ledger/Yin_L_A0044_v1.md#a-family-inside-the-binary-equations) | All 32 double identities and the ten remaining Laurent polynomials in the interleaved column order. |
| [Six compatible triples](#six-compatible-triples) | [Six triple equations](../../ledger/Yin_L_A0044_v1.md#solving-the-triples-with-variable-ratios) | Pairwise variation, full solution inside this family, and surviving nonzero coefficients. |

## Whole-argument finding

Independent multiplication with the stated integer group law in the original-first order gave 37 doubles, ten triples, five quadruples and four quintuples.
The three named larger fibers and all five selected doubles are entire fibers.
The 37 double arrows grouped by row pair agree with the displayed table.
With the two reference coefficients normalized, a double with three known nonzero variables uniquely determines the fourth.
The indicated sequence determines all sixteen missing coordinates from the six free coordinates, and direct substitution makes every double equation vanish as a Laurent polynomial.
Since the free parameters themselves are coordinates of the solution, this is a single translated six-dimensional torus with the claimed inverse chart.

On the five selected doubles alone, division gives \(U_6/U_7=U_2,\ U_3/U_7=U_5,\ V_{10}/V_{11}=V_5\).
After these substitutions, \(P_G/U_7+P_F/V_{11}\) agrees term by term with \(P_T\) apart from the extra nonzero term \(V_{12}/V_{11}\).
The contradiction uses no remaining coefficient equation, and all divisions are permissible in the fraction field, including in characteristic two.
The indicated eight fibers must retain their actual full multiplicities for this deduction to apply to a larger table.

Comparing the six-component integer exponent vectors in the original uncollected terms of every larger fiber gave eight triples, five quadruples and two quintuples with no constant internal ratio.
For \(a=x=y=z=1\), the three equations are \(2+b,\ 2-c,\ 3+b-c\).
In the given order the three rational witnesses kill the prescribed pairs and give respectively \(-1,1,1\) in the remaining equation.
All coordinates of the parametrization are nonzero there.
The reviewer also ran [the coupling verifier](../../computations/programs/Yin_J_A0003/verify_coupling.py), which reconstructed the chart by unit pivots, checked the identity both on that chart and with only five doubles imposed, and reproduced the rational witnesses.
For each additional witness deleting a double, the reviewer compared all eight displayed coordinates with the program and independently substituted them into the eight original coefficient equations using integer arithmetic after clearing denominators.
Upon division by the common scale, every retained coefficient vanished and the five omitted values were \(-1,1/2,-1,-2/3,1\), respectively.
Together with the three witnesses deleting a larger fiber, this proves inclusion-minimality over \(\mathbb Q\) and \(\mathbb C\).
The eight-equation obstruction itself holds over every commutative domain with nonzero support coefficients.

## Thickened tables and endpoint multiplicity

Both \(x\) and \(y\) invert \(t=(xy)^2\) under conjugation by the presentation, so \(\langle t\rangle\) is normal.
Modulo \(t\), multiplying the stated identities for \(xyx,\ x^{-1}yx^{-1}\) yields \(xy^2x^{-1}=y^{-2}\), and the analogous identity gives \(yx^2y^{-1}=x^{-2}\).
Thus \(x^2,y^2\) commute and generate a normal abelian subgroup with quotient of order at most four.
The four sign pairs in the affine-plane image distinguish those cosets, and the translations \((2,0),(0,2)\) detect every nontrivial element of the subgroup of squares.
This proves injectivity of the affine-plane representation modulo \(t\).
The lift to the Heisenberg group detects \(\langle t\rangle\) by its infinite-order central Heisenberg translation, proving faithfulness.
An alternative representation of any original product remains a distinct representation after multiplying both corresponding rows and columns by fixed exterior powers on their respective sides.
This proves absence of singleton fibers at every stated thickening.

The reviewer ran [the exact table verifier](../../computations/programs/Yin_J_A0003/verify.py), checked the two-generator relators and compared the output with the table in its specified interleaved order.
The eight-by-twelve counts were \(32,8,2\) for sizes two through four, and the ten larger fibers agreed entry by entry.
With the right weights one, the eight selected linear equations on the left weights give successively \(u_2=u_3,\ u_5=u_6,\ u_3=u_4,\ u_8=u_6\) and then \(u=0\).
The determinant was \(-1\), so odd integral right weights also give a nonzero determinant by reduction modulo two.
The rational weights in the ledger kill all ten larger equations and have coefficient \(-19\) at the identity.
The interleaved twelve-by-twelve calculation returned the displayed twelve selected indices and determinant \(-1\).

At either extremal height in a double coset, each contributing cell can supply only one representation.
If every actual product has at least \(k\) representations and at most \(2k-2\) cells are available, the extremal cells at either end must all give the same product at that end.
Otherwise two products would require at least \(2k\) cells.
At least two cells attain both ends since the two extremal collections each have size at least \(k\).
Those cells realize the full height span.
In a double coset meeting the rectangle of maximal widths, the positive coefficients of the width formula force every such cell to lie in the rectangle, and every rectangle cell to attain both ends.
If the column direction is reversed, the common maximal column width converts coincident low-height representatives to coincident products of the chosen low row and low column endpoints.
This leaves every product of the two endpoint sets repeated, contradicting the established unique-product theorem for sets of at most four elements per side.
Thus some double coset meeting that rectangle has at least \(2k-1\) cells.
The four residue classes bound each mixed double coset by four cells in these thickenings, so singleton-free tables always retain a double fiber.

## Six compatible triples

The reviewer ran [the eight-by-twelve family verifier](../../computations/programs/Yin_J_A0003/verify_eight.py).
It multiplies signed Laurent monomials in each actual fiber before collecting terms.
All 32 doubles vanish identically, all ten listed Laurent expressions agree, and the terms have distinct exponents within each of fibers \(1,4,5,6,9,10\).
Independence of \(c,e,r\) in this family proves that none of these ratios is fixed by the binary equations.
Fiber 5 forces \(c=(1+e)r^3\), and fiber 1 then forces \(r^4=-1\).
Conversely those identities with \(e\ne0,-1\) make fibers \(4,6,9,10\) vanish by \(r^8=1\).
They preserve exact support and leave fiber 7 equal to \(-r^3\), so the rational-polynomial parametrization supplies simultaneous compatibility for precisely the stated subsystem without producing a zero product.
