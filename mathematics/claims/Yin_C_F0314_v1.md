---
author: Yin
---

# The difference of the two curvature kernels on exchange-symmetric normal pairs

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z_0,Z_1\) be normal generators of a finite von Neumann algebra with a faithful normal probability trace, [full actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct), and a trace-preserving involution exchanging them.
Write \(\mu\) for the common spectral law, \(s=\|\xi_0\|_2=\|\xi_1\|_2>0\) for the common vacuum norm, and \(B_j=W^*(Z_j)\).
Let \(\gamma_j\) be the partial liberation derivation with value \(b\otimes1-1\otimes b\) on the marginal polynomials of coordinate \(j\) and zero on the other coordinate and its adjoint.
For the squared Menger curvature kernel set
\[
 g(z,v)=\int\kappa(z,w,v)^2\,d\mu(w),\qquad q^{(n)}=\min(g,n).
\]
Here \(\kappa\) is the reciprocal circumradius, zero on collinear or repeated triples.
Write \(q_j^{(n)}\) for the bounded tensor obtained by evaluating \(q^{(n)}\) on the two inner spectral legs of \(Z_j\).
For a bounded tensor of this type and sums of such tensors put
\[
 F_q^j(u)=\operatorname{Re}\langle u,C I_q\gamma_j(u)\rangle,\qquad C=\mathrm{id}\otimes\tau ,
\]
where \(I_{a\otimes b}(v\otimes w)=va\otimes bw\).
The test unitaries are \(u=h\pm i\sqrt{1-h^2}\) for all strict selfadjoint contractions \(h\) in the original represented starred polynomial algebra.
For every such \(u\) the scalar limit
\[
       D(u)=\lim_{n\to\infty} F^0_{q_0^{(n)}-q_1^{(n)}}(u)
                                                                        \tag{1}
\]
exists.
If \(F^j(u)=\lim_n F^j_{q_j^{(n)}}(u)\), then
\[
 \begin{split}
 F^0(u)+F^1(u)&=D(u)+H(u),\\
 H(u)&=\iint g(z,v)
 \left(1-\operatorname{Re}\big(\overline{\mathbb E_{B_1}u(z)}\,\mathbb E_{B_1}u(v)\big)\right)
                    d\mu(z)d\mu(v),\qquad 0\le H(u)\le4s^2 .
 \end{split}                                                           \tag{2}
\]
On exchange eigenvectors \(u\) the left side is \(2F^0(u)\).

Let \(d=\sup_u(-D(u))_+/s^2\), where \(a_+=\max(a,0)\).
Let \(k\) be the maximum, over both coordinates and the original and adjoint orientations, of the right slice cost on the whole original polynomial unit ball divided by \(s\).
In the extended nonnegative reals,
\[
                  k\le4+2\sqrt{4+d},\qquad d\le4(k+1)^2.                 \tag{3}
\]
Writing \(d_*=\sup d\) over these laws and using the [mixed output constant](Yin_C_F0311_v1.md#statement), one consequently has
\[
 K_{\rm mix}\le4+2\sqrt{4+d_*},\qquad
 d_*\le4\big(1+\sqrt{K_{\rm mix}^2+(1+\sqrt2)^2}\big)^2.               \tag{4}
\]
The universal normal implication \(\mathsf A\Rightarrow\mathsf S\) holds exactly when \(d_*<\infty\), and also exactly when each individual exchange-symmetric actual pair has finite \(d\).
Its failure gives a single such pair on which the normalized negative scalar forms in (1) are unbounded.

There is a freely independent exchange-symmetric pair with full strong duals and a fixed exchange-invariant strict polynomial test \(h\) for which both associated analytic unitaries satisfy
\[
 \left\|I_{q_0^{(n)}-q_1^{(n)}}\gamma_0\big(h\pm i\sqrt{1-h^2}\big)\right\|_2
                    \longrightarrow\infty.                             \tag{5}
\]
Thus (1) can converge on actual tests with divergent coarse norm in (5).
Whether the negative part of (1) is bounded in terms of \(s^2\) uniformly over all pairs and tests remains open.

## Argument

### Adding the two partial liberations

On the whole represented core \(\gamma_0+\gamma_1=\operatorname{ad}\), where \(\operatorname{ad}(x)=x\otimes1-1\otimes x\), by equality on all generators and the product rule.
All three derivations admit the same identity at the specified analytic tests by the binomial power series for the square root.
The norm bounds on its differentiated powers use \(\|\gamma_j(h^m)\|_2\le m\|h\|^{m-1}\|\gamma_jh\|_2\), with \(\|h\|<1\).
For a bounded marginal kernel \(q\) on \(B_1\) a direct pairing gives
\[
 \operatorname{Re}\langle u,CI_q\operatorname{ad}(u)\rangle
 =\iint q(z,v)\left(1-\operatorname{Re}(\overline{b(z)}b(v))\right)d\mu(z)d\mu(v)
\]
when \(q\) is real and \(b=\mathbb E_{B_1}u\).
Indeed the first coarse summand for a separated tensor \(a\otimes c\) gives \(\tau(a)\tau(c)\) before taking real parts, since \(u^*u=1\).
The second gives \(\tau(u^*a)\tau(cu)\).
Linearity and normality of the inner marginal representation extend this computation to bounded measurable kernels.
As \(|b|\le1\), the parenthesized factor lies between zero and two.
Adding and subtracting \(F^0_{q_1^{(n)}}(u)\) now proves (2) at every finite cutoff.

The [scalar curvature weight](Yin_C_F0267_v1.md#statement) has integral \(\|\mathbb E_{B_1}\xi_1\|_2^2\), and contains the nonnegative summand \(\tfrac12\int g(z,v)d\mu(v)\).
It follows that \(\iint g\,d\mu^2\le2s^2\), giving convergence of the inner term and its bound in (2).
For the matched forms, \(|z-v|\kappa(z,w,v)\le2\) and conditional Jensen give \(\int |z-v|^2g^2\,d\mu^2\le4\iiint\kappa^2d\mu^3<\infty\).
Consequently \((z-v)q^{(n)}\to(z-v)g\) in \(L^2(\mu^2)\), also for the conjugate difference.
These are exactly the two nonzero generator tensors of \(I_{q_j^{(n)}}\gamma_j\).
Finite Leibniz expansions pass their convergence to \(h\), and the differentiated binomial series gives convergence on \(u\), as in the [signed curvature limit](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries).
Subtracting the convergent inner term from the two matched scalar limits gives (1).
Exchange intertwines the matched derivations and sends \(q_0^{(n)}\) to \(q_1^{(n)}\), so \(F^1(u)=F^0(\sigma u)\) for the exchange \(\sigma\).
If \(\sigma u=\pm u\), this equals \(F^0(u)\).
The scalar cancellation itself holds on every test in (1).

### Quantitative control of the full cores

For each \(j\) let \(T_{jx},T_{jy}\) be the right slices of the two real parts \((\delta_j+\delta_j^\#)/2,(\delta_j-\delta_j^\#)/(2i)\), and let \(\zeta_{jx},\zeta_{jy}\) be their real vacua.
The reversed derivation is \(\delta_j^\# p=(\delta_j(p^*))^\dagger\), with flip-adjoint \(\dagger\).
Write \(V^2=\sum_{j=0,1}\sum_{a=x,y}\|T_{ja}u\|_2^2\).
The sum of the four squared vacuum norms is \(2s^2\).
Summing (19) and (20) of the [actual mixed-energy identity](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains), with the signed form in the convention of (2), gives the equality
\[
 V^2=2\operatorname{Re}\sum_{j,a}\langle T_{ja}u,u\zeta_{ja}\rangle
                         -\tfrac12\big(D(u)+H(u)\big).
                                                                        \tag{6}
\]
The energy calculation applies to actual normal tuples on this analytic core and uses the matched gap tensors at each coordinate.

If \(d<\infty\), Cauchy--Schwarz and \(H\ge0\) give \(V^2\le2\sqrt2\,s V+d s^2/2\).
The positive root yields \(V\le(\sqrt2+\sqrt{2+d/2})s\).
Each oriented slice on \(u\) is a sum or difference \(T_{jx}u\pm iT_{jy}u\) of norm at most \(\sqrt2 V\).
Both analytic signs are tested, and averaging the two unitaries bounds the same slices of \(h\).
Approximation by strict scalar dilations includes selfadjoint polynomial contractions of norm one.
Every polynomial contraction is the sum of its selfadjoint real part and \(i\) times its selfadjoint imaginary part, each of norm at most one.
The additional factor two gives the first inequality in (3).

Conversely, if \(k<\infty\), norm-convergent partial sums for \(u\) are core polynomials with operator norms tending to one, and their oriented derivative values converge by the product rule and the power series.
Every oriented slice at \(u\) therefore has norm at most \(ks\).
The parallelogram identity gives \(\|T_{jx}u\|_2^2+\|T_{jy}u\|_2^2\le k^2s^2\), so \(V\le\sqrt2 ks\).
Solving (6) for \(-D(u)\), Cauchy--Schwarz and \(H\le4s^2\) give
\[
                 -D(u)\le2V^2+4\sqrt2\,sV+4s^2\le4(k+1)^2s^2 .
\]
These finite-case implications include (3) in the extended reals.

Both the adjoint pair and the original pair are actual exchange-symmetric normal pairs, and the reversed vacuum is the adjoint of the original vacuum by the [normal reversal identity](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability).
Exchange identifies the two coordinate costs within either orientation.
Hence \(\sup k=K_{\rm ex}\) in the notation of the [exchange reduction](Yin_C_F0311_v1.md#statement).
Combining that reduction with (3) gives (4) and the universal criterion.
If the universal implication fails, the [single-pair assembly](Yin_C_F0313_v1.md#statement) gives an actual exchange-symmetric pair with infinite original slice cost.
For this pair (3) forces \(d=\infty\).
Conversely a pair with \(d=\infty\) forces \(d_*=\infty\), completing the individual-pair criterion.

### Divergent coarse norms on invariant analytic tests

Take two free copies of the [countable-circle scalar law](Yin_C_F0292_v1.md#a-law-with-divergent-curvature-compositions) with radii \(r_\ell=2^{-4\ell-4}\) and masses \(t_\ell=7\,2^{-3\ell}\) on normalized arclength, \(\ell\ge1\).
This compact law has an actual scalar vacuum and satisfies the separated-circle hypothesis of that result.
Free product gives a trace-preserving involution exchanging the copies and extends each marginal derivation and vacuum, by the [reduced-word vacuum computation](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
Thus the pair is actual and the separated-circle conclusion gives full strong duals at both coordinates.
For almost every two endpoints on circle \(\ell\), the third point on that circle gives \(g(z,v)\ge t_\ell/r_\ell^2\).
Consequently \(\int g^2d\mu^2\ge\sum_\ell t_\ell^4/r_\ell^4=\infty\).

Let \(b=\operatorname{Re}Z_0\), which has positive variance, and choose \(c>0\) so \(h=c(\operatorname{Re}Z_0+\operatorname{Re}Z_1)\) has norm less than one.
Then \(\gamma_0h=c(b\otimes1-1\otimes b)\).
For each \(n\) the squared norm of its insertion by the *other* marginal kernel is
\[
        \|I_{q_1^{(n)}}\gamma_0 h\|_2^2
                   =2c^2\operatorname{Var}(b)\,\|q^{(n)}\|_{L^2(\mu^2)}^2 .
\]
Indeed in the opposite tensor representation inner insertion is right multiplication.
Traciality pairs \((q_1^{(n)})^2\) with \(c^2(b\otimes1-1\otimes b^{\rm op})^2\).
Conditional expectation onto the two \(B_1\) legs sends \(b,b^2\) in each leg to their traces by freeness.
This leaves the constant \(2c^2(\tau(b^2)-\tau(b)^2)\).
The crossed norm diverges by monotone convergence, while the matched insertion on \(\gamma_0 h\) is uniformly bounded by the gap-weighted estimate above.
The triangle inequality gives divergence for their difference at \(h\).

For each finite \(n\), \(I_{q_0^{(n)}-q_1^{(n)}}\gamma_0\) is an outer derivation and the power series admits both \(u_+=h+i\sqrt{1-h^2}\) and \(u_-=u_+^{-1}\).
The inverse product rule relates their two values by a minus sign and two outer unitary multipliers, so the two Hilbert norms agree.
Since \(h=(u_++u_-)/2\), both norms dominate the diverging difference norm at \(h\).
Exchange fixes \(h\) and hence both unitaries, proving (5).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:55 |
| status | open |
| reason | Fix the scalar curvature difference criterion, the constants in both directions and the divergent coarse example for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar cancellation, dimensionless cost comparisons, the single-pair criterion, and divergent coarse norms on fixed invariant tests. |
| argument | [Argument](#argument) | Sum of partial liberations, actual mixed-energy equality, ordered tensor and scalar limits, both orientations, and the free two-circle-law-copy calculation. |
| dependency | [Actual mixed energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Equations (19) and (20) on strict polynomial analytic unitaries, with real vacua at both coordinates. |
| dependency | [Signed curvature limit](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Matched gap-tensor convergence, analytic graph evaluation and the sign of the curvature term. |
| dependency | [Curvature weight](Yin_C_F0267_v1.md#statement) | Integrability of the squared curvature with half the kernel integral bounded by the squared marginal vacuum norm. |
| dependency | [Normal reversal](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Reversed derivations and actual reversed vacua on the original starred core. |
| dependency | [Exchange comparison](Yin_C_F0311_v1.md#statement) | Bounds for the full exchange cost and the output orthogonal to the first marginal, and universal equivalence. |
| dependency | [Single-pair assembly](Yin_C_F0313_v1.md#statement) | A single exchange-symmetric actual pair with infinite forward cost when the universal implication fails. |
| dependency | [Countable-circle example](Yin_C_F0292_v1.md#a-law-with-divergent-curvature-compositions) | Actual vacuum, circle radii and masses, and separated-circle full domains. |
| dependency | [Free extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Preservation of the coordinate derivations and their actual scalar vacua under the free product. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:58 |
| status | proved |
| reason | Adopt the scalar curvature-difference criterion, both normalized bounds and the free-pair obstruction after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar cancellation, dimensionless cost comparisons, the single-pair criterion, and divergent coarse norms on fixed invariant tests. |
| argument | [Argument](#argument) | Sum of partial liberations, actual mixed-energy equality, ordered tensor and scalar limits, both orientations, and the free two-circle-law-copy calculation. |
| dependency | [Actual mixed energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Equations (19) and (20) on strict polynomial analytic unitaries, with real vacua at both coordinates. |
| dependency | [Signed curvature limit](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Matched gap-tensor convergence, analytic graph evaluation and the sign of the curvature term. |
| dependency | [Curvature weight](Yin_C_F0267_v1.md#statement) | Integrability of the squared curvature with half the kernel integral bounded by the squared marginal vacuum norm. |
| dependency | [Normal reversal](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Reversed derivations and actual reversed vacua on the original starred core. |
| dependency | [Exchange comparison](Yin_C_F0311_v1.md#statement) | Bounds for the full exchange cost and the output orthogonal to the first marginal, and universal equivalence. |
| dependency | [Single-pair assembly](Yin_C_F0313_v1.md#statement) | A single exchange-symmetric actual pair with infinite forward cost when the universal implication fails. |
| dependency | [Countable-circle example](Yin_C_F0292_v1.md#a-law-with-divergent-curvature-compositions) | Actual vacuum, circle radii and masses, and separated-circle full domains. |
| dependency | [Free extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Preservation of the coordinate derivations and their actual scalar vacua under the free product. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0323_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
