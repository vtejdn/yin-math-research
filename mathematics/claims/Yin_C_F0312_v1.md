---
author: Yin
---

# The off-diagonal block at an omitted projection has no positive singular atom

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded normal with diffuse spectral law in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Let \(p\) be a nontrivial projection, \(q=1-p\), and \(M=W^*(Z,p)\).
On the represented starred polynomial algebra suppose an outer derivation \(\delta\) has \(\delta Z=1\otimes1,\ \delta p=0\) and actual vacuum \(\xi=\delta^*(1\otimes1)\).
Put \(T=pZq\) and regard \(|T|\) as a positive element of \(qMq\) with unit \(q\).
Its singular law has no atom in \((0,\infty)\).
Moreover the trace in \(M\) of its kernel in \(qMq\) is \(\max\{\tau(q)-\tau(p),0\}\), and the trace of the kernel of \(|T^*|\) in \(pMp\) is \(\max\{\tau(p)-\tau(q),0\}\).

If \(t=\tau(p)=\tau(q)=1/2\), the two corner singular laws coincide and are diffuse.
Writing \(\nu\) for the law of \(|T|\) in \((qMq,\tau/t)\), one has
\[
                         \nu([0,s])^2\le\pi s\,t^{-3/2}\|p\xi q\|_2
                              \qquad(s>0).                               \tag{1}
\]
In particular the two-point modulus of the [nonnormal separating family](Yin_C_F0225_v1.md#statement) cannot occur as the off-diagonal block at any positive parameter.
Approximate concentration of at least \(1/2\) of the normalized trace inside \([0,s]\) already forces \(\|\xi\|_2\ge t^{3/2}/(4\pi s)\).
At trace one half the generated algebra \(M\) has no nonzero finite type I central summand.
These conclusions restrict the candidate models and do not estimate the slice on arbitrary mixed words.

## Argument

### The differentiated singular level

Use the spatial opposite tensor representation \(a\otimes b\mapsto a\otimes b^{\rm op}\), so the two outer multiplier actions are left multiplication by the corresponding two-leg element.
Normality and diffuseness force \(\delta Z^*=k(z,v)=(\bar z-\bar v)/(z-v)\) in the two marginal legs. [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability)
The actual adjoint formula gives closability and hence the [kernel propagation identity](Yin_C_F0216_v1.md#argument) \(r\cdot\delta(x)\cdot l=0\) for every core \(x\), whenever \(r\le1_{\{0\}}(|x^*|)\) and \(l\le1_{\{0\}}(|x|)\).
Here the identity uses the closed graph of the one given derivation; no derivation at \(p\) is needed.
Since \(\delta T=p\otimes q^{\rm op}\), taking the left and right defect projections inside the rectangle gives \(r\otimes l^{\rm op}=0\).
At least one defect is zero.
The support traces agree by polar decomposition, giving exactly the asserted kernel traces.

The coordinating agent proposed testing a positive singular level against the equality between the normal phase times the inner gap and its conjugate.
Suppose \(a>0\) is an atom, \(e=1_{\{a\}}(|T|)\le q\), and \(w=a^{-1}Te\), so \(w^*w=e,\ ww^*=f\le p\).
Apply kernel propagation at \(T^*T-a^2q\) with both test projections \(e\).
Differentiation of \(T^*T\), using \(\delta T^*=(q\otimes p^{\rm op})k\), gives
\[
               (e\otimes w^{\rm op})k=-w^*\otimes e^{\rm op}.
\]
Indeed \(Te=aw\) occurs on the right leg of the term with \(\delta T^*\), and \(eT^*=aw^*\) on the left leg of the term with \(\delta T\).
Multiplication on the left by \(e\otimes(w^*)^{\rm op}\) gives \((e\otimes f^{\rm op})k=-w^*\otimes(w^*)^{\rm op}\).
Multiply on the right by \(Z\otimes1-1\otimes Z^{\rm op}\), using the normal phase identity and the reversed multiplication on the second leg.
Returning to ordinary Hilbert tensors yields
\[
      eZ^*\otimes f-e\otimes Z^*f
              =-w^*Z\otimes w^*+w^*\otimes Zw^*.                         \tag{2}
\]
The functional \(x\mapsto\tau(fx)/\tau(f)\) on the second Hilbert leg takes \(f\) to one and \(w^*\) to zero, since \(w^*=e w^* f\) and \(ef=0\).
Thus \(eZ^*\in\operatorname{span}\{e,w^*\}\) and \(Ze\in\operatorname{span}\{e,w\}\).
Because \(qw=0\), this forces \(qZe=c e\) for some scalar \(c\).
The [scalar-shift bound for the diagonal compression](Yin_C_F0309_v1.md#statement), applied to \(q\), excludes a nonzero kernel of \(qZq-cq\) in \(qMq\).
That kernel would contain \(e\), a contradiction.

### The rectangular estimate at zero

Assume the two corner traces equal \(t\).
Polar decomposition and the kernel calculation identify the two singular laws in normalized corner traces.
For \(u>0\) write \(R=(T^*T+u^2 q)^{-1}\) in \(qMq\), \(L=(TT^*+u^2 p)^{-1}\) in \(pMp\) and \(V=TR=LT\).
Using \(\delta p=\delta q=0\), the inverse and product rules give
\[
             \delta V=u^2 L\otimes R^{\rm op}-(V\otimes V^{\rm op})k .
\]
In the term involving \(\delta T^*\), the factor \(q\otimes p^{\rm op}\) is absorbed because \(Vq=pV=V\).
The identity holds by graph limits of geometric polynomial approximants to the corner inverse \(R\) with ratio \(q-(T^*T+u^2q)/c,\ c>\|T\|^2+u^2\): the differentiated tails are summable since the ratio has norm below one in the corner.
Using \(\|k\|\le1\) in the spatial algebra, tracial Hölder and the normalized spectral law yield
\[
 t^2\left[
     u^2\left(\int\frac{d\nu(v)}{u^2+v^2}\right)^2
       -\left(\int\frac{v\,d\nu(v)}{u^2+v^2}\right)^2
     \right]\le \operatorname{Re}\langle p\xi q,V\rangle_\tau .
\]
Here each scalar trace of \(L,R\) or \(|V|\) acquires the factor \(t\) in the global trace.
Integrate against \(2du/\pi\) from \(s\) to \(R_0>s\), then send \(R_0\) to infinity using the [arctangent divided-difference calculation](Yin_C_F0229_v1.md#argument).
The vector integral of \(V\) has operator norm at most one by its polar formula, and its right support is at most \(q\), so its global Hilbert norm is at most \(\sqrt t\).
The resulting left side is \(2t^2/\pi\) times the \(\nu^2\)-integral of the nonnegative divided difference of \(v\mapsto\arctan(v/s)\), which is at least \(1/(2s)\) on \([0,s]^2\).
This proves (1) with the stated normalization.

### Excluding a finite type I component

Still at trace one half, suppose \(M\) has a nonzero homogeneous finite type I central summand with unit \(c\) and matrix size \(n\).
Such a piece occurs in any nonzero finite type I central summand by the [finite type I decomposition](Yin_C_F0216_v1.md#type-i-structure-source).
The polar part of \(T\) implements equivalence of \(p\) and \(q\), hence \(P=cp,\ Q=cq\) are equivalent and both nonzero.
The [central compression of the derivation](Yin_C_F0216_v1.md#argument) descends on the compressed represented algebra: for any core \(x\) with \(cx=0\), kernel propagation gives \(c\cdot\delta(x)\cdot c=0\).
Thus the compressed derivation takes \(W=cZ\) to \(c\otimes c\) and kills \(P,Q\).

Consider its restriction to the unstarred algebra generated by \(W\) over \(\operatorname{span}\{P,Q\}\).
No finite linear combination of distinct path monomials
\[
                  a_0 W a_1 W\cdots W a_d,\qquad a_j\in\{P,Q\},
\]
can vanish unless all its coefficients are zero.
Indeed the derivative has algebraic tensor values on this subalgebra, so it may be iterated on the leftmost tensor leg.
For a relation of highest \(W\)-degree \(d\), the \(d\)-fold iteration takes each top monomial to \(a_0\otimes\cdots\otimes a_d\) and kills all lower monomials.
Only successive cuts from the last \(W\) toward the first survive.
The resulting top tensors are linearly independent since \(P,Q\) are nonzero orthogonal projections, and the algebraic tensor embeds in the Hilbert tensor product for the faithful trace.
Descending degree proves the assertion.

In particular \(X=PWP,\ Y=PWQWP\) generate an unstarred free algebra in their \(P\) corner: concatenations give distinct paths, whose successive visits to \(P\) recover the sequence of \(X\) and \(Y\).
Set \(d'=n^2+1\), \(B_j=XY^j\) for \(1\le j\le d'\).
The alternating sum of products of these \(B_j\), one per permutation with its sign, is nonzero because the concatenated words are distinct.
In the homogeneous summand it vanishes pointwise, since the alternating product is an alternating multilinear function of \(n^2+1\) vectors in the \(n^2\)-dimensional complex space of matrix entries.
This contradiction excludes every such summand, independently of any bound on possible matrix sizes.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:46 |
| status | open |
| reason | Fix the positive singular atom obstruction, the trace-half rectangular bound and exclusion of finite type I pieces for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Positive singular atoms, exact zero defects, normalized small singular masses at equal trace and the structure of the projection model. |
| argument | [Argument](#argument) | Singular-level graph differentiation, phase-gap identity, rectangular resolvent integral, analytic coefficient paths and a finite-matrix identity. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Phase identity and spatial norm on the diffuse marginal tensor algebra. |
| dependency | [Kernel propagation and central compression](Yin_C_F0216_v1.md#argument) | Compression by left and right kernels for a single closable derivation, including the induced derivation on a central piece. |
| dependency | [Finite type I structure](Yin_C_F0216_v1.md#type-i-structure-source) | Homogeneous finite matrix components over abelian centers. |
| dependency | [Scalar shifts in an omitted corner](Yin_C_F0309_v1.md#statement) | No kernel at a scalar shift of the diagonal compression \(qZq\). |
| dependency | [Arctangent integral](Yin_C_F0229_v1.md#argument) | Signed resolvent test, singular-value kernel and numerical bound. |
| dependency | [Two-point modulus](Yin_C_F0225_v1.md#statement) | Singular law of the old nonnormal separating family. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:51 |
| status | proved |
| reason | Adopt the rectangular singular-law estimates and the finite type I exclusion after independent review of the full proof and its six inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Positive singular atoms, exact zero defects, normalized small singular masses at equal trace and the structure of the projection model. |
| argument | [Argument](#argument) | Singular-level graph differentiation, phase-gap identity, rectangular resolvent integral, analytic coefficient paths and a finite-matrix identity. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Phase identity and spatial norm on the diffuse marginal tensor algebra. |
| dependency | [Kernel propagation and central compression](Yin_C_F0216_v1.md#argument) | Compression by left and right kernels for a single closable derivation, including the induced derivation on a central piece. |
| dependency | [Finite type I structure](Yin_C_F0216_v1.md#type-i-structure-source) | Homogeneous finite matrix components over abelian centers. |
| dependency | [Scalar shifts in an omitted corner](Yin_C_F0309_v1.md#statement) | No kernel at a scalar shift of the diagonal compression \(qZq\). |
| dependency | [Arctangent integral](Yin_C_F0229_v1.md#argument) | Signed resolvent test, singular-value kernel and numerical bound. |
| dependency | [Two-point modulus](Yin_C_F0225_v1.md#statement) | Singular law of the old nonnormal separating family. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0322_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
