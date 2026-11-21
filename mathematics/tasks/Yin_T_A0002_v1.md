---
author: Yin
---
# Kaplansky's zero-divisor conjecture over the complex numbers

## Contract

### Original question

Let \(G\) be any torsion-free discrete group, and let \(\mathbb C[G]\) be its group algebra of finitely supported complex functions, with multiplication induced by the group law.
Determine whether
\[
 \forall \alpha,\beta\in\mathbb C[G],\qquad
 \alpha\beta=0\ \Longrightarrow\ \alpha=0\ \text{or}\ \beta=0
\]
holds for every such \(G\).
Equivalently, determine whether \(\mathbb C[G]\) is a domain for every torsion-free discrete group.

### Reduction to finitely generated groups

The union of the supports of a proposed pair \(\alpha,\beta\) generates a finitely generated torsion-free subgroup \(H\le G\).
The inclusion \(\mathbb C[H]\subseteq\mathbb C[G]\) preserves the pair, its product and nonvanishing.
It therefore suffices to resolve the assertion for finitely generated torsion-free groups.

### Completion criteria

Either prove the assertion for every group in the stated scope, or rigorously specify a torsion-free group \(G\) and two nonzero finite sums \(\alpha,\beta\in\mathbb C[G]\) with \(\alpha\beta=0\).
A counterexample must include verification of torsion-freeness, nonvanishing of both factors and the exact zero product.
Completion requires a review covering this exact contract and the full proof or counterexample, with independent review of the complete logical chain under the applicable review rules.

## Relation to the Atiyah task

The [complex-coefficient strong Atiyah assertion in A0001](Yin_T_A0001_v1.md#contract) implies this scalar zero-divisor assertion.
A counterexample here also refutes A0001, since a nonzero scalar convolution operator with a nonzero finitely supported null vector has von Neumann kernel dimension strictly between zero and one.
The [known-results synthesis](../ledger/Yin_L_A0001_v1.md#formulation-and-algebraic-interface) retains the division-closure interface and its source.

## Starting evidence

The [known positive cases](../ledger/Yin_L_A0001_v1.md#known-positive-results) supply established complex-coefficient group classes through strong Atiyah results.
The [shared bibliography](../literature/references.bib) also contains the direct algebraic results and the recent positive-characteristic constructions under KLM88, FSP26, Ope26f, Iva26 and MD26.

[Mghirbi–Douglas Proposition 8.3](../audits/literature/MD26/Yin_U001.md#proposition-83-and-its-quantifiers) supplies a sufficient route to a complex counterexample from counterexamples in infinitely many distinct prime characteristics with uniform bounds on both actual support sizes.
The same reading retains the [type-incidence rank obstruction](../audits/literature/MD26/Yin_U001.md#the-rank-obstruction-in-theorem-81) and the [unresolved support bound for the present constructions](../audits/literature/MD26/Yin_U001.md#what-the-existing-constructions-supply).
The latter distinguishes graph and alphabet size from support after collecting equal group elements.

## Current decision

[Selected decision](#decision-initial)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-11-21T02:15 |
| status | active |
| authority | Yin explicitly requested Task A0002 with the complex-coefficient Kaplansky conjecture as its objective, following the discussion of zero divisors. |
| reason | The scalar finite-support assertion has its own resolution criterion and starting evidence in the retained literature on characteristic transfer. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Absence of nonzero zero divisors in the complex group algebra of every torsion-free discrete group, resolved by a complete proof or rigorous counterexample with the stated review. |
