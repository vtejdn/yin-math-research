---
author: Yin
---

# Full-domain duals and conjugate variables for normal and arbitrary tuples

## Finding

At 2026-11-16T19:56 UTC an agent reviewing for Yin independently checked the original [F0011 contract](../../tasks/Yin_T_F0011_v1.md#contract) and the fixed support listed below.
The reviewer took no part in developing the proofs and received the contract, target locators and review assignment without proof-development dialogue, additional author explanations or exploration notes.
The fixed materials contained their own historical assessments.
The reviewer formed the mathematical findings from the proofs before consulting the earlier review records for their actual scope and relationships.

For every tuple of bounded normal generators in the contract, \(\mathsf A(X)\) is equivalent to \(\mathsf S(X)\), with the specified canonical choice \(-\overline{(\mathrm{id}\otimes\tau)\partial_i}\).
The two rationality tests consequently apply to the same normal tuples.
For arbitrary finite generating tuples, each of \(\mathsf F\) and \(\mathsf A\) implies maximal \(\Delta\), and neither implies the other.
The same two counterexamples separate \(\mathsf S\) and \(\mathsf A\) on that class.
The support meets the original completion criteria.

### The normal-coordinate estimate

I rederived the new uniform estimate in [C_F0346](../../claims/Yin_C_F0346_v1.md#argument).
For a relative coordinate the partial liberation vacuum is a scalar multiple of \([Z^*,\xi]\), so its spectral measure has no diagonal mass and \(\int |z-w|^{-2}\,d\nu\le\|\xi\|_2^2\).
In the circle models every square of a single label also has zero mass.
Inside any such cell, including any of its subcells \(R\), the projection square identity gives \(F_{1_R\otimes1_R}\ge0\).
In the two spike tests \(k\pm N^{3/4}1_R\), where \(\mu(R)=t_l/N\), the squared denominator is asymptotic to \(N^{1/2}t_l\) uniformly among subcells at fixed \(l,k\).
Averaging signs cancels the odd terms, and the product of two endpoint indicators vanishes in the integral against \(\nu\).
Averaging over the cells and using symmetry of \(\nu\) leaves the term \(2\sum_i k_i^2\nu_{il}/t_l\).
The spike's trace is \(O(N^{-1/4})\).
This proves the required positive semidefinite inequality for every pivot using only the distinguished relative derivative.

On \(Q=3B\), centering \(p\) makes every uncompressed vector \(r_l,b_l\) orthogonal to the cell-mass vector \(t\).
Expanding the outer products gives off-diagonal contributions \(-(p_i^2+p_j^2)\) and \(2p_ip_j\).
The null vector \(t\), with all entries positive, fixes the diagonal as \(\sum_j(p_i-p_j)^2t_j/t_i\).
Compressing these positive summands to \(B\) leaves boundary energy \(\sum_{i\in B,j\in Q\setminus B} t_it_j(p_i-p_j)^2\).
Each diagonal cost away from its pivot is bounded by \(4(t_l/\mu(Q))\operatorname{osc}_Q(p)^2\), and the pivot costs zero since \(\nu_{ll}=0\).
The trace pairing with the positive matrices gives the lower bound (1), including its sign, for every bounded real spectral test \(p\) by uniform simple approximation.

For the two angular components the boundary energy integrates to at most a constant times the total squared curvature.
Indeed their squared differences sum to \(|z-w|^2\kappa^2\), whereas the integral in centers and radii is at most \(C/|z-w|^2\).
The same integral against \(\nu\) controls the second term on disks with \(T(B)\le K\mu(3B)\) because the integrated squared oscillation is \(O(T(B))\).
Disks with \(\mu(3B)=0\) give zero pairing.
On the remaining disks the [absolute estimate of C_F0337](../../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) applies to the two angular components after integration in the third point.
Its unconditional part uses only the distinguished derivative and the scalar marginal energy.
At truncated scales the kernel pairing is linear and normal on bounded kernels.
The truncations increase to the curvature kernel up to a positive absolute normalization, and \(|z-w|^2 g^2\) is integrable by conditional Jensen and \(|z-w|\kappa\le2\).
The two gap tensors therefore converge on fixed words and on the two analytic unitary tests.
In [the mixed energy identity](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) the signed term is \(-F_g/2\).
All omitted letters have zero derivative in the relative proof, so the same product rules, phase graphs and test estimates apply there.
Solving the quadratic bound and averaging the two unitary tests proves the required original slice estimate with an absolute constant.

The [circle construction and graph recovery](../../claims/Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) preserve the original finite-label words.
On distinct circles the conditional mean of \(1/(z-w)\) equals \(1/(c_i-c_j)\) by the convergent geometric series and vanishing nonconstant circle moments.
Graph approximation of the label projections and bimodularity recover the discrete derivative on every word, with vacuum cost \(O(B_c)\).
In the reverse rounding direction \(B_c\le C\|\xi\|_2\) and both the off-diagonal indicator and discrete phase converge on the original coarse space by diffuseness.
This order removes the zero-square partition assumption from the original law.
The [trace-half coefficient comparison](../../claims/Yin_C_F0308_v1.md#statement) loses at most a factor two regardless of the number of selfadjoint coefficients.
Normality and diffuseness force zero derivative on the omitted adjoints, so these coefficients may be the real and imaginary parts of every other coordinate.
The left slice follows by the flip-adjoint operation, which preserves the vacuum norm and exchanges the two slices.

The core adjoint of the right slice is bounded in terms of the left slice and \(\|\xi\|_2\) by its adjoint pairing on the represented starred algebra.
Uniformly bounded Kaplansky approximants therefore have weakly convergent subnets in both graphs.
Weak closedness puts each \(a\Omega\), \(a\in M\), in the original closure and its actual Hilbert adjoint domain.
Graph approximation passes the generator commutator to the closure and negation gives the generator-first sign.
Conversely, normal strong duals give Hilbert–Schmidt commutators on the represented starred core.
The [spectral cutoff argument](../../claims/Yin_C_F0070_v2.md#proof-by-continuous-cutoffs-and-finite-averaging) kills the diagonal error by diffuseness and forces the adjoint-generator phase.
After normalizing a supplied dual at the vacuum, the double-trace functional is represented by \(-D_i^*\Omega+(D_i\Omega)^*\), which uses the actual adjoint at \(\Omega\).
These steps establish the claimed equivalence for arbitrary correlations and also give \(\mathsf A\Rightarrow\mathsf F\) on normal tuples by restriction.

### The fraction quantifiers and operator domains

With \(\Delta=d\), the affiliated tensor criterion uses the unstarred division closure \(F=\operatorname{Div}_{L^0(M)}\mathbb C\langle X\rangle\).
For a rational element one can clear on the left and right the finitely many factors of its derivative tensors along with the element itself, producing one common bounded regular fraction \(Q\) and a finite-rank solution.
Conversely dividing a solution's tensors by its two regular denominators and balancing over the division ring gives \(u\in F\).
The finite-rank cycle criterion gives uniqueness at a fixed \(Q\).

For normal strong systems the dense left module and adjoint test module can both be \(M\Omega\).
The finite-defect fraction algebra and its common-denominator argument apply, while the normal commutation identity gives the boundary equation with right multipliers \(\rho(X_i)\).
The canonical closed operator is the closure of its restriction to \(M\Omega\), since that restriction contains the original polynomial core and lies inside the closed operator.
At each legal \(Q\) its literal fraction expression is defined on the dense set \(\{v:bv,tv\in\operatorname{Dom}D_i\}\).
Testing against \(M\Omega\) in the adjoint identifies any finite-rank bounded extension there with the full natural-domain expression.
For the generator-first convention the unique solution is the **negative** of the fraction closure.
Finite rank at one common \(Q\) for every \(i\) suffices and entails finite rank at every \(Q\), with coordinatewise rank independent of \(Q\).
For a supplied strong dual, the normalization discrepancy on \(M\Omega\) cancels by \(sb=at\).
Both expressions are closable, so whenever one has finite rank their closures agree for that fixed \(i,Q\).
No equality of two arbitrary unclosed domains or of solutions at different fractions is needed.

### The general-tuple separations and maximality

In [C_F0133](../../claims/Yin_C_F0133_v1.md#statement) the bounded tracial inner similarity preserves \(\Omega\) and \(P_\Omega\), so it transports the negative semicircular backward shift, extended by zero on the reducing complement, to a generator-first dual with both domains equal to \(H\).
The central square of \(X=sK\) recovers \(s1\) and its spectral cuts recover \(K\), which gives the constant matrix units.
Differentiating the represented relation \([X^2,X^*]=0\) forces the \(e_{21}\otimes e_{11}\) coefficient of every possible \(\delta X^*\) to equal \(s/(s-t)\) almost everywhere.
Its square is nonintegrable on an interior square with positive density.
This excludes every normalized starred derivation while verifying \(\mathsf S\) and \(\mathsf F\).

In [C_F0225](../../claims/Yin_C_F0225_v1.md#all-bounded-duals-and-the-separating-tuple), \(X^*X\) recovers both spectral projections, so the star core is the group algebra of \(\mathbb Z*\mathbb Z_2\).
I checked the presentation relators, the cancellation giving \(\delta X=1\otimes1\), and the cut enumeration on reduced words.
Only \(u\) and \(us\) survive in the double trace, with coefficients \(1/2\) and \(-1/2-1/(1-\varepsilon)\), giving an actual uniformly bounded adjoint vacuum.
Testing any bounded \(M\to L^2(M)\) dual at \(p\) and multiplying by \(upu^{-1}\) gives \(\|E\|\ge1/(4\sqrt2\,\varepsilon)\) independently of its value at the vacuum.
In [the countable assembly](../../claims/Yin_C_F0210_v1.md#simultaneous-testing-of-diagonal-duals), scaling controls the diagonal starred derivatives and the squared vacuum norms, while separation of the spectral disks gives a square-summable mixed inner kernel.
The simultaneous sign test forces any bounded witness to dominate the divergent weighted sum of squared corner costs.
The [free semicircular extension](../../claims/Yin_C_F0205_v1.md#bounded-witnesses-and-the-three-universal-assertions) preserves both actual derivations by reduced-word testing.
On that extension the semicircular coordinate makes every member of an algebraic dual system bounded from the algebra norm to the Hilbert norm, by applying automatic continuity to its own dual and that dual plus the other member.
Conditional compression would thus give a bounded witness for the assembled generator.
This contradiction excludes every algebraic system on the pair, hence also every strong system.

The [bare-domain proof](../../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) first clears the finitely many cycle range vectors using an injective right multiplier and applies the dual only after those ranges lie in \(M\Omega\).
The composites are then bounded finite rank, and two independent right multipliers provide dense tests after taking the usual trace.
Thus no normality, adjoint or continuity of an initial dual is used in proving \(\mathsf F\Rightarrow\Delta=d\).
I checked the derivation definition, Theorem 3.4 and Proposition 3.5 on published pp. 34–36 of [ACSY24](../../literature/pdf/ACSY24.pdf) against the source unit.
Its starred-core and actual adjoint hypotheses coincide with \(\mathsf A\).
In the source unit's reconstruction, resolvents of the selfadjoint doubling regularize the generator commutators in Hilbert–Schmidt norm, which suffices to test each finite-rank cycle.
This gives the second maximality implication without assuming \(\mathsf F\).
Finally the circular example has both hypotheses and a bounded canonical dual commuting with \(c^*\).
Every fraction of \(c^*\) then has zero commutator, while the division closure is contained in the centralizer of \(c\) and \([c,c^*]\Omega\ne0\).
This checks the stated boundary on extending the fraction test to nonnormal tuples.

### Depth of the reused inputs

After the initial checks I verified that the [proved decision](../../claims/Yin_C_F0346_v1.md#decision-reviewed) selects the same statement and argument inspected here.
The [independent review of C_F0346](Yin_R_F0350_v1.md#finding) covers its complete normal theorem and twenty-one direct interfaces, and the [disk and circle-model review](Yin_R_F0352_v1.md#finding) checks that narrower transfer.
The [bad-disk review](Yin_R_F0342_v1.md#finding) checks the precise square-function and kernel theorems used there at their statement interfaces.
The [matched-energy review](Yin_R_F0302_v1.md#finding), [lattice review](Yin_R_F0344_v1.md#finding) and [single-projection review](Yin_R_F0317_v1.md#finding) cover the gap-weighted limit, both directions of discretization, and the factor-two coefficient reduction, respectively.
I checked their applications above and used the published harmonic-analysis theorems at those documented scopes.
The [general separation](Yin_R_F0233_v1.md#whole-proof-finding), [similarity](Yin_R_F0140_v1.md#conclusion), [original maximality proof](Yin_R_F0067_v1.md#fresh-v1-original), [fraction criteria](Yin_R_F0041_v1.md#conclusion) and [supplied-dual comparison](Yin_R_F0048_v1.md#conclusion) have prior reviews at those respective scopes.
The earlier [two-domain](Yin_R_F0045_v1.md#conclusion) and [normal converse](Yin_R_F0052_v1.md#conclusion) findings are self-reviews, and the earlier [flip-adjoint](Yin_R_F0046_v1.md#conclusion) and [circular example](Yin_R_F0047_v1.md#conclusion) findings have unknown relationships.
This review checked the steps needed from all four directly.
It uses the source units' existing foundations for the free-product representation, automatic continuity, finite-tracial affiliated operators and the maximal-\(\Delta\) characterization.
The review is a mathematical inspection of the stated contract and its assembled proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Original contract](../../tasks/Yin_T_F0011_v1.md#contract) | Both implication questions, actual operator and adjoint domains, all-witness counterexamples, both rationality criteria, and the nonnormal boundary. |
| [Finding](#finding) | [Normal theorem](../../claims/Yin_C_F0346_v1.md#statement) | Every finite normal generating tuple, both oriented slices, the original canonical system, converse and fraction consequences. |
| [Finding](#finding) | [Normal proof](../../claims/Yin_C_F0346_v1.md#argument) | Pivot estimates, compressed Laplacian, integration, graph recovery, both universal reductions and canonical and supplied-operator applications. |
| [Finding](#finding) | [Two-point-modulus separation](../../claims/Yin_C_F0225_v1.md#all-bounded-duals-and-the-separating-tuple) | Uniform actual vacua, unrestricted bounded cost, countable assembly and exclusion of every algebraic system after free enlargement. |
| [Finding](#finding) | [Bounded-similarity separation](../../claims/Yin_C_F0133_v1.md#statement) | Whole-H strong dual, generation and failure of every normalized represented starred derivation. |
| [Finding](#finding) | [Bare maximality](../../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Common right denominator, finite-dimensional compositions and dense independent tests for arbitrary tuples. |
| [Finding](#finding) | [ACSY24 Proposition 3.5](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual represented starred-core adjoints, regularization of the canonical system and maximality without normality. |
| [Finding](#finding) | [Existential boundary equation](../../claims/Yin_C_F0068_v1.md#statement) | Holomorphic division closure in the affiliated algebra and one bounded regular fraction with a solution in bounded finite-rank operators. |
| [Finding](#finding) | [Specified fraction test](../../claims/Yin_C_F0068_v1.md#dual-specializations) | One common versus every fraction, uniqueness at a fixed fraction, dual convention, all natural domains and ranks. |
| [Finding](#finding) | [Canonical comparison](../../claims/Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) | Agreement on \(M\Omega\), closability and equality of the bounded finite-rank closures for the same prescribed fraction. |
| [Finding](#finding) | [Circular boundary](../../claims/Yin_C_F0074_v1.md#statement) | Both actual hypotheses on \(c\), holomorphic nonrationality of \(c^*\) and every-fraction vanishing. |
