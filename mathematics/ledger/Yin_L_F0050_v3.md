---
author: Yin
---
# ACSY24 Proposition 3.5 and full-domain duals: extended equivalence classes and remaining questions

Date: 2026-10-14T13:28.
Human author Yin.
This is a bounded continuation under the explicit request to investigate mutual implication of the two mathematical hypotheses below.
The root agent organized this comparison after the fixed proofs and reviews linked below.
This synthesis is self-checked; it does not supply an additional independent review of those proofs.
The [previous comparison](Yin_L_F0050_v2.md) and [first comparison](Yin_L_F0050_v1.md) retain their historical scopes.

## Exact hypotheses

Let (M,tau) be finite tracial with faithful normal tracial state, H=L2(M,tau), Omega=1, P=P_Omega, and let X=(X_1,...,X_d) be a finite bounded generating tuple.
Put A_X^*=C<X,X*> for the represented unital star algebra.

- F(X): complex-linear maps D_i:M Omega -> H exist and satisfy [X_j,D_i]=delta_ij P on all M Omega.
  No continuity, closability or adjoint-domain hypothesis is imposed.
  The maximal-Delta argument at this scope is fixed in [C_F0024 Section 3](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors).
- A(X): outer-bimodule derivations partial_i:A_X^* -> H tensor_2 H exist with partial_i(X_j)=delta_ij 1 tensor 1 and 1 tensor 1 in Dom partial_i*.
  These are actual Hilbert adjoints.
  This is the complete hypothesis of [ACSY24 Proposition 3.5](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).

Both conditions imply Delta(X)=d.
The source condition does not require normality or reality.
The separate source reconstruction, including its nonnormal regularization, was checked in [R_F0044](../audits/reviews/Yin_R_F0044_v1.md#acsy-no-normality).
Mutual coverage through the hypotheses means F(X) implies A(X) and A(X) implies F(X); a shared conclusion does not establish either implication.

All assertions below concern existence of systems.
They do not identify an arbitrary supplied full-domain map with a canonical Hilbert closure on all bounded vectors.

## Current implication map

| Class of generating tuple or additional premise | F(X) implies A(X) | A(X) implies F(X) | Fixed support |
| --- | --- | --- | --- |
| Any finite selfadjoint tuple | Yes | Yes | [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement), Part B |
| Each coordinate selfadjoint or unitary, with arbitrary correlations | Yes | Yes | [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement), Part D |
| One arbitrary normal generator | Yes | Yes | [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement), Part C |
| Invertible complex affine changes of selfadjoint generating tuples | Yes | Yes | [C_F0071 v2](../claims/Yin_C_F0071_v2.md#statement), Part E |
| Elliptic images X_j=alpha_j U_j+beta_j U_j* of arbitrary generating unitaries, with unequal coefficient moduli | Yes | Yes | [C_F0130](../claims/Yin_C_F0130_v1.md#statement) |
| Every X_j* belongs to Div_M C<X>, without normality | Yes | Not established in this whole class | [C_F0129](../claims/Yin_C_F0129_v1.md#statement) |
| Arbitrary correlated normal tuples | Not resolved generally | Not resolved generally | Exact remaining interfaces below |
| Arbitrary bounded generating tuples | Not resolved generally | Not resolved generally | No separating example established here |

The positive conclusions of C_F0129, C_F0130 and C_F0072 remain proved in their responsible decisions.
Their whole findings have, respectively, unknown, unknown and self-reviewed relationships in R_F0136, R_F0137 and R_F0045.
Their respective complete reviews are [R_F0136](../audits/reviews/Yin_R_F0136_v1.md#conclusion), [R_F0137](../audits/reviews/Yin_R_F0137_v1.md#conclusion), and [R_F0045](../audits/reviews/Yin_R_F0045_v1.md#conclusion).
The exact review arrangements, accepted inputs and inspection limits remain in those records.

## Bounded division closure: the former candidate is now checked

Put B=Div_M C<X>, using only inverses of elements invertible in M, so that all intermediate expressions stay bounded.
Assume X_j* belongs to B for every j.
The complete argument in [C_F0129](../claims/Yin_C_F0129_v1.md#argument) now gives

\[
 \mathsf F(X)\Longrightarrow\mathsf A(X),
\]

without a normality hypothesis.
It gives more: for normalized maps E_i(a)=-D_i(a)+aD_i(1), the actual operators

\[
 \widehat D_i=-\overline{E_i|_{A_X^*\Omega}}
\]

satisfy

\[
 M\Omega\subseteq\operatorname{Dom}\widehat D_i
                 \cap\operatorname{Dom}\widehat D_i^*,
 \qquad [X_j,\widehat D_i]=\delta_{ij}P
 \quad\hbox{on }M\Omega.
\]

The whole-proof review checked the extra interfaces that were previously pending: automatic M-to-H continuity for a general Hilbert-Schmidt commutator with a diffuse selfadjoint element; implementation of the conjugate derivation by bounded right coefficients; realification and actual vacua; and the two canonical graph restorations.
Existing component reviews were not treated as a substitute for this whole check.

This is an adopted forward implication, not a new proof of the reverse one.
The automatic-continuity mechanism begins with a map already defined on every bounded vector.
It cannot by itself extend an ACSY core operator.
Nor does normality imply the bounded-division-adjoint premise.

## Elliptic coordinates: a further multivariable equivalence class

For a generating unitary tuple U with arbitrary correlations, let

\[
 X_j=\alpha_jU_j+\beta_jU_j^*,\qquad |\alpha_j|>|\beta_j|.
\]

The complete new [C_F0130 proof](../claims/Yin_C_F0130_v1.md#argument) establishes

\[
 \mathsf A(X)\Longleftrightarrow\mathsf A(U)
 \Longleftrightarrow\mathsf F(U)\Longleftrightarrow\mathsf F(X).
\]

Translations are allowed; replacing U_j by U_j* covers the opposite strict inequality.
Equal moduli are excluded from this coordinate equivalence.
The common star algebra follows from

\[
 U_j=\frac{\overline{\alpha_j}X_j-\beta_jX_j^*}
 {|\alpha_j|^2-|\beta_j|^2}.
\]

This recovery uses the adjoint and is not a claim that the holomorphic rational fields are equal.

The projective coefficient

\[
 J_i=\alpha_i1\otimes1-\beta_iU_i^*\otimes U_i^*,\qquad
 q_i=J_i^{-1}=\frac1{\alpha_i}\sum_{n\ge0}
    (\beta_i/\alpha_i)^n(U_i^*)^n\otimes(U_i^*)^n
\]

gives the two coordinate transformations.
Its absolute projective summability makes the right-multiplier corrections act on bounded maps M -> H.
The substantive adjoint step for the infinite derivation transformation is the actual estimate

\[
 \|\theta_i^*(U_i^n\otimes U_i^n)\|_2\le\|\xi_i\|_2+2n.
\]

Together with the geometric coefficients this proves an absolutely convergent vacuum-vector series.
Hilbert-tensor boundedness alone would not justify that adjoint assertion.
No finite-rank preservation is inferred from this infinite series.

The new multivariable range is not confined to tuples with bounded rational adjoints.
For Haar U and 0<r<1, X=U+rU* satisfies both conditions, but X* is not in Div_M C[X].
The rational-function automorphism z -> r/z fixes z+r/z and excludes rational recovery of z.
[C_F0130 Section 7](../claims/Yin_C_F0130_v1.md#7-this-class-need-not-have-adjoints-in-the-bounded-division-closure) gives the complete example.
The scalar equivalence was already known; this example only distinguishes the additional premises.
The new equivalence permits arbitrary correlations among several such coordinates.

## Two contraction bounds remove the reality requirement

The newly checked [C_F0072](../claims/Yin_C_F0072_v1.md#statement) isolates a sufficient analytic condition.
For any outer derivation delta on a weakly dense unital star algebra, put

\[
 E=(\mathrm{id}\otimes\tau)\delta,
 \qquad L=(\tau\otimes\mathrm{id})\delta.
\]

If both are bounded from the operator norm to L2, with constants C_E,C_L, then

\[
 1\otimes1\in\operatorname{Dom}\delta^*,\qquad
 \|\delta^*(1\otimes1)\|_2\le2(C_E+C_L).
\]

No reality, coassociativity or initial closability assumption is required.
The same proof gives, for the specified core operator E_0 and xi=delta*(1 tensor 1),

\[
 E_0^*(a\Omega)=a\xi-(L(a^*))^*,\qquad
 M\Omega\subseteq\operatorname{Dom}\overline{E_0}
                 \cap\operatorname{Dom}E_0^*.
\]

The proof extends the continuous-square-partition mechanism by estimating the two contractions separately.
The argument and actual graph estimates are owned by C_F0072; the comparison does not treat this as an already printed ACSY result.

For a normal tuple satisfying F(X), [C_F0070 Part A](../claims/Yin_C_F0070_v1.md#statement) already gives the unique starred derivations and bounded RIGHT contractions.
Consequently a uniform bound for the LEFT contraction on the entire starred algebra would now give A(X), as well as the two canonical full domains.
This is a sufficient route with one precise missing estimate; no necessity of the left bound for A(X) is asserted.

## Remaining general questions and the attempted spectral route

For a normal tuple already satisfying A(X), write E_i0=(id tensor tau)partial_i on A_X* Omega.
[C_F0070 Part B](../claims/Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) gives

\[
 \mathsf F(X)\Longleftrightarrow
 M\Omega\subseteq\operatorname{Dom}\overline{E_{i,0}}
 \quad\hbox{for every }i.
\]

This is equivalent to a uniform operator-norm-to-L2 bound on each canonical core contraction: closed graph gives necessity, and Kaplansky plus weakly closed graph gives sufficiency.
The right-domain conclusion alone must not be conflated with the additional adjoint-domain conclusion obtained from the TWO estimates in C_F0072.

For the opposite direction, the retained normal spectral phase has modulus one on the off-diagonal product spectrum.
In the attempted finite-partition implementation of the conjugate derivation, it introduces sums involving E_i(a p_r) p_s and the phase coefficients.
Its norm bound as a multiplier on the coarse Hilbert tensor product does not yield an estimate for these maps M -> H independent of the partition size.
This continuation did not establish such a uniform estimate.
It therefore supplies neither a proof nor a counterexample for unrestricted normal tuples.

The elliptic proof avoids that unresolved passage because its coefficients have an explicitly summable projective expansion and the associated adjoint vectors grow only linearly.
Letting the coefficient moduli become equal does not remove the restriction: the Neumann bound diverges and star-linear recovery of U degenerates.
This is a limitation of that coordinate method, not a separating example.

Two precise next targets remain:

1. Starting from F(X) for a general normal tuple, control the left contractions on the full starred polynomial algebra, or find a system for which the actual vacuum fails.
   The existing right-contraction bound alone does not complete this route.
2. Starting from A(X), prove the needed canonical right-contraction bound, or exhibit a tuple for which the canonical bounded-vector domain fails.
   Merely changing to another algebraic full-domain extension cannot bypass the normal-tuple equivalence above.

## Counterexamples that do not separate the two hypotheses

The strong normal atomic example in [C_F0128 v2](../claims/Yin_C_F0128_v2.md#statement) has a normalized closable dual on a dense starred core and an actual adjoint vacuum for that OPERATOR, but does not have the full starred Hilbert-valued derivation hypothesis.
It refutes the weaker dense-domain-to-full-domain assertions, not either implication between A(X) and F(X).

The one-sided transport and Jordan tests in [L_F0049](Yin_L_F0049_v1.md) make both A(X) and F(X) fail.
The Jordan example still has maximal Delta, so maximal Delta alone supplies neither condition.
These examples must not be reused as a separation of A and F.

No separating counterexample has been established by this continuation.
The expanded positive classes and the two-contraction criterion are fixed with the finding-specific review relationships above; the general correlated-normal and arbitrary-bounded-tuple comparison remains unresolved.
