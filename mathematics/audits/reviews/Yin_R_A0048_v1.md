---
author: Yin
---
# Independent review of localized cut directions and commutator bounds

## Review arrangement and inputs

The review act was completed at 2026-11-12T15:10 UTC for the human record author Yin.
A separately assigned agent outside substantive proof development inspected the fixed [C14 v5 statement](../../claims/Yin_C_A0014_v5.md#statement), its complete [argument](../../claims/Yin_C_A0014_v5.md#argument), and its [scope conclusions](../../claims/Yin_C_A0014_v5.md#what-the-estimates-do-and-do-not-settle).
The arrangement is independent review.
No exploratory drafts, proof-generation dialogue, author explanations, or previous R findings were supplied or consulted.
The reviewer enumerated the obligations from the statement and reconstructed all seventeen numbered equations and both gap-forcing implications from the fixed proof and necessary inputs.
No prior R conclusion is relied upon.

The necessary inputs are the [v4 conventions](../../claims/Yin_C_A0014_v4.md#setup-and-coefficient-averaging), its [positive translation averages](../../claims/Yin_C_A0014_v4.md#strong-sums-and-the-norm-estimate), its [cut identities and half-unit argument](../../claims/Yin_C_A0014_v4.md#cut-energies-and-the-half-unit-threshold), and the scalar specialization of [C1 v2 localization](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization).
The [original matrix boundary proof](../../claims/Yin_C_A0001_v1.md#matrix-boundary-estimate) was also read to check the scalar boundary coefficient directly.
The external scalar projectionlessness input is exactly the [BCM04 assembly-trace consequence](../literature/BCM04/Yin_U001.md#assembly-trace) combined with [HK97 amenable assembly](../literature/HK97/Yin_U001.md#amenable-assembly).
Those source units supply established published inputs with their recorded statement-level source checks; their assembly proofs are outside this review.
No new external mathematical premise is introduced.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole argument](#whole-argument) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole argument](#whole-argument) | [C14 v5 statement](../../claims/Yin_C_A0014_v5.md#statement) | All hypotheses, conventions, seventeen equations, quantifiers, convergence assertions, and both gap-forcing conclusions. |
| [Whole argument](#whole-argument) | [C14 v5 argument](../../claims/Yin_C_A0014_v5.md#argument) | Complete proof, including local estimates, boundary factorization, phase-sensitive forms, spectral concentration, and both coercive implications. |
| [Whole argument](#whole-argument) | [C14 v5 scope](../../claims/Yin_C_A0014_v5.md#what-the-estimates-do-and-do-not-settle) | Dimension versus norm distinction, absence of uniform synthesis or correlation estimates, and the stated limits of the gap-forcing conclusions. |
| [Whole argument](#whole-argument) | [C14 v4 conventions](../../claims/Yin_C_A0014_v4.md#setup-and-coefficient-averaging) | Exact finite kernels, coefficient averaging, overlap orientation, positive contraction bounds, and the normalization of the trace deficit. |
| [Whole argument](#whole-argument) | [C14 v4 positive averages](../../claims/Yin_C_A0014_v4.md#strong-sums-and-the-norm-estimate) | Strong sums of right-translated coordinate and exact-kernel projections used in equations (2), (4), (14), and (17). |
| [Whole argument](#whole-argument) | [C14 v4 cut identity](../../claims/Yin_C_A0014_v4.md#cut-energies-and-the-half-unit-threshold) | Positive cut-commutator identity, block decomposition, and the half-unit norm obstruction used in the limitations. |
| [Whole argument](#whole-argument) | [C1 v2 localization](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization) | Only the bounded scalar group-ring specialization with one column and no auxiliary denominator, giving the boundary coefficient one. |
| [Whole argument](#whole-argument) | [C1 v1 boundary proof](../../claims/Yin_C_A0001_v1.md#matrix-boundary-estimate) | Direct finite-propagation justification of the scalar boundary specialization. |
| [Whole argument](#whole-argument) | [BCM04 scalar projectionlessness interface](../literature/BCM04/Yin_U001.md#assembly-trace) | Exact scalar reduced-algebra projection consequence for finitely generated torsion-free amenable groups, with its recorded source-inspection limit. |
| [Whole argument](#whole-argument) | [HK97 assembly interface](../literature/HK97/Yin_U001.md#amenable-assembly) | Countable amenable degree-zero surjectivity used by that projection consequence; no independent review of assembly machinery. |

<a id="whole-argument"></a>
## Whole-argument finding

The complete mathematical statement and argument of C14 v5 are correct at their stated scopes.
No missing logical implication, inconsistent orientation, lost constant, spectral-endpoint error, or unsupported extension of the scalar projectionlessness input was found.
The decisive checks follow.

### Local energies and the two-scale dimension estimate

For a vector supported in T, the translated windows that cut its support are indexed by the union-minus-intersection of the sets \(W^{-1}t\).
Inversion takes those sets to \(t^{-1}W\), giving precisely the factor \(|W|\beta_W(T)\).
On either eigenspace of Q, the commutator reduces to one orthogonal projection applied to \(P_{Wz}\xi\), so its squared norm is at most \(\|\xi\|_2^2\).
This proves (1) with constant one and no convolution norm.
For \(T\subset E\), every vector in \(K_T\) lies in \(K_E\), and the same support count applies to the projections \(P_{Wz}-Q_{Wz}\), proving both parts of (2).

The cut energy is block diagonal relative to Q, so its indicated cutoff product is a projection and \(\eta h^+\le\mathsf A_W(Q)\).
Compression gives \(\|h^+Q_T\|^2\le\beta_W(T)/\eta\), including the finite and infinite versions of (3).
For an orthonormal basis of \(K_T\), coefficient averaging and traciality identify \(\tau(h^+b_T)\) with the normalized sum of the squared projected vector norms.
The positive contraction \(p-b_T\) contributes at most its trace \(\delta_T\), giving exactly (4).
The scalar specialization of C1 has \(n=1\) and \(k=0\), so its boundary coefficient is one.
No unknown \(\alpha\) remains after that replacement.
The argument controls trace dimension, including the case \(K_T=0\), and does not give an upper bound on the largest cut energy.

### Boundary map and exact factorization

If \(y\in I_W\), every coordinate \(s^{-1}y\) used by a lies in W, so cutting a global kernel vector to W preserves its equation at y.
Thus the compression range lies in \(L_W\).
A vector in \(L_W\) has its remaining possible output in \(O_W\), and vanishing there is exactly the full kernel equation.
This proves \(\ker B_W=K_W\).

The compression defect is a positive contraction supported in \(L_W\cap K_W^\perp\), proving the order statement in (5).
Rank-nullity on \(B_W|_{L_W}\) gives its asserted rank bound.
After extension by \(P_{L_W}\), the orthogonal complement of the kernel of \(B_W\) is precisely \(L_W\cap K_W^\perp\).
The finite singular-value decomposition therefore gives (6), also when \(B_W=0\).
This uses the original coefficient map and imposes no lower bound on its nonzero singular values.

### Phase-sensitive forms and small positive spectrum

The isometry with second coordinate \(\pi(x^{-1})\xi_W\) produces the kernel \(\phi_W(yx^{-1})\), which matches the left-convolution and right-window conventions.
For the defect D in the proof, \(pa^*=0\) gives \(D^*(p\otimes I)D=ar_Wa^*\).
Expanding \(D^*D\) yields (7), while expanding the squared coordinate commutators yields the strong-sum formula (8).
Both expansions have the cross terms in the stated order.
The coefficient of each ordered pair \((s,t)\) is exactly the bracket in (9), with displacement \(st^{-1}\).
Equal displacements are combined in the actual group ring.

For each group unitary the defect norm is \(\sqrt{2(1-\phi_W(s))}\).
The symmetry \(\phi_W(s^{-1})=\phi_W(s)\) gives the stated constant for the expansion of \(a^*\), hence \(\nu_W\le\epsilon_W(a)^2\).
Fixed finite support and the left Følner condition justify both zero limits.
The amplified row calculation uses \(pB=B\) and retains the rectangular matrix sizes, proving (10).

The inverse in \(T_\lambda\) is restricted to \([\lambda,\infty)\), so it is bounded, with \(a^*T_\lambda=e_\lambda\) and \(T_\lambda^*T_\lambda\le\lambda^{-1}e_\lambda\).
These identities prove (11).
The strict inequality \(\nu_W/\lambda<\eta\) makes \(h^-_{W,\eta}\wedge e_\lambda=0\).
Both projections lie below q, so finite von Neumann dimension gives
\[
\tau(h^-_{W,\eta})+\tau(e_\lambda)\le\tau(q).
\]
Its complement is exactly \(1_{(0,\lambda)}(H)\), proving (12) without counting the zero atom or losing the endpoint \(\lambda\).
Applying the triangle inequality to \(r_W^{1/2}\) on the orthogonal low and high positive spectral pieces proves (13) with the displayed square-root constant.

### The two gap-forcing implications

Every column of a nonzero finite convolution f is nonzero.
Thus the compression of \(f^*f\) to any nonempty finite window has a positive eigenvalue, and its nullspace is exactly the corresponding finite kernel.
The finite spectral inequality can therefore be translated and averaged with a single positive constant \(\gamma_W(f^*f)\).
Taking \(f=a\) and using the norm error gives both inequalities in (14).

When the error is strictly smaller than \(\gamma_W(H)\), compression to p bounds \(b_W\) below on all of p.
Because \(0\le b_W\le p\), the support of \(b_W\) is p and the nonzero spectrum of \(b_W\) is bounded away from zero.
Continuous functional calculus places p in \(C_r^*(G)\).
Finitely generated groups are countable, so the exact BCM04/HK97 scalar consequence applies under torsion-freeness and amenability.
It leaves only \(p=0\), since \(a\ne0\) excludes \(p=1\).
Then \(b_W=0\), and (14) gives the full lower bound (15).

The relative-form implication is a separate argument.
For \(f=a^*\), the normalized Hilbert direct sum of the vectors \(P_{Wz}f\zeta\) has norm \(\|f\zeta\|_2\), and the normalized sum of commutator squares is exactly \(\Gamma_W(a)\).
Minkowski's inequality and (16) give the factor \(1+\sqrt C\).
The local spectral inequality bounds the squared other side below by \(\gamma_W(f^*f)\|\zeta\|_2^2\) when \(\zeta\perp\ker f\), because \(b_W(f)\) kills that complement.
This proves (17), including its denominator \((1+\sqrt C)^2\), for every group in the setup.

Under torsion-freeness and amenability, the resulting spectral gap on the complement places the kernel projection of \(aa^*\) in the reduced algebra.
Projectionlessness removes that kernel.
Finite-trace polar decomposition then removes the kernel of a and transfers the same nonzero spectral lower bound to \(a^*a\).
Consequently bounded invertibility follows with the stated hypotheses.
Neither gap argument assumes scalar injectivity before deriving it.

<a id="what-the-estimates-do-and-do-not-settle"></a>
## What the estimates do and do not settle

The proof gives the stated local estimates, exact finite boundary factorization, finite signed commutator bounds, trace-dimension concentration, and obstructions to the two coercive upgrades.
The fixed v4 half-unit argument remains an operator-norm obstruction: its positive-contraction block argument and strong-limit passage are compatible with the small trace bounds here.
A nonzero exceptional spectral projection may have arbitrarily small trace, so (4) and (12) do not remove that obstruction.

No uniform control of the full kernel, locality of its projection, norm bound for the boundary pseudoinverse, bounded coefficient correlations, or general cut-energy upper bound below one half follows from this review.
The coercive implications concern exactly (14)'s strict error condition and (16)'s finite relative constant; they do not rule out every possible signed estimate.
There is no new group-class result or Task-completion conclusion.

This was a mathematical proof and dependency-interface review, without numerical examples or formal verification.
The existing BCM04/HK97 source identification and applicability are sufficient for their actual use; the original assembly proofs remain accepted external inputs at their recorded depth.
No additional unresolved mathematical or source-applicability obligation was found within the selected proof.
