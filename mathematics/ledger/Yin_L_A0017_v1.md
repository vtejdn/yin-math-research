---
author: Yin
---
# Tools for atomic corrections: return operators, mass transport and finite-support modules

Date: 2026-11-11 (Asia/Hong_Kong).
This source comparison follows the exact commutation correction and failed counting implications in [L_A0016](Yin_L_A0016_v1.md).
It supports the current [geometric route](../strategies/Yin_S_A0006.md) and [word route](../strategies/Yin_S_A0007.md) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
The main agent and three search helpers inspected primary-source statements, conventions and selected arguments.
This is source preparation and strategy comparison, not a full proof audit, a formal independent project review or a new Atiyah group-class result.

The existing [Ele03 source proof](../audits/literature/Ele03/Yin_U001.md) and [matrix finite-support estimate](../claims/Yin_C_A0001_v1.md#matrix-boundary-estimate) already supply the amenable group-kernel extraction mechanism.
The existing [SS15 record](../audits/literature/SS15/Yin_U001.md) supplies the free-probability algebraicity and matrix-atom benchmark.
The new search therefore asks for useful additional structure, not another statement of those reductions.

## Selection and remaining arithmetic

| Role | Selected mechanism | Actual missing input |
| --- | --- | --- |
| Exact analytic organization | First-return operator functions and overlapping decompositions | An actual separator or controlled interaction, followed by an independent atomic index |
| Atom-only geometry | Mass transport on the finite components of spectral support | A relation-compatible extension beyond trees and a reason expected counts have the required discrete values |
| Cyclic graph calibration | Finite decorations and their invisible eigenspaces | Full matrix-trace recovery, including modes invisible at the attachment vertex |
| Arithmetic certificate | Finite free resolutions of finite-support eigenfunction modules | Existence and exactness of a finite resolution in the actual group algebra |
| Word compatibility | Positive-definite indicator kernels and central winding variables | Boundary arithmetic beyond merely recovering a genuine quotient-group law |

No selected theorem simultaneously treats arbitrary torsion-free groups, all matrix sizes and all complex coefficients.
Failure to locate such a theorem in this bounded search is not a nonexistence or novelty assertion.

<a id="first-return-functions"></a>
## First-return operator functions

The inspected source is GV17, [arXiv:1702.04032v2](https://arxiv.org/html/1702.04032v2), Definition 2.2 and Theorems 2.5, 3.1, 6.1--6.2.
We use only its bounded Hilbert-space specialization.

**Definition.**
For a bounded operator \(T\) on a Hilbert space, an orthogonal projection \(P\), and \(Q=I-P\), its first-return function on \(P\mathcal H\) is
\[
f_P(t)=PT(I-tQT)^{-1}P,\qquad
s_P(t)=P(I-tT)^{-1}P,
\]
initially for \(|t|\|T\|<1\); the two displayed resolvents act on \(\mathcal H\), while \(s_P(t)^{-1}\) and \(I_P\) below act on \(P\mathcal H\).
The renewal equation is \(s_P(t)^{-1}=I_P-tf_P(t)\).
For selfadjoint \(T\), the source also supplies the Nevanlinna extension.

If \(\mathcal H=\mathcal H_-\oplus\mathcal H_0\oplus\mathcal H_+\) and
\(T=(T_L\oplus0_+)+(0_-\oplus T_R)\), projection onto \(\mathcal H_0\) gives \(f=f_L+f_R\).
Subtract an overlap block \(T_0\) if it was counted twice.
This requires \(P_-TP_+=P_+TP_-=0\).

For S_A0006, the operator-valued return amplitude keeps the off-diagonal transport lost by scalar branch counts.
A square lattice admits a line separator, but its interface is infinite-dimensional.
The renewal identity alone applies to arbitrary operators and imposes no integer residue.

<a id="mass-transport-atoms"></a>
## Mass transport and the atomic support

The source is Sal16, [arXiv:1609.09374v1](https://arxiv.org/html/1609.09374v1), Section 1.2, Theorem 2 and equations (16)--(20).
For the bounded-degree specialization, all adjacency operators below are bounded.

**Definition.**
A probability law of connected locally finite rooted graphs is unimodular when every nonnegative Borel function of a doubly rooted graph satisfies
\[
\mathbb E\sum_x h(G,o,x)=\mathbb E\sum_x h(G,x,o).
\]
This is the mass transport principle.
Let \(\mu_{G,v}\) be the adjacency spectral law at \(\delta_v\), let
\(S_\lambda=\{v:\mu_{G,v}(\{\lambda\})>0\}\), and let \(\partial S_\lambda\) be its external vertex boundary.

For a unimodular random tree, the components induced by \(S_\lambda\) are finite and
\[
\mathbb E\mu_{G,o}(\{\lambda\})
=
\mathbb P(o\in S_\lambda)
-\tfrac12\mathbb E[\deg_{S_\lambda}(o)\mathbf1_{o\in S_\lambda}]
-\mathbb P(o\in\partial S_\lambda).
\]
This is an actual adjacency-atom formula obtained from cavity boundary analysis.
It does not require the complete Green function to be algebraic.
Cycles destroy the scalar cavity decomposition used in its proof.
Moreover, expected component and boundary counts need not be integers.
A transfer must address both obstacles.

<a id="decoration-and-invisible-modes"></a>
## Finite decoration and invisible modes

SA00, [math-ph/0008013v1](https://arxiv.org/html/math-ph/0008013v1), Proposition 3.1, equations (3.3), (3.7), (3.15) and remarks (3.25)--(3.26), treats a finite selfadjoint decoration \(D\) attached at a root \(r\) to an arbitrary bounded selfadjoint base \(H_0\).
Let \(P\) project onto the attachment coordinates.
For \(H=PH_0P+I\otimes D\), the attachment-root resolvent equals the base resolvent at
\[
\gamma(z)=-\frac1{\langle\delta_r,(D-z)^{-1}\delta_r\rangle}.
\]
The source uses \((H-z)^{-1}\).
The rational Herglotz map \(\gamma\) gives full spectral inverse-image recovery when \(\delta_r\) is cyclic for \(D\).
Without cyclicity, the orthogonal complement of its cyclic subspace carries additional decoration eigenmodes.
These are absent from the attachment-root measure.

A direct calibration suggested by this interface is
\[
H=\begin{pmatrix}A&I&I\\I&0&0\\I&0&0\end{pmatrix},
\qquad A=u+u^{-1}+v+v^{-1}\in\mathbb C[\mathbb Z^2].
\]
The constant symmetric/antisymmetric change of leaf coordinates gives
\[
H\cong
\begin{pmatrix}A&\sqrt2 I\\\sqrt2 I&0\end{pmatrix}\oplus0.
\]
The first block has bounded inverse
\(\begin{pmatrix}0&I/\sqrt2\\I/\sqrt2&-A/2\end{pmatrix}\).
Thus its zero-atom dimension is zero, the full unnormalized kernel dimension is one, and the normalized matrix atom is \(1/3\).
The attachment coordinate sees none of this atom.
This elementary calculation is a local benchmark, not a theorem attributed to SA00 or a new group case.

For an embedded-atom test, a further candidate replaces the two identity couplings by \(1-u\) and replaces \(A\) by \(v+v^{-1}\), with adjoints in the lower row.
The antisymmetric channel remains explicit.
Its complete atom/resolvent and continuous-boundary analysis is proposed work, not asserted completed here.

<a id="finite-support-euler"></a>
## Finite-support modules and Euler characteristics

Kra23, [arXiv:2103.12734v3](https://arxiv.org/html/2103.12734v3), Theorems 1.1, 6.1, 6.3 and Lemma 5.1, supplies a genuinely arithmetic certificate.

For a finite-range periodic selfadjoint operator with \(q\) vertex representatives, let \(K_\lambda\) be its \(\mathbb CG\)-module of finitely supported \(\lambda\)-eigenfunctions.

**Definition.**
A finite free resolution here means an exact sequence of modules
\[
0\longrightarrow(\mathbb CG)^{r_d}\longrightarrow\cdots
\longrightarrow(\mathbb CG)^{r_0}\longrightarrow K_\lambda
\longrightarrow0,
\qquad r_j<\infty.
\]
Theorem 6.3 assumes finitely generated \(G\) of subexponential growth and such a resolution, and concludes
\[
q\,\mu(\{\lambda\})=\sum_{j=0}^{d}(-1)^jr_j.
\]
For \(G=\mathbb Z^d\), the source establishes the resolution mechanism by Laurent polynomial methods.
Section 7 includes a nonfree eigenfunction module with one relation among three generators, giving normalized mass \((3-1)/6=1/3\).

This directly fits the desired atomic Euler index while allowing transcendental continuous spectrum.
Finite generation alone is insufficient, and a finite projective resolution is not automatically a finite free one.
For general groups, neither subexponential growth nor the required finite resolution follows from torsion-freeness.
The amenable localization step overlaps the already retained C_A0001; the additional useful input is the finite homological certificate.

Vep26, [arXiv:2606.17187v1](https://arxiv.org/html/2606.17187v1), Theorem 2.1, Theorem 2.6 and Corollary 2.10, extends the localization perspective to unimodular random networks.
Corollary 2.10 assumes amenability, finite expected degree and a finite-range operator; positive eigenspace trace yields a finitely supported eigenfunction with positive probability.
Theorem 2.6 requires the stronger specified balanced Følner hypothesis to recover the trace as averaged finite-support dimensions divided by set size.
These are useful analytic-to-local interfaces, not integer quantization: limits and expectations of normalized integer counts can be nonintegral.
This is a 2026 preprint statement-level input, with no complete proof audit claimed.

<a id="matching-measure-boundary"></a>
## Matching probabilities: exact on trees, a different law with cycles

Mes20, [arXiv:2011.04012v2](https://arxiv.org/html/2011.04012v2), Theorems 9--11, identifies zero-temperature uncovered vertices on bounded-degree trees with the determinantal process of the adjacency-kernel projection.
Thus their exposure probabilities recover diagonal zero-atom masses.
Theorem 11's broader finite bounded-degree graph approximation does not extend that matching interpretation.

**Definition.**
For an orthogonal projection \(P\) on \(\ell^2(V)\) with countable \(V\), its determinantal process is a random subset \(X\subseteq V\) with
\(\mathbb P(F\subseteq X)=\det[P(x,y)]_{x,y\in F}\) for every finite \(F\subseteq V\).
Using \(P=P_{\ker A}\) is a probability representation of the unknown kernel, unless an independent construction of \(X\) is available.

BeMe20, [arXiv:2005.12107v1](https://arxiv.org/html/2005.12107v1), Theorems 1.1 and 1.3, has atom-component bounds on general unimodular graphs, including equality at zero.
Its measure is different.

**Definition.**
For a bounded-degree rooted graph \((G,o)\), its simple-path tree has all finite vertex-simple paths starting at \(o\) as vertices, with adjacency by adding or deleting the final vertex.
The matching measure is the adjacency spectral law of this tree at the length-zero path.

It coincides with the original rooted adjacency law on trees, not on general cyclic graphs.
Already \(C_4\) has perfect matchings but adjacency eigenvalues \(2,0,0,-2\).
Hence uncovered-vertex counts cannot be transferred directly to its adjacency nullity.
A successful cycle correction between the two measures would be an additional theorem.

<a id="positive-definite-word-kernels"></a>
## A precise compatibility test for return words

IS05, [arXiv:math/0405063v2](https://arxiv.org/html/math/0405063v2), Theorem 2.1(ii) and its proof, identifies positive-definite idempotents as subgroup indicators.
Use the normalized nonzero case on the discrete free group \(F_r\).

**Definition.**
A function \(\varphi:F_r\to\mathbb C\) is positive definite when
\([\,\varphi(w_i^{-1}w_j)\,]_{i,j=1}^k\) is positive semidefinite for every finite list \(w_1,\ldots,w_k\).
If \(\varphi(e)=1\) and \(\varphi\) takes only values zero and one, the source theorem gives \(\varphi=\mathbf1_N\) for a subgroup \(N\).
Conjugation invariance makes \(N\) normal.
The condition \(w^m\in N\Rightarrow w\in N\), for every positive integer \(m\), says exactly that \(F_r/N\) is torsion-free.

For example, \(\varphi(h)=\varphi(k)=1\) forces \(\varphi(h^{-1}k)=1\): otherwise the Gram determinant on \(e,h,k\) is negative,
\[
\det\begin{pmatrix}1&1&1\\1&1&a\\1&a&1\end{pmatrix}
=-(1-a)^2.
\]
A proposed monoid language must first respect free reduction to define this function.
This test detects compatibility omitted by L_A0016's scalar moment construction.
Imposing the full test recovers genuine quotient-group data; it does not solve their matrix rank problem.

<a id="central-winding-series"></a>
## Central winding as a relation-sensitive calculation

AER26, [arXiv:2605.12793v1](https://arxiv.org/html/2605.12793v1), Definition 1.3, Section 3 and Theorem 2.8, studies
\[
G(p_1,\ldots,p_k)=
\langle a_1,\ldots,a_k\mid a_1^{p_1}=\cdots=a_k^{p_k}\rangle,
\qquad p_i\ge2.
\]
Its bivariate series retains powers of the common central element, and taking the winding constant term recovers actual return counts.
For all \(p_i=2\), Theorem 2.8 gives
\[
F_k(z;q)=
\frac{2(k-1)}
{k-2+k\sqrt{1-4(k-1)(q+2+q^{-1})z^2}},
\qquad
\text{return series}=[q^0]F_k(z;q).
\]
This offers an explicit next model after commutation, with relation data preserved before scalarization.
It is a special scalar generating-set computation; complex matrix coefficients and residue quantization remain additional work.
The central-edge nature also overlaps the existing S_A0005 calibration and does not settle a noncentral amalgam.

The general asymptotics are not adopted here.
Theorem 7.12, equation (7.38), prints an \(O(\sqrt n)\) error inside a purported local-limit leading bracket.
Corollary 7.13 describes a cogrowth series as an algebraic number.
These passages require clarification before they support asymptotic deductions; the exact Theorem 2.8 is the selected interface.

<a id="regularity-obstructions"></a>
## Universal regularity targets already excluded

For a finite symmetric generating set, the cogrowth series counts identity words of each length, equivalently the unnormalized return-moment series of its adjacency sum.
BeMi18, [arXiv:1805.08118v1](https://arxiv.org/html/1805.08118v1), Theorem 1.1, states that every finite symmetric generating set of a finitely generated amenable group that is not nilpotent-by-finite has non-D-finite cogrowth.
Here D-finite means satisfying a nonzero linear differential equation with polynomial coefficients.
Thus a finite-order differential equation can organize selected families but cannot replace algebraicity as a universal S_A0007 target.
The converse assertion that algebraic scalar cogrowth forces virtual freeness is treated as a conjecture by AER26, not an adopted theorem here.

Gra15, [arXiv:1409.3212v3](https://arxiv.org/html/1409.3212v3), Appendix, Corollary 12, gives
\[
T=ft+t^{-1}f\in\mathbb Q[\mathbb Z^3\wr\mathbb Z],
\qquad
f=7+\sum_{j=1}^3(s_j+s_j^{-1}),
\]
with
\[
\mu_T((0,\varepsilon))\ge C|\log\varepsilon|^{-3}
\]
for every sufficiently small positive \(\varepsilon\).
This group is torsion-free: a finite-order element projects trivially to \(\mathbb Z\), and its base lies in the torsion-free direct sum of copies of \(\mathbb Z^3\).
Therefore even a positive-power upper bound depending on this individual operator fails.
The open interval omits the zero atom, so this is no counterexample to Atiyah.
The cited random-Jacobi upstream theorem was not audited in full.

<a id="secondary-tools-and-source-limits"></a>
## Secondary tools and source-use limits

Bel15b, [arXiv:1510.05377v2](https://arxiv.org/html/1510.05377v2), Theorem 2.2, supplies noncommutative Julia--Wolff--Caratheodory boundary control.
Its finite directional slopes do not by themselves supply a common completely positive linear derivative: the additional hypotheses of (1') or (2) matter.
It can support the analytic step of a matrix-return argument, not the missing arithmetic.
The existing [BBL21 interface](../audits/literature/BBL21/Yin_U001.md#cauchy-boundary-recovery) remains the directly prepared atom-recovery input.

Lue15, [arXiv:1310.8564v2](https://arxiv.org/html/1310.8564v2), Theorem 1.8, gives a positive-power bound for the punctured singular-value density of complex Laurent matrices when the selected maximal minor has positive width.
The corresponding published statement is Theorem 1.2, p.76, [DOI 10.5802/ambp.346](https://numdam.org/articles/10.5802/ambp.346/).
Its printed zero-width matrix branch instead asserts a scalar zero/one step.
For \(A=I_2\), the source's unnormalized \(F_A(\lambda)\) equals two for \(\lambda\ge1\), contradicting that branch.
The search helper checked the same clause in the published PDF.
No use of that branch, full proof audit or author-erratum search is claimed.
The positive-width estimate is an optional abelian calibration, not a general group hypothesis.

DSS21, [arXiv:2105.02058v1](https://arxiv.org/html/2105.02058v1), Theorem 1.2, supplies the Feshbach--Schur nullity correspondence when the complementary compression is invertible.
It does not remove this invertibility assumption at an embedded atom.
Ordinary finite-dimensional nullity cannot be substituted for the trace of a matrix over an infinite group algebra.

The inspected spectral-shift comparison of Behrndt--Gesztesy--Nakamura, [Theorem 4.1 and Corollary 4.2](https://pmc.ncbi.nlm.nih.gov/articles/PMC6407858/), requires a common symmetric restriction, boundary-triple and Schatten conditions.
Its almost-everywhere boundary formula does not automatically control a prescribed atom, nor compare operators on different group spaces.

Gra11, [arXiv:1004.2030v3](https://arxiv.org/html/1004.2030v3), Sections 2.6, 3.2 and Theorem 4.3, illustrates how integrating finite-orbit kernel counts can produce nondiscrete traces.
Its group-ring encoding in Lemma 2.6 uses order-two projections \((e+g)/2\).
The selected construction therefore supplies an adversarial test for probabilistic counting, not a torsion-free counterexample.
The inspected edition is v3; the available v4 was not substituted for that inspected input.

The additionally inspected SS15 Theorems 3.1, 3.4 and Corollary 3.6, [arXiv:1305.1920v1](https://arxiv.org/html/1305.1920v1), give an existing positive benchmark.
Freely independent normal inputs with atomic denominators \(d_j\) yield normal matrix-polynomial atomic denominators dividing \(\ell\prod_j d_j\) at matrix size \(\ell\).
Their arithmetic uses freeness and the stated Atiyah-property permanence; it does not survive arbitrary added relations by these theorems alone.

<a id="source-scope-correction"></a>
## Correction of the earlier source-scope restriction

BGVM20, [arXiv:2008.03318v2](https://arxiv.org/html/2008.03318v2), Section 2.2 and Theorem 3.1, already uses complex Hermitian scalar weights and real potentials.
Lemma 2.1 removes phases by a tree gauge.
Theorem 6.1 additionally has a unitary-edge-weighted finite-graph multiplicity lower bound.
These facts correct S_A0006's overly broad assertion that the inspected index source only permitted positive real weights.
They do not extend BBGSS23's separate product interface or prove equality for arbitrary matrix coefficients.
For use of the forest conclusions, restrict to nonzero weights on the effective edge support; the source's treatment of zero-weight graph edges has not been resolved here.
The previous positive-weight specialization and the formulas of L_A0016 remain valid.

## Concrete continuation

First test full-trace recovery on the finite-decoration benchmark, using its explicit invisible kernel sector.
Then use a model with nonzero atom and accumulating continuous spectrum to test the operator-valued first-return boundary calculation.
A useful theorem must identify the atomic contribution from independently checkable data, rather than assuming the rank of its correction operator.

For S_A0007, require a genuine positive-definite group-word kernel before scalarizing, and use the explicit central-winding model as a controlled relation test.
Neither D-finiteness nor a positive Novikov--Shubin exponent is a universal premise.
The finite-support free-resolution certificate is the most direct inspected bridge to an integer Euler expression, conditional on its actual algebraic hypotheses.

The two unresolved source passages in AER26 and the zero-width clause in Lue15 are excluded from accepted use.
They require targeted clarification only if that later work selects the affected conclusions.
No change to the A0001 completion criteria or claimed coverage follows from this search.
