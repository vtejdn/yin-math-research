---
author: Yin
---

# Polynomial invertibility of fixed GUE pencils and Brown-measure convergence

Context: [F0012](../tasks/Yin_T_F0012_v1.md#contract).
This proof was developed through coordinated mathematical exploration.
The selected assessment adopts the complete argument with its independent whole-chain review and stated external-theorem acceptance boundary.
No novelty or priority claim is made.

<a id="statement"></a>
## Exact statement

Let \(d,m\ge1\) and fix arbitrary \(R_1,\ldots,R_d\in M_m(\mathbb C)\).
For each \(N\), let \(H_1^{(N)},\ldots,H_d^{(N)}\) be independent Hermitian matrices with density proportional to \(\exp(-N\operatorname{Tr}(H^2)/2)\).
Set
\[
 T_N:=I_m\otimes I_N+\sum_{j=1}^dR_j\otimes H_j^{(N)}.
\]
There is \(A<\infty\), depending only on the fixed coefficients, such that
\[
 \mathbb P\{s_{\min}(T_N)<N^{-A}\}\longrightarrow0.
\]
No irreducibility, positive-capacity or bilinear-covariance nondegeneracy is assumed.
More precisely, for each finite \(M\) there are \(C,\alpha,\varepsilon_0,c>0\), independent of \(N\), such that for all sufficiently large \(N\) and \(0<\varepsilon\le\varepsilon_0\),
\[
 \mathbb P\{s_{\min}(T_N)\le\varepsilon,\ \max_j\|H_j^{(N)}\|\le M\}
 \le C N^{5/2}\varepsilon^\alpha
       \exp(CN^{5/2}\varepsilon^\alpha)+e^{-cN^2}.
 \tag{P}
\]

Consequently, fix any scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\), with degree and coefficients independent of \(N\), in self-adjoint indeterminates.
If \(s_1,\ldots,s_d\) are free centered semicircular elements of variance one in a finite von Neumann algebra with faithful normal tracial state, then
\[
 \frac1N\sum_{j=1}^N\delta_{\lambda_j(P(H^{(N)}))}
 \ \longrightarrow\ \mu_{P(s)}^{\mathrm{Br}}
\]
weakly in probability on \(\mathbb C\), with algebraic eigenvalue multiplicities.
The meaning of weak convergence is the one in the exact F0012 contract.

<a id="inputs"></a>
## External inputs and inspection limits

The proof accepts the real polynomial distance inequality (KS2) stated on p. 2 of Kurdyka--Spodzieja--Szlachcinska, arXiv:1412.5088v1, and Lotz's Theorem 1.1 in arXiv:1210.3742v4 at their explicit statements below.
Their statements and hypotheses were read in the primary sources.
The adaptations to singular zero sets, Gaussian measure and Hermitian input spaces are proved here; they are not attributed to the sources.
The full original proofs of those external theorems have not been independently re-audited.

For the final Brown-measure application, the accepted external inputs are the normalized-GUE star-moment limit and bounded norm event, the resolvent comparison in CGP22 Corollary 1.3 at arXiv:1912.04588v1, and SS15 Theorem 1.1(5)(6) and Corollary 1.2 at arXiv:1305.1920v1.
The latter two statements and their hypotheses were inspected directly.
The standard GUE convergence and Brown hermitization conventions have the [retained source inspection](../audits/literature/Han26/Yin_U001.md#hermitization).
No conclusion for GUE polynomials is borrowed from Han26's Ginibre theorem.

<a id="argument"></a>
## Complete argument

The first step is a deterministic dimension-uniform error bound.
The second converts it to (P) using a degree-controlled tube estimate.
The final step transfers the polynomial floor through linearization and removes the logarithmic cutoff.

<a id="target"></a>

## Deterministic backward error

Fix \(m,d\ge1\) and \(R_1,\ldots,R_d\in M_m(\mathbb C)\).
For Hermitian \(N\)-by-\(N\) matrices \(H_j\), put
\[
 T_N(H):=I_m\otimes I_N+\sum_{j=1}^dR_j\otimes H_j.
\]
Fix an operator-norm cutoff \(M<\infty\).
The estimate to prove is that constants \(C,\alpha,\varepsilon_0>0\), depending only on the fixed coefficients and \(M\), satisfy the following for every \(N\):
if \(\max_j\|H_j\|\le M\) and \(s_{\min}(T_N(H))\le\varepsilon\le\varepsilon_0\), there are Hermitian perturbations \(\Delta H_j\) with
\[
 \det T_N(H+\Delta H)=0,
 \qquad
 \Big(\sum_j\|\Delta H_j\|_{\mathrm{HS}}^2\Big)^{1/2}
 \le C\varepsilon^\alpha.
 \tag{BE}
\]
No irreducibility or one-step covariance condition is imposed.
The exponent must be independent of \(N\); an exponent of order \(1/N\) would not supply the proposed probabilistic consequence.

<a id="compression"></a>
## Fixed-dimensional compression of an approximate kernel

Choose a unit vector \(v=(v_1,\ldots,v_m)\in\mathbb C^m\otimes\mathbb C^N\) with \(\|T_N(H)v\|\le\varepsilon\).
Set
\[
 W:=\operatorname{span}\{v_1,\ldots,v_m\},\quad k:=\dim W\le m,
 \qquad
 W_{\mathrm{out}}:=\sum_{j=1}^d P_{W^\perp}H_jW,
 \quad \ell:=\dim W_{\mathrm{out}}\le dk.
\]
The two spaces are orthogonal, and \(k\ge1\).
Choose isometries \(U:\mathbb C^k\to W\) and \(V:\mathbb C^\ell\to W_{\mathrm{out}}\), omitting \(V\) when \(\ell=0\).
Define
\[
 A_j:=U^*H_jU\in\operatorname{Herm}_k,
 \qquad B_j:=V^*H_jU\in M_{\ell,k}(\mathbb C),
 \qquad \widetilde v_a:=U^*v_a.
\]
By the definition of \(W_{\mathrm{out}}\),
\[
 H_jU=UA_j+VB_j.
 \tag{C1}
\]
Thus all components of \(T_N(H)v\) lie in \(W\oplus W_{\mathrm{out}}\), and their coordinates are
\[
 \widetilde v+\sum_j(R_j\otimes A_j)\widetilde v,
 \qquad
 \sum_j(R_j\otimes B_j)\widetilde v.
 \tag{C2}
\]
The squared sum of the norms of these two expressions equals \(\|T_N(H)v\|^2\), not merely a bound for a compression of that residual.
Also \(\|\widetilde v\|=1\), \(\|A_j\|_{\mathrm{HS}}\le\sqrt{k}M\), and \(\|B_j\|_{\mathrm{HS}}\le\sqrt{k}M\).

For each of the finitely many pairs \(1\le k\le m\), \(0\le\ell\le dk\), use real coordinates for the Hermitian matrices \(A_j\), real and imaginary coordinates for \(B_j\), and real and imaginary coordinates for \(\widetilde v\).
Define the real polynomial map \(F_{k,\ell}\) by the real and imaginary parts of (C2), together with the scalar coordinate \(\|\widetilde v\|^2-1\).
Its degree is at most two.
Its number of real input coordinates is
\[
 p_{k,\ell}=dk^2+2d\ell k+2mk
 \le m^2(2d^2+d+2),
 \tag{C3}
\]
and its number of real output coordinates is \(2m(k+\ell)+1\).
The actual input \(x=(A,B,\widetilde v)\) satisfies
\[
 |F_{k,\ell}(x)|\le\varepsilon,
 \qquad |x|^2\le 2dkM^2+1,
 \tag{C4}
\]
with Hilbert--Schmidt orthonormal coordinates for the Hermitian blocks.
No full-rank constraint is imposed on the matrix with columns \(\widetilde v_a\).
Allowing its rank to drop under repair is intentional; the repaired vector need only remain normalized and supported in the same physical space \(W\).

<a id="error-bound"></a>
## Polynomial error bound and lifting back to the original dimension

The source input is the global real polynomial error bound stated as (KS2) on p. 2 of [Kurdyka--Spodzieja--Szlachcińska, arXiv:1412.5088v1](https://arxiv.org/pdf/1412.5088#page=2).
For a real polynomial map \(F:\mathbb R^p\to\mathbb R^q\) of degree \(D\), that statement gives a constant \(c_F>0\) such that
\[
 |F(x)|\ge c_F
 \left(\frac{\operatorname{dist}(x,F^{-1}(0))}{1+|x|^2}\right)^{D(6D-3)^{p-1}}.
 \tag{KSS}
\]
The paper attributes this input to Kurdyka--Spodzieja and also gives the algebraic-restriction form in Corollary 2.1, p. 5.
The displayed statement was inspected; its original proof was not independently reviewed here.
Empty zero sets are handled below by compactness, without relying on a source convention for their distance.

For a nonempty zero set of \(F_{k,\ell}\), (C4) and (KSS) give a zero \(x'=(A',B',\widetilde v')\) with
\[
 |x'-x|\le C_{k,\ell}\varepsilon^{\alpha_{k,\ell}},
 \qquad
 \alpha_{k,\ell}=\frac1{2\,9^{p_{k,\ell}-1}}.
 \tag{C5}
\]
The zero set is closed, so distance is attained.
If that zero set is empty, continuity on the closed bounded region (C4) gives a strictly positive minimum residual, so sufficiently small residuals of that type cannot occur.
There are only finitely many types, so constants and a common positive exponent can be chosen independently of \(N\).

To lift the repair, retain the original physical isometries \(U,V\) and put
\[
 \Delta H_j:=U(A'_j-A_j)U^*
       +V(B'_j-B_j)U^*
       +U(B'_j-B_j)^*V^*.
 \tag{C6}
\]
These perturbations are Hermitian.
For \(v'_a:=U\widetilde v'_a\), their construction gives
\[
 (H_j+\Delta H_j)U=UA'_j+VB'_j,
 \qquad \|v'\|=1.
\]
Consequently the exact equations \(F_{k,\ell}(x')=0\) imply \(T_N(H+\Delta H)v'=0\).
Only the columns issuing from \(W\) and their adjoint rows have been changed.
The unchanged action on columns outside \(W\) contributes nothing, since \(v'\) is supported in \(W\).
Orthogonality of \(W\) and \(W_{\mathrm{out}}\) gives
\[
 \sum_j\|\Delta H_j\|_{\mathrm{HS}}^2
 =\sum_j\big(\|A'_j-A_j\|_{\mathrm{HS}}^2
               +2\|B'_j-B_j\|_{\mathrm{HS}}^2\big)
 \le2|x'-x|^2.
 \tag{C7}
\]
Equations (C5)--(C7) prove (BE).
The physical subspaces may depend on the witness, but the coordinate maps and their bounds range over only the stated finite list; thus the resulting deterministic event inclusion requires no measurable choice of witnesses.

<a id="tubes"></a>
## Gaussian tubular-neighborhood bound

The geometric source is [Lotz, arXiv:1210.3742v4, Theorem 1.1, p. 1](https://arxiv.org/pdf/1210.3742#page=1), whose v4 header is dated 28 September 2013.
For a real complete intersection of codimension one, defined by a polynomial of degree at most \(D\), its stated bound for a point uniform in a ball of radius \(\sigma\) is
\[
 \mathbb P\{\operatorname{dist}(x,Z)\le\rho\}
 \le4\sum_{r=1}^n\binom nr
       (2D\rho/\sigma)^r(1+\rho/\sigma)^{n-r}.
 \tag{T1}
\]
In particular, the right side is at most
\[
 \frac{8nD\rho}{\sigma}
 \exp\!\left(\frac{n(2D+1)\rho}{\sigma}\right).
 \tag{T2}
\]
This uses the binomial identity and the mean-value bound for the difference of two \(n\)-th powers.
The main agent checked this source statement and the regular-level extension below during development; this is not independent review of the source's proof.

For a standard Gaussian \(g\in\mathbb R^n\), an exact mixture representation is to sample \(S\sim\chi_{n+2}\), then sample \(g\) uniformly in the ball of radius \(S\).
Indeed its radial mixing density is
\[
 w_n(s)=\frac{s^{n+1}e^{-s^2/2}}{2^{n/2}\Gamma(n/2+1)},
\]
and, writing \(\omega_n\) for unit-ball volume,
\[
 \int_{|x|}^{\infty}\frac{w_n(s)}{\omega_ns^n}\,ds
 =(2\pi)^{-n/2}e^{-|x|^2/2}.
 \tag{T3}
\]
Condition on \(S\ge\sqrt n/2\), whose complement has probability at most \(e^{-cn}\) for a universal \(c>0\) and sufficiently large \(n\).
Then (T2) yields
\[
 \mathbb P\{\operatorname{dist}(g,Z)\le\rho\}
 \le C D\sqrt n\,\rho\,
          \exp(C(D+1)\sqrt n\,\rho)+e^{-cn}.
 \tag{T4}
\]
In the regime \((D+1)\sqrt n\,\rho\le1\), this is \(O(D\sqrt n\,\rho)+e^{-cn}\).
The exponential factor must be retained until that small-radius condition is imposed.

For GUE, choose a real Hilbert--Schmidt orthonormal basis of \(\operatorname{Herm}_N\).
The Task normalization makes each basis coordinate an independent real Gaussian of variance \(1/N\).
Thus the tuple is \(H=N^{-1/2}g\) in \(n=dN^2\) real coordinates.
Its singular-input set is
\[
 Z_N:=\{g:q_N(g)=0\},\qquad
 q_N(g):=|\det T_N(N^{-1/2}g)|^2.
\]
Here \(q_N\) is a nonnegative real polynomial of degree at most \(2mN\), and \(q_N(0)=1\).
If its zero set is empty, the tube probability is zero; (BE) then excludes sufficiently small singular values on the norm event.
This includes the case of constant \(q_N\).

For a nonempty zero set, the following regular-level argument extends (T1) to \(q_N^{-1}(0)\), even if it is singular or has real codimension greater than one.
Fix a ball radius \(\sigma\), a tube radius \(\rho\), and an approximation tolerance \(\eta>0\).
The relevant zero points lie in the compact set \(q_N^{-1}(0)\cap\overline B_{\sigma+\rho+1}\).
Every neighborhood of each such zero contains a point where \(q_N>0\), since a nonzero nonnegative polynomial cannot vanish on an open set.
Choose, near each zero, such a positive point and a smaller neighborhood of zeros that is still within distance \(\eta\) of that point.
For every zero in this smaller neighborhood, the segment to the chosen positive point lies within its \(\eta\)-ball.
Continuity on that segment supplies a point of \(q_N^{-1}(\delta)\) for every positive \(\delta\) below the value at the positive endpoint.
A finite cover gives one positive upper bound on \(\delta\) valid for all relevant zeros.
Choose a regular value below that bound, using [Sard's theorem](../audits/literature/Sar42/Yin_U001.md#sar42-u001).
Then every relevant zero lies within \(\eta\) of the smooth hypersurface \(q_N^{-1}(\delta)\), so
\[
 \{x\in B_\sigma:\operatorname{dist}(x,q_N^{-1}(0))\le\rho\}
 \subseteq
 \{x\in B_\sigma:\operatorname{dist}(x,q_N^{-1}(\delta))\le\rho+\eta\}.
\]
Apply (T1) with radius \(\rho+\eta\), and let \(\eta\downarrow0\).
The degree and numerical constants do not depend on the chosen regular level.
This proves the same bound for the original zero set without assuming it smooth.

Using this extension, (BE) gives the inclusion, on the norm event,
\[
 \{s_{\min}(T_N)\le\varepsilon\}
 \subseteq
 \{\operatorname{dist}(g,Z_N)\le C\sqrt N\,\varepsilon^\alpha\}.
 \tag{T5}
\]
Substituting \(D\le2mN\), \(\sqrt n=\sqrt d\,N\), and \(\rho=C\sqrt N\varepsilon^\alpha\) in (T4) gives the estimate
\[
 \mathbb P\{s_{\min}(T_N)\le\varepsilon\}
 \le \mathbb P\{\max_j\|H_j\|>M\}
     +C_R N^{5/2}\varepsilon^\alpha
        \exp(C_RN^{5/2}\varepsilon^\alpha)
     +e^{-c_RN^2},
 \tag{T6}
\]
for small enough \(\varepsilon\).
The constants in (T6) also depend on the fixed cutoff \(M\).
Taking \(M>2\) and \(\varepsilon=N^{-A}\) with \(A\alpha>5/2\) gives a polynomial floor, since the GUE norm event has probability tending to one.
For any fixed \(r>0\), take \(A\alpha>r+5/2\); the tube term is then \(o(N^{-r})\).


<a id="polynomial-application"></a>
## From the pencil bound to the exact scalar-polynomial conclusion

For constant \(P\), both measures are the same point mass, so assume \(P\) nonconstant.
Fix \(z\ne P(0)\).
Use the following elementary word-chain linearization, as in the [general linearization principle in Han26 Section 2.2](https://arxiv.org/html/2606.01664v1#S2.SS2).
For a word \(c_wx_{i_1}\cdots x_{i_k}\) of length \(k\ge2\), set \(Q_w=I_{k-1}-V_w\), with strictly upper diagonal entries \((V_w)_{r,r+1}=x_{i_{r+1}}\).
Take \(B_w=(c_wx_{i_1},0,\ldots,0)\) and \(C_w=(0,\ldots,0,-x_{i_k})^{\mathsf T}\).
Then \(Q_w^{-1}=I+V_w+\cdots+V_w^{k-2}\) and \(-B_wQ_w^{-1}C_w\) is that word.
Concatenate these blocks and place the affine part of \(P-z\) in the root to obtain
\[
 L_P(z;x)=\begin{pmatrix}a_z&B\\C&Q\end{pmatrix},\qquad
 a_z-BQ^{-1}C=P(x)-z.
\]
Its fixed size is \(q:=1+\sum_{|w|\ge2}(|w|-1)\); if \(P\) is affine, use \(q=1\).
All entries are affine in \(x\), and \(Q\) is unit upper triangular with a polynomial inverse.

At zero input the constant part is \(D_z=\operatorname{diag}(P(0)-z,1,\ldots,1)\).
Thus
\[
 \widetilde T_N(z):=(D_z^{-1}\otimes I_N)L_P(z;H^{(N)})
 =I_q\otimes I_N+\sum_j\widetilde R_j(z)\otimes H_j^{(N)}.
\]
For each fixed \(z\ne P(0)\), apply the proved pencil estimate to these fixed coefficients.
The inverse root block is
\[
 (\widetilde T_N(z)^{-1})_{11}
 =(P(0)-z)(P(H^{(N)})-zI)^{-1}.
\]
Hence
\[
 s_{\min}(P(H^{(N)})-zI)\ge |P(0)-z|s_{\min}(\widetilde T_N(z)).
 \tag{L}
\]
Invertibility of both matrices is equivalent by the Schur complement, so the inequality also covers singular matrices.
Absorbing the fixed positive factor into a power of \(N\) gives some \(B_z<\infty\) with
\[
 \mathbb P\{s_{\min}(P(H^{(N)})-zI)<N^{-B_z}\}\longrightarrow0.
 \tag{LSV}
\]
No uniformity in \(z\) is required.
Each finite-\(N\) determinant is a nonzero polynomial in the Gaussian coordinates for \(z\ne P(0)\), as its value at zero input is nonzero.
Thus the singular event has probability zero for each such fixed \(z\).

Put \(A_N:=P(H^{(N)})\) and \(a:=P(s)\).
Let \(\nu_N^z\) be the empirical law of squared singular values of \(A_N-zI\), and let \(\nu^z\) be the spectral distribution of \(Q_z(s)\), where
\[
 Q_z:=(P-z)^*(P-z).
\]
The top homogeneous part of \(Q_z\) is \(P_{\deg P}^*P_{\deg P}\ne0\), so this is a nonconstant self-adjoint scalar polynomial.
CGP22 Corollary 1.3, with coefficient amplification size one, gives
\[
 |\mathbb E G_{Q_z(H^{(N)})}(w)-G_{Q_z(s)}(w)|
 \le C_zN^{-2}\big((\Im w)^{-5}+(\Im w)^{-2}\big),\qquad \Im w>0.
 \tag{R}
\]
The source uses \(G(w)=\int(w-x)^{-1}\,d\nu(x)\); absolute imaginary parts remove its sign.
SS15 gives an atomless limit and a Puiseux expansion of this transform at zero.
The bound \(|G(i\eta)|\le1/\eta\) excludes powers below \(-1\), and absence of a zero atom excludes a pole of order one.
There exist \(0<\beta_z\le1\) and \(C_z<\infty\) with
\[
 t|\Im G_{Q_z(s)}(it)|\le C_z t^{\beta_z}\quad(0<t\le1).
\]
The scalar kernel inequality \(1_{[0,t]}(x)\le2t^2/(x^2+t^2)\) gives
\[
 \mathbb E\nu_N^z([0,t])\le C_z(t^{\beta_z}+N^{-2}t^{-4}).
\]
Fix \(0<\gamma_z<2/(4+\beta_z)\).
For \(N^{-\gamma_z}\le t\le1\),
\[
 \mathbb E\nu_N^z([0,t])\le C_z t^{\beta_z}.
 \tag{W}
\]
These are pointwise-in-\(z\) bounds.

On the good event in (LSV), every squared singular value is at least \(N^{-2B_z}\).
The part of the negative logarithmic tail below \(N^{-\gamma_z}\) is at most
\[
 2B_z(\log N)\,\nu_N^z([0,N^{-\gamma_z}]).
\]
Its expectation bound from (W) tends to zero.
For \(N^{-\gamma_z}<x<\varepsilon<1\), integration by parts and (W) give an expected negative log contribution bounded by
\[
 C_z\varepsilon^{\beta_z}(1+|\log\varepsilon|)
   +C_z(\log N)N^{-\gamma_z\beta_z}.
\]
If \(2B_z<\gamma_z\), the interval below the floor is simply empty; the same displayed bounds remain sufficient.
Markov's inequality and the probability of the exceptional event therefore show
\[
 \lim_{\varepsilon\downarrow0}\limsup_N
 \mathbb P\!\left\{\int_{(0,\varepsilon)}|\log x|\,d\nu_N^z(x)>\delta\right\}=0
 \quad(\delta>0).
 \tag{UI}
\]
The same power behavior gives the corresponding integrability for \(\nu^z\).

Star-moment convergence and a bounded norm event give weak convergence in probability of \(\nu_N^z\) to \(\nu^z\).
For each fixed cutoff, the bounded continuous logarithmic truncation therefore converges in probability.
The upper logarithmic tail is controlled on the same norm event, and (UI) removes the lower cutoff.
It follows that for almost every \(z\),
\[
 u_N(z):=\frac1N\log|\det(A_N-zI)|
   =\frac12\int\log x\,d\nu_N^z(x)
 \longrightarrow
 u(z):=\tau(\log|a-z|)
\]
in probability.

For completeness, this pointwise statement upgrades to local \(L^1\) convergence in probability.
Choose \(M\) with \(\mathbb P(\|A_N\|\le M)\to1\) and \(\|a\|\le M\).
On that event, all eigenvalues of \(A_N\) lie in the radius-\(M\) disk, and
\[
 u_N(z)=N^{-1}\sum_{j=1}^N\log|z-\lambda_j(A_N)|.
\]
For a compact \(K\subset\mathbb C\), the \(L^2(K)\) norms of translated logarithmic kernels are uniformly bounded for translations in that disk.
Jensen's inequality gives \(\|u_N\|_{L^2(K)}\le C_{M,K}\).
The Brown-potential identity gives the same bound for \(u\).
For every fixed \(\delta>0\), dominated convergence in \(z\) gives
\[
 \mathbb E\,\big|\{z\in K:|u_N(z)-u(z)|>\delta\}\big|\longrightarrow0.
\]
On the norm event, Cauchy--Schwarz bounds the \(L^1\) difference by
\(\delta|K|+2C_{M,K}|\{|u_N-u|>\delta\}\cap K|^{1/2}\).
This proves \(u_N\to u\) in \(L^1_{\mathrm{loc}}\) in probability.

For \(\varphi\in C_c^\infty(\mathbb C)\), distributional logarithmic-potential identities now give
\[
 \int\varphi\,d\mu_{A_N}
 =\frac1{2\pi}\int u_N\Delta\varphi\,d^2z
 \longrightarrow
 \frac1{2\pi}\int u\Delta\varphi\,d^2z
 =\int\varphi\,d\mu_a^{\mathrm{Br}}
\]
in probability.
The bounded norm event gives tightness, and smooth approximation on the fixed disk extends convergence to every bounded continuous test function.
This is precisely the original F0012 assertion.

## Current assessment
[Selected decision](#decision-reviewed-proof)

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-04T17:07 |
| status | open |
| reason | A complete candidate argument is retained for whole-chain scrutiny, including the fixed-dimensional real error bound, singular-variety tube passage, Gaussian scaling and the exact F0012 application. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Polynomial invertibility for every fixed monic matrix-coefficient GUE pencil and Brown-measure convergence for every fixed scalar GUE polynomial. |

### Decision reviewed-proof

| Field | Value |
| --- | --- |
| date | 2026-11-04T17:34 |
| status | proved |
| reason | The complete fixed argument establishes the pencil estimate and its full scalar-polynomial consequence. The independent whole-chain finding checks the exact statement, all local interfaces and the F0012 contract, with the stated external-theorem acceptance boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every fixed monic matrix-coefficient GUE pencil, estimate (P), and Brown-measure convergence for every fixed scalar GUE polynomial. |
| argument | [Complete argument](#argument) | Fixed-dimensional compression, real polynomial repair, Gaussian tubes, linearization, logarithmic integrability and planar convergence. |
| review | [Independent whole-chain finding](../audits/reviews/Yin_R_F0190_v1.md#whole-chain-finding) | The exact statement and complete argument, including the accepted external inputs and their application hypotheses; no formal verification or priority claim. |

