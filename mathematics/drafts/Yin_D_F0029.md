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

<a id="pure-imaginary-carrier-scope"></a>
## Conditional carriers when every input is purely imaginary with zero diagonal

This further development addresses a restricted scalar noncommutative-polynomial class, beyond the preceding arbitrary-shift boundary.
It preserves the earlier even-dimensional almost-sure zero-shift conclusion and does not strengthen the arbitrary-shift floor without a new argument.
The following complete argument is research development by Yin's contributing agent, not an independent review or an adopted extension of a fixed Claim.
The relevant adopted inputs are [C_F0194_v7](../claims/Yin_C_F0194_v7.md#decision-complex-floor-reviewed), [C_F0187_v2](../claims/Yin_C_F0187_v2.md#statement), and [C_F0186_v4](../claims/Yin_C_F0186_v4.md#statement).
The [now adopted C_F0186_v11 carrier theorem](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed) treats eligible exposed laws instead; its probability-level logarithmic and cyclic arguments are applicable at the interfaces checked below, but its carrier theorem itself does not supply the new pure-imaginary floors.

Fix a finite tuple of independent Hermitian Wigner matrices within each dimension, with strict upper entries
\[
 W_{j,ab}^{(N)}=i\eta_{j,ab}/\sqrt N\quad(a<b),\qquad
 W_{j,ba}^{(N)}=-i\eta_{j,ab}/\sqrt N,\qquad
 W_{j,aa}^{(N)}=0.
 \tag{Imaginary-tuple}
\]
For each \(j\), the real amplitudes are independent copies of a fixed law with mean zero and variance one.
The laws may differ with \(j\), and no higher moment, density or cross-size independence is imposed.
Write \(s_1,\ldots,s_d\) for a free standard semicircular tuple in a finite von Neumann algebra with faithful normal tracial state \(\tau\).
Every finite realization has \((W_j^{(N)})^T=-W_j^{(N)}\).

Choose an exposed index and label it \(1\).
For arbitrary scalar complex polynomials in their indicated variables, take
\[
 \begin{split}
 T_\nu&=x_{j_\nu}+Q_\nu((x_j)_{j\ne1,j_\nu}),
       \qquad j_\nu\in\{2,\ldots,d\},\quad 1\le\nu\le K,\\
 H&=cT_1\cdots T_K,\qquad c\in\mathbb C\setminus\{0\},\\
 R&=(x_1+Q(x_2,\ldots,x_d))H.
 \end{split}
 \tag{Imaginary-carrier}
\]
The certificate is finite and fixed as \(N\) varies; set \(H=c\) when \(K=0\).
Indices may repeat, and all factors may share background variables and be dependent.
There is no reversal or transpose-symmetry restriction on \(Q\), \(Q_\nu\), or \(H\).
The requirement that \(Q_\nu\) omit both \(x_1\) and \(x_{j_\nu}\) is substantive: it gives the conditional independence used for its floor, while keeping \(H\) independent of the final exposed input.

For every fixed \(\lambda\in\mathbb C\), the proposed conclusion, proved below, is
\[
 \frac1N\log|\det(R(W^{(N)})-\lambda I)|
   \longrightarrow \tau\log|R(s)-\lambda|\in\mathbb R
       \quad\text{in probability as even }N\to\infty,
 \tag{Imaginary-carrier-even-log}
\]
and
\[
 \limsup_{N\to\infty}\frac1N\log|\det(R(W^{(N)})-\lambda I)|
   =\tau\log|R(s)-\lambda|\quad\text{almost surely}
 \tag{Imaginary-carrier-limsup}
\]
under every allowed coupling across dimensions.
The assertion includes \(\lambda=0\), with a finite target.
The [two-sided, polynomial and finite-product conclusions](#imaginary-carrier-closures) have the same even-probability and full-sequence-limsup scope.
No full-sequence probability limit or even-dimensional almost-sure limit is asserted for this general class.

<a id="transpose-polynomial-dichotomy"></a>
### The transpose operation and nonvanishing after semicircular substitution

On \(\mathbb C\langle x_1,\ldots,x_d\rangle\), define the complex-linear involutive anti-automorphism \(\#\) by
\[
 c^\#=c,\qquad x_j^\#=-x_j,\qquad
 (UV)^\#=V^\#U^\#.
\]
It reverses words and multiplies a word of length \(r\) by \((-1)^r\), without conjugating its coefficient.
Thus \(P(W)^T=P^\#(W)\) exactly, and
\[
 \mathfrak S(P):=\frac{P+P^\#}{2},\qquad
 \operatorname{sym}P(W)=\mathfrak S(P)(W).
 \tag{Transpose-polynomial}
\]
Here \(\operatorname{sym}A=(A+A^T)/2\) is unrelated to the Hermitian part \((A+A^*)/2\).
The operation \(\#\) is formal; no transpose operation on the ambient free von Neumann algebra is assumed.

A nonzero scalar free polynomial \(P\) cannot vanish at the free standard semicircular tuple.
Here is an explicit proof at the precise algebraic scope needed.
Let \(\mathcal F=\mathbb C\Omega\oplus\bigoplus_{r\ge1}(\mathbb C^d)^{\otimes r}\), let \(\ell_j\) prepend the basis vector \(e_j\), and put \(S_j=\ell_j+\ell_j^*\).
Expanding a vacuum word shows that its nonzero terms are exactly the color-respecting noncrossing creation-annihilation pairings: an annihilation must remove the current leftmost tensor of the same color, and the word must end at the vacuum.
Each such term has value one.
These are exactly the joint moments of a free standard semicircular tuple, the same colored-pairing convention used in [C_F0186_v4's bounded moment argument](../claims/Yin_C_F0186_v4.md#bounded-moments).
Consequently \(\tau(P(s)^*P(s))=\|P(S)\Omega\|^2\).
If the largest degree in \(P\) is \(r\), the grade-\(r\) component of \(P(S)\Omega\) is
\[
 \sum_{i_1,\ldots,i_r}
    p_{i_1\cdots i_r}\,e_{i_1}\otimes\cdots\otimes e_{i_r},
\]
where the coefficients are those of its degree-\(r\) words after equal words have been combined.
Only the all-creation term of each such word reaches that grade, so this vector is nonzero.
The degree-zero case is immediate.
This proves \(\tau(P(s)^*P(s))>0\), hence \(P(s)\ne0\), without an algebraic-freeness theorem being imported without proof.

It follows that if \(P\) is formally nonzero, there are fixed \(a>0\) and \(\delta>0\) such that, with probability tending to one,
\[
 s_{\lfloor\delta N\rfloor}(P(W))\ge a.
 \tag{Polynomial-bulk}
\]
Indeed the nonzero positive operator \(|P(s)|\) has positive spectral mass above some positive threshold, by faithfulness of \(\tau\).
Choose a smaller threshold at a continuity point of its law, and then a smaller positive \(\delta\).
The fixed-polynomial Hermitized weak law in [C_F0186_v4](../claims/Yin_C_F0186_v4.md#row-concentration) makes the number of singular values above that threshold at least \(\delta N\), eventually almost surely under every allowed coupling.
This proves the displayed probability statement as well; no quantitative convergence rate or inverse of \(P(s)\) is required.
The same reasoning applies to a polynomial in any subtuple of the background variables.

Two elementary singular-value facts will be used.
For the principal compression \(A_i\) obtained by deleting one coordinate from an \(N\)-by-\(N\) matrix \(A\),
\[
 s_k(A_i)\ge s_{k+2}(A)\qquad(1\le k\le N-2).
 \tag{Compression-quantile}
\]
To verify this, let \(P_i\) be the coordinate projection and embed \(A_i\) as \(P_iAP_i\), with one extra zero singular value.
The difference \(A-P_iAP_i=(I-P_i)A+P_iA(I-P_i)\) has rank at most two.
Intersecting the singular-value min-max subspace with its kernel proves the displayed rank-two inequality.
Also
\[
 s_k(BAC)\le\|B\|\,\|C\|\,s_k(A),
 \tag{Bounded-multipliers}
\]
by applying \(B\) and \(C\) to a best rank-\((k-1)\) singular-value truncation of \(A\).
These statements require neither normality nor symmetry.

For every fixed polynomial \(P\) of degree \(D\ge1\), [C_F0186_v4's power tail](../claims/Yin_C_F0186_v4.md#positive-tail) gives
\[
 \mathbb P\{\|P(W)\|>N^M\}\le C_PN^{1-2M/D}.
 \tag{Carrier-norm}
\]
Choose \(M\) sufficiently large to make any prescribed polynomial failure bound; constant polynomials are immediate.
All degrees and the finite lists of polynomials below are fixed.

<a id="imaginary-factor-floors"></a>
### Every certified factor has a floor along even dimensions

Fix a factor \(T_\nu\), and condition only on the input matrices other than \(W_{j_\nu}\).
Its shift \(Q_\nu(W)\) is independent of \(W_{j_\nu}\), and (Carrier-norm) supplies a polynomial entry guard with probability tending to one.
Put \(S_\nu=\mathfrak S(Q_\nu)\).
If \(S_\nu\) is the zero polynomial, \(Q_\nu(W)\) is exactly complex transpose-skew in every dimension.
The adopted [C_F0194_v7 even skew floor](../claims/Yin_C_F0194_v7.md#even-floor), integrated over the independent shift on its entry guard, gives a fixed exponent \(b_\nu>0\) such that
\[
 \mathbb P\{s_{\min}(T_\nu(W))<N^{-b_\nu}\}\longrightarrow0
       \quad\text{through even }N.
 \tag{Factor-even-floor}
\]
In this branch the error can in fact be any prescribed inverse power after increasing the exponent.

If \(S_\nu\) is formally nonzero, (Polynomial-bulk) gives at least \(\delta_\nu N\) singular values of \(\operatorname{sym}Q_\nu(W)\) above a fixed \(a_\nu>0\), with probability tending to one.
For \(k_N=4\lfloor\sqrt N\rfloor+1\), eventually \(k_N+2\le\lfloor\delta_\nu N\rfloor\).
Because the exposed matrix has zero diagonal and is transpose-skew, the symmetric part of every actual principal minor of \(T_\nu(W)\) is exactly the corresponding compression of \(\operatorname{sym}Q_\nu(W)\).
By (Compression-quantile), all those minors simultaneously have their \(k_N\)-th singular value at least \(a_\nu\ge N^{-1}\), eventually on the bulk event.
Apply the adopted [C_F0194_v7 quantile floor](../claims/Yin_C_F0194_v7.md#quantile-guard-floor) with \(L_0=1\), then add the entry-guard and bulk-event failure probabilities.
This proves (Factor-even-floor), in this branch actually through all dimensions.
This application conditions on the independent shift alone, not on the intersection of the norm or spectral guards.
Equivalently the uniformly bounded conditional probability of the least-value failure intersected with the guards is integrated, and their unconditional failure probabilities are then added.

There are only finitely many factors, so a union bound and
\(s_{\min}(UV)\ge s_{\min}(U)s_{\min}(V)\) give a fixed \(b_H>0\) with
\[
 \mathbb P\{H(W)\text{ is invertible and }
          \|H(W)^{-1}\|\le N^{b_H}\}\longrightarrow1
       \quad\text{through even }N.
 \tag{H-even-inverse}
\]
The fixed nonzero factor \(c\) is absorbed by increasing \(b_H\); \(K=0\) is direct.
No independence between the factors, or conditional floor after conditioning on their common good event, is used.

<a id="imaginary-carrier-floor"></a>
### The inverse shift reduces to one fixed polynomial

Fix \(\lambda\in\mathbb C\).
Choose a fixed \(M>0\) so that \(\|H(W)\|,\|Q(W)\|\le N^M\) outside a probability tending to zero, and let
\[
 J_N=\{H(W)\text{ invertible},\ \|H(W)^{-1}\|\le N^{b_H},
                 \ \|H(W)\|,\|Q(W)\|\le N^M\}.
\]
This event depends only on the background inputs \(W_2,\ldots,W_d\), and \(\mathbb P(J_N^c)\to0\) through even dimensions by (H-even-inverse) and (Carrier-norm).
Define a background-measurable shift in every dimension and on the whole probability space by
\[
 F_N=
 \begin{cases}
 Q(W)-\lambda H(W)^{-1},&J_N,\\
 0,&J_N^c.
 \end{cases}
 \tag{Background-shift}
\]
It is independent of the whole exposed matrix \(W_1\), and for a sufficiently large fixed \(\gamma\), \(\|F_N\|\le N^\gamma\) deterministically for all sufficiently large \(N\).
The finite-dimensional inverse on the open set of invertible matrices is continuous, so this extension is measurable.
On \(J_N\),
\[
 R(W)-\lambda I=(W_1+F_N)H(W).
 \tag{Carrier-factorization}
\]

Introduce the fixed background polynomial
\[
 K_\lambda=H^\#\mathfrak S(Q)H-\lambda\mathfrak S(H).
 \tag{Carrier-transpose-polynomial}
\]
For every invertible finite matrix \(H=H(W)\), the exact identity on \(J_N\) is
\[
 \begin{split}
 H^T\operatorname{sym}(F_N)H
 &=H^T\operatorname{sym}(Q(W))H
   -\frac\lambda2 H^T(H^{-1}+H^{-T})H\\
 &=H^T\operatorname{sym}(Q(W))H
   -\frac\lambda2(H^T+H)
 =K_\lambda(W).
 \end{split}
 \tag{Inverse-transpose-identity}
\]
The scalar is \(\lambda\), not \(\bar\lambda\), because ordinary transpose is complex-linear.
This identity does not use or assert an inverse of \(H(s)\).

If \(K_\lambda\) is formally zero, invertibility of \(H(W)\) makes \(\operatorname{sym}F_N=0\) on \(J_N\); the extension is also skew on \(J_N^c\).
The even skew floor therefore supplies a polynomial least-value floor for \(W_1+F_N\) through even dimensions.
It applies to its globally defined independent shift with the deterministic polynomial entry bound just verified.

If \(K_\lambda\) is formally nonzero, (Polynomial-bulk) supplies fixed \(a,\delta>0\) and an event \(B_N\), with \(\mathbb P(B_N^c)\to0\), on which
\(s_{\lfloor\delta N\rfloor}(K_\lambda(W))\ge a\).
On \(J_N\cap B_N\), (Inverse-transpose-identity), (Bounded-multipliers), and \(\|H^T\|=\|H\|\) give
\[
 s_{\lfloor\delta N\rfloor}(\operatorname{sym}F_N)
       \ge aN^{-2M}.
\]
Choose the fixed exponent \(L_0=2M+1\).
By (Compression-quantile) and \(k_N+2\le\lfloor\delta N\rfloor\) eventually, the symmetric part of every actual principal minor of \(W_1+F_N\) has its \(k_N\)-th singular value at least \(N^{-L_0}\) on \(J_N\cap B_N\).
Here the symmetric part of \(W_1\) is exactly zero, including its diagonal.
The quantile floor yields the desired least-value probability bound intersected with this guard.
Adding \(\mathbb P(J_N^c)+\mathbb P(B_N^c)\), which tend to zero along even dimensions, gives a fixed \(A_\lambda>0\) such that
\[
 \mathbb P\{s_{\min}(W_1+F_N)<N^{-A_\lambda}\}\longrightarrow0
        \quad\text{through even }N.
 \tag{Inverse-shift-even-floor}
\]
This does not condition on \(J_N\), \(B_N\), or their intersection with the quantile guard; the random-shift theorem is applied by conditioning only on the complete background-measurable \(F_N\).
Its constants are uniform in that shift, and the guard failure is bounded by the displayed background failure probabilities.

The formal-zero and formal-nonzero alternatives exhaust all \(K_\lambda\), since the Fock argument excludes a formally nonzero polynomial with zero semicircular evaluation.
Combining (Carrier-factorization), (H-even-inverse), and (Inverse-shift-even-floor) gives a fixed \(b_\lambda>0\) with
\[
 \mathbb P\{s_{\min}(R(W)-\lambda I)<N^{-b_\lambda}\}
       \longrightarrow0\quad\text{through even }N.
 \tag{Carrier-even-floor}
\]
This works for every certificate (Imaginary-carrier), including repeated exposed background indices, \(K=0\), and \(\lambda=0\).
It requires no dichotomy or nonvanishing test on the random finite matrix \(K_\lambda(W)\) itself.

<a id="imaginary-carrier-log"></a>
### Intermediate values and the logarithmic conclusion

Set \(q_N=\lceil N^{3/4}\rceil\), write singular values increasingly as \(a_r\), and put \(L=K+1\).
Apply the accepted [C_F0187_v2 intermediate theorem](../claims/Yin_C_F0187_v2.md#statement) to each \(T_\nu(W)\), conditioned only on all inputs other than its exposed \(W_{j_\nu}\), and to \(W_1+F_N\), conditioned only on the background.
The law of each exposed matrix is its original fixed purely imaginary law with zero diagonal.
The theorem permits an arbitrary independent complex shift without any norm guard.
Its constants are uniform in each realization of that shift.
For the finite list of factors, a union bound gives, outside a summable probability \(CN^2e^{-cN^{1/4}}\),
\[
 a_r(T_\nu(W)),\ a_r(W_1+F_N)
       \ge c(r-1)/N\qquad(q_N+1\le r\le N),
 \tag{Carrier-factor-middle}
\]
where \(c>0\) may be decreased to accommodate the finitely many fixed laws.
The summability here does not make \(J_N^c\) or the quantile-floor errors summable.

For square matrices, the singular-value min-max inequality
\[
 a_{r+s-1}(UV)\ge a_r(U)a_s(V),\qquad r+s-1\le N,
\]
is proved at its singular-matrix scope in [C_F0186_v6](../claims/Yin_C_F0186_v6.md#argument).
Iterating it for the \(L\) factors, and taking \(r=\lfloor k/L\rfloor\), gives on \(J_N\) and (Carrier-factor-middle)
\[
 a_k(R(W)-\lambda I)\ge c_1(k/N)^L
       \qquad(2L(q_N+1)\le k\le N)
 \tag{Carrier-middle}
\]
for a fixed \(c_1>0\), absorbing \(|c|\).
Indeed the iterated index is \(L(r-1)+1\le k\), while \(r-1\ge k/(2L)\) throughout this range for all sufficiently large \(N\).
This is a product singular-value statement and does not require independent factors.
Together with (Carrier-even-floor), it supplies both bounds on an event of probability tending to one along even dimensions.

For completeness, these bounds justify the finite free logarithm rather than assuming it.
Let \(\mu_N\) be the singular law of the fixed polynomial \(P(W)=R(W)-\lambda I\), and let \(\mu\) be that of \(|R(s)-\lambda|\).
The fixed-polynomial weak law in C_F0186_v4 gives \(\mu_N\Rightarrow\mu\) in probability, including along even dimensions.
On the middle event,
\[
 \mu_N([0,t])\le\frac{2L(q_N+1)}N+C t^{1/L},\qquad t>0,
\]
after harmless enlargement of the fixed constant.
At each continuity point the empirical count converges in probability to its deterministic limiting count, while the displayed upper bound holds with probability tending to one.
Passing first at those points and then downwards through continuity points yields \(\mu([0,t])\le C t^{1/L}\).
Thus \(\mu(\{0\})=0\) and \(\int_0^1|\log t|\,d\mu(t)<\infty\).
The free operator is bounded, so its positive logarithm is also integrable.

On the floor-and-middle event the bottom \(2L(q_N+1)\) normalized negative logarithms are at most \(O(N^{-1/4}\log N)\).
The remaining values below \(t<1\) contribute at most \(C't^{1/L}(1+|\log t|)+o(1)\), by summing \(-\log[c_1(k/N)^L]\) over \(k\le C Nt^{1/L}+O(N^{3/4})\).
Equivalently, fix a small index fraction first and then a smaller singular cutoff; the integral comparison \(N^{-1}\sum_{k\le\varepsilon N}\log(N/k)\le\varepsilon(1-\log\varepsilon)+o(1)\) gives the same vanishing bound.
Negative logarithmic tails therefore vanish in probability as the cutoff tends to zero along even dimensions.
The [positive-tail control in C_F0186_v4](../claims/Yin_C_F0186_v4.md#positive-tail) handles the upper cutoff.
Convergence for the continuous logarithm clipped at two fixed positive cutoffs, followed by removal of both tails, proves (Imaginary-carrier-even-log).
This is also an instance of the exact [probability-level transfer in C_F0186_v11](../claims/Yin_C_F0186_v11.md#norm-and-log-transfer), now with its two singular-value hypotheses supplied at the new pure-imaginary scope.

For every fixed positive regularizer, the accepted regularized logarithmic convergence in C_F0186_v4 holds almost surely under every cross-size coupling.
Since \(\log t\le\frac12\log(t^2+\varepsilon^2)\), intersecting a countable sequence \(\varepsilon\downarrow0\) gives the full-sequence almost-sure upper bound by \(\tau\log|R(s)-\lambda|\).
Select a deterministic subsequence of even dimensions along which the probability of deviation by more than \(1/m\) in (Imaginary-carrier-even-log) is at most \(2^{-m}\).
First Borel--Cantelli gives convergence to the same finite target along that subsequence under every allowed coupling.
Together these prove (Imaginary-carrier-limsup), equivalently the applicable [C_F0190_v1 lower-deviation criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion).
No summability of the quantile-floor error, and no independence across sizes, is used.

<a id="imaginary-carrier-closures"></a>
### Two-sided carriers, polynomial images and finite ordered products

Let \(H_{\mathrm L},H_{\mathrm R}\) be fixed scalar polynomials omitting \(x_1\), and suppose \(H_{\mathrm R}H_{\mathrm L}\) has certificate (Imaginary-carrier) for \(H\).
Set
\[
 \widetilde R=H_{\mathrm L}(x_1+Q)H_{\mathrm R},\qquad
 R=(x_1+Q)H_{\mathrm R}H_{\mathrm L}.
\]
For \(U=H_{\mathrm L}(W)\), \(V=(W_1+Q(W))H_{\mathrm R}(W)\), the identity \(\det(UV-\lambda I)=\det(VU-\lambda I)\) holds for every \(\lambda\), including zero.
At the free level, [the bounded cyclic determinant identity in C_F0186_v4](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) gives \(\Delta(uv-\lambda)=\Delta(vu-\lambda)\) for \(\lambda\ne0\).
At zero it follows from [bounded FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation), including zero determinant values.
Thus both logarithmic conclusions for \(\widetilde R\) follow from those for \(R\), with the same finite target.
No independent factor certificate, finite-dimensional inverse, or free inverse for \(H_{\mathrm L}\) or \(H_{\mathrm R}\) is required.

For either carrier form and any fixed scalar polynomial \(g\), if \(g(t)-\lambda\) is nonconstant, factor it over \(\mathbb C\) as
\[
 g(t)-\lambda=b\prod_{h=1}^r(t-\alpha_h),\qquad b\ne0,
\]
with roots counted with multiplicity.
Finite determinants and bounded FK multiplicativity give the corresponding sums of logarithms, with constant \(\log|b|\), in finite dimensions and at the free limit.
Every root parameter \(\alpha_h\) has the even-dimensional probability conclusion above, so a finite union bound proves that conclusion for \(g(R)-\lambda\), with a finite target.
The full-sequence upper bound applies to this new fixed polynomial itself, and the deterministic even subsequence argument gives its full-sequence almost-sure limsup equality.
One does not add separate limsup equalities.
If \(g(t)-\lambda\) is a nonzero constant, both logarithms equal its scalar logarithmic modulus identically.
If it is identically zero, both are identically \(-\infty\).

Finally let \(S=\prod_{h=1}^q g_h(R_h)\) be any fixed finite ordered product of these one-sided or two-sided carriers, allowing different exposed indices, shared inputs and noncommuting factors.
If all \(g_h\) are nonzero polynomials, determinant multiplicativity expresses the normalized finite logarithm at zero as a finite sum converging in probability along the same even dimensions.
Bounded FK multiplicativity identifies its finite target with \(\tau\log|S(s)|\).
Apply the full-sequence upper regularizer bound to the fixed polynomial \(S\) and the same deterministic subsequence argument to obtain its full-sequence limsup equality.
A zero polynomial factor makes \(S=0\) and both logarithms \(-\infty\); the empty product is the identity and has logarithm zero.
No nonzero-shift conclusion for a general ordered product is obtained by this zero-shift factorization.

All conclusions are for each fixed tuple of laws, certificate, polynomial and scalar parameter; simultaneous finitely many uses follow by finite intersection.
No event simultaneous over an uncountable parameter family is asserted.
The all-negative formal transpose evaluation used above depends on the zero-diagonal and purely imaginary assumptions on every background input; it does not silently transfer to arbitrary diagonals or mixed background laws.
Nor does the certificate condition cover an arbitrary scalar noncommutative polynomial or a matrix-coefficient polynomial.
Odd dimensions cannot in general be added to the probability conclusion: the allowed carrier \(R=x_1\) at \(\lambda=0\) is singular in every odd dimension, while its free logarithm is finite.
This obstruction is consistent with, and does not prevent, the full-sequence limsup conclusion.

<a id="signed-transpose-carriers"></a>
### Extension to inputs with fixed transpose signs

There is a further exact extension within the original centered finite-second-moment model, for which every step of the preceding argument can be checked.
Assign a deterministic sign \(\sigma_j\in\{+1,-1\}\) to each input.
For \(\sigma_j=+1\), let \(W_j\) be a real symmetric Wigner input with centered variance-one real strict upper law and any fixed centered real finite-second-moment diagonal law, independent of its upper entries.
For \(\sigma_j=-1\), let \(W_j\) have the purely imaginary strict upper law and identically zero diagonal in (Imaginary-tuple).
The complete entry families and inputs remain independent within each dimension, with arbitrary coupling across dimensions.
Thus every realization satisfies \(W_j^T=\sigma_jW_j\).
The diagonal freedom in the positive-sign class is within the original model; no noncentered diagonal extension is being added here.

Take precisely the finite carrier certificate (Imaginary-carrier), now permitting either sign at the active and factor-exposure indices and at every background index.
Every \(Q_\nu\) still omits both the active input and its own exposed input.
All even-dimensional probability, finite-target, full-sequence almost-sure limsup, two-sided, polynomial-image, finite ordered zero-shift product, and constant-case conclusions above hold unchanged.
The proof requires the following explicit substitutions, not a claim that a purely imaginary least-value floor holds for every shift.

Define the complex-linear involutive anti-automorphism \(\#_\sigma\) by
\[
 c^{\#_\sigma}=c,\qquad x_j^{\#_\sigma}=\sigma_jx_j,
 \qquad(UV)^{\#_\sigma}=V^{\#_\sigma}U^{\#_\sigma},
 \qquad\mathfrak S_\sigma(P)=\frac{P+P^{\#_\sigma}}2.
\]
Multiplication of a reversed word by the product of its input signs gives \(P(W)^T=P^{\#_\sigma}(W)\) exactly.
The free limit is still a free standard semicircular tuple by C_F0186_v4, so the Fock nonvanishing proof and (Polynomial-bulk) are unchanged for every formally nonzero scalar polynomial produced by this operation.
The rank-two compression bound and polynomial norm guards also do not depend on the signs.

At a factor-exposure index \(j_\nu\) with \(\sigma_{j_\nu}=+1\), the original real upper law is eligible in C_F0186_v11: its variance one implies \(\mathbb P(\operatorname{Re}\xi_{j_\nu}\ne0)>0\).
Use its accepted [eligible floor interface](../claims/Yin_C_F0186_v11.md#floor-interfaces) for the independent polynomially bounded complex shift \(Q_\nu(W)\).
This supplies a polynomial floor in probability through all dimensions, in particular through even ones, without any symmetry restriction on that shift or vanishing-diagonal hypothesis on the exposed real input.
At an index with \(\sigma_{j_\nu}=-1\), put \(S_\nu=\mathfrak S_\sigma(Q_\nu)\) and repeat the exact two branches at [the factor floors](#imaginary-factor-floors): formal zero gives a skew shift and the even floor; formal nonzero gives a positive bulk and the quantile floor because this exposed input has zero symmetric part.
The presence of positive-sign background inputs does not enter that last equality, since it only uses the exposed input's negative sign and the identity \(\operatorname{sym}Q_\nu(W)=S_\nu(W)\).
The same finite union bound therefore supplies (H-even-inverse) and the same background event \(J_N\).

At the active index, use the globally defined independent shift (Background-shift) and its polynomial bound.
If \(\sigma_1=+1\), the eligible floor interface directly yields (Inverse-shift-even-floor), actually through every dimension where \(J_N\) has probability tending to one; only its even-dimensional probability is needed and established in general.
If \(\sigma_1=-1\), define
\[
 K_{\lambda,\sigma}
   =H^{\#_\sigma}\mathfrak S_\sigma(Q)H
           -\lambda\mathfrak S_\sigma(H).
\]
The matrix calculation (Inverse-transpose-identity) gives exactly \(H(W)^T\operatorname{sym}(F_N)H(W)=K_{\lambda,\sigma}(W)\) on \(J_N\).
Its formal-zero case gives a skew shift, and its formal-nonzero case supplies the same positive bulk and principal-minor quantile guard by the Fock, weak-law, norm and rank-two arguments already proved.
The exposed input's zero diagonal and negative transpose sign ensure that no additional symmetric noise term appears in these minors.
This proves (Inverse-shift-even-floor) and hence (Carrier-even-floor) at either active sign, without conditioning on a spectral or joint factor guard.

The original complex intermediate theorem allows both real and purely imaginary laws and their prescribed real diagonals.
Thus the same within-dimension conditioning on each independent shift proves (Carrier-factor-middle), and the deterministic product inequality proves (Carrier-middle).
The fixed-polynomial weak, positive-log and regularized controls have exactly the centered finite-second-moment hypotheses of this signed model.
Consequently [the complete logarithmic passage](#imaginary-carrier-log) applies unchanged, as do the algebraic determinant and bounded FK identities in [the closure argument](#imaginary-carrier-closures).
This completes the sign-class extension as proof development.
It still allows the all-negative carrier \(R=x_1\), so the odd-dimensional obstruction remains.
An arbitrary complex Hermitian background input generally has neither fixed transpose sign, and is not covered by this formal \(\#_\sigma\) argument.
