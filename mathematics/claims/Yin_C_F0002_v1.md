---
author: Yin
---

# Dual commutator derivatives and bounded rational rules

## Current assessment
[Selected decision](#decision-exact-finding-scope)

## Dual-System Commutators as Derivatives

<a id="yin_c_f0002"></a>
## Yin_C_F0002: Tensor Realization, Rational Rules, and the Finite-Rank Interface

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Route: [Yin_S_F0001](../strategies/Yin_S_F0001.md#s_f0001).

Provenance: **mixed**.
The polynomial identity and Hilbert-Schmidt interpretation are recorded in [Voi98](../literature/pdf/Voi98.pdf), Sections 5.11-5.12, through [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005), and explicitly restated in [Shl24-U001](../audits/literature/Shl24/Yin_U001.md#shl24-u001).
The proofs below directly check the more general bounded-generator convention, scalar bounded-inverse extension, finite-family interface, and exact domain limits.
No novelty is asserted.

Current assessment: [selected assessment](#decision-exact-finding-scope).
The [complete derivative finding](../audits/reviews/Yin_R_F0001_v1.md#complete-derivative-finding) records the inspected 2026-09-08 revision and mathematical verification boundaries.
Its reviewer had supplied a separate derivation, so the actual relationship is contributor self-review.

### Setting and Tensor Conventions

Let (M,tau) be a finite von Neumann algebra with a faithful normal tracial state, tau(1)=1.
Write H=L2(M,tau), Omega=1, and P=P_Omega.
Identify M with its left multiplication representation lambda on H.
Use the inner product **linear in the second argument**,

\[
\langle a,b\rangle=\tau(a^*b),\qquad J(a)=a^*.
\]

For bounded X_1,...,X_d in M, suppose D_1,...,D_d in B(H) satisfy

\[
[D_i,X_j]=\delta_{ij}P,\qquad [S,T]=ST-TS.
\tag{DS}
\]

Normality, selfadjointness, free independence, and D_i Omega=0 are **not** assumptions of Yin_C_F0002.
In particular, it applies under Yin_C_F0001's hypotheses without strengthening them.
Write A_X=C<X_1,...,X_d> for the unital algebra with no adjoints automatically adjoined, and R_X=Div_M(A_X) for the scalar bounded division closure specified in Yin_C_F0001.

Use the algebraic tensor product H odot H and its Hilbert completion H tensor_2 H.
Define

\[
\Theta(\xi\otimes\eta)\zeta
   =\xi\langle J\eta,\zeta\rangle,
\qquad \xi,\eta,\zeta\in H.
\tag{T}
\]

For a,b in M this reads

\[
\Theta(a\otimes b)\zeta=a\,\tau(b\zeta),
\qquad \Theta(a\otimes b)=aPb.
\tag{TP}
\]

For general L2 factors, (T) defines a bounded operator of rank at most one; writing aPb as a product of bounded left multiplications would be unjustified.
The right bra is Jb=b*, not b.
The outer M-bimodule action is

\[
a\cdot(\xi\otimes\eta)\cdot b=(a\xi)\otimes(\eta b).
\tag{B}
\]

### Statement

1. **Polynomial formula.** For every formal polynomial p,
   \[
   \boxed{[D_i,p(X)]=\Theta\bigl((\partial_i p)(X)\bigr)
      =\bigl((\partial_i p)(X)\bigr)\#P,}
   \quad (a\otimes b)\#T=aTb,
   \tag{P}
   \]
   where the free difference quotient uses the outer Leibniz rule and partial_i x_j=delta_ij (1 tensor 1).
   It descends to a well-defined map on the evaluated algebra A_X.
   The corresponding vacuum identity is
   \[
   D_i(p(X)\Omega)=p(X)D_i\Omega+
      ((\mathrm{id}\otimes\tau)(\partial_i p)(X))\Omega.
   \tag{V}
   \]
2. **Hilbert-Schmidt realization.** Theta extends to a unitary linear map from H tensor_2 H onto S2(H), the Hilbert-Schmidt operators, and carries H odot H exactly onto the finite-rank operators.
   It intertwines (B) with left and right composition by lambda(M).
3. **A precise derivative on bounded elements.** Set
   \[
   \mathcal B_D=\{f\in M:[D_i,f]\in S_2(H)\text{ for every }i\},
   \qquad \partial_i^D f=\Theta^{-1}[D_i,f].
   \tag{M}
   \]
   This is a unital subalgebra of M closed under inverses that exist in M.
   The maps partial_i^D are outer bimodule derivations on this domain, extend (P), and satisfy
   \[
   \partial_i^D(fg)=f\cdot\partial_i^Dg+(\partial_i^Df)\cdot g,
   \qquad
   \partial_i^D(f^{-1})=-f^{-1}\cdot\partial_i^Df\cdot f^{-1}.
   \tag{L}
   \]
4. **Exact finite-factor criterion.** For f in M, all [D_i,f] have finite rank if and only if f belongs to B_D and each partial_i^D f belongs to H odot H.
   Equivalently, there is one finite family g_1,...,g_N in H and scalar matrices alpha^(i) such that
   \[
   \boxed{\partial_i^Df=\sum_{p,q=1}^N\alpha_{pq}^{(i)}g_p\otimes g_q
       \quad\text{for all }i.}
   \tag{F}
   \]
   One may take N at most 2 sum_i rank[D_i,f].
   For zero commutators the empty family suffices, or one zero-coefficient factor if a nonempty family is desired.
5. **Bounded rational expressions.** R_X is contained in B_D, and
   \[
   \partial_i^D(R_X)\subseteq R_X\odot R_X.
   \tag{R}
   \]
   Differentiating any scalar rational expression with all intermediate inverses in M gives the same evaluated tensor for a fixed f.
   In particular, the rational-to-finite-rank implication in Yin_C_F0001 holds, without using normality.
6. **Minimal-closure boundary.** The polynomial derivation is closable as an operator from K=closure_{L2}(A_X) to (H tensor_2 H)^d.
   On bounded elements in its minimal graph closure, it agrees with partial^D.
   The converse domain inclusion is not asserted; it already fails for the polynomial core C[U] in the Haar-unitary example below.

### Proof: Polynomial Identity and Descent

For a word w=x_{j_1}...x_{j_m}, repeated use of the commutator product rule and (DS) gives

\[
[D_i,w(X)]=\sum_{s:j_s=i}
 X_{j_1}\cdots X_{j_{s-1}}P
 X_{j_{s+1}}\cdots X_{j_m}.
\tag{W}
\]

Empty prefixes and suffixes are 1.
The free difference quotient is exactly the sum of the corresponding prefix tensor suffix terms, proving (P) by (TP) and linearity.
In particular, repeated appearances of a generator contribute separate terms in their original order.

The map Theta on tensors of bounded elements is injective, as shown below.
Consequently p(X)=0 implies (partial_i p)(X)=0.
Thus no separate algebraic-freeness assumption is needed to define the evaluated derivative: different polynomial representatives give the same tensor.
We do not need to invoke or prove a stronger algebraic-freeness theorem here.

Apply (W) to Omega to get (V).
Omitting p(X)D_i Omega requires the additional normalization D_i Omega=0.
A general D_i Omega is only an L2 vector, so subtracting right multiplication by it need not produce a bounded normalized dual.

### Proof: Tensor Identification and Module Actions

The anti-linearity of J and the conjugate-linearity of the first inner-product slot make (T) complex linear in both tensor factors.
On rank-one tensors, with the HS inner product Tr(S* T),

\[
\langle\Theta(\xi\otimes\eta),\Theta(\xi'\otimes\eta')\rangle_{S_2}
 =\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle.
\tag{I}
\]

Indeed Theta(xi tensor eta)=|xi><J eta|, and the trace of the product reduces to <xi,xi'> <J eta',J eta>=<xi,xi'> <eta,eta'>.
Sesquilinear expansion proves the isometry and injectivity; all rank-one operators have this form since J is onto.
Finite-rank operators are dense in S2, so the extension is onto.
A finite-rank decomposition and injectivity show that its preimage is exactly H odot H.

For a,b in M, J(eta b)=b* J eta.
Consequently

\[
\Theta(a\cdot t\cdot b)=a\Theta(t)b
\tag{E}
\]

first for elementary tensors and then, by continuity of bounded module actions, for all completed tensors.
These facts prove statement 2 and the injectivity used in polynomial descent.

### Proof: Maximal Bounded Domain and Rational Rules

For f,g in M,

\[
[D_i,fg]=[D_i,f]g+f[D_i,g],
\quad
[D_i,f^{-1}]=-f^{-1}[D_i,f]f^{-1}
\tag{C}
\]

when f is invertible in M.
The second formula follows by commuting with ff^{-1}=1.
Hilbert-Schmidt operators form a two-sided ideal under bounded multiplication, with ||aTb||_HS at most ||a|| ||T||_HS ||b||.
Thus B_D is a unital inverse-closed subalgebra; (E) transports (C) to (L).

Polynomials belong to B_D by (W).
Induct on finite scalar rational expressions using (L): each tensor remains a finite sum whose factors belong to R_X, because all inverses used exist in M.
This proves (R).
If two expressions give the same f, their differentiated tensors both map to [D_i,f]; injectivity of Theta proves representation independence.
This proof imports neither matrix-to-scalar rational-closure equality nor affiliated-operator inversion.

### Proof: Common Finite Family

Let T_i=[D_i,f] be finite rank and put

\[
V=\sum_{i=1}^d\bigl(\operatorname{Ran}T_i+J\operatorname{Ran}T_i^*\bigr).
\tag{S}
\]

This space has dimension at most 2 sum_i rank T_i.
A finite singular-value decomposition writes T_i as a sum of |u><v| with u in Ran T_i and v in Ran T_i*.
Its inverse tensor under Theta is a sum of u tensor Jv, so it belongs to V odot V.
A basis g_1,...,g_N of V gives (F).
Conversely every tensor in (F) maps to a finite sum of rank-one operators.
This proves statement 4 without asserting boundedness or rationality of the factors.

### Proof: L2 Limits and the Minimal Polynomial Closure

For h,b,c in M, boundedness of D_i and the tracial L2 norm give

\[
\begin{aligned}
\langle b,[D_i,h]c\rangle
 &=\langle D_i^*b,hc\rangle-\langle h^*b,D_ic\rangle,\\
|\langle b,[D_i,h]c\rangle|
 &\leq\|h\|_2\bigl(\|c\|_\infty\|D_i^*b\|_2
                 +\|b\|_\infty\|D_ic\|_2\bigr).
\end{aligned}
\tag{G}
\]

Suppose f_n,f in M, f_n tends to f in L2, and [D_i,f_n] tends to T_i in HS.
Estimate (G) shows convergence of every matrix coefficient against b,c in M; HS convergence also implies operator-norm convergence.
As M Omega is dense in H, T_i=[D_i,f].
Neither a uniform operator-norm bound on f_n nor invariance of M Omega under D_i is required.

Apply this with f_n in A_X and f=0 to prove closability.
Applying it to a bounded f in the minimal graph closure gives

\[
f\in M\cap\operatorname{Dom}(\overline\partial_X)
\ \Longrightarrow\ f\in\mathcal B_D,
\qquad \overline\partial_X f=\partial^D f.
\tag{G2}
\]

Here the initial domain is dense in K by definition.
For normal nonselfadjoint generators, K need not be H.
The term "maximal" in (M) means the largest subset of bounded M on which these commutators are HS, not a claimed equality with a minimal closed extension on H.

### Checked Boundary Example: One Haar Unitary

Take M=L-infinity of the unit circle with normalized Haar trace, H=l2(Z) in the Fourier basis e_n, Ue_n=e_{n+1}, and Omega=e_0.
Define the bounded operator

\[
De_n=\mathbf1_{\{n\geq1\}}e_{n-1},\qquad \|D\|=1.
\]

Then (DU-UD)e_n=(1_{n>=0}-1_{n>=1})e_n=delta_{n0}e_0, so [D,U]=P.
The inverse rule gives

\[
[D,U^{-1}]=-U^{-1}PU^{-1},
\qquad \partial^D(U^{-1})=-U^{-1}\otimes U^{-1}.
\]

The commutator is nonzero rank one.
But K=closure(C[U] Omega) is the closed span of e_n for n>=0, and U^{-1}Omega=e_{-1} is orthogonal to K.
Hence U^{-1} is not in the minimal closure's domain.
This is a counterexample to an unconditional identification of those two derivative domains for the holomorphic polynomial core, not to Yin_C_F0001: U^{-1} belongs to R_U.

### Source Normalization and Verification Boundaries

Voi98 uses selfadjoint generators and selfadjoint Y with [X_j,Y_i]=i delta_ij P.
Set **D_i=iY_i** to obtain (DS); its formula i[Y_i,T]=Psi(partial_i T) then becomes (P).
That source uses the first-variable-linear inner product, whereas (T) states the equivalent identification using the second-variable-linear convention.
Shl24 prints (P) directly for its selfadjoint setting; Yin_C_F0002's broader bounded-generator scope is justified by (W), not attributed to that source.

For the [Unt20 reading](../audits/literature/Unt20/Yin_U001.md#unt20-u001), statement 4 supplies the finite L2-factor condition exactly when its derivative is taken to be partial^D.
It does not identify the manuscript's unspecified derivative domain with this one.
The rational-factor converse, integration/reconstruction, and Yin_C_F0001's full reverse implication remain open.
Any use of partial_i on the extracted L2 factors requires its own domain justification.

The proof uses only the displayed commutator algebra, rank-one/HS Hilbert-space identities, bounded L2 multiplication, and finite-rank decomposition.
No unresolved external theorem, computational experiment, or formal verification is used.
The [proof-audit index](../audits/reviews/index.md) locates the separate review evidence selected below.


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
| argument | [Exact material](#proof-polynomial-identity-and-descent) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0001_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision exact-finding-scope

Select the actual old mathematical finding through its precise current locator and truthful relationship.
The original inspection dates, proof, statement, negative findings and source limits remain unchanged; this is no new mathematical review.

| Field | Value |
| --- | --- |
| date | 2026-10-20T22:16 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof-polynomial-identity-and-descent) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact complete finding](../audits/reviews/Yin_R_F0001_v1.md#complete-derivative-finding) | Actual whole 2026-09-08 contributor self-review of all six statement items, complete proofs, exact source convention and Haar minimal-domain boundary; earlier separate derivation is retained and no new independent review is inferred. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

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

Review: [Exact material](../audits/reviews/Yin_R_F0001_v1.md).

Material covered by that review: [Exact material](Yin_C_F0002_v1.md).
