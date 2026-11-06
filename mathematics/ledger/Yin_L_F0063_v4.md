---
author: Yin
---

<a id="strong-single-pole-rectangle-test"></a>
# Actual-minor rectangle spread and a strong-single-pole resonance test

This ordinary test for Yin, dated 2026-11-06T08:23 UTC, checks one proposed use of the adopted [C194v17 rectangles](../claims/Yin_C_F0194_v17.md#statement) in the free-gap high-inverse-energy branch of the [matrix-pencil contract](../tasks/Yin_T_F0013_v1.md#contract).
It gives an actual-minor polynomial spread bound and a conditional original-law small-ball bound for a frozen quadratic proxy.
It does not establish the corresponding bound for the complete Schur polynomial or refute the possibility of such a bound.
This is ordinary exploration and authoring self-checking, not an independent review or a new Claim assessment.
The [D10 development](../drafts/Yin_D_F0010.md#strong-single-pole-rectangle-test) is extraction provenance; the complete bounded test is retained below.
It continues the [positive-frame physical-interface comparison](Yin_L_F0063_v3.md#positive-frame-physical-boundary), without claiming that the strong one-pole branch is typical or exhaustive.

<a id="model"></a>
## Exact original model and the branch being tested

Fix \(d\ge1\) and real symmetric \(A_0,\ldots,A_d\in M_3(\mathbb R)\), independently of \(N\), with
\[
 \chi_A=\inf_{\substack{u,v\in\mathbb C^3\\\|u\|=\|v\|=1}}
              \sum_{j=1}^d|u^*A_jv|^2>0.
\]
For input \(j\), the independent upper off-diagonal entries of the real symmetric \(W_j^{(N)}\) have the fixed real law \(\xi_j/\sqrt N\), with \(\mathbb E\xi_j=0\) and \(\mathbb E\xi_j^2=1\).
Its independent diagonal entries have a fixed real centered finite-second-moment law \(\zeta_j/\sqrt N\); lower entries are the symmetric copies.
All original coordinates and inputs are independent within each size, while cross-size coupling is arbitrary.
No density, bounded-support condition or moment above two is imposed.
Put
\[
 L_N=A_0\otimes I_N+\sum_j A_j\otimes W_j^{(N)},\qquad
 L=A_0\otimes1+\sum_j A_j\otimes s_j,
\]
where the \(s_j\) are free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal trace \(\tau\).
Assume \(0\notin\sigma(L)\).
The original objective is the finite-target determinant limsup under every coupling,
with normalization \(1/(3N)\) and free trace \(\operatorname{tr}_3\otimes\tau\).
This record analyzes only the actual-minor branch displayed below and supplies no unconditional determinant conclusion.

Fix one deterministic real sequence \(\theta_N\to0\) and an integer \(r\ge0\).
In the one-pole branch, \(e\in\mathbb R^{3n}\) is a real unit eigenvector of the actual real symmetric minor \(M\), and \(\lambda\in\mathbb R\setminus\{0\}\) is its signed inverse eigenvalue:
\[
 Me=\lambda^{-1}e,\qquad M^{-1}e=\lambda e.
\]
Thus the transposes, real quadratic polynomials and real MNV16 theorem below refer to these real objects.
The measurable spectral choice retains the sign of \(\lambda\); no complex eigenvector or absolute eigenvalue is substituted.
Constants may depend on the fixed coefficients and laws, the deletion bound, and the fixed branch/guard constants \(K,c_0,B_0\), but not on \(N,\lambda\) or a particular good conditioning.

<a id="actual-minor-spread"></a>
## Exact C194v17 normalization for actual fixed-deletion minors

For a deterministic physical deletion set \(S\), \(|S|\le r+1\), put \(n=N-|S|\) and
\[
 M_{N,S}=(A_0+\theta_NI_3)\otimes I_n+
                      \sum_jA_j\otimes W_{j,N,S}.
\]
All entries of the actual input minors still have normalization \(N^{-1/2}\).
Apply C194v17 at dimension \(n\) to
\[
 \widetilde M=\sqrt{N/n}\,M_{N,S}.
\]
Its random entries now have the exact prescribed laws divided by \(\sqrt n\), the noise coefficients remain the original \(A_j\), and its deterministic affine term is \(\sqrt{N/n}(A_0+\theta_NI_3)\otimes I_n\).
C194v17 is uniform over that deterministic term, so no varying-coefficient theorem is required.

Let \(a_{\rm R},\delta_{\rm R},c,C\) be its constants.
For deterministic \(b_N\ge1\), on its rectangle event for \(\widetilde M\) and the minor-measurable guard \(\|M_{N,S}\|\le b_N\), every real unit vector \(e=(e_k)_{k\in[n]}\) with
\[
 \|M_{N,S}e\|\le\frac{a_{\rm R}}{4\sqrt N}
\]
has more than \(\lfloor\delta_{\rm R}n\rfloor\) physical blocks satisfying
\[
 \|e_k\|>\frac{a_{\rm R}}{8b_N\sqrt{Nn}}.
 \tag{Single-pole-actual-minor-spread}
\]
Indeed the norm guard after scaling is \(\widetilde b_n=\sqrt{N/n}\,b_N\), and the two displayed conditions are exactly
\(\|\widetilde M e\|\le a_{\rm R}/(4\sqrt n)\) and
\(\|e_k\|>a_{\rm R}/(8\widetilde b_n n)\).
For each such deterministic minor the rectangle failure is at most \(Ce^{-cn}\).
A union bound over the at most \(O_r(N^{r+1})\) fixed-deletion sets still gives exponentially small failure up to that polynomial factor.
The assertion therefore includes the parent and all these actual minors, and applies to any measurably selected eigenmode because the rectangle event already covers every qualifying unit vector.

The original [Frobenius guard](../claims/Yin_C_F0186_v22.md#frobenius-norm-guard) permits \(b_N=B_0\sqrt N\) for fixed sufficiently large \(B_0\), with probability tending to one.
Compression bounds every minor's norm by that of the full parent, so this gives a simultaneous unconditional norm guard without a union of \(o(1)\) norm errors.
For a conditional fresh-row argument, however, the good event uses the actual minor guard \(\|M_{N,S}\|\le B_0\sqrt N\), not the full-parent norm event that could involve that fresh row.
Under this guard, (Single-pole-actual-minor-spread) gives
\[
 \#\{k:\|e_k\|>\kappa N^{-3/2}\}\ge c_1N
 \tag{Single-pole-polynomial-block-spread}
\]
for fixed \(\kappa,c_1>0\) and all sufficiently large \(N\).
For an actual inverse eigenmode \(M_{N,S}e=\lambda^{-1}e\) with \(|\lambda|\ge c_0N\), the required near-zero condition holds eventually.
This lower bound is small: the guaranteed squared mass in the displayed blocks is only of order \(N^{-2}\).
It supplies no bound tending to zero for \(\max_k\|e_k\|^2\), and is not the head delocalization used by the spectral-point coefficient theorem.

<a id="frozen-proxy"></a>
## Stable residual background and the actual original-row proxy

Now expose one physical block of an actual parent, with retained minor \(M\), original border \(R\), and original diagonal correction \(D_i\).
Explicitly, \(R e_a=\sum_j(A_je_a)\otimes x_j\), where \(e_a\) is an auxiliary standard basis vector and \(x_{j,k}=\xi_{j,k}/\sqrt N\), while \(D_i=\sum_jA_jW_{j,ii}\).
Work on the minor-measurable spectral branch
\[
 Z=M^{-1}=E+\lambda ee^T,\qquad
 \|e\|=1,\quad Ee=0,\quad
 \|E\|_F^2/N\le K,\quad |\lambda|\ge c_0N,
 \tag{Single-pole-branch}
\]
where \(K,c_0>0\) are fixed and the spectral choice is measurable under the original retained input minors.
Here \(K\) may be enlarged to at least one.
The original \(d\) border rows remain independent of those minors and of the exposed diagonal after conditioning on their sigma-field \(\mathcal F\).

Use only the [rank-background comparison in C194v20](../claims/Yin_C_F0194_v20.md#finite-poles-and-trace-tail-boundary), whose direct spectral calculation in this one-mode case is
\[
 \|g_\eta-g_E\|\le\eta K+\frac1{N\eta}.
\]
Here \(g_\eta=N^{-1}\sum_k[(M-i\eta I)^{-1}]_{kk}\), \(g_E=N^{-1}\sum_kE_{kk}\), and the sums use the actual three-by-three physical diagonal blocks.
Together with the adopted [actual-minor fixed-eta identity](../claims/Yin_C_F0194_v18.md#fixed-eta-identity), this gives relative marginal probability tending to zero for
\(\|B_Eg_E-I_3\|>1/2\) on (Single-pole-branch), where
\(B_E=A_0+\theta_NI_3-\sum_jA_jg_EA_j\).
This does not invoke C194v20's small nuclear-error conclusion, whose hypothesis fails in the strong-pole regime.
With \(h_K=\sqrt{3K}\), the good event gives \(s_{\min}(B_E)\ge(2h_K)^{-1}\) and \(\|B_E\|\le C_K\).
Also restrict the already conditioned diagonal to \(\|D_i\|\le(8h_K)^{-1}\), whose complementary marginal probability tends to zero.
Set
\[
 B=B_E+D_i,\qquad S_E=A_0+\theta_NI_3+D_i-R^TER.
\]
Then \(B\) is \(\mathcal F\)-measurable, \(s_{\min}(B)\ge3/(8h_K)\), and \(\|B\|\le C_K\).
The [original finite-second-moment quadratic estimate](../claims/Yin_C_F0194_v18.md#quadratic-concentration) gives
\[
 \mathbb E[\|S_E-B\|\mid\mathcal F]\le q_N(K),\qquad q_N(K)\to0.
 \tag{Single-pole-residual-error}
\]
Thus the exposed diagonal has been retained in the frozen background, and the remaining error is precisely the original residual-row quadratic fluctuation.

Write the raw original border variables as \(\xi_{j,k}\), before division by \(\sqrt N\), and put
\[
 z=\sqrt N\,R^Te=\sum_k V_k\xi_k,\qquad
 V_k=(A_1e_k,\ldots,A_de_k),\qquad
 \xi_k=(\xi_{1,k},\ldots,\xi_{d,k})^T.
\]
The original positive frame gives
\[
 V_kV_k^T\succeq\chi_A\|e_k\|^2I_3,\qquad
 \mathbb E[\|z\|^2\mid\mathcal F]
 =\sum_j\|(A_j\otimes I_n)e\|^2\le\Lambda,
 \quad \Lambda=\sum_j\|A_j\|^2.
 \tag{Single-pole-proxy-frame}
\]
In particular this step preserves all \(d\) original input laws rather than replacing \(z\) by an independent auxiliary vector.

Define the conditional frozen proxy
\[
 Q_N=\frac N\lambda\det B-z^T\operatorname{adj}(B)z.
 \tag{Single-pole-frozen-proxy}
\]
Since \(B\) is uniformly invertible on this good conditioning, \(H=\operatorname{adj}(B)\) has \(s_{\min}(H)\ge c_K'>0\).
For distinct physical indices \(k,l\), frame positivity implies
\[
 \|V_k^THV_l\|_F
 \ge\chi_A\|e_k\|\,\|e_l\|\,\|H\|_F.
 \tag{Single-pole-proxy-block-coefficient}
\]
To see this, write the square as
\(\operatorname{Tr}(H V_kV_k^T H V_lV_l^T)\) and apply the two displayed positive-semidefinite lower bounds.
For every pair of the \(c_1N\) spread blocks, some entry has modulus at least \(d^{-1}\|V_k^THV_l\|_F\).
The coefficient of the corresponding distinct raw variables \(\xi_{a,k}\xi_{b,l}\) in \(z^THz\) is twice that entry.
Pairing disjoint spread blocks therefore gives \(c_2N\) pairwise disjoint quadratic monomials, each with coefficient of magnitude at least
\[
 c_3N^{-3}.
 \tag{Single-pole-proxy-matching}
\]
These are coefficients of the normalized proxy \(Q_N\); the corresponding coefficients of \(y^THy\), with \(y=R^Te=z/\sqrt N\), have the extra factor \(N^{-1}\).

This matching does supply a conditional small-ball estimate for \(Q_N\) under the original row laws.
For each original scalar use its exact two-copy representation
\[
 \xi=\frac{\xi'+\xi''}{2}
           +\varepsilon\frac{\xi'-\xi''}{2},
\]
where the copies have that same law and the sign is independent and fair.
Nonzero variance and fixed \(d\) give fixed \(b_0,p_0>0\) such that
\(\mathbb P\{|\xi_j'-\xi_j''|\ge b_0\}\ge p_0\) for every law.
The disjoint pairs in (Single-pole-proxy-matching) survive independently with probability at least \(p_0^2\), so a linear number survive except with probability \(Ce^{-cN}\).
Conditioning all copies converts the proxy to a real multilinear sign polynomial of degree at most two; squares contribute only affine sign terms, and each surviving quadratic coefficient retains a fixed multiple of \(N^{-3}\).
The accepted [MNV16 degree-two finite-interval theorem](../audits/literature/MNV16/Yin_U001.md#quadratic-specialization) consequently gives, for a sufficiently small fixed \(c_4>0\),
\[
 \mathbb P\{|Q_N|\le c_4N^{-3}\mid\mathcal F\}
 \le Ce^{-cN}+C\sqrt{\log N}\,N^{-1/9}\longrightarrow0.
 \tag{Single-pole-original-law-proxy-small-ball}
\]
The interval center and all lower-degree coefficients are unrestricted.
This source use retains the recorded accepted-statement and unreviewed-source-proof boundary; no new external source has been searched or adopted.

<a id="same-row-gap"></a>
## The exact same-row difference does not match that window

The actual complete Schur determinant is
\[
 S=S_E-\lambda yy^T,\qquad
 p=\det S=\det S_E-\lambda y^T\operatorname{adj}(S_E)y.
\]
Normalize the full polynomial, retaining its lower degrees, as
\[
 P_N=\frac N\lambda p
     =\frac N\lambda\det S_E-z^T\operatorname{adj}(S_E)z.
 \tag{Single-pole-complete-normalized-polynomial}
\]
For \(\|S_E-B\|\le\eta\le1\), fixed-dimensional determinant and adjugate estimates give
\[
 |P_N-Q_N|
 \le C_K\eta\left(\frac N{|\lambda|}+\|z\|^2\right)
 \le C_{K,c_0}\eta(1+\|z\|^2).
 \tag{Single-pole-same-row-error}
\]
For example, conditional on the good minor, Markov's inequality yields for every \(L\ge1\)
\[
 \mathbb P\{|P_N-Q_N|>C_{K,c_0}\eta(1+L)
                         \mid\mathcal F\}
 \le q_N(K)/\eta+\Lambda/L.
\]
Taking \(\epsilon_N=q_N(K)+N^{-1}\), \(\eta=\epsilon_N^{1/2}\), and \(L=\epsilon_N^{-1/4}\) proves only \(P_N-Q_N=o_{\mathbb P}(1)\), uniformly on these conditionings.
This argument never treats \(z\) and \(S_E\) as independent.
Before normalization the error carries the factor \(|\lambda|/N\); the displayed normalization handles it explicitly rather than discarding it.

To transfer (Single-pole-original-law-proxy-small-ball) by this comparison, one would need the approximation error to be negligible at its \(N^{-3}\) interval scale.
The adopted finite-second-moment residual estimate supplies no rate ensuring that conclusion.
At a polynomial choice of \(\eta\), the term \(q_N(K)/\eta\) is not known to tend to zero.
An \(o_{\mathbb P}(1)\) error can exceed that window, so it does not prove a polynomial small-ball bound for \(P_N\).
This is the first unsupported transfer in the frozen-proxy approach, not a proof that the original same-row resonance cannot be controlled.

<a id="graph-interface"></a>
## Graph normalization is explicit; complete coefficients remain unproved

The exact spectral orthogonality \(Ee=0\) gives
\[
 \Gamma_E=I_3+R^TE^2R,\qquad
 \Gamma=I_3+R^TZ^2R=\Gamma_E+\frac{\lambda^2}{N}zz^T,\qquad
 \det\Gamma=\det\Gamma_E
       \left(1+\frac{\lambda^2}{N}z^T\Gamma_E^{-1}z\right).
\]
Moreover
\[
 \mathbb E[\operatorname{Tr}\Gamma_E\mid\mathcal F]
 \le3+\Lambda K,\qquad
 \mathbb E[\|z\|^2\mid\mathcal F]\le\Lambda.
\]
On \(\operatorname{Tr}\Gamma_E\le L\) and \(\|z\|^2\le L\), for \(L\ge3\) and \(|\lambda|\ge c_0N\),
\[
 \sqrt{\det\Gamma}
 \le(L/3)^{3/2}\sqrt{1+\lambda^2L/N}
 \le C_{c_0}L^2\,\frac{|\lambda|}{\sqrt N}.
\]
The complementary conditional probability is at most \((3+\Lambda K+\Lambda)/L\).
Hence the actual normalized numerator satisfies
\[
 \frac{|\det S|}{\sqrt{\det\Gamma}}
 \ge \frac{|P_N|}{C_{c_0}L^2\sqrt N}
\]
on that event.
The large pole cancels from this graph comparison, but the required polynomial small-ball estimate for the complete \(P_N\) is still missing.

<a id="conclusion"></a>
## Outcome and first unsupported interface

C17's many small lower bounds do not supply the vanishing maximum head loads and residual own-scale collision bounds used in the [fixed mixed-factor transfer](../claims/Yin_C_F0187_v24.md#mixed-physical-collisions).
Nor does the frozen degree-two matching prove that the actual degree-at-most-six polynomial \(P_N\), after the same two-copy substitution, retains those coefficients: its residual-dependent terms use the same fresh variables and can contribute to the same complete coefficients.
No cancellation counterexample for the actual original minor is claimed.
The bounded test therefore stops at direct control of the complete polynomial or its conditional matching coefficients.
That is a possible next ordinary test; it is not undertaken or assumed in this section.
