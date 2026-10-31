---
author: Yin
---

# Failure of original regular-commutator fraction independence on supplied dual domains

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Original Regular Commutator Domain Counterexamples

<a id="statement"></a>

Date: 2026-09-30.
Human record author: Yin.
Proof construction: the coordinating agent and the separately assigned another AI agent and another AI agent agents.
All three contributed to these arguments; their checks are self-review, not independent acceptance.

Assessment: the canonical Claim and Task records govern acceptance and lifecycle.
This artifact gives the complete two-model argument; independent findings are recorded in the separate whole-proof and contract review.
No formal verification, personal human inspection, external review, or novelty assertion is made.

Subsequent related material, 2026-10-01: [C_F0066](Yin_C_F0066_v1.md#existential-original-regular-commutator-counterexample) addresses the existential-only variant left outside these two models.
Its [relationship map](Yin_C_F0066_v1.md#dependencies-and-relationships) preserves the different closedness and quantifier scopes; the statements and review of the present proof remain unchanged.

Target: T_F0001 Task metadata v7, [original contract](../tasks/Yin_T_F0001_v4.md#yin_t_f0001), the literal supplied-domain condition (RC)/(T).
This is a counterexample to fraction independence and to rationality implying the condition for every bounded fraction pair.
It is **not** a counterexample for the closed polynomial restriction.

The two mechanisms are distinct.
Model 1 fails density for a nonclosed supplied restriction, even with the dual relation on its entire domain.
Model 2 uses a closed supplied extension with all bounded vectors in its domain and two dense natural domains; its failure is the absence of a bounded extension on the entire second natural domain.
Both use a rank-one compact polynomial starred commutator and genuinely unbounded rational witnesses.
Neither asserts a refutation when the supplied operator is required to equal the closure of its polynomial restriction.

## Model 1: a literal polynomial domain has zero composition domain

### 1. Precise statement and reuse boundary

There exist a diffuse abelian finite tracial von Neumann algebra `(M,tau)`, one bounded selfadjoint generator `X`, and a densely defined, closable, normalized operator `D` with domain exactly `P=C[X]`, such that:

- `Omega` belongs to the actual Hilbert-adjoint domain of `D`; indeed `Dom D*=H`.
- `[D,X]=P_Omega` on `P`; because `X*=X`, the starred commutator has a rank-one bounded extension.
- The genuinely unbounded rational affiliated element `u=X^{-1}` has one bounded fraction pair whose full natural domain is `P`, with rank-one bounded defect extension.
- The same `u` has another bounded fraction pair whose full natural domain is `{0}`.

Thus the example satisfies both package (D) alone and the compact-starred-commutator comparison baseline.
It also has `D Omega=0`, a dense actual adjoint domain, and closability.
The obstruction is the supplied nonclosed domain, not the absence of those extra properties.

The [prior C_F0026 artifact](Yin_C_F0026_v1.md#yin_c_f0026) was inspected.
Its missing-vacuum obstruction does not compute the required dense natural domains and has a noncompact starred commutator.
The present argument addresses these different quantifiers directly.
The local Voi98-U005 source audit ([source audit](../audits/literature/Voi98/Yin_U005.md#voi98-u005), subsection "Semicircular model and sign correction: 5.13") supplies established semicircular dual-model context.
Voi98-U003 ([source audit](../audits/literature/Voi98/Yin_U003.md#voi98-u003), Proposition 3.8 subsection) records the monic orthonormal recurrence and `P_n=U_n(X/2)` normalization.
These are attribution and convention checks: all concrete model, normalization, dual, denominator and domain assertions used below are explicitly verified here.
No conclusion of C_F0063, C_F0064, C_F0034, or C_F0026 is used as a mathematical premise.
The method index and current S_F0011 were consulted; no existing domain-compatibility theorem covers this example.

### 2. The concrete finite tracial model and dual

Let

\[
I=(-2,2),\qquad d\mu(x)=\frac{1}{2\pi}\sqrt{4-x^2}\,dx,
\]

and let `M=L^infty(I,mu)`, with faithful normal probability trace `tau(f)=int f dmu`, `H=L^2(I,mu)`, `Omega=1`.
The measure is a probability measure because the integral of `sqrt(4-x^2)` on `[-2,2]` is the area of a semicircle of radius 2, namely `2pi`.
The coordinate multiplier `X(x)=x` is bounded and selfadjoint and generates `M` as a von Neumann algebra.
Its starred polynomial algebra is precisely `P=C[x]`, viewed as vectors in `H`.

For `n>=0` let `e_n(x)=U_n(x/2)`, equivalently

\[
e_n(2\cos\theta)=\frac{\sin((n+1)\theta)}{\sin\theta},\qquad 0<\theta<\pi.
\]

Substitution `x=2cos(theta)` gives

\[
\langle e_m,e_n\rangle
=\frac2\pi\int_0^\pi
\sin((m+1)\theta)\sin((n+1)\theta)\,d\theta
=\delta_{mn}.
\]

These are polynomials with degree `n` and leading coefficient one, as follows from

\[
e_0=1,\qquad e_1=x,\qquad xe_n=e_{n+1}+e_{n-1}\quad(n\geq1).
\]

Their linear span is all of `P`.
Polynomials are dense in `H`: continuous functions on the compact interval are dense in this finite-measure L2 space, and uniform polynomial approximation supplies density in the continuous functions.
Thus `(e_n)_{n>=0}` is an orthonormal basis.

Define the unilateral shift `S e_n=e_{n+1}` on this basis.
Then `S` is an isometry, `S*e_0=0`, `S*e_n=e_{n-1}` for `n>=1`, and the recurrence gives the bounded-operator equality

\[
X=S+S^*,\qquad S^*S=I,\qquad SS^*=I-P_\Omega.
\]

Define the **supplied operator** by

\[
D=S^*|_{\mathcal P},\qquad \operatorname{Dom}D=\mathcal P.
\]

It is densely defined and complex-linear, `D Omega=0`, and on the invariant polynomial domain

\[
[D,X]=[S^*,S+S^*]|_{\mathcal P}=P_\Omega|_{\mathcal P}.
\]

Because `X*=X`, the starred commutator is the same rank-one restriction.
It therefore has a compact bounded extension (indeed it belongs to every Schatten ideal).

With the inner product linear in its second variable, `D*=S` with domain all of `H`: for every `h in H` and `p in P`, `<h,Dp>=<Sh,p>`.
Conversely this identity uniquely determines the adjoint on the dense domain.
Hence `Omega in Dom D*` and `D*Omega=e_1`.
The graph closure is the everywhere bounded operator

\[
\overline D=S^*,\qquad\operatorname{Dom}\overline D=H,
\]

because approximating an arbitrary vector by polynomials also approximates its bounded `S*` image.
The supplied `D` itself is not closed: `P` is a proper dense subspace of `H`.

### 3. A regular multiplier whose range misses every nonzero polynomial

Enumerate without repetition the rational points of `I` as `(r_n)_{n>=1}`.
Define the extended nonnegative measurable function

\[
V(x)=\sum_{n=1}^{\infty}2^{-n}|x-r_n|^{-1/2},
\qquad m(x)=\exp(-V(x)),
\]

using `|0|^{-1/2}=+infinity` and `exp(-infinity)=0`.

The density of `mu` is at most `1/pi`.
For each `r in I`,

\[
\int_I |x-r|^{-1/2}\,d\mu(x)
\leq\frac2\pi\bigl(\sqrt{r+2}+\sqrt{2-r}\bigr)
\leq\frac8\pi.
\]

Monotone convergence of the nonnegative series gives `int V dmu<=8/pi`, so `V<infinity` almost everywhere.
Consequently `m` is measurable, `0<m<=1` almost everywhere, and is a bounded regular element of `M`: its measurable affiliated inverse is `1/m`.
Isolated zeros and any other null exceptional set do not affect these operator assertions.

We claim

\[
\boxed{\quad p\in\mathbb C[x],\quad p/m\in L^2(\mu)
\quad\Longrightarrow\quad p=0.\quad}
\tag{1}
\]

Take a nonzero polynomial `p`.
Its finite zero set cannot contain every rational point of `I`, so choose `n` such that `p(r_n)!=0`.
There are `epsilon>0` and constants `c_1,c_2>0` such that the interval `J=(r_n-epsilon,r_n+epsilon)` lies in `I`, `|p(x)|>=c_1` on `J`, and the density of `mu` is at least `c_2` on `J`.
Almost everywhere on `J`,

\[
\frac{|p(x)|^2}{m(x)^2}
\geq c_1^2\exp\bigl(2^{1-n}|x-r_n|^{-1/2}\bigr).
\]

For `h>0`, the power-series bound `exp(z)>=z^4/24` at `z=2^{1-n}h^{-1/2}` shows

\[
\exp\bigl(2^{1-n}h^{-1/2}\bigr)
\geq\frac{2^{4-4n}}{24}h^{-2}.
\]

Integrating on either side of `r_n` proves `int_J |p/m|^2 dmu=infinity`.
This proves (1).

Equivalently, the bounded multiplication operator by `m` has

\[
\operatorname{Ran}(m)\cap\mathcal P=\{0\}.
\tag{2}
\]

There is no conflict with regularity: `m` is injective and has dense range, but two dense linear subspaces need not have nonzero intersection.

### 4. One genuinely unbounded rational element and two exact natural domains

The coordinate `X` is regular because `mu({0})=0`.
In `U(M)` its inverse is multiplication by `1/x`.
In particular

\[
u=X^{-1}\in\operatorname{Div}_{U(M)}\mathbb C[X].
\]

This `u` is genuinely unbounded: every interval around zero has positive measure, so `1/x` is not essentially bounded.

#### Polynomial fraction pair

Use `(s,a,b,t)=(X,1,1,X)`, so `s^{-1}a=bt^{-1}=u`, with both denominators regular.
Its full natural composition domain is

\[
\mathcal E_0
=\{q\in H:q\in\mathcal P,\ Xq\in\mathcal P\}
=\mathcal P.
\]

For every `q in E_0`,

\[
\Delta_0q=XDq-D(Xq)=-P_\Omega q.
\]

Thus the natural domain is dense and the unique bounded extension is the rank-one operator `-P_Omega`.
This verifies the entire finite-rank condition at this pair, including agreement on its **full** natural domain.

#### Nonpolynomial regular fraction pair

Use

\[
(s,a,b,t)=(X,1,m,Xm).
\]

All coefficients belong to `M`; both `X` and `Xm` are regular since they are nonzero almost everywhere.
Pointwise almost everywhere,

\[
s^{-1}a=1/x=m/(xm)=bt^{-1}=u.
\]

The full natural domain is exactly

\[
\begin{aligned}
\mathcal E_1
&=\{q\in H:mq\in\mathcal P,\ Xmq\in\mathcal P\}\\
&=\{q\in H:mq\in\mathcal P\}\\
&=\{0\}.
\end{aligned}
\]

The second equality uses invariance of polynomials under `X`; the third follows from (1): if `mq=p`, then `q=p/m in H`, forcing `p=0`, after which regularity of `m` forces `q=0`.

On this domain the literal defect is the zero map.
Its domain is not dense, so it **fails** the contract's finite-rank condition, regardless of the fact that one could choose many bounded extensions from the zero subspace.
This is a direct counterexample to the "some if and only if every" clause, and to the implication from affiliated rationality to the every-fraction clause.

For an even simpler bounded witness, take `u=1`: the pair `(1,1,1,1)` has domain `P` and zero defect, whereas `(1,1,m,m)` has domain `{0}`.
The unbounded witness above ensures the negative conclusion also occurs at the genuinely affiliated scope.

### 5. Closure comparison and exact unresolved branches

Replacing the supplied operator by its closure changes the conclusion.
For `Dbar=S*` both displayed natural domains are all of `H`, and the same two defects are respectively

\[
X S^*-S^*X=-P_\Omega,
\qquad
X S^*m-S^*Xm=(XS^*-S^*X)m=-P_\Omega m.
\]

The second formula is an equality of bounded operators and uses only `t=Xm`.
Since `m` is nonzero almost everywhere, `P_Omega m` is a nonzero rank-one operator.
Thus the counterexample does **not** persist for the closed polynomial restriction, even though `P` is a graph core for that closure.
It does not decide the criterion under an explicit hypothesis that the supplied operator is closed, equals its closed polynomial restriction, or has a suitable dense-module domain.
It also does not refute the [bounded-dual criterion C_F0013](Yin_C_F0013_v1.md#1-statement-and-exact-scope), which requires an everywhere-defined bounded operator.

Adding the compact-extension condition cannot rescue the literal universal-fraction assertion on arbitrary supplied domains: this example already has rank-one starred commutators.
Neither adding normalization, closability, nor a dense actual adjoint domain rescues it.
A successful replacement hypothesis must exclude this supplied-domain phenomenon or change the requested realization; the latter would be a contract change, not an identification already proved here.

The counterexample establishes failure of one implication and fraction independence, not failure of the separate equivalence between rationality and existence of some finite-rank fraction.
For the exhibited `u`, that existential condition holds.
No counterexample to that separate existential equivalence is asserted.

### 6. Self-check and review handoff

The proof author checked: normalization and faithful trace; selfadjoint generation; the polynomial orthonormal basis; the shift sign; actual adjoint domain and vacuum; closability versus the nonclosed supplied domain; the rank-one starred commutator; measurable finiteness and regularity of `m`; divergent inverse integrability for every nonzero polynomial; both fraction identities; the exact two natural domains and full-domain defect agreements; genuine unboundedness of `u`; and the explicit closure comparison.

The independent reviewer should reconstruct those steps without treating this checklist as evidence.
The only general background inputs are elementary integration, Hilbert-space adjoints and bounded multiplication operators, and density of polynomials for the compactly supported semicircle measure.
No external rationality theorem is used.
Record any source-attribution issue separately from the directly proved mathematical assertions.
Root owns allocation, canonical records, any adopted review, and comparison with T_F0001's completion criteria.

## Model 2: closed supplied extensions

### 1. Statement and precise boundary

There exist a diffuse abelian finite tracial von Neumann algebra, a single bounded selfadjoint generator X, and a densely defined **closed** complex-linear supplied operator D such that:

1. The actual domain of D contains all bounded vectors, hence all starred polynomials.
2. Omega belongs to the actual Hilbert-adjoint domain of D.
3. On starred polynomials, [D,X]=P_Omega, and [D,X*] has the same rank-one compact extension.
4. The genuinely unbounded rational affiliated element u=X^{-1} has two bounded polynomial fraction pairs.
   At both pairs the literal natural domain is dense.
   At one pair the defect is an everywhere bounded rank-one operator.
   At the other pair the defect has no bounded extension agreeing on its entire natural domain.

Thus the equivalence of "some" and "every" fraction pair in the T_F0001 contract fails even when closedness and generator-invariance of the supplied domain are added to the compact polynomial-commutator baseline.
This does **not** refute the additional hypothesis that the starred polynomials are a graph core for the supplied D: that hypothesis fails in this construction.
Nor does the construction satisfy the stronger requirement that the dual relation hold on the entire supplied domain.

### 2. The bounded semicircular dual

Let

\[
d\mu(x)=\frac1{2\pi}\sqrt{4-x^2}\,1_{[-2,2]}(x)\,dx,
\quad M=L^\infty([-2,2],\mu),\quad H=L^2(\mu),
\quad \tau(f)=\int f\,d\mu,
\quad Xf(x)=xf(x),\quad \Omega=1.
\]

The trace is faithful and normal, and the coordinate generates M.
The inner product is linear in its second variable.
The measure is symmetric, diffuse, and has a strictly positive continuous density near zero.
The vector Omega has norm one.

Define polynomials e_0=1, e_1=x, and e_{n+1}=xe_n-e_{n-1}.
Substituting x=2 cos(theta) gives

\[
e_n(2\cos\theta)=\frac{\sin((n+1)\theta)}{\sin\theta},
\qquad d\mu=\frac2\pi\sin^2\theta\,d\theta.
\]

Sine orthogonality makes (e_n) orthonormal.
Its span is the polynomial algebra, dense in H by uniform polynomial approximation on the compact interval and density of continuous functions in L2 of a finite Borel measure.
Define the bounded backward shift B by B e_0=0 and B e_n=e_{n-1} for n>=1.
The recurrence gives, on the basis and hence on all H,

\[
[B,X]=P_\Omega,\qquad B\Omega=0,\qquad B^*\Omega=X\Omega.
\tag{1}
\]

No external dual-system or free-field theorem is needed for this construction.

### 3. The closed multiplier perturbation

Put

\[
h(x)=|x|^{-1/3}\quad(x\ne0),
\qquad V=\{f\in H:hf\in H\},
\qquad Af=Bf+hf\quad(f\in V).
\tag{2}
\]

Assign any finite value to h at the null point zero.
Local comparison with Lebesgue measure near zero shows that h belongs to H, but h^2 does not belong to H: the relevant exponents are -2/3 and -4/3.
Every bounded vector belongs to V because h is in H.
Multiplication by real h on its maximal domain V is densely defined selfadjoint.
For precision, closedness follows by selecting almost-everywhere convergent subsequences from f_n and hf_n when both converge in H.
Its adjoint has the same multiplication domain, as follows by testing the adjoint identity on bounded functions supported where h is bounded.
Bounded perturbation then gives

\[
A\text{ closed},\qquad
\operatorname{Dom}A^*=V,\qquad
A^*=B^*+M_h,\qquad
A^*\Omega=X+h.
\tag{3}
\]

The domain V is invariant under X.
Thus, using (1),

\[
[A,X]f=P_\Omega f\qquad(f\in V).
\tag{4}
\]

Since h^2 is not in H, h is not in V.
On the other hand, Xh and Xh^2 are bounded, so Xh belongs to V.
Consequently

\[
W=V\mathbin{\dotplus}\mathbb C h
\tag{5}
\]

is an algebraically direct sum and XW is contained in V, hence in W.

### 4. A closed supplied extension with the correct actual adjoint vacuum

Let g=X+h and

\[
c=\langle g,h\rangle=\tau(h^2)>0,
\tag{6}
\]

where symmetry makes tau(Xh)=0.
Define the actual supplied operator by

\[
\operatorname{Dom}D=W,
\qquad D(f+\alpha h)=Af+\alpha c\Omega.
\tag{7}
\]

The decomposition proves single-valuedness and complex linearity.
Its graph is

\[
G(D)=G(A)+\mathbb C(h,c\Omega).
\tag{8}
\]

A closed subspace plus a finite-dimensional subspace is closed: the image of the latter in the quotient Hilbert space by the former is finite dimensional and closed, and the sum is its inverse image.
Thus D is closed, with dense domain containing all bounded vectors.

For f in V, (3) gives <Omega,Af>=<g,f>.
Equation (6) gives the same identity for the added vector h.
Therefore

\[
\langle\Omega,Dq\rangle=\langle g,q\rangle\qquad(q\in W).
\tag{9}
\]

By the actual Hilbert-adjoint definition, Omega belongs to Dom D* and D*Omega=g.
No polynomial or all-M adjoint domain is asserted.

On polynomials, D agrees with A and X preserves V.
Since X*=X, (4) proves

\[
[D,X]p=P_\Omega p,\qquad [D,X^*]p=P_\Omega p
\qquad(p\in\mathbb C[X]).
\tag{10}
\]

The starred-polynomial algebra is exactly C[X].
Both commutators in (10) have the rank-one compact extension P_Omega.
These identities also hold on V; they are not assumed to hold on all W.

### 5. The rational unbounded witness and its bad pair

The diffuse coordinate X is regular in U(M), and

\[
u=X^{-1}\in\operatorname{Div}_{U(M)}\mathbb C[X].
\tag{11}
\]

This affiliated multiplication operator is genuinely unbounded because every neighborhood of zero has positive measure.

Take the bounded polynomial fraction pair

\[
(s,a,b,t)=(X,1,1,X),\qquad u=s^{-1}a=bt^{-1}.
\tag{12}
\]

Since XW is contained in W, its entire natural domain is

\[
\mathcal E_{\mathrm{bad}}
=\{q:q\in W,\ Xq\in W\}=W.
\tag{13}
\]

This is Hilbert dense.
The original defect is

\[
\Delta_{\mathrm{bad}}q=XDq-D(Xq),\qquad q\in W.
\tag{14}
\]

On V, (4) gives Delta_bad=-P_Omega.
At the additional domain vector h, because Xh belongs to V,

\[
\begin{aligned}
\Delta_{\mathrm{bad}}h
&=cX-A(Xh)\\
&=cX-B(Xh)-Xh^2\\
&=-P_\Omega h+X(c\Omega-Bh)-Xh^2.
\end{aligned}
\tag{15}
\]

All terms displayed as vectors in (15) belong to H; in particular Xh^2 is bounded.
The last expression is **not** -P_Omega h.
If it were, the equality

\[
x\bigl(c-Bh(x)-h(x)^2\bigr)=0
\]

would hold almost everywhere.
Since x is nonzero almost everywhere, it would imply h^2=c-Bh almost everywhere.
The right side belongs to H, contradicting h^2 not in H.

Any bounded operator agreeing with (14) on the full domain W would agree with -P_Omega on dense V and therefore be -P_Omega on H, contradicting (15).
Thus the bad pair has no bounded extension at all and fails the contract's bounded finite-rank condition.
This failure occurs despite a dense natural domain.

The full formula, for the unique q=f+alpha h with f in V, is

\[
\Delta_{\mathrm{bad}}q=-P_\Omega f+
\alpha\bigl(cX-B(Xh)-Xh^2\bigr).
\tag{16}
\]

Its algebraic range is finite dimensional.
Nevertheless it is not closable: choose polynomials p_n tending to h in H; then h-p_n tends to zero, whereas Delta_bad(h-p_n) tends to the nonzero vector Delta_bad h+P_Omega h.
The contract distinguishes this from a bounded finite-rank extension.

### 6. A good pair with natural domain all H

For the same u and the same supplied D take

\[
(s,a,b,t)=(X,1,X,X^2).
\tag{17}
\]

Both denominators X and X^2 are regular, and X(X^2)^{-1}=X^{-1}.
The functions hX and hX^2 are bounded.
Consequently Xq and X^2q belong to V for every q in H.
The full natural domain of (17) is therefore H.
Direct calculation using only values where D agrees with A gives

\[
\begin{aligned}
\Delta_{\mathrm{good}}q
&=XD(Xq)-D(X^2q)\\
&=XA(Xq)-A(X(Xq))\\
&=-P_\Omega Xq\qquad(q\in H).
\end{aligned}
\tag{18}
\]

The bounded operator -P_Omega X has rank one: q maps to tau(Xq) is nonzero, for example at q=X because tau(X^2)=1.
Both natural domains are dense, but the literal bounded finite-rank condition holds at (17) and fails at (12).
All coefficients are polynomials, and u is unbounded.

### 7. What the construction does and does not refute

The starred polynomial restriction of D has closure exactly A.
The graph norm of A is equivalent to the graph norm of M_h, since B is bounded.
The latter is the L2 norm for the finite Borel measure (1+h^2)dmu on the compact interval.
Uniform polynomial approximation of continuous functions and L2 density of continuous functions therefore make polynomials a core for A.
They cannot be a core for D, which properly extends A by h.

Thus replacing D by the closure of its polynomial restriction changes D to A and changes the task data.
For A, the pair (12) has natural domain V and defect -P_Omega there, so the present obstruction disappears.
No refutation of the compact **closed-polynomial-core** hypothesis package follows.

The example refutes (T) under (D), under (D) plus compact polynomial starred commutators, and under that latter package plus closedness and generator-invariance of the actual supplied D.
It does not refute every possible replacement condition.
A polynomial graph-core requirement, suitable actual adjoint compatibility, or requiring the dual relation on the entire supplied domain excludes this particular mechanism and is a separate question.

The C_F0024 comparison theorem explicitly restricts larger supplied operators to M and concerns those restrictions and their closures.
Applied to the restriction D|M, that convention concerns A: M is a graph core for A, and the adjoint of D|M equals A* and contains M.
These statements about the restriction do not identify the original supplied D on W, and no all-M adjoint-domain assertion is made for D itself.
The C_F0063/C_F0064 intrinsic and weak-form results likewise remain within their recorded realizations.
None of those results identifies (14) on the extra graph vector h.

### 8. Independent review needed

Before acceptance, independently check the shift sign, singular exponents, directness of W, closed graph extension, actual adjoint-vacuum identity, XW subset V, both full natural domains, almost-everywhere cancellation in (15), and the genuinely unbounded rational witness.
Compare the resulting negative scope directly with the T_F0001 contract.
No independent mathematical review, formal verification, or historical-priority claim is made by this author artifact.


## Direct dependencies and research outcome

No earlier project Claim is a mathematical premise of the counterexamples.
The Voi98 source audits attached to the Claim supply checked model attribution and conventions; all model identities used here have local proofs.
The C_F0024/C_F0026/C_F0063/C_F0064 references describe comparison boundaries, not logical dependencies.
The relevant method index and route were consulted before construction; the decisive new mechanism is an explicit mismatch between the supplied graph and the full natural composition domain.

For the original T_F0001 v7 quantifiers, each construction gives one rational affiliated element and two bounded regular fraction pairs for the same supplied dual.
The good pair satisfies the entire stipulated condition and the bad pair does not.
Consequently the universal three-way equivalence is false.
This resolves the contract's negative alternative without claiming that every stronger domain condition is impossible, or that the existential-only equivalence is false.
The intrinsic criterion, original weak-form results and bounded-dual criterion C_F0013 retain their existing scopes.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-30T08:10 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#original-regular-commutator-domain-counterexamples) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Two exact counterexamples to the literal supplied-domain criterion, even with rank-one polynomial starred commutators.
For the same genuinely unbounded rational element, one fraction pair satisfies the dense-domain bounded finite-rank condition and another fails.
One model has a zero natural domain; the other uses a closed supplied dual containing all bounded vectors and polynomial fractions with dense natural domains but no bounded extension at one pair.
The closed polynomial-core and existential-only criteria are not refuted.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:18 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#original-regular-commutator-domain-counterexamples) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0079_v1.md#retained-r107-t_f0001-original-domain-counterexamples-review) | Unknown initial relationship after unspecified construction-result summaries; whole two-model proof including the recorded final scope clarifications, without changing stronger unresolved branches or historical Task completion. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T01:29 |
| status | proved |
| reason | Adopt the fresh isolated whole-proof finding after its initial mathematical judgment and subsequent comparison with the separately preserved original unknown account(s). Preserve the exact statement, proof, mathematical status, all non-review inputs and every historical decision; no Task lifecycle change or mathematical repair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#original-regular-commutator-domain-counterexamples) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Fresh whole-proof finding](../audits/reviews/Yin_R_F0079_v1.md#fresh-c107-whole) | Independently reviewed. Both complete supplied-domain models and exact SOME/EVERY negative quantifier scope, with stronger branches preserved. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-30T08:20 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#original-regular-commutator-domain-counterexamples) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r107) | Whole two-model proof and both exact natural-domain comparisons, closed graph extension and actual adjoint, all hypotheses, source attribution, unchanged-contract negative scope and explicitly undecided stronger branches. |

Recorded mathematical summary: Two exact counterexamples to the literal supplied-domain criterion, even with rank-one polynomial starred commutators.
For the same genuinely unbounded rational element, one fraction pair satisfies the dense-domain bounded finite-rank condition and another fails.
One model has a zero natural domain; the other uses a closed supplied dual containing all bounded vectors and polynomial fractions with dense natural domains but no bounded extension at one pair.
The closed polynomial-core and existential-only criteria are not refuted.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/Voi98/Yin_U005.md); [Exact material](../audits/literature/Voi98/Yin_U003.md).

Whole two-model proof and both exact natural-domain comparisons, closed graph extension and actual adjoint, all hypotheses, source attribution, unchanged-contract negative scope and explicitly undecided stronger branches.

Review: [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r107).

Material covered by that review: [Exact material](../audits/literature/Voi98/Yin_U005.md); [Exact material](../audits/literature/Voi98/Yin_U003.md); [Exact material](Yin_C_F0065_v1.md).
