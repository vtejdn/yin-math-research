---
author: Yin
---

# Uniform full-core slice bounds for product laws with bounded Haar density

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be Haar unitary and free from a unitary \(V\) with trace law \(\nu=\rho\,dm\), where \(m\) is Haar probability on the circle and \(0\le\rho\le L<\infty\).
Allow \(\rho\) to vanish on sets of positive Haar measure.
Write \(Y=X^*V\), and let \(F\) be a bounded Borel map on the circle with a measurable inverse on a conull set for \(m\).
Assume \(F(X),F(Y)\) have full actual starred conjugate variables in their generated tracial algebra.
Let \(s\) be their common vacuum norm and \(k\) the maximum of the two coordinate single-input right-slice costs in both adjoint orientations divided by \(s\), as in the [correlated Haar model](Yin_C_F0315_v1.md#statement).
Then
\[
                 k\le 38+2\sqrt{4/\pi}+3(2+\sqrt2)(3L+1).              \tag{1}
\]
The bound is uniform over the entire original starred polynomial unit ball and over \(F\).
It applies to uniforms on arbitrary measurable sets of Haar mass at least \(\ell>0\) with \(L=\ell^{-1}\), including arcs with a shrinking spectral hole.

## Argument

### A Fourier decomposition of the terminal derivative

Use \(Z=F(X)\), \(A=W^*(Z)=W^*(X)\), \(B=W^*(V)\), write \(X=h(Z)\), and let \(\mu\) be the law of \(Z\).
The [automatic product vacuum and full-core transfer](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) give an actual scalar vacuum \(\xi_V\) and reduce the estimate at \(Z\) to the corresponding right slice for \((Z,h(Z)^*V)\).
If \(V\) is Haar, the same result already gives \(k\le3\).
Otherwise put \(H=\xi_V V^*-1\), \(J=\iint |h(z)-h(w)|^2|z-w|^{-2}d\mu^2\), and let \(\xi_\mu\) be the scalar vacuum of the normal base.
The [phase criterion](Yin_C_F0265_v1.md#statement) gives \(J<\infty\) and \(s^2=\|\xi_\mu\|_2^2+\|H\|_2^2J\).

On Laurent polynomials \(b\) in \(V\), the terminal derivative in the [weighted free-product calculation](Yin_C_F0265_v1.md#a-global-square-integrable-kernel-estimate-for-mixed-columns) is
\[
     D b(z)=\int \frac{b(z)-b(w)}{z-w}\,w\,d\nu(w),
                 \qquad \tau(Db)=\tau(bH^*).
\]
Indeed \(Db=E_V(bV)-b\) for the scalar right slice \(E_V\).
Let \(P_-,P_+\) be the orthogonal projections on the strictly negative and strictly positive Fourier modes in \(L^2(m)\).
Then on this core
\[
       Db=bP_-\rho-P_-(b\rho),\qquad H^*=P_-\rho-P_+\rho
             \quad(\nu\text{-almost everywhere}).                        \tag{2}
\]
For \(0<r<1\), replacing \(w/(z-w)\) in the integral by \(rw/(z-rw)=\sum_{j\ge1}r^j(w/z)^j\) gives the first formula with the negative Fourier projection damped by \(r^j\).
As \(r\uparrow1\) the projections converge in \(L^2(m)\) by Parseval, hence also in \(L^2(\nu)\) by the upper density bound.
For each Laurent polynomial the difference-quotient integrand is bounded uniformly for \(r\ge1/2\), since \(|z-rw|^2=(1-r)^2+r|z-w|^2\).
Dominated convergence at the null diagonal gives the claimed \(Db\).
Integrating the formula against \(\rho\,dm\), the bilinear Fourier pairing moves \(P_-\) to \(P_+\) on \(\rho\), proving the second identity by density of Laurent tests.

Since \(P_-\rho+P_+\rho=\rho-1\), write
\[
       Db=D_{\rm b}b+\tfrac12 bH^*,\qquad
       D_{\rm b}b=\tfrac12(\rho-1)b-P_-(\rho b).
\]
The second formula defines a Hilbert-space bounded map on \(L^2(\nu)\), including at densities with zero sets: \(\rho b\in L^2(m)\) is independent of the representative, with norm at most \(\sqrt L\|b\|_{2,\nu}\).
Thus \(\|D_{\rm b}\|_{2\to2}\le(3L+1)/2\).
Denote \(b-\tau(b)\) by \(b^\circ\).
On centered polynomial \(b\) the centered output \((Db)^\circ\) splits into
\[
              R_1 b=(D_{\rm b}(b^\circ))^\circ,\qquad
              R_2 b=(b^\circ H^*)^\circ/2
\]
summed together.
Both maps kill constants and take values in \(B^\circ=L^2(B)\ominus\mathbb C1\).
The first has Hilbert norm at most \((3L+1)/2\), and the second has operator-norm-to-Hilbert norm at most \(\|H\|_2\).
No boundedness of multiplication by \(H\) on \(L^2(\nu)\) is used.

### The marginal kernel on a terminal base factor

For \(d=z-w\) put \(m_\epsilon=|d|^2/(|d|^2+\epsilon^2)\) and \(k_\epsilon=m_\epsilon(h(z)\overline{h(w)}-1)/d\), zero on the diagonal.
This is a bounded measurable kernel for fixed \(\epsilon>0\), with \(\|k_\epsilon\|_{L^2(\mu^2)}\le\sqrt J\).
For \(a\in A\) let \(O_{k_\epsilon}a(z)=\int k_\epsilon(z,w)a(w)d\mu(w)\).
The scalar soft slice \(E_{\mu,\epsilon}a(z)=\int m_\epsilon(z,w)(a(z)-a(w))/(z-w)\,d\mu(w)\) gives
\[
            O_{k_\epsilon}a=E_{\mu,\epsilon}a-hE_{\mu,\epsilon}(\bar h a).
                                                                    \tag{3}
\]
This follows by combining the two bounded-kernel integrals and using \(|h|=1\).
The [scalar bridge and its cutoff version](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) bound the column cost of \(E_{\mu,\epsilon}\) on all bounded marginal inputs by \(3(2+\sqrt2)\|\xi_\mu\|_2\), uniformly in \(\epsilon\).
Consequently the corresponding column cost of \(O_{k_\epsilon}\) is at most \(6(2+\sqrt2)\|\xi_\mu\|_2\), since multiplication by \(\bar h\) preserves the marginal column norm.

### Estimating all mixed words

On the algebraic free product \(\mathcal Q=A*\mathbb C[V,V^*]\) let \(\mathcal L\) be the derivation killing \(A\) and taking \(V\) to \(1\otimes V\).
Write \(C=\mathrm{id}\otimes\tau\).
The [terminal-block identity](Yin_C_F0265_v1.md#a-global-square-integrable-kernel-estimate-for-mixed-columns) gives \(CI_{k_\epsilon}\mathcal L(uba)=u(Db)(O_{k_\epsilon}a)\) for a reduced prefix \(u\) ending in \(A^\circ\) or empty, centered terminal noise polynomial \(b\), and arbitrary bounded base factor \(a\).
It vanishes on pure base inputs.
In this formula the scalar part \(\tau(Db)\) contributes at most \(2\|H\|_2\|k_\epsilon\|_2\) to the column cost by (5)–(6) of the cited calculation.
For the centered part associated with \(R_2\) the same proof gives cost at most \(2\sqrt{\kappa}\|H\|_2\|k_\epsilon\|_2\), \(\kappa=4/\pi\).
In fact its centered-output argument only uses \(R_2(1)=0\), its centered range and its bounded map norm \(C^*(V)\to B^\circ\): the terminal coefficient column of \(P_B(xa)\) has operator norm at most \(2\|a\|_2\) for every unit mixed column \(x\), and the commutative finite-family inequality applies to \(R_2\) with factor \(\sqrt{\kappa}\).
Those estimates apply to bounded measurable \(k_\epsilon\) by approximation by separated bounded kernels in the inner spectral calculus, as there.

For \(R_1\) we instead use (3) on the **last base factor**.
Indeed, on any finite input column \(x=(x_j)\) in \(\mathcal Q\), choose orthonormal families of reduced prefixes \(u_\alpha\) ending in \(A^\circ\) or empty and centered terminal Laurent polynomials \(b_i\) in \(L^2(B)\) spanning its finitely many noise-containing components.
Then
\[
                x_j=a_j+\sum_{\alpha,i}u_\alpha b_i a_{j\alpha i},
                    \qquad a_j,a_{j\alpha i}\in A .
\]
This is the right \(A\)-module decomposition, since word vectors ending in \(B^\circ\), tensored with the final \(L^2(A)\) variable, append isometrically and are orthogonal to the pure \(A\) summand.
In particular \(\mathbb E_A(\sum_j x_j^*x_j)=\sum_j a_j^*a_j+\sum_{j,\alpha,i}a_{j\alpha i}^*a_{j\alpha i}\).
Here one can verify the module identity by testing bounded terminal multipliers on the vacuum and using the same isometry.
The squared norm of the mixed \(R_1\) output is therefore at most
\[
   \sum_{j,\alpha}\left\|\sum_i R_1 b_i\otimes O_{k_\epsilon}a_{j\alpha i}
                           \right\|_2^2
   \le \|R_1\|_{2\to2}^2\sum_{j,\alpha,i}\|O_{k_\epsilon}a_{j\alpha i}\|_2^2
   \le \big(6(2+\sqrt2)\|R_1\|_{2\to2}\|\xi_\mu\|_2\big)^2
                     \left\|\sum_jx_j^*x_j\right\|.
 \]
The middle inequality applies \(R_1\) on the terminal noise Hilbert leg and uses orthogonality before this application; it assumes no orthogonality of the vectors \(R_1b_i\).
This controls the Hilbert-bounded term by marginal vacuum energy even if the Hilbert–Schmidt norm of \(k_\epsilon\) is large.

### The original and reversed slices

The [regularized target identity](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core), equation (7), writes the distinguished regularized right slice for \(Z,Y\) as the sum of its free reference liberation term and \(CI_{k_\epsilon}\mathcal L\).
The free term has column cost at most \(36\|\xi_\mu\|_2\) on the represented target core by the same bounded graph approximation for the measurable phase \(h\).
The target core is contained in \(\mathcal Q\), so the estimates of all three terminal contributions apply there.
As \(\epsilon\downarrow0\) the regularized derivative tensors tend to the actual tensors on each fixed target word by strong convergence of \(I_{m_\epsilon}\) on the coarse Hilbert space.
The resulting original right column cost at \(Z\) is bounded by
\[
      \big(36+3(2+\sqrt2)(3L+1)\big)\|\xi_\mu\|_2
           +(2+2\sqrt{\kappa})\|H\|_2\sqrt J .
\]
In the [reversed orientation](Yin_C_F0265_v1.md#adjoints-and-the-strong-duals) the free reference variable is \(V^*\), whose density is \(\rho(\bar z)\) with the same bound, and the phase energy and vacuum norms are unchanged.
The [original core transfer and exchange](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) give the single-input bounds on the reparametrized \(F(X),F(Y)\) core.
In this transfer the normal bounded slice on \(M\) agrees there with the original derivation contraction by bounded strong-star approximation of the omitted marginal.
Since \(\|\xi_\mu\|_2,\ \|H\|_2\sqrt J\le s\), these bounds give (1).
The argument imposes only the upper density bound and does not settle uniformity over densities with arbitrarily large essential supremum.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:17 |
| status | open |
| reason | Fix the uniform estimate for the whole mixed core at bounded product density, including densities with a spectral hole. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform cost for bounded densities and both orientations of all actual common generating reparametrizations. |
| argument | [Argument](#argument) | Negative Fourier projection, separation of the angular vacuum term, terminal marginal column estimate, and transfer through the actual cutoffs. |
| dependency | [Correlated Haar model](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Automatic product vacuum, exact normalization, freeness at Haar, exchange and the original-core transfer. |
| dependency | [Weighted unitary phase calculation](Yin_C_F0265_v1.md#argument) | Terminal noise cut, scalar output, centered-map estimate, measurable phase and reference cutoff transfer, and adjoint orientation. |
| dependency | [Scalar bridge](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Scalar cutoff formula and its uniform column bound on bounded marginal columns. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:31 |
| status | proved |
| reason | Adopt the uniform estimate on the entire mixed core for bounded product densities after independent review of the terminal decomposition and its inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform cost for bounded densities and both orientations of all actual common generating reparametrizations. |
| argument | [Argument](#argument) | Negative Fourier projection, separation of the angular vacuum term, terminal marginal column estimate, and transfer through the actual cutoffs. |
| dependency | [Correlated Haar model](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Automatic product vacuum, exact normalization, freeness at Haar, exchange and the original-core transfer. |
| dependency | [Weighted unitary phase calculation](Yin_C_F0265_v1.md#argument) | Terminal noise cut, scalar output, centered-map estimate, measurable phase and reference cutoff transfer, and adjoint orientation. |
| dependency | [Scalar bridge](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Scalar cutoff formula and its uniform column bound on bounded marginal columns. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0326_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
