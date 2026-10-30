---
author: Yin
---

# Projection windows and local tests in dense left modules

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Yin_C_F0032: Large Projections and Local Test Spaces in Dense Left Modules

<a id="statement"></a>
<a id="yin_c_f0032"></a>

Role: lemma.
Role origin: agent-proposed; the user explicitly authorized this extraction.
Provenance: project deduction, extracted from the argument identified below.
Mathematical status at authorship: proof draft.
Review status at authorship: self-reviewed; independent review pending.
Current proof: candidate [yin_c_f0032-p1](#yin_c_f0032-p1), dated 2026-09-10.

### Extraction Provenance and Authorization

The source is [Yin_C_F0029, Section 2](Yin_C_F0029_v1.md#yin_c_f0029).
The extracted statement retains exactly the projection, window, local closed-graph, and weak-continuity mechanisms.
It states closability directly, rather than requiring the stronger dense left-module certificate inside each adjoint domain.
It allows arbitrary bounded right-product targets, since normality and generation are not used in these mechanisms.
These are explicit removals of assumptions unused by the extracted argument.
Yin_C_F0029 is extraction provenance, not a logical premise or a proof dependency of yin_c_f0032-p1.
The [batch authorization](../ledger/Yin_L_F0014_v1.md#authorization) covers this lemma and its planned uses.

### Statement and Scope

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, and put \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
Use the inner product linear in its second variable.
Let \(\mathcal E\subseteq H\) be a dense left \(M\)-module, and let \(Y_1,\ldots,Y_r\in M\) be a finite family of bounded elements.
They need not be normal or generate \(M\).

There are projections \(e_n,p_n\in M\), not required to be increasing, such that
\[
e_n\in\mathcal E,\qquad
p_n\leq e_n,\qquad
Me_n\subseteq\mathcal E,\qquad
Mp_nY_j\subseteq Me_n\quad(1\leq j\leq r),
\tag{32.1}
\]
and
\[
\tau(1-e_n)\longrightarrow0,\qquad
\tau(1-p_n)\leq(r+1)\tau(1-e_n)\longrightarrow0.
\tag{32.2}
\]
Both sequences converge strongly to \(1\) in the left and right actions on \(H\).
In particular the union of the spaces \(Mp_n\) is dense in \(H\), even though that union need not be an increasing union.

Suppose additionally that \(D_1,\ldots,D_m:\mathcal E\to H\), with domain exactly \(\mathcal E\), are closable complex-linear operators.
For each \(i,n\), there is a finite \(c_{i,n}\) such that
\[
\|D_i z\|_2\leq c_{i,n}\|z\|
\quad(z\in Me_n).
\tag{32.3}
\]
If \(z_\alpha,z\in Me_n\), \(z_\alpha\to z\) in \(L^2\), and \(\sup_\alpha\|z_\alpha\|<\infty\), then
\[
D_i z_\alpha\rightharpoonup D_i z.
\tag{32.4}
\]
For an operator-norm-bounded net \(z_\alpha,z\in Mp_n\) converging in \(L^2\), the same conclusion applies simultaneously to
\[
D_i z_\alpha,\qquad D_i(z_\alpha Y_j),\qquad (D_i z_\alpha)Y_j.
\tag{32.5}
\]
In particular each corresponding map on \(Mp_n\) is bounded from operator norm to Hilbert norm and has this bounded-set weak continuity.
Finite sums of these maps and bounded Hilbert-space operators restricted to \(Mp_n\) have the same properties.

No uniform bound in \(n\), operator-norm estimate for \(D_i^*\), or right invariance of \(\mathcal E\) is asserted.
The required adjoint fact is only that \(\operatorname{Dom}D_i^*\) is dense, equivalently closability of the densely defined \(D_i\).
A dense subspace \(V_i\subseteq\operatorname{Dom}D_i^*\) is a sufficient certificate; its left-module property is not needed for this lemma.

### Proof Dependencies of yin_c_f0032-p1

There are no direct project-claim dependencies.
The accepted analytic inputs are:

- The identification \(H\subseteq U(M)\), affiliated polar decomposition, and bounded spectral calculus for the absolute value of an affiliated operator, at the standard finite-tracial scope recorded in [Miy22-U006](../audits/literature/Miy22/Yin_U006_v1.md#miy22-u006).
- Hilbert-space adjoints and closures, and the closed graph theorem for a linear map between Banach spaces.
- Equality of traces of the left and right supports of a bounded operator, obtained from its polar decomposition; finite subadditivity of projection trace under joins.
- Density of \(M\) in \(L^2(M,\tau)\), and extension of uniformly bounded operator convergence from a dense test subspace.

The argument below verifies the applicability of these inputs.
This extraction does not claim a fresh audit of their original source proofs.

<a id="yin_c_f0032-p1"></a>
### Proof yin_c_f0032-p1

Choose \(z_n\in\mathcal E\) such that \(\|z_n-\Omega\|_2\to0\).
Take the affiliated polar decomposition \(z_n=v_n|z_n|\), and define
\[
e_n=1_{[1/2,\infty)}(|z_n|).
\]
The inverse in
\[
a_n=e_n|z_n|^{-1}v_n^*
\]
is restricted to that spectral support.
Thus \(a_n\in M\), \(\|a_n\|\leq2\), and \(a_nz_n=e_n\).
Left invariance puts \(e_n\) in \(\mathcal E\), and then \(Me_n\subseteq\mathcal E\).

Let \(q_n=1-e_n\).
The spectral definition gives \(\|z_nq_n\|_2\leq\frac12\|q_n\|_2\), so
\[
\|z_n-\Omega\|_2
\geq\|(z_n-\Omega)q_n\|_2
\geq\|q_n\|_2-\|z_nq_n\|_2
\geq\tfrac12\|q_n\|_2.
\]
Therefore
\[
\tau(1-e_n)\leq4\|z_n-\Omega\|_2^2\longrightarrow0.
\tag{32.6}
\]
The vectors \(z_n\) need not be bounded.
Only the left coefficient \(a_n\) must be bounded, and the spectral cutoff supplies that bound.

Write \(l(y)\) and \(r(y)\) for the left and right support projections of \(y\in M\).
Define
\[
p_n=e_n\wedge
\bigwedge_{j=1}^r\bigl(1-l(Y_j(1-e_n))\bigr).
\tag{32.7}
\]
By construction \(p_nY_j(1-e_n)=0\).
Consequently \((ap_n)Y_j=(ap_nY_j)e_n\in Me_n\) for every \(a\in M\).
Moreover \(r(Y_j(1-e_n))\leq1-e_n\), and polar decomposition gives
\[
\tau(l(Y_j(1-e_n)))=\tau(r(Y_j(1-e_n)))\leq\tau(1-e_n).
\]
Taking complements in (32.7) and using projection-trace subadditivity proves the bound in (32.2).

For a projection \(f_n\) with \(\tau(1-f_n)\to0\), bounded \(a\in M\) satisfies
\[
\|(1-f_n)a\|_2,\ \|a(1-f_n)\|_2
\leq\|a\|\tau(1-f_n)^{1/2}.
\]
Since these left and right projection actions are uniformly bounded on \(H\), density of \(M\) extends their convergence to every Hilbert vector.
This proves strong convergence for both \(e_n\) and \(p_n\), with no monotonicity requirement.
For bounded \(a\), \(ap_n\in Mp_n\) and \(ap_n\to a\) in \(H\), proving the claimed density.

For fixed \(i,n\), \(Me_n\) is a closed subspace of the Banach space \(M\) in operator norm.
Suppose \(z_k\to z\) in that norm and \(D_i z_k\to v\) in \(H\).
Then \(z_k\to z\) in \(H\), and the closed Hilbert operator \(\overline D_i\) gives \(\overline D_i z=v\).
Since \(z\in Me_n\subseteq\mathcal E\), this is \(D_i z=v\).
Closed graph now proves (32.3).

For (32.4), test against \(\eta\in\operatorname{Dom}D_i^*\):
\[
\langle\eta,D_i z_\alpha\rangle
=\langle D_i^*\eta,z_\alpha\rangle
\longrightarrow
\langle D_i^*\eta,z\rangle
=\langle\eta,D_i z\rangle.
\]
The test domain is dense by closability, and (32.3) bounds the images uniformly.
Approximating an arbitrary Hilbert test vector by adjoint-domain vectors proves weak convergence.

Finally \(z_\alpha Y_j,zY_j\in Me_n\) by (32.1), their operator norms are bounded by the input bound times \(\|Y_j\|\), and
\[
\|(z_\alpha-z)Y_j\|_2\leq\|Y_j\|\|z_\alpha-z\|_2\longrightarrow0.
\]
Apply (32.4) to these inputs.
Bounded right multiplication takes weakly convergent \(D_i z_\alpha\) to weakly convergent \((D_i z_\alpha)Y_j\).
This proves all of (32.5) and the finite-sum conclusion.

### Version, Review, and Intended Consumers

The candidate yin_c_f0032-p1 is self-contained at the accepted analytic inputs just listed.
Its extraction from a reviewed parent argument does not itself establish review of this newly stated interface.
Peer review is pending.

Its direct intended consumer is [Yin_C_F0033, proof yin_c_f0033-p1](Yin_C_F0033_v1.md#yin_c_f0033-p1).
A future lemma-based proof of Yin_C_F0029 may also invoke it for local test spaces or the large projections used in maximal Delta.
Yin_C_F0024 and Yin_C_F0030 have \(\mathcal E=M\), so they can use the trivial choices \(e_n=p_n=1\) instead.
These are proposed consumer relationships, not changes to the dependencies of their preserved original proofs.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0032-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0020_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:45 |
| status | proved |
| reason | Select the actual retained finding scopes and their known mathematical-development relationships, preserving status, authorized role, exact statement/proof/dependency selections and all historical decisions. No new mathematical review is asserted. |

Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0032-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0020_v1.md#local-test-spaces-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

## Historical assessments


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
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0020_v1.md).

The original whole-source review covered the local test-space and normal-commutation lemmas, their extraction interfaces and proposed uses in the parent criterion.
The exact findings and their source-depth limits remain in the cited review.
