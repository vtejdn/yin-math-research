---
author: Yin
---
# Independent review of the two scalar tests at a fixed inverse layer

## Whole finding

At 2026-11-22T04:10 UTC a reviewer outside the development of C_A0112_v1 checked its fixed statement and all three proof sections for Yin.
The initial inspection used the Claim and the mathematical inputs it cites, without its development dialogue, author explanations or earlier review conclusions about this Claim.
The two tests and their stated consequences hold with the given trace, group, degree and layer conventions.
The hypotheses needed to apply them in a general induction remain open.

### The compression and its atoms

For \(x\) affiliated with the origin copy let \(p\) and \(e\) be its left and right supports.
The partial inverse of \(x\) gives an isomorphism \(eU\to pU\) by left multiplication by \(x\).
The kernel of \(x^*\) is \((1-p)U\), so for \(w\in pU\) the equation \(x^*(T-\lambda)w=0\) is equivalent to \((pTp-\lambda p)w=0\).
Thus the nullity on \(eU\) is the ambient trace of this kernel projection in the corner, while \((1-e)U\) contributes exactly \(\alpha=\nu(x)\).
The support inverse is used only for the dimension computation, so it places no extra inverse in either test expression.
Trace-preserving inclusion of subgroups takes each generating scalar and each genuine inverse at one layer to the same operation at that layer in the larger group, by induction on the layer.

Let \(\beta=\tau(p)=1-\alpha\).
The integer translates of \(p\) have product trace because any finite family lies in mutually commuting coordinate factors with the direct-product trace.
For \(0<\beta<1\), the probability of an infinite consecutive occupied ray starting at a given site is at most \(\beta^n\) for each \(n\), hence zero.
The probability of any such ray is zero by the countable union over sites and orientations, so finite paths exhaust the corner.
A length-\(\ell\) start has trace \(\alpha^2\beta^\ell\), and its \(\ell\) translates in the path block carry the finite Dirichlet adjacency matrix.
The total contribution has the normalization \(\sum_{\ell\ge1}\ell\alpha^2\beta^\ell=\beta\).
Each eigenline therefore contributes the start trace, even when the eigenvalue appears at several distinct lengths. [Regular coordinate trace](../../claims/Yin_C_A0017_v2.md#copies-in-the-regular-representation), [Dirichlet blocks](../../claims/Yin_C_A0005_v2.md#path-blocks-and-the-exact-kernel-dimension), [corner spectral measure](../../claims/Yin_C_A0005_v2.md#actual-projections-and-boundary-residues).

Injectivity of \(r\mapsto 2\cos(\pi r)\) on \((0,1)\) makes the contributing lengths at a reduced fraction \(a/b\) precisely \(nb-1\), one eigenline for each \(n\ge1\).
Summing the geometric series gives the asserted excess \(\alpha^2\beta^{b-1}/(1-\beta^b)\), strictly decreasing in \(b\).
In particular \(b=2\) gives \(\alpha\beta/(1+\beta)\), while no path contributes at \(2\).
For \(\alpha=0\), \(x\) is a unit, and the Fourier multiplier \(2\cos\theta-\lambda\) of \(T-\lambda\) vanishes on a Haar-null set for every real \(\lambda\).
For \(\alpha=1\), faithfulness implies \(x=0\).
These endpoint checks and the positive interior excess establish both directions of the fixed-group equivalence.

### Dyadic sites, complexity and the induction condition

At step \(m\) the two conjugations in (6) send \(0,\ldots,2^m-1\) respectively to the even and odd sites of \(0,\ldots,2^{m+1}-1\).
The actions transport \(x^*x\) without modifying its coefficient in the copy of \(K\).
For the resulting finite family of positive affiliated copies, spectral projections in different coordinates commute, so joint functional calculus identifies the kernel of their sum with the joint zero projection.
The product trace gives exactly \(\alpha^{2^m}\).
This uses no boundedness of \(x\).
Degree starts at two and grows by at most two per step, and a reused previous output needs only two conjugations and one addition per step.
For polynomial input of word radius \(R\), the first radius is at most \(2R\), and multiplication by the two affine-generator letters adds at most two at each subsequent step.

The multiplier of a finite-order element of the affine permutation group is \(2^n=1\), and its remaining translation then has finite order only for zero displacement.
Translation by any dyadic number is generated because \(us^{-1}\) translates by one and conjugation by \(s^{-d}\) gives translation by \(2^{-d}\).
This proves transitivity, hence generation of every lamp copy from the origin.
The abelian translation kernel and cyclic multiplier image give amenability of the acting group.
The extension and direct-sum arguments for torsion-freeness and amenability therefore apply to the stated two ambient groups.

Under \(P_k(K)\), every \(x\in D_{k+1}(K)\) has a finite polynomial presentation in an allowed alphabet \(F\), since this layer adjoins the inverses of those elements of \(D_k(K)\) that are units in the ambient affiliated ring.
The adjoint-closed alphabet gives the same degree bound \(D\) for \(x^*\).
The positive test of step \(m\) consequently belongs to \(B_{2D+2m}(F)\).
If \(0<\alpha<1\), the logarithm of its reciprocal nullity is \(2^m(-\log\alpha)\), which eventually exceeds \(c(1+2D+2m)^d\) for fixed \(F,D,c,d\).
This proves the sufficient implication, with constants allowed to depend on the alphabet.
Conversely, universal \(P_{k+1}\) on torsion-free groups applies to the whole torsion-free test group, whose indicated alphabet and its words all lie in that layer.
Every positive nullity of such a word combination is then one, giving (7).
The converse uses the universal premise, so it supplies no unconditional estimate for an arbitrary fixed group satisfying only \(P_k(K)\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0112_v1.md#statement) | The fixed-layer scalar identity, exact excess, distinct nullities, dyadic powers, complexity and ambient group properties. |
| [Whole finding](#whole-finding) | [Scalar pencil](../../claims/Yin_C_A0112_v1.md#the-scalar-pencil-and-its-exact-nullities) | Left and right supports, unnormalized corner mass, all path eigenvalues, and the zero and unit cases. |
| [Whole finding](#whole-finding) | [Dyadic sites](../../claims/Yin_C_A0112_v1.md#degree-and-nullity-on-the-dyadic-sites) | Joint positive functional calculus, exact product trace, bounds on degree and radius, finite generation, amenability and torsion-freeness. |
| [Whole finding](#whole-finding) | [Induction estimate](../../claims/Yin_C_A0112_v1.md#a-sufficient-estimate-for-one-induction-step) | Full fixed-alphabet growth contradiction and the converse under universal torsion-free layer injectivity. |
