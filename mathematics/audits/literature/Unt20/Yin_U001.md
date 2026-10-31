---
author: Yin
---

<a id="unt20-u001"></a>
# Unt20-U001: Reading Map of the Attempted Rationality Proof

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Source/version: [Unt20](../../../literature/pdf/Unt20.pdf), the four-page user-supplied manuscript. |
| source-locator | Printed pages and PDF pages both run from 1 to 4. |
| inspection | Coverage: **Read**, all four pages, with selected algebra checks and the open steps below. |

- Source/version: [Unt20](../../../literature/pdf/Unt20.pdf), the four-page user-supplied manuscript.
  Printed pages and PDF pages both run from 1 to 4.
- Trigger/intended use: user request on 2026-09-08 to understand and organize the manuscript's attempted proof paths in connection with [Yin_T_F0001](../../../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
- Coverage: **Read**, all four pages, with selected algebra checks and the open steps below.
  This is a reading map, not certification of a complete proof or acceptance of a new theorem.
- Reading/review: primary agent read the complete extracted text and all four rendered pages; separate AI readers the representation-formula reviewer (pp. 1-2) and the integration-formula reviewer (pp. 3-4) checked the corresponding formulas and route interpretations.
- Access/search boundary: local manuscript only; public release is unverified.
  No manuscript text or derived query was sent to a public search or external service.
  No external source theorem or original proof was newly inspected.

## Source Setting and Missing Context

The opening discusses formal noncommutative rational functions and their linear representations.
It then assumes an operator tuple X with \(\Delta(X)=d\), leaves possible additional assumptions open, and considers \(Y\in L^2(M)\) in the domain of each \(\partial_k\).

The four pages do not define Delta, the precise closed-derivation domains, the term "regular" used on p. 4, or the referenced "Conjecture 2.1."
That conjecture is not included in the supplied artifact.
These omissions must remain visible: the source's setting is not automatically identical to [Yin_C_F0001](../../../claims/Yin_C_F0001_v1.md#yin_c_f0001).

For readability below, write Z for the element whose rationality is sought, use N for the number of derivative factors, and use F for a candidate reconstructed rational function.
This avoids the source's reuse of Y as both a target element and a generator in Example 2, and of r as both a family and its size.
Superscript T means transpose, not adjoint.

## Starting Identity: Derivatives of a Linear Representation

On p. 1, take

\[
F=uA^{-1}v,\qquad A=A_0+\sum_{k=1}^d A^{(k)}x_k,
\qquad r=uA^{-1},\quad l=A^{-1}v,
\]

with scalar row/column vectors u,v and a full linear matrix A over the free polynomial algebra.
Applying the inverse rule gives the source's equation (1):

\[
\partial_kF=-\sum_{i,j}a^{(k)}_{ij}r_i\otimes l_j.
\]

The intended reversal begins with a common finite family g and scalar coefficient matrices:

\[
\partial_kZ=\sum_{i,j=1}^N\alpha^{(k)}_{ij}g_i\otimes g_j,
\qquad g_i\in L^2(M),\qquad k=1,\ldots,d.
\]

The family g represents the derivatives.
The missing step is to give this family enough structure to reconstruct Z, rather than assuming it already constitutes the left and right families of a linear representation.
The source mentions the characterization of minimal representations by linear independence of both families, but does not turn that fact into a reconstruction argument or cite its proof.

## 1. If g_i Could Be Left and Right Families

Source: Section 1, pp. 1-2, including Example 1.

Set \(A^{(k)}=-\alpha^{(k)}\).
The derivative data now fix all variable coefficients of A.
Try to choose a scalar constant matrix A_0 so that

\[
u=gA(X),\qquad v=A(X)g^T
\]

are scalar-valued vectors and A is full.
If the inverses, evaluations, and derivation rules involved are valid, these identities would make g the evaluated right family and g^T the evaluated left family.
Then \(F=uA^{-1}v\) would satisfy \(\partial_kF(X)=\partial_kZ\).

**What Example 1 establishes about the attempt.**
The derivative of x is \(1\otimes1\).
With the enlarged family \(g=(1,X)\), the proposed scalar-vector conditions can be solved using

\[
A=\begin{pmatrix}a-x&1\\1&0\end{pmatrix}.
\]

But the same derivative admits the smaller family g=(1).
This forces A=a-x and u=v=a-X, which are not scalar for a non-scalar X.
Thus an arbitrary given derivative-factor list need not contain all the components needed for the proposed linear representation.
The example does not refute rationality of the target and does not rule out enlarging or replacing the list.

**Unresolved step.**
There is no general procedure in the manuscript for selecting/enlarging the family, constructing A_0, or proving fullness and valid evaluation.

## 2. If g_i Could Be Rational Functions

Source: Section 2, pp. 3-4, including Example 2.

The second attempt drops the demand that u,v be scalar.
Instead, suppose the g_i can be chosen as evaluations of rational functions.
Form

\[
F(X)=gA(X)g^T.
\]

Now choose \(A^{(k)}=+\alpha^{(k)}\).
With the derivation module actions understood, the product rule is the source's equation (3):

\[
\partial_kF(X)=\partial_kZ+E_k,\qquad
E_k=(\partial_kg)v+u(\partial_kg^T),
\quad u=gA(X),\quad v=A(X)g^T.
\]

The proposed task is to choose A_0 so that every E_k vanishes.
Rationality of the factors would make F a rational candidate, subject to evaluation/domain issues.
Because this construction does not invert A, fullness of A is not itself needed to form gAg^T; the manuscript's final fullness remark is not a substitute for the missing cancellation argument.

For the derivative of x, g=(1) now works: A=a+x gives F=a+x and no derivative cross terms.
For xy, the source uses g=(1,X,Y).
These factors represent both derivatives, but omit the product XY.
The scalar-vector requirement from the first attempt fails because the first entries of u and v contain -XY.
The second construction illustrates cancellation of the cross terms in this particular example; its printed matrix uses the negative coefficient convention and produces \(F=a_{11}-xy\).
See the sign notes below.

**Unresolved steps.**
The rationality of the g_i is assumed, not obtained from finite-tensor derivatives.
The existence of a suitable A_0 for general rational g is also not established.
For merely L2 factors, products, derivation domains, and membership of the candidate in the desired ambient algebra require additional justification.

## 3. More General Case: A Rational-Factor Intermediate Condition

Source: Section 3, p. 4.

The source proposes, rather than proves, equivalence of:

1. Z is "regular" (undefined in this artifact).
2. Every relevant derivative admits a finite decomposition using a common family of L2 vectors.
3. Every relevant derivative admits such a decomposition using a common family of rational functions whose evaluations lie in L2(M).

Read (2) and (3) as requiring Z to lie in all the relevant derivation domains and one finite family that works for all k; the source's prose is informal.
Condition (3) implies (2) by forgetting the extra property of the witnesses.
The reverse implication is the proposed rational-factor extraction step, not a supplied theorem.
Even after obtaining (3), reconstruction or integration is still required to reach (1).

The last paragraph worries that a rational target may have decompositions involving nonrational g_i, including arbitrary factors attached to zero coefficients.
This explains why one cannot infer rationality of every supplied factor.
It does **not** contradict the existential formulation of (3): the desired conclusion is that some rational-factor decomposition exists, not that every decomposition is rational.
The source supplies no general mechanism for finding one.

## Formula Notes Needed for a Faithful Reading

These are checks of the displayed examples, not counterexamples to Yin_C_F0001 or completed repairs of the general routes.

| Locator | Printed issue | Reading consequence |
| --- | --- | --- |
| p. 2, Example 1, final two-dimensional representation | With the displayed A and the newly defined u=gA, v=Ag^T, one gets u=(a,1), v=(a,1)^T and F=x+a; the source writes x-a. Keeping the original u=(0,1), v=(0,1)^T instead would give x-a. | Preserve the new definitions when reconstructing the example. Both expressions have derivative 1 tensor 1, so the substantive obstruction is unchanged. |
| pp. 3-4, Example 2 | Equation (3) adopts positive variable coefficients, but the example uses A_13=a_13-x and A_21=a_21-y. After the stated cancellation it obtains F=a_11-xy. | Under that matrix convention the reconstructed derivative is the negative of the target derivative; negate the resulting F to match it. The example is not a verification of the positive-sign formula as printed. |
| p. 4, expanded derivative with respect to Y | The last term is printed as -partial_X Z, while the preceding unexpanded line is -partial_Y Z. | The last term should be -partial_Y Z. |

## Interfaces Still Needed for Yin_T_F0001

The manuscript directly studies finite-tensor derivatives and rational reconstruction.
To make it a proof of Yin_C_F0001, the following interfaces would have to be supplied, with the normal-generator hypotheses retained:

1. **Commutator to derivative:** the subsequent [Yin_C_F0002 audit](../../../claims/Yin_C_F0002_v1.md#yin_c_f0002) supplies the polynomial identity and an exact finite-tensor formulation for arbitrary bounded f when the derivative is defined on its maximal bounded HS commutator domain.
   The manuscript does not specify whether its derivative uses this domain.
   Identifying it with a minimal polynomial closure is a separate issue and, for the holomorphic polynomial core in the Haar example, is false.
   No Delta assumption is needed for Yin_C_F0002's formula.
2. **Finite data to reconstruction:** justify one of the two constructions, or another integration argument, without assuming rationality of the target.
   A chosen factor list's failure is only failure of that construction.
3. **Equality up to constants:** after matching all derivatives, justify a common-kernel result strong enough to conclude that f-F(X) is scalar (or otherwise belongs to the required rational algebra).
   Equal derivatives alone do not supply this conclusion in an unspecified domain.
4. **Exact rational closure:** distinguish formal matrix inversion, an affiliated evaluation, bounded evaluation, and membership in the scalar division closure inside M.
   Fullness of a formal pencil and even boundedness of its scalar output do not by themselves supply the particular bounded-inverse construction required by Yin_C_F0001.
   This reading establishes no conversion between these notions.

These are obligations for transferring the source attempt to the project, not new hypotheses silently added to Yin_C_F0001.

## Assessment and Handoff

The useful content is a proposed reverse passage from finite derivative data to a finite linear representation, with two concrete failures of treating the derivative factors as a complete representation family, and an existential rational-factor condition offered as an intermediate target.
The general reconstruction and the remaining interfaces to Yin_C_F0001 are unresolved; the exact commutator/finite-factor interface is now supplied by Yin_C_F0002 under its specified derivative convention.

The candidate is registered as [Yin_S_F0001](../../../strategies/Yin_S_F0001.md#s_f0001), with disposition proposed.
The initial reading task supplied no project theorem or general counterexample and did not constitute a full source audit, formal verification, external human review, or novelty assessment.
The subsequent user-requested formula audit is a separate project result, Yin_C_F0002.

Final reading-record review, 2026-09-08: the representation-formula reviewer independently inspected this integrated note and Yin_S_F0001 against the supplied manuscript and the recorded Yin_C_F0001 scope.
No correction was requested to the route mapping, example notes, existential interpretation, or verification boundaries.
This was a review of the source reading and its presentation, not a proof review of Yin_C_F0001.

Dated correction after the next user instruction, 2026-09-08: the initial reading listed the commutator-to-derivative passage too broadly as unresolved.
Yin_C_F0002 proves the algebraic formula, the exact finite-factor correspondence for the maximal bounded derivative, and the forward rationality implication.
What remains unspecified in Unt20 is its chosen closed-derivative domain, not the existence of this concrete dual-system formula.
The previous reading review does not replace Yin_C_F0002's separate mathematical audit.
