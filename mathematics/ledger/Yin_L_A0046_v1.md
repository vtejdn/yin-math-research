---
author: Yin
---
# The seven complete fibers in the exceptional even-support quotient test

For connected Ope26f matching graphs both selected sides have the same even number \(n\) of vertex occurrences.
Collecting repeated group labels over \(\mathbb F_2\) preserves the total parity on each side and the parity in each quotient class.
The [classification for \(C_7\)](../claims/Yin_C_A0042_v1.md#statement) admits exactly one form of obstruction at a prime over two for these projected equations.
Both true supports must occupy exactly four classes, each of odd cardinality, and their nontrivial Fourier orbits must be opposite.
Here the same obstruction has a short proof directly in the seven group-product fibers, without computing a Fourier determinant.

## Complete fibers with arbitrary positive odd multiplicities

After translating the two sides independently and applying one common automorphism of \(C_7\), their occupied color sets are \(D=\{0,1,2,4\}\) and \(-D\).
Indeed the two four-point masks are translates of complements of opposite oriented Fano lines, as in the [cubic-orbit calculation](../claims/Yin_C_A0042_v1.md#separating-the-cubic-factors).
For instance the triple complementary to \(D\) is \(\{3,5,6\}=6-\{0,1,3\}\).
Write \(A_i\) for the true support elements with row color \(i\), and \(B_j\) for the true support elements with **column color \(-j\)**.
In the table a pair \(ij\) denotes the entire rectangle \(A_i\times B_j\), whose size is \(|A_i||B_j|\).
Independent translations merely shift the displayed product colors.

| Product color \(i-j\) | All class pairs | Number of pairs if every class contains one label |
| --- | --- | --- |
| \(0\) | \(00,11,22,44\) | 4 |
| \(1\) | \(10,21\) | 2 |
| \(2\) | \(20,42\) | 2 |
| \(3\) | \(41,04\) | 2 |
| \(4\) | \(14,40\) | 2 |
| \(5\) | \(02,24\) | 2 |
| \(6\) | \(01,12\) | 2 |

The seven lists partition all sixteen class pairs.
For arbitrary multiplicities their disjoint unions are precisely the full quotient product fibers.
Two cells in one quotient fiber may represent different elements of the original group.
The sparse triple–quadruple example in [L_A0045](Yin_L_A0045_v1.md#three-obstructing-product-fibers-in-a-cyclic-quotient-of-order-seven) has a different table and cannot be the pair of parity masks for two connected sides here.

## Why four appears in the identity coefficient

Let \(u_i,v_j\) be the sums of the lifted row and column coefficients in \(A_i,B_j\).
All eight sums reduce to one when the indicated counts are odd, so are units at the marked point over every finite extension of \(\mathbb Q_2\) and modulo every positive power of two.
Write \(p_i=u_i v_i\).
If the six noncentral coefficient sums are zero, multiply the two-term equalities for each pair of opposite product colors.
For colors \(1,6\) this gives \(p_1p_0=p_2p_1\), so \(p_0=p_2\).
Colors \(2,5\) give \(p_2p_0=p_4p_2\), and colors \(3,4\) give \(p_4p_1=p_0p_4\).
Hence \(p_0=p_1=p_2=p_4\).
The coefficient in the remaining fiber is exactly \(4p_0\).
It is nonzero in characteristic zero and modulo \(8\mathcal O_L\) for every finite extension \(L/\mathbb Q_2\), regardless of ramification.
The equalities of the four products hold in the quotient by the six noncentral equations after the eight aggregates are inverted.
Every lift at the marked point takes values in a ring where the aggregates are units, including modulo the specified precision.

For a modulo-four solution put \(u_0=v_0=1\) and give all six other aggregates value \(-1\).
Each of the six two-term equations vanishes over \(\mathbb Z\), and the central coefficient is four.
Each aggregate sign is realized by one copy of that sign and opposite pairs for the other occurrences, because each of the eight multiplicities is odd.
This proves the existence of the modulo-four lift and the obstruction at the next precision directly on the complete quotient fibers.

## Which counts come from the paper

The [author release](https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026) contains the paper, the TeX sections, figures and references.
The authors explicitly state in [§6, p. 24](../literature/pdf/Ope26f.pdf#page=24) that the proof does not specify the matchings from which a concrete presentation and factors could be read.
The incidence data in §2.1 fix the numbers of each vertex type and each signed letter on the full sides.
They do not give a spanning forest, its cycle words, or the multiplicities of equal group labels at the roots.
Consequently the seven-fiber certificate above is conditional on the indicated **actual occupied classes and counts**.
It does not identify those eight odd counts in a specific Ope26f presentation.

In the [balanced seven-color construction](Yin_L_A0047_v1.md#occurrence-counts-and-the-actual-characteristic-two-supports) every occurrence class instead has exactly \(n/7\) vertices.
Each product color \(k\) receives all seven rectangles \(A_i\times B_{k-i}\), using the direct column color in this sentence, and exactly \(n^2/7\) occurrence pairs.
After collection, every class has even positive size \(n/7-o(n)\) along the selected sequence.
The count in each true-support product fiber is divisible by four and equals \(n^2/7-o(n^2)\).
Those parity and asymptotic statements do not identify the individual finite multiplicities.
Opposite sign pairs on either side then cancel in each projected class over \(\mathbb Z\).
