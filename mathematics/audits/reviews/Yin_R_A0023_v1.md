---
author: Yin
---
# Independent review of normal compressed transport and constant potentials

Review act: 2026-11-11T17:31 UTC.
Human record author: Yin.
The reviewed artifact is [C_A0008 v1](../../claims/Yin_C_A0008_v1.md), the complete dated 12 November 2026 candidate, including its statement, every argument and formula (1)--(23), comparisons, degeneracies and limiting discussion.
This is an initial whole-artifact mathematical review by an agent outside its substantive proof development.
The reviewer received the fixed candidate, required scope, actual Task authority and operational metadata, without proof-generation discussion, development drafts, proposing-agent mathematical summaries or previous review findings.
The reviewer derived the obligations from the candidate and then checked its fixed mathematical inputs and relevant source passages.
Necessary fixed inputs contain references to existing reviews, but those R findings were neither opened nor relied on.
The review does not select a Claim assessment or complete [T_A0001](../../tasks/Yin_T_A0001_v1.md#contract).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0008_v1.md#statement) | Entire stated normal-hopping and finite-matrix conclusions with their actual quantifiers and exclusions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0008_v1.md#argument) | All formulas (1)--(23), complete kernel projections, group and coefficient admissibility, domains, degeneracies, source comparisons and zero-potential limit. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite graph input](../../claims/Yin_C_A0003_v1.md#finite-graph-certificate) | Incidence convention, flat-tree specialization and trace-one frame; no use of arbitrary-border injectivity. |
| [Whole-artifact finding](#whole-artifact-finding) | [Tree argument](../../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators) | Complete tree kernel and equivariant isometric frame used by the finite star. |
| [Whole-artifact finding](#whole-artifact-finding) | [Projection-middle interface](../../claims/Yin_C_A0005_v1.md#projection-middle-and-finite-orbits) | Bounded kernel parametrization and dimension interface; its application is independently recomputed in C_A0008. |
| [Whole-artifact finding](#whole-artifact-finding) | [Compressed-transport interface](../../claims/Yin_C_A0005_v1.md#compressed-transport-certificate) | Identification of the overlap kernel and the separate zero-defect premise; no claim to re-audit the general affiliated proof. |
| [Whole-artifact finding](#whole-artifact-finding) | [Commuting-orbit statement](../../claims/Yin_C_A0005_v2.md#statement) | Hypothesis comparison only: pairwise commutation fails for the nontrivial present construction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Abelian rank-two statement](../../claims/Yin_C_A0005_v4.md#statement) | Hypothesis comparison only: its abelian coefficient field and rank-two frame do not apply to the present general rank-one construction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Character-orbit argument](../../ledger/Yin_L_A0007_v1.md#the-character-orbit-certificate) | Bounded homogeneous specialization and finite-eigenspace dimension reasoning needed for the free calibration. |
| [Whole-artifact finding](#whole-artifact-finding) | [Graded companion input](../../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) | Degree-one bounded case with constant coefficient 1 for the free-group trinomial; no reliance on a newly inspected general unbounded companion theorem. |
| [Whole-artifact finding](#whole-artifact-finding) | [Lin93 comparison](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) | Retained exact Theorem 1.3 hypotheses and free-by-cyclic coverage comparison, without a fresh audit of the original proof. |
| [Whole-artifact finding](#whole-artifact-finding) | [Route-four interface](../../strategies/Yin_S_A0004.md#mechanism-and-obstruction) | Scope comparison with actual rational-closure units; no identification of the differently signed trinomials or completion of the all-matrix contract. |

## Obligations and verification

The statement requires an exact corner kernel theorem, an admissible finite group-ring construction, an actual normal compression despite noncommuting translates, a complete spectral law and full finite-matrix kernels.
It also requires the claimed inverse certificates to precede their use, the parameter and coincidence cases to remain valid, and the source and zero-potential limitations to match the conclusions.
The following checks cover those obligations without assuming injectivity of the coefficient trinomial.

### Normal spectral averaging

For \(K=ptp|_p\), direct adjunction gives \(KK^*=p\sigma(p)p\) and \(K^*K=p\sigma^{-1}(p)p\).
For a vector in the \(p\)-corner, \(Kx=0\) is exactly \(tx\in(1-p)\ell^2(G)^d\), so its kernel is \(p\wedge\sigma^{-1}(1-p)\); the adjoint gives the other intersection.
Normality makes those kernels equal.
The height action fixes the corner and rotates \(K\), hence preserves the scalar spectral measure while rotating its argument.
For a nonzero complex number, each line equation \(2\operatorname{Re}(e^{i\theta}z)+\varepsilon=0\) has at most two angular solutions, including tangency.
For \(z=0\) it holds precisely when \(\varepsilon=0\).
Tonelli applies to the nonnegative Borel indicator and the finite trace measure, and trace faithfulness converts the resulting masses into the actual projection identities in (3).
The same argument covers the zero corner.
For nonzero potential the selfadjoint bounded residual has zero kernel and dense range, so its inverse is a densely defined affiliated corner operator.
There is no bounded-inverse claim and no use of that inverse on arbitrary Hilbert vectors.

### Group, star and independently certified inverses

The automorphism in (7) has the displayed inverse because it fixes every \(w_j\in H\).
The reduced-word torsion argument works for arbitrary torsion-free \(H\), including the trivial group, and the infinite cyclic quotient then proves torsion-freeness of \(G\).
Every row of \(A=(-d\ I_8)\) is exactly the leaf-to-root incidence convention of C_A0003.
The equations determine all eight leaves from the root, so no kernel component or cycle constraint is omitted.
The factor \(1/3\) makes \(V^*V=1\), and cyclicity of the matrix trace gives \((\operatorname{Tr}_9\otimes\tau_G)(VV^*)=1\).

Using \(d^*d=8\), multiplication gives \((I_8+dd^*)(I_8-dd^*/9)=I_8\) on both sides.
It follows that \(A^*JA=1-p\), and multiplication of \(B+p\) with \(X=p+A^*J^2A\) gives the two-sided identity and the remaining relations in (11).
All entries are finite group-ring sums, and all these inverses and graph maps are bounded.
Thus no Gram normalization depends on the unknown scalar kernel.

### Normality, noncommutation and product trace

Multiplying \(V^*\sigma(V)\) gives three identity terms and the six ordered \(w_j\), exactly \(c^*c/9\).
This calculation does not commute \(u\) with \(v\).
The resulting positive contraction \(C\) is fixed by \(\sigma\), and \(V^*KV=Ct\); consequently both products of this operator with its adjoint equal \(C^2\).
The actual scalar kernel is \(e=P_{\ker c}=P_{\ker C}\), and the isometry transports it to both overlap projections in (14).
Subgroup regular-representation decomposition preserves this kernel projection and its trace in \(G\).

If \(p\) commuted with \(\sigma(p)\), the compression \(C^2\) would be a projection and positivity would make \(C\) a projection.
Its nonnegative finite probability coefficients imply that its support would be a finite multiplicatively closed subset containing the identity, hence a finite subgroup.
That support contains both \(u,v\); torsion-freeness contradicts this when either is nonidentity.
Repeated or identity labels produce no cancellation and do not alter the argument.
A corresponding nonidentity \(w_j\) also gives distinct matrix entries \(z_jw_j^n/9\) along the orbit, proving infinitude.

The subgroup generated by \(H,t\) is \(H\times\mathbb Z\), since commutation and the semidirect normal form give injectivity of that product description.
Its regular trace is the tensor-product trace.
The joint bounded spectral calculus therefore proves (16), including its normalization to mass one in the trace-one corner.
For every \(r>0\) the pushforward of angular measure under \(\varepsilon+2r\cos\theta\) has no atoms, even at endpoints; the \(r=0\) fiber contributes exactly the mass at \(\varepsilon\).
This verifies (17) without a freeness assumption or an inverse of \(C\).

### Complete kernels and projections

The lower equation for (18) forces \(x\in p\ell^2(G)^9\), and the upper equation compressed by \(p\) is exactly \(R_\varepsilon x=0\).
For \(\varepsilon\ne0\), it follows that \(x=0\) and \(y\in p\ell^2(G)^9\), proving the first projection in (19), rank seventeen and normalized zero mass \(1/18\).
At zero potential, \(x\in\delta\), \(pTx=0\), and \(BX=q\) determines the entire \(q\)-part of \(y\) as \(-XTx\).
The remaining lower \(p\)-part is arbitrary, proving both directions of (20) and the bounded inverse parametrization.

For the graph operator \(F_\delta\), the positive corner operator \(D_\delta=F_\delta^*F_\delta\ge\delta\) has a bounded inverse on its corner.
The formula \(F_\delta D_\delta^{-1}F_\delta^*\) is its actual range projection.
Its range is orthogonal to the lower \(p\)-coordinate because \(pXT\delta=pT\delta=0\).
The two summands in (22) thus give the whole orthogonal kernel projection, with the zero-corner convention correctly included.
The graph is isomorphic to the \(\delta\)-module, so the trace is \(1+\tau_H(e)\), and division by eighteen gives the stated probability-normalized mass.
The congruence by \(\operatorname{diag}(I_9,X)\) also has off-diagonal block \(q\), but the proof uses its bounded invertibility for dimension preservation and never treats it as unitary.

### Degenerate parameters and limiting claim

The augmentation of \(c\) is three, hence \(c\ne0\); faithfulness gives \(0\le\tau_H(e)<1\), without supplying zero nullity.
When \(u=v=1\), \(C=1\) and \(e=0\), and the stationary orbit has the asserted dimension for every potential.
The cases \(2+w\) and \(1+2u\) have direct Neumann-series inverses after the stated dominant-term normalization.
The inverse-pair case is a nonzero Laurent polynomial in an infinite-order element, so its cyclic Fourier multiplier has a null zero set.
For commuting coefficient labels, their finitely generated torsion-free abelian subgroup gives the same Laurent-polynomial argument.

For \(H=F(u,v)\), the height assigning degree one to each generator makes \(u+v\) homogeneous.
Distinct eigenspaces of this bounded operator have injective bounded sum maps, by polynomial separation of their distinct eigenvalues.
Polar decomposition bounds the sum of their von Neumann dimensions by one.
Rotation invariance makes a nonzero eigenvalue orbit have constant dimension, which must therefore be zero.
This checks the degree-one specialization used to prove that \(1+u+v\) is an affiliated unit, independently of a whole-group Atiyah theorem.
The subgroup comparison transports the certificate, and \(N\cong F_8\) gives the stated free-by-cyclic calibration.

On the coefficient subspace \(e\), the nonzero-potential scalar is exactly \(\varepsilon e\), with inverse \(\varepsilon^{-1}e\).
Consequently the claimed nonzero-potential certificates give no uniform inverse control or injectivity conclusion at zero.
The moving atom description in (16) is exact and is consistent with a hypothetical nonzero \(e\).
No limiting interchange or hidden zero-potential unit is used.

## Source completeness and inspection limits

The finite-graph, projection-middle, commuting-orbit and rank-two comparisons were checked against the exact fixed inputs bound above.
The new construction derives its own finite matrices and bounded kernel identities, so those comparisons import neither an abelian field hypothesis nor an integer trace for the new overlap.
The character input was checked at the bounded degree-one scope actually needed here; this review does not claim a new audit of all unbounded arguments elsewhere in L_A0007.

The retained Lin93 source unit identifies Theorem 1.3 on printed page 562 and its free-normal-subgroup, torsion-free overgroup and elementary amenable quotient hypotheses.
They apply with the normal free subgroup \(F_8\) and quotient \(\mathbb Z\).
That is a known-coverage comparison only.
This review reused the source unit's exact statement and recorded source limits; it did not independently reread the original journal proof or its external foundations.

The reviewer read the introduction, Theorem 1.1 on page 2 and Proposition 3.1 on page 4 directly in [ASM19, arXiv:1905.00951v1](../../literature/pdf/ASM19--arxiv-v1.pdf).
The source distinguishes algebraic regularity from absence of an analytic kernel, and Proposition 3.1 proves the positive-square kernel interface by the sum of squared norms.
For three distinct labels, \(\|c\|_2^2=3\) and \(\|c\|_1^2=9\), so its stated sufficient condition fails as \(6<9\).
The candidate neither upgrades that algebraic theorem to an analytic theorem nor uses it as a premise.
No whole-paper proof audit, literature-wide search, priority conclusion or verification of the candidate author's earlier search process is asserted.
The bounded source comparison is supported at precisely the passages and applicability just checked.

## Whole-artifact finding

The complete statement and argument of C_A0008 v1 are mathematically supported at their stated scope, with no proof gap found.
The finite torsion-free construction, all twenty-three formulas, complete kernel projections, inverse admissibility, trace conventions, noncommuting infinite orbit, source comparisons and parameter boundaries satisfy the obligations above.
The nonzero-potential certificate proves nullity one for the specified eighteen-square matrices.
The zero-potential formula retains exactly \(1+\dim_H\ker(1+u+v)\); this review supplies no vanishing or arithmetic assertion for that unresolved scalar kernel over arbitrary torsion-free \(H\).
It neither proves a new whole-group Atiyah class nor resolves the full all-matrix Task.
No correction to the candidate is required for this finding, and no formal verification is claimed.
