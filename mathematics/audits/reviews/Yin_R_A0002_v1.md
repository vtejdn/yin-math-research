---
author: Yin
---
# Independent review of amenable kernel extraction and Schur complements

The review act occurred on 2026-11-10T14:42 (UTC), under Yin.
The reviewed object is the complete statement, argument and scope discussion of [Yin_C_A0001_v1](../../claims/Yin_C_A0001_v1.md), as directly read on that date.
The reviewer did not develop this Claim and received no proof-generation dialogue, mathematical summary of the proposed deduction, or earlier verdict before reading the fixed Claim.
The necessary Ele03 source reconstruction and the retained affiliated-operator foundations were read as mathematical inputs.
The reviewer independently reconstructed the finite-dimensional inequalities and the affiliated block calculation.
The separate source audits of Lin93, Lin06 and Bar19 supplied no development context for this Claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Exact statement](../../claims/Yin_C_A0001_v1.md#statement) | All matrix sizes, finite-set bounds, amenable kernel extraction, Schur-complement hypotheses and scalar-kernel conclusion. |
| [Whole-argument finding](#whole-argument-finding) | [Exact argument](../../claims/Yin_C_A0001_v1.md#argument) | Complete matrix boundary estimate and affiliated Schur extraction under the stated finite-tracial foundations. |

## Inputs and retained foundations

The [Ele03 finite-set proof](../literature/Ele03/Yin_U001.md#boundary-proof) and its [metric and boundary conventions](../literature/Ele03/Yin_U001.md#folner-and-propagation) give the finite-propagation setting.
The review checked the displayed argument instead of treating its inspection conclusion as proof.
The [MSY23 trace and invertibility facts](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and [rank-invariance proof](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) were checked at the polar-support, closure-of-range and kernel-inclusion steps.
The [MSY23 Schur calculation](../literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) supplies its general affiliated-algebra interface only; its strong Atiyah conclusion is not a premise.
The [Lin00 closed-product convention](../literature/Lin00/Yin_U001.md#bounded-fractions-and-common-denominators) does not import Lin00's free-group rationality theorem.

Existence and associativity of the finite-tracial affiliated algebra, polar decomposition, the tracial property, and the Følner characterization remain accepted external foundations.
Their original general existence proofs were not re-audited.
No integer-valued analytic rank, free-field realization, scalar Ore condition, or torsion-free zero-divisor conjecture is assumed.

## Whole-argument finding

The whole statement and proof are supported under their stated hypotheses.
No unresolved internal mathematical gap was found.

### Finite-set estimate

For a closed right-invariant subspace of \(\ell^2(G)^n\), each component has constant group-basis diagonal projection trace.
For a finite-dimensional subspace supported on \(F\), the sum over \(F\) is its ordinary dimension.
Projection order therefore gives exactly the local-dimension comparisons used in the Claim, with unnormalized component trace.

For \(A\in M_{p,q}(\mathbb CG)\), the metric satisfies \(d(sx,x)=|s|\), so input supported on \(F^{-w}\) has output supported on \(F\).
The restricted kernel is supported on \(F\) in \(q\) components, and its image is supported on \(F\) in \(p\) components.
Rectangular polar decomposition equates the initial and final support traces and gives \(\delta+\rho=q\).
Finite-dimensional rank-nullity gives \(u_F+t_F=q|F^{-w}|/|F|\).
The inequalities \(u_F\le\delta\), \(t_F\le\rho\) show that both deficits are nonnegative and sum to \(q|\partial_wF|/|F|\).
Consequently
\[
\delta-q|\partial_wF|/|F|
\le u_F
\le \dim_{\mathbb C}(\ker A\cap\mathbb C[F]^q)/|F|
\le\delta.
\]
The coefficient is \(q\), not the output dimension \(p\).
The estimate handles empty interior, \(A=0\), and finite \(G\) with \(F=G\) under the stated empty-complement convention.
It uses the closure of the range and needs no closed-range assumption.

A nonzero invariant kernel has \(\delta>0\) by trace faithfulness.
Amenability is used precisely to choose a finite \(F\) with boundary error smaller than \(\delta\).
This yields a nonzero finite-support kernel vector, without rank integrality or a uniform lower bound on \(\delta\).

### Affiliated Schur extraction

Multiplying the two triangular factors in the stated order transforms
\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\quad\text{into}\quad
\operatorname{diag}(a-bd^{-1}c,d).
\]
Each factor is invertible over \(U\), with inverse obtained by reversing its off-diagonal sign.
Rank invariance and diagonal additivity give
\[
\operatorname{rk}M=1+\operatorname{rk}r,\qquad
\dim_G\ker M=\dim_G\ker r.
\]
A nonzero kernel for \(r\) therefore gives a finite-support nonzero \((x,y)\) in the kernel of the bounded matrix \(M\).
If \(x=0\), its second row and invertibility of \(d\) force \(y=0\), so \(x\ne0\).
The rows imply \(rx=0\) in the affiliated algebra.
If \(\lambda(x)\) were injective, its affiliated inverse would imply \(r=0\), a contradiction.
Thus the scalar group-ring element \(x\ne0\) has nontrivial analytic kernel.

This cancellation is an identity of closed affiliated products.
It assumes neither that every finite-support vector belongs to the pointwise domain of \(d^{-1}\), nor that an affiliated inverse is bounded.
Those domain issues do not invalidate the algebraic calculation.

### Scope

If every nonzero element of \(\mathbb CG\) acts injectively, the extracted \(x\) cannot exist.
Every nonzero Schur complement in the stated family is then injective, hence invertible in \(U\).
For \(d=1-g\), infinite order of \(g\) excludes a nonzero square-summable vector constant along its infinite cyclic orbits, giving the required affiliated inverse.

The finite-support extraction still requires amenability of the group generated by all coefficients.
Torsion-freeness alone supplies neither Følner sets nor scalar injectivity.
This finding supports the conditional amenable result, not arbitrary nonamenable torsion-free groups, new group-class coverage, or completion of the whole rational-closure Task.
