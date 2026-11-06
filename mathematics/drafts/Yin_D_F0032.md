---
author: Yin
---

# Two original boundary rows: cancelling geometry and conditional minor floors

This is ordinary proof development for Yin on 2026-11-05 within the original [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract) questions.
It tests whether retaining both original independent boundary rows removes the [conditional singular atom](../ledger/Yin_L_F0066_v5.md#actual-minor-singular-atom) obtained when the whole second input was fixed.
The answer is positive at that actual-minor geometry, with the exact scope and normalization proved below.
The general actual-minor case with a fixed inverse bound is now covered by the [reviewed C_F0194_v12 theorem](../claims/Yin_C_F0194_v12.md#decision-two-original-row-reviewed), whose complete proof stays in that fixed Claim.
The cancelling-minor finite-variance, arithmetic, exponential, resonance and neighbourhood conclusions below retain their distinct scope.
The [growing-inverse calculation](#polynomial-minor-inverse-guard) is continuing ordinary development, while the [zero-bulk boundary](#fixed-guard-at-zero-bulk) explains why a fixed inverse bound does not cover typical minors in the actual bounded model.
The direct small-ball source input beyond elementary moment and exponential Markov bounds is the accepted [MNV16 Theorem 1.6](../audits/literature/MNV16/Yin_U001.md#matching-rank), used at its stated real fair-sign scope.
The later zero-bulk comparison separately reuses the fixed bounded-model spectral-mass result identified there.
The previous [free-density certificate](../ledger/Yin_L_F0066_v5.md#identity-direction-free-density) supplies the finite free target for the same coefficients and is not repeated here.

<a id="two-row-model"></a>
## Exact conditioned model and Schur determinant

Set \(\alpha=\sqrt2\), \(\beta=1+\alpha\), and initially \(K=1\).
All diagonal laws are zero.
Fix \(N\ge2\), put \(n=N-1\), and condition on the two original principal minors only, at values \(A'=C\), \(B'=-C\), with \(C=C^T\in M_n(\mathbb R)\) and zero diagonal.
Keep both original boundary rows independent:
\[
 A=\begin{pmatrix}0&x^T\\x&C\end{pmatrix},\qquad
 B=\begin{pmatrix}0&y^T\\y&-C\end{pmatrix},\qquad
 x_i=a_i/\sqrt N,\quad y_i=b_i/\sqrt N.
 \tag{Two-rows}
\]
The pairs \((a_i,b_i)\) are independent across \(i\), and their two components have independent fixed centered variance-one real laws.
This is the actual conditional law whenever the prescribed minor pair is an atom of positive probability; for other fixed \(C\), the displayed border ensemble remains a precisely defined conditional model, without asserting positive probability of that exact minor relation in a continuous-law ensemble.
No typicality of the cancelling relation is assumed.

Write
\[
 u=x+y,\qquad v=x+\alpha y,\qquad D=(1-\alpha)C,
 \quad X=A+B,\quad Y=A+\alpha B,
 \quad L_N=\begin{pmatrix}X&I_N\\I_N&Y\end{pmatrix},
 \quad Q_N=YX-I_N.
\]
After placing the two exposed physical coordinates first, the exact physical minor, coupling and Schur complement are
\[
 \mathcal M=\begin{pmatrix}0&I_n\\I_n&D\end{pmatrix},\qquad
 \mathcal M^{-1}=\begin{pmatrix}-D&I_n\\I_n&0\end{pmatrix},\qquad
 R=\begin{pmatrix}u^T&0\\0&v^T\end{pmatrix},
\]
\[
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix}-R\mathcal M^{-1}R^T
  =\begin{pmatrix}u^TDu&1-u^Tv\\1-u^Tv&0\end{pmatrix}.
 \tag{Two-row-Schur}
\]
Thus, with \(q=u^Tv-1\),
\[
 \det S=-q^2,\qquad
 \det L_N=\det Q_N=(-1)^Nq^2,
 \qquad
 q=\frac1N\sum_{i=1}^n\psi(a_i,b_i)-1,
 \tag{Two-row-scalar-sum}
\]
where
\[
 \psi(a,b)=a^2+\alpha b^2+\beta ab.
\]
These identities hold for every \(C,x,y\); the scalar sum does not involve \(C\).
For example, the direct product is
\[
 Q_N=\begin{pmatrix}u^Tv-1&0\\Du&vu^T-I_n\end{pmatrix},
\]
and the rank-one determinant of the lower diagonal block gives the same squared identity.

<a id="two-row-floor-conversion"></a>
## The normalization needed for an actual singular-value floor

Put \(A_C=1+\|C\|\) and \(R_{x,y}=1+\|x\|+\|y\|\).
Constants in this section depend only on \(\alpha\).
The explicit inverse gives \(s_{\min}(\mathcal M)\ge c/A_C\), while
\[
 \|S\|\le C A_C R_{x,y}^2,
 \qquad
 s_{\min}(S)=\frac{|q|^2}{\|S\|}
 \ge\frac{c|q|^2}{A_C R_{x,y}^2}
 \quad(q\ne0).
\]
The exact block factorization is
\[
 L_N\simeq
 \begin{pmatrix}I_2&R\mathcal M^{-1}\\0&I_{2n}\end{pmatrix}
 \begin{pmatrix}S&0\\0&\mathcal M\end{pmatrix}
 \begin{pmatrix}I_2&0\\\mathcal M^{-1}R^T&I_{2n}\end{pmatrix},
\]
where \(\simeq\) denotes only the simultaneous physical-coordinate permutation.
The norms of the two triangular inverses are at most \(C A_C R_{x,y}\).
Consequently
\[
 s_{\min}(L_N)
 \ge\frac{c\min\{1,|q|^2\}}{A_C^3 R_{x,y}^4}.
 \tag{Two-row-normalized-floor}
\]
The same lower bound holds for \(s_{\min}(Q_N)\).
Indeed, after swapping auxiliary columns the pencil is \(\begin{psmallmatrix}I&X\\Y&I\end{psmallmatrix}\); when it is invertible, the lower-right block of its inverse is \((I-YX)^{-1}=-Q_N^{-1}\).
Hence \(\|Q_N^{-1}\|\le\|L_N^{-1}\|\), and the singular case follows by the zero lower bound.
This argument explicitly retains the minor inverse and graph factors; a determinant lower bound alone is not being read as a least-value estimate.

<a id="two-rademacher-calculation"></a>
## Two Rademacher rows: exact multilinearization and stronger bounds

First take \(a_i=\varepsilon_i\), \(b_i=\eta_i\), with all \(2n\) signs independent and fair.
Then
\[
 \psi(\varepsilon_i,\eta_i)=\beta(1+\varepsilon_i\eta_i),\qquad
 q=h_N+\frac\beta N\sum_{i=1}^n\zeta_i,
 \quad h_N=\frac{\beta n}{N}-1,
 \quad \zeta_i:=\varepsilon_i\eta_i.
 \tag{Rademacher-sum}
\]
The products \(\zeta_i\) are themselves independent fair signs.
If \(J\) is the number of products equal to one, then
\[
 J\sim\operatorname{Bin}(n,1/2),\qquad
 q=\frac{2\beta J}{N}-1.
 \tag{Exact-binomial}
\]
As a polynomial on the original \(2n\)-sign cube, the exact multilinearization of \(q^2\) is
\[
 h_N^2+\frac{\beta^2n}{N^2}
 +\frac{2h_N\beta}{N}\sum_i\varepsilon_i\eta_i
 +\frac{2\beta^2}{N^2}\sum_{i<j}\varepsilon_i\eta_i\varepsilon_j\eta_j.
 \tag{True-quartic-layer}
\]
For \(n\ge2\), its highest degree is four, with
\[
 \sigma_4^2=\binom n2\frac{4\beta^4}{N^4},\qquad
 \tau_4=\frac2n.
\]
Here \(\sigma_4^2\) is the sum of squared top-degree coefficients and \(\tau_4\) is the maximal coordinate load divided by that energy, as defined in the [typical-minor test](Yin_D_F0010.md#typical-minor-energy-matching).
There are explicitly \(\lfloor n/2\rfloor\) disjoint quartic monomials of modulus \(2\beta^2/N^2\), by pairing disjoint physical indices.
Thus this geometry supplies the required top-degree spread after both original rows are retained, whereas fixing the second border at the earlier atom collapsed the polynomial to one sign.
Rewriting in the independent signs \(\zeta_i\) makes the same expression degree two, with the same energy and load ratio and \(\lfloor n/2\rfloor\) disjoint quadratic coefficients.
For example, MNV16 at degree two gives
\[
 \sup_{z\in\mathbb C}\mathbb P\{|\det L_N-z|\le\rho\mid C\}
 \le C\sqrt{\log n}\,n^{-1/9},
 \qquad 0<\rho<\beta^2/N^2,
 \tag{Binomial-MNV-bound}
\]
for all sufficiently large \(N\).
The determinant is real, so projection of a complex disk onto the real line and the source's interval convention justify the same displayed center range.
This generic matching bound is weaker than the following direct conclusions at the actual center zero.

Since \(\beta=1+\sqrt2\), the number \(2\beta J-N\) is never zero.
Multiplying by its quadratic conjugate gives the nonzero integer
\[
 (2(1+\sqrt2)J-N)(2(1-\sqrt2)J-N)
 =N^2-4NJ-4J^2.
\]
The conjugate factor has modulus at most \((2\sqrt2-1)N\), since \(0\le J\le n\).
Therefore every row realization satisfies
\[
 |q|\ge\frac1{(2\sqrt2-1)N^2},\qquad
 s_{\min}(L_N),s_{\min}(Q_N)
 \ge\frac{cN^{-4}}{(1+\|C\|)^3}.
 \tag{Rademacher-arithmetic-floor}
\]
The last step uses \(R_{x,y}\le3\) in (Two-row-normalized-floor).
In particular exact conditional singularity has probability zero at every dimension, and an actual sign minor obeys \(\|C\|\le\sqrt N\), giving a deterministic floor \(cN^{-11/2}\).

There is also a stronger probabilistic floor.
For all sufficiently large \(N\), \(h_N\ge3\alpha/4\), so
\[
 \mathbb P\{q\le\alpha/2\mid C\}
 \le\mathbb P\left\{\sum_i\zeta_i\le-\frac{\alpha N}{4\beta}\right\}
 \le e^{-cN}.
\]
The last bound follows directly from \(\mathbb E e^{-s\zeta_i}=\cosh s\le e^{s^2/2}\) and exponential Markov optimization.
Consequently, uniformly over every fixed \(C\),
\[
 \mathbb P\left\{s_{\min}(L_N)<\frac c{(1+\|C\|)^3}\ \middle|\ C\right\}
 +\mathbb P\left\{s_{\min}(Q_N)<\frac c{(1+\|C\|)^3}\ \middle|\ C\right\}
 \le C e^{-cN}.
 \tag{Rademacher-summable-floor}
\]
Uniformly bounded cancelling minors therefore have a conditional constant floor outside summable failures, rather than a persistent singular atom.

<a id="original-atomic-law-restored"></a>
## Unfixing the second border also repairs the previous atomic-law example

The preceding exponential conclusion does not depend on the second input being Rademacher.
Retain the original first-input sign law and the exact finite-support second-input law in [the earlier construction](../ledger/Yin_L_F0066_v5.md#actual-minor-singular-atom), but now condition only on \(A'=C,B'=-C\).
Both borders remain independent and bounded, and the summands \(\psi(a_i,b_i)\) are independent bounded real variables with
\[
 \mathbb E\psi(a_i,b_i)=1+\alpha=\beta.
\]
For any fixed bounded centered variance-one pair of independent real laws, elementary exponential Markov applied near the origin gives
\(\mathbb P\{q\le\alpha/2\}\le C e^{-cN}\).
For completeness, boundedness makes
\(\mathbb E e^{-s(\psi-\mathbb E\psi)}=1+O(s^2)\)
as \(s\downarrow0\); a fixed sufficiently small \(s>0\) then controls any fixed lower deviation of the empirical average exponentially in \(n\).
The row norms are uniformly bounded, so (Rademacher-summable-floor), with law-dependent constants, holds for this original pair of laws as well.
Thus the probability-\(1/2\) singular atom was caused by fixing a rare second border, and disappears as a fixed-size atom when that independent border is retained.
It is not asserted that singularity is impossible for the original multivalued law.
Indeed the prescribed second border \(y=t e_1/\sqrt N\), followed by \(a_1=1\), still has probability \(p_0^{n-1}/16\) conditional on the two cancelling minors, and still makes the pencil singular.
This exponential lower bound is consistent with the exponential upper bound; no deterministic floor is claimed for that law.

<a id="finite-variance-two-row-floor"></a>
## A vanishing-error floor for arbitrary real finite-variance border laws

The exact scalar sum also yields a probability floor when the raw border laws have only the original finite second moments.
First \(Z:=\psi(a,b)\) is nonconstant.
If it were almost surely constant, four independent draws \(a,a',b,b'\) and the full product law would give almost surely
\[
 0=\psi(a,b)-\psi(a',b)-\psi(a,b')+\psi(a',b')
   =\beta(a-a')(b-b').
\]
Each input has nonzero variance, so the right side is nonzero with positive probability, a contradiction.
This argument uses the two retained independent original laws rather than a conditional variance of mixed factors.

Choose \(b_0,p>0\) with
\(\mathbb P\{|(Z-Z')/2|\ge b_0\}\ge p\)
for an independent copy \(Z'\).
Use independent two-copy representations
\[
 Z_i=c_i+d_i\epsilon_i,
 \qquad c_i=(Z_i^{(0)}+Z_i^{(1)})/2,
 \quad d_i=(Z_i^{(0)}-Z_i^{(1)})/2,
\]
with independent fair signs \(\epsilon_i\).
The represented \(Z_i\) have exactly their original independent laws.
An exponential indicator bound gives at least \(pn/2\) coefficients with \(|d_i|\ge b_0\), outside probability \(C e^{-cn}\).
Conditional on all copies, apply the second bound of MNV16 at degree one to the linear polynomial \(\sum_i d_i\epsilon_i/b_0\), whose constant term and other coefficients are unrestricted.
It follows that, for every real center \(w\),
\[
 \mathbb P\left\{\left|\sum_iZ_i-w\right|\le b_0/4\right\}
 \le C n^{-1/2},
\]
and hence
\[
 \mathbb P\{|q|\le b_0/(4N)\mid C\}\le C N^{-1/2}.
 \tag{Finite-variance-scalar-floor}
\]
This small-ball proof requires no second moment of \(Z\); the original second moments of \(a,b\) may leave \(Z\) with only a finite first moment.

For \(\gamma\ge0\), \(\theta>0\), restrict \(\|C\|\le N^\gamma\).
The actual row second moments imply
\[
 \mathbb E(\|x\|^2+\|y\|^2)=2n/N\le2,
 \qquad
 \mathbb P\{R_{x,y}>N^\theta\}\le C N^{-2\theta}
\]
for all sufficiently large \(N\).
No independence between this norm event and \(q\) is needed.
Using their union bound and (Two-row-normalized-floor) gives
\[
 \mathbb P\{s_{\min}(L_N)<cN^{-(2+3\gamma+4\theta)}\mid C\}
 +\mathbb P\{s_{\min}(Q_N)<cN^{-(2+3\gamma+4\theta)}\mid C\}
 \le C N^{-1/2}+C N^{-2\theta}.
 \tag{Finite-variance-cancelling-floor}
\]
The estimate is uniform over the displayed cancelling-minor class and gives convergence in probability of a polynomial floor.
Its main failure term is not summable, and no almost-sure full-sequence floor follows from it for arbitrary cross-size coupling.
The remaining intermediate singular range and bottom logarithm are not supplied by this conditional estimate.

<a id="two-row-critical-boundary"></a>
## A nearby coefficient resonance prevents a general summable claim

Changing \(K\) is not part of the preceding \(K=1\) result, but gives a precise boundary to extrapolation.
For \(K>0\) the same cancelling-minor calculation yields
\[
 \det L_N=(-1)^N K^{2N-4}(u^Tv-K^2)^2.
\]
With both border laws Rademacher and \(K^2=\beta\), exact singularity is equivalent to \(J=N/2\).
It is impossible for odd \(N\), whereas for even \(N\),
\[
 \mathbb P\{L_N\text{ singular}\mid C\}
 =2^{-(N-1)}\binom{N-1}{N/2}\asymp N^{-1/2}.
 \tag{Critical-binomial-atom}
\]
The upper bound follows from the same degree-one MNV16 estimate.
For the lower bound, the binomial mass is maximal at either central value; Chebyshev places a fixed positive mass in an interval of \(O(\sqrt N)\) integers around the mean, so this maximal mass is at least \(c/\sqrt N\).
The displayed conditional probabilities are not summable even along all even dimensions.
This does not refute an unconditional estimate for the original matrices, because the cancelling-minor event itself may be extremely rare.
It does show that preserving two fresh rows does not uniformly create arbitrary-power or summable failure bounds at every fixed coefficient tuple.

<a id="near-cancelling-minors"></a>
## A genuine neighbourhood of the cancelling geometry

For fixed bounded real input laws, the \(K=1\) exponential floor extends to actual minors close to cancellation.
Let now \(A'=C_1\), \(B'=C_2\), put
\[
 E=C_1+C_2,\qquad D=C_1+\alpha C_2,\qquad a_D=1+\|D\|,
 \qquad
 \mathcal M=\begin{pmatrix}E&I_n\\I_n&D\end{pmatrix}.
\]
The original independent borders and the coupling \(R\) remain as above.
Compare with \(\mathcal M_0=\begin{psmallmatrix}0&I_n\\I_n&D\end{psmallmatrix}\), for which \(\|\mathcal M_0^{-1}\|\le a_D\).
If \(\|E\|a_D\le1/2\), the inverse identity gives
\[
 \|\mathcal M^{-1}\|\le2a_D,
 \qquad
 \|\mathcal M^{-1}-\mathcal M_0^{-1}\|\le2a_D^2\|E\|.
\]
Bounded raw laws give a deterministic bound \(\|R\|\le C\).
On the event \(q\ge\alpha/2\), whose complement has probability at most \(C e^{-cN}\), the reference Schur complement obeys \(s_{\min}(S_0)\ge c/a_D\).
Moreover
\[
 \|S-S_0\|\le C a_D^2\|E\|.
\]
Choose a sufficiently small fixed \(c_0>0\), depending only on the bounded laws and \(\alpha\).
The actual-minor hypothesis
\[
 \|C_1+C_2\|
 \le c_0(1+\|C_1+\alpha C_2\|)^{-3}
 \tag{Near-cancellation-guard}
\]
ensures both inverse control and \(s_{\min}(S)\ge c/(2a_D)\) on that event.
The same triangular factorization then gives
\[
 \mathbb P\{s_{\min}(L_N)<c(1+\|D\|)^{-3}\mid C_1,C_2\}
 \le C e^{-cN}.
 \tag{Near-cancellation-floor}
\]
The scalar product reduction has the same floor by the inverse-block argument already given.
This is a uniform conditional estimate on an explicit neighbourhood of actual minors; it is not a statement that (Near-cancellation-guard) occurs typically.

<a id="general-minor-bridge"></a>
## What remains for a general actual minor

For an arbitrary invertible actual physical minor
\[
 \mathcal M=\begin{pmatrix}C_1+C_2&I_n\\I_n&C_1+\alpha C_2\end{pmatrix},
 \qquad \mathcal M^{-1}=(R_{ij})_{i,j=1}^2,
\]
the two-row Schur determinant is exactly
\[
 (u^TR_{11}u)(v^TR_{22}v)
       -(1-u^TR_{12}v)^2.
 \tag{General-two-row-quartic}
\]
The symmetry of \(\mathcal M^{-1}\) identifies the two off-diagonal scalar entries.
Here the quartic expression need not reduce to an independent scalar sum, and an arbitrary inverse block is not a substitute for these actual relations.
The cancelling test shows that the old bad-minor geometry becomes controllable after the second original row is restored, including a true nearby class; it also supplies an explicit top-degree matching certificate in the sign case.
The [reviewed fixed-inverse theorem](../claims/Yin_C_F0194_v12.md#statement) now covers every actual minor with a fixed bounded inverse and two original Rademacher borders.
Its [three-branch argument](../claims/Yin_C_F0194_v12.md#three-branches) handles low sign degree explicitly, rather than requiring spread in a uniformly nonzero fourth layer.
It neither places typical actual minors near cancellation nor bounds their inverse norms.
The remaining bridge is the probability of the inverse guard, its singular-minor complement and the other original off-diagonal laws; the calculations below make the first obstruction quantitative without asserting its resolution.
A suitable floor must still be joined to middle-range or direct bottom-logarithm control before F0013 or F0014 follows, and the full F0012 Brown conclusion retains its stronger requirements.

<a id="polynomial-minor-inverse-guard"></a>
## Tracking a polynomially growing minor inverse

This section explicitly retraces the constants in the [fixed-inverse proof](../claims/Yin_C_F0194_v12.md#argument); it is not an application of a fixed-\(M\) theorem with \(M\) silently replaced by \(M_N\).
This growing-\(M_N\) extension is ordinary proof development and is outside the fixed-\(M\) scope of that Claim's independent review.
Keep its \(\alpha=\sqrt2\), fixed nonzero real \(K\), actual minor, two original independent Rademacher borders, and original \(N^{-1/2}\) normalization.
Let \(M_N\ge1\) be deterministic and restrict the actual inverse by
\[
 \|\mathcal M^{-1}\|\le M_N.
 \tag{Growing-inverse-guard}
\]
Choose a constant \(d_K>0\), depending only on \(K\), sufficiently small that the exposed real diagonals satisfy the witness bound whenever
\[
 |a|+|b|\le \delta_N:=\frac{d_K}{1+M_N}.
 \tag{Growing-diagonal-guard}
\]
For example, take
\[
 d_K\le\min\left\{1,
 \frac{K^2}{4(1+\alpha+(\alpha-1)^2)}\right\}.
\]
Indeed \(\delta_N((1+\alpha)\delta_N+(\alpha-1)^2M_N)\le K^2/4\).
The anti-diagonal averaged witness therefore remains at distance at least \(3K^2/4\) from zero.

Use the sign coefficients \(p_E\), energies \(\sigma_d^2\), loads \(\Lambda_{i,d}\), and quadratic coefficient matrix \(\mathcal Q_2\) from the fixed proof.
The three quadratic-form matrices have operator norm at most \(C_K M_N\), and the three Schur-entry constants \(f_0,h_0,r_0\) have modulus at most \(C_K M_N\).
Thus the exact coefficient formulas there give the following explicit bounds:
\[
 \begin{split}
 \|\mathcal Q_2\|&\le C_K M_N^2/N,\qquad
 |p_{\{i,j\}}|\le C_K M_N^2/N,\\
 \Lambda_{i,2}&\le C_K M_N^4/N^2,\qquad
 \sigma_2^2\le C_K M_N^4/N,\\
 \Lambda_{i,4}&\le C_K M_N^4/N^3,\qquad
 \sigma_4^2\le C_K M_N^4/N^2,\qquad
 \operatorname{Var}p\le C_K M_N^4/N .
 \end{split}
 \tag{Growing-coefficient-bounds}
\]
For the fourth-degree load, the factors in each row-energy times total-energy product are respectively \(O_K(M_N^2)\) and \(O_K(NM_N^2)\), so the displayed \(M_N^4/N^3\) retains the full inverse dependence.
No eigenvector spread or cancellation of a large inverse mode is used.

Fix
\[
 0\le\kappa<\tfrac14,\qquad 1\le M_N\le N^\kappa.
 \tag{Polynomial-inverse-range}
\]
The original energy split \(N^{-5/2}\), if left unchanged, would only make the crude fourth-degree matching diverge for \(\kappa<1/8\).
Instead split at
\[
 T_N:=M_N^2N^{-5/2}.
 \tag{Growing-energy-split}
\]
If \(|p_0|\ge K^2/4\), the same constant-gap argument gives failure at most \(C_KM_N^4/N\) for \(|p|\le N^{-4}\).

In the branch \(\sigma_4^2\ge T_N\), retaining coefficients above
\[
 \lambda_4=\frac{\sigma_4}{\sqrt2(2n)^2}
       \ge c_K M_NN^{-13/4}
\]
preserves at least half of the fourth-layer energy.
The greedy matching removes at most \(C_KM_N^4/N^3\) per selected four-set, so it has
\[
 r_4\ge c_K\frac{\sigma_4^2N^3}{M_N^4}
      \ge c_K\frac{\sqrt N}{M_N^2}
      \ge c_K N^{1/2-2\kappa}.
 \tag{Growing-quartic-matching}
\]
This diverges uniformly in the displayed range, and \(2N^{-4}<\lambda_4\) eventually.
The accepted degree-four MNV estimate therefore bounds the small-ball probability by
\[
 C_{K,\kappa}\sqrt{\log N}\,
       N^{-(1-4\kappa)/34}.
 \tag{Growing-quartic-error}
\]
The dimension threshold may depend on \(\kappa\), but no unspecified \(M_N\)-dependent constant has been absorbed into this bound.

In the branch \(\sigma_4^2<T_N\), the sum of paired fourth coefficients has modulus at most
\[
 \sqrt{\binom n2}\,\sigma_4
 \le C M_NN^{-1/4}
 \le C N^{\kappa-1/4}=o(1).
 \tag{Growing-paired-error}
\]
When \(|p_0|<K^2/4\), the paired witness consequently forces \(\left|\sum_i p_{\{\epsilon_i,\eta_i\}}\right|\ge K^2/4=:a_*\) for large \(N\).
Keep the same quadratic threshold \(\lambda_2=a_*/(2N)\), rather than shrinking it by \(M_N^2\).
The upper bound \(C_KM_N^2/N\) on each coefficient then gives at least
\[
 r_2\ge c_K N/M_N^2\ge c_KN^{1-2\kappa}
\]
disjoint paired quadratic monomials above \(\lambda_2\).
The fourth-layer remainder is controlled at that quadratic scale:
\[
 \mathbb P\{|p_4|>\lambda_2/4\}
 \le C_K N^2\sigma_4^2
 \le C_KM_N^2/\sqrt N .
 \tag{Growing-remainder-error}
\]
The same interval inclusion as in the fixed proof and degree-two MNV give a bound
\[
 C_{K,\kappa}\sqrt{\log N}\,N^{-(1-2\kappa)/9}
       +C_KN^{-(1/2-2\kappa)} .
\]
Combining the three branches proves the following development conclusion, uniformly over the guarded actual minors and exposed diagonals:
\[
 \mathbb P_{\varepsilon,\eta}\{|p|\le N^{-4}\}
 \le C_{K,\kappa}\sqrt{\log N}\,
       N^{-(1-4\kappa)/34}.
 \tag{Growing-Schur-floor}
\]
The endpoint \(\kappa=1/4\) is not covered: the upper bounds for the paired fourth sum and the mean-gap error cease to vanish, and the guaranteed fourth matching need not diverge.
This is a boundary of these norm-only estimates, not a counterexample to a stronger theorem.

The least-value conversion has an additional explicit loss.
The sign rows still give \(\|R\|\le C\), while
\[
 \|S\|\le C_KM_N,\qquad
 \|\text{each triangular inverse}\|\le C_KM_N,\qquad
 s_{\min}(\mathcal M)\ge M_N^{-1}.
\]
The block factorization therefore yields
\[
 s_{\min}(L_N)\ge
 c_KM_N^{-3}\min\{1,|p|\},
 \qquad
 s_{\min}(Q_N)\ge |K|s_{\min}(L_N).
 \tag{Growing-normalization}
\]
Consequently
\[
 \begin{split}
 \mathbb P_{\varepsilon,\eta}\{&
 s_{\min}(L_N)\le c_KM_N^{-3}N^{-4}
 \ \hbox{or}\
 s_{\min}(Q_N)\le c_KM_N^{-3}N^{-4}\}\\
 &\le C_{K,\kappa}\sqrt{\log N}\,
       N^{-(1-4\kappa)/34}.
 \end{split}
 \tag{Growing-two-row-floor}
\]
In particular \(c_KN^{-(4+3\kappa)}\) is a common allowed floor.
The three inverse factors have not been omitted by interpreting a determinant gap directly as a least singular value.

For one fixed exposed index with the original finite-second-moment diagonal laws, the new shrinking diagonal guard has failure probability at most
\[
 \mathbb P\left\{\frac{|\zeta_1|+|\zeta_2|}{\sqrt N}>\delta_N\right\}
 \le C_K\bigl(\mathbb E|\zeta_1|^2+\mathbb E|\zeta_2|^2\bigr)
        \frac{M_N^2}{N}
 \le C_{K,\zeta}N^{-(1-2\kappa)}.
 \tag{Growing-diagonal-error}
\]
For bounded raw diagonal laws this guard holds deterministically for all sufficiently large \(N\), since \(\kappa<1/2\); zero diagonals satisfy it identically.
Let \(\mathcal G_N(M_N)\) denote invertibility and (Growing-inverse-guard) for the actual minor.
Integrating (Growing-two-row-floor) gives the same bound plus (Growing-diagonal-error) for the floor event intersected with \(\mathcal G_N(M_N)\).
The unrestricted event still requires adding \(\mathbb P(\mathcal G_N(M_N)^c)\), which includes both singular minors and inverse norms above \(M_N\).
No division by the probability of the minor event, union over all exposed positions, or control of this new bad-minor event is implicit.

<a id="fixed-guard-at-zero-bulk"></a>
## Fixed inverse guards are atypical in the actual zero-bulk model

The [reviewed bounded two-channel result](../claims/Yin_C_F0187_v4.md#decision-bounded-two-channel-reviewed) applies to the actual \(K=1\) model with independent fixed bounded real centered variance-one off-diagonal laws and fixed bounded centered real diagonal laws.
In particular it includes two Rademacher inputs with zero diagonals and retains the original \(N^{-1/2}\) normalization after physical deletions.
The [positive channel mass](../claims/Yin_C_F0187_v4.md#positive-channel-mass) and its [uniform weighted minor consequence](../claims/Yin_C_F0187_v4.md#weighted-minor-mass) give, for each fixed \(0<\delta<\delta_0\),
\[
 \operatorname{Tr}\Pi_\ell
      \mathbf1_{[-\delta,\delta]}(\mathcal M_{N,S})
 \ge c_1\delta(N-|S|),\qquad \ell=1,2,
 \tag{Retained-channel-mass}
\]
simultaneously over \(|S|\le1\), outside probability at most \(C_\delta N^2e^{-c_\delta N}\) for all sufficiently large \(N\).
The cited proof even allows two physical deletions, but the single-deletion scope already suffices here.
Only this fixed-scale mass conclusion is used in the following deduction, not its separate eigenvector or inverse-residual conclusions.

Fix \(M\ge1\), and choose \(0<\delta<\min\{\delta_0,1/M\}\).
On (Retained-channel-mass), every such minor has an eigenvalue in \([-\delta,\delta]\).
If it is singular it is outside the inverse guard; otherwise the real symmetric spectral theorem gives
\[
 \|\mathcal M_{N,S}^{-1}\|\ge1/\delta>M.
\]
It follows that
\[
 \begin{split}
 \mathbb P\{\exists S,\ |S|\le1:\ 
 &\mathcal M_{N,S}\text{ is invertible and }
 \|\mathcal M_{N,S}^{-1}\|\le M\}\\
 &\le C_\delta N^2e^{-c_\delta N}\longrightarrow0 .
 \end{split}
 \tag{Fixed-guard-atypical}
\]
Thus the fixed-\(M\) conditional floor does not describe a typical minor at this actual bulk point, even in its exact Rademacher submodel.
Its conditional conclusion remains valid; the guard itself occupies a vanishing-probability part of that ensemble.

The growing-inverse calculation enlarges the guarded class to \(M_N=N^\kappa\), \(\kappa<1/4\), but supplies no probability estimate for that class.
In particular (Retained-channel-mass) cannot be used with \(\delta=N^{-\kappa}\): its expectation approximation threshold and concentration constants are asserted only after fixing \(\delta\).
Positive mass in every fixed neighbourhood proves the displayed vanishing probability for the intersection of invertibility with each fixed inverse guard.
It gives neither a power-law escape rate nor a statement obtained by conditioning on invertibility.
To decide whether the new guard captures typical minors, one needs quantitative spectral control at the shrinking scale \(N^{-\kappa}\), or a row argument normalized so that large inverse modes and singular minors no longer enter through this guard.
The present calculation establishes neither alternative.
The non-summable error and the remaining logarithmic obligations therefore persist.

<a id="graph-normalized-block-distance"></a>
## Fixed graph normalization of a physical column distance

The complete [graph isometry and distance identity](../claims/Yin_C_F0194_v13.md#graph-distance) are retained in the [reviewed graph-energy reduction](../claims/Yin_C_F0194_v13.md#decision-graph-energy-reviewed).
For real symmetric \(L=\begin{pmatrix}A&B^T\\B&M\end{pmatrix}\) with invertible \(M\), the distance matrix is \(D:=\Gamma^{-1/2}S\), where \(S:=A-B^TM^{-1}B\) and \(\Gamma:=I_2+B^TM^{-2}B\).
This is a one-sided normalization of the exposed-column distance, with \(\|D\|\le\|L\|\) and \(\det D=\det S/\sqrt{\det\Gamma}\).

The earlier growing-inverse calculation has the direct consequence \(\sqrt{\det\Gamma}\le1+B_0^2M_N^2\) when \(\|B\|\le B_0\) and \(\|M^{-1}\|\le M_N\).
On a fixed full-matrix norm guard it therefore gives distance scale \(cM_N^{-2}N^{-4}\) from that Schur small-ball estimate.
This is a distance bound, and the many-index step remains necessary to infer a whole-matrix bound.

<a id="single-pole-graph-area"></a>
## Fixed graph area at the inverse-mode scale

The [fixed largest-mode graph-area proof](../claims/Yin_C_F0194_v13.md#pole-area) retains the exact rank-one update and gives area at most \(C|q|\mathcal R\) on its stated residual-size conditions.
It imposes neither a polynomial upper bound on \(|q|\) nor dominance for the graph estimate.
The [fixed coefficient argument](../claims/Yin_C_F0194_v13.md#dominant-coefficients) uses dominance only to control complete fourth-layer cancellation.
The general graph-energy interface and its finite-interval scale are stated in [the fixed theorem](../claims/Yin_C_F0194_v13.md#statement).

<a id="graph-distance-to-matrix-assembly"></a>
## Fixed averaging and the remaining minor exception

The complete [physical-block average](../claims/Yin_C_F0194_v13.md#block-averaging) converts the conditional distance estimate into matrix scale \(c b_N^{-2}N^{-5}\) without multiplying the small-ball error by \(N\).
The [dominant-mode application](../claims/Yin_C_F0194_v13.md#dominant-branch-statement) retains the average singular-or-nondominant minor term.
The [combined application](../claims/Yin_C_F0194_v13.md#combined-branch-statement) also uses the high-effective-rank energy theorem, leaving only singular minors or invertible minors in neither coefficient branch.
Neither average has been proved to vanish; the result is not an unconditional floor or a determinant theorem.
The following example remains useful because one prescribed block distance cannot replace that average.

<a id="single-block-distance-obstruction"></a>
## A single well-normalized block distance cannot control the whole matrix

The need for many physical indices is genuine even with bounded actual-pencil data.
Take even \(n\ge4\), \(N:=n+1\), two orthogonal sign vectors \(x,y\in\{\pm N^{-1/2}\}^n\), and \(0<\epsilon<1\).
Use zero exposed diagonals, \(K=1\), \(u:=x+y\), \(v:=x+\sqrt2y\), and original principal blocks
\[
 C_1:=(1-\epsilon)I_n,\qquad C_2:=0.
\]
Then
\[
 M_\epsilon:=
 \begin{pmatrix}(1-\epsilon)I_n&I_n\\I_n&(1-\epsilon)I_n\end{pmatrix}.
\]
For every \(z\perp u,v\), the full bordered pencil has the eigenvector with zero exposed coordinates and retained coordinates \((z,-z)\), with eigenvalue \(-\epsilon\).
Such a nonzero vector exists because \(n\ge4\).
Thus \(s_{\min}(L_\epsilon)\le\epsilon\).

Nevertheless its selected block distance stays bounded below as \(\epsilon\downarrow0\).
Put
\[
 A_*:=\begin{pmatrix}\|u\|^2&-\langle u,v\rangle\\
                    -\langle u,v\rangle&\|v\|^2\end{pmatrix}
 =\frac nN
    \begin{pmatrix}2&-(1+\sqrt2)\\-(1+\sqrt2)&3\end{pmatrix}.
\]
The last matrix is positive definite since its determinant is
\(6-(1+\sqrt2)^2=(\sqrt2-1)^2>0\).
Direct inversion of \(M_\epsilon\) gives
\[
 \epsilon S_\epsilon\longrightarrow A_*/2,\qquad
 \epsilon^2\Gamma_\epsilon\longrightarrow A_*/2,
 \qquad
 \Gamma_\epsilon^{-1/2}S_\epsilon
       \longrightarrow(A_*/2)^{1/2}.
\]
Hence \(d_\epsilon\) stays uniformly positive, also along the displayed dimensions with \(\epsilon:=\epsilon_N\downarrow0\), while the least singular value of the whole matrix may decay arbitrarily quickly.
The small retained eigenmodes orthogonal to the boundary coupling account for this difference.
This is a deterministic example with the exact original-input algebraic pencil form and admissible sign borders, not a claim that its chosen principal blocks occur under a fixed original Wigner law.
It prevents replacing the many-index step by an assertion that one graph-normalized Schur complement alone controls the full least singular value.
