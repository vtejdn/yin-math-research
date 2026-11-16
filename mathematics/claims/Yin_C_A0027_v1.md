---
author: Yin
---
# Half-rank obstructions from higher moments and concentration on four points

## Statement

Use the regular representation of a torsion-free discrete group \(G\), the canonical trace \(\tau\), and \(r(a)=\tau(P_{\mathrm{ran}\,a})\), where the range projection is onto the closed range.
The following restrictions concern either scalar factor of a putative [complementary half-rank zero product](../ledger/Yin_L_A0036_v1.md#nontrivial-intersection-and-the-remaining-gap).

1. For a nonzero scalar \(a\) supported in four right cosets of an infinite cyclic subgroup, write \(A\) for the left normalization in [L_A0038](../ledger/Yin_L_A0038_v1.md#normalization), \(X=AA^*\), \(\mu_j=\tau(X^j)\), and \(s=\mu_2\).
   If \(r(a)\le1/2\), then
   \[
     \begin{pmatrix}s-2&\mu_3-2s\\ \mu_3-2s&\mu_4-2s^2\end{pmatrix}\succeq0,\qquad
     \|X^2-2X\|_2^2\le16(s-2).
     \tag{1}
   \]
   These tests also apply to overlapping double cosets.
   A finite product-table condition below gives open sets of Laurent coefficients where \(s>2\) and the second inequality fails.
2. For every nonzero \(b\in\mathbb CG\) supported on at most four group elements,
   \[
                  r(b)\ \ge\ \tfrac12+2^{-69}.
                  \tag{2}
   \]
   There is a constant \(\kappa>0\), independent of the torsion-free group and the coefficients, with the following consequence.
   If \(r(a)\le1/2\) and \(S\) consists of at most four points of \(G\), then
   \[
          \sum_{g\notin S}|a_g|^2\ \ge\ \kappa\sum_{g\in S}|a_g|^2
          \qquad(a\in\mathbb CG).
          \tag{3}
   \]
   In particular (3) applies to the four largest coefficients and uses squared coefficient mass, independently of the cardinality of the remaining support.

## Two moment tests

Write \(A=\sum_i g_i(h)x_i\), with the four \(Hx_i\) distinct and \(\sum_i|g_i|^2=1\) almost everywhere on the circle of \(H=\langle h\rangle\).
Then \(\mu_1=1\) by trace orthogonality, and \(r(A)=r(a)\) by the affiliated change of coefficients.
The row \([g_1(h),\ldots,g_4(h)]\) has operator norm one and the column \((x_1,\ldots,x_4)^{\mathsf T}\) has norm two.
Hence \(0\le X\le4\).
Write \(P=\operatorname{supp}X\).
If \(r(A)\le1/2\), the spectral measure of \(X\) has mass at least \(1/2\) at zero.
Subtract half a unit mass there and apply positivity of the remaining measure to polynomials of degree at most two.
The resulting moment matrix in the basis \(1,x,x^2\) has first row \((1/2,1,s)\) and lower right block \(\left(\begin{smallmatrix}s&\mu_3\\\mu_3&\mu_4\end{smallmatrix}\right)\).
Eliminating its positive first entry gives the first inequality in (1).
This is the degree-two specialization of the [Christoffel variational principle](Yin_C_A0014_v2.md#definition-christoffel-minima-at-the-target-point).

For an explicit lower bound, project \(P\) in trace \(L^2\) onto the span of \(X,X^2\).
Their inner products with \(P\) are \(1,s\).
When \(s\mu_4-\mu_3^2>0\), inverting their Gram matrix gives
\[
 r(A)\ge\frac{\mu_4-2s\mu_3+s^3}{s\mu_4-\mu_3^2}
        =\frac1s+\frac{(\mu_3-s^2)^2}{s(s\mu_4-\mu_3^2)} .
\]
In the singular case \(X^2=cX\) by linear dependence, and taking traces gives \(c=s\), so \(X=sP\) and \(r(A)=1/s\).
In the nonsingular case \(\mu_3>s^2\): equality in Cauchy–Schwarz for \(X^{1/2},X^{3/2}\) would again give \(X=sP\).

Independently, \(\|X-2P\|_2^2=s-4+4r(A)\).
Since \(X^2-2X=X(X-2P)\) and \(\|X\|\le4\), this gives the second inequality in (1).
On any set of group elements at which \(X\) has zero Fourier coefficient, the squared Fourier mass of \(X^2\) alone thus cannot exceed \(16(s-2)\) at half rank or below.
More generally one may use any individual coefficient of \(X^2-2X\).

## A coefficient test above the fourth-moment threshold

Consider representatives \(x_1=1,\ x_2=u,\ x_3=u^2,\ x_4=v\) for four distinct right \(H\)-cosets.
Impose two conditions on the finite group product table.
Among the twelve off-diagonal differences \(x_i x_j^{-1}\), only \(u\) and \(u^{-1}\) occur more than once, each twice.
For \(Y=\{x_i x_j^{-1}:1\le i,j\le4\}\), require \(u^4\notin Y\) and that \(u^4\) has exactly one ordered representation in \(YY\), namely \(u^2u^2\).
These conditions are consistent, for example by reduced word form with \(h,u,v\) free generators.
The resulting degree calculation uses only the indicated finite product data.
In particular the double coset \(HuH\) already repeats.

Take the four constant coefficients \((1,1,1,t)\) with \(0<t<1\).
After row normalization, the diagonal of \(X\) has trace one, and the coefficient of each off-diagonal difference is the sum of its pair weights divided by \(3+t^2\).
The two repeated differences each contribute an extra \(2/(3+t^2)^2\) to the sum of squares beyond treating the pairs separately, giving
\[
                 s=2+\frac{1-t^4}{(3+t^2)^2}.
\]
Also \(\widehat X(u^2)=1/(3+t^2)\), \(\widehat X(u^4)=0\) and \(\widehat{X^2}(u^4)=1/(3+t^2)^2\).
If \(1>16(1-t^4)(3+t^2)^2\), as holds for \(t=9999/10000\), this one coefficient violates (1) despite \(s>2\).
Thus \(r(A)>1/2\) in a case where the direct bound \(1/s\) is strictly below \(1/2\).

Both strict inequalities persist in a sufficiently small circle sup-norm neighborhood of the four coefficient functions.
Indeed the normalizing denominator \((\sum_i|f_i|^2)^{1/2}\) is bounded away from zero there.
The resulting \(A,X,X^2\), their moments and the coefficient at \(u^4\) of \(X^2-2X\) consequently vary continuously, using the operator norm for the operators.
Intersecting this neighborhood with Laurent polynomials allows arbitrarily high degrees and multiple terms in each occupied coset.
The test does not require \(u^4\) to stay outside the Fourier support after such a perturbation.

## Four-point rank

Let \(b=\sum_{i=1}^m c_i g_i\) with distinct \(g_i\), nonzero \(c_i\), \(1\le m\le4\), and normalize \(\sum_i|c_i|^2=1\).
If all ordered off-diagonal differences \(g_i g_j^{-1}\) are distinct, then
\[
 \|bb^*\|_2^2
   =1+\sum_{i\ne j}|c_i|^2|c_j|^2
   =2-\sum_i|c_i|^4\le 7/4 .
\]
Trace Cauchy–Schwarz therefore gives \(r(b)\ge4/7\).

Otherwise let \(d\ne e\) occur for two different ordered pairs.
The corresponding directed edges are left multiplications by \(d\) joining their respective endpoints in \(\{g_i\}\).
They cannot have the same source or the same target and cannot be reverses because \(G\) is torsion-free.
With three different endpoints, all three lie in one right coset of the infinite cyclic group \(\langle d\rangle\), and at most one other support point remains.
With four different endpoints the two edges together lie in at most two such cosets.
Thus the support of \(b^*\) is covered by at most two left \(\langle d\rangle\)-cosets.
One occupied coset gives full rank by the [cyclic-coset theorem](Yin_C_A0019_v1.md#statement).
For two occupied cosets its quantitative bound (2) there has \(t=1/8\) and \(c\ge(1/8)(1/16)^7=2^{-31}\) because the support has at most four points.
It follows that \(r(b)=r(b^*)\ge(1+2^{-68})/2\).
This proves (2) in every case.

## Uniform exclusion of concentration on four coefficients

Fix \(\eta=2^{-70}\).
There exists \(\epsilon>0\) such that every \(b\) considered in (2) with \(\|b\|_2=1\) satisfies
\[
                   \tau(1_{[\epsilon,\infty)}(|b|))>1/2+\eta .
                   \tag{4}
\]
Suppose otherwise and choose \(b_n\) with the left side at \(\epsilon=1/n\) at most \(1/2+\eta\).
Pass to a subsequence with a fixed support size \(m\), enumerate its distinct group elements, and pass to a further subsequence on which the coefficient tuples converge.
Restrict to the subgroup generated by these \(m\) elements in each group: the regular spectral measure is preserved by decomposing into right cosets.
Enumerate the words of the free group \(F_m\) and take a diagonal subsequence along which the truth of each word relation eventually stabilizes.
The words eventually equal to the identity form a normal subgroup \(N\).
The quotient \(F_m/N\) is torsion-free, since a fixed power relation holding eventually in torsion-free groups forces the corresponding word itself to be the identity eventually.
The \(m\) marked elements remain distinct in the quotient, and their limiting coefficients, possibly with some zeros, still have total squared modulus one.
Write \(b_\infty\) for the resulting element.

Every fixed moment of \(b_n^*b_n\) converges to the corresponding moment for \(b_\infty^*b_\infty\), by expansion into finitely many words and convergence of their coefficients.
All these operators have spectrum in \([0,4]\) by \(\|b_n\|\le\sum_i|c_i|\le2\), including the limit case.
Polynomial approximation therefore gives convergence against continuous functions of \(|b_n|\) on \([0,2]\).
By (2), the spectral mass of \(|b_\infty|\) on \((0,2]\) exceeds \(1/2+\eta\).
Choose a continuous function with values in \([0,1]\), supported away from zero, whose integral against this measure exceeds \(1/2+\eta\).
Its integrals for \(b_n\) eventually exceed that number, contrary to the choice at \(1/n\).
This proves (4) uniformly over the groups.

Finally, put \(a_S=\sum_{g\in S}a_g g\) and suppose \(a_S\ne0\).
Apply (4) to \(b=a_S/\|a_S\|_2\), with spectral projection \(E=1_{[\epsilon,\infty)}(|b|)\).
The kernel projection \(Q\) of \(a\) satisfies \(\tau(Q)\ge1/2\), so \(\tau(E\wedge Q)\ge\tau(E)+\tau(Q)-1>\eta\).
On \(E\wedge Q\), \(a\) vanishes and \(a_S\) is bounded below in norm by \(\epsilon\|a_S\|_2\).
Consequently \(\|a-a_S\|_2^2\ge\epsilon^2\eta\|a_S\|_2^2\).
Together with the immediate \(a_S=0\) case this gives (3) with \(\kappa=\epsilon^2\eta\).
The argument provides a uniform existence bound for \(\epsilon\); it supplies no numerical value for it.

## Assessment history

### Decision higher-moments

| Field | Value |
| --- | --- |
| date | 2026-11-17T00:51 |
| status | proved |
| reason | The independent review covers the full fixed statement, proof and stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Higher moments, strict overlapping inputs, four-point rank and uniform coefficient concentration. |
| argument | [Proof](#two-moment-tests) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0058_v1.md#whole-argument-finding) | Independent mathematical review of the result and its limitations. |

## Current assessment

[Selected decision](#decision-higher-moments)
