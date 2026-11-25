---
author: Yin
---

# The dimension of the joint range in the finite-rank commutator equation

## Statement

Let \(G\) be a finitely generated discrete group, \(A=\mathbb CG\), \(M=\mathcal N(G)\), \(H=L^2(M,\tau)\), and \(U=L^0(M)\).
Let \(D\) be the division closure of \(A\) in \(U\).
For a finite marking \(S\) of \(G\), identify each \(g\in S\) with its left multiplier, let \(\rho_g\) be right multiplication by \(g\) on \(H\), and let \(P_e\) project onto the span of \(\delta_e=1\).
For \(u\in U\), consider the [finite-rank equation](Yin_C_A0131_v1.md#statement)
\[
  u=s^{-1}a=bt^{-1},\qquad
  \sum_{g\in S}[\rho_g,T_g]=sP_e b-aP_e t ,                         \tag{1}
\]
where \(s,a,b,t\in M\), \(s,t\) are affiliated units, and the \(T_g\) are bounded operators of finite complex rank.
Fix \(k\ge1\).
The following conditions on \(G\) are equivalent.

1. For every matrix \(X\) over \(A\) with \(k\) columns, the orthogonal projection onto \(\ker X\) has entries in \(D\).
2. For every finite marking, any \(u\) admitting witnesses for (1) with \(\dim_{\mathbb C}(\mathbb C s\delta_e+\sum_g\operatorname{Ran}T_g)\le k+1\) belongs to \(D\).
3. For every finite symmetric marking, any positive contraction \(u\in M\) admitting the following witnesses for (1) belongs to \(D\).
   The denominators are \(s=t=c\) for a positive injective contraction \(c\), and \(T_{g^{-1}}=T_g^*\).
   One complex subspace of \(H\) of dimension at most \(k+1\) contains \(c\delta_e\) and all ranges of the \(T_g\) and \(T_g^*\).

In particular, the two-dimensional test in condition 3 is equivalent to rationality of the kernel projections of all group-ring scalars.
Requiring condition 3 at every finite dimension is equivalent to [complete deletion of the local commutation condition](../tasks/Yin_T_A0003_v3.md#contract) for this group.
For a fixed marking, (1) with \(\mathbb C s\delta_e+\sum_g\operatorname{Ran}T_g\) of dimension one holds precisely for \(u\in\operatorname{span}_{\mathbb C}(\{1\}\cup S)\).

For the unrestricted question, fix any one finite marking, and write \(\partial T=\sum_{g\in S}[\rho_g,T_g]\).
Let \(R\) be the \(*\)-regular closure of \(A\) in \(U\), and fix a projection \(0<p<1\) in \(M\).
Then \(p\in R\) if and only if there exist positive \(a,b\in M\) with support projections \(p,1-p\), respectively, for which the single rank-one operator \(bP_e a\) equals \(\partial T\) for a finite-rank tuple.
Equivalently, the nontrivial projections of \(R\) can be recovered by choosing only the tuple.
Whenever \(F=\partial T\) has complex rank one, the closed spans of the left \(G\)-translates of \(\operatorname{Ran}F\) and \(\operatorname{Ran}F^*\) are orthogonal.
If together they span \(H\), the projection onto the latter space is right multiplication by a nontrivial \(p\in R\), and every such \(p\) occurs.
Thus complete deletion for \(G\) is equivalent to this right projection belonging to the right copy of \(D\) for every such tuple on the fixed marking.

One can dispense with joint cyclicity by asking for a separating projection.
Complete deletion holds if and only if for every rank-one \(F=\partial T\) there is a projection \(e\in D\) such that right multiplication by \(e\) annihilates \(\operatorname{Ran}F\) and fixes \(\operatorname{Ran}F^*\).
The stronger assertion that \(\operatorname{im}\partial\) contains no operator of complex rank one is equivalent to \(D\) being a division ring.
For torsion-free \(G\) this rank-one exclusion is equivalent to the complex strong Atiyah conjecture for \(G\).

## Argument

### Recovering a finite space from the ranges

Identify \(H\otimes_{\mathbb C}H\) with the finite-rank operators by \(\Theta(v\otimes w)\xi=v\tau(w\xi)\).
The adjoint sends \(v\otimes w\) to \(w^*\otimes v^*\).
The commutator with \(\rho_g\) corresponds to \(\Psi_g(v\otimes w)=vg\otimes w-v\otimes gw\). [Finite-rank tensor identities](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
In a minimal tensor decomposition of \(\Theta^{-1}(T_g)\) the second factors are linearly independent, so the first factors span \(\operatorname{Ran}T_g\).
Normalize (1) by multiplying its tensor identity on the outer left by \(s^{-1}\) and on the outer right by \(t^{-1}\).
This gives \(u\otimes 1-1\otimes u=\sum_g\Psi_g(b_g)\) in \(U\otimes_{\mathbb C}U\), where the first factors of \(b_g\) lie in \(s^{-1}\operatorname{Ran}T_g\).

Under condition 2's dimension bound, the complex space
\[
             V=\operatorname{span}_{\mathbb C}\{1,u\}
                       +s^{-1}\sum_g\operatorname{Ran}T_g
\]
has dimension at most \(k+2\), since left multiplication by \(s^{-1}\) is injective and sends \(s\) to \(1\).
Take a linear map \(\varphi:V+\sum_g Vg\to U\) with \(\varphi(1)=0\) and \(\varphi(vg)=\varphi(v)g\) for \(v\in V\).
Apply it to the first leg of the normalized identity and multiply the resulting tensor factors.
Every balance cancels, leaving \(\varphi(u)=0\).
The [criterion with at most \(k\) auxiliary vectors](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) now gives \(u\in D\) under condition 1.
This proves \(1\Rightarrow2\), and restricting the witnesses gives \(2\Rightarrow3\).

### Commutators for a compression of the kernel projection

Let \(X\) have \(k\) columns and put \(B=X^*X\), \(Q=B^{[-1]}\), and \(p=I-QB\).
The relative inverse \(Q\) is selfadjoint, commutes with \(B\), and inverts \(B\) on its support, so \(p=p_{\ker X}\).
For a complex unit column \(\xi\) of length \(k\), set
\[
                u=\xi^*p\xi,\qquad w=Q\xi,\qquad y=w^*=\xi^*Q .
\]
Then \(u\) is a positive contraction, \(yB^2=\xi^*B\), \(B^2w=B\xi\), and \(1-u=yB\xi=\xi^*Bw\).
For a row \(l\), a square matrix \(C\) and a column \(r\) of compatible sizes define
\[
       \Delta(l,C,r)=\sum_{i,j}\big(l_i C_{ij}\otimes r_j
                                       -l_i\otimes C_{ij}r_j\big).
\]
In \(U\otimes_{\mathbb C}U\) one has
\[
 u\otimes1-1\otimes u
       =-\Delta(y,B,\xi)+\Delta(y,B^2,w)-\Delta(\xi^*,B,w).       \tag{2}
\]
Indeed the six terms, contracted over the scalar coordinates of \(\xi\) where applicable, are
\[
 -(yB\xi)\otimes1+\sum_i y_i\otimes(B\xi)_i
 +\sum_j(yB^2)_j\otimes w_j-\sum_i y_i\otimes(B^2w)_i
 -\sum_j(\xi^*B)_j\otimes w_j+1\otimes(\xi^*Bw).
\]
The two identities involving \(B^2\) cancel the four middle sums.

Enlarge a finite generating set to a finite symmetric marking containing the nonidentity group elements supporting \(B,B^2\).
Write \(B=\sum_g B_g g\), \(B^2=\sum_g C_g g\) with scalar coefficient matrices.
The right side of (2) equals \(\sum_{g\in S}\Psi_g(b_g)\), where
\[
 b_g=-\sum_i (B_g\xi)_i y_i\otimes1
        +\sum_{i,j}(C_g)_{ij}y_i\otimes w_j
        -\sum_j(\xi^*B_g)_j 1\otimes w_j .
\]
Terms from the group identity contribute zero to (2).
The conjugate-linear map \(v\otimes w'\mapsto(w')^*\otimes v^*\) sends \(b_g\) to \(b_{g^{-1}}\), since \(B_{g^{-1}}=B_g^*\), \(C_{g^{-1}}=C_g^*\), and \(y_i=w_i^*\).

Choose \(c=(1+\sum_i w_i^*w_i)^{-1/2}\), a positive injective contraction in \(M\).
Each \(w_i c\) belongs to \(M\) because \(c w_i^*w_i c\le1\), and \(c y_i=(w_i c)^*\).
Multiply (2) by \(c\) on the two outer sides and set \(T_g=-\Theta(c b_g c)\), where these outer products put both tensor factors in \(M\).
With \(s=t=c\), \(a=cu\) and \(b=uc\), these operators satisfy precisely (1), including its sign.
They satisfy \(T_{g^{-1}}=T_g^*\), and the ranges of every \(T_g\) and every \(T_g^*\) lie in \(\operatorname{span}_{\mathbb C}\{c,c y_1,\ldots,c y_k\}\subset H\).
Condition 3 therefore gives \(\xi^*p\xi\in D\) for every complex unit column \(\xi\).
Polarization of this \(M\)-valued Hermitian form recovers all entries of \(p\) by complex linear combinations, proving \(3\Rightarrow1\).

For \(k=1\), a column \(X\) has \(\ker X=\ker(X^*X)\), and every scalar is itself a one-column matrix.
For arbitrary \(k\), the [matrix-size equivalence](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) identifies the conjunction of condition 1 over all \(k\) with complete deletion.
Thus the dimension bound is on a single subspace supporting all the commutators' finite-rank witnesses, even when the number of marked group elements used to encode the matrix grows.

### The one-dimensional boundary

If every range lies in \(\mathbb C s\delta_e\), the normalized tensors above have the form \(b_g=1\otimes r_g\) for \(r_g\in U\).
Apply \(\operatorname{id}\otimes\varphi\), for a complex linear functional on \(U\) with \(\varphi(1)=1\), to \(u\otimes1-1\otimes u=\sum_g(g\otimes r_g-1\otimes gr_g)\).
The result puts \(u\) in \(\operatorname{span}_{\mathbb C}(\{1\}\cup S)\).
Conversely for \(u=\lambda_0+\sum_{g\in S}\lambda_g g\), take \(s=t=1\), \(a=b=u\) and \(T_g=-\lambda_g P_e\).
Their commutator sum gives (1), and the prescribed joint space is \(\mathbb C\delta_e\).

### Rank-one commutator sums on one fixed marking

For \(p\in R\) the [balanced tensor characterization](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) gives \(p\otimes1-1\otimes p=\sum_{g\in S}\Psi_g(d_g)\) in the algebraic tensor product over \(\mathbb C\).
Write \(q=1-p\) and let \(J\subset U\) consist of the adjoints of all first factors and all second factors in finite decompositions of the \(d_g\).
Put
\[
 c=\left(1+\sum_{v\in J}(p v^*v p+q v^*v q)\right)^{-1/2}.
\]
This positive injective contraction commutes with \(p\).
Since \(c p v^*v p c\le 1\) and \(c q v^*v q c\le1\), both \(vp c\) and \(vq c\) are bounded, hence so is \(vc\).
Clearing (on the outer sides) by \(c\) therefore gives finite-rank operators \(-\Theta(cd_g c)\) whose commutator sum is \([cP_e c,p]\).
Left multiplication by \(q\) and right composition with left multiplication by \(p\) commute past the right translations in this sum.
The compressed sum equals \(q c P_e c p=bP_e a\) with \(a=cp\), \(b=cq\), which are positive with supports exactly \(p,q\).

Conversely, take a rank-one boundary \(F=\partial T\) and choose \(\xi,\eta\in H\) such that \(F=\Theta(\xi\otimes\eta^*)\).
Let \(r,s\in M\) be the right supports of \(\xi,\eta\) as affiliated operators.
For a vector \(v\in H\) with right support \(h\), the closed left-translation span of \(v\) is \(Hh\).
Indeed its orthogonal projection is in the commutant of the left regular representation, and the smallest right projection fixing \(v\) is right multiplication by \(h\).
For every left translation \(\lambda(x)\), the ordinary operator trace of \(\lambda(x)F\) is zero by cyclicity on finite-rank operators and commutation of left with right translations.
This trace equals \(\langle\lambda(x)\xi,\eta\rangle\) with the inner product linear in its first argument.
Thus \(Hr\) and \(Hs\) are orthogonal, and joint cyclicity of the two ranges means exactly \(r+s=1\).

The finite-rank tensor identity gives \(\xi\otimes_A\eta^*=0\) in \(U\otimes_A U\).
Multiply on the outer sides by \(\xi^{[-1]}\) and \((\eta^*)^{[-1]}\) to obtain \(r\otimes_A s=0\).
The conjugate-linear flip \(v\otimes_A w\mapsto w^*\otimes_A v^*\) is well defined because \(A=A^*\), giving \(s\otimes_A r=0\) as well.
If \(r+s=1\), then \(s\otimes_A1=s\otimes_A s=1\otimes_A s\), so \(s\in R\) by the [equalizer theorem](Yin_C_A0131_v1.md#the-equalizer-in-the-affiliated-ring).
For the particular boundary \(bP_e a\) the two right supports are \(q,p\), proving the positive-factor converse and realizing both complementary cyclic subspaces.
Finally, \(D\subseteq R\), and \(D=R\) if all projections of \(R\) belong to \(D\), since these include \(p_{\ker x}\) for every \(x\in D\). [Scalar kernel projection criterion](Yin_C_A0131_v1.md#which-rationality-is-detected)

### Separating the ranges and excluding rank one

Let \(F=\partial T\) have rank one and let \(r,s\) be the right supports of its two directions as above.
The relation \(r\otimes_A s=0\) gives \(r\otimes_R s=0\) in \(U\otimes_R U\).
Since \(R\) is von Neumann regular, every left \(R\)-module is flat. [Flatness over a regular ring](../ledger/Yin_L_A0077_v1.md#the-obstruction-for-one-principal-right-ideal)
In particular, tensoring the inclusion of right modules \(rR\subseteq U\) with the left module \(U\) remains injective, so \(r\otimes_R s=0\) already in \(rR\otimes_R U\).
Let \(I=\{a\in R:ra=0\}\).
The map \(a\mapsto ra\) identifies \(R/I\) with \(rR\), and \((R/I)\otimes_R U\cong U/IU\) sends the tensor in question to the class of \(s\).
Thus \(s=\sum_i a_i z_i\) for finitely many \(a_i\in I\), \(z_i\in U\).
The left support \(e\) of \(\sum_i a_i a_i^*\) belongs to \(R\) by relative inversion and is the join of the left supports of the \(a_i\).
Consequently \(re=0\) and \(es=s\).
Right multiplication by \(e\) therefore kills \(Hr\) and fixes \(Hs\).
This always supplies a separator in \(R\), hence one in \(D\) under complete deletion.
Conversely, for the positive-factor boundary associated to \(0<p<1\) in \(R\), the conditions on a separator are \((1-p)e=0\) and \(pe=p\).
They force \(e=p\), so rational separation for every rank-one boundary gives all projections of \(R\) in \(D\).

If \(D\) is a division ring, a rank-one boundary would give \(\xi\otimes_D\eta^*=0\) in \(U\otimes_D U\) by changing the balancing ring from \(A\) to \(D\).
Both factors are nonzero vectors in their respective right and left vector spaces over \(D\).
Extending each to a basis gives coordinate functionals taking it to one, so their elementary tensor cannot vanish.
If \(D\) is not a division ring, there is a nonzero \(x\in D\) without an inverse in \(D\).
Division closure implies that \(x\) is not an affiliated unit, and finite trace then gives \(0<p_{\ker x}<1\).
This projection lies in \(R\), and the positive-factor construction produces a rank-one boundary on the fixed marking.
For torsion-free groups the [division-ring characterization](Yin_C_A0131_v1.md#which-rationality-is-detected) identifies the two cases with the validity or failure of the complex strong Atiyah conjecture.

## Assessment history

### Decision rank-one-separation

| Field | Value |
| --- | --- |
| date | 2026-11-25T12:55 |
| status | proved |
| reason | Balanced tensors and flatness give a separator for each rank-one commutator boundary in the regular closure, and complementary cyclic ranges force its value. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The dimension of joint witness ranges, rational separation of rank-one boundaries, and the division-ring characterization. |
| argument | [Argument](#argument) | The bounded commutator construction, the cyclic range supports, and separation by a projection in the regular closure. |
| dependency | [Matrix-size criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) | The finite-dimensional vanishing test at each column count. |
| dependency | [Tensor identities](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) | Balancing over the group algebra and the finite-rank operator equation. |
| dependency | [Kernel projections](Yin_C_A0131_v1.md#which-rationality-is-detected) | The regularity and division-ring criteria. |
| dependency | [Flatness](../ledger/Yin_L_A0077_v1.md#the-obstruction-for-one-principal-right-ideal) | Tensor exactness over a regular ring. |
| review | [Rank-one separation](../audits/reviews/Yin_R_A0172_v1.md#rank-one-separation) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-rank-one-separation)
