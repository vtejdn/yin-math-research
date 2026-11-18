---
author: Yin
---

# Disk maxima and Taylor minors of the cyclic Wigner determinant

<a id="disk-minors-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-18T10:57 UTC an agent acting for Yin independently checked the full [disk criterion and its deterministic sufficient condition](../../claims/Yin_C_F0359_v3.md#statement).
The reviewer received the fixed Claim without proof-development discussion or an earlier verdict on this version.
The [earlier independent review](Yin_R_F0367_v2.md#local-cutoff-whole-proof) applies to the preceding version, whose uniform clipped convergence, chart identity and pathwise potential criterion are used here at their proved scopes.

For a fixed polynomial and laws, countability yields one event of full probability in the given coupling on which the clip converges uniformly on each chart and the lower bound holds eventually for each fixed disk and rational tolerance.
For a maximizer \(s\) on a covering disk \(D_j\), the submean inequality controls the mean of \(U_N\) from below on \(B(s,2r)\).
Every point there has distance at most \(4r\) from every point of \(D_j\), so the mean loss \(V_N-U_N\) on the larger disk is at most \(2\epsilon+\omega_u(4r)\).
Positivity of the loss permits restriction to \(D_j\), and the total area of the larger disks is bounded independently of small rational \(r\).
Uniform clipped convergence now gives local \(L^1\) convergence.
The chart Jacobian and trace normalization transfer this conclusion to the scalar potentials on every compact set, and applying \((2\pi)^{-1}\Delta\) gives vague convergence to the Brown measure of total mass one.
Conversely, the pathwise potential criterion applies under independent sizes, where every failed test costs at least \(\epsilon|D|\) in local \(L^1\).
Independence forces summability of those marginal probabilities.
Parseval and the Taylor bound differ by at most \(\log(n+1)/(2n)\) after normalization, so using a smaller rational tolerance gives the same series criterion in both directions.

The SVD reduces the Taylor coefficient of order \(k\) to a sum of principal minors with a common unimodular factor, including at singular centers.
For all sufficiently large \(N\), \(q<n=mN\), so a value at least \(c=N^{-B}\) precedes the subcutoff values whenever they occur.
Before the first ratio below \(h=\delta/(4nq)\), each retained subcutoff value is at least \(ch^q\).
At a gap every exchange of \(\ell\) bottom indices in the leading term costs a factor at most \(h^\ell\) in the complementary product.
The sum of the competing magnitudes, divided by the positive leading product, is at most \(e^{knh}-1\le e^{\delta/4}-1\le\delta/2\) for \(0<\delta\le1\).
The prescribed minor therefore survives cancellation.
If there is no gap the product at the center already suffices, and if there is an exact zero the first drop to zero or an earlier gap has a positive complementary product.
Restoring the retained logarithms and using the radius-\(r\) Taylor bound costs \(O(q^3\log N+q|\log r|+1)=o(n)\) for the stated \(q\) and fixed \(m,r,C\).

The equivalence and deterministic estimate hold at their stated scopes.
Summability for the full Wigner contract still requires a probability bound for the disk failures.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#disk-minors-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#disk-minors-whole-proof) | [Disk statement](../../claims/Yin_C_F0359_v3.md#statement) | Every-coupling equivalence for each fixed nonconstant polynomial and finite-variance model, with countably many disks and tolerances. |
| [Whole-proof finding](#disk-minors-whole-proof) | [Disk argument](../../claims/Yin_C_F0359_v3.md#argument) | Cover, submean inequality, chart transfer, independent-size necessity and Taylor norm equivalence. |
| [Whole-proof finding](#disk-minors-whole-proof) | [Bottom singular spaces](../../claims/Yin_C_F0359_v3.md#minors) | Principal-minor expansion and deterministic gap estimate, including exact zeros. |
| [Whole-proof finding](#disk-minors-whole-proof) | [Polynomial cutoff theorem](../../claims/Yin_C_F0359_v2.md#statement) | Applicability of its proved compact-chart conclusions for each fixed cutoff exponent and model. |
| [Whole-proof finding](#disk-minors-whole-proof) | [Chart identity](../../claims/Yin_C_F0359_v2.md#chart) | Bounded Jacobian and the finite and free trace factors. |
| [Whole-proof finding](#disk-minors-whole-proof) | [Clipped potentials](../../claims/Yin_C_F0359_v2.md#clip) | Uniform complete convergence at rational tolerances on each chart. |
| [Whole-proof finding](#disk-minors-whole-proof) | [Potential criterion](../../claims/Yin_C_F0359_v2.md#equivalence) | Pathwise local potential convergence under weak convergence for the contracted laws. |
