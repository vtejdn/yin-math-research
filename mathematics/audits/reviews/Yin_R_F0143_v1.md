---
author: Yin
---
# Independent review of the selfadjoint contraction estimate with kernel weights

Review performed and recorded: 2026-10-14T17:33.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not derive, edit or participate in the preparation cross-check of [C_F0136 v1](../../claims/Yin_C_F0136_v1.md).
Root assigned the fixed candidate and disclosed that root developed it and a branch agent checked tensor order and the analytic-unitary passage during preparation.
No proof-development discussion or mutable author draft was consulted.
The reviewer read the complete fixed candidate selected by its initial decision dated 2026-10-14T17:29, the exact Dab10-U002 input, and the cited C_F0043 analytic-unitary passage as mechanism attribution before forming this finding.

This is an initial whole-proof review of the statement and all four proof sections.
It covers the output-weight estimate, the sharper analytic-unitary bound, all actual core-adjoint and trace identities, the passage to analytic unitaries with unbounded xi, approximation of bounded weights from the kernel algebra, and the actual affiliated-weight domain/limit.
It does not review a downstream application or assume this candidate established while checking it.

Dab10-U002 is the sole declared mathematical dependency.
Its exact selfadjoint represented-difference-quotient, reality, actual vacuum, core-adjoint and closability interfaces are accepted at their retained inspection depth.
C_F0043 provides the identified analytic-unitary mechanism; its different unitary-generator theorem is not an additional premise.
No new original-PDF or recursive foundational proof inspection is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0136 statement](../../claims/Yin_C_F0136_v1.md#statement) | Affiliated positive b in L2(W*(B)) with actual xi b in L2, the constant-4 output estimate for every core polynomial, the constant-2 analytic-unitary estimate for bounded selfadjoint kernel weights, and the bounded-xi corollary. |
| [Conclusion](#conclusion) | [C_F0136 argument](../../claims/Yin_C_F0136_v1.md#argument) | All four proof sections: real core adjoint and coassociativity, weighted tensor/trace energy identity, first-derivative analytic series and actual graph limit, and bounded/affiliated weight approximation with actual right-multiplier domains. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Sections 1-3 at the stated selfadjoint joint-conjugate assumptions: represented algebraic difference quotient, selfadjoint actual vacuum, reality, closability and E_0* q=q xi-E_0 q on the polynomial core. No weighted estimate or bounded-H conclusion is imported. |

## Exact premises and core identities

The generators are bounded and selfadjoint and have joint L2 conjugate variables, so the represented free difference quotient has algebraic tensor values on A, is real in the dagger convention, and has the actual selfadjoint vacuum xi.
The right contraction E_0 maps A into A, since its second-leg scalar contractions are finite sums of polynomial factors.
Dab10-U002 supplies its closability and the exact actual adjoint formula E_0*q=q xi-E_0q for q in A.
This is the right contraction; no interchange of its two tensor legs is made.

The coassociativity identity is also established locally: the two iterated derivatives are algebraic on A, their product cross terms cancel in their difference, and that difference vanishes on every selfadjoint generator.
Contracting the third leg gives

\[
\delta(E_0p)=(\mathrm{id}\otimes E_0)\delta p.
\]

Thus every second application used in the core calculation has an actual polynomial input.
Neither an unbounded-H iteration nor a closed-derivation functional-calculus statement is assumed at this stage.

For positive affiliated b and the selfadjoint measurable xi, the condition xi b in L2 is an actual domain condition for closed right multiplication by b.
Taking adjoints in the finite tracial measurable algebra gives (xi b)*=b xi, so the two integrability conditions and L2 norms agree.
This uses selfadjointness and the tracial L2 involution, not commutation of b and xi.
No invertibility of b is required.

## The weighted core energy identity and tensor order

Take c=c* in B.
Since delta(B)=0 and B is a star algebra, c squared lies in A, has zero derivative and E_0(c squared)=0.
Its actual core-adjoint value is c squared xi.
For any v in A,

\[
\tau((E_0v)c^2)
=\langle c^2,E_0v\rangle
=\langle c^2\xi,v\rangle
=\tau(\xi c^2v)=\tau(v\xi c^2).
\]

The last two expressions retain the order xi c squared.
All products are legitimate because xi is L2 and all other factors are bounded.

Writing delta p as a finite sum of u tensor v, coassociativity and the zero derivative of c squared give

\[
E_0((E_0p)c^2)
=\sum u\,\tau((E_0v)c^2)
=(\mathrm{id}\otimes\tau)
      \bigl((\delta p)(1\otimes\xi c^2)\bigr).
\]

The finite sum on the right uses only bounded polynomial coefficients multiplied by the L2 vector xi c squared.
The left is an actual second core application because (E_0p)c squared belongs to A.

Let T=tau((E_0p)* p xi c squared) and Q=(tau tensor tau)(delta(p*p)(1 tensor xi c squared)).
The adjoint pairing with the actual core vector (E_0p)c squared gives

\[
\|(E_0p)c\|_2^2
=\tau(p^*(E_0p)c^2\xi)
 -(\tau\otimes\tau)
   \bigl((p^*\otimes1)\delta p(1\otimes\xi c^2)\bigr).
\]

The first term is conjugate(T): conjugation yields tau(c squared xi p* E_0p), and tracial cyclicity brings the bounded outer factors to the displayed order.
No c-xi interchange is used.

Reality sends each u tensor v term of delta p to v* tensor u* in delta(p*).
Consequently

\[
(\tau\otimes\tau)
  \bigl(\delta(p^*)(1\otimes p\xi c^2)\bigr)
=\tau((E_0p)^*p\xi c^2)=T.
\]

The product rule for delta(p*p) therefore identifies the subtracted term as Q-T.
This proves exactly the candidate's identity (9), namely the weighted norm squared equals 2 Re T-Q.
It is an equality at the algebraic core, not a formal use of an adjoint or an assumed second-operator domain.
At this stage bounded coefficients times xi belong to L2 and hence L1, so every trace is defined even if xi is unbounded.

## Analytic unitaries use only the final identity

For selfadjoint a in A with norm(a)<1, the chosen binomial branch gives u=a+i(1-a squared)^(1/2), a unitary.
Its polynomial truncations p_n converge in operator norm, and their adjoint truncations converge to u*.
The estimate

\[
\|\delta(a^m)\|_2\le m\|a\|^{m-1}\|\delta a\|_2
\]

makes both differentiated series absolutely convergent in the coarse Hilbert norm.
The same uniform coefficient bounds justify multiplying and differentiating the two series: their scalar analytic product is the constant 1, so the product-rule limit of delta(p_n*p_n) is zero.
This is a direct convergent-series computation.
It does not apply an unproved derivative to an arbitrary functional-calculus element.

The bounded slice id tensor tau makes E_0p_n converge in H.
Since p_n tends to u in H and E_0 is closable, the resulting graph limit lies in its specified closure E and equals Eu.
The same conclusion holds at u*.
No second application E(Eu) or E((Eu)c squared) is used or required.

Every term of the final core identity (9) has a justified limit.
Bounded c sends E_0p_n to Eu continuously in L2.
The trace term pairs E_0p_n in L2 with p_n xi c squared in L2; the latter converges because p_n converges in operator norm.
Products of those two L2 factors belong to L1, so their traces converge.
Finally the Q-term is the Hilbert pairing of delta(p_n*p_n), which tends to zero, against the fixed tensor 1 tensor c squared xi.
The adjoint order in that representing tensor is exactly consistent with the original right factor xi c squared.

The resulting identity is

\[
\|(Eu)c\|_2^2
=2\operatorname{Re}\tau((Eu)^*u\xi c^2)
=2\operatorname{Re}\langle(Eu)c,u\xi c\rangle.
\]

The second equality moves bounded c cyclically around an L1 product; it does not commute c past xi.
The unitary u acts isometrically on xi c.
Cauchy-Schwarz yields r squared at most 2 r norm(xi c)_2 for r=norm((Eu)c)_2, proving the constant-2 bound, including r=0.
The same argument works for u*.

Since a=(u+u*)/2 and E's domain is linear, the estimate applies to E_0a.
Scaling a by norm(a)+epsilon and sending epsilon to zero gives the selfadjoint bound with factor 2 norm(a).
Splitting arbitrary p into real and imaginary selfadjoint parts, each of norm at most norm(p), gives the factor 4 in (12).
The proof does not need a convergence rate or a general C1 domain-preservation theorem.
The cited C_F0043 Section 3.2 is accurate mechanism attribution; its different additional unitary-generator terms are not imported here.

## From B to N and then to the affiliated weight

Let c be any bounded selfadjoint element of N=W*(B).
Kaplansky approximation in C*(B), followed by norm approximation with selfadjoint elements of B, supplies uniformly bounded selfadjoint c_alpha in B tending strongly-star, hence in L2, to c.
Since E_0p is bounded, (E_0p)c_alpha tends to (E_0p)c in H.

The corresponding convergence xi c_alpha to xi c also holds for unbounded xi in L2.
For a bounded L2 approximant xi_0, the error from xi-xi_0 is controlled by the uniform operator bounds of c_alpha and c, while the remaining term is bounded by norm(xi_0) times norm(c_alpha-c)_2.
This proves strong convergence of the products and of their norms.
Passing (12) to the limit therefore covers every bounded selfadjoint c in N.
The argument never claims delta(c)=0, or even defines delta(c), for arbitrary c in N.

For the positive affiliated b, choose b_n=b 1_{b at most n} in N.
Its assumed L2 membership gives b_n tending to b in L2.
The separate actual condition xi in Dom rho(b) gives xi b_n tending to xi b in L2 by the spectral-domain convergence for the closed right multiplier.
This second convergence does not follow merely from b_n tending to b in L2; the extra product-domain hypothesis is explicitly used.
Boundedness of E_0p gives (E_0p)b_n tending to (E_0p)b in L2.
The already established bounded-weight inequality now passes to b and proves (2).

When xi is bounded, ordinary bounded left multiplication gives norm(xi b)_2 at most norm(xi) norm(b)_2, so the corollary follows for every positive b in L2(N).
The zero weight and zero weighted-vacuum cases are included without dividing by their norms.

## Dependency and scope boundaries

Dab10-U002 supplies the exact represented real difference quotient, actual core adjoint and closability at the stated finite-Fisher assumptions.
The new weighted energy identity, all noncommuting factor orders and the complete first-derivative analytic series passage were checked directly above.
C_F0043 is only the identified mechanism; the proof does not depend on that Claim's unitary theorem, normalization or extra constants.
Original foundational source-proof inspection limits remain those of the retained input.

The proof uses no freeness between N and the distinguished coordinate and does not assert a closed derivation vanishes on every element of N.
The final statement concerns E_0p for p in A.
It establishes neither complete product-domain equality nor actual adjoint-domain inclusions for a general weighted nonreal contraction.
There is no numerical, proof-assistant or novelty claim, and no downstream result was assumed in this review.

## Conclusion

The complete statement and all four proof sections of C_F0136 v1 pass this independently organized review with no required mathematical correction.
The sole declared mathematical dependency is used at its exact accepted scope, and the separate mechanism attribution is accurate.
This finding supports proved / independently reviewed for the fixed candidate if its responsible decision adopts it.

The supported conclusion is the constant-4 right-output estimate for positive affiliated weights from the von Neumann algebra generated by a delta-zero star subalgebra, with both stated L2 product hypotheses, together with the sharper bounded-weight analytic-unitary estimate and bounded-xi corollary.
It is not itself a general nonnormal ACSY-to-full-domain implication or a statement about both domains of an arbitrary weighted contraction.
