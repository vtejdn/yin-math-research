---
author: Yin
---

# Finite-variance Wigner spectral controls, cyclic subclasses and the exact logarithmic defect

This version addresses the broadened [finite-variance Task](../tasks/Yin_T_F0012_v3.md#contract).
It preserves the separate [completed GUE theorem](Yin_C_F0186_v3.md#statement) without asserting its affine fixed-shift logarithmic conclusion for arbitrary entry laws.

<a id="statement"></a>
## Exact partial and conditional conclusions

Assume the fixed-law centered finite-second-moment Wigner model of the Task, including complex or real off-diagonal entries, a separate finite-variance diagonal law, and arbitrary dependence across matrix sizes.
For each fixed scalar noncommutative polynomial \(P\), use the potentials defined in [the model](#model).
The following assertions hold.

1. Every fixed self-adjoint matrix polynomial has almost-sure weak spectral convergence to its free semicircular law, and its expected spectral measures converge weakly.
   This includes every fixed Hermitization \((P-z)^*(P-z)\).
2. Polynomial singular-value measures have the expected power-tail bound (Tail), and all fixed powers of their positive logarithm are uniformly integrable in expectation and have the pathwise tail control (Pos-AS).
   For degree \(D\ge1\), normalized singular \(p\)-moments converge almost surely for \(0<p<1/(5D)\).
3. For every fixed \(\delta>0\), \(u_{N,\delta}\to u_\delta\) locally uniformly in the planar variable almost surely, and at each fixed planar parameter in every finite \(L^p\), \(p\ge1\).
   Some sufficiently slow deterministic \(\delta_N\downarrow0\) gives \(u_{N,\delta_N}\to u\) in local planar \(L^1\) almost surely.
4. The eigenvalue measures of \(P(W^{(N)})\) are almost surely tight, have an eventual pathwise uniform positive logarithmic second moment, and their logarithmic potentials have eventual uniform local planar \(L^2\) bounds.
5. On the probability-one control event, the exact almost-sure weak Brown-measure conclusion for \(P\) is equivalent to [the planar defect condition (Defect)](#remaining-defect).
   The defect condition is not established for arbitrary \(P\).
6. The full almost-sure weak Brown-measure conclusion does hold for every \(P=g(A C^*C)\), where \(A=A^*\) and \(C\) are fixed scalar noncommutative polynomials and \(g\) is any one-variable complex polynomial.
   This includes genuinely nonnormal examples such as \(xy^2\).

The almost-sure assertions use one event for each fixed model and polynomial, intersecting the stated countable parameter or test families where necessary.
No independence between sizes, moment above two, density, or almost-sure operator-norm bound is used.
No assertion about convergence of all untruncated trace moments, or expectation convergence of an unregularized logarithmic determinant, is included.
The general nonnormal Task remains open.

## Inputs and provenance

The argument is a project deduction with explicit external concentration inputs and bounded FK multiplicativity.
The selected source editions and reading limits are [Gui12](../audits/literature/Gui12/readme.md), [War16](../audits/literature/War16/readme.md), and the [bounded finite-tracial FK input](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
The Brown logarithmic-potential convention is the one used in [the prior polynomial application](Yin_C_F0186_v1.md#polynomial-application).
This is not a novelty or priority claim.

<a id="argument"></a>
## Proof of the stated controls and reductions

## Source scope

For the bounded-entry colored moment input and its attribution, Alice Guionnet's *Lecture Notes, Minneapolis*, dated 2 July 2012, [Section 2.3, Theorem 4, PDF pp. 13--14](https://perso.ens-lyon.fr/aguionne/minneapolis.pdf#page=13), was inspected in the author-hosted original.
It treats real or complex independent Wigner matrices with uniformly bounded moments of every order; it does not require independence of real and imaginary parts of an entry.
The local moment proof below also makes explicit why a different bounded diagonal variance causes no change.
That theorem is applied only after a fixed entry truncation, not directly to finite-variance entries.

The bounded-differences inequality was inspected in Lutz Warnke, *On the method of typical bounded differences*, [arXiv:1212.5796v1, Theorem 1, PDF p. 2](https://arxiv.org/pdf/1212.5796v1#page=2).
The ordinary inequality stated there applies to independent blocks, with tail \(\exp(-2t^2/\sum c_k^2)\); apply it to the negative function for the lower tail.
The original McDiarmid proof is an accepted external input, not re-audited here.
No typical-good-set version of that inequality is used.

Finite-dimensional spectral min-max, singular-value decomposition, Cauchy--Binet, Schur triangularization, Tonelli/Fubini and first Borel--Cantelli are the elementary inputs used at their explicit interfaces.
The rank and singular-value estimates needed below are proved here.
No unproved transfer of nonnormal eigenvalues through a low-rank perturbation is used.

<a id="model"></a>
## Model and notation

Use the fixed entry laws and coupling quantifiers of the Task.
Write \(\operatorname{tr}_N=N^{-1}\operatorname{Tr}_N\).
For a fixed self-adjoint \(m\)-by-\(m\) matrix polynomial \(Q\), let \(\nu_{N,Q}\) be the empirical spectral probability measure of \(Q(W^{(N)})\), with normalization \(1/(mN)\), and let \(\nu_Q\) be the law of \(Q(s)\) under \(\operatorname{tr}_m\otimes\tau\).
The polynomial and coefficient size remain fixed.

For a fixed scalar polynomial \(P\) of degree \(D\ge1\), put \(A_N=P(W^{(N)})\), \(a=P(s)\), and
\[
 Q_z(x)=(P(x)-z)^*(P(x)-z),\qquad
 u_N(z)=\frac1N\log|\det(A_N-zI_N)|,
\]
\[
 u_{N,\delta}(z)=\frac1{2N}\log\det(Q_z(W^{(N)})+\delta^2I_N),\qquad
 u_\delta(z)=\frac12\tau\log(Q_z(s)+\delta^2),\qquad
 u(z)=\tau\log|a-z|.
\]
The unregularized potentials are locally integrable functions of the planar variable, with value \(-\infty\) at a finite eigenvalue allowed.
Constant \(P\) is immediate for the spectral assertions and can be separated throughout.

<a id="rank-stability"></a>
## Rank stability for self-adjoint polynomial spectra

If \(X,Y\) are tuples of \(N\)-by-\(N\) matrices, telescope each word in a fixed matrix polynomial.
Rank subadditivity and \(\operatorname{rank}(BCD)\le\operatorname{rank}C\) imply
\[
 \frac{\operatorname{rank}(Q(X)-Q(Y))}{mN}
 \le C_Q\sum_j\frac{\operatorname{rank}(X_j-Y_j)}N.
 \tag{R1}
\]
The constant depends only on the finite list of words, not on matrix norms or entries.
Tensoring a rank-\(r\) physical perturbation with a fixed \(m\)-by-\(m\) coefficient contributes rank at most \(mr\).

For Hermitian \(B,C\) of size \(n\), the min-max principle gives
\[
 \sup_x|F_B(x)-F_C(x)|\le\frac{\operatorname{rank}(B-C)}n.
 \tag{R2}
\]
Indeed, restriction to the kernel of \(B-C\), of codimension at most that rank, gives both eigenvalue-counting inequalities.
For a real test function \(f\) of finite total variation,
\[
 \left|\frac1n\operatorname{Tr}f(B)-\frac1n\operatorname{Tr}f(C)\right|
 \le\frac{\operatorname{rank}(B-C)}n\,\operatorname{Var}(f).
 \tag{R3}
\]
This follows by Stieltjes integration by parts; the difference of the two distribution functions vanishes at both infinities.
For a complex resolvent test \(f_z(x)=(z-x)^{-1}\), the same integration gives a constant bounded by \(\pi/|\Im z|\).
A norm perturbation of size \(\eta\) instead changes the normalized resolvent by at most \(\eta/|\Im z|^2\).

These statements are used only for Hermitian polynomial outputs or Hermitized outputs.
There is no corresponding assertion here for the eigenvalue measures of arbitrary nonnormal \(P(X)\).

<a id="bounded-moments"></a>
## Bounded-entry colored moments

For a fixed cutoff \(R\), center the truncated entry variables:
\[
 \xi_{j,R}=\xi_j1_{\{|\xi_j|\le R\}}-\mathbb E[\xi_j1_{\{|\xi_j|\le R\}}],
 \qquad
 \zeta_{j,R}=\zeta_j1_{\{|\zeta_j|\le R\}}-\mathbb E[\zeta_j1_{\{|\zeta_j|\le R\}}].
\]
Let \(W_{j,R}^{(N)}\) be the correspondingly coupled Wigner matrices, and put
\(\sigma_{j,R}^2=\mathbb E|\xi_{j,R}|^2\).
Then \(\sigma_{j,R}\to1\), and every truncated raw entry is bounded by \(2R\).

For completeness, the expected normalized trace of a word of length \(k\) is an index sum with factor \(N^{-1-k/2}\).
A fixed equality pattern determines a connected graph of vertices and colored unoriented edges.
Centering and independence force each colored edge variable to occur at least twice.
Thus its number \(e\) of colored edges is at most \(k/2\), and its number \(v\) of vertices is at most \(e+1\).
Bounded entry moments make every pattern with \(v-1-k/2<0\) negligible.
Equality requires a tree with no loops and with every edge appearing exactly twice.
The closed tree walk traverses every edge once in each direction, giving variance \(\sigma_{j,R}^2\) for its color, regardless of dependence between the real and imaginary parts.
Diagonal loops cannot occur in a leading tree.
The surviving patterns are exactly the color-respecting noncrossing pairings.
Consequently, the joint expected word moments converge to those of
\((\sigma_{1,R}s_1,\ldots,\sigma_{d,R}s_d)\).

The argument extends to matrix coefficients by expanding the coefficient products and taking the normalized matrix trace.
For every self-adjoint \(Q\), all moments of the deterministic expected measure \(\mathbb E\nu_{N,Q(W_R)}\) therefore converge to the moments of the compactly supported law of \(Q(\sigma_Rs)\).
Even-moment bounds give tightness and uniform integrability of each smaller moment.
Moment determinacy of a compactly supported law yields weak convergence of these expected measures.
This is the bounded-entry moment theorem at precisely the use needed below.

<a id="finite-variance-weak"></a>
## Finite-variance expected weak limits

The coupling of the original and centered truncated variables satisfies
\[
 e_R:=\sum_j\sup_N\mathbb E\operatorname{tr}_N
       \bigl(W_j^{(N)}-W_{j,R}^{(N)}\bigr)^2\longrightarrow0.
 \tag{T1}
\]
For an off-diagonal entry, the difference variance is bounded by
\(\mathbb E|\xi_j|^2 1_{\{|\xi_j|>R\}}\); the analogous diagonal bound has the additional factor \(1/N\) in the normalized Hilbert--Schmidt sum.
Finite second moments prove (T1).

Fix \(0<\eta\le1\).
For the Hermitian difference \(D_j=W_j-W_{j,R}\), spectral truncation gives
\[
 D_j=B_j+E_j,\qquad
 \|E_j\|\le\eta,\qquad
 \frac{\operatorname{rank}B_j}N
 \le \eta^{-2}\operatorname{tr}_N D_j^2.
 \tag{T2}
\]
Fix \(M>2\) and let \(V_{j,R}\) be \(W_{j,R}\) with eigenvalues clipped to \([-M,M]\).
Since \(\sigma_{j,R}\le1\), the bounded-entry one-matrix weak limit gives
\[
 \mathbb E\frac{\operatorname{rank}(W_{j,R}-V_{j,R})}N\longrightarrow0
 \quad(N\to\infty)
 \tag{T3}
\]
for each fixed \(R\), by the closed-set Portmanteau bound outside \([-M,M]\).

Compare the following polynomial inputs in order:
\[
 W,\qquad W_R+E,\qquad V_R+E,\qquad V_R,\qquad W_R.
\]
The first, second and fourth transitions are controlled by (R1)--(R3) and the ranks in (T2)--(T3).
The middle transition has uniformly bounded inputs, and word telescoping gives
\[
 \|Q(V_R+E)-Q(V_R)\|\le C_{Q,M}\eta.
\]
For every fixed spectral parameter \(w\notin\mathbb R\), the normalized resolvents consequently satisfy
\[
 \limsup_N\mathbb E
  |G_{Q(W)}(w)-G_{Q(W_R)}(w)|
 \le C_{Q,M,w}(e_R/\eta^2+\eta).
 \tag{T4}
\]
No norm bound on the original untruncated Wigner matrices is assumed.

First let \(R\to\infty\), then \(\eta\downarrow0\).
Since \(Q(\sigma_Rs)\to Q(s)\) in operator norm, the bounded-entry result and (T4) yield
\[
 \mathbb E\nu_{N,Q}\Longrightarrow\nu_Q.
 \tag{Weak-mean}
\]
The standard Stieltjes continuity theorem applies because the limiting transform is that of a probability measure.
This statement concerns weak spectral measures, not convergence of all untruncated entry or trace moments.

<a id="row-concentration"></a>
## Row-block concentration and almost-sure weak limits

Partition the independent input variables, for each \(j\), into upper-triangular row blocks:
block \(k\) contains the diagonal variable at \(k\) and all upper entries \((k,\ell)\), \(\ell>k\).
There are \(dN\) independent blocks.
Changing one block changes one Hermitian input by rank at most two.
By (R1)--(R3), for
\[
 \Phi_{N,f}=\int f\,d\nu_{N,Q},
\]
the bounded-differences constant for each block is at most \(C_Q\operatorname{Var}(f)/N\).
Hence, for a constant \(c_Q>0\),
\[
 \mathbb P\{|\Phi_{N,f}-\mathbb E\Phi_{N,f}|>t\}
 \le2\exp\left[-\frac{c_QNt^2}{\operatorname{Var}(f)^2}\right].
 \tag{BD}
\]
For a constant polynomial the statistic is deterministic.
No entry moment or density assumption is used by (BD) itself.

Apply (BD) to a countable convergence-determining family of real and imaginary resolvent tests.
Their expectations converge by (Weak-mean), and their fixed-deviation probabilities are summable in \(N\).
First Borel--Cantelli therefore gives
\[
 \nu_{N,Q}\Longrightarrow\nu_Q
 \quad\text{almost surely}
 \tag{Weak-AS}
\]
under every coupling across sizes allowed by the Task.
In particular this applies to \(Q_z=(P-z)^*(P-z)\) for each fixed \(z\), and to every fixed self-adjoint matrix polynomial.
The event may depend on that polynomial and parameter, as stipulated.

<a id="positive-tail"></a>
## Polynomial singular-value tails from only second moments

If a matrix \(B\) has at most \(r\) singular values above \(t\), there is a subspace of codimension at most \(r\) on which its operator norm is at most \(t\).
For a product \(B_1\cdots B_k\), intersect the successive inverse images of these subspaces under the right partial products.
The intersection has codimension at most \(\sum_\ell r_\ell\), because a linear inverse image cannot increase codimension.
On it the product norm is at most \(\prod_\ell t_\ell\).
Similarly, intersecting subspaces for summands shows that a sum has at most \(\sum_\ell r_\ell\) singular values above \(\sum_\ell t_\ell\).

Apply these two facts to the finite words of a fixed matrix polynomial \(P\) of degree \(D\ge1\), absorbing its fixed coefficient norms.
For large \(R\), its normalized singular-value counting function is bounded by a fixed sum of the input counting functions at a threshold \(c_PR^{1/D}\).
Since
\[
 \sup_N\mathbb E\operatorname{tr}_N(W_j^2)
 \le \max(1,\mathbb E\zeta_j^2),
\]
Markov's inequality for the input singular values gives
\[
 \sup_N\mathbb E\left[
  \frac1{mN}\#\{i:s_i(P(W^{(N)}))>R\}\right]
 \le C_PR^{-2/D}.
 \tag{Tail}
\]
The same bound holds for raw entry truncations that only reduce entry moduli, without centering.
It also holds uniformly for \(P-z\) when \(z\) ranges over a fixed compact set.

Tail integration implies uniformly bounded expected singular moments of every order \(0<p<2/D\), and uniform integrability of every fixed power of the positive logarithm.
In particular,
\[
 \lim_{R\to\infty}\sup_N
 \mathbb E\int_{(R,\infty)}\log s\,d\mu_{|P(W)|}(s)=0.
 \tag{Pos-EUI}
\]
No moment of the entries above two is hidden in this deduction.

<a id="log-statistics"></a>
## Almost-sure logarithmic-growth statistics

Clip every raw input variable at modulus \(N^2\), without centering, to obtain \(\widehat W^{(N)}\).
By the finite second moments and a union bound,
\[
 \mathbb P\{\widehat W^{(N)}\ne W^{(N)}\}\le C N^{-2}.
 \tag{Entry-cut}
\]
Thus the two tuples are equal for all sufficiently large \(N\), almost surely, under every allowed cross-size coupling.
The clipped entries still form independent row blocks.
Deterministically,
\[
 \|\widehat W_j^{(N)}\|\le N^{5/2},\qquad
 \|P(\widehat W^{(N)})\|\le C_PN^{5D/2}.
 \tag{Poly-norm}
\]

Let \(Q=P^*P\), and let \(h:[0,\infty)\to\mathbb R\) be continuous and nondecreasing, with
\[
 |h(x)|\le C_h(1+\log^r(2+x))
\]
for some fixed finite \(r\ge1\).
On the deterministic spectral interval from (Poly-norm), its total variation is \(O_h(1+\log^rN)\).
Extend it constantly above that interval and below zero, and apply (BD) to the clipped tuple.
For every fixed \(t>0\),
\[
 \mathbb P\left\{\left|
 \int h\,d\nu_{N,Q(\widehat W)}
 -\mathbb E\int h\,d\nu_{N,Q(\widehat W)}
 \right|>t\right\}
 \le2\exp[-c_{P,h}Nt^2/(1+\log^{2r}N)].
 \tag{Log-conc}
\]
These probabilities are summable.

The expected clipped spectral measures have the same weak limit as the original ones, because their probability of disagreement tends to zero.
The power tail (Tail), also valid for the clipped input, makes the logarithmic-growth integrals uniformly integrable.
Consequently their expectations converge to the corresponding free integral.
Combining (Entry-cut), (Log-conc) and first Borel--Cantelli proves
\[
 \int h\,d\nu_{N,Q}\longrightarrow\int h\,d\nu_Q
 \quad\text{almost surely}.
 \tag{Log-AS}
\]

For positive logarithmic tail control, apply this to
\(h_R(x)=(\log x-\log\sqrt R)_+\), with its continuous value zero at \(x=0\).
For \(x>R>1\), \(\log x\le2h_R(x)\).
The free squared-singular-value law has compact support, so for every sufficiently large fixed \(R\), (Log-AS) gives
\[
 \int_{(R,\infty)}\log x\,d\nu_{N,Q}(x)\longrightarrow0
 \quad\text{almost surely}.
 \tag{Pos-AS}
\]
The same argument with \(h_R^r\) controls fixed powers of the positive logarithmic tail.

<a id="regularized-potentials"></a>
## Almost-sure regularized potentials

For fixed \(\delta>0\), the function \(h_\delta(x)=\tfrac12\log(x+\delta^2)\) satisfies the hypotheses above.
Thus, for every fixed \(z\),
\[
 u_{N,\delta}(z)\longrightarrow u_\delta(z)
 \quad\text{almost surely and in expectation}.
 \tag{Reg}
\]
Expectation convergence follows directly from weak spectral convergence, the fixed lower bound and (Pos-EUI).
For each fixed \(z,\delta\), Jensen and (Tail) give uniformly bounded moments of every fixed order of \(u_{N,\delta}(z)\).
The almost-sure convergence therefore also holds in every fixed finite \(L^p\), by using a uniformly bounded moment of some order greater than \(p\).

The [retained singular-value Frobenius perturbation proof](../claims/Yin_C_F0186_v3.md#singular-value-perturbation) and
\(\operatorname{Lip}[\tfrac12\log(s^2+\delta^2)]=1/(2\delta)\) show that
\[
 |u_{N,\delta}(z)-u_{N,\delta}(w)|
 \le |z-w|/(2\delta).
\]
The same bound holds for the expectations and their free limit.
Apply (Reg) on a countable dense planar set and use this common equicontinuity.
For every fixed \(\delta>0\), convergence is locally uniform in \(z\), almost surely.
One may intersect these events over a countable sequence \(\delta_k\downarrow0\).

The same row argument works for deterministic moving regularizers
\(N^{-a}\le\delta_N\le1\), with any fixed \(a>0\): the clipped logarithm has total variation \(O(\log N)\).
On a fixed compact planar set, a mesh of size proportional to \(N^{-a}\) has polynomially many points.
The union bound in (Log-conc), followed by the \(O(N^a)\) Lipschitz bound in \(z\), proves almost-sure locally uniform concentration around the clipped expectation.

There exists a sufficiently slowly decreasing deterministic choice of such \(\delta_N\) for which
\[
 u_{N,\delta_N}\longrightarrow u
 \quad\text{in }L^1_{\rm loc}(\mathbb C)\text{ almost surely}.
 \tag{Slow-reg}
\]
To construct it, take \(\delta_k=1/k\).
For each \(k\), fixed-regularizer convergence of the clipped expectations is uniform on the radius-\(k\) disk.
Choose increasing \(N_k\ge k^{1/a}\) so its error is at most \(1/k\) for all \(N\ge N_k\), and set \(\delta_N=1/k\) for \(N_k\le N<N_{k+1}\).
Then \(\delta_N\ge N^{-a}\).
The concentration just proved removes fluctuations, while \(u_{\delta_k}\downarrow u\) in local \(L^1\).
For this last step, \(u\) is the Brown logarithmic potential, hence locally integrable, and \(u_{\delta_1}-u\) is an integrable upper bound for the decreasing nonnegative difference.
This diagonal construction gives no polynomial mesoscopic rate and no control of the difference \(u_{N,\delta_N}-u_N\).

<a id="noncompact-planar"></a>
## Tightness and planar potential control without operator-norm boundedness

For any square matrix \(A\) with eigenvalues \(\lambda_i\) and singular values \(s_i\), Schur triangularization and Cauchy--Binet give, for \(t>0\),
\[
 \prod_i(1+|\lambda_i|^2/t)
 \le\det(I+A^*A/t)=\prod_i(1+s_i^2/t).
 \tag{CB}
\]
Indeed, after Schur triangularization, the determinant on the middle is the sum over all squared minors with their powers of \(t^{-1}\).
Its principal-minor terms alone sum to the left side.

Define the nonnegative increasing function
\[
 F(x)=\int_1^\infty\log(1+x^2/t)\,\frac{dt}{t}.
\]
For \(x\ge1\), integration on \(1\le t\le x^2\) gives
\(F(x)\ge2(\log x)^2\).
Splitting the integral at \(x^2\) also gives
\(F(x)\le C(1+\log^2(1+x))\); for \(0\le x\le1\), \(F(x)\le x^2\).
Taking logarithms in (CB), integrating and using Tonelli yields
\[
 \frac1N\sum_i F(|\lambda_i(A_N)|)
 \le\frac1N\sum_i F(s_i(A_N)).
 \tag{Eig-log}
\]
The right side converges almost surely to a finite value by (Log-AS), applied to \(h(x)=F(\sqrt x)\).
Thus almost surely
\[
 \sup_{N\ \mathrm{large}}\frac1N\sum_i(\log^+|\lambda_i(A_N)|)^2<\infty.
 \tag{Log2}
\]
This proves pathwise tightness of the empirical eigenvalue measures, since their mass outside radius \(R>1\) is at most the bound in (Log2) divided by \((\log R)^2\).

For every compact planar set \(K\), a direct radial integration gives
\[
 \int_K|\log|z-\lambda||^2\,d^2z
 \le C_K\bigl(1+(\log^+|\lambda|)^2\bigr).
\]
For bounded \(\lambda\), the singularity is integrable because
\(\int_0^1 r|\log r|^2dr<\infty\); for large \(\lambda\), its distance from \(K\) is comparable with \(|\lambda|\).
The finite eigenvalue potential identity and Jensen, together with (Log2), imply
\[
 \sup_{N\ \mathrm{large}}\|u_N\|_{L^2(K)}<\infty
 \quad\text{almost surely}.
 \tag{Planar-L2}
\]
The free Brown potential has the corresponding local \(L^2\) bound because its Brown measure is compactly supported.
The same estimates and (Tail) also give \(\sup_N\mathbb E\|u_N\|_{L^2(K)}^2<\infty\).
This is a bound on averaged eigenvalue potentials, not uniform integrability of individual small singular-value logarithms.

<a id="small-power-tightness"></a>
## An alternative small-power bound

There is also a direct power-moment version of the preceding tightness argument.
Fix \(0<p<1/(5D)\).
For the clipped tuple from (Entry-cut), the test \(h(x)=x^{p/2}\) on the spectrum of \(P(\widehat W)^*P(\widehat W)\) has total variation at most \(C_PN^{5Dp/2}\).
Thus the same rank bounded-differences argument gives
\[
 \mathbb P\left\{\left|
 \frac1N\operatorname{Tr}|P(\widehat W)|^p
 -\mathbb E\frac1N\operatorname{Tr}|P(\widehat W)|^p
 \right|>t\right\}
 \le2\exp[-c_{P,p}t^2N^{1-5Dp}].
 \tag{Small-p-conc}
\]
The exponent is positive, so the probabilities are summable.
Choose a fixed \(q\) with \(p<q<2/D\).
The expected singular \(q\)-moments are uniformly bounded by (Tail), making the \(p\)-moment integrals uniformly integrable.
Weak spectral convergence and (Entry-cut) then imply
\[
 \frac1N\operatorname{Tr}|P(W^{(N)})|^p
 \longrightarrow \tau(|P(s)|^p)
 \quad\text{almost surely}.
 \tag{Small-p-AS}
\]
This is a small positive moment assertion, not convergence of all polynomial trace moments under finite second moments.
No optimality of the displayed exponent range is claimed.

For \(0<p<2\), integrate the logarithm of (CB) against \(t^{p/2-1}dt\) on \((0,\infty)\).
The scalar identity
\[
 \int_0^\infty\log(1+x^2/t)t^{p/2-1}dt
 =c_p x^p,\qquad
 c_p=\int_0^\infty\log(1+1/u)u^{p/2-1}du\in(0,\infty),
\]
follows by substitution; the restrictions \(p>0\) and \(p<2\) give integrability at zero and infinity.
Tonelli therefore yields
\[
 \frac1N\sum_i|\lambda_i(A_N)|^p
 \le\frac1N\sum_i s_i(A_N)^p.
\]
For the small \(p\) above, (Small-p-AS) supplies an eventual almost-sure uniform bound on the left.
It implies power tightness of the eigenvalue measures and again yields (Planar-L2), since \((\log^+x)^2\le C_p(1+x^p)\).
This alternative uses no additional majorization theorem beyond the locally proved Cauchy--Binet inequality.

<a id="remaining-defect"></a>
## Exact remaining negative-tail interface

The preceding results do not establish the Task.
A sufficient remaining statement is the almost-sure planar defect condition
\[
 \lim_{\delta\downarrow0}\limsup_{N\to\infty}
 \int_K\bigl(u_{N,\delta}(z)-u_N(z)\bigr)\,d^2z=0
 \tag{Defect}
\]
for every compact disk \(K\), where the difference is nonnegative and the unregularized logarithm is locally integrable.
It suffices to use integer-radius disks and \(\delta_k=1/k\), since the defects are nonnegative and decrease as the regularizer decreases.
If (Defect) holds, the locally uniform fixed-regularizer convergence (Reg) and
\(u_\delta\downarrow u\) in local \(L^1\) imply \(u_N\to u\) in local \(L^1\) almost surely.
The distributional Laplacian identity then gives convergence against compactly supported smooth tests, and the pathwise tightness above extends this to the exact weak convergence of probability measures required by the Task.

Conversely, on the probability-one event where the controls above hold, weak eigenvalue-measure convergence to the Brown measure implies (Defect).
Here is the required deterministic continuity argument; no pointwise convergence of untruncated logarithmic potentials is asserted from weak convergence alone.
Fix a compact disk \(K\), and let \(\chi_R\) be a continuous cutoff in the eigenvalue variable, equal to one on the radius-\(R\) disk, zero outside radius \(2R\), and taking values in \([0,1]\).
For fixed \(R,M\), the kernel
\[
 k_{R,M}(z,\lambda)
 =\chi_R(\lambda)\max(\log|z-\lambda|,-M)
\]
is bounded and continuous in \(\lambda\), uniformly bounded for \(z\in K\).
Weak convergence therefore gives convergence of its integrals for each \(z\), and dominated convergence in \(z\) gives convergence in \(L^1(K)\).

The far-eigenvalue error is uniformly small by (Log2).
For \(R\) sufficiently large compared with \(K\),
\[
 \int_{|\lambda|>R}\int_K |\log|z-\lambda||\,d^2z\,d\mu_N(\lambda)
 \le C_K\int_{|\lambda|>R}(1+\log|\lambda|)\,d\mu_N(\lambda)
 \le \frac{C_{K,\omega}}{\log R}
\]
for all sufficiently large \(N\), on the fixed path under consideration.
The limiting Brown measure has compact support, so its far error vanishes for large \(R\).
The lower-kernel truncation has the uniform bound
\[
 \int_K\bigl(\max(\log|z-\lambda|,-M)-\log|z-\lambda|\bigr)\,d^2z
 \le 2\pi\int_0^{e^{-M}}r\log(e^{-M}/r)\,dr
 =\frac\pi2e^{-2M}.
\]
This bound survives integration against any probability measure in \(\lambda\).
Letting \(N\to\infty\), then \(R,M\to\infty\), proves \(u_N\to u\) in \(L^1(K)\) on that path.
For each fixed \(\delta_k\), (Reg) now gives
\[
 \int_K(u_{N,\delta_k}-u_N)\,d^2z
 \longrightarrow\int_K(u_{\delta_k}-u)\,d^2z.
\]
The right side decreases to zero with \(k\), proving (Defect).
Thus, after intersecting the already available events for integer disks and the countable regularizers, the exact weak Brown-measure conclusion is equivalent to (Defect).
This equivalence identifies the unproved assertion rather than establishing it.

An alternative sufficient hypothesis is almost-sure uniform integrability at zero of the logarithm of the squared singular values of \(P(W)-z\), for Lebesgue-almost every fixed \(z\).
For Lebesgue-almost every fixed \(z\), exact singularity already has probability zero at every finite \(N\): integrate its indicator over \(z\), use that each realized matrix has finitely many eigenvalues, and apply Tonelli followed by a countable union over \(N\).
Thus the usual integral over \((0,\varepsilon)\) is legitimate after discarding this deterministic null set of parameters; it does not silently omit a positive-probability zero singular value.
Then (Weak-AS) and (Pos-AS) give pointwise potential convergence almost surely.
Fubini on countably many disks gives one event of planar almost-everywhere convergence.
The bound (Planar-L2) upgrades this to local \(L^1\) on that event, with the same Brown-measure conclusion.

Neither a low-rank truncation of a nonnormal output nor the existence of some slowly decreasing regularizer proves (Defect).
Choosing an extremely small regularizer separately at each finite \(N\) to approximate \(u_N\) does not ensure that its expected regularized limit remains the free one.
The [nilpotent-shift tests](../ledger/Yin_L_F0058_v1.md#failed-shortcuts) already show why weak Hermitized limits and bounded norms alone cannot remove this logarithmic defect.
They are obstructions to the shortcut, not counterexamples within the present Wigner contract.

<a id="cyclic-selfadjoint-reduction"></a>
## An exact nonselfadjoint subclass reduces to the selfadjoint problem

Let \(A=A^*\) be a scalar noncommutative polynomial and let \(C\) be any scalar noncommutative polynomial.
Set
\[
 P=A C^*C,\qquad Q=CAC^*.
 \tag{C1}
\]
The polynomial \(Q\) is selfadjoint, whereas \(P\) need not be normal.
For every finite tuple of Hermitian matrices, put \(U=A(W)C(W)^*\) and \(V=C(W)\).
Then \(P(W)=UV\), \(Q(W)=VU\), and the determinant identity
\[
 \det(zI-UV)=\det(zI-VU)
 \tag{C2}
\]
holds for every \(z\in\mathbb C\), including multiplicities.
For \(z\ne0\), (C2) follows by taking the two Schur complements of \(\begin{pmatrix}zI&U\\V&I\end{pmatrix}\); polynomial continuity gives \(z=0\).
Thus the eigenvalue measures of \(P(W)\) and \(Q(W)\) agree exactly for every \(N\), with no inversion or least-singular-value assumption on \(C(W)\).

The free counterpart follows from the same block matrix and bounded FK multiplicativity.
For bounded \(u,v\) in a finite tracial algebra and \(z\ne0\),
\[
 \Delta_{\operatorname{tr}_2\otimes\tau}
 \left(\begin{pmatrix}z&u\\v&1\end{pmatrix}\right)^{2}
 =\Delta_\tau(z-uv)
 =|z|\,\Delta_\tau(1-vu/z)
 =\Delta_\tau(z-vu).
 \tag{C3}
\]
The triangular factors used in the two Schur decompositions have determinant one.
For completeness, an elementary upper unitriangular factor \(E(a)\) is similar through \(\operatorname{diag}(t,1)\) to \(E(ta)\), and its determinant is unchanged by this invertible similarity.
As \(t\downarrow0\), norm continuity of the determinant on invertible elements gives \(\Delta(E(a))=1\); the lower-triangular case is identical.
Block-diagonal normalization gives the square and the factor \( |z| \) in (C3).
The potentials in (C3) agree off one point and hence have identical distributional Laplacians, so the Brown measures of \(uv\) and \(vu\) coincide.
In (C1), this common Brown measure is the spectral measure of the selfadjoint \(Q(s)\).

Consequently (Weak-AS) proves the Task's conclusion for (C1), under the exact finite-variance model and arbitrary cross-size couplings.
For example \(P(x,y)=xy^2\) reduces to \(Q(x,y)=yxy\).
This transfer does not require almost-sure operator-norm bounds or moments of order \(2+\varepsilon\).
The selfadjoint input is supplied by the finite-variance proof above, at exactly the same model and cross-size coupling quantifiers.

The same reduction extends to \(g(P)\) for any one-variable complex polynomial \(g\).
At finite size its eigenvalue measure is \(g_*\mu_{P(W)}\), by the ordinary spectral mapping identity with algebraic multiplicity.
For a nonconstant \(g\), write \(g(t)-z=b\prod_{j=1}^r(t-\lambda_j)\), with roots counted with multiplicity.
For any bounded element \(a\), FK multiplicativity and the Brown logarithmic potential formula give
\[
 \log\Delta(g(a)-z)
 =\log|b|+\sum_{j=1}^r\int\log|w-\lambda_j|\,d\mu_a^{\mathrm{Br}}(w)
 =\int\log|g(w)-z|\,d\mu_a^{\mathrm{Br}}(w).
\]
The equality is valid in the extended real sense, since the positive parts are bounded on the compact Brown support.
Taking distributional Laplacians proves \(\mu_{g(a)}^{\mathrm{Br}}=g_*\mu_a^{\mathrm{Br}}\); constant \(g\) gives the same identity directly.
Weak convergence is preserved under this continuous pushforward, because a bounded continuous test function composed with \(g\) is still bounded and continuous.

## Retention and scope

The proof retains the finite-variance spectral and potential arguments developed for the reactivated Task, together with the exact cyclic reduction.
Their common core is polynomial spectral convergence; an additional Claim identity is unnecessary for these variants.
The intermediate singular-value method is separately reusable and has its own [Claim](Yin_C_F0187_v1.md#statement).
No Gaussian small-ball estimate is transferred to arbitrary product measures here.

## Current assessment
[Selected decision](#decision-finite-variance-reviewed)

## Assessment history

### Decision finite-variance-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:39 |
| status | open |
| reason | The complete partial theorem and exact defect equivalence are retained for independent mathematical review; the general nonnormal defect is explicitly outside the asserted unconditional conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Partial theorem and equivalence](#statement) | Finite-variance spectral controls, regularized potentials, exact remaining defect, and the cyclic nonnormal subclass. |

### Decision finite-variance-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:46 |
| status | proved |
| reason | Independent whole-proof inspection found no gap in the six stated assertions under their accepted external inputs. The general nonnormal planar defect is explicitly not asserted and the Task remains active. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All six exact partial and conditional conclusions, including the unconditional cyclic nonnormal subclass. |
| argument | [Complete argument](#argument) | The complete finite-variance spectral, logarithmic, planar and cyclic argument. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0190_v4.md#finite-variance-controls) | Exact statement and complete argument, with explicit source and scope limits. |

