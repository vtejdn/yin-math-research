---
author: Yin
---
# A common-power factorization and a universal quarter bound

Date: 2026-11-12 (Asia/Hong_Kong).
This development continues [route four](../strategies/Yin_S_A0004.md) under the full [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
The fixed predecessors are the [short signed-cycle restriction](../claims/Yin_C_A0009_v4.md#statement) and the [central three-translate bounds](../claims/Yin_C_A0009_v5.md#statement).
The immediate question is whether the remaining middle relation gives a genuinely independent unit certificate, rather than only normality of a kernel-equivalent operator.
The factorization below closes that relation and strengthens the universal scalar bound.
It does not provide a kernel-preserving reduction of arbitrary finite matrices to this scalar family, and even the resulting scalar bound is weaker than injectivity.
Those remain separate gaps between this investigation and the complete Task.

## Statement

Let G be a torsion-free discrete group and let \(u,v\in G\).
With the actual left regular representation and canonical trace, put
\[
 T=1+u-v,\qquad X=T^*T,\qquad
 \delta=\dim_G\ker T.
\]
If \((vu)^2=u^3\), then T has an actual affiliated inverse and \(\delta=0\).
For every pair, without that extra relation, one has
\[
 \boxed{\delta<\frac14.}
 \tag{1}
\]

There is a further restriction on a hypothetical relatively large kernel.
If \(\delta\ge4/19\), then the signed three-regular bipartite graph of T has no cycle of lengths four, six or eight, and
\[
 (\tau(X),\tau(X^2),\tau(X^3),\tau(X^4))=(3,15,87,543).
 \tag{2}
\]
Its girth is therefore at least ten.
This is only a necessary configuration in the interval \([4/19,1/4)\), not a construction of a positive kernel.

The reusable elementary factorization has the following broader scope.
For \(a,b\in G\) and positive integers m,n, assume
\[
 a^m=b^n=z\ne e,\qquad a\ne b.
\]
Then the difference of finite geometric sums
\[
 F_{m,n}(a,b):=\sum_{j=0}^{m-1}a^j-\sum_{k=0}^{n-1}b^k
\]
has an actual affiliated inverse, given by the factorization below.
Neither a division property for the whole group ring nor an Ore property of it is assumed.

<a id="argument"></a>
## Actual inverses and the ordered factorization

The only inverse certificate needed here is the [infinite-order regular-shift argument](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions).
For a nonidentity element g of a torsion-free group, \(g-1\) has zero kernel and dense range in the regular representation, and hence an inverse in the affiliated algebra.
The inverse need not be bounded.
Likewise, for distinct a and b, the factorization
\[
 b-a=a(a^{-1}b-1)
\]
independently certifies an affiliated inverse of \(b-a\).
All products and inverses in this section are closed affiliated-ring operations.
No equality asserts that an unbounded inverse may be applied to every Hilbert-space vector.

Under the common-power assumptions, z commutes with a and b.
Since \(z\ne e\), both a and b are nonidentity and all three of \(a-1,b-1,z-1\) are independently certified units.
The finite geometric identities imply
\[
 \sum_{j=0}^{m-1}a^j=(z-1)(a-1)^{-1},\qquad
 \sum_{k=0}^{n-1}b^k=(z-1)(b-1)^{-1}.
 \tag{3}
\]
The following ordered identity is valid in any ring for units A and B:
\[
 A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}.
\]
It follows simply by multiplying out the two terms in that order and requires no commutation of A and B.
Applying it to \(A=a-1\), \(B=b-1\) gives
\[
 \boxed{
 F_{m,n}(a,b)
 =(z-1)(a-1)^{-1}(b-a)(b-1)^{-1}.}
 \tag{4}
\]
Every factor has its independent actual inverse from the preceding paragraph.
Consequently
\[
 F_{m,n}(a,b)^{-1}
 =(b-1)(b-a)^{-1}(a-1)(z-1)^{-1}.
 \tag{5}
\]
Both ordered products of (4) and (5) equal one by adjacent cancellation.
These formulas are inside the actual affiliated algebra and also inside the actual division closure, since they use finitely many already certified inverses of group-ring elements.
No abstract skew field is substituted for that algebra.
The hypotheses \(z\ne e\) and \(a\ne b\) are essential to this certificate and are not inferred from a merely formal presentation.

## The middle relation has zero kernel

Suppose \((vu)^2=u^3\), and put \(w=vu\), \(z=u^3=w^2\).
If \(u=e\), torsion-freeness gives \(v^2=e\), hence \(v=e\) and \(T=1\).
Assume \(u\ne e\); then \(z\ne e\).
Also \(w\ne u\): otherwise \(u^2=u^3\), forcing \(u=e\).
Thus all hypotheses of (4) apply with \((a,b,m,n)=(u,w,3,2)\).
The right multiplication already used in C_A0009_v5 gives
\[
 S:=Tu=u+u^2-w
 =F_{3,2}(u,w).
\]
In particular,
\[
 S=(z-1)(u-1)^{-1}(w-u)(w-1)^{-1}.
 \tag{6}
\]
Here \(w-u\) is an actual nonzero group binomial, with its own cyclic inverse certificate.
Formula (5) supplies the inverse of S, and \(T=S u^{-1}\) has inverse \(uS^{-1}\).
This proves the first assertion of the statement, including every possible further relation in the actual supporting subgroup.
No injectivity statement is inherited from the presented common-power parent group.
Normality and a central-phase selfadjoint representative were valid earlier observations, but are not premises of this unit certificate.

## The universal quarter bound

Assume for contradiction that \(\delta\ge1/4\).
The accepted [C_A0009_v5 statement](../claims/Yin_C_A0009_v5.md#statement), using the complete finite-cycle classification at its documented scope, forces
\[
 (vu)^2=u^3.
\]
The preceding section then gives \(\delta=0\), a contradiction.
This proves (1) for every torsion-free group and all u,v.
Coincident-label and cyclic cases already have zero kernel, as recorded in the fixed predecessors, and also cannot satisfy the contradictory hypothesis.

This proof reuses the independently reviewed finite classification and central-support bounds as accepted inputs.
It does not assert that those inputs themselves proved scalar injectivity, nor does the narrower common-power theorem imply injectivity for pairs without that relation.

## A sharper necessary girth condition above four nineteenths

Suppose \(\delta\ge4/19\).
This is larger than \(1/6\), so the central-support bounds in C_A0009_v5 exclude
\[
 v^2=u^3,\qquad (vu^2)^2=u^3.
\]
The middle relation is excluded by (6).
Thus all three possible positive eight-cycle classes from C_A0009_v4 are absent.
Its nonzero-kernel classification gives
\[
 m_1=3,\quad m_2=15,\quad m_3=87,\quad
 m_4=543-8n_-,\qquad n_-\in\mathbb Z_{\ge0},
 \tag{7}
\]
where \(n_-\) counts the true negative cyclic word classes in that fixed complete table.
If \(n_-\ge1\), then \(m_4\le535\).
Use the real polynomial
\[
 q(s)=1-\frac{25}{38}s+\frac3{38}s^2.
 \tag{8}
\]
Since \(q(0)=1\), bounded spectral calculus gives
\[
 \delta\le\tau(q(X)^2)
 =1-\frac{25}{19}m_1+\frac{853}{1444}m_2
       -\frac{75}{722}m_3+\frac9{1444}m_4
 \le\frac4{19}.
 \tag{9}
\]
For the last step the coefficient of \(m_4\) is positive, and substitution of \((3,15,87,535)\) gives numerator
\[
 -4256+12795-13050+4815=304,
\]
with denominator 1444, namely \(4/19\).

The first inequality in (9) is strict by the same actual finite-support argument as in [C_A0009_v3](../claims/Yin_C_A0009_v3.md#a-polynomial-certificate-using-four-actual-moments).
Indeed, equality would force \(q(X)^2=p\), with \(p=P_{\ker T}\), and then \(q(X)^4=q(X)^2\) would be a finite group-ring identity.
Ordinary augmentation gives \(\varepsilon(X)=1\) and \(q(1)=8/19\), whose square is neither zero nor one, contradicting that identity.
Only the equality case invokes augmentation on the finite group ring; no extension to the von Neumann algebra is assumed.
Thus \(n_-\ge1\) would imply \(\delta<4/19\), contrary to the present hypothesis.
Consequently \(n_-=0\), proving (2).

The accepted tables already exclude four- and six-cycles under \(\delta>0\).
There are now neither positive nor negative eight-cycle classes, so their complete enumeration excludes eight-cycles as well.
The graph is simple, bipartite and three-regular in this nonzero-kernel case, hence has girth at least ten.
This deduction does not replace the labels by new generators or assume absence of longer relations.

For comparison, the coefficients in (8) solve
\[
 \begin{pmatrix}15&87\\87&535\end{pmatrix}
 \binom c d=-\binom3{15},
\]
whose determinant is 456 and solution is \((c,d)=(-25/38,3/38)\).
This explains the chosen finite polynomial using the variational mechanism already attributed in C_A0009_v3; no new general minimization theorem is needed.

## Source use and remaining full-task gaps

The proof uses the retained cyclic regular-shift certificate, exact actual affiliated-ring operations, the reviewed short-cycle tables, and the reviewed central-support bounds.
The ordered difference-of-inverses identity and common-power calculation are direct finite algebra, with no extra external theorem premise.
The finite polynomial calculation reuses the existing Christoffel-minimization attribution only as explanation; its constants and inequalities are proved above.
No historical novelty or previously unknown whole-group Atiyah coverage is asserted.

The middle common-power obstruction identified in v5 is resolved for this scalar operator by (6).
The remaining scalar question includes pairs with no short relation and possible kernels strictly below one quarter.
The girth conclusion identifies a narrower finite-word problem for kernels at least \(4/19\), but supplies neither all higher-moment bounds nor an induction to zero.
For the full Task, arbitrary matrices and actual rational Schur complements still require independently invertible pivots after noncyclic path sums.
No correspondence reducing every such pivot to (4) has been supplied.
The original all-group, all-matrix objective and its completion criterion are unchanged.

## Assessment history

### Decision reviewed-common-power-quarter

| Field | Value |
| --- | --- |
| date | 2026-11-11T19:52 |
| status | proved |
| reason | Independent whole-artifact review verifies the actual common-power inverse, the universal strict quarter bound and the necessary girth-ten configuration above four nineteenths. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common-power unit theorem, the middle-relation inverse, universal strict quarter bound, and conditional moment and girth restriction. |
| argument | [Argument](#argument) | Complete ordered affiliated operations, degenerate cases, accepted dependency interfaces, exact polynomial constants, strictness and full-Task limits. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0028_v5.md#whole-artifact-finding) | Entire fixed statement and argument, with the precise accepted short-cycle and central-support review scopes. |

## Current assessment

[Selected decision](#decision-reviewed-common-power-quarter)

