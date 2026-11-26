---
author: Yin
---

# A half kernel forces polynomial growth of finite powers of the original product of involutions

## Statement

Use the [two independent signs and the assembly](Yin_C_A0345_v1.md#statement) for a noninteger two-square rectangle, and \(A=J_gTJ_hT^{-1}\) in the four-coordinate regular representation.
For each real \(C\ge1\) there is a constant \(c_C\in(0,1]\), independent of the group and coefficients with \(\|T\|\|T^{-1}\|\le C\), such that a half kernel forces
\[
          \max_{0\le j\le m}\|A^{2j}\|
                      \ \ge\ (c_C m/49)^{1/8}\qquad (m\ge1).
\]
In particular no forward power-bounded product \(A\) can give a half kernel, without a restriction on the condition number of the individual input.
For any fixed conditioning bound \(C\) and any finite power norm bound \(K\ge1\) there are a finite \(m=m(C,K)\) and \(\epsilon(C,K)>0\) such that
\[
         \max_{0\le j\le m}\|A^{2j}\|\le K
                  \quad\Longrightarrow\quad \delta\le 1/2-\epsilon(C,K).
\]
For rational upper bounds \(C,K\), positive lower bounds on the constants and an admissible integer \(m\) may be obtained by finite real polynomial tests.
The quantitative statements include the visible rank-three and rank-four index-four evaluations.
They do not assert that the growth condition suffices for a half kernel.

## A finite-support lower bound at bounded condition number

Normalize \(T\) so all singular values lie in \([1,C]\).
The [word inequalities and signed graph projections](Yin_C_A0345_v1.md#four-step-words-and-the-commutator-kernel) give \(t(A^2)=0\) and \(t(\operatorname{proj}\ker(A^2-I))=\delta\), using normalized four-coordinate trace.
These word and graph identities apply to the nonunitary \(T\) as well: the group words in \(A^2\) have the same four alternating letters.
The sign and the three-parameter bound give \(\delta\le1/2\).

In fact \(\|A^4-I\|_2^2\ge c_C\) uniformly over this conditioning range, where the norm is formed with \(t\).
An exact identity \(A^4=I\) would give a group-ring idempotent \(E=(I+A^2)/2\), of unnormalized trace two by the word identities.
Both \(J_g\) and \(L_T=TJ_hT^{-1}\) conjugate \(A\) to \(A^{-1}\).
They therefore commute with \(E\), and on its range they commute with each other.
The four group-ring idempotents \((I+\xi J_g)(I+\eta L_T)E/4\) consequently sum to \(E\), and have equal trace by the independent sign changes.
An idempotent in a finite von Neumann algebra has trace equal to its range dimension: in the orthogonal splitting by its closed range its diagonal blocks are the identity and zero.
Thus each has unnormalized rank \(1/2\), contradicting scalar injectivity on a nonzero group-ring entry.

As in the [finite partition bound](Yin_C_A0345_v1.md#a-positive-lower-bound-from-finitely-many-equality-patterns), the square norm is determined by the partition of at most 257 group words and the numerical assembly.
The normalized conditioning range is compact.
For every partition admitting no zero at any such \(T\) the minimum is strictly positive; the preceding argument excludes the other partitions for the groups under consideration.
Choose a common lower bound \(0<c_C\le1\) for the former minima.
The finite real polynomial procedure still applies by treating \(T^{-1}\) as a numerical variable with both inverse equations, and imposing the singular-value bounds on \(T^*T\).

## Averaging a finite orbit of the metric

Put \(S=A^2\).
Since \(J_g A J_g=A^{-1}\) and \(J_g\) is unitary, \(\|S^{-j}\|=\|S^j\|\).
For a fixed \(m\ge1\) write \(K_m=\max_{0\le j\le m}\|S^j\|\), \(D=m^{-1}\sum_{j=0}^{m-1}(S^*)^j S^j\), and \(Y=D^{1/2}S D^{-1/2}\).
Then \(K_m^{-2}I\le D\le K_m^2 I\), and telescoping gives
\[
 \|Y^*Y-I\|\le e,\qquad e=K_m^2(K_m^2-1)/m .
\]
Indeed \(S^*DS-D=((S^*)^m S^m-I)/m\), with the last difference of positive operators bounded in norm by \(K_m^2-1\) using the inverse-power bound as well.
If \(e\le1\), polar decomposition gives a unitary \(V\) with \(\|V-Y\|\le e\), since \(|\sqrt t-1|\le|t-1|\) for \(t\ge0\) and \(Y\) is invertible.
Thus \(|t(V)|\le e\), as \(t(Y)=t(S)=0\).
For the orthogonal projection \(p\) onto \(\ker(Y-I)\) one has \(t(p)=\delta\) by bounded invertible similarity and \(\|(V-I)p\|\le e\).
The two complementary input spaces and the two factorizations of \(V^2-I\) give
\[
   \|V^2-I\|_2^2
     \le4\|(V-I)p\|_2^2+4\|(V+I)(I-p)\|_2^2
     \le 8(1-2\delta)+8e+4e^2 .
\]
Here \(\|V+I\|_2^2=2+2{\rm Re}\,t(V)\) and \(\delta\le1/2\).
Moreover \(\|Y^2-V^2\|\le (1+\sqrt{1+e})e\le3e\).
Undo the similarity, whose condition number is at most \(K_m^2\).
The uniform lower bound from the preceding section therefore gives
\[
       \sqrt{c_C}\le K_m^2\left(3e+
                     \sqrt{8(1-2\delta)+8e+4e^2}\right).
\]

## The growth exponent and a finite certificate

At \(\delta=1/2\) and \(e\le1\) the right hand side is at most \(7K_m^2\sqrt e\le7K_m^4/\sqrt m\).
If \(e>1\) then \(K_m^4>m\), which also implies \(K_m^8\ge c_C m/49\).
This proves the growth bound.
For the finite-gap claim choose \(m\) so large that \(K^4/m\le c_C/(100 K^4)\).
When \(K_m\le K\), one has \(e\le K^4/m\le1\).
Using \(3e+\sqrt{8e+4e^2}\le7\sqrt e\), the estimate implies
\[
    \sqrt{c_C}\le K^2\sqrt{8(1-2\delta)}+\tfrac7{10}\sqrt{c_C}.
\]
For example \(\epsilon(C,K)=9c_C/(1600K^4)\) suffices, with the indicated choice of \(m\).

## Assessment history

### Decision finite-orbit-metrics-and-power-growth

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:53 |
| status | proved |
| reason | A finite average of the orbit metrics yields an eighth-power lower bound on the growth of norms at a half kernel. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A finite average of the orbit metrics yields an eighth-power lower bound on the growth of norms at a half kernel. |
| argument | [A finite-support lower bound at bounded condition number](#a-finite-support-lower-bound-at-bounded-condition-number) | A finite-support lower bound at bounded condition number. |
| argument | [Averaging a finite orbit of the metric](#averaging-a-finite-orbit-of-the-metric) | Averaging a finite orbit of the metric. |
| argument | [The growth exponent and a finite certificate](#the-growth-exponent-and-a-finite-certificate) | The growth exponent and a finite certificate. |
| dependency | [Earlier result, version 1](Yin_C_A0345_v1.md#statement) | A short-word equality partition and two sign projections give a uniform quantitative obstruction near the unitary group. |
| review | [The uniform neighborhood of unitary assemblies](../audits/reviews/Yin_R_A0237_v1.md#the-uniform-neighborhood-of-unitary-assemblies) | Independent inspection at the scope used. |
| review | [Finite orbit metrics and power growth](../audits/reviews/Yin_R_A0237_v1.md#finite-orbit-metrics-and-power-growth) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-finite-orbit-metrics-and-power-growth)
