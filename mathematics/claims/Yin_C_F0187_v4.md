---
author: Yin
---

# Weak physical delocalization and residual inverse row energy for a bounded two-channel pencil

This theorem develops the physical-block control branch of [F0013](../tasks/Yin_T_F0013_v1.md#contract), with [independent whole-proof coverage](../audits/reviews/Yin_R_F0191_v4.md#bounded-two-channel-physical-spread) selected below.
The [positive-frame intermediate theorem](Yin_C_F0187_v3.md#statement) remains fixed at v3 and is not replaced by the present different statement.
The coefficients here have zero one-step frame constant, but the original independent coordinates and positive mass in both auxiliary spectral channels give a weaker physical delocalization result.
Indeed, both noise coefficients have zero matrix element between the two different coordinate directions of the auxiliary space.
The conclusion concerns a fixed bounded real input model and does not resolve the arbitrary finite-second-moment contract.
This is a project deduction without a novelty claim.

<a id="statement"></a>
## Model, uniform minor scope and exact conclusions

Put
\[
 J_\circ=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 T=\operatorname{diag}(1,\alpha),\qquad \alpha=\sqrt2.
\]
For \(j=1,2\), let \(W_j^{(N)}\) be independent real symmetric Wigner matrices whose off-diagonal entries are independent copies of \(\xi_j/\sqrt N\).
The fixed real laws satisfy
\(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and \(|\xi_j|\le L\).
Each input has a fixed centered real diagonal law bounded by \(L\), with independent diagonal entries scaled by \(N^{-1/2}\).
Zero diagonal laws are allowed.
All upper-triangular coordinates and both inputs are independent within each size; cross-size dependence is unrestricted.
Enlarge the fixed \(L\) if necessary to cover all four laws.

For \(S\subset[N]\) with \(|S|\le1\), set \(n=N-|S|\), retain the principal physical submatrices \(C_{N,S},D_{N,S}\) of the two inputs, and put
\[
 \mathcal M_{N,S}
 =J_\circ\otimes I_n+I_2\otimes C_{N,S}+T\otimes D_{N,S}
 =\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix},
 \qquad X=C_{N,S}+D_{N,S},\quad
 Y=C_{N,S}+\alpha D_{N,S}.
 \tag{Actual-pencil}
\]
The retained entries still have normalization \(N^{-1/2}\), not \(n^{-1/2}\).
Let \(P_i\) be the rank-two physical coordinate projection at a retained index \(i\), and let \(\Pi_1,\Pi_2\) be the rank-\(n\) projections onto the two auxiliary channels.
Matrix block notation below uses the auxiliary-first order in (Actual-pencil).

There are constants \(\delta_0,C,c_*>0\), depending only on the fixed laws, such that the following assertions hold.

First, for every fixed \(0<\delta<\delta_0\),
\[
 \mathbb P\left\{
 \max_{\substack{|S|\le1\\i\notin S}}
 \left\|P_i(\mathcal M_{N,S}-i\delta)^{-1}P_i\right\|>C
 \right\}\longrightarrow0,
 \tag{Physical-resolvent}
\]
and, on an event of probability tending to one,
\[
 \max_{\substack{|S|\le1\\i\notin S}}
 \left\|P_i\mathbf1_{[-\delta,\delta]}(\mathcal M_{N,S})P_i\right\|
 \le 2C\delta.
 \tag{Physical-projector}
\]
The constants are independent of \(\delta\); the dimension threshold and convergence rate may depend on this fixed \(\delta\).
In particular, among all real unit eigenvectors corresponding to eigenvalues of smallest absolute value, the maximum physical coordinate mass tends to zero in probability, uniformly over \(|S|\le1\).
This statement also permits zero eigenvalues and arbitrary multiplicity.

Second, restrict each \(\mathcal M_{N,S}\) to its invertible branch.
For any real unit eigenpair
\(\mathcal M_{N,S}w=\lambda w\), write
\[
 w=\binom uv,\qquad q=\lambda^{-1},\qquad
 \mathsf E_w=\mathcal M_{N,S}^{-1}-qww^T
       =\begin{pmatrix}F&H_0\\H_0^T&J_0\end{pmatrix},
 \qquad T_0=(H_0+H_0^T)/2.
\]
Define
\[
 \begin{split}
 \mathcal R_w^2&=\|\operatorname{off}F\|_{\rm F}^2
       +\|\operatorname{off}J_0\|_{\rm F}^2
       +\|\operatorname{off}T_0\|_{\rm F}^2,\\
 \rho_{i,w}&=\sum_{j\ne i}
       \bigl(|F_{ij}|^2+|(J_0)_{ij}|^2+|(T_0)_{ij}|^2\bigr).
 \end{split}
\]
Here \(\operatorname{off}\) removes the diagonal in the original independent-coordinate basis.
For every fixed \(\varepsilon>0\),
\[
 \begin{split}
 \mathbb P\{\exists S,\ |S|\le1:\;&\mathcal M_{N,S}\text{ is invertible and there is a real unit eigenpair }(\lambda,w)\\
 &\text{with }\mathcal R_w^2<c_*\|\mathsf E_w\|_{\rm F}^2
       \text{ or }\max_i\rho_{i,w}>\varepsilon\mathcal R_w^2\}
 \longrightarrow0.
 \end{split}
 \tag{Residual-row-spread}
\]
The comparison includes \(\mathcal R_w>0\) eventually on the stated good events.
It is uniform over the removed eigenmode, including any choice inside an eigenspace.

These are unconditional bad-event bounds intersected with invertibility.
They do not prove that any of these minors is invertible with probability tending to one, or give a conditional probability bound after division by its invertibility probability.
They also do not prove a fourth-layer energy lower bound, dominance of the largest inverse mode, a least-value floor, or a logarithmic determinant lower limit.

<a id="inputs"></a>
## Fixed inputs and scope of reuse

The [bounded colored moment proof](Yin_C_F0186_v4.md#bounded-moments) supplies its tree expansion and noncrossing-pairing limit.
The weighted auxiliary insertion needed here is proved explicitly below.
The same fixed Claim's [source scope](Yin_C_F0186_v4.md#source-scope) retains the inspected ordinary bounded-differences inequality from War16; it is used here for independent bounded coordinate groups and for scalar quadratic forms.
The [bounded-product convex concentration inequality (9)](Yin_C_F0187_v2.md#proof) supplies the fresh-row lower tail, at its retained GNT14 source boundary.

The [semicircular Cauchy identity and uniqueness proof](Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness), equations (6)--(7), supply the finite-dimensional Dyson identity for selfadjoint coefficients.
The coefficient substitution \(I_2,T,J_\circ\), and the corresponding trace Poisson bound and bounded free density, are fixed in [L_F0066_v5](../ledger/Yin_L_F0066_v5.md#identity-direction-free-density).
Only this deterministic free input is used from that ledger.
The positive lower mass in each auxiliary channel is derived below, rather than inferred from the total density upper bound.

Finite-dimensional spectral calculus, Fourier inversion for smooth compactly supported functions, the integral identity for differences of matrix exponentials, Schur complements and fixed-dimensional sphere nets are used at their explicit elementary interfaces.
The argument below is independent of any rolling draft and uses no local-law theorem, bounded real inverse hypothesis or ordinary interlacing assertion about weighted spectral measures.
The [single-pole conditional development](../drafts/Yin_D_F0033.md#single-pole-residual-test) motivated the residual normalization; it is an application context, not a logical dependency.

<a id="argument"></a>
## Complete proof

<a id="positive-channel-mass"></a>
### Positive free mass in both auxiliary channels

Let
\[
 \ell=J_\circ\otimes1+I_2\otimes s_1+T\otimes s_2,\qquad
 G(z)=(\operatorname{id}_2\otimes\tau)((z-\ell)^{-1}),
\]
where \(s_1,s_2\) are free variance-one semicircular elements.
The reused Cauchy identity gives
\[
 G(z)^{-1}=zI_2-J_\circ-G(z)-TG(z)T.
 \tag{Two-channel-Dyson}
\]
Its strictly lower-half-plane solution is unique at \(z=i\eta\), \(\eta>0\), by the cited elementary uniqueness argument.

Transposition preserves this equation, its drift and covariance, and the strictly negative imaginary part.
Thus uniqueness gives \(G(i\eta)^T=G(i\eta)\).
Put \(Q=\operatorname{diag}(1,-1)\).
Since \(QJ_\circ Q=-J_\circ\) and \(QT=TQ\), the matrix \(-Q\overline{G(i\eta)}Q\) is another solution with strictly negative imaginary part.
Uniqueness therefore gives
\[
 G(i\eta)=\begin{pmatrix}-ia&r\\r&-ib\end{pmatrix},
 \qquad a,b>0,\quad r\in\mathbb R.
\]
Write \(\beta=1+\alpha\) and
\[
 D_\eta=(\eta+2a)(\eta+3b)+(1+\beta r)^2>0.
\]
Direct inversion of (Two-channel-Dyson) yields
\[
 aD_\eta=\eta+3b,\qquad
 bD_\eta=\eta+2a,\qquad
 r=-\frac1{D_\eta+\beta}.
 \tag{Positive-branch-equations}
\]
In particular
\(a(D_\eta^2-6)=\eta(D_\eta+3)>0\), so \(D_\eta>\sqrt6\).
The fixed trace Poisson bound gives \(a+b\le2\), and the displayed formula bounds \(r\).
Consequently \(a,b,r,D_\eta\) are bounded for \(0<\eta\le1\).

Consider any subsequential limit as \(\eta\downarrow0\).
If either of \(a,b\) vanished, both would vanish by the first two equations.
Then
\[
 D_\eta\longrightarrow
 \left(\frac{D_0}{D_0+\beta}\right)^2<1
\]
would contradict \(D_0\ge\sqrt6\).
Both limits are therefore positive, and the first two equations force \(D_0=\sqrt6\) and \(a_0/b_0=\sqrt{3/2}\).
The determinant equation gives
\[
 r_0=-\frac1{\sqrt6+\beta},\qquad
 a_0b_0=\frac1{\sqrt6}-\frac1{(\sqrt6+\beta)^2}>0.
 \tag{Positive-channel-limit}
\]
These conditions determine a unique positive \(a_0,b_0\), so they describe the full limit.

Let \(\mu_1,\mu_2\) be the probability measures given by the two diagonal entries of the free operator-valued spectral measure.
Their average is the scalar free law.
The fixed scalar density bound \(1/\pi\) therefore gives each \(\mu_\alpha\) a density at most \(2/\pi\).
Their Poisson transforms at zero tend respectively to \(a_0,b_0>0\).
This does not by itself assert pointwise continuity of either density.
For a fixed \(K>1\), the contribution of \(|t|>K\eta\) to either transform is at most
\[
 \frac2\pi\int_{|t|>K\eta}\frac{\eta}{t^2}\,dt
 =\frac4{\pi K}.
\]
Choose \(K\) so this is smaller than one quarter of \(\min(a_0,b_0)\), and then take \(\eta\) sufficiently small.
Since the Poisson kernel is at most \(1/\eta\),
\[
 \mu_\alpha([-K\eta,K\eta])\ge c\eta,\qquad \alpha=1,2.
\]
Renaming \(K\eta\) shows that, for fixed constants \(c_0,\delta_0>0\),
\[
 \mu_\alpha([-\delta,\delta])\ge c_0\delta
 \quad(0<\delta<\delta_0,\ \alpha=1,2).
 \tag{Channel-mass}
\]

<a id="weighted-minor-mass"></a>
### Weighted spectral mass uniformly after at most two physical deletions

For this paragraph allow \(|S|\le2\), and use the same principal pencil and normalization as in (Actual-pencil).
Its size is \(2n\), where \(n=N-|S|\).
For every fixed polynomial \(f\), the bounded colored moment expansion gives
\[
 \frac1n\mathbb E\operatorname{Tr}\Pi_\alpha f(\mathcal M_{N,S})
 \longrightarrow\int f(t)\,d\mu_\alpha(t).
 \tag{Weighted-moments}
\]
To verify the extra weight, expand each word in the coefficient matrices and the physical Wigner entries.
Inserting \(\Pi_\alpha\) changes the coefficient trace to its \(\alpha\)-th diagonal entry and leaves the index graph, centering and power count unchanged.
Only color-respecting paired trees survive.
The scaling factor \(n/N\to1\) leaves their limit unchanged, and diagonal loops remain lower order even when the two diagonal variances differ.
The resulting expected weighted measures are probability measures.
Their moments converge to those of the compactly supported free measure, with bounded higher moments giving uniform integrability.
Thus (Weighted-moments) also gives expected weak convergence.
The distribution depends on \(|S|\), not on the particular retained indices, so this expectation conclusion is uniform over the at most three deletion sizes.

For a real \(f\in C_c^\infty(\mathbb R)\), Fourier inversion and
\[
 e^{itA}-e^{itB}
 =i\int_0^t e^{i(t-s)A}(A-B)e^{isB}\,ds
\]
give, also for negative \(t\) with the integral orientation understood,
\[
 |\operatorname{Tr}\Pi_\alpha(f(A)-f(B))|
 \le C_f\|A-B\|_1,\qquad
 C_f=\int_{\mathbb R}|t\widehat f(t)|\,dt<\infty,
 \tag{Weighted-smooth-difference}
\]
up to the fixed Fourier normalization constant.
Here \(\|\cdot\|_1\) is trace norm.
The bound follows from the ideal property of trace norm and \(\|\Pi_\alpha\|=1\); it does not require the matrices or the weight to commute.

Group the independent raw coordinates by the first index of their upper-triangular position, including both inputs and their diagonal coordinates.
Replacing one such group changes the pencil only in a bounded number of physical rows and columns.
Its rank is bounded independently of \(N\), and its operator norm is bounded by a fixed multiple of \(L\), since every changed normalized row has bounded Euclidean norm.
Its trace norm is therefore bounded by a fixed constant.
By (Weighted-smooth-difference), the quantity
\(n^{-1}\operatorname{Tr}\Pi_\alpha f(\mathcal M_{N,S})\)
changes by at most \(C_{f,L}/n\) under one group replacement.
The accepted ordinary bounded-differences inequality gives
\[
 \mathbb P\left\{
 \left|\frac1n\operatorname{Tr}\Pi_\alpha f(\mathcal M_{N,S})
 -\frac1n\mathbb E\operatorname{Tr}\Pi_\alpha f(\mathcal M_{N,S})\right|>t
 \right\}
 \le2\exp(-c_{f,L}nt^2).
 \tag{Weighted-smooth-concentration}
\]

Fix \(0<\delta<\delta_0\).
Choose a smooth function \(0\le f_\delta\le1\) which equals one on \([-\delta/2,\delta/2]\) and vanishes outside \([-\delta,\delta]\).
Its free weighted integral is at least \(c_0\delta/2\) by (Channel-mass).
Expected weak convergence and (Weighted-smooth-concentration), followed by a union over both channels and all \(|S|\le2\), imply
\[
 \operatorname{Tr}\Pi_\alpha
       \mathbf1_{[-\delta,\delta]}(\mathcal M_{N,S})
 \ge c_1\delta n
 \quad(\alpha=1,2,\ |S|\le2)
 \tag{All-minor-channel-mass}
\]
outside a set of probability tending to zero.
For this fixed \(\delta\), the failure is bounded by \(C_\delta N^2e^{-c_\delta N}\) for all sufficiently large \(N\).
The threshold at which the expected weak convergence is accurate need not have a quantitative rate.
No weighted eigenvalue interlacing assertion is used.

<a id="fresh-row-projector"></a>
### Fresh independent rows turn channel mass into a physical projector bound

Fix \(|S|\le1\) and \(i\notin S\).
Reorder physical index \(i\) first, so
\[
 \mathcal M_{N,S}
 =\begin{pmatrix}A_i&B_i^T\\B_i&\mathcal M_{N,S\cup\{i\}}\end{pmatrix},
 \qquad \widehat B_i=\sqrt N\,B_i.
\]
The entries of \(\widehat B_i\) depend only on the two fresh input rows and are independent of the retained minor.
In auxiliary-first order, for \(u=(u_1,u_2)\in\mathbb C^2\), its coordinates at each remaining physical position are
\[
 \binom{u_1(\xi_1+\xi_2)}{u_2(\xi_1+\alpha\xi_2)}.
\]
The \(2\)-by-\(2\) covariance is
\[
 Q_u=\operatorname{diag}(u_1,u_2)
       \begin{pmatrix}2&\beta\\\beta&3\end{pmatrix}
       \operatorname{diag}(\overline u_1,\overline u_2)
 \ge\gamma\operatorname{diag}(|u_1|^2,|u_2|^2),
 \tag{Directional-covariance}
\]
where \(\gamma>0\), since \(6-\beta^2=(\sqrt2-1)^2>0\).
This lower bound is not a positive one-step coefficient frame on the full auxiliary space.

Condition on the retained minor and set
\(P=\mathbf1_{[-\delta,\delta]}(\mathcal M_{N,S\cup\{i\}})\).
On its event (All-minor-channel-mass), independence and centering give, for every unit \(u\),
\[
 \mathbb E\bigl[\|P\widehat B_i u\|^2\mid\mathcal M_{N,S\cup\{i\}}\bigr]
 =\operatorname{Tr}P\,\operatorname{Cov}(\widehat B_i u)
 \ge c_2\delta N.
 \tag{Projected-row-second-moment}
\]
The harmless replacement of the minor dimension \(N-|S|-1\) by \(N\) is valid for large \(N\).

As a function of the independent raw scalar coordinates, \(\|P\widehat B_i u\|\) is convex and has Lipschitz constant bounded independently of \(u,N\).
Each raw coordinate has support diameter at most \(2L\).
The accepted convex concentration inequality and its integrated squared-deviation bound imply that the median is at least \(c_3\sqrt{\delta N}\) for sufficiently large \(N\).
Its lower tail below half this value is at most \(Ce^{-c\delta N}\).
On the entire bounded support, \(\|\widehat B_i\|\le C_L\sqrt N\).
A deterministic sphere net of mesh a sufficiently small fixed multiple of \(\sqrt\delta\) in \(\mathbb C^2\) therefore makes the lower bound uniform in \(u\).
Its cardinality depends on \(\delta\) but not on \(N\).
Dividing by \(\sqrt N\), then taking a union over the \(O(N^2)\) choices of \(S,i\), gives
\[
 B_i^TPB_i\ge c_4\delta I_2
 \quad(|S|\le1,\ i\notin S)
 \tag{Projected-row-lower}
\]
with probability tending to one.
Conditioning is legitimate because every mirrored occurrence of these fresh coordinates disappears in the deleted physical column.
The estimates are averaged over both independent input matrices; no uniform assertion for every deterministic frozen second input is made.

Let \(R_i=(\mathcal M_{N,S\cup\{i\}}-i\delta)^{-1}\).
Spectral calculus gives
\[
 \operatorname{Im}R_i\ge(2\delta)^{-1}P.
\]
The physical diagonal block of the full resolvent is the inverse of
\(A_i-i\delta I_2-B_i^TR_iB_i\).
Its negative imaginary part is at least \(c_4I_2/2\) by (Projected-row-lower), so its inverse norm is at most \(2/c_4\).
This proves (Physical-resolvent).
Finally,
\[
 \mathbf1_{[-\delta,\delta]}(\mathcal M_{N,S})
 \le2\delta\,\operatorname{Im}(\mathcal M_{N,S}-i\delta)^{-1}
\]
in positive semidefinite order, proving (Physical-projector).

Every unit eigenvector with \(|\lambda|\le\delta\) consequently has
\(\|P_iw\|^2\le2C\delta\) at every physical index.
The free mass lower bound and the uniform minor count above ensure an eigenvalue in \([-\delta,\delta]\) for every \(|S|\le1\), with probability tending to one.
Thus every closest-to-zero eigenvector satisfies that leverage bound.
First choose \(\delta\) small and then let \(N\to\infty\); this proves the stated convergence in probability without an inverse bound or simplicity assumption.

<a id="spectral-residual-spread"></a>
### Full residual row energy and physical diagonal blocks

We first record a norm event obtained from the same bounded-differences input.
For a deterministic real unit vector \(v\), the scalar quadratic form \(v^TW_j^{(N)}v\) is a sum of independent centered bounded terms.
The sum of the squared replacement bounds is at most \(C L^2/N\).
Consequently its tail at a fixed \(t>0\) is at most \(2e^{-cNt^2/L^2}\).
A \(1/4\)-net of the real unit sphere has at most \(9^N\) elements, and
\(\|W_j^{(N)}\|\le2\max_v|v^TW_j^{(N)}v|\) over that net.
Choose a sufficiently large fixed \(t\).
It follows that both input norms, and hence every \(X,Y,\mathcal M_{N,S}\) with \(|S|\le1\), are bounded by a fixed \(K_0\) outside a set of probability \(Ce^{-cN}\).

Fix an invertible minor and remove any one unit eigenmode to form \(\mathsf E_w\).
It commutes with \(\mathcal M_{N,S}\).
The remaining \(2n-1\) inverse eigenvalues and Cauchy--Schwarz give
\[
 \|\mathsf E_w\|_{\rm F}^2
 \ge\frac{(2n-1)^2}{\operatorname{Tr}\mathcal M_{N,S}^2}
 \ge c_5 n
 \tag{Residual-basic-size}
\]
on this norm event, uniformly in the removed mode.

In fact \(\|\mathsf E_w\|_{\rm F}^2/n\) diverges in probability, uniformly in the same sense on all invertible minors.
To see this, (Channel-mass) and the free density upper bound give fixed \(a_*>0,c_6>0\) such that
\[
 \mu_\ell\{a_*h\le|t|\le h\}\ge c_6h
\]
for every sufficiently small fixed \(h>0\).
Choose a smooth function between zero and one which equals one on this annulus and vanishes outside \(\{a_*h/2<|t|<2h\}\).
The weighted moment/concentration argument above, summed over the two channels, gives at least \(c_7hn\) eigenvalues in an annulus with upper absolute endpoint at most \(2h\), simultaneously for all \(|S|\le1\), with probability tending to one.
Deleting one eigenmode removes at most one from this count.
Therefore
\[
 \|\mathsf E_w\|_{\rm F}^2
 \ge\frac{c_7hn-1}{4h^2}.
 \tag{Residual-divergence}
\]
Taking \(N\to\infty\) at fixed \(h\), and then \(h\downarrow0\), proves the asserted uniform divergence.
This argument does not first divide by the probability of invertibility.

For fixed \(\delta\), split
\(\mathsf E_w=\mathsf E_<+\mathsf E_>\)
using the spectral projection of \(\mathcal M_{N,S}\) onto \([-\delta,\delta]\) and its complement.
This decomposition is orthogonal in spectral coordinates, including when the removed mode lies in a repeated eigenspace.
On (Physical-projector), every low-energy unit eigenvector has physical mass at most \(2C\delta\).
Thus, for
\(d_i(\mathsf E_w)=\|P_i\mathsf E_w\|_{\rm F}^2\),
\[
 d_i(\mathsf E_w)
 \le2C\delta\|\mathsf E_<\|_{\rm F}^2+2\delta^{-2},
 \tag{Full-row-bound}
\]
because \(\|\mathsf E_>\|\le\delta^{-1}\) and \(P_i\) has rank two.
After division by (Residual-basic-size), this proves
\[
 \frac{\max_i d_i(\mathsf E_w)}{\|\mathsf E_w\|_{\rm F}^2}
 \longrightarrow0
 \tag{Full-row-spread}
\]
in probability on the invertible branch, uniformly over minors and removed modes.

The energy inside physical diagonal blocks is also negligible.
Put
\(\mathcal D(\mathsf E_w)=\sum_i\|P_i\mathsf E_wP_i\|_{\rm F}^2\).
If \(P_<\) denotes the low-energy projection, then
\[
 \|P_i\mathsf E_<P_i\|_{\rm F}^2
 \le\|P_iP_<\|^2\|\mathsf E_<P_i\|_{\rm F}^2
 \le2C\delta\,\operatorname{Tr}P_i\mathsf E_<^2.
\]
For the high-energy part, each diagonal block has squared Frobenius norm at most \(2\delta^{-2}\).
Consequently
\[
 \mathcal D(\mathsf E_w)
 \le4C\delta\|\mathsf E_w\|_{\rm F}^2+4n\delta^{-2}.
 \tag{Physical-diagonal-energy}
\]
Use (Residual-divergence) at fixed \(\delta\), then send \(\delta\downarrow0\).
This gives
\(\mathcal D(\mathsf E_w)/\|\mathsf E_w\|_{\rm F}^2\to0\)
with the same uniform bad-event meaning.
No assertion about individual inverse entries follows from a spectral moment alone; fresh-coordinate concentration supplied the physical projector bound used here.

<a id="actual-residual-blocks"></a>
### The actual block identity controls the residual scale

Write the full inverse as
\[
 \mathcal M_{N,S}^{-1}
 =\begin{pmatrix}G&H\\H^T&J\end{pmatrix}.
\]
The upper-left block of \(\mathcal M_{N,S}^{-1}\mathcal M_{N,S}=I\) gives
\(H=I-GX\).
The eigenvector equation gives \(v=\lambda u-Xu\).
Subtracting the chosen mode therefore yields the exact identity
\[
 H_0=H-q uv^T=I-uu^T-FX.
 \tag{Residual-actual-identity}
\]
This is where the actual pencil structure controls a potentially large antisymmetric part of \(H_0\).

Since \(\|X\|\le K_0\) on the norm event and \(\|I-uu^T\|_{\rm F}^2\le n\),
\[
 \begin{split}
 \|\mathsf E_w\|_{\rm F}^2
 &=\|F\|_{\rm F}^2+\|J_0\|_{\rm F}^2+2\|H_0\|_{\rm F}^2\\
 &\le(1+4K_0^2)(\|F\|_{\rm F}^2+\|J_0\|_{\rm F}^2)+4n.
 \end{split}
 \tag{Residual-block-comparison}
\]
Moreover,
\[
 \begin{split}
 \mathcal R_w^2
 &\ge\|F\|_{\rm F}^2+\|J_0\|_{\rm F}^2
       -\sum_i(|F_{ii}|^2+|(J_0)_{ii}|^2)\\
 &\ge\frac{\|\mathsf E_w\|_{\rm F}^2-4n}{1+4K_0^2}
       -\mathcal D(\mathsf E_w).
 \end{split}
\]
By (Residual-divergence) and (Physical-diagonal-energy), this is at least
\(c_*\|\mathsf E_w\|_{\rm F}^2\), with
\(c_*=[2(1+4K_0^2)]^{-1}\), outside a set of probability tending to zero.

Finally,
\(|(T_0)_{ij}|^2\le(|(H_0)_{ij}|^2+|(H_0)_{ji}|^2)/2\),
so \(\rho_{i,w}\le d_i(\mathsf E_w)\).
The comparison just proved and (Full-row-spread) give (Residual-row-spread).
All estimates are uniform in the removed eigenmode on the same events, rather than union bounds over a selected eigenbasis.
This completes the argument.

<a id="remaining-energy-boundary"></a>
## What this supplies to the original minor question

For the closest-to-zero mode of an invertible actual minor in this bounded real model, both its physical leverage and the normalized residual off-diagonal row load vanish in probability.
This proves the two spread conditions used by the single-pole coefficient test through actual randomness in the original coordinate basis.
It does not prove that the pole dominates the residual scale, or that the cross fourth layer has energy bounded below by a fixed multiple of \(\mathcal R_w^2/N^4\).
Those cancellation and normalization questions remain even after the present load estimates.
The singular branch, the matrix-distance conversion, the bottom logarithm and extension beyond bounded laws also remain unresolved here.
No completion or lower-deviation estimate for the full F0013 contract follows solely from this Claim.

## Current assessment
[Selected decision](#decision-bounded-two-channel-reviewed)

## Assessment history

### Decision bounded-two-channel-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T18:38 |
| status | open |
| reason | Complete candidate probability argument for weak physical delocalization and residual row-energy spread in the fixed bounded real two-channel model, uniform over single physical deletions. Independent checking of the free partial-mass calculation, weighted minor concentration, fresh-row estimate and actual residual normalization remains required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact bounded two-channel conclusions](#statement) | Physical projector bounds and invertible-branch residual row-energy spread, including all single physical minors and the original N normalization. |
| argument | [Complete candidate proof](#argument) | Positive channel mass, weighted concentration, independent fresh rows, spectral residual estimates and actual inverse-block identity. |
| dependency | [Bounded colored moments and concentration source](Yin_C_F0186_v4.md#bounded-moments) | Fixed-law bounded Wigner tree expansion and the Claim's inspected ordinary bounded-differences input; the weighted insertion and finite-deletion use are supplied locally. |
| dependency | [Convex bounded-product concentration](Yin_C_F0187_v2.md#proof) | Equation (9) only, with fixed coordinate diameter and uniformly bounded Lipschitz constant. |
| dependency | [Semicircular Cauchy identity](Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness) | Equations (6)--(7) and elementary uniqueness at positive imaginary spectral parameter. |
| dependency | [Fixed free density bound](../ledger/Yin_L_F0066_v5.md#identity-direction-free-density) | The same two-channel coefficient substitution and scalar density at most 1/pi; the channel lower bound is proved here. |

### Decision bounded-two-channel-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T19:05 |
| status | proved |
| reason | The independent whole-proof finding checks the free channel mass, weighted minor concentration, fresh-row independence, physical projector bounds and residual normalization for all stated minor and eigenmode choices. This adopts the bounded-model spread conclusions while retaining the singular branch, fourth-layer energy, pole dominance and full determinant contract as unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact bounded two-channel conclusions](#statement) | Physical projector bounds and invertible-branch residual row-energy spread, including all single physical minors and the original N normalization. |
| argument | [Complete candidate proof](#argument) | Positive channel mass, weighted concentration, independent fresh rows, spectral residual estimates and actual inverse-block identity. |
| dependency | [Bounded colored moments and concentration source](Yin_C_F0186_v4.md#bounded-moments) | Fixed-law bounded Wigner tree expansion and the Claim's inspected ordinary bounded-differences input; the weighted insertion and finite-deletion use are supplied locally. |
| dependency | [Convex bounded-product concentration](Yin_C_F0187_v2.md#proof) | Equation (9) only, with fixed coordinate diameter and uniformly bounded Lipschitz constant. |
| dependency | [Semicircular Cauchy identity](Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness) | Equations (6)--(7) and elementary uniqueness at positive imaginary spectral parameter. |
| dependency | [Fixed free density bound](../ledger/Yin_L_F0066_v5.md#identity-direction-free-density) | The same two-channel coefficient substitution and scalar density at most 1/pi; the channel lower bound is proved here. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0191_v4.md#bounded-two-channel-physical-spread) | Complete statement and argument, all exact dependency interfaces, bounded real laws, uniform physical minors and eigenmodes, and unconditional invertible-branch interpretation. |

