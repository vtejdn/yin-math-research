---
author: Yin
---
# Dual systems for liberation derivations

## Voi99-U001

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published edition, Advances in Mathematics 146 (1999), 101–166; the unchanged local PDF is identified in the registry (private lookup: `../../../literature/registry.md#voi99-source-artifact`). |
| source-locator | Section 13, Definition 13.1, Remarks 13.2(a)–(e), Proposition 13.3; printed pp.160–161, PDF pp.60–61. |
| inspection | 2026-10-18, authoring agent for Yin. The complete section was read; both pages were visually inspected. The commutant conditions, normalizations, construction formulas and trace argument were checked. This is source review, not independent project review or formal verification. |

<a id="bounded-liberation-dual-system"></a>
## Definition 13.1: bounded selfadjoint dual systems

Let \((M,\tau)\) be a tracial \(W^*\)-probability space, let \(H=L^2(M,\tau)\), let \(\Omega=1\), and let \(P_\Omega\) project onto \(\mathbb C\Omega\).
The algebras act by left multiplication.
For unital von Neumann subalgebras \(A_1,\ldots,A_n,B\subseteq M\), a source dual system to \((A_1,\ldots,A_n;B)\) consists of bounded selfadjoint \(T_j\in\mathcal B(H)\) satisfying
\[
 T_j\in\bigl(W^*(A_1,\ldots,\widehat A_j,\ldots,A_n,B)\bigr)',
 \qquad T_j-P_\Omega\in A_j'.
\]
Equivalently,
\[
 [a,T_j]=[a,P_\Omega]\quad(a\in A_j),\qquad
 [c,T_j]=0\quad(c\in A_k,\ k\ne j,\ \text{or }c\in B).
\]
The prime is the commutant in \(\mathcal B(H)\).
Definition 13.1 imposes no vacuum-annihilation condition.
The section explicitly identifies these as the analogues, for the liberation derivation, of the dual systems for free difference quotients in Part V.
The expression “liberation dual system” is a descriptive name for this role; the source calls the object a “dual system to \((A_1,\ldots,A_n;B)\).”

## Relations and proof checks

| Passage | Checked statement and reasoning |
| --- | --- |
| 13.2(a) | Group consecutive algebras into \(C_s=W^*(A_{n_{s-1}+1},\ldots,A_{n_s})\), with \(0=n_0<\cdots<n_k=n\), and put \(R_s=\sum_{n_{s-1}<p\le n_s}T_p\). On each generating algebra exactly one summand contributes \([a,P_\Omega]\); all others commute. This gives the grouped system. The last tuple is \(C_1,\ldots,C_k\); the printed \(C_n\) is an index slip. |
| 13.2(b) | Subtracting two systems removes the \(P_\Omega\) terms, so each coordinate difference belongs to the commutant of the generated algebra. |
| 13.2(c) | For the Part V convention with selfadjoint \(X_k,Y_k\), \([X_p,Y_k]=\mathrm i\delta_{pk}P_\Omega\), define \(T_k=\mathrm i[Y_k,JX_kJ]\). Selfadjointness follows from the commutator of selfadjoint operators; Jacobi's identity and commutation of left and right multiplication give \([T_k,X_p]=\delta_{kp}[P_\Omega,X_k]\). The identity \([P_\Omega,JX_kJ]=[P_\Omega,X_k]\) uses traciality. |
| 13.2(d) | Compression to \(L^2(N)\), for \(A_1,\ldots,A_n,B\subseteq N\subseteq M\), preserves selfadjointness and both commutant identities because \(E_N\) intertwines the left action and fixes the vacuum. |
| 13.2(e) | The free-product construction uses the right free-product representations of the source operators and the left representations of the algebras. The commutator is zero on reduced words except for the vacuum/terminal-letter transition, which gives the required vacuum projection term. This uses the usual left/right free-product Hilbert-space representation, not tensor-product amplification. |
| 13.3 | If \(T\) is dual to \((A;B)\) on \(L^2(W^*(A,B))\), then \(j(A:B)=(T-JTJ)\Omega\). Expanding \([T,a_1b_1\cdots a_nb_n]\), using \([T,a]=[P_\Omega,a]\), and pairing with the vacuum gives exactly the moment formula for \(j\). |

In Proposition 13.3 the displayed operator expression must act on \(\Omega\) to denote an \(L^2\) vector.
The printed formula omits this application; the first line of its proof explicitly uses \(T1\) and \(JT1\).
The gradient formula uses selfadjointness of \(T\); it is not an adjoint formula for an arbitrary unbounded operator.

<a id="liberation-dual-system-domain-variant"></a>
## Definition: a domain variant for normal generators

Let \(X_1,\ldots,X_d\in M\) be bounded normal operators generating \(M\).
A liberation dual system for \(X\), in this domain variant, is a tuple of linear operators \(L_i\) on \(H\) satisfying
\[
 M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*,
 \qquad L_i\Omega=0,
\]
and
\[
 [X_j,L_i]\xi=\delta_{ij}[X_i,P_\Omega]\xi
 \quad(\xi\in M\Omega,\ 1\le i,j\le d).
\]
The domain inclusion already implies dense definition and closability.
Every composition displayed on \(M\Omega\) is defined because \(X_jM\Omega\subseteq M\Omega\).
This definition is a local adaptation of the source's commutation pattern, with an explicit vacuum normalization.
It does not require boundedness or selfadjointness.
No equivalence with Definition 13.1, existence theorem, or permission to subtract an arbitrary unbounded commutant operator is asserted by the definition.

For \(A_i=W^*(X_i)\) and \(B=\mathbb C1\), the source's bounded commutant relations imply the displayed generator relations.
That comparison alone does not produce \(L_i\Omega=0\).
Conversely, passing from unbounded generator relations on \(M\Omega\) to von Neumann algebra relations requires an appropriate domain/intertwining argument.
The source's bounded commutant definition does not itself prove that passage.

## Dependencies and limits

The source uses the tracial standard representation, conditional expectations, the free-product Hilbert-space representations, and the liberation-gradient moment definition from [Voi99-U003](Yin_U003_v1.md#liberation-derivation-and-gradient).
Those foundational constructions are accepted inputs; their original external proofs were not recursively audited.
The full source does not state that a square-integrable liberation gradient alone supplies this domain variant with \(M\Omega\) in both domains.
The complete source-review coverage and remaining issues are recorded in the [source entrance](readme.md).
