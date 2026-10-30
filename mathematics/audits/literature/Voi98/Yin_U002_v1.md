---
author: Yin
---

<a id="voi98-u002"></a>
# Voi98-U002: Conjugate Variables and Scalar Hilbert Transforms

- Source: [Voi98](../../../literature/pdf/Voi98.pdf), Section 3 through Proposition 3.5, printed pp. 192-197 / PDF pp. 4-9.
- Record: 2026-09-08, the conjugate-variable agent, for [Voi98 finite-Fisher source audit](readme.md#voi98-finite-fisher-source-audit).
- Scope: definitions, tensor conventions, uniqueness, adjoint characterization, first-order perturbation and the scalar Hilbert-transform realization.
  The following unit contains the free-extension and regularization results.

## Setting and the Iterated Difference Quotient

Let $(M,\tau)$ be a finite von Neumann algebra with a faithful normal tracial state, $1\in B\subseteq M$ a star-subalgebra, and $X=X^*\in M$.
Write $A=B[X]$ and $N=W^*(A)$.
The source initially assumes that $X$ and $B$ are **algebraically free**, so evaluation identifies the formal polynomial algebra $B\langle x\rangle$ with $A$.
This is different from free independence of the state.
Define

$$
\partial X=1\otimes1,\qquad \partial b=0,\qquad
\partial(ab)=(\partial a)(1\otimes b)+(a\otimes1)\partial b.
$$

These are algebraic tensor products over $\mathbb C$, with the outer bimodule actions.
The vector-space-identical map $\widetilde\partial$ takes values in $A\otimes A^{\rm op}$; its multiplication differs, and $(a\otimes b)\mathbin{\#}c=acb$.
Do not exchange ordinary and opposite multiplication when using Jacobians or adjoints.

Set $\partial^{(1)}=\partial$ and $\partial^{(k+1)}=(\partial\otimes\mathrm{id}^{\otimes k})\partial^{(k)}$.
For a word $b_0Xb_1\cdots Xb_m$, $\partial^{(p)}$ is the sum over increasing choices of $p$ of its $m$ occurrences of $X$: remove those occurrences and put the resulting $p+1$ consecutive subwords in separate tensor factors.
Empty intervening subwords retain their coefficient $b_j$.
The same sum results if further differentiation is inserted in any tensor position, proving the source's coassociativity formula.
Every choice occurs **once**, with no factor $p!$.
For example,

$$
\partial^{(2)}X^2=1\otimes1\otimes1.
$$

This convention is essential for the later higher-adjoint formulas.
It is not the ordinary iterated scalar derivative convention.

We use $\|\xi\|_q=\tau(|\xi|^q)^{1/q}$ for $1\leq q<\infty$ and the operator norm for $q=\infty$.
The final line of printed p. 193 omits the $1/q$ power when displaying the $L^q$ notation.
Membership is unaffected, but all norm inequalities below use the actual norm.
Elements of $L^1(N)$ are the usual tracial measurable affiliated operators; pairing $\tau(\xi a)$ with bounded $a$ is defined and continuous.

## Definition 3.1 and Remarks 3.2

For integer $p\geq1$, $J_p(X:B)$ is an element $\xi\in L^1(N)$ satisfying

$$
\tau(\xi a)=\tau^{\otimes(p+1)}(\partial^{(p)}a)
\quad(a\in A).
\tag{1}
$$

Existence is a condition, not part of the definition of every $X$.
The symbol $J$ means $J_1$.
Equation (1) gives $\tau(\xi)=0$.
It also gives the explicit sum of products of traces obtained by cutting words as above; the scalar traces in Remark 3.2(b) are multiplied, not tensor factors of a new algebra.
Its final subscript $b_m$ should agree with the word's index $b_n$.

The following details justify the source's short remarks.

1. **Uniqueness and projection.**
   If $\xi,\eta\in L^1(N)$ have the same pairings on $A$, their normal functionals agree on $N$ by bounded strong-star density and hence $\xi=\eta$.
   If a solution is initially in $L^1(M)$, its trace-preserving conditional expectation $E_N\xi$ has the same pairings.
   This uses the normal predual extension of conditional expectation, not an $L^2$ projection on an arbitrary $L^1$ element.
2. **Coefficient closure.**
   Kaplansky approximation of each coefficient $b_j\in W^*(B)$ by a uniformly bounded net in $B$ passes the word identities to the closure.
   Products converge strongly-star on bounded sets.
   For the left side, approximate $\xi$ in $L^1$ by bounded truncations and use $|\tau((\xi-\xi_R)a)|\leq\|\xi-\xi_R\|_1\|a\|$; for bounded truncations, normality suffices.
   Thus the same moment relations describe $J_p(X:B)$ and $J_p(X:W^*(B))$.
   Whenever the difference quotient is used as an operator on an evaluated algebra, its well-definedness remains part of the setting; the moment-identity extension by itself is not an assertion about arbitrary quotient algebras.
3. **Selfadjointness.**
   Taking the star of a word reverses the order of its cuts and tensor factors.
   The product trace is invariant under this reversal.
   Therefore the functional on the right of (1) satisfies $L(a^*)=\overline{L(a)}$, and uniqueness gives $\xi^*=\xi$.
   No boundedness of $\xi$ is used.
4. **Opposite algebra.**
   For $p=1$, the product trace of $\widetilde\partial a$ agrees with that of $\partial a$.
   This is the exact interface used by Proposition 3.10 in [U003](Yin_U003_v1.md#voi98-u003).

## Lemma 3.3: Adjoint Characterization

Equip $L^2(N)$ with $\langle u,v\rangle=\tau(v^*u)$, linear in the first variable.
Regard $\partial^{(p)}$ as a densely defined operator with domain $A$ from $L^2(N)$ to $L^2(N^{\overline\otimes(p+1)})$.
For $\xi\in L^2(N)$, (1) is equivalent to

$$
1^{\otimes(p+1)}\in\operatorname{Dom}((\partial^{(p)})^*),
\qquad (\partial^{(p)})^*1^{\otimes(p+1)}=\xi.
\tag{2}
$$

Indeed, use selfadjointness of $\xi$ and tensor-reversal symmetry to rewrite (1) as the Hilbert-space adjoint identity against every polynomial.
Conversely that identity, evaluated at starred polynomials, gives (1).
The ordinary and opposite tensor products have the same product-trace Hilbert space under the vector-space identification, giving the $p=1$ statement for $\widetilde\partial$.
Printed Lemma 3.3(iii) drops $A$ from the displayed algebraic codomain; it must be $A\otimes A^{\rm op}$.
Existence of the single adjoint vector in (2) does not itself prove closability; the dense adjoint-domain argument belongs to Section 4.

For clarity about coefficient closures and later limit arguments, the following first-order consequence can also be reconstructed directly.
Suppose the formal version of (1) holds for $p=1$ with an $L^1$ vector, without first assuming algebraic freeness.
If a formal polynomial $P$ evaluates to zero, test (1) on $aPb$.
The Leibniz terms containing an undifferentiated $P$ vanish, leaving

$$
(\tau\otimes\tau)\big((a\otimes1)(\partial P)(X)(1\otimes b)\big)=0
$$

for all evaluated polynomials $a,b$.
Tensor-product $L^2$ density implies $(\partial P)(X)=0$.
If a nonzero relation of minimal positive $X$ degree $m$ existed, evaluation would be injective on degrees less than $m$, and therefore also on their algebraic tensor product.
Each factor of $\partial P$ has degree less than $m$, so $\partial P=0$ formally.
The component obtained by cutting the first $X$ in the degree-$m$ term shows that this is impossible.
Degree-zero evaluation is just the original embedding of $B$.
Thus first-order formal conjugate relations rule out algebraic relations.
This argument fills an interface for $p=1$ only; this paragraph does not claim an analogous theorem from a lone higher-order relation.

## Proposition 3.4: The Perturbation Coefficient Is One Half

Assume $S$ is standard semicircular, free from $A$, and $J(X:B)\in N$ is bounded.
For every fixed word $b_0Xb_1\cdots Xb_n$,

$$
\tau\big(b_0(X+\tfrac\varepsilon2J)b_1\cdots
(X+\tfrac\varepsilon2J)b_n\big)
=\tau\big(b_0(X+\sqrt\varepsilon S)b_1\cdots
(X+\sqrt\varepsilon S)b_n\big)+O(\varepsilon^2)
\tag{3}
$$

as $\varepsilon\downarrow0$.
Constants may depend on the fixed word, coefficients and operators; there is no asserted uniform approximation over all polynomials or operator-norm transport statement.

On the left, expand in $\varepsilon$.
Moving each inserted $J$ to the start using the trace and applying (1) produces two identical contributions for each unordered pair of positions; the factor $1/2$ removes that double counting.
On the right, symmetry of the law of $S$, together with freeness, eliminates terms with an odd number of $S$ factors.
Each term with two $S$ factors contributes $\tau(SaSb)=\tau(a)\tau(b)$ after cyclic rotation.
These are exactly the same unordered-pair terms.
Terms with at least four $S$ factors have order at least $\varepsilon^2$.
The expansion on the left is legitimate because $J$ is bounded.
The proof uses only a symmetric bounded perturbation of variance one, as the source observes; semicircularity is not needed for this particular order of approximation.

The check with $X=S$ and the second moment gives $(1+\varepsilon/2)^2=1+\varepsilon+O(\varepsilon^2)$ and fixes the coefficient without relying on typography.
One must not insert this $1/2$ into the definition of $J$ or into the later Fisher-information norm.

## Proposition 3.5: Scalar Hilbert-Transform Realization

Take $B=\mathbb C$.
Assume the compactly supported law of bounded $X$ has density $p\in L^3(\mathbb R,dt)$.
Use the normalized Hilbert transform

$$
Hf(t)=\frac1\pi\operatorname{p.v.}\int\frac{f(s)}{t-s}\,ds.
$$

Then

$$
J(X)=g(X),\qquad g=2\pi Hp,
\qquad g_\varepsilon(t)=2\int\frac{(t-s)p(s)}{(t-s)^2+\varepsilon^2}\,ds
\longrightarrow g
\tag{4}
$$

in both Lebesgue $L^3$ and $L^2(p(t)dt)$.
In particular this is an $L^2$ conjugate variable, and boundedness is not asserted.

The algebraic part of the proof is the scalar identity

$$
(\tau\otimes\tau)(\partial m(X))
=\iint\frac{m(t)-m(s)}{t-s}\,p(t)p(s)\,dt\,ds.
$$

The polynomial difference quotient is bounded on the compact square containing the support.
Multiplying it by $(t-s)^2/((t-s)^2+\varepsilon^2)$ and applying dominated convergence is legitimate; the diagonal has zero product measure.
Interchanging $s,t$ in half the regularized integral gives $\int m(t)g_\varepsilon(t)p(t)dt$.

For the analytic interface, the exact normalized Hilbert-transform definition, its $L^2$ Fourier multiplier, and its $L^q$ boundedness for $1<q<\infty$ were checked in the author's [Tao06 notes](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf), pp. 1, 3, 7 and Corollary 2.10 on p. 9.
This is an alternative primary exposition of the needed theorem; Voi98's cited Stein-Weiss book was not inspected.
Accept the $L^3$ boundedness theorem with its complete original proof outside this audit.

Here is the remaining regularization argument, rather than importing an unspecified mode of convergence.
Let $P_\varepsilon(t)=\varepsilon/(\pi(t^2+\varepsilon^2))$.
The Poisson kernels are an approximate identity: their mass is one, their mass outside any fixed neighborhood tends to zero, and Minkowski's inequality plus continuity of translations proves $P_\varepsilon*h\to h$ in $L^3$ for every $h\in L^3$.
The elementary Fourier transform of $P_\varepsilon$ is $e^{-2\pi\varepsilon|\zeta|}$; applying the Hilbert multiplier $-i\operatorname{sgn}\zeta$ identifies $HP_\varepsilon(t)=t/(\pi(t^2+\varepsilon^2))$.
Since compact support and $p\in L^3$ give $p\in L^2$, this identity can first be used in $L^2$ Fourier calculus, and then in the $L^3$ realization.
Hence $g_\varepsilon=2\pi P_\varepsilon*Hp\to2\pi Hp$ in $L^3$.
Finally,

$$
\int|g_\varepsilon-g|^2p
\leq\|p\|_3\,\|g_\varepsilon-g\|_3^2\longrightarrow0.
$$

Passing the polynomial pairings to this limit proves (4).
The factor $2\pi$ follows from the explicitly normalized kernel, independently of the historical $\Phi$ notation in Section 2.

## Verification and Limits

All assigned source paragraphs were read, and every displayed formula on PDF pp. 4-9 was visually inspected on 2026-09-08.
The tensor-cut convention, $L^1$ approximation, adjoint identity, first-order algebraic-freeness interface, perturbation coefficient and weighted Hilbert convergence were reconstructed as recorded.
The exact standard Hilbert-transform interface is primary-statement-checked; the full Stein-Weiss book and Tao's complete Calderon-Zygmund proof were not audited.
Source version/erratum searches are recorded in the integrated audit; this unit does not assert author confirmation of its typographical corrections.
On 2026-09-08, the separate external-input reviewer checked the first-order no-relations argument as a consumed interface and found no local issue.
The separate derivation-agent reviewer then checked the complete draft, the relevant rendered Voi98 formulas, and the exact Tao06 kernel, multiplier and boundedness interfaces.
The adjoint conventions, pair-counting factor, double-integral argument and weighted convergence passed that review with no unresolved local gap.
No numerical computation, formalization or external human review is claimed.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Voi98, the retained 39-page published journal article, printed pp. 189-227; printed page = PDF page + 188. Other works retain their separate exact versions and inspection limits in the body. |
| source-locator | Section 3, Definition 3.1 through Proposition 3.5, printed pp. 192-197 / PDF pp. 4-9. |
| inspection | 2026-09-08: L1 uniqueness, L2 adjoint characterization, the first-order no-relations argument, perturbation coefficient and scalar Hilbert realization reconstructed and separately reviewed. The exact harmonic-analysis interface is accepted after primary-statement checks; the full Stein-Weiss book and complete Calderon-Zygmund proof were not audited. |
