---
author: Yin
---
# Cyclic coset covers and regular rank: whole-argument review

On 2026-11-16T15:12 UTC a separate reviewing agent inspected the [fixed Claim](../../claims/Yin_C_A0019_v1.md) for Yin.
The reviewer neither developed this proof nor received its exploration notes, proof-generation discussion, author explanations or a previous verdict on it.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0019_v1.md#statement) | Projection estimate, quantitative gap, stabilizer bounds and two-factor consequence under the stated hypotheses. |
| [Whole-argument finding](#whole-argument-finding) | [Compression](../../claims/Yin_C_A0019_v1.md#compression-to-the-occupied-cosets) | Fiber dimension, leakage identity, and the one- and two-stabilizer bounds. |
| [Whole-argument finding](#whole-argument-finding) | [Stabilizer](../../claims/Yin_C_A0019_v1.md#the-stabilizer) | Cyclicity of the stabilizer in a torsion-free ambient group. |
| [Whole-argument finding](#whole-argument-finding) | [Circle estimate](../../claims/Yin_C_A0019_v1.md#a-coefficient-independent-estimate-on-the-circle) | All induction constants for distinct integer frequencies. |
| [Whole-argument finding](#whole-argument-finding) | [Trace bound](../../claims/Yin_C_A0019_v1.md#quantitative-trace-bound) | Conditional expectation, transfer to one right coset, and both ranges of the trace. |
| [Whole-argument finding](#whole-argument-finding) | [Consequences](../../claims/Yin_C_A0019_v1.md#consequences-for-group-ring-products) | Passage to rank, the support-size bound and the exclusion of two factors with two-coset covers. |

## Whole-argument finding

The support bounds hold for a projection fixing one nonzero finitely supported vector.
The right translates of the vector inside the occupied left cosets generate a subspace of trace dimension one over \(\mathcal N(H)\).
Indeed, the vector-valued polynomial in Fourier coordinates spans a line almost everywhere, and orthogonality to all polynomial multiples is equivalent to pointwise orthogonality to that line almost everywhere.
The compression fixes this submodule and is a positive contraction, so the trace of its square is at least one.
The trace defect is the sum of squared norms lost from the \(k\) representatives.
Since \(p\delta_{g_i}\) has coefficient \(\widehat p(u)\) at \(ug_i\), a coefficient occurs in that sum once for each occupied coset that \(u\) sends outside \(Y\).
The zero-count elements are precisely the setwise stabilizer.
This gives the asserted expectation estimate, forces \(p=1\) for \(k=1\), and counts every nonidentity coefficient at least once when the two stabilizers intersect trivially.
For the single trivial stabilizer, solving the resulting quadratic gives the stated positive root.

The permutation kernel is cyclic and of finite index.
If it is infinite, an element inverting it would have a power in it that is fixed and inverted by conjugation, hence that power must be trivial.
Torsion-freeness excludes such an element, so the kernel is central.
Summing the exponents in the finite permutation of its transversal gives an additive map to \(\mathbb Z\) that is nonzero on a generator of the kernel.
Every element has a power in the kernel, making this map injective by torsion-freeness.
The other case is a finite torsion-free stabilizer, which is trivial.

In the circle estimate the measure of bad translations is at most \(u/2\), and the overlap integral lost there is at most \(u^2/2\).
One can therefore retain overlap of at least \(u^2/2\) while keeping at least \(Mu\) of the chosen coefficient and killing a different frequency.
For an exponent \(E\) in the inductive bound, the factor after differencing is \((u/2)(u^2/4)^E=(u/2)^{2E+1}\).
The constant-modulus initial case thus gives \(E_d=2^{d-1}-1\); losing more than one frequency strengthens the bound.
No frequency-size or coefficient-ratio assumption enters this step.

After normalizing \(\|z\|_1=1\), right multiplication by \(z\) transfers the Fourier leakage bound to the error on \(z\) with operator norm at most one.
On the right coset containing a largest coefficient, the restricted polynomial has a coefficient of modulus at least \(1/s\).
The circle estimate with \(u=t\) gives modulus at least \(c\) outside a set of measure less than \(t\), even if that coset uses fewer than \(s\) frequencies.
When \(1-\delta\ge2t\), the good set carries at least \(t\) of the integral of \(1-b_L\), so its square integral there is at least \(t^2\) by Cauchy–Schwarz.
When \(1-\delta<2t\), \(k\delta-1>(k-1)/2\), which already exceeds \(c^2t^2\) for the stated constants.
Constant functions handle the trivial stabilizer with the same inequalities.

Taking the range projection for \(a\) is valid because it fixes \(a\delta_e\).
Pairing two support points in one left coset gives at most \(s-1\) occupied cosets, and when only one coset is occupied the rank is one.
For a zero product the two range ranks sum to at most one by polar equivalence; this is incompatible with two ranks strictly greater than one half.
The result does not exclude zero products with unrestricted supports or prove the general Atiyah contract.
The application to amenable groups uses the [previous finite descent](../../claims/Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) at its stated scope; this review does not re-audit that theorem.
