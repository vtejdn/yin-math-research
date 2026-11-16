---
author: Yin
---

# An averaged square-density estimate for both canonical domains

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a finite bounded normal generating tuple satisfying the [actual starred conjugate-variable hypothesis](../tasks/Yin_T_F0011_v1.md#contract) in a finite tracial von Neumann algebra \((M,\tau)\).
Write \(P=\mathbb C\langle X,X^*\rangle\), \(\delta=\delta_i\), \(\xi=\delta^*(1\otimes1)\), and \(\mu\) for the law of \(Z\).
Put \(D=\operatorname{diam}(\operatorname{supp}\mu)>0\), \(r_j=2^{-j}D\), and
\[
        W=\int\sum_{j\ge0}
                   \frac{\mu(B(z,8r_j))^2}{r_j^2}\,d\mu(z).
        \tag{1}
\]
If \(W<\infty\), the canonical \(D_i=-\overline{(\mathrm{id}\otimes\tau)\delta}\) and its Hilbert adjoint have domains containing \(M\Omega\), and \([X_k,D_i]=\delta_{ik}P_\Omega\) on \(M\Omega\).
The other coordinates can have arbitrary normal spectra and correlations.
The two oriented original slices satisfy operator-norm-to-\(L^2\) bounds by \(C(\|\xi\|_2+\sqrt W)\) with an absolute constant \(C\).
Thus (1) at every coordinate gives \(\mathsf A\Rightarrow\mathsf S\) in this class.

The estimate uses localization in both spectral variables of the signed curvature form.
There is a compactly supported absolutely continuous planar probability satisfying (1), with actual scalar vacuum, for which the quadratic form of the curvature integral kernel on bounded unit vectors of \(L^2(\mu)\) is unbounded both above and below.
On this example the [positive projection-block decomposition with a row-bounded remainder](Yin_C_F0292_v1.md#statement) is impossible.

## Argument

### A localized kernel in the liberation energy

Let \(\gamma\) denote partial liberation at \(Z\), with \(\gamma(f)=f\otimes1-1\otimes f\) on its marginal and zero on omitted coordinates.
Its vacuum for \(i\gamma\) is \(\zeta=-i[Z^*,\xi]\).
The [liberation identities](Yin_C_F0238_v1.md#statement) give \(d\nu_\zeta=|z-v|^2d\nu_\xi\) for the corresponding spectral measures of left and right multiplication.
Fix a Borel set \(B\) of marginal mass \(t>0\) and put \(e=1_B(Z)\), \(h=\|e\zeta e\|_2\).
For a bounded real symmetric kernel \(q\) supported on \(B^2\) set \(E_q=(\mathrm{id}\otimes\tau)iI_q\gamma\), with inner insertion \(I_{s\otimes l}(v\otimes w)=vs\otimes lw\).
For \(u=a\pm i\sqrt{1-a^2}\) from a strict selfadjoint polynomial contraction define \(Q_q(u)=\operatorname{Im}\langle u,E_qu\rangle\), with inner products linear in the second variable.
We claim
\[
       |Q_q(u)|\le\|q\|_\infty(2\sqrt t\,h+3t^2).                        \tag{2}
\]

First take a finite real symmetric simple tensor sum on \(B^2\) with \(\|q\|_\infty\le1\), represented with both factors supported on \(B\).
Put \(b_k=q^{\circ k}\) for kernel composition against \(\mu\).
Then \(b_k\) is supported on \(B^2\) with \(\|b_k\|_\infty\le t^{k-1}\), as the \(k-1\) integrations are over \(B\).
The vacuum of \(iI_{b_k}\gamma\) is \(S_{b_k}\zeta\) and has norm at most \(t^{k-1}h\) by the [marginal adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint).
The row integral of \(b_k\) has \(L^2(\mu)\) norm at most \(t^{k+1/2}\).
Every \(E_{b_k}u\) ends in the projection \(e\), by inner insertion and the binomial series.
In equations (B0c) and (B0e) of the [exact finite-kernel energy identities](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy), the composition term therefore has absolute value at most \(\|ue\|_2\|E_{b_{2k}}u\|_2=\sqrt t\,\|E_{b_{2k}}u\|_2\).
Writing \(v_k=\|E_{b_k}u\|_2\), the two identities yield
\[
      v_k^2\le2(t^{k-1}h+t^{k+1/2})v_k+\sqrt t\,v_{2k}.
\]
For this fixed \(u\), the finite Leibniz expansion at \(a\) and its differentiated binomial series give \(v_k\le C_u\|b_k\|_{L^2(\mu^2)}\le C_u t^k\).
The finite bound follows because inserting \(b_k\) into each bounded simple tensor of \(\gamma(a)\) costs at most its two coefficient norms times \(\|b_k\|_2\), and differentiating \(a^l\) costs at most \(l\|a\|^{l-1}\) times the derivative norm at \(a\).
For \(w_k=v_k/t^{k-1}\) the recurrence reads \(w_k^2\le2(h+t^{3/2})w_k+t^{3/2}w_{2k}\).
Taking the finite supremum over dyadic \(k\) bounds it by \(2h+3t^{3/2}\), by a sequence approaching the supremum.
A final pairing against \(ue\) gives (2).
For arbitrary measurable \(q\), conditional expectations on refining finite product partitions respecting \(B\) preserve symmetry, support and the sup norm and converge in \(L^2(\mu^2)\).
The same fixed-\(u\) insertion bound passes (2) to the limit and homogeneity restores \(\|q\|_\infty\).

### Summing by triangle diameter

Put \(g(z,v)=\int\kappa(z,w,v)^2\,d\mu(w)\), with \(\kappa\) the reciprocal circumradius and zero on repeated or collinear triples.
For each \(j\) use the half-open planar grid of side \(r_j\).
Assign each triple of distinct points of positive diameter to its unique shell \((r_j/2,r_j]\) and to the square \(A\) containing the third point \(w\).
Let \(q_{jA}(z,v)\) be the resulting restricted integral of \(\kappa^2\) over \(w\).
For the concentric half-open square \(B=5A\), both endpoints then belong to \(B\).
Write \(t_B=\mu(B)\), \(e_B=1_B(Z)\), \(h_B=\|e_B\zeta e_B\|_2\), \(s_{jA}=\|q_{jA}\|_\infty\), and omit zero-mass squares \(B\).
Since \(\kappa\le2/\operatorname{diam}(\{z,w,v\})\), we have
\[
               s_{jA}\le16\mu(A)/r_j^2,\qquad
               \sum_{j,A}s_{jA}t_B^2\le16 W.                           \tag{3}
\]
Indeed, \(B\subset B(w,8r_j)\) for \(w\in A\).
At one scale at most 25 such dilated squares contain a given point, and a square containing \(z,v\) requires \(r_j\ge |z-v|/(5\sqrt2)\).
Using \(s_{jA}/t_B\le16/r_j^2\) gives
\[
 \sum_{j,A}\frac{s_{jA}}{t_B}h_B^2
 \le 16\int_{z\ne v}|z-v|^2
        \sum_{j,A:\ z,v\in5A} r_j^{-2}\,d\nu_\xi(z,v)
 \le C_0\|\xi\|_2^2.                                                     \tag{4}
\]
The geometric sum in (4) costs at most an absolute constant times \(|z-v|^{-2}\).
Combining (2)--(4) by Cauchy--Schwarz gives
\[
          \sum_{j,A}|Q_{q_{jA}}(u)|
                 \le C_1(\sqrt W\|\xi\|_2+W).
\]
The kernels are pointwise nonnegative and sum to \(g\) almost everywhere.
The gap times \(g\) belongs to \(L^2(\mu^2)\) by conditional Jensen, \(|z-v|\kappa\le2\), and the [finite total curvature of an actual marginal](Yin_C_F0255_v1.md#statement).
Hence the partial sums times either oriented gap converge in \(L^2(\mu^2)\) by domination.
These gap tensors are exactly the generator values of the weighted liberation, which vanishes on omitted generators.
The outer Leibniz formula and differentiated binomial series therefore identify the sum with \(Q_g(u)\) as a gap-tensor evaluation.
Applying the [signed mixed-energy and domain argument](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) gives the asserted bounds and domains, since its real-component squared norm obeys \(V^2\le2\|\xi\|_2 V+|Q_g(u)|/2\).

### A marginal whose curvature quadratic form has both signs at unbounded scale

We first construct a bounded planar density \(\sigma\) of compact support for which the curvature kernel has a negative direction.
For \(0<d<1/10\) take the three rectangles in Cartesian coordinates
\[
  A=[1,2]\times[-d,d],\qquad B=[-d,d]\times[1,2],\qquad
  C=[-d,d]^2 .
\]
On them put normalized area probabilities \(\sigma_A,\sigma_B,\sigma_C\).
Set \(\sigma=\varepsilon\sigma_A+\varepsilon\sigma_B+(1-2\varepsilon)\sigma_C\) and \(f=1_A-1_B\).
Write the quadratic form \(\iint g_\sigma(z,v)f(z)f(v)d\sigma(z)d\sigma(v)\) divided by \(\varepsilon^2\) as an integral over the third point of the endpoint pair measure \((\sigma_A-\sigma_B)^{\otimes2}\) against \(\kappa^2\).
For the term with third point in \(C\), let \(d\to0\) by parametrizing each rectangle by a fixed uniform square.
With probability one the limiting endpoints on the same segment are distinct and collinear with zero, while mixed endpoints on the two axes make a nondegenerate triangle with zero.
The diameter is at least \(1-2d\) throughout, so domination gives a strictly negative limit for this term.
Fix \(d>0\) giving a strictly negative value.
The other two third-point terms are finite for this fixed \(d\).
Indeed for each of the three area probabilities every ball of radius \(r\le1\) has mass at most \(C_d r^2\), and for three independent points the diameter has lower-tail probability \(O_d(r^4)\) by conditioning on one point.
This makes the inverse squared diameter integrable.
Choosing \(\varepsilon>0\) small now gives a strictly negative quadratic form.
The constant function has a strictly positive quadratic form because a triple of independent draws is noncollinear almost surely.

Place a translated and scaled copy of \(\sigma\) at each center \(2^{-n}\), using scale \(R_n=2^{-4n-4}\) and mass \(t_n=7\,2^{-3n}\) for \(n\ge1\).
The cluster supports \(K_n=2^{-n}+R_n\operatorname{supp}\sigma\) have \(d_{nm}=\operatorname{dist}(K_n,K_m)\ge2^{-\min(n,m)}/4\).
Consequently \(J=\sup_n\sum_{m\ne n}t_m/d_{nm}^2<\infty\).
For \(z\in K_n\), the other clusters contribute at most \(Jr^2\) to \(\mu(B(z,r))\), while its own contributes at most \(C_d t_n\min(1,r^2/R_n^2)\).
Summing the squares divided by \(r_j^2\) at radii \(8r_j\), with the own-cluster terms split at \(8r_j=R_n\), gives \(O_d(1+t_n^2/R_n^2)\).
Thus \(W<\infty\) since \(\sum_n t_n^3/R_n^2<\infty\).
In particular the maximal linear density is square-integrable by dyadic comparison, and the total squared curvature is finite by (3) and Tonelli.
The [geometric characterization](Yin_C_F0255_v1.md#statement) gives an actual scalar vacuum.

Split \(g\) into the contributions of triples lying entirely within one cluster and a remainder.
For endpoints in \(K_n^2\), the remainder is at most \(4J\) by the diameter bound.
For endpoints in \(K_n,K_l\), \(l\ne n\), the integral over third points outside \(K_n\) is at most \(4J\), and third points in \(K_n\) add at most \(4t_n/d_{ln}^2\le4J\).
Thus the remainder is a bounded integral operator.
The same-cluster part on \(K_n^2\) is exactly \(t_n/R_n^2\) times the rescaled \(g_\sigma\).
Transport each of the two template test functions, normalized in \(L^2(\sigma)\), to \(K_n\) and multiply by \(t_n^{-1/2}\), extending by zero.
These are bounded unit vectors and the resulting quadratic forms equal \(t_n^2/R_n^2\) times their respective nonzero fixed forms, up to a bounded error.
This proves divergence with both signs.
Any decomposition from (1) of [the positive block theorem](Yin_C_F0292_v1.md#statement) has a Hilbert--Schmidt remainder and a positive-semidefinite sum on bounded inputs.
Indeed \(g\) and the absolute remainder are integrable, so dominated convergence passes positivity of the finite block forms to bounded tests.
Such a decomposition would bound the form below, contradicting the negative tests.

The sufficient condition (1) does not follow from scalar actuality: a uniform interval has an actual scalar conjugate variable by the geometric criterion, while \(\mu(B(z,r))/r\) stays positive at every interior point for small radii.
Its curvature is zero, so no diameter-shell estimate of the kernel is needed on that law.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:29 |
| status | open |
| reason | Fix the localized energy estimate, its sum over triangle diameters and the signed curvature-operator obstruction for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both original domains and quantitative bounds under the averaged square density, and failure of global positive-block decomposition on an actual law. |
| argument | [Argument](#argument) | Supported-kernel recurrence, localized vacuum sum, graph passage and explicit amplification of the two template signs. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#statement) | Squared-gap spectral identity and the actual partial liberation. |
| dependency | [Finite-kernel energy and marginal adjoint](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Equations (B0c) and (B0e) on analytic unitaries and measurable finite tensors, including the symmetric vacuum formula from (S1). |
| dependency | [Marginal criterion](Yin_C_F0255_v1.md#statement) | Diffuseness and total curvature under actuality, and sufficiency of finite geometric energy for the scalar example. |
| dependency | [Signed curvature and both original domains](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Limiting curvature energy, both oriented core bounds and original commutator passage; its positive block condition is tested in the example. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:36 |
| status | proved |
| reason | Independent review verified the localized recurrence, the sum over triangle diameters, both domains and the two-sided curvature example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both original domains and quantitative bounds under the averaged square density, and failure of global positive-block decomposition on an actual law. |
| argument | [Argument](#argument) | Supported-kernel recurrence, localized vacuum sum, graph passage and explicit amplification of the two template signs. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#statement) | Squared-gap spectral identity and the actual partial liberation. |
| dependency | [Finite-kernel energy and marginal adjoint](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Equations (B0c) and (B0e) on analytic unitaries and measurable finite tensors, including the symmetric vacuum formula from (S1). |
| dependency | [Marginal criterion](Yin_C_F0255_v1.md#statement) | Diffuseness and total curvature under actuality, and sufficiency of finite geometric energy for the scalar example. |
| dependency | [Signed curvature and both original domains](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Limiting curvature energy, both oriented core bounds and original commutator passage; its positive block condition is tested in the example. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0305_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
