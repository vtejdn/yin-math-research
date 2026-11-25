---
author: Yin
---

# Finite-index transfer for the unrestricted commutator criterion

## Scope of the transfer

For a discrete group \(J\), write \(A_J=\mathbb CJ\), \(U_J=L^0(\mathcal N(J))\), and \(D_J=\operatorname{Div}_{U_J}(A_J)\).
The involution preserves \(D_J\) since it preserves the generators and the scalar inverse operations.
Say that \(D_J\) is regular when every \(x\in D_J\) has an inner inverse \(y\in D_J\) with \(xyx=x\).
The inherited involution is positive definite, so this is equivalent to \(*\)-regularity and to \(p_{\ker x}\in D_J\) for all \(x\in D_J\). [Regular closure and kernel projections](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected)

For every finite-index subgroup \(H\le G\), regularity of \(D_G\) is equivalent to regularity of \(D_H\).
Consequently, among finitely generated groups, the property that equation (1) by itself detects division-closure membership for all affiliated elements is invariant under abstract commensurability. [The unrestricted equation](../tasks/Yin_T_A0003_v3.md#contract)
This gives complete deletion of the local condition on a commensurability class as soon as one member has regular division closure.

## The finite-index coefficient matrices

Choose representatives \(g_1=1,\ldots,g_m\) of the left cosets \(G/H\).
Identify \(\ell^2G=\bigoplus_{i=1}^m\lambda(g_i)\ell^2H\).
The block of a left translation by \(g\) from the \(j\)-th summand to the \(i\)-th is left translation by \(g_i^{-1}gg_j\in H\) if \(gg_j\in g_iH\), and zero otherwise.
This gives a unital normal \(*\)-embedding \(\mathcal N(G)\hookrightarrow M_m(\mathcal N(H))\) in the indicated Hilbert space identification, carrying \(A_G\) into \(M_m(A_H)\).
Spectral calculus extends it to a unital \(*\)-embedding \(\iota:U_G\to M_m(U_H)\).
Separately, the natural trace-preserving inclusion \(\mathcal N(H)\subseteq\mathcal N(G)\) extends to \(U_H\subseteq U_G\).
The first summand reduces \(U_H\) under this inclusion and its restriction there is the original representation.

We have the exact intersection formula
\[
                 \iota(D_G)=\iota(U_G)\cap M_m(D_H).
\]
To prove the forward inclusion, write \(x\in D_G\) in an affine realization \(x=\alpha L^{-1}\beta\) with constant \(\alpha,\beta\) and an injective bounded square pencil \(L\) over \(A_G\).
In the coset representation \(L\) becomes an injective bounded square matrix over \(A_H\).
The Gram argument for group pencils also applies to any such bounded matrix \(C\) over \(A_H\).
Each leading block of \(C^*C\) is the Gram matrix of an injective restriction of \(C\), hence is an affiliated unit.
Inductive Schur elimination then uses only inverses of scalar affiliated units belonging to \(D_H\), giving \(C^{-1}\) with entries in \(D_H\).
Contraction with the constant row and column proves \(\iota(x)\in M_m(D_H)\). [Affine realizations and scalar Gram elimination](../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)

For the converse, take \(y\in U_G\) and let \(a_i=\iota(y)_{i1}\in U_H\).
Then
\[
                         y=\sum_{i=1}^m\lambda(g_i)a_i .
\]
Indeed, subtract the right side and call the difference \(h\).
Its first block column is zero since the first block column of each summand has \(a_i\) in position \(i\) alone.
Thus \(\iota(h)e_{11}=0\) in the affiliated matrix algebra.
Multiplying by the ambient relative inverse shows \(p_{\ker\iota(h)}e_{11}=e_{11}\), so the Hilbert space kernel of \(h\) contains \(\ell^2H\).
This kernel is invariant under all right translations of \(G\) because \(h\) is affiliated with \(\mathcal N(G)\).
The translates of \(\ell^2H\) span a dense subspace of \(\ell^2G\), forcing \(h=0\).
This argument also handles unbounded entries of the first column.
In particular, if \(\iota(y)\in M_m(D_H)\), then all \(a_i\in D_H\subseteq D_G\) and hence \(y\in D_G\).
Here the inclusion \(D_H\subseteq D_G\) follows by evaluating a finite scalar rational expression in the inclusion \(U_H\subseteq U_G\).
The same computation gives \(D_G=\bigoplus_i\lambda(g_i)D_H\) as a right \(D_H\)-module and \(D_G\cap U_H=D_H\), the latter by taking the first diagonal block of an element of \(U_H\).

## Ascent and descent of kernel projections

If \(D_H\) is regular, then \(M_m(D_H)\) is \(*\)-regular by matrix permanence of von Neumann regularity and positive definiteness of the involution. [Matrix amplification of regular rings](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)
For \(x\in D_G\), the kernel projection of \(\iota(x)\) consequently belongs to \(M_m(D_H)\), since a \(*\)-regular subring contains the relative inverse and kernel projection of each of its elements.
This projection is also \(\iota(p_{\ker x})\) by spectral calculus.
The intersection formula gives \(p_{\ker x}\in D_G\).

Conversely, suppose \(D_G\) is regular and \(x\in D_H\).
Its kernel projection in \(U_H\) maps to the kernel projection in \(U_G\) under the spectral inclusion.
It therefore belongs to \(D_G\cap U_H=D_H\).
This proves descent as well as ascent for arbitrary finite index.
Finite generation passes between the groups in a finite-index pair.
The characterization by kernel projections now gives the stated commensurability invariance of equation (1).

## A class where equation (1) suffices

Suppose \(G\) is finitely generated and has a locally indicable subgroup \(H\) of finite index.
The subgroup \(H\) satisfies the strong Atiyah conjecture over \(\mathbb C\) and is torsion-free, so \(D_H\) is a division ring. [Jaikin-Zapirain and López-Álvarez, Theorem 1.1](https://arxiv.org/pdf/1810.12135#page=2) and [Linnell and Lück, Theorem 2.3(3)](https://arxiv.org/pdf/1602.06906#page=10)
It follows that \(D_G\) is regular and the unrestricted finite-rank equation characterizes \(D_G\) for every \(u\in U_G\).
In particular this proves the desired deletion for all torsion-free virtually locally indicable groups.

There is also a direct published route for this class.
The normal core of \(H\) is locally indicable and has finite index.
Linnell and Lück's Lemma 2.9 gives semisimple Artinian division closure in \(U_G\) whenever the finite-index normal subgroup is torsion-free and has skew-field division closure. [Linnell and Lück, Lemma 2.9](https://arxiv.org/pdf/1602.06906#page=12)
Semisimplicity alone supplies regularity here.
The argument requires no division-ring conclusion for \(D_G\) itself.
The universal deletion question still asks for regularity of \(D_G\) for every finitely generated torsion-free \(G\), including groups outside these finite-index cases.
