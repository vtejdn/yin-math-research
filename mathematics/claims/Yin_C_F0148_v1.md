---
author: Yin
---
# Actual target vacua force an integrable inverse row square

Human author: Yin.
The target-functional branch agent developed the resolvent test and its actual-core proof in D_F0005.
Root checked its constants and weak-limit mechanism, suggested the general row formulation and the full bounded-vector range corollary.
These are development contributions, not independent review.
The general-branch agent had independently found the earlier Riesz criterion but did not develop the resolvent obstruction fixed here.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, H=L2(M,tau), and let X=(X_1,...,X_d) be a bounded generating tuple.
Set

\[
 \mathcal A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
 \quad R=[X_1\ \cdots\ X_d],\quad Q=RR^*=\sum_jX_jX_j^*.
 \tag{1}
\]

The matrix kernel projection p of R belongs to M_d(M); write c_i=tau(p_ii).
Inner products are linear in their second variable and all derivations below use outer bimodule actions.

**Coordinate obstruction.**
Suppose Q is regular and c_i>0.
If a complex-linear derivation

\[
 \delta:\mathcal A\longrightarrow H\otimes_2H,
 \qquad \delta X_j=\delta_{ij}1\otimes1,
 \qquad 1\otimes1\in\operatorname{Dom}\delta^*
 \tag{2}
\]

exists, then tau(Q^-1)<infinity.
The starred values delta X_j* are arbitrary Hilbert tensors consistent with the target algebra; they need not be zero or scalar.
No derivation on a larger reference algebra is assumed.

**Full-system consequence.**
If d>=2 and the full target ACSY condition A(X) holds, then Q is regular and tau(Q^-1)<infinity.
Moreover every a in M belongs to the actual row range R H^d.
With R=Q^(1/2)V its polar decomposition, one may choose

\[
 v=V^*Q^{-1/2}a\in H^d,\qquad Rv=a,\qquad
 \sum_j\|v_j\|_2^2\le\tau(Q^{-1})\|a\|^2.
 \tag{3}
\]

This does not construct a coordinate dual on M or prove A implies F.
It rules out the specific finite-row nonrange obstruction under A.

**Application.**
For the accepted common-left-factor tuple of C_F0147,

\[
 h=2+s_0,\quad X_j=hS_j\ (j=1,2),\quad N=W^*(X_1,X_2),
 \tag{4}
\]

with three free standard semicircular reference variables, neither coordinate admits (2) on the target star core in N.
Thus A(N;X_1,X_2) is false.
Together with C_F0147, this tuple has maximal Delta=2 while A and F both fail; it is not an A-to-F separating example.

## Reuse and source scope

The exact tuple, its spectral facts, its target row-kernel traces and the existing all-bare-dual obstruction are fixed in [C_F0147](Yin_C_F0147_v1.md#statement).
The current functional development first read that fixed result and its independent review, then the continuing D_F0003 boundaries.
The present proof does not use a failed candidate lift as a universal obstruction.

The known interpretation of actual-vacuum derivations as the actual gradient-adjoint domain was checked in [CN21-U001](../audits/literature/CN21/Yin_U001.md#cn21-u001), arXiv v2 Lemma 3.1, PDF p.9.
This is attribution and a compatible formulation; the pairing used below is computed directly.
The separate closure/dimension and approximate-Jacobian interfaces in [CN25-U001](../audits/literature/CN25/Yin_U001.md#cn25-u001) do not supply the new resolvent sequence and are not assumed as proof premises.
Neither an ambient dimension upper bound nor a target-to-reference extension is used.
Source inspection limits remain those of the exact units.

For the full-system regularity assertion only, [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) gives maximal Delta from the exact target hypotheses, without a normality premise.
[MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) then makes each full one-by-one affine matrix X_j injective.
These are accepted source interfaces; no new audit of all their original proofs is claimed.

## Argument

### 1. The target resolvent identity uses only original core tests

Assume (2) and put xi=delta*1 and K_j=delta X_j*.
All these are fixed Hilbert vectors.
For epsilon>0 set

\[
 A_\varepsilon=(Q+\varepsilon)^{-1},\quad
 T_\varepsilon=\tau(A_\varepsilon),\quad
 c_{i,\varepsilon}=1-\tau(X_i^*A_\varepsilon X_i).
 \tag{5}
\]

The positive contractions R*(Q+epsilon)^-1 R increase strongly to 1-p.
Hence c_i,epsilon decreases to c_i>0.
In particular the normalizing factor in

\[
 f_\varepsilon=\frac{A_\varepsilon X_i}{T_\varepsilon c_{i,\varepsilon}}
 \tag{6}
\]

is nonzero.

Here is the precise core justification for manipulating this resolvent.
Fix epsilon and take B>||Q||+epsilon.
The series

\[
 A_\varepsilon=B^{-1}\sum_{k\ge0}
          (1-(Q+\varepsilon)/B)^k
 \tag{7}
\]

converges in operator norm, with theta=||1-(Q+epsilon)/B||<1.
Its partial sums are in the target star core.
The Leibniz rule bounds the derivative of the kth power in Hilbert tensor norm by k theta^(k-1) times the fixed norm of delta(Q)/B.
The differentiated series therefore converges and satisfies the usual inverse product rule.
Multiplication by X_i and the fixed scalar in (6) preserves this graph convergence.
Passing the actual adjoint identity against 1 to this limit is legitimate by Hilbert continuity on both sides.
No inverse belongs to an initially assumed algebraic domain, and no domain of h or S_j has been used.

On the core, the prescribed unstarred values give

\[
 \delta Q=1\otimes X_i^*+\sum_jX_jK_j.
\]

The series just checked consequently gives the derivative value

\[
 \delta(A_\varepsilon X_i)
   =A_\varepsilon\otimes1
       -A_\varepsilon\otimes X_i^*A_\varepsilon X_i
       -\sum_j(A_\varepsilon X_j)K_j(A_\varepsilon X_i).
 \tag{8}
\]

The multiplication around K_j is the bounded outer action.
For any bounded a,b and Hilbert tensor K, tracial cyclicity gives

\[
 \langle1,aKb\rangle=\langle K^*,a\otimes b\rangle,
 \tag{9}
\]

where K* is the componentwise tensor adjoint without a flip.
This follows first for an elementary tensor and then by Hilbert approximation.
Equations (5)--(9) yield the exact scalar identity

\[
 \langle\xi,f_\varepsilon\rangle
   =1-\sum_j\left\langle K_j^*,
       \frac{A_\varepsilon X_j\otimes A_\varepsilon X_i}
            {T_\varepsilon c_{i,\varepsilon}}\right\rangle.
 \tag{10}
\]

This identity is already a consequence of original polynomial core tests via (7); no closed-derivation product rule on an unverified larger domain is a premise.

### 2. Divergence of the inverse trace contradicts every actual witness

Suppose tau(Q^-1)=infinity.
Regularity of Q and monotone spectral convergence imply T_epsilon tends to infinity.
Positivity and traciality give

\[
 \sum_j\|A_\varepsilon X_j\|_2^2
    =\tau(QA_\varepsilon^2)\le T_\varepsilon.
 \tag{11}
\]

Thus ||f_epsilon||_2<=1/(c_i,epsilon sqrt(T_epsilon)) tends to zero, and the normalized vectors

\[
 a_{j,\varepsilon}=A_\varepsilon X_j/\sqrt{T_\varepsilon}
 \tag{12}
\]

are bounded in H.
They converge weakly to zero.
Indeed, for d_0>0 let e_(d_0)=1_(0,d_0)(Q).
The high-spectral part satisfies

\[
 \|(1-e_{d_0})a_{j,\varepsilon}\|_2
      \le\frac{\|X_j\|_2}{d_0\sqrt{T_\varepsilon}}
          \longrightarrow0.
 \tag{13}
\]

For a fixed test vector v, the low-spectral pairing has absolute value at most ||e_(d_0)v||_2.
Since Q is regular, these projections decrease strongly to zero as d_0 decreases to zero.
Taking the two limits in that order proves weak convergence.

The tensors a_j,epsilon tensor a_i,epsilon are bounded and weakly converge to zero in H tensor_2 H.
On elementary test tensors this follows from weak convergence of one factor and boundedness of the other, and the uniform norm bound extends it by density to all Hilbert tensors.
Since c_i,epsilon tends to the positive number c_i, all tensor pairings in (10) tend to zero.
Its left side also tends to zero because xi is fixed and f_epsilon tends strongly to zero.
Equation (10) would then give 0=1, a contradiction.

This proves the coordinate obstruction for every possible set of starred values and every actual vacuum.
It does not mistake weak tensor convergence for norm convergence.
Alternatively, one can choose finite partial sums in (7) at each epsilon so that all scalar and Hilbert errors tend to zero; the same contradiction then occurs along a single sequence of original target polynomials.

### 3. A full system forces actual row surjectivity on bounded vectors

Under full A, the exact ACSY interface gives Delta(X)=d.
The full-linear-matrix criterion of MSY23 applies to arbitrary bounded tuples and, in particular, to each full scalar polynomial x_j.
Thus each X_j is injective.
In a finite tracial algebra its adjoint is injective as well: the initial and final support projections of its polar decomposition have equal trace, so full initial support forces full final support.
Hence Q is regular.

For R=[X_1 ... X_d], regularity of Q makes the final support in its rectangular polar decomposition equal to 1.
Equality of the finite unnormalized rectangular traces gives

\[
 \sum_i c_i=(\tau\otimes\operatorname{Tr}_d)(p)=d-1.
 \tag{14}
\]

If d>=2, at least one c_i is positive.
The corresponding actual coordinate witness and the proved obstruction force tau(Q^-1)<infinity.
No assertion that every c_i is positive is needed.
For d=1 the sum is zero and this argument supplies no such conclusion.

Now Q^-1/2 is in L2(M).
For a in M, bounded right multiplication gives Q^-1/2 a in H, with squared norm at most tau(Q^-1)||a||^2.
Write R=Q^1/2 V; its bounded rectangular partial isometry satisfies VV*=1.
Define v=V*Q^-1/2 a, which is an actual Hilbert column.
Its squared norm is exactly ||Q^-1/2 a||_2^2 and

\[
 Rv=Q^{1/2}VV^*Q^{-1/2}a=a.
\]

The last equality is the spectral identity on the actual range of Q^-1/2.
This proves (3) without assuming that Q^-1 a is a Hilbert vector.
In particular, writing a formal composition R*Q^-1 is unnecessary and would require an extra domain check.

Every bounded a therefore lies in sum_j X_j H.
The finite-row obstruction of C_F0147, which requires 1 outside this range, cannot occur under full A with d>=2.
A coherent family of coordinate dual maps satisfying all commutators is a different requirement and is not constructed here.

### 4. Application to the common-left-factor tuple

Use exactly the target algebra N and restricted trace from C_F0147.
There, h and each S_j are regular, h^-1 is not L2, and the row-kernel traces are c_1=c_2=1/2.
Also Q is regular: X_1*=S_1h is injective on the ambient standard Hilbert space, so its restriction to the target space is injective.

The norm of each standard semicircle is 2, hence in the ambient finite algebra

\[
 Q=h(S_1^2+S_2^2)h\le8h^2.
\]

For each epsilon>0, order reversal of bounded positive inverses gives

\[
 \tau((Q+\varepsilon)^{-1})
       \ge\tau((8h^2+\varepsilon)^{-1})\longrightarrow\infty,
 \tag{15}
\]

because tau(h^-2)=infinity.
Both Q and its resolvent are in N and use the same trace.
Thus tau(Q^-1)=infinity, and each positive c_i excludes its own actual target coordinate witness by Section 2.
No target-domain membership of the reference factors or equality of target and ambient algebras enters this step.

The accepted maximal-Delta and all-bare-F conclusions of C_F0147 remain unchanged.
The new information is that actual target A fails as well.
This resolves the target-A question for that particular candidate and does not settle the general comparison task.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:58 |
| status | open |
| reason | Complete target-resolvent obstruction, full-A inverse-trace/range consequence, and A-failure for the accepted common-left-factor tuple; independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Coordinate obstruction at positive row-kernel diagonal trace, full-system inverse integrability and bounded-vector row range, and failure of both actual target coordinates in C_F0147. |
| argument | [Argument](#argument) | All four sections: original-core series, arbitrary starred Hilbert coefficients, weak tensor limit, full-system support traces and actual polar range, and target/ambient application. |
| dependency | [Common-left-factor tuple](Yin_C_F0147_v1.md#statement) | Exact reference model, h inverse-square divergence, target kernel traces 1/2, and existing maximal-Delta/all-bare-F conclusions. Its failed reference lift is not used to infer target A failure. |
| dependency | [Actual A implies maximal Delta](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 at arbitrary bounded generating tuples, with actual starred-core derivations and actual vacuum adjoints; used only to obtain regularity for the full-system corollary. |
| dependency | [Full linear matrices](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta implies injectivity of the full one-by-one affine matrices x_j; finite polar support then gives adjoint injectivity and regular Q. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:05 |
| status | proved |
| reason | Adopt the actual target-resolvent obstruction and its full-system range consequence after R_F0155 independently checked the entire statement, all four proof sections and all three direct interfaces. The common-left-factor tuple fails actual A as well as F and therefore does not separate them. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Coordinate obstruction at positive row-kernel diagonal trace, full-system inverse integrability and bounded-vector row range, and failure of both actual target coordinates in C_F0147. |
| argument | [Argument](#argument) | All four sections: original-core series, arbitrary starred Hilbert coefficients, weak tensor limit, full-system support traces and actual polar range, and target/ambient application. |
| dependency | [Common-left-factor tuple](Yin_C_F0147_v1.md#statement) | Exact reference model, h inverse-square divergence, target kernel traces 1/2, and existing maximal-Delta/all-bare-F conclusions. Its failed reference lift is not used to infer target A failure. |
| dependency | [Actual A implies maximal Delta](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 at arbitrary bounded generating tuples, with actual starred-core derivations and actual vacuum adjoints; used only to obtain regularity for the full-system corollary. |
| dependency | [Full linear matrices](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta implies injectivity of the full one-by-one affine matrices x_j; finite polar support then gives adjoint injectivity and regular Q. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0155_v1.md#conclusion) | Whole fixed proof, three direct inputs, prior-input and reused-dependency disclosures, arbitrary starred values, actual weak limits and target row-range application. |

