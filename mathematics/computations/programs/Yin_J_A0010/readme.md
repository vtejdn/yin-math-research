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

## Three internal blocks at orders six and twelve

Run `python -B verify_middle_terms.py` with assertions enabled in this directory.
The [second verifier](verify_middle_terms.py) uses the same exact determinant procedure to compare the selected four-index frequency with the constant frequency and with the eight other paths joining its endpoints.
For both choices of endpoint block at order six the nine absolute norms have values \(3,9,12\), and at order twelve they have values \(9,36\).
The absolute norms of \(1-X^4\) are \(3,9\), respectively.
The [three-block proof](../../../claims/Yin_C_A0245_v1.md#a-coefficient-with-three-ordered-factors) verifies nonvanishing of the selected operator coefficient, and the lower-order quotient is recovered from the larger module by the index of \(1-X^4\).

## Six fibers of the rectangular determinant

Run `node verify_six_fibers.mjs` in this directory.
The [finite-field verifier](verify_six_fibers.mjs) tests the possible multiplicities of two selected roots in each of the six fibers of the fourth-power map on the twenty-fourth roots of unity.
It enumerates every unordered pair with repetition in each fiber, giving one million patterns.
One test multiplies the six quadratic factors and checks all missing coefficients of the sparse determinant after the first two determine the remaining factor.
A second test imposes point evaluations and repeated-root derivative equations on the nine possible coefficients, stopping a branch when its row rank is nine.
With generator 4 modulo 97 both tests leave zero patterns, and with generator 7 modulo 193 both leave 24.
The [six-point obstruction](../../../claims/Yin_C_A0244_v1.md#an-obstruction-for-six-numerical-matrices) explains why absence over the first field excludes the complex determinant configuration.

## Three-step frequencies at orders three and twenty-four

Run `python -B verify_small_collisions.py` in this directory with assertions enabled.
The [frequency verifier](verify_small_collisions.py) computes the nine order-three integral norms for each of two paths, obtaining \(1,3,9,12\).
At \(p=7,73,97,193\) it enumerates the monic marked factors of the Frobenius degree, checking that their product is \(\Phi_{24}\bmod p\).
It isolates a nonzero frequency at each of the four quadratic and 24 linear marked factors for both possible invertible Fourier blocks.
It compares the chosen path with every other pair of intermediate channels, including those with zero Fourier index.
At \(p=5\) it exhausts all \(6^3\) paths starting at zero for each of the four quadratic factors; none has an isolated nonconstant frequency.
The [three-step proof](../../../claims/Yin_C_A0251_v1.md#frequency-comparison-on-the-twenty-fourth-simple-factors) supplies the operator nonvanishing and rank implications.

## Alternating group of degree five

Run `python -B verify_a5_transfer.py` with assertions enabled in this directory.
The [permutation verifier](verify_a5_transfer.py) constructs all 60 even permutations and tests all 3600 ordered pairs.
Among the 2280 generating pairs, 1560 pass adjacent generation.
None satisfy either of the two necessary [finite transfer support conditions](../../../claims/Yin_C_A0280_v1.md#statement).
The separate counts record the 720 pairs that pass the sign condition before testing the identity label.
