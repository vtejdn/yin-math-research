---
author: Yin
---

# Positive spectral mass at the bottom of the spectrum

At 2026-11-17T02:07 UTC an agent outside the development of Yin_C_A0056_v1 independently reviewed its fixed statement and complete argument for Sheng Yin.
The reviewer read the claim and its cited mathematical inputs without receiving proof-development discussion, author explanations or another verdict on this claim.
The reviewer had previously inspected the four-line hypotheses and the projection-decay criterion used as inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0056_v1.md#statement) | Unnormalized matrix trace, positive spectral mass, bounds (1) and (2), fixed-word-matrix quantifiers and scope on good tuples. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0056_v1.md#argument) | Clopen projections, matrix ball estimate, Fejér polynomial, both conclusions about the positive spectral tail and the closed-range implication. |
| [Whole-argument finding](#whole-argument-finding) | [Common interval](../../claims/Yin_C_A0056_v1.md#a-common-spectral-interval-for-a-fixed-word-matrix) | Common normalization and one transported free moment, exact nullity from a missing point, and the sufficient finite norm test. |
| [Whole-argument finding](#whole-argument-finding) | [Examples and spatial decay](../../claims/Yin_C_A0056_v1.md#the-exponent-for-positive-matrices-and-the-spatial-condition) | Free-tree edge density and its positive-operator scope, cyclic Gram matrices, and the two-dimensional abelian example. |
| [Whole-argument finding](#whole-argument-finding) | [Trace input](../../ledger/Yin_L_A0054_v1.md#from-hyperbolicity-to-integral-traces) | Integrality of traces of reduced matrix-algebra projections. |
| [Whole-argument finding](#whole-argument-finding) | [Free rank and moments](../../ledger/Yin_L_A0054_v1.md#the-rank-seen-by-a-fixed-matrix) | Quotient nullity bounded below by integral free nullity and eventual exactness of each fixed word moment. |
| [Whole-argument finding](#whole-argument-finding) | [Ball and spatial estimates](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Scalar ball inequality for the realized marked group and consequences of the two spatial summability conditions. |
| [Whole-argument finding](#whole-argument-finding) | [Equality of finite words](../../claims/Yin_C_A0052_v1.md#bounded-certificates-in-the-cone-presentation) | Finite moment computations with a supplied tuple, word-problem data and exact coefficients. |

## Whole-argument finding

Each nonempty part of a finite clopen spectral partition gives a projection of positive integer trace, and their traces add to the number \(m\) of columns.
Gaps between distinct components of a compact subset of the line furnish just such partitions, so the spectrum has at most \(m\) closed interval components.
Accumulation of positive spectrum at zero therefore supplies an entire interval at zero.

The Fejér polynomial runs from one to zero before or at the right endpoint of this interval once \(n\) is sufficiently large, independently of \(k\).
Its \(k\)-th power consequently takes the value \(1/2\), giving norm \(1/4\) for the defect polynomial.
The matrix ball estimate follows from Cauchy–Schwarz on the input column of vectors and the scalar operator bounds on the entries.
Summing the squared coefficient norms gives exactly the unnormalized matrix trace of \(X^*X\), so the scalar ball constant suffices at radius \(2k(n-1)w\).
Squaring yields (2), and the omitted zero atom contributes nothing. [Nica, inequality for balls](../../literature/pdf/Nic17--arxiv.pdf#page=1)

At \(n=\lceil2/\sqrt t\rceil\), the squared defect above \(t\) is at most \(16^{-k}\).
Choosing \(k=\lceil2\log(1/t)\rceil\) makes this error negligible against the radius bound of order \(t^{3/2}(1+\log(1/t))^{-3}\).
For the critical limsup the decreasing majorant at \(k=1\) is constant up to \(n^{-2}\), then has derivative \(-2n^{-4}t^{-3}\).
The Stieltjes integral of this majorant would be \(o(n^{-3})\) if the positive mass were \(o(t^{3/2})\), contradicting (2).
The argument gives the stated positive limsup and the separate pointwise logarithmic estimate.
A gap places the Gram kernel projection in the reduced matrix algebra, giving closed range and integral nullity.

For a fixed word matrix the free nullity \(d\) is an integer and quotient nullity is at least \(d\) by the free-ring factorization.
The free trace of \((1-B_F)^N\) decreases to \(d\).
Fixing \(N\) before choosing \(s\) and then applying marked systole transports one strict moment bound to all sufficiently large good tuples.
The quotient trace of \([0,s]\) is consequently below \(d+1\).
A missing point in \((0,s]\) makes the lower spectral cut clopen, hence of integer trace exactly \(d\).
Faithfulness gives equality with the kernel projection and excludes all positive spectrum below the missing point.
This proves the common-interval assertion and the strict-norm certificate, without requiring uniformity of the rapid-decay constant over tuples.

For the degree-four tree, solving the branch resolvent and taking its imaginary part gives the claimed density.
At the upper edge its denominator stays positive and the numerator vanishes as a square root.
Equivalently this is Kesten's simple random-walk spectral law for two free generators after multiplying the walk operator by four. [Kesten, proof of Theorem 3, p. 349, following (4.9)](https://sites.math.northwestern.edu/~auffing/papers/KRW.pdf#page=14)
The resulting \(t^{3/2}\) mass calibrates the positive-contraction estimate.
Negative augmentation precludes using this very operator as a one-column group-ring Gram example.
For the cyclic rows the positive eigenvalue vanishes to order \(2d\) at one angle and the kernel projection is analytic on an annulus, yielding the stated slow spectral power and all polynomial spatial moments on the ambient group.
For the torus row the positive eigenvalue vanishes quadratically in two variables, while the kernel projection has incompatible continuous limits on the coordinate axes.
The shell count on \(\mathbb Z^2\) would force absolute Fourier convergence from either spatial condition, contradicting those limits.

The argument supports the full claim at its stated hypotheses.
The estimates control the positive part of the spectral measure and do not determine a general kernel trace or establish spatial decay for nonclosed-range matrices on the four-line groups.
