---
author: Yin
---
# Odd-characteristic transfer for a single reflection in generalized dihedral groups

## Scope

This exploration groups a family of actual product tables with exactly one larger fiber and shows that they cannot provide an odd-characteristic exact-support solution without a complex exact-support solution.
It concerns coefficient arithmetic within the [complex-coefficient Kaplansky task](../tasks/Yin_T_A0002_v1.md); the ambient groups below contain an involution and are not torsion-free counterexamples.
The signed-lattice mechanism extends the [character condition in C25](../claims/Yin_C_A0025_v1.md) and the [branch treatment in C26](../claims/Yin_C_A0026_v1.md).
The arguments are given in full and have not received independent review.

## Nonvanishing can be preserved when lifting signed binomial equations

Let \(M=\mathbb Z^m\), let \(d_1,\ldots,d_q\in M\), and let \(F\in\mathbb Z[M]\) be a Laurent polynomial.
Suppose a character \(z:M\to K^\times\), over a field of odd characteristic, satisfies
\[
 z(d_j)=-1\quad(1\le j\le q),\qquad F(z)\ne0.
\]
Then there exists a character \(w:M\to\mathbb C^\times\) satisfying the same signed binomial equations and \(F(w)\ne0\).

To prove this, put \(L=\langle d_1,\ldots,d_q\rangle_{\mathbb Z}\).
Every integer relation \(\sum_j n_jd_j=0\) gives
\[
 1=\prod_j z(d_j)^{n_j}=(-1)^{\sum_jn_j}.
\]
Odd characteristic implies that \(\sum_jn_j\) is even.
Thus \(\chi(\sum_jn_jd_j)=(-1)^{\sum_jn_j}\) defines a character \(L\to\{1,-1\}\).
Set
\[
 R=\mathbb Z[M]/(X^\ell-\chi(\ell):\ell\in L).
\]
The listed equations for the \(d_j\) generate this same ideal, by multiplication and inversion of Laurent monomials.
Choose one representative \(r_c\) for each coset \(c\in M/L\).
In \(R\), every monomial \(X^{r_c+\ell}\) equals \(\chi(\ell)X^{r_c}\).
These reductions identify \(R\), as an abelian group, with the free group on the symbols \(X^{r_c}\): multiplying two such symbols uses the sign determined by the difference between their representative sum and the representative of the sum coset.
The character law for \(\chi\) makes this multiplication associative and gives an inverse to the quotient map.
In particular \(R\to R\otimes_{\mathbb Z}\mathbb C\) is injective.

Smith normal form extends \(\chi\) to a complex character on \(M\).
Rescaling Laurent monomials by that extension identifies
\[
 R\otimes_{\mathbb Z}\mathbb C\cong\mathbb C[M/L].
\]
Since \(M/L\) is finitely generated abelian, its free part gives Laurent variables and its finite part gives a finite direct product of copies of \(\mathbb C\).
Thus this complex algebra is a finite product of Laurent polynomial algebras.
A nonzero element of such an algebra has nonzero evaluation at some complex torus point.
If \(F\) vanished at every complex solution of the signed equations, its image in this algebra would therefore be zero.
Injectivity would give \(F=0\) in \(R\), and evaluation at the original \(K\)-point would give \(F(z)=0\), a contradiction.

This argument preserves a nonvanishing condition, not an additional vanishing condition.
In particular it does not assert that adding \(F=0\) to a signed binomial system permits odd-characteristic transfer.

## A whole family with one larger fiber admits odd-characteristic transfer

Let \(H\) be an abelian group and
\[
 G=H\rtimes\langle s\rangle,\qquad s^2=1,\qquad shs=h^{-1}\quad(h\in H).
\]
Let \(D\subset H\) be finite with \(|D|\ge2\), and assume that each nonidentity element has either zero or exactly two representations \(de^{-1}\) with \(d,e\in D\).
Take
\[
 A=D\cup\{s\},\qquad B=D^{-1}\cup\{s\}.
\]
The identity fiber has size \(|D|+1\), every represented nonidentity element of \(H\) has a two-term fiber, and every represented reflection \(ds\), \(d\in D\), has precisely the two representations
\[
 d\cdot s=s\cdot d^{-1}.
\]
These are all the fibers.

For these fixed supports, an exact-support solution over any field of odd characteristic implies an exact-support solution over \(\mathbb C\).
The complex coefficients need not lift the originally chosen coefficients.

Write a coefficient assignment as
\[
 \alpha=\sum_{d\in D}u_d\,d+v s,\qquad
 \beta=\sum_{d\in D}w_d\,d^{-1}+t s,
\]
with every coefficient nonzero.
The reflection equations are
\[
 u_dt+vw_d=0.
\]
Hence, with \(\lambda=-t/v\ne0\), they are equivalent to
\[
 w_d=\lambda u_d,\qquad t=-\lambda v.
\]
The other equations become
\[
 \sum_{de^{-1}=g}u_du_e=0\quad(g\in DD^{-1}\setminus\{1\}),
 \qquad
 v^2=Q(u):=\sum_{d\in D}u_d^2.                              \tag{1}
\]
Each equation indexed by \(g\ne1\) is a signed binomial after division by one of its nonzero monomials.
An odd-characteristic exact-support solution of (1) has \(Q(u)=v^2\ne0\).
Apply the preceding lemma to these signed binomials and \(F=Q\).
It gives nonzero complex values \(u_d\) satisfying all the nonidentity equations and \(Q(u)\ne0\).
Choose a nonzero complex square root \(v\) of \(Q(u)\), choose any \(\lambda\in\mathbb C^\times\), and reconstruct \(w_d,t\) by the displayed formulas.
This gives an exact-support complex solution of every coefficient equation.

The proof covers arbitrary finite \(D\) satisfying the representation-count hypothesis; it does not depend on a bounded enumeration of small groups.
It excludes this family as a source of the proposed odd-characteristic versus complex arithmetic diagnostic.
It does not exclude such a diagnostic for product tables with several reflection terms in each support, more than one larger fiber, or other ambient groups.

## The order-fourteen example and the distinction between fixed coefficients and supports

Let
\[
 G=\langle r,s:r^7=s^2=1,\ srs=r^{-1}\rangle,
 \qquad D=\{1,r,r^2,r^4\}.
\]
Every nonidentity element of \(\langle r\rangle\) has exactly two representations in \(DD^{-1}\).
For exponents \(1,2,3\), the respective ordered pairs of exponents are
\[
 (1,0),(2,1);\qquad
 (2,0),(4,2);\qquad
 (0,4),(4,1),
\]
and reversing the pairs gives exponents \(6,5,4\), respectively.
Thus \(A=D\cup\{s\}\), \(B=D^{-1}\cup\{s\}\) have one five-term fiber and ten two-term fibers.

Put
\[
 P=1-r-r^2-r^4,\qquad P^\vee=1-r^{-1}-r^{-2}-r^{-4}.
\]
The two terms of each nonidentity coefficient of \(PP^\vee\) have opposite signs, while its identity coefficient is \(4\).
Also \(Ps=sP^\vee\).
Consequently, for every scalar \(c\),
\[
 (P+c s)(P^\vee-c s)=4-c^2.                                 \tag{2}
\]
For \(c=1\), this gives an integral identity with right-hand side \(3\), and hence an exact-support zero product over \(\mathbb F_3\).
The same displayed integer coefficients do not give a complex zero product.
For \(c=2\), however, (2) gives a complex zero product with exactly the same supports.
Indeed, in characteristic \(3\) the choice \(c=-2\) reduces to \(c=1\), so a characteristic-zero solution even specializes to the displayed \(\mathbb F_3\)-point after allowing the reflection coefficients to change as integers.
Thus failure of the particular integer expression at \(c=1\) is neither failure of exact-support transfer nor failure of lifting that residue point.

The reflection coefficient supplies a genuine free parameter here.
More explicitly, the nonidentity equations after the reflection reduction force
\[
 (u_1,u_r,u_{r^2},u_{r^4})=(u,-u,-u,-u),
\]
because three of them are
\[
 u_r(u_1+u_{r^2})=0,\qquad
 u_{r^2}(u_1+u_{r^4})=0,\qquad
 u_{r^4}(u_1+u_r)=0.
\]
The remaining equation is \(v^2=4u^2\), which has the nonzero solutions \(v=\pm2u\) in every field of odd characteristic.
This exact calculation is the useful calibration from the bounded search.
It prevents the identity \(3\) from being mistaken for a table whose entire complex exact-support solution set is empty.
