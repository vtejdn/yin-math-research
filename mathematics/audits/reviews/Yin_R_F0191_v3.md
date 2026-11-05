---
author: Yin
---

# Independent review of the positive-frame block intermediate theorem

Review date: 2026-11-05T14:02 UTC.
Human record author: Yin.
The reviewing agent did not develop this proof and received the fixed candidate, exact review assignment and operational scope without inherited substantive proof-development context.
No development draft, proof-generation discussion, author explanation or prior conclusion about the new block proof was consulted.
The review checked the complete statement and argument, including the free logarithm and every retained projection, coefficient-change, linearization and elimination boundary.
The earlier R_F0191 family was inspected to confirm its intermediate-singular-value review topic; its findings are not substituted for this new whole-proof inspection.

## Inputs

- [Fixed statement](../../claims/Yin_C_F0187_v3.md#statement) and [complete argument](../../claims/Yin_C_F0187_v3.md#argument), as selected by [the candidate decision](../../claims/Yin_C_F0187_v3.md#decision-block-intermediate-candidate).
- [Accepted bounded-product input](../../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed): only inequality (9) in its argument, for independent bounded Euclidean coordinate blocks, with its recorded original-source inspection limits.
- [Accepted finite-variance controls](../../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed): the matrix-polynomial weak law, expected and pathwise positive-log tails, and bounded FK unitriangular and Schur identities.
- [Accepted carrier theorem](../../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed): only the finite free logarithm of the real-input ordered product at parameter one.
- [Exact word-chain object](../../ledger/Yin_L_F0058_v2.md#exact-linearization): the displayed coefficient geometry was inspected for the asserted zero-frame comparison, without adopting the ledger's other arguments.
- [Original matrix-pencil contract](../../tasks/Yin_T_F0013_v1.md#contract): its arbitrary fixed coefficients, model and completion boundary were compared with this restricted intermediate theorem.

The three accepted theorem inputs were used at their actual inspected interfaces, without recursively auditing their supporting claims, review findings or original external proofs.
In particular, the scalar intermediate theorem was not tensorized, and the carrier theorem was not used in the new probability argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#positive-frame-block-reviewed) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Statement](../../claims/Yin_C_F0187_v3.md#statement) | Entire fixed complex finite-second-moment model with the additional hypothesis chi_A>0; the summable intermediate bound, free CDF and finite FK logarithm, intermediate and positive-log controls, uncontrolled bottom quantity, and all stated deterministic boundaries. |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Argument](../../claims/Yin_C_F0187_v3.md#argument) | Complete physical-block projection, conditional truncation, covariance and concentration, auxiliary net, block Schur identity, index count, logarithmic and weak-limit deductions, actual projection counterexample, coefficient transformations, word-chain geometry, Hermitization and Schur-elimination examples. |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Bounded-product concentration](../../claims/Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Accepted inequality (9) only, checked for independent complex coordinates viewed as real two-dimensional blocks, convexity, Lipschitz constant, support diameter and conditional use; no new audit of its original proof. |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Finite-variance controls](../../claims/Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Accepted fixed matrix-polynomial Hermitized weak law and positive-log controls under the exact model; bounded unitriangular and Schur identities with normalized matrix trace. |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Carrier finite target](../../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) | Real-input specialization R=s_2s_1, obtained by relabeling the distinguished input, with Q=0, one remaining carrier factor and fixed parameter one; finite free logarithm only. |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Word-chain coefficients](../../ledger/Yin_L_F0058_v2.md#exact-linearization) | Direct comparison of the displayed auxiliary blocks and couplings, establishing zero random auxiliary diagonals whenever auxiliary coordinates occur. |
| [Whole-proof finding](#positive-frame-block-reviewed) | [Matrix-pencil contract](../../tasks/Yin_T_F0013_v1.md#contract) | Scope comparison only: the additional coefficient frame and missing bottom-log estimate do not resolve the original arbitrary-coefficient determinant-limsup question. |

<a id="positive-frame-block-reviewed"></a>
## Whole-proof finding

No mathematical gap was found in the complete stated theorem or its retained boundary assertions under the three accepted inputs at the scopes above.
The conclusion requires \(\chi_A>0\), and establishes neither a least-singular-value estimate nor the determinant-limsup equality of F0013.

### Independence, covariance and uniform block directions

Deleting physical column \(i\) removes the constant and diagonal contributions to the exposed row block and every mirrored occurrence of its fresh off-diagonal variables in other retained rows.
Thus the projected other-row space is independent of the entire fresh family, although the unprojected space need not be.
The ambient and span dimensions give codimension at least \(mk\), and coordinate projection contracts both distances in the direction used by the proof.

The common good set is determined by independent physical-index families.
The union bound over the fixed \(d\) input laws gives bad-index probability at most \(dN^{-1/2}\), and the Chernoff estimate at \(N^{5/8}\) has the stated stronger exponent.
Conditioning on this set preserves independence of all retained scalar coordinates because the good event at an index is the intersection of separate modulus restrictions on its independent inputs.
Conditioning also on the independent projected other-row space does not change these laws.
Removing the bad indices costs at most \(m|\mathcal J^c|\) dimensions, leaving codimension at least \(mk/2\).

For a fixed unit \(u\), each centered physical coordinate of \(X_{\mathcal J}^*u\) is a sum of independent centered scalars multiplying \(A_j^*u\).
Both conjugate orientations have the same centered absolute variance, so its complex covariance is precisely the displayed \(T_{u,N}\).
Testing that matrix on a unit \(v\) gives \(\sum_jv_{j,N}|u^*A_jv|^2\ge\chi_A/2\).
This calculation uses no pseudo-variance hypothesis.
The nonzero conditional mean contributes a nonnegative squared projected norm, yielding the asserted conditional second-moment lower bound.

The norm of the real-linear map from all retained complex scalars to \(P_{\mathcal J}X_{\mathcal J}^*u\) is at most \(M_A\), so the accepted convex Lipschitz inequality applies with diameter \(2N^{1/4}\).
Its integrated second-moment deviation about the median is \(O(N^{1/2})\).
The \(L^2\) triangle inequality therefore puts the median above a positive multiple of \(\sqrt{k}\), since the median error is \(O(N^{1/4})\) and \(k\ge2\lceil N^{3/4}\rceil\).
The resulting lower tail has exponent \(k/N^{1/2}\).

The deterministic support bound \(\|X_{\mathcal J}\|\le C_A N^{3/4}\) makes the \(N^{-1}\)-net error \(O(N^{-1/4})\).
Because the same retained-coordinate set serves every auxiliary direction, the net event really gives the infimum over the whole unit sphere.
The cardinality \((3N)^{2m}\), the concentration exponent and the bad-index exception give the claimed single-block failure probability.
Both distance contractions then yield \(G_i\ge c_1^2kI_m\).
All these estimates are independent of \(A_0\) and the diagonal laws.

### Block Gram identity, indices and coupling

A nonzero row relation would contradict the positive distance Gram in a block with a nonzero relation coefficient, so the retained rectangular matrix has full row rank on the good event.
The diagonal block of its inverse Gram matrix is the inverse distance Gram by the Schur-complement formula.
Taking traces gives the exact displayed negative-second-moment identity and the bound \(CmN/k\); no scalar-row independence is needed here.

For every target \(4m\lceil N^{3/4}\rceil\le j\le mN-1\), the choice \(k:=\lfloor j/(2m)\rfloor\) satisfies all deletion bounds.
The singular index \(mN-j\) is admissible for the retained matrix, with exactly \(j-mk+1\) indices at or below it in decreasing order.
Using their inverse squares, row-deletion interlacing and the raw normalization \(\sqrt N\) gives the stated floor \(cj/(mN)\).
The two finite unions, over physical blocks and target indices, produce the factor \(N^{2m+2}\).
The displayed failure probabilities are summable, so first Borel--Cantelli applies under arbitrary cross-size coupling.

### Logarithmic consequences and the remaining bottom range

The increasing-index conversion is correct; the chosen \(r_N\) conservatively omits one additional index beyond the theorem's first controlled index.
If a controlled \(a_r\) is below \(t<1\), then \(r-1\le mNt/c\) and \(-\log a_r\le\log(mN/[c(r-1)])\).
The stated integral comparison therefore yields the intermediate-log bound \(Ct(1+|\log t|)\).

The accepted matrix-polynomial weak law applies to the fixed self-adjoint polynomial \(L^*L\), with normalization \(1/(mN)\), and passage through the square-root map gives the singular law.
The uncontrolled bottom fraction tends to zero, so the intermediate count passes to \(\nu_{|L|}([0,t])\le Ct\) at its continuity points and then at all small positive \(t\).
Letting \(t\downarrow0\) removes any zero atom, and integration of this CDF bound against \(dt/t\) gives a finite negative logarithm.
Boundedness of the free pencil gives its finite positive logarithm.
The finite-dimensional positive-tail conclusions have exactly the fixed matrix-polynomial scope supplied by C_F0186_v4, including expectation uniform integrability and pathwise control.

None of these steps bounds the negative logarithms of the bottom \(O(N^{3/4})\) singular values.
Their total normalized contribution can still be infinite on a singular finite matrix.
The proof leaves that quantity explicitly unresolved and does not replace the arbitrary-coefficient Task by the positive-frame subclass.

### Projection and elimination boundaries

Direct multiplication verifies the inverse of \(\begin{pmatrix}W&I\\I&0\end{pmatrix}\), and its unitriangular-times-swap factorization gives determinant \((-1)^N\) in finite dimensions and FK determinant one in the bounded free setting.
The displayed products of \(A_0\) and \(E_{11}\) generate all four matrix units.
Nevertheless deleting physical column \(i\) annihilates the entire second auxiliary row of the exposed block.
Its projected distance Gram is therefore singular for every realization, even though the actual free pencil is boundedly invertible.
This is a counterexample to the unrestricted projected-block lower bound, without asserting singularity of the original unprojected distance Gram or failure of the determinant Task.

Compactness of the two unit spheres makes \(\chi_A=0\) equivalent to a nonzero annihilating pair for all coefficient matrices.
The stated transformations \(S^{-*}u\) and \(T^{-1}v\) carry that pair to the transformed coefficient family, and the inverse transformations give the converse.
The directly inspected word-chain blocks have only constant auxiliary diagonal entries, while their variable couplings are off that diagonal.
An auxiliary basis vector tested on both sides consequently witnesses zero frame.
For \(z\ne P(0)\), the constant coefficient of that construction is invertible, and its left normalization cannot remove this witness under the just-checked equivalence.
The doubled Hermitization coefficients likewise have zero compression within the first auxiliary half.

For the second example, \(E_{12},E_{21}\) generate the full matrix algebra and have zero frame, and eliminating a diagonal identity block gives precisely \(I-W_2W_1\).
The product is bilinear in the original inputs and does not lie in the affine independent-noise model of the new estimate.
For its free target, relabeling the distinguished input in C_F0186_v10 gives the carrier \(s_2s_1\) with zero additive polynomial and one remaining factor.
Its parameter-one conclusion supplies the finite logarithm of \(s_2s_1-1\); multiplication by \(-1\) leaves that logarithm unchanged.
The accepted bounded Schur identity gives the displayed factor \(1/2\) under \(\operatorname{tr}_2\otimes\tau\).
Thus the example has a finite free target while retaining the asserted failure of closure under this elimination.
No impossibility claim about all alternative eliminations is inferred.

### Source use and limits

The actual uses of the three declared accepted inputs match their inspected statements, hypotheses and normalizations.
Their retained external-source limits remain in force, including the absence of a new audit of the bounded-product concentration proof and original bounded FK proof.
The word-chain reference serves the checked object comparison, and the unused arbitrary-minor example is not needed for any implication in this proof.
No unresolved mathematical or source-applicability gap was identified in the stated scope.
This finding supplies whole-proof evidence for C_F0187_v3 only at its exact additional positive-frame hypothesis and explicit remaining-bottom boundary.
