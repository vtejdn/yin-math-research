---
author: Yin
---

# Starred-core compact adjoint commutators: weak finite rank implies affiliated rationality

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Weak Finite-Rank Commutators on the Starred Polynomial Core

<a id="statement"></a>

<a id="yin_c_f0025"></a>
## Yin_C_F0025: Small-Core Normal Duals and the Rationality Implication

Date: 2026-09-10.
Authorization: the user requested that the main theorem be reconsidered with the smaller domains in ACSY24 Proposition 3.5.
Human author: Yin.
Proof development: another AI agent, using the normal-coordinate spectral argument independently developed by the coordinating agent and another AI agent.
The compact-commutator refinement was proposed by the coordinating agent and separately checked by another AI agent before integration.
The argument below proves a small-core sufficient criterion for bounded affiliated rationality.
It does not claim the full converse of Yin_C_F0024 under smaller-domain assumptions alone.
The [selected assessment](#current-assessment) records the mathematical and review assessments; no historical-priority or formal-verification claim is made.

## 1. Exact Hypotheses and Conclusion

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal probability trace, and put
\[
H=L^2(M,\tau),\qquad \Omega=1,\qquad P=P_\Omega.
\]
Use the inner product linear in its second variable, $\langle a,b\rangle=\tau(a^*b)$.
Write $\lambda(a)$ and $\rho(a)$ for bounded left and right multiplication by $a\in M$, suppressing $\lambda$ in products.
Let $X=(X_1,\ldots,X_d)$ be a finite bounded normal tuple generating $M$, and distinguish
\[
\mathcal A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
\qquad
A=\mathbb C\langle X_1,\ldots,X_d\rangle.
\]
The starred algebra $\mathcal A$ is dense in $H$; no density assertion is made for $A$.
Put $U=U(M)$ and $F=\operatorname{Div}_U A$.

Suppose complex-linear operators $D_{i,0}$ have domain exactly $\mathcal A$ and satisfy
\[
\Omega\in\operatorname{Dom}D_{i,0}^*,\qquad
[D_{i,0},X_j]z=\delta_{ij}Pz\quad(z\in\mathcal A),
\tag{1}
\]
and suppose every $[D_{i,0},X_j^*]|_{\mathcal A}$ has a compact bounded extension to $H$.
Section 2 proves that these extensions are automatically Hilbert--Schmidt under normality.
Compactness is part of these hypotheses; mere boundedness is not silently substituted.
As proved in Section 2, the adjoint-vacuum condition and the bounded generator commutators already imply $\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*$.
In particular every $D_{i,0}$ is closable.
Write $D_i=\overline{D_{i,0}}$.

For $f\in M$ define the weak commutator form on $\mathcal A\times\mathcal A$ by
\[
\beta_i^f(p,q)
=\langle D_{i,0}^*p,fq\rangle
 -\langle f^*p,D_{i,0}q\rangle.
\tag{2}
\]
Every vector in this formula exists without requiring $fq\in\operatorname{Dom}D_i$ or $f^*p\in\operatorname{Dom}D_i^*$.
Say that this form has a **bounded finite-rank representative** if there is $T_i\in B(H)$ with finite-dimensional range such that
\[
\beta_i^f(p,q)=\langle p,T_iq\rangle
\qquad(p,q\in\mathcal A).
\tag{3}
\]
Density makes the representative unique.
Equivalently, the form is bounded in the two Hilbert norms and the ranks of all finite matrices $(\beta_i^f(p_r,q_s))_{r,s}$ have a common finite bound.
Indeed boundedness extends the form to an operator on $H$, and a rank bound on all finite test matrices gives the same rank bound for that operator by density.
Algebraic finite rank of an unbounded form on $\mathcal A$ alone is not the condition in (3).

Then $\Delta(X)=d$, the accepted MSY23 theorem identifies $F$ with the embedded free skew field, and
\[
\boxed{
f\in M,\quad \beta_i^f\text{ has a bounded finite-rank representative for every }i
\quad\Longrightarrow\quad f\in F.
}
\tag{4}
\]
In particular, (4) applies if $f$ preserves every $\operatorname{Dom}D_i$ and $[D_i,f]$ there is the restriction of a bounded finite-rank operator.
The proof establishes neither the reverse implication in (4) nor an equivalence between weak forms and the latter full-domain condition under (1) alone.

## 2. Normalization and the Exact ACSY24 Interface

First the commutator product rule on the invariant algebra $\mathcal A$ gives, for every $a\in\mathcal A$, a unique compact bounded extension $T_{i,a}$ of $[D_{i,0},a]$.
Every word in the generators and their adjoints gives a finite sum of bounded multipliers composed with the specified compact generator commutators.
Any two word presentations agree as operators on the dense domain $\mathcal A$, so their bounded extensions agree.
The adjoint-vacuum hypothesis now gives, for $a\in\mathcal A$,
\[
D_{i,0}^*a=aD_{i,0}^*\Omega-T_{i,a^*}^*\Omega.
\]
Indeed for $q\in\mathcal A$, apply the vacuum adjoint identity to $a^*q$ and use $D_{i,0}(a^*q)=a^*D_{i,0}q+T_{i,a^*}q$.
The displayed $H$ vector represents the functional $q\mapsto\langle a,D_{i,0}q\rangle$.
This proves $\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*$ and closability, rather than imposing either as an extra hypothesis.

For each $i$, set $\eta_i=D_{i,0}\Omega$ and define $N_i z=z\eta_i$ on $\mathcal A$.
For $p\in\mathcal A$, traciality gives
\[
N_i^*p=p\eta_i^*\in H.
\]
The normalized maps $E_{i,0}=D_{i,0}-N_i$ therefore still satisfy (1), have the same commutators with all left multipliers from $\mathcal A$, and satisfy $E_{i,0}\Omega=0$.
Their adjoints on $\mathcal A$ are $E_{i,0}^*p=D_{i,0}^*p-p\eta_i^*$.
For any bounded $f$ and $p,q\in\mathcal A$, the change in (2) is zero, because
\[
\langle p\eta_i^*,fq\rangle
=\tau(\eta_i p^*fq)
=\tau(p^*fq\eta_i)
=\langle f^*p,q\eta_i\rangle.
\tag{5}
\]
Thus the weak forms, and in particular condition (3), are unchanged by normalization.
For the rest of the proof relabel the normalized maps as $D_{i,0}$.

Let $Jz=z^*$ and use the Hilbert--Schmidt identification
\[
\Theta(g\otimes h)z=g\langle Jh,z\rangle,
\qquad
\Theta(a\otimes b)=aPb.
\tag{6}
\]
It extends to a unitary from $H\otimes_2H$ to $S_2(H)$ and identifies the algebraic tensor product with the finite-rank operators.
Its outer bimodule convention is
\[
a\cdot(g\otimes h)\cdot b=ag\otimes hb.
\]

We first establish maximal Delta using only boundedness of these commutators, before using compactness to obtain the Hilbert--Schmidt source interface.
Fix $i$, let $D$ be the closure of the normalized $D_{i,0}$, and put $B_{ij}=T_{i,X_j^*}$.
Graph approximation on $\mathcal A$ proves that each $a\in\mathcal A$ preserves $\operatorname{Dom}D$ with $[D,a]=T_{i,a}$ there.
Adjoint pairing applied to $a^*$ shows that $a$ also preserves $\operatorname{Dom}D^*$ and that $[D^*,a]=-T_{i,a^*}^*$.
For the selfadjoint doubling and a diagonal coordinate multiplier, put
\[
S=\begin{pmatrix}0&D^*\\D&0\end{pmatrix},
\qquad Z_j=\operatorname{diag}(X_j,X_j),
\qquad C_j=[S,Z_j]
=\begin{pmatrix}0&-B_{ij}^*\\\delta_{ij}P&0\end{pmatrix}.
\]
The bounded-regularization calculation reconstructed in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) gives, with $R_t=(1+tS^2)^{-1}$,
\[
[SR_t,Z_j]=R_tC_jR_t-tSR_tC_jSR_t.
\]
This follows from the sum of the resolvents at $\pm i/\sqrt t$ and uses no assertion about invariance of $\operatorname{Dom}S^2$.
Spectral calculus gives $R_t\to I$ strongly and $\sqrt t\,SR_t\to0$ strongly with norm at most $1/2$.
The displayed commutators therefore converge strongly to $C_j$, even when their entries are only bounded.
Their lower-left blocks yield bounded $D_{i,t}=D(1+tD^*D)^{-1}$ such that $[D_{i,t},X_j]\to\delta_{ij}P$ strongly.

If finite-rank operators $Q_k$ satisfy $\sum_k[Q_k,X_k]=0$, ordinary bounded trace cyclicity gives, for arbitrary $V,W\in M'$,
\[
0=\sum_k\operatorname{Tr}(Q_kV[X_k,D_{i,t}]W).
\]
Strong convergence suffices for the finite-rank trace pairings, and its limit is $-\operatorname{Tr}(Q_iVPW)=0$.
The independent dense commutant-vector tests imply $Q_i=0$.
The finite-rank-cycle characterization in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) therefore proves $\Delta(X)=d$.
The accepted [MSY23 free-field interface](../audits/literature/MSY23/Yin_U004.md#msy23-u004) identifies $F$ with the embedded free skew field.
In particular every $X_j-c$, $c\in\mathbb C$, is injective, because the nonzero formal element $x_j-c$ is a unit of that field.
Normality therefore makes the spectral distribution $\mu_j$ of $X_j$ nonatomic.

On $L^2(W^*(X_j))\otimes_2L^2(W^*(X_j))$, let $v_j$ be the vector represented by
\[
\frac{\bar z-\bar w}{z-w}\quad(z\ne w),
\]
with value zero on the null diagonal.
It is square integrable, of absolute value one almost everywhere.
The Hilbert--Schmidt operator $S_j=\Theta(v_j)$ satisfies
\[
[X_j,S_j]=[X_j^*,P],
\]
as multiplication by $z-w$ on that abelian tensor subspace cancels its displayed denominator.
On the other hand, differentiating $[X_j,X_j^*]=0$ by the core commutator with $D_{i,0}$ gives
\[
[X_j,B_{ij}]=\delta_{ij}[X_j^*,P].
\]
Thus $B_{ij}-\delta_{ij}S_j$ is a compact operator commuting with the bounded normal $X_j$.
There is no nonzero such compact operator.
Indeed, for $C=B_{ij}-\delta_{ij}S_j$, bounded Fuglede gives commutation of $C$ with $X_j^*$ as well as $X_j$, so the positive compact operator $C^*C$ commutes with $X_j$ and $X_j^*$.
A nonzero positive eigenvalue of $C^*C$ would have a nonzero finite-dimensional reducing eigenspace.
The restriction of $X_j$ to that space would have an eigenvector, contrary to the injectivity of every $X_j-c$.
Consequently
\[
B_{ij}=\delta_{ij}S_j\in S_2(H).
\]
The compact-to-Hilbert--Schmidt upgrade has now been proved without assuming it in the maximal-Delta step.

All extensions $T_{i,a}$ are therefore Hilbert--Schmidt by the same word product rule, and they are unchanged by normalization.
Consequently
\[
\partial_i a=\Theta^{-1}(T_{i,a})
\tag{7}
\]
is a well-defined derivation $\mathcal A\to H\otimes_2H$ with $\partial_iX_j=\delta_{ij}1\otimes1$.
Normalization and application of the commutator to $\Omega$ give
\[
D_{i,0}a=T_{i,a}\Omega=(\mathrm{id}\otimes\tau)\partial_i a.
\tag{8}
\]
Moreover
\[
\langle1\otimes1,\partial_i a\rangle
=\langle\Omega,D_{i,0}a\rangle
=\langle D_{i,0}^*\Omega,a\rangle,
\tag{9}
\]
so $1\otimes1\in\operatorname{Dom}\partial_i^*$.

Conversely, derivations satisfying ACSY24 Proposition 3.5 on $\mathcal A$ produce (1) by its Theorem 3.4 and (8).
For completeness, if $\xi_i=\partial_i^*(1\otimes1)$, its adjoint calculation is
\[
D_{i,0}^*a
=a\xi_i-\bigl(\Theta(\partial_i(a^*))\bigr)^*\Omega,
\qquad a\in\mathcal A.
\tag{10}
\]
The term on the right is an $H$ vector because $\Theta(\partial_i(a^*))$ is Hilbert--Schmidt and hence bounded.
This identity follows by using $[D_{i,0},a^*]=\Theta(\partial_i(a^*))$ and $D_{i,0}^*\Omega=\xi_i$ on polynomial test vectors.
It makes $\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*$ explicit.
Thus, for the normal tuples in this theorem, the compact-commutator operator hypotheses used here are equivalent, up to the harmless normalization (5), to the small-core derivation hypotheses of the source.
No affiliation of $D_i$ with $M$ is asserted.

The exact source and the additional domain-safe regularization proof are recorded in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), published pp. 34--36.
The source derivation formulation independently recovers the maximal-Delta conclusion already established above from bounded commutators.
This argument does not use the all-$M$ domain theorem Yin_C_F0024 to establish maximal Delta.

## 3. Normality Forces the Adjoint Derivatives

For every $i$ and $c\in\mathbb C$, the nonzero formal polynomial $x_i-c$ is a nonzero element of the embedded field $F$.
Its value $X_i-c$ is therefore invertible in $U$ and has zero kernel on $H$.
As $X_i$ is normal, its scalar spectral distribution $\mu_i$ has no atoms.

On the coarse Hilbert tensor product define the bounded normal operator
\[
L_i=\lambda(X_i)\otimes I-I\otimes\rho(X_i).
\tag{11}
\]
It is injective.
To see this, the commuting spectral actions of its two terms have scalar joint distribution $\mu_i\times\mu_i$ in the faithful product trace.
The projection onto the kernel is the joint spectral projection of the diagonal $z=w$.
This diagonal has product measure zero because $\mu_i$ is nonatomic, and faithfulness makes its spectral projection zero.
Equivalently, this reasoning can be applied to the abelian von Neumann algebra generated by those two tensor-leg actions; its restricted product trace is faithful.

Differentiate $X_iX_i^*=X_i^*X_i$ with $\partial_j$.
The outer module rule gives
\[
L_i(\partial_jX_i^*)
=\delta_{ij}(X_i^*\otimes1-1\otimes X_i^*).
\tag{12}
\]
Let $B_i=W^*(X_i)$ and identify $L^2(B_i)\otimes_2L^2(B_i)$ with $L^2(\mu_i\times\mu_i)$.
This is a reducing subspace for $L_i$, on which $L_i$ is multiplication by $z-w$.
The function
\[
k_i(z,w)=\frac{\bar z-\bar w}{z-w}\quad(z\ne w),
\qquad k_i(z,z)=0,
\tag{13}
\]
has absolute value one away from the null diagonal and determines a vector $v_i$ in this reducing subspace.
It solves $L_iv_i=X_i^*\otimes1-1\otimes X_i^*$.
Injectivity of $L_i$ on the entire coarse Hilbert space now gives the exact identities
\[
\partial_jX_i^*=\delta_{ij}v_i.
\tag{14}
\]
In particular no unspecified component of an adjoint derivative remains outside the abelian tensor subspace.

## 4. The Fundamental Identity on the Small Core

Define a second bounded operator on the coarse tensor product by
\[
B_i^{\mathrm{in}}=\rho(X_i)\otimes I-I\otimes\lambda(X_i).
\tag{15}
\]
It commutes with every outer left and right module action, since left and right multiplication commute on each tensor leg.
On $L^2(B_i)\otimes_2L^2(B_i)$ its action agrees with $L_i$, because $B_i$ is abelian.
Hence
\[
B_i^{\mathrm{in}}(1\otimes1)=X_i\otimes1-1\otimes X_i,
\qquad
B_i^{\mathrm{in}}v_i=X_i^*\otimes1-1\otimes X_i^*.
\tag{16}
\]

The map $\delta=\sum_i B_i^{\mathrm{in}}\partial_i$ is a derivation from $\mathcal A$ into the outer coarse bimodule.
Equations (14)--(16) show that it agrees, on every starred generator, with the inner derivation $a\mapsto a\otimes1-1\otimes a$.
The Leibniz rule therefore gives
\[
\sum_i B_i^{\mathrm{in}}\partial_i a
=a\otimes1-1\otimes a\qquad(a\in\mathcal A).
\tag{17}
\]

Set $R_i=\rho(X_i)$ and define on $\mathcal A$
\[
K_0=\sum_i(R_iD_{i,0}-D_{i,0}R_i).
\tag{18}
\]
Every input to $D_{i,0}$ in this expression belongs to $\mathcal A$.
Contracting (17) with $\mathrm{id}\otimes\tau$ gives the bounded identity
\[
\boxed{K_0a=(1-d)a-\tau(a)\Omega\qquad(a\in\mathcal A).}
\tag{19}
\]
Indeed the contraction of the first part of $B_i^{\mathrm{in}}\partial_i a$ is $(D_{i,0}a)X_i$.
By the Leibniz rule,
\[
D_{i,0}(aX_i)
=(\mathrm{id}\otimes\tau)((\partial_i a)\cdot X_i)+a.
\]
Traciality on the second tensor leg makes the other contracted part equal to $D_{i,0}(aX_i)-a$.
Thus the left side of (17) contracts to $K_0a+da$, while its right side contracts to $a-\tau(a)\Omega$.

Write $K=(1-d)I-P$ for the bounded extension in (19).
The formal adjoint expression
\[
K_0^{\mathrm{form},*}p
=\sum_i\bigl(D_{i,0}^*R_i^*p-R_i^*D_{i,0}^*p\bigr)
\tag{20}
\]
is defined for all $p\in\mathcal A$, because $R_i^*p=pX_i^*\in\mathcal A$.
Pairing (20) against $q\in\mathcal A$ gives $\langle K_0^{\mathrm{form},*}p,q\rangle=\langle p,K_0q\rangle$.
Density and (19) therefore identify (20) with $K^*p$.
This step does not assert that any individual right multiplier preserves the domain of a closed $D_i$.

## 5. Weak Commutators Give the Tensor Identity

Let $f\in M$ satisfy (3), and let $T_i$ be the bounded finite-rank representatives.
For $p,q\in\mathcal A$, right multiplication commutes with the bounded left multipliers $f,f^*$, so direct expansion of (2) gives
\[
\begin{aligned}
\sum_i\langle p,[R_i,T_i]q\rangle
&=\sum_i\bigl(\beta_i^f(R_i^*p,q)-\beta_i^f(p,R_iq)\bigr)\\
&=\left\langle
\sum_i(D_{i,0}^*R_i^*-R_i^*D_{i,0}^*)p,fq
\right\rangle\\
&\qquad-\left\langle f^*p,
\sum_i(R_iD_{i,0}-D_{i,0}R_i)q
\right\rangle\\
&=\langle K^*p,fq\rangle-\langle f^*p,Kq\rangle\\
&=\langle p,(fP-Pf)q\rangle.
\end{aligned}
\tag{21}
\]
All applications of $D_{i,0}$ and $D_{i,0}^*$ use vectors in the stated core or adjoint domain.
In particular the computation never applies $D_i$ to $fq$.
Every operator left in the first and last lines of (21) is bounded, so density yields
\[
\sum_i[R_i,T_i]=fP-Pf\quad\text{on }H.
\tag{22}
\]

Write $T_i=\sum_\alpha\Theta(g_{i\alpha}\otimes h_{i\alpha})$ with $g_{i\alpha},h_{i\alpha}\in H$.
The finite-tensor interface gives
\[
[\rho(x),\Theta(g\otimes h)]
=\Theta(gx\otimes h-g\otimes xh).
\]
Thus (22) is exactly
\[
f\otimes1-1\otimes f
=\sum_{i,\alpha}
\bigl(g_{i\alpha}X_i\otimes h_{i\alpha}
      -g_{i\alpha}\otimes X_ih_{i\alpha}\bigr)
\tag{23}
\]
in the algebraic tensor product $H\otimes_{\mathbb C}H$.

The canonical linear inclusion $H\hookrightarrow U$ gives an injective map of complex algebraic tensor products into $U\otimes_{\mathbb C}U$.
Pass from there to $U\otimes_FU$.
Each right-hand summand of (23) vanishes by balancing, and hence
\[
f\otimes_F1=1\otimes_Ff.
\tag{24}
\]
If $f\notin F$, then $1,f$ are right-$F$ linearly independent in $U$.
Indeed a relation $a+fb=0$ with $b\ne0$ would give $f=-ab^{-1}\in F$.
Extend $1,f$ to a right-$F$ basis and choose a right-$F$ linear map $\phi:U\to F$ with $\phi(1)=0$ and $\phi(f)=1$.
Applying $\phi\otimes\mathrm{id}$ to (24), and identifying $F\otimes_FU$ with $U$, gives $1=0$.
This contradiction proves (4).

## 6. Domain Interpretation and Standard Corollaries

For the original, possibly unnormalized operators of Section 1, if $f\operatorname{Dom}D_i\subseteq\operatorname{Dom}D_i$ and $[D_i,f]$ on that domain equals a bounded finite-rank operator $T_i$, then for $p,q\in\mathcal A$
\[
\beta_i^f(p,q)
=\langle p,D_i(fq)-fD_iq\rangle
=\langle p,T_iq\rangle.
\]
Thus the actual closed-domain condition implies the weak condition and consequently affiliated rationality.
The reverse passage is not part of this theorem.
Although $\mathcal A$ is a core for $D_i$ by definition, it need not be a core for $D_i^*$ from the hypotheses stated here.
Testing the first variable only on $\mathcal A$ therefore does not automatically establish membership in $\operatorname{Dom}D_i=(D_i^*)^*$.

For bounded selfadjoint generators with $L^2$ conjugate variables, the normalized polynomial duals satisfy (1), and their adjoint-generator commutators are already $\delta_{ij}P$.
Consequently (4) applies directly on their polynomial core.
The additional all-$M$ domain estimates in [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002) recover the full equivalence and domain interpretations of [Yin_C_F0022](Yin_C_F0022_v1.md#yin_c_f0022) for this standard case.
This includes the finite-dimensional q-Gaussian tuples for $-1<q<1$ through their known finite-Fisher property.
The present proof does not transfer those additional estimates to arbitrary normal tuples.

For free Haar generators the bounded terminal-deletion duals have $[D_i,U_j]=\delta_{ij}P$ and
\[
[D_i,U_j^*]=-\delta_{ij}U_j^*PU_j^*.
\]
They therefore satisfy the small-core hypotheses, including the Hilbert--Schmidt adjoint commutators.
Their complete bounded-dual criterion remains available from [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013).
The sign convention and group-word calculation are recorded in [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005).

## 7. What Remains Outside This Statement

The proof establishes the small-core implication (4), with automatic maximal Delta and a normality-based fundamental identity on the actual starred core.
It does not prove that every $f\in F\cap M$ has the bounded finite-rank representatives in (3) under these hypotheses alone.
It also does not define cleared defects $sD_i(bz)-aD_i(tz)$ on arbitrary bounded vectors for arbitrary bounded affiliated fractions.
Those terms require domain information that a starred polynomial core does not itself provide.

The whole-$M$ assumptions of [Yin_C_F0024](Yin_C_F0024_v1.md#yin_c_f0024) remain sufficient for its full affiliated equivalence.
Nothing here converts affiliated rationality into bounded scalar division closure, asserts $F\cap L^2\subseteq M$, or replaces cleared defects for arbitrary affiliated elements by raw weak commutators.
The pre-existing Yin_C_F0012 and Yin_C_F0014 obstructions retain their original scopes.

The proof consumes the reviewed ACSY24 small-core/maximal-Delta interface, the accepted MSY23 free-field realization, bounded Fuglede, normal spectral calculus in the coarse bimodule, and the finite-tensor identification.
Its new finite-rank-to-rational step is (21)--(24), after the small-core identity (19).
No use of Yin_C_F0024's full-domain theorem is hidden inside that step.
The [complete artifact review](../audits/reviews/Yin_R_F0014_v1.md) records the actual inspected scope, final assessment, and preliminary contributions disclosed above.

Revision, 2026-09-10: the initial Hilbert--Schmidt hypothesis draft, was broadened to compact adjoint-generator commutators before promotion of the claim.
The added proof first obtains maximal Delta from bounded commutators alone, then uses diffuseness, normality, and compact rigidity to recover the exact Hilbert--Schmidt source interface.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-normalization-and-the-exact-acsy24-interface) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0014_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:41 |
| status | proved |
| reason | Select the actual retained findings and their individual checking relationships, with unchanged mathematical status, statement and argument. Original findings, dates, accepted-source depths and historical decisions remain intact; this is no new mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-normalization-and-the-exact-acsy24-interface) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0014_v1.md#small-core-rationality-finding) | Complete compact small-core theorem and operator/coarse equivalence, automatic maximal Delta and Hilbert--Schmidt upgrade, exact normal phase/tensor descent, with the arbitrary bounded-fraction converse and all-M domain claims withheld. |

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

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0014_v1.md).

Material covered by that review: [Exact material](Yin_C_F0025_v1.md).
