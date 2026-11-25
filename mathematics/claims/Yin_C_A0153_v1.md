---
author: Yin
---

# Vanishing orders for rational matrix coefficients with varying group support

## Statement

Let \(G\) be a finitely generated discrete group, \(U=L^0(\mathcal N(G))\), and let \(D_G\) and \(R_G\) be the division closure and the \(*\)-regular closure of \(\mathbb CG\) in \(U\).
Fix \(n\ge1\) and \(d\ge0\).
Consider the [polynomial realizations](Yin_C_A0149_v1.md#statement)
\[
 f(z)=\alpha L(z)^{-1}\beta,\qquad L\in M_n(\mathbb CG[z]),\qquad \deg L\le d,
\]
with constant complex row and column \(\alpha,\beta\), a central indeterminate \(z\), and \(L\) invertible over \(U((z))\).

Suppose \(R_G\) embeds as a unital complex algebra in a product of rings \(M_{m_i}(K_i)\), where the \(K_i\) are division algebras over \(\mathbb C\) and \(m_i\le m<\infty\).
This includes the case of semisimple Artinian \(D_G\), with \(m\) the largest of its simple matrix sizes.
If \(n\ge2\) and \(0\ne f\in z^N U[[z]]\), then
\[
                       N\le ((n-2)m+1)d.                         \tag{1}
\]
For \(n=1\), a nonzero \(f\) cannot have positive order.
For \(n\ge2\) the bound in (1) is attained over each single matrix algebra \(M_m(\mathbb C)\), and over a finite group algebra whenever its largest simple matrix size is \(m\).
Taking \(N>((2n-2)m+1)d\) suffices for all three [zero, constant and idempotent tests](Yin_C_A0149_v1.md#statement) at size \(n\) with unrestricted group support.
In particular \(m=1\) gives the sharp zero-test bound \((n-1)d\) when \(D_G\) is a division ring.

For general \(G\), a bound on the **number** of group elements occurring in \(L\) does not suffice.
In the two-generator elementary amenable group \(\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)\rtimes\mathbb Z\) there are fixed integers \(n_*,s_*\) and, for each \(k\ge2\), a nonzero realization of order exactly \(k\) with size \(n_*\), degree one, and at most \(s_*\) group elements across all entries of its coefficients.
Its pivot is already invertible at zero.
This group has torsion, and the counterexample concerns uniform finite determination for realizations in an individual group.
The [deletion question for torsion-free groups](../tasks/Yin_T_A0003_v3.md#contract) remains open.

## Argument

### The bound over a division algebra

First use coefficients in \(M_b(K)\), where \(K\) is a complex division algebra, and assume \(L\) is invertible over \(K((z))\) after expanding its blocks.
Write \(P=K[[z]]\) and use right vector spaces over \(K\).
Let \(f\ne0\) have entries in \(z^NP\), with \(N\ge1\), and put \(r=\operatorname{rank}_{K((z))}f\).
The scalar row and column are nonzero.
Independent constant complex changes of bases on the two sides of \(L\) make each of them select the first block coordinate.
In the matrix
\[
 B=\begin{pmatrix}L&-\beta\\ \alpha&0\end{pmatrix}
\]
the two selected blocks of size \(b\) are respectively \(-I_b\) and \(I_b\).
Eliminating on these blocks leaves the submatrix \(C\) of \(L\) obtained by deleting its first block row and column.
Over the division ring \(K((z))\), elimination on \(L\) gives \(\operatorname{rank}B=nb+r\).
Consequently \(C\) has rank \(h=(n-2)b+r\).
Choose an invertible \(h\)-by-\(h\) submatrix \(A\) of \(C\), allowing the empty matrix for \(h=0\).
Adjoin both sets of constant pivot rows and columns to \(A\) inside \(B\).
The resulting square submatrix \(W\) has size \(h+2b=nb+r\) and is equivalent over \(K[z]\) to \(\operatorname{diag}(I_{2b},A)\) by the same constant pivots.

For a matrix over \(P\), write \(T_N\) for multiplication modulo \(z^N\) on coefficient columns of length \(N\).
Replacing the lower-right zero block of \(B\) by \(-f\) makes its Schur complement zero, so the corresponding submatrix \(W'\) has rank at most \(nb\) over \(K((z))\).
All entries of \(W'\) lie in \(P\).
At least \(r\) rows can be made zero by invertible row and column operations over \(P\).
Indeed, pivot on an entry of smallest order, for which every quotient needed to clear its row and column has nonnegative order, and repeat on the remaining matrix.
Since \(W=W'\pmod {z^N}\), the \(K\)-corank of \(T_N(W)\) is at least \(rN\).
The equivalence to \(\operatorname{diag}(I_{2b},A)\) identifies this corank with the \(K\)-nullity of the square \(T_N(A)\).

A polynomial column \(v\) of degree less than \(N\) in that kernel has \(Av\) supported on degrees \(N,\ldots,N+d-1\).
The assignment \(v\mapsto Av\) is injective since \(A\) is invertible over \(K((z))\).
The indicated coefficient space has dimension \(hd\), so
\[
                       rN\le ((n-2)b+r)d .                       \tag{2}
\]
For \(n=1\), \(f\) is a nonzero complex multiple of \(L^{-1}\), hence \(r=b\), and the right side is zero.
For \(n\ge2\), \(r\ge1\) and (2) gives (1) with \(m=b\).

### Sharpness and passage to group coefficients

For \(n\ge2\), designate the first block as input and the last as output in \(\mathbb C^{nm}\).
Choose a chain of coordinate vectors starting at the first input coordinate, passing through all \((n-2)m\) coordinates in the middle blocks, and ending at the first output coordinate.
Let \(T\) send each chain vector to its successor and kill the last vector and every coordinate outside the chain.
Take \(L=I-z^dT\) with input and output the designated block inclusions and extractions.
The finite geometric expansion of \(L^{-1}\) gives \(f=z^{((n-2)m+1)d}E_{11}\), including \(d=0\).
For a finite group with largest simple matrix size \(m\), use this \(T\) in that summand of its complex group algebra and zero in the remaining summands.
The other outputs are zero because the chosen input and output block coordinates are distinct.

For the group realization in the statement, the entries of \(L^{-1}\) lie in the formal scalar division closure, and every Laurent coefficient of each such entry lies in \(R_G\). [Formal scalar inversion](Yin_C_A0143_v1.md#formal-inversion-by-scalar-pivots) and [Laurent coefficients](Yin_C_A0141_v1.md#statement)
The given embedding thus sends both inverse identities coefficientwise to each division-algebra component.
A nonzero coefficient of \(f\) survives in at least one component, where (2) applies.
If \(D_G\) is semisimple Artinian, it is regular and closed under adjoints, so its relative inverses computed in \(U\) belong to \(D_G\), giving \(R_G=D_G\). [Regular closure and relative inverses](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)
For the constant and idempotent tests apply the zero test at size \(2n\) to \(f(z)-f(2z)\) and \(f^2-f\) in their [degree-preserving block realizations](Yin_C_A0149_v1.md#constant-jets-and-idempotent-jets).
Descent of a constant series gives the asserted membership in \(D_G\).

### Finite subgroup averages of bounded realization size

Use the finite presentation of \(\Gamma=\operatorname{SL}_3(\mathbb Z)\) on the six elementary matrices. [Steinberg presentation in Young, §2.3, equation (1), p. 975](https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n3-p04-p.pdf#page=7)
For every quotient onto a finite group \(Q\), take the corresponding finite cover of its presentation complex.
With cellular coordinates chosen as right modules, its first two complex boundary maps are group-ring matrices \(D_1,D_2\) acting by left multiplication, obtained from the same fixed attaching words in each quotient.
Their dimensions and the number of group elements in their coefficients are bounded independently of \(Q\).
The fundamental group of the cover is the finite-index kernel of \(\Gamma\to Q\).
It inherits Kazhdan's property (T) from \(\Gamma\). [Property (T) and finite-index restriction](Yin_C_A0121_v1.md#the-obstruction-to-an-amenable-action)
Its abelianization is finite, since it is finitely generated and an infinite finitely generated abelian group has a quotient \(\mathbb Z\), which lacks property (T).
Thus the cover has zero complex first homology, or \(\ker D_1=\operatorname{im}D_2\).
It follows from the orthogonal decomposition of the degree-one chains into \(\operatorname{im}D_1^*\) and \(\operatorname{im}D_2\) that
\[
 \Delta=D_1^*D_1+D_2D_2^*\quad\text{is invertible},\qquad
 e_Q=1-D_1\Delta^{-1}D_1^*=\frac{1}{|Q|}\sum_{q\in Q}q .
\]
Indeed \(D_1\Delta^{-1}D_1^*\) is the orthogonal projection onto \(\operatorname{im}D_1\), the orthogonal complement of the constants because the cover is connected.
The operator \(\Delta^{-1}\) belongs to the same matrix algebra over \(\mathbb CQ\), as follows from the finite-dimensional inverse identity.
The displayed expression for \(e_Q\) therefore has a fixed number of matrix entries and a bounded number of group elements before inversion, even when \(|Q|\) grows.

### A finite permutation delaying the first nonzero coefficient

Let \(k\ge2\), choose \(k\) distinct odd primes \(p_i\), and use the quotient \(Q=\prod_{i=1}^k\operatorname{SL}_3(\mathbb F_{p_i})\) of \(\Gamma\).
Reduction is onto because elementary transvections generate each factor by elimination, and the Chinese remainder theorem lifts any one of their parameters with zero parameters in all the other factors.
The element \(\operatorname{diag}(-1,-1,1)\) in the \(i\)-th factor gives commuting independent involutions \(v_1,\ldots,v_k\).
Write \(V\) for their span as a vector space over \(\mathbb F_2\).
Realize \(Q\) by left translations on its underlying finite set.
There are at least two right cosets \(Vx\).
In each coset define a permutation \(s(vx)=A_x(v)x\) after choosing one representative \(x\).
Choose the linear isomorphism \(A_x\) to send each \(v_i\) with \(i<k\) to \(v_{i+1}\), using \(v_1\) for the image of \(v_k\) in the identity coset and \(v_1+v_2\) in the others.
Both choices are invertible.
Then \(sv_i s^{-1}=v_{i+1}\) for \(i<k\), whereas \(sv_ks^{-1}\) acts by two different translations on the indicated cosets and cannot be a single left translation in \(Q\).

Embed \(\operatorname{Sym}(Q)\) on a finite subset of \(\mathbb Z\) and put \(t=s^{-1}\).
The ambient group \(G=\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)\rtimes\mathbb Z\) is generated by the integer shift and the transposition \((0,1)\), since its conjugates give all adjacent transpositions.
The permutation subgroup is locally finite, so this extension is elementary amenable.
Consider
\[
                    g_k(z)=(1-v_1)(1-zt)^{-1}e_Q .
\]
Its coefficient in degree \(j\) equals \(t^j(1-t^{-j}v_1t^j)e_Q\).
For a group element \(u\), \((1-u)e_Q=0\) exactly when \(u\in Q\), by the supports of the two coset sums.
The conjugates for \(0\le j<k\) are the indicated \(v_{j+1}\), while the conjugate for \(j=k\) lies outside \(Q\).
This proves the exact order \(k\).

For an explicit realization let \(a\) be the number of generators in the fixed presentation and take the upper triangular block pivot
\[
 \begin{pmatrix}
 1 & -(1-v_1) & 0 & 0\\
 0 & 1-zt & -1 & D_1\\
 0 & 0 & 1 & 0\\
 0 & 0 & 0 & \Delta
 \end{pmatrix}.
\]
Use the block column \(\left(\begin{smallmatrix}0\\0\\1\\D_1^*\end{smallmatrix}\right)\) and read the first output coordinate.
Back substitution gives \(g_k\).
To obtain a constant complex input column, append one scalar pivot \(1\), placing the negative of this entire stacked column above it, and select the new last input coordinate.
The size is \(a+4\) and the only coefficient of positive degree is \(-t\).
The group elements in \(D_1,D_1^*,\Delta\) belong to the images of a single finite set of words in the fixed presentation, while \(v_1,t,1\) contribute at most three further elements.
The resulting cardinality bound is independent of \(k\), and every diagonal block is invertible at zero.
Since \(g_k\) has positive order, its defect \(g_k^2-g_k\) also has exact order \(k\).
Thus the same examples invalidate the uniform constant and idempotent tests with this cardinality condition.

## Assessment history

### Decision varying-group-support

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:46 |
| status | proved |
| reason | Skew-field truncations bound the vanishing order without a support condition, while finite subgroup averages in one elementary amenable group give arbitrary orders at fixed support cardinality. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The sharp matrix-size bound over bounded products of matrix rings and the degree-one counterexample with torsion. |
| argument | [Argument](#argument) | Rank comparisons over a division algebra, an extremal chain, finite-cover Laplacians and shifted finite permutations. |
| dependency | [Formal coefficients](Yin_C_A0141_v1.md#statement) | Coefficients in the regular closure. |
| dependency | [Formal matrix inverses](Yin_C_A0143_v1.md#formal-inversion-by-scalar-pivots) | Laurent inverses in the scalar closure. |
| dependency | [Finite determination](Yin_C_A0149_v1.md#constant-jets-and-idempotent-jets) | Double-sized transfer matrices for constant and idempotent tests. |
| dependency | [Relative inverses](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Identification of the two closures when the division closure is semisimple Artinian. |
| dependency | [Integral presentation](../audits/literature/You13/Yin_U001.md#you13-u001) | Six elementary generators and finitely many relators at rank three. |
| dependency | [Property (T)](Yin_C_A0121_v1.md#the-obstruction-to-an-amenable-action) | The property for the integral special linear group and finite-index restriction. |
| review | [Varying support](../audits/reviews/Yin_R_A0171_v1.md#varying-support) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-varying-group-support)
