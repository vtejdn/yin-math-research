---
author: Yin
---
# Sharp paired quadratic estimates for scalar rotational normal laws

Task: [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
Provenance: project deduction, developed by the scalar-test subagent for Yin on 2026-10-16 and fixed from the continuing exploration.
The initial registration retained a complete candidate argument for fresh independent review without accepting it as proved.
The [selected assessment](#current-assessment) records the subsequent adoption.
The statement sharpens the existing radial operator-norm bounds by proving the paired quadratic estimates and their optimal constants.

## Current assessment
[Selected decision](#decision-reviewed-quadratic)

## Statement

Let \(R>0\), and let \(\mu\) be a rotation-invariant Borel probability supported on the closed disk \(\{z:|z|\le R\}\).
Put
\[
 M=L^\infty(\mu),\qquad \tau(f)=\int f\,d\mu,\qquad
 H=L^2(\mu),\qquad X(z)=z,\qquad P=\mathbb C[X,X^*].
\]
The trace is faithful and normal, \(X\) is a bounded normal generator, and \(P\) is the represented unital star algebra.
All inner products are linear in the second variable.
The radius distribution is \(\nu=|\cdot|_*\mu\), initially a probability on \([0,R]\).

Condition A means that there exists a complex-linear outer derivation
\[
 \delta:P\subset H\longrightarrow H\otimes_2H,\qquad
 \delta X=1\otimes1,\qquad 1\otimes1\in\operatorname{Dom}\delta^*,
\]
where the last domain is the actual Hilbert adjoint domain.
The outer actions are \(a\cdot(u\otimes v)\cdot b=au\otimes vb\).
For \(r>0\), define
\[
 F_-(r)=\nu((0,r)),\quad F_+(r)=\nu((0,r]),\qquad
 q(r)=\frac{F_-(r)+F_+(r)}r.
\]
Set \(q(0)=0\) solely to define a measurable function on \([0,R]\); this convention does not remove the separate zero-atom condition below.

Then condition A holds if and only if
\[
 \nu(\{0\})=0,\qquad q\in L^2(\nu).
 \tag{S1}
\]
In particular zero mass at the origin is necessary, while positive-radius atoms are permitted.
Under (S1), \(\mu\) is nonatomic, the derivation is uniquely determined and equals
\[
 \delta f(z,w)=\frac{f(z)-f(w)}{z-w},\qquad
 \xi=\delta^*(1\otimes1),\qquad
 \xi(re^{i\theta})=e^{i\theta}q(r).
 \tag{S2}
\]
The diagonal is a product-null set.

For every \(a\in P\), the tensors \(a\otimes1\) and \(1\otimes a\) belong to \(\operatorname{Dom}\delta^*\), and
\[
 T_\ell(a)=\delta^*(a\otimes1)
 =\delta^*(1\otimes a)=T_r(a)=:T(a).
\]
The pairing below is real and nonnegative, and
\[
 \|Ta\|_2^2
 \le\langle T(|a|^2),\xi\rangle
 \le\|\xi\|_2\|T(|a|^2)\|_2.
 \tag{S3}
\]
Consequently both requested estimates
\[
 \|T_\ell(a)\|_2^2\le C_\ell\|T_\ell(a^*a)\|_2,\qquad
 \|T_r(a)\|_2^2\le C_r\|T_r(aa^*)\|_2
 \quad(a\in P)
\]
hold with the individually optimal constants
\[
 C_\ell=C_r=\|\xi\|_2>0.
 \tag{S4}
\]
No boundedness of these maps on the entire Hilbert space is assumed.

## Direct inputs and scope

| Direct proof input | Exact use |
| --- | --- |
| [C_F0076, Part 1](Yin_C_F0076_v1.md#statement), with its [selected proof](Yin_C_F0076_v1.md#decision-reviewed) | The full actual A condition for a bounded normal generator forces its spectral law to be nonatomic; this excludes a radius-zero atom in the necessity direction. No second-derivative or coassociativity assertion is used. |
| [C_F0047, Sections 2-6](Yin_C_F0047_v1.md#2-the-same-radius-calculation), with its [selected proof](Yin_C_F0047_v1.md#decision-candidate-0004) | Exact same-radius and unequal-radius Fourier formulas, actual midpoint vacuum criterion, the quantile Hardy estimate controlling the tail at zero, and the already established original bounded-function domains. |
| [C_F0055, Section 7](Yin_C_F0055_v1.md#7-actual-adjoints-and-original-graph-restoration), with its [selected proof](Yin_C_F0055_v1.md#decision-candidate-0002) | The actual scalar adjoint identity \(E_0^*a=a\xi-JE_0Ja\), applied on the represented starred core. Its pairing is also explained directly below. |

The [Mai15 norm-estimate audit](../audits/literature/Mai15/Yin_U002.md#mai15-u002) motivates the proposed paired estimates and the [power-iteration consumer](../drafts/Yin_D_F0002.md#the-power-iteration-mechanism-from-mai15-and-the-missing-quadratic-estimate).
Its real coassociative energy identity is not an input to this proof.
The additional argument is the elementary positive-kernel calculation below; no external theorem or novelty assertion is newly introduced.
The working origin D_F0017 records extraction ancestry, not an additional proof dependency.

Condition S and the canonical bounded-function domains were already known for this radial class from C_F0047.
The new assertion is the sharp quadratic estimate, including laws whose canonical contraction is unbounded on \(L^2\).
Neither arbitrary nonradial scalar laws nor correlated normal tuples are covered.

## Argument

### 1. Actual normal model and vacuum

First suppose the full actual condition A holds.
Part 1 of [C_F0076](Yin_C_F0076_v1.md#statement) applies with one normal generator and gives that its spectral law \(\mu\) is nonatomic.
In particular \(\mu(\{0\})=\nu(\{0\})=0\).
No claim about a diffuse radius distribution follows or is needed.

For a rotation-invariant Borel probability, averaging any bounded Borel test function over rotations gives the angular disintegration
\[
 \int g(z)\,d\mu(z)
 =\int_{[0,R]}\int_0^{2\pi}g(re^{i\theta})\,\frac{d\theta}{2\pi}\,d\nu(r).
\]
Indeed rotation invariance and Fubini preserve the left integral, and the averaged test depends only on the radius.
Thus, after the necessary exclusion of zero mass at the origin, \(\nu\) is a Borel probability on \((0,R]\) and

\[
 d\mu(re^{i\theta})=d\nu(r)\frac{d\theta}{2\pi},\qquad
 M=L^\infty(\mu),\quad \tau(f)=\int f\,d\mu,\quad H=L^2(\mu).
\]
The coordinate \(X(z)=z\) is bounded, normal and generates \(M\).
The measure \(\mu\) is nonatomic even when \(\nu\) has atoms.
The trace is faithful and normal.
Write \(P=\mathbb C[X,X^*]\), interpreted as the represented unital star algebra in \(M\).
It is dense in \(H\).

Define
\[
 F_-(r)=\nu((0,r)),\quad p(r)=\nu(\{r\}),\quad
 F_+(r)=F_-(r)+p(r),\quad
 q(r)=\frac{F_-(r)+F_+(r)}r.
 \tag{1}
\]
For the constructive direction, assume precisely \(q\in L^2(\nu)\).
For the necessary direction this integrability will follow from the actual vacuum criterion below.
There is no assumed lower bound for \(r\), no nonatomicity assumption on \(\nu\), and no Hilbert-space boundedness assumption on the operators below.

On \(P\), put
\[
 \delta f(z,w)=\frac{f(z)-f(w)}{z-w}.
 \tag{2}
\]
The diagonal has \(\mu^2\)-measure zero.
For each represented starred polynomial the quotient is bounded on the compact support, since the polynomial is Lipschitz on a surrounding compact rectangle.
The quotient depends only on the represented function, because changing that function on a null set changes the quotient only on the union of two product null sets.
The map is an outer derivation into \(H\otimes_2H\), and \(\delta X=1\otimes1\).
It is the unique outer derivation on this core with that generator value.
Indeed, differentiating \(XX^*=X^*X\) forces
\[
 (z-w)\delta(X^*)(z,w)=\bar z-\bar w.
\]
Since the collision diagonal is null, this determines \(\delta(X^*)\) almost everywhere; the Leibniz rule then determines the map on every starred polynomial.
Thus the ensuing statement applies to any actual condition-A derivation for this radial model, not merely to one chosen witness.

Let
\[
 E_0 f(z)=\int\delta f(z,w)\,d\mu(w).
\]
The exact vacuum computation of C_F0047 gives
\[
 \tau(E_0f)=\langle\xi,f\rangle,\qquad
 \xi(re^{i\theta})=e^{i\theta}q(r),\qquad f\in P,
 \tag{3}
\]
with inner products linear in the second variable.
This is the actual Hilbert-adjoint identity for \(\delta\), since
\(\langle1\otimes1,\delta f\rangle=\tau(E_0f)\).
Thus \(1\otimes1\in\operatorname{Dom}\delta^*\), \(\delta^*(1\otimes1)=\xi\), and \(\|\xi\|_2=\|q\|_{L^2(\nu)}\).
Conversely the existing C_F0047 criterion shows that any actual vacuum for this radial law requires \(q\in L^2(\nu)\) and has exactly (3).

The source's midpoint is \(m(r)=F_-(r)+p(r)/2\), so \(q=2m/r\).
In particular a radius atom contributes exactly \(p(r)/r\) to \(q\), not zero and not \(2p(r)/r\).
This includes the same-circle contribution in the actual divided difference, rather than interpreting its two singular summands separately.

The divided difference is invariant under swapping \(z,w\).
The actual adjoint formulas therefore give, for every \(a\in P\),
\[
 T_\ell(a)=\delta^*(a\otimes1)
 =\delta^*(1\otimes a)=T_r(a)=:T(a),
 \qquad
 T(a)=a\xi-JE_0Ja,\quad Ja=\overline a.
 \tag{4}
\]
All tensors in (4) belong to the actual adjoint domain.
For completeness, expanding \(\delta(\overline a f)\), applying (3), and exchanging the two variables proves the adjoint pairing directly.
It yields \(T(a)=E_0^*a\) on \(P\), with the indicated actual Hilbert adjoint.

C_F0047 already proves that the closure of \(E_0\) and the actual \(E_0^*\) contain every bounded function.
It also proves the operator-norm-to-\(L^2\) bounds needed for that graph conclusion.
These facts are used only as existing domain information, not as the proposed quadratic estimate.
In particular this proof does not replace the actual adjoint with an arbitrary extension.

### 2. Exact angular blocks

Write a starred polynomial as a finite angular sum
\[
 a(re^{i\theta})=\sum_{n\in\mathbb Z}f_n(r)e^{in\theta}.
\]
Its coefficients are bounded; in fact \(f_n(r)\) is \(r^{|n|}\) times a polynomial in \(r^2\).
By (4) and the exact C_F0047 Fourier formula,
\[
 T\bigl(f(r)e^{in\theta}\bigr)
  =e^{i(n+1)\theta}B_nf(r),
\]
where, for \(n\ge0\),
\[
 B_nf(r)=\frac{F_+(r)}r f(r)
       +r^{-n-1}\int_{s<r}s^n f(s)\,d\nu(s),
 \tag{5}
\]
and, for \(k\ge1\),
\[
 B_{-k}f(r)=\frac{F_-(r)}r f(r)
       -r^{k-1}\int_{s>r}s^{-k}f(s)\,d\nu(s).
 \tag{6}
\]
The inequalities in the integrals are strict.
The same-radius atom has already been incorporated into the diagonal coefficients \(F_+\) and \(F_-\).
This distinction is necessary for the negative-block calculation below.

For \(n=0\), (5) defines a positive operator on bounded radial functions and
\[
 B_0 1=q.
 \tag{7}
\]
For \(n\ge0\), the factor \((s/r)^n\) on \(s<r\) is at most one, so
\[
 |B_nf|\le B_0|f|.
\]
Pointwise Cauchy--Schwarz for the positive measure
\[
 \frac{F_+(r)}r\delta_r+\frac1r\,\nu|_{(0,r)}
\]
of total mass \(q(r)\) yields
\[
 |B_nf(r)|^2
 \le q(r)B_0(|f|^2)(r),\qquad n\ge0.
 \tag{8}
\]
The right-hand side is integrable for bounded \(f\), since
\(0\le B_0(|f|^2)\le \|f\|_\infty^2q\) and \(q\in L^2(\nu)\).

### 3. Negative angular blocks and their positive remainder

Fix \(k\ge1\), and first take bounded \(f\) vanishing on \((0,\varepsilon)\) for some \(\varepsilon>0\).
Set
\[
 d(r)=\frac{F_-(r)}r,\qquad
 A(r)=\frac{F_-(r)F_+(r)}{r^2},
\]
and
\[
 J_k(u)=\int_{t<u}\bigl(u^{2k-2}-t^{2k-2}\bigr)\,d\nu(t).
 \tag{9}
\]
For \(k=1\), \(J_1=0\).
For \(k\ge2\), Tonelli gives
\[
 J_k(u)=\int_0^u(2k-2)v^{2k-3}F_-(v)\,dv.
 \tag{10}
\]
Changing \(F_-\) at radius atoms has no effect on this Lebesgue integral.
Consequently \(J_k\) is nonnegative, continuous and nondecreasing, and \(J_k(0)=0\).

Expanding the square in (6), with every integral absolutely justified by the cutoff on \(f\), gives
\[
 \|B_{-k}f\|_2^2
 =\int A(r)|f(r)|^2\,d\nu(r)
  -\iint\overline{f(r)}f(s)
        \frac{J_k(\min(r,s))}{r^ks^k}\,d\nu(r)d\nu(s).
 \tag{11}
\]
Here is the complete accounting of the radius atoms.
For distinct \(r>s\), the off-diagonal coefficient in the expansion of \(\|B_{-k}f\|_2^2\), relative to \(\nu^2\), is
\[
 \frac1{r^ks^k}
 \left[\int_{t<s}t^{2k-2}\,d\nu(t)-F_-(s)s^{2k-2}\right]
 =-\frac{J_k(s)}{r^ks^k}.
 \tag{12}
\]
The diagonal multiplication from \(dI\) is \(d(r)^2\).
The square of the integral term contributes, at a radius atom \(r\), the additional coefficient
\[
 p(r)r^{-2k}\int_{t<r}t^{2k-2}\,d\nu(t).
\]
On the right side of (11), its diagonal coefficient is
\[
 A(r)-p(r)r^{-2k}J_k(r)
 =d(r)^2+p(r)r^{-2k}\int_{t<r}t^{2k-2}\,d\nu(t).
 \tag{13}
\]
Thus (11) includes all diagonal mass, including arbitrary atomic and mixed radius laws.

The subtracted form is nonnegative.
Indeed the elementary identity
\[
 J_k(\min(r,s))
   =\int_0^R{\bf1}_{u<r}{\bf1}_{u<s}\,dJ_k(u)
\]
gives
\[
 \iint\overline{f(r)}f(s)
        \frac{J_k(\min(r,s))}{r^ks^k}\,d\nu(r)d\nu(s)
 =\int_0^R
       \left|\int_{r>u}r^{-k}f(r)\,d\nu(r)\right|^2dJ_k(u)
 \ge0.
 \tag{14}
\]
The cutoff makes Fubini legitimate; \(J_k\) is bounded on \([0,R]\).
For \(k=1\), (11) is the exact identity
\[
 \|B_{-1}f\|_2^2=\int A|f|^2\,d\nu.
\]
For every \(k\ge1\) it follows that
\[
 \|B_{-k}f\|_2^2\le\int A|f|^2\,d\nu.
 \tag{15}
\]

To remove the cutoff, let \(f_\varepsilon=f{\bf1}_{[\varepsilon,R]}\) for any bounded radial \(f\).
The multiplication terms converge in \(L^2(\nu)\), since \(d\le q\in L^2(\nu)\).
For the integral terms, use
\[
 \left|r^{k-1}\int_{s>r}s^{-k}f_\varepsilon(s)\,d\nu(s)\right|
 \le \|f\|_\infty V(r),\qquad
 V(r):=\int_{s>r}\frac1s\,d\nu(s).
 \tag{16}
\]
The quantile Hardy estimate in C_F0047 proves \(V\in L^2(\nu)\) under the assumed \(q\in L^2(\nu)\).
More precisely its quantile tail majorizes this strict-radius tail, so its proved \(L^2\) estimate applies also when \(\nu\) has atoms.
The integrals converge pointwise for every \(r>0\).
Dominated convergence in (16) therefore gives \(B_{-k}f_\varepsilon\to B_{-k}f\) in \(L^2\).
Also \(A\le q^2\), so the right side of (15) converges.
Thus (15) holds for every bounded radial \(f\), including the actual polynomial coefficients.
No assertion about an entire-\(H\) domain was used in this limit.

Finally,
\[
 A(r)\le q(r)\frac{F_+(r)}r,\qquad
 B_0(|f|^2)(r)\ge\frac{F_+(r)}r|f(r)|^2,
\]
so (15) gives the same estimate as (8):
\[
 \|B_{-k}f\|_2^2
 \le\int q(r)B_0(|f|^2)(r)\,d\nu(r).
 \tag{17}
\]

### 4. Paired estimate, reality of the pairing and sharpness

The output angular frequencies in (5)--(6) are distinct, so Parseval and (8), (17) give
\[
 \|Ta\|_2^2
 \le \int q\,B_0\left(\sum_n|f_n|^2\right)d\nu.
 \tag{18}
\]
The zeroth angular coefficient of \(|a|^2\) is
\(b_0(r)=\sum_n|f_n(r)|^2\).
Since \(\xi=e^{i\theta}q\), only the output angular frequency \(1\) contributes to the pairing with \(\xi\).
Hence (18) becomes the actual estimate
\[
 \boxed{\quad
 \|Ta\|_2^2\le
 \langle T(|a|^2),\xi\rangle
 \le\|\xi\|_2\,\|T(|a|^2)\|_2,\qquad a\in P.
 \quad}
 \tag{19}
\]
The middle pairing is real and nonnegative: it equals the displayed integral in (18), with \(q\ge0\), \(b_0\ge0\), and \(B_0\) positive.
Thus no real-part convention or reality assumption on \(\delta\) is being suppressed.
In the commutative algebra, \(a^*a=aa^*=|a|^2\), and \(T_\ell=T_r=T\).
Equation (19) therefore proves both requested estimates with
\[
 C_\ell=C_r=\|\xi\|_2.
 \tag{20}
\]

These constants are sharp for this fixed law.
Taking \(a=1\) gives \(T1=\xi\), so any admissible constant \(C\) satisfies
\(\|\xi\|_2^2\le C\|\xi\|_2\).
The vector \(\xi\) is nonzero because
\(\langle\xi,X\rangle=\langle1\otimes1,\delta X\rangle=1\).
Therefore \(C\ge\|\xi\|_2\).

For a single Haar circle of radius \(r\), (5)--(6) reduce to
\[
 T=r^{-1}e^{i\theta}P_{\{n\ge0\}},\qquad
 \xi=r^{-1}e^{i\theta}.
\]
This directly confirms (19) and its sharp constant.

For the accepted countable-circle family of C_F0047, take
\[
 r_j=2^{-j},\qquad p_j=(1-s)s^{j-1},\qquad
 s=2^{-\beta},\quad 2/3<\beta<1.
\]
The actual vacuum satisfies
\[
 \|\xi\|_2^2
 =\frac{4(1-s)(1+s)^2}{1-4s^3}<\infty.
\]
The canonical contraction is unbounded on \(L^2(\mu)\), as already proved in that Claim, but (19) still holds sharply.
Thus Hilbert-space unboundedness does not obstruct the paired quadratic route.


## Review boundary

The candidate argument includes the full actual-A criterion, zero-atom exclusion, all radius-atom diagonal coefficients, the cutoff passage at zero, and the sharp constants.
At the original candidate checkpoint, the positive kernel calculation and its interaction with the actual Fourier blocks required fresh independent review before acceptance.
No Task completion, general A-to-S implication, source-priority claim or theorem role is selected.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:07 |
| status | open |
| reason | Fix the complete radial candidate with actual vacuum/domain interfaces, strict-radius atomic bookkeeping, positive negative-mode remainder, the zero-radius cutoff and optimal paired constants; fresh independent review remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The exact rotational actual-A criterion, unique divided difference, actual one-sided adjoints, strengthened scalar pairing estimate and individually optimal constants. |
| argument | [Argument](#argument) | All four proof sections, including zero-mass necessity, actual vacuum equivalence, atomic Fourier blocks, positive kernel remainder, zero-endpoint limit, sharpness and the Hilbert-unbounded example. |
| dependency | [Normal diffuseness](Yin_C_F0076_v1.md#statement) | Part 1 only, applied to the full actual one-generator A premise to exclude a spectral atom at zero. |
| dependency | [Arbitrary-radius Fourier and vacuum theorem](Yin_C_F0047_v1.md#yin_c_f0047) | Sections 2-6 supply the actual radial Fourier/vacuum/Hardy/domain interfaces; Section 7 supplies the already accepted Hilbert-unbounded countable-circle example. |
| dependency | [Actual scalar adjoint](Yin_C_F0055_v1.md#7-actual-adjoints-and-original-graph-restoration) | The actual core identity for \(E_0^*\); no general mixed-word bound is imported. |

### Decision reviewed-quadratic

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:23 |
| status | proved |
| reason | Adopt the complete quadratic-estimate statement and argument after the separately organized full-proof review; retain its precise coordinate or radial scope and all actual-domain requirements. The unrestricted normal A-to-S problem remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fixed statement, hypotheses and quantitative conclusions. |
| argument | [Argument](#argument) | Complete fixed argument and its exact direct-input applications. |
| dependency | [Normal diffuseness](Yin_C_F0076_v1.md#statement) | Part 1 only, applied to the full actual one-generator A premise to exclude a spectral atom at zero. |
| dependency | [Arbitrary-radius Fourier and vacuum theorem](Yin_C_F0047_v1.md#yin_c_f0047) | Sections 2-6 supply the actual radial Fourier/vacuum/Hardy/domain interfaces; Section 7 supplies the already accepted Hilbert-unbounded countable-circle example. |
| dependency | [Actual scalar adjoint](Yin_C_F0055_v1.md#7-actual-adjoints-and-original-graph-restoration) | The actual core identity for \(E_0^*\); no general mixed-word bound is imported. |
| review | [Independent full-proof review](../audits/reviews/Yin_R_F0166_v1.md#conclusion) | Exact statement, complete argument and declared direct dependencies at the scopes retained in the review bindings. |

