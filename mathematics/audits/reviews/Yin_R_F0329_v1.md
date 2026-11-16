---
author: Yin
---

# Independent review of the reduction to product two-marginal traces

## Finding

On 2026-11-16T17:33 UTC a reviewer outside proof development independently examined the [candidate decision](../../claims/Yin_C_F0321_v1.md#decision-candidate) dated 2026-11-16T17:31.
The reviewer received the fixed claim and the requested scope without proof-development dialogue or a prior finding on this candidate.
The proof gives the stated transfer for each finite witness and both comparisons of suprema in (2).

The entries of \(2U\) are commuting selfadjoint unitaries, and any two distinct rows, or columns, have zero inner product.
Thus \(U\) is unitary and the two off-diagonal entries of \(s_0^2\) vanish by cancellation.
The diagonal entries of \(s_0^2\) equal one, and the trace of \(s_0\) is zero.
In computing \(\tau(f(W)s_0g(W)s_0)\), each of the four block terms carries the factor \(1/4\) from the outer trace and the two occurrences of \(s_0\).
The diagonal terms factor by freeness of \(D\) from \(A\), also after conjugating \(D\) by the unitary \(U\in A\).
Within an off-diagonal term each pair of internal slots has weight \(1/16\).
By cyclicity its trace pairs a bottom-slot spectral function with a conjugate of the top-slot function by \(1,-1,J\) or \(-J\).
Each bottom slot contains its own semicircular, free from the algebra of that conjugate, including when the top slot contains the original correlated \(Z,J\).
The two off-diagonal terms therefore give the cross products of the two half-traces.
The four products sum with the stated weights to the product of the full traces for bounded Borel tests.
The centered diagonal symmetries give \(\tau(f(W)s_0)=0\), and the sign change at \(D\) followed by the outer diagonal conjugation fixes \(W\) and negates \(s_0\).

At a matrix pivot each lift preserves the Leibniz rule and multiplies its vacuum by the normalized trace of that pivot before insertion in the diagonal entry.
Here the inner and outer pivots have traces \(1/4\) and \(1/2\), and the intervening free extension by zero preserves the vacuum.
The final vector is \(t e_i\xi_i\), of Hilbert norm \(t^{3/2}\|\xi_i\|_2\) with \(t=1/8\).
All eight lifts kill the symmetry entries, and the orthogonal padding vacua contribute at most \(t^{3/2}\sqrt7\).
The separated-spectrum kernel supplies the cross terms missing from \(LW\), with vacuum norm at most two and norm at most two for the resulting derivative of \(s_0\).
Inserting its negative divided by \(\epsilon\) in the free semicircular derivative kills \(T\) at vacuum cost at most \(2/\epsilon\).
The spectral gap gives both graph approximation to the sign with derivative zero and norm convergence \(s\to s_0\).
The diffuse normal phase and the zero sign derivative take values in the intrinsic coarse space, so Hilbert projection gives the claimed actual vacuum after restriction.

To check the exact equality after smoothing, put \(B_0=\operatorname{span}\{1,s_0\}\).
Reduced words give \(\mathbb E_{\mathcal M}s\in B_0\), and the grading forces this expectation to equal \(c s_0\) for a real \(c\).
For \(d=s-cs_0\) one gets \(\mathbb E_{\mathcal M}d^2=1-c^2\).
The identity \(\tau(g(W)s_0)=0\) puts \(g(W)-\tau(g(W))\) in the kernel of \(\mathbb E_{B_0}\).
Whenever such an element separates two words from \(W^*(B_0,S)\) centered over \(B_0\), adjacent end coefficients from \(B_0\) preserve its zero conditional mean.
The noise-containing reduced product then has zero expectation onto \(\mathcal M\), and separate normality extends the identity to \(d\) on both sides.
Expanding \(s g(W)s\) leaves exactly the convex combination with coefficients \(c^2\) and \(1-c^2\) stated in the proof.
Pairing with \(f(W)\) gives equal product traces for both terms, with no approximation error in (1).

The cycle \(1,5,2,6,1\) uses the entries \(1,1,J,1\) of the cross blocks after removing their common \(1/\sqrt8\).
Its product times \(64\) is already selfadjoint at \(s_0\).
The approximating selfadjoint coefficient therefore tends to \(e_1J\) in ambient operator norm as \(\epsilon\) tends to zero.
The inner cut at \(e_1\) kills both \(s\) and the derivatives of all slot projections, since each slot indicator is constant on the first spectral piece.
Norm and coarse-graph approximation of the slots applies because their real spectra are separated.
For the fixed test word, scaling the corner derivative by \(\alpha\) leaves exactly the old two generator tensors at \(e_1Z\) and its adjoint.
The normalized corner trace agrees with the old trace there, giving convergence of the right slice with the test norm, independently of \(\alpha\).

Fixing \(\epsilon\) first makes that test cost at least \(b-\eta\) with input norm at most \(1+\eta\).
The traced product rule gives the factor \(2\) in the direct comparison, with \(t^{3/2}\) on the normalized corner side.
Multiplication of (4) by \(\alpha\) then leaves \(t^{3/2}\|\xi\|_2\) in the limit \(\alpha\downarrow0\), canceling the corner factor.
The positive vacuum norms follow by testing the unit derivative on the distinguished generator.
The sign grading gives the fully actual even pair, its exact exchange involution, unchanged vacuum norm and the remaining factor \(\sqrt2\) by orthogonality of the two slice components.
The argument also covers an infinite intermediate cost by selecting a sufficiently large finite polynomial witness.
The reverse comparison retains each first-coordinate test in the crossed-product realization.
The pointwise marginal output estimate for exchange pairs continues to hold on this subclass, proving the second comparison and, with the projection criterion, the stated finiteness equivalence.
The review checked all five direct inputs at their specified interfaces.
The product condition specifies ordered two-marginal traces, and the existence of one such pair of infinite cost remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0321_v1.md#decision-candidate) | Whole proposed decision and five declared inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0321_v1.md#statement) | Exact Borel product traces, first-coordinate and mixed suprema, finite-witness loss, uniform equivalence and limitation to that scope. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0321_v1.md#argument) | Initial matrix symmetry, trace factorization, nested lifts, sign correction, conditional expectation, cycle reconstruction, parameter order and even-algebra transfer. |
| [Finding](#finding) | [Projection reduction](../../claims/Yin_C_F0308_v1.md#argument) | Graph approximation of cuts, direct corner slice bound, trace normalization and universal projection criterion. |
| [Finding](#finding) | [Matrix lifts and free noise](../../claims/Yin_C_F0306_v1.md#argument) | Both pivot-vacuum factors, intervening free extension, off-diagonal kernel and inserted noise vacuum. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Actual scalar restriction, diffuse marginal and uniqueness of the adjoint-generator tensor in the complete coarse space. |
| [Finding](#finding) | [Conditional trace after smoothing](../../claims/Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Centered reduced-word conditional expectation with base algebra \(\operatorname{span}\{1,s_0\}\). |
| [Finding](#finding) | [Exchange and projected slice](../../claims/Yin_C_F0311_v1.md#argument) | Even-pair actuality and both vacuum norms, \(\sqrt2\) comparison, crossed-product converse and pointwise marginal bound. |
