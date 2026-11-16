---
author: Yin
---

# Singular values of a normal coordinate compressed by an omitted projection

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be a bounded normal operator with diffuse marginal law \(\mu\) in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
On a weakly dense represented unital starred algebra containing \(Z,p\), suppose that an outer derivation \(\delta\) has \(\delta Z=1\otimes1\), \(\delta p=0\), and actual vacuum \(\xi=\delta^*(1\otimes1)\), where \(p\) is a projection with \(0<t=\tau(p)<1\).
The same conclusions apply if \(p\) belongs to the von Neumann algebra of omitted starred coefficients killed by \(\delta\), as specified in the graph argument below.
Set \(T=pZp\), use the probability trace \(\tau_p=t^{-1}\tau\) on \(pMp\), and let \(W=W^*(T)\) be generated in the corner with unit \(p\).
Write \(\mathbb E_W:pMp\to W\) for the trace-preserving conditional expectation.

There is an outer derivation \(D\) on the represented starred polynomial algebra of \(T\) into \(L^2(W,\tau_p)\otimes_2 L^2(W,\tau_p)\) satisfying
\[
   DT=p\otimes p,\qquad
   \xi_T=D^*(p\otimes p)=t^{-1}\mathbb E_W(p\xi p),\qquad
   \|\xi_T\|_{2,\tau_p}\le t^{-3/2}\|p\xi p\|_{2,\tau}.
\]
Under the identification \(a\otimes b\mapsto a\otimes b^{\rm op}\) the value at \(T^*\) is a contraction in \(W\bar\otimes W^{\rm op}\).
More precisely, it equals \((\Psi\otimes\Psi^{\rm op})(k)\), where \(\Psi(f)=\mathbb E_W(p f(Z)p)\) for bounded marginal functions and \(k(z,w)=(\bar z-\bar w)/(z-w)\) off the null diagonal.
Consequently, for every \(\lambda\in\mathbb C,\ r>0\),
\[
       \tau_p(1_{[0,r]}(|T-\lambda p|))^2
           \le\pi r\|\xi_T\|_{2,\tau_p}
           \le\pi r t^{-3/2}\|p\xi p\|_{2,\tau}.                       \tag{1}
\]
In particular if \(|pZp|\) has the [two-point singular law](Yin_C_F0225_v1.md#statement) with mass \(1/2\) each at \(\varepsilon,1\), \(0<\varepsilon\le1/2\), then \(\|\xi\|_{2,\tau}\ge t^{3/2}/(4\pi\varepsilon)\).
Thus exact realizations of these laws on corners of fixed positive trace cannot have uniformly bounded distinguished vacua as \(\varepsilon\downarrow0\).
The bound concerns these compressions and their singular laws; it supplies no general upper bound on the original slice cost.

## Argument

### Derivation and vacuum on the compressed generated algebra

The coordinating agent proposed testing the two-point construction through the starred value of the induced derivative.
By the [normal commutation identity](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability), \(\delta Z^*=k\) in the marginal coarse space, since the two outer spectral variables have a product-null diagonal.
The actual vacuum and the polynomial tensor adjoint formula make \(\delta\) closable. [Actual adjoint formula](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001)
If \(p\) is only in the omitted von Neumann algebra, approximate it boundedly strongly-star by elements of the killed starred coefficient algebra.
Their derivatives and adjoint derivatives vanish, and for each fixed word in \(p,Z,Z^*\) the bounded outer multipliers converge strongly on coarse tensors.
This gives graph approximation of every such word with the indicated product rule and \(\bar\delta p=0\), as in the [omitted graph argument](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra).
Write \(\delta\) for this restriction as well.

For a corner polynomial \(x\) in \(T,T^*\), \(\delta x=p\cdot\delta x\cdot p\) follows from \(x=pxp\).
Insert \(p\) on the inner side of each leg, sending \(a\otimes b\) to \(ap\otimes pb\), and identify the resulting vector in the normalized corner coarse space.
This insertion commutes with outer multiplication and gives a derivation on the corner polynomial algebra.
Next apply the Hilbert projections onto \(L^2(W,\tau_p)\) on both legs; these are \(W\)-bimodular, so the result is a derivation \(D\) on the same represented algebra.
At \(T\) its value is \(p\otimes p\).
At \(T^*\), in the opposite tensor representation the four corner multiplications give \((p\otimes p^{\rm op})k(p\otimes p^{\rm op})\).
Applying the trace-preserving conditional expectation from the corner spatial tensor algebra to \(W\bar\otimes W^{\rm op}\) gives the same Hilbert projections and has operator norm one.
Its result is the stated contraction, equivalently the indicated product map on the marginal spatial tensor algebra, by equality on simple tensors and normality.

The Hilbert projections preserve the corner double trace.
By global traciality and the two outer supports, the inner insertions preserve the global double trace on \(\delta x\).
These assertions pass from simple tensors by trace Hilbert continuity.
It follows that
\[
     (\tau_p\otimes\tau_p)(Dx)=t^{-2}(\tau\otimes\tau)(\delta x)
       =t^{-2}\langle \xi,x\rangle_{\tau}
       =\langle t^{-1}\mathbb E_W(p\xi p),x\rangle_{\tau_p}.
\]
The equality gives the actual Hilbert adjoint domain and vacuum on the dense represented corner core.
The corner Hilbert norm of an element is \(t^{-1/2}\) times its inherited norm, proving the displayed estimate.

### A contraction at the starred generator

Put \(B=T-\lambda p\), and let \(\nu\) be the law of \(|B|\) under \(\tau_p\).
Write \(K\) for the spatial contraction at \(B^*\) just proved.
For \(s>0\) use \(R=(B^*B+sp)^{-1}\), \(L=(BB^*+sp)^{-1}\) and \(V=BR=LB\).
On polynomial approximants the product rule \(DB=p\otimes p,\ DB^*=K\) gives the [resolvent derivative formula](Yin_C_F0229_v1.md#argument)
\[
                  DV=sL\otimes R^{\rm op}-(V\otimes V^{\rm op})K .
\]
For the vacuum test one may take a geometric series for \(R\) with ratio \(p-(B^*B+sp)/c\) for \(c>\|B\|^2+s\).
Its differentiated tails converge in coarse Hilbert norm since the ratio has norm strictly below one; this justifies the identity in the graph limit and the corresponding vacuum pairing.
The left and right singular laws of \(B\) are equal under the finite trace including at zero, by polar decomposition.
Using tracial Hölder for the product with \(K\), only its contraction bound is needed to deduce
\[
  s\left(\int\frac{d\nu(v)}{v^2+s}\right)^2
   -\left(\int\frac{v\,d\nu(v)}{v^2+s}\right)^2
          \le \operatorname{Re}\langle\xi_T,V\rangle_{\tau_p}.
\]
Integrate at \(s=u^2\) against \(2\,du/\pi\) over \(r\le u\le R_0\).
The polar decomposition bounds the norm of \((2/\pi)\int_r^{R_0}B(B^*B+u^2p)^{-1}du\) by one, since its scalar radial integral is bounded by \((2/\pi)\int_0^\infty v/(v^2+u^2)\,du\le1\).
Let \(\Lambda_u(v,w)\) denote the nonnegative divided difference of \(v\mapsto\arctan(v/u)\), extended on the diagonal by the derivative.
The scalar kernel at \(v,w\ge0\) on the left before integration is
\[
    \frac{u^2-vw}{(u^2+v^2)(u^2+w^2)}
                  =-\frac{d}{du}\Lambda_u(v,w).
\]
This identity includes diagonal and zero values by continuity for \(u>0\).
Sending \(R_0\to\infty\), using \(\Lambda_{R_0}\le1/R_0\), yields
\(\iint\Lambda_r\,d\nu^2\le(\pi/2)\|\xi_T\|_{2,\tau_p}\).
On \([0,r]^2\) the mean-value theorem gives \(\Lambda_r\ge1/(2r)\), proving (1).
Taking \(\lambda=0,\ r=\varepsilon\) in the two-point example gives the claimed lower bound; the same inequality with \(r\downarrow0\) excludes a zero singular atom at every scalar shift.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:27 |
| status | open |
| reason | Fix the omitted-projection compression and the resulting obstruction to a small-vacuum realization of the two-point singular law. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized compressed vacuum, spatial contraction at the starred generator, uniform scalar-shift mass bound and two-point consequence. |
| argument | [Argument](#argument) | Outer and inner corner projections, normalized trace calculation, product expectation and signed arctangent resolvent estimate. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Forced starred value on the diffuse marginal and its spatial norm. |
| dependency | [Actual adjoint formula](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Closability from the vacuum and algebraic tensor domain. |
| dependency | [Omitted graph actions](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Extension to omitted von Neumann projections and zero derivatives. |
| dependency | [Resolvent singular-mass estimate](Yin_C_F0229_v1.md#argument) | Differentiated inverse product rule, signed polar integral, arctangent kernel and numerical mass bound. |
| dependency | [Two-point modulus](Yin_C_F0225_v1.md#statement) | Exact singular law of the comparison family with bounded intrinsic vacuum and increasing bounded-dual cost. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:32 |
| status | proved |
| reason | Adopt the normalized compression formula and singular-mass estimate after independent review of the complete proof and its five direct inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized compressed vacuum, spatial contraction at the starred generator, uniform scalar-shift mass bound and two-point consequence. |
| argument | [Argument](#argument) | Outer and inner corner projections, normalized trace calculation, product expectation and signed arctangent resolvent estimate. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Forced starred value on the diffuse marginal and its spatial norm. |
| dependency | [Actual adjoint formula](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Closability from the vacuum and algebraic tensor domain. |
| dependency | [Omitted graph actions](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Extension to omitted von Neumann projections and zero derivatives. |
| dependency | [Resolvent singular-mass estimate](Yin_C_F0229_v1.md#argument) | Differentiated inverse product rule, signed polar integral, arctangent kernel and numerical mass bound. |
| dependency | [Two-point modulus](Yin_C_F0225_v1.md#statement) | Exact singular law of the comparison family with bounded intrinsic vacuum and increasing bounded-dual cost. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0318_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
