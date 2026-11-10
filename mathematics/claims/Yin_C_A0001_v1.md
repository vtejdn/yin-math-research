---
author: Yin
---
# Finite-support kernel extraction for amenable Schur complements

This deduction answers the Schur-complement transfer question in the [fourth route](../strategies/Yin_S_A0004.md) for finitely generated amenable groups.
It extracts the matrix form of the [Ele03 boundary proof](../audits/literature/Ele03/Yin_U001.md#boundary-proof) and applies the established affiliated Schur identity.
It asserts a conditional reduction at this group scope, with no claim of new Atiyah group-class coverage.

## Statement

Let \(G\) be finitely generated and amenable, \(B=\mathbb CG\) in its faithful left regular representation, and \(U=\mathcal U(\mathcal N(G))\).
Use the canonical trace and unnormalized matrix trace.

For every \(A\in M_{p,q}(B)\), \(p,q\ge1\), if \(\ker_{\ell^2}A\ne0\), there exists \(0\ne v\in B^q\) with \(Av=0\).
More precisely, for any finite nonempty \(F\subset G\) and a propagation width \(w\) for \(A\), put \(\delta=\dim_G\ker A\) and use the [right-invariant metric and inner boundary convention](../audits/literature/Ele03/Yin_U001.md#folner-and-propagation).
Then
\[
\delta-q\,\frac{|\partial_wF|}{|F|}
\le
\frac{\dim_{\mathbb C}(\ker A\cap\mathbb C[F]^q)}{|F|}
\le\delta.
\]

In particular let \(a,b,c,d\in B\), assume \(d\) is invertible in \(U\), and set
\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad r=a-bd^{-1}c\in U.
\]
If \(r\ne0\) and \(\ker_{\ell^2}r\ne0\), there exist \(x,y\in B\) with
\[
x\ne0,\qquad ax+by=0,\qquad cx+dy=0,
\qquad \ker_{\ell^2}\lambda(x)\ne0.
\]
Thus nonzero noninjectivity of this rational Schur complement yields a nonzero scalar group-ring element with nontrivial analytic kernel.
Consequently, if every nonzero element of \(B\) acts injectively on \(\ell^2(G)\), every such \(r\) is either zero or invertible in \(U\).

## Current assessment

[Selected decision](#decision-reviewed-amenable-extraction)

## Assessment history

### Decision reviewed-amenable-extraction

| Field | Value |
| --- | --- |
| date | 2026-11-10T14:45 |
| status | proved |
| reason | The complete finite-set estimate and Schur extraction have passed independent review under the stated amenability and finite-tracial hypotheses; no assertion for arbitrary torsion-free groups is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Rectangular matrix estimate, finite-support kernel extraction and the stated scalar-denominator Schur consequence. |
| argument | [Complete argument](#argument) | Local projection dimensions, boundary estimate, affiliated block elimination and cancellation. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0002_v1.md#whole-argument-finding) | Independently reviewed complete statement and argument, with the recorded foundational boundaries. |
| dependency | [Finite-trace affiliated interfaces](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Exactly Lemmas 5.1–5.5 and 5.9: injectivity versus affiliated invertibility, stable finiteness and rank invariance under the specified invertible block operations, with closed-product conventions. |

The source attribution and proof-extraction origin are [Ele03's finite-set argument](../audits/literature/Ele03/Yin_U001.md#boundary-proof).
The local proof reproduces that estimate and its matrix extension; it does not assume the source theorem or integer-valued matrix ranks as an unproved premise.

## Argument

### Matrix boundary estimate

For right-invariant subspaces of \(\ell^2(G)^n\), use
\[
\dim_G V=\sum_{j=1}^n\langle P_V\delta_{e,j},\delta_{e,j}\rangle,
\quad
\dim_F W=\frac1{|F|}\sum_{g\in F}\sum_{j=1}^n
\langle P_W\delta_{g,j},\delta_{g,j}\rangle.
\]
Here \(P_W\) means projection onto the closure.
Invariant subspaces have constant diagonal in each component.
For subspaces supported on \(F\), \(\dim_FW=\dim_{\mathbb C}W/|F|\).
Projection monotonicity, positivity and faithfulness follow componentwise from the scalar proof.

Let \(w\) bound the word lengths of the supports of all entries of \(A\), with \(w=0\) if \(A=0\).
Finite propagation gives
\[
T_F=A|_{\mathbb C[F^{-w}]^q}:
\mathbb C[F^{-w}]^q\longrightarrow\mathbb C[F]^p.
\]
Write \(\rho=\dim_G\overline{\operatorname{im}A}\).
Polar decomposition for the bounded equivariant matrix operator gives \(\delta+\rho=q\).
Set
\[
u_F=\dim_{\mathbb C}\ker T_F/|F|,\qquad
t_F=\dim_{\mathbb C}\operatorname{im}T_F/|F|.
\]
The kernel and image inclusions, followed by local-dimension monotonicity, give
\[
u_F\le\delta,\qquad t_F\le\rho,\qquad
u_F+t_F=q\,|F^{-w}|/|F|.
\]
Thus
\[
(\delta-u_F)+(\rho-t_F)=q\,|\partial_wF|/|F|.
\]
Both deficits are nonnegative.
The inclusion \(\ker T_F\subseteq\ker A\cap\mathbb C[F]^q\) proves the claimed lower bound.
Projection monotonicity proves the upper bound.

If the kernel is nonzero, faithfulness gives \(\delta>0\).
Choose a Følner set for which \(q|\partial_wF|/|F|<\delta\).
The finite-dimensional kernel then contains a nonzero vector.
The estimate uses only finite propagation up to this selection of \(F\), and the selection is the use of amenability.

### Schur-complement extraction

The established rank calculus in a finite affiliated algebra is used here at its exact scope.
Analytic rank is invariant under invertible affiliated row and column operations, additive for diagonal blocks, and equals the number of columns minus kernel dimension.
For scalar affiliated operators, injectivity is equivalent to invertibility in \(U\).
These foundations are retained in the [MSY23 source units](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) and [Lin00 affiliated-algebra account](../audits/literature/Lin00/Yin_U001.md).
The direct operator interfaces are [MSY23 Lemmas 5.1–5.5](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and [Lemma 5.9](../audits/literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof).
Integer-valued rank is not assumed.

Affiliated multiplication gives the exact identity
\[
\begin{pmatrix}1&-bd^{-1}\\0&1\end{pmatrix}
M
\begin{pmatrix}1&0\\-d^{-1}c&1\end{pmatrix}
=\begin{pmatrix}r&0\\0&d\end{pmatrix}.
\]
Both triangular factors are invertible, so
\[
\operatorname{rk}M=1+\operatorname{rk}r,\qquad
\dim_G\ker M=\dim_G\ker r>0.
\]
The matrix result supplies a nonzero \((x,y)\in B^2\) with \(M(x,y)^t=0\).
If \(x=0\), then \(dy=0\), and invertibility of \(d\) in \(U\) implies \(y=0\), a contradiction.
Thus \(x\ne0\).
The second row gives \(y=-d^{-1}cx\) in \(U\), so the first row yields \(rx=0\) in \(U\).

These are identities of affiliated operators induced by the group-ring equations, rather than a presumption that every kernel vector lies in the domain of every summand of a rational expression.
If \(\lambda(x)\) were injective, it would be invertible in \(U\).
Right cancellation in \(rx=0\) would then give \(r=0\), contrary to the hypothesis.
Hence \(\lambda(x)\) has a nontrivial analytic kernel.
The final consequence follows because any nonzero \(r\) with a kernel would contradict the assumed scalar injectivity.

## Scope and use

For the route's family,
\[
a=1-f,\quad b=1-h,\quad c=1-k,\quad d=1-g,
\]
infinite order of \(g\) supplies invertibility of \(d\) in \(U\).
Indeed \((1-g)\xi=0\) makes \(\xi\) constant along infinite cyclic orbits, so square summability forces \(\xi=0\).
The extraction argument then additionally uses amenability of \(G\).
It neither obtains a Følner sequence nor scalar injectivity from torsion-freeness.

The conditional Ore argument already retained in [Yin_L_A0002](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) gives the known broader amenable-domain route once its stated hypotheses hold.
The present deduction identifies the particular finite-matrix kernel mechanism behind a Schur-complement extraction.

## Derivation context

On 10 November 2026, Yin requested a complete Ele03 audit and an analysis of its transfer to the fourth route.
The coordinating agent reconstructed the source proof and wrote this matrix and Schur deduction.
The source theorem, its finite-set estimate, the local matrix extension, and the affiliated-algebra input have the separate scopes specified above.
