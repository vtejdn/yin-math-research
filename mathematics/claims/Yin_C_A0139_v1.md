---
author: Yin
---

# Eliminating a block of group-ring columns by finite relations

## Statement

Let \(G\) be a countable discrete group, \(A=\mathbb CG\), \(U=L^0(\mathcal N(G))\), and \(D=\operatorname{Div}_U(A)\).
Group-ring matrices act by left convolution on columns, and \(p_{\ker X}\) denotes the orthogonal projection onto the Hilbert-space kernel.
Suppose \(B\in M_{m,r}(A)\) admits a finite matrix \(Z\in M_{s,m}(A)\) with
\[
                  ZB=0,\qquad \ker Z=\overline{\operatorname{ran}B}.
\]
Then for every \(C\in M_{m,q}(A)\),
\[
      p_{\ker[B\ C]}\in M_{r+q}(D)
      \quad\Longleftrightarrow\quad
      p_{\ker(ZC)}\in M_q(D).
\]
In particular, when \(C=w\) is a single column, the only projection to test is the kernel projection of the group-ring scalar \(w^*Z^*Zw\).

For a finite presentation \(G=\langle g_1,\ldots,g_d\mid R_1,\ldots,R_t\rangle\), let \(B=\partial_1^*\), where \(\partial_1=[g_1-1,\ldots,g_d-1]\).
Such a \(Z\) exists for this column exactly when \(b^{(2)}_1(G)=0\).
In that case one can take \(Z=\partial_2^*\) for the cellular Fox matrix of the presentation, so that the scalar to test for \([B\ w]\) is \(w^*\partial_2\partial_2^*w\).

## Argument

### Block elimination

Set \(H=BB^*+Z^*Z\).
The decomposition into \(\overline{\operatorname{ran}B}\) and its orthogonal complement reduces both summands.
On the first summand \(BB^*\) is injective and \(Z^*Z\) vanishes, while on the second \(Z^*Z\) is injective and \(BB^*\) vanishes.
Hence \(H\) is an affiliated unit, and its inverse has entries in \(D\) by [scalar Gram elimination](Yin_C_A0132_v1.md#argument).
By polar decomposition on these two summands, \(J=B^*H^{-1}\) is the affiliated Moore–Penrose inverse of \(B\).
In particular \(BJ\) projects onto \(\ker Z\), and \(1-JB=p_{\ker B}\) has entries in \(D\).

For a bounded matrix \(X\) with \(n\) columns, its kernel on affiliated columns is \(p_{\ker X}U^n\), by polar decomposition.
For \((u,v)\in U^r\oplus U^q\) the equation \(Bu+Cv=0\) is equivalent to
\[
                   B(u+JCv)=0,\qquad ZCv=0.
\]
Indeed the original equation implies \(ZCv=0\), and the latter identity gives \(BJCv=Cv\) because \(BJ=p_{\ker Z}\).
Thus the invertible change of variables \(S(u,v)=(u+JCv,v)\), with \(S,S^{-1}\) over \(D\), carries the affiliated kernel of \([B\ C]\) onto that of \(\operatorname{diag}(B,ZC)\).

To see that this change preserves rationality of the orthogonal projection, let \(P\in M_n(D)\) be any orthogonal projection and \(L\in\operatorname{GL}_n(D)\).
The orthogonal projection onto the affiliated column module \(LPU^n\) is
\[
        LP\big(PL^*LP+1-P\big)^{-1}PL^* .
\]
The denominator is an affiliated unit since \(L\) is injective on \(PU^n\) and the complementary block is the identity.
The displayed matrix is selfadjoint and idempotent, fixes \(LP\), and has image in \(LPU^n\).
Scalar Gram elimination gives its entries in \(D\).
Applying this observation to \(S\) and \(S^{-1}\) proves the equivalence, since the projection for the diagonal kernel has blocks \(1-JB\) and \(p_{\ker(ZC)}\).
For one column, \(Zw\) and \((Zw)^*Zw\) have the same Hilbert-space kernel.

### The presentation boundary

Use the cellular chains of the universal cover of the presentation complex as free right \(A\)-modules, with the indicated \(\partial_1\) and with \(\partial_2\in M_{d,t}(A)\) the boundary of its lifted relator cells.
The universal cover is simply connected, so \(\ker_A\partial_1=\operatorname{im}_A\partial_2\).
Attaching cells of dimensions at least three to the presentation complex gives a classifying space with the same first two differentials.
Consequently \(b^{(2)}_1(G)\) is the von Neumann dimension of \(\ker\partial_1\ominus\overline{\operatorname{ran}\partial_2}\) on Hilbert-space columns.
Faithfulness of the trace shows that this dimension vanishes precisely when \(\overline{\operatorname{ran}\partial_2}=\ker\partial_1\).
Taking orthogonal complements then gives \(\ker\partial_2^*=\overline{\operatorname{ran}\partial_1^*}\).

Conversely, if any finite group-ring matrix \(Z\) satisfies \(Z\partial_1^*=0\), its adjoint columns belong to \(\ker_A\partial_1\).
Algebraic exactness gives a group-ring matrix \(Y\) with \(Z^*=\partial_2Y\).
If also \(\ker Z=\overline{\operatorname{ran}\partial_1^*}\), then
\[
   \ker\partial_1=\overline{\operatorname{ran}Z^*}
   \ \subseteq\ \overline{\operatorname{ran}\partial_2}
   \ \subseteq\ \ker\partial_1 .
\]
This forces \(b^{(2)}_1(G)=0\) and proves necessity for every choice of the finite relations.

## Assessment history

### Decision finite-block-elimination

| Field | Value |
| --- | --- |
| date | 2026-11-25T10:14 |
| status | proved |
| reason | A complete set of finite left relations supplies a rational inverse between supports and a shear eliminating the specified input columns. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Block reduction, the one-column residual and the exact first Betti number test for the presentation boundary. |
| argument | [Argument](#argument) | The positive Gram denominator, the change of kernel variables and the cellular chain argument. |
| dependency | [Matrix inverse closure](Yin_C_A0132_v1.md#argument) | Scalar rational inversion of an affiliated-unit matrix over the division closure. |
| review | [Elimination of columns](../audits/reviews/Yin_R_A0168_v1.md#elimination-of-columns) | Whole statement and proof at the scope of the recorded independent review. |

## Current assessment

[Selected decision](#decision-finite-block-elimination)
