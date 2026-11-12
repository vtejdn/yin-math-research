---
author: Yin
---
# Rectangular finite-witness normalization over arbitrary amalgamated edges

This argument strengthens the finite-witness mechanism of [C_A0007 v3](../claims/Yin_C_A0007_v3.md) by allowing an explicitly controlled enlargement.
The cyclic principal-ideal normalization remains a smaller-size alternative at its stated scope.
The new construction uses all coset coefficients as a rectangular matrix and needs no principal-ideal, commutativity, torsion or coefficient-division hypothesis on the edge group.
Its indispensable input is still a displayed finite kernel witness with full-support expected Gram.
It does not assert existence of that witness for arbitrary analytic kernels.

## Statement

Let \(G=G_1*_H G_2\) be an actual amalgamated product, with arbitrary discrete groups and the specified injective subgroup embeddings.
Let \(E_H:\mathcal N(G)\to\mathcal N(H)\) be the canonical coefficient-extracting conditional expectation, amplified entrywise as needed.
All matrix traces and kernel dimensions are unnormalized.
For a bounded matrix \(Z\), write \(\nu(Z)\) for the trace of its actual Hilbert-space kernel projection in its domain size, and \(\operatorname{rk}(Z)\) for its affiliated rank.

Let \(Y_j=Y_j^*\in M_n(\mathbb CG_j)\), \(Y=Y_1+Y_2\), and suppose that
\[
 W\in M_{n,k}(\mathbb CG),\qquad YW=0,\qquad
 C:=E_H^{(n)}(WW^*)\text{ has support }I_n,
 \qquad k\ge1.
 \tag{1}
\]
Choose the distinct cosets \(Hu_1,\ldots,Hu_s\) meeting the finite support of \(W\), and write
\[
 W=\sum_{\alpha=1}^s F_\alpha u_\alpha,
 \qquad F_\alpha\in M_{n,k}(\mathbb CH),
 \qquad N:=sk.
 \tag{2}
\]
Define the explicitly finite matrices
\[
 D=(F_1\ \cdots\ F_s)\in M_{n,N}(\mathbb CH),
 \qquad
 W_0=\begin{pmatrix}u_1I_k\\\vdots\\u_sI_k\end{pmatrix}
 \in M_{N,k}(\mathbb CG),
 \tag{3}
\]
\[
 Y'_j=D^*Y_jD,\qquad Y'=Y'_1+Y'_2,\qquad X_0=W_0W_0^*.
 \tag{4}
\]
Then \(N\ge n\), all these are matrices over the asserted finite group rings, and
\[
 W=DW_0,\qquad Y'W_0=0,\qquad
 E_H^{(N)}(W_0W_0^*)=E_H^{(N)}(X_0)=I_N,
 \tag{5}
\]
\[
 E_H^{(N)}(P_{\ker Y'})\ge s^{-1}I_N,
 \qquad
 \boxed{\nu(Y')=\nu(Y)+N-n.}
 \tag{6}
\]
The actual operator-valued subordination boundary values for the new finite sum exist at zero and satisfy
\[
 b'_j=E_H^{(N)}(Y'_jX_0)\in M_N(\mathbb CH),
 \qquad Q_j:=Y'_j-b'_j\in M_N(\mathbb CG_j).
 \tag{7}
\]
In particular they are finite edge coefficients, rather than only bounded measurable or rational coefficients.
Their exact kernel formula is
\[
 \boxed{\nu(Y)=\nu(Q_1)+\nu(Q_2)-2N+n,}
 \qquad
 \boxed{\operatorname{rk}(Y)=\operatorname{rk}(Q_1)+\operatorname{rk}(Q_2).}
 \tag{8}
\]
It suffices that the two specific \(Q_j\) have independently certified integer nullities to conclude \(\nu(Y)\in\mathbb Z\).
Known complex Atiyah properties of the two torsion-free vertex groups are a sufficient special case.
Their subgroup regular representations preserve the indicated ranks in \(G\); no full division-closure premise is required for this conclusion.

## Argument

### Exact coefficient expectation and an independent rectangular inverse

Coefficients in (2) are on the left.
For distinct cosets \(Hu_\alpha,Hu_\beta\), one has \(u_\alpha u_\beta^{-1}\notin H\).
Bimodularity of the actual conditional expectation gives
\[
 C=\sum_\alpha F_\alpha F_\alpha^*=DD^*.
 \tag{9}
\]
No normality of \(H\) in either vertex or in \(G\) is used.
The full-support assumption in (1) independently makes \(C\) an injective positive operator in \(M_n(\mathcal N(H))\).
Finite-trace polar decomposition gives its actual affiliated inverse \(C^{-1}\).
The subgroup regular-representation decomposition embeds that inverse in the actual affiliated algebra of \(G\), preserving its kernel and trace.
The bounded inverse of \(C\), and membership of that inverse in a coefficient division ring, are not asserted or needed.

The rectangular affiliated matrix
\[
 R:=D^*C^{-1}\in M_{N,n}(\mathcal U(H))
 \tag{10}
\]
satisfies \(DR=I_n\) in the actual affiliated algebra.
Thus \(D\) has rank \(n\), which implies \(N\ge n\).
This certification precedes any use of the unknown rank of \(Y\).
All subsequent unbounded products are closed affiliated products.

### Complete nullity correction for the enlargement

From \(Y'=D^*YD\), rank cannot increase through multiplication, so \(\operatorname{rk}(Y')\le\operatorname{rk}(Y)\).
Conversely (10) gives the affiliated identity
\[
 R^*Y'R=(DR)^*Y(DR)=Y,
 \tag{11}
\]
and hence \(\operatorname{rk}(Y)\le\operatorname{rk}(Y')\).
Both inequalities use the standard rectangular rank monotonicity from polar decomposition, or the domain-correct affiliated rank inequalities retained in [L_A0006](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement).
Therefore the ranks are equal and their different square sizes give precisely (6).
The correction is the known integer \(N-n\), with neither an unknown extra compression kernel nor a factor of two.
The identity does not assert that the possibly unbounded \(R\) acts on every original Hilbert-space kernel vector.
It is a rank identity between the original bounded matrices, justified inside their actual affiliated algebra.

Each entry of \(D\) and \(D^*\) is in the edge group ring, so every \(Y'_j\) remains a finite selfadjoint matrix in its original vertex ring.
No product between different vertex rings is introduced into \(Y'_j\).
The kernel equation follows directly from bounded finite identities:
\[
 Y'W_0=D^*YW=0.
 \tag{12}
\]

### Uniform expected kernel and actual finite boundary values

The \((\alpha,\beta)\) block of \(W_0W_0^*\) is \(u_\alpha u_\beta^{-1}I_k\).
Expectation therefore deletes every off-diagonal block and retains each diagonal identity, proving (5).
Also
\[
 W_0^*W_0=sI_k,\qquad \|W_0\|^2=s.
 \tag{13}
\]
Writing \(p'=P_{\ker Y'}\), equation (12) gives \(p'W_0=W_0\), so
\[
 0\le W_0W_0^*\le s p'.
\]
Expectation preserves this order and proves the uniform lower bound in (6).
This is an actual bounded inverse for the new expected kernel, obtained without assuming one for the original expected kernel or for \(C\).

The vertex von Neumann algebras are free over \(\mathcal N(H)\) under coefficient expectation: expanding centered finite group-ring elements yields reduced alternating words outside \(H\).
The same argument applies to centered matrix products entry by entry, giving freeness over \(M_N(\mathcal N(H))\).
The accepted [BBL21 general-base boundary theorem](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), together with the precise kernel-inclusion interface retained in [C_A0007 v3](../claims/Yin_C_A0007_v3.md#statement), now applies to \(Y'_1+Y'_2\).
It supplies the actual bounded selfadjoint boundary values \(b'_j\), their sum zero, the inclusions \(p'\le P_{\ker(Y'_j-b'_j)}\), and
\[
 \nu(Q_1)+\nu(Q_2)=N+\nu(Y').
 \tag{14}
\]
The source's analytic existence and limit theorem is accepted at its inspected scope; the algebraic calculation does not replace that theorem with a merely compatible candidate boundary.

Since \(p'X_0=X_0\), those kernel inclusions imply the bounded equations
\[
 (Y'_j-b'_j)X_0=0.
\]
Taking expectation in the displayed order and using \(E_H^{(N)}(X_0)=I_N\) gives
\[
 E_H^{(N)}(Y'_jX_0)=b'_j E_H^{(N)}(X_0)=b'_j.
 \tag{15}
\]
The product on the left is finite over \(\mathbb CG\), and coefficient extraction has finite output in \(\mathbb CH\).
This proves (7), without any assertion about the rationality of \(p'\) or of its conditional expectation.
Combining (14) with the exact correction (6) gives both identities in (8).

### Why the two-variable local obstruction does not apply

In the retained two-variable test, let \(H=\mathbb Z^2=\langle x,y\rangle\), let \(s\) be an independent infinite cyclic generator, and take
\[
 W=(x-1)+(y-1)s.
 \tag{16}
\]
Its expected Gram has full support but no bounded inverse.
The [same-size scalar obstruction](../claims/Yin_C_A0007_v3.md#why-the-same-polynomial-repair-fails-for-a-two-variable-edge) and the [identity-stabilization obstruction](../ledger/Yin_L_A0026_v1.md) remain correct.
They require a square polynomial factor of the original or identity-padded size and consequently would force the nonfree local coefficient module to be free.

Here the factors are instead
\[
 D=(x-1\ \ y-1),\qquad W_0=(1\ \ s)^{\mathsf T},
 \qquad E_H(W_0W_0^*)=I_2.
 \tag{17}
\]
The matrix \(D\) has an actual affiliated right inverse by (9)--(10), but it is not a square polynomial isomorphism of the coefficient module.
Its extra kernel has dimension one and is retained in \(\nu(D^*YD)=\nu(Y)+1\) for every compatible bounded scalar \(Y\).
For the concrete abelian example a compatible finite scalar \(Y\) is zero, since \(W\) is an independently injective nonzero abelian Laurent polynomial.
Thus this calibration illustrates the normalization and its exact scope, not a new nonzero scalar-kernel example.
The rectangular construction changes the finite coefficient module and pays an explicit integer kernel correction, which is precisely the operation excluded from the earlier impossibility statements.

### The remaining full-support obstruction

If the expected Gram in (1) is deficient, \(D\) has rank less than \(n\), and (10) no longer gives a right inverse.
Neither equality of ranks in (11) nor the stated size correction then follows.
The earlier [noncentral support-cut example](../ledger/Yin_L_A0023_v1.md#smith-support-and-the-exact-compression-correction) makes the limitation concrete.
After its cyclic shear, its witness is \((1,0,a,b)^{\mathsf T}\); the three distinct coset coefficients give \(D=(e_1\ e_3\ e_4)\).
The original four-square matrix has rank two and nullity two, whereas \(D^*\widehat YD=0_3\) has rank zero and nullity three.
In that example the discarded boundary row independently certifies the correction, but full-support normalization alone does not do so.

The enlarged theorem therefore repairs full-support witnesses over arbitrary edges while leaving deficient expected support and absence of finite polynomial kernel columns unresolved.
It does not turn a torsion-free hypothesis into the finite-witness condition.
It does not establish a new group-wide Atiyah permanence theorem or claim historical novelty.
The original cyclic same-size normalization, explicit four-path calibration and their reviews remain available in the earlier physical versions with their actual scopes.
The new ingredients are the rectangular coset synthesis, its independently certified rank equality, and the resulting general-edge finite boundary formula.

## Assessment history

### Decision reviewed-rectangular-boundaries

| Field | Value |
| --- | --- |
| date | 2026-11-11T18:34 |
| status | proved |
| reason | Independent whole-candidate review supports rectangular finite-witness normalization over arbitrary amalgamated edges, its exact integer size correction and actual finite boundary recovery, while retaining the full-support witness premise. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General-edge rectangular construction, exact nullity and rank identities, actual finite vertex matrices and conditional integer-nullity consequence. |
| argument | [Argument](#argument) | All ordered coefficient identities, actual rectangular inverses and domains, general-base subordination input, examples and precise remaining obstruction. |
| review | [Independent whole-candidate finding](../audits/reviews/Yin_R_A0020_v4.md#whole-candidate-finding) | Whole fixed statement and argument, exact source and previous-version interfaces, all dimensions and retained limitations. |

## Current assessment

[Selected decision](#decision-reviewed-rectangular-boundaries)

