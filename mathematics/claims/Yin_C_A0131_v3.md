---
author: Yin
---

# Detecting division-closure membership by finite-rank commutators on a finite-dimensional subspace

## Statement

Let \(G=\langle g_1,\dots,g_d\rangle\) be a finitely generated discrete group.
Put \(H=\ell^2(G)=L^2(M,\tau)\), \(M=\mathcal N(G)\) and \(U=L^0(M)\), and let \(D_G\) be the division closure of the group algebra \(A=\mathbb CG\) in \(U\).
Write \(X_j=\lambda(g_j)\), let \(\rho_j\) be right multiplication by \(X_j\) on \(H\), and let \(P_e\) project onto \(\mathbb C\delta_e\).
Use \(M\delta_e\subset H\subset U\) to identify a bounded element with its vector.
Let \(\mathcal F(H)\) denote the bounded operators of finite complex rank.

For every \(u\in U\), membership \(u\in D_G\) is equivalent to existence of all the following witnesses.
Take a fraction pair \(u=s^{-1}a=bt^{-1}\) with \(s,a,b,t\in M\) and \(s,t\) invertible in \(U\), a tuple \(T_1,\ldots,T_d\in\mathcal F(H)\), and a finite-dimensional complex subspace \(V\subset H\) containing \(s\delta_e\) and the ranges of all \(T_j\).
They must satisfy
\[
             \sum_{j=1}^d[\rho_j,T_j]=sP_e b-aP_e t. \tag{1}
\]
The additional condition concerns only the restrictions of finite-rank operators to \(V\) and its translates.
For every \(B\in\mathcal F(H)\) require
\[
  B(s\delta_e)=0,\quad [B,\rho_j]|_V=0\ \ (1\le j\le d)
       \quad\Longrightarrow\quad B|_V=0 . \tag{2}
\]
In (2) commutation on \(V\) means \(B(vX_j)=B(v)X_j\) for every \(v\in V\).
The criterion applies to arbitrary finitely generated groups and to unbounded affiliated elements.

## Argument

### A subspace obtained from a rational element

For \(u\in D_G\), choose a fraction pair, solutions \(T_j\) of (1), and a finite row \(\eta\) of vectors in \(H\) whose span contains every \(\operatorname{Ran} T_j\), as given by the [pencil and range criterion](Yin_C_A0131_v2.md#statement).
This row satisfies \(\eta L=s\alpha\) for a scalar row \(\alpha\) and an injective square affine pencil \(L=L_0+\sum_j L_jX_j\) with scalar matrix coefficients.
Take \(V=\operatorname{span}_{\mathbb C}\{s\delta_e,\eta_1,\ldots,\eta_m\}\).
For \(B\) in the premise of (2), apply \(B\) to each entry of \(\eta L=s\alpha\).
Commutation on \(V\) gives \(B(\eta)L=0\) in \(H^{1\times m}\).
The pencil is invertible over \(U\), so multiplying on the right there gives \(B(\eta)=0\).
Together with \(B(s\delta_e)=0\) this proves (2).

### Recovering the vectors in the subspace

Suppose (1) and (2) hold.
Choose a basis \(v=(v_1,\ldots,v_n)\) of \(V\) with \(v_1=s\delta_e\), which is nonzero.
Set \(X_0=1\) and \(E=\sum_{j=0}^d VX_j\).
Choose a basis of the complex linear relations among the finite list \((v_iX_j)_{1\le i\le n,\,0\le j\le d}\).
For each such relation with coefficients \(c_{ij}\), form the column with entries \(\sum_{j=0}^d c_{ij} X_j\) indexed by \(i\).
Let \(P\) be the matrix of these columns and adjoin the first coordinate column to get \(K=[e_1\ P]\) with entries in \(A\).
Then \(vK=(s,0,\ldots,0)\) in affiliated matrices.

If \(z\in H^{1\times n}\) satisfies \(zK=0\), then \(z_1=0\) and the list \((z_iX_j)_{i,j}\) satisfies every linear relation of \((v_iX_j)_{i,j}\).
Consequently the assignments \(v_iX_j\mapsto z_iX_j\) define a linear map \(E\to H\).
Extend it by zero on \(E^\perp\) to get \(B\in\mathcal F(H)\).
It sends \(s\delta_e\) to zero and commutes with all \(\rho_j\) on \(V\).
Condition (2) gives \(z_i=Bv_i=0\) for all \(i\).

Taking adjoints entrywise identifies rows in \(H^{1\times n}\) with columns in \(H^n\) and sends \(zK\) to \(K^*z^*\).
The preceding step proves \(\ker K^*=0\), and the bounded positive square matrix \(S=KK^*\) has the same kernel.
It has an affiliated inverse by finite trace.
Each leading principal block of \(S\) is injective, since its quadratic form is the restriction of the positive definite quadratic form of \(S\).
When the inverse of one leading block has entries in \(D_G\), its scalar Schur complement in the next block belongs to \(D_G\) and is an affiliated unit because both blocks are invertible.
Starting with the first scalar block and inverting each such complement in \(D_G\) gives \(S^{-1}\in M_n(D_G)\). [Scalar pivot argument](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Thus \(K\) has a right inverse \(K^*S^{-1}\) with entries in \(D_G\).
Multiplying \(vK=(s,0,\ldots,0)\) by this right inverse gives \(s^{-1}V\subseteq D_G\).

The range of the left side of (1) is contained in \(E\).
Its value at \(t^*\delta_e\) is \(s\tau(bt^*)-a\tau(tt^*)\) by the right side of (1).
Since \(s\delta_e\in V\) and \(\tau(tt^*)>0\), this gives \(a\in E\).
Now \(s^{-1}E\subseteq\sum_{j=0}^d D_G X_j\subseteq D_G\), so \(u=s^{-1}a\in D_G\).

## Assessment history

### Decision local-commutation

| Field | Value |
| --- | --- |
| date | 2026-11-25T07:30 |
| status | proved |
| reason | Relations among a finite-dimensional subspace and its first translates give a group-algebra matrix with a right inverse over the division closure under the local commutation condition. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A division-closure criterion for all finitely generated groups using the fraction equation and finite-rank commutation on a subspace. |
| argument | [Argument](#argument) | Construction of the subspace and recovery of its normalized vectors from the matrix of all first-translation relations. |
| dependency | [Finite-rank witnesses for rational elements](Yin_C_A0131_v2.md#constructing-the-finite-rank-operators) | The fraction, the finite-rank solutions and the affine row for the forward implication. |
| dependency | [Scalar inverses of Gram blocks](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Finite-trace invertibility and scalar Schur elimination for an injective positive group-algebra matrix. |
| review | [Self-review](../audits/reviews/Yin_R_A0165_v3.md#finite-rank-commutation-on-a-subspace) | Scope, both implications and the cases of an unbounded inverse and a nonunit projection. |

## Current assessment

[Selected decision](#decision-local-commutation)
