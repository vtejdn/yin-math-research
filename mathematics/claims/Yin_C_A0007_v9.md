---
author: Yin
---
# Finite free translates of an arbitrary kernel and the remaining trace obstruction

This result serves [S_A0005](../strategies/Yin_S_A0005.md#route).
It replaces the integer-rank stopping argument in [v8](Yin_C_A0007_v8.md#kernel-projections-and-the-translate-sum) by a quantitative free-product estimate that applies without an Atiyah hypothesis.
The resulting finite spanning family has a bounded inverse on its expected support.
An exact finite group-ring constraint matrix records the trace that this construction does not determine.

## Statement

Let \(G\) be any discrete group, let \(\Gamma=G*\langle z\rangle\), and put \(M=\mathcal N(\Gamma)\), \(M_0=\mathcal N(G)\).
The application to A0001 takes \(G\) torsion-free, in which case \(\Gamma\) is torsion-free as well.
Write \(E_0=\operatorname{id}_{M_n}\otimes\tau_G\) for the expectation from \(M_n(M_0)\) onto \(B=M_n(\mathbb C)\).
All matrix traces below are unnormalized and incorporate the canonical group trace.

Let \(p\in M_n(M_0)\) be any nonzero projection, and set
\[
 C=E_0(p),\qquad q=s(C),\qquad
 \lambda=\min\operatorname{spec}(C|_{q\mathbb C^n})>0,
 \qquad t=\operatorname{Tr}_n(p),\qquad d=\operatorname{rank}_{\mathbb C}(q).
 \tag{1}
\]
Thus \(0<\lambda\le1\).
For a positive integer \(m\), define exactly \(m\) translates and their sum by
\[
 p_k=z^kpz^{-k}\quad(0\le k<m),\qquad
 S_m=\sum_{k=0}^{m-1}p_k.
 \tag{2}
\]
If \(m\lambda>(1+\sqrt2)^2\), then
\[
 S_m\ge
 \bigl(m\lambda-1-2\sqrt{m\lambda}\bigr)q.
 \tag{3}
\]
In particular the choice
\[
 m=\left\lceil\frac6\lambda\right\rceil
 \quad\hbox{gives}\quad
 S_m\ge(5-2\sqrt6)q>0\quad\hbox{on }q.
 \tag{4}
\]
Consequently the join of these \(m\) projections is exactly \(q\), and \(S_m\) has a bounded inverse in \(qM_n(M)q\).
Neither rationality of \(p\), integrality of \(t\), nor a division ring containing the original input is a premise.
The dependence on a positive lower bound for \(C|_q\) cannot in general be replaced by a bound depending only on \(n\) and \(t\).

For an actual finite input \(A\in M_{a,n}(\mathbb CG)\), take \(p=P_{\ker A}\).
Set \(A_k=z^kAz^{-k}\), entrywise, and form the finite group-ring matrix
\[
 D_m=
 \begin{pmatrix}
 A_0&0&\cdots&0\\
 0&A_1&\cdots&0\\
 \vdots&\vdots&\ddots&\vdots\\
 0&0&\cdots&A_{m-1}\\
 I_n&I_n&\cdots&I_n
 \end{pmatrix}
 \in M_{ma+n,mn}(\mathbb C\Gamma).
 \tag{5}
\]
For every \(m\) satisfying the condition of (3), its regular nullity is exactly
\[
 \nu(D_m)=mt-d.
 \tag{6}
\]
In particular, for two consecutive such sizes,
\[
 \nu(D_{m+1})-\nu(D_m)=t.
 \tag{7}
\]
This is an exact transfer of the unknown trace to finite input matrices, not a proof that the two nullities on the left are integers.

There is also a direct restriction on edge recovery for an unchanged input.
Let \(H=\langle z\rangle\).
If \(Y\in M_n(M_0)\), \(b\in M_n(\mathcal N(H))\), and \((Y-b)p=0\), then
\[
 bq=cq,\qquad c=(\operatorname{id}_{M_n}\otimes\tau_H)(b)\in M_n(\mathbb C).
 \tag{8}
\]
Thus any determined edge action is constant on \(q\); when \(q=I_n\), the whole coefficient \(b\) is constant.

The free projection examples below are operator/probability calibrations.
They are not exhibited kernels of finite matrices over torsion-free group rings and do not constitute counterexamples to A0001.

## Argument

### Freeness and the constant expected support

For integers \(k_1,\ldots,k_l\) with \(k_i\ne k_{i+1}\), and nonidentity elements \(g_i\in G\), the product
\[
 (z^{k_1}g_1z^{-k_1})\cdots(z^{k_l}g_lz^{-k_l})
 =
 z^{k_1}g_1z^{k_2-k_1}g_2\cdots
 z^{k_l-k_{l-1}}g_lz^{-k_l}
\]
is nonidentity by free-product normal form.
Here only adjacent indices must differ; the entire list need not have distinct entries.
It follows first on group polynomials, and then on the von Neumann closures, that the algebras \(z^kM_0z^{-k}\) are scalar free for different \(k\).
Their matrix amplifications are free over \(B=M_n(\mathbb C)\) for the entrywise trace expectation.
This follows by expanding a centered alternating matrix product into products of centered entries.

Faithfulness of the expectation gives
\[
 E_0((I-q)p(I-q))=(I-q)C(I-q)=0
 \quad\Longrightarrow\quad p\le q.
 \tag{9}
\]
Since \(q\) is a constant matrix, \(p_k\le q\) for every \(k\).
The compressions by \(q\) remain free over \(qBq\), with its identity \(q\) and its compressed expectation.
The expectation onto the different algebra \(M_n(\mathcal N(H))\) also satisfies
\[
 E_H(p)=C,
 \tag{10}
\]
because \(G\cap H=\{e\}\).
The finite-dimensional matrix \(C|_q\) has the strictly positive minimum eigenvalue in (1).
No lower bound for that eigenvalue is being inferred from \(t\) alone.

### A norm estimate with explicit constants

We use the following length-one estimate for selfadjoint centered elements \(x_k\) from free algebras over a common base, with expectation \(E\):
\[
 \left\|\sum_k x_k\right\|
 \le
 \max_k\|x_k\|
 \,+\,2\left\|\sum_k E(x_k^2)\right\|^{1/2}.
 \tag{11}
\]
For completeness, its upper bound follows directly from the reduced free-product representation.
Let \(\Pi_k\) be the projection onto words whose first centered letter comes from the \(k\)-th algebra.
These projections are mutually orthogonal and commute with the left action of the base.
Centered multiplication decomposes as
\[
 x_k=\Pi_kx_k\Pi_k+
       \Pi_kx_k(I-\Pi_k)+(I-\Pi_k)x_k\Pi_k.
 \tag{12}
\]
The first terms in (12) have orthogonal domain and range blocks, so their sum has norm at most \(\max_k\|x_k\|\).
For the sum \(L=\sum_k\Pi_kx_k(I-\Pi_k)\) of creation terms, orthogonality and the centered free-product action give
\[
 L^*L
 =\sum_k(I-\Pi_k)E(x_k^2)(I-\Pi_k)
 \le \sum_k E(x_k^2).
 \tag{13}
\]
The remaining sum is \(L^*\), since \(x_k=x_k^*\).
The triangle inequality proves (11).
The representation is faithful, so these are the original operator norms.
This is the creation, diagonal and annihilation decomposition in
[RX06, Section 1 and Lemmas 2.1--2.3](https://arxiv.org/html/math/0505302v2#S2), with the Hilbert-module extension explained in [Section 5](https://arxiv.org/html/math/0505302v2#S5).
The argument above supplies the particular constants used here.
The [selected local edition](../literature/pdf/RX06--arxiv-v2.pdf) is arXiv v2.

All subsequent operations take place in the corner with identity \(q\).
Let \(C_q^{-1/2}\) denote the inverse square root on that corner, extended by zero on its complement, and put
\[
 u_k=C_q^{-1/2}p_kC_q^{-1/2},\qquad x_k=u_k-q.
 \tag{14}
\]
These variables are free over \(qBq\), and
\[
 E(u_k)=q,\qquad 0\le u_k\le\lambda^{-1}q,\qquad
 \|x_k\|\le\max\{1,\lambda^{-1}-1\}\le\lambda^{-1}.
 \tag{15}
\]
The centered row and column variance bounds coincide because each \(x_k\) is selfadjoint.
More explicitly,
\[
 E(x_k^*x_k)=E(x_kx_k^*)=E(u_k^2)-q
 \le(\lambda^{-1}-1)q\le\lambda^{-1}q.
 \tag{16}
\]
Here \(u_k^2\le\lambda^{-1}u_k\), by positive functional calculus.
Equation (11) therefore yields
\[
 \left\|\sum_{k=0}^{m-1}x_k\right\|
 \le \lambda^{-1}+2\sqrt{m/\lambda}.
 \tag{17}
\]
It follows that
\[
 S_m=C^{1/2}\left(mq+\sum_{k=0}^{m-1}x_k\right)C^{1/2}
 \ge \left(m-\lambda^{-1}-2\sqrt{m/\lambda}\right)C.
 \tag{18}
\]
When \(m\lambda>(1+\sqrt2)^2\), the scalar multiplying \(C\) in (18) is positive.
Only in this case do we use \(C\ge\lambda q\) to deduce (3).
For (4), \(m\lambda\ge6\), and the function \(s-1-2\sqrt s\) is increasing for \(s>1\).
This proves the stated lower bound \(5-2\sqrt6>0\).
Since all summands are supported on \(q\), (3) identifies their join with \(q\).

If \(p=0\), which was excluded in (1), all translates and their join are zero and no parameter \(\lambda\) is needed.

### The exact remaining kernel

Retain the actual finite group-ring input in (5).
Let
\[
 P=\operatorname{diag}(p_0,\ldots,p_{m-1}),\qquad
 R=(p_0\ \cdots\ p_{m-1}).
 \tag{19}
\]
This bounded \(n\)-by-\(mn\) row satisfies \(R=RP\) and \(RR^*=S_m\).
By (3), its range is the whole closed corner \(qL^2(M)^n\).
Write \(S_{m,q}^{-1}\) for the bounded inverse on that corner, extended by zero elsewhere.
The operator
\[
 Q=R^*S_{m,q}^{-1}R
 \tag{20}
\]
is the orthogonal projection onto the complement of the kernel of \(R\).
It satisfies \(Q\le P\), and its trace equals \(\operatorname{Tr}_n(q)=d\), by the polar decomposition of \(R\).

The first \(ma\) rows of \(D_m\) require each coordinate vector \(\xi_k\) to lie in \(\ker A_k\).
Thus they require \((\xi_k)_k\in P L^2(M)^{mn}\).
On this subspace, the last \(n\) rows of \(D_m\) are exactly \(R\).
Consequently
\[
 P_{\ker D_m}=P-Q,\qquad
 \nu(D_m)=\operatorname{Tr}_{mn}(P)-\operatorname{Tr}_{mn}(Q)=mt-d.
 \tag{21}
\]
This proves (6), with both the input and output sizes specified in (5).
Applying the same formula to \(m+1\) gives (7).
All entries of \(D_m\) are finite group-ring expressions even though the projections in its proof need not be rational.

There is a conditional algebraic use of (7) with no ambient Atiyah premise.
If the two particular finite matrices \(D_m,D_{m+1}\) have independent integer-nullity certificates, then \(t\) is an integer.
For example, explicit invertible row and column operations in the actual affiliated algebra reducing each matrix to an identity block and zero blocks supply such certificates when every pivot inverse is independently justified.
This condition is about these concrete reductions; assuming the entire enlarged group has Atiyah would instead assume the needed conclusion.
The free-spanning estimate proves neither certificate.
Without independent reductions, (21) locates the original unknown trace inside another group-ring kernel.

### Free projections with arbitrary real trace

For clarity, the scalar free-projection join formula used in the calibration is
\[
 \tau(e\vee f)=\min\{\tau(e)+\tau(f),1\}
 \tag{22}
\]
for free projections \(e,f\) in a tracial probability space.
It follows from the already accepted [BBL21, Theorem 3.5(vii), arXiv v2, PDF p.8](../literature/pdf/BBL21--arxiv-v2.pdf#page=8), as follows.
Put \(\alpha=\tau(e)\), \(\beta=\tau(f)\), and \(r=P_{\ker(e+f)}\).
Positivity gives \(r=(1-e)\wedge(1-f)\).
If \(\tau(r)>0\), its scalar expectation has a bounded inverse.
The source theorem supplies scalar boundary values \(b_1,b_2\) and the kernel inclusions.
Since \(er=fr=0\), these inclusions force \(b_1=b_2=0\).
The trace identity is therefore
\[
 (1-\alpha)+(1-\beta)=1+\tau(r),
 \qquad \tau(r)=1-\alpha-\beta.
 \tag{23}
\]
When \(\alpha+\beta<1\), the general projection-dimension inequality already gives
\(\tau(r)\ge1-\alpha-\beta>0\), so (23) applies.
When \(\alpha+\beta\ge1\), a positive \(\tau(r)\) would contradict (23), so \(r=0\).
This proves (22).
The analytic theorem is used at its [retained source interface](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), not re-proved here.

For every real \(0<\delta<1\), take an arc projection \(e_\delta\) of Haar measure \(\delta\) in \(\mathcal N(\langle u\rangle)\cong L^\infty(\mathbb T)\).
Inside \(\mathcal N(\langle u\rangle*\langle z\rangle)\), its conjugates
\(e_{\delta,k}=z^ke_\delta z^{-k}\) are free projections of trace \(\delta\).
The join of the first \(m-1\) belongs to the algebra generated by those factors and is free from the next projection.
Induction in (22) gives
\[
 \tau\left(\bigvee_{k=0}^{m-1}e_{\delta,k}\right)=\min\{m\delta,1\}.
 \tag{24}
\]
For \(m=\lceil6/\delta\rceil\), the stronger bound (4) also gives a bounded inverse for their sum.
The normalized frame (19)--(20) then has residual projection of trace
\[
 m\delta-1.
 \tag{25}
\]
For irrational \(\delta\), this trace is irrational.
Thus actual freeness, finite spanning, a bounded inverse, and the resulting polar normalization coexist with every real original trace in \((0,1)\).
The projection \(e_\delta\) is measurable functional calculus in a cyclic group algebra.
It has not been exhibited as the kernel of a finite group-ring matrix.
Equations (24)--(25) exclude a trace-quantization argument using only these analytic features; they do not exhibit a failure of the group-ring conjecture.

The order \(1/\lambda\) in the sufficient count cannot generally be improved to a smaller order.
For the scalar calibration, \(\lambda=\delta\), and (24) requires \(m\delta\ge1\) even to have full support.
There is also no count determined by \(n\) and \(t\) alone.
Fix \(0<t<1\), let \(0<\varepsilon<t/2\), and use
\[
 p=\operatorname{diag}(e_{t-\varepsilon},e_\varepsilon)
 \quad\hbox{in }M_2(\mathcal N(\langle u\rangle)).
 \tag{26}
\]
Here \(q=I_2\), \(\operatorname{Tr}_2(p)=t\), and \(\lambda=\varepsilon\).
The second diagonal coordinate of the join of \(m\) translates has trace
\(\min\{m\varepsilon,1\}\), by (24).
Full support therefore requires \(m\varepsilon\ge1\), although \(n=2\) and \(t\) remain fixed.
These are again operator/probability examples, not finite group-ring kernel witnesses.

### Edge coefficients for an unchanged original input

Suppose \((Y-b)p=0\) as in (8).
The subgroup expectation \(E_G:M_n(M)\to M_n(M_0)\) sends \(b\) to the constant matrix \(c\), since \(G\cap H=\{e\}\).
Bimodularity gives
\[
 Yp=E_G(bp)=cp,
 \qquad (b-c)p=0.
 \tag{27}
\]
Taking the expectation onto the edge algebra instead yields
\[
 0=E_H((b-c)p(b-c)^*)=(b-c)C(b-c)^*.
 \tag{28}
\]
Hence \((b-c)C^{1/2}=0\).
The inverse of \(C^{1/2}\) on its finite-dimensional support gives \((b-c)q=0\), proving (8).
No selfadjointness or boundary-limit existence was needed for this restriction.
If \(b\) is supplied by an actual subordination problem, it obeys the same restriction whenever \(Y\) and \(p\) remain in the original factor.
A different realization with summands involving new free letters is outside this last assertion and needs its own kernel and coefficient analysis.

### Scope of the advance

The finite-join obstruction left open by the absence of integer ranks is removed in this free extension: (3) supplies a quantitative bounded inverse on the exact expected support for every projection.
This fact alone supplies no algebraic formula for the original projection from the finite input \(A\).
In particular the inverse is an inverse of a sum of analytic projections, whose membership in a chosen rational closure has not been established.
The free calibrations and (21) show exactly where the original unrestricted trace survives.
Further progress requires an independently justified algebraic certificate for the residual matrices, or a different realization that uses additional information from the original finite group-ring coefficients.

## Assessment history

### Decision free-spanning

| Field | Value |
| --- | --- |
| date | 2026-11-21T04:11 |
| status | proved |
| reason | Independent whole-proof inspection supports the stated result at its declared scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Quantitative bounded spanning, finite group-ring matrices and determined edge restriction. |
| argument | [Proof](#argument) | Complete free-product norm and trace calculations, calibrations and scope. |
| review | [Whole finding](../audits/reviews/Yin_R_A0020_v9.md#whole-finding) | Complete independent review including the external interfaces and limitations stated in the finding. |

## Current assessment

[Selected decision](#decision-free-spanning)
