---
author: Yin
---

# A conditional two-block vacuum test and an obstruction from atoms in the spectral coupling

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X,Y\) be bounded normal elements of a finite von Neumann algebra with faithful normal probability trace.
Write \(\mu,\eta\) for their respective spectral laws and suppose that \(\mu\) is diffuse.
Let \(\gamma\) be the probability on \(\sigma(Y)\times\sigma(X)\) determined by \(\tau(1_E(Y)1_F(X))\), and write \(\gamma(dy,ds)=\eta(dy)\nu_y(ds)\).
For each star polynomial \(h\) on \(\sigma(X)\) use
\[
       D h(s,z)=\frac{h(s)-h(z)}{s-z},\qquad
       L_y(h)=\iint D h(s,z)\,d\nu_y(s)d\mu(z).                           \tag{1}
\]
Values on \(s=z\) may be set to zero.
Define the linear functional on formal sums of two-block words \(\sum_j g_j(Y)h_j(X)\) by \(\sum_j\int g_j(y)L_y(h_j)\,d\eta(y)\), with \(g_j,h_j\) star polynomials.

1. This functional descends to those represented vectors and is bounded in their \(L^2(M)\) norm if and only if there exists \(H\in L^2(\gamma)\) such that, for \(\eta\)-almost every \(y\) and all star polynomials \(h\),
   \[
        L_y(h)=\int h(z)\overline{H(y,z)}\,d\nu_y(z).                      \tag{2}
   \]
   Such \(H\) is unique and its \(L^2(\gamma)\) norm equals the functional norm.
   When \(X,Y\) are distinct coordinates of a normal tuple with actual ACSY, (2) holds and this norm is at most \(\|\xi_X\|_2\) for the actual distinguished vacuum.
   The converse in this item describes boundedness on the two-block subspace only.
2. Suppose on a measurable set of \(y\)'s of positive \(\eta\)-measure the conditional law has the form
   \[
       \nu_y=\sum_{j=1}^{m}\lambda_j(y)\delta_{a_j(y)}+p_y\,\mu ,
                                                                            \tag{3}
   \]
   with fixed finite \(m\ge1\), distinct measurable \(a_j(y)\in\sigma(X)\), measurable \(\lambda_j(y)>0\), and nonnegative jointly measurable \(p_y(z)\) uniformly bounded and uniformly Lipschitz in the plane variable \(z\) on \(\sigma(X)\).
   Then the two-block functional is unbounded or fails to descend.
   No positive lower bound is required for \(p_y\); in particular it can vanish identically.
   Thus such a pair cannot occur as the indicated coordinates of an actual normal ACSY tuple.
3. Take a unitary \(w\) free from \(W^*(X)\), and \(Y=wXw^*\).
   If \(0<|\tau(w)|<1\), the pair fails the two-block test.
   If \(|\tau(w)|=1\), it also fails the test and \(Y=X\).
   If \(\tau(w)=0\), the two copies of \(W^*(X)\) are free.
   At this last endpoint the pair has actual ACSY precisely when the scalar marginal has actual ACSY, and in that case the pair has strong duals with the original bounded-vector domains.
   Hence this conjugation construction cannot produce an actual normal pair lacking bare full-domain duals.

## Argument

### The ordered product space and disintegrated test

The commuting left action of \(Y\) and right action of \(X\) on the trace vector give the joint spectral probability \(\gamma\).
In particular it has the stated marginals, even when \(X,Y\) do not commute.
For existence of the conditional kernel one may take, for each continuous \(f\) on \(\sigma(X)\), the conditional integral of \(f(s)\) over the first coordinate of \(\gamma\).
More explicitly apply scalar Radon–Nikodym to the measures \(E\mapsto\int_{E\times\sigma(X)}f(s)\,d\gamma(y,s)\) against \(\eta\) first on a countable dense rational star algebra of continuous functions.
Outside one null set these functionals are unital, respect rational linear combinations and conjugation, are bounded by \(\|f\|_\infty\) and are nonnegative on squares.
They extend by density to positive linear functionals of norm one, giving probability measures \(\nu_y\) by Riesz representation.
The resulting kernel is measurable first for continuous tests and then for bounded Borel tests by monotone extension.

The map sending \(g(y)h(s)\) to \(g(Y)h(X)\) is an isometry on sums in the \(L^2(\gamma)\) norm.
Indeed the inner product between two such words is the integral of the product of their scalar symbols, by cyclically moving the right factor from the adjointed word to the end of the trace.
The separated star polynomials are dense by compactness and Stone–Weierstrass, so the map identifies \(L^2(\gamma)\) with the Hilbert closure of the ordered two-block words.
The off-diagonal difference in (1) is bounded for every fixed polynomial by its real derivative bound on a rectangle containing the spectrum, and the diagonal is null for \(\nu_y\otimes\mu\) since \(\mu\) is diffuse.
All terms in the formal functional are therefore finite.
Representation of a descended bounded functional by \(H\) gives (2) on each monomial by testing against arbitrary \(g\), using density in continuous functions to identify the two integrable \(y\)-densities.
Countably many monomials suffice to have every polynomial test outside one null set.
Conversely (2) gives the required bounded functional by Cauchy–Schwarz and the two-block isometry, which also gives uniqueness and the norm equality.

For an actual normal tuple, the [normal coordinate phase](Yin_C_F0076_v1.md#statement) forces \(\delta_X g(Y)=0\) and identifies \(\delta_X h(X)\) with \(D h\) on the marginal tensor square.
Under outer multiplication by \(g(Y)\), its double trace is the integral of \(g(y)D h(s,z)\) against \(\gamma(dy,ds)\mu(dz)\).
This identity holds first for elementary rectangular tensors of bounded marginal functions.
It passes to arbitrary bounded marginal \(D h\) by rectangular simple approximation in \(L^2(\mu\otimes\mu)\), since the \(s\)-marginal of \(\gamma\) is \(\mu\) and \(g\) is bounded.
Thus the formal functional is precisely the restriction of \(P\mapsto\langle\xi_X,P\rangle\), with inner products linear in the second variable.
Its representative corresponds to the orthogonal projection of \(\xi_X\) onto the indicated ordered subspace.

### A Lipschitz density and the atomic terms

Suppose (2) holds.
Testing only functions of \(X\), the bounded scalar functional \(\iint D h\,d\mu^2\) has a representative \(\zeta\in L^2(\mu)\).
To see this, integrate (1) over \(y\), use the \(\mu\) marginal, and use the isometry on words \(h(X)\).
Its identity extends to every Lipschitz function \(f\) on \(\sigma(X)\):
\[
        \iint D f(s,z)\,d\mu(s)d\mu(z)=\int f(z)\overline{\zeta(z)}\,d\mu(z).
                                                                            \tag{4}
\]
For this extension, extend each real and imaginary part to the plane with the same Lipschitz constant by the infimum formula \(x\mapsto\inf_u(f_{\rm real}(u)+L|x-u|)\) for a real test of constant \(L\).
Mollifications converge uniformly on the compact spectrum with a uniform Lipschitz bound.
For each mollification, use [real \(C^1\) polynomial approximation on a rectangle](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) to obtain uniform convergence of values and off-diagonal differences there.
Then pass from mollifications to \(f\) by dominated convergence off the null diagonal.
In particular this uses no smoothness or analyticity of a background density beyond its stated Lipschitz bound.

For each eligible \(y\) and each polynomial \(h\), the product \(p_y h\) is Lipschitz on the compact spectrum.
Applying (4) and the product difference rule gives
\[
 \iint p_y(s)D h(s,z)\,d\mu(s)d\mu(z)
       =\int h(z)B_y(z)\,d\mu(z),\qquad
 B_y(z)=p_y(z)\overline{\zeta(z)}
         -\int\frac{p_y(s)-p_y(z)}{s-z}\,d\mu(s).                        \tag{5}
\]
If the common supremum and Lipschitz bounds are \(C,L\), respectively, then \(\|B_y\|_{2,\mu}\le C\|\zeta\|_2+L\).
Consequently \(B_y\) is square integrable in \(\eta(dy)\mu(dz)\) on the eligible set.
So is \(p_y\overline{H(y,\cdot)}\), since \(p_y^2\le C p_y\) and \(p_y\mu\le\nu_y\).

Set \(P_y(z)=\prod_{j=1}^m(z-a_j(y))\).
In (2) take \(h=P_y g\) for any star polynomial \(g\), a valid fiberwise choice because all polynomial tests hold on one full-measure set.
Each atomic input contributes \(\lambda_j(y)\int [P_y(z)/(z-a_j(y))] g(z)\,d\mu(z)\), whereas its point evaluation on the right of (2) vanishes.
The marginal diffuseness permits ignoring the finitely many \(z=a_j(y)\).
Using (5) and polynomial density against finite measures gives, \(\mu\)-almost everywhere off these locations,
\[
     p_y(z)\overline{H(y,z)}-B_y(z)=
                   \sum_{j=1}^m \frac{\lambda_j(y)}{z-a_j(y)}.            \tag{6}
\]
Indeed before division by \(P_y\), the right side times \(P_y\) is an ordinary polynomial in \(z\) and the left side times \(P_y\) is integrable.
Thus for the identity of these finite measures no integrability of the individual poles is presumed.

On a measurable subset \(E\) of positive \(\eta\)-measure, \(\lambda_1\ge\epsilon>0\) and \(|a_j-a_1|\ge2d>0\) for all \(j>1\).
This follows by countable exhaustion from strict positivity and distinctness, with any \(d>0\) when \(m=1\).
Where \(|z-a_1|<d\), the sum over \(j>1\) in (6) is bounded in modulus by \(1/d\), since the weights sum to at most one.
On the complement the first pole is itself bounded by \(1/d\).
Equation (6) and its square-integrable left side therefore give
\[
       \int_E\int \frac{\lambda_1(y)^2}{|z-a_1(y)|^2}\,d\mu(z)d\eta(y)<\infty .
\]
But \(\sigma=(a_1)_*(1_E\lambda_1^2\,\eta)\) is nonzero and \(\sigma\le\mu\), by (3), \(\lambda_1^2\le\lambda_1\), and the marginal identity for \(\mu\).
Consequently this integral is at least the [critical planar self-energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) \(\iint|u-z|^{-2}\,d\sigma(u)d\sigma(z)=\infty\).
This contradiction proves item 2, including graphs of varying location and mass with an arbitrary off-set coupling.

### A conjugated copy of a normal marginal

Put \(\lambda=|\tau(w)|^2\).
For bounded \(g,h\) of \(X\), the centered expansion in the free algebras \(W^*(X),W^*(w)\) gives
\[
    \tau(wg(X)w^*h(X))=
       \lambda\,\tau(g(X)h(X))+(1-\lambda)\tau(g(X))\tau(h(X)).
\]
Indeed the terms linear in \(w-\tau(w)\) or its adjoint have zero trace, and the centered-unitary pair contributes \((1-\lambda)\tau(g(X))\tau(h(X))\) by freeness.
Thus the conditional coupling is \(\nu_y=\lambda\delta_y+(1-\lambda)\mu\).
Item 2 applies whenever \(\lambda>0\).
If \(\lambda=1\), then \(\|w-\tau(w)\|_2^2=0\) makes \(w\) scalar and \(Y=X\); normalization at two copies of a single represented generator is already inconsistent.

If \(\lambda=0\), any reduced alternating centered word in \(W^*(X),wW^*(X)w^*\) expands into an alternating word of centered elements of \(W^*(X)\) and centered \(w,w^*\).
Hence these two copies are free, regardless of the other moments of \(w\).
If the scalar marginal has actual ACSY, the [free-core vacuum calculation](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) extends its two copies by the zero derivation on the opposite factor, preserving both actual vacua by centered-word orthogonality.
Conversely restricting an actual pair derivation to its original marginal and projecting its vacuum there gives scalar actual ACSY by the marginal phase rule.
The [free normal bounds](Yin_C_F0162_v1.md#statement), Part B, then give both original dual domains at each coordinate of the pair.

## Scope

The conditional functional uses the whole marginal polynomial \(h(X)\) following the omitted block \(g(Y)\).
The [first-layer conditional-expectation calculation](Yin_C_F0217_v1.md#statement) treats \(N(X-\mathbb E_N X)N\) and projected columns, while the [free drift theorem](Yin_C_F0212_v1.md#statement) treats Hilbert–Schmidt commutators for semicircular extensions.
The conditional laws determine the norm of this ordered two-block functional; full mixed-word vacuum existence when all these tests are bounded requires additional information.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:10 |
| status | open |
| reason | The conditional criterion, finite atomic graph obstruction and complete free-unitary conjugation test are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact norm of the ordered two-block functional, the obstruction on a positive set of finite atomic graphs over a Lipschitz background, and the endpoints of free-unitary conjugation. |
| argument | [Argument](#argument) | Joint spectral isometry, measurable disintegration, marginal Lipschitz identity, isolation of finite poles, critical energy and the free-product centered expansion. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, zero derivative on the omitted coordinate and its adjoint and the distinguished marginal divided difference with a diffuse marginal under actual ACSY. |
| dependency | [Smooth marginal approximants](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform approximation of a smooth function and both real first derivatives on the rectangle by star polynomials. |
| dependency | [Critical planar self-energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | The inverse-square self-energy of a nonzero compactly supported planar finite measure diverges. |
| dependency | [Free-core vacuum calculation](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Faithful algebraic free-product core and centered-word proof extending a factor derivation and its actual vacuum, applied to each of two scalar normal factors. |
| dependency | [Free normal dual domains](Yin_C_F0162_v1.md#statement) | Part B, canonical strong domains for the free normal pair once its actual vacua have been obtained. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:25 |
| status | proved |
| reason | Adopt the exact two-block test, the conditional atom obstruction and the free-conjugation classification after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact norm of the ordered two-block functional, the obstruction on a positive set of finite atomic graphs over a Lipschitz background, and the endpoints of free-unitary conjugation. |
| argument | [Argument](#argument) | Joint spectral isometry, measurable disintegration, marginal Lipschitz identity, isolation of finite poles, critical energy and the free-product centered expansion. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, zero derivative on the omitted coordinate and its adjoint and the distinguished marginal divided difference with a diffuse marginal under actual ACSY. |
| dependency | [Smooth marginal approximants](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform approximation of a smooth function and both real first derivatives on the rectangle by star polynomials. |
| dependency | [Critical planar self-energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | The inverse-square self-energy of a nonzero compactly supported planar finite measure diverges. |
| dependency | [Free-core vacuum calculation](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Faithful algebraic free-product core and centered-word proof extending a factor derivation and its actual vacuum, applied to each of two scalar normal factors. |
| dependency | [Free normal dual domains](Yin_C_F0162_v1.md#statement) | Part B, canonical strong domains for the free normal pair once its actual vacua have been obtained. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0248_v1.md#whole-proof-finding) | Disintegration, moving poles and critical energy, including a vanishing background and both trace cases for the conjugating unitary. |
