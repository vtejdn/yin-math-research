---
author: Yin
---

# Paired skew singular values and an even-dimensional Wigner logarithm

<a id="scope"></a>
## Scope and review boundary

This bounded development does not change C_F0194_v6, C_F0186_v10 or D_F0028.
The probabilistic input is only [C_F0194_v6's adopted second-smallest floor](../claims/Yin_C_F0194_v6.md#phase-line-second-floor), whose stated phase range is every fixed \(|c|=1\), including \(c=i\).
Its [reviewed decision](../claims/Yin_C_F0194_v6.md#decision-phase-line-floor-reviewed) adopts that auxiliary statement following the [independent whole-proof review](../audits/reviews/Yin_R_F0200_v6.md#finding).
The main least-value theorem there requires \(\operatorname{Re}c\ne0\) and is not invoked for a purely imaginary law.
The new pairing proof, even-dimensional logarithmic deduction and further assembly interfaces in this D remain development without their own formal independent review or adoption.
The deterministic pairing assertion is proved independently below and has separate classical attribution.

<a id="pairing-source"></a>
## Classical source and inspected scope

[You61 and its inspected edition](../audits/literature/You61/readme.md) supply a checked primary reference for the classical skew form.
The selected 1961 original is actually retained as [the local PDF](../literature/pdf/You61--CJM.pdf).
Printed p. 694 / PDF p. 1, introduction equations (2)-(3), was read in text and visually from that retained page.
It states unitary congruence of any complex transpose-skew matrix to blocks \(\begin{pmatrix}0&\sigma\\-\sigma&0\end{pmatrix}\), with \(\sigma>0\), and zeros, and records its even rank.
Both congruence factors are unitary, so the displayed blocks give paired positive singular values.
This is attribution for a classical fact, not a novelty claim or a claimed inspection of the entire source proof.
The following self-contained proof is the mathematical argument used here.

<a id="singular-pairing"></a>
## A short antilinear proof covering complex skew matrices

Let \(A\in M_n(\mathbb C)\) satisfy \(A^T=-A\).
No Hermitian or normal hypothesis is imposed.
Write \(C\) for coordinatewise conjugation and \(T=AC\) for the resulting antilinear map.
Since \(A^*=-\overline A\),
\[
 T^2=A\overline A=-AA^*=-H,\qquad H=AA^*\ge0.
\]
Consequently \(T\) commutes with \(H=-T^2\) as real-linear maps.
For each positive eigenvalue \(\lambda\) of \(H\), its complex eigenspace \(E_\lambda\) is therefore invariant under \(T\), and
\[
 (T|_{E_\lambda})^2=-\lambda I.
\]
If \(m=\dim_{\mathbb C}E_\lambda\), write the restriction in a complex basis as \(v\mapsto S\overline v\).
Then
\[
 S\overline S=-\lambda I_m,\qquad
 |\det S|^2=(-\lambda)^m.
\]
The first equation makes \(S\) invertible, so the left side is positive and \(m\) must be even.
Every positive eigenvalue of \(AA^*\), hence every positive singular value of \(A\), has even multiplicity.
Its rank is even, and if \(n\) is even its zero singular value also has even multiplicity.
Writing singular values decreasingly, for even \(n\),
\[
 s_{2j-1}(A)=s_{2j}(A)\quad(1\le j\le n/2),
 \qquad s_n(A)=s_{n-1}(A).
 \tag{Skew-pairing}
\]
For odd \(n\), even rank forces \(s_n(A)=0\).
Equivalently odd-dimensional skew matrices have zero determinant by transposing it.

<a id="even-floor"></a>
## Arbitrary-power floor deduction on even dimensions

Fix a real law \(\eta\) with \(\mathbb E\eta=0\) and \(\mathbb E\eta^2=1\), and let \(W_N\) have upper entries \(i\eta_{jk}/\sqrt N\), conjugate lower entries, and identically zero diagonal.
The upper amplitudes are independent.
Every realization has \(W_N^*=W_N\) and \(W_N^T=-W_N\).
Let \(F\) be any deterministic complex transpose-skew matrix satisfying \(\max|F_{jk}|\le N^\gamma\).
It need not be Hermitian.
Then \(M_N=W_N+F\) is complex skew and, on even dimensions, (Skew-pairing) identifies its least and second-smallest singular values exactly.
Thus the adopted auxiliary statement gives the following deduction: for every \(\gamma,b>0\), some fixed \(A,C,N_0\) satisfy
\[
 \sup_{\substack{F^T=-F\\\max|F_{jk}|\le N^\gamma}}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C N^{-b},
 \qquad N\ge N_0,\quad N\ \mathrm{even}.
 \tag{Even-skew-floor}
\]
Only the adopted auxiliary second-floor statement is used, not the unavailable purely imaginary main least-value theorem.
For independent random skew \(F_N\), the same bound holds on its polynomial entry guard by within-dimension conditioning, and the guard complement is added otherwise.
Every odd-dimensional \(W_N+F_N\) is singular, without a probability exception.
No floor for arbitrary nonskew \(F\) follows from this pairing identity.

<a id="even-zero-log"></a>
## A complete zero-shift logarithmic development argument

Take \(F=0\) and any allowed coupling of these Wigner matrices across dimensions.
Use (Even-skew-floor) with \(b>2\).
Its failures are summable over even dimensions, so first Borel--Cantelli supplies an eventual polynomial least-value floor there.
The accepted [C_F0187_v2 intermediate theorem](../claims/Yin_C_F0187_v2.md#statement), applied to the original complex law \(i\eta\), gives increasing singular values
\[
 a_r(W_N)\ge c(r-1)/N,\qquad
 \lceil N^{3/4}\rceil+1\le r\le N
\]
outside a summable exceptional event.
This intermediate theorem allows the zero diagonal and imposes no real/imaginary independence condition.

The accepted [C_F0186_v4 complex-input controls](../claims/Yin_C_F0186_v4.md#statement) give weak convergence to the semicircular spectral law, equivalently convergence of singular laws to that of \(|s|\), and positive logarithmic tail control.
The semicircular law has bounded density near zero, so \(\tau\log|s|\) is finite.
On the even-dimensional good event, the bottom \(O(N^{3/4})\) normalized negative logarithms contribute \(O(N^{-1/4}\log N)\).
The middle bound controls the remaining values below \(t\) by \(Ct(1+|\log t|)+o(1)\).
Clipping the logarithm at fixed lower and upper cutoffs, passing by the weak law, then removing the tails proves
\[
 \frac1N\log|\det W_N|\longrightarrow \tau\log|s|\in\mathbb R
 \quad\hbox{almost surely as }N\to\infty\hbox{ through even dimensions}.
 \tag{Even-log}
\]
Every odd-dimensional log determinant equals \(-\infty\) identically.
Consequently the same deduction includes
\[
 \limsup_{N\to\infty}N^{-1}\log|\det W_N|
  =\tau\log|s|,\qquad
 \liminf_{N\to\infty}N^{-1}\log|\det W_N|=-\infty
 \quad\hbox{almost surely under every allowed coupling}.
\]
This is the one-input zero-shift instance, rather than a theorem for arbitrary polynomials or arbitrary spectral parameters.

<a id="internal-skew-interface"></a>
## The even internal block supplies a different coefficient floor

There is a further exact interface for even original size \(N\), without a completed nonzero-shift theorem here.
An outer principal minor \(D_i\) then has odd size \(N-1\), and its internal principal block \(B_j\) has even size \(p=N-2\).
For a fixed polynomially bounded shift \(F\),
\[
 \operatorname{skew}B_j
 =W_{\mathrm{sub}}+\operatorname{skew}F_{\mathrm{sub}},
 \qquad \operatorname{skew}X=(X-X^T)/2.
\]
This is an even-dimensional complex skew matrix with the pure-imaginary Wigner part and a deterministic skew shift.
Its random part is normalized by \(\sqrt N\), not \(\sqrt p\).
Writing it as \(\sqrt{p/N}\) times the standard \(p\)-dimensional model and rescaling the shift changes only fixed polynomial exponents, since \(p/N\) stays between \(1/2\) and \(1\).
Thus the developed consequence (Even-skew-floor) gives a polynomial lower bound for \(s_{\min}(\operatorname{skew}B_j)\), uniformly over internal pairs after enlarging the polynomial failure exponent to absorb their \(O(N^2)\) union.

On the branch where \(B_j\) is invertible, put \(R=B_j^{-1}\).
The deterministic identity
\[
 \operatorname{skew}R
  =-B_j^{-T}(\operatorname{skew}B_j)B_j^{-1}
\]
gives, on \(\|B_j\|\le N^K\) and \(s_{\min}(\operatorname{skew}B_j)\ge N^{-L}\),
\[
 s_{\min}(\operatorname{skew}R)\ge N^{-L-2K}.
 \tag{Internal-skew-coefficient}
\]
It needs no upper bound for \(\|B_j^{-1}\|\).
All displayed guards are measurable in the internal block, before exposing its deleted row.

For a raw pure-imaginary border \(z=iE\eta\), with deterministic diagonal signs \(E_{kk}\in\{1,-1\}\), the [exact complex internal-row formula](../claims/Yin_C_F0194_v6.md#complex-internal-row) becomes
\[
 \Phi(z)=\frac{Rz+R^T\overline z}{2}
  =i(\operatorname{skew}R)E\eta.
\]
The actual normalized cofactor map contains \(N^{-1/2}\Phi(z)\), so its full coefficient floor is \(N^{-L-2K-1/2}\).
It does not use a positive real-part variance or condition away the real amplitudes.
Deleting \(q\) rows and \(q\) columns from this coefficient matrix leaves at least \(p-2q\) singular directions at that lower scale, by the deterministic singular-value min-max principle.
This identifies a possible substitute for the positive-real-part majority-orientation bridge on its internal invertible-block branch.

<a id="remaining-interface"></a>
## The symmetric-part guard and the unassembled nonzero-shift branch

The low-matching to small-minor-ratio argument still uses
\[
 D_i^T\operatorname{sym}(\operatorname{adj}D_i)
  =(\operatorname{sym}D_i)\operatorname{adj}D_i,
 \qquad \operatorname{sym}X=(X+X^T)/2,
\]
and a polynomial floor for \(\operatorname{sym}D_i\).
Here \(\operatorname{sym}D_i=\operatorname{sym}F_i\) is deterministic for a deterministic shift and need not be invertible.
Pairing does not supply this missing guard for arbitrary \(F\).
For \(F=-\lambda I\), \(\lambda\ne0\), that particular guard is deterministic with least value \(|\lambda|\).

In this scalar-shift case \(B_j=W_{\mathrm{sub}}-\lambda I\) is generally not skew.
The even skew floor is applied to \(\operatorname{skew}B_j=W_{\mathrm{sub}}\), not incorrectly to \(B_j\) itself.
The inverse formula above is used only on \(\det B_j\ne0\), as required by the internal cofactor expansion.
These observations suggest a precise replacement interface for the scalar nonzero-shift assembly.
A complete proof must still insert that interface into the actual internal-row small-ball and cover-union argument, verify the large-diagonal versus \(\det B_j=0\) split, and reassemble its low-matching, isolated-minor, rank and second-value branches with one parameter order.
That assembly has not been carried out or claimed here.
In particular this record does not yet infer the nonzero-\(\lambda\) pure-imaginary floor, its full one-variable polynomial determinant theorem, or a general nonsymmetric-shift floor.
