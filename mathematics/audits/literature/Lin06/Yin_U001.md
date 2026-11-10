---
author: Yin
---

# Lin06: Ore localization and its distinction from affiliated rational closure

<a id="lin06-u001"></a>
## Source and actual inspection

On 2026-11-10 the source reviewer compared the [published chapter and arXiv v2](readme.md#inspected-editions) at the localization definitions, the complete proof of Proposition 2.2, and Theorem 2.6 with its surrounding qualifications.
The relevant passages are published pp. 41–47 / collection PDF pp. 51–57 and arXiv pp. 1–6.
Proposition 2.2 is on published pp. 42–43 / arXiv p. 3, and Theorem 2.6 is on published p. 44 / arXiv p. 4.
Their numbering, hypotheses and conclusions agree across the inspected editions.
The basic Ore definitions and the matrix-localization/closure definitions also agree mathematically; bibliography numbers and line/page layout differ.
This is a selected source audit, not a full audit or full edition comparison of the twenty-page chapter.

The reviewer was separate from current project proof development and formed the source findings from the actual texts.
Theorem 2.6 has no proof in either inspected passage: Linnell attributes it to Tamari and points to other sources for a proof.
The finite-support argument below checks its mechanism and applicability directly, with [Kielak's reproduced field-case proof](../Bar19/Yin_U001.md#amenable-direction) as a second inspected source.
It does not claim to have inspected Tamari's original paper or Linnell's two cited proof sources.

<a id="crossed-product-and-ore-conventions"></a>
## Crossed products, regular elements and Ore fractions

A **crossed product** \(R*G\) is an associative unital ring that is a free left \(R\)-module with basis \(\{\bar g:g\in G\}\), with \(\bar1=1\), multiplication

\[
\bar x\bar y=\tau(x,y)\overline{xy},\qquad
\bar x r=\sigma_x(r)\bar x,
\]

where each \(\tau(x,y)\) is a unit of \(R\) and each \(\sigma_x\) is an automorphism of \(R\).
Associativity includes the compatibility conditions on \(\tau,\sigma\).
The multiplication need not be the untwisted group-ring multiplication, and \(R,G\) alone do not determine a crossed product.
For finite supports \(S,F\), multiplication sends the corresponding finite-support subspaces into the subspace supported on \(SF\).
When \(R=D\) is a division ring, the homogeneous basis is also a right \(D\)-basis, with coefficients transferred across basis units using the automorphisms.

For a unital ring \(R\), a **regular element** or **nonzerodivisor** is \(s\) such that \(sr\ne0\) and \(rs\ne0\) for every nonzero \(r\in R\).
Write \(S\) for the set of all such elements.
The **right Ore condition** means

\[
\forall a\in R,\ s\in S\quad
\exists b\in R,\ t\in S:\quad at=sb.
\]

The **left Ore condition** instead requires \(ta=bs\).
These multiplication orders matter.
In a domain, \(S=R\setminus\{0\}\).
The right condition gives a ring of right fractions \(RS^{-1}\), with elements \(as^{-1}\), an injective map \(R\to RS^{-1}\), and the universal property for maps that invert \(S\).
Common right multiples permit common right denominators and define the fraction arithmetic.
It is flat as a left \(R\)-module, so \(-\otimes_R RS^{-1}\) preserves injections of right \(R\)-modules.
The chapter cites Stenström, Proposition II.3.5, for flatness; that original proof was not read here.

If both Ore conditions hold, the left and right localizations agree over \(R\), and this is the source's **classical ring of quotients**.
For a domain it is a division ring.
For \(kG\) with \(k\) a commutative field, the anti-automorphism fixing \(k\) and taking \(g\) to \(g^{-1}\) interchanges left and right Ore conditions.
This particular anti-automorphism argument must not be assumed for an arbitrary twisted crossed product over a noncommutative division ring.

<a id="free-subgroup-obstruction"></a>
## Proposition 2.2: the free-subgroup obstruction

Let \(D\) be any division ring and \(G\) contain a subgroup \(H\cong F_2\).
For every crossed product \(D*G\), Proposition 2.2 says the right Ore condition fails.
The whole ring is not assumed to be a domain.
The proof supplies regular elements \(\bar a-1,\bar b-1\), from free generators of \(H\), whose principal right ideals have zero intersection.

For \(G=F(a,b)\), use the alternating syllable length in \(\langle a\rangle*\langle b\rangle\).
A putative common multiple can be expressed as

\[
\alpha=\sum_i(\bar a^{q_i}-1)\bar x_i d_i
       =\sum_j(\bar b^{r_j}-1)\bar y_j e_j.
\]

Remove zero terms and use induction on the maximum length \(L\) of the \(x_i,y_j\), then on the number of terms attaining \(L\).
If \(x_i=a^p h\) has maximal length and starts with an \(a\)-syllable, the identity

\[
(\bar a^q-1)\bar a^p\bar h\,d
=(\bar a^{q+p}-1)\bar h\,d-(\bar a^p-1)\bar h\,d
\]

reduces the maximal-length count; twisting units are absorbed into the right coefficient \(d\).
After this reduction, maximal \(x_i\)'s start with \(b\)-syllables.
Their products \(a^{q_i}x_i\) have length \(L+1\) and start with \(a\).
No term on the other side can produce such an \(a\)-initial word of length \(L+1\), so their sum must vanish.
Reduced-word uniqueness forces cancelling terms to have the same \(q_i\) and \(x_i\), permitting their coefficients to be combined and reducing the maximal-length count again.
The base case \(L=0\) has disjoint nonidentity \(a\)- and \(b\)-supports and gives zero.
This verifies the induction and the zero intersection.

For a larger group \(G\), write \(D*G\) as a free left \(D*H\)-module over right-coset representatives.
The intersection calculation then holds in each coset component.
The regularity of \(\bar a-1\) follows because left or right multiplication by \(\bar a\) shifts the finite support along infinite \(a\)-orbits, with nonzero invertible coefficient changes; a nonzero finitely supported vector cannot be fixed.
The same holds for \(\bar b-1\).
Right Ore would require a nonzero common right multiple of these two regular elements, contradicting the computed intersection.

This obstruction is stronger than the assertion that a free group is nonamenable.
It identifies the precise denominator-clearing failure and works even if other parts of \(D*G\) have zero divisors.
It does not obstruct an embedding in a division ring or the existence of a rational closure obtained by inverting matrices.

<a id="amenable-domain-localization"></a>
## Theorem 2.6: amenability with a domain hypothesis

Theorem 2.6 assumes that \(G\) is amenable, \(D\) is a division ring, and the specified crossed product \(D*G\) is a domain.
It concludes that \(D*G\) has a classical ring of quotients that is a division ring.
The domain hypothesis is explicit, and torsion-freeness alone is not substituted for it.

Here is the finite-support dimension check underlying the statement.
Fix \(a,s\in D*G\), \(s\ne0\), and a finite \(S\subseteq G\) containing both supports.
Take a nonempty finite Følner set \(F\) with \(|SF|<2|F|\).
Use right \(D\)-coefficients and consider

\[
T:(D*G)_F\oplus(D*G)_F\longrightarrow(D*G)_{SF},
\qquad (t,b)\longmapsto at-sb.
\]

This map is right \(D\)-linear, because its fixed multipliers act on the left.
Its domain dimension is \(2|F|\), and its target dimension is at most \(|SF|\), so it has a nonzero kernel vector.
If \(t=0\), then \(sb=0\), and the domain hypothesis forces \(b=0\), a contradiction.
Thus \(t\ne0\), and the equation \(at=sb\) is exactly right Ore.
The left Ore property follows by the corresponding right-multiplication argument with left \(D\)-coefficients and right Følner sets, or by applying the right argument to the opposite crossed product.
The domain hypothesis ensures that the nonzero denominators are regular and that the resulting classical quotient ring is a division ring.

This check uses only finite-support multiplication, finite-dimensional linear algebra over a division ring, and the Følner inequality.
It does not assert that the resulting division ring is already embedded in \(U(G)\).
For the actual complex affiliated embedding, that further step requires the chosen nonzero denominators to be invertible in \(U(G)\), an analytic nonzerodivisor input.
The distinction is relevant even when the algebraic Ore construction itself is settled.

## Matrix localization and fixed-ambient closures

Section 3, published pp. 45–47 / arXiv pp. 4–6, distinguishes universal localization from rational closure in a chosen ring.
For a ring \(R\) and a chosen set \(\Sigma\) of square matrices over \(R\), a map \(\theta:R\to S\) is **\(\Sigma\)-inverting** if every matrix \(\theta(A)\), \(A\in\Sigma\), is invertible over \(S\).
The **universal localization** is a ring \(R_\Sigma\) with a \(\Sigma\)-inverting map \(\lambda:R\to R_\Sigma\) such that every other \(\Sigma\)-inverting map factors uniquely through \(\lambda\).
Existence and uniqueness are cited to Cohn [5], Theorem 7.2.1.
The map \(\lambda\) need not be injective.

For a specified unital inclusion \(R\subseteq T\), let \(\Phi\) be all square matrices over \(R\) invertible over \(T\).
The **rational closure** \(R_T(R)\) consists of all entries of inverses \(A^{-1}\), \(A\in\Phi\).
Block upper-triangular matrices show that this is a subring containing \(R\).
Its defining ambient ring \(T\) is essential.
The canonical map \(R_\Phi\to R_T(R)\) is surjective, but the source explicitly warns that it need not be injective even if \(R\to T\) is injective.
Thus existence of a formal matrix localization does not identify the actual affiliated rational closure.

The **division closure** \(D_T(R)\) is the smallest subring containing \(R\) and closed under inversion of its elements invertible in \(T\).
One has \(D_T(R)\subseteq R_T(R)\).
If \(T\) is a division ring, the closures coincide and are a division ring; if the actual division closure is already a division ring, its matrix rings are inverse closed in the ambient matrix rings and the same equality follows.
These are the fixed-ambient constructions already retained at [MSY23](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra), rather than new definitions for each choice of \(T\).

Proposition 3.1, read at statement depth, records Cohn's Cramer stabilization: an element \(p\) of the appropriate matrix rational closure is stably equivalent, via invertible matrices over the target, to a matrix over the image of \(R\).
This is the algebraic interface used by [Lin93 Lemma 3.7](../Lin93/Yin_U001.md#free-group-proof).
The original Cohn proof and the remaining propositions of Section 3 were not audited in this selected inspection.

## Scope for Schur complements

Proposition 2.2 rules out a scalar Ore-denominator strategy as soon as the group contains \(F_2\).
Theorem 2.6 makes that strategy available for amenable groups with the explicit domain hypothesis.
Neither statement turns a formal Schur complement into a valid inverse inside an unspecified ambient ring.
Matrix inversion and Schur identities remain available after specifying the actual invertible matrix and the target ring, even in the non-Ore case.
Conversely, an abstract division-ring embedding or a universal matrix localization alone does not prove that a matrix is invertible in \(U(G)\), or that its inverse has the intended affiliated rank.

The source's open-problem remarks describe the 2004/2006 text.
This unit does not present those historical remarks as a current classification of arbitrary crossed products.
