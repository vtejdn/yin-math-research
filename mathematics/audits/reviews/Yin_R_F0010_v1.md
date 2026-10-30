---
author: Yin
---

# Yin_C_F0022 - Complete Artifact Review of the Conjugate-Variable Extension

<a id="conjugate-variable-extension-finding"></a>

## Actual review relationship

The reviewer supplied the preliminary contraction/domain/cutoff route and authored its Dab10-U002 interface, then suggested and checked the displayed domain-corollary material. This substantive contribution to the reviewed proof makes the retained whole finding self-reviewed.
The original independent descriptions, dates and full checked scope are preserved as historical facts; no isolated arrangement or new review is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Retained complete finding](#conjugate-variable-extension-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Retained complete finding](#conjugate-variable-extension-finding) | [Exact statement](../../claims/Yin_C_F0022_v1.md#statement) | Entire selfadjoint finite-Fisher affiliated criterion, actual all-bounded-vector dual/adjoint domains, regular-cutoff cancellation, both implications, fraction independence and both final bounded-element formulations, with original source-depth limits. |
| [Retained complete finding](#conjugate-variable-extension-finding) | [Exact argument](../../claims/Yin_C_F0022_v1.md#yin_c_f0022) | Entire selfadjoint finite-Fisher affiliated criterion, actual all-bounded-vector dual/adjoint domains, regular-cutoff cancellation, both implications, fraction independence and both final bounded-element formulations, with original source-depth limits. |

- Date and reviewer: 2026-09-09; the reviewing agent.
- Target: [Yin_C_F0022](../../claims/Yin_C_F0022_v1.md#yin_c_f0022), Sections 1-8, authored by the coordinating agent.
- Disclosure: the reviewer supplied the preliminary contraction/domain/cutoff route and authored the source interface Dab10-U002, but did not author the target theorem file.
  This is a separate full artifact review with that involvement disclosed, not a claim of independent rediscovery.
  Dab10-U002 itself received a separate complete review by another AI agent against the primary source.
- Scope: the whole written proof, including source hypotheses, all operator domains, both implications, fraction independence, the bounded-element weak test, and exclusions of stronger conclusions.
- Outcome: the theorem is correct within its stated selfadjoint and finite-Fisher hypotheses, including both bounded-element formulations in the final artifact.
  No mathematical correction was required; the recommended explanatory insertion and the author's domain-corollary addition have been checked in the final review supplement below.
  The responsible Claim materials and their selected decisions own the current mathematical and review assessments.

## Backward Obligations and Forward Evidence

| Obligation | Evidence checked | Finding |
| --- | --- | --- |
| Canonical unbounded dual is well defined and closable | Conjugacy yields $D_i^*p=p\xi_i-D_i^0p$ on dense polynomials | Correct tensor leg and adjoint convention |
| Every bounded numerator/denominator acts inside the required domain | Dab10's infinity-to-$L^2$ estimate and weakly closed graphs give $M\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*$ | Correct actual Hilbert closure; no arbitrary extension |
| Cleared defects make sense on a fixed common core | $sD_i(bz)-aD_i(tz)$ is defined for all $z\in M$ | Correct |
| Finite algebraic rank becomes bounded operator rank | The displayed adjoint domain makes each defect closable; a finite-dimensional-coordinate argument then gives boundedness | Correct |
| Some fractions are equivalent to every fraction | Common regular multiples plus bounded regular spectral cutoffs replace naive dense-range cancellation | Correct; no inverse is presumed bounded |
| Rational elements have finite defects | Sum, product, and unit-inverse identities hold on the invariant vector space $M$ | Correct |
| A fundamental identity holds beyond polynomial vectors | Normalization gives $\sum_i[\rho(X_i),D_i]=(1-d)I-P$ on polynomials; bounded-set weak continuity extends it to $M$ | Correct; Fuglede is unnecessary here |
| Finite defects imply affiliated rationality | The bounded finite-rank identity gives an algebraic tensor identity, balanced descent, and the division-ring equalizer contradiction | Correct |
| Weak polynomial tests match the bounded-element criterion | Density in the first variable and bounded polynomial approximation in the second recover the $M$-core commutator | Correct |
| Source and model scope are retained | Finite Fisher supplies maximal Delta; $d=1$ reduces to a free two-variable extension; nonselfadjoint and raw-$L^2$ variants are not asserted | Correct |

## The Analytic Steps Are Sufficient

For each $x\in M$, uniformly bounded polynomial approximants converge to $x$ in $L^2$.
Both their $D_i^0$ images and polynomial-adjoint images are bounded in $H$.
Weak compactness and weak closedness of the two closed graphs give precisely the actual closure values at $x$.
The adjoint is already closed, so its graph needs no new choice of extension.
The constants $4\|\xi_i\|_2$ and $5\|\xi_i\|_2$ follow from the selfadjoint estimate and splitting a complex polynomial into its real and imaginary parts.
They need not be optimal.

The bounded-net continuity proof pairs against the dense adjoint domain and uses the uniform Hilbert bound to extend convergence to all test vectors.
This avoids assuming convergence in operator norm, graph norm, or even strong convergence of the contracted derivatives.
It also applies after each fixed bounded coefficient in a defect.

The adjoint formula for the defect,
\[
T_i^*\eta=b^*D_i^*(s^*\eta)-t^*D_i^*(a^*\eta),\qquad\eta\in M,
\]
has the correct factor order and makes its adjoint domain dense.
The finite-rank lemma is valid: the orthogonal projection of a dense linear adjoint domain onto a finite-dimensional range is the whole range, so every range coordinate has an $H$-continuous representing vector.

The regular-cutoff argument addresses the substantial extra issue caused by an unbounded dual.
For regular $y'=v|y'|$, the polar partial isometry is unitary in the finite algebra, and
\[
y'\bigl(|y'|^{-1}1_{[1/n,\infty)}(|y'|)v^*z\bigr)
=v1_{[1/n,\infty)}(|y'|)v^*z
\]
is uniformly bounded in operator norm and converges to $z$ in $L^2$.
Although its preimages may have large norms, the continuity is used on the displayed images, exactly where the uniform bound holds.
Their defect values remain in a fixed finite-dimensional space, whose weak closedness gives finite rank at every bounded vector.
This is not the invalid inference that the range of a regular multiplier is a graph core for an arbitrary closed operator.

## Both Algebraic Directions Remain Valid

The common-multiple identities and product expansion were checked with every multiplication side retained.
All inputs of $D_i$ in those formulas are bounded vectors.
No commutator with a newly chosen denominator is introduced, and no infinite series or unbounded product is differentiated.
The inverse step only applies to units of the affiliated algebra, and correctly makes the two old numerators regular.
Thus the finite-defect class is an inverse-closed algebra containing the generators.

For the reverse direction, the vacuum value of $K+P$ is $(1-d)\Omega$.
Its exact algebraic commutation with every polynomial therefore identifies it on the polynomial cyclic domain.
The extension to $M$ uses the continuity already proved, and the cleared identity has the correct sign:
\[
\sum_i[\rho(X_i),T_i]=aPt-sPb.
\]
After finite rank is known, both sides are bounded, so extension from $M$ to $H$ is legitimate.

The conversion to $a\otimes t-s\otimes b$ uses the algebraic $L^2$ tensor product, followed by its injective inclusion into $U\otimes_{\mathbb C}U$.
Balancing over the division subring $F$ kills the right-multiplication differences.
The outer actions by $s^{-1}$ and $t^{-1}$ preserve the relevant module structures.
The final basis-functional argument only needs that $F$ is a division ring, and does not require $U$ itself to have no zero divisors.

The maximal-Delta input is obtained from existence of conjugate variables, not from the as-yet unproved boundedness of the canonical dual.
The proof therefore has no circular use of Yin_C_F0013's bounded-dual hypothesis.

## Clarification Recommended and Verification Limits

The reviewed text's Section 5 invokes the polynomial dual relation for generator membership on the common domain $M$.
Section 3 already proves all ingredients of its extension, but an explicit sentence is useful:
apply uniformly bounded polynomial approximation and equation (10) to conclude $[D_i,X_j]=\delta_{ij}P$ on $M$.
This is an explanatory insertion, not a missing analytic hypothesis or change of theorem.

The bounded-output criterion can additionally be stated as invariance of $\operatorname{Dom}D_i$ and a finite-rank bounded commutator there.
Indeed $M$ is a graph core for $D_i$, and a bounded extension of $[D_i,f]|_M$ passes to graph limits by closedness.
That optional strengthening was suggested to the author but is not required by the reviewed statement.

The review retains the original source foundations for conjugacy, closed real derivations, maximal Delta, and finite tracial affiliated fractions.
It is not a full new audit of Voi98, CS05, or MSY23, a formal proof, a numerical experiment, external human review, or a novelty determination.
No full-domain affiliated commutator or cofinite-domain formulation was silently inferred.

## Final Artifact Supplement

The reviewer reread the entire final artifact after the author made the following additions.

1. At the end of Section 3, the individual generator relation is explicitly extended from $A$ to $M$ using uniformly bounded polynomial approximation.
   Both $D_i(X_jp_n)$ and $X_jD_ip_n$ have the asserted weak limits by equation (10), while $Pp_n\to Pz$ strongly.
   Thus this addition supplies exactly the previously recommended explanation and is correct.
2. The statement and the end of Section 7 now include the full closed-domain formulation for bounded $f$.
   Because $A$ is a core by definition of $D_i$, any intermediate domain $A\subseteq M\subseteq\operatorname{Dom}D_i$ is also a core.
   For graph approximants $z_n\in M$, boundedness of $f$ and the finite-rank extension $T_i$ gives convergence of both $fz_n$ and $D_i(fz_n)=fD_iz_n+T_iz_n$.
   Closedness yields $f\operatorname{Dom}D_i\subseteq\operatorname{Dom}D_i$ and the desired identity there.
   Restriction proves the reverse implication.
   No uniform operator-norm bound on these graph approximants is required at this stage, since $T_i$ has already been proved bounded on $H$.
3. The closing review paragraph now links to this audit, with no mathematical change to the proved theorem.

The final artifact is accepted in full.
