---
author: Yin
---

# Dense Adjoint Domains and Closability

## Bla06-U001

Source: [Bla06, author-hosted revision](../../../literature/pdf/Bla06--author-2017.pdf), dated 8 February 2017.
The canonical bibliography identifies the Springer 2006 monograph; the inspected pages belong to this author revision, not a separately compared print copy.

Locator: Definition I.7.2.1, printed p.30 / PDF p.38; Definition I.7.2.2 and Proposition I.7.2.3 with its proof, printed p.31 / PDF p.39.

Record: 2026-10-12, direct text reading and visual inspection of p.31 by the authoring AI agent for Yin.
Reading coverage: Audited within scope; self-review, with no independent reviewer.

### Statement and hypotheses

For a densely defined linear operator $T$ on a Hilbert space $H$, the domain of $T^*$ is dense if and only if $T$ is closable.
In that case $T^{**}=\overline T$.
Definition I.7.2.2 calls density of $\operatorname{Dom}T^*$ adjointability.
Definition I.7.2.1 defines closability by a closed extension, equivalently by the graph closure being an operator graph.

### Proof mechanism and inspection

Let $\Gamma(S)$ denote an operator graph and let $V(\xi,\eta)=(\eta,-\xi)$.
Directly from the adjoint definition,
$$\Gamma(S^*)=[V\Gamma(S)]^\perp.$$
Thus adjoints are closed.
If $T^*$ has dense domain, $T^{**}$ is a closed extension of $T$, establishing closability.
Blackadar states this direction immediately before the proposition; the displayed graph identity in its proof also justifies the closedness assertion.

For the reverse direction, the source reduces to closed $T$.
Since $V$ is unitary and $V^2=-I$, it obtains $[V\Gamma(T^*)]^\perp=\Gamma(T)$.
A vector orthogonal to $\operatorname{Dom}T^*$ would then produce a vertical vector $(0,\eta)$ in $\Gamma(T)$, so it must vanish.
The same identity gives $T^{**}=T$.
For closable $T$, the reduction uses $(\overline T)^*=T^*$, as follows by continuity of the adjoint pairing along graph limits.
These steps and the reduction were checked locally.

Retained background: Hilbert-space orthogonal complements and bounded unitary maps; no independent audit of their foundational proofs.
Only the specified definitions and criterion were reviewed, with no computation or formal verification.
The author-hosted errata were searched for the relevant section; no correction to I.7.2.3 was located.
The 2006 print text was not compared page by page with the 2017 revision.

### Restriction to a dense subspace and citation correction

Let $\mathcal M$ be a finite von Neumann algebra with faithful normal tracial state $\tau$, put $H=L^2(\mathcal M,\tau)$, and write $\Omega=1\in H$.
Suppose $D_i$ is densely defined on $H$ and $\mathcal M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*$.
Then $D_i^{\circ}=D_i|_{\mathcal M\Omega}$ is densely defined and restriction reverses adjoint inclusion.
Consequently
$$\mathcal M\Omega\subseteq\operatorname{Dom}D_i^*\subseteq\operatorname{Dom}(D_i^{\circ})^*.$$
The leftmost space is dense, so the criterion applies.
It proves closability without a core or essential-adjointness assertion.

The earlier MS23 passage check identified a use of the criterion, rather than its proof.
Bla06 Proposition I.7.2.3 supplies a proof-bearing source.
The bounded search also located Peterson's operator-algebra notes, Proposition 4.1.6, as a proof-bearing alternative.
Search stopped after the classic monograph's statement, definitions, proof and applicability were verified.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Bla06, Springer 2006 monograph; author-hosted revision dated 8 February 2017, retained as Bla06--author-2017.pdf.

Passages: Definitions I.7.2.1--I.7.2.2 and Proposition I.7.2.3; printed pp.30--31 / PDF pp.38--39.

Inspection: Direct statement, definition and proof reading; visual check of p.31; criterion and dense-subspace restriction consequence self-reviewed on 2026-10-12.
No independent or whole-book audit; no print/revision comparison.
