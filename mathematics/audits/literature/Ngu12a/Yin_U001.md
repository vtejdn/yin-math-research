---
author: Yin
---

<a id="ngu12a-u001"></a>
# Vector-valued progressions and concentration conventions

The selected edition and original-theorem inspection limits are recorded in [Ngu12a source notes](readme.md).
The progression and concentration definitions below were read in arXiv:1105.5733v1, PDF pp. 1--3.
They use Euclidean coefficient space and real scalar random variables; the consuming complex case identifies \(\mathbb C\) with \(\mathbb R^2\).
No originality or equivalence with an uninspected edition is asserted.

<a id="progression-conventions"></a>
## Definition: generalized arithmetic progressions

For vectors \(g_0,\ldots,g_r\in\mathbb R^d\) and integer endpoints \(K_i\le K_i'\), a generalized arithmetic progression is
\[
 Q=\{g_0+\sum_{i=1}^r k_i g_i: k_i\in\mathbb Z,\ K_i\le k_i\le K_i'\}.
\]
Its displayed rank is \(r\), its generators are the \(g_i\), and its volume is \(\prod_i(K_i'-K_i+1)\).
Its size is its actual cardinality, which can be smaller than that volume.
It is proper when the integer-box map is injective.
It is symmetric in this source convention when \(g_0=0\) and \(K_i=-K_i'\).
A vector is \(\delta\)-close to a set if its Euclidean distance to some point of that set is at most \(\delta\).
The local counting proof also uses nonproper progressions, retaining an explicit bound on their displayed integer boxes; the source inverse theorem itself supplies proper symmetric progressions.

<a id="concentration-conventions"></a>
## Definition: linear and quadratic concentration

Let \(\xi_1,\ldots,\xi_n\) be independent copies of a real law \(\xi\), and let \(\beta>0\).
For \(A=(a_i)\) with \(a_i\in\mathbb R^d\), define
\[
 \rho_{\beta,\xi}(A)=\sup_{v\in\mathbb R^d}
 \mathbb P\{\|\sum_i a_i\xi_i-v\|_2\le\beta\}.
\]
For a symmetric array \(A=(a_{ij})\) of vectors in \(\mathbb R^d\), the source's quadratic concentration is
\[
 \rho_{\beta,\xi}(A)=\sup_{v,b_1,\ldots,b_n\in\mathbb R^d}
 \mathbb P\{\|\sum_{i,j}a_{ij}\xi_i\xi_j+\sum_i b_i\xi_i-v\|_2\le\beta\}.
\]
The quadratic convention includes a supremum over linear terms, and differs from fixing those terms in advance.
The local proof's particular quadratic form is bounded by this supremum.
The two uses of \(\rho\) are distinguished by their coefficient arrays.

The inverse-theorem statements and actual local deduction are used in [C_F0188_v2](../../../claims/Yin_C_F0188_v2.md#argument).
The source proof itself remains an accepted external input at the inspection depth stated in the source notes.

<a id="real-scalar-geometric-inverse"></a>
## The real-scalar geometric inverse theorem

Condition 1, printed/PDF p. 2, requires a real law \(\xi\) and constants \(0<c_1<c_2\), \(c_3>0\) such that \(\mathbb P\{c_1\le|\xi-\xi'|\le c_2\}\ge c_3\), where \(\xi'\) is an independent copy.
Theorem 1.3, printed/PDF pp. 2--3, fixes \(0<\epsilon<1\) and \(B>0\), allows \(\beta>0\) to depend on \(n\), and takes coefficients \(a_i\in\mathbb R^d\) with \(\sum_i\|a_i\|_2^2=1\).
If \(\rho:=\rho_{\beta,\xi}(A)\ge n^{-B}\), then for every \(n^\epsilon\le n'\le n\) there is a proper symmetric GAP \(Q\subset\mathbb R^d\) such that at least \(n-n'\) coefficients are \(\beta\)-close to \(Q\),
\[
 \operatorname{rank}(Q)=O_{B,\epsilon}(1),\qquad
 |Q|\le\max\{O_{B,\epsilon}(\rho^{-1}/\sqrt{n'}),1\}.
\]
The constants may also depend on the fixed ambient dimension and the three anti-concentration constants.
This geometric part of the source theorem is accepted as an established external input; the theorem's rational-coordinate clause is not needed for this interface.
The variables are independent copies of one real scalar, whereas the deterministic coefficient vectors can be identified with complex numbers by taking \(d=2\).
This is not itself a theorem for correlated pairs of complex scalars.

For example, a fixed symmetric compound-Poisson integer law satisfies Condition 1.
Precisely, let \(N_\lambda\) have the Poisson law with fixed \(\lambda>0\), and let \(\eta:=\sum_{j=1}^{N_\lambda}\varepsilon_j\), where the signs are independent Rademacher variables independent of \(N_\lambda\).
The law has positive atoms at zero and one, from respectively zero jumps and one positive jump.
Consequently \(\mathbb P\{|\eta-\eta'|=1\}>0\), so \(c_1=1/2\) and \(c_2=3/2\) give Condition 1 with a fixed positive \(c_3\).
This is a direct hypothesis check for that fixed real law, without uniformity as \(\lambda\) varies or a claimed complex-scalar extension.

<a id="symmetric-properization"></a>
## Symmetric properization and rank reduction

The symmetric specialization of Lemma 2.2, printed/PDF p. 6, says that a symmetric GAP \(P\subset\mathbb R^d\) of rank \(r\ge1\), which may be nonproper, is contained in a proper symmetric GAP \(Q\) with
\[
 \operatorname{rank}(Q)\le r,\qquad |Q|\le r^{Cr^3}|P|,
\]
where \(C\) depends only on the ambient dimension.
Only symmetric progressions are adopted here; the lemma's wording is not used to extend this rank bound to arbitrary translates.
If \(r\) is fixed and a displayed integer box for \(P\) has polynomial volume, then \(|P|\) is at most that volume, and the containing proper progression has polynomial size as well.
This conclusion requires no rational-coordinate description of the original generators.

For a primary confirmation of this symmetric scope, [TV08b's inspected arXiv v2](../TV08b/readme.md#arxiv-v2) gives Theorem 1.9 on printed/PDF p. 3.
For a symmetric GAP \(P\) of rank \(r\) in a torsion-free additive group and \(t\ge1\), it gives a \(t\)-proper symmetric containing progression of rank at most \(r\) and size at most \((2t)^r r^{6r^2}|P|\).
Here \(t\)-proper means that the integer-box map stays injective after multiplying all its dimensions by \(t\).
Taking \(t=1\) and the additive group of \(\mathbb C\), which is torsion-free, supplies the required proper container.
The source's size is image cardinality, as specified by Definition 1.3 on p. 2.

Theorem 2.1 of Ngu12a, printed/PDF pp. 6--7, further gives the following rank-reduction interface.
For \(U\) contained in a proper symmetric rank-\(r\) progression \(P\), there is a proper symmetric \(Q\supseteq U\) with rank at most \(r\), size \(O_r(|P|)\), and the integer-coordinate images of \(U\) spanning \(\mathbb R^{\operatorname{rank}(Q)}\).
The surrounding setup identifies \(r\) as the rank of \(P\); no conclusion here requires \(Q\) to contain all of \(P\).

On 2026-11-05 UTC, an agent representing Yin directly reread Condition 1 and Theorem 1.3 on pp. 2--3 and inspected Lemma 2.2 and Theorem 2.1 on pp. 6--7.
Ngu12a p. 6 and TV08b p. 3 were also rendered and checked visually.
The stated symmetric properization and rank-reduction interfaces are accepted as established external inputs at statement and applicability depth; their complete proofs and additive-combinatorial dependencies were not independently audited.
No claim about the remaining mixed-scalar or matrix least-value argument follows from these source checks alone.
