---
author: Yin
---
# Full regular rank for the seven positive generators and for three-term sums in the Gardam group

## Statement

Let \(\Gamma\) be the Gardam group with positive triangle generators \(a,b,c,d,e,f,g\).
Write \(d:\Gamma\to C_3\) for the type homomorphism sending each positive generator to \(1\) and write \(\psi:\Gamma\to C_7\) for the homomorphism with respective values
\[
                          6,1,0,4,2,5,3.
\]
We use the residual \(2\)-finiteness of \(\ker d\) established in [C108](Yin_C_A0108_v1.md#statement).
Here residual \(p\)-finiteness means that finite \(p\)-group quotients separate elements.

Let \(0\ne\alpha=\sum_{g\in S}a_g g\), with all \(a_g\ne0\).
Either of the following support conditions suffices:

1. All elements of \(S\) have the same type and \(\psi\) is injective on \(S\).
   In particular, \(S\) may be any nonempty subset of the seven positive generators.
2. The set \(S\) consists of three distinct elements and \(\psi(S)\) has at least two elements.
   The three types and all word lengths are unrestricted.

Over \(\mathbb C\), left convolution by \(\alpha\) has zero kernel and dense range on \(\ell^2(\Gamma)\), so \(\alpha\) is an affiliated unit.
Over every field of characteristic zero or two, \(\alpha\) has no nonzero finitely supported annihilator on either side.
There is also a coefficient-dependent conclusion for three distinct group elements when \(\psi\) is constant on their support.
If at most two types occur and the coefficients lie in a number field with a place above \(2\) of residue degree one, then \(\alpha\) is again an affiliated unit over \(\mathbb C\).
This includes all rational three-term inputs taking at most two types.
The general matrix rank criterion below also applies to left supports of other sizes when their reductions satisfy its hypothesis.
The unrestricted complex zero-divisor and strong Atiyah questions for \(\Gamma\) remain open in this argument.

<a id="argument"></a>
## Reduction of rank over a finite normal \(p\)-subgroup

Let \(G\) be finitely generated, let \(d:G\twoheadrightarrow D\) have finite image, and suppose \(K=\ker d\) is residually \(p\).
There is a descending sequence \(L_n\triangleleft G\) contained in \(K\) with trivial intersection such that \(P_n=K/L_n\) is a finite \(p\)-group.
Indeed, enumerate the nonidentity elements of \(K\), taking for each an excluding normal subgroup of \(p\)-power index in \(K\).
Its \(G\)-conjugates form a finite family because it is normal in \(K\) and \(G/K\) is finite.
The intersection of these conjugates still has \(p\)-power index in \(K\), by the diagonal map into the product of their quotient groups.
Intersect the resulting \(G\)-normal subgroups successively.
If \(K\) is finite the sequence may be taken eventually constant at the trivial group.
Set \(Q_n=G/L_n\), so \(Q_n/P_n=D\).
Every fixed finite subset of \(G\) is eventually separated in \(Q_n\).

Let \(k\) be a field of characteristic \(p\) and let \(A\) be an \(m\)-by-\(s\) matrix over \(k[G]\), acting on columns by left convolution.
Let \(\bar\chi:G\to k^\times\) be a character, extending the coefficient field if necessary.
The twist \(A^{\bar\chi}\) multiplies each group coefficient at \(g\) by \(\bar\chi(g)\).
For any \(G\)-quotient \(Q\) write \(A_Q\) for the induced matrix, viewed in rank formulas as an ordinary \(m|Q|\)-by-\(s|Q|\) matrix.
Twisting takes place on \(G\) before passage to a quotient.
Then
\[
  \frac{\operatorname{rank}_k((A^{\bar\chi})_{Q_n})}{|Q_n|}
       \ \ge\ \frac{\operatorname{rank}_k((A^{\bar\chi})_D)}{|D|}.
                                                               \tag{1}
\]

To see this, the augmentation ideal \(I\) of \(k[P_n]\) is nilpotent.
For a nontrivial finite \(p\)-group choose a central element \(z\) of order \(p\).
The kernel of \(k[P_n]\to k[P_n/\langle z\rangle]\) is \((z-1)k[P_n]\), whose \(p\)th power is zero by centrality and the characteristic.
Induction on group order proves nilpotence of \(I\), starting with the trivial group.
As a right \(k[P_n]\)-module, \(k[Q_n]\) has a basis of \(|D|\) coset representatives.
Left multiplication is right module linear, and augmentation of the entries in this basis gives the ordinary matrix on \(k[D]\), since \(P_n\) is normal.
If that matrix has rank \(r\), choose an invertible scalar \(r\)-by-\(r\) submatrix.
The corresponding block over \(k[P_n]\) is invertible: after multiplication by the inverse scalar block it has the form \(1+E\) with entries of \(E\) in \(I\), and a finite geometric series in \(E\) gives the inverse.
Thus its ordinary rank on \(k[P_n]^r\) is \(r|P_n|\), proving (1).
In the scalar case, a unit on \(k[D]\) consequently gives a unit on every \(k[Q_n]\).
Full input rank on \(D\) gives injectivity on \(k[G]^s\), since a proposed nonzero finite kernel vector survives in some \(Q_n\) after twisting its entries.
For a scalar unit the same argument with multiplication on the other side excludes finite left annihilators.

## Complex rank and the lift of a character

Take a matrix \(A\) over \(\mathbb C[G]\).
Embed the field generated over \(\mathbb Q\) by its finite coefficient set and by \(\mu_e(\mathbb C)\) into \(\overline{\mathbb Q}_p\), where \(e\) is a fixed positive integer prime to \(p\).
Such an embedding exists: a finite transcendence basis can be mapped to an algebraically independent tuple in \(\mathbb Q_p\), since each algebraic closure of a countable subfield is countable and \(\mathbb Q_p\) is uncountable.
Extend the resulting embedding to the finite algebraic extension inside \(\overline{\mathbb Q}_p\).
Use its valuation to reduce integral entries into \(k=\overline{\mathbb F}_p\).
For a nonzero matrix one can first divide all coefficients by one of minimum valuation to keep every coefficient integral and at least one a unit.
Scalar division preserves rank.
Write \(A_0\) for the resulting reduced matrix.

Reduction gives an isomorphism \(\mu_e(\mathbb C)\to\mu_e(k)\) through the chosen embedding.
Indeed, the \(e\) roots are integral units and reducing their product factorization of \(X^e-1\) gives all its roots, which are simple because \(p\nmid e\).
Every character \(\bar\chi:G\to\mu_e(k)\) therefore lifts via this isomorphism to a complex character \(\chi\) of absolute value one.
For each \(Q_n\), reducing the finite matrix \((A^\chi)_{Q_n}\) gives \((A_0^{\bar\chi})_{Q_n}\), because each quotient coefficient is a finite sum of twisted coefficients.
Every nonzero residue minor comes from a nonzero characteristic-zero minor, and field embeddings preserve these ranks.

The regular actions on \(Q_n\) are a sofic approximation of \(G\): eventual separation of each fixed word ball gives the required local relations at every point.
[Jaikin-Zapirain, Theorem 1.3](../audits/literature/JZ19/Yin_U001.md#rank-and-approximation-definitions) gives convergence of normalized complex ranks for the fixed matrix \(A^\chi\).
The source's right multiplication on row vectors is equivalent to our left convention by sending a coefficient function \(f(h)\) to \(f(h^{-1})\) and replacing the matrix by its transpose with each group element inverted.
This linear unitary identification preserves both finite ranks and the canonical trace dimensions.
On \(\ell^2(G)\), the unitary \(\delta_h\mapsto\chi(h)\delta_h\) conjugates left multiplication by \(g\) to left multiplication by \(\chi(g)g\).
Twisting thus preserves the regular rank, since this conjugation preserves the identity-vector trace on the group von Neumann algebra.
Writing \(\operatorname{rk}_G\) for image dimension with the unnormalized matrix trace, we obtain
\[
 \operatorname{rk}_G(A)
  \ \ge\ \limsup_n
      \frac{\operatorname{rank}_k((A_0^{\bar\chi})_{Q_n})}{|Q_n|}
  \ \ge\ \frac{\operatorname{rank}_k((A_0^{\bar\chi})_D)}{|D|}.
                                                               \tag{2}
\]
In particular, full input rank in the last expression gives zero \(\ell^2\) kernel.
For a scalar this is rank one, so the output complement also has trace zero and the range is dense.
The closed densely defined inverse on that range is affiliated.

## Fourier calculation for \(C_3\) and \(C_7\)

Apply (1) and (2) with \(p=2,\ G=\Gamma,\ D=C_3\).
With nonzero reduced coefficients \(c_g\in k=\overline{\mathbb F}_2\), form
\[
       F(X,Y)=\sum_g c_g X^{d(g)}Y^{\psi(g)}
         \quad \text{in }k[X,Y]/(X^3-1,Y^7-1).
\]
For \(\eta\in\mu_7(k)\), the character \(\bar\chi_\eta(g)=\eta^{\psi(g)}\) gives \(F(X,\eta)\) as the twisted image in \(k[C_3]\).
It is a unit exactly when \(F(\tau,\eta)\ne0\) for every \(\tau\in\mu_3(k)\), since \(X^3-1\) has simple roots.
Equivalently,
\[
        N(Y)=\prod_{\tau\in\mu_3(k)}F(\tau,Y)
                 \ne0\quad\text{in }k[Y]/(Y^7-1),           \tag{3}
\]
because evaluation at all seven distinct roots identifies this last algebra with \(k^7\).
The complex lift used in (2) is the one for this same \(\eta\) and the chosen embedding, with \(e=7\).

In support condition 1, every nonempty subset remaining after reduction has distinct \(\psi\)-degrees in one type.
Hence \(F(X,Y)=X^d f(Y)\) with \(f\ne0\) in \(k[C_7]\).
Some \(\eta\) has \(f(\eta)\ne0\), which gives full rank in (1) and (2).

For condition 2, first consider three surviving coefficients.
If exactly two \(\psi\)-degrees occur, one degree has just one coefficient.
For each fixed \(\tau\) its coefficient in \(F(\tau,Y)\) is nonzero.
After factoring a power of \(Y\), the other term has a different degree modulo seven.
Raising to their nonzero degree difference permutes \(\mu_7(k)\).
There is therefore at most one zero among the seven values of \(Y\) for each \(\tau\), including when the two coefficients at the repeated degree cancel.
The three values of \(\tau\) exclude at most three of the seven choices.

Suppose instead that the three \(\psi\)-degrees \(i,j,h\) are distinct.
One common type was handled above.
For two types, factor out the type monomial belonging to the pair and put \(U=aY^i+bY^j,\ V=cY^h\) for the nonzero reduced coefficients.
As \(\tau\) varies, its power given by the nonzero type difference ranges over \(\mu_3(k)\).
The product in (3) is \(U^3+V^3\), because the product of the three type monomials is one.
In characteristic two all four coefficients in the binomial expansion of \(U^3\) are nonzero.
Their degrees \(3i,2i+j,i+2j,3j\) are distinct modulo seven.
The single monomial \(V^3\) leaves at least three of them nonzero.
For three types, order the coefficients by types \(0,1,2\) and write \(U=aY^i,\ V=bY^j,\ W=cY^h\).
The identity
\[
     \prod_{\tau^3=1}(U+\tau V+\tau^2 W)
                  = U^3+V^3+W^3+UVW
\]
follows by multiplying the three factors in characteristic two.
The three cube degrees are distinct modulo seven, so the last monomial leaves at least two of them nonzero.
Thus (3) holds in every three-survivor case.

## When reduction removes a label

For an original three-term complex input, the minimum-valuation normalization can leave just one or two coefficients in the residue field.
A single term has full rank in every quotient.
With two terms, take their group ratio \(u\ne1\).
It has infinite order by torsion-freeness of \(\Gamma\).
For completeness, the [triangle-building realization](Yin_C_A0106_v2.md#combining-the-exceptional-and-nonexceptional-supports) gives a free action on vertices and a fixed point for every finite-order element.
Such an element preserves the smallest simplex containing that point in its relative interior.
A nonidentity one must act there as a three-cycle: fixing a vertex forces identity, and the cyclic type shifts exclude transpositions.
Translate one vertex of this triangle to the identity vertex.
The resulting conjugate or its inverse acts by a positive generator \(s\), moving that vertex to a positive neighbor and satisfying \(s^3=1\).
But \(ss\) is either irreducible or shortens to \(t^{-1}\) with \(t\ne s\), because the [seven triangle relators and complete normal forms](Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) contain no \(sss\).
Both possibilities distinguish \(ss\) from \(s^{-1}\).

Let \(m_n\) be the order of the image of \(u\) in \(Q_n\).
These orders tend to infinity, since any fixed list of nontrivial powers \(u,\ldots,u^M\) eventually stays nontrivial in the quotients.
Up to multiplication by group and scalar units, the reduced two-term operator is \(1+c u\) with \(c\ne0\).
On each of the \(|Q_n|/m_n\) cycles of left translation by \(u\) its kernel has dimension at most one, since one coordinate determines the entire solution.
The normalized residue ranks are at least \(1-1/m_n\).
Equation (2) with trivial character now gives full complex regular rank even if the two remaining \(\psi\)-degrees agree.

At a residue-degree-one place of the coefficient field, all nonzero reduced coefficients are \(1\) in \(\mathbb F_2\).
Choose the embedding into \(\overline{\mathbb Q}_2\) through the completion at that place.
If all three terms survive and they occupy at most two types, reduction to \(\mathbb F_2[C_3]\) leaves a single monomial: either all three terms have the same type or the repeated type occurs twice and cancels.
This is a unit, so (2) with the trivial character proves the coefficient-dependent statement.
With fewer survivors the preceding one- and two-term estimates apply.

Over any characteristic-two coefficient field we may extend to its algebraic closure and use the same Fourier calculation directly, with all original coefficients nonzero and all seventh and third roots available.
The arguments for (1) apply verbatim over this algebraic closure and descend injectivity to the original field.
Over an arbitrary characteristic-zero field, a finite zero product would involve only a finitely generated characteristic-zero subfield, which embeds into \(\mathbb C\) by choosing a transcendence basis and extending across the finite algebraic part.
Support and the zero-product identity survive that embedding.
The complex affiliated-unit conclusion excludes such a product on either side.
For the seven positive generators this removes the finite right-support size restriction of [C106v3](Yin_C_A0106_v3.md#statement) in characteristics zero and two.

## Assessment history

### Decision modular-twist-rank

| Field | Value |
| --- | --- |
| date | 2026-11-21T07:15 |
| status | proved |
| reason | The independent review verifies descent and unit lifting, all type and support degenerations and the complex rank limit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full regular rank on the positive generators, on arbitrary three-point supports separated at two or more seven-character values, and on the stated residue-degree-one inputs. |
| argument | [Proof](#argument) | Finite modular ranks, prime-to-two characters, algebraic specialization and normalized ranks of a separating finite quotient sequence. |
| review | [Whole finding](../audits/reviews/Yin_R_A0146_v1.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Type kernel and seven-character values](Yin_C_A0108_v1.md#decision-skew-triangle-model) | The separating two-group quotients and the specified labels. |
| dependency | [Finite approximation of complex rank](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Jaikin-Zapirain's Theorem 1.3 for these finite sofic approximations. |
| dependency | [Building action](Yin_C_A0106_v2.md#combining-the-exceptional-and-nonexceptional-supports) | The vertex action and type geometry used in the torsion argument. |
| dependency | [Triangle normal form](Yin_C_A0105_v2.md#decision-exact-balls) | Order-three exclusions in the finite-order argument. |

## Current assessment

[Selected decision](#decision-modular-twist-rank)
