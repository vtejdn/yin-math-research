---
author: Yin
---

# Rational derivative factors and restricted minimal L2 states

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Canonical Rational Derivatives and Square-Integrable States

<a id="statement"></a>

<a id="yin_c_f0007"></a>
## Yin_C_F0007: Rational Tensor Factors and a Restricted Minimal-State Consequence

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Date: 2026-09-09.
Provenance: project deduction from [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002), [Yin_C_F0005](Yin_C_F0005_v1.md#yin_c_f0005), and the audited [MSY23 bounded-dual/maximal-Delta interfaces](../audits/literature/MSY23/readme.md#accepted-inputs).
Prepared in response to the user's request to use the classical Kronecker proof to advance Yin_C_F0001.
Current assessment: [selected assessment](#decision-isolated-review-20261022); review evidence remains in the [independent audit](../audits/reviews/Yin_R_F0062_v1.md#rational-states).
No novelty claim is made.

The unrestricted result identifies the actual finite commutators with algebraically differentiated rational expressions and supplies rational L2 factors.
A further statement supplies L2 left and right states for a specified minimal representation regular at a scalar point.
Neither statement establishes bounded scalar division closure.

## Setting and Statements

Assume all of [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001): a finite tracial von Neumann algebra (M,tau), bounded normal generators X=(X_1,...,X_d), M=W*(X), H=L2(M,tau), Omega=1, P=P_Omega, and bounded duals satisfying [D_i,lambda(X_j)]=delta_ij P.
Write U=U(M) and

\[
F=\operatorname{Div}_{U}\mathbb C\langle X\rangle.
\]

The audited MSY23 interface identifies F with the evaluated free field and gives maximal Delta.
Identify H with its canonical subspace of U.
Every tensor product in this record is algebraic over C, not a Hilbert-space completion.
For g,h in H, use the Yin_C_F0002 convention

\[
\Theta(g\otimes h)\xi=g\langle Jh,\xi\rangle,
\qquad \Theta:H\otimes H\longrightarrow\operatorname{FinRank}(H).
\]

This is a linear bijection.
For bounded g,h, it is the operator gPh; for arbitrary L2 factors it is defined by the displayed rank-one formula, not by an unjustified product of unbounded multipliers.

1. **Uniqueness on affiliated tensors.**
   The map

   \[
   \Psi:(U\otimes U)^d\longrightarrow U\otimes U,
   \qquad
   \Psi((t_i)_i)=\sum_i\Psi_i(t_i),
   \quad
   \Psi_i(g\otimes h)=gX_i\otimes h-g\otimes X_i h
   \tag{1}
   \]

   is injective.
   Algebraically differentiating a valid scalar rational expression for any f in F, using the outer bimodule product and inverse rules, gives tensors \(\partial_i^{\mathrm{rat}}f\in F\otimes F\) independent of the chosen expression.

2. **Actual finite derivatives have rational L2 factors.**
   If f in M has finite-rank [D_i,lambda(f)] for every i, then Yin_C_F0005 gives f in F and

   \[
   \Theta^{-1}([D_i,\lambda(f)])
      =\partial_i^{\mathrm{rat}}f
      \in(F\cap H)\otimes(F\cap H).
   \tag{2}
   \]

   Thus each finite commutator has a finite factorization whose two families lie in F intersect L2(M,tau).
   This asserts existence of suitable rational factors; it does not assert that every originally chosen factor family is rational or bounded.

3. **L2 states for a minimal monic representation.**
   In addition to part 2, suppose the formal rational function representing f admits

   \[
   r(x)=u\Bigl(I_n-\sum_i A_i x_i\Bigr)^{-1}v,
   \quad u\in M_{1,n}(\mathbb C),\quad v\in M_{n,1}(\mathbb C),
   \quad A_i\in M_n(\mathbb C),
   \tag{3}
   \]

   with the explicit reachability and observability conditions

   \[
   \operatorname{span}_{\mathbb C}\{A_wv:w\text{ a word}}=\mathbb C^n,
   \qquad
   \bigcap_w\ker(uA_w)=\{0\}.
   \tag{4}
   \]

   Here the empty word is included and A_empty=I_n.
   Put B=I_n-sum_i A_i X_i, which is invertible over U by the free-field evaluation, and

   \[
   g=uB^{-1},\qquad h=B^{-1}v.
   \]

   Then every entry of g and h belongs to F intersect H.
   Moreover,

   \[
   \operatorname{rank}[D_i,\lambda(f)]=\operatorname{rank}_{\mathbb C}A_i,
   \qquad
   n\le1+\sum_i\operatorname{rank}[D_i,\lambda(f)].
   \tag{S}
   \]

   Thus the finite commutator ranks bound the dimension of this minimal state space.
   This conclusion concerns these left and right states; it does not assert that every entry of B^{-1} is L2 or bounded.
   The representation is explicitly regular at scalar zero.
   No claim that every free-field element admits such a scalar chart is made.

## 1. Extend Finite-Cycle Injectivity by Clearing Outer Denominators

Let rho(a) denote right multiplication by a.
The source convention for Delta uses rho(X_i)=J lambda(X_i*)J.
Maximal Delta means that a finite-rank cycle

\[
\sum_i[\rho(X_i),T_i]=0
\]

has every T_i zero.
The sign obtained by reversing both commutators does not change this zero-cycle condition.
The exact input is [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002), together with the bounded-dual implication in [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005).
Neither an adjoint-generator substitution nor a selfadjointness hypothesis is introduced.

Yin_C_F0002's tensor convention gives, for g,h in H,

\[
[\rho(X_i),\Theta(g\otimes h)]
=\Theta(gX_i\otimes h-g\otimes X_i h).
\tag{5}
\]

Both products remain in H because X_i is bounded.
It follows at once that Psi is injective on (H tensor H)^d.

Now take any tuple t in (U tensor U)^d with Psi(t)=0, and choose finite decompositions of all its entries.
There are common bounded regular elements a,b in M such that every first factor g in these decompositions satisfies ag in M and every second factor h satisfies hb in M.
Here regular means invertible over U, not necessarily invertible over M.
This uses only the finite-tracial affiliated algebra and its rectangular polar decomposition.
Explicitly, for the affiliated row G formed from all first factors one may take

\[
a=(1+GG^*)^{-1/2};
\]

functional calculus makes a a bounded regular element and aG a bounded row.
For the affiliated column C formed from all second factors, take

\[
b=(1+C^*C)^{-1/2},
\]

so Cb is bounded.
These constructions also explain why the two denominators must be placed on the indicated outer sides.

Define the outer multiplication map

\[
L_aR_b(g\otimes h)=ag\otimes hb.
\]

It is invertible on U tensor U, since a,b are units of U, and

\[
\Psi_i(ag\otimes hb)
=agX_i\otimes hb-ag\otimes X_i hb
=L_aR_b\bigl(\Psi_i(g\otimes h)\bigr).
\tag{6}
\]

Consequently s_i=L_aR_b(t_i) lies in M tensor M, hence in H tensor H, and Psi(s)=0.
The finite-cycle argument gives every s_i=0.
Invertibility of L_aR_b then gives every t_i=0, proving (1) on the full affiliated tensor space.
No boundedness of a^{-1} or b^{-1} was used.

## 2. Rational Differentiation and the Actual Commutators

Define derivatives first on a chosen rational expression, not on equivalence classes.
Start with partial_i X_j=delta_ij(1 tensor 1) and partial_i c=0, and use

\[
\begin{aligned}
\partial_i(ab)&=(\partial_i a)\cdot b+a\cdot(\partial_i b),\\
\partial_i(a^{-1})&=-a^{-1}\cdot(\partial_i a)\cdot a^{-1}.
\end{aligned}
\tag{7}
\]

The outer bimodule convention is c dot (g tensor h) dot e=(cg) tensor (he).
For a valid scalar expression in the division ring F, (7) produces finite tensors in F tensor F.
Put delta(a)=a tensor 1-1 tensor a.
It satisfies the same product and inverse identities.
Each Psi_i is a homomorphism for these outer bimodule actions.
Induction on the expression therefore gives

\[
\sum_i\Psi_i(\partial_i r)=\delta(r).
\tag{8}
\]

If two expressions represent the same element of F, subtract (8).
Injectivity of Psi proves equality of their derivative tuples.
This establishes expression independence directly, rather than importing a differentiation theorem for the free field.

For the f in part 2, let t_i=Theta^{-1}([D_i,lambda(f)]).
Yin_C_F0005's normal commutator identity gives

\[
\sum_i\Psi_i(t_i)=f\otimes1-1\otimes f.
\tag{9}
\]

Yin_C_F0005 also places f in F.
Its rational derivative tuple from (8) and the actual tuple from (9) therefore have the same Psi image, so injectivity gives t_i=partial_i^rat f in U tensor U.
This proves the equality in (2), with no attempt to form a bounded commutator with the unbounded intermediate elements of a rational expression.

### The Algebraic Tensor Intersection

For any two vector subspaces E,L of a complex vector space V,

\[
(E\otimes E)\cap(L\otimes L)
=(E\cap L)\otimes(E\cap L)
\quad\text{inside }V\otimes V.
\tag{10}
\]

To prove it, choose vector-space complements E=K direct-sum E_0 and L=K direct-sum L_0, where K=E intersect L.
Their sum is the direct sum K direct-sum E_0 direct-sum L_0: any relation between E_0 and L_0 modulo K would contradict the definition of K.
Extend this to a vector-space decomposition of V.
The resulting tensor-block decomposition is direct, and the only blocks shared by E tensor E and L tensor L form K tensor K.
This is an algebraic argument; no topological complement or bounded projection is asserted.

Apply (10) with V=U, E=F, L=H.
The identified derivative belongs both to F tensor F and to H tensor H, so it belongs to (F intersect H) tensor (F intersect H), proving the rational L2 factor assertion.

## 3. Recover the Left and Right Minimal States in L2

First, the entries of g and of h in (3) are each complex-linearly independent.
For example, a constant column c with gc=0 gives the formal coefficients uA_w c=0 for every word w, so observability forces c=0.
A constant row c with ch=0 similarly gives cA_w v=0 for every w; reachability forces c=0.
These formal coefficient comparisons are legitimate because the displayed monic inverse is regular at zero and has the formal expansion sum_w A_w x^w.
A zero free-field rational function has zero such expansion by the same defined-domain rational consistency used in [MSY23-U003](../audits/literature/MSY23/Yin_U003.md#msy23-u003).
The formal series algebra is stably finite: a one-sided inverse of a square matrix forces its constant matrix to be invertible, and its resulting formal Neumann inverse is two-sided.
Thus that consistency theorem applies here.
The injective evaluation F into U preserves these linear-independence statements for the evaluated entries.

The inverse rule in (7) yields

\[
\partial_i^{\mathrm{rat}}f
=\sum_{j,k=1}^n g_j(A_i)_{jk}\otimes h_k
=\sum_k(gA_i)_k\otimes h_k
=\sum_j g_j\otimes(A_i h)_j.
\tag{11}
\]

Let pi:U to U/H be the algebraic vector-space quotient.
Part 2 says (11) lies in H tensor H, hence its image under pi tensor id is zero.
Linear independence of the h_k gives pi((gA_i)_k)=0 for every k.
Thus gA_i has L2 entries.
Apply id tensor pi instead and use independence of the g_j to conclude that A_i h has L2 entries.

Finally the defining equations gB=u and Bh=v read

\[
g=u+\sum_i(gA_i)X_i,
\qquad
h=v+\sum_i X_i(A_i h).
\tag{12}
\]

Right and left multiplication by the bounded X_i preserve H.
All terms on the right of (12) therefore have L2 entries.
This proves the state assertion.
The formulas make no orthogonality or completeness assumption about evaluated words.

### Exact Coefficient Ranks and the State-Dimension Bound

The left state family defines an injective map G:C^n to H by Gc=sum_j g_j c_j.
The right family defines a surjective map L:H to C^n by (Lxi)_k=<Jh_k,xi>.
Its surjectivity follows from linear independence of the h_k and finite dimensionality of the target.
Equations (2) and (11) give the factorization

\[
[D_i,\lambda(f)]=G A_i L.
\]

Since G is injective and L is surjective, this operator has rank exactly rank_C A_i.
This proves the first assertion in (S), without requiring either state family to be orthonormal.
For every nonempty word w=i_1...i_k, the vector A_wv lies in Ran A_{i_1}.
Reachability therefore gives

\[
\mathbb C^n=\operatorname{span}\{A_wv\}
\subseteq\mathbb Cv+\sum_i\operatorname{Ran}A_i,
\]

so n<=1+sum_i rank_C A_i.
This proves the second assertion in (S).
The estimate is for the representation satisfying the explicitly stated minimality conditions; adding unused states would destroy the relevant independence and is not allowed.

## 4. A Boundary Example: Rational L2 Does Not Imply Bounded

Let S be the closed unit disk and

\[
d\mu(z)=\frac{2}{\pi}|z|^2\,dA(z),
\qquad M=L^\infty(S,\mu),\quad X(z)=z.
\]

The measure is a probability, is nonatomic, and has full disk support.
X is bounded normal and generates M as a von Neumann algebra.
On L2(mu), define the Cauchy operator initially on bounded functions by

\[
(D\xi)(z)=\int_S\frac{\xi(w)}{w-z}\,d\mu(w).
\]

The singularity is locally integrable in two dimensions.
Both Schur integrals of the absolute kernel are at most

\[
\frac{2}{\pi}\int_{|u|<2}\frac{1}{|u|}\,dA(u)=8.
\]

Thus D extends boundedly to L2(mu), with norm at most 8.
Direct cancellation gives [D,X]xi=integral xi dmu, hence [D,X]=P.
The calculation first holds on bounded functions and extends by boundedness.

Since the zero set of X has measure zero, X is invertible over U.
Its rational inverse belongs to F, and

\[
\left\|\frac1z\right\|_{L^2(\mu)}^2
=\frac{2}{\pi}\int_{|z|\le1}dA(z)=2.
\]

Nevertheless 1/z is not essentially bounded: mu({|z|<epsilon})=epsilon^4>0 for every 0<epsilon<1.
Therefore F intersect H is not contained in M, even with a bounded normal generator and a bounded dual.

This example limits the proposed implication "rational L2 factors are automatically bounded."
It is not a bounded f with finite commutators whose good state realization is impossible.
Indeed, [Yin_C_F0004](Yin_C_F0004_v1.md#yin_c_f0004) proves the original conjecture for this one-generator model and gives zero-free bounded denominators for its bounded finite-rank elements.
No counterexample to Yin_C_F0001 or to a bounded-realization existence statement is claimed.

## Consequences and Remaining Proof Obligations

The result advances the [Unt20 reconstruction route](../strategies/Yin_S_F0001.md#s_f0001) by producing a suitable rational L2 tensor family.
It also supplies actual L2 left and right states in the specified monic minimal chart, which is a concrete finite-state consequence of the finite commutators.
Neither conclusion duplicates only the field-membership statement of Yin_C_F0005.

For a Kronecker-style stability argument, further control is still required.
Norms of evaluated states in L2(M,tau) do not by themselves give square summability of the formal free-word coefficients: evaluated words need not be orthogonal, independent as an L2 expansion, or total.
Consequently a coefficient-space Gramian or a strict-row-contraction theorem cannot be applied solely on the basis of (12).
A missing next interface is an estimate that converts these actual state vectors into a coefficient or realization norm strong enough to bound an entire inverse pencil, or a different direct boundedness argument for a rational realization.

Even a bounded matrix inverse realization must be related to Yin_C_F0001's scalar division closure through an applicable bounded elimination argument.
The present result supplies neither that scalar descent nor the reverse implication that every bounded affiliated rational function has finite commutators.
It does not assume a bounded dual can be normalized to kill Omega, and it does not extend the commutator formula to arbitrary affiliated inputs as a bounded-operator identity.

The proof uses the already audited maximal-Delta and affiliated-operator foundations, ordinary finite-dimensional linear algebra, and an explicit Schur-test example.
The [current independent mathematical review](../audits/reviews/Yin_R_F0062_v1.md#rational-states) records its checked artifact and scope; the [selected assessment](#decision-isolated-review-20261022) records the assessment.
No numerical computation, formal verification, external human review, or full new source audit is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:20 |
| status | proved |
| reason | Select the actual previously adopted finding explicitly, preserving its original date, complete checked mathematical scope and retained limits while declaring its actual known or genuinely unestablished relationship. The statement, argument, dependencies and mathematical assessment are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#1-extend-finite-cycle-injectivity-by-clearing-outer-denominators) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Actual complete finding](../audits/reviews/Yin_R_F0062_v1.md#rational-state-finding) | Entire affiliated finite-cycle injectivity with common outer denominators, rational derivative descent, algebraic intersection/L2 factors, conditional minimal monic state identities and exact rank bounds, including the weighted-disk boundary. No whole inverse L2/boundedness, universal scalar chart, bounded scalar reconstruction or Task completion. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:48 |
| status | proved |
| reason | Adopt the actually performed context-isolated independent whole-argument finding after its complete comparison with the old review; fixed mathematics and historical decisions remain at their original scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#1-extend-finite-cycle-injectivity-by-clearing-outer-denominators) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0062_v1.md#rational-states) | Complete affiliated finite-cycle injectivity, rational derivative/L2 factors, conditional minimal monic states and exact ranks, weighted-disk counterexample and all boundedness/scalar-chart/source limits. |

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
| argument | [Exact material](#1-extend-finite-cycle-injectivity-by-clearing-outer-denominators) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0062_v1.md#rational-state-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0062_v1.md#rational-state-finding).

Material covered by that review: [Exact material](Yin_C_F0007_v1.md).
