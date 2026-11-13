---
author: Yin
---
# A uniform singular-value mass bound for shifts of a normal coordinate by its omitted algebra

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a bounded normal generating tuple with [actual ACSY](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra with faithful normal probability trace.
Fix \(i\), write \(N=W^*(X_j:j\ne i)\), and let \(\xi=\delta_i^*(1\otimes1)\) be the actual vacuum.
For every \(b\in N\), including nonnormal \(b\), put \(T=X_i-b\) and \(P=|T|\).
Then \(T,T^*\) have zero kernel, and
\[
   \tau(1_{[0,r]}(|T|))^2\le\pi r\|\xi\|_2\qquad(r>0).                \tag{1}
\]
The same bound holds for \(|T^*|\).
For \(0<a<1/2\) this gives \(\tau(|T|^{-a})\le(\pi\|\xi\|_2)^a/(1-2a)\) uniformly over \(b\).
More precisely let \(T=UP\) be its unitary polar decomposition, \(\mu\) the law of \(P\), and \(k=\Phi(\delta_i X_i^*)\) the unitary marginal phase in the coarse tensor algebra identified below.
Let \(m(v,w)\) represent the conditional expectation of \((1\otimes U^{\rm op})k(U\otimes1)\) onto \(W^*(P)\bar\otimes W^*(P)^{\rm op}\).
Define
\[
 J(r)=\frac2\pi\iint
 \frac{\arctan(v/r)-\arctan(w/r)}{v-w}\,d\mu(v)d\mu(w)
\]
with the derivative at equality.
Then \(J(r)\ge0\), its limit as \(r\downarrow0\) exists, and
\[
 \lim_{r\downarrow0}J(r)
 +\iint\frac{1-{\rm Re}\,m(v,w)}{v+w}\,d\mu(v)d\mu(w)
       ={\rm Re}\langle\xi,U\rangle\le\|\xi\|_2 .                      \tag{2}
\]
These conclusions concern the singular law before conditional expectation onto \(N\).
The [column obstruction](Yin_C_F0211_v1.md#statement) involves sums of cubed masses divided by squared radii.
The bound (1) alone leaves that obstruction open.

## Argument

Write \(\delta=\delta_i\) and identify the coarse Hilbert space with \(L^2(\mathcal B)\), where \(\mathcal B=M\bar\otimes M^{\rm op}\), by the linear unitary \(\Phi(a\otimes c)=a\otimes c^{\rm op}\).
The outer operations \(a\cdot K\cdot c\) then correspond to left multiplication by \(a\otimes c^{\rm op}\).
The [normal marginal phase](Yin_C_F0076_v1.md#statement) gives \(k=\Phi(\delta X_i^*)\) unitary in \(\mathcal B\).
The [omitted-algebra graph property](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) puts \(T,T^*\) in the closed graph, with values \(1\otimes1,\Phi^{-1}k\).
Every star polynomial in \(T,T^*\) is in this graph with its product rule.
Indeed approximate \(b\) strongly-star on a bounded ball by omitted polynomials using [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) and norm density of the polynomial core.
Their derivatives and those of their adjoints are zero.
In a fixed polynomial the outer factors stay bounded and converge strongly on the tensor Hilbert space, which proves graph convergence.

For \(s>0\) write \(R_s=(T^*T+s)^{-1}\), \(L_s=(TT^*+s)^{-1}\), \(W_s=TR_s=L_sT\).
In particular
\[
 \Phi(\bar\delta W_s)
   =s L_s\otimes R_s^{\rm op}-(W_s\otimes W_s^{\rm op})\,k .         \tag{3}
\]
To justify the inverse in the graph, for \(C>\|T\|^2+s\) expand \(R_s=C^{-1}\sum_{n\ge0}(1-(T^*T+s)/C)^n\).
The operator in parentheses has norm \(q<1\) and the differentiated series converges in coarse norm by the summable bound by a constant times \(nq^{n-1}\).
The Leibniz expansion of the series gives \(\bar\delta R_s=-R_s\bar\delta(T^*T)R_s\).
Applying the product rule to \(TR_s\) by the same polynomial approximations and using \(1-TR_sT^*=s L_s\) gives (3).

Let \(\mu\) be the singular-value law of \(T\), counting any kernel mass.
In a finite tracial algebra \(|T|\) and \(|T^*|\) have identical laws by polar decomposition and equality of the trace of the support projections.
Use the actual vacuum identity on \(W_s\).
By the differentiated resolvent formula, tracial Hölder's inequality, \(\|k\|=1\), and the product trace,
\[
 s\left(\int \frac{d\mu(v)}{v^2+s}\right)^2
 \le {\rm Re}\langle\xi,W_s\rangle+
          \left(\int \frac{v\,d\mu(v)}{v^2+s}\right)^2 .             \tag{4}
\]
Indeed the absolute value of the phase term obtained by tracing (3) is bounded by the trace norm of \(W_s\otimes W_s^{\rm op}\), equal to \(\tau(|W_s|)^2\).
Inequality (4) keeps the signed real vacuum pairing.

First multiply the scalar inequality by \(s\) and take \(s\downarrow0\).
The left side tends to \(\mu(\{0\})^2\), and \(s\|W_s\|\le\sqrt s/2\).
The integrand \(\sqrt{s}\,v/(v^2+s)\) is at most \(1/2\) and tends pointwise to zero, including at \(v=0\).
Dominated convergence gives zero on the right.
Thus \(T\) has zero kernel, as does its adjoint.

Set \(t=\sqrt s\) and integrate the difference of the two scalar terms in that inequality against \(2\,dt/\pi\) over \([\lambda,R]\), with \(0<\lambda<R\).
For \(v,w>0\) the scalar double kernel is
\[
 \frac{t^2-vw}{(t^2+v^2)(t^2+w^2)}
  =-\frac{d}{dt}\left(\frac{\arctan(v/t)-\arctan(w/t)}{v-w}\right).
\]
At \(v=w\) its primitive on the right before differentiation is \(t/(t^2+v^2)\).
These formulas follow by differentiating and agree by continuity on the diagonal.
All integrands on each bounded integration interval are bounded.
Writing \(\Psi_\lambda(v,w)\) for the positive divided difference of \(v\mapsto\arctan(v/\lambda)\) at \(v,w\), the left integral therefore equals \((2/\pi)\iint(\Psi_\lambda-\Psi_R)\,d\mu^2\).
The remaining vector integral on the right is bounded by \(\|\xi\|_2\), since the polar decomposition \(T=U|T|\) gives
\[
 \left\|\frac2\pi\int_\lambda^R W_{t^2}\,dt\right\|
  \le\sup_{v>0}\frac2\pi\int_0^\infty\frac{v\,dt}{v^2+t^2}=1 .
\]
As \(R\uparrow\infty\), \(\Psi_R\le1/R\).
It follows that \(\iint\Psi_\lambda\,d\mu^2\le(\pi/2)\|\xi\|_2\).
For \(0\le v,w\le\lambda\), the real mean-value theorem gives \(\Psi_\lambda(v,w)\ge1/(2\lambda)\).
In particular \(\mu([0,\lambda])^2\le \pi\lambda\|\xi\|_2\).

For \(0<a<1/2\) layer integration gives \(\tau(P^{-a})=\int_0^\infty a r^{-a-1}\mu([0,r])\,dr\).
Using the smaller of one and \(\sqrt{\pi r\|\xi\|_2}\) and splitting at \(r=1/(\pi\|\xi\|_2)\) yields the stated uniform fractional moment.
The vacuum is nonzero by pairing the generator with it.

### The integrated phase defect

The zero-kernel conclusion and finiteness of \(M\) make \(U\) unitary.
Put \(g_t(v)=v/(t^2+v^2)\).
Then \(W_{t^2}=Ug_t(P)\), and the reversed multiplication in the opposite algebra and cyclicity of the product trace give
\[
  (\tau\otimes\tau^{\rm op})((W_{t^2}\otimes W_{t^2}^{\rm op})k)
      = \iint g_t(v)g_t(w)m(v,w)\,d\mu(v)d\mu(w).
\]
The tensor conditional expectation is contractive and preserves the trace, so \(|m|\le1\) and \(1-{\rm Re}\,m\) is nonnegative.
Consequently the real part of the exact vacuum pairing in the differentiated resolvent formula splits into the signed scalar difference integrated above and the nonnegative term with \(g_t(v)g_t(w)(1-{\rm Re}\,m)\).
Integrating over \([\lambda,R]\) with factor \(2/\pi\), the signed part is \(J(\lambda)-J(R)\).
As \(R\uparrow\infty\) and \(\lambda\downarrow0\), \((2/\pi)\int_\lambda^R W_{t^2}\,dt\to U\) in \(L^2\) by bounded convergence in the polar representation.
The nonnegative term increases to the stated integral because for \(v,w>0\)
\[
       \frac2\pi\int_0^\infty
        \frac{vw\,dt}{(v^2+t^2)(w^2+t^2)}=\frac1{v+w}.
\]
Partial fractions give the formula for \(v\ne w\), and continuity gives it at equality.
Since \(J(R)\le 2/(\pi R)\) and \(J(\lambda)\ge0\), the defect integral is finite.
The integrated equality now gives the limit of \(J(\lambda)\) and proves the identity in the statement.
An endpoint inverse half-moment and the exponent \(2/3\) relevant to the single-projection column obstruction do not follow from the mass estimate here.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:42 |
| status | open |
| reason | Fixed the singular-value mass bound uniformly over omitted shifts and the integrated identity with its nonnegative phase defect. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform unconditioned singular mass, fractional inverse moments and the polar phase-defect identity. |
| argument | [Argument](#argument) | Closed graph resolvent, exact vacuum pairing, positive arctangent divided differences and integrated defect. |
| dependency | [Normal coordinate phase](Yin_C_F0076_v1.md#statement) | The actual starred value is unitary in the marginal tensor algebra and the derivation is closable. |
| dependency | [Omitted-algebra graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded coefficients of omitted coordinates and their adjoints have zero derivative in the closed graph. |
| dependency | [Kaplansky approximation](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strongly-star approximants to the shift from omitted-coordinate star polynomials. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:45 |
| status | proved |
| reason | Adopt the uniform singular-value estimate and exact integrated polar identity after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform unconditioned singular mass, fractional inverse moments and the polar phase-defect identity. |
| argument | [Argument](#argument) | Closed graph resolvent, exact vacuum pairing, positive arctangent divided differences and integrated defect. |
| dependency | [Normal coordinate phase](Yin_C_F0076_v1.md#statement) | The actual starred value is unitary in the marginal tensor algebra and the derivation is closable. |
| dependency | [Omitted-algebra graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded coefficients of omitted coordinates and their adjoints have zero derivative in the closed graph. |
| dependency | [Kaplansky approximation](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strongly-star approximants to the shift from omitted-coordinate star polynomials. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0238_v1.md#whole-proof-finding) | Closed resolvent identity, both kernel exclusions, arctangent constants, uniform subcritical inverse moments and the integrated polar phase defect. |
