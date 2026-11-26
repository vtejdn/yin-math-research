---
author: Yin
---

# A contractivity test on one spiral for rational affiliated operators

## Statement

Let \(G\) be a finitely generated discrete group, \(A=\mathbb CG\), \(M=\mathcal N(G)\), and \(U=L^0(M)\).
Write \(D\) and \(R\) for the division closure and the \(*\)-regular closure of \(A\) in \(U\).
For an affiliated operator \(u\), let \(P_u\in M_2(M)\) project onto its graph and put \(V_u=2P_u-I_2\).
Use one central variable \(z\) and the rational power series ring
\[
 O=\operatorname{Div}_{U((z))}(A[z])\cap U[[z]] .
\]
Each entry of a matrix over \(O\) is given by a scalar rational expression.
The expressions can be evaluated in \(U\) outside a countable subset of the complex plane. [Ordinary evaluation](Yin_C_A0143_v1.md#statement)

Then \(u\in D\) if and only if there exists \(f\in M_2(O)\) with \(f(0)=V_u\) such that
\[
                 \|f(t\exp(i\log t))\|\le1
                 \qquad (0<t<\varepsilon)
\]
outside a countable exceptional set, for some \(\varepsilon>0\).
Here \(f(0)\) is the formal constant coefficient, and the norm inequality requires the evaluated matrix to be a bounded contraction.
The criterion uses one matrix of scalar expressions and one prescribed curve.
It applies to unbounded \(u\) and requires no local commutation test or bounds on expression size.

There is also a sharp probability threshold.
For a fixed lift \(f\) and radius \(r>0\), let \(a_f(r)\) be the probability that \(f(re^{i\theta})\) is defined and is a contraction, with \(\theta\) uniform on \([0,2\pi)\).
Then
\[
 \begin{aligned}
 u\in D &\quad\Longleftrightarrow\quad
      \text{some lift of } V_u \text{ has } \limsup_{r\downarrow0}a_f(r)>1/2,\\
 u\in R &\quad\Longleftrightarrow\quad
      \text{some lift of } V_u \text{ has } \limsup_{r\downarrow0}a_f(r)\ge1/2 .
 \end{aligned}
\]
For \(u\in R\setminus D\) the construction below attains the limit \(1/2\).

For a set \(\Theta\subset\mathbb R\) of directions, impose the same norm test on all the rays \(z=t e^{i\theta}\), \(\theta\in\Theta\), \(0<t<\varepsilon\), outside a countable set of complex parameters.
The resulting condition characterizes \(D\) if, for every integer \(m\ge1\), the set
\[
                 \{e^{im\theta}:\theta\in\Theta\}
\]
is contained in no closed semicircle.
If it is contained in a closed semicircle for some \(m\), the condition characterizes \(R\), equivalently solvability of [the unrestricted finite-rank equation (1)](Yin_C_A0131_v1.md#statement).
Every finite set of straight rays gives this latter test.
These conclusions identify the two rings detected for each group, including when the rings coincide.
Whether they always coincide for torsion-free \(G\) remains open.

## Argument

### A unitary constant coefficient and the first varying term

For a finite matrix of fixed rational expressions the [Laurent asymptotics in measure](Yin_C_A0143_v1.md#statement) hold jointly off a countable set.
Suppose \(f\) has unitary constant coefficient \(V\), and let \(Cz^m\), \(m\ge1\), be its first nonconstant term.
For any allowed sequence \(z_j\to0\) with \(z_j/|z_j|\to\omega\), multiplication and adjoint in the affiliated algebra give
\[
 \frac{I-f(z_j)^*f(z_j)}{|z_j|^m}
          \ \longrightarrow\ -2\operatorname{Re}(\omega^m V^*C)
                      \quad\text{in measure}.
\]
The positive cone is closed in measure.
Indeed, a selfadjoint limit having a nonzero spectral projection on a bounded interval strictly below zero would have a nonzero intersection of that projection with a cut where the difference from a positive approximant is uniformly small.
The quadratic forms on this intersection would have opposite signs.
This uses the [finite-tracial measure topology](../audits/literature/FK86/Yin_U001.md#measure-topology-interface).

If the \(f(z_j)\) are contractions, the displayed limit is positive.
On the spiral every point of the unit circle is a limiting direction, even after countably many points are removed.
Indeed every open angular interval is visited on open parameter intervals arbitrarily near zero.
On a prescribed straight ray the limiting direction is that ray itself.
In either case suppose the resulting values of \(\omega^m\) fit in no closed semicircle.
Writing \(T=V^*C\), the inequalities \(\operatorname{Re}(\omega^m T)\le0\) force \(T=0\).
For details, \(d=(I+T^*T+TT^*)^{-1/2}\) is a positive bounded affiliated unit and \(dTd\) is bounded.
For each Hilbert-space vector \(\xi\), the numerical value \(\langle \xi,dTd\,\xi\rangle\), with the inner product linear in the second entry, satisfies all the same rotated real-part inequalities.
A nonzero such value puts all the rotations in a closed semicircle.
Polarization now gives \(dTd=0\) and invertibility of \(d\) gives \(C=0\), contradicting the choice of the first term.
Thus \(f\) is constant under the spiral test or the stated semicircle exclusion.

The [constant-term theorem](Yin_C_A0141_v1.md#statement) puts every constant coefficient of \(O\) in \(R\), and every constant series in \(O\) in \(D\).
To apply it to any affiliated \(u\), write
\[
 P_u=\binom{1}{u}(1+u^*u)^{-1}\begin{pmatrix}1&u^*\end{pmatrix}.
\]
This orthogonal projection has affiliated column image \(\{(v,uv)^{\mathsf T}:v\in U\}\).
Since its top left entry is an affiliated unit, \(u=(P_u)_{21}(P_u)_{11}^{-1}\).
Thus the entries of \(V_u\) lie in \(D\) exactly when \(u\in D\), and the same statement holds for \(R\).
The constant series \(V_u\) passes all the tests when \(u\in D\).
Conversely every proposed lift implies \(u\in R\), and the rigidity just proved implies \(u\in D\) for the spiral and the sets of rays satisfying the exclusion.

### The angular probability bound

For fixed expressions, evaluation is continuous in measure relative to their common domain.
This follows from continuity of ring operations and [continuity of inversion at affiliated units](../ledger/Yin_L_A0075_v1.md#regular-specialization-of-the-compressed-resolvent).
The domain has countable complement, and the contractions form a measure-closed set by positivity of \(I-f^*f\).
The event defining \(a_f(r)\) is consequently measurable.
Removing a countable exceptional set leaves its angular measure unchanged at every \(r>0\).

For a nonconstant lift, take \(m,C,T,d\) as above and choose \(\xi\) such that \(b=\langle\xi,dTd\,\xi\rangle\ne0\), which is possible by polarization.
Every limiting direction of contractive evaluations tending to zero belongs to
\[
                  E_b=\{\omega\in\mathbb T:
                            \operatorname{Re}(\omega^m b)\le0\}.
\]
Here we discard the common countable exceptional set from the asymptotic expansion.
The set \(E_b\) has normalized arc length \(1/2\) because taking the \(m\)-th power preserves uniform measure on the circle.
For every open neighborhood of \(E_b\), all the remaining good directions lie in that neighborhood at every sufficiently small radius.
Otherwise compactness would give a limiting good direction in its closed complement.
Neighborhoods of \(E_b\) have arc lengths arbitrarily close to \(1/2\), proving \(\limsup_{r\downarrow0}a_f(r)\le1/2\).
A lift exceeding this bound is therefore constant, and the constant lift for \(u\in D\) has probability one.

### A contractive lift on the right half-plane

Suppose \(u\in R\).
We construct a rational lift of \(V_u\) contractive in the right half-plane.
Use the [single-vector criterion](Yin_C_A0137_v1.md#testing-a-whole-space-or-a-single-vector) for \(u^*\in R\).
It supplies an \(n\)-by-\(b\) group-ring matrix \(K\), constant vectors \(\epsilon\in\mathbb C^{1\times b}\), \(\gamma\in\mathbb C^{n\times1}\), and an affiliated row \(v\) such that
\[
 vK=\epsilon,\qquad v\gamma=u^*,\qquad
                  yK=0\ \Longrightarrow\ y\gamma=0
                  \quad (y\in U^{1\times n}).
\]
Form the finite group-ring matrix and the coordinate inclusion
\[
 B=\begin{pmatrix}K^*&-\epsilon^*&0\\ \gamma^*&0&-1\end{pmatrix},
 \qquad J(w,y)=(0,w,y)^{\mathsf T}.
\]
The image under \(J^*\) of the affiliated kernel of \(B\) is exactly the graph of \(u\).
In fact \(K^*x=\epsilon^*w\) implies that \(x-v^*w\) is in \(\ker K^*\), hence \(y=\gamma^*x=uw\).
Conversely \(x=v^*w\) supplies a solution for every \(w\in U\).
Put \(A_0=B^*B\), let \(P\) project onto \(\ker B\), and set \(C_0=J^*PJ\).
The support projection of \(C_0\) is \(P_u\), since \(C_0=(J^*P)(J^*P)^*\) has the same affiliated column image as \(J^*P\) by polar decomposition.

Consider the two rational matrices
\[
 H(z)=J^*z(z^2I+A_0)^{-1}J,\qquad
 W(z)=(H(z)-I)(H(z)+I)^{-1}.
\]
Splitting \(A_0\) into its kernel and support gives a formal Laurent inverse for \(z^2I+A_0\) and
\(H(z)=z^{-1}C_0+O(z)\). [Positive resolvent expansion](Yin_C_A0141_v1.md#realizing-every-element-of-the-regular-closure)
For \(p=P_u\) the product \((I+H(z))(zp+I-p)\) is a power series with invertible constant \(C_0+I-p\).
Thus \((I+H(z))^{-1}\) is a power series with constant \(I-p\).
The inverse of \(I+H\) is the last diagonal block of the inverse of the polynomial matrix
\[
                  \begin{pmatrix}z^2I+A_0&J\\-zJ^*&I\end{pmatrix},
\]
which is a formal unit by Schur elimination at \(z^2I+A_0\).
The inverses of this matrix and its leading block have entries in the scalar rational Laurent ring by [formal matrix inversion](Yin_C_A0143_v1.md#formal-inversion-by-scalar-pivots).
Consequently \(W=I-2(I+H)^{-1}\) belongs to \(M_2(O)\) and \(W(0)=2p-I=V_u\).

For \(\operatorname{Re}s>0\) and \(a\ge0\),
\[
 \frac{s}{s^2+a}
      =\frac12\left(\frac1{s+i\sqrt a}+\frac1{s-i\sqrt a}\right)
\]
has nonnegative real part.
Spectral calculus and compression give \(\operatorname{Re}H(s)\ge0\).
Here \(H(s)\) is bounded, \(I+H(s)\) is invertible, and
\[
 (I+H(s))^*(I+H(s))-(H(s)-I)^*(H(s)-I)=4\operatorname{Re}H(s)\ge0.
\]
This proves \(\|W(s)\|\le1\).
The open right half of each circle already gives \(a_W(r)\ge1/2\).
If \(u\in R\setminus D\), its lift \(W\) is nonconstant, so the angular bound gives \(a_W(r)\to1/2\).
Together with the constant-term necessity \(u\in R\), this completes both probability assertions.
On the imaginary axis away from zero and the countable exceptional set of the rational evaluations, \(s^2I+A_0\) is an affiliated unit and \(H(s)\) is skew-adjoint.
Its Cayley transform is then unitary by spectral calculus.
The displayed matrix evaluations agree with the fixed scalar rational expressions off a countable set by the same matrix inversion formulas and [ordinary evaluation of rational identities](Yin_C_A0143_v1.md#preservation-of-formal-identities).

If \(\{e^{im\theta}:\theta\in\Theta\}\) fits in a closed semicircle, choose \(|\lambda|=1\) rotating it into the closed right half-plane.
The series \(f(z)=W(\lambda z^m)\) still belongs to \(M_2(O)\) with constant coefficient \(V_u\).
Every prescribed ray maps into that half-plane and the preimage of the countable exceptional set is countable.
This proves the assertion for those directions.
Finally, for any finite list \(\theta_1,\ldots,\theta_k\), partition the \(k\)-torus into finitely many boxes of angular side less than \(\pi/2\).
Two distinct nonnegative powers of \((e^{i\theta_1},\ldots,e^{i\theta_k})\) lie in one box.
Their positive exponent difference \(m\) puts all \(e^{im\theta_j}\) in the open right semicircle, as required.

## Assessment history

### Decision angular-contractivity

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:30 |
| status | proved |
| reason | The first varying Laurent coefficient confines all limiting contractive directions to half the circle, and an accretive graph realization attains this threshold. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One-spiral and angular probability tests for an arbitrary affiliated operator, with the threshold and ray classification. |
| argument | [Argument](#argument) | Leading term in measure, angular compactness, graph compression, and the Cayley transform on the closed half-plane. |
| dependency | [Laurent asymptotics](Yin_C_A0143_v1.md#statement) | Generic evaluation and asymptotic expansion in measure. |
| dependency | [Constant series](Yin_C_A0141_v1.md#statement) | Identifying constant series and constant coefficients. |
| dependency | [Graph equations](Yin_C_A0137_v1.md#testing-a-whole-space-or-a-single-vector) | A linear presentation of an element of the regular closure. |
| dependency | [Measure topology](../audits/literature/FK86/Yin_U001.md#fk86-u001) | Continuity in measure for affiliated operators. |
| review | [Angular contractivity](../audits/reviews/Yin_R_A0176_v1.md#angular-contractivity) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-angular-contractivity)
