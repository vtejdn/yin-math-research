---
author: Yin
---

# Spatial decay and the trace of the kernel projection

An agent outside the development of Yin_L_A0055_v1 independently reviewed its full argument for Sheng Yin at 2026-11-17T01:36 UTC.
The reviewer read the fixed ledger, the relevant four-line and assembly results and the cited source statements without receiving development dialogue, author explanations or a prior verdict on this argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Decay assumptions](../../ledger/Yin_L_A0055_v1.md#spatial-decay-of-a-kernel-projection-would-give-integrality-on-the-four-line-groups) | Matrix trace normalization, the dyadic shell condition and the weighted moment condition for a single realized group. |
| [Whole-argument finding](#whole-argument-finding) | [Proof and obstruction](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Operator norm and trace \(L^2\) convergence, exact distance for fractional trace, nonclosed-range example and the obstruction to virtual compact specialness. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line groups](../../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws) | Torsion-free hyperbolicity on the specified event. |
| [Whole-argument finding](#whole-argument-finding) | [Assembly trace](../../ledger/Yin_L_A0054_v1.md#from-hyperbolicity-to-integral-traces) | Integer values on projections in matrix algebras over the reduced group algebra. |

## Whole-argument finding

The chosen finite marking is admissible in the ball form of the Haagerup inequality.
A torsion-free virtually cyclic group is trivial or infinite cyclic, and in either case its group algebra over \(\mathbb F_2\) is a domain.
The two nonzero binary factors with zero product therefore ensure non-elementarity.
In a single dyadic shell of outer radius \(2^{j+1}\), applying the ball estimate entry by entry gives a bound \(C_{G,m}2^{3j/2}b_j\) in operator norm, allowing dependence on the group, the marking and the matrix size.
This application allows arbitrary complex coefficients. [Nica, ball inequality in §1](https://arxiv.org/pdf/1509.08317#page=1)

The identity coefficient is a finite matrix term outside the shells.
After including it, absolute summability gives norm convergence in the reduced algebra and Fourier orthogonality identifies the limit with \(p\) in trace \(L^2\).
For the unnormalized trace, \(\|x\|_2\le\sqrt m\,\|x\|\), which suffices for the identification.
The moment bound controls \(\sum_j2^{(3+\delta)j}b_j^2\), and Cauchy–Schwarz against \(2^{-\delta j/2}\) gives the required summability.
The matrix projection now has integer trace by surjectivity of assembly for a hyperbolic group and the assembly trace theorem for a countable torsion-free group. [Lafforgue](https://ems.press/journals/jncg/articles/3925) · [BCM04, Theorem 6.3](../literature/BCM04/Yin_U001.md#assembly-trace)

If \(\|p-a\|=r<1/2\), the straight path from \(p\) to the selfadjoint part of \(a\) has spectrum in \([-r,r]\cup[1-r,1+r]\).
Its upper spectral projection varies norm continuously and ends in the reduced algebra, so equivalence of sufficiently close projections preserves the initial trace along the whole path.
Fractional trace would therefore force a distance of at least \(1/2\), attained by half the identity.
For the row \((1-g,0)\) the infinite-order shift has no \(\ell^2\) fixed vectors, while normalized indicators of successively longer orbit intervals show that \(1-g\) is not bounded below.
This verifies the nonclosed range and the constant diagonal kernel projection.
For a nonzero scalar the faithful trace excludes a kernel projection of trace one.
Finally the four-line binary zero product contradicts the division-ring embedding available over \(\mathbb F_2\) for every torsion-free virtually compact special group. [Fisher and Sánchez-Peralta, Theorem 1.3(1)](../../literature/pdf/FSP26.pdf#page=3)

The two decay tests, the distance obstruction and the stated examples are supported.
Whether the projections of arbitrary matrices over the four-line groups satisfy either decay test remains open.
The review checks the quoted analytic and embedding theorems at their interfaces.
