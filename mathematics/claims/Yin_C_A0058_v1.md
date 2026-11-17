---
author: Yin
---
# Exponential Fourier decay of kernel projections over free subgroups

## Statement

Let \(H\) be a finitely generated free subgroup of a finitely generated group \(G\), with word length \(|\cdot|_G\) from any fixed finite generating set.
For every finite rectangular matrix \(A\) over \(\mathbb CH\), let \(p\) be the orthogonal projection onto its regular kernel on \(\ell^2(G)^m\), where \(m\) is the number of columns.
Then \(p\) belongs to the matrix algebra over the rational closure of \(\mathbb CH\) in \(C_r^*(H)\), represented on \(G\).
There is a \(c>0\), depending on the matrix and marking, such that
\[
                   \sum_{g\in G}e^{c|g|_G}\|p(g)\|_{\rm HS}^2<\infty .
                                                               \tag{1}
\]
Its kernel dimension is the algebraic nullity over the free group's affiliated division ring.
In particular every finite matrix carried by such a subgroup of a good four-line group satisfies both spatial conditions in [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace), including when its range is nonclosed.
There are rows of nonclosed range on each of these groups for which the projection is not supported in any cyclic subgroup.

For arbitrary finitely generated \(G\), there is also a matrix-specific sufficient condition for (1).
Let \(\mathcal N(G)\) be the group von Neumann algebra, \(U(G)\) its affiliated ring, and \(S_G\) the rational closure of \(\mathbb CG\) in \(C_r^*(G)\).
Suppose \(R\subset U(G)\) is a unital \(*\)-subring containing \(\mathbb CG\), closed under entries of finite matrix inverses whenever the matrices over \(R\) are invertible in the affiliated algebra.
Suppose further that
\[
                       R\cap\mathcal N(G)\ \subseteq\ S_G.               \tag{2}
\]
For a rectangular \(A\) over \(\mathbb CG\), it suffices that some rectangular \(X\) over \(R\) satisfy \(AXA=A\).
Then the actual kernel projection lies in \(M_m(S_G)\) and satisfies (1).
If the trace of every matrix projection over \(C_r^*(G)\) is integral, its kernel dimension is therefore integral.
The hypotheses allow \(R\) to have zero divisors and impose no prior integrality requirement on affiliated projections.

## Argument

The rational closure in a unital ambient algebra consists of entries of inverses of finite square matrices over the original ring that are invertible in that ambient algebra. [Matrix rational closure and the block formulas](../audits/literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra)
For the finitely generated free group \(H\), write \(D_H\) for the division closure of \(\mathbb CH\) in \(U(H)\).
It is a division ring, stable under adjoints, and \(D_H\cap\mathcal N(H)=S_H\).
The bounded-intersection identity is [Linnell, Theorem 1.1](../literature/pdf/Lin00--arxiv-v1.pdf#page=3), with the [precise finite-generator interface](../audits/literature/Lin00/Yin_U004.md#the-bounded-input-supplied-by-dr97).

Compute a basis for the right kernel of \(A\) over \(D_H\) and let \(V\in M_{m,d}(D_H)\) have those basis columns.
Gaussian elimination over the division ring gives invertible left and right changes reducing \(A\) to a rectangular identity padded by zeros.
Those changes remain invertible over \(U(H)\), so \(V U(H)^d=\ker_{U(H)} A\) and \(V\) has a left inverse.
If \(d=0\), the projection is zero.
Otherwise any column \(v\) in the kernel of \(V^*V\) over \(D_H\) satisfies \((Vv)^*(Vv)=0\).
The affiliated algebra has proper involution, so \(Vv=0\) and the left inverse gives \(v=0\).
An injective square matrix over a division ring is invertible.
Consequently
\[
                          p_H=V(V^*V)^{-1}V^*
\]
is a selfadjoint idempotent with image \(V U(H)^d\).
Selfadjoint idempotents in the affiliated algebra are bounded orthogonal projections.
Multiplying a bounded \(A\) on the left by its affiliated Moore–Penrose inverse gives the complementary support projection, so its affiliated right-module kernel is the image of its Hilbert kernel projection.
Two orthogonal projections generating the same right module are equal, since each acts identically on the other's image.
Thus \(p_H\) is the Hilbert kernel projection.
The polar part of \(V\) has initial support \(I_d\) by injectivity and final support \(p_H\), giving trace \(d\).
Every entry of \(p_H\) is both bounded and in \(D_H\), so Linnell places it in \(S_H\).

## Bounded rational inverses have exponential tails

For any finitely generated group write an element of \(S_G\) as an entry of \(P^{-1}\), with \(P\) a square group-ring matrix boundedly invertible over \(C_r^*(G)\).
Choose \(w\ge1\) bounding the lengths of its coefficients and \(M>\|P\|^2\).
For \(T=I-P^*P/M\) one has \(q=\|T\|<1\) by the positive lower bound for \(P^*P\).
The finite sums
\[
              Q_j=M^{-1}\sum_{k=0}^j T^k P^*
\]
have propagation at most \((2j+1)w\).
They approximate \(P^{-1}=(P^*P)^{-1}P^*\) in operator norm with error at most \(\|P\|q^{j+1}/[M(1-q)]\).
For an entry \(s\) this estimate bounds the coefficient \(\ell^2\)-norm of its tail beyond \((2j+1)w\), by applying the difference to the identity basis vector.
Splitting into these consecutive shells and summing the resulting geometric series gives \(\sum_g e^{c|g|}|s(g)|^2<\infty\) for some \(c>0\).
For a finite matrix take the least of finitely many valid exponents.
The free-group case also agrees with the decay from recognizable reduced-word series and the degree-energy recurrence in [Duchamp–Reutenauer, Lemma 10(i)](../audits/literature/DR97/Yin_U004.md#lemma-10i-decay-and-the-bounded-operator).

Under the decomposition into right cosets \(Ht\), the left regular representation of \(\mathbb CH\) on \(\ell^2(G)\) is a direct sum of copies of its regular representation on \(H\).
The kernel projection therefore has the same entries as \(p_H\) in the represented subgroup algebra, with identical Fourier coefficients on \(H\) and zero coefficients elsewhere.
The identity coefficient preserves its unnormalized trace.
If \(C\ge1\) bounds the ambient lengths of a finite free basis, then \(|h|_G\le C|h|_H\), so the subgroup estimate implies (1) after dividing the exponent by \(C\).
The trivial subgroup gives constant matrices and satisfies (1) directly.

## A nonclosed-range example on the four-line groups

Every good four-line group contains two noncommuting elements \(u,v\).
Indeed a torsion-free abelian group has domain group algebra over \(\mathbb F_2\), as every pair of finite supports lies in a finitely generated free abelian subgroup, whereas the four-line groups have a [nonzero binary zero product](Yin_C_A0051_v1.md#statement).
In the [row construction of C57](Yin_C_A0057_v1.md#nonclosed-range-with-exponential-decay-after-canceling-an-injective-factor), put \(T=u+v\) and take \(A=(1-u)(1,T)\).
That construction gives nonclosed range, an exponentially decaying kernel projection, and kernel \(\{(-Tz,z)\}\).
For \(D=(1+T^*T)^{-1}\), the orthogonal graph projection has entries \(p_{22}=D\) and \(p_{12}=-TD\), by the displayed basis formula with \(V=(-T,I)^t\).
If every entry were supported on a cyclic subgroup \(J\), they would belong to \(\mathcal N(J)\) by the subgroup conditional expectation, and \(D^{-1}\) would belong there as well by bounded functional calculus.
It would follow that \(T=-p_{12}D^{-1}\in\mathcal N(J)\), forcing both \(u\) and \(v\) into \(J\) by uniqueness of Fourier coefficients.
Their noncommutation rules this out.

## An affiliated inner inverse on a larger group

Assume (2) and take \(X\) with \(AXA=A\).
The affiliated matrix \(E=I-XA\) is idempotent, \(AE=0\), and \(E\) acts identically on the affiliated kernel of \(A\).
Thus its right-module image is that kernel.
To produce the orthogonal projection over \(R\), form
\[
 L=EE^*+(I-E^*)(I-E)=I+(E-E^*)^*(E-E^*).
\]
The last expression shows \(L\) is positive with \(L\ge I\), so it has a bounded inverse in the affiliated algebra.
Its entries lie in \(R\), and the assumed matrix inverse closure puts the entries of \(L^{-1}\) there as well.
All calculations take place in the affiliated ring using its closed products.
The two summands in the first expression annihilate one another in both orders because \((I-E)E=0\).
Consequently \(EE^*\) commutes with \(L\) and satisfies \((EE^*)^2=EE^*L\), so \(P=EE^*L^{-1}\) is a selfadjoint idempotent.
Moreover \(EP=P\) and \(PE=E\), the latter following from \(LE=EE^*E\).
It has the same affiliated image as \(E\), so it is exactly the Hilbert kernel projection by the argument above.
Applying (2) to its bounded entries proves \(P\in M_m(S_G)\), and the bounded inverse approximation proves (1).
This argument applies to any given idempotent over \(R\) and its orthogonal image projection.
For matrices involving four-line group relations outside a free subgroup, (2) and the existence of an inner inverse over the selected \(R\) remain additional mathematical requirements.

## Assessment history

### Decision free-subgroup-projection-decay

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:24 |
| status | proved |
| reason | The review checked the bounded rationality input, finite propagation, coset transfer and conditions in the larger group. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exponential decay for rectangular kernel projections in free subgroups and an affiliated inner-inverse criterion. |
| argument | [Proof](#argument) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0094_v1.md#whole-argument-finding) | Independent review of the statement, proof and its direct inputs at the indicated scope. |

## Current assessment

[Selected decision](#decision-free-subgroup-projection-decay)
