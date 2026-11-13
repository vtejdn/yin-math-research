---
author: Yin
---
# Independent review of the two-point-modulus counterexample to bare full-domain duality

## Whole-proof finding

At 2026-11-13T16:07 UTC a separately assigned agent checked the [statement](../../claims/Yin_C_F0225_v1.md#statement) and [complete argument](../../claims/Yin_C_F0225_v1.md#argument) fixed by the [16:04 candidate decision](../../claims/Yin_C_F0225_v1.md#decision-candidate).
The reviewer had worked on other single-generator models in the same Task and knew the pre-existing ratio criterion and free-extension method.
The reviewer had also seen a status summary mentioning a general singular-projection test.
The reviewer did not participate in the two-point-modulus construction or receive its proof-development dialogue, draft, coefficient calculations, or a prior review finding about this candidate.
The fixed candidate, the Task definitions and the fixed theorem inputs supplied the mathematical review materials.
The argument establishes the full candidate, including the failure of algebraic bare duality after augmentation.

### Core, descent and adjoint

The two distinct values \(\varepsilon^2,1\) of \(X^*X\) recover \(p\) by a polynomial, then \(s,h^{-1},u\), and hence \(u^{-1}=u^*\), all in the generated star algebra.
Conversely \(X,X^*\in\mathbb C G\), so the represented domain is exactly \(\mathbb C G\), which is dense in the group trace Hilbert space.
In its faithful left representation, applying a group-algebra element to the identity basis vector verifies linear independence of the group basis.
Both inverse relations follow from \(\delta u^{-1}=-u^{-1}(\delta u)u^{-1}\) with its separate left and right outer actions.
The left \(q\) and right \(p\) in \(\delta p\) have opposite \(s\)-eigenvalues, so \(s\delta s+(\delta s)s=0\).
These exhaust the presentation relators and give descent of the complex-linear derivation, including its value on the represented \(X^*\).
In \((\delta u)h\) the two right multipliers give \(q\) and \(\varepsilon p\), respectively.
The other Leibniz term is \(2uqu^{-1}\otimes p=(1-t)\otimes p\), so the two \(t\) terms cancel and \(\delta X=1\otimes1\).

For a group-tensor \(a\otimes b\) in a marked positive cut the traces impose \(P=a^{-1}\) and \(Q=b^{-1}\) on the reduced prefix and suffix.
The negative cut has tensor \(-u^{-1}a\otimes b u^{-1}\), imposing \(P=a^{-1}u,\ Q=ub^{-1}\).
Since \(b\in\{1,s\}\), both allowable negative suffixes start with \(u\) and contradict reducedness after \(u^{-1}\).
In the positive cuts from the singular coefficient \(a=t\), the required prefix \(t^{-1}=usu^{-1}\) contradicts reducedness before \(u\).
The positive cuts with \(a=1\) contribute \(1/2\) at \(u\) and \(-1/2\) at \(us\).
For the \(s\)-cuts, \(2\delta p=-(u^{-1}-su^{-1})\otimes(1+s)/(1-\varepsilon)\).
A required suffix \(s\) or prefix \(us\) would put two \(s\)'s together.
Only \(P=u,\ Q=1\) survives, adding \(-1/(1-\varepsilon)\) at \(us\).
This tests all cuts in every reduced word, including the empty word by \(\delta1=0\).
The two real coefficients therefore represent the trace functional in the stated Hilbert convention.
Their squared sum is at most \(1/4+(5/2)^2=13/2\).
By linearity this is a bounded functional of the Hilbert norm of the input throughout the dense represented star core, giving the actual Hilbert adjoint at \(1\otimes1\).
As a normalization check, pairing this vector with \(X=((1+\varepsilon)u+(\varepsilon-1)us)/2\) gives one.

### Lower bound and the two distinct existential conclusions

The projections \(p\) and \(f=upu^{-1}\) have trace \(1/2\), and \(Xp=fX=\varepsilon up\) has operator norm \(\varepsilon\).
Thus evaluation of \([E,L_X]=P_\Omega\) at \(p\), followed by left multiplication by \(f\), has Hilbert norm \(1/(2\sqrt2)\).
For every bounded solution its two terms are bounded by \(\varepsilon\|E\|\) each, using the actual operator norm at the input \(Xp\) and the bounded left action of \(fX\) at the output \(E(p)\).
Nothing in this estimate restricts \(E(1)\).

At \(\varepsilon_n=2^{-n}\) the generators have norm one, the exhibited actual vacua have uniformly bounded norms, and each \(\delta_n(X_n^*)\) is a finite sum of coarse group tensors.
Consequently the [C_F0210 v1 criterion](../../claims/Yin_C_F0210_v1.md#statement) applies with unbounded \(\beta(X_n)/(1+\|\xi_n\|_2)\), including its alternative when some individual cost is already infinite.
Its assembly permits unbounded starred costs across the sequence and yields one bounded generator of infinite bounded-dual cost with actual ACSY.
The [C_F0205 v1 free extension](../../claims/Yin_C_F0205_v1.md#statement) preserves actual ACSY for both coordinates after adjoining a free semicircular element.
For this enlarged tuple a full algebraic system implies bounded old-coordinate witnesses, whose restrictions and conditional-expectation compressions would give a bounded old-coordinate witness on the original algebra.
This contradicts the assembled infinite cost and excludes every enlarged algebraic system.
Negating the witness matches the Task's generator-first commutator sign, and restriction of a system with both full domains gives a bare system.
These are the two existential conclusions at their stated lengths.
The review uses the independently reviewed [assembly theorem](Yin_R_F0218_v1.md#whole-proof-finding) and [free extension theorem](Yin_R_F0213_v1.md#whole-proof-finding) at those interfaces.
The normal-tuple branch and the existence of an unbounded algebraic witness for an individual unaugmented single generator are outside this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0225_v1.md#statement) | Individual group-ring witnesses and exact constants, one bounded generator of infinite bounded cost, two-coordinate failure of both full-domain conditions. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0225_v1.md#argument) | Core equality, group relators and inverse legs, all reduced-word trace tests, actual adjoint, projection lower bound, assembly and algebraic exclusion. |
| [Whole-proof finding](#whole-proof-finding) | [Ratio criterion](../../claims/Yin_C_F0210_v1.md#statement) | Effective unit cutoff and diverging ratio of bounded cost to one plus actual vacuum norm, individually finite starred costs, and the assembled single generator. |
| [Whole-proof finding](#whole-proof-finding) | [Free extension](../../claims/Yin_C_F0205_v1.md#statement) | Preservation of actual ACSY, bounded-witness compression and exclusion of all algebraic systems after adding one free semicircular coordinate. |
| [Whole-proof finding](#whole-proof-finding) | [Task definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Outer actions, actual adjoint-domain requirement, both full-domain definitions and the generator-first sign. |
| [Whole-proof finding](#whole-proof-finding) | [Bounded cost](../../claims/Yin_C_F0201_v1.md#statement) | Operator-norm input, Hilbert-space output, unrestricted vacuum value and opposite commutator sign in the bounded-dual convention. |
