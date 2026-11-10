---
author: Yin
---
# Complex-coefficient Atiyah conjecture: known results and route boundaries

Date: 2026-11-10.
This synthesis serves the [exact torsion-free complex-coefficient contract](../tasks/Yin_T_A0001_v1.md#contract).
The responsible main agent combined separate classical-source, recent-source and strategy inspections for Yin.
The work covers theorem statements, hypotheses, source versions and bounded feasibility checks; it is not a proof audit or a solution of the Task.

## Formulation and algebraic interface

Write \(SA_{\mathbb C}(G)\) for the Task's integrality assertion for every finite matrix over \(\mathbb CG\), with unnormalized matrix trace.
Every matrix has support in a finitely generated subgroup, so the Task's stated subgroup reduction suffices for arbitrary discrete groups.
For torsion-free \(G\), the central algebraic interface is
\[
SA_{\mathbb C}(G)
\quad\Longleftrightarrow\quad
D_{\mathbb C}(G)\subseteq\mathcal U(G)\text{ is a division ring},
\]
where \(D_{\mathbb C}(G)\) is the division closure in the affiliated-operator ring.
This is [LL18, Theorem 2.3(3), arXiv v3, printed p.10](https://arxiv.org/pdf/1602.06906v3#page=10).
An embedding of \(\mathbb CG\) into an unrelated abstract division ring does not by itself identify the canonical analytic matrix rank.

## Known positive results

All conclusions in the following table concern complex coefficients.
For statements allowing torsion, only the torsion-free consequence is used here.

| Class or operation | Scope relevant to the Task | Inspected primary locator |
| --- | --- | --- |
| Linnell's class \(\mathcal C\) | Every torsion-free member satisfies the conjecture; the class starts with free groups and is closed under directed unions and extensions with elementary amenable quotient. | [LL18, Theorem 2.3(4), v3 p.10](https://arxiv.org/pdf/1602.06906v3#page=10) |
| Locally indicable groups | Every such group satisfies the conjecture, without a sofic assumption; this includes torsion-free one-relator groups. | [JZLA20, Theorem 1.1 and Corollary 1.3, v4 pp.2–3](https://arxiv.org/pdf/1810.12135v4#page=2) |
| Schick's class \(\mathcal D\) | The earlier algebraic-coefficient theorem has already been upgraded to \(\mathbb C\); residual torsion-free elementary amenable examples are covered. | [JZ19, Corollary 1.2(1), author manuscript p.4](https://verso.mat.uam.es/~andrei.jaikin/preprints/sac.pdf) |
| Geometric and pro-\(p\) examples | Artin braid groups, torsion-free finite extensions of compact special cube complex groups, and torsion-free \(p\)-adic analytic pro-\(p\) groups are covered. | [JZ19, Corollary 1.2(2)–(4), author manuscript p.4](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf) |
| Three-manifold groups | Every torsion-free three-manifold fundamental group is covered, without restricting to compact manifolds; all three-manifold groups belong to \(\mathcal C\). | [KL24, Theorem 1.4 and Corollary 1.5(1), v3 p.2](https://arxiv.org/pdf/2303.15907v3#page=2) |
| Graphs of groups with finite edge groups | The countable theorem assumes strong Atiyah for the vertices over a conjugation-closed coefficient field and bounded finite-subgroup orders; in the torsion-free setting the edges are trivial, yielding free products. | [SP25, Theorem 1.1, v2 §1](https://arxiv.org/html/2409.12268v2#S1) |
| Selected finite-index subgroups of outer automorphism and mapping class groups | FN26 proves the complex-coefficient conjecture for certain torsion-free finite-index subgroups, including ones in \(\operatorname{Out}(A_\Gamma)\) for finite-graph RAAGs; the full groups are only asserted to satisfy the weak conjecture. | [FN26, Theorem 1.3, v1 §1.1](https://arxiv.org/html/2606.19606v1#S1.SS1) |

Locally indicable means that each nontrivial finitely generated subgroup maps onto \(\mathbb Z\).
The class \(\mathcal C\) row includes torsion-free elementary amenable and free-by-elementary amenable groups.
The free-group source inspection already retained at [Lin00/Yin_U004](../audits/literature/Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate) remains usable at its documented depth.
FN26 is a June 2026 preprint; no journal publication was located in this search.

## Coefficients and permanence

For a fixed group, the implications from \(\mathbb C\) to \(\overline{\mathbb Q}\) to \(\mathbb Q\) are immediate restrictions of the allowed matrices.
The reverse coefficient implication is not formal.
For sofic groups, [JZ19, Theorem 1.1, author manuscript p.4](https://verso.mat.uam.es/~andrei.jaikin/preprints/sac.pdf) proves the upgrade from \(\overline{\mathbb Q}\) to \(\mathbb C\).
Thus a route whose entire objective is that upgrade for \(\mathcal D\) or the listed geometric examples would repeat known coverage.
The earlier \(\overline{\mathbb Q}\)-coefficient result for \(\mathcal D\) appears in [DLM+03, Theorem 1.4, arXiv v3](https://arxiv.org/pdf/math/0107049v3); it is historical context for this upgrade, without a new proof audit here.

Subgroups and directed unions preserve the torsion-free conjecture.
The corrected [Sch00, arXiv v4, Propositions 2.2–2.3 and Corollary 3.2](https://arxiv.org/pdf/math/0001101v4) also gives extension permanence for a torsion-free elementary amenable quotient.
An elementary amenable quotient with finite subgroups requires the theorem's additional control of their preimages.
Remark 1.1 records an unfixable gap in an earlier version and removal of the results depending on it.
The appended erratum restricts the relevant approximation extension to a normal subgroup extension.
Its old abstract is therefore unsuitable evidence for stronger permanence claims.

General ascent from a finite-index subgroup to a torsion-free overgroup remains an explicit gap in [FN26, §1.1](https://arxiv.org/html/2606.19606v1#S1.SS1).
[LS07, Theorem 4.60 and Corollary 4.62, v5 p.34](https://arxiv.org/pdf/math/0403229v5#page=34) supplies substantial positive cases using finite classifying spaces, cohomological completeness and enough torsion-free quotients.
These are benchmark hypotheses to weaken, not assumptions to omit.
For finite index \(d\), restriction to the subgroup multiplies von Neumann dimension by \(d\), so subgroup integrality directly gives only the lattice \(\frac1d\mathbb Z\).

## Finite-extension probe

Assume \(H\triangleleft G\), \(G/H\) finite, \(G\) torsion-free and \(SA_{\mathbb C}(H)\).
A candidate bridge is to prove that the induced crossed product \(D_{\mathbb C}(H)*(G/H)\) realizes the relevant analytic division closure and is a division ring.
The embedding and closure comparison must be checked in the actual affiliated-operator setting.

For an index-two extension, put \(D=D_{\mathbb C}(H)\), choose \(t\notin H\), and write
\[
td=\alpha(d)t,\qquad t^2=h\in H,\qquad D*(G/H)=D\oplus Dt.
\]
The direct calculation
\[
(t-\alpha(b))(t+b)=h-\alpha(b)b
\]
holds for \(b\in D\).
Thus a solution of \(\alpha(b)b=h\) produces nonzero factors with zero product in the crossed product.
If \(b\in H\), then
\[
(b^{-1}t)^2=b^{-1}\alpha(b)^{-1}h=1,
\]
contradicting torsion-freeness.
The unresolved issue is whether rational elements \(b\in D\) can behave differently.
This self-checked algebraic probe neither excludes such solutions nor establishes a complete division criterion.
A resulting obstruction in the actual analytic closure would need a fully verified passage to a finite group-ring matrix before it could be a Task counterexample.

## Infinite-edge probe

For \(G=A*_C B\), use the source's \(*\)-regular closures and set
\[
R=\mathcal R_{\mathbb C[A]}
  *_{\mathcal R_{\mathbb C[C]}}
  \mathcal R_{\mathbb C[B]}.
\]
[SP25, Conjecture 7.1, v2 §7](https://arxiv.org/html/2409.12268v2#S7) singles out
\[
\operatorname{Tor}_1^{R}(\mathcal U(G),\mathcal U(G))=0
\]
when the edge regular closure is a universal localization of \(\mathbb C[C]\).
The proposed initial case is \(C\cong\mathbb Z\), whose scalar rational model is explicit.
One must still identify the missing finite-edge proof step and prove its replacement, then verify the implication to the desired regular/division closure.
Exact Tor vanishing and vanishing of von Neumann dimension are different targets.
No theorem for arbitrary infinite-edge amalgams is inferred here.

## Approximation probe

Let marked torsion-free groups \(G_i\) converge to \(G\), and let \(A_i\) and \(A\) be obtained from the same finite word matrix with fixed complex coefficients.
If each \(SA_{\mathbb C}(G_i)\) holds and their kernel dimensions converge to that of \(A\), then the limit is an integer, since the approximating dimensions belong to \(\{0,\ldots,n\}\).
Two premises need evidence: existence of the proposed approximating family and convergence of rank.

Known convergence should be reused first.
[JZ19, Corollary 1.4, author manuscript p.5](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf) covers marked approximations whose approximating groups are sofic.
[JZLA20, Theorem 1.5 and §7, v4](https://arxiv.org/pdf/1810.12135v4#page=4) covers virtually locally indicable target groups.
Consequently the sofic integer-rank approximant case is already a conditional permanence consequence, not a new analytic estimate to prove.

Outside an applicable rank theorem, a sufficient additional estimate for the spectral measures \(\mu_i\) of \(A_i^*A_i\), together with their weak convergence, is
\[
\lim_{\varepsilon\downarrow0}\sup_i\mu_i((0,\varepsilon))=0.
\]
This prevents nonzero spectral mass from collapsing into the zero atom.
Weak convergence alone is inadequate: in a finite tracial algebra with a projection \(p\) of trace \(1/2\), the operators \(p+\varepsilon(1-p)\) are invertible for \(\varepsilon>0\) but converge to \(p\), whose kernel has dimension \(1/2\).
This is a method obstruction in a general finite algebra, not a torsion-free group-ring counterexample.
Approximating only by finite groups instead supplies lattices \(|G_i|^{-1}\mathbb Z\) with growing denominators and does not force integrality.

## Relation-sensitive analytic probe

For a bounded tuple \(X\) in a finite von Neumann algebra \(M\) with faithful normal normalized trace, put \(A_X=\mathbb C\langle X\rangle\), the evaluated algebra, and take both closures in \(\mathcal U(M)\):
\[
R_X=\operatorname{Rat}_{\mathcal U(M)}A_X,\qquad
D_X=\operatorname{Div}_{\mathcal U(M)}A_X.
\]
The retained [MSY23, Theorem 5.25 inspection](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) gives the exact equivalence
\[
\text{every polynomial matrix in }X\text{ has integer analytic rank}
\quad\Longleftrightarrow\quad
R_X\text{ is a division ring}
\quad\Longleftrightarrow\quad
D_X\text{ is a division ring}.
\]
Ranks here use unnormalized matrix trace.
Under these equivalent conditions \(R_X=D_X\), and analytic matrix rank agrees with inner rank over this actual closure.
No algebraic freeness of \(X\), free-field realization or maximal free dimension is a hypothesis of this equivalence.
The same source's Example 5.24 distinguishes this property from the stronger realization of the free field on the specified generators.

For \(G=\langle g_1,\ldots,g_d\rangle\), take \(M=\mathcal N(G)\) and \(X=(\lambda(g_1),\lambda(g_1^{-1}),\ldots,\lambda(g_d),\lambda(g_d^{-1}))\).
Then \(A_X=\lambda(\mathbb CG)\), so the theorem applies directly to the Task's finitely generated reduction, with rectangular matrices handled by zero padding and kernel dimension equal to the number of columns minus analytic rank.
The fourth route therefore has an established bridge to the Task: prove division of this actual rational closure using an independent analytic mechanism.
Because \(R_X\) is inverse closed in \(\mathcal U(M)\), it suffices to show that every nonzero scalar \(r\in R_X\) has analytic rank one.
It is not enough to prove this only for elements of the original group ring.
The source's linear representations and Schur-complement argument supply concrete probes, but invoking integer polynomial-matrix rank to prove their invertibility would simply assume the target.
The commuting-unitary case \(\mathbb Z^2\) remains a calibration example before testing a specified noncommutative group relation.
Such tests would assess the proposed analytic mechanism, not claim new group coverage.

## Search scope and continuation limits

The search covered the cited classical permanence sources, the 2019 coefficient and locally indicable results, the 2024 three-manifold result, the 2025 finite-edge theorem and the June 2026 outer-automorphism preprint.
No general proof or counterexample meeting the exact Task contract was found in this bounded search.
Torsion examples, positive-characteristic group-ring results and reduced group \(C^*\)-algebra projection questions do not resolve that contract.

JZ19 was checked through its publisher/author summaries and indexed primary-PDF passages containing Theorem 1.1, Corollary 1.2, Theorem 1.3 and Corollary 1.4.
Opening the complete author PDF failed, so no full-text or proof inspection is claimed for that source.
The other cited theorem passages were opened in their primary PDF/HTML editions.
No source proof was audited to completion.
The prior local MSY23 and Lin00 inspections retain their original limits.

The first two proposed routes have concrete algebraic tests and receive the highest initial priority.
Approximation needs a specified family beyond already applicable theorems; the analytic route remains exploratory until it supplies an independent invertibility mechanism for the actual rational closure.
Success on any restricted family would advance the Task without resolving its arbitrary-group quantifier.
Current allocation and next actions belong to the [Task's strategies](../strategies/index.md#task-yin_t_a0001).
