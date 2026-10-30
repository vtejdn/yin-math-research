---
author: Yin
---

# Yin_C_F0027: Complete Review of Bounded Inversion and the Core-Estimate Extension

<a id="bounded-inversion-core-estimates-finding"></a>

## Actual review relationship

The reviewer supplied the preliminary bounded-regularization argument reused in the audited ACSY24/target interface and then reviewed the assembled proof. This disclosed mathematical contribution makes the full finding self-reviewed.
The original independent descriptions, dates and full checked scope are preserved as historical facts; no isolated arrangement or new review is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Retained complete finding](#bounded-inversion-core-estimates-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Retained complete finding](#bounded-inversion-core-estimates-finding) | [Exact statement](../../claims/Yin_C_F0027_v1.md#statement) | Complete bounded matrix-inverse domain calculus without normality, and separately the two-core-estimate bridge for normal tuples to the same actual all-M closures and complete affiliated criterion; no automatic bare-core estimates. |
| [Retained complete finding](#bounded-inversion-core-estimates-finding) | [Exact argument](../../claims/Yin_C_F0027_v1.md#2-closed-domain-commutators-and-selfadjoint-doubling) | Complete bounded matrix-inverse domain calculus without normality, and separately the two-core-estimate bridge for normal tuples to the same actual all-M closures and complete affiliated criterion; no automatic bare-core estimates. |

- Date and reviewer: 2026-09-10; the reviewing agent.
- Target: [Yin_C_F0027](../../claims/Yin_C_F0027_v1.md#yin_c_f0027), complete Sections 1--6.
- Author: another AI agent, with the final identifier and scope clarifications by the coordinating agent.
- Disclosure: the reviewer supplied the preliminary bounded-regularization argument used in the separately audited ACSY24 interface, but did not author the target module.
  This is a separate full-artifact review with that contribution disclosed, not independent rediscovery of every ingredient.
- Outcome: accepted in the exact two scopes stated below; no mathematical or operator-domain correction was required.
  The responsible Claim materials and their selected decisions own the current mathematical and review assessments.

## Exact Conclusions Reviewed

The first conclusion assumes closable duals on the dense starred polynomial algebra, the prescribed rank-one commutators with the listed generators, and bounded commutators with their adjoints.
It proves that the bounded rational closure $\operatorname{Rat}_M\mathbb C\langle X\rangle$ preserves the actual closed dual domains and has bounded finite-rank commutators.
Hilbert--Schmidt adjoint commutators are sufficient, but their Hilbert--Schmidt norm is not needed in this part.
Normality is also unnecessary for this bounded-inversion argument.

The second conclusion assumes a normal generating tuple, the core generator identities, inclusion of the starred core in the adjoint domains, and the two separate bounds
\[
\|D_{i,0}p\|_2\le c_i\|p\|,
\qquad
\|D_{i,0}^*p\|_2\le c_i'\|p\|.
\]
It proves that both actual closed domains contain all bounded vectors and transfers the entire affiliated criterion of Yin_C_F0024.
This part does not require bounded commutators with the adjoint generators.
The final revision makes that weaker scope explicit, and Section 5's proof was checked against it.

Neither part asserts the full affiliated forward implication from the bare ACSY24 small-core hypotheses alone.
The two analytic estimates are not claimed to follow automatically in the general normal setting.

## Closed Domains and the Inverse Argument

The product rule supplies bounded commutators with all starred polynomials on the common core.
For a graph-convergent sequence $z_n$ in that core, the identity
\[
D_0(az_n)=aD_0z_n+T_az_n
\]
has a convergent right side.
Closedness therefore proves both invariance of the full domain of $D$ and the extended commutator identity there.
Applying the result to $a^*$ and pairing against the entire adjoint domain gives
\[
[D^*,a]=-T_{a^*}^*.
\]
The proof does not presume that the polynomial algebra is a core for $D^*$.

The selfadjoint doubling
\[
S=\begin{pmatrix}0&D^*\\D&0\end{pmatrix}
\]
has the stated domain $\operatorname{Dom}D\oplus\operatorname{Dom}D^*$.
For a bounded diagonal multiplier preserving that domain, the block commutator has the advertised lower-left and upper-right entries.
Adjoint pairing for selfadjoint $S$ correctly makes its bounded-commutator algebra closed under adjoints.

The regularization formula
\[
[S(1+tS^2)^{-1},\widetilde a]
=R_tC_aR_t-B_tC_aB_t
\]
was recomputed from the two resolvents at $\pm i/\sqrt t$.
The factors and sign are correct.
This derivation only uses invariance of $\operatorname{Dom}S$, and avoids an unsupported invariance assertion for $\operatorname{Dom}S^2$.
Spectral calculus gives the strong limits of $R_t$ and $B_t$, and the norms $\|R_t\|\le1$ and $\|B_t\|\le1/2$ give the stated $5/4$ bound.

For a bounded inverse $a^{-1}$, the inverse formula is first applied to the everywhere bounded regularizations.
The proof then uses
\[
R_t\widetilde a^{-1}\zeta\longrightarrow\widetilde a^{-1}\zeta,
\qquad
S(R_t\widetilde a^{-1}\zeta)
\longrightarrow\widetilde a^{-1}S\zeta
-\widetilde a^{-1}C_a\widetilde a^{-1}\zeta.
\]
Both limits are valid for $\zeta\in\operatorname{Dom}S$.
Closedness supplies actual inverse-domain invariance and the inverse commutator formula.
No formal multiplication by an inverse is used before its domain has been established.

## Matrix Inverses and Finite Rank

The direct-sum amplification has precisely the coordinatewise domains needed by the matrix argument.
A finite matrix whose entries preserve both scalar domains preserves those direct-sum domains, and its commutator matrix is bounded.
The preceding inverse proof therefore applies to any inverse that is bounded in $M_n(M)$.
Testing a vector with only one nonzero coordinate confirms that each inverse entry preserves both scalar domains.

Finite rank of the lower-left commutator is preserved by sums, products and the bounded inverse formula.
A finite matrix of finite-rank operators is itself finite rank on $H^n$.
Thus the inverse commutator
\[
-L^{-1}[D_i^{(n)},L]L^{-1}
\]
is finite rank, and so are all its entries.
This proves the claimed rational-closure inclusion at exactly the bounded matrix-inverse scope.

The weak test formula follows from the actual domain invariance already proved.
The artifact explicitly refrains from inferring that invariance in the opposite direction merely from polynomial weak tests.
This correctly retains the possible difference between a core for $D_i$ and a core for $D_i^*$.

## The Two-Estimate Analytic Extension

Kaplansky density followed by norm approximation gives uniformly bounded starred-polynomial approximants converging to every $x\in M$ in $L^2$.
The first core estimate gives weakly compact sets of dual images.
Weak closedness of the graph of the actual closure places $x$ in $\operatorname{Dom}D_i$.
The independent adjoint estimate applies to the already closed operator $D_{i,0}^*=D_i^*$ and places $x$ in its domain.
Weak lower semicontinuity gives both asserted bounds after the approximation tolerance tends to zero.

Pairing against a dense adjoint domain and using those bounds proves bounded-set weak continuity on all of $M$.
The same argument for the adjoint uses the dense domain of the closed dual.
This extends each generator identity from the core to all bounded vectors.
The proof requires no adjoint-generator commutator bound in this section.

The inclusions
\[
\mathcal A\subseteq M\subseteq\operatorname{Dom}D_i
\]
and the defining graph-core property of $\mathcal A$ make the closure of $D_i|_M$ equal to the original $D_i$.
Consequently Yin_C_F0024 applies to exactly the same closed duals, rather than to an unspecified extension.
The transfer includes all bounded fraction choices, bounded finite-rank extensions of their defects, and the bounded-element full-domain formulation.

## Source and Scope Checks

The selfadjoint finite-Fisher application retains the separate Dab10-U002 analytic input and its explicit one-variable reduction.
The general normal ACSY24 derivations are not assigned the reality, coassociativity, or contraction estimates of that special case without proof.
The source adjoint formula contains a separate adjoint tensor contraction, so keeping the second core estimate explicit is justified.

The distinction between $\operatorname{Rat}_M A$ and $F\cap M$, with $F=\operatorname{Div}_{U(M)}A$, is essential and correctly maintained.
The cited Yin_C_F0012 example excludes its witness from $C^*(X)$.
Every bounded matrix-inverse representation over the original generators has its output in $C^*(X)$, because a unital C*-subalgebra and its matrix amplifications are inverse closed in the corresponding ambient C*-algebras.
Thus Yin_C_F0012 does exclude the proposed shortcut by bounded representations, as the final explanatory sentence states.
It does not provide a counterexample to the still-unproved bare-ACSY affiliated forward implication.

## Final Revision Verification

The complete initial artifact was read and all proof steps above were checked.
The coordinating agent then added the Yin_C_F0027 identifier, the review link, the explicit C*-algebra argument, and the weaker hypothesis statement for the analytic bridge.
The revised opening statement, relevant Section 5 dependencies, and final scope discussion were inspected against the original complete proof.
Every change is supported by that proof, and the final artifact is accepted without outstanding findings.

This is an internal AI mathematical review, not proof-assistant verification, numerical validation, external human peer review, or a historical-priority assessment.
