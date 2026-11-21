---
author: Yin
---
# Phase rigidity and finite translation chains for three left labels

## Statement

Let \(G\) be torsion-free, let \(g_1,g_2,g_3\) be distinct, and suppose
\[
 \alpha=\sum_{i=1}^3 a_i g_i,\qquad
 \beta=\sum_{b\in B}v_b b,\qquad
 a_i,v_b\in\mathbb C^\times,\qquad
 0\ne\beta,\quad \alpha\beta=0.
\]
The set \(B\) is finite, and both displayed supports are exact.
Every actual product fiber has two or three cells, because a singleton cannot cancel and group cancellation permits at most one cell from each left row.

### Pure pair fibers

If every actual fiber has two cells, then
\[
                         |a_1|=|a_2|=|a_3|.                 \tag{1}
\]
Join two column labels in a graph whenever their cells form a product pair, retaining multiple edges.
The two cells have different rows and different columns.
On each connected component of this pair graph, the moduli \(|v_b|\) are constant.
Restricting \(\beta\) to any component still gives a zero product with the same \(\alpha\).
In particular a right annihilator of minimal support has connected pair graph.

There is also rigidity of all the coefficient phases, without assuming algebraicity of the original coefficients.
Let
\[
 M=\mathbb Z^{\{1,2,3\}\sqcup B},\qquad
 L=\langle e_i+f_b-e_j-f_{b'}:
                  \{(i,b),(j,b')\}\text{ is a full fiber}\rangle,
 \qquad S=(L\otimes\mathbb Q)\cap M.
\]
If \(B_1,\ldots,B_t\) are the connected pair-graph components, then
\[
 S=\left\{\sum_i u_i e_i+\sum_b w_bf_b:
              \sum_i u_i=0,\quad
              \sum_{b\in B_j}w_b=0\ (1\le j\le t)\right\}.
                                                                    \tag{2}
\]
Thus \(\operatorname{rank}L=|B|+2-t\).
Every left ratio \(a_i/a_j\), and every right ratio \(v_b/v_{b'}\) within a connected component, is a root of unity.
If \(e\) is the exponent of \(S/L\), all these roots have order dividing \(2e\).

Normalize \(a_1=1\) and one \(v_b=1\) in each pair-graph component.
There are exactly \([S:L]\) complex solutions of the pair equations after this normalization.
In particular, on a connected right support the normalized coefficient set is finite.
Equation (2) is a necessary rational-rank test for a complex lift of an actual torsion-free pair table with three left labels.
It is not a proof that a table passing the test is realizable or that its remaining finite branches can all be excluded.

### What triples permit and force

Put \(r_i=|a_i|\), \(M_0=\max_{b\in B}|v_b|\), and \(B_{\max}=\{b:|v_b|=M_0\}\).
If one \(r_i\) is strictly greater than the other two, then every output \(g_i b\), \(b\in B_{\max}\), is a triple fiber.
Consequently there are at least \(|B_{\max}|\) triple fibers.

If \(r_i=r_j>r_k\), let \(x=g_j^{-1}g_i\) and decompose \(B_{\max}\) into its finite consecutive \(x\)-chains.
Each such chain forces two distinct triple outputs, and outputs forced by different chains are distinct.
In particular at least two triple fibers are necessary in this case.
Thus the equality-of-moduli and phase conclusions above cannot simply be transferred from pair-only tables to mixed tables.

### A quantitative chain constraint for all fibers

For each pair \(i\ne j\), let \(m_{ij}\) be the largest number of vertices in a consecutive chain
\[
                   b,xb,\ldots,x^{m-1}b\ \subseteq B,
                   \qquad x=g_i^{-1}g_j.
\]
Isolated vertices are chains of length one.
The element \(x\) has infinite order, so all the translation components on finite \(B\) are paths.
For \(\{i,j,k\}=\{1,2,3\}\), every complex zero product satisfies
\[
       \left|r_k^2-r_i^2-r_j^2\right|
             \le 2r_i r_j
                    \cos\!\left(\frac{\pi}{m_{ij}+1}\right).
                                                                    \tag{3}
\]
This includes arbitrary coefficient phases and any number of triple fibers.
It implies the strict triangle inequalities
\[
                         |r_i-r_j|<r_k<r_i+r_j.              \tag{4}
\]
For example, if \((r_1,r_2,r_3)=(19/10,1,1)\), the right support must contain a chain of at least four vertices for \(g_2^{-1}g_3\).
This identifies a particular ratio and a stronger progression than the [coefficient-free three-vertex conclusion](Yin_C_A0098_v1.md#statement) in this modulus regime.
It does not exclude longer chains.

## The maximal-modulus argument

Suppose first that \(r_1\) is uniquely largest.
At an output \(g_1b\) with \(b\in B_{\max}\), a two-cell equation would give
\[
               a_1v_b=-a_jv_{b'},\qquad
               |v_{b'}|=(r_1/r_j)M_0>M_0,
\]
which is impossible.
A singleton is also impossible.
Hence that output must have all three representations.
Different \(b\)'s give different outputs by cancellation.

Now suppose \(r_1=r_2>r_3\) and all fibers are pairs.
For \(b\in B_{\max}\), the cell \(g_1b\) can only pair with \(g_2b'\), with \(b'\in B_{\max}\).
It follows that \(g_1B_{\max}\subseteq g_2B_{\max}\).
These finite sets have equal cardinality, so they are equal.
The nonidentity element \(g_2^{-1}g_1\) then stabilizes the finite nonempty set \(B_{\max}\).
A positive power fixes a point, forcing this element to have finite order, contrary to torsion-freeness.
The uniquely largest case and this tied case prove (1).

For the stronger mixed-fiber statement in the tied case, use the full translation graph of \(x=g_2^{-1}g_1\) on \(B_{\max}\), whether the associated output is a pair or a triple.
A maximal chain is
\[
                 b,xb,\ldots,x^{q-1}b.
\]
At its terminal cell \(g_1x^{q-1}b\), pairing with row two would require \(x^qb\in B_{\max}\), and pairing with row three would require a coefficient larger than \(M_0\).
Both are impossible, so this is a triple.
At the other end, the output \(g_2b\) must likewise be a triple because \(x^{-1}b\notin B_{\max}\).
The two outputs cannot coincide, since that would give \(x^qb=b\).
Nor can outputs of the two different kinds from distinct chains coincide: such an equality would put the end of one chain next to the start of the other in the same translation graph.
Outputs of the same kind are distinct by cancellation.
This proves the stated count.

Under pure pairing, (1) makes the moduli of two column coefficients equal along every edge, and hence on each connected component.
Each full fiber incident to a component stays inside that component.
Consequently all its coefficient equations remain valid after deleting the other components, proving the restriction assertion.

## Saturation forced by three rows

For any real linear form \(\ell:M\to\mathbb R\) vanishing on \(L\), and any positive real \(t\), replace the coefficients by
\[
             a_i(t)=a_it^{\ell(e_i)},\qquad
             v_b(t)=v_bt^{\ell(f_b)}.
                                                                    \tag{5}
\]
Each pair equation acquires a common nonzero monomial factor, so the product is still zero with exactly the same supports.
Apply (1) to every member of this family.
Since the original left moduli are equal, this forces
\[
                         \ell(e_i-e_j)=0
                           \qquad\text{for all }i,j.
\]
The annihilator of the real relation space is precisely the space of these forms.
Thus \(e_i-e_j\in(L\otimes\mathbb R)\cap M=S\).
The final equality holds because the relation space is rational.

For an edge between columns \(b,b'\), its pair difference gives
\[
 f_b-f_{b'}=(e_i+f_b-e_j-f_{b'})-(e_i-e_j)\in S.
\]
Following paths puts every column difference within one component in \(S\).
These row and column differences generate the right side of (2).
Conversely every generator of \(L\) has row sum zero and column sum zero separately in each component, so its saturation is contained in that same subgroup.
This proves (2), including its rank.

The coefficient assignment is a character \(z:M\to\mathbb C^\times\).
Each pair difference has value \(-1\); hence \(z(L)\subseteq\{1,-1\}\).
For \(s\in S\), the definition of the exponent \(e\) gives \(es\in L\), and therefore \(z(s)^{2e}=1\).
This proves the root-of-unity assertions for the given solution, even if its unnormalized scalar factors were transcendental.

The differences \(e_2-e_1,e_3-e_1\), together with \(f_b-f_{b_j}\) for each nonreference column \(b\in B_j\), give an integral basis of \(S\).
The chosen reference row and reference column in each component give a complementary free summand of \(M\).
The normalizations fix the character on that complement.
On \(L\) the values form a well-defined character \(\chi:L\to\{1,-1\}\), since the original solution exists.
Its extensions to \(S\) form a torsor under \(\operatorname{Hom}(S/L,\mathbb C^\times)\), a group with \([S:L]\) elements.
Each extension solves all pair equations, and the complement normalization makes its extension to \(M\) unique.
This proves the exact count.

The general character-extension mechanism is already in [C22](Yin_C_A0022_v1.md#equal-moduli-for-the-paired-coefficient-equations) and [C26](Yin_C_A0026_v1.md#coefficient-table-and-statement).
The additional three-row conclusion is that the required row saturation, and then the complete componentwise saturation (2), are forced by torsion-freeness and the maximum-modulus argument.
This is not the dimension estimate obtained by projective boundary pruning in [C33](Yin_C_A0033_v1.md#cutting-a-component-by-product-coordinates).

## Signs and finite characters are separate requirements

The phase rigidity does not by itself replace the normalized coefficients by signs.
For the character \(\chi\) on \(L\), a sign assignment on all row and column labels exists exactly when
\[
                           \chi(L\cap2M)=\{1\}.              \tag{6}
\]
Necessity follows because a sign character is trivial on \(2M\).
For sufficiency, (6) makes \(\chi\) a well-defined linear character on the image of \(L\) in \(M/2M\), and every linear functional on a subspace of this finite-dimensional \(\mathbb F_2\)-space extends to the whole space.
Equivalently, solve the pair-incidence equations with right side one over \(\mathbb F_2\).
This is a different test from the integer-relation consistency criterion for complex coefficients.

An odd index \([S:L]\) is sufficient for (6).
Indeed if \(2m\in L\), saturation first gives \(m\in S\); its class in \(S/L\) has order dividing two, so oddness implies \(m\in L\), and \(\chi(2m)=\chi(m)^2=1\).
For even index, (6) must still be checked.
The assertion here is sufficiency, not necessity of an odd index.

Nor does a root-of-unity assignment to coefficient variables supply a finite group character on \(G\).
The pair equations verify phase consistency around cycles of the finite pair graph.
A homomorphism on the subgroup generated by the group labels must additionally respect all of its group relations.
No claim that the finite pair graph checks those relations is made.
Likewise, passing to a product with a finite cyclic phase group introduces torsion and does not preserve the torsion-free task.

At characteristic two, a three-label full-support zero product over \(\mathbb F_2\) has only pair fibers: every nonzero coefficient is one, while a triple sum is one.
Such a table need not satisfy the complex character-consistency condition.
The [actual cyclic order-seven example in C93](Yin_C_A0093_v1.md#a-fiber-with-exceptional-characteristic) has this behavior.
Its ambient group has torsion and is used only to distinguish coefficient fields.
The present results provide necessary tests for a complex lift of a torsion-free binary candidate; they do not make that lift automatic.

## The finite-chain estimate

Fix \(x=g_i^{-1}g_j\), and let \(P_B\) be coordinate projection onto \(\mathbb C[B]\).
The compression \(P_B\lambda(x)P_B\) is a direct sum of finite directed path shifts, because \(x\) has infinite order.
The longest path has \(m=m_{ij}\) vertices.
For every phase \(\theta\), its Hermitian part
\[
 \frac12\left(e^{i\theta}P_B\lambda(x)P_B
                +e^{-i\theta}P_B\lambda(x^{-1})P_B\right)
\]
is unitarily conjugate, on each path, to one half of its ordinary adjacency matrix.
A diagonal gauge along that path removes the phase.
The sine eigenvectors give largest eigenvalue \(\cos(\pi/(q+1))\) on a \(q\)-vertex path, as in the [existing path-block calculation](Yin_C_A0005_v2.md#path-blocks-and-the-exact-kernel-dimension).
Taking the largest block and then the supremum over \(\theta\) gives
\[
       |\langle\lambda(x)\beta,\beta\rangle|
               \le\cos\!\left(\frac{\pi}{m+1}\right)\|\beta\|_2^2.
                                                                    \tag{7}
\]
The bound is sharp for this compressed shift: a sine vector on a longest path, with the appropriate diagonal phase, attains it.
Sharpness of the shift estimate does not assert existence of a group-ring zero product attaining it.

From \(\alpha\beta=0\),
\[
                a_kg_k\beta=-(a_ig_i\beta+a_jg_j\beta).
\]
Using the inner product linear in its first argument, taking squared norms yields
\[
 (r_k^2-r_i^2-r_j^2)\|\beta\|_2^2
       =2\operatorname{Re}
          \bigl(a_i\bar a_j\langle g_i\beta,g_j\beta\rangle\bigr).
\]
The absolute inner product on the right is
\(|\langle\beta,\lambda(g_i^{-1}g_j)\beta\rangle|\).
Apply (7) and divide by the nonzero norm to obtain (3).
Since the cosine is strictly less than one and \(r_i,r_j>0\), the two strict inequalities in (4) follow.

For the numerical example,
\[
 \frac{(19/10)^2-1-1}{2}=\frac{161}{200}
          >\cos(\pi/4)=1/\sqrt2.
\]
Thus \(m_{23}\le3\) would contradict (3), proving \(m_{23}\ge4\).
More generally the bound becomes a chain-length obstruction as a coefficient approaches the sum of the other two moduli.
It supplies no uniform contraction when the chain lengths are unrestricted.

## Literature and remaining scope

[Abdollahi–Taheri, Theorem 1.1 and its proof in Section 2](https://arxiv.org/pdf/1905.09494v1#page=2), already reduce rational three-term zero divisors to a signed integral left factor by reduction at primes.
That result allows triple fibers but assumes rational left coefficients.
The pair-only phase theorem here treats arbitrary complex coefficients and obtains a finite set of normalized phases through the actual pair lattice.
[Abdollahi–Soleimani Malekan, Theorem 1.1](https://arxiv.org/pdf/1905.00951#page=2), give a coefficient-norm sufficient condition for regularity.
The estimate (3) instead retains the finite translation-chain geometry of the particular right support.
These source comparisons do not assert priority for every intermediate elementary inequality.

The mixed case can contain genuine three-term sums with unequal moduli.
In that case the torus deformation (5) generally fails to preserve those sums, and neither (1) nor (2) follows from the argument.
The [single-residual-fiber criterion](Yin_C_A0026_v2.md#exactly-one-larger-fiber) and the [saturated triple obstruction](Yin_C_A0025_v1.md#statement) remain applicable under their own additional hypotheses.
For general three-left-label tables, the results above constrain phases, triples and translation chains but leave the zero-divisor question open.

## Assessment history

### Decision phase-and-chain

| Field | Value |
| --- | --- |
| date | 2026-11-21T05:07 |
| status | proved |
| reason | The independent inspection verifies the stated deductions and the applicability of the identified inputs at the recorded scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized phases for pair fibers, mixed-fiber constraints and the three-label chain estimate. |
| argument | [Proof](#the-maximal-modulus-argument) | Maximal moduli, saturation and sign tests, compressed paths and the comparison to known rational results. |
| review | [Whole finding](../audits/reviews/Yin_R_A0135_v1.md#whole-finding) | Full inspection with its stated dependency and example limits. |

## Current assessment

[Selected decision](#decision-phase-and-chain)
