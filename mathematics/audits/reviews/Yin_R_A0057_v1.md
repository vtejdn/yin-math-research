---
author: Yin
---
# Unit propagation, cyclotomic norms and univariate coefficient equations

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0026_v1.md) for Yin on 2026-11-16T16:27 UTC.
The reviewer had checked the earlier binomial character criterion, and did not develop this derivation or receive its exploration notes, development discussion, author explanations or earlier verdicts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Coefficient table and statement](../../claims/Yin_C_A0026_v1.md#coefficient-table-and-statement) | All three assertions for actual fibers and nonzero coefficients. |
| [Whole-argument finding](#whole-argument-finding) | [Propagation along a projected line](../../claims/Yin_C_A0026_v1.md#propagation-along-a-projected-line) | Integral unit values, endpoints, enlargement, saturation and termination. |
| [Whole-argument finding](#whole-argument-finding) | [Arithmetic contribution](../../claims/Yin_C_A0026_v1.md#the-arithmetic-contribution-of-a-pinned-pair) | Forced third-term ratio, norm identity, prime-power coefficients and nonnegative relations. |
| [Whole-argument finding](#whole-argument-finding) | [Exact test](../../claims/Yin_C_A0026_v1.md#exact-test-with-one-remaining-direction) | Finite branch tests with zero or one residual direction and extension back to the label lattice. |

## Whole-argument finding

The oriented two-term equations require the value \(-1\) on their generators.
When consistent on \(L\), this assignment has finitely many extensions to the saturation \(S\) since the index is finite.
In Smith coordinates those extensions choose finite-order roots of prescribed signs.
A coefficient solution necessarily gives one of these branches.

At each propagation step, \(M/U\) is free, so every difference on the projected line is an integer multiple of its primitive direction modulo \(U\).
Shifting to the smallest exponent yields an ordinary polynomial with two nonzero algebraic-unit endpoint coefficients.
Only the interior coefficients can cancel on collecting like exponents.
Dividing by the leading unit and using transitivity of integrality proves that the direction value is an algebraic integer.
Reversing the polynomial proves the same for its inverse.
Saturation preserves the conclusion because a complex number whose positive power is a unit is itself a unit, by integrality for the number and its inverse.
The same argument applies to every direction eligible before a simultaneous enlargement, and each nonempty enlargement raises the rank.

In a triple, the third ratio must be \(-(1+\zeta)\), which excludes \(\zeta=-1\).
If an integer combination of its differences belongs to \(U\), the corresponding product of the forced nonzero values is an algebraic unit in their common cyclotomic field \(E\), even for negative exponents.
Its absolute norm must be one.
For \(\omega=-\zeta\) of order \(m>1\) the absolute norm in \(\mathbb Q(\omega)\) is \(\Phi_m(1)\).
Evaluating the cyclotomic factorization of \((X^m-1)/(X-1)\) at one gives \(p\) when \(m\) is a power of \(p\), and one otherwise, by induction over proper divisors.
In the larger field the norm is raised to the extension degree.
Division of its prime valuation by \([E:\mathbb Q]\) therefore gives exactly \(1/\varphi(m)\) in the prime-power case for that prime and zero elsewhere.
These additive valuations prove the relation test and the exclusion by a nonnegative relation with a positive prime contribution.
For a \(2\)-group quotient, all surviving pinned pairs have a positive contribution at two, including \(\zeta=1\).
This also verifies the stated obstruction from a parallel triple with distinct endpoints.

If residual differences span a rational line, a primitive direction in \(M/S\) gives integral exponents within each fiber.
Its polynomial includes the sum of all coefficients at each exponent before the gcd test.
After discarding identically zero polynomials and shifting away the smallest remaining exponent, each nonzero polynomial has nonzero constant term.
A positive-degree common gcd thus has a nonzero complex root, while a constant gcd rules out a common root by Bézout.
Both the case of identically vanishing polynomials and the case with no residual direction are included.
The preimage of the primitive direction is a direct summand of \(M\), since the quotient by it is free, so every passing assignment extends to a character on all labels.
This proves exactness for coefficient solvability in the stated one-direction scope.
