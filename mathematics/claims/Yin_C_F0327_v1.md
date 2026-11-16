---
author: Yin
---

# A normal coordinate relative to a spectral projection conjugated by a free Poisson unitary

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded and normal with diffuse compact law \(\mu\) in a finite tracial von Neumann algebra with faithful probability trace.
Let \(A=W^*(Z)\), take a Borel sign \(a=a(Z)\in\{-1,1\}\) with \(\tau(a)=0\), and let \(u\) be a unitary free from \(A\) with Poisson law of parameter \(r\), \(0<r<1\).
Thus \(\tau(u^k)=r^{|k|}\).
A complex parameter of modulus \(r\) gives the same conjugation after scalar rotation.
Write \(s=uau^*\), \(P=(1+s)/2\), \(M=W^*(Z,P)\), \(d=z-w\), and put
\[
  \rho=r^2,\qquad c_\rho=\frac{\rho}{1-\rho^2},\qquad
  J=\iint_{z\ne w}\frac{|a(z)-a(w)|^2}{|z-w|^2}\,d\mu(z)d\mu(w).
\]
On the represented starred polynomial core in \(Z,P\), a distinguished outer derivation \(\delta\) with \(\delta Z=1\otimes1,\ \delta P=0\) and actual vacuum \(\xi=\delta^*(1\otimes1)\) exists exactly when \(Z\) has an actual scalar divided-difference vacuum \(\xi_\mu\) and \(J<\infty\).
In that case
\[
 \|\xi\|_2^2=\|\xi_\mu\|_2^2+c_\rho^2 J,\qquad
 \left(\sum_j\|(\mathrm{id}\otimes\tau)\delta x_j\|_2^2\right)^{1/2}
 \le C\|\xi\|_2\left\|\sum_j x_j^*x_j\right\|^{1/2}                    \tag{1}
\]
for every finite polynomial column, with an absolute \(C\).
The corresponding assertion for \(Z^*\) has the same energies and constant.
At \(r=0\) the sign is free from the base and only scalar actuality is required.
At \(r=1\) the nonconstant sign commutes with \(Z\) and no such distinguished derivation exists.
These relative models therefore cannot yield divergent ratios in the [projection formulation of the general normal implication](Yin_C_F0308_v1.md#statement).
For example, give two separated planar disks half the probability each with constant area density on each disk, and take opposite signs on the two disks.
The scalar vacuum is bounded by symmetrizing the divided-difference integral, since the absolute inverse distance has uniformly bounded integral in either variable on the two disks.
Here \(J<\infty\) by separation, and \(\tau(as)=\rho>0\) makes the relative model nonfree.
The projection is an atomic coefficient.
The [free conjugation obstruction for diffuse coefficients](Yin_C_F0243_v1.md#statement) concerns a different marginal hypothesis.

## Argument

### The two symmetries and the full joint law

Let \(B=W^*(a)=\operatorname{span}\{1,a\}\).
The algebras \(aW^*(u)a\) and \(W^*(u)\) are free, since alternating centered elements expand to reduced words separated by the centered base sign \(a\).
The positive analytic powers of \(aua\) have moments \(r^k\), as do the positive powers of \(u^*\).
The trace on each of the two unital analytic polynomial algebras is the character evaluating its generator at \(r\).
Thus the trace is the product character on their algebraic free product: the centered parts stay centered under multiplication within either factor, and an alternating product of centered parts has zero trace by freeness.
It follows that \(as=(aua)u^*\) has moments \(\rho^{|k|}\).
Every word in two symmetries reduces to a power of their product or such a power times one symmetry.
By cyclic reduction the trace of an odd word equals that of one of the two centered symmetries, hence vanishes.

In another free product let \(S\) be a centered symmetry free from \(A\), form \(v=aS\), and set
\[
 \Phi_\rho(v)=(\rho+v)(1+\rho v)^{-1},\qquad
 s_\rho=a\Phi_\rho(v)
       =\rho a+(1-\rho^2)S(1+\rho aS)^{-1}.                             \tag{2}
\]
The unitary \(v\) is Haar by its alternating reduced powers.
As \(ava=v^*\) and the coefficients of \(\Phi_\rho\) are real, \(s_\rho\) is a selfadjoint unitary.
Its trace is zero by the absolutely convergent Laurent expansion and the odd-word calculation for \(a,S\).
The moments of \(as_\rho=\Phi_\rho(v)\) are \(\rho^{|k|}\), by the constant coefficients of its analytic powers and adjoints.
This identifies all traces of words in \(a,s_\rho\) and \(a,s\), and hence their \(B\)-valued moments, by testing against \(1,a\).
In the first model \(A\) and \(W^*(a,s)\subset B\vee W^*(u)\) are free over \(B\).
The same holds for \(A,W^*(a,s_\rho)\subset A\vee W^*(S)\) in the second, using \(W^*(a,s_\rho)\subset B\vee W^*(S)\).
In both cases this follows from the [reduced-word amalgamation calculation](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners).
Expansion into \(B\)-means and alternating centered products now identifies every mixed trace including arbitrary \(A\) letters, so trace faithfulness identifies the generated algebras fixing \(A\).
Moreover
\[
          S=-\rho a+(1-\rho^2)s_\rho(1-\rho a s_\rho)^{-1}.               \tag{3}
\]
Thus \(M=A*W^*(S)\) in this representation, and we use \(s=s_\rho\) below.

### A derivative with prescribed values on the two symmetries

Let \(\Gamma^0\) equal \(b\otimes1-1\otimes b\) on \(A\) and vanish on \(S\) on the represented algebraic free product of \(A,\operatorname{span}\{1,S\}\).
Its double trace is zero by traciality and the centered reduced-word decomposition.
For an \(A\)-tensor \(\theta\) write \(a\theta\) for its outer left product, and use the same convention on either side for other outer products.
If \(\gamma a=\theta\), \(a\theta=-\theta a\) and \(\gamma s=0\), formal differentiation of (3) prescribes
\[
 \gamma S=-\rho\theta+c_\rho(S+\rho a)\theta(S+\rho a)
          =c_\rho\{S\theta S-\theta+\rho[(a\theta)S-S(a\theta)]\}.        \tag{4}
\]
Indeed differentiating the inverse in (3) puts \(s(1-\rho a s)^{-1}=(S+\rho a)/(1-\rho^2)\) on both sides of \(\theta\).
Take \(\theta=\alpha=a\otimes1-1\otimes a\).
Define \(\gamma\) by adding the right side of (4) at \(S\) to \(\Gamma^0\), keeping its values on \(A\).
Both summands anticommute with \(S\) under the two outer actions, exactly respecting \(S^2=1\).
The algebraic free product is represented faithfully by reduced words.
Equations (2) and (3) are reciprocal identities of norm-convergent resolvents.
Their Neumann series and product-rule derivatives converge since their \(n\)th derivative terms are bounded by \(C_\rho n\rho^{n-1}\).
Differentiating the inverse substitutions in both orders now shows that this derivation kills \(s\).
Equivalently one can substitute (4) in the derivative of (2); the factor multiplying a change in \(S\) has invertible outer factors from \(1+\rho aS\) and \(1+\rho Sa\).
These graph extensions restrict to a represented derivation: the algebraic derivations in (4) have adjoint vacua below, and their adjoint domains contain bounded algebraic simple tensors by the product rule.
For that last assertion their fixed right sides at \(S\) here are finite algebraic tensors, so both one-leg integrations in the adjoint calculation are bounded.
Consequently \(\gamma\) on the original core is its partial liberation at \(Z\).

Specifically, on the two-dimensional scalar algebra of \(S\) use the derivations \(D_1S=S\otimes S-1\otimes1\) and \(D_2S=1\otimes S-S\otimes1\).
Each kills \(1\), respects \(S^2=1\), and has scalar right slice of operator-norm-to-Hilbert norm one, with scalar vacuum \(-S\) and zero, respectively.
They extend across \(A\) by zero.
For \(\beta\in L^2(\mu^2)\) let \(D_{i,\beta}\) insert \(\beta\) at the two inner legs, first for bounded simple tensor sums and then by approximation on each finite word.
Writing \(C_0=\mathrm{id}\otimes\tau\) and \(J_S(f\otimes g)=f(Z)Sg(Z)\), the [free terminal-block bound and vacuum formula](Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) give
\[
 c(C_0 D_{i,\beta})\le (2\sqrt{4/\pi}+2)\|\beta\|_2,\qquad
 D_{1,\beta}^*(1\otimes1)=-J_S(\bar\beta),\quad D_{2,\beta}^*(1\otimes1)=0 .
\]
Here \(c\) is the finite-column cost on the bounded-base free core.
The proof needs the centered scalar slice, its bound, and the actual scalar vacuum of each indicated derivation.
On \(x+yS\) their slices are \(-y\) and \(-yS\).
No derivation sending \(S\) to \(1\otimes1\) is used.
Freeness makes \(J_S\) an isometry from \(L^2(\mu^2)\), with range perpendicular to \(L^2(A)\).
It intertwines the outer marginal actions with multiplication in the first and second variables.

We have \(\gamma=\Gamma^0+c_\rho(D_{1,\alpha}+\rho D_{2,a\alpha})\).
Its vacuum on the original core is \(\eta=-c_\rho J_S(\alpha)\), since \(\alpha(z,w)=a(z)-a(w)\) is real, (2) has graph approximants, and the target core generates all of \(M\).
Its left-right marginal spectral measure is therefore \(c_\rho^2|\alpha|^2\mu^2\).
The [liberation recovery formula](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) together with [its adjoint limit](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) gives the exact relative criterion and vacuum norm in (1).
In applying this argument only the distinguished spectral law needs diffuseness: the inner multiplier \(I_d\) is injective on its coarse space, the formal derivative takes the marginal forced values and kills the coefficient, and \(I_d\delta=\gamma\) on words.
The omitted sign is selfadjoint, so its starred value is already fixed.
These are the descent and scalar-adjoint calculations in the cited proof, irrespective of the coefficient law.
In the model (2) the vector itself is \(\xi=\xi_\mu-c_\rho J_S(\alpha/\bar d)\), with the inverse taken off the product-null diagonal.

### Uniform control of the original right slice

Suppose the two finiteness conditions hold.
Set \(k_\epsilon=\bar d/(|d|^2+\epsilon^2)\), \(m_\epsilon=d k_\epsilon\) and \(\beta_\epsilon=k_\epsilon\alpha\).
On the target core, inner multipliers commute with outer multiplication and \(\alpha,a\alpha\) are marginal tensors, giving
\[
  C_0 I_{m_\epsilon}\delta
     = C_0 I_{k_\epsilon}\Gamma^0+
            c_\rho C_0 (D_{1,\beta_\epsilon}+\rho D_{2,a\beta_\epsilon}). \tag{5}
\]
The correction has column cost at most \(2(2\sqrt{4/\pi}+2)c_\rho\sqrt J\), since \(\|\beta_\epsilon\|_2\le\sqrt J\).
For fixed \(\epsilon\) all these kernels are bounded.
The reference term on \(A\) is the scalar slice
\[
           f(z)\longmapsto\int k_\epsilon(z,w)(f(z)-f(w))\,d\mu(w).
\]
Its column cost on all bounded Borel inputs is at most \(3(2+\sqrt2)\|\xi_\mu\|_2\), uniformly in \(\epsilon\). [Scalar bridge and soft cutoff](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word)
The free extension has the same bound on the bounded-base free core.
Indeed expand each input into orthonormal reduced prefixes ending outside \(A\), or empty, times bounded terminal \(A\)-coefficients.
Only the terminal cut survives the second-leg trace and the sum of the squared coefficients equals the conditional expectation onto \(A\) of the original squared column. [Free right-module calculation](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate)
Applying the scalar column bound to this joint coefficient family gives the assertion.

For a target polynomial column replace \(s\) by partial Neumann sums in (2).
They converge in operator norm, entrywise for the column, and in the coarse graph of each of the displayed free-core derivations for fixed \(\epsilon\), by the same summable differentiated series.
Thus the column bounds pass to every target polynomial column with its actual input norm.
In (5) \(I_{m_\epsilon}\) converges strongly to the identity on each coarse vector by diffuseness and absolute continuity of its joint inner marginal spectral measure.
Passing to the limit proves (1) with an absolute constant, by the exact squared vacuum identity.
The adjoint coordinate uses the same sign \(a\), the reflected spectral law, and the denominator \(\bar z-\bar w\), with unchanged squared norms.
At \(r=0\) reduced words give freeness of the conjugated sign from the whole base, and the scalar slice bound and free right-module calculation apply without the correction.
At \(r=1\), \(s=a\) and differentiating \([Z,s]=0\) while killing \(s\) would give \(1\otimes s-s\otimes1=0\), impossible for a centered sign.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:07 |
| status | open |
| reason | Fix the actual relative criterion and uniform column bound for the trace-half spectral projection under free Poisson conjugation for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full relative actuality criterion and universal original slice ratio on this conjugated atomic coefficient. |
| argument | [Argument](#argument) | Dihedral mixed-law model, resolvent inversion, two sign derivatives and the soft-cutoff column estimate. |
| dependency | [Free amalgamation](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Equality of the two-symmetry laws extended to all base words. |
| dependency | [Free terminal-block estimate](Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) | Arbitrary inner base tensor, scalar vacua and column costs at the free sign. |
| dependency | [Liberation and relative descent](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Recovering the represented derivative and the normal commutator. |
| dependency | [Scalar adjoint limit](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Exact vacuum formula from its marginal and finite inverse-gap energy. |
| dependency | [Soft scalar bound](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Cutoff-independent scalar finite-column cost on bounded Borel inputs. |
| dependency | [Free right modules](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) | Action of the free reference slice on the terminal base and its squared column. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:39 |
| status | proved |
| reason | Adopt the dihedral projection criterion and the uniform column bound after independent review of the law, graph and both orientations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full relative actuality criterion and universal original slice ratio on this conjugated atomic coefficient. |
| argument | [Argument](#argument) | Dihedral mixed-law model, resolvent inversion, two sign derivatives and the soft-cutoff column estimate. |
| dependency | [Free amalgamation](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Equality of the two-symmetry laws extended to all base words. |
| dependency | [Free terminal-block estimate](Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) | Arbitrary inner base tensor, scalar vacua and column costs at the free sign. |
| dependency | [Liberation and relative descent](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Recovering the represented derivative and the normal commutator. |
| dependency | [Scalar adjoint limit](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Exact vacuum formula from its marginal and finite inverse-gap energy. |
| dependency | [Soft scalar bound](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Cutoff-independent scalar finite-column cost on bounded Borel inputs. |
| dependency | [Free right modules](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) | Action of the free reference slice on the terminal base and its squared column. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0334_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
