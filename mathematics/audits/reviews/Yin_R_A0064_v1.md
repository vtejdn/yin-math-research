---
author: Yin
---
# Boundary supports and Newton polygons in the coefficient variety

A separate agent checked [C_A0033 v1](../../claims/Yin_C_A0033_v1.md) from its statement through its example and two-parameter application.
The reviewer had prior context on the A0001 coefficient problem, had inspected the projective rank observation in L_A0040, and worked on the separate character and elimination tests in C_A0026 and C_A0032.
The reviewer did not develop C_A0033 or receive its author's derivation or a previous verdict on it.
The reviewed application explicitly requires affine span of the plane, as requested during this inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0033_v1.md#statement) | Component dimensions, edge roots, rank comparisons and label counts under the stated hypotheses. |
| [Whole-argument finding](#whole-argument-finding) | [Projective cuts](../../claims/Yin_C_A0033_v1.md#cutting-a-component-by-product-coordinates) | Segre hyperplane intersections, the finite support recursion and the zero-dimensional arithmetic conclusion. |
| [Whole-argument finding](#whole-argument-finding) | [Edge-root limits](../../claims/Yin_C_A0033_v1.md#each-edge-root-gives-an-actual-limiting-pair) | Unimodular coordinates, boundary fibers, rescaling, ordinary closure and the mixed-point rank inequality. |
| [Whole-argument finding](#whole-argument-finding) | [Counting boundary labels](../../claims/Yin_C_A0033_v1.md#counting-boundary-labels-around-the-polygon) | Distinct exponents, affine dimension two, vertex overlaps and opposite-face counts. |
| [Whole-argument finding](#whole-argument-finding) | [Two residual parameters](../../claims/Yin_C_A0033_v1.md#testing-a-branch-with-two-residual-parameters) | Curve factors, isolated points, the zero-polynomial case, the nine-label conclusion and the multiple-root calculation. |

## Whole-argument finding

On an irreducible projective variety of positive dimension a hyperplane avoiding its generic point cuts a nonempty section of dimension one less.
In the Segre embedding the coordinate \(a_xb_y\) is linear, and on each irreducible component of its zero section at least one of these two coordinate functions vanishes throughout.
The two projective factors remain nonzero and the bihomogeneous product equations persist.
After \(d\) cuts at least \(d\) support labels have disappeared, so the lower bound of sixteen on the two remaining support sizes gives \(d\le |A|+|B|-16\).
For total size sixteen the exact-support scheme has finitely many complex points as a set, and the density of algebraic points on its rationally defined locus forces every normalized point to be algebraic.
For the recursion, the two generic supports occur on the intersection of two dense open sets.
Every choice of a generically nonzero cell gives a valid cut and every resulting component omits at least one of its two labels.
These quantifiers give the minimum over cells outside the maximum over allowed subtables.
For dimension zero the non-discarded recursion is always at least zero.
The extra discarded small supports for a component containing a half pair follow from the separate upper rank bounds on its closure and the cited strict four-point and two-coset rank bounds.

Primitivity of the edge normal allows a unimodular coordinate change, including for each of the two normals to a segment.
After removing its least power of \(u\), the irreducible Laurent factor remains irreducible in \(\mathbb C[u,v^{\pm1}]\), since it is indivisible by \(u\) and localization adds precisely the powers of \(u\) to the units.
Its specialization at zero contains the distinct terms of the face and has a nonzero root.
Every such root belongs to the closure of the curve with \(u\ne0\), including repeated roots, by ordinary complex density of the nonempty Zariski-open subset of this irreducible variety.
In the two separately rescaled factors the least-degree terms survive with nonzero coefficients at exactly the asserted group labels.
Continuity of multiplication for these finite supports gives a zero product.
The numerical test in \(C_4\) has \(gb=b\) and \(a(s,t)b=((1+t)^2+s)b\), with \(a\) tending to \(1-2g+g^2\) along \(s=-(1+t)^2,\ t\to-1\).
It verifies the repeated-root limiting example on its stated group.

For the two regular ranks, [the holomorphic rank bound](../../claims/Yin_C_A0030_v1.md#rank-from-random-evaluations-on-a-connected-parameter-space) makes both suprema simultaneously attainable on the connected smooth locus of the irreducible curve.
Their sum is at most one.
Norm lower semicontinuity bounds each rank on the entire curve and on its limits after separate rescaling by the same supremum.
This proves the comparison between one boundary rank and the opposite rank at any curve point.
For a component containing a half pair, its corresponding two suprema are at most one half even when the half pair lies elsewhere on that component.
The \(2^{-69}\) separation has the indicated sign by [the four-point estimate](../../claims/Yin_C_A0027_v1.md#four-point-rank).

When a side's exponents are distinct and span the plane affinely, an exposed vertex would leave a single invertible group monomial in a zero product with a nonzero opposite factor.
The tested directions must therefore expose distinct edges of this side's polygon.
Only their shared vertices are counted twice, adding at most \(q\) extra incidences over \(q\) edges, whereas opposite faces are disjoint for the segment test.
Five labels per exposed face on a curve containing a half pair gives the bounds \(4q\) and ten, respectively.
The lower bound sixteen for the sum of the two face sizes gives \(14q\) and thirty-two when both sides satisfy the planar hypotheses.
A Laurent gcd accounts for all irreducible curves of a proper closed subset of the two-dimensional torus, since height-one primes in its coordinate ring are principal.
The other components are isolated points.
If all equations vanish identically, a generic direction exposing a single row label gives the direct monomial contradiction.
These alternatives imply the final nine-label conclusion with the affine-span qualification.

The cited [Nielsen–Soelberg support theorem](../literature/NS24/readme.md#author-manuscript), [complex rank specialization](../../claims/Yin_C_A0030_v1.md#components-and-exact-support), standard complex projective dimension and density facts, and the fixed small-support rank bounds were accepted at those scopes.
Maclagan's tropical minimum convention supplies terminology; the boundary lifting itself is proved by the coordinate calculation.
The complete argument supports the stated scoped conclusions.
