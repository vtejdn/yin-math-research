---
author: Yin
---

# Three nonzero labels exclude type I lattice liberation models

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(e_1,\ldots,e_m\) be a partition of unity by nonzero projections in a finite von Neumann algebra with faithful normal probability trace, and let \(P\) be a projection.
Write \(D=\operatorname{span}\{e_i\}\), \(N=W^*(D,P)\), and \(\mathcal A=\operatorname{alg}^*(D,P)\).
Suppose the partial liberation \(\gamma(e_i)=e_i\otimes1-1\otimes e_i,\ \gamma(P)=0\) descends to a closable outer derivation from \(\mathcal A\subset L^2(N)\) to the coarse correspondence.
In the [finite-label lattice model](Yin_C_F0339_v1.md#statement) this closability follows from its actual vacuum.

If \(N\) is type I and nonabelian, exactly two labels are nonzero.
Every nonscalar matrix fiber has size two almost everywhere, with \(P\) and each of these two labels of rank one, and no nonscalar central atom is possible.
If in addition \(\tau(P)=1/2\) and \(m\ge3\), \(N\) cannot be type I, abelian or otherwise.
Two nonzero labels do occur at trace one half in a type I algebra with actual liberation vacuum zero.
This excludes type I origins of tests with at least three labels, without excluding amenable type II algebras.

## Argument

### Central compression and disjoint pairs of fibers

The actual-vacuum assertion uses that \(i\gamma\) is real under the flipped involution, as is checked on the selfadjoint generators and then on words.
The adjoint product rule pairs a core tensor \(a\otimes b\) against the derivative by using the vacuum against a word with coefficients \(a,b\) and the first partial traces of their derivatives.
Those derivatives are algebraic core tensors, so the resulting functional of the input is Hilbert bounded.
Thus adjoint-domain tensors are dense and \(\gamma\) is closable.

Use the [two-kernel lemma and central descent](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections): if \(zp=0\) for a central projection \(z\) and \(p\in\mathcal A\), then \(z\,\gamma(p)\,z=0\) using the outer actions.
Hence \(\gamma_z(zp)=z\,\gamma(p)\,z\) is a well-defined derivation on the represented algebra \(z\mathcal A\), with the same prescriptions using unit \(z\).
No derivation on a single nonatomic fiber and no boundedness of the compressed vacuum is assumed.

Use the [type I structure theorem](Yin_C_F0216_v1.md#type-i-structure-source) to work on homogeneous central parts with matrix size \(n<\infty\), with the trace measure on the center.
There are at most countably many positive-trace parts.
After partitioning them further by the integer ranks of all generators, call each resulting central piece a rank profile.
As in the [matrix fiber description](Yin_C_F0216_v1.md#homogeneous-summands-and-matrix-fibers), words generate the full matrix algebra almost everywhere: approximate constant matrix units in the \(L^2\) space of the piece by word polynomials and take a subsequence converging in matrix norm almost everywhere.

Take disjoint positive central sets \(S,T\) of constant profiles with dimensions \(n,l\), ordering them so that \(n\ge l\), and apply the compression to \(z=1_S+1_T\).
For almost every \((s,t)\in S\times T\), joint word evaluation on the pair generates \(M_n\oplus M_l\) as a complex algebra.
Indeed \(z\mathcal A\) is dense in \(L^2(zN)\); approximate \(1_S\) there by polynomials and pass to a subsequence converging pointwise on each part.
The finite-dimensional diagonal image is closed and hence contains \((I_n,0)\), and it surjects to each individual matrix algebra by the preceding argument.
This uses disjoint positive central sets rather than any assumption of algebraic independence of their individual fibers.

For such a pair and matrix \(J\in M_{n,l}\), evaluate tensors by \(a\otimes b\mapsto a(s)Jb(t)\).
Denote by \(L_J(p)\) its application to the compressed derivative of the formal word \(p\).
The word rule gives an upper triangular representation with diagonal entries \(p(s),p(t)\) and upper right entry \(L_J(p)\).
Only matrix-unit \(J\)'s need to be used, since they span \(M_{n,l}\).
We check the [two-point splitting argument](Yin_C_F0216_v1.md#splitting-the-two-point-upper-triangular-representation) also when \(n\ne l\).
Put \(k=n^2+1\).
The polynomial
\[
 \sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)
       Y_0 X_{\sigma(1)}Y_1\cdots X_{\sigma(k)}Y_k
\]
vanishes on the compressed algebra by alternation in \(k\) matrices in each space of dimension at most \(n^2\).
Its compressed derivative therefore vanishes on every substitution of words.
There are countably many such substitutions, so on a single conull set of pairs all the triangular representations satisfy the identity, also for polynomial substitutions by multilinearity.
This assertion concerns formal word evaluations and does not require evaluation of an arbitrary center field at a specified point.

The kernel of diagonal projection of the triangular image is a bimodule in \(M_{n,l}\) for the two full matrix algebras, hence is zero or the entire rectangular space by matrix-unit multiplication.
In the latter case the image would be the full block upper triangular algebra.
It violates the identity: use as the \(X\)'s the \(n^2\) different first-block matrix units followed by \(E_{n+1,n+1}\) from the second block.
Writing the resulting list as \(E_{a_j b_j}\), put \(Y_0=E_{1a_1}\), \(Y_j=E_{b_j a_{j+1}}\) between slots, and \(Y_k=E_{b_k,n+1}\).
All these are upper block triangular, and the prescribed row and column in each slot leave only the identity permutation with product \(E_{1,n+1}\).
Thus the diagonal projection is an isomorphism.
Its lift of the central idempotent \((I_n,0)\) has upper-right entry \(K\); commuting with every evaluated word gives \(L_J(p)=p(s)K-Kp(t)\).

### Rank restrictions

Write \(r_i,u_i\) for the label ranks on \(S,T\), and \(q,v\) for their \(P\)-ranks.
At the labels, the prescribed derivative instead gives \(L_J(e_i)=e_i(s)J-Je_i(t)\); at \(P\) it gives zero.
Thus \(J-K\) intertwines the labels and \(K\) intertwines the projections \(P(s),P(t)\).
Every rectangular matrix is a sum of these two kinds of intertwiners because this is true of each matrix unit \(J\).
Their intersection is zero: a simultaneous intertwiner intertwines the diagonal word images, including \((I_n,0)\).
Counting the dimensions of their equal-eigenvalue blocks yields
\[
        \sum_i r_i u_i = q(l-v)+(n-q)v .                              \tag{1}
\]
This equality holds for the two fixed profiles whenever such disjoint positive central subsets exist.

On a nonscalar profile of size \(n>1\), irreducibility gives \(0<q<n\) and \(r_i\le a:=\min(q,n-q)\) for every \(i\).
Indeed if a label range intersects the range or the kernel of \(P\) nontrivially, the intersection reduces all the selfadjoint generators, which a full nontrivial matrix algebra forbids.
The rank inequalities follow by counting dimensions of intersections.
A central atom of this size is impossible: central descent gives an algebraic derivation on the full matrix summand, and the [finite-dimensional diagonal rank identity](Yin_C_F0343_v1.md#two-spaces-of-intertwiners) requires \(\sum_i r_i^2=2q(n-q)+1\), while \(\sum_i r_i^2\le na\le 2q(n-q)\).

Consequently every positive nonscalar profile can be split into two disjoint central sets of positive trace.
Applying (1) to them gives
\[
       2a(n-a)=\sum_i r_i^2\le a\sum_i r_i=an\le 2a(n-a).
\]
Equality forces \(q=n/2\) and every nonzero \(r_i=n/2\); precisely two labels occur there.
Since these two projections are complementary, together with \(P\) the fiber algebra is generated by two projections.
For one of them \(e\), take an eigenvector \(w\) of \(ePe\) on the range of \(e\).
The space spanned by \(w,Pw\) is invariant under both \(P\) and \(e\); irreducibility therefore forces \(n\le2\), so \(n=2\).

Fix a positive nonscalar profile with label pair \(\{i,j\}\).
Another nonscalar profile with a different label pair would have common-label rank sum at most one, whereas the right hand side of (1) equals two.
A scalar profile with its sole label outside \(\{i,j\}\) would have rank sum zero against the fixed profile, whereas the right hand side is one for either scalar \(P\)-value.
Thus every label present with positive trace belongs to the same pair.
If \(N\) is abelian, the commuting finite-spectrum generators instead make \(N\) finite-dimensional; at trace one half the [finite-dimensional exclusion](Yin_C_F0343_v1.md#opposite-scalar-summands-at-trace-one-half) gives \(D=\mathbb C1\).

### A two-label realization

On \([0,\pi]\) with normalized Lebesgue measure and the normalized matrix trace, take symmetries
\[
       a=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
       b=\begin{pmatrix}0&e^{it}\\e^{-it}&0\end{pmatrix}.
\]
Use the two spectral projections of \(a\) as labels and let \(P=(1+b)/2\), of trace one half.
Their algebra is \(L^\infty([0,\pi];M_2)\): the real part of \(ab\) is the scalar \(\cos t\), which generates the center, and the sign of its imaginary part gives the constant diagonal splitting almost everywhere, whose two coordinates \(a\) interchanges.
Every nonempty reduced alternating word in \(a,b\) has zero trace, since odd words are off diagonal and the even words have normalized matrix trace \(\cos(kt)\) for a nonzero integer \(k\).
Distinct reduced words are therefore orthogonal in \(L^2\), so the abstract relations \(a^2=b^2=1\) present the represented word algebra.
The prescribed derivative at \(a\) is \(a\otimes1-1\otimes a\), and it is zero at \(b\); these values respect both square relations.
Each cut of a nonempty reduced word has at least one nonempty reduced word on its two tensor legs, so its double trace is zero.
This proves actuality with vacuum zero in the generated type I algebra.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:38 |
| status | open |
| reason | Fix the exclusion of all type I sources with at least three labels and the sharp two-label realization for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Type I rank and label rigidity, trace-half exclusion and sharpness for two labels. |
| argument | [Argument](#argument) | Central descent, rectangular two-fiber splitting, the rank identity, irreducible fibers and an actual two-label model. |
| dependency | [Lattice model](Yin_C_F0339_v1.md#statement) | Represented partial liberation, actual vacuum, trace convention and labeled algebra. |
| dependency | [Central descent](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the represented derivation to a central projection from closability of the original graph. |
| dependency | [Type I structure](Yin_C_F0216_v1.md#type-i-structure-source) | Decomposition into measurable finite-matrix homogeneous summands. |
| dependency | [Matrix fibers](Yin_C_F0216_v1.md#homogeneous-summands-and-matrix-fibers) | Coarse product measure and fiberwise generation by approximation of matrix units. |
| dependency | [Triangular splitting](Yin_C_F0216_v1.md#splitting-the-two-point-upper-triangular-representation) | Alternating identity, conull word substitutions and central idempotent splitting, adapted to unequal sizes. |
| dependency | [Finite summand rank](Yin_C_F0343_v1.md#two-spaces-of-intertwiners) | The additional diagonal interchange dimension on a single matrix summand. |
| dependency | [Scalar summands](Yin_C_F0343_v1.md#opposite-scalar-summands-at-trace-one-half) | Trace-half obstruction when the generated algebra is abelian finite-dimensional. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:50 |
| status | proved |
| reason | R_F0348 verified the central restrictions, rectangular matrix-fiber argument, classification of noncommutative type I models, sharp example, and all seven declared interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Type I rank and label rigidity, trace-half exclusion and sharpness for two labels. |
| argument | [Argument](#argument) | Central descent, rectangular two-fiber splitting, the rank identity, irreducible fibers and an actual two-label model. |
| dependency | [Lattice model](Yin_C_F0339_v1.md#statement) | Represented partial liberation, actual vacuum, trace convention and labeled algebra. |
| dependency | [Central descent](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression of the represented derivation to a central projection from closability of the original graph. |
| dependency | [Type I structure](Yin_C_F0216_v1.md#type-i-structure-source) | Decomposition into measurable finite-matrix homogeneous summands. |
| dependency | [Matrix fibers](Yin_C_F0216_v1.md#homogeneous-summands-and-matrix-fibers) | Coarse product measure and fiberwise generation by approximation of matrix units. |
| dependency | [Triangular splitting](Yin_C_F0216_v1.md#splitting-the-two-point-upper-triangular-representation) | Alternating identity, conull word substitutions and central idempotent splitting, adapted to unequal sizes. |
| dependency | [Finite summand rank](Yin_C_F0343_v1.md#two-spaces-of-intertwiners) | The additional diagonal interchange dimension on a single matrix summand. |
| dependency | [Scalar summands](Yin_C_F0343_v1.md#opposite-scalar-summands-at-trace-one-half) | Trace-half obstruction when the generated algebra is abelian finite-dimensional. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0348_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
