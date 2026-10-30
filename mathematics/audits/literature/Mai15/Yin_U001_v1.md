---
author: Yin
---

# Mai15: The actual adjoint domain of a general derivation

## Mai15-U001

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [Mai15, retained arXiv:1512.07593v2](../../../literature/pdf/Mai15--arxiv-v2.pdf), revised 7 March 2016, 44 pages; the preprint identified in the registry (private lookup: `../../../literature/registry.md#mai15-source-artifact`). Printed and PDF page numbers agree. |
| source-locator | Remark 3.4, p.13; Definition 4.1, p.22; Section 4.1, Lemma 4.3 and its proof, pp.23–24; Definition 4.4 and Lemma 4.6, pp.24–25; Lemma 4.7 and its proof, pp.25–26. Definition 4.8 and the statement of Theorem 4.9, p.26, were checked only to delimit the stronger estimates. |
| inspection | 2026-10-16T00:47, AI source reader for Yin: direct statement and hypothesis checks in the retained PDF; both adjoint pairings in Lemma 4.3 and the two parts of Lemma 4.7 were checked, with Lemma 4.6's displayed identities as supporting input. This is selected source reading and self-review, not an independent review or a full-paper audit. Theorem 4.9's proof and the Wigner-chaos results are outside this unit's review. |

### Setting and notation

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal tracial state, and let $H=L^2(M,\tau)$.
Definition 4.1 takes a complex-linear derivation
\[
 \delta:\mathcal A\subset H\longrightarrow H\bar\otimes H,
\]
where $\mathcal A=\operatorname{Dom}\delta$ is a weakly dense unital $*$-subalgebra of $M$.
The bimodule actions are the outer actions
\[
 a\cdot(\eta\otimes\zeta)\cdot b=(a\eta)\otimes(\zeta b),
\]
and the product rule holds for all $a,b\in\mathcal A$.
The source uses $\odot$ for an algebraic tensor product and $\otimes$ for this Hilbert space tensor product; this unit writes the latter as $\bar\otimes$.
The values of $\delta$ need not lie in $\mathcal A\odot\mathcal A$.

Weak density makes $\mathcal A$ dense in $H$, so $\delta^*$ is the actual Hilbert space adjoint.
Membership of $u$ in $\operatorname{Dom}\delta^*$ means that pairing $\delta(a)$ with $u$ is represented by an $H$-vector for every $a\in\mathcal A$.
It is not a merely formal integration-by-parts identity on free words before evaluation.
We use $\langle a,b\rangle=\tau(b^*a)$, linear in the first variable, consistently with the source's adjoint pairings.

For $u\in M\odot M$, Remark 3.4 defines $u\mathbin{\#}\eta$ by linear extension of
\[
 (a\otimes b)\mathbin{\#}\eta=a\cdot\eta\cdot b.
\]
Each such multiplier is bounded on $H\bar\otimes H$.
The involution $*$ on this Hilbert space is componentwise, whereas
\[
 (a\otimes b)^\dagger=b^*\otimes a^*
\]
also flips the factors.
This distinction matters in the formulas below.

### Lemma 4.3: multiplication in the actual adjoint domain

For every $u\in\operatorname{Dom}\delta^*\cap(M\odot M)$ and $x\in\mathcal A$, the source asserts $x\cdot u,u\cdot x\in\operatorname{Dom}\delta^*$ and
\[
\begin{aligned}
 \delta^*(x\cdot u)
 &=x\delta^*(u)-(\tau\otimes\mathrm{id})
       \bigl(u\mathbin{\#}\delta(x^*)^*\bigr),\\
 \delta^*(u\cdot x)
 &=\delta^*(u)x-(\mathrm{id}\otimes\tau)
       \bigl(u\mathbin{\#}\delta(x^*)^*\bigr).
\end{aligned}
\tag{1}
\]
In particular, $a\cdot u\cdot b\in\operatorname{Dom}\delta^*$ for all $a,b\in\mathcal A$.
Neither assertion assumes that $\delta$ is real.

The proof on p.24 was read and its two adjoint tests checked.
For $y\in\mathcal A$, the product rule expands $x^*\delta(y)$ through $\delta(x^*y)$ and expands $\delta(y)x^*$ through $\delta(yx^*)$.
Pairing the first terms with $u$ uses the given $\delta^*(u)$; pairing the remaining terms produces the two partial traces in (1).
The resulting vectors belong to $H$: multiplication by $x$ is bounded, the $\#$ multiplier has bounded algebraic coefficients, and both partial traces are bounded contractions on the Hilbert space tensor product.
Thus each pairing is bounded in $\|y\|_2$, which proves actual adjoint-domain membership as well as the formulas.
Iteration is legitimate because $x\cdot u$ and $u\cdot x$ still belong to $M\odot M$.

### Lemma 4.7: the vacuum assumption without reality

Assume
\[
 1\otimes1\in\operatorname{Dom}\delta^*,
 \qquad \xi=\delta^*(1\otimes1)\in H.
\]
The first assertion of Lemma 4.7 is
\[
 \mathcal A\odot\mathcal A\subseteq\operatorname{Dom}\delta^*.
\tag{2}
\]
The first paragraph of its proof on p.26 explicitly separates (2) from the later reality assumption.
It follows by applying Lemma 4.3 twice to $1\otimes1$ and taking finite sums.

Combining those same two source formulas gives the following elementary-tensor form, with the stars retained:
\[
 \delta^*(a\otimes b)
 =a\xi b
  -(\tau\otimes\mathrm{id})\bigl(\delta(a^*)^*\bigr)b
  -a(\mathrm{id}\otimes\tau)\bigl(\delta(b^*)^*\bigr),
 \qquad a,b\in\mathcal A.
\tag{3}
\]
Equation (3) is a direct combination of Lemma 4.3, rather than the source's reality-dependent simplified formula.
As an immediate operator-theoretic consequence of (2), $\delta^*$ is densely defined and $\delta$ is closable.
This uses density of $\mathcal A\odot\mathcal A$ in $H\bar\otimes H$ and the usual Hilbert space adjoint criterion.
It does not assert that this algebraic tensor domain is a core for $\delta^*$.

### The stronger formulas and estimates

Definition 4.4 calls $\delta$ real when $\delta(x^*)=\delta(x)^\dagger$ for every $x\in\mathcal A$.
Under this additional assumption, Lemma 4.6 converts (3) into the elementary-tensor case of Lemma 4.7's formula (4.7):
\[
 \delta^*(a\otimes b)
 =a\xi b-(\mathrm{id}\otimes\tau)\delta(a)\,b
          -a(\tau\otimes\mathrm{id})\delta(b).
\tag{4}
\]
The passage from (3) to (4) was checked using the flip and componentwise involution separately.
Without reality, (4) is not the formula established by this source.

Definition 4.8 additionally requires both $\delta(\mathcal A)\subseteq\mathcal A\odot\mathcal A$ and
\[
 (\delta\otimes\mathrm{id})\delta
   =(\mathrm{id}\otimes\delta)\delta
\]
for coassociativity.
Theorem 4.9 assumes reality, this coassociativity condition, and the vacuum-adjoint assumption.
Its statement on p.26 bounds $\delta^*(x\otimes1)$ and $\delta^*(1\otimes x)$ in $L^2$ by $\|\xi\|_2\|x\|$, and bounds either partial-trace contraction of $\delta(x)$ by $2\|\xi\|_2\|x\|$.
Only these hypotheses and displayed statements were checked here; the proof of those estimates was not reviewed for this unit.
They cannot be imported under the vacuum assumption alone.

### Relation to the general starred-polynomial hypothesis

For bounded generators $X_1,\ldots,X_d$ of $M$, put $\mathcal A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle$.
If actual outer derivations $\partial_i$ on this represented algebra satisfy $\partial_i(X_j)=\delta_{ij}1\otimes1$ and $1\otimes1\in\operatorname{Dom}\partial_i^*$, then (2) and (3) apply to each $\partial_i$.
The derivations must respect all relations already present in this algebra; their values on $X_j^*$ are not independently prescribed by these hypotheses.
No normality or reality assumption on this tuple is needed for the adjoint-domain conclusion.
Replacing this domain by $\mathbb C\langle X_1,\ldots,X_d\rangle$ alone does not in general supply the weakly dense star domain required in Definition 4.1.

[ACSY24-U003](../ACSY24/Yin_U003_v1.md#derivation-adjoint-and-compression) records the corresponding general adjoint formula, and ACSY24 Lemma 3.3 cites Mai15 Lemma 4.3.
The construction of a closable dual and the maximal-$\Delta$ conclusion belong to ACSY24 Theorem 3.4 and Proposition 3.5, with their separate checked domain argument in [ACSY24-U001](../ACSY24/Yin_U001_v1.md#acsy24-u001).
This unit supplies the primary-source adjoint interface and attribution; it adds no theorem asserting full-$M$ domains for those duals, finite Fisher information for a $2d$-tuple of real and imaginary parts, or a general rationality criterion.

### Search and verification limits

The source was located by following ACSY24 Lemma 3.3 to its cited Lemma 4.3 and then checking the primary arXiv record and PDF.
The retained v2 was read again at the stated pages after acquisition.
The arXiv record identifies v1 as 23 December 2015 and v2 as 7 March 2016, and lists no journal reference.
A bounded exact-title and author search did not establish a journal edition; publication and acquisition facts remain in the registry rather than being inferred from this unit.
No complete comparison with another edition, exhaustive errata search, full-paper proof review, independent review, or formal verification is claimed.
