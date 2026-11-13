---
author: Yin
---
# Independent review of the two-coordinate relative commutant and the obstruction to mixed laws

## Whole-proof finding

Review performed at 2026-11-13T10:10 by a separately assigned agent outside proof development.
The reviewer read the fixed claim, the F0011 hypotheses and the four direct inputs, without development dialogue, additional author explanations or earlier review findings on the candidate.

Under the ACSY hypothesis, both the multiplier and its adjoint preserve the algebraic graph for each left or right action from the other coordinate's polynomial star algebra.
Boundedness of those actions passes invariance to the closed graph, and normality of their representations extends commutation of its projection to the generated von Neumann algebra.
Equal-trace partitions make the diagonal coarse projections converge strongly to zero on bounded simple tensors and then on the full coarse space, forcing the second component of the projected central vector to vanish.
Orthogonality to the graph forces the remaining first-coordinate error to vanish against the dense core.
For a graph-core approximation \(p_n\to a\), multiplication of either \(p_n-a\) or \(\delta_i p_n\) by the fixed bounded \(X_i\) is continuous in the relevant Hilbert norm.
Thus \([p_n,X_i]\to0\) while its derivative tends to \(a\otimes 1-1\otimes a\), and closability followed by vacuum contraction gives \(a=\tau(a)1\).
This reasoning uses neither reality of the derivation nor uniform operator-norm control of these core approximants.

For bare duals, the normalized normal representative satisfies \(E_i1=0\), so the generator-first witness \(-E_i\) normalizes back to \(E_i\) and the polynomial commutator formula holds on all bounded inputs.
A nonzero Hilbert--Schmidt operator commuting with the Haar unitary would give a nonzero finite-dimensional spectral subspace of its squared absolute value invariant under that unitary and its inverse.
An eigenvector there would contradict the diffuse spectral measure in the faithful left representation.
The Hilbert-space mean ergodic argument therefore makes the conjugation averages of each polynomial commutator small in Hilbert--Schmidt norm.
Left \(W^*(X_j)\)-linearity identifies these averages on \(M\) with the commutators of the averaged approximants.
Kaplansky density permits a single uniformly bounded sequence approximating the specified \(a\) in \(L^2\) by testing the strong approximation on \(\Omega\).
Averaging preserves this error bound since \(a\) commutes with the averaging unitary.
For \(w\in M\), \(\|(r_n-a)w\|_2\le\|w\|_M\|r_n-a\|_2\), and uniform boundedness extends strong convergence to every vector in \(H\), including \(E_i(v)\).
Bounded strong convergence gives ultraweak convergence, and multiplication by fixed \(v\in M\) preserves that convergence.
Normality of \(E_i\) thus identifies the weak limit of \(E_i(r_nv)\), while the commutator error tends to zero in norm.
The two product expansions against \(X_i\) now give \(aP_\Omega=P_\Omega L_a\) on \(M\), yielding scalarity at \(1\).

A nontrivial trace decomposition on the common cutoff algebra gives each component a bound by the mixed trace on positive elements, allowing its linear functional to descend through the GNS kernel and extend continuously in \(L^2\).
Traciality makes each representing vector commute with the polynomial algebra, and bounded strong-star approximation extends the equality to the generated algebra.
In a factor the spectral projections of the absolute value and the polar partial isometry of each central affiliated vector are scalar, so normalization identifies both component traces with the mixed trace.
Distinct joint laws must differ on the norm-dense polynomial algebra even when every one-coordinate marginal agrees.
Both branches prove the asserted relative commutant in the full generated algebra for every distinct pair.

The fixed statement and complete argument pass at the stated hypotheses.
The three project results were checked at their invoked interfaces and Kaplansky density at the statement and applicability depth recorded in AP18-U001.
The [cited selfadjoint comparison](https://arxiv.org/html/0804.2906v2) supplies historical context in Section 1, particularly Remark 3.
This review covers neither an implication between the two hypotheses nor a non-Gamma assertion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0202_v1.md#statement) | Every distinct pair under either hypothesis, factoriality and the obstruction to mixtures of distinct joint laws. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0202_v1.md#argument) | Graph-domain argument, averaged compact commutators, pointwise passage to the limit and extremality of factorial traces. |
| [Whole-proof finding](#whole-proof-finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 supplies diffuse marginals, closability and the other starred coordinate's zero derivative. |
| [Whole-proof finding](#whole-proof-finding) | [Normal representative](../../claims/Yin_C_F0132_v1.md#statement) | Part A gives the normalized normal representative and its omitted-coordinate module identity on bounded inputs. |
| [Whole-proof finding](#whole-proof-finding) | [Starred commutators](../../claims/Yin_C_F0070_v1.md#statement) | Part A gives diffuse marginals and polynomial Hilbert--Schmidt commutators on all bounded inputs for this representative. |
| [Whole-proof finding](#whole-proof-finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | The generated star algebra gives uniformly bounded approximants at the single vacuum vector. |
