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

## Five numerical fibers for the order-twenty marking

Run `node verify_five_fibers.mjs` in this directory.
The [verifier](verify_five_fibers.mjs) selects two fourth-root eigenvalues with multiplicity in each of five fibers, multiplies their linear factors and tests the six missing-coefficient equations over the field with 101 elements.
Of the 100000 choices, the numbers surviving with zero through five opposite pairs are respectively 0, 0, 0, 0, 60 and 32.
The [five-fiber argument](../../../claims/Yin_C_A0312_v1.md#the-five-numerical-fibers) explains why these finite-field ranks give a necessary condition on complex matrices.

## Four-channel matchings at the order-sixteen marking

Run `python -B verify_four_phase_extrema.py` in this directory with assertions enabled.
The [standard-library verifier](verify_four_phase_extrema.py) checks the seven fourth-root module certificates in the [order-sixteen calculation](../../../claims/Yin_C_A0328_v2.md#all-small-fourth-root-modules).
The 256 paths give sixteen admissible pairs of used edge sets.
At every tested minimum the single-path sites require only the second-site coefficient or the product-site coefficient, and at every maximum they require only the identity-site or the first-site coefficient.
The two extremal pairs are unique in all seven cases; the numerical extrema are printed with the four integer weights.

## Eight-channel interval and matching tests

Run `python -B verify_eighth_phase_extrema.py` in this directory with assertions enabled.
The [standard-library verifier](verify_eighth_phase_extrema.py) covers all prime-field and quadratic eighth-root modules of odd order at most \(16^4\).
The interval test leaves 41 of 1614 split primes and 14 of 86 quadratic factors; testing each marked root leaves 178 cases for the weighted matchings.
For each possible missing singleton corner it checks the unique extremal flow and the ratio of matching spread to \(128p\), with maximum \(11/48\) over the chosen certificates.
The [order-sixteen proof](../../../claims/Yin_C_A0328_v3.md#both-possible-missing-corners-at-the-remaining-178-markings) supplies the original representation and the rank estimate.

## Norms of sixteen-site cycles

Run `python -B verify_sixteenth_cycle_norms.py` in this directory with assertions enabled.
The [integer verifier](verify_sixteenth_cycle_norms.py) enumerates the undirected simple cycles and all integral unit-capacity circulations for the shifts one and six on sixteen sites.
It finds 15691 cycles, 91 with zero opposite-coordinate difference, and 4213 distinct nonzero projected vectors.
Their 58 distinct positive norms are at most 3298.
Among the 2912 circulations the smaller of the two through-site counts is at most four.
The [large-prime proof](../../../claims/Yin_C_A0328_v4.md#the-two-possible-reversal-counts) uses this last count to bound the rank cost of replacing one possibly singular numerical corner.

## The finite sixteenth-root affine images

Run `node verify_sixteenth_remainder.mjs` from this directory.
The option `--witnesses` prints all 12692 individual certificates as JSON lines before the summary.
The [finite verifier](verify_sixteenth_remainder.mjs) uses only the Node.js standard library and writes no files.
It covers all primitive sixteenth-root marked fields with \(p\le49152\) and \(p^f\le2^{40}\), including 5000 linear, 7512 quadratic and 180 quartic factors.
It verifies the 2912 feasible pairs of used permutation edges and a unique pair of minimum cost at each chosen functional, and adds the cost of repairing the possible missing corner at the cheaper endpoint.
The worst selected ratio is \(2985632/6031616<99/200\).
The masks, weights, modular products and ratio comparisons stay within the exact integer range.
The [order-sixteen conclusion](../../../claims/Yin_C_A0328_v5.md#the-12692-finite-certificates-with-a-possible-singular-corner) combines these certificates with the stronger ball-volume inequality above the finite range.

## Bidegree-two polynomials on five sign squares

Run `python -B verify_fifth_sign_squares.py` in this directory with assertions enabled.
The [standard-library verifier](verify_fifth_sign_squares.py) takes two of the four points in each square \((\pm z,\pm z^2)\), \(z^5=1\), and forms the evaluation matrix on \(x^a y^b,\ 0\le a,b\le2\).
Full rank modulo 101 at the primitive fifth root 36 excludes 7552 of 7776 systems.
For every remaining system the program computes signed minors in \(\mathbb Z[\zeta_5]\) and checks a full basis for the kernel over \(\mathbb Q(\zeta_5)\).
There are 4 exact rank-seven and 220 exact rank-eight systems.
In 104 cases the entire kernel is contained in a corner coordinate hyperplane.
The other 120 kernels give 20 distinct projective coefficient vectors, each occurring six times, with ten even only in \(x\) and ten even only in \(y\).
After reversing the first axis to use \(x^2=y^4\) on the squares, these vectors come from the two polynomials \(-1\pm\sqrt5\,y-2y^2+x^2(2\mp\sqrt5\,y+y^2)\) by rotating the five squares and using the corresponding exchange of axes.
The program compares the full set of projective vectors in the original coordinates to these transformed polynomials.
If the constraints on the first square are instead \(f=f_x=f_y=0\) at \((1,1)\), 1294 of 1296 systems have full rank modulo 101.
Both remaining systems have exact rank eight, and neither admits four nonzero corner coefficients.
The [index-four character test](../../../claims/Yin_C_A0336_v1.md#character-ranks-and-zero-orders-on-the-grid) translates these two enumerations into a restriction on the original regular transfer.
