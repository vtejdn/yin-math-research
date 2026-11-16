---
author: Yin
---

# Post-completion review of the normal rationality and general maximality criteria

## Finding

At 2026-11-16T20:03 UTC a separately assigned reviewer for Yin inspected the adopted [completion decision](../../tasks/Yin_T_F0011_v1.md#decision-complete-comparison), its [original contract](../../tasks/Yin_T_F0011_v1.md#contract) and the fixed support below.
The reviewer did not develop the proofs or receive their development dialogue, exploration notes or an explanation from the authors.
The Task and the fixed proofs themselves disclosed their conclusions; I formed my initial assessment by checking the arguments before consulting the earlier R findings.
Both original objectives hold at their stated quantifiers, and I found no mathematical reason to reopen the Task.

### Why the normal estimate applies to the original tuple

At a distinguished relative normal coordinate the liberation vacuum is \(-i[Z^*,\xi]\) in the real convention.
Its spectral measure \(\nu\) has zero mass on the diagonal, and its inverse squared gap integral is at most \(\|\xi\|_2^2\).
This does not say that \(\nu(C^2)=0\) on a cell \(C\) of positive marginal mass.
I checked where the stronger vanishing enters and how it is removed.

On a model with zero mass on each label square, every measurable subcell \(R\) of that label has \(F_{1_R\otimes1_R}\ge0\) by the projection square identity.
Split a cell of mass \(t_l>0\) into \(N\) equal pieces and average the uncentered-square test at \(k\pm N^{3/4}1_R\).
The relative error in the squared denominator \(t_l\sqrt N\) tends uniformly to zero, the trace perturbation is \(t_lN^{-1/4}\), and the two-endpoint terms in the numerator vanish on \(R^2\).
Summing the two one-endpoint terms and averaging pieces gives \(2\int k(z)^2 1_l(w)\,d\nu/t_l\), by the symmetry of the spectral measure of the selfadjoint vacuum.
The normalized positive numerators have bounded average at fixed \(l,k\), justifying replacement of the denominators even for unequal row masses.

On \(Q=3B\), center \(p\) in the cell weights and first omit the compression to \(B\).
The proposed outer products have off-diagonal sum \(-p_i^2-p_j^2+2p_ip_j\) and each vector is perpendicular to the positive mass vector \(t\); hence their diagonal is uniquely the weighted Laplacian diagonal.
Compressing the summands to \(B\) leaves scalar energy exactly on edges crossing from \(B\) to \(Q\setminus B\).
At pivot \(l\) a possibly large diagonal coefficient is paired with \(\nu_{ll}=0\); off that pivot the coefficient is at most \(4t_l\operatorname{osc}_Q(p)^2/\mu(Q)\).
Taking the trace against each positive row bound gives the lower bound with the stated sign, without a lower mass cutoff.
The case \(\mu(Q)=0\) contributes nothing.

For the real and imaginary angular tests together the squared difference is \(|z-w|^2\kappa(z,w,v)^2\).
The integral of admissible centers and radii for \(z\in B,w\in3B\) is bounded by \(\pi\int_{|z-w|/4}^{\infty}r^{-3}dr\).
Thus the edge cost is bounded by total squared curvature, and the second cost by the inverse-gap integral on the disks where \(T(B)\le K\mu(3B)\).
On the other disks the bound of C_F0337 applies to the collected kernel for that disk.
In its change of measure \(d\sigma=d\mu/f\), \(f=M_1\mu+(\iint\kappa^2\,d\mu^2)^{1/2}\), a disk has \(\sigma\)-mass at most twice its radius; assigning each triple to its smallest \(f\) controls restricted curvature by \(3\sigma(Q)\).
This permits the linear-growth theorem of Tolsa on each restriction and then the indicator tests of Lacey–Martikainen.
The smooth kernel has the required derivative bound in the second variable, and in both variables for the Hilbert-valued Hörmander estimates.
The resulting global \(L^2\) estimate permits García-Cuerva–Martell at \(p=3\); Hölder against \(f\,d\sigma\) recovers the needed density-square bound for the original measure.
No linear-growth bound on that original measure is imported.
I compared the theorem statements with the retained [Tolsa preprint, p. 102](../../literature/pdf/Tol17--arxiv-v2.pdf), [Lacey–Martikainen, pp. 1–2](../../literature/pdf/LM17.pdf) and [García-Cuerva–Martell, printed pp. 617 and 626](../../literature/pdf/GM00.pdf).

Truncating the positive disk representation and using conditional Jensen gives \(\iint |z-w|^2g(z,w)^2\,d\mu^2\le4\iiint\kappa^2\,d\mu^3\).
The two gap-weighted symbols therefore converge in the coarse norm; finite word expansions and the differentiated series at a strict selfadjoint contraction pass this limit to the analytic unitary tests.
The mixed derivative calculation uses the graph derivatives of the two phases at \(Z,Z^*\), and zero derivatives at all killed letters.
It needs no derivative normalized at the auxiliary projection.
Its defect is subtracted as \(F_g/2\), so the lower bound on \(F_g\) controls the quadratic slice energy; averaging the two unitaries and then splitting a general polynomial into real and imaginary parts removes the test restriction.

For any finite lattice model C_F0339 spreads its labels on disjoint circles of radius \(h/8\).
The relative vacuum costs \(O(B_c)\): distinct components have gaps comparable to the label gaps, and the scalar cross-component Cauchy sums differ from the center sums by \(O(M_i)\).
On the old algebra the partial liberation has \(e_i\eta e_i=0\); its extension preserves this vacuum, supplying zero mass on each individual circle square.
Smooth cutoffs approximate each component projection in operator norm and in the original derivative graph.
The two conditional circle integrals of \(1/(z-w)\) kill every nonconstant term of its uniformly convergent geometric series on unequal circles, giving \(1/(c_i-c_j)\).
Outer bimodularity recovers the discrete derivative of every label word with the same absolute estimate.
In the other direction rounding any diffuse relative coordinate to the lattice controls \(B_c\) by its own vacuum norm, using the maximal density and soft Cauchy estimates.
The rounded unit and phase tend almost everywhere to the original unit and phase off the diagonal, bounded by one, and word values converge in norm.
This proves the uniform bound for the original projection models without requiring a zero-square partition there.
C_F0308 passes it with factor at most two to finitely many selfadjoint coefficients: the \(t^{3/2}\) corner factor in the sliced witness is the same factor multiplying the leading vacuum cost after scaling, with noise chosen before the scaling.
For the actual tuple, diffuseness and the normal relations force zero on the omitted adjoints, allowing the real and imaginary parts of the other coordinates as precisely those coefficients.

The flip-adjoint derivation at \(X^*\) exchanges the slices and conjugates the actual vacuum.
For the original right slice \(E\) and left slice \(L\), the adjoint on the starred core is \(E^*p=p\xi-(L(p^*))^*\).
Their operator-norm estimates control both graphs on a uniformly bounded Kaplansky net; weak closedness puts every \(a\Omega\) in \(\operatorname{Dom}\overline E\cap\operatorname{Dom}E^*\).
The core identity \(E(X_jp)=X_jE(p)+\delta_{ij}P_\Omega p\) passes to those graph limits, so the original choice \(D=-\overline E\) has the generator-first sign.
In the opposite direction C_F0070 uses the normal commutation relations and spectral cutoffs to identify the adjoint-generator commutators with the forced phase on the represented core.
For a supplied strong system the normalized slice is \(-D_i(a\Omega)+aD_i\Omega\); testing at the vacuum gives the actual representing vector \(-D_i^*\Omega+(D_i\Omega)^*\).
Hence \(\mathsf A\Longleftrightarrow\mathsf S\) for the whole normal class, and each implies \(\mathsf F\) there.

### Fractions and signs

For maximal \(\Delta\), clearing \(u\) and the finitely many legs of its rational derivative tensors yields **one common** bounded regular fraction \(u=s^{-1}a=bt^{-1}\) with a bounded finite-rank solution of \(\sum_i[\rho(X_i),T_i]=aP_\Omega t-sP_\Omega b\).
Conversely, division of the solution tensors on the left by \(s\) and on the right by \(t\) gives the affiliated tensor identity; balancing over the division ring detects membership in the holomorphic division closure of \(\mathbb C\langle X\rangle\).
Maximality makes a solution unique at a fixed fraction.
The starred derivation domain does not change this algebra.

Under the now equivalent normal hypotheses the specified defects \(\Gamma_i=sD_i b-aD_i t\) have domains \(\{q:bq,tq\in\operatorname{Dom}D_i\}\).
For the canonical closure, its restriction to \(M\Omega\) contains the original polynomial graph and is contained in that closure, so closing the restriction gives precisely the same closed operator used in the criterion.
The natural domains contain \(M\Omega\); testing on \(M\Omega\) with the actual adjoint gives closability even for a supplied system with a different larger domain.
The specified defects for a rational element have finite rank at **every** regular fraction; finite rank in all coordinates at one common fraction also suffices.
The sign change from operator-first to generator-first gives \(T_i=-\overline{\Gamma_i}\).
At a fixed fraction the normalization term cancels by \(sb=at\); a closable finite-rank restriction has bounded closure on all of \(H\), which any other agreeing closable defect must extend and hence equal there.
This proves equality of the finite-rank closures at that fraction without identifying the two unclosed domains.
Across fractions, the outer denominators are units in the affiliated algebra and preserve the tensor rank of the same rational derivative tensor; this gives equality of numerical ranks, not of operators.

### All witnesses in the arbitrary-tuple comparisons

In C_F0133 the half-semicircle coordinate times \(\operatorname{diag}(1,-1)\) has the full semicircle law.
Extending the backward shift by zero on the reducing complement gives the rank-one commutator on all of \(H\); the bounded similarity by \(a\mapsto hah^{-1}\) fixes the vacuum and preserves the trace, hence preserves \(P_\Omega\).
The transformed element \(X=sK\) generates the full matrix algebra over the scalar center because \(X^2=s^2I\) recovers \(s\), and \(K\) and \(K^*\) generate the constant matrix units.
Negating the transported operator gives \(\mathsf S\) and hence \(\mathsf F\).
For **every** proposed normalized starred derivation, differentiating \([X^2,X^*]=0\) forces the \(e_{21}\otimes e_{11}\) coefficient of \(\delta X^*\) to be \(s/(s-t)\).
Its square is not integrable on \([1/2,1]^2\); no such Hilbert-valued derivation exists.

For C_F0225 the spectral values of \(X^*X\) recover both projections and \(u\), so the star core is the group ring of \(\mathbb Z*\mathbb Z_2\).
The given derivation respects \(s^2=1\) and the two inverse relations, and \(uqu^{-1}=(1-usu^{-1})/2\) cancels the unwanted part of \(\delta(uh)\).
In the word-cut test a cut at \(u^{-1}\) would require the next letter \(u\); the term with left factor \(usu^{-1}\) at a positive cut would require the preceding letter \(u^{-1}\).
The remaining \(u\)-cuts and the sole possible \(s\)-cut give coefficients \(1/2\) at \(u\) and \(-1/2-1/(1-\varepsilon)\) at \(us\).
These coefficients represent the actual adjoint functional on every group word with bounded norm uniformly for \(0<\varepsilon\le1/2\).
Testing at \(p\) and multiplying on the left by \(upu^{-1}\) shows \(2\varepsilon\|E\|\ge 1/(2\sqrt2)\) for every bounded dual, irrespective of \(E(1)\).

C_F0210 chooses a subsequence and trace weights for which both the diagonal starred derivative tensors and the diagonal vacuum are square summable; the separated spectral disks make the mixed inner kernel square summable as well.
On any supposed bounded dual, averaging independent signs on finitely many input corners bounds its squared norm below by \(\sum_n(t_n^3/r_n^2)\beta(T_n)^2\), which diverges for these weights.
This excludes bounded witnesses for one actual generator.
C_F0205 next adjoins a free semicircular \(s\): extending the old derivation by zero across the free factor, or extending the semicircular derivation by zero on the old algebra, preserves the corresponding vacuum by testing alternating centered words.
In any putative bare system on the pair, the dual for \(s\) and its sum with the old-coordinate dual both have the nonzero normalized commutator with the normal \(s\).
Automatic continuity from the operator norm of the algebra to \(H\) makes their difference bounded; restriction and conditional projection give a bounded witness on the old generator, contradicting the preceding lower bound.
It is this two-coordinate example that excludes **all** algebraic systems and therefore all strong systems.

Finally, the bare maximality proof first clears the range vectors of a finite-rank cycle by an injective right multiplier, so compositions with the algebraic dual are bounded finite rank before taking any trace.
Two independently chosen right multipliers test a dense set in each vacuum slot.
I checked the actual starred-domain hypothesis of [ACSY24, Proposition 3.5, published p. 35](../../literature/pdf/ACSY24.pdf); its application needs no normality or full \(M\Omega\) dual.
In the retained reconstruction the selfadjoint doubling gives Hilbert–Schmidt convergence of the regularized commutators, enough to test the same cycles.
Thus both hypotheses give \(\Delta(X)=d\) although neither implies the other on arbitrary tuples, also with \(\mathsf S\) in place of \(\mathsf F\).
For the distinct rationality boundary, the circular Fock operators have \([E,c]=P_\Omega,\ [E,c^*]=0\) and actual vacuum \(E^*\Omega=c\Omega\).
Every fraction defect of \(c^*\) vanishes on \(H\), but \(c^*\) does not commute with \(c\), whereas the affiliated centralizer contains the holomorphic division closure.
This example separates neither hypothesis.

### Scope of prior evidence and of this review

The adopted [R_F0353](Yin_R_F0353_v1.md#finding) inspected the contract and its selected support for completion.
[R_F0350](Yin_R_F0350_v1.md#finding) covers the normal theorem and its direct interfaces, [R_F0352](Yin_R_F0352_v1.md#finding) its disk-to-model passage, and [R_F0342](Yin_R_F0342_v1.md#finding) the local-mass estimate.
[R_F0233](Yin_R_F0233_v1.md#whole-proof-finding) addresses the two-point-modulus construction with the assembly and free-extension interfaces; it discloses the reviewer's prior knowledge of those methods.
[R_F0140](Yin_R_F0140_v1.md#conclusion) addresses the opposite separation.
The earlier two-domain and cutoff findings are [self-review](Yin_R_F0045_v1.md#conclusion) and [self-review](Yin_R_F0052_v1.md#conclusion); the earlier [flip-adjoint](Yin_R_F0046_v1.md#conclusion) and [circular](Yin_R_F0047_v1.md#conclusion) relationships are recorded as unknown.
None of those relationships is changed by this inspection.
I checked the project arguments at the interfaces used above; the cited source theorems and the foundations of the free-product representation, automatic continuity and affiliated free-field criterion are established inputs, without a fresh audit of all their predecessor proofs.
This is an independent project mathematical review after completion, not formal verification or external peer review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Adopted completion](../../tasks/Yin_T_F0011_v1.md#decision-complete-comparison) | Subsequent review of both conclusions as adopted, at the same original scope. |
| [Finding](#finding) | [Original contract](../../tasks/Yin_T_F0011_v1.md#contract) | Both objectives, domains, quantifiers, counterexamples and boundaries. |
| [Finding](#finding) | [Previously adopted finding](Yin_R_F0353_v1.md#finding) | Actual whole-contract pre-adoption review of the declared support, distinguished from this subsequent inspection. |
| [Finding](#finding) | [Normal equivalence](../../claims/Yin_C_F0346_v1.md#statement) | Both directions on arbitrary correlated normal generating tuples. |
| [Finding](#finding) | [Normal proof](../../claims/Yin_C_F0346_v1.md#argument) | Relative kernel lower bound, both lattice comparisons, two slices and the original operator and adjoint. |
| [Finding](#finding) | [No bare system](../../claims/Yin_C_F0225_v1.md#all-bounded-duals-and-the-separating-tuple) | Every bounded witness on the assembly and every algebraic system on the enlarged pair. |
| [Finding](#finding) | [Strong system without normalized derivation](../../claims/Yin_C_F0133_v1.md#statement) | Single generator, full Hilbert domains and obstruction independent of the putative derivation. |
| [Finding](#finding) | [Bare maximality](../../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Finite-rank regularization without normality or any imposed continuity. |
| [Finding](#finding) | [ACSY maximality](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual hypotheses of Proposition 3.5 and the Hilbert–Schmidt regularization interface. |
| [Finding](#finding) | [Existential fraction criterion](../../claims/Yin_C_F0068_v1.md#statement) | Affiliated tensor criterion and existence of one common bounded regular fraction and solution. |
| [Finding](#finding) | [Specified realizations](../../claims/Yin_C_F0068_v1.md#dual-specializations) | Some versus every fraction for strong systems, negative sign, natural domains and rank. |
| [Finding](#finding) | [Finite-rank compatibility](../../claims/Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) | Agreement on \(M\Omega\) and equality of finite-rank closures at each fixed fraction. |
| [Finding](#finding) | [Circular boundary](../../claims/Yin_C_F0074_v1.md#statement) | Nonnormality, actual starred vacuum, nonrational adjoint and rank zero at every fraction. |
| [Finding](#finding) | [Integrated estimate](../../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) | Collected signed cost on the disks of small mass and the three square-function source interfaces. |
| [Finding](#finding) | [Lattice transfer](../../claims/Yin_C_F0339_v1.md#statement) | Both directions with absolute constants; circle graph recovery versus rounding on the original law. |
| [Finding](#finding) | [Coefficient reduction](../../claims/Yin_C_F0308_v1.md#statement) | Trace-half projection constant controls all finite families of killed selfadjoint coefficients. |
| [Finding](#finding) | [Mixed energy](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Gap-weighted test, sign of the defect and scope of the actual graph calculation. |
| [Finding](#finding) | [Two domains](../../claims/Yin_C_F0072_v1.md#statement) | Actual core adjoint and graph argument for both domains. |
| [Finding](#finding) | [Reverse normal implication](../../claims/Yin_C_F0070_v2.md#actual-vacuum-under-the-additional-single-vector-adjoint-condition) | Normalized supplied system and actual vacuum on its represented starred core. |
| [Finding](#finding) | [Countable assembly](../../claims/Yin_C_F0210_v1.md#statement) | Weighted actual single-generator witness with divergent optimal bounded cost. |
| [Finding](#finding) | [Free extension](../../claims/Yin_C_F0205_v1.md#bounded-witnesses-and-the-three-universal-assertions) | Preservation of the two actual vacua, automatic continuity and compression of every proposed system. |
