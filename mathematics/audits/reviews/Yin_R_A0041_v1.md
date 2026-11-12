---
author: Yin
---
# Independent review of polynomial localization and spectral-mass bounds

## Review arrangement and inputs

The review was performed at 2026-11-12T13:11 for Yin by a separately assigned agent outside the substantive development of this argument.
The reviewer received the fixed [Claim](../../claims/Yin_C_A0014_v1.md), the requested whole-proof scope and applicable repository rules.
No development discussion, exploration draft, author explanation or prior project-review conclusion was supplied or consulted.
The mathematical inputs inspected were the Claim's complete Statement, Argument and What has and has not been reduced sections, together with the exact source interfaces in [Sim08](../literature/Sim08/Yin_U001.md#christoffel-variational-principle), [its moment-inverse formula](../literature/Sim08/Yin_U001.md#abc-moment-inverse) and [BCM04](../literature/BCM04/Yin_U001.md#amenable-projective-trace).
This review identifies the working revision of physical v1 read on 2026-11-12, including equation (8a).
It does not cover any later substantive alteration merely because the path remains unchanged.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole argument](#whole-argument) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole argument](#whole-argument) | [Statement](../../claims/Yin_C_A0014_v1.md#statement) | All stated hypotheses, definitions and conclusions, including (1)–(10) and the critical restriction (8a). |
| [Whole argument](#whole-argument) | [Argument](../../claims/Yin_C_A0014_v1.md#argument) | Complete proof, including the external scalar-idempotent interface, singular and nonsingular moment cases, rounding obstruction and all rate estimates. |
| [Whole argument](#whole-argument) | [Scope](../../claims/Yin_C_A0014_v1.md#what-has-and-has-not-been-reduced) | Conditional and necessary character of the conclusions, distinction between a kernel atom and continuous spectrum, and absence of a general amenable-group solution claim. |

<a id="whole-argument"></a>
## Finding: whole argument

**The stated mathematical conclusions are supported at their exact conditional scope.**
The following checks cover every substantive step of the selected proof.

For \(a\ne0\), faithfulness of the regular representation gives \(H\ne0\) and \(M>0\), while \(p=1\) would imply \(H=0\).
Thus \(\alpha<1\) is justified.
The Cauchy-residue convention is correct: the integrand \(i\eta/(i\eta-x)\) has modulus at most one and converges pointwise to \(1_{\{0\}}(x)\).
Dominated convergence supplies the stated limit, without a density assumption on the positive spectral part.

The constrained polynomial images form a nonempty affine subspace of a finite-dimensional subspace of \(L^2(\mu)\), so a unique minimizing vector exists even when polynomial representatives are nonunique.
Variation by complex multiples of any polynomial vanishing at zero gives full complex orthogonality.
Applying it to \(f_n-f_m\) proves the exact norm-increment identity (2).
The trial polynomials \((1-x/M)^n\) prove convergence to the atom, and the value at zero proves the exact error (11).
Finite propagation gives the radius \(2^{j+1}w\) for each dyadic difference.
Coefficient Cauchy–Schwarz then turns (3) into a convergent series in \(\ell^1(G)\), with the same \(L^2\) limit as the kernel projection.
Equality on \(\delta_e\), followed by commutation with right translations, identifies the resulting regular operator with \(p\).
The accepted scalar-idempotent theorem therefore forces \(p=0\), and \(\ker(a^*a)=\ker(a)\) gives the asserted injectivity.

Infinite support makes every nonzero polynomial have positive squared norm, so the ordinary moment inverse in (4) is legitimate.
Constrained quadratic minimization gives both displayed formulas with the stated degree convention.
For finite support, the spectral support equals the operator spectrum because the canonical trace is faithful.
Interpolation on that finite set makes the kernel projection a polynomial in \(H\); the same idempotent theorem eliminates it.
No singular inverse or extension of the source's nonsingular formula is used.

In the rounding argument, \(\|4d\|_{\ell^1}<1\) makes the inverse-square-root series converge in the unital Banach algebra.
Its algebraic square identity and commutation with \(q\) prove that (13) is an idempotent.
In the regular representation the series is the positive inverse square root, since the operator defect has norm less than \(1/4\).
Thus (13) is exactly the upper spectral projection and is nontrivial whenever the spectrum meets both sides of \(1/2\).
The contradiction applies to this \(\ell^1\) idempotent, without requiring spectral invariance of \(\ell^1(G)\) or a reduced-\(C^*\)-algebra projection theorem.

The finite Fourier identity in (14) has the correct normalization and degree \(m-1\).
The bound by one follows from \(\lvert\sin(mt)\rvert\le m\lvert\sin t\rvert\), and the other bound follows from the numerator bound by one.
At \(M\), parity gives precisely zero or \(1/m^2\).
As \(M\in\sigma(H)\), the hypothesis \(0\in\sigma(H)\) therefore puts both required spectral values in \(F_m(H)^k\).
Its defect has propagation radius \(2k(m-1)w\), yielding the factor \(16V(2Nw)\) in (7).
The integrand vanishes at zero, so this estimate neither assumes nor detects a positive atom there.

For the power estimate, the dyadic positive-spectrum pieces give a convergent geometric sum precisely when \(2k>\beta\).
The degree choice \(m=\lfloor n/k\rfloor+1\) preserves admissibility and gives \(\lambda_n-\alpha=O(n^{-2\beta})\).
The summands in (3) are consequently \(O(2^{j(D/2-\beta)})\).
The same filters have defect integral at most their positive-spectrum squared norm, while (7) gives a lower bound of order \(m^{-D}\).
This proves the stronger spectral exclusion when \(2\beta>D\), including the possible continuous-spectrum case.

For (8a), put \(s:=D/2>0\) and \(t:=M/m^2\), and fix \(k\) with \(2k>s\).
If \(\mu((0,u])=o(u^s)\), then for any \(\eta>0\) the distribution is bounded by \(\eta u^s\) below a fixed \(\varepsilon_0>0\).
On dyadic intervals with upper endpoint below \(\varepsilon_0\), the squared filter bound gives at most a constant times \(\eta t^s\sum_{j\ge0}2^{j(s-2k)}\).
The single interval crossing \(\varepsilon_0\) is split there: its lower part is bounded using \(\mu((0,\varepsilon_0])\le\eta\varepsilon_0^s\), and its upper part belongs to the remaining tail.
The crossing lower part obeys the same geometric bound because its lower endpoint lies between \(\varepsilon_0/2\) and \(\varepsilon_0\).
On the tail above \(\varepsilon_0\), the squared filter is \(O_{\varepsilon_0}(m^{-4k})\).
Hence the positive-spectrum squared norm, and therefore the defect integral in (7), is \(o(m^{-D})\), contradicting its lower bound.
For the nonnegative distribution ratio, failure of this little-oh condition is exactly the stated strictly positive limsup.

For the stretched exponential estimate, \(\theta:=2\beta/(2\beta+1)\) satisfies \(2\beta(1-\theta)=\theta\).
Integer choices \(k\asymp n^\theta\), \(m\asymp n^{1-\theta}\) can have \(k(m-1)\le n\) and \(m\to\infty\).
The split at \(4M/m^2\) gives the two bounds \(\exp(-c' m^{2\beta})\) and \(16^{-k}\), each of order at most \(C\exp(-c''n^\theta)\).
The volume contribution has order \(\exp(Cn^\kappa)\), so the strict condition \(\kappa<\theta\) proves both summability and contradiction with (7) if zero were spectral.
No endpoint equality is asserted.

## Source completeness and limits

The Christoffel attribution and nonsingular matrix convention match the exact source statements recorded in Sim08.
The Claim supplies its own elementary derivations of the variational identities and atom limit, avoiding the source-display defects recorded in that unit.
The BCM04 source unit records the published theorem chain and the trace comparison on \(K_0(\ell^1(G))\), which supplies the precise scalar-idempotent input for torsion-free amenable \(G\).
The group hypotheses here meet that interface.
Those existing primary-source inspections are reused as established external theorem evidence; this review did not re-audit the assembly-theoretic proofs or reread the original PDFs.
There is no unresolved source-applicability issue for the selected deductions at that boundary.

The review establishes conditional certificates and necessary spectral-distribution restrictions, not the missing tail estimates for arbitrary group-ring elements.
It does not establish a converse, an optimal exponent, new group-class coverage or completion of A0001.
The exclusions of zero from the whole spectrum are stronger than injectivity and are correctly distinguished from it.
No computation or proof-assistant formalization is claimed.
