---
author: Yin
---

# A square observation at zero and its preservation by affine Schur realization

<a id="statement"></a>
## A polynomial observation theorem

Work with the [fixed-law finite-variance Hermitian Wigner model](../tasks/Yin_T_F0013_v1.md#input-model) and free semicircular variables \(s\).
Let \(H=H^*\) be a square matrix polynomial of size \(m\), let \(J\) have size \(r\times m\), and set \(L=H+iJ^*J\), \(G=H^2+J^*J\).
All entries are noncommutative polynomials in the selfadjoint variables, with fixed complex coefficients.
Write \(\mathcal C_{\mathcal N}(D)\) for the following property of a square polynomial \(D\) of fixed size \(h\), on a specified deterministic sequence of dimensions \(\mathcal N\) tending to infinity:
\[
 \log\Delta_{\operatorname{tr}_h\otimes\tau}(D(s))\in\mathbb R,\qquad
 \frac1{hN}\log|\det D(W^{(N)})|
 \longrightarrow\log\Delta_{\operatorname{tr}_h\otimes\tau}(D(s))
 \quad\text{in probability along }\mathcal N .
\]
The three assertions below are equivalent.
1. \(\mathcal C_{\mathcal N}(L)\) holds.
2. \(\mathcal C_{\mathcal N}(G)\) holds.
3. There are fixed polynomial matrices \(M\) of size \(m\times m\) and \(K\) of size \(m\times r\) such that \(\mathcal C_{\mathcal N}(B)\) holds for \(B=MH+KJ\).

Each assertion yields the [every-coupling dimension upper limit](Yin_C_F0190_v1.md#coupling-criterion) for \(L\) at its finite free value.
The individual free logarithms for \(B,G,L\) may differ.
The implication from 3 to 1 extends the [observation by iterated rows](Yin_C_F0186_v35.md#statement) because \(JH^d=(JH^{d-1})H\) for \(d\ge1\).
It permits \(H\) itself to enter a witness.
The two additional conclusions below give an affine realization preserving this certificate and a scalar class at every prescribed real shift.

<a id="argument"></a>
## Logarithmic control from the two rows

Use the [logarithmic tail lemma](Yin_C_F0186_v34.md#logarithmic-tails-of-products).
For a rectangular finite matrix \(X\) write \(F_l(X)=\sum_{j\le l}\log^+s_j(X)\) with decreasing singular values and zero padding.
Fixed polynomial evaluations have
\[
 \lim_{\delta\downarrow0}\limsup_{N\in\mathcal N}
 \Pr\{F_{\lfloor\delta N\rfloor}(X_N)>\eta N\}=0
 \quad(\eta>0)
 \tag{Tail}
\]
by [positive logarithmic control](Yin_C_F0186_v4.md#positive-tail), also for rectangular blocks after square embedding.
On a square polynomial evaluation, invertibility with probability tending to one and (Tail) for the inverse on that event are equivalent to \(\mathcal C_{\mathcal N}\) by the cited tail lemma.
We use the [product and sum inequalities](Yin_C_F0186_v35.md#argument) \(F_l(XY)\le F_l(X)+F_l(Y)\) and \(F_l(X+Y)\le F_l(X)+F_l(Y)+l\log 2\).

Suppose 3 holds, suppress evaluation and work on the event that \(B\) is invertible.
If \(Lv=0\), the imaginary quadratic form gives \(Jv=0\), whence \(Hv=0\) and \(Bv=0\).
Thus \(L\) is invertible.
For \(Z=L^{-1}\), \(Y=JZ\), we have \(HZ=I-iJ^*Y\) and \(Y^*Y=-\operatorname{Im}Z\).
The max-min principle gives \(s_j(Y)^2\le s_j(Z)\), as shown in the [iterated-row proof](Yin_C_F0186_v35.md#argument).
Since
\[
 BZ=M+(K-iMJ^*)Y ,
\]
the two inequalities for \(F_l\) give
\[
 F_l(Z)\le 2\bigl(F_l(B^{-1})+F_l(M)+F_l(K-iMJ^*)+l\log 2\bigr).
\]
Every term on the right has (Tail).
This proves 1.
Assertion 2 implies 3 with \(M=H,\ K=J^*\).

Suppose finally that 1 holds and put \(S=\begin{pmatrix}H\\ J\end{pmatrix}\), meaning the vertical stack of \(H\) above \(J\).
On the high-probability invertibility event for \(L\), the matrix \(Z[I,\ iJ^*]\) is a left inverse of \(S\), because \(L=[I,\ iJ^*]S\).
Thus \(G=S^*S\) is invertible and the Moore--Penrose inverse of \(S\) equals \(Z[I,\ iJ^*]\pi_{\operatorname{ran}S}\).
The singular values of \(G^{-1}\) are the squares of the nonzero singular values of that inverse, giving
\[
 F_l(G^{-1})\le2F_l(Z)+2F_l([I,\ iJ^*]).
\]
The tail lemma proves 2.
For each parameter the [upper-semicontinuity bound](../ledger/Yin_L_F0061_v2.md#upper-limit) applies along the full sequence.
Choosing a deterministic subsequence with summable lower deviations in 1 proves the upper-limit assertion for every cross-size coupling.

<a id="affine-lift"></a>
## Preserving the witness in an ordinary affine pencil

Given \(H,J\) as above and \(B=MH+KJ\), there is an explicit Hermitian affine \(F=F^*\) and a constant coordinate projection row \(J_0\) such that the affine pencil \(\mathscr L=F+iJ_0^*J_0\) has
\[
 |\det \mathscr L(X)|=|\det L(X)|,\qquad
 h\log\Delta_{\operatorname{tr}_h\otimes\tau}(\mathscr L(s))
   =m\log\Delta_{\operatorname{tr}_m\otimes\tau}(L(s)),
 \tag{Schur}
\]
where \(h\) is its auxiliary size.
The finite identity holds at every tuple \(X\) of Hermitian matrices of each common size.
Polynomial matrices \(M_0,K_0\) give a square affine-pencil observation \(B_0=M_0 F+K_0J_0\) whose finite determinant modulus is exactly \(|\det B(X)|\) and whose free total logarithm equals that of \(B\).
Here \(B_0\) may be polynomial of higher degree, while both the observed selfadjoint pencil \(F\) and \(\mathscr L\) are affine.

To construct it, define
\[
 F_b=
 \begin{pmatrix}H&J^*\\ J&0\end{pmatrix},\qquad J_b=[0,\ I_r].
\]
Schur elimination over \(iI_r\) in \(F_b+iJ_b^*J_b\) gives exactly \(L\).
On this enlarged polynomial use the static witness
\[
 M_b=\begin{pmatrix}M&K\\0&0\end{pmatrix},\qquad
 K_b=\binom{-MJ^*}{I_r},\qquad M_bF_b+K_bJ_b=\operatorname{diag}(B,I_r).
\]

Use the [word-chain construction](../ledger/Yin_L_F0058_v2.md#exact-linearization) for the matrix polynomial \(F_b\), treating each coefficient times a matrix unit entrywise and concatenating the finite auxiliary chains.
This writes \(F_b=a-UT^{-1}V\), where \(a,U,T,V\) are affine, \(T\) is unit upper triangular and \(T^{-1}\) is polynomial.
In an individual monomial matrix entry the row of \(U\) and column of \(V\) attach its first and last letters to the desired output and input indices.
The internal strictly upper shift of that monomial's chain supplies its remaining letters in the given order.
A polynomial of degree at most one needs no auxiliary chains.
Set
\[
 D=\begin{pmatrix}0&T^*\\ T&0\end{pmatrix},\quad
 C=2^{-1/2}[U,\ V^*],\quad
 F=\begin{pmatrix}(a+a^*)/2&C\\ C^*&D\end{pmatrix},
 \quad J_0=[J_b,\ 0].
\]
The inverse of \(D\) has top-right block \(T^{-1}\), bottom-left block \((T^*)^{-1}\) and zero diagonal blocks.
The Schur complement of \(D\) in \(F\) is precisely \(F_b\) because \(F_b=F_b^*\).
The triangular matrix
\[
 T_0=\begin{pmatrix}I&0\\-D^{-1}C^*&I\end{pmatrix}
\]
and its inverse are polynomial, \(T_0^* F T_0=\operatorname{diag}(F_b,D)\), and \(J_0 T_0=J_0\).
The finite modulus and the free normalized determinant of each of \(D,T_0\) are one, using the flip and its unit triangular factors for \(D\).
The [bounded FK triangular and trace-weight identities](Yin_C_F0186_v3.md#linearization-transfer) apply before and after the Schur steps, including singular targets.
This proves (Schur).

Set \(M_0=\operatorname{diag}(M_b,D^{-1})T_0^*\), \(K_0=\begin{pmatrix}K_b\\0\end{pmatrix}\).
Then \((M_0F+K_0J_0)T_0=\operatorname{diag}(B,I_r,I)\).
This verifies both determinant identities for the observation and transports \(\mathcal C_{\mathcal N}(B)\) to the lifted pencil with the indicated auxiliary trace scaling.

<a id="real-axis-application"></a>
## Scalar polynomials allowing arbitrary shared input

Fix any scalar \(H=H^*\), scalar polynomial \(R\), and nonzero scalar affine polynomial \(b\), all using the same input variables if desired.
For
\[
 P=H+i\{R^*R+(RH+b)^*(RH+b)\}
\]
the [F0014 equality](../tasks/Yin_T_F0014_v1.md#contract) holds at every fixed real \(z\), with a finite target and probability convergence along all even dimensions.
Indeed replace \(H\) by \(H-z\), use \(J=\binom{R}{RH+b}\), and take \(M=-R,\ K=[-z,\ 1]\).
Then \(M(H-z)+KJ=b\).
The [affine scalar theorem](Yin_C_F0186_v11.md#scalar-affine-statement) supplies \(\mathcal C_{\mathcal N}(b)\) along the even dimensions.
This proof uses neither independence between \(H,R,b\) nor a determinant estimate for either component of \(J\).

At \(z=0\) the same statement applies to \(H+i(RH+b)^*(RH+b)\) by using only the last observation row.
For example \(H=x,\ R=y,\ b=1\) gives the static identity \(-yx+(yx+1)=1\).
At the scalar tuple \(x=1,y=-1\), every iterated observation \((yx+1)x^j\) vanishes.
Thus a constant nonzero witness obtained from the static rows can exist even when no polynomial combination of those iterated rows gives the same constant.
The [winding obstruction](Yin_C_F0349_v1.md#statement) concerns a different boundary of the method at a nonreal parameter.

## Assessment history

### Decision static-observation-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:33 |
| status | proved |
| reason | Independent whole-proof review checked the Gram equivalence, the affine Schur realization and the repeated-variable real-axis application. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete stated conclusions under the specified hypotheses. |
| argument | [Proof](#argument) | Full mathematical argument for this version. |
| support | [Affine realization](#affine-lift) | Finite determinants, free trace weights and the static witness. |
| support | [Real shifts](#real-axis-application) | Two observation rows for every real shift and the single-row case at zero. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0359_v1.md#static-observation) | Complete fixed statement, proof and applicability boundaries. |

## Current assessment

[Selected decision](#decision-static-observation-reviewed)
