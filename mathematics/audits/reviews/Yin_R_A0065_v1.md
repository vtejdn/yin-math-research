---
author: Yin
---
# Finite tests for exclusion of two half ranks

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0034_v1.md) for Yin on 2026-11-16T17:16 UTC.
The reviewer had checked the earlier window, component and moment inputs, and worked on a different coefficient-variety result.
The reviewer received the topic of this investigation but no substantive development discussion, author explanations, exploration notes or prior verdict on this proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0034_v1.md#statement) | Uniform window bracket, finite exclusions and their converses with the indicated hypotheses. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0034_v1.md#argument) | Trace comparisons, torsion-free strictness, feasibility, window sampling, Følner limit and moment certificates. |
| [Whole-argument finding](#whole-argument-finding) | [Four-coset example](../../claims/Yin_C_A0034_v1.md#a-four-coset-table-with-both-kinds-of-component) | Actual fiber sizes, component decomposition, ranks, moments and the finite window. |
| [Whole-argument finding](#whole-argument-finding) | [Window comparison](../../claims/Yin_C_A0029_v1.md#a-finite-window-bracket-valid-over-every-field) | The complex trace comparison for scalar convolution on a finite input set. |
| [Whole-argument finding](#whole-argument-finding) | [Component sampling](../../claims/Yin_C_A0030_v1.md#statement) | Simultaneous attainment of the two generic regular ranks and the strict gap in the absence of a half pair. |

## Whole-argument finding

For fixed \(F\), the global range projection compressed to \(SF\) dominates the projection onto the ordinary window image.
The kernel projection compressed to \(F\) dominates the projection onto the exact kernel of the same map.
The constant diagonals of these two global projections give \(R_F(c)\le|SF|r(c)\) and \(|F|r(c)\le R_F(c)\).
Applying the two inequalities to each factor, taking the minimum and then taking suprema gives (1) with the maximum of the two output expansion factors.
The normalized window minimum takes only finitely many values on the nonempty set \(V\), so it has a maximum.

Equality in the window lower bound forces the compression of the kernel projection \(Q\) to equal the projection onto its window kernel by positivity and faithfulness.
Idempotence then forces \((1-e)Qe=0\) and hence commutation with \(e\).
Any nonzero Fourier coefficient at \(g\) forces \(y\in F\) exactly when \(gy\in F\), as the coefficient occurs between each such pair of coordinates.
The left stabilizer of a finite nonempty set is finite, since an element acting trivially fixes a point and equals the identity.
Torsion-freeness thus forces \(Q\) to be scalar, excluding equality when \(0<r(c)<1\).
This proves the claimed strictness separately for each factor at a half pair.

Both lower thresholds on the finite matrix ranks can be imposed on a single tuple by disjunctions of nonzero minors together with the exact-support equations.
For an individual geometric component its equations can be taken over the algebraic closure of \(\mathbb Q\), since the original variety is defined over \(\mathbb Q\) and geometric irreducibility persists over the algebraically closed extension to \(\mathbb C\).
On an irreducible component, one nonidentically vanishing minor for each positive maximal rank suffices to obtain both maximal ranks on a common dense open set.
Rank zero requires no such minor.
The analytic null-set result applies to each excluded proper closed subset on the smooth locus, and the union over countably many windows still has measure zero.
The finite upper certificate requires testing infeasibility of a higher threshold on all of \(V\).

When the subgroup of the two supports is amenable, windows in that finitely generated subgroup can be chosen with both expansion ratios tending to one.
Equation (1) then squeezes \(U_F(V)\) uniformly, since the expansion factor is independent of the chosen coefficients and ranks are bounded by one.
Attainment of \(t(V)\) makes absence of two half ranks equivalent to its strict inequality below one half, for the full variety as well as a component.
It follows that some window detects every negative instance under the stated amenability hypothesis.
On a component of a general group, \(h_k(c)\) increases to the individual regular rank by bounded spectral calculus.
Almost-sure attainment therefore gives a finite successful moment whenever that generic rank is above one half.
Conversely one strict moment anywhere forces a generic rank above one half, which excludes two half ranks throughout that component.

For the example, the four finite frequencies decouple after Fourier transformation in \(C_4\).
At each fixed output \(s\)-coordinate the heights have respectively \(4,8,4\) representations, since each of the permitted input height pairs has four representations on \(C_4\).
At each frequency the zero-product condition for the two degree-at-most-one factors forces at least one to vanish identically.
The assignments of complementary frequency sets give linear spaces before passage to the exact-support chart.
Each nonempty proper frequency subset has points active at every assigned frequency and with all inverse Fourier coefficients nonzero in both layers, by avoidance of finitely many proper linear hyperplanes.
Thus all the indicated components survive and are distinct after scalar normalization.
An active frequency has rank one on its circle, giving the two generic ranks with weight \(1/4\) per frequency.

At \(a=(1+t)p,\ b=(1+t)(1-p)\), both layers on both sides have all four coefficients nonzero.
The normalized \(j\)-th moment of \(b^*b\) is \((3/4)\binom{2j}{j}/(3/2)^j\).
At orders one through four this gives \(1,2,40/9,280/27\).
The numerator and denominator of the stated Gram bound are \(16/27\) and \(80/81\), yielding \(3/5\).
For \(F=C_4\) the window has one scalar input per frequency and contributes rank one exactly for an active polynomial.
The smaller window rank is at most one on the indicated component and reaches one, giving \(U_F=1/4\).
On a two-frequency component the dense open ranks really are \(1/2,1/2\), as claimed for this group with torsion.
