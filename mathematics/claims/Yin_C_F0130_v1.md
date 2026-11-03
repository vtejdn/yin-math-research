---
author: Yin
---
# Actual vacua and full-domain duals for elliptic images of unitary tuples

Date: 2026-10-14T13:19.
Human author Yin.
The acsy_to_full_domain agent developed the coordinate and adjoint-domain argument under the explicit request to continue comparing the ACSY24 derivation condition with the existence of bare full-domain duals.
Root suggested the projective-correction source and the strict scope example.
The proof below is a complete candidate; the current decision does not yet adopt an independent review.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal tracial state, H=L2(M,tau), Omega=1, and P=P_Omega.
Let U=(U_1,...,U_d) be any finite generating tuple of unitaries.
No freeness assumption is made.
Choose complex numbers alpha_j,beta_j with |alpha_j|>|beta_j| and put

\[
 X_j=\alpha_jU_j+\beta_jU_j^*\qquad(1\le j\le d).
 \tag{1}
\]

Translations X_j+c_j1 have the same conclusions.
By replacing an individual U_j with U_j*, the statement also covers |alpha_j|<|beta_j|.
The equal-modulus case is not included in the coordinate equivalence below.

For a generating tuple Y, write A(Y)=C<Y,Y*> and define two existential conditions:

- \(\mathsf A(Y)\): there are outer-bimodule derivations \(\partial_i:A(Y)\to H\otimes_2H\) such that \(\partial_i(Y_j)=\delta_{ij}1\otimes1\) and \(1\otimes1\in\operatorname{Dom}\partial_i^*\).
  This is the exact ACSY24 Proposition 3.5 condition, with actual Hilbert adjoints.
- \(\mathsf F(Y)\): there are complex-linear maps \(D_i:M\Omega\to H\) satisfying \([Y_j,D_i]=\delta_{ij}P\) on all M Omega.
  No continuity, closability or adjoint-domain premise is imposed on these supplied maps.

Then

\[
 \mathsf A(X)\ \Longleftrightarrow\ \mathsf A(U)
 \ \Longleftrightarrow\ \mathsf F(U)
 \ \Longleftrightarrow\ \mathsf F(X).
 \tag{2}
\]

In particular, the two hypotheses are equivalent for every tuple whose coordinates are nondegenerate elliptic images of generating unitaries.
This gives a class of correlated normal tuples.
It does not settle the equivalence for arbitrary correlated normal tuples.

For the implication A(U) to A(X), if xi_i is the actual vacuum vector for the chosen unitary-coordinate derivation, the constructed X-coordinate derivation satisfies the explicit bound

\[
 \|\partial_i^*(1\otimes1)\|_2
 \le \frac{\|\xi_i\|_2}{|\alpha_i|-|\beta_i|}
       +\frac{2|\beta_i|}{(|\alpha_i|-|\beta_i|)^2}.
 \tag{3}
\]

No assertion identifies arbitrary supplied full-domain operators with canonical Hilbert closures.

## Argument

### 1. Existing inputs and exact scope

The unitary equivalence A(U) if and only if F(U) is [C_F0071 v2, Part D](Yin_C_F0071_v2.md#statement), with its selected self-reviewed [R_F0044 conclusion](../audits/reviews/Yin_R_F0044_v1.md#conclusion).
The automatic operator-norm-to-L2 boundedness of every bare dual for a normal coordinate is [C_F0069, Part A](Yin_C_F0069_v1.md#statement).
Both apply without freeness.

The coefficient implementation below reuses [C_F0018, Section 1](Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma), checked in the [original R_F0064 account](../audits/reviews/Yin_R_F0064_v1.md#decisive-checks), whose initial-context relationship remains unknown.
The later [isolated C_F0018 finding](../audits/reviews/Yin_R_F0064_v1.md#projective-correction) is separate evidence, not an input to that earlier reuse act.
That argument is stated there for B(H).
Here its same bounded right-multiplier formulas are applied to B(M,H), where M has its operator norm.
This change of Banach spaces and all required identities are verified in Section 5.

The finite algebraic-coefficient adjoint interface is ACSY24 Lemma 3.3, published pp.34-35.
The exact original passage was checked together with the [existing source audit](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
Section 3 supplies the quantitative unitary-tensor test needed for the infinite series.
We do not extend Lemma 3.3 to arbitrary bounded measurable coefficients without an estimate.

The new statement concerns a different coordinate class from [C_F0071](Yin_C_F0071_v2.md#statement); Section 7 also shows that it is not contained in the bounded-division-adjoint hypothesis of [C_F0129](Yin_C_F0129_v1.md#statement).
The latter candidate is a comparison only and is not a proof dependency.
No external priority or novelty claim is made.

### 2. The common algebra and projective coefficients

Each X_j is normal.
The explicit inverse star-linear formula is

\[
 U_j=\frac{\overline{\alpha_j}X_j-\beta_jX_j^*}
 {|\alpha_j|^2-|\beta_j|^2}.
 \tag{4}
\]

Therefore A(X)=A(U)=:A, and W*(X)=W*(U)=M.
Formula (4) is not a holomorphic rational formula; both starred and unstarred coordinates are used.

Use the Banach projective tensor algebra

\[
 \mathcal B=M\widehat\otimes_\pi M^{\mathrm{op}},
 \qquad(a\otimes b)(c\otimes d)=ac\otimes db.
\]

The label op records the multiplication.
On the Hilbert coarse bimodule define the bounded inner coefficient action

\[
 I_{c\otimes d}(a\otimes b)=ac\otimes db.
 \tag{5}
\]

It commutes with both outer bimodule actions, and extends to each z in B with operator norm at most ||z||_pi.
The natural map B to H tensor_2 H is continuous; no injectivity of that completion map is assumed.

For each i set

\[
 J_i=\alpha_i1\otimes1-\beta_iU_i^*\otimes U_i^*,\qquad
 q_i=J_i^{-1}
 =\frac1{\alpha_i}\sum_{n=0}^{\infty}
       \left(\frac{\beta_i}{\alpha_i}\right)^n
       (U_i^*)^n\otimes(U_i^*)^n.
 \tag{6}
\]

This is a Neumann series in the projective norm, and

\[
 \|q_i\|_\pi\le\frac1{|\alpha_i|-|\beta_i|}.
 \tag{7}
\]

We also write q_i and J_i for their images in the coarse Hilbert space.
The images of these specific identities are justified by continuity and the displayed absolutely convergent series.

### 3. Actual adjoints at unitary tensors

Let gamma:A to H tensor_2 H be any outer derivation with actual vacuum xi=gamma*(1 tensor 1).
If v,w are unitaries in A, then

\[
 v\otimes w\in\operatorname{Dom}\gamma^*,\qquad
 \|\gamma^*(v\otimes w)\|_2
 \le\|\xi\|_2+\|\gamma(v^*)\|_2+\|\gamma(w^*)\|_2.
 \tag{8}
\]

Here the last two norms are coarse Hilbert-space norms.
To prove (8), apply the vacuum pairing to v* p w* and expand

\[
 \gamma(v^*pw^*)
 =\gamma(v^*)\cdot pw^*
   +v^*\cdot\gamma(p)\cdot w^*
   +v^*p\cdot\gamma(w^*)\qquad(p\in A).
\]

Pairing the middle term with 1 tensor 1 is exactly the pairing of gamma(p) with v tensor w.
The vacuum term is bounded by ||xi||_2 ||p||_2.
Each other term is bounded by the corresponding Hilbert tensor norm in (8) times ||p||_2: apply the appropriate trace contraction and then Cauchy-Schwarz; multiplication by v or w is an isometry.
Thus the functional p -> <v tensor w,gamma(p)> is L2-bounded on the dense domain A, proving the actual adjoint assertion and estimate.
No reality hypothesis is used.

For a unitary-coordinate derivation theta_i with theta_i(U_j)=delta_ij 1 tensor 1 and vacuum xi_i, the inverse and product rules give

\[
 \|\theta_i(U_i^{-n})\|_2\le n\qquad(n\ge0).
\]

Indeed the derivative is a sum of n tensors of unitaries, each of coarse norm one.
Therefore (8) gives

\[
 \|\theta_i^*(U_i^n\otimes U_i^n)\|_2
 \le\|\xi_i\|_2+2n.
 \tag{9}
\]

### 4. Equivalence of the actual-vacuum conditions

Assume A(X), and fix i.
Write eta_ij=partial_i(U_j).
Since U_j is unitary and belongs to the common algebra A,

\[
 \partial_i(U_j^*)=-U_j^*\cdot\eta_{ij}\cdot U_j^*,
 \qquad
 \alpha_j\eta_{ij}-\beta_jU_j^*\cdot\eta_{ij}\cdot U_j^*
 =\delta_{ij}1\otimes1.
 \tag{10}
\]

The outer action eta -> U_j* eta U_j* is unitary on the coarse Hilbert space.
Its norm-convergent Neumann inverse in (10) yields eta_ij=delta_ij q_i.
Define

\[
 \theta_i=I_{J_i}\partial_i.
 \tag{11}
\]

The inner coefficient action commutes with the outer actions, so theta_i is a derivation.
All coefficients of q_i lie in the commutative marginal algebra generated by U_i, so (6) gives I_{J_i}q_i=1 tensor 1.
Consequently theta_i(U_j)=delta_ij 1 tensor 1.

Its actual vacuum exists.
Explicitly,

\[
 \theta_i^*(1\otimes1)
 =\overline{\alpha_i}\,\partial_i^*(1\otimes1)
  -\overline{\beta_i}\,\partial_i^*(U_i\otimes U_i).
 \tag{12}
\]

The last vector exists by (8), since U_i is in A.
Thus A(U) holds.
This step uses the star-linear recovery (4) and the actual inverse derivation rule, not an unprescribed choice of partial_i(X_j*).

Conversely, assume A(U), with derivations theta_i and vacua xi_i.
Define

\[
 \partial_i=I_{q_i}\theta_i.
 \tag{13}
\]

This is a well-defined Hilbert-valued derivation by (7).
Since theta_i(X_j)=delta_ij J_i, (6) implies partial_i(X_j)=delta_ij 1 tensor 1.

To check the actual vacuum, the following vector series converges absolutely in H by (9):

\[
 \eta_i=\frac1{\overline{\alpha_i}}
 \sum_{n=0}^{\infty}
 \left(\frac{\overline{\beta_i}}{\overline{\alpha_i}}\right)^n
 \theta_i^*(U_i^n\otimes U_i^n).
 \tag{14}
\]

For every p in A, both the Hilbert tensor series (13) and the vector series (14) converge in norm.
Termwise adjoint pairing is therefore legitimate and gives

\[
 \langle1\otimes1,\partial_i p\rangle
 =\langle\eta_i,p\rangle.
\]

Hence partial_i*(1 tensor 1)=eta_i is the actual adjoint vector.
Summing the geometric series and its derivative gives exactly (3).
This completes A(X) if and only if A(U).

### 5. Projective corrections on all bounded vectors

Put B(M,H) for bounded complex-linear maps from M with its operator norm to H.
Write rho(a)xi=xi a for bounded right multiplication, and let the same notation denote its restriction to M.
For elementary z=a tensor b set

\[
 Q_z(E)=\rho(a)E\rho(b),\qquad\kappa(z)=aPb.
 \tag{15}
\]

Then

\[
 \|Q_z(E)\|_{M\to H}\le\|a\|\|b\|\|E\|_{M\to H}.
\]

Both Q and kappa extend continuously to B.
The exact identities from C_F0018 remain valid on M:

\[
 Q_wQ_z=Q_{zw},\qquad
 Q_w(\kappa(z)|_M)=\kappa(zw)|_M,\qquad
 [Q_z(E),y]=Q_z([E,y])\quad(y\in M).
 \tag{16}
\]

They follow by composing right multipliers, which commute with left multiplication; projective approximation proves them for completed tensors.
In the last formula every commutator is a bounded map M to H.
Thus (16) needs no Hilbert-space closability of E.

### 6. Equivalence of the full-domain conditions

Assume F(U).
Write E_i=-D_i, so [E_i,U_j]=delta_ij P on M.
Since U_i is normal, C_F0069 Part A makes E_i bounded M to H.
The inverse rule is valid on M and gives

\[
 [E_i,X_j]=\delta_{ij}\kappa(J_i)|_M.
\]

Consequently \(\widetilde E_i=Q_{q_i}(E_i)\) satisfies

\[
 [\widetilde E_i,X_j]=\delta_{ij}P,
 \qquad
 \|\widetilde E_i\|_{M\to H}
 \le\frac{\|E_i\|_{M\to H}}{|\alpha_i|-|\beta_i|}.
 \tag{17}
\]

Taking minus these maps proves F(X).
Normalization at Omega is optional for both existential conditions.

Conversely, assume F(X) and put E_i=-D_i.
Every X_i is normal, so C_F0069 again gives E_i in B(M,H).
For K_ij=[E_i,U_j], the full-domain inverse rule gives

\[
 \alpha_jK_{ij}-\beta_jU_j^*K_{ij}U_j^*
 =\delta_{ij}P|_M.
 \tag{18}
\]

Here the rightmost U_j* acts on M by left multiplication.
The map K -> U_j* K U_j* is an isometry on B(M,H).
A Neumann inversion of (18) therefore gives

\[
 K_{ij}=\delta_{ij}\kappa(q_i)|_M.
 \tag{19}
\]

The series identity follows directly by applying the iterated outer multipliers to P.
Now \(\widehat E_i=Q_{J_i}(E_i)\) satisfies [widehat E_i,U_j]=delta_ij P by (16), since q_i J_i=1.
Its norm is at most (|alpha_i|+|beta_i|)||E_i||_{M to H}.
Taking minus these maps proves F(U).

The accepted unitary equivalence from C_F0071 completes (2).
The proof has not assumed continuity of the original maps; it derived the precise Banach-space continuity needed for the two corrections from C_F0069.

### 7. This class need not have adjoints in the bounded division closure

Take M=L-infinity(T) with Haar trace, U(z)=z, and X=U+rU* with real 0<r<1.
On the Fourier basis e_n(z)=z^n, define the bounded operator

\[
 Ee_n=\begin{cases}e_{n-1},&n\ge1,\\0,&n\le0.\end{cases}
\]

A direct calculation gives [E,U]=P.
Thus F(U), and hence all four conditions in (2), hold in this example.

Nevertheless

\[
 X^*\notin\operatorname{Div}_M\mathbb C[X].
 \tag{20}
\]

Indeed every element of the bounded scalar division closure is represented by a rational function of X.
If X*=R(X) for such a rational function, then

\[
 U=\frac{X-rX^*}{1-r^2}
\]

would belong to C(X).
An almost-everywhere rational identity on the unit circle is an identity of rational functions in a complex indeterminate z, after clearing the finitely many denominator zeros.
But the automorphism sigma of C(z) defined by sigma(z)=r/z fixes x=z+r/z and does not fix z.
Therefore z cannot belong to C(x), a contradiction.
This proves (20).

The example shows a strict scope increase beyond the bounded-division-adjoint hypothesis; it does not claim disjointness from the known scalar-normal equivalence.
For d>1 the proof of (2) allows arbitrary correlations among the generating unitaries.
No rational-field identification or finite-rank preservation is inferred from the infinite projective correction.

## Review obligations and limits

The complete new proof requires an independent check of the shared star algebra, the distinct outer and inner coefficient actions, the unitary-tensor adjoint estimate, the absolute convergence used in (14), the extension of the reviewed projective correction to B(M,H), and the two full-domain Neumann inversions.
The complete candidate and its direct inputs are retained here for that review.

The general implications A(X) implies F(X) and F(X) implies A(X) for arbitrary correlated normal tuples remain unresolved by this result.
No separating counterexample to those general implications is claimed.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:19 |
| status | open |
| reason | Complete candidate for a further correlated normal coordinate class; independent review of the assembled argument remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Four-condition equivalence](#statement) | Exact elliptic-coordinate hypotheses, equivalence and quantitative vacuum bound. |
| argument | [Complete argument](#argument) | Sections 1-7, including the adjoint series, projective correction and strict scope example. |
| dependency | [Unitary equivalence](Yin_C_F0071_v2.md#statement) | Part D, A(U) if and only if F(U), for arbitrary generating unitary tuples. |
| dependency | [Automatic continuity](Yin_C_F0069_v1.md#statement) | Part A for each normal U_i and X_i, making the supplied full-domain maps bounded M to H. |
| dependency | [Projective correction](Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma) | Right-multiplier identities and projective estimates; Section 5 verifies the required change of Banach spaces. |
| dependency | [ACSY24 source interface](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Exact derivation and actual-vacuum condition; algebraic coefficient adjoint interface in Lemma 3.3, also checked quantitatively here. |

### Decision reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T13:26 |
| status | proved |
| reason | The exact fixed four-condition equivalence passed whole-argument independent review, including both actual-vacuum transformations, both full-domain corrections and the strict scope example. The result applies to arbitrary correlated elliptic images of unitary generators, while the unrestricted normal comparison remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Four-condition equivalence](#statement) | Elliptic-coordinate hypotheses, four equivalent existence conditions and explicit actual-vacuum bound. |
| argument | [Complete argument](#argument) | All Sections 1-7, including outer/inner actions, adjoint series, projective corrections and the Haar scope example. |
| dependency | [Unitary equivalence](Yin_C_F0071_v2.md#statement) | Part D, actual-vacuum and full-domain equivalence for arbitrary generating unitary tuples. |
| dependency | [Automatic continuity](Yin_C_F0069_v1.md#statement) | Part A for each normal diagonal coordinate, giving bounded maps from M with its operator norm to H. |
| dependency | [Projective correction](Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma) | Right-multiplier implementation and projective estimates, with the B(M,H) adaptation proved here. |
| dependency | [ACSY24 source interface](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Exact starred derivation and actual-vacuum condition; finite unitary-tensor adjoint estimates are proved explicitly here. |
| review | [Independent whole-argument review](../audits/reviews/Yin_R_F0137_v1.md#conclusion) | Exact fixed statement and complete proof, including the quantitative adjoint series and precise limits. |

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:59 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Elliptic-coordinate hypotheses, four equivalent existence conditions and explicit actual-vacuum bound. |
| argument | [Exact material](#argument) | All Sections 1-7, including outer/inner actions, adjoint series, projective corrections and the Haar scope example. |
| dependency | [Exact material](Yin_C_F0071_v2.md#statement) | Part D, actual-vacuum and full-domain equivalence for arbitrary generating unitary tuples. |
| dependency | [Exact material](Yin_C_F0069_v1.md#statement) | Part A for each normal diagonal coordinate, giving bounded maps from M with its operator norm to H. |
| dependency | [Exact material](Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma) | Right-multiplier implementation and projective estimates, with the B(M,H) adaptation proved here. |
| dependency | [Exact material](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Exact starred derivation and actual-vacuum condition; finite unitary-tensor adjoint estimates are proved explicitly here. |
| review | [Original finding](../audits/reviews/Yin_R_F0137_v1.md#conclusion) | Whole Sections 1–7 four-condition elliptic-unitary equivalence, actual unitary-tensor adjoints, quantitative projective series, both full-domain corrections and strict Haar scope example; preliminary-outline/context relationship unknown. |
