---
author: Yin
---

# Rational L2 commutators and full minimal affine inverse; all-q matrix spectral reduction

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Actual rational L2 states, finite dual commutators and affine inverse pencils

<a id="statement"></a>
<a id="yin_c_f0107"></a>

Date/author: 2026-09-11, another AI agent.
Record kind: substantive research continuation for [Yin_T_F0006](../tasks/Yin_T_F0006_v1.md).
Assessment: complete candidate arguments below, author checked; independent review pending.
No Claim ID or Role is assigned.

The new interface is an operator-domain argument.
Under the bounded normalized dual and bounded conjugate hypotheses available for every finite canonical q-Gaussian tuple, an affiliated rational L2 element has bounded finite-rank commutators on the polynomial core.
Their tensors are its rational derivatives.
This permits an L2 bootstrap through an arbitrary minimal affine-linear representation, including representations with singular constant matrix: the entire evaluated inverse pencil has L2 entries.

No boundedness of that inverse is inferred.
The full q-Gaussian L2 question is thereby reduced to inverses of full selfadjoint matrix affine pencils.
For the holomorphic q-circular subfield, the result also supplies the previously missing iterated negative-dual tests.
A specific Hilbert-space totality assertion remains necessary in the proposed route to holomorphic reconstruction.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0107** after [complete independent review](../audits/reviews/Yin_R_F0117_v1.md#7-outcome-and-verification-limits).
The bounded finite-rank L2 commutators, actual rational derivative tensors, entire minimal affine inverse in L2, matrix spectral equivalence and rational iterated-test inclusion are proved under (1), hence for every finite canonical q-Gaussian tuple.
The positive reconstruction conclusion (29) retains its explicit Hilbert-totality premise.
This supersedes the initial pending labels; full Q5/Q6 remain open.
The additional source input is [CR94-U001](../audits/literature/CR94/Yin_U001.md#cr94-u001).
No Role or lemma extraction is assigned.

## 1. Inputs, source search and exact hypotheses

The initial local search and reading covered [Yin_C_F0101](Yin_C_F0101_v1.md), [Yin_C_F0103 and the actual-state obstruction](Yin_C_F0103_v1.md), [the negative-dual kernel calculation](Yin_C_F0118_v1.md#argument), [Yin_C_F0023](Yin_C_F0023_v1.md#yin_c_f0023), [Yin_C_F0031](Yin_C_F0031_v1.md#yin_c_f0031), [Yin_C_F0034](Yin_C_F0034_v1.md#yin_c_f0034), [Yin_C_F0005](Yin_C_F0005_v1.md#yin_c_f0005), [Yin_C_F0007](Yin_C_F0007_v1.md#yin_c_f0007), and [Yin20's reconstructed representation existence](../audits/literature/Yin20/Yin_U001.md).
In particular, Yin20's representation audit expressly does not supply minimality.

Primary searches for q-Fock rational L2 states, q-difference recurrences and minimal free-field representations did not supply a theorem closing the q-Gaussian boundedness step.
The relevant additional source is P. M. Cohn and C. Reutenauer, *A Normal Form in Free Fields*, Canadian Journal of Mathematics 46 (1994), 517–531, [published primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/49C8E6861D278833D2CA949D3791A1C8/S0008414X00045946a.pdf/normal_form_in_free_fields.pdf), DOI [10.4153/CJM-1994-027-4](https://doi.org/10.4153/CJM-1994-027-4).
Section 3.1, printed p. 524, uses full affine matrices with scalar row and column and no invertible-constant requirement.
Lemma 4.5, p. 527, gives independence of both state families for a representation of least dimension.
Its complete short proof was inspected and is reproduced in Section 5 below.
Proposition 4.7, p. 528, confirms the converse, which is not needed here.
This is a selected source interface, not a full article audit or a new source ID.
The source's more elaborate uniqueness and scalar-extension arguments are not premises of our use of Lemma 4.5.

For the analytic arguments, let X_1,...,X_d be bounded selfadjoint generators of a finite tracial von Neumann algebra M, set
\[
H=L^2(M,\tau),\quad \Omega=1,\quad P=P_\Omega,\quad
\mathcal P=\mathbb C\langle X_1,\ldots,X_d\rangle,\quad
U=L^0(M),\quad \mathcal F_X=\operatorname{Div}_{L^0(M)}\mathcal P.
\]
Inner products are linear in the second variable.
We identify affiliated L2 elements with their vacuum vectors.
Assume bounded operators D_i on H satisfy
\[
[D_i,X_j]=\delta_{ij}P,\qquad D_i\Omega=0,
\qquad D_i(\mathcal P)\subseteq\mathcal P,\qquad
D_i^*(\mathcal P)\subseteq M.
\tag{1}
\]
The last condition means actual bounded affiliated elements, not merely vectors in H.

These conditions hold for every finite canonical q-Gaussian tuple, real -1<q<1, by Yin_C_F0023 and its bounded conjugate construction:
\[
D_i^*p=p\xi_i-D_i p,\qquad \xi_i=D_i^*\Omega\in M
\quad(p\in\mathcal P).
\tag{2}
\]
Polynomial invariance also follows directly from normalization and the coordinate commutators.
The bounded dual/free-field input in Yin_C_F0005 identifies \(\mathcal F_X\) with the embedded free skew field.
We use Yin_C_F0007's injectivity of
\[
\Psi:(U\otimes_{\mathbb C}U)^d\longrightarrow U\otimes_{\mathbb C}U,\qquad
\Psi((t_i)_i)=\sum_i\Psi_i(t_i),\quad
\Psi_i(g\otimes h)=gX_i\otimes h-g\otimes X_i h.
\tag{3}
\]
All tensors in this record are algebraic.
We do not replace the actual q-Gram norm by the ordinary coefficient norm.

## 2. A rational L2 element has a bounded finite-rank core commutator

Fix \(f\in\mathcal F_X\cap H\).
On the dense domain \(\mathcal P\Omega\), define
\[
T_{i,f}p=D_i(fp)-fD_i p.
\tag{4}
\]
Both terms are in H: f times a bounded polynomial is in H, D_i is bounded, and D_i p is a bounded polynomial.
There is no initial composition of f with D_i on all H.

First, (4) is closable.
For \(p,r\in\mathcal P\),
\[
\langle r,T_{i,f}p\rangle
=\left\langle f^*D_i^*r-D_i^*(f^*r),p\right\rangle.
\tag{5}
\]
The first term of the representing vector is in H because \(D_i^*r\in M\), and the second is in H because \(f^*r\in H\) and \(D_i^*\) is bounded.
Hence every polynomial vector belongs to the actual adjoint domain of \(T_{i,f}\), proving closability.

Next use the canonical bounded fractions
\[
s=(1+ff^*)^{-1/2},\quad a=sf,\qquad
t=(1+f^*f)^{-1/2},\quad b=ft.
\tag{6}
\]
Here s,t are bounded regular elements, a,b are bounded, and \(f=s^{-1}a=bt^{-1}\) in U.
Yin_C_F0034 applies with both module domains equal to H, since D_i and its adjoint are bounded.
It gives a bounded finite-rank cleared defect
\[
F_{i,f}=sD_i b-aD_i t.
\tag{7}
\]
Rational membership is used here: Yin_C_F0034 places every element of \(\mathcal F_X\) in its inverse-closed finite-defect algebra.

The special denominator in (6) permits recovery on every polynomial vector.
Indeed,
\[
t^{-1}=(1+f^*f)^{1/2}\in H,\qquad
\|t^{-1}\|_2^2=1+\|f\|_2^2.
\tag{8}
\]
For \(p\in\mathcal P\), put \(\zeta=t^{-1}p\in H\).
Affiliated multiplication, and the fact that b,t are bounded, give \(t\zeta=p\) and \(b\zeta=fp\) in H.
Consequently
\[
F_{i,f}\zeta
=sD_i(fp)-aD_i p
=s\bigl(D_i(fp)-fD_i p\bigr)=sT_{i,f}p.
\tag{9}
\]
The bounded injective operator s maps the range of \(T_{i,f}\) into the finite-dimensional range of \(F_{i,f}\).
Its injectivity implies that \(T_{i,f}\) has finite-dimensional range.
Yin_C_F0031 now applies to the closable densely defined operator (4): its closure is a bounded finite-rank operator on H.
Denote it again by \(T_{i,f}\).

This proof does not assert that \(D_i(tH)\) lies in the domain of f.
It only uses the vectors \(t^{-1}p\), for which all terms in (9) were explicitly checked.
It also does not infer boundedness of f from finite rank.

## 3. Identification with rational derivatives for L2 outputs

Let \(R_i=\rho(X_i)\) denote bounded right multiplication, and put \(K=\sum_i[R_i,D_i]\).
The Yin_C_F0005 Jacobi calculation shows \(K+P\in M'\).
It does not involve f.
Normalization gives
\[
K\Omega=-d\Omega,\qquad
(K+P)\Omega=(1-d)\Omega.
\]
Since \(\Omega\) is cyclic for M and \(K+P\in M'\),
\[
K=(1-d)I-P.
\tag{10}
\]
The coordinate selfadjointness makes the promotion from the generated star algebra to M immediate; no commutation modulo finite rank is used.

For a polynomial p, \(R_i p=pX_i\) is again polynomial.
The definition (4), the fact that left affiliated multiplication by f commutes with bounded right multiplication, and polynomial invariance give
\[
\begin{aligned}
\sum_i[R_i,T_{i,f}]p
&=\sum_i\bigl([R_i,D_i](fp)-f[R_i,D_i]p\bigr)\\
&=K(fp)-fKp\\
&=f\tau(p)-\tau(fp)\Omega.
\end{aligned}
\tag{11}
\]
Every displayed vector is in H.
In the second line the potentially unbounded multiplication acts on \(Kp=(1-d)p-\tau(p)\Omega\), a polynomial vector.
The right side extends boundedly to H because f is in H; explicitly it equals \(\Theta(f\otimes1-1\otimes f)\), where
\[
\Theta(g\otimes h)\eta=g\langle Jh,\eta\rangle .
\]
Both sides of (11) are therefore bounded and agree on a dense core.
Write \(t_i=\Theta^{-1}(T_{i,f})\in H\otimes H\).
Yin_C_F0005's right-action tensor formula gives
\[
\Psi((t_i)_i)=f\otimes1-1\otimes f.
\tag{12}
\]

The rational differentiation rule from Yin_C_F0007 independently produces \(\partial_i^{\rm rat}f\in\mathcal F_X\otimes\mathcal F_X\) and satisfies the same identity (12) inside \(U\otimes U\).
Injectivity (3) identifies the two tuples.
Its elementary tensor-intersection argument then gives
\[
\boxed{\quad
\partial_i^{\rm rat}f
=\Theta^{-1}(T_{i,f})
\in(\mathcal F_X\cap H)\otimes(\mathcal F_X\cap H).
\quad}
\tag{13}
\]
This extends the derivative-factor conclusion to arbitrary affiliated rational L2 outputs under (1).
It does not assume the output is bounded.

Since \(D_i\Omega=0\), evaluation of (4) at \(\Omega\) further yields
\[
D_i(f\Omega)
=T_{i,f}\Omega
=(\mathrm{id}\otimes\tau)(\partial_i^{\rm rat}f).
\tag{14}
\]
Here \(\tau(h)=\langle\Omega,h\rangle\) is defined for every h in H.
In particular \(D_i(\mathcal F_X\cap H)\subseteq\mathcal F_X\cap H\).

## 4. Scalar L2 output implies L2 entries of the entire minimal inverse

Take an affine pencil over scalar coefficients
\[
B(x)=A_0-\sum_{i=1}^d A_i x_i,\qquad
A_i\in M_n(\mathbb C),
\]
full over the free algebra, with \(f=uB(X)^{-1}v\), where u,v are scalar row and column.
Write \(B=B(X)\), \(g=uB^{-1}\) and \(h=B^{-1}v\).
Assume the two state families \(g_1,\ldots,g_n\) and \(h_1,\ldots,h_n\) are separately complex-linearly independent in the embedded free field.
Section 5 explains why any representation of least dimension has this property.
No hypothesis that \(A_0\) is invertible is made.

Suppose f is in H.
Equation (13) and the inverse differentiation rule give, for every \(i\ge1\),
\[
\partial_i^{\rm rat}f
=\sum_k(gA_i)_k\otimes h_k
=\sum_j g_j\otimes(A_i h)_j\in H\otimes H.
\tag{15}
\]
Apply the quotient \(U\to U/H\) in the first tensor factor.
Independence of the h_k implies that every entry of \(gA_i\) is in H.
Apply the quotient in the second factor instead; independence of the g_j implies that every entry of \(A_i h\) is in H.

The identities \(gB=u\) and \(Bh=v\) then give
\[
gA_0=u+\sum_{i=1}^d(gA_i)X_i\in H^{1\times n},\qquad
A_0h=v+\sum_{i=1}^dX_i(A_i h)\in H^{n\times1}.
\tag{16}
\]
Thus these conclusions hold also for i=0.

Both scalar matrices
\[
Q_R=\sum_{i=0}^d A_iA_i^*,\qquad
Q_L=\sum_{i=0}^d A_i^*A_i
\tag{17}
\]
are positive definite.
For example, a nonzero common kernel vector for the A_i would give a constant kernel vector for B, contradicting its invertibility over the free field; a common kernel vector for all A_i^* would similarly give a nonzero constant left kernel.
Consequently
\[
g=\left(\sum_{i=0}^d(gA_i)A_i^*\right)Q_R^{-1}\in H^{1\times n},
\qquad
h=Q_L^{-1}\sum_{i=0}^d A_i^*(A_i h)\in H^{n\times1}.
\tag{18}
\]
This is the required replacement for a monic reconstruction of the states.

Now apply (13) again, separately to each rational L2 element h_j.
The exact derivative formula is
\[
\partial_i^{\rm rat}h_j
=\sum_k(B^{-1}A_i)_{jk}\otimes h_k
\in H\otimes H,\qquad i\ge1.
\tag{19}
\]
The same quotient argument and the unchanged independence of the h_k imply \(B^{-1}A_i\in M_n(H)\) for i>=1.
Next
\[
B^{-1}A_0=I+\sum_{i=1}^d(B^{-1}A_i)X_i\in M_n(H).
\tag{20}
\]
The invertible scalar matrix \(Q_R\) finally gives
\[
\boxed{\quad
B^{-1}=\left(\sum_{i=0}^d(B^{-1}A_i)A_i^*\right)Q_R^{-1}
\in M_n(H).
\quad}
\tag{21}
\]
All multiplication used to reconstruct L2 vectors is by bounded scalar matrices or by the bounded X_i.
The appearance of the entire inverse in (21) is a proved two-stage bootstrap.
It was not assumed from scalar L2 output, from minimality alone, or from an abstract formal realization.

## 5. Minimality and the absence of a scalar-origin restriction

The local Yin20 reconstruction supplies a full affine representation of every free-field element.
Choose one of least positive dimension for a nonzero f; existence of a least dimension is just well ordering of the nonempty set of possible sizes.
A constant f can alternatively be handled with a one-dimensional constant pencil, and f=0 requires no inverse.

Here is the particular source argument needed from Cohn–Reutenauer Lemma 4.5.
If the entries of \(h=B^{-1}v\) are dependent over \(\mathbb C\), a scalar invertible column change makes its last entry zero.
In that basis \(B(h',0)^T=v\).
The first n-1 columns of B are independent over the division ring, so some n-1 rows select an invertible square submatrix C from those columns.
This is ordinary Gaussian elimination over a division ring; because C is an affine polynomial matrix, invertibility in the free field makes it full.
Restricting the equations to those rows yields \(h'=C^{-1}v'\).
The output is \(u'h'\), a smaller affine representation, a contradiction.
For n=1, a zero state gives f=0, already excluded.
The symmetric argument using the row \(g=uB^{-1}\) proves independence of its entries.
Scalar basis changes preserve affine linearity, and no scalar value of the variables is substituted.

The new analytic bootstrap in Section 4 therefore applies to a minimal representation of every \(f\in\mathcal F_X\cap H\), whether or not f has any scalar evaluation point.
The source proof used here is the elementary necessity direction, not the converse or its scalar-extension proof.

## 6. A precise matrix spectral reduction of Q5

Under (1), the following two assertions are equivalent:

1. \(\mathcal F_X\cap L^2(M,\tau)\subseteq M\).
2. For every full selfadjoint affine pencil \(L(x)\in M_N(\mathbb C\langle x\rangle)\), if \(L(X)^{-1}\) has L2 entries, then \(L(X)^{-1}\in M_N(M)\).

The first assertion implies the second because each inverse entry is an affiliated rational element.
Conversely, given scalar rational f in H, Sections 4–5 supply a full affine pencil B whose entire inverse has L2 entries.
Hermitize it:
\[
L(x)=\begin{pmatrix}0&B(x)\\B(x)^*&0\end{pmatrix},\qquad
L(X)^{-1}=
\begin{pmatrix}0&(B(X)^*)^{-1}\\B(X)^{-1}&0\end{pmatrix}.
\tag{22}
\]
Since the generators are selfadjoint, L is a selfadjoint affine pencil in the same variables.
The displayed inverse in the free field shows fullness.
Its entries are L2 because the trace makes adjunction preserve L2.
Assertion 2 makes B's inverse bounded and therefore makes \(f=uB^{-1}v\) bounded.

For a full selfadjoint L, let \(\mu_L\) be its spectral probability measure with respect to the normalized matrix trace and \(\tau\).
The remaining implication is exactly
\[
\int_{\mathbb R}|\lambda|^{-2}\,d\mu_L(\lambda)<\infty
\quad\Longrightarrow\quad 0\notin\sigma(L(X)).
\tag{23}
\]
Fullness ensures affiliated invertibility and no atom at zero.
Finiteness of the integral alone does not exclude zero from the support for a general measure.
A q-Gaussian proof must establish the additional exclusion for matrix affine pencils; the scalar marginal density calculation does not cover them.

This reduction holds in particular for d=2,q=1/2.
It gives neither an unbounded L2 inverse at those parameters nor a proof that none exists.
A sufficient new estimate would force divergence in (23) at every zero spectral point of every full selfadjoint affine q-pencil.
No such estimate is asserted here.

## 7. Exact q-weighted insertion equations for those actual L2 states

The reduction has an exact actual-state recurrence, without raw recognizability.
Let \(Y=B(X)^{-1}\in M_n(H)\) be supplied by (21), and expand each entry in raw q-Fock words:
\[
Y\Omega=\sum_w y_w\otimes e_w,\qquad y_w\in M_n(\mathbb C).
\]
For a fixed word w, extraction of its raw coordinate from a homogeneous finite-dimensional particle space is legitimate even though the raw basis is not orthogonal.
The standard annihilator action is
\[
\ell_q(e_i)^* e_{a_1\cdots a_m}
=\sum_{k:a_k=i}q^{k-1}e_{a_1\cdots\widehat{a_k}\cdots a_m}.
\]
It is the q-Fock action already used in the audited MS23 foundations.
Since creation and annihilation are bounded and change degree by one, projecting \(BY=I\) onto a fixed homogeneous degree gives a finite sum of actual coefficient equations:
\[
A_0y_w
-\mathbf1_{\{|w|\ge1\}}A_{w_1}y_{w_2\cdots w_{|w|}}
-\sum_{i=1}^d A_i\sum_{w=uv}q^{|u|}y_{uiv}
=\mathbf1_{\{w=\varnothing\}}I_n.
\tag{24}
\]
Every cut \(w=uv\), including the two endpoint cuts, occurs.
If different cuts produce the same inserted word, their contributions must be added.
The empty-word equation is \(A_0y_\varnothing-\sum_i A_i y_i=I_n\).

For d=2,q=1/2, the last sum has weights \(2^{-|u|}\).
At one scalar mode with \(B=\zeta-X\), (24) reduces to
\[
\zeta y_n-y_{n-1}-[n+1]_q y_{n+1}=\delta_{n0},
\]
with \(y_{-1}=0\), exactly the recurrence of Yin_C_F0103.
Thus (24) accommodates the known nonrecognizable resolvent.

Equation (24), together with actual q-L2 summability, is not yet a finite-state recurrence: it couples a coefficient to all one-letter insertions, rather than only one prefix or suffix residual.
No exponential particle-energy estimate follows merely by naming this a q-difference system.
The degree-n summability premise is
\[
\sum_{m\ge0}\sum_{a,b=1}^n
\left\|\sum_{|w|=m}(y_w)_{ab}e_w\right\|_q^2<\infty,
\tag{25}
\]
where n is the fixed pencil size and m is particle degree.
It is not \(\sum_w\|y_w\|_{\rm HS}^2<\infty\).
The analytic problem left by (24) is to derive enough decay, or to construct a solution coming from an actual affiliated inverse that violates boundedness.
Neither has been done in this round.

## 8. What is now automatic for holomorphic q-circular rationals

Use the signed coordinates and bounded duals \(D_j^\pm\) of [the complete kernel-interface proof](Yin_C_F0118_v1.md#argument), and let
\[
\mathcal F_+=\operatorname{Div}_{L^0(M)}\mathbb C\langle c_1,\ldots,c_d\rangle
\subseteq\mathcal F_{x,y}.
\]
The change from the selfadjoint tuple \((x_j,y_j)\) to \((c_j,c_j^*)\) is invertible and complex linear.
Combining the tensor identities (13) accordingly gives, for every \(f\in\mathcal F_+\cap H\),
\[
\partial_j^-f=0,\qquad
\partial_j^+f\in(\mathcal F_+\cap H)\otimes(\mathcal F_+\cap H).
\tag{26}
\]
For the second assertion, rational differentiation initially has both factors in \(\mathcal F_+\); its actual tensor is in \(H\otimes H\).
The same algebraic intersection identity used in (13) applies to these two subspaces of U.

Normalization and (14) imply
\[
D_j^-(f\Omega)=0,\qquad
D_j^+(f\Omega)\in\mathcal F_+\cap H.
\tag{27}
\]
Iterating the second statement and then the first proves
\[
\boxed{\quad \mathcal F_+\cap H\subseteq K_{\rm iter},\quad}
\tag{28}
\]
where \(K_{\rm iter}\) is precisely the common kernel of all \(D_k^-D_{j_m}^+\cdots D_{j_1}^+\) defined in that earlier record.
Thus the rational-state premise for those iterated tests is now supplied by an operator-domain proof.
The unresolved assertion \(K_{\rm iter}=H_+\) remains separate; the earlier finite-polynomial proof is not extended by truncation.

For clarity, if that totality assertion were proved, it would complete the holomorphic rational problem.
Take a minimal affine representation over the positive variables c.
The state bootstrap works by (26), with coefficients and the positive generators in (16)–(21), so its entire inverse Y has entries in \(\mathcal F_+\cap H\), hence in \(H_+\) under the extra assertion.
The positive generators act on \(H_+\) as literal left creation.
The vacuum component of \(BY=I\) would then say \(A_0 y_\varnothing=I_n\), forcing the scalar matrix \(A_0\) to be invertible even though that was not assumed.

After multiplying by \(A_0^{-1}\), the exact positive-word recursion gives recognizable actual coefficients.
Yin_C_F0101 and the actual-state argument in Section 3 of the earlier q-rational evaluation record then reconstruct all entries in the bounded scalar division closure.
Consequently the conditional conclusion would be
\[
\mathcal F_+\cap H
=\operatorname{Div}_{M}\mathbb C\langle c_1,\ldots,c_d\rangle.
\tag{29}
\]
Equation (29) is conditional on the stated Hilbert totality assertion.
Neither finite triangularity of the duals nor the simple common negative-dual kernel establishes that assertion.
No q-Gaussian or holomorphic rational boundedness goal is marked solved here.

## 9. Review boundaries

The substantive candidate proof is Sections 2–6 and the automatic rational test statement (28).
Section 7 supplies an exact recurrence with no decay conclusion.
Section 8's reconstruction conclusion (29) has an explicit additional premise.
Checks include the actual adjoint in (5), both bounded fraction placements, the use of \(t^{-1}\in L^2\), injectivity rather than a bounded inverse for s, the sign of K, full versus bounded matrix inverses, singular constant matrices, both coefficient Gram matrices, and the second derivative bootstrap.
Yin_C_F0103's counterexample to universal raw-Wick recognizability is preserved.
No numerical experiment, unbounded rational L2 counterexample, whole-source audit, formal verification or independent review is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:46 |
| status | proved |
| reason | Adopt the exact original finding at its disclosed unknown initial-context relationship. Preserve the mathematical statement, status, selected proof, conditional boundaries, dependencies and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-a-rational-l2-element-has-a-bounded-finite-rank-core-commutator) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0117_v1.md#7-outcome-and-verification-limits) | Whole nine-section operator-interface proof: actual finite-rank rational L2 commutators and derivative tensors, nonmonic minimal whole inverse in L2, matrix spectral equivalence, exact q-insertion recurrence and rational iterated-test inclusion. Positive reconstruction (29) remains conditional on the stated Hilbert totality; no Q5/Q6 completion. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-a-rational-l2-element-has-a-bounded-finite-rank-core-commutator) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0117_v1.md#current-isolated-finding) | Complete Sections 1–9 operator-interface mathematics, actual finite-rank rational L2 commutators, nonmonic minimal full inverse in L2, matrix spectral reduction and exact signed insertion recurrence; positive reconstruction (29) remains conditional on the stated K_iter=H_+ equality. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; positive reconstruction conditional

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-a-rational-l2-element-has-a-bounded-finite-rank-core-commutator) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0117_v1.md#7-outcome-and-verification-limits) | Original selected finding; its actual scope and limits remain in the cited review. |

Original review classification and limitations: independently reviewed; positive reconstruction conditional

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

<a id="decision-candidate-0004"></a>

### Historical assessment candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-a-rational-l2-element-has-a-bounded-finite-rank-core-commutator) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0117_v1.md#7-outcome-and-verification-limits) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0117_v1.md#7-outcome-and-verification-limits).

Material covered by that review: [Exact material](Yin_C_F0107_v1.md).
