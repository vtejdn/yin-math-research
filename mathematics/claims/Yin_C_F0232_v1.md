---
author: Yin
---
# Coarse derivation rank of the two-point modulus algebra and its normal encodings

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(k\ge1\) be an integer, \(G=\langle u,s\mid s^2=1\rangle=\mathbb Z*\mathbb Z_2\), and \(\mathcal A_k=M_k(\mathbb C)\otimes\mathbb CG\) inside \(M=M_k(\mathbb C)\bar\otimes L(G)\) with its normalized product trace.
Let \(y_1,\ldots,y_d\) generate \(\mathcal A_k\) as a unital star algebra.
Suppose that for every \(1\le i\le d\) there is a complex-linear outer derivation \(\delta_i:\mathcal A_k\to L^2(M)\otimes_2L^2(M)\) satisfying \(\delta_i y_j=\delta_{ij}1\otimes1\).
Then
\[
                            d\le 1+\frac1{2k^2}.                         \tag{1}
\]
In particular \(\mathcal A_k\) has no normal star-generating tuple satisfying the actual ACSY condition.
The rank bound itself requires neither normality nor any vacuum-adjoint hypothesis.

For the unamplified algebra set \(p=(1+s)/2,\ h_\varepsilon=\varepsilon p+1-p,\ Z_\varepsilon=u h_\varepsilon\).
None of the normal pairs
\[
 (\operatorname{Re}Z_\varepsilon,\operatorname{Im}Z_\varepsilon),
 \qquad (u,h_\varepsilon),\qquad 0\le\varepsilon\le1/2
\]
satisfies actual ACSY in its generated tracial von Neumann algebra.
Suppose \(Y^{(n)}\) are actual ACSY normal pairs on a common operator norm cutoff, with actual coordinate vacua \(\xi_{1,n},\xi_{2,n}\).
If there are \(\varepsilon_n\in[0,1/2]\) and a choice of either displayed pair at each \(n\) such that every fixed star-word trace at \(Y^{(n)}\) differs from the corresponding encoding trace by a quantity tending to zero, then
\[
                          \max_{i=1,2}\|\xi_{i,n}\|_2\longrightarrow\infty .
\]
For any fixed \(k\) and any fixed normal tuple that star-generates \(\mathcal A_k\), the same divergence of the maximum holds for normal actual ACSY tuples of the same length on a common cutoff converging to its star law.

## Argument

### Matrix units and coarse derivation parameters

Write \(\mathcal B=M\bar\otimes M^{\rm op}\) with its product trace and identify the coarse space with \(L^2(\mathcal B)\) by \(a\otimes b\mapsto a\otimes b^{\rm op}\).
The outer actions are left multiplication on the first tensor leg and right multiplication on the second.
Thus the outer multiplications act by left operators in \(\mathcal B\), and right multiplication by each \(c\in\mathcal B\) commutes with them.
Write \(F=M_k(\mathbb C)\) and denote by \(e_{ab}\) the matrix units in \(F\otimes1\), and below write \(u,s\) for \(1_F\otimes u,1_F\otimes s\).
For an outer derivation \(\delta\) define \(\eta_0=k^{-1}\sum_{a,b}e_{ab}\cdot\delta(e_{ba})\).
The matrix-unit identity \(\sum f e_{ab}\otimes e_{ba}=\sum e_{ab}\otimes e_{ba}f\) for \(f\in F\), followed by \(x\otimes y\mapsto x\cdot\delta y\), gives \(\delta f=f\cdot\eta_0-\eta_0\cdot f\).
The projection onto \(F\)-central vectors in the coarse space is left multiplication by
\[
 Q=\frac1k\sum_{a,b} e_{ab}\otimes (e_{ba})^{\rm op},\qquad
                      \tau_{\mathcal B}(Q)=k^{-2}.
\]
Indeed the matrix-unit rules give \(Q^*=Q=Q^2\), its image commutes with every matrix unit under the outer actions, and it fixes every \(F\)-central vector.
Replacing \(\eta_0\) by \(\eta=(1-Q)\eta_0\) leaves its inner derivation \(\delta^{\rm in}(x)=x\cdot\eta-\eta\cdot x\) unchanged on \(F\).
The residual derivation \(\delta'=\delta-\delta^{\rm in}\) kills \(F\).
Since \(u,s\) commute with \(F\), both \(v=\delta'u\) and \(w=\delta's\) are \(F\)-central.
Since \(s=s^{-1}\), the relation \(s^2=1\) also gives \((s\otimes s^{\rm op})w=-w\).
Thus \(v\in QL^2(\mathcal B)\) and \(w\in QP_-L^2(\mathcal B)\) for \(P_-=(1-s\otimes s^{\rm op})/2\).
The projections \(Q,P_-\) are in separate tensor factors after regrouping the matrix and group legs, so they commute and \(\tau_{\mathcal B}(QP_-)=1/(2k^2)\), using \(\tau(s)=0\).

Fix expressions for the \(y_j\) in matrix units and \(u,u^{-1},s\).
Their derivatives are bounded linear functions of \((\eta,v,w)\) given by a single \(d\)-by-three matrix \(C\) over \(\mathcal B\) acting on the left.
For the inner term use \(y_j\cdot\eta-\eta\cdot y_j\), and for the residual terms apply the word rule with \(\delta'(u^{-1})=-u^{-1}\cdot v\cdot u^{-1}\) and \(\delta's=w\).
Put \(D=\operatorname{diag}(1-Q,Q,QP_-)\).
For each \(i\), the actual \(\delta_i\) supplies a vector in \(DL^2(\mathcal B)^3\) whose image under \(C\) is the \(i\)-th coordinate unit vector of \(L^2(\mathcal B)^d\) with entry \(1_{\mathcal B}\).
Right multiplication by \(c\in\mathcal B\) commutes with \(CD\), so its image contains every coordinate vector with entry \(c\) and is dense.
Consequently the polar partial isometry of the rectangular matrix \(CD\) has final projection \(I_d\) and initial projection at most \(D\).
Equality of their unnormalized matrix traces over \(\tau_{\mathcal B}\) gives \(d\le(1-k^{-2})+k^{-2}+(2k^2)^{-1}\), proving (1).

### Normal encodings and moment perturbations

One normal generator generates an abelian star algebra, and \(\mathcal A_k\) contains the noncommuting \(u,s\).
With two or more candidate coordinates (1) excludes even the normalized derivations.
In particular, at \(k=1\) set \(Z=u(\varepsilon p+1-p)\) for \(p=(1+s)/2\).
For \(0<\varepsilon\le1/2\), the represented core of \(Z\) contains \(p=(1-Z^*Z)/(1-\varepsilon^2)\) and \(u=Zh_\varepsilon^{-1}\) by [the group-ring calculation](Yin_C_F0225_v1.md#the-represented-coordinates-and-their-derivation).
Thus both the normal pair \((\operatorname{Re}Z,\operatorname{Im}Z)\) and the polar pair \((u,\varepsilon p+1-p)\) generate the full represented \(\mathbb CG\), and neither gives normal ACSY.
At the limit \(\varepsilon=0\), one has \(Z=u(1-p)\) and \(1-p=Z^*Z\), but the modulus has no inverse.
For the polar pair the full star algebra is still generated, since the two coordinates explicitly give \(u\) and \(p\).
For \((\operatorname{Re}Z,\operatorname{Im}Z)\) at \(\varepsilon=0\), a separate kernel argument suffices.
Indeed \(Zp=0\), and \(Z^*(upu^*)=0\).
A normalized derivation at \(\operatorname{Re}Z\) for that selfadjoint pair would be closable by [the normal phase theorem](Yin_C_F0076_v1.md#statement) under actual ACSY and satisfy \(\delta Z=1\otimes1\).
The [two-kernel identity](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) would force \(upu^*\otimes p=0\), despite both projections having trace \(1/2\).
Here the projections are in the generated von Neumann algebra since they equal \(1-ZZ^*\) and \(1-Z^*Z\).

Consequently these two normal encoding families cannot even be star-moment limits of uniformly bounded normal ACSY tuples with uniformly bounded vacua.
More precisely, suppose a sequence of normal actual ACSY laws on a fixed cutoff approaches a fixed such encoding in moments, at any \(0\le\varepsilon\le1/2\).
Then the maximum of its coordinate vacuum norms tends to infinity, since a bounded subsequence would give actual ACSY at that limit by [the compact normal-law theorem](Yin_C_F0201_v2.md#statement).
This conclusion holds also for sequences whose fixed-degree moment discrepancies from the encoding at a varying \(\varepsilon_n\) tend to zero at every degree.
Otherwise take a bounded-vacuum subsequence, fix the encoding type on a further subsequence, and pass to \(\varepsilon_n\to\varepsilon\) by compactness of the parameter interval.
The encoded operators themselves are norm-continuous in \(\varepsilon\), giving one of the excluded limiting laws.
The same fixed-target compactness argument applies at every \(k\) to a normal encoding generating the full matrix-amplified star algebra.

### Comparison with the known dimension formulas

The number on the right of (1) also equals the known free Stein dimension \(\sigma(\mathcal A_k)\).
Lück's free-product formula gives \(\beta_0^{(2)}(G)=0\) and \(\beta_1^{(2)}(G)=1-1/2=1/2\), using the infinite cyclic and order-two factors, whose first Betti numbers in \(L^2\)-homology are zero. [Lück, *\(L^2\)-Invariants*, Example 1.38](../literature/pdf/Luc02--book-manuscript.pdf)
Connes and Shlyakhtenko identify the tracial group-algebra Betti numbers with the corresponding group Betti numbers. [CS05, Proposition 2.3, equations (2.12)–(2.13)](../literature/pdf/CS05--arxiv-v1.pdf)
For a selfadjoint star-generating list of \(\mathbb CG\), the group-algebra formula of Charlesworth and Nelson gives \(\sigma(\mathbb CG)=1+\beta_1^{(2)}(G)-\beta_0^{(2)}(G)=3/2\).
Its proof identifies the corresponding nonmicrostates free entropy dimensions for that selfadjoint list through Mineyev and Shlyakhtenko's theorem. [CN21, Proposition 5.1 and its proof, arXiv v2, p. 17](../literature/pdf/CN21--arxiv-v2.pdf)
The algebraic matrix amplification formula then gives \(\sigma(\mathcal A_k)=1+k^{-2}(\sigma(\mathbb CG)-1)\). [CN25, Theorem 2.5, arXiv v2, p. 8](../literature/pdf/CN25--arxiv-v2.pdf)
The preceding proof checks the actual normalization at arbitrary complex generators directly on the whole represented star algebra, including for derivations with no vacuum hypothesis.
The [CN21 restriction discussion](../audits/literature/CN21/Yin_U001.md#restriction-is-not-extension) and the [CN25 module discussion](../audits/literature/CN25/Yin_U001.md#actual-derivations-versus-their-closure) describe the distinction between actual domain assertions and module dimension.
The numerical dimension formulas are contextual identifications and are not used to infer the existence or extension of any derivation.

## Scope and provenance

The check_defect agent developed the matrix-unit proof and its application to normal encodings for Yin during the investigation of [T_F0011](../tasks/Yin_T_F0011_v1.md#contract), following the coordinating agent's request to examine normal encodings of the two-point modulus counterexample.
The [development entry](../drafts/Yin_D_F0006.md#two-point-modulus-matrix-encoding) records the remaining construction question.
A proper star subalgebra generating the same von Neumann algebra need not contain the group unitaries and matrix units in its actual derivation domains.
Adding further independent generators to the represented algebra can change the available derivation parameters.
The comparison and the perturbation exclusions therefore do not settle the existence of a separating normal law.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:13 |
| status | open |
| reason | The rank obstruction and the normal moment-limit consequences are fixed for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized algebraic derivations on the matrix-amplified group ring, excluded normal encodings, and divergence of the maximum vacuum norm under moment perturbations. |
| argument | [Argument](#argument) | Finite matrix-unit inner correction, order-two support projection, rectangular rank inequality, zero-modulus endpoint, and compactness at a common cutoff. |
| dependency | [Represented two-point modulus algebra](Yin_C_F0225_v1.md#the-represented-coordinates-and-their-derivation) | Positive modulus, recovery of the group ring from the star-polynomial core and identification of the unamplified encoding. |
| dependency | [Closable normal coordinates](Yin_C_F0076_v1.md#statement) | Item 1, closability of the normalized actual ACSY derivation at the distinguished selfadjoint coordinate. |
| dependency | [Two kernel projections](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the derivative between the left and right kernels for the singular zero-modulus endpoint. |
| dependency | [Closure of normal laws at fixed vacuum bounds](Yin_C_F0201_v2.md#statement) | Inheritance of normal actual ACSY at every cluster law under a common cutoff and uniform coordinatewise vacuum bounds. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:28 |
| status | proved |
| reason | Independent review verifies the amplified rank obstruction, both normal encodings through zero modulus and divergence of the vacuum norms along moving moment targets. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized algebraic derivations on the matrix-amplified group ring, excluded normal encodings, and divergence of the maximum vacuum norm under moment perturbations. |
| argument | [Argument](#argument) | Finite matrix-unit inner correction, order-two support projection, rectangular rank inequality, zero-modulus endpoint, and compactness at a common cutoff. |
| dependency | [Represented two-point modulus algebra](Yin_C_F0225_v1.md#the-represented-coordinates-and-their-derivation) | Positive modulus, recovery of the group ring from the star-polynomial core and identification of the unamplified encoding. |
| dependency | [Closable normal coordinates](Yin_C_F0076_v1.md#statement) | Item 1, closability of the normalized actual ACSY derivation at the distinguished selfadjoint coordinate. |
| dependency | [Two kernel projections](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the derivative between the left and right kernels for the singular zero-modulus endpoint. |
| dependency | [Closure of normal laws at fixed vacuum bounds](Yin_C_F0201_v2.md#statement) | Inheritance of normal actual ACSY at every cluster law under a common cutoff and uniform coordinatewise vacuum bounds. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0241_v1.md#whole-proof-finding) | The whole coarse rank and moment-limit argument and the contextual comparison with the known dimension formulas. |
