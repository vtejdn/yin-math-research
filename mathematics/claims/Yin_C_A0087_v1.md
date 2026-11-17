---
author: Yin
---

# Separating cyclic spectral packets in different rows of the original matrix

## Statement

Fix a non-elementary torsion-free word-hyperbolic group \(G\).
For the conjugation-shell conclusions use an individual four-line realization in the [scope of C80](Yin_C_A0080_v1.md#statement).
Let \(A\in M_{r,m}(\mathbb CG)\), partition its rows into blocks of sizes \(r_i\), and choose pairwise nonconjugate maximal cyclic subgroups \(H_i=\langle t_i\rangle\), one for each block.
Suppose there is a finite group-ring matrix \(J\in M_{m,r}(\mathbb CG)\) with
\[
                  AJ=\operatorname{diag}_i P_i(t_i),                    \tag{1}
\]
where every \(P_i\) is a square complex Laurent matrix of size \(r_i\) with nonzero determinant.
This condition allows several cyclic directions and right linear combinations of columns.
Given the stated subgroups, finite candidate supports of \(J\) and Laurent degree bounds for the \(P_i\), the identity and nonzero determinants in (1) can be tested by original group-product comparisons and finite polynomial algebra.

In block \(i\), collect each coefficient column in right cosets \(H_i x\) as \(\sum_x F_{i,j,x}(t_i)x\).
Use the same representative for a coset throughout the block.
Concatenate all these Laurent columns into \(F_i\) and choose a basis matrix \(D_i(t_i)\) of their Laurent column module.
Each basis has \(r_i\) columns.
Then \(A=D T\), \(D=\operatorname{diag}_i D_i(t_i)\), where \(D\) is injective with dense range and \(T\) is a finite group-ring matrix mapping onto \(\ell^2(G)^r\) with a positive lower bound for \(TT^*\).
Consequently \(\dim_G\ker A=m-r\), and the range of \(A\) is closed exactly when every \(F_i(z)\) has row rank \(r_i\) for every \(|z|=1\).
The construction obtains the same-kernel closed-range matrix from the coefficients and (1).
The case of one cyclic block and an actual selected minor is the [cyclic-minor theorem](Yin_C_A0081_v1.md#statement).

In the nonclosed case let \(d\) be the largest multiplicity of any unit-circle zero of a Laurent invariant factor of any \(D_i\), and put \(\alpha=1/(2d)\).
For \(Q=I-A^*A/M\) with \(M>\|A\|^2\), the positive spectral mass below \(s\) for \(I-Q\) is comparable to \(s^\alpha\) at zero.
The kernel projection \(p\) has an exponentially weighted Fourier square sum.
On the four-line group take the [C76](Yin_C_A0076_v1.md#statement) time choices with \(\beta\ge0,\ \kappa\alpha>\beta\).
With the notation of [C80, equation (1)](Yin_C_A0080_v1.md#statement), the *original* widened-shell conjugation defect satisfies
\[
 t_j=\|1_{S_j^+}(I-\mathsf P)\widehat K_j\|_2
              \le C\big(e^{-c 2^j}+2^{-\kappa\alpha j/2}\big).         \tag{2}
\]
Choosing the C80 widening constant \(a>\kappa\alpha/(2\log_2(1/\rho))\), this gives for \(R=2^J\) sufficiently large
\[
        \|B_\bullet\|_{\beta,\,|g|\ge R}^2
                 \le C'\big(e^{-c' R}+R^{-(\kappa\alpha-\beta)}\big).    \tag{3}
\]
The constants and the spectral normalizations refer to the individual group and matrix.

Every such four-line group admits an explicit two-row form satisfying (1) whose row Gram support requires the entire nonfree group.
It has nonclosed range, kernel of von Neumann dimension one, and no full-rank square block over a single cyclic subgroup, even after group-ring right column combinations and independent row and column translations by group elements.
One choice of its coefficient yields no nonzero finitely supported null vector, so its actual projection has infinite support.

## Argument

The constraints in (1) with the specified finite supports are linear equations on coefficients, obtained by equating the coefficient of each group product.
On their complex solution space the product of the determinants of the Laurent blocks, considered in independent commuting variables for the blocks, must be a nonzero Laurent polynomial at some point.
This is equivalent to one of its Laurent coefficients being a nonzero polynomial on the parameter space, since \(\mathbb C\) is infinite.
Thus testing these finite candidate bounds requires neither a spectral estimate nor prior knowledge of a closed-range substitute.
No search bound for all feasible certificates is asserted.

Projection of the products \(AJ\) in row block \(i\) onto \(H_i\) puts each column of \(P_i\) in the Laurent span of \(F_i\).
Indeed the contribution of \(F_{i,j,x} xJ_{j,l}\) to this projection is \(F_{i,j,x} E_{H_i}(xJ_{j,l})\), with the last coefficient in \(\mathbb C H_i\).
The nonzero determinant implies full module rank.
The Laurent polynomial ring is a principal ideal domain, so taking a free basis gives \(F_i=D_i F'_i\) with \(\det D_i\ne0\) and \(F'_i\) having a Laurent right inverse.
Reassembling the coefficients of \(F_i'\) gives \(A=D T\).
Each \(D_i\) acts by its circle multiplier on the right cosets of \(H_i\) and hence is injective with dense range.
In particular \(TJ=Y\) is block diagonal: all its off-block columns vanish by injectivity, and its diagonal blocks \(Y_i\) have support in \(H_i\).
For the last assertion, left multiplication by \(D_i\) preserves each right coset of \(H_i\), and the equation on every coset other than \(H_i\) has zero right side.
Thus \(D_iY_i=P_i\) over the Laurent ring with \(\det Y_i\ne0\).

## Angular separation and the Gram lower bound

Let \(\Lambda_i\) be the finite unit-circle zero set of \(\det Y_i\).
Let \(E_{i,\delta}\) project spectrally for \(t_i\) onto the union of chordal \(\delta\)-neighborhoods of \(\Lambda_i\), with the zero projection for an empty set.
For \(i\ne j\) and any fixed \(g\in G\),
\[
                \|E_{i,\delta}\,g\,E_{j,\delta}\|=O_{i,j,g}(\delta^{1/3}).
                                                                        \tag{4}
\]
The same estimate holds for \(i=j\) when \(g\notin H_i\).
Indeed the boundary fixed-point pair of \(t_i\) and that of \(g t_jg^{-1}\) are disjoint in these cases.
An element fixing one of the two points for \(H_i\) belongs to \(H_i\), which is the stabilizer of the pair by maximal cyclicity in this torsion-free group.
If the pairs share a point, \(g t_jg^{-1}\) therefore lies in \(H_i\) and fixes the whole pair.
It follows that \(gH_jg^{-1}=H_i\) by the same stabilizer property, and in the same-block case that \(g\in H_i\). [Boutonnet–Carderi, Lemma 2.2 and proof](../literature/pdf/BC15--arxiv-v2.pdf#page=6)

For disjoint pairs, sufficiently large positive and negative powers of both elements send the complement of their repelling neighborhoods into disjoint attracting neighborhoods, so common powers of exponent \(q\) freely generate by ping-pong.
For a packet on an arc about \(\lambda\), replacing the vector by the mean of the first \(N\) powers of \(\bar\lambda^q t_i^q\) changes it by at most \(q(N+1)\delta/2\) times its norm.
The same holds on the translated arc for the other generator.
The product of the adjoint of the first phase average with the second has norm at most \(2/\sqrt N\): on the free cosets split at the projection onto words beginning with the first generator's syllable, and use disjoint translates of the complementary starting cones for the respective averages. [Two-generator average estimate](Yin_C_A0081_v1.md#spectral-packets-along-a-maximal-cyclic-subgroup)
Thus for one pair of arcs the norm is at most \(2/\sqrt N+q(N+1)\delta\).
Splitting overlapping arc unions into disjoint pieces and summing over at most \(|\Lambda_i||\Lambda_j|\) pairs gives (4) with \(N=\lceil\delta^{-2/3}\rceil\).

Put \(E=\operatorname{diag}_i E_{i,\delta}I_{r_i}\).
For the \(i,i\) block of \(TT^*\) one has
\[
               E_{H_i}((TT^*)_{ii})=F_i'(F_i')^*\ge b_0 I_{r_i}
\]
with a common \(b_0>0\) by the Laurent right inverses and compactness.
Products from different right cosets of the same input column fall outside \(H_i\), which gives the equality.
All the remaining terms of the matrix have compressed norm total at most \(C\delta^{1/3}\) by (4).
Within diagonal blocks these are precisely the coefficients outside \(H_i\); between two different blocks (4) applies to every coefficient, including the identity.
Choosing \(C\delta^{1/3}<b_0/2\) gives \(ETT^*E\ge b_0E/2\).
Outside the arcs, the least singular values of \(Y_i\) have a common positive lower bound \(\sigma_\delta\), so
\[
  \|(I-E)\xi\|\le\sigma_\delta^{-1}\|Y^*\xi\|
           \le (\|J\|/\sigma_\delta)\|T^*\xi\| .
\]
Using \(\|E\xi\|\le(2/b_0)^{1/2}\big(\|T^*\xi\|+\|T\|\|(I-E)\xi\|\big)\) supplies a uniform lower bound for \(T^*\), hence \(T\) is onto.
For empty arc sets the complementary estimate applies on the corresponding blocks.
Thus \(\operatorname{ran} A=\operatorname{ran}D\) is dense.
It is closed exactly when every \(D_i\) is invertible on its circle, equivalent to the circle rank test for \(F_i\) since \(F_i'\) has a right inverse.
Polar decomposition gives the kernel dimension \(m-r\).

## The original conjugation defect and signed shell arrays

There are constants \(0<c_0\le C_0\) with
\[
                 c_0 DD^*\le AA^*\le C_0 DD^* .
\]
In each block the boundedly invertible left and right matrices in the Laurent Smith reduction compare the ordered singular values of \(D_i\) with those of its invariant-factor diagonal uniformly on the circle.
At a zero of multiplicity \(k\) the squared absolute value of a factor is comparable to the angular distance to the power \(2k\).
There are finitely many such zeros, and one attains the largest multiplicity \(d\).
Circle integration for \(DD^*\), trace comparison under the displayed order and equality of the positive trace spectra of the two rectangular Grams give the exponent \(\alpha=1/(2d)\). [C81, spectral comparison](Yin_C_A0081_v1.md#estimating-the-original-shell-sums)
The original spectral trace thus satisfies C76's dyadic heat bound by integrating its positive spectral measure.
Since \(\ker A=\ker T\), the projection \(p=I-T^*(TT^*)^{-1}T\) has exponentially small coefficient square tails, from the finite geometric inverse sums for \(TT^*\) with propagation growing linearly. [C58](Yin_C_A0058_v1.md#bounded-rational-inverses-have-exponential-tails)

For clarity, \(K_j=(1-z_j)\sum_{l=0}^{N_j} z_j^l Q^l\) in (2) still uses \(A\).
If \(R_z=(1-z)(I-zQ)^{-1}\), then \(\|K_j-R_{z_j}\|_2\le\sqrt m z_j^{N_j+1}\), and C76's positive-mass estimate gives \(\|R_{z_j}-p\|_2=O((1-z_j)^{\alpha/2})\). [C76, finite-shell transfer](Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell)
On \(S_j^+\) the projection coefficients and those of its four conjugates have unweighted norm \(O(e^{-c2^j})\).
Indeed the inner radius for their original coefficients is at least \(2^j-b(k_j+1)\), with \(b\) fixed and \(k_j=O(j)\) as in C80.
The norm of \(I-\mathsf P\) is at most two on the full coefficient space.
These facts give (2), since C76's prescribed truncation makes \(z_j^{N_j+1}=O(2^{-\kappa\alpha j/2})\).
In particular this bound controls the endpoint sum with the original commutator insertions \(Q^l-(g^*Qg)^l\) after actual products at the same endpoint have been added.
The kernel estimate used to prove (2) comes from the cyclic packet argument above.
Multiplying the squared bound by \(2^{\beta j}\) and summing for \(j\ge J\), then applying [C80, equation (2)](Yin_C_A0080_v1.md#signed-estimates-on-widened-shells) at the stated widening constant, proves (3).

## A whole-group row Gram without a common cyclic block

In an individual good four-line group choose a malnormal free subgroup with basis \(u,v\), using [Kapovich, Theorem 7.7, arXiv v1](../literature/pdf/Kap99--arxiv-v1.pdf#page=29).
Here the ambient group is non-elementary torsion-free word-hyperbolic. [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace)
We accept the stated existence theorem at these hypotheses after checking its statement in the preprint.
The cyclic subgroups of these basis elements are maximal in \(G\): a root of either commutes with it, hence lies in the free subgroup by malnormality and then lies in its cyclic centralizer there.
If nonzero powers of the two elements were conjugate in \(G\), malnormality would put the conjugator in the free subgroup, contradicting their independent abelianizations there.
Thus their maximal cyclic groups are not conjugate.

Let \(P\) be the uniform probability on the identity and a finite symmetric generating set of \(G\), and set \(U=1-u\), \(V=1-v\), \(W=32I+\epsilon P\) with \(0<\epsilon\le1\).
Take
\[
 A=\operatorname{diag}(U,V)
       \begin{pmatrix} U&0&W\\0&V&I\end{pmatrix}.                    \tag{5}
\]
The first two columns realize (1) in their respective row blocks.
After the displayed left factors have been removed, the first row's collected Laurent coefficients have no common nonunit divisor: any such divisor must divide \(1-u\), but the identity coset coefficient of \(W\) evaluated at \(u=1\) is positive.
The second row already has an identity coefficient from its third column.
Hence the displayed factors give precisely the basis choice in the theorem.
Both selected normalized pivots still vanish at phase one, and the shared third column alone has rank at most one.
The near-zero packets of the two different directions are therefore relevant even after this normalization.
The angular estimate makes the inner two-row factor onto and yields nonclosed range for \(A\), \(\dim_G\ker A=1\), and \(\alpha=1/2\) in (2)–(3).

The first diagonal entry of the original \(AA^*\) is
\[
              B=U(UU^*+W^2)U^* .
\]
Its coefficient at \(u\) is nonzero: that coefficient in \(32^2 UU^*\) equals \(-32^2\), whereas \(\|B-32^2 UU^*\|\le4(4+64+1)\).
Its identity coefficient is positive as well.
If \(B\) belonged to the von Neumann algebra of a subgroup \(H\), the support would put \(u\) in \(H\).
The cyclic shift gives an inverse of \(U\) affiliated with \(\mathcal N(H)\).
Removing the two exterior factors and subtracting \(UU^*\) therefore puts the bounded \(W^2\) in \(\mathcal N(H)\).
The positive square root gives \(W\), so the entire generating support of \(P\) lies in \(H\).
Thus \(H=G\), including when the subgroup test is made after left and right translations of this entry: its nonzero identity coefficient first changes the test to one on a conjugate subgroup.
The original group is not free, since its binary group ring has a [nonzero zero product](Yin_C_A0051_v1.md#statement).
In particular the row Gram does not meet C82's free-subgroup support hypothesis.

More strongly, over every cyclic subgroup \(K\), no finite group-ring right combinations of the original columns can give a full-rank square matrix supported in \(K\), even allowing independent group elements multiplying rows on the left and columns on the right.
Every original entry in row one has the left factor \(1-u\), and every entry in row two has the left factor \(1-v\).
For the corresponding \(t=u,v\), the coefficient sum of \((1-t)Y\) on every right coset of \(\langle t\rangle\) is zero for every finite \(Y\).
All right combinations preserve this property.
If a row translated on the left by \(g_i\) has its entries in \(K\) after right column translations, each allowed support before translation is contained in some \(g_i^{-1}K h_j^{-1}\).
Each such set meets any given right coset of \(\langle t\rangle\) at most once unless \(g_i^{-1}K g_i\cap\langle t\rangle\ne\{e\}\), by taking left differences.
A nonzero row requires this exception.
It cannot occur for both rows, since a cyclic group meeting a conjugate of each in a nonidentity element would conjugate nonzero powers of \(u\) and \(v\).
Thus at least one whole row vanishes in any proposed common cyclic square matrix.
This obstruction concerns group-ring right combinations and row and column group translations, with no claim about arbitrary left matrix operations.

Finally take any transcendental real \(\epsilon\in(0,1)\).
For any fixed finite candidate support in each of the three input coordinates, the equations for a kernel vector give a finite complex linear system whose entries are polynomials in \(\epsilon\) with rational coefficients.
Only finitely many output endpoints can occur.
At \(\epsilon=0\), injectivity of the two exterior factors and elimination of the third coordinate give \((1-u)x=32(1-v)y\).
The left side minus the right side is the divergence of a finite flow on copies of the free \(u,v\) tree, which cannot vanish for a nonzero finite flow by a leaf argument. [C64](Yin_C_A0064_v1.md#the-row-map-and-its-kernel)
The third coordinate then vanishes too.
For every nonempty choice of supports, the finite system thus has a full-column minor nonzero at zero, which cannot vanish at the chosen transcendental coefficient.
This excludes all nonzero finitely supported null vectors on \(G\).
The actual dimension-one kernel projection consequently has infinite group support, since any nonzero column supported on finitely many group elements would give such a vector.
It also fails the finite-support conclusion of every [finite-power Perron test](Yin_C_A0069_v1.md#statement).

## Assessment history

### Decision separated-cyclic-packets

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:37 |
| status | proved |
| reason | Independent review verifies the packet estimate and the consequences for the original matrix. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinct cyclic directions for row blocks, the original signed exterior and the example without a common cyclic minor. |
| argument | [Proof](#argument) | Laurent column reconstruction, packet compression, spectral comparison, shell transfer and the whole-group example. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0123_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-separated-cyclic-packets)
