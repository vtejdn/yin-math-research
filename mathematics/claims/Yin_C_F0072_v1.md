---
author: Yin
---
# Two bounded derivation contractions give an actual vacuum and full canonical domains

Date: 2026-10-14T13:21.
This project deduction addresses the authorized comparison between full-domain dual identities and the actual vacuum condition for starred derivations.
The acsy_rationality_check agent developed the two-contraction extension of the spectral-partition argument; root checked the Leibniz and core-adjoint formulas before this fixed candidate was prepared.
This preliminary discussion is not a fixed-material independent review.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with a faithful normal tracial state.
Put \(H=L^2(M,\tau)\) and \(\Omega=1\), with the inner product linear in its second variable.
Let \(A\subseteq M\) be a weakly dense unital star subalgebra.
Consider an outer-bimodule derivation
\[
 \delta:A\longrightarrow H\otimes_2 H,
 \qquad
 \delta(ab)=(a\otimes1)\delta(b)+\delta(a)(1\otimes b).
\]
The bounded slice maps on the Hilbert tensor product define
\[
 E(a)=(\mathrm{id}\otimes\tau)\delta(a),
 \qquad F(a)=(\tau\otimes\mathrm{id})\delta(a).
\]
Assume that
\[
 \|E(a)\|_2\le C_E\|a\|,
 \qquad
 \|F(a)\|_2\le C_F\|a\|
 \qquad(a\in A)                                      \tag{1}
\]
for finite constants \(C_E,C_F\).
No reality, coassociativity or a priori closability condition is imposed.

**A. Actual vacuum.**
Regard \(\delta\) as a densely defined operator from \(H\) to \(H\otimes_2H\), with domain \(A\Omega\).
Then
\[
 1\otimes1\in\operatorname{Dom}\delta^*,\qquad
 \xi:=\delta^*(1\otimes1),\qquad
 \|\xi\|_2\le2(C_E+C_F).                              \tag{2}
\]

**B. Canonical contraction and both full domains.**
Let \(E_0\) denote the operator \(a\Omega\mapsto E(a)\), with domain \(A\Omega\).
It is closable, and
\[
 E_0^*(a\Omega)=a\xi-(F(a^*))^* \qquad(a\in A).        \tag{3}
\]
For \(\widetilde E=\overline{E_0}\),
\[
 \begin{split}
 M\Omega&\subseteq\operatorname{Dom}\widetilde E
                 \cap\operatorname{Dom}\widetilde E^*,\\
 \|\widetilde E(a\Omega)\|_2&\le C_E\|a\|,\\
 \|\widetilde E^*(a\Omega)\|_2&\le(\|\xi\|_2+C_F)\|a\|
 \qquad(a\in M).
 \end{split}                                         \tag{4}
\]
The involution on \(F(a^*)\in H\) is the tracial involution.
The estimates concern the specified canonical closure and its actual Hilbert-space adjoint.

## Argument

### 1. A continuous bilinear identity

Put \(B=\overline A^{\|\cdot\|}\) and
\[
 \phi=(\tau\otimes\tau)\delta=\tau E=\tau F.
\]
Both contractions and \(\phi\) have unique operator-norm-continuous extensions to \(B\).
The Leibniz rule gives
\[
 \phi(ab)=\tau(F(a)b)+\tau(aE(b))
 \qquad(a,b\in A).                                   \tag{5}
\]
Products of a bounded element and an \(L^2\) vector have a well-defined tracial pairing.
Continuity of both sides extends (5) to every \(a,b\in B\).
This extension does not assert that \(\delta\) itself extends to \(B\).

### 2. Continuous square partitions control the vacuum functional

Fix \(a=a^*\in B\).
On its compact real spectrum choose finitely many real nonnegative continuous functions \(h_j\) such that
\[
 \sum_j h_j^2=1,
\]
at most two functions are nonzero at each point, and each support meeting the spectrum has diameter at most \(\varepsilon\).
One obtains such a square partition by using consecutive overlapping intervals, a subordinate continuous partition, and division by the square root of the sum of squares.
Each function of \(a\) lies in \(B\).
Write \(h_j=h_j(a)\), and choose \(\lambda_j\) in the corresponding spectral support.
Then
\[
 a_\varepsilon:=\sum_j\lambda_jh_j^2\longrightarrow a
 \quad\hbox{in operator norm},\qquad
 \sum_j\lambda_j^2\|h_j\|_2^2\longrightarrow\|a\|_2^2.
                                                               \tag{6}
\]
The first limit follows from the support diameter.
For the second, the functions \(\sum_j\lambda_j^2h_j(t)^2\) converge uniformly to \(t^2\) on the compact spectrum, so their traces converge.

For independent symmetric signs \(\sigma_j\), pointwise Cauchy--Schwarz and overlap two give
\[
 \left\|\sum_j\sigma_jh_j\right\|\le\sqrt2.
\]
The Hilbert-space sign identity and (1) therefore yield
\[
 \begin{split}
 \sum_j\|E(h_j)\|_2^2
 &=\mathbb E_\sigma\left\|E\!\left(\sum_j\sigma_jh_j\right)\right\|_2^2
 \le2C_E^2,\\
 \sum_j\|F(h_j)\|_2^2&\le2C_F^2 .
 \end{split}                                                   \tag{7}
\]
All expectations are finite averages.

Apply (5) with both inputs equal to \(h_j\).
No Hermiticity or reality assumption is used:
\[
 \phi(h_j^2)=\tau(F(h_j)h_j)+\tau(h_jE(h_j)).
\]
Cauchy--Schwarz in \(H\) and then over the finite index set gives
\[
 \begin{split}
 |\phi(a_\varepsilon)|
 &\le
 \left(\sum_j\lambda_j^2\|h_j\|_2^2\right)^{1/2}
 \left[
  \left(\sum_j\|F(h_j)\|_2^2\right)^{1/2}
  +\left(\sum_j\|E(h_j)\|_2^2\right)^{1/2}
 \right]\\
 &\le\sqrt2(C_E+C_F)
       \left(\sum_j\lambda_j^2\|h_j\|_2^2\right)^{1/2}.
 \end{split}                                                   \tag{8}
\]
Letting \(\varepsilon\) decrease to zero and using norm continuity of \(\phi\) proves
\[
 |\phi(a)|\le\sqrt2(C_E+C_F)\|a\|_2
 \qquad(a=a^*\in B).                                           \tag{9}
\]

For arbitrary \(p\in B\), write \(p=a+\mathrm ib\), where \(a,b\in B\) are selfadjoint.
Traciality gives \(\|a\|_2^2+\|b\|_2^2=\|p\|_2^2\).
Hence
\[
 |\phi(p)|
 \le\sqrt2(C_E+C_F)(\|a\|_2+\|b\|_2)
 \le2(C_E+C_F)\|p\|_2.                                        \tag{10}
\]
Since \(A\Omega\) is dense in \(H\), (10) is exactly the actual vacuum-adjoint condition in (2).
In particular, there is a unique \(\xi\in H\) such that
\[
 \phi(p)=\langle\xi,p\Omega\rangle=\tau(\xi^*p)
 \qquad(p\in A).
\]

### 3. The actual adjoint of the canonical contraction

For \(a,b\in A\), use (5) and the preceding representation of \(\phi\):
\[
 \begin{split}
 \langle a\Omega,E_0(b\Omega)\rangle
 &=\tau(a^*E(b))\\
 &=\phi(a^*b)-\tau(F(a^*)b)\\
 &=\langle a\xi-(F(a^*))^*,b\Omega\rangle .
 \end{split}                                                   \tag{11}
\]
For fixed \(a\), the last vector is in \(H\).
Thus \(a\Omega\in\operatorname{Dom}E_0^*\), and (11) proves (3).
Density of \(A\Omega\) makes \(E_0\) closable.
Moreover,
\[
 \|E_0^*(a\Omega)\|_2
 \le(\|\xi\|_2+C_F)\|a\|\qquad(a\in A).                         \tag{12}
\]
The adjoint of \(\widetilde E=\overline{E_0}\) is \(E_0^*\).

### 4. Restoration of both full domains

Fix \(a\in M\) and \(\varepsilon>0\).
Kaplansky density for \(B\subseteq M\), followed by norm approximation from \(A\), supplies a net \(a_\gamma\in A\) with
\[
 a_\gamma\Omega\longrightarrow a\Omega\quad\hbox{in }H,\qquad
 \|a_\gamma\|\le\|a\|+\varepsilon .
                                                               \tag{13}
\]
The nets \(E_0(a_\gamma\Omega)\) and \(E_0^*(a_\gamma\Omega)\) are bounded in \(H\), by (1) and (12).
Pass to a common subnet on which both converge weakly.
The graphs of \(\widetilde E\) and \(E_0^*\) are norm-closed linear subspaces of \(H\oplus H\), and therefore are weakly closed.
Their respective graph-pair limits imply
\[
 a\Omega\in\operatorname{Dom}\widetilde E
          \cap\operatorname{Dom}E_0^* .
\]
The weak limits are the corresponding actual graph values.
Weak lower semicontinuity and then \(\varepsilon\downarrow0\) give all the bounds in (4).

## Scope and mathematical relationship

The argument extends the continuous spectral-partition mechanism of [C_F0071 v2, the symmetric-form lemma](Yin_C_F0071_v2.md#symmetric-form-lemma).
That result uses reality to identify the left contraction with the tracial conjugate of the right contraction.
Here the two contractions are estimated separately, so no such identification is required.
The complete modified proof is given above.

The graph-restoration mechanism is the one used in [C_F0070, the exact canonical-domain comparison](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses).
Here both needed bounds are established explicitly, including the actual core-adjoint formula.
These are argument provenance and reused mechanisms; neither earlier Claim is being cited as if it already stated the present two-contraction conclusion.

For a general normal tuple, [C_F0070 Part A](Yin_C_F0070_v1.md#statement) gives a bounded right contraction from bare full-domain duals.
The present statement additionally requires the left-contraction bound.
It does not prove that this extra bound follows from normality or from the right-contraction bound alone.
The boundedness of a measurable multiplier on the coarse Hilbert tensor product by itself supplies no such operator-norm-to-\(L^2\) estimate.
No new conclusion for arbitrary correlated normal tuples is asserted without verifying (1).

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:21 |
| status | open |
| reason | Complete two-contraction proof and actual canonical-domain argument retained for review of this fixed candidate. |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The actual vacuum, explicit adjoint formula and both full canonical domains under the two norm bounds. |
| argument | [Argument](#argument) | The bilinear identity, continuous square-partition estimates and two weakly closed graph passages. |
| dependency | [C_F0071 v2 symmetric-form mechanism](Yin_C_F0071_v2.md#symmetric-form-lemma) | Continuous square partitions and the Hilbert sign estimate; the modified two-contraction proof is supplied in full. |
| dependency | [C_F0070 canonical graph mechanism](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky approximation and weakly closed graphs; both present operator bounds and the actual adjoint are checked explicitly. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:25 |
| status | proved |
| reason | The entire fixed two-contraction proof passed a separately performed check, including the non-Hermitian functional estimate, actual adjoint formula, and both canonical graph domains. The separate left-contraction bound remains an explicit hypothesis. |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual vacuum, its quantitative bound, actual core-adjoint formula and both full canonical domains under two operator-norm-to-L2 bounds. |
| argument | [Argument](#argument) | Complete bilinear, continuous-square-partition and graph-restoration argument. |
| dependency | [C_F0071 symmetric-form mechanism](Yin_C_F0071_v2.md#symmetric-form-lemma) | Provenance of the partition and Hilbert sign estimate, extended and proved here for two separately bounded contractions. |
| dependency | [C_F0070 canonical graph mechanism](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky and weak-graph mechanism with both present bounds and the actual adjoint supplied by this argument. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0045_v1.md#conclusion) | Exact fixed statement and complete argument, with shared discussion and inspection limits disclosed. |

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:59 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Actual vacuum, its quantitative bound, actual core-adjoint formula and both full canonical domains under two operator-norm-to-L2 bounds. |
| argument | [Exact material](#argument) | Complete bilinear, continuous-square-partition and graph-restoration argument. |
| dependency | [Exact material](Yin_C_F0071_v2.md#symmetric-form-lemma) | Provenance of the partition and Hilbert sign estimate, extended and proved here for two separately bounded contractions. |
| dependency | [Exact material](Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky and weak-graph mechanism with both present bounds and the actual adjoint supplied by this argument. |
| review | [Original finding](../audits/reviews/Yin_R_F0045_v1.md#conclusion) | Whole two-contraction functional estimate, actual vacuum and adjoint formula, and both canonical graph domains; self-reviewed with disclosed developing argument, shared discussion and author explanations. |
