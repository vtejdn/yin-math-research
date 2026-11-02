---
author: Yin
---
# Nonlinear target derivations and an exact actual-adjoint test

Human author: Yin.
The acsy_to_full_domain agent developed the affiliated resolvent construction, target polynomial relation, uniqueness argument and positive-reference Hilbert--Schmidt range formula.
Root supplied the precise necessary equation for an arbitrary bare full-domain witness and emphasized that its Hilbert--Schmidt uniqueness is not all-witness uniqueness.
These are development contributions; this candidate has not received independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be finite with faithful normal probability trace, H=L2(M,tau), Omega=1, and P the orthogonal projection onto C Omega.
Inner products are linear in the second variable.
Let h,S be bounded selfadjoint generators with represented free difference quotients partial_h,partial_S on A_0=C<h,S> and actual conjugate vectors xi_h=partial_h*(1 tensor 1), xi_S=partial_S*(1 tensor 1) in H.
Assume h is positive and regular, meaning ker h=0.
No bounded inverse or inverse-L2 hypothesis is imposed.
Put
\[
 Y=ShS+\mathrm i hSh,\qquad
 A_X=\mathbb C\langle h,Y,Y^*\rangle,\qquad
 N=M\bar\otimes M^{\mathrm{op}}.
 \tag{1}
\]
Identify H tensor_2 H with L2(N) by u tensor v corresponding to u tensor v^op.
Products of affiliated operators below are their closed affiliated products.

Then W*(h,Y)=M.
On A_X there is exactly one L0(N)-valued outer derivation for each of the coordinate prescriptions
\[
 \delta_Yh=0,\quad\delta_YY=1,\qquad
 \theta_hh=1,\quad\theta_hY=0.
 \tag{2}
\]
Both derivations actually take values in N, hence in L2(N).
They have the following explicit formulas.
Let
\[
 \begin{gathered}
 b=h^{-1},\quad B=h\otimes h^{\mathrm{op}},\quad
 Q=S\otimes b^{\mathrm{op}}+b\otimes S^{\mathrm{op}},\quad
 R=(Q+\mathrm i)^{-1},\quad
 F=Sh\otimes1+1\otimes(hS)^{\mathrm{op}}+\mathrm iB,\quad
 \beta=F^{-1}=B^{-1}R,\qquad
 C=\partial_hY=S\otimes S^{\mathrm{op}}
      +\mathrm i\bigl(1\otimes(Sh)^{\mathrm{op}}+hS\otimes1\bigr).
 \end{gathered}
 \tag{3}
\]
Here Q is selfadjoint affiliated with N, R belongs to N with norm at most 1, and F is regular in N.
On A_X the formulas are
\[
 \delta_Y(p)=(\partial_Sp)\beta,\qquad
 \theta_h(p)=\partial_hp-\delta_Y(p)C.
 \tag{4}
\]
In particular
\[
 \delta_Y(Y^*)=(Q-\mathrm i)(Q+\mathrm i)^{-1}=:k
 \tag{5}
\]
is unitary in N.
Formula (4) is evaluated in L0(N); beta itself need not belong to L2(N).

Let A(h,Y) mean the full ACSY condition: existence of Hilbert-tensor-valued outer derivations on the represented star algebra A_X with (2) and actual vacuum adjoints.
Then the exact equivalence is
\[
 \mathsf A(h,Y)\quad\Longleftrightarrow\quad
 1,C^*\in\operatorname{Dom}(\delta_Y:A_X\subset H\longrightarrow L^2(N))^*.
 \tag{6}
\]
When (6) holds, the unique actual conjugate vectors are
\[
 v_Y=\delta_Y^*1,\qquad v_h=\xi_h-\delta_Y^*C^*.
 \tag{7}
\]
The criterion does not assert that either adjoint test automatically holds.

There is a separate operator equation associated with a bare full-domain dual.
If any linear E:M->H satisfies [E,h]=0 and [E,Y]=P on M, put
\[
 V=[E,S],\quad A=h^{1/2}Sh^{1/2},\quad U=h^{1/2}Vh^{1/2}.
\]
These are actual maps on M, and
\[
 AU+UA+\mathrm i hUh=h^{1/2}Ph^{1/2}\quad\hbox{on }M.
 \tag{8}
\]
Equation (8) has at most one Hilbert--Schmidt solution.
If, in addition, S>=c1 for a constant c>0, it has an actual Hilbert--Schmidt solution with norm at most 1/(2c), given explicitly in Section 5 below.
Neither this existence nor uniqueness says that every bare witness has Hilbert--Schmidt U.
No implication A-to-F, F-to-A or S-to-A is asserted for the tuple (1).

## Argument

### 1. Sources, actions and generation

The finite-tracial affiliated algebra is used at the checked [AP18 interface in Miy26-U004](../audits/literature/Miy26/Yin_U004.md#miy26-u004).
AP18 Theorem 7.2.8, printed pp.105-106, makes the closed densely defined affiliated operators a star algebra with closure of sums and products; Theorem 7.3.2 identifies L2 vectors with square-integrable affiliated operators.
The registered primary PDF was reread at PDF pp.111-112 for the sum, product and adjoint rules.
These are accepted source interfaces, not a new audit of the foundational proofs.

For a,b in M, the outer action a dot (u tensor v) dot b is (au) tensor (vb).
In L2(N) or L0(N) this is left multiplication by a tensor b^op.
Right multiplication by any fixed affiliated coefficient commutes with these outer actions.
In particular a right-coefficient multiplication of a represented derivation is still a represented derivation into L0(N).
No extension of an arbitrary supplied derivation to a rational closure is assumed.

Generation is direct.
Let N_0=W*(h,Y) and Z=(Y-Y*)/(2i)=hSh.
For epsilon>0, f_epsilon=(h+epsilon)^{-1} belongs to N_0, and
\[
 f_\epsilon Zf_\epsilon=e_\epsilon S e_\epsilon\in N_0,
 \qquad e_\epsilon=h(h+\epsilon)^{-1}.
\]
Regularity gives e_epsilon->1 strongly, and ||e_epsilon||<=1.
Thus e_epsilon S e_epsilon->S strongly, so S belongs to N_0 and N_0=M.
This generation argument uses bounded functional calculus inside a von Neumann algebra.
It does not apply a target derivation to f_epsilon or to S.
In particular A_X is dense in H, and its Hilbert adjoints in (6) are well-defined.

### 2. The affiliated inverse and the actual target derivations

Both summands of Q in (3) are selfadjoint affiliated operators.
Their closed affiliated sum is selfadjoint, since the affiliated star-algebra rule gives Q*=Q.
Thus spectral calculus gives R=(Q+i)^-1 in N with ||R||<=1.
A raw sum on an unspecified intersection of Hilbert domains is not being substituted for this closed sum.

Opposite multiplication gives the exact affiliated identities
\[
 F=(Q+\mathrm i)B,\qquad
 F^{-1}=B^{-1}R,\qquad B\beta=R.
 \tag{9}
\]
Indeed (S tensor b^op)B=Sh tensor 1 and (b tensor S^op)B=1 tensor (hS)^op.
Since h is regular, B is affiliated-invertible, and so is Q+i.
Consequently F is affiliated-invertible as asserted.

Define the maps (4) initially on all of A_0 with values in L0(N).
They are represented derivations: partial_h and partial_S are represented, and the right coefficient actions by beta and beta C commute with the outer actions.
Direct differentiation gives
\[
 \partial_SY=F,\quad
 \partial_SY^*=F-2\mathrm iB,\quad
 \partial_hY^*=C_-:=S\otimes S^{\mathrm{op}}
       -\mathrm i\bigl(1\otimes(Sh)^{\mathrm{op}}+hS\otimes1\bigr).
\]
It follows that (2) holds and
\[
 \delta_Y(Y^*)=1-2\mathrm iR=k,\qquad
 \theta_h(Y^*)=C_- -kC.
 \tag{10}
\]
The Cayley transform k is unitary, and C_-,C belong to N.
Every p in A_X has a finite Leibniz expansion in its three starred generators h,Y,Y*.
All these derivative values and all outer coefficients are bounded.
Hence both restrictions A_X->N are actual Hilbert-tensor-valued derivations.
This conclusion does not require beta in the original coarse Hilbert space.

### 3. The target relation and uniqueness for every coarse-affiliated derivation

Put W=(Y+Y*)/2=ShS and retain Z=hSh.
There is an actual polynomial relation in A_X:
\[
 hWZ=ZWh,
 \tag{11}
\]
since both sides equal hShShSh.

Let zeta:A_X->L0(N) be an outer derivation with zeta h=zeta Y=0.
Set q=zeta(Y*).
Then zeta W=q/2 and zeta Z=i q/2.
Differentiating (11) gives Kq=0, where K is the bounded outer coefficient
\[
 K=h\otimes Z^{\mathrm{op}}-Z\otimes h^{\mathrm{op}}
       +\mathrm i hW\otimes1-\mathrm i1\otimes(Wh)^{\mathrm{op}}.
 \tag{12}
\]
This multiplication acts on q on the left, in contrast to the right coefficients in (4).

To factor K, put
\[
 P_0=h^{1/2}\otimes(h^{1/2})^{\mathrm{op}},\quad
 A=h^{1/2}Sh^{1/2},\quad
 A_1=A\otimes1,\quad A_2=1\otimes A^{\mathrm{op}},\quad T=A_1+A_2.
\]
Here B=P_0^2.
Direct affiliated multiplication gives
\[
 \begin{aligned}
 P_0^{-1}KP_0^{-1}
   &=A_2-A_1+\mathrm i(A_1^2-A_2^2)B^{-1},\\
 K&=\mathrm iP_0(A_1-A_2)(T+\mathrm iB)P_0^{-1},\\
 T+\mathrm iB&=P_0FP_0^{-1}.
 \end{aligned}
 \tag{13}
\]
For the order in the first line, the hW term becomes A^2h^-1 tensor (h^-1)^op=A_1^2B^-1, whereas the Wh term becomes h^-1 tensor (h^-1 A^2)^op=A_2^2B^-1.
Factoring A_1^2-A_2^2 uses only that A_1 and A_2 commute; B need not commute with either.

The selfadjoint operator A has a diffuse spectral law.
Here is the exact maximality input and its scalar consequence.
The original finite-Fisher pair meets [ACSY24-U001, Proposition 3.5](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), hence Delta(h,S)=2.
For every scalar lambda, the formal linear matrix
\[
 \begin{pmatrix}s&\lambda\\1&h\end{pmatrix}
 \tag{14}
\]
is full over the free polynomial algebra: a scalar substitution with sh-lambda nonzero makes it invertible, ruling out any factorization through dimension less than two.
The [MSY23-U002, Theorem 3.1 interface](../audits/literature/MSY23/Yin_U002.md#msy23-u002) therefore makes its evaluation injective, hence invertible in the finite affiliated matrix algebra.
Taking the Schur complement of the regular h shows that S-lambda h^-1, and thus Sh-lambda, is affiliated-invertible.
The identity A-lambda=h^(1/2)(Sh-lambda)h^(-1/2) then shows that A has no scalar eigenvalue.

The joint trace law of A_1 and A_2 is the product of this diffuse law with itself.
The diagonal has zero measure, so A_1-A_2 is regular in N.
Every factor in the second line of (13) is now affiliated-invertible: for T+iB this follows from the last line and (9).
Consequently K is regular and Kq=0 forces q=0.

The difference of any two derivations with the same coordinate values (2) meets this argument.
It vanishes on h,Y,Y*, and thus on all of A_X.
This proves uniqueness among all L0(N)-valued derivations, in particular among all Hilbert-tensor-valued candidate ACSY witnesses.
The proof never differentiates h^-1 or S using an unknown target derivation.

### 4. Exact actual-adjoint criterion

Generation makes A_X dense in H.
Regard delta_Y and theta_h as their actual densely defined Hilbert-space maps with this domain; no closability is presumed.
For p in A_X, tracial cyclicity in N and boundedness of delta_Y(p),C give
\[
 \langle1,\theta_h(p)\rangle_{L^2(N)}
  =\langle\xi_h,p\rangle_H
     -\langle C^*,\delta_Y(p)\rangle_{L^2(N)}.
 \tag{15}
\]
Therefore 1 belongs to the actual adjoint domain of theta_h if and only if C* belongs to that of delta_Y.
In that event theta_h*1=xi_h-delta_Y*C*.
The other coordinate has an actual vacuum precisely when 1 is in Dom delta_Y*.

If the two conditions in (6) hold, the constructed restrictions supply both actual ACSY witnesses, with (7).
Conversely any ACSY witnesses must be these restrictions by Section 3, so their actual vacuum domains imply exactly (6).
This proves both directions at the existential A level.
It does not treat a formal moment functional as an actual L2 vector without the two bounded-functional conditions.

The tensor C* is bounded, but its factors contain S, which need not belong to A_X.
Thus membership of 1 in Dom delta_Y* does not justify membership of C* by the usual algebraic target-coefficient adjoint formula.
This is a real remaining test.
Also beta need not be in L2(N), so writing the vacuum as partial_S*(beta*) without an additional actual-domain argument would be invalid.

### 5. The independent Hilbert--Schmidt equation

First let E:M->H be any bare witness as in the statement, with no continuity or adjoint premise.
Since multiplication by each bounded factor preserves M, V=[E,S] is an actual map M->H, and the product rule gives
\[
 Sh\,V+V\,hS+\mathrm i hVh=P\quad\hbox{on }M.
 \tag{16}
\]
Composing on both sides with left multiplication by h^(1/2), and putting U=h^(1/2)Vh^(1/2), gives (8).

On the Hilbert space S2(H), write L_a and R_a for left and right composition by the bounded left multiplication operator a on H.
Define
\[
 \mathcal T=L_A+R_A,\qquad \mathcal B=L_hR_h.
\]
Then mathcal T is selfadjoint and mathcal B is positive and injective.
A homogeneous Hilbert--Schmidt solution satisfies
\[
 0=\operatorname{Im}\langle U,(\mathcal T+\mathrm i\mathcal B)U\rangle
   =\|h^{1/2}Uh^{1/2}\|_{\mathrm{HS}}^2.
\]
Regularity of h gives U=0, proving uniqueness in this class for every selfadjoint S.

Now assume S>=c1.
Then A>=ch and A is positive regular.
There is a bounded X with
\[
 A^{1/2}X=h^{1/2},\qquad\|X\|\le c^{-1/2}.
 \tag{17}
\]
For the actual range justification, define X* on Ran A^(1/2) by X*A^(1/2)z=h^(1/2)z.
The inequality A>=ch gives its bound, and density of that range extends it to H.
Taking the adjoint proves (17).
This is the elementary majorization-to-factorization step of [Douglas's Theorem 1](../audits/literature/Dou66/readme.md); the full special-case proof just given fixes the range and norm without an extra premise.
The registered 1966 paper, printed pp.413-414, was read for its theorem and this proof step in the institution-hosted original scan.
This is source attribution for the reproduced step; the unbounded-operator Theorem 2 is not used.

The commuting positive operators L_A,R_A have a bounded joint multiplier
\[
 \mathcal Q=(L_A+R_A)^{-1}L_{A^{1/2}}R_{A^{1/2}},
\]
defined by sqrt(st)/(s+t), with value zero at (0,0).
Thus ||mathcal Q||<=1/2 and mathcal T mathcal Q=L_(A^(1/2))R_(A^(1/2)).
Put
\[
 \mathcal D=L_XR_{X^*},\qquad
 J=\mathcal Q\mathcal D.
\]
Equation (17) and its adjoint show, with actual bounded operators on S2(H), that
\[
 \|J\|\le\frac1{2c},\qquad
 \mathcal TJ=\mathcal B^{1/2}.
 \tag{18}
\]
Since mathcal T is injective, (18) proves the actual range inclusion Ran mathcal B^(1/2) subset Ran mathcal T.
It identifies J with the everywhere-defined product mathcal T^-1 mathcal B^(1/2); no formal unbounded product is substituted for this proof.

Let
\[
 C_0=\mathcal B^{1/2}J=J^*\mathcal TJ.
\]
The equality follows by taking adjoints in (18).
Hence C_0 is bounded positive, and ||(I+i C_0)^-1||<=1.
The Hilbert--Schmidt operator
\[
 U=J(I+\mathrm iC_0)^{-1}P
 \tag{19}
\]
is an actual solution, because mathcal B J=mathcal B^(1/2)C_0 gives
\[
 (\mathcal T+\mathrm i\mathcal B)U
   =\mathcal B^{1/2}P=h^{1/2}Ph^{1/2}.
\]
Its norm is at most 1/(2c), since ||P||HS=1.
The homogeneous argument supplies its uniqueness among Hilbert--Schmidt solutions.

## Scope and remaining obligations

The full nonlinear reduction (1)-(7) applies to arbitrary correlated reference pairs with the stated joint finite-Fisher hypothesis.
It settles the represented starred derivations and their uniqueness, but not the two actual vacuum tests.
The positive-S result (19) is an independent range statement.
It does not show that h^(-1/2)Uh^(-1/2) is Hilbert--Schmidt or that U arises from a full-domain dual.
For sign-changing S the positive factorization (17) is unavailable; no inhomogeneous Hilbert--Schmidt range conclusion is claimed there.

A bare E:M->H gives commutators as maps M->H, not as elements of L0(N).
The invertibility of K on the coarse affiliated algebra cannot be applied to an arbitrary such map.
Thus Section 3 does not establish uniqueness of all bare F witnesses, and Hilbert--Schmidt uniqueness in Section 5 must not be used for that purpose.
The generator-first conventions of S and F are obtained from E by D=-E when such an E is available.

No inference here uses the unresolved symmetric-projective-tensor shortcut or a norm-to-measure derivation-extension theorem.
Their precise source concerns and useful exploration remain in the continuing D.
The finite models retained in J_F0008 are diagnostics only, are not premises of this proof, and are not actual finite-Fisher or full-dual counterexamples.

Developer checks covered the two coefficient actions, opposite-factor multiplication, selfadjoint affiliated resolvent, represented target restriction, every factor in (13), the full-linear-pencil interface, actual adjoint equivalence, and the bounded-operator range construction (17)-(19).
Independent review remains required before independent acceptance.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:39 |
| status | open |
| reason | Complete nonlinear derivation construction and uniqueness reduce the full existential ACSY premise to two actual adjoint tests; an independent positive-S weighted Hilbert--Schmidt range result is also proved, with bare-dual limits explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Nonlinear reduction and range statement](#statement) | Generation, unique represented coarse-affiliated coordinate derivations, bounded starred values, exact actual-adjoint criterion and the separately stated Hilbert--Schmidt equation. |
| argument | [Complete argument](#argument) | Five sections, including all coefficient-order calculations, source applications, actual domains and the positive-S range formula. |
| dependency | [Finite affiliated algebra](../audits/literature/Miy26/Yin_U004.md#miy26-u004) | Only its AP18 Theorems 7.2.8 and 7.3.2 interfaces: closed affiliated star algebra and L2 identification. |
| dependency | [ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The original selfadjoint reference conjugate system gives Delta(h,S)=2. |
| dependency | [Full linear matrices](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Theorem 3.1 and finite-tracial kernel/invertibility interface, applied to (14) to prove diffuseness of h^(1/2)Sh^(1/2). |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:46 |
| status | proved |
| reason | Adopt the complete proof after R_F0149 independently checked generation, every affiliated coefficient and uniqueness step, both actual-adjoint directions, and the separately quantified Hilbert-Schmidt range result. The remaining adjoint tests and arbitrary bare-witness problem are not declared solved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Nonlinear reduction and range statement](#statement) | Generation, unique represented coarse-affiliated coordinate derivations, bounded starred values, exact actual-adjoint criterion and the separately stated Hilbert--Schmidt equation. |
| argument | [Complete argument](#argument) | Five sections, including all coefficient-order calculations, source applications, actual domains and the positive-S range formula. |
| dependency | [Finite affiliated algebra](../audits/literature/Miy26/Yin_U004.md#miy26-u004) | Only its AP18 Theorems 7.2.8 and 7.3.2 interfaces: closed affiliated star algebra and L2 identification. |
| dependency | [ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The original selfadjoint reference conjugate system gives Delta(h,S)=2. |
| dependency | [Full linear matrices](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Theorem 3.1 and finite-tracial kernel/invertibility interface, applied to (14) to prove diffuseness of h^(1/2)Sh^(1/2). |
| review | [Independent complete review](../audits/reviews/Yin_R_F0149_v1.md#conclusion) | Entire statement and five-section argument, all three direct dependency scopes, primary Douglas attribution and exact all-witness limitations. |

