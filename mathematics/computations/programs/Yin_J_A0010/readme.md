---
author: Yin
---

# Four root-of-unity terms at the order-24 marking

## Question and scope

Compute the integer norms of the four-term cyclotomic relations for the residual marking \(3,4\) at cyclic order 24.
The three calculations use the polynomials \(\Phi_3,\Phi_8,\Phi_{24}\).

## Files

The [integer verifier](verify_four_terms.py) forms the matrix of multiplication by each four-term polynomial in the power basis and computes its determinant exactly.

## Reproduction

Run `python -B verify_four_terms.py` from this directory with assertions enabled.
The verifier uses only the Python 3 standard library and writes no files.

## Results and limits

At order three the norms are \(1,4,7,16\).
At order eight all eight normalized choices have norm 8.
At order twenty-four the 216 normalized choices have norms \(1,4,16,25,64,73,97,193,196\).
The [four-step argument](../../../claims/Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group) supplies the relation in the actual module.
The norm calculation then bounds the order of its cyclic integral quotient.
