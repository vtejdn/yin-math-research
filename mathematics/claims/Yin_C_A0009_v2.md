---
author: Yin
---
# Cyclic spectral inertia bounds for three-term kernels

Date: 2026-11-12 (Asia/Hong_Kong).
This route-four investigation seeks an independent rank bound after the [ordered-quotient and normality screens](../ledger/Yin_L_A0021_v1.md) have no applicable premise.
It uses the actual Haar spectral measure of a single infinite-order relative group element and a finite-trace isotropic-subspace argument.
It supplies a coefficient-dependent upper bound on a possible kernel, not its vanishing or an integer-rank theorem.
No historical priority is asserted.

## Statement

Let \(G\) be a discrete group, let \(g_0,g_1,g_2\) be distinct elements such that every \(g_i^{-1}g_j\), \(i\ne j\), has infinite order, and let \(\alpha_0,\alpha_1,\alpha_2\) be nonzero complex numbers.
Every torsion-free group with three distinct labels satisfies this relative-order hypothesis.
Use the actual left regular representation and its canonical trace, and put
\[
T=\alpha_0g_0+\alpha_1g_1+\alpha_2g_2,\qquad
a_i=|\alpha_i|,\qquad \delta=\dim_G\ker T.
\tag{1}
\]
If the three positive lengths \(a_i\) do not form a strict triangle, then \(\delta=0\).
If they form a strict triangle with opposite angles \(\theta_0,\theta_1,\theta_2\), then
\[
\boxed{\delta\le\frac{\min_i\theta_i}{\pi}\le\frac13.}
\tag{2}
\]
Thus an equal-modulus three-term element has analytic rank at least \(2/3\), without a group Atiyah or orderability premise.
The conclusion does not assert that the interval \(0<\delta\le1/3\) is realized by any torsion-free group.
It leaves that interval unresolved.

There is also a matrix version with its own narrower coefficient hypothesis.
Let \(M\) be a finite von Neumann algebra with a faithful normal finite trace \(\tau\), where \(0<\tau(1)=d<\infty\).
Let \(U_0,U_1,U_2\in M\) be unitaries for which each relative unitary \(U_i^*U_j\) has Haar spectral measure under \(\tau/d\).
For \(T=\sum\alpha_iU_i\), the same argument gives
\[
\tau(P_{\ker T})\le d\,\frac{\min_i\theta_i}{\pi}
\tag{3}
\]
in the strict-triangle case and zero otherwise.
In particular (3) applies to \(U_i=C_i\otimes g_i\) with constant unitary \(C_i\in M_d(\mathbb C)\), using the unnormalized matrix trace and the same relative-order condition.
It does not apply to arbitrary three-term matrix coefficients or arbitrary rows containing three monomials.

## Argument

### Finite-trace isotropic dimension

Let \(B=B^*\in M\) be bounded, with spectral projections \(e_+,e_-,e_0\) for the positive, negative and zero parts.
Suppose \(e_0=0\), and let \(p\) be a projection satisfying
\[
pBp=0.
\tag{4}
\]
The bounded map \(e_+p:p\mathcal H\to e_+\mathcal H\) is injective.
Indeed, if \(e_+\xi=0\) for \(\xi=p\xi\), then \(\xi=e_-\xi\).
Equation (4) gives \(\langle B\xi,\xi\rangle=0\), whereas strict negativity of \(B\) on its negative spectral subspace gives \(\xi=0\).
This last implication does not require a spectral gap: the integral of the strictly positive function \(-t\) against the spectral measure of a nonzero vector in \(e_-\mathcal H\) is strictly positive.
The polar decomposition of \(e_+p\) therefore has initial projection \(p\) and final projection at most \(e_+\).
Finite-trace equivalence of these projections proves \(\tau(p)\le\tau(e_+)\).
Applying the same argument to \(-B\) gives
\[
\boxed{\tau(p)\le\min\{\tau(e_+),\tau(e_-)\}.}
\tag{5}
\]
If \(B\) is instead positive or negative with zero kernel, (4) directly forces \(p=0\).
All maps in this argument are bounded; there is no unbounded inverse or pointwise domain claim.

### The exact compression imposed by a three-term kernel

Let \(p=P_{\ker T}\), first in the abstract unitary setting of (3).
Fix a permutation \((i,j,k)\) of \((0,1,2)\).
The equation \(Tp=0\) gives
\[
(\alpha_iU_i+\alpha_jU_j)p=-\alpha_kU_kp.
\]
Taking the product with its adjoint in the prescribed order gives
\[
p\left(a_i^2+a_j^2+
       2\operatorname{Re}(\overline{\alpha_i}\alpha_j U_i^*U_j)
  \right)p=a_k^2p.
\tag{6}
\]
Write
\[
e^{i\varphi_{ij}}=\frac{\overline{\alpha_i}\alpha_j}{a_ia_j},
\qquad
X_{ij}=\operatorname{Re}(e^{i\varphi_{ij}}U_i^*U_j),
\qquad
\kappa_k=\frac{a_k^2-a_i^2-a_j^2}{2a_ia_j}.
\]
Then (6) is exactly
\[
p(X_{ij}-\kappa_k)p=0.
\tag{7}
\]
No commutation of \(p\) with any unitary or spectral projection has been used.

The Haar hypothesis makes \(X_{ij}\) have the distribution of \(\cos t\) for uniform \(t\in[0,2\pi)\), with total trace mass \(d\).
It has no atom at any real number.
For \(-1<\kappa<1\),
\[
\tau(1_{(\kappa,\infty)}(X_{ij}))=\frac d\pi\arccos\kappa,
\qquad
\tau(1_{(-\infty,\kappa)}(X_{ij}))
=d\left(1-\frac1\pi\arccos\kappa\right).
\tag{8}
\]
Apply (5) to \(B=X_{ij}-\kappa_k\).
For the strict triangle, the ordinary cosine law gives
\[
\kappa_k=-\cos\theta_k,\qquad
\arccos\kappa_k=\pi-\theta_k.
\]
Consequently
\[
\tau(p)\le d\min\{\theta_k/\pi,1-\theta_k/\pi\}
\quad\text{for every }k.
\tag{9}
\]
Choose \(k\) with smallest angle.
Since the three angles sum to \(\pi\), this angle is at most \(\pi/3\), so (9) gives (3) and its upper bound \(d/3\).

If a strict triangle fails, choose \(k\) with largest length \(a_k\ge a_i+a_j\).
Then \(\kappa_k\ge1\), and \(X_{ij}-\kappa_k\) is nonpositive and injective, including the equality case because the Haar distribution has no atom at \(1\).
Equation (7) therefore gives \(p=0\).
This also verifies the coefficient-dominance boundary, rather than discarding equality.

### Actual regular groups and the matrix specialization

For an infinite-order \(h\in G\), the left action of \(h\) on every right coset of \(\langle h\rangle\) is the bilateral shift.
Its canonical spectral measure is Haar on the circle, either by the cyclic Fourier transform or by \(\tau_G(h^m)=0\) for every nonzero integer \(m\).
This is the [actual cyclic representation input](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), not a general assertion about arbitrary infinite-order unitaries.
Multiplying by a scalar phase preserves that Haar law.
Taking \(U_i=g_i\) and \(d=1\) in (3) proves (1)--(2) in the actual regular representation.

For the stated constant-unitary matrix specialization, \(U_i^*U_j=(C_i^*C_j)\otimes(g_i^{-1}g_j)\).
Its nonzero integer moments under the normalized matrix trace vanish, because the group factor has zero trace.
Trigonometric-polynomial approximation therefore identifies its spectral measure with Haar.
Its total unnormalized trace is \(d\), exactly as required for (3).
Arbitrary matrix-valued coefficients need not be scalar multiples of unitaries and do not satisfy (6); no general three-term-row induction follows from this specialization.

Coincident group labels or zero coefficients are excluded from the strict statement but cause no missing endpoint for scalar inputs.
Combine coincident labels and delete zero coefficients first.
A resulting nonzero one- or two-term group-ring element in a torsion-free group is injective by the monomial or cyclic-binomial argument.
A resulting zero element has kernel dimension one and is outside the nonzero hypothesis.

## Consequences for the retained Schur problems

For \(T=1+u-v\) with \(e,u,v\) distinct in a torsion-free group, (2) gives
\[
\dim_G\ker T\le\frac13.
\tag{10}
\]
The coincident-label cases in [L_A0021](../ledger/Yin_L_A0021_v1.md#actual-setting-and-fixed-inputs) are already injective.
Under the separate original-Schur admissibility conditions \(u\ne e\) and \(uv\ne e\), the [power-column identity](../ledger/Yin_L_A0020_v1.md#exact-inclusion-of-an-equal-modulus-trinomial-problem) uses independently invertible cyclic factors and gives
\[
\dim_G\ker r=\dim_G\ker T\le\frac13,
\qquad
\operatorname{rank}_G
\begin{pmatrix}1-uv&1-u\\1-(uv)^2&1-u^3\end{pmatrix}
\ge\frac53.
\tag{11}
\]
The displayed matrix is exactly the original L_A0020 matrix under \(h=u,f=uv,g=u^3,k=(uv)^2\), retaining the order of the square of \(uv\).
Its known lower-right cyclic pivot gives rank \(2-\dim_G\ker T\), as used in (11).
The condition \(uv=e\) remains excluded from that transfer, since its original Schur value vanishes.

For the [complex-phase numerator](../ledger/Yin_L_A0007_v1.md#exact-screening-in-the-concrete-free-group-example)
\[
s=(1+i)-ig-h
\]
with distinct \(e,g,h\), the coefficient lengths are \((\sqrt2,1,1)\), with triangle angles \((\pi/2,\pi/4,\pi/4)\).
Thus
\[
\dim_G\ker s\le\frac14,\qquad
\operatorname{rank}_G s\ge\frac34.
\tag{12}
\]
This improves the retained independent one-half rank bound even when no supporting-subgroup character or ordered quotient has been established.
If \(g=h\ne e\), then \(s=(1+i)(1-g)\) is already a cyclic unit.
For \(g,h\ne e\), the exact reciprocal-ratio identity in that input has
\[
r=(1-g)^{-1}(1-h)+(1-h)^{-1}(1-g),\qquad
\dim_G\ker r=2\dim_G\ker s,
\]
so the new bound implies \(\dim_G\ker r\le1/2\), with every original denominator certified before that use.
It does not imply that this remaining rational kernel vanishes.

For the [normal finite-star family](../claims/Yin_C_A0008_v1.md#statement), the same equal-modulus bound applies to \(c=1+u+v\).
All its coincidence cases were independently settled in that claim.
At zero potential its complete eighteen-square matrix therefore satisfies
\[
1\le\dim_G\ker\mathcal H_0
=1+\dim_H\ker c\le\frac43.
\tag{13}
\]
The nonzero-potential nullity remains exactly one by the independent theorem already proved there.
Equation (13) is a quantitative improvement on the unresolved correction, not an arithmetic restriction sufficient to make that correction zero.

## Scope and next question

The entire bound is derived from bounded compression, polar-decomposition dimension comparison and the canonical cyclic spectral measure.
The triangle cosine law is an elementary coefficient identity.
The local comparison did not find this coefficient-angle bound in the retained A-line claims or ledgers; that bounded comparison supports no historical novelty claim.
An exploratory external search supplied no adopted additional theorem, and no literature-wide absence or open-status conclusion is inferred.

Only pairwise relative Haar laws enter (6)--(9).
Thus this estimate does not exploit the full joint regular group law, whose importance is retained in [C_A0006](../claims/Yin_C_A0006_v1.md#source-scope-and-remaining-question).
It excludes a substantial interval of possible fractional ranks, but does not exclude every noninteger rank between zero and one.
A continuation would have to derive additional compatible constraints from repeated group multiplication or produce independently invertible kernel-preserving transformations for which these angle bounds shrink to zero.
No such transformation or shrinking sequence has been constructed here.
The missing shrinking transformation remains a separate obligation, rather than a premise of the proved bound.

## Assessment history

### Decision reviewed-cyclic-inertia

| Field | Value |
| --- | --- |
| date | 2026-11-11T17:54 |
| status | proved |
| reason | Independent whole-artifact review supports the cyclic spectral inertia bound, all coefficient and trace endpoints, and its exact original-Schur, complex-phase and finite-star applications under the clarified finite von Neumann hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar relative-order theorem and the exact pairwise-Haar finite von Neumann and constant-unitary matrix specializations. |
| argument | [Argument](#argument) | Complete bounded isotropic-dimension proof, Haar tail calculation, triangle boundaries, degeneracies and formulas (1)--(13) including all applications and limitations. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0028_v1.md#whole-artifact-finding) | Complete v2 artifact, initial abstract-setting precision finding and actual v2 recheck, with exact dependency and source scopes. |

## Current assessment

[Selected decision](#decision-reviewed-cyclic-inertia)

