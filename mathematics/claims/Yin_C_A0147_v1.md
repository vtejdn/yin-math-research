---
author: Yin
---

# Lifting an idempotent germ recovers a rational kernel projection

## Statement

Let \(G\) be a finitely generated discrete group, let \(U=L^0(\mathcal N(G))\), and write \(D_G\) and \(R_G\) for the division closure and the \(*\)-regular closure of \(\mathbb CG\) in \(U\).
For one central indeterminate \(z\), put \(S=\operatorname{Div}_{U((z))}(\mathbb CG[z])\) and \(O=S\cap U[[z]]\).
Give formal series the coefficientwise involution fixing \(z\).
Taking the constant coefficient defines a surjective ring map \(O\to R_G\), and the constant series in \(O\) form \(D_G\). [Constant-term theorem](Yin_C_A0141_v1.md#statement)

Let \(B\in M_n(D_G)\) be positive in \(M_n(U)\), and let \(p\) be the orthogonal projection onto its kernel.
The entries of \(p\) lie in \(D_G\) if and only if some \(e\in M_n(O)\) satisfies \(e^2=e\) and \(e(0)=p\).
Every such lift, including a nonselfadjoint one, gives the constant series
\[
                     p=I-B(B^2+ee^*)^{-1}B.                         \tag{1}
\]
The inverse in (1) has entries in \(O\).

Consequently the [unrestricted finite-rank equation](Yin_C_A0131_v1.md#statement) detects membership in \(D_G\) for every affiliated element if and only if every idempotent in \(R_G\) lifts to an idempotent in \(O\).
It suffices to lift just the scalar orthogonal projections \(p_{\ker x}\) for \(x\in D_G\).
In ring-theoretic terms, complete deletion for \(G\) is equivalent to \(O\) being semiregular.

## Argument

### Recovering the orthogonal projection

A scalar of \(O\) whose constant coefficient is a unit in \(U\) has a power series inverse in \(U[[z]]\), and this inverse lies in \(O\) by the division closure defining \(S\).
For \(H\in M_n(O)\) with invertible constant matrix in \(M_n(U)\), the same conclusion gives \(H^{-1}\) with entries in \(O\).
Indeed each leading block of \(H(0)^*H(0)\) is the Gram matrix of a set of columns with a left inverse, hence is an affiliated unit.
Eliminate the entries of \(H^*H\) in the order of these leading blocks.
At each step the scalar Schur pivot has invertible constant coefficient by the block factorization at zero, so its inverse belongs to \(O\).
This gives \((H^*H)^{-1}H^*=H^{-1}\) over \(O\).

Work first in the larger matrix algebra over \(U[[z]]\), where the constant series \(p\) is available.
Set \(q=I-p\) and \(h=ep+(I-e)q\).
Then \(h(0)=I\), and \(eh=hp\) since \(e^2=e\).
It follows that \(e=hph^{-1}\).
The power series \(K=ph^{-1}(h^{-1})^*p\) in the \(p\)-corner has constant coefficient \(p\), so \(q+K\) is invertible and its inverse acts as the identity on \(q\).
Put \(V=B+hp\).
Its constant term \(B+p\) is an affiliated unit, since \(B\) is invertible on its support in the affiliated corner.
Since \(Vq=qV^*=B\) and \(Vp=hp\), we have
\[
                  B^2+ee^*=V(q+K)V^*,
       \qquad B(B^2+ee^*)^{-1}B=q(q+K)^{-1}q=q .
\]
The factorization proves (1).
The matrix \(B^2+ee^*\) belongs to \(M_n(O)\) and its constant term is the affiliated unit \(B^2+p\).
The matrix inverse observation puts the entire right side of (1) in \(M_n(O)\).
The [descent of constant series](Yin_C_A0141_v1.md#descent-of-a-constant-series) now puts the entries of \(p\) in \(D_G\).
Conversely, when \(p\) has its entries in \(D_G\), the constant matrix \(p\) itself is an idempotent lift.

### The Jacobson radical and complete deletion

The kernel of the constant coefficient map is \(zO\), since \(z^{-1}\in S\).
For any \(a,b\in O\), the inverse of \(1-azb\) belongs to \(O\) by its constant coefficient.
Thus \(zO\) lies in the Jacobson radical \(J(O)\).
The quotient \(R_G\) is von Neumann regular and has zero Jacobson radical.
Indeed if \(u\in J(R_G)\) and \(u=uvu\), then \(1-vu\) is a unit and \(u(1-vu)=0\) forces \(u=0\).
The image of \(J(O)\) lies in the radical of the quotient, giving \(J(O)=zO\).
Semiregularity therefore means exactly that idempotents lift under \(O\to R_G\). [Nicholson, Theorem 2.9](https://doi.org/10.4153/CJM-1976-109-2)

If the unrestricted equation detects \(D_G\), its [regular-closure characterization](Yin_C_A0131_v1.md#which-rationality-is-detected) gives \(D_G=R_G\), so every idempotent lifts as a constant.
Conversely, every \(x\in D_G\) has its kernel projection in \(R_G\) by relative inversion.
If that projection admits an idempotent lift, apply (1) with \(B=x^*x\), which has the same kernel as \(x\).
Thus all these projections belong to \(D_G\), which implies complete deletion by the same characterization.

### Finite truncations and adjoining a complementary idempotent

Let \(p\) now be any idempotent in \(R_G\), and fix \(N\ge1\).
The [finite truncation isomorphism](Yin_C_A0146_v1.md#constant-terms-at-finite-order) \(O/z^NO\simeq R_G[z]/(z^N)\) supplies \(f\in O\) with \(f=p+O(z^N)\) in \(U[[z]]\).
In particular \(f(0)=p\) and \(f^2-f\in z^NO\).
The constant classes \(p\) form a compatible family of idempotents in these quotients as \(N\) varies.

One can also lift the pair \(\operatorname{diag}(p,1-p)\) to an exact matrix idempotent in \(M_2(O)\), agreeing with that constant matrix through degree \(N-1\).
Define
\[
         W_f=\begin{pmatrix}f&1-f\\1-f&f\end{pmatrix},
       \qquad E_f=W_f\begin{pmatrix}1&0\\0&0\end{pmatrix}W_f^{-1}.
\]
The constant change of basis with columns \((1,1)^{\mathsf T},(1,-1)^{\mathsf T}\) diagonalizes \(W_f\) to \(\operatorname{diag}(1,2f-1)\).
The constant coefficient \(2p-1\) squares to one, so \(W_f^{-1}\) exists in \(M_2(O)\).
Since \(W_f=W_p+O(z^N)\) and \(W_p^2=I\), the inverse agrees with \(W_p\) through the same degree.
It follows that \(E_f^2=E_f\) and \(E_f=\operatorname{diag}(p,1-p)+O(z^N)\).

For a kernel projection \(p=p_{\ker B}\) in the scalar test, lifting \(p\oplus0_k\) or \(p\oplus I_k\) for any \(k\ge1\) already implies \(p\in D_G\), by (1) applied to \(B\oplus I_k\) or \(B\oplus0_k\).
The construction with the complementary summand \(1-p\) works for every residue idempotent, independently of its rationality.
Thus finite-order lifts and a joint lift with the complement are available for every group, whereas a single exact lift of \(p_{\ker B}\) is the criterion (1).

## Assessment history

### Decision idempotent-lifting

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:12 |
| status | proved |
| reason | An exact idempotent lift gives the orthogonal kernel projection by one rational inverse and descent of a constant series. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Recovery from one exact lift, semiregularity, finite truncations, and the effect of adjoining a summand. |
| argument | [Argument](#argument) | A two-sided factorization, the Jacobson radical, scalar kernel tests and complementary idempotents. |
| dependency | [Constant coefficients and constant series](Yin_C_A0141_v1.md#statement) | Surjective reduction and descent to the division closure. |
| dependency | [Unrestricted equation](Yin_C_A0131_v1.md#which-rationality-is-detected) | Scalar kernel projections characterize complete deletion. |
| dependency | [Finite truncations](Yin_C_A0146_v1.md#constant-terms-at-finite-order) | Arbitrary jets of residue idempotents. |
| dependency | [Semiregularity](../audits/literature/Nic76/Yin_U001.md#nic76-u001) | Nicholson, Theorem 2.9, equivalence of conditions (1) and (2). |
| review | [Idempotent lifting](../audits/reviews/Yin_R_A0170_v1.md#idempotent-lifting) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-idempotent-lifting)
