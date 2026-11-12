---
author: Yin
---
# Local alternatives after the global heat criterion fails

This revision records the 2026-11-12 continuation of [S_A0006](../strategies/Yin_S_A0006.md) under Yin's instruction to test the strength of the global coefficient bound before pursuing it further.
The [first version](Yin_L_A0031_v1.md) retains its Cauchy, inverse-gate, matching and gauge arguments unchanged.
The new [C14 v3](../claims/Yin_C_A0014_v3.md#statement) proves the global-filter obstruction, its positive-time-averaging extension and the exact finite-kernel correlation criterion.
The present material examines the local alternatives and records why several automatically available approximations still do not resolve the atom.
There is no concrete-example probing and no assertion that the known amenable Atiyah/domain equivalence is new progress.

Unless stated otherwise, \(G\) is finitely generated torsion-free amenable, \(A=\ell^1(G)\), \(0\ne a\in\mathbb CG\), \(H=a^*a\), \(p=1_{\{0\}}(H)\), and \(\alpha=\tau(p)<1\).
All group von Neumann traces are normalized in the scalar algebra.
The [BCM04 scalar-idempotent input](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace) and the separate [HK97/BCM04 reduced-C*-projection input](../audits/literature/BCM04/Yin_U001.md#assembly-trace) retain their established-source scope.

## What the global obstruction changes

[C14 v3](../claims/Yin_C_A0014_v3.md#global-filter-boundedness-on-invertible-inputs) shows that asking for bounded heat or Euler subsequences on every already-invertible group-ring input is exactly the quasi-Hermitian property.
The [SW20 interface](../audits/literature/SW20/Yin_U001.md#elementary-amenable-growth) shows that this fails throughout the torsion-free finitely generated elementary amenable exponential-growth class.
Thus the earlier global target asks for more than the absence of atoms.

The [positive-time-averaging obstruction](../claims/Yin_C_A0014_v3.md#positive-time-averaging-does-not-remove-a-negative-banach-spectral-point) also excludes a general cure by Cesaro or random positive heat times.
The obstruction applies to actual \(A\)-valued Bochner integrals.
It does not apply to a rational function merely because the same scalar function has a positive Laplace representation on the regular positive spectrum.
This distinction leaves a local resolvent possibility.

## Local actual Abel inverses

A sufficient atom-only condition is the existence of \(t_j\downarrow0\) such that
\[
H+t_j\in GL(A),\qquad
\sup_j\|t_j(H+t_j)^{-1}\|_A<\infty.
\tag{1}
\]
These are actual Banach-algebra inverses.
Their regular representations are the usual positive resolvents, which converge in \(L^2(\tau)\) to \(p\).
The [bounded-coefficient-mass criterion](../claims/Yin_C_A0014_v2.md#bounded-coefficient-mass-suffices-without-norm-convergence) therefore gives \(p=0\).
No operator-norm convergence or gap at zero is used.

This condition is local near zero in the Banach spectrum.
A fixed negative spectral point \(-c\), \(c>0\), contributes the scalar value \(t/(t-c)\), which tends to zero as \(t\downarrow0\), rather than the exponentially growing \(e^{ct}\).
It does not by itself obstruct (1).
For example as a general sufficient hypothesis, if \(H\in GL(A)\), then for \(0<t<(2\|H^{-1}\|_A)^{-1}\) the Neumann series gives
\[
\|t(H+t)^{-1}\|_A\le2t\|H^{-1}\|_A\longrightarrow0,
\]
without requiring all of \(\sigma_A(H)\) to be positive.
This is a conditional algebraic argument, not a search for an example.

For \(-c\in\sigma_A(H)\), \(0<t<c\), the formal expression
\[
\int_0^\infty t e^{-ts}e^{-sH}\,ds
\tag{2}
\]
cannot be an \(A\)-valued Bochner integral: the character used in C14 evaluates its integrand to \(t e^{(c-t)s}\).
An actual inverse at that parameter, if it exists, is not justified by (2).
The unresolved premise in (1) is precisely local invertibility and local norm control; neither follows here from the regular inverse or amenability.
This is an alternative sufficient condition, not a proved implication from the previous bounded-subsequence heat condition and not a universal reduction.

## Principal annihilators and local projection constants

Let
\[
K=\ker(L_a:A\to A).
\]
It is right-translation invariant and weak-star closed for \(A=c_0(G)^*\), because finite-support convolution is weak-star continuous.
If \(K\) is complemented as a Banach subspace of \(A\), then \(p=0\).

Indeed, let \(P:A\to K\) be a bounded projection and write \(R_gf(x)=f(xg)\).
Choose a left-invariant mean \(m\) on bounded functions of \(g\).
For \(f\in A\), \(\varphi\in c_0(G)\), define
\[
\langle Qf,\varphi\rangle
=m_g\langle R_gPR_g^{-1}f,\varphi\rangle.
\tag{3}
\]
The right side is a bounded functional on \(c_0(G)\), with norm at most \(\|P\|\|f\|_1\), so it defines \(Qf\in A\).
Each conjugate has range in \(K\) and fixes \(K\).
Weak-star closedness, or directly commuting the finite convolution equation with the mean, gives \(\operatorname{ran}Q\subset K\) and \(Q|_K=I\).
Left invariance gives \(R_hQR_h^{-1}=Q\).
Any bounded operator on \(\ell^1(G)\) commuting with right translations is left convolution by \(q=Q\delta_e\in A\); this follows first on the coordinate basis and then by \(\ell^1\) density.
Thus \(q^2=q\) and \(aq=0\).
The scalar-idempotent input forces \(q=0\), because \(q=1\) would imply \(a=0\).
Hence \(K=0\).
[Complete amenable kernel density](../claims/Yin_C_A0001_v2.md#rational-kernel-localization) then gives \(p=0\).

### Definition: local kernel projection constant

For finite \(F\subset G\), let \(K_F=\ker a\cap\mathbb C[F]\) and define
\[
\kappa_F=
\inf\{\|P\|_{\ell^1(F)\to\ell^1(F)}:
P^2=P,\ \operatorname{ran}P=K_F\}.
\tag{4}
\]
For \(K_F=0\), set \(\kappa_F=0\).
This is the usual relative Banach-space projection constant, here applied to the stated finite kernel and its inherited \(\ell^1\) norm.
Finite-dimensional linear algebra guarantees that the defining class is nonempty.
The value concerns arbitrary projections, not necessarily the orthogonal projection for the \(\ell^2\) inner product.

For every increasing finite exhaustion \(F_n\uparrow G\),
\[
\liminf_n\kappa_{F_n}<\infty\quad\Longleftrightarrow\quad p=0.
\tag{5}
\]
To prove the nontrivial implication, select a uniformly bounded subsequence of projections, extend each by zero on the complement of \(F_n\), and pass to a pointwise weak-star convergent subnet.
The existence of such a subnet follows by taking the product of the weak-star compact balls containing the image of each \(f\in A\); linearity and the common norm bound pass to the limit.
The resulting bounded map \(P:A\to K\) fixes every finite-support kernel vector, since such a vector eventually belongs to \(K_{F_n}\).
It is not necessary to assert that those vectors are \(\ell^1\)-dense in \(K\).

Apply the averaging construction (3) to this map.
The resulting convolution \(Q=L_q\) has \(aq=0\) and fixes each finite-support kernel vector, because all its right translates are also finite-support kernel vectors fixed by \(P\).
Convolution by \(q\in A\) is bounded on \(\ell^2(G)\).
Complete amenable \(\ell^2\) kernel density therefore gives
\[
qp=p,\qquad pq=q.
\]
Consequently \(q^2=qpq=pq=q\), and the scalar-idempotent theorem again gives \(p=0\).
The converse in (5) holds because every \(K_F\) is then zero.

Thus a hypothetical nonzero kernel forces \(\kappa_{F_n}\to\infty\) along every increasing exhaustion and forces \(K\) to be uncomplemented.
This is a precise geometric pathology.
It is not an independently established impossibility for principal annihilators.
No general estimate for \(\kappa_F\), or comparison with C14's averaged orthogonal correlation sums, is supplied here.

## Amenable averaging and operator-norm locality

Use the [finite propagation and uniform Roe conventions](../audits/literature/KU14/Yin_U001.md#uniform-roe-algebra).
An operator \(T\) has finite propagation when its matrix entries vanish outside \(xy^{-1}\in E\) for some finite \(E\subset G\).
The uniform Roe algebra \(C_u^*(G)\) is their operator-norm closure; their coefficients may depend on position.
The source's [ITAP definition and amenable interface](../audits/literature/KU14/Yin_U001.md#itap) place the following direct argument in its established terminology, without invoking its deeper tensor results.

For every \(T\in\mathcal N(G)\),
\[
\operatorname{dist}(T,C_r^*(G))
=\operatorname{dist}(T,C_u^*(G)).
\tag{6}
\]
To see this, average the right-translation conjugates of \(A\in B(\ell^2(G))\) using an invariant mean on their matrix coefficients, or equivalently on their bounded sesquilinear forms.
This defines a linear norm contraction \(\mathcal E:B(\ell^2(G))\to\mathcal N(G)\), fixing every \(T\in\mathcal N(G)\).
Right translation preserves the difference \(xy^{-1}\), so \(\mathcal E\) sends finite propagation to finite propagation.
A right-translation invariant finite-propagation operator is a group-ring convolution.
Thus
\[
\mathcal E(C_u^*(G))\subset C_r^*(G),\qquad
\|T-\mathcal E(A)\|\le\|T-A\|.
\]
This proves one distance inequality; the other follows from \(C_r^*(G)\subset C_u^*(G)\).

For a nontrivial scalar projection \(p\in\mathcal N(G)\), the [fixed distance calculation](Yin_L_A0031_v1.md#a-precise-norm-barrier) now gives
\[
\operatorname{dist}(p,C_u^*(G))=\frac12.
\tag{7}
\]
Consequently a single finite-propagation approximation with operator-norm error strictly below \(1/2\) would exclude the atom, even if its coefficients depend on position.
No such approximation follows from the known finite-support density.
The [exact kernel averages](../claims/Yin_C_A0014_v3.md#finite-window-kernel-correlation-criterion) instead have \(\|p-b_F\|=1\) whenever the kernel is nontrivial.
The norm-locality certificate is therefore another unresolved structural input, not a consequence of Hilbert density.

## Følner smoothing gives norm-small residuals but not norm-small projection defects

Let \(F_j\) be a left Følner sequence, and put
\[
\phi_F(g)=\frac{|F\cap gF|}{|F|},\qquad
r_F=M_{\phi_F}(p).
\tag{8}
\]
Here \(M_\phi\) is the Fourier multiplier with coefficient formula \(M_\phi(T)(g)=\phi(g)T(g)\).
The function \(\phi_F\) is positive definite, equals one at the identity, has finite support \(FF^{-1}\), and tends pointwise to one.
For completeness, realize it as
\(\phi_F(s)=\langle\pi(s)\xi,\xi\rangle\)
using the left regular representation and \(\xi=|F|^{-1/2}1_F\).
Set
\[
V\delta_x=\delta_x\otimes\pi(x^{-1})\xi.
\]
This is an isometry and gives the Schur multiplier formula
\(M_{\phi_F}(T)=V^*(T\otimes I)V\).
In particular it is unital and completely positive.

It follows directly that
\[
r_F\in\mathbb CG,\qquad
0\le r_F\le1,\qquad
\tau(r_F)=\alpha,\qquad
\|r_F-p\|_2\longrightarrow0.
\tag{9}
\]
The convergence also follows from the explicit coefficient sum
\[
\|r_F-p\|_2^2=\sum_g|1-\phi_F(g)|^2|p(g)|^2
\]
by dominated convergence.
These finite approximants depend on the unknown coefficients of \(p\); they are not the finite-kernel construction of C14 and are not a finite algorithm for the atom.

Writing \(H=\sum_sh_s\lambda_s\), one has the operator-norm bound
\[
\|Hr_F\|
\le\sum_s|h_s|\sqrt{2(1-\phi_F(s))}
\longrightarrow0.
\tag{10}
\]
Indeed,
\[
\|(\lambda_s\otimes I)V-V\lambda_s\|
=\|\xi-\pi(s^{-1})\xi\|
=\sqrt{2(1-\operatorname{Re}\phi_F(s))}.
\]
Expanding \(H\) bounds \(\|(H\otimes I)V-VH\|\) by the sum in (10).
Take adjoints, insert \(p\otimes I\), and use \(Hp=0\) to obtain (10).
Thus the residual is small in operator norm, not merely in trace.

Nevertheless, if \(0<\alpha<1\), then
\[
\tau(r_F-r_F^2)\longrightarrow0,\qquad
\|r_F-r_F^2\|=\frac14
\quad\text{for all sufficiently large }F_j.
\tag{11}
\]
The trace assertion follows from (9).
Let \(m_F,M_F\) be the minimum and maximum of the spectrum of the positive contraction \(r_F\).
The trace pairings
\(\tau(r_F(1-p))\to0\) and \(\tau((1-r_F)p)\to0\)
give \(m_F\to0\) and \(M_F\to1\), since respectively \(1-\alpha>0\) and \(\alpha>0\).
Every scalar self-adjoint element of \(C_r^*(G)\) has connected spectrum under the cited projectionless interface: a spectral disconnection would give a nontrivial continuous-functional-calculus projection.
Hence \(1/2\in\sigma(r_F)\) for all sufficiently large \(F_j\).
The function \(x(1-x)\) then proves the exact norm assertion in (11).

Thus finite support, positivity, exact preservation of the atom trace, norm-small kernel residual and tracial near-idempotency can all coexist with a persistent norm defect.
Amenability automatically supplies these properties under a hypothetical atom, so their achievement alone cannot exclude that atom.
Also, for any actual finite kernel witness \(ab=0\), one has
\[
e^{-tH}b=b,\qquad (1-H/\|H\|)^n b=b.
\]
Boundedness only on a chosen kernel vector or its generated right module is automatic and provides no replacement for a genuine projection or coefficient certificate.

## Remaining mathematical obligation

The universal global heat/Euler target has been rejected for a proved structural reason, not merely because an estimate was unavailable.
The local Abel condition, the finite-kernel correlation bound, local projection constants and operator-norm locality avoid that particular obstruction.
None is proved here from amenability and torsion-freeness alone.

Among the retained alternatives, C14's correlation sums are defined from finite matrices with their actual tied coefficients, and automatically vanish for every injective input.
They give a precise place where new control of group-word cancellations could enter.
However, their equivalence to zero kernel is expressly retained; the change of formulation is not itself a difficulty reduction or new group-class theorem.
The present evidence rules out global positive-time smoothing and several automatic Følner improvements as substitutes for the missing estimate.
