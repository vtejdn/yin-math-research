---
author: Yin
---
# Three-term fibers and the saturation of the binomial relations

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0025_v1.md) for Yin on 2026-11-16T16:09 UTC.
The reviewer had reviewed the binomial character criterion used in earlier work and had no role in developing this proof.
No development discussion, author explanations, exploration notes or prior verdict on this argument was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0025_v1.md#statement) | Divisibility of all three difference orders, obstruction for odd fibers and exact coefficient-solvability test under the stated saturation assumptions. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0025_v1.md#argument) | Character values on the saturation, unit-circle geometry, the cyclotomic parity argument and extension of a character from the difference sublattice. |

## Whole-argument finding

The statement holds for the actual product fibers of the given finite supports in any group.
The disjoint label sets make a character of the free lattice equivalent to arbitrary choices of nonzero row and column coefficients.
A vanishing two-term sum forces value \(-1\) on its difference in either orientation, so all lattice combinations of these differences have values in \(\{\pm1\}\).
The saturation has the same rank as the binomial lattice and contains it with finite index.
Thus a difference of order \(m\) in their quotient has character value of order dividing \(2m\).

For a triple satisfying the two stated membership hypotheses, the third difference is also in the saturation by subtraction.
Dividing by a nonzero reference product brings the equation to \(1+\xi+\eta=0\) with the other two terms of unit modulus.
Then \(\Re(\xi)=-1/2\) and \(\eta=-1-\xi\), so the ratios to the reference term are the two different primitive cube roots.
Their quotient and all three inverse ratios also have order three.
It follows that three divides \(2m\) and hence \(m\) for each within-fiber difference.
Lagrange's theorem gives the index obstruction.

For an odd fiber satisfying the stated power-of-two hypothesis, the finitely many ratios to the reference term lie in one cyclic group of order \(2^s\) for some \(s\ge1\).
Recording their exponents between zero and \(2^s-1\) gives an integer polynomial whose value at one is the number of terms, including multiplicities.
Vanishing at a primitive \(2^s\)-th root would make it a multiple over \(\mathbb Z\) of the monic cyclotomic polynomial \(X^{2^{s-1}}+1\).
Evaluation at one then contradicts odd cardinality.

For a table consisting entirely of pairs and saturated triples, cancellation fixes each paired ratio and gives exactly two possible ordered assignments of the nonreference ratios of each triple.
Testing the sum of the assigned exponents modulo six on a basis of the full integer kernel tests it on every integral dependency.
This condition is necessary and sufficient for the assignments to define a character on the generated difference sublattice.
In Smith coordinates the sublattice has generators \(k_i e_i\), and taking a \(k_i\)-th root of each prescribed value assigns a character to \(e_i\).
All prescribed values are roots of unity, so those roots can also be chosen as roots of unity, and the free complementary coordinates can be assigned one.
The extended character recovers coefficients on the original row and column labels and cancels every fiber with its selected ratios.
This gives a finite test of coefficient solvability, with regular ranks of any resulting factors left to a separate calculation.
