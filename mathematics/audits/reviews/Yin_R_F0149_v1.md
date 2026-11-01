---
author: Yin
---
# Independent review of nonlinear target derivations and actual-adjoint reduction

Review performed and recorded: 2026-10-14T18:44.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0142 v1](../../claims/Yin_C_F0142_v1.md).
Root assigned the fixed candidate after completion of the C_F0078 review.
The disclosed developers were the general-branch author for the affiliated construction, polynomial relation, uniqueness and positive-reference range formula, and root for the arbitrary-bare-witness equation.
No mutable D or proof-development discussion was read.
Root also supplied unrelated literature-correction context; it was not consulted or used as a mathematical premise.
The full fixed candidate and its three declared exact source-unit scopes were read before this conclusion.

This review covers the whole statement and all five proof sections: generation; opposite multiplication and affiliated inverse; bounded starred derivative values; uniqueness among all coarse-affiliated derivations; full-linear-matrix applicability and diffuseness; both directions of the existential actual-adjoint criterion; the equation for an arbitrary bare witness; Hilbert-Schmidt uniqueness; and the separate positive-S range construction.
The current text's meaning-preserving repair of the missing backslash before quad in (6) was verified.
No substantive proof change was made during this review.

The existing AP18, ACSY24 and MSY23 source units are accepted at their recorded statement/proof and version-inspection limits.
The Douglas attribution was independently checked in parsed primary text at printed pages 413-414, Theorem 1 and its majorization-to-factorization proof step.
No original AP18 source reread, whole-source audit, numerical experiment or proof-assistant verification is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0142 statement](../../claims/Yin_C_F0142_v1.md#statement) | Exact finite-Fisher reference and positive regular h, nonlinear generation, unique L0(N)-valued coordinate derivations and bounded target values, equivalent actual-adjoint tests, arbitrary bare-witness equation and separately quantified Hilbert-Schmidt uniqueness/positive-S existence. |
| [Conclusion](#conclusion) | [C_F0142 argument](../../claims/Yin_C_F0142_v1.md#argument) | Complete Sections 1-5, including all affiliated coefficient orders, full-pencil/Schur-complement applicability, target-only uniqueness, actual vacuum equivalence, weighted range factorization and limits on the bare-witness interpretation. |
| [Conclusion](#conclusion) | [Miy26-U008 AP18 interface](../literature/Miy26/Yin_U004.md#miy26-u004) | AP18 Theorems 7.2.8 and 7.3.2 only: finite-tracial closed affiliated star algebra with closure of sums/products, and the actual L2-affiliated identification, applied also to M tensor M opposite. |
| [Conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 with the original selfadjoint reference core and its actual conjugate system, giving Delta(h,S)=2. No actual target vacuum is inferred from reference maximality. |
| [Conclusion](#conclusion) | [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) | Theorem 3.1 for full linear square matrices and the finite-trace adjoint-kernel equality, followed by the affiliated inverse interface, to prove diffuseness of h to the one-half S h to the one-half. No bounded inverse estimate is imported. |

## Actions, generation and the affiliated inverse

Under the displayed identification with L2(M tensor M opposite), the outer action by a and b is left multiplication by a tensor b opposite: the second factor becomes v b.
Right multiplication by a fixed affiliated coefficient consequently commutes with all outer actions.
This verifies the derivation convention in (4); it is different from the left coefficient acting on an unknown derivative in Section 3.

The imaginary part of Y is hSh.
The bounded functions (h+epsilon) inverse are in W*(h,Y), and their two-sided compression of hSh is e_epsilon S e_epsilon.
The factors e_epsilon are contractions converging strongly to 1 because h is positive regular.
These uniformly bounded compressions converge strongly to S.
Thus the target pair generates M, and A_X is dense in H.
This uses only bounded von Neumann functional calculus and applies no unknown target derivation to an inverse or to S.

Each summand S tensor b opposite and b tensor S opposite is selfadjoint affiliated, by joint spectral calculus of the separate tensor legs.
Their closed affiliated sum is selfadjoint by the finite-tracial affiliated star-algebra adjoint rule.
Its resolvent R is therefore an actual bounded element of N with norm at most one.
This conclusion concerns the closed affiliated sum, not an unspecified raw sum domain.

The opposite order gives (S tensor b opposite)B=Sh tensor 1 and (b tensor S opposite)B=1 tensor (hS) opposite.
Hence F=(Q+i)B and its affiliated inverse is B inverse times R, in precisely that order.
Positive regular h makes B affiliated-invertible; the selfadjoint resolvent gives invertibility of Q+i.
This proves regularity of the bounded F without asserting boundedness of F inverse.

The two maps in (4), initially on A_0 into L0(N), are represented derivations because each correction multiplies on the right.
Direct differentiation yields F, F-2iB, C and C_- as stated.
In particular the starred Y value is 1-2iR=(Q-i)(Q+i) inverse, a unitary.
The h-coordinate starred value is C_- minus kC, also bounded.
Finite Leibniz expansions in h,Y,Y* now prove that both restricted derivations have bounded N values.
No coarse-L2 premise for beta is needed.

## The target relation and regularity of its left coefficient

The actual polynomial relation hWZ=ZWh has both sides equal to hShShSh.
For the difference zeta of two derivations with the same prescribed h,Y values, zeta(W)=q/2 and zeta(Z)=i q/2, where q=zeta(Y*).
Its differentiated relation is exactly Kq=0 with K in (12).
All differentiations occur within A_X.

The factorization (13) was checked with opposite multiplication.
Conjugation of the first two K terms by P_0 inverse gives A_2-A_1.
The hW term gives A squared h inverse tensor h inverse opposite, equal to A_1 squared B inverse.
The Wh term gives h inverse tensor (h inverse A squared) opposite, equal to A_2 squared B inverse.
Therefore

\[
P_0^{-1}KP_0^{-1}=-(A_1-A_2)
 +i(A_1-A_2)(A_1+A_2)B^{-1}.
\]

Factoring on the displayed side and then multiplying back gives K=iP_0(A_1-A_2)(T+iB)P_0 inverse.
Independently, P_0 F P_0 inverse=T+iB.
The argument commutes only A_1 with A_2; it never commutes B with either.

The original selfadjoint reference derivations and actual conjugate vectors meet ACSY24 Proposition 3.5 on the whole represented star core, so their Delta is 2.
For each scalar lambda, the formal linear matrix in (14) is full: choose scalar h,s with sh-lambda nonzero, making its scalar evaluation have rank two.
A factorization through dimension one would have scalar evaluation rank at most one, a contradiction.
This checks the exact full-linear premise of MSY23 Theorem 3.1.

That input gives zero kernel for the bounded evaluated matrix.
In the finite tracial matrix algebra its adjoint kernel also vanishes, so the evaluated matrix is invertible in the affiliated matrix algebra.
Taking the Schur complement at regular h gives affiliated invertibility of S-lambda h inverse.
Multiplication by h gives regularity of Sh-lambda.
The affiliated similarity by h to the one-half gives regularity of A-lambda.
Since A is bounded selfadjoint, this excludes every spectral atom of its law.

The trace law of A_1,A_2 is the product of this diffuse law with itself.
The diagonal spectral projection is zero, proving regularity of A_1-A_2 in N.
The other factors in (13) are affiliated-invertible, so K is affiliated-invertible.
Multiplication by its inverse forces q=0 for every q in L0(N).
Thus both coordinate prescriptions have exactly the constructed derivation on A_X, not merely uniqueness within a selected construction or Hilbert class.

This conclusion does not extend to arbitrary linear maps M to H.
Such maps have not been represented as affiliated elements of N, and K inverse has no defined action on that whole class.
The candidate keeps this distinction explicit.

## Exact actual-adjoint criterion

For p in A_X, both delta_Y(p) and C are bounded elements of N.
Cyclicity of its finite trace identifies the correction vacuum pairing with the pairing of C* against delta_Y(p).
The reference partial_h vacuum is valid on this subalgebra.
Under the second-variable-linear convention this gives exactly

\[
\langle1,\theta_h(p)\rangle
 =\langle\xi_h,p\rangle-\langle C^*,\delta_Y(p)\rangle.
\]

The first functional on the right is already bounded in the H norm.
Hence the left functional is H-bounded if and only if the second is H-bounded.
Density of A_X proves the equivalence of the two actual adjoint memberships, with theta_h*1=xi_h-delta_Y*C*.
The other target coordinate has an actual vacuum precisely when 1 belongs to Dom delta_Y*.

Every Hilbert-tensor-valued candidate derivation embeds in the coarse affiliated algebra through the accepted L2 identification.
The preceding uniqueness therefore applies to any proposed ACSY witnesses.
This proves the converse direction of (6) at the existential level; the forward direction uses the constructed restrictions and their two actual adjoint memberships.
It is not merely a statement about one chosen candidate's formal moments.

The source coefficient C contains S, which need not be in the target star algebra.
The usual tensor-adjoint formula for target algebra coefficients therefore cannot infer C* membership from vacuum membership alone.
Similarly beta need not belong to coarse L2, so no formal partial_S*(beta*) expression is substituted for an actual adjoint-domain test.
The two remaining tests are preserved as genuine conditions, not proved automatically by this reduction.

## Arbitrary bare witnesses and Hilbert-Schmidt uniqueness

For any bare E on all M, products by the bounded factors preserve its actual domain.
Expanding its commutator with ShS+i hSh, using [E,h]=0, gives Sh V+V hS+i hVh=P.
Sandwiching by left h to the one-half gives exactly (8) for U=h to the one-half V h to the one-half.
No continuity, adjoint or Hilbert-Schmidt premise is needed for this necessary equation.

On S2(H), left and right composition by selfadjoint A are commuting selfadjoint bounded operators, so mathcal T is selfadjoint.
The positive operator mathcal B has square root given by composition with h to the one-half on both sides.
It is injective: h to the one-half is injective with dense range, and a Hilbert-Schmidt operator is bounded.
Taking the imaginary part of the homogeneous equation therefore yields norm(mathcal B to the one-half U) squared equal to zero, and U=0.

An equation stated initially on dense M is an equality of bounded operators whenever U is Hilbert-Schmidt, so this Hilbert-Schmidt inner-product test is legitimate.
It proves at most one solution in that class for arbitrary selfadjoint S; it does not show that a bare witness's U belongs to that class.

## Positive-reference actual range construction

Under S>=c1, A>=ch and A is positive regular.
Define X* on Ran A to the one-half by X*(A to the one-half z)=h to the one-half z.
The inequality gives norm at most c to the power -1/2, and regularity makes the source range dense.
Its bounded extension and adjoint yield the actual equality A to the one-half X=h to the one-half on all H.
This is an actual range factorization, with no use of an everywhere-defined formal A inverse.

The primary [Douglas paper](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf), printed pages 413-414, was checked at Theorem 1 and the proof of majorization implying factorization.
These match the reproduced bounded-factor proof and its norm.
The unbounded-operator Theorem 2 is not used.
The local proof is complete, so this is source attribution rather than a new unresolved theorem premise.

The joint multiplier sqrt(st)/(s+t) is bounded by one-half on the positive spectral quadrant, with the stated zero value at the origin.
Thus mathcal Q is a genuine bounded operator and mathcal T mathcal Q equals composition by A to the one-half on both sides.
In the product with mathcal D=L_X R_(X*), right composition reverses order: the right factor becomes X* A to the one-half, exactly the adjoint of A to the one-half X.
Consequently mathcal T J=mathcal B to the one-half with norm(J)<=1/(2c), as in (18).

The positive regular A makes mathcal T injective; for example its quadratic form is the sum of the squared Hilbert-Schmidt norms obtained by composing with A to the one-half on either side.
The displayed bounded identity therefore proves the full actual range inclusion and identifies J with mathcal T inverse times mathcal B to the one-half on every Hilbert-Schmidt input.

Taking the adjoint of that identity gives J* mathcal T=mathcal B to the one-half.
Thus C_0=mathcal B to the one-half J=J* mathcal T J is bounded positive, without any presumed commutation of J and mathcal T.
Its resolvent I+iC_0 has inverse norm at most one.
Direct multiplication then gives

\[
(\mathcal T+i\mathcal B)J
 =\mathcal B^{1/2}(I+iC_0).
\]

Applying this to the stated inverse and to P proves the actual solution formula (19).
Since P has Hilbert-Schmidt norm one, the solution norm is at most 1/(2c).
The previously proved homogeneous uniqueness applies.
This does not undo the singular h sandwich or construct a full-domain dual, and the candidate makes no such inference.

## Source and result limits

All three direct dependency scopes are matched to the required hypotheses.
AP18 is used only through its accepted finite-tracial affiliated-algebra and L2 identification interfaces; the candidate does not transfer statements specific to factors or bounded inverses.
ACSY24 is applied to the original finite-Fisher pair, and MSY23 to the explicitly verified full linear pencil.
Their recorded original-proof and edition boundaries remain unchanged.
The new Douglas source check covers only the bounded factorization theorem and the displayed proof step.

The already corrected display command in (6) changes no mathematical content.
No result from unrelated derivation-extension literature, symmetric projective tensor arguments or diagnostic finite models is a premise.
This review supplies no claim that the nonlinear ACSY tests hold automatically, that any A/F/S implication is settled for this tuple, or that all bare witnesses are determined by the affiliated or Hilbert-Schmidt uniqueness arguments.

## Conclusion

The complete statement and argument of C_F0142 v1 pass this independently organized review.
No mathematical gap, omitted direct input, affiliated-order error, actual-domain mismatch or unresolved source-interface issue was found.
This finding supports proved / independently reviewed when adopted by the responsible Claim decision.

The supported conclusions are the exact nonlinear represented-derivation construction and uniqueness, the two actual-adjoint tests equivalent to existential A, the necessary equation for every bare witness, and the separately scoped Hilbert-Schmidt uniqueness and positive-S solution.
The remaining actual-adjoint tests and dual-existence implications remain open in this material.
