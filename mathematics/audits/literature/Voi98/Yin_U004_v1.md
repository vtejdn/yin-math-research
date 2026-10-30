---
author: Yin
---

<a id="voi98-u004"></a>
# Voi98-U004: Closed Difference Quotients and Analytic Changes of Variable

- Source: [Voi98](../../../literature/pdf/Voi98.pdf), supplied published version, Section 4, Propositions 4.1-4.10, printed pp. 203-208 (PDF pp. 15-20).
- Record: 2026-09-08, the derivation agent, proof reconstruction for [Voi98 finite-Fisher source audit](readme.md#voi98-finite-fisher-source-audit).
- Coverage: the local adjoint, closure, smooth-image, power-series, contraction and chain-rule arguments were inspected.
  Corrections and the separate abstract-completion limitation are recorded below.
  This is not formal verification.

## Setting and tensor conventions

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal tracial state, $B\subseteq M$ a unital star algebra, and $X=X^*\in M$ algebraically free from $B$.
Put $A=B[X]$, $N=W^*(A)$ and $H=L^2(N,\tau)$.
The difference quotient is the densely defined operator

$$
\partial:A\subset H\longrightarrow H\otimes_2H,
\qquad \partial X=1\otimes1,\quad \partial B=0,
$$

with $\partial(ab)=(a\otimes1)\partial b+\partial a(1\otimes b)$.
The unadorned tensor product in this identity has ordinary componentwise multiplication.
Hilbert-space inner products are linear in the first variable.
The flip-star relation is $\partial(a^*)=\sigma((\partial a)^*)$, where $\sigma(u\otimes v)=v\otimes u$.

For differential composition only, put $\widetilde\partial a\in A\otimes A^{\mathrm{op}}$, replacing the second factor of $\partial a$ by its opposite-algebra copy.
Here

$$
(a\otimes b^{\mathrm{op}})(c\otimes d^{\mathrm{op}})
=ac\otimes(db)^{\mathrm{op}},\qquad
(a\otimes b^{\mathrm{op}})\cdot\zeta=a\zeta b.
$$

These two tensor multiplications must not be interchanged.
If $\zeta\in H$, the bilinear map $(a,b)\mapsto a\zeta b$ extends to the Banach projective tensor product with norm at most $\|\zeta\|_2$.
Multiplication $m_1(a\otimes b)=ab$ is projective-norm contractive; it is not bounded on the Hilbert tensor product in general.

## Adjoint domains and closability: 4.1-4.3

For $\eta\in\operatorname{Dom}\partial^*$ and $a\in A$, the two actual formulas in 4.1 are

$$
\begin{aligned}
\partial^*(\eta(1\otimes a))
 &= (\partial^*\eta)a-(\mathrm{id}\otimes\tau)(\eta(\partial(a^*))^*),\\
\partial^*((a\otimes1)\eta)
 &=a\partial^*\eta-(\tau\otimes\mathrm{id})((\partial(a^*))^*\eta).
\end{aligned}
$$

Products with $\partial(a^*)$ are bounded multiplications on $L^2(N\bar\otimes N)$, and the partial-trace maps are $L^2$ contractions.
Pair each expression against $q\in A$, move $a$ to the other side of the Hilbert pairing, and apply the Leibniz formula to $qa^*$ or $a^*q$.
The resulting functional is bounded in $\|q\|_2$, which establishes both domain membership and the formulas; formal integration by parts alone would not establish membership.

Write $\xi=\mathcal J(X:B)=\partial^*(1\otimes1)\in H$, using the conjugate-variable/adjoint equivalence from Section 3.3.
Applying 4.1 twice shows that $A\otimes A\subset\operatorname{Dom}\partial^*$.
This domain is dense in $H\otimes_2H$, so $\partial$ is closable; denote its closure by $\bar\partial$.
No boundedness of $\xi$ is required.

For $a,b\in A$, the resulting formula is

$$
\partial^*(a\otimes b)
=a\xi b-(\mathrm{id}\otimes\tau)(\partial a)b
-a(\tau\otimes\mathrm{id})(\partial b).
\tag{1}
$$

Equivalently, for $\eta\in A\otimes A$,

$$
\partial^*\eta=m_\xi(\eta)
-m_1(\mathrm{id}\otimes\tau\otimes\mathrm{id})
  (\partial\otimes\mathrm{id}+\mathrm{id}\otimes\partial)\eta.
\tag{2}
$$

The ordinary tensor star and the flip-star relation explain the order of each contraction.
Formula (2), printed as Proposition 4.3, passes this check unchanged.

## Iterated derivatives and the missing factor two: 4.4 and 4.7

Use the source's divided-derivative convention

$$
\partial^{(p+1)}=(\partial\otimes\mathrm{id}^{\otimes p})\partial^{(p)},
\qquad \partial^{(1)}=\partial.
$$

For a word containing $m$ occurrences of $X$, $\partial^{(p)}$ sums over the $\binom mp$ increasing choices of $p$ cut positions.
Coassociativity follows by choosing the same cut positions regardless of the factor subsequently differentiated.
Thus

$$
(\partial\otimes\mathrm{id}+\mathrm{id}\otimes\partial)\partial a
=2\partial^{(2)}a.
$$

Consequently the correct 4.4 identity is

$$
\partial^*\partial a
=m_\xi(\partial a)
-2m_1(\mathrm{id}\otimes\tau\otimes\mathrm{id})\partial^{(2)}a.
\tag{3}
$$

The published display omits the factor **2**, and Proposition 4.7 repeats the omission.
This is visible in the rendered PDF, not an extraction artifact.
For $a=X^2$, (1) gives

$$
\partial^*\partial X^2=X\xi+\xi X-2,
$$

whereas the published 4.4 expression gives $X\xi+\xi X-1$.
The membership $A\subset\operatorname{Dom}(\partial^*\partial)$ survives; the formula requires correction.

## Smooth completions: precise operational conclusions in 4.5-4.7

With $\|\cdot\|_{\pi,r}$ the projective norm on $r$ copies of $N$ equipped with operator norm, use the consistent indices

$$
\|a\|_{(k)}=\|a\|+\sum_{p=1}^k\|\partial^{(p)}a\|_{\pi,p+1}.
$$

The source occasionally writes a $p$-factor norm for a $(p+1)$-factor derivative, and its star-reversal index must likewise reverse all $p+1$ factors.
The product identity partitions the $p$ ordered cuts between the two multiplied words, with their common boundary factors multiplied.
Summing these estimates proves submultiplicativity.
Reversal and adjoint are isometries, proving $\|a^*\|_{(k)}=\|a\|_{(k)}$.

Let $\mathcal B_k$ first mean the **abstract completion** of $A$ in this norm, with its continuous evaluation map $E_k:\mathcal B_k\to C^*(A)$.
The following operator conclusions hold for its image and are sufficient for the paper's subsequent analytic changes:

1. If $a\in E_1(\mathcal B_1)$, then $a\in\operatorname{Dom}\bar\partial$, and its projective first derivative maps to $\bar\partial a\in H\otimes_2H$.
2. If $a\in E_1(\mathcal B_1)$ and $z\in\operatorname{Dom}\bar\partial$, both $az$ and $za$ belong to that domain and satisfy the two Leibniz formulas of 4.5.
3. The canonical Hilbert-space image of $\mathcal B_1\widehat\otimes_\pi\mathcal B_1$ belongs to $\operatorname{Dom}\partial^*$, with (2) extended continuously as an $L^2$ formula.
   If $\xi\in N$, the output is bounded.
4. If $a\in E_2(\mathcal B_2)$, then $a\in\operatorname{Dom}(\partial^*\bar\partial)$, with corrected formula (3).
   If $\xi\in N$, the output is bounded.

Here is the domain argument omitted as an exercise in the source.
A graph-norm Cauchy polynomial sequence converges in operator norm, and its first derivatives converge in projective norm, hence Hilbert norm.
Closedness of $\bar\partial$ proves item 1.
For a fixed polynomial $z$, pass to this limit in the polynomial product rule.
Then approximate general $z$ in the graph norm of $\bar\partial$: if $\eta=\sum a_j\otimes b_j$ is projective-summable, the map $z\mapsto\sum a_j\otimes b_jz$ has norm at most $\|\eta\|_\pi$ from $L^2$ to the Hilbert tensor product.
This makes every product-rule term converge, and closedness proves item 2.

For item 3, on elementary tensors formula (1) is bounded from the projective product of the first-derivative norms to $L^2$, for example by $(\|\xi\|_2+2)\|a\|_{(1)}\|b\|_{(1)}$.
Polynomial approximation and closedness of $\partial^*$ therefore give the formula on the completed tensor product's Hilbert-space image.
Any kernel of that canonical map is automatically killed by this extended adjoint formula.
For item 4, (3) yields an $L^2$-Cauchy sequence of adjoint outputs whenever the input sequence is Cauchy in $\|\cdot\|_{(2)}$.
Apply closedness of $\partial^*$ to the convergent first derivatives.
The second derivative in this argument is a chosen projective limit from the smooth completion; the contracted output in (3) is independent of that choice by closedness and uniqueness of the first derivative.
This does not assert uniqueness of an uncontracted higher projective derivative.
The corresponding operator-norm estimates when $\xi\in N$ establish boundedness.

**Abstract identification boundary.**
The source directly identifies every $\mathcal B_k$ with a subalgebra of $C^*(A)$.
Mere Hilbert-space closability does not, by itself, prove injectivity of a stronger projective graph completion.
For $k=1$ this audit supplies the missing justification: Haa85, Proposition 2.2 and its following remark, give injectivity of the canonical two-C*-factor projective-to-minimal tensor map.
The minimal tensor product embeds into $L^2(N\bar\otimes N)$ via its faithful tensor trace.
Therefore a first-derivative projective limit with zero Hilbert image is zero, and $E_1$ is injective.
The general $k\geq2$ abstract identification, and injectivity of the completed tensor product of the smooth Banach algebras themselves, are **not independently established in this audit**.
The four image statements above avoid needing those stronger identifications; this limitation does not question their proved operator conclusions.

## Power series and convergence: 4.8

Write the degree-$k$ coefficient of a noncommutative $B$-coefficient polynomial as the single tensor

$$
c_k=\sum_{i\in I(k)}b_0^{(k,i)}\otimes\cdots\otimes b_k^{(k,i)}.
$$

The well-defined projective coefficient norm is

$$
|P|_R=\sum_{k\geq0}\|c_k\|_{\pi,k+1}R^k.
\tag{4}
$$

Equivalently, take the infimum of the sums of products of coefficient norms over tensor representations degree by degree.
The printed p. 206 display instead sums the projective norms of individual elementary tensors; without this infimum or moving the coefficient sum inside the norm, it depends on the representation of a polynomial.
For instance writing the zero polynomial as $t-t$ gives a positive displayed value.
We use (4) for $B_R\{t\}$, including the norm closure of $B$ in its coefficients.
Concatenating coefficient tensors and multiplying the adjacent boundary factors proves the Banach-algebra estimate.

For fixed $p\geq1$ and $R>\|X\|$, the correct derivative bound is

$$
\|\partial^{(p)}P(X)\|_{\pi,p+1}
\leq\sum_{k\geq p}\binom{k}{p}\|X\|^{k-p}\|c_k\|_{\pi,k+1}
\leq C_{p,R,X}|P|_R,
$$

where $C_{p,R,X}=\sup_{k\geq p}\binom{k}{p}\|X\|^{k-p}R^{-k}<\infty$.
At $X=0$ the only surviving degree is $k=p$, interpreted directly.
The source prints $k$ instead of $\binom{k}{p}$; this is insufficient for general $p$, although polynomial growth is still dominated by the strict radius margin.
Polynomial partial sums therefore converge in every $\|\cdot\|_{(p)}$ and evaluate to a bounded operator in each smooth image.
Under $\xi\in L^2$, item 4 above proves $P(X)\in\operatorname{Dom}(\partial^*\bar\partial)$.
No equality at the radius boundary $R=\|X\|$ is asserted.

## A small analytic inverse: 4.9

For $R,\delta>0$, set

$$
C=\sup_{k\geq1}\frac{k(R+\delta/2)^{k-1}}{(R+\delta)^k}<\infty,
\qquad \eta\leq\min\{\delta/2,(2C)^{-1}\}.
$$

If $P=P^*\in B_{R+\delta}\{t\}$ and $|P|_{R+\delta}<\eta$, the source's map

$$
H(T)=\tfrac12(t+T-P(T))
$$

is a contraction on the closed real subspace ball $\Omega=\{T=T^*:|T|_R\leq R+\delta/2\}$.
Expanding a monomial difference by replacing one factor at a time gives

$$
|P(T_1)-P(T_2)|_R\leq C|P|_{R+\delta}|T_1-T_2|_R.
$$

Thus $H$ is $3/4$-Lipschitz.
Also $|P(T)|_R\leq|P|_{R+\delta}\leq\delta/2$, so $|H(T)|_R\leq R+\delta/2$.
Completeness proves a unique fixed point in this ball, satisfying $G+P(G)=t$ and $G=G^*$.
This is sharper than the stated $|G|_R\leq R+\delta$.
The proof line saying only $P\in B_R\{t\}$ must retain $P\in B_{R+\delta}\{t\}$; several symbols in the polynomial display there are also displaced.
The contraction proof itself survives with these corrected definitions.
It gives the indicated local right composition inverse, not a global inverse for arbitrary changes of variable.

## The chain rule: 4.10

For $Y=P(X)$, differentiation of each occurrence of $P(X)$ gives

$$
\widetilde\partial_X q(Y)
 =\bigl(\widetilde\partial_Yq(Y)\bigr)
   \bigl(\widetilde\partial_XP(X)\bigr),
\tag{5}
$$

with multiplication in the opposite tensor algebra specified above.
On a monomial, the first factor inserts the entire derivative of $P$ between its prefix and suffix; this proves the order in (5).

As an identity on **formal expressions** $q$, this requires no extra freeness of $Y$.
As an identity between well-defined derivations on the evaluated algebra $B[Y]$, it requires that $\partial_Y$ descend to that algebra, for example algebraic freeness of $Y$ from $B$.
The printed assumptions $P=P^*$ alone include constant $P$, for which $\partial_Y(Y)=1\otimes1$ and $\partial_Y(B)=0$ are incompatible.
We therefore do not reuse the literal unrestricted statement.
Near-identity changes used elsewhere must separately justify their evaluation and derivative domains.
Power-series versions follow by the strict-radius estimates, when the relevant substitutions and derivatives converge.

## Dependencies, search and review limits

- Section 3 supplies the well-defined polynomial difference quotient and the $L^2$ conjugate-variable criterion; no argument here assumes the later Fisher-information or entropy conclusions.
- The needed two-factor tensor injectivity was checked in the primary [Haa85 PDF, Proposition 2.2, pp. 96-97, and following remark](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1980s/1985_The_Grothendieck_inequality_for_bilinear_forms_on_C-star_algebras.pdf).
  Its finite-rank-bilinear-approximation proof was read; the underlying noncommutative Grothendieck theorem is accepted with original proof unreviewed.
  Bibliographic and access details belong in the [literature registry](../../../literature/readme.md).
- Search on 2026-09-08 was triggered by the projective-completion interface and the displayed factor discrepancy.
  Queries included `Banach projective tensor product C* algebras canonical map minimal tensor product injective Haagerup` and `Voiculescu 1998 Fisher information 4.4 factor 2 errata`.
  Gupta-Jain arXiv:1809.01131v1, Proposition 3.2, was used only to locate Haa85.
  Follow-up searches using `projective tensor C*-algebras three injective`, `projective tensor multilinear Voiculescu`, and `Voiculescu B(1) closable` did not supply the needed higher-completion argument.
  No source located in this bounded search supplied an author-confirmed correction.
  We stopped the two-factor branch after its primary statement was checked; the stronger multi-factor abstract identification is expressly outside the established conclusions above.
  These search limits do not establish that a general identification is false or absent from the literature.
- The adjoint and fixed-point proofs use elementary Hilbert-space adjoint theory, projective tensor estimates and the contraction principle, reconstructed above.
  No whole-book audit or computational test is needed for these arguments.
  Rendered PDF pp. 15-20 were inspected directly, including all affected displays.
- Independent AI review, 2026-09-08, the conjugate-variable agent: read this full unit and all rendered source PDF pp. 15-20; recomputed the 4.1 multiplication orders, (2), the $X^2$ factor check, operator-image limits, projective-to-Hilbert estimates, coefficient norm and binomial derivative bound, contraction constants and opposite-algebra chain order.
  The reviewer also inspected Haa85 Proposition 2.2 and its following remark directly.
  No unresolved issue was found in the recorded operator-image conclusions; the reviewer agreed that general higher-$k$ abstract-completion faithfulness remains unestablished here.
  The full Grothendieck proof was not reviewed.

## Revisions and downstream effects

2026-09-08: first audit records corrected factors in 4.4/4.7, the projective coefficient norm and higher-derivative estimate, strict analytic-radius hypotheses, and the well-definedness condition for 4.10.
Smooth operator-image statements are separated from the unestablished general abstract-completion identification.
These corrections preserve the recorded closure and analytic-change mechanisms; downstream formulas must use (3), not the printed contraction coefficient.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Voi98, the retained 39-page published journal article, printed pp. 189-227; printed page = PDF page + 188. Other works retain their separate exact versions and inspection limits in the body. |
| source-locator | Section 4, Propositions 4.1-4.10, printed pp. 203-208 / PDF pp. 15-20. |
| inspection | 2026-09-08: adjoint domains, closability, smooth operator images, corrected analytic estimates, inverse construction and formal chain rule reconstructed and independently reviewed. General higher-order abstract projective-completion faithfulness remains unestablished; the Haa85 two-factor proof inspection does not include the full underlying Grothendieck proof. |
