---
author: Yin
---
# NS06-U004: semicircular mixed moments and normalized free compression

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Existing registered 434-page publisher-layout [NS06.pdf](../../../literature/pdf/NS06.pdf), with original artifact identity.

Passages: Equation (14.5), printed p.228/PDF p.245; Notation 14.7 and Remarks 14.8, printed p.229/PDF p.246; Theorem 14.10, printed p.230/PDF p.247, and its proof through printed p.231/PDF p.248.

Inspection: 2026-10-14T19:29, Yin: exact statements, normalizations and surrounding text read by pdftotext.
Statement and applicability accepted; the general combinatorial proof and all its dependencies were not independently re-audited.


<a id="ns06-u004"></a>
## Inspected mathematical input

For a standard semicircular family free from an algebra B, equation (14.5) expresses mixed moments of semicircular letters alternating with B coefficients as the sum over noncrossing pairings of those letters, with the B moments specified by the complementary partition.
Only equal-index semicircular letters may pair.
In particular, for a single standard S free from B, the conditional fourth-moment consequence is

\[
 E_B(SaSbScS)=\tau(a)\tau(c)b+\tau(b)\tau(ac)1
 \qquad(a,b,c\in B).
\]

This displayed conditional form follows by testing the source scalar formula against arbitrary B coefficients.
It is a direct specialization, not an additional general operator-valued theorem.

If a projection e has trace t>0 and is free from variables a_1,...,a_m, the normalized corner trace is tau_e=t^-1 tau.
Theorem 14.10 gives

\[
 \kappa_n^{eMe}(ea_{i_1}e,\ldots,ea_{i_n}e)
 =t^{n-1}\kappa_n(a_{i_1},\ldots,a_{i_n}).
\]

Thus eSe/sqrt(t) is standard semicircular in the normalized corner when S is standard semicircular and free from e.
The theorem does not by itself assert freeness of this compression from elements that are not free from e.

For an abelian N free from S and e in N, the joint normalized-corner moments with eNe coefficients can instead be checked from equation (14.5).
Insert e at every end and divide each S by sqrt(t); the noncrossing-pairing recursion becomes the same standard semicircular recursion with tau_e on eNe.
This proves that eSe/sqrt(t) and eNe have the standard free joint law.
This local adaptation explicitly uses the mixed-moment formula.
Corollary 14.12 is not invoked on eNe, since e is not free from its own subalgebra.

The source supplies established mixed-moment and compression formulas.
The consumer remains responsible for choosing the normalized trace and for every actual derivation or adjoint domain.
No result concerning liberation gradients or weighted quadratic-form bounds is imported from these passages.
No new PDF acquisition or whole-book audit is claimed.
