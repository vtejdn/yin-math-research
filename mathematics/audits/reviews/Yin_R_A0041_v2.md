---
author: Yin
---
# Independent review of bounded coefficient mass and polynomial localization

## Review arrangement and inputs

This review was performed at 2026-11-12T13:17 for Yin by the same separately assigned reviewer who performed the [independent v1 review](Yin_R_A0041_v1.md#whole-argument).
The reviewer remains outside substantive proof development.
The complete fixed [C14 v2](../../claims/Yin_C_A0014_v2.md) was read directly and compared with v1.
No development discussion, exploration draft, author explanation or other agent's review conclusion was supplied or consulted.
The prior review's own reasoning is reused only for the unchanged v1 statements and arguments whose continuing applicability was confirmed in v2.
All added assertions and their affected interfaces were independently examined.

The source interfaces were reread in [Sim08](../literature/Sim08/Yin_U001.md#christoffel-variational-principle), [its moment-inverse formula](../literature/Sim08/Yin_U001.md#abc-moment-inverse) and [BCM04](../literature/BCM04/Yin_U001.md#amenable-projective-trace).
The review covers physical v2 read on 2026-11-12, including (1a)–(1c), the strengthened conclusion of (3), and (8a).
The preserved v1 review remains evidence for its actual v1 inputs; it is not treated as having already reviewed these additions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole v2 argument](#whole-argument) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole v2 argument](#whole-argument) | [Statement](../../claims/Yin_C_A0014_v2.md#statement) | Complete v2 hypotheses, definitions and conclusions, including (1a)–(1c), spectral exclusion under (3), and (8a). |
| [Whole v2 argument](#whole-argument) | [Argument](../../claims/Yin_C_A0014_v2.md#argument) | Complete proof, with fresh checks of bounded coefficient mass, all specified approximating families, norm divergence and spectral exclusion under (3); unchanged steps reuse the confirmed v1 checks. |
| [Whole v2 argument](#whole-argument) | [Scope](../../claims/Yin_C_A0014_v2.md#what-has-and-has-not-been-reduced) | Distinction between atom-only bounded mass and the spectral-gap consequence of (3), with all retained conditional and necessary scope limits. |

<a id="whole-argument"></a>
## Finding: whole v2 argument

**The complete v2 conclusions are supported at their stated scope.**
No mathematical gap was found in the additions, their interfaces or the retained argument.

### Bounded coefficient mass and its applications

Finite liminf in (1a) supplies one subsequence and a finite constant \(C\) bounding all its \(\ell^1\) norms.
Convergence in \(L^2(\tau)\) gives convergence of every Fourier coefficient, whose coordinate difference is bounded by the \(L^2\) difference.
For each finite \(E\subset G\), passage to the limit in a finite sum gives \(\sum_{g\in E}|p(g)|\le C\).
The same \(C\) works for every finite set, so taking the supremum proves that the Fourier coefficient function of \(p\) belongs to \(\ell^1(G)\).
This uses neither spatial tightness nor an interchange of a limit with an infinite sum.

The resulting regular operator agrees with \(p\) on \(\delta_e\).
Both operators commute with right translation, so they agree on every standard basis vector and hence everywhere.
The identified \(\ell^1\) element is therefore an idempotent.
BCM04 applies at the unchanged torsion-free amenable hypotheses, and \(p=1\) is excluded by \(a\ne0\), giving \(p=0\).

Equation (11) supplies \(L^2\) convergence for the first family in (1b).
Nonunique polynomial representatives in the finite-support case give the same represented operator under the faithful trace, so they do not affect its coefficient norm.
For the second family, the squared \(L^2\) error is
\[
\int_{(0,M]}(1-x/M)^{2n}\,d\mu(x)\longrightarrow0.
\]
Dominated convergence handles both endpoints and any atom at zero correctly.
Both families consist of group-ring elements, so their norms are finite sums without an unknown atom parameter.

For each fixed \(t\ge0\), the exponential series converges absolutely in \(\ell^1(G)\), with norm at most \(\exp(t\|H\|_{\ell^1})\).
Continuity of the regular representation identifies this series with the operator exponential.
Its squared \(L^2\) error is
\[
\int_{(0,M]}e^{-2tx}\,d\mu(x)\longrightarrow0.
\]
A finite liminf as \(t\to\infty\) supplies \(t_j\to\infty\) with bounded norms, so (1a) proves (1c).
For both discrete families and the continuous heat parameter, failure of divergence to \(+\infty\) yields exactly such a bounded subsequence.
This verifies the stated norm-growth obstruction when \(p\ne0\).

### Spectral exclusion under summable increments

The retained proof under (3) gives convergence of \(f_{2^j}(H)\) to \(p=0\) in \(\ell^1(G)\).
The regular operator norm is bounded by the coefficient \(\ell^1\) norm, so operator-norm convergence follows.
If \(0\in\sigma(H)\), polynomial functional calculus and \(f_{2^j}(0)=1\) give \(\|f_{2^j}(H)\|\ge1\) for every \(j\), a contradiction.
The strengthened conclusion therefore needs no additional decay assumption or source theorem.

Condition (3) supplies a bounded dyadic subsequence of the Christoffel approximants and hence implies the first criterion in (1b).
The reverse implication is not used.
The bounded-mass proof identifies an \(\ell^1\) coefficient limit without giving operator-norm convergence, so the revised scope correctly separates its atom argument from the spectral-gap argument.

### Retained polynomial estimates and complete-chain coverage

The direct comparison confirms that the original hypotheses, variational definition and identities, moment-inverse formula and finite-support argument are unchanged.
The rounding construction, polynomial filters and propagation estimates (5)–(7) are unchanged.
The power estimate (15), its spectral contradiction, the critical little-oh argument (8a), and the stretched exponential estimate (16) are also unchanged.
Their complete checks remain those in [the v1 finding](Yin_R_A0041_v1.md#whole-argument), including the interval crossing the cutoff in (8a) and the strict comparison in (10).
The added argument uses the already checked \(L^2\) convergence and idempotent interface without altering any of these hypotheses or estimates.
The new consequence of (3) agrees with the retained rate consequences.
These confirmed unchanged checks and the new checks above together cover the complete v2 statement, proof and scope.

## Source completeness and limits

The reread source units preserve the precise Sim08 conventions and BCM04 scalar-idempotent interface needed here.
The new steps are supplied by coefficient convergence, finite sums, the Banach-algebra exponential series and the stated functional calculus.
No additional unresolved external input is introduced.
Existing primary-source inspections are reused; the original PDFs and assembly-theoretic proofs were not independently re-audited in this review.

The conclusion remains conditional on the displayed boundedness or rate conditions.
No boundedness theorem for arbitrary torsion-free amenable group-ring elements, general injectivity theorem, optimal threshold, new group class or completion of A0001 is established.
No computation or proof-assistant formalization is claimed.
