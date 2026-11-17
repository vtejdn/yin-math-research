---
author: Yin
---

# Uniform singular counts and prescribed-shift trimming for Wigner polynomials

The reviewer checked the 2026-11-17T06:36 UTC candidate of [C195v2](../../claims/Yin_C_F0195_v2.md#decision-uniform-count-candidate) on 2026-11-17T06:40 UTC under human record author Yin.
The reviewer worked outside the substantive development of this proof.
The assignment named the statement, dependencies to examine and intended scope, without development dialogue, author explanations or a prior conclusion on this candidate.
The previous review of C195v1 was consulted for that fixed input.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#uniform-count-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#uniform-count-whole-proof) | [C195v2 statement](../../claims/Yin_C_F0195_v2.md#statement) | Uniform free and expected counts, simultaneous empirical count and uniform clipped limit. |
| [Whole-proof finding](#uniform-count-whole-proof) | [C195v2 argument](../../claims/Yin_C_F0195_v2.md#argument) | Complete proof of (1)–(4). |
| [Whole-proof finding](#uniform-count-whole-proof) | [Finite counts](../../claims/Yin_C_F0195_v2.md#finite-count) | Uniform constants, shrinking net and clipping. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Scalar statement](../../claims/Yin_C_F0195_v2.md#scalar-shifts) | All compact sets of scalar shifts including the constant term. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Word-chain argument](../../claims/Yin_C_F0195_v2.md#word-chain) | Free and finite scalar transfer. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Quadratic application](../../claims/Yin_C_F0195_v2.md#fixed-shift-trim) | Each prescribed nonreal limiting shift sequence, both trims and both products. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Dyson uniqueness](../../claims/Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness) | Pointwise uniqueness of the strictly negative-imaginary-part branch for the Hermitian coefficient dilation. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Coste’s ordered-field formulation](../literature/Cos00/readme.md#ordered-real-field) | Theorem 2.6 on printed p. 28 of the October 2002 text, with arbitrary fixed real parameters. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Wigner comparison](../../claims/Yin_C_F0195_v1.md#statement) | Uniformity in the deterministic drift in the Wigner-to-GOE step. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Count comparison](../../claims/Yin_C_F0195_v1.md#count-proof) | Resolvent smoothing and powers after multiplying by the imaginary parameter. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Graph comparison](../../claims/Yin_C_F0195_v1.md#polynomial-transfer) | Min-max count for the scalar Schur complement including singular matrices. |
| [Whole-proof finding](#uniform-count-whole-proof) | [GOE comparison](../literature/Sch05/Yin_U001.md#goe-hermitization-specialization) | Theorem 3.2, equation (3.6), constant random coefficients and compact matrix parameters. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Scalar atomlessness](../literature/SS15/Yin_U001.md#ss15-u001) | Corollary 1.2 for scalar nonconstant selfadjoint polynomials in a free semicircular family. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Word-chain pivot](../../ledger/Yin_L_F0061_v2.md#linearization-transfer) | Invertible triangular pivot, shift only in the scalar corner and normalized free determinant identity. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Weak convergence](../../claims/Yin_C_F0186_v4.md#finite-variance-weak) | Weak convergence of expected selfadjoint polynomial laws under second moments. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Concentration](../../claims/Yin_C_F0186_v4.md#row-concentration) | Rank control in independent upper-row groups, with a.s. weak convergence. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Logarithmic tails](../../claims/Yin_C_F0186_v4.md#log-statistics) | Positive logarithmic uniform integrability under arbitrary cross-size coupling. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Quadratic model](../../claims/Yin_C_F0186_v36.md#statement) | Fixed real symmetric pair, fourth off-diagonal and second diagonal moments and joint independence within size. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Rank guard](../../claims/Yin_C_F0186_v36.md#rank-loss) | Uniform conditional estimates over compact subsets separated from the real axis. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Initial normalization](../../claims/Yin_C_F0186_v36.md#initial-product) | Scaling of canonical minors, bounded multiplicity of sizes and auxiliary determinant normalization. |
| [Whole-proof finding](#uniform-count-whole-proof) | [Terminal product](../../claims/Yin_C_F0186_v36.md#final-product) | Paired rank progression, summable chain bound, triangular factors and polynomial norm bound. |

<a id="uniform-count-whole-proof"></a>
## Whole-proof finding

The complete argument supports (1)–(4) with the stated hypotheses and probability quantifiers.

For fixed \(\eta>0\) the constant coefficient is a legitimate Hermitian drift after dilation.
The uniqueness argument for the Dyson equation uses a strictly contractive left-right map after weighting by the positive matrices \(-\operatorname{Im}G_j\) of the two candidate solutions, so the real polynomial system with the strict matrix sign condition selects exactly the resolvent.
All its real parameters are allowed in Coste's [October 2002 text, Theorem 2.6, printed p. 28](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf#page=29).
I checked the theorem and its treatment of existential and universal quantifiers at that passage, accepting the underlying projection theorem.
The maximum over \(K\) exists by compactness and continuity.
It decreases to zero because for each tolerance finitely many neighborhoods witness the pointwise decrease at finitely many positive scales.

In a quantifier-free description of the maximum graph at least one nonconstant defining polynomial must vanish at each interior-parameter point, since strict signs persist locally.
After dividing their product by its largest power of \(\eta\), its specialization at zero is nonzero as a polynomial and vanishes at the origin.
Its finite root multiplicity \(r\) implies \(c h^r\le C\eta\) along the graph by the bounded first derivative of a polynomial on a compact rectangle.
This supplies the uniform exponent \(1/r\) even if the maximizer changes with \(\eta\).
Integration of the resulting distribution bound against \(dt/t\) controls the free clipping error uniformly.

In the Wigner replacement the derivative estimates depend on the spectral distance \(\eta\) from the real axis uniformly in the drift.
In the Schultz estimate the deterministic coefficient stays zero and the single matrix argument is \(i\eta I-B_0(b)\).
Its norm is bounded on the specified compact set and \(\|(\operatorname{Im}\lambda)^{-1}\|=\eta^{-1}\).
After multiplication by \(t=\eta\), the two errors divided by \(t^\beta\) are bounded at \(t\ge n^{-\gamma}\) since \(\gamma(3+\beta)<1/2\) and \(\gamma(6+\beta)<1\).
The trace of the Hermitian interval indicator equals the normalized singular count including both copies at zero.
Resampling an independent upper row changes its underlying affine matrix by bounded rank, irrespective of the center.
The union over a polynomial-size net and logarithmically many thresholds costs a summable error with exponent \(n^{1-2\gamma\beta}\).
The rounding bound \(t+n^{-\gamma}\le2t\) followed by a dyadic enlargement gives \(4t\) even at the bottom endpoint.

For a fixed positive clip \(d\), pointwise weak convergence and positive-tail control apply to the singular law via the squared singular polynomial.
The finite statistics have Lipschitz constant \(1/d\) in the constant term, and continuous functional calculus gives the continuous free limit on \(K\).
Taking countably many fixed clips and a dense set of parameters, and integrating the simultaneous count bound from \(n^{-\gamma}\) to \(d\), proves the uniform almost-sure conclusion for each coupling.
This argument requires only within-size independence.

For a formal nonconstant scalar polynomial, a maximal-degree monomial contributes a coefficient \(|c_w|^2>0\) to the uniquely split word \(w^*w\) in the highest homogeneous component of the squared singular polynomial.
Scalar atomlessness and faithful trace therefore give zero kernel even at \(z=P(0)\).
The word-chain Schur equations preserve this property throughout a closed disk containing the requested compact set.
The finite graph \(x\mapsto(x,-Q^{-1}Cx)\) preserves dimension and expands norm.
Its min-max count bound loses only the fixed auxiliary size and remains valid for exact zeros.
At any fixed \(t<1\), weak convergence bounds the free mass of \([0,t]\) by the lower limit of the finite expected counts at \(t+\epsilon\), with the same constants for every shift.
The endpoint \(1\) uses total mass one.
Scalar clipped logs then converge by the same dense-set and two-clip estimates.

For each prescribed \(z_N\to z\notin\mathbb R\), the normalized old inputs have the correct canonical marginals even when a dimension occurs twice.
Splitting first and second occurrences preserves the every-coupling conclusion.
The free companion log is \(u(z)/3\) by Schur elimination with two constant pivots and normalized trace.
The uniform estimates at \(w_N=z_NN/n\to z\) leave strictly fewer than \(q_0\) singular values below the polynomial cutoff eventually, since \(n^{1-\gamma\beta}=o(N/\log^3 N)\).
All retained terms therefore have their genuine logarithm.
The omitted positive parts have total \(o(n)\) by positive-logarithm uniform integrability at a fixed drift and the bounded additive perturbation of each singular value.
The scaling sandwich has logarithmic cost at most \(2r_0|\log\sqrt{n/N}|=o(N)\).

At each growth step the final shift is \(z_N\), the retained rank rises by six and its deficit decreases by three.
The old-minor guards and paired-border estimates in C186v36 have common constants on the compact rectangle.
With the stated deficits the union of chain errors is summable and the cost \(O((N-n)\log N)\) is \(o(N)\).
The complementary upper estimate loses at most \(q_N|\log d|\) from a fixed clip of the full matrix.
Sequentially letting \(N\to\infty\) and \(d\downarrow0\) gives the two-sided companion limit at the physical normalization \(1/N\).

For each triangular factor of size \(D=3N\), determinant one identifies its top \(D-q_N\) singular product with the top \(q_N\) product of its inverse.
Using the inverse factorization as well bounds both directions of the comparison with the block diagonal matrix by \(\exp(O(q_N\log N))\).
This remains valid when a full matrix is singular and the established companion lower bound ensures eventual positivity of the retained products.
Inserting the \(2N\) unit singular values into the scalar list can reintroduce at most \(q_N\) omitted scalar values above one, each bounded by the polynomial norm estimate.
The resulting normalized discrepancy tends to zero for both prescribed trims.

The last assertion concerns each prescribed deterministic sequence.
Its border event may depend on that sequence, whereas the clipped limits hold simultaneously on each fixed parameter compact.
The conclusions leave the logarithmic contribution of the omitted smallest values unresolved.
The established source theorems and the earlier reviewed paired-border and comparison arguments were used at the named interfaces without a new audit of their complete proofs.
