---
author: Yin
---
# Regular ranks along connected analytic families

A separate reviewing agent inspected the complete [fixed Claim](../../claims/Yin_C_A0028_v1.md) for Yin on 2026-11-16T16:31 UTC.
The reviewer inspected the four-point and two-coset inputs separately and received no development discussion, exploration notes, author explanations or prior verdict on the present derivation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0028_v1.md#statement) | Cross-point rank inequality on a connected complex manifold and the conditional boundary tests. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0028_v1.md#argument) | Filtered coefficient space, spectral projection, identity theorem and passage to the rank bound. |
| [Whole-argument finding](#whole-argument-finding) | [Nonhomogeneous triple](../../claims/Yin_C_A0028_v1.md#a-boundary-with-a-nonhomogeneous-triple) | Divisibility criterion, independence in the weight quotient, connectedness, boundary charts and the support exclusions. |
| [Whole-argument finding](#whole-argument-finding) | [Boundary phases](../../claims/Yin_C_A0028_v1.md#averaging-the-boundary-phases) | Averaging over all roots on the boundary, difference residues and the separated case. |
| [Whole-argument finding](#whole-argument-finding) | [Four-point input](../../claims/Yin_C_A0027_v1.md#four-point-rank) | Strict rank bound for a nonzero boundary sum on at most four elements of a torsion-free group. |

## Whole-argument finding

The mixed-point rank bound holds for the entire connected manifold.
The polynomial growth bound for \(d_n\) follows by counting monomials in a fixed finite set of generators, even when the generators satisfy relations.
Since \(d_n\) is positive and nondecreasing, an eventual ratio bounded below by \(1+\delta\) for any \(\delta>0\) would contradict that growth bound.
The coefficient spaces consist of actual holomorphic functions, so pointwise vanishing of a vector-valued element implies its vanishing in the finite tensor product by pairing with arbitrary Hilbert space vectors.
For the spectral subspace \(E\) of \(|T(p)|\) above \(\varepsilon\), norm continuity gives a lower bound on that same subspace throughout a neighborhood of \(p\).
An element of \(V_n\otimes E\ell^2(G)\) killed by \(T_n\) consequently vanishes as a function on the neighborhood.
The scalar identity theorem and connectedness make it zero everywhere.
The map is bounded and commutes with the right regular action, so polar decomposition shows that its range closure has dimension at least \(d_n\tau(E)\).
The limit of these spectral dimensions as \(\varepsilon\downarrow0\) is \(r(T(p))\).
Composition from \(V_n\) through \(V_{n+1}\) to \(V_{n+2}\) vanishes because the coefficient functions multiply pointwise and the original product vanishes identically.
Dimension comparison in the middle space therefore yields the stated inequality for any two choices \(p,q\), after taking a subsequence of ratios converging to one.

Divisibility of every actual fiber coefficient by the displayed trinomial makes the product zero on its torus curve.
In the single-triple criterion the rational dual weights annihilate all other fiber differences and assign independent coordinate axes to the two selected differences.
One common denominator gives the same exponent \(N\) in both axes and introduces only a common monomial on each fiber.
The base point \((1,1)\) lies on the curve because the three original terms cancel.
In the affine chart the roots of \(\gamma_0+\gamma_1s^N\) are simple and nonzero.
Continuation around such a root acts transitively on the \(N\) values of \(t\), so the unbranched portion is connected.
Adding the ramification points preserves connectedness, and deleting finitely many points from this smooth complex curve leaves it connected.
This includes \(N=1\).

Removing the separate minimum \(u\)-weights gives holomorphic families at every \(s=0\) point on the chart with \(t\ne0\).
At \((1,1)\) the compensating scalars are one, so comparison with the two original half ranks bounds each boundary rank by one half.
At \(t=0\) the same computation uses the minimum \(v\)-weights.
At infinity a torus monomial becomes \((Z/S)^{-(u+v)}(T/S)^v\), so clearing the pole selects the maximum \(u+v\) and all remaining phase factors are nonzero.
At each boundary the surviving coefficients on distinct group elements are nonzero and the product still vanishes.
This excludes a uniquely represented product and, for torsion-free groups, allows the requisite two-coset and four-point rank bounds.
Strict monotonicity on each of four occupied cosets leaves at most one minimal point per coset, as that application requires.

At \(s=0\) the \(N\) roots for \(t\) give all the stated phases with \(\tau(TT^*)=m\) independent of the root.
Trace Cauchy–Schwarz and \(r(T)\le1/2\) require the fourth moment at each phase to be at least \(2m^2\).
For a fixed \(g=xx'^{-1}\), averaging its squared Fourier coefficient preserves the cross terms exactly when their two exponents \(v_x-v_{x'}\) agree modulo \(N\).
This gives (4), with the identity contribution \(m^2\) because \(xx'^{-1}=e\) forces \(x=x'\).
Under residue separation the nonidentity terms contribute \(m^2-\sum_x|c_x|^4\), strictly less than \(m^2\) since the boundary support is nonempty.
The boundary tests require the stated curve through the original complementary pair.
