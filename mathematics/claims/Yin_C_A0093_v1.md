---
author: Yin
---
# A single-prime transfer bound from the integral product table

## Statement

Let \(A=\{x_1,\ldots,x_a\}\), \(B=\{y_1,\ldots,y_b\}\) be two nonempty sets of distinct elements of a group \(G\), with \(a,b\ge2\).
The question here allows the supports of the two nonzero factors to be subsets of \(A,B\).
For each \(g\in AB\) put \(F_g=\sum_{x_i y_j=g}X_iY_j\) and let \(c\) be the largest fiber size.
Write \(S_{u,v}\) for the free integral module of bihomogeneous polynomials of bidegree \((u,v)\) in \(X,Y\).
Form the integral matrix in monomial bases
\[
  M:\bigoplus_{g\in AB} S_{b-1,0}\longrightarrow S_{b,1},
               \qquad (H_g)_g\longmapsto\sum_g H_gF_g.
\]
It has \(N=b\binom{a+b-1}{b}=(a+b-1)\binom{a+b-2}{a-1}\) rows.
Over any algebraically closed field there is a zero product on the specified subsets if and only if \(M\) has rank less than \(N\).
Here and below a zero product has both factors nonzero.
If the rational rank is full, the exceptional prime characteristics are exactly the prime divisors of the gcd of the full-size minors.
If the rational rank is deficient, all prime characteristics admit a zero product over their algebraic closures.

Suppose a zero product on these subsets exists over a field of characteristic \(p>0\).
If
\[
                       p> c^{N/2},
\]
then \(\overline{\mathbb Q}[G]\), and hence \(\mathbb C[G]\), admits a zero product supported inside the same two sets.
If the mod-\(p\) rank defect of \(M\) is \(t\), the weaker inequality \(p^t>c^{N/2}\) suffices.
For a characteristic-\(p\) witness using every label, one may instead use \(p>c^{N_{\min}/2}\), where \(N_{\min}\) is the size of the smallest occupied row block in the universal abelian grading defined below.
At odd primes the singleton and two-cell columns admit an integral graph reduction, and a surviving mod-\(p\) rank defect in a reduced block of \(r\) rows gives the further cutoff \(p>c^r\).
In particular \(c\le\min(a,b)\) supplies a bound depending only on the two support sizes.
For torsion-free \(G\), a table meeting either test gives a counterexample to [A0002](../tasks/Yin_T_A0002_v1.md#contract) and [A0001](../tasks/Yin_T_A0001_v1.md#contract).
The single-prime conclusion permits smaller supports on transfer.
[Mghirbi–Douglas Proposition 8.3](../audits/literature/MD26/Yin_U001.md#proposition-83-and-its-quantifiers) retains every coefficient on a recurring exact pattern over infinitely many primes.

## Argument

Over an algebraically closed field \(k\), zeros of all \(F_g\) in \(Z=\mathbb P^{a-1}\times\mathbb P^{b-1}\) correspond exactly to the required zero products, up to scaling the two factors.
At such a point evaluation annihilates the image of \(M\), and some \(X_i^bY_j\) evaluates nontrivially.
Hence the rank is deficient.

Conversely suppose there is no such point.
The \(F_g\) generate \(\mathcal O_Z(1,1)\) everywhere, so their sheaf Koszul complex ending in \(\mathcal O_Z\) is exact: after local trivialization one section is a unit and contracts the complex.
Twist by \(\mathcal O_Z(b,1)\).
Its \(k'\)-th term \(E_{k'}\) is a sum of copies of \(\mathcal O_Z(b-k',1-k')\), and \(H^0(E_1)\to H^0(E_0)\) is the displayed matrix.
For \(2\le k'\le b\), the second factor has degree between \(1-b\) and \(-1\) and is acyclic.
For \(b+1\le k'\le a+b-1\), the first factor has degree between \(1-a\) and \(-1\) and is acyclic.
These vanishings on the product follow from [projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS) and [the Künneth formula over a field](https://stacks.math.columbia.edu/tag/0BEC).
Writing \(K_i=\operatorname{im}(E_i\to E_{i-1})\), one has \(K_1=E_0\) and exact sequences \(0\to K_{i+1}\to E_i\to K_i\to0\).
The cokernel of the global multiplication map injects into \(H^1(K_2)\).
The long exact sequences and the preceding vanishings inject this successively into \(H^2(K_3),\dots,H^{a+b-1}(K_{a+b})=0\), since \(Z\) has dimension \(a+b-2\).
An absent Koszul term is zero, so the reasoning also applies when the number of fibers is small.
This proves surjectivity, and completes the rank criterion in every characteristic.
This use of a bihomogeneous multiplication map is the classical Sylvester method for bilinear equations.
The integer matrix here is formed from the actual group product fibers.

Every column of \(M\) is a monomial multiple of one \(F_g\), with exactly \(\#\{(i,j):x_iy_j=g\}\) distinct unit entries.
Cancellation in a group allows at most one cell in each row and column of a fiber.
Every \(N\)-square minor has absolute value at most \(c^{N/2}\) by Hadamard's inequality.
In full rational rank some such minor is a nonzero integer.
Reduction loses rank precisely when every full minor is zero modulo the prime.
More precisely, when the rank falls by \(t\), the final \(t\) invariant factors in the integer Smith normal form are divisible by \(p\), so \(p^t\) divides every full minor.
Conversely, if every full minor vanishes over \(\mathbb Q\), it vanishes identically as an integer and in every reduction.
All rank comparisons are unchanged by extending the coefficient field.
Over \(\overline{\mathbb Q}\) the resulting projective point has coefficients in a number field because it has finitely many coordinates.
The support inclusions are sufficient to verify nonvanishing and the exact product in the original group once its actual table is supplied.

## A smaller minor from the abelian grading

Let \(\Gamma\) be the free abelian group with generators \(u_i,v_j\) modulo the differences \(u_i+v_j-u_k-v_l\) whenever \(x_i y_j=x_k y_l\).
Use the entire finitely generated abelian group, including its torsion.
Its presentation only records homogeneity of the equations and is computable from the table.
Give \(X_i,Y_j\) degrees \(u_i,v_j\).
Every column \(X^\alpha F_g\) is homogeneous, so \(M\) is the direct sum of its integer degree blocks \(M_w\).
Count the target monomials \(X^\beta Y_j\) of degree \(w\) to obtain the row size \(N_w\), and set \(N_{\min}=\min_{N_w>0}N_w\).
If a projective solution uses every input label, evaluation is nonzero on each of those monomials and annihilates the image in every block.
Thus every occupied block has deficient rank in that characteristic.
Full rational row rank requires every one of the blocks to have full row rank over \(\mathbb Q\).
For each block, a nonzero full minor is then divisible by \(p\) and bounded by \(c^{N_w/2}\).
This proves the stronger cutoff, even for \(p\)-primary torsion in \(\Gamma\), because the direct sum is indexed by degrees of monomials before any reduction.
No characters of \(\Gamma\) are required.
More precisely, one can compare \(p^{t_w}\) with the product of the largest \(N_w\) column norms in the block, where \(t_w=N_w-\operatorname{rank}_{\mathbb F_p}M_w\).
If a block has fewer than \(N_w\) columns, its deficiency is already rational.
Transposing the roles of the two sets gives a second valid grading calculation by exchanging the formal row and column variables in the same equations.
Exact support of the input is used in the all-block assertion; the complex output may still have smaller support.

## Elimination of one- and two-cell fibers

In each degree block of the monomial matrix, take one vertex for each target monomial.
Each two-entry column gives the relation \(e_u+e_v=0\) between distinct vertices, and each one-entry column kills a vertex.
Take the quotient of the free row lattice by all these relations first.
Along a spanning tree each basis vector is plus or minus a chosen root vector.
Each further edge imposes either no relation or twice that vector equal to zero, according to the parity of its fundamental cycle.
A killed vertex also kills its whole component.
The quotient is therefore a direct sum with one free generator per unanchored bipartite component and one generator of order two per unanchored nonbipartite component.
Include isolated vertices in this description.

Over \(\mathbb Q\) and all fields of odd characteristic only the \(r\) free generators remain.
Map the other columns into these free coordinates by signed summation on the bipartite components, omitting anchored and nonbipartite components.
Right exactness of the cokernel presentation identifies the cokernel of this reduced matrix with the original block cokernel over each such field.
Each reduced column has integer \(\ell^1\)-norm at most \(c\), hence Euclidean norm at most \(c\).
If the reduced matrix has full rational row rank and a rank defect \(t>0\) in odd characteristic \(p\), the same minor argument gives \(p^t\le c^r\).
When there are no larger fibers, the reduced matrix has no columns.
The projective characteristic-zero and odd-characteristic existence tests then agree for every support table of fiber sizes at most two.
This derivation controls the size of the reduced linear system when higher fibers remain.

## Support growth in a family

For \(s=a+b\), one has \(N\le(s-1)2^{s-2}\).
If the respective complex group rings in a family have no zero products on the indicated subsets, their prime characteristics satisfy
\[
 \log p\le \tfrac12(s-1)2^{s-2}\log\min(a,b).
\]
Thus along such a family with \(p\to\infty\), \(\liminf s/\log\log p\ge1/\log 2\), using natural logarithms.
With one side fixed at \(a\ge2\), the same estimate using the exact binomial coefficient gives \(\log p=O_a(b^a)\), hence \(b\gg_a(\log p)^{1/a}\).
Equivalently a family growing strictly more slowly than either applicable threshold yields a characteristic-zero zero product.
For a one-element support, multiplication by its nonzero group monomial is injective over any field.
The reviewed construction parameters in [MD26 Section 8](../audits/literature/MD26/Yin_U001.md#what-the-existing-constructions-supply) give no verified actual table meeting the single-prime test.

## A fiber with exceptional characteristic

In the cyclic group of order seven let \(A\) have exponents \(0,1,3\) and \(B\) exponents \(0,1,2,4\).
Over \(\mathbb F_2\) the all-ones factors multiply to \(1+z^7=0\) in the group ring.
Over \(\mathbb C\) any nonzero polynomial supported in \(A\) vanishes at no more than two seventh roots of unity.
Indeed a cubic with three distinct such roots and zero quadratic coefficient would force their sum to vanish.
No three distinct seventh roots sum to zero, since the minimal polynomial of a primitive seventh root is \(1+t+\cdots+t^6\), while the polynomial with ones at just three distinct exponents between zero and six cannot be its multiple.
For smaller degree the same root bound follows directly.
Any annihilating polynomial supported in \(B\) would therefore vanish at at least five distinct roots despite having degree at most four.
This is an actual table whose multiplication matrix has full rational rank and deficient rank in characteristic two.
The cyclic group has torsion and serves solely to test the characteristic-sensitive criterion.

## Assessment history

### Decision single-prime-transfer

| Field | Value |
| --- | --- |
| date | 2026-11-21T03:25 |
| status | proved |
| reason | Independent whole-proof review supports the stated result under its declared hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Projective zero products on subsets, integral rank criterion and all single-prime cutoffs. |
| argument | [Argument](#argument) | Full proof including graded blocks, odd-prime graph quotient, growth estimates and the cyclic comparison. |
| review | [Whole finding](../audits/reviews/Yin_R_A0129_v1.md#whole-finding) | Complete independent review of the fixed statement, proof and direct interfaces. |

## Current assessment

[Selected decision](#decision-single-prime-transfer)
