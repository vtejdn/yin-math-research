---
author: Yin
---
# Generic sampling and finite moments on the coefficient variety

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0030_v1.md) for Yin on 2026-11-16T16:37 UTC.
The reviewer previously checked the analytic-family argument used here and had no role in developing this proof.
No exploration notes, author explanations, development discussion or prior verdict on this proof were supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0030_v1.md#statement) | Almost-sure simultaneous ranks, singular points, attainment, uniform gap and all three equivalent conditions on fixed supports. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0030_v1.md#argument) | Evaluation and dimension comparison, complex components, real algebraic approximation, support normalization and the finite-moment limit. |
| [Whole-argument finding](#whole-argument-finding) | [Analytic-family estimate](../../claims/Yin_C_A0028_v1.md#argument) | Lower bound on ranks of the maps on spaces of coefficient functions and a subsequence with successive dimensions of ratio tending to one. |

## Whole-argument finding

On a connected complex manifold, evaluations of a basis of \(V_{n+1}\) span its entire dual since no nonzero function in that space vanishes identically.
There is therefore a tuple on which the evaluation determinant is nonzero.
The determinant is holomorphic on a connected product manifold, so its zero set is volume null.
The product law of independent samples from any absolutely continuous distribution assigns zero probability to that set.
This reasoning allows a distribution supported in a proper measurable portion of the smooth locus.

On an invertible evaluation tuple, evaluation tensored with the identity identifies the output Hilbert module with a direct sum of \(d_{n+1}\) copies of the regular module.
The invertible map preserves the dimension of a closed submodule by polar decomposition on that submodule.
The evaluated closed image of \(T_n\) lies in the direct sum of closed fiber images by the evaluation identity and continuity of the map.
Taking expectations gives the stated upper bound, while the spectral-cut argument in the linked Claim gives the lower bound \(d_n\sup_p r(T(p))\).
The same spectral cut, stable on its initial subspace under a small norm perturbation, proves lower semicontinuity and hence measurability of rank.
Since the rank is bounded above by its supremum, the subsequence of adjacent dimensions of ratio tending to one forces equality with the supremum almost surely.
Intersecting the two events on the same component gives simultaneous attainment for both factors.

Separate nonzero rescalings normalize a chosen coefficient on each side, preserve the zero-product equations and preserve both ranks.
The smooth locus used is intrinsic to each reduced irreducible component of this finite-type complex variety.
Its analytic connectedness and density give the necessary manifold and ensure that every larger-than-threshold rank at a singular point is approached by such ranks on the smooth locus.
The finite number of components and the separate treatment of point components cover component intersections and dimension zero.
At a simultaneous attaining point the two ranks sum to at most one by range-kernel containment.
A singular half pair thus also forces both generic ranks on its component to be precisely one half.
In the unrestricted coefficient torus dominance of one coefficient gives an invertible operator after unit translation by a Neumann series, so the same generic-rank argument gives full rank for a factor with a density on that torus.

On each component the smaller rank consequently attains the minimum of the two separate suprema.
Taking the maximum over finitely many components gives attainment on the whole nonempty set \(Z\).
As the rank sum is at most one, this maximum equals one half precisely when a pair has both ranks equal to one half.
Its strict inequality otherwise yields the stated fixed-support gap even though the coefficient torus is noncompact.

In real and imaginary coordinates all equations have rational coefficients, and nonzero coefficients can be imposed by strict inequalities on squared moduli.
Existence in any rational open box meeting \(Z\) transfers from \(\mathbb R\) to the real algebraic numbers by quantifier elimination for real closed fields.
This yields complex algebraic coefficients dense in \(Z\), including near singular points, without requiring a chosen component to be defined over \(\mathbb Q\).
The two strict lower rank thresholds at a half pair hold in a common neighborhood by lower semicontinuity.
Conversely, attaining the supremum of the smaller rank upgrades arbitrarily close algebraic pairs to an exact complex half pair.

For the moment test, unit \(L^2\) normalization on \(m\) distinct support points bounds the squared operator norm by \(m\).
Then \((1-c^*c/m)^k\) decreases spectrally to the kernel projection, and its trace converges to the nullity.
Thus each pair's smaller moment bound increases to its smaller rank, and interchanging the two suprema gives the claimed limit of \(s_k\).
Every normalized torus solution yields a unit-norm solution, and every such sphere solution can be rescaled back to the coordinate slice with the same moments after unit normalization, since phases have no effect on \(c^*c\).
The exact-support unit-sphere constraints are semialgebraic in real coordinates, and each moment requires only finitely many coefficient products, conjugations and group equalities.
The conclusion concerns the supremum and limit, with no assertion that a finite moment order decides existence of a half pair.
