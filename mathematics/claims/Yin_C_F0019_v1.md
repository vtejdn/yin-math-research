---
author: Yin
---

# An unbounded R-diagonal L2 inverse in a normal bounded-dual model

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## An R-Diagonal L2 Inverse Inside a Normal Bounded-Dual Model

<a id="statement"></a>

<a id="yin_c_f0019"></a>
## Yin_C_F0019: R-Diagonality Does Not Give Unrestricted Affiliated L2 Boundedness

Date: 2026-09-09.
Provenance: project deduction by another AI agent, extending the beta-law input of [Yin_C_F0016](Yin_C_F0016_v1.md#yin_c_f0016).
This is a boundary result for [Yin_S_F0009](../strategies/Yin_S_F0009.md#s_f0009) within the authorized Yin_T_F0001 follow-up.
Initial assessment: complete proof draft pending independent review.
The [selected assessment](#current-assessment) records the mathematical and review assessments.

### 1. Statement and setting

Let
\[
(M_h,\tau_h)=
\left(L^\infty((0,1),w(t)\,dt),\int_0^1(\cdot)w(t)\,dt\right),
\quad
w(t)=140t^3(1-t)^3,
\quad h(t)=t.
\]
Let $(M_u,\tau_u)=(L^\infty(\mathbb T),\text{normalized Haar integral})$ with its coordinate Haar unitary $u$, and form the reduced tracial von Neumann free product
\[
(M,\tau)=(M_u,\tau_u)*(M_h,\tau_h).
\tag{1}
\]
Then the following hold.

1. The bounded normal tuple $X=(u,h)$ generates $M$, and there are bounded operators $E_u,E_h$ on $L^2(M,\tau)$ with
   \[
   [E_u,u]=[E_h,h]=P_\Omega,\qquad
   [E_u,h]=[E_h,u]=0.
   \tag{2}
   \]
   Thus this precise listed tuple meets the normality and bounded-dual hypotheses of [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013).
2. The bounded element $a=uh$ is R-diagonal and generates $M$ as a von Neumann algebra.
3. Its affiliated inverse satisfies
   \[
   a^{-1}=h^{-1}u^*\in
   \operatorname{Div}_{\mathcal U(M)}\mathbb C\langle a\rangle
   \subseteq F_X,
   \qquad
   \|a^{-1}\|_2^2=7,
   \qquad a^{-1}\notin M.
   \tag{3}
   \]
   In particular the unrestricted assertion that every affiliated rational function of a bounded R-diagonal variable which belongs to L2 is bounded is false, even inside a normal bounded-dual generating model.

The use of Yin_C_F0013 is for the normal tuple $(u,h)$, not for the generally nonnormal singleton $(a)$ or its real and imaginary coordinates.

### 2. Normalized factor duals

On $H_u=L^2(M_u)=\ell^2(\mathbb Z)$, put $\delta_n=u^n\Omega_u$ and define
\[
D_u\delta_n=
\begin{cases}
\delta_{n-1},&n\ge1,\\
0,&n\le0.
\end{cases}
\tag{4}
\]
This has norm one and $D_u\Omega_u=0$.
On each basis vector,
\[
(D_uu-uD_u)\delta_n=
\begin{cases}\delta_0,&n=0,\\0,&n\ne0.\end{cases}
\]
Hence $[D_u,u]=P_{\Omega_u}$ on all of $H_u$.

For $h$, [Yin_C_F0016, Part B](Yin_C_F0016_v1.md#yin_c_f0016) supplies the bounded operator on $H_h=L^2(w\,dt)$
\[
(Df)(s)=\operatorname{p.v.}\int_0^1\frac{f(t)w(t)}{t-s}\,dt,
\qquad [D,h]=P_{\Omega_h}.
\tag{5}
\]
The displayed kernel is interpreted through the bounded Hilbert-transform conjugation in that proof.
Its norm is at most $\pi\|w\|_\infty$.

The same reviewed beta calculation gives a bounded function
\[
g(s)=2\left[
w(s)\log\frac{s}{1-s}
-\int_0^1\frac{w(t)-w(s)}{t-s}\,dt
\right],
\qquad
D\Omega_h=-\tfrac12g(h)\Omega_h.
\tag{6}
\]
Indeed, splitting $w(t)=w(s)+(w(t)-w(s))$ in (5) gives exactly (6).
The difference-quotient integral is polynomial, and the endpoint logarithms are multiplied by third-order zeros, so $g$ is bounded.

Subtract the bounded multiplication operator by $D\Omega_h$:
\[
D_h=D+\tfrac12M_{g(h)}.
\tag{7}
\]
Then $D_h\Omega_h=0$.
Multiplication by $g(h)$ commutes with $h$, so $[D_h,h]=P_{\Omega_h}$.
This normalization is essential for the free-product construction below; a general factor dual need not have a bounded vacuum vector which permits it.

### 3. Free-product extension of the normalized duals

We prove the extension explicitly.
More generally, for finitely many tracial factors $(M_i,\tau_i)$ with $x_i\in M_i$, suppose $D_i\in B(H_i)$ satisfies
\[
D_i\Omega_i=0,\qquad [D_i,x_i]=P_{\Omega_i},
\qquad H_i=L^2(M_i).
\tag{8}
\]
No normality is needed for this extension lemma itself.
Write $H_i^0=H_i\ominus\mathbb C\Omega_i$.
The reduced free-product Hilbert space is
\[
H=\mathbb C\Omega\oplus
\bigoplus_{\substack{k\ge1\\i_1\ne i_2,\ldots,i_{k-1}\ne i_k}}
H_{i_1}^0\otimes\cdots\otimes H_{i_k}^0.
\tag{9}
\]
Let $K_i$ be the vacuum plus all reduced words whose last factor is not $i$.
There is a unitary identification
\[
U_i:K_i\otimes H_i\longrightarrow H
\]
which sends $\zeta\otimes\Omega_i$ to $\zeta$ and $\zeta\otimes\xi$ to the concatenation $\zeta\otimes\xi$ for $\xi\in H_i^0$; when $\zeta=\Omega$, the latter is the single-factor vector $\xi$.
Define
\[
E_i=U_i(I_{K_i}\otimes D_i)U_i^*.
\tag{10}
\]
Then $\|E_i\|=\|D_i\|$.
It annihilates the vacuum and words not ending in factor $i$.
On a word $\zeta\otimes\xi$ ending in $i$, decompose
\[
D_i\xi=\xi'+c\Omega_i,\quad \xi'\in H_i^0;
\qquad
E_i(\zeta\otimes\xi)=\zeta\otimes\xi'+c\zeta.
\tag{11}
\]

We check the commutator with the usual left free-product action of $x_j$.
That action changes only the first block: it multiplies a first block in factor $j$, splitting the result into its centered and scalar parts, or prepends its centered vector and adds its scalar multiple if the first block is from another factor.

For words of length at least two, the first-block operation and (11) commute.
Expanding each into its centered and scalar terms verifies this even if one or both operations delete an endpoint block.
When a two-block word has both endpoints deleted, either order gives the same product of the two scalar coefficients times $\Omega$.
If an endpoint of the relevant type is absent, $E_i$ gives zero on both sides; deleting a first block of a word of length at least two does not change its last factor.

For a single centered block $\xi\in H_k^0$, the remaining cases are:

- If $k\ne i$, $E_i\xi=0$, and left multiplication by any $x_j$ never produces a word ending in $i$.
  Thus both commutator terms vanish.
- If $k=i=j$, both operators act in $H_i$, and the commutator is $P_{\Omega_i}\xi=0$ by (8).
- If $k=i\ne j$, write $x_j\Omega_j=x_j^0+\tau_j(x_j)\Omega_j$ and use (11).
  In either order the result is
  \[
  x_j^0\otimes\xi'
  +c x_j^0
  +\tau_j(x_j)\xi'
  +c\tau_j(x_j)\Omega.
  \]

Finally, on the vacuum, $E_ix_j\Omega=0$ for $j\ne i$.
For $j=i$, (8) gives $D_ix_i\Omega_i=\Omega_i$, so $E_ix_i\Omega=\Omega$.
Since $E_i\Omega=0$, these checks establish
\[
[E_i,x_j]=\delta_{ij}P_\Omega.
\tag{12}
\]
Algebraic reduced vectors are dense, and all operators in (12) are bounded, so the identity holds everywhere.

Apply (10) to the normalized factors (4) and (7).
This proves (2).
The trace of (1) is faithful and normal, $u$ and $h$ are normal, and each generates its factor, so $W^*(u,h)=M$.

### 4. The R-diagonal inverse and its domain

Since $u$ is Haar and is free from $h$, $a=uh$ is R-diagonal.
The precise external input is NS06, Corollary 15.9, printed p. 244, in the local 434-page publisher-layout PDF at PDF p. 261.
It states that a Haar unitary times a *-free element is R-diagonal.
The statement and applicability were read in the local source; the general cumulant-product proof behind that corollary is accepted without a new complete audit.

The measure $w(t)\,dt$ gives zero mass to $\{0\}$.
Thus $h$ has support projection one and has a densely defined affiliated inverse $q=h^{-1}$.
In the algebra $\mathcal U(M)$ of affiliated operators,
\[
(uh)(q u^*)=1,\qquad (q u^*)(uh)=1.
\tag{13}
\]
These are products in the affiliated algebra, using $hq=qh=1$.
They do not assert that the unbounded inverse is defined on every Hilbert vector.
By bounded unitary invariance of L2,
\[
\|q u^*\|_2^2=\|q\|_2^2
=140\int_0^1 t(1-t)^3\,dt=7.
\tag{14}
\]
This can also be seen by the bounded spectral cutoffs of $q$, whose L2 limits give (14).
Every interval $(0,\varepsilon)$ has positive $h$-spectral measure, so $q$ is unbounded.
If $qu^*$ were bounded then $q=(qu^*)u$ would be bounded, a contradiction.

As $a\in\mathbb C\langle u,h\rangle$ is invertible in $\mathcal U(M)$, (13) places its inverse in both indicated division closures in (3).
The embedded-free-field identification for $F_X$ follows from the already established normal bounded-dual hypotheses and the MSY23 input of Yin_C_F0013; no identification for a nonnormal tuple is needed for the inclusion itself.

Moreover $|a|=(a^*a)^{1/2}=h$ and $a$ has trivial kernel.
Its polar unitary is $u$.
Both belong to $W^*(a)$ by the polar decomposition in a von Neumann algebra.
Hence $W^*(a)=W^*(u,h)=M$.

### 5. Why this does not contradict holomorphic coefficient boundedness

The automorphisms of the free product given by
\[
\theta_t(u)=e^{it}u,\qquad \theta_t(h)=h
\]
preserve the trace and extend unitarily to L2.
Their extension to affiliated L2 sends
\[
\theta_t(a)=e^{it}a,\qquad
\theta_t(a^{-1})=e^{-it}a^{-1}.
\]
For $n\ge0$, unitary invariance of the L2 inner product gives
\[
\langle a^n,a^{-1}\rangle
=e^{-i(n+1)t}\langle a^n,a^{-1}\rangle
\quad(t\in\mathbb R),
\]
so this inner product is zero.
Thus
\[
a^{-1}\perp
\overline{\operatorname{span}\{1,a,a^2,\ldots\}}^{\,L^2}.
\tag{15}
\]
This uses L2 inner products and the unitary gauge action, avoiding any unjustified trace of products of unbounded operators.
The inverse is nonzero and is not an element of the holomorphic subspace required in [Yin_C_F0017](Yin_C_F0017_v1.md#yin_c_f0017).
A formal rational function with a pole at zero has no Taylor series there; replacing that point by a nonzero pole also does not by itself assure positive-word Taylor evaluation, as the Haar example in Yin_C_F0017 shows.

### 6. Normal-coordinate boundary

Writing $x=(a+a^*)/2$ and $y=(a-a^*)/(2i)$ gives selfadjoint generators of $M$.
It does not transfer (2) to a bounded dual system for $(x,y)$.
Recovering $(u,h)$ from $a$ uses $|a|$ and polar decomposition, not an invertible rational coordinate change of the kind established in [Yin_C_F0006](Yin_C_F0006_v1.md#yin_c_f0006).
No bounded-dual assertion for $(x,y)$ is made here.

For a standard circular element $c=(s_1+i s_2)/\sqrt2$, the real and imaginary parts are scalar multiples of the free semicircular pair, and the standard bounded duals rescale to give the hypothesis.
At the opposite boundary, if $a=u$ is itself Haar, its real and imaginary parts satisfy $x^2+y^2=1$.
A two-coordinate independent dual system would contradict the algebraic freeness forced by bounded duals in the Yin_C_F0013/MSY23 interface.
Thus arbitrary R-diagonal real and imaginary coordinates cannot be admitted without a separate proof.
The singleton $u$ is normal and does have the bounded dual (4).

### 7. Verification boundary

The new argument explicitly checks normalized factor duals, their bounded free-product extension, the complete normal generating tuple, affiliated inverse domains, and L2 unboundedness.
It imports the reviewed beta Hilbert-transform operator from Yin_C_F0016 and the source-statement-checked Haar-product R-diagonal fact from NS06.
Initial independent review was pending when this draft was written.
No Brown-measure formula, spectrum theorem, unbounded commutator product, numerical experiment, or formal verification is used.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:36 |
| status | proved |
| reason | Select the actual retained finding and its explicit relationship at the unchanged mathematical input and original source boundaries; no new whole-proof review or changed mathematical status is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-normalized-factor-duals) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0065_v1.md#r-diagonal-inverse-finding) | Whole normal (u,h) bounded normalized-dual free-product model, actual R-diagonal inverse with squared L2 norm 7 and unboundedness, positive-holomorphic-subspace exclusion and exact accepted NS06 scope. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-normalized-factor-duals) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0065_v1.md#fresh-c19-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

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
| argument | [Exact material](#2-normalized-factor-duals) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0065_v1.md#r-diagonal-inverse-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0065_v1.md#r-diagonal-inverse-finding).

Material covered by that review: [Exact material](Yin_C_F0019_v1.md).
