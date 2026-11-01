---
author: Yin
---
# A semicircular product with an actual intrinsic vacuum: complete independent review

Date: 2026-10-14T20:18.
Human record author: Yin.
This separately organized agent review covers the complete fixed [C_F0150 v1 statement](../../claims/Yin_C_F0150_v1.md#statement), all four argument sections and its two declared direct dependencies.
The initial decision is dated 2026-10-14T20:14.
The CN21 source unit was also checked at its expressly comparative restriction scope.

The reviewer did not develop the coefficient choice, integrability argument or separated-leg adjoint construction.
Prior work on other T_F0011 normal-domain questions, and earlier independent reviews of C_F0145 and C_F0147, is related background rather than development of this result.
The assignment supplied the candidate X=(2+s0)S, the claimed actual-vacuum scope and the identities of the developers.
No D_F0003 development notes or proof-generation dialogue were consulted.
The fixed C and its exact input sections were read, and the calculations below were reconstructed independently.
No earlier C_F0150 review conclusion was supplied or relied on.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0150 statement](../../claims/Yin_C_F0150_v1.md#statement) | Intrinsic whole-star-core derivation for X=hS, actual vacuum of norm at most sqrt(2), both separated-leg reference adjoint domains, coefficient integrability and explicit absence of an F or S conclusion. |
| [Conclusion](#conclusion) | [C_F0150 argument](../../claims/Yin_C_F0150_v1.md#argument) | All four sections: actual adjoint isometries, two-variable coefficients, full reference-core pairing and conditional-expectation compression. |
| [Conclusion](#conclusion) | [Miy22-U001](../literature/Miy22/Yin_U001.md#miy22-u001) | Variance-one free semicircular Fock model, faithful trace, word orthonormality, recurrence and normalization. Foundational source limits remain those of the unit. |
| [Conclusion](#conclusion) | [C_F0144 exact word cuts](../../claims/Yin_C_F0144_v1.md#letter-count-grading-and-the-actual-reference-adjoint) | The recurrence proof of the polynomial word-cut identity, equally for either letter. No nonlinear-target result or finite-degree bound is needed. |
| [Conclusion](#conclusion) | [CN21-U001](../literature/CN21/Yin_U001.md#cn21-u001) | Attribution and comparison only: actual versus closed adjoint domain, restriction versus extension, and the target projection required for an intrinsic restricted vacuum. The compression proof in C_F0150 is checked directly. |

## Findings

### 1. The separated-leg adjoints are actual isometries

In the standard two-letter Fock basis, the tensor U_m(s0) tensor U_n(S) corresponds to the pair of words (0^m,1^n).
In the word-cut formula, insertion of the derivative letter 0 gives the unique word 0^(m+1)1^n, and insertion of letter 1 gives 0^m1^(n+1).
For each of these two maps separately, different pairs (m,n) produce different output words, including the cases m=0 or n=0.
Thus each map is isometric on the algebraic separated-leg span.
The two maps need not have orthogonal ranges; the proof does not assert this.

For an arbitrary vector eta in the closed separated-leg tensor space, expand it in this orthonormal basis and take the corresponding isometric output series.
Pairing against every reference Wick polynomial gives the exact adjoint identity: only finitely many word cuts occur in each test polynomial.
Hence the output represents the actual adjoint functional on the entire mixed polynomial core.
This proves the actual domain inclusion for all eta, not only a weak functional identity on the marginal algebras.
It also independently verifies equation (2).
Translating s0 to h does not change the derivative or its polynomial domain.

### 2. Both coefficients are Hilbert vectors with the stated normalization

The joint variables u and v belong to separate commuting tensor legs with the product law of h and S.
They are not being treated as commuting operators inside the reference von Neumann algebra.
The equality

\[
 |\alpha(u,v)|^2+|\beta(u,v)|^2=(u^2+v^2)^{-1}
\]

holds off the product-null origin.
The semicircular density bound 1/pi gives the inner integral at most 1/u for u>0.
For the shifted density sqrt(u(4-u))/(2 pi), substitution u=4 sin^2(theta) gives

\[
 \int_0^4u^{-1}\frac{\sqrt{u(4-u)}}{2\pi}\,du
 =\frac4\pi\int_0^{\pi/2}\cos^2\theta\,d\theta=1.
\]

Tonelli therefore gives I at most 1 and both coefficients in the closed oriented tensor space.
The same density has no atom at zero, while its inverse-square integrand is comparable to u^(-3/2) there.
Thus h is regular and h inverse is not L2, exactly as claimed.
The scalar identity v alpha+u beta=1 uses the second-leg right action by S and first-leg left action by h.
It proves delta(hS)=1 tensor 1 with the displayed action order.
The reverse product derivative beta dot h+S dot alpha is a Hilbert tensor because h and S are bounded; it is not assigned independently.

### 3. The vacuum pairing holds on the full represented reference algebra

The reference free difference quotients exist on the represented free semicircular polynomial algebra.
Their values on each polynomial are finite sums of tensors with bounded legs.
Outer insertion of either Hilbert coefficient is consequently defined on every such value, intertwines the outer bimodule actions and preserves the Leibniz rule.
No bounded operator on the whole coarse Hilbert space is required for this insertion.

For elementary bounded a tensor b, traciality gives the vacuum pairing of a dot eta dot b with eta's componentwise adjoint against a tensor b.
Hilbert continuity extends this equality to the displayed coefficients.
Their being real functions of the two selfadjoint tensor variables means componentwise eta*=eta, so no adjoint or conjugation factor is missing in equation (7).
With the stated inner-product convention, the actual adjoint identity is precisely

\[
 \langle1,\delta p\rangle
 =\langle\partial_h^*\alpha+\partial_S^*\beta,p\rangle.
\]

The two actual adjoint memberships follow from Section 1, and their separate isometry estimates yield

\[
 \|v_0\|_2\le\|\alpha\|_2+\|\beta\|_2
 \le\sqrt{2(\|\alpha\|_2^2+\|\beta\|_2^2)}\le\sqrt2.
\]

This is an actual Hilbert-adjoint assertion on the full reference core.
It uses neither a formal inverse h inverse nor an extension of a target-only derivation.

### 4. The compression has the correct intrinsic target and vacuum

Conditional expectation Q_N extends to an orthogonal contraction on L2 and is N-bimodular.
Its tensor square therefore intertwines the outer target actions.
Restricting delta to the target star core and then applying this tensor square gives a derivation into the intrinsic coarse space of N.
The target core is L2-dense in N, and its generator value remains 1 tensor 1.
For every target polynomial p,

\[
 \langle1,(Q_N\otimes Q_N)\delta p\rangle
 =\langle1,\delta p\rangle
 =\langle v_0,p\rangle
 =\langle Q_Nv_0,p\rangle.
\]

This proves the actual target adjoint domain and the same norm bound.
It separately projects both the coefficient legs and the vacuum, without identifying N with the larger reference algebra.
This agrees with the corrected CN21 restriction interface, but the local argument is complete without importing a restriction or extension theorem from that source.

## Source and review limits

The exact source units and the C_F0144 word-cut argument were read.
The Fock trace and semicircular identification are accepted at Miy22-U001's recorded foundational scope; no fresh audit of every original textbook or of all Miy22 pages is claimed.
The local recurrence, separated-leg adjoint tests, integrals and compression were checked directly.
CN21 is used as the named comparison recorded in the fixed claim, not as a premise asserting target-to-reference extension.
No numerical computation or formal verification is represented as proof evidence.

The argument proves intrinsic A(N;hS).
It makes no assertion about a bare full-N dual, the full bounded-vector domains of canonical operators, or a separation of A and F.
In particular, failure of the individual coefficient h inverse tensor 1 to be Hilbert does not contradict the successful two-coefficient construction.

## Conclusion

The exact statement and complete argument of C_F0150 v1 pass this independent review.
Both declared dependency interfaces apply, the additional source comparison respects its inspected boundary, and no remaining mathematical gap or required source correction was found.
This supports a `proved` and `independently reviewed` assessment upon adoption by the responsible decision, at the explicitly limited A-positive scope.
