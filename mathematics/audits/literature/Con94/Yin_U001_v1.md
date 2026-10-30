---
author: Yin
---

<a id="con94-u001"></a>
# Con94-U001: The Free-Group Tree Module and the Rationality Conjecture

- Source: [Con94, retained electronic book](../../../literature/pdf/Con94.pdf), 654 PDF pages.
  Original acquisition provenance and the electronic revision date are not inferred from the file's presence.
  The registry (private lookup: `../../../literature/registry.md#con94-section-iv5-intake`) owns those acquisition facts.
- Locators: Chapter IV, Section 5, opening construction, Lemma 1, Corollary 2 and Remark 3, numbered/PDF pp. 348-351.
  Necessary internal interfaces: IV.1 Proposition 4 and Corollary 5, p. 303; Lemma 6 and Proposition 7, p. 304; IV.3 Proposition 1 and equation (4.19), p. 322.
  These are the electronic book's displayed page numbers, not an asserted pagination concordance with every printed edition.
- Record: 2026-10-10T12:24, a delegated source reviewer under Yin, within the requested Section IV.5 audit.
  The tree, trace, idempotent and forward inverse-closure arguments were reconstructed directly.
  This is a source-proof review, with the local reconstruction self-reviewed; it does not assert an additional independent review of this written unit unless recorded below.
- Assessment: audited within this scope, with the explicit notation correction to Remark 3 and the accepted Kronecker input identified below.
  The remainder of Section IV.5 and the rest of the book are outside this unit.

## Tree module, representations and domains

Let \(\Gamma\) be a free group.
Choose its Cayley tree \(T\), rooted at \(p=e\), with vertex set \(T^0\) and unoriented edge set \(T^1\).
More generally the construction uses a tree on whose **vertices** \(\Gamma\) acts freely and transitively, without edge inversions.
“Freely and transitively” on p. 349 is interpreted on vertices: the edge set generally has one orbit for each free generator.
A free group is torsion free, so an element swapping the endpoints of an edge would have square fixing a vertex and hence cannot occur.
Thus edge stabilizers are also trivial.

For \(q\ne p\), let \(\phi(q)\) be the final edge of the path from \(p\) to \(q\).
Each edge has exactly one endpoint farther from the root, so \(\phi:T^0\setminus\{p\}\to T^1\) is bijective.
Put

\[
H_+=\ell^2(T^0),\qquad H_-=\ell^2(T^1)\oplus\mathbb C,
\qquad P\delta_p=(0,1),\quad P\delta_q=\delta_{\phi(q)}\ (q\ne p).
\]

The basis bijection makes \(P:H_+\to H_-\) a unitary.
Write \(A=C_r^*(\Gamma)\).
The vertex representation is regular and the edge representation is a Hilbert direct sum of regular representations.
Consequently both extend boundedly to \(A\), even when the free generating set is infinite.
The source uses

\[
\pi_+(a)=a_V,\qquad \pi_-(a)=a_E\oplus0,
\qquad \pi(a)=\pi_+(a)\oplus\pi_-(a).
\]

In particular the scalar summand has **zero** action.
This is a linear, multiplicative, adjoint-preserving representation, but it is not unital on \(H=H_+\oplus H_-\):

\[
I_H-\pi(1)=e_0,
\]

where \(e_0\) is the rank-one projection onto the auxiliary scalar.
No augmentation representation is inserted.
For a nonabelian free group the trivial group representation does not extend to the reduced group C*-algebra, so that substitution would require an unavailable bounded representation.

All operators in this unit are bounded and everywhere defined.
Set

\[
F=\begin{pmatrix}0&P^*\\P&0\end{pmatrix},\qquad
\gamma=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
da=[F,\pi(a)].
\]

Then \(F=F^*\), \(F^2=I\), \(F\gamma=-\gamma F\), and \(\pi(a)\gamma=\gamma\pi(a)\).
There are no affiliated-operator products or unbounded common-domain assumptions here.

## Lemma 1: compactness and the character

If the root is moved from \(p\) to \(gp\), the final-edge assignments can differ only at vertices on the finite path \([p,gp]\).
Off that path the two root paths meet before their common final edge.
With the root/scalar columns included, this proves that

\[
\pi_-(g)P-P\pi_+(g)
\]

has finitely many nonzero basis columns.
It therefore has finite rank for every \(g\in\Gamma\), and likewise for every group polynomial.
The other block of \(da\) equals the conjugate by \(P^*\) of this block, with its sign reversed.
Thus \(d(\mathbb C\Gamma)\) consists of finite-rank operators.

For any \(a\in A\), choose group polynomials converging to \(a\) in norm.
The bound \(\|[F,\pi(a)]\|\le 2\|a\|\) shows that their commutators converge in operator norm, and compact operators are norm closed.
This proves the Fredholm-module assertion.
The trace-class algebra

\[
\mathcal A_1=\{a\in A:da\in\mathcal L^1(H)\}
\]

is a dense involutive subalgebra, since it contains \(\mathbb C\Gamma\), the commutator satisfies the Leibniz rule, and trace-class operators form a two-sided adjoint-stable ideal.
It contains the identity of \(A\), although \(d1=[F,\pi(1)]\) need not vanish: the representation is nonunital and this particular defect has finite rank.
The book denotes this algebra by calligraphic \(\mathcal A\).

For \(a\in\mathcal A_1\), block multiplication gives

\[
\frac12\operatorname{Tr}\bigl(\gamma F[F,\pi(a)]\bigr)
=\operatorname{Tr}_{H_+}\bigl(a_V-P^*\pi_-(a)P\bigr).
\tag{1}
\]

Both diagonal blocks are trace class, and the second is conjugate by \(P\) to the first, which justifies the factor \(1/2\).
Let \(\tau(a)=\langle a\delta_e,\delta_e\rangle\).
Every diagonal entry of \(a_V\) and of \(a_E\) equals \(\tau(a)\).
This holds first for group polynomials because the actions on both sets are free, and then for \(a\in A\) by norm approximation.
Hence the trace-class operator inside the right side of (1) has zero diagonal away from \(p\), and its diagonal at \(p\) is \(\tau(a)\), because \(P\delta_p\) lies in the zero-action scalar summand.
Its trace is therefore \(\tau(a)\).

This verifies the normalization and sign of the zero-dimensional character.
It identifies the character on \(\mathcal A_1\) with the **restriction** of the canonical continuous trace on \(A\); it does not assert that every commutator on \(A\) is trace class.
The canonical trace is positive, normalized and faithful.
For example, \(\tau(a^*a)=\|a\delta_e\|^2\), and if this vanishes then commutation with right translations makes \(a\) zero on a dense set.
The phrase “unique positive trace” in the proof means the unique continuous positive trace extending the specified coefficient functional on the dense group algebra.
It is not a uniqueness assertion for all traces when \(\Gamma=\mathbb Z\).

## Corollary 2: the passage from the dense algebra to all idempotents

The exact internal input, IV.1 Corollary 5 on p. 303, says that a representative of the Chern character of a finitely summable Fredholm module pairs integrally with K-theory.
Proposition 4 immediately above it supplies the Fredholm-index pairing.
The displayed even-case proof, including its compressed operator and trace formula, was read.
For the present zero-dimensional character it gives

\[
\tau(K_0(\mathcal A_1))\subseteq\mathbb Z.
\]

Applying this directly to an arbitrary projection of \(A\) requires the dense-algebra comparison, not density alone.
IV.1 Lemma 6 and Proposition 7 on p. 304 supply holomorphic-functional-calculus stability and the K-theory comparison.
Their exact statements and applicability were checked.
The original Chapter III Appendix C proof of the general K-theory comparison was not recursively audited.
The concrete projection passage needed here can also be checked as follows.

Equip \(\mathcal A_1\) with \(\|a\|+\|da\|_1\).
This is complete: a Cauchy sequence converges in the C*-norm and in the trace norm of its commutators, and the two commutator limits agree in operator norm.
If \(a\) is invertible in \(A\), then

\[
\pi(a)+e_0
\]

is invertible on \(H\), with inverse \(\pi(a^{-1})+e_0\).
Its commutator with \(F\) is trace class whenever \(da\) is, since \([F,e_0]\) is finite rank.
The ordinary inverse-commutator identity on \(\mathcal B(H)\) proves that \(d(a^{-1})\) is trace class.
The same argument works for resolvents; subtracting their finite-dimensional scalar contribution gives the resolvents represented by \(\pi\).
Cauchy integration in the graph norm then proves the holomorphic-functional-calculus statement used here.

Given a projection \(p\in A\), approximate it by a selfadjoint \(b\in\mathcal A_1\).
For sufficiently close approximation the spectrum of \(b\) splits into disjoint neighborhoods of 0 and 1.
Its Riesz projection \(q\) around 1 belongs to \(\mathcal A_1\) and can be chosen with \(\|p-q\|<1\).
Close projections are unitarily conjugate in the unital C*-algebra; this follows by polar decomposition of \(qp+(1-q)(1-p)\).
Thus \(\tau(p)=\tau(q)\in\mathbb Z\).
Positivity gives \(0\le\tau(p)\le1\), and faithfulness gives \(p=0\) or \(p=1\).

An arbitrary idempotent \(E\in A\) has its range projection in \(A\); explicitly,

\[
q=EE^*\bigl(1-(E-E^*)^2\bigr)^{-1}.
\]

The denominator is positive and bounded below by 1, and the formula is the range projection, as seen in the orthogonal decomposition \(\operatorname{Ran}E\oplus\ker E^*\).
Since \(q\) is 0 or 1, the idempotent \(E\) is 0 or 1 as well.
This proves Corollary 2 in the **unamplified** algebra.
It does not exclude the usual nontrivial projections in matrix algebras over \(A\).
The index/integrality theorem is the retained established external input at its exact book interface; the proof above makes the omitted dense-algebra passage explicit.

## Remark 3: matrix rational closure and the forward implication

<a id="con94-matrix-rational-closure"></a>
The source defines \((\mathbb C\Gamma)^{\sim}\) to be the smallest subalgebra \(B\subseteq A\) containing \(\mathbb C\Gamma\) such that, for **every finite matrix size** \(n\),

\[
x\in M_n(B),\quad x^{-1}\in M_n(A)
\quad\Longrightarrow\quad x^{-1}\in M_n(B).
\tag{2}
\]

This is matrix rational closure inside \(C_r^*(\Gamma)\).
It is not merely scalar inverse closure, nor division closure in the *-algebra of affiliated operators.
Define

\[
\mathcal A_{\mathrm{fin}}=\{a\in A:da\text{ has finite rank}\}.
\]

Remark 3 proves the forward inclusion and poses the reverse inclusion as a conjecture:

\[
(\mathbb C\Gamma)^{\sim}\subseteq\mathcal A_{\mathrm{fin}},
\qquad
\mathcal A_{\mathrm{fin}}\subseteq(\mathbb C\Gamma)^{\sim}
\quad\text{(conjectural in this passage, except for \(\Gamma=\mathbb Z\)).}
\tag{3}
\]

Here is the matrix inverse step with the nonunital representation accounted for.
In the algebraic quotient \(\mathcal B(H)/\mathcal F(H)\), the representation \(\bar\pi\) is unital because \(I-\pi(1)=e_0\) has finite rank.
The map

\[
\delta(a)=\bar F\bar\pi(a)-\bar\pi(a)\bar F
\]

is a derivation into the unital \(A\)-bimodule given by this quotient, and its kernel is \(\mathcal A_{\mathrm{fin}}\).
Entrywise extension and the inverse identity give

\[
\delta_n(x^{-1})=-\bar\pi_n(x^{-1})\delta_n(x)\bar\pi_n(x^{-1}).
\]

Thus the kernel satisfies (2), and it contains the group algebra by the tree calculation.
This proves (3)'s forward inclusion.
The quotient is by **finite-rank** operators, not their norm closure.
Using the Calkin algebra here would establish only compactness and would lose the rationality criterion.

No finite-generation assumption is needed for this forward proof or for Lemma 1 and Corollary 2.
The reverse inclusion for noncyclic free groups is not proved in this part of Con94.

## The cyclic group, the Hardy model and the notation error

For \(\Gamma=\mathbb Z\), identify \(H_+\) and the edge space with \(\ell^2(\mathbb Z)\), where the edge labeled \(n\) is \(\{n,n+1\}\).
Let \(S\delta_n=\delta_{n+1}\), let \(Q_+\) project onto \(\operatorname{span}\{\delta_n:n\ge1\}\), and put \(D=S^{-1}Q_+\).
The edge component \(V\) of the tree unitary satisfies

\[
V\delta_n=\begin{cases}\delta_{n-1},&n>0,\\0,&n=0,\\\delta_n,&n<0,\end{cases}
\qquad V=I+D(I-S).
\]

For \(a\in C^*(S)\), which commutes with \(S\),

\[
[V,a]=[D,a](I-S),\qquad [D,a]=S^{-1}[Q_+,a].
\tag{4}
\]

The scalar component of \(Pa-\pi_-(a)P\) always has rank at most one.
Moreover \(I-S\) has dense range, since neither bilateral shift \(S\) nor its adjoint has a nonzero invariant \(\ell^2\) vector.
If \(T\) is bounded, finite rank of \(T(I-S)\) therefore implies finite rank of \(T\): its range is contained in the closure of the finite-dimensional range of \(T(I-S)\).
Consequently the tree commutator is finite rank exactly when \([Q_+,a]\) is finite rank.
Replacing \(Q_+\) by the Hardy projection onto indices \(n\ge0\) changes the commutator by a finite-rank operator.

Under Fourier transform, \(C_r^*(\mathbb Z)=C(S^1)\), the shift becomes multiplication by \(z\), and the Hardy involution is \(F_H=2Q-1\).
IV.3 Proposition 1, p. 322, explicitly states for \(f\in L^\infty(S^1)\) that \([F_H,M_f]\) has finite rank if and only if \(f\) agrees almost everywhere with a rational fraction having no pole on \(S^1\).
This is the accepted Kronecker input used here.
Con94 quotes it rather than proving it; this audit checked its primary book statement and its application through (4), not Kronecker's original proof or reference [457].
For continuous \(f\), the almost-everywhere equality is equality everywhere.

The matrix rational closure of \(\mathbb C[z,z^{-1}]\) in \(C(S^1)\) is exactly the rational fractions with no pole on \(S^1\).
Indeed, such a reduced fraction \(p/q\) is obtained by inverting a polynomial \(q\) with no circle zero.
Conversely entries of the inverse of a finite matrix of rational fractions are rational by the adjugate formula and have no circle pole when that matrix is pointwise invertible.
This proves the asserted cyclic case of (3).

**Correction to the retained electronic text, p. 351.**
Remark 3 calls the rational-fractions algebra “\(\mathcal A\)”.
Read literally as the trace-class algebra introduced in Lemma 1, this is false.
The intended algebra here must be \((\mathbb C\Gamma)^{\sim}\), equivalently \(\mathcal A_{\mathrm{fin}}\) in the just-proved cyclic case.
This is visible in the rendered PDF; it is not a text-extraction substitution.

For a concrete distinction, take \(f(z)=e^z\) on \(S^1\).
On \(\ell^2(\mathbb Z)\),

\[
e^S=\sum_{k\ge0}\frac{S^k}{k!},\qquad
\|[Q_+,S^k]\|_1=k,
\qquad \sum_{k\ge1}\frac{k}{k!}<\infty.
\]

Hence \([Q_+,e^S]\) is trace class.
Formula (4) and the finite scalar block show that the tree commutator is trace class too, so \(e^S\in\mathcal A_1\).
However \(e^z\) is not a rational function: a rational function agreeing with it on the circle would agree analytically near the circle and then throughout its connected meromorphic domain, forcing all its poles to be removable and making the exponential a polynomial.
By the Kronecker criterion its commutator has infinite rank.
Thus trace class and finite rank cannot be interchanged in Remark 3 or in subsequent citations.

This local correction repairs a notation collision, not the proof of the forward implication or the cyclic rationality criterion.
No author-confirmed erratum or comparison with a different Con94 edition is claimed.

## Interfaces with later audited sources

- [DR97-U002](../DR97/Yin_U002_v1.md#dr97-u002) uses the same vertex-to-last-edge map and zero scalar representation.
  Its algebraic coefficient argument is the additional converse mechanism.
  [DR97-U003](../DR97/Yin_U003_v1.md#dr97-u003), with [DR97-U004](../DR97/Yin_U004_v1.md#dr97-u004), proves equality of all matrix inverse closures, scalar inverse closure and the finite-rank algebra for a **finitely generated** free group.
  Thus DR97 resolves the corresponding finite-generator case of the conjecture in Remark 3, not merely an analogy with an unrelated Fredholm module.
  The existing DR97 audit has its own explicit inverse-derivation and residual-support repairs.
- [Lin00-U001](../Lin00/Yin_U001_v1.md#lin00-u001) instead assigns the identity on the auxiliary scalar to each bounded coefficient.
  This assignment differs by a rank-one operator and preserves the finite-rank property, but it is not additive.
  Con94's trace and normalization calculation uses the zero scalar action and cannot be copied unchanged with Linnell's assignment.
  Lin00's unbounded fraction tests and bounded-intersection identity are additional results; Remark 3 contains neither.
  The [Lin00 interface audit](../Lin00/Yin_U004_v1.md#lin00-u004) retains the finite-generator boundary of its accepted DR97 input.
- [MSY23-U005](../MSY23/Yin_U005_v1.md#msy23-u005) checks the bounded terminal-deletion operators for finitely many free Haar generators, with the source's sign correction.
  The operator \(D\) in (4) is their one-generator instance, satisfying \([D,S]=P_{\delta_0}\).
  This supplies a precise link to bounded dual systems, while retaining the distinction between matrix rational closure in \(C_r^*(\Gamma)\) and division closure in the *-algebra of affiliated operators.
- For [F0001](../../../tasks/Yin_T_F0001_v7.md#yin_t_f0001), this unit supplies the precise historical statement and the tree-module normalization behind the DR97 comparison.
  It does not independently prove an arbitrary-normal-tuple criterion, bounded closure descent, or a common theorem containing all conclusions of Con94, DR97 and Lin00.
  No Claim decision is changed by this source audit.

## Independent cross-review

On 2026-10-10T12:27, the coordinating agent independently reviewed the complete written reconstruction, comparing the tree, trace, projection passage, matrix inverse step and circle counterexample with rendered pp. 349-351 and the IV.1 definitions.
No additional correction was needed.
This review covers those local arguments and the declared interfaces; it does not claim a new audit of Kronecker's original proof, the original index-theorem foundations or the general K-theory comparison in Chapter III Appendix C.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Con94, retained 654-page electronic book. Acquisition and edition/revision facts belong to the registry; no unverified original download history or printed-edition identity is asserted. |
| source-locator | IV.5 opening, Lemma 1, Corollary 2 and Remark 3, numbered/PDF pp. 348-351; internal dependencies IV.1 Proposition 4/Corollary 5 p. 303, Lemma 6/Proposition 7 p. 304, IV.3 equation (4.19)/Proposition 1 p. 322. |
| inspection | 2026-10-10T12:24: assigned source text read, rendered pp. 349-351, 303-304 and 322 inspected; tree almost-equivariance, trace normalization, projection passage, matrix closure and the circle-model comparison reconstructed. Remark 3's trace-class/finite-rank notation collision has an explicit counterexample and corrected reading. The exact index/integrality and Kronecker statements are retained accepted inputs with the inspection depths stated above. Their original external proofs, a whole-book audit, author-confirmed errata, an edition concordance and formal verification are outside scope. |
