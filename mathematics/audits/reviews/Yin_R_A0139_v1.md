---
author: Yin
---
# Independent review of minimal zero-product supports and their coefficient fields

On 2026-11-21 at 05:25 UTC, a reviewer for Yin completed an independent inspection of the fixed statement and all six proof sections of C_A0103_v1, including the clarified scope of the boundary-prime criterion.
The reviewer took no part in developing this proof and received the fixed material and review scope without development notes, author explanations or an earlier verdict on it.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0103_v1.md#statement) | Simultaneous geometric inclusion-minimality, the five assertions, and the coarsening to the supporting subgroup's abelianization. |
| [Whole finding](#whole-finding) | [Finite Segre section](../../claims/Yin_C_A0103_v1.md#the-finite-segre-section-and-its-length) | Scheme-theoretic torus containment, the bound by Segre degree and uniqueness on both sides. |
| [Whole finding](#whole-finding) | [Normalized algebra](../../claims/Yin_C_A0103_v1.md#the-normalized-coefficient-algebra-and-a-finite-basis) | Finite grading, homogeneous unit basis, binomial presentation and separate generation by row and column degrees. |
| [Whole finding](#whole-finding) | [Supporting subgroup](../../claims/Yin_C_A0103_v1.md#the-symmetric-supporting-subgroup) | Correct coset sides, collision differences and the quotient onto the abelianization. |
| [Whole finding](#whole-finding) | [Coefficient fields](../../claims/Yin_C_A0103_v1.md#joint-coefficient-fields-and-character-quotients) | Coordinate field descent, invariant field, degree bounds, character action and multiplicity of its fibers. |
| [Whole finding](#whole-finding) | [Reduction primes](../../claims/Yin_C_A0103_v1.md#reduction-primes-and-the-boundary-condition) | All proper supports, exact criterion for boundary primes and valuation of normalized ratios. |
| [Whole finding](#whole-finding) | [Example and enumeration](../../claims/Yin_C_A0103_v1.md#a-characteristic-two-multiplicity-check-and-finite-enumeration) | Cyclic example, finite coefficient list and the separate group-realization condition. |
| [Whole finding](#whole-finding) | [Integral matrix criterion](../../claims/Yin_C_A0093_v1.md#statement) | Applicability of the all-characteristic full-row-rank criterion to the original table and every deletion with both sizes at least two. |

## Whole finding

The five assertions and the exceptional-prime criterion follow for supports minimal over an algebraic closure of the stated prime field.
The full \(p\)-part of the grading contributes to scheme length in characteristic \(p\), even when it contributes no new geometric coefficient points.

In the Segre embedding, any positive-dimensional projective component meets the hyperplane \(X_1Y_1=0\), giving a solution on a proper subrectangle.
Emptiness of this boundary for every coordinate puts the whole finite scheme in the torus, since restriction to an open containing its underlying points preserves its local rings.
To check the length bound, over the algebraic closure choose successive table hyperplanes avoiding all components of the current positive-dimensional section.
Each such choice exists because the base locus is finite, the ground field is infinite and the pure Cohen–Macaulay section has only its minimal points associated.
The sections remain pure Cohen–Macaulay effective Cartier divisors until dimension zero.
Taking \(a+b-2\) backward differences of the product of the projective-space Hilbert polynomials gives \(\binom{a+b-2}{a-1}\).
Restriction from the resulting finite section to its closed subscheme \(Z\) gives a surjection of coordinate algebras, which bounds the dimension even when \(Z\) has nilpotents.
The given coordinates and the single-factor section counts agree with the cited sources. [Segre embedding](https://stacks.math.columbia.edu/tag/01WD) · [Projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS)

For a fixed row solution, a right kernel of dimension at least two meets the hyperplane of vectors with their first coordinate zero in a nonzero vector.
Minimality excludes this, giving a unique normalized right factor, and the symmetric argument gives a unique left factor.
The quotient of the Laurent ring is graded by the presented group because each table equation is homogeneous.
Each degree has a unit, so finite dimension forces a finite group and multiplication by such a unit identifies each graded component with the degree-zero component.
Monomials in invariant-factor generators with exponents smaller than their orders have distinct degrees and span by this identification.
This proves the free basis and the binomial presentation over \(R_0\), including in residue characteristic dividing the orders.
For the quotient \(Q\) by all row degrees, twisting the columns by the basis of \(\bar k_0[Q]\) preserves the constant row equations.
The one-dimensional kernel over the field extends to a free kernel of rank one over that algebra, by splitting the original linear map over the field.
The first coordinate fixes the multiplier to \(1\), and each nonzero column coefficient then identifies the basis element for its quotient degree with the identity basis element.
Thus every column degree is zero in \(Q\), even for a nonreduced group algebra.
Interchanging the two factors gives the other generation assertion.

After translation the left factor preserves each summand supported on \(Ht\) for \(H=\langle A_0\rangle\).
Two nonzero right summands would give a proper support by restriction, so the identity in \(B_0\) puts all of \(B_0\) in \(H\).
Using \(t\langle B_0\rangle\) on the left proves the reverse containment of generated groups.
Equal products give precisely the abelianized sum relations needed for the surjection from \(\Gamma\).
For the additional localization formula, distinct row components of the collision graph have disjoint output sets and each would give a zero product on its own.
Thus the rows are connected, and each edge difference \(g_{i'}^{-1}g_i=h_{j'}h_j^{-1}\) in the translated labels belongs to the indicated intersection.
A path from the identity expresses every row generator as a product of edge differences and their inverses.

The one-dimensional right kernel descends to the field of the normalized left coordinates by linear elimination, including the normalization at the first entry.
The reverse descent accounts for both equalities of coefficient fields.
The image \(F\) of \(R_0\) is a finite-dimensional domain over the prime field, and a basis for the lattice of degree-zero exponents gives multiplicative generators for its evaluated monomials.
Thus \([F:k_0]\leq\dim_{k_0} R_0=\ell/q\).
The evaluated binomial generators have successive extension degrees at most their orders.
Over a finite field the \(p^s\)-th root of a coefficient in \(F\) already lies in \(F\), reducing the degree bound to the prime-to-\(p\) factors.
After adjoining the indicated roots of unity all the resulting separable binomials split in the compositum.
Their root ratios determine each automorphism and multiply under composition because the roots of unity are fixed.
This proves the claimed divisibility over the enlarged field and the upper bound over \(F\).

Over each geometric point of \(R_0\), the presentation gives \(q'\) distinct geometric solutions, each of fiber length \(q_p\), with \(q_p=1\) in characteristic zero.
Since the number of geometric points of \(R_0\) is at most its vector-space dimension, the total point count is at most \(q'\dim R_0=\ell/q_p\).
Two points in the same fiber differ by a character because the coordinate ratios are trivial on the lattice of degree-zero monomials, and freeness follows from the nonzero generating coordinates.
Coarsening to \(H_{\rm ab}\) repeats the unit-basis argument with its own kernel lattice and invariant algebra.
These twists use characters of the supporting subgroup \(H\).

For each single deletion with two sides of size at least two, the rational matrix has full row rank by complex minimality.
The reduction loses rank precisely at primes dividing the gcd of its maximal row-size minors.
The integral matrix for the full rectangle is already rank-deficient over the rationals, so all of its maximal row-size minors vanish in every residue field.
I checked the projective rank criterion at this use, including its allowance of subsets, and the one-label exception by injectivity of monomial multiplication. [C_A0093_v1](../../claims/Yin_C_A0093_v1.md#argument)
Every boundary point omits a row or column and is covered by one of the deletions.
Thus \(p\mid\Delta\) forces failure of geometric minimality for this pair, while existence of a full-support point in that characteristic is a separate question.
Outside the exceptional set, dividing each factor by an entry of minimum valuation leaves a nonzero reduction on each side, and the absence of a boundary forces every entry on that side to have the same valuation.

For the \(C_2\) example, elimination gives \(y=-x\) and \(x^2=1\).
The table relations identify the two degrees and give a cyclic grading of order two.
In characteristic two the sole solution has length two, as required.
Finally, there are finitely many partitions for fixed sizes, and the normalized coefficients of every complex-minimal partition form a finite zero-dimensional algebraic set over \(\mathbb Q\).
Computing these sets enumerates candidates before imposing group realization.
The result supplies necessary conditions on a proposed counterexample and leaves the torsion-free zero-divisor conjecture open.
