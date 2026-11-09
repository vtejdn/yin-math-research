---
author: Yin
---

# Disk averages and a truncated second eigenvalue moment for F0012

This working argument concerns the [fixed-law finite-variance Wigner problem](../tasks/Yin_T_F0012_v3.md#contract).
It gives a one-statistic criterion for an arbitrary fixed polynomial, and proves the full convergence when the filled Brown support has zero planar area.
The general lower bound for the statistic is open.
The filled-support theorem and its free-semidefinite product application are now fixed with independent review in [C186v25](../claims/Yin_C_F0186_v25.md#decision-free-semidefinite-reviewed).
The general disk-moment and paired-growth investigations retain the checking limits stated at their responsible records.

<a id="positive-part"></a>
## The upper bound for the potential

Let \(A_N=P(W^{(N)})\), \(a=P(s)\), \(\mu_N\) be the empirical eigenvalue probability measure, and \(\mu\) be the Brown measure of \(a\).
Use the sign convention \(U_\eta(z)=\int\log|z-w|\,d\eta(w)\) and write \(u_N=U_{\mu_N}\), \(u=U_\mu\).
All integrals in \(z\) below use Lebesgue area \(dA\).
Fix a sample in the probability-one event of the [regularized potential limits](../claims/Yin_C_F0186_v4.md#regularized-potentials) for \(\delta=1/k\) and the [eigenvalue bounds](../claims/Yin_C_F0186_v4.md#noncompact-planar).
For each such \(\delta\), the singular-value regularization \(u_{N,\delta}\) majorizes \(u_N\) and converges locally uniformly to \(u_\delta\).
Also \(u_\delta\downarrow u\) in local \(L^1\).
For any bounded disk \(D\), these facts give
\[
 \limsup_N\int_D(u_N-u)_+\,dA\le \int_D(u_\delta-u)\,dA .
\]
Sending \(\delta\) to zero gives \(\int_D(u_N-u)_+\,dA\to0\) on this same event for every bounded disk.
This uses regularized Hermitization and no estimate for a least singular value.

<a id="disk-moment"></a>
## A disk average and the remaining lower bound

Fix \(R>\max_{w\in\operatorname{supp}\mu}|w|\), for instance \(R>\|a\|\), and let \(D_R=\{|z|<R\}\).
Define \(m=\int|w|^2\,d\mu(w)\) and \(m_{N,R}=\int\min(|w|^2,R^2)\,d\mu_N(w)\).
We claim the pathwise identity
\[
 \int_{D_R}|u_N-u|\,dA=\frac{\pi}{2}(m-m_{N,R})+o(1).
 \tag{1}
\]
In addition, \(\int_{R<|z|<S}|u_N-u|\,dA\to0\) for every \(S>R\).

The [circle mean used for scalar spectral smoothing](../ledger/Yin_L_F0065_v1.md#scalar-planar-smoothing) gives
\[
 \frac1{2\pi}\int_0^{2\pi}\log|re^{i\theta}-w|\,d\theta=\log\max(r,|w|).
\]
Write \(t_N(r)=\int\log^+(|w|/r)\,d\mu_N(w)\).
For \(r>\max_{\operatorname{supp}\mu}|w|\), the circular mean of \(u_N-u\) is \(t_N(r)\ge0\).
The logarithmic singularity of an eigenvalue on the circle is integrable.
Radial integration shows that the signed integral of \(u_N-u\) over each such exterior annulus is nonnegative.
Its \(L^1\) norm there is therefore bounded by twice the integral of \((u_N-u)_+\), which tends to zero.
In particular, choose \(\max_{\operatorname{supp}\mu}|w|<r_0<R\).
Monotonicity in \(r\) gives
\[
 \pi(R^2-r_0^2)t_N(R)
 \le\int_{r_0<|z|<R}(u_N-u)\,dA
 \le\int_{D_R}(u_N-u)_+\,dA\longrightarrow0 .
\]

Integrating the same circle mean with \(2\pi r\,dr\) from zero to \(R\) gives the exact kernel identity
\[
 \int_{D_R}\log|z-w|\,dA(z)
 =\pi R^2(\log R-\tfrac12)
  +\frac{\pi}{2}\min(|w|^2,R^2)+\pi R^2\log^+(|w|/R).
 \tag{2}
\]
Indeed, one splits the radial integral at \(|w|\) when \(|w|<R\).
Integrating (2) against \(\mu_N-\mu\) gives
\(\int_{D_R}(u_N-u)\,dA=\tfrac\pi2(m_{N,R}-m)+\pi R^2t_N(R)\).
Put \(p_{N,R}=\int_{D_R}(u_N-u)_+\,dA\) and \(E_{N,R}=\int_{D_R}|u_N-u|\,dA\).
The identity \(|x|=2x_+-x\) gives the exact remainder
\[
 E_{N,R}-\frac{\pi}{2}(m-m_{N,R})
 =2p_{N,R}-\pi R^2t_N(R).
\]
Both terms on the right tend to zero on the control event, which proves (1).

In particular \(\limsup_N m_{N,R}\le m\).
Convergence \(u_N\to u\) in \(L^1_{\mathrm{loc}}(\mathbb C)\) is equivalent to the single lower bound \(\liminf_N m_{N,R}\ge m\), by (1) and exterior annulus convergence.
The [pathwise Brown criterion](../claims/Yin_C_F0186_v4.md#remaining-defect) then gives exactly the weak convergence required by F0012.
The cutoff in \(m_{N,R}\) keeps this test bounded under finite second moments of the original inputs.
The statistic uses eigenvalues of \(A_N\), while \(N^{-1}\operatorname{Tr}(A_N^*A_N)\) measures squared singular values.
For the [nilpotent shifts with Haar unitary limit](../ledger/Yin_L_F0058_v1.md#failed-shortcuts), \(m_{N,R}=0\) and \(m=1\) at every \(R>1\).
In this example \(E_{N,R}=\pi/2\) and the remainder in (1) is identically zero.

<a id="one-disk-criterion"></a>
## Weak convergence from one disk

The same criterion applies to any sequence of probability measures \(\mu_N\) with \(\int\log^+|w|\,d\mu_N(w)<\infty\) and a probability measure \(\mu\) compactly supported in \(D_R\), provided \(p_{N,R}\to0\).
Only this one disk is needed for weak convergence.
Necessity follows by testing weak convergence against the bounded continuous function \(w\mapsto\min(|w|^2,R^2)\), which equals \(|w|^2\) on the support of \(\mu\).
For sufficiency, \(t_N(R)\ge0\) in the exact remainder gives, for each \(N\),
\[
 E_{N,R}\le 2p_{N,R}+\frac{\pi}{2}(m-m_{N,R})_+ .
\]
Thus \(\liminf_N m_{N,R}\ge m\) gives \(E_{N,R}\to0\).
For every \(\varphi\in C_c^\infty(D_R)\), the distributional Laplacian identity bounds \(\left|\int\varphi\,d(\mu_N-\mu)\right|\) by \(\|\Delta\varphi\|_\infty E_{N,R}/(2\pi)\).
This gives vague convergence on \(D_R\) by uniform approximation of continuous compactly supported tests.
Take a smooth cutoff \(0\le\chi\le1\) supported in \(D_R\) and equal to one on \(\operatorname{supp}\mu\).
Then \(\int(1-\chi)\,d\mu_N\to0\), and applying the local conclusion to \(\chi f\) gives weak convergence on the plane for every bounded continuous \(f\).
In particular on the F0012 control event the quantity \(\limsup_N E_{N,R}=\frac{\pi}{2}(m-\liminf_N m_{N,R})\) vanishes exactly when \(\mu_N\Rightarrow\mu\).

For example, take elements \(a_N,a\) in tracial von Neumann algebras with normalized traces, with \(a_N\) converging in \(*\)-moments to \(a\) and \(M=\max(\|a\|,\sup_N\|a_N\|)<\infty\).
Choose \(R>M\) and let the measures be their Brown measures.
For fixed \(z\in D_R\) and \(\delta>0\), approximate \(t\mapsto\frac12\log(t+\delta^2)\) uniformly by polynomials on \([0,(M+R)^2]\) and apply \(*\)-moment convergence to \((a_N-z)^*(a_N-z)\).
The resulting regularized potentials \(u_{N,\delta}\) converge pointwise to \(u_\delta\) and, by the common bound at this \(\delta\), also in \(L^1(D_R)\).
Since \(u_N\le u_{N,\delta}\) and \(u_\delta\downarrow u\) in \(L^1(D_R)\), the [positive-part argument](#positive-part) gives \(p_{N,R}\to0\).
All Brown measures here are supported in \(\{|w|\le M\}\), so weak convergence is equivalent to convergence of their ordinary second radial moments.

<a id="literature-precedent"></a>
## The Biane--Lehner antecedent

The bounded-operator criterion follows directly from BL01, Lemma 2.1, in Section 2.1 of the published paper, printed p. 183.
The [published original](https://www.impan.pl/shop/publication/transaction/download/product/87905#page=3) and the [1999 preprint](https://arxiv.org/pdf/math/9912242v1#page=2) have the same lemma number, hypotheses and two potential conclusions.
The inspected passages are Lemma 2.1 and its proof, and Corollary 2.2 and its proof, on printed pp. 183--184 of the publication and PDF pp. 2--3 of the preprint.
The source supplies the potential comparison and exterior equality used below.
The second-moment equivalence and its calculation are the following deduction.

Under the preceding common operator-norm bound and \(*\)-moment convergence, let \(\nu\) be any subsequential weak limit of \(\mu_{a_N}\).
Lemma 2.1 gives \(U_\nu\le U_{\mu_a}\), with equality for all sufficiently large \(|z|\).
Consequently \(h=U_{\mu_a}-U_\nu\) is a nonnegative, compactly supported \(L^1\) function, defined almost everywhere, with \(\Delta h=2\pi(\mu_a-\nu)\).
Choose a smooth compactly supported \(\chi\) equal to one on a neighborhood of the supports of \(h,\mu_a,\nu\).
Testing against \(\chi(z)|z|^2\) and using \(\Delta|z|^2=4\) yields
\[
 \int |w|^2\,d\mu_a(w)-\int |w|^2\,d\nu(w)
 =\frac{2}{\pi}\int_{\mathbb C}h(z)\,dA(z)\ge0.
\]
Equality forces \(h=0\) almost everywhere and hence \(\nu=\mu_a\).
Common compact support makes the second radial moment continuous along every weakly convergent subsequence.
It follows that \(\limsup_N\int|w|^2\,d\mu_{a_N}\le\int|w|^2\,d\mu_a\), and that weak convergence to \(\mu_a\) is equivalent to the reverse liminf inequality.
Corollary 2.2 gives \(\operatorname{supp}\nu\subseteq\mathbb C\setminus G\), and its proof gives equality of the two potentials on the unbounded component \(G\) considered below.
Thus the bounded version of that support argument also has a published antecedent.

The literature check on 2026-11-09 addressed the provenance of the second-moment criterion and the finite-\(N\) remainder (1).
Searches used Brown measure with second moment, logarithmic potential, balayage, offdiagonality, upper semicontinuity and truncated radial moment, and inspected the relevant primary passages of BL01 and the [previously located Sni02 determinant upper bound](../audits/literature/Sni02/readme.md).
The located sources supply the potential-order mechanism, while no inspected passage states this precise second-moment equivalence or the truncated finite-\(N\) formula (1).
This scoped search establishes a sufficient reference for the bounded criterion, with the precise cutoff formulation's publication history still undetermined.
For the fixed-law finite-variance F0012 contract, the common operator-norm bound is an extra hypothesis.
The cutoff criterion here instead uses the [one-disk positive-part control](#one-disk-criterion), and the lower bound on \(m_{N,R}\) for arbitrary \(P\) remains the separate input identified below.

<a id="thin-support"></a>
## Convergence on the unbounded component and a sufficient support condition

Let \(G\) be the unbounded component of \(\mathbb C\setminus\operatorname{supp}\mu\), and let \(H=\mathbb C\setminus G\).
Then \(u_N\to u\) in \(L^1_{\mathrm{loc}}(G)\).
If \(H\) has planar area zero, the convergence holds in \(L^1_{\mathrm{loc}}(\mathbb C)\) and the empirical measures converge weakly to \(\mu\).
This covers a Brown support contained in a line segment.
The unit circle illustrates why bounded complementary components enter \(H\).

The complete finite-variance proof is fixed in [C186v25](../claims/Yin_C_F0186_v25.md#argument), with the [independent whole-proof finding](../audits/reviews/Yin_R_F0190_v24.md#free-semidefinite-whole-proof).
Its [product application](../claims/Yin_C_F0186_v25.md#free-semidefinite-factor) covers arbitrary repeated-variable self-adjoint factors \(A,B\) whenever \(B(s)\) is semidefinite, including models in which \(B(W^{(N)})\) is eventually indefinite.

<a id="wigner-lower-bound"></a>
## The missing estimate for arbitrary support

For a general \(P\), the remaining random-matrix input is a lower bound on \(m_{N,R}\) under the original fixed laws.
For the quantifier over all cross-size couplings, an exact marginal target is
\[
 \sum_N\mathbb P\{m_{N,R}<m-\eta\}<\infty
 \qquad\text{for every rational }\eta>0 .
\]
It suffices by the first Borel--Cantelli lemma.
It is necessary for an every-coupling conclusion because independent matrices across sizes form an allowed coupling, to which the second Borel--Cantelli lemma applies.
No such marginal bound for arbitrary \(P\) follows from (1) or the Hermitized weak limits.
For independent row-block replacements, the [fourth-moment bound and mean condition](../ledger/Yin_L_F0067_v1.md#mean-and-influences) give one sufficient route to this summability.
The [single-entry construction for bounded Wigner inputs](../ledger/Yin_L_F0067_v1.md#single-entry-oscillation) rules out a uniform \(o(1)\) influence bound, leaving the size of typical changes open.

<a id="paired-border-growth"></a>
## Continuing paired-border test

The [fixed paired-border calculation](../ledger/Yin_L_F0067_v2.md#paired-border-growth) gives a deterministic increase of two controlled singular factors from one simultaneous scalar row and column addition, allowing arbitrary dependence of the two fresh borders.
It supplies a symmetry-compatible replacement for the independent half-steps in SSS25 until only one old singular direction remains.
The [terminal calculation and fixed-law example](../ledger/Yin_L_F0067_v2.md#paired-border-terminal) identify exact conditional cancellation and show why planar integration removes that particular two-root example at cost at most \(\pi/N\).
For general polynomial evaluations, physical compression must be performed on an exact affine linearization, which introduces an auxiliary block sharing the same fresh input borders.
The next test is a simultaneous auxiliary-block version of the fixed inequality, retaining the complete Schur block and an accumulated logarithmic cost tending to zero.
Its application also requires original-law projection lower bounds and a terminal small-dimensional Schur estimate with its actual dependence on \(z\).

<a id="auxiliary-block-interface"></a>
### Exact auxiliary-block reduction and the unresolved volume bound

The bounded follow-up on 2026-11-09 tested a simultaneous auxiliary block of size \(k=2\), with the following algebra valid for arbitrary \(k\).
Let
\[
 B=\begin{pmatrix}M&U\\V^*&D\end{pmatrix},\qquad
 U,V\in\mathbb C^{n\times k},\qquad D\in\mathbb C^{k\times k},
\]
and choose \(0\le r\le n-2k\).
Assume \(p_r(M)>0\), since a proposed lower bound with this factor is otherwise trivial.
In singular-vector bases for \(M\), write \(M=\operatorname{diag}(D_1,T)\), where \(D_1\) has size \(r\) and \(T\) has size \(h=n-r\).
Split \(U=\binom{U_1}{X}\), \(V=\binom{V_1}{Y}\), and retain the full auxiliary Schur block
\[
 A=D-V_1^*D_1^{-1}U_1.
\]
When \(A\) is invertible, compress \(\bigwedge^{r+2k}B\) to the exterior bases containing all \(r\) head coordinates, any \(k\) tail coordinates and all \(k\) auxiliary coordinates.
For each pair of tail index sets \(I,J\), the corresponding minor is
\[
 \det(D_1)\det(A)\det\bigl(T_{I,J}-X_I A^{-1}Y_J^*\bigr).
\]
Thus this compression is \(p_r(M)\det(A)\bigwedge^k E\), where
\[
 R=XA^{-1}Y^*,\qquad E=T-R,
\]
and its norm gives the exact lower bound
\[
 p_{r+2k}(B)\ge p_r(M)|\det A|\,p_k(E).
 \tag{Block-compression}
\]
Let \(P\) project onto the left-singular directions of \(T\) after its first \(k\), and put \(\operatorname{vol}_k(Z)=\det(Z^*Z)^{1/2}\) for a matrix with \(k\) columns.
Factoring the rank-at-most-\(k\) exterior map gives
\[
 p_k(PR)=\frac{\operatorname{vol}_k(PX)\operatorname{vol}_k(Y)}{|\det A|}.
 \tag{Block-volume}
\]
Consequently a sufficient deterministic interface is a constant \(C_k<\infty\), depending only on \(k\), such that
\[
 p_k(PR)\le C_k\,p_k(T-R)
 \quad\text{whenever }\operatorname{rank}R\le k,
 \qquad P=P_{>k}^{\mathrm{left}}(T).
 \tag{Projection-volume-target}
\]
It would imply the desired block gain
\[
 p_{r+2k}(B)\ge C_k^{-1}p_r(M)
       \operatorname{vol}_k(PX)\operatorname{vol}_k(Y).
\]
Only after proving a uniform constant in this interface could that resulting block inequality be extended to singular \(A\) by perturbing \(D\) and continuity.
The interface is sufficient, not an equivalence with the full block inequality, because the exterior compression can lose norm.
The scalar calculation gives \(C_1=2\), but it does not establish \(C_2\).
Repeating scalar additions changes the intermediate Schur blocks and projection spaces, so it does not supply the displayed simultaneous-block estimate or fresh conditional randomness.

The related source LHZ21, inspected in [arXiv:2008.01312v3](https://arxiv.org/pdf/2008.01312v3) at Theorem 2 on PDF p. 5, Lemma 4 and its use on PDF p. 8, and equation (16) on PDF p. 9, proves Schatten-\(q\) projection-error bounds for real matrices.
In the notation above, its Theorem 2 gives \(\|PR\|_q\le2\|(T-R)_{\max(k)}\|_q\) for \(1\le q\le\infty\).
These norm bounds do not imply (Projection-volume-target), which controls the product of the first \(k\) singular values rather than their \(q\)-power sum.
No proof or counterexample for (Projection-volume-target) at \(k=2\) was obtained in this bounded follow-up.
The next mathematical decision is whether that specific multiplicative inequality holds; the original-law projection estimates and terminal Schur control remain separate even if it does.
