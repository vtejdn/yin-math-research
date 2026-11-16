---
author: Yin
---

# Exchange symmetry and the mixed output of a normal coordinate

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Use the finite tracial relative models of the [projection reduction](Yin_C_F0308_v1.md#statement), with one bounded normal generator and finitely many bounded selfadjoint coefficients killed by its actual distinguished derivation.
Write \(K_{\rm rel}\) for the supremum of the right slice norm on polynomial contractions divided by the distinguished vacuum norm.
Define \(K_{\rm sign}\) by restricting to one projection coefficient \(P\) in \(M=W^*(Z,P)\) such that a trace-preserving involutive automorphism \(\beta\) fixes \(Z\) and sends \(P\) to \(1-P\).
In particular \(\tau(P)=1/2\).

Let \(K_{\rm ex}\) be the corresponding supremum at the first generator of a pair \((Z_0,Z_1)\) of bounded normal generators of \(Q\) with [full actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) and a trace-preserving involutive automorphism exchanging them.
Let \(E_0\) and \(\xi_0\) be the first right slice and vacuum, \(B_0=W^*(Z_0)\), and let \(\mathbb E_{B_0}\) denote trace-preserving conditional expectation.
Define \(K_{\rm mix}\) on the same pairs and polynomial contractions \(x\) by using \(\|(1-\mathbb E_{B_0})E_0x\|_2/\|\xi_0\|_2\).
In the extended nonnegative reals,
\[
 \begin{aligned}
 K_{\rm sign}&\le K_{\rm rel}\le 2K_{\rm sign},\\
 K_{\rm ex}&\le K_{\rm sign}\le \sqrt2 K_{\rm ex},\\
 K_{\rm mix}&\le K_{\rm ex}\le\sqrt{K_{\rm mix}^2+(1+\sqrt2)^2}.
 \end{aligned}                                                        \tag{1}
\]
Thus the universal normal implication \(\mathsf A\Rightarrow\mathsf S\) is equivalent to \(K_{\rm mix}<\infty\).
Every finite relative witness transfers to an exchange-symmetric pair at a ratio at least \(1/(2\sqrt2)\) times the original ratio up to arbitrary additive error.
The scalar marginals in these pairs coincide, and the remaining output vanishes on the linear span of polynomials in the individual generators.
The finiteness of \(K_{\rm mix}\) remains open.

More precisely, in a sign-symmetric projection model put \(s=2P-1\), \(Q=M^\beta\), \(B=W^*(Z)\), \(N=\operatorname{span}\{1,s\}\), and \(K=B\oplus sB\) with both summands closed in trace Hilbert norm.
Then \(Q=W^*(Z,sZs)\) is an exchange-symmetric pair algebra and every core element has a unique expression \(a+bs\) for polynomials \(a,b\) in those two normal generators and their adjoints.
For the projection model's slice \(E\) and vacuum \(\xi\),
\[
 E(a+bs)=E_0a+(E_1b)s,\qquad
 \|\operatorname{proj}_K Ex\|_2\le(1+\sqrt2)\|\xi\|_2\|x\|.            \tag{2}
\]
Here \(E_1\) is the slice at \(sZs\), the terms in the first formula are orthogonal, and \(\xi=\xi_0\) inside \(L^2(Q)\).
The second estimate bounds the whole output on finite sums of \(n f(Z)n'\) with \(n,n'\in N\) and marginal starred polynomials \(f\).

## Argument

### The sign change in the projection model

In the [doubled matrix construction](Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) let \(J=\mathrm{diag}(1,-1,\ldots,-1)\) on the first \(k\) indices and \(D=\mathrm{diag}(J,-J)\) on the doubled matrix algebra.
Its star-shaped matrix \(B_{\rm mat}\) has nonzero entries only between the first index and the other indices, so \(JB_{\rm mat}J=-B_{\rm mat}\).
Consequently \(J\) commutes with \((1-(B_{\rm mat}/c)^2)^{1/2}\).
In the two diagonal blocks of \(2P_0-1\), conjugation by \(D\) reverses the sign of \(B_{\rm mat}\), and in its off-diagonal blocks the extra minus sign reverses the sign of the square root.
Thus \(DP_0D=1-P_0\), whereas \(DWD=W\) for its diagonal normal generator \(W\).

Conjugation by \(D\) on the matrix base and \(S\mapsto-S\) on the independent standard semicircular factor extend to one trace-preserving involution on their free product.
Indeed the factor maps preserve centered letters, the reduced-word trace, and multiplication, and the resulting trace isometry on the dense free-product algebra intertwines left multiplication in its trace representation.
The map sends \(Y=P_0+\varepsilon S\) to \(1-Y\).
As \(1/2\) is in the spectral gap, it sends \(P=1_{(1/2,\infty)}(Y)\) to \(1-P\), and it restricts to \(W^*(W,P)\).
The [direct witness comparison](Yin_C_F0308_v1.md#direct-comparison-of-the-original-and-compressed-slices) on precisely these output models therefore gives \(K_{\rm rel}\le 2K_{\rm sign}\), with the finite-witness assertion and arbitrary additive error there.
Inclusion gives \(K_{\rm sign}\le K_{\rm rel}\).

### Derivations on the even algebra

For any such projection model let \(\alpha=\operatorname{Ad}_s\) on \(Q\).
Since \(s^2=1\) and \(\beta s=-s\), moving each occurrence of \(s\) to the right groups every word in \(Z,Z^*,s\) as an even polynomial in \(Z_0=Z,\ Z_1=sZs\) and their adjoints, possibly followed by \(s\).
The trace of each odd word vanishes by invariance under \(\beta\).
The two parts of any polynomial \(x=a+bs\) are \((x+\beta x)/2\) and \((x-\beta x)/2\), proving uniqueness.
The normal conditional expectation \((1+\beta)/2\) onto \(Q\) and weak density of the core give \(Q=W^*(Z_0,Z_1)\).
The odd Hilbert space is \(L^2(Q)s\), since right multiplication by \(s\) exchanges the two spaces.
In particular \(M\) has the tracial crossed-product representation \(Q\rtimes_\alpha\mathbb Z/2\): the two Fourier coefficients in this algebra have the same multiplication, involution and trace Hilbert norm as \(a+bs\) in \(M\).
The resulting trace isometry intertwines the generated left algebras.
The automorphism \(\alpha\) exchanges \(Z_0,Z_1\).

The relative derivation \(\delta\) is equivariant for \(\beta\) acting on both tensor legs.
Indeed the assignments at \(Z,s\) are equivariant and the forced value at \(Z^*\) is the marginal phase.
This uses the [normal phase identity](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) at a single relative coordinate, by projecting the restricted marginal derivative and vacuum to the marginal before applying the scalar diffuseness conclusion.
The double-trace identity and equivariance show \(\beta\xi=\xi\).
On the even polynomial core the derivative splits into its even-even and odd-odd parts.
Projection onto either part commutes with the outer actions of \(Q\).
Take \(D_0\) to be the even-even part and \(D_1\) the odd-odd part followed by the inner isometry \(I_{s\otimes s}(u\otimes v)=us\otimes sv\) to even-even.
Both are represented outer derivations into the coarse space of \(Q\).
At \(Z_0,Z_1\) the two values of \(\delta\) are \(1\otimes1,s\otimes s\), respectively, giving the unit derivative on the distinguished coordinate and zero on the other for each \(D_j\).
The same parity decomposition of the marginal phase and its outer conjugate by \(s\) gives the corresponding starred values.
Only the even-even tensor contributes to the double trace on even inputs, hence \(D_0^*(1\otimes1)=\xi\).
Conjugating by \(s\) exchanges the derivations in the sense \(D_1=(\alpha\otimes\alpha)D_0\alpha\).
This follows on the full starred core by the generator values, including the phases just identified.
It gives the second actual vacuum \(\alpha\xi\).

For \(a\) even, tracing the second leg kills its odd-odd tensor.
For \(bs\), the product rule gives \((\delta b)\cdot s\), whose even-even contribution before right multiplication now has zero trace in the second leg.
An odd-odd tensor \(u\otimes v\) contributes \(u\tau(vs)\), which equals \((us\,\tau(sv))s\) by traciality.
This proves the first identity in (2).
Writing \(a_0\) for the single-input cost of \(E_0\), exchange gives the same cost for \(E_1\).
For \(\|x\|\le1\) the two Fourier coefficients are contractions by the formulas using \(\beta\).
Orthogonality therefore bounds \(\|Ex\|_2\) by \(\sqrt2\,a_0\).
More precisely, the even part of \(x^*x\) is \(a^*a+\alpha(b)^*\alpha(b)\le1\), so the same squared output equals the sum of squares of \(E_0\) on the two entries of a contractive column.
The restriction to the even core has cost exactly \(a_0\).
These facts and \(\xi=\xi_0\) give \(K_{\rm sign}\le\sqrt2 K_{\rm ex}\), as well as the stated finite-witness transfer by selecting the larger of the two component outputs.

### Realizing each exchange-symmetric pair

Conversely, take an exchange-symmetric actual pair and its exchanging involution \(\alpha\).
On its represented starred polynomial algebra, the normal phase formula gives \(D_1=(\alpha\otimes\alpha)D_0\alpha\) for the two distinguished derivations, including their adjoint-generator values.
Form \(M=Q\rtimes_\alpha\mathbb Z/2\) with normalized trace, and use \(s=s^*=s^{-1}\) for the group unitary.
Its sign automorphism \(\beta(a+bs)=a-bs\) fixes \(Z_0\), reverses \(s\), and preserves the trace.
The pair \(Z_0,P=(1+s)/2\) generates \(M\) since \(sZ_0s=Z_1\).

For even polynomial \(a\) put \(\Delta a=D_0a+I_{s\otimes s}D_1a\).
The second term is odd-odd and inner insertion commutes with the outer actions.
The exchange relation between \(D_0,D_1\) gives \(\Delta(\alpha a)=s\cdot(\Delta a)\cdot s\).
Indeed \(s\cdot (u\otimes v)\cdot s=I_{s\otimes s}(\alpha u\otimes\alpha v)\) for even tensors and the reverse identity holds after inner insertion.
Thus \(\Delta s=0\) and \(\Delta(a+bs)=\Delta a+(\Delta b)\cdot s\) respect \(s^2=1,\ sa=(\alpha a)s\).
Uniqueness of the two Fourier coefficients and the product rule on the even core give a represented derivation on \(\operatorname{alg}^*(Z_0,P)\).
It takes \(Z_0\) to \(1\otimes1\).
Its double trace on \(a+bs\) is the double trace of \(D_0a\), since each other term has an odd leg.
The vacuum is therefore \(\xi_0\) and the even restriction of the right slice is \(E_0\).
This proves \(K_{\rm ex}\le K_{\rm sign}\).

### The output outside the marginal

Let \(B=W^*(Z)\) in the projection model.
The sign automorphism fixes \(B\) pointwise and sends \(s\) to \(-s\), so \(\mathbb E_B n=\tau(n)1\) for \(n\in N\).
In particular \(L^2(B)\) and \(sL^2(B)\) are orthogonal, and \(U(n\otimes a)=na\) maps \(L^2(N)\otimes L^2(B)\) isometrically onto \(K\).
The [ordered two-block output estimate](Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) applies with both Gram constants one.
To check its use here, for \(n\in N\), \(a\) a marginal polynomial and \(x\) in the joint core, differentiate \(a^*n^*x\) in the vacuum identity.
As \(\delta n=0\), this gives \(\langle na,Ex\rangle=\langle na,x\xi^*\rangle-\langle nLa,x\rangle\) with \(L\) the conjugated scalar right slice \(JE_BJ\), where \(J\) denotes complex conjugation on the marginal.
The scalar adjoint bound \(\|L^*b\|_2\le\sqrt2\|b\sqrt w\|_2\) holds on the weighted marginal domain for the [integrable scalar weight](Yin_C_F0267_v1.md#statement) of mass \(\|\mathbb E_B\xi\|_2^2\), by weighted polynomial approximation as in the ordered-output estimate.
The isometry \(U\) intertwines right \(B\)-multiplication, and so does the projection onto \(K\).
Applying the scalar bound to the two components of \(U^{-1}\operatorname{proj}_K x\), with bounded truncations of \(\sqrt w\), bounds the norm of the functional from the last pairing by \(\sqrt2\|x\sqrt w\|_2\).
The first pairing costs at most \(\|x\xi^*\|_2\), giving (2).
For \(n f(Z)n'\), the derivative has terms \(n\cdot\delta f\cdot n'\) with \(\delta f\) in the marginal coarse space, so tracing the second leg puts the whole output in \(nL^2(B)\subseteq K\).
These arguments require only the distinguished actual vacuum and the zero derivative at the omitted projection.

For even \(a\), \(E_0a\) is even and its projection onto \(K\) equals \(\mathbb E_B E_0a\).
Applying this in the crossed product for any exchange pair and taking orthogonal squares gives the last bounds in (1).
The residual is zero on first-coordinate polynomials because their derivative is marginal, and on second-coordinate polynomials because their first derivative vanishes.
Combining (1) with the [universal characterization by the relative bound](Yin_C_F0308_v1.md#equivalence-to-the-general-comparison) proves the equivalence.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:44 |
| status | open |
| reason | Fix the exchange-symmetric reduction, the crossed-product slice identity and the quantitative mixed-output criterion for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Transfer of finite witnesses, comparison of four suprema, exact exchange symmetry and residual mixed output. |
| argument | [Argument](#argument) | Sign involution on the projection transfer, even and odd derivations, converse crossed product and uniform projected output estimate. |
| dependency | [Finite projection reduction](Yin_C_F0308_v1.md#argument) | Specific doubled matrix and noise construction, direct factor-two finite-witness bound and universal equivalence. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuseness and forced starred values on the relative and two-coordinate cores. |
| dependency | [Ordered output estimate](Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Vacuum pairing and weighted scalar adjoint argument with exact product Gram for the finite coefficient algebra. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Integrable positive marginal weight of vacuum mass and the complex scalar adjoint bound. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:49 |
| status | proved |
| reason | Adopt the exchange-symmetric reduction and estimate on the component in the marginal algebra after complete independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Transfer of finite witnesses, comparison of four suprema, exact exchange symmetry and residual mixed output. |
| argument | [Argument](#argument) | Sign involution on the projection transfer, even and odd derivations, converse crossed product and uniform projected output estimate. |
| dependency | [Finite projection reduction](Yin_C_F0308_v1.md#argument) | Specific doubled matrix and noise construction, direct factor-two finite-witness bound and universal equivalence. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuseness and forced starred values on the relative and two-coordinate cores. |
| dependency | [Ordered output estimate](Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Vacuum pairing and weighted scalar adjoint argument with exact product Gram for the finite coefficient algebra. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Integrable positive marginal weight of vacuum mass and the complex scalar adjoint bound. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0320_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
