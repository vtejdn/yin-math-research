---
author: Yin
---

# Finite signed return sums on spatial shells with no volume loss

## Statement

Fix a finite group-ring matrix on a finitely generated group, normalize \(Q=I-A^*A/M\) with \(M\ge\|A\|^2,\ M>0\), and let \(p=1_{\{1\}}(Q)\).
Use the [padded first-return coefficients](Yin_C_A0067_v1.md#statement) \(f_t^\pm\) computed separately for two matrix coordinates, an endpoint \(g\ne e\) and a phase \(\zeta\in\{1,\mathrm i\}\).
Include all these indices in a single coefficient space \(\mathscr H=\ell^2(g,i,j,\zeta)\), retaining the signs at each endpoint.
Write \(d=\sum_{t\ge1}t(f_t^--f_t^+)\) pointwise and set \(b_n=\sum_{t=1}^n(f_t^+-f_t^-)\), including \(b_0=0\).
If \(m\) is the number of columns, the following unweighted square bound holds for **every** input:
\[
                         \sum_{n\ge0}\|b_n\|_{\mathscr H}^2\le128m .       \tag{1}
\]
All \(b_n\) use only finitely many original product fibers.
The sum (1) controls the cumulative signed differences across time and is independent of group growth.

Suppose additionally that the following return differences at the identity satisfy a bound for some \(0<\alpha<2\), \(D<\infty\):
\[
       \tau_m(Q^{2^j}-Q^{2^{j+1}})\le D\,2^{-\alpha j}\qquad(j\ge0).      \tag{2}
\]
This infinite family of scalar estimates is an assumption to be established for the chosen matrix; each individual test involves finite products and no kernel atom.
Let \(\beta\ge0,\ \kappa>\beta/\alpha\), choose \(J_0\) so \(2^{-\kappa J_0}\le1/2\), and use \(z_j=1-2^{-\kappa j}\) for \(j\ge J_0\).
Choose \(L>(\kappa+\kappa\alpha)\log(2)/2\) and \(N_j=\lceil L(j+1)2^{\kappa j}\rceil\).
For \(2^j\le|g|<2^{j+1}\) put
\[
 B_\bullet(g,i,j',\zeta)=\sum_{n=0}^{N_j}z_j^n b_n(g,i,j',\zeta).
\]
The spatial shell index \(j\) and the column-coordinate index \(j'\) are independent.
With the exterior coefficient norm using squared weight \((1+|g|)^\beta\), for each \(J\ge J_0\),
\[
             \|d-B_\bullet\|_{\beta,\ |g|\ge2^J}
                 \le C\,2^{-(\kappa\alpha-\beta)J/2}.                  \tag{3}
\]
In particular the exterior norm of the actual projection is bounded by the norm of these **finite** signed sums on the exterior plus the explicit error in (3).
Conversely that finite-sum array has exterior norm at most four times the projection's exterior norm plus the same error.
These are two one-sided estimates, valid also when the compared tails diverge.
The constants may depend on the matrix and the parameters; the time horizon per shell is \(O(R^\kappa\log R)\) for radius \(R=2^j\).
No factor counting the endpoints in a shell enters (3).
The norm of the computed arrays must still be bounded across all exterior shells to infer the desired integrability.

## The joint square bound across time and endpoints

Use the notation \(R_z=(1-z)(I-zQ)^{-1}\), now also for complex \(|z|<1\).
For each padded probe the scalar function \(a_\pm(z)=(1-z)\sum_{t\ge0}h_t^\pm z^t\) is the integral of \((1-z)/(1-zs)\) against a probability measure on \([0,1]\) with an atom of at least \(1/2\) at one.
For \(|z|<1,\ 0\le s\le1\) the integrand has nonnegative real part:
\[
 1-(1+s)\operatorname{Re}z+s|z|^2\ge(1-|z|)(1-s|z|).
\]
The atom contributes its full mass to the real part.
Thus \(|a_\pm(z)|\ge1/2\) uniformly on the complex disk, including at a nonclosed range.
Also \(\|R_z\|\le2\) there, since \(|1-z|\le |1-zs|+|z|(1-s)\le2|1-zs|\).

For \(x=\delta_g e_i,y=\delta_e e_{j'}\) define the polarization
\[
       \mathcal P(X)_{g,i,j',\zeta}
       =(\zeta x^*Xy+\bar\zeta y^*Xx)/2 .
\]
Both arrays in this average have norm at most \(\sqrt2\|X\|_2\) since reversing the endpoints inverts \(g\) and exchanges the matrix indices, and there are two phases.
For selfadjoint \(X\) the array is the real polarized coefficient.
On the disk the renewal identity gives
\[
 C(z)=\sum_{n\ge0} b_n z^n
     =\frac{f^+(z)-f^-(z)}{1-z}
     =\frac{\mathcal P(R_z)}{a_+(z)a_-(z)}
\]
coordinate by coordinate.
The common trace norm bound \(\|R_z\|_2\le2\sqrt m\) gives \(\|C(z)\|_{\mathscr H}^2\le128m\).
Integrate the coordinatewise scalar power-series square identity on \(|z|=r<1\), then sum the nonnegative integrals and let \(r\uparrow1\).
This gives (1) without an exchange of an infinite time sum with a spatially weighted estimate.
In particular for real \(0<z<1\), truncating at \(N\) costs at most
\[
          \sqrt{128m}\,z^{N+1}/\sqrt{1-z^2}
\]
in the norm of the **entire** coefficient array, by Cauchy–Schwarz on the remaining time coefficients.

## Passing from finite returns to a spatial shell

Telescoping (2) at dyadic times gives \(\tau_m(Q^{2^j}-p)\le D(1-2^{-\alpha})^{-1}2^{-\alpha j}\), by bounded spectral convergence.
For the positive mass \(F(t)=\tau_m(1_{(0,t]}(I-Q))\), the bound implies \(F(t)\le C_1t^\alpha\) on \(0<t\le1\).
Indeed take \(2^j\le1/t<2^{j+1}\) for \(t\le1/2\); on \((0,t]\), \(Q^{2^j}\) has multiplier at least \((1-t)^{1/t}\ge1/4\).
For real \(1/2\le z<1\) this yields
\[
 \|R_z-p\|_2^2=\int_{(0,1]}
       \left(\frac{1-z}{1-z+zt}\right)^2\,dF(t)\le C_2(1-z)^\alpha .
\]
Bound the part below \(1-z\) by \(F(1-z)\); on the subsequent dyadic intervals the squared multiplier decreases as \(O(2^{-2v})\) and the mass bound increases as \(O(2^{\alpha v})\).
The positive remainder also controls all individual probe denominators.
In fact \(a_\pm(z)-a_\pm(1)=(\xi_\pm^*(R_z-p)\xi_\pm)/2\), with \(a_\pm(1)\) the endpoint atom of the padded probe.
For any positive matrix \(X\) the latter quadratic form before division by two is at most twice \(\tau_m(X)\), by Cauchy–Schwarz on the two sites and translation invariance of the diagonal.
Hence \(\sup|a_\pm(z)-a_\pm(1)|\le\sqrt m\,\|R_z-p\|_2\).
The denominators are bounded below by \(1/2\), so the difference of their reciprocal products is bounded by a uniform constant times this supremum.
Applying this bound to \(\mathcal P(p)\), and the polarization norm bound to \(R_z-p\), gives
\[
            \|C(z)-d\|_{\mathscr H}\le C_m\|R_z-p\|_2 .
\]
Here \(d=\mathcal P(p)/(a_+(1)a_-(1))\) by C67.

For \(z=z_j\), the squared approximation error to \(d\) is \(O(2^{-\kappa\alpha j})\).
The squared time truncation error is \(O(2^{\kappa j}\exp(-2L(j+1)))\) since \(z_j^{N_j}\le \exp(-(1-z_j)N_j)\).
The choice of \(L\) makes this term at most \(O(2^{-\kappa\alpha j})\).
Restrict each global error estimate to its assigned shell, multiply by the maximum squared-norm weight \(O(2^{\beta j})\) there, and sum from \(J\) upwards.
This proves (3).
The [pointwise factor bounds of C67](Yin_C_A0067_v1.md#statement) and the triangle inequality give the two exterior comparisons.

On the [original-group integer rows with a massive walk Green kernel](Yin_C_A0074_v1.md#resolvent-of-the-original-product-fibers), both (1) and (3) hold although every finite-power coefficient test fails.
Indeed \(F(t)\le Ct^\alpha\) with \(\alpha=1/(2d)\) there, and integration of \((1-t)^n\le e^{-nt}\) against the positive spectral measure gives \(\tau_m(Q^n-p)=O(n^{-\alpha})\), hence (2).
Their signed shell arrays consequently differ from the exponentially localized true signed means by the polynomial error in (3).
For a general matrix on a good four-line group neither the full family (2) nor summability of the signed finite-shell arrays is automatic.

## Assessment history

### Decision finite-signed-shell-arrays

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:03 |
| status | proved |
| reason | Independent review verified the signed square bound on the disk, the spectral implication from dyadic returns and the shellwise time truncation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All-input joint square bound and finite signed shell estimates under the stated time decay assumption, without a group-volume loss. |
| argument | [Proof](#the-joint-square-bound-across-time-and-endpoints) | Complex polarization, coefficient square identity, signed Abel approximation and the polynomial time horizon per shell. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0112_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-finite-signed-shell-arrays)
