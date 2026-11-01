---
author: Yin
---
# A common left factor separates maximal Delta from all bare full-domain duals

Human author: Yin.
The general ACSY-to-full-domain branch developed the finite row-relation obstruction and the concrete tuple.
Root contributed the row-kernel mechanism, the maximal-Delta substitution lead and checks of the failed full-reference lift.
Both are development contributors, not independent reviewers.
This fixes the complete argument from the continuing D_F0003 investigation; it makes no ACSY-to-full-domain separation claim.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, H=L2(M,tau), Omega=1, and P(a)=tau(a)1 on M.
A bare full-domain dual system for a bounded generating tuple X consists of arbitrary complex-linear maps D_i:M->H with

\[
 [X_j,D_i](a)=\delta_{ij}\tau(a)1\quad(a\in M).
 \tag{1}
\]

No boundedness, closability or actual adjoint-domain premise is imposed.

**General obstruction.**
If a bounded row relation sum_j X_j a_j=0 has tau(a_i) nonzero, while 1 does not belong to sum_j X_j L2(M), then no D_i satisfying (1) exists.

**Concrete tuple.**
Let s_0,S_1,S_2 be standard free semicircular elements, tilde M=W*(s_0,S_1,S_2), h=2+s_0, X_j=hS_j for j=1,2, and N=W*(X_1,X_2) with the restricted trace.
Then Delta_N(X_1,X_2)=2, but neither coordinate admits a bare dual (1) on all N.
The target star algebra C<X_1,X_2,X_1*,X_2*> is algebraically free on its four generators, and both X_j are nonnormal.

**Reference-lifting boundary.**
No derivation on the full reference polynomial algebra C<h,S_1,S_2>, taking values in L2(tilde M) tensor_2 L2(tilde M) with outer actions, can satisfy delta(X_j)=delta_ij 1 tensor 1 for either fixed i.
This does not exclude derivations on the target star algebra alone.

The ACSY condition A(N;X_1,X_2), requiring coordinate derivations on the target star core with actual vacuum adjoints, remains unresolved here.
Thus the result separates maximal Delta from bare full-domain existence, but does not assert a separation of A from bare full-domain existence.

## Argument

The exact source inputs are [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002), which equates maximal Delta with injectivity of all full affine linear square matrices for arbitrary bounded tuples, and [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004), Theorem 5.6, which equates that condition with injectivity of all full square polynomial matrices.
Reference maximal Delta comes from the standard actual semicircular vacua and [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), with its hypotheses checked in Section 3.
No assertion that arbitrary polynomial substitutions preserve fullness is imported.

### 1. A row-kernel obstruction excluding every bare full-domain witness

The following finite relation is an exact obstruction to (1), rather than a test of a chosen canonical operator.
Suppose a_1,...,a_d in M satisfy

\[
 \sum_jX_j a_j=0,\qquad\tau(a_i)\ne0,
 \qquad
 1\notin\sum_jX_jL^2(M).
 \tag{2}
\]

If D_i satisfied (1), put E_i=-D_i, so E_i(X_j a)=X_j E_i(a)+delta_ij tau(a)1.
Applying E_i to the bounded relation would give 0=sum_j X_j E_i(a_j)+tau(a_i)1, contrary to the last condition in (2).
No boundedness, normalization, closability or adjoint assumption on E_i has been used.

### 2. A concrete common-left-factor tuple with F false

Let the ambient finite tracial algebra tilde M contain three freely independent standard semicircular elements s_0,S_1,S_2.
Put h=2+s_0 and

\[
 X_1=hS_1,\quad X_2=hS_2,\qquad
 N=W^*(X_1,X_2)\subseteq\widetilde M.
 \tag{3}
\]

The target algebra here is N with its restricted trace; it is not assumed equal to the reference algebra.
The law of h has density sqrt(t(4-t))/(2 pi) on (0,4).
It has no mass at zero, so h is positive regular.
Its inverse square is not integrable because t^(-2) times this density has order t^(-3/2) near zero.
Thus h^-1 is not in L2(tilde M).
Each S_j is regular by its nonatomic semicircular law.
Set R=[X_1,X_2] and let p be its kernel projection in M_2(N).
Since left multiplication by h is injective on the ambient L2 space,

\[
 \ker R=\ker[S_1,S_2]
 \quad\text{on }L^2(\widetilde M)^2.
 \tag{4}
\]

The row [S_1,S_2] has dense final range: its adjoint has zero kernel because S_1 is regular.
Its polar decomposition therefore has final projection 1 and initial projection 1-p.
Equality of the finite rectangular traces gives (tau tensor Tr_2)(p)=1.
The Fock-space permutation interchanging S_1 and S_2 and fixing s_0 implements a trace-preserving automorphism preserving N.
It sends R to R J, with J the two-by-two swap matrix, and therefore sends p to JpJ by functional calculus.
It interchanges p_11 and p_22, so tau(p_11)=tau(p_22)=1/2.
This argument requires no bounded inverse or lower spectral gap for S_1^2+S_2^2.

The first column (a_1,a_2)=(p_11,p_21) belongs to N^2 and satisfies R a=0 with tau(a_1)=1/2.
On the other hand

\[
 X_1L^2(N)+X_2L^2(N)
   \subseteq hL^2(\widetilde M),\qquad
 1\notin hL^2(\widetilde M),
 \tag{5}
\]

because a solution h eta=1 would be the unique affiliated inverse eta=h^-1, which is not L2.
Conditions (2) hold, so no E_1 exists.
The second column gives the same conclusion for E_2.
Thus F(N;X_1,X_2) is false for every possible choice of bare duals.
Generation holds by the definition of N.
This excludes every bare witness; A(N;X_1,X_2) is not established, so (3) is a candidate test, not an A-to-F separation theorem.

### 3. Polynomial retraction proves maximal Delta

The same tuple has maximal Delta.
This uses an exact matrix-fullness argument rather than inferring maximality from algebraic freeness.
The reference tuple (h,S_1,S_2) has the standard actual semicircular conjugates (s_0,S_1,S_2).
For the actual-domain check use the [standard Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001): partial_j U_w is the sum of U_u tensor U_v over cuts w=u j v.
Pairing with the vacuum tensor gives zero unless w is the one-letter word j, when it gives one.
Thus the actual adjoint value is the semicircular vector, a Hilbert-bounded functional on the entire polynomial core.
The scalar translation s_0 to h preserves this core and all derivative identities.
The reference tuple is bounded and generates the reference algebra, so it has maximal Delta by [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
Let P(x_1,x_2) be a full square polynomial matrix of size n.
The substituted matrix P(h s_1,h s_2) is full over C<h,s_1,s_2>: any factorization through size r<n would, under the polynomial retraction h mapped to 1 and s_j mapped to x_j, give such a factorization of P itself.
By the full-linear criterion in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) and its full-polynomial equivalence in [MSY23-U004, Theorem 5.6](../audits/literature/MSY23/Yin_U004.md#theorem-56-exact-equivalences), P(X_1,X_2) is injective on the ambient L2 space.
It is therefore injective on L2(N)^n.
Applying MSY23-U002's converse to full affine linear matrices over the two target variables gives

\[
 \Delta_N(X_1,X_2)=2,\qquad
 \mathsf F(N;X_1,X_2)\text{ is false}.
 \tag{6}
\]

All these source interfaces explicitly allow the target tuple to be nonnormal.
No ambient generation assumption is imported: the reference tuple generates the ambient algebra, while the target tuple generates N by definition.
Equation (6) supplies no actual target-A witness.

### 4. The target star algebra is free, but ordinary reference lifting fails

There is no polynomial-star-relation obstruction for (3).
The reference variables h,S_1,S_2 are algebraically free.
Before translation a semicircular monomial applied to the vacuum has its corresponding word as the highest-length term; distinct highest words cannot cancel.
The invertible formal scalar translation s_0 -> h preserves this assertion.
The four target words hS_1,hS_2,S_1h,S_2h are distinct words of length two in that alphabet.
Every concatenation admits unique decoding into its successive blocks of length two.
Distinct words in the four target symbols are therefore distinct reference words, proving algebraic freeness of C<X_1,X_2,X_1*,X_2*>.
Each X_j is nonnormal: hS_j^2h-S_jh^2S_j is a nonzero polynomial in the algebraically free reference variables.
Prescribing arbitrary coarse L2 values on the four symbols consequently defines an algebraic derivation; its actual vacuum remains a separate condition.

An L2-valued derivation on the FULL reference algebra cannot realize even one target coordinate.
To prove this, let alpha=delta h and beta_j=delta S_j.
In the coarse algebra tilde M tensor bar tilde M^op, the desired target values would force

\[
 (h\otimes1)\beta_j+(1\otimes S_j^{\mathrm{op}})\alpha
      =\delta_{ij}1,
 \qquad j=1,2.
 \tag{7}
\]

Here the outer right action on a tensor alpha is left multiplication by 1 tensor S_j^op; this fixes the coefficient order.
Let r be the two-entry column with entries 1 tensor S_j^op and q the orthogonal projection onto ker r*.
It lies entirely in the second tensor factor.
The same polar-trace and swap arguments give (tau tensor tau)(q_ii)=1/2.
Multiplying (7) by q and using commutation with h tensor 1 gives

\[
 q\begin{pmatrix}\beta_1\\\beta_2\end{pmatrix}
   =(h^{-1}\otimes1)q e_i.
 \tag{8}
\]

The right side has infinite squared L2 norm: its trace separates into tau(h^-2) times the positive value 1/2 from the second factor.
The left side is L2 if the beta_j are L2.
This contradiction does not depend on the value of alpha.

Equations (7)–(8) exclude ordinary L2 reference-Jacobian lifting.
They do NOT exclude A on the target star algebra: h,S_j are not assumed to lie in its polynomial core or in an actual closed-derivation domain.
No passage to them through weak closure or unbounded inverses has been proved.
In particular failure of the natural reference extension is not yet failure of every target derivation with an actual vacuum.

The next precise obligation is to construct target derivations with delta_i X_j=delta_ij 1 and actual vacuum adjoints, allowing their starred values to vary, or to derive from that actual target condition an obstruction that applies without extending delta to h,S_1,S_2.
The row-kernel proof has already settled all-bare-F nonexistence for (3); only this target-A question is open in the test.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:39 |
| status | open |
| reason | Complete candidate proof of the finite row obstruction and the maximal-Delta tuple with no bare coordinate dual; actual target A is explicitly outside the conclusion. Independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General obstruction, concrete maximal Delta and all-bare-dual nonexistence, star algebraic freeness, and failed full-reference Hilbert lifting. |
| argument | [Argument](#argument) | All four sections, including target/ambient domains, finite traces, polynomial retraction and coarse coefficient order. |
| dependency | [Semicircular Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Standard normalization, Wick basis and word-cut actual vacuum identity; no general full-domain extension theorem. |
| dependency | [ACSY vacuum implication](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 applied only to the selfadjoint translated reference tuple with actual conjugates checked in Section 3. |
| dependency | [Maximal Delta and full linear matrices](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Theorem 3.1 in both directions, with arbitrary bounded target tuple and ambient/target algebras distinguished. |
| dependency | [Full polynomial matrices](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Theorem 5.6 promotes the reference full-linear condition to injectivity of full polynomial matrices. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:44 |
| status | proved |
| reason | Adopt the general row obstruction and the concrete maximal-Delta tuple after R_F0154 independently checked the entire statement, four proof sections and all four direct source interfaces. Actual target ACSY remains unresolved; no A-to-F separation is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General obstruction, concrete maximal Delta and all-bare-dual nonexistence, star algebraic freeness, and failed full-reference Hilbert lifting. |
| argument | [Argument](#argument) | All four sections, including target/ambient domains, finite traces, polynomial retraction and coarse coefficient order. |
| dependency | [Semicircular Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Standard normalization, Wick basis and word-cut actual vacuum identity; no general full-domain extension theorem. |
| dependency | [ACSY vacuum implication](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 applied only to the selfadjoint translated reference tuple with actual conjugates checked in Section 3. |
| dependency | [Maximal Delta and full linear matrices](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Theorem 3.1 in both directions, with arbitrary bounded target tuple and ambient/target algebras distinguished. |
| dependency | [Full polynomial matrices](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Theorem 5.6 promotes the reference full-linear condition to injectivity of full polynomial matrices. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0154_v1.md#conclusion) | Entire corrected argument, all four exact inputs, both actual Hilbert range obstructions, nonnormal target scope and the unresolved target-A boundary. |

