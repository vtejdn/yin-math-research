---
author: Yin
---
# Reduced norms and an adjoint determinant for three-term zero products

## Statement

Let \(H=\ker(d:\Gamma\to C_3)\) in Gardam's group, and let \(u,v\in H\) be such that \(1,u,v\) are pairwise distinct.
Use the faithful lift \(\rho:H\to D^\times\) in [C108](Yin_C_A0108_v1.md#statement), where \(D\) is the cyclic division algebra with \(Xc=c^2X\) for \(c\in E=\mathbb F_8\), \(s=X^3\), and center \(K=\mathbb F_2(s)\).
Set \(U=\rho(u)\), \(V=\rho(v)\), and
\[
 F(h)=\operatorname{Nrd}_{D/K}(\rho(h)-1),\qquad
 Z=(U-1)^{-1}(V-1).
\]
Let \(D_0\) be the kernel of the reduced trace in \(D\), and let \(\operatorname{Ad}(W)\) mean conjugation \(x\mapsto WxW^{-1}\) on \(D_0\).
Form the homogeneous determinant over \(K\)
\[
 P_{u,v}(x,y)=
 \det_{D_0}\!\big[x(\operatorname{Ad}(U)-I)+y(\operatorname{Ad}(V)-I)\big].
 \tag{1}
\]

Over any field of characteristic zero or two, if a scalar supported exactly on \(\{1,u,v\}\) has a nonzero finitely supported right annihilator in the group algebra of \(\Gamma\), then all three of the following conditions hold.

1. The reduced characteristic polynomial of \(Z\) is either \(t^3+t+1\) or \(t^3+t^2+1\).
2. \(F(u)=F(v)=F(u^{-1}v)\).
3. \(P_{u,v}\) is identically zero.

The same necessary conditions hold for a finitely supported left annihilator.
The support may lie entirely in \(\ker(d,\psi)\), where \(\psi:\Gamma\to C_7\) is as in C108.
No separation by \(\psi\) is required.
The assertions concern the algebraic zero-divisor problem [A0002](../tasks/Yin_T_A0002_v1.md#contract).
They give no conclusion here about general \(\ell^2\) kernels.

For any fixed nonidentity \(u,v\in H\), among the indices \(j\ge0\) with \(1,u,v^{2^j}\) pairwise distinct, at most one can pass condition 2 for that triple.
This applies in particular to noncommuting elements of \(\ker(d,\psi)\).

<a id="argument"></a>
## The splitting matrices and the norm at infinity

View \(D\) as a right \(E(s)\)-space with basis \(1,X,X^2\), and represent its elements by left multiplication.
Write \(M(W)\) for this matrix.
Explicitly,
\[
 M(c)=\operatorname{diag}(c,c^4,c^2)\quad(c\in E),\qquad
 M(X)=\begin{pmatrix}0&0&s\\1&0&0\\0&1&0\end{pmatrix}.
 \tag{2}
\]
These matrices give the splitting \(D\otimes_K E(s)\cong M_3(E(s))\).
Indeed the matrices of \(1,\theta,\theta^2\), where \(\theta^3+\theta+1=0\), span the diagonal over \(E(s)\) by the Vandermonde determinant on the three distinct conjugates of \(\theta\).
Their products with \(M(X)\) and \(M(X)^2\) span the other two cyclic diagonals.
Both algebras have dimension nine over \(E(s)\).
The coefficient Frobenius on \(E(s)/K\) acts on \(M(W)\) by conjugation by \(M(X)\), as (2) verifies on the generators.
Hence the determinant, trace and characteristic polynomial of \(M(W)\) lie in \(K\).
They are respectively the reduced norm, reduced trace and reduced characteristic polynomial.

For every positive letter \(p\), (2) gives \(\det M(X+c_p)=s+c_p^7=s+1\).
The lift of a word of total exponent \(e\) in C108 divides its product by \((1+s)^{e/3}\).
Taking determinants proves \(\det M(\rho(h))=1\) for every \(h\in H\).
Consequently \(F(h)=\operatorname{tr}M(\rho(h))+\operatorname{tr}M(\rho(h)^{-1})\), by expanding the cubic characteristic polynomial at 1 in characteristic two.

For nonidentity \(h\in H\), \(F(h)\) is nonzero and nonconstant.
Indeed \(\rho(h)-1\ne0\) in the division algebra.
Put \(T=X^{-1}\), \(z=T^3=s^{-1}\), and use the skew Laurent series of [C108](Yin_C_A0108_v1.md#explicit-separating-quotients).
Every \(X+c_p\) has leading term \(X\), and its inverse has leading term \(X^{-1}\).
The normalized lift therefore has leading term \(1\), even for words of negative signed exponent.
Thus \(\rho(h)-1=T^m W\) with \(m>0\) and \(W\) a unit of the skew power series ring.
That ring is a free right \(E[[z]]\)-module with basis \(1,T,T^2\), by grouping exponents modulo three.
Left multiplication by \(W\) is invertible over \(E[[z]]\), while left multiplication by \(T\) has determinant \(z\) on this basis.
After extension to \(E((z))\) this determinant representation is the one in (2) expressed in the new basis.
Therefore \(\operatorname{ord}_{z=0}F(h)=m>0\), proving the assertion.

## Finite annihilators and reduction of coefficients

An annihilator in the ambient group algebra has a nonzero component inside \(k[H]\) after translation.
For a right annihilator split its support along \(Ht\) and multiply a nonzero component on the right by \(t^{-1}\).
For a left annihilator use \(tH\) and translate on the left.
The group \(H\) is torsion-free.
It is residually \(2\) by C108, so the odd part of any finite-order element is trivial.
An element \(W\in D^\times\) of \(2\)-power order equals 1, since \((W-1)^{2^n}=W^{2^n}-1\) and \(D\) is a division ring.
Apply this to the faithful lift.

In characteristic zero we use [C101](Yin_C_A0101_v1.md#statement) on the torsion-free group \(H\).
For a three-term admissible row its two normalized coefficients are algebraic units, and at each place over 2 the row has a nonzero finite right annihilator after reduction, with all three labels retained.
The finitely many coefficients of any proposed characteristic-zero product generate a field embeddable in \(\mathbb C\), so the assertion applies over an arbitrary characteristic-zero field.
For an original left annihilator apply C101 after group inversion and then invert the group labels again.
In characteristic two no reduction is needed.
We can thus work with a field \(k\) of characteristic two and a row \(a+b u+c v\) with \(abc\ne0\) having a nonzero left or right annihilator.

Let \(\pi:H\to\operatorname{GL}_n(L)\) be any representation over a field extension \(L/k\).
If \(a I+b\pi(u)+c\pi(v)\) is invertible, the row has no finite annihilator on either side.
To see this, twist every coefficient by \(\sum d_h h\mapsto\sum d_h\pi(h)h\).
This is an injective algebra homomorphism to \(M_n(L[H])\), since multiplication respects the group law and each coefficient matrix \(d_h\pi(h)\) is nonzero for \(d_h\ne0\).
Choose a finite \(2\)-group quotient \(Q\) separating the support of the proposed annihilator, by residual \(2\)-finiteness and a finite product of separating quotients.
Its twisted image remains nonzero in \(M_n(L[Q])\).
The augmentation ideal of \(L[Q]\) is nilpotent.
Indeed a nontrivial \(Q\) has a central involution \(t\), \((t-1)^2=0\), and quotienting by \((t-1)\) gives \(L[Q/\langle t\rangle]\), so induction proves the assertion.
The same nilpotence holds for the matrix ideal.
An inverse modulo that ideal lifts to an inverse by the finite geometric series, both on the left and on the right.
The twisted row would therefore be invertible in \(M_n(L[Q])\), contradicting the zero product.

## The constant eigenvalue

The trivial representation first forces \(a+b+c=0\).
Thus \(r=b/c\) belongs to \(k\setminus\{0,1\}\).
Choose an algebraic closure \(\bar k\) containing \(E\), and realize \(s\) as an indeterminate over \(\bar k\).
Take \(L=\bar k(s)\) and use the representation \(M\circ\rho\) from (2).
The singularity just proved gives
\[
      \det\!\big[r(M(U)-I)+(M(V)-I)\big]=0 .
\]
Since \(U-1\) is a unit of \(D\), \(r\) is a root of the reduced characteristic polynomial \(p_Z(t)\in K[t]\).
Clearing denominators and comparing the coefficients of the independent variable \(s\) shows that \(r\) satisfies a nonzero polynomial over \(\mathbb F_2\).
Its minimal polynomial over \(\mathbb F_2\) stays irreducible over the pure transcendental extension \(K\), for example by linear independence of a constant-field basis over \(\mathbb F_2(s)\).

The \(K\)-minimal polynomial of \(Z\) is irreducible since \(K[Z]\) is a finite-dimensional commutative domain.
It is also the minimal polynomial of \(M(Z)\) over \(K\) by faithfulness.
The matrix satisfies this polynomial and its reduced characteristic polynomial belongs to \(K[t]\), so all irreducible factors of the latter equal that minimal polynomial: over a splitting field each eigenvalue satisfies it.
Its degree consequently divides three.
Since \(r\notin\mathbb F_2\), its irreducible polynomial is cubic, equals \(p_Z\), and has coefficients in \(\mathbb F_2\).
The monic irreducible cubics over \(\mathbb F_2\) are \(t^3+t+1\) and \(t^3+t^2+1\), as follows by excluding the two possible roots.
In particular \(r\in\mathbb F_8\setminus\mathbb F_2\), and \(p_Z(0)=p_Z(1)=1\).

It follows that \(\operatorname{Nrd}(Z)=\operatorname{Nrd}(1-Z)=1\).
The identities \(V-1=(U-1)Z\) and \(U-V=(U-1)(1-Z)\) give
\[
           \operatorname{Nrd}(V-1)=\operatorname{Nrd}(U-1)
                                  =\operatorname{Nrd}(U-V).
\]
Multiplying by \(U^{-1}\) preserves the norm since \(U\) has norm one.
In characteristic two \(1-U^{-1}V\) equals \(U^{-1}V-1\), proving condition 2.

## The adjoint representation

The reduced trace of \(1\) is \(3=1\) in \(K\).
Hence \(D_0\) has dimension eight, and the splitting (2) identifies its scalar extension with the trace-zero \(3\times3\) matrices.
Conjugation gives a representation on \(D_0\) defined over \(K\).
After extending scalars to \(L\), the preceding twisting test gives \(P_{u,v}(r,1)=0\).
At \((1,0),(0,1),(1,1)\) the respective matrices in (1) have nullity at least two.
For each noncentral \(W\in\{U,V,U^{-1}V\}\) the same minimal-polynomial argument gives \([K[W]:K]=3\), since a linear minimal polynomial would make \(W\) central.
The subspace \(K[W]\cap D_0\) has dimension at least two and is fixed by \(\operatorname{Ad}(W)\).
Noncentrality follows from faithfulness of the projective representation in C108.
At \((1,1)\) multiply by \(\operatorname{Ad}(U)^{-1}\) to obtain \(I+\operatorname{Ad}(U^{-1}V)\).

At any projective point where the homogeneous matrix has nullity at least two, a constant change of input basis makes at least two columns vanish at that point.
Each entry in those columns is a linear multiple of the linear form defining the point.
Thus the determinant has that linear factor at least twice, and
\[
       P_{u,v}(x,y)=x^2 y^2 (x+y)^2 Q(x,y)
\]
for some homogeneous quadratic \(Q\) over \(K\), allowing the zero polynomial.
Because \(r\ne0,1\), \(Q(r,1)=0\).
The constant \(r\) has degree three over \(K\), so \(Q(t,1)\) vanishes identically and hence \(P_{u,v}=0\).
This proves condition 3.

## Powers in the common character kernel

For \(j\ge0\), the identity \(\rho(v)^{2^j}-1=(\rho(v)-1)^{2^j}\) gives
\[
                    F(v^{2^j})=F(v)^{2^j}.
\]
Their positive orders at infinity are \(2^j\operatorname{ord}_{z=0}F(v)\), which are pairwise distinct.
Only one can equal the order of \(F(u)\), as condition 2 would require.
Noncommuting pairs exist even in \(\ker(d,\psi)\).
For example \(u=a^{21}\) and \(v=b^{21}\) are both in this kernel, and the complete rewriting system of [C105v2](Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) gives the following distinct normal words for \(uv\) and \(vu\), with capital letters denoting inverses:
\[
             a^{21}bF^{10},\qquad
             \mathtt{cgbebdcfedebdccccgffGBGCBGGCEFC}.
\]
The calculation is reproduced by applying \(\mathtt{normal\_form}\) in [J5](../computations/programs/Yin_J_A0005/verify.py) to the two respective concatenations.
The derived conditions are necessary; a support passing all three still requires a separate argument.
