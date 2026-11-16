---
author: Yin
---

# Singular-value atoms of a compressed normal coordinate

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded and normal with diffuse trace law \(\mu\) in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Assume the [relative derivation hypotheses](Yin_C_F0309_v1.md#statement): on a weakly dense represented unital starred algebra an outer derivation \(\delta\) has \(\delta Z=1\otimes1\) and an actual adjoint vacuum.
Let \(p\) be a projection of trace \(0<t<1\) killed by \(\delta\), either on this algebra or in the von Neumann algebra of its killed starred coefficients.
Use the normalized trace \(\tau_p=\tau/t\) on \(pMp\).
Put \(B=p(Z-\lambda)p\) for \(\lambda\in\mathbb C\) and let \(u\) be the polar unitary of \(Z-\lambda\), which has trivial kernel by diffuseness.

For \(a>0\) let \(r_a=1_{\{a\}}(|Z-\lambda|)\) in \(M\).
The right and left singular atom projections in the corner are the following meets in \(M\):
\[
  e_a=1_{\{a\}}(|B|)=p\wedge r_a\wedge u^*pu,\qquad
  q_a=1_{\{a\}}(|B^*|)=p\wedge r_a\wedge upu^*=u e_a u^*.
                                                               \tag{1}
\]
In particular \(\tau_p(e_a)\le\mu(\{|z-\lambda|=a\})/t\).
The total mass of the atomic part of the corner singular law satisfies
\[
                 \sum_{a\ge0}\tau_p(1_{\{a\}}(|B|))
                    \le \frac{\max(2t-1,0)}{t}.                \tag{2}
\]
At \(a=0\) the projection in this sum is taken in the corner.
Thus every scalar shift has a diffuse singular law for \(t\le1/2\), including at the trace in the [projection reformulation of the slice problem](Yin_C_F0308_v1.md#statement).
Every proper compression under these hypotheses has a nonzero nonatomic part, excluding exact realizations of every purely atomic modulus, including the two-point modulus, at any finite vacuum cost.
The bound is attained when \(\mu\) is supported on one circle centered at \(\lambda\), with the possible atom at its radius.
Such models exist for every \(0<t<1\).

## Argument

### Restricting the derivative to an atom

We use the [ambient graph construction](Yin_C_F0309_v1.md#derivation-and-vacuum-on-the-compressed-generated-algebra) to differentiate words in \(p,Z,Z^*\), also for a projection in the omitted von Neumann algebra.
The derivation is closable, and its value at \(Z^*\) in the opposite tensor representation \(\Phi(b\otimes c)=b\otimes c^{\rm op}\) is the unitary marginal phase \(k(z,v)=(\bar z-\bar v)/(z-v)\).
Thus
\[
 k(Z\otimes1-1\otimes Z^{\rm op})=Z^*\otimes1-1\otimes(Z^*)^{\rm op}.
                                                               \tag{3}
\]
Outer multiplication on the two legs is left multiplication in \(M\bar\otimes M^{\rm op}\).

For a bounded selfadjoint word \(x\) in this algebra and \(s\in\mathbb R\), put \(E_s=1_{\{s\}}(x)\).
Then \(E_s\cdot\delta x\cdot E_s=0\).
To see this, take \(h_n(v)=(v-s)/(1+n(v-s)^2)\), which converges uniformly to zero.
The coarse derivative of \(h_n(x)\) is the divided difference of \(h_n\) in the two outer spectral variables of \(x\), applied to \(\delta x\), with value \(h_n'(v)\) on the diagonal.
Indeed this holds for polynomials by the product rule, and each fixed \(h_n\) has polynomial approximants converging together with their first derivatives uniformly on a compact interval containing the spectrum.
One obtains these approximants by approximating the derivative and integrating.
The divided differences have absolute value at most one and converge at every pair to the indicator of \(\{(s,s)\}\), including on the diagonal.
Bounded convergence for the joint spectral measure of \(\delta x\) and closability prove the assertion.

Fix \(a>0\) with \(e=e_a\ne0\), put \(q=q_a\), and write \(w=Be/a\).
Then \(w^*w=e,\ ww^*=q,\ Be=aw,\ eB^*=aw^*\).
Apply the preceding calculation to \(x=B^*B\) and \(s=a^2\) in the ambient algebra, where the positive spectral projection is still \(e\).
Since \(\Phi\delta B=p\otimes p^{\rm op}\) and \(\Phi\delta B^*=(p\otimes p^{\rm op})k\), differentiation gives
\[
  (e\otimes w^{\rm op})\,k=-w^*\otimes e^{\rm op},\qquad
  (e\otimes q^{\rm op})\,k=-w^*\otimes(w^*)^{\rm op}.
                                                               \tag{4}
\]
The second identity follows by left multiplication with \(e\otimes(w^*)^{\rm op}\).

Multiply the second identity on the right by \(Z\otimes1-1\otimes Z^{\rm op}\), apply (3), and multiply on the right by \((1-p)\otimes p^{\rm op}\).
The terms with \(e(1-p)\) or \(w^*(1-p)\) vanish, giving
\[
             eZ^*(1-p)\otimes q^{\rm op}
              =-w^*Z(1-p)\otimes(w^*)^{\rm op}.               \tag{5}
\]
The vectors \(q,w^*\) are linearly independent.
Otherwise \(w^*=c q\) for a scalar of modulus one, so \(e=q\) and \(Be=a\bar c e\), contradicting the [zero-kernel bound for all corner scalar shifts](Yin_C_F0309_v1.md#statement).
Separating the two second legs of (5) by Hilbert space functionals gives \((1-p)Ze=0\) and \((1-p)Z^*w=0\).
Consequently \((Z-\lambda)e=aw\) and \((Z-\lambda)^*w=ae\), the latter using \(B^*w=ae\).
It follows that \(e\le r_a\) and \(w=ue\), whence \(e\le u^*pu\).

Conversely, on the range of \(p\wedge r_a\wedge u^*pu\), the operator \(Z-\lambda\) acts by \(au\), with output in the range of \(p\).
Its adjoint sends this output back to \(a^2\) times the input.
Thus the meet is contained in \(e_a\), including when \(e_a=0\).
Conjugating the right projection by \(u\), which commutes with \(r_a\) by normality, gives the left projection and proves (1).

### The rectangular operator has maximal rank

All the positive right atom projections for a fixed \(\lambda\) lie in the kernel of \(X=(1-p)Zp\), since (5) gave \((1-p)Ze_a=0\).
We compute the part of that kernel in \(p\).
Let \(e_0'\le p\) and \(f_0'\le1-p\) be the right and left kernel projections of \(X\) as a rectangular operator between these two projections.
Its ambient right and left kernel projections are \(1-p+e_0'\) and \(p+f_0'\), respectively.

For \(s>0\) put \(R_s=(X^*X+s)^{-1}\), \(L_s=(XX^*+s)^{-1}\), \(V_s=XR_s\).
Writing \(K_X=\Phi\delta X\) and \(K_{X^*}=\Phi\delta X^*\), the [resolvent product rule](Yin_C_F0229_v1.md#argument) gives
\[
  \Phi\bar\delta(sV_s)
   =(sL_s\otimes(sR_s)^{\rm op})K_X
        -(\sqrt{s}V_s\otimes(\sqrt{s}V_s)^{\rm op})K_{X^*}.
\]
For this word \(X\) the inverse rule follows by the same geometric expansion at each fixed \(s\), whose differentiated terms are summable in coarse norm.
The input \(sV_s\) has norm at most \(\sqrt{s}/2\), while \(sL_s,sR_s\) converge boundedly strongly-star to the two ambient kernel projections.
The factors \(\sqrt{s}V_s\) converge boundedly strongly-star to zero by polar decomposition and the bounded pointwise convergence of \(v\mapsto\sqrt{s}v/(v^2+s)\), including at zero.
The two outer legs consequently converge strongly as multipliers on the coarse space.
Closedness shows that the left and right kernel projections annihilate \(K_X\) when placed on its respective outer legs.
Here \(K_X=(1-p)\otimes p^{\rm op}\), so \(f_0'\otimes(e_0')^{\rm op}=0\).
One rectangular kernel therefore vanishes, and the polar decomposition gives \(t-\tau(e_0')=1-t-\tau(f_0')\).
It follows that \(\tau(e_0')=\max(2t-1,0)\).
The sum of the mutually orthogonal right atom projections is dominated by \(e_0'\), with the zero singular atom already excluded by the corner scalar-shift bound.
This proves (2).

If \(r_a=1\), the rectangular column is \(X=a(1-p)up\) and its right kernel within \(p\) is \(p\wedge u^*pu=e_a\).
Every other positive atom vanishes by (1).
For each trace \(t\), take a Haar unitary \(Z\) freely independent of a projection \(p\) of trace \(t\) and set \(\lambda=0\).
The [free-product vacuum computation](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) gives the Haar Laurent derivation with \(\delta Z=1\otimes1\) and vacuum \(Z\); extending by zero on the projection algebra preserves that vacuum by testing centered reduced words.
This supplies equality in (2) for every \(t\).
The atom restriction gives no bound on the slice norm for general mixed polynomial inputs.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:41 |
| status | open |
| reason | Fix the circle projection formula, sharp total atomic mass bound and trace-half diffuseness for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Right and left singular atom projections for every scalar shift, sharp bound on their total mass, trace-half diffuseness and exclusion of purely atomic moduli. |
| argument | [Argument](#argument) | Atom differentiation, marginal phase and opposite-leg calculation, rectangular kernel rank and sharp circle examples. |
| dependency | [Ambient graph and phase](Yin_C_F0309_v1.md#derivation-and-vacuum-on-the-compressed-generated-algebra) | Closability, extension to a killed von Neumann coefficient and the forced marginal phase before inner corner compression. |
| dependency | [Corner scalar-shift inequality](Yin_C_F0309_v1.md#statement) | Trivial right kernels of every scalar shift in the corner. |
| dependency | [Resolvent graph product rule](Yin_C_F0229_v1.md#argument) | Fixed-radius geometric inversion and opposite-leg product rule used on the rectangular column. |
| dependency | [Free-product vacuum](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual Laurent Haar vacuum and its extension by zero across the free projection algebra in the sharp examples. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:49 |
| status | proved |
| reason | Adopt the sharp atom formula after independent verification of the graph argument, rectangular ranks and examples. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Right and left singular atom projections for every scalar shift, sharp bound on their total mass, trace-half diffuseness and exclusion of purely atomic moduli. |
| argument | [Argument](#argument) | Atom differentiation, marginal phase and opposite-leg calculation, rectangular kernel rank and sharp circle examples. |
| dependency | [Ambient graph and phase](Yin_C_F0309_v1.md#derivation-and-vacuum-on-the-compressed-generated-algebra) | Closability, extension to a killed von Neumann coefficient and the forced marginal phase before inner corner compression. |
| dependency | [Corner scalar-shift inequality](Yin_C_F0309_v1.md#statement) | Trivial right kernels of every scalar shift in the corner. |
| dependency | [Resolvent graph product rule](Yin_C_F0229_v1.md#argument) | Fixed-radius geometric inversion and opposite-leg product rule used on the rectangular column. |
| dependency | [Free-product vacuum](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual Laurent Haar vacuum and its extension by zero across the free projection algebra in the sharp examples. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0319_v1.md#whole-proof-finding) | Complete fixed statement, argument and direct dependency interfaces. |
