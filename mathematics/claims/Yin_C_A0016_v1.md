---
author: Yin
---
# Fourier support of individual induction defects and a coprime cyclic restriction test

## Statement

Let \(G\) be discrete, let \(K\subseteq\mathbb C\) be a conjugation-closed subfield, and use the regular representation, \(N=\mathcal N(G)\), \(U=\mathcal U(G)\), the actual scalar division closure \(D=D(K[G],U)\), and the canonical trace \(\tau\).
Use right modules, matrices acting from the left and unnormalized matrix traces.
For a finitely generated \(D\)-module \(X\), denote by \(h_X\) the bounded positive central element determined by
\[
 \tau(qh_X)=\dim_U((X\otimes_D U)q)
 \qquad(q\in Z(N)\text{ a projection}).
\]
These cuts are additive on orthogonal central projections and are bounded by \(n\tau(q)\) for a quotient of \(D^n\), giving their bounded density on the center.
For a finite matrix \(A\) over \(K[G]\), write \(h_A=h_{\operatorname{coker}A_D}\).
It is the matrix center-valued trace of the projection onto \(\ker A^*\).

1. For every homomorphism \(\phi:G\to\mathbb Z\), the Fourier support of \(h_X\) is contained in \(\ker\phi\).
   The same holds for the positive center-valued defect of each finitely generated short exact sequence after induction from \(D\) to \(U\).
2. For an element \(g\) of finite conjugacy class, suppose \(g\in H\le C_G(g)\), with \(H\) of finite index in \(G\), and some homomorphism \(H\to\mathbb Z\) is nonzero on \(g\).
   Then the coefficient at \(g\) of every \(h_X\) and every individual defect in item 1 vanishes.
3. Suppose the orders of finite subgroups have finite least common multiple, \(\phi:G\twoheadrightarrow\mathbb Z\), and \(H_m=\ker(\phi\bmod m)\).
   Write \(A_m\) for the finite \(K[H_m]\)-matrix obtained by restricting free right modules in the coordinates of the left cosets \(tH_m\), and \(h_{A_m}^{H_m}\) for its cokernel dimension in the regular representation of \(H_m\).
   Then \(T_G(h_{A_m}^{H_m})=m h_A\), where \(\mathcal N(H_m)\) is embedded in \(N\) and \(T_G\) is the center-valued trace of \(G\).
   If \(h_{A_m}^{H_m}\in L_K(H_m)\) and \(h_{A_n}^{H_n}\in L_K(H_n)\) for two coprime positive indices \(m,n>1\), then \(h_A\in L_K(G)\).
   In fact the original class witness restricts to an actual witness over each \(D_{H_m}=D(K[H_m],\mathcal U(H_m))\), and its signed defect \(S_m\) satisfies \(T_G(S_m)=mS\).

These assertions do not posit a map \(G_0(D)\to Z(N)\) induced by dimension.
They give restrictions on the terms of a single class relation and a sufficient arithmetic certificate for its total defect.

## A fixed cokernel relation

Fix a signed finite-subgroup expression for the class of \(C=\operatorname{coker}A_D\) as in [KLS17 Theorem 3.7(3)](../audits/literature/KLS17/Yin_U001.md#why-condition-3-has-not-been-cleared).
Let \(b\in L_K(G)\) be the corresponding signed sum of center-valued dimensions of finite-subgroup projectives after induction to \(U\).
For a short exact sequence \(0\to X'\xrightarrow{i} X\to X''\to0\) its positive defect \(e_i\) is determined by the cuts of \(\ker(i\otimes_D U)\).
The [cut calculation](Yin_C_A0015_v1.md#applying-an-exact-sequence-class-relation) gives \(e_i=h_{X'}+h_{X''}-h_X\), regardless of exactness after tensoring.
If the signed sequence relations are taken in the orientation \([X]-[X']-[X'']\), every witness for the fixed expression satisfies
\[
 S=\sum_i m_i e_i=b-h_A.
\]
Changing the witness with fixed endpoints leaves \(S\) unchanged even before reduction modulo the lattice.
Changing the finite-subgroup expression changes \(S\) by an element of \(L_K(G)\).
Thus the search for a different expression only helps if one can certify an additional property of its actual defects.

## Character twists and central cuts

Write \(\alpha_w(\lambda(g))=w^{\phi(g)}\lambda(g)\) for \(w\in\mathbb T\).
The diagonal unitary \(\delta_x\mapsto w^{\phi(x)}\delta_x\) implements a trace-preserving automorphism of \(N\) and hence of \(U\).
It also gives \(\|\alpha_w(h)-\alpha_v(h)\|_2\to0\) as \(w\to v\) for every bounded \(h\in N\), by dominated convergence on the squared Fourier coefficients.

Take a finite rectangular matrix \(B\) over \(D\), its final support \(p\) in a matrix ring over \(N\), and \(r=T_{G,\mathrm{mat}}(p)\).
Each entry of \(B\) has a finite expression in \(K[G]\) using sums, products and inverses of actual affiliated units.
Indeed the union of the finite scalar-inversion stages is already division closed.
Twisting the entire expression gives \(B(w)=\alpha_w(B)\) for every \(w\).
Its starting matrices are bounded-coefficient Laurent polynomials and every inverse in the expression exists at every \(w\).
For each nonzero central projection \(q\), compute in \(qN\) with faithful restricted trace and unit \(q\).
Compression preserves every indicated inverse since \(q\) is central.
The [one-variable generic rank theorem for actual rational expressions](Yin_C_A0012_v2.md#rational-expressions-with-actual-defined-inverse-gates) makes the scalar rank of \(qB(w)\) constant off a countable subset of the circle.
This uses complex coefficients in the analytic corner even if the starting field \(K\) is smaller.
It requires no action of the twists on the ring \(D\) itself.

By equivariance of the final support and the center-valued trace this scalar rank is \(\tau(q\,\alpha_w(r))\).
This function is continuous by the preceding \(L^2\) estimate, hence it is constant everywhere and equals \(\tau(qr)\).
This argument is applied separately for each \(q\), so it requires no common exceptional set over all central projections.
Testing all \(q\) gives \(\alpha_w(r)=r\) for every \(w\).

Now write \(X=D^n/J\), allowing an infinitely generated relation module \(J\).
For a finite subset \(Y\subset J\), form the matrix \(B_Y\) with those columns and put \(r_Y=T_{G,n}(p_{\operatorname{im}B_Y})\), using its final support.
The \(r_Y\) increase with \(Y\) and are fixed by the twists just considered.
Right exactness gives \(X\otimes_D U=U^n/JU\), where \(JU\) is the directed union of the images \(B_Y U^{|Y|}\).
Scalar dimension is additive and cofinal after every central cut, and the trace is normal.
Consequently \(h_X=n1-\sup_Y r_Y\) in the bounded center.
Normality of \(\alpha_w\) gives \(\alpha_w(h_X)=h_X\).
Comparing the coefficient at \(g\) proves its vanishing whenever \(\phi(g)\ne0\).
The formula for \(e_i\) proves the assertion term by term, even when the class witness uses modules without finite presentations.

## Finite-index detection and coprime restrictions

For \(x\in N\) use \(\widehat x(g)=\tau(x\lambda(g)^*)\).
On a finite conjugacy class the Fourier coefficient of \(T_G(x)\) is the arithmetic mean of the coefficients of \(x\) on that class.
This follows by pairing with its central class sum in the trace, using \(\tau\circ T_G=\tau\).
On every infinite conjugacy class central \(\ell^2\)-coefficients vanish.
These facts apply to the sum of diagonal entries of a matrix projection.

Let \(H\le G\) have index \(d\), and decompose the Hilbert space in the coordinates \(tH\) for a left transversal.
The restricted cokernel projection is the same Hilbert projection \(p_A\) in these coordinates since adjoints and kernels are preserved by this unitary decomposition.
Writing \(x=\sum_j(p_A)_{jj}\) and \(E_H:N\to\mathcal N(H)\) for Fourier truncation, its untraced diagonal sum is
\[
 y=\sum_{tH} E_H(\lambda(t)^*x\lambda(t)).
\]
For \(g\in H\le C_G(g)\), the coefficient at \(g\) of \(T_H(y)\) is that of \(y\), since \(g\) is central in \(H\).
As \(tH\) varies, each element of the \(G\)-conjugacy class of \(g\) appears \([C_G(g):H]\) times in \(tgt^{-1}\).
Thus \(\widehat{T_H(y)}(g)=d\,\widehat h_A(g)\).
Applying the character calculation in \(H\) to the finite restricted matrix therefore gives \(\widehat h_A(g)=0\).
The same diagonal formula applies to the final support of each \(B_Y\) in the preceding proof.
In coset coordinates the expression for \(B_Y\) is a finite matrix rational expression over \(K[H]\).
All its inverse gates remain units at the original point because restriction represents the original affiliated inverse and its two product identities in \(M_d(\mathcal U(H))\).
Equivalently, the Hilbert-space identification embeds \(\mathcal N(G)\) in \(M_d(\mathcal N(H))\) and carries the polar decomposition and spectral projections of affiliated operators into this matrix algebra.
Twisting those restricted group coefficients inside \(H\) preserves the inverse identities at every circle point.
The central-cut generic rank argument applies to this matrix expression as written, including its matrix inverse gates.
This proves \(\widehat r_Y(g)=0\) without identifying either subgroup closure with a matrix-entry ring.
A bounded increasing net of central positive elements \(r_Y\) converges in \(L^2\) to its supremum \(r\), since \(\tau((r-r_Y)^2)\le n\tau(r-r_Y)\to0\).
Thus the coefficient vanishes also for \(h_X\) and \(e_i\), proving item 2.
For example, in the Klein bottle group \(\langle x,y\mid xyx^{-1}=y^{-1}\rangle=\mathbb Z\rtimes\mathbb Z\), every integer character kills \(y\).
The index-two abelian subgroup \(\langle x^2,y\rangle\) has a character sending \(y\) to one, so item 2 kills the coefficient at every \(y^k\), \(k\ne0\), for each actual defect.

For normal \(H\), \(E_H\) commutes with conjugation by \(G\).
Class averaging gives \(T_GE_H=E_HT_G\) on \(N\), and \(T_GT_H=T_G\) on \(\mathcal N(H)\).
For the latter equality, each finite \(G\)-class in \(H\) is partitioned into finite \(H\)-classes, and averaging each part preserves its sum.
It follows from the diagonal formula that
\[
 T_G(h_{A|H}^{H})=d\,E_H(h_A),
 \qquad T_G\bigl(L_K(H)\bigr)\subseteq L_K(G).
\]
The inclusion follows on each generator by applying \(T_GT_H=T_G\) to a projection over a finite subgroup of \(H\).
For \(H=H_m\), item 1 gives \(E_H(h_A)=h_A\).
Thus independently certifying the two restricted matrix dimensions gives \(m h_A,n h_A\in L_K(G)\).
An integral Bezout combination gives \(h_A\in L_K(G)\), and hence \(S=b-h_A\in L_K(G)\).

### Restricting the same short exact sequences

Fix \(H=H_m\) and put \(d=m\), \(D_H=D(K[H],U_H)\) and \(U_H=\mathcal U(H)\).
First, \(D_H\) is closed under adjoints by construction and \(M_j(D_H)\) contains the inverse of each of its elements that is a unit in \(M_j(U_H)\).
For the matrix statement use induction on \(j\), starting with scalar division closure.
Given an invertible \(V\), put \(P=V^*V\).
The first column \(v\) of \(V\) admits no nonzero right annihilator, and \(v^*v\) has the same right kernel as \(v\) by the affiliated polar decomposition.
Hence \(P_{11}=v^*v\) has full support, is a unit of \(U_H\), and has inverse in \(D_H\).
With this pivot, block elimination over \(D_H\) reduces \(P\) to two diagonal blocks, \(P_{11}\) and an ambient-invertible Schur complement of size \(j-1\).
The induction hypothesis gives the inverse of the latter over \(D_H\), and \(V^{-1}=P^{-1}V^*\) follows over \(D_H\).

In the coset representation \(U(G)\hookrightarrow M_d(U_H)\), the entries of every element of \(K[G]\) belong to \(K[H]\).
By the preceding inverse argument the preimage of \(M_d(D_H)\) is division closed, so every element of \(D\) has matrix entries in \(D_H\).
The natural embedding \(U_H\hookrightarrow U(G)\) preserves inverses, and thus \(D_H\subseteq D\).
Choosing the identity representative for \(H\), the column over that coset of any \(u\in U(G)\) has entries \(u_t\in U_H\).
The operator \(\sum_{tH}\lambda(t)u_t\) has the same column, interpreted as an equality of affiliated products.
Their difference annihilates the full first coset projection in \(M_d(U_H)\) and therefore has kernel containing \(\ell^2(H)\).
Its kernel projection lies in \(\mathcal N(G)\), so all right translates of this subspace are also in the kernel and exhaust \(\ell^2(G)\).
Reading the same column gives uniqueness of the expansion.
For \(u\in D\) the entries \(u_t\) lie in \(D_H\), and conversely the finite sums with such entries lie in \(D\).
This proves the right-module decompositions \(U(G)=\bigoplus_{tH}\lambda(t)U_H\) and \(D=\bigoplus_{tH}\lambda(t)D_H\).
Multiplication is therefore an isomorphism \(D\otimes_{D_H}U_H\cong U(G)\) of \((D,U_H)\)-bimodules.

Restriction from \(D\) to \(D_H\) is exact and preserves finite generation by the displayed decomposition.
For every right \(D\)-module \(X\), associativity identifies \((\operatorname{Res}X)\otimes_{D_H}U_H\) with \(\operatorname{Res}(X\otimes_D U(G))\), naturally for each map in the witness.
In particular the defects themselves restrict as modules.
Every finite subgroup \(F\le G\) is contained in \(H\), and \(H\) is normal.
In coset coordinates a projector over \(K[F]\) restricts to the direct sum of the conjugate projectors over \(K[t^{-1}Ft]\subseteq K[H]\).
This follows by applying the projector to each summand \(\lambda(t)D_H\), with the same computation entrywise for a matrix projector.
Restriction thus gives a genuine short-exact-sequence witness for the restricted cokernel with signed finite-subgroup endpoint \(b_m\in L_K(H)\).
It requires no surjectivity hypothesis on the whole of \(G_0(D_H)\).
For these finite-subgroup projectors the diagonal formula gives \(T_G(b_m)=m b\), since all conjugates of their finite-order support lie in \(H\).
Combining this with the formula for \(h_{A_m}^{H}\) gives the exact transfer of signed defects,
\[
 T_G(S_m)=T_G(b_m-h_{A_m}^{H})=m(b-h_A)=m S.
\]
In particular \(S=T_G(S_3)-T_G(S_2)\) for the index-three and index-two covers.
Dimension-flatness of \(U_H\) over \(D_H\) or of \(U(G)\) over \(D\) enters none of these comparisons.

## Arithmetic left undetected

If every infinite-order element of \(\Delta(G)\) satisfies the finite-index character condition of item 2, then \(S\) is supported on \(\Delta^+(G)\).
In the torsion-free case this makes \(S\) a scalar even when \(N\) has nontrivial center.
Membership in a finite-dimensional central subspace by itself gives no divisibility information on the coordinates in the finite-subgroup trace lattice.

For a torsion-free ICC group, \(L_{\mathbb C}(G)=\mathbb Z1\) and the center of \(N\) consists of scalars.
Writing \(b=k1\), the defect is \((k-\dim_U\operatorname{coker}A_U)1\).
Every nonidentity Fourier test already vanishes in this setting, even before a class witness is supplied.
A one-sided bound or conjugation invariance of a term does not discretize its scalar trace.
For instance, in \(\mathcal N(F_2)\) the spectral projection of a free generator on a circle arc of Haar measure \(1/3\) has center-valued trace \((1/3)1\), since its nonzero powers have regular trace zero.
This is an ambient projection example only.
No identification with the kernel of a group-ring matrix or with a defect from \(D\) is supplied by its trace or its right translation invariance.

Two examples locate the limits of the tests.
In the integer Heisenberg group the infinite-order central commutator \(c=[u,v]\) is killed by every integer character on every finite-index subgroup containing \(c\).
Indeed such a subgroup contains \(u^r,v^r\) for some \(r>0\), and \([u^r,v^r]=c^{r^2}\).
This shows the precise reach of virtual character detection even in an amenable example covered by other arguments.

For an arbitrary torsion-free ICC group \(J\) and a matrix \(B\) over \(\mathbb C[J]\), put \(G=J\times\mathbb Z\) and take \(A=B\) in degree zero.
Then \(h_A=(\dim_{\mathcal U(J)}\operatorname{coker}B_{\mathcal U(J)})1\) by the tensor decomposition of the regular representation.
Restriction to \(J\times m\mathbb Z\) gives \(m\) diagonal copies of \(B\), so the two cover computations merely return the two multiples of that same scalar.
The example transfers no \(G_0\)-surjectivity assumption between the groups.
It explains why a cyclic quotient alone gives no independent certification of the two smaller matrix dimensions.
The unrestricted KLS17 implication still needs arithmetic information from (3) or another regular-representation argument beyond Fourier support.
