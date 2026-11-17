---
author: Yin
---

# A coefficient test for finite support of the kernel projection

At 2026-11-17T03:27 UTC an agent outside the development of Yin_C_A0069_v1 independently reviewed its fixed statement and both proof sections for Sheng Yin.
The reviewer received no development dialogue, author explanations or prior findings on the argument.
The reviewer had previously checked the trace-sublevel comparison and the corrected endpoint series in C62.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0069_v1.md#statement) | Finite test for a fixed matrix, unitary and power, finite-support determination, trace and endpoint bounds and sharpness of the sufficient geometric schedule. |
| [Whole-argument finding](#whole-argument-finding) | [Lifted components](../../claims/Yin_C_A0069_v1.md#finite-and-infinite-components-of-the-lifted-graph) | Coefficient domination and Perron bound, tree displacements, finite projection computation, both spectral edges on infinite components and interpolation between multiples of the power. |
| [Whole-argument finding](#whole-argument-finding) | [Cancellation example](../../claims/Yin_C_A0069_v1.md#cancellation-after-two-steps-on-the-original-group) | Positive contraction with signed coefficients, positivity after squaring, actual constant unitary, true group support and lower return bound in the original group. |
| [Whole-argument finding](#whole-argument-finding) | [Trace sublevels](../../claims/Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group) | Direction of the sublevel trace inequality for ordered positive operators. |
| [Whole-argument finding](#whole-argument-finding) | [Corrected series](../../claims/Yin_C_A0062_v1.md#statement) | Unnormalized trace, endpoint term, squared increments and the strict convergence threshold for the exhibited matrix. |

## Whole-argument finding

Absolute values of the collected coefficients of \(T\) give a selfadjoint matrix \(P\) with nonnegative coefficients.
The triangle inequality applied to each subsequent product gives \(|\widehat{T^n}_{ij}(g)|\le\widehat{P^n}_{ij}(g)\), including the diagonal coefficient at the identity.
The positive Perron vector for an irreducible block of \(S\) bounds both operator norms by the radius of that block through the weighted row-sum inequality.
Blocks of radius less than one therefore contribute only an exponentially decaying remainder.

For a radius-one block, following the tree path to \(j\), an edge labelled \(g\) to \(i\), and the reverse tree path gives displacement \(w_i^{-1}gw_j\).
These finitely many words generate all closed displacements by insertion of tree paths.
If all are trivial, every component has exactly one point in each state, and restriction of \(T\) gives the same positive contraction matrix in every component.
An entry of its eigenprojection at one can occur only at displacement \(w_iw_j^{-1}\).
All its other eigenvalues are strictly below one, so the finite component computation and its error bound follow.

A nontrivial displacement instead gives an infinite-order element, with a conjugate loop available at every state.
The Perron identity writes the form of \(I-P\) as a nonnegative weighted sum of squared edge differences after division by the state weights.
Telescoping along each chosen loop bounds the single-displacement difference by a constant times that form.
The finitely many path positions and uniqueness of the starting group element from any fixed translated edge give bounded multiplicity on the infinite lifted graph.
Thus \(I-P\) dominates a positive constant times the direct sum of cyclic Laplacians.
The finite-state antecedent of this form comparison is the path estimate in [Diaconis and Saloff-Coste, Theorem 2.1, p. 698](https://pi.math.cornell.edu/~lsc/papers/comp-rev.pdf).
The cyclic Laplacians have no zero atom and trace mass \(O(\sqrt t)\) at the lower edge.
The form comparison transfers this *upper* sublevel bound to \(I-P\).

Strict positivity of \(T\) gives a uniform positive diagonal identity coefficient, including after the constant change of coordinates.
Subtracting a smaller \(\epsilon I\) leaves nonnegative coefficients and weighted row sums \(1-\epsilon\), in units of the Perron vector.
This places the lower spectral edge of \(P\) at or above \(2\epsilon-1\).
Consequently the negative-spectrum return decays exponentially and the upper-edge estimate bounds the positive-spectrum return by \(O(n^{-1/2})\).
Taking traces in the coefficient inequality for the even power then gives the same upper rate for \(\|T^n\|_2^2\) on the infinite blocks and excludes any projection at one there.
Undoing the fixed unitary preserves finiteness of the union of all entry supports.
Positivity of \(Q\) gives the error bound at every intervening integer power and bounds each later increment by the current error.
For the projection, its finitely many displacements give the \(O(R^{-4})\) endpoint term, so weighting on geometric schedules gives convergence for \(\kappa>2\beta\).

In the example the nonzero coefficients of \(q\) at exponents \(\pm2\) are negative, giving absolute mass \(1+4\varepsilon\).
All exponents from \(-8\) to \(8\) already have positive mass in \(q_0^2\), so the finitely many coefficients of \(q^2\) stay positive for sufficiently small \(\varepsilon\).
The sum-of-squares identity uses \(|1-z^2|^2=4|1-z|^2-|1-z|^4\).
Its first positive square and the lower bound \(q\ge1-12a\) yield an injective nonclosed cyclic column, strictly within the norm allowed by \(M=1\).
When \(l/k\) stays in a compact subinterval of \((1,\infty)\), the quadratic vanishing of \(1-q\) gives the matching lower bound of order \(k^{-1/2}\) for the squared increment on an arc of length comparable to \(k^{-1/2}\).

In the actual coordinates the projection is \(0\oplus S_0P_fS_0^*\), whose indicated diagonal entry has positive coefficients at the identity and generators.
Its identity coefficient is strictly less than one, so the scalar complement in the input retains both the identity and all these generators as well.
Within-entry support differences consequently force the whole group even after independent translations.
Conjugation by the specified \(W=1\oplus S_0\) yields the finite block \(3I/4+P_f/4\), with row sums one and transitions \(h_i h_j^{-1}\) whose closed displacements telescope to the identity.
In these same coordinates the cyclic block passes the test at \(L=2\) and fails at \(L=1\).
Its lower increment bound forces divergence when \(\kappa\le2\beta\), establishing sharpness for this example on the original four-line group.

The review supports the test for the specified \(A,L,W\) and its constructive projection formula given the finite identity comparisons.
Existence of a passing choice for an arbitrary matrix remains open.
