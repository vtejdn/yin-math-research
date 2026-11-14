---
author: Yin
---

# Cubic singular concentration puts the polar factors of omitted shifts in both canonical domains

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a finite bounded normal generating tuple with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Fix a coordinate \(Z=X_i\), let \(N=W^*(X_j:j\ne i)\), and let \(E=(\mathrm{id}\otimes\tau)\delta\) denote its right slice on the original starred polynomial algebra, with vacuum \(\xi=\delta^*(1\otimes1)\).
Use \(E^\#\) for the corresponding right slice at \(Z^*\) of the adjoint tuple, and \(E_r,E_r^\#\) for the [normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) at radius \(r>0\).
For a nonempty family \(\mathcal G\subset N\) define
\[
 T_b=Z-b=U_b|T_b|,\qquad F_b(s)=\tau(1_{[0,s]}(|T_b|)),\qquad
 F(s)=\sup_{b\in\mathcal G}F_b(s),\qquad I(F)=\int_0^\infty F(s)^3\,\frac{ds}{s^3}.
\]
The [kernel theorem](Yin_C_F0229_v1.md#statement) makes \(U_b\) unitary, including for nonnormal \(b\).
Assume \(I(F)<\infty\).
For all \(b\in\mathcal G\), contractions \(a,c\in N\), and \(\sigma\in\{1,-1\}\), the vector \(x=aU_b^\sigma c\) belongs to the four domains of \(\bar E,E^*,\overline{E^\#},(E^\#)^*\).
For an absolute \(C\),
\[
\begin{aligned}
 \max\{\|\bar E x\|_2,\|\overline{E^\#}x\|_2,
                \sup_{r>0}\|E_r x\|_2,\sup_{r>0}\|E_r^\#x\|_2\}
     &\le C\sqrt{I(F)},\\
 E^*x=x\xi-\overline{E^\#}x,\qquad (E^\#)^*x
     &=x\xi^*-\bar E x .
\end{aligned}                                                         \tag{1}
\]
Both \(E_r x\to\bar E x\) and \(E_r^\#x\to\overline{E^\#}x\) in \(L^2\) as \(r\downarrow0\), uniformly over the displayed \(b,a,c,\sigma\).
The shifts in the supremum defining \(F\) may vary with \(s\), and the family needs no common bound on \(\|b\|\).

In particular these conclusions hold over all omitted shifts at a coordinate satisfying the [narrow secant cone condition](Yin_C_F0272_v1.md#statement), and over all shifts preserving normality at any coordinate by the [normal residual estimate](Yin_C_F0270_v1.md#statement).
The [necessary cubic estimate for finite columns](Yin_C_F0258_v1.md#statement) involves precisely \(I(F)\) over all omitted shifts.
Equation (1) recovers domain inclusion and uniform strong cutoff convergence on the specified polar factors and their omitted multiples from this estimate alone.
Boundedness of either slice on arbitrary bounded inputs remains a separate question.

There is a corresponding result for any fixed mixed starred polynomial \(p\) in the original coordinates.
Put
\[
 B_p=\max_{D\in\{\delta,\delta^\#\},\,q\in\{p,p^*\}}
                  \|\Phi(Dq)\|_{M\bar\otimes M^{\mathrm{op}}}.
\]
For any nonempty family \(\mathcal G\subset N\), define \(F\) with the residuals \(p-b\) in place of \(Z-b\).
If \(I(F)<\infty\), conclusions (1) and both uniform cutoff limits hold for these residuals with \(C B_p\sqrt{I(F)}\) on the right of the norm bound.
In particular, for selfadjoint \(p\) and a nonempty set of real thresholds \(\Lambda\), take \(F(s)=\sup_{t\in\Lambda}\tau(1_{[t-s,t+s]}(p))\).
If \(I(F)<\infty\), every \(1_{(-\infty,t)}(p)\), \(t\in\Lambda\), belongs to the four domains and both cutoffs converge uniformly in \(t\).
This includes single thresholds at which the [absolute resolvent integral](Yin_C_F0285_v1.md#statement) is infinite.

For a symmetric compactly supported real scalar law with an actual vacuum, write \(\mu\) for the law of \(|Z|\) and \(F_0(s)=\mu([0,s])\).
At the shift zero the squared slice norm of the sign is comparable, with absolute positive constants, to \(I(F_0)\).
There are such laws for which \(I(F_0)<\infty\) but the integral of the \(L^2\) norms of the sliced polar resolvents diverges.

## Argument

### The two derivations and the polar resolvents

Write \(T=T_b\), \(P=|T|\), \(P'=|T^*|\), and \(\mu=\operatorname{law}(P)=\operatorname{law}(P')\).
For \(s>0\) put
\[
 R_s=(T^*T+s^2)^{-1},\qquad L_s=(TT^*+s^2)^{-1},\qquad W_s=T R_s=L_sT .
\]
Use \(\mathcal B=M\bar\otimes M^{\mathrm{op}}\) to represent the coarse tensor under \(\Phi(u\otimes v)=u\otimes v^{\mathrm{op}}\).
Outer multiplication by \(u,v\) is left multiplication by \(u\otimes v^{\mathrm{op}}\).
For \(D=\delta,\delta^\#\), write \(V=\Phi(DT)\), \(V'=\Phi(DT^*)\), where \(\delta^\#x=(\delta(x^*))^\dagger\) on the core and \(\dagger\) flips and takes adjoints on both legs.
In each orientation one of \(V,V'\) is \(1\) and the other is a unitary marginal secant phase.
Set \(g_r(z,w)=|z-w|^2/(|z-w|^2+r^2)\) in the two inner spectral variables of \(Z\).
For the original slices set \(g=1\), and for radius \(r\) set \(g=g_r\).
The cutoff multiplies from the right by \(g\) in \(\mathcal B\).
The [resolvent graph identity](Yin_C_F0229_v1.md#argument) reads
\[
 \Phi(DW_s)g=s^2 (L_s\otimes R_s^{\mathrm{op}})Vg
                      -(W_s\otimes W_s^{\mathrm{op}})V'g .              \tag{2}
\]
For \(W_s^*\) interchange \(T,T^*\), hence \(L_s,R_s\), \(V,V'\), and replace both copies of \(W_s\) by \(W_s^*\).
The derivative of \(aW_sc\) adds just the outer multipliers \(a,c\) to (2).
Indeed \(a,b,c\) have bounded strong-star approximants by polynomials in the omitted coordinates, whose two derivatives vanish identically.
For fixed \(b,s\) one may approximate the inverse by its geometric series with contraction \(1-(T^*T+s^2)/C_0\), where \(C_0\) is greater than \(s^2\) plus a common bound on the squared norms of the approximating residuals.
The differentiated tails tend to zero in the coarse Hilbert space by a bound proportional to \(\sum_{n>m}nq^{n-1}\) with \(q<1\).
For every fixed partial polynomial the bounded outer factors tend strongly-star to their targets, giving simultaneous graph approximation for both orientations, with bounded strong-star convergence of the inputs.
This proves the sliced identities for the closed original forward operators and, by normality on bounded inputs, for the fixed-radius extensions.
In the core adjoint identities \(E^*p=p\xi-E^\#p\) and \((E^\#)^*p=p\xi^*-Ep\), the products with the vacua converge in \(L^2\) under these same approximations. [Polynomial adjoint identities](Yin_C_F0271_v1.md#exact-energy-and-affine-line-rigidity)
Closedness gives both identities for \(aW_sc\) and \(aW_s^*c\), and Riemann sums give them for integrals over compact intervals of \(s>0\), where the resolvents and their displayed derivatives are norm continuous.

### Orthogonal output projections and the cubic integral

First take \(a=1\).
For \(d=2^j\), \(j\in\mathbb Z\), let \(e_d=1_{[d,2d)}(P')\) when the input contains \(W_s\) and use \(P\) for \(W_s^*\).
Their sum is the unit, and \(p_d=\tau(e_d)=\mu([d,2d))\).
The second-leg trace slice of \((A\otimes B^{\mathrm{op}})V_0\) is bounded in \(L^2\) by \(\|A\|_2\|B\|_1\|V_0\|\), since the second-leg functional has norm \(\|B\|_1\).
The outer suffix \(c\) replaces \(B\) by \(Bc\), whose trace norm is at most \(\|B\|_1\).
The first factors in (2) satisfy
\[
 \|e_d L_s\|_2\le\frac{\sqrt{p_d}}{d^2+s^2},\qquad
 \|e_d W_s\|_2\le\frac{2d\sqrt{p_d}}{d^2+s^2}.
\]
The second estimate uses \(W_s=P'(P'^2+s^2)^{-1}U_b\).
For \(W_s^*\) the swapped estimates have the same bounds.
Since \(\|Vg\|,\|V'g\|\le1\), the \(L^2\) norm of the \(e_d\)-part of each sliced integrand at \(W_s c\) or \(W_s^*c\) is at most
\[
 2\sqrt{p_d}\int\frac{s^2+dw}{(d^2+s^2)(w^2+s^2)}\,d\mu(w).
                                                                    \tag{3}
\]
For \(d,w>0\) the fraction factors as
\[
 \frac1{d+w}\left(\frac d{d^2+s^2}+\frac w{w^2+s^2}\right).
\]
Its integral over \(s>0\) equals \(\pi/(d+w)\).
Thus each projected integral converges absolutely in \(L^2\) with norm at most \(2\pi\sqrt{p_d}K(d)\), where \(K(v)=\int(v+w)^{-1}\,d\mu(w)\).
For \(d\le v<2d\), \(K(d)\le2K(v)\), so the square sum over \(d\) is bounded by \(16\pi^2\int K(v)^2\,d\mu(v)\).
Left multiplication by the omitted contraction \(a\) after adding the orthogonal components preserves the resulting bound.

For any probability law \(\mu\) on \((0,\infty)\), with \(F_\mu(t)=\mu((0,t])\), one has
\[
                 \tfrac12 I(F_\mu)
           \le \int K^2\,d\mu \le 6 I(F_\mu).                          \tag{4}
\]
For the lower bound take three independent variables \(v,w,w'\) with law \(\mu\).
The product \((v+w)^{-1}(v+w')^{-1}\) dominates \(1/(4\max(v,w,w')^2)\), whose mean is \(I(F_\mu)/2\) by layer integration.
For the upper bound use
\[
 K(v)\le\int \frac{d\mu(w)}{\max(v,w)}
      =\int_v^\infty F_\mu(t)\,\frac{dt}{t^2}.
\]
Squaring and integrating by Tonelli gives the upper bound
\[
  2\int_{0<t<u}\frac{F_\mu(t)^2F_\mu(u)}{t^2u^2}\,dt\,du
   =2\int_0^\infty\int_0^\infty
         h(t)^2 h(te^y)e^{-y/3}\,dy\,\frac{dt}{t},
 \qquad h(t)=F_\mu(t)t^{-2/3}.
\]
Hölder's inequality for \(dt/t\) bounds the inner product in \(t\) by \(\int h^3\,dt/t=I(F_\mu)\), and integration in \(y\) proves (4).
The proof also applies by nonnegative integration when either side is infinite.

### Uniform removal of the integration endpoints and the cutoff

For every \(b\), take the input \((2/\pi)a\int_\epsilon^A W_s\,ds\,c\) or its version with \(W_s^*\).
These operators have norm at most one and converge strongly-star to \(aU_b c\) or \(aU_b^* c\), by the scalar arctangent formula and the absence of a kernel.
We show that their sliced values converge in norm with uniform tail bounds over \(b,a,c,\sigma,r\) and both original orientations.
It suffices to prove this for \(a=1\).
Fix a positive dyadic \(\eta\) and separate the output projections indexed by \(d<\eta\) from those indexed by \(d\ge\eta\).
For the first group the total squared tail is at most an absolute constant times \(\int_{v<\eta}K(v)^2\,d\mu(v)\), by (3) and orthogonality.
The layer representation used in (4) bounds this last expression by
\[
 2\int_{0<t<u}
       F(t)F(u)\min\{F(\eta),F(t)\}\,\frac{dt\,du}{t^2u^2}.
\]
It tends to zero as \(\eta\downarrow0\), uniformly over \(b\), by dominated convergence using the finite upper integral in (4) with the common envelope \(F\) in place of \(F_\mu\).
That estimate uses only the function \(h\) and \(I(F)\), and finiteness implies \(F(0+)=0\).

For \(d\ge\eta\), integration of (3) over \(0<s<\epsilon\) gives, up to an absolute constant, the bound
\[
   \sqrt{p_d}\,\eta^{-1}
       \big(\epsilon/\eta+ F(\sqrt{\epsilon})+\sqrt{\epsilon}\big).
\]
Indeed the two integrals in the factored kernel are \(\arctan(\epsilon/d)\) and \(\arctan(\epsilon/w)\); split the latter at \(w=\sqrt{\epsilon}\) and use \(d+w\ge\eta\).
For \(s>A\) the two integrals are \(\arctan(d/A)\) and \(\arctan(w/A)\), whose sum divided by \(d+w\) is at most \(1/A\).
Thus the upper-tail bound is \(2\sqrt{p_d}/A\) for every \(d\).
Both bounds can be squared and summed because \(\sum p_d=1\).
This proves uniform endpoint control by choosing \(\eta\) first and then \(\epsilon,A\).
It also proves the bound (1) for the resulting forward integrals by (3) and (4).

For the original slices, closedness now puts \(x\) in both forward domains.
The compact-integral adjoint identities pass to the limit by bounded strong-star convergence of the inputs against \(\xi,\xi^*\), giving the remaining domains and identities.
For each \(r>0\), normality identifies the integral with \(E_r x\) or \(E_r^\#x\) by the same bounded convergence of inputs and the norm convergence of outputs.
On \([\epsilon,A]\) the cutoff error for each sliced integrand is bounded by \(2s^{-2}\|g_r-1\|_{L^2(\mathcal B)}\), uniformly over the family, by (2), the contraction of the Hilbert-space trace slice, and the operator bounds \(\|R_s\|,\|L_s\|\le s^{-2}\), \(\|W_s\|\le (2s)^{-1}\).
The diffuse coordinate law gives \(g_r\to1\) in \(L^2(\mathcal B)\).
The compact-interval estimate and the uniform endpoint bounds prove the two uniform limits.

### Mixed residuals and spectral cuts

For any fixed mixed starred polynomial \(p\), Leibniz differentiation expands each \(\Phi(Dq)\) in the definition of \(B_p\) as a finite sum of left outer word multipliers times the bounded marginal generator symbols.
Thus \(B_p<\infty\), as in the [mixed polynomial resolvent estimate](Yin_C_F0285_v1.md#slices-of-resolvents-of-a-mixed-polynomial).
Set \(T=p-b\), so \(V=\Phi(Dp)\), \(V'=\Phi(Dp^*)\) for either orientation.
The hypothesis gives \(F_b(0+)=0\), hence \(|T|\) has trivial kernel and so does \(|T^*|\) by equality of the two support traces.
The same bounded strong-star polynomial approximation gives (2), with these \(V,V'\), since all derivatives of \(b\) still vanish.
Estimate (3) acquires the factor \(B_p\) from the tensor slice inequality, and the compact-interval cutoff error acquires the same factor from \(\|V(g_r-1)\|_2,\|V'(g_r-1)\|_2\le B_p\|g_r-1\|_2\).
All other endpoint estimates depend only on \(F\).
This proves the mixed residual assertion, including uniformity in the shifts and the two omitted multipliers.
For \(p=p^*\) and \(b=t1\), the absence of an atom at \(t\) gives \(1_{(-\infty,t)}(p)=(1-U_{t1})/2\).
The unit belongs to all four domains, and its forward and cutoff slices vanish, proving the assertion about mixed spectral cuts.

### Real symmetric laws at the logarithmic endpoint

In the real symmetric single-generator case at \(b=0\), \(T=Z=Z^*\), \(R_s=L_s\) and \(V=V'=1\).
Symmetry makes \(\tau(W_s)=0\), hence \(EW_s=s^2R_s\,\tau(R_s)\) is a positive function of \(|Z|\).
The scalar finite column estimate and the necessary cubic estimate give \(I(F_0)<\infty\). [Scalar columns](Yin_C_F0267_v1.md#statement) [Necessary cubic estimate](Yin_C_F0258_v1.md#statement)
Using nonnegative integration of \(s^2/((v^2+s^2)(w^2+s^2))\), whose integral is \(\pi/(2(v+w))\) by partial fractions with the continuous value at equality, the original forward integral gives
\[
                \bar E\,\operatorname{sgn}(Z)=K(|Z|).
\]
Equation (4) proves the squared norm comparison.

For \(1/3<\alpha\le2/3\) take the probability density proportional to
\[
       1_{\{0<|t|<1/2\}}\,|t|^{-1/3}\log(e/|t|)^{-\alpha}
\]
on the real line.
It belongs to \(L^3(dt)\) since \(3\alpha>1\), so the real coordinate has an [actual scalar vacuum](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate).
For \(0<s<1/2\), \(F_0(s)\) is comparable to \(s^{2/3}\log(e/s)^{-\alpha}\), using \(\log(e/t)\ge\log(e/s)\) for the upper estimate and \(s/2<t<s\) for the lower estimate.
Thus \(I(F_0)<\infty\), whereas \(\int_0^1 F_0(s)^{3/2}\,ds/s^2=\infty\).
On \(|Z|\le s\), \(R_s\ge 1/(2s^2)\), so \(\|EW_s\|_2=s^2\|R_s\|_2\tau(R_s)\ge F_0(s)^{3/2}/(4s^2)\).
Here \(\int_0^\infty\|EW_s\|_2\,ds=\infty\) even though the polar integral converges in the original forward graph.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:27 |
| status | open |
| reason | Fix the cubic criterion for uniform polar-factor domain inclusion and cutoff convergence, including its exact scalar symmetric norm comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both polar orientations of shifted coordinates or mixed polynomials and their omitted multiples under the common cubic estimate, with the spectral-cut specialization. |
| argument | [Argument](#argument) | Polar resolvent identities, orthogonal singular output projections, cubic energy, uniform endpoint bounds, and the logarithmic scalar example. |
| dependency | [Shifted resolvents](Yin_C_F0229_v1.md#argument) | Kernel-free polar decomposition, omitted-algebra approximation, unitary normal phase and opposite-tensor derivatives. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normal extensions of the original fixed-radius right slices; the same argument applies to the adjoint tuple. |
| dependency | [Polynomial adjoints](Yin_C_F0271_v1.md#exact-energy-and-affine-line-rigidity) | Both actual core adjoint identities. |
| dependency | [Mixed polynomial symbols](Yin_C_F0285_v1.md#slices-of-resolvents-of-a-mixed-polynomial) | Opposite-tensor norm bound for the derivative of a mixed starred polynomial and comparison with the absolute resolvent criterion for selfadjoint inputs. |
| dependency | [Narrow cone](Yin_C_F0272_v1.md#statement) | Common cubic concentration over all omitted shifts in the indicated marginal class. |
| dependency | [Normal residuals](Yin_C_F0270_v1.md#statement) | Cubic concentration over all shifts preserving normality. |
| dependency | [Finite columns and cubic concentration](Yin_C_F0258_v1.md#statement) | Necessary cubic estimate for shifts and its use for the scalar symmetric example. |
| dependency | [Scalar columns](Yin_C_F0267_v1.md#statement) | Finite column constant of the scalar actual coordinate. |
| dependency | [Actual real coordinate](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Actual scalar vacuum for a compactly supported real probability density in \(L^3\). |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:37 |
| status | proved |
| reason | Independent review verified the localized resolvent bounds, both actual adjoint domains and the uniform cutoff limits, including the mixed polynomial and scalar conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both polar orientations of shifted coordinates or mixed polynomials and their omitted multiples under the common cubic estimate, with the spectral-cut specialization. |
| argument | [Argument](#argument) | Polar resolvent identities, orthogonal singular output projections, cubic energy, uniform endpoint bounds, and the logarithmic scalar example. |
| dependency | [Shifted resolvents](Yin_C_F0229_v1.md#argument) | Kernel-free polar decomposition, omitted-algebra approximation, unitary normal phase and opposite-tensor derivatives. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normal extensions of the original fixed-radius right slices; the same argument applies to the adjoint tuple. |
| dependency | [Polynomial adjoints](Yin_C_F0271_v1.md#exact-energy-and-affine-line-rigidity) | Both actual core adjoint identities. |
| dependency | [Mixed polynomial symbols](Yin_C_F0285_v1.md#slices-of-resolvents-of-a-mixed-polynomial) | Opposite-tensor norm bound for the derivative of a mixed starred polynomial and comparison with the absolute resolvent criterion for selfadjoint inputs. |
| dependency | [Narrow cone](Yin_C_F0272_v1.md#statement) | Common cubic concentration over all omitted shifts in the indicated marginal class. |
| dependency | [Normal residuals](Yin_C_F0270_v1.md#statement) | Cubic concentration over all shifts preserving normality. |
| dependency | [Finite columns and cubic concentration](Yin_C_F0258_v1.md#statement) | Necessary cubic estimate for shifts and its use for the scalar symmetric example. |
| dependency | [Scalar columns](Yin_C_F0267_v1.md#statement) | Finite column constant of the scalar actual coordinate. |
| dependency | [Actual real coordinate](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Actual scalar vacuum for a compactly supported real probability density in \(L^3\). |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0296_v1.md#finding) | The entire fixed candidate, all nine direct dependency interfaces, uniform endpoint estimates, mixed spectral cuts and the logarithmic endpoint example. |
