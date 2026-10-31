---
author: Yin
---

# Normal-tuple affiliated criterion with dual and adjoint domains containing M

## Current assessment
[Selected decision](#decision-theorem-role-2026-10-10)

## Affiliated Rationality for Normal Tuples with Duals on Bounded Vectors

<a id="statement"></a>

<a id="yin_c_f0024"></a>
## Yin_C_F0024: An Abstract Main Theorem with Automatic Free-Field Realization

Date: 2026-09-10.
Authorization: the user requested broad dual-system hypotheses including normal generators, with the selfadjoint finite-Fisher case as an automatic corollary.
Human author: Yin.
Proof development: the coordinating agent, incorporating independently developed preliminary arguments from another AI agent and another AI agent.
This statement generalizes [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013) and [Yin_C_F0022](Yin_C_F0022_v1.md#yin_c_f0022), whose recorded statements and proofs remain unchanged.
The [Current assessment](#current-assessment) identifies the selected material decision.
This is a project deduction, with no historical priority or formal-verification claim.

## 1. Hypotheses and Conclusions

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal probability trace, and let
\[
H=L^2(M,\tau),\qquad \Omega=1,\qquad P=P_\Omega.
\]
Identify $M\Omega$ with $M\subset H$.
Use the inner product linear in its second variable, $\langle a,b\rangle=\tau(a^*b)$.
Write $\lambda(x)$ and $\rho(x)$ for bounded left and right multiplication by $x\in M$; suppress $\lambda$ in products.

Let $X=(X_1,\ldots,X_d)$ be a finite tuple of bounded **normal** operators with $M=W^*(X)$.
Suppose complex-linear operators $D_i$ with the common dense domain exactly $M\Omega$ satisfy
\[
M\Omega\subseteq\operatorname{Dom}D_i^*,
\qquad
D_i(X_jz)-X_jD_i z=\delta_{ij}\tau(z)\Omega
\quad(z\in M).
\tag{1}
\]
Equivalently one can start with operators on larger domains, require both domains to contain $M\Omega$ and the displayed identities there, and then restrict to $M\Omega$.
All conclusions below concern these restrictions and their closures $\widehat D_i=\overline{D_i}$.

No boundedness on $H$, vacuum normalization, separate continuity estimate, or maximal-Delta assumption is imposed.
No density of the holomorphic polynomial algebra $A=\mathbb C\langle X\rangle$ in $H$ is imposed.
In particular, adjoints of the generators are not silently adjoined to $A$.

Put $U=U(M)$, the finite-tracial affiliated algebra, and $F=\operatorname{Div}_{U}A$.
Then:

1. $\Delta(X)=d$, and the accepted MSY23 theorem identifies $F$ with an embedded free skew field.
2. For every $u\in U$, choose bounded fractions
   \[
   u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
   \qquad s,t\text{ regular}.
   \tag{2}
   \]
   Here regular means invertible in $U$, equivalently bounded injective with dense range on $H$.
   Define the cleared defects on the common domain $M$ by
   \[
   T_i z=sD_i(bz)-aD_i(tz).
   \tag{3}
   \]
   Then $u\in F$ if and only if every $T_i$ has finite-dimensional range, for some, equivalently every, fraction pair (2).
   Every such finite-rank defect has a unique bounded finite-rank extension to $H$.
3. In particular,
   \[
   F\cap M=\{f\in M:[D_i,f]|_M\text{ has finite rank for all }i\}.
   \tag{4}
   \]
   Equivalently, $f\operatorname{Dom}\widehat D_i\subseteq\operatorname{Dom}\widehat D_i$ and $[\widehat D_i,f]$ on that full domain is the restriction of a bounded finite-rank operator, for every $i$.

These are sufficient hypotheses, not a claimed characterization of all possible unbounded dual systems.
The adjoint-domain requirement in (1) is a genuine extra condition beyond merely writing an algebraic dual relation on a small core.

## 2. The Analytic Estimates Are Automatic

Because $\operatorname{Dom}D_i^*$ contains the dense space $M$, each $D_i$ is closable.
Its Hilbert closure agrees with $D_i$ at every vector of $M$.
Viewed as a linear map from the Banach space $(M,\|\cdot\|)$ to $H$, $D_i$ has closed graph: if $z_n\to z$ in operator norm and $D_i z_n\to v$ in $H$, then $(z,v)$ belongs to the graph of $\widehat D_i$, and $z\in M$ forces $v=D_i z$.
The closed graph theorem therefore supplies a finite constant $c_i$ with
\[
\|D_i z\|_2\le c_i\|z\|\qquad(z\in M).
\tag{5}
\]
The adjoint $D_i^*$ is closed, and the same argument applied to its restriction to all of $M$ gives a finite $c_i'$ with
\[
\|D_i^*z\|_2\le c_i'\|z\|\qquad(z\in M).
\tag{6}
\]
Thus neither estimate is an additional hypothesis.

We repeatedly use bounded-set weak continuity:
\[
z_\alpha\to z\text{ in }H,\quad z_\alpha,z\in M,
\quad\sup_\alpha\|z_\alpha\|<\infty
\quad\Longrightarrow\quad
D_i z_\alpha\rightharpoonup D_i z.
\tag{7}
\]
Indeed, pair first against $\eta\in\operatorname{Dom}D_i^*$ and use $\langle\eta,D_i z_\alpha\rangle=\langle D_i^*\eta,z_\alpha\rangle$.
The test domain is dense and (5) bounds the images uniformly, so the convergence holds against all of $H$.
The analogous assertion for $D_i^*|_M$ follows using the dense domain of $\widehat D_i$ and (6).
Finite sums and compositions with fixed bounded left or right multipliers inherit (7).

## 3. Maximal Delta from Dual Identities on All Bounded Vectors

This section needs only the maps $D_i:M\to H$ and the generator relations in (1).
It needs neither normality, adjoint domains, nor continuity of those maps.
It extends the bounded-dual trace mechanism of MSY23 Proposition 6.2 by first moving each finite-dimensional range into the domain.

We use the accepted finite-rank-cycle characterization from [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002): $\Delta(X)=d$ is equivalent to
\[
\sum_i[T_i,X_i]=0,\quad T_i\in\operatorname{FinRank}(H)
\quad\Longrightarrow\quad T_i=0\text{ for all }i.
\tag{8}
\]
This left-multiplication version is equivalent to the source's right-multiplication definition by conjugation and adjoints.
The source allows arbitrary bounded tuples.

First recall a finite-tracial fraction fact.
Every finite family $g_1,\ldots,g_N\in H\subset U$ admits one bounded regular $r\in M$ such that $g_k r\in M$ for all $k$.
Write $g_k=b_k t_k^{-1}$ with bounded $b_k$ and bounded regular $t_k$.
For two regular denominators, write the affiliated unit $t_1^{-1}t_2=pq^{-1}$ with $p,q$ bounded regular; then $t_1p=t_2q$ is a regular common right multiple.
Induction gives $r=t_k c_k$ with every $c_k\in M$, so $g_k r=b_k c_k\in M$.
These elementary fraction facts are also reconstructed in Yin_C_F0013 Section 3 and [Miy22-U006](../audits/literature/Miy22/Yin_U006.md#miy22-u006).

Suppose the cycle in (8) is given.
Choose the $g_k$ as a basis of the finite-dimensional space $\sum_i\operatorname{Ran}T_i$, and choose $r$ as above.
The bounded right multiplier $Q=\rho(r)$ is injective: $vr=0$ for $v\in H\subset U$ implies $v=0$ by invertibility of $r$ in $U$.
Moreover every $QT_i$ has range contained in $M$.

For arbitrary $c,e\in M$, put
\[
S_i=\rho(c)QT_i\rho(e).
\]
All right multipliers commute with every left $X_i$, so the $S_i$ still satisfy the cycle identity and still have their ranges in $M$.
Each literal composition $D_j S_i$ is an everywhere-defined bounded finite-rank operator: a finite basis of $\operatorname{Ran}S_i\subset M$ expresses it as a finite sum of bounded coordinate functionals with fixed vectors $D_j g$.
The same domain observation applies to $D_j X_i S_i$ and $D_j S_i X_i$.
Applying $D_j$ to the cycle and using (1) consequently gives the identity of bounded finite-rank operators
\[
0=\sum_i\bigl(D_jS_iX_i-D_jX_iS_i\bigr)
 =\sum_i[D_jS_i,X_i]-PS_j.
\tag{9}
\]
Only now take the ordinary operator trace.
Cyclicity involves the bounded finite-rank $D_jS_i$ and bounded $X_i$, so it is legitimate and gives
\[
0=\operatorname{Tr}(PS_j)
 =\langle\rho(c)^*\Omega,QT_j\rho(e)\Omega\rangle.
\tag{10}
\]
The two test-vector families are independently dense in $H$, since they are $c^*$ and $e$ with $c,e\in M$.
Hence $QT_j=0$, and injectivity of $Q$ gives $T_j=0$.
This proves (8), and therefore $\Delta(X)=d$.

The accepted MSY23 Theorem 1.1 free-field equivalence, at [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004), now identifies $F$ with the free skew field on the specified $d$ generators.
In particular $F$ is a division subring of $U$.
No finite-Fisher or selfadjoint entropy comparison is needed for this deduction.
Equation (9) never takes the trace of an uncontrolled product involving an unbounded $D_j$.

## 4. Normality and a Banach-Space Liouville Argument

On $M$ define
\[
R_i=\rho(X_i),\qquad
K=\sum_i(R_iD_i-D_iR_i),\qquad C=K+P.
\tag{11}
\]
All terms are defined because bounded right multiplication preserves $M$.
By (5), $C$ is a bounded linear map from $M$ with its operator norm to $H$ with its Hilbert norm.
It also has the bounded-set weak continuity (7).

Traciality gives $[R_j,P]=[X_j,P]$ for any bounded $X_j$.
Jacobi's identity on the common invariant inputs $M$, together with (1), gives
\[
[K,X_j]=[R_j,P]=[X_j,P],\qquad [C,X_j]=0\quad\text{on }M.
\tag{12}
\]
The fact that outputs of $D_i$ need not lie in $M$ causes no issue here: all subsequent multipliers on such outputs are bounded operators on $H$.

Fix a normal $x=X_j$.
The function
\[
\mathcal E(z)=\lambda(e^{zx^*})\,C\,\lambda(e^{-zx^*})
\quad(z\in\mathbb C)
\tag{13}
\]
is entire with values in the Banach space $B(M_{\infty},H_2)$.
The left multiplier on the right of $C$ acts on $M$; the left multiplier on its left acts on $H$.
Equation (12) implies that $C$ intertwines the two exponentials of $x$.
Since $x$ is normal, (13) can therefore be written as
\[
\mathcal E(z)
 =\lambda(e^{zx^*-\bar z x})\,C\,
   \lambda(e^{-zx^*+\bar z x}).
\tag{14}
\]
Both exponentials in (14) are unitary elements of $M$.
Their left actions are isometries on $H_2$ and on $M_\infty$, respectively, so $\|\mathcal E(z)\|\le\|C\|$ uniformly.
Applying scalar Liouville to every continuous linear functional on this Banach space shows that $\mathcal E$ is constant.
Differentiating at zero gives $[C,x^*]=0$ on $M$.

Consequently $C$ intertwines left multiplication by every element of the star algebra $\mathbb C\langle X,X^*\rangle$.
For $a\in M$, choose uniformly bounded star-polynomials $a_\alpha$ converging to $a$ in $L^2$, by Kaplansky density and norm approximation in $C^*(X)$.
For fixed $z\in M$, the left side of $C(a_\alpha z)=a_\alpha Cz$ converges weakly to $C(az)$ by (7).
The right side converges strongly to $aCz$: uniformly bounded $L^2$ convergence of the $a_\alpha$ gives strong convergence of their left multipliers on $H$, by approximating an arbitrary $H$ vector with bounded vectors.
Thus
\[
C(az)=aCz\qquad(a,z\in M).
\tag{15}
\]
In particular $Cz=zC\Omega$, but $C\Omega$ need not be bounded and no bounded extension of $C$ to all $H$ is asserted.
This replaces ordinary Hilbert-space Fuglede by a valid argument in $B(M_\infty,H_2)$.

## 5. Closability, Finite Rank, and Denominator Independence

For any fractions (2), the defects (3) satisfy, for $\eta,z\in M$,
\[
\langle\eta,T_i z\rangle
 =\left\langle b^*D_i^*(s^*\eta)-t^*D_i^*(a^*\eta),z\right\rangle.
\tag{16}
\]
Thus $M\subseteq\operatorname{Dom}T_i^*$, and $T_i$ is closable.
It has an infinity-to-$L^2$ bound by (5), and bounded-set weak continuity by (7).

A densely defined closable operator $T$ with finite-dimensional range $E$ has a bounded finite-rank extension.
Indeed the projection of the dense linear space $\operatorname{Dom}T^*$ onto $E$ is a dense linear subspace of a finite-dimensional space, hence all of $E$.
For an orthonormal basis $e_j$ of $E$, choose $\eta_j\in\operatorname{Dom}T^*$ with projection $e_j$.
Then $\langle e_j,Tz\rangle=\langle T^*\eta_j,z\rangle$ bounds each coordinate in the Hilbert norm.
The finite sum gives the extension, and density gives uniqueness.

The following cancellation step is necessary for an initially unbounded defect.
Suppose $y,y'\in M$ are regular and $yTy'$ has finite rank on $M$, where $T$ has the continuity and closability just established.
Injectivity of $y$ puts $T(y'M)$ in a fixed finite-dimensional space $E$.
Write $y'=v|y'|$, with $v$ unitary, and put
\[
e_n=1_{[1/n,\infty)}(|y'|),\quad p_n=ve_nv^*,\quad
w_n=|y'|^{-1}e_nv^*z\in M\quad(z\in M).
\]
Then $y'w_n=p_nz\to z$ in $L^2$ and $\|p_nz\|\le\|z\|$.
Weak continuity gives $T(p_nz)\rightharpoonup Tz$, and weak closedness of $E$ puts $Tz$ in $E$.
Thus $T$ has finite rank and consequently a bounded extension.

For two fraction pairs for the same $u$, common regular left and right multiples give bounded regular $x,y,x',y'$ such that
\[
xs=ys_1,\quad xa=ya_1,\qquad tx'=t_1y',\quad bx'=b_1y'.
\]
The right multiples were constructed in Section 3; left multiples follow by the reversed construction.
Substitution on $M$ gives
\[
yT_i^{s_1,a_1,b_1,t_1}y'=xT_i^{s,a,b,t}x'.
\tag{17}
\]
The cancellation argument proves equivalence of finite rank for the two fraction choices.
Once the extensions are bounded, injective-left and dense-right multiplication also preserve their finite numerical ranks.

Let $\mathcal R$ be this fraction-independent class.
The generators and constants belong to $\mathcal R$ by (1).
Common denominators make the defect of a sum the sum of the defects.
For products $u_j=s_j^{-1}a_j=b_jt_j^{-1}$, take bounded $x,y,p,q$ with $x,q$ regular such that
\[
xa_1=ys_2,\qquad t_1p=b_2q.
\]
These come from fractions of $a_1s_2^{-1}$ and $t_1^{-1}b_2$; $y,p$ need not be regular.
Then
\[
u_1u_2=(xs_1)^{-1}ya_2=b_1p(t_2q)^{-1},
\]
and its defect on $M$ is
\[
x(s_1D_i b_1-a_1D_i t_1)p
 +y(s_2D_i b_2-a_2D_i t_2)q.
\tag{18}
\]
The middle terms cancel because $t_1pz=b_2qz$ is the same bounded input of $D_i$.
Finally, if $u=s^{-1}a=bt^{-1}$ is a unit of $U$, then $a,b$ are regular and $u^{-1}=a^{-1}s=tb^{-1}$ has defect $aD_i t-sD_i b$, the negative of the original one.
These operations prove that $\mathcal R$ is an inverse-closed unital algebra containing $A$, and hence
\[
F\subseteq\mathcal R.
\tag{19}
\]

## 6. Tensor Descent and the Reverse Inclusion

Suppose $u\in\mathcal R$, with its bounded finite-rank extensions $T_i$.
For (2), $sb=at$.
Right multiplication commutes with every left numerator and denominator, and (15) gives on $M$
\[
\begin{aligned}
\sum_i[R_i,T_i]z
 &=sK(bz)-aK(tz)\\
 &=sC(bz)-aC(tz)+(aPt-sPb)z\\
 &=(aPt-sPb)z.
\end{aligned}
\tag{20}
\]
The $C$ terms cancel as $(sb-at)Cz$, without a vacuum-normalization assumption.
All operators remaining in (20) are bounded on $H$, so density extends the identity to $H$.

Let $Jz=z^*$ be the tracial antiunitary and identify finite-rank operators with algebraic tensors by
\[
\Theta(g\otimes h)z=g\langle Jh,z\rangle,
\qquad g,h\in H.
\]
This is the accepted finite-tensor interface of [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002).
For every bounded $x$,
\[
[\rho(x),\Theta(g\otimes h)]
 =\Theta(gx\otimes h-g\otimes xh).
\]
Write $T_i=\sum_\alpha\Theta(g_{i\alpha}\otimes h_{i\alpha})$.
Equation (20) becomes
\[
a\otimes t-s\otimes b
 =\sum_{i,\alpha}
 (g_{i\alpha}X_i\otimes h_{i\alpha}
       -g_{i\alpha}\otimes X_i h_{i\alpha})
\tag{21}
\]
in $H\otimes_{\mathbb C}H$, and hence in $U\otimes_{\mathbb C}U$.
The latter injection follows because $H\hookrightarrow U$ is a complex-linear injection.
Pass to $U\otimes_F U$.
Every right-hand term vanishes, and the invertible outer actions of $s^{-1}$ and $t^{-1}$ give
\[
u\otimes_F1=1\otimes_Fu.
\tag{22}
\]
If $u\notin F$, then $1,u$ are right-$F$ linearly independent in $U$, since $F$ is a division ring by Section 3.
Extend them to a right-$F$ basis and choose a right-$F$ linear map $\phi:U\to F$ with $\phi(1)=0$ and $\phi(u)=1$.
Applying $\phi\otimes\mathrm{id}$ to (22) gives $1=0$, a contradiction.
Thus $\mathcal R\subseteq F$, proving the full equivalence.

For bounded $f$, use $s=t=1$ and $a=b=f$ to obtain (4).
For its full-domain formulation, $M$ is a graph core for $\widehat D_i$ by definition.
If $T_i$ is the bounded extension of $[D_i,f]|_M$ and $z\in\operatorname{Dom}\widehat D_i$, take graph approximants $z_n\in M$.
Then $fz_n\to fz$ and
\[
D_i(fz_n)=fD_i z_n+T_i z_n
 \longrightarrow f\widehat D_i z+T_i z.
\]
Closedness proves $fz\in\operatorname{Dom}\widehat D_i$ and the required identity there.
Restriction to $M$ gives the converse.
This conclusion is not asserted for an arbitrary larger closed extension whose core need not contain $M$ densely in graph norm.

## 7. Automatic Corollaries and Optional Normalization

**Bounded duals and Haar generators.**
Any bounded dual system for a normal tuple restricts to maps satisfying (1), so Yin_C_F0013 is an immediate special case of the affiliated and bounded criteria above.
For free Haar generators, the bounded operator deleting a terminal positive generator from a reduced group word has $[D_i,U_j]=\delta_{ij}P$.
The sign and complete reduced-word check are in [MSY23-U005, Proposition 6.3](../audits/literature/MSY23/Yin_U005.md#msy23-u005).
Thus the abstract theorem includes Haar unitaries without replacing $\mathbb C\langle U\rangle$ by an adjoint-generated polynomial algebra or treating real and imaginary parts as algebraically free variables.
Yin_C_F0013's additional cofinite-H-domain formulation for bounded duals remains separately valid at its original scope.

**Selfadjoint generators with finite Fisher information.**
Suppose instead that $X$ is selfadjoint and its conjugate variables lie in $L^2(M)$.
Take the closure of the normalized polynomial operators $(\mathrm{id}\otimes\tau)\partial_i$.
[Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002), using Lemma 12 with the explicit one-variable reduction, proves that both their domains and adjoint domains contain $M$.
Its bounded-set continuity extends their generator identities from polynomials to $M$, as explicitly checked in Yin_C_F0022 Section 3.
Restricting to $M$ therefore satisfies (1), and the present theorem yields all of Yin_C_F0022's affiliated and bounded conclusions.
The closure of the restriction is the original canonical closure, because the polynomial core is contained in $M$.
This corollary consumes only the analytic construction of Yin_C_F0022, not its final rationality assertion, so there is no dependency cycle.
Maximal Delta follows anew from Section 3, without invoking a selfadjoint entropy-dimension comparison.
In particular MS23's finite-Fisher conclusion covers all finite-dimensional q-Gaussian tuples for every $-1<q<1$; Yin_C_F0023 independently supplies the stronger boundedness of their normalized duals throughout that interval.

**Normalization does not change the defects.**
For a system satisfying (1), set $\eta_i=D_i\Omega\in H$ and $N_i z=z\eta_i$ on $M$.
For bounded test vectors, traciality gives $N_i^*z=z\eta_i^*$, so $M\subseteq\operatorname{Dom}N_i^*$.
The maps $D_i-N_i$ satisfy (1), vanish at $\Omega$, and have exactly the same cleared defects, since
\[
sN_i(bz)-aN_i(tz)=(sb-at)z\eta_i=0.
\]
No assumption $\eta_i\in M$ is required.
For normalized systems, (15) and the vacuum calculation give $C=(1-d)I$ on $M$, recovering Yin_C_F0022's scalar identity.
For arbitrary systems, leaving $C$ as the module map of Section 4 is sufficient.

## 8. A Genuinely Unbounded Normal Example

Let $M=L^\infty(0,1)$ with its integral trace, and let $S(t)=t$.
Its conjugate variable is
\[
\xi(t)=2\log\frac{t}{1-t}\in L^2(0,1)\setminus L^\infty(0,1).
\tag{23}
\]
Here is a direct verification.
For a polynomial $p$, its divided difference is bounded on the square, and symmetry on $|x-y|>\varepsilon$ gives
\[
\iint_{|x-y|>\varepsilon}\frac{p(x)-p(y)}{x-y}\,dx\,dy
 =2\int_0^1p(x)\left(\int_{|x-y|>\varepsilon}\frac{dy}{x-y}\right)dx.
\]
The inner integral tends to $\log(x/(1-x))$.
For $0<\varepsilon<1/2$, its absolute value is bounded by $|\log x|+|\log(1-x)|$, including the two truncated endpoint intervals.
Dominated convergence on both sides proves the conjugate identity for (23).
Square integrability follows from that of each logarithm, and essential unboundedness follows at either endpoint.

Let $D$ be the canonical closed dual supplied by the finite-Fisher corollary's analytic construction.
It is genuinely unbounded on $H$.
Otherwise the polynomial adjoint identity would imply
\[
\|p\xi\|_2=\|(D+D^*)p\|_2\le2\|D\|\|p\|_2.
\tag{24}
\]
For $p_n(t)=t^n$, $n\ge3$, one has $\|p_n\|_2^2=(2n+1)^{-1}$.
On $[1-1/n,1)$, $p_n\ge(1-1/n)^n\ge1/4$ and $\xi\ge2\log(n-1)$, so
\[
\|p_n\xi\|_2^2\ge\frac{\log^2(n-1)}{4n}.
\]
The ratio to $\|p_n\|_2^2$ tends to infinity, contradicting (24).

Now set $X=iS$ and $E=-iD$.
Then $X$ is normal and nonselfadjoint, $W^*(X)=M$, and $[E,X]=P$ on $M$.
One has $E^*=iD^*$ and $M\subseteq\operatorname{Dom}E\cap\operatorname{Dom}E^*$, while $E\Omega=0$ and $E$ is genuinely unbounded.
Thus the abstract hypotheses admit a normal, nonselfadjoint tuple equipped with a genuinely unbounded normalized dual.
The selfadjoint adjoint formula is used for $S$ in (24); it is not copied without its required coordinate change to $X$.

## 9. Source, Review, and Scope Boundaries

Accepted external inputs are finite-tracial affiliated fractions and polar decomposition, the maximal-Delta/free-field equivalence at the exact MSY23 source units, Hilbert-space adjoints and closed graph, Kaplansky density, scalar Liouville, and the finite-tensor identification.
The source's original Proposition 6.2 assumes bounded duals; Section 3 is the additional domain-safe extension proved here.
The source/audit identities and foundational inspection limits are not changed by this new argument.
The finite-Fisher corollary additionally uses the independently reviewed Dab10-U002 contraction construction.

Normality is used specifically in Section 4, not in maximal Delta or the fraction algebra.
The theorem does not assert the same rationality criterion for arbitrary nonnormal tuples merely from (1).
Neither a dual on a possibly nondense holomorphic polynomial space nor $\Omega\in\operatorname{Dom}D_i^*$ alone substitutes for the full-domain conditions.
The two separate questions $F\cap L^2(M)\subseteq M$ and $F\cap M=\operatorname{Div}_M A$ remain untouched, and the existing Yin_C_F0012/Yin_C_F0014/Yin_C_F0016 obstructions remain valid.
Restricting (3) to affiliated $L^2$ elements retains cleared defects and does not introduce raw unbounded commutators.

The separate [complete artifact review](../audits/reviews/Yin_R_F0013_v1.md) records the actual inspected scope, reviewer contributions and final findings; the selected material decision owns the current assessment.
No numerical test, proof-assistant verification, external human review, publication or historical-priority assessment is asserted.


## Argument: yin_c_f0024-p2


<a id="yin_c_f0024-p2"></a>
## Yin_C_F0024-P2: Bounded Vectors in Both Domains

The authoritative statement remains [Yin_C_F0024, Section 1](#yin_c_f0024).
This version directly uses Yin_C_F0029-P2 with \(E=V_i=M\).
The inclusion \(M\subseteq\operatorname{Dom}D_{i,0}^*\) is precisely the required adjoint-module hypothesis.
The prescribed normal tuple, trace and generator relations agree.
Consequently maximal Delta, the affiliated finite-defect criterion, its bounded extensions and the full closed-domain bounded-element equivalence follow.
For operators initially given on larger domains, restrict to \(M\) first as the original statement specifies; their closures are those of these restrictions.
No conclusion about an arbitrary larger closed extension is substituted.

The analytic construction for finite Fisher information, optional normalization and unbounded example remain separately proved in Yin_C_F0024-P1 Sections 7-8 and the accepted Yin_C_F0022/Dab10 inputs.
This batch changes the proof of the three numbered criterion conclusions, not those source interfaces or their historical reviews.
The complete Yin_C_F0013 and Yin_C_F0022 claims retain their P1 proofs, including the auxiliary conclusions not stated by Yin_C_F0029.


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
| argument | [Exact material](#yin_c_f0024-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#7-automatic-corollaries-and-optional-normalization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0029_v1.md#decision-candidate-0002) | Selected P2 specialization: E=V_i=M. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0013_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision theorem-role-2026-10-10

| Field | Value |
| --- | --- |
| date | 2026-10-09T17:46 |
| status | proved |
| authority | Explicit user instruction on 2026-10-10 to designate C_F0024 as Theorem. |
| reason | The Claim role is set to theorem. The statement, selected P2 proof, dependencies and original Section 7 remain those selected by the preceding decision. R_F0123 records an independent recheck of the statement, P2 proof and Section 7; the earlier reviews retain their original scope. |

Role designation: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0024-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#7-automatic-corollaries-and-optional-normalization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0029_v1.md#decision-candidate-0002) | Selected P2 specialization: E=V_i=M. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0013_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Independent selected-proof recheck](../audits/reviews/Yin_R_F0067_v1.md#conclusion) | Fresh independent inspection of the exact statement, selected P2 through C_F0029, and selected Section 7; accepted source and auxiliary-result limits remain explicit. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0012_v1.md); [Exact material](../audits/reviews/Yin_R_F0013_v1.md).

Material covered by that review: [Exact material](#yin_c_f0024-p2), [Exact material](Yin_C_F0029_v1.md#yin_c_f0029-p2), [Exact material](Yin_C_F0030_v1.md#yin_c_f0030-p2) (together retain the original whole-source scope); [Exact material](Yin_C_F0024_v1.md).
