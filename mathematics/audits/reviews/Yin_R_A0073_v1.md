---
author: Yin
---

# Precision eight and characteristic-zero lifting on the seven-cycle

A separate reviewing agent inspected the fixed C_A0042_v1 for Yin on 2026-11-16T18:15 UTC.
The reviewer had previously read the sparse quotient example in L_A0045 and worked on which finite quotients occur in a random matching presentation.
The reviewer did not participate in C_A0042's arithmetic classification and received or consulted no development dialogue, author explanation or previous verdict on that argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0042_v1.md#statement) | Complete table with separate odd and occupied masks, precisions four and eight, exact lifts and allowance for arbitrary finite ramification. |
| [Whole-argument finding](#whole-argument-finding) | [Cubic factors](../../claims/Yin_C_A0042_v1.md#separating-the-cubic-factors) | Fourier orbits, the chosen place and the enumeration of binary masks consistent with the residual zero product. |
| [Whole-argument finding](#whole-argument-finding) | [Two determinants](../../claims/Yin_C_A0042_v1.md#the-two-small-determinants) | Liftable linear systems, exact determinant valuations, invertible cofactors and forced augmentation valuation over arbitrary finite extensions. |
| [Whole-argument finding](#whole-argument-finding) | [Completing the lift](../../claims/Yin_C_A0042_v1.md#completing-the-lift-and-distinguishing-the-two-precisions) | Fourier recombination, choice of field, nonzero aggregate coordinates, and realization by individual unit coefficients. |
| [Whole-argument finding](#whole-argument-finding) | [Mask counts and example](../../claims/Yin_C_A0042_v1.md#exact-masks-and-an-example-failing-first-at-eight) | Exact counts of ordered supports and coefficient-by-coefficient verification of the exhibited integral product. |

## Whole-argument finding

The residual polynomial \(X^7-1\) separates into degrees \(1,3,3\) over \(\mathbb F_2\), with the two nontrivial orbits exchanged by inversion.
Every residue-one occurrence has aggregate reduction prescribed by the parity of its class.
The full-indicator and zero-indicator constructions correctly allow even occupied classes to cancel internally.
In the remaining cases each side occupies one nontrivial Fourier orbit and annihilates its opposite, with at most one side nonzero at augmentation.
In the binary remainder coordinates the seven nonzero vectors of \(\mathbb F_2^3\) give the seven lines of three points, their seven complements, and the empty and full masks as the sixteen zero-sum subsets.
This accounts for all masks under the assumed residual product equation.

The two periods satisfy \(\eta+\eta'=-1\) and \(\eta\eta'=2\).
Their distinct reductions give the claimed local embeddings and \(v_2(\eta)=1\).
After adjoining seventh roots to any finite extension, the relevant Vandermonde matrices stay invertible integrally, since the reductions of all seven roots are distinct.
At a frequency where a factor has nonzero residual value its partner must vanish modulo the full \(2^n\), even for ramified coefficients.
This is stronger than vanishing modulo the \(n\)-th power of a uniformizer in the ramified case.

The reviewer recomputed all seven remainder columns by starting at \((1,0,0)\) and applying
\[
                (d,e,f)\longmapsto(f,\ d+(1+\eta)f,\ e+\eta f)
\]
with \(\eta^2+\eta+2=0\).
The triple determinant at \(0,1,3\) is \(\eta\).
Adding the augmentation row to columns \(2,4,5,6\) gives exactly the printed matrix with determinant \(4+\eta\).
Both determinants are \(2\)-adic units times \(2\), and translation or inversion preserves the required valuation via unit transformations or exchange of the two orbits.
All three-point minors of the four remainder columns of a complementary affine plane are units because any three points there are linearly independent modulo two.
The four augmented columns have binary rank three, and adding any point outside that plane gives rank four.

For a tightly occupied triple the adjugate contradicts the necessary divisibility by \(4\) since each aggregate coordinate is a unit.
For a tightly occupied quadruple with remainder zero modulo \(2^n\), \(n\ge2\), each component of the adjugate equation gives its augmentation times a unit congruent to the determinant times a unit modulo \(2^n\).
The right side has valuation \(v_L(2)<n v_L(2)\); thus the augmentation has exactly that valuation.
Two tight quadruples consequently have augmentation product of valuation \(2v_L(2)\), which is sufficient at precision four but impossible at eight.
This argument excludes lifts over every finite ramified extension, not just choices in the unramified splitting field.
The positive precision-four example for this case also follows in general by solving the two cubic systems separately over \(\mathbb Z_2\), leaving both augmentations even.

In each successful exact case the invertible minors solve the specified linear systems over the subfield \(\mathbb Q(\eta)\subset\mathbb Q_2\), with free coordinates chosen integral at the indicated place.
Its completion there is \(\mathbb Q_2\), since its closure contains the dense subfield \(\mathbb Q\).
The split Fourier equations give vanishing of the entire group-ring product.
For nontrivial cubic branches, all relevant maximal minors are nonzero in characteristic zero by the explicit determinant computation or their invertible reductions.
This agrees with the comparison to prime-order Fourier minors, without substituting a characteristic-zero result for the valuation calculation. [Tao, Lemma 1.3, journal p. 123](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2005/0012/0001/MRL-2005-0012-0001-a011.pdf#page=3)
With at least one additional occupied column, deletion of any one column preserves full row rank, permitting a kernel perturbation off all coordinate hyperplanes over this infinite number field while preserving residues.
Assigning one to all but the last occurrence of each class realizes each prescribed aggregate, including a zero aggregate of an even occupied class.

Independent exhaustive binary convolution of the \(127^2\) ordered nonempty mask pairs gives \(420\) zero products.
There are \(126\) involving a full indicator, \(98\) each of sizes \((3,4)\) and \((4,3)\), and \(98\) of size \((4,4)\).
Direct integer convolution of the two signed example factors yields coefficients \((-4,0,0,0,0,0,0)\) in order of the seven powers of \(X\).
Thus the finite table and the exact characteristic-zero cutoff hold at their stated scope.
The classification concerns lifts through the prescribed residue point for the projected equations.
It does not establish a lift or obstruction on any particular torsion-free group without the necessary projection data.
