---
author: Yin
---

# Positive certificates, the full positive cone and the ordered affine determinant formula

## Current assessment
[Selected decision](#decision-internal-review)

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(s_1,\ldots,s_n\) be free standard semicircular elements.
For selfadjoint \(a,a_1,\ldots,a_n\in M_d(\mathbb C)\), put \(S=a+\sum_j a_js_j\), \(\eta(x)=\sum_j a_jxa_j\) and \(\mathcal C_b(x)=bxb\).
The empty noise family is allowed, all traces in the formula are normalized, and zero determinants are included.
The strict Hilbert--Schmidt domain \(\{b>0:\mathcal C_b-\eta\succ0\}\) is equivalent to the existence of \(q>0\) with \(bqb-\eta(q)>0\), and is in bijection with every positive \(q\) through
\[
 b(q)=q^{-1/2}[q^{1/2}(I+\eta(q))q^{1/2}]^{1/2}q^{-1/2},\qquad
 q=(\mathcal C_b-\eta)^{-1}(I).
\]
At that unrestricted positive trial,
\[
 \log\Delta(S)=-\tfrac12+\inf_{q>0}\max_{h=h^*}
 \left\{\frac1{2d}\log\frac{\det(I+\eta(q))}{\det q}
 +\operatorname{tr}_d(ah)-\tfrac12\operatorname{tr}_d(hb(q)hb(q)+h\eta(h))\right\}.
\]
For each \(q\) the inner maximum is finite and uniquely attained; no interchange of extrema or outer attainment is asserted.
The equivalent inverse-map formula and the entire centered capacity reduction, including singular outputs, zero capacity and nonattainment, are proved below.
For arbitrary complex coefficients the stated extension is through the size-\(2m\) hermitization and its capacity-square identity, not by deleting pseudo-covariance.

## Provenance and accepted inputs

The complete positive-certificate, bijection, quadratic-completion and capacity argument is retained from [L_F0031](../ledger/Yin_L_F0031_v1.md), authored by root on 2026-09-13.
Its general determinant equality is an explicit reformulation of the [C_F0124 strict-domain theorem](Yin_C_F0124_v1.md#statement), whose Spe26 proposal attribution and project proof are retained; this is not a second independent general proof.
The original [R_F0123 Section 2 finding](../audits/reviews/Yin_R_F0123_v1.md#2-positive-certificates-and-the-full-positive-cone) checked this full module at its original fixed L input and disclosed mathematical collaboration.

## Argument

### 1. Replace the Hilbert--Schmidt Constraint by a Positive Certificate

Use the selfadjoint setting and normalized trace of Yin_C_F0124: \(S=a+\sum_j a_js_j\) in matrix size \(d\), with \(a,a_j\) selfadjoint and \(\eta(x)=\sum_j a_jxa_j\).
For \(b>0\), let \(\mathcal C_b(x)=bxb\).
Then
\[
 \mathcal C_b-\eta\succ0\text{ on Hilbert--Schmidt space}
 \quad\Longleftrightarrow\quad
 \exists q>0:\ bqb-\eta(q)>0.
                                                               \tag{1}
\]
For the reverse direction, put \(\Psi=\mathcal C_{b^{-1/2}}\eta\mathcal C_{b^{-1/2}}\) and \(W=b^{1/2}qb^{1/2}>0\).
The certificate says \(W-\Psi(W)>0\).
Conjugating the map by \(W^{1/2}\) makes it strictly subunital, hence its spectral radius is less than one.
Since \(\Psi\) is Hilbert--Schmidt selfadjoint, \(I-\Psi\succ0\), proving the left side.
This is the positive-map contraction argument already checked in Yin_C_F0124.

Conversely, the left side gives \(\|\Psi\|_{2\to2}<1\), including the negative-eigenvalue control proved in Yin_C_F0124.
The geometric series \((I-\Psi)^{-1}=\sum_{k\ge0}\Psi^k\) is completely positive.
Therefore
\[
 q=(\mathcal C_b-\eta)^{-1}(I)
 =b^{-1/2}(I-\Psi)^{-1}(b^{-1})b^{-1/2}>0,
                                                               \tag{2}
\]
and it satisfies the stronger certificate \(bqb-\eta(q)=I\).
Strict positivity of \(q\) follows already from the zeroth geometric-series term.
Thus the certificate can always be normalized to the fixed identity matrix.

### 2. A Bijection with All Positive Trial Matrices

For every freely chosen \(q>0\), define
\[
 b(q)=q^{-1/2}
       \left(q^{1/2}(I+\eta(q))q^{1/2}\right)^{1/2}q^{-1/2}.
                                                               \tag{3}
\]
This is the unique positive solution of
\[
 b(q)\,q\,b(q)=I+\eta(q).
                                                               \tag{4}
\]
To verify uniqueness, conjugate (4) by \(q^{1/2}\) and use uniqueness of the positive square root.
Equations (1)--(2) show that \(q\mapsto b(q)\) is a bijection from the entire positive cone onto the strict feasible set of Yin_C_F0124: its inverse is (2), and (4) proves both compositions.
In particular, this substitution loses no admissible matrix and adds no closure assumption.

Taking determinants in (4) gives
\[
 \Delta_d(b(q))
 =\left(\frac{\det(I+\eta(q))}{\det q}\right)^{1/(2d)}.
                                                               \tag{5}
\]
Hence Yin_C_F0124 is equivalently the single-positive-variable infimum
\[
 \Delta(S)=e^{-1/2}\inf_{q>0}
 \left(\frac{\det(I+\eta(q))}{\det q}\right)^{1/(2d)}
 \exp\left[\frac12\operatorname{tr}_d
       \left(a(\mathcal C_{b(q)}+\eta)^{-1}(a)\right)\right].
                                                               \tag{6}
\]
Every positive matrix is a permitted trial.
The map inverse remains a finite linear solve, but its existence and positivity as a Hilbert--Schmidt operator follow automatically from (4), rather than being an additional feasibility test.

### 3. An Ordered Formula Without an Inverse Linear Map

For each \(q>0\), strict positivity of \(\mathcal C_{b(q)}+\eta\) gives the elementary quadratic identity
\[
 \frac12\langle a,(\mathcal C_{b(q)}+\eta)^{-1}(a)\rangle_2
 =\max_{h=h^*}
 \left\{\operatorname{tr}_d(ah)
 -\frac12\operatorname{tr}_d(hb(q)hb(q))
 -\frac12\operatorname{tr}_d(h\eta(h))\right\}.
                                                               \tag{7}
\]
The maximum is attained at a unique \(h\), by completing the square in the real Hilbert space of Hermitian matrices.
Equation (6) therefore also gives
\[
 \log\Delta(S)=-\frac12+\inf_{q>0}\max_{h=h^*}
 \left\{\frac1{2d}\log\frac{\det(I+\eta(q))}{\det q}
       +\operatorname{tr}_d(ah)
       -\frac12\operatorname{tr}_d(hb(q)hb(q)+h\eta(h))\right\}.
                                                               \tag{8}
\]
The order of extrema is part of this assertion.
Neither a minimax interchange nor convexity of the reduced objective in ordinary matrix coordinates is asserted.
This reformulation uses only positive square roots, ordinary traces and determinants, and freely chosen positive/Hermitian matrices.

### 4. The Zero-Mean Reduction Is Now Immediate

If \(a=0\), the inner maximum in (8) is identically zero at \(h=0\).
For every positive map \(\eta\),
\[
 \inf_{q>0}\frac{\det(I+\eta(q))}{\det q}
   =\operatorname{cap}(\eta).
                                                               \tag{9}
\]
The left side is at least capacity because \(I+\eta(q)\ge\eta(q)\ge0\) and determinant is monotone on the positive semidefinite cone.
Conversely, for any fixed \(r>0\), set \(q=tr\).
Then
\[
 \frac{\det(I+\eta(tr))}{\det(tr)}
 =\frac{\det(t^{-1}I+\eta(r))}{\det r}
 \longrightarrow\frac{\det\eta(r)}{\det r}
 \quad(t\longrightarrow\infty).
\]
Take the infimum over \(r\).
This proves (9) even when \(\eta(r)\) is singular, capacity is zero, or no capacity optimizer exists.
Thus (6) becomes exactly
\[
 \Delta\left(\sum_j a_js_j\right)
 =e^{-1/2}\operatorname{cap}(\eta)^{1/(2d)}.
\]
For arbitrary complex coefficients, apply the same formula to the size-\(2m\) hermitization from Yin_C_F0124.
Its already proved identity \(\operatorname{cap}(\Theta)=\operatorname{cap}(\eta_0)^2\) gives the original full MS24 coefficient scope.
No additional Dyson condition is introduced when setting the mean to zero.

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
| review | [Internal finding](../audits/reviews/Yin_R_F0175_v1.md#positive-cone-finding) | Entire positive-certificate, bijection, ordered formula and centered-reduction chain with exact accepted C_F0124 interfaces. |

