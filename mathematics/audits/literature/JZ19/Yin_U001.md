---
author: Yin
---

# JZ19: Coefficient Base Change, Regular Envelopes, and Sofic Rank Approximation

<a id="jz19-u001"></a>
## Source, inspection, and conclusion boundary

The inspected original is the [GAFA journal edition](readme.md#journal-edition), printed pp. 464–538, corresponding to PDF pp. 1–75.
All 75 pages, including every proof in Sections 3–10, the introductory statements and proof outline, and the references, were read on 2026-11-10.
The proof reconstruction below distinguishes the arguments actually supplied in this edition from its cited foundations.
Rendered PDF pp. 49 and 52 were also inspected to verify the missing constant-function qualifications described below.
The relevant online author-manuscript passages were compared only for that issue; they were not substituted for the journal edition.

This was a separately organized source inspection by an agent outside the current project's substantive proof development.
The assignment, repository rules, source identity, and broad application question were supplied, but the main agent's new mathematical development and conclusions were not supplied.
No project Claim or proposed new proof of the unrestricted Atiyah conjecture was reviewed here.
The exposition and local checking explanations in this rolling unit were self-checked by its authoring agent.
This is a complete reading and proof audit of the selected article, with explicit external-foundation and local-proof limits, rather than a claim of foundational reproof of every cited work.
The initially unresolved Lemma 9.10 interface is supplied by the separate [fixed completion](../../../claims/Yin_C_A0002_v1.md), developed by the coordinating agent and checked in the independent review selected there.
That local proof and its review have their own scope; they do not retrospectively enlarge the initial source review or constitute an independent review of this entire article.

The article proves complex-coefficient sofic rank approximation and, conditional on the strong Atiyah conjecture over the algebraic numbers for the same sofic group, complex-coefficient strong Atiyah.
It does not prove the strong Atiyah conjecture for every torsion-free sofic group, nor remove soficity from its coefficient-change argument.
The arithmetic proof contains literal statement errors at constant rational functions, and the Hilbert–Schmidt argument needs the distinctness and codomain corrections recorded below, with a complete local proof of its weak-injectivity step.
These are distinguished from a counterexample to the main theorems; none is asserted here.

<a id="rank-and-approximation-definitions"></a>
## Rank conventions and approximation objects

Sections 1.1–1.4, printed pp. 466–470, use right multiplication by an $n\times m$ group-ring matrix $A$ on row vectors in $\ell^2(G)^n$.
The group acts on the left for the Hilbert-module structure.
The rank is

\[
\operatorname{rk}_G(A)=\dim_G\overline{\operatorname{im}A}
=n-\dim_G\ker A.
\]

The trace on $M_n(\mathcal N(G))$ is the sum of the diagonal group traces, so $\operatorname{rk}_G(I_n)=n$, without division by $n$.
For finite $G$, the ordinary complex rank of the induced matrix is divided by $|G|$.
For an arbitrary group the rank of a finite matrix is computed inside a finitely generated subgroup containing its support; induction of Hilbert modules makes this independent of the subgroup.
The strong Atiyah assertion over $K\subseteq\mathbb C$, when $d=\operatorname{lcm}(G)<\infty$, is $\operatorname{rk}_G(A)\in d^{-1}\mathbb Z$ for every rectangular matrix over $K[G]$.
For torsion-free $G$, $d=1$.
This is consistent with the [existing affiliated strong-Atiyah normalization](../MSY23/Yin_U005.md#setting-and-closure-conventions), but no identification with polynomial inner rank is part of this definition.

**Definition: sofic approximation in the source's presentation convention.**
Write $G=F/N$, where $F$ is free on a finite set $S$, and let $B_s(1)$ be its word ball.
A sequence of nonempty finite right $F$-sets $X_k$ is a sofic approximation if, for each $s$, the proportion of points $x\in X_k$ for which

\[
xw=x\quad\Longleftrightarrow\quad w\in N
\qquad(w\in B_s(1))
\]

tends to one.
The source calls a finitely generated group sofic when it admits such an approximation, and an arbitrary group sofic when all its finitely generated subgroups do.
For $A\in M_{n\times m}(K[F])$, the finite rank is $\operatorname{rk}_{X_k}(A)=|X_k|^{-1}\operatorname{rank}_{K}(f_{X_k}(A))$, or equivalently the complex rank after the specified embedding of $K$.

**Definition: general approximation.**
Section 6.3, pp. 493–494, replaces each finite $X_k$ by an $(H_k,F)$-set: the left $H_k$-action is free, has finitely many orbits, and commutes with the right $F$-action.
The same local relations are required on a proportion tending to one of the $H_k$-orbits.
After choosing orbit representatives, the operator algebra is $M_{|H_k\backslash X_k|}(\mathcal U(H_k))$, and its rank is $|H_k\backslash X_k|^{-1}\operatorname{rk}_{H_k}$.
A different set of representatives changes coordinates by conjugation and leaves the rank unchanged.
Finite sofic approximations have $H_k=1$; converging marked groups arise from transitive left and right actions.

Theorem 1.3, p. 470, states $\operatorname{rk}_{X_k}(A)\to\operatorname{rk}_G(A)$ for every complex group-ring matrix and every sofic approximation.
Theorem 10.1, p. 530, proves the analogous assertion for general approximations when all the groups $H_k$ are sofic.
In particular, Corollary 1.4 concerns convergence through sofic marked groups, not arbitrary marked groups.

<a id="regular-closure-definitions"></a>
## Regular rings, relative inverses, and the three closure operations

Sections 3–4, pp. 476–481, distinguish the following constructions.
The ambient affiliated ring is the classical Ore localization $\mathcal U(G)$ of $\mathcal N(G)$, equivalently the ring of closed densely defined affiliated operators with the affiliated-ring operations.
It is a positive definite $*$-regular ring, with a faithful rank satisfying $\operatorname{rk}_G(u)=1$ exactly when $u$ is invertible.
The existence of this affiliated-ring structure and its localization interpretation is cited to Berberian and Reich; its original analytic construction is not reproved in JZ19.

**Definition: regularity, proper involution, and relative inverse.**
A unital ring $U$ is von Neumann regular if, for every $x\in U$, some $y\in U$ satisfies $xyx=x$.
An involution is proper if $x^*x=0$ implies $x=0$, and positive definite if $\sum_{i=1}^n x_i^*x_i=0$ implies every $x_i=0$, for every finite $n$.
A $*$-regular ring is regular with proper involution; positive definiteness guarantees that every matrix ring is again $*$-regular.
For $x\in U$, the source denotes by $e=\operatorname{RP}(x)$ and $f=\operatorname{LP}(x)$ the unique projections satisfying $Ux=Ue$ and $xU=fU$.
The relative inverse $x^{[-1]}$ is the unique $y\in eUf$ with $yx=e$ and $xy=f$.
It is an inverse on the support, not necessarily a two-sided inverse of $x$ in the unital ring.

Proposition 3.2 is checked directly using $\operatorname{Ann}_r(x^*x)=\operatorname{Ann}_r(x)$, properness, and uniqueness of projections generating the same principal ideal.
Its identities $(x^*)^{[-1]}=(x^{[-1]})^*$ and $x^{[-1]}=(x^*x)^{[-1]}x^*$ explain why adjoining relative inverses preserves the involution.
For selfadjoint $x$, $x$ commutes with $x^{[-1]}$.
Proposition 3.3 follows because $x^*x\in I$ implies $x,x^*\in I$, giving a proper induced involution on every quotient.

**Definition: the $*$-regular closure and its rank completion.**
For a $*$-subring $R\subseteq U$ of a $*$-regular ring, $\mathcal R(R,U)$ is the smallest $*$-regular subring containing $R$.
Proposition 3.4 constructs it by repeatedly adjoining relative inverses and taking the union; Corollary 3.5 says closure under relative inverses of selfadjoint elements already suffices.
For conjugation-stable $K\subseteq\mathbb C$, write

\[
\mathcal R_{K[G]}=\mathcal R(K[G],\mathcal U(G)),
\qquad
\overline{\mathcal R}_{K[G]}
=\text{its completion for }d(a,b)=\operatorname{rk}_G(a-b).
\]

The overline is essential in the center and algebraic-base-change proof of Section 10.1.
It is a rank-metric completion, not an operator-norm or strong-operator closure.

The rational and division closures retain their [existing fixed-ambient definitions](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra).
JZ19 Section 4.2 defines the rational closure through entries of inverses of matrices over the original ring that are actually invertible in the specified ambient ring.
Its universal localization $R_\Sigma$ is the initial ring making the chosen square matrices $\Sigma$ invertible; the map to a concrete ambient rational closure need not be injective merely from this universal property.
JZ19's $*$-regular closure additionally contains support projections and relative inverses of singular elements.
No general equality among these closures is asserted by Sections 3–6.

<a id="epic-rank-linearization"></a>
## Epic envelopes and the block-matrix mechanism

**Definition: epic homomorphism and Sylvester ranks.**
A unital ring map $f:R\to U$ is epic if two maps out of $U$ agreeing on $f(R)$ agree everywhere.
It need not be surjective.
Proposition 4.1 identifies this with the multiplication isomorphism $U\otimes_R U\to U$, while Proposition 4.2 says a regular ring has no strictly larger dominion under a ring map.
Both are cited to Stenström, Propositions XI.1.2 and XI.1.4.
Corollary 4.3 is proved by comparing dominions and identifies images of two epic regular $R$-rings in a common ambient ring.

A Sylvester matrix rank assigns nonnegative real numbers to finite rectangular matrices, has rank zero on zero matrices and rank one on $1$, is bounded above by either factor under multiplication, is additive on block diagonal sums, and is at least the sum of the diagonal ranks on block upper triangular matrices.
Its associated module rank on $M_A=R^m/(R^nA)$ is $\dim(M_A)=m-\operatorname{rk}(A)$.
Faithfulness means $\operatorname{rk}(a)=0\Rightarrow a=0$.
A regular rank is induced through a homomorphism to a regular ring; a $*$-regular rank is induced through a $*$-homomorphism to a $*$-regular ring.
An epic $*$-regular $R$-ring in Section 6.2 includes the faithful rank as data and requires that its underlying ring be generated as a $*$-regular closure of the image of $R$.
Its isomorphisms commute with the $R$-maps, preserve $*$, and preserve rank.

Proposition 5.1, pp. 482–483, derives subadditivity, the product bound $\operatorname{rk}(uv)\geq\operatorname{rk}(u)+\operatorname{rk}(v)-1$, and a bound $n/\epsilon$ on scalar rank drops $\operatorname{rk}(A-\lambda I_n)\leq n-\epsilon$.
The scalar bound uses pairwise comaximal factors $A-\lambda_i I$ and induction on their product.
Proposition 5.10, pp. 488–489, extends this to rectangular pencils:

\[
\#\{\lambda:\operatorname{rk}(A)-\operatorname{rk}(A-\lambda B)\geq\epsilon\}
\leq\operatorname{rk}(A)/\epsilon
\]

for a regular rank.
The proof chooses $C$ with $ACA=A$, compresses to the corner with identity $CA$, normalizes the corner rank by $\operatorname{rk}(CA)$, and applies the previous scalar bound there.
This is a bound for one fixed rank, not the uniform finiteness over all finite permutation representations proved later in Section 8.

Proposition 5.11, pp. 489–491, is the key finite presentation argument.
For $R\subseteq U$ epic with $U$ regular and finitely many $r_i\in U$, it constructs one matrix $M$ over $R$ and rows $v_i$ over $R$ such that

\[
\operatorname{rk}\Bigl(\sum_i t_i r_i\Bigr)
=\operatorname{rk}\begin{pmatrix}M\\ \sum_i t_i v_i\end{pmatrix}
-\operatorname{rk}(M)
\qquad(t_i\in R).
\]

The same presentation works for every Sylvester rank on $U$.
The proof writes $U$ as a filtered colimit of finitely presented $R$-modules, uses $U\otimes_R U=U$, and observes that the kernel of $U^k\to\sum_i Ur_i$ is finitely generated because the sequence splits over the regular ring.
Those finitely many relations vanish at a single finite stage of the colimit.
At that stage the generated submodule maps isomorphically to $\sum_i Ur_i$, and the difference of the two presentation ranks gives the formula.
The finite generation of this kernel is what makes the argument uniform in the coefficients $t_i$ and the rank function.

Proposition 6.1, pp. 491–492, verifies that $*$-regular closure is epic.
Inside $U\otimes_R U$, let $S=\{r:1\otimes r=r\otimes1\}$.
It is a subring containing $R$.
If $r\in S$ is selfadjoint and $s=r^{[-1]}$, the identities $rs=sr$, $rsr=r$, and $srs=s$ give the displayed tensor calculation $1\otimes s=s\otimes1$.
Corollary 3.5 forces $S=U$, proving that multiplication on the tensor product is an isomorphism.
Corollary 6.2 applies Proposition 5.11 to matrix rings and gives the same rank-difference formula for rectangular matrices with entries in $\mathcal R(R,U)$.

Theorem 6.3, pp. 492–493, then identifies two epic $*$-regular envelopes if and only if their ranks agree on every matrix over $R$.
The proof takes the $*$-regular closure of the diagonal image of $R$ in $U_1\oplus U_2$.
Corollary 4.3 makes both projections surjective.
Corollary 6.2 transfers equality of the original matrix ranks to equality on every element of this diagonal closure.
Faithfulness makes both projection kernels zero, yielding the required rank-preserving $*$-isomorphism.
This is a structural consequence of already established matrix-rank equality, not a way to assume such equality from an abstract skew-field embedding.

The rank-ultraproduct in Section 5.7 is the product of regular rings modulo the ideal of sequences with ultralimit rank zero.
Its induced rank is faithful, and quotient properness preserves $*$-regularity.
Theorem 6.6, pp. 494–495, applies Theorem 6.3 to the affiliated rank envelope and this ultraproduct envelope.
Convergence for every group-ring matrix is equivalent to their isomorphism for every nonprincipal ultrafilter.
The final passage back from ultralimits uses boundedness of matrix ranks and the fact that a bounded real sequence converges if all its nonprincipal ultralimits equal the same value.

<a id="natural-rank-extensions"></a>
## Natural coefficient extensions and their uniqueness

Section 7, pp. 496–503, constructs rank extension rather than identifying arbitrary embeddings of coefficient fields by formal algebra alone.

**Definition: natural transcendental extension.**
For a regular rank $r$ on a $K$-algebra $R$, multiplication by $A(t)\in M_{n\times m}(R[t])$ on $(R[t]/(t^j))^n$ is a map of finite free $R$-modules.
The natural extension is

\[
\widetilde r(A)=\lim_{j\to\infty}\frac1j
r\bigl(A:(R[t]/(t^j))^n\to(R[t]/(t^j))^m\bigr).
\]

Propositions 7.4–7.5 establish existence and regularity and extend the rank to $R\otimes_K K(t)$, because every nonzero scalar polynomial has rank one.
For regular $R=U$, the associated module rank comes from the exact entropy length of Proposition 7.1.
If $Q_{j-1}\subset U[t]$ denotes the polynomials of degree at most $j-1$, Lemma 7.3 gives

\[
\widetilde r(A)=\lim_{j\to\infty}
\frac{\dim_U((Q_{j-1})^nA)}j.
\]

The proof compares polynomial image growth with the quotient modulo $t^j$; the bounded-degree boundary contributes only a bounded number of free $U$-coordinates as $j\to\infty$.
Lemma 7.2 justifies computing the entropy with any finite set of module generators, by approximating an arbitrary finite-length submodule inside a sufficiently large Laurent translate of their span.

Proposition 7.6 identifies the entropy dimension of a left ideal $I\subset U[t^{\pm1}]$ with the supremum of $r(a_0)$ over constant terms of polynomials $a_0+\cdots+a_nt^n\in I$.
The successive dimensions of $I\cap Q_j$ have monotone increments because multiplication by $t$ induces injections between the successive quotients.
Their limiting increment equals the linear growth rate.
Passing to the constant-term quotient gives the corresponding ideal in $U$, and regularity makes its finitely generated subideals cyclic, giving the supremum formula.

Proposition 7.7 proves the decisive uniqueness criterion: a Sylvester rank $r'$ on $U[t^{\pm1}]$, extending $r$, equals $\widetilde r$ if

\[
r'(I_n+tA)=n\qquad(A\in M_n(U),\ n\geq1).
\]

Its block linearization reduces every matrix polynomial with identity constant term to a larger pencil $I+tD$, preserving rank after adding known identity blocks.
For an arbitrary element, Proposition 7.6 supplies nearly maximal constant-term ranks both in its generated ideal and in its annihilator.
Multiplying by generalized inverses in $U$ converts these to polynomials with identity constant term.
The resulting lower and upper inequalities squeeze $r'$ to $\widetilde r$.
Thus the criterion is a statement over the regular envelope $U$, not merely over the original group ring.

Corollary 7.8 states that natural transcendental extension commutes with ultralimits of regular ranks.
Corollary 7.9 states that, over algebraically closed $K$, ranks obtained by evaluating $t$ at any sequence of distinct scalars converge to the natural extension.
The latter uses the scalar-rank-drop bound on $I+tA$ and Proposition 7.7.
Proposition 7.10 realizes the extension as a $*$-regular rank when the original envelope is positive definite, with $t^*=t^{-1}$.
The truncated unilateral shifts become unitary in the rank-ultraproduct because the boundary defects have normalized rank tending to zero.
Proposition 7.11 then identifies its envelope with $Q_l(U[t^{\pm1}])$ when $U$ is semisimple Artinian: non-zero-divisors have full entropy rank, and Goldie's theorem supplies the semisimple classical quotient.

**Definition: natural algebraic extension.**
For an algebraic field extension $E/K$, choose a finite subextension $E_0/K$ containing the entries of $A\in M_{n\times m}(R\otimes_K E)$.
Define $\widetilde r(A)$ to be the $R$-rank of multiplication by $A$ on the free $R$-module $R\otimes_K E_0$, divided by $[E_0:K]$.
Enlarging $E_0$ repeats the same representation with the appropriate multiplicity, so the value is independent of the choice.
Proposition 7.13 gives commutation with ultralimits directly from this finite restriction-of-scalars formula.

Proposition 7.12(1) proves that $U\otimes_K E$ is regular for a separable algebraic extension.
For finite $E/K$, embed it in $U\otimes_K\operatorname{End}_K(E)\cong M_{[E:K]}(U)$, obtain an inner inverse there, and project onto the $E$-bimodule summand $E\subseteq\operatorname{End}_K(E)$.
Separability makes that bimodule splitting available and the projected element remains an inner inverse.
Part (2) additionally assumes rank completeness, a field center, and that $K$ is relatively algebraically closed in that center.
The extended center is then a field, and the rank-complete regular-ring characterization from Proposition 5.7 supplies simplicity and uniqueness of rank.
The completeness and center hypotheses cannot be dropped from this use.

<a id="strict-eigenvalue-proof"></a>
## The strict eigenvalue theorem and its arithmetic proof

Theorem 8.1, p. 504, takes the product of all finite permutation representations $f_X:E[F]\to M_{|X|}(E)$, where $E\subseteq\mathbb C$ is conjugation-stable.
For $z,w\in M_{n\times m}(\mathcal R(f(E[F]),\prod_X M_{|X|}(E)))$ and $\epsilon>0$, it asserts finiteness of the scalars $\lambda\in\overline E$ for which

\[
\operatorname{rank}(w_X)-\operatorname{rank}(w_X-\lambda z_X)
\geq\epsilon |X|
\]

for at least one finite $F$-set $X$.
The quantifier over all $X$ is essential.
Theorem 2.2 is its group-ring specialization.
Neither statement assumes that the finite sets form a sofic approximation.

Section 8.1 uses Corollary 6.2 to replace $w-\lambda z$ by a matrix pencil over the original group ring and a fixed rank subtraction.
The subtraction cancels from the rank drop, so the exceptional sets are unchanged.
One may therefore enlarge the coefficient field to an algebraic closure and work with ordinary group-ring matrices $A,B$.
The two examples in Section 8.2 are explanatory special cases, and the source explicitly does not use them as later lemmas.

Sections 8.3–8.5 establish the quantitative input over Dedekind domains.
For a matrix $M$, $\deg_+(M)$ is the length of the torsion part of the presented module, using $\log_2$ of cardinality in the number-field case and dimension over the algebraically closed constant field in the function-field case.
Localizing at every maximal ideal reduces to Smith normal form over a discrete valuation ring.
Lemma 8.3 identifies the torsion length with the colength of the ideal of maximal nonzero minors.
Lemma 8.4 compares the torsion length of the matrix obtained by stacking $\alpha I_m$ under $M$ with $(m-\operatorname{rank}M)\deg_+(\alpha)$.
Its error is bounded by $\deg_+(M)$, by splitting the presented module into its projective torsion-free part and torsion part.
Proposition 8.5 applies this comparison locally to $M_2-\alpha M_1$, obtaining

\[
\deg_+(\alpha)\leq
\frac{\deg_+(M_2)}{\operatorname{rank}(M_2)-\operatorname{rank}(M_2-\alpha M_1)}.
\]

At a place where $\alpha$ has a pole, its positive valuation is zero, so that place contributes nothing to the inequality.

For number fields, Lemmas 8.6–8.7 bound torsion length through one nonzero minor, the product formula, and the maximum column sum of the absolute sizes of all Galois conjugates of the coefficients.
Permutation substitution does not increase this coefficient bound, independently of $|X|$.
Corollary 8.8 therefore controls the positive ideal norm $N_+(\alpha)$ from a rank drop of size $\epsilon |X|$.
Proposition 8.15 turns bounded degree and bounded values $N_+(\alpha-i)$, for finitely many consecutive integers $i$, into finiteness of $\alpha$.
The proof forms the conjugate-product polynomial and recovers its coefficients from its values by an invertible Vandermonde matrix; after normalizing by the common ideal factor the allowed integer norm values form a finite set.
This is why merely bounding the complex absolute value of a possible eigenvalue would not suffice.

For function fields, the valuations are normalized to have value group $\mathbb Z$ on each finite extension of the rational function field.
The sum of the positive valuations of a nonconstant function equals the degree of the function field over the subfield generated by that function and the constants, and equals the sum of its pole orders.
Using both the integral closures of $Q[x]$ and $Q[x^{-1}]$ covers all places.
Lemmas 8.11–8.13 bound matrix torsion length by the sum of coefficient pole orders, which scales by the field-extension degree and does not increase under permutation substitution.
Corollary 8.14 bounds $[K(\alpha):Q(\alpha)]$ for nonconstant $\alpha$ causing a large rank drop.
The printed statement needs that qualification, as explained below.

Proposition 8.16 is a finite-fiber separation lemma on the algebraic curve.
For distinct functions of uniformly bounded extension degree and bounded degree as functions, at most $C(2C+1)$ underlying places can have only finitely many values along the whole sequence.
At many purported exceptional places, repeatedly selecting an infinite subsequence makes all the values agree at those places.
Two members of the subsequence then have too many common finite values, hence too many zeros of their difference; places with common infinite value are bounded by the number of poles.
The difference being a nonzero constant must be separated as a zero-free case, rather than assigned a field degree.

Section 8.8 first bounds the algebraic degree of every offending scalar over the coefficient field: all its Galois conjugates cause the same rank drop in the same finite matrix, so Proposition 5.10 bounds their number.
In the algebraic-number case an ultralimit rank chooses a finite family of integer shifts with small rank loss, and Corollary 8.8 bounds the shifted norms.
Proposition 8.15 gives a contradiction to infinitely many distinct scalars.
In the transcendental case Lemma 8.17 uses natural rank extension, restriction of scalars, and unramified specialization to find arbitrarily many places where specializing $B$ loses at most $\epsilon/4$ of rank.
Intersecting finitely many ultrafilter-large sets makes the corresponding loss at most $\epsilon/2$ for every chosen place and every retained finite representation.
Lemma 8.18 selects a place with infinitely many distinct finite reductions of the offending scalars, using Proposition 8.16 in the nonconstant case.
Finite-matrix rank cannot increase on specialization, so the reduced pencil retains a drop of at least $\epsilon/2$.
This contradicts the inductive strict-eigenvalue theorem over the algebraically closed constant field.
The argument is an induction on the finite transcendence degree needed by the finitely many original coefficients.

<a id="constant-function-defect"></a>
### Confirmed constant-function defects and their limited consequences

Lemma 8.9, printed p. 512, literally assumes only $0\ne\alpha\in K$ and asserts $[K:Q(\alpha)]=\sum_{v(\alpha)>0}v(\alpha)$.
Take $K=Q(x)$ and $\alpha=1$, with $Q$ algebraically closed.
The right side is zero and the left side is an infinite field-extension degree.
This is a confirmed false statement as printed, not an OCR artifact.
Its standard nonconstant form is the one required for the degree-of-function argument.

The field-degree conclusion of Corollary 8.14, printed p. 515, also fails for constants under its printed hypotheses.
Take $K=Q(x)$, $M_1=M_2=(1)$, $\alpha=d=1$, and an $F$-set consisting of one fixed point.
Then $m_2-m_1=1$, both coefficient-pole bounds in the numerator are zero, but $[K(\alpha):Q(\alpha)]=[Q(x):Q]$ is infinite.
Thus its field-degree conclusion must be restricted to $\alpha\notin Q$.
The displayed consequence in Lemma 8.11 and the use of field degree in Corollary 8.10 likewise require separating constant functions.
For example, $\alpha_1=x+1$ and $\alpha_2=x$ make their difference constant and invalidate Corollary 8.10 if interpreted literally with field-extension degrees.

These issues have a concrete local resolution at the proof interfaces actually used.
In Lemma 8.12 a nonzero constant minor has torsion degree zero, so the asserted upper bound is immediate without the nonconstant degree formula.
In Proposition 8.16 a nonzero constant difference has no zeros, so its contribution to the zero-count estimate is zero.
In Lemma 8.18, if infinitely many of the distinct $\lambda_j$ lie in the constant field $Q$, every valuation preserves those distinct values and the required conclusion is immediate.
Otherwise one discards the finitely many constant $\lambda_j$, and the corrected nonconstant form of Corollary 8.14 applies to the remaining infinite sequence.
These elementary case distinctions explain why the displayed counterexamples do not refute Theorem 8.1.
They are local audit explanations, not an assertion that the author has confirmed an erratum or that a separately reviewed corrected edition exists.

A bounded comparison with the [author manuscript](https://verso.mat.uam.es/~andrei.jaikin/preprints/sac.pdf), Lemmas 8.9–8.11 and Corollary 8.14, found the same unrestricted formulations.
No author correction was established by this comparison.

<a id="hilbert-schmidt-mechanism"></a>
## Hilbert–Schmidt centralizers and the transcendental obstruction

Section 9, pp. 521–529, supplies the analytic mechanism needed after the arithmetic finiteness theorem.

**Definition: affiliated Hilbert–Schmidt centralizer.**
For a Hilbert space $\mathcal H$, $HS(\mathcal H)$ consists of bounded operators $D$ with $\sum_b\|bD\|^2<\infty$ for an orthonormal basis, independently of that basis, and has inner product $\langle D,E\rangle_{HS}=\sum_b\langle bD,bE\rangle$.
For a free cocompact left $H$-set $X$, the Hilbert space of Hilbert–Schmidt operators on $\ell^2(X)$ is identified with $\ell^2(X\times X)$, with its $H\times H$-action.
In the source's right-operator convention the action is $v((g,h)\cdot D)=h((g^{-1}v)D)$.
If $A=B_1^{-1}C_1=C_2B_2^{-1}\in\mathcal U_H(\ell^2(X))$, where the $B_i,C_i$ are bounded and the $B_i$ are affiliated-invertible, the centralizer is

\[
C_{HS}(A)=\{D\in HS:C_1DB_2=B_1DC_2\}.
\]

This denominator-cleared definition is necessary because unrestricted products of an unbounded operator and a Hilbert–Schmidt operator need not be defined everywhere.
It is independent of the chosen left and right fractions.
Matrix versions use $HS(\ell^2(X)^n)=M_n(HS(\ell^2(X)))$.
Proposition 9.3 and Corollary 9.4 identify it with the kernel of the difference of the two tensor-coordinate actions, with the appropriate adjoint/conjugate convention on the first factor.
The Hilbert–Schmidt centralizer dimension is normalized by $|X|^2$ for a finite set $X$, not by $|X|$.

Proposition 9.5 uses the simultaneous product containing both $\mathcal U(G)$ and the finite matrix representations.
Its projection onto the affiliated coordinate is surjective on $*$-regular closures, and assumed approximation over $K$ extends to the whole closure by Corollary 6.2.
Proposition 9.6 then applies the same argument to $X_j\times X_j$, which approximates $G\times G$, to get convergence of normalized finite centralizer dimensions.
Here approximation over $K$ is assumed for the relevant sofic groups generally, including $G\times G$; approximation for a single unrelated group would not suffice.

Put $n_{\lambda,i}(A)=\dim_G\ker(A-\lambda)^i$, with $n_{\lambda,0}=0$, and $\Delta_{\lambda,i}=n_{\lambda,i+1}-n_{\lambda,i}$.
The finite-dimensional Jordan formula of Proposition 9.7 gives $\dim C(A)=\sum_{\lambda,i}\Delta_{\lambda,i}^2$.
One can see the formula directly by decomposing into Jordan blocks: the intertwiner space between two blocks of lengths $a,b$ has dimension $\min(a,b)$, and counting pairs of blocks of length greater than $i$ gives the square formula.
Proposition 9.11 bounds the omitted tail after keeping eigenvalues with geometric multiplicity at least $n/k$ and levels $i<k$ by $n^2/k$.
It uses the decreasing sequence $\Delta_{\lambda,i}$, its sum equal to the generalized-eigenspace dimension, and $\Delta_{\lambda,i}\leq n/(i+1)$.
Corollary 9.8 uses this same formula to show that a sufficiently large centralizer forces one eigenvalue with eigenspace dimension exceeding half the ambient dimension; uniqueness of that eigenvalue then forces it into the coefficient field by Galois invariance.

Proposition 9.9 claims the lower bound

\[
\dim_{G\times G}C_{HS}(A)
\geq\sum_{\lambda\in\sigma_p(A)}\sum_{i\geq0}\Delta_{\lambda,i}^2
\]

for arbitrary affiliated $A$.
The source uses bounded cutoffs in the successive generalized-kernel layers for $A$ and $A^*$, losing arbitrarily little von Neumann dimension.
The tensors

\[
w_j(v,u)=\sum_{i=0}^j
\delta_{v(A^*-\bar\lambda)^{j-i}}\otimes u(A-\lambda)^i
\]

commute with $A$ after applying the Hilbert–Schmidt identification.
The denominator-cleared calculation in Lemma 9.10(1) was checked term by term: the intermediate terms cancel, and the two end terms vanish by the generalized-kernel conditions.
The dimension argument needs bounded injectivity on the completed tensor source, rather than algebraic independence of elementary tensors alone.

<a id="lemma-910-2-completion"></a>
### Completion of the cutoff tensor argument

The full argument is retained in [Yin_C_A0002](../../../claims/Yin_C_A0002_v1.md#argument), with its exact statement and independent review selected at that fixed home.
It resolves the previously unverified affiliated weak-injectivity step, subject to the following explicit corrections of the printed formulation.

First, the parameters $\lambda_1,\ldots,\lambda_k$ must be pairwise distinct.
The source does not state this on p. 527.
If repeats are allowed, the formula fails already for the trivial group, a one-dimensional Hilbert space, $A=0$, two copies of $\lambda=0$ and upper level $1$: the left side is $1$, whereas the right side is $2$.
The distinct-parameter statement is exactly what Proposition 9.9 needs when summing over eigenvalues.

Second, the stated cutoff conditions do not ensure that powers of a vector stay in the sum of the chosen cutoff layers.
The completed proof takes the codomain to be the full Hilbert tensor product and then its closed image, without that unsupported invariance assumption.

The [explicit cutoff construction](../../../claims/Yin_C_A0002_v1.md#explicit-chain-cutoffs) intersects one generalized-kernel layer with the kernel of a bounded finite column of operators.
A spectral cutoff for $|A|$ controls every actual intermediate iterate, with dimension loss below $\varepsilon$.
Polar decomposition of the closed affiliated powers supplies the equality of the $A$ and $A^*$ layer dimensions used in equation (25).

For one spectral parameter, a bounded projection onto the highest remaining second-factor layer isolates an injective tensor map, giving descending elimination.
For distinct parameters, Chinese-remainder polynomials separate the finite nilpotent chains.
Each potentially unbounded polynomial is first multiplied on the left by a bounded injective denominator, so the separation identities extend to completed tensors as identities of bounded maps.
No unbounded operator is applied to an arbitrary tensor-completion vector.

The [dimension calculation](../../../claims/Yin_C_A0002_v1.md#dimension-equality-and-the-cutoff-limit) gives, for each fixed cutoff, the sum of the products of the two cutoff-layer dimensions.
The finite squeeze as $\varepsilon\downarrow0$ gives the printed square sum; nested cutoffs and closed ranges are unnecessary.
The [same proof](../../../claims/Yin_C_A0002_v1.md#centralizer-inclusion-and-amplification) verifies the denominator-cleared centralizer inclusion, Hilbert–Schmidt closure and unnormalized matrix amplification, yielding Proposition 9.9.
Its accepted spectral and Hilbert-module foundations remain explicit, and this completion does not independently re-audit the later coefficient-change assembly or every external input.

Theorem 9.12 assumes $K$ algebraically closed and approximation over $K$.
The strict eigenvalue theorem makes the set of eigenvalues with normalized multiplicity at least $1/k$ finite uniformly in the approximating matrices.
Proposition 9.5 gives convergence of the dimensions of their fixed generalized kernels.
The $n^2/k$ tail estimate permits passage from the finite centralizer formula to a sum over $\lambda\in K$.
Combining that upper bound with Proposition 9.9 excludes every eigenvalue outside $K$.
Corollary 9.13 translates the resulting full rank of $A-\lambda I$ into invertibility in the actual affiliated regular closure.
The line preceding equation (27), p. 529, says “for every” $\lambda\in\mathbb C$, but Proposition 9.5 at this induction stage justifies the assertion for $\lambda\in K$.
Only $\lambda$ in the finite set $S_{1/k}\subseteq K$ is used, so this overstatement can be removed without changing the argument.

<a id="base-change-proof"></a>
## Coefficient induction and the strong Atiyah deduction

Section 10.1 first proves algebraic extension of ranks.
For an ICC sofic group, Proposition 5.8 places $Z(\overline{\mathcal R}_{K[G]})$ inside $\mathbb C$.
Proposition 10.4 shows that a scalar in that center algebraic over $K$ already belongs to $K$.
Choose an element of $\mathcal R_{K[G]}$ within rank $1/5$ of the scalar.
Its annihilating polynomial has rank at most $1/5$, while Proposition 9.9 gives centralizer dimension at least $16/25$.
Finite approximation supplies a matrix with polynomial rank at most $1/4$ and centralizer dimension at least $3/5$ of the full square dimension.
Corollary 9.8 gives an eigenvalue $k\in K$ of multiplicity greater than one half.
The polynomial value at $k$ has rank at most $3/4$; being scalar, it must vanish.
Irreducibility of the original polynomial then forces degree one.

Theorem 10.2 embeds a group in a sofic ICC overgroup, invokes Proposition 7.12 on the rank completion, and identifies the rank after algebraic scalar extension by its uniqueness.
The source cites Hayes–Sale for the required sofic wreath-product closure.
The finite-group boundary requires first placing the finite group in an infinite sofic overgroup before using the stated ICC observation for the wreath product.
Corollary 10.3 applies this algebraic extension simultaneously to $G$ and all approximating $H_k$, and Proposition 7.13 commutes it with the ultralimit.

Theorem 10.5 handles a transcendental scalar $\lambda\notin Q$, with $Q$ algebraically closed and conjugation-stable.
Corollary 9.13 says $I_n+\lambda A$ has full rank for every $A\in M_n(\mathcal R_{Q[G]})$.
Proposition 7.7 therefore identifies the actual analytic rank on $Q(\lambda)[G]$ with the natural transcendental extension.
Corollary 10.6 applies the same identification to the approximating groups and uses Corollary 7.8.
Alternating algebraic closure and unit-circle transcendental generators maintains conjugation stability and covers the finitely many coefficients of any complex matrix.
The initial rational approximation result is external to the article and is identified below.
This closes Theorem 10.1 once the declared foundations and the affiliated centralizer lower bound are supplied.

Theorem 10.7, pp. 533–535, assumes $G$ countable and sofic, $d=\operatorname{lcm}(G)<\infty$, and strong Atiyah over $\overline{\mathbb Q}$.
It proves

\[
\mathcal R_{\overline{\mathbb Q}[G]}
\cong\bigoplus_{i=1}^k M_{n_i}(D_i),
\qquad
\mathcal R_{\mathbb C[G]}
\cong\bigoplus_{i=1}^k M_{n_i}\bigl(Q_l(D_i\otimes_{\overline{\mathbb Q}}\mathbb C)\bigr),
\]

where the $D_i$ and the indicated classical quotient rings are division rings.
Proposition 5.11 identifies the additive group generated by original matrix ranks with the group generated by ranks of regular-closure elements.
Discreteness in $d^{-1}\mathbb Z$ bounds the number of nonzero orthogonal idempotents by $d$.
Repeated splitting must therefore stop, and regularity gives a finite sum of simple left ideals; Artin–Wedderburn yields the first decomposition.

For a finitely generated field extension of $\overline{\mathbb Q}$, the scalar extension of this semisimple ring is Noetherian.
The proof cites the almost-simple-ring criterion in Jaikin-Zapirain [JAI99, Lemma 2.15] to establish semiprimeness and applies Goldie's theorem for its classical ring of fractions.
Rowen–Saltman [RS13, Lemma 1.1] supplies the absence of zero-divisors in each $D_i\otimes_{\overline{\mathbb Q}}L$.
Proposition 7.11 and the natural rank extensions then identify the actual $*$-regular envelopes through alternating transcendental and algebraic scalar extensions.
Epicity ensures that rank agreement on the group-ring matrices determines ranks throughout the extended regular ring.
Faithfulness makes the algebraic scalar-extension map into $\mathcal U(G)$ injective.
Directed unions give the complex extension.
The minimal idempotents in the corresponding matrix blocks have the same ranks, so the additive rank group remains $d^{-1}\mathbb Z$.
This gives Theorem 1.1; passing through finitely generated support removes countability from its statement.

For torsion-free $G$, the discrete bound is $d=1$, so the first semisimple ring is one division ring and the complex regular closure is its scalar-extension Ore division ring.
The premise is still the strong Atiyah property over $\overline{\mathbb Q}$, including all matrix sizes.
Scalar absence of zero-divisors alone does not supply that premise.

Section 10.4 also gives the strong algebraic-eigenvalue conclusion, scalar center conclusion for the rank completion, and independence of the field embedding in $\mathbb C$.
For the center statement, a scalar in the completion can be approximated within rank less than one by a regular-closure element.
If that scalar were transcendental over $K$, Corollary 1.5 would force the difference to have rank one, a contradiction; Proposition 10.4 then removes the algebraic extension.
For field-embedding independence, finite matrix rank is algebraic and unchanged by the embedding, and Theorem 1.3 passes this equality to the analytic limit.
These conclusions do not claim unrestricted determinant approximation for complex coefficients.

<a id="external-foundations"></a>
## External foundations and actual primary-source follow-up

The following distinctions are part of the proof audit, rather than a claim that every external source was re-audited.

| Input used by JZ19 | Exact source interface and inspection boundary |
| --- | --- |
| Regular-ring structure and rank completion | Proposition 3.1 cites Goodearl's regular-ring structure; Proposition 5.7 cites the second edition, Theorems 19.7, 19.13, and 19.14, for regular completion and the equivalence of field center, simplicity, and unique rank. Their formulations and uses in JZ19 were checked; the book's proofs were not inspected here. |
| Affiliated operators | Section 3.2 cites Berberian [BER82] and Reich [REI98] for the Ore localization and affiliated-ring foundation. Proposition 5.8 also cites Liu [LIU12, Proposition 30] for the center of the affiliated algebra. These are retained analytic foundations, not rederived constructions. |
| Ring epimorphisms and localization ranks | Stenström XI.1.2/XI.1.4 underlie Propositions 4.1–4.2; Schofield, Theorems 4.2 and 7.4, underlies Proposition 5.4; Malcolmson Lemma 2 underlies well-defined module rank in Proposition 5.2. JZ19's downstream algebraic arguments were reconstructed, but these original proofs were not read. |
| Extension from exact module rank to length | Proposition 5.6 cites [VIR17], an unnumbered 2017 preprint. The exact-rank condition and extension formulas are matched directly to Li21, arXiv:1901.07158v2, Corollary 4.3 and Lemma 3.8, as checked below. The historical identity of Vir17 remains unverified; this attribution limit does not leave the matched extension theorem without a readable source. |
| Entropy extension | Proposition 7.1 cites Virili [VIR17a, Theorem B], discussed below at statement-and-applicability depth. Its full external proof was not audited. |
| Dedekind and curve theory | Section 8.3 uses Narkiewicz, Chapter 1, including projectivity of finitely generated torsion-free modules and localization to discrete valuations. Lemma 8.9 cites Hartshorne II.6.9. The standard nonconstant degree formula, finite ramification, and valuation-extension identities are external foundations; the constant-function errors of JZ19 are separately demonstrated above. |
| Hilbert-module dimension | Proposition 9.1 cites Lück, Theorem 1.12, for additivity in weakly exact Hilbert-module sequences. The finite Jordan centralizer formula cited to Collingwood–McGovern, Theorem 6.13, was also reconstructed directly from Jordan blocks. The affiliated cutoff/weak-injectivity step has the separately reviewed completion linked above; the original general dimension foundations remain accepted inputs. |
| Sofic closure and the rational starting case | The group-theoretic closure needed to embed in a sofic ICC group is cited to Hayes–Sale. The rational/general approximation starting case is identified in the author's survey below; it is not a consequence of JZ19's later complex approximation theorem. |
| Scalar-extension quotient rings | Theorem 10.7 uses Goldie's theorem, Hilbert basis, Artin–Wedderburn, [JAI99, Lemma 2.15], and [RS13, Lemma 1.1]. The Rowen–Saltman lemma and proof were checked in the primary preprint below. JZ99 Lemma 2.15 and its density-theorem proof have also been checked in the journal original against the simple factors in Theorem 10.7. |

In [Virili, arXiv:1410.8306v2](https://arxiv.org/pdf/1410.8306v2), Theorem B on PDF p. 4 states that entropy is a length function for a compatible length on an amenable crossed product, with the specified value on induced modules.
The inspected version is retained as the [local Vir19 arXiv v2 original](../../../literature/pdf/Vir19--arxiv-v2.pdf#page=4).
Taking the trivial $\mathbb Z$-action on $U$, the crossed product is $U[t^{\pm1}]$; compatibility is automatic, and every finitely generated $U$-submodule has finite dimension because $\dim_U U=1$.
This checks the domain and normalization needed by JZ19 Proposition 7.1.
The full proof in Virili Section 4 was not inspected.

The author's [survey manuscript](https://matematicas.uam.es/~andrei.jaikin/preprints/surveyl2.pdf), Corollary 10.11 on manuscript p. 39, gives the precise general approximation statement over $\overline{\mathbb Q}$ with sofic $H_k$.
Its Sections 10.2–10.4 were inspected for the rational base-case mechanism: local convergence gives convergence of spectral moments, integral finite matrices have nonzero spectral product at least one, and this determinant bound makes the small positive spectral mass uniformly vanish near zero.
The rational specialization supplies the starting case without invoking the later complex base-change argument.
The subsequently acquired [local author manuscript of JZ19b](../../../literature/pdf/JZ19b--author.pdf#page=34), PDF pp. 34–39, was also inspected through Corollary 10.11.
These local passages reproduce the numbered statements and the determinant-to-kernel mechanism recorded from the earlier UAM access.
This is a comparison of the selected mathematical passages, not a claim of byte identity or a comparison of the complete editions; the local file was acquired separately from the author's WordPress site.
The survey's complete proof and historical original papers were not fully audited here.

In [Rowen–Saltman, arXiv:1106.5517v1](https://arxiv.org/pdf/1106.5517v1), Lemma 1.1 and its following qualification on PDF pp. 3–4 were read directly.
Over an algebraically closed central base field $F$, a field extension $L$ tensored with an $F$-domain has no zero-divisors.
The proof writes two purported zero-divisors with linearly independent coefficients in the domain and specializes the finitely generated commutative coefficient field at an $F$-point where both finite coefficient families remain nonzero.
Their product would then be zero in the original domain, a contradiction.
The authors explicitly remove finite-dimensionality over the center and finite generation of the field extension, matching the $D_i\otimes_{\overline{\mathbb Q}}L$ use in JZ19.
The inspected version is retained as the [local RS13 arXiv v1 original](../../../literature/pdf/RS13--arxiv-v1.pdf#page=3).
Only this Rowen–Saltman lemma and its proof were audited, and the journal version was not separately compared.

<a id="jz99-lemma-215"></a>
### JZ99 Lemma 2.15 and the scalar-extension application

The [JZ99 journal original](../JZ99/readme.md) is the article cited as JAI99 by JZ19.
The definition on printed p. 116, PDF p. 3, calls a ring \(A\) almost simple when every nonzero two-sided ideal has nonzero intersection with \(Z(A)\).
Lemma 2.15 on printed pp. 125–126, PDF pp. 12–13, states that a finite tensor product of simple rings over a common central subring is almost simple.
The statement and the complete displayed two-factor proof were read, and the lemma pages were visually checked.
The proof applies the density theorem to isolate one coefficient over the first center and then does the same for the second factor, producing a nonzero central element in the ideal generated by the original nonzero tensor.
The density theorem itself and the remainder of JZ99 were not audited.

In JZ19 Theorem 10.7(2), apply the lemma to each simple ring \(M_{n_i}(D_i)\) and the extension field \(K\) over the common central field \(\overline{\mathbb Q}\).
The finite product of these scalar-extended components has the same ideal-intersection property, so simplicity is required of the components rather than of the entire initial semisimple ring.
The lemma establishes almost simplicity, not semiprimeness by itself.
JZ19 separately uses that the center is semiprime: a nonzero nilpotent ideal would meet that center in a nonzero nilpotent element.
The independently checked RS13 domain input for each \(D_i\otimes_{\overline{\mathbb Q}}K\) also retains its separate role in identifying division-ring quotient components.
The JZ99 statement and this direct componentwise specialization are accepted for the cited scalar-extension step, without claiming a new proof of the density or Goldie theorems.

<a id="exact-rank-to-length"></a>
### A readable source for the exact-rank extension

JZ19 Section 5.5, printed pp. 485–486, defines an exact Sylvester module rank \(d\) by the additional requirement

\[
d(M)-d(N)=\inf\{d(L):L\twoheadrightarrow\ker\phi,\ L\text{ finitely presented}\}
\]

for every surjection \(\phi:M\twoheadrightarrow N\) of finitely presented left \(R\)-modules.
A normalized length function on a unital ring \(R\) is an isomorphism-invariant map from left \(R\)-modules to \([0,+\infty]\), vanishing at zero, taking value one at \(R\), additive on all short exact sequences, and satisfying \(d(M)=\sup_{L\le M,\ L\text{ finitely generated}}d(L)\).
Proposition 5.6 specifies the infimum over finitely presented covers for finitely generated modules and then the supremum over finitely generated submodules for arbitrary modules.

The [Li21 arXiv v2 original](../Li21/readme.md), Theorem 3.3 on p. 6, Lemma 3.8 on pp. 7–8 and Definition 4.1 through Corollary 4.3 on pp. 16–17, gives the same exactness condition, extension formulas and normalization.
These statements were compared directly with JZ19 Section 5.5; the relevant pages and formulas were visually checked.
Corollary 4.3 states that precisely this exactness condition is equivalent to extension to a unique normalized length function.
Lemma 3.8 identifies the finitely generated value with the infimum over finitely presented covers, and Definition 4.1 supplies the supremum formula and additivity on arbitrary short exact sequences.
The proof of Proposition 4.2 was read for the passage from relative rank to an ordinary length function; the full proof of the general bivariant extension theorem in Section 3 was not audited.
These identified established statements are accepted as a readable alternative source for Proposition 5.6's extension theorem, with the exactness hypothesis retained.
No extension of an arbitrary nonexact Sylvester rank to an additive length function is inferred.

Li21 attributes Corollary 4.3 to the published article registered as [Vir19b](../Vir19b/readme.md), not to the distinct entropy paper Vir19.
The publisher metadata identifies Vir19b, but its PDF endpoints did not yield a readable article in this search.
The exact title *Crawley-Boewey's extension of invariants in the non-discrete case* was found only as the unnumbered 2017 citation in other primary papers, not as an accessible original.
Neither Vir19b nor Vir19 is identified with Vir17 without documentary evidence.
The remaining follow-up is the historical citation's exact identity or a documented title change; the extension statement itself now has the explicitly matched Li21 source above.
These supplements record scoped literature checks and do not enlarge the earlier independent-review relationship or assert complete audits of the newly consulted articles.

<a id="affiliated-and-schur-applicability"></a>
## Applicability to the actual affiliated rational closure and Schur complements

The usable mechanism is rank preservation in the actual affiliated representation, followed by the canonical $*$-regular-envelope theorem.
JZ19 does not replace that representation by an abstract division ring and then infer its analytic rank.
Sofic approximation enters precisely where finite permutation ranks and centralizer dimensions must recover the affiliated ranks, including on the product group.
The strict eigenvalue theorem is uniform over finite permutation representations, but it becomes a statement about $\mathcal U(G)$ only through those approximation steps.

The finite block formula of Proposition 5.11 and Corollary 6.2 is directly useful for comparing ranks of rational expressions after adjoining relative inverses.
It expresses a new rank as a difference of ranks of matrices over the original ring.
It does not itself show that these ranks are integers or that all nonzero elements of the closure have full rank.
Those conclusions require the original integer-rank premise, or another argument establishing it, together with the faithful actual affiliated rank.

The ordinary Schur-complement identities and their domain requirements are already retained in the [MSY23 representation audit](../MSY23/Yin_U003.md#msy23-u003).
They can transfer a verified rank or invertibility assertion between a rational expression and a larger block matrix once the denominator block is actually invertible in $\mathcal U(G)$.
JZ19's natural-extension proof uses closely related block linearizations in Proposition 7.7, but its substantive new input is the full-rank assertion $I+tA$ for all matrices over the regular envelope.
That assertion comes from the sofic centralizer/eigenvalue argument, not from the formal block manipulation.

Under Theorem 10.7's torsion-free hypotheses, the actual $*$-regular closure is a division ring, so rational and division-closure comparisons may be made using their established fixed-ambient implications.
Without the $\overline{\mathbb Q}$-Atiyah premise, Theorem 1.3 gives rank approximation but no integer-value restriction on its limits.
Without soficity, this article supplies no replacement for the finite-to-affiliated rank interface.
Consequently it provides a powerful conditional coefficient-change and closure-identification mechanism, but no unconditional proof for all torsion-free complex group algebras.
