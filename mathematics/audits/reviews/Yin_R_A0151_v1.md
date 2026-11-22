---
author: Yin
---
# Independent review of central specialization at finite inverse depth

## Whole finding

At 2026-11-22T04:11 UTC a reviewer acting for Yin independently checked C_A0114_v1, including the specialization estimate, both directions of the layer criterion and the Schur application.
The reviewer received the fixed Claim and the review assignment and took no part in proof development.
The reviewer consulted the cited source inspection of the layer definition, the complex-parameter rank estimate, the generic rational-rank statement, the explicit polynomial realization and the affiliated elimination identity.
The assignment supplied no development dialogue, private explanation or previous review conclusion about this Claim.
Both the equivalence at each fixed depth and the single-specialization criterion follow from the proof.

For \(l>D\) distinct values and any \(s_0\), use input vector polynomials in \(s-s_0\) of degree less than \(l-D\) with coefficients in the initial support of \(T(s_0)\).
If the least nonzero coefficient is \(v\) in degree \(k\), the coefficient of degree \(k\) in the product by \(T(s)\) equals \(T(s_0)v\ne0\).
The product has degree less than \(l\), so evaluation at the \(l\) points is injective on the resulting polynomials by the scalar Vandermonde identity.
The composite is a bounded injective module map into the direct sum of the closed output ranges.
By polar decomposition its range closure has dimension equal to that of the input.
This yields \((l-D)r(s_0)\le\sum_{s\in E}r(s)\), with the same trace normalization as the Claim.
Taking the supremum in \(s_0\) gives total deficit at most \(Dr_*\), which also holds immediately for \(l\le D\).
Since \(r_*\le\min(m,n)\), this proves (2) for the whole complex line, including when \(D=0\).
Any finite collection of deficits at least \(1/h\) has at most \(hDr_*\) members.
The exceptional set is countable, and the supremum is attained elsewhere, including almost everywhere on the circle.
Multiplication by a power of \(s\) preserves each rank at nonzero \(s\).

Under Fourier transformation of the cyclic coordinate, bounded coefficients are measurable fields and the product trace integrates their fiber traces.
For a square denominator the kernel and adjoint kernel are decomposable, and full rank almost everywhere gives a measurable closed inverse field.
One may see the latter by applying spectral truncations to the inverse modulus in the polar decomposition.
The finitely many group elements in the syntax generate a countable subgroup in the \(H\) coordinate.
Restriction to that subgroup preserves kernel traces and reflects invertibility, since the regular action of the larger group restricts to copies on cosets.
It follows by induction over the finite expression that the evaluation of each inverse gate exists almost everywhere and the final fiber element belongs to the same or a lower inverse layer.
The resulting common conull domain supplies the nonempty torus evaluation domain needed for the rational specialization statement in C_A0012_v2.

The block realizations for a sum, product and inverse in C_A0012_v1 apply inside the actual affiliated algebra of the product group.
In particular one can apply that recursion to the constant family with coefficients in the group ring of \(H\times\mathbb Z\).
At an inverse gate the previous denominator is a unit, and elimination identifies the new bordered denominator with the direct sum of that unit and the expression being inverted.
This checks the unit premise in the larger algebra before taking fibers, even when none of the gates is known to be defined at the particular central phase \(1\).
The resulting denominator and border are finite group-ring matrices, hence have bounded Laurent coefficients over \(H\).
Outside a countable set their ranks equal their respective maxima.
On the common conull domain the first maximum equals the full denominator size, and subtraction of that size from the border rank gives the same scalar rank in every such fiber.
Integration preserves this constant.
Under \(P_j(H)\) it is zero or one for every expression at depth at most \(j\).
Faithfulness and equivalence of the initial and final supports give the asserted dichotomy in the actual affiliated algebra.

Conversely, the trace-preserving inclusion sends each allowable inverse expression over \(H\) to the same expression at the same depth in the product.
Its scalar support traces are unchanged, so a nonzero nonunit in \(D_j(H)\) stays a nonzero nonunit there.
Every finite expression over a torsion-free abelian factor uses only a finitely generated free abelian subgroup, and restriction to this subgroup again reflects invertibility.
Iteration thus proves the equivalence for arbitrary such factors.
For the matrix certificate the rank-two specialization forces maximal rank two for the polynomial border at all but countably many phases, even when the given value lies off the circle or the first pivot vanishes at that particular value.
The nonzero pivot has full rank in the product by the depth-zero equivalence.
Ordered affiliated elimination gives scalar complement rank one.
The displayed evaluation at \(1\) is triangular with two units, and its off-diagonal coefficient does not affect its invertibility.
The proof leaves a constant matrix of unknown rank over \(H\) at that same rank.

At 2026-11-22T04:14 UTC the same reviewer independently checked the additional assertion and proof for the two row groups \(H_i\times\langle z\rangle\), using the free product criterion in C_A0111_v1.
A nonzero scalar coefficient \(a_g(z)\) excludes only finitely many phases, so \(P_0(H_1)\) gives the pivot inverse in the fibers and hence in the product.
This step uses no density hypothesis on arbitrary elements of \(\mathbb CH\).
If the second row is nonzero, one of its scalar coefficient polynomials likewise keeps the specialized row nonzero outside a finite set.
The free product criterion thus restricts every remaining fiber rank to one or two, and (2) makes one of these the almost-everywhere rank.
At rank one the proportionality scalar of the two specialized columns equals \(b_g(\lambda)/a_g(\lambda)\) for almost every phase, since the first pivot has nonzero \(g\)-coefficient there.
For every group label the corresponding coefficients of \(a_g b-b_g a\) and \(a_g d-b_g c\) are scalar Laurent polynomials vanishing on this conull set, so both identities hold over the Laurent polynomial ring.
This gives one common \(f=b_g/a_g\) in \(\mathbb C(z)\), including \(f=0\) when \(b_g=0\).
Every nonzero scalar Laurent denominator is an affiliated unit by its almost-everywhere nonvanishing, so \(\mathbb C(z)\) acts centrally in the product and the proportionality implies \(ca^{-1}b=fc=d\).
For generic rank two, integration and the global pivot give complement rank one and hence an affiliated unit.
If the second row vanishes, the complement is zero directly.
This establishes the stated criterion even when only the factor groups satisfy \(P_0\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0114_v1.md#statement) | Both directions for every fixed finite depth and arbitrary torsion-free abelian central factor, the full-rank one-value test and vanishing of the two-row Schur complement over a common central cyclic subgroup. |
| [Whole finding](#whole-finding) | [Specialization estimate and argument](../../claims/Yin_C_A0114_v1.md#a-bound-on-the-total-rank-lost-by-specialization) | The complete argument from the sharper existing rank bound through the fiber proof, the one-value test and the two-row criterion over the central cyclic subgroup. |
| [Whole finding](#whole-finding) | [Generic fiber](../../claims/Yin_C_A0114_v1.md#the-rank-at-a-generic-phase-for-a-finite-inverse-expression) | Defined expressions, rank constancy, reflection of subgroup invertibility and iteration. |
| [Whole finding](#whole-finding) | [Schur certificate](../../claims/Yin_C_A0114_v1.md#a-second-order-certificate-on-the-actual-regular-group) | Product-group invertibility from regular rank at one nonzero complex value, the example and the constant-family limit. |
| [Whole finding](#whole-finding) | [Two rows sharing the central cyclic subgroup](../../claims/Yin_C_A0114_v1.md#two-rows-sharing-the-central-cyclic-subgroup) | The factorwise pivot premise, the globally common rational proportionality scalar, both rank outcomes and the zero-row case. |
| [Whole finding](#whole-finding) | [Free-factor two-row criterion](../../claims/Yin_C_A0111_v1.md#statement) | The single common complex coefficient ratio at each rank-one fiber with nonzero pivot and nonzero second row, and rank two in the remaining case. |
| [Whole finding](#whole-finding) | [Finite layers](../literature/Yin20/Yin_U002.md#61-definition-iv55-and-all-parts-of-remark-iv56) | The finite scalar-inverse recursion in Remark IV.5.6(iv). |
| [Whole finding](#whole-finding) | [Complex-parameter Vandermonde bound](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | The input-support dimension argument giving total rank deficit at most degree times supremal rank on the complex line. |
| [Whole finding](#whole-finding) | [Generic rational-rank theorem](../../claims/Yin_C_A0012_v2.md#statement) | Constancy on the circle for a finite rational expression with a nonempty gatewise-defined domain. |
| [Whole finding](#whole-finding) | [Polynomial realization](../../claims/Yin_C_A0012_v1.md#rational-expressions-and-explicit-polynomial-schur-realizations) | The algebraic block recursion applied in the product-group ambient where the expression is defined. |
| [Whole finding](#whole-finding) | [Schur rank identity](../../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) | Ordered multiplication with a certified affiliated unit pivot and the consequent rank difference. |
