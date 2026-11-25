---
author: Yin
---

# Finite-dimensional spaces for rational elements and for the unrestricted commutator equation

## Statement

Let \(G\) have a finite marking \(X_1,\ldots,X_d\), let \(A=\mathbb CG\), \(M=\mathcal N(G)\), \(U=L^0(M)\), and \(D=\operatorname{Div}_U(A)\).
Use the same \(X_j\) for the marked left multipliers regarded as elements of \(A\).
Fix \(u\in U\).
For a finite-dimensional complex subspace \(V\subset U\) containing \(1,u\), put \(E=V+\sum_j VX_j\).
Consider the complex-linear maps \(\phi:E\to U\) such that
\[
 \phi(1)=0,\qquad \phi(vX_j)=\phi(v)X_j \quad(v\in V,\ 1\le j\le d).
\]

1. There exists such a \(V\) for which every such map vanishes on \(V\) if and only if \(u\in D\).
2. There exists such a \(V\) for which every such map vanishes at \(u\) if and only if \(u\) admits fractions and finite-rank witnesses in [equation (1)](../tasks/Yin_T_A0003_v3.md#contract).
3. If one requires \(V\subset A+uA\), both vanishing tests are equivalent to \(u=pq^{-1}\) with \(p,q\in A\) and \(q\) an affiliated unit.

In the first criterion the only witness is \(V\), and the universal map test can be replaced by injectivity of the adjoint of the relation matrix below.
There are no denominator or commutator witnesses to specify in either finite-dimensional formulation.
The second criterion changes the subspace on which vanishing is required for the same class of maps.
The criteria in 1 and 2 still have separate existential choices of \(V\).
More precisely, for each \(k\ge1\), promotion of single-vector vanishing to membership in \(D\) for all finite markings and spaces of dimension at most \(k+2\) is equivalent to rationality of all kernel projections of group-ring matrices with \(k\) input columns.

## Argument

### Testing a whole space or a single vector

Choose a basis row \(v=(v_1,\ldots,v_n)\) for \(V\) with \(v_1=1\), and write \(u=v\gamma\) for a constant column \(\gamma\).
Put \(X_0=1\), and for a relation \(\sum c_{ij}v_iX_j=0\) use the column with entries \(\sum_j c_{ij} X_j\).
Take one column for each vector in a complex basis of the space of relations and adjoin \(e_1\) as the first column to obtain a matrix \(K\in M_{n,m}(A)\).
Then \(vK=\epsilon\), where \(\epsilon=(1,0,\ldots,0)\) is a row of length \(m\).
A row \(z\in U^{1\times n}\) with \(zK=0\) gives a map of the stated kind by \(v_iX_j\mapsto z_iX_j\), since all the complex relations are respected.
Conversely the restriction row of any such map satisfies \(zK=0\).
If \(P=p_{\ker K^*}\in M_n(M)\), the rows satisfying \(zK=0\) are exactly the rows with \(z=zP\), by the support identity in the affiliated algebra.
Consequently the whole-space test is \(P=0\), equivalently injectivity of \(KK^*\) on \(\ell^2(G)^n\), and the single-vector test is \(P\gamma=0\).

When \(P=0\), multiplication of \(vK=\epsilon\) on the right gives
\[
                      v=\epsilon K^*(KK^*)^{-1}.
\]
The inverse of this positive injective group-ring matrix has entries in \(D\) by [scalar Gram elimination](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations), so \(u=v\gamma\in D\).
Conversely every \(u\in D\) has an affine realization \(u=\alpha L^{-1}\beta\) with constant row and column, \(L=L_0+\sum_j L_jX_j\), and \(L\) invertible over \(U\). [Affine realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Use the span of \(1\) and the entries of \(\eta=\alpha L^{-1}\) as \(V\).
It contains \(u\), and applying \(\phi\) to \(\eta L=\alpha\) gives \(\phi(\eta)L=0\) by the local right-translation rules.
Thus \(\phi(\eta)=0\), proving the whole-space condition.

### Single-vector vanishing and equation (1)

Suppose \(u\) satisfies (1).
The [tensor characterization](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) gives an identity in \(U\otimes_{\mathbb C}U\)
\[
 u\otimes1-1\otimes u
   =\sum_{j,p}\big(l_{jp}X_j\otimes r_{jp}-l_{jp}\otimes X_jr_{jp}\big)
\]
with finitely many \(l_{jp},r_{jp}\in U\).
Choose \(V\) as the span of \(1,u\) and the \(l_{jp}\).
Both sides lie in \(E\otimes_{\mathbb C}U\), which includes injectively into \(U\otimes_{\mathbb C}U\).
Apply \(\phi\) to the first factor and multiply the two factors in \(U\).
Local commutation cancels every summand on the right and leaves \(\phi(u)=0\).

Conversely suppose \(P\gamma=0\) for some \(V\).
Let \(K^{[-1]}\in M_{m,n}(U)\) be the relative inverse, which inverts \(K\) between its supports and vanishes on its range complement.
It has entries in the \(*\)-regular closure \(R\) of \(A\) by matrix regularity, applied in a square block amplification when \(K\) is rectangular. [Matrix regularity and relative inverses](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)
Since \(KK^{[-1]}=1-P\), one obtains
\[
                         u=v(1-P)\gamma=\epsilon K^{[-1]}\gamma\in R .
\]
The [unrestricted commutator criterion](Yin_C_A0131_v1.md#statement) identifies membership in \(R\) with equation (1).
This use of the regular closure identifies precisely the condition imposed by single-vector vanishing on elements tested for \(D\).

### Restriction to the right module generated by the input

Suppose \(u=pq^{-1}\), with \(p,q\in A\) and \(q\in U^\times\).
For every group element in the supports of \(p,q\), choose a word in the marked generators and their inverses.
Take \(V\) to contain the span of the prefixes of these words starting respectively from \(1\) for \(p\) and from \(u\) for \(q\), together with \(1,u\); use exactly this span.
It lies in \(A+uA\).
Any \(\phi\) in the statement transports its value along each prefix by the corresponding right multiplier.
For a negative letter the next prefix multiplied by \(X_j\) is the preceding prefix, so the same commutation rule applies in reverse.
Applying \(\phi\) to \(uq=p\) gives \(\phi(u)q=\phi(1)p=0\).
Invertibility of \(q\) forces \(\phi(u)=0\) and consequently all prefix values vanish.

Conversely, take \(V\subset A+uA\) satisfying the single-vector test.
When \(u\in\mathbb C\), the scalar is its own numerator over \(1\).
Otherwise choose a basis beginning with \(1,u\) and for each \(i\) write \(v_i=a_i+ub_i\), \(a_i,b_i\in A\), taking \((a_1,b_1)=(1,0)\) and \((a_2,b_2)=(0,1)\).
For each basis relation \(\sum c_{ij}v_iX_j=0\) put \(m_c=\sum c_{ij}b_iX_j\in A\).
Then \(um_c=-\sum c_{ij}a_iX_j\in A\).
Form \(q=\sum_c m_c m_c^*\in A\), so that \(uq\in A\).
If \(q\) were not an affiliated unit, its nonzero kernel projection \(h\) would satisfy \(hm_c=0\) for every \(c\).
Thus \(v_iX_j\mapsto h b_iX_j\) would respect all the relations and define an allowed map with \(\phi(1)=0\) and \(\phi(u)=h\ne0\).
The single-vector condition therefore implies \(q\in U^\times\), proving the right fraction assertion and completing all three equivalences.

### The number of auxiliary vectors

For a fixed finitely generated group \(G\) and integer \(k\ge1\), the following conditions are equivalent.

1. For each finite matrix \(X\) over \(A\) with \(k\) columns, the kernel projection has entries in \(D\).
2. For every finite marking of \(G\), an element \(u\) passing the single-vector test with \(\dim_{\mathbb C}V\le k+2\) belongs to \(D\).

First suppose \(1,u\) are independent and the single-vector test holds for \(V\) of any finite dimension.
Choose the first two basis vectors as \(1,u\) and delete the first two rows of \(K\) to obtain \(K_0\).
Both \(Pe_1=0\) and \(Pe_2=0\), the first by the initial column of \(K\) and the second by the single-vector test.
Thus all columns in \(\ker K^*\) have zero first two coordinates, and \((0,0,\xi)^{\mathsf T}\) lies in that kernel exactly when \(K_0^*\xi=0\).
It follows that \(P=\operatorname{diag}(0,0,p_{\ker(K_0K_0^*)})\).
If the last block has entries in \(D\), then the group-ring matrix \(KK^*\) plus \(P\) is an affiliated unit over \(D\), and
\[
             u=\epsilon K^*(KK^*+P)^{-1}e_2\in D .
\]
Indeed \(vKK^*=\epsilon K^*\), and \(KK^*(KK^*+P)^{-1}=1-P\).
The inverse has rational entries by [scalar Gram elimination for affiliated matrices](Yin_C_A0132_v1.md#argument).
In dimension two the last block is empty, and for \(3\le\dim V\le k+2\) it is the kernel projection of a positive group-ring matrix of size at most \(k\).
Adding an identity block if needed permits application of condition 1.
The case \(u\in\mathbb C\) is immediate, proving \(1\Rightarrow2\).

Conversely put \(T=X^*X\in M_k(A)\) and \(p=p_{\ker X}=1-T^{[-1]}T\).
Fix indices \(i,j\) and set \(u=p_{ij}\), \(y=e_i^*T^{[-1]}\), a row of length \(k\).
Use the identities
\[
                yT^2=e_i^*T,\qquad u=\delta_{ij}-yTe_j .
\]
Enlarge the marking by the nonidentity group elements in the supports of the entries of \(T,T^2\).
On the span \(V\) of \(1,u\) and the \(k\) entries of \(y\), each identity involves only those vectors and their first translates.
Every allowed map satisfies \(\phi(y)T^2=0\) and \(\phi(u)=-\phi(y)Te_j\).
Properness applied to \(\phi(y)T^2\phi(y)^*\) gives \(\phi(y)T=0\), hence \(\phi(u)=0\).
Condition 2 gives \(p_{ij}\in D\), and the construction applies to each entry.
For \(k=1\) the test with at most three vectors thus covers exactly kernel projections of group-ring scalars.
Requiring the equivalent conditions for all \(k\) simultaneously gives [complete deletion](../tasks/Yin_T_A0003_v3.md#contract), since each \(V\) in the single-vector criterion is finite dimensional.
Equivalently, rational kernel projections of all group-ring matrices imply rational scalar kernel projections for \(D\) by the [bordered reduction](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil).

## Assessment history

### Decision two-vanishing-tests

| Field | Value |
| --- | --- |
| date | 2026-11-25T09:54 |
| status | proved |
| reason | An injective relation adjoint recovers all state vectors by a scalar rational inverse; a determined single vector only requires the inverse between supports. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Whole-space and single-vector vanishing, the scalar right fraction condition and the matrix-size equivalence at every finite bound. |
| argument | [Argument](#argument) | Linear relations, the balancing identity, inverse on supports, right fractions and the finite-dimensional construction of individual kernel entries. |
| dependency | [Unrestricted commutator criterion](Yin_C_A0131_v1.md#statement) | Finite balancing expressions and the identification of equation (1) with the regular closure. |
| dependency | [Affine realizations and Gram pivots](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | A row over an invertible affine pencil and scalar inversion of an injective positive group-ring matrix. |
| dependency | [Matrix regularity](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Rectangular relative inverses over the regular closure. |
| dependency | [Affiliated Gram pivots](Yin_C_A0132_v1.md#argument) | Inverses of square matrices over the division closure that are units over the affiliated ring. |
| dependency | [Bordered reduction](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil) | Relation between universal matrix projection membership and unrestricted deletion. |
| review | [Independent proof review](../audits/reviews/Yin_R_A0167_v1.md#finite-dimensional-tests) | Whole-space and single-vector conditions, the right fraction criterion and the matrix-size equivalence. |

## Current assessment

[Selected decision](#decision-two-vanishing-tests)
