---
author: Yin
---
# Exact product fibers after exterior thickening

The [Python verifier](verify.py) constructs the support sets and multiplies their vertices in the integer Heisenberg group with two sign actions.
The faithful representation and the coefficient conclusions are given in [the mathematical argument](../../../ledger/Yin_L_A0043_v1.md).
The program checks the presentation relators, the fiber multiplicities before and after thickening, the indicated minors over the rationals, and the nonzero coefficient assignment on the eight-by-twelve table.
The larger table adds one left translate as well as one right translate.
Run `python verify.py` from this directory with Python 3.
For the [coupled three-fiber certificate](../../../claims/Yin_C_A0035_v1.md), run [the second verifier](verify_coupling.py) with `python verify_coupling.py` in the same directory.
This calculation numbers the eight original vertices first on both sides.
It derives the full normalized six-parameter chart by solving double-fiber equations one vertex at a time and substituting back into all 37.
It verifies that each of the three selected fibers has pairwise distinct term exponents, that all three choices of two fibers admit full-support solutions on this chart, and that five double fibers already imply the Laurent identity obstructing joint cancellation.
Five further rational assignments witness full-support consistency after removing any one of the five doubles from this eight-equation subsystem.
Both programs use the standard library and write their results to standard output.

Run `python verify_eight.py` to check the three-parameter family in [L_A0044](../../../ledger/Yin_L_A0044_v1.md).
The [family verifier](verify_eight.py) substitutes signed Laurent monomials in all thirty-two double equations and the ten larger equations.
