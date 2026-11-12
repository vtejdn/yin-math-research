---
author: Yin
---
# Independent review of rectangular finite-witness normalization

## Inputs and arrangement

The reviewed candidate is the complete [statement](../../claims/Yin_C_A0007_v4.md#statement) and [argument](../../claims/Yin_C_A0007_v4.md#argument) of C_A0007 v4 as read on 2026-11-11T18:31 UTC.
The reviewer was a separately assigned agent outside the candidate's substantive proof development, with no inherited proof-generation dialogue, author explanations, development drafts or previous review conclusions.
The assignment supplied the exact fixed candidate, review scope, rules and operational metadata only.
The reviewer read the candidate directly and reconstructed its obligations before consulting its necessary fixed mathematical inputs.
No earlier R finding was consulted or used as proof evidence.
This is an independent whole-candidate proof review, with the changed interfaces to [C_A0007 v3](../../claims/Yin_C_A0007_v3.md#statement) checked at their actual scope.

The retained affiliated foundations are the [domain-aware rank argument](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) and its [MSY23 source unit](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof).
The analytic input is the [BBL21 general-base source interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface).
The reviewer additionally inspected Theorems 3.2 and 3.5, the norm-limit construction and equation (3.7) in the matching [arXiv v2 primary text](https://arxiv.org/html/1903.09002v2).
The [identity-stabilization obstruction](../../ledger/Yin_L_A0026_v1.md#the-local-dimension-contradiction) and the [noncentral support-cut example](../../ledger/Yin_L_A0023_v1.md#smith-support-and-the-exact-compression-correction) were read directly for the candidate's comparison and limitations.
These are proof and source inputs, not inherited review conclusions.

## Whole-candidate finding

The complete conditional statement and argument are supported.
No mathematical gap was found in the rectangular normalization, exact size correction, actual finite boundary recovery, vertex-nullity consequence or stated examples and limitations.
The review covers all of equations (1)--(17), including the noncommutative order, matrix sizes and the actual affiliated interpretation of the rank comparison.
It does not infer finite witnesses from a nonzero analytic kernel or establish a group-wide Atiyah permanence theorem.

### Coefficient order, sizes and actual rank

For distinct cosets \(Hu_\alpha\), the condition \(u_\alpha u_\beta^{-1}\notin H\) is exactly the condition needed by the left-coefficient expansion.
In each summand of \(WW^*\), bimodularity places \(F_\alpha\) on the left and \(F_\beta^*\) on the right of the expected group word.
This verifies \(C=\sum_\alpha F_\alpha F_\alpha^*=DD^*\) without commuting a coefficient past a group element or assuming normality of \(H\).
The sizes are \(D:n\times N\), \(W_0:N\times k\), \(R:N\times n\), and \(Y'_j,X_0,Q_j:N\times N\), with \(N=sk\).
Thus both \(DW_0=W\) and \(Y'_j=D^*Y_jD\) are correctly typed finite group-ring identities.
The edge entries of \(D\) preserve each vertex ring and selfadjointness under this operation.

Full support makes the positive \(n\)-square operator \(C\) injective.
Its spectral inverse is a densely defined operator affiliated with the actual edge von Neumann algebra.
The decomposition of the subgroup regular representation into copies on cosets preserves that inverse, kernel projections and their traces in the ambient group algebra.
Consequently \(R=D^*C^{-1}\) is an actual affiliated right inverse, with \(DR=I_n\), before any rank of \(Y\) is used.
This forces \(\operatorname{rk}D=n\) and \(N\ge n\).

For composable rectangular affiliated matrices, the closure of the product range is contained in the closure of the left factor's range, and the right factor's kernel is contained in the product kernel.
Polar decomposition identifies initial and final support traces, so these inclusions give rank monotonicity with the appropriate domain and codomain sizes.
Applying it to \(Y'=D^*YD\) and to \(Y=R^*Y'R\) proves equality of the two ranks.
Subtracting from their respective sizes gives \(\nu(Y')=\nu(Y)+N-n\).
This verifies the full correction, including when the inverse is unbounded, without applying \(R\) to every original Hilbert-space kernel vector.

### Expected kernel, analytic input and finite boundary recovery

The off-diagonal \(k\)-square blocks of \(W_0W_0^*\) have zero expectation, while every diagonal block is \(I_k\).
Also \(W_0^*W_0=sI_k\), so \(\|W_0\|^2=s\).
The identity \(Y'W_0=0\) therefore gives \(0\le X_0\le s p'\) and \(E_H^{(N)}(p')\ge s^{-1}I_N\).
This is the required bounded inverse for the new expected kernel; no lower bound for the original expected Gram or original expected kernel is used.

Reduced alternating group words verify freeness of the vertex group rings over the edge ring.
Bounded strong approximation and normality of the expectation extend this to the von Neumann algebras, and the entrywise centered-product expansion gives the matrix amplification over \(M_N(\mathcal N(H))\).
The bounded selfadjoint matrices \(Y'_j\), normalized matrix trace and the displayed strict lower bound satisfy the general-base hypotheses of BBL21 Theorem 3.5.
Its part (vii) supplies the meet identity \(p'=P_{\ker Q_1}\wedge P_{\ker Q_2}\) and the trace formula.
The boundary construction in Theorem 3.2 identifies the \(b'_j\) as the actual norm limits, with sum zero.
The source's analytic existence and limit foundations are accepted external inputs whose full original proofs were not re-audited.

Multiplying the normalized trace identity by \(N\) gives \(\nu(Q_1)+\nu(Q_2)=N+\nu(Y')\), with no extra doubling factor.
Since \(p'X_0=X_0\), the kernel inclusions give \(Y'_jX_0=b'_jX_0\).
Left bimodularity and \(E_H^{(N)}(X_0)=I_N\) then identify the actual limit as \(b'_j=E_H^{(N)}(Y'_jX_0)\), in that order.
Finite coefficient extraction puts this matrix in \(M_N(\mathbb CH)\); its boundedness and selfadjointness come from the same actual boundary value, without an additional rationality assumption.
Substitution of the size correction gives \(\nu(Y)=\nu(Q_1)+\nu(Q_2)-2N+n\), and subtracting from the sizes gives \(\operatorname{rk}(Y)=\operatorname{rk}(Q_1)+\operatorname{rk}(Q_2)\).
Integer nullities of those two finite vertex matrices suffice, and subgroup trace preservation justifies using their vertex regular representations.
The conditional use of known torsion-free vertex Atiyah properties adds no division-closure requirement.

### Earlier interfaces, exact examples and limits

The new proof replaces v3's square principal-ideal factor with the rectangular coset coefficient matrix and replaces its constructed identity-expectation matrix by \(W_0W_0^*\).
The finite-boundary deduction survives because it requires exactly the same kernel inclusion and identity expectation.
The rank comparison changes from equal square sizes to the explicit \(N-n\) correction, which was independently checked above.
No principal-ideal, commutativity or torsion assumption enters the new construction.

In the two-variable calibration, the expected Gram has torus symbol \(|x-1|^2+|y-1|^2\), whose zero set has measure zero but admits no positive uniform lower bound.
The matrices \(D=(x-1\ \ y-1)\) and \(W_0=(1\ \ s)^{\mathsf T}\) give the stated factorization and identity expectation, and the affiliated rank of \(D\) is one.
Thus its extra kernel dimension is exactly one.
The nonzero abelian Laurent polynomial \(W\) is injective by its almost-everywhere nonzero torus symbol; hence a compatible scalar \(Y\) annihilating it is zero.
The candidate correctly treats this as a normalization calibration.
The earlier scalar common-divisor argument and the identity-padded local-module argument exclude square polynomial normalizations only: locally, \(\mathfrak m\oplus S^\ell\) has residue dimension \(\ell+2\), whereas a free rank-\(\ell+1\) module has residue dimension \(\ell+1\).
The rectangular map is not the square polynomial module isomorphism those arguments exclude.

For the deficient-support comparison, the sheared witness \((1,0,a,b)^{\mathsf T}\) has coefficient matrix \(D=(e_1\ e_3\ e_4)\), of rank three rather than four.
The displayed four-square matrix in L_A0023 has its only nonzero couplings through the second coordinate and therefore compresses to zero on those three coordinates.
Its associated row \((-s\ \ a-1\ \ b-1)\), with \(s=(a-1)a+(b-1)b\), has dense range because its adjoint kernel is contained in that of \(a^{-1}-1\).
The latter kernel is zero on infinite \(\langle a\rangle\)-orbits.
The four-square matrix thus has rank two and nullity two, while its three-square compression has rank zero and nullity three, exactly as stated.
This checks the failure of the claimed rank equality when full support is absent, without borrowing an unknown rank to certify a correction.

The remaining witness-existence and deficient-support restrictions are substantive and correctly retained.
The earlier cyclic normalization and four-path calibration remain their own fixed arguments; this finding does not relabel their earlier reviews or make a historical novelty claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [Statement](../../claims/Yin_C_A0007_v4.md#statement) | Complete rectangular finite-witness theorem, exact dimension and rank formulas, actual finite boundary values, vertex-nullity implication and all stated hypotheses and limitations. |
| [Whole-candidate finding](#whole-candidate-finding) | [Argument](../../claims/Yin_C_A0007_v4.md#argument) | Entire argument, equations (1)--(17), noncommutative order and sizes, actual affiliated rank/domain reasoning, general-base subordination applicability, changed v3 interfaces and both obstruction comparisons, with the stated accepted analytic foundations. |
