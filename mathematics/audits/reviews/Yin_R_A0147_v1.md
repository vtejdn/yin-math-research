---
author: Yin
---
# Independent review of the norm and adjoint conditions for three group elements

## Whole finding

At 2026-11-21T07:18 UTC a reviewer outside the development of C_A0110_v1 independently checked the [statement](../../claims/Yin_C_A0110_v1.md#statement) and [whole argument](../../claims/Yin_C_A0110_v1.md#argument) for Yin.
The assignment supplied the fixed Claim and its scope, without development dialogue, author explanations, exploration notes, or an earlier verdict on this Claim.
The reviewer read the cited mathematical inputs and a neighboring review of the modular character tests.
The proof establishes all three necessary conditions for both sides of a finite zero product, and the bound of one exponent in the stated family.

### The lift, splitting and valuation

In the right basis \(1,X,X^2\), moving \(c\in E\) past \(X^i\) to the right applies \(\sigma^{-i}\) to \(c\), giving the diagonal entries \(c,c^4,c^2\).
Left multiplication by \(X\) advances the basis index, with \(X^3=s\).
The three diagonal matrices for \(1,\theta,\theta^2\) have independent coordinate vectors by the Vandermonde determinant on \(\theta,\theta^4,\theta^2\).
Multiplication by the two powers of the cyclic shift therefore gives all nine matrix units after extending scalars.
Conjugation by the shift sends the three diagonal entries to \(c^2,c,c^4\) and fixes the shift, which verifies the claimed Frobenius action on the whole image.
The determinant on this splitting is the reduced norm.
For \(X+c\) it is \(s+c^{1+4+2}=s+1\), and a normalized word of signed exponent \(e\) has determinant \((s+1)^e/(s+1)^e=1\).
For a determinant-one matrix of size three the linear coefficient of its characteristic polynomial in characteristic two is the trace of its inverse, giving the stated trace formula at \(1\).

In the Laurent series model, the leading term of a word of signed exponent \(e\) is \(X^e\), as is that of its central normalizing factor even for \(e<0\).
Faithfulness gives \(\rho(h)-1\ne0\) for \(h\ne1\), so its lowest \(T\)-exponent is a positive integer \(m\).
The matrix of left multiplication on the right \(E[[z]]\)-basis \(1,T,T^2\) has unit determinant for every power series unit, since its inverse also has entries in \(E[[z]]\).
For multiplication by \(T\) the determinant is \(z\).
Extending coefficients to \(E((z))\) changes the original splitting basis by \(T=zX^2,\ T^2=zX\).
Thus the \(z\)-order of the reduced norm of \(T^mW\) for a series unit \(W\) is exactly \(m\). [Skew lift and projective faithfulness](../../claims/Yin_C_A0108_v1.md#statement), [Laurent series model](../../claims/Yin_C_A0108_v1.md#explicit-separating-quotients).

### Finite support and coefficient reduction

Multiplication on the left by the given row preserves each \(k[Ht]\), and multiplication on the right preserves each \(k[tH]\).
Translation of a nonzero component gives the appropriate one-sided annihilator in \(k[H]\).
For a finite-order element of \(H\), its odd-order part maps trivially to all finite \(2\)-quotients, hence is trivial by separation.
Its remaining \(2\)-power part has \((\rho(h)-1)^{2^n}=0\) for some \(n\), so the division ring and faithfulness force \(h=1\).
This proves exactly the torsion-free hypothesis of the [finite-place reduction](../../claims/Yin_C_A0101_v1.md#statement).
The row and witness use finitely many coefficients in characteristic zero, so their field embeds in \(\mathbb C\) by choosing images of a transcendence basis and extending over the finite algebraic extension.
After normalizing the row, its three coordinates are units at the chosen place over two.
Scaling the witness by a coordinate of least valuation retains at least one nonzero residue coefficient.
For a left annihilator, group inversion first gives a right annihilator of the inverse-label row, and a second inversion restores the original three labels after reduction.

For every representation \(\pi\) over an extension of the residue field, the coefficient of \(h\) in the twisted witness is its scalar coefficient times \(\pi(h)\).
A finite \(2\)-quotient separating all pairwise differences in the witness support keeps at least one such nonzero matrix coefficient.
If \(I\) is the augmentation ideal of the quotient group algebra, induction on the group order gives \(I^N\subseteq(t-1)\) for a central involution \(t\) and some \(N\), whence \(I^{2N}=0\).
A matrix invertible modulo \(I\) is invertible over the group algebra by lifting its scalar inverse and summing the finite series in the nilpotent matrix error.
Multiplication of the zero-product equation by this inverse would force the surviving witness to be zero.
Therefore every such matrix evaluation of the row is singular.
The same argument starts with the given field when its characteristic is already two.

### The three conditions and the power family

The trivial representation forces \(a=b+c\), so \(r=b/c\) differs from \(0,1\).
In the splitting representation the evaluated matrix divided by \(c\) factors as \(M(U-1)(rI+M(Z))\).
The first factor is invertible, so the degree-three reduced characteristic polynomial \(p_Z\) vanishes at \(r\).
Clearing denominators in \(p_Z(t)\) gives a nonzero polynomial in \(s,t\) over \(\mathbb F_2\).
As \(s\) is transcendental over \(\bar k\), each coefficient of \(s^i\) vanishes at \(r\), and some such coefficient is a nonzero polynomial in \(t\).
The minimal polynomial of the algebraic constant \(r\) has the same degree over \(K\) as over \(\mathbb F_2\), by extending a basis of \(\mathbb F_2(r)\) to rational functions in \(s\).
The minimal polynomial of \(Z\) over \(K\) is irreducible because \(K[Z]\) is a field.
It annihilates \(M(Z)\), so every eigenvalue of \(M(Z)\) is a root of that same irreducible polynomial.
Consequently \(p_Z\) is its power and its irreducible factor has degree dividing three.
Since \(r\) is a root outside \(\mathbb F_2\), the degree is three and \(p_Z\) is the minimal polynomial of \(r\).
The two monic cubics over \(\mathbb F_2\) without roots give the list in condition 1, and both have value one at \(0,1\).
Thus \(Z\) and \(1-Z\) have norm one.
Factoring \(V-1\) and \(U-V\) on the left by \(U-1\), then multiplying the latter by \(U^{-1}\) of norm one, yields all three equalities in condition 2.

The reduced trace of \(1\) is \(1\), so the trace-zero subspace \(D_0\) has dimension eight.
The projective faithfulness from C_A0108 and the distinctness of \(1,u,v\) make each of \(U,V,U^{-1}V\) noncentral.
For each such \(W\) the same degree-divisibility argument gives \([K[W]:K]=3\).
The restriction of the trace to this subfield has rank one, leaving two independent trace-zero vectors fixed by conjugation.
They give nullity at least two for the adjoint pencil at \((1,0),(0,1),(1,1)\), using left multiplication by \(\operatorname{Ad}(U)^{-1}\) at the last point.
At each of the three points a \(K\)-basis starting with two kernel vectors gives two columns of linear forms vanishing there.
Each column contributes one copy of the corresponding linear factor to the determinant, hence the product \(x^2y^2(x+y)^2\) divides it.
The adjoint representation after extension to \(\bar k(s)\) forces the determinant to vanish also at \((r,1)\).
None of the three linear factors vanishes there, and a nonzero polynomial of degree at most two over \(K\) cannot vanish at \(r\).
The remaining homogeneous quadratic is therefore zero, proving condition 3.

Frobenius powers of \(\rho(v)-1\) have norms \(F(v)^{2^j}\), of strictly increasing orders \(2^j\operatorname{ord}_{z=0}F(v)\) for \(v\ne1\).
At most one order can equal that of \(F(u)\).
Since \(21\) is divisible by both character group orders, \(a^{21},b^{21}\) belong to the common kernel.
The reviewer reran the presentation and overlap check in [J_A0005](../../computations/programs/Yin_J_A0005/verify.py), obtaining 98 rules and 560 joined overlaps.
Applying its normal form to the two words gave \(a^{21}bF^{10}\) and \(\mathtt{cgbebdcfedebdccccgffGBGCBGGCEFC}\), respectively.
Their difference establishes noncommutation by the [complete rewriting system](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system).
Passing the three conditions leaves existence of a finite annihilator undecided, and the review gives no assertion about an arbitrary \(\ell^2\) kernel.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0110_v1.md#statement) | All three necessary conditions for both finite annihilator sides in characteristic zero or two, and the bound on power indices including the common character kernel. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0110_v1.md#argument) | All five sections, including the local valuation, finite quotient twisting, the two representations and the noncommuting example. |
| [Whole finding](#whole-finding) | [Faithful lift and projective model](../../claims/Yin_C_A0108_v1.md#statement) | The skew division algebra with its center, the normalized lift, projective faithfulness, the characters and residual two-finiteness of the type kernel. |
| [Whole finding](#whole-finding) | [Laurent series embedding](../../claims/Yin_C_A0108_v1.md#explicit-separating-quotients) | Embedding at infinity, the skew action on the coefficients and the powers of the series parameter. |
| [Whole finding](#whole-finding) | [Finite-place reduction](../../claims/Yin_C_A0101_v1.md#statement) | Reduction of a normalized three-label row and a finite witness for a torsion-free group, preserving every row label and a nonzero witness. |
| [Whole finding](#whole-finding) | [Complete rewriting system](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) | Equality of group words is equivalent to equality of the irreducible forms in the seven triangle generators. |
| [Whole finding](#whole-finding) | [Normal-form program](../../computations/programs/Yin_J_A0005/verify.py) | The presentation and overlap check and the normal forms of the two orders of the twenty-first powers. |
