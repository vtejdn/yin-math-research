---
author: Yin
---

# Independent review of the one-third radial phase threshold for cubic concentration

## Finding

At 2026-11-14T13:02 UTC I independently reviewed for Yin the [candidate dated 2026-11-14T12:59](../../claims/Yin_C_F0261_v2.md#decision-candidate), its complete argument and its five declared dependency interfaces.
I did not participate in the development of the candidate.
I read the [review of v1](Yin_R_F0270_v1.md#finding) alongside the new candidate for the inherited inputs and checked the new averaging and endpoint calculations directly.
The subcritical integral estimate, the retained accretive estimate and the endpoint obstruction for the scalar radial identities all hold in the stated scopes.

### From the vacuum pairing to a positive average

For a fixed shift, let \(K=U_bP_b(P_b^2+s^2)^{-1}\).
Tracing the differentiated resolvent at squared radius \(s^2\) gives \(H_b(s)^2=s^2\operatorname{Re}\langle\xi,K\rangle+\operatorname{Re}\iint a_s(v)a_s(w)m_b(v,w)\,d\mu_b^2\).
The conditional expectation defining \(m_b\) preserves this trace because the two radial factors belong to its range.
For \(y>0\) the strict superlevel set of \(v/(v^2+s^2)\) above \(y\) is contained in \(0<v<1/y\), and \(\|K\|\le1/(2s)\).
The trace pairing of \(\xi\) with the polar part times each superlevel projection is at most \(H(F(1/y))\) in modulus by the rearrangement bound.
Integrating in \(y\) up to \(1/s\) and putting \(x=1/y\) gives \(|\langle\xi,K\rangle|\le D(s)\).
Thus \(H_b(s)^2\le c^2A_b(s)^2+s^2D(s)\), which implies (3) by subadditivity of the square root on nonnegative summands.

With \(0<\beta<1\), both integrals forming the full Mellin integral in (4) converge absolutely.
The substitution \(x=y^2\) gives their weighted difference as \(\frac{\pi}{2}(\csc(\pi\beta/2)-c\sec(\pi\beta/2))\).
I checked the slit integral using the jump \(1-e^{2\pi ip}\) on the positive ray and residue \(e^{i\pi(p-1)}\) at \(-1\).
The same value for \(0<p<1\) follows by taking \(a=p,\ b=1-p\) in Euler's beta integral and applying the reflection formula, as recorded in [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1), [5.12.3](https://dlmf.nist.gov/5.12.E3), and [5.5.3](https://dlmf.nist.gov/5.5.E3).
Since \(\cot(\pi\beta/2)\) decreases continuously from \(1/\sqrt3\) to \(0\) on \(2/3\le\beta\le1\), a choice strictly above \(2/3\) is available for every specified \(c\), including zero.
For a cutoff below \(c\), taking the upper tail removes a nonpositive integral from the nonnegative full value.
For a cutoff above \(c\), its entire upper tail is nonnegative.
Moreover \(0\le t\le1\), \(u\ge1\) imply \((1-ct/u)/(1+(t/u)^2)\ge(1-c)/2\).
These facts prove the lower bound on \(K(t)\), including when the full Mellin integral vanishes and at \(t=0\).
The average is absolutely integrable on the left since the one-particle kernels are bounded, and on the right since \(D(s)\le\|\xi\|_2/s\) and \(\beta>1/2\).
Applying the kernel lower bound before taking the supremum gives (5) for a nondecreasing measurable \(F\), with no maximizing shift required.

### Closing the integral on the stated families

In \(L^{3/2}(ds/s)\) over \(s\ge\varepsilon\), each dilation \(s\mapsto sy\), \(y\ge1\), decreases the norm of \(H(F(s))/s^{1/3}\).
Its undilated norm is \(J_\varepsilon^{2/3}\), giving the factor \(3/2\) upon integrating \(y^{-2/3}\,dy/y\).
In the subsequent \(L^3\) bound for (5) the dilation costs \(u^{2/3}\), so the integrated cost is \(1/(\beta-2/3)\).
The layer formulas of v1 require only that \(F\) be nondecreasing at this step, since the superlevel sets are terminal intervals up to their endpoints.
Hölder's inequality with exponents \(4,4,2\) and \(\|H(t)/t\|_2\le2\|v_\xi\|_2\) give \(J_\varepsilon\le3(2I_\varepsilon/3)^{1/4}\sqrt2\,\|\xi\|_2^{3/2}\) independently of the lower cutoff.
Inserting its cube root into (6) leaves \(I_\varepsilon^{1/4}\) on the left after division in the positive case.
The fourth power and monotone convergence give (2), also for an empty family or zero truncated integral.

For the accretive family v1 uses \(s=(2+3\kappa)r,\ g=2(1+\kappa)r\) and the inverse \(R=(V^*(Z-b)W+s)^{-1}\).
The vacuum pairing has modulus \(|\tau R|^2\ge g^2\|R\|_2^4\), and the mass up to \(r\) is bounded by \((s+r)^2\|R\|_2^2\) by compression to that spectral projection.
The resulting factor after squaring the mass bound and dividing by \(g^2r^2\) is \(81(1+\kappa)^2/4\).
The tail of the inverse at any test level is bounded by the same envelope since \(b-sVW^*\in N\) gives real part at least \(g\) with the original rotations.
The nonlinear estimate of v1 squares this factor, yielding the asserted fourth power for all \(\kappa\ge0\).

### Endpoint law and scope of sharpness

For \(d\mu(v)=(2/3)v^{-1/3}\,dv\) on \((0,1)\), the sum kernel is integrable by integrating first in \(0<w<v\), which leaves a multiple of \(\int_0^1v^{-2/3}\,dv\).
The multiplicative exclusion in the difference term is symmetric, bounds \(1/|v-w|\) by a cutoff-dependent multiple of \(1/(v+w)\), and permits the separate symmetrizations.
After \(w=vu\), inverting above one and then substituting \(u=t^3\) gives the signed coefficient \(-3\int_0^1(1+t+t^2)^{-1}dt=-\pi/\sqrt3\).
The unsigned coefficient is \(2\pi/\sqrt3\), so their linear combination with weights \(4/3,2/3\) vanishes.
The truncated full-line coefficient stays bounded, and \(v^{-1/3}\) is integrable against \(\mu\).
For the removed tail the absolute integral on \(1<w<2\) is bounded by a constant times \(1+|\log(1-v)|\), and the remaining tail is bounded by integrating a multiple of \(w^{-4/3}\).
This majorant is in \(L^2(\mu)\), proving square integrability of the proposed vector and justifying passage to the limit after integration against every bounded profile.
Restoring the original difference quotient uses its uniform bound by \(\|\phi'\|_\infty\) and the zero product mass of the diagonal.
These arguments also cover complex \(C^1\) profiles and profiles with a nonzero value at zero.
For \(\phi(v)=v/(v^2+s^2)\), the two quotients have respective numerators \(s^2-vw\) and \(s^2+vw\) over the common denominator \((v^2+s^2)(w^2+s^2)\).
Thus \(s^2\mathcal L(\phi)=H_\mu(s)^2-\rho A_\mu(s)^2\) with the claimed sign and normalization.
The normalized mass is exactly \(r^{2/3}\) on \(0<r\le1\), so the cubic integral includes \(\int_0^1dr/r\).
This verifies sharpness for the scalar identities.
Realization by an omitted shift of an actual tuple remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0261_v2.md#decision-candidate) | Full candidate at its stated revision and five direct dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0261_v2.md#statement) | Subcritical uniform estimate, radius-dependent accretive family and sharpness for the scalar radial identities. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0261_v2.md#argument) | Vacuum inequality, positive scale average, two truncated norm estimates, accretive transfer and representation of every endpoint radial profile. |
| [Finding](#finding) | [Compressed phase](../../claims/Yin_C_F0229_v1.md#the-integrated-phase-defect) | Conditional expectation paired with the two radial resolvent factors under product trace. |
| [Finding](#finding) | [Fixed-radius vacuum identity](../../claims/Yin_C_F0261_v1.md#nonpositive-radial-phase-on-a-fixed-shift-family) | Equality with the signed phase at squared radius \(s^2\) before imposing any sign condition. |
| [Finding](#finding) | [Vacuum rearrangement](../../claims/Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) | Layer bound for a polar contraction against the square-integrable vacuum. |
| [Finding](#finding) | [Nonlinear integral estimate](../../claims/Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) | Truncated superlevel and Hardy estimates for nondecreasing envelopes and the full estimate used for rotations. |
| [Finding](#finding) | [Accretive family](../../claims/Yin_C_F0261_v1.md#omitted-unitary-rotations-into-a-half-plane) | Uniformity of the rotated inverse bound, positive shift and admissibility of its tails at every radius. |
