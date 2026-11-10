---
author: Yin
---

# Lin93: division closure, free groups and elementary amenable extensions

<a id="lin93-u001"></a>
## Source and inspection scope

The inspected source is the [complete journal scan](readme.md#journal-scan), printed pp. 561–576, including every article page and the bibliography.
On 2026-11-10 a source reviewer working separately from current project proof development read all sixteen article pages visually and checked the internal proof chain of Theorem 1.5, its implication for Theorem 1.3, and the distinct universal-field assertion in Lemma 5.2.
The initial source findings were formed from the paper, without project proof-generation dialogue.
The earlier [Lin00 supporting-source account](../Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate) was subsequently read for its actual earlier scope.
This is a full inspection of Lin93's exposition and internal arguments, with the external foundations and their uninspected original proofs identified below; it is not a recursive proof audit of all twenty-three references.
No formal verification, inspection of associated code, source-author confirmation or review of a new project Claim is asserted.

## Affiliated closure and rank conventions

For a discrete group \(G\), the source uses the left convolution representation on \(\ell^2(G)\), writes \(W(G)\) for the weak closure of \(\mathbb CG\), and writes \(U(G)\) for closed densely defined operators affiliated with \(W(G)\).
The sums and products in \(U(G)\) are the affiliated-operator ring operations, rather than unrestricted compositions of unbounded operators on arbitrary domains.
The source takes from Berberian [2], Theorems 1 and 10, that \(U(G)\) is a \(*\)-regular ring, that its matrix ring is \(M_n(U(G))\), and that every affiliated operator is a fraction of bounded operators with a regular bounded denominator.
Every projection in \(M_n(U(G))\) lies in \(M_n(W(G))\).
These analytic foundations are retained external inputs; their original proofs were not read in this inspection.

For a unital inclusion \(R\subseteq S\), the **division closure** is the smallest unital subring containing \(R\) and closed under taking inverses of its elements that are invertible in \(S\).
It is not defined to be a division ring.
Lin93 defines

\[
D_n(G)=\operatorname{Div}_{M_n(U(G))}(M_n(\mathbb CG)),\qquad
D(G)=D_1(G),\qquad
W_n(G)=M_n(W(G))\cap D_n(G).
\]

This is the general fixed-ambient division-closure construction already indexed through [MSY23](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra), with the ambient algebra and generators specialized here.
The \(n\)-matrix closure \(D_n(G)\) must not be assumed equal to \(M_n(D(G))\) before the relevant Artinian hypothesis has been supplied.
Lemma 4.1 proves that equality when the scalar division closure is Artinian.

The canonical trace is \(\tau(x)=\langle x\delta_1,\delta_1\rangle\), and the matrix trace is the unnormalized sum \(\operatorname{Tr}_n(x)=\sum_i\tau(x_{ii})\), so \(\operatorname{Tr}_n(1_n)=n\).
For \(\theta\in M_n(U(G))\), its **affiliated rank** is \(\operatorname{rank}(\theta)=\operatorname{Tr}_n(e)\), where \(e\) is the unique projection generating the principal right ideal \(\theta M_n(U(G))\).
For bounded \(\theta\), this is the trace of the projection onto the closure of its range.
It is not divided by \(n\), and it is different from ordinary finite-dimensional operator rank.
Lemma 2.3 checks invariance under multiplication by invertible matrices on either side and the strict bounds \(0<\operatorname{rank}(\theta)<n\) for a nonzero noninvertible \(\theta\).
The right multiplication statement follows from equality of principal ideals; the left multiplication statement uses equivalence of their generating projections and invariance of finite von Neumann trace.
The required projection/conjugacy facts are attributed to Berberian [1] and Linnell [18], and are not silently inferred from an arbitrary algebraic similarity preserving an operator norm.

## Group class and exact theorems

An **elementary amenable group** belongs to the smallest class containing finite and abelian groups and closed under extensions and directed unions.
The source's class \(\mathcal C\) is the smallest class containing all free groups, closed under directed unions, and closed under extensions with elementary amenable quotient: if \(H\triangleleft G\), \(H\in\mathcal C\), and \(G/H\) is elementary amenable, then \(G\in\mathcal C\).
Neither definition makes every torsion-free group a member of \(\mathcal C\).

Theorem 1.3, printed p. 562, assumes \(E\triangleleft G\), with \(G\) torsion free, \(E\) free, and \(G/E\) elementary amenable.
It concludes that a division ring \(D\) exists with \(\mathbb CG\subseteq D\subseteq U(G)\).
The proof actually supplies \(D(G)\).
The statement is not restricted to amenable \(G\): a nonabelian free group is obtained by taking \(E=G\).

Theorem 1.5, printed pp. 563–564, has the more general hypothesis \(G\triangleleft H\), \(G\in\mathcal C\), and bounded orders of the finite subgroups of \(G\).
Set \(l=\operatorname{lcm}\{|F|:F\leq G\text{ finite}\}\), which is finite under that boundedness hypothesis.
For every positive integer \(n\), it asserts:

1. \(D_n(G)=D_n(G)^*=M_n(D(G))=h^{-1}D_n(G)h\) for every \(h\in H\).
2. \(D_n(G)\) is semisimple Artinian.
3. Every idempotent \(e\in D_n(G)\) is conjugate within \(D_n(G)\) to a projection, by a unit \(\alpha\) that also satisfies \(eD_n(G)=\alpha eD_n(G)\).
4. Every \(\alpha\in D_n(G)\) is \(\beta\gamma^{-1}\), with \(\beta\in W_n(G)\) and \(\gamma\) a nonzerodivisor in \(W_n(G)\).
5. A projection \(e\) with \(0\ne e\ne1_n\) satisfies \(\operatorname{Tr}_n(e)=m/l\) for an integer \(0<m<ln\).

The torsion-free specialization has \(l=1\).
For \(n=1\), semisimplicity and conjugacy of idempotents to projections then exclude a nontrivial idempotent, so the semisimple Artinian ring \(D(G)\) is a division ring.
This is the implication used to obtain Theorem 1.3; it does not invoke the scalar Ore condition on \(\mathbb CG\).

The introduction also explains why the existence of such a division ring implies the analytic nonzerodivisor assertion \(a\xi\ne0\) for nonzero \(a\in\mathbb CG\), \(\xi\in\ell^2(G)\).
If \(a\xi=0\), the projection onto the closed right-translation-invariant span of \(\xi\) is a nonzero projection \(e\in W(G)\) with \(ae=0\), contradicting invertibility of \(a\) in \(U(G)\).
Proposition 1.4 adds a further right-orderable quotient using Linnell [19], Theorem 2; Lin93 does not reprove that external theorem, and this audit does not claim to have done so.
The opening references to \(L^2\)-cohomology are consequences through the cited dimension framework, not an additional cohomology proof supplied in this paper.

<a id="free-group-proof"></a>
## The free-group proof, Section 3

For \(F_2\), the tree construction supplies a bijection \(\pi:F_2\to F_2\sqcup F_2\sqcup\{*\}\) with \(\pi(1)=*\).
Its induced unitary \(\alpha:\ell^2(F_2)\to\ell^2(F_2)\oplus\ell^2(F_2)\oplus\mathbb C\) has finite-rank defect
\[
\alpha\lambda(g)-(\lambda(g)\oplus\lambda(g)\oplus0)\alpha
\]
for each group element \(g\).
The extra scalar summand carries zero operator action, not a unital group representation on a singleton.
This unitary and its \(n\)-fold amplification \(\beta\) are the free-tree-specific analytic input.
The existence of \(\pi\) is cited to Effros [10], Section 4, and Julg–Valette [13], Corollary 1.5; those original constructions were not recursively audited here.

Lemma 3.5 compares finite von Neumann trace with ordinary trace of a finite-rank defect.
For bounded \(\theta\in M_n(W(F_2))\) such that \(\theta-\beta^{-1}\theta\beta\) has finite rank, it proves

\[
\operatorname{Tr}_n(\theta)
=\operatorname{trace}(\theta-\beta^{-1}\theta\beta).
\]

The scalar matrix coefficients of a group von Neumann operator have the same diagonal value at every group basis vector.
Under \(\pi\), the diagonal values cancel except at \(1\), whose image lies in the zero-action scalar summand.
Summing diagonal entries of the finite-rank defect gives the formula, and summing matrix diagonal blocks gives its amplification.
The zero action matters: inserting the identity on the scalar summand changes this exact trace identity.

Lemma 3.6 then proves \(\operatorname{rank}(\theta)\in\mathbb Z\) for every \(\theta\in M_n(\mathbb CF_2)\).
Choose a cofinite set \(A\subseteq F_2\) on which \(\pi\) intertwines every group element in the finite support of \(\theta\).
The closed ranges of \(\theta\) and \(\beta^{-1}\theta\beta\) contain the same closed subspace \(\overline{\theta\ell^2(A)^n}\), with finite-dimensional orthogonal complements.
Their range projections therefore differ by a finite-rank operator whose ordinary trace is the difference of those two finite dimensions, hence an integer.
Apply Lemma 3.5 to the range projection.
This justifies the step for a possibly nonclosed original range; replacing the closures by algebraic ranges would not be adequate.

Lemma 3.7 proves that \(D(F_2)\) is a division ring.
Every nonzero \(a\in D(F_2)\) belongs to the rational closure of \(\mathbb CF_2\) in \(U(F_2)\).
Cohn's Cramer stabilization, [6], Proposition 7.1.3, gives invertible matrices \(X,Y\) over \(U(F_2)\) and a matrix \(\theta\in M_n(\mathbb CF_2)\) with

\[
X\operatorname{diag}(a,1_{n-1})Y=\theta.
\]

If \(a\) were noninvertible in \(U(F_2)\), Lemma 2.3 would give \(0<\operatorname{rank}(a)<1\), and therefore \(n-1<\operatorname{rank}(\theta)<n\), contrary to Lemma 3.6.
Thus \(a\) is invertible in the ambient affiliated ring, and division closure puts its inverse in \(D(F_2)\).
The last paragraph on p. 567 cites “Lemma 3.5” for the integrality contradiction; the applicable statement is Lemma 3.6, which itself uses Lemma 3.5.
This is a locally checkable reference-number slip, not a missing integrality premise.

Cohn stabilization is an accepted external algebraic input here, with its exact invoked form checked in Lin93 and [Lin06 Proposition 3.1](../Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures).
Its original book proof was not read in this audit.
The free-group argument proves a property of the actual embedding into \(U(F_2)\); an arbitrary abstract embedding into a skew field would not identify that ambient rank.

<a id="routine-lemmas-and-induction"></a>
## Ring lemmas and the extension argument

Section 2 establishes the subgroup embeddings \(U(H)\subseteq U(G)\) by orthogonal decomposition over right cosets.
For a normal subgroup and a conjugation-invariant coefficient ring in \(U(H)\), Lemma 2.1 identifies the generated ring as the appropriate crossed product over \(G/H\).
Coset independence is part of this identification, not merely a formal choice of notation.
Lemma 2.4 shows that division closures are \(*\)-stable and invariant under the applicable conjugations, and that a \(*\)-closed subring of \(M_n(U(G))\) is semiprime: a nonzero element \(a\) of a nonzero ideal gives \((aa^*)^2\ne0\).

The following checks cover every lemma of Section 4 at its actual interface.

| Source | Checked argument and retained external boundary |
| --- | --- |
| Lemma 4.1, p. 568 | Scalar matrices and matrix units put \(M_n(D)\) in the matrix division closure; an Artinian unital subring is inverse closed in any containing ring, because multiplication by an ambient-invertible element is injective and hence surjective on its finite-length regular module. This gives equality. |
| Lemma 4.2, p. 568 | A finite-index crossed product over an Artinian ring is finite over the coefficient ring and Artinian. It contains \(\mathbb CG\), is inverse closed, and is generated by \(D(H)\) and \(G\), giving \(D(G)=D(H)*G/H\). |
| Lemma 4.3, p. 568 | A simple Artinian coefficient ring is \(M_n(F)\). An automorphism is an entrywise automorphism of \(F\) followed by an inner automorphism, as cited to Jacobson [12], p. 237. Changing the Laurent generator gives a skew Laurent ring over \(F\); invertibility of all constant-one polynomials makes every nonzero skew polynomial invertible after factoring its lowest term. Its skew fraction field and the matrix units then give the required Artinian closure. The automorphism theorem and ordinary skew-polynomial fraction construction remain external inputs. |
| Lemma 4.4, pp. 568–569 | A power of the Laurent generator fixes all primitive central idempotents of a semisimple Artinian coefficient ring. Apply Lemma 4.3 in each component, then recover the original ring by a finite extension. The constant-one invertibility hypothesis is passed to each corner by adjoining the complementary identity. |
| Lemma 4.5, p. 569 | Conjugation invariance of the matrix set extends automorphisms to universal localization. The twisting units also map to units, so the crossed product persists. The two universal maps agree on coefficients and group representatives; the displayed covariance calculation checks multiplicativity and proves \((R*G)_\Sigma\cong R_\Sigma*G\). |
| Lemma 4.7, p. 570 | Surjectivity on \(K_0\), together with decomposition of coefficient projectives into projection ideals, gives stable conjugacy of an arbitrary idempotent to a diagonal list of coefficient projections. Passing from equality in \(K_0\) to an isomorphism after free stabilization uses complements of finitely generated projectives; it is not an assertion that equality in \(K_0\) implies an unstabilized isomorphism. The final matrix-conjugacy interface is Linnell [18], Lemma 8. |
| Lemma 4.8, p. 570 | A finitely generated virtually free group has a finite graph-of-finite-groups decomposition. Induction over its edges, using the cited amalgam and HNN \(K_0\) results, yields surjectivity from finite subgroup \(K_0\)'s. The graph-of-groups theorem and the cited Dicks/Schofield induction theorems remain external foundations. |
| Lemma 4.9, p. 571 | The transfinite hierarchy starts with free-by-finite groups, takes locally preceding-stage groups followed by finitely generated abelian-by-finite quotients at successor stages, and unions at limits. The displayed extension calculation proves that its union is \(\mathcal C\); taking a finite intersection of conjugates proves stability of each stage under finite extension. Subgroup closure and the local form are checked by the same induction. |

Proposition 5.1, p. 572, starts with the explicit hypothesis that \(D(G)\) is Artinian.
It combines the preceding ring lemmas with positivity of \(1+aa^*\), conjugacy of idempotents to projections, and the bounded-fraction construction to obtain Theorem 1.5's structural conclusions.
Its final assertion bounds the length of a strict descending chain of right ideals in \(D_n(G)\) by \(ln\), provided projection traces lie in \(l^{-1}\mathbb Z\).
Indeed, semisimplicity turns such a chain into a sum of nonzero orthogonal-in-the-ideal-sense summands, each with projection trace at least \(1/l\), while their total trace is \(n\).
The needed additivity is the affiliated projection-dimension result cited to Linnell [18], Lemmas 11–12.

Lemma 5.2, pp. 572–573, is the virtually free base case.
Every finitely generated subgroup of a free group embeds in \(F_2\); subgroup compatibility and Lemma 3.7 therefore give a division ring \(D(H)\) for an arbitrary-rank free group \(H\), by directed union.
For a finite-index free normal subgroup \(H\), Lemma 4.2 gives the Artinian crossed product \(D(G)=D(H)*G/H\).
The trace-denominator part additionally uses the universal-field identification described below, Schofield's projective-rank results, and Lemma 4.8 to obtain a surjection from the \(K_0\)'s of finite subgroups to \(K_0(D(G))\).
Lemma 4.7 expresses each projection stably through projections in \(\mathbb CF\), \(F\leq G\) finite.
For such \(F\), a projection has trace an integer divided by \(|F|\), by the ordinary finite-dimensional regular representation of \(F\).
Consequently the resulting trace belongs to \(l^{-1}\mathbb Z\).

Lemma 5.3, pp. 573–575, supplies the transfinite induction.
At a local/directed-union step, every finite chain of right ideals has witnesses in one subgroup stage.
The uniform bound from Proposition 5.1 makes the union Artinian, while each matrix projection already belongs to a finite stage and retains its trace denominator.
The uniform bounded-finite-subgroup hypothesis is essential here; a bare increasing union of Artinian rings need not be Artinian.

At an extension step, first pass to a finite-index torsion-free abelian quotient and reduce its rank to the infinite cyclic case.
For \(1+\delta_1x+\cdots+\delta_rx^r\) with \(\delta_i\in D(H)\), Proposition 5.1 clears the finitely many coefficients by a common regular element of \(W(H)\cap D(H)\).
Linnell [19], Theorem 4, then says the resulting bounded polynomial is a nonzerodivisor in \(W(G)\), hence invertible in \(U(G)\).
Lemma 4.4 proves the Artinian assertion.
This is an explicit external analytic input to the extension proof; it is not supplied by torsion-freeness of \(G\) alone.

For traces at that extension step, \(D(H)G\) is semiprime Noetherian, so Goldie's theorem identifies its regular localization with \(D(G)\).
Lemma 2.2 supplies the surjection on \(G_0\), and Moody's induction theorem [20], Theorem 1, reduces \(G_0(D(G))\) to groups \(F\) lying over finite subgroups of \(G/H\).
These \(F\)'s lie in the earlier local stage by Lemma 4.9(iv).
Semisimplicity identifies \(G_0\) and \(K_0\); Lemma 4.7 and trace additivity then transfer the earlier \(l^{-1}\mathbb Z\) bound.
The final line on p. 575 assembles Theorem 1.5 from Lemma 5.3, Lemmas 2.4 and 4.1, and Proposition 5.1.
No additional amenability approximation or Følner argument is hidden in this assembly.

<a id="hughes-lewin-and-universality"></a>
## Hughes, Lewin and the universal-field assertion

The sentence on p. 573 identifying \(D(H)\), for \(H\) free, with the universal field of fractions of \(\mathbb CH\) has a distinct proof dependency from the division-ring assertion of Lemma 3.7.
It invokes Hughes [11], p. 182 and its uniqueness theorem, together with Lewin [16], Proposition 6.
It is used in Lemma 5.2 to identify \(D(H)\) with a universal matrix localization and thereby enter Schofield's \(K_0\) argument.
Thus these references are unnecessary for the standalone proof that \(D(F_2)\) is a division ring, but are part of the paper's proof of its full extension theorem.

The required uniqueness interface is the uniqueness of a **Hughes-free** division ring of fractions over a locally indicable group ring, fixing that group ring.
Here a group is **locally indicable** if every nontrivial finitely generated subgroup admits an epimorphism onto \(\mathbb Z\).
A division ring of fractions is a division ring containing the specified group ring and generated from it by finite applications of ring operations and inversion of nonzero elements.
The independence condition concerns \(N\triangleleft K\leq H\), with \(K\) finitely generated and \(K/N\cong\mathbb Z\): powers of a lift \(t\) of a quotient generator are left linearly independent over the division closure of \(\mathbb CN\).
In Lin93's actual affiliated embedding, the subgroup division closure is \(D(N)\), and independence of the distinct \(Nt^i\) components is the coset argument behind Lemma 2.1.
It is stronger than the assertion that the abstract group algebra embeds in some division ring.

The [author-hosted Dicks–Herbera–Sánchez reproof](https://mat.uab.cat/~dicks/Hughes.pdf), Section 1, pp. 1–3, and Theorem 7.1, p. 21, was read at statement/interface depth to check the precise locally indicable and independence hypotheses of Hughes uniqueness.
Its proof and Hughes's 1970 original proof were not audited.
The [Wiley original-paper request](https://doi.org/10.1002/cpa.3160230205) supplied bibliographic metadata but no original proof text.
An [AMS request for Lewin's original](https://www.ams.org/tran/1974-192-00/S0002-9947-1974-0338055-4/S0002-9947-1974-0338055-4.pdf) failed with HTTP 403, so Proposition 6 is retained here as the exact external input cited by Lin93, without claiming direct inspection of its original formulation or proof.
The full universal-field identification is consequently checked as Lin93's dependency interface, not as a newly independent proof of Hughes or Lewin.
A use needing independent original-proof coverage of those foundations still requires it.

<a id="transfer-boundaries"></a>
## What transfers to an affiliated rational-closure argument

The general ring operations, matrix stabilization, rank invariance, subgroup inclusions and finite von Neumann projection calculus do not require amenability.
The free-tree finite-defect unitary and the resulting integer-rank conclusion in Section 3 do require the free-group structure used there.
The extension proof requires membership in \(\mathcal C\), bounded finite-subgroup orders, and the listed analytic and \(K\)-theoretic inputs; replacing these hypotheses by torsion-freeness alone is unsupported.

For a torsion-free \(G\) covered by Theorem 1.5, the actual division closure \(D(G)\subseteq U(G)\) is a division ring and its matrix division closures equal \(M_n(D(G))\).
The fixed-ambient rational closure consequently agrees with \(D(G)\) through the usual matrix-inverse closure of a division ring inside a larger ring, as reflected in the [localization conventions](../Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures).
This is compatible with the failure of scalar Ore localization for free groups.
It supplies no expression of every element as \(ab^{-1}\) with \(a,b\in\mathbb CG\), and no universal-field identification for every \(G\in\mathcal C\).

Schur-complement calculations remain calculations in a specified ambient ring with a specified invertible block.
Lin93 can supply that ambient division ring for its stated group classes, but the formal block identity itself cannot establish integer ranks, analytic injectivity, or the necessary invertibility of a block in \(U(G)\).
In particular, this source does not prove the existence of a division ring between \(\mathbb CG\) and \(U(G)\) for an arbitrary torsion-free group; that is Conjecture 1.1 in its own introduction.
