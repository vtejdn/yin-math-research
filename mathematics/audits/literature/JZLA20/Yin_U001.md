---
author: Yin
---
# Yin: JZLA20, rational complexity, Hughes freeness, and the analytic division ring

<a id="jzla20-u001"></a>
## Inspected object and conclusion

The object is [arXiv:1810.12135v4, 11 November 2019](readme.md#arxiv-v4), including all 47 pages, Sections 1–8, and the references.
The inspection was performed on 10 November 2026.
All on-page mathematical arguments were read and their logical interfaces reconstructed, including the three cases of Proposition 5.1, the simultaneous inductions in Propositions 7.9 and 8.4, and the finite-index reduction in Theorem 7.1.
The suspected formulas and statements on printed pages 28–30, 33, 41 and 45 were also checked directly against rendered PDF pages.
The review was separately organized from the repository's mathematical proof development; no project proof, exploration notes or proof-generation discussion was supplied or consulted.
The parallel inspection of JZ19 was consulted afterward for the cited primary-source interfaces identified below.
This is source evidence, not a review of a project Claim or an adoption of these results by a project argument.

The main conclusion is that the source establishes the strong Atiyah conjecture over the complex numbers for locally indicable groups and marked-group Lück approximation for virtually locally indicable groups.
The proof constructs the actual analytic division ring through a Hughes-free rank envelope; it does not start by assuming integer-valued ranks on all group-ring matrices.
Its rational-expression complexity is a well-order on finite rooted trees, minimized over formal representations, rather than a bound on matrix size or a syntactic count of inverse symbols.
Local indicability enters exactly where the finitely generated source subgroup of a minimal rational expression must admit a quotient onto the infinite cyclic group.
The source does not supply that step for arbitrary torsion-free groups.

No remaining defect was found in the principal deductions after the explicit elementary clarifications recorded in [the correction section](#source-corrections).
This conclusion accepts the accurately stated foundational inputs listed in [the dependency boundary](#external-foundations); their original proofs were not all re-audited here.
In particular, whole-paper reading and reconstruction are not a claim to have reconstructed the proofs of every cited paper, the combinatorial source-subgroup theorem, or all of the background on regular rings and length functions.
No associated formal proof code was inspected.

<a id="rank-and-closures"></a>
## Rank, regular envelopes, and the three closure operations

**Definitions and conventions, Sections 1.1 and 2, pp. 1–11.**
For a countable group $G$, a closed left $G$-invariant subspace $V\subseteq\ell^2(G)^n$ has dimension $\dim_G V=\sum_{i=1}^n\langle\operatorname{proj}_V(1_i),1_i\rangle$.
For $A\in M_{n\times m}(\mathbb C[G])$, right multiplication gives $\phi_A:\ell^2(G)^n\to\ell^2(G)^m$, and $\operatorname{rk}_G(A)=n-\dim_G\ker\phi_A$.
The image in the corresponding image-dimension formula is understood with closure.
For arbitrary $G$, the rank is computed in a finitely generated subgroup containing the finite support of the entries; the subgroup embedding preserves this rank.
If finite-subgroup orders have a finite least common multiple $\operatorname{lcm}(G)$, the strong Atiyah conjecture over $K\subseteq\mathbb C$ asserts $\operatorname{rk}_G(A)\in\operatorname{lcm}(G)^{-1}\mathbb Z$ for every finite matrix over $K[G]$.
For torsion-free $G$, this is an assertion about all matrix sizes with integer normalization, not merely about scalar group-ring elements.

A ring $U$ is von Neumann regular if every $x\in U$ admits $y\in U$ with $xyx=x$.
A proper involution satisfies $x^*x=0\Rightarrow x=0$; a regular ring with such an involution is a $*$-regular ring.
The source calls it positive definite when $M_n(U)$ is $*$-regular for every positive integer $n$.
For $x$ in a $*$-regular ring, the relative inverse $x^{[-1]}$ is characterized by $xx^{[-1]}x=x$, $x^{[-1]}xx^{[-1]}=x^{[-1]}$, and the requirement that $\operatorname{LP}(x)=xx^{[-1]}$ and $\operatorname{RP}(x)=x^{[-1]}x$ are self-adjoint idempotents.
The $*$-regular closure $\mathcal R(R,U)$ of a $*$-subring $R\subseteq U$ is the smallest $*$-regular subring containing it; Proposition 2.2 constructs it by adjoining relative inverses repeatedly.
When $K\subseteq\mathbb C$ is closed under conjugation, $K[G]$ has $(\lambda g)^*=\bar\lambda g^{-1}$ and the source writes $\mathcal R_{K[G]}=\mathcal R(K[G],\mathcal U(G))$.
Here $\mathcal U(G)$ is the algebra of operators affiliated with the group von Neumann algebra; it is positive definite $*$-regular and its faithful rank extends $\operatorname{rk}_G$.
For an uncountable group the source uses the directed union over finitely generated subgroups.

The general fixed-ambient division and rational closure conventions already have a [responsible definition home](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra).
In JZLA20 Section 4.3, $\mathcal D_{R,S}$ denotes the division closure of $R\subseteq S$: start with $R$, repeatedly adjoin inverses of elements that are invertible in $S$, and take the union of the resulting subrings.
Thus $\mathcal D_{R,S}$ need not itself be a division ring.
For a crossed-product map $E*G\to S$, $\mathcal D_{H,S}$ abbreviates the division closure of the image of $E*H$ in $S$.
JZLA20's calligraphic $\mathcal R_{K[G]}$ denotes a $*$-regular closure, not matrix rational closure.
In a general ambient ring these closure operations must not be identified by notation alone.

Lemma 4.5, p. 23, is a decisive ambient-independence statement with an explicit regularity hypothesis.
If $T\subseteq R\subseteq S$, then $\mathcal D_{T,S}=\mathcal D_{T,\mathcal D_{R,S}}\subseteq\mathcal D_{R,S}$.
If a regular subring $U\subseteq S$ contains $R$, then $\mathcal D_{R,S}=\mathcal D_{R,U}$.
To check the second assertion, if $x\in U$ is invertible in $S$ and $xyx=x$ in $U$, multiplication by the ambient inverse gives $yx=xy=1$; consequently the inverse already belongs to $U$.
The repeated-inversion construction then gives equality of the division closures.
The source repeatedly uses this fact to move a closure between two larger ambient rings through their common regular subring.

**Definition of Sylvester rank and its envelopes, Section 2.4, pp. 8–11.**
A Sylvester matrix rank $r$ assigns a nonnegative real number to every finite rectangular matrix over a unital ring $R$, with $r(0)=0$, $r(1)=1$, $r(AB)\leq\min\{r(A),r(B)\}$, additivity on block diagonal matrices, and $r(\begin{smallmatrix}A&C\\0&B\end{smallmatrix})\geq r(A)+r(B)$.
The associated rank of a finitely presented left module $M=R^m/R^nA$ is $\dim_r M=m-r(A)$; Proposition 2.6 states that this is well-defined and gives the usual bijection with Sylvester module ranks.
The ideal $\ker r=\{a\in R:r(a)=0\}$ vanishes when the rank is faithful.
An envelope of a rank on $R$ is a homomorphism $\phi:R\to S$ together with a faithful rank $r_S$ whose pullback is the given rank.
A homomorphism is epic when it is right cancellable against maps to every ring; Proposition 2.3 gives the equivalent multiplication isomorphism $S\otimes_R S\to S$.
For a $*$-map into a $*$-regular ring, Proposition 2.4 identifies epicness with generation by $*$-regular closure.
A regular rank admits a regular envelope, and a $*$-regular rank admits a $*$-regular envelope through a $*$-map.
The source takes its $*$-regular envelopes to have faithful rank and epic structure map.
An integer-valued rank has an epic division envelope by the cited Malcolmson theorem.
The sets of all ranks, regular ranks, $*$-regular ranks and integer-valued ranks are denoted $\mathbb P(R)$, $\mathbb P_{\rm reg}(R)$, $\mathbb P_{*\rm reg}(R)$ and $\mathbb P_{\rm div}(R)$, respectively.

Lemma 2.7 checks that a square matrix over a regular ring with faithful rank is invertible exactly when its rank is its size.
The proof reduces to $xyx=x$ and faithfulness for the scalar normalized rank, then applies this to the regular matrix ring with rank divided by its size.
This assertion requires regularity and faithfulness; full rank alone in an arbitrary ring does not supply an inverse.
Theorem 2.8 identifies epic division envelopes by all matrix ranks on the original ring.
Theorem 2.9 is the $*$-regular counterpart and identifies rank-preserving $*$-envelopes, not arbitrary abstract regular envelopes.
The distinction is used in Section 3 when passing from agreement of ranks to an embedding of the actual analytical envelope.

<a id="natural-extensions"></a>
## Natural extensions and the common regular ambient ring

**Definitions, Sections 3.1–3.2, pp. 11–17.**
Given an automorphism $\tau$ of $R$, use $ta=\tau(a)t$ for $R[t;\tau]$, its Laurent version $R[t^{\pm1};\tau]$, and formal series $R[[t;\tau]]$ and $R((t;\tau))$ with exponents bounded below.
A rank $r$ is $\tau$-compatible if $r(\tau(A))=r(A)$ for every matrix.
For the associated module rank, Lemma 3.1 identifies this with $\dim_r(tM)=\dim_r(M)$, where the left action on the twist is $a(tm)=t(\tau^{-1}(a)m)$.
For $A$ over $R[t;\tau]$, let $\phi_{A,n}$ be right multiplication on the corresponding finite sums of $R[t;\tau]/R[t;\tau]t^n$.
The normalized truncated rank is $\widetilde r_n(A)=r(\phi_{A,n})/n$.
The natural extension is the pointwise limit $\widetilde r(A)=\lim_{n\to\infty}\widetilde r_n(A)$ when it exists.
It has $\widetilde r(t)=1$, and the source extends it to the Laurent ring using full-rank localization.

A Sylvester module rank is exact if for every surjection of finitely presented modules $M\twoheadrightarrow N$ the difference $\dim M-\dim N$ is the infimum of $\dim L$ over finitely presented modules mapping onto its kernel.
A normalized length function on all modules has value one on $R$, is additive on short exact sequences, and is the supremum of its values on finitely generated submodules.
Proposition 3.2, attributed to Virili, extends exact module rank to length by an infimum over finitely presented covers followed by this supremum.
On a regular ring finitely presented modules are projective, giving the required exactness.
Proposition 3.3 uses the entropy limit

\[
E_{M,N}=\lim_{j\to\infty}\frac{\dim(N+tN+\cdots+t^{j-1}N)}{j},\qquad
\widetilde{\dim}(M)=\sup_{\dim N<\infty}E_{M,N},
\]

to obtain the normalized length on the skew Laurent ring and identify its matrix rank with the truncated-rank limit.
The existence and length-function assertions are cited foundational input; this paper does not reproduce their full proof.

Proposition 3.4 identifies the length of a left ideal with the asymptotic lengths of its bounded-degree polynomial portions.
For regular coefficients it also equals the supremum of the ranks of constant coefficients of polynomials in the ideal.
Proposition 3.5 characterizes the natural extension on a regular coefficient ring by $r'(I_n+At)=n$ for every $A\in M_n(U)$, among ranks restricting to the specified rank on $U$.
These are the stated skew analogues of results from JZ19, with their original proofs referred to there rather than printed in full.
The paper does not claim natural extensions exist for every rank on every coefficient ring.

For positive definite $*$-regular $U$ and a rank-preserving $*$-automorphism $\tau$, equations (3)–(5) construct

\[
\mathcal P_{\omega,\tau}^{U}
=\left(\prod_{n\geq1}\operatorname{End}_U(U[t;\tau]/U[t;\tau]t^n)\right)/\ker r_\omega,
\quad
r_\omega=\lim_\omega r_n,
\quad r_n=\frac{r}{n},
\]

for a nonprincipal ultrafilter $\omega$.
Positive definiteness makes every matrix factor $*$-regular, and the rank-zero ideal quotient has a faithful rank.
Truncated multiplication gives a homomorphism from $U[t;\tau]$; the image of $t$ has rank one and is invertible by Lemma 2.7.
The Laurent-polynomial map is a $*$-map when $t^*=t^{-1}$, since the finite shift and its adjoint differ from mutual inverses only at the truncation boundary, of normalized rank tending to zero.
For a nonzero formal Taylor series $p=a_it^i+a_{i+1}t^{i+1}+\cdots$ with $i\geq0$, its truncated matrix has rank at least $(n-i)r(a_i)$ for sufficiently large $n$.
Consequently $r_\omega(p)\geq r(a_i)>0$ and the Taylor-series map is injective; inverting the image of $t$ then gives the injective formal Laurent-series ring map.
An involution on all these formal Laurent series is not part of that construction; see [the wording correction](#source-corrections).

Proposition 3.7 extends $\tau$ from $R$ to its epic $*$-regular envelope by Theorem 2.9, since the two structure maps induce the same rank.
It then constructs the natural extension upstairs and pulls it back; positive definiteness is required for the additional $*$-regular conclusion.
Corollary 3.8 checks commutation of natural extension with ultralimits by passing to a product of envelopes and using the $I_n+At$ criterion.
Proposition 3.9 makes the corresponding argument for integer-valued ranks using Theorem 2.8, and identifies the new epic division envelope with the Ore field $D(t;\tau)$.
Here the leading coefficient of a nonzero skew polynomial has division-ring rank one, so the localization to $D(t;\tau)$ preserves rank.

For $H=N\rtimes\langle t\rangle$, write $U_H$ and $U_N$ for the $*$-regular closures of the group subrings in an epic positive definite envelope $U$.
If the rank on $K[H]$ is the natural extension of its restriction to $K[N]$, Theorem 2.9 identifies $U_H$ with the $*$-regular closure of the image of $K[H]$ in $\mathcal P_{\omega,\tau}^{U_N}$.
Thus equation (7), pp. 17–18, places $U_H$ and $U_N((t;\tau))$ in one common ambient ring with the original embeddings of $K[H]$ agreeing.
This is a substantive analytic-algebraic interface, not a consequence of formal Laurent notation alone.

<a id="hughes-free"></a>
## Local indicability, crossed products, and Hughes freeness

**Definitions, Sections 1.1 and 3.3, pp. 2 and 18–19.**
A group is indicable if it is trivial or maps onto $\mathbb Z$, and is locally indicable if every finitely generated subgroup is indicable.
A nontrivial finitely generated subgroup $H$ of a locally indicable group therefore has $N\lhd H$ and a lift $t$ with $H=N\rtimes\langle t\rangle$ and $H/N\cong\mathbb Z$.
Local indicability implies torsion-freeness, but the source's proofs require the actual cyclic quotients and not just this consequence.

A crossed product $E*G$ of a division ring $E$ and a group $G$ is a $G$-graded ring with degree-identity part $E$ and an invertible element $u_g$ in each homogeneous part.
The homogeneous units $E^\times G=\{a u_g:a\in E^\times,g\in G\}$ form a group with normal subgroup $E^\times$ and quotient $G$.
For a group ring this is $\{ag:a\in E^\times,g\in G\}$; for a general crossed product the chosen homogeneous lifts need not form a copy of $G$.
The use of $E^\times G$ in the rational syntax retains the twisting data.

An epic division $E*G$-ring $(D,\phi)$ is Hughes-free if, for every nontrivial finitely generated $H\leq G$ and every $N\lhd H$ with $H/N\cong\mathbb Z$, its division closure $D_H$ is the Ore field of $D_N[t^{\pm1};\tau]$ as an $E*H$-ring.
Here $D_N$ is the division closure of $\phi(E*N)$, $t$ is a homogeneous lift of a quotient generator, and $\tau$ is conjugation by its image.
Equivalently, the nonnegative powers of that image are left linearly independent over $D_N$; this linear-independence condition is substantive and is not automatic for an arbitrary division-ring embedding.
The source notes that a Hughes-free map is injective.
A Sylvester rank on $E*G$ is Hughes-free if for every such pair $(H,N)$ its restriction to $E*H$ equals the natural extension of its restriction to $E*N$.
Lemma 3.10 checks the equivalence of these two formulations for epic division rings by Proposition 3.9 and uniqueness of epic division envelopes.

Proposition 3.11 is the essential analytic input: for any group $G$, any subfield $K\subseteq\mathbb C$, and any finitely generated indicable subgroup $H$ with $N\lhd H$ and $H/N\cong\mathbb Z$, the von Neumann rank on $K[H]$ is the natural extension of the rank on $K[N]$.
The proof is cited to [19, Corollary 12.2] in the paper, rather than derived there.
For a locally indicable group this verifies Hughes freeness of the actual analytical rank on every required subgroup.
For a general torsion-free group it remains true on the indicable subgroups to which it applies, but that does not supply the missing quotient for every finitely generated source subgroup.

<a id="rational-complexity"></a>
## The actual rational-expression complexity

**Definitions, Section 4, pp. 19–25.**
For a multiplicative group $V$, use the multiplicative-action convention of the source's cited [5, Definition 4.1]: a $V$-semiring has a unital multiplicative map $V\to R$ and the induced left and right actions.
Its addition is commutative and associative, its multiplication is associative, unital and distributive, and an additive zero is not required.
A rational $V$-semiring additionally has an operation $r\mapsto r^\diamond$ satisfying $(urv)^\diamond=v^{-1}r^\diamond u^{-1}$.
JZLA20 expresses the action condition in terms of a $V$-biset; the multiplicative-action convention makes the compatibility used by its universal construction explicit.
Morphisms preserve addition, multiplication, the multiplicative identity, the group actions, and $\diamond$.
The universal rational $V$-semiring $\operatorname{Rat}(V)$ consists of formal nonempty sums of formal products built from $V$ and successively introduced formal rational-operation symbols, with the balancing relation that a group factor can be moved between adjacent factors.
More precisely, for a $V$-biset $X$, $V\natural X$ is the union of balanced words $X^{\times_V n}$, with its length-zero part $V$.
Write $X^\diamond$ for a disjoint copy with $u x^\diamond v=(v^{-1}xu^{-1})^\diamond$.
Start with $X_0=\varnothing$ and $X_1=(\mathbb N[V]\setminus\{0\})^\diamond$; then

\[
X_{n+1}=\bigl(\mathbb N[V\natural X_n]\setminus\mathbb N[V\natural X_{n-1}]\bigr)^\diamond\cup X_n,
\quad X=\bigcup_nX_n,
\quad\operatorname{Rat}(V)=\mathbb N[V\natural X]\setminus\{0\}.
\]

Lemma 4.2 gives the unique rational-semiring morphism from $\operatorname{Rat}(V)$ to any rational $V$-semiring.
The formal object does not impose coefficient-addition identities from the evaluated ring or the identities of a division ring.
In particular, distinct formal expressions can evaluate to the same element or to zero.

Let $\mathcal T$ be the finite rooted trees up to isomorphism.
Its zero $0_{\mathcal T}$ is the one-vertex tree; $\exp(T)$ adjoins a root and one edge above $T$, and $1_{\mathcal T}=\exp(0_{\mathcal T})$.
Addition identifies roots, and multiplication is $XY=\sum_{X'\in\operatorname{fam}(X),\,Y'\in\operatorname{fam}(Y)}\exp(X'+Y')$, where $\operatorname{fam}$ records the subtrees below the root with multiplicity.
The rational operation is $T^\diamond=\exp^2(T)$ and the group action is trivial.
The ordering compares the largest child subtree recursively, then deletes equal largest children and continues; the zero tree is least.
The cited combinatorial results assert that this is a well-order and that the additive and multiplicative strictness properties in Lemma 4.1 hold.
The universal map $\operatorname{Tree}:\operatorname{Rat}(V)\cup\{0\}\to\mathcal T$ assigns the formal complexity.
On nonzero expressions it preserves addition, multiplication and the rational operation, while an adjoined formal zero maps to $0_{\mathcal T}$.
If $\log(T)$ denotes the largest child subtree, the proof uses in particular the formulas for $\log\operatorname{Tree}(\alpha\beta)$ and $\log^2\operatorname{Tree}(\alpha\beta)$ in Lemma 4.3, and the fact that the tree of a single formal word has width one.
Those facts control products and inverse-series coefficients even when their ordinary expression lengths grow.

For a crossed-product map into an arbitrary ring $S$, endow $\mathcal D_{H,S}$ with $a^\diamond=a^{-1}$ if $a$ is invertible, and $a^\diamond=0$ otherwise.
This total operation is essential: a noninvertible evaluation does not leave the formal map undefined.
The universal evaluation $\Phi_{H,S}:\operatorname{Rat}(E^\times H)\cup\{0\}\twoheadrightarrow\mathcal D_{H,S}$ is surjective.
Define

\[
\operatorname{Tree}_H(a)=\min\{\operatorname{Tree}(\alpha):\Phi_{H,S}(\alpha)=a\}.
\]

The well-order gives the minimum, and $\operatorname{Tree}_G(a)\leq\operatorname{Tree}_H(a)$ for $H\leq G$.
An isomorphism of the corresponding crossed-product division closures preserves their rational operation and this minimum complexity.
The induction therefore concerns minimal semantic complexity in a specified ambient realization, not the complexity of an arbitrarily chosen expression.

Theorem 4.4 supplies a finitely generated subgroup $\operatorname{source}(\alpha)\leq V$, with $\alpha\in\operatorname{Rat}(\operatorname{source}(\alpha))V$.
It is the least subgroup $W$ for which $\alpha\in\operatorname{Rat}(W)V$, in the sense that it lies in every such $W$.
An expression is primitive when it already lies in $\operatorname{Rat}(\operatorname{source}(\alpha))$.
Every expression becomes primitive after multiplication by a group unit, without changing the source subgroup or its complexity.
Existence of this source and the tree properties are cited to Dicks–Herbera–Sánchez and Sánchez, rather than proved in JZLA20.
Their exact stated interfaces suffice for the inductions below; this inspection does not claim to have reconstructed those external combinatorial proofs.

Section 4.4 supplies a separate rational structure on an epic $*$-regular $K[G]$-ring using relative inverses.
Lemma 4.6 checks $(uxv)^{[-1]}=v^{-1}x^{[-1]}u^{-1}$ for $u,v\in K^\times G$ by conjugating the support projections; centrality of $K$ follows from Lemma 2.5.
The text expressly states that this relative-inverse version is not used in the present proof of the Atiyah theorem.
The main induction uses scalar division closure with inverse-or-zero evaluation from Section 4.3.

<a id="key-induction"></a>
## Proposition 5.1 and the strictly decreasing coefficients

The setting on pp. 25–26 is a finitely generated group $H$ with $H/N\cong\mathbb Z$, a crossed product $E*H=(E*N)[t^{\pm1};\tau]$, a regular $E*N$-ring $A$ with a compatible extension of $\tau$, and a ring $\mathcal P$ containing $A((t;\tau))$.
The induced crossed-product map defines $\mathcal D_{N,\mathcal P}$ and $\mathcal D_{H,\mathcal P}$.
By regularity of $A$, $\mathcal D_{N,\mathcal P}=\mathcal D_{N,A}$; conjugation preserves this division closure, so its skew Laurent-series ring is meaningful.
Fix $a\in\mathcal D_{H,\mathcal P}$ and assume every nonzero element of strictly smaller $H$-complexity is invertible in that division closure.
Proposition 5.1 proves that each $b$ of complexity at most that of $a$ lies in $\mathcal D_{N,\mathcal P}((t;\tau))$ and has homogeneous summands $b_k\in\mathcal D_{N,\mathcal P}t^k$ satisfying $\operatorname{Tree}_H(b_k)\leq\operatorname{Tree}_H(b)$.
For $b\ne0$, equality for some $k$ occurs exactly in the exceptional case where $b=b_k$ and every complexity-minimizing expression for $b$ belongs to $\operatorname{Rat}(E^\times N)t^k$.
Both the conclusion about all minimizing expressions and the equality characterization are needed later.

The proof is a subsidiary induction on $\operatorname{Tree}_H(b)$ and splits a minimizing expression into three possible forms after the unit case.
For a product of two nonunit formal words, both factors have smaller complexity, and minimality of the product forces the chosen factors to be minimal for their evaluations.
Each coefficient is a finite convolution of earlier coefficients, since the series have a common lower bound on exponents.
Taking $\log$ bounds its complexity by the sum of the two leading subtree complexities.
If equality occurs, the width-one property of each word forces equality in the coefficient complexities for both factors, and the inner induction makes both factors homogeneous monomials.
Their product and its original formal expression are then homogeneous in the same quotient degree.

For a nontrivial sum, strictness of tree addition again forces minimality of each summand.
The corresponding coefficient is the sum of two coefficients, so its complexity is bounded by the sum of their trees.
Equality forces equality for both components, and the inner induction makes them monomials of the same degree.
This gives the claimed monomial conclusion also for the original sum expression.

For $\beta=\gamma^\diamond$ with nonzero evaluation $b$, the evaluation $c=\Phi(\gamma)$ is invertible and $b=c^{-1}$.
Minimality forces $\gamma$ to realize the complexity of $c$, which is strictly below that of $b$.
The inner induction expands $c=\sum c_k$, and the outer invertibility hypothesis makes every nonzero homogeneous term invertible.
For its leading term $c_\ell$, the coefficient $c_\ell t^{-\ell}\in\mathcal D_{N,\mathcal P}$ is invertible in $\mathcal P$, hence its inverse lies in that division closure.
The formal geometric inverse is therefore available in $\mathcal D_{N,\mathcal P}((t;\tau))$ and equals $b$ in the common ambient ring.
Each homogeneous term of that inverse is a finite sum of products involving $c_\ell^{-1}$ and $-c_j$; equations (9) and (10) control these by $\log^2$ of the trees.
An equality can only come from the leading inverse term, forcing $c$ itself to be a monomial by the inner induction, and therefore forcing the same condition on $b$ and its original expression.
The inverse formula is used with the correction on p. 29 recorded below.

This proof checks a scalar rational induction in a regular ambient setting.
It neither assumes all matrices have integral analytical rank nor proves that such a common Laurent-series environment exists for arbitrary torsion-free groups.

Theorem 5.2, pp. 29–30, applies the proposition to the diagonal division closure of $E*G$ in the product of two Hughes-free epic division rings.
Choose a primitive minimizing expression and let $H$ be the image of its finitely generated source in $G$.
If $H$ is nontrivial, local indicability supplies $N\lhd H$ with cyclic quotient; Hughes freeness embeds the two subgroup division rings into their respective skew Laurent-series fields.
Their product gives the required common environment.
A one-term expansion would force the original source into $E^\times N$ by Theorem 4.4, contradicting the definition of $H$.
All nonzero terms therefore have strictly smaller complexity; the leading coefficient is invertible, and the entire element is invertible in the common series ring and hence in the division closure.
Both projections of the resulting division ring are isomorphisms because their images are division subrings containing the given group-ring images and each target is epic.
This proves uniqueness of a Hughes-free epic division ring, conditional on existence, without asserting uniqueness of all division-ring embeddings.

<a id="atiyah-proof"></a>
## The actual analytic division ring and the consequences in Section 6

**Theorem 6.1, pp. 30–31.**
Let $G$ be locally indicable, $K\subseteq\mathbb C$ conjugation-closed, and let a Hughes-free $*$-regular rank on $K[G]$ have epic positive definite $*$-regular envelope $U$.
Then $U$ is a division ring.
The proof starts with $D=\mathcal D_{G,U}$ and proves invertibility of every nonzero element of $D$ by the well-ordered minimum complexity.
For a minimizing primitive expression with source image $H$, its $H$-complexity equals its $G$-complexity: its expression supplies one inequality and subgroup inclusion supplies the other.
The case $H=1$ lies in the image of $K$.
Otherwise choose the cyclic quotient of $H$, take $A=U_N$, and construct $\mathcal P_{\omega,\tau}^{U_N}$.
Hughes freeness and envelope uniqueness identify $U_H$ with a regular subring in that ambient ring, so Lemma 4.5 identifies the division closures and preserves their complexities.
The global induction supplies the lower-complexity invertibility assumption of Proposition 5.1.
The source-subgroup contradiction rules out a one-term expansion, exactly as in Theorem 5.2, and the leading coefficient gives invertibility of the element.
Once $D$ is a division ring, it is a $*$-regular subring containing the original $*$-ring, so epicness and the definition of $U$ give $D=U$.

Corollary 6.2 applies this to $U=\mathcal R_{\mathbb C[G]}$ with its actual affiliated-operator rank, whose Hughes freeness is Proposition 3.11.
The resulting division ring has its unique vector-space matrix rank, so all analytical matrix ranks are integral.
This ordering of the argument is significant: scalar-closure invertibility is proved first using the independently supplied cyclic-quotient rank property, and matrix integrality follows from division-ring linear algebra.
Corollary 6.3 takes any subfield $K\subseteq\mathbb C$, without requiring conjugation closure, and obtains the Hughes-free epic division closure $D_{K[G]}$ inside $\mathcal R_{\mathbb C[G]}$.
Its Hughes freeness follows by restricting the linear independence of the powers of $t$ over $\mathcal R_{\mathbb C[N]}$ to the smaller coefficient division ring.

Proposition 6.5, pp. 31–32, extends the strong Atiyah conclusion to an extension $1\to G_1\to G_2\to Q\to1$ where $G_1$ is torsion-free and satisfies the conjecture over $K\subseteq\mathbb C$, and $Q$ is locally indicable.
The extension is torsion-free because a finite-order element maps trivially to torsion-free $Q$ and must then be trivial in $G_1$.
For the source subgroup $H$ of a rational expression, either $H\leq G_1$, where the assumed Atiyah/division-closure equivalence supplies invertibility, or its nontrivial finitely generated image in $Q$ supplies an epimorphism of $H$ onto $\mathbb Z$.
Proposition 3.11 still supplies the analytical natural extension for that indicable $H$.
This is a precise enlargement of the class covered by the proof, not removal of the source-subgroup alternative.

The remaining corollaries were checked with the following interfaces.

| Passage | Statement and checked deduction | External or scope boundary |
| --- | --- | --- |
| Corollary 6.4, p. 31 | A locally indicable group of homological dimension one is locally free, using Corollary 6.2. | The implication from the Atiyah conjecture to local freeness is [22, Theorem 2]; its original proof was not rechecked. |
| Corollary 6.6, p. 32 | For two embeddings of a characteristic-zero field $K$ into $\mathbb C$, every matrix over $K[G]$ has the same analytical rank after either embedding. | Corollary 6.3 and Hughes-free uniqueness identify the two division envelopes as $K[G]$-rings. |
| Corollary 6.7, pp. 32–33 | Every characteristic-zero field $K$ admits a Hughes-free epic division $K[G]$-ring. | A matrix involves finitely many coefficients, contained in a finitely generated subfield embeddable into $\mathbb C$; independence gives a coherent integer rank, and the epic division-envelope theorem supplies the ring. |
| Lemma 6.8, p. 33 | If $D\otimes_K L$ is a domain, its classical Ore field is Hughes-free for $L[G]$. | Finitely generated field subextensions give noetherian domains, hence Ore domains; clearing denominators reduces Hughes independence to the scalar extension of an independent skew-polynomial family. |
| Corollary 6.9, pp. 33–34 | If $\lambda$ is transcendental over $K$, then $A-\lambda I$ is invertible for matrices $A$ over $D_{K[G]}$. | The written $\mathcal R_{K[G]}$ statement needs the convention correction below; adjoining $\lambda^{-1}$ identifies the new field with $D_{K[G]}(x)$ and sends $\lambda$ to $x^{-1}$, where $A-x^{-1}I$ has a formal inverse. |
| Corollary 6.10, p. 34 | For countable locally indicable $G$, $D_{K[G]}\cap\mathbb C=K$. | A minimal primitive expression with nontrivial source has at least two quotient-degree terms; multiplication by its unit factor shifts degrees, whereas a scalar has only degree zero. |
| Corollary 6.11, p. 35 | For locally indicable ICC $G$ and characteristic-zero $K$, the Hughes-free division ring has center $K$. | A proposed central element is contained in finitely generated coefficients and a countable ICC subgroup; after embedding the coefficients in $\mathbb C$, the affiliated factor has scalar center and Corollary 6.10 applies. |
| Corollary 6.12, p. 35 | For any characteristic-zero field extension $L/K$, $D\otimes_K L$ is a domain and its Ore field is the Hughes-free ring over $L$. | In the ICC case, center $K$ makes the tensor ring simple and its map into the existing Hughes-free $L$-division ring injective; the general nontrivial case embeds in $G\wr\mathbb Z$, and $G=1$ is handled directly. |

In Lemma 6.8 the finite-generation argument can be read by choosing a finite transcendence basis, centrally localizing a polynomial ring over $D$, and adjoining the finite algebraic extension; noetherianity is preserved in that sequence.
Every finite set of tensor coefficients lies in such a field subextension, which proves the Ore property in the directed union.
In Corollary 6.7 the finite matrix defining each truncated natural-extension rank also uses only finitely many field coefficients, so the same coherent embedding argument verifies Hughes freeness, rather than just integer values.
In Corollary 6.10 the nonprimitive unit is shown to lie in $K^\times H$ using $\mathcal R_{\mathbb C[H]}\cap K^\times G=K^\times H$ before the quotient-degree contradiction is made.
For Corollary 6.11 a countable ICC overgroup inside $G$ is obtained by repeatedly adding countably many conjugators for every nontrivial element of the preceding countable subgroup.
These are the specific finiteness and ambient arguments behind the terse corollary proofs.

Corollaries 1.3 and 1.6 for one-relator groups, pp. 3–4, also use external group-theoretic inputs.
The torsion-free case uses local indicability of torsion-free one-relator groups; the torsion case of the Atiyah/eigenvalue/center/independence package uses virtual specialness and the earlier results cited in [18].
Marked-group approximation uses virtual torsion-freeness of one-relator groups and local indicability of their torsion-free subgroups.
Those external classifications are not proved in this paper and their original proofs were not reviewed here.
The [JZ19 supplement](../JZ19/Yin_U001.md#lemma-910-2-completion) now supplies a separately reviewed completion of Lemma 9.10(2), with its explicit distinctness and codomain corrections.
The use of JZ19's published coefficient-change consequences for the torsion one-relator corollary remains an accepted external-theorem use; the selected analytic completion does not constitute an independent review of that entire external chain.
The directly checked algebraic rank-envelope interfaces used in JZLA20 Theorem 6.1 and the locally indicable approximation proof do not pass through that step.
The source's Conjecture 3 is explicitly a conjecture about scalar extension for general Atiyah groups, not an additional theorem supplied by Corollary 6.12.

<a id="approximation-proof"></a>
## The marked-group approximation argument

**Definition and statement, Section 1.3 and Theorem 7.1, pp. 3–4 and 36.**
Fix a finitely generated free group $F$ with a finite free generating set.
Its marked-group space is the set of normal subgroups of $F$, where convergence means eventual agreement on each finite ball, equivalently on membership of each fixed word.
The source gives the metric $e^{-n}$ where $n$ is the largest matching Cayley-ball radius; the topology is independent of the chosen free generating set.
For $M_i\to M$, the matrix $A\in M_{n\times m}(\mathbb C[F])$ is evaluated in the quotient group rings.
Theorem 7.1 asserts $\operatorname{rk}_{F/M_i}(A)\to\operatorname{rk}_{F/M}(A)$ for every such matrix when $F/M$ is virtually locally indicable.
No local indicability, finiteness, residual finiteness, soficity, or monotonicity assumption is imposed on the approximating groups $F/M_i$.
For arbitrary groups the introductory formulation applies this condition to their finitely generated subgroups.

Fix a nonprincipal ultrafilter $\omega$.
The Kazhdan inequality in Proposition 7.2 is the lower bound $\lim_\omega\operatorname{rk}_{F/M_i}\geq\operatorname{rk}_{F/M}$.
It is cited to [19, Proposition 10.7]; this source does not reprove the analytic inequality.
A rank ultraproduct of the positive definite rings $\mathcal R_{\mathbb C[F/M_i]}$ produces a positive definite epic $*$-regular envelope $U$ of the limiting rank.
Relations in $M$ vanish in that rank ultraproduct by eventual membership.
Conversely, the Kazhdan inequality and faithfulness of the quotient's analytical rank show that an element outside the ideal generated by $m-1$, $m\in M$, does not vanish.
Thus the map factors faithfully through $\mathbb C[G]$, where $G=F/M$, and both the ordinary rank and the ultralimit rank can be compared on the same group ring.

Proposition 7.3, pp. 36–37, transports a chain $r_1\leq\cdots\leq r_n$ from $R$ to the diagonal division closure in a product of faithful envelopes.
The cited Cohn matrix linearization gives, for a matrix $A$ over that closure, an equality $A\oplus I_k=P A'Q$ with $P,Q$ invertible there and $A'$ a matrix over the original ring image.
Ranks therefore compare on $A$ because they compare on $A'$.
Faithfulness makes the last projection injective.
For regular envelopes, Corollary 7.4 shows that the first projection also preserves the inverse-or-zero rational operation: invertibility in the first factor has rank one, forcing invertibility in every larger-rank regular factor.
Corollary 7.5 then compares two diagonal closures for $r_1\leq r_2\leq r_3$.
For the same formal expression, nonzero evaluation in factors $(1,2)$ implies nonzero evaluation in factors $(1,3)$, and the two evaluations are invertible simultaneously.
The larger-rank comparison is essential; projection of a division closure to an arbitrary factor does not automatically preserve inverse-or-zero evaluation.

Proposition 7.8 arranges a usable larger rank without assuming that the original ultralimit is Hughes-free.
For $M\leq N\lhd F$ with $F/N\cong\mathbb Z$, put $K_i=M_i\cap N$.
Then $K_i\to M$, and $r_{(F/K_i)}$ is the natural extension of the restriction of $r_{(F/M_i)}$ to $\mathbb C[N]$ by Proposition 3.11 and Corollary 3.8.
Moreover $r_{(F/M_i)}\leq r_{(F/K_i)}$.
For this inequality, $F/K_i$ embeds diagonally into $(F/M_i)\times(F/N)$; Lemma 7.7 compares projection onto the first factor with the rank on its product with $\mathbb Z$.
Lemma 7.6 proves invariance of the untwisted natural extension under $t\mapsto t+1$ by identifying the bounded-degree coefficient modules, and the leading-coefficient rank bound then proves Lemma 7.7.
This avoids a generally unjustified assertion that every quotient group lowers von Neumann matrix rank.

Proposition 7.9, pp. 40–41, proves the diagonal division closure in $\mathcal R_{\mathbb C[G]}\times U$ is a division ring when $G$ is locally indicable.
The induction is simultaneous over all finitely generated locally indicable limits and all their marked approximations, with the same well-ordered tree complexity.
For the finitely generated source subgroup $H\leq G$ choose a finitely generated free lift $F'\leq F$ and the preimage $N'\lhd F'$ of $N\lhd H$.
Replace $M_i'=M_i\cap F'$ by $K_i'=M_i'\cap N'$ to get

\[
\operatorname{rk}_H\leq r_{(F'/M_i')}\leq r_{(F'/K_i')}.
\]

The first rank has the known Hughes-free division envelope from Section 6, and the third is a natural extension.
Take $A=\mathcal R_{\mathbb C[N]}\times U_N$ and embed its Laurent-series ring into $\mathcal R_{\mathbb C[N]}((t;\tau))\times\mathcal P_{\omega,\tau}^{U_N}$.
The regular subring $\mathcal R_{\mathbb C[H]}\times U'$ realizes the first and third ranks, so Lemma 4.5 and Corollary 7.5 transfer the original element's invertibility question to a nonzero element $a'$ in the common-series setting.
If the minimum complexity drops after this transfer, the simultaneous induction already proves invertibility.
In the remaining equality case the original primitive expression still minimizes complexity, Proposition 5.1 applies, and its equality alternative would contradict the source subgroup.
The leading term is therefore invertible by induction and gives invertibility of $a'$ and of the original element.
This explicit split supplies the terse proof's omitted minimality qualification.

For locally indicable $G$, Theorem 7.1 now identifies the two envelopes by projection from their diagonal division closure and hence identifies the ranks on every matrix.
For virtually locally indicable ICC $G$, choose a finite-index normal locally indicable subgroup $G'$, restricting the approximation through a finite-index subgroup of $F$.
The already established case identifies the two $*$-regular closures on $G'$.
The analytical closure on $G$ equals the crossed product $\mathcal R_{\mathbb C[G']}*(G/G')$: it is artinian over the division ring, has proper involution and hence zero radical, and is therefore semisimple regular.
Its rank metric is complete because a faithful rank on a semisimple artinian ring has a positive minimum nonzero scalar rank.
The cited JZ19 completion results and the ICC condition imply that this closure is simple with unique rank.
The subgroup isomorphism extends to the crossed product using conjugation compatibility, is injective by simplicity, and is onto by epicness and regularity.
Unique rank identifies the matrix ranks.
Finally $G*\mathbb Z$ reduces a nontrivial general virtually locally indicable group to the ICC case, and restricting the free-product approximations recovers the result for $G$.
The trivial limit is handled directly; see [the degenerate-case qualification](#source-corrections).
Since the argument works for every nonprincipal ultrafilter, the bounded real rank sequence has the asserted ordinary limit.

<a id="universality"></a>
## What Section 8 proves about universality

**Definitions, p. 43.**
Ranks are ordered pointwise on all matrices.
A rank $r\in\mathcal F\subseteq\mathbb P(R)$ is universal in $\mathcal F$ if $s\leq r$ for every $s\in\mathcal F$.
An epic division $R$-ring $D$ is universal if its rank dominates the ranks of all division $R$-rings; if $R\to D$ is also injective it is a universal division ring of fractions.
Being maximal only means that $s\geq r$ with $s$ in the specified class forces $s=r$.
It does not compare $r$ with ranks that are incomparable in this partial order.

Theorem 8.1 asserts maximality of a Hughes-free epic division rank in $\mathbb P_{\rm div}(E*G)$ for locally indicable $G$ and a division coefficient ring $E$, assuming such a Hughes-free ring exists.
Corollary 8.2 identifies it with a universal epic division ring if a universal one exists separately.
Question 1 explicitly asks for stronger universality properties of $\operatorname{rk}_G$ in several classes of ranks on $\mathbb Q[G]$; those are not established in this edition.
The free-group remark giving equality with inner rank is a separately cited free-group fact, not a conclusion for all locally indicable groups.

Lemma 8.3, pp. 43–44, proves that the natural extension of an integer-valued $\tau$-compatible coefficient rank is largest among ranks on the skew Laurent ring that restrict to that coefficient rank.
Its proof localizes at the square coefficient matrices of full rank, extends rank using Schofield's theorems, and quotients by the rank-zero maximal ideal to reach the division envelope $D$.
The automorphism preserves this localization and its ideal, so every competing rank factors through $D[t^{\pm1};\tau]$.
Matrices over that skew Laurent principal ideal domain admit diagonal reduction; the natural rank is one on every nonzero scalar diagonal entry, and therefore dominates every competing rank.
This is universality with a fixed coefficient-rank restriction, which is stronger than needed for one cyclic step but does not establish unrestricted group-ring universality.

Proposition 8.4 repeats the simultaneous rational induction for a rank $r\geq r_D$ with epic division envelope $E'$.
For $H=N\rtimes\mathbb Z$, replace the second subgroup envelope by its Ore extension $E'_N(t;\tau)$.
Lemma 8.3 yields $r_D|_{E*H}\leq r|_{E*H}\leq r_{E'_N(t;\tau)}$.
The proof of Corollary 7.5 is purely about regular envelopes and the inverse-or-zero rational structure, so the same proof applies here to $E*H$, despite its earlier statement using $\mathbb C[H]$.
It transfers the element to a product of skew Laurent-series division rings.
The same strict-complexity-drop/equality split as in Proposition 7.9 then justifies the application of Proposition 5.1.
The resulting diagonal division closure identifies the two epic division envelopes and proves $r=r_D$, which is precisely maximality.

<a id="source-corrections"></a>
## On-page corrections and the strength of the finding

The following points were checked against the original PDF, rather than inferred only from extracted text.
They are source-inspection findings and local readings of the displayed proof, not reports of author-confirmed errata or claims that the main theorems are false.

1. On p. 28, Proposition 5.1, Case 3, the sentence after the complexity inequality writes $\Phi(\gamma')=c^{-1}=b$ even though $\gamma'$ was chosen with $\Phi(\gamma')=c$.
   The needed expression is $\Phi((\gamma')^\diamond)=c^{-1}=b$, which follows from the immediately preceding definitions.
   This is a missing operation symbol in a minimality argument.
2. On p. 29, the monomial-inverse display writes $t^{-k}(c'_k)^{-1}=\tau^{-k}(c'_k)t^{-k}$.
   The correct right side is $\tau^{-k}((c'_k)^{-1})t^{-k}$.
   The conclusion that the inverse lies in $\mathcal D_{N,\mathcal P}t^{-k}$ is unaffected.
3. On pp. 30 and 41, the formal Laurent-series embedding is called a $*$-homomorphism.
   Equations (4) and (5) establish a $*$-map on Laurent polynomials and an injective ring map on all formal Laurent series, respectively.
   Coefficientwise adjoint together with $t^*=t^{-1}$ does not in general preserve the bounded-below support of an infinite formal series, so that wording is not supplied by the preceding construction.
   Only the ring embedding is used for Proposition 5.1, while the subgroup envelope is compared through the $*$-map on the Laurent-polynomial subring.
4. On p. 33, Corollary 6.9 allows an arbitrary subfield $K\subseteq\mathbb C$ but writes matrices over $\mathcal R_{K[G]}$, defined in Section 2.2 only for conjugation-closed $K$.
   The proof works for matrices over $D_{K[G]}$ for every subfield, and gives the written $\mathcal R_{K[G]}$ statement when $K$ is conjugation-closed.
   It should not be read as silently adjoining complex conjugates to an arbitrary $K$ while keeping algebraicity relative to the original field.
5. On pp. 41 and 45, the proof first states $\operatorname{Tree}_H(a')\leq\operatorname{Tree}(\alpha)$ and then uses $\alpha$ in the minimizing-expression clause of Proposition 5.1.
   If the inequality is strict, the simultaneous induction proves $a'$ invertible immediately; otherwise $\alpha$ is minimizing and the written source-subgroup contradiction applies.
   This supplies an omitted case distinction using the induction already stated, without an additional theorem or assumption.

There are also two elementary degenerate cases in the full proof reconstruction.
In Corollary 6.12, $G\wr\mathbb Z$ is ICC for nontrivial $G$, while for $G=1$ the tensor ring is simply the field $L$.
In the final reduction of Theorem 7.1, $G*\mathbb Z$ is ICC for nontrivial $G$, while if $G=1$ then $M=F$ and convergence forces every finite free generator to belong to $M_i$ eventually, so eventually $M_i=F$ and rank convergence is immediate.
These cases are not obstacles to either conclusion.

<a id="external-foundations"></a>
## Cited inputs and the audit boundary

The source's explicit external-input interfaces were read in their uses and matched to the stated hypotheses.
The following grouping identifies what is retained as foundational input rather than claiming a recursive proof audit.

| Source references in JZLA20 | Role in the inspected proof | Actual inspection boundary |
| --- | --- | --- |
| [1], [12], [32] | $*$-regular closures, matrix regularity, regular-ring epimorphisms, and ordinary quotient-ring facts in Sections 2–3 and 7. | Their statements and on-page uses were checked; the cited original books and paper were not re-audited. |
| [3], [4], [28], [31] | Epic division envelopes, uniqueness by matrix rank, stable matrix linearization, and full-rank universal localization in Sections 2, 7 and 8. | The exact roles are stated above; Cohn's and Schofield's proofs are not claimed checked by this unit. |
| [5], [29] | Well-order and monotonicity of rooted-tree complexity, universality of rational semirings, and the finitely generated minimal source subgroup in Section 4. | The primary [5] definition and source-subgroup statement were checked as described below; its complete recursive construction and the thesis proofs were not audited. |
| [18] = JZ19 | Epic $*$-regular envelope uniqueness, natural rank-extension interfaces, and rank-completion simplicity and uniqueness in Sections 2–3 and 7. | A separately performed direct primary-source audit confirmed the interfaces; see [JZ19](../JZ19/Yin_U001.md#epic-rank-linearization), [natural extensions](../JZ19/Yin_U001.md#natural-rank-extensions), and [its foundational boundary](../JZ19/Yin_U001.md#external-foundations). |
| [18], coefficient-change consequences | Earlier results on virtually special/sofic groups in the torsion one-relator consequences of Corollary 1.3. | JZ19 Lemma 9.10(2) has the separately reviewed completion linked above; this unit does not claim an independent recheck of the entire external coefficient-change chain. |
| [19, Corollary 12.2 and Proposition 10.7] | Natural extension of analytical rank across an infinite cyclic quotient, and the Kazhdan lower bound for marked-group limits. | The primary survey statements and their displayed short deductions were checked as described below; the entire supporting survey was not audited. |
| [24], [33], [34] | Exact module ranks, normalized lengths, and entropy construction of natural extensions. | The skew-extension interfaces in Propositions 3.2–3.5 were checked as stated; the original entropy and extension theorems are not claimed proved here. |
| [2], [11], [15], [22], [25], [35] | One-relator local indicability/virtual results, homological-dimension consequence, and finite-index group-ring crossed-product realization. | The deductions from those inputs were checked at their source hypotheses; their original proofs remain external. |

This boundary is relevant to interpreting the word “full”: every section and on-page proof in the selected original was inspected, but the source itself invokes substantial external mathematics and sometimes states a skew analogue while referring to earlier proofs.
In particular, the exact natural-extension characterization, the finitely generated source-subgroup theorem, the analytical cyclic-extension identity, and the Kazhdan inequality are genuine mathematical inputs rather than conclusions of the local scalar induction.
The current source inspection supplies no independent project review or blanket approval of later generalizations.

The targeted primary-source follow-up on 10 November 2026 read [Dicks–Herbera–Sánchez's author PDF](https://mat.uab.cat/~dicks/Hughes.pdf), Definition 4.1 on printed p. 8 and Lemma 5.4 through Theorem 5.7 on p. 15.
It confirms the multiplicative-action convention, finite generation and least-subgroup property used by JZLA20 Theorem 4.4.
Its Lemma 3.3 proof on pp. 6–7 was also read: a descending tree chain is contradicted by successively minimizing height, largest child and width.
The preceding recursive source construction was not fully audited.

The same follow-up read the [author-hosted survey](https://andreijaikin.wordpress.com/wp-content/uploads/2024/05/surveyl2.pdf), Proposition 10.7 on p. 36 and Corollary 12.2 on p. 45.
The former derives the kernel-dimension upper bound from weak convergence of spectral measures and Portmanteau at the closed set $\{0\}$.
The latter states the natural-extension identity for a countable group with amenable quotient and reduces it to Theorem 12.1 and Proposition 8.3.
For JZLA20 the subgroup $H$ is finitely generated and the quotient is $\mathbb Z$, so these conditions hold; restriction from the conjugation-closed coefficient setting gives the stated subfield case.
The survey's preceding general spectral-approximation and amenable-extension proofs were not audited here.

<a id="general-torsion-free-boundary"></a>
## Transfer to a general torsion-free rational-closure problem

The generally reusable parts are the regular-ambient Lemma 4.5, rational inverse-or-zero evaluation, the tree-based statement of Proposition 5.1, and the rank-comparison linearization in Proposition 7.3.
Each retains its exact ambient, invertibility and lower-complexity hypotheses.
The theorem converting an epic positive definite $*$-regular envelope into a division ring additionally needs local indicability and Hughes freeness.
Those hypotheses enter before the scalar-closure conclusion and cannot be recovered merely by writing an element as a rational expression or a matrix inverse entry.

For a general torsion-free $G$, a minimal expression still has finite support, but the finitely generated image of its source need not be supplied with a quotient onto $\mathbb Z$ by the hypotheses under discussion.
Without that quotient there is no $N\rtimes\mathbb Z$ step, no relevant Laurent-series decomposition, and no source-subgroup contradiction establishing strict coefficient complexity reduction.
An abstract division-ring embedding, when available, also does not by itself identify its rank with the given affiliated-operator rank.
JZLA20 achieves the latter identification through the natural-extension property and epic $*$-regular envelope uniqueness.

The stable linearization in Proposition 7.3 transfers comparisons that already hold for all matrices over the original ring.
It does not create integer ranks from scalar rank information.
For example, with $Q$ invertible in the fixed regular ambient ring, ordinary block elimination gives

\[
r\begin{pmatrix}Q&v\\u&a\end{pmatrix}
=\operatorname{size}(Q)+r(a-uQ^{-1}v).
\]

This is the same rank-preserving elementary-equivalence mechanism, written as a Schur complement.
If the block matrix rank is not already known to be integral, the equality does not force the scalar complement to have rank zero or one.
Using integrality of that arbitrary original-ring block matrix to prove the division-ring conclusion would import the matrix Atiyah assertion that the argument is intended to establish.
Conversely, JZLA20's successful locally indicable argument first proves actual scalar invertibility by the cyclic-quotient complexity induction and only then deduces matrix integrality.

Finally, Section 8 cannot fill this gap by invoking universality without proof: its theorem is maximality among integer-valued ranks, and the existence of a universal epic division ring is a separate premise of Corollary 8.2.
No statement here establishes inner-rank equality, rational-closure division, or analytical matrix integrality for every torsion-free group.
Any proposed extension must provide the missing cyclic/source reduction or a different argument with its own fixed mathematical evidence.
