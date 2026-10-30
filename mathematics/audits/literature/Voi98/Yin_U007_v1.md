---
author: Yin
---

# Continuity, semicircular regularization, and the classical comparison

<a id="voi98-u007"></a>

## Voi98-U007 — Fisher-information lower semicontinuity and heat bounds

- Source: [Voi98](../../../literature/pdf/Voi98.pdf), retained published journal version; shared bibliographic identity is in [references.bib](../../../literature/references.bib).
- Locator: Proposition 6.10, Lemma 6.11, Corollaries 6.12-6.14, and Remark 6.15; printed pp. 218-222 / PDF pp. 30-34.
- Record: 2026-09-08; local reconstruction and self-review by the BR10/Fisher-information agent; independent mathematical review by the derivations agent found no gap in the first-order chain or the higher-order chain with an algebraically free limit, as stated below.
- Kind and coverage: continuity and regularization mechanism.
  The first-order chain and the higher-order lemma under the explicitly stated limit-freeness hypothesis are audited within scope.
  The literal higher-order derivation claim at a possibly algebraically dependent limit retains the precise qualification below.
- Purpose: [Voi98 finite-Fisher source audit](readme.md#voi98-finite-fisher-source-audit); supplies the well-defined decreasing, right-continuous integrand and tail bounds needed for Section 7.

### Hypotheses and statements

Use the finite faithful normal tracial setting and notation in [Voi98-U006](Yin_U006_v1.md#voi98-u006).
All approximants and limits below are selfadjoint elements of a single \(M\), and coefficient algebra \(B\) is fixed.
If \(X_j^{(k)}\to X_j\) strongly for every \(j\), Proposition 6.10 asserts

\[
 \Phi^*(X:B)\le\liminf_{k\to\infty}\Phi^*(X^{(k)}:B).
\]

This is a sequential lower-semicontinuity statement for a fixed representation and tracial algebra.
It is not an assertion that arbitrary weak operator convergence, moment convergence without uniform boundedness, or changing coefficient algebras gives the same conclusion.

For Lemma 6.11 fix \(p\ge1\), set \(B_1^{(k)}=B[X_2^{(k)},\ldots,X_n^{(k)}]\), \(B_1=B[X_2,\ldots,X_n]\), and suppose the higher conjugates \(\eta_k=\mathcal J_p(X_1^{(k)}:B_1^{(k)})\) exist with \(\sup_k\|\eta_k\|_2\le C<\infty\).
Let \(H=L^2(W^*(B,X),\tau)\) and \(P_H=E_{B[X]}\).
The source conclusion is

\[
 P_H\eta_k\rightharpoonup\eta=\mathcal J_p(X_1:B_1),
\]

and if additionally \(\|\eta_k\|_2\to\|\eta\|_2\), then \(\eta_k\to\eta\) in \(L^2(M)\).
Here weak convergence is initially asserted for the **projected** vectors; it does not automatically hold for unprojected vectors without additional information.

For \(p=1\), the statement follows unconditionally from the source hypotheses by the repaired argument below.
For general \(p\), that argument always constructs the unique limit vector satisfying the formal higher-conjugate moment identities.
Identification with the source's derivation-defined \(\mathcal J_p\) uses the limit algebraic-freeness convention discussed below; it must not be silently supplied by strong convergence.

### Construct the limiting functional before naming its conjugate

Strong convergence of a sequence of bounded operators gives a uniform operator-norm bound by uniform boundedness.
Since the generators are selfadjoint, they converge strongly star as well.
A fixed noncommutative polynomial with coefficients in \(B\), and its adjoint, therefore converge strongly and are uniformly norm bounded.
In a finite von Neumann algebra this implies convergence in \(L^2(\tau)\).
For completeness, bounded strong-star convergence makes \(\tau((P_k-P)^*(P_k-P))\to0\) by normality and continuity of normal functionals on bounded strong-star sets.

For a formal polynomial expression \(Q\) in the tuple, the scalar

\[
 F_p(Q;X)=(\tau^{\otimes(p+1)})(\partial_1^{(p)}Q)(X)
\]

can be evaluated by its explicit finite tensor-cut formula even before a quotient derivation has been proved to exist.
It is a finite sum of products of moments of polynomial segments, and hence is the limit of \(F_p(Q;X^{(k)})\).
The approximant identities and the uniform conjugate bound give

\[
 |F_p(Q;X)|
 =\lim_k|\tau(\eta_kQ(X^{(k)}))|
 \le C\|Q(X)\|_2.
\]

Thus this functional vanishes on every expression evaluating to zero and descends to the evaluated polynomial algebra.
Different polynomial expressions for coefficients in \(B_1\) give the same tensor-cut scalar: only their evaluated coefficients and moments occur in those cuts.
The functional extends continuously to \(H\), giving a unique vector \(\eta\in H\) of norm at most \(C\) with \(\tau(\eta Q(X))=F_p(Q;X)\).
This is the existence step missing from the source's displayed argument, which starts by writing \(\mathcal J_p(X_1:B_1)\) before constructing it.

For every fixed polynomial \(Q(X)\), Cauchy-Schwarz yields

\[
 |\tau(\eta_k(Q(X^{(k)})-Q(X)))|
 \le C\|Q(X^{(k)})-Q(X)\|_2\longrightarrow0.
\]

Combining this with the moment identity proves convergence of \(\tau(P_H\eta_kQ(X))\) to \(\tau(\eta Q(X))\).
Polynomials are dense in **\(H\)**, and \(P_H\eta_k\) are uniformly bounded, so convergence holds against every vector of \(H\); it is weak convergence in \(L^2(M)\) too, because all these vectors lie in \(H\) and pairing with \(H^\perp\) is zero.

**Printed density error, p. 220:** the polynomial words need not be total in \(L^2(M)\).
For example, the ambient algebra may contain another free factor.
The correct generated subspace \(H\), together with the projection already present in the lemma, repairs the step.

### First-order algebraic freeness at the limit

The source defines the difference quotient on \(B_1[X_1]\) under algebraic freeness of \(X_1\) from \(B_1\).
This property is not preserved by arbitrary strong convergence, so it requires an argument when obtaining the first-order conjugate in Proposition 6.10.

The limit functional just constructed for \(p=1\) provides that argument.
Let \(\mathcal A=B_1*\mathbb C\langle x\rangle\) be the formal one-variable coefficient algebra, with evaluation \(\mathrm{ev}(x)=X_1\).
Suppose \(R\in\ker\mathrm{ev}\).
Apply the first-order moment relation to \(aRb\), for arbitrary formal polynomials \(a,b\).
The outer Leibniz terms contain the evaluated \(R=0\), and the left-hand trace vanishes.
Consequently

\[
 (\tau\otimes\tau)\bigl((a(X_1)\otimes1)
  (\mathrm{ev}\otimes\mathrm{ev})(\partial R)
  (1\otimes b(X_1))\bigr)=0.
\]

The test tensors are dense in \(H\otimes H\) and the trace is faithful, so \((\mathrm{ev}\otimes\mathrm{ev})(\partial R)=0\).
If a nonzero relation of minimal \(x\)-degree \(d\ge1\) existed, evaluation would be injective on the vector space of degree at most \(d-1\).
Its tensor square is then injective on the space containing \(\partial R\).
The formal derivative of a positive-degree nonzero polynomial cannot vanish: the component cutting the first occurrence of \(x\) in its highest-degree part is the corresponding nonzero coefficient tensor in bidegree \((0,d-1)\).
This contradicts the displayed vanishing.
Hence no relation exists, the difference quotient is well-defined at the limit, and the constructed vector is the source's \(\mathcal J(X_1:B_1)\).

This reasoning can be applied separately to every coordinate when proving Proposition 6.10.
It does not assume freeness in the probabilistic sense, and it does not require importing a later no-algebraic-relations theorem.

### Higher-order qualification in Lemma 6.11

For \(p>1\), the bounded formal moment functional and the projected weak convergence above are proved without any additional assumption.
If \(X_1\) is algebraically free from \(B_1\) at the limit, these are exactly the defining \(p\)-th conjugate identities in [Voi98-U002](Yin_U002_v1.md#voi98-u002), so the full higher-order lemma follows.

Without that limit assumption, the source proof does not establish that its quotient operator \(\partial_1^{(p)}\) exists.
The first-order relation argument cannot simply be reused: differentiating \(aRb\) \(p\) times produces additional terms involving intermediate derivatives of \(R\).
This audit has not proved that the existence of the limiting \(p\)-th formal moment representative alone forces the needed algebraic freeness or quotient-derivative property.
Accordingly, the unrestricted higher-order identification is **not promoted to a checked derivation statement** here.
This qualification does not affect Proposition 6.10, Corollaries 6.12-6.14, or the Section 7 entropy arguments, all of which use \(p=1\).
It is a limitation of the recorded proof, not a verified counterexample to the published higher-order claim.

### From projected weak convergence to strong convergence

Weak lower semicontinuity gives \(\|\eta\|_2\le\liminf\|P_H\eta_k\|_2\).
If \(\|\eta_k\|_2\to\|\eta\|_2\), contraction and this inequality force \(\|P_H\eta_k\|_2\to\|\eta\|_2\).
Orthogonal decomposition then gives

\[
 \|(1-P_H)\eta_k\|_2^2
 =\|\eta_k\|_2^2-\|P_H\eta_k\|_2^2\longrightarrow0.
\]

Weak convergence plus norm convergence in the Hilbert space \(H\) implies \(P_H\eta_k\to\eta\) strongly, and the orthogonal remainder proves \(\eta_k\to\eta\) in \(L^2(M)\).
Equivalently, the mixed inner product in \(\|\eta_k-\eta\|_2^2\) converges because \(\eta\in H\).
The penultimate norm formula on p. 220 misplaces the superscripts on \(X_1\) and \(B_1\); it must be the lemma's original norm-convergence assumption, not conjugates with mismatched coefficient algebras.

To prove Proposition 6.10, there is nothing to do when the liminf is infinite.
Otherwise select a subsequence whose information tends to the finite liminf; its coordinate conjugates are uniformly bounded.
Apply the \(p=1\) argument to each coordinate.
In the finite Hilbert direct sum, the vector of projected conjugates converges weakly to the limiting conjugate vector, whose squared norm is bounded by the liminf of the approximant squared norms.
This is the desired inequality, including existence of every limiting conjugate when the liminf is finite.

### Vanishing free perturbations: Corollaries 6.12-6.13

Suppose \(B[X]\) and \(C[Y^{(k)}]\) are free for every \(k\), and \(\|Y_j^{(k)}\|\to0\) for all \(j\).
Freeness already implies that \(C\) is free from \(B[X]\).
The lower-semicontinuity result with fixed coefficient algebra \(B\vee C\), followed by free extension, gives

\[
 \liminf_k\Phi^*(X+Y^{(k)}:B\vee C)
 \ge\Phi^*(X:B\vee C)=\Phi^*(X:B).
\]

The free-sum projection inequality from [Voi98-U006](Yin_U006_v1.md#voi98-u006) gives the reverse upper bound for every \(k\).
Thus the quantities converge to \(\Phi^*(X:B)\) in \((0,+\infty]\), with convergence to \(+\infty\) understood in the extended sense.
Norm convergence of the perturbations is more than needed for the lower-bound passage, but is the exact source hypothesis.

**Wrong cross-reference, p. 221:** Corollary 6.12 cites Lemma 6.7 for the liminf inequality.
The needed result is Proposition **6.10**; Lemma 6.7 is only the matrix chain rule.

For one variable, \(C=\mathbb C\), and finite \(\Phi^*(X:B)\), convergence of information gives convergence of the conjugate norms.
Lemma 6.11 with \(p=1\) then proves \(\|\mathcal J(X+Y^{(k)}:B)-\mathcal J(X:B)\|_2\to0\), which is Corollary 6.13.
No joint freeness between different perturbation indices is required.

### Semicircular heat regularization: Corollary 6.14

Let \(S_1,\ldots,S_n\) be a standard centered variance-one free semicircular family free from \(B[X]\).
Define

\[
 f(t)=\Phi^*(X_1+\sqrt t S_1,\ldots,X_n+\sqrt t S_n:B),
 \qquad C^2=\tau\Bigl(\sum_jX_j^2\Bigr).
\]

Then \(f:[0,\infty)\to(0,\infty]\) is nonincreasing and right-continuous, with extended right continuity allowed at \(t=0\).
For every \(t>0\),

\[
 \frac{n^2}{C^2+nt}\le f(t)\le\frac nt<\infty.
\]

For the semigroup step, freely adjoin a further standard family \(S'\).
The pairs \((B,X+\sqrt{t+\varepsilon}S)\) and \((B,X+\sqrt t S+\sqrt\varepsilon S')\) have the same joint tracial distribution: centered free semicircular covariances add, and the noise remains free from \(B[X]\).
Conjugate moment identities and their minimal \(L^2\) norms depend only on that joint distribution.
One may therefore compute the second information in this free-product extension without changing the first one.
The free-sum projection inequality proves monotonicity in \(t\), and Corollary 6.12 applied to \(\sqrt\varepsilon S'\) proves right continuity.
The perturbation norms are \(2\sqrt\varepsilon\), so the required norm convergence holds.

Freeness and centering give exactly \(\sum_j\|X_j+\sqrt t S_j\|_2^2=C^2+nt\), including noncentered \(X\).
Cramer-Rao gives the lower bound.
Applying the free-sum projection inequality from the noise side gives the upper bound, because its conjugates are \(S_j/\sqrt t\) and its information is \(n/t\).
The source's displayed \(nt^{-1}\) is a finite estimate only for \(t>0\).
At \(t=0\) and \(C^2=0\), use the separately recorded infinite-information case rather than an undefined fraction or product.

These bounds and right continuity are precisely the inputs needed for the entropy integral.
No continuity from the left or finite information of the unsmoothed tuple is asserted.

### Classical comparison: Remark 6.15

Let \(p\) be a smooth compactly supported probability density on \(\mathbb R^n\).
Polynomial functions are dense in \(L^2(p\,dx)\): their restrictions separate points of the compact support and are uniformly dense in continuous functions there; continuous functions are dense in this finite-measure \(L^2\) space.
The polynomial representation is faithful because a nonzero continuous density is positive on a nonempty open set, and a polynomial vanishing there is identically zero.

For the polynomial differentiation operator \(D_j=\partial/\partial x_j\), integration by parts with the compactly supported smooth density has no boundary term:

\[
 \int D_jq\,p\,dx=-\int q\,\partial_jp\,dx.
\]

Thus, provided the score \(-\partial_jp/p\) belongs to \(L^2(p\,dx)\), it represents \(D_j^*1\).
The quotient is defined on \(\{p>0\}\) and arbitrarily on the \(p\,dx\)-null complement.
Since a smooth nonnegative function has zero first derivative at its zero points, this convention also agrees with the usual integral of \(|\nabla p|^2/p\), interpreted through its positive set.
Summing yields

\[
 \sum_j\|D_j^*1\|_{L^2(p\,dx)}^2
 =\int_{\{p>0\}}\frac{|\nabla p|^2}{p}\,dx.
\]

This verifies the source's limited adjoint representation of classical Fisher information.
It does not identify a free difference quotient with an ordinary derivative, or establish equality between classical and free information for general laws.

### Verification facts and downstream boundary

All five local source pages were read in extracted text and rendered form on 2026-09-08.
The limit functional, density repair, first-order relation argument, Hilbert-space convergence, vanishing-noise squeeze, semigroup step, heat bounds, and classical integration-by-parts identity were reconstructed.
The derivations agent independently reviewed the unit and found no gap in the first-order chain or the higher-order chain with an algebraically free limit.
No finite computation, proof assistant, or external human review was performed.
The source's general higher-order lemma remains subject to the explicit quotient/freeness qualification above; consumers using only first-order information do not inherit that unresolved higher-order obligation.
Local typographical repairs are not claimed to be author-confirmed errata.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Voi98, the retained 39-page published journal article, printed pp. 189-227; printed page = PDF page + 188. Other works retain their separate exact versions and inspection limits in the body. |
| source-locator | Proposition 6.10, Lemma 6.11, Corollaries 6.12-6.14 and Remark 6.15, printed pp. 218-222 / PDF pp. 30-34. |
| inspection | 2026-09-08: first-order limit existence, lower semicontinuity, vanishing noise and heat bounds reconstructed and independently reviewed. For higher order the formal limit vector is constructed and source derivation identification is checked with an algebraically free limit; the unrestricted higher-order quotient interpretation remains unestablished. First-order consumers do not inherit that unresolved higher-order obligation. |
