---
author: Yin
---
# Bounded coefficient mass, polynomial localization and positive spectral mass

This argument studies the amenable branch of [A0001](../tasks/Yin_T_A0001_v1.md#contract) through scalar spectral approximation and spatial summability.
It uses the established absence of nontrivial idempotents in \(\ell^1(G)\) for torsion-free amenable \(G\), rather than assuming the desired scalar injectivity.
The Christoffel variational principle and moment-matrix formula are classical inputs attributed to [Sim08](../audits/literature/Sim08/Yin_U001.md).
The deductions below combine their precise scalar approximation with finite propagation and the \(\ell^1\) obstruction.
They give sufficient analytic conditions and necessary quantitative restrictions, without asserting a general amenable solution or new group-class coverage.
This revision retains the [first version's](../claims/Yin_C_A0014_v1.md) polynomial estimates and adds a weaker bounded-coefficient-mass criterion.
It also identifies the stronger spectral-gap consequence of the original summable-increment condition.
The new criterion requires no norm convergence of the approximants and supplies the atom-specific target of this revision.

## Statement

Let \(G\) be a finitely generated torsion-free amenable group with a fixed finite symmetric generating set, word balls \(B_R\), and \(V(R)=|B_R|\).
Let \(0\ne a\in\mathbb CG\), put \(H=a^*a\), \(M=\|H\|>0\), and choose an integer \(w\ge1\) with \(\operatorname{supp}H\subset B_w\).
Let \(\mu\) be the probability spectral measure of \(H\) for the canonical trace, supported in \([0,M]\).
Write \(p=1_{\{0\}}(H)\) and \(\alpha=\tau(p)=\mu(\{0\})<1\).
The Cauchy convention \(G_\mu(z)=\int(z-x)^{-1}\,d\mu(x)\) gives
\[
\alpha=\lim_{\eta\downarrow0}i\eta G_\mu(i\eta).
\]

### Definition: Christoffel minima at the target point

For a compactly supported probability measure \(\mu\) on \(\mathbb R\), a real point \(x_0\), and \(n\ge0\), define
\[
\lambda_n^\mu(x_0)=
\min\left\{\int |f(x)|^2\,d\mu(x):
f\in\mathbb C[x],\ \deg f\le n,\ f(x_0)=1\right\}.
\tag{1}
\]
This is the Christoffel function with degree bound \(n\), so the associated moment matrix has size \(n+1\).
The minimum exists even when the moment matrix is singular: it is the minimum norm in the finite-dimensional image of the displayed affine polynomial space in \(L^2(\mu)\).
Its minimizing \(L^2(\mu)\) vector is unique, although the polynomial representative need not be.
In the present application set \(x_0=0\), write \(\lambda_n=\lambda_n^\mu(0)\), and choose any minimizing representative \(f_n\).
The source's nonsingular formula will be used only when its actual positive-definiteness hypothesis holds.

### Bounded coefficient mass suffices without norm convergence

Suppose \(u_j\in\ell^1(G)\), in its regular representation, converges to \(p\) in \(L^2(\tau)\), and
\[
\liminf_{j\to\infty}\|u_j\|_{\ell^1(G)}<\infty.
\tag{1a}
\]
Then \(p\in\ell^1(G)\), hence \(p=0\).
In particular either of the explicit conditions
\[
\liminf_{n\to\infty}\|f_n(H)\|_{\ell^1(G)}<\infty,
\qquad
\liminf_{n\to\infty}\|(1-H/M)^n\|_{\ell^1(G)}<\infty
\tag{1b}
\]
implies injectivity of \(a\).
Each norm in (1b) is a finite sum of absolute values of group-word coefficients; these conditions contain no unknown atom mass.
The second is a bounded-total-variation subsequence condition for convolution powers of the finite complex measure \(1-H/M\).
No positivity or probability normalization of that complex measure is assumed.
Another sufficient condition is
\[
\liminf_{t\to\infty}\|e^{-tH}\|_{\ell^1(G)}<\infty.
\tag{1c}
\]
The heat element belongs to \(\ell^1(G)\) for each fixed \(t\), by its absolutely convergent exponential series.
Consequently a hypothetical nonzero kernel forces every norm in (1b), and the norm in (1c), to tend to infinity.
These are necessary growth obstructions to a counterexample, not bounds derived here from amenability.

Condition (1a) only controls a subsequence and does not assert convergence in \(\ell^1\), uniform spatial tails or an operator-norm approximation to \(p\).
Thus its proof does not exclude positive spectrum accumulating at zero.
By contrast, the summable-increment condition below excludes zero from the entire spectrum.

### A moment-increment criterion with no unknown atom in its hypothesis

For \(m>n\),
\[
\|f_m(H)-f_n(H)\|_2^2=\lambda_n-\lambda_m,
\qquad
\lambda_n\downarrow\alpha.
\tag{2}
\]
Here \(\|T\|_2^2=\tau(T^*T)\).
If
\[
\sum_{j=0}^{\infty}
\sqrt{V(2^{j+1}w)}
\sqrt{\lambda_{2^j}-\lambda_{2^{j+1}}}
<\infty,
\tag{3}
\]
then \(p\in\ell^1(G)\), hence \(p=0\) and \(a\) acts injectively on \(\ell^2(G)\).
In fact (3) implies \(0\notin\sigma(H)\).
Every summand in (3) is determined by finite group-word moments and a finite ball size.
Convergence of the entire series is an infinite condition, requiring an additional tail estimate; this is not a finite-step decision procedure.

If \(\mu\) has infinite support, then
\[
\mathsf M_n=\bigl(\tau(H^{i+j})\bigr)_{i,j=0}^n>0,\qquad
\lambda_n=\frac{1}{e_0^*\mathsf M_n^{-1}e_0},
\tag{4}
\]
and the coefficient column of \(f_n\) is
\[
\frac{\mathsf M_n^{-1}e_0}{e_0^*\mathsf M_n^{-1}e_0}.
\]
If \(\mu\) has finite support, the kernel projection is already a polynomial in \(H\), so it is zero under the present nonzero-element and group hypotheses.
Thus no inverse of a singular moment matrix is needed to handle that case.

### A positive-spectrum lower bound at every polynomial scale

For \(m\ge2\), let
\[
F_m(x)=\frac1{m^2}
\left[m+2\sum_{r=1}^{m-1}(m-r)T_r(1-2x/M)\right],
\tag{5}
\]
where \(T_r(\cos\theta)=\cos(r\theta)\) is the Chebyshev polynomial.
For an integer \(k\ge1\), put \(N=k(m-1)\) and \(q=F_m(H)^k\).
If \(0\in\sigma(H)\), then
\[
\|q^2-q\|_{\ell^1(G)}\ge\frac14,
\tag{6}
\]
and consequently
\[
\int_{(0,M]}
\left[F_m(x)^k\bigl(1-F_m(x)^k\bigr)\right]^2\,d\mu(x)
\ge \frac1{16V(2Nw)}.
\tag{7}
\]
This bound concerns the positive spectral part; the integrand vanishes at the atom.
It holds whether zero is an eigenvalue or only belongs to the continuous spectrum, and must not be presented as an atom-specific contradiction.
The left side is also determined by finitely many moments.

### Rate consequences and their scope

Suppose \(V(R)\le C_0(1+R)^D\) and
\[
\mu((0,\varepsilon])\le C_1\varepsilon^\beta
\quad(0<\varepsilon\le M),\qquad \beta>D/2.
\tag{8}
\]
Then (3) holds, so \(a\) is injective.
In fact, (7) shows under (8) that \(0\notin\sigma(H)\), a stronger conclusion.
This is a conditional analytic certificate, not a new Atiyah result for groups of polynomial growth.
There is also a critical necessary restriction: if \(D>0\), \(V(R)\le C_0(1+R)^D\), and \(0\in\sigma(H)\), then
\[
\limsup_{\varepsilon\downarrow0}
\frac{\mu((0,\varepsilon])}{\varepsilon^{D/2}}>0.
\tag{8a}
\]
Thus even a little-oh improvement at the critical exponent is excluded.

More generally suppose
\[
V(R)\le C_0\exp(C_1R^\kappa),\quad 0<\kappa<1,
\qquad
\mu((0,\varepsilon])\le C_2\exp(-c\varepsilon^{-\beta})
\tag{9}
\]
for sufficiently small positive \(\varepsilon\), with \(\beta>0\).
If
\[
\kappa<\frac{2\beta}{2\beta+1},
\tag{10}
\]
then (3) again holds and \(0\notin\sigma(H)\).
Neither (8) nor (9) is proved for arbitrary group-ring inputs.
The power-rate test does not cover exponential word growth, and (10) requires a strict comparison of the stated exponents.

## Current assessment

[Selected decision](#decision-reviewed-bounded-mass)

## Assessment history

### Decision reviewed-bounded-mass

| Field | Value |
| --- | --- |
| date | 2026-11-12T13:18 |
| status | proved |
| reason | The bounded coefficient-mass criteria, exact polynomial identities, positive-spectrum lower bounds and rate consequences have passed independent review under their stated hypotheses; the required all-input coefficient bounds and the general amenable conjecture remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete v2 assertions, including bounded subsequences, the heat criterion, spectral exclusion under summable increments and the critical positive-spectrum restriction. |
| argument | [Complete argument](#argument) | Coefficient limits, actual projection identification, finite propagation, moment minimization, Banach rounding and all stated rate estimates. |
| review | [Whole-v2 finding](../audits/reviews/Yin_R_A0041_v2.md#whole-argument) | Independent whole-v2 review, with unchanged v1 checks reused only at their confirmed scopes and every added implication freshly checked. |
| dependency | [BCM04 scalar-idempotent interface](../audits/literature/BCM04/Yin_U001.md#bcm04-u001) | No nontrivial scalar idempotents in the complex Banach group algebra of a torsion-free amenable group; established source theorem at its inspected statement and applicability scope. |
| dependency | [Sim08 variational interface](../audits/literature/Sim08/Yin_U001.md#sim08-u001) | Classical Christoffel convention, nonsingular inverse-moment formula and compact-support atom limit; the local argument supplies its own finite-support and endpoint justifications. |

The [first version](Yin_C_A0014_v1.md) and its [review](../audits/reviews/Yin_R_A0041_v1.md#whole-argument) retain their exact earlier scope.
This decision selects the weaker bounded-mass interface as well as the stronger polynomial estimates; it supplies no unconditional boundedness theorem.

## Argument

### The exact external idempotent input

The [BCM04 trace interface](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace) records Theorems 1.3 and 1.4, Lemma 1.5 and Proposition 6.1.
For torsion-free amenable groups these give that the Kaplansky trace on \(K_0(\ell^1(G))\) equals augmentation and is integer valued.
In particular \(\ell^1(G)\) has no idempotents other than \(0\) and \(1\).
The scalar assertion follows either directly from Proposition 6.1 or from faithful trace on its regular operator realization.
It does not assert that all nonzero elements of \(\mathbb CG\) are injective.
The original assembly-theoretic proof remains an established external input at the scope recorded in the source unit.

### Variational identities and spatial convergence

A minimizer \(f_m\) is orthogonal in \(L^2(\mu)\) to every polynomial of degree at most \(m\) vanishing at zero.
For \(m>n\), this applies to \(f_n-f_m\), giving the Pythagorean identity
\[
\lambda_n=\lambda_m+\|f_n-f_m\|_{L^2(\mu)}^2.
\]
Every admissible polynomial contributes exactly \(\alpha\) at zero, so \(\lambda_n\ge\alpha\).
The trial polynomial \((1-x/M)^n\) has value one at zero and converges pointwise to zero on \((0,M]\), with absolute value at most one.
Dominated convergence therefore gives \(\lambda_n\downarrow\alpha\).
Since \(f_n(0)=1\), functional calculus also gives the exact approximation error
\[
\|f_n(H)-p\|_2^2=\lambda_n-\alpha.
\tag{11}
\]

To prove (1a), pass to a subsequence on which \(\|u_j\|_{\ell^1}\le C\).
The \(L^2\) convergence makes every Fourier coefficient converge to the corresponding coefficient of \(p\).
For every finite \(E\subset G\), it follows that
\[
\sum_{g\in E}|p(g)|=\lim_j\sum_{g\in E}|u_j(g)|\le C.
\]
Taking the supremum over finite sets gives an element of \(\ell^1(G)\) with exactly the Fourier coefficients of \(p\).
Faithfulness and commutation with right translations identify its regular representation with \(p\).
The BCM04 scalar-idempotent input gives \(p=0\), since \(a\ne0\).
Equation (11) supplies the first choice in (1b).
For the second, the polynomials \((1-x/M)^n\) converge pointwise to \(1_{\{0\}}(x)\) on \([0,M]\), with absolute value at most one.
The same dominated-convergence argument applies to \(e^{-tx}\) and proves (1c).
If any of these nonnegative norms failed to tend to infinity when \(p\ne0\), it would have a bounded subsequence, contradicting the just-proved criterion.
The proof permits coefficient mass to escape to arbitrarily distant group elements; it never upgrades coefficient convergence to norm convergence.

A polynomial in \(H\) of degree at most \(r\) is supported in \(B_{rw}\).
For every group-ring element \(b\) supported there, coefficient Cauchy--Schwarz gives
\[
\|b\|_{\ell^1(G)}\le\sqrt{V(rw)}\,\|b\|_2.
\tag{12}
\]
Apply this to \(f_{2^{j+1}}(H)-f_{2^j}(H)\).
Equations (2) and (3) make the sequence \(f_{2^j}(H)\) Cauchy in the Banach algebra \(\ell^1(G)\).
Its \(\ell^1\) limit has the same \(\ell^2\) Fourier coefficients as \(p\), by (11).
The regular representation is faithful, and equality on \(\delta_e\) gives equality on its right translates, so this limit is the bounded operator \(p\).
It is an idempotent in \(\ell^1(G)\).
The external scalar-idempotent result gives \(p\in\{0,1\}\).
The possibility \(p=1\) would give \(H=0\), contrary to \(a\ne0\), hence \(p=0\).
Under (3) the convergence is in \(\ell^1\) norm, and hence in operator norm.
If \(0\in\sigma(H)\), every polynomial \(f_{2^j}\) has value one at that spectral point, so \(\|f_{2^j}(H)\|\ge1\).
This contradicts norm convergence to \(p=0\), proving the stronger spectral exclusion stated after (3).

For infinite support, a nonzero polynomial cannot vanish \(\mu\)-almost everywhere, so the moment matrix in (4) is positive definite.
Minimizing \(c^*\mathsf M_nc\) under \(e_0^*c=1\) gives (4) by finite-dimensional quadratic minimization.
This is the [classical Christoffel and inverse-moment formula](../audits/literature/Sim08/Yin_U001.md).
For finite support, polynomial interpolation on the finite spectral set gives \(p=r(H)\in\mathbb CG\), so the same idempotent input already gives \(p=0\).

### A Banach-algebra rounding obstruction

Let \(q=q^*\in\mathbb CG\) have \(0\le q\le1\) as an operator.
Suppose \(\|q^2-q\|_{\ell^1}<1/4\), and put \(d=q^2-q\).
The binomial series
\[
s=(1+4d)^{-1/2}
\]
converges absolutely in \(\ell^1(G)\), since \(\|4d\|_{\ell^1}<1\).
Because \(s\) commutes with \(q\) and \((2q-1)^2=1+4d\), the element
\[
e=\frac12+\left(q-\frac12\right)s
\tag{13}
\]
is an idempotent in \(\ell^1(G)\).
In the regular representation the same series is the positive inverse square root of \((2q-1)^2\), so \(e\) is the spectral projection of \(q\) above \(1/2\).
If the spectrum of \(q\) contains a value below \(1/2\) and a value above \(1/2\), that projection is neither zero nor one, contrary to BCM04.
Thus such a \(q\) must have \(\ell^1\) defect at least \(1/4\).
This proof uses only the stated Banach norm and functional calculus; no gap for the original \(H\) and no projection integrality theorem for the reduced group \(C^*\)-algebra is required.

Set \(x=M\sin^2(\theta/2)\) for \(0\le\theta\le\pi\).
The finite Fourier identity for (5) gives
\[
F_m(x)=\left[\frac{\sin(m\theta/2)}{m\sin(\theta/2)}\right]^2,
\qquad
F_m(0)=1,\qquad
0\le F_m(x)\le\min\left(1,\frac{M}{m^2x}\right).
\tag{14}
\]
At \(x=M\), its value is zero for even \(m\) and \(1/m^2\) for odd \(m\).
Thus \(F_m(M)^k<1/2\) for all \(m\ge2\), \(k\ge1\).
If \(0\in\sigma(H)\), then \(M\in\sigma(H)\) as well and spectral mapping puts both \(1\) and a value below \(1/2\) in \(\sigma(q)\).
Equation (13) proves (6).
The defect is supported in \(B_{2Nw}\), so (12) gives
\[
\frac1{16}
\le \|q^2-q\|_{\ell^1}^2
\le V(2Nw)\,\tau\bigl((q^2-q)^2\bigr).
\]
Functional calculus identifies the last trace with the integral in (7), proving that bound.

### Power rates

Assume (8), fix an integer \(k>\beta/2\), and set \(f=F_m^k\).
On \((0,M/m^2]\), its squared absolute value is at most one.
On the successive intervals
\([2^jM/m^2,2^{j+1}M/m^2]\cap(0,M]\), it is at most \(2^{-2kj}\).
The distribution bound therefore gives
\[
\int_{(0,M]} |f(x)|^2\,d\mu(x)
\le C\left(\frac{M}{m^2}\right)^\beta
\left(1+2^\beta\sum_{j\ge0}2^{j(\beta-2k)}\right)
\le C' m^{-2\beta}.
\tag{15}
\]
For a given sufficiently large degree bound \(n\), choose \(m=\lfloor n/k\rfloor+1\).
Then \(\deg f=k(m-1)\le n\), and (15) yields
\[
0\le\lambda_n-\alpha\le C''n^{-2\beta}.
\]
Thus each dyadic summand in (3) is bounded by a constant times \(2^{j(D/2-\beta)}\), proving convergence.

For the stronger spectral assertion, suppose \(0\in\sigma(H)\).
Since \(0\le f\le1\),
\(\int f^2(1-f)^2\,d\mu\le\int_{(0,M]}f^2\,d\mu\).
Equation (7) lower bounds the former by a positive constant times \(m^{-D}\), whereas (15) upper bounds it by \(C'm^{-2\beta}\).
The inequality \(2\beta>D\) is a contradiction for large \(m\).
Hence zero is absent from the spectrum.

To prove (8a), suppose instead that the positive spectral distribution is \(o(\varepsilon^{D/2})\), and fix an integer \(k>D/4\).
For any \(\eta>0\), choose \(\varepsilon_0>0\) so that its distribution below \(\varepsilon_0\) is at most \(\eta\varepsilon^{D/2}\).
The same dyadic estimate below that threshold bounds the filtered integral by \(C\eta m^{-D}\).
For the interval whose upper endpoint first exceeds \(\varepsilon_0\), use the distribution bound at \(\varepsilon_0\); its contribution has the same estimate.
Above \(\varepsilon_0\), (14) bounds the remaining integral by \(C_{\varepsilon_0}m^{-4k}\).
Multiplying by \(m^D\), letting \(m\to\infty\), and then letting \(\eta\downarrow0\) shows that the integral in (7) is \(o(m^{-D})\).
This contradicts (7) and proves (8a).

### Stretched exponential rates

Assume (9) and put \(\theta=2\beta/(2\beta+1)\).
For large \(n\), choose integers \(k\asymp n^\theta\) and \(m\asymp n^{1-\theta}\), with \(k(m-1)\le n\).
Set \(\varepsilon=4M/m^2\).
On \([\varepsilon,M]\), (14) gives \(F_m^{2k}\le16^{-k}\).
On \((0,\varepsilon]\), it is at most one.
Consequently
\[
0\le\lambda_n-\alpha
\le C_2\exp(-c\varepsilon^{-\beta})+16^{-k}
\le C_3\exp(-c_3 n^\theta).
\tag{16}
\]
The constants may change when the hypothesis is initially restricted to sufficiently small \(\varepsilon\).
The dyadic terms in (3) are at most
\[
C_4\exp(C_4 2^{j\kappa}-c_4 2^{j\theta}),
\]
which are summable under (10).
If zero belonged to the spectrum, the lower bound (7) would be at least a positive constant times \(\exp(-C_5 n^\kappa)\), contradicting (16) for the same filters.
This also proves the asserted spectral exclusion.

## What has and has not been reduced

The scalar Cauchy residue is subjected to a spatial summability test built from optimal polynomial approximants and exact finite-word moments.
Condition (3) does not contain the unknown residue, and the positive-spectrum estimate (7) does not receive any contribution from it.
The bounded-mass conditions (1a)–(1c) use coefficient convergence instead of norm convergence and give a weaker sufficient route that does not require a spectral gap.
These are additional quantitative analytic constraints, not the already-known amenable equivalence between Atiyah integrality and the group-ring domain problem.
They remain conditional or necessary statements: no general bound making (3) converge is derived from amenability alone.
Condition (3) itself, as well as its stated rate consequences, is strong enough to exclude zero from the whole spectrum and therefore does not handle every analytically injective operator with continuous spectrum at zero.
The more appropriate atom-only target is bounded coefficient mass for an actual specified approximating sequence, or another independently proved way to put the kernel projection in \(\ell^1(G)\).
No such bound for every nonzero torsion-free amenable group-ring element has been proved here.
No converse, optimal threshold, new group class, historical novelty claim or complete solution of A0001 is asserted.
