---
author: Yin
---

# The finite-rank criterion for the regular closure of a group algebra

## Group-algebra criterion

At 2026-11-25T06:18 UTC the authoring agent checked the [statement](../../claims/Yin_C_A0131_v1.md#statement) and [complete argument](../../claims/Yin_C_A0131_v1.md#argument) for Yin.
This is a self-review.

Jaikin-Zapirain's Proposition 6.1 applies first inside the generated regular closure, where multiplication is injective on its tensor square over the group algebra.
The equality obtained there maps to the larger tensor square without requiring that this map be injective.
In the converse, two maps out of the affiliated ring agreeing on the regular closure give a balanced additive map into their target by multiplication in the indicated order.
Proposition 4.2 applies to the inclusion of that regular closure in the affiliated ring.
Equivalently, after passing to tensors over the regular closure \(R\), the quotient right module \(U/R\) is flat over the von Neumann regular ring \(R\).
Tensoring the injection of left modules \(R\hookrightarrow U\) with \(U/R\) detects \((u+R)\otimes1\), so the equalizer has no element outside \(R\).
The cited propositions are used at their stated hypotheses. [JZ19 source inspection](../literature/JZ19/Yin_U001.md#epic-rank-linearization)

I checked that telescoping handles words containing generator inverses, the left and right factors can be cleared simultaneously on their respective sides including \(u\), and \(T_j=-\Theta(s k_j t)\) gives the displayed order and sign.
Starting with a solution calls only for \(L^2\) factors in \(\Theta^{-1}T_j\).
Outer cancellation in the balanced tensor product uses the same two affiliated units as the given fraction.
These steps establish existence for some fraction pair, with ordinary finite-dimensional complex ranges.

For the kernel criterion, \(x^*x+p_x\) has trivial kernel with dense range and its inverse agrees on the support with the relative inverse of \(x^*x\).
Multiplication on the right by \(x^*\) yields \(x^{[-1]}\), including when \(x=0\).
The strong Atiyah input concerns complex coefficients and the regular representation.
An abstract division-ring embedding would not supply that input.

In the relator argument the switched tensor factors in a negative occurrence give the same telescoping increment as a positive occurrence.
Opposite signs for one labelled oriented edge cannot cancel on a shortest freely reduced closed path, including lengths one and two.
The identical matrix units appear when commuting the word with a putative dual on the group-algebra vectors.
For a free basis the negative terminal deletion has the required sign on the identity vector.
For \(\mathbb Z^2\), Fubini's theorem applied to a nonzero Laurent polynomial gives its Haar-null zero set, and the two commuting shifts give the stated contradiction to a dual.
For finite groups \(U=A\) and every element passes the test, consistent with the regular-closure conclusion even in the presence of zero divisors.

The argument establishes the stated equivalences, the known torsion-free cases and the marked-relator obstruction.
The equality of the two closures for arbitrary finitely generated torsion-free groups remains a separate question.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Group-algebra criterion](#group-algebra-criterion) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Group-algebra criterion](#group-algebra-criterion) | [Statement](../../claims/Yin_C_A0131_v1.md#statement) | The three equivalent conditions, kernel projection criterion, strong Atiyah special case and marked-generator obstruction. |
| [Group-algebra criterion](#group-algebra-criterion) | [Argument](../../claims/Yin_C_A0131_v1.md#argument) | The complete equalizer, denominator, finite-rank, relative inverse and relator arguments, including both cyclic and free-basis boundary cases. |
| [Group-algebra criterion](#group-algebra-criterion) | [Regular-ring source](../literature/JZ19/Yin_U001.md#epic-rank-linearization) | Propositions 4.2 and 6.1 in their respective ambient rings. |
