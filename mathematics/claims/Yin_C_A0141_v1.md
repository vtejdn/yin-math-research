---
author: Yin
---

# Constant terms and constant series in the division closure with one formal parameter

## Statement

Let \(G\) be a finitely generated discrete group, \(A=\mathbb CG\), and \(U=L^0(\mathcal N(G))\).
Write \(D_G\) and \(R_G\) for the division closure and the \(*\)-regular closure of \(A\) in \(U\), respectively.
For one central indeterminate \(z\), write \(U((z))\) for formal Laurent series with coefficients in \(U\) and a finite lower bound on their exponents.
Let \(S=\operatorname{Div}_{U((z))}(A[z])\), formed by adjoining scalar inverses of two-sided units of this Laurent series ring.
For a power series \(f\), denote its constant term by \(f(0)\).
Then
\[
       \{f(0): f\in S\cap U[[z]]\}=R_G,
       \qquad S\cap U=D_G ,
\]
where \(U\) in the second equality consists of constant series.
In fact every Laurent coefficient of every member of \(S\) belongs to \(R_G\).

Thus an affiliated \(u\) satisfies [the unrestricted finite-rank equation](Yin_C_A0131_v1.md#statement) precisely when it occurs as the constant term of a power series in \(S\).
It belongs to \(D_G\) precisely when its constant series belongs to \(S\).
Complete deletion of the local condition for \(G\) is equivalent to closure of \(S\cap U[[z]]\) under taking the constant term as a constant series.
The [specialization test for a compressed resolvent](../ledger/Yin_L_A0075_v1.md#regular-specialization-of-the-compressed-resolvent) concerns one prescribed function of a real parameter and asks for an expression whose inverses are all defined at zero.
The two equalities here describe all formal scalar expressions with Laurent inverses, including expressions whose intermediate inverses have poles.

## Argument

### Recovering a Laurent coefficient from finitely many equations

Every element of \(S\) has a realization \(f=\alpha L(z)^{-1}\beta\) with a polynomial square matrix \(L\) over \(A[z]\) invertible in the formal Laurent ring and constant complex vectors \(\alpha,\beta\).
For a polynomial \(p\), take the upper-right entry of the inverse of \(\left(\begin{smallmatrix}1&-p\\0&1\end{smallmatrix}\right)\).
Sums use block diagonal matrices and products use upper triangular block matrices with off-diagonal block \(-\beta_1\alpha_2\).
Inverting a unit realization uses the bottom-right entry of the inverse of \(\left(\begin{smallmatrix}L&\beta\\\alpha&0\end{smallmatrix}\right)\), with a minus sign.
These operations follow by block multiplication and preserve the stated domain of every inverse.

Write \(L(z)=\sum_{j=0}^d L_jz^j\), and choose \(m\ge0\) so that \(L^{-1}\) has no terms below degree \(-m\).
The same bound holds for \(y=L^{-1}\beta\).
To recover \(y_h\) for \(h\ge-m\), take \(N=\max(0,h+m)\) and form the finite system
\[
              \sum_{j=0}^d L_j v_{\ell-j}
                  =\boldsymbol 1_{\ell=0}\beta
              \qquad(-m\le \ell\le N),
\]
with unknown columns \(v_{-m},\ldots,v_N\) and zero columns outside this range.
Truncating \(y\) gives a solution over \(U\).
For the Laurent polynomial \(v(z)\) of any solution, \(L(z)v(z)-\beta\) has order at least \(N+1\).
Multiplication by \(L^{-1}\) shows that \(v-y\) has order at least \(N+1-m>h\).
In particular every solution has \(v_h=y_h\).

The block Toeplitz matrix \(T\) of the finite system has entries in \(A\).
Its relative inverse \(T^{[-1]}\), defined by inverting between supports and taking zero on the orthogonal complement of the range, has entries in \(R_G\) by [matrix regularity](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions).
The right-hand column \(b\) is in \(TU^n\), where \(n\) is the number of scalar unknowns, so \(TT^{[-1]}b=b\).
The solution \(T^{[-1]}b\) supplies \(y_h\) over \(R_G\), proving \(\alpha y_h\in R_G\) for each \(h\).

### Realizing every element of the regular closure

For \(u\in R_G\), the [single-vector criterion and its converse](Yin_C_A0137_v1.md#single-vector-vanishing-and-equation-1) give a group-ring matrix \(K\) and constant vectors \(\epsilon,\gamma\) with \(u=\epsilon K^{[-1]}\gamma\).
Put \(B=KK^*\), \(P=p_{\ker B}\) and \(C=B^{[-1]}\).
In the matrix Laurent series ring, direct multiplication gives
\[
             (B+zI)^{-1}
             =z^{-1}P+\sum_{j\ge0}(-z)^j C^{j+1}.
\]
Indeed \(BP=PB=0\), \(BC=CB=I-P\), and \(CP=PC=0\).
Every leading principal submatrix of \(B\) is also positive, so the same formula in its size proves that every leading principal block of \(B+zI\) is invertible.
Eliminating the blocks in order gives scalar unit pivots and expresses every entry of the full inverse in \(S\).
In detail, bordering an invertible leading block by one row and column gives a scalar Schur complement which is a two-sided unit by the invertibility of the enlarged block, and the block inverse formula uses only this additional scalar inverse.

Since \(K^*P=0\), the series \(f=\epsilon K^*(B+zI)^{-1}\gamma\) belongs to \(S\cap U[[z]]\).
Its constant coefficient is \(\epsilon K^*C\gamma=u\), by the relative inverse identity \(K^{[-1]}=K^*(KK^*)^{[-1]}\).
This gives the entire image of the constant-term map.

### Descent of a constant series

The inclusion \(D_G\subset S\cap U\) follows by performing its scalar inversions on constant series.
Suppose conversely that \(u=\alpha L(z)^{-1}\beta\) as a constant formal series, with the realization above.
Let \(J=G\times\mathbb Z\) and let \(Z\) be the unitary of the positive generator of the second factor.
On \(\ell^2(J)\), a vector supported on finitely many integer heights has coefficients in \(\ell^2(G)=L^2(\mathcal N(G))\subset U\).
It therefore gives a Laurent polynomial column over \(U\) on which \(L(Z)\) acts as multiplication by \(L(z)\).
The formal inverse rules out a nonzero finite-height kernel vector of \(L(Z)\).
For any rectangular group-ring matrix over \(J\), the finite-height vectors in its Hilbert kernel span a dense subspace by the [interval kernel theorem](Yin_C_A0136_v1.md#statement).
Consequently \(L(Z)\) is injective, and, being square over a finite von Neumann algebra, it has an affiliated inverse.
The entries of this inverse belong to \(D_J\) by [scalar Gram elimination](Yin_C_A0132_v1.md#argument).

Choose a bounded affiliated-unit left denominator \(s\in\mathcal N(G)\) for \(u\), with \(a=su\in\mathcal N(G)\).
Consider the Hilbert kernel of the bounded row of blocks \([L(Z),-\beta]\).
For any finite-height vector \((x,w)\) in this kernel, the formal identity \(L(z)x(z)=\beta w(z)\) gives \(s\alpha x(z)=aw(z)\).
The interval kernel theorem applied to this row gives density of the finite-height solutions in the full Hilbert kernel.
Since \([s\alpha,-a]\) is bounded, it annihilates the whole kernel and therefore its orthogonal projection.
The affiliated column \(\binom{L(Z)^{-1}\beta}{1}\) lies in the right module of that projection, since \([L(Z),-\beta]\) annihilates the column.
Applying \([s\alpha,-a]\) to the column yields \(s\alpha L(Z)^{-1}\beta=a\).
Thus the constant copy of \(u\) belongs to \(D_J\), and [torus specialization](Yin_C_A0132_v1.md#argument) gives \(u\in D_J\cap U=D_G\).

## Assessment history

### Decision formal-constant-terms

| Field | Value |
| --- | --- |
| date | 2026-11-25T10:17 |
| status | proved |
| reason | Finite coefficient equations give the constant-term image, while finite-height relations and central specialization identify the constant series. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All coefficients, realization of every unrestricted solution and exact membership of constant series. |
| argument | [Argument](#argument) | Finite Toeplitz equations, positive principal compressions and descent along the central shift. |
| dependency | [Equation (1)](Yin_C_A0131_v1.md#statement) | Unrestricted solvability and regular-closure membership. |
| dependency | [Matrix regularity](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Relative inverses of the finite coefficient equations. |
| dependency | [Realization between supports](Yin_C_A0137_v1.md#single-vector-vanishing-and-equation-1) | Writing every unrestricted solution as a coefficient of a relative inverse. |
| dependency | [Interval kernel theorem](Yin_C_A0136_v1.md#statement) | Density of finite-height solutions of a rectangular graph relation. |
| dependency | [Central specialization](Yin_C_A0132_v1.md#argument) | Scalar Gram pivots and descent of constant affiliated operators. |
| review | [Formal constant terms](../audits/reviews/Yin_R_A0168_v1.md#formal-constant-terms) | Whole statement and proof at the scope of the recorded independent review. |

## Current assessment

[Selected decision](#decision-formal-constant-terms)
