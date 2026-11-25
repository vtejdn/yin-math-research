---
author: Yin
---

# A countable coefficient test for complete deletion

## Statement

Let \(G\) be a finitely generated discrete group.
For a conjugation-stable field \(k\subset\mathbb C\), write \(D_k(H)\) for the division closure of \(kH\) in the algebra \(U_H\) of affiliated group operators.
Write \(\Lambda=\bigoplus_{i\ge1}\mathbb Z\).
There is a countable conjugation-stable field \(F\subset\mathbb C\) for which the following are equivalent.

1. The unrestricted [finite-rank equation (1)](../tasks/Yin_T_A0003_v3.md#contract) detects \(D_{\mathbb C}(G)\) for every \(u\in U_G\).
2. The ring \(D_F(G\times\Lambda)\) is von Neumann regular.
3. For each \(m\ge0\) and every finite rectangular matrix \(X\) over \(F[G\times\mathbb Z^m]\), there is some \(j\ge m\) and a matrix \(Y\) over \(D_F(G\times\mathbb Z^j)\) such that \(XYX=X\).

The groups \(\mathbb Z^m\) occupy the first \(m\) coordinates of \(\Lambda\).
The test assumes no division-ring property.
If \(G\) is sofic, one can take \(F=\mathbb Q\), and it suffices in condition 3 to use integer group-ring inputs \(X\).
For a fixed torsion-free sofic \(G\), words in the marking give lists of the integer group-ring input matrices and the syntactic candidate expressions for their witnesses.
The assertion is a countable mathematical criterion and supplies no algorithm for deciding whether an affiliated inverse exists.

More precisely, one may use any countable conjugation-stable \(F\) such that applying an automorphism of \(\mathbb C\) fixing \(F\) to the coefficients of a complex group-ring matrix preserves its affiliated rank.
Choose real \(t_1,t_2,\ldots\) algebraically independent over \(F\) and set \(K=F(t_1,t_2,\ldots)\).
Sending the central generators of \(\Lambda\) to the \(t_i\) gives a rank-preserving ring isomorphism \(D_F(G\times\Lambda)\simeq D_K(G)\).
The involution sends a central generator to its inverse before evaluation and fixes the chosen real scalar after evaluation.

## Argument

### A field controlling ranks

For every finite matrix size and group support use the coefficients of the group elements in all matrix entries as independent complex variables.
For each rational threshold \(q\), the locus on which the affiliated rank is at most \(q\) is a complex algebraic set by [closedness of rank sublevels](Yin_C_A0128_v1.md#statement).
There are countably many of these loci because \(G\) is countable.
Choose finite sets of polynomial equations for them and adjoin their coefficients and complex conjugates to \(\mathbb Q\).
The resulting countable field \(F\) has the asserted invariance, since all rational rank comparisons determine the real rank.
For a sofic group, ranks of complex group-ring matrices are limits of ordinary normalized ranks on the same finite permutation models before and after a field automorphism. [Sofic coefficient invariance](Yin_C_A0007_v10.md#scalars-in-the-division-closure-on-a-sofic-group)
Ordinary ranks are invariant under all field automorphisms, so \(F=\mathbb Q\) works here.

We use two facts about matrix ranks and rational expressions.
When two evaluations agree on all ranks of matrices over a common coefficient ring, any scalar rational expression is defined at one evaluation exactly when it is defined at the other.
To verify this, represent an expression with defined internal operations as a coordinate of an invertible block matrix over the coefficient ring.
Addition uses a diagonal sum, multiplication uses a triangular matrix, and for an inverse the bordered matrix is invertible precisely when its scalar Schur complement has full rank.
Induction on gates therefore detects legality at both evaluations.
For a matrix of such expressions put all the individual pivots in a block diagonal matrix and use a row and a column of extraction blocks.
The rank of the resulting bordered matrix minus the sum of the pivot sizes is the rank of the desired matrix.
In particular equality of two expressions is detected by the rank of their difference. [Rational linearization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
These arguments use ring operations alone, so they also transport an equation \(XYX=X\) under a coefficient automorphism that does not commute with complex conjugation.

For a conjugation-stable coefficient field \(k\), regularity of \(D_k(H)\) is equivalent to every rectangular matrix over \(kH\) having an inner inverse over \(D_k(H)\).
Regularity passes to finite matrix rings and rectangular matrices by padding.
Conversely take \(x=\alpha L^{-1}\beta\in D_k(H)\) with \(L\) over \(kH\) an affiliated unit.
Its inverse has entries in \(D_k(H)\) by [Gram elimination](Yin_C_A0132_v1.md#argument), which uses only adjoints, ring operations and inverses of affiliated units.
An inner inverse over \(D_k(H)\) of the matrix with blocks \(L,\beta,\alpha,0\) gives one of \(\operatorname{diag}(L,-x)\) by the two invertible Schur row and column operations.
Its last corner, with sign reversed, is an inner inverse for \(x\).

### Specializing the central group generators

For a matrix \(P\) over \(F[G\times\Lambda]\) only finitely many central variables occur, say the first \(m\).
After Fourier transform in the central factor, its rank is the integral of the ranks of \(P(s)\) on the \(m\)-torus.
Almost every point of that torus has its coordinates algebraically independent over \(F\).
Indeed there are countably many nonzero polynomials over \(F\), each of whose torus zero sets is Haar-null by induction in the coordinates.
At every such point an automorphism of \(\mathbb C\) fixing \(F\) sends its coordinates to \(t_1,\ldots,t_m\), by extending a transcendence basis.
Thus the integral is precisely the rank of \(P(t_1,\ldots,t_m)\) in \(U_G\).
The same comparison holds for the countable direct sum, since passage from a subgroup to a larger group preserves the affiliated rank of its matrices, by the decomposition into right cosets.

The preceding linearization now gives a rank-preserving isomorphism of division closures onto the closure of the specialized group ring.
This closure contains the field \(K\), since all the nonzero numerical polynomial values in the \(t_i\) are scalar units.
It therefore equals \(D_K(G)\).
The comparison of ranks on all Laurent polynomials gives this isomorphism using ring operations alone.

### Transporting inner inverses between coefficient fields

Set \(D=D_{\mathbb C}(G)\).
Suppose first that \(D_K(G)\) is regular, and take a matrix \(X\) over \(\mathbb CG\).
Some automorphism of \(\mathbb C\) fixing \(F\) sends its finitely many coefficients into the algebraic closure of \(K\) inside \(\mathbb C\).
Indeed a transcendence basis of the field they generate over \(F\) is finite and can be sent to some of the independent \(t_i\).
The remaining algebraic extension then embeds in the algebraic closure of \(K\).
The resulting partial field isomorphism extends to \(\mathbb C\) by choosing transcendence bases of its domain and image complements.
Both complements have the same transcendence degree because the specified fields are countable.

The transported matrix \(X'\) is defined over \(EG\) for a finite extension \(E/K\).
Represent scalars of \(E\) by their \(K\)-linear multiplication matrices in one basis of \(E/K\).
The resulting block matrix \(X'_K\) over \(KG\) has an inner inverse over \(D_K(G)\).
In characteristic zero a scalar change of basis over a finite normal extension simultaneously diagonalizes the multiplication matrices, with diagonal entries indexed by the embeddings of \(E\) over \(K\).
After the same scalar changes on the row and column spaces, \(X'_K\) is a diagonal sum of the conjugate matrices of \(X'\).
The corresponding diagonal block of its transformed inner inverse is an inner inverse of \(X'\) over \(D\).
The rank-invariant coefficient transport carries this identity back to \(X\).
The rectangular matrix criterion proves regularity of \(D\).

Conversely suppose \(D\) is regular and take \(X\) over \(KG\).
Choose an inner inverse of \(X\) over \(D\) and fix finite rational expressions for its entries.
The input coefficients of \(X\) use only finitely many \(t_i\).
Fix the field generated by these \(t_i\) and \(F\), and move all complex scalars in the witness expressions into the algebraic closure of \(K\) by the same field argument, using unused \(t_i\) for the finite transcendence basis.
This fixes \(X\), preserves legality and gives an inner inverse with rational expressions over \(EG\) for a finite normal extension \(E/K\).

Apply the multiplication-matrix representation of \(E/K\) to every coefficient in those expressions.
Every embedding of \(E\) over \(K\) extends to an automorphism of \(\mathbb C\) fixing \(F\).
Consequently all conjugate expressions are defined and each satisfies the same inner-inverse identity for \(X\).
The represented gates are simultaneously similar over \(\mathbb C\) to these diagonal conjugate gates.
At an inverse gate the block matrix over \(D_K(G)\) is therefore an affiliated unit, and Gram elimination puts its inverse back over \(D_K(G)\).
Induction gives a block inner inverse over \(D_K(G)\) for the multiplication-matrix form of \(X\).
Since \(X\) was over \(KG\), that form is a direct sum of identical copies of \(X\) after reordering coordinates.
One diagonal block yields the required inner inverse over \(D_K(G)\), and the rectangular matrix criterion proves regularity.

### Finite matrices in the countable test

The [unrestricted equation criterion](Yin_C_A0131_v1.md#which-rationality-is-detected) equates condition 1 with regularity of \(D\).
The isomorphism and field argument equate it with condition 2.
Every group-ring matrix over \(F[G\times\Lambda]\) has support in a finite coordinate subproduct.
Every rational witness uses only finitely many further group elements in its finitely many gates.
The affiliated inverses of subgroup operators are the same in the subgroup and in the whole group, by right-coset decomposition.
This proves the equivalence of conditions 2 and 3.
When \(F=\mathbb Q\), multiplying an input matrix by a common nonzero integer clears its denominators without affecting the existence of an inner inverse over the division closure.

## Assessment history

### Decision countable-coefficient-test

| Field | Value |
| --- | --- |
| date | 2026-11-25T12:56 |
| status | proved |
| reason | Rank-preserving specialization in central variables and finite Galois descent transfer regularity between the countable test ring and the full complex division closure. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The countable coefficient criterion, specialization isomorphism and integer inputs for sofic groups. |
| argument | [Argument](#argument) | Fields of definition of rank loci, torus specialization, rational linearization and restriction of scalars. |
| dependency | [Algebraic rank loci](Yin_C_A0128_v1.md#statement) | Closedness of every rank sublevel at fixed support and size. |
| dependency | [Sofic ranks](Yin_C_A0007_v10.md#scalars-in-the-division-closure-on-a-sofic-group) | Coefficient automorphisms preserve complex group-matrix rank in sofic groups. |
| dependency | [Rational linearization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Rank tests for the domain and value of rational expressions. |
| dependency | [Matrix inverse closure](Yin_C_A0132_v1.md#argument) | Gram elimination over a conjugation-stable division closure. |
| dependency | [Regularity criterion](Yin_C_A0131_v1.md#which-rationality-is-detected) | Equivalence between complete deletion and regularity of the complex division closure. |
| review | [Countable coefficient test](../audits/reviews/Yin_R_A0172_v1.md#countable-coefficient-test) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-countable-coefficient-test)
