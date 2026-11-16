---
author: Yin
---

# Review of the cubic singular-mass bound and its least-squares criterion

## Finding

At 2026-11-16T15:08 UTC an agent outside proof development independently checked the complete [candidate dated 2026-11-16T15:02](../../claims/Yin_C_F0294_v1.md#decision-candidate) and its six declared dependency interfaces.
The reviewer received the fixed candidate and scope without substantive development dialogue, exploration notes, author explanations or previous findings about this candidate.
The cubic estimate holds for the original slice even for a pair, and the residual series characterizes divergence of the cubic integral regardless of whether that slice is bounded.

For finite \(a\), the slice has the ultraweak-to-weak continuity and two positive densities asserted in the single-input theorem.
The product rule on the core gives the trace term for \(Z\) and zero commutator for omitted polynomials; multiplication by a fixed element of \(M\) on \(L^2\) is bounded, and testing \(bE(x)\) against a fixed \(L^2\) vector gives a normal functional of \(b\).
This justifies extension in each variable.
For the open spectral tail \(l\) of \(h+k\), polar decomposition gives \(\tau(\operatorname{supp}|lT|)\le\tau(l)\).
Removing the two bad projections from the right cutoff by taking meets therefore costs at most \(2\tau(l)\), without any commutation assumption.
The surviving \(p\) satisfies \(lTp=0\) as well as \(lp=0\).
Thus \(Tp\) has both supports in \(1-l\), where the compressed forms of \(h,k\) are bounded by \(K\); each density term for \(Tp\) is bounded by \(K\|Tp\|_2^2\).
The unitary polar decomposition identifies the left cutoff \(f\) with a conjugate of the right cutoff, so that \(\tau(f)=s\) and \(\|T^*f\|_2\le r\sqrt{s}\) even for a nonnormal shift.
The pairing with \(f\) then gives \(s^2/r^2\le32a^2u^*(s/4)\), with \(u=h+k\).
Taking a shift with \(s>t\) and then radii descending to \(q(t)\) preserves this bound with \(t\) in place of \(s\).
The uniform square-mass bound implies \(q(t)>0\), while the zero shift gives \(q(t)\le\|Z\|\).
The level set in the layer integral is a half-line up to its endpoint, so the factor from integration is \(3/2\); after \(v=t/4\) the factor is \(192\), multiplied by a rearrangement integral at most \(\tau(u)\le2\).
The bare-dual theorem bounds this very slice on the represented starred core; restricting a strong dual gives a bare dual.

In the residual calculation the linear term is \(-2\operatorname{Re}\tau(b^*C_e)\); the strictly positive weight acts on the right of \(b\).
Completing the square yields \(b(W_e+\eta1)=C_e\), with a bounded solution even when \(W_e\) has a kernel.
Taking \(\eta\downarrow0\) and testing each fixed \(b\) gives the unpenalized infimum without a compactness assumption.
At fixed \(b\), continuity follows from \(\lvert\tau((e-e')|Z-b|^2)\rvert\le\|e-e'\|_2\||Z-b|^2\|_2\).
The countable family therefore yields the full projection-layer infimum upon interchanging the two infima.
In the Gram matrix calculation, a null linear combination of the \(w_ae\) pairs to zero with \(Ze\), so the pseudoinverse gives the actual finite-dimensional squared distance.
Kaplansky approximation in the trace representation evaluates strongly on the vector \(e\), giving precisely the required approximation of \(be\); the source's selfadjoint version on real and imaginary parts also supplies bounded strong-star approximation.

For \(r<q(t/2)\), a trace-\(t\) test projection has trace overlap at least \(t/2\) with the complement of every right cutoff, without needing the projections to commute.
For \(r>q(t)\), some right cutoff has trace greater than \(t\); diffuseness of the generated algebra allows a trace-\(t\) subprojection.
These comparisons give \(tq(t/2)^2/2\le d_n\le tq(t)^2\), and exclude zero residual at any fixed dyadic level.
Integration of \(s^2\) from \(t/2\) to \(t\) gives \(7t^3/24\); the lower-endpoint quantile thus gives the upper integral bound \(7B_{n+1}/3\).
The factor in the residual upper comparison is \(2(t/(t/2))^3=16\).
The interval above \(1/2\) has finite contribution by positivity of \(q(1/2)\).
These arguments for the divergence equivalence require the uniform singular-law theorem but never the finiteness of \(a\).

The dependencies were checked at their stated uses, without re-auditing their proofs or the original source behind the Kaplansky unit.
No mathematical repair was identified.
No tuple with divergent integral and no converse from finite integral to finite slice norm were established.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0294_v1.md#decision-candidate) | Whole fixed candidate dated 2026-11-16T15:02 and its six direct interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0294_v1.md#statement) | Cubic integral bound, original bare and strong dual obstruction, positive residuals and divergence criterion. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0294_v1.md#argument) | Two-sided support trimming, trace pairing, quantile integration, least squares, Gram approximation and dyadic comparisons. |
| [Finding](#finding) | [Single-input theorem](../../claims/Yin_C_F0276_v1.md#statement) | Normal extension of the original bounded slice and two normal densities of mass at most one. |
| [Finding](#finding) | [Omitted module action](../../claims/Yin_C_F0276_v1.md#averaging-over-the-omitted-algebra) | Vanishing of the omitted starred generator derivatives and extension of the left module identity. |
| [Finding](#finding) | [Shifted singular laws](../../claims/Yin_C_F0229_v1.md#statement) | Equal right and left cutoff traces by unitary polar decomposition and uniform square-mass bound for arbitrary omitted shifts. |
| [Finding](#finding) | [Bare normal duals](../../claims/Yin_C_F0070_v1.md#statement) | Uniqueness of the starred-core derivation and boundedness of its original contraction from bare duality. |
| [Finding](#finding) | [Polynomial congruence cuts](../../claims/Yin_C_F0288_v1.md#statement) | Countable density in the trace Hilbert metric on each prescribed trace layer. |
| [Finding](#finding) | [Projection layers](../../claims/Yin_C_F0282_v1.md#a-bounded-patch-in-a-fixed-trace-layer) | Trace dimension inequality and subprojections of prescribed trace in diffuse corners. |
| [Finding](#finding) | [Diffuseness in this application](../../claims/Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Actual normal tuples with at least two coordinates generate a diffuse algebra. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong approximation on the trace vector for a cut and selfadjoint approximation for the starred version. |
| [Finding](#finding) | [Task hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual starred conjugate variables on the represented algebra and strong-to-bare implication by restriction. |
