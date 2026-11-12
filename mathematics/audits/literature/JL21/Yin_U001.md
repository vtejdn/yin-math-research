---
author: Yin
---

# JL21: amenable rank comparison and its arithmetic limit

<a id="jl21-u001"></a>
## Source and inspection

The inspected source is [arXiv v2](readme.md#arxiv-v2).
On 2026-11-12 Theorems 1.1–1.3 on pp. 3–4, the group-ring specialization in Examples 3.2 and 5.2 on pp. 11–12 and 15–16, and the surrounding normal-extension hypotheses were checked.
This is statement and applicability reading; the full proofs of the linear infimum rule, continuity and trace comparison were not audited.

<a id="amenable-rank-comparison"></a>
## The applicable interface

Theorem 1.1 concerns a unital ring \(R\) with a Sylvester matrix rank function and a right amenable normal extension \(S\), equipped with the specified finite approximation system preserving that rank.
It identifies the limit of the normalized finite-module ranks with their infimum.
Theorem 1.2 proves affine continuous dependence on the original rank under its additional weak-quasitiling hypothesis.
These conclusions give a canonical extension and a limit formula, not an integer-range theorem.

For a discrete amenable group \(G\), Examples 3.2 and 5.2 apply with \(R=\mathbb C\), \(S=\mathbb CG\), and finite-support subspaces \(\mathbb CF\), where \(F\subset G\) is finite.
The normalizing elements in Example 5.2 are group elements, hence units; this group-ring application does not assume that all nonzero elements of \(\mathbb CG\) are regular.
In particular, it does not require the zero-divisor conjecture as a hypothesis.
For a row-convention matrix \(A\in M_{n,m}(\mathbb CG)\), the finite ranks in this specialization are

\[
r_F(A)=\dim_{\mathbb C}\bigl((\mathbb CF)^nA\bigr).
\]

Theorem 1.1 gives the canonical extended rank as the limit of \(r_F(A)/|F|\) along increasingly right-invariant finite sets, equal to the infimum over nonempty finite \(F\).
Theorem 1.3 on p. 4 applies to an amenable discrete group acting by a trace-preserving twisted action on a unital tracial \(C^*\)-algebra.
It identifies the rank induced by the extended trace on the maximal crossed product with the rank obtained by the finite approximation system on its algebraic crossed product.
Taking the coefficient algebra to be \(\mathbb C\) and the action and cocycle trivial identifies the preceding group-ring rank with the canonical analytic von Neumann rank.

<a id="no-integer-range-conclusion"></a>
## Why this does not settle the domain step

The uniqueness of the rank on the coefficient field does not assert uniqueness of all Sylvester matrix rank functions on \(\mathbb CG\).
The extension and trace-comparison statements determine a real-valued rank, but do not prove that a nonzero scalar group-ring element has rank one.
Normalized finite ranks have denominators \(|F|\); convergence or an infimum formula does not make their limit integral.
The source therefore supplies a precise algebraic–analytic comparison, while leaving the scalar full-rank issue unresolved.
