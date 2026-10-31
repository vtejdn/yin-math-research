---
author: Yin
---

# Affiliated free-field criterion via bounded-denominator finite defects

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Affiliated Free-Field Membership from Finite Bounded Defects

<a id="statement"></a>

<a id="yin_c_f0013"></a>
## Yin_C_F0013: A Finite-Defect Criterion for a Normal Tuple with Bounded Duals

Context: user-authorized follow-up analysis on 2026-09-09 after the completion of [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
This result changes the ambient algebra and criterion; it does not reopen Yin_T_F0001 or change the refuted [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001).
No successor goal is allocated here.

Provenance: project deduction by extending [Yin_C_F0005](Yin_C_F0005_v1.md#yin_c_f0005), with the fraction and defect constructions audited in [Miy22-U006-U007](../audits/literature/Miy22/Yin_U006.md#miy22-u006).
Human author: Yin.
Proof development: mathematical AI agent another AI agent.
Initial assessment: complete proof draft, under review; the [selected assessment](#decision-isolated-review-20261022) records the mathematical and review assessments.
No historical novelty claim is made.

## 1. Statement and Exact Scope

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal tracial state, $H=L^2(M,\tau)$, $\Omega=1$, and $P=P_\Omega$.
Let $X=(X_1,\ldots,X_d)$ be a finite tuple of bounded normal operators such that $M=W^*(X)$.
Assume bounded operators $D_i\in B(H)$ satisfy
\[
[D_i,\lambda(X_j)]=\delta_{ij}P.
\tag{1}
\]
Here $\lambda$ is left multiplication.
Below, bounded elements of $M$ in operator formulas denote their left actions.

Let $U=U(M)$ be the algebra of closed densely defined affiliated operators, with its closed algebraic sums and products, and put
\[
F=\operatorname{Div}_{U}\mathbb C\langle X_1,\ldots,X_d\rangle.
\tag{2}
\]
The generators' adjoints are not silently adjoined in (2).
The accepted MSY23 input specified in Section 2 identifies $F$ with an embedded free skew field.

Every $u\in U$ has bounded fractions
\[
u=s^{-1}a=bt^{-1},
\qquad s,a,b,t\in M,\quad s,t\text{ regular}.
\tag{3}
\]
A bounded regular element is invertible in $U$, equivalently injective with dense range on $H$.
Its inverse need not be bounded.
For (3), define the everywhere bounded defect
\[
\Delta_i(s,a,b,t)=sD_i b-aD_i t.
\tag{4}
\]

Then the following three conditions are equivalent:

1. $u\in F$.
2. For some pair of fractions (3), every $\Delta_i(s,a,b,t)$ has finite rank.
3. For every pair of fractions (3), every $\Delta_i(s,a,b,t)$ has finite rank.

In particular,
\[
F\cap M
=\{f\in M:\operatorname{rank}[D_i,f]<\infty\text{ for every }i\}.
\tag{5}
\]
Restricting the same defect criterion to $u\in L^2(M,\tau)$ characterizes $F\cap L^2(M,\tau)$.
This last assertion uses (4), not an unspecified unbounded commutator $[D_i,u]$.

There is also a domain formulation.
The three conditions are equivalent to the existence of an algebraically finite-codimensional linear subspace $V\subset H$ such that, for every $i$,
\[
D_i(V\cap\operatorname{dom}u)\subseteq\operatorname{dom}u,
\qquad
D_i u\xi=uD_i\xi\quad(\xi\in V\cap\operatorname{dom}u).
\tag{6}
\]
No closedness of $V$ and no reverse domain inclusion are asserted.

## 2. Accepted Inputs and Their Roles

- [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005), Proposition 6.2, published pp. 47-48, says that bounded duals imply $\Delta(X)=d$.
  Its convention is $[X_i,D_j]=\delta_{ij}P$, matched by replacing our $D_j$ with $-D_j$.
  The source statement permits nonselfadjoint tuples.
- [MSY23's accepted free-field interface](../audits/literature/MSY23/readme.md#accepted-inputs), Theorem 1.1(i),(v), published pp. 3-4, identifies (2) with an embedded free skew field.
  In particular, $F$ is a division subring of $U$.
  The reverse proof below needs this division-ring property, not a bounded inverse theorem.
  The source audit owns the exact source coverage and retained external foundations.
- Standard finite-tracial affiliated-operator calculus supplies $U$, its canonical inclusion of $L^2(M,\tau)$, polar decomposition, bounded fractions, and invertibility of regular bounded elements.
  [Miy22-U006](../audits/literature/Miy22/Yin_U006.md#miy22-u006) records these interfaces and their scope.
  For example,
  \[
  s=(1+uu^*)^{-1/2},\quad a=su,\qquad
  t=(1+u^*u)^{-1/2},\quad b=ut
  \tag{7}
  \]
  are bounded valid representatives, with regular $s,t$.
  Functional calculus and polar decomposition make $a,b$ contractions.
- [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002) identifies algebraic tensors in $H\otimes_{\mathbb C}H$ with finite-rank operators.
  [Yin_C_F0005](Yin_C_F0005_v1.md#yin_c_f0005) proves the normal commutant identity and algebraic equalizer mechanism used below.
  Their necessary steps are reconstructed here.

The closure computations adapt Miy22's bounded identities without using its Fock relations, bounded rationality theorem, or adjoint-closure argument.
This proof therefore does not assume an analogue of Miy22's bounded analytic conclusion.

## 3. Common Denominators and Independence of Fractions

All tensor products used later are algebraic.
This section concerns bounded operators only.

First, any two regular left denominators $s_1,s_2$ have a regular common left multiple.
Write the affiliated unit $s_1s_2^{-1}$ as $x^{-1}y$ with bounded $x,y$ and regular $x$.
Since $s_1s_2^{-1}$ is invertible in $U$, so is $y=x(s_1s_2^{-1})$; consequently $y$ is also regular.
Then
\[
s=xs_1=ys_2
\tag{8}
\]
is regular.
Similarly, if
\[
t_1^{-1}t_2=pq^{-1},
\]
both $p,q$ are regular, and
\[
t=t_1p=t_2q
\tag{9}
\]
is a regular common right multiple.
The corresponding numerators are multiplied on the same indicated sides and stay bounded.

Suppose (3) has finite defects and
\[
u=s_1^{-1}a_1=b_1t_1^{-1}
\]
is another bounded pair.
Choose common multiples as above, now denoted
\[
xs=ys_1,\qquad tx'=t_1y',
\]
with all $x,y,x',y'$ bounded and regular.
Multiplying the fraction identities in $U$ gives bounded identities
\[
xa=ya_1,\qquad bx'=b_1y'.
\]
Therefore
\[
y\Delta_i(s_1,a_1,b_1,t_1)y'
=x\Delta_i(s,a,b,t)x'.
\tag{10}
\]
The right side is finite rank.
The injective left multiplier $y$ can first be canceled: an injective map preserves the dimension of the range on which it acts.
The dense-range right multiplier $y'$ can then be canceled: the bounded image of $H$ lies in the closure of the image of $y'H$, and the latter image is already finite dimensional and closed.
Thus the left-hand defect itself is finite rank.

This proves the equivalence of “some” and “every” fractions.
It asserts invariance of finite-rank membership; no equality of numerical ranks is needed.
No commutator with $x,y,x',y'$ is formed.

## 4. The Finite-Defect Class Contains the Affiliated Division Closure

Let $\mathcal R$ denote the elements satisfying the equivalent finite-defect conditions.
Each $X_j$ belongs to $\mathcal R$ by its fractions with $s=t=1$ and (1), and constants also belong.
We show that $\mathcal R$ is a unital subalgebra closed under inverses of its elements invertible in $U$.

### Sums and scalar multiples

For $u_1,u_2\in\mathcal R$, take common regular left and right denominators:
\[
u_j=s^{-1}a_j=b_jt^{-1}.
\]
The sum has numerators $a_1+a_2,b_1+b_2$, and its defect is the sum of the two defects.
Scalar multiples work in the same way.

### Products

Start with possibly different fractions
\[
u_j=s_j^{-1}a_j=b_jt_j^{-1}.
\]
Choose bounded fractions
\[
a_1s_2^{-1}=x^{-1}y,\qquad
t_1^{-1}b_2=pq^{-1},
\tag{11}
\]
where $x,q$ are regular.
The numerators $y,p$ need not be regular: neither ratio in (11) is assumed invertible.
The relations
\[
xa_1=ys_2,\qquad t_1p=b_2q
\]
give
\[
u_1u_2=(xs_1)^{-1}ya_2=b_1p(t_2q)^{-1}.
\tag{12}
\]
Both denominators in (12) are regular products.
Direct expansion gives
\[
\begin{aligned}
xs_1D_i b_1p-ya_2D_i t_2q
={}&x(s_1D_i b_1-a_1D_i t_1)p\\
&+y(s_2D_i b_2-a_2D_i t_2)q.
\end{aligned}
\tag{13}
\]
The middle terms cancel using the two bounded relations following (11).
The right side is finite rank.

### Inverses

If $u=s^{-1}a=bt^{-1}\in\mathcal R$ is invertible in $U$, then $a=su$ and $b=ut$ are units of $U$ and are bounded, so they are regular.
Its inverse has fractions
\[
u^{-1}=a^{-1}s=tb^{-1},
\]
whose defect is
\[
aD_i t-sD_i b=-\Delta_i(s,a,b,t).
\tag{14}
\]
Thus $u^{-1}\in\mathcal R$.
This step assumes invertibility in $U$, not merely that an arbitrary element of $U$ is nonzero.

Consequently $\mathcal R$ is an inverse-closed subalgebra of $U$ containing the given generators, and
\[
F\subseteq\mathcal R.
\tag{15}
\]
Adjoint closure of $\mathcal R$ is not used or claimed for a general normal tuple.

## 5. Normality Gives the Fundamental Bounded Identity

Write $\rho(x)$ for right multiplication by $x\in M$ on $H$.
It is a bounded linear antihomomorphism commuting with $\lambda(M)$.
Traciality gives
\[
\rho(x)\Omega=\lambda(x)\Omega,\qquad
P\rho(x)=P\lambda(x),
\]
hence $[\rho(x),P]=[\lambda(x),P]$.
Define
\[
K=\sum_i[\rho(X_i),D_i].
\tag{16}
\]
Since all operators are bounded, Jacobi's identity and (1) yield
\[
[K,\lambda(X_j)]
=[\rho(X_j),P]
=[\lambda(X_j),P].
\]
Therefore $C:=K+P$ commutes with every $\lambda(X_j)$.
Each $\lambda(X_j)$ is normal.
Exact Fuglede commutation then makes $C$ commute with each adjoint and consequently with $\lambda(M)$.

For completeness, the exact normal-commutation fact used here has the elementary proof recorded in Yin_C_F0005.
If $TN=NT$ and $N$ is bounded normal, the entire function
\[
z\longmapsto e^{zN^*}Te^{-zN^*}
=e^{zN^*-\bar zN}Te^{-zN^*+\bar zN}
\]
is uniformly bounded in norm by $\|T\|$.
The second expression uses only $TN=NT$ and normality; its two exponentials are unitary.
Scalar Liouville followed by differentiation at zero gives $[N^*,T]=0$.
This is exact commutation, not a statement modulo finite rank.

Now fix any bounded fraction pair (3).
The equality $sb=at$ holds in $M$.
Since the right multipliers commute with $s,a,b,t$,
\[
\begin{aligned}
\sum_i[\rho(X_i),\Delta_i(s,a,b,t)]
&=sKb-aKt\\
&=s(C-P)b-a(C-P)t\\
&=aPt-sPb.
\end{aligned}
\tag{17}
\]
The $C$-terms vanish because $C$ commutes with $M$ and $sb=at$.
Equation (17) involves only bounded operators.
It is the replacement for an attempted identity with an unbounded $[D_i,u]$.

## 6. Finite Tensors and Descent to the Free Field

Use the inner product linear in its second variable, and let $J$ be the tracial antiunitary.
The bijection from Yin_C_F0002 is
\[
\Theta(g\otimes h)\xi=g\langle Jh,\xi\rangle,
\qquad
\Theta:H\otimes_{\mathbb C}H\longrightarrow\operatorname{FinRank}(H).
\tag{18}
\]
For bounded $g,h$, it agrees with $gPh$.
For arbitrary $g,h\in H$ and bounded $x$,
\[
[\rho(x),\Theta(g\otimes h)]
=\Theta(gx\otimes h-g\otimes xh).
\tag{19}
\]
Indeed, $\rho(x)g=gx$ and $\rho(x)^*Jh=J(xh)$.
Both products in (19) remain in $H$.

For $u\in\mathcal R$, let
\[
\Delta_i=\sum_\alpha\Theta(g_{i\alpha}\otimes h_{i\alpha}),
\qquad g_{i\alpha},h_{i\alpha}\in H.
\]
Injectivity of $\Theta$ converts (17) into
\[
a\otimes t-s\otimes b
=\sum_{i,\alpha}
\left(g_{i\alpha}X_i\otimes h_{i\alpha}
-g_{i\alpha}\otimes X_i h_{i\alpha}\right).
\tag{20}
\]
This is an equality in the algebraic tensor product $H\otimes_{\mathbb C}H$.
The canonical injection $H\hookrightarrow U$ induces an injection on these tensor products because the base ring is the field $\mathbb C$; thus (20) is also an identity in $U\otimes_{\mathbb C}U$.

Apply the quotient map to $U\otimes_F U$, with the first $U$ a right $F$-module and the second a left $F$-module.
Each right-hand summand in (20) vanishes because $X_i\in F$.
Hence
\[
a\otimes_F t=s\otimes_F b.
\tag{21}
\]
Outer multiplication by $s^{-1}$ on the first factor and $t^{-1}$ on the second is a well-defined invertible map on this balanced tensor product: left multiplication on the first factor is right $F$-linear, and right multiplication on the second is left $F$-linear.
It converts (21) to
\[
u\otimes_F1=1\otimes_Fu.
\tag{22}
\]

Here is the algebraic equalizer argument.
If $u\notin F$, then $1,u$ are right $F$-linearly independent in $U$: a relation $a+ub=0$ with $b\ne0$ implies $u=-ab^{-1}\in F$, while $b=0$ forces $a=0$.
Extend $1,u$ to a right $F$-basis of $U$ and choose a right $F$-linear map $\phi:U\to F$ with $\phi(1)=0$, $\phi(u)=1$.
Applying $\phi\otimes\mathrm{id}$ to (22) and identifying $F\otimes_F U$ with $U$ gives $1=0$, a contradiction.
Thus $u\in F$.

The module argument permits zero divisors in $U$; it requires that $F$ be a division ring.
No continuity of $\phi$, completed tensor product, or boundedness of an affiliated inverse is asserted.

Combining this reverse inclusion with (15) proves the three equivalent conditions in Section 1.

## 7. Bounded and Square-Integrable Parts

For bounded $f\in M$, choose $s=t=1$, $a=b=f$.
Its defect is exactly $[D_i,f]$.
Fraction independence and the proved equivalence therefore give (5).

This adds the previously unproved reverse inclusion $F\cap M\subseteq\{f:[D_i,f]\text{ finite rank}\}$ to Yin_C_F0005.
It does not give
\[
F\cap M=\operatorname{Div}_M\mathbb C\langle X\rangle.
\]
That latter equality fails for the [Yin_C_F0012 sandwich tuple](Yin_C_F0012_v1.md#yin_c_f0012).
The counterexample is fully consistent with (5).

Since $L^2(M,\tau)\subset U$, restricting the equivalence to $u\in L^2(M,\tau)$ gives precisely the stated $F\cap L^2$ corollary.
Square integrability does not make left multiplication by $u$ bounded on $H$, nor does it ensure that $D_i$ preserves $\operatorname{dom}u$.
Accordingly the corollary retains the bounded defect (4).
No ordinary commutator, weak commutator, or choice of a core is substituted without a separate definition and argument.

## 8. An Algebraically Cofinite Domain Formulation

Two domain facts will be used.
If $u=s^{-1}a$ with $s$ regular and $a,s$ bounded, the literal composition $s^{-1}\circ a$ is closed: from $\xi_n\to\xi$ and $s^{-1}a\xi_n\to\eta$, boundedness of $a$ and closedness of $s^{-1}$ give $a\xi\in\operatorname{dom}s^{-1}$ and $s^{-1}a\xi=\eta$.
The affiliated product is its closure, hence it is already this composition.
Thus
\[
\operatorname{dom}u=\{\xi:a\xi\in\operatorname{ran}s\},
\qquad su\xi=a\xi\quad(\xi\in\operatorname{dom}u).
\tag{23}
\]
For any bounded right fraction $u=bt^{-1}$, the affiliated product extends the literal composition on $\operatorname{ran}t$, giving
\[
tH\subseteq\operatorname{dom}u,\qquad ut=b\text{ on }H.
\tag{24}
\]
For the particular $t=(1+u^*u)^{-1/2}$, spectral calculus gives the stronger identity $tH=\operatorname{dom}u$.
This is the usual bounded transform: $t$ is a bijection from $H$ onto $\operatorname{dom}|u|=\operatorname{dom}u$, with the inverse on that range given by $(1+u^*u)^{1/2}$.

Suppose first that $u\in\mathcal R$, and use that particular $t$ together with (7).
Let
\[
W=\bigcap_i\ker\Delta_i.
\]
It has finite algebraic codimension in $H$.
Choose an algebraic complement $L$ of $\operatorname{dom}u=tH$ in $H$, and set
\[
V=tW\oplus L.
\tag{25}
\]
Then $V\cap\operatorname{dom}u=tW$ and
\[
\dim(H/V)=\dim(tH/tW)=\dim(H/W)<\infty,
\]
using injectivity of $t$.

For $\xi=t\eta$ with $\eta\in W$, equation $\Delta_i\eta=0$ gives
\[
aD_i\xi=sD_i b\eta=sD_i u\xi\in\operatorname{ran}s.
\]
Equation (23) implies $D_i\xi\in\operatorname{dom}u$, and injectivity of $s$ then gives $uD_i\xi=D_i u\xi$.
This proves (6).

Conversely, suppose an algebraically cofinite $V$ satisfies (6), and choose any bounded pair (3).
The set
\[
W=\{\eta\in H:t\eta\in V\}
\]
is cofinite, since $H/W$ injects into $H/V$ by the induced linear map of $t$.
For $\eta\in W$, (24) puts $\xi=t\eta$ in $V\cap\operatorname{dom}u$.
The assumed invariance and commutation give
\[
\Delta_i\eta
=sD_i u\xi-aD_i\xi
=s(D_i u\xi-uD_i\xi)=0,
\]
where (23) is applicable to $D_i\xi$.
Each bounded defect therefore factors through the finite-dimensional quotient $H/W$ and has finite rank.

This proves exactly (6).
It does not prove the stronger equality
\[
V\cap\operatorname{dom}u
=V\cap\bigcap_i\operatorname{dom}(uD_i).
\]
The reverse inclusion in [Miy22-U008](../audits/literature/Miy22/Yin_U008.md#miy22-u008) uses its creation/annihilation identities and is not imported here.
The complements in (25) are algebraic, with no Hilbert-closedness or graph-norm-density claim.

## 9. Checks, Review, and Limits

The proof reconstructs denominator cancellation, all algebraic closure operations, the normality step, finite-tensor descent, and the stated cofinite-domain formulation.
Zero and scalar elements require no inversion; inverses are used only for units in $U$.
The finite number of duals makes the common kernel in (25) cofinite.

The main new step is the bounded fraction identity (17), which avoids assuming derivatives of the arbitrary bounded denominators are finite rank.
The converse does not depend on the closure argument, so there is no regularization cycle.
Normality is used to put $K+P$ in $\lambda(M)'$; no selfadjoint replacement of the polynomial generators or density of holomorphic polynomials is assumed.

Source inputs are the already audited interfaces linked above; no new source acquisition, complete external-foundation proof, numerical test, formal verification, external human review, or literature-priority assessment was performed for this deduction.

On 2026-09-09, another AI agent independently reviewed all nine sections and recorded a [complete proof audit](../audits/reviews/Yin_R_F0063_v1.md#affiliated-criterion-finding).
The review reconstructed both containments, fraction independence, the balanced tensor operations, and the precise cofinite-domain equivalence.
No corrective mathematical edit was required; the reviewer recommends `proved` and `independently reviewed`.
This paragraph only integrates that subsequent review evidence; it changes no mathematical statement or argument.
The [selected assessment](#decision-isolated-review-20261022) records the mathematical and review assessments.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:32 |
| status | proved |
| reason | Select the exact retained finding with its actual relationship and original mathematical scope. The statement, argument, status, original review date and historical decisions remain unchanged; no new whole-proof review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0013) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0063_v1.md#affiliated-criterion-finding) | Entire three-way affiliated finite-defect equivalence, bounded/L2 restrictions and cofinite forward-domain formulation, preserving exact fraction/domain conventions, generator algebra and MSY23 accepted-source depth. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:53 |
| status | proved |
| reason | Adopt the actual context-isolated whole-argument review after complete comparison with the old finding, retaining fixed mathematics, exact assumptions and historical adoption facts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0013) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0063_v1.md#affiliated-defects) | Complete three-way affiliated finite-defect criterion, bounded/L2 restrictions and algebraically cofinite forward-domain equivalence, with exact fractions, native domains and accepted-source boundaries. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

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
| argument | [Exact material](#yin_c_f0013) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0063_v1.md#affiliated-criterion-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



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

Review: [Exact material](../audits/reviews/Yin_R_F0063_v1.md#affiliated-criterion-finding).

Material covered by that review: [Exact material](Yin_C_F0013_v1.md).
