---
author: Yin
---

# Tolsa's corona packing and curvature transfer

<a id="tol05-u001"></a>
## Linear growth, good sets and the image top family

The inspection on 2026-11-14 used the [published edition](readme.md#yin-edition).
Theorem 1.3, p. 1246, bounds the total squared Menger curvature of the image of a compactly supported measure under a bilipschitz map of the plane, assuming unit linear growth and finite curvature.
The bound is a constant depending on the map times the sum of the initial curvature and mass.
The definition on p. 1245 takes uniform operator norms of the hard Cauchy truncations outside the radius-\(\varepsilon\) disk for every \(\varepsilon>0\).
Theorem 1.4, p. 1247, transfers this \(L^2\) boundedness under a global bilipschitz map for a nonatomic Radon measure.
The paper uses the kernel \(1/(w-z)\) at the output point \(z\), whose negative has identical truncation norms.

Main Lemma 3.1, p. 1250, constructs a family of doubling top squares with finite packing sum \(P=\sum_R\theta_\sigma(R)^2\sigma(R)\), where \(\theta_\sigma(R)=\sigma(R)/\ell(R)\).
Its sets \(G_{1/2}(R)\) in Lemma 5.2(d), p. 1268, lie in \(R/2\) and have uniformly bounded overlap.
For the same family, (5.7), p. 1270, bounds \(P\) by twice the contribution \(P'\) of squares outside the very concentrated class.
In §5.3, p. 1271, (5.8) subdivides that contribution into low-density stops, high-curvature stops and the good sets.
Equation (5.10) bounds the first weighted sum by \(\eta P'\), with the choice \(C_{17}\eta\le1/2\).
Equation (5.11) bounds the high-curvature sum by a constant times the total curvature, using doubling to pass from stopping squares to their fourfold dilates.
The weighted good-set sum is exactly the left side of (5.12).
There the paper uses the global growth bound \(C_0\) and bounded overlap to obtain a multiple of \(C_0^2\sigma(E)\).
Remark 5.4, p. 1272, justifies the original packing bound by finite truncation and the terminal-square estimate after (5.13).

Main Lemma 8.1, pp. 1290–1291, bounds image curvature by the packing sum for a family of doubling image squares containing a root and satisfying its three local curve and density conditions.
Section 8.1 applies it to the push-forward of the family in Main Lemma 3.1.
In particular the image of an Ahlfors–David regular curve remains regular, and the distortion of the annular integral in condition (b) is bounded by the inverse Lipschitz constant.
The root term in §8.2, p. 1292, is already controlled by the root density squared times the total mass.

The mathematical inputs retained here are the two main lemmas, the specified intermediate inequalities and the geometric push-forward in §8.1.
Their statements, the relevant stopping terms and the passage between the top families were inspected.
The construction of the regular curves and the proofs of the high-curvature and low-density estimates are accepted at the stated hypotheses.
The replacement of (5.12) by an integral of the squared maximal density and the passage to measures with unbounded growth are project deductions in the [application to marginal vacua](../../../claims/Yin_C_F0256_v1.md#argument).
