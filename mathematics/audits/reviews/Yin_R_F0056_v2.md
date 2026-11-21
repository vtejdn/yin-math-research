---
author: Yin
---

# Review of the one-sided product variant of Yin_C_F0012

Date: 2026-11-21T13:51, UTC.
Human record author: Yin.
Arrangement: the agent that developed the variant performed this self-review after writing its complete proof.
The development discussion, existing sandwich proof and prior review descriptions were available.
This is not an independent inspection, and the independently reviewed v1 statement does not confer that relationship on v2.

## Inputs

- [Yin_C_F0012 v2 statement and proof](../../claims/Yin_C_F0012_v2.md#statement): the exact pair \((h,bh)\), its unstarred polynomial algebra, the explicit bounded duals and the matrix rational closure separation.
- [v1 standard tracial model](../../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model): the tensor realization, the free semicircular variable and bounded right multiplication.
- [v1 scalar dual](../../claims/Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction): the Hilbert-transform normalization, boundedness estimate and last-factor lift.
  The accepted finite-interval Hilbert-transform bound is reused; its external source proof was not re-audited in this review.

<a id="one-sided-finding"></a>
## Finding

The exact v2 statement and proof have no unresolved gap in this self-review.
The following mathematical interfaces were rechecked.

The inverse vector \(q\) has squared norm two.
The last-factor functional in \(R_q\) is bounded and lowers orthogonal grades, so its norm stays uniformly \(\sqrt2\) on the full Hilbert direct sum.
Commutation with first-factor \(h\) includes grade one, where that factor is retained.
The only nonzero contribution to \([R_q,\ell]\) is on grade zero, and both orders in \([R_q,\ell^*]\) vanish on grades zero and one.
On all higher grades the contractions are on different factors.
This gives the actual whole-space rank-one operator \([R_q,b]=|\Omega\rangle\langle q|\).
Multiplication on the right by bounded \(h\) changes its input vector to \(hq=\Omega\).
No unbounded multiplier is used to define a dual.

For \(T\), the generator-first sign is the negative of the v1 scalar dual.
The last-factor lift commutes with left \(b\), including the grade-one contraction into grade zero.
The correction \(\rho(b)R_q\) cancels \([bh,T]=bP_\Omega\), since \([bh,R_q]=-P_\Omega\) and \(\rho(b)P_\Omega=bP_\Omega\).
The four equations and both stated norm bounds follow.
The same computation verifies the two rank-one commutators with the witness \(b\).

The bounded cutoff products \(Yh^{-1}1_{[\varepsilon,1]}(h)=b1_{[\varepsilon,1]}(h)\) converge strongly to \(b\), proving generation of the specified \(M\).
The affiliated identity \(Yh^{-1}=b\) uses the zero kernel of \(h\) and is valid in \(L^0(M)\).

For nonmembership, every nonempty word kills the normalized small-spectral vectors asymptotically because its rightmost letter does.
The set \(\mathcal B\) of operators acting asymptotically by a scalar is a unital algebra, with unique scalar evaluation.
For a matrix over \(\mathcal B\) having bounded inverse, a kernel vector of its scalar evaluation would violate the bounded inverse lower bound.
The displayed inverse identity then proves that every inverse entry is again in \(\mathcal B\).
This argument applies to all sizes and iterations, not just to scalar inversions or the displayed affiliated formula.
Finally freeness gives zero mean and norm one for \(b\xi_\varepsilon\), so the distance from \(b\) to \(\mathcal B\), hence to the bounded matrix rational closure, is at least one.

The nonnormality check uses \(E_{W^*(h)}(Y^*Y)=h^2\) and \(E_{W^*(h)}(YY^*)=\tau(h^2)1\).
The additional adjoint generator would not kill these vectors: its squared norm there is \(\tau(h^2)=2/3\).
Thus neither normal generators, exclusion from the generated C*-algebra, nor a result for the generated polynomial *-algebra is claimed.
The existing selfadjoint v1 result retains its distinct scope and evidence.

## Review relationships

| Review | Relationship |
| --- | --- |
| [One-sided finding](#one-sided-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [One-sided finding](#one-sided-finding) | [v2 statement](../../claims/Yin_C_F0012_v2.md#statement) | All hypotheses and conclusions, explicitly limited to the unstarred polynomial algebra of a nonnormal pair. |
| [One-sided finding](#one-sided-finding) | [v2 proof](../../claims/Yin_C_F0012_v2.md#argument) | All boundedness, commutator, generation, rational membership and matrix nonmembership steps. |
| [One-sided finding](#one-sided-finding) | [v1 model](../../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | Applicability of the standard tracial model and its bounded right action to this pair. |
| [One-sided finding](#one-sided-finding) | [v1 scalar dual](../../claims/Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction) | The scalar Hilbert-transform estimate and the signs and boundary grades of its lift; no new primary-source audit. |
