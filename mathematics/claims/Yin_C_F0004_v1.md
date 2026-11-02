---
author: Yin
---

# One normal generator: rational degree, exact rank and coordinate subalgebras

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Rationality for One Normal Generator

<a id="yin_c_f0004"></a>
## Yin_C_F0004: Single-Generator Criterion and Coordinate Corollary

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Provenance: project deduction; no novelty claim.
Assessment: [selected assessment](#current-assessment).
This establishes the full equivalence in [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001) when d=1, using the reviewed forward implication [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002).

Current independent review: [complete one-generator finding](../audits/reviews/Yin_R_F0061_v1.md#one-normal-generator-finding).

## Statement

Let (M,tau), H=L2(M,tau), Omega=1, P=P_Omega, X, and D satisfy Yin_C_F0001 with d=1.
Thus X is bounded and normal, M=W*(X), D is bounded on H, and [D,X]=P.
Then for every f in M,

\[
\operatorname{rank}[D,f]<\infty
\quad\Longleftrightarrow\quad
f\in\operatorname{Div}_M\mathbb C[X].
\]

More precisely, if r=rank[D,f] is finite, there are polynomials p,q with q nonzero on the spectrum of X such that f=p(X)q(X)^{-1}.
For nonconstant f, every reduced representation satisfies max(deg p,deg q)=r.
The original 2026-09-08 proof established the upper degree bound; the matching rank bound was added and separately reviewed on 2026-09-09 below.
When r=0, f is scalar.
The zero function is represented by p=0, q=1; no degree convention for the zero polynomial is needed.

## Proof

### 1. Spectral representation and absence of atoms

The spectral theorem for one normal generator, with its faithful normal trace, identifies M with L-infinity(S,mu), H with L2(S,mu), X with multiplication by the coordinate z, Omega with the constant function 1, and P with the integral operator whose kernel is 1.
Here mu is a compactly supported Borel probability measure on C, and S=supp(mu) is the spectrum of X.
Every f in M is represented by an essentially bounded measurable function on S.

The measure mu has no atoms.
Indeed, if mu({lambda})>0, let E be multiplication by the indicator of {lambda}.
Since XE=EX=lambda E,

\[
E[D,X]E=0.
\]

But the dual relation makes this equal to EPE.
The latter is nonzero: its range is spanned by E Omega and its value at E Omega is mu({lambda}) E Omega.
This contradiction proves the assertion.
In particular, the diagonal {(z,w): z=w} has zero mu-times-mu measure, and any finite subset of C has zero mu measure.

### 2. The finite-rank commutator determines a divided-difference kernel

Write T=[D,f] and suppose rank T=r is finite.
Since f commutes with X, the two expansions of [D,fX]=[D,Xf] give

\[
TX+fP=Pf+XT,
\qquad [T,X]=[P,f].
\tag{1}
\]

Every finite-rank operator on L2(mu) has a kernel of the form

\[
K(z,w)=\sum_{j=1}^{r} a_j(z)b_j(w),
\qquad a_j,b_j\in L^2(\mu),
\tag{2}
\]

with (Th)(z)=integral K(z,w)h(w)dmu(w).
This uses the complex bilinear kernel convention; the conjugates of the vectors representing the linear functionals are included in b_j.
The kernel belongs to L2(mu times mu).

Under the Hilbert-Schmidt/kernel identification, (1) becomes

\[
(w-z)K(z,w)=f(w)-f(z)
\quad\text{for }\mu\times\mu\text{-almost every }(z,w).
\tag{3}
\]

Indeed, TX has kernel w K(z,w), XT has kernel z K(z,w), Pf has kernel f(w), and fP has kernel f(z).
No integral representation or Hilbert-Schmidt property of D is assumed.
Only T is represented by a kernel.

Because the diagonal is null, (3) determines

\[
K(z,w)=\frac{f(z)-f(w)}{z-w}
\quad\text{almost everywhere off the diagonal}.
\tag{4}
\]

If r=0, (1) gives [P,f]=0.
Applying this to Omega yields f=tau(f)1, proving the scalar assertion.
Assume henceforth r>=1.

### 3. Finite-dimensional columns force rationality

Fix measurable representatives of f,a_j,b_j.
By Fubini's theorem there is a set W of full mu measure such that for each w in W, all the needed values f(w),b_j(w) are finite and the function

\[
q_w(z)=\frac{f(z)-f(w)}{z-w}
\]

(defined arbitrarily at z=w) represents the L2 vector sum_j b_j(w)a_j.
Thus all q_w belong to V=span_C{a_1,...,a_r}, whose dimension is at most r.

Since mu is nonatomic, W contains r+1 distinct points w_1,...,w_{r+1}.
The corresponding vectors are linearly dependent, so choose c_1,...,c_{r+1}, not all zero, such that

\[
\sum_{i=1}^{r+1}c_i\frac{f(z)-f(w_i)}{z-w_i}=0
\quad\text{for }\mu\text{-almost every }z.
\tag{5}
\]

Multiplying by the polynomial product_i(z-w_i), and ignoring only the null finite set of selected points, gives

\[
B(z)f(z)=A(z)\quad\mu\text{-almost everywhere},
\tag{6}
\]

where

\[
\begin{aligned}
B(z)&=\sum_{i=1}^{r+1}c_i\prod_{k\ne i}(z-w_k),\\
A(z)&=\sum_{i=1}^{r+1}c_i f(w_i)\prod_{k\ne i}(z-w_k).
\end{aligned}
\tag{7}
\]

Both polynomials have degree at most r.
The polynomial B is not identically zero: whenever c_i is nonzero,

\[
B(w_i)=c_i\prod_{k\ne i}(w_i-w_k)\ne0.
\]

Because the zero set of B is finite and mu is nonatomic, (6) implies f=A/B almost everywhere.
If A=0, f=0 and the conclusion follows.
Otherwise cancel the common polynomial factors of A and B to obtain relatively prime nonzero polynomials p,q with f=p/q almost everywhere and max(deg p,deg q)<=r.

### 4. Essential boundedness places every inverse inside M

The reduced denominator q has no zero on S.
Suppose instead q(lambda)=0 for some lambda in S.
Relative primeness implies p(lambda) is nonzero.
Consequently |p(z)/q(z)| tends to infinity as z tends to lambda through z not equal to lambda; shrink the neighborhood if necessary to exclude any other zero of q.
Let C be an essential bound for |f|.
There is then epsilon>0 such that

\[
0<|z-\lambda|<\epsilon
\quad\Longrightarrow\quad
|p(z)/q(z)|>C+1.
\]

Since lambda is in the support, mu(B(lambda,epsilon))>0, while mu({lambda})=0.
This contradicts f=p/q almost everywhere and the essential bound.
Thus q is nonzero on S.

Compactness of S gives min_{z in S}|q(z)|>0.
Hence q(X) is invertible in M with bounded inverse, and

\[
f=p(X)q(X)^{-1}\in\operatorname{Div}_M\mathbb C[X].
\]

This proves the reverse implication with exactly the bounded scalar division closure required in Yin_C_F0001.
The forward implication is Yin_C_F0002's polynomial and bounded inverse commutator rule.
Alternatively, it follows directly here by repeatedly applying [D,ab]=[D,a]b+a[D,b] and [D,a^{-1}]=-a^{-1}[D,a]a^{-1}.
QED.

## Exact Rank Refinement and the Kronecker Comparison

Added 2026-09-09 in response to the user's comparison with Miy22 Theorem 2.8.
Let f=p(X)q(X)^{-1} be nonconstant, with p,q relatively prime and q nonzero on S, and put n=max(deg p,deg q).
By the already proved forward implication, r=rank[D,f] is finite.
The preceding construction gives some reduced quotient with numerator and denominator degrees at most r.
Two such quotients that agree mu-almost everywhere agree as rational functions: their polynomial cross-product vanishes on a full-measure set, whereas a nonzero one-variable polynomial has only finitely many zeros and mu has no atoms.
Uniqueness of the reduced quotient therefore gives n<=r.

For the opposite inequality, form the polynomial

\[
\mathcal B(z,w)=\frac{p(z)q(w)-p(w)q(z)}{z-w}.
\]

The numerator vanishes when z=w, so the quotient is a polynomial.
Its degree in each variable is at most n-1.
Expand it as \(\mathcal B(z,w)=\sum_{j=0}^{n-1}z^j b_j(w)\).
The commutator kernel, already uniquely determined by (3) off the null diagonal, becomes

\[
K(z,w)=\sum_{j=0}^{n-1}
\frac{z^j}{q(z)}\frac{b_j(w)}{q(w)}.
\]

Every factor is bounded on the compact spectrum, hence square integrable.
This is a decomposition into at most n separated terms, proving r<=n.
Thus

\[
\boxed{\operatorname{rank}[D,f]=\max\{\deg p,\deg q\}}
\]

for reduced nonconstant f=p/q.
Constants, including zero, have rank zero and are treated separately.
The equality holds for every bounded dual in the original statement.
It does not require a Bezoutian determinant theorem or an explicit kernel for D.

Equivalently, the rank is the total pole multiplicity of this rational function on the Riemann sphere, including infinity.
The finite poles contribute deg q; infinity contributes max(deg p-deg q,0).
For example, f=X has rank one although its scalar rational function has no finite pole.
Miy22's strictly proper Laurent convention excludes an infinity pole; the [Kronecker comparison](../audits/literature/Miy22/Yin_U009.md#miy22-u009) explains that distinction and the precise Haar specialization.
This is a refinement of Yin_C_F0004, not a claim of novelty.

## Corollary: Functions of One Coordinate in a General Tuple

Let X=(X_1,...,X_d) and D satisfy Yin_C_F0001, fix j, and let f belong to the abelian von Neumann algebra N_j=W*(X_j).
Then finite rank of [D_j,f] alone implies

\[
f=p(X_j)q(X_j)^{-1}
\quad\text{with }q(X_j)\text{ invertible in }N_j.
\]

Indeed, let H_j=L2(N_j,tau) be the closed subspace of H generated by N_j Omega, and let Q_j be its orthogonal projection.
This subspace is invariant under left multiplication by every a in N_j and by its adjoint, so Q_j commutes with those multiplication operators.
Since Omega lies in H_j, the bounded compression D'_j=Q_j D_j|_{H_j} satisfies

\[
[D'_j,X_j|_{H_j}]
 =Q_j[D_j,X_j]|_{H_j}=P_{\Omega}|_{H_j},
\]

and

\[
[D'_j,f|_{H_j}]
 =Q_j[D_j,f]|_{H_j}.
\]

The latter has rank at most rank[D_j,f].
The one-generator theorem applied to (N_j,tau|_{N_j}) proves the assertion, including the same upper degree bound.
The inverse in N_j is also an inverse in M, so f belongs to the original R_X.
Conversely, Yin_C_F0002 implies that this rational form has finite-rank commutators with every D_i.
Thus Yin_C_F0001's equivalence holds for every f in the union of the individual W*(X_j), without proving it for their jointly generated algebra.

## Scope and Mechanism

- This proves the entire one-generator case, including selfadjoint, unitary, and normal generators with planar spectral support whenever a bounded dual exists.
- It does not change the algebra to C[X,X*].
  The normal adjoint counterexample Yin_C_F0003 is compatible with the result: its adjoint has infinite-rank commutator.
- It uses no density of C[X] in L2(mu), no explicit kernel for D, no boundedness of arbitrary derivative factors, and no affiliated-to-bounded closure identification.
- Its central mechanism is the scalar commutativity identity [T,X]=[P,f], followed by linear dependence among divided-difference columns.
  For d>1, f need not commute with X_j, so (1) acquires the extra term [D_i,[f,X_j]]; the present proof does not remove that obstruction.
- The initial 2026-09-08 proof gave only an upper degree bound.
  The separately reviewed 2026-09-09 refinement above proves equality with the reduced rational degree, including the pole at infinity.
  No assumption on mutual commutation in a multi-generator tuple is added.


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
| argument | [Exact material](#proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0003_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original review classification and limitations: independently reviewed, including exact-rank refinement

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0003_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:03 |
| status | proved |
| reason | Select the two actual findings of the previously adopted composite review separately, preserving the same statement, argument, mathematical assessment and distinct old scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original one-generator finding](../audits/reviews/Yin_R_F0003_v1.md#decisive-checks) | Original four-step reverse implication, upper degree bound and coordinate compression; actual old relation is unknown and exact-rank equality is excluded. |
| review | [Exact-rank refinement finding](../audits/reviews/Yin_R_F0003_v1.md#independent-review-of-the-exact-rank-refinement-2026-09-09) | Actual contributor review of the added rank equality and compatibility with unchanged original proof; not an independent re-review of that earlier proof. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T13:44 |
| status | proved |
| reason | Adopt the actual new isolated mathematical-first whole review of the exact one-generator theorem, complete proof, exact-rank refinement and coordinate corollary after comparison with both old findings. Preserve original dates and the old unknown versus contributor-self distinction; no arbitrary multivariable converse, source-proof-wide audit or Task/E change is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Complete selected argument](#proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Actual complete finding](../audits/reviews/Yin_R_F0061_v1.md#one-normal-generator-finding) | Complete exact Statement, all four proof steps, both exact-rank inequalities including infinity and constant cases, the coordinate-compression upper bound and every bounded/spectral/source interface; independently reviewed. |

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

Original review classification and limitations: independently reviewed, including exact-rank refinement

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0003_v1.md).

Material covered by that review: [Exact material](Yin_C_F0004_v1.md).
