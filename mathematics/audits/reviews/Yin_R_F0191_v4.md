---
author: Yin
---

# Bounded two-channel physical delocalization and residual row energy: independent whole-proof review

Review time: 2026-11-05T18:56.
The human record author is Yin.
The fixed target is [C_F0187_v4](../../claims/Yin_C_F0187_v4.md#statement), including its [complete argument](../../claims/Yin_C_F0187_v4.md#argument), [declared inputs](../../claims/Yin_C_F0187_v4.md#inputs), and [selected candidate decision](../../claims/Yin_C_F0187_v4.md#decision-bounded-two-channel-candidate).
This review does not select a new Claim assessment or a Task decision.

The reviewing agent was separately assigned outside substantive development of this proof and received no inherited proof-development discussion, mathematical summary, author explanation or earlier review conclusion.
It read the exact statement and argument and the necessary fixed mathematical dependencies before forming its findings.
It did not consult drafts or previous R findings.
A second separately assigned checker, also without development context, checked the deterministic free-channel calculation and its C_F0119_v1 and L_F0066_v5 inputs; its conclusion agreed with the lead reviewer's own checks.
The lead reviewer checked the entire probability argument and residual normalization directly.
Neither reviewer contributed a repair.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Exact statement](../../claims/Yin_C_F0187_v4.md#statement) | All stated physical resolvent/projector, closest-mode and invertible-branch residual conclusions, including fixed-law hypotheses, original N normalization, uniform minor and eigenmode quantifiers. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Complete argument](../../claims/Yin_C_F0187_v4.md#argument) | All five proof sections, from the positive free-channel mass through the actual residual block identity. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Declared input scope](../../claims/Yin_C_F0187_v4.md#inputs) | Exact scope and applicability of every substantive reused input; the draft/application link supplies no mathematical premise. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Selected candidate](../../claims/Yin_C_F0187_v4.md#decision-bounded-two-channel-candidate) | The open candidate's exact statement, argument and declared dependencies; this review supplies evidence but changes no assessment. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Bounded colored moments](../../claims/Yin_C_F0186_v4.md#bounded-moments) | The fixed-law bounded-entry tree expansion and compact-support moment limit, together with the locally checked weighted insertion and finite-deletion adaptation in the target. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Bounded-differences source scope](../../claims/Yin_C_F0186_v4.md#source-scope) | Accepted ordinary independent-coordinate bounded differences from War16, Theorem 1 of arXiv v1, PDF p. 2, and retained Gui12 attribution for the moment method. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Bounded-product convex concentration](../../claims/Yin_C_F0187_v2.md#proof) | Equation (9) only, for independent bounded real scalar coordinates and a convex Euclidean Lipschitz norm; no other conclusion of v2 is adopted. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Semicircular Cauchy identity and uniqueness](../../claims/Yin_C_F0119_v1.md#resolvent-existence-and-pointwise-uniqueness) | Equations (6)--(7), the moment recursion and elementary strict-contraction uniqueness argument for the substituted selfadjoint coefficients. |
| [Whole-proof finding](#bounded-two-channel-physical-spread) | [Fixed scalar free-density bound](../../ledger/Yin_L_F0066_v5.md#identity-direction-free-density) | The same coefficient substitution, trace Poisson bound and scalar density bound of \(1/\pi\); no singular-atom or other ledger construction is used. |

<a id="bounded-two-channel-physical-spread"></a>
## Finding: the complete bounded two-channel statement is supported

No substantive mathematical gap was found in the exact statement and its complete argument under the expressly accepted external inputs described below.
The conclusion has the stated unconditional bad-event meaning on the invertible branch and does not assert high-probability invertibility.
The constants can be chosen independently of each subsequently fixed small spectral window, while its dimension threshold and failure rate may depend on that window.

### Free-channel input and positive mass

The ordered moment recursion in C_F0119_v1 proves the Dyson identity for arbitrary selfadjoint coefficient matrices, not only for that Claim's original Hermitization blocks.
Its two imaginary-part identities and strict row/column contraction prove uniqueness at positive imaginary spectral parameter with coefficients \(I_2,T\) and drift \(J_\circ\).
The ledger's inequality \(V\ge G^*VG\) makes \(V^{1/2}GV^{-1/2}\) a contraction.
Similarity therefore bounds all eigenvalues of \(G\) without requiring \(G\) to be normal, and gives the scalar trace Poisson bound and the scalar density bound by the interval/Fatou argument.

Both symmetry transformations in the target preserve the Dyson equation and strict negative imaginary part.
Direct inversion gives exactly
\[
 aD_\eta=\eta+3b,\qquad bD_\eta=\eta+2a,
 \qquad r=-\frac1{D_\eta+\beta}.
\]
Thus \(a(D_\eta^2-6)=\eta(D_\eta+3)>0\), and the trace bound gives boundedness of the positive branch.
A subsequential limit with either diagonal imaginary part zero would have both zero and \(D_0=(D_0/(D_0+\beta))^2<1\), contradicting \(D_0\ge\sqrt6\).
The resulting positive ratio and product determine one limit and agree with the target's displayed formulas.

Each channel measure is dominated by twice the scalar measure, so its density bound is \(2/\pi\).
Writing \(m:=\min(a_0,b_0)>0\), choose \(K\) with \(4/(\pi K)<m/4\).
Eventually each full Poisson transform exceeds \(m/2\), so its contribution from \([-K\eta,K\eta]\) exceeds \(m/4\) and its mass there is at least \(m\eta/4\).
This proves a common linear mass lower bound at every sufficiently small fixed window without an assumption of density continuity.

### Weighted moments and simultaneous minor concentration

Inserting an auxiliary-channel projection into the trace changes only the finite coefficient factor in each colored word.
The physical index graph, centering, tree power count and variance factors are unchanged.
The retained normalization contributes factors tending to one because \(n/N\) tends to one after at most two deletions.
Diagonal loops remain lower order with arbitrary bounded centered diagonal laws, including zero diagonal laws.
The expected weighted measures are probability measures, and higher-moment bounds plus the compactly supported limiting law justify expected weak convergence.
Their distributions depend only on the number of deleted indices.

The matrix-exponential integral formula and the trace-norm ideal inequality justify the weighted smooth-test bound without commutation of the weight with either matrix.
Replacing one upper-triangular coordinate group changes a bounded number of normalized rows and columns, with bounded rank and bounded operator norm on the entire support.
Its trace norm is consequently bounded independently of \(N\).
The bounded-differences constants for the normalized statistic are \(O(1/n)\), and the number of independent groups is \(O(N)\).
At each fixed window the resulting exponential tail absorbs the \(O(N^2)\) minor union, while expected weak convergence supplies a sufficiently large deterministic dimension threshold.
No quantitative moment-convergence rate or weighted interlacing assertion is needed.

### Fresh rows, the physical resolvent and closest modes

Deleting physical index \(i\) removes every mirrored occurrence of the raw off-diagonal coordinates in its two fresh rows.
Those coordinates are therefore independent of the retained minor, including when another physical index has already been deleted.
For every complex unit direction \(u\), the displayed covariance satisfies
\[
 Q_u\ge\gamma\operatorname{diag}(|u_1|^2,|u_2|^2),
 \qquad 6-(1+\sqrt2)^2=(\sqrt2-1)^2>0.
\]
The two weighted minor mass bounds then give the conditional projected second moment at least \(c\delta N\) uniformly in \(u\).
This directional inequality does not assume a positive one-step frame constant on the full auxiliary matrix space.

The projected norm is a convex function of independent real scalar coordinates with uniformly bounded Lipschitz constant.
The accepted convex concentration inequality gives a dimension-free bound on the squared deviation from its median.
The \(L^2\) triangle inequality then bounds the median below by \(\sqrt{c\delta N}-O(1)\), which implies the claimed lower tail for each fixed \(\delta\) and all sufficiently large \(N\).
The deterministic \(O(\sqrt N)\) bound for the fresh-row operator and a complex two-dimensional sphere net of mesh \(O(\sqrt\delta)\) extend that estimate to every direction.
The net size depends only on the fixed window, and the \(O(N^2)\) union over deleted sets and exposed indices preserves convergence to probability one.

The sign of the retained resolvent's imaginary part is positive for the convention \((\mathcal M-i\delta)^{-1}\).
Its lower bound on the small spectral projection makes the negative imaginary part of the Schur complement uniformly positive, so the inverse block norm is bounded independently of \(\delta\).
The final spectral-calculus inequality gives the physical projector estimate.
Simultaneous positive minor spectral mass ensures that a closest-to-zero eigenvalue lies in each fixed small window.
The projector estimate controls every vector in each such eigenspace, including zero eigenvalues and arbitrary multiplicities, so no measurable eigenbasis choice or simplicity hypothesis is needed.

### Residual energy and the actual inverse-block comparison

The bounded-differences estimate for each deterministic quadratic form, followed by a fixed sphere net, gives one common bounded-norm event for the full inputs and all their principal minors.
On every invertible minor, removing any one unit eigenmode leaves \(2n-1\) inverse eigenvalues.
Cauchy--Schwarz therefore bounds the squared Frobenius norm of the residual below by a fixed positive multiple of \(n\).
The scalar linear mass lower bound and scalar density upper bound also leave positive mass in a fixed-ratio annulus about zero.
Smooth-test concentration provides order \(hn\) eigenvalues in the enlarged annulus for each fixed \(h\).
Deleting one mode loses at most one eigenvalue, proving divergence of the residual squared norm divided by \(n\) uniformly over the invertible minors and all removed modes.
This uses no conditioning on an event of invertibility.

The low/high residual pieces have orthogonal spectral supports even when the removed eigenvector is chosen arbitrarily inside a repeated eigenspace.
The physical projector estimate bounds every low-energy row contribution, while the high-energy operator norm is at most \(\delta^{-1}\).
This proves the full residual row-spread bound using the basic lower bound proportional to \(n\).
The same projector estimate applied on both sides of each physical diagonal block gives the target's bound for their total energy.
Here the stronger divergence relative to \(n\) is essential to dispose of the \(O(n\delta^{-2})\) high-energy term at fixed \(\delta\) before \(\delta\) decreases to zero.

Finally, the top-left block equation for the actual inverse and the eigenvector equation give exactly
\[
 H_0=I-uu^T-FX.
\]
Since the squared Frobenius norm of \(I-uu^T\) is at most \(n\) and \(X\) is uniformly bounded on the common norm event, the displayed full-residual comparison follows with factor \(1+4K_0^2\).
Negligibility of the physical diagonal blocks and divergence relative to \(n\) yield the stated positive comparison constant \(c_*\) for the off-diagonal residual scale.
The elementary bound on each entry of the symmetrized \(H_0\) gives \(\rho_{i,w}\le d_i(\mathsf E_w)\).
Combining these estimates proves the exact residual row-spread assertion, uniformly over all removed eigenmodes on the same events.
No union over an arbitrarily chosen eigenbasis is being substituted for that quantifier.

## Source completeness and limits of the finding

The source identification and use boundaries were checked through adequate retained fixed inputs and source notes.
The bounded colored moment mechanism was checked directly in C_F0186_v4, with its recorded Gui12 Section 2.3, Theorem 4, PDF pp. 13--14 attribution.
The ordinary bounded-differences input is the recorded War16 arXiv v1 Theorem 1 on PDF p. 2, applied to independent bounded coordinate groups and scalar quadratic forms.
The convex concentration input is the recorded GNT14 arXiv v1 Theorem 3.7 and Corollary 3.8 on PDF p. 30, used here only for independent bounded real scalar coordinates.
The semicircular interface retains MS17 Chapter 9, Definition 10, Theorem 11, Proposition 13 and the Cauchy-transform relation at the exact passages recorded in C_F0119_v1 and the [MS17 source account](../literature/MS17/Yin_U001.md#offline-affine-extension-additional-source-interfaces).
The local coefficient substitution, uniqueness, density deduction and every subsequent project adaptation were checked directly.
No unresolved source-applicability objection was found in these uses.

This review reuses the recorded primary-source inspections; it does not claim a new inspection of the original PDFs or an independent proof audit of the external concentration theorems or the general MS17 cumulant foundations.
No formal verification or numerical experiment supplies the conclusion.
The proof's finite-dimensional spectral calculus, Fourier inversion, trace-norm inequalities, Schur complements and sphere-net steps were checked at their actual interfaces.

Coverage is restricted to the fixed bounded real two-channel model and the probability conclusions expressly stated in C_F0187_v4.
It does not establish high-probability invertibility, conditional probabilities divided by an invertibility probability, pole dominance, a fourth-layer energy lower bound, a least-value floor, matrix-distance conversion, a bottom-logarithm estimate, or extension to arbitrary finite-second-moment laws.
The draft single-pole application and the complete F0013 contract were not audited.
This finding does not cover other physical versions or later substantive changes of the target.
