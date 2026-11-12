---
author: Yin
---
# Commutation determinants and return-language obstruction: independent whole-artifact review

Review performed at 2026-11-11T12:23 (UTC minute).
The human record author is Yin.
The reviewed artifact is the 2026-11-11 revision of [Yin_L_A0016_v1](../../ledger/Yin_L_A0016_v1.md), including every numbered formula (1)--(21), the intervening derivations and the concluding strategy limitations.
This inspected revision includes the explicit reciprocal definition preceding (19) and the final route-specific sentence allowing a weaker sufficient compatibility condition.

The reviewer was outside substantive development and received the fixed artifact, its necessary dependencies, the review assignment and operational rules without proof-generation dialogue, mathematical development summaries or prior review conclusions.
The fixed argument was inspected before recording the findings below.
No earlier R finding was used as proof evidence, and no substantive repair was supplied or made by this reviewer.
The direct source interfaces listed below were read in their identified primary sources; their complete proofs were not independently audited.
The review covers the fixed L artifact and its stated implications, not future revisions of S_A0006 or S_A0007 and not completion of A0001.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0016_v1](../../ledger/Yin_L_A0016_v1.md) | Complete 2026-11-11 artifact: formulas (1)--(21), all derivations, source conventions and strategy limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Tree and lattice transforms](../../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms) | Exact transforms, analytic normalization and correction derivative. |
| [Whole-artifact finding](#whole-artifact-finding) | [Root deletion](../../ledger/Yin_L_A0016_v1.md#what-root-deletion-actually-changes) | Compressed resolvent, off-diagonal counts and tautological substitution. |
| [Whole-artifact finding](#whole-artifact-finding) | [Nonbacktracking correction](../../ledger/Yin_L_A0016_v1.md#a-finite-nonbacktracking-determinant-correction) | Unnormalized edge trace, local determinant algebra, change of variable and physical continuation. |
| [Whole-artifact finding](#whole-artifact-finding) | [Primitive returns](../../ledger/Yin_L_A0016_v1.md#primitive-returns-and-their-critical-growth) | Root-closed identity products, inversion, coefficients, critical growth and convergence radii. |
| [Whole-artifact finding](#whole-artifact-finding) | [Boundary residues](../../ledger/Yin_L_A0016_v1.md#boundary-residues-and-failure-of-an-algebraic-cavity-repair) | Edge asymptotics, nonalgebraicity, imaginary-axis limits, atomlessness and scope of the obstruction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Language obstruction](../../ledger/Yin_L_A0016_v1.md#even-cyclic-root-closure-and-positive-moments-do-not-suffice) | Integer nonnegative necklace multiplicities, cyclic/root closure, positive aggregate moments and failure of group-identity realization. |
| [Whole-artifact finding](#whole-artifact-finding) | [Strategy consequences](../../ledger/Yin_L_A0016_v1.md#consequence-for-the-two-strategies) | What the fixed calculations exclude and what remains unproved. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0015 boundary residues](../../ledger/Yin_L_A0015_v1.md#boundary-residues-and-reciprocal-slopes) | Scalar reciprocal convention and the direct dominated-convergence residue criterion used in the present artifact. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0015 cyclic products](../../ledger/Yin_L_A0015_v1.md#torsion-free-cycle-arithmetic-and-its-obstruction) | Scalar full-alphabet specialization of the primitive-word product and the fractional-law antecedent; no broader independent review of L_A0015 is asserted. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0015 geometric comparison](../../ledger/Yin_L_A0015_v1.md#a-geometric-index-mechanism-beyond-algebraicity) | The first-order tree/lattice discrepancy and the stated scope of the tree source comparison. |
| [Whole-artifact finding](#whole-artifact-finding) | [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract) | Comparison of the pilot's scalar special cases with the all-groups, all-sizes complex-coefficient target; no completion finding. |

## Whole-artifact finding

No substantive mathematical gap was found in the exact formulas, the constructed language obstruction or their stated calibration scope.
The finite operator determinant supplies an all-orders commutation correction, while its analytic behavior excludes the proposed finite algebraic-factor representation.
The language example establishes the insufficiency of the listed generic cyclic and positivity properties, without providing a group-ring counterexample.
The following checks are the grounds for that conclusion.

### Transform, normalization and deletion checks

For (1), bounded spectral support permits differentiation of the principal logarithmic potential on the upper half-plane.
The unit-mass normalization fixes the multiplicative constant at infinity.
The identity relating D to Phi is first read on the small lower-half-plane sector in t where 1/t lies in the upper half-plane, and then as the normalized germ.
Thus the inversion of variables does not silently identify incompatible logarithm branches.

For (2), the cavity equation gives z=m^{-1}+3m and the original root contributes four branches.
Differentiating the logarithm of 1/[m(1-m^2)] gives m/(1-m^2), and its leading term at infinity is z.
These observations verify both the Cauchy transform and its determinant normalization.
The full return count in (3), the integral definition of K and its even expansion give (4) with modulus 4/z and with no missing degree-four rescaling.
Substitution into the tree formulas gives the displayed expressions for M_T and D_T, and differentiation gives both equalities in (5) with their stated signs.

The four diagonal, eight ordered adjacent and four ordered opposite neighbor pairs give exactly the coefficients in (6).
The deleted-graph path counts have lengths zero and two on a diagonal, length two between adjacent neighbors, and minimum length four with two choices between opposite neighbors.
They therefore give the recorded first self-energy discrepancy.
In (7), matrix inversion after deleting the root subtracts the product of two resolvent entries divided by g_0.
Translation and reflection symmetry identify those entries, so the products are analytic squares.
The two full-resolvent equations then make the proposed substitution into (6) an identity, as claimed.

### Determinant and continuation checks

Formula (8) counts the last-to-first prohibition as well as all successive prohibitions.
Its trace is the usual four-by-four matrix trace composed with the group trace, without division by four.
The constant vector has eigenvalue three for ee^T-J and its orthogonal complement has eigenvalues of modulus one; hence the stated norm bound and convergence disk follow.

For the direct proof of (9), R=JU is a selfadjoint involution with zero edge trace.
Its determinant factor is consequently (1-s^2)^2.
Also rRe=4 and re=A_G, so the rectangular factor in the displayed calculation is correct in the actual, possibly noncommutative, group algebra.
Removing its scalar denominator contributes one inverse factor of 1-s^2 because the vertex trace of the identity is one.
This leaves the exponent one in (9).
Cyclicity of the trace verifies the local logarithmic determinant operations used here; the argument does not require global multiplicativity for arbitrary logarithm branches.

There are no nonempty reduced identity words in the free group, so N_T=1.
Factoring 1-sA+3s^2 as (1+3s^2)(1-tA) proves (10), including its normalization at zero.
The inverse substitution s=m(z), together with (2), gives both parts of (11).
The composition outside the cycle-series disk is correctly designated as analytic continuation.
On the imaginary axis its polynomial factor has real part (1-3r^2)I>0, which supplies the stated logarithm branch up to, but not including, the limiting boundary point.
The cycle series is not evaluated termwise at that boundary.

### Primitive counts and singularity checks

For (12)--(13), the two identity languages are closed under powers and primitive roots, and free identity words form a subset of commuting identity words.
This makes the difference of primitive-class multiplicities nonnegative, rather than merely giving an arbitrary formal quotient of Euler products.
Each primitive class of length d contributes d rooted words at every multiple of d, yielding the stated Mobius inversion.
The full-alphabet bound gives absolute convergence for |t|<1/4.

Exact expansion of the tree generating function gives the even moments 4, 28, 232 and 2092.
Together with (3), these give the three coefficients in (14) and primitive counts 2, 28 and 350.
Expanding the rational substitution gives the nonbacktracking logarithm coefficients -2, -4 and -27, hence rooted counts 8, 24 and 216 and primitive counts 2, 4 and 26.
This confirms the distinction between full-alphabet and nonbacktracking primitivity.

For (15), Stirling gives the dominant lattice term 16^n/(pi n), while the tree term is bounded by 12^n.
In the divisor inversion every proper divisor contributes at most exponential order 4^n, up to a polynomial factor, so it does not alter the claimed leading term after division by 2n.
Odd counts vanish by parity.
At the critical t value, the logarithmic determinant sum is bounded by a convergent multiple of the sum of n^{-2}; the limiting correction is therefore positive.
The elliptic asymptotic gives (16) with coefficient 1/pi and proves a logarithmic derivative singularity despite zero local power exponent.
The nonzero endpoint value prevents that singularity from being explained by a vanishing analytic factor.
Together with the existing convergence bounds and the nonzero substitution derivative 3/8, this establishes the two exact radii claimed in the text.

### Boundary and nonalgebraicity checks

The complementary elliptic modulus squared at z=4+delta is delta/2+O(delta^2).
Substitution into the cited asymptotic gives the coefficient 1/(4 pi) and the constant 32 inside the logarithm in (17); the tree value is 3/8.
The polynomial-coefficient contradiction for the logarithmically divergent q is valid: after the stated division, a positive power of delta dominates every remaining logarithmic power.
Finite algebraic extensions are closed under differentiation, sums and quotients, so finite products of algebraic functions with fixed complex powers have algebraic logarithmic derivative wherever their branches are defined.
This verifies the excluded representation and the nonalgebraicity consequences for C, R and N_Z.
It does not exclude a finite formula involving transcendental functions or a separate argument controlling only residues.

The torus map in (18) is a surjective finite covering and sends Haar measure to Haar measure.
Integrating one cosine coordinate gives the reciprocal square-root integral with negative imaginary sign, and its elliptic modulus gives exactly the constant 16 in the imaginary-axis asymptotic.
The tree limit has the stated negative sign.
Using the explicit scalar reciprocal definition F_Z=1/g_Z, consistent with the directly cited L_A0015 setting, proves every limit in (19).
This is an infinite reciprocal slope with zero atom mass.

The lattice level sets have zero measure by the stated fixed-coordinate fiber argument.
The tree transform has finite boundary values on its support, including its endpoints, and is analytic off that support.
The dominated-convergence boundary-residue criterion therefore excludes all atoms in both laws and gives zero residue for their logarithmic-derivative difference at every real point.

### Language obstruction and strategic scope

The Catalan expansion places D_* in 1+t Z[[t]], and coefficientwise Euler elimination gives integer exponents.
Logarithmic differentiation gives (20); comparison with primitive four-letter necklaces gives nonnegativity as well as the asserted asymptotic growth.
Thus taking exactly half of the necklaces at each length is possible.
Rotation and passage to a positive power preserve the primitive necklace, which proves both language identities.
Counting its d distinct rotations at a multiple of d gives (21), including the separately specified zeroth moment.
The displayed two-point probability law realizes these aggregate moments and the fractional local exponent.

The obstruction to group-identity realization is decisive already at lengths one and two.
Exactly two letters would have identity labels; root closure prevents either other label from squaring to the identity, leaving at most the four identity-label pairs and the two mixed nonidentity pairs.
Their total cannot reach the required count eight.
The torsion-two label example correctly realizes the aggregate law once root closure is dropped.
This checks the new obstruction without importing an Atiyah premise.

The strategy consequences are supported as restrictions on the mechanisms tested here.
In particular, these examples prove that the listed cyclic and aggregate positivity properties alone cannot supply the desired quantization.
They do not prove that a successful argument must retain every item of the full joint distribution, as opposed to some stronger but smaller compatibility condition.
The final statement about retaining full group-word compatibility is explicitly limited to the proposed route and allows a weaker sufficient compatibility condition.
Likewise, the fixed four-by-four operator matrix still has coefficients in the actual group algebra and supplies no independent solution of its rank problem.
The scalar free and abelian pilots do not satisfy the all-groups, all-matrix-sizes completion criterion of A0001.

## Source applicability and review limits

The source interfaces were checked independently at the following exact locations:

- [Gut10, arXiv:1004.1435v1, Section 1, equations (4), (6), (8), (10)](https://arxiv.org/html/1004.1435v1): the lattice structure function is the adjacency symbol divided by four, and the return counts agree after this rescaling.
  The nearby hypergeometric argument ambiguity is real; the local modulus integral and coefficient derivation avoid relying on that ambiguous display.
- [GIL07, arXiv:math/0605753v3, Lemma 4.2, Theorem 6.5 and Lemma 7.1(ii)](https://arxiv.org/html/math/0605753v3): the free translation actions on the tree and square lattice satisfy the periodic simple-graph hypotheses, with one vertex representative, degree four and Euler characteristic minus one.
  The source zeta is the inverse of the artifact's N, giving the same determinant sign, exponent and regular-graph disk.
- [BBGSS23, arXiv:2309.00437v1, equations (1.3), (1.5), (2.1) and Theorem 2.1, equation (2.6)](https://arxiv.org/html/2309.00437v1): the bouquet with one vertex and two geometric edges satisfies the stated tree setting.
  Changing from the source resolvent and logarithm conventions negates both its scalar Green function and its one-vertex exponential potential, giving the artifact's formula.
- [DLMF 19.12.1 and the value d(0) following 19.12.3](https://dlmf.nist.gov/19.12): the leading term is log(4/k') with the claimed next-order bound on the real approach used here.

These are statement, convention and applicability checks, with the displayed local derivations independently inspected.
They are not full proof audits of the external papers or a historical-priority survey.
Finite coefficients were recomputed by exact algebra from the displayed generating functions; no numerical experiment or formal verification is claimed.

The local reciprocal definition and the explicit route-specific qualification were checked at their actual uses.
They clarify the already inspected convention and the limited strategic implication without altering a formula or adding a proof step.
No formula repair, source-dependency repair or additional mathematical hypothesis is required for the supported fixed-artifact conclusion.
