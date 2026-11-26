---
author: Yin
---

# Two explicit rank-two commutators exposing the original Schur kernel

## Statement

Under the [order-24 half-kernel hypotheses](Yin_C_A0282_v1.md#statement), let \(K=B+At-s(D+Ct)\) and permute scalar rows and columns so that \(K=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) has a chosen nonzero pivot \(a\).
Use the permuted coefficient matrices in this expression.
Put \(\sigma=d-ca^{-1}b,\ p=1_{\ker\sigma}\), and let \(D_j\) denote the actual scalar inverse layers in \(U(H)\).
There are bounded operators \(T_s,T_t\) of ordinary complex rank exactly two such that
\[
     [\rho_s,T_s]+[\rho_t,T_t]=uP_e v
\]
has ordinary rank one, with
\[
      u\in D_1\cap\mathcal N(H),\qquad
      v\in D_2\cap\mathcal N(H),\qquad
      \operatorname{supp}_r u=1-p,\quad \operatorname{supp}_l v=p .
\]
Each input is a sum of two operators \(xP_e y\) with \(x\in D_1\cap\mathcal N(H)\) and \(y\in D_2\cap\mathcal N(H)\).
Here \(\rho_g\) is right multiplication on \(\ell^2(H)\), and \(P_e\) projects onto the identity group vector.
The closed spans of left translates of the output range and adjoint range are exactly \(L^2(\mathcal N(H))(1-p)\) and \(L^2(\mathcal N(H))p\), each of dimension one half.
Thus the two-label [rank-one boundary criterion](Yin_C_A0157_v1.md#separating-the-ranges-and-excluding-rank-one) can use this particular kernel projection in the original group.

All left factors and \(u\) use only the single inverse of the group-ring scalar \(a^*a+c^*c\).
For the right factors one may first use only \(a^{-1},\det(Ct+D)^{-1}\), taking the determinant before the column permutation if working in the initial coordinates, and then use one positive scalar inverse as described below, allowing adjoints.
The construction requires no bounded inverse for the pivot.

## A balance with the specified two labels

Write \(Q=Ct+D\) and put \(\ell=(-ca^{-1},1),\ \theta=(-a^{-1}b,1)^{\mathsf T}\).
The [actual first-layer idempotent](Yin_C_A0282_v1.md#recovering-the-scalar-idempotent-from-the-schur-coordinate) gives a scalar \(h\) with \(hU=\ker_U\sigma\), using only the indicated pivot and cyclic determinant inverses.
Let \(z=\theta h\).
Then \(Kz=0,\ z_2=h,\ \ell K=(0,\sigma)\).
In \(U\otimes_{\mathbb C} U\), use \(\Psi_g(v\otimes w)=vg\otimes w-v\otimes gw\).
Summing the balancing differences for all four entries of \(K\) gives
\[
 \sum_{i,j}\big(\ell_i K_{ij}\otimes z_j-\ell_i\otimes K_{ij}z_j\big)
                    =\sigma\otimes h.
\]
Splitting the \(st\) terms first at \(s\) and then at \(t\) writes the left side as
\[
    -\Psi_s\left(\sum_i\ell_i\otimes(Qz)_i\right)
       +\Psi_t\left(\sum_j(\ell(A-sC))_j\otimes z_j\right).
\]
The constant term balances over \(\mathbb C\).
The terms belonging to \(s\) include the entire \(Qz\); the remaining \(t\) terms have \(s\) on the first leg of the \(C\)-coefficient.
Each sum has just two elementary tensors.

## Bounded coefficients and the two support projections

The group-ring scalar \(P=a^*a+c^*c\) is an affiliated unit since \(a\) is injective.
Set
\[
           L=1-cP^{-1}c^*,\qquad Lca^{-1}=cP^{-1}a^* .
\]
Indeed for \(x=ca^{-1}\) the equality \(P=a^*(1+x^*x)a\) gives these identities from \(L=(1+xx^*)^{-1}\).
Both \(L\) and \(Lx\) are bounded by scalar singular-value calculus, and \(L\) is an affiliated unit.
Therefore \(L\ell,\ L\ell(A-sC)\) and \(u=L\sigma=Ld-(Lx)b\) are bounded, with the advertised single inverse.

Stack the four entries of \(z,Qz\) as a column \(Z\), and put \(R=(1+Z^*Z)^{-1}\).
This positive contraction is an affiliated unit in \(D_2\); \(ZR\) is bounded because the scalar function \(r/(1+r^2)\) is bounded.
In particular \(v=hR\) is bounded.
Multiply the tensor identity on the outer sides by \(L,R\).
The [finite-rank tensor identification](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) sends \(x\otimes y\) with bounded legs to \(xP_e y\) and sends \(\Psi_g\) to commutation with \(\rho_g\).
This gives the asserted equality, with the minus sign included in \(T_s\).

Left multiplication by the injective affiliated unit \(L\) preserves the kernel of \(\sigma\), so \(\operatorname{supp}_r u=1-p\).
Right multiplication by \(R\) preserves the affiliated image of \(h\), giving \(\operatorname{supp}_l v=p\).
Both are nonzero by the assumed half rank and scalar pivot elimination; the output consequently has ordinary rank one.
The closed left-translation span of a bounded vector \(x\) is \(L^2(\mathcal N(H))\operatorname{supp}_r x\), by polar decomposition and spectral truncation.
Apply this to \(u,v^*\).
Finally the [two-label small-input exclusion](Yin_C_A0166_v2.md#statement) rules out rank one of the output if either nonzero input has rank one, or if only one label is active.
Thus the two upper bounds on input rank are both attained.

## Assessment history

### Decision two-commutators-with-prescribed-schur-supports

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | The explicit bounded tensor formula gives the original kernel and complementary support with input ranks exactly two. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two inverse layers, two labels and ordinary ranks. |
| argument | [A balance with the specified two labels](#a-balance-with-the-specified-two-labels) | The two Schur equations and splitting at the mixed word. |
| argument | [Bounded coefficients and the two support projections](#bounded-coefficients-and-the-two-support-projections) | The actual positive denominators, supports and ordinary-rank lower bounds. |
| review | [Two commutators with prescribed Schur supports](../audits/reviews/Yin_R_A0213_v1.md#two-commutators-with-prescribed-schur-supports) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-two-commutators-with-prescribed-schur-supports)
