---
author: Yin
---

# Mixed moments on two cyclic cosets and a finite word test at order twenty

## Statement

Let \(K=P(t)-sQ(t)\) be a two-square affine group-ring pencil in the [normalized order-twenty orientation](Yin_C_A0336_v1.md#the-coefficient-lines).
Write \(Y=\langle t\rangle\), \(F=Y\cup sY\), and \(M(z)=P(z)Q(z)^{-1}\).
In particular \(t\) has infinite order, \(Q\) is invertible on the unit circle, and \(M(z)^2=\omega(z)I\) with \(|\omega(z)|=1\) there.
Under the hypothesis of fractional nullity the [original group word test](Yin_C_A0343_v1.md#which-group-words-can-contribute-to-the-trace) gives
\[
 Y\cap sYs^{-1}=\{e\},\qquad s^{-1}t^a s^{-1}t^b\ne e\quad(a,b\in\mathbb Z).
 \tag{1}
\]
The ambient assumptions for that deduction are torsion-freeness, scalar group-ring injectivity, and the indicated marking.
The following local conclusion uses just (1), the sign character negating \(s\) and fixing \(t\), and the displayed circle hypotheses.
It also applies directly to groups satisfying these premises independently of any fractional kernel.

For a putative kernel projection \(p\), the block at \(u,v\in F\) of its tracial Gram matrix is \((\mathrm{id}\otimes\tau)(u p v^*)=c(v^{-1}u)\), where \(c(x)=(\mathrm{id}\otimes\tau)(xp)\).
There is one array on \(F\), compatible under all finite restrictions, satisfying all the following necessary conditions at unnormalized nullity \(1/2\).

* Equal group differences have equal blocks, reverse differences have adjoint blocks, and the Gram operator is a positive contraction.
* Its diagonal block \(c(e)\) has ordinary trace \(1/2\), and the two coefficient rows of \(K\) annihilate the entire array.
* The sum of \(\|c(x)\|_{\mathrm{HS}}^2\) over the distinct visible differences \(x\in F^{-1}F\) is strictly less than \(1/2\), hence satisfies the scalar upper bound from the projection identity.

These conditions cannot exclude a half kernel at any order on the two cosets.
They impose neither extension to the other group elements nor the full convolution identity for a projection.
The [scattering theorem](Yin_C_A0343_v1.md#statement) already excludes such a kernel for every normalized prototype with three independent numerator coefficients.
For the definite interval \(2<d=\operatorname{tr}(M(0)M(\infty))<5/2\), the four-occurrence word calculation below gives the explicit estimate
\[
                \delta\le \tfrac12-\frac{1}{512\bigl(1+\binom{100}{4}\bigr)}
\tag{2}
\]
for the regular nullity under (1) and the order-twenty marking.
It uses the identity and words with four \(s^{-1}\)'s and total nonnegative \(t\)-exponent at most \(96\), independently of the coefficients throughout that interval.

## Differences in the original group

For \(u=t^j,\ v=t^i\), or \(u=st^j,\ v=st^i\), the difference is \(t^{j-i}\).
The forward mixed differences \(t^{-i}s t^j\) are indexed injectively by \((i,j)\): equality with \(t^{-i'}s t^{j'}\) gives \(t^{i'-i}=s t^{j'-j}s^{-1}\), so both powers are trivial by (1).
These differences are disjoint from their inverses: a common element would give \(s t^a s t^b=e\) for some integers \(a,b\), contradicting (1) after inversion and cyclic permutation.
The sign character separates both mixed sets from \(Y\).
This lists all identifications within the Gram array; the order-twenty quotient alone identifies many more group elements.

The only translate of the four marked sites \(\{e,t,s,st\}\) contained in \(F\) is the original one.
Indeed its left multiplier \(h\) and \(hs\) would both lie in \(F\).
For \(h\in Y\) the sign requires \(hs\in sY\), giving \(h\in Y\cap sYs^{-1}\).
For \(h\in sY\) it requires \(hs\in Y\), giving a forbidden two-step return.
This assertion is about the four sites together, without assuming that every row separately occupies them all.

## A positive contraction in the original input coordinates

Use normalized Haar measure on the circle and set
\[
      N=Q^{-1}P,\qquad D=(I+N^*N)^{-1},\qquad W=D/2 .
\]
All these matrices act pointwise and \(N^2=\omega I\).
In particular \((NN^*)^{-1}=N^*N\) and \(|\det N|=1\).
The positive matrix \(N^*N\) has reciprocal eigenvalues, so \(\operatorname{tr}D=1\).
Functional calculus gives \(NDN^*=D\) and \(ND^2N^*=D(I-D)\): writing \(A=N^*N\) and \(NN^*=A^{-1}\), the two left sides are \(A^{-1}(I+A^{-1})^{-1}\) and \(A^{-1}(I+A^{-1})^{-2}\).
It follows that \(\operatorname{tr}W=1/2\), \(0<W<I/2\), and
\[
     PWP^*=QWQ^*,\qquad PW^2P^*+QW^2Q^*=\tfrac12 QWQ^* .        \tag{3}
\]
These are identities for the actual coefficient pencils.

On \(E=L^2(\mathbb T;\mathbb C^2)\) let \(V\) denote multiplication by \(W^{1/2}\).
Define \(L_A f=\int A(z)f(z)\,dz\) for \(A=P,Q\), with \(dz\) denoting normalized Haar measure, and \(A_0=L_P V,\ B_0=L_Q V\).
Then \(X=A_0 A_0^*=B_0 B_0^*>0\) by (3) and invertibility of \(Q\).
The operator \(J=A_0^*X^{-1}B_0\) is a partial isometry of rank two because \(X^{-1/2}A_0\) and \(X^{-1/2}B_0\) are coisometries.
In particular \(A_0J=B_0\) and \(B_0J^*=A_0\).
Define
\[
  \Gamma=\begin{pmatrix}V&0\\0&V\end{pmatrix}
    \begin{pmatrix}I&J\\J^*&I\end{pmatrix}
    \begin{pmatrix}V&0\\0&V\end{pmatrix}.
\]
The middle block lies between zero and \(2I\), so \(0\le\Gamma\le I\).
Use the orthonormal modes \(z^{-j}\) in each copy of \(E\), corresponding to \(t^j\) and \(st^j\).
Both diagonal blocks are multiplication by \(W\) and have the same Toeplitz coefficients and trace \(1/2\) at difference \(e\).
Each mixed entry may be assigned to its own group difference by (1), with its adjoint on the inverse difference.
The coordinate form of \([L_P,-L_Q]\) is exactly the coefficient row of blocks of \(K\), since \(\int P(z)z^{-j}\,dz=P_j\).
The two partial-isometry identities give \([L_P,-L_Q]\Gamma=0\), the equation against every column at once.
Thus all restrictions are consistent, including those to \(-n\le i,j\le n\).
Any positive contraction is the compression of a single orthogonal projection on a doubled Hilbert space, by adjoining off-diagonal blocks \((\Gamma-\Gamma^2)^{1/2}\) and the complementary diagonal \(I-\Gamma\).
This dilation gives no regular group projection.

## The visible Fourier coefficients

Set \(Y_P=\int P W^2P^*\), \(Y_Q=\int QW^2 Q^*\), so \(Y_P+Y_Q=X/2\).
The mixed operator \(C=VJV\) has rank two.
From \(C= (V A_0^*) X^{-1}(B_0 V)\) its squared Hilbert--Schmidt norm is
\[
 \|C\|_{\mathrm{HS}}^2
  =\operatorname{tr}(X^{-1}Y_P X^{-1}Y_Q)
  =\operatorname{tr}\bigl(H(\tfrac12 I-H)\bigr)\le \tfrac18,
 \qquad H=X^{-1/2}Y_P X^{-1/2}.
\]
Indeed each of the two eigenvalues of \(H\) is in \([0,1/2]\).
The pure coefficients contribute \(\int\operatorname{tr}W^2<1/4\), since \(W\) has two positive eigenvalues summing to \(1/2\).
Parseval on each disjoint mixed orientation gives \(\|C\|_{\mathrm{HS}}^2\) there, while both pure blocks count only once.
The resulting total is strictly below \(1/2\).
A genuine projection would have total energy \((\operatorname{Tr}_2\otimes\tau)p=1/2\) over all group elements.
The estimate uses its scalar budget on the visible elements only.

## A uniform cutoff with four occurrences of the other generator

For \(2<d<5/2\) use the [constant positive form](Yin_C_A0337_v1.md#statement) to put the transfer in a numerical basis in which \(M(z)\) is unitary on the circle.
Changing this basis and passing from the rectangle to \(M(t)-sI\) preserve the nullity.
Put \(U=s^{-1}M(t)\) and use trace normalized by \(1/2\) on the two group coordinates for the following unitary estimates.
The absence of same-sign returns in (1) gives trace zero for \(T=U^2\) by expansion in absolutely summable coefficients.
The sign character fixing \(t\) interchanges the two eigenspaces of \(U\) at \(1,-1\).
Thus \(T\) has mass at least \(\delta\) at one with the normalized trace.
For \(D_0=T^2-I\) the [unitary moment bound](Yin_C_A0343_v2.md#a-word-cutoff-for-each-fixed-real-parameter) gives \(\|D_0\|_2^2\le 8(1-2\delta)\).

Write \(q(z)=z^2-a z+2,\ p_0(z)=2z^2-a z+1,\ a=\pm\sqrt5\), so \(\omega=p_0/q\).
At the marking characters \(y^{10}=1,\ x=\pm y^2\), the matrix \(D_0(x,y)\) is \(((p_0(y)/q(y))^2/y^8-1)I\).
The remainder of \(p_0^2-z^8q^2\) modulo \(z^{10}-1\) is
\[
             -8+8z^2-4a z^3+4z^4-4z^8+4a z^9 .
\]
The squared moduli of its six coefficients sum to \(320\).
Finite Fourier orthogonality and \(\max_{|z|=1}|q(z)|\le3+\sqrt5\) therefore give a character where each diagonal entry of \(D_0(x,y)\) has modulus at least \(\sqrt{320}/(3+\sqrt5)^2>1/2\).

To control the coefficients independently of the chosen transfer, write \(qM=\sum_{j=0}^2 F_j z^j\).
Each \(\|F_j\|\le3+\sqrt5<6\) by Fourier integration in the unitary basis.
The roots of \(q\) are \(\sqrt2 e^{\pm i\theta}\) with \(|\sin\theta|=\sqrt{3/8}\).
The coefficient of degree \(j\) in \(1/q\) has modulus at most \((\sqrt2)^{-j}/(2|\sin\theta|)<(\sqrt2)^{-j}\), by expanding the two geometric factors.
For \(r=4/3\), the Taylor coefficients \(M_j\) therefore satisfy
\[
             \sum_{j\ge0}\|M_j\|r^j
             <\frac{6(1+r+r^2)}{1-r/\sqrt2}<500 .
\]
In \(U^4\) the terms indexed by \(i_1,\ldots,i_4\ge0\) have words \(s^{-1}t^{i_1}\cdots s^{-1}t^{i_4}\).
Those whose index sum exceeds \(96\) have total norm less than \(500^4(3/4)^{96}<1/4\).
Collect in the actual group the identity and the words of index sum at most \(96\), at most \(b=1+\binom{100}{4}\) endpoints of length at most \(100\).
Outside this set the sum of absolute values of the coefficients of a diagonal entry of \(D_0\) is less than \(1/4\), including after any group identifications.
The character with mismatch greater than \(1/2\) forces the absolute coefficient sum on the selected endpoints to exceed \(1/4\).
Cauchy--Schwarz and the normalized two-coordinate trace bound that sum above by \(\sqrt{2b}\,\|D_0\|_2\).
Together with the unitary moment bound this proves (2).
The cutoff bounds an absolutely summable expansion using a uniform tail estimate and does not require solving the word problem or assuming that the selected words are all distinct.
For the other admissible real parameters the existing scattering argument supplies a coefficient-dependent cutoff; the constant in (2) is asserted only on the definite interval.

## Assessment history

### Decision two-coset-moments-and-four-occurrence-cutoff

| Field | Value |
| --- | --- |
| date | 2026-11-28T06:58 |
| status | proved |
| reason | One positive contraction meets the two-coset tests at half trace, and a four-occurrence estimate yields a uniform explicit gap throughout the definite interval. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Statement. |
| argument | [Differences in the original group](#differences-in-the-original-group) | Differences in the original group. |
| argument | [A positive contraction in the original input coordinates](#a-positive-contraction-in-the-original-input-coordinates) | A positive contraction in the original input coordinates. |
| argument | [The visible Fourier coefficients](#the-visible-fourier-coefficients) | The visible Fourier coefficients. |
| argument | [A uniform cutoff with four occurrences of the other generator](#a-uniform-cutoff-with-four-occurrences-of-the-other-generator) | A uniform cutoff with four occurrences of the other generator. |
| dependency | [The coefficient lines](Yin_C_A0336_v1.md#the-coefficient-lines) | The normalized character grid, scalar-square identity and cyclic denominator. |
| dependency | [Statement](Yin_C_A0337_v1.md#statement) | The fixed positive Hermitian form on the definite parameter interval. |
| dependency | [Which group words can contribute to the trace](Yin_C_A0343_v1.md#which-group-words-can-contribute-to-the-trace) | Original-group inequalities for cyclic intersection and same-sign returns. |
| dependency | [Statement](Yin_C_A0343_v1.md#statement) | Scope of the existing exclusion for the normalized exceptional prototypes. |
| dependency | [A word cutoff for each fixed real parameter](Yin_C_A0343_v2.md#a-word-cutoff-for-each-fixed-real-parameter) | The unitary moment bound for normalized coordinate trace and the character test. |
| review | [Two-coset moments and four-occurrence cutoff](../audits/reviews/Yin_R_A0244_v1.md#two-coset-moments-and-four-occurrence-cutoff) | Independent review of the entire fixed proof and its dependency interfaces. |

## Current assessment

[Selected decision](#decision-two-coset-moments-and-four-occurrence-cutoff)
