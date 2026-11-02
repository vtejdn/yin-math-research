---
author: Yin
---

# Scalar elliptic infimum and two precise affine variational obstructions

## Current assessment
[Selected decision](#decision-internal-review)

## Statement

Let \(T=a+\sum_j c_js_j\), where \(a,c_j\in\mathbb C\) and the \(s_j\) are free standard semicircular elements in a finite tracial von Neumann algebra.
Put \(v=\sum_j|c_j|^2\), \(\gamma=\sum_j c_j^2\), and rotate by a scalar unitary so that \(\gamma=t\in[0,v]\) and the rotated \(a=x+iy\).
Then, with the ordinary normalized tracial determinant and extended-real infimum,
\[
 \log\Delta(T)=\inf_{r>v}\left[-\tfrac12+\tfrac12\log r+
 \frac{x^2}{2(r+t)}+\frac{y^2}{2(r-t)}\right].
\]
The unrotated drift term is \([r|a|^2-\operatorname{Re}(\overline\gamma a^2)]/[2(r^2-|\gamma|^2)]\).
This includes the line case \(t=v\), an absent zero numerator interpreted on the open trial domain, and the noiseless case \(v=0\), giving \(\log|a|\), including \(-\infty\) at zero.
For fixed genuine elliptic noise, the explicit shifts in the argument rule out any formula whose entire drift dependence is only \(|a|^2PQ\).
For circular covariance \(\eta=\mathrm{id}_{M_2}\) and \(a=\mathrm{diag}(1,-1)\), the displayed stationary joint positive-matrix action has supremum \(+\infty\), although \(\log\Delta(a+cI_2)=0\).
The latter is a failure of the joint maximum; it asserts no failure of an ordered optimization.

## Provenance and accepted inputs

The complete independent scalar derivation and two explicit failed candidate mechanisms are [retained below in Sections 5-7](#5-independent-scalar-elliptic-infimum), authored by the parallel exploration agent on 2026-09-13.
The scalar proof uses only the [C_F0119 Dyson identity and determinant primitive](Yin_C_F0119_v1.md), with its physical resolvent conventions, and does not use C_F0124 or the derived two-positive-matrix formula.
No source theorem from the related Hachem--Loubaton--Najim search is imported.
The phase and similarity counterexamples preserve the exact fixed noise and drift families of that original exploration.

## Argument

### 5. Independent Scalar Elliptic Infimum

This section uses the two-by-two Dyson equation and its determinant primitive from Yin_C_F0119, but does not use Yin_C_F0124 or (4).
Let \(m=1\), let \(T=a+\sum_j c_js_j\), and set
\[
 v=\sum_j|c_j|^2,\qquad \gamma=\sum_jc_j^2,\qquad |\gamma|\le v.
\]
Assume first \(v>0\).
Rotating \(T\) by a scalar unitary lets us take \(\gamma=t\in[0,v]\).
Write the rotated drift as \(a=x+iy\).
Define
\[
 f_a(r)=-\frac12+\frac12\log r
           +\frac{x^2}{2(r+t)}+\frac{y^2}{2(r-t)},\qquad r>v.
                                                               \tag{11}
\]
Then
\[
 \log\Delta(T)=\inf_{r>v}f_a(r).                                \tag{12}
\]
Equivalently, before rotation the final two terms in (11) are
\[
 \frac{r|a|^2-\operatorname{Re}(\overline\gamma\,a^2)}
        {2(r^2-|\gamma|^2)}.                                   \tag{13}
\]

To prove (12), the physical hermitized resolvent has the form
\[
 R_\varepsilon=
 \begin{pmatrix}iq&h\\\bar h&iq\end{pmatrix},\qquad q>0.
\]
The equal diagonal imaginary parts follow from equality of the tracial singular-value laws of \(TT^*\) and \(T^*T\).
Put \(r=(q^2+|h|^2)^{-1}\).
Direct inversion and the Dyson equation give
\[
 (r-v)q=\varepsilon,\qquad
 rh+t\bar h=a,\qquad
 h=\frac{x}{r+t}+i\frac{y}{r-t}.                               \tag{14}
\]
Therefore \(r>v\) and
\[
 r\left(\frac{x^2}{(r+t)^2}
        +\frac{y^2}{(r-t)^2}
        +\frac{\varepsilon^2}{(r-v)^2}\right)=1.                \tag{15}
\]
Each term \(r/(r\pm t)^2\), and \(r/(r-v)^2\), is strictly decreasing on \(r>v\), except an absent coefficient contributes zero.
Thus (15) has a unique root; its left side decreases from infinity to zero.
The derivative of \(f_a\) has the sign of
\[
 1-r\left(\frac{x^2}{(r+t)^2}+\frac{y^2}{(r-t)^2}\right).
\]
Consequently the minimizer is the boundary \(r\downarrow v\) if the boundary expression is at most one, and otherwise is the unique interior root where it equals one.
The roots of (15) converge to that minimizing point or boundary.

The determinant primitive, after direct substitution of (14), reads
\[
 \log\Delta_\varepsilon(T)
      =f_a(r_\varepsilon)+\frac{\varepsilon q_\varepsilon}{2}.
                                                               \tag{16}
\]
For an explicit check, the primitive is \(\frac12\log r+\frac t2\operatorname{Re}(h^2)-\frac v2q^2\).
Use \(rh+t\bar h=a\), \(r(q^2+|h|^2)=1\) and \((r-v)q=\varepsilon\) to obtain (16).
Moreover \(q^2\le1/r\le1/v\), so the correction tends to zero.
The regularized logarithmic determinant decreases to the ordinary one, proving (12), including the degenerate line case \(t=v\).
When \(t=v\) and \(y=0\), interpret the absent \(y^2/(r-t)\) term as identically zero on the open domain.

If \(v=0\), all noise coefficients vanish.
The same trial expression with \(t=0\) gives \(\inf_{r>0}[-1/2+\frac12\log r+|a|^2/(2r)]=\log|a|\), including \(-\infty\) when \(a=0\).

### 6. A Fixed-Noise Obstruction to a Radial Drift Term

Suppose a proposed general formula uses positive scalar trials \(P,Q\) when \(m=1\), and all its dependence on the drift is through \(\bar a P aQ=|a|^2PQ\).
Its result must be radial in \(a\), regardless of how completely it records the fixed noise data elsewhere.

Fix \(v=1\) and \(\gamma=t\in(0,1)\), realized by
\[
 T_0=\sqrt{\frac{1+t}{2}}s_1
       +i\sqrt{\frac{1-t}{2}}s_2.
\]
For \(0<r<1-t\), equation (12) gives
\[
 \log\Delta(T_0+r)=-\frac12+\frac{r^2}{2(1+t)},\qquad
 \log\Delta(T_0+ir)=-\frac12+\frac{r^2}{2(1-t)}.
\]
They differ.
Both \(\eta\) and \(\rho\), as well as the entire noise family, are fixed in this comparison.
Thus this is stronger than the earlier observation that ordinary covariance alone does not determine an affine determinant: even with full covariance information, the proposed form of the drift term discards a necessary phase.
A general formula needs a phase-sensitive quadratic term such as (13), or the [auxiliary complex matrix in the full positive-pair formula](Yin_C_F0165_v1.md#statement).

### 7. An Unrestricted Two-Matrix Maximum Can Diverge

For circular covariance \(\eta=\operatorname{id}_{M_2}\), a natural zero-regularization stationary action is
\[
 F(P,Q)=\log\det Q+
        \log\det(P+a^*Q^{-1}a)-\operatorname{Tr}(PQ),
       \qquad P,Q>0.                                         \tag{17}
\]
For scalar coefficients, maximizing the analogous expression gives the correct circular potential.
This does not extend to a joint matrix maximum.

Take \(a=\operatorname{diag}(1,-1)\).
Write \(W=Q^{1/2}PQ^{1/2}\) and \(D=Q^{-1/2}aQ^{1/2}\).
Then
\[
 F(P,Q)=\log\det(W+D^*D)-\operatorname{Tr}W.
\]
For fixed \(Q\), diagonalize \(D^*D\) with eigenvalues \(\lambda_1,\lambda_2\).
Concavity and sign-symmetry averaging allow \(W\) to be diagonal in that basis.
The supremum equals
\[
 \phi(\lambda_1)+\phi(\lambda_2),\qquad
 \phi(\lambda)=
 \begin{cases}\lambda-1,&0\le\lambda\le1,\\
               \log\lambda,&\lambda\ge1.
 \end{cases}
\]
Now set \(Q=e^{2uX}\), where \(X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).
Since \(aX=-Xa\), the singular values of \(D=e^{-uX}ae^{uX}\) are \(e^{2u}\) and \(e^{-2u}\).
Thus the supremum over \(P\) is
\[
 4u+e^{-4u}-1\longrightarrow+\infty.
\]
In contrast, for \(T=a+cI_2\) with a standard circular \(c\), its two diagonal components are \(c+1\) and \(c-1\), each with logarithmic determinant zero by (12).
Hence \(\log\Delta(T)=0\).
This explicit failure rules out promoting a stationary two-matrix action to a joint maximum.
Ordered optimization remains a separate question.

## Assessment history

### Decision registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:24 |
| status | open |
| reason | Register this complete retained argument for its actual current internal review; preserve the original derivation, attribution and dependency boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete hypotheses, conclusions, ordered extrema and limitations above. |
| argument | [Argument](#argument) | Entire retained proof and its disclosed accepted mathematical interfaces. |

### Decision internal-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:26 |
| status | proved |
| reason | The retained complete proof and exact current statement passed the actual internal mathematical and interface review at their disclosed accepted input scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete hypotheses, conclusions and precise limits above. |
| argument | [Argument](#argument) | Entire retained argument, including the original dependency and nonconclusion boundaries. |
| review | [Internal finding](../audits/reviews/Yin_R_F0175_v1.md#scalar-obstructions-finding) | Complete independent scalar elliptic infimum and exact phase/joint-maximum obstructions, including every disclosed degenerate case. |

