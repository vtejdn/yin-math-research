---
author: Yin
---
# Three fixed diagonal perturbations: whole-argument review

On 2026-11-16T15:10 UTC a separate reviewing agent checked the full [statement](../../claims/Yin_C_A0018_v1.md#statement) and [argument](../../claims/Yin_C_A0018_v1.md#argument) for Yin.
The reviewer did not develop the proof or receive its exploration notes, development conversation, author explanations or an earlier verdict on it.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0018_v1.md#statement) | Fixed-group equivalence, size and excesses of the witness, mass bound, and positive restriction. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0018_v1.md#argument) | Affiliated kernel and image calculations, parameter fibers, explicit witness, and both directions of the positive test. |
| [Whole-argument finding](#whole-argument-finding) | [Amenable scalar descent](../../claims/Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) | Applicability of finite scalar descent to a matrix of nonintegral rank, including descent to finitely generated subgroups. |

## Whole-argument finding

The three-point condition is equivalent to integrality of all matrix ranks over the specified group ring.
Projection of the pencil kernel onto the first coordinate has image the spectral module of the compressed selfadjoint operator in the corner with unit \(e\).
Indeed, solving its lower equation restricts the first coordinate to \(eU\); the remaining freedom in the upper equation fills exactly \((1-e)U\), by the polar projection of the adjoint column restricted to \(\ker D\).
The fiber at zero is the fixed common kernel of the lower block and the adjoint column.
The image is a projection module and hence projective, so taking dimensions of the kernel and image gives the stated sum without assuming a closed Hilbert range for the lower block.
The spectral projections at distinct parameters are orthogonal in the corner; under integrality each excess is an integer because the fixed fiber is itself the kernel of a rectangular group-ring matrix.

In the converse construction the projection \(Q\) modulo the old column range gives an increment of \(1-\tau(p)\), even if the original Hilbert range was not closed.
The last row of the witness imposes \(y\in pU\), and the two rows involving the last variable impose \(x-y\in(1-p)U\), with independent choices of the two lifts.
Thus \(y=px=\lambda x\); for \(x=0\) the free variables lie in the kernels of \(B\) and \([v\ B]^*\), respectively.
This verifies the three excesses \(1-\tau(p),\tau(p),0\), also when \(B\) has no columns.
If all successive column increments had been zero or one, their sum could not have been a noninteger.

For the positive restriction the lower kernel is killed by the adjoint column, by positivity of the whole block matrix.
An invertible triangular change of variables in the affiliated algebra then makes the Schur complement positive; it is at most \(u\le1\), so it is bounded.
The eigenspace at one is killed by \(1-u\) and by \(w\) because the two terms of \(1-S\) are positive and \(D^\dagger\) is injective on its support.
A nonzero such eigenspace forces \(1-u\) and each entry of \(w\) to vanish under scalar injectivity, excluding an atom at zero.
In the reverse direction the Gram matrix has fixed fiber of dimension \(\nu(a)\); its Schur complement is the kernel projection of \(a^*\), with trace \(\nu(a)\) by polar equivalence.
Both endpoint excesses are positive for a nonzero scalar with nonzero kernel.
The amenable specialization uses the linked Claim only for its established implication from fractional matrix rank to nonzero group-ring zero divisors; the opposite obstruction is already supplied by a scalar of noninteger rank.

This inspection uses the ordinary spectral and polar calculus of a finite von Neumann algebra with its unnormalized matrix trace, as laid out in the [affiliated-operator unit](../literature/MSY23/Yin_U004.md#msy23-u004).
It does not re-audit those foundations or the earlier amenable kernel-localization theorem.
The proof gives neither an unconditional three-point inequality for all torsion-free groups nor a torsion-free counterexample.
