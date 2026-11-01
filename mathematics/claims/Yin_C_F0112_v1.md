---
author: Yin
---

# Bounded division closure for two free square-zero matrix-unit algebras

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Bounded rational reconstruction for two free square-zero matrix units

<a id="statement"></a>

Kind: Claim/proof module.
Date: 2026-09-16.
Human record author: Yin.
Argument developed by a research subagent with coordinator feedback.
Consumer: [Yin_T_F0007_v1](../tasks/Yin_T_F0007_v1.md#decision-candidate-0001).
Canonical research metadata owns the current mathematical and review assessments.
This restricted result does not complete the general Task contract.

<a id="free-square-zero-bounded-closure"></a>
## 1. Exact setting and conclusion

Let
\[
 (M,\tau)=(M_2(\mathbb C),\operatorname{tr}_2)*
             (M_2(\mathbb C),\operatorname{tr}_2)
\]
be the reduced tracial von Neumann free product, with faithful normal probability trace.
Write
\[
 x=e_{12}^{(1)},\qquad y=e_{12}^{(2)},\qquad
 A_1=\mathbb C1+\mathbb Cx,\quad
 A_2=\mathbb C1+\mathbb Cy,\quad
 A=\mathbb C\langle x,y\rangle.
\]
The proposed restricted conclusion is
\[
 \boxed{\operatorname{Div}_{L^0(M)}A\cap M
          =\operatorname{Div}_M A.}                 \tag{1}
\]
Both closures use only scalar inverses in their specified ambient algebras.
In particular, adjoints are not adjoined to A.
Both input algebras are proper non-star subalgebras of their full matrix factors, so the previously accepted full-star-factor result C_F0106 does not itself imply (1).

The T_F0007 hypotheses hold for each input: x and x* give all matrix units, so W*(A_1)=M_2(C), and likewise for y.
Every alpha 1+beta x is invertible in M_2(C) exactly when alpha is nonzero; its inverse is alpha^{-1}1-beta alpha^{-2}x.
Since L^0(M_2(C))=M_2(C), both division closures of A_1 equal A_1, and the same holds for A_2.
Thus this is an actual test of the original permanence question.

## 2. Reuse, source scope and search boundary

The following existing inputs were read before the corresponding proof investment.

- [T_F0007](../tasks/Yin_T_F0007_v1.md) and [Yin_S_F0016](../strategies/Yin_S_F0016.md) specify the original non-star input requirement.
- [C_F0106](Yin_C_F0106_v1.md) and its [independent review](../audits/reviews/Yin_R_F0116_v1.md#original-f0043-account) establish the full finite-dimensional star case and identify the descent limitation.
- [C_F0087](Yin_C_F0087_v1.md#yin_c_f0087), with its independently reviewed status, supplies the single-operator coprime numerator-denominator Bezout cancellation.
  Its inspected Hun74 input is retained, rather than re-registered as a new algebraic result.
- [CK14-U001](../audits/literature/CK14/Yin_U001.md#ck14-u001), also used in [C_F0100](Yin_C_F0100_v1.md#yin_c_f0100), gives the exact two-free-projection support and intersection formula.
  At traces 1/2, every character intersection vanishes and the generic parameter has support [0,1].
  These previously checked formulas are the only free-projection spectral inputs below.
- [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004), Lemmas 5.1-5.5, gives injectivity iff affiliated invertibility in a finite tracial von Neumann algebra, also in corners and matrix amplifications.
- [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005), the audited and repaired Lemma 5.19 on published p. 38, gives sum_j tau(p_{ker(T-lambda_j)}) <=1 for distinct eigenvalues of an affiliated T.
  This lemma itself requires no maximal-Delta hypothesis; the ambient unit's later rational-matrix applications have stronger hypotheses that are not imported here.
- [DR97-U004](../audits/literature/DR97/Yin_U004.md#dr97-u004), Lemma 11, already gives adjoint-free bounded scalar elimination when a finite state matrix has powers tending to zero.
  Thus the use of B*B in C_F0106 is not an essential new obstruction once a stable original-alphabet realization is known.
  The proof below instead uses a central four-dimensional rational algebra and does not invoke a finite-state realization.

A targeted method-index read found only entries whose recorded examples concern other structural questions; their scope discipline was useful, but neither supplies a mathematical premise here.
Local searches for nilpotent, square-zero, proper non-star, and triangular inputs did not locate this two-matrix-unit conclusion.
Bounded primary-web searches on 2026-09-16 for free nilpotent Brown measures, free E12/F12 pairs, two square-zero generated algebras, and nonselfadjoint division closures found related source pages but no theorem used in this proof.
A point-spectrum source search was superseded by finding the exact existing MSY23 Lemma 5.19 audit.
No new external theorem or full-source audit, and no novelty claim, results from these searches.

All unbounded products below are products in L^0(M), with its closed affiliated realizations.
Ordinary Hilbert-space kernel arguments are used only for bounded operators or after explicitly assuming an affiliated expression is bounded.

## 3. Actual affiliated inverses and an unbounded idempotent

Put
\[
 p=xx^*,\quad q=yy^*,\quad s=x+y,\quad
 t=s^2=xy+yx.                                      \tag{2}
\]
Both p and q are projections of trace 1/2, and they are free.
The matrix-unit relations give
\[
 x^2=y^2=0,\quad x^*x=1-p,\quad y^*y=1-q,\quad
 \ker x=pH,\quad \ker y=qH,
\]
where H=L^2(M,tau).
The CK14 interface gives
\[
 p\wedge q=0,\qquad \|pq\|=1.                    \tag{3}
\]
For the norm assertion, the same interface identifies the generic pqp compression with the parameter on support [0,1], so its norm is 1 and ||pq||^2=||pqp||=1.
This statement does not say that the endpoint is an eigenvalue.

If s xi=0, then x xi=-y xi lies in pH intersect qH, hence is zero by (3).
Thus xi lies in ker x intersect ker y=pH intersect qH and is zero.
The finite-trace injectivity interface shows that s is invertible in L^0(M).
Therefore t=s^2 is invertible there too.

The identities x^2=y^2=0 give tx=xt=xyx and ty=yt=yxy; hence t commutes with x,y.
Define
\[
 e=xy\,t^{-1}\in\operatorname{Div}_{L^0(M)}A.
\]
Then
\[
 (xy)^2=txy,\qquad e^2=e,\qquad ex=x,\qquad ey=0. \tag{4}
\]
For example, ex=xyx t^{-1}=tx t^{-1}=x, with commutation with t^{-1} justified by the preceding commutation with t.

The idempotent e is unbounded.
If it were bounded, right multiplication of ex=x by x* and of ey=0 by y* would give ep=p and eq=0 as identities of bounded operators.
Since ||qp||=1, choose unit vectors xi_k in pH with ||q xi_k|| tending to 1.
Orthogonal projection gives
\[
 \|\xi_k-q\xi_k\|^2=1-\|q\xi_k\|^2\longrightarrow0,
 \qquad e(\xi_k-q\xi_k)=\xi_k,
\]
contradicting boundedness of e.
Consequently t^{-1} is unbounded, since otherwise e=xy t^{-1} would be bounded.
The same argument implies that s^{-1} is unbounded.

Thus the natural singular inverses exist, but their associated idempotent does not supply a counterexample to (1).
Its unboundedness will instead rule out the remaining possible singular coefficient.

## 4. Every nonzero central polynomial has an actual affiliated inverse

For unit complex numbers u,v, the factor inner automorphisms induced by diag(u,1) and diag(v,1) extend to a trace-preserving free-product automorphism alpha_{u,v} with
\[
 \alpha_{u,v}(x)=ux,\quad\alpha_{u,v}(y)=vy,
 \quad\alpha_{u,v}(t)=uvt.                         \tag{5}
\]
For completeness, the extension is implemented on the reduced free-product Hilbert space by applying the factor trace-preserving unitaries to each centered tensor letter and fixing the vacuum; it intertwines the left factor actions.
It therefore preserves the represented von Neumann algebra and trace.
Its unitary conjugation also extends to L^0(M).

For lambda nonzero, let delta=tau(p_{ker(t-lambda)}).
Equation (5) implies that every point on the circle of radius |lambda| has the same kernel trace delta.
Choosing arbitrarily many distinct such points and applying the existing MSY23 Lemma 5.19 gives N delta<=1 for every N.
Hence delta=0, and faithfulness gives ker(t-lambda)=0.
For lambda=0, injectivity was already proved in Section 3.

Every nonzero polynomial Q in C[z] factors into nonzero scalar and factors z-lambda.
Thus Q(t) is invertible in L^0(M), as a finite product of actual affiliated units.
In particular t is algebraically transcendental, and the evaluation
\[
 K=\mathbb C(z)\longrightarrow L^0(M),\qquad
 r\longmapsto r(t)
\]
is an injective field homomorphism.
This asserts nothing about normality of t or about its bounded spectrum.
Throughout the proof, central means central in the algebra generated by x,y, not central in M.

## 5. The entire affiliated scalar closure has four rational coefficients

The alternating words in x,y are linearly independent: they are nonzero orthogonal reduced free-product tensors, since x and y are centered and each has nonzero L^2 norm.
Every word containing xx or yy vanishes.
The relations imply, for k>=1,
\[
 (xy)^k=t^{k-1}xy,\qquad
 (yx)^k=t^k-t^{k-1}xy,
\]
and, for k>=0,
\[
 (xy)^k x=t^k x,\qquad (yx)^k y=t^k y.
\]
Consequently A is a free C[t]-module with basis 1,x,y,xy.
Independence follows by comparing the odd alternating words, the even words starting with y, the vacuum coefficient, and then the remaining even words starting with x.

Consider its central localization
\[
 L=\{a(t)+b(t)x+c(t)y+d(t)xy:a,b,c,d\in K\}
       \subset L^0(M).                            \tag{6}
\]
All denominators in (6) are actual affiliated units by Section 4; clearing a common central denominator preserves the above independence.
The relations make L an algebra.
Abstractly it is M_2(K), by
\[
 x\longmapsto E_{12},\qquad
 y\longmapsto zE_{21},\qquad t\longmapsto zI_2.
                                                               \tag{7}
\]
Indeed the four displayed basis elements become a K-basis of M_2(K), and their multiplication relations agree.

If f in L is invertible in L^0(M), its image under (7) cannot be a singular matrix over K: a singular matrix has a nonzero right-annihilated matrix over K, whose inverse image would be a nonzero g in L with fg=0.
Hence its matrix inverse exists over K and belongs to L; under the faithful embedding into L^0(M), it is the actual inverse of f.
Thus L is scalar inverse closed in L^0(M).
Conversely, every element of L is constructed from A by adjoining the scalar inverses Q(t)^{-1}.
We have proved
\[
 \operatorname{Div}_{L^0(M)}A=L.                  \tag{8}
\]
The abstract matrices in (7) are an algebraic coordinate calculation; no unbounded change of Hilbert-space basis or unitary diagonalization is asserted.

## 6. A bounded corner forces the reduced scalar denominator to be boundedly invertible

For r in K, the following implication is the critical analytic step:
\[
 r(t)x\in M\quad\Longrightarrow\quad
 r(t)\in\operatorname{Div}_M\mathbb C[t].          \tag{9}
\]
The same holds with y replacing x.

Use the matrix units x,x*,p,1-p from the first factor to identify M with M_2(N), where N=pMp has its normalized faithful trace.
Since t commutes with x=E_{12}, it has the form
\[
 t=\begin{pmatrix}c&h\\0&c\end{pmatrix},\qquad c,h\in N.
                                                               \tag{10}
\]
This uses only the commutation equation: if the four blocks of t are c,h,k,l, then tE12=E12t gives k=0 and l=c.
Neither c nor h is assumed normal or commuting.

Take a reduced representation r=P/Q with coprime polynomials P,Q; the zero rational function is immediate.
The bounded polynomial Q(t) has the form
\[
 Q(t)=\begin{pmatrix}Q(c)&h_Q\\0&Q(c)\end{pmatrix},\qquad h_Q\in N.
\]
It is injective by Section 4.
A vector in ker Q(c), placed in the first matrix coordinate, would lie in ker Q(t); hence Q(c) is injective and has an affiliated inverse in L^0(N).
The explicit upper-triangular inverse formula in the affiliated matrix algebra shows that the diagonal entries of r(t) are r(c), and therefore
\[
 r(t)x=\begin{pmatrix}0&r(c)\\0&0\end{pmatrix}.
\]
The assumed boundedness of r(t)x implies r(c) in N.

The C_F0087 Bezout mechanism now applies in the corner: choose U,V in C[z] with UP+VQ=1 and multiply the evaluated identity on the right by Q(c)^{-1}.
This gives
\[
 Q(c)^{-1}=U(c)r(c)+V(c)\in N.                    \tag{11}
\]
Consequently the actual inverse
\[
 Q(t)^{-1}=
 \begin{pmatrix}
 Q(c)^{-1}&-Q(c)^{-1}h_Q Q(c)^{-1}\\
 0&Q(c)^{-1}
 \end{pmatrix}                                  \tag{12}
\]
is bounded in M.
In particular its off-diagonal entry is explicitly controlled by three bounded factors.
Hence r(t)=P(t)Q(t)^{-1} belongs to the bounded scalar division closure of C[t], proving (9).

This is stronger than merely observing bounded diagonal entries.
That observation alone would not control a nonnormal upper-triangular rational expression.
Equation (11), which uses both coprimality and the actual regularity of Q(c), supplies the missing denominator bound and makes (12) legitimate.
The case with y uses the second factor's matrix units and the same commutation with t.

## 7. Recovering all four coefficients using bounded operations

Take a bounded f in the left side of (1).
By (8), write it uniquely as
\[
 f=a(t)+b(t)x+c(t)y+d(t)xy.                        \tag{13}
\]
Let omega be a primitive third root of unity and use the automorphism alpha=alpha_{omega,omega^{-1}} from (5).
It fixes t and xy, multiplies x by omega, and y by omega^{-1}.
The three finite Fourier averages of f,alpha(f),alpha^2(f) therefore give separately
\[
 f_0=a(t)+d(t)xy\in M,\qquad b(t)x\in M,\qquad c(t)y\in M.
                                                               \tag{14}
\]
Only a finite linear combination of bounded operators is used; no boundedness of the individual rational coefficients was assumed.
By (9), b(t) and c(t) already belong to Div_M C[t].

Since x^2=0 and t commutes with x,
\[
 xf_0=a(t)x.
\]
The left side is bounded, so (9) gives a(t) in Div_M C[t].
Thus
\[
 g=f_0-a(t)=d(t)xy\in M.
\]
Multiplication on the right by x gives
\[
 gx=d(t)xyx=t\,d(t)x.
\]
Apply (9) once more to E(z)=z d(z).
The result is not only that E(t) is bounded, but that for its reduced expression E=P/Q the operator Q(t) has a bounded inverse, by (11)-(12).

Because t^{-1} is unbounded, Q(0) is nonzero.
Indeed, if Q(z)=zQ_1(z), the commutation of these polynomial factors and Q(t)^{-1} gives
\[
 t^{-1}=Q_1(t)Q(t)^{-1}\in M,
\]
contradicting Section 3.
Define
\[
 \eta=E(0)=P(0)/Q(0),\qquad
 H(z)=\frac{P(z)-\eta Q(z)}{zQ(z)}.
\]
The numerator is divisible by z, so H(t) is a polynomial in t times the bounded scalar inverse Q(t)^{-1}.
Therefore H(t) belongs to Div_M C[t].
In the affiliated algebra,
\[
 E(t)=\eta+tH(t),\qquad
 d(t)=\eta t^{-1}+H(t),\qquad
 g=\eta e+H(t)xy.                                 \tag{15}
\]
Both g and H(t)xy are bounded.
Since e is unbounded, (15) forces eta=0.
Thus d(t)=H(t) also lies in Div_M C[t].

All four coefficients in (13) have now been reconstructed by bounded scalar inverses in C[t], and t=xy+yx belongs to the original A.
Hence f belongs to Div_M A.
The reverse inclusion in (1) holds because every bounded inverse is also its affiliated inverse.
This proves the proposed restricted equality.

## 8. Assessment and continuation boundary

Author checks covered the exact input closures, the factor order in ex=x and (15), the trace-half free-projection interface, the finite gauge coefficient extraction, the use of MSY23 Lemma 5.19 without a maximal-Delta premise, the injection of the central localization, and the off-diagonal control in (12).
No numerical computation, proof assistant, external human review, or independent review is claimed at authoring.

The conclusion is a nontrivial proper non-star input case of T_F0007.
It is not the full permanence statement, does not cover arbitrary proper non-star finite-dimensional input algebras, and says nothing new about diffuse inputs.
The singular affiliated idempotent e is explicitly unbounded, so it is a checked obstruction to that proposed counterexample, not a refutation of T_F0007.
The next action is independent review of the complete argument, with particular attention to Sections 4-7 and preservation of the original scalar-inversion algebra.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:03 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-bounded-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: The two proper non-star algebras generated by free 2-by-2 square-zero matrix units satisfy bounded division-closure equality; central localization and a bounded corner Bezout argument give scalar reconstruction.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:10 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-bounded-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0087_v1.md#decision-candidate-0002) | Reviewed coprime numerator-denominator Bezout cancellation, applied in the bounded corner and reproduced with explicit off-diagonal control. |
| review | [Exact material](../audits/reviews/Yin_R_F0098_v1.md) | Entire square-zero proof, actual affiliated inverses and source interfaces, fixed C_F0087 input, off-diagonal denominator control and bounded scalar reconstruction; no general T_F0007 completion. |

Recorded mathematical summary: The two proper non-star algebras generated by free 2-by-2 square-zero matrix units satisfy bounded division-closure equality; central localization and a bounded corner Bezout argument give scalar reconstruction.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:53 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-bounded-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0087_v1.md#decision-candidate-0002) | Reviewed coprime numerator-denominator Bezout cancellation, applied in the bounded corner and reproduced with explicit off-diagonal control. |
| review | [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0087-applicability) | Yin_C_F0112 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: The two proper non-star algebras generated by free 2-by-2 square-zero matrix units satisfy bounded division-closure equality; central localization and a bounded corner Bezout argument give scalar reconstruction.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-applicability

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:13 |
| status | proved |
| reason | Select the same actual applicability finding at its responsible R home, with its original date, exact per-Claim scope and known shared mathematical context, preserving statement, argument, dependencies and mathematical assessment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-bounded-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0087_v1.md#decision-candidate-0002) | Reviewed coprime numerator-denominator Bezout cancellation, applied in the bounded corner and reproduced with explicit off-diagonal control. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0103_v1.md#c-f0087-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Entire square-zero proof, actual affiliated inverses and source interfaces, fixed C_F0087 input, off-diagonal denominator control and bounded scalar reconstruction; no general T_F0007 completion.

Review: [Exact material](../audits/reviews/Yin_R_F0098_v1.md).

Material covered by that review: [Exact material](Yin_C_F0112_v1.md).

Yin_C_F0112 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0087-applicability).

Material covered by that review: [Exact material](Yin_C_F0112_v1.md).
