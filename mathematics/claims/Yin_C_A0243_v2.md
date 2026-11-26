---
author: Yin
---

# Traceless finite-rank matrices and a single coordinate rank increment in the original group

## Statement

Let \(G\) be a finitely generated discrete group, let \(S\) be any finite generating list, and fix \(q\ge2\).
Use the [traceless system of ordinary finite-rank operators](Yin_C_A0243_v1.md#statement) on \(H=\ell^2(G)\).
Its bounded vectors \(x_i,y_i\) have the same left-translation spans \(Hp_i\) in each pair for an orthogonal partition \(\sum_i p_i=1\).
They satisfy \(\tau(y_j^*x_i)=\delta_{ij}\), and the span of the operators \(h\mapsto x_i\tau(y_j^*h)\) meets the commutator boundary on \(S\) in exactly its traceless matrices.

Such a system exists precisely when the actual \(*\)-regular closure of \(\mathbb CG\) in its affiliated algebra \(U\) contains unital algebraic \(q\)-square matrix units.
Units in the scalar inverse layer \(D_l(G)\) give bounded vectors and finite-rank witness factors in \(D_{l+2}(G)\).
In the reverse direction \(x_i\in D_k(G)\) suffices to recover the matrix units in \(D_{k+1}(G)\).
The [orthogonalization](Yin_C_A0243_v1.md#making-the-diagonal-projections-orthogonal), [bounded finite balances](Yin_C_A0243_v1.md#simultaneous-bounded-witnesses-on-one-marking) and [original-group reconstruction](Yin_C_A0243_v1.md#recovering-the-matrix-units-from-the-witnesses) prove these statements.
They also give the [finite-depth application to rational ranks in the free cyclic extension](Yin_C_A0243_v1.md#statement).

In the same group as any such system, there exist a finite matrix \(L\) over \(\mathbb CG\) and a single constant coordinate row \(w\) of its input width such that
\[
       \mathrm{rk}_Z\binom{L}{w}-\mathrm{rk}_Z L=\frac1q\,1 .
\]
Here \(\mathrm{rk}_Z\) is the center-valued trace of the image projection with the unnormalized coordinate trace.
Consequently a finite matrix over this original group ring has either irrational regular rank or regular rank \(a+1/q\) for a nonnegative integer \(a\).
The rank alternative needs only bounded vectors in \(\mathcal N(G)\).

There is also an adjoint-preserving form.
The system can be chosen with \(y_i=x_i\) for every \(i\) precisely when the regular closure contains unital matrix units satisfying \(g_{ij}^*=g_{ji}\).
From such adjoint-preserving units in \(D_l\) the bounded vectors and all witness factors can be taken in \(D_{l+1}\).
In this form the ordinary operators on the orthonormal vectors act as the usual matrices on their span and vanish on its orthogonal complement.

## A rank increment on every central summand

The [recovery argument](Yin_C_A0243_v1.md#recovering-the-matrix-units-from-the-witnesses) gives algebraic matrix units with diagonal \(p_i\) in the regular closure.
For each central projection \(z\in\mathcal N(G)\), their cuts by \(z\) identify the affiliated modules of the \(zp_i\).
The scalar trace of each is therefore \(\tau(z)/q\), since their sum is \(z\).
Equivalently each \(p_i\) has center-valued trace \(1/q\).

Apply the [group-ring equations for a regular-closure matrix](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix) to the one-coordinate input \(1-p_1\).
They provide a group-ring matrix \(L\) and a coordinate projection \(w\) onto the original unknown such that \(w(\ker_U L)=p_1U\).
The kernel of this coordinate map restricted to \(\ker L\) is exactly \(\ker\binom{L}{w}\).
Rank-nullity on the common input space and additivity of dimension give
\[
          \operatorname{rk}_G\binom{L}{w}-\operatorname{rk}_G L=\tau(p_1).
\]
The same kernel and image sequence restricts to each central summand \(zU\), since \(z\) commutes with all coefficients and the coordinate projection.
Its scalar rank increment is \(\tau(zp_1)=\tau(z)/q\), which gives the asserted center-valued identity.

Let \(\alpha=\operatorname{rk}_G L\).
An irrational \(\alpha\) already gives the first outcome.
If \(\alpha=c/d\) in lowest terms with \(d\ge1\), the block direct sum of \(\binom{L}{w}\) and \(d-1\) copies of \(L\) has regular rank \(d\alpha+1/q=c+1/q\).
This is one group-ring matrix over \(G\) with the exact indicated fractional part.

## Equal vectors and adjoint-preserving units

Given adjoint-preserving units \(g_{ij}\), their diagonal entries are already orthogonal projections.
Apply the [one-corner simultaneous clearing](Yin_C_A0243_v1.md#simultaneous-bounded-witnesses-on-one-marking) directly to them.
Its positive denominator \(c\) yields \(x_i=cg_{1i}\) and \(y_i^*=g_{i1}c=x_i^*\).
The scalar inverse for this clearing is the only additional inverse layer when starting in \(D_l\).
Biorthogonality is now ordinary orthonormality.

Conversely, for \(y_i=x_i\) the common product \(b=x_i x_i^*\) in the [reconstruction](Yin_C_A0243_v1.md#recovering-the-matrix-units-from-the-witnesses) is positive.
Write \(x_i=b^{1/2}u_i\) in the left polar decomposition, with \(u_i^*u_i=p_i\) and \(u_i u_i^*=s(b)\).
Then the recovered \(v_{ij}=x_i^\dagger x_j\) equals \(u_i^*u_j\), so \(v_{ij}^*=v_{ji}\).
Membership of \(v_{ij}\) in the regular closure, or in \(D_{k+1}\) when the \(x_i\) belong to \(D_k\), follows from the same reconstruction.
The polar decomposition identifies the adjoints of the recovered elements.

## Assessment history

### Decision traceless-boundaries-and-constant-coordinate-increments

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:32 |
| status | proved |
| reason | Whole-proof reviewers verified the original construction, its reverse direction, the finite-depth estimates and the center-valued rank increment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Biorthogonal vectors, the full traceless subspace, finite depth and both converses. |
| argument | [A rank increment on every central summand](#a-rank-increment-on-every-central-summand) | One constant coordinate row, center-valued equivalence and the rank alternatives. |
| argument | [Equal vectors and adjoint-preserving units](#equal-vectors-and-adjoint-preserving-units) | Single-corner clearing and identification of the inverse maps by polar factors. |
| argument | [Earlier fixed argument](Yin_C_A0243_v1.md#making-the-diagonal-projections-orthogonal) | Algebraic flag and one-layer orthogonalization. |
| argument | [Earlier fixed argument](Yin_C_A0243_v1.md#simultaneous-bounded-witnesses-on-one-marking) | Simultaneous clearing of the finite balanced tensors. |
| argument | [Earlier fixed argument](Yin_C_A0243_v1.md#recovering-the-matrix-units-from-the-witnesses) | Trace identities, equalizer and finite-layer converse. |
| argument | [Earlier fixed argument](Yin_C_A0243_v1.md#off-diagonal-rank-one-boundaries-alone) | The cyclic-group test separating off-diagonal units and diagonal differences. |
| review | [Traceless boundaries and constant coordinate increments](../audits/reviews/Yin_R_A0201_v1.md#traceless-boundaries-and-constant-coordinate-increments) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-traceless-boundaries-and-constant-coordinate-increments)
