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

## Additional retained definition source recheck

<a id="voi98-definition-recheck"></a>


It retains the exact source-definition/convention content, already sufficient linked U homes, actual primary and visual locators, original reader roles and unreviewed-proof limits.
The earlier unit proof review does not retrospectively cover this later definition-reading event.
References to unchanged files and a sidecar describe the original checkpoint; this maintenance performs no source reopening, new proof review or stronger historical attribution.

Date: 2026-09-10.
Reviewer: the selfadjoint-interface agent.
This definition-review sidecar supplements the existing [Voi98 audit](readme.md); it allocates no source-unit or claim identifier and changes no original audit.
The source is the registered 39-page [published PDF](../../../literature/pdf/Voi98.pdf).
Printed page = one-based PDF page + 188.
The passages identified below were freshly checked against that PDF; decisive displays in Definitions 3.1, 5.1, 5.14, 6.1 and 7.1 were also visually checked.
This verifies definitions and convention boundaries, not every cited proof or historical priority.

<a id="difference-quotients-and-closure"></a>
## Difference Quotients, Iterates and Closure

Exact source: Section 3, printed pp. 192-194 / PDF pp. 4-6; Corollary 4.2, printed p. 203 / PDF p. 15, and Proposition 4.3, printed p. 204 / PDF p. 16.
Existing homes: [U002, setting and iterated quotient](Yin_U002_v1.md#setting-and-the-iterated-difference-quotient) and [U004, adjoint domains and closability](Yin_U004_v1.md#adjoint-domains-and-closability-41-43).

In a finite tracial von Neumann algebra, let \(B\) be a unital star-subalgebra and \(X=X^*\) algebraically free from \(B\).
The evaluated derivation on \(A=B[X]\) is determined by

\[
\partial X=1\otimes1,\qquad \partial B=0,\qquad
\partial(ab)=(a\otimes1)\partial b+(\partial a)(1\otimes b).
\]

The tensor product here is algebraic, with outer bimodule actions.
The formal polynomial quotient can be written before evaluation; descent to an evaluated algebra and its use as a Hilbert-space operator require the indicated well-definedness.
The source's \(\widetilde\partial\) has the same underlying vector values in \(A\otimes A^{\mathrm{op}}\), with the different product \((a\otimes b^{\mathrm{op}})(c\otimes d^{\mathrm{op}})=ac\otimes(db)^{\mathrm{op}}\).
Its action on a vector is \(a\xi b\).
This is a tensor convention, not permission to identify the two multiplications.

The unscaled iterates satisfy \(\partial^{(1)}=\partial\) and \(\partial^{(p+1)}=(\partial\otimes\mathrm{id}^{\otimes p})\partial^{(p)}\); in particular \(\partial^{(2)}X^2=1\otimes1\otimes1\), without a factorial.
When the densely defined \(L^2(W^*(A))\to L^2(W^*(A))\otimes_2L^2(W^*(A))\) operator is closable, \(\overline\partial\) denotes its graph closure.
Corollary 4.2 supplies closability when \(1\otimes1\in\operatorname{Dom}\partial^*\); this is a cited result, not an extra clause in the algebraic definition.
The domain of a closure is not automatically all bounded elements.

## Conjugate Variables

Exact source: Definition 3.1 and Lemma 3.3, printed p. 194 / PDF p. 6.
Existing home: [U002, Definition 3.1 and Remarks 3.2](Yin_U002_v1.md#definition-31-and-remarks-32).
For integer \(p\geq1\), the source defines \(\mathcal J_p(X:B)\) as a vector \(\xi\in L^1(W^*(B[X]))\) satisfying

\[
\tau(\xi a)=\tau^{\otimes(p+1)}(\partial^{(p)}a),\qquad a\in B[X].
\]

The first-order notation is \(\mathcal J=\mathcal J_1\).
The source definition is in \(L^1\); \(L^2\) membership is an additional integrability condition used for Fisher information and adjoints.
Lemma 3.3 supplies the known adjoint characterization \(\mathcal J_p=(\partial^{(p)})^*1^{\otimes(p+1)}\) in the \(L^2\) case.
No new project claim is needed to use this equivalence.
Changing the coefficient algebra or derivative order specifies parameters of this relative construction, rather than separately registered definitions.
The existing audit records the missing codomain factor in Lemma 3.3(iii) and the product-of-traces reading of Remark 3.2(b).

<a id="bounded-dual-systems"></a>
## Bounded Dual Systems and General Representations

Exact source: Definition 5.1, printed p. 208 / PDF p. 20, and Definition 5.14, printed p. 213 / PDF p. 25.
Existing home: [U005, Definitions 5.1-5.4](Yin_U005_v1.md#definitions-and-scope-51-54), with the separate 5.14 discussion later in that unit.
For bounded selfadjoint \(X_1,\ldots,X_n\in M\), a source dual system is a tuple of **bounded selfadjoint** \(Y_j\in B(L^2(M,\tau))\) with

\[
[b,Y_j]=0\quad(b\in B),\qquad [X_j,Y_k]=i\delta_{jk}P_\Omega.
\]

There is no requirement \(Y_j\Omega=0\), and no general unbounded-domain convention in Definition 5.1.
Definition 5.14 uses the same bounded selfadjoint relations in a Hilbert space with a unit trace vector \(\xi\) for \(B[X]\), replacing \(P_\Omega\) by \(P_\xi\).
The following assertion that the cyclic subspace automatically reduces the \(Y_j\) is not part of the definition and retains the counterexample and compression repair in U005.

The project's convention \([D_i,X_j]=\delta_{ij}P_\Omega\), often with nonsymmetric \(D_i\), must be stated explicitly.
For a source dual, \(D_i=iY_i\) has that commutator sign, but it is not thereby vacuum-normalized.
The selfadjoint-coordinate conversion from arbitrary bounded project duals is already recorded in [Dab10-U001](../Dab10/Yin_U001_v1.md#conversion-from-the-projects-bounded-dual-convention); it is a conversion of hypotheses, not a new meaning of Definition 5.1.

<a id="fisher-information"></a>
## Relative Fisher Information

Exact source: Definition 6.1, printed pp. 213-214 / PDF pp. 25-26.
Existing home: [U006, exact definition](Yin_U006_v1.md#setting-and-exact-definition).
For a selfadjoint tuple \(X\), put \(B_j=B[X_1,\ldots,\widehat X_j,\ldots,X_n]\).
Then

\[
\Phi^*(X:B)=\sum_{j=1}^n\|\mathcal J(X_j:B_j)\|_2^2
\]

when all those conjugates exist in \(L^2\), and \(+\infty\) otherwise.
The old scalar heat-derivative quantity discussed in Section 2 and the later \(\Phi^*\) must not be interchanged; [U001](Yin_U001_v1.md#the-two-entropy-constructions-and-the-scalar-constants) records the factor-two normalization and the defective introductory cubic-density coefficient.
The source's Fock fields \((l(h)+l(h)^*)/2\) have variance \(\|h\|^2/4\), unlike the variance-one q-Gaussian convention in MS23.

<a id="relative-nonmicrostates-entropy"></a>
## Relative Non-Microstates Free Entropy

Exact source: Definition 7.1, printed pp. 222-223 / PDF pp. 34-35.
Existing home: [U008, definition and integral](Yin_U008_v1.md#definition-and-existence-of-the-integral).
For a free variance-one semicircular family \(S\) free from \(B[X]\), the definition is

\[
\chi^*(X:B)=\frac12\int_0^\infty
\left(\frac{n}{1+t}-\Phi^*(X+\sqrt tS:B)\right)dt
+\frac n2\log(2\pi e).
\]

The source explicitly distinguishes this relative colon from microstates entropy “in the presence of” an algebra.
The integral has the extended-value interpretation established in the existing U008 audit; the definition alone does not identify microstates and non-microstates entropy.

## Remaining Source Conventions and Outcome

The smooth graph norms and projective coefficient norms of Section 4 remain source-local constructions, with precise homes in [U004](Yin_U004_v1.md#voi98-u004), printed pp. 205-207 / PDF pp. 17-19.
The distinction between an abstract completion and its operator image, the \(p+1\) tensor factors for \(\partial^{(p)}\), and the repaired coefficient norm remain as audited there; this sidecar does not promote the unrestricted higher-completion identification.
No new definition correction beyond those already recorded was found in the rechecked passages.
Suitable citation purposes are “current formulation” or “standard” for Definitions 3.1, 5.1, 6.1 and 7.1, and “notation” for derivative/tensor conventions; no historical-origin claim is made.
