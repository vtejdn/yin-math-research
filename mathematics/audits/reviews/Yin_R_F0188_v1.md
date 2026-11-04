---
author: Yin
---

# Independent review of the deterministic and Gaussian geometry for F0186

Review act: 2026-11-04T17:18 UTC.
The human record author is Yin.
This was a separately organized, targeted independent inspection of the fixed candidate [Yin_C_F0186_v1](../../claims/Yin_C_F0186_v1.md).
The reviewer was outside substantive proof development and received only the fixed candidate, necessary rules, the assigned scope and primary-source locators.
No exploration drafts, strategies, proof-generation dialogue, author explanations, previous review findings, mathematical messages or other-agent task summaries were consulted.
The source theorems' statements and applicability were inspected directly; their original proofs were not fully re-audited.

The inspected candidate initially bore the modification time 2026-11-04T17:07:59 UTC.
The exact inspected mathematics is its pencil statement and the sections from deterministic backward error through (T6), identified by the bindings below.
A later addition of the domain of the displayed resolvent estimate (R) lies outside this scope and changes none of these findings.
This review does not assess the subsequent scalar-polynomial linearization, Brown-measure application, resolvent comparison or logarithmic-integrability argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Targeted finding](#geometry-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Targeted finding](#geometry-finding) | [Statement](../../claims/Yin_C_F0186_v1.md#statement) | The fixed-coefficient monic GUE pencil assertion and cutoff estimate (P), including arbitrary coefficients and constants independent of N; excludes the subsequent Brown-measure conclusion. |
| [Targeted finding](#geometry-finding) | [Inputs](../../claims/Yin_C_F0186_v1.md#inputs) | The KSS polynomial-map distance inequality and Lotz tube theorem as accepted external inputs, with the source limits stated in this finding. |
| [Targeted finding](#geometry-finding) | [Argument](../../claims/Yin_C_F0186_v1.md#argument) | Only the deterministic backward-error and Gaussian tube chain through (P)/(T6); no coverage of the subsequent polynomial application. |
| [Targeted finding](#geometry-finding) | [Backward-error target](../../claims/Yin_C_F0186_v1.md#target) | Exact Hermitian perturbation statement (BE), its norm cutoff and dimension-uniform constants. |
| [Targeted finding](#geometry-finding) | [Compression](../../claims/Yin_C_F0186_v1.md#compression) | Equations (C1)-(C4), real coordinate count, full residual and bounded coordinate region. |
| [Targeted finding](#geometry-finding) | [Error bound and lift](../../claims/Yin_C_F0186_v1.md#error-bound) | KSS applicability, empty zero sets, (C5)-(C7), rank loss and uniformity in N. |
| [Targeted finding](#geometry-finding) | [Gaussian tubes](../../claims/Yin_C_F0186_v1.md#tubes) | Equations (T1)-(T6), regular-level extension, Gaussian mixture and scaling, and the algebraic rate implication; the standard GUE norm asymptotic is accepted separately and was not source-audited here. |

<a id="geometry-finding"></a>
## Targeted finding

No substantive gap or counterexample was found in the assigned deterministic and Gaussian geometric chain.
The argument establishes (BE), (P) and (T6) with constants independent of the matrix dimension, accepting the explicitly identified KSS and Lotz inputs at their checked statements.
The following checks supply the reasoning and boundaries of this conclusion.

### Compression and repair

For a unit approximate kernel vector, its component span has dimension \(1\le k\le m\), and the outgoing space has dimension \(0\le\ell\le dk\).
The two physical spaces are orthogonal, and their definitions imply \(H_jU=UA_j+VB_j\) exactly.
Consequently (C2) describes the entire residual, including every outgoing component.
Its Euclidean norm is the original residual norm.

The real input dimension is \(dk^2+2d\ell k+2mk\), with the stated upper bound independent of \(N\).
Both compressed matrix blocks have Hilbert--Schmidt norm at most \(\sqrt{k}M\), so the compact coordinate region in (C4) is valid.
The map has degree exactly two because of its normalization coordinate, even when all coefficient matrices vanish.

For a nonempty real zero set, KSS on this bounded region gives (C5), and a nearest point exists because the zero set is closed.
For an empty real zero set, the continuous residual norm has a strictly positive minimum on the fixed closed coordinate ball.
Choosing a strictly smaller residual threshold excludes that type.
Taking the minimum positive exponent, a maximum constant and one sufficiently small threshold over the finite list of types proves uniformity in \(N\).
Types not physically realizable in a particular \(N\) cause no problem.

The perturbation (C6) is Hermitian.
Multiplication by \(U\) annihilates the added adjoint off-diagonal term and produces exactly the repaired blocks \(A'_j,B'_j\).
The normalization equation makes the repaired vector nonzero of norm one, and the other equations make it an exact kernel vector.
No action on the complement of its supporting space is needed.
The three matrix blocks are orthogonal in Hilbert--Schmidt inner product, giving precisely \(\|\Delta A_j\|_{\mathrm{HS}}^2+2\|\Delta B_j\|_{\mathrm{HS}}^2\) and hence (C7).
Loss of rank among repaired vector components and the case \(\ell=0\) are harmless.
Witness-dependent isometries require no measurable selection for the resulting deterministic set inclusion.

### Primary-source matching

The reviewer read and visually inspected (KS2) on page 2 of [Kurdyka--Spodzieja--Szlachcinska, arXiv:1412.5088v1](https://arxiv.org/pdf/1412.5088v1#page=2), and read its algebraic-restriction Corollary 2.1 on page 5.
The quoted real polynomial-map inequality has the stated denominator and exponent, permits a vector-valued target and imposes no regularity of the real zero set.
Its constant may depend on the map, which is sufficient because only finitely many fixed maps occur here.
The candidate treats empty zero sets separately and does not need a source convention for their distance.

The full two-page [2019 correction](https://link.springer.com/content/pdf/10.1007/s00454-019-00128-4.pdf) was also inspected.
Its mathematical items change target-dimension exponents for semialgebraic graph arguments in the published Corollary 2.2, Remark 2.4 and Corollary 3.3.
Its final item corrects a grant number.
Comparing those exact targets with the candidate's invocation shows that the correction does not revise the polynomial-map statement (KS2) used here or the cited algebraic-restriction consequence.

The reviewer read and visually inspected [Lotz, arXiv:1210.3742v4, Theorem 1.1, page 1](https://arxiv.org/pdf/1210.3742v4#page=1), and its complete-intersection definition in Section 4.2 on page 11.
That definition requires independent defining gradients at every real zero.
Specializing the theorem to one defining equation gives precisely (T1).
No coefficient-dependent constant or compactness hypothesis is added to that statement.
The original proofs of these external inputs have not been fully reviewed here.

### Singular zero sets and tube constants

A positive global regular value \(\delta\) of \(q_N\) makes \(q_N^{-1}(\delta)\) a real smooth hypersurface satisfying Lotz's gradient condition everywhere.
Subtracting \(\delta\) does not increase its degree.
The candidate's passage from zero level to regular levels is valid on the compact set of relevant nearest zeros.
For each such zero one can choose a positive point at distance less than \(\eta/4\), then take a neighborhood of zeros of radius less than \(\eta/4\).
Each zero in that neighborhood has a segment of length less than \(\eta\) to the chosen positive endpoint.
A finite cover supplies a positive minimum of the endpoint values, and any smaller positive regular value is reached on every required segment.
Sard's theorem supplies such a global regular value.

Nearest zeros to points of the ball at distance at most \(\rho\) belong to the indicated compact set.
Thus the inclusion into the \((\rho+\eta)\)-tube is justified, including singular zeros and zero sets of real codimension greater than one.
If that relevant compact set is empty, the event is empty.
Letting \(\eta\) tend to zero uses continuity only of the explicit numerical upper bound, without assuming convergence of the hypersurfaces or their measures.

Writing \(t=\rho/\sigma\), the sum in (T1) equals
\[
4\big[(1+(2D+1)t)^n-(1+t)^n\big].
\]
The mean-value bound for powers and \(1+u\le e^u\) give (T2) for every nonnegative radius.
The exponential factor is necessary until the stated small-radius regime is imposed, and the candidate retains it correctly.

### Gaussian mixture and dimension dependence

The density \(w_n\) in (T3) is the density of \(\chi_{n+2}\).
Dividing by the volume of the radius-\(s\) ball leaves \((2\pi)^{-n/2}s e^{-s^2/2}\), whose integral from \(|x|\) to infinity is exactly the standard Gaussian density.
Thus the mixture identity is exact.
For its lower-tail estimate, the elementary exponential-moment bound gives
\[
\mathbb P\{S^2<n/4\}
\le \exp\!\left(\frac n4-\frac{n+2}{2}\log3\right),
\]
which is bounded by \(e^{-cn}\) for a universal positive \(c\).
On the complementary event, \(n/S\le2\sqrt n\), yielding (T4) with universal constants.

In real Hilbert--Schmidt orthonormal coordinates, the prescribed GUE density has independent coordinates of variance \(1/N\).
The tuple therefore has real dimension \(n=dN^2\) and equals \(N^{-1/2}g\).
The polynomial \(q_N\) is nonnegative, has degree at most \(2mN\) and is nonzero at the origin.
Empty zero sets, including the constant case, are consistent with (BE) and give no small-residual event on the cutoff once its common threshold is imposed.
For nonempty zero sets, rescaling a repair by \(\sqrt N\) proves (T5).

The substitution into (T4) gives
\[
D\sqrt n\,\rho=O(N^{5/2}\varepsilon^\alpha),
\qquad e^{-cn}=e^{-c_dN^2},
\]
with constants depending only on the fixed coefficients, \(d,m\) and the norm cutoff.
This proves (P), and adjoining the complement of the norm event proves (T6).
For \(\varepsilon=N^{-A}\), the implications from \(A\alpha>5/2\) and from \(A\alpha>r+5/2\) to the stated tube-term rates are correct.
Removal of the norm cutoff also uses the separately accepted standard normalized-GUE norm convergence; its source was not independently audited in this targeted review.

## Limits of the finding

This is an independent targeted mathematical review, not a whole-proof or Task-completion review.
It supplies no conclusion about the uninspected Brown-measure portion of F0186.
It accepts the checked external theorem statements without claiming an audit of their complete original proofs.
No numerical computation or formal verification is asserted.
