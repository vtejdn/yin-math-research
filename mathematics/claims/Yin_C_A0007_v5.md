---
author: Yin
---
# Defects of expected-support compression

This investigation serves [route five](../strategies/Yin_S_A0005.md) under the [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
It investigates the exact kernel correction for compressing a selfadjoint finite group-ring matrix to the expected support of a finite kernel witness, and whether that correction supplies information independent of the original Atiyah problem.
The directly selected inputs are [L_A0023 v3](../ledger/Yin_L_A0023_v3.md) and [C_A0007 v4](../claims/Yin_C_A0007_v4.md).

## Statement

The initial calculation gives the defect as the rank of the off-corner map restricted to the compression kernel when the complete original kernel lies in the corner.
A finite witness does not itself imply that inclusion.
The next test constructs a finite additive matrix with an explicit finite witness whose expected support is exactly the actual expected-kernel support, while its compression defect equals the rank of an arbitrary Task input.
For every bounded selfadjoint matrix, the exact correction is (3), and under the independently verified inclusion of its complete kernel in the corner it is the nonnegative rank (4).
Deficient rectangular normalization retains the finite boundary rank identity (8), with the explicit corrections (10)--(11).
For every rectangular complex group-ring input over every torsion-free group, (12)--(18) realize its rank as such a correction, even with a witness attaining the actual expected-kernel support.
The independently pivoted family (19)--(21) supplies a directly certified positive class; the last section states the remaining complete-chain gaps.

<a id="argument"></a>
## The exact compression formula and its domains

Let \(\mathcal M\) be a finite von Neumann algebra with faithful finite trace \(\operatorname{tr}\), incorporating any unnormalized matrix amplification into the notation.
Let \(Y=Y^*\in\mathcal M\) be bounded and let \(q\in\mathcal M\) be a projection.
An edge-algebra requirement on \(q\) is unnecessary for this operator identity, but is needed later for the conditional expectation and additive coefficient assertions.
Set
\[
 p=P_{\ker Y},\qquad A_q=qYq:q\mathcal H\longrightarrow q\mathcal H,
 \qquad e=P_{\ker_{q\mathcal H}A_q}\le q,
 \qquad B_q=(1-q)Yq:q\mathcal H\longrightarrow(1-q)\mathcal H.
 \tag{1}
\]
The kernel projection \(e\) is taken in the corner, so the automatic kernel \((1-q)\mathcal H\) of the ambient extension of \(qYq\) is excluded.
All operators in (1), including \(B_qe\), are bounded and defined on their whole indicated Hilbert spaces.
Write \(\operatorname{rk}(B_qe)\) for the trace of its range support, equivalently its initial support by the polar-decomposition rank facts retained in [L_A0006](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement).
No inverse or unbounded pointwise kernel transport occurs here.

For \(x\in e\mathcal H\), the equality \(A_qx=0\) gives \(Yx=B_qx\).
Consequently
\[
 \ker(B_q|_{e\mathcal H})=p\mathcal H\cap q\mathcal H,
 \qquad
 \operatorname{rk}(B_qe)=\operatorname{tr}(e)-\operatorname{tr}(p\wedge q).
 \tag{2}
\]
The latter identity follows by taking the initial support of the bounded operator with domain \(e\mathcal H\); its kernel in that domain is exactly \((p\wedge q)\mathcal H\).
Thus the formula valid without any kernel-inclusion assumption is
\[
 \boxed{\nu_q(A_q)-\nu(Y)
 =\operatorname{rk}(B_qe)
 -\bigl(\operatorname{tr}(p)-\operatorname{tr}(p\wedge q)\bigr).}
 \tag{3}
\]
Selfadjointness is compatible with all intended applications, although the kernel argument (1)--(3) also works for a general bounded square \(Y\).

If the additional inclusion \(p\le q\) has been proved, then \(p\le e\) and the second term in (3) vanishes.
In that case
\[
 \boxed{\delta_q(Y):=\nu_q(qYq)-\nu(Y)
 =\operatorname{rk}\bigl((1-q)YqP_{\ker_q(qYq)}\bigr),
 \qquad 0\le\delta_q(Y)\le\operatorname{tr}(1-q).}
 \tag{4}
\]
The upper bound uses only that the range lies in \((1-q)\mathcal H\).
For an \(n\)-square matrix with the unnormalized trace, the corresponding rank loss is
\[
 \boxed{\operatorname{rk}(Y)-\operatorname{rk}(qYq)
 =n-\operatorname{tr}(q)+\delta_q(Y).}
 \tag{5}
\]
In particular the nullity correction and the ambient rank loss are different quantities.
For [L_A0023 v3](../ledger/Yin_L_A0023_v3.md#a-single-support-compression-and-its-exact-correction), \(n=12\), \(\operatorname{tr}(q)=11\), and \(\delta_q=1\), so (5) gives rank loss two, in agreement with its ranks six and four.

## What an expected witness support actually implies

Let \(\mathcal B\subseteq\mathcal M\) have a faithful trace-preserving conditional expectation \(E\), with its matrix amplification understood.
For a positive bounded operator \(K\), the projection \(s(E(K))\) is the smallest projection in \(\mathcal B\) containing \(s(K)\).
Indeed, with \(q=s(E(K))\), bimodularity gives
\[
 E((1-q)K(1-q))=(1-q)E(K)(1-q)=0.
\]
Faithfulness makes \((1-q)K(1-q)=0\), hence \(K^{1/2}(1-q)=0\) and \(s(K)\le q\).
Conversely \(s(K)\le r\in\mathcal B\) gives \(E(K)=rE(K)r\), so \(s(E(K))\le r\).
This argument applies in particular to \(K=p\), proving
\[
 p\le q_p:=s(E(p)).
 \tag{6}
\]

For a bounded finite kernel witness \(YW=0\), let
\[
 s_W=P_{\overline{\operatorname{ran}W}},\qquad
 q_W=s(E(WW^*)).
\]
Then \(s_W\le p\), \(s_W\le q_W\), and \(q_W\le q_p\).
The final inclusion also follows from \(WW^*\le\|W\|^2p\).
There is no implication \(p\le q_W\) without additional information about the complete analytic kernel.
If \(s_W=p\), that information is available and the minimality characterization gives \(q_W=q_p\).
Full support \(q_W=I\) is another sufficient case, but deficient witness support alone is insufficient.

The failure persists even when every polynomial kernel vector is included.
Use the exact free amalgam and three-square additive matrix \(T\) in [L_A0023 v1](../ledger/Yin_L_A0023_v1.md#an-additive-noncentral-boundary-matrix): \(G=F(z,a,b)\), \(H=\langle z\rangle\), \(\nu(T)=1\), and \(\ker(T:(\mathbb CG)^3\to(\mathbb CG)^3)=0\).
Set \(Y=0_1\oplus T\) and \(W=e_0\).
The complete polynomial kernel of \(Y\) is \(e_0\mathbb CG\), so every finite polynomial witness has expected support at most \(q=e_0e_0^*\), and this \(W\) attains it.
Nevertheless \(p=\operatorname{diag}(1,P_{\ker T})\not\le q\).
Here \(qYq=0_q\), \(B_q=0\), \(\nu_q(qYq)=1\), and \(\nu(Y)=2\).
Equation (3) correctly gives \(-1=0-1\), whereas (4) would give a false equality if its inclusion premise were silently inferred from maximal polynomial witness support.
This example reuses the proved tree-boundary facts, with no new whole-group rank assertion.

## The deficient rectangular construction and the exposed correction

Return to an actual amalgam \(G=G_1*_HG_2\), a finite selfadjoint additive matrix \(Y=Y_1+Y_2\), and a nonzero finite witness \(YW=0\).
Use precisely the coset decomposition of [C_A0007 v4](../claims/Yin_C_A0007_v4.md#statement), now allowing deficient support:
\[
 W=DW_0,\qquad D=(F_1\ \cdots\ F_s)\in M_{n,N}(\mathbb CH),
 \qquad E_H(WW^*)=DD^*,\qquad q=s(DD^*),\qquad N=sk.
 \tag{7}
\]
The stacked witness still satisfies \(E_H(W_0W_0^*)=I_N\) and \(W_0^*W_0=sI_k\), independently of the rank of \(D\).
Define \(Y'_j=D^*Y_jD\) and \(Y'=Y'_1+Y'_2\).
These remain finite selfadjoint vertex matrices, and \(Y'W_0=D^*YW=0\).
Therefore the actual analytic boundary argument of C_A0007 v4 still supplies finite edge matrices \(b'_j\), finite vertex matrices \(Q_j=Y'_j-b'_j\), and
\[
 \operatorname{rk}(Y')=\operatorname{rk}(Q_1)+\operatorname{rk}(Q_2).
 \tag{8}
\]
Only the comparison with the original \(Y\), rather than this normalized analytic interface, used full row rank in that Claim.

Let \((DD^*)^\dagger\) mean the actual affiliated inverse in the support corner \(q\), extended by zero on \(1-q\), and put \(R=D^*(DD^*)^\dagger\).
The inverse exists because \(DD^*\) is injective on its support corner, and subgroup representation transports that actual inverse from \(H\) to \(G\).
All products involving it are closed affiliated products.
Then \(DR=q\), \(qD=D\), and
\[
 Y'=D^*(qYq)D,\qquad R^*Y'R=qYq.
\]
The same two rank inequalities used in C_A0007 v4 give
\[
 \operatorname{rk}(Y')=\operatorname{rk}(qYq),\qquad
 \nu(Y')=N-\operatorname{tr}(q)+\nu_q(qYq).
 \tag{9}
\]
These are rank equalities of bounded endpoint matrices, justified inside the affiliated algebra; no claim is made that \(R\) acts on every original Hilbert-space kernel vector.

If \(p\le q\) is separately known, combining (4), (8), and (9) yields
\[
 \boxed{\nu(Y')=\nu(Y)+N-\operatorname{tr}(q)+\delta_q(Y),}
 \tag{10}
\]
\[
 \boxed{\operatorname{rk}(Y)
 =\operatorname{rk}(Q_1)+\operatorname{rk}(Q_2)
   +n-\operatorname{tr}(q)+\delta_q(Y).}
 \tag{11}
\]
Without that inclusion, replace \(\delta_q(Y)\) on the right sides of (10)--(11) by \(\operatorname{rk}(B_qe)-[\operatorname{tr}(p)-\operatorname{tr}(p\wedge q)]\), as in (3).
Thus finite boundary recovery still leaves the actual support trace, the off-corner rank, and possibly the omitted original kernel dimension to be controlled.
If the edge group already satisfies the complex Atiyah assertion, then \(\operatorname{tr}(q)=\operatorname{rk}_H(D)\) is integral.
If both vertex groups have that property, this edge premise follows from their subgroup rank comparison.
These observations do not make \(\delta_q(Y)\) integral, since \(B_qe\) need not be a finite matrix over either controlled vertex ring.

## An arbitrary Task input occurs as an exact support defect

Let \(\Gamma\) be any torsion-free discrete group and let \(A\in M_{m,n}(\mathbb C\Gamma)\), with \(m,n\ge1\), be the original arbitrary Task input.
Introduce independent infinite-order generators \(z,a,b\) and the actual groups
\[
 H=\langle z\rangle,\qquad
 G_1=\Gamma*F(z,a),\qquad G_2=F(z,b),\qquad
 G=G_1*_HG_2=\Gamma*F(z,a,b).
 \tag{12}
\]
The embeddings are the displayed free-factor embeddings.
The universal property of the free product gives the stated isomorphism, because amalgamation identifies just the two copies of \(z\).
Reduced normal form makes every displayed vertex and \(\Gamma\) embedding injective and keeps \(H\) noncentral in both vertices.
It also shows that these groups are torsion-free: a finite-order element in a free product is conjugate into a factor, while a cyclically reduced word of length at least two has nontrivial powers of increasing length.
No assertion about the Atiyah property of \(\Gamma\) or \(G_1\) is used.
The regular representation decomposes over right cosets of \(\Gamma\), so \(\operatorname{rk}_G(A)=\operatorname{rk}_\Gamma(A)\) by the [Task's subgroup argument](../tasks/Yin_T_A0001_v1.md#reduction-to-finitely-generated-groups).

Set
\[
 R_a=(I_n\ \ -aI_n),\qquad T=AR_a\in M_{m,2n}(\mathbb CG_1),
 \qquad D_b=(3+b+b^{-1})I_m\in M_m(\mathbb CG_2),
\]
\[
 Y=\begin{pmatrix}0_{2n}&T^*\\T&D_b\end{pmatrix}
 =\underbrace{\begin{pmatrix}0&T^*\\T&0\end{pmatrix}}_{Y_1\in M_{2n+m}(\mathbb CG_1)}
 +\underbrace{\begin{pmatrix}0&0\\0&D_b\end{pmatrix}}_{Y_2\in M_{2n+m}(\mathbb CG_2)},
 \qquad q=\operatorname{diag}(I_{2n},0_m).
 \tag{13}
\]
This is a finite selfadjoint additive matrix with actual nonedge coefficients from both vertices when \(A\ne0\).
The matrix \(D_b\) is positive with \(D_b\ge I_m\), since \(\|b+b^{-1}\|\le2\).
Its positivity is independently certified, without knowing a rank of \(A\).

The finite witness
\[
 W=\begin{pmatrix}aI_n\\I_n\\0_{m,n}\end{pmatrix}
 \in M_{2n+m,n}(\mathbb CG_1)
 \tag{14}
\]
satisfies \(YW=0\), since \(T(aI_n,I_n)^{\mathsf T}=Aa-Aa=0\).
Because \(a\notin H\), exact coefficient expectation gives
\[
 E_H(WW^*)=\operatorname{diag}(I_n,I_n,0_m)=q,
 \qquad W^*W=2I_n.
 \tag{15}
\]
Thus the witness expected Gram is not merely supported by \(q\); it equals \(q\) and is uniformly positive on that corner.

The complete kernel inclusion is independently verified.
For a vector \((x,y)\in\ell^2(G)^{2n}\oplus\ell^2(G)^m\), the equation \(Y(x,y)=0\) says
\[
 T^*y=0,\qquad Tx+D_by=0.
\]
Taking the inner product of the second equation with \(y\) and using the first gives \(\langle D_by,y\rangle=0\).
The lower bound on \(D_b\) implies \(y=0\), after which \(Tx=0\).
Conversely those two conditions plainly imply \(Y(x,y)=0\).
Hence
\[
 \ker Y=\ker T\oplus\{0\},\qquad p\le q.
 \tag{16}
\]
Bimodularity gives \(E_H(p)\le q\), while \(WW^*\le2p\) and (15) give \(E_H(p)\ge q/2\).
Consequently
\[
 \boxed{s(E_H(p))=s(E_H(WW^*))=q.}
 \tag{17}
\]
Every finite kernel witness lies in \(q\), by (16), so this witness also attains the maximal possible expected support.
No completeness assertion for its polynomial columns is needed.

The column \(J=(I_n,0)^{\mathsf T}\) satisfies \(R_aJ=I_n\), so \(T=AR_a\) and \(TJ=A\) prove \(\operatorname{rk}_G(T)=\operatorname{rk}_\Gamma(A)\) by bounded rectangular rank monotonicity.
Equations (13) and (16) now give
\[
 qYq=0_q,\qquad
 \nu(Y)=2n-\operatorname{rk}_\Gamma(A),\qquad
 \operatorname{rk}(Y)=m+\operatorname{rk}_\Gamma(A),
\]
\[
 \boxed{\delta_q(Y)=\nu_q(qYq)-\nu(Y)=\operatorname{rk}_\Gamma(A).}
 \tag{18}
\]
This is an exact arbitrary-input encoding, including the finite coefficients, genuine amalgam embeddings, complete kernel inclusion, actual expected support, and all size corrections.
The support compression yields a zero matrix with a displayed full-support finite witness, so its subordination conclusion gives no information about the rank on the right of (18).
In the coset construction (7), all coefficient columns of (14) lie in \(q\), and therefore \(D^*Y_jD=0\) for both \(j\).
Even the two normalized finite vertex matrices are zero in this family.

Universal integrality of these compression defects is equivalent to the original Task assertion: \(\delta_q(Y)=\operatorname{rk}_\Gamma(A)=n-\nu_\Gamma(A)\) for every input.
The equivalence does not use a hypothetical nonintegral example or assert that such an example exists.
It shows that the support formula and the normalized vertex matrices do not themselves constrain the unknown defect to a discrete set.
This family does not refute a future defect theorem restricted to amalgams whose two vertex ranks are independently controlled.
Its first vertex contains the arbitrary \(\Gamma\), so assuming the full complex Atiyah property of \(G_1\) would already imply the desired property for \(\Gamma\) by subgroup restriction.
That stronger premise would therefore resolve the arbitrary input before the compression argument, and cannot be silently counted as a new reduction.

## A genuinely two-vertex class with an independent unit pivot

There is a useful positive class whose correction is certified without any group-wide Atiyah hypothesis.
Let \(G=G_1*_HG_2\) be any actual amalgam, choose \(u_j\in G_j\setminus H\), let \(K_j\in M_r(\mathbb CH)\), and put
\[
 C_j=K_j+u_jI_r,\qquad T=(I_r\ \ C_1\ \ C_2),\qquad
 Y=\begin{pmatrix}0_{3r}&T^*\\T&I_r\end{pmatrix},\qquad
 q=\operatorname{diag}(I_{3r},0_r).
 \tag{19}
\]
Assign the \(C_1,C_1^*\) blocks and constant blocks to vertex one and the \(C_2,C_2^*\) blocks to vertex two, giving a finite selfadjoint additive decomposition.
The displayed first column block of \(T\) is a unit pivot, so \(T(I_r,0,0)^{\mathsf T}=I_r\) and \(\operatorname{rk}(T)=r\).
The kernel calculation (16), now with \(D_b=I_r\), gives \(p\le q\), \(\nu(Y)=2r\), and \(\delta_q(Y)=r\).
These statements use no group-ring division theorem.

There is also a full expected-support witness in the corner:
\[
 W=\begin{pmatrix}-C_1&-C_2\\I_r&0\\0&I_r\\0&0\end{pmatrix},
 \qquad YW=0.
 \tag{20}
\]
Writing its expected Gram on the \(q\)-corner, coefficient expectation gives
\[
 E_H(WW^*)\big|_q=
 \begin{pmatrix}
  K_1K_1^*+K_2K_2^*+2I_r&-K_1&-K_2\\
  -K_1^*&I_r&0\\-K_2^*&0&I_r
 \end{pmatrix}
 =L\operatorname{diag}(2I_r,I_r,I_r)L^*,
\]
\[
 L=\begin{pmatrix}I_r&-K_1&-K_2\\0&I_r&0\\0&0&I_r\end{pmatrix}.
 \tag{21}
\]
The matrix \(L\) has the explicit bounded finite inverse obtained by changing the two minus signs to plus signs.
Consequently (21) is bounded below by a positive multiple of \(q\), so \(q\) is exactly both the witness expected support and the actual expected-kernel support.
The cross terms in \(E_H(C_jC_j^*)\) vanish because \(u_j\notin H\), while \(u_ju_j^*=1\); no centrality assumption on the edge is used.

The family (19) therefore demonstrates an independently certified nonzero compression defect with arbitrary finite edge parameters and both vertex contributions.
Its rank is already determined by the displayed pivot, so it adds an expression-level class and no group-wide Atiyah coverage.
It includes examples over groups not assumed to lie in a known positive class, but does not assert the conjecture for their other matrices.
The new requirement for an informative transfer theorem remains a defect certificate that covers inputs without an already available pivot or equivalent rank computation.

## Complete-chain attempt, known coverage, and continuation boundary

For the original arbitrary \((\Gamma,A)\), the construction (12)--(18) completes an exact route from the input to a finite additive matrix, a displayed witness, its maximal actual expected support, and a full-support compressed problem with finite normalized boundaries.
All these steps are unconditional and their size corrections are explicit.
The first unsupported step toward Task integrality is to certify \(\delta_q(Y)\in\mathbb Z\); equation (18) identifies it with the exact original unknown rank.
Continuing under that extra premise reaches \(\nu_\Gamma(A)=n-\delta_q(Y)\in\mathbb Z\), but contributes no independent proof of that premise.
Replacing it by an assumed whole-vertex Atiyah theorem for \(G_1\) encounters the decisive later scope gap that \(G_1\) contains the arbitrary input group.
There is no proved reduction here to vertices already known to satisfy Atiyah.

For a fixed amalgam whose two vertex ranks are independently controlled, the corresponding conditional chain has distinct remaining obligations.
An arbitrary analytic kernel need not admit a useful finite polynomial witness, as the exact tree-boundary input already demonstrates.
Even a maximal family of polynomial witnesses need not have expected support containing the whole analytic kernel, as the direct sum above demonstrates.
If a finite witness and \(p\le q\) are established, (7)--(11) give finite normalized vertex matrices and isolate the single remaining correction \(\delta_q(Y)\), with \(\operatorname{tr}(q)\) controlled by the known edge ranks.
That defect is the rank of \((1-q)Yqe\) and may involve the compression-kernel projection \(e\), so neither its finiteness over a vertex ring nor its integer trace follows from the displayed formula.
The arbitrary-input family identifies a genuine danger of repackaging the original unknown rank, while leaving open a more restrictive theorem whose additional hypotheses exclude that family for a proved substantive reason.

The [known-results synthesis](../ledger/Yin_L_A0001_v1.md#known-positive-results) already records complex Atiyah for free groups and the finite-edge graph-of-groups permanence theorem, whose torsion-free case includes free products.
Thus when \(\Gamma\) already belongs to a certified positive class and the recorded free-product theorem applies, the free-product ambient groups in (12) give known group coverage.
That comparison is not an input to (18), which holds for every torsion-free \(\Gamma\) without a whole-group integrality assumption.
The maximal-witness counterexample is over the already controlled free group, while the unit-pivot family is a directly computed class of matrices in arbitrary actual amalgams.
No historical novelty, new group-wide permanence theorem, or counterexample to the Task is asserted.

The useful next investigation is a defect certificate for a finite additive input whose vertices have independently controlled ranks, whose complete analytic kernel is known to lie in the finite-witness support, and whose off-corner restriction is not already resolved by a finite unit pivot, an energy argument, or an assumed equivalent rank theorem.
The present formula supplies exact bookkeeping and an arbitrary-input obstruction to treating that bookkeeping as an independent rank constraint.

## Assessment history

### Decision reviewed-support-defects

| Field | Value |
| --- | --- |
| date | 2026-11-11T19:55 |
| status | proved |
| reason | Independent whole-artifact review verifies the exact support-compression corrections, deficient finite-boundary normalization and the family encoding every original Task rank in the correction despite maximal actual expected support. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General compression formula, support inclusion limits, deficient normalization, arbitrary rectangular-input encoding and independently pivoted comparison class. |
| argument | [Argument](#argument) | Complete bounded and affiliated calculations, all sizes, actual group embeddings, analytic boundary interface, examples and full-Task limitations. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0020_v5.md#whole-artifact-finding) | All equations and stated interfaces, including the exact accepted BBL21 source scope and known-coverage comparison. |

## Current assessment

[Selected decision](#decision-reviewed-support-defects)

