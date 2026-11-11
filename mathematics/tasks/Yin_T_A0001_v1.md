---
author: Yin
---
# The complex-coefficient Atiyah conjecture for torsion-free groups

## Contract

### Original question

Let \(G\) be any torsion-free discrete group, let \(\lambda_G\) be its left regular representation on \(\ell^2(G)\), and let \(\mathcal N(G)=\lambda_G(G)''\) have canonical trace \(\tau_G(T)=\langle T\delta_e,\delta_e\rangle\).
For \(m,n\geq 1\) and \(A\in M_{m,n}(\mathbb C G)\), let \(\lambda_G(A)\colon\ell^2(G)^n\to\ell^2(G)^m\) act by entrywise left convolution.
Let \(p_A\in M_n(\mathcal N(G))\) be the orthogonal projection onto its kernel.
The question is whether every such \(G\) and \(A\) satisfy
\[
\dim_{\mathcal N(G)}\ker\lambda_G(A)
  =(\operatorname{Tr}_n\otimes\tau_G)(p_A)\in\mathbb Z_{\geq 0}.
\]
Here \(\operatorname{Tr}_n(I_n)=n\).

### Reduction to finitely generated groups

The union of the supports of the entries of \(A\) generates a finitely generated torsion-free subgroup \(H\leq G\).
Left convolution by \(A\) on each right coset \(Ht\) is a copy of the operator over \(H\).
The trace is evaluated at the identity in the coset \(H\), so the kernel dimensions over \(H\) and \(G\) agree.

### Completion criteria

Resolve the question by a proof for all the stated groups and matrices, or exhibit a torsion-free group and a finite matrix over its complex group ring whose kernel has provably nonintegral von Neumann dimension.
Completion requires a review covering the exact contract and the full proof or counterexample.

## Starting references

For torsion-free \(G\), the integrality statement is equivalent to the division closure of \(\mathbb C G\) in the algebra of operators affiliated to \(\mathcal N(G)\) being a skew field. [Lück and Linnell, Theorem 2.3(3)](https://arxiv.org/pdf/1602.06906v3#page=10)
Free groups give a known case over \(\mathbb C\). [Linnell's free-group case](../audits/literature/Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate)

## Research preparation

The [known-results synthesis](../ledger/Yin_L_A0001_v1.md) distinguishes published cases, the inspected 2026 preprint, source-reading limits and the remaining bridges.
The [research strategies](../strategies/index.md#task-yin_t_a0001) give the current mechanisms and their discriminating steps.
The [first investigation of route four](../ledger/Yin_L_A0002_v1.md) records direct torsion-free invertibility tests and the remaining rational-kernel obstruction.

## Current decision

[Selected decision](#decision-initial)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-11-10T12:19 |
| status | active |
| authority | Yin assigned the complex-coefficient Atiyah conjecture for torsion-free groups as an A-series Task. |
| reason | The group-ring integrality question has its own hypotheses and criterion for resolution. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Integer von Neumann kernel dimension for all finite complex group-ring matrices over torsion-free discrete groups, with the stated trace convention and completion criteria. |
