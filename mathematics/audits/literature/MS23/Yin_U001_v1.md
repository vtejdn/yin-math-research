---
author: Yin
---

# MS23: Fock Conventions and the Dual-Conjugate Interface

<a id="ms23-u001"></a>
## MS23-U001: Foundations and Domains

Source: the [supplied published MS23](../../../literature/pdf/MS23.pdf), pp. 5-10; edition and inspection scopes in the [source index](readme.md).
Date: 2026-09-09.
Author/reviewer of this reconstruction: the coordinating agent; original contributor checks and the fresh2026-10-21 isolated review have separate exact scopes in the source home.
Coverage: complete reading of Section 2, with direct reconstruction of Lemma 2.2 and both directions of Theorem 2.5.
Foundational q-Fock positivity, faithful trace and homogeneous norm estimates are retained external results, with their precise roles below.

### Setting, norms and corrected Wick recursion

Fix finite d and -1<q<1.
Write H=C^d with the standard real basis, F_alg(H)=direct sum of H^{tensor n}, and Omega=e_0.
On degree n the q-inner product is induced by the positive definite symmetrizer P^(n)=sum_{sigma in S_n} q^{inv(sigma)} U_sigma.
Different degrees are orthogonal.
Strict positivity makes every elementary word independent; these words are not generally orthonormal in the q-inner product.
In degree one they are orthonormal.
The completion is F_q(H).

The source writes l_i^* for **left creation** and l_i for its q-adjoint.
Set A_i=l_i+l_i^*.
The vacuum state is a faithful trace, M=W*(A), and L2(M)=F_q(H).
Wick evaluation W(e_w)=Q[w] has W(e_w)Omega=e_w; its triangular leading monomial also proves algebraic freeness of A.
These facts use the source's [5]-[7] q-Fock foundations; [BKS97-U001](../BKS97/Yin_U001_v1.md#bks97-u001) provides the existing source interface.

For the source's reversed labels w=j_n...j_1, annihilation is

\[
l_i e_{j_n\cdots j_1}=\sum_{k=1}^n q^{n-k}\delta_{i,j_k}e_{j_n\cdots\widehat{j_k}\cdots j_1}.
\]

Consequently the correct Wick recursion is

\[
Q[j_{n+1}\cdots j_1]
=A_{j_{n+1}}Q[j_n\cdots j_1]
-\sum_{k=1}^n q^{n-k}\delta_{j_{n+1},j_k}
 Q[j_n\cdots\widehat{j_k}\cdots j_1].
\tag{1}
\]

**Source correction, p. 6:** the printed recursion omits the Kronecker factor in (1).
The rendered page confirms that this is not an extraction error.
Already Q[ij]=A_iA_j-delta_ij detects the problem for i!=j.
The source's later computations, including p. 27, use the corrected contraction.
This local omission does not invalidate the downstream combinatorial formulas.

Keep the vector norm ||eta||_q separate from the operator norm ||W(eta)||.
For homogeneous degree n the accepted Bozejko estimate is

\[
\|\eta\|_q\le\|W(\eta)\|
\le(n+1)C_{|q|}^{3/2}\|\eta\|_q,
\quad C_r=\prod_{k\ge1}(1-r^k)^{-1}.
\tag{2}
\]

Its statement and applicability were checked in the primary [Dab14, Theorem 28](https://arxiv.org/pdf/1008.4742), PDF p. 40, as well as the existing [Dab14-U001](../Dab14/Yin_U001_v1.md#dab14-u001).
Bozejko's original 1999 proof is not independently audited here.

### Lemma 2.2: free right deletion is bounded

The source's r_i is the literal deletion map r_i(e_{wj})=delta_ij e_w, r_i Omega=0.
For nonzero q this is **not** the adjoint of right creation.
Its q-adjoint r_i^* is not obtained by simply adjoining a letter.
This convention differs from the right q-annihilation used by Yin_C_F0020.

Retain the established one-step symmetrizer comparison

\[
P^{(m)}\otimes I\le w(q)^{-1}P^{(m+1)},\qquad
w(q)^2=(1-|q|^2)^{-1}\prod_{k\ge1}\frac{1-|q|^k}{1+|q|^k}>0.
\tag{3}
\]

This is the external input attributed by MS23 to Bozejko 1998.
Its uniform-in-degree form is independently confirmed in [Nou04, Lemma 1 proof, PDF p. 6](https://arxiv.org/pdf/math/0605789), in the more general strictly contractive Yang-Baxter setting.
The explicit product constant is retained as stated in MS23; Nou's displayed passage only names a positive constant.
The Bozejko institutional endpoint was blocked by an anti-bot challenge, so no full original-source proof or successful complete-page reading of that paper is claimed.

Let Q_i be the ordinary rank-one projection onto Ce_i.
For xi in degree m+1,

\[
\|r_i\xi\|_q^2
=\langle\xi,(P^{(m)}\otimes Q_i)\xi\rangle_0
\le w(q)^{-1}\langle\xi,P^{(m+1)}\xi\rangle_0.
\]

The outputs of different input degrees remain orthogonal, so summing proves ||r_i||<=w(q)^(-1/2) on the whole F_q(H).
Positivity of the infinite product follows from sum |q|^k<infinity.
This proves all local steps of Lemma 2.2 given (3); no tensor-word orthonormality is assumed.

### Definitions 2.3-2.4 and Theorem 2.5

For a bounded selfadjoint tuple X in a faithful tracial W*-space, a conjugate system xi_i in L2(W*(X)) satisfies

\[
\tau(p(X)\xi_i)=(\tau\otimes\tau)(\partial_i p(X)),
\quad \partial_i x_j=\delta_{ij}1\otimes1.
\]

For algebraically free X, the difference quotients act on polynomial vectors.
A normalized dual has a domain containing those vectors, D_i Omega=0, Omega in dom(D_i^*), and [D_i,X_j]=delta_ij P_Omega **on the polynomial domain**.
The word "unbounded" in the source denotes densely defined operators; it neither requires infinite operator norm in every case nor asserts boundedness.

With the inner product linear in the first entry, a conjugate vector for a selfadjoint tuple is selfadjoint (apply the defining identity to p and p*, using the flip relation for the difference quotient).
The following formula describes the unique normalized dual on polynomials:

\[
D_i(p(X)\Omega)=(\mathrm{id}\otimes\tau)(\partial_i p(X))\Omega.
\tag{4}
\]

Indeed, (4) has zero value at 1 and obeys the commutator identity.
Conversely the Leibniz expansion of [D_i,p] applied to Omega forces (4).
Existence of a conjugate system supplies algebraic freeness and hence well-definedness, as in the accepted Voi98/MSY interfaces; for q-Gaussians the triangular Wick argument already supplies it.
The conjugate identity makes p -> <D_i p,Omega> a bounded L2 functional and identifies D_i^*Omega=xi_i.

For the forward direction, expand [D_i,p] by the Leibniz rule and take its vacuum coefficient.
This gives the defining conjugate identity, with all Kronecker factors and the necessary word reversal/conjugation intact.
Normalization removes the term involving D_i Omega.
Thus the article's full Theorem 2.5 is justified, including its externally attributed converse, at the stated domain convention.

Closability can be checked without the source's long index expansion.
For polynomials a,p,

\[
\langle D_i a,p\rangle
=\langle D_i(p^*a),\Omega\rangle
-\langle[D_i,p^*]a,\Omega\rangle.
\]

Here [D_i,p^*] is the bounded finite-rank polynomial commutator, and the first term equals <p* a,xi_i>.
Both terms are bounded in ||a||_2.
Therefore p belongs to dom(D_i^*) and

\[
D_i^*p=p\xi_i-[D_i,p^*]^*\Omega.
\tag{5}
\]

The adjoint domain is dense, proving closability of the polynomial restriction.
If an arbitrary larger domain is allowed, the source's computation must hold on that larger domain before claiming closability there; all constructed q-duals in this paper have exactly F_alg as their initial domain.

**Source correction, p. 10:** the displayed commutator expansion used for closability omits delta_{i,j_k} in its sum.
The preceding display retains it.
Formula (5) is the corrected proof and avoids any change to the conclusion.

The separate closability of the free difference quotient follows from [Voi98-U004, Corollary 4.2 and Proposition 4.3](../Voi98/Yin_U004_v1.md#voi98-u004): if A=C<X>, existence of xi_i=partial_i^*(1 tensor 1) implies A algebraic-tensor A is contained in dom(partial_i^*), a dense domain.
Thus partial_i is closable from L2(M) to L2(M) Hilbert-tensor L2(M).
This is the precise previously audited adjoint-domain interface used in [the Wick-derivative graph-closure argument](Yin_U004_v1.md#the-graph-closure-step), distinct from closability of D_i proved above.

Lipschitz conjugates mean xi_i in dom(closure(partial_j)) and closure(partial_j)xi_i in the spatial von Neumann tensor product M bar-tensor M.
This is neither a statement that D_i is bounded nor a projective-tensor norm estimate.
Finite Fisher information is sum ||xi_i||_2^2.
The source's Fisher/entropy consequences retain the established Voi98 entropy interfaces; see [U005](Yin_U005_v1.md#ms23-u005).

### Verification and boundaries

All pp. 5-10 were text-read; pp. 6, 7, 9 and 10 were visually inspected, including complex conjugations and the two missing Kronecker factors.
The typo P^(tensor n) in the p. 5 direct sum means the degree symmetrizers P^(n).
The p. 10 phrase "orthonormal basis" for e_n refers to the undeformed inner product; in the q-inner product ||e_n||_q^2=[n]_q!, as immediately specified by the source.

The complete q-Fock construction, the original symmetrizer lower bound, and the original Haagerup theorem are accepted foundations, not newly proved results of this audit.
No unresolved local algebra or domain correction remains in the reconstruction above.
The original contributor review and later isolated proof check are recorded separately in the [source completion review](readme.md#goal-completion-review).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | MS23, the supplied 36-page published article, Advances in Mathematics 413 (2023), 108834; printed and one-based PDF pages agree. The earlier 30-page arXiv reading and external source editions retain their separate recorded scopes. |
| source-locator | Section 2, printed/PDF pp. 5-10; Lemma 2.2 and both directions of Theorem 2.5. |
| inspection | 2026-09-09: complete Section 2 reading and local reconstruction of q-Fock conventions, deletion estimates and the dual/conjugate domain interface; separate artifact review is recorded in the source home. Complete q-Fock construction, the original symmetrizer lower bound and homogeneous Haagerup theorem remain accepted foundations, not newly proved results. |


## Current project proof review

The fresh2026-10-21 [independent finding](../../reviews/Yin_R_F0060_v1.md#ms23-u001-isolated-finding) covers its unchanged v1 mathematical core and the corrected dual/quotient adjoint-domain interface.
It checks fixed local mathematics at the retained accepted-source depth; it performs no new primary-page inspection or finite execution and certifies no old reviewer isolation or date.
The [later old-findings comparison](../../reviews/Yin_R_F0060_v1.md#ms23-old-findings-comparison) preserves the original negative interface findings and distinguishes their historical evidence from this current proof review.
