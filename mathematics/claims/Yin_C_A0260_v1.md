---
author: Yin
---

# Two-coordinate tests when finite conjugacy classes are detected by virtual characters

## Statement

Let \(G\) be finitely generated and torsion-free, and write \(R=\mathcal R(G)\) for the actual star-regular closure.
Suppose every nonidentity \(g\) having finite conjugacy class belongs to a finite-index subgroup \(H\le C_G(g)\) with a homomorphism \(H\to\mathbb Z\) nonzero on \(g\).
Then all the [matrix-corner size alternatives](Yin_C_A0259_v1.md#statement) and the threshold \(\sup_L(b-h)_+<1/3\) for strong Atiyah hold over this same \(G\), including if \(G\) has nontrivial center.
They also hold for all finitely generated torsion-free amenable groups without a virtual-character assumption.
Here \(h,b\) are the joint and separate coordinate rank increments of the original group-ring matrix as in the [two-coordinate comparison](Yin_C_A0255_v1.md#statement).

More generally it suffices that every scalar projection \(p\in R\) have center-valued trace \(\tau(p)1\).
Under the stated virtual-character hypothesis the same proportionality holds for matrix projections over \(R\), with unnormalized matrix trace.
For an initial polynomial Schur matrix over such a group, the [polynomial column shears](Yin_C_A0257_v1.md#statement) satisfy \(\sup_v (b(v)-h)=\min(\delta,1-\delta)\) when the Schur kernel has trace \(\delta\).
The condition includes \(G=K\times\mathbb Z^s\) with torsion-free ICC \(K\) and \(s\ge1\): all finite-class elements are then supported in the abelian factor and are detected there.
These statements give criteria and quantitative consequences, without proving the required inequality for every such group.

## Center-valued ranks of finite graphs

For a group-ring matrix \(A\), the center-valued rank \(r_A\) of its image projection has zero Fourier coefficient at any element detected as in the statement.
Here are the two steps of the [virtual-character argument](Yin_C_A0016_v1.md#finite-index-detection-and-coprime-restrictions) for these polynomial inputs.
First, for a homomorphism \(\phi:G\to\mathbb Z\), twist each \(g\) to \(z^{\phi(g)}g\), \(|z|=1\).
On any fixed nonzero central cut \(q\), the twisted polynomial matrix has constant rank off a countable set of parameters by the [one-parameter rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) after clearing negative powers.
On the entire circle its rank on this cut is \(\tau(q\alpha_z(r_A))\), where \(\alpha_z\) is the trace-preserving twist automorphism.
The Fourier expansion makes the latter scalar continuous by dominated convergence in \(L^2\), thus constant everywhere.
Testing all \(q\) gives \(\alpha_z(r_A)=r_A\), so its coefficient at an element of nonzero \(\phi\)-height is zero.

For the virtual case restrict to \(H\) in the coordinates of a left transversal, and write \(x\) for the sum of the original image projection's diagonal entries.
The untraced sum of the new diagonal entries is \(\sum_{tH}E_H(t^{-1}xt)\), with \(E_H\) Fourier truncation to \(H\).
Since \(g\) is central in \(H\), taking the center-valued trace over \(H\) preserves the coefficient at \(g\).
Counting the repetitions of \(tgt^{-1}\) shows that this coefficient equals \([G:H]\widehat r_A(g)\): \(r_A\) averages \(\widehat x\) on the finite conjugacy class.
Applying the first step to the restricted polynomial matrix gives the desired vanishing.

For a projection \(P\in M_n(R)\), use the [polynomial equations for \(I-P\)](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix) to write \(P U^n=W(\ker_U L)\) for a constant coordinate projection \(W\) and a polynomial \(L\).
Rank-nullity after every central cut gives
\[
       Z_{\rm mat}(P)=r_{\binom{L}{W}}-r_L .
\]
The preceding virtual vanishing applies to both terms.
Every central element of the finite von Neumann algebra has square-summable Fourier coefficients constant on conjugacy classes and therefore has zero coefficients on all infinite classes.
The stated detection now leaves only the identity coefficient, which is the unnormalized scalar trace of \(P\).
For torsion-free amenable groups the [central-cut proportionality theorem](Yin_C_A0158_v1.md#central-cuts-in-a-torsion-free-amenable-group) gives the same conclusion directly.

## Packing when the center-valued ranks are scalar

If every scalar projection of \(R\) has constant center-valued trace, every nonzero such projection has full central support in \(\mathcal N(G)\).
Also any two such projections admit von Neumann comparison according to their ordinary traces, because the same comparison holds between their center-valued traces.
Consequently the supremum of \(\operatorname{rk}(qvp)\) for \(v\in\mathbb CG\) is \(\min(\tau(p),\tau(q))\) for any projections \(p,q\in R\), by \(L^2\) polynomial approximation of a comparison partial isometry.
These are the two uses of the factor hypothesis in the [minimal projection packing](Yin_C_A0259_v1.md#packing-a-minimal-projection) and [packing without minimal projections](Yin_C_A0259_v1.md#packing-without-minimal-projections).
In the first use the join of all group conjugates of \(p\) is its central support, so some \(qgp\ne0\) for nonzero \(p,q\).
The remaining module calculations and the [polynomial realization of a corner](Yin_C_A0255_v1.md#realizing-a-corner-by-polynomial-equations) apply without a factor assumption.
This yields every asserted size alternative and the two-coordinate threshold.
Applying the scalar center-valued trace identity to the Schur kernel projection gives the stated shear supremum.

## Assessment history

### Decision virtual-characters-and-the-same-group-threshold

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:07 |
| status | proved |
| reason | Independent review verified the Fourier vanishing, matrix graph argument and transfer of the packing estimates. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The virtual character condition, amenable alternative and the Schur shear supremum. |
| argument | [Center-valued ranks of finite graphs](#center-valued-ranks-of-finite-graphs) | Cut traces, virtual Fourier coefficients and the graph representation. |
| argument | [Packing when the center-valued ranks are scalar](#packing-when-the-center-valued-ranks-are-scalar) | The two replacements for factor comparison and the consequences for original ranks. |
| review | [Virtual characters and the same-group threshold](../audits/reviews/Yin_R_A0203_v1.md#virtual-characters-and-the-same-group-threshold) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-virtual-characters-and-the-same-group-threshold)
