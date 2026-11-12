---
author: Yin
---
# Coefficient potentials on the normal hopping defect: independent whole-artifact review

Review performed at 2026-11-11T17:52 UTC for Yin.
The inspected final candidate is [C_A0010 v2](../../claims/Yin_C_A0010_v2.md), including its complete statement, formulas (1)--(23), construction, source interfaces, screens, counterexample and limitations.
This is an initial independent inspection by an agent outside the candidate's substantive development.
The supplied assignment contained the exact candidate, review scope and operational authorization, without proposing dialogue, draft, mathematical summary or candidate-review conclusions.
Obligations were derived from the statement before supporting proofs were checked.
No previous R finding for the candidate was consulted.
A whole-file read of the necessary MSY23-U006 dependency also displayed its bundled earlier source-review paragraph after the reconstructed proof; the present finding rechecks the bounded-row proof itself rather than adopting that paragraph as evidence of this candidate's correctness.

The initial input was [C_A0010 v1](../../claims/Yin_C_A0010_v1.md).
The reviewer identified that its phrase "fixed projection" could be read as either action-invariant or merely chosen, whereas the corner argument requires the action-invariant reading.
Version 2 makes that intended hypothesis explicit.
Direct comparison of the two actual files showed that this is their only change.
The whole previously inspected chain was rechecked under the explicit hypothesis, including invariance of the defect, corner action, coefficient degrees and every concrete application.
The reviewer supplied no new proof or construction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0010 statement](../../claims/Yin_C_A0010_v2.md#statement) | Complete finite-tracial theorem with action-fixed p, common hopping kernel, inequalities (3), projection identities (4), finite consequences and stated boundaries. |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0010 argument](../../claims/Yin_C_A0010_v2.md#argument) | Complete affiliated proof, domains, actual corner units, inverse order, singular coefficient bound, semidefinite and Vq=0 conclusions, and downstream formulas (5)--(23). |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0010 finite matrices](../../claims/Yin_C_A0010_v2.md#complete-finite-matrix-consequence) | Independent bounded Gram inverse premise, complete Hilbert-space parametrization, orthogonal projection, dimension and zero-corner conventions in (12)--(15). |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0010 finite-star potential](../../claims/Yin_C_A0010_v2.md#an-actual-noncommuting-finite-star-potential) | All finite data, injective cyclic energy compression, all real parameters, complete kernels, noncommutation and direct screens (16)--(21). |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0010 indefinite example](../../claims/Yin_C_A0010_v2.md#why-arbitrary-indefinite-potentials-require-the-upper-bound) | Actual torsion-free group, measurable projection, complete bounded graph and orthogonal projection (22)--(23), exact upper-bound saturation and finite-group-ring exclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0010 limits](../../claims/Yin_C_A0010_v2.md#what-remains-unresolved) | Unresolved coefficient kernel, annihilating potentials, absence of zero-parameter injectivity or inverse-limit conclusion, and absence of a group-wide Atiyah claim. |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0008 argument](../../claims/Yin_C_A0008_v1.md#argument) | Reused normal-kernel and finite-star interfaces: actual group, ordered labels, complete frame, polynomial Gram inverse, normal scalar compression, coefficient defect and zero-potential graph projection, with normal spectral and canonical product-trace reasoning. |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0005 zero-defect interface](../../claims/Yin_C_A0005_v1.md#compressed-transport-certificate) | Affiliated companion proof and distinction from the bounded finite-layer alternative, for the comparison in C_A0010. |
| [Whole-artifact finding](#whole-artifact-finding) | [C_A0004 finite-layer proof](../../claims/Yin_C_A0004_v3.md#height-layer-certificate) | Bounded outer-inverse hypothesis, closed finite graph and trace estimate, only to substantiate the stated domain boundary. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0008 singular coefficient bound](../../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient) | Complete relative-inverse unit completion and rank-subadditivity argument, applied at the normalized corner trace and rescaled. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0007 character proof](../../ledger/Yin_L_A0007_v1.md#the-character-orbit-certificate) | Affiliated finite-eigenspace trace bound, infinite nonzero eigenvalue orbit and affiliated invertibility, without maximal-Delta or bounded-inverse premises. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0007 companion proof](../../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) | General affiliated coefficients, twisted action, explicit triangular lower-block inverse and ordered Schur complement. |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0006 rank interface](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) | Rank invariance under independently certified affiliated units without unrestricted Hilbert-vector substitution. |
| [Whole-artifact finding](#whole-artifact-finding) | [MSY23-U004 rank proof](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) | Local closure-domain proof of product-rank inequalities and unit invariance, with its preceding finite-trace polar and matrix-amplification setting. |
| [Whole-artifact finding](#whole-artifact-finding) | [MSY23-U006 domain repair](../literature/MSY23/Yin_U006.md#lemma-519-domain-repair) | Bounded-row Vandermonde and rectangular-polar proof for distinct eigenspaces of an arbitrary closed affiliated operator; only this general lemma is used. |
| [Whole-artifact finding](#whole-artifact-finding) | [JZ19 relative inverse](../literature/JZ19/Yin_U001.md#regular-closure-definitions) | Actual relative inverse, support identities, uniqueness and fixed-action compatibility; no smaller rational-closure membership is inferred. |

## Whole-artifact finding

The complete mathematical conclusions of C_A0010 v2 are supported at their stated operator and finite-matrix scopes.
Its explicit invariance of \(p\) supplies the action on the corner.
Homogeneity of \(K\) then makes its kernel and support projections action-invariant, so all subsequent compressed coefficients and degrees have the required meaning.
No additional normality, commutation, division-ring, integer-defect-trace or bounded-inverse hypothesis is needed.

### Singular defect and exact kernel bounds

The equality of the two hopping kernels makes both supports of \(K_r\) equal to \(r\), independently certifying its affiliated inverse before any residual calculation.
The right multiplier in (5) has the displayed two-sided inverse and degree-one lower block.
Ordered multiplication gives exactly the three summands in (6).
The constant lower-left block is \(B^*\), and the constant lower-right block is \(r\).
Right multiplication by the displayed elementary unit cancels \(B^*\), without requiring an inverse of \(D\).

The invoked singular-coefficient rank bound was checked at its actual affiliated scope.
The relative-inverse support identities make the displayed \(C_0,D_0\) in L_A0008 genuine two-sided inverses.
The perturbation retains nonnegative degrees and this independently invertible constant term.
Its complementary off-diagonal block has rank \(2(n-\operatorname{rk}A)\), so rank subadditivity yields exactly \(\operatorname{rk}P\ge\operatorname{rk}A\).
Rescaling the corner trace gives (8) with \(\tau(r)\), rather than a normalized integer.
The range-closure and kernel inclusions in MSY23-U004 prove product-rank inequalities for closed affiliated products; applying them in both directions proves unit invariance.
No unbounded multiplier is applied pointwise to an unrestricted Hilbert-space kernel.

The lower projection \(q_0\) is killed by all three bounded summands of \(R\).
For positive \(V\), the energy identity on \(\delta\) identifies \(q=q_0\), and negative \(V\) reduces to the same argument for \(-V\).
If merely \(Vq=0\), the bounded equations likewise give \(q\le P_{\ker R}\).
The rank upper bound and faithfulness then give the stated actual projection equalities.
The degenerate cases \(p=0\), \(r=0\), \(\delta=0\) and \(q=0\) agree with the formulas and conventions.

### Ordered Schur elimination and affiliated grading

For injective selfadjoint \(D\), finite-trace polar decomposition provides its actual affiliated inverse.
In \(U^*RU\), the off-diagonal cancellations are \(-DD^{-1}B+B=0\) and \(-B^*D^{-1}D+B^*=0\).
The remaining block is precisely \(K_r+K_r^*+E-B^*D^{-1}B\), with a selfadjoint action-fixed effective coefficient.
Right multiplication by \((K_r^*)^{-1}\) produces the identity constant term in (11).
The order of every Schur factor is correct.

The general affiliated companion criterion is justified by its inspected proof.
Genuine eigenvectors of a closed operator belong to every needed power domain, and finite Vandermonde equations make their sum map injective.
The bounded row of eigenprojections has initial support their diagonal sum and final support their join.
Rectangular polar decomposition bounds the sum of eigenspace traces even if the algebraic eigenspace sum is not closed.
An infinite phase orbit of a nonzero eigenvalue then forces each such kernel trace to vanish.

The diagonal twist makes the companion matrix homogeneous for a trace-preserving action.
The lower-right block of identity minus the companion has an explicit finite triangular inverse, and its Schur complement is exactly the normalized original polynomial.
This proves the assertion for the possibly unbounded effective coefficient in (11).
Only the established affiliated algebra and independently known units are used.
The C_A0004 recurrence instead requires bounded outer inverses to obtain a closed bounded graph and cannot independently justify this unbounded case.
The candidate states that limitation correctly.

### Complete finite matrix kernels

The bounded Gram inverse premise yields \(B_AX=XB_A=1-p\) and \(Xp=pX=p\) before residual injectivity is considered.
The lower equation forces \(x\in p\ell^2(G)^d\), and the upper equation compressed by \(p\) is exactly the residual equation.
An injective defect compression therefore forces \(x=0\) and \(y\in p\ell^2(G)^d\), proving the complete projection (13).

In the semidefinite case the same equations force \(x\in k\ell^2(G)^d\).
Since \(pS_0k=0\), the vector \(-XS_0x\) lies in \((1-p)\ell^2(G)^d\), solves the remaining equation and is orthogonal to every lower \(p\)-coordinate.
Thus the inverse parametrization really reads \(x\) and \(py\).
The graph operator is bounded below on the range of \(k\) by its first coordinate, so \(D_k\ge k\) has a bounded corner inverse.
The displayed graph projection and its orthogonal sum with \(\operatorname{diag}(0,p)\) prove both assertions in (15), including \(k=0\).

The reused star construction was checked directly.
Its eight transport entries are unitaries, giving \(d^*d=8\), an isometric nine-coordinate frame, and the complete kernel of \((-d\ I_8)\).
The identity \((dd^*)^2=8dd^*\) verifies the explicit row Gram inverse.
Using \(AA^*J=JAA^*=I_8\) verifies both orders of the identities for \(X=p+A^*J^2A\).
The ordered six labels give \(F^*\sigma(F)=(3+\sum_jw_j)/9=c^*c/9\).
Since \(\sigma\) fixes \(H\), \(Ct\) is normal with defect \(e\), and frame transport gives \(\delta=FeF^*\).
The explicit automorphism inverse and the free-product and cyclic-quotient arguments establish the actual torsion-free group.
The canonical subgroup trace and bounded normal spectral calculation also validate the reused zero-potential kernel and graph projection without assuming \(e=0\).

### Cyclic energy, noncommutation and the direct screens

The free letter \(z\) has infinite order for every allowed choice of the original labels.
Its shift has no nonzero fixed square-summable vector, so \(1-z\) and \(W\) are injective.
The cyclic Fourier multiplier approaches zero on positive-measure sets, so the affiliated inverse exists and is unbounded.
For \(x\in e\ell^2(G)\), (17) proves that \(eWe\) is injective without computing \(e\), using \(c^{-1}\), or asserting a positive lower bound.
All nonzero real parameters consequently have the stated complete kernel and normalized zero atom.
At zero parameter the retained graph has the stated trace correction.

For \(w_j\ne1\), free-product normal forms make the coefficient of \(z_j\) in (20) exactly \(-C_1\).
The other three terms do not contribute to that word.
Coincident labels preserve \(C_1\ge1/3\), so noncommutation is proved independently of \(e\).

At \(\lambda=1/10\), support contains the identity and the noncommuting elements \(z,t\), excluding containment in a cyclic subgroup or coset.
Height \(1\), height \(-1\) and potential supports are disjoint, giving coefficient absolute-value sum \(2+4\lambda\).
Every hopping coefficient is at most one and each potential coefficient is at most \(2\lambda\), so no coefficient dominates all the others.
For vectors supported on \(H\times\mathbb Z\), the \(z^{\pm1}\) terms contribute zero quadratic form and the potential contributes \(2\lambda\).
Tensor-product spectral localization near the upper edge of \(C\) and the negative height edge gives a negative form because \(\|C\|>\lambda\); the positive height edge gives a positive form.
Selfadjointness then excludes nonnegative real part for every scalar phase with nonzero real part.
A purely imaginary phase has zero, noninjective real part.
These calculations establish exactly the three direct screens, without excluding every factorization or larger realization.

### Indefinite boundary and unresolved scope

In the measurable example, inversion exchanges the two coefficient semicircles, so \(q_+tq_+=0\).
The compressed hopping is precisely \(\operatorname{diag}(t,0)\), is normal and has the stated defect.
The potential is selfadjoint and indefinite, its defect compression is zero, and its kernel has trivial intersection with that defect.
The lower equation gives \(x\in(1-q_+)\ell^2(G)\).
The identity \(S(1-q_+)=q_+S\) makes the upper equation equivalent to the unique lower coordinate \(-Sx\).
This bounded closed graph has the displayed projection, a bounded first-coordinate inverse and trace \(1/2\), attaining the upper bound with zero lower bound.

A scalar group-ring or rational-function idempotent over \(\mathbb C[a^{\pm1}]\) is zero or one, whereas \(q_+\) has trace \(1/2\).
The example is therefore outside the finite group-ring matrix contract.
The general finite-tracial theorem supplies no integer trace for \(q\) or \(\delta\).
The frame potential \(W=C\) annihilates \(e\), so semidefiniteness alone does leave that defect.
The cyclic energy potential resolves its nonzero-parameter residual without settling the zero-parameter trinomial kernel.
No uniform inverse bound or limiting argument at zero was proved or used, and no whole-group Atiyah conclusion follows.

## Source and verification limits

The fixed local proof interfaces in the bindings were directly inspected, and their decisive algebraic, domain and trace arguments were reconstructed.
MSY23-U004 retains the basic affiliated star-algebra, matrix amplification and finite-trace polar-decomposition foundations, and JZ19-U001 supplies the actual relative-inverse conventions.
Those foundational theories are accepted at their retained scope without a new construction or associativity proof of the general affiliated algebra.
The MSY23-U006 repair was checked as a complete local proof of the general eigenspace lemma, independently of maximal-Delta and free-field results.
No new primary-source PDF audit or literature-wide priority search was performed.
No source theorem outside these inspected interfaces is required by the candidate.
Unrelated dependency results and old source-review paragraphs receive no new whole-file endorsement.
This finding is a mathematical review of C_A0010 v2, not formal verification or a completion review of T_A0001.
