---
author: Yin
---

# Affiliated-Rationality Manuscript Conventions

These conventions apply to the Yin_T_F0001 paper.
The current TeX remains authoritative for the mathematical manuscript.
The [writing choices](writing.md) govern audience, exposition, source roles, citations and bibliography display.
The [organization record](organization.md) governs selected environments and their order.

## Tracial Setting and Operator Actions

Use a tracial \(W^*\)-probability space \((\mathcal M,\tau)\) with faithful normal tracial state.
Set \(H=L^2(\mathcal M,\tau)\) and \(\Omega=1\).
Identify elements of \(\mathcal M\) with left multiplication and use \(\rho(x)\xi=\xi x\) for right multiplication.
The inner product is linear in its second variable.
Explain the setting and operator actions at their first mathematical use rather than repeating them mechanically.

## Algebras, Fractions and Rationality

Write \(\mathcal A_X=\mathbb C\langle X_1,\ldots,X_d\rangle\) and \(\mathcal A_X^\ast=\mathbb C\langle X_1,\ldots,X_d,X_1^\ast,\ldots,X_d^\ast\rangle\).
Use \(\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X\) and \(\operatorname{Div}_{\mathcal M}\mathcal A_X\) directly.
Do not introduce aliases such as \(F_X\) or \(R_X\) for these division closures.
Use “rational in \(X\)” for membership in the division closure and distinguish this from rational closure when the distinction matters.

Name \(L^0(\mathcal M)\) the \(*\)-algebra of affiliated operators.
At its definition, state that its elements are closed, densely defined operators affiliated with the specified finite tracial von Neumann algebra.
Do not shorten the name to “affiliated algebra”.
Name tensor products by their actual factors and distinguish algebraic tensors from Hilbert-space or von Neumann tensor products.

Use “fraction pair” for \(Q=(s,a,b,t)\) with \(u=s^{-1}a=bt^{-1}\).
Call \(s,t\) denominators and \(a,b\) numerators.
Use “left fraction” for \(s^{-1}a\) and “right fraction” for \(bt^{-1}\).
Do not add “bounded” to “fraction pair” or call numerators and denominators coefficients.
State boundedness where it is needed mathematically, and retain regularity of denominators.

Use “free field” for the universal division ring of fractions of a free polynomial algebra.
Do not use “free skew field” for this object.
When specifying a finite-generator free group, write “a free group \(\mathbb F_d\) with \(d\) generators” and use the manuscript macro `\bF_d`.

## Tensor Right Multiplication

For $x\in L^0(\mathcal M)$, use $\Psi_x(k):=k(x\otimes1-1\otimes x^{\mathrm{op}})$ on $L^0(\mathcal M)\otimes_{\mathbb C}L^0(\mathcal M)^{\mathrm{op}}$.
For the fixed tuple X, write $\Psi_i:=\Psi_{X_i}$.
In the proof of Lemma 4.3, right multiplication by $x^{\mathrm{op}}$ on the second factor sends $v^{\mathrm{op}}$ to $(xv)^{\mathrm{op}}$.
Use a tilde for the induced quotient-space maps there, reserving the bar for operator closure.

## Dual Systems and Fraction Commutators

Use \(D_i\) for a dual system in Definition 1.8, with
\(\mathcal M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*\) and the generator-first normalization
\[
[X_j,D_i]=\delta_{ij}P_\Omega\qquad\text{on }\mathcal M\Omega.
\]
State normality and generation separately in results that use them.
Bounded dual systems satisfy the domain requirements automatically.
Use \(P_\Omega\) directly for the orthogonal projection onto \(\mathbb C\Omega\).
For \(D_i^\circ:=D_i|_{\mathcal M\Omega}\), write its closure as \(\overline{D_i^\circ}\), not with a separate hat notation.
Write its adjoint as \((D_i^\circ)^*\).

Use \(L_i\) for liberation dual operators associated with an arbitrary tuple \(X\in\mathcal M^d\) on \(H=L^2(\mathcal M,\tau)\).
The manuscript's domain variant has \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*\) and the generator-first relation \([X_j,L_i]=\delta_{ij}[X_i,P_\Omega]\) on \(\mathcal M\Omega\).
The term refers to this explicitly defined variant of Voi99 Definition 13.1; it does not import that source's boundedness or selfadjointness requirements.
Call a liberation dual system **normalized** when \(\sum_iL_i\xi=P_\Omega\xi\) for every \(\xi\in\mathcal M\Omega\).
This sum condition is a manuscript convention; it is not the zero-vacuum normalization of ordinary dual systems in MS23 Definition 2.4.
Use normalized rather than canonical: the sum condition does not select a unique system.
Theorem 1.7 fixes any such normalized system and includes \(\overline{\Gamma[Q,L_i]}\in[\rho(X_i),\mathcal F(H)]\) for every fraction pair and every index as assertion (4).
The liberation criterion assumes that \(X_i-\lambda\) is regular for every \(1\leq i\leq d\) and every \(\lambda\in\mathbb C\).
Generation of the ambient algebra is specified where needed, in particular in the liberation-gradient and conjugate-variable constructions.
For the liberation contraction on \(\mathcal P_i\Omega\), use \(C_i^\circ\), its actual closure \(C_i:=\overline{C_i^\circ}\), and \(L_i:=\mathrm i C_i\), consistent with the generator-first liberation commutator.
Lemma 4.1 then supplies a normalized system.

Use “fraction commutator” for the project-local construction associated with \(Q\):
\[
\Gamma[Q,D]:=sDb-aDt,\qquad
\operatorname{Dom}\Gamma[Q,D]=\{\xi\in H:b\xi,t\xi\in\operatorname{Dom}D\}.
\]
The formal cleared-denominator identity is \(\Gamma[Q,D]=s[D,u]t\) when the compositions are defined.
The expression \(sDb-aDt\) on the stated domain defines the operator; the formal identity alone does not establish boundedness or an everywhere-defined commutator.
For bounded \(u\), the unit-denominator fraction pair recovers \([D,u]\) on its natural domain.
The operator may depend on the fraction pair.
Use \(\Gamma[Q,D_i]\) for bounded duals and \(\overline{\Gamma[Q,D_i]}\) for a bounded closure.
State the domain and bounded-extension hypotheses whenever an unbounded dual is used.
Do not attribute the local name “fraction commutator” to Miy22.

Use \(\mathcal F(H)\) for bounded finite-rank operators and \(S_2(H)\) for the Schatten class of Hilbert--Schmidt operators.
Use \(T_i\) for finite-rank operator witnesses and \(T=(T_1,\ldots,T_d)\) for a tuple.
Use “von Neumann dimension” for the module dimension in \(\Delta\), with Luc02 Definition 1.10 for the name and CS05 Definition 2.10 for the general tracial-algebra construction.

<a id="conjugate-variables"></a>
## Liberation Gradients and Conjugate Variables

Use Definition 6.1 for \(L^2\) liberation gradients on \(\mathcal P_i=\operatorname{Alg}(A_i,B_i)\), where \(A_i=W^*(X_i)\) and \(B_i=W^*(X_j:j\ne i)\), with \(B_1=\mathbb C1\) when \(d=1\).
The represented derivations \(\gamma_i\) must be well-defined on this full algebra and satisfy \(1\otimes1\in\operatorname{Dom}\gamma_i^*\) for their actual Hilbert-space adjoints.
With the manuscript's second-variable-linear inner product, write \(j_i:=j(A_i:B_i)=-\gamma_i^*(1\otimes1)\), so \(j_i^*=-j_i\) and \(\tau(j_ip)=(\tau\otimes\tau)(\gamma_ip)\).
For the real derivation and its adjoint vector, use \(\delta_i:=\mathrm i\gamma_i\) and \(\eta:=\mathrm i j_i=\delta_i^*(1\otimes1)\).
Lemma 6.2 constructs a normalized liberation dual system from these hypotheses.
Proposition 6.3 adds normality and nonatomic spectral distributions explicitly; finiteness of liberation Fisher information alone does not supply nonatomicity.

Use Definition 6.4 for the existence of ordinary conjugate variables on \(\mathcal A_X^\ast\).
In Lemma 6.6 and Corollary 6.7, write admits conjugate variables and cite Definition 6.4 rather than repeating the derivation conditions.
Choose the derivations from that definition at the start of a proof when they are used.
The tuple X generates M, so the starred polynomial algebra is dense in H.
The definition requires derivations \(\partial_i\) with \(\partial_iX_j=\delta_{ij}1\otimes1\) and \(1\otimes1\in\operatorname{Dom}\partial_i^*\).
For such derivations, write \(\xi_i:=\partial_i^*(1\otimes1)\in H\) for the conjugate variables.
In Lemma 6.6, distinguish the polynomial derivation \(\gamma_i^\circ:=\Psi_i\partial_i\) from the derivation \(\gamma_i\) on \(\mathcal P_i\).
The formula \(j_i=[\xi_i,X_i^*]\) is first proved on the polynomial algebra; the word-moment extension and relation descent establish the full-domain actual adjoint condition before Proposition 6.3 is applied.
Remark 6.8 retains the arcsine example and records \(j(W^*(X):\mathbb C)=0\).

## Terminology and Concise Explanations

Retain the name “Jacobi's identity” and briefly explain it or give the commutator formula when using it.
In the fundamental commutator identity, mention traciality, density of \(\mathcal M\Omega\) and boundedness for the extension instead of a vector-by-vector calculation.
The tensor, trace and operator-restriction terminology follows the explicit conventions above together with the current repository writing rules.
