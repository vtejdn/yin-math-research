---
author: Yin
---

# A Gaussian diagonal shift and the ordinary determinant of a shared-input Hermitian product

<a id="statement"></a>
## An all-dimension limit at each prescribed nonreal parameter

Fix real \(c\), nonreal \(z\), and the [original Wigner laws and arbitrary coupling across dimensions](../tasks/Yin_T_F0014_v1.md#contract) for three independent colors \(X,Y,Z\).
Put
\[
 A_N=cI+X_N,\qquad B_N=X_NY_N+Y_NX_N+Z_NY_NZ_N,\qquad P_N=A_N B_N .
\]
Assume the raw diagonals of \(X\) are centered Gaussian with nonzero variance and \(Y_N\) is normalized GUE.
The off-diagonal law of \(X\) and both laws of \(Z\) may be arbitrary admissible fixed two-moment laws, including atomic laws.
Then, almost surely through all dimensions,
\[
 N^{-1}\log|\det(P_N-zI)|\ \longrightarrow\
 \tau\log|(c+s_x)(s_xs_y+s_ys_x+s_zs_ys_z)-z|.
 \tag{1}
\]
The same conclusion holds with the GUE assumption on \(Y\) replaced by the [total-variation translation modulus](Yin_C_F0186_v38.md#statement) for its raw upper law on \(\mathbb R^2\) and raw diagonal law on \(\mathbb R\), under the original second moments.
The probability-one event may depend on \(z\).
The [associated word-chain pencil](../ledger/Yin_L_F0061_v2.md#linearization-transfer) has the same finite and limiting logarithms divided by its fixed auxiliary size.
For \(c\ge2\), the [negative-subspace determinant](Yin_C_F0358_v3.md#statement) consequently has normalized logarithm tending to zero almost surely at the same \(z\), including \(c=2,z=i\).

<a id="argument"></a>
## Conditioning on the traceless part of the first color

We show that for every \(q>0\) there exists \(b>0\) with
\[
 \Pr\{s_{\min}(P_N-zI)\le N^{-b}\}=O_{q,z,c}(N^{-q}).                \tag{2}
\]
Constants may also depend on the fixed laws.
Write \(X=X^\circ+tI\) with \(t=\operatorname{tr}_N X\).
If the raw diagonal variance is \(\sigma_x^2\), then \(t\) has law \(N(0,\sigma_x^2/N^2)\) independently of \(X^\circ,Z,Y\).
This is orthogonal projection of the independent Gaussian diagonal vector, together with independence of the strict-upper entries.

On the real Hilbert space \(\mathcal H_N\) of Hermitian matrices with inner product \(\operatorname{Tr}(HK)\), use the selfadjoint real-linear operator
\[
 \mathcal T(H)=XH+HX+ZHZ=\mathcal T^\circ(H)+2tH ,
\]
where \(\mathcal T^\circ\) uses \(X^\circ,Z\).
Selfadjointness follows by cyclicity of the trace.
Conditioned on \(X^\circ,Z\), the \(N^2\) eigenvalues of \(\mathcal T^\circ\) and the \(N\) eigenvalues of \(cI+X^\circ\) are fixed.
A union bound using the \(O(N)\) density of \(t\) gives
\[
 \Pr\{s_{\min}(\mathcal T)<u\ \text{or}\ s_{\min}(A)<u\}
        \le C N^3 u .
\]
Choose \(L>q+4\).
Outside a set of probability \(O(N^{-q})\) both least values exceed \(N^{-L}\) (the endpoints also have probability zero), and \(\|X\|,\|Z\|\le N^L\) since their squared Hilbert--Schmidt norms have expectations \(O(N)\).
Fix \(X,Z\) on this event, and put \(K=A^{-1}\).
Then \(\|K\|\le N^L,\ s_{\min}(K)=1/\|A\|\ge c_0N^{-L}\) for a constant \(c_0>0\) and \(\|\mathcal T^{-1}\|_{\rm HS\to HS}\le N^L\).

<a id="repair"></a>
## A Hermitian correction for an approximately singular product

Consider any \(Y'\in\mathcal H_N\) with \(\|Y'\|\le N^L\) and set \(B'=\mathcal T(Y')\), so that \(\|B'\|\le3N^{3L}\) for large \(N\).
If \(s_{\min}(AB'-zI)\le\epsilon\), there exists a unit \(v\) with
\[
       \|(B'-zK)v\|\le N^L\epsilon,\qquad
       |v^*Kv|\le N^L\epsilon/|\operatorname{Im}z|.
\]
The second bound follows by taking imaginary parts, since \(v^*B'v\) is real.
Write \(k=s_{\min}(K)>0\) and \(s=v^*Kv\).
For \(|s|<k/4\) we construct a unit \(w\) with \(w^*Kw=0\) and \(\|w-v\|\le2\sqrt{|s|/k}\).
When \(s=0\) take \(w=v\).
Otherwise decompose \(v=v_++v_-\) in the positive and negative spectral subspaces of \(K\), and put \(\alpha=v_+^*Kv_+,\ \beta=-v_-^*Kv_-\).
In the case \(s>0\), replace \(v_+\) by \(\sqrt{\beta/\alpha}\,v_+\).
The squared change is at most \(((\alpha-\beta)/\alpha)\|v_+\|^2\le s/k\), and the new vector is isotropic for \(K\).
It is nonzero since the change is less than \(1/2\), and normalization at most doubles the change.
For \(s<0\) interchange the signs.
If \(K\) is definite the premise \(|s|<k/4\) is impossible.

Take \(\epsilon=N^{-b}\) with \(b>2L+1\) so that the construction applies for large \(N\).
Set \(e=zKw-B'w\).
Then \(w^*e\) is real and
\[
   \|e\|\le N^L\epsilon+(\|B'\|+|z|\|K\|)\|w-v\|
          \le C_z N^{4L}\sqrt\epsilon .
\]
The Hermitian matrix \(E=ew^*+we^*-(w^*e)ww^*\) satisfies \(Ew=e\) and \(\|E\|_{\rm HS}\le3\|e\|\).
Thus \(A(B'+E)-zI\) is singular and \(Y'+\mathcal T^{-1}(E)\) is a singular input at Hilbert--Schmidt distance at most \(C_zN^{5L}\sqrt\epsilon\) from \(Y'\).

<a id="tube"></a>
## Conditional Gaussian probability of the corrected set

In the GUE case write \(Y'=G=N^{-1/2}\sum_{\alpha=1}^{N^2}g_\alpha H_\alpha\) for independent standard real Gaussians and a Hilbert--Schmidt orthonormal Hermitian basis.
More generally consider \(Y'=Y_0+\delta G\) with arbitrary fixed Hermitian center \(Y_0\) and \(0<\delta\le1\).
The squared modulus of \(\det(A\mathcal T(Y')-zI)\) is a real nonnegative polynomial in the \(N^2\) Gaussian coordinates of degree at most \(2N\).
It is nonzero as a polynomial: these coordinates range over the whole Hermitian space, and \(Y'=0\) gives determinant \((-z)^N\).
On the joint event \(\|Y'\|\le N^L,\ s_{\min}(A\mathcal T(Y')-zI)\le\epsilon\), the Hermitian correction places the Gaussian vector within Euclidean distance
\(\rho=C_z\delta^{-1}N^{5L+1/2}\sqrt\epsilon\) of this polynomial zero set.
The [coefficient-uniform Gaussian tube estimate](Yin_C_F0186_v3.md#tube-without-floor) bounds its probability by \(C N^2\rho\exp(CN^2\rho)\), uniformly in the center and the admitted \(X,Z\).
This includes an empty zero set.

For GUE take \(Y_0=0,\ \delta=1\).
In the translation-regular case let the center be the original independent \(Y\) and take independent \(G\) with \(\delta=N^{-J}\).
If \(\alpha>0\) is a common modulus exponent, the [product-law translation estimate](Yin_C_F0186_v38.md#argument) gives
\(\|\operatorname{law}(Y+\delta G)-\operatorname{law}(Y)\|_{\rm TV}\le C N^2\delta^\alpha\).
It applies to upper and diagonal coordinates at their raw scales; the Gaussian tail beyond unit translations is also bounded by the same fractional moment estimate.
Choose \(J>(q+2)/\alpha\) in this case and use \(J=0\) for GUE.
Apply the tube bound to the joint norm and least-value event, conditioning on the center when necessary, before transferring its probability to the original law.
The original \(Y\) violates the norm guard with probability \(O(N^{1-2L})\) by its second moments.
Taking \(b\) sufficiently large that \(N^{2+J+5L+1/2-b/2}=O(N^{-q})\), and including the exceptional \(X,Z\), proves (2).

<a id="limit"></a>
## From the least singular value to the ordinary logarithm

Let \(L_P(z)\) be the [exact word-chain pencil](../ledger/Yin_L_F0061_v2.md#linearization-transfer) of size \(m\).
It is the product of two [triangular Schur factors](Yin_C_F0195_v4.md#scalar-fisher) and \(\operatorname{diag}(P-z,Q_{\rm aux})\), where the two factors and the auxiliary pivot have polynomial inverses in the inputs.
For \(q>2\) the norm guard for all three colors and (2) hold eventually almost surely by the first Borel--Cantelli lemma under every coupling.
There is thus a fixed \(b'>0\) such that \(s_{\min}(L_P(z))\ge N^{-b'}\) eventually almost surely, by multiplying the polynomial norm bounds for these inverses and \((P-z)^{-1}\).
The [finite-variance polynomial cutoff theorem](Yin_C_F0186_v40.md#determinant) gives almost-sure convergence of the \(N^{-b'}\)-clipped pencil logarithms to the free pencil logarithm under the original two-moment laws.
This part of that theorem uses the intermediate count and row concentration for the full pencil, and the finite target here follows from the [free logarithmic integrability of a nonconstant scalar polynomial](Yin_C_F0186_v38.md#polynomial-consequences).
Eventually the clipped and ordinary logarithms coincide.
Multiplication by \(m\) proves (1) by the exact finite and free Schur identities.
For \(c\ge2\) the free first factor is positive and injective, so subtracting the [convergent Hermitian comparison logarithm](Yin_C_F0358_v3.md#comparison) gives the assertion about the compressed determinant.

## Current assessment
[Selected decision](#decision-diagonal-shift-reviewed)

## Assessment history

### Decision diagonal-shift-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:04 |
| status | open |
| reason | The mean Gaussian diagonal shifts the entire conditional Hermitian operator, and a corrected isotropic vector gives a polynomial least-value floor for the shared-input product. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prescribed nonreal shift](#statement) | All sizes, original two-moment first upper law and third color, and a GUE or translation-regular second color. |
| argument | [Conditional shift and inverse bounds](#argument) | The \(N^2\) real eigenvalues of the second-color map and the \(N\) first-factor eigenvalues. |
| support | [Isotropic correction](#repair) | Exact Hermitian correction with a bound on its Hilbert--Schmidt norm. |
| support | [Conditional tube](#tube) | Full Gaussian coordinates, anisotropic inverse cost and transfer to the second color. |
| support | [Ordinary logarithm](#limit) | Polynomial inverse guards and finite-variance clipped convergence for the exact word chain. |

### Decision diagonal-shift-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:13 |
| status | proved |
| reason | A shared Gaussian diagonal shift and a Hermitian correction to the singular set give an arbitrary inverse-power floor and full-sequence ordinary logarithms under the stated partial regularity. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed assertions](#statement) | A shared Gaussian diagonal shift and a Hermitian correction to the singular set give an arbitrary inverse-power floor and full-sequence ordinary logarithms under the stated partial regularity. |
| argument | [Complete proof](#argument) | Original input restrictions, exact parameter and coupling requirements. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0368_v2.md#diagonal-shift-whole-proof) | Assessment of the complete fixed proof. |
