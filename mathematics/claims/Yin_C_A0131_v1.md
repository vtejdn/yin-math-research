---
author: Yin
---

# Finite-rank detection of the regular closure of a group algebra

## Statement

Let \(G=\langle g_1,\ldots,g_d\rangle\) be a finitely generated discrete group, \(H=\ell^2(G)\), \(M=\mathcal N(G)\) with its group trace, and \(U=L^0(M)\).
Write \(X_j=\lambda(g_j)\), let \(\rho(x)\) denote right multiplication by \(x\) on \(H=L^2(M)\), and let \(P_e\) project onto \(\mathbb C\delta_e\).
Inside \(U\), let \(D_G\) be the division closure of \(A=\mathbb CG\) and let \(R_G\) be its \(*\)-regular closure.
The former adjoins two-sided inverses of elements invertible in \(U\), and the latter also allows the relative inverse \(x^{[-1]}\), the inverse between the two supports of \(x\) extended by zero.
Both closures are algebraic.

For every \(u\in U\) the following conditions are equivalent.

1. \(u\in R_G\).
2. \(u\otimes_A1=1\otimes_Au\) in the algebraic bimodule \(U\otimes_A U\).
3. There exist \(s,a,b,t\in M\) with \(s,t\) invertible in \(U\) and \(u=s^{-1}a=bt^{-1}\), and bounded operators \(T_1,\ldots,T_d\) of finite complex rank on \(H\), such that
   \[
                  \sum_{j=1}^d[\rho(X_j),T_j]=sP_e b-aP_e t. \tag{1}
   \]

Consequently (1), with the stated existential quantifiers, detects \(D_G\) for every \(u\) exactly when the kernel projection of each \(x\in D_G\) belongs to \(D_G\).
This condition holds for every torsion-free \(G\) satisfying the strong Atiyah conjecture over \(\mathbb C\).
It covers, for example, the locally indicable groups in the stated finitely generated setting.

If the marked generators satisfy a nontrivial freely reduced relator, the homogeneous equation in (1) has a nonzero finite-rank solution.
There is then no system of operators \(B_i\) defined on \(\mathbb CG\delta_e\) with \([X_j,B_i]=\delta_{ij}P_e\) there.
For a free basis such a system exists and can be chosen bounded.

## Argument

### The equalizer in the affiliated ring

Apply Jaikin-Zapirain's Proposition 6.1 to \(A\subseteq R_G\).
Multiplication identifies \(R_G\otimes_A R_G\) with \(R_G\), so \(r\otimes_A1=1\otimes_A r\) for every \(r\in R_G\), also after mapping the two factors to \(U\).
Conversely, suppose this tensor equality holds for \(u\in U\).
For any unital ring maps \(f,h:U\to B\) that agree on \(R_G\), the biadditive map \((v,w)\mapsto f(v)h(w)\) is \(A\)-balanced.
Applying it to the equality gives \(f(u)=h(u)\).
Thus \(u\) belongs to the dominion of \(R_G\hookrightarrow U\), the subring on which every such pair of maps agrees.
Proposition 4.2 of the same paper identifies this dominion with \(R_G\), since \(R_G\) is von Neumann regular. [JZ19, Propositions 4.2 and 6.1](../audits/literature/JZ19/Yin_U001.md#epic-rank-linearization)

### Balancing and ordinary finite rank

On \(U\otimes_{\mathbb C}U\) put \(\Psi_j(v\otimes w)=vX_j\otimes w-v\otimes X_jw\).
The kernel of the quotient map to \(U\otimes_A U\) is \(\sum_j\operatorname{im}\Psi_j\).
Indeed, balancing for a product follows by telescoping the two factor relations.
The relation for \(X_j^{-1}\) on \(v\otimes w\) is \(-\Psi_j(vX_j^{-1}\otimes X_j^{-1}w)\).
Linearity and group generation therefore give every \(A\)-balancing relation.
In particular, condition 2 means that \(u\otimes1-1\otimes u=\sum_j\Psi_j(k_j)\) for finite algebraic tensors \(k_j\).

Use the finite-trace common denominator property to choose a bounded regular \(s\) clearing \(u\) and all first tensor factors on the left, and a bounded regular \(t\) clearing \(u\) and all second factors on the right.
Write \(a=su,\ b=ut\) and multiply the identity by \(s\) on the outer left and \(t\) on the outer right.
This yields \(a\otimes t-s\otimes b=\sum_j\Psi_j(s k_j t)\), with \(s k_j t\in M\otimes_{\mathbb C}M\).
The common denominator argument and the following finite-rank identification are the ones in [F0001, preliminaries](../manuscripts/Yin/Yin_T_F0001/paper/sections/preliminaries.tex).

The linear bijection \(\Theta:H\otimes_{\mathbb C}H\to\mathcal F(H)\) is given by \(\Theta(v\otimes w)\xi=v\tau(w\xi)\).
It satisfies \(\Theta(v\otimes w)=vP_e w\) for \(v,w\in M\), and \(\Theta\Psi_j=[\rho(X_j),\Theta(\,\cdot\,)]\) on \(H\otimes_{\mathbb C}H\).
Thus \(T_j=-\Theta(s k_j t)\) solve (1).
Conversely, applying \(\Theta^{-1}\) to (1) gives \(s\otimes b-a\otimes t=\sum_j\Psi_j(\Theta^{-1}T_j)\) in \(H\otimes_{\mathbb C}H\).
Include these tensors in \(U\otimes_{\mathbb C}U\), pass to \(U\otimes_A U\), and multiply on the outer sides by \(s^{-1}\) and \(t^{-1}\).
The resulting equality is \(1\otimes_A u=u\otimes_A1\).
This proves all three equivalences, with the sign of (1) as in the [F0001 manuscript](../manuscripts/Yin/Yin_T_F0001/paper/sections/maximal-delta.tex).
It also proves independence of the marked generating set for existence of a certificate with some fraction pair.

### Which rationality is detected

The ring \(D_G\) is stable under adjoints since \(A\) is, and \(D_G\subseteq R_G\) since the relative inverse of a unit is its ordinary inverse.
If \(D_G=R_G\), then \(p_x=1-x^{[-1]}x\), the kernel projection of \(x\), belongs to \(D_G\) for every \(x\in D_G\).
Conversely, suppose all these projections belong to \(D_G\).
The operator \(x^*x+p_x\) is invertible in \(U\), acting as \(x^*x\) on its support and as the identity on its kernel.
On these supports the relative inverse is
\[
                     x^{[-1]}=(x^*x+p_x)^{-1}x^*.
\]
This lies in \(D_G\) by division closure, so repeated adjoining of relative inverses gives \(R_G=D_G\). [JZ19, Propositions 3.2 and 3.4](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)

For torsion-free \(G\), the complex strong Atiyah conjecture is equivalent to \(D_G\) being a division ring.
In this case each nonzero \(x\in D_G\) is an affiliated unit and has \(p_x=0\).
The complex-coefficient theorem for locally indicable groups gives the stated example. [Linnell and Lück, Theorem 2.3(3)](../ledger/Yin_L_A0001_v1.md#formulation-and-algebraic-interface) and [Jaikin-Zapirain and López-Álvarez, Theorem 1.1](../audits/literature/JZLA20/Yin_U001.md#jzla20-u001)

### The cycle of a relator

Choose a shortest nonempty freely reduced relator \(w\) and write \(h_k\in G\) for the value of its first \(k\) letters, with \(h_0=h_n=e\).
Identify each \(h_k\) with its left translation in algebraic tensors.
For its \(k\)-th letter \(g_j\) add \(h_{k-1}\otimes h_k^{-1}\) to \(c_j\).
For \(g_j^{-1}\) add \(-h_k\otimes h_{k-1}^{-1}\) to \(c_j\).
Here each \(c_j\) starts at zero.
Applying \(\Psi_j\) to either contribution gives \(h_k\otimes h_k^{-1}-h_{k-1}\otimes h_{k-1}^{-1}\), so \(\sum_j\Psi_j(c_j)=0\).

The vertices \(h_0,\ldots,h_{n-1}\) are distinct, since a repetition gives a shorter nonempty freely reduced relator.
For \(n\ge3\) each edge of this simple cycle occurs once.
For \(n=2\), opposite contributions to the same labelled oriented edge would be consecutive inverse letters, and for \(n=1\) there is one term.
In every case at least one \(c_j\) is nonzero, since tensor products of distinct group basis vectors are linearly independent.
The operators \(\Theta(c_j)\) give the asserted nonzero homogeneous solution.

If the proposed coordinate duals existed on the group-algebra vectors, expand \([\lambda(w),B_i]\) there by the product rule and \([X_j^{-1},B_i]=-X_j^{-1}[X_j,B_i]X_j^{-1}\).
The result is precisely \(\Theta(c_i)\), since \(\lambda(v)P_e\lambda(h)^{-1}\) maps \(\delta_h\) to \(\delta_v\) and vanishes on the other basis vectors.
The left side vanishes since \(\lambda(w)=1\), a contradiction for a nonzero \(c_i\).
For a free basis the negative of the operator deleting a terminal positive \(g_i\), zero on all other words, supplies \(B_i\) in the displayed sign convention. [MSY23, Proposition 6.3, with the sign checked on the vacuum](../audits/literature/MSY23/Yin_U005.md#msy23-u005)

For instance, for the standard generators of \(\mathbb Z^2\), \(D_G=\mathbb C(z_1,z_2)\) by Fourier transform, since a nonzero Laurent polynomial vanishes on a Haar-null set of the torus.
Equation (1) therefore characterizes ordinary rational functions of two variables among measurable functions modulo almost-everywhere equality.
The relation \(X_1X_2=X_2X_1\) prevents coordinate duals already on group-algebra vectors.
Indeed \([X_2,B_1]=0\) forces \([X_2,[X_1,B_1]]=0\), but \([X_2,P_e]\delta_e=\delta_{g_2}\).
The \(\mathbb Z^2\) cycle was identified in the [earlier comparison with the Atiyah problem](../ledger/Yin_L_A0069_v1.md#what-transfers-from-the-f-tasks).

## Assessment history

### Decision group-algebra-criterion

| Field | Value |
| --- | --- |
| date | 2026-11-25T06:19 |
| status | proved |
| reason | The tensor equalizer and denominator argument identify the class detected by finite rank, and the closed-path calculation verifies the separate obstruction to coordinate duals. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-rank detection of the regular closure, the kernel projection criterion for division closure, the torsion-free strong Atiyah cases and the relator obstruction. |
| argument | [Argument](#argument) | The complete tensor, finite-rank, relative inverse and marked-generator proofs. |
| dependency | [Regular closure](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Propositions 3.2 and 3.4 on relative inverses and regular closure, Proposition 4.2 on the dominion of a regular ring and Proposition 6.1 on multiplication over the original algebra. |
| dependency | [F0001 tensor and fraction calculations](Yin_C_F0068_v1.md#argument) | The finite-rank tensor identification and simultaneous outer denominator clearing in Part A, both valid before any injectivity hypothesis. |
| dependency | [Complex strong Atiyah equivalence](../ledger/Yin_L_A0001_v1.md#formulation-and-algebraic-interface) | Linnell and Lück, Theorem 2.3(3), in the original group von Neumann algebra. |
| dependency | [Locally indicable groups](../audits/literature/JZLA20/Yin_U001.md#jzla20-u001) | The complex-coefficient assertion of Theorem 1.1. |
| dependency | [Free Haar unitaries](../audits/literature/MSY23/Yin_U005.md#msy23-u005) | The signed terminal-deletion computation for a free basis in Proposition 6.3. |
| review | [Self-review](../audits/reviews/Yin_R_A0165_v1.md#group-algebra-criterion) | Whole statement and proof with the declared source interfaces and existential fraction scope. |

## Current assessment

[Selected decision](#decision-group-algebra-criterion)
