---
author: Yin
---

# Annulus-local angular comparison gives original local dual domains and a dense-module affiliated criterion

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Annulus-local angular comparison gives original local dual domains

<a id="statement"></a>

Kind: Claim/proof module.
Date: 2026-09-16.
Human record author: Yin.
Argument developed by a research subagent and checked by the coordinator.
Consumer: the separate normal-domain investigation, Q3.

The registered statement consists of assertions A and B below.
Assertion C is expressly unresolved.
Canonical research metadata owns the current mathematical and review assessments.
This continuation changes no Task contract or manuscript designation.

<a id="annulus-local-dual-domains"></a>
## 1. Exact scope and separation of conclusions

Use the exact hypotheses of [C_F0025](Yin_C_F0025_v1.md#yin_c_f0025).
Thus `(M,tau)` is finite tracial, `H=L2(M,tau)`, `Omega=1`, and `X=(X_1,...,X_d)` is a bounded normal generating tuple.
The original operators `D_{j,0}` have domain precisely

\[
\mathcal P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
\]

the vacuum belongs to each actual Hilbert-adjoint domain, `[D_{j,0},X_k]=delta_{jk}P_Omega`, and the starred-generator commutators have compact bounded extensions.
Write `D_j=closure(D_{j,0})`.
Inner products are linear in the second variable.

Assume in addition that the coordinate algebras `B_j=W*(X_j)` are freely independent.
Their spectral probabilities have the form

\[
d\mu_j=b_j\,d\nu_j,\qquad
d\nu_j(re^{i\theta})=d\sigma_j(r)\,\frac{d\theta}{2\pi},
\quad \sigma_j((0,R_j])=1,
\tag{1}
\]

where the measurable densities satisfy

\[
\int_0^{2\pi}b_j(re^{i\theta})\,\frac{d\theta}{2\pi}=1
\quad(\sigma_j\text{-almost every }r).
\tag{2}
\]

Require only annulus-local comparison: for each `0<a<c<infinity` there are constants depending on that annulus such that

\[
0<m_{j,a,c}\le b_j\le B_{j,a,c}<\infty
\quad\nu_j\text{-almost everywhere on }\{a<|z|<c\}.
\tag{3}
\]

No global bound or uniformity as `a` tends to zero is required.
The absence of a planar atom at zero is already forced by C_F0025; it is written in (1) to specify the radial representation.
Zero may belong to the topological support of `sigma_j`; no positive lower bound on the radius is assumed.
Positive-radius atoms of `sigma_j` are allowed.

**A. Original local domains.**
Put

\[
e_{j,n}=1_{\{|X_j|\ge1/n\}},\qquad n\ge1.
\tag{4}
\]

Then for every `j,n`,

\[
Me_{j,n}\subseteq\operatorname{Dom}D_j
 \cap\operatorname{Dom}D_{j,0}^*,
\qquad
\|D_jf\|_2+\|D_{j,0}^*f\|_2\le C_{j,n}\|f\|_\infty
\quad(f\in Me_{j,n}),
\tag{5}
\]

for a finite constant `C_{j,n}`.
These are the original closure and actual original Hilbert adjoint.

**B. A full affiliated criterion on a common dense module.**
Define

\[
p_n=\bigwedge_{j=1}^d e_{j,n},\qquad
\mathcal E=\bigcup_{n\ge1}Mp_n,
\qquad\mathcal D_j=D_j|_{\mathcal E}.
\tag{6}
\]

Then `E` is a dense complex-linear left `M`-module.
With

\[
A_X=\mathbb C\langle X_1,\ldots,X_d\rangle,
\quad F=\operatorname{Div}_{U(M)}A_X,
\]

the complete conclusion of [C_F0029](Yin_C_F0029_v1.md#yin_c_f0029) holds for `mathcal D_j` on `E`: if

\[
u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
\quad s,t\text{ regular},
\]

then `u in F` if and only if each map

\[
z\longmapsto sD_j(bz)-aD_j(tz),\qquad z\in\mathcal E,
\tag{7}
\]

has finite-dimensional range.
It is enough to use one fraction pair, and then every pair works.
Every finite-rank defect has a unique bounded finite-rank extension; its rank is fraction-independent.
For `f in M`, this specializes to bounded finite-rank commutators on `E` and full-domain invariance for the closures `closure(mathcal D_j)`.

**C. Original polynomial weak forms remain a separate obligation.**
No assertion here identifies `closure(mathcal D_j)` with `D_j`.
Consequently B does not, by itself, prove that every `f in F cap M` has bounded finite-rank weak commutator forms on the original `P x P`.
The exact partial compatibility and the remaining gap are stated in Section 7.

## 2. Reuse and input boundary

The needed inputs have already been checked in the repository:

1. [C_F0025, Section 2](Yin_C_F0025_v1.md): normalization, the canonical marginal divided difference, closability, the original core adjoint identity, and bounded-generator invariance of the original closed domains.
2. [C_F0045, Sections 3--5](Yin_C_F0045_v1.md): the full-core orthogonal right-module decomposition and actual direct-sum closure/adjoint formulas.
   Their proofs do not use the global marginal infinity-to-2 estimate.
3. [C_F0049, Sections 2--3](Yin_C_F0049_v1.md): finite-measure annular normalization and smooth-cutoff recovery in the original global graph.
   Only the comparison bounds on the selected annulus occur in these sections.
   The global comparison constant enters its later necessity argument, which is not invoked here.
4. [C_F0048, measurable sufficient direction](Yin_C_F0048_v1.md), together with [C_F0047](Yin_C_F0047_v1.md), supplies the bounded annular operator.
   Its radial midpoint condition is automatic on a fixed annulus bounded away from zero.
5. The exact complex little Grothendieck inequality used in C_F0045, with squared constant `k_C=4/pi`, is already source-checked at [Pis12-U001](../audits/literature/Pis12/Yin_U001_v1.md#pis12-u001).
   It applies to a bounded map from a commutative continuous-function algebra to a Hilbert space; it requires neither normality nor complete boundedness of that map.
6. Real C1 polynomial approximation, already source-checked as [VV16-U001](../audits/literature/VV16/Yin_U001_v1.md#vv16-u001), is used only to put smooth cutoffs times polynomials in the actual original graphs.
7. C_F0029 is used at its stated dense-left-module scope, including its explicit distinction between closures of restrictions and larger closed extensions.

The relevant complete reviews of [C_F0045](../audits/reviews/Yin_R_F0023_v1.md) and [C_F0049](../audits/reviews/Yin_R_F0024_v1.md) were also read.
The method index was searched; its shared-structure heuristic supplies no additional analytic input here.
No new external theorem or unverified citation is used.
The substantive new assembly is the local-map lifting and simultaneous restoration of the two original graphs below.

## 3. Marginal cutoff maps in the actual graphs

Fix `j` and omit its subscript temporarily.
Normalize on the original full core:

\[
\eta=D_{j,0}1,\qquad E_0p=D_{j,0}p-p\eta.
\]

Let `e_0` be its restriction to `P_j=C[X_j,X_j*]`, let `e=closure(e_0)`, and let `xi=e_0*1`.
C_F0045's exact decomposition shows that `xi in H_j=L2(mu)` and that the actual marginal adjoint satisfies, on `P_j`,

\[
e_0^*b=b\xi-Je_0Jb,\qquad Jb=\overline b.
\tag{8}
\]

Choose a real smooth radial function `h` compactly supported in an annulus `V={a<|z|<c}`; let `K=supp h` and `dist(K,V^c)>0`.
Zero-measure annuli give only the zero cutoff map and may be discarded.

By (2), `mu(V)=nu(V)=t`.
Normalize both restricted measures by `t`.
On that annulus (3) gives the global comparison required by C_F0048, and the normalized radial midpoint quantity is at most `1/a`.
Its measurable sufficient direction therefore yields the actual canonical annular operator `F_{mu,V}`, with unnormalized integration measure, and a finite bound

\[
\|F_{\mu,V}g\|_{L^2(\mu|_V)}\le c_V\|g\|_\infty
\quad(g\in L^\infty(\mu|_V)).
\tag{9}
\]

For a starred polynomial `b`, real C1 polynomial approximation puts `hb` in the original marginal closure and identifies its value as the canonical divided-difference integral.
The exact split is

\[
e(hb)(z)=
\begin{cases}
F_{\mu,V}(hb)(z)+h(z)b(z)c_{\mu,V^c}(z),&z\in V,\\
-\displaystyle\int_V\frac{h(w)b(w)}{z-w}\,d\mu(w),&z\notin V,
\end{cases}
\tag{10}
\]

where `c_{mu,V^c}` is evaluated only on `K`.
The cross kernels are separated by `dist(K,V^c)>0`.
Equation (9) therefore gives a finite `a_h` such that

\[
\|e(hb)\|_2\le a_h\|b\|_\infty.
\tag{11}
\]

Uniformly bounded starred polynomials approximating a bounded measurable `b` in L2, followed by weak closedness of the original graph, extend (10)--(11) to every `b in L-infinity(mu)`.
This is precisely the C_F0049 cutoff argument: only `h` is differentiated, and no global comparison constant is used.

The actual adjoint also admits these inputs.
First approximate `h` in real C1 norm by starred polynomials.
For polynomial `b`, the inputs converge uniformly, the canonical divided differences converge in L2, and (8), including the multiplication by `xi`, converges in L2.
Closedness of the actual adjoint gives

\[
e_0^*(hb)=hb\xi-Je(h\overline b).
\tag{12}
\]

For arbitrary bounded measurable `b`, use uniformly bounded polynomial approximants converging almost everywhere and in L2.
The term `hb\xi` converges strongly by dominated convergence; (11) bounds the other term, whose weak limit is identified by the original graph of `e`.
Weak closedness of the actual adjoint proves (12) for that `b`, and hence

\[
hL^\infty(\mu)\subseteq\operatorname{Dom}e\cap\operatorname{Dom}e_0^*,
\qquad
\|e_0^*(hb)\|_2\le(a_h+\|h\xi\|_2)\|b\|_\infty.
\tag{13}
\]

In particular the maps

\[
T_h:b\longmapsto e(hb),\qquad
T'_h:b\longmapsto e_0^*(hb)
\tag{14}
\]

are bounded complex-linear maps from `C*(X_j)=C(sigma(X_j))` to `H_j`, with the bounds in (11) and (13).
They are Banach-space maps formed from actual closed operators; they do not replace those operators by new extensions.

## 4. Lifting the cutoff maps while recovering both original graphs

Use C_F0045's orthogonal right-module decomposition for this fixed `j`.
Every `p in P` has a finite expansion

\[
p=\sum_{u\in F}u b_u,\qquad b_u\in P_j,
\quad
\left\|\sum_{u\in F}|b_u|^2\right\|_\infty\le\|p\|_\infty^2.
\tag{15}
\]

The original normalized operator and its actual adjoint act on this full core as the orthogonal direct sums of `e_0` and `e_0*`, respectively.
Since `hb_u` belongs to both actual marginal domains by Section 3, the direct-sum formulas suggest values for `p h`.
We now verify these values in the two original, nonnormalized graphs.

Choose starred polynomials `q_l` converging to `h` in real C1 norm on a square containing the spectral support.
The original inputs `p q_l` lie in `P` and converge in operator norm to `p h`.
Because the expansion (15) is finite, C1 divided-difference convergence gives

\[
E_0(pq_l)\longrightarrow\sum_{u\in F}u e(hb_u)
\quad\text{in }H.
\tag{16}
\]

The corresponding actual adjoint values converge to `sum_u u e_0*(h b_u)`, by (8), C1 convergence for the conjugated input, and uniform convergence of the input multiplying `xi`.
On the original polynomial core the exact normalization identities are

\[
D_{j,0}q=E_0q+q\eta,\qquad
D_{j,0}^*q=E_0^*q+q\eta^*.
\tag{17}
\]

Uniform convergence of `p q_l` makes the two right-multiplier terms converge in L2.
Closedness of `D_j` and of the actual `D_{j,0}*` therefore proves

\[
\begin{aligned}
D_j(ph)&=\sum_{u\in F}uT_hb_u+ph\eta,\\
D_{j,0}^*(ph)&=\sum_{u\in F}uT'_hb_u+ph\eta^*.
\end{aligned}
\tag{18}
\]

This step is the required original-graph restoration.
It does not identify the closure of an unbounded sum with the sum of its closures.

Apply the already checked complex little Grothendieck inequality to each of the maps in (14), then use (15) and orthogonality.
With `k_C=4/pi`,

\[
\begin{aligned}
\|D_j(ph)\|_2
 &\le \bigl(\sqrt{k_C}a_h+\|h\|_\infty\|\eta\|_2\bigr)\|p\|_\infty,\\
\|D_{j,0}^*(ph)\|_2
 &\le \bigl(\sqrt{k_C}(a_h+\|h\xi\|_2)
                   +\|h\|_\infty\|\eta\|_2\bigr)\|p\|_\infty.
\end{aligned}
\tag{19}
\]

The constants are independent of the length and number of reduced words in `p`.

For `a in M`, take uniformly bounded polynomial approximants `p_l` converging to `a` in L2; their uniform norm bound can be made arbitrarily close to `||a||`.
Then `p_l h` converges strongly in H to `a h`, and (19) bounds both original operator outputs.
A weakly convergent subsequence in the product Hilbert space, followed by weak closedness of the two original graphs, puts `a h` in both original domains.
Lower semicontinuity proves the two bounds (19) with `p` replaced by `a`.
No graph-core assertion for `M h` is used.

## 5. Spectral projections and the common dense module

For fixed `j,n`, choose a real smooth radial cutoff `0<=h<=1` which vanishes near zero and equals one on all radii `[1/n,R_j]`; take the outer boundary of its supporting annulus strictly above `R_j`.
Then

\[
e_{j,n}h(X_j)=e_{j,n}.
\]

If `f in M e_{j,n}`, then `f=f h(X_j)`.
Apply Section 4 with coefficient `a=f` to obtain (5), with a finite constant depending on the chosen cutoff.
If the projection is zero, (5) is immediate.

Each `e_{j,n}` increases strongly to 1 because `mu_j({0})=0`.
Their finite meets `p_n` also increase and satisfy

\[
\tau(1-p_n)\le\sum_{j=1}^d\tau(1-e_{j,n})\longrightarrow0.
\tag{20}
\]

Thus `p_n` converges strongly to 1, and `E=union_n M p_n` is complex-linear, left `M`-invariant, and dense in H.
Since `p_n<=e_{j,n}`,

\[
Mp_n\subseteq Me_{j,n}
\subseteq\operatorname{Dom}D_j\cap\operatorname{Dom}D_{j,0}^*
\tag{21}
\]

for every `j`.

## 6. Exact dense-module interface

C_F0025's original-core graph approximation already proves that each generator preserves `Dom D_j` and that

\[
D_j(X_kz)-X_kD_jz=\delta_{jk}\langle1,z\rangle1
\qquad(z\in\operatorname{Dom}D_j).
\tag{22}
\]

For completeness, approximate `z` in the graph by `q_l in P`; then `X_k q_l` and their operator values converge by the bounded original generator commutator.
Closedness gives (22).
Restricting to `E` is legitimate because `E` is left `M`-invariant.

By (21), `E` is contained in the actual adjoint domain of `D_j`, and hence in the adjoint domain of its restriction `mathcal D_j`.
C_F0029 therefore applies with common dual domain `E` and every adjoint test module also equal to `E`.
Its hypotheses impose no vacuum in `E` and no right-module invariance.
All fraction inputs `bz,tz` in (7) lie in `E` by left invariance.

This proves B with the original operator values on every displayed input.
The closure used in C_F0029's final full-domain reformulation is exactly `closure(mathcal D_j)`, which is a restriction of `D_j`; no equality of these closures has been proved.

## 7. Mixed weak-form compatibility and the precise remaining gap

Fix `f in F cap M`.
B supplies a bounded finite-rank `T_j` with

\[
D_j(fz)-fD_jz=T_jz\qquad(z\in\mathcal E).
\tag{23}
\]

For `p in Dom D_j*` and `q in E`, the actual adjoint pairing gives

\[
\langle D_j^*p,fq\rangle-\langle f^*p,D_jq\rangle
=\langle p,T_jq\rangle.
\tag{24}
\]

In particular (24) holds on `P x E`.
There is also the complementary identity on `E x Dom D_j`.
Indeed `p,f*p in E` are both in `Dom D_j*`.
Pair (23) against `p` for all `z in E`.
Density gives the equality of actual Hilbert vectors

\[
D_j^*(f^*p)-f^*D_j^*p=-T_j^*p.
\tag{25}
\]

Pairing (25) against an arbitrary `q in Dom D_j` proves (24) there.
Thus the existing and local-module weak forms agree with the same bounded finite-rank operator whenever at least the appropriate one of the two test vectors lies in `E`.

This does **not** permit passage to `P x P` merely from Hilbert density of `E`: both terms contain unbounded operators.
One sufficient missing bridge would be graph density of `E` in every original `Dom D_j`, or graph density in every original adjoint domain; either would justify a limit in (24).
Another compatible extension argument could suffice, but none is supplied here.
C_F0029 expressly warns against replacing the closure of the prescribed restriction by a larger closed extension.

Accordingly the result removes global angular comparison for original *local* dual/adjoint domains and for the full affiliated criterion tested on their common dense module.
It neither asserts an original all-M domain conclusion nor settles the original starred-polynomial weak-form converse for this larger class.
Singular angular laws, correlated tuples, Q1/Q2/Q4 at their full scope, and bounded rational reconstruction are unaffected.

## 8. Review targets and continuation

An independent review should check: annular normalization under only local comparison; the original marginal adjoint limit (12); both original nonnormalized graph limits (16)--(18); the domain and column-square hypotheses for little Grothendieck; approximation of `a h` with constants controlled by `||a||`; projection-meet density; the exact C_F0029 inputs; and both signs in (24)--(25).

The next mathematical question is the explicit graph-core/compatible-extension bridge in Section 7.
It should be tested before reporting an enlarged solution of the original Q3 converse.
The present A/B proof is sufficient for a separate scoped continuation after review, without changing the original Task's completion criteria.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:03 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#annulus-local-dual-domains) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Local annular density bounds restore the original dual and adjoint on spectral windows; the common dense module supports the full affiliated criterion, with the original polynomial-core converse left open.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:08 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#annulus-local-dual-domains) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original polynomial-core normalization, adjoint identity and bounded-generator graph invariance. |
| dependency | [Exact material](Yin_C_F0029_v1.md#decision-candidate-0002) | Complete affiliated criterion on the constructed common dense left module; closure-of-restriction boundary retained. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Full-core orthogonal right-module decomposition, actual adjoints, column-square estimate and little Grothendieck lifting interface. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficiency on each normalized annulus away from zero, including positive-radius atoms. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Measurable sufficient density transfer on a fixed annulus. |
| dependency | [Exact material](Yin_C_F0049_v1.md#decision-candidate-0002) | Finite-measure annular normalization and smooth-cutoff recovery in the original global graph; no global necessity step reused. |
| review | [Exact material](../audits/reviews/Yin_R_F0026_v1.md) | Entire selected module, assertions A and B and mixed pairings; fixed direct inputs; original polynomial-core converse explicitly excluded. |

Recorded mathematical summary: Local annular density bounds restore the original dual and adjoint on spectral windows; the common dense module supports the full affiliated criterion, with the original polynomial-core converse left open.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:07 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#annulus-local-dual-domains) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original polynomial-core normalization, adjoint identity and bounded-generator graph invariance. |
| dependency | [Exact material](Yin_C_F0029_v1.md#decision-candidate-0002) | Complete affiliated criterion on the constructed common dense left module; closure-of-restriction boundary retained. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Full-core orthogonal right-module decomposition, actual adjoints, column-square estimate and little Grothendieck lifting interface. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficiency on each normalized annulus away from zero, including positive-radius atoms. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Measurable sufficient density transfer on a fixed annulus. |
| dependency | [Exact material](Yin_C_F0049_v1.md#decision-candidate-0002) | Finite-measure annular normalization and smooth-cutoff recovery in the original global graph; no global necessity step reused. |
| review | [Original finding](../audits/reviews/Yin_R_F0026_v1.md#6-scope-of-acceptance) | Whole exact assertions A/B and mixed pairings, self-reviewed with disclosed prior conditional original-closure bridge development; original polynomial-core converse and unadopted conditional graph bridge excluded. |

## Recorded review scopes

Entire selected module, assertions A and B and mixed pairings; fixed direct inputs; original polynomial-core converse explicitly excluded.

Review: [Exact material](../audits/reviews/Yin_R_F0026_v1.md).

Material covered by that review: [Exact material](Yin_C_F0050_v1.md).
