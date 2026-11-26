---
author: Yin
---

# Fractions detected by two rank-one commutators

## Statement

Let \(G\) have a finite marking \(S\), put \(M=\mathcal N(G)\), \(U=L^0(M)\), and write \(D_G\) for the division closure of \(\mathbb CG\) in \(U\).
Suppose that every nonidentity element of \(S\) has infinite order, as holds for torsion-free \(G\).
In the [finite-rank commutator equation](Yin_C_A0131_v1.md#statement) for \(u\in U\), measure a solution by \(k=\sum_{g\in S}\operatorname{rank}_{\mathbb C} T_g\).

For \(b=0,1,2\), there is a solution with \(k\le b\) if and only if one can choose at most \(b\) nonidentity marked elements \(g_i\), with repetitions allowed, and nonconstant scalar fractional linear functions \(F_i\) such that
\[
 u=d^{-1}n\quad\text{or}\quad u=nd^{-1},\qquad
 d,n\in\operatorname{span}_{\mathbb C}\{1,F_i(g_i):i\},\qquad d\in U^\times .
 \tag{1}
\]
In particular every such \(u\) belongs to \(D_G\).
At \(b=1\) the nonscalar elements obtained are exactly the fractional linear functions of one marked element.

Suppose that \(u\notin D_G\) has a solution with \(k=3\).
It must use three nonidentity labels \(g_1,g_2,g_3\), distinct up to inversion, each with a rank-one operator.
There are nonconstant scalar fractional linear functions \(F_i\) such that all three differences \(F_i(g_i)-F_j(g_j)\), \(i<j\), fail to be affiliated units.
Consequently each pair gives a nonzero element supported on at most the four sites \(1,g_i,g_j,g_i g_j\) with a nonzero regular Hilbert-space kernel in the subgroup \(\langle g_i,g_j\rangle\).
When \(G\) is torsion-free, every one of these pair subgroups must have finite abelianization.
In particular the scalar analytic zero-divisor conjecture for \(G\) suffices for every solution of total rank at most three to give \(u\in D_G\).
The argument leaves open the existence of a three-label example under torsion-freeness alone.

## Argument

### Endpoint spaces

For \(l,r\in U\) put \(\Psi_g(l\otimes r)=lg\otimes r-l\otimes gr\) and \(\delta u=u\otimes1-1\otimes u\) in \(U\otimes_{\mathbb C}U\).
After discarding the identity label and clearing or restoring the two outer denominators, a solution of total rank at most \(b\) is equivalent to an identity
\[
                  \delta u=\sum_{i=1}^k\Psi_{g_i}(l_i\otimes r_i),\qquad k\le b.
 \tag{2}
\]
Indeed tensor rank is ordinary operator rank under the finite-rank identification, and multiplication by the two affiliated units on the respective tensor factors preserves it. [Denominator and tensor identities](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank)
Use only nonzero simple tensors and take minimal tensor decompositions within each label.
For a nonidentity label \(g\), every nonzero affine polynomial in \(g\) is an affiliated unit, since on the cosets of \(\langle g\rangle\) the regular action is a sum of bilateral shifts. [Cyclic calculation](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions)
In particular each of
\[
 E_i=\operatorname{span}_{\mathbb C}\{l_i,l_i g_i\},
 \qquad H_i=\operatorname{span}_{\mathbb C}\{r_i,g_i r_i\}
\]
is a plane.
Write \(a=\dim_{\mathbb C}\sum_i E_i\) and \(b'=\dim_{\mathbb C}\sum_i H_i\).
Factoring (2) through its \(2k\) signed simple tensors gives \(\operatorname{rank}_{\mathbb C}(\delta u)\ge a+b'-2k\). [Endpoint dimension inequality](Yin_C_A0166_v2.md#endpoint-dimensions-and-a-cyclic-chain)
For nonscalar \(u\) this tensor has rank two and both its factor spaces equal \(\operatorname{span}_{\mathbb C}\{1,u\}\).
Hence that span lies in each of \(\sum_i E_i\) and \(\sum_i H_i\).

If \(\sum_i E_i\subset wD_G\) for some \(w\in U\), then \(1=wx\) for some \(x\in D_G\).
The finite affiliated ring is directly finite, so \(w=x^{-1}\in D_G\), and consequently \(u\in D_G\).
The same argument applies to \(\sum_i H_i\subset D_Gw\).

### The exact two-term fractions

For \(k=0\) equation (2) gives precisely the scalars.
For \(k=1\) and nonscalar \(u\), its first factor space equals \(E_1\), so \(1=l_1 P(g_1)\) and \(u=l_1 Q(g_1)\) for independent affine polynomials \(P,Q\).
Thus \(u=P(g_1)^{-1}Q(g_1)\).

For \(k=2\) and nonscalar \(u\), the dimension inequality gives \(\min(a,b')\le3\).
Suppose first that \(a\le3\).
There is a nonzero \(w\in E_1\cap E_2\), and \(w=l_iP_i(g_i)\) for a nonzero affine polynomial \(P_i\) on each plane.
Choose an affine polynomial \(Q_i\) independent of \(P_i\), and write \(F_i=Q_i/P_i\).
Then
\[
           E_1+E_2=wW,\qquad W=\operatorname{span}_{\mathbb C}\{1,F_1(g_1),F_2(g_2)\}.
\]
Since \(1,u\in wW\), write \(1=wd,\ u=wn\) with \(d,n\in W\).
Direct finiteness gives \(u=d^{-1}n\).
If \(b'\le3\), write a nonzero common point \(w\) of \(H_1,H_2\) as \(P_i(g_i)r_i\).
This gives \(H_1+H_2=Ww\) for that common point \(w\), and yields \(u=nd^{-1}\).

Conversely, for \(F_i(X)=(a_i+b_i X)/(c_i+e_i X)\) put \(v_i=(c_i+e_i g_i)^{-1}\).
The scalar divided difference gives
\[
                 \delta F_i(g_i)=(b_i c_i-a_i e_i)\Psi_{g_i}(v_i\otimes v_i).
\]
This identity follows by multiplying the two tensor factors by their respective denominators.
Write \(n=n_0+\sum n_i F_i(g_i)\) and \(d=d_0+\sum d_iF_i(g_i)\) with complex coefficients.
For \(u=d^{-1}n\) one has \(\delta u=d^{-1}(\delta n-(\delta d)u)\), where products with tensors act on the outer factors.
Thus each \(i\) contributes one boundary, with first factor \(d^{-1}v_i\) and second factor \((b_i c_i-a_i e_i)v_i(n_i-d_i u)\).
For \(u=nd^{-1}\) the identity is \(\delta u=(\delta n-u(\delta d))d^{-1}\), giving the same bound on the number of simple tensors.
Restoring the denominators in (2) proves the converse, including repeated labels.

### The obstruction at total rank three

Assume that \(u\notin D_G\) in (2) with \(k=3\).
First suppose \(a\le4\) and that \(E_1,E_2\) meet in a nonzero \(w\), relabeling the planes when needed.
As above, their sum lies in \(wD_G\).
If \(E_3\) meets their sum in a nonzero point \(l_3P(g_3)=wx\) with \(x\in D_G\), then \(l_3=wxP(g_3)^{-1}\), putting all three planes in \(wD_G\).
If the intersection is zero, quotient the first factor of (2) by \(E_1+E_2\).
The image of \(E_3\) still has dimension two, so the resulting tensor has rank two and its second factor space equals \(H_3\).
That space lies in \(\operatorname{span}_{\mathbb C}\{1,u\}\) by the left side of (2), and equality follows by dimension.
The one-plane calculation now puts \(u\) in \(\mathbb C(g_3)\).
Both alternatives contradict the assumption.
The right-hand argument interchanges the two factors and uses multiplication by coefficients on the left.

Any two planes in dimension at most three meet.
Hence \(a,b'\ge4\), and the endpoint inequality gives \(a=b'=4\).
On either side every two of its three planes are complementary.
Project a basis \(w_3,z_3\) of \(E_3\) onto the two summands of \(E_1\oplus E_2\), writing \(w_3=w_1+w_2\) and \(z_3=z_1+z_2\).
Both projections restrict to isomorphisms on \(E_3\), so \(w_i,z_i\) form a basis of \(E_i\).
Each such basis satisfies \(z_i=w_i F_i(g_i)\) for a nonconstant fractional linear function \(F_i\), by expressing the two vectors as \(l_i\) times independent affine polynomials.
Abbreviate \(f_i=F_i(g_i)\).
The two basis equations imply
\[
                    w_1(f_1-f_3)+w_2(f_2-f_3)=0 .
\]
If either displayed difference is a unit in \(U\), its inverse is in \(D_G\).
One of \(w_1,w_2\) then belongs to the other times \(D_G\), and their sum \(w_3\) does as well.
This puts every \(E_i=\operatorname{span}\{w_i,w_i f_i\}\) in the same \(wD_G\).
If \(f_1-f_2\) is a unit, the identity \(w_1(f_1-f_2)=w_3(f_3-f_2)\) gives the same contradiction.

It remains to show that the three labels are distinct up to inversion.
Two terms with inverse labels can first be oriented alike by
\(\Psi_{g^{-1}}(l\otimes r)=-\Psi_g(lg^{-1}\otimes g^{-1}r)\).
If combining same-label tensors decreases \(k\), the two-term result already applies.
Otherwise suppose \(g_1=g_2=g\).
Identify \(E_i\), for \(i=1,2\), with the space of affine polynomials by \(P\mapsto l_iP(g)\).
Complementarity makes \(E_3\) the graph of an invertible linear map between these copies of \(\mathbb C^2\).
Take a nonzero eigenvector \(P\) with eigenvalue \(\lambda\).
Then \((l_1+\lambda l_2)P(g)\) is a nonzero point of \(E_3\).
Replace the first two input tensors by
\[
          (l_1+\lambda l_2)\otimes r_1,\qquad
          l_2\otimes(r_2-\lambda r_1).
\]
They give the same boundary since they carry the same label, and minimality gives two nonzero tensors.
The new first endpoint span still has dimension four, and the first and third planes now meet, which has already been excluded.

Finally write \(F_i=N_i/D_i\) with independent affine polynomials in numerator and denominator.
Clearing \(f_i-f_j\) on the left by \(D_i(g_i)\) and on the right by \(D_j(g_j)\) gives the group-ring element
\[
                 N_i(g_i)D_j(g_j)-D_i(g_i)N_j(g_j).
\]
The scalar coefficient tensor \(N_i\otimes D_j-D_i\otimes N_j\) is nonzero by independence, and its four monomials correspond to distinct group elements \(1,g_i,g_j,g_i g_j\).
Thus the element is nonzero.
Its two clearing factors are affiliated units, so the element is a nonunit and has a nonzero kernel on \(\ell^2(G)\).
The restriction of the regular representation to the pair subgroup is a direct sum of its regular representation, which puts the same kernel obstruction in that subgroup.

Suppose now that \(G\) is torsion-free and that a pair subgroup admits a nonzero character to \(\mathbb Z\).
Write \(a_0,b_0\) for the heights of its two generators, with at least one nonzero.
Each value in the list \(0,a_0,b_0,a_0+b_0\) occurs at most twice.
Translate the lowest nonempty layer of the four-site element to height zero.
Its coefficient is a group monomial or a nonzero binomial in the kernel of the character.
Either coefficient is injective, since any ratio of distinct group elements in the binomial has infinite order.
The [injective extreme-coefficient criterion](../ledger/Yin_L_A0062_v1.md#one-injective-extreme-coefficient-a-bounded-window-proof) makes the entire element injective, contrary to its construction.
The pair subgroup is finitely generated, so the absence of a nonzero character to \(\mathbb Z\) means that its abelianization is finite.

## Assessment history

### Decision low-witness-ranks

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:01 |
| status | proved |
| reason | Endpoint spaces give fractions at total rank two and force singular four-site group-ring elements at rank three. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The exact two-term fractions and the necessary pair obstructions at total rank three. |
| argument | [Argument](#argument) | Both fraction identities, endpoint intersections and the support and heights of each singular scalar. |
| dependency | [Tensor identity](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) | Finite-rank witnesses and common denominators. |
| dependency | [Cyclic calculation](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | Invertibility at an infinite-order generator. |
| dependency | [Endpoint dimensions](Yin_C_A0166_v2.md#endpoint-dimensions-and-a-cyclic-chain) | Rank inequality for sums of boundaries. |
| dependency | [Extreme coefficient](../ledger/Yin_L_A0062_v1.md#one-injective-extreme-coefficient-a-bounded-window-proof) | Injectivity from the first occupied height. |
| review | [Low witness ranks](../audits/reviews/Yin_R_A0180_v1.md#low-witness-ranks) | Independent review of the statement and argument. |

## Current assessment

[Selected decision](#decision-low-witness-ranks)
