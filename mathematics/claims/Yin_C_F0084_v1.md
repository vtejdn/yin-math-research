---
author: Yin
---

# Arbitrarily large nondense support does not give global rationality

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0084: An Arbitrarily Large Nondense Module Gives a False Positive

<a id="statement"></a>
<a id="yin_c_f0084"></a>

Provenance: project deduction using the accepted interval Hilbert transform.
Mathematical assessment at authorship: proof draft; complete candidate below.
Review assessment at authorship: self-reviewed; independent review pending.
Current candidate proof: [yin_c_f0084-p1](#yin_c_f0084-p1).

For every \(0<\varepsilon<1\), there exist a finite tracial commutative von Neumann algebra \(\mathcal M\), a selfadjoint generator \(X\), a projection \(p\in\mathcal M\) with \(\tau(p)=1-\varepsilon\), and a bounded operator \(D\in B(H)\), such that on the left module \(\mathcal E=\mathcal M p\),
\[
[D,X]z=Pz\qquad(z\in\mathcal E).
\tag{36.1}
\]
Nevertheless there is a bounded projection \(f\in\mathcal M\) for which
\[
\operatorname{rank}([D,f]|_{\mathcal E})=1,
\qquad
f\notin\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X.
\tag{36.2}
\]
The same \(D\) and \(D^*\) are defined and bounded on all of \(H\).
Thus the failure concerns weakening the space on which the dual relation and defects are tested, not an ambiguity about adjoints of nondensely defined operators.
The closure of \(\mathcal E\) is the proper subspace \(Hp\).

### Dependencies and Exact Scope

The only non-elementary construction input is the previously checked [Tao06 \(L^2\) Hilbert-transform bound and its interval compression](../audits/reviews/Yin_R_F0005_v1.md#4-primary-hilbert-transform-input-and-the-interval-obstruction).
The scalar fraction description is proved below by induction.
The optional maximal-Delta diagnosis uses the finite-rank-cycle characterization in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002).
Yin_C_F0029's conclusion is not used.

<a id="yin_c_f0084-p1"></a>
### Proof yin_c_f0084-p1

Put \(c=1-\varepsilon\) and
\[
\mathcal M=L^\infty([0,1],ds)\oplus\mathbb C,
\qquad
\tau(g,\alpha)=c\int_0^1g(s)\,ds+\varepsilon\alpha.
\]
This is a faithful normal probability trace.
Its standard Hilbert norm is
\[
\|(g,\alpha)\|_H^2=c\|g\|_{L^2(ds)}^2+\varepsilon|\alpha|^2.
\]
Let \(X=(s,2)\), \(p=(1,0)\), and \(f=1-p=(0,1)\).
The spectral projection of \(X\) at \(2\) is \(f\), and the coordinate function generates the interval summand; hence \(\mathcal M=W^*(X)\).

Let \(K\) be the bounded interval Hilbert-transform operator with kernel
\[
(Kg)(t)=\operatorname{pv}\int_0^1\frac{g(s)}{s-t}\,ds,
\qquad \|K\|\leq\pi.
\]
The accepted normalization gives
\[
K(sg)(t)-t(Kg)(t)=\int_0^1g(s)\,ds
\tag{36.3}
\]
as an equality of bounded operators on \(L^2([0,1],ds)\).
One first checks it on smooth compactly supported functions and extends by boundedness.

Define an operator on all of \(H\) by
\[
D(g,\alpha)=
\left(cKg,\;c\int_0^1\frac{g(s)}{s-2}\,ds\right).
\tag{36.4}
\]
The functional in the second component is bounded because \(\int_0^1|s-2|^{-2}\,ds=1/2\).
In particular
\[
\|D\|^2\leq c^2\pi^2+\frac{\varepsilon c}{2}<\infty.
\]
The omitted input component is simply annihilated; (36.4) specifies the actual ambient bounded operator, not only a restriction.

For \(z=(g,0)\in\mathcal E\), (36.3) and cancellation of \(s-2\) in the lower component give
\[
(DX-XD)z
=\left(c\int_0^1g(s)\,ds,\;c\int_0^1g(s)\,ds\right)
=\tau(z)\Omega=Pz.
\]
Also \(fz=0\), so
\[
[D,f]z=-fDz
=\left(0,-c\int_0^1\frac{g(s)}{s-2}\,ds\right).
\tag{36.5}
\]
This range is the one-dimensional atomic summand, and the value for \(g=1\) is nonzero since the integral is \(-\log2\).
Thus its rank is exactly one.

To exclude rationality, every element of \(\operatorname{Div}_{L^0(\mathcal M)}\mathbb C[X]\) has the form
\[
\left(\frac{a(s)}{b(s)},\frac{a(2)}{b(2)}\right),
\qquad a,b\in\mathbb C[s],\quad b\ne0,\quad b(2)\ne0.
\tag{36.6}
\]
Indeed these fractions contain the polynomial algebra and are closed under sums and products.
Such a fraction is invertible in \(L^0(\mathcal M)\) precisely when its numerator is a nonzero polynomial and \(a(2)\ne0\); its inverse again has form (36.6).
Conversely every displayed denominator is nonzero almost everywhere for the probability measure \(c\,ds+\varepsilon\delta_2\), so its inverse is permitted.
This proves the description from the definition of division closure.

If (36.6) equals \(f=(0,1)\), its interval coordinate implies \(a=0\), since a nonzero polynomial cannot vanish almost everywhere on an interval.
Its atomic coordinate would then be zero, a contradiction.
This proves (36.2).

Finally the orthogonal projection onto the atomic Hilbert summand is a nonzero bounded finite-rank operator commuting with \(X\).
The accepted cycle characterization therefore also shows that maximal Delta fails.
This diagnoses why the non-dense test relation cannot replace the density assumption even at the free-field realization step.

### Density Boundary

The example works for every positive omitted trace \(\varepsilon\), however small.
It does not refute a faithful-support condition that forces actual density, a factor-only statement, or a formulation using several test modules with dense aggregate span.

For a left \(\mathcal M\)-module \(\mathcal E\subset H\), asking only that \(\Omega\) lie in its Hilbert closure is equivalent to Hilbert density: multiplication by any \(a\in\mathcal M\) takes approximants for \(\Omega\) to approximants for \(a\Omega\), and those vectors are dense.
Likewise an internal sequence of projections with traces tending to one already implies density.
These are alternative certificates, not genuine weakenings.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:54 |
| status | proved |
| reason | Adopt the exact actual original finding at its complete reviewed scope while preserving the mathematical assessment, fixed argument, dependencies and historical decisions. The original initial context-isolation fact remains unknown; no new or redated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0084-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0084_v1.md#yin_c_f0084-failure-on-a-proper-test-module) | Actual original complete C_F0084 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0084-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0084_v1.md#fresh-c84-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0084-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0084_v1.md#yin_c_f0084-failure-on-a-proper-test-module) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0084_v1.md#yin_c_f0084-failure-on-a-proper-test-module).

Material covered by that review: [Exact material](Yin_C_F0084_v1.md), [Exact material](Yin_C_F0036_v1.md), [Exact material](Yin_C_F0037_v1.md), [Exact material](Yin_C_F0038_v1.md), [Exact material](../ledger/Yin_L_F0019_v1.md) (together retain the original whole-source scope).
