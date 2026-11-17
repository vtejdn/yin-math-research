---
author: Yin
---

# A polynomial cutoff for the cyclic pencil away from zero

<a id="statement"></a>
## Uniform clipped logarithms and the remaining area integral

Take any fixed nonconstant scalar polynomial \(P\) and any real or complex Hermitian Wigner laws in the [finite-second-moment contract](../tasks/Yin_T_F0012_v3.md#contract).
Write \(P_N=P(W^{(N)})\) and \(p=P(s)\).
For \(R>0\), put \(\lambda=4(R+1)\), \(H=1+P/\lambda\), \(D=\deg P\), and let \(T\) be the size-\(m\) [cyclic affine pencil](Yin_C_F0359_v1.md#construction) for \(H\).
Use the principal root to define the compact set
\[
 \Omega_R=\{(1+w/\lambda)^{1/D}: |w|\le R\}.
\]
Write \(L_N(t)=tI-T(W^{(N)})\), \(L(t)=tI-T(s)\) and \(u(t)=\log\Delta_{\operatorname{tr}_m\otimes\tau}L(t)\).
Let \(\nu_{N,t}\) count the \(mN\) singular values of \(L_N(t)\), with mass \(1/(mN)\) each.
Fix any \(B>0\), set \(c_N=N^{-B}\), and define
\[
 V_N(t)=\int\log\max(s,c_N)\,d\nu_{N,t}(s),\qquad
 Z_{N,R}=\int_{\Omega_R}\int \log^+(c_N/s)\,d\nu_{N,t}(s)\,dA(t).
\]
Use ordinary planar Lebesgue measure \(dA\) and \(+\infty\) for the loss at \(s=0\).
The free potential \(u\) is finite and continuous on \(\Omega_R\), and for every \(\varepsilon>0\),
\[
 \sum_{N\ge1}\Pr\{\sup_{t\in\Omega_R}|V_N(t)-u(t)|>\varepsilon\}<\infty. \tag{1}
\]
For the specified polynomial and laws, full-sequence weak convergence of the empirical eigenvalue measures of \(P_N\) to the Brown measure of \(p\), almost surely under every permitted cross-size coupling, is equivalent to
\[
 \sum_{N\ge1}\Pr\{Z_{N,R}>\varepsilon\}<\infty
 \qquad\text{for every positive integer }R\text{ and every }\varepsilon>0. \tag{2}
\]
One fixed \(B>0\) suffices, and if (2) holds for one such \(B\), it holds for every fixed \(B>0\).
The test can equivalently use all \(R>0\).
For constant \(P\), (2) and the weak limit hold deterministically, as shown below.
The general estimate (2) is the outstanding probability question.

<a id="chart"></a>
## Removing the structural zero from the test region

The disk \(1+\{|w|\le R\}/\lambda\) is contained in \(\{|v-1|\le1/4\}\).
The map \(w=\lambda(t^D-1)\) therefore has a holomorphic inverse on a neighborhood of the disk in the \(w\)-plane given by the chosen principal root.
On \(\Omega_R\) its area Jacobian \(J(t)=\lambda^2D^2|t|^{2D-2}\) is bounded above and strictly away from zero.
Use \(U_N(t)=(mN)^{-1}\log|\det L_N(t)|\) and the finite and free logarithmic potentials \(U_{P_N},U_p\) with their scalar trace normalization.
The [ordinary finite and free identities](Yin_C_F0359_v1.md#argument) give
\[
 U_{P_N}(w)-U_p(w)=m\,[U_N(t)-u(t)].
 \tag{3}
\]
Indeed the shared structural term \((m-D)\log|t|\) and the shared term \(-\log\lambda\) from \(t^D-H=(w-P)/\lambda\) cancel.
The determinant of \(L_N(t)\) is a nonzero monic polynomial in \(t\), so its logarithm is locally integrable even when some roots lie in \(\Omega_R\).
Thus \(Z_{N,R}=\int_{\Omega_R}(V_N-U_N)\,dA\) is finite for each realization.

<a id="count"></a>
## Uniform singular counts on the chart

For \(t\in\Omega_R\) the algebraic Schur complement of the cyclic pencil is \(t^{-(D-1)}(t^D-H)\).
The triangular pivot is invertible over the free polynomial algebra since \(t\ne0\).
The scalar complement is a nonzero free polynomial, hence invertible in the free skew field, proving fullness of every member of the compact coefficient family.
For \(D=1\) fullness follows directly from the same scalar polynomial.
Apply the [compact-family free estimate](Yin_C_F0352_v1.md#statement) to obtain a uniform free singular count \(C a^\eta\) on \(0<a\le1\), with \(\eta>0\), for \(L(t)\).

The [finite bounded-entry comparison](Yin_C_F0195_v4.md#bounded-core) changes only the constant Hermitian drift when \(t\) varies.
Its cutoff rank bound and random coefficients are unchanged, the replacement derivatives use the common resolvent norm \(a^{-1}\), and its [Gaussian comparison](Yin_C_F0195_v4.md#free-background) is uniform in the drift.
Consequently the comparison error before adding the smoothed free term is bounded by \(C(M^{-2}+N^{-1/2}a^{-3}+N^{-1}a^{-4})\) for all \(t\in\Omega_R\).
For the conditional free term the same compact-family estimate gives \(C(1+M)^h a^\eta\), with fixed positive semicircular noise scales and background normalized Hilbert--Schmidt norms bounded by \(M\).
Decreasing \(\eta\) if necessary and choosing \(M=a^{-\eta/(2(h+1))}\) gives precisely the [polynomial-window argument](Yin_C_F0186_v40.md#argument) with constants independent of the shift.
In particular there are \(C,\beta,\gamma>0\) such that for all large \(N\),
\[
 \sup_{t\in\Omega_R}\mathbb E\nu_{N,t}([0,a])\le C a^\beta,
 \qquad N^{-\gamma}\le a\le1. \tag{4}
\]

<a id="clip"></a>
## Uniform expectation and summable fluctuations

Affineness and the two raw moments give \(\mathbb E\sup_{t\in\Omega_R}\|L_N(t)\|_{\rm HS}^2\le C_R N\).
Indeed \(\sup|t|\) is bounded, the coefficient sizes are fixed, and each input has expected squared Hilbert--Schmidt norm \(O(N)\).
In particular the expected normalized contribution \(\int\log^+(s/K)\,d\nu_{N,t}\) is at most \(C/K^2\) for \(K\ge1\), uniformly in \(t,N\), by \(\log^+ y\le y^2\).
The free norms are uniformly bounded.

For \(0<d<1<K\) the bounded test \(\log\min(K,\max(d,s))\) has pointwise convergence of its expected singular integrals by the [finite-variance weak law](Yin_C_F0186_v4.md#finite-variance-weak) applied to the signed Hermitian dilation.
Each expected integral is \(d^{-1}\)-Lipschitz in \(t\) since the ordered singular values change by at most the shift distance.
The pointwise free limit inherits this Lipschitz bound, so compactness gives uniform convergence at these fixed cutoffs.
The difference between lower clipping at \(d\) and at \(c_N\) has expectation at most
\[
 C d^\beta/\beta+C B N^{-\gamma\beta}\log N
\]
for all large \(N\), uniformly on \(\Omega_R\), by integrating (4) with \(da/a\) and bounding the count below \(N^{-\gamma}\) by monotonicity.
On the free side the corresponding loss from zero to \(d\) is at most \(C d^\eta/\eta\).
Letting \(d\downarrow0\) and \(K\uparrow\infty\) gives continuity and finiteness of \(u\), and \(\sup_{\Omega_R}|\mathbb EV_N-u|\to0\).

Let \(\widehat V_N\) also clip the positive end of \(V_N\) at the singular value \(N^2\).
Uniformly in \(t\), its expectation differs from \(\mathbb EV_N\) by at most \(C N^{-4}\).
The probability that this extra clip changes \(V_N\) anywhere on \(\Omega_R\) is at most \(C N^{-3}\) by the preceding Hilbert--Schmidt estimate and Markov's inequality.
For each fixed \(t\), the test for \(\widehat V_N\) has total variation at most \((B+2)\log N\) on nonnegative singular values.
Replacing one independent physical row group changes \(L_N\) by bounded rank, uniformly in \(t\) and the entries, because each changed color is supported on the corresponding row and column.
The [bounded-differences inequality for the Hermitian dilation](Yin_C_F0186_v4.md#row-concentration) therefore gives
\[
 \Pr\{|\widehat V_N(t)-\mathbb E\widehat V_N(t)|>x\}
 \le 2\exp[-c N x^2/((B+2)\log N)^2]\qquad(N\ge2).
\]
A mesh of radius \(N^{-(B+2)}\) with centers in \(\Omega_R\) has \(O_R(N^{2B+4})\) points by a planar packing bound.
Both \(\widehat V_N\) and its expectation are \(N^B\)-Lipschitz, so passage from the mesh to the whole set costs at most \(2N^{-2}\) in centered deviation.
The polynomial mesh times the exponential bound is summable for each fixed \(x>0\).
Restoring the upper clip outside its summable exception and using uniform expectation convergence proves (1).

<a id="equivalence"></a>
## From the unestimated lower tail to weak convergence

For each realization, \(V_N-U_N\ge0\) almost everywhere.
The norm inequality for integrable functions gives
\[
 \left|\int_{\Omega_R}|U_N-u|\,dA-Z_{N,R}\right|
 \le |\Omega_R|\,\sup_{\Omega_R}|V_N-u| . \tag{5}
\]
By (3) and change of variables, the scalar \(L^1\) error on the radius-\(R\) disk equals \(m\int_{\Omega_R}|U_N-u|J(t)\,dA(t)\).
Thus its vanishing is equivalent to vanishing of the unweighted integral in (5).
The [pathwise scalar potential criterion](Yin_C_F0186_v4.md#remaining-defect) shows that, on one probability-one event in any given coupling, weak Brown convergence implies convergence of the scalar potentials in local \(L^1\).
Its converse follows by the distributional Laplacian and the same theorem's pathwise tightness.
These implications use the stated finite-variance controls on the logarithmic positive tails.

If (2) holds, first Borel--Cantelli for (1) and (2) on integer radii and rational positive tolerances gives convergence of all disk errors on one event for each coupling.
The scalar criterion proves weak convergence there.
Conversely take the allowed coupling that makes the entire tuples independent across dimensions.
Under the assumed every-coupling conclusion, the disk errors tend to zero almost surely there, for each fixed \(R>0\).
By (1) and (5), \(Z_{N,R}\to0\) almost surely.
Each event in (2) depends only on the tuple of its own dimension, so the independent-events Borel--Cantelli lemma forces the stated series of marginal probabilities to converge.
This proves the assertions about \(B\) and the choice of radii.

For \(P=a\) constant use \(D=m=1\) and \(T=1+a/\lambda\).
The finite and free scalar laws both equal \(\delta_a\).
On any chart, \(Z_{N,R}\le\int_{|z|<c_N}\log(c_N/|z|)\,dA(z)=\pi c_N^2/2\) by translation.
If the chart contains \(1+a/\lambda\), its free potential takes the value \(-\infty\) there, which explains the nonconstant hypothesis in (1).

## Current assessment
[Selected decision](#decision-local-cutoff-reviewed)

## Assessment history

### Decision local-cutoff-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:57 |
| status | open |
| reason | The compact full-pencil count controls the polynomial clip uniformly away from the structural zero, yielding an exact terminal-area criterion for the arbitrary-coupling scalar question. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete convergence of the clip and terminal equivalence](#statement) | All fixed nonconstant scalar polynomials, both entry models, all fixed cutoffs and the deterministic constant case. |
| argument | [Uniform counts](#count) | Fullness on one compact chart and applicability of the finite and free estimates there. |
| support | [Clipped potentials](#clip) | Uniform expectation, summable fluctuations and the positive tail with two moments. |
| support | [Equivalence](#equivalence) | Weighted chart identity, scalar potential topology, product coupling and the remaining unproved series. |
| dependency | [Cyclic determinant identities](Yin_C_F0359_v1.md#argument) | Finite and free ordinary shifts with their respective trace weights. |

### Decision local-cutoff-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:03 |
| status | proved |
| reason | Uniform polynomial clipping on the cyclic shift region reduces the full all-coupling Brown convergence problem exactly to the displayed marginal series. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed theorem](#statement) | Uniform polynomial clipping on the cyclic shift region reduces the full all-coupling Brown convergence problem exactly to the displayed marginal series. |
| argument | [Complete argument](#chart) | The stated input laws, parameter sets and coupling requirements. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0367_v2.md#local-cutoff-whole-proof) | Full scope of this version. |
