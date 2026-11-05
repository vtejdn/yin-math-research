---
author: Yin
---

# Pure-imaginary Wigner scalar shifts and skew singular directions

<a id="scope"></a>
## Scope and review boundary

This bounded development does not change any fixed Claim.
The first parity statements have identically zero diagonal; the later scalar-shift result allows an arbitrary fixed real diagonal law with finite second moment.
The accepted probabilistic inputs are the every-unit-phase [second-smallest floor](../claims/Yin_C_F0194_v6.md#phase-line-second-floor), [corank tail](../claims/Yin_C_F0194_v6.md#phase-line-rank-tail), and [restricted isolated-minor estimate](../claims/Yin_C_F0194_v6.md#phase-line-isolated-minor) of C_F0194_v6.
Its [cyclic gauge](../claims/Yin_C_F0194_v6.md#phase-line-gauge) and [complex-coordinate distance proof](../claims/Yin_C_F0194_v6.md#complex-distance), together with the [deterministic spread and averaging interface](../claims/Yin_C_F0194_v3.md#spread-and-average) and [real-border matching estimate](../claims/Yin_C_F0194_v3.md#two-copy-matching), are used only at the checked scopes below.
Its [reviewed decision](../claims/Yin_C_F0194_v6.md#decision-phase-line-floor-reviewed) adopts those every-phase auxiliary interfaces following the [independent whole-proof review](../audits/reviews/Yin_R_F0200_v6.md#finding).
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

For even original size \(N\), the paired least-value bound gives the following stronger special case of the many-direction interface used below.
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

<a id="quantile-guard-floor"></a>
## A uniform all-dimension floor on a symmetric-quantile guard

Now let \(W_N\) have independent upper entries \(i\eta_{jk}/\sqrt N\), conjugate lower entries, and independent real diagonal entries \(\zeta_j/\sqrt N\).
Here \(\eta\) is centered with variance one, and \(\zeta\) is any fixed real law with finite second moment, independent of the off-diagonal family.
Centering of \(\zeta\) is not needed for this floor lemma.
Fix \(\gamma,L_0,b>0\), let \(F\) be deterministic with \(\max|F_{jk}|\le N^\gamma\), and put \(M=W_N+F\).
For every omitted index \(i\), define
\[
 D_i=M[[N]\setminus\{i\}],\quad
 A_i=\operatorname{adj}D_i,\quad
 S_i=\operatorname{sym}D_i
   =\operatorname{diag}(\zeta_j/\sqrt N)_{j\ne i}
      +\operatorname{sym}F_i.
\]
Use decreasing singular values, put \(r_N=\lfloor\sqrt N\rfloor\), \(k_N=4r_N+1\), and define the exact guard
\[
 \Sigma_N(F,L_0)
 =\bigcap_{i=1}^N
     \{s_{k_N}(S_i)\ge N^{-L_0}\}.
 \tag{Symmetric-quantile-guard}
\]
For all sufficiently large \(N\), \(k_N\le N-1\).
The proposed complete deduction is that some fixed \(A,C_b,C,N_0\), depending only on the laws and displayed exponents, satisfy
\[
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A},\ \Sigma_N(F,L_0)\}
 \le C_bN^{-b}
       +C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Quantile-guard-floor}
\]
The constants are uniform over the entire displayed class of deterministic complex shifts.
There is no parity restriction.
<a id="quantile-guard-failure"></a>
For a random shift \(F_N\) independent of \(W_N\), define
\[
 \Gamma_N=\{\max|F_{N,jk}|\le N^\gamma\},
 \qquad
 \varepsilon_N^{\rm guard}
   =\mathbb P\bigl(\Gamma_N^c\cup
             \Sigma_N(F_N,L_0)^c\bigr).
 \tag{Guard-failure}
\]
Within-dimension conditioning gives the same right side plus \(\varepsilon_N^{\rm guard}\) for the unguarded least-value probability.
This permits an arbitrary random complex matrix shift, including a fixed polynomial of other independent inputs.
It does not condition on the guard itself and requires no independence between that guard and \(W_N\).

<a id="pure-imaginary-weighted-gauge"></a>
### The correct graph and the symmetric guard survive the gauge

Use the exact C_F0194_v6 cyclic gauge with \(c=i\).
Its diagonal phase matrix is \(Z_i=iE_i\), where \(E_i\) is real diagonal with signs, and \(U_i=Z_iP_i=iO_i\), where \(O_i=E_iP_i\) is real monomial orthogonal.
Consequently
\[
 \widehat D_i=U_i^*D_iU_i=O_i^TD_iO_i,\qquad
 \operatorname{sym}\widehat D_i=O_i^TS_iO_i.
 \tag{Pure-imaginary-gauge}
\]
All singular quantiles in \(\Sigma_N\) are preserved exactly.
The gauge also preserves the full determinant, the minor determinant, all singular values and the adjugate Frobenius norm.
The accepted cyclic calculation, not a symmetry assumption on the amplitude law, shows that \(\widehat D_i\) again has upper law \(i\eta/\sqrt N\) and the same independent diagonal law.

The correct outer quadratic coefficients are
\[
 Q_i^{\rm wt}=\operatorname{sym}(Z_i^*A_iZ_i)
     =E_i\operatorname{sym}(A_i)E_i,\qquad
 \widehat Q_i=P_i^TQ_i^{\rm wt}P_i
     =\operatorname{sym}(\operatorname{adj}\widehat D_i).
\]
Thus in this pure-imaginary case the absolute weighted edge values equal the original absolute sym-adjugate entries, up to permutation.
We nevertheless keep the gauge, because its exposed upper and lower borders are the same iid real \(\eta/\sqrt N\) vector plus fixed offsets.
This is the exact hypothesis of the accepted real-border two-copy matching proof.
For the graph with edges \(|(Q_i^{\rm wt})_{jk}|\ge h\|A_i\|_F\), let \(H_i(h,r)\) mean \(A_i\ne0\) and a matching of size at least \(r\).
For some law-dependent \(c_*,C>0\), on this minor event,
\[
 \mathbb P\left\{
 \frac{|\det M|}{\|A_i\|_F}\le c_*h/N
          \ \middle|\ D_i,\ M_{ii}\right\}
 \le C\psi(r),\qquad
 \psi(r)=e^{-c_*r}+\sqrt{\log(2+r)}r^{-1/9}.
 \tag{Pure-imaginary-matching}
\]
This invokes C_F0194_v3's real-border estimate after verifying its deterministic gauge hypotheses.
It does not invoke the nonzero-real-part assumption of C_F0194_v6's low-matching probability theorem.
The \(N^{-1}\) radius is the actual quadratic normalization.

<a id="internal-many-directions"></a>
### A second-value bound suffices in every internal dimension

Fix an outer index \(i\) and an internal index \(j\) of \(\widehat D_i\).
Let \(B\) be the internal block of size \(p=N-2\), and put \(K_B=\operatorname{skew}B\).
Its random part has zero diagonal and pure-imaginary upper law, irrespective of the real diagonal variables of \(B\):
\[
 K_B=W_{\rm off,sub}+\operatorname{skew}\widehat F_{i,-j}.
\]
The shift in this display is deterministic and skew, and its entries have the original polynomial bound.
The normalized random part is \(\sqrt{p/N}\) times the standard size-\(p\) zero-diagonal model.
Since \(p/N\) stays in \([1/2,1]\), the accepted all-phase second-value theorem, with a fixed exponent slack for the shift and this factor, gives a fixed \(L>0\) with
\[
 s_{p-1}(K_B)\ge N^{-L}
 \tag{Internal-skew-second}
\]
outside any prescribed polynomial failure probability.
The exponent \(L\) can be chosen before all coefficient thresholds, with enough probability margin for the \(O(N^2)\) internal blocks.
This assertion allows odd \(p\): one singular value may vanish.

On \(\det B\ne0\), write \(R=B^{-1}\).
Using the identity already established above and singular min-max under invertible multipliers,
\[
 s_{p-1}(\operatorname{skew}R)
 =s_{p-1}(-B^{-T}K_BB^{-1})
 \ge \frac{s_{p-1}(K_B)}{\|B\|^2}
 \ge N^{-L-2K}
\]
on \(\|B\|\le N^K\).
No inverse-norm bound for \(B\), parity of \(p\), or least-value bound for \(K_B\) is needed.
For the raw internal column \(z=iE\eta\), the exact cofactor coefficient map is
\[
 \mathcal L\eta
  =N^{-1/2}\Phi(z)
  =\frac{i}{\sqrt N}(\operatorname{skew}R)E\eta.
\]
It has at least \(p-1\) complex singular values at least
\(\kappa_N=N^{-L-2K-1/2}\).

If \(q\) input coordinates and the same \(q\) output coordinates are discarded, at least \(p-1-2q\) singular directions of the remaining square block still have that lower bound.
Indeed intersect a good subspace of complex codimension at most one with the retained coordinate space and with the kernel of the discarded output rows.
Its dimension is at least \(p-1-2q\), and on it the retained output has the full output norm.
This is the singular min-max assertion needed for the following row estimate.

<a id="pure-imaginary-uncovered-diagonal"></a>
### Full-row uncovered-diagonal exclusion without a central strip

Fix \(K\) and a polynomial failure exponent \(b_0>0\), choose \(L\) as above, and then choose any fixed \(J\ge0\) and
\[
 H>J+L+2K+2.
 \tag{Pure-imaginary-row-scale}
\]
Outside probability \(C_{b_0}N^{-b_0}+C e^{-cN}\), simultaneously for all \(i\), all covers \(I\) with \(|I|<2r_N\), and all \(j\notin I\), the following configuration is absent:
\[
 \begin{split}
 &\widehat A_i\ne0,\quad\|\widehat D_i\|\le N^K,\\
 &|(\widehat Q_i)_{ab}|<N^{-H}\|A_i\|_F
       \quad(a\ne b,\ a,b\notin I),\\
 &|(\widehat Q_i)_{jj}|\ge N^{-J}\|A_i\|_F.
 \end{split}
 \tag{Pure-imaginary-uncovered-event}
\]
Here \(\widehat A_i=\operatorname{adj}\widehat D_i\).

To prove this, first remove the simultaneous (Internal-skew-second) exceptions, requesting their individual failure exponents with margin for all \(i,j\).
For fixed \(i,I,j\), condition on the internal block \(B\).
The last inequality forces \(\det B=(\widehat Q_i)_{jj}\ne0\), since the adjugate is nonzero.
If \(\det B=0\), the indicated event is empty.
On the block-measurable norm and skew-second guards, the preceding coefficient estimate therefore applies.
Let \(T\) be the internal coordinates outside \(I\), and also fix the raw row amplitudes indexed by \(I\).
The retained amplitudes \(\eta_T\) remain independent copies of the original real centered variance-one law, independent of \(B\).
The deleted diagonal may also be fixed; it does not enter this off-diagonal cofactor map.

The exact internal-row identity reads
\[
 -\frac{(\widehat Q_i)_{-j,j}}{\det B}
   =\frac{i}{\sqrt N}(\operatorname{skew}R)E\eta
          +\frac{Rg+R^Tf}{2},
\]
with deterministic affine offsets after conditioning.
The two displayed coefficient hypotheses force the retained output norm to be at most
\[
 \sqrt{|T|}\,N^{J-H}.
\]
The retained coefficient matrix has at least \(p-1-2|I|\ge |T|/2\) singular directions at scale \(\kappa_N\), eventually.
Project to those good left singular directions and divide by their singular values.
A small-output event then places \(\eta_T\) within distance at most
\[
 \sqrt{|T|}N^{J-H+L+2K+1/2}
\]
of a fixed complex affine subspace of complex codimension at least \(|T|/2\).
The exponent in this display is strictly negative by (Pure-imaginary-row-scale).
The accepted fixed-cutoff distance bound for a real variance-one law near complex affine subspaces consequently makes its conditional probability at most \(C e^{-c|T|}\le C e^{-c'N}\).
All constants are uniform in \(B\), the retained coefficient matrix, the conditioned coordinates and the affine center.
No global row-dependent norm or adjugate event has been conditioned on: these events are used only to imply membership in the fixed-center small-output event.
The number of \(i,j,I\) is at most \(N^{2r_N+3}=\exp(o(N))\).
Union this bound and add the internal-block exceptions to prove the assertion.
There is no majority-orientation requirement or discarded central strip.

<a id="low-matching-quantile"></a>
### A symmetric quantile turns low matching into an isolated minor

Let the matching in \(H_i(N^{-H},r_N)\) fail while \(A_i\ne0\).
Take the endpoints \(I\) of a maximal matching in the cyclic ordering, so \(|I|<2r_N\) and every off-diagonal entry of \(\widehat Q_i\) outside \(I\) is below the edge threshold.
On the last lemma's good event, all its diagonals outside \(I\) are below \(N^{-J}\|A_i\|_F\).
Thus
\[
 \widehat Q_i=Q_{\rm hub}+E,\qquad
 \operatorname{rank}Q_{\rm hub}\le2|I|<4r_N,\qquad
 \|E\|_F\le e_N\|A_i\|_F,
 \quad e_N=\sqrt{N-1}N^{-J}+(N-1)N^{-H}.
\]
The exact adjugate identity is
\[
 \widehat D_i\widehat Q_i\widehat D_i^T
     =(\det D_i)\widehat S_i,
 \qquad \widehat S_i=\operatorname{sym}\widehat D_i.
\]
On \(\Sigma_N(F,L_0)\), the preserved quantile gives
\[
 |\det D_i|N^{-L_0}
 \le s_{k_N}((\det D_i)\widehat S_i)
 \le \|\widehat D_i E\widehat D_i^T\|
 \le N^{2K}e_N\|A_i\|_F,
\]
because \(k_N\) exceeds the hub rank.
Hence
\[
 \rho_i=\frac{|\det D_i|}{\|A_i\|_F}
       \le N^{2K+L_0}e_N.
 \tag{Quantile-low-ratio}
\]
Only the indicated singular quantile is used, not \(s_{\min}(S_i)\).
This remains true if \(S_i\) is singular.
For any prescribed \(T_0>0\), choose
\[
 J>2K+L_0+T_0+2,\qquad
 H>\max\{J+L+2K+2,\ 2K+L_0+T_0+3\}.
\]
Then \(\rho_i\le N^{-T_0}\) eventually.
If \(D_i\) is invertible, the elementary identity
\(\rho_i=(\sum_j s_j(D_i)^{-2})^{-1/2}\)
gives \(t_1(D_i)\le\sqrt{N-1}\rho_i\).
If it is singular with nonzero adjugate, it has exactly corank one and \(\rho_i=t_1(D_i)=0\).

<a id="quantile-assembly"></a>
### Complete parameter order and probability assembly

Fix the requested \(b>0\).
Choose a raw cutoff exponent \(\kappa>(b+6)/2\), then
\(K>\max\{\kappa+1/2,\gamma+1\}\), with fixed slack for constants.
The finite-second-moment entry union bound gives
\(\mathbb P\{\|M\|>N^K\}\le C_bN^{-b-2}\).
Apply the accepted every-phase corank estimate to the raw matrix \(\sqrt N M\), whose shift exponent is at most \(\gamma+1\), to remove rank at most \(N-2\) with probability \(C_bN^{-b-2}\).

Apply the accepted second-value theorem to every actual \(D_i\).
Its size is \(N-1\), its normalization is \(\sqrt N\), and its shift becomes bounded by \((N-1)^{\gamma+2}\) after raw rescaling.
Choosing a larger failure exponent for their union and absorbing the bounded dimension ratio yields a fixed \(L_2\) with
\[
 t_2(D_i)\ge N^{-L_2}\quad\hbox{for every }i
\]
outside probability \(C_bN^{-b-2}\).
Next choose \(A_0,L_{\rm iso}\) from the accepted raw isolated-minor theorem at shift exponent \(\gamma+1\), requesting failure exponent \(b+3\).
These choices precede all fine coefficient thresholds.
Choose the internal skew-second exponent \(L\) with the same margin for the \(O(N^2)\) block union.
Finally select
\[
 T_0>L_{\rm iso}+L_2+3,\qquad
 J>2K+L_0+T_0+2,\qquad
 H>\max\{J+L+2K+2,\ 2K+L_0+T_0+3\},
\]
and take
\[
 A>\max\{H+2K+3,\ A_0+2K+3,\ 2\}.
 \tag{Final-quantile-parameters}
\]
All exponents are fixed before exposing any random minor or row.

The accepted complex-coordinate rectangular-distance argument, with the deterministic cofactor spread and averaging proof, gives constants \(a,\delta,C_1>0\) as follows.
Outside \(C e^{-cN}\), the event
\[
 \|M\|\le N^K,\quad
 \operatorname{rank}M\ge N-1,\quad
 s_{\min}(M)\le\varepsilon_N=N^{-A}
\]
forces at least \(\delta N/2\) indices with
\[
 G_i=\left\{
 A_i\ne0,\quad\|M\|\le N^K,\quad
 \frac{|\det M|}{\|A_i\|_F}
       \le C_1N^{2K+1}\varepsilon_N
 \right\}.
\]
The required preliminary smallness \(\varepsilon_N\le a/(4\sqrt N)\) holds by the final choice of \(A\).
The rectangular input is valid for the pure-imaginary law and its conjugate orientations by C_F0194_v6's complex-distance statement; the spread and averaging implication is deterministic once those rectangles hold.
In particular the probability of the target event intersected with \(\Sigma_N\) is bounded by \(C/N\) times the sum of the corresponding probabilities \(G_i\cap\Sigma_N\), plus the common exceptions.
This is averaging, not a union over the high-matching probabilities.

For high matching, the choice of \(A\) gives
\(C_1N^{2K+1-A}\le c_*N^{-H-1}\)
eventually, so (Pure-imaginary-matching) contributes at most \(C\psi(r_N)\).
The additional symmetric guard can simply be dropped in this upper bound.
For low matching, the simultaneous uncovered-diagonal and skew-second guards and \(\Sigma_N\) give \(\rho_i\le N^{-T_0}\).
If \(D_i\) is invertible, then
\[
 t_1(\sqrt N D_i)\le N^{1-T_0},\qquad
 \frac{t_1(\sqrt N D_i)}{t_2(\sqrt N D_i)}
      \le N^{1/2+L_2-T_0}.
\]
Both are at most \(N^{-L_{\rm iso}}\) eventually.
The singular nonzero-adjugate case is already exactly corank one.

For every usable low-matching index the raw full ratio satisfies the exact scaling identity
\[
 \frac{|\det(\sqrt N M)|}
      {\|\operatorname{adj}(\sqrt N D_i)\|_F}
   =N\,\frac{|\det M|}{\|A_i\|_F}
   \le C_1N^{2K+2-A}\le N^{-A_0}.
\]
The factor is \(N\), since the determinant has degree \(N\) and the minor adjugate degree \(N-2\) in the scalar rescaling.
Gauge similarity introduces no additional factor.
Thus each low contribution lies in the union event of the accepted raw isolated-minor theorem, whose probability is at most \(C_bN^{-b-3}\).
This use checks both its absolute and relative singular thresholds instead of inferring isolation solely from \(\rho_i\).
The average of these low-event indicators is no larger than the indicator of their union.
Adding norm, rank, second-value, internal skew and uncovered-diagonal failures yields
\[
 \mathbb P\{s_{\min}(M)\le N^{-A},\Sigma_N\}
       \le C_bN^{-b}+C\psi(\lfloor\sqrt N\rfloor).
\]
The exponential part of \(\psi\) is absorbed into the polynomial error, and its other part is bounded by \(C\sqrt{\log(2+N)}N^{-1/18}\).
This proves the displayed proposed floor.
All auxiliary guards are combined by set inclusion and union bounds, never by conditioning on their global intersection.
For the random-shift form, condition only on \(F_N\) within this dimension, use the uniform deterministic proof, and add the exact guard failure already defined.
No cross-size independence is used.

<a id="scalar-shift-guards"></a>
## Fixed scalar shifts and the full diagonal-law classification

Take \(F=-\lambda I\) for fixed \(\lambda\in\mathbb C\).
For \(\lambda\ne0\), finite second moment implies
\[
 \mathbb P\left\{\max_{j\le N}|\zeta_j|>
                 |\lambda|\sqrt N/2\right\}
 \le N\mathbb P\{|\zeta|>|\lambda|\sqrt N/2\}\longrightarrow0.
\]
Indeed \(t^2\mathbb P\{|\zeta|>t\}\le
\mathbb E[|\zeta|^2{\bf1}_{\{|\zeta|>t\}}]\to0\).
On its complementary event every diagonal entry of every \(S_i\) has modulus at least \(|\lambda|/2\).
Thus \(\Sigma_N(-\lambda I,1)\) holds eventually on that event.
The quantile-floor theorem gives, in every dimension and for some fixed \(A_\lambda\),
\[
 \mathbb P\{s_{\min}(W_N-\lambda I)\le N^{-A_\lambda}\}\longrightarrow0.
 \tag{Nonzero-scalar-floor}
\]
No summable rate is asserted for the diagonal-tail guard.

If \(\lambda=0\) and \(\mathbb P\{\zeta\ne0\}>0\), choose fixed \(d,p_0>0\) with
\(\mathbb P\{|\zeta|\ge d\}=p_0\).
A Bernoulli Chernoff bound gives at least \(p_0N/2\) such diagonal coordinates outside probability \(C e^{-cN}\).
Deleting any one coordinate leaves more than \(k_N\) such coordinates for all sufficiently large \(N\).
Hence \(s_{k_N}(S_i)\ge d/\sqrt N\ge N^{-1}\) for every \(i\), eventually.
The same quantile theorem gives an all-dimension polynomial floor in probability at zero, with the displayed \(N^{-1/18}\sqrt{\log N}\) error plus any prescribed polynomial error.
This argument needs neither a density nor a lower bound on every diagonal coordinate.

If \(\lambda=0\) and \(\zeta=0\) almost surely, the symmetric guard vanishes.
Use the paired even-dimensional floor and the exact odd-dimensional singularity already proved above.
There is then an arbitrary-power even-dimensional least-value floor and an identically zero odd-dimensional determinant.
These three cases exhaust the fixed scalar parameter and real diagonal law.

<a id="fixed-scalar-log"></a>
## Logarithmic consequences for each fixed scalar parameter

For this section impose the centered diagonal hypothesis \(\mathbb E\zeta=0\) of the original Task, retaining its finite second moment.
Write \(s\) for a variance-one semicircular element and
\(c_\lambda=\tau\log|s-\lambda|\).
This target is finite for every fixed complex \(\lambda\): the bounded semicircular density makes a real logarithmic singularity integrable, and a nonreal \(\lambda\) is at positive distance from the real support.

In the first two scalar cases, the new least-value floor has probability tending to one.
The accepted C_F0187_v2 intermediate bound for the original complex Hermitian input and the fixed shift \(-\lambda I\) has summable failure.
The bottom \(O(N^{3/4})\) negative-log contribution is \(O(N^{-1/4}\log N)\) on the floor event, and the remaining small values contribute at most \(Ct(1+|\log t|)+o(1)\).
The accepted C_F0186_v4 weak law and positive logarithmic tails apply to the original fixed polynomial \(x-\lambda\).
Clipping and removing these tails therefore gives
\[
 \frac1N\log|\det(W_N-\lambda I)|
       \longrightarrow c_\lambda
       \quad\hbox{in probability},
 \tag{Scalar-log-probability}
\]
through all dimensions whenever \(\lambda\ne0\) or \(\mathbb P\{\zeta\ne0\}>0\).
The diagonal tail at nonzero \(\lambda\) and the matching error are not treated as summable.
For the remaining case \(\lambda=0,\zeta=0\), the earlier even-dimensional almost-sure limit and odd-dimensional zero determinant retain their exact scopes.

In every case the accepted regularized-potential bound gives the full-sequence almost-sure limsup upper inequality under every allowed coupling.
In the first two cases the full-sequence probability convergence supplies the [lower-deviation criterion of C_F0190_v1](../claims/Yin_C_F0190_v1.md#coupling-criterion).
In the remaining case the same criterion is supplied along the deterministic even subsequence, or directly by the even-dimensional almost-sure limit.
Thus the complete proposed one-parameter conclusion is
\[
 \limsup_{N\to\infty}\frac1N
       \log|\det(W_N-\lambda I)|
       =\tau\log|s-\lambda|
 \quad\hbox{almost surely under every allowed coupling}.
 \tag{Pure-imaginary-scalar-limsup}
\]
The event may depend on \(\lambda\), and no event simultaneous over all parameters is claimed.
This is proof development requiring its own review; the adopted input reviews do not constitute review of the new quantile-guard assembly.

<a id="remaining-interface"></a>
## Actual boundary for general shifts

The general shift theorem controls the event intersected with the exact quantile guard, and its unguarded form adds \(\varepsilon_N^{\rm guard}\) as defined above.
No bound on that failure probability is claimed for an arbitrary independent complex polynomial shift.
At zero shift with zero diagonal the guard is false, and odd-dimensional singularity prevents an all-dimension least-value theorem.
Thus removing the guard is a real additional obligation rather than a formal consequence of skew pairing.

A full least-value floor for \(\operatorname{sym}F\) alone would not ensure such a floor for all its principal compressions.
For example the block diagonal symmetric matrix with two-by-two blocks \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) has full least value one, but deleting a single coordinate leaves a singular principal compression.
The present theorem avoids a full-compression least-value requirement by using only the \(k_N\)-th singular values of the actual \(S_i\).
In this example the compression loses only one singular direction and its relevant quantile is still one; it is not a counterexample to the quantile guard.
No matrix-polynomial transfer or general noncommutative-polynomial conclusion is included here.
