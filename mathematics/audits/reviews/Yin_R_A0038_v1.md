---
author: Yin
---
# Independent review of the central-specialization transport certificate

Review act: 2026-11-11T18:34, in UTC minutes, for Yin.
The inspected artifact is the complete working-tree [C_A0012 v1](../../claims/Yin_C_A0012_v1.md), dated 2026-11-12 in Asia/Hong_Kong, including its statement, argument, example, comparisons and source-scope discussion.
The Claim was unselected when inspected.
This is a fresh whole-argument independent review by a separately assigned agent outside the proof's substantive development.
The reviewer received the fixed candidate path, the requested whole scope, repository instructions and operational work-round facts.
No development draft, proof-generation dialogue, mathematical development summary or prior finding about this candidate was supplied or consulted.
Necessary fixed dependencies and source-unit arguments were read directly.
Prior-review links and historical inspection descriptions occurring within those dependencies were not used as substitutes for the present reasoning checks.
The reviewer supplied no repair and made no change to the candidate.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0012_v1.md#statement) | All quantified group, matrix, specialization, trace and potential hypotheses; full row rank, complete projection, zero overlap defect, residual invertibility and complete finite-matrix kernel; the explicitly asserted weaker affiliated-inverse premise. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0012_v1.md#argument) | The entire proof from the finite-eigenvalue estimate through scalar and multivariable specialization, rational realizations, domains, group/corner transfer, graded residual and bounded kernel equations, together with the example, comparisons and source-use boundaries. |

## Reconstructed obligations and ambient objects

The statement assumes an arbitrary torsion-free discrete group \(H\), an integer \(d\ge1\), \(N:=H\times\mathbb Z^d\), and an automorphism \(\sigma\) fixing \(H\) pointwise and acting by \(GL_d(\mathbb Z)\) on the central factor.
The actual group is \(G:=N\rtimes_\sigma\mathbb Z\), with infinite cyclic generator \(t\) satisfying \(tnt^{-1}=\sigma(n)\).
The input is a finite group-ring matrix \(M\in M_{r,n}(\mathbb CN)\), where \(1\le r\le n\).
Its specialization \(M_0:=M(1,\ldots,1)\) has row Gram matrix \(L_0:=M_0M_0^*\) with an independently established inverse.
The bounded-inverse statement is a special case of the affiliated-inverse premise actually used in the argument.

The required conclusions concern the actual regular representations and their canonical group traces with unnormalized matrix trace.
They are full row rank \(r\), the complete kernel projection \(p\) with trace \(n-r\), an affiliated inverse for the overlap completion \(W\), injectivity of compressed hopping and its adjoint, and an affiliated inverse for every stated residual.
The last step must identify the actual kernel of the bounded \(2n\)-square group-ring matrix, rather than only an abstract module of the same dimension.
The selfadjoint finite coefficient potential makes that matrix selfadjoint; no commutation of the potential with hopping is available or needed.
Nothing in these obligations grants a coefficient division algebra or integrality for arbitrary matrices over \(H\).

For this review, \(L^0(\mathcal A)\) denotes the algebra of closed densely defined affiliated operators of a finite von Neumann algebra \(\mathcal A\); this is the candidate's \(\mathcal U(\mathcal A)\).
All affiliated algebra identities below have the closed-operation interpretation specified in the candidate.
I checked the distinction between those identities and pointwise claims on Hilbert-space domains.

## Finite eigenvalues and one-variable specialization

The [MSY23 U006 bounded-row repair](../literature/MSY23/Yin_U006.md#lemma-519-domain-repair) supplies the required finite-eigenprojection estimate for every affiliated operator, without a maximal-\(\Delta\), freeness or generating-tuple hypothesis.
I reconstructed its domain argument: each genuine eigenvector belongs to every power domain, so a scalar Vandermonde matrix separates a finite linear relation between distinct eigenspaces.
The bounded sum row has exactly the direct sum of these eigenspaces as its initial support and their closed span as final support.
Rectangular polar decomposition therefore equates the sum of their traces with the trace of their join.
No orthogonality or unbounded passage through a norm limit is used.
A faithful finite trace then makes the set of nonzero eigenprojections countable, by taking the union over thresholds \(1/a\).

For a bounded-coefficient polynomial \(P(z)\), translating by \(y:=z-1\) places its known affiliated unit at the constant coefficient.
Multiplying the other coefficients on the left by that inverse defines the companion entries even if the inverse is unbounded.
I checked the lower bidiagonal block and its finite inverse in \(I-yT\).
Its Schur complement is exactly \((A'_0)^{-1}\widehat P(y)\), with all multiplication orders as stated.
The [L_A0006 rank interface](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) applies because every elimination multiplier used here is already an actual affiliated unit.
For \(y\ne0\), failure of full rank is exactly the eigenvalue condition \(y^{-1}\in\sigma_{\mathrm{point}}(T)\).
The case \(y=0\) is supplied by the premise, and degree zero and degree one require no missing lower block.
Thus the exceptional scalar set is countable.

Clearing negative powers by a scalar monomial preserves the value at \(1\) and invertibility on the torus.
The same reasoning works at another prescribed nonzero base point.
This step never requires a bounded inverse of a generic slice or the inverse of a positive-degree coefficient.

## Several variables, trace and inverse domains

The induction uses the \((d-1)\)-variable specialization with the last coordinate equal to \(1\).
For almost every such slice its base value is an affiliated unit, which is exactly the hypothesis of the one-variable result just verified.
For each good slice the remaining exceptional circle set is countable.
I checked that the full bad set is measurable: the traces of \((I+aP(z)^*P(z))^{-1}\) are continuous, decrease to the faithful trace of the fiber kernel projection, and make the positive-kernel set Borel.
Fubini is therefore applicable to the exceptional fibers.

In \(\mathcal A\overline\otimes L^\infty(\mathbb T^d)\), bounded functional calculus and the tensor-product trace give the displayed integral for the regularized kernel trace.
The uniform bound \(k\tau(1)\) justifies dominated convergence.
Faithfulness gives zero actual kernel, and finite-trace polar decomposition gives an affiliated inverse.
The proof correctly integrates the canonical trace and never equates it with evaluation at one point.

I also checked the domain assertion for a bounded polynomial denominator \(L\).
Its inverse is the closed inverse on its dense range.
The regularizations \((L^*L+a^{-1}I)^{-1}L^*\) converge on that range to the inverse by the spectral theorem.
They identify the measurable inverse field in the Fourier realization.
Conversely, a measurable square-integrable inverse field defines a Hilbert vector whose bounded image under \(L\) is the original vector, establishing the claimed maximal domain.
No fiberwise inverse is asserted to act on every vector or to have a uniform bound.
For arbitrary \(H\), the finite coefficient support reduction to \(H_0\) supplies a separable realization whenever that language is wanted; right-coset copies preserve the operator statements and the canonical trace on return to the ambient group.

## Rational evaluation and the overlap certificate

I checked the recursive realization \(E=D-CL^{-1}B\) at each syntax operation, including rectangular sizes.
The sum uses a block diagonal denominator.
For the product, the upper-right denominator block \(B_1C_2\) gives the inverse block \(-L_1^{-1}B_1C_2L_2^{-1}\).
Substitution produces the four terms of \(E_1E_2\) in their original order.
The adjoint interchanges the border matrices, takes \(L^*\), and uses the Laurent involution that agrees with adjoints on the torus.
Empty denominator blocks cause no difficulty.

At an inverse gate the polynomial block \(J\) has Schur complement \(E\).
The two explicitly displayed triangular factors reduce \(J\) to \(\operatorname{diag}(E,L)\), so the premises on \(E(1)\) and \(L(1)\) certify \(J(1)\) without assuming a generic inverse.
The upper-left block of \(J^{-1}\) is \(E^{-1}\), giving the claimed new realization.
There are only finitely many resulting polynomial denominators.
Applying the already proved specialization theorem to all of them gives a common conull set of fibers and actual integrated affiliated units.
The same Schur identity supplies each selected inverse gate in the integrated algebra.
Applying one final inverse construction when \(E(1)\) is a unit proves the rational-unit implication.
This is an evaluation of certified finite syntax, not a homomorphism on the entire affiliated algebra or an appeal to undefined denominators in a free-field identity.

For \(L=MM^*\), that theorem supplies its actual affiliated inverse.
The identity \(\ker M^*=\ker MM^*\) and rectangular polar decomposition prove full row rank.
The same decomposition identifies \(M^*L^{-1}M\) as the bounded initial support projection, so its complement is the complete kernel projection and has trace \(n-r\).
The specialized formula gives the actual projection \(p_0\) under the weaker affiliated-inverse premise as well.

Evaluation at the central identity commutes with \(\sigma\), because every generator image is a central Laurent monomial and every coefficient in \(H\) is fixed.
The inverse gates for \(p\) and \(\sigma(p)\) thus have the same independently defined value \(L_0^{-1}\), and both projections evaluate to \(p_0\).
Consequently \(W(1)=p_0^3+I-p_0=I\).
The rational theorem proves \(W\) is an actual affiliated unit.
Its block structure yields an affiliated unit \(p\sigma(p)p\) on the \(p\)-corner.
The identical argument for \(\sigma^{-1}\) supplies the other overlap block.
These conclusions require neither normal hopping nor any arithmetic restriction on other coefficient projections.

## Graded residual and the complete bounded kernel

A finite-order element of \(G\) has trivial image in its infinite cyclic quotient and hence lies in torsion-free \(N\), proving the asserted torsion-freeness.
Subgroup inclusion preserves the coefficient kernel and inverse certificates in the actual regular representation.
The height characters give trace-preserving automorphisms fixing every coefficient operator and sending \(t\) to \(e^{i\theta}t\).

The bounded equations \(KK^*=p\sigma(p)p\) and \(K^*K=p\sigma^{-1}(p)p\) identify both hopping kernels as zero.
If \(p\ne0\), the corner has a faithful finite trace, and its normalization if desired matches the state convention in [L_A0007](../../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials).
I reconstructed that dependency's companion proof and character-orbit argument directly.
It permits affiliated coefficients: the diagonal phase conjugation makes the companion homogeneous, the finite-eigenprojection estimate removes its nonzero eigenvalues, and the triangular Schur elimination uses only independently certified units.

For \(C:=pVp\), the ordered product \((K^*)^{-1}R_V\) has degrees \(0,1,2\) and constant coefficient equal to the corner identity.
Thus this exact theorem applies, even though \((K^*)^{-1}\) can be unbounded.
Multiplication by the already certified \(K^*\) gives the residual inverse.
The alternative [C_A0010 v2 statement](../../claims/Yin_C_A0010_v2.md#statement) agrees at zero defect; it is unnecessary to the directly reconstructed graded proof.
The degenerate case \(p=0\), including \(n=r\), is handled by the empty corner.

The final kernel calculation uses only bounded equations.
The lower block equation forces \(\xi\in\ker M=p\ell^2(G)^n\).
Compressing the upper equation by \(p\) gives \(R_V\xi=0\), hence \(\xi=0\).
The remaining upper equation forces \(\eta\in\ker M\), and every such pair \((0,\eta)\) is killed.
This proves the actual projection \(\operatorname{diag}(0,p)\), its unnormalized dimension \(n-r\), and its probability-normalized zero mass \((n-r)/(2n)\).
No support inverse of \(M^*M\) was applied to a Hilbert vector.

## Example and exact exclusions

For the three-cycle example, direct multiplication gives \(M_0=(-2\ \ 2)\), \(M_0M_0^*=8\), and the complete graph kernel with the stated isometric frame.
The row Gram multiplier is \(2|1+x_0|^2\), which is injective but has no positive lower spectral bound.
The supported part of \(M^*M\) has the same property by polar decomposition.
The projection's entries give orbit exactly three.

I checked \(F^*\sigma(F)=(1+x_0^{-1}x_1)/2\) and both Laurent expressions in (31).
They are distinct, so the compressed hopping is not normal.
The multiplier \(h\) has values strictly between \(0\) and \(1\) on a set of positive Haar measure and is not a projection.
Commutation of \(p\) with \(\sigma(p)\) would force their compression \(h\) to be a projection, so the orbit is noncommuting.
The coefficient \(C\) vanishes on a Haar-null set but is arbitrarily small on positive-measure neighborhoods, proving the asserted unbounded overlap inverse.
The resulting four-square matrix therefore has complete kernel dimension one for every stated selfadjoint finite potential.
The index-three auxiliary subgroup is abelian, but this supplies no theorem about arbitrary matrices over the factor \(H\).

I read the actual comparison matrices in [C_A0011](../../claims/Yin_C_A0011_v1.md#finite-group-ring-origin-of-the-complete-projection) and [C_A0008](../../claims/Yin_C_A0008_v1.md#specified-group-and-finite-regular-transport-input).
In C_A0011, \(f(1)=f^*(1)=0\) kills the first \(m\) rows, whereas the last \(r\) rows retain the unit block \(I_r+AA^*\).
The specialized row rank is exactly \(r<m+r\), and the displayed rational unitary has no defined inverse gate there.
In C_A0008, augmentation on the free generators exists but sends \(\sigma(z_j)\) to \(w_j\), while applying \(\sigma\) after augmentation gives \(1\).
For a nontrivial twist these differ; the central compatible-evaluation argument is unavailable.
If all twists are trivial, the cited star has stationary projection and zero hopping defect as stated.
Neither comparison contradicts the new criterion or extends it to arbitrary noncentral parameters.

## Source use and verification limits

The mathematical source interfaces were checked in the retained [MSY23 U004 finite-trace foundations](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness), its [domain-aware rank proof](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof), its [polynomial-block supplement](../literature/MSY23/Yin_U004.md#supplement-for-the-arbitrary-domain-aside-on-p-36), and the U006 bounded-row repair.
Those units identify the 50-page published JFA 285 (2023), article 110016 edition and the relevant passages, including the printed Lemma 5.19 domain defect.
The reviewed proof uses the repaired bounded-row argument, not the defective printed limit passage.
Its rational recursion is explicit and needs no maximal-\(\Delta\) theorem, free-field embedding, inner-rank equality or center-valued projection-comparison theorem.

General affiliated-algebra closure and associativity, polar decomposition, bounded functional calculus and the tensor-product trace are accepted foundational inputs at the source units' recorded scope.
The specific rank, eigenprojection, companion, rational-block and domain interfaces used here were reconstructed directly.
The original literature PDFs, the general foundational proofs and literature-wide historical priority were not newly audited.
The candidate's attribution to existing mechanisms and its express lack of a novelty or whole-group Atiyah claim are consistent with the inspected sources and comparisons.
No numerical evidence or proof-assistant verification is used or claimed.

## Whole-argument finding

The complete stated implication and its explicitly asserted weaker affiliated-Gram premise are supported by this independent review.
I found no unresolved mathematical gap in the specialization proof, its rational evaluation and domain interfaces, the group and corner applications, the complete finite-matrix kernel, or the supplied example and exclusions.
The review supports precisely this certified finite family and the proved specialization interface.
It does not complete [T_A0001](../../tasks/Yin_T_A0001_v1.md#contract), establish all-matrix integrality for arbitrary \(H\), or assign values to rational syntax whose chosen inverse gates fail at the base point.
Claim acceptance and any later Task decision remain the responsibility of their own exact evidence selections.
