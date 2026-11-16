---
author: Yin
---

# Independent review of the finite-dimensional lattice liberation criterion

## Finding

On 2026-11-16T19:26 UTC the reviewer independently examined the [candidate fixed at 19:24 UTC](../../claims/Yin_C_F0343_v1.md#decision-candidate), its complete statement and argument, and its declared finite-label interface.
The reviewer had worked on a separate estimate for the Cauchy slice in the lattice setting and had considered innerness as a possible constraint on matrix models.
The reviewer did not participate in developing this classification or receive its proof-generation discussion, author explanations or a prior finding on it.
The proof establishes the exact block criterion for arbitrary central trace weights and the trace-half conclusion.

The represented algebraic word algebra is a linear subspace of a finite-dimensional algebra and hence already closed.
Thus each putative derivation is defined on all of \(N\) and is continuous into the finite-dimensional coarse space.
Averaging \(u^*\cdot\gamma(u)\) on the compact unitary group and applying right Haar invariance to \(u\mapsto uv\) gives
\(v\cdot K=\gamma(v)+K\cdot v\).
The span of the unitaries is all of \(N\), fixing the sign and both outer actions in the inner implementation.
In particular no independent adjoint-domain condition survives once the derivation exists.

In \(N\otimes N^{\rm op}\) outer right multiplication \(b\otimes c\mapsto b\otimes cx\) becomes left multiplication by \(1\otimes x^{\rm op}\).
The constraint at \(D\) is therefore that \(1-K\) has left support under the equal-label projection; the constraint at \(P\) requires \(K\) to have left support under the equal-\(P\)-eigenvalue projection.
In a finite matrix summand the elements in either right ideal are exactly matrices whose columns belong to the corresponding vector range.
Their sum contains the identity if and only if these two ranges span the whole carrier, including when the projections do not commute.
If this holds on all summands, decomposing the unit gives an inner implementer which obeys the original assignments on the represented generators.
This verifies sufficiency in addition to necessity.

On \(\operatorname{Hom}(\mathbb C^{d_\beta},\mathbb C^{d_\alpha})\) the equal-label range consists of the independent blocks from \(e_{i\beta}\) to \(e_{i\alpha}\), giving dimension \(\sum_i r_{i\alpha}r_{i\beta}\).
For the other range the corresponding dimension is \(q_\alpha q_\beta+(d_\alpha-q_\alpha)(d_\beta-q_\beta)\).
An operator in both intertwines the complete generated algebra.
For \(\alpha\ne\beta\) the central projection of the first summand forces the intertwiner to vanish; even two summands of identical matrix size remain inequivalent.
For \(\alpha=\beta\) only scalar intertwiners remain.
Subtracting the intersection dimension from the sum of the two ranks and equating it to \(d_\alpha d_\beta\) gives exactly (1).
Its diagonal form has odd right side, hence \(d_\alpha=\sum_i r_{i\alpha}\equiv\sum_i r_{i\alpha}^2\equiv1\bmod 2\).

Weighting (1) by the two normalized block traces gives the extra strictly positive term \(\sum_\alpha w_\alpha^2/d_\alpha^2\) precisely from equal summands.
At trace one half this forces \(\sum_i t_i^2>1/2\) and then \(\max_i t_i>1/2\).
For a maximizing label both meets with \(P\) and \(1-P\) are nonzero by \(\tau(e\wedge f)\ge\tau(e)+\tau(f)-1\).
Each meet commutes with all generators, and its compressed algebra consists of scalars, so each is a single one-dimensional central summand.
They have the same label and opposite projection values.
If another summand \(\beta\) existed, pairing it with the two different characters would give \(r_{i_0\beta}=q_\beta=d_\beta-q_\beta\), which contradicts oddness.
Thus the identified label is the unit.
Conversely when \(D=\mathbb C1\) the zero derivation satisfies every prescription, including its vacuum.
The [lattice statement](../../claims/Yin_C_F0339_v1.md#statement) uses exactly this trace and represented generator algebra and allows \(N\) to be infinite dimensional.
The exclusion therefore applies to the proposed finite-dimensional realization and leaves open the general lattice bound.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0343_v1.md#decision-candidate) | Complete fixed candidate and its single declared external Claim interface. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0343_v1.md#statement) | All ordered-rank conditions, automatic vacuum, parity and exact trace-half classification. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0343_v1.md#argument) | Inner implementation, right ideals, simple carriers, central weighting and two forced one-dimensional summands. |
| [Finding](#finding) | [Lattice model](../../claims/Yin_C_F0339_v1.md#statement) | Prescribed liberation on the represented partition and projection algebra with the faithful normalized trace. |
