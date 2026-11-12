---
author: Yin
---
# Signed color cycles and finite moment certificates

This continuing exact computation serves [A0001](../../../tasks/Yin_T_A0001_v1.md#contract) and [route four](../../../strategies/Yin_S_A0004.md).
Its fixed starting point is the [short-cycle table](../../../claims/Yin_C_A0009_v4.md#reproducible-finite-expansion) and the [girth-ten restriction](../../../claims/Yin_C_A0009_v6.md#statement).
The task is to enumerate the next signed proper-color cycle classes and test exact polynomial bounds before any actual-group exclusion is asserted.
The native enumeration continues the cyclic-word convention of the earlier short JavaScript calculation, using incremental proper-color generation and integer arithmetic.

## Native program and reproduction

The continuing program is `cycles.py` in this directory.
It uses Python 3 standard-library integer and rational arithmetic only.
Its default generated output belongs to the matching directory under `mathematics/computations/outputs/`, resolved from this program's actual containing J directory independently of the working directory.
Run `python cycles.py --lengths 4 6 8 10 12` from this directory or invoke its absolute path.
The generated JSON is reproducible output and may be replaced by the same program after checking actual consumers.
No generated data is yet an indispensable fixed proof input.

## Mathematical scope and current status

The program constructs all proper cyclic color strings, converts their alternating labels to freely reduced words, and groups them only by cyclic conjugation and inversion in the free group.
The signed multiplicity records the number of occurrences of the negative color.
It does not solve the word problem in any actual group, establish torsion-freeness, identify which relations can coexist, or certify an analytic kernel dimension.
The cyclic-color count is checked against the exact formula `2**n + 2` for even n.
Tree moments and polynomial coefficients are computed with exact arithmetic, separately from any actual-group moment-matching hypothesis.
The program was run for lengths 4, 6, 8, 10 and 12 with Python 3.14 and exact standard-library arithmetic.
The color totals were respectively 18, 66, 258, 1026 and 4098; the cyclic-word class totals were 6, 13, 36, 105 and 351.
The shorter totals and signed counts agree with the retained v4 tables.
The free tree moments through order six were `1, 3, 15, 87, 543, 3543, 23823`.
The weighted polynomial calculation gave `q = 1 - 2s/3 + s²/12`, free value `2/9` and fifth-moment coefficient `-1/1296`.
The [independent whole-artifact finding](../../../audits/reviews/Yin_R_A0028_v6.md#whole-artifact-finding) includes inspection of the native program and independent exhaustive reproduction of every class multiplicity at the stated lengths, together with the tree and polynomial arithmetic.
The actual-group arguments and their conditional scope are retained separately in [C_A0009 v7](../../../claims/Yin_C_A0009_v7.md#statement); the finite enumeration supplies no additional group-theoretic exclusion.

## Ten-cycle symmetries and bounded certificate search

The continuing `ten_cycle_orbits.py` imports the unchanged word conventions from `cycles.py`.
Run `python ten_cycle_orbits.py` in this directory, or invoke its absolute path.
It computes the eighteen orbits of the fifty negative ten-cycle classes under the two specified substitutions, and checks that only the three fifth-power classes have multiplicity two while every other class has multiplicity ten.
It also searches elementary Nielsen substitutions with reduced cyclic word length at most ten and a bound of 20000 discovered words, retaining every successful path and its induced images of the original generators.
The specified target set contains a cyclic presentation, cyclic-normalizer presentations with exponents -3, -2, -1, 1, 2, 3, and a common-two-three relation.
The program was run with Python 3.14, giving four cyclic target orbits, one cyclic-normalizer target orbit, five common-two-three target orbits, and eight target searches with no certificate.
The fifth-power orbit is among the latter and is excluded mathematically by torsion-freeness, not by this target search.
The largest search visited 128 words, below its explicit bound; exhaustion of this bounded length graph still supplies no classification under unrestricted changes of generators.
Its reproducible JSON output is `mathematics/computations/outputs/Yin_J_A0001/ten-cycle-orbits.json`, resolved from the native program location and atomically replaced on a successful rerun.
The [independent R_A0028 v7 finding](../../../audits/reviews/Yin_R_A0028_v7.md#whole-artifact-finding) checks the inspected program, every signed class and orbit against a separate exhaustive enumeration, successful Nielsen paths and the stated run bounds.
The review executes the finite functions in memory; it inspects the output-writing entry point in code without rerunning its filesystem replacement, and gives no unrestricted Nielsen or actual-group word-solver claim.
