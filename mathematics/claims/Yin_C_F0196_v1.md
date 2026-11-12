---
author: Yin
---

# Physical incompressibility for a two-sided Wigner product

This Claim develops the original-law least-value route for \(P(A,B)=AB+2BA\) in [F0012](../tasks/Yin_T_F0012_v3.md#contract).
It proves a norm-guarded compressible-vector exclusion and physical-column distance average under fourth off-diagonal moments.
The complete argument has received [independent whole-proof review](../audits/reviews/Yin_R_F0203_v1.md#whole-candidate-finding), adopted below.
It does not supply the distance small-ball estimate, a least-value floor or a Brown-measure conclusion.

<a id="source-comparison"></a>
## Existing inputs and method attribution

The [two-sided physical Schur calculation](../ledger/Yin_L_F0066_v19.md#two-sided-conditional-quartic-test) retains the actual companion and its conditional quartic numerator and denominator.
The [positive-frame spread theorem](../claims/Yin_C_F0194_v25.md#natural-scale-spread) supplies a related proof organization, but its positive-frame and real selfadjoint hypotheses are not imposed or invoked here.
The present proof instead isolates an independent original rectangular block on sparse vectors.

The familiar norm-guarded small-ball and sparse-net method appears in Rudelson--Vershynin, [arXiv:math/0703503v2](https://arxiv.org/pdf/math/0703503v2), Proposition 2.5 and Lemma 2.6 on PDF pp. 11--12, and Lemmas 3.3--3.4 on PDF pp. 15--16.
Those passages and their displayed proofs were inspected as method attribution.
The scalar distance-average argument in the same source, Lemma 3.5 on PDF pp. 16--17, is also method attribution for the physical-block counting argument below.
That additional passage was inspected during independent review; the block projection and companion reduction are proved explicitly here.
Their independent-real-entry theorem is not invoked for the dependent product below.
The complex affine small-ball estimate, both lawful rectangular exposures, uniformity in the shift, and the companion transfer are proved here.
Only elementary fourth-moment expansion, Cauchy--Schwarz, independent Bernoulli concentration and finite-dimensional nets are used.

<a id="statement"></a>
## Exact statement

For each \(N\), let \(A_N,B_N\) be independent Hermitian Wigner matrices.
Their strict upper entries are independent copies of \(\xi_A/\sqrt N\) and \(\xi_B/\sqrt N\), respectively, where each fixed complex law is centered, has second absolute moment one and has finite fourth absolute moment.
Their lower entries are conjugates, and the real diagonal coordinates are independent of the strict upper entries and each other.
The diagonal laws can be arbitrary for the norm-guarded assertion; the original fixed finite-second-moment diagonal laws are included.
No independence between the real and imaginary parts of an entry is assumed, so real symmetric inputs are included.
All within-size independence is as just stated, and the coupling across sizes is arbitrary.

Fix \(K\ge1\) and \(Z\ge0\), and put
\[
 \Omega_{N,K}=\{\|A_N\|\le K,\ \|B_N\|\le K\},
 \qquad P_N=A_NB_N+2B_NA_N.
\]
There are constants \(\delta,\rho,a,c,C>0\), depending only on \(K,Z\) and the two fourth-moment bounds, such that for all sufficiently large \(N\),
\[
 \mathbb P\!\left\{\Omega_{N,K},\
  \exists |z|\le Z,\ \exists u\in\operatorname{Comp}_N(\delta,\rho):
       \|(P_N-zI_N)u\|\le a\right\}
 \le Ce^{-cN}.
 \tag{Two-sided-compressible-exclusion}
\]
Here \(\operatorname{Comp}_N(\delta,\rho)\) is the set of complex unit vectors at Euclidean distance at most \(\rho\) from the set of complex unit vectors supported on at most \(\lfloor\delta N\rfloor\) coordinates.
All constants are independent of \(N\) and the diagonal distributions.
The norm guard is an event restriction and is never conditioned into the law of a fresh rectangular block.
No summability assertion is made for \(\mathbb P(\Omega_{N,K}^c)\).

The same exceptional event supplies the [natural-scale spread](#spread) and [physical companion distance average](#companion-average) below.

## Current assessment
[Selected decision](#decision-incompressibility-reviewed)

## Assessment history

### Decision incompressibility-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-11T13:33 |
| status | open |
| reason | The complete local rectangular-exposure proof and its companion consequence await independent checking. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Fixed norm-guarded compressible exclusion, simultaneous bounded-shift spread and physical-column distance averaging for the two-sided product. |
| argument | [Complete argument](#argument) | Complex affine small-ball bound, two independent rectangular exposures, sparse nets, companion transfer and distance average. |

### Decision incompressibility-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-11T13:42 |
| status | proved |
| reason | Independent whole-argument inspection, including the corrected count-event implication and exact method attribution, supports the full norm-guarded exclusion, spread and physical distance average at the stated complex fourth-moment scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Fixed norm-guarded compressible exclusion, simultaneous bounded-shift spread and physical-column distance averaging for the two-sided product. |
| argument | [Complete argument](#argument) | Complex affine small-ball bound, two independent rectangular exposures, sparse nets, companion transfer and distance average. |
| review | [Independent whole-candidate finding](../audits/reviews/Yin_R_F0203_v1.md#whole-candidate-finding) | Entire statement, argument and exact source-method attribution, including the independently rechecked count-event explanation and all guarded probability boundaries. |

<a id="argument"></a>
<a id="affine-small-ball"></a>
## A complex affine small-ball bound from fourth moments

Let \(\eta_j\) be independent centered complex variables with \(\mathbb E|\eta_j|^2=1\) and \(\mathbb E|\eta_j|^4\le\kappa\), and set \(S=\sum_jv_j\eta_j\), \(r^2=\sum_j|v_j|^2>0\).
The laws may differ and may include conjugates of a fixed law.
Independence and centering give
\[
 \mathbb E|S|^2=r^2,
 \qquad \mathbb E|S|^4\le C_4r^4,
 \tag{Fourth-linear-moment}
\]
with \(C_4\) depending only on \(\kappa\).
For the fourth moment, expand \(S\overline S S\overline S\).
Terms having an index occurring just once vanish, the all-equal-index terms are bounded by \(\kappa\sum_j|v_j|^4\), and the three pairings are each bounded by a constant multiple of \(r^4\), using \(|\mathbb E\eta_j^2|\le1\).
This proves the displayed bound without any real-imaginary independence hypothesis.

Let \(S'\) be an independent copy of \(S\) and \(D=S-S'\).
Then \(\mathbb E|D|^2=2r^2\) and \(\mathbb E|D|^4\le C_5r^4\), by the same expansion or \(|S-S'|^4\le8(|S|^4+|S'|^4)\).
Writing \(E=\{|D|>r\}\), Cauchy--Schwarz gives
\[
 2r^2\le r^2+(\mathbb E|D|^4)^{1/2}\mathbb P(E)^{1/2},
 \qquad \mathbb P(E)\ge C_5^{-1}.
\]
If both \(S,S'\) lie in a disk of radius \(r/4\) around the same center, then \(|D|\le r/2\).
Therefore, after choosing a fixed \(p\in(0,1)\) depending only on \(\kappa\),
\[
 \sup_{w\in\mathbb C}\mathbb P\{|S-w|\le r/4\}\le1-p.
 \tag{Affine-fourth-small-ball}
\]
Choose one \(p\) valid for both input laws and all their conjugates.

For independent rows \(Y_i=N^{-1/2}\sum_jv_j\eta_{ij}+w_i\), with deterministic complex centers \(w_i\), the indicators of \(|Y_i|>r/(4\sqrt N)\) are independent and each has mean at least \(p\).
If the number of rows \(q\) is at least \(N/5\), the elementary multiplicative Chernoff bound implies
\[
 \mathbb P\!\left\{\sum_{i=1}^q|Y_i|^2<c_0^2r^2\right\}
 \le e^{-c_1N},
 \qquad c_0=\sqrt{p/160},\quad c_1=p/40.
 \tag{Rectangular-affine-bound}
\]
Indeed, except on a Chernoff count event of probability at most \(e^{-pq/8}\le e^{-c_1N}\), at least \(pq/2\) indicators are one.
On this count-good event their squared contribution is at least \(pqr^2/(32N)\ge p r^2/160\), which proves the displayed small-norm probability bound.
The centers are unrestricted.

<a id="sparse-rectangles"></a>
## A simultaneous lower bound for the first rectangular action

Choose a small \(\delta<1/8\) later and set \(s=\lfloor\delta N\rfloor\).
For each set \(S\subset[N]\) of size \(s\), choose deterministically disjoint sets \(I(S),J(S)\subset S^c\), each of size \(\lfloor N/4\rfloor\).
For large \(N\) these sets exist and each has size at least \(N/5\).
Choose the choices before revealing the matrices.
The entries of \(B_{J,S}\) belong to distinct unordered off-diagonal pairs, so are independent, with each raw law either \(\xi_B\) or \(\overline{\xi_B}\).
For each deterministic complex unit vector \(v\) supported in \(S\), (Rectangular-affine-bound) with zero centers gives
\[
 \mathbb P\{\|B_{J,S}v\|<c_0\}\le e^{-c_1N}.
\]
Let
\[
 \eta=\min\left\{\frac12,\frac{c_0}{2K},
                         \frac{c_0^2}{12K^2}\right\}.
\]
For every \(S\), fix an \(\eta\)-net \(\mathcal N_S\) of its complex unit sphere, with cardinality at most \((1+2/\eta)^{2s}\).
On \(\{\|B\|\le K\}\), approximation by this net shows that
\[
 \inf_{\substack{v\in\mathbb C^S\\\|v\|=1}}\|B_{J,S}v\|<c_0/2
\]
implies \(\|B_{J,S}v_0\|<c_0\) for some \(v_0\in\mathcal N_S\).
Consequently, if \(\mathcal B_N\) denotes the event that
\[
 \|B\|\le K,
 \qquad \|B_{J(S),S}v\|\ge\beta:=c_0/2
 \quad\text{for every }S,\ v\in\mathbb C^S,\ \|v\|=1,
 \tag{First-rectangle-good-event}
\]
then
\[
 \mathbb P\{\|B\|\le K,\ \mathcal B_N^c\}
 \le {N\choose s}(1+2/\eta)^{2s}e^{-c_1N}.
\]
Choose \(\delta>0\) sufficiently small that, for all large \(N\),
\[
 {N\choose s}(1+2/\eta)^{2s}\le e^{c_1N/2}.
 \tag{Sparse-entropy}
\]
This is possible because \(\delta\log(e/\delta)+2\delta\log(1+2/\eta)\to0\) as \(\delta\downarrow0\).
Thus the excluded probability on the fixed norm guard is at most \(e^{-c_1N/2}\).

<a id="lawful-second-rectangle"></a>
## The fresh rectangle for the two-sided product

Fix \(S\), abbreviate \(I=I(S),J=J(S)\), and fix \(v\in\mathcal N_S\).
Condition on all of \(B\) and all original coordinates of \(A\) except the unordered pairs between \(I\) and \(J\).
The entries of \(A_{I,J}\) remain independent original entries, possibly conjugated according to their positions.
The mirrored entries of \(A_{J,I}\) are the same variables and are not treated as an independent rectangle.

Because \(v\) is supported on \(S\), one has \(Av=A_{[N],S}v\).
This vector is fixed by the conditioning, since \(S\cap(I\cup J)=\varnothing\).
In particular, \(2BAv\) is fixed, including its coordinates in \(I\).
The vector \(Bv\) is also fixed, and the only fresh entries of \((ABv)_I\) occur in \(A_{I,J}(Bv)_J\).
Thus the exact conditional identity is
\[
 (P_Nv)_I=A_{I,J}(Bv)_J+c,
 \tag{Original-fresh-rectangle}
\]
with a fixed complex center vector \(c\).
The event \(\mathcal B_N\) ensures \(\|(Bv)_J\|=\|B_{J,S}v\|\ge\beta\).
The rows of the remaining rectangle are independent, so (Rectangular-affine-bound) yields
\[
 \mathbb P\{\|(P_Nv)_I\|<c_0\beta
       \mid B,\ A\text{ outside the }I\text{-}J\text{ pairs}\}
 \le e^{-c_1N}
\]
on \(\mathcal B_N\).
There is no conditioning on \(\Omega_{N,K}\) in this inequality.

Integrate this conditional estimate and take the union over \(S,v\in\mathcal N_S\).
By (Sparse-entropy), the resulting failure probability on \(\mathcal B_N\) is at most \(e^{-c_1N/2}\).
On \(\Omega_{N,K}\), \(\|P_N\|\le3K^2\), so the chosen net precision gives
\[
 \|(P_Nu)_{I(S)}\|\ge c_0\beta-3K^2\eta
 \ge\gamma:=c_0^2/4
\]
for every complex unit \(u\) supported on \(S\), outside the combined exception of probability at most \(2e^{-c_1N/2}\).
Every support of size at most \(s\) is contained in an \(S\) of size \(s\), so this covers all such sparse unit vectors.
Since \(u_{I(S)}=0\), it follows on the same event that
\[
 \|(P_N-zI_N)u\|\ge\gamma
 \quad\text{for every sparse unit }u\text{ and every }z\in\mathbb C.
 \tag{Sparse-all-shifts}
\]
No net over \(z\) is required.

<a id="compressible-extension"></a>
## Compressible vectors and uniform bounded shifts

Put \(L=3K^2+Z\), choose
\[
 \rho=\min\{1/2,\gamma/(4L)\},\qquad a=\gamma/2.
\]
For \(|z|\le Z\), a compressible unit \(u\) has a sparse unit \(v\) within distance \(\rho\), and on the norm guard
\[
 \|(P_N-zI_N)u\|
 \ge\|(P_N-zI_N)v\|-L\|u-v\|
 \ge\gamma-L\rho\ge3\gamma/4>a.
\]
Together with the preceding probability estimate this proves (Two-sided-compressible-exclusion).
The same event works for all bounded complex shifts and all complex unit vectors.

<a id="spread"></a>
## Natural-scale spread of the original root vector

On this good norm-guarded event, every unit \(u\) with
\(\|(P_N-zI_N)u\|\le a\) is outside \(\operatorname{Comp}_N(\delta,\rho)\).
Let \(H\) be the indices of its \(s\) largest coordinate moduli.
The unit vector \(u_H/\|u_H\|\) is sparse, and
\[
 \left\|u-\frac{u_H}{\|u_H\|}\right\|^2
 =2(1-\|u_H\|)\le2\|u_{H^c}\|^2.
\]
Thus \(\|u_{H^c}\|^2>\rho^2/2\).
For large \(N\), every coordinate outside \(H\) is at most \(\sqrt{2/\delta}\,N^{-1/2}\).
Coordinates there smaller than \(\rho/(2\sqrt N)\) carry total squared mass at most \(\rho^2/4\).
The remaining coordinates therefore carry squared mass at least \(\rho^2/4\), giving
\[
 \#\left\{i:\ \frac{\rho}{2\sqrt N}\le|u_i|
              \le\frac{\sqrt{2/\delta}}{\sqrt N}\right\}
 \ge p_*N,\qquad p_*:=\delta\rho^2/8.
 \tag{Two-sided-root-spread}
\]
The argument applies to complex vectors without alteration.

<a id="companion-average"></a>
## Physical companion spread and the distance average

Use the actual companion
\[
 \mathcal L_N(z)=
 \begin{pmatrix}-zI&A_N&2B_N\\B_N&-I&0\\A_N&0&-I\end{pmatrix},
\]
and group its three coordinates at each physical position.
For a unit vector \(w=(u,v,t)\), write the three residuals of \(\mathcal L_N(z)w\) as \((r_0,r_1,r_2)\).
The exact identities are
\[
 v=Bu-r_1,\quad t=Au-r_2,\qquad
 (P_N-zI)u=r_0+Ar_1+2Br_2.
\]
If \(\|\mathcal L_N(z)w\|\le\varepsilon\le1/4\), the triangle inequality gives
\[
 1\le(1+2K)\|u\|+2\varepsilon,
 \qquad \|u\|\ge c_u:=\frac1{2(1+2K)},
\]
while \(\|(P_N-zI)u\|\le(1+3K)\varepsilon\).
Set
\[
 \varepsilon_*:=\min\{1/4,\ c_u a/(1+3K)\},
 \qquad c_*:=c_u\rho/2.
\]
Whenever \(\varepsilon\le\varepsilon_*\), apply (Two-sided-root-spread) to \(u/\|u\|\).
At least \(p_*N\) physical blocks of \(w\) then satisfy \(\|w_i\|\ge c_*/\sqrt N\).
This holds simultaneously for all such complex near-kernel vectors and all \(|z|\le Z\).

Let \(C_i(z)\) be the three physical columns of \(\mathcal L_N(z)\), and let \(Q_i(z)\) be the orthogonal projection onto the complement of all its other columns.
Define \(d_i(z)=s_{\min}(Q_i(z)C_i(z))\); these objects are defined even if some outside columns are dependent.
For a near-kernel vector and every index with the stated lower block bound,
\[
 d_i(z)\|w_i\|\le\|Q_iC_iw_i\|
 =\|Q_i\mathcal L_N(z)w\|\le\varepsilon.
\]
Taking a least right singular vector, counting these indices pointwise and then taking expectation yields, for every fixed \(|z|\le Z\) and \(0\le\varepsilon\le\varepsilon_*\),
\[
 \mathbb P\{\Omega_{N,K},\ s_{\min}(\mathcal L_N(z))\le\varepsilon\}
 \le Ce^{-cN}
   +\frac1{p_*N}\sum_{i=1}^N
      \mathbb P\!\left\{\Omega_{N,K},\
                  d_i(z)\le\frac{\sqrt N\varepsilon}{c_*}\right\}.
 \tag{Two-sided-distance-average}
\]
No independence among the physical distance events is used.
The norm-guard failure must be added if that guard is removed.

This average removes the factor \(N\) of a bare union bound at the physical distance interface.
It does not supply a bound for its averaged right side.
For real inputs, the [complete quartic quotient and rank branch](../ledger/Yin_L_F0066_v19.md#two-sided-quartic-first-obligation) remain the appropriate conditional objects; no quadratic inverse theorem or generic tube bound applies to them automatically.
A polynomially decaying conditional matching bound, if proved with the actual random background and denominator, would now be sufficient for an in-probability floor after averaging, without requiring an arbitrary-power row bound merely to pay for a union over indices.
Summability and the original almost-sure Brown conclusion require additional quantitative control.
