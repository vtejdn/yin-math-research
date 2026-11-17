---
author: Yin
---

# Free-subgroup kernels, bounded rationality and exponential Fourier tails

A separate reviewing agent inspected fixed C_A0058_v1 for Yin on 2026-11-17T02:19 UTC.
The reviewer received the fixed mathematical text and its direct references, did not develop its argument and received no C_A0058 development dialogue, author explanation or earlier verdict.
The inspection covers the free-subgroup statement, the nonclosed-range example and the matrix-specific sufficient condition on general groups.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0058_v1.md#statement) | Finitely generated free subgroup, arbitrary finitely generated ambient group, subgroup trace, all spatial moments and conditional general extension. |
| [Whole-argument finding](#whole-argument-finding) | [Rectangular projection](../../claims/Yin_C_A0058_v1.md#argument) | Division-ring kernel basis, proper matrix involution, bounded projection, unnormalized trace and bounded-intersection theorem. |
| [Whole-argument finding](#whole-argument-finding) | [Exponential tails](../../claims/Yin_C_A0058_v1.md#bounded-rational-inverses-have-exponential-tails) | Matrix Neumann approximation, propagation radius, squared Fourier tail, finite entrywise exponent, coset inclusion and change of length. |
| [Whole-argument finding](#whole-argument-finding) | [Nonclosed range](../../claims/Yin_C_A0058_v1.md#a-nonclosed-range-example-on-the-four-line-groups) | Infinite-order factor, exact graph kernel and exclusion of common cyclic Fourier support. |
| [Whole-argument finding](#whole-argument-finding) | [Inner inverse](../../claims/Yin_C_A0058_v1.md#an-affiliated-inner-inverse-on-a-larger-group) | Conversion of an affiliated idempotent to its orthogonal range projection, membership in the bounded rational closure and conditional integrality. |
| [Whole-argument finding](#whole-argument-finding) | [Finite-generator source interface](../literature/Lin00/Yin_U004.md#the-bounded-input-supplied-by-dr97) | Bounded and affiliated closures at the scope required here, without an infinite-generator assumption. |
| [Whole-argument finding](#whole-argument-finding) | [Matrix rational closure](../literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) | Realization as entries of inverses invertible in the indicated ambient algebra. |
| [Whole-argument finding](#whole-argument-finding) | [Spatial criterion](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Dyadic shell sum with factor \(2^{3j/2}\) and the polynomial moment of order \(3+\delta\). |
| [Whole-argument finding](#whole-argument-finding) | [C57 row construction](../../claims/Yin_C_A0057_v1.md#nonclosed-range-with-exponential-decay-after-canceling-an-injective-factor) | Nonclosed range after an injective factor and the bounded graph-projection calculation. |

## Whole-argument finding

The definition of the bounded rational closure and the intersection assertion were inspected in [Linnell, Theorem 1.1, English p. 3](../../literature/pdf/Lin00--arxiv-v1.pdf#page=3).

In the English statement on p. 3, Linnell fixes a free group, recalls from his earlier result that \(D(H)\) is a division ring, defines \(S(H)\) to be the rational closure of \(\mathbb CH\) in \(C_r^*(H)\), and gives \(D(H)\cap W(H)=S(H)\) in Theorem 1.1.
The finite basis in C_A0058 is within the finite-alphabet bounded theorem recorded in the direct source interface.
The proof only applies the intersection identity on \(H\).
For the trivial subgroup the matrix, kernel projection and Fourier assertion are constant directly.

For an \(m\)-column matrix with right nullity \(d>0\), division-ring elimination places its \(m\times d\) basis matrix \(V\) as the last columns of an invertible change of coordinates, up to an invertible change of basis in dimension \(d\).
Its affiliated image therefore equals the affiliated kernel, including for rectangular matrices.
The proper involution on affiliated matrix algebras makes \(V^*V\) injective over the division ring, hence invertible there.
The stated formula is a selfadjoint idempotent, acts identically on the columns of \(V\), and has precisely their affiliated image.
For bounded \(A\), its affiliated Moore–Penrose inverse identifies this right-module kernel with the module of its Hilbert kernel projection.
Selfadjoint idempotents with the same module image coincide, so the basis formula is the bounded Hilbert projection.
The rectangular polar part implements equivalence of this projection with \(I_d\), giving trace \(d\) with the unnormalized matrix convention.
The case \(d=0\) is immediate.
Its bounded entries lie in \(D_H\cap W(H)\), so the indicated \(C^*\)-rationality follows.

For an invertible square polynomial matrix \(P\), \(T=I-P^*P/M\) has \(q=\|T\|<1\) when \(M>\|P\|^2\).
The truncation through \(T^jP^*\) has propagation at most \((2j+1)w\).
Its operator-norm error bounds the \(\ell^2\) coefficient tail outside that radius by applying one entry to \(\delta_e\).
In the next shell the squared tail is bounded by a constant times \(q^{2j+2}\).
Weighting by \(e^{c(2j+3)w}\) gives a convergent sum for \(e^{cw}q<1\).
Taking a common positive exponent over the finitely many entries gives precisely the Hilbert–Schmidt sum in the Claim.
The dyadic shell norm at radius \(2^j\) is then \(O(e^{-c2^j/2})\), and every fixed polynomial square-sum moment follows as well.
Thus both spatial conditions in L_A0055 are met without using them as premises.
Right-coset copies preserve the subgroup projection and its trace, with Fourier coefficients zero outside \(H\).
The inequality \(|h|_G\le C|h|_H\) transfers the decay by shrinking \(c\), without an undistortion hypothesis.

A good four-line group is torsion-free and nonabelian by its nonzero characteristic-two zero product.
For noncommuting \(u,v\), the row \((1,T)\) is onto and the infinite-order \(1-u\) is injective with nonclosed range.
Consequently the product row has that same nonclosed range and kernel the graph of \(-T\).
The bounded graph formula yields \(D=(1+T^*T)^{-1}\) in its lower-right entry and \(-TD\) in its upper-right entry.
If all entries lay in \(\mathcal N(J)\) for a common cyclic \(J\), the inverse of \(D\) would lie there by bounded functional calculus, forcing \(T=u+v\) to have both Fourier labels in \(J\).
This contradicts noncommutation.
The example uses the separate bounded graph formula.
It does not require that the particular \(u,v\) chosen generate a free subgroup.

In the extension for arbitrary \(G\), \(E=I-XA\) satisfies \(E^2=E\), kills \(A\) on the stated side in the sense \(AE=0\), and fixes the entire affiliated kernel.
The identity \(EE^*+(I-E^*)(I-E)=I+(E-E^*)^*(E-E^*)\) holds using \(E^2=E\), so the affiliated matrix \(L\) has bounded inverse by positivity.
Its two summands annihilate one another, making \(P=EE^*L^{-1}\) a selfadjoint idempotent.
Independently, \(EP=P\) follows from \(E^2=E\), and commutation of \(L^{-1}\) with \(EE^*\) and the identity \(LE=EE^*E\) give \(PE=E\).
Thus \(P\) is the orthogonal projection onto the same affiliated image.
The assumed matrix inverse closure places \(L^{-1}\) and \(P\) over \(R\), boundedness of \(P\) permits application of (2), and its trace is integral under the separately stated \(C_r^*(G)\) projection-trace hypothesis.
The argument allows zero divisors in \(R\) and gives no general bounded-intersection identity or inner inverse for every four-line matrix.
The complete fixed Claim is supported at these scopes.
