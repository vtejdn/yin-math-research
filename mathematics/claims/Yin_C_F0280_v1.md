---
author: Yin
---

# Alternating conditional expectations give a full-column test for a normal pair

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \((Z,Y)\) be a bounded normal generating pair in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace and [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Write \(B=W^*(Z)\), \(N=W^*(Y)\), \(D=B'\cap M\), \(C=N'\cap M\), and \(P=\mathbb C\langle Z,Y,Z^*,Y^*\rangle\).
Let \(E_0=(\mathrm{id}\otimes\tau)\delta_Z\) be the original right slice on \(P\).
Suppose its single-input norm \(a=\sup_{\|p\|\le1,\,p\in P}\|E_0p\|_2\) is finite.
Write \(E:M\to L^2(M)\) for its normal extension and \(h\in L^1(M)_+\), \(k\in L^1(C)_+\) for any two densities of traces at most one satisfying
\[
              \|Ex\|_2^2\le a^2\big(\tau(hx^*x)+\tau(kxx^*)\big)
                           \qquad(x\in M).
\]
These densities exist by the [two-state estimate](Yin_C_F0276_v1.md#statement).
Use the scalar curvature weight \(W\in L^1(B)_+\) and scalar slice \(S\) of the law of \(Z\), with weighted norm at most \(s_0=2+\sqrt2\) and \(\tau(W)=\|\xi_B\|_2^2\), where \(\xi_B\) is the marginal conjugate variable. [Scalar weight estimate](Yin_C_F0267_v1.md#statement)

For every \(b\in B\) and \(x\in M\), the operator-first commutator is
\[
      E(bx)-bE(x)= S\big(b\,\mathbb E_Bx\big)-bS(\mathbb E_Bx).
                                                                     \tag{1}
\]
Here \(S\) is the weighted extension of the original scalar slice to bounded Borel inputs, and the values in (1) belong to \(L^2(B)\) on the right.
Let \(\Lambda=\mathbb E_C\mathbb E_D\) be the composition of the trace-preserving conditional expectations on \(L^1(M)\), with the rightmost applied first.
For every integer \(m\ge1\) and \(x\in M\),
\[
 \|Ex\|_2\le
 a\sqrt{\tau(hx^*x)+\tau((\Lambda^m k)xx^*)}
                 +2m s_0\|x\sqrt W\|_2 .                             \tag{2}
\]
If \(K=\|\Lambda^m k\|_\infty<\infty\), the original finite-column cost \(c\), the supremum of \((\sum_j\|E_0p_j\|_2^2)^{1/2}\) over \(\|\sum_jp_j^*p_j\|\le1\), satisfies
\[
                   c\le a\sqrt{1+K}+2m s_0\|\xi_B\|_2.               \tag{3}
\]
In particular it suffices that \(\Lambda^m\) map \(L^1(C)_+\) into \(M\) with \(\|\Lambda^m f\|_\infty\le K_0\|f\|_1\) on this cone.
Then \(K_0\) can be used in (3) without choosing \(k\).

Here is a criterion using just the two spectral algebras and their joint two-block trace.
Suppose \(B,N\) are maximal abelian in \(M\), and their ordered spectral probability \(\gamma(dy,dz)\), determined by \(\tau(1_G(Y)1_F(Z))\), has density \(g(y,z)\) with respect to the product of their laws \(\eta(dy)\mu(dz)\).
Set
\[
                   H(y,y')=\int g(y,z)g(y',z)\,d\mu(z).
\]
Let \(H_m\) be the kernel of its \(m\)-fold composition with integration in \(\eta\).
If \(H_m\) is essentially bounded, (3) holds with \(K=\|H_m\|_\infty\).
In particular, \(g\le L\) gives \(K\le L\) with \(m=1\).
More generally the same single-step test holds with \(K=L^2\) if \(\operatorname*{ess\,sup}_y\|g(y,\cdot)\|_{L^2(\mu)}\le L\), allowing an unbounded joint density.
These estimates control every mixed polynomial output, with no dependence on its degree.
The integer \(m\) measures the number of averaging steps in the test.

## Argument

### The full marginal commutator

On \(B\) the scalar estimate extends \(S\) by polynomial density to \(L^2(W\,d\mu)\to L^2(\mu)\).
Indeed continuous functions and then polynomials in \(z,\bar z\) are dense for the finite Borel measure \(W\,d\mu\).
For each bounded \(b\in B\), choose marginal polynomials \(b_l\) uniformly bounded and converging almost everywhere to \(b\).
For this construction, approximate \(b\) by continuous functions in \(L^2(\mu)\), project their values onto the closed disk of radius \(\|b\|_\infty\), approximate uniformly by starred polynomials, and extract an almost everywhere convergent subsequence.
This prescription also gives convergence in \(L^2((1+W)d\mu)\).
Consequently \(b\) is in the graph closure of the original scalar slice and its value there agrees with \(Sb\).
The scalar slice is closable by its actual vacuum.

First let \(b\) be a marginal polynomial.
The product rule on \(x\in P\) gives
\[
       E(bx)-bE(x)=\Theta(\delta_Z b)x,\qquad
       \Theta(s\otimes t)x=s\,\tau(tx).
\]
The derivative of \(b\) is its scalar divided difference in \(L^2(B)\otimes_2 L^2(B)\) by the [normal starred symbol rule](Yin_C_F0076_v1.md#statement).
Thus the Hilbert--Schmidt operator \(\Theta(\delta_Z b)\) takes values in \(L^2(B)\) and depends on \(x\) only through \(\mathbb E_Bx\), by finite tensor approximation.
For \(x\in M\), both sides are normal in \(x\): a bounded Hilbert operator applied to \(x1\) has normal matrix elements, and multiplication and \(E\) on the left are normal.
The identity therefore holds on all of \(M\).
Normality of \(E\) and the preceding bounded marginal approximation give \(E(q)=S(q)\) for each \(q\in B\), by testing the weak limit of \(E(q_l)\) against the strong \(L^2\) limit of \(S(q_l)\).
Apply the commutator identity also at \(x=\mathbb E_Bx\) to obtain (1) for polynomial \(b\).
For arbitrary bounded \(b\) use the same approximants \(b_l\).
The left side converges weakly by normality of \(E\) and bounded strong convergence of the multipliers.
The scalar \(S(b_l\mathbb E_Bx)\) converges in norm by weighted dominated convergence, and \(b_l S(\mathbb E_Bx)\to b S(\mathbb E_Bx)\) in norm.
This proves (1) on both claimed domains.

For \(u\) unitary in \(B\), both terms on the right of (1) have norm at most \(s_0\|(\mathbb E_Bx)\sqrt W\|_2\), which is at most \(s_0\|x\sqrt W\|_2\) by conditional Schwarz and truncation of \(W\).
For every unitary \(v\in N\), the omitted-algebra module property gives \(E(vx)=vE(x)\). [Normal extension and module property](Yin_C_F0276_v1.md#averaging-over-the-omitted-algebra)
Suppose \(w\) is a finite product of unitaries of \(B,N\) with at most \(m\) factors from \(B\).
Telescoping its commutator evaluates each nonzero term at a unitary left multiple of \(x\).
Left multiplication by a unitary preserves both \(\|x\sqrt W\|_2\) and the norm of any output, giving
\[
                  \|E(wx)-wE(x)\|_2\le2m s_0\|x\sqrt W\|_2.         \tag{4}
\]

### Averaging the row density

Apply the original two-density estimate to \(wx\).
By (4) and positivity of the densities,
\[
 \|Ex\|_2 \le
 a\sqrt{\tau(hx^*x)+\tau(w^*kw\,xx^*)}+2m s_0\|x\sqrt W\|_2 .
\]
For a finite probability average of such products, average this inequality and use concavity of the square root.
The same bound then holds with the averaged density in the row term.

For either \(A=B\) or \(A=N\), the conditional expectation onto \(A'\cap M\) of a positive \(L^1\) density is in the \(L^1\)-closed convex hull of its conjugates by unitaries of \(A\).
This is the [conditional-expectation averaging argument](Yin_C_F0276_v1.md#averaging-over-the-omitted-algebra): for bounded truncations take the unique least-norm point of the closed convex hull in \(L^2\), which is the invariant projection, and use \(L^1\) contraction and truncation to obtain the assertion for the original density.
Apply this first with \(B\), then with \(N\), repeating the pair of operations \(m\) times.
The value \(\Lambda^m k\) lies in the \(L^1\)-closed convex hull of the conjugates \(w^*kw\) with \(w=u_1v_1\cdots u_mv_m\), \(u_j\in\mathcal U(B)\), \(v_j\in\mathcal U(N)\).
Indeed at each next step approximate the conditional expectation of the preceding target by a finite average, then apply that same average to a preceding approximant.
Conjugation averages contract \(L^1\), so the two approximation errors add.
Passing to the limit at each fixed \(xx^*\in M\) gives (2).

When \(\Lambda^m k\le K1\), traciality bounds the row term by \(K\tau(x^*x)\).
Apply (2) to each element of a finite column and take its Euclidean norm using the triangle inequality.
The first term is bounded by \(a\sqrt{\tau(h)+K}\,\|\sum_j x_j^*x_j\|^{1/2}\), and the second by \(2m s_0\sqrt{\tau(W)}\,\|\sum_j x_j^*x_j\|^{1/2}\).
This proves (3), even on all bounded columns.

### The criterion in terms of two marginal laws

Maximal abelianness gives \(C=N\) and \(D=B\).
The defining rectangle probabilities identify \(\mathbb E_B f(Y)(z)=\int f(y)g(y,z)\,d\eta(y)\), first on simple functions and then on positive integrable functions by truncation.
The analogous conditional expectation onto \(N\) uses integration in \(z\).
Both row and column integrals of \(g\) are one almost everywhere by its marginals.
Tonelli's theorem identifies \(\Lambda\) on \(L^1(N)_+\) with the stated kernel \(H\), and iteration gives \(H_m\).
Hence an essentially bounded kernel gives the stated \(L^1\)-to-\(L^\infty\) estimate.
The bound \(H\le L\) for \(g\le L\) follows by estimating just one factor, using the unit row mass for the other.
The last single-step test follows by Cauchy--Schwarz in \(L^2(\mu)\).

For example, if the two diffuse marginal algebras are free, both are maximal abelian in their generated tracial free product.
Indeed the orthogonal complement of either \(L^2\) marginal decomposes into sums of coarse bimodules over that marginal, and conjugation by powers of a marginal Haar unitary converges weakly to zero there, by the [free-product averaging argument](Yin_C_F0243_v1.md#recovering-the-abelian-algebra-and-the-conjugating-unitary).
Thus every bounded element commuting with that marginal lies in it.
The ordered pair law has \(g=1\) by freeness and \(K=1\) works in one step.
For a nonfree pair the same test requires its own commutants and density.
The argument does not derive the assumed single-input bound from the joint conjugate variable.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:39 |
| status | open |
| reason | Fix the full marginal commutator on bounded Borel inputs and the full-column criterion through a finite iterate of conditional expectations for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact commutator for arbitrary bounded marginal functions, quantitative original mixed columns, iterated row test and ordered spectral criteria. |
| argument | [Argument](#argument) | Bounded marginal approximation, weighted commutator telescoping, successive convex averages, spectral kernels and the free example. |
| dependency | [Single-input normal extension and row estimate](Yin_C_F0276_v1.md#statement) | Normal extension, two trace-controlled densities, omitted-unitary equivariance and conditional-expectation averaging for positive integrable densities. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Weighted bound for the original scalar right slice, its weight mass and scalar vacuum at the distinguished marginal. |
| dependency | [Normal symbol](Yin_C_F0076_v1.md#statement) | Divided differences of marginal starred polynomials in the marginal coarse tensor space. |
| dependency | [Free-product averaging](Yin_C_F0243_v1.md#recovering-the-abelian-algebra-and-the-conjugating-unitary) | Diffuse abelian free-factor coarse complement and averaging by powers of a Haar unitary for the product-density example. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:52 |
| status | proved |
| reason | The independent review verifies the full bounded marginal commutator and the alternating-expectation estimate for mixed columns of every length. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact commutator for arbitrary bounded marginal functions, quantitative original mixed columns, iterated row test and ordered spectral criteria. |
| argument | [Argument](#argument) | Bounded marginal approximation, weighted commutator telescoping, successive convex averages, spectral kernels and the free example. |
| dependency | [Single-input normal extension and row estimate](Yin_C_F0276_v1.md#statement) | Normal extension, two trace-controlled densities, omitted-unitary equivariance and conditional-expectation averaging for positive integrable densities. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Weighted bound for the original scalar right slice, its weight mass and scalar vacuum at the distinguished marginal. |
| dependency | [Normal symbol](Yin_C_F0076_v1.md#statement) | Divided differences of marginal starred polynomials in the marginal coarse tensor space. |
| dependency | [Free-product averaging](Yin_C_F0243_v1.md#recovering-the-abelian-algebra-and-the-conjugating-unitary) | Diffuse abelian free-factor coarse complement and averaging by powers of a Haar unitary for the product-density example. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0289_v1.md#finding) | The conditional expectation order, weighted telescoping, both density tests and the free diffuse example. |
