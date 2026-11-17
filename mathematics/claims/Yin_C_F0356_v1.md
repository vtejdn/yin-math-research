---
author: Yin
---

# Spectral flow of one diagonal sign color at a stable energy of a Hermitian pencil

<a id="statement"></a>
## A polynomial floor under the original sign law

Let \(A_1,\ldots,A_g,C\) be fixed Hermitian \(m\)-square matrices and assume \(A_1\ge cI\) for some \(c>0\).
At each \(N\) take independent real symmetric matrices \(W_j\) whose upper triangular entries, including the diagonals, are independent signs divided by \(\sqrt N\).
Put \(H=C\otimes I+\sum A_j\otimes W_j\).
Fix a real \(E\) such that the positive-imaginary-part solution of
\[
 -M(z)^{-1}=zI-C+\mathcal S(M(z)),\qquad \mathcal S(T)=\sum_j A_j T A_j ,
\]
and the inverse of \(T\mapsto T-M(z)\mathcal S(T)M(z)\) are uniformly bounded on \(z=E+i\eta,\ \eta>0\).
Then for all sufficiently large \(N\)
\[
 \Pr\{s_{\min}(H-EI)\le N^{-3}\}\le C_E N^{-1/4}. \tag{1}
\]
Consequently the ordinary normalized log determinant converges in probability through all sizes to the normalized free log determinant.
Under every cross-size coupling it converges almost surely on \(N=2^j\), the all-size almost-sure limsup equals the free target, and the part below \(N^{-3}\) vanishes eventually along these even sizes.
The algebraic condition and examples below allow three-dimensional coefficient spaces without a rank-one random coefficient, including irreducible examples.

<a id="argument"></a>
<a id="local-law"></a>
## Local projection bounds and resampling the number of positive diagonals

Subtract \(E\) in all eigenvalue counts below.
Set \(a=N^{-31/32}\), \(b=N^{-1/3}\), and \(l=\lceil N^{1/8}\rceil\).
Write \(R(t)=(H-E-it)^{-1}\); physical diagonal blocks have size \(m\).
The [stable Kronecker local law of Alt, Erdős, Krüger and Nemish](../audits/literature/AEKN19/Yin_U001.md#stable-block-law) bounds \(\max_i\|R(t)_{ii}\|\le C\) outside probability \(O_D(N^{-D})\) for each \(D\), simultaneously at \(b,2a\) and dyadic multiples of \(a\) up to \(2\).
In the physical ordering with mean-zero site vectors the stability operator is identity; its constant part is the stated finite-dimensional operator.
The assumptions in the source concern the ray above the spectral parameters in use and the usual bounded normalized moments; the given hypothesis and sign laws meet them.
Since \(\mathbf1_{[-t,t]}(H-E)\le2t\operatorname{Im}R(t)\), the count in such a window is \(O(Nt)\) and each diagonal block of its projection has norm \(O(t)\).
These statements use the original independent signs.

Represent the first color's \(N\) diagonal signs by a uniform random permutation of the sites and an independent \(q\sim{\rm Bin}(N,1/2)\).
The first \(q\) sites have positive sign.
Write \(H_q\) for the resulting Hermitian chain, with the other entries drawn once.
Let \(q_-,q_+\) be the integer-rounded endpoints of \(N/2\pm\sqrt{6N\log N}\).
Outside this interval the binomial probability is \(O(N^{-10})\) by the scalar exponential bound.
Inside it each point probability is at least an inverse power of \(N\) by Stirling's formula and is at most \(C/\sqrt N\).
Thus an event with arbitrary polynomial failure under the original law still has arbitrary polynomial failure for all these central \(H_q\) simultaneously, by conditioning on the binomial count and a union bound.

Remove the entire first-color diagonal term and denote the resulting matrix by \(H_*\), independent of the permutation.
Its resolvent at \(ib+E\) has the same uniform diagonal imaginary-part bound with arbitrary polynomial failure.
Indeed in the unconditioned law \(\|H-H_*\|\le\|A_1\|/\sqrt N\).
The resolvent identity bounds the norm of \(R_*(b)\) applied to any vector by at most \(2\) times the norm of \(R(b)\) applied to that same vector, since \(\|R(b)(H_*-H)\|\le \|A_1\|/(b\sqrt N)=o(1)\).
Use \(\operatorname{Im}R=bR^*R\).
Hence the projection \(P=\mathbf1_{[-b,b]}(H_*-E)\) has \(\max_i\|(P)_{ii}\|\le Cb\), with this guard depending only on \(H_*\).
On its range let \(B_i=P(I_m\otimes e_i e_i^*)P\); then \(\sum B_i=I,\ 0\le B_i\le C bI\).

<a id="negative-sites"></a>
## Mass on the coordinates available for the next flips

Uniformly for the central \(q\)'s, the still-negative sites \(J_q\) see at least \(1/4\) of the squared norm of each vector in the range of \(P\), with arbitrary polynomial failure.
For independent fair signs \(\epsilon_i\), this follows from \(\|\sum_i\epsilon_i B_i\|\le1/2\), then conditioning on the central count as above.
Here is a moment proof at fixed guarded \(P\).
For independent standard normals \(g_i\), convexity and conditioning on the Gaussian signs bound the \(2p\)-th norm moment of the sign sum by \((\mathbb E|g_1|)^{-2p}\mathbb E\operatorname{Tr}Z^{2p}\) with \(Z=\sum_i g_i B_i\).
Integration by parts gives \(\mathbb E\operatorname{Tr}Z^{2p}\le (2p-1)\|\sum B_i^2\|\mathbb E\operatorname{Tr}Z^{2p-2}\).
In an eigenbasis of \(Z\), each intermediate trace \(\operatorname{Tr} B_i Z^j B_i Z^{2p-2-j}\) is bounded in absolute value by \(\operatorname{Tr}B_i^2|Z|^{2p-2}\), by the scalar weighted arithmetic-geometric mean and symmetry of \(|(B_i)_{uv}|^2\); \(p=1\) is direct.
Since \(\sum B_i^2\le C bI\), \(p=\lceil\log N\rceil\) gives the asserted failure via Markov, with trace dimension at most \(mN\).

Let \(V_q\) be the range of \(\mathbf1_{[-2a,2a]}(H_q-E)\).
On the preceding events \(V_q\) has dimension at most \(CNa\), and its projection has diagonal block norms at most \(Ca\).
For \(v\in V_q\), \(\|(1-P)v\|\le(2a+\|A_1\|/\sqrt N)\|v\|/b=o(1)\|v\|\) by the spectral theorem at \(H_*\).
Therefore \(\sum_{i\in J_q}\|v_i\|^2\ge c_1\|v\|^2\) for all these \(q\), writing \(v_i\in\mathbb C^m\) for its physical component.
The guard for a single \(q\) may here be taken to concern only \(H_*\), the current signs and the current \(H_q\).

At each \(q\le q_+-l\) the next \(l\) sites \(I_q\) are conditionally uniform without replacement within \(J_q\) given the order through \(q\) and the matrix entries used to form \(H_*\).
On the single-\(q\) guard, with arbitrary polynomial conditional failure,
\[
 \sum_{i\in I_q}\|v_i\|^2\ge c_2(l/N)\|v\|^2,\qquad v\in V_q. \tag{2}
\]
For a fixed unit \(v\) the weights \(\|v_i\|^2\) are at most \(Ca\) and their sum on \(J_q\) is at least \(c_1\).
First retain each site independently with probability \(l/|J_q|\).
Exponential Markov applied to the weighted sum with Laplace parameter \(1/(Ca)\) bounds the probability of obtaining less than half a fixed fraction of \(l/N\) by \(\exp[-c l/(Na)]\); use \(1-e^{-u}\ge (1-e^{-1})u\) on \([0,1]\).
Condition on retaining exactly \(l\), at cost at most \(C\sqrt N\) by Stirling.
A sphere net on \(V_q\) of mesh \(c_3\sqrt{l/N}\) costs \(\exp(CNa\log N)\), absorbed since \(l/(Na)\gg Na\log N\).
The tested coordinate projection is contractive, so the net bound extends to all vectors.
Apply the conditional estimate on present-time guards and union over \(q\); this does not condition a future set \(I_q\) on later projection information.

<a id="crossings"></a>
## The number of visits to a narrow interval

Let \(\lambda_j(q)\) be the eigenvalues of \(H_q-E\) in increasing order.
They are nondecreasing in \(q\) because \(A_1>0\).
If \(|\lambda_j(q)|\le N^{-3}\), then (2) implies \(\lambda_j(q+l)>\lambda_j(q)+2N^{-3}\).
To prove this, work in the span of eigenvectors with indices at least \(j\), splitting each unit \(v=x+y\) at energy \(\lambda_j(q)+a\) with the lower part \(x\in V_q\).
The old Rayleigh quotient is at least \(\lambda_j(q)+a\|y\|^2\).
If \(\|y\|\ge c_4\sqrt{l/N}\), this gain suffices.
Otherwise the norm of \(v\) projected on \(I_q\) is at least \(\sqrt{c_2 l/N}\|x\|-\|y\|\ge c_5\sqrt{l/N}\), for a suitable \(c_4\).
The positive increment on \(I_q\) has least block eigenvalue at least \(2c/\sqrt N\).
The min-max principle now gives a gain of at least \(c_6(l/N)\min(a,N^{-1/2})\gg N^{-3}\).
Monotonicity therefore allows at most \(l\) central visits per index, also for indices first seen in the last \(l\) positions.

The expected number of indices capable of visiting is at most \(C(Na+(\log N)^{3/2})\).
Here are details for crossings between the endpoints.
Set \(K_0=H_{q_-}-E\), \(\Delta=H_{q_+}-H_{q_-}\ge0\).
The number of eligible indices is at most
\[
 n_-(K_0)-n_-(K_0+\Delta)+
 \#\operatorname{spec}_{[-2a,2a]}(K_0)+\#\operatorname{spec}_{[-2a,2a]}(K_0+\Delta),
\]
counting multiplicities and using strict negatives in \(n_-\).
Move the eigenvalues of \(K_0\) in \([-a,a]\) to \(2a\) and call the result \(K'\).
This changes either count of strict negatives in the difference by at most \(CNa\) on the initial local-law guard.
For invertible \(K'\),
\[
 n_-(K')-n_-(K'+\Delta)
 \le \operatorname{Tr}(\Delta |K'|^{-1}).
\]
Indeed compute the inertia of \(\left(\begin{smallmatrix}K'&\Delta^{1/2}\\\Delta^{1/2}&-I\end{smallmatrix}\right)\) by both Schur complements.
The difference counts eigenvalues \(\le-1\) of \(\Delta^{1/2}(K')^{-1}\Delta^{1/2}\), bounded by its trace norm, and splitting \((K')^{-1}\) into positive and negative parts gives the displayed bound.
The dyadic counts \(O(Nt)\) at the initial endpoint give \(\operatorname{Tr}|K'|^{-1}\le CN\log N\), including the part beyond one.
Given the initial state and its own guard, the flipped coordinates form a uniform subset of \(J_{q_-}\) of size \(q_+-q_-\).
Hence \(\mathbb E[\Delta\mid\text{initial state}]\le C(q_+-q_-)N^{-3/2}I\).
Use this bound before discarding later exceptions.
Both endpoint near counts are \(O(Na)\) in expectation, and the negligible failures of the initial guard cost at most \(mN\) each for the eligible index count.
This proves the claimed expected bound.

The independent binomial \(q\) has maximum atom \(C/\sqrt N\).
Multiply the expected index count by \(Cl/\sqrt N\), and add the binomial tails and the arbitrary polynomial chain exceptions for (2).
This gives (1).
The pencil \(H-E\) is full because setting the first scalar variable large and the other scalar variables to zero gives an invertible evaluation.
The [polynomially clipped logarithms](Yin_C_F0186_v40.md#band) converge almost surely under the original law by their fixed-clip assembly and row concentration, before using any translation modulus.
Together with (1) they give ordinary convergence in probability and almost surely along \(2^j\), the latter by first Borel--Cantelli.
The fixed-clip upper bound holds over all \(N\), giving the full limsup on the same event.

<a id="examples"></a>
## Irreducible three-dimensional spaces and scalar continuants

For \(m=2\) take \(I,\sigma_x=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right),\sigma_z=\operatorname{diag}(1,-1)\) as the three random coefficients and \(C=0\).
All three are invertible, and they generate the full matrix algebra.
One has \(M(z)=m_3(z)I\) with \(-1/m_3=z+3m_3\), \(\operatorname{Im}m_3>0\).
On the Pauli basis the eigenvalues of \(\mathcal S\) are \(3,1,1,-1\).
For \(|E|<2\sqrt3\), \(|m_3(E+i\eta)|\le1/\sqrt3\), and \(1-3m_3^2\ne0\) uniformly along that ray, by the quadratic formula and its interior boundary value.
The other three stability denominators stay at distance at least \(2/3\) from zero.
Thus (1) applies at each such fixed energy, including zero inside the spectrum.

For any \(m\ge2\), choose distinct nonzero real slopes \(d_1,\ldots,d_m\), random coefficients \(I,D=\operatorname{diag}(d_i)\), and a sufficiently small fixed Hermitian drift \(C\).
At energy zero when \(C=0\) the diagonal Dyson entries \(m_j\) solve \(-1/m_j=z+(1+d_j^2)m_j\).
The stability denominators in matrix units are \(1-(1+d_i d_j)m_i m_j\).
For \(i\ne j\), \(|1+d_id_j|<\sqrt{(1+d_i^2)(1+d_j^2)}\) and \(|m_i|\le(1+d_i^2)^{-1/2}\).
For \(i=j\) each \(m_i\) is positive imaginary on the vertical ray and has a positive imaginary boundary value.
These facts give uniformly bounded inverse stability there.
The condition persists for all sufficiently small Hermitian \(C\): on a compact vertical segment including \(\eta=0\) the implicit function theorem gives a continuous nearby branch, uniformly positive in its imaginary part and with invertible derivative on a finite covering.
It equals the positive Dyson solution for \(\eta>0\) by uniqueness.
For large \(\eta\) the resolvent bound \(\|M\|\le1/\eta\) and a Neumann series give uniform stability independently.
A connected tridiagonal drift with nonzero neighboring couplings is irreducible with \(D\) and \(I\), and the coefficient space has dimension exactly three.

Take such a real symmetric tridiagonal \(C\), with diagonal \(h_j\) and neighboring entries \(k_j\ne0\).
For selfadjoint indeterminates \(x,y\) set \(U_j=x+d_jy+h_j\) and
\[
 T_0=1,\qquad T_1=U_1,\qquad T_j=U_jT_{j-1}-k_{j-1}^2T_{j-2}.
\]
The scalar polynomial \(T_m\) obeys the same ordinary-log convergence at zero, along the same dyadic dimensions, and the corresponding all-size limsup, with the free scalar trace.
Indeed permute column blocks to order \(2,\ldots,m,1\) in the tridiagonal pencil.
The leading pivot is lower triangular with diagonal \(k_1,\ldots,k_{m-1}\).
Solving the first \(m-1\) equations with zero right sides gives \(v_j=(-1)^{j-1}(k_1\cdots k_{j-1})^{-1}T_{j-1}v_1\).
The final Schur complement is \((-1)^{m-1}(k_1\cdots k_{m-1})^{-1}T_m\).
The absolute finite determinants agree, since the pivot cancels its scalar multiplier, and the same triangular Schur factors and multiplicativity give \(\log\Delta(T_m)=m\log\Delta_{\operatorname{tr}_m\otimes\tau}(H(s))\).
A prescribed scalar shift is covered when it has this realization with the stated Hermitian coupling and stability.
The bound does not assert a floor for all shifts or nonselfadjoint three-direction pencils.

## Current assessment
[Selected decision](#decision-monotone-sign-reviewed)

## Assessment history

### Decision monotone-sign-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:24 |
| status | open |
| reason | The stable local law and growth along the original diagonal sign chain give a polynomial least-value estimate at the specified energies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Stable Hermitian sign pencils](#statement) | A definite sign direction, the stated Dyson stability and ordinary dyadic limits. |
| argument | [Local subspace estimates](#argument) | Original Kronecker law, fixed sign counts and a diagonal-free comparison. |
| support | [Available site mass](#negative-sites) | Sampling in the two spectral windows and conditioning on the current state. |
| support | [Spectral crossings](#crossings) | Min-max growth, endpoint trace estimate and binomial probability. |
| support | [Irreducible examples](#examples) | Three full-rank coefficient directions and exact scalar tridiagonal realizations. |

### Decision monotone-sign-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:31 |
| status | proved |
| reason | A definite physical diagonal sign direction and the stable local law give a polynomial floor in the original sign ensemble. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Stable diagonal sign flow](#statement) | The model, exact hypotheses, fixed parameters and coupling requirements. |
| argument | [Complete argument](#argument) | A definite physical diagonal sign direction and the stable local law give a polynomial floor in the original sign ensemble. |
| support | [Available sites](#negative-sites) | Two spectral windows and concentration under sampling without replacement. |
| support | [Crossings](#crossings) | Min-max increment and the expected number of eligible indices. |
| support | [Examples](#examples) | Irreducible Hermitian three-direction spaces and their scalar tridiagonal applications. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0364_v1.md#monotone-sign-whole-proof) | All stated conclusions at the indicated interfaces. |
