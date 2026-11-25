---
author: Yin
---

# A finite-rank rationality criterion with the subspace determined by the witnesses

## Statement

Let \(G=\langle g_1,\ldots,g_d\rangle\) be a finitely generated discrete group, let \(M=\mathcal N(G)\), \(H=L^2(M,\tau)=\ell^2(G)\), \(U=L^0(M)\), and let \(D_G\) be the division closure of \(\mathbb CG\) in \(U\).
Write \(X_j=\lambda(g_j)\), \(\rho_j\xi=\xi X_j\), and \(P_e\) for the projection onto \(\mathbb C\delta_e\).
Identify bounded left multipliers with their vectors in \(M\delta_e\subset H\) when taking spans.
All finite-rank operators below are bounded and have finite complex rank.

For every \(u\in U\), membership \(u\in D_G\) is equivalent to the existence of \(s,a,b,t\in M\) and finite-rank operators \(T_1,\ldots,T_d\) such that
\[
 s,t\in U^\times,\qquad u=s^{-1}a=bt^{-1},\qquad
 \sum_j[\rho_j,T_j]=sP_e b-aP_e t,                                      \tag{1}
\]
and the following condition holds on the prescribed subspace
\[
 V_0=\mathbb C s\delta_e+\sum_j\operatorname{Ran}T_j .
\]
For every finite-rank \(B\) require
\[
 B(s\delta_e)=0,\quad [B,\rho_j]|_{V_0}=0\ \ (1\le j\le d)
             \quad\Longrightarrow\quad B|_{V_0}=0 .                       \tag{2}
\]
For fixed witnesses, a single matrix injectivity condition is equivalent to (2).
Set \(X_0=1\), choose a basis \(v_1=s\delta_e,v_2,\ldots,v_n\) of \(V_0\), and take a complex basis of the relations \(\sum_{i,j}c_{ij}v_iX_j=0\) for \(0\le j\le d\).
Form a matrix \(K\) with first column the first coordinate vector \(e_1\) and one further column \((\sum_{j=0}^d c_{ij}X_j)_{i=1}^n\) for each basis relation.
Then (2) is equivalent to
\[
                         \ker_{H^n}(KK^*)=0 .                             \tag{3}
\]
The truth of (3) is independent of both basis choices.
The fraction and finite-rank tuple in (1) are the only freely chosen witnesses in the version using (3).
This supplies a simplification for torsion-free groups while leaving open the effect of deleting (3) throughout that class.

## Argument

### The relation matrix of the prescribed subspace

For a local test map \(B\) satisfying the premises of (2), the row \(z_i=Bv_i\) satisfies \(zK=0\).
Conversely \(zK=0\) means \(z_1=0\) and that \(v_iX_j\mapsto z_iX_j\) respects all the relations on these vectors.
It defines a linear map on their finite-dimensional span, which extends by zero on the orthogonal complement to a bounded finite-rank \(B\).
The resulting \(B\) satisfies both premises in (2).
Thus (2) says exactly that right multiplication by \(K\) has zero kernel on \(H^{1\times n}\).
Taking adjoints entrywise and using positivity of \(KK^*\) gives (3) and the asserted independence of the choices. [Relation matrix argument](Yin_C_A0131_v3.md#recovering-the-vectors-in-the-subspace)

If (1) and (2) hold, the [criterion allowing a chosen subspace](Yin_C_A0131_v3.md#statement) applies with \(V=V_0\) and gives \(u\in D_G\).
For the converse fix \(u\in D_G\).
The [affine row construction](Yin_C_A0131_v2.md#constructing-the-finite-rank-operators) supplies one fraction pair and witnesses \(T_j^0\) of (1), together with bounded vectors \(\eta_1,\ldots,\eta_m\) whose span contains their ranges.
The space \(W=\operatorname{span}\{s\delta_e,\eta_1,\ldots,\eta_m\}\) satisfies the local implication (2) with \(W\) in place of \(V_0\). [Local uniqueness on the affine row](Yin_C_A0131_v3.md#a-subspace-obtained-from-a-rational-element)

### An infinite group with a relator in the chosen generators

Use the identification \(\Theta(x\otimes y)\xi=x\tau(y\xi)\) of \(H\otimes_{\mathbb C}H\) with the finite-rank operators.
It takes \(\Psi_j(x\otimes y)=xX_j\otimes y-x\otimes X_j y\) to \([\rho_j,\Theta(x\otimes y)]\). [Finite-rank tensor identification](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
Write group elements for their left translations in tensors.
Choose a shortest nonempty freely reduced relator, inverting it and cyclically rotating as necessary so its first letter is positive.
A shortest such relator is cyclically reduced, since cancellation of opposite end letters would give a shorter relator.
Its path in the labelled Cayley graph is a cycle with distinct vertices up to the final return.

Orient every labelled edge for \(j\) from its positive tail \(q\) to \(h=qg_j\), regardless of the traversal direction, and write \(\epsilon=1\) for forward traversal and \(\epsilon=-1\) for reverse traversal.
Let \(S\) be the set of all these positive tails, so \(e\in S\).
For each \(j\) sum \(\epsilon q\otimes h^{-1}\) over the cycle edges of label \(j\) to obtain \(c_j\).
Applying \(\Psi_j\) gives the stepwise increment of \(p\otimes p^{-1}\) between consecutive path vertices, so \(\sum_j\Psi_j(c_j)=0\).
For each label the positive tails are distinct and hence so are the heads.
Indeed a simple cycle of length at least three does not repeat an edge.
For a cycle of length two, opposite traversals of one labelled oriented edge would be consecutive inverse letters, and two traversals in the same direction have distinct starting vertices.
A length-one loop gives a single term. [Cycle of a relator](Yin_C_A0131_v1.md#the-cycle-of-a-relator)

Write \(k_j^0=\Theta^{-1}(T_j^0)\) and let \(Z\subset H\) be a common finite-dimensional span of their second factors.
There is a finite set \(F_0\subset G\) on which coordinate restriction is injective on \(Z\), since the coordinate functionals span the dual of \(Z\).
Let \(F\) be the finite set of inverse heads \(h^{-1}\) used in all \(c_j\).
Choose \(k_1,\ldots,k_m\in G\) so that the \(Fk_i\) avoid \(F_0\) and are pairwise disjoint.
At each step only finitely many choices are forbidden, and \(G\) is infinite.
Define
\[
 T_j=\Theta\!\left(k_j^0+
       \sum_{i=1}^m\ \sum_{\text{cycle edges }(q,h)\text{ of label }j}
                \epsilon\,\eta_i q\otimes h^{-1}k_i\right).
\]
For each \(i\) the summands added across the labels have zero boundary, by outer multiplication of the cycle by \(\eta_i\) and \(k_i\).
Thus the same fraction pair still satisfies (1).
For a fixed \(j\) the new second factors are distinct group basis vectors and linearly independent modulo \(Z\).
In a finite tensor with independent second factors, the range of its operator is the span of its corresponding first factors, since one can prescribe the values of the finitely many independent linear functionals separately.
Applying this to each \(j\), using a basis for the old second factors, gives
\[
 V_0=W+\operatorname{span}_{\mathbb C}\{\eta_i q:1\le i\le m,\ q\in S\}.
\]
Here the inclusion \(W\subseteq V_0\) uses \(e\in S\), and the old ranges lie in \(W\).

A \(B\) as in (2) vanishes on \(W\), by local uniqueness on \(W\).
For each \(i\) and each cycle edge the tail vector \(\eta_i q\) belongs to \(V_0\), so
\[
                        B(\eta_i h)=B(\eta_i q)X_j .
\]
The shift is invertible, and hence zero values propagate in either traversal direction.
Starting with \(B\eta_i=0\) at \(e\) and following the cycle gives \(B(\eta_iq)=0\) for all \(q\in S\).
This proves (2), including at edges whose head vector lies outside \(V_0\).

### A free marking or a finite group

When the marking has no nonempty freely reduced relator, it is a free basis.
The homogeneous finite-rank boundary is then injective.
Indeed there are bounded coordinate duals \(D_i\) such that \([\rho_j,D_i]=\delta_{ij}P_e\), obtained from the bounded left coordinate duals by the unitary that reverses reduced words. [Free coordinate duals](Yin_C_A0131_v1.md#the-cycle-of-a-relator)
If \(\sum_j[\rho_j,S_j]=0\) for finite-rank \(S_j\), the same identity holds for \(xS_j y\) with arbitrary bounded left multipliers \(x,y\in M\).
Taking the operator trace after multiplying by \(D_i\) and using cyclicity gives \(\operatorname{Tr}(P_e xS_i y)=0\).
The vectors \(y\delta_e\) and \(x^*\delta_e\) each range over a dense subspace, so \(S_i=0\).

For any solution of (1), a test \(B\) in the premises of (2) commutes with \(\rho_j\) on \(\operatorname{Ran}T_j\).
Consequently
\[
     \sum_j [\rho_j,BT_j]=B(sP_e b-aP_e t)=-\Theta(B(a\delta_e)\otimes t).
\]
The multiplication map \(H\otimes_{\mathbb C}H\to U\) annihilates every \(\Psi_j\) by associativity.
Applying it after \(\Theta^{-1}\) gives \(B(a\delta_e)t=0\), so \(B(a\delta_e)=0\) by invertibility of \(t\) in \(U\).
Homogeneous injectivity now gives \(BT_j=0\) for every \(j\), proving (2).

If \(G\) is finite and \(d>0\), the identity on \(H\) has finite rank.
Replace \(T_1^0\) by \(T_1^0+cI\) with \(c\in\mathbb C\) chosen to make it invertible.
The commutator is unchanged and \(V_0=H\).
Any test \(B\) in (2) commutes with the right action of \(G\) and kills \(s\delta_e\).
Its right translates span \(H\), since \(U=M=\mathbb CG\) in this case and left multiplication by \(s\) is invertible.
Thus \(B=0\).
For the empty marking \(G\) is trivial and \(s\delta_e\) already spans \(H\).

## Assessment history

### Decision prescribed-space

| Field | Value |
| --- | --- |
| date | 2026-11-25T08:33 |
| status | proved |
| reason | Homogeneous relator perturbations or homogeneous injectivity on a free marking give the prescribed witness space. The matrix of translation relations converts the local condition into one injectivity test. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Criterion](#statement) | Rationality for all finitely generated discrete groups with a subspace fixed by the witnesses and a basis-independent matrix test. |
| argument | [Proof](#argument) | The relation matrix and the constructions for infinite groups with a relator, free markings and finite groups. |
| dependency | [Earlier criterion](Yin_C_A0131_v3.md#statement) | Sufficiency of an admissible local space and existence of an affine-row space for a rational element. |
| dependency | [Affine row and operators](Yin_C_A0131_v2.md#constructing-the-finite-rank-operators) | Common bounded affine-row realization and finite-rank solution for the same fractions. |
| dependency | [Relator cycles and free markings](Yin_C_A0131_v1.md#the-cycle-of-a-relator) | Oriented tensor cycles and bounded coordinate duals for a free basis. |
| review | [Independent proof review](../audits/reviews/Yin_R_A0165_v5.md#prescribed-witness-space) | All quantifiers, both implications and all marking cases. |

## Current assessment

[Selected decision](#decision-prescribed-space)
