---
author: Yin
---

# Finite-depth and sparse descent past the two critical metabelian quotients

## Statement

Suppose \(H=\langle s,t\rangle\) is torsion-free with scalar group-ring injectivity and the two-by-two four-site matrix \(K_0=B+At-s(D+Ct)\) has regular rank \(3/2\).
Use the unnormalized coordinate trace.
Suppose \(H\) surjects onto \(C_m\) for \(m=25\) or \(26\), and put \(N=[H,H]\), \(K=[N,N]\), \(b=[N:K]\).
The [abelian quotient exclusion](Yin_C_A0201_v1.md#consequence-for-finite-abelian-quotient-orders) and finite generation force \(H_{\rm ab}=C_m\).
Indeed any larger finite abelianization surjecting onto \(C_m\) would have order at least \(2m\), and an infinite finitely generated abelianization would give cyclic quotients of arbitrarily large order.
Normalize the marking as in that same result.

* At order 25, \(b\) is odd and at most \(18^4 88^{20}\). There is a square matrix of size \(50b\) over \(\mathbb CK\) with regular nullity \(25b/2\).
  It has at most eight group monomials in each row and each column counted over all its entries.
  In particular some nonzero scalar of \(D_{50b-1}(K)\) has fractional regular rank.
* At order 26, \(b\) is odd and at most \(75^{24}\).
  With \(g=s^{13}\), let \(J_1=\langle K,g\rangle\). This is an index-two extension of \(K\).
  Over \(\mathbb C J_1\) there is a square matrix of size \(26b\) with at most eight group monomials in each row and column and regular nullity \(13b/2\).
  There is also an actual matrix \(V_1\in{\rm GL}_{13b}(D_b(K))\) satisfying
  \[
                      V_1\operatorname{Ad}_g(V_1)=g^{-2} I_{13b} .
  \]
  Consequently either a nonzero scalar of \(D_{(15b-3)/2}(K)\) has fractional regular rank, or there is a scalar norm solution in \(D_{(15b-1)/2}(K)\).
  In the latter case adjoining the actual \(g\) gives a half-dimensional scalar idempotent on \(J_1\); the norm solution has no nonzero two-sided group-ring clearing over \(K\).

Thus the ranks can be tested on the second derived subgroup itself at order 25, and on that subgroup and a specific index-two extension at order 26, with bounds independent of the group and the complex coefficients.
These are necessary consequences of a counterexample, including when \(b=1\).

## Restricting the four-site matrix

The [prime-power order test](Yin_C_A0212_v1.md#statement) and the [order-26 test](Yin_C_A0210_v1.md#statement) give the respective bounds and oddness of \(b\).
At order 25, \([H:K]=25b\).
At order 26 the metabelian quotient is \((N/K)\rtimes C_{26}\) with the marked \(s\) lifting the cyclic factor, by [the cyclic coefficient calculation](Yin_C_A0210_v1.md#the-cyclic-coefficient-module).
Thus \(g^2=s^{26}\in K\), \(g\notin K\) and \([H:J_1]=13b\).
In each case let \(H_1\) be the proposed subgroup and \(e=[H:H_1]\), an odd integer.

Decompose \(\ell^2(H)\) over the left cosets \(h_iH_1\) into \(e\) copies of \(\ell^2(H_1)\), using \(h_i x\mapsto x\).
Each group translation acts as a single permutation with group elements on the nonzero positions.
The restriction of a finite matrix over \(\mathbb CH\) gives a finite matrix over \(\mathbb CH_1\).
Its unnormalized kernel dimension over \(H_1\) is \(e\) times that over \(H\): the coset-coordinate diagonal traces sum the kernel projection diagonal coefficients at all \(h_i\), which are equal by commutation with right translations.
Each original row or column here has at most eight coefficient monomials, since there are two coordinate indices and four group sites.
Each monomial contributes at most once to a given new row or column, proving the support bound even when some terms coincide.
This gives both sparse witnesses.

For any \(d\)-by-\(d\) group-ring matrix of noninteger regular rank, scalar Gaussian elimination either encounters a nonzero nonunit or removes a unit pivot and passes to its Schur matrix one inverse layer later.
Zero pivots can be avoided by row and column permutations when any nonzero entry exists.
Reaching a zero matrix after only unit pivots would make the original rank an integer.
Hence one encounters a fractional-rank scalar by depth \(d-1\), proving the first scalar consequence.

## Restricting the odd norm without an abstract specialization

In the order-26 case let \(J=\langle N,g\rangle\).
The [original kernel coordinates](Yin_C_A0199_v1.md#subgroup-coordinates-and-the-odd-dimensional-norm) give \(V\in{\rm GL}_{13}(D_1(N))\) with \((Vg)^2=I_{13}\).
Choose representatives in \(N\) for the \(b\) left cosets of \(K\) in \(N\).
They also represent the cosets of \(J_1\) in \(J\).
The preceding regular coordinate map gives a unital injection \(\rho:U(J)\to M_b(U(J_1))\), by applying the same unitary decomposition to affiliated operators.
It restricts on \(\mathbb CN\) to matrices over \(\mathbb CK\), and sends \(U(N)\) into \(M_b(U(K))\) by bounded transforms and spectral calculus.

One has \(\rho(D_1(N))\subseteq M_b(D_b(K))\).
For an input scalar denominator its image is a square group-ring matrix \(M\) invertible in \(M_b(U(K))\), by preservation of the true affiliated inverse.
Each entry of \(M^{-1}\) requires at most \(b\) scalar inverse layers on \(K\).
Indeed \(M^*M\) has full rank on each leading principal block, since the corresponding columns of \(M\) are jointly injective.
Successive Gram elimination uses one scalar affiliated-unit pivot per coordinate, and \(M^{-1}=(M^*M)^{-1}M^*\).
Sums and products stay in the resulting layer.
This is the [finite-index Gram calculation](Yin_C_A0129_v1.md#statement) restricted to the first input layer.

In the chosen coordinates \(\rho(g)=C(gI_b)\), with \(C\) a permutation matrix weighted by elements of \(K\).
Indeed \(g h_j=h_i k g\) for a unique target coset and some \(k\in K\), since \(g\) normalizes \(K,N\).
Separating the common \(g\) from \(\rho(Vg)\) therefore gives \(V_1(gI_{13b})\) with \(V_1\) over \(D_b(K)\).
Its square is the identity, proving the claimed norm.
The equation also gives its inverse in the same layer, by direct finiteness.
The dimension \(13b\) is odd.
Apply the [controlled semilinear elimination](Yin_C_A0213_v2.md#removing-a-cyclic-pair-of-coordinates) with initial layer \(b\) and \((13b-1)/2\) possible pairs.
The two depth bounds follow, and scalar injectivity passes to \(J_1\) from \(H\), giving the [two-sided clearing obstruction](Yin_C_A0213_v2.md#two-sided-denominators-in-the-scalar-branch).
All witnesses are obtained by faithful regular restriction; integrality for an arbitrary second derived subgroup and exclusion of the remaining scalar norm remain open.

## Assessment history

### Decision sparse-restriction-to-the-second-derived-subgroup

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:12 |
| status | proved |
| reason | Independent inspection verified the finite-index rank factors, sparsity and inverse-depth bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both critical quotient orders and all stated depth bounds. |
| argument | [Restricting the four-site matrix](#restricting-the-four-site-matrix) | Module dimension scaling and eight monomials in each row and column. |
| argument | [Restricting the odd norm without an abstract specialization](#restricting-the-odd-norm-without-an-abstract-specialization) | The genuine restricted norm, Gram inverses and controlled elimination. |
| review | [Sparse restriction to the second derived subgroup](../audits/reviews/Yin_R_A0190_v1.md#sparse-restriction-to-the-second-derived-subgroup) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-sparse-restriction-to-the-second-derived-subgroup)
