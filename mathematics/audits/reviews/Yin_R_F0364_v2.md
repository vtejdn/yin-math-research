---
author: Yin
---

# Positive Hermitian differences of physical sign words

<a id="sign-chord-whole-proof"></a>
## Independent whole-proof finding

At 2026-11-17T13:34 an independent agent acting for Yin inspected the fixed [C356v2 proof](../../claims/Yin_C_F0356_v2.md#statement) and the directly used preceding theorem and original local law.
The reviewer took no part in the construction and received no development discussion, drafts, author explanations or prior v2 finding before its first conclusions.
The full proof is supported at every specified stable real energy.

For each fixed active set, assigning the positive subset with the binomial count and a uniform permutation gives each of its subsets exactly probability \(2^{-|R|}\).
The independently drawn inactive words then reconstruct exactly the initial product sign distribution.
The first count is deterministic when the two words exhaust the alphabet.
Otherwise the joint conditioning at typical counts costs at most a polynomial factor and leaves order \(N\) negative sites.
Removing all diagonals makes the reference spectral projection independent of every word; its resolvent comparison costs \(O(N^{-1/2})\) in operator perturbation.
The successive sign tests give uniform mass on the negative endpoint sites, and future flips sample uniformly there conditional only on the current state.
The net entropy is absorbed since \(N^{3/32}\) dominates \(N^{1/32}\log N\).
The inertia identity includes an endpoint zero and the expectation of the number of visits retains only the initial guard when averaging the endpoint shift.
The resulting probability is \(O(N^{-11/32}+N^{-3/8}\log^{3/2}N)\), sufficient for the stated floor.

The reviewer checked the Pauli covariance eigenvalues, the uniform ray stability in the open bulk and invertibility and indefiniteness of each of the three matrices.
The scalar continuants use the indicated two-input tridiagonal realization and its own normalization factor \(m\).
The almost-sure conclusion is dyadic and the full-size limsup holds under arbitrary coupling.
The review rechecked AEKN19 at Lemma B.1(i)'s stated interface without re-proving its original proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#sign-chord-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#sign-chord-whole-proof) | [Original sign model](../../claims/Yin_C_F0356_v2.md#statement) | Bound on the least value and ordinary log at a fixed stable energy. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Active sign words](../../claims/Yin_C_F0356_v2.md#argument) | Correct unconditional marginal and the two central counts. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Available negative endpoints](../../claims/Yin_C_F0356_v2.md#negative-sites) | Uniform sampling, leverage and control independent of the words. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Counting possible visits](../../claims/Yin_C_F0356_v2.md#crossings) | Monotonicity, inertia and the expectation under a typical active count. |
| [Whole-proof finding](#sign-chord-whole-proof) | [All-indefinite triple](../../claims/Yin_C_F0356_v2.md#examples) | Bulk stability, positive chord and the scope of the continuant application. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Local flow estimate](../../claims/Yin_C_F0356_v1.md#crossings) | The min-max and endpoint comparison. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Tridiagonal Schur transfer](../../claims/Yin_C_F0356_v1.md#examples) | The two-input scalar continuant realization. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Stable local law](../../audits/literature/AEKN19/Yin_U001.md#stable-block-law) | The physical diagonal-block bound at the two window scales. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Clipped determinant](../../claims/Yin_C_F0186_v40.md#band) | Use before translation regularity. |
| [Whole-proof finding](#sign-chord-whole-proof) | [Free target](../../claims/Yin_C_F0352_v1.md#statement) | Finiteness at full pencils. |
