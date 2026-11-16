---
author: Yin
---
# Three fibers in a finite image of the Nielsen–Soelberg support table

The integer calculation in [verify.py](verify.py) tests a finite permutation representation of presentation (4.2) in [Nielsen and Soelberg, §4, p. 8](../../../literature/pdf/NS24--author.pdf#page=8).
The application to complex group-ring coefficients is in [L_A0041](../../../ledger/Yin_L_A0041_v1.md).

## Reproduction

Run `python verify.py` in this directory using Python 3 and its standard library.
Each of the first two coordinate pairs is an affine permutation of \(\mathbb Z/3\), and the last coordinate lies in \(\mathbb Z/4\).
The program verifies the two identity assignments and all fourteen defining relations before computing the finite images of the sixty-four products.
It prints the three selected image fibers and checks that each consists exactly of the indicated two cells.
All inputs are in the program, and its output is written to standard output.

The deduction that each image pair is an actual double uses the authors' no-unique-product result for their original group.
The triple used in the coefficient contradiction follows from the presentation and the authors' bound of three on the size of an actual fiber.
