---
author: Yin
---
# A vacuum-weighted phase criterion for normal coordinates and a factor with no uniform phase gap

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace and [actual ACSY](../tasks/Yin_T_F0011_v1.md#contract).
Use \(H=L^2(M,\tau)\) with inner products linear in the second variable, fix \(i\), and suppose the omitted algebra \(N=W^*(X_j:j\ne i)\) is abelian.
This includes every normal pair.
Write \(\delta=\delta_i\) for the unique normal coordinate derivation on the represented starred polynomial core \(\mathcal P\), \(\xi=\delta^*(1\otimes1)\), and \(Ep=(\mathrm{id}\otimes\tau)\bar\delta p\).
Let \(\mathcal D_b\) consist of the bounded \(p\in\operatorname{Dom}\bar\delta\) with uniformly operator-bounded core approximants converging strongly-star to \(p\) and in the Hilbert graph of \(\bar\delta\).

Set \(x=X_i-\mathbb E_N X_i\), let \(H_{\pm}=\overline{\operatorname{span}(NxN+Nx^*N)}^{\,2}\), let \(P_{x,x^*}\) project onto \(H_{\pm}\), and put \(P_{\pm}=\mathbb E_N+P_{x,x^*}\) on \(H\).
These two ranges are orthogonal.
Let \(\eta_1=P_{x,x^*}\xi,\ \eta_2=P_{x,x^*}\xi^*\).
Write \(A=N\bar\otimes N^{\rm op}\subset\mathcal B=M\bar\otimes M^{\rm op}\) with product traces, use \(\mathbb E_A:\mathcal B\to A\) for the trace-preserving conditional expectation, and use the Hilbert unitary \(\Phi(a\otimes b)=a\otimes b^{\rm op}\) from the coarse Hilbert space to \(L^2(\mathcal B)\).
The marginal phase \(k=\Phi(\bar\delta x^*)\) is unitary.
Put \(t=\mathbb E_A(k)\), \(D=1-t^*t\), and use \(\pi\) for the normal representation of \(A\) on the joint cyclic space of \(\eta_1,\eta_2\) extending the action \((a\otimes b^{\rm op})y=ayb\).
Existence of this representation on that space is part of the [joint-span argument](Yin_C_F0223_v1.md#argument).

1. The vector \(\theta=\eta_1-\pi(t^*)\eta_2\) has zero component in \(\ker\pi(D)\).
   If
   \[
                      v=\pi(D)^{-1/2}\theta\ \in H,                       \tag{W1}
   \]
   with inverse on the support, every finite column in \(\mathcal D_b\) satisfies
   \[
      \left(\sum_j\|P_{\pm}Ep_j\|_2^2\right)^{1/2}
        \le \big(\|\xi\|_2+\|\eta_2\|_2+\|v\|_2\big)
                         \left\|\sum_j p_j^*p_j\right\|^{1/2}.
   \]
   This includes all original starred polynomials.
2. There is a normal generating pair \((Z,Y)\) in a tracial factor with actual ACSY and strong duals for **both** coordinates, with the full bounded-vector operator and adjoint domains.
   For the distinguished \(Y\), its marginal is not supported on a line, condition (W1) holds, \(D>0\) almost everywhere, and \(\|t\|=1\).
   Specifically, let \(Z=z\) on the unit disk with probability measure \(d\mu(z)=(3/\pi)|z|^4\,dA(z)\) for plane area \(dA\), \(h=|Z|^{5/4}\), \(S\) a standard semicircular element free from \(W^*(Z)\), and \(T=hSh\).
   Take \(Y=T+\mathrm i\lambda T^2\) for any \(0<2\lambda\|T\|<1\).
   For \(A=L^\infty(\mu\otimes\mu)\) the phase defect satisfies the two-sided estimate (W2) below, and the target \(Y\)-vacuum satisfies \(h^{-1}\xi_Y,\xi_Yh^{-1}\in L^2\).

## Argument

### The joint vacuum pairing with a singular phase weight

Let \(y=qx+rx^*\) with \(q,r\in N\odot N^{\rm op}\) and use the product trace \(\tau_A\).
The [joint-span pairing and polar argument](Yin_C_F0223_v1.md#argument) gives the normal representation \(\pi\) on the projected vacuum cyclic space independently of the gap.
Its two endpoint identities, with \(V_p=\mathbb E_A((p\otimes1)k)\) and \(U_p=\mathbb E_A(p\otimes1)\), are
\[
 \langle y,p\xi^*-Ep\rangle=\tau_A(q^*V_p+r^*U_p),\qquad
 \langle y,\pi(a)\eta_1+\pi(b')\eta_2\rangle
 =\tau_A\big(q^*(a+tb')+r^*(t^*a+b')\big)
 \quad(a,b'\in A).
\]
Here \(y\) ranges over a dense subspace of \(H_{\pm}\) and the pairings hold for every \(p\in\mathcal D_b\).
Taking \(a=s,b'=-st^*\) in the second identity and using commutativity gives for every \(s\in A\)
\[
          \langle y,\pi(s)\theta\rangle=\tau_A(q^*Ds).
\]
In particular, setting \(s=1_{\{0\}}(D)\) and using density gives the assertion about the kernel.
Put \(k_0=k-t\) and \(C_p=\mathbb E_A((p\otimes1)k_0)=V_p-U_pt\).
For a finite column, conditional Schwarz gives
\[
    \sum_j C_{p_j}^* C_{p_j}
      \le \mathbb E_A\!\left(k_0^*((\textstyle\sum_j p_j^*p_j)\otimes1)k_0\right)
      \le\left\|\sum_j p_j^*p_j\right\| D ,
\]
since \(\mathbb E_A(k_0^*k_0)=1-t^*t\).
The \(a_p=C_pD^{-1/2}\), taken zero on the kernel, thus belong to \(A\) and satisfy the same column estimate with the unit in place of \(D\).
For \(e_n=1_{[1/n,1]}(D)\), test \(\pi(a_p D^{-1/2}e_n)\theta\) against \(y\) by the preceding pairing.
The vectors converge in \(H\) to \(\pi(a_p)v\) by (W1), and the traces tend to \(\tau_A(q^*C_p)\) since \(C_p\) vanishes on the kernel.
The pairing of \(\pi(U_p)\eta_2\) against \(y\) is \(\tau_A(q^*tU_p+r^*U_p)\).
Commutativity of \(A\) gives \(tU_p=U_pt\), hence
\[
       P_{x,x^*}(p\xi^*-Ep)=\pi(U_p)\eta_2+\pi(a_p)v .
\]
The finite columns of \(U_p\) are contractive by conditional Schwarz.
This identity and the projection onto \(L^2(N)\) from [C_F0217](Yin_C_F0217_v1.md#statement) give the claimed estimate by the Hilbert direct-sum triangle inequality.
For a nonabelian omitted algebra the endpoint system instead contains \(V_p-tU_p=C_p+[U_p,t]\), with defects \(1-tt^*\) and \(1-t^*t\) on different sides.
The present calculation uses the equality of the two products in \(A\).

### A correlated example with an unbounded inverse phase weight

Take the abelian disk law \(d\mu(z)=(3/\pi)|z|^4\,1_{\{|z|\le1\}}\,dA(z)\) for \(Z\) in [C_F0140](Yin_C_F0140_v1.md#statement).
Put \(N=W^*(Z)\), \(h=|Z|^{5/4}\), \(b=h^{-1}\), let \(S\) be a standard semicircular free from \(N\), and set \(T=hSh\).
The function defining \(h\) is \(C^1\) on the plane and \(b\in L^4(N)\) since the fourth-moment integral is \(6\int_0^1 r^{5-5}\,dr\).
The [free congruence theorem](Yin_C_F0140_v1.md#statement) gives actual ACSY and both full domains for \((Z,T)\), with \(T\)-vacuum \(\xi_T=bSb\).
For \(R=\|T\|>0\) and \(0<2\lambda R<1\), put \(Y=T+\mathrm i\lambda T^2\).
The two tuples generate the same von Neumann algebra and even the same represented starred core, since \(T=(Y+Y^*)/2\).

Passage to this parabolic coordinate preserves the strong condition even though the omitted coordinate \(Z\) is normal with disk spectrum.
Use the normalized canonical operator-first duals at \((Z,T)\), whose restrictions and actual adjoint restrictions on \(M\) are operator-norm-to-Hilbert bounded by the full canonical domains and the closed graph theorem.
The old \(Z\)-dual commutes with \(T\) and hence with \(Y\) on all bounded inputs.
For the old \(T\)-dual \(E_T\), insert the projective tensor
\[
       g=(1+\mathrm i\lambda(T\otimes1+1\otimes T))^{-1}
        =\sum_{m,n\ge0}d_{mn}T^m\otimes T^n
\]
in its commutator using the [projective correction and adjoint formula](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators).
The Neumann series converges projectively since \(2\lambda R<1\), with coefficients \(d_{mn}=(-\mathrm i\lambda)^{m+n}\binom{m+n}{m}\).
The corrected dual commutes with \(Z\), and its kernel at \(Y\) is the product of \(g\) and \(1+\mathrm i\lambda(T\otimes1+1\otimes T)\), hence gives the vacuum projection.
Both actual domains contain \(M\) by that same formula.
The resulting normal pair has actual ACSY by the [normal vacuum corollary](Yin_C_F0070_v1.md#statement), since the actual adjoint domains of both duals contain the unit.
Its generated algebra is a factor by [two-coordinate scalar commutant](Yin_C_F0202_v1.md#statement).
The spectral law of \(T\) is diffuse by [C_F0076](Yin_C_F0076_v1.md#statement).
Consequently the marginal of \(Y\) is not supported on a line, since a line meets the given parabola in at most two points.

The conditional expectation \(\mathbb E_N\) on functions of \(T\) gives probability laws \(\nu_z\) on \([-R,R]\), with \(\mathbb E_N(g(T))(z)=\int g\,d\nu_z\) for continuous \(g\).
For instance these laws are obtained by applying the positive unital map to a countable uniformly dense rational star subalgebra of \(C([-R,R])\), using positivity on squares and the norm bound off a common null set, then extending by continuity and applying Riesz representation.
They have mean zero and variance \(h(z)^2\tau(h^2)\), since \(\mathbb E_N S=0\) and \(\mathbb E_N(Sh^2S)=\tau(h^2)1\) by centered freeness.
For the distinguished \(Y\), division of \(\overline{Y(s)-Y(r)}\) by \(Y(s)-Y(r)\) gives \(F(s+r)=(1-\mathrm i\lambda(s+r))/(1+\mathrm i\lambda(s+r))\).
The diagonal has zero product marginal measure by diffuseness.
Continuous tensor approximation on the square, and the product expectation onto \(A\), therefore yield
\[
                t(z,w)=\iint F(s+r)\,d\nu_z(s)d\nu_w(r).
\]
For independent samples \(L,L'\) from the conditional sum law,
\[
  D(z,w)=1-|t(z,w)|^2=\tfrac12\mathbb E|F(L)-F(L')|^2
      \asymp_{\lambda,R} \tau(h^2)\big(h(z)^2+h(w)^2\big).              \tag{W2}
\]
Indeed \(|F(l)-F(l')|=2\lambda |l-l'|/(|1+\mathrm i\lambda l|\,|1+\mathrm i\lambda l'|)\) on \([-2R,2R]\), and the variance of the independent sum is the sum of the two variances.
Thus \(D>0\) almost everywhere, while it is arbitrarily small on positive product-measure sets near \((0,0)\).
In this factor \(\|t\|=1\) and \(D^{-1/2}\) is unbounded.

The vacuum condition (W1) nevertheless holds.
Compose the original \(T\)-derivation \(\delta_T\), killing \(N\) on its closed domain, with the outer-bimodule endomorphism
\[
   a\otimes c\longmapsto\sum_{m,n}d_{mn}\,aT^m\otimes T^n c .
\]
The projective norm bound makes this a bounded map on the coarse Hilbert space, and applying it to \(\delta_TY\) gives the unit tensor by the same divided-difference product.
The composite respects represented relations on the common core and agrees there with the unique normalized \(Y\)-derivation.
With inner products linear in the second variable its actual vacuum is the norm-convergent series
\[
     \xi_Y=\sum_{m,n\ge0}\bar d_{mn}\,\delta_T^*(T^m\otimes T^n).
\]
Indeed the vacuum pairing on each fixed polynomial gives this series termwise by tracial cyclicity and the projective convergence.
The tensor-adjoint product rule, obtained by expanding the vacuum pairing on \(T^m pT^n\), gives
\[
 \delta_T^*(T^m\otimes T^n)=T^m\xi_T T^n
    -\big((\mathrm{id}\otimes\tau)\delta_T T^m\big)T^n
    -T^m\big((\tau\otimes\mathrm{id})\delta_T T^n\big).
\]
Here \(\delta_T\) is real, since \(T\) is selfadjoint and the two omitted starred values vanish.
The two correction terms together have operator norm at most \((m+n)R^{m+n-1}\), interpreted as zero for \(m+n=0\), by the cut formula for \(T^m,T^n\).
The main term has Hilbert norm at most \(R^{m+n}\|\xi_T\|_2\).
These bounds are summable against \(|d_{mn}|\), proving the asserted adjoint and convergence.
Moreover \(b\xi_T=b^2Sb\) and \(\xi_T b=bSb^2\) are in \(L^2\).
For bounded spectral truncations of the powers of \(b\) this follows from \(\|aSc\|_2^2=\|a\|_2^2\|c\|_2^2\) for \(a,c\in N\), and truncation extends the identity and product to these \(L^2\) powers.
For \(m\ge1\) the bounded operator \(bT=Sh\) gives \(\|b T^m\xi_T T^n\|_2\le\|Sh\|R^{m+n-1}\|\xi_T\|_2\).
For \(m=0\) use \(\|b\xi_T\|_2R^n\), and right multiplication by \(b\) obeys the reverse estimate using \(Tb=hS\).
The two correction terms also remain summable in either weighted norm because their operator-norm bound can be multiplied by \(\|b\|_2\).
Closedness of left and right multiplication by the affiliated \(b\) consequently puts \(b\xi_Y,\xi_Y b\) in \(H\).
In particular \(b\xi_Y^*\in H\).
The joint cyclic projection commutes with the spectral projections of left \(b\), and its projected vacua \(\eta_1,\eta_2\) therefore belong to that left multiplication domain.
On their normal \(A\)-representation \(\pi(t^*)\) commutes with these same spectral projections since \(N\) is abelian.
Consequently \(b\theta\in H\).
By (W2), \(D^{-1}\le C(h^{-2}\otimes1)\) almost everywhere for a finite constant depending on this law, so spectral truncation proves (W1).

This proves the projected estimate for an actual gapless normal pair in a factor.
Condition (W1) is sufficient and its necessity or universal validity is not asserted.
The estimate concerns \(P_{\pm}E\).
Control of \((1-P_{\pm})E\) on arbitrary normal tuples remains an additional question.

## Provenance

The main agent proposed replacing the uniform phase gap by a vacuum-weighted estimate and testing whether the gap follows from a nonlinear marginal.
The check_defect agent developed the covariance estimate, factor example and weighted target-vacuum proof for Yin in the [normal endpoint investigation](../drafts/Yin_D_F0006.md#weighted-phase-and-a-gapless-normal-factor).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:32 |
| status | open |
| reason | The weighted projected estimate and its strict extension beyond the uniform gap in an explicit factor are fixed for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Abelian omitted algebra, weighted projected columns, and the normal factor satisfying the weight condition without a gap. |
| argument | [Argument](#argument) | Endpoint cancellation, covariance, spectral truncations, phase variance, actual dual transport and weighted vacuum bounds. |
| dependency | [Joint-span identities](Yin_C_F0223_v1.md#argument) | Normal action on the projected vacua and both endpoint pairings before inversion of the gap matrix. |
| dependency | [Omitted projection](Yin_C_F0217_v1.md#statement) | Projection of the right slice onto \(L^2(N)\) for bounded graph tests. |
| dependency | [Congruence class](Yin_C_F0140_v1.md#statement) | Normalized disk law, complete ACSY and strong domains for a regular congruence, and its actual \(T\)-vacuum. |
| dependency | [Projective correction](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Operator-first right multipliers, transported commutators and actual adjoint domains. |
| dependency | [Strong-to-vacuum implication](Yin_C_F0070_v1.md#statement) | Parts A and C give represented starred derivations and their actual vacua from the strong duals. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Diffuseness, uniqueness, marginal phase, and adjoint-reversed vacuum. |
| dependency | [Scalar commutant](Yin_C_F0202_v1.md#statement) | Factoriality for the two normal generators with actual ACSY. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:45 |
| status | proved |
| reason | Adopt the weighted phase criterion and gapless factor example after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Abelian omitted algebra, weighted projected columns, and the normal factor satisfying the weight condition without a gap. |
| argument | [Argument](#argument) | Endpoint cancellation, covariance, spectral truncations, phase variance, actual dual transport and weighted vacuum bounds. |
| dependency | [Joint-span identities](Yin_C_F0223_v1.md#argument) | Normal action on the projected vacua and both endpoint pairings before inversion of the gap matrix. |
| dependency | [Omitted projection](Yin_C_F0217_v1.md#statement) | Projection of the right slice onto \(L^2(N)\) for bounded graph tests. |
| dependency | [Congruence class](Yin_C_F0140_v1.md#statement) | Normalized disk law, complete ACSY and strong domains for a regular congruence, and its actual \(T\)-vacuum. |
| dependency | [Projective correction](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Operator-first right multipliers, transported commutators and actual adjoint domains. |
| dependency | [Strong-to-vacuum implication](Yin_C_F0070_v1.md#statement) | Parts A and C give represented starred derivations and their actual vacua from the strong duals. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Diffuseness, uniqueness, marginal phase, and adjoint-reversed vacuum. |
| dependency | [Scalar commutant](Yin_C_F0202_v1.md#statement) | Factoriality for the two normal generators with actual ACSY. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0237_v1.md#whole-proof-finding) | Singular phase truncation, actual pairs of domains, conditional phase variance and the weighted vacuum construction. |
