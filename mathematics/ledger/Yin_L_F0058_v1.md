---
author: Yin
---

# F0012: conditional Gaussian subclasses and logarithmic-tail strategies

Date and owner: 2026-11-04T16:14 UTC, Yin.
This synthesis answers the request to inspect [F0012](../tasks/Yin_T_F0012_v1.md#contract), search and propose feasible strategies.
The main agent and three development subagents contributed source checks and calculations.
This is strategy development and self-checking, not independent proof review, a new Claim assessment or Task completion.

<a id="source-boundary"></a>
## Sources and search boundary

The search on 2026-11-05 in Asia/Shanghai covered GUE and Hermitian polynomial Brown-measure convergence, least singular values, quadratic models, elliptic products, Gaussian anti-concentration and pseudospectral regularization.
It reused the existing source inspections and the recorded corrections to Han26. [Han26](../audits/literature/Han26/Yin_U001.md#gue-boundary), [BSS18](../audits/literature/BSS18/readme.md), [formula corrections](../audits/literature/Han26/Yin_U001.md#local-corrections), [shift dependence](../audits/literature/Han26/Yin_U001.md#shift-dependence).
Precise searches for \(H_1H_2+2H_2H_1\) and polynomials linear in one of two GUE inputs did not locate an existing theorem for the subclass below.
No general solution of F0012 was found.
These bounded searches establish neither nonexistence nor novelty.
They stopped after locating a concrete subclass mechanism and the remaining general logarithmic-tail problem.

| Source and inspected edition | Inspected input and use |
| --- | --- |
| [Han26, arXiv:2606.01664v1](https://arxiv.org/html/2606.01664v1#S1.SS2) | Theorem 1.2 covers holomorphic Ginibre polynomials; Question 1.8 excludes the adjoint extension from its framework. The local audit supplies the detailed hermitization interface and exposed-column obstruction. |
| [CGP22, arXiv:1912.04588v1, Corollary 1.3, p. 5](https://arxiv.org/pdf/1912.04588#page=5) | Mean normalized resolvent comparison for self-adjoint GUE polynomials with error \(CN^{-2}(\eta^{-5}+\eta^{-2})\). The statement and hypotheses were checked, not the full proof. |
| [SS15, arXiv:1305.1920v1, Theorem 1.1(5)(6), Corollary 1.2, pp. 2-3](https://arxiv.org/pdf/1305.1920#page=2) | Algebraic Cauchy transform, Puiseux expansions and atomlessness for nonconstant self-adjoint scalar semicircular polynomials. Statements were checked, not full proofs. |
| [Nie22, arXiv:2111.05553v2, Definition 1.5 and Theorem 1.6](https://arxiv.org/html/2111.05553v2#S1.SS2) | Least-singular-value estimate for jointly Gaussian complex matrices under global bilinear small-ball and norm quantile conditions, including nonzero means. The statement was checked; its proof remains an external input. |
| [BKMS21, arXiv:1906.11819v4, Theorem 1.5, pp. 2-3](https://arxiv.org/pdf/1906.11819#page=2) | Eigenvector-overlap control under independent additive Ginibre perturbations. A methodological model only; its noise hypothesis does not automatically hold for GUE polynomials. |

These source observations remain with the comparison instead of being duplicated in U.
Bibliographic keys identify published works; theorem numbering above refers to the stated preprints.
The inspected [DHH+25, Theorem 1.21](https://arxiv.org/html/2510.10712v1#S1.SS2.SSS2) still requires bi-invariant random-walk steps.
Its introductory description of quadratic GUE convergence cannot replace its cited quadratic Ginibre source.
It supplies no general F0012 conclusion.

<a id="common-bridge"></a>
## The common analytic bridge

Use the Task normalization, and set \(A_N:=P(H^{(N)})\), \(a:=P(s)\), \(Q_z:=(P-z)^*(P-z)\).
Let \(\nu_N^z\) denote the empirical law of the **squared** singular values of \(A_N-zI\).
For nonconstant \(P\) of degree \(m\), the top part of \(Q_z\) is \(P_m^*P_m\ne0\).
Thus \(Q_z\) is nonconstant for every fixed \(z\); constant \(P\) is trivial.

CGP22 with coefficient amplification size one gives
\[
 |\mathbb E G_{Q_z(H^{(N)})}(w)-G_{Q_z(s)}(w)|
 \le C_{P,z}N^{-2}\big((\Im w)^{-5}+(\Im w)^{-2}\big),\qquad \Im w>0.
\]
SS15 gives atomlessness and a Puiseux expansion at zero.
The Stieltjes bound excludes powers below \(-1\), and absence of an atom excludes a pole of order one.
Hence some \(0<\alpha_z\le1\) satisfies
\(t|\Im G_{Q_z(s)}(it)|\le C_z t^{\alpha_z}\) for \(0<t\le1\).
The inequality \(1_{[0,t]}(x)\le2t^2/(x^2+t^2)\) yields
\[
 \mathbb E\nu_N^z([0,t])\le C_z(t^{\alpha_z}+N^{-2}t^{-4}).
\]
Choose \(0<\gamma_z<2/(4+\alpha_z)\).
For \(N^{-\gamma_z}\le t\le1\), this is at most \(C_z t^{\alpha_z}\).
This is a direct source specialization; the constants initially depend on \(z\).

A sufficient remaining target is: for almost every fixed \(z\), find \(0<\kappa_z<\alpha_z\gamma_z\) with
\[
 \mathbb P\{s_{\min}(A_N-zI)^2<e^{-N^{\kappa_z}}\}\longrightarrow0.
 \tag{F}
\]
On its good event the negative log contribution below \(N^{-\gamma_z}\) is at most
\(N^{\kappa_z}\nu_N^z([0,N^{-\gamma_z}])\), whose expectation is \(O(N^{\kappa_z-\alpha_z\gamma_z})\).
Above that scale, integration by parts bounds the tail up to \(\varepsilon\) by
\(O(\varepsilon^{\alpha_z}(1+|\log\varepsilon|)+(\log N)N^{-\alpha_z\gamma_z})\).
Markov's inequality therefore gives logarithmic uniform integrability under (F).
A polynomial lower bound is sufficient but stronger than necessary.

The potential is \(u_N(z):=N^{-1}\log|\det(A_N-zI)|=\frac12\int\log x\,d\nu_N^z(x)\) away from the finite eigenvalue set.
At a fixed positive cutoff, star-moment convergence and norm control identify the limit.
First \(N\to\infty\), then cutoff removal, gives pointwise convergence in probability for almost every \(z\).
On \(\|A_N\|\le M\), the eigenvalue formula gives a uniform local \(L^2\) bound for \(u_N\).
Thus the convergence is local \(L^1\) in probability.
The distributional Laplacian with factor \(1/(2\pi)\), followed by norm-based tightness, gives F0012.
This uses the [retained hermitization interface](../audits/literature/Han26/Yin_U001.md#hermitization).
The full-class estimate (F) remains unproved.

<a id="conditional-gaussian"></a>
## First route: conditional Gaussianity of the original matrix

Take \(P(x,y):=xy+2yx\).
For \(X=\operatorname{diag}(1,2)\), \(Y=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), its value is \(\begin{pmatrix}0&5\\4&0\end{pmatrix}\), which is nonnormal.
In contrast, \(xy+i\,yx\) satisfies \(P^*=-iP\), so is a scalar multiple of a self-adjoint polynomial and is a poor stress test.

Condition on \(H_1=U\operatorname{diag}(\lambda_i)U^*\).
By invariance and independence, \(h:=U^*H_2U\) retains the independent normalized GUE law.
For the following conditional calculation, write \(A_N\) for its unitary conjugate \(U^*A_NU\); singular values, operator norms and determinants are unchanged.
Then \(A_{ij}=(\lambda_i+2\lambda_j)h_{ij}\), and for unit \(v,w\),
\[
 \mathbb E_{H_2}|v^*A_Nw|^2
 =N^{-1}\sum_{i,j}|v_i|^2|w_j|^2|\lambda_i+2\lambda_j|^2.
 \tag{G}
\]
Indeed \(\mathbb E h_{ij}\overline{h_{kl}}=N^{-1}\delta_{ik}\delta_{jl}\).
Hermitian correlation does not invalidate this conjugated covariance.

The Task density gives the Gaussian orthogonal decomposition
\[
 H_1=H_1^0+(g/N)I,\qquad g:=\operatorname{Tr}H_1\sim N(0,1),
\]
with \(g\) independent of the traceless part.
This follows from \(\operatorname{Tr}(H_1^2)=\operatorname{Tr}((H_1^0)^2)+g^2/N\).
Conditionally on \(H_1^0\), each coefficient is
\(\lambda_i^0+2\lambda_j^0+3g/N\), whose real density is at most \(CN\).
The union bound, including \(i=j\), gives
\[
 \mathbb P\{\min_{i,j}|\lambda_i+2\lambda_j|\le\delta\}\le CN^3\delta.
 \tag{W}
\]
Thus \(B>3\) gives the coefficient lower bound \(N^{-B}\) with probability tending to one.

On that event (G) is at least \(N^{-2B-1}\).
A complex Gaussian scalar has a real projection with at least half its total variance.
The real Gaussian density bound, uniformly in its mean, implies
\[
 \inf_{\|v\|=\|w\|=1}
 \mathbb P_{H_2}\{|v^*(A_N-zI)w|>cN^{-B-1/2}\}\ge\tfrac12.
\]
This is Nie22's condition for complex matrices, including the shift.
On \(\|H_1\|\le R\), \(\|A_N-zI\|\le3R\|H_2\|+|z|\), so a fixed conditional norm quantile \(s=s_{R,z}\) exists.
Nie22 gives
\[
 \mathbb P\{s_{\min}(M)\le\varepsilon^2 b^2/(N^3s)\}\le C\varepsilon
\]
for bilinear threshold \(b\) and \(\mathbb P(\|M\|>s)\le1/8\).
Take \(b=cN^{-B-1/2}\) and \(\varepsilon=N^{-r}\), \(r>0\).
The resulting development estimate is
\[
 \mathbb P\{s_{\min}(A_N-zI)\le c_{R,z}N^{-(2B+4+2r)}\}
 \le CN^{3-B}+CN^{-r}+\mathbb P(\|H_1\|>R).
 \tag{N}
\]
For fixed \(R>2\), this tends to zero.
This supplies a concrete bridge to the subclass through (F).
The assembled subclass argument still awaits focused checking and formal assessment; no proved Claim is registered here.

The extension to try is
\[
 P(x,y):=q(x)+\sum_\ell f_\ell(x)y g_\ell(x),\qquad
 K(u,v):=\sum_\ell f_\ell(u)g_\ell(v).
\]
A convenient sufficient condition is \(K_m(1,1)\ne0\), where \(K_m\) is the highest homogeneous part of degree \(m\).
Then \(K(u+t,v+t)\) has fixed leading coefficient \(K_m(1,1)\).
After trace splitting, the polynomial in \(g\) has leading coefficient \(N^{-m}K_m(1,1)\).
If its modulus is at most \(\delta\), root factorization puts real \(g\) within \(CN\delta^{1/m}\) of one of its at most \(m\) complex roots.
The bounded Gaussian density and union bound yield \(CN^3\delta^{1/m}\).
Taking \(B>3m\) supplies the same coefficient lower bound and conditional Nie argument.
A nonzero constant \(K\) requires no such estimate.
The deterministic \(q(H_1)\) changes only the mean and norm quantile.
The hypothesis is sufficient, not necessary; \(K=u-v\) has zero diagonal weights and is outside this argument.
Polynomials nonlinear in every possible conditioned input do not retain joint Gaussianity.
Success on this subclass does not complete F0012.

<a id="schur-route"></a>
## Second route: normalized Schur-complement anti-concentration

The [Han26 linearization](../audits/literature/Han26/Yin_U001.md#linearization) can be evaluated on self-adjoint inputs.
For fixed \(z\ne P(0)\) it gives \(T_N:=I_m\otimes I_N+\sum_j R_j(z)\otimes H_j^{(N)}\), with fixed \(m\), and root inverse compression relates it to \(P(H)-zI\).
Losses depend on fixed \(P,z\), not \(N\); the single excluded shift is harmless for planar hermitization.

Deleting only one column loses the independence used in Han26.
Delete its physical row and column together and write
\[
 T_N=\begin{pmatrix}D&B\\C&Q\end{pmatrix},\qquad S:=D-BQ^{-1}C.
\]
The minor \(Q\) is independent of exposed GUE entries.
On invertible minors, \(S\) is a fixed-size matrix-valued quadratic Gaussian polynomial.
The actual distance to the other block columns is represented by
\[
 F:=(I+BQ^{-1}Q^{-*}B^*)^{-1/2}S.
 \tag{S}
\]
The row operator \([I,-BQ^{-1}]\) annihilates those columns and has the displayed Gram matrix.

A sufficient target is \(\mathbb P\{s_{\min}(F_a)<e^{-N^\kappa}\}=o(N^{-1})\) per block, including exceptional minor events.
The union bound and
\(\|T_N^{-1}\|_{\mathrm{HS}}^2=\sum_a\|F_a^{-1}\|_{\mathrm{HS}}^2\)
give \(s_{\min}(T_N)\ge e^{-N^\kappa}/\sqrt{mN}\).
A slightly larger \(\kappa'<\alpha_z\gamma_z\) absorbs the factor and the passage to squared singular values in (F).
An averaged block estimate could replace the union bound.
No such full-class bound is established here.

Fixed-degree anti-concentration of \(\det S\) alone is insufficient.
For instance \(\begin{pmatrix}1&Mg\\0&1\end{pmatrix}\) has determinant one but smallest singular value of order \(1/|Mg|\) when \(|Mg|\) is large.
One must control the graph normalization, adjugate scale and typical minors, without assuming a bound for every invertible \(Q\).

For the pilot \(xy+2yx\), an exact pencil is
\[
 L_z=\begin{pmatrix}-zI&H_1&2H_2\\H_2&-I&0\\H_1&0&-I\end{pmatrix}.
\]
Its root Schur complement is \(P(H)-zI\).
The random coefficients \(E_{12}+E_{31}\) and \(2E_{13}+E_{21}\) generate \(M_3(\mathbb C)\): their squares give \(E_{32}\), \(2E_{23}\), then products give diagonal projections and all remaining matrix units.
Yet take auxiliary directions \(e_2,e_2\) and orthogonal physical vectors: both mean and every random coefficient vanish in that bilinear form.
Therefore irreducibility does not imply Nie22's global small-ball condition for a sparse linearization.
Use the first route as a simpler comparison on this pilot; test broader reach on \(x^2y^2+2y^2x^2\), nonlinear in both inputs.

<a id="averaged-route"></a>
## Third route: planar logarithmic defect and structured smoothing

Now use ordinary singular values:
\[
 F_N^z(t):=N^{-1}\#\{j:s_j(A_N-zI)<t\},\qquad
 D_N(K,\varepsilon):=\int_K\int_0^\varepsilon F_N^z(t)\frac{dt}{t}\,d^2z.
\]
The sufficient target, for every compact \(K\) and \(\delta>0\), is
\[
 \lim_{\varepsilon\downarrow0}\limsup_N\mathbb P\{D_N(K,\varepsilon)>\delta\}=0.
 \tag{A}
\]
This is the local \(L^1\) gap between \(u_N\) and
\(u_{N,\varepsilon}:=N^{-1}\sum_j\log\max(s_j(A_N-zI),\varepsilon)\).
The fixed-cutoff limit then gives F0012 without a uniform-in-\(z\) smallest singular value bound.

A stronger concrete subtarget is
\[
 \mathbb P\{A_N\text{ diagonalizable and }\kappa_V(A_N)\le N^{C_P}\}\to1,
 \quad \kappa_V(A):=\inf_{A=VDV^{-1}}\|V\|\|V^{-1}\|,
 \tag{V}
\]
with \(D\) diagonal, as in BKMS21.
No general GUE-polynomial theorem for (V) was found.
On its good event,
\(s_{\min}(A_N-zI)\ge N^{-C_P}\operatorname{dist}(z,\operatorname{Spec}A_N)\).
Integrating logarithmic kernels over at most \(N\) disks of radius \(N^{C_P-b}\) gives
\[
 D_N(K,N^{-b})\le(\pi/2)N^{1+2C_P-2b}=o(1),\qquad b>C_P+1/2.
\]

The common mass estimate, converted from squares, gives for almost every \(z\) some \(a_z,\beta_z,C_z>0,N_z\) with
\(\mathbb EF_N^z(t)\le C_z t^{\beta_z}\) for \(N\ge N_z\) and \(N^{-a_z}\le t\le1\).
One may take \(a_z=\gamma_z/2\) and \(\beta_z=2\alpha_z\).
No uniform compact-set constants are assumed.
Take increasing measurable \(E_j\subset K\) where the relaxed estimate
\(\mathbb EF_N^z(t)\le j t^{1/j}\) holds for \(N\ge j\), \(N^{-1/j}\le t\le1\).
Countably many rational thresholds define such sets, and the pointwise bounds give \(|K\setminus E_j|\to0\).

On \(\|A_N\|\le M\), \(\|u_N\|_{L^2(K)}\le C_{M,K}\) and
\(u_N\le u_{N,\varepsilon}\le B_{M,K}\).
Thus
\(\int_E(u_{N,\varepsilon}-u_N)\,d^2z\le C'_{M,K}|E|^{1/2}\)
for every measurable \(E\subset K\), uniformly in \(N,0<\varepsilon<1\).
First fix large \(j\) to control \(K\setminus E_j\).
For \(b>\max(C_P+1/2,1/j)\), split the defect on \(E_j\) at \(N^{-b}\) and \(N^{-1/j}\).
The bottom part has the disk bound; the middle expectation is at most
\(j|K|(b-1/j)(\log N)N^{-1/j^2}\), and the upper expectation is at most
\(j^2|K|\varepsilon^{1/j}\).
Intersect with the norm and (V) good events and apply Markov's inequality to the middle and upper parts.
First \(N\to\infty\), then \(\varepsilon\downarrow0\), proves (A) under (V).

A possible mechanism is GUE input refresh
\[
 H_j(t):=e^{-t/2}H_j+\sqrt{1-e^{-t}}H'_j\stackrel d=H_j
\]
with fresh independent GUE inputs.
A conditional estimate for the refreshed polynomial would transfer to the original law without removing external output noise.
Its output perturbation is correlated and polynomial, so BKMS21 is only a model.
The first test is a quantitative nondegeneracy condition controlling overlaps or pseudospectral area under this structured refresh.
The nonlinear remainder cannot be discarded without a stability argument.
If (V) recreates the original difficulty, retain the weaker target (A) and deprioritize the eigenvector formulation.

<a id="failed-shortcuts"></a>
## Excluded shortcuts and remaining scope

Star moments and limiting logarithmic integrability do not control the finite-\(N\) tail.
The nilpotent shift \(J_N\) has eigenvalue law \(\delta_0\) and star-moment limit a Haar unitary.
Its potential \(\log|z|\) differs from the Haar Brown potential, which is zero in the unit disk.
The planar logarithmic defect therefore stays positive.
This deterministic sequence is not a counterexample to F0012.

Nor does vanishing perturbation norm imply continuity of eigenvalue measures.
For \(\delta_N=N^{-c}\), \(J_N+\delta_N E_{N1}\) has characteristic polynomial \(z^N-\delta_N\); its eigenvalue radii tend to one although the perturbation norm tends to zero.
An independent-output-noise result consequently needs an additional stability argument to address the unperturbed Task.

The full determinant has degree proportional to \(N\).
A scalar small-ball exponent inversely proportional to that degree gives no useful floor at \(e^{-N^\kappa}\) with \(\kappa<1\).
The first route instead uses joint Gaussianity; the second seeks fixed-size blocks with their necessary normalization.

Prioritize the conditional Gaussian subclass, then the general normalized Schur obstruction, retaining the averaged route as a distinct backup.
No numerical experiment, full-class tail estimate, independent review or new mathematical status is claimed.
