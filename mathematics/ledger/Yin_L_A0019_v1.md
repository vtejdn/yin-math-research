---
author: Yin
---
# Central winding and the disappearance of torsion-quotient atoms

Date: 2026-11-12 (Asia/Hong_Kong).
This bounded investigation serves [S_A0007](../strategies/Yin_S_A0007.md) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
It tests a concrete joint-word constraint beyond cyclic root closure: the exact central winding shared by two generator powers, with the canonical trace recovered by Haar integration in that winding variable.
For the selected scalar family over an actual torsion-free central amalgam, fractional atoms of its torsion quotient occur only in exceptional central fibers and do not survive in the original group law.
The scalar atomlessness conclusion is already covered by the retained height mechanism; the value of the calculation is its exact joint-trace interface and its obstruction to transferring quotient atoms or setting the winding variable to one.
No new Atiyah group class, general matrix theorem or historical priority is claimed.

## The actual group and the winding coordinate

Let
\[
G_{p,q}=\langle a,b\mid a^p=b^q\rangle,\qquad p,q\ge2,\qquad z=a^p=b^q,
\]
and let \(Q=C_p*C_q=\langle s,t\mid s^p=t^q=1\rangle\).
The element \(z\) is central, since it commutes with both generators.
If \(d=\gcd(p,q)\), the homomorphism
\[
\phi:G_{p,q}\longrightarrow\mathbb Z,\qquad
\phi(a)=q/d,\quad\phi(b)=p/d
\tag{1}
\]
is well defined, and \(\phi(z)=pq/d\ne0\).
Thus \(z,a,b\) have infinite order.

Every word can be rewritten as \(z^m v\), where \(m\in\mathbb Z\) and \(v\) is an alternating sequence of syllables \(a^r\), \(1\le r<p\), and \(b^s\), \(1\le s<q\).
Extract multiples of \(p\) and \(q\) from each power and move them into the central factor, then combine adjacent syllables of the same type.
The quotient by \(z=1\) is exactly \(Q\).
Its reduced free-product words determine \(v\) uniquely.
For equal \(v\), equality of two powers of \(z\) forces equality of their exponents by (1).
In particular, the kernel of the quotient map \(G_{p,q}\to Q\) is exactly \(\langle z\rangle\).
This is the central normal form used in [AER26, Lemma 3.1, Corollary 3.2 and Section 3.1](https://arxiv.org/html/2605.12793v1#S3).
The preceding direct argument specifies the quotient and uniqueness needed here.

For completeness, \(G_{p,q}\) is torsion-free.
A finite-order element in \(Q\) is conjugate into one cyclic factor: cyclically reduce its alternating normal form, and observe that a cyclically reduced word of length at least two has nontrivial reduced positive powers.
Lift the conjugator to \(G_{p,q}\).
An element of \(G_{p,q}\) with finite-order image is consequently conjugate to \(a^r z^m\) or \(b^s z^m\).
These are powers of \(a\) or \(b\), respectively, and a finite-order such power must be the identity by (1).
This also handles the case of trivial quotient image.

## A full joint trace identity, not just a scalar moment fit

Write \(\tau_Q\) for the canonical trace of \(\mathcal N(Q)\), and use its group generators \(s,t\) as unitaries.
For \(0\le\theta<2\pi\), define a unitary representation of the presented group by
\[
\rho_\theta(a)=e^{i\theta/p}s,\qquad
\rho_\theta(b)=e^{i\theta/q}t,\qquad
\rho_\theta(z)=e^{i\theta}1.
\tag{2}
\]
Both defining powers equal \(e^{i\theta}1\), so the actual relation is respected.
For a normal form \(z^m v\), its \(\tau_Q\)-value under \(\rho_\theta\) is zero when \(v\) is nonempty, and equals \(e^{im\theta}\) when \(v\) is empty.
Therefore, for every group-ring element \(x\), including every noncommutative word in generators and their inverses,
\[
\boxed{\tau_G(x)=\frac1{2\pi}\int_0^{2\pi}
          \tau_Q(\rho_\theta(x))\,d\theta.}
\tag{3}
\]
The equality is a coefficient calculation on the full group ring, not a finite set of scalar return moments.
Each integrand is a positive tracial state coming from a unitary representation of the same presented group.
The integral recovers the canonical trace, not an arbitrarily chosen trace on an abstract torsion-free group.
The separate branches in (2) need only be measurable on the chosen interval.
Changing \(\theta\) by \(2\pi\) rotates the cyclic generators by characters and leaves the scalar distributions unchanged.

Let \(X=X^*\in\mathbb CG_{p,q}\), and write \(X_\theta=\rho_\theta(X)\).
All \(X_\theta\) have a common norm bound supplied by the sum of the absolute values of the finitely many group-ring coefficients.
Applying (3) to every power of \(X\), then using uniform polynomial approximation on that common compact real interval, gives
\[
\mu_X=\frac1{2\pi}\int_0^{2\pi}\mu_{X_\theta}\,d\theta.
\tag{4}
\]
Thus the scalar Cauchy transform identity holds throughout the upper half-plane.
For every fixed \(\lambda\in\mathbb R\), apply (4) to the positive bounded functions
\[
h_{\eta,\lambda}(x)=\frac{\eta^2}{(x-\lambda)^2+\eta^2},
\qquad 0\le h_{\eta,\lambda}\le1.
\]
Dominated convergence gives the exact boundary-atom formula
\[
\boxed{\mu_X(\{\lambda\})=
\frac1{2\pi}\int_0^{2\pi}
        \mu_{X_\theta}(\{\lambda\})\,d\theta.}
\tag{5}
\]
No uniform small-singular-value rate, spectral gap, meromorphic continuation or interchange of an uncontrolled asymptotic series is assumed.
In particular, the return-series germ is not evaluated outside its convergence disk.

## Independent atom exclusion from the winding fibers

Consider the actual finite group-ring element
\[
X=c\,a+\bar c\,a^{-1}+d_0\,b+\bar d_0\,b^{-1},
\qquad c,d_0\in\mathbb C\setminus\{0\}.
\tag{6}
\]
The symbol \(d_0\) denotes a coefficient and is unrelated to the greatest common divisor in (1).
Its two fiber summands belong to the freely independent cyclic factor algebras of \(\mathcal N(C_p*C_q)\).
Their laws are
\[
\mu_{a,\theta}=\frac1p\sum_{j=0}^{p-1}
 \delta_{\,2\operatorname{Re}(c e^{i(\theta+2\pi j)/p})},
\qquad
\mu_{b,\theta}=\frac1q\sum_{k=0}^{q-1}
 \delta_{\,2\operatorname{Re}(d_0 e^{i(\theta+2\pi k)/q})},
\tag{7}
\]
and
\[
\mu_{X_\theta}=\mu_{a,\theta}\boxplus\mu_{b,\theta}.
\]
The cyclic factor algebras are free for the canonical trace because every alternating product of centered elements expands into nonempty reduced words of \(Q\).

For almost every \(\theta\), the \(p\) displayed locations in the first marginal are distinct, as are the \(q\) locations in the second.
To check this explicitly, write \(c=|c|e^{i\beta}\).
For two distinct residues \(j,l\bmod p\), equality of their cosine values cannot come from equal arguments modulo \(2\pi\).
The other cosine identity requires
\[
2\theta/p+2\beta+2\pi(j+l)/p\in2\pi\mathbb Z,
\]
which has only finitely many solutions in the chosen interval.
There are only finitely many pairs, and the same argument applies to the second marginal.
Off this finite exceptional set their atom masses are exactly \(1/p\) and \(1/q\).

The scalar free additive atom criterion says that an output atom must be a sum of two input atoms whose masses have sum strictly larger than one, and its mass is that sum minus one.
This is the scalar statement recalled precisely in [BBL21, arXiv v2, Introduction, PDF p.1](../literature/pdf/BBL21--arxiv-v2.pdf#page=1), attributed there to Bercovici--Voiculescu.
It is also the scalar-base specialization of its prepared tracial atom mechanism.
Here
\[
\frac1p+\frac1q\le1,
\]
so \(\mu_{X_\theta}\) has no atom at any real point outside the finite exceptional set.
Equation (5) proves
\[
\boxed{\dim_G\ker(X-\lambda)=0\quad
       \text{for every }\lambda\in\mathbb R.}
\tag{8}
\]
The strict threshold matters when \(p=q=2\); equality of the two masses with total one still produces no atom.
If exactly one of \(c,d_0\) is zero, (8) follows directly from the already established cyclic rational/Fourier calculation for the other infinite-order generator.
If both vanish, \(X=0\) is the elementary exceptional case.

This is a complete scalar boundary argument using the actual winding variable and free conditional factor laws.
It is stronger than merely verifying that a proposed zero-one word kernel comes from a torsion-free quotient, but it retains substantial central-amalgam and scalar-additive structure.

## The mixed-power test and its fractional quotient atoms

Take \(p=2,q=3,c=d_0=1\), so
\[
G=\langle a,b\mid a^2=b^3\rangle,\qquad
X=a+a^{-1}+b+b^{-1}.
\tag{9}
\]
At \(\theta=0\), equivalently after setting the central winding variable to one, the representation factors through \(C_2*C_3\).
Its marginal laws are
\[
\mu_{a,0}=\tfrac12\delta_2+\tfrac12\delta_{-2},
\qquad
\mu_{b,0}=\tfrac13\delta_2+\tfrac23\delta_{-1}.
\]
The same exact free atom criterion gives
\[
\mu_{X_0}(\{1\})=\mu_{X_0}(\{-3\})=\tfrac16,
\tag{10}
\]
and no other atoms.
Thus the torsion quotient has genuine fractional scalar atoms.

At \(\theta=\pi\), the first summand is identically zero and the second has law
\[
\mu_{X_\pi}=\tfrac23\delta_1+\tfrac13\delta_{-2}.
\tag{11}
\]
This fiber is entirely atomic.
Outside \(\theta\in\{0,\pi\}\) modulo \(2\pi\), both marginal supports are distinct and their maximal masses sum to \(5/6\), so the fiber law is atomless.
Nevertheless, the actual \(G\)-law has no atoms by (5).
A fractional atom at a quotient fiber, even an entirely atomic exceptional fiber, contributes zero to the original canonical group trace unless it persists on a set of positive Haar measure.

This explicitly refutes the proposed inference that an atom of the zero-winding quotient must survive a torsion-free central lift.
It also shows why the specialization \(q=1\) in a winding series cannot replace the constant-winding-coefficient extraction.
In the normal-form notation, the former counts every central power, while the latter counts only the actual identity.
The finite exceptional fibers do not violate torsion-freeness of \(G\); they are nonfaithful quotient representations, and their individual traces are not \(\tau_G\).

## Known coverage and what this test does not establish

The positive scalar conclusion (8) does not provide new coverage beyond the retained height mechanism.
For the concrete mixed-power test, (1) assigns heights \(3\) and \(2\) to \(a,b\).
In \(X-\lambda\), the highest nonzero support term is a single scalar multiple of a group unit, so the [singleton extreme-support criterion](../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) already proves (8).
For unequal general \(p,q\), the same reasoning applies.
For \(p=q\), the extreme coefficient is a nonzero binomial in the distinct group elements \(a,b\), hence is independently a cyclic unit by torsion-freeness before invoking the [graded extreme-coefficient mechanism](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials).
The normal form ensures \(a\ne b\).
The winding calculation is consequently an alternative exact trace mechanism and a quotient-transfer obstruction, not a new scalar Atiyah theorem.

The joint constraint used here is stronger and more concrete than the root-closed positive language in [L_A0016](../ledger/Yin_L_A0016_v1.md#even-cyclic-root-closure-and-positive-moments-do-not-suffice): it retains actual inverse relations, alternating normal forms, the common central power and the full family of positive tracial representations in (2).
These data permit both the exact trace identity and the independent free atom test.
There is no general construction of such fiber laws for arbitrary torsion-free groups.

For general matrix group-ring inputs, (3)--(5) still give exact trace and atom disintegration with unnormalized matrix traces.
They do not quantize the fiber masses or their integral.
The scalar marginal threshold argument does not apply to arbitrary matrix polynomials, and fiber atoms could in principle persist with uncontrolled trace.
Extending this calculation requires a new actual matrix-kernel constraint, not more expansion of the same scalar generating series.
Similarly, a fiber atom moving with \(\theta\) requires an actual argument about its level sets; nonconstancy or analyticity of a scalar entry alone does not certify that matrix rank behavior.
The present test has no unresolved boundary passage because atomlessness holds at every real value in almost every fiber.

## Source scope and continuation decision

The preparation first reused L_A0015--L_A0018, the existing BBL21 source unit and the AER26 source content map.
A bounded primary-source check on 12 November 2026 read AER26 v1, Definition 1.3, Lemma 3.1, Corollary 3.2, Definition 3.3 and Section 3.1, plus the identification of the \((2,3)\) presentation in Section 8.2.
Those passages provide attribution for the central normal form and winding formulation.
The unresolved general local-limit and cogrowth-asymptotic passages already excluded in L_A0017 are not used.
The matching [BBL21 arXiv v2 HTML Introduction](https://arxiv.org/html/1903.09002v2#S1) was read directly for the complete scalar atom criterion, including its strict threshold and exact mass.
That standard analytic theorem is an accepted source input here; its historical proof and the full BBL21 paper were not re-audited.
No separate new source or exhaustive novelty search is claimed.

This bounded discriminator is complete at its stated scalar scope.
Further work on this same scalar central-amalgam family would duplicate a resolved height case.
A useful continuation must instead exhibit an actual matrix or noncentral relation family for which the full joint trace data yield a verifiable kernel constraint not already supplied by the cyclic, graded, energy or known division-coefficient certificates.
The exact exceptional-fiber calculation remains useful when screening a proposed transfer from a torsion quotient or a specialization of a multivariate return series.
