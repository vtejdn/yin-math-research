---
author: Yin
---
# Independent review of coefficient change on finite direct powers

On 2026-11-21 at 04:26 UTC, a separately assigned reviewer completed an independent inspection of the full statement and argument of Yin's C_A0096_v1.
The reviewer received the fixed claim, the two task contracts and the scope of the inspection, without proof-development dialogue, author explanations or previous conclusions about this claim.
The reviewer checked the primary source for the division-closure criterion and consulted the cited comparisons after forming the initial findings.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0096_v1.md#statement) | The support counts, signed witnesses in every characteristic, universal coefficient equivalences and the prescribed finite power for a matrix of given size and coefficient count. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0096_v1.md#argument) | All four proof sections, including separation of affiliated alternating tensors, the rational division-closure criterion, Ore fractions and bounded elimination. |

## Whole finding

All three assertions follow with the stated hypotheses and bounds.
Writing \(v=\sum_j d_jh_j\), the original relation \(uv=0\) gives a nontrivial linear dependence among the \(g_i v\).
Thus \(Pv^{\otimes a}=0\), and the \(a!\) permutations of the distinct \(g_i\) give distinct signed terms of \(P\).
On the \(b^a\) allowed inputs, the matrix of left multiplication by \(P\) has integer entries and only finitely many possible output coordinates.
Its rank is unchanged by extension from \(\mathbb Q\) to \(\mathbb C\), so rational row reduction and clearing denominators give a nonzero integral right factor on that support.

The coefficient of the class sum \(U_\mu\) in \(v^{\otimes a}\) is \(\prod_j d_j^{\mu_j}\).
There are exactly \(q=\binom{a+b-1}{a}\) such classes, and their coefficients give a nontrivial linear dependence among the \(P U_\mu\).
Consequently \(P^{\otimes q}\mathcal A(U_1,\ldots,U_q)=0\).
Every basis tuple contributing to the second factor determines the multiplicity class in each block and thus the unique permutation and the sign of that term.
The first factor also has distinct signed basis tuples.
With the classes ordered, for example, lexicographically by their multiplicity vectors, the signed factors use only the ordered supports and survive reduction to any field, including characteristic two.

The coordinate embeddings of the group von Neumann algebras preserve regular bounded operators and hence extend to their affiliated rings by localization.
The images in different coordinates commute, including their fractions, and the embeddings carry the required division closures into the closure on the product.
For the affiliated row \(R\), the inverse of \(h=(1+RR^*)^{-1/2}\) exists in the affiliated ring and \((hR)(hR)^*=RR^*(1+RR^*)^{-1}\leq 1\).
Thus the entries \(hx_i\) are bounded, and multiplication by \(h\) preserves their complex linear independence.
Faithfulness of the trace gives independence of the corresponding \(L^2\) vectors.
On the identity vector the squared norm of their alternating tensor is \(j!\) times the positive determinant of their Gram matrix.
Multiplication by \(h^{\otimes j}\) therefore proves nonvanishing of the original affiliated alternating tensor.
Its membership in the division ring \(D_j\) makes it a unit.
If \(p\) is the kernel projection of a nonzero scalar combination of the \(x_i\), alternation annihilates \(p^{\otimes j}\) on the right, whence \(\tau(p)^j=0\).
The polar isometry of an injective affiliated operator is unitary in this finite algebra, so the combination has an affiliated inverse.
Picking an independent subset of the original list keeps these elements in \(D_1\).

Lück and Linnell's Definition 2.2 and Theorem 2.3(3) apply to every field \(\mathbb Q\subseteq F\subseteq\mathbb C\), including \(F=\mathbb Q\).
Their right-multiplication formulation gives the same universal matrix integrality condition under the left and right regular representation correspondence.
The review uses the published division-closure criterion at this scope and does not re-audit its original proof. [Lück and Linnell, §2, pp. 9–10](https://him-lueck.uni-bonn.de/data/1602.06906v3.pdf#page=10)

The central coefficients make \(E\) a quotient of the left and right Noetherian ring \(D[T_1,\ldots,T_s]\).
If \(aE\cap bE=0\) for nonzero \(a,b\), the term in \(aE\) of any finite relation \(\sum_i b^iar_i=0\) must vanish.
Cancellation of \(b\) and iteration then give a direct sum of nonzero right ideals, whose finite partial sums contradict the ascending chain condition.
The opposite ring gives the left Ore condition.
Since each nonzero denominator is an affiliated unit, the fraction division ring embeds in \(U(G)\), and elimination in it preserves the actual tracial rank.
Thus the rank is the number of pivots and the kernel dimension is the number of columns minus this rank.

For the finite bound, rational matrix integrality descends from \(G^J\) to each \(G^j\) with \(1\le j\le J\), since the group trace of an induced kernel projection agrees with its subgroup trace.
Every element of \(V_{M_r}\) has an expansion in at most \(J\) scalar monomials with coefficients from \(D\), so the preceding test makes each nonzero such element a unit at its actual independent length.
If the strict inequality \(2\dim_D V_{lM}>\dim_D V_{(l+1)M}\) failed for every \(l<k_i\), iteration from dimension one would give \(\dim_D V_{k_iM}\ge 2^{k_i}\), contrary to the monomial bound.
The resulting right \(D\)-linear kernel gives \(au=bv\) with \(v\ne0\) because \(a\) is injective, also when \(b=0\).
For a residual entry \(d\) below \(b\) and the corresponding first-column entry \(c\), the column multiplication in the actual affiliated algebra gives
\[
             (d-ca^{-1}b)v=dv-cu\in V_{(l+1)M}\subseteq V_{M_{i+1}} .
\]
Here \(v\) is an affiliated unit since \(lM\le M_r\).
Each pivot removes one row and one column, giving at most \(r=\min(m,n)\) steps and the stated \(J\).

The universal equivalences use closure of torsion-free groups under finite direct powers, clearing rational matrix denominators, and the inclusion of signed integral pairs in the complex group algebra.
The rational matrix assertion on the requisite powers and the exclusion of the signed pairs remain the respective open hypotheses of [A0001](../../tasks/Yin_T_A0001_v1.md#contract) and [A0002](../../tasks/Yin_T_A0002_v1.md#contract).
Mghirbi–Douglas assume infinitely many distinct primes and uniform bounds on both actual supports.
Jaikin-Zapirain uses soficity and the algebraic-coefficient Atiyah premise on the same group.
Restriction of scalars alone can multiply a fractional nullity by a field degree.
These comparisons enter no proof step above. [MD26 comparison](../literature/MD26/Yin_U001.md#proposition-83-and-its-quantifiers) · [JZ19 comparison](../literature/JZ19/Yin_U001.md#jz19-u001) · [Restriction of scalars](../../ledger/Yin_L_A0030_v1.md#the-precise-limit-of-restriction-of-scalars)
