---
author: Yin
---

# Complete independent review of Yin_C_F0115_v1

Date: 2026-09-16.
Reviewer: the reviewing agent.
Proof author: the coordinating research agent.
Human record author: Yin.
This is an independent, nonblind mathematical review, not proof-assistant verification or an external human review.

## Fixed material and disposition

**Pass for the whole stated result and its application boundary.**
No correction to the mathematical argument was required.
This review covers Sections 1–5 of [the proof](../../claims/Yin_C_F0115_v1.md#free-square-zero-sum-hermitization) and the complete attached [NS06-U002 interface](../literature/NS06/Yin_U002.md#ns06-u002), as selected by [Yin_C_F0115_v1](../../claims/Yin_C_F0115_v1.md#decision-candidate-0001).

The complete argument was first reviewed in the proof candidate.
The final registered proof was then reread: the status/header was updated to Claim/proof with separate-review attribution; the mathematical argument and attachment are unchanged.

There are **no direct project Claim dependencies**.
The scalar-law source input is NS06-U002, and the affiliated invertibility input is the existing [MSY23-U004](../literature/MSY23/Yin_U004.md#msy23-u004) interface.
The previous two-generator bounded-closure result is comparison only; neither its theorem nor its proof is used to obtain the present result.
No operator-valued subordination, Brown-measure theorem, random-matrix approximation or numerical experiment is used.

## Exact statement and scope

For every finite integer n>=3, let M be the reduced free product of n copies of `(M2(C),tr2)`, with its faithful tracial state tau.
In the ith factor let `x_i=e12`, set `s=sum_i x_i`, and put `H=[[0,s],[s*,0]]` in M2(M), with normalized faithful trace `tr2 tensor tau`.
Then s is injective and has a two-sided affiliated inverse in L0(M), and this actual inverse is unbounded.
The proof obtains the boundary value

`lim_(eta downarrow 0) G_H(i eta) = -i (n-1)/(n sqrt((n-2)/2))`.

The spectral measure of H has no atom at zero, while zero lies in its spectrum.
The conclusion therefore concerns the actual represented affiliated inverse, rather than a formal rational inverse or an arbitrary algebraic Cauchy-transform branch.

The result excludes the particular reciprocal `(sum_i x_i)^(-1)` as a bounded counterexample in T_F0007.
It does not prove or disprove general free-product bounded-closure permanence, does not classify other rational expressions, and makes no claim about a complete density, spectrum or Brown measure.
The argument uses n>=3 explicitly through `a=sqrt((n-2)/2)>0` and does not silently extend the boundary calculation to n=2.

## Independence and source-inspection depth

The reviewer did not develop this hermitization proof, write the source attachment, or participate in the author's calculations.
The reviewer had shared T_F0005/T_F0007 context, including a prior review of the distinct two-generator square-zero result.
The coordinator supplied the candidate, named the steps needing particular scrutiny, and supplied the NS06 locators.
This is independent checking of another agent's proof, but not a blind review.
The reviewer reported a whole-chain pass before registration; final correspondence was checked afterwards.
No change to the proof or source attachment was made by the reviewer.

The reviewer independently extracted and read the designated primary passages in the already registered local [NS06.pdf](../../literature/pdf/NS06.pdf), using the bundled Python `pypdf` runtime.
The file has 434 physical pages.
Read scope:

- Proposition 12.3 and its short proof: printed p.196 / physical PDF p.213, with the continuation on printed p.197 / PDF p.214.
- Theorem 12.5 and the Cauchy-series discussion: printed p.198 / PDF p.215.
- Notation 12.6 and Theorem 12.7 with the displayed derivation: printed p.199 / PDF p.216.
- Proposition 16.8 and its short proof: printed p.263 / PDF p.280, as corroborating multivariate context, not an additional necessary theorem.

The primary text gives cumulant additivity, the formal moment/cumulant identity, and the inverse-Cauchy/R-transform identity with the sign convention `G(z)=integral (z-t)^(-1) dmu(t)`.
The attachment accurately separates the formal identity from its use as a local analytic germ for compactly supported laws.
The analytic upgrade is checked below.
The general combinatorial foundations, including the full proof of vanishing mixed free cumulants and the earlier moment/cumulant theory, are accepted established inputs rather than newly audited here.

The reviewer also read the existing MSY23-U004 finite-trace polar-decomposition argument for injectivity if and only if affiliated invertibility, including its warning that this is not bounded invertibility.
Its primary source was not reopened for this review.
No new source work or PDF was acquired, no source rendering was performed, and no rendered-page validation is claimed.
The source attachment is a newly specified interface to the already registered NS06 work, not a new bibliographic work.
Its author's failed MiKTeX extraction is not evidence of a successful render or build; the review's successful evidence is the independent pypdf text extraction just described.

## Complete argument checks

1. **Individual law and conditional expectations.**
   For `H_i=[[0,x_i],[x_i*,0]]`, one has `H_i^2=diag(p_i,q_i)`, where `p_i=e11` and `q_i=e22`, and `H_i^3=H_i`.
   Their traces are `tau(p_i)=tau(q_i)=1/2`, while `tau(x_i)=0`.
   Thus the conditional expectation onto the outside M2(C) is `(1/2)I_2` on positive even powers and zero on odd powers.
   Together with the identity's expectation this gives `E_B(P(H_i))=(tr2 tensor tau)(P(H_i)) I_2` for every scalar polynomial.
   The scalar law is exactly `nu=(1/4)delta_-1+(1/2)delta_0+(1/4)delta_1`; in particular its second moment is 1/2, with no lost amplification-normalization factor.

2. **Scalar freeness is proved entry by entry.**
   If `P(H_i)` is scalar-centered, the preceding expectation identity makes every matrix entry tau-centered in the ith original free factor.
   Each entry of an alternating product of such centered matrices is a finite sum over intermediate matrix indices of products of centered original-factor entries.
   Adjacent factor indices remain different in every such product.
   Original scalar freeness makes its tau expectation zero, hence the normalized scalar matrix trace is zero.
   This is precisely the required scalar freeness of the unital polynomial algebras generated by the selfadjoint H_i.
   No generally false transfer of arbitrary scalar freeness through matrix amplification is assumed.
   Consequently the law of H is the n-fold scalar additive free convolution of nu.

3. **Symmetry and the rational one-summand transform.**
   The centered symmetric law nu has vanishing odd cumulants; additivity preserves this property, and the moment/cumulant relation gives vanishing odd moments of the compactly supported law of H, hence symmetry.
   Independently, conjugation of H by `diag(1,-1)` reverses its sign and also confirms the symmetry.
   Direct evaluation of the three atoms gives `G_nu(u)=(u^2-1/2)/(u(u^2-1))`, with only real poles `-1,0,1`.

4. **The local series is an actual analytic germ.**
   For a bounded selfadjoint variable with law mu, `g(t)=G_mu(1/t)` is analytic near t=0 and satisfies `g(t)=t+O(t^2)`.
   Its local analytic inverse exists by the inverse function theorem.
   The Laurent germ `K(w)=1/g^(-1)(w)` has leading term `1/w`; the source's formal inverse identities identify `K(w)-1/w` uniquely with the R-series.
   Thus this R-series converges locally and the formal identities are valid analytic germ identities.
   Cumulant additivity therefore gives `R_H=n R_nu` as convergent germs.
   This step needs bounded support and uniqueness of the inverse germ; it does not assert that an arbitrary formal series or selected cubic root defines the actual Cauchy transform.

5. **The upper-half-plane continuation has neither a sign error nor a hidden pole.**
   For the actual `w(z)=G_H(z)` on C+, `Im w(z)<0` because H has a probability spectral law.
   Hence w never vanishes, `Im(1/w)>0`, and `u(z)=(z+(n-1)/w(z))/n` is analytic and takes C+ into C+.
   On a nonempty open part near infinity, the local inverse identity gives `z=n R_nu(w)+1/w`, so `u=R_nu(w)+1/w` and `G_nu(u)=w`.
   The composition `G_nu(u(z))` is analytic on the whole connected C+, since u stays away from all real poles.
   The identity theorem now extends this equality globally.
   No continuation of R itself to all w-values, no global inverse of G_nu, and no unproved subordination theorem is required.

6. **The imaginary-axis branch is determined uniquely.**
   Symmetry gives `w(i eta)=-i h(eta)` with `h=integral eta/(eta^2+t^2) drho(t)>0`.
   Thus `u=i v`, where `v=(eta+(n-1)/h)/n>0`.
   The rational identity yields

   `h=(v^2+1/2)/(v(v^2+1))`, and `eta=F(v)=v(v^2-a^2)/(v^2+1/2)`, with `a^2=(n-2)/2`.

   Positivity of eta and v forces v>a, excluding the other real algebraic possibilities.
   Direct differentiation gives the displayed numerator `v^4+(a^2+3/2)v^2-a^2/2`.
   On v>=a it is at least `2a^4+a^2>0`.
   Therefore F maps `[a,infinity)` strictly increasingly and continuously onto `[0,infinity)`, and the actual v equals its unique inverse branch.
   It tends to a as eta decreases to zero.
   Substitution gives `h -> (a^2+1/2)/(a(a^2+1))=(n-1)/(n a)`.
   For n=3 this is `2 sqrt(2)/3`, as stated.

7. **Absence of an atom gives an actual affiliated inverse.**
   The functions `eta^2/(eta^2+t^2)` are bounded by one and converge pointwise to the indicator of zero.
   Thus `rho({0})=lim eta h(eta)=0`.
   The spectral projection onto ker H has normalized trace zero; faithfulness makes it zero.
   Since `H(xi,zeta)=(s zeta,s* xi)`, both s and s* have zero kernel.
   The existing finite-algebra criterion then supplies a closed densely defined two-sided inverse of s in L0(M).
   Equivalently, the inverse is defined on the dense range of s and is affiliated; no assumption about a bounded inverse has entered this step.

8. **The same boundary limit rules out a bounded inverse.**
   If H were boundedly invertible, its selfadjoint spectrum would avoid some interval `(-c,c)`, and its spectral law would give `h(eta)<=eta/c^2 -> 0`, contradicting the strictly positive finite boundary value.
   Hence zero lies in the spectrum of H.
   If the actual affiliated inverse of s were bounded, its adjoint would be the bounded inverse of s*, and `[[0,(s*)^(-1)],[s^(-1),0]]` would multiply H on either side to the identity.
   This contradicts the preceding conclusion.
   Therefore `s^(-1)` is unbounded.
   No pointwise density inference from a finite Poisson limit is used.

9. **The Task consequence follows with its exact restriction.**
   The element s lies in the polynomial algebra generated by the x_i and is invertible in the affiliated ambient algebra, so its inverse belongs to that algebra's affiliated division closure.
   The proof has shown that this particular inverse is not bounded.
   Its failure as a bounded counterexample does not imply the general closure equality, nor does it decide any other bounded rational expression.
   The source and comparison boundaries in Section 5 are consistent with this scope.

## Review outcome and mutation boundary

The registered proof and attached scalar-law source interface pass at the stated scope.
All nontrivial mathematical steps from scalar freeness through global analytic continuation to the actual unbounded inverse were checked.
No general T_F0007 completion, historical novelty, numerical confirmation, formal verification or rendered-PDF validation is asserted.

The reviewer wrote only this audit.
The proof, source attachment, canonical records, immutable versions, navigation and Task contract were not modified by the reviewer.
