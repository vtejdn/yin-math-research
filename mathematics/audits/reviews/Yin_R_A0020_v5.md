---
author: Yin
---
# Independent review of expected-support compression defects

## Inputs and arrangement

The reviewed artifact is the complete [statement](../../claims/Yin_C_A0007_v5.md#statement) and [argument](../../claims/Yin_C_A0007_v5.md#argument) of C_A0007 v5, reviewed on 2026-11-11T19:54 UTC.
The reviewer was a separately assigned agent outside substantive development of this artifact, with no inherited proof-generation dialogue, author explanations, development summaries or draft reasoning.
The assignment supplied the fixed artifact, exact whole-artifact scope, applicable rules and operational metadata.
The reviewer read the candidate directly, reconstructed its obligations, and checked the necessary fixed mathematical inputs.
The earlier [R_A0014 boundary finding](Yin_R_A0014_v1.md#nonrationality-and-boundary-values) was consulted for the declared source interface after the candidate obligations had been reconstructed.
[R_A0020 v4](Yin_R_A0020_v4.md#whole-candidate-finding) was read only after the initial v5 findings had been formed, for comparison with the unchanged normalization interface.
Neither earlier review is treated as reviewing v5.

The directly inspected inputs are the [rectangular normalization argument](../../claims/Yin_C_A0007_v4.md#argument), the [precise v3 analytic interface](../../claims/Yin_C_A0007_v3.md#statement), the [free-boundary matrix](../../ledger/Yin_L_A0023_v1.md#an-additive-noncentral-boundary-matrix), and the [twelve-coordinate compression calibration](../../ledger/Yin_L_A0023_v3.md#a-single-support-compression-and-its-exact-correction).
For the last calibration, the [eight-coordinate input](../../ledger/Yin_L_A0023_v2.md#an-explicit-additive-eight-square-matrix), its explicit auxiliary inverse and complete kernel were also read.
The affiliated-rank input is the [L_A0006 domain convention](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement), with the actual range-closure and kernel arguments in [MSY23-U004](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof).
The [original Task contract and subgroup argument](../../tasks/Yin_T_A0001_v1.md#contract) determine the quantifiers and trace normalization being tested.

The source interface is the [BBL21 general-base unit](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface).
The reviewer checked Theorems 3.2 and 3.5, their boundary-value construction and the kernel-intersection conclusion against the matching [arXiv v2 primary text](https://arxiv.org/html/1903.09002v2).
The analytic foundations are accepted at those hypotheses; their original proofs were not re-audited.
For known coverage, the reviewer checked the relevant [known-results entries](../../ledger/Yin_L_A0001_v1.md#known-positive-results), the [Lin93 free-group input](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems), and the statement of [SP25 Theorem 1.1, arXiv v2](https://arxiv.org/html/2409.12268v2#S1).
Those coverage results are comparison inputs, not premises of the arbitrary-input encoding.

## Whole-artifact finding

The complete stated result is supported.
No mathematical gap was found in equations (1)--(21), the exact dependency interfaces, the stated counterexample to witness-support inclusion, the arbitrary-input encoding, the unit-pivot class, or the complete-chain limitations.
This is an independent whole-artifact proof review with accepted affiliated-operator and analytic subordination foundations.
It establishes neither the original Atiyah Task nor a new permanence theorem for amalgams with independently controlled vertex groups.

### Compression kernels and both corrections

The compression kernel is taken inside \(q\mathcal H\), so its projection \(e\) excludes the automatic ambient kernel on \((1-q)\mathcal H\).
For \(x\in e\mathcal H\), the bounded equation \(qYx=0\) gives \(Yx=(1-q)Yx\).
Therefore the kernel of \(B_q\) restricted to \(e\mathcal H\) is exactly \((p\wedge q)\mathcal H\).
Polar decomposition of this bounded restricted map gives
\[
 \operatorname{rk}(B_qe)=\operatorname{tr}(e)-\operatorname{tr}(p\wedge q).
\]
Subtracting \(\operatorname{tr}(p)\) verifies (3), including the sign of the missing original-kernel term.
When \(p\le q\), that term vanishes, and the range support of \(B_qe\) lies below \(1-q\), proving (4) and its upper bound.
Subtracting the corner rank \(\operatorname{tr}(q)-\operatorname{tr}(e)\) from the full rank \(n-\operatorname{tr}(p)\) gives exactly (5).
The ambient rank loss thus includes the discarded corner dimension in addition to the nullity change.

All maps used in this argument are bounded and defined on their indicated whole Hilbert spaces.
The proof does not transport Hilbert-space kernels through an unbounded inverse.
The same calculation works for a bounded nonselfadjoint square operator, as stated; selfadjointness remains available for the subsequent subordination application.

The twelve-coordinate numerical comparison was checked at its actual input.
The eight-coordinate kernel equations force \(y_1=t_2=abf\), vanishing multiplier coordinates and the remaining free-boundary kernel of dimension one.
Four independent zero coordinates and the displayed unitary rotations therefore give nullity six and rank six.
The constant terminal projection has trace eleven and contains the whole transported kernel.
After compression, the two constraint rows have the explicitly invertible triangular two-column submatrix in L_A0023 v3, so the selfadjoint off-diagonal block has rank four.
The corner nullity is seven, giving nullity correction one and ambient rank loss two, in agreement with (5).
This is the calibration interface used by v5, not an independent review of every unused rotation obstruction in that ledger.

### Expected support and the incomplete-witness counterexample

For \(K\ge0\), the vanishing of \(E((1-q)K(1-q))\), where \(q=s(E(K))\), implies \((1-q)K(1-q)=0\) by faithfulness.
Factoring through \(K^{1/2}\) proves \(s(K)\le q\).
Conversely, any base projection containing \(s(K)\) also contains \(s(E(K))\) by bimodularity.
This proves the claimed minimality and, in particular, \(p\le s(E(p))\).

For a kernel witness, \(WW^*\le\|W\|^2p\) proves \(q_W\le q_p\), while minimality gives \(s_W\le q_W\).
These implications do not reverse.
If \(s_W=p\), both expected supports are the smallest base projection containing the same projection; this verifies the stated sufficient case without assuming closed range for \(W\).

The free-boundary input really has analytic nullity one and zero polynomial kernel.
Its row \((a-1\ \ b-1)\) has dense range because its adjoint kernel is contained in the invariant vectors for the infinite cyclic subgroup generated by \(a\).
Its finitely supported kernel is zero by the tree leaf-removal argument on each right coset of \(F(a,b)\).
Consequently \(Y=0_1\oplus T\) has complete polynomial kernel \(e_0\mathbb CG\), analytic nullity two and maximal polynomial expected support \(q=e_0e_0^*\).
The off-corner restriction is zero, but \(\operatorname{tr}(p)-\operatorname{tr}(p\wedge q)=1\).
Thus (3) gives the actual correction \(-1\).
This verifies the counterexample to the proposed support implication without asserting a nonintegral group-ring rank.

### Deficient rectangular normalization and its analytic interface

The coset coefficients remain on the left, so distinct \(Hu_\alpha\) give \(E_H(u_\alpha u_\beta^{-1})=0\).
Hence \(DD^*=E_H(WW^*)\), while the stacked \(W_0\) has identity expected Gram and \(W_0^*W_0=sI_k\), regardless of the rank of \(D\).
The sizes are \(D:n\times N\), \(W_0:N\times k\), \(R:N\times n\), and \(Y',Q_j:N\times N\).
Edge coefficients on both sides of each \(Y_j\) preserve its original vertex ring.
The equation \(Y'W_0=0\) therefore remains a finite bounded identity.

The input's analytic step does not require \(D\) to have full row rank.
Writing \(p'=P_{\ker Y'}\), the bounded inequality \(W_0W_0^*\le sp'\) gives \(E_H(p')\ge s^{-1}I_N\).
Reduced alternating words give amalgamated freeness, and the entrywise centered-product expansion gives its matrix amplification.
Thus the general von Neumann base, bounded selfadjoint summands, trace and bounded-inverse hypotheses of BBL21 all hold.
The theorem supplies actual boundary values, kernel inclusions and the unnormalized identity
\[
 \nu(Q_1)+\nu(Q_2)=N+\nu(Y').
\]
Taking expectation of \(Y'_jW_0W_0^*=b'_jW_0W_0^*\) identifies the actual \(b'_j\) with the finite coefficient expectation.
Subtracting nullities from their sizes proves (8).
No candidate boundary or full-support-only diffuse-base argument replaces the analytic theorem.

On the support corner \(q\), the positive operator \(DD^*\) is injective and has its actual spectral affiliated inverse.
Extended by zero, it yields \(DR=q\); this is not an inverse on the complementary corner.
Subgroup representation preserves the support and this spectral inverse.
The identities \(Y'=D^*(qYq)D\) and \(R^*Y'R=qYq\) hold in the actual affiliated algebra with closed products.
Rectangular rank monotonicity follows from the range-closure and kernel arguments with the appropriate domain and codomain traces, or by zero padding those arguments.
It gives equality of the bounded endpoint ranks and then (9).

Combining this equality with the previously checked compression formula proves every size term and sign in (10)--(11).
Without \(p\le q\), the replacement prescribed after (11) is exactly (3).
An edge Atiyah hypothesis controls \(\operatorname{tr}(q)=\operatorname{rk}_H D\), but supplies no integer trace for the possibly nonpolynomial \(B_qe\).
That limitation is substantive and correctly retained.

### Exact encoding of every rectangular Task input

Free-product normal form verifies the displayed embeddings, the identification \(G=\Gamma*F(z,a,b)\), noncentrality of \(H\), and torsion-freeness of the groups when \(\Gamma\) is torsion-free.
No integrality assertion enters those facts.
The right-coset decomposition preserves the kernel projections and their trace for \(A\), including when the original group is not finitely generated.

The order in \(T=A(I_n\ \ -aI_n)\) is essential and is correct.
It gives \(T(aI_n,I_n)^{\mathsf T}=Aa-Aa=0\), with no commutation of \(a\) past an entry of \(A\).
The displayed block decomposition is finite, additive and selfadjoint.
When \(A\ne0\), the free letter \(a\) makes an actual first-vertex nonedge coefficient, and \(D_b\) supplies second-vertex nonedge coefficients.
For \(A=0\), the same formulas remain valid; the claim of both nonedge contributions is explicitly conditional.

The lower bound \(D_b\ge I_m\) is independently established from the norm of \(b+b^{-1}\).
Pairing \(Tx+D_by=0\) with \(y\), after using \(T^*y=0\), proves \(y=0\).
This proves the whole kernel identity, not merely inclusion of the displayed witness.
The witness has expected Gram \(q\) and squared norm two, so
\[
 q/2\le E_H(p)\le q.
\]
Thus the actual expected-kernel support equals the witness support and is maximal among all finite kernel witnesses.
Completeness of the displayed polynomial columns is unnecessary.

The bounded identities \(T=AR_a\) and \(TJ=A\) prove \(\operatorname{rk}T=\operatorname{rk}_\Gamma A\) in both directions.
The domain of \(T\) has size \(2n\), whereas \(Y\) has size \(2n+m\).
Consequently
\[
 \nu(Y)=2n-\operatorname{rk}_\Gamma A,\qquad
 \operatorname{rk}(Y)=m+\operatorname{rk}_\Gamma A,\qquad
 \delta_q(Y)=\operatorname{rk}_\Gamma A.
\]
The zero corner has nullity \(2n\).
Both compressed summands vanish, so the coset normalization also gives \(Y'_1=Y'_2=0\), with zero actual boundaries and zero \(Q_j\).
This checks the full content of (18), including all rectangular size corrections and the zero-input case.

Integrality of the defects in this family for all \((\Gamma,A)\) is equivalent to the exact Task contract because \(\operatorname{rk}_\Gamma A=n-\nu_\Gamma(A)\).
This is an equivalence of assertions, not evidence of a nonintegral example.
Assuming the whole first vertex satisfies Atiyah already resolves the embedded \(\Gamma\) input by subgroup restriction.
The encoding therefore leaves open a theorem with independently established vertex hypotheses and correctly does not purport to disprove one.

### The two-vertex unit-pivot family and the continuation boundary

In (19), the first block of \(T\) gives a bounded finite right inverse before any use of a group-wide rank theorem.
Thus \(\operatorname{rk}T=r\), and the positive bottom block gives \(\ker Y=\ker T\oplus0\).
The sizes \(3r\) and \(4r\) yield nullity \(2r\), ambient rank \(2r\) and defect \(r\).

Multiplication checks the two block columns of the witness in (20).
For each \(j\), expectation removes the cross terms of \((K_j+u_jI_r)(K_j+u_jI_r)^*\) because \(u_j\notin H\).
It leaves \(K_jK_j^*+I_r\), with no normality or centrality premise on \(H\).
Multiplying the triangular factors in (21) reproduces all off-diagonal signs and the full upper-left block.
The displayed finite inverse of \(L\) gives a positive uniform lower bound on the corner.
Together with the complete kernel inclusion this proves equality of the two expected supports.
The defect is independently certified, but its rank was already fixed by the unit pivot, exactly as the candidate says.

The full route from an arbitrary Task input reaches a valid finite additive matrix and valid full-support normalized problem.
Its first unproved integrality step is the defect itself, which (18) identifies with the original unknown rank.
For inputs in amalgams with independently controlled vertices, finite-witness existence, inclusion of the complete analytic kernel and integrality of the off-corner restriction remain separate requirements.
The tree example and its direct sum distinguish the first two failures.
No formula in the artifact discharges the third.

The free-group comparison is covered by the inspected Lin93 input.
SP25 Theorem 1.1 assumes a countable fundamental group, finite edges, vertex strong Atiyah over a conjugation-closed field and bounded finite-subgroup orders.
The candidate's qualification that the recorded free-product theorem must apply preserves those hypotheses; it does not apply that theorem directly to its infinite cyclic amalgam.
Known free-product coverage is a comparison when \(\Gamma\) is already controlled.
The arbitrary-input identity itself has no countability or known-group-class restriction.
Source identification is sufficient for these stated uses, with no priority claim or inspection of an unavailable journal edition.

The reviewed argument is mathematically complete at its actual scope.
Its retained unknown defect is the expressly identified limit of the proposed transfer method, not a gap in the proved equivalence or formulas.
This review uses direct symbolic and operator arguments; it claims no formal verification or numerical evidence for unrestricted integrality.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0007_v5.md#statement) | Complete statement, including both compression formulas, deficient normalization, every rectangular-input encoding, the unit-pivot family and all explicit scope limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0007_v5.md#argument) | Entire artifact and equations (1)--(21), with bounded and affiliated domains, support inclusions, exact subgroup and analytic interfaces, calibration corrections, known-coverage comparison and complete-chain limitations. |
