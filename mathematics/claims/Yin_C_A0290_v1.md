---
author: Yin
---

# The two cyclic factors of the middle transfer detect unmatched pole orders

## Statement

Suppose that \(H=\langle s,t\rangle\) is torsion-free, that its nonzero complex group-ring scalars act injectively in the regular representation, and that the normalized marks in \(H_{\rm ab}=C_{24}\) are \(3,4\).
If the two-by-two rectangle \(B+At-s(D+Ct)\) has regular rank \(3/2\), put \(P(z)=Az+B,\ Q(z)=Cz+D,\ M(z)=P(z)Q(z)^{-1}\).
Then the maximal orders of the actual unit-circle poles of \(M\) and \(M^{-1}\) are equal.
Equivalently, \(\det P\) has a double unit-circle zero if and only if \(\det Q\) has a double unit-circle zero.
In that case all four corner matrices \(A,B,C,D\) are invertible, and the matrices \(A^{-1}B\) and \(C^{-1}D\) each have one nondiagonal Jordan block with unimodular eigenvalue.
The two double zeros may be at different points under this necessary condition.

## Singular value bounds for two cyclic factors

Let \(x,y\) be infinite-order elements of a discrete group \(G\) whose cyclic subgroups intersect trivially.
Let \(L,R\in{\rm GL}_n(\mathbb C(z))\), \(W=L(x)R(y)\), and use the normalized trace \({\rm tr}_n\otimes\tau\).
For an affiliated matrix \(T\) write \(D_T(u)={\rm Tr}(1_{(u,\infty)}(|T|))\).
If the boundary poles of \(L\) and \(R\) have order at most one, then
\[
                         D_W(u)\le C u^{-2/3}\qquad(u\ge1).
\]
If \(L\) or \(R\) has a boundary pole of order \(d\ge1\), then
\[
                         D_W(u)\ge c u^{-1/d}\qquad(u\ge u_0).
\]
Constants may depend on the rational matrices.
No independence assumption on words with more than two cyclic factors is required.

In fact \(\tau(f(x)h(y))=(\int f)(\int h)\) for bounded scalar functions, with Haar probability integrals on the circle.
For Laurent polynomials this follows from \(\langle x\rangle\cap\langle y\rangle=\{1\}\), and bounded Fourier approximants give the identity for bounded measurable functions.
Applying it entrywise and cycling the matrix trace gives
\[
 \|U(x)V(y)\|_2^2
 =\iint{\rm tr}_n\!\left(V(w)^*U(z)^*U(z)V(w)\right)\,dz\,dw
\]
for bounded measurable matrix functions \(U,V\), where \(dz,dw\) also denote Haar probabilities.

For \(T=L,R\) and \(a\ge1\), let \(E_{T,a}=1_{\{\|T(z)\|\le a\}}\) be a scalar cutoff.
A finite set of at most simple poles gives \(\int(1-E_{T,a})\le C/a\) and \(\int E_{T,a}\|T\|^2\le Ca\), the latter by integration of the tail.
Set \(W_a=E_{L,a}(x) W E_{R,a}(y)\).
The displayed integral gives \(\|W_a\|_2^2\le Ca^2\).
Moreover \(W-W_a=(I-E_{L,a}(x))W+E_{L,a}(x)W(I-E_{R,a}(y))\) has rank at most \(C/a\) by its left and right supports.
For any affiliated matrices \(T,T_0\),
\[
                  D_T(u)\le {\rm rk}(T-T_0)+D_{T_0}(u).
\]
Indeed the intersection of the kernel of their difference and the low spectral subspace of \(|T_0|\) has codimension at most the right hand side and the norm of \(T\) on it is at most \(u\).
The same argument uses the dimension of the intersection with the high spectral subspace of \(|T|\), or bounded high spectral slices followed by monotone convergence for unbounded operators.
Taking \(a=u^{2/3}\) and using \(D_{W_a}(u)\le Ca^2/u^2\) proves the upper estimate.

For the lower estimate on the left factor put \(S=L(x)\).
Choose a closed arc of positive Haar measure \(b\) on which \(R\) and \(R^{-1}\) are regular, and write \(q\) for its scalar spectral projection in \(y\), times \(I_n\).
Then \(S q=W V\), with \(V=R(y)^{-1}q\) bounded and nonzero.
For \(e=1_{(a,\infty)}(|S|)\), two-factor trace factorization gives \({\rm Tr}(eqe)=b\,{\rm Tr}(e)\).
Since \(0\le eqe\le e\), the spectral projection of \(eqe\) for \((b/2,1]\) has trace at least \(b{\rm Tr}(e)/(2-b)\).
The positive spectral distributions of \(eqe\) and \(qeq\) agree by the polar decomposition of \(eq\).
Thus \(D_{eq}(\sqrt{b/2})\ge bD_S(a)/(2-b)\).
Writing \(S=U|S|\), the contraction \(a e |S|^{-1}U^*\) sends \(S q\) to \(a e q\).
Multiplication by a bounded matrix of norm \(k>0\) on either side satisfies \(D_{T V}(ku),D_{V T}(ku)\le D_T(u)\) when \(\|V\|\le k\).
For left multiplication this follows by restriction to the low spectral subspace of \(|T|\), and adjoints give right multiplication.
Consequently
\[
 D_W\!\left(a\sqrt{b/2}/\|V\|\right)\ \ge\ D_{Sq}(a\sqrt{b/2})
 \ \ge\ b D_S(a)/(2-b).
\]
A pole of order \(d\) in one entry gives \(\|L(z)\|\ge c|z-z_0|^{-d}\) on a punctured arc, so \(D_S(a)\ge c' a^{-1/d}\) for large \(a\), counting at least one singular value with weight \(1/n\).
The same lower estimate for the right factor follows by applying the left-factor proof to \(W^*\) with the cyclic groups interchanged.

## Applying the four-step identity

Write \(t_i=s^its^{-i}\), \(g=s^4\).
Any nontrivial intersection of neighboring cyclics is a common power subgroup \(\langle t^k\rangle\) normal in \(H\) by the [middle subgroup theorem](Yin_C_A0240_v1.md#statement).
The quotient by it is cyclic by the [periodic image theorem](Yin_C_A0288_v1.md#statement), making \(H\) virtually cyclic since that quotient is a quotient of \(C_{24}\).
A torsion-free virtually cyclic group is cyclic, which is incompatible with \(H_{\rm ab}=C_{24}\).
Thus neighboring cyclics intersect trivially.
For \(W=M(t_1)M(t_0)\), [the ordered identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) reads
\((s^2 W s^{-2})W=gI\).
Hence \(W^{-1}=g^{-1}s^2 W s^{-2}\) has the same singular value distribution as \(W\).
The inverse has the two-factor expression \(M^{-1}(t_0)M^{-1}(t_1)\), with the same disjoint cyclics in reverse order.

By the [six-evaluation obstruction](Yin_C_A0244_v1.md#statement), both \(M\) and \(M^{-1}\) have a boundary pole.
The adjugate formulas and quadratic determinant denominators bound each order by two.
If one rational matrix had only simple poles and the other had a pole of order two, the common distribution of \(W,W^{-1}\) would be bounded above by \(Cu^{-2/3}\) and below by \(cu^{-1/2}\) for all sufficiently large \(u\), which is impossible.

It remains to relate actual poles to the determinant zeros.
The [four-column reduction](Yin_C_A0184_v1.md#statement) makes the assembled constant matrix invertible, so \(\binom{P(z_0)}{Q(z_0)}\) has rank two for every finite \(z_0\).
At a double zero of \(\det Q\) where \(Q(z_0)\) has rank one, the image of \(\operatorname{adj}Q(z_0)\) is \(\ker Q(z_0)\).
The restriction of \(P(z_0)\) to that line is injective, so \(P(z_0)\operatorname{adj}Q(z_0)\ne0\) and \(M\) has an actual double pole.
If \(Q(z_0)=0\), then \(Q(z)=(z-z_0)C\) with \(C\) invertible.
The matrices \(M(z)\) then occupy projectively a pencil of at most two constant matrices.
Such a generically invertible pencil has a constant point correspondence: normalize by the inverse of an invertible member on the left and take an eigenline of the other basis matrix.
This is excluded by the [constant point correspondence test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
Interchanging \(P,Q\) gives the corresponding argument for \(M^{-1}\), since a constant point correspondence reverses for the inverse.
A double unit-circle determinant zero gives nonzero leading and constant coefficients, hence makes both coefficient matrices of that pencil invertible.
The repeated eigenvalue of the normalized constant coefficient has modulus one and its eigenspace has dimension one by the rank-one calculation.
This proves all stated coefficient conditions.

## Assessment history

### Decision tails-of-the-two-cyclic-factors

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | The upper and lower tail estimates distinguish double poles from simple poles for the actual middle product. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Pole orders and both Jordan conditions. |
| argument | [Singular value bounds for two cyclic factors](#singular-value-bounds-for-two-cyclic-factors) | Square-norm factorization, finite-rank loss in trace and the lower spectral slice. |
| argument | [Applying the four-step identity](#applying-the-four-step-identity) | Reciprocity and lack of cancellation at a double determinant zero. |
| review | [Tails of the two cyclic factors](../audits/reviews/Yin_R_A0214_v1.md#tails-of-the-two-cyclic-factors) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-tails-of-the-two-cyclic-factors)
