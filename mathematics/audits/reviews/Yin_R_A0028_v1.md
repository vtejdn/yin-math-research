---
author: Yin
---
# Independent review of the cyclic spectral inertia bound

Review time: 2026-11-11T17:48 (UTC).
Human record author: Yin.
This is an independent whole-artifact mathematical review of [C_A0009_v2](../../claims/Yin_C_A0009_v2.md), including its scalar statement, finite von Neumann algebra statement, constant-unitary matrix specialization, every displayed bound and the three retained applications.
It is not a review of Task completion.

## Arrangement and exact inputs

The reviewer was outside substantive development of this proof and received the fixed candidate, review instructions and operational metadata, without proof-generation dialogue, development drafts, author explanations of the argument or previous findings about this candidate.
Obligations were derived from the fixed statement before inspecting the necessary dependency interfaces.
No previous R finding was consulted or adopted.
The local source unit specified below was read for its established foundational interfaces and local proofs, rather than as a verdict on this candidate.

Initial inspection covered [C_A0009_v1](../../claims/Yin_C_A0009_v1.md).
Its abstract phrase “finite tracial algebra” did not explicitly identify a von Neumann algebra with faithful normal trace, although spectral projections and deduction of zero projections from zero trace require that setting in the displayed proof.
This was a precision issue in the abstract statement, not a failure of the actual regular-group proof.
The authoring agent supplied v2 with the explicit hypotheses that the algebra is finite von Neumann, the trace is faithful, normal and finite, and its total mass satisfies \(0<d<\infty\).
The reviewer inspected the saved v1-to-v2 diff, confirmed that this is its only change, and rechecked the clarified statement and the complete affected argument and application chain.
No additional proof step or alternative mathematical mechanism was supplied by the reviewer for that clarification.

The necessary inspected inputs were:

- [L_A0002_v1, cyclic rational functions](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), for the actual bilateral-shift representation and nonzero cyclic Laurent-polynomial units.
- [MSY23 U004, finite-trace invertibility](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and [its local rank proof](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof), for polar supports, unnormalized matrix rank and rank invariance under closed affiliated multiplication.
- [L_A0006_v1, affiliated rank](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement), for the actual closed-product and Schur conventions used by the applications.
- [L_A0020_v1](../../ledger/Yin_L_A0020_v1.md#exact-inclusion-of-an-equal-modulus-trinomial-problem), including its preceding actual matrix and power-column factorization, for the original ordered Schur transfer.
- [L_A0021_v1, actual setting](../../ledger/Yin_L_A0021_v1.md#actual-setting-and-fixed-inputs), for the coincident-label cases and excluded original denominator cases only.
- [L_A0007_v1, reciprocal-ratio block](../../ledger/Yin_L_A0007_v1.md#the-reciprocal-ratio-complementary-block-and-an-independent-rank-bound), with its actual scalar definitions, for the two scalar blocks, conjugation and nullity identity.
- [C_A0008_v1](../../claims/Yin_C_A0008_v1.md#complete-finite-matrix-kernels-with-and-without-the-potential), with its specified finite input, Gram formulas, compressed coefficient and degeneracies, for the eighteen-square kernel formula and the unchanged nonzero-potential result.
- [C_A0006_v1, joint words](../../claims/Yin_C_A0006_v1.md#joint-words-still-contain-the-unknown-input) and [its scope](../../claims/Yin_C_A0006_v1.md#source-scope-and-remaining-question), for the comparison between marginal Haar information and additional joint-word constraints.

These are necessary interface inspections, not new whole-artifact reviews of every linked material.
The original MSY23 source proof and the general foundations of spectral calculus and affiliated-algebra closure were not re-audited; the identified local foundational interface was reused and its rank derivation was checked for the actual uses here.
Neither an ordered-quotient theorem nor a whole-group Atiyah theorem is a premise of the reviewed bound.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact v2 statement](../../claims/Yin_C_A0009_v2.md#statement) | Full scalar hypotheses and coefficient cases, explicit finite von Neumann trace setting, constant-unitary matrix specialization and all claimed scope restrictions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact v2 argument](../../claims/Yin_C_A0009_v2.md#argument) | Complete formulas (4)--(9), isotropic dimension comparison, Haar distributions, endpoints, group realization, matrix specialization and scalar coincidences. |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact v2 applications](../../claims/Yin_C_A0009_v2.md#consequences-for-the-retained-schur-problems) | Complete formulas (10)--(13), original Schur matrix and admissibility, complex-phase and reciprocal-ratio transfers, and finite-star trace normalization. |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact v2 limits](../../claims/Yin_C_A0009_v2.md#scope-and-next-question) | Logical limits of the proved bound, absence of an asserted shrinking construction, and separation from integrality, injectivity and historical priority. |
| [Whole-artifact finding](#whole-artifact-finding) | [Cyclic input](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | Actual Haar spectral law and independently invertible cyclic factors used here. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite-trace source interface](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) | Polar support trace identities, affiliated invertibility and unnormalized rank convention; reuse of the recorded foundational interface. |
| [Whole-artifact finding](#whole-artifact-finding) | [Closed-product rank argument](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) | Local proof of rank inequalities and invariance under actual affiliated units. |
| [Whole-artifact finding](#whole-artifact-finding) | [Application rank convention](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) | Kernel dimension invariance and Schur rank shift with independently certified denominators. |
| [Whole-artifact finding](#whole-artifact-finding) | [Original matrix](../../ledger/Yin_L_A0020_v1.md#actual-setting-and-an-elementary-screen) | Exact original ordered two-by-two matrix and its lower-right Schur pivot. |
| [Whole-artifact finding](#whole-artifact-finding) | [Power-column factors](../../ledger/Yin_L_A0020_v1.md#the-chosen-power-column-family) | Factorization and all cyclic-unit premises for the selected substitution. |
| [Whole-artifact finding](#whole-artifact-finding) | [Trinomial transfer](../../ledger/Yin_L_A0020_v1.md#exact-inclusion-of-an-equal-modulus-trinomial-problem) | Substitution h=u, f=uv, g=u cubed, k=(uv) squared, ordered factors and excluded u=e or uv=e cases. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coincidence inputs](../../ledger/Yin_L_A0021_v1.md#actual-setting-and-fixed-inputs) | Coincident support labels and the original-transfer exclusions only; no ordered-quotient theorem adopted. |
| [Whole-artifact finding](#whole-artifact-finding) | [Reciprocal-ratio identity](../../ledger/Yin_L_A0007_v1.md#the-reciprocal-ratio-complementary-block-and-an-independent-rank-bound) | Exact two-block diagonalization, conjugation and nullity doubling under the original nonidentity denominator assumptions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite-star scalar interface](../../claims/Yin_C_A0008_v1.md#normal-hopping-noncommuting-transport-and-the-exact-scalar-interface) | Isometric coefficient c-star-c divided by nine and equality of its kernel with the scalar kernel. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite-star complete kernel](../../claims/Yin_C_A0008_v1.md#complete-finite-matrix-kernels-with-and-without-the-potential) | Actual eighteen-square matrix, bounded kernel parametrization and nullities at zero and nonzero potential. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite-star degeneracies](../../claims/Yin_C_A0008_v1.md#degeneracies-previous-mechanisms-and-the-missing-scalar-unit) | Coincidence and cyclic cases necessary to cover all coefficient choices in formula (13). |

## Whole-artifact finding

The complete v2 argument establishes its stated coefficient-angle bounds and applications.
The clarified abstract setting supplies every spectral-projection, faithfulness and trace-normalization premise used by the proof.
No unresolved mathematical gap remains in this reviewed scope.

### Compression and dimension obligations

For a bounded selfadjoint \(B\) with zero kernel projection and \(pBp=0\), a vector in \(p\mathcal H\) annihilated by \(e_+\) lies entirely in the negative spectral subspace.
Its zero quadratic form forces it to vanish, since the integral of \(-t>0\) on that subspace is strictly positive for a nonzero vector even if the spectrum approaches zero.
Thus the polar factor of \(e_+p\) has initial projection exactly \(p\) and final projection bounded above by \(e_+\), whether or not its range is closed.
Equality of the two support traces gives \(\tau(p)\le\tau(e_+)\), and replacing \(B\) by \(-B\) gives the other inequality.
This verifies formula (5) without commutativity or a spectral gap.

From \((\alpha_iU_i+\alpha_jU_j)p=-\alpha_kU_kp\), taking the adjoint times the original operator gives precisely the compression in (6).
The two cross terms are \(\overline\alpha_i\alpha_jU_i^*U_j\) and its adjoint; the right-hand side is \(a_k^2p\) because \(U_k\) is unitary.
Division by the positive scalar \(2a_ia_j\) therefore gives (7) with the stated sign of \(\kappa_k\).
No projection is commuted through a unitary.

The Haar pushforward by real part has no atoms and has upper-tail mass \(d\arccos(\kappa)/\pi\) for \(-1<\kappa<1\).
Faithfulness turns its zero atom at \(\kappa\) into a zero kernel projection for \(X_{ij}-\kappa\), so the preceding dimension comparison applies.
The cosine law gives \(\kappa_k=-\cos\theta_k\), hence the two spectral masses are \(d(1-\theta_k/\pi)\) and \(d\theta_k/\pi\).
For the least angle, \(0<\theta_k\le\pi/3\), the latter is the smaller mass and proves (2)--(3).
The argument remains valid for obtuse triangles.

For three positive lengths failing a strict triangle, the largest is at least the sum of the others, and its \(\kappa_k\) is at least one.
The operator \(X_{ij}-\kappa_k\) is nonpositive with zero kernel, including equality because the Haar pushforward has no atom at one.
Its zero quadratic form on \(p\mathcal H\) therefore forces \(p=0\).
This checks the degenerate triangle boundary, not only strict coefficient dominance.

### Actual group and coefficient scope

An infinite-order regular group element has all nonzero integer moments zero and the bilateral-shift realization on each right cyclic coset.
Both arguments identify its canonical spectral law as Haar, so the scalar group statement uses precisely the declared pairwise relative-order condition.
No condition on the order of arbitrary other elements of the group is needed.
The normalized trace of a nonzero integer power of \((C_i^*C_j)\otimes(g_i^{-1}g_j)\) vanishes by the group factor.
The moment characterization of Haar therefore applies to the constant-unitary specialization, and its unnormalized total trace is the matrix size \(d\).
The proof supplies no corresponding formula (6) for arbitrary matrix coefficients and no induction over rows containing three monomials.

After coincident labels are combined and zero coefficients removed, a nonzero scalar binomial factors into a monomial times a nonzero cyclic linear polynomial.
The declared torsion-free endpoint discussion is therefore injective in every one- or two-term case.
An identically zero combined expression is correctly excluded.

### Original Schur and complex-phase applications

Substitution into the original L_A0020 matrix gives exactly
\[
 A=\begin{pmatrix}1-uv&1-u\\1-(uv)^2&1-u^3\end{pmatrix},
\]
with the noncommutative order in \((uv)^2\) preserved.
For \(u\ne e\) and \(uv\ne e\), the factors \(1-u^3\), \(1-uv\) and \(S=1+u+u^2\) are independently actual affiliated units by the cyclic input.
The ordered identity \(r=S^{-1}u(1+u-v)(1-uv)\) and the lower-right Schur reduction give
\[
 \operatorname{rank}_G A=1+\operatorname{rank}_G r
 =2-\dim_G\ker(1+u-v).
\]
This proves the exact lower bound \(5/3\) in (11), using unnormalized two-by-two rank.
If \(uv=e\), the original first column vanishes and the scalar Schur value is zero; the independent cyclic trinomial may nevertheless be injective.
The candidate correctly excludes that case from the transfer.
The \(u=e\) denominator failure and the remaining coincident-label cases also agree with the inspected input.

For \(s=(1+i)-ig-h\), the squared lengths are \(2,1,1\), giving opposite angles \(\pi/2,\pi/4,\pi/4\) and exactly the nullity bound \(1/4\).
To check the rational transfer independently, put \(a=1-g\), \(b=1-h\) and \(r=a^{-1}b+b^{-1}a\).
The bounded matrix \(J=\left(\begin{smallmatrix}-b&-a\\-a&b\end{smallmatrix}\right)\) has lower-right Schur value \(-b-ab^{-1}a=-ar\).
Since \(a,b\) are actual units, \(\operatorname{rank}J=1+\operatorname{rank}r\).
The constant unitary diagonalization of \(\operatorname{diag}(-1,1)J\) has scalar blocks \(s=b+ia\) and \(c=b-ia\), with no commutation assumption on \(a,b\).
Complex conjugation of the regular basis exchanges these blocks and preserves their kernel traces, proving \(\dim_G\ker r=2\dim_G\ker s\).
Consequently \(\dim_G\ker r\le1/2\), and all original denominators have been certified before the Schur use.
For \(g=h\ne e\), the separately stated cyclic certificate gives zero nullity instead.

### Finite-star application and remaining scope

The inspected finite-star input has \(V^*V=1\), \(p=VV^*\) of trace one, the explicitly invertible row Gram operator, and bounded \(X\) with \(BX=XB=1-p\).
Its compressed forward coefficient is \(C=c^*c/9\), so \(\ker C=\ker c\), and its actual commuting height generator identifies the residual zero-potential kernel with the isometric image of this coefficient kernel.
The bounded parametrization \((x,z)\mapsto(x,-XTx+z)\), for \(x\) in that residual kernel and \(z\in p\mathcal H\), has a bounded inverse on the full kernel of the specified eighteen-square matrix.
It therefore gives the exact unnormalized nullity \(1+\dim_H\ker c\).
The corresponding normal spectral or direct-product angular calculation removes every nonzero-potential residual kernel, leaving precisely the lower trace-one corner.
These checks confirm the actual finite matrix and scalar interface required here, without a coefficient-division premise.

For distinct \(e,u,v\), the equal-modulus theorem bounds the correction by \(1/3\).
If the support labels coincide, the inspected input reduces \(c\) to \(3\), \(2+w\) or \(1+2u\), all independently invertible; its cyclic inverse-pair case is also already settled.
Thus all parameter cases of (13) satisfy \(1\le\dim_G\ker\mathcal H_0\le4/3\), and the nonzero-potential nullity remains exactly one.

All newly proved estimates use only the indicated pairwise relative Haar laws.
The joint-word comparison is compatible with that limitation and supplies no extra premise.
No shrinking sequence, scalar injectivity theorem, full matrix integrality theorem or example attaining a positive fractional kernel is proved or assumed.
The candidate's statements about a bounded local comparison and an exploratory external search are not used as mathematical evidence; this review does not reproduce that search or certify a literature-wide novelty or absence assertion.
No new external theorem is adopted by this review.
The mathematical acceptance supported here is the complete fixed v2 statement and its precisely bounded consequences, with the broader Task still outside the review scope.
