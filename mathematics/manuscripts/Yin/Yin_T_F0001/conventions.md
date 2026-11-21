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

Write \(\mathcal A_X=\mathbb C\langle X_1,\ldots,X_d\rangle\).
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

<a id="tensor-element-notation"></a>
## Tensor Element Notation

Use $\ell$ as the default symbol for elements introduced in the algebraic tensor product $\mathcal M\otimes_{\mathbb C}\mathcal M^{\mathrm{op}}$ in this paper.
Use indices or other decorations to distinguish such tensors that occur together, such as $\ell_i$ and $\ell_0$.
Retain existing notation for tensors introduced in $L^0(\mathcal M)\otimes_{\mathbb C}L^0(\mathcal M)^{\mathrm{op}}$, $H\otimes_{\mathbb C}H$ or abstract vector-space tensor products.

## Tensor Right Multiplication

For $x\in L^0(\mathcal M)$, use $\Psi_x(k):=k(x\otimes1-1\otimes x^{\mathrm{op}})$ on $L^0(\mathcal M)\otimes_{\mathbb C}L^0(\mathcal M)^{\mathrm{op}}$.
For the fixed tuple X, write $\Psi_i:=\Psi_{X_i}$.
In the proof of Lemma 4.6, right multiplication by $x^{\mathrm{op}}$ on the second factor sends $v^{\mathrm{op}}$ to $(xv)^{\mathrm{op}}$.
Use a tilde for the induced quotient-space maps there, reserving the bar for operator closure.

For the range assertion in [Lemma 4.6](paper/sections/liberation-dual-system-criterion.tex), put \(U:=L^0(\mathcal M)\), \(V:=U\otimes_{\mathbb C}U^{\mathrm{op}}\) and \(W:=H\otimes_{\mathbb C}H\), with the second factor identified as in Definition 1.3.
The linear map \(m:V\to U\), \(m(u\otimes v^{\mathrm{op}}):=uv\), satisfies \(m\Psi_x(u\otimes v^{\mathrm{op}})=uxv-u(xv)=0\).
Since \(m(1\otimes1)=1\), the tensor \(1\otimes1\in W\) does not belong to \(\Psi_x(V)\).
For \(x\in\mathcal M\) with every \(x-\lambda\) regular, Lemma 4.6 gives injectivity on \(V\) and \(\Psi_x^{-1}(W)=W\); thus \(\Psi_x|_W\) is a bijection onto \(\Psi_x(V)\cap W\), a proper subspace of \(W\).

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

For a linear operator \(L\) on \(H\) with \(\mathcal M\Omega\subseteq\operatorname{Dom}L\), use \(m_L(\ell):\mathcal M\Omega\to H\) for \(\ell\in\mathcal M\otimes_{\mathbb C}\mathcal M^{\mathrm{op}}\).
On \(\mathcal M\Omega\), set \(m_L(c\otimes e^{\mathrm{op}}):=cLe\) for \(c,e\in\mathcal M\) and extend linearly in \(\ell\).
Use \(m_{L_i}\) in Section 4 and \(m_{D_i}\) in Lemma 5.3.

Use “fraction commutator” for the project-local construction associated with \(Q\):
\[
\Gamma[Q,D]:=sDb-aDt,\qquad
\operatorname{Dom}\Gamma[Q,D]=\{\xi\in H:b\xi,t\xi\in\operatorname{Dom}D\}.
\]
The formal cleared-denominator identity is \(\Gamma[Q,D]=s[D,u]t\) when the compositions are defined.
The expression \(sDb-aDt\) on the stated domain defines the operator; the formal identity alone does not establish boundedness or an everywhere-defined commutator.
For bounded \(u\), the unit-denominator fraction pair recovers \([D,u]\) on its natural domain.
The operator may depend on the fraction pair.
Use \(\Gamma[Q,D_i]\) for the fraction commutator and \(\overline{\Gamma[Q,D_i]}\) for its closure.
Specify the domain of an identity involving possibly unbounded operators and state any bounded-extension hypotheses it uses.
Do not attribute the local name “fraction commutator” to Miy22.

Use \(\mathcal F(H)\) for bounded finite-rank operators and \(S_2(H)\) for the Schatten class of Hilbert--Schmidt operators.
Use \(T_i\) for finite-rank operator witnesses and \(T=(T_1,\ldots,T_d)\) for a tuple.
Use “von Neumann dimension” for the module dimension in \(\Delta\), with Luc02 Definition 1.10 for the name and CS05 Definition 2.10 for the general tracial-algebra construction.

<a id="liberation-gradients"></a>
## Liberation Gradients

Remark 4.1 uses \(j(A_i:B_i)\) for the liberation gradients, where \(A_i=W^*(X_i)\) and \(B_i=W^*(X_j:j\ne i)\), with \(B_1=\mathbb C1\) when \(d=1\).
It cites Voi99 Sections 5.3--5.4 for the gradient formulation and states the existence of a normalized liberation dual system with the domains in Definition 1.6.
The construction and estimates remain in [C_F0082](../../../claims/Yin_C_F0082_v1.md#argument).
For the normal-operator application, nonatomicity is a separate hypothesis.

Example 6.1 gives the arcsine example and records \(j(W^*(X):\mathbb C)=0\).
It excludes ordinary dual systems by applying the dual commutator to odd monomials and using both vacuum domain inclusions.

## Terminology and Concise Explanations

Retain the name “Jacobi's identity” and briefly explain it or give the commutator formula when using it.
In the fundamental commutator identity, mention traciality, density of \(\mathcal M\Omega\) and boundedness for the extension instead of a vector-by-vector calculation.
The tensor, trace and operator-restriction terminology follows the explicit conventions above together with the current repository writing rules.
