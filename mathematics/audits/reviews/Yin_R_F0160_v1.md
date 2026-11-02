---
author: Yin
---
# Independent complete review of the singular-factor full-domain dual construction

Review performed and recorded: 2026-10-14T20:44.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and scope

The complete fixed [C_F0152 v1](../../claims/Yin_C_F0152_v1.md), initial decision dated 2026-10-14T20:40, and all three exact direct inputs were read.
This review covers its complete statement and all six proof sections: actual coefficient expansion, complete-terminal-block cancellation, partial-block column estimate, orthogonal multiplication and means, ambient original closure, and intrinsic target original closure and dual sign.

The general-branch author and root developed the cut construction and supplied no proof contribution through this reviewer.
The assignment disclosed the intended cancellation/column mechanism.
Earlier, while developing a different test, this reviewer had read D_F0003's then-existing coupled coefficient expansion and its failed termwise summation bound.
Those prior inputs are disclosed: the review is not blind to the coefficient series.
The reviewer did not read the later D12 complete-block/partial-block proof development and did not participate in its construction.
All new estimates and their interfaces below were reconstructed from the fixed C.

This reviewer developed the separate holomorphic scalar estimate in D_F0005 and the different row obstruction C_F0148.
Those are related development, not independent evidence for themselves.
Neither is a premise of C_F0152, and neither is used to supply a missing bound here.
C_F0150's adopted actual-derivation construction is reused at its exact fixed scope; this review does not broaden it retrospectively.

## Current relationship clarification

Before this fixed proof review the reviewer had actually read the same D12 construction’s coupled coefficient expansion and failed termwise summation argument.
Those are substantive development inputs to the present coefficient/cancellation problem, beyond the later fixed proof and accepted dependencies; the selected whole-proof conclusion therefore has a self relationship.
Reconstructing the later complete-block and partial-block estimates does not remove that known shared context.
The reviewer’s separate C_F0148 or scalar work is not itself the reason for this relationship.
All original mathematics, dates, limits and historical independent wording are preserved; no new review is claimed and no reviewer-supplied repair is recorded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0152 statement](../../claims/Yin_C_F0152_v1.md#statement) | Exact reference coefficients, full ambient original forward closure, explicit infinity-to-L2 bound and all-bounded-vector commutator, intrinsic original target closure and generator-first bare dual; no full adjoint-domain assertion. |
| [Conclusion](#conclusion) | [C_F0152 argument](../../claims/Yin_C_F0152_v1.md#argument) | Every step in all six sections, including noncommuting row order, exact versus partial terminal cuts, column rather than square-sum control, actual product identification, dense adjoint domain, and simultaneous ambient/target weak graph limits. |
| [Conclusion](#conclusion) | [C_F0150](../../claims/Yin_C_F0150_v1.md#statement) | Actual represented reference and intrinsic target derivations, their actual vacua, Hilbert coefficient integrability, separated-leg adjoint isometries, h regular, tau(h inverse)=1 and norm h=4. No F or full-domain result is assumed from that earlier Claim. |
| [Conclusion](#conclusion) | [Miy22-U001](../literature/Miy22/Yin_U001.md#miy22-u001) | Variance-one Fock normalization, faithful trace, right append/delete actions, right semicircular multiplication and orthonormal Wick words. Recorded foundational-source limits remain unchanged. |
| [Conclusion](#conclusion) | [C_F0144 word cuts](../../claims/Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) | Only its exact polynomial derivative word-cut identity and recurrence, for either reference letter. No nonlinear target construction, total-degree estimate or summability theorem is imported. |

## 1. Coefficients and the exact original contraction

For u>0, the positive q in (4) is in (0,1) and satisfies 1-q squared=u q.
Substituting -i q into the semicircular generating series gives the denominator 1+i q v-q squared=q(u+i v), so its numerator q produces exactly (5).
Orthogonality of U_n in the second leg gives the sum q squared/(1-q squared)=q/u.
Its integral is finite by the precise tau(h inverse)=1 input.
Thus the series is a genuine coarse Hilbert expansion.
Its even and odd terms give the beta and alpha series with the signs shown, and the odd q-power square sum is exactly the beta norm squared.

In a derivative word cut, tracing the second leg against U_n(S) selects precisely a pure-1 suffix of length n.
The beta term deletes an odd total number of terminal 1 letters; the alpha term deletes those letters and the immediately preceding 0.
Right multiplication by the indicated power of q follows the deletions.
This proves (8) with the displayed order.
A finite Wick polynomial has only finitely many surviving cuts, and coarse coefficient convergence followed by its finite bounded outer actions identifies these values with the original contraction.
No operator-norm convergence of the full series is needed.

## 2. Complete terminal blocks and noncommuting operator order

P0 includes both the vacuum and the words ending in 0.
Thus C_n=P0 r1*^n has initial projection onto exactly the words whose terminal block of 1 letters has length n.
These initial projections are pairwise orthogonal, so the cut column is a Hilbert contraction even though the ranges of its entries coincide.

Let A=I+Q r0*.
The decomposition A=(I+r0*)-(I-Q)r0* is valid without commuting Q and r0*.
The two-factor inequality gives

    BB* <= AA*
        <= 2(I+r0*)(I+r0)+2(I-Q)r0*r0(I-Q)
        = 2 rho(h)+2(I-Q)^2 <= 4 rho(h).

Here r0*r0=I and (I+r0*)(I+r0)=2I+r0+r0*=rho(h).
The scalar estimate (1-q)^2<=h is valid by 1-q squared=hq, including the zero endpoint by continuity.
Thus the inequality has the correct order throughout.

For a finite row the square is the sum Q^n BB* Q^n.
Q and rho(h) commute because both are scalar functions of right h.
Summing the odd geometric series after multiplying by h gives q/(1+q squared), bounded by one half.
Regularity of h removes any issue with the value of that limit on its zero spectral projection.
The row norm is at most sqrt(2), uniformly in the truncation, and hence extends to the Hilbert direct sum.
Composition with the cut column proves (13) and its convergence.

Since r0*P1=0, the alpha part selected by this complete-block construction is the entire alpha part of (8).
The remaining beta terms are precisely P1 r1*^n p followed by right q^n multiplication.
This checks E=K+R on the original core, without an unbounded exchange of sums or a different extension of E.

## 3. The partial-block column estimate

For the unilateral creation isometry r1, the Chebyshev recurrence gives U_n(r1+r1*)=sum_(j=0)^n r1^(n-j)r1*^j.
Subtracting r1 U_(n-1) leaves r1*^n, verifying (15).
Applying P1 and using P1 r1=r1 gives (16).

The vectors U_n(S) for odd n form an orthonormal family; the even family U_(n-1)(S), including its vacuum member, does too.
Left multiplication by the fixed bounded p has Hilbert norm at most ||p||.
Therefore each of the two maps from ell2 into H in (16) has norm at most ||p||, and their difference A_p has norm at most 2||p||.
This is a column-operator estimate.
It does not assert sum ||a_n|| squared<=4||p|| squared, which would be a different and unjustified bound.

The centered coefficient vector sum epsilon_n e_n tensor b_n has squared Hilbert norm sum ||b_n|| squared, at most ||beta|| squared.
Applying A_p tensor identity gives (19).
This retains cancellation within each a_n and avoids the failed sum of individual q-power norms.

## 4. Concatenation, scalar means and the stated constant

Every Wick word in P1H ends in 1.
Multiplying it by a nonempty pure-0 Wick word causes no annihilation; the product is the concatenated Wick word.
The final 0 block determines its length and hence the split uniquely, even if the preceding word contains earlier 0 blocks.
The resulting products are an orthonormal family, proving the multiplication isometry on the completed Hilbert tensor space.

For the actual use, the a_n are polynomial vectors, and each b_n is a bounded function of h.
Approximating the second factor in L2 by its marginal polynomials makes the isometric concatenation equal its genuine product, since multiplication by the fixed polynomial first factor is bounded.
On any polynomial input only finitely many a_n are nonzero.
Thus the centered part of R has precisely the claimed bound 2||p||||beta||.

The nonnegative scalar means have sum tau(q/(1-q squared))=tau(h inverse)=1 by monotone convergence.
Each P1 r1*^n is a Hilbert contraction, so their signed mean-weighted sum converges in Hilbert operator norm with bound one.
Adding its norm, the complete-block bound sqrt(2), and the centered bound gives (21).
The two Hilbert terms use ||p||2<=||p||, and ||beta||<=1 gives the stated upper bound sqrt(2)+3.

## 5. Actual adjoint core, closability and ambient bounded vectors

The integration-by-parts formula (22) has the correct nonreal order and sign.
It can be checked directly: apply the actual vacuum identity to a* p and expand delta(a* p).
The resulting pairing is

    <a,Ep>=<a v0,p>-< (id tensor tau)delta-dagger(a),p>.

The tensor flip in delta-dagger is required; componentwise adjoint without the flip would put the wrong contraction on the second term.
Both displayed output terms are Hilbert vectors for every fixed core a.
This proves actual membership in Dom(E*) and density of that domain.
It is also consistent with the coefficient-graph approximation supplied in the candidate: the separated-leg adjoint isometries and their flipped counterparts give convergence of the vacua, while finite outer multiplications handle each fixed polynomial.
Thus E is closable; no assumed full adjoint domain is involved.

Uniformly operator-norm-bounded Kaplansky approximants from the original core converge in L2 to any a in M.
The bound (21) gives a weakly convergent subnet of their E values.
The closed linear graph of the actual Hilbert closure is weakly closed, so it contains the limiting pair.
This proves a in Dom(overline E), uniqueness of its value and the claimed bound by weak lower semicontinuity and then epsilon decreasing to zero.

The same approximants satisfy the exact core commutator (23).
Bounded left multiplication by X and the L2-continuity of tau pass it to the weak graph limit, giving the actual all-M commutator.
This proves both parts of (2) for the original closure, rather than only for an independently selected bounded extension.

## 6. Intrinsic target closure and generator-first sign

On N, T=Q_N overline(E) is bounded for the operator norm and has the required commutator because Q_N is N-bimodular.
This already supplies a Hilbert-valued full-N map.
To identify the specified target closure one needs the additional argument in Section 6, which is valid: contraction on the second tensor leg commutes with Q_N tensor Q_N by trace preservation, so E_N=Q_N E on the target star core.

C_F0150's actual intrinsic target vacuum and the same Leibniz pairing give a dense actual adjoint domain for E_N.
Target Kaplansky approximants have uniformly bounded E images by (21).
Choose a simultaneous weakly convergent subnet; the ambient original graph identifies its E limit with overline(E)a, and the target original graph identifies the Q_N-projected limit with overline(E_N)a.
Thus overline(E_N)a=Ta for every bounded target a, with the same norm bound.
No assertion N=M is made or needed.

Finally D=-overline(E_N)|_N gives [X,D]=[overline(E_N),X]=P, which is the requested generator-first convention.
The proof does not place all M or N in the actual adjoint domains, and it does not establish a general A-to-F theorem beyond this tuple.

## Source and verification limits

The complete three fixed inputs and their exact interfaces were read.
Miy22's standard trace/Fock foundations remain accepted at U001's recorded inspection limits; its external textbooks were not newly audited.
The word-cut formula is reused from the exact fixed C_F0144 section, while the new cut and column estimates are all checked above.
No numerical computation, formal verification, external multiplier theorem or older degree-summability result is used as proof evidence.

## Conclusion

**The complete fixed C_F0152 v1 statement and all six proof sections pass independent review, with every declared direct dependency covered.**
No correction or additional hypothesis is required.
The proof establishes the actual ambient and intrinsic original forward closures on all bounded vectors and an intrinsic bare full-domain dual, with the stated constant.
It does not establish full adjoint domains or resolve the unrestricted A-to-F implication.
