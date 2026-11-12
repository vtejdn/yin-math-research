---
author: Yin
---
# A weighted fifth-moment condition for large trinomial kernels

This continuation serves [route four](../strategies/Yin_S_A0004.md) under the full [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
The selected [common-power and quarter-bound argument](../claims/Yin_C_A0009_v6.md#statement) supplies the actual girth-ten hypothesis when the kernel dimension is at least 4/19.
The question here is what the next moment can constrain without assuming that the original group has the free joint law.
The result is a further necessary signed-cycle condition, not injectivity or a reduction of arbitrary matrices to this scalar family.

## Statement

Let G be torsion-free, let u and v belong to G, and set
\[
 T=1+u-v,\qquad X=T^*T,\qquad \delta=\dim_G\ker T.
\]
Suppose the actual signed bipartite graph of T is simple and has girth at least ten.
Let \(C_{10}\) denote the signed number of cyclically nonbacktracking length-ten closed paths from a marked vertex of the part corresponding to X.
The sign of a path is minus one to the number of its v-labelled edges.
Then
\[
 \boxed{\delta<\frac29-\frac{C_{10}}{1296}.}
 \tag{1}
\]
In particular, if \(\delta\ge2/9\), the accepted v6 result supplies the girth hypothesis and (1) forces \(C_{10}<0\).
Such a hypothetical kernel therefore requires a negative simple ten-cycle in the original labels.
If instead \(\delta\ge4/19\), then \(C_{10}\le15\).
Neither necessary condition is asserted to occur, and neither gives an unconditional strict 2/9 bound.

<a id="argument"></a>
## The actual fifth moment and signed paths

The same bounded bipartite adjacency realization and marked-part trace convention as [C_A0009_v4](../claims/Yin_C_A0009_v4.md#every-four--or-six-cycle-excludes-a-nonzero-kernel) identify \(\tau(X^j)\) with signed closed paths of length 2j.
Under the stated girth hypothesis, every closed path of length at most eight reduces completely by removing immediate reversals.
At length ten the only additional paths are cyclically nonbacktracking closed paths of length ten.
Indeed, a surviving reduced portion with a nonempty tail would have a closed portion of length at most eight, and a non-simple reduced ten-path would also contain a shorter cycle.
Both contradict girth at least ten.
The completely reducible paths have sign plus one and are counted by the degree-three tree, since removing an edge and its reverse removes its sign twice.

The accepted tree counts give
\[
 m_0=1,\quad m_1=3,\quad m_2=15,\quad m_3=87,\quad m_4=543.
\]
For length ten, the Dyck paths of semilength five, grouped by their number of excursions, have counts
\[
 (14,14,9,4,1).
\]
These follow by composing positive excursions: one excursion has Catalan count 14; two have counts \(5+2+2+5=14\); three have counts \(3\cdot2+3=9\); four have four choices for the unique excursion of semilength two; and five have one choice.
Each path with r excursions has \(3^r2^{5-r}\) choices in the three-regular tree.
The resulting count is
\[
 14\cdot3\cdot16+14\cdot9\cdot8+9\cdot27\cdot4
       +4\cdot81\cdot2+243=3543.
\]
Consequently the actual moment identity is
\[
 m_5=3543+C_{10}.
 \tag{2}
\]
This is an identity in the original group, with every actual closed path counted; it does not impose absence of ten-cycles or replace the group by a free presentation.

## A nonnegative polynomial on the actual spectral interval

The norm estimate \(\|T\|\le3\) gives \(0\le X\le9I\).
Define
\[
 q(s)=1-\frac23s+\frac1{12}s^2,\qquad
 P(s)=\left(1-\frac{s}{9}\right)q(s)^2.
 \tag{3}
\]
Thus \(P(s)\ge0\) for \(0\le s\le9\), and \(P(0)=1\).
If \(p=P_{\ker T}=1_{\{0\}}(X)\), bounded spectral calculus gives \(P(X)-p\ge0\), and hence
\[
 \delta\le\tau(P(X)).
\]
Direct expansion gives
\[
 P(s)=1-\frac{13}{9}s+\frac{41}{54}s^2
          -\frac{29}{162}s^3+\frac{25}{1296}s^4-\frac1{1296}s^5.
 \tag{4}
\]
Substituting (2) and the four preceding moments yields
\[
 \tau(P(X))=\frac29-\frac{C_{10}}{1296}.
 \tag{5}
\]

The inequality is strict.
Equality and faithfulness would give \(P(X)=p\), so \(P(X)^2=P(X)\) would be an identity between finite group-ring elements.
The regular representation is faithful on that algebra, and ordinary augmentation has \(\varepsilon(X)=1\).
It would therefore imply \(P(1)^2=P(1)\).
But \(q(1)=5/12\), so \(P(1)=25/162\), which is neither zero nor one.
This contradiction uses augmentation only on the finite-support algebraic identity, not on an arbitrary von Neumann projection.
It proves (1).

For \(\delta\ge2/9>4/19\), v6 ensures the required girth, and (1) gives \(C_{10}<0\).
A negative signed total entails at least one negative path; the preceding girth argument makes it a simple ten-cycle.
For \(\delta\ge4/19\), (1) instead gives
\[
 C_{10}<1296\left(\frac29-\frac4{19}\right)=\frac{288}{19}<16.
\]
The path count is an integer, proving \(C_{10}\le15\).

## Coefficient choice and finite enumeration scope

The coefficients in (3) can be obtained without a general minimization theorem.
For the free moments define \(w_j=m_j-m_{j+1}/9\), obtaining
\[
 (w_0,w_1,w_2,w_3,w_4)=\tfrac13(2,4,16,80,448).
\]
The normal equations for the quadratic expression in \((c,d)\) associated with \((1-s/9)(1+cs+ds^2)^2\) are
\[
 \begin{pmatrix}16/3&80/3\\80/3&448/3\end{pmatrix}
 \binom c d=-\binom{4/3}{16/3}.
\]
The determinant is \(256/3>0\), and the solution is \((-2/3,1/12)\).
The positive leading entry and determinant prove strict convexity of this finite quadratic problem, so the free-moment value 2/9 is minimal within this specified weighted-quadratic class.
This is the same finite moment-minimization mechanism attributed to Sim08 in [C_A0009_v3](../claims/Yin_C_A0009_v3.md#source-attribution-known-coverage-and-remaining-joint-requirement), with all needed arithmetic and the positive spectral comparison proved here.

The continuing [J_A0001 computation](../computations/programs/Yin_J_A0001/readme.md) enumerates the free cyclic word classes of proper color paths through length twelve using integer arithmetic.
It finds 1026 marked proper color strings and 105 cyclic-word classes at length ten, and 4098 strings and 351 classes at length twelve.
These finite outputs guide subsequent relation tests; they are not used as a proof that any class vanishes in an actual torsion-free group.
The proof of (1)--(5) needs neither those numerical class totals nor a proposed list of group-theoretic exclusions.
The native program, exact conventions and reproduction command are retained under that J; its generated output has no independently reviewed actual-group classification status.

## Full-chain limit and next discriminating test

For the original arbitrary Task input, no kernel-preserving reduction to this particular scalar signed trinomial has been established.
Even assuming such a reduction for a restricted family, the present inequality only forces a negative ten-cycle when its remaining scalar kernel is at least 2/9.
The first new missing scalar step is an independently valid actual-group restriction on those negative cycles or on their signed aggregate.
Continuing under a hypothetical exclusion of every such cycle would give a strict 2/9 scalar bound, but still neither injectivity for smaller kernels nor a dimension induction for all rational pivots.
Those later gaps prevent treating successive finite-moment bounds as an already established convergence-to-zero argument.
No new group-wide Atiyah result or historical novelty is asserted.

## Assessment history

### Decision reviewed-weighted-fifth-moment

| Field | Value |
| --- | --- |
| date | 2026-11-12T01:22 |
| status | proved |
| reason | Independent whole-artifact review verifies the weighted fifth-moment inequality, strictness and necessary negative ten-cycle condition, while retaining the exact girth and full-Task limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Strict signed-count bound under actual simplicity and girth at least ten, negative ten-cycle necessity at 2/9, and the signed-count ceiling at 4/19. |
| argument | [Argument](#argument) | Complete path, polynomial, trace and augmentation calculations, finite minimization, ancillary enumeration scope and unresolved full-Task chain. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0028_v6.md#whole-artifact-finding) | Whole fixed proof, exact accepted dependencies and separately checked finite native arithmetic through length twelve. |

## Current assessment

[Selected decision](#decision-reviewed-weighted-fifth-moment)

