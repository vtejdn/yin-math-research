---
author: Yin
---
# Eliminating one vector of group-ring coefficients

A separate agent reviewed the entire [fixed Claim](../../claims/Yin_C_A0032_v1.md) for Yin on 2026-11-16T17:20 UTC.
The reviewer shared the Task context and had worked on specific product tables, but took no part in developing this Claim and received no development notes, proof-generation discussion, author explanations or earlier conclusions on its argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0032_v1.md#statement) | Exact support feasibility, branching hypotheses and limits of the two-variable test. |
| [Whole-argument finding](#whole-argument-finding) | [Full support and rank strata](../../claims/Yin_C_A0032_v1.md#full-support-and-rank-strata) | Column-deletion criterion, pivot witnesses and combined coefficients in minors. |
| [Whole-argument finding](#whole-argument-finding) | [Character equations from minors](../../claims/Yin_C_A0032_v1.md#character-equations-from-minors) | Relation test, saturation, torus splitting and projected pivot inequalities. |
| [Whole-argument finding](#whole-argument-finding) | [Curves and isolated solutions in two variables](../../claims/Yin_C_A0032_v1.md#curves-and-isolated-solutions-in-two-variables) | Common components, residual resultant, specialized gcds and recovery. |

## Whole-argument finding

The stated tests give the exact coefficient feasibility decision within their specified range.
For fixed right coefficients, the actual product rows give the asserted linear map.
The kernel projects nontrivially to a given coordinate exactly when its column is redundant.
If every such projection is nonzero, the product of its restrictions is a nonzero polynomial on the kernel over the infinite field \(\mathbb C\), so a vector with all coordinates nonzero exists.
Choosing a surviving minor separately for each deletion yields precisely the rank strata and handles a one-column matrix through the empty list of admissible ranks.
A determinant can use a label repeatedly, and grouping by the exponent vector sums the full signed multiplicity before any binomial ratio is read off.

An assignment on the list of exponent differences descends to their generated lattice exactly when it is trivial on the integral relation kernel.
In Smith coordinates the extensions to the saturation choose all roots of finitely many nonzero algebraic numbers, independently along its invariant factors.
Each choice extends over a complementary free summand, so this list covers every coefficient vector satisfying the binomials.
Upon combining equal terms, dividing each remaining equation by its own monomial leaves all exponents in the common difference lattice.
For fixed coordinates on its saturation the pivot product is a Laurent polynomial in complementary variables.
It can take a nonzero value exactly when at least one of its grouped coefficients is nonzero, including when the complement has rank zero.
Thus projecting the inequalities loses no simultaneous pivot requirement.

The constant and univariate checks exclude the zero coordinate and cover empty equation lists.
In the plane, over the algebraic closure of the coefficient field, every irreducible curve of the common gcd meets the torus because coordinate factors were removed.
A pivot coefficient outside its prime ideal gives a nonempty open subset there.
On dividing by the common gcd, every remaining irreducible factor of a chosen nonconstant residual equation fails to divide at least one other residual equation.
Reducing the parameterized linear combination modulo that irreducible gives a nonzero polynomial in the combination parameter over a domain.
Only finitely many integer parameter values are excluded in all.
For the resulting coprime pair, passing to the rational function field in \(X\) gives a nonzero \(Y\)-resultant when at least one polynomial has positive \(Y\)-degree.
Its polynomial combination identity persists even at a simultaneous drop in leading degree, so every common affine point is detected.
If both polynomials only use \(X\), coprimality already rules out all common points.
At every candidate nonzero \(x\), some residual equation specializes to a nonzero polynomial, since otherwise \(X-x\) would divide them all.
The specialized gcd and the projected pivot inequalities decide membership even at a degree drop.
These arguments also cover vertical curves, constant residual equations and intersections between a component of the gcd and a residual solution.

The factor can be recovered by linear algebra from any passing full set of right coefficients.
The comparison to the one-direction test supplies no premise to this proof.
This review concerns the prescribed finite multiplication table and its coefficient equations.
A surviving branch of higher difference rank retains its stated limitation, and a zero product alone supplies no value for the regular rank in the Task contract.
